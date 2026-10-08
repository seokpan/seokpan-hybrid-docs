"""Declared FE/BE rollout request calculation; never a scheduling approval.
Reads Kustomize YAML via PyYAML. No Kubernetes API or credential access.
"""
from decimal import Decimal, InvalidOperation
import argparse, json, re
import yaml

class Unsupported(ValueError): pass

def cpu_milli(value):
    text=str(value)
    if not re.fullmatch(r'[0-9]+(?:\.[0-9]+)?m?',text): raise Unsupported('CPU_QUANTITY_UNSUPPORTED')
    number=Decimal(text[:-1]) if text.endswith('m') else Decimal(text)*1000
    if not number.is_finite() or number<=0: raise Unsupported('POSITIVE_REQUEST_REQUIRED')
    if number != int(number): raise Unsupported('CPU_PRECISION_BELOW_ONE_MILLICORE')
    return number

def memory_mib(value):
    match=re.fullmatch(r'([0-9]+(?:\.[0-9]+)?)(Ki|Mi|Gi|Ti)',str(value))
    if not match: raise Unsupported('MEMORY_QUANTITY_UNSUPPORTED')
    factor={'Ki':Decimal(1)/1024,'Mi':Decimal(1),'Gi':Decimal(1024),'Ti':Decimal(1024)**2}[match[2]]
    number=Decimal(match[1])*factor
    if not number.is_finite() or number<=0: raise Unsupported('POSITIVE_REQUEST_REQUIRED')
    return number

def workload(row):
    spec=row['spec'];pod=spec['template']['spec']
    replicas=spec.get('replicas')
    if type(replicas) is not int or replicas!=1: raise Unsupported('CURRENT_LAB_REPLICAS_CHANGED')
    if pod.get('initContainers') or pod.get('overhead') or pod.get('resources'):
        raise Unsupported('INIT_OVERHEAD_OR_POD_RESOURCES_REQUIRE_REVIEW')
    strategy=spec.get('strategy',{})
    if strategy.get('type')!='RollingUpdate' or strategy.get('rollingUpdate')!={'maxSurge':1,'maxUnavailable':0}:
        raise Unsupported('CURRENT_ROLLOUT_STRATEGY_CHANGED')
    containers=pod.get('containers')
    if not isinstance(containers,list) or not containers: raise Unsupported('CONTAINERS_REQUIRED')
    cpu=mem=Decimal(0)
    for container in containers:
        resources=container.get('resources',{});requests=resources.get('requests',{});limits=resources.get('limits',{})
        if set(requests)!={'cpu','memory'}: raise Unsupported('REQUEST_SCOPE_REQUIRES_REVIEW')
        c,m=cpu_milli(requests['cpu']),memory_mib(requests['memory'])
        if 'cpu' not in limits or 'memory' not in limits: raise Unsupported('LIMITS_REQUIRED')
        if c>cpu_milli(limits['cpu']) or m>memory_mib(limits['memory']): raise Unsupported('REQUEST_EXCEEDS_LIMIT')
        cpu+=c;mem+=m
    return {'cpu_m':cpu,'memory_mib':mem}

def analyze(rows):
    selected={}
    for row in rows:
        if not isinstance(row,dict): continue
        if row.get('kind')=='HorizontalPodAutoscaler': raise Unsupported('HPA_REQUIRES_LIVE_REVIEW')
        if row.get('kind')=='Deployment' and row.get('metadata',{}).get('name') in ('frontend','backend'):
            if row['metadata'].get('namespace') != 'seokpan-argotest': raise Unsupported('CURRENT_LAB_NAMESPACE_CHANGED')
            name=row['metadata']['name']
            if name in selected: raise Unsupported('DUPLICATE_FE_BE')
            selected[name]=workload(row)
    if set(selected)!={'frontend','backend'}: raise Unsupported('FE_BE_PAIR_REQUIRED')
    steady={k:sum(v[k] for v in selected.values()) for k in ('cpu_m','memory_mib')}
    # Same-size old/new Pods: one extra Pod per rollout, before terminating leftovers.
    result={'scope':'FE_BE_DECLARED_REQUESTS_ONLY','source_inputs':'rendered lab; old/new equal requests assumption',
        'per_pod':selected,'fe_be_steady_subtotal':steady,
        'fe_rollout_subtotal':{k:steady[k]+selected['frontend'][k] for k in steady},
        'be_rollout_subtotal_after_fe_old_pods_gone':{k:steady[k]+selected['backend'][k] for k in steady},
        'simultaneous_rollout_comparison_not_selected':{k:2*steady[k] for k in steady},
        'result':'CALCULATED_NOT_SCHEDULING_APPROVAL',
        'remaining_live_checks':['admitted old/new Pod requests, sidecars/init/overhead/LimitRange',
          'eligible individual Worker allocatable minus all requests; CPU, memory, pod slots, taints/affinity',
          'memory usage/pressure, terminating Pods, Registry/Pruner/Quota, owner window',
          'FE old Pods fully gone before BE; additional requests from any leftover Pod count separately']}
    return result

def serial(value):
    if isinstance(value,Decimal): return int(value) if value==int(value) else str(value)
    if isinstance(value,dict): return {k:serial(v) for k,v in value.items()}
    if isinstance(value,list): return [serial(v) for v in value]
    return value

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--render',required=True);args=parser.parse_args()
    try:
        with open(args.render,encoding='utf-8-sig') as stream: rows=list(yaml.safe_load_all(stream))
        print(json.dumps(serial(analyze(rows)),sort_keys=True));return 0
    except Unsupported as error:
        print(json.dumps({'result':'BLOCKED','reason_codes':[str(error)]}));return 2
    except Exception:
        print(json.dumps({'result':'BLOCKED','reason_codes':['LOCAL_RENDER_FORMAT_OR_READ_ERROR']}));return 2

if __name__=='__main__':
    raise SystemExit(main())
