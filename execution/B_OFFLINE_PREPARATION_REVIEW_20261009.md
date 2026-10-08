# B 독립 선행 준비 재검토 — 2026-10-09

ROSA·OCP·App·이관·Recovery의 실행 조건을 구분하고, 실제 입력 없이 가능한 검사 준비를 보완했다. 실제 환경을 생성하거나 인증/State/Plan·서비스를 호출한 기록이 아니다. 기존 설계·예산·사용창 후보·배포 Source 및 Image SHA를 변경하지 않았다.

## 추적 범위와 확인 결과

네 저장소 main 및 관련 17개 이슈/댓글을 대조했다. 기준 Source는 App `188199630ceb5fd67d8fe57d4d5650694e2e00e3`, GitOps `26f7d63d64b5f67fe7042c7867ed358dbf40c814`, Infra `aaa8cff09cd70298b142afdba5faf15d73664cc3`, Docs의 이 변경 전 `d00cb43154885797d913e948070807b9edd81652`다. A PR #54 구현/보완은 B 고유 작업에 넣지 않는다. A/C의 실제 인계, 프로젝트 지원/예산 결정, D의 Registry 공급·현재 자원/창은 아직 수신하지 않았다.

| 경로 | 이미 준비했거나 이번에 보완한 범위 | 실제로 받아야 하는 조건 |
|---|---|---|
| ROSA 기반·SG 수신 | 기존 입력 계약·Code/Lock·Controller mock, 이번 SG 출력명↔입력키↔GroupName 검사 | A의 보호 입력/권한/State 저장소·C SG 관측/개정 |
| ROSA 첫 Plan | 별도 초기 IAM/OIDC 준비·Cluster 생성 단계의 변경/수량 검사, 기존 상태·조회 누락을 검토 항목으로 표시 | 실제 목적 인증·Backend·지원/Quota·입력 수락 후 전체 Plan |
| OCP 새 Image | Run #5 SHA/Digest 수락·Migration 대조, 아래 순차 교체 requests 계산 | D Registry index/child mapping·Pull·양 Worker 현재 자원/창 |
| App 업무·다중 Pod·WS·장애·Prune/Delete | 기존 Source 시험/Case/보호 선언, App4·GitOps10에서 실제 Run 연결 유지 | 해당 실행 환경·승인 Image/입력·사용창 |
| Pool·Cloud App | 기존 DB_CONNECTION_BUDGET_PREPARATION의 Engine/Process/Replica/롤링 예산 | C 실제 RDS 연결 상한·예약, B/C 채택 값 |
| 1차 이관 | 기존 FIRST_SERVICE_WRITE_STOP_PREPARATION의 재기동 제어·중지 유지·복귀·current/App 순서 | 실제 1차 접근/관리 경로·담당/이관 창·C 최종 비교 |
| Recovery·독립 사본 | Host/CA 해시 및 기존 선언·준비 절차, 진단 ZIP PC 추가 보존 기록 | Namespace·나머지 보호 입력·Controller 밖 사본 목적지/복원 담당·실제 복원 |
| 비용·재생성·최종 정리·증거/발표 | 기존 후보 제안·D 원장 재계산/보완 요청·단계별 보존/정리 기준 | 담당 의견/채택·실제 전체 비용·각 환경 실행 결과 |

## SG와 첫 Plan의 오프라인 검사

[검사 도구](../tools/b_preflight/offline_review.py)로 SG ID 맞바뀜(형식/같은 VPC만으로 검출 불가), 프로젝트 AWS 계정/VPC/Component 태그·출력 대응을 대조한다. 이 검사는 관측 파일의 내부 일관성이며 실제 존재·진위/최신성·기존 SG Rule·Worker 소속을 입증하지 않는다. A/C가 새 전용 양식을 작성하도록 요구하지 않고 받은 제한 자료를 B가 연결한다.

첫 Plan 검사는 현재 Root의 초기 두 단계만 대상으로 한다. IAM/OIDC 준비는 Terraform input_contract 1·RHCS OIDC 1·AWS OIDC 1·Operator Role 6·Attachment 6, Cluster 생성 단계는 Classic Cluster 1 추가다. Binding은 null이다. 이 수량은 Terraform 관리 객체이며 CP/Infra/Worker의 실제 AWS 자원 수/비용이 아니다. 생성 후 Binding 및 삭제 단계에는 같은 기준을 재사용하지 않는다.

삭제·양 순서의 교체·Update·이동/import·관리 범위 밖 객체·누락·Role/Attachment 키 불일치·실패/불완전 Plan을 차단한다. 기존 State/no-op과 조회 누락, unknown 조건은 검토 대기로 표시한다. 삭제/교체 집계의 중복을 수정했다. 파일 열기 전후 객체 대조·Linux 소유자/600·JSON 중복/overflow 검사와 값 없는 진단을 추가했다. Windows ACL 및 실제 Linux Controller 실행은 아직 검증하지 않았다.

