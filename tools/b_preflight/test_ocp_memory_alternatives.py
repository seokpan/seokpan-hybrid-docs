"""Offline decision boundaries, not OCP execution results."""
import copy
import json
import unittest
from decimal import Decimal
from pathlib import Path

from ocp_memory_alternatives import Invalid, analyze, number, serial, unique


def fixture():
    return {"basis": "synthetic", "nodes": {
        "worker-1": {"headroom_mib": "14.5", "reserve_mib": None},
        "worker-2": {"headroom_mib": "272.5", "reserve_mib": 256}},
        "alternatives": [{"name": "unchanged", "released_requests_mib": {
            "worker-1": 0, "worker-2": 0}, "steps": [{"name": "pull-worker1",
            "additional_requests_mib": {"worker-1": 32, "worker-2": 0}}]}]}


class AlternativesTests(unittest.TestCase):
    def test_no_cross_node_headroom_aggregation(self):
        result = analyze(fixture())
        row = result["alternatives"][0]["steps"][0]
        self.assertEqual(row["remaining_mib"]["worker-1"], Decimal("-17.5"))
        self.assertEqual(row["result"], "MEMORY_DEFICIT")
        self.assertIs(result["runtime_approval"], False)

    def test_fe_pause_does_not_create_safety_margin(self):
        data = fixture()
        data["alternatives"][0]["released_requests_mib"]["worker-1"] = 32
        row = analyze(data)["alternatives"][0]["steps"][0]
        self.assertEqual(row["remaining_mib"]["worker-1"], Decimal("14.5"))
        self.assertEqual(row["result"], "RESERVE_UNCONFIRMED")

    def test_movement_consumes_destination_and_pruner_reserve(self):
        data = fixture()
        data["alternatives"][0]["released_requests_mib"] = {"worker-1": 128, "worker-2": -128}
        row = analyze(data)["alternatives"][0]["steps"][0]
        self.assertEqual(row["after_reserve_mib"]["worker-2"], Decimal("-111.5"))
        self.assertEqual(row["result"], "MEMORY_DEFICIT")

    def test_reduction_pull_and_be_surge_are_separate(self):
        data = fixture()
        candidate = data["alternatives"][0]
        candidate["released_requests_mib"]["worker-1"] = 128
        candidate["steps"].append({"name": "be-surge-worker1", "additional_requests_mib": {
            "worker-1": 128, "worker-2": 0}})
        rows = analyze(data)["alternatives"][0]["steps"]
        self.assertEqual(rows[0]["remaining_mib"]["worker-1"], Decimal("110.5"))
        self.assertEqual(rows[1]["remaining_mib"]["worker-1"], Decimal("14.5"))
        self.assertEqual(rows[1]["result"], "RESERVE_UNCONFIRMED")

    def test_known_reserve_never_approves_runtime(self):
        data = fixture()
        data["nodes"]["worker-1"]["reserve_mib"] = 10
        data["alternatives"][0]["released_requests_mib"]["worker-1"] = 64
        result = analyze(data)
        self.assertEqual(result["alternatives"][0]["steps"][0]["result"], "MEMORY_ONLY_PENDING_REVIEW")
        self.assertIs(result["runtime_approval"], False)

    def test_numeric_and_duplicate_input_rejection(self):
        for value in (True, False, 1.5, "NaN", "Infinity", "-1", None, [], {}):
            with self.subTest(value=value), self.assertRaises(Invalid):
                number(value)
        with self.assertRaises(Invalid):
            json.loads('{"x":0,"x":1}', object_pairs_hook=unique)
        self.assertEqual(number("14.5546875"), Decimal("14.5546875"))

    def test_unknown_reserve_missing_nodes_and_changed_scope(self):
        original = fixture()
        for mutate in (
            lambda d: d["alternatives"][0]["released_requests_mib"].pop("worker-2"),
            lambda d: d["alternatives"][0]["steps"][0]["additional_requests_mib"].update({"other": 0}),
            lambda d: d.update({"runtime_approval": True}),
            lambda d: d["alternatives"].append(copy.deepcopy(d["alternatives"][0])),
            lambda d: d["alternatives"][0]["steps"].append(copy.deepcopy(d["alternatives"][0]["steps"][0])),
            lambda d: d["nodes"]["worker-1"].pop("reserve_mib"),
            lambda d: d["alternatives"].clear(),
        ):
            data = copy.deepcopy(original)
            mutate(data)
            with self.assertRaises(Invalid):
                analyze(data)
        self.assertEqual(original, fixture())

    def test_historical_example_expected_results_and_serialization(self):
        data = json.loads(Path(__file__).with_name("ocp-memory-alternatives.example.json").read_text())
        result = analyze(data)
        names = {x["alternative"]: x for x in result["alternatives"]}
        self.assertEqual(names["release-two-64Mi-hypothesis"]["steps"][1]["remaining_mib"]["worker-1"],
                         Decimal("14.5"))
        self.assertEqual(names["move-128Mi-to-worker2-hypothesis"]["steps"][0]["result"], "MEMORY_DEFICIT")
        self.assertIn('"runtime_approval": false', json.dumps(serial(result)))

    def test_change_surge_cannot_spend_future_reclaimed_requests(self):
        data = json.loads(Path(__file__).with_name("ocp-memory-alternatives.example.json").read_text())
        unchanged = analyze(data)["alternatives"][0]["steps"]
        self.assertEqual(unchanged[2]["remaining_mib"]["worker-1"], Decimal("-49.5"))
        self.assertEqual(unchanged[3]["after_reserve_mib"]["worker-2"], Decimal("-47.5"))
        self.assertEqual(unchanged[2]["result"], "MEMORY_DEFICIT")
        self.assertEqual(unchanged[3]["result"], "MEMORY_DEFICIT")


if __name__ == "__main__":
    unittest.main()
