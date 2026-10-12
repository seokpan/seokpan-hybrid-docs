"""Connection cap boundaries and missing-input tests; no DB/API or credential access."""

from copy import deepcopy
import ast
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from db_connection_budget import review
from offline_review import Invalid


def fixture(size=3, overflow=2, maximum=80):
    def group(pods):
        return {'pods': pods, 'processes_per_pod': 1,
                'engines': {name: {'pool_size': size, 'max_overflow': overflow}
                            for name in ('identity', 'game')}}
    return {'schema_version': 1, 'input_kind': 'candidate',
            'rds_max_connections': maximum, 'reserved_connections': 10,
            'pod_groups': {'steady': group(3), 'surge': group(1), 'terminating': group(1)}}


class BudgetTests(unittest.TestCase):
    def test_existing_candidate_formula_and_boundary(self):
        source = fixture()
        result = review(source)
        self.assertEqual(result['group_connection_caps'], {'steady': 30, 'surge': 10, 'terminating': 10})
        self.assertEqual(result['required_connections'], 60)
        self.assertEqual(result['remaining_connections'], 20)
        self.assertFalse(result['runtime_approval'])
        source['rds_max_connections'] = 60
        self.assertEqual(review(source)['result'], 'WITHIN_DECLARED_LIMIT_PENDING_REVIEW')
        source['rds_max_connections'] = 59
        self.assertEqual(review(source)['result'], 'DECLARED_CAP_EXCEEDS_LIMIT')

    def test_library_default_is_not_safe_cloud_configuration(self):
        result = review(fixture(size=5, overflow=10))
        self.assertEqual(result['required_connections'], 160)
        self.assertEqual(result['result'], 'DECLARED_CAP_EXCEEDS_LIMIT')

    def test_process_engine_and_old_new_rollout_caps(self):
        source = fixture()
        source['pod_groups']['surge']['engines']['identity']['pool_size'] = 1
        source['pod_groups']['surge']['engines']['game']['max_overflow'] = 0
        source['pod_groups']['terminating']['engines'] = {
            name: {'pool_size': 5, 'max_overflow': 10} for name in ('identity', 'game')}
        source['pod_groups']['terminating']['processes_per_pod'] = 2
        self.assertEqual(review(source)['group_connection_caps'],
                         {'steady': 30, 'surge': 6, 'terminating': 60})
        source['pod_groups']['terminating']['pods'] = 0
        self.assertEqual(review(source)['required_connections'], 46)

    def test_unknowns_never_become_zero_or_complete_result(self):
        for scope, key in [('root', 'rds_max_connections'), ('root', 'reserved_connections'),
                           ('terminating', 'pods'), ('steady', 'processes_per_pod')]:
            with self.subTest(key=key):
                source = fixture()
                target = source if scope == 'root' else source['pod_groups'][scope]
                target[key] = None
                result = review(source)
                self.assertEqual(result['result'], 'INPUT_INCOMPLETE')
                self.assertIsNone(result['remaining_connections'])
                self.assertFalse(result['runtime_approval'])

    def test_old_steady_connections_remain_in_rollout_budget(self):
        source = fixture(maximum=80)
        # Synthetic old/new configurations: old Pods may still be active as well
        # as terminating. Do not budget only new pool settings for steady Pods.
        for name in ('steady', 'terminating'):
            source['pod_groups'][name]['engines'] = {
                engine: {'pool_size': 5, 'max_overflow': 10}
                for engine in ('identity', 'game')}
        result = review(source)
        self.assertEqual(result['group_connection_caps'],
                         {'steady': 90, 'surge': 10, 'terminating': 30})
        self.assertEqual(result['required_connections'], 140)
        self.assertEqual(result['result'], 'DECLARED_CAP_EXCEEDS_LIMIT')
        self.assertFalse(result['runtime_approval'])

    def test_unbounded_malformed_and_missing_group_inputs(self):
        for change in (
            lambda x: x.update(rds_max_connections=True),
            lambda x: x.update(reserved_connections=-1),
            lambda x: x.update(reserved_connections=10.0),
            lambda x: x.update(schema_version=True),
            lambda x: x['pod_groups'].pop('terminating'),
            lambda x: x['pod_groups']['steady'].update(processes_per_pod=0),
            lambda x: x['pod_groups']['steady']['engines']['identity'].update(pool_size=0),
            lambda x: x['pod_groups']['steady']['engines']['game'].update(max_overflow=-1),
            lambda x: x['pod_groups']['steady']['engines'].pop('game'),
            lambda x: x.update(unexpected_secret='DO_NOT_ECHO'),
        ):
            source = deepcopy(fixture())
            change(source)
            with self.assertRaises(Invalid):
                review(source)

    def test_cli_complete_incomplete_excess_and_redacted_failure(self):
        script = Path(__file__).with_name('db_connection_budget.py')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'input.json'
            for source, expected, code in (
                (fixture(), 'WITHIN_DECLARED_LIMIT_PENDING_REVIEW', 0),
                (fixture(maximum=59), 'DECLARED_CAP_EXCEEDS_LIMIT', 2),
                (fixture(maximum=None), 'INPUT_INCOMPLETE', 2),
                ({'unknown': 'DO_NOT_ECHO'}, 'BLOCKED', 2),
            ):
                path.write_text(json.dumps(source), encoding='utf-8')
                path.chmod(0o600)
                result = subprocess.run([sys.executable, '-B', str(script), str(path)],
                                        capture_output=True, text=True, check=False)
                self.assertEqual(result.returncode, code)
                self.assertEqual(json.loads(result.stdout)['result'], expected)
                self.assertNotIn('DO_NOT_ECHO', result.stdout + result.stderr)
            path.write_text('{"schema_version":1,"schema_version":1}', encoding='utf-8')
            result = subprocess.run([sys.executable, '-B', str(script), str(path)],
                                    capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 2)
            self.assertIn('DUPLICATE_JSON_KEY', result.stdout)

    def test_python39_and_no_input_mutation(self):
        script = Path(__file__).with_name('db_connection_budget.py')
        ast.parse(script.read_text(encoding='utf-8-sig'), feature_version=(3, 9))
        source = fixture()
        original = deepcopy(source)
        review(source)
        self.assertEqual(source, original)


if __name__ == '__main__':
    unittest.main()
