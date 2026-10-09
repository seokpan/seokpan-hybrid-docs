import copy
import unittest
from management_acceptance import CASES, review
from offline_review import Invalid
class ManagementReceiptTests(unittest.TestCase):
    def fixture(self,emergency=True):
        names=list(CASES)+(["emergency_path"] if emergency else ["emergency_not_adopted_review"])
        return {"schema_version":1,"namespace":"fixture-cloud","policy_revision":"a"*40,"observed_at":"2026-10-09T00:00:00+00:00","context_receipt":"receipt:fixture-context","idp_receipt":"receipt:fixture-idp","emergency_path_required":emergency,"case_results":{k:{"status":"pass","evidence_ref":"receipt:fixture-"+k} for k in names}}
    def test_complete_form_still_requires_owner_decision(self):
        for emergency in (True,False):
            v=review(self.fixture(emergency))
            self.assertEqual(v["result"],"FORM_COMPLETE_OWNER_REVIEW_REQUIRED")
            self.assertEqual(v["live_authorization_and_bootstrap_cleanup"],"NOT_AUTHORIZED_BY_THIS_TOOL")
    def test_each_missing_negative_or_normal_admin_case_blocks(self):
        for name in list(CASES)+["emergency_path"]:
            with self.subTest(name=name):
                c=self.fixture();c["case_results"][name]["status"]="not_run"
                self.assertEqual(review(c)["pending_cases"],[name])
                c["case_results"][name]["status"]="fail"
                self.assertEqual(review(c)["result"],"BLOCKED")
    def test_pass_without_evidence_and_missing_subject_case_rejected(self):
        c=self.fixture();c["case_results"]["openshift_subject_mapping"]["evidence_ref"]=""
        with self.assertRaises(Invalid):review(c)
        c=self.fixture();del c["case_results"]["revoked_subject_existing_session_denied"]
        with self.assertRaises(Invalid):review(c)
    def test_secret_unknown_field_fake_revision_and_bad_time_rejected(self):
        for key,value in [("client_secret","sentinel"),("policy_revision","main"),("observed_at","2026-10-09"),("schema_version",True),("namespace","openshift-admin"),("emergency_path_required",1)]:
            with self.subTest(key=key):
                c=self.fixture();c[key]=value
                with self.assertRaises(Invalid):review(c)
    def test_arbitrary_evidence_value_and_extra_case_rejected(self):
        c=self.fixture();c["case_results"]["team_new_login"]["evidence_ref"]="sentinel-token"
        with self.assertRaises(Invalid):review(c)
        c=self.fixture();c["case_results"]["secret_admin"]={"status":"pass","evidence_ref":"receipt:fixture"}
        with self.assertRaises(Invalid):review(c)
if __name__=="__main__":unittest.main()
