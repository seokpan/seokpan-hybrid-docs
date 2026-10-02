# 石나가는 판단 2차 프로젝트 05 구현·통합·검증 진행 기록

> **현재 단계:** 05 협업 진행본 — 저장소 공유와 현행 작업·입력 인계 연결
> **기준일:** 2026-10-02 KST. 이전 01:27 KST Source 관측은 보존하며 후속 Source/권한 관측과 팀 보고는 공통 진행표에 별도 연결
> **상태:** 사용자 04·개정 지침 등록 완료 확인. 네 저장소 main/Tree/Branch/PR/Issue 읽기 점검과 팀 전체 진행 안내 보강. 앞선 B 로컬 초안은 보존. 팀의 Infra 병합·OCP 보고와 AI의 Source 관측·로컬 검사·미실행 Runtime을 구분
> **기준:** 승인된 01/02/03, 닫힌 `04_IMPLEMENTATION_READINESS.md`, 최종 개정 `PROJECT_INSTRUCTIONS.md`, 사용자 최신 명시적 결정
> **기간/한도:** 2026-09-28~2026-10-26, 10/16 Technical Freeze, $450 계획선+$50 여유=$500 한도
> **공유와 종료:** 공유 반영은 [PR #5](https://github.com/seokpan/seokpan-hybrid-docs/pull/5)의 병합 Metadata로 확인한다. 변경은 Branch/PR에서 검토하고 개인별 읽기/쓰기 접근·실제 팀 도입은 별도 확인한다. 05 최종 종료는 구현·검증·정리 후다.


**팀원이 시작할 위치:** [실행 안내](README.md)에서 읽는 순서를 확인하고, [공통 진행표](WORK_TRACKER.md)에 자기 작업과 입력 인계를 연결한다. [인계 양식](HANDOFF_TEMPLATE.md)은 해당 작업 Issue의 제출/확인 기록으로 사용한다. 실제 실행 결과는 [Evidence 안내](../evidence/README.md)의 Run별 양식으로 남긴다.

2026-10-02 02:32 KST 조회 시 승인00~04의 [설계 등록 PR #3](https://github.com/seokpan/seokpan-hybrid-docs/pull/3)는 main 미병합이었다. 이번 공유 작업에서 그 고정 Commit의 원문5개와 첨부의 Git blob 바이트 동일성을 확인했다. 설계 파일을 이 PR에서 중복 등록하지 않는다. 프로젝트 지침은 사용자 등록본을 따르며 이 PR의 새 사본으로 대체하지 않는다.

현재는 설계 PR #3·실행 PR #5·발표 PR #7 모두 병합돼 main에 있다. 이전 조회는 이력으로 보존하고 현재 계정/Source와 다음 인계는 §0.18·§8·[진행표](WORK_TRACKER.md#next-handover)를 따른다.

**추가 자료와 최신 후속:** [2026-10-02 자료 수용·권한 계약·현재 작업](#supplement-20261002)에서 I03 부분 접수, GitOps #7 종료 범위, App #1·GitOps #5/#6 및 Infra #14/#15를 확인한다. 과거 관측은 유지하고 현재 상태는 진행표에 연결한다.

**복구 목표 피드백 후속:** [§9 복구 예행과 목표 재검토](#recovery-objective-review-20261002)는 현 구조에서 가능한 개선·사용자 영향·팀 부담을 확인하는 실행 준비다. 승인된 RTO 30분·영속 DB RPO 90분·운영 중 1시간 백업은 변경 결정 전까지 유지한다.

**정태훈 전체 실행·등록 후속:** [§9.11 전체 작업 등록과 ROSA 입력 준비](#tjung03-registration-rosa-input-20261002)에서 실제 상위/실행 Issue, TH-01~19·81개 세부 식별자의 기존 연결과 ROSA 후속 HCL 수신계약·Registry/CI Source 수신 조건을 확인한다. 기존 §9.9/9.10의 구현·검사/미실행 경계는 보존한다.

현재 진행 현황:

- [x] 03 상세설계와 04 운영 결정·구현 인계 완료
- [x] 두 최종 문서의 프로젝트 소스 등록 완료 사용자 확인
- [x] 01:27 KST 기준 네 저장소 main/전체 Tree·Branch·PR/Issue 읽기 점검
- [x] 팀 전체 05 범위·역할·작업 인계·OCP/ROSA 구분·증거/비용 종료 안내 연결
- [x] 네 사람의 첫 작업·기록 책임·수신자 확인·공유 실행 충돌 처리 보강
- [x] 3회 연쇄 검토·보완 후 재검증 수렴 — 최종 추가 보완 0건
- [x] 공통 문서/진행표 경로와 기존 작업·입력 보고 연결 — 현재 확인 범위는 진행표
- [x] 네 사람의 명시 GitHub 계정 매핑·네 저장소 권한 API 16건 확인 — 모두 admin
- [ ] 개인 본인환경의 실제 사용·현재 미반영 작업과 실행 입력 인계
- [x] 앞선 B App 연결·GitOps 로컬 초안과 수행 가능한 검사 — 해당 범위 24건 PASS
- [ ] 실제 이관 Seed·실습 Overlay·Image/Secret 입력 확정과 저장소 반영
- [ ] AWS 생성·Cloud 통합 — 실제 Plan·비용·담당 실행 조건 확인 후
- [ ] 장애·복구·부하 시험과 결과·시연·정리

**승인된 상세설계와 운영 결정·실행 인계 문서는 04 종료로 완료됐다.** 05는 네 사람의 구현·통합·검증과 발표 준비·자원 정리까지 연결하는 실행 기록이다. 실제 값·코드·시험 결과는 남아 있으며 별도 Gate로 판정한다. 현재 정의된 주 문서 흐름은 05까지다. 이후 번호를 추가하는 필수 계획은 확정되지 않았다.

**팀은 05의 최종 완료를 기다리지 않는다.** 검토한 작업 안내를 먼저 공유하고, 각 담당자는 자기 작업의 입력·범위·완료 증거를 확인해 독립 준비를 진행한다. 결과는 각자가 Issue/PR/Run에 직접 남기며 수신자가 인계를 확인한다. 05는 이를 연결해 진행 중 계속 갱신하고 마지막에 최종 결과를 닫는다. 정태훈이 모든 사람의 일을 일일이 배정·수집·대필하는 운영을 전제로 하지 않는다.

| 작업 순서 | 현재 상태 | 무엇을 하면 끝나는가 |
|---|---|---|
| 1 설계와 운영 책임 | 완료 | 승인된 03·04·지침 등록과 종료 확인 |
| 2 App·GitOps 코드 준비 | 첫 로컬 묶음 완료, 실제 이관·Build/Kustomize·실습은 남음 | 연결 설정·배포 선언 작성, 로컬 검사, 실제 이관/실습 인계 준비 |
| 3 AWS·ROSA 코드와 실행 입력 | 담당별 진행 상태 인계 필요 | foundation 인계·ROSA 코드·실제 도구/계정/Backend·검토된 Plan |
| 4 Cloud 생성과 통합 | 이 기록에서 실행 전 | 비용 확인 후 생성, Image/Secret·Data 연결·로그인/게임/WS·Backup 정상 시험 |
| 5 장애와 복구와 부하 | 최종 시험 전 | 검증 조합으로 장애·재생성·Offline 복구·부하의 실제 결과 확보 |
| 6 결과와 시연과 정리 | 실행 결과 확보 후 | Must 판정, Runbook·기여·시연·잔존 비용과 보존 책임 정리 |

앞선 첫 코드 작업은 **정태훈 담당 App 연결·GitOps base/Overlay**이며 §7에 보존한다. 현재 진입 정리는 네 사람의 진행을 통합하는 범위다. PR #12는 이번 Metadata 조회에서 병합을 확인했으며 과거 읽기 검토를 현재 미해결 작업으로 취급하지 않는다. 당시 이력은 §3.3에 남긴다.

## 0 팀 전체의 05 진입 안내

### 0.1 지금 완료된 것과 앞으로 완료할 것

01은 목적·범위·성공 기준, 02는 목표 구조, 03은 상세설계·기술 계약·시험·비용 기준, 04는 사람별 운영 결정과 구현 인계다. 00은 역사적 출발점이다. 승인된 구조와 실행 책임은 닫혔고, 05는 그 기준을 실제 Source와 환경에 적용한 결과를 남긴다. 새 06 실시설계를 먼저 완성해야 구현을 시작하는 흐름은 현재 없다.

실제 AZ ID·Endpoint·Host 용량·계정 정책·지원 조합·현재 가격·측정 Resource/Pool처럼 환경에서 확인해야 하는 값은 구현 상세화에 해당한다. 코드/정적 검사, 실제 Plan/실행 준비, 배포 성공, 업무/장애/복구 Acceptance는 서로 다른 완료 상태다. 문서 종료로 다음 상태를 미리 통과시키지 않는다.

| 구분 | 현재 의미 | 완료 판단 |
|---|---|---|
| 설계 기준 문서 | 03·04 승인/등록·종료 | 결정·책임·의존·인계의 문서 검토 수렴 |
| 작업별 준비 | W02 입력과 W03/W04 구현·예행 연결 중 | 해당 작업의 실제 입력·Source·도구·인계 확보 |
| 핵심 구현·통합 | 목표 10/16 Technical Freeze | Cloud 정상 업무·Data·CI/Pull·관리·복구 자료가 연결되고 주요 Must 결함 정리 |
| 최종 검증 | 목표 10/19~21 | 검증 조합으로 재생성·장애·부하·Offline 복구와 정량 결과 확보 |
| 시연·발표 준비 | 10/22 Demo Freeze, 10/23 Presentation Ready 목표 | 실제 결과·제한·영상·보고/발표 근거가 연결 |
| 비용·프로젝트 종료 | 10/26 종료 목표, 보존/청구 확인은 책임 기록 | 불필요 유료 자원 정리·잔존/보존 책임·최종 Must 판정 |

날짜는 승인된 목표다. 네 사람의 실제 가용시간·진행·단가·가동시간을 확보하기 전 완료일을 확약하거나 전체 완료율을 산출하지 않는다.

### 0.2 최신 저장소 관측과 팀 보고

조회 시각은 2026-10-01T16:27:32.695Z, 같은 시각의 KST는 2026-10-02 01:27:32.695+09:00다. main recursive Tree는 네 곳 모두 truncated=false였고, 조회 가능한 Branch는 main 하나씩, 열린 PR은 없었다. 개인 작업 사본·미커밋 변경의 부재를 뜻하지 않는다. 이후 변화는 새 시점/Commit으로 기록한다.

| 저장소 | 조회 main 전체 SHA | 확인한 Source·진행 | 다음 연결 |
|---|---|---|---|
| [Infra](https://github.com/seokpan/seokpan-hybrid-infra) | `c9a3e797a436bef32a5e7d14b9d8fce58e28a574` | bootstrap HCL/Lock/Backend·세션 script 존재, PR #11/#12 병합. foundation/rosa/ansible은 README뿐 | 현 실행 결과·미반영 작업을 담당 인계로 연결하고 foundation/rosa 실제 구현 준비 |
| [App](https://github.com/seokpan/seokpan-hybrid-app) | `6902f3a184b4f1f07ade782536335a88d72612fc` | README·.gitignore. 실제 App 이관은 main에서 미확인 | 최신 검증 1차 Source·Seed/미반영 변경 확인 후 독립 2차 이관 |
| [GitOps](https://github.com/seokpan/seokpan-hybrid-gitops) | `523e9206dd6398adc6776855573890063b837a85` | README·.gitignore. #1 OCP lab 열림, #2~4 UWM/Argo/정책·웹훅 관련 lab 보고 닫힘 | 미커밋 lab Overlay 원본/조건을 확보하고 실제 hybrid base/Overlay를 검증 |
| [Docs](https://github.com/seokpan/seokpan-hybrid-docs) | `eb36bf10499d29b414a9e02c3f2569dde4d9ef1e` | README. 실행 Ledger/Evidence Index의 main 반영은 미확인 | 승인 기준의 위치·개정과 Source/Run/Evidence를 연결할 문서 인계 |

PR #12의 Metadata 병합 시각은 2026-10-01T11:02:14Z이다. 이번 점검은 해당 PR diff/권한의 재심사나 댓글·변경·Merge 작업을 포함하지 않는다. Merge 관측이 실제 Apply/Role 시험 성공을 증명하지 않는다.

팀 OCP Issue의 닫힘은 해당 lab 범위의 종료 보고다. #1의 9항목, #2의 UWM, #3의 공개 Argo 예제, #4의 Ingress 정책/웹훅 결과를 실제 hybrid base·ROSA·실제 메일 수신·전체 Egress 검증으로 확대하지 않는다. 상세 Source/조건과 Runtime 원본은 지정 담당자의 인계에서 확인한다. #1의 옛 짧은 SHA/임시 넓은 DB 권한·미커밋 Overlay와 #3의 lab GitOps 버전·예제 경로는 최종 검증 조합과 구분한다.

이번 main 하위 README에도 foundation/rosa Key가 `foundation/terraform.tfstate`·`rosa/terraform.tfstate`로 남고 상세설계 뒤 CIDR/Sizing/API를 결정한다는 옛 표현이 있다. 루트 README와 승인03/04는 `phase2/foundation/terraform.tfstate`·`phase2/rosa/terraform.tfstate`와 이미 승인된 구조를 따른다. 이는 담당 구현 PR에서 문서/HCL/Backend 예시를 정합화할 Source 항목이며, 실제 State 재이전이나 설계 재선택을 지시하는 것이 아니다. 이전 §3.2 S05-01의 관측이 이번 SHA에서도 남아 있다.

후속 Source 관측은 `2026-10-01T18:07:38Z` / `2026-10-02 03:07:38+09:00`다. Infra/App/GitOps main SHA는 위와 같았고 기존 Bootstrap 실행 보고·OCP lab 보고를 [진행표](WORK_TRACKER.md#current-observation)에 연결했다. Docs에서는 설계 PR #3·실행 PR #5·발표 PR #7이 병렬 진행 중이었다. 현재 역할별 작업·I01~I07 부분 보고·권한 조회와 남은 인계는 [진행표](WORK_TRACKER.md)와 [Issue #8](https://github.com/seokpan/seokpan-hybrid-docs/issues/8)을 정본으로 확인한다. 기존 표를 새 Runtime 판정으로 덮어쓰지 않는다.

### 0.3 네 사람의 작업과 인계

최신 사람 배정은 04 §2.2다. 과거 트랙 표의 미확정 이름 표현보다 우선한다.

| 담당 | 독립적으로 준비할 작업 | 통합 전에 넘길 결과 |
|---|---|---|
| 이유빈 | bootstrap/foundation 전체 통합·Network/Hybrid·Host/최소 Ansible·실제 실행 환경 | 검토된 전체 Root Plan·정본 Backend/Caller·기반 연결 결과·필요한 비밀값 아닌 Output 입력 개정 |
| 정태훈 | rosa Root·App·GitOps base/환경 Overlay·관리 인증·Release/Recovery App | 실제 Source/Seed·검증 Manifest/설정·업무/Pool 계약·ROSA Context/Host·배포 조합 |
| 김상희 | foundation Data 선언·DB TLS/GRANT·이관·Backup·격리 Recovery DB/새 Redis·Restore | Schema/권한/CA 참조·검증 Backup ID/Hash/Data 기준 시각·Restore 결과와 업무 재개 조건 |
| 최유준 | foundation Registry/CI 권한 선언·Jenkins/ECR/Harbor·실제 base의 OCP lab·Native/UWM·Harness·비용/Index | Build/Test/Scan·Image Digest/플랫폼·Push/PR/Pull 결과·관측/측정 준비·비용·증거 연결 |

김상희와 최유준이 foundation의 자기 영역을 작성해도 별도 State나 독립 Apply가 생기지 않는다. 이유빈이 Root 전체를 통합·실행한다. rosa 실행과 App 배포 변경 조율은 정태훈, Data Restore/Cutover는 김상희, 시험 일정·증거 Index 조율은 최유준이다. 영역별 결과와 실패 기록은 각 담당자가 작성하고 관련자가 리뷰한다.

같은 State 쓰기, 공유 Cluster/Root 변경, DB Restore/Cutover, Worker·DB·Redis 장애 주입과 부하는 지정 실행자와 인계 순서대로 수행한다. 코드·Render·로컬 Restore·시험 도구 준비는 병행한다. 사람마다 맡은 작업 수가 같아야 한다는 전제 대신 통합 부담과 실제 가용시간을 확인하며, 특히 이유빈의 foundation 통합과 정태훈의 ROSA/App 동시 부담을 일정에 반영한다.

### 0.4 실제로 진행하는 순서

| 순서 | 수행 내용 | 다음 단계로 넘기는 조건 |
|---|---|---|
| 현행 연결 W02 | main/PR/Issue와 미커밋·Controller/lab 작업·팀 보고의 출처를 연결 | 작업별 담당·전체 SHA·조건·남은 입력·현재 결과가 구분됨 |
| 구현과 예행 W03/W04 | 독립 Root/App/base/CI 코드, 입력 양식, Image Build/Test/Scan·Render·격리 Restore·Harness 준비 | 실제 도구의 해당 검사와 인계 결과 확보. 로컬 합성 검사로 대체하지 않음 |
| 생성 전 비용 W05 | 실제 Plan·지원/Quota·가격/Credit·누적/잔존·Window·재시험/정리 비용 확인 | 전체 계획 ≤$450, $50 여유 포함 총 $500 한도와 실제 실행 조건 충족 |
| 정상 통합 Window A W06/W07 | 기존 bootstrap 정본→foundation→rosa 인계, Data/Secret/Pull/GitOps/대표 E2E·Backup 정상 연결 | 정상 Baseline·복구 자료·통합 결함 조치·검증 Release 확보 |
| 최종 시험 Window B W08 | Clean Recreate→정상 Baseline→분리된 장애 Case→부하, 격리 Offline Recovery | 실제 수치·데이터/업무 확인·실패/재시험·제한과 Must 판정 |
| 결과와 정리 W09/W10 | 비교·Troubleshooting·영상·발표/보고·보존·유료 자원 정리·잔존 비용 | 증거 접근/무결성·검증 조합·실제 기여·최종 판정·정리와 보존 책임 연결 |

Window는 ROSA를 필요한 기간에 생성·사용·삭제하는 가동 구간이다. 최신03의 기본 계획은 정상 통합 A와 최종 검증 B다. 두 Window의 실제 시작/종료·가동시간은 팀 시간과 비용 입력을 받아 채운다. 02의 추가 Demo Window 예시를 필수 C로 늘리지 않는다. 살아 있는 서비스를 보여줘야 하는 요구가 있으면 영상/증거로 충족 가능한지 먼저 확인하고 추가 가동이 필요한 경우 남은 비용·일정에 반영한다.

새 관측마다 01~04 기준과 대조해 이미 정합한 구현, 승인 기준에 맞출 구현 보완, 아직 착수하지 않은 항목, 실제 결과를 기다리는 항목으로 구분한다. 단순 미확인 입력 때문에 모든 작업을 중단하지 않는다. 현재 제약이 승인 구조·범위·권한·성공 기준·기간/비용을 실질적으로 바꾸면 원인·기존/새 상태·직접/후속 영향·대안·결정을 기록하고 필요한 선택을 묶어 사용자에게 제시한다. 평상시 코드/실측 기록은 05에 누적하고 닫힌03/04를 매번 재개하지 않는다. 승인 기준 자체가 변경되면 관련 기준도 결정 후 함께 현행화한다.

### 0.5 OCP 사전 검증과 ROSA 최종 검증

| 영역 | OCP/로컬에서 먼저 확인 | 실제 ROSA/AWS 또는 최종 복구 조합에서 확인 |
|---|---|---|
| App | Image·임의 UID/SCC·Probe/종료·Route/HTTP/WSS·인증/재접속/중복 Case | 실제 3 Replica/AZ 배치·Ingress·RDS/Redis와 대표 업무·Resource/Pool |
| GitOps | 실제 base/Overlay Render·Sync/SelfHeal·Secret/삭제 보호·권한 | 실제 Classic 설치 조합·관리 인계·재생성 후 Context/Host/Secret과 Sync |
| Data | 테스트 DB/Redis의 Driver·CA/Hostname 검증·거부 Case·Migration 예행 | 실제 Endpoint/목적 권한·TLS·RDS/Redis Failover·업무/Data 일관성 |
| CI/Pull | Build/Test/Scan·PAT/Job·Harbor와 lab Pull | 실제 ECR 새 Worker/캐시 없는 Pull·12시간 이상 지속 사용 후 새 Pull·재생성 후 Pull |
| Network/관측 | lab 정책·UWM/Alert 경로·수집기·Harness | AWS Route/SG/WireGuard·정상 Cloud의 On-Prem 비의존·실제 장애/Metric/Alert 상관 |
| Recovery/재현/비용 | 격리 Restore·자료/Key/도구·Bundle 예행 | 실제 검증 Backup/Release로 외부 신규 조회 없는 Offline 복구·RTO/RPO·Terraform Clean Recreate·실제 비용 |

OCP에서 확인 가능한 해당 Case는 먼저 수행해 유료 시간의 문제 발견 비용을 줄인다. 그러나 환경/버전/Source/Digest/조건이 다르면 같은 결과로 판정하지 않는다. 로컬 독립 복구도 실제 최종 조합과 장애 조건으로 수행하면 T18의 본 검증이 될 수 있다. 단순 실습 Restore와 실제 Offline Acceptance를 구분한다.

### 0.6 승인 일정과 현재 미정인 시간

| 목표 창 | 작업 |
|---|---|
| 10/1~10/2 | 설계 기준 종료·Source/실행 입력 연결 |
| 10/5~10/8 | Foundation/핵심 PoC·Window A 후보 |
| 10/12~10/15 | Migration/통합·핵심 결함 해소·복구 자료 |
| 10/16 | Technical Freeze |
| 10/19~10/21 | Window B 후보·재생성/장애/부하/Offline 검증 |
| 10/22 | Demo Freeze |
| 10/23 | Presentation Ready |
| 10/26 | Final Buffer/발표·프로젝트 종료 목표 |

근거는 03 §3-H.4와 04 §9다. 주말·공휴일을 자동 가용시간에 넣지 않는다. 기술 동결 뒤에는 핵심 Must 결함 조치·필요 재시험에 집중하고 구조 확대는 기존 변경 기준을 따른다. 실제 일정이 위 목표를 못 맞추는 제약은 진행표에서 바로 드러내며 뒤로 숨기지 않는다.

### 0.7 발표와 보고에 사용할 측정과 증거

발표 자료를 만들 때부터 값을 찾기 시작하지 않는다. 요구→측정값→비교 기준→목표→실측→원본→해석의 연결을 시험 전에 만든다. Charter의 12개 성공축과 03의 T01~T23 통합 시험을 사용하며 IF/IM/Data 하위 Case를 이어 관리한다. 새로운 번호로 기존 요구를 누락하지 않는다.

| 항목 | 승인된 목표와 측정 경계 |
|---|---|
| 부하 | Smoke 10명/5분, Baseline 30명/15분, Target 60명/30분. 모두 Warm-up 이후이며 실제 Room 인원·행동/HTTP/WS 비율을 기록 |
| 정상 HTTP/WS | 대표 HTTP 업무 p95 ≤1초, Client가 업무 결과를 …19809 tokens truncated…urrent-observation)에 기록한다. Infra [PR #14](https://github.com/seokpan/seokpan-hybrid-infra/pull/14)는 새 유효 모드의 세션 발급 전 이전 세션 해제와 실패 시 Caller 표시를 반영했고 [PR #15](https://github.com/seokpan/seokpan-hybrid-infra/pull/15)는 MFA/처음 설정/실행자 안내를 보완해 병합됐다. 인자 오타는 이전 세션을 유지하므로 모든 실패가 같은 동작이라고 요약하지 않는다. 이 Source 수정을 전원 실제 세션·Caller/Backend/Provider 일치나 오류 시 Plan/Apply 차단 완료로 확대하지 않는다. A/B의 실제 실행 확인은 I02에 남긴다. Bootstrap 재구축이나 State 이전 반복은 요구하지 않는다.

검토에서는 자료→승인03/04→계정/TLS/Client→Source/Build→base lab→ROSA→Evidence/발표→비용/정리의 영향을 대조했다. 중복 보고의 새 Run 오인, lab 권한 교체 재요구, 미시험 DDL의 PASS 오인, 예제 Engine/Host 고정, 전역 모니터 권한 복사, 전체팀 직렬 대기, 최신 Infra 수정 누락을 보완하고 그 영향을 다시 대조했다. 이번 문서 반영 범위에서 추가 보완은 없다. 실제 Runtime/Acceptance가 완료됐다는 뜻은 아니다.

공식 Test/Acceptance는03, Actual과 원본 참조는05/`evidence/`, 발표 후보·비교·과장 방지는 [Presentation Baseline](../presentation/PRESENTATION_BASELINE.md)을 따른다. 발표 가치가 있는 실제 Run은 원본 링크와 간략한 후보 판정만 [Docs Issue #6](https://github.com/seokpan/seokpan-hybrid-docs/issues/6)에 연결한다. 자료 접수·과거 PoC만으로 새 발표 후보 PASS를 만들거나1차 재측정을 먼저 실행하지 않는다. Source/입력의 수신과 미반영 작업은 [Docs Issue #8](https://github.com/seokpan/seokpan-hybrid-docs/issues/8)과 진행표로 이어간다.

### 8.7 1차 MariaDB 사전 점검과 데이터 이관 범위

김상희가 2026-10-02 12:02~12:12 KST(03:02~03:12Z)에 1차 MariaDB를 읽기 전용으로 점검했다. 대상은 `read_only = 1`인 Replica 노드이고, 세션도 읽기 전용으로 고정해 `SELECT`·`SHOW`만 실행했다. 1차 DB 변경·덤프·이관은 하지 않았다. 상세 결과와 행 수 기준값은 [Infra #17](https://github.com/seokpan/seokpan-hybrid-infra/issues/17)에 있다.

| 항목 | 확인 결과 | 2차에 주는 영향 |
| --- | --- | --- |
| 버전 | MariaDB 11.8.9 | AWS 공식 버전 문서에서 RDS for MariaDB 11.8.9 제공을 확인했다(2026-10-02). 이 문서 8.3절(RDS TLS·목적별 권한의 구현 인계)에서 남겨 둔 Engine 확인 중 1차 원본 쪽은 끝났다. 서울 리전에서 실제로 만들 수 있는지는 Plan 때 확인한다 |
| 대상 DB | `stone_game` 1개, 테이블 8개, 약 0.36MB | 작은 데이터 규모의 사전 점검 보고. 실제 Dump·전송·Import·전체 업무 재개 시간과 비용은 미측정이며 크기만으로 복구 목표 달성을 판정하지 않음 |
| 문자셋 | DB·테이블 모두 utf8mb4 / utf8mb4_unicode_ci, 예외 컬럼 없음 | 덤프에 그대로 담겨 옮겨진다 |
| 시간대 | 1차 서버 KST, 날짜 컬럼 8개 전부 `DATETIME` | 아래 "시간대" 참고 |
| 객체 | View·Routine·Trigger·Event 없음, PK 없는 테이블 없음, 외래 키 7개 | DEFINER 문제가 없다. 외래 키는 복원 후 관계 검증 기준으로 쓴다 |
| 스키마 관리 | Alembic, 현재 리비전 `20260902_0002` | 이 문서 8.2절(비민감 DB 권한 계약과 I03 부분 접수)의 lab 보고에 나온 Migration 리비전과 같다 |
| 권한 | 점검 계정 `db_admin`의 GRANT가 8.2절의 표와 일치. `mysql.user` 조회는 거부됨 | 1차 최소권한 설계대로 동작한 것이며 실패가 아니다 |
| 민감 컬럼 | `member.login_id`, `member.password_hash`. **실사용자 계정 포함** | 아래 "결정" 참고 |

**결정.** 1차 실제 데이터를 논리 덤프로 RDS에 옮긴다(Schema + 데이터). 03 상세설계 문서 3-D.6절에 적힌 논리 덤프 우선 방식과 같다. 팀은 사전 점검의 작은 데이터 규모를 근거로 이관 부담이 작다고 판단해, 비용을 이유로 "실제 데이터는 옮기지 않는다"고 했던 이전 방향을 변경했다. 이관 → 백업 → 온프렘 복원을 같은 데이터로 이어서 검증할 수 있다는 점이 이유다. 이는 팀의 선택 근거이며 실제 Dump·전송 비용이나 프로젝트 전체 비용이 0임을 측정한 결과는 아니다.

실사용자 계정이 있으므로 덤프 파일과 행 내용은 저장소·Issue·PR·Evidence에 넣지 않고, 기록에는 행 수·관계·SHA-256만 남긴다. 덤프는 만들자마자 age로 암호화하고, 프로젝트가 끝나면 RDS·백업 S3·복구 VM의 이관 데이터를 지운다. 실사용자에게 안내나 동의가 필요한지는 팀과 강사님께 확인한다. 확인 결과 반출이 어렵다면 `member.login_id`를 가명으로 바꿔 옮기는 대안으로 전환한다. 대안의 방법과 전환 기준은 Infra #17에 적어 두었다.

**시간대.** 기존 행은 KST로 기록돼 있다. `DATETIME`은 덤프·복원 과정에서 값이 바뀌지 않는다. 문제는 이관 이후 새로 쌓이는 값이다. RDS 기본 시간대(UTC)나 UTC로 동작하는 컨테이너가 새 값을 쓰면, 같은 컬럼에 KST와 UTC가 9시간 차이로 섞인다.

| 원인 | 대응 | 담당 |
| --- | --- | --- |
| 기본값이 `current_timestamp(3)`인 컬럼 4개는 DB 세션 시간대를 따름 | RDS 파라미터 그룹 `time_zone = Asia/Seoul`, 복구 DB도 KST로 고정 | 김상희 작성, 이유빈 foundation 통합 |
| `started_at`·`ended_at`·`confirmed_at`은 앱이 직접 넣는 값 | 앱의 시간 생성 방식과 Pod `TZ` 확인 | 정태훈 (App #1과 함께 확인) |

**아직 하지 않은 것.** 덤프 실행 계정과 위치, Backup·Restore 목적 계정, 복구 VM Host 실측이 남아 있다. 실사용자 데이터는 2026-10-02에 그대로 이관하기로 결정했고(가명화 대안 사용 안 함, 취급 조건 유지), 근거는 Infra #17 결정 코멘트에 있다. 이번 점검은 이관 준비를 위한 조회이며 이관·백업·복원 시험의 결과가 아니다.

### 8.8 foundation Data 코드 초안과 Data 권한 요청

김상희가 2026-10-02 foundation Data 영역 코드를 [Infra #19](https://github.com/seokpan/seokpan-hybrid-infra/issues/19)의 브랜치 `infra/19-foundation-data`에 작성했다. 04 문서 2.2절(작성과 실행과 리뷰 배정)대로 코드 작성은 김상희, foundation 통합과 apply는 이유빈이다. 아직 main에 반영하지 않았고, AWS에 만든 자원도 없다.

**코드 배치.** Network 코드가 아직 없어 Data 코드를 `terraform/modules/data/` 모듈로 먼저 만들고 단독으로 검증했다. Network 코드가 합쳐지면 **첫 plan·apply 전에** foundation Root에 직접 두는 구조로 바꾸고 PR을 한 번만 올린다(이유빈 합의). apply 뒤에 바꾸면 Terraform이 리소스 주소가 바뀐 것을 삭제 후 재생성으로 판단하기 때문이다. 03 문서 3-F.3절(저장소와 디렉터리 대응)은 모듈을 나누는 기준만 두고 Data 배치는 정하지 않았다.

| 대상 | 초안 내용 | 근거 |
| --- | --- | --- |
| Data SG | RDS·Redis SG 분리. 규칙은 모두 별도 Rule 리소스, ROSA Worker → Data SG 규칙은 rosa State가 추가. 온프렘 → RDS는 Data VM `/32` 확정 전 규칙 없음 | 03 3-B.9.6~9.7절 |
| RDS | MariaDB 11.8.9 Multi-AZ, db.t4g.small, gp3 20GiB(자동 확장 끔). 파라미터 그룹 `time_zone = Asia/Seoul`·`sql_mode` 1차 동일·`require_secure_transport = 1`·utf8mb4_unicode_ci | 03 3-D.10.3절, 이 문서 8.7절 |
| Redis | Redis OSS 7.1, cache.t4g.small 2개(Primary+Replica, Multi-AZ), `noeviction`, TLS + AUTH | 03 3-D.9.7절, 3-D.10.4절 |
| Backup S3 | `hourly/` 7일 후 삭제, `protected/` 자동 삭제 없음, 버전 관리·HTTPS 강제 | 03 3-D.9.5~9.6절 |
| Backup User | 업로드·다운로드·목록만, 삭제 권한 없음. Access Key는 Terraform 밖에서 발급 | 03 3-C.13절 |

**비밀값과 State.** RDS 마스터 비밀번호는 RDS가 만들어 Secrets Manager에 보관하는 방식, Redis Token은 State에 저장되지 않는 write-only 인자를 쓴다. Backup User Access Key는 Terraform으로 만들지 않는다. 세 가지 모두 비밀값이 Terraform State에 남지 않게 하려는 선택이며, RDS 방식은 이유빈 확인을 기다린다.

**확인한 것.** 저장소 밖 검증용 Root(AWS provider 6.67.0 고정)에서 모듈 8개 파일의 `terraform validate`가 통과했고, 입력 검사 2개(서브넷 3개, 온프렘 주소 `/32`)가 잘못된 값을 막는 것을 확인했다. 서울 리전 조회로 RDS 11.8.9 + db.t4g.small + Multi-AZ + gp3, Redis 7.1 조합이 생성 가능함을 확인했다.

**권한 요청.** foundation 실행 Role에 붙일 Data 권한을 [#19 코멘트](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-5947207348)로 이유빈에게 전달했다. 리소스 이름을 `seokpan-` 접두사로 제한했고, 백업 객체 읽기·쓰기, 마스터 비밀번호 열람, Access Key 발급, 복구·장애 시험 권한은 일부러 뺐다.

**아직 하지 않은 것.** 구조 전환과 PR, bootstrap 권한 반영, 실제 plan·apply, Redis 7.1과 App Driver 호환 확인(정태훈)이 남아 있다. validate와 조회는 코드와 생성 가능 조합의 확인이며, 권한·생성·접속 시험의 결과가 아니다.

<a id="recovery-objective-review-20261002"></a>
## 9 복구 예행과 목표 재검토 — 2026-10-02

### 9.1 피드백·후속 범위와 유지하는 기준

정태훈이 전달한 강사 피드백은 `architecture/exports/10-backup-offline-recovery.png`의 RTO 30분·RPO 90분이 사용자 관점에서 넓으며, RTO 5~10분 정도를 검토할 수 있다는 의견이다. RPO 수치나 일반 인터넷 사용자 전체의 복구를 필수로 확대한다는 결정은 전달되지 않았다. 분류는 **외부 피드백 / 목표 재검토 입력**이며 실제 성능 Evidence가 아니다.

직전 AI 제안의 RTO 10분·RPO 15분·5분 백업은 검증 전 후보였고, 특정 수치를 먼저 정해 설계를 맞추는 우선 권고는 철회했다. 사용자는 실현 가능성·편의성·구현/학습/운영 부담·기간·비용·설계 정합성·멘토 설명 근거를 함께 고려하고 후속 작업을 진행하도록 지시했다. 이번 절은 그에 따른 기존 작업의 구체화이며 새 수치·구조·역할·상시 서비스 운영을 확정하지 않는다.

| 구분 | 현재 기준 / 처리 |
| --- | --- |
| 공식 목표 | 03 §3-G.7의 Offline RTO 30분 이내·영속 DB RPO 90분 이내, 3-D.9.6의 운영 중 1시간 백업·일반 사본 7일 및 보호 사본 유지 |
| 우선 후속 | Cloud Primary + On-Prem Restore-based Recovery에서 W04 예행·T17/T18 준비를 이어가며 실제 병목과 적은 변경의 효과 확인 |
| 미확정 | 새 목표·백업 주기, 사용자 접속/처리 규모의 확대, 지속 복제·Warm Standby |
| 지킬 경계 | 1차 보호, 격리 복원·새 Redis, Terraform/GitOps/Secret Ownership, 사전 로컬 자료, 전체 복구 시간선과 데이터/업무 검증 |
| 일정·비용 | 10/16 Technical Freeze·10/22 Demo Freeze·10/23 Presentation Ready·10/26 종료, $450 계획선/$500 한도 유지. 실제 가용시간·추가 비용은 I07에서 확인 |
| 현재 실측 | Infra #17의 원본 점검·행 수 보고를 활용하되 이번 조회에서 전체 Backup/Restore·RTO/RPO Run의 연결 근거는 미확인. AI는 Runtime을 실행하지 않음 |

목표는 업무 영향과 기술·자원 제약을 함께 고려한다. 근거 없이 느슨하거나 엄격한 목표를 정하지 않는다는 공식 참고는 [AWS REL13-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.html)이다(2026-10-02 확인). 특정 분 단위 값은 AWS가 이 프로젝트에 지정한 기준이 아니다.

### 9.2 예행 전 입력과 계속할 독립 준비

| 담당 / 기존 연결 | 예행에 필요한 입력·산출물 | 막히는 실행 / 계속할 준비 |
| --- | --- | --- |
| 김상희 — [Infra #17](https://github.com/seokpan/seokpan-hybrid-infra/issues/17), [#19](https://github.com/seokpan/seokpan-hybrid-infra/issues/19), I03/I05 | 목적별 Dump/Restore 계정·도구/CA·Schema, 보호 Backup ID·Data 기준 시각/확인 수준, S3/로컬 완성본·무결성, 격리 DB·복원 공간 | 실제 자산·계정이 없으면 해당 Dump/Import 대기. Backup/Restore 코드·도구 계약·크기 산정은 병행. #19는 Data 인프라 코드이며 Backup/Restore Run 자체가 아님 |
| 정태훈 — [App #1](https://github.com/seokpan/seokpan-hybrid-app/issues/1), [GitOps #5](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5)·[#6](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6), I01/I05 | 검증 Image·Recovery Manifest/Secret·CA, DB/새 Redis 연결, 상태 정리·로그인·완료 기록 조회·새 게임 계약, 지정 클라이언트의 접속 경로 | 미인계 Image/base로 업무 복구 완료 주장 금지. Source/Render·App 접속/복구 계약 준비는 병행 |
| 이유빈 — [Infra #23](https://github.com/seokpan/seokpan-hybrid-infra/issues/23), [#16](https://github.com/seokpan/seokpan-hybrid-infra/issues/16), I03 자산 협업 | 실제 복구 Host/플랫폼·Storage 여유·로컬 DNS/Harbor·도구 가용성, Data VM과 복구 DB의 배치·장애 영역 | #23 foundation·#16 VPN 진행을 유지. 새 전용 VM의 실제 CPU/RAM/디스크 확보는 별도 확인. 전용 VPN VM 준비가 복구 DB/독립 Storage 준비 완료를 뜻하지 않음 |
| 최유준 — 기존 시험/CI/lab 작업, I04/I07 | 단계별 시간선·측정 절차·Release/Backup 연결, 실제 가용시간·추가 작업/재시험/비용 집계, 조건과 실패 결과의 Index | 기존 Run 양식을 사용. 모든 담당 입력을 기다리지 않고 계측/조건·CI/Harbor 인계를 준비. 공유 시험은 각 실행자·리뷰·대상/Context·시간/비용을 확인해 조율 |

새 Issue나 별도 계획서를 일괄 추가하지 않는다. 기존 담당 작업에서 코드·입력을 준비하고, 독립적인 완료 조건이 필요한 실제 Backup/Restore 작업이 생길 때만 담당자가 Issue 분리 여부를 정한다. 담당과 실제 수행자·Reviewer는 실행 기록에서 구분한다.

### 9.3 W04 예행의 순서와 측정 범위

1. **조건 고정:** 실제 Source/Release·Image·Schema·도구·Backup과 격리 대상을 식별한다. 로컬 자산의 전원/준비 수준, 담당자 대응 조건, 클라이언트 위치·접속 주소·HTTPS/WSS, 복구할 기능·처리 규모를 Run에 기록한다. 장애 후 VM 설치가 필요한 조건이면 그 시간도 포함한다. 모든 인터넷 사용자나 정상 Cloud 부하 전체를 복구했다고 자동 해석하지 않는다.
2. **Backup 경로 확인:** DB Data 기준 시각/확인 수준, Dump 시작/종료, 압축·암호화, S3 보관, 로컬 다운로드·완성본 확인 시각을 구분한다. 완성본의 Hash/해독 확인과 실제 DB/App 복원 검증은 별도 상태다. 백업마다 전체 복원 시험을 새 상시 작업으로 추가하지 않는다.
3. **Offline 복구 예행:** 장애 시작 t0 → 탐지 → 복구 판단/조치 시작 → 사용 사본 선택·검증/해독 → 격리 DB Import/계정/TLS·필수 Data 확인 → 새 Redis/App 적용·상태 정리 → 접속 안내/재로그인·대표 업무/영속 Data 확인 완료 t1을 기록한다. 먼저 정한 2/3/3/2분 배분에 맞추지 않고 실제 소요·대기를 기록한다.
4. **경계·실패 영향 확인:** 기존 T17/T18의 지연·부분 실패·이전 사본 선택 Case에 연결해 백업 간격 끝부분의 최신성, 사본 실패 후 실제 사용 Data 시점의 변화를 확인한다. 격리 사본/시험 경로에서 수행하며 1차·공유 VPN·Cloud 자원을 임의 중지하지 않는다. 예정 장애 직전에 성공 백업을 한 결과만으로 운영 RPO를 판정하지 않는다.
5. **병목 개선·필요 재예행:** 오래 걸린 단계와 수작업 원인을 확인해 기존 스크립트·Bundle·사전 확인/인계부터 보완한다. 변경·실패·조건 차이에 필요한 재시험만 수행하고, 모든 백업 주기/DR 구조의 비교 구현을 요구하지 않는다. 한 번의 가장 빠른 결과로 새 목표를 확정하지 않는다.

AWS·S3·GitHub·Cloud IDP·ECR·AWS KMS 신규 조회가 필요한 단계는 Offline 성공으로 처리하지 않는다. 로컬 DNS·Harbor·복구 플랫폼은 승인된 가용 조건을 유지한다. OCP/대역 DB·로컬 예행은 가능한 준비를 먼저 검증하되 실제 RDS에서 만든 Backup/승인 Release를 사용한 최종 T18과 조건 차이를 남긴다. 최종 Offline 검증을 위해 ROSA를 불필요하게 계속 켜두는 조건은 추가하지 않는다.

VPN 단절이나 한 운영자의 AWS 접속 실패만으로 Cloud 전체 장애를 판정하지 않는다. 이번 범위는 격리 복원·지정 클라이언트의 업무 검증이다. 실제 사용자 트래픽을 로컬 쓰기 서비스로 전환하는 범위를 추가하면 Cloud/로컬 동시 쓰기 방지·사용자 진입·복귀 절차와 작업량을 먼저 검토하고 변경 결정으로 연결한다.

### 9.4 계산과 결과 해석

| 항목 | 계산 / 기록 기준 |
| --- | --- |
| RTO | `t1 - t0`. Import·Pod Ready 시간만 대입하지 않음. 탐지/판단·기동·접속 안내·업무/Data 확인 포함 |
| 영속 DB RPO | `t0 - 실제 사용 Backup의 Data 기준 시각`. 마지막 로컬 파일의 수정 시각이나 Dump 종료 시각을 사용하지 않음 |
| 백업 지연 | Data 기준 시각에서 사용 가능한 로컬 완성본 확보까지. Snapshot 시각 불확실성·스케줄 지연·중복 실행 생략·재전송·이전 사본 선택을 구분 |
| 정상 경로의 후보 검토 | 성공이 매번 이어지고 지연이 제한된다는 조건에서 성공 사본 Data 기준 시각 사이의 최대 간격＋그 기준 시각부터 로컬 완성본 확보까지의 최대 지연을 검토. 스케줄 지연을 중복 합산하지 않으며 실패·장기 중단·복원 실패로 이전 사본을 사용할 때는 이 계산으로 RPO 상한을 보장하지 않음 |
| 상태 손실 | 백업 이후 회원/완료 게임/Rating 등 영속 쓰기의 유실 범위, 새 Redis의 세션/진행 게임 중단을 별도로 기록. 임의 정상 완료/승패·Rating 생성 금지 |
| 운영 조건 | 준비된 학원 환경·담당자 대응·지정 클라이언트 결과를 24시간 복구 보장이나 전체 Public 서비스의 전환 성공으로 확대하지 않음 |

정확한 Data 시각을 알 수 없으면 Dump 시작 시각 등 보수적 경계와 비민감 시험 Marker/쓰기 시각·복원 후 존재 여부를 대조한다. 시점 범위·시계 불확실성을 기록하고 목표 충족을 판정할 수 없으면 수치 PASS를 주지 않는다. 지연·실패로 목표를 넘기면 실제 값과 미달을 그대로 남긴다.

### 9.5 부담 비교와 변경 결정 조건

**먼저 볼 대안은 현 구조의 사전 준비·필수 스크립트·인계 개선이다.** RTO 개선과 백업 주기 단축은 따로 평가한다. 백업 주기를 줄이는 후보는 기존 Timer·중복 실행 방지·완성본/최신성 관측에서 감당 가능한 간격을 비교하고, 이미 이름에 `hourly/`를 쓰는 S3 Prefix의 의미·보관/정리·코드/대장 영향도 함께 확인한다. Prefix 이름 때문에 실제 실행 주기를 고정하거나 이름만 바꿔 주기 변경 완료로 기록하지 않는다.

| 판단 항목 | 필요한 근거 / 선택 제한 |
| --- | --- |
| 사용자 영향 | 허용할 업무 중단, 백업 이후 신규 회원·완료 결과·Rating 손실, 재로그인/진행 게임 중단, 접속/처리 규모. 강사 피드백과 이 범위를 대조하고 AI가 허용 손실을 임의 확정하지 않음 |
| 가능한 개선 | 단계별 실측·수작업·필수 의존. 적은 변경으로 줄일 수 있는 구간과 남는 불확실성을 설명 |
| 팀 부담·편의성 | 네 사람의 실제 가용시간 안에서 구현·학습·사용/유지·실패 처리·인계·재시험·문서/그림 반영·발표 준비까지 산정. 반복 사용과 예비 담당자의 실행 가능성을 확인 |
| 추가 비용 | 실제 암호문 크기·운영 시간·주기별 건수·7일/보호/버전 사본·작업 임시/복원 공간·S3 요청/전송·DB 부하·Cloud 추가 가동/재시험·삭제 지연을 I07 전체 산식에 합산. DB 크기만으로 추가 비용 0 판정 금지 |
| 범위 확대 | 지속 복제·Warm Standby·새 Public 전환은 현재 추가하지 않음. 필수 요구와 현 구조의 실측 부족이 확인되면 대안·효과·부담·시험/복귀까지 비교한 뒤 결정 |
| 일정 보호 | 목표 재검토는 Window A/W04 결과와 함께 10/16 Freeze 전 판단에 연결. 입력이 늦으면 미확인·담당·막는 작업을 드러내며 전체 독립 구현을 중지하거나 Freeze를 임의 연장하지 않음 |

예행 결과만 보고 통과하기 쉬운 목표를 만들지 않는다. 업무 영향과 실현 가능 범위를 함께 비교하고, **새 Acceptance 적용 전** 사용자 변경 결정과 영향 기록을 남긴다. 최종시험 실패 뒤 같은 Run의 목표를 낮춰 PASS로 바꾸지 않는다. 기준 변경이 필요하면 이전 목표/Run을 보존하고 새 개정·후속 시험을 분리한다.

기존 30분/90분 유지가 필요한 경우에도 이유·검증 조건·한계를 설명한다. 강화 목표를 감당할 수 없으면 범위/대안을 재논의하며 미달을 완료로 처리하지 않는다. 검토는 필요한 입력과 대표 병목에 한정하고, 추가 개선의 효과가 작거나 핵심 Migration/검증/발표 시간을 침해하면 확장을 보류할 수 있다.

### 9.6 기록 위치와 변경 영향

| 기록 | 정본 / 연결 |
| --- | --- |
| 이번 피드백·제안 수정·예행 준비와 판단 조건 | 이 절. 공식 새 목표를 정한 결정 기록은 아직 아님 |
| 코드·자산·입력·Blocker·인계 수신 | 해당 Infra/App/GitOps 작업 Issue·PR. 현재 원문 링크와 필요한 입력만 WORK_TRACKER·Docs Issue #8에 연결 |
| 실제 시험 | `evidence/<test-id>/<run-id>/`의 기존 다섯 양식. Source/Release·조건·실제 수행자와 단계 시각을 기록; 새 시험 ID나 가짜 Actual을 만들지 않음 |
| 시간선 | 기존 `timeline.csv` 열을 유지하고 `event_id`로 장애/탐지/판단/사본/Import/Redis/App/접속/업무 완료를 식별. `event`와 `evidence_ref`에 단계 의미·근거 연결; Backup 생성·사전 확보는 장애 전 시각 |
| 수치와 해석 | `metrics.csv`의 `metric_id`로 RTO/RPO·Backup 로컬 확보 지연·단계 소요를 구분하고 unit/aggregation/condition_ref 기록. 미측정은 Actual 빈 값, `summary.md`에 계산·시점 범위·실패·제한. 기존 `release.json`에 실제 Backup/Release 조합 연결 |
| 발표 후보 | 실제 Run 확보 후 Docs Issue #6에 원본 링크·후보 판단·주장 범위만 연결. 이번 문서 검토나 목표 후보를 달성 Evidence로 등록하지 않음 |
| 변경 채택 후 | 03의 Data/시험/WBS·Cost/결정, 04의 Runbook/입력·판정, 05/Tracker·관련 코드/Issue, 그림 생성 원본과 영향 SVG/PNG를 함께 대조. 상위01/02·지침·발표 참조는 실제 영향이 있는 내용만 갱신 |

역사적 승인/Run은 덮어쓰지 않는다. 숫자만 바꾸는 전역 치환 대신 현재 기준과 과거 이력을 구분한다. 목표·범위 변경 전에는 `build_diagrams.py`와 설계 SVG/PNG를 새 값으로 재생성하지 않는다. 원문 SQL/Backup·행 내용·Password/Key·State/Plan은 공개 기록에 넣지 않는다.

### 9.7 문서 검토와 남은 실행

피드백 → 승인 목표/복원 범위 → Backup·자산·App/접속·Owner → 계측/판정 → 작업량/비용·Freeze → 변경 기록·그림/발표의 영향을 대조했다. 첫 검토에서 특정 수치 우선 권고와 DB 크기 기반의 복원/비용 단정을 보완했다. 후속 대조에서 예행/최종시험·백업 완성본/실제 복원·운영 조건·양쪽 쓰기·Prefix/보관·기준 변경 시점을 구분하고, 정상 경로의 최신성 계산에서 스케줄 지연 중복 합산을 방지했다. 최종 문서/링크/차이 대조 범위에서 추가 보완을 발견하지 못해 이번 준비 기록의 검토를 종료했다. 실제 Runtime PASS와 구분한다.

- [x] 피드백 분류·기존 승인 기준/구조 유지·특정 수치 우선 권고 수정
- [x] 기존 W04/T17/T18의 담당 입력·예행·계측·기록 위치·변경 판단 준비
- [ ] I03/I05/I07·App/Image/Bundle/접속의 실제 입력과 실행 시간 확보
- [ ] 실제 예행·필요 재시험·실행 Run/단계별 병목·백업 최신성·팀 부담 확인
- [ ] 업무 영향과 실현 가능성 대조, 변경이 필요하면 새 Acceptance 적용 전 사용자 결정
- [ ] 채택 변경의 코드·문서·SVG/PNG·발표 참조 반영과 최종시험


<a id="recovery-time-helper-20261002"></a>
### 9.8 후속 구현 — Run 시각 계산 보조

PR #18 병합 후 [현재 Source 관측](WORK_TRACKER.md#follow-up-observation-20261002)의 변경과 원 lab 인계를 읽고, 실제 복구 입력을 기다리지 않아도 진행할 수 있는 계측 준비를 구현했다. 도구는 [tools/recovery_metrics.py](../tools/recovery_metrics.py), 사용법·출력 의미는 [Evidence 안내](../evidence/README.md#recovery-time-calculation)에 둔다. 기존 Run의 release.json을 읽기만 하며 양식·원본·목표·판정은 바꾸지 않는다.

변경 원인은 수동 시간 계산에서 일부 단계만 RTO로 쓰거나 불확실한 Data 시각을 정확한 RPO로 옮길 위험이다. 전체 RTO와 Dump/Import를 나눠 계산하고, Data 시각 확인 전에는 시간 차이만 표시하며 RPO는 null로 둔다. Reviewer가 실제 시각·확인 수준·Backup/Marker 근거를 확인한 경우에만 명시 옵션을 쓴다. 도구가 근거를 자동 검증하거나 PASS를 내리는 것은 아니다. 누락·시간대 없는 시각·단계 역전·중복 JSON 키·기록 수치 불일치를 구분한다.

추가 설치·Cloud 자원·서비스 호출 없이 Python 3.9 이상 표준 라이브러리로 실행한다. C의 Backup/Restore·B의 App/Recovery·D의 실제 계측 책임은 유지하고 새 상시 파이프라인은 추가하지 않는다. timeline.csv·Raw·무결성·시계 오차·업무/손실 검증과 실제 작업량/비용은 각 Run·I07에서 별도 확인한다.

로컬 코드 검사: `python3 -m unittest discover -s tools -p 'test_recovery_metrics.py' -v` — 합성 입력 11개 테스트 통과. 빈 양식은 UNMEASURED/null이며 CLI의 원본 미변경·신규 파일 미생성도 확인했다. 재검토에서 중간 시각 누락 시 단계 역전 탐지와 비정상 수치·중복 키 처리를 보완하고 다시 검사했다. 실제 Run이나 T17/T18 PASS·새 목표 달성의 Evidence가 아니며 Run Index에 추가하지 않는다.

- [x] 기존 양식으로 선택 사용 가능한 계산 코드·사용 안내·합성 입력 검사
- [x] PR #19 사용자 승인·병합·브랜치 삭제 확인 — 2026-10-02
- [ ] 담당자의 실제 Run 적용·근거 확인
- [ ] §9.7의 실제 예행·병목/백업 최신성·부담 검토와 필요 변경 결정



<a id="recovery-app-source-20261002"></a>
### 9.9 App 연결 구현·GitOps 선언과 실제 예행의 인계

아래 §9.9는 최초 인계 시점 기록이다. 최신 수정 Source와 재검증은 [§9.10](#recursive-source-review-20261002)에 이어 기록한다.

PR #19 병합 이후 목적을 다시 대조했다. 결과물은 실제 예행의 시간선·영속 데이터 손실/Backup 최신성·접속 범위·팀 부담과 그에 따른 변경 판단이다. 계측 도구 준비만 늘리지 않고 T17/T18을 막는 App/Image/Manifest 입력을 구현한다. 작업 Owner는 정태훈, Source 작성·로컬 검사 지원은 Codex이며 실제 서버·Image·Restore 수행과 구분한다.

| 산출물 | 현재 Source / 완료 범위 | 남은 직접 의존 |
| --- | --- | --- |
| App #1 | [원본 인계 기록](https://github.com/seokpan/seokpan-hybrid-app/issues/1#issuecomment-5950971722). 고정 Seed `7fce757f963ba59cc81c03028c043be5b45719b2`와 기존 hybrid-app main `cef46c4e7b0cbd0cf6ebab487ee92c32d800ccdc`를 두 부모로 보존한 로컬 Commit `c7a452d514742f77abd2c49c5836566df7386550`. 76개 전체 이력 Bundle·새 clone/두 부모/Tree/16개 변경 파일 동일성 확인 | 인증된 개인 작업환경의 Branch Push·별도 PR/리뷰/사람 Merge, 개인 PC/Controller 미커밋 변경 대조. 원격 main에는 아직 코드 없음 |
| 연결 계약 | legacy 기본 동작 유지. cloud/lab/recovery의 정확한 DB/Redis 대상, Runtime·Migration·Alembic 동일 검증, rediss·별도 AUTH·명시적 CA/Hostname, 안전한 구성 오류/repr·Client/Pool 정리. Dependency/Lock·Schema·Lifecycle·FE Source는 변경 없음 | C/D의 실제 대상/CA/AUTH·Schema/계정과 새로운 TLS Redis 시험. 현재 원 lab 평문 Redis는 새 비legacy 계약과 맞지 않음 |
| GitOps #5/#6 | [Draft PR #9](https://github.com/seokpan/seokpan-hybrid-gitops/pull/9), HEAD `113d24597fbe2f699d48d4e20c731ccb28b2cddb`. 실제 Kustomize base/lab/Recovery Source 후보. [B의 원 lab 참고 범위 수신·인계](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5#issuecomment-5950971514). 원 lab `259e73b0fac1af40f7bb7b43bd1982410d1df150`은 참고 Branch 보존 | D 새 Image/Registry Digest·Pull·실제 Sync/Health·업무, C/A 격리 Recovery 플랫폼/Namespace·직접 DB·새 Redis·접속, 자원·임의 UID 파일 권한 |
| 실행 보류 | 미해결 INPUT_REQUIRED/.invalid와 replicas0 후보. Kustomize 출력의 입력 검사는 보류 값이 있으면 Release 파일 생성 거부, 통과해도 기존 파일/Symlink 덮어쓰기 거부 | 완전한 배포 준비 검사나 Runtime PASS 아님. 실제 입력 개정·검증 조합을 검토한 별도 변경 전 Apply/Sync 금지 |

App Source 선택 시 동일 Seed의 GitHub Jenkins Image Pipeline #39 상태가 success였고 별도 Check Run은 0건이었다. 원본 성공 Image를 수정 Source의 새 Image로 간주하지 않는다. 개인 미반영 작업과 실제 Build/Scan/Digest 원문·서버 검증은 별도 입력이다. 처음 사용한 B ZIP의 URL 인증·`.yaml.in` 프로토타입은 현재 완료본으로 승격하지 않는다.

App 검사는 정확한 Python3.13.15/uv0.12.5/frozen lock에서 전체 pytest1724개·신규 hybrid54개를 통과했다. 독립 검토에서 DB CA 경로 repr 노출을 보완한 뒤 관련132개를 다시 확인했고 전체 ruff check/format·mypy119 Source·diff 검사를 통과했다. 실제 redis-py8.1.0의 loopback TLS/합성 RESP peer로 AUTH/PING 정상·잘못된 AUTH/CA/Hostname 거부를 확인했으며 MemoryBIO·종료/취소 검사도 연결했다. 이는 로컬 Driver/회귀 검사이고 실제 RDS/ElastiCache·lab·Recovery Runtime/업무 PASS가 아니다.

GitOps는 공식 고정 Kustomize v5.7.1 바이너리 공개 Checksum을 대조하고 base/lab/Recovery Build와 선언·출력 보존 검사10개를 통과했다. CA/AUTH/환경변수는 App Source와 대조했다. 공통 base에 고정 UID/GID·lab Host/CA/hostAliases·Registry 자격·기존 Redis를 넣지 않는다. Secret 값/Object는 별도 공급 Owner, Migration은 별도 승인 단일 실행이다. 새 Recovery Redis의 실제 배치·공급은 C 입력/작업으로 남는다. Cloud Overlay·Policy/UWM·관리 인증·실제 자원 조정은 이번 부분 구현에 포함되지 않는다. timeout/Probe/종료 유예는 실제 환경 실측 전 후보다.

Git 읽기는 가능하지만 Git Push 인증이 없어 App 전체 이력을 현재 연결로 전송하지 못했다. 파일 Snapshot만 API로 올려 승인된 이력 보존 방식을 바꾸지 않았다. `seokpan-hybrid-app-connection-20261002.zip` 안의 검토용 Bundle·Source/Hash·정확한 Branch 전송 절차를 준비했다. Bundle SHA256은 `49d46ca94856647d3d8f9df816768a11a20fa44e4162528eb7ea945da3fa4539`이다. 현재 코드의 원격 공개·팀 수신 완료로 기록하지 않는다. 기존 1차 Image Pipeline 원문은 reference에 보존하고 이관본 Image 진입점은 CI #2 전환 전 즉시 중단하도록 했으며 기존 1차 Job·공유 Template은 변경하지 않았다.

[App #2의 B 리뷰](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-5950294428)와 [D의 반영 수락](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-5950470901)을 읽었으므로 A~F를 다시 승인 대기로 돌리지 않는다. F 수명 문구는 사용자 채택04의 무기한 허용 시 우선/제한 시 허용 최대 수명·Org 정책 유지 기준으로 정합한다. Registry별 Digest/Platform/Release Mapping·Lifecycle Preview·승인 Harbor 보존·Worker Pull foundation Owner·실제 AUTH 공급 Gate는 기존 승인 경계의 구현 확인이다.

연쇄 재대조에서 실제 Code→App/Secret/CA→GitOps→Image/lab→Recovery 자산/예행→기록/목표 판단을 추적했다. CA repr 불일치와 성공 출력의 기존 파일 덮어쓰기 문제를 보완하고 관련 검사·Source/전송본 동일성을 확인했다. 현재 검토 범위에서 남은 중대한 Code/계약 충돌을 발견하지 않았다. 준비·Source 검토를 Runtime PASS로 확대하지 않고 빈 Run/가짜 Actual을 만들지 않았다. RTO30분/RPO90분/1시간 Backup·복원 구조·예산/Freeze·설계 그림은 유지한다.

- [x] PR #19 병합 후 Source/인계·목적·직접 의존 재확인
- [x] App 연결 코드·로컬 실제 Driver/전체 회귀 및 최종 관련 재검증, 이력 보존 이관 묶음
- [x] Kustomize 실제 Source 후보·입력/출력 보존 검사·Draft PR #9와 원본 Issue 기록
- [ ] 인증된 App Branch 전송·PR, GitOps Source 리뷰와 C/D 실제 입력 수신
- [ ] 새 Build/Scan/Digest·lab #6/#5, 격리 DB/Backup/새 Redis·Bundle/접속과 담당 실행 시간
- [ ] 기존 실제 Run의 복구 예행·Backup Data 시각/로컬 최신성·손실/팀 부담 측정
- [ ] 업무 영향/실현 가능성 대조와 필요한 변경 결정·실제 최종 Acceptance/발표 연결


<a id="recursive-source-review-20261002"></a>

### 9.10 직전 구현·인계 전체의 재귀 검토와 수정

사용자 요청에 따라 직전 답변의 완료 표현부터 Source·실제 Driver·GitOps·이관 명령·계측·원본 Issue·PR·기록까지 연쇄 검토했다. §9.9의 추가 보완 없음 판단 뒤 이번 독립 재현에서 아래 결함/문구 불일치가 확인되어 수정했다. 검토는 코드·선언·전송본·기록 범위이며 실제 배포·복구 성공을 뜻하지 않는다.

| 발견 / 후속 영향 | 수정과 최종 확인 |
| --- | --- |
| DB 빈 Fragment가 URL 검사를 통과하지만 Driver에는 `charset=utf8mb4#`로 전달됨 | DB/hybrid Redis의 raw Fragment를 거부. 정상 인코딩 비밀번호 `%23` 유지. 전체 pytest 1,728개·hybrid 58개·관련 155개, 전체 ruff/format·mypy 119 Source 통과 |
| SAN 필수 문구가 현재 Python 기본 Hostname 검증(CN fallback 포함)의 강제 범위보다 강함 | 승인 Host 유효성 검증과 lab/Recovery 인증서의 SAN·CA 수명 공급/실제 검증을 구분. TLS/Hostname 검증 정책을 새로 바꾸지 않음 |
| 초기 2차 main 대비 `diff --check`가 원본 Seed의 공백 9건으로 정상 이관을 중단함 | 고정 Seed 대비 새 변경 검사로 수정. Seed 대비 17개 수정과 초기 hybrid main 대비 전체 이관 386개 파일을 각각 기록. 최종 ZIP 명령은 인증 Push 직전까지 새 Clone에서 확인 |
| App 이관 Tree에서 초기 hybrid main의 `.gitignore` 보호 규칙이 없어짐 | 초기 main의 Terraform State/tfvars/override/CLI 설정 제외 규칙을 기존 App 규칙과 보존. 대표 보호 경로의 `git check-ignore` 확인 |
| `runtime.env` 변경 후 ConfigMap만 바뀌고 기존 Backend PodTemplate은 같음 | base/Overlay를 내용 Hash Generator로 연결해 실제 Kustomize의 이름·envFrom 참조가 함께 변경됨. 세 환경 Build·11개 검사, lab 변경의 환경 격리와 공통 값 전파 확인 |
| 외부 Secret/CA 값 변경만으로 재기동/연결 갱신이 완료된 것으로 오인할 수 있음 | 값/Object 공급 Owner가 새 개정·검증 조합을 인계하고 승인 Backend 재기동·재접속/업무·회수 검증을 수행하도록 명시. 자동 Prune/실제 실행은 추가하지 않음 |
| UTC 경계 입력의 정규화가 traceback/exit 1 발생 | 안전한 입력 오류/exit 2, 표준 출력/원본 보존을 실제 CLI로 검증 |
| 선택 Dump 완성 전 Import/업무 완료를 허용하고 중간 시각 누락이 역순을 숨김 | 기존 순서의 존재하는 시각 쌍 18개를 검사. 정상 사전 Backup과 미측정값은 유지. 최종 도구 16 unittest와 독립 역순 18개·정상/동일/누락 72개 입력 검사 통과 |

App 최종 Commit은 `8828ed22295c27c6f3b419e762b865d17eb50b8c`, Tree `751e18a7154f7fbedfad4b50a5aae736e60991bd`다. 초기 두 부모 이관 Commit `c7a452d514742f77abd2c49c5836566df7386550`을 부모로 이어 원본 Seed와 초기 2차 main을 포함한 77개 이력을 보존했다. 수정 묶음 `seokpan-hybrid-app-connection-reviewed-20261002.zip`의 Bundle SHA256은 `a25ab40d6e784d8861dcc5fba6866b03443befdafa427a33f018de932914530c`이다. 이전 ZIP은 최초 기록으로 보존하고 새 묶음을 사용한다. App 원격 Branch/PR/새 Build는 아직 없다.

[GitOps Draft PR #9](https://github.com/seokpan/seokpan-hybrid-gitops/pull/9)의 최신 HEAD는 `f1e959d2f3ec5207cc42f0523cbd391930b247d7`이다. 고정 Kustomize v5.7.1 실제 Source 17개 파일을 대조하며 일반 ConfigMap 원문은 Generator로 교체해 삭제했다. replicas0·미해결 입력·Release 파일 생성 거부를 유지한다. Hash/PodTemplate 변화는 Source 검사 결과이며 실제 Rolling Update나 업무 성공은 아니다.

Merged PR #19의 도구 보완은 이 Docs PR #20의 후속 Commit으로 제공한다. 기존 설계·Run 양식·Evidence Index·공식 RTO30분/RPO90분/1시간 Backup·예산/Freeze는 유지한다. 도구는 여전히 읽기 전용 시각 계산이며 Acceptance/Backup 무결성·실제 Data 손실을 판정하지 않는다.

CI #2는 B 최신 리뷰·D 수락의 A~F 구현 방향을 유지한다. 다만 현재 D 작성 본문에는 옛 N30/비용 단정, Scan용 `GetDownloadUrlForLayer` 확정 표현, 선택형 `BatchDeleteImage`, F 유한 만료 문구가 남아 있다. 원래 [B 후속 정합 기록](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-5951015819)에 최신 Infra #18·승인04와의 차이를 연결하며, D 구현 명세/실제 E2E 후속으로 남긴다. 새 CI 진입점과 `promote_gitops.py`의 hybrid 대상/Job·Folder·권한은 구현 전환 범위이고, 상속된 1차 Helper를 직접 실행하지 않는다. Issue 전체 본문 정합/CI 구현을 완료로 표시하지 않는다.

최초 독립 검토 → 재현·수정 → 작성자가 아닌 검토자의 교차 검토에서 계측 중간값 누락 경로를 추가 보완 → 최종 Code/계약·묶음 명령·원격 Tree/기록 대조 순서로 진행했다. 마지막 대조에서 현재 확인 가능한 Source/인계 범위의 추가 필수 보완을 발견하지 않아 재귀를 종료한다. 새 Runtime 입력·리뷰·실제 실패가 생기면 해당 범위를 다시 검토한다.

- [x] 직전 답변의 완료 범위·최신 원격 Source/리뷰·후속 영향 대조
- [x] 재현한 결함/문구 보완·관련/전체 검사·독립 교차 검증
- [x] 수정 묶음·열린 PR·원본 Issue/진행 기록 연결
- [ ] App Branch Push/PR·Source 리뷰/사람 Merge, Docs/GitOps PR 검토·병합
- [ ] D CI 본문/구현·새 Image/Registry별 Digest·lab 실제 검증
- [ ] Foundation/Data/ROSA 실제 입력·Plan/Cost Gate·각 Owner 통합 실행
- [ ] 격리 DB·Backup/새 Redis·접속·Offline Bundle 수신/실제 Run
- [ ] 실제 시간/손실/최신성/팀 부담 판단·필요 변경·최종 Acceptance·발표/정리

<a id="tjung03-registration-rosa-input-20261002"></a>

### 9.11 정태훈 전체 작업 등록과 ROSA 입력 준비

사용자의 연결 구조 확정·등록·후속 독립 준비 지시에 따라 전체 관리 Issue 1개와 별도 완료 조건을 가진 실행 Issue 3개를 등록했다. 등록 결과 기록 시각은 `2026-10-02T11:53:47.771Z` / `2026-10-02T20:53:47.771+09:00`이다. **기존 개인계획 TH-01~19·81개 세부 식별자를 유지**하고 실제 결과는 원래 작업 Issue·PR·Run에 남긴다. 개인 계획·승인03/04·지침을 새 설계로 대체하거나 공식 T01~T23·목표/Freeze/예산을 바꾸는 작업이 아니다.

| 실제 기록 위치 | 담당 범위와 기존 연결 |
| --- | --- |
| [Docs #21 상위](https://github.com/seokpan/seokpan-hybrid-docs/issues/21) | 전체 TH·완료 기준·현재/다음/Blocker·학습/발표·최종 종료의 원본 링크. 팀원 상세 결과를 대필하거나 모든 TH 완료로 표시하지 않음 |
| [App #4 실행](https://github.com/seokpan/seokpan-hybrid-app/issues/4) | TH-02·06·07·14의 이력 보존 이관·사용자 경로/생명주기·검사/Release 인계·다중 Pod 안전. 기존 [App #1](https://github.com/seokpan/seokpan-hybrid-app/issues/1) Client/시간대·[App #2](https://github.com/seokpan/seokpan-hybrid-app/issues/2) CI·D [GitOps #6](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6) 검증 유지 |
| [GitOps #10 실행](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10) | TH-08·09·15의 base/lab·Cloud/Recovery 선언·App 복구 인계. [Draft PR #9](https://github.com/seokpan/seokpan-hybrid-gitops/pull/9) 후속 작성과 D의 [#5](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5)·[#6](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6) 실제 검증을 구분 |
| [Infra #25 실행](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) | TH-10~13·16·19의 ROSA 입력/Root·관리/Secret·Plan/Cost·통합·재생성·최종 보존/정리. A [#23](https://github.com/seokpan/seokpan-hybrid-infra/issues/23)·D [#18](https://github.com/seokpan/seokpan-hybrid-infra/issues/18)·C [#19](https://github.com/seokpan/seokpan-hybrid-infra/issues/19)의 Owner/인계는 유지 |

#### Source와 실제 접수 범위

네 Repo Source 조회 기준은 `2026-10-02T11:39:14.141Z` / `2026-10-02T20:39:14.141+09:00`이고, 이후 새 Infra PR #24 HEAD와 등록 객체를 추가 연결했다. Docs 기록 기반은 열려 있는 [PR #20](https://github.com/seokpan/seokpan-hybrid-docs/pull/20) HEAD `006d374b08d8c19fa1f047c8658a9c479dfe64f4`다. main 병합·실제 Runtime 재실행을 뜻하지 않으며, 모든 객체가 같은 순간에 조회된 Snapshot도 아니다. 과거 관측·다른 담당자의 행·§9.9/9.10은 그대로 보존한다.

- **I01:** §9.10의 고정 Seed와 App 최종 `8828ed22295c27c6f3b419e762b865d17eb50b8c`·77개 이력 Bundle/로컬 검사 보고, [B 원 lab 참고 범위 수신](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5#issuecomment-5950971514), GitOps PR #9 HEAD `f1e959d2f3ec5207cc42f0523cbd391930b247d7`의 Kustomize 후보를 연결했다. App 인증 Push/PR·개인 미반영 코드 대조, D 새 Build/Scan/Registry별 Digest·실제 lab, C/D 새로운 대상/CA/AUTH·Recovery Bundle 수신은 별도다. PR #9의 입력 대기·replicas0를 실행 준비 완료로 바꾸지 않는다.
- **I02:** [A의 #23 답변](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-5951505800)을 Source로 접수했다. A는 공통 Backend/Provider/변수/출력·foundation 전체 통합/Plan/Apply, D는 Registry/CI 전용 파일을 같은 Root에 작성한다. 네 사람 personal/Bootstrap 완료 보고는 보존하며 rosa 서비스 Role 권한·실제 입력/지원·Plan 증거로 확대하지 않는다. 필요한 제한 출력의 실제 개정·공급/수신 합의와 A 리뷰는 대기한다.
- **I04:** [B CI A~F 리뷰](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-5950294428)·[D 방향 수신](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-5950470901)은 완료한 범위로 유지한다. [후속 정합 기록](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-5951015819)과 새 Infra PR #24의 코드/설명 차이는 사용할 개정의 준비 수신 조건이다. 실제 Job/PAT 정책·재현 등록·Push/Scan/Preview/Pull·A 통합 Plan을 완료로 표기하지 않는다.

#### ROSA 독립 문서 준비와 실제 Gate

[ROSA 문서 준비 PR #27](https://github.com/seokpan/seokpan-hybrid-infra/pull/27), Commit `cfcf10d8c64a1eac6bdd4ade335569c2d7d00a55`는 `terraform/rosa/README.md`·`INPUT_CONTRACT.md` 두 문서를 준비한다. Public Classic Multi-AZ, 정본 Key `phase2/rosa/terraform.tfstate`, 설치 Subnet Public3+ROSA Private3, 제한된 출력의 필드 의미·Account/Region·출처/개정/실재 자원 대조·오류 차단·A 리뷰·T19·최종 보존/정리 조건을 연결한다. 정확한 공급 필드명/형태·소비 HCL Schema·실제 수신 개정은 **후속 HCL 수신계약**으로 대조한다. HCL/Root Lock·Cloud 객체·Role 정책·Secret·Plan/Apply를 구현/실행한 PR이나 전체 TH-10 완료가 아니다. PR의 준비 Commit 게시와 리뷰·병합·A의 수신 결과는 각각 구분한다.

Data SG 본체/기반 Rule은 foundation, Worker→Data의 종속 Binding은 rosa, ECR Worker Pull Policy/실제 Classic Worker Role Attachment는 foundation Owner를 유지한다. [A #23](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-5951505800)과 새 PR #24 모두 Worker Pull을 미완료로 남겼다. 실제 Role/공유 범위·지원 연결과 서비스/기반 조회 권한은 A/B 후속 PR·검증으로 확인한다. Bootstrap의 Backend 권한 또는 ECR/CI 권한 Apply 보고를 ROSA 서비스/Runtime Pull 성공으로 바꾸지 않는다.

실제 Plan은 해당 Root Code/Lock·입력·Caller/MFA/목적 Role·Backend/Lock·지원/Quota·보호 Plan 경로를 확인한 뒤 수행한다. Apply는 Root 전체 실제 Plan/A 리뷰, 최신 기반 인계·Secret/Pull·Cost/Window·단일 지정 실행자를 확인한다. 전체 누적+잔여 기반/Data+ROSA Window+전송/관측+재시험/정리 지연 비용에서 **$450 계획선 초과 시 신규 가동 보류·조정, $500 전체 한도**를 유지한다. 실제 단가/시간/입력 없이 Cost PASS·Window 개시를 확정하지 않는다.

T19는 삭제 전 기존 Binding의 foundation 재실행 중 유지, Binding 해제 뒤 기반 Rule/Data/Network와 bootstrap Backend 보존, 새 Worker SG·Host/Context 연결·양쪽 정상 Plan·GitOps/Secret/Pull/업무 재현을 구분해 검증한다. 최종 삭제는 T19와 별도이며 App 쓰기/진행 상태·최신 로컬 Backup·Image/Render/도구/독립 사본/복호화 수단 접근·복원 가능성을 확인한다. 기본 Destroy는 rosa, foundation/bootstrap 전체 Destroy는 별도 명시적 승인 조건을 유지한다. 실제 삭제·잔존/후속 비용·보관 책임과 불필요 인증 폐기/보존 Key 유지는 해당 Owner의 결과로 기록한다.

#### 새 Registry/CI PR의 수신 조건

[Infra PR #24](https://github.com/seokpan/seokpan-hybrid-infra/pull/24) HEAD `33432eecc6cae81f7725c9d39f8a7730ca9ce815`는 담당 4파일 Source 제출이며 미승인·실제 통합 Plan/Apply 전이다. [B의 후속 리뷰](https://github.com/seokpan/seokpan-hybrid-infra/pull/24#issuecomment-5951869578)에 부분 Source 수신과 최종 Preview/E2E Gate를 분리해 연결했다. `registry.tf`의 N50·untagged7일을 확정 입력으로 수락하지 않는다. [Infra #18](https://github.com/seokpan/seokpan-hybrid-infra/issues/18)/[App #2 방향 수신](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-5950470901)의 **Preview 전 untagged 만료 제외·N 보류**와 코드가 정합돼야 한다. A1의 Harbor 사본 Scan/Smoke와 PR 본문의 ECR Pull 설명, `GetDownloadUrlForLayer`의 실제 E2E 필요 범위도 후속 정합 대상으로 유지한다.

담당자가 코드/설명을 정합한 개정의 준비 범위는 부분 수신할 수 있다. 최종 N·Lifecycle/CI 권한·Worker Pull의 확정/PASS는 실제 Preview/E2E·Role 검증에 연결하며, A~F 방향 전체를 다시 승인 대기로 돌리지 않는다. 입력 대기는 해당 실행에만 적용하고 ROSA 입력계약/HCL·App/base·학습/기록의 독립 준비는 계속한다.

#### 다음 작업과 기록

등록과 문서 준비는 실제 실행 결과가 아니므로 **새 Run 디렉터리·빈 Run·Run Index·Shared Execution 실제 행을 추가하지 않았다.** 본인 작업·코드·인계·실행·시험의 다섯 축을 분리한다. 상세 원본은 해당 Issue/PR에, 실제 시험/재시험은 새 Run에, 05/WORK_TRACKER와 상위 Issue에는 링크·상태·영향을 연결한다. 수신 개정/범위·보완·Reviewer와 배정 담당/실제 수행자·Caller를 구분하고 보호 원본 경로/접근/보존 책임은 보호 운영 대장에 기록한다.

다음은 개인 미반영 변경/인증 Push와 실제 입력 확인, D 새 Image/검증 인계, PR #9/문서 준비 PR의 리뷰·수신, PR #24 정합 개정·A 제한 출력/Worker Role 소비 리뷰다. 다중 Pod 위험 조사는 TH-04/06부터 앞당기며 실제 Runtime 시험은 환경/정상 Baseline을 확보한 뒤 진행한다. Docs PR 반영 대기 때문에 직접 인계·독립 준비를 멈추지 않는다. 현재 연결은 [WORK_TRACKER 등록 후속](WORK_TRACKER.md#tjung03-registered-work-20261002)을 따른다.

## 남은 작업과 다음 단계

- [x] 최종 04·지침 등록 확인과 전체 설계 완료 상태 유지
- [x] 01:27 KST 기준 팀 전체 main/Tree·Branch·PR/Issue 관측과 05 진입 안내 연결
- [x] 역할별 첫 작업·직접 기록·인계 수신 확인·공유 실행·동시 문서 편집 보강
- [x] 연쇄 추적과 보완 후 재검증에서 추가 보완 0건으로 수렴
- [x] 협업 사용본의 저장소 경로·기존 Issue/부분 보고·별도 발표 참조 연결
- [x] 네 사람 계정 매핑·네 저장소 권한 API 조회 완료 — 16건 모두 admin
- [ ] 개인 본인환경의 실제 사용·현재 미반영 Source·실제 입력 인계 — Issue #8
- [x] 앞선 B 고정 Source의 Path/Port/Client 계약과 App 연결·GitOps 로컬 초안 검사 — 실제 배포 준비 완료와 구분
- [x] 2026-10-02 추가 자료 분류·비민감 GRANT/I03 부분 접수·최신 Issue/Source 연결 — §8
- [x] 1차 MariaDB 읽기 전용 사전 점검과 데이터 이관 범위 결정(실제 데이터 논리 덤프) — 8.7절(1차 MariaDB 사전 점검과 데이터 이관 범위), Infra #17
- [x] 실사용자 데이터 이관 여부 결정 — 그대로 이관, `login_id` 가명화 대안 사용 안 함, 취급 조건 유지 — Infra #17
- [x] foundation Data 코드 초안·정적 검증과 foundation Role Data 권한 요청 — 8.8절(foundation Data 코드 초안과 Data 권한 요청), Infra #19
- [x] 복구 목표 피드백·특정 수치 우선 권고 수정과 기존 W04/T17/T18 예행/부담 판단 준비 — §9
- [x] Run 시각 계산 보조 구현·합성 입력 검사 — §9.8, 실제 시험과 구분
- [ ] 실제 복구 예행·백업 최신성·팀 부담 확인과 필요 목표 변경 결정 — §9, I03/I05/I07
- [ ] Data 코드의 foundation Root 직접 배치 전환·PR과 첫 plan 확인 — Infra #19, 이유빈 Network 코드 merge 후
- [ ] I01~I07의 현 Source·실제 입력/결과·미반영 작업·담당별 가용시간/비용 인계
- [x] 고정 Seed Source·원 lab 참고 범위 수신, App 연결 코드·이력 보존 묶음·실제 Kustomize 후보 구현 — §9.9
- [ ] 인증된 App 원격 이관/PR·새 Build/Scan·실제 lab/완성 Bundle — §9.9
- [ ] 병행하는 foundation/Data/CI 구현과 B의 ROSA 코드 연결·실제 Plan 준비
- [ ] 비용 확인 후 Cloud 생성·App/Data/Secret·GitOps 통합
- [ ] 장애·재생성·복구·부하 시험과 Must 결과 판정
- [ ] 결과·시연·발표·자원 정리와 보존 책임 완료

다음은 **공유 가능한 협업 사용본·기록 위치를 팀에 연결하고, 각 담당자가 현행/실제 입력을 직접 갱신하며 독립 구현과 인계를 병행**하는 것이다. B에서는 실제 Seed/실습 인계→저장소 반영·전체 테스트/Build→완성 Kustomize Build와 실습을 연결한다. 05 전체는 실제 구현·최종 검증 완료 전이며, 03·04의 설계 종료는 유지한다.


