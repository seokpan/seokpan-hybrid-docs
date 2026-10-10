# worker-1 자원 확보·시험 실행 준비 — 2026-10-11

## 현재 결정과 입력 경계

OCP 운영·변경은 우리 팀이 관리한다. B는 변경/복구안·배포 조합·결과 수락을
판단하고 D는 현장 입력·실행·관측을 연결한다. 외부 팀의 별도 승인 대기는 없다.
[기존 조사·비교](OCP_CAPACITY_ALTERNATIVES_20261011.md)를 재사용한다.
이 문서는 실행 순서 준비이며 변경 명령·감축값·VM 증설량의 채택이 아니다.

- 기본 ArgoCD/controller/dex와 GitopsService 전체 중단·삭제는 제외한다.
- FE 중단·128→64Mi·worker-2 이동은 현재 실행안으로 채택하지 않는다.
- DB·Redis·PVC·NFS·다른 업무를 자원 회수 대상으로 추가하지 않는다.
- Pruner/PriorityClass/SCC/nodeName 변경이나 requests 없는 시험 Pod로 우회하지 않는다.

## B가 준비한 노드별 비교

현재 requests 여유 H, 변경 완료 뒤 실제 회수량/allocatable 증가 Δ, 별도 동시 작업
요청 J, 확인된 안전 여유 R, 해당 단계의 새 Pod 유효 요청 A를 사용한다.
각 노드에서 `H + Δ - J - A - R >= 0`을 확인한다. R 미확인은 0이 아니다.
Pruner가 현재 합계에 포함됐으면 J에 중복 추가하지 않는다. 메모리만으로
CPU·슬롯·배치·실사용/Pressure·Admission·서비스 안전성을 통과 처리하지 않는다.

과거 worker-1 H=14.5Mi의 회수/증설 하한은 Pull32Mi에17.5Mi+J+R,
BE surge128Mi에113.5Mi+J+R다. 단계가 순차이면32+128을 동시에 추가하지 않는다.
실제 FE 종료·자원 반환 후 BE로 진행한다. 이 값은 추천 VM RAM/안전 여유가 아니다.
변경 도중 아직 회수되지 않은 Δ는0이다. replicas1/maxSurge25%/maxUnavailable25%의
새64Mi Pod도 변경 전 여유에 들어가야 한다. 과거 예시는 worker-1에49.5Mi,
worker-2에 Pruner256Mi를 별도 확보하면47.5Mi 부족이다. 원복 시에도 원래 요청의
새 Pod·종료 중 Pod를 별도로 계산한다.

## 변경·복구·시험 순서

| 단계 | 준비한 처리 | 남은 현장 입력/실행 | 다음 진행 조건 |
|---|---|---|---|
| 후보 비교 | 감축·용량 확장·전환/복구 하한 | plugin 사용/Peak, 호스트 RAM·CPU·증설/게스트 인식 | 후보와 제외 사유 구분 |
| 변경안 고정 | 원래 값/필드 부재·변경 범위·복귀 결과 | 현재 CR/Operator, 정확한 값·새/종료 Pod | 전환·원복 자원과 서비스 영향 확인 |
| 실행 시각 | B/D 실행자·중단 연락·동시 작업 구분 | 날짜·시작/종료·Pruner/배포/Backup 충돌 | 같은 대상 중복 변경 없음 |
| 변경 직전 | 필요한 조건만 재측정 | 양 Worker 전체 admitted requests·CPU/슬롯·Pressure·Pending/종료·배치 | 과거값을 최신값으로 승계하지 않음 |
| 변경·확인 | 검토한 한 후보, 실제 반환/증가량 확인 | D 실행·Operator 조정·Pod Ready/Restart/OOM·App/Argo 기능 | 계획 상태·확보량·기능 모두 확인 |
| worker-1 Pull | FE 회수 뒤 BE, 동시 시험 Pod 최대1 | Index/child·기존 SA·server dry-run·전체 Pod priority 비교 | 각 생성 전 재확인, Succeeded/exit0/imageID·정리 |
| 교체·업무 | 같은 Release/Config/DB의 FE→BE·복귀·보호 Case | GitOps/등록 SHA·targetRevision·Gate/live Diff·DB current/Secret/CA·실행 경로 | #37 Draft 조건 검토, 병합된 SHA만 소비, Sync는 별도 수락 |

감축은 `.spec.consolePlugin.backend.resources`와
`.spec.consolePlugin.gitopsPlugin.resources`의 해당 항목만 검토한다.
[공식 설정 안내](https://docs.redhat.com/en/documentation/red_hat_openshift_gitops/1.21/html/managing_resource_use/configure-resource-requests-and-limits-for-gitops-plugin-components)는
상위 CR 조정을 설명한다. 문서는1.21이며 현장1.22.1에서 받은 CRD 필드를 재사용하되
현재 Operator 동작은 실행 시 확인한다. 하위 Deployment patch/scale이 지속된다고
가정하지 않는다. 다른 전환 전략도 Operator 지원·기능 영향 확인 전에는 명령으로
확정하지 않는다. 원래 필드가 없으면 복귀는 임의128Mi 입력이 아니라 원래 부재/
상위 설정 복원과 실제 결과 대조다.

VM 경로는 호스트 가용량·Hot-add 지원/게스트 인식 여부를 확인한다. 재시작이
필요하면 drain/eviction 대상·PDB·로컬 데이터와 반대편 배치 여유부터 대조한다.
현재 worker-2가 worker-1 Pod를 받아줄 수 있다고 가정하지 않는다. force drain·
PDB 우회·강제 종료를 준비 명령에 넣지 않는다. RAM 변경 후 실제 allocatable·
Ready·기능을 확인해야 하며 RAM 증가분을 그대로 Δ로 쓰지 않는다.

## 중단·원복·기존 증거

계획과 상태/입력이 다르거나 필요한 전체 조회가 불완전하면 시작하지 않는다.
Pending/InsufficientMemory·Pressure·OOM·예상 밖 Operator 조정·서비스 장애가 나타나면
다음 생성/교체를 중단하고 증거를 보존한다. 새 후보/우회로 자동 전환하지 않는다.
원복에도 자원이 부족하면 무조건 restore하지 않고 확보/배치 순서를 다시 판단한다.
종료 시 CR/Pod·App/Argo·Replica/Digest·시험 Pod 정리를 확인한다. VM 원복도 RAM 즉시
축소로 가정하지 않으며 이미 늘어난 사용량·Pod와 재시작 영향부터 확인한다.

worker-2 성공은 유지한다. 당시 사용창·실행 직전/FE→BE 사이 자원 기록은 존재/없음을
그대로 확인하며 현재 권한/측정으로 소급 완성하지 않는다. 보완 재시험 여부는 B가
증거 대조 후 결정한다. 나머지 D 현장/CI/계측/비용/보존 입력은
[통합 인계 요청](D_PENDING_HANDOFF_20261011.md)으로 확인한다.
