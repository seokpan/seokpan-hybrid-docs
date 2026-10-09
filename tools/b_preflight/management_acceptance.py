"""Offline management-auth receipt completeness, never IdP/RBAC validation or cleanup authorization."""
import argparse
import datetime
import json
from pathlib import Path
import re
import sys
from offline_review import read_json, Invalid
CASES = (
    "team_new_login", "nonteam_new_login_denied", "openshift_subject_mapping",
    "namespace_read", "secret_read_denied", "pod_create_denied", "exec_portforward_denied", "rolebinding_change_denied",
    "other_namespace_denied", "revoked_subject_existing_session_denied",
    "revoked_subject_new_session_denied", "existing_token_disposition",
    "normal_admin_path", "bootstrap_identity_inventory", "post_change_retest",
)
def review(receipt):
    keys={"schema_version","namespace","policy_revision","observed_at","context_receipt","idp_receipt","emergency_path_required","case_results"}
    if not isinstance(receipt,dict) or set(receipt)!=keys:
        raise Invalid("MANAGEMENT_RECEIPT_FIELDS")
    if type(receipt["schema_version"]) is not int or receipt["schema_version"]!=1:
        raise Invalid("MANAGEMENT_RECEIPT_VERSION")
    ns=receipt["namespace"]
    if not isinstance(ns,str) or len(ns)>63 or not re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*",ns) or ns=="default" or ns.startswith(("kube-","openshift-")) or "input-required" in ns:
        raise Invalid("MANAGEMENT_NAMESPACE")
    if not isinstance(receipt["policy_revision"],str) or not re.fullmatch(r"[a-f0-9]{40}",receipt["policy_revision"]):
        raise Invalid("MANAGEMENT_POLICY_REVISION")
    try:
        t=datetime.datetime.fromisoformat(receipt["observed_at"].replace("Z","+00:00"))
        if t.tzinfo is None: raise ValueError
    except (ValueError,TypeError,AttributeError):raise Invalid("MANAGEMENT_OBSERVATION_TIME") from None
    def ref(v):
        return isinstance(v,str) and re.fullmatch(r"(?:receipt:[a-zA-Z0-9._-]{1,120}|https://github\.com/seokpan/[a-z0-9-]+/(?:issues|pull)/[1-9][0-9]*(?:#(?:issuecomment|pullrequestreview)-[0-9]+)?)",v) is not None
    if not ref(receipt["context_receipt"]) or not ref(receipt["idp_receipt"]):
        raise Invalid("MANAGEMENT_OWNER_REFERENCES")
    if type(receipt["emergency_path_required"]) is not bool:
        raise Invalid("EMERGENCY_PATH_DECISION")
    cases=receipt["case_results"]
    expected=set(CASES)|({"emergency_path"} if receipt["emergency_path_required"] else {"emergency_not_adopted_review"})
    if not isinstance(cases,dict) or set(cases)!=expected:
        raise Invalid("MANAGEMENT_REQUIRED_CASES")
    pending=[]
    for name,row in cases.items():
        if not isinstance(row,dict) or set(row)!={"status","evidence_ref"} or row["status"] not in ("pass","fail","not_run"):
            raise Invalid("MANAGEMENT_CASE_FORMAT")
        if row["status"]=="pass" and not ref(row["evidence_ref"]):
            raise Invalid("MANAGEMENT_CASE_EVIDENCE_REQUIRED")
        if row["status"]!="pass":pending.append(name)
    return {"scope":"OWNER_RECEIPT_FORM_ONLY","result":"BLOCKED" if pending else "FORM_COMPLETE_OWNER_REVIEW_REQUIRED","pending_cases":sorted(pending),"live_authorization_and_bootstrap_cleanup":"NOT_AUTHORIZED_BY_THIS_TOOL"}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("receipt",type=Path);args=p.parse_args()
    try:
        verdict=review(read_json(args.receipt,limit=65536))
        print(json.dumps(verdict,sort_keys=True));return 2 if verdict["pending_cases"] else 0
    except (Invalid,OSError,ValueError,TypeError):
        print("MANAGEMENT_ACCEPTANCE_FORM: BLOCKED / INPUT_CONTRACT",file=sys.stderr);return 2
if __name__=="__main__":sys.exit(main())
