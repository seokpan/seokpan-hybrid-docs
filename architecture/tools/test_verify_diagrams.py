"""Provenance/history regression tests; no network or Runtime credentials."""
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location('verify_diagrams', Path(__file__).with_name('verify_diagrams.py'))
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.base = {
            'recorded_date': '2026-10-07 KST', 'source_basis_date': '2026-10-07 KST',
            'files': [{'path': f'design/{i:02}.md', 'sha256': str(i)} for i in range(5)],
            'review': {'status': 'HISTORICAL'},
            'followup_review': {'requirements': {'rto_minutes': 10, 'persistent_db_rpo_minutes': 30,
                                               'operating_portable_backup_interval_minutes': 15},
                                'full_t18_acceptance': 'NOT RUN'},
            'data_engine_followup': {'target_engine': 'Valkey 7.2', 'status': 'SOURCE_MERGED_RUNTIME_PENDING'},
            'followup_review_history': [{'date': 'old', 'result': 'undecided'}],
        }
        self.old = {
            'created_date': '2026-10-02 KST', 'runtime_validation': 'NOT_ASSESSED',
            'followup_review': {'requirements': {'rto_minutes': 30}},
            'data_engine_followup': {'status': 'SOURCE_PENDING'},
            'followup_review_history': [{'date': 'earliest', 'result': 'partial'}],
            'check_scope_history': [{'check': 'original'}],
            'latest_check_scope': {'date': '2026-10-06 KST', 'check': 'previous'},
            'future_extension': {'keep': ['nested', {'value': 7}]},
        }
        self.checks = {'declared_geometry': 0}

    def compose(self, previous=None, mode='integrity_only'):
        return MODULE.compose_manifest(self.base, self.old if previous is None else previous,
                                       [], self.checks, mode)

    def test_current_dr_requirements_survive(self):
        self.assertEqual(self.compose()['followup_review'], self.base['followup_review'])

    def test_current_valkey_source_overrides_stale_status(self):
        self.assertEqual(self.compose()['data_engine_followup'], self.base['data_engine_followup'])

    def test_both_historical_decision_lists_survive(self):
        self.assertEqual(len(self.compose()['followup_review_history']), 2)

    def test_previous_latest_check_moves_into_history(self):
        result = self.compose()
        self.assertIn(self.old['latest_check_scope'], result['check_scope_history'])
        self.assertIn(self.old['check_scope_history'][0], result['check_scope_history'])

    def test_unknown_extension_is_preserved(self):
        self.assertEqual(self.compose()['future_extension'], self.old['future_extension'])

    def test_no_input_mutation_or_alias(self):
        base, old = deepcopy(self.base), deepcopy(self.old)
        result = self.compose()
        result['future_extension']['keep'].append('new')
        result['followup_review']['requirements']['rto_minutes'] = 999
        self.assertEqual(self.base, base)
        self.assertEqual(self.old, old)

    def test_repeated_output_is_identical(self):
        one = self.compose()
        self.assertEqual(self.compose(previous=one), one)

    def test_creation_date_is_not_rewritten(self):
        self.assertEqual(self.compose()['created_date'], '2026-10-02 KST')

    def test_no_runtime_success_or_geometry_success_from_integrity_only(self):
        result = self.compose()
        self.assertEqual(result['runtime_validation'], 'NOT_ASSESSED')
        self.assertEqual(result['latest_check_scope']['declared_geometry'], 'SKIPPED_NO_BUILD_LAYOUT')
        self.assertEqual(result['followup_review']['full_t18_acceptance'], 'NOT RUN')

    def test_default_geometry_mode_is_distinct(self):
        self.assertEqual(self.compose(mode='build_layout')['latest_check_scope']['declared_geometry'],
                         'CHECKED_AGAINST_BUILD_LAYOUT')

    def test_missing_optional_source_key_does_not_erase_previous_metadata(self):
        del self.base['data_engine_followup']
        self.assertEqual(self.compose()['data_engine_followup'], self.old['data_engine_followup'])

    def test_source_identity_refresh(self):
        self.assertEqual(self.compose()['source_files'], self.base['files'])

    def test_atomic_write_and_interruption_preserve_old_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'manifest.json'
            path.write_text('old\n')
            with patch.object(MODULE.os, 'replace', side_effect=OSError('simulated interruption')):
                with self.assertRaises(OSError):
                    MODULE.atomic_write(path, 'new\n')
            self.assertEqual(path.read_text(), 'old\n')
            self.assertEqual(list(path.parent.iterdir()), [path])
            MODULE.atomic_write(path, 'new\n')
            self.assertEqual(path.read_text(), 'new\n')


if __name__ == '__main__':
    unittest.main()
