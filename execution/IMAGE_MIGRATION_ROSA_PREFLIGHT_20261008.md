# 새 Image·이관 준비·ROSA 사전검증 연결 — 2026-10-08

FE(Frontend, 사용자 화면)·BE(Backend, 서버 처리)의 새 이미지 공급, 1차 이관 준비, ROSA(Red Hat OpenShift Service on AWS) 첫 Plan 준비를 분리해 연결한다.

## 새 OCP Image의 고정 Source

- 기존 승인 Image: App `46e21a74dd608b41f2c12a0a57d76bddfcf25949`, `git-46e21a74dd60`, [D 공급 원본](https://github.com/seokpan/seokpan-hybrid-gitops/issues/14#issuecomment-6016144794).
- 새 Build 대상: App `5df2ce280188a7e3874fa370ec8116d50ca34af3`. 태그 규칙상 후보 `git-5df2ce280188`; 새 Build/Scan/Digest 승인 태그로 이미 존재한다는 뜻이 아님. 이후 main 변경은 이 Build Source에 자동 승계하지 않음.
- Migration 디렉터리 6개 파일의 구/신 Git Blob 동일, 두 Source의 Alembic head `20260902_0002`. 실제 Image의 heads·Source label·SBOM/Scan/Digest·포함 파일은 D 새 Run에서 확인. 실제 DB current는 별도 C/B 검증.
- 병합 App 수정은 포함하지만 아직 main에 없는 개인 App2/GitOps2개 Branch의 변경을 포함했다고 표시하지 않음. 추가 병합 App #29는 Promotion의 GitHub Transport 구현으로 Backend/Frontend Runtime·Migration 변경 없음. App `17310a54`에서 최신 `5df2ce28`로 Build 기준 갱신, 실제 Image 생성/배포는 별도.

## D의 공급 Issue·ZIP 보존

- 기존 GitOps #14는 최초 Context/Registry 경로·입력/승인 Image 공급 이력. 새 FE/BE 재공급·현재 Source/Scan/Digest/내부 mapping·신규 Pull·Rolling/rollback·현재 Owner/창은 새 D Issue에서 추적하고 #14/#10/App2를 연결.
- 새 Issue 번호와 계속될 사용창 담당/원 #5 연결을 남긴 뒤 #14를 최초 인계 범위로 정리/종료 가능. D의 Issue 본문/종료는 이 변경에서 수정하지 않음.
- Run 37330480298/artifact 11353184732 진단 ZIP의 현재 작업 PC 사본 확인: 9020 bytes, SHA256 `4472b0bf42034b02567afbfe1aae97fdc24f3589b9ec5862e6e1278f0681cd62`, 내부 8개 렌더 체크섬 PASS. D의 로컬 보존 보고와 현재 PC 추가 사본을 연결. D 파일의 현재 가용성이나 물리적 장애 영역을 직접 검사한 결과는 아님.
- ZIP의 Source `6ea2d9a`는 당시 진단 이력. 최신 실행 Manifest·새 Image/Recovery Bundle의 대체물 아님. 원본/해시·보관/접근·만료 전 별도 보존을 유지하며 공개 경로 대신 논리 참조 사용.

## 현재 lab 자원·순차 교체

- [D GitOps #14](https://github.com/seokpan/seokpan-hybrid-gitops/issues/14): worker-2 requests 여유 약 272Mi, 10/08 14:3x 유휴 관측. 이번 직접 재조회나 실행 창 수락 아님.
- Source: lab FE/BE 각각 1 Replica, BE 100m/128Mi 요청·500m/256Mi 제한, FE 25m/32Mi 요청·250m/64Mi 제한. maxSurge 1/maxUnavailable 0. Valkey 1개 유지, Migration suspend.
- 기본 교체는 한 Deployment씩 진행하는 후보. FE 교체 완료·old Pod 종료/자원 재조회 후 BE. FE 32Mi 또는 BE 128Mi 추가 예약, 동시 두 교체라면 최소 160Mi 추가지만 이 숫자만으로 안전/배치 수락하지 않음.
- 양쪽 Worker의 최신 Allocatable−admitted requests·실사용/MemoryPressure·CPU·Quota/LimitRange·sidecar/init/overhead·종료 중 Pod·Pruner/우선순위 작업을 확인. [Kubernetes 자원 안내](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)·[Rolling 동작](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) 대조.
- 기존 DB/Redis/PVC/team4/NFS 기본 유지. 부족하면 새 시험 중단·다른 창 또는 기존 FE/BE만 별도 수락 범위에서 조정. requests를 임의 축소·노드 강제 고정·공유 Workload 선점으로 해결하지 않음.
- 실제 순차 Sync/교체는 새 Digest·Source·Root targetRevision·Gate/live Diff·Owner/사용창/실행 경로 수락 후. Schema 변경 없는 Image 교체 때문에 held Migration을 해제하거나 Valkey Sync를 반복하지 않음. migration Image 참조의 새 승인 BE Digest 연결은 Source 검토 후 별도, 실행과 구분.

## B의 이관 작업

원 [Infra #17 B 분담](https://github.com/seokpan/seokpan-hybrid-infra/issues/17#issuecomment-6053814538)과 [C v1.5](https://github.com/seokpan/seokpan-hybrid-infra/issues/44)는 이미 연결돼 있으며, 본인 작업표에 다음을 독립 항목으로 관리.

1. [1차 중지 준비](FIRST_SERVICE_WRITE_STOP_PREPARATION.md): 실제 Context/제어 Owner·AutoSync/Parent/HPA/쓰기 주체 읽기, 중지/복귀 경로·실행자/창 수락.
2. 이관 당일 쓰기 중지 유지: C 최종 Dump 직전~RDS Import/비교 완료, 이후 전환/재개 판단 전까지 수락 상태 유지.
3. C 비교 수락 후 ROSA 단일 Migration current·Revision·Backend Ready/대표 업무, C 첫 백업·서비스 전환/1차 재개 여부 별도.

C의 실사용자 취급 판단·복제/Data 사전 확인 보고는 원 #17/#44에서 수신. 이번 변경은 C의 Runbook/데이터·기존 §8 기록을 수정하거나 법적/실행 수락을 대신하지 않음.

## ROSA 첫 Plan의 준비 묶음

| 묶음 | 실제 상태 | 다음 담당·입력 |
|---|---|---|
| 인증·공식 정책/사본 | B Controller 인증·필수5/5·사본17해시/권한 PASS | 성공 조회 반복 없음. A 보호 전달/수신은 대기 |
| Controller 읽기 사전검증 | 기존 clone/원격/개인 변경/Lock·Core·실제 Operator 목록/기존 정책 대조 블록 준비, 문법/합성3개 검사 PASS | B jth@ansible에서 실행. 새 실제 결과는 아직 NOT RUN |
| 기반/권한/입력 | A #47/#23·C/A 실제 SG2·Backend 공급 개정·Actual Policy ARN Map 미수신/미수락 | A/C 공급, B 대조. Backend 권한과 서비스 권한 분리 |
| 실제 Caller/Backend·지원 | 개인 목적 세션·기존 Workspace/State 위치·Provider/Lock·지원 stable 4.20 GA patch/구독/Quota/disk 미확인 | B실제 보호 Workspace/목적 Role·A 관련 권한·프로젝트 Red Hat 조직/AWS/OCM 연결 |
| 예비 비용/실행 창·첫 Plan | Cost PARTIAL/$450 계획/$500 한도, 첫 실제 전체 Plan 미실행 | B예비 입력·A/D 관련 수락·Owner/창 → 전체 Root Plan. 유료 생성 승인은 실제 Plan 뒤 별도 |

읽기 블록은 Git fetch로 원격 참조만 갱신하고 Core version·Red Hat sts_credential_requests를 조회. AWS/IAM·파일 수정/State/init·Plan/Apply 없음. 실제 Catalog 역할 6개 Guard와 제공 정책 ID 대조, A의 account_role_prefix `seokpan-fnd-rosa`·RHCS 1.7.7의 64자 규칙으로 예상 Map Key 생성. 실제 ARN/권한/조직 연결 수락 아님. API 목록 변화·정책 누락/키 충돌은 Source/Owner 검토로 처리하고 Guard를 약화하지 않음.

문서 Source/읽기 준비 완료를 실환경 사전검증 전체 PASS로 사용하지 않음. OCP 철거·전체 이관/Recovery를 첫 Plan 선행조건으로 만들지 않으며 같은 State 쓰기·Restore/장애/삭제는 지정 실행자/창으로 조율. 멘토링/OADP는 보류.
