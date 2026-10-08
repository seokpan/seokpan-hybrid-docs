# 1차 쓰기 중지·이관 후 App 확인 준비

상태: Source 검토와 준비 절차 작성. 실제 1차 Context/Caller·제어 Owner·사용창·상위 Argo 관리·HPA/다른 쓰기 주체 확인 대기. 이 문서는 중지·복귀·DB 변경을 실행한 근거가 아님.

원본: [Infra17 B 분담 확인](https://github.com/seokpan/seokpan-hybrid-infra/issues/17#issuecomment-6053814538), [C 최신 답변](https://github.com/seokpan/seokpan-hybrid-infra/issues/17#issuecomment-6054742252), [Infra44 v1.5](https://github.com/seokpan/seokpan-hybrid-infra/issues/44). 1차 공식 종료 Baseline은 2026-09-23 유지. 이번 범위는 합의된 이관 쓰기 중지·복귀의 제한된 운영 준비.

## Source와 실제 상태

1차 GitOps 조회 기준 `531119303cafc781657a908ef64506ceb7a8bf4f`.

| 대상 | Source에서 확인 | 실행 전에 읽기 확인할 실제 입력 |
|---|---|---|
| Backend | application/backend, replicas2, 종료 유예45초 | 현재 Image/Replica·Pod/Endpoint·진행 요청/연결·기동 주체 |
| Argo Application | argocd/apps-backend, GitOps main/apps/backend, AutoSync·SelfHeal·Prune 활성 | 실제 Source/Revision·현재 작업·관리 Parent/ApplicationSet·관리 경로 |
| PDB | application/backend, minAvailable1 | 실제 객체와 다른 자동 제어. PDB를 중지 유지 장치로 사용하지 않음 |
| HPA/다른 쓰기 주체 | 조회한 GitOps Source에서 HPA 파일 없음 | 실제 HPA·Job/CronJob·CI/hooks·다른 프로세스/관리 쓰기 확인 |

[Backend Source](https://github.com/seokpan/seokpan-gitops/blob/531119303cafc781657a908ef64506ceb7a8bf4f/apps/backend/deployment.yaml), [Application Source](https://github.com/seokpan/seokpan-gitops/blob/531119303cafc781657a908ef64506ceb7a8bf4f/argocd/applications/apps-backend.yaml), [PDB Source](https://github.com/seokpan/seokpan-gitops/blob/531119303cafc781657a908ef64506ceb7a8bf4f/apps/backend/pdb.yaml). Source 존재를 실제 클러스터 재조회로 사용하지 않음.

## 담당·실행 입력

| 단계 | 담당 | 다음에 넘길 결과 |
|---|---|---|
| 중지 준비·제어 경로·중지/복귀 조율 | B | 읽기 확인·원래 제한 설정·수락한 제어 경로·실행자/창·중지 판정 |
| 복제·최종 Dump·RDS Import/비교 | C | v1.5의 도메인별 GTID/복제/테이블·Schema·Revision·Dump/Import 판정 |
| VPN/RDS 경로 | A | 목적 연결·실제 Endpoint/CA/네트워크 공급 |
| 시간선·증거 | D | 구간별 시각·실행 조합·논리 참조·한계 |

실제 수행자 한 명과 사용창 확정 전 중지/복귀를 실행하지 않음. 보호 기록에는 필요한 기존 Replica/SyncPolicy/HPA·Job suspend/유입 제어의 제한 항목만 보관. Secret 값·kubeconfig·전체 State/Output/Plan을 공개 기록에 넣지 않음.

## 1. 읽기 준비

기존 승인된 1차 관리 환경에서 본인에게 허용된 Context를 명시. Controller의 jth에 kubeconfig·권한이 있다고 가정하지 않음. ROSA/OCP lab Context를 1차 대상으로 사용하지 않음.

```bash
# SRC_CONTEXT는 현장에서 확인한 1차 전용 Context. placeholder 상태에서는 실행 중단.
: "${SRC_CONTEXT:?1차 승인 Context 확인 필요}"
kubectl --context "$SRC_CONTEXT" auth can-i get deployment/backend -n application
kubectl --context "$SRC_CONTEXT" auth can-i get applications.argoproj.io -n argocd
kubectl --context "$SRC_CONTEXT" -n application get deployment backend   -o jsonpath='{.spec.replicas}{" / "}{.status.readyReplicas}{"\n"}'
kubectl --context "$SRC_CONTEXT" -n argocd get application apps-backend   -o jsonpath='{.spec.source.targetRevision}{"\n"}{.spec.syncPolicy.automated}{"\n"}{.metadata.ownerReferences}{"\n"}'
kubectl --context "$SRC_CONTEXT" -n application get hpa
kubectl --context "$SRC_CONTEXT" -n application get jobs,cronjobs
```

공유 결과는 대상 일치·권한·Replica·자동 동기화/Parent·쓰기 주체의 값 없는 판정과 필요한 Source/Revision만 기록. 전체 객체/Secret/DB 행 내용 출력은 제외. 권한 부족·Context 불명확·진행 중 Sync·미확인 쓰기 주체가 있으면 변경 단계 중단.

## 2. 중지 상태를 유지할 제어 경로 수락

단순 scale0은 Source의 replicas2로 복구될 수 있음. 다음 중 실제 관리 구조에서 유효한 한 경로와 복귀 방법을 지정 Owner가 수락.

- GitOps 유지 경로: 검토한 유지보수 개정에서 필요한 Backend desired replicas0/HPA·Job·유입 제어를 표현하고 정확한 Source로 적용. Argo가 중지 desired state를 유지하도록 확인. 실제 1차 Source 변경/PR·Sync는 아직 미수행.
- 제한된 수동 경로: Source 변경을 쓰지 않는 경우 자동 동기화/상위 관리·HPA 등 재기동 제어를 원래 설정과 함께 제한된 범위로 중지한 뒤 Backend 중지. Parent/ApplicationSet이 설정을 되돌릴 수 있으면 Child만 변경하지 않음. 버전·권한·현재 설정 확인 후 대상별 명령 확정.

두 경로를 동시에 실행하거나 수락하지 않은 우회 경로를 사용하지 않음. Application 삭제/finalizer 제거·Namespace 삭제·DB read_only/계정·GRANT·MaxScale·Storage 변경을 중지 수단으로 사용하지 않음. [Argo 자동 동기화 안내](https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/)의 SelfHeal과 Parent 관리 조건 대조.

## 3. 이관 당일 중지·C 인계

1. B/C/A/D: 작업 시간·연락·중단·실제 수행자·복귀 기준 확인, D 시간선 시작.
2. B: 승인한 유입 제어로 신규 쓰기/새 연결 차단, 기존 요청·WS 연결의 종료/유예 처리. 유입 차단만으로 기존 연결의 쓰기 중단을 판정하지 않음.
3. B: 재기동 제어가 수락 경로대로 유지되는지 확인, Backend 중지.
4. B: desired/actual Replica0, Backend Pod 종료·Service Endpoint 제거 및 HPA/Job/Parent가 재기동하지 않음을 반복 읽기 확인. 남은 쓰기 주체가 있으면 C 최종 Dump 시작 불가.
5. C: Primary 마지막 쓰기의 Replica 반영·도메인별 GTID/복제 상태·Data 비교를 v1.5대로 판정. DB는 읽기 확인만 하며 값이 달라지면 Dump/이관 중단.
6. C: 최종 Dump 직전~RDS Import/비교 완료 구간 동안 B가 중지 유지. 실제 이벤트 시각·논리 Dump 참조·실행자와 실패/대기 기록.

[Infra44 v1.5](https://github.com/seokpan/seokpan-hybrid-infra/issues/44)의 비교 기준은 당일 최종 Dump의 행 수·해시·Schema·Alembic Revision. 10/02 값은 이력. Replica의 과거 추가 도메인 때문에 GTID 전체 문자열 일치로 되돌리지 않음.

## 4. 이관 후 2차 ROSA 확인

- C RDS Import/데이터 비교와 계정/TLS/GRANT·실제 DB Host/Name/CA 수락 후 B 진행.
- 승인 Backend Image와 같은 Digest의 단일 Migration Job에서 `seokpan-migration-gate current` 읽기 확인. Cloud 대상 Namespace·목적 Secret/CA·Host/Port/Name·수락 Deadline/사용창을 사용. lab의 placeholder Job을 그대로 실행하지 않음.
- 기대 Code head와 실제 DB Revision 비교. 현재 새 Image 대상 App의 Source head는 `20260902_0002`이며, 실제 Image/DB 확인으로 수락. 불일치하면 중단; upgrade/stamp를 자동 실행하거나 Schema Guard를 약화하지 않음.
- C의 계정/데이터 수락·정확 Source/Image·Gate/live Diff 확인 후 B Backend 기동, Ready/TLS·로그인·랭킹·방/게임 등 대표 업무 확인. Frontend/Origin/WS·증거를 D와 같은 조합으로 연결.
- 첫 백업은 C의 별도 단계. 실제 서비스 전환과 1차 재개 여부는 RDS 비교·Migration/App·백업/운영 조건을 함께 확인해 결정. Cloud에 새 쓰기가 생기면 1차로 단순 복귀하지 않음.

## 5. 중단·복귀

쓰기가 계속 발생하거나 중지 상태가 유지되지 않으면 최종 Dump 시작/진행 중단. 불일치·Import 실패·TLS/Revision/업무 실패는 원인과 데이터를 보존하고 C/B가 다음 경로를 판단. 배포 실패를 DB 이관 성공/실패로 혼동하지 않음.

1차 재개가 수락된 경우 기록한 원래 Replica·HPA/Job·Argo/Parent·유입 설정을 선택한 제어 경로로 복원, Ready/대표 업무 후 유입 개방. source가 아직중지 상태인 채로 manual Replica만 늘리거나, Cloud 새 쓰기 이후 구 데이터를 자동 재개하지 않음. DB/Redis/PVC/기존 자료 보존.

## 준비 종료와 실제 실행의 구분

- [x] 원 분담·C v1.5·1차 Source·중지/복귀 순서 정리
- [ ] 실제 1차 Context/Caller·Parent/HPA/다른 쓰기 주체 읽기 확인
- [ ] 실행 제어 경로·실제 수행자·사용창·복귀 설정 수락
- [ ] 이관 당일 중지 유지·C 최종 Dump/Import/비교·2차 current/App/첫 백업

이 준비와 OCP 새 Image 공급은 ROSA 첫 Plan의 일괄 선행조건이 아님. ROSA Root 입력/권한/지원/비용/창 사전검증을 병행. T05/전체 서비스 전환·DR 수치 달성·TH/Q 완료는 별도 실제 Run으로 판정.
