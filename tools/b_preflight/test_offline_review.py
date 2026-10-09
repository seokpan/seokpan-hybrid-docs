"""Negative fixtures test semantic swaps, dangerous Plan actions, and safe diagnostics."""
import ast
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from offline_review import BASE, SG_CONTRACT, Invalid, plan_review, read_json, sg_review, validate_file_stat
from types import SimpleNamespace
from unittest.mock import patch
import offline_review

HERE = Path(__file__).parent

def sg_fixture():
    ids = {'mariadb': 'sg-00000001', 'redis': 'sg-00000002'}
    inputs = {'foundation': {'account_id': '111111111111', 'vpc_id': 'vpc-00000001', 'data_security_groups': ids}}
    outputs = {SG_CONTRACT[key][0]: {'value': value, 'sensitive': False} for key, value in ids.items()}
    groups = {'SecurityGroups': [{'GroupId': value, 'GroupName': SG_CONTRACT[key][1], 'VpcId': 'vpc-00000001', 'OwnerId': '111111111111', 'Tags': [{'Key': 'Component', 'Value': 'data'}]} for key, value in ids.items()]}
    return inputs, outputs, groups

def plan_fixture(cluster=True):
    changes = []
    for base, count in BASE.items():
        kind, name = base.split('.')
        for index in range(count):
            keyed = base in ('aws_iam_role.operator', 'aws_iam_role_policy_attachment.operator')
            key = 'MOCK_OPERATOR_' + str(index)
            row = {'mode': 'managed', 'type': kind, 'name': name, 'address': base + ('["' + key + '"]' if keyed else ''), 'change': {'actions': ['create'], 'before': None, 'after': {'sensitive_placeholder': 'DO_NOT_ECHO'}}}
            if keyed: row['index'] = key
            changes.append(row)
    if cluster:
        changes.append({'mode': 'managed', 'type': 'rhcs_cluster_rosa_classic', 'name': 'cluster', 'index': 0, 'address': 'rhcs_cluster_rosa_classic.cluster[0]', 'change': {'actions': ['create'], 'before': None}})
    return {'format_version': '1.2', 'terraform_version': '1.16.4', 'complete': True, 'errored': False, 'applyable': True,
            'variables': {'cluster_enabled': {'value': cluster}, 'worker_sg_binding': {'value': None}},
            'checks': [{'status': 'pass'}], 'resource_changes': changes}

