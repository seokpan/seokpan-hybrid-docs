# 石나가는 판단 2차 프로젝트 — 팀 작업·환경 전환·입력 인계 안내

| 항목 | 내용 |
| --- | --- |
| 프로젝트 | 석판팀(石나가는 판단) 2차 프로젝트 — AWS Hybrid Cloud 마이그레이션 및 운영 검증 |
| 프로젝트 기간 | 2026-09-28 ~ 2026-10-26 |
| 작성일·기준일 | 2026-10-02, Asia/Seoul(KST, UTC+09:00) |
| 공유 현황 확인 시각 | 2026-10-02 04:48 KST. 저장소 권한·Source의 개별 관측 시각은 공통 진행표를 따름 |
| 문서 관리 | 정태훈(tjung03) — 공통 기준·역할·인계 안내의 정합성 유지 |
| 문서 버전·성격 | 1.0 — 팀 공통 안내, 담당별 작업·입력 인계 안내 및 기존 역할 배정 참조 기록 |
| 목적 | 현재 Source와 결과 연결, 병렬 작업, OCP 사전검증, ROSA 가동 조건, 결과·인계·정리 기록 안내 |
| 적용 기준 | 승인된 01~04, 05 구현·통합·검증 진행 기록, WORK_TRACKER, Presentation Baseline |
| 역할 배정 근거 | 04 구현 준비와 실행계획 §2.2·§3. 기존 배정을 안내하며 새 배정 승인을 기록하지 않음 |
| 문서 상태 | 공유용 안내 작성본. 실제 팀 전달·개인별 열람·수신·작업 완료 여부는 해당 작업 기록에서 확인 |
| 권장 저장소 위치 | seokpan-hybrid-docs / execution / TEAM_WORK_AND_HANDOFF_GUIDE.md |

<a id="contents"></a>
## 목차

