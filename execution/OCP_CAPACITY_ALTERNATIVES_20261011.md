# OCP 사용처 조사와 자원 확보안 비교 — 2026-10-11

worker-1을 시험 대상에서 제외하지 않는다. OCP 변경은 우리 팀에서 결정·진행하며, B/D가 변경 과정의 자원·서비스 영향·복구 범위와 실행 시각을 정리한다. 이 기록의 과거값 계산만으로 현재 배치 가능 여부를 판정하지 않는다.

## 관리 담당·실행 담당·Kubernetes 관리 객체

OCP 운영·변경을 우리 팀에서 관리하는 범위로 정리한다. B(정태훈)는 App/GitOps 변경 조율·사용처 조사·요구량과 대안 계산·변경/복구안 결정·결과 수락, D(최유준)는 현장 OCP/공급·시험 실행과 관측을 담당한다. 외부 팀의 별도 변경 승인을 실행 선행조건으로 두지 않는다. VM 용량 확장이 필요하면 OCP 변경과 별도로 호스트의 실제 가용 RAM·CPU와 조정 방법을 확인하며 A의 작업으로 추정하지 않는다.

Pod의 `ownerReferences`는 재생성/조정을 수행하는 객체다. 이 연결로 변경할 상위 CR과 복구 범위를 찾으며, 실제 서비스 사용처·영향과 구분한다.

## 받은 읽기 결과를 재사용한 조사

실제 수행은 기존 bastion 세션이며, 새 로그인/세션·Secret 출력·파일 쓰기·리소스 변경 없이 받은 출력이다. 시간은 과거 관측이며 최신 스냅샷으로 재사용하지 않는다.

