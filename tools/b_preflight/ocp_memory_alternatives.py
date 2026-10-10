"""Compare declared per-node memory alternatives offline, never approve execution.

Input headroom is an observed allocatable-minus-requests subtotal, not free RAM.
Changes describe steady state after reconciliation, not the transient rollout.
No API, credentials, Kubernetes quantity inference or automatic remediation.
"""
import argparse
import json
from decimal import Decimal, InvalidOperation


class Invalid(ValueError):
    pass


def number(value, negative=False):
    if type(value) not in (int, str):
        raise Invalid("EXPLICIT_DECIMAL_REQUIRED")
    try:
        result = Decimal(value)
    except InvalidOperation:
        raise Invalid("DECIMAL_FORMAT") from None
    if not result.is_finite() or (not negative and result < 0):
        raise Invalid("FINITE_NONNEGATIVE_REQUIRED")
    return result


def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise Invalid("DUPLICATE_JSON_KEY")
        result[key] = value
    return result


def keys(value, expected):
    if not isinstance(value, dict) or set(value) != set(expected):
        raise Invalid("INPUT_SCOPE")


def analyze(data):
    keys(data, ("basis", "nodes", "alternatives"))
    if not isinstance(data["basis"], str) or not data["basis"].strip():
        raise Invalid("BASIS_REQUIRED")
    nodes = data["nodes"]
    if not isinstance(nodes, dict) or not nodes:
        raise Invalid("NODES_REQUIRED")
    headroom = {}
    for name, row in nodes.items():
        if not name or not isinstance(name, str):
            raise Invalid("NODE_NAME_REQUIRED")
        keys(row, ("headroom_mib", "reserve_mib"))
        headroom[name] = number(row["headroom_mib"], negative=True)
        if row["reserve_mib"] is not None:
            number(row["reserve_mib"])
    alternatives = data["alternatives"]
    if not isinstance(alternatives, list) or not alternatives:
        raise Invalid("ALTERNATIVES_REQUIRED")
    seen = set()
    results = []
    for alternative in alternatives:
        keys(alternative, ("name", "released_requests_mib", "steps"))
        name = alternative["name"]
        if not isinstance(name, str) or not name.strip() or name in seen:
            raise Invalid("DISTINCT_ALTERNATIVE_REQUIRED")
        seen.add(name)
        changes = alternative["released_requests_mib"]
        keys(changes, nodes)
        # Positive = requests removed; negative = requests moved/added here.
        after = {node: headroom[node] + number(changes[node], negative=True)
                 for node in nodes}
        steps = alternative["steps"]
        if not isinstance(steps, list) or not steps:
            raise Invalid("STEPS_REQUIRED")
        names = set()
        rows = []
        for step in steps:
            keys(step, ("name", "additional_requests_mib"))
            if not isinstance(step["name"], str) or not step["name"].strip() or step["name"] in names:
                raise Invalid("DISTINCT_STEP_REQUIRED")
            names.add(step["name"])
            additional = step["additional_requests_mib"]
            keys(additional, nodes)
            remaining = {node: after[node] - number(additional[node]) for node in nodes}
            reserve_remaining = {node: None if nodes[node]["reserve_mib"] is None else
                                 remaining[node] - number(nodes[node]["reserve_mib"])
                                 for node in nodes}
            deficit = any(v < 0 for v in remaining.values()) or any(
                v is not None and v < 0 for v in reserve_remaining.values())
            result = "MEMORY_DEFICIT" if deficit else (
                "RESERVE_UNCONFIRMED" if any(v is None for v in reserve_remaining.values())
                else "MEMORY_ONLY_PENDING_REVIEW")
            rows.append({"step": step["name"], "remaining_mib": remaining,
                         "after_reserve_mib": reserve_remaining, "result": result})
        results.append({"alternative": name, "after_change_headroom_mib": after,
                        "steps": rows})
    return {"basis": data["basis"], "scope": "DECLARED_MEMORY_ARITHMETIC_ONLY",
            "runtime_approval": False, "alternatives": results,
            "unverified": ["input provenance/freshness and admissible changes",
                           "CPU/pod slots/placement/taints/affinity and admitted requests",
                           "actual memory/peaks/pressure and operator reconciliation",
                           "change rollout surge/terminating Pods and other concurrent jobs",
                           "consumers, service impact/restoration and execution window"]}


def serial(value):
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, dict):
        return {k: serial(v) for k, v in value.items()}
    if isinstance(value, list):
        return [serial(v) for v in value]
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    try:
        with open(args.input, encoding="utf-8-sig") as stream:
            data = json.load(stream, object_pairs_hook=unique,
                             parse_constant=lambda _: (_ for _ in ()).throw(Invalid("NONFINITE_JSON")))
        print(json.dumps(serial(analyze(data)), sort_keys=True))
        return 0
    except Invalid as error:
        print(json.dumps({"result": "BLOCKED", "reason_codes": [str(error)],
                          "runtime_approval": False}))
        return 2
    except Exception:
        print(json.dumps({"result": "BLOCKED", "reason_codes": ["LOCAL_INPUT_READ_OR_FORMAT"],
                          "runtime_approval": False}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
