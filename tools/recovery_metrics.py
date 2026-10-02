#!/usr/bin/env python3
"""Read-only recovery time arithmetic; this is not an acceptance validator."""

import argparse
from datetime import datetime, timezone
from itertools import combinations
import json
import math
from pathlib import Path
import sys


TIME_FIELDS = (
    "data_reference_time_utc", "incident_at_utc",
    "dump_started_at_utc", "dump_finished_at_utc",
    "import_started_at_utc", "import_finished_at_utc",
    "business_resumed_at_utc",
)


def timestamp(value, field):
    if value is None:
        return None
    if not isinstance(value, str) or "T" not in value:
        raise ValueError(f"{field}: timezone-aware ISO timestamp or null required")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"{field}: invalid ISO timestamp") from exc
    if parsed.utcoffset() is None:
        raise ValueError(f"{field}: timezone is required")
    return parsed.astimezone(timezone.utc)


def calculate(record, confirmed_data_time=False):
    if not isinstance(record, dict) or record.get("record_kind") != "run":
        raise ValueError("record_kind must be run; release candidates are not Runs")
    recovery = record.get("recovery")
    if not isinstance(recovery, dict):
        raise ValueError("recovery must be an object")
    times = {key: timestamp(recovery.get(key), key) for key in TIME_FIELDS}
    # Check only present pairs. Missing values never become zero durations.
    pairs = (
        ("data_reference_time_utc", "incident_at_utc"),
        ("dump_started_at_utc", "dump_finished_at_utc"),
        ("data_reference_time_utc", "dump_finished_at_utc"),
    )
    pairs += tuple(combinations(("incident_at_utc", "import_started_at_utc",
                                 "import_finished_at_utc", "business_resumed_at_utc"), 2))
    for first, last in pairs:
        if times[first] is not None and times[last] is not None:
            if times[last] < times[first]:
                raise ValueError(f"{last} precedes {first}")

    def duration(first, last):
        if times[first] is None or times[last] is None:
            return None
        return (times[last] - times[first]).total_seconds()

    rto = duration("incident_at_utc", "business_resumed_at_utc")
    data_age = duration("data_reference_time_utc", "incident_at_utc")
    level = recovery.get("data_reference_level")
    backup_id = recovery.get("backup_id")
    if confirmed_data_time and (
        data_age is None or not isinstance(level, str) or not level.strip()
        or not isinstance(backup_id, str) or not backup_id.strip()
    ):
        raise ValueError("confirmed data time requires both timestamps, backup_id and data_reference_level")
    rpo = data_age if confirmed_data_time else None
    for field, computed in (("rto_seconds", rto), ("rpo_seconds", data_age)):
        recorded = recovery.get(field)
        if recorded is None:
            continue
        if (isinstance(recorded, bool) or not isinstance(recorded, (int, float))
                or (isinstance(recorded, float) and not math.isfinite(recorded)) or recorded < 0):
            raise ValueError(f"{field}: finite nonnegative number or null required")
        if computed is None:
            raise ValueError(f"{field}: recorded value has no supporting timestamp pair")
        try:
            matches = math.isclose(recorded, computed, rel_tol=0, abs_tol=0.000001)
        except OverflowError:
            matches = False
        if not matches:
            raise ValueError(f"{field}: recorded value disagrees with timestamp arithmetic")
    notes = [
        "Timestamp arithmetic only; no target comparison or acceptance decision.",
        "Reviewer must check clock uncertainty, timeline/raw evidence, actual business recovery and data losses.",
        "One Run does not establish an operational RPO bound or recovery guarantee.",
    ]
    if not confirmed_data_time:
        notes.append("Data-time difference is unverified; do not copy it as exact RPO. Review data_reference_level and backup/marker evidence first.")
    if rto is None:
        notes.append("RTO unmeasured: incident or business-resumed timestamp is missing.")
    return {
        "run_id": record.get("run_id"),
        "calculation_status": "CALCULATED" if rto is not None or data_age is not None else "UNMEASURED",
        "rto_seconds": rto,
        "rpo_seconds": rpo,
        "data_time_difference_seconds": data_age,
        "rpo_basis": "REVIEWER_CONFIRMED_DATA_TIME" if confirmed_data_time else "UNVERIFIED",
        "dump_seconds": duration("dump_started_at_utc", "dump_finished_at_utc"),
        "import_seconds": duration("import_started_at_utc", "import_finished_at_utc"),
        "notes": notes,
    }


def reject_constant(value):
    raise ValueError(f"non-finite JSON number: {value}")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("release", type=Path, help="existing Run release.json; read only")
    parser.add_argument(
        "--confirmed-data-time", action="store_true",
        help="reviewer attests the selected backup's actual data time and evidence have been checked",
    )
    args = parser.parse_args(argv)
    try:
        record = json.loads(args.release.read_text(encoding="utf-8"),
                            parse_constant=reject_constant, object_pairs_hook=unique_object)
        result = calculate(record, args.confirmed_data_time)
    except (OSError, ValueError) as exc:
        print(f"recovery_metrics: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