class ReviewTests(unittest.TestCase):
    def test_reference_metadata_and_python39(self):
        # Pinned metadata identifies the Source read during preparation. This
        # offline test does not claim a new network/source authenticity check.
        record = json.loads((HERE / 'source-reference.json').read_text())
        self.assertEqual(record['source_head'], 'aaa8cff09cd70298b142afdba5faf15d73664cc3')
        self.assertEqual(record['operator_count_guard'], 6)
        self.assertEqual(set(record['managed_resource_declarations']), set(BASE) | {'rhcs_cluster_rosa_classic.cluster', 'aws_vpc_security_group_ingress_rule.worker_to_data'})
        self.assertEqual(len(record['files']), 5)
        self.assertTrue(all(re.fullmatch('[0-9a-f]{64}', f['sha256']) for f in record['files']))
        self.assertFalse(record['actual_plan_or_sg_handoff_received'])
        ast.parse((HERE / 'offline_review.py').read_text(encoding='utf-8-sig'), feature_version=(3, 9))

    def test_correct_sg_and_swap(self):
        original = sg_fixture()
        self.assertEqual(sg_review(*original)['result'], 'CONSISTENT_PENDING_HANDOFF_REVIEW')
        # Both the output-name mapping and input map are consistently swapped:
        # same VPC, two distinct valid IDs still must fail GroupName semantics.
        inputs, outputs, groups = deepcopy(original)
        mapping = inputs['foundation']['data_security_groups']
        mapping['mariadb'], mapping['redis'] = mapping['redis'], mapping['mariadb']
        for key in mapping: outputs[SG_CONTRACT[key][0]]['value'] = mapping[key]
        self.assertIn('SG_PURPOSE_NAME_MISMATCH', sg_review(inputs, outputs, groups)['reason_codes'])

    def test_sg_negative_cases(self):
        for name, mutate, code in [
            ('wrong_vpc', lambda i,o,g: g['SecurityGroups'][0].update(VpcId='vpc-00000002'), 'SG_VPC_MISMATCH'),
            ('wrong_account', lambda i,o,g: g['SecurityGroups'][0].update(OwnerId='222222222222'), 'SG_PROJECT_ACCOUNT_MISMATCH'),
            ('wrong_component', lambda i,o,g: g['SecurityGroups'][0]['Tags'][0].update(Value='rosa'), 'SG_COMPONENT_TAG_MISMATCH'),
            ('duplicate_component', lambda i,o,g: g['SecurityGroups'][0]['Tags'].append({'Key':'Component','Value':'data'}), 'SG_COMPONENT_TAG_MISMATCH'),
            ('duplicate_id', lambda i,o,g: i['foundation']['data_security_groups'].update(redis='sg-00000001'), 'DATA_SG_IDS_NOT_DISTINCT'),
            ('output_swap_only', lambda i,o,g: o['rds_security_group_id'].update(value='sg-00000002'), 'OUTPUT_TO_INPUT_MAPPING_MISMATCH'),
            ('sensitive_output', lambda i,o,g: o['rds_security_group_id'].update(sensitive=True), 'OUTPUT_SENSITIVITY_UNCONFIRMED'),
            ('unobserved_id', lambda i,o,g: i['foundation']['data_security_groups'].update(mariadb='sg-00000003'), 'SUPPLIED_SG_NOT_OBSERVED'),
        ]:
            with self.subTest(name=name):
                fixture = deepcopy(sg_fixture()); mutate(*fixture)
                result = sg_review(*fixture)
                self.assertEqual(result['result'], 'BLOCKED'); self.assertIn(code, result['reason_codes'])

    def test_plan_stage_and_pending_checks(self):
        for cluster, stage in [(True, 'cluster-create'), (False, 'iam-oidc-preparation')]:
            with self.subTest(stage=stage):
                plan = plan_fixture(cluster)
                self.assertEqual(plan_review(plan, stage)['result'], 'NO_LISTED_ANOMALY_PENDING_REVIEW')
                plan['checks'][0]['status'] = 'unknown'
                result = plan_review(plan, stage)
                self.assertEqual(result['result'], 'NO_LISTED_ANOMALY_PENDING_REVIEW')
                self.assertIn('CHECKS_PENDING_APPLY', result['pending_codes'])
                self.assertIn('DATA_READ_COMPLETENESS_REVIEW', result['pending_codes'])
                self.assertIn('full-root command receipt', ' '.join(result['not_verified']))

    def test_dangerous_plan_cases(self):
        def add_foreign(plan):
            plan['resource_changes'].append({'mode':'managed','address':'aws_security_group.foundation','type':'aws_security_group','name':'foundation','change':{'actions':['create']}})
        def wrong_attachment(plan):
            row = next(r for r in plan['resource_changes'] if r['type'] == 'aws_iam_role_policy_attachment')
            row.update(index='MOCK_DIFFERENT', address='aws_iam_role_policy_attachment.operator["MOCK_DIFFERENT"]')
        cases = [
            ('delete', lambda p: p['resource_changes'][0]['change'].update(actions=['delete']), 'DELETION_PRESENT'),
            ('replace_delete_first', lambda p: p['resource_changes'][0]['change'].update(actions=['delete','create']), 'REPLACEMENT_PRESENT'),
            ('replace_create_first', lambda p: p['resource_changes'][0]['change'].update(actions=['create','delete']), 'REPLACEMENT_PRESENT'),
            ('update', lambda p: p['resource_changes'][0]['change'].update(actions=['update']), 'UPDATE_REQUIRES_SEPARATE_REVIEW'),
            ('foreign_foundation', add_foreign, 'RESOURCE_OUTSIDE_FIRST_ROSA_SCOPE'),
            ('missing_operator', lambda p: p['resource_changes'].pop(3), 'EXPECTED_RESOURCE_COUNTS_MISMATCH'),
            ('attachment_other_key', wrong_attachment, 'OPERATOR_ROLE_ATTACHMENT_KEY_MISMATCH'),
            ('duplicate', lambda p: p['resource_changes'].append(deepcopy(p['resource_changes'][0])), 'DUPLICATE_RESOURCE_ADDRESS'),
            ('import', lambda p: p['resource_changes'][0]['change'].update(importing={'id':'SECRET_ID'}), 'MODULE_MOVE_IMPORT_OR_DEPOSED_REVIEW'),
            ('move', lambda p: p['resource_changes'][0].update(previous_address='PRIVATE_OLD_ADDRESS'), 'MODULE_MOVE_IMPORT_OR_DEPOSED_REVIEW'),
            ('incomplete', lambda p: p.update(complete=False), 'PLAN_COMPLETE_NOT_ACCEPTABLE'),
            ('errored', lambda p: p.update(errored=True), 'PLAN_ERRORED_NOT_ACCEPTABLE'),
            ('not_applyable', lambda p: p.update(applyable=False), 'PLAN_APPLYABLE_NOT_ACCEPTABLE'),
            ('wrong_core', lambda p: p.update(terraform_version='1.15.0'), 'CORE_VERSION_MISMATCH'),
            ('future_format', lambda p: p.update(format_version='2.0'), 'UNSUPPORTED_JSON_FORMAT'),
            ('wrong_stage', lambda p: p['variables']['cluster_enabled'].update(value=False), 'STAGE_CLUSTER_FLAG_MISMATCH'),
            ('binding_early', lambda p: p['variables']['worker_sg_binding'].update(value={'worker_security_group_id':'PRIVATE_ID'}), 'FIRST_STAGE_BINDING_MUST_BE_NULL'),
            ('failed_check', lambda p: p['checks'][0].update(status='fail'), 'FAILED_CHECK_PRESENT'),
            ('drift', lambda p: p.update(resource_drift=[{'sensitive_placeholder':'DO_NOT_ECHO'}]), 'DRIFT_REQUIRES_REVIEW'),
            ('deferred', lambda p: p.update(deferred_changes=[{}]), 'DEFERRED_CHANGES_PRESENT'),
        ]
        for name, mutate, code in cases:
            with self.subTest(name=name):
                plan = deepcopy(plan_fixture()); mutate(plan)
                result = plan_review(plan, 'cluster-create')
                self.assertEqual(result['result'], 'BLOCKED'); self.assertIn(code, result['reason_codes'])
                serialized = json.dumps(result)
                for secret in ('DO_NOT_ECHO', 'SECRET_ID', 'PRIVATE_OLD_ADDRESS', 'PRIVATE_ID'):
                    self.assertNotIn(secret, serialized)

    def test_action_counts_are_exclusive_and_state_is_visible(self):
        for actions, category in [(['delete'],'delete'), (['update'],'update'), (['delete','create'],'replace'), (['create','delete'],'replace')]:
            plan = plan_fixture(); plan['resource_changes'][0]['change']['actions'] = actions
            result = plan_review(plan, 'cluster-create')
            self.assertEqual(result['managed_action_counts'][category], 1)
            self.assertEqual(sum(result['managed_action_counts'].values()), len(plan['resource_changes']))
        plan = plan_fixture(); plan['resource_changes'][0]['change']['actions'] = ['no-op']
        self.assertIn('EXISTING_MANAGED_RESOURCES_REVIEW', plan_review(plan,'cluster-create')['pending_codes'])
        plan = plan_fixture(); plan['prior_state'] = None
        self.assertNotIn('EXISTING_STATE_OWNERSHIP_REVIEW', plan_review(plan,'cluster-create')['pending_codes'])
        plan = plan_fixture(); plan['prior_state'] = {'values': {'root_module': {}}}
        self.assertIn('EXISTING_STATE_OWNERSHIP_REVIEW', plan_review(plan,'cluster-create')['pending_codes'])

    def test_data_scope_and_stage_are_not_inferred(self):
        plan = plan_fixture()
        self.assertEqual(plan_review(plan, 'cluster-create')['expected_data_address_count'], 13)
        self.assertIn('DATA_READ_COMPLETENESS_REVIEW', plan_review(plan, 'cluster-create')['pending_codes'])
        for key in ('current', 'foundation', 'cluster'):
            kind = {'current':'aws_caller_identity','foundation':'aws_vpc','cluster':'rhcs_rosa_operator_roles'}[key]
            plan['resource_changes'].append({'address':'data.'+kind+'.'+key,'mode':'data','type':kind,'name':key,'change':{'actions':['no-op']}})
        for kind, keys in [('aws_iam_role.account',('installer','support','controlplane','worker')), ('aws_subnet.public',('az_a','az_b','az_c')), ('aws_subnet.rosa_private',('az_a','az_b','az_c'))]:
            t,n = kind.split('.')
            for key in keys: plan['resource_changes'].append({'address':'data.'+kind+'['+json.dumps(key)+']','mode':'data','type':t,'name':n,'index':key,'change':{'actions':['no-op']}})
        result = plan_review(plan, 'cluster-create')
        self.assertEqual(result['observed_data_address_count'], 13)
        self.assertNotIn('DATA_READ_COMPLETENESS_REVIEW', result['pending_codes'])
        self.assertEqual(result['result'], 'NO_LISTED_ANOMALY_PENDING_REVIEW')
        with self.assertRaises(Invalid): plan_review(plan, 'delete')
        plan['resource_changes'][0]['generated_config'] = 'DO_NOT_ECHO'
        self.assertIn('MODULE_MOVE_IMPORT_OR_DEPOSED_REVIEW', plan_review(plan,'cluster-create')['reason_codes'])

    def test_permission_policy_and_file_open_race(self):
        good = SimpleNamespace(st_mode=0o100600, st_uid=1000)
        validate_file_stat(good, posix=True, uid=1000)
        for mode, owner in [(0o100644,1000),(0o100600,1001),(0o120600,1000),(0o040700,1000)]:
            with self.subTest(mode=mode,owner=owner):
                with self.assertRaises(Invalid): validate_file_stat(SimpleNamespace(st_mode=mode,st_uid=owner),posix=True,uid=1000)
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'mock.json';p.write_text('{}');p.chmod(0o600);st=p.stat()
            fake=SimpleNamespace(st_mode=st.st_mode,st_uid=st.st_uid,st_dev=st.st_dev,st_ino=st.st_ino+1)
            with patch.object(offline_review.os,'fstat',return_value=fake):
                with self.assertRaises(Invalid) as caught: read_json(p)
                self.assertEqual(str(caught.exception),'INPUT_FILE_CHANGED_DURING_OPEN')

    def test_overflow_numbers_and_unlimited_outputs_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'mock.json';p.write_text('{"value":1e999}');p.chmod(0o600)
            with self.assertRaises(Invalid) as caught: read_json(p)
            self.assertEqual(str(caught.exception),'NONFINITE_JSON')
            with self.assertRaises(Invalid): read_json(p,limit=2)
        fixture=sg_fixture();fixture[1]['extra_owner_output']={'value':'DO_NOT_ECHO','sensitive':True}
        result=sg_review(*fixture)
        self.assertIn('LIMITED_SG_OUTPUT_KEYS_REQUIRED',result['reason_codes'])
        self.assertNotIn('DO_NOT_ECHO',json.dumps(result))

    def test_json_and_cli_redaction(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / 'mock.json'
            for raw, code in [('{' , 'JSON_FORMAT'), ('{"value":1,"value":2}', 'DUPLICATE_JSON_KEY'), ('{"value":NaN}', 'NONFINITE_JSON')]:
                p.write_text(raw); p.chmod(0o600)
                with self.assertRaises(Invalid) as caught: read_json(p)
                self.assertEqual(str(caught.exception), code)
            malformed = plan_fixture()
            malformed['resource_changes'][0]['change'] = 'DO_NOT_ECHO'
            p.write_text(json.dumps(malformed)); p.chmod(0o600)
            result = subprocess.run([sys.executable, str(HERE / 'offline_review.py'), 'plan', '--plan', str(p), '--stage', 'cluster-create'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(json.loads(result.stdout)['reason_codes'], ['RESOURCE_CHANGE_FORMAT'])
            self.assertEqual(result.stderr, '')
            self.assertNotIn('DO_NOT_ECHO', result.stdout)

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ReviewTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    record = {'scope': 'synthetic_offline_tests_only', 'test_groups': result.testsRun, 'success': result.wasSuccessful(),
              'sg_negative_cases': 9, 'plan_negative_cases': 20, 'additional_adversarial_test_groups': 4, 'actual_sg_handoff_or_plan_tested': False,
              'aws_terraform_or_credential_calls': 0, 'source_reference': 'source-reference.json'}
    print(json.dumps(record, sort_keys=True))
    sys.exit(0 if result.wasSuccessful() else 1)
