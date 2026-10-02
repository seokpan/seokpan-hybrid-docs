"""Synthetic arithmetic checks; no infrastructure or recovery Run is executed."""

from contextlib import redirect_stderr, redirect_stdout
from copy import deepcopy
import io
import json
from pathlib import Path
import tempfile
import unittest

from recovery_metrics import calculate, main


def sample():
    return {
        "record_kind": "run", "run_id": "synthetic-unit-test",
        "recovery": {
            "backup_id": "synthetic-backup",
            "data_reference_level": "synthetic exact snapshot (test fixture only)",
            "data_reference_time_utc": "2026-10-02T09:00:00Z",
            "incident_at_utc": "2026-10-02T10:00:00Z",
            "dump_started_at_utc": "2026-10-02T09:00:00Z",
            "dump_finished_at_utc": "2026-10-02T09:00:05Z",
            "import_started_at_utc": "2026-10-02T10:02:00Z",
            "import_finished_at_utc": "2026-10-02T10:02:10Z",
            "business_resumed_at_utc": "2026-10-02T10:08:00.250Z",
        },
    }


class RecoveryMetricsTests(unittest.TestCase):
    def test_total_rto_includes_wait_and_business_check(self):
        result = calculate(sample(), True)
        self.assertEqual(result["rto_seconds"], 480.25)
        self.assertEqual(result["rpo_seconds"], 3600)
        self.assertEqual(result["import_seconds"], 10)
        self.assertNotIn("acceptance", result)
        self.assertNotIn("target", result)

    def test_unreviewed_data_time_is_not_exact_rpo(self):
        record = sample()
        record["recovery"]["data_reference_level"] = "dump start, uncertain snapshot"
        result = calculate(record)
        self.assertIsNone(result["rpo_seconds"])
        self.assertEqual(result["data_time_difference_seconds"], 3600)

    def test_timezone_offsets_and_day_boundary(self):
        record = sample()
        record["recovery"] = {
            "incident_at_utc": "2026-10-02T23:59:55Z",
            "business_resumed_at_utc": "2026-10-03T09:00:05+09:00",
        }
        self.assertEqual(calculate(record)["rto_seconds"], 10)

    def test_template_is_unmeasured_and_unchanged(self):
        path = Path(__file__).resolve().parents[1] / "evidence/_template/release.json"
        record = json.loads(path.read_text())
        original = deepcopy(record)
        result = calculate(record)
        self.assertEqual(result["calculation_status"], "UNMEASURED")
        self.assertIsNone(result["rto_seconds"])
        self.assertIsNone(result["data_time_difference_seconds"])
        self.assertEqual(record, original)

    def test_missing_business_completion_is_not_import_rto(self):
        record = sample()
        record["recovery"]["business_resumed_at_utc"] = None
        self.assertIsNone(calculate(record)["rto_seconds"])

    def test_invalid_timestamps_and_order_rejected(self):
        for field, value in (
            ("incident_at_utc", "2026-10-02T10:00:00"),
            ("incident_at_utc", "2026-10-02"),
            ("incident_at_utc", ""),
            ("incident_at_utc", 0),
            ("data_reference_time_utc", "2026-10-02T11:00:00Z"),
            ("dump_finished_at_utc", "2026-10-02T08:59:59Z"),
            ("import_started_at_utc", "2026-10-02T09:59:59Z"),
            ("import_finished_at_utc", "2026-10-02T10:01:00Z"),
            ("business_resumed_at_utc", "2026-10-02T10:02:05Z"),
        ):
            with self.subTest(field=field, value=value):
                record = sample()
                record["recovery"][field] = value
                with self.assertRaises(ValueError):
                    calculate(record)

    def test_confirmation_requires_backup_and_level_and_times(self):
        for field in ("backup_id", "data_reference_level", "data_reference_time_utc", "incident_at_utc"):
            with self.subTest(field=field):
                record = sample()
                record["recovery"][field] = None
                with self.assertRaises(ValueError):
                    calculate(record, True)

    def test_missing_intermediate_stage_does_not_hide_reversed_order(self):
        record = sample()
        record["recovery"]["import_finished_at_utc"] = None
        record["recovery"]["business_resumed_at_utc"] = "2026-10-02T10:01:00Z"
        with self.assertRaises(ValueError):
            calculate(record)

    def test_recorded_numbers_must_match_present_times(self):
        record = sample()
        record["recovery"].update(rto_seconds=480.25, rpo_seconds=3600)
        self.assertEqual(calculate(record, True)["rpo_seconds"], 3600)
        for field, value in (("rto_seconds", 10), ("rpo_seconds", 3599), ("rto_seconds", True),
                             ("rto_seconds", -1), ("rto_seconds", float("nan")),
                             ("rto_seconds", 10 ** 1000), ("rto_seconds", 1e308)):
            with self.subTest(field=field, value=value):
                changed = deepcopy(record)
                changed["recovery"][field] = value
                with self.assertRaises(ValueError):
                    calculate(changed)
        record["recovery"]["business_resumed_at_utc"] = None
        with self.assertRaises(ValueError):
            calculate(record)

    def test_candidate_and_wrong_shapes_rejected(self):
        for record in ([], {"record_kind": "candidate"}, {"record_kind": "run", "recovery": None}):
            with self.subTest(record=record), self.assertRaises(ValueError):
                calculate(record)

    def test_cli_read_only_and_exit_codes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "release.json"
            path.write_text(json.dumps(sample()))
            original = path.read_bytes()
            output = io.StringIO()
            with redirect_stdout(output):
                self.assertEqual(main([str(path)]), 0)
            self.assertIsNone(json.loads(output.getvalue())["rpo_seconds"])
            confirmed = io.StringIO()
            with redirect_stdout(confirmed):
                self.assertEqual(main([str(path), "--confirmed-data-time"]), 0)
            self.assertEqual(json.loads(confirmed.getvalue())["rpo_seconds"], 3600)
            self.assertEqual(path.read_bytes(), original)
            self.assertEqual([p.name for p in path.parent.iterdir()], ["release.json"])
            for invalid in ("{", '{"rto_seconds": NaN}',
                            '{"record_kind":"run","recovery":{"rto_seconds":1e999}}',
                            '{"record_kind":"candidate","record_kind":"run","recovery":{}}'):
                path.write_text(invalid)
                with redirect_stderr(io.StringIO()):
                    self.assertEqual(main([str(path)]), 2)
            with redirect_stderr(io.StringIO()):
                self.assertEqual(main([str(path.parent / "missing.json")]), 2)


if __name__ == "__main__":
    unittest.main()