1. [문서 목적과 읽는 방법](#purpose)
2. [팀 공통 안내](#common)
   - [현재 단계와 저장소·문서 구조](#current-state)
   - [역할·공유 실행 책임과 병렬 협업](#roles-and-collaboration)
   - [OCP·ROSA 작업 구분과 전환 조건](#environment-transition)
   - [목표 일정과 실제 가동 확정](#schedule)
   - [기록 위치와 Issue #6·#8](#records-and-issues)
   - [첫 Source·입력 인계와 수신 확인](#first-handover)
   - [최종 결과 보존과 유료 자원 정리](#preservation-and-cleanup)
   - [담당별 안내 바로가기](#role-navigation)
3. [이유빈 — Foundation·Network·Hybrid·Host](#role-a)
4. [정태훈 — Application·GitOps·ROSA](#role-b)
5. [김상희 — Data·Backup·Restore·Offline Recovery](#role-c)
6. [최유준 — CI·Registry·OCP·측정·Evidence Index](#role-d)
7. [문서 변경·공유·수신 기록 원칙](#document-records)
8. [주요 용어](#terms)
9. [근거 문서와 검토 결과](#references-and-review)

<a id="purpose"></a>
## 1. 문서 목적과 읽는 방법

이 문서는 석판팀 2차 프로젝트의 공통 안내와 네 사람의 담당별 다음 작업을 한 파일에서 확인하기 위한 공유 문서다. 승인된 역할을 현재 Source·실제 입력·인계 대상과 연결하고, OCP 사전검증에서 ROSA 통합·최종검증으로 이어지는 조건을 설명한다.

먼저 [팀 공통 안내](#common)를 읽고, 공통 안내 하단의 [담당별 바로가기](#role-navigation)에서 본인 절로 이동한다. 실제 상세 작업은 연결된 작업 Issue·PR·Run에서 진행하고, 최신 상태는 WORK_TRACKER와 05에서 확인한다. 모든 설계 원문을 다시 읽는 것을 착수 조건으로 삼지 않고 본인 작업에 필요한 기준부터 확인한다.

이 문서는 협업 안내와 역할 배정의 참조 기록이다. 공식 시험·성공 기준은 03, 운영 책임·시작 조건은 04, 실제 진행과 통합 결과는 05 및 WORK_TRACKER가 담당한다. 실제 실행 증거는 evidence/의 Run에 기록한다. 문서 작성이나 저장소 등록은 팀원 전달·열람, 실제 수행·기여, 실행 준비 완료 또는 시험 성공을 증명하지 않는다.

00은 1차 종료 상태와 2차의 역사적 출발점이다. 현재 설계 기준은 후속 승인·결정이 반영된 01~04를 함께 적용한다.

<a id="common"></a>
## 2. 팀 공통 안내

<a id="current-state"></a>
### 2.1 현재 단계와 저장소·문서 구조

03 상세설계와 04 구현 준비의 문서 단계는 종료됐으며, 05는 지금부터 공동으로 사용하는 구현·통합·검증 진행 기록이다. 현재 단계에서는 각자의 미반영 Source와 실제 결과를 연결하고, 필요한 입력을 직접 인계하면서 구현을 계속한다. 구현·시험·발표 준비·자원 정리는 실제 결과와 별도로 완료를 판정한다.

기준 시각에 확인한 공유 기록은 다음과 같다.

- 설계·실행·발표 기준 문서는 Docs 저장소 main에서 열람할 수 있다.
- 네 사람의 GitHub 계정과 네 저장소 권한은 기존 진행표에서 확인됐다. 개인 환경의 실제 사용·기록 성공과 AWS·Cluster 인증은 해당 작업에서 별도로 확인한다.
- 현재 Source와 필요한 입력의 개인별 인계·수신 확인은 계속 필요하다. 진행표의 빈칸은 개인 로컬 작업의 부재나 실패를 의미하지 않는다.
- 첫 Full Apply의 조건 충족 근거와 실제 공유 실행 창은 진행표에 아직 연결되지 않았다.
- Docs Issue #6과 #8은 열린 상태다. 이후 상태는 각 Issue와 진행표를 확인한다.

첫 확인 순서는 다음과 같다.

1. [실행 안내](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/README.md)를 읽는다.
2. 이 문서의 본인 담당 절과 연결된 05의 담당별 첫 작업을 확인한다.
3. [다음 인계](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/WORK_TRACKER.md#next-handover)와 [입력 인계](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/WORK_TRACKER.md#input-handover)에 현재 작업·개정·필요 입력을 연결한다.

프로젝트 저장소는 다음과 같이 사용한다.

| 저장소 | 기록할 내용 |
| --- | --- |
| [seokpan-hybrid-app](https://github.com/seokpan/seokpan-hybrid-app) | Application 이관·수정, Build 대상 Source와 관련 검사 |
| [seokpan-hybrid-infra](https://github.com/seokpan/seokpan-hybrid-infra) | Terraform Root, AWS·Hybrid 기반, 실행 자동화, Data·Backup·Restore 관련 코드 |
| [seokpan-hybrid-gitops](https://github.com/seokpan/seokpan-hybrid-gitops) | 공통 base와 환경별 Overlay, Application·Platform 배포 선언, Release 후보 |
| [seokpan-hybrid-docs](https://github.com/seokpan/seokpan-hybrid-docs) | 설계·협업 안내·공동 진행 링크·정리된 실제 Run·발표 선별 기준 |

Docs에서 팀원이 실제로 확인할 위치는 다음과 같다.

| 경로 | 확인 목적 |
| --- | --- |
| [design/](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/design/README.md) | 00~04 원문과 역할 확인. 공식 Test/Acceptance는 03, 배정·실행 준비·인계는 04 |
| [architecture/](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/architecture/README.md) | 목표 구조와 흐름 확인. 현재 그림은 설계 목표이며 실제 구축 증거와 구분 |
| [execution/](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/README.md) | 실행 안내, 05, WORK_TRACKER, HANDOFF_TEMPLATE |
| [evidence/](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/evidence/README.md) | 실제 실행·수치·시간선·실패·재시험의 Run 기록 |
| [presentation/](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/presentation/README.md) | 실제 결과의 발표 후보 선별, 비교·주장 범위 확인 |

<a id="roles-and-collaboration"></a>
### 2.2 역할·공유 실행 책임과 병렬 협업

작성·통합 책임과 실제 공유 실행 책임은 04 §2.2의 배정을 따른다.

| 담당자·GitHub 계정 | 작성·통합 책임 | 공유 실행·조율 책임 | 주요 직접 인계 |
| --- | --- | --- | --- |
| 이유빈 · ggbun2 | bootstrap, foundation 전체 통합, Network·IAM·Hybrid·Host·필요한 최소 Ansible | bootstrap·foundation Root 실행 | 정태훈 ROSA 입력, 김상희 Data/Host, 최유준 Registry·자원/비용 |
| 정태훈 · tjung03 | App, 공통 base·환경별 Overlay, rosa Root, Release/Recovery App·관리 인증 연결 | rosa Root 실행, App 배포 변경 조율 | 최유준 Build/lab, 김상희 DB/Recovery, 이유빈 기반 요구 |
| 김상희 · kshi1313-gif | Foundation Data 영역, Data 이전·Backup·Restore·복구 준비 | Data 이전·Restore/Cutover | 이유빈 Data/Host, 정태훈 App/Recovery, 최유준 복구 Evidence |
| 최유준 · cyj200115-prog | Foundation Registry/CI 권한 영역, CI·관측·실제 base lab·측정 도구·Evidence Index | 시험·비용/시간 조율. 각 자원 실행자는 해당 배정을 유지 | 이유빈 Registry/CI·비용, 정태훈 Image/lab, 김상희 Recovery |

김상희와 최유준이 작성하는 Foundation 담당 선언은 같은 foundation Root/State에 통합한다. 전체 변경 통합·실행은 이유빈이 담당하며 별도 State나 담당 영역 단독 Apply로 분리하지 않는다. Resource Ownership도 기존 Terraform·GitOps·Secret 경계를 유지한다.

각자는 자기 작업 Issue·PR·Run에 결과를 작성하고 수신자에게 직접 인계한다. 정태훈은 본인 Source와 App/ROSA 통합을, 최유준은 시험 조율과 Evidence Index 연결을 담당한다. 담당별 원 기록과 수신 확인을 연결한다.

독립적인 Source 조사·코드 작성·렌더링·설정 준비·로컬 검증은 병렬로 진행한다. 입력이 부족하면 그 입력에 의존하는 실행만 대기로 남긴다. 같은 State 쓰기, 공유 배포, Restore/Cutover, 장애·부하 시험은 실행자·입력·리뷰·Caller/Context·Plan·비용·시간 조건을 확인하고 순서를 조율한다.

인계나 대체 실행이 필요한 경우 배정 담당자, 실제 작성자·수행자, 사용 Principal, Reviewer와 협업 범위를 구분해 기록한다. Commit 계정만으로 실제 수행자를 단정하거나 기존 실습을 현재 배정 담당자의 기여로 소급하지 않는다.

<a id="environment-transition"></a>
### 2.3 OCP·ROSA 작업 구분과 전환 조건

OpenShift Container Platform(OCP) 실습 환경은 사전검증에 사용한다. Red Hat OpenShift Service on AWS(ROSA) Classic Multi-AZ는 정상 Cloud 서비스의 최종 대상이다. 같은 네 사람이 담당 영역을 유지하며 환경별 준비·통합·검증을 이어간다.

| 영역 | OCP·로컬에서 먼저 확인 | 실제 ROSA/AWS 또는 최종 복구 조합에서 확인 |
| --- | --- | --- |
| Application | 이미지·임의 UID/SCC·Probe·종료·Route/HTTP/WSS·인증·재접속·중복 처리 | 실제 Replica/AZ 배치·Ingress·RDS/Redis 연결·대표 업무·Resource/Pool |
| GitOps | 실제 base/Overlay Render·Sync/SelfHeal·Secret 참조·권한·삭제 보호 | 실제 ROSA 설치·관리 인계·재생성 후 Context/Host/Secret·Sync |
| Data | 테스트 DB/Redis의 Driver·TLS/CA·Hostname 검증·거부 Case·Migration 예행 | 실제 Endpoint·목적별 권한·TLS·RDS/Redis Failover·업무/Data 일관성 |
| CI·Pull | Build/Test/Scan·Job/PAT·Harbor·lab Pull | ECR 신규 Worker/캐시 없는 Pull, 12시간 이상 지속 사용 후 새 Pull, 재생성 후 Pull |
| Network·관측 | lab 정책·UWM/Alert 경로·수집·측정 도구 | 실제 AWS Route/SG/WireGuard·Cloud의 On-Prem 비의존·장애/Metric/Alert 상관 |
| Recovery·재현·비용 | 격리 Restore·자료/Key/도구·복구 Bundle 예행 | 검증 Backup/Release를 사용한 Offline 복구·RTO/RPO·Clean Recreate·실제 비용 |

기존 공개 예제·실습 결과, 실제 프로젝트 base의 검증, ROSA 최종 Acceptance는 환경·Source·이미지·조건별로 구분한다. 환경·버전·Commit·Digest·설정이 변경되면 영향을 받은 항목을 다시 확인한다.

정태훈은 실제 공통 base와 환경별 Overlay를 제공하고 최유준은 지정한 Commit·Context/Namespace에서 실제 base의 lab Argo 검증을 수행한다. 김상희와 정태훈은 DB/TLS/Migration 조건을 대조한다. 상세 인계는 [04 §3](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/design/04_IMPLEMENTATION_READINESS.md#3-base와-ocp-lab-인계)을 따른다. Cloud Application의 배포 참조는 lab Branch와 분리한다.

OCP 사전검증과 AWS 기반 코드 준비는 병렬로 진행한다. 실제 Plan과 실제 생성은 각각 필요한 입력을 확인한 뒤 진행한다. ROSA 가동에 필요한 주요 조건은 다음과 같다.

1. 가동할 Source·이미지·설정과 필요한 사전검증·인계 결과가 식별돼 있다.
2. 해당 Root의 도구·Provider/Lock, 실제 입력·Caller/Role·Backend, 지원·Quota를 확인하고 Root 전체 Plan과 자원·삭제 범위를 검토했다.
3. 필요한 인증·Secret 공급과 초기화 조건, 다음 실행자에게 넘길 출력·환경 조건을 확인했다.
4. 실제 가격·Credit·누적/잔존 비용·가동·재시험·삭제 시간을 반영한 Cost Gate와 실행 창을 확인했다.
5. 실행 책임자, 실제 수행자, 시작·종료 예정, 중단·잔존 처리와 다음 인계가 연결돼 있다.

조건이 충족되면 기존 bootstrap 정본을 기준으로 foundation → rosa 인계를 확인하고 Window A 통합을 진행한다. 모든 팀원의 모든 입력 제출을 독립 작업의 공통 선행조건으로 확대하지 않는다.

전체 예상 비용은 현재 누적 비용, 남은 기반/Data/Storage, 남은 ROSA Window, 전송·요청·관측, 정리 지연·실패 예상 비용을 합산한다. **$450 계획선을 초과하면 신규 가동을 보류하고 조정한다.** $50 여유를 포함한 **총 $500 한도**를 유지하며 실제 자료 없이 Cost PASS를 기록하지 않는다.

최종 Offline Recovery는 승인된 격리 로컬 환경에서 실제 Backup/Release와 장애 조건으로 수행하면 본 검증이 될 수 있다. ROSA 가동 구간 안에서만 수행하는 조건을 추가하지 않는다. AWS·GitHub·Cloud IDP·ECR·AWS KMS 신규 조회에 의존하지 않는 복구 경로를 검증하며 로컬 DNS·Harbor까지 차단하는 시험으로 확대하지 않는다.

확인 위치: [05 §0.5 환경별 검증](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/05_IMPLEMENTATION_AND_VALIDATION.md#05-ocp-사전-검증과-rosa-최종-검증), [§0.4 진행 순서](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/05_IMPLEMENTATION_AND_VALIDATION.md#04-실제로-진행하는-순서), [04 §6 시작 조건](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/design/04_IMPLEMENTATION_READINESS.md#6-작업별-구현-시작-조건).

<a id="schedule"></a>
### 2.4 목표 일정과 실제 가동 확정

Window는 ROSA를 필요한 기간에 생성·사용·삭제하는 가동 구간이다. Window A는 정상 통합과 결함 해소, Window B는 검증된 Release·복구 자료를 기반으로 재생성·장애·부하 등 최종시험을 수행하는 구간이다.

| 목표 기간·날짜 | 작업 |
| --- | --- |
| 10/1~10/2 | 설계 기준 종료·Source와 실행 입력 연결 |
| 10/5~10/8 | Foundation·핵심 PoC·Window A 후보 |
| 10/12~10/15 | Migration·통합·핵심 결함 해소·복구 자료 확보 |
| 10/16 | Technical Freeze — 핵심 구조·구현 동결 목표 |
| 10/19~10/21 | Window B 후보·재생성·장애·부하·Offline 검증 |
| 10/22 | Demo Freeze — 시연 구성 동결 목표 |
| 10/23 | Presentation Ready — 발표 준비 완료 목표 |
| 10/26 | 최종 점검·발표·프로젝트 종료 목표 |

이는 승인된 목표 일정이다. 10/5는 ROSA 자동 개시일이 아니다. 실제 Window A/B 시작·종료와 가동시간은 입력·Plan·비용·가용일을 받아 진행표에 확정한다. 주말·공휴일을 자동으로 가용시간에 포함하지 않는다. 목표를 맞추기 어려운 제약은 담당·영향·다음 행동을 드러내고 승인 목표를 임의로 변경하지 않는다.

Window A에서 정상 E2E·Backup·Release와 통합 결함 조치를 확보한다. Window B는 Clean Recreate → 정상 Baseline → 분리된 장애·복구 Case → 부하의 순서를 조율한다. 시험 준비는 병렬로 진행할 수 있으나 동일 환경의 충돌 실행은 조율한다.

일정 근거는 [05 §0.6](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/05_IMPLEMENTATION_AND_VALIDATION.md#06-승인-일정과-현재-미정인-시간), 실제 확정과 진행은 [WORK_TRACKER의 Shared Execution](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/WORK_TRACKER.md#shared-execution)을 확인한다.

<a id="records-and-issues"></a>
### 2.5 기록 위치와 Issue #6·#8

| 내용 | 기록 위치 |
| --- | --- |
| 상세 작업·진행·Blocker·인계 제출과 수신 확인 | 해당 App/Infra/GitOps 작업 Issue |
| 코드·검사·리뷰·최종 변경 | 해당 저장소 Branch/PR |
| 현재 Source·입력 개정·전체 인계와 통합 상태 | WORK_TRACKER와 05에 원본 링크·확인 시각 연결 |
| 실제 실행·수치·시간선·실패·재시험 | Docs의 evidence/&lt;test-id&gt;/&lt;run-id&gt;/ |
| 발표 후보·비교 분류·주장 범위 | Docs Issue #6에 원본 Run 링크와 간략 판정 |

같은 범위를 추적하는 기존 Issue가 있으면 재사용한다. 별도 산출물·완료 조건이 필요한 작업만 분리하며, 이 안내에서 새 Issue 번호·성공값·실제 시각을 미리 만들지 않는다.

**[Docs Issue #8 — 05 팀 접근·현행 작업·실제 입력 인계 연결](https://github.com/seokpan/seokpan-hybrid-docs/issues/8)**

각자의 저장소 실제 사용, 현재 Source, 필요한 입력, 다음 수신자의 사용 가능 여부를 연결하는 추적 Issue다. 저장소 권한 확인 후에도 개인별 Source·입력 인계·수신 확인이 남아 있어 기준 시각에 열린 상태다. 대표 작업 Issue/PR와 인계 상태를 연결하고 상세 결과·로그는 원래 작업 위치에 둔다.

댓글에서 요청한 Presentation Baseline 링크와 병합 상태 현행화는 반영됐으며 [처리 답변](https://github.com/seokpan/seokpan-hybrid-docs/issues/8#issuecomment-5938904136)이 남아 있다. 이 요청의 처리 완료와 Issue #8 전체 인계 완료는 구분한다.

**[Docs Issue #6 — 05 구현·검증 결과 발표 Evidence 추적](https://github.com/seokpan/seokpan-hybrid-docs/issues/6)**

실제 Run 중 발표에 사용할 후보를 놓치지 않고 추적하기 위한 Issue다. 원본 Run 링크와 후보 판단·비교 분류·주장 범위/한계를 연결하며 원본 수치·로그·시간선은 Run에 보존한다. 앞으로 확보할 결과를 계속 추적하므로 기준 시각에 열린 상태다.

공식 Test/Acceptance는 [03 상세설계](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/design/03_DETAILED_DESIGN.md), Actual은 05와 evidence/, 발표 선별은 [Presentation Baseline](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/presentation/PRESENTATION_BASELINE.md)을 따른다. 발표 기준을 시험 조건·성공 기준·실제 결과를 변경하거나 재해석하는 근거로 사용하지 않는다. 1차 재측정은 2차 Harness·측정 정의가 충분히 고정된 뒤 동일·대응 조건의 비교 가치가 있는 항목만 검토한다.

각 실행 담당자가 자기 증거를 작성하고 최유준은 Index와 형식을 연결한다. Run에는 실제 Source 전체 SHA·이미지 Digest/플랫폼·입력/도구/환경 개정·실행자/Reviewer·UTC와 KST 시각·시험 조건을 연결한다. 실패 Run을 보존하고 재시험은 새 Run으로 연결한다. 판정은 NOT RUN/PASS/PARTIAL/FAIL/N/A로 기록하며 PASS에는 해당 조건의 증거, N/A에는 이유·제외 범위가 필요하다.

<a id="first-handover"></a>
### 2.6 첫 Source·입력 인계와 수신 확인

각 담당자는 [HANDOFF_TEMPLATE](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/HANDOFF_TEMPLATE.md)을 기존 작업 Issue의 본문이나 댓글에 사용한다.

1. 대표 Issue/PR/Run, 저장소·브랜치·전체 커밋 SHA, 입력 개정을 기록한다.
2. 완료한 범위·검사/실행 조건·결과 근거와 미확인·남은 범위를 구분한다.
3. 필요한 입력, 제공 담당자, 직접 막히는 후속 작업과 다음 확인 시점을 기록한다.
4. 수신자와 사용할 대상·범위를 지정하고 진행표에 원본 링크를 연결한다.
5. 수신자는 받은 개정·접근 여부·사용 범위를 확인하고 수락/일부 수락/보완 요청/보류와 후속 작업을 기록한다.

인계 수락은 후속 실행 성공과 별도다. 입력이 없는 작업만 대기하고 계속할 독립 준비를 적는다. 개인 본인 환경의 첫 작업 기록으로 실제 사용을 확인하며 별도 형식적인 시험 Commit을 요구하지 않는다.

비밀번호·Token·Private Key·전체 Credential, 평문 또는 전체 State/Plan, SQL/Backup 원본과 상세 보호 접속정보는 공개 기록에 넣지 않는다. 보호 경로의 논리 참조·보관자·접근/보존 책임을 연결한다.

새 Source나 실측 제약은 01~04와 대조한다. 이미 정합한 구현, 필요한 구현 보완, 미착수 항목, 실제 결과 대기 항목을 구분한다. 승인 구조·권한·성공 기준·기간/비용을 바꿔야 하는 제약은 원인·직접/후속 영향·대안·결정을 기록하고 관련 기준을 현행화한다. 일상 실행 기록만으로 종료된 설계문서를 매번 재개하지 않는다.

<a id="preservation-and-cleanup"></a>
### 2.7 최종 결과 보존과 유료 자원 정리

최종 검증·재시험·영상·보고서·질의 근거를 확보한 뒤 필요한 Live Demo 여부와 비용을 함께 판단한다. ROSA 삭제 전에 필요한 원본 증거·Source/Release·Runbook·영상·비용/시간선을 외부에 보존하고 실제 접근·무결성을 확인한다.

검증 Backup, Harbor 이미지, 렌더링한 배포 자료·도구, 필요한 복호화 Key와 독립 사본을 보존하고 복원 가능성을 확인한다. 기존 1차 자원은 승인된 보호 경계를 유지한다.

자원별 Owner, 삭제/보존 대상, 실행 범위·의존 순서, Data/State 보호, 남길 비용과 책임을 기록한다. 기본 비용절감 Destroy는 rosa State이며 **foundation/bootstrap 전체 Destroy는 기존의 별도 명시적 승인 조건을 유지한다.** 이 안내가 추가 삭제 권한을 부여하지 않는다.

삭제 요청과 완료를 구분하고 실제 자원 목록·비용 대장으로 잔존을 확인한다. 불필요한 자격증명은 정리하되 보존 자료의 해독에 필요한 Key는 구분해 유지한다. 남길 자료·자원의 담당, 보존 기간·비용, 후속 청구 확인 책임을 남긴다.

05 종료는 핵심 Must의 실제 판정과 제한, 재현·복구 가능한 조합과 자료, 발표·보고·시연 준비, 각자의 실제 기여, 자원 정리·잔존/보존 책임이 연결됐는지로 판단한다. 상세 절차는 [05 §0.8](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/05_IMPLEMENTATION_AND_VALIDATION.md#08-유료-자원-정리와-05-종료)을 따른다.

<a id="role-navigation"></a>
### 2.8 담당별 안내 바로가기

공통 안내를 확인한 뒤 아래 본인 안내로 이동한다.

| 담당자 | 역할별 안내 |
| --- | --- |
| 이유빈 | [Foundation·Network·Hybrid·Host 작업과 인계](#role-a) |
| 정태훈 | [Application·GitOps·ROSA 작업과 인계](#role-b) |
| 김상희 | [Data·Backup·Restore·Offline Recovery 작업과 인계](#role-c) |
| 최유준 | [CI·Registry·OCP·측정·Evidence Index 작업과 인계](#role-d) |

<a id="role-a"></a>
## 3. 이유빈 — Foundation·Network·Hybrid·Host

### 3.1 담당 범위와 첫 기록

이유빈은 bootstrap과 foundation 전체 통합·실행, Network·공통 IAM·Hybrid·Host와 필요한 최소 Ansible, 다른 담당자가 사용할 기반 출력을 담당한다.

현재 Infra 작업 Issue/PR에 다음을 연결한다.

- 브랜치·전체 커밋 SHA, 실제 완료 범위와 결과
- 완료된 Bootstrap 결과와 이후 변경
- 세션 발급 실패 시 이전 Role 환경이 남는 문제의 후속 Source·실패 차단 확인 결과
- 부족한 입력·제공 담당자·다음 확인 시점

완료된 Bootstrap 작업은 기존 결과로 연결하고 남은 변경부터 진행한다. 현재 Remote State 정본과 보호 이전 기록을 확인하며 각 팀원의 clone에서 State 이전을 반복하지 않는다.

기존 작업 원본은 [Infra Issue #10](https://github.com/seokpan/seokpan-hybrid-infra/issues/10), [PR #11](https://github.com/seokpan/seokpan-hybrid-infra/pull/11), [PR #12](https://github.com/seokpan/seokpan-hybrid-infra/pull/12)을 참고한다. 이후 실제 Foundation 작업과 세션 실패 처리의 최신 상태는 담당자가 별도로 연결한다.

### 3.2 OCP·로컬 준비와 ROSA 통합 연결

OCP 사전검증과 병행해 Foundation HCL·도구/Provider/Lock, Network 요구사항, 기반 출력 계약을 준비한다. 가능한 정적·로컬 확인과 실제 Plan/Apply 결과를 구분한다.

김상희의 Data 선언과 최유준의 Registry/CI 권한 선언을 같은 foundation Root에 통합한다. 실제 Plan은 Root 코드·도구/Provider/Lock·현재 Caller/Role·Backend/Lock·실제 입력과 보호된 Plan 저장 경로를 확인한 뒤 수행한다. 실제 Apply는 생성된 Root 전체 Plan의 직접·후속 영향과 자원·삭제 범위, 지원·실행 입력과 해당 비용/시간 조건을 검토한 뒤 수행한다. 새 인증 실패 후 공유 실행 전에 현재 Caller/세션을 확인한다.

정상 통합에서는 foundation 적용 결과와 제한된 출력을 정태훈에게 인계하고 정태훈이 rosa Root 작업을 이어간다. 원래 Root 실행 배정과 State 쓰기 실행자 한 명 원칙을 유지한다.

### 3.3 직접 인계할 내용

| 수신자 | 인계 내용 |
| --- | --- |
| 정태훈 | ROSA에 필요한 Network·IAM 등 제한된 출력, 입력 개정·사용 조건과 남은 제약 |
| 김상희 | Data·Host 기반 구성과 실제 자산 조건 |
| 최유준 | Registry/CI 기반 정보, 자원 수명·구성 및 비용 산정 입력 |

실제 ID나 출력이 아직 없으면 먼저 공유할 계약과 실제 제공 시점, 막히는 후속 작업을 구분한다. 상세 작업은 Infra Issue/PR, 상태는 WORK_TRACKER와 Docs Issue #8에 연결한다.

확인 문서: [05 이유빈 담당](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/05_IMPLEMENTATION_AND_VALIDATION.md#이유빈), [다음 인계](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/WORK_TRACKER.md#next-handover), [04 시작 조건](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/design/04_IMPLEMENTATION_READINESS.md#6-작업별-구현-시작-조건).

[담당별 바로가기](#role-navigation) · [목차](#contents)

<a id="role-b"></a>
## 4. 정태훈 — Application·GitOps·ROSA

### 4.1 담당 범위와 첫 기록

정태훈은 Application, GitOps 공통 base·환경별 Overlay, rosa Root, 관리·인증 연결과 Release/Recovery App 통합을 담당한다.

실제 App 이관 직전에 검증된 기준 Source(Seed)의 전체 SHA와 검증 근거를 고정하고 Seed까지 Git 이력을 보존한다. 관측 main을 검증 Seed로 자동 채택하지 않는다. 미반영 Maintenance·로컬 변경, 기존 Overlay 원본·작성자/수행자·이미지/설정 조건을 확인하고 1차 상속 내용과 2차 변경·실제 기여를 구분한다.

현재 App/GitOps/ROSA 작업 Issue에 Source·완료 범위·필요 입력·다음 인계를 연결한다.

### 4.2 OCP 사전검증 준비

다음 계약과 Source를 준비한다.

- App 경로·포트·설정·TLS·Probe·SCC·세션/WebSocket·다중 Pod 관련 계약
- 공통 base와 Cloud·lab·Recovery 환경별 Overlay, Render와 가능한 로컬 검증
- Build 대상 Source와 이미지 조건
- 최유준의 실제 base 검증에 필요한 브랜치·전체 Commit·Digest·Secret 참조·Context/Namespace 조건
- 김상희와 대조할 DB/TLS/Migration 및 Recovery App 연결·업무 확인 항목

실습용 설정과 Cloud 배포 참조를 분리하고 Cloud Application을 lab Branch에 연결하지 않는다. 최유준에게 실제 base 결과를 받아 검증 개정·조건과 이후 변경의 영향을 확인한다.

### 4.3 ROSA 통합·최종검증 연결

AWS 기반 코드·ROSA 입력 준비는 OCP 검증과 병행한다. 실제 rosa Root Plan은 해당 Root 코드·도구/Provider/Lock·실제 입력·Caller/Role·Backend와 보호된 Plan 저장 경로를 확인한 뒤 수행한다. 실제 ROSA 생성·Apply는 생성된 Root 전체 Plan을 검토하고 최신 Foundation 인계, 지원·Quota, 필요한 Secret 초기화와 Cost/Window 조건을 확인한 뒤 진행한다.

Window A에서 실제 ROSA·RDS·Redis·ECR·Secret·GitOps·대표 업무 흐름을 연결하고 정상 Baseline·Backup·검증 Release를 확보한다. Window B에서 재생성·장애·부하 Case의 App·배포 조합을 지원한다. 김상희의 최종 Offline Recovery에 사용할 App·이미지·렌더링한 선언·설정과 업무 확인 조건을 인계한다.

관리 인계에서는 실제 지원 방식에 맞춰 정상 개인 IDP/RBAC의 허용·거부, 유지할 비상 관리 경로, 초기 Bootstrap 인증과 관련 Token/세션 회수 결과를 확인한다. 정상·비상 접속과 회수 후 재접속 결과를 남기며 마지막 유효 관리 경로를 확인한 순서로 인계한다. 기준은 [04 §5.6](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/design/04_IMPLEMENTATION_READINESS.md#56-확정된-비상-접속과-초기-관리자-회수)을 따른다.

### 4.4 직접 인계할 내용

| 수신자 | 인계 내용 |
| --- | --- |
| 최유준 | 실제 Build/lab 대상 App/base 커밋·범위, 이미지·배포 조건과 검증 요청 |
| 김상희 | DB/TLS/Migration 요구, Recovery App 연결·대표 업무/Data 확인 항목 |
| 이유빈 | Foundation 출력 사용 요구와 ROSA 기반 조건 |

정태훈은 받은 개정과 사용 범위를 확인하고 본인 Source·통합 기록을 갱신한다. 다른 담당자의 상세 결과는 각자가 원래 Issue/PR/Run에 작성한다.

확인 문서: [05 정태훈 담당](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/05_IMPLEMENTATION_AND_VALIDATION.md#정태훈), [04 base와 ocp-lab 인계](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/design/04_IMPLEMENTATION_READINESS.md#3-base와-ocp-lab-인계), [환경별 검증 범위](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/05_IMPLEMENTATION_AND_VALIDATION.md#05-ocp-사전-검증과-rosa-최종-검증).

[담당별 바로가기](#role-navigation) · [목차](#contents)

<a id="role-c"></a>
## 5. 김상희 — Data·Backup·Restore·Offline Recovery

### 5.1 담당 범위와 첫 기록

김상희는 Foundation Data 선언, 목적별 DB 권한·TLS·Migration, Backup·격리 Restore·Recovery 준비와 실제 Data 이전·Restore/Cutover를 담당한다.

현재 작업 Issue/PR·브랜치·전체 SHA, 실제 완료 범위·결과와 미공유 Source를 연결하고 다음 입력을 확인한다.

- 사용할 Host의 실제 CPU/RAM/디스크 여유·복구 공간과 독립 Data/Storage 조건
- Schema·목적별 GRANT·Driver/Client·TLS/CA와 확인 결과
- Backup·독립 사본·복호화 수단의 보호 논리 참조와 접근/보존 책임
- 부족한 값·제공 담당자·다음 확인 시점

새 복구 VM 생성 가능 여부와 실제 Host 자원 여유는 구분하며 실측 없이 배치·복구 공간 확보 완료를 기록하지 않는다.

### 5.2 OCP·로컬 준비와 실제 Cloud Data 연결

정태훈과 Driver·권한·TLS/CA·Hostname·Migration 계약을 대조하고 확보한 자산부터 격리 복원·Bundle 예행을 진행한다. 테스트 DB·대역 환경의 결과를 실제 RDS·Redis 결과와 구분한다.

Foundation Data 선언은 김상희가 작성하고 이유빈이 전체 Root에 통합·Apply한다. 실제 Cloud 입력이 필요한 작업과 독립적인 복구 준비를 나눠 병행한다.

ROSA 통합에서는 실제 Endpoint·목적별 권한·TLS로 App 연결·데이터 이전·Backup을 확인하고 정태훈에게 인계한다. 최종시험에서는 Failover와 업무/Data 일관성 등 본인 영역의 실제 결과를 확인한다.

### 5.3 최종 Offline Recovery와 결과 기록

승인된 새 전용 VM의 격리 MariaDB에 직접 TLS로 연결하고 새 Recovery Redis를 사용한다. 기존 1차 DB/MaxScale·Data는 보호한다.

실제 Restore/Cutover 전 격리 환경·저장 공간·CA·검증 Backup·복호화 수단·검증 Release/이미지·App 업무 확인 범위를 맞춘다. 장애 중 AWS·GitHub·Cloud IDP·ECR·AWS KMS 신규 조회에 의존하지 않는 경로를 사용하고 로컬 DNS·Harbor 차단으로 범위를 확대하지 않는다.

다음 결과를 실제 Run에 남긴다.

- 사용 Backup ID/hash, 데이터 기준 시각과 확인 수준
- TLS·목적별 권한, 복원 Schema·행·관계와 대표 업무/Data 확인
- 장애/접속 불가 시작, 탐지·결정·복원·App/Host 안내·업무 확인의 단계 시각
- RTO/RPO 판정, 확인된 데이터·Redis Runtime 손실, 실패·재시험과 제한

RTO는 장애/접속 불가 시작부터 대표 업무·Data 확인까지의 전체 시간이며 현재 승인 목표는 **10분 이내**다. 영속 DB RPO는 사고 시각과 실제 사용 Backup의 데이터 기준 시각 차이이며 현재 승인 목표는 **30분 이내**, 운영 중 Portable Backup은 **15분 주기**다. [03 §3-I.14.5](../design/03_DETAILED_DESIGN.md#recovery-design-decision-20261005)의 범위·선택 근거·실행 Gate를 따른다. [Docs #30](https://github.com/seokpan/seokpan-hybrid-docs/pull/30)의 main 병합으로 설계 선택은 완료됐다. 기존 30분·90분·1시간은 이전 시점의 기록으로 보존한다. 실제 가동·전송·최신성·전체 업무 재개 검증은 별도 수행한다. 백업 주기만으로 RPO 충족을 보장하지 않는다. 파일 수정·Dump 종료 시각으로 데이터 기준을 대체하지 않고 정확한 시점이 불확실하면 범위·확인 수준을 기록한다. Import 명령 성공이나 합성 부분 예행만으로 업무 복구 PASS를 판정하지 않는다.

### 5.4 직접 인계할 내용

| 수신자 | 인계 내용 |
| --- | --- |
| 이유빈 | Foundation Data·Host 선언과 필요한 입력·자산 조건 |
| 정태훈 | DB/TLS/Migration·Recovery 연결과 업무 확인 조건·결과 |
| 최유준 | Backup 식별자·데이터 기준 시각·복구 시간선·판정과 원본 Evidence 링크 |

비밀값과 Backup 원본은 보호 참조로 연결한다. 상세 작업·Source와 수신 확인은 해당 Issue/PR, 공동 상태는 WORK_TRACKER와 Docs Issue #8에 연결한다.

확인 문서: [05 김상희 담당](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/05_IMPLEMENTATION_AND_VALIDATION.md#김상희), [입력 인계](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/WORK_TRACKER.md#input-handover), [실제 Run 기록 안내](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/evidence/README.md).

[담당별 바로가기](#role-navigation) · [목차](#contents)

<a id="role-d"></a>
## 6. 최유준 — CI·Registry·OCP·측정·Evidence Index

### 6.1 담당 범위와 첫 기록

최유준은 Jenkins/CI·ECR/Harbor·Scan, Foundation Registry/CI 권한 선언, 실제 프로젝트 base의 OCP 검증, 관측·측정 도구·시험/비용 조율과 Evidence Index를 담당한다.

현재 작업 Issue/PR·브랜치·전체 SHA·완료 범위와 다음을 연결한다.

- 기존 GitOps 실습 Issue #1~#4 등 필요한 결과와 원본 Manifest/Overlay·Commit·이미지·조건
- 확인된 원래 작성자·수행자와 실제 수행 범위
- Jenkins Job/Agent·Credential Binding·Scan·Registry·PAT 정책·저장소 규칙의 현재 구성
- 부족한 입력·제공 담당자·다음 확인 시점

기존 실습은 원본 결과와 수행 범위로 연결한다. 변경된 조건이나 아직 검증하지 않은 부분에 새 Run을 수행하며 과거 결과를 새 Commit의 검증으로 대체하지 않는다.

기존 보고는 [GitOps Issue #1](https://github.com/seokpan/seokpan-hybrid-gitops/issues/1), [#2](https://github.com/seokpan/seokpan-hybrid-gitops/issues/2), [#3](https://github.com/seokpan/seokpan-hybrid-gitops/issues/3), [#4](https://github.com/seokpan/seokpan-hybrid-gitops/issues/4)를 참고한다. 현재 CI·실제 base·최종시험 작업은 담당자가 해당 Issue/PR로 연결한다.

### 6.2 실제 base의 OCP 검증과 CI·이미지 인계

정태훈에게 실제 프로젝트 base/Overlay 전체 Commit과 조건을 받아 lab Argo 검증을 수행한다. 지정 Context/Namespace·공유 Operator 책임, 이미지/Secret 참조, Sync/SelfHeal·권한·삭제 보호와 필요한 관측 항목을 확인한다.

검증 Commit·이미지·환경 조건·결과·남은 제약을 정태훈에게 직접 인계한다. 이후 Source 변경은 영향 범위 재검증으로 연결한다.

실제 Build 대상 App/base Source를 받아 Build/Test/Scan 결과에 Source 커밋·플랫폼·Digest와 ECR/Harbor 대응 관계를 남긴다. Foundation Registry/CI 선언은 이유빈에게 넘겨 같은 Root/State에 통합한다.

### 6.3 ROSA 시험·측정·비용과 결과 Index

ROSA 통합·최종시험은 자원별 실행 담당자와 조율한다. 정상 Baseline 이후 분리된 장애·복구 Case와 부하를 순서대로 실행하고 같은 환경의 충돌을 피한다.

ECR 검증 일정에는 신규 Worker/캐시 없는 Pull, 12시간 이상 지속 사용 후 새 Pull, 재생성 후 Pull에 필요한 실제 시간을 반영한다. Build나 한 번의 Pull 성공으로 모든 조건의 Acceptance를 대신하지 않는다.

Harness와 지표·집계 정의를 반복 실행·비교가 가능한 수준으로 고정한다. 각 담당자가 실제 Run 결과를 작성하고 최유준은 Index·형식을 연결·확인한다. 발표 후보는 원본 Run 링크와 간략한 판정·주장 범위만 Docs Issue #6에 연결한다. 1차 재측정은 측정 정의 고정 뒤 필요한 비교 항목만 검토한다.

네 사람의 실제 가용시간과 자원 입력을 받아 가격·Credit·누적/잔존 비용, ROSA 가동·생성/삭제 대기·재시험·정리 시간을 집계한다. $450 계획선 초과 시 신규 가동을 보류·조정하고 총 $500 한도 내 실행 창을 확인한다. 자원별 보존·삭제 범위와 후속 청구 책임도 연결한다.

### 6.4 직접 인계할 내용

| 수신자 | 인계 내용 |
| --- | --- |
| 정태훈 | 배포 이미지·Digest/플랫폼·Scan 결과, 실제 base lab 결과와 조건 |
| 김상희 | Recovery 이미지·검증 정보, 복구 시험의 측정·결과 연결 조건 |
| 이유빈 | Foundation Registry/CI 권한 선언, 자원·수명·비용 입력 |
| 각 시험 실행 담당자 | Case·Source/환경 조합·실행 창·측정 정의·결과 제출/재시험 조건 |

현재 Source·필요 입력은 해당 Issue/PR, 공동 상태는 WORK_TRACKER와 Docs Issue #8에 연결한다.

확인 문서: [05 최유준 담당](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/05_IMPLEMENTATION_AND_VALIDATION.md#최유준), [04 base와 ocp-lab 인계](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/design/04_IMPLEMENTATION_READINESS.md#3-base와-ocp-lab-인계), [Run 기록 안내](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/evidence/README.md), [발표 후보 Issue #6](https://github.com/seokpan/seokpan-hybrid-docs/issues/6).

[담당별 바로가기](#role-navigation) · [목차](#contents)

<a id="document-records"></a>
## 7. 문서 변경·공유·수신 기록 원칙

이 문서는 execution/의 협업 안내·역할 배정 참조 기록으로 유지한다. evidence/에는 실제 Run 증거를 기록하며 이 안내에 test-id/run-id 또는 Runtime PASS를 부여하지 않는다. 역할별 최종본을 별도 네 파일로 중복 관리하지 않고 이 파일의 담당별 링크를 공유한다.

저장소 기록은 문서 개정의 Issue/PR/Commit 이력으로 남긴다. 실제 팀 전달·열람·개인별 작업 확인은 사실이 확인된 경우에만 해당 작업 Issue와 인계 기록에 남긴다. 확인 전에는 전달 완료·수신 완료·팀 합의 완료를 기록하지 않는다.

각 담당자는 기존 작업 Issue에 Source·입력·결과를 기록하고 수신자는 같은 기록에서 확인한다. Docs Issue #8은 대표 링크와 인계 상태를 연결한다. 이 문서 하단에 별도 개인 확인 표를 만들어 진행표와 중복 관리하지 않는다.

역할·운영 기준 변경 시 관련 승인 근거와 영향부터 확인하고 이 안내를 갱신한다. 일상 진행은 WORK_TRACKER·05·원본 작업 기록에서 관리한다. 문서 수정은 최신 main을 기준으로 Branch/PR에서 검토하고 다른 담당자의 기록과 충돌을 확인한다.

<a id="terms"></a>
## 8. 주요 용어

| 용어 | 이 문서에서의 의미 |
| --- | --- |
| OCP | OpenShift Container Platform. 프로젝트의 실습·사전검증 환경 |
| ROSA Classic Multi-AZ | Red Hat OpenShift Service on AWS의 채택된 최종 Cloud 플랫폼과 다중 가용영역 배치 |
| Root / State | Terraform 실행 단위와 관리 상태. bootstrap·foundation·rosa의 기존 분리를 유지 |
| Plan / Apply / Destroy | Terraform의 변경 계획 검토 / 실제 적용 / 지정 범위 삭제 |
| Caller / Context·Namespace | 실제 AWS 호출 주체 / 실제 Cluster와 논리 작업 공간의 실행 대상 |
| Seed / Source SHA | 이관 직전 고정한 검증 Source / 전체 Git 커밋 식별자 |
| base / Overlay | 공통 배포 선언 / 환경별 차이를 적용하는 설정 |
| CI / GitOps | Build·Test 등 통합 자동화 / Git 선언을 기준으로 배포 상태를 관리하는 방식 |
| Image Digest / Registry | 실제 이미지의 불변 식별자 / 이미지 보관·배포 저장소 |
| SCC / UWM | OpenShift 실행 보안 제약 / 사용자 Workload 관측 기능 |
| Release / Bundle | 검증할 Source·이미지·설정 조합 / 복구에 사전 확보한 자료·도구 묶음 |
| Run / Evidence Index | 특정 조건의 실제 실행 기록 / 원본 실행 결과를 찾는 색인 |
| Harness | 반복 시험·측정·결과 수집에 사용하는 실행 도구 |
| Gate / Blocker | 해당 실행 전에 확인할 조건 / 해당 후속 작업을 직접 막는 제약 |
| Window A / B | ROSA 정상 통합 / 최종검증을 위한 가동 구간 |
| RTO / RPO | 장애 시작부터 업무·데이터 복구 확인까지의 시간 / 사고 시각과 사용 Backup 데이터 기준 시각의 차이 |

<a id="references-and-review"></a>
## 9. 근거 문서와 검토 결과

### 9.1 근거 문서

| 근거 | 확인할 내용 |
| --- | --- |
| [01 Project Charter](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/design/01_PROJECT_CHARTER.md) | 프로젝트 목적·기간·비용·성공 축 |
| [02 Target Architecture](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/design/02_TARGET_ARCHITECTURE.md) | Cloud Primary와 On-Prem Restore-based Recovery |
| [03 Detailed Design](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/design/03_DETAILED_DESIGN.md) | 공식 Test/Acceptance, Source 이력·Ownership·Offline·WBS/비용 |
| [04 Implementation Readiness](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/design/04_IMPLEMENTATION_READINESS.md) | §2.2 역할, §3 base/lab, §6 시작 조건, §9 일정, §10 인계·Run·비용 |
| [05 Implementation and Validation](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/05_IMPLEMENTATION_AND_VALIDATION.md) | §0.4 순서, §0.5 환경, §0.6 일정, §0.7 증거/발표, §0.8 정리, 담당별 첫 작업 |
| [WORK_TRACKER](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/WORK_TRACKER.md) | 현재 관측·계정 매핑·작업/입력/공유 실행·수신 상태 |
| [HANDOFF_TEMPLATE](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/HANDOFF_TEMPLATE.md) | 제공자·수신자의 실제 인계 기록 |
| [Evidence 안내](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/evidence/README.md) | 실제 Run의 기록·판정·보호·Index |
| [Presentation Baseline](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/presentation/PRESENTATION_BASELINE.md) | 발표 선별·비교·주장 범위 |

작성 시 대조한 Docs 기준 개정은 [b70e4bf9199b7e400b21695ecfaaa53d47ebdbdc](https://github.com/seokpan/seokpan-hybrid-docs/commit/b70e4bf9199b7e400b21695ecfaaa53d47ebdbdc)다. 위 main 링크는 최신 문서 확인용이며 작성 당시 기록은 기준 개정과 확인 시각으로 구분한다.

### 9.2 연쇄 검토와 보완

공통·개인별 실행 안내를 역할 → Source·입력 → 수신자 → 공유 실행 → 환경 전환 → 시험·재시험 → 비용·정리 → 기록 위치 순서로 대조하고, 수정한 내용의 직접·후속 영향을 다시 검토했다.

| 검토 영역 | 최종 반영 내용 |
| --- | --- |
| 독립 문서·출처 | 제목·메타데이터·목차, 객관적 담당자 표현, 기존 배정 근거·현황 시각과 전달 미확인 상태 |
| 역할·협업 | Root 실행자, Foundation 담당 선언의 통합, 직접 인계, 담당자와 실제 수행자 구분 |
| Source·기여 | 실제 이관 직전 Seed 고정과 Git 이력 보존, 1차 상속과 2차 변경 구분 |
| 환경·일정 | OCP 예제/실제 base/ROSA 판정 구분, 조건별 진입·병렬 준비, 후보 날짜와 실제 가동 확정 |
| Plan·관리 인계 | 실제 Plan 작성과 검토 후 Apply의 시작 조건 분리, 정상/비상 접속·초기 인증/세션 회수와 관리 인계 |
| 비용·삭제 | $450 초과 시 신규 가동 보류, 전체 비용 구성, rosa와 foundation/bootstrap 삭제 범위 구분 |
| Offline·측정 | 실제 조합·장애 조건의 로컬 최종검증, 외부 신규 조회 범위, RTO/RPO 기준, 실제 Pull 시험 시간 |
| 기록·발표 | Issue #6/#8 역할, Run 정본·실패/재시험, 협업 기록과 Runtime Evidence 구분 |
| 이동·참조 | 상단 목차, 공통 안내 하단 네 사람 바로가기, 각 담당 절의 복귀 링크와 근거 링크 |

| 검토 단계 | 결과 |
| --- | --- |
| 1차 기준 대조 | 기존 안내를 승인 기준과 대조하고 독립 문서·비용/삭제·Seed·Offline·측정 경계를 보완 |
| 2차 통합본 재검토 | Plan/Apply 조건의 혼합과 관리 인증 인계 누락 2건을 발견해 수정 |
| 3차 정정 후 내용 재검증 | 수정 부분과 공통 실행·인계·비용·복구·삭제의 후속 영향을 다시 확인. 추가 필수 보완·변경 0건 |
| 최종 구조·참조 검증 | 제목·메타데이터·목차 순서, 네 사람 이동·복귀 링크, 문서 경로·절 참조·표 구조 검사 통과 |

**최종 재검증 상태:** 확인한 기준 개정과 문서 정합 범위에서 추가 필수 보완·변경 0건으로 수렴해 재귀 검토를 종료했다.

검토 대상은 이 안내의 내용·참조·형식 정합성이다. 실제 구현·계정/환경·Plan·비용·Runtime 시험은 해당 작업의 입력과 실제 결과로 계속 확인한다.

[목차로 돌아가기](#contents)