| 관측·출처 | 확인한 내용 | 아직 입증하지 못한 내용 |
|---|---|---|
| 10/10 01:36 KST Node/Pod | worker-1 Ready·Pressure 없음, GitOps4개 requests 1408Mi, 실사용5655Mi/83% | 변경 허용·최대 사용량·현재 여유 |
| 10/10 02:00 KST Deployment/RS/Service·CRD/CR | cluster128Mi·gitops-plugin128Mi → GitopsService/cluster; application-controller1024Mi·dex128Mi → ArgoCD/openshift-gitops. 관련 Service 존재 | Application/사용자·업무 영향·실제 트래픽 |
| 같은 시각 | GitopsService는 **Cluster scope**, 실제 CR은 consolePlugin:{}; backend/gitopsPlugin resources 필드 지원. GitOps Operator1.22.1. 해당 Namespace PDB 목록 비어 있음 | 임의 정지/삭제가 안전하다는 의미 아님 |
| 같은 시각 Console | enabled plugins에 gitops-plugin 없음, ConsolePlugin/Service/Pod는 존재 | Console 미사용이 backend/plugin의 모든 소비자 부재를 입증하지 않음 |
| 10/10 02:12 KST 순간 metrics | cluster22Mi·plugin40Mi. 두 Pod Ready/restart0 | 과거 사용량 조회 실패. Peak·부하·OOM/안전 requests 미확인 |
| [D 기존 worker-1 조사와 B 후속](https://github.com/seokpan/seokpan-hybrid-gitops/issues/32#issuecomment-6084841284) | requests6797Mi, 여유약14.5Mi. 종료 Pod는 이미 제외, FE32Mi만 B 서비스에서 회수 가능 | 현재 노드/다른 사용자의 변경 상태 |

공식 [GitOpsService 자원 설정 안내](https://docs.redhat.com/en/documentation/red_hat_openshift_gitops/1.21/html/managing_resource_use/configure-resource-requests-and-limits-for-gitops-plugin-components)는 `.spec.consolePlugin.backend.resources`와 `.spec.consolePlugin.gitopsPlugin.resources`를 제시한다. 문서는1.21, 현장 설치는1.22.1이며 해당 필드는 받은1.22.1 CRD에서도 확인됐다. 실행 전에 현재 CR/Operator 동작을 다시 대조한다. 하위 Deployment만 직접 scale/patch하는 방식은 Operator의 재조정과 충돌할 수 있어 확보안으로 확정하지 않는다. Console 비활성만으로 Pod requests를 회수할 수 있다는 가정도 제외한다.

B가 추가 준비한 Application·ArgoCD·Service 대상·NetworkPolicy 목록 읽기를 기존 인증서 Context에서 수행한 결과를 수신했다. 4회 읽기 PASS, 로그인/Secret·파일 쓰기/변경 없음이다. 해당 출력에는 시작/종료 시각이 없어 실행 시각·동시 스냅샷을 새로 만들어 기록하지 않는다.

- 반환된 Application은 `openshift-gitops/seokpan-ocp-lab-app` 1개, 목적 Namespace `seokpan-argotest`, Project `seokpan-ocp-lab-app`, `Synced`, 자동 Sync 없음이다. 이는 현재 설정된 B App 관리 대상을 확인한 결과이며 다른 사람의 Console/CLI 사용 부재를 뜻하지 않는다.
- 기본 `ArgoCD/openshift-gitops`의 ownerReferences도 `GitopsService/cluster`다. controller 요청1Gi, Dex SSO, Server Route 활성화가 확인됐다. 이 ArgoCD와 연결된 application-controller/dex를 미사용으로 보고 중단하거나 `GitopsService/cluster`를 통째로 삭제하는 안은 제외한다. sourceNamespaces:null은 받은 필드 값이며 클러스터 접근 범위/다른 소비자 부재 판정으로 확대하지 않는다.
- `cluster`와 `gitops-plugin` Service에는 각각 Ready Pod1개, NotReady0이 있다. Ready Endpoint는 실제 접속/트래픽의 증거가 아니다. GitOps 구성요소용 NetworkPolicy7개 이름을 받았으나 정책 규칙/로그인 허용·거부를 검사한 것은 아니다.

남은 확인은 우리 서비스의 구성요소 사용처·중단 영향·복구 범위, Peak와 변경 과정의 자원 여유, B/D 실행 시각과 동시 작업이다. 이미 받은 이 목록이나 앞선 Pod/requests 읽기를 자동 반복하지 않는다. 현재 여유의 재측정은 실제 변경/시험 직전에 수행한다.

## 과거 requests를 이용한 후보 비교

예시는 D의 서로 다른 과거 시각에서 받은 worker-1 약14.5Mi와 worker-2 약272.5Mi를 사용한 **산술 비교**다. 동시 현재 실측이 아니며 worker-2의 Pruner256Mi는 아직 requests에 없는 경우의 별도 예약 비교다. 이미 실행 중인 Pruner가 합계에 포함됐으면 중복 차감하지 않는다. worker-1의 안전 여유값은 미확인으로 둔다.

| 후보 — 아직 채택하지 않음 | worker-1 변경 완료 후 여유 | worker-1 시험32Mi 후 | worker-1 BE surge128Mi 후 | 반대편 영향·결정 조건 |
|---|---:|---:|---:|---|
| 그대로 | 14.5Mi | -17.5Mi | -113.5Mi | 시험 불가 산술 |
| 우리 FE 일시 중단 | 46.5Mi | 14.5Mi | 적용하지 않음 | FE 중단/업무 영향. FE가 worker-2에 복귀하면240.5Mi로 Pruner256Mi보다15.5Mi 부족 |
| plugin 또는 backend128→64Mi | 78.5Mi | 46.5Mi | -49.5Mi | 64Mi는 비교용 후보, Peak/실제 소비자/변경 중 새 Pod의 자원 필요 |
| 두 구성요소 각각128→64Mi | 142.5Mi | 110.5Mi | 14.5Mi | Pull 산술 여유가 전체 교체의 안전 여유는 아님. 변경 전환 과정도 별도 확보 |
| 128Mi 구성요소 하나를 worker-2로 이동 | 142.5Mi | 110.5Mi | 14.5Mi | worker-2는144.5Mi, Pruner256Mi보다111.5Mi 부족. 단순 이동 추천 안 함 |
| Worker 용량 확장 | 실제 새 allocatable 수신 뒤 계산 | 미확정 | 미확정 | VM/노드 관리 담당, CPU/메모리·영향·재시작/복구/창을 확인. VM RAM 증가분을 allocatable 증가로 대신하지 않음 |

FE/BE 현재 선언의 추가 requests는 FE25m/32Mi, BE100m/128Mi다. [기존 Source 계산](B_OFFLINE_PREPARATION_REVIEW_20261009.md#ocp-순차-교체의-source-requests)을 유지하며 FE 이전 Pod가 모두 없어진 뒤 BE를 진행한다. 실제 배치 후보별 CPU/메모리·Pod 슬롯·taint/affinity·admitted init/sidecar/overhead·종료 Pod·동시 작업을 추가로 대조한다.

**설정 변경 자체의 전환 조건:** 받은 두 Deployment는 replicas1·RollingUpdate maxSurge25%/maxUnavailable25%다. 현재1 Replica에서는 새 Pod1개/Unavailable0이므로 requests를64Mi로 낮춰도 기존 Pod가 먼저 사라져64Mi를 공짜로 얻는 방식이 아니다. 예시의 변경 전 worker-1에는 새64Mi가 들어가지 않는다. worker-2도 Pruner256Mi를 따로 확보한 여유는16.5Mi이므로 새64Mi에47.5Mi 부족하다. 기존 Pod를 먼저 종료하는 전략 변경이나 일시 중단은 B/D가 서비스 영향·Operator 재조정·실행 순서·복구 방법을 확인한 뒤 결정한다. 설정 반영·새 Pod의 실제 배치·이전 Pod 종료를 확인한 후에만 확보된 여유를 인정한다.

## 오프라인 계산 재사용

[검사기](../tools/b_preflight/ocp_memory_alternatives.py)와 [과거값/가정 예시](../tools/b_preflight/ocp-memory-alternatives.example.json)는 노드별 여유를 합산하지 않고, 이동 시 반대편 감소·시험과 BE surge·별도 예약을 계산한다. 양수 `released_requests_mib`는 requests 감소, 음수는 추가/이동을 뜻한다. 각 step은 해당 변경 완료 상태에서의 독립 비교이며 누적 작업 시간선이 아니다. 감축량이 실제 회수됐다는 확인은 도구가 하지 않는다.

```bash
python3 tools/b_preflight/ocp_memory_alternatives.py --input tools/b_preflight/ocp-memory-alternatives.example.json
python3 -m unittest discover -s tools/b_preflight -p 'test_ocp_memory_alternatives.py' -v
```

`MEMORY_DEFICIT`는 입력 기준 메모리 부족, `RESERVE_UNCONFIRMED`는 안전 여유 미확인, `MEMORY_ONLY_PENDING_REVIEW`는 입력한 메모리/예약 산술 이내다. 세 판정 모두 `runtime_approval=false`다. 입력은 필터된 공개 수량·논리 참조만 사용하며 Credential/원문 응답을 넣지 않는다. 이 도구는 실제 Pod 유효 requests 집계기·스케줄러·트래픽/승인 검사기가 아니다.

## D 인계와 실행 준비

[D 미완료 인계 통합 요청](D_PENDING_HANDOFF_20261011.md)을 현재 전달문으로 사용한다.
OCP·기존 증거·Source 리뷰·CI/Release·계측·비용·Recovery 자산을 한 목록으로 확인한다.
완료 결과를 반복 요청하지 않으며 [변경·복구 실행 준비](OCP_CAPACITY_EXECUTION_PREPARATION_20261011.md)의
전환/원복 자원·VM 재시작·시험 순서를 적용한다.

실제 서비스 영향·Peak·전환 자원 때문에 감축이 적절하지 않으면 용량 확보 쪽으로 전환한다. B가 조사·계산·변경/복구안 검토를 진행하고 D가 현장 실행과 관측을 연결하므로 자원 확보 전체를 외부 승인 대기로 표시하지 않는다. 요청한 실행안이 나온 뒤 해당 변경에 필요한 현재 상태만 재측정한다.
