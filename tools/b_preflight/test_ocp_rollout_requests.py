from copy import deepcopy
from decimal import Decimal
from pathlib import Path
import json,unittest,yaml,hashlib
from ocp_rollout_requests import analyze,cpu_milli,memory_mib,Unsupported,serial
HERE=Path(__file__).parent
ROWS=json.loads((HERE/'lab-requests-fixture.json').read_text(encoding='utf-8'))
class BudgetTests(unittest.TestCase):
 def test_actual_pinned_source_render(self):
  reference=json.loads((HERE/'lab-source-reference.json').read_text(encoding='utf-8'))
  self.assertEqual(reference['source_head'],'26f7d63d64b5f67fe7042c7867ed358dbf40c814')
  self.assertEqual(hashlib.sha256((HERE/'lab-requests-fixture.json').read_bytes()).hexdigest(),reference['fixture_sha256'])
  result=serial(analyze(ROWS))
  self.assertEqual(result['per_pod'],{'backend':{'cpu_m':100,'memory_mib':128},'frontend':{'cpu_m':25,'memory_mib':32}})
  self.assertEqual(result['fe_be_steady_subtotal'],{'cpu_m':125,'memory_mib':160})
  self.assertEqual(result['fe_rollout_subtotal'],{'cpu_m':150,'memory_mib':192})
  self.assertEqual(result['be_rollout_subtotal_after_fe_old_pods_gone'],{'cpu_m':225,'memory_mib':288})
  self.assertEqual(result['simultaneous_rollout_comparison_not_selected'],{'cpu_m':250,'memory_mib':320})
  self.assertEqual(result['result'],'CALCULATED_NOT_SCHEDULING_APPROVAL')
 def test_units_and_submilli(self):
  self.assertEqual(cpu_milli('0.125'),125)
  with self.assertRaises(Unsupported):cpu_milli('0.5m')
  self.assertEqual(memory_mib('1Gi'),1024);self.assertEqual(memory_mib('1024Ki'),1)
  for value in ('NaN','-1','0','1G','1e100','1m'):
   with self.subTest(value=value):
    with self.assertRaises(Unsupported):memory_mib(value)
 def test_changes_cannot_silently_reuse_old_budget(self):
  cases=[('replicas',lambda p:p['spec'].update(replicas=3)),
   ('namespace',lambda p:p['metadata'].update(namespace='OTHER_ENVIRONMENT')),
   ('surge',lambda p:p['spec']['strategy']['rollingUpdate'].update(maxSurge=2)),
   ('percentage',lambda p:p['spec']['strategy']['rollingUpdate'].update(maxSurge='25%')),
   ('boolean_surge',lambda p:p['spec']['strategy']['rollingUpdate'].update(maxSurge=True)),
   ('boolean_unavailable',lambda p:p['spec']['strategy']['rollingUpdate'].update(maxUnavailable=False)),
   ('float_surge',lambda p:p['spec']['strategy']['rollingUpdate'].update(maxSurge=1.0)),
   ('init',lambda p:p['spec']['template']['spec'].update(initContainers=[{}])),
   ('overhead',lambda p:p['spec']['template']['spec'].update(overhead={'memory':'16Mi'})),
   ('pod_resources',lambda p:p['spec']['template']['spec'].update(resources={} or {'requests':{}})),
   ('missing_requests',lambda p:p['spec']['template']['spec']['containers'][0]['resources'].pop('requests')),
   ('request_over_limit',lambda p:p['spec']['template']['spec']['containers'][0]['resources']['requests'].update(memory='512Mi'))]
  for name,mutate in cases:
   with self.subTest(case=name):
    rows=deepcopy(ROWS);dep=next(x for x in rows if x.get('kind')=='Deployment' and x['metadata']['name']=='backend');mutate(dep)
    with self.assertRaises(Unsupported):analyze(rows)
 def test_added_regular_sidecar_is_counted(self):
  rows=deepcopy(ROWS);dep=next(x for x in rows if x.get('kind')=='Deployment' and x['metadata']['name']=='backend')
  dep['spec']['template']['spec']['containers'].append({'name':'MOCK_SIDE_CAR','resources':{'requests':{'cpu':'50m','memory':'16Mi'},'limits':{'cpu':'50m','memory':'16Mi'}}})
  self.assertEqual(analyze(rows)['per_pod']['backend'],{'cpu_m':150,'memory_mib':144})
 def test_hpa_and_duplicate_rejected(self):
  for extra in ({'kind':'HorizontalPodAutoscaler'},next(x for x in ROWS if x.get('kind')=='Deployment' and x['metadata']['name']=='backend')):
   with self.assertRaises(Unsupported):analyze(ROWS+[deepcopy(extra)])
if __name__=='__main__':
 suite=unittest.defaultTestLoader.loadTestsFromTestCase(BudgetTests);r=unittest.TextTestRunner(verbosity=2).run(suite)
 print(json.dumps({'test_groups':r.testsRun,'success':r.wasSuccessful(),'pinned_render_subset_fixture_tested':True,'cluster_or_actual_admitted_pods_tested':False}))
 raise SystemExit(0 if r.wasSuccessful() else 1)
