# 정태훈 실행판 — 완료 근거와 실제 잔여

## 정태훈 담당 완료 결과 — 2026-10-20 KST

아래는 기존 실행·원 기록으로 확인한 완료 범위다. Source·Plan·Apply·실제 통신·업무 수락을 구분한다.

| 구분 | 완료 결과 | 근거·한계 |
| --- | --- | --- |
| ROSA 설치·정상 관리 | 기존 설치9/9 Ready·Operator34, Data Binding2개·Native FE/BE×Compute3 실행6/6, Cloud 보호 입력/TLS·Argo 허용/거부·정상 관리 | [Infra25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25). 당시 환경 결과이며 새 클러스터·Cloud 업무 완료가 아님 |
| ROSA 중간 삭제·보존 | Root State 자원 제거, 옛 소유 태그 EC2/ENI/LB/EBS 잔존0·조회 오류0, Snapshot4·독립 해독 자료6개 보존 | [실제 결과](https://github.com/seokpan/seokpan-hybrid-infra/issues/25#issuecomment-6236061743). untagged/shared 전체 부재·청구0·새 재생성/E2E·최종 종료를 뜻하지 않음 |
| NAT·EIP·기본 경로 | A(이유빈)의 NAT3·전용 EIP3·ROSA 기본 경로3 재생성. 10/20 10:56:44~10:58:32 KST Apply exit0/add9, 11:02:11 KST NAT available·EIP 연결·동일AZ 경로 active 확인 | [Infra23](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-6281612432). Source `81c648247c47fe2232b81678445e57806c2bbdbf`, Plan add9/change0/delete0/replace0. B 실행이나 새 ROSA 외부 통신 결과로 확대하지 않음 |
| RDS Start | A(이유빈)의 10/20 11:10:56 Start, 11:21:02 KST available 확인·기존 Endpoint 일치 | [Infra45](https://github.com/seokpan/seokpan-hybrid-infra/issues/45#issuecomment-6281899697). 로그인/TLS·데이터·백업 재개·앱 기동은 미검증 |
| 실행 도구·Controller 반영 | Infra90 병합 `ace9511`, Infra91 병합 `041d01a`, 기존 Controller 소스 반영·보호 입력 처리·제한 결과 전달·발생기 연결 완료 | [Infra90](https://github.com/seokpan/seokpan-hybrid-infra/pull/90)·[Infra91](https://github.com/seokpan/seokpan-hybrid-infra/pull/91)·[91 CI](https://github.com/seokpan/seokpan-hybrid-infra/actions/runs/39348811154). CI/도구 준비를 SQL·새 생성·앱/측정 성공으로 쓰지 않음 |
| Recovery Valkey·CNI/Pull | 보호5객체/Harbor 공급·Valkey1 Ready/재시작0·UID999/파일·port-forward TLS/AUTH, 뒤 r2 TCP6379 허용6/차단6·worker01 Valkey fresh Pull | [GitOps10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10#issuecomment-6213554272). worker02는 cache. 다른 포트/FE·BE 이미지/노드·노드CA 인과·전체 복구로 확대하지 않음 |
| Recovery 계정·권한 | A(이유빈)의 6계정·REQUIRE SSL·업무 권한과 game_svc.member 최소 컬럼 SELECT/UPDATE6행 확인 | [Infra48](https://github.com/seokpan/seokpan-hybrid-infra/issues/48#issuecomment-6261703688). global Grant_priv=N 확인과 DB/table 수준 GrantOption 부재 검증은 별개. 실제 Job 출발지/TLS/current·업무 미검증 |
| 선택 모니터링 | 고정 개정 Sync/Healthy·3객체/규칙3개 로드·smoke firing/정리 | [T15 원 결과](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/evidence/T15/monitoring-gitops-sync-20261016-01/summary.md). Deployment PARTIAL/Acceptance NOT RUN. 앱 metrics·target UP·실제 알림·시험 리뷰 수락은 별도 |

[Docs21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21)의 TH 원81개·현재37완료/44미완료를 유지한다. 정상 관리·중간 삭제·도구 준비 등 부분 성공으로 복합 체크를 완료하지 않는다.

### 현재 미완료 조건

| 담당 | 실제 잔여 | 적용 단계 |
| --- | --- | --- |
| B 정태훈 | 수신한 NAT 활성 입력/proof의 생성 config/readiness 결합, 현재 비용·가동/종료 창, 새 테스트 데이터 앱을 위한 non-import 경로 보완 | 실제 재생성·앱 실행 전. 기존 Import/Writer 성공값을 임의로 채우지 않음 |
| A 이유빈·B 정태훈 | 실제 목적 계정/Grant/TLS/매칭 Host·Schema 준비·목적 SQL/current·운영 Pool/앱, 전역 PROCESS 근거 또는 기존 관리자 관측 경로와 실제 한도/예약 | RDS Start 완료와 구분. Migration current는 Schema 생성 명령이 아님 |
| D 최유준·B 정태훈 | 새 환경 target/query·선정 메일 실수신·선정 정상/롤링·별도 HPA 결과 | 기존 receiver/발생기/관측 준비 재요구 없음. SMTP 보호 원본은 메일 시험 선정 시만 |
| 각 자원·보관 담당 | 비상 접근/회수·Cloud 독립 보관 책임, 최종 N/Release/Retention, 운영 Recovery 사본/신규 진입·전체 업무/RTO/RPO, 최종 보존/삭제/청구·발표 | 각 원 정의의 잔여로 유지 |

현재 Cloud는 새 테스트 데이터 경로의 실제 앱·SQL·Schema·운영 Pool이 미완료다. 원본 Writer 중지·PR156·GO/최종 Dump/Import·VPN은 별도 이관을 선정할 때의 조건이며 현재 앱의 공통 선행으로 붙이지 않는다. [1차155](https://github.com/seokpan/seokpan-gitops/issues/155)·[PR156](https://github.com/seokpan/seokpan-gitops/pull/156)은 내용 승인·blocked/open·미병합 상태다. 실제 중지/Sync·Pod/Endpoint/Job/Argo 종료·GO/덤프는 미실행이며, Cloud 새 쓰기 뒤 단순 원본 재개·자동 DB rollback은 하지 않는다.

NAT 활성 입력을 사용하고 옛 비활성 입력·삭제 전 State/destroy Plan·옛 API/Token/UID를 재사용하지 않는다. Foundation 사후 전체 재계획·옛 Worker/State 두 규칙 metadata·실제 사용 Plan 리뷰/최종 hash는 별도 잔여이며 기록용 재실행·사전 승인 소급 작성으로 채우지 않는다. ROSA 재생성은 보류 상태다.

비용은 [10/19 원장](https://github.com/seokpan/seokpan-hybrid-docs/issues/43#issuecomment-6258569496)의 청구352.31달러/추정355~358달러가 마지막 공개 보고다. 오늘 청구·잔여예산은 미확인이고 $450 계획/$500 한도·PARTIAL을 유지한다. 새 NAT/EIP 가동·RDS Start 구간을 비용에 반영하며 NAT 정리 후 유휴0.10달러/시간 추정을 현재 활성 시나리오에 적용하지 않는다. 12:20~14:20 KST A/B 부재 예정은 가동·상태 보존·재개 창에 포함한다.

완료한 설치/Pull/TLS/로그인/smoke/UI/Source·CI/Preview/CNI·보존/해독·삭제/잔존·독립 예행·Controller 준비/진단을 반복하지 않는다. 다음 새 삭제는 보존·의존성 확인과 별도 실행 결정 후 진행한다. Recovery Valkey1/template을 보존하고 held0 전체 선언을 그대로 적용하지 않는다.

## 원 정의·이력

TH-01~19의81개 원 정의와 체크는 [Docs21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21)에 유지한다. 세부 영역은 [App4](https://github.com/seokpan/seokpan-hybrid-app/issues/4)·[Infra25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25)·[GitOps10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10),완료 결과는 [완결 작업 결과](TJUNG03_COMPLETED_RESULTS_20261016.md)로 연결한다. 날짜별 Source/실행 기록은 각 원 이슈/PR의 개정과 수행자를 기준으로 사용한다.

[10/16 실행판](https://github.com/seokpan/seokpan-hybrid-docs/blob/276818cc2468af99716f770dad4b9e353011f486/execution/TJUNG03_EXECUTION_BOARD.md)은 당시 이력이다. 과거36/45·설치/삭제 전 대기를 현재 상태로 재사용하지 않는다.