확장 후 SG/Plan 검사 10개 시험 그룹 통과. 최초 오류 사례 29개에 추가 경계 시험을 연결했으며 실제 SG 인계·Cloud Plan PASS가 아니다. `NO_LISTED_ANOMALY_PENDING_REVIEW`도 실행 승인이 아니다. 실제 Source/Lock/입력 해시·전체 Root 명령(타깃 미사용)·권한/Trust 내용·지원·Quota·비용·창을 별도로 검토한다. [Terraform JSON 형식](https://developer.hashicorp.com/terraform/internals/json-format)을 기준으로 삼았다.

## OCP 순차 교체의 Source requests

현재 GitOps main의 base/lab 11개 파일을 격리 사본으로 받아 Kustomize v5.7.1로 렌더했다. FE/BE 각 1 Replica, maxSurge=1/maxUnavailable=0, old/new requests가 동일한 선언을 기준으로 계산했다.

| 상태 | FE/BE CPU requests 소계 | FE/BE 메모리 requests 소계 | 추가 Pod requests |
|---|---:|---:|---|
| 정상 FE 1 + BE 1 | 125m | 160Mi | 없음 |
| FE 교체 중 | 150m | 192Mi | FE 1개: 25m/32Mi |
| FE old Pod 종료 확인 후 BE 교체 | 225m | 288Mi | BE 1개: 100m/128Mi |
| 동시 교체 비교(선택하지 않음) | 250m | 320Mi | FE+BE: 125m/160Mi |

**표는 FE/BE 선언의 소계이며 Node/Namespace 전체 필요량·최대 실사용·교체 가능 판정이 아니다.** Valkey/Registry/Pruner/다른 Pod, admitted sidecar/init/overhead/LimitRange, 종료 중 Pod는 별도로 더한다. 교체 중 old/new requests가 다르면 새 계산이 필요하다. FE Ready/rollout 완료만으로 old Pod 종료를 대신하지 않는다. [Deployment 종료 Pod의 자원 소비](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)와 [requests 기반 자원 관리](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)를 대조한다.

양 Worker 중 실제 배치 가능한 개별 노드의 CPU/메모리·Pod 슬롯·affinity/taint·현재 requests와 실사용/MemoryPressure, Namespace Quota와 작업창을 함께 확인한다. 단순 두 노드의 잔여량 합계나 과거 272Mi로 승인하지 않는다. [선언 계산 도구](../tools/b_preflight/ocp_rollout_requests.py)의 5개 시험 그룹에서 현재 렌더·추가 일반 컨테이너·단위·Replica/strategy/HPA/init/overhead 변경을 검증했다. 실제 배치 시험은 수행하지 않았다.

## 다음 실행과 완료 판단

- 부분 인계가 오면 그 범위를 먼저 대조한다. 전체 팀 작업 종료를 한꺼번에 기다리지 않는다.
- A/C의 수신 조건 뒤 목적 인증·State 저장소 사전검증과 실제 전체 Plan을 진행한다. 예비 비용 후보 제안은 이미 전달했으며 채택되지 않았다.
- OCP는 자체 공급·자원·창이 충족되면 ROSA와 독립적으로 FE→BE 교체/업무 시험을 진행한다.
- Pool은 RDS 실측/예산 합의, 이관은 실제 접근/제어/날짜, Recovery는 대상/입력/복원 담당 뒤 진행한다. 독립 복구 자료의 실제 사용/복원 가능성은 별도 미완료다.

이 검토 범위에서 추가 보완을 찾지 못한 상태와 프로젝트 전체 완료를 구분한다. 새로운 인계·Source 변경·실환경 결과는 다시 검토하며 Source 준비를 TH/Q·전체 DR/운영 완료로 승격하지 않는다. 멘토링/OADP 보류 유지.

## 도구 사용 범위와 재현

Python 3.9+에서 SG/Plan 도구는 표준 라이브러리만 사용한다. requests 계산에는 PyYAML이 필요하다. 시험은 합성 자료와 고정 Source의 제한 렌더 fixture를 사용하며 Cloud/Cluster/인증/State를 호출하지 않는다.

```bash
python3 tools/b_preflight/test_offline_review.py
python3 tools/b_preflight/test_ocp_rollout_requests.py
```

실제 수신 뒤 B가 보호 경로에 연결할 호출 형태다. 아래 경로 표시는 현재 실행 입력이 아니다. SG 파일은 기존 foundation의 account_id/vpc_id/data_security_groups 제한 사본, rds_security_group_id/redis_security_group_id 제한 출력, 두 SG의 GroupId/GroupName/VpcId/OwnerId/Tags 관측 자료다. 전체 State/Output·Secret 값을 공급하지 않는다. Linux에서는 파일 소유자/600 권한을 검사한다.

```text
python3 tools/b_preflight/offline_review.py sg --inputs <제한입력.json> --outputs <제한출력.json> --observations <SG관측.json>
python3 tools/b_preflight/offline_review.py plan --plan <보호Plan.json> --stage iam-oidc-preparation
python3 tools/b_preflight/offline_review.py plan --plan <보호Plan.json> --stage cluster-create
python3 tools/b_preflight/ocp_rollout_requests.py --render <검토한lab렌더.yaml>
```

SG 결과는 내부 대응 확인, Plan 결과는 나열한 구조 검사, requests 결과는 선언 소계다. 비차단 종료 코드도 실행 승인으로 사용하지 않는다. 참조 Source가 바뀌거나 stage/Replica/strategy/Namespace 등이 달라지면 새 기준을 검토한다. 실제 Controller 도구 실행과 실제 자료 수신·Plan 생성·OCP 변경은 아직 수행하지 않았다.
