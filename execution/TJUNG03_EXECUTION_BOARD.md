# 정태훈 실행판 — 지금 할 일·입력 대기·OCP와 ROSA 수명

현재 추가 수신: D의 Run #5 OCI 복사·bastion 반입/Registry·Worker requests 보고, A PR #54 B 승인·병합 대기를 [새 공급 후속](OCP_RUN5_SUPPLY_FOLLOWUP_20261009.md)에 연결했다. 실제 push·내부 mapping·Pull·교체나 ARN/SG 인계 완료를 뜻하지 않는다. Controller의 격리 오프라인 시험은 Linux 파일3건·SG/Plan10·OCP계산5 PASS를 수신했고 임시 사본 제거·설치 없음으로 마쳤다.

> **현재 확인 — 2026-10-09:** EC2 JSON 전달 오류는 로컬 `ParamValidation`으로 확인했고 정규 임시 파일 교정 후 기존 Controller의 제한 읽기2회가 성공했다. [교정 부분 Run](../evidence/T03/controller-seoul-ec2-input-corrected-20261009-01/summary.md)에서 조회 조건의 인스턴스0·예약0과 미확인 범위를 구분한다. 이 오류에 대한 A IAM 변경 요청/진단 반복은 필요 없다. 프로젝트 AWS 계정 ID·공통 Role/정책·ROSA 작업용 권한/State 저장소·SG2·지원/Quota·비용/사용창 입력은 계속 대기한다. [B 선행 검사·requests 계산](B_OFFLINE_PREPARATION_REVIEW_20261009.md)을 준비했고, 새 Image는 App18819963/Run #5/#32 수락 기준이다. 실제 전체 Plan·OCP 공급/교체·Pool·이관·Recovery는 각 조건 뒤 수행한다. 아래 이전 날짜의 안내는 당시 이력이다.


> **현재 확인 — 2026-10-08 Docs #95 병합 후:** [병합·Controller 인증·실행 대기](MERGED_SOURCE_PLAN_READINESS_20261008.md). App30/34·GitOps33 승인·병합·PR 브랜치 삭제 완료. App18819963의 D Run5 성공 보고·FE/BE Harbor 공급 후보 수락, B/jth의 Source/Lock·기본 Caller/MFA·서울 사양/Quota 부분 결과 유지. EC2 진단v1/v2는 코드 비식별·사용량 미확보·원인 미확정으로 자동 API 재시도 종료, B 현장/A 계정 Owner 비공개 확인 입력 대기. 실제 역할/SG2·목적 세션/Backend·프로젝트 조직/지원·EBS 기준/비용 입력·전체 Plan, 내부 공급/Pull·Runtime은 별도 미완료. 아래 날짜별 기록은 당시 이력.

> **최신 조사 후속 — 2026-10-07:** [전수 조사](REPOSITORY_AUDIT_20261007.md)·[05§9.47](05_IMPLEMENTATION_AND_VALIDATION.md#repository-full-audit-20261007) 참조. GitOps main의 Root SHA B/FE·BE1은 소스 병합 상태이며, 마지막 수신 Runtime은 SHA A/FE·BE0이다. 성공한 등록/선택Sync·금고 본체 확인을 반복하지 않는다. C의 GitOps26/6038214247 DB 형식·GRANT·TLS 접속·합성 출처 수락 보고는 수신했고 실제 Stage2 적용·Route/업무는 원 #26에서 후속 확인한다. 아래 시점별 인계 보존.

### 조사 중 추가된 실행 보고·수정 PR — 2026-10-07 후속 조회

[D 등록·선택 Sync 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5#issuecomment-6034601393)는 SHA A의 Valkey 4객체 `Succeeded`·FE/BE 미생성을, [Pod 확인](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6#issuecomment-6034590906)은 검토 Digest의 amd64 하위 ImageID·허용 UID만 보고했다. 등록/Sync를 다시 미실행으로 되돌리지 않는다. 실제 TLS/AUTH/Hostname·Ready 전체 Run과 Prune/Delete 차단은 아직 근거가 없으며 공유 Owner 재확인·등록 Commit·B 공유 시각의 빈칸 및 사전 합의되지 않은 `oc patch operation.sync.resources` 경로는 원 #5에서 보완·수락한다. #21의 완료 체크만으로 이 잔여를 완료 처리하지 않는다. 이 조사자는 클러스터를 직접 재조회하지 않았다.

[GitOps #25](https://github.com/seokpan/seokpan-hybrid-gitops/pull/25)은 A 새 승인 후 `61edd0fd60e1004260c0b5082dc792fce847616b`에 병합·원격 PR 브랜치 삭제, 병합 validate success를 확인했다. checker 정책 #27과 회귀/안내2파일 보완 종료. 현재 Root는 SHA B `bfee2669e62bf823969ce224e5599eccace5d024`이며 최신 병합 main의 등록 비교/전체 lab release Gate는 Source PASS, 실제 적용/Sync/보호는 원 #5/#26의 별도 수락이다. 이전53314d3/69PASS·재리뷰 요청은 당시 근거로 보존.

[Infra #43](https://github.com/seokpan/seokpan-hybrid-infra/pull/43)은 `6849c32d5b24a0e4994b7fbe849a1032211dc9a3` 병합·원격 PR 브랜치 삭제와 validate success를 확인했다. default State Key 유지, Workspace prefix/List 범위 정합 보완 완료. 기존 초기화/Workspace/State 위치 확인 뒤 목적 Caller/Backend·지원·A 기반/C SG2·예비 비용/창을 수락해 첫 Plan으로 진행한다. 병합 Source의 오프라인 fmt/helper/harness 보존 PASS와 실제 Controller/Cloud Plan NOT RUN을 구분.

[GitOps #26](https://github.com/seokpan/seokpan-hybrid-gitops/issues/26#issuecomment-6050000112)의 D 최신 로그인·방 생성/접속·게임 종료·업무 영향 없음 보고와 C6038214247의 DB 형식/GRANT/TLS 접속·합성 출처 수락을 수신했다. Vote 미확인·Valkey ERR 증가 원인 조사는 후속. 정확한 실제 Source/Image/Run·Route/Origin·TLS/Hostname·Ready·Owner/사용창/Gate/live Diff·삭제 보호 수락은 별도로 남으며 직접 Runtime 재조회·전체 PASS로 사용하지 않는다.

첫 읽기·작업 위치·실행 조건은 [실행 인계](EXECUTION_ENTRYPOINT_20261007.md)를 따른다. 원 보고와 이 Source 수정의 수신/검토·실행은 별개다.


## 현재 실행 기준 — 2026-10-07 원격 변경 대조·구현 인계

| 경로 | 완료·수신 범위 | 직접 남은 조건 |
|---|---|---|
| App #17/#18/#19 | 최신 D 재승인 후 모두 squash 병합·작업 브랜치 삭제. 결합 main `a2afffb8605dafff1cb5b9af215aa0cf93aadcdb`의 기존 정식 CI에서 Backend1762·부분집합runner47·별도Lua9 PASS, dirty=false | [App2 Build 인계](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-6033610765) → D의 같은 Source Build/Scan·새 Backend Digest/플랫폼·Registry/Pull → B의 App/별도 held Migration 소비 검토. 기존 승인 Digest가 세 수정을 포함한다고 승계하지 않음 |
| GitOps #20 | 검토 HEAD `b13ae9575206a335a9e6f87efc34dd4c198884f7`의 metadata allowlist·58PASS 후 재승인 수신, `5dc2bd546de1acbbeb47a380c85103ce2b31017f` 병합·작업 브랜치 삭제 | 재리뷰/병합 대기는 해소. Controller 등록 checker와 Stage-1 Gate·실제 등록/보호 동작은 별도 |
| GitOps #22/#24 | Stage-1 Source SHA A=`244b48b885d7ac645c402e561a032ae65a8f3461`, 등록 Source=`a25172c7453b9d7999cb1f3cbeb1ef35774e3b63` 병합. #24의 `targetRevision`은 SHA A를 고정 | D의 실제 등록·Valkey 4객체 선택 Sync 성공 보고 수신. Owner 재확인/등록 Commit/공유 시각·Gate/live Diff 근거 보완, TLS/AUTH/Hostname·삭제 보호·Ready 전체 Run과 B 수락은 별도 |
| Infra #40/#42 | #40=`a0da58c345f877659e522a5b4ab5392b1d0626d3`, #42=`36dc2403aa77e2896cc4ec3c545b92e0afb49205` 병합. #42는 일반 사본 `periodic/`와 `backup_periodic_retention_days`로 정합화 | A의 기존 tfvars/변수 소비·Root Plan, C의 Job/권한/Lifecycle·대장 개정 수락과 실제 Backup은 별도. 운영 Data/Valkey/전체 T18 완료 아님 |
| Docs #69/#72/#77 | #69 보존 브랜치는 후속 작업에 사용하지 않음. #72는 기존 HEAD `376afcb03849e2325c5a10e80a363081bb0cd2de` 이후의현재 상태를 보완하는 리뷰 PR. [#77](https://github.com/seokpan/seokpan-hybrid-docs/pull/77)의 C Data 공급 보고는 `a9b0207b563aa25be17d4a635f6cc903fbe0e74a`에 병합 | #72 최신 main 정상 결합·재리뷰/병합. #77의 공급·확인 보고를 새 Runtime 재조회나 Foundation Apply·SQL 계정 생성으로 확대하지 않음. C의 05 §8.15·Tracker 기록 보존 |
| Cloud 금고 | [C Valkey 해독/형식/암호문 해시 보고](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6028766924)·[B 수신](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6028919355), [B SQL 금고 jth 확인](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6033157659)·[C의 세 계정 확인](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6033174437) 완료 보고 | Controller 밖 독립 키/암호문 사본·복원한 identity로 해독 확인만 별도. 이 문서 작성 환경의 직접 복호화 결과가 아님. 완료한 공개키 전달·본체 해독을 반복하지 않음 |
| 개인 clone·ROSA·Cost | clone의 경로/필수파일 검사 중단 이력, CP3/Infrastructure3/Worker3와 원장(3)의 PARTIAL·미완19·입력오류0·기타미확인4 유지 | [직접 실행 안내](TJUNG03_WORKFLOW_AND_LEARNING_GUIDE.md#b-direct-actions-20261007)의 현재 첨부/실파일 구분과 Infra 정본 LOCAL_PREPARATION의 읽기 중심 준비 → 본인 도구/Caller/Backend·지원·실제 사양/시간·A 제한 출력/prerequisite·C SG2. disk300 등 임의 입력 금지, $450/$500 유지 |

Stage-1 작성/리뷰는 끝난 Source를 재사용한다. SHA A의 lab 선언은 Valkey만 replicas1/`source-reviewed-runtime-unverified`, FE/BE는0/`input-required`, Migration은 suspend/current/300초·단일 실행이다. base/Recovery hold와 기존 전체 `release-manifest`를 보존하고, 별도 Valkey Stage-1 Preflight Gate가 지정한 리소스/입력·보호 범위를 확인한 뒤 선택 수동 Sync한다. #20의 등록 checker를 Stage-1 Gate로 대신하지 않는다.

#24의 등록 Source는 기존 `openshift-gitops` Controller와 제한 AppProject/Application 각1개, destination=`seokpan-argotest`, path=`apps/overlays/lab`, targetRevision=SHA A다. D의 등록·Valkey 선택 Sync 보고 이후 남은 범위는 상단 추가 보고의 근거 보완·실제 Service/Ready/TLS/AUTH/Hostname·삭제 보호 판정이다. DB/Secret/CA/Route와 새 Backend Image를 수락한 Stage2는 별도 FE/BE 활성화 SHA B → 등록 targetRevision 갱신/검토·지정 apply → 기존 전체 Gate 정상 통과 → 필요한 단일 Migration·FE/BE 수동 Sync → 같은 조합 업무 Run으로 이어진다. Source 병합·등록·Synced·Valkey Ready·전체 lab/ROSA/Cost PASS를 분리한다.

[Docs #74](https://github.com/seokpan/seokpan-hybrid-docs/pull/74)/#75의 `periodic/` 결정·과거 `hourly/` 구분과 C의 05/Tracker 기록은 보존한다. Infra #42의 Source 병합 대기는 해소됐지만 실제 tfvars·Plan/Apply·백업 수락은 [work W09](WORK_HANDOFF_20261007.md)에서 확인한다. 03·04 설계 종료, DR10분/영속 DB RPO30분/DB 운영 중15분 계획 주기를 유지한다.

[원 GitOps5 결정](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5#issuecomment-6032629690)·[Cost43 대조](https://github.com/seokpan/seokpan-hybrid-docs/issues/43#issuecomment-6033030041)·[Source 현재 대조](SOURCE_REVIEW_20261007.md#b-work-current-delta-20261007)·[대장 현재 대조](REPOSITORY_CONSISTENCY_AUDIT.md#b-work-current-delta-audit-20261007)·[work 인계](WORK_HANDOFF_20261007.md)를 따른다. 아래 과거 관측·실패·Run·리뷰는 해당 시점의 이력이다. TH81/실제 완료2·기존 Q 체크는 변경하지 않으며 Q02/03/04/05/10과 실제 개인/공유 실행·전체 목표 판정은 별도다.

## 먼저 열 이슈와 기록 순서

**개인 출발점은 [h-docs Issue #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21)입니다.** TH01~19의 81개 체크와 완료 2개를 유지하며, 상단 현재 안내 → 저장소별 실행 카드 → 원 PR/Run → 제출/수신 → 상위 TH 확인 순으로 읽습니다. 이전 본문은 접어 보존하고 체크 정본을 복제하지 않습니다. Native Sub-issues는 등록되지 않았으며 기존 본문 양방향 링크 구조입니다.

| 찾을 일 | 주 기록 위치 |
| --- | --- |
| 지금 첫 OCP 선언·입력표·Render·Case, Cloud/Recovery·Bundle | [h-gitops Issue #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10) |
| Client 계약·DB/Redis 접속·실제 Client 검사 | [h-app Issue #1](https://github.com/seokpan/seokpan-hybrid-app/issues/1) |
| App 경로·업무 안전·Build 인계·TH17 App/Pool | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) |
| D CI·새 Image와 B 리뷰/수신 | [h-app Issue #2](https://github.com/seokpan/seokpan-hybrid-app/issues/2) |
| D 실제 OCP Sync/보호·Client/업무와 B 수신 | [h-gitops Issue #5](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5)·[h-gitops Issue #6](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6) |
| ROSA 준비/실제 Plan·Window A/B·TH17 ROSA/SG·최종 정리 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) |
| 발표·시연 증거 | [h-docs Issue #6](https://github.com/seokpan/seokpan-hybrid-docs/issues/6) |
| 팀 입력/공유 실행 조정·현행 기록 연결 | [h-docs Issue #8](https://github.com/seokpan/seokpan-hybrid-docs/issues/8)·[Tracker](WORK_TRACKER.md)·[05](05_IMPLEMENTATION_AND_VALIDATION.md) |

TH17은 App4의 App/Pool, GitOps10의 선언/관측, Infra25의 ROSA/SG/재생성에 **같은 실제 Run을 연결**합니다. TH04/05와 TH07.2의 Client 원본은 App1입니다. 결과를 각 원본에 먼저 기록하고 개인 체크는 Docs21, 공식 T/Must·팀 종료는 실제 Run/Index와 05의 수락으로 별도 확인합니다.

막힌 실행은 필요한 입력/개정·공급 Issue/담당·제출/수신/보완·다음 확인 시점·지금 계속할 준비를 남깁니다. 한 PR의 Source 병합이 전체 Runtime 범위 완료를 뜻하지 않으면 `Refs`로 연결해 자동 종료를 피합니다. 문서 현행화와 실제 Run/PASS·다른 담당의 수신은 구분합니다.

이슈 추적 경로와 실행 안내의 검토 결과는 [05 §9.24](05_IMPLEMENTATION_AND_VALIDATION.md#b-issue-navigation-audit-20261005)에 기록합니다. 기존 범위에서 B의 마지막 정리까지 연결되어 있어 새 중복 이슈는 만들지 않았습니다.


## 1 전체 작업 진행 현황과 B의 현재 위치

- [x] 승인 설계·DR10분/30분/15분 반영, 00 역사/01~04 기준 유지
- [x] [h-docs PR #33](https://github.com/seokpan/seokpan-hybrid-docs/pull/33) main b45ea2d 병합·해당 Branch 삭제 확인
- [x] App [h-app PR #5](https://github.com/seokpan/seokpan-hybrid-app/pull/5) 병합, GitOps/ROSA 후보 Source 검사, 두 합성 부분 예행과 [h-infra PR #29](https://github.com/seokpan/seokpan-hybrid-infra/pull/29) 도구 병합
- [x] [h-docs PR #34](https://github.com/seokpan/seokpan-hybrid-docs/pull/34) main `efb07db36c140d77702fe5e2854d6d44df0af198` 병합·해당 브랜치 삭제 확인
- [x] 네 저장소의 기존 실행 이슈 10개 탐색 보완과 TH81/기존 완료2·원 기록/메타데이터 보존
- [x] [h-docs PR #35](https://github.com/seokpan/seokpan-hybrid-docs/pull/35) 병합·해당 브랜치 삭제 확인, OCP 최초 제어·인계 Source와 ROSA 리뷰/실행 안내 게시
- [x] [h-docs PR #36](https://github.com/seokpan/seokpan-hybrid-docs/pull/36) main `d5ead4600c7e819141c1d8213c760cc693f3c238` 병합·해당 브랜치 삭제 확인, D의 이전 HEAD Source 승인·비차단 제안 접수
- [x] [h-docs PR #37](https://github.com/seokpan/seokpan-hybrid-docs/pull/37) main `198996c32b02985578e339b514d38155ec17cff8` 병합·해당 브랜치 삭제 확인, GitOps #9 최신 HEAD에 대한 C Source 승인 수신
- [ ] B 남은 선언/검사·실제 Image/입력·OCP 새 조합 수락
- [ ] A/C/D 실제 기반·Data·CI/Pull/비용과 B ROSA 실제 실행/통합
- [ ] 최종 시험·발표·삭제/잔존/보관·팀 종료

<details>
<summary>2026-10-05~06의 Source·비용·인계 관측 이력 — 현재 지시는 상단·§2~10</summary>

**B의 본인 환경 준비는 A 전체 업무 완료를 기다리지 않는다.** D Run3 Image 제공·B 개정 수락과 Lab/Recovery Source 승인·병합은 완료됐다. 다음 활성화·실행은 D/C의 최소 lab/Pull Secret/Data/Owner 입력 수락 뒤 진행하며, ROSA 실제 제한 Output/SG2·B 목적 Caller/Backend·비용 준비는 병행한다. OCP 정리는 별도이며 ROSA 시작의 일괄 조건으로 추가하지 않는다.

**현재 B 작업 묶음:** [D Run#3](https://github.com/seokpan/seokpan-hybrid-app/pull/10#issuecomment-6009053898) SUCCESS·Harbor-only·`linux/amd64` 보고와 FE/BE Final Index Digest를 [B 수락 답변](https://github.com/seokpan/seokpan-hybrid-app/pull/10#issuecomment-6009213599)에서 제공 개정으로 수락했다. App Source는 `46e21a74dd608b41f2c12a0a57d76bddfcf25949`, Final tag는 `git-46e21a74dd60`다. 초기 frontend Alpine 경고는 최신 D 스캔 정정으로 공급 대기에서 해소했다. Private Harbor 원본 metadata/bytes를 독립 조회로 검증한 것은 아니며 cp-03 Podman Pull/Smoke 보고도 OCP Workload Pull/Ready 판정과 구분한다. [GitOps PR #13](https://github.com/seokpan/seokpan-hybrid-gitops/pull/13)은 검토 HEAD `c798ed28d516533d5ffb984ad58332e3a5e5829d`의 [D 최신 승인](https://github.com/seokpan/seokpan-hybrid-gitops/pull/13#pullrequestreview-5424398322) 후 main `fc175a7002ad567e9d5206b6e4b6642e8416eea2`로 병합됐고 작업 브랜치 삭제를 확인했다. [Source CI #40](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37420661610)의 39개 검사 통과(skip0)는 기존 검증 결과이며 이번에 새 검사/실행을 추가하지 않았다. 이전 e757 승인 `DISMISSED`·c798 `blocked`/재검토 요청은 [보완 답변](https://github.com/seokpan/seokpan-hybrid-gitops/pull/13#issuecomment-6010256873) 당시 이력이고 현재 Source 승인·병합 대기는 해소됐다. [Docs #53](https://github.com/seokpan/seokpan-hybrid-docs/pull/53)도 main `17b601b1e4dc2db82efaf8e82df78a39ae9c1376`로 병합·브랜치 삭제됐다. Source 준비 완료와 실제 입력 공급·활성화·실행 수락은 별개다. Lab/Recovery FE·BE 및 held Migration에 제공된 Final Index Digest를 연결했고 Lab `lab-harbor-pull` 참조를 추가했다. Recovery `recovery-harbor-pull`은 유지한다. App replicas0·Migration suspend/current·기타 INPUT_REQUIRED·Cloud ECR 보류는 그대로다. Image 제공·개정 수락과 Source 승인·병합 대기는 해소됐다. B는 이제 D와 대상 Namespace의 실제 Pull Secret 공급·Context·권한·단일 Owner, C/D Data·CA/TLS/AUTH·Schema/필요 Migration 준비를 수락한다. 그 뒤 별도 활성화 개정·필요 단일 Migration·수동 Sync를 수행하며 해당 Job/Pod의 Workload Pull·Ready/FE/API/WSS/대표 업무 Case를 같은 조합으로 확인한다. 선언의 Digest/Secret 이름만으로 실제 실행을 완료 처리하지 않는다. ROSA 준비는 Infra25에서 병행한다. [05 §9.36](05_IMPLEMENTATION_AND_VALIDATION.md#b-image-receipt-held-source-pullsecret-20261006)·학습 안내 §5.8을 본다.

| 실제 위치/원본 | 이번 결과 | 직접 막힌 실행·다음 행동 |
| --- | --- | --- |
| App2/PR10 → GitOps10/5/6 | D Run3 SUCCESS·Final Digest·최신 Scan 보고 수신/B 개정 수락. Lab/Recovery held Source 연결 | Source 병합 완료. D Namespace Secret/Owner + C/D Data·Schema 준비 → B 활성화/수동 Sync → Workload Pull·Ready/Case |
| rosa 목적 Role 수요·Infra20/25 | PR35 A 재승인·병합, 정상 Get/조건부 Update 수요 확정 | 첫 Plan용 조회·State 정책/Caller·Backend·필수 Output/SG2/지원 수락 → 첫 Plan. 생성/Update/삭제 검증·조건부 ListTags 호출/미발생 기록은 해당 단계 |
| B Infra25 ↔ D Docs43 | 개정 xlsx 수신·60수식/18시나리오 독립 재계산. 미완19·미확인5·PARTIAL 유지 | D 남은 수식 보완·재검증 + B 비용 입력1~6 준비. 예상/실제 구분, 본인 가용성은 별도 미확인 |

**지금 확인할 결과:** Docs52·53 병합·브랜치 삭제, D Run3/Image·최종 스캔 정정 보고와 B 개정 수락을 확인했다. [GitOps PR #13](https://github.com/seokpan/seokpan-hybrid-gitops/pull/13)은 검토 HEAD `c798ed28d516533d5ffb984ad58332e3a5e5829d`의 [D 최신 승인](https://github.com/seokpan/seokpan-hybrid-gitops/pull/13#pullrequestreview-5424398322) 후 main `fc175a7002ad567e9d5206b6e4b6642e8416eea2`로 병합됐고 작업 브랜치 삭제를 확인했다. [Source CI #40](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37420661610)의 39개 검사 통과(skip0)는 기존 검증 결과이며 이번에 새 검사/실행을 추가하지 않았다. 이전 e757 승인 `DISMISSED`·c798 `blocked`/재검토 요청은 [보완 답변](https://github.com/seokpan/seokpan-hybrid-gitops/pull/13#issuecomment-6010256873) 당시 이력이고 현재 Source 승인·병합 대기는 해소됐다. [Docs #53](https://github.com/seokpan/seokpan-hybrid-docs/pull/53)도 main `17b601b1e4dc2db82efaf8e82df78a39ae9c1376`로 병합·브랜치 삭제됐다. Source 준비 완료와 실제 입력 공급·활성화·실행 수락은 별개다. 실제 OCP Workload Pull/Ready·Data/Migration/업무, Recovery Redis TLS/AUTH/Storage/임의 UID/T18, ROSA ECR·본인 Caller/Backend/Plan/Cost는 별도다. 기존 진단 자료/체크·C 기록은 유지한다.

**이번 비용 점검 — 내 일과 팀원 일:** [05 §9.37](05_IMPLEMENTATION_AND_VALIDATION.md#b-cost-ledger-independent-audit-20261006)에서 수식 근거를 보고 [B 실행 원본 Infra #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) → [D 비용 원본 Docs #43](https://github.com/seokpan/seokpan-hybrid-docs/issues/43)로 진행한다. 개정 원장의 B 입력은 **19~24행**이며 이전16~21행 안내는 구원장 이력이다.

| 구분 | 지금 할 일 | 직접 기다리는 것 |
| --- | --- | --- |
| **내 일 B** | 서비스 지원/예상 구성·Worker disk·LB/IPv4 견적 입력1~3, Window/재시험/삭제 예상4~5, 본인 가용성6 확인 | 실제 사양·시간은 미확인. 후보·예시를 확정으로 채우지 않음 |
| **팀원 D** | Docs43에서 미확인 글자/음수 검증, 최대시간의 비시간 비용, 합계·하한 표시 보완 | 이번 감사 답변을 반영한 개정 원장·전체 비용 판정 |
| **팀원 A/C** | A 실제 기반/공통 역할, C 실제 Data SG2 공급 | #33은 main2c17488 병합(062a371 리뷰 이력). 실제 출력 미수락, #36은 main a332d85 병합. A Network IAM 복구 Apply/정책·Role 연결·No changes 보고 수신. ROSA account-wide/Worker ECR 제외 |
| **생성 후 B/D** | 실제 목록·가동/삭제 완료·잔존으로 예측을 개정 | 생성 전 실제 목록을 요구하지 않으며 유료 생성은 Plan·비용·실행 창 수락 뒤 |

**핵심:** 기간 공란을0으로 계산하는 문제는 보완됐지만 전체 판정 수식에는 남은 문제가 있다. 현재 비용 PASS·유료 실행 허용으로 읽지 않는다. #33의 NAT 기본false와 운영 창의 NAT3/EIP3 기간은 통신·비용 계획에 함께 반영하며 B Source 추가 변경은 필요하지 않다.

**보고 형식 유지:** 목적·저장소/파일·이번 결과/한계·관련자/연계·막힌 직접 입력·핵심 동작·B 다음 행동을 짧은 카드/표로 함께 설명한다. 상단 전체 현황·하단 전체 남은 작업을 유지하며 첫 회 전체 개요는 반복하지 않는다.

**이전 #12 인계 자료:** [병합 main Native Run 37330480298](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37330480298)의 정확 main39 PASS·Source clean과 artifact11353184732의 11파일/YAML8 Hash·main/Tree·보류·Secret0 검증을 완료했다. `ocp-source-handoff-6ea2d9a90ab7c58803767220abf956d3c1b54a5f`를 **10/13 00:09:31 KST** 만료 전 별도 보존·수신하며 원 제출/요청은 [원 댓글](https://github.com/seokpan/seokpan-hybrid-gitops/pull/12#issuecomment-5998279839)이다. 이전60bda/10/12 안내는 당시 이력이다.

**현행 Image Source의 기존 검증:** [Native #40](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37420661610)의 39 PASS(skip0)와 artifact `11392428533`의 Render8/Hash 대조는 기존 확인 결과다. 해당 자료 만료는 **10/13 14:52:05 KST**다. 이번 비용 감사에서 새 Render/다운로드나 Runtime 시험을 수행한 것은 아니다.

<details>
<summary>이전 Source 리뷰·수락 판단 — 병합 전 관측 이력</summary>

**현재 B 작업 묶음:** [GitOps #9](https://github.com/seokpan/seokpan-hybrid-gitops/pull/9)는 main `c8b87904a28b8a6db5fbcdb35ac781cfb3f72615` 병합·기존 브랜치 보존 이력이다. [Docs #39](https://github.com/seokpan/seokpan-hybrid-docs/pull/39)는 main `6f77ef39de0508752c52bfe7d427df4b78767483` 병합·해당 브랜치 삭제를 확인했다. [GitOps #11](https://github.com/seokpan/seokpan-hybrid-gitops/pull/11) `7d66958f0a7bfa00104f6bd82656d9785b393eba`는 [C 최신 승인](https://github.com/seokpan/seokpan-hybrid-gitops/pull/11#pullrequestreview-5415539176) 수신·merge_state clean·A/D 요청 유지, [Infra #28](https://github.com/seokpan/seokpan-hybrid-infra/pull/28) `8061326041f03aa2cd556afab9a8fbb4890df310`는 [A](https://github.com/seokpan/seokpan-hybrid-infra/pull/28#pullrequestreview-5415411614)·[C](https://github.com/seokpan/seokpan-hybrid-infra/pull/28#pullrequestreview-5415579240)·[D](https://github.com/seokpan/seokpan-hybrid-infra/pull/28#pullrequestreview-5415352568) 최신 HEAD 승인 수신·변경 요청 해소·merge_state clean이다. 두 Source는 기존 CI 통과·현재 보호/충돌 상태 기준으로 병합 가능하며 아직 병합/브랜치 삭제를 수행하지 않았다. #11의 base main 전환으로 #9 Stack 의존은 해소됐고 삭제는 main 포함·추가 미병합 변경·다른 PR base·본인 변경 보존을 확인한 뒤 판단한다. **B는 병합 #9의 OCP Source·Render·입력표·Case를 D/C에 인계하면서 Cloud/Recovery·Secret·Controller/실제 Plan 준비를 병행한다.** 기본0/미확정 입력·별도3Replica Preview/captured·Owner/실제 업무 수락과 Runtime7/T18은 그대로다. [최신 판단](05_IMPLEMENTATION_AND_VALIDATION.md#b-current-source-acceptance-20261005)을 우선한다.

| 지금 검토할 원본 | 사용할 전체 HEAD·자료 | 다음 확인 |
| --- | --- | --- |
| [h-gitops PR #9](https://github.com/seokpan/seokpan-hybrid-gitops/pull/9) | main `c8b87904a28b8a6db5fbcdb35ac781cfb3f72615` 병합 · [OCP 최초 인계](https://github.com/seokpan/seokpan-hybrid-gitops/blob/c8b87904a28b8a6db5fbcdb35ac781cfb3f72615/handoff/OCP_FIRST_DEPLOYMENT.md) · 기존 브랜치 보존 | B/D/C는 병합 Source·Render·Case를 인계하고 해당 실입력부터 새 Run. [Runtime7 표](https://github.com/seokpan/seokpan-hybrid-gitops/pull/9#issuecomment-5995162694)의 실제 수락은 별도 |
| [h-gitops PR #11](https://github.com/seokpan/seokpan-hybrid-gitops/pull/11) | `7d66958f0a7bfa00104f6bd82656d9785b393eba` · base main · [39개 Source PASS](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37318410790) | [C 최신 승인](https://github.com/seokpan/seokpan-hybrid-gitops/pull/11#pullrequestreview-5415539176) 수신·merge_state clean·A/D 요청 유지. 현재 Source 병합 가능, 기본0/입력보류·별도3Replica Preview와 captured/Owner·실제 업무 수락은 별도. [최종 원 답변](https://github.com/seokpan/seokpan-hybrid-gitops/pull/11#issuecomment-5996033678) |
| [h-infra PR #28](https://github.com/seokpan/seokpan-hybrid-infra/pull/28) | `8061326041f03aa2cd556afab9a8fbb4890df310` · [동일 HEAD Source CI](https://github.com/seokpan/seokpan-hybrid-infra/actions/runs/37315242625) · [원 실행 조건](https://github.com/seokpan/seokpan-hybrid-infra/blob/8061326041f03aa2cd556afab9a8fbb4890df310/terraform/rosa/REVIEW_AND_EXECUTION_GATES.md) | [A](https://github.com/seokpan/seokpan-hybrid-infra/pull/28#pullrequestreview-5415411614)·[C](https://github.com/seokpan/seokpan-hybrid-infra/pull/28#pullrequestreview-5415579240)·[D](https://github.com/seokpan/seokpan-hybrid-infra/pull/28#pullrequestreview-5415352568) 최신 HEAD 승인 수신·변경 요청 해소·merge_state clean. 현재 Source 병합 가능, 실제 issuer preflight·Plan/비용·생성 후 SA JWT/STS는 Infra25 별도 단계. [최종 원 답변](https://github.com/seokpan/seokpan-hybrid-infra/pull/28#issuecomment-5996034151) |

</details>

이전에는 실제 Image/lab/Recovery 수락이나 실제 기반 입력을 Draft 해제의 선행으로 함께 묶었다. 이번에는 입력 대기 선언의 **Source 리뷰·병합**과 **실제 활성화·Plan·시험 수락**을 분리한다. Source의 입력 보류·Owner·수동 Sync·삭제 보호·Case를 사람에게 검토받는 데 실제 배포 전체 완료가 필요하지 않기 때문이다. Source 검사/Ready와 Runtime PASS는 다르며, 새 OCP Root/Project와 선택 Namespace·suspended 읽기 전용 Schema 확인 Job도 실제 적용·DDL 실행 증거가 아니다. 상세 근거는 [05 §9.25](05_IMPLEMENTATION_AND_VALIDATION.md#b-source-review-handoff-20261005)에 연결한다.

이번 리뷰 후속의 처리 근거·새 개정·재리뷰 경로는 [05 §9.26](05_IMPLEMENTATION_AND_VALIDATION.md#b-source-review-resolution-20261005)에 연결한다. 비차단 제안을 모두 물리 실행으로 처리하거나, 모든 제안을 설계 변경으로 확대하지 않는다. Cloud 다중 Pod 모드는 자동 확정하지 않고 실제 계약·상태/경합 검증 후 활성화한다. 실제 OCP와 ROSA 실행 Gate·TH 완료 판정은 그대로 유지한다.

**추가 검증의 시점:** RHCS 1.7.7의 scheme 제거와 이번 `StringEquals` Source 보완은 실제 AWS/JWT/STS 성공 증거가 아니다. 고정 Classic v1.7.2/현행은 ForAnyValue 예제이며 별도 rosa-sts 모듈의 plain 비교와 구분한 뒤 AWS 단일 요청 값 규칙을 채택한다. 생성 전 실제 입력/권한·issuer/TLS/JWKS·전체 Plan/비용/범위를 확인하고 실제 Operator SA JWT의 Web Identity STS는 승인 Cluster 생성 후 확인한다. 이를 Source 병합 전 일괄 조건으로 묶지 않으며 실패 시 확대 실행 중단·Owner/비용/정리를 기록한다. 최신 근거는 [05 §9.28](05_IMPLEMENTATION_AND_VALIDATION.md#b-oidc-condition-review-followup-20261005)이다. 현재 OCP 실입력/보류 검사·ROSA 로컬 준비는 [05 §9.32](05_IMPLEMENTATION_AND_VALIDATION.md#b-ocp-input-gates-rosa-local-preparation-20261006)를 따른다. §9.29~9.31의 당시 Source 리뷰·병합 대기는 이력이다.

상위 개인 체크 정본은 [h-docs Issue #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21)의 TH01~19/81개다. 완료체크 TH03.1/03.2를 보존하고 아래 준비/실측 분해만으로 다른79개를 자동완료 처리하지 않는다. 팀 전체 W/T는 [팀 실행 순서](TEAM_EXECUTION_SEQUENCE.md)·[h-docs Issue #8](https://github.com/seokpan/seokpan-hybrid-docs/issues/8)이며 B 개인 일과 구분한다.


</details>

## 2 다음 작업 구간에서 B가 할 순서

| 우선 | B의 구체적인 행동 | 남길 결과/관련 담당 | 기다리는 범위 | 원본·TH |
| --- | --- | --- | --- | --- |
| 1 | 본인 clone의 HEAD·개인 변경을 보존하고 App/GitOps/Infra 병합 SHA·도구를 읽기 확인 | 본인 환경에서 확인한 전체 SHA·변경/도구·확인 시각. 별도 조사용 작업 공간의 결과와 구분 | A/C/D 전체 완료 대기 없음. 본인 PC 접근 확인만 본인 수행 | Docs21, TH01/02 |
| 2 | 병합 #12의 최신 main artifact를 별도 승인 경로에 보존하고 ZIP/Hash·Source 개정 수신 기록 | 만료10/13 00:09:31 KST 전 보존 위치/개정·수신/보완. GitOps10↔D GitOps5/6 | Source PR 리뷰/병합 대기 해소. ZIP 직접 수신/보존은 아직 기록 미확인 | GitOps10/5/6, TH08 |
| 3 | D의 AppSHA→Build/Scan/Digest/Pull·lab Owner/권한, C의 DB/Redis/TLS/CA/Secret/Schema·Migration 보호 공급 개정 대조 | 제출·수신/보완·실입력 수락 범위. 값/Token/Key 원문은 공개하지 않음 | 실제 공급 개정을 쓰는 시험만 대기. 필요한 입력/Case 대조는 지금 가능 | App1/2·GitOps5/6/10, TH03~08/14.1 |
| 4 | 최소 입력 수락 후 별도 lab 활성화 PR에서 Replica/Digest·Renderer/보류 검사 함께 검토 | 같은 BE Digest/Config·필요 Schema/단일 Migration 수락 → D/B/C 수동 Sync·동일 조합 새 Run | 현재 보류 artifact는 실행용이 아님. 실제 Image/Context/Data/Migration 수락 필요 | GitOps5/6/10·App1/4, TH08.4 |
| 병행 A | OCP 결과와 Cloud/Recovery 차이·Secret/관리/Bundle·다중 Pod/업무 Case 준비 | Owner/보호 공급/환경 차이·수락/재시험 범위 | 실제 적용만 해당 입력 대기. OCP/ROSA 전체 종료 대기 없음 | GitOps10·App4, TH09/11/15 |
| 병행 B | ROSA 로컬 안내로 본인 clone/Lock·도구·Caller/Backend·서비스 권한/지원·A/C 출력 대응 확인 | Infra25↔A Infra23/20·C Infra19·D Infra18의 실제 입력/준비 수락표 | 안내 문서 검토와 실제 Plan은 별도. 실제 보호 출력/목적 권한·지원/예비 비용 수락 후 첫 Plan | Infra25, TH10~12 |

전체 Cloud Root/NP/UWM/완성 Recovery Bundle를 모두 끝내야 첫 OCP Sync를 할 수 있다는 일괄 조건은 만들지 않는다. 기존 OCP의 승인 Project/Application을 쓸 수 있으면 그 시험의 직접 Source·Owner·권한·입력을 확인해 최소 조합부터 검증한다. 공통/Cloud 전체 선언의 남은 범위는 병행해 완료한다. 공유 환경 소유/권한 가능 여부는 실제 Owner 확인이 필요하다.

## 3 B를 막는 입력은 실행별로 다르다

| 보류 중인 실행 | 최소 직접 입력 / 공급 책임 | 입력을 기다리는 동안 계속할 B 작업 | 완료 확인 위치 |
| --- | --- | --- | --- |
| **OCP 최초 App Sync** | D: 새 App Source의 Harbor 승인 원본을 보존 복사한 내부 Registry Image·Scan/Digest/Platform/Pull·Context/Namespace/공유 Operator/실효 권한. C/D: lab DB·Schema·직접TLS/CA·Redis TLS/별도AUTH. B: 해당 선언/Secret 공급·Migration·초기 활성화 | 선언·Render·Case·인계와 Cloud/Recovery/ROSA Source 준비 | GitOps5/6의 동일 조합 새 Run·D 결과/B 수신 |
| **실제 rosa Plan** | A: 실제 필수 기반 출력/개정·Backend/목적 실행 Role. C: Data SG 의미 검토. B: Controller/정확 Caller·서비스 권한·지원/Quota·입력 대조. D/B: 사전 비용/창 리뷰 | PR28 Source/Schema/리뷰·Controller 준비, OCP·Secret·Bundle Source | Infra25와 원 보호 Plan/리뷰 참조 |
| **유료 ROSA 생성** | 최신 Source/실입력의 보호 전체 Plan·리뷰, 실제 지원/권한/Quota, D 전체 비용($450 계획/$500 한도)·기간/삭제/재시험/잔존·단일 실행자·구체적 실행 동의 | lab 실패 수정·Cloud 승격 조합 준비·관리/Secret Case | Infra25·Cost/Shared Execution·실제 생성 Run |
| **ROSA 최초 App 배포/E2E** | 실제 Cluster/Worker SG→Data Binding, 실제 C RDS/Redis Endpoint·목적 계정/CA/TLS/AUTH/Schema, D ECR Image/Worker Pull, B Root/Cloud Secret·Migration/Host/Route | App/선언 결함 수정·E2E/관측·복구 자산 구성 | 해당 원 Issue와 Run/Index·인계 수신 |
| **격리 로컬 전체 T18** | A: 승인 격리 Host/공간/Storage. C: 실제 검증 Backup·로컬 완성본/Hash·독립 Key/CA·복원. D: 보존 Harbor Image/Scan/Mapping·시간선. B: 복구 Render/도구/FE/API/WSS/업무 계약 | Bundle 목록/Render/Case·부분 예행 검토·코드 준비 | Infra17/App4·T18 새 Run·C 검토/D Index 수신 |
| **초기 관리자 회수** | 정상 개인 관리·Argo 권한과 유지 비상 경로 실제 성공, 신규/기존 Token·Session 회수 Case | IDP/RBAC/공급 선언과 Case | 실제 환경별 Run·B/A 리뷰 |
| **중간/최종 rosa 삭제** | App 쓰기/진행상태 보호·Backup 로컬완성·Release/Bundle/Key/영상 접근·Binding 해제·범위/비용/인계 | 삭제/보존 목록·Runbook·발표·증거 정리 | Infra25·T19/T20·실제 삭제/잔존 기록 |

Harbor에서 생성·보존하고 OCP 내부 Registry로 복사한 Image의 lab 사전검증을 ECR+Harbor CI E2E나 최종 Cloud Release 완료로 표시하지 않는다. ECR이 아직 없어도 해당 lab Image/보호/승인 경로로 OCP 사전검증을 준비할 수 있으며, ECR/Worker Pull과 양쪽 Registry 실제 검증은 별도로 남긴다. 현재 기록에 새 Image/입력이 없다는 것은 공급 완료 미확인 상태이며 서버에 없다고 직접 관측한 뜻이 아니다.

## 4 A가 어느 범위까지 제공하면 B의 실제 Plan이 가능한가

현 [h-infra PR #28](https://github.com/seokpan/seokpan-hybrid-infra/pull/28) 병합 main `eab495210981b7c5ab0db436c082f449c6554792`의 계약 기준이며 검토 Source `8061326041f03aa2cd556afab9a8fbb4890df310`와 같은 Tree다. OIDC 공통 정규화/검사를 보강하되 Root·State·권한 Owner·버전/Lock의 경계를 유지한다. **A의 모든 업무 종료가 아니라 rosa가 소비하는 필수 실제 출력 묶음의 수락**이 필요하다. 현재 코드는 Network만으로 Plan할 수 없다.

| 필요 묶음 | 필요한 내용 | 여기까지 필요 없는 것 |
| --- | --- | --- |
| 입력 정체/정본 | 같은 Account/Region·VPC, 제한 출력 개정·생성 SHA/시각·도구/Provider 고정, 허용 필드 | 전체 State dump·가짜 실제ID |
| Network | VPC·3AZ의 Public3/ROSA-private3 Subnet과 AZ 매핑 | VPN 최종 재구축/전체 Hybrid 장애 시험 |
| 공통 ROSA prerequisite | 실제 Classic Account Role4개 ARN/prefix/path와 Operator Policy 참조 | 생성 뒤에야 알 수 있는 실제 Worker SG |
| Data 경계 | MariaDB/Redis Data SG-ID2개와 C의 의미/통신 범위 검토 | 실제 DB 데이터 이전·백업 전체·DB/Redis Endpoint/비밀번호/CA |
| 실행 연결 | bootstrap 정본 Backend의 rosa Key/Lock·본인 목적 Role/Caller와 서비스 권한, 지원/Quota 및 입력/지원/사전비용/창 리뷰 | A 복구 Host 완성·C/D 모든 팀 업무 종료 |

Account-wide prerequisite는 승인 설계의 foundation 소유이고, Cluster-specific IAM/OIDC/SG Binding은 B의 rosa 소유다. 입력 봉투에 들어 있다는 이유로 역할 작성책임을 새로 옮기지 않는다. A는 foundation 소유 범위의 코드 통합/Plan/실행·출력 공급, B는 실제 Classic/RHCS 요구·소비 Schema·Cluster-specific 역할/OIDC·권한 차이를 검토/보완·인계한다.

현재 PR28은 **1단계 Cluster 생성 시 worker_sg_binding=null 허용 → 2단계 실제 Cluster/Worker SG 확인 뒤 Data Binding 적용**이다. 이때 처음부터 Data SG 참조2개는 필수다. Stage1 Source/Plan 가능, 실제 유료 생성 가능, Stage2 연결·App 업무 가능을 각각 기록한다. Source fmt/Backend 없는 validate/schema 성공에 실제 A 출력이나 Cloud 인증을 요구하지 않는다. Stage2와 실제 Worker Pull/Data/Secret 확인 전 App을 기동 가능한 상태로 판정하지 않는다.

## 5 OCP에서 무엇을 하고 언제 나오는가

OCP는 이미 수행한 공개 예제/demo2 보고를 버리고 처음부터 새 Cluster를 만드는 단계가 아니다. **현재 hybrid Source+새 Image 조합**으로 미검증 위험을 앞당겨 확인한다. 실습 실행/결과 조율은 D, B는 base/Overlay·App 문제 해결/인계, C는 DB/Client 계약을 협업한다.

| 순서 | 실제 OCP 작업 | 나오는 조건 / 다음 행동 |
| --- | --- | --- |
| 준비 | exact Source·필요 선언·Image/CA/Secret/Context·Owner·Migration·삭제 보호 확인 | 해당 시험 입력이 수락되면 제한 배포. 전체 Cloud/Recovery 선언 완료는 첫 배포의 일괄 Gate가 아님 |
| 배포 | 필요한 Platform/Application 수동 Sync·App 보류→Image/Secret·대상/Schema 검토→필요한 Migration 단일 실행·결과 수신→Schema 준비 확인→App 최초 수동 Sync·초기1Replica | 기존 Schema라면 불필요한 DDL을 강제하지 않는다. 배포0Replica/Synced만으로 성공 아님. 실제 Pod/Service Ready·목적 TLS/AUTH·업무 확인 |
| App/컨테이너 | 임의UID/SCC·쓰기/Volume·Pull·FE/API/WSS·Probe·TLS/CA/AUTH 양성/음성·Migration·CA개정/Pod교체·대표 업무/오류·종료/재접속 | 새 조합 Run·실패/제한·C/D 검토/수신. 다중Pod 조기Case는 lab 가용/승인 범위에서, Cloud3Replica 최종 판정은 ROSA |
| Argo/관측 | 해당 조합의 Sync/Health·Secret 별도 공급·Owner/Namespace·자동Prune 보류/Finalizer·연쇄삭제 보호·UWM/Alert 소비의 필요한 범위 | GitOps5/6 수락과 B Source 검토/리뷰. 공유lab DB 재시작/삭제 금지(PVC없음) 유지 |
| **OCP 사전검증 업무 완료** | 승격할 Source/Digest/Platform/설정·검사·실패/Cloud차이·재시험 범위를 D/B/C가 확인해 인계 | 해당 조합을 ROSA에서 검증. 실제 ECR/Worker Pull·RDS/ElastiCache Multi-AZ/Failover·ROSA 관리/재생성은 ROSA에 남음 |
| **OCP 실습 자원 정리** | 필요한 미커밋 원본/Overlay/Image/Run 보존 → D 검증종료+B 인계+공유 사용종료 → 승인 앱/예제/시험Secret 등 대상별 정리 | 공유 OCP Cluster 전체 삭제나 1차 자산 종료가 아님. 필요 재시험을 유지하면 Owner/끝내는 조건/잔존을 명시 |

OCP의 사전검증 업무 완료와 정리 날짜는 별개다. 추천 운영 배치는 새 조합의 필요한 lab 위험을 해결해 Window A에 넘기고, Cloud 초기 결함의 재현이 필요하면 그 범위만 유지한 뒤 정리하는 것이다. **OCP 삭제는 ROSA 시작 조건이 아니다.** Cloud 준비/Plan과 OCP 작업은 겹칠 수 있다. 최종 Offline 복구는 승인된 1차 On-Prem Kubernetes·새 전용 격리 MariaDB/새 Redis·보존 자산 경로이며 OCP 실습 종료와 같은 수명으로 묶지 않는다.

## 6 ROSA는 언제 시작하고 언제 끝나는가

| ROSA 단계 | B의 실행 / 직접 조건 | 종료·다음 단계 |
| --- | --- | --- |
| **준비 시작: 지금** | Source/Lock/Schema·Controller·지원/Caller/Backend·권한 gap·시간/Cost 준비. OCP와 병행 | 실제 필수 출력이 오면 Plan. A 전체 업무·OCP 철거 대기 없음 |
| **첫 실제 Plan** | §4 필수 실제 출력·목적 Role/Backend·지원/Quota·사전리뷰 | 보호 전체 Plan·A/C/D 필요한 범위 리뷰·D 전체 Cost/Window |
| **유료 생성/Window A 시작** | Source/Plan·지원/권한/총비용·유료 범위/기간/삭제책임·실행자 확인 | Cluster/실제 Worker SG·Stage2 Binding/Pull → 최소 Operator bootstrap → Root/Platform 수동 → App 보류 → Secret/Schema/Image → App 수동 |
| **Window A 정상 통합** | C 실제Data/이전·D ECR/Pull·B Secret/App/GitOps·대표 E2E/Backup·Release·정상 Baseline | Must결함 수정·재시험·검증Backup/Harbor/Bundle/Key 보존. OCP 재현/로컬 복구 준비 병행 |
| **Window A 종료/중간 정리** | 필요한 자산/접근·Data 쓰기/백업·Binding/정리 범위·Cost 확인 | 승인 rosa 중간삭제/실제잔존 확인 → 기반/Data/Backend 보존 → Window B 재생성 입력. 유지하면 실제 시간·비용·근거를 기록 |
| **Window B 후보** | T19 새Cluster/SG/Pull/Secret/GitOps/E2E 재생성 → 정상Baseline → T10~14 분리장애 → T16부하 | 공식 Run·실패/재시험·비교·영상/최종 Cloud자료 보존. T17/18 실제 사전 자산 확보 |
| **최종 ROSA 종료** | 최종 Cloud 필요시험/시연 자료·영상·복구 가능한 사전Backup/Release/Bundle/Key 확보 후 승인rosa 삭제 | 요청과 실제삭제·부속/잔존/Cost/후속청구 따로 확인. 발표일까지 가동할 필요 없음 |
| **프로젝트 완료** | 전체T/Must 판정·Run/Index 수신·발표·자료/Key 보존·불필요Credential/실데이터·잔존/보관책임 확인 | 10/26 목표. rosa 삭제·AWS비용 종료·프로젝트 완료를 각각 판정 |

정상 사용자 Cloud 경로는 VPN을 필수로 하지 않는다. VPN/Host의 실제 준비는 이전/Backup/Recovery 등 해당 실행에 필요하며 전체 B 또는 첫 Cluster 생성의 자동 선행조건으로 확대하지 않는다. 실제 자원 생성은 App/Pull/Secret 준비 상태와 남은 위험·대기 시간까지 Cost/Window에 반영해 유료 Cluster만 장시간 기다리게 하지 않도록 계획한다. 이는 OCP의 모든 최종 시험을 새 생성 Gate로 추가하는 뜻이 아니다.

전체 T18은 필요한 실제 사전 Backup/Release·로컬 독립 사본·해독/도구·FE/API/WSS가 준비되면 **ROSA 가동 창 밖에서도 가능**하다. AWS/GitHub/CloudIDP/ECR/KMS 신규 조회 비의존, 로컬 DNS/Harbor 허용·RTO10/DB RPO30·G+D+U≤30 실측을 유지한다. 부분 Fixture2건을 전체운영 성공으로 승계하지 않는다.

**중간 정리는 자동 삭제가 아니다.** 검증 Backup의 로컬 완성본·Release/Bundle/Key의 해독/접근, App 쓰기·Data/Binding 보호, 승인 삭제 범위·비용·인계를 확인한 뒤 실행한다. 유지하면 이유·실제 가동시간·비용과 후속 삭제/재생성 계획을 기록한다. 기존 Schema에는 불필요한 DDL을 강제하지 않고 필요한 Migration만 단일 실행·결과 확인한다.

## 7 정태훈 타임라인 — 승인 목표 창과 실제 실행 시각

개인계획 §9의 승인 날짜를 세분화한 배치다. 날짜는 목표 창이며 실제 가용시간·입력·Plan/Cost 없이 하루 완료/ROSA 생성삭제 시각을 확정하지 않는다.

| 목표 구간 | B 우선 작업 | OCP/로컬 | ROSA | 기간 말 확인 |
| --- | --- | --- | --- | --- |
| **지금~10/8** | §2 최초 lab 인계 묶음·실제 Image/입력수신, Cloud/Secret/Bundle·rosa 준비 병행 | 최소 새 조합 사전검증·실패수정. 필요한 조합을 WindowA에 넘기는 목표 | Source/Controller·지원·권한·필수Output·Plan/Cost 준비. 조건 충족 시 WindowA 후보 | 무엇이 준비완료/실측대기인지, 막는 입력/Owner/다음 확인시점 |
| **10/12~15** | WindowA 통합·Migration·대표업무·Must수정·Backup/Release/Bundle | Cloud결함 재현/재시험·격리 복구 준비. 사전검증 수락과 실습정리는 별도 | 필요한 WindowA 가동·정상통합/중간정리, 실제 시간을 Cost에 기록 | 동결할 Source/Digest/Config/Schema와 남은결함 |
| **10/16** | Technical Freeze | 핵심구현/조합동결·남은Case/자료gap | 핵심구현동결, 상시가동 뜻 아님 | Must/retest/누락자료와 실행계획 |
| **10/19~21** | TH16→TH17: 재생성·정상Baseline·분리장애·부하·비교 | 실자산준비 후 전체T18. ROSA창 밖에서도 수행 | WindowB 후보. 실제 생성/삭제시각은 Plan/Cost/가용창으로 확정 | T별Actual/판정·실패/한계·최종필요영상/자료 |
| **10/22** | Demo Freeze·영상/시연흐름·증거보존 | 자료/해독/접근·재현검증, 실습잔존정리 | 최종 Cloud시험/자료확보 후 승인rosa삭제 가능. 10/22를 확정삭제일로 지정한 것은 아님 | 시연/예비영상·자료/Key 접근·남은시험 |
| **10/23** | Presentation Ready·개인기여/대본/Q&A/리허설 | Runbook/Index/한계·보관수신 | 잔존/후속청구/보관확인. 필요한 추가가동은 Cost/창/정리범위 별도 | 발표준비와 실제정리/잔여상태 |
| **10/26** | 발표·최종판정·인계·프로젝트 종료 | 증거/Key/자료보존·불필요Credential/실데이터정리 | 실제삭제/잔존비용·후속청구책임 | 필수미완료 해결 또는 승인범위재결정·수신된 후속책임 |

실제 OCP 정리일·Window A/B 시작/종료시각·최종 rosa 삭제일은 **미확정**이다. 입력이 늦으면 해당 실행만 늦추고 독립 작업은 진행한다. 목표 창이 위험해지면 날짜를 조용히 미루거나 Cost를 임의 PASS하지 않고 막는 산출물·영향·우선순위/범위 대응을 원 Issue에 기록한다. 10/26까지 Cloud를 계속 켜두는 계획이 아니다.

## 8 팀 전체 병행·직접 의존 표

| 공급 작업/담당 | 지금 병행할 수 있는 일 | 무엇을 직접 풀어주는가 | 이 작업이 끝나기 전에 가능한 B/팀 작업 |
| --- | --- | --- | --- |
| A 공통foundation/Network·공통prerequisite/권한 | 전체Root 틀·코드통합·제한Output/Plan/Cost/실행·인계 | §4 필수출력이 실제수락되면 B rosaPlan/해당생성 | B App/GitOps/Render/OCP준비·D CI/lab·C DataSource |
| A VPN/격리Host | 기존PoC보존·최종Route/허용거부·Host/Storage/공간·복구준비 | 실제 이전/Backup전송·격리Restore/접속 | B Source/OCP·ROSA Source/Plan/지원준비; Cloud정상사용자경로와 구분 |
| C DataRoot/SG | module→foundation직접배치·공통파일/Network개정 리뷰·권한/SG 계약 | A 통합Plan, SG2개수락은 B rosaPlan 직접입력 | C 전체DB이전/백업 완료 없이 B 독립Source/OCP |
| C 목적DB/Redis/TLS/Schema | lab계약과 Cloud/복구계약·GRANT/CA/AUTH·이전조건 | 해당 lab 실제연결, Cloud App/Migration 연결 | B Manifest/Case·rosaSource/필수Output후Plan; lab과Cloud값혼용금지 |
| C 이전/15분Backup/Restore/Key | 반출/가명화조건·Timer/실패·성공Data간격/로컬지연·보호사본/해독·실측 | T05/T17/T18·중간/최종Data/Cloud정리보존 | 실데이터동의대기는그반출만; 독립합성/Source·D Image·B OCP준비 계속 |
| D OCP용Image/lab | 새SourceBuild/Scan·HarborDigest/Platform/Pull·Context/Namespace·실효권한·Owner | OCP 최초Sync/같은조합수락 | ECR/전체foundation없는구간의 Source/labImage준비 가능; 최종CI E2E와분리 |
| D 2차CI/Registry/WorkerPull | PAT/Job/Plugin/등록재현·CI정책/ReleaseMapping·ECR실제Push/거부·Preview/N·WorkerPull/12시간/재생성 | Cloud Image/실제Pull·T21 | B Source·OCP사전조합, A/C 기반/Data준비 |
| D Harness/관측/Index/Cost | Case/시간선·UWM/Alert/부하순서·시험수신·가동/잔존/재시험집계 | 해당유료Apply Cost/Window와 실제시험판정/Index | B/C/A자기Case·Runbook·부분예행과제출; D수신을대신체크하지않음 |
| B 각환경선언/App/Secret/rosa | §2 독립준비·필요Source/Case·검사와소비인계 | Dlab의선언입력·C복구App계약·ROSA생성/Cloud통합 | B안에서도 Source·OCP·ROSA준비를병행. 실제공유State/Restore/배포/장애는단일실행조율 |

같은 foundation State는 A 통합/실행을 유지하고 C/D가 별도State/단독Apply하지 않는다. 작업이 끝났다는 보고·인계 제출·수신·실제실행·시험판정을 구분하며 미관련Owner의 모든업무를 종료조건으로 삼지 않는다.

## 9 TH81 세부행의 준비·실측 분해

원본 TH식별자/순서를 유지한 안내 표다. 준비/기존근거/입력대기/후속실측은 체크정본을 대체하지 않는다. 아래표만 보고 기존79개를 완료처리하지 않는다. 마지막 열은 결과를 먼저 남길 실행 원본이며, 세부 완료 기준과 체크 정본은 Docs21에 그대로 둔다.

| TH | 지금 할 부분/현재 근거 | 보류 실행·최소 조건 | 주 기록 위치 |
|---|---|---|---|
| TH-01.1 | 지금: 개인Controller/clone/HEAD/도구/Reviewer 점검 | 실제 Controller 정보는 본인 확인; 외부Source준비는 계속 | [h-docs Issue #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21) |
| TH-01.2 | 지금: 미커밋/미추적/ignored/ZIP 비교보존 | 본인PC자료 접근 필요, 공개자료로대체하지 않음 | [h-docs Issue #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21) |
| TH-01.3 | 지금: SHA·논리참조·변경범위·부족입력 표 | 수신한 실제 개정으로 갱신 | [h-docs Issue #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21) |
| TH-02.1 | 기존근거: 1차종료/최신Seed/출처 구분 | 다시이관하지 않고 근거연결 | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) |
| TH-02.2 | 기존근거: App Source 수락/검사; Image수락 별도 | D 승인Image/전체Digest·Platform | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) |
| TH-02.3 | 기존근거: App PR5 이력보존병합 | Source 이관 완료를 미착수로 되돌리지 않음 | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) |
| TH-02.4 | 지금: D/C/GitOps에 소비범위 인계 | D/C 수신응답을 별도기록 | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) |
| TH-03.1 | 기존완료: CI A~F 리뷰게시 | 기존체크 유지 | [h-app Issue #2](https://github.com/seokpan/seokpan-hybrid-app/issues/2) |
| TH-03.2 | 기존완료: D 방향수신 확인 | 기존체크 유지 | [h-app Issue #2](https://github.com/seokpan/seokpan-hybrid-app/issues/2) |
| TH-03.3 | 지금: App2/Infra18/23 최종소비개정 대조 | PAT/CI실측 결과와 작성통합수신 분리 | [h-app Issue #2](https://github.com/seokpan/seokpan-hybrid-app/issues/2) |
| TH-03.4 | 지금: LifecycleN/재현등록/PAT/Release 후속담당/시점 | 실제 Preview/PAT/CI 실행은 D입력 | [h-app Issue #2](https://github.com/seokpan/seokpan-hybrid-app/issues/2) |
| TH-04.1 | 지금: DB/Redis/TLS/CA/Hostname/AUTH 소비계약 | 실제 C대상/계정/CA 공급은 연결시 | [h-app Issue #1](https://github.com/seokpan/seokpan-hybrid-app/issues/1) 계약 범위 |
| TH-04.2 | 지금: Engine별Pool/수명/KST/Schema·이관조건 | 실제데이터 반출만 C동의/가명화조건 확인대기 | [h-app Issue #1](https://github.com/seokpan/seokpan-hybrid-app/issues/1) 계약 범위 |
| TH-04.3 | 지금: 상태공유/동시확정/Generation/부분실패 코드gap | 최종다중Pod 판정은 실제환경 | [h-app Issue #1](https://github.com/seokpan/seokpan-hybrid-app/issues/1) 계약 범위 |
| TH-04.4 | 지금: C/D 수정·Case·필요입력 인계 | C/D 실제수락/보완 응답 | [h-app Issue #1](https://github.com/seokpan/seokpan-hybrid-app/issues/1) 계약 범위 |
| TH-05.1 | 기존근거: 환경대상/Runtime·Migration 검사Source 병합 | 실제목적계정/환경조합 검증별도 | [h-app Issue #1](https://github.com/seokpan/seokpan-hybrid-app/issues/1) |
| TH-05.2 | 기존근거: Redis URL자격거부·별도AUTH/TLS Source | 승인Driver/실제CA·AUTH 런타임검증 | [h-app Issue #1](https://github.com/seokpan/seokpan-hybrid-app/issues/1) |
| TH-05.3 | 기존근거: App파서/Settings/Client; Secret참조 대조 | GitOps 최신선언 개정정합 확인 | [h-app Issue #1](https://github.com/seokpan/seokpan-hybrid-app/issues/1) |
| TH-05.4 | 기존근거: 양성/음성검사 | 실제환경 오류/비밀값로그 미노출 확인 | [h-app Issue #1](https://github.com/seokpan/seokpan-hybrid-app/issues/1) |
| TH-06.1 | 지금/기존근거: FE/API/WSS/Origin/오류Source gap리뷰 | 실제브라우저/WSS 경로는 OCP/Cloud | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) |
| TH-06.2 | 지금: Probe/UID/쓰기/Drain 선언대조 | 실제Image와 OCP UID/Volume/종료검증 | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) |
| TH-06.3 | 지금: 시간/재접속/Generation/상태코드 조사수정 | 최종Runtime결과는 별도 | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) |
| TH-06.4 | 후속실측: Pod내부·ServiceReady·업무/종료Case | 같은Image/Secret/Context lab 또는Cloud | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) |
| TH-07.1 | 기존근거/지금: 기존검사범위연결·필요gap 검사 | 의미있는 변경/미해결관심만 재검사 | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) 검사/인계 |
| TH-07.2 | 기존근거: 부분예행; 실제Driver Client수명Case | 목적CA/AUTH/승인Driver 실제연결조합 | [h-app Issue #1](https://github.com/seokpan/seokpan-hybrid-app/issues/1) Client 실제검사 |
| TH-07.3 | 지금: 병합main SHA·검사·빌드범위 D인계 | D 수신과 Build실행 별도 | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) Build 인계 |
| TH-07.4 | 입력대기: 다음 App 개정이 필요하면 D 새Image/RegistryDigest·Platform·Scan수신 | 현재 승인 Image의 공급 수락은 보존. 새 Build와 GitOps6 실제 결과는 별도 | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) Image 수신 |
| TH-08.1 | 지금: 원 labManifest 개정/범위/질문 대조 | 개인원본 미반영자료는 D/작성자확인 | [h-gitops Issue #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10) |
| TH-08.2 | 지금: Root/Project/Namespace/NP/Migration 누락Source | 실제Secret값/Cloud주소 없이 선언준비가능 | [h-gitops Issue #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10) |
| TH-08.3 | 지금: KustomizeBuild/Owner/Sync·Prune·삭제Case | 실제Sync는 Context/Secret/Image 후 | [h-gitops Issue #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10) |
| TH-08.4 | 지금인계/입력대기: SHA/조건 D전달·실제lab 수신 | D같은조합 결과·Image/Context/Secret | [h-gitops Issue #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10) |
| TH-09.1 | 지금: Cloud ECR/Replica/PDB/Rolling/AZ선언 | Cloud Runtime은 실제ROSA/Pull/Data | [h-gitops Issue #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10) |
| TH-09.2 | 지금: RecoveryHarbor/1Replica/새Redis/DBTLS Render | 실제Host/Volume/Image/CA/Secret은 배치시 | [h-gitops Issue #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10) |
| TH-09.3 | 지금: 환경배포참조/Secret공급/Owner 경계리뷰 | 해당Owner 수신응답 별도 | [h-gitops Issue #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10) |
| TH-09.4 | 지금Render/입력대기: Source·Config개정고정·C/D검토 | 실제Image/설정 조합의 수락 | [h-gitops Issue #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10) |
| TH-10.1 | 지금: A/C/D Schema·Owner·Account/Region 의미리뷰 | 실제값수신/대상존재는 Plan직전 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) |
| TH-10.2 | 기존근거: PR28 Root/Lock/Cluster/OIDC/Binding Source | Source리뷰와 실제Plan/권한 별도 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) |
| TH-10.3 | 기존근거/지금: 제한입력/오류차단 Source검사 | 실제Caller/자원존재/통신으로 확대금지 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) |
| TH-10.4 | 지금/입력대기: A리뷰·권한README정합 | A 실제입력개정 수신·PR30범위 별도 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) |
| TH-11.1 | 지금: Cloud주/예비·독립사본·CI예비 준비 | 실제자산/Identity·공급·수신 확인필요 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) 공급책임 |
| TH-11.2 | 지금선언/후속실측: IDP/RBAC/Argo/비상Case | OCP모형과 ROSA실제관리 판정구분 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) 관리/공급 |
| TH-11.3 | 후속실측: 초기인증/높은Binding/Token/Session회수 | 정상개인+유지비상 경로 실증후 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) 관리/공급 |
| TH-11.4 | 후속실측: 공급/복호화/재주입/회수·책임인계 | 실제서비스/Secret대상·수신 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) 공급/회수 수락 |
| TH-12.1 | 지금Controller준비/입력대기: 지원·Quota·Caller·Backend | 실제목적Role/기반허용출력·지원확인 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) |
| TH-12.2 | 입력대기: 보호Root전체Plan·A리뷰 | 실제Backend/Caller/SourceLock/입력 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) |
| TH-12.3 | 지금: 수량/시간/부속/잔존 비용입력 D전달 | 실제Plan/단가/Credit/가용창으로 완성 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) |
| TH-12.4 | 입력대기: 전체Cost/실행창·유료조건 확인 | $450계획선/$500총한도·기간/삭제책임 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) |
| TH-13.1 | 후속실측: WindowA rosa생성 | 최신Plan/입력/리뷰/비용/공유실행/실행의사 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) 통합 Run |
| TH-13.2 | 후속실측: Secret/Pull/GitOps/Schema/Migration통합 | 실제Cluster·Data/Pull·목적계정·C이전조건 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) 통합 Run |
| TH-13.3 | 후속실측: 대표E2E/TLS/시간/Digest 정상Baseline | 앞선 App/Data 통합조합 | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) 실제 업무 |
| TH-13.4 | 후속실측: 검증Release/Backup계약/Recovery보존 | 정상업무·검증사본·접근/인계 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) 통합 보존 |
| TH-14.1 | 지금: 코드위험/gap·수정·Case 앞당김 | A전체완료/ROSA창 대기불필요 | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) |
| TH-14.2 | 후속실측: 만료/중복/경쟁/Commit불명/다른Pod | OCP가능범위와최종ROSA 조건분리 | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) |
| TH-14.3 | 후속실측: DB/Redis/통지부분실패·최종상태/시도수 | 실제Data/다중Pod·D충돌없는시험순서 | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) |
| TH-14.4 | 후속실측: T07~13결과·실패/새Run/한계인계 | 해당환경결과·DIndex수신 | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) |
| TH-15.1 | 지금Bundle구조/입력대기: Image/Render/CA/Secret/도구 | 검증Release·C/D실제입력·AHost | [h-gitops Issue #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10) B 복구인계 |
| TH-15.2 | 후속실측: 독립사본/Harbor/로컬/해독/공급접근 | 장애전확보·Owner보호자산 | [h-gitops Issue #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10) B 복구인계 |
| TH-15.3 | 지금: 새Redis/완료기록/신규게임/클라이언트 계약 | C 사용범위/수신응답 별도 | [h-gitops Issue #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10) B 복구인계 |
| TH-15.4 | 후속실측: 실제전체업무재개/Data/시간선 | 준비된격리환경·신규외부조회비의존·C/DRun | [h-gitops Issue #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10) B 복구업무 |
| TH-16.1 | 지금계획/후속실측: Binding보호·보존/삭제/재생성 | 실제foundation전후Plan·BCloud조합 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) |
| TH-16.2 | 후속실측: 쓰기제한·최신Backup·rosa중간삭제 | C데이터중지/재개·로컬완성본·기반보존 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) |
| TH-16.3 | 후속실측: 새rosa/SG/Host/Pull/Secret/GitOps | WindowB Cost/실행조건·새입력 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) |
| TH-16.4 | 후속실측: 새E2E·양쪽Plan·T19 | 실제재생성·이전SG잔존없음 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) |
| TH-17.1 | 지금Case계획/후속실측: 정상후 분리시험순서 | D순서/주입자/중단조건·실제Baseline | [h-docs Issue #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21) B 시험순서 |
| TH-17.2 | 후속실측: 공식장애/단절/Pull/관측/부하 B범위 | D조율·실제Cloud/보호/되돌림 | 해당 자원 [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4)/[h-gitops Issue #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10)/[h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) |
| TH-17.3 | 후속실측: Resource/Pool/업무/성능/시간/차이 | 실제수치·실패/새Run재시험 | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) App/Pool 업무 |
| TH-17.4 | 후속실측: B실제Run→Index/D집계 | D 수신확인·팀 전체 PASS는 별도 근거 필요 | [h-docs Issue #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21) B 수행 집계 |
| TH-18.1 | 지금: 구현/검증/판단/Troubleshooting 구분·후보 | 실제기여/근거 범위만 Docs6연결 | [h-docs Issue #6](https://github.com/seokpan/seokpan-hybrid-docs/issues/6) |
| TH-18.2 | 지금구조/후속실측: 조건/수치/한계/비교/기여 | ROSAActual·실제Run 뒤 내용확정 | [h-docs Issue #6](https://github.com/seokpan/seokpan-hybrid-docs/issues/6) |
| TH-18.3 | 후속실측: 시연/예비영상/대본/Q&A/리허설 | 10/22DemoFreeze·10/23Ready 목표 | [h-docs Issue #6](https://github.com/seokpan/seokpan-hybrid-docs/issues/6) |
| TH-18.4 | 후속실측: 발표결과·Source/Release/영상개정보존 | 최종발표·자료접근 확인 | [h-docs Issue #6](https://github.com/seokpan/seokpan-hybrid-docs/issues/6) |
| TH-19.1 | 후속실측: 최종Source/Release/Schema/Config/판정고정 | Must결과·미완료범위 판단 | [h-docs Issue #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21) 최종 조합 |
| TH-19.2 | 후속실측: Backup/Harbor/Bundle/Run/영상독립보존 | 해당Owner 확인·서로다른사본 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) 삭제 전 보존 |
| TH-19.3 | 후속실측: 자료접근/무결성/복원성/Key | 해독수단은 불필요Credential과 구분 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) 보존자산 수락 |
| TH-19.4 | 지금계획/후속실측: 삭제/보존Owner/순서/비용/책임 | 실제자원목록·선택범위/기간 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) 삭제/보존 목록 |
| TH-19.5 | 후속실측: 최종쓰기제한/Backup완성/Binding/삭제 | 보호자료·C중지/재개·승인rosa범위 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) 실행 + [h-docs Issue #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21) 개인종료 |
| TH-19.6 | 후속실측: 삭제완료/잔존/Orphan·Owner확인 | 기본rosa만·기반전체삭제별도승인 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) 실행 + [h-docs Issue #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21) 개인종료 |
| TH-19.7 | 후속실측: 잔존비용/기간/후속청구Owner·시점 | 실제잔존·D집계/Owner수신 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) 잔존비용 인계 |
| TH-19.8 | 후속실측: Credential/Token/임시자료/실데이터정리 | 필요한해독Key/검증자료 보존 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) B Credential/자원 정리 |
| TH-19.9 | 후속실측: T20/T23·Cost/Index/Tracker/05/Docs8정합 | 실제삭제/확인시각·원본링크 | [h-infra Issue #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) 실제 삭제/잔존 |
| TH-19.10 | 후속실측: B완료/수신/제외/보존/정리·상위종료 | 필수미완료해결 또는승인범위재결정·후속책임수신 | [h-docs Issue #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21) B 개인 종료 |

## 10 전체 남은 작업 현황

**현재 구분:** 기존 복합 체크를 보존하며 새 완료 체크는 추가하지 않는다. Image 제공·B 수락과 실제 Namespace Secret 공급·OCP Workload Pull/Ready/업무는 구분한다. D 공급·C/D Data 입력과 B 활성화, A/C 기반·목적 Role/Backend·지원/비용 준비를 병행한다. 비용1~5·예상/실제 기록·본인 가용성TBD·기존 목표 창·보존/종료 조건은 유지한다.

- [ ] **B 지금:** 본인 Source/개인 변경 대조 → 병합 OCP Source와 새 인계 PR의 입력/Case·진단 Render 보존·검사 → 제출·사람 수신/보완 → 최소 lab 입력 수신 → D와 새 조합 검증. TH01/03~08/14.1
- [ ] **B 병행Source:** Cloud/Recovery차이·Root/AppProject/NP/UWM·단일Migration·Secret/관리/Bundle·rosa계약/Controller·비용/창입력. TH09~12/15/17.1/18/19계획
- [ ] **A 기반:** foundation공통틀/Network·Data/Registry/공통ROSA prerequisite·권한코드통합, 보호Plan/비용/실행·필수제한Output수신. VPN/Host후속과구분
- [ ] **A Host/VPN:** 실제종단/Route·허용거부·재부팅/재구축·격리Host/공간/통신. 실제이전/Backup/Recovery의직접조건
- [ ] **C DataSource/입력:** Root전환/SG·목적GRANT/TLS/CA/AUTH/Schema·lab/Cloud/복구구분·실제이전/반출조건·인계수신
- [ ] **C Backup/Restore:** 운영중15분적용·성공Data간격/로컬완성지연/시각여유·실패/부하/공간·보호사본/Key·실제전체복원/수신
- [ ] **D Image/OCP:** 승인 원본·내부 Registry 사본/Scan/Digest/Platform·labContext/권한/Owner·같은조합Sync/Client/업무/삭제보호·Run/수신·실습정리
- [ ] **D CI/Pull:** 2차PAT/Job/등록재현/계정/권한·ECR/Harbor실제 Mapping·Push/거부·LifecyclePreview/최종N·HarborRelease보존·WorkerPull/12시간/재생성
- [ ] **공동Plan/유료실행:** B실제입력/Caller/Backend/지원·전체Plan/리뷰·D총Cost/가용창·구체적유료범위/기간/삭제/재시험·Shared Execution
- [ ] **ROSA Window A:** 생성/Stage2Binding/Pull·최초GitOps/관리Secret·C이전/Schema·App대표업무/정상Baseline·Backup/Release·Must결함/새Run. TH13/14
- [ ] **ROSA 중간/Window B:** 자산/접근·쓰기/Backup·Binding·범위/비용 확인 후 조건부 중간 삭제(유지 시 시간/비용 기록) → T19 재생성 → 정상 Baseline → 분리 장애/관측 → 부하·비교/실패/재시험. TH16/17
- [ ] **격리 전체T18:** 실제Backup/Release/독립사본/Key/Host·새DB직접 TLS/새Redis·FE/API/WSS/업무·RTO10/DBRPO30 실제판정. ROSA창밖가능, TH15
- [ ] **공식T01~T23/기록:** 환경/Case별최종판정·Must결함/범위·원Issue/새Run·C검토/DIndex수신·Tracker/05·개인 기여 범위를정합. Source/lab을Cloud최종PASS로승계금지
- [ ] **OCP 업무/정리:** 승격조합/차이/결함인계·공유사용종료·승인실습대상/시험Secret정리. 공유OCP전체/1차자산삭제로확대금지
- [ ] **최종ROSA/비용:** 영상/Backup/Harbor/Bundle/Key접근·복원확인→승인rosa삭제·실제부속/잔존·후속청구/Owner. foundation/bootstrap전체Destroy별도승인
- [ ] **발표·전체종료:** 비교/한계/기여·시연/예비영상/대본·자료/해독Key보존·불필요Credential/실데이터정리·보관/후속책임수신·T20/T23/Cost정합. TH18/19, W09~10
- [ ] **메타데이터/후속:** GitHub Freeze milestone은 현재10/18이며 승인 Technical Freeze10/16으로 정정 미완료. 원본/제출/사람 수신/실입력/Runtime 정합과 새 OCP 인계 PR 검사·Render artifact/Hash 수신·학습 안내 유지. Infra28/GitOps11 Source 승인·main 병합과 GitOps9/11 작업 브랜치 삭제·Docs40 병합 확인 완료

근거: 승인03 §3-C.4/3-F/3-G/3-H·3-I.14.5, 04 §2.2~2.3/3.1~3.2/4/9~10, 개인계획 §6/7/9/11/12/18, 지침 §37, 최신 원 Issue/PR/Tree/체크. 현재기록은원격Source/보고범위이며본인PC·OCP/AWS/Registry실제입력수신/서버상태는해당Owner/새Run으로확인한다.

<details>
<summary>이전 시점의 관측·검토 이력 — 현재 실행 지시와 구분</summary>

<a id="gitops17-merged-checkpoint-20261007"></a>
## 2026-10-07 현재 작업 기준 — GitOps #17 병합

[GitOps #17](https://github.com/seokpan/seokpan-hybrid-gitops/pull/17)은 2026-10-06 23:45:46 KST에 main `fa3cea313e2cb1533d9703082619b085a3de25cc`로 병합됐고 작업 브랜치가 삭제됐다. 검토 HEAD `adacf6fffd9d179eef4715e92a3fed721759db55`와 병합 SHA, 승인 Image Source `46e21a74dd608b41f2c12a0a57d76bddfcf25949`와 현재 App main은 각각 구분한다.

| 구분 | 현재 결과와 다음 조건 |
|---|---|
| Source | FE/BE·별도 Migration Job의 내부 Registry 주소·기존 Digest·lab Redis URL/기대 Host 연결이 병합됐다. lab Harbor Pull 참조 제거는 실제 Secret 삭제가 아니다. Cloud ECR·Recovery Harbor는 유지한다 |
| 실제 실행 | FE/BE replicas 0·Migration suspend/current/300초·단일 실행을 유지한다. 검토된 Valkey 선언과 Service/Ready 확인, DB/Schema·CA/목적 Secret·Route·권한·공유 사용창·live Diff 수락 뒤 필요한 단일 Migration → Backend → Frontend → 동일 조합 시험으로 진행한다 |
| Cloud 금고 | B 공개키 전달·C 암호문 공급 안내 수신은 완료다. Docs #66의 C 계정별 해독 확인 보고와 B 본인 확인·수신·독립 사본 검증은 구분해 대조한다. 비밀값을 기록하지 않는다 |
| 조사 범위 | 이번 Source 병합 반영은 네 저장소 전수조사 완료가 아니다. 설계·주석·그림·등록본의 발견과 남은 검토는 [정합성 조사 대장](REPOSITORY_CONSISTENCY_AUDIT.md) Q01~Q12를 따른다 |

아래 날짜별 기록은 해당 시점의 이력이다. 과거 대기 표시를 현재의 새 선행조건으로 되살리지 않는다. 기존 TH 81개·실제 완료 표시, C의 05 §8.13과 담당별 기록, 비용·Run 원본은 보존한다. Docs #64의 실제 병합 여부는 다음 작업 시작 시 GitHub에서 확인한다.

## 최신 후속 — 2026-10-07: GitOps #17 병합과 정합성 조사

[GitOps #17](https://github.com/seokpan/seokpan-hybrid-gitops/pull/17)은 2026-10-06 23:45:46 KST main `fa3cea313e2cb1533d9703082619b085a3de25cc`에 병합됐고 `b/lab-internal-registry-binding` 브랜치는 삭제됐다. 검토 HEAD `adacf6fffd9d179eef4715e92a3fed721759db55`와 병합 SHA를 구분한다. 내부 Registry 소비 Source의 리뷰·병합 대기는 해소됐으며, 아래 10/6 기록의 해당 대기 표시는 당시 이력이다.

| 작업 | 현재 상태 | B의 다음 행동·직접 조건 |
|---|---|---|
| lab 이미지·접속 선언 | FE/BE·별도 Migration Job의 내부 Registry 경로, 승인 Digest 보존, lab Harbor Pull 참조 제거, Redis URL/기대 Host 연결이 main에 반영됨 | 실제 사용할 main 개정을 확인한다. 기존 Secret을 삭제한 것은 아니며 Cloud ECR·Recovery Harbor는 유지한다 |
| Valkey와 앱 활성화 | FE/BE replicas 0, Migration suspend/current/300초·단일 실행·목적 자격 유지. #17 병합은 실제 Sync/Ready/업무 시험이 아님 | Valkey 선언·제한 AppProject Kind·TLS/AUTH/Probe/자원 검토와 실제 Service/Ready 확인. 나머지 DB/Schema·CA/목적 Secret·Route·권한·공유 사용창·live Diff까지 수락한 뒤 필요한 단일 Migration → Backend → Frontend → 동일 조합 Run |
| Cloud 금고 | B 공개키 전달과 C 암호문 공급 안내 수신 완료. Docs #66에는 C의 A/B 계정별 해독 확인 보고가 추가됨 | 원 보고의 수행자·시각·범위와 B 본인 확인/수신을 대조한다. C 보고를 B의 직접 확인·독립 사본 완료로 자동 승계하지 않는다. Token 값은 수집·출력하지 않는다 |
| Docs #64 | #17 병합 결과와 현재/과거 경계를 보완 중 | C의 #66 main 변경을 보존하며 실행판·학습 안내·Tracker·05를 정합화한다. #64 실제 병합·브랜치 삭제는 다음 작업 전 GitHub에서 확인한다 |
| 저장소·등록본 조사 | 네 저장소 전체의 최종 전수조사는 미완료 | [정합성 조사 대장](REPOSITORY_CONSISTENCY_AUDIT.md)의 Q01~Q12와 발견·미확인·재검증을 이어간다. 파일 목록 확보나 #17 검토를 전체 조사 완료로 확대하지 않는다 |
| ROSA·비용 병행 | 실제 기반 출력·Data SG 2개, B Caller/Backend·지원·사양·시간·전체 Cost 수락은 별도 | 독립 준비는 계속한다. OCP 정리·모든 Recovery 자산 완료를 실제 ROSA Plan의 일괄 선행조건으로 추가하지 않는다 |

**현재 설계 정합성의 주의사항:** 등록된 02~04는 저장소 Blob과 다르며, 저장소 03 도입부에도 DR를 병합 전 후보로 설명하는 문구가 남아 있다. 현재 요구는 RTO 10분·영속 DB RPO 30분·DB 운영 중 백업 계획 주기 15분이다. 설계 문서·코드·가이드·주석·그림 원본/SVG/PNG·등록본의 연쇄 대조가 끝나기 전에는 전체 정합성 완료를 선언하지 않는다. 실제 전체 T18 달성과는 별도다.

다음 10/6 절과 그 안의 이전 관측은 이력으로 보존한다. B의 TH 81개·실제 완료 체크는 이번 Source 병합과 문서 조사만으로 추가 완료 처리하지 않는다.

## 최신 후속 — 2026-10-06: 내부 Registry 소비·Valkey 선언·Cloud 금고 확인

[Docs63](https://github.com/seokpan/seokpan-hybrid-docs/pull/63)은 main `fa94b3ded9698516af9f4ec1837cab7e5cb74c2f`에 병합됐고 브랜치 삭제를 확인했다. 아래 이전 시점 안내에서 미수신으로 적힌 public key/암호문·Registry copy/Pull은 이번 수신 상태를 우선한다. 공급 보고·실제 복호화·Pod/업무 시험은 구분한다.

| 구분 | 현재 완료/수신 | B 행동·직접 대기 |
| --- | --- | --- |
| **내 일: Cloud AUTH** | B age public recipient 생성·C 전달 완료. C의 본인 계정 암호문 공급 안내 수신 | **10/7** 본인 Controller에서 값 출력 없이 복호화/64hex 검사·암호문 Hash 앞12자리 `9a86f90e6ba6` 대조 → C에 결과만 회신. 파일 존재/실제 성공·개인키 독립 사본은 미확인. Cloud/lab Token 분리 |
| **내 일: lab 소비 Source** | [GitOps PR17](https://github.com/seokpan/seokpan-hybrid-gitops/pull/17) 검토 HEAD `adacf6fffd9d179eef4715e92a3fed721759db55`; 후속 병합 main `fa3cea313e2cb1533d9703082619b085a3de25cc`·작업 브랜치 삭제 완료. FE/BE+별도 Migration Job 주소 내부 Registry 전환·lab Harbor Pull 참조 제거·Redis URL/Host 연결. Source39검사/진단Render8은 기존 검사 결과 | Source 리뷰/병합 대기 해소. replicas0·Job suspend/current/300초·삭제 보호 유지. 기존 Secret 삭제·Valkey 선언/활성화·실제 Sync는 하지 않음 |
| **팀원 D: Registry** | [D 원 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/14#issuecomment-6016144794): FE/BE Index Digest 보존 복사와 워커2×Image2/default SA Pull4건. Image Source46e21a74는 현재 App main과 구분 | 최종 실행 SA·Pruner 보존·사용창 확인은 직전 확인. Harbor 망 연결/Cloud ECR은 lab 직접 대기에서 제외 |
| **팀원 D/C: lab Valkey** | [Image 원 기록](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6#issuecomment-6014194818)·[TLS 원 기록](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6#issuecomment-6016508869) + D 메시지의 AUTH/Runtime Secret 공급 완료 보고 수신. 선택 DNS lab-redis.seokpan-argotest.svc | **D 초안 작성 → C Data/B Source·권한 리뷰의2안 제안**. D 수락은 미확인. StatefulSet/Service/config Source가 아직 없으므로 DNS/Pod Ready가 아님. AUTH 공급의 비민감 개정·동일 Token 검사 결과는 D가 #6 보완 |
| **내 일: 활성화** | 초기자원 후보/단계 순서 유지 | Valkey 초안에 TLS-only·AUTH·noeviction·저장off/emptyDir·valkey binary·REDISCLI_AUTH+VALKEYCLI_AUTH·restricted UID·Probe/쓰기경로 적용. 같은 App이면 StatefulSet Kind만 AppProject에 제한 허용 검토 → DB/Route/권한/사용창/live Diff 수락 → Valkey1 → 필요한 단일 Migration → BE1 → FE1 → 새Run |
| **병행: ROSA/비용** | Data PR37/SLR 생성 보고 수신 상태 유지 | A/C의 실제 Network 출력/SG2, B Caller/Backend·지원·사양/Volume/LB·기간/가용성, D Cost 보완 → 전체Plan/Cost/실행창. OCP 종료나 모든 복구 자산을 일괄 기다리지 않음 |

기록 정본: [GitOps10 B 후속](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10#issuecomment-6016940121)·[Infra19 B 금고 수신](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6016940538). 제출·수신은 실제 기록으로 갱신하며 답장 초안 작성과 전달 완료를 구분한다.

**10/6 입력에 대한 한정 판단:** 공개키·암호문 공급과 내부 Registry 소비 연결 자체는 목표 플랫폼·엔진·TLS/AUTH·Data 영속성·격리/역할 경계를 바꾸지 않는다. 당시 이 입력만으로 새 아키텍처 변경은 필요하지 않다고 판단했다. 이 판단은 00–04·아키텍처 그림 전체에 남은 불일치가 없다는 전수조사 결과가 아니다. 후속 전체 대조와 발견 사항은 상단 10/7 기록·정합성 조사 대장을 따른다. GitHub Freeze milestone10/18 vs 승인10/16 메타데이터 정정은 별도 미완이다.

### 이전 시점의 기록 — 현재 상태는 위 표 우선


> 기준 2026-10-06 KST: Docs #62 병합·브랜치 삭제와 C lab v1.1 기준 제공을 확인했다. v2.2 Valkey7.2/CA ConfigMap 계약과 OCP 내부 Registry 선택을 수신했다. 10/6 Owner 사용 수락은 확인됐으며 D 노드 자원/NFS 보고는 부분 수신했고 copy/Pull·최소 Data 실입력 뒤 lab 초기1개 시험을 검토한다. ROSA 준비는 병행하고 실제 출력/SG2·Cost PARTIAL/Pool 합의는 남았다.

**초기 Network 검토 이력:** **B Network 소비 검토:** A [Infra #33](https://github.com/seokpan/seokpan-hybrid-infra/pull/33) HEAD `2a5b05bb4b8e8903cfd359f1133c0d7df993d3f4`와 병합 rosa 소비 Source를 대조해 B 범위의 추가 필수 Source 수정 요청0을 [원 답변](https://github.com/seokpan/seokpan-hybrid-infra/pull/33#issuecomment-6008053282)에 남겼다. A의 [수신 답변](https://github.com/seokpan/seokpan-hybrid-infra/pull/33#issuecomment-6008091169)에서 제한 Public3/ROSA Private3·Account/Region·Code SHA/시각을 실제 공급에 반영하겠다는 범위 수신을 확인했다. 이 수신은 실제 값 공급/수락이 아니다. Public3/ROSA Private3 슬롯·CIDR·AZ 쌍과 출력 표현은 현재 계약으로 소비할 수 있다. PR은 A 소유 **Draft**이며 B 답변은 전체 승인/Ready 전환·실제 Output/Plan/Apply가 아니다. C/A의 공통 `onprem_job_host_cidrs` 선언 합의와 VPN ENI/반환 Route 후속은 해당 Data 접근/이전의 조건으로 유지한다. VPN·전체 Data 이전·Backup/OCP 정리를 B 첫 ROSA Plan의 일괄 조건으로 추가하지 않는다.

## 이번 Registry 대응 — 내 일·팀원 입력을 나누어 보기

**최신 기준 v2.2:** [Docs #62](https://github.com/seokpan/seokpan-hybrid-docs/pull/62) main `3dc4f8d637c026a9d86157f5691b7046b85139f1` 19:55:03 KST 병합·해당 브랜치 삭제 확인. Docs59 main `f196a4d`는 이전 병합 이력이다. [C 계약 v2.2](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6014028826) 전체 수신·SHA256 `40f4480d3d6d40d932e0ca7c336c129985010429c6f4cab95de90a688954f509`. Valkey7.2 팀 선택·CA ConfigMap 정정을 수락했으며 현재 Data Source/실제 호환·CA 공급은 별도다. [A 최신 답변](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6013894166)의 VM `/32`·Token 공급 방식·master Secret·시간대 방향은 수신 수락, Root Source 병합은 아래 최신 PR37 기록을 따르고 실제 값/Route/Run은 남았다.

**지금 B가 먼저 할 입력 — Cloud AUTH:** [C 요청에 대한 B 응답](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6015974607)을 기준으로 본인 Controller의 기존 표준 age(X25519) identity 사용 가능 여부를 먼저 확인한다. 사용 가능한 기존 키가 있으면 재사용하고, 없으면 본인 환경에서 준비한 뒤 **public recipient만** C에게 전달한다. 실제 B public key·별도 private identity 보관 확인·복호화는 미확인이다. C는 **Cloud Valkey AUTH 한 파일**을 C+A+B 세 public recipient로 암호화하고 세 사람이 각자 복호화할 수 있는지 확인한다. Backup 데이터·lab CA Key·전체 Cloud Bundle의 보관 역할은 바꾸지 않는다. ROSA 연결은 [Infra25 원 기록](https://github.com/seokpan/seokpan-hybrid-infra/issues/25#issuecomment-6015978789)을 본다.

**팀원 C/A의 Data Role 생성 보고 수신:** [C 원 기록](https://github.com/seokpan/seokpan-hybrid-infra/pull/37#issuecomment-6015927016)에서 배정 A·실제 C가 사람 IAM User `ksh_data`의 personal MFA 세션으로 없던 `AWSServiceRoleForElastiCache`/`AWSServiceRoleForRDS`를 21:02:29/31 KST에 생성했다고 보고했다. Data 서비스 연결 Role 부재는 해당 범위 해소됐으며 Terraform/bootstrap Source는 바꾸지 않았다. 이 Role은 AWS Data 서비스가 사용하는 역할이다. B ROSA 실행/공통 역할·Worker Pull, 실제 Caller/Backend·지원·출력/SG2·Endpoint·첫 Plan/Apply는 별도 확인이다. B public age recipient 준비도 계속 남았다.

**0 Sync 병행:** D가 오늘 수락된 범위/대상·삭제 보호·수행 권한/live Diff를 확인하면 replicas0·Migration 미실행의 Argo 선언/Sync 범위 시험은 Registry 복사·신규 Data Pod·자원 숫자를 기다리지 않고 별도 진행할 수 있다. 승인 실행 선언을 사용하며 진단 artifact/helper guard를 우회하지 않는다. 이 결과는 Pod/업무 PASS가 아니다.

**지금 실행 순서:** D 노드별 자원·기존 FE/BE 관측/Quota·LimitRange 공급 → B의 **lab만** requests/limits 선언 검토 → 선택한 새 lab Redis1(준비 완료 시) → Schema 확인 후 필요할 때 단일 Migration → Backend1 → Frontend1. 새 시험의 최고 사용량은 준비의 선행값으로 요구하지 않는다. D의 노드별 admitted requests+신규 requests가 맞으면 기존 FE/BE는 유지한다. 부족할 때만 D와 비교시험 종료·결과 보존 뒤 자신의 FE/BE 축소 또는 다른 승인창을 정하고 재측정한다. DB/기존 Redis/PVC·4조 객체는 보호한다. 우리 새 workload의 OOM/Pending·노드 pressure·Owner 중단 요청 때 기동 확대를 멈춘다. 실제 적용/시험은 아직 아니다.

**다음 Source:** 수신한 D 자원 보고와 B 후보의 기동 보류 lab 자원 Source는 PR16 병합·브랜치 삭제를 확인했다. Source 준비 대기는 해당 범위 해소됐다. Registry/Data 최소 실입력을 수락한 뒤 별도 활성화를 검토한다. Cloud3HA를 줄이거나 숫자 limits를 추측하지 않는다. Pool 최종 합의 후 B App Source→D 새 Build/Digest가 필요하고, [C lab 기준 v1.1](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6014685336) §5/6의 임의 UID·0440 실제 SCC 읽기 확인·TLS+AUTH exact PONG readiness/liveness없음을 조건부 수락. 기준 제공 대기는 해소됐으며 정확 Image/binary·Service/SAN·CA bytes·두 Secret의 같은 Token 공급과 실제 Run은 D 입력이다. C50m/128Mi 요청·256Mi limit/maxmemory192mb·data/tmp emptyDir256Mi는 D 적격노드 측정 후 lab 후보로 검토하며 OOM 안전 보장은 아니다. Recovery는 선택 binary/TLSAUTH Probe·Storage/UID·전용 CA/Token/새 Digest 공급을 별도로 확인한다. 비용의 Valkey 노드 단가20% 후보는 전체 비용20% 감소가 아니며 D 재계산/현재 PARTIAL·Credit 미차감을 유지한다. 학습 정본은 [§5.11](TJUNG03_WORKFLOW_AND_LEARNING_GUIDE.md#511-이번-학습--팀-결정이-source와-실제-실행으로-이어지는-조건), 기록은 [05 §9.39](05_IMPLEMENTATION_AND_VALIDATION.md#b-v22-internal-registry-bounded-lab-followup-20261006).


**지금 병행할 Source:** [App #13 ECR](https://github.com/seokpan/seokpan-hybrid-app/issues/13)은 실제 ECR 저장소/제한 CI 자격 뒤 E2E, [App #14 Writer](https://github.com/seokpan/seokpan-hybrid-app/issues/14)는 Writer 발급·등록/권한 검증, [App #15 Promotion](https://github.com/seokpan/seokpan-hybrid-app/issues/15)는 [B 범위 확인·구현 인계](https://github.com/seokpan/seokpan-hybrid-app/issues/15#issuecomment-6015110466)에서 실제 Image 키·동반 held Migration·기존 04 §5.4/§10.3 Release 형식과 최초 Image Source46e21 추적 범위를 확인해 게시했다. D는 지금 pure planner/mock·기본 비활성 Source PR을 준비할 수 있고 B는 annotation 파일명/구현을 그 PR에서 리뷰한다. D 수신·Source 패치·실 Writer Run은 미확인이다. 이 Source 준비는 PAT 실수신·OCP 실입력을 기다리지 않는다. 실제 Writer 등록/scope 확인 뒤 같은 실 Branch Push·PR 생성 Run을 #14/#15에 연결해 각각 수락하므로 두 Issue 전체 완료를 서로 선행조건으로 묶지 않는다. 현재 1차 `scripts/promote_gitops.py`를 그대로 2차 자동화 완료 또는 credential-free offline 도구로 보지 않는다. CA 개인 Key의 B 예비 보관은 역할 제안 검토 중이며 보호 Host/실제 사본 수신은 없다. 전체 종료까지의 지도와 남은 메타데이터 예외는 [05 §9.40](05_IMPLEMENTATION_AND_VALIDATION.md#b-current-map-source-parallel-receipt-20261006)를 본다.

**lab 자동화 경계:** 실제 lab Promotion은 D 내부 Registry의 승인 원본↔target Index/amd64 mapping 수신 전 Writer 변경하지 않으며 현재 Harbor 자리는 이력/fixture 범위다.

**AUTH 공급 후속:** [B의 lab v1.1 후속 검토](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6015027863)에서 초기 생성과 회전을 나누고 난수 생성/create/get 실패·빈값/불일치·실제 requirepass를 별도로 확인하는 보완을 요청했다. 초기 공급 검토 후보는 합성 CLI 12조건 중 정상1만 PASS·실패/중단11은 nonzero/임시 파일 정리 확인이며 실제 oc/Secret/TLS 시험은 아니다. 댓글 게시·readback과 C/D 메시지 수신/채택은 구분한다. 이 보완은 해당 AUTH 실제 공급에만 적용하며 Registry Image 복사나 승인된 replicas0 Sync를 막지 않는다.

**D 자원 입력 부분 수신:** [D 자원 입력 정정·공급](https://github.com/seokpan/seokpan-hybrid-gitops/issues/14#issuecomment-6015356358)의 노드별 메모리 예약 여유 worker-1 430Mi/worker-2 145Mi, CPU 4986m/5716m·대상 두 Namespace의 Quota/LimitRange 없음, Registry NFS197G 중 여유191G 보고를 받았다. 기존 5일 최대 working set BE107Mi/FE9.2Mi는 기동 Peak·부하 조건을 보장하지 않고 Migration은 미측정이다. BE Harbor 원본 Index 일치만 확인됐으며 FE·복사/target Digest·노드 Pull은 진행/대기다. [B lab 최초 자원 후보](https://github.com/seokpan/seokpan-hybrid-gitops/issues/14#issuecomment-6015449085)에 초기 수치/단계별 시험을 게시했다. [GitOps PR #16](https://github.com/seokpan/seokpan-hybrid-gitops/pull/16)의 lab-only 자원 Source HEAD `2dc0cabde223fde79c6883169842cbbfed959385`는 21:08:58 KST main `43860c37c7a60b7723f373021d49af08a67c1bc7`에 병합됐고 해당 브랜치 삭제를 확인했다. 기존 로컬 Source39 PASS와 [같은 HEAD Source CI](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37458708031) success/진단 Render 보존은 Source 범위다. replicas0/Job held·300초는 유지하며 Source 병합 이후의 실제 활성화/Run은 대기다. 기존 관측을 새 workload의 안전/기동 PASS로 쓰지 않는다.

**새 원 기록:** [D Registry 원 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/14#issuecomment-6011344271)의 2026-10-06 16:44:49 KST 개정에서 bastion→Harbor TCP443 timeout·Harbor SYN 미도착·lab↔vrouter ping 실패와 임시 route 원복을 보고했다. lab 노드의 직접 경로 검사는 아직 미실행이며 모든 홉의 원인을 독립 확정하지 않는다. 현재 직접 Harbor Pull 경로는 수락할 수 없다. Secret은 인증, CA는 TLS 신뢰, DNS는 주소 찾기이므로 셋만 공급해도 망 연결이 생기지 않는다. 승인 Run3 Image·Final Index Digest·Source 수락은 유지한다.

**진행 판단:** lab은 **기존 OCP 내부 Registry**를 선택한다. [D의 4조 Owner 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/14#issuecomment-6013827433)로 10/6 사용·Argo/내부 Registry/노드 자원 사용 동의를 수신했다. 이후 사용창·연락/중단 담당은 미확정이다. D가 승인 Backend/Frontend Image의 index와 children/amd64를 보존해 복사하고 target Digest·Pull/Trust·ServiceAccount를 확인한 뒤 B가 lab mapping을 연결한다. copy/Pull 성공은 아직 아니다. 직접 Harbor 경로 차단은 기존 관측으로 유지하며 Cloud ECR·Recovery Harbor 역할과 기동 보류/현 guard를 유지한다.

| 구분 | 지금 가능한 일 | 직접 대기·다음 소비 |
| --- | --- | --- |
| **내 일 B** | Cloud AUTH용 본인 public age recipient 준비·C 전달, v2.2 소비 계약/Source·D 내부 Registry mapping·자원 입력 리뷰. 본인 clone·Caller/Backend·지원·가용시각 준비 병행 | 제어 등록: B 권한/대행·Git 접근/live Diff 확인. 10/6 Owner 사용 수락은 수신; 이후 창은 미확정. lab 자원 held Source는 PR16 병합·브랜치 삭제 완료. 초기1개 활성화는 Registry/Data 최소 실입력 수락 뒤 |
| **팀원 D** | OCP 내부 Registry로 승인 BE/FE index·children 보존 복사/target 검증, 전용 nonoverwrite ImageStream tag·pruner/보관·Pull/Trust/SA·실제 NFS 여유 공급 | 100Gi PVC−표시6.1Gi로 여유를 계산하지 않음. NFS197G/여유191G·메모리 예약 여유430/145Mi·CPU4986/5716m·Quota/LimitRange 없음과 기존 FE/BE 관측은 D 보고 부분 수신. 복사/target Digest/노드 Pull·실제 새 workload 결과는 대기, 기동 Peak/부하 조건·Migration은 아직 미측정 |
| **공유 4조·망 Owner / A와 D** | 10/6 미사용·Argo/내부 Registry/노드 사용 구두 수락 보고 수신 | 이후 창·연락/중단 담당 미확정. team4 hello/neuroplan-*/pvc-test-2·nfs-provisioner 보호. 노드 재시작 수반 변경은 직전 재안내하며 현재 Trust 변경/재시작 안 함 |
| **팀원 C/D** | DB/Redis Endpoint까지 lab 노드/App의 실제 경로·CA/TLS/AUTH·목적 Secret·Schema/필요 Migration 공급 | Registry가 풀려도 Data 연결은 별도. Harbor CA와 Data CA를 섞지 않음 |
| **팀원 A/C → 내 일 B ROSA** | A 기반/공통 역할·C Data SG2 공급, B 첫 Plan 준비 | Infra33 main `2c17488f47f377f62444bfc49db5c48bbe7d069a` 병합은 Source 상태. 실출력/SG2·실효 Caller/Backend·지원/비용은 별도. Infra36은 17:59:30 KST main `a332d859416bd2e43a672d663d9ee0e114cafd39` 병합(Source HEAD5b999fb). Network IAM 범위의 [A 보고](https://github.com/seokpan/seokpan-hybrid-infra/pull/36#issuecomment-6013414243)로 bootstrap 복구 Apply2 add/0 change/0 destroy·정책 생성/Role 연결·재Plan No changes를 수신했다. 실제 Network/Full foundation 출력·SG2·ROSA 권한은 별도 대기 |


| 시험 단계 | 지금 준비할 것·직접 조건 | 실제 효과·남는 시험 |
| --- | --- | --- |
| 제한 Project/Root/Child 등록·Repo/Render/Diff | 단일 Owner·수행자·B 권한/대행 범위·4조 사전 공지/사용창 수락·Git 저장소 접근, 정확 Controller/SHA/Path | 필요 시 bootstrap→Root의 수동 Sync로 Child Application 등록. 현재 Child 자동 Sync가 없어 App 8객체 적용/Pod 기동과 별개. Registry·Data·Migration 전체를 이 준비의 선행으로 묶지 않음 |
| Lab 8객체를 replicas0로 Sync | 기존 동명 Deployment/Service/Route/ConfigMap·selector/Route host·Owner·실제 Diff와 수락한 시험 범위 | Pod가 새로 기동하지 않아도 Deployment2·Service2·ConfigMap1·Route3는 실제 API 변경. 기존 App을0으로 줄일 수 있음. 현 진단 YAML/Release helper의 Apply·Sync 금지/거부를 그대로 유지하며 바로 실행하거나 우회하지 않음 |
| Pod 활성화·Pull/Ready·업무 | 수락한 Registry 경로/DNS/TLS/Pull Secret + C/D Data 경로·목적 계정/CA/TLS/AUTH·Schema/필요 Migration + 실제 lab Owner/권한/사용창 | 별도 활성화 PR·필요 단일 Migration·수동 App Sync 뒤 같은 조합의 실제 Run. 등록/Synced/0Replica Health를 Runtime PASS로 바꾸지 않음 |


**내부 Registry 수락 범위:** D가 index/children·amd64 전체 복사와 target Digest, 전용 덮어쓰지 않는 ImageStream tag·pruner/보관 범위, 노드 Pull·DNS/TLS/Trust·Namespace ServiceAccount를 확인한다. NFS 실사용/여유를 실측하며 PVC 용량만으로 사용 가능성을 계산하지 않는다. 현재 Registry 구성·clusterTrust/노드 재시작·이미지 복사는 실행하지 않았다.

**수신 구분:** D가 Context `team4-ocp-lab`·Controller `openshift-gitops`·Namespace `seokpan-argotest` Active/managed-by 일치를 보고한 범위는 환경 설명으로 부분 수신했다. D Caller `system:admin`은 B 권한 확인이 아니다. AppProject default만/Applications 없음도 Namespace의 기존 workload 부재를 뜻하지 않는다. 공유 Owner·수행자/사용창·기존 객체/Diff 수락 뒤 실제 등록 개정을 만든다. 새 Namespace/guard 우회는 추가하지 않는다.

**병합된 후속 Source:** [GitOps PR #15](https://github.com/seokpan/seokpan-hybrid-gitops/pull/15)은 문서 2파일 PR이며 C의 최신 HEAD 승인 후 18:42:19 KST에 main `57c73bea3c01609a90143f7cf7e51d86035e0fc9`로 병합·브랜치 삭제됐다. D의 [02215c8 승인](https://github.com/seokpan/seokpan-hybrid-gitops/pull/15#pullrequestreview-5426097223)은 문서 정확성 범위이며 실제 입력/Runtime 수락이 아니다. 동일 Podman 계정·모드와 실패 결과 기록, 실제 Redis protocol 기록과 중복 설명을 같은 PR에서 보완해 최신 HEAD `cdb77dc3abd99d7321f905d53dfd431d2ea554ef`의 C 리뷰를 수락해 병합했다. [같은 HEAD Native CI](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37441602354)의 Source 검사 39개 PASS·진단 Render 8경로/22객체 생성을 확인했고 최신 C 문서 승인을 확인했다. Pool/Redis 판단의 기준은 [최초 배포 안내](https://github.com/seokpan/seokpan-hybrid-gitops/blob/57c73bea3c01609a90143f7cf7e51d86035e0fc9/handoff/OCP_FIRST_DEPLOYMENT.md)이며 실제 설정 선택·Registry 이동/IDMS 적용은 별도다. 승인 YAML·Image·Guard·Namespace·기동 보류는 그대로다. CI artifact ZIP을 이번에 독립 다운로드·Hash 대조한 것은 아니다.

**앞선 검토/CI 이력:** `02215c823bbbe7e74cabccf54e9a61b81b34f401`의 [Native CI](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37436964045)는 39검사 PASS·8경로/22객체 Render 생성이다. 이전 `db0251baf7283de5529c0bfd43cad82950e8f3b1`의 [Native CI](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37435158422)39검사 PASS·8경로/22객체 Render 생성과6d626c5/Run37434254592·54952bf/Run37433341860은 구 HEAD 이력이다. 당시 main은 fc175a70이며 실제 OCP/AWS/Registry/Image 명령·호환 Run은 미실행이다.

**C v2 전체 파일 수신·B §6 대응:** 제공된 `data-contract-v2-20261006.md`의 §0~7 전체를 읽었다. SHA256은 `8679c46b80b1fe93b2083aea584a47e65cf4882d0c976a7cd9218159fe8f4616`다. [Infra19 v2 원 기록](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6011904645)·[§6 수락 요청](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6011914737)·[GitOps6 연결](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6#issuecomment-6011931355)과 연결한다. C는 원 댓글도2026-10-06 17:14:34 KST에 §0~7 전체로 갱신했다. 최초 공개 조회의 소개/§0 관측은 당시 이력이며 파일/원 댓글 전체 수신·공유는 완료다. 실제 공급값·Run 수락은 별도다.

| C §6의 B 요청 | B 수신·Source 판단 | 내 일 또는 팀 공급으로 남는 실제 확인 |
| --- | --- | --- |
| App Image Alembic head=`20260902_0002` | 승인 Image Source46와 App2003의 Migration2개가 같은 Blob이며 Source head=`20260902_0002` 확인. Cloud import 후 `current` 전제 조건부 수락 | 실제 Run3 Image 자산/명령 확인·C 실제 import/DB `current` 출력은 별도. Source head 확인을 실제 Schema PASS로 쓰지 않음 |
| Valkey7.2 팀 선택·실제 호환 | [C v2.2](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6014028826)의 Cloud/lab/Recovery Valkey7.2 계열 선택을 수락. 기존 bd08 Redis7.1/초기 af8c 요청변경은 이전 이력이다. [Infra PR #37](https://github.com/seokpan/seokpan-hybrid-infra/pull/37) Source 병합 HEAD `4cec3988afaeb8766836b8e589f05b4047e98f76`의 Data Root·Valkey7.2·필수 Token 검사는 정확 HEAD의 [B의 최신 HEAD Source 승인](https://github.com/seokpan/seokpan-hybrid-infra/pull/37#pullrequestreview-5427701443)과 [A 승인](https://github.com/seokpan/seokpan-hybrid-infra/pull/37#pullrequestreview-5427740684) 뒤 20:38:47 KST main `2af2d61f6985ca15dbe8415c84712575f0e92aeb`에 통합됐다. B가 요청한 AUTH 문자/IPv4 검사 2건은 해소됐다. C Branch `infra/19-foundation-data`는 남아 있으며 임의 삭제하지 않는다. 실제 Plan/Apply·Endpoint/SG2 수락은 별도다 | B: redis-py8.1·Lua10모듈/명령29종·RESP3/전체 업무 실제 시험. 기존 redis_version7.2.4 검사를 보존하고 INFO 원문 server_name/valkey_version·AWS 실제 engine/version을 기록. 팀 선택/지원표만으로 호환 PASS 아님 |
| native Endpoint/no CNAME·세션 시간대 미지정 | Source에 `SET time_zone` 없고 게임 UTC-naive/회원 CURRENT_TIMESTAMP 사용을 확인해 조건 수락. RDS `time_zone=Asia/Seoul`·DATETIME±9h 일괄 변환 금지 유지 | A가 Asia/Seoul 통합 방향을 수락. C Root 연결·실제 DB 전역/세션 값은 후속. B: 실제 Client/업무 시각 확인. Endpoint/CA/Secret 실값은 Apply 후 |
| backend Pod/process·Pool/rolling | C v2.2 Engine당 pool3+overflow2는 제안 후보. Engine2·process1이면10/Pod, (활성4+종료1)×10+예약10=60인 시나리오 | B/C: 실제 max_connections·process·종료 중 연결 상한/시간·예약 예산 확정. 현재 Pool 환경변수 소비 없음. 합의→B App Source→D 새Build/Digest→활성화. 60은 전체 최대 보장 아님 |
| Runtime Host=VPC `/20` | Source machineCIDR192.168.64.0/20·podCIDR10.128.0.0/14를 구분하고 VPC SQL Host를 조건부 수락. Worker→Data SG 제한 유지 | 생성 후 B/A/C가 실제 CNI/Egress·DB SQL 출처/Host·SG를 확인. 기본 OVN Node SNAT 가능성을 실제 환경의 성공으로 쓰지 않음. [A 답변](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6013894166)으로 Data VM192.168.52.50/32 확정. 실제 Route/왕복·계정 접속은 후속이며 `%`로 넓히지 않음. |

**이미 받은 공급 계약:** §2.9의 논리 자원6개는 `backend-config`, `backend-db-runtime`, `backend-db-migration`, `backend-redis-runtime`, `backend-database-ca`, `backend-redis-ca`로 명시돼 있다. 현재 Source는 비민감 `backend-config` ConfigMap·목적 Secret3개·공개 CA ConfigMap2개를 소비한다. C v2.2가 CA 공급을 ConfigMap으로 정정해 kind 불일치는 해소됐다. 실제 CA bytes/Hash·대상 kind 대조는 공급 때 확인하며 중복 Secret을 만들지 않는다. RDS 서울 CA Bundle 조건을 수락하되 실제 bytes/Hash는 별도 수신, Redis CA는 생성 후 실제 체인 인계 대기다. 실제 자격/값은 보호 공급하고 공개 댓글에 복사하지 않는다.

**Migration/lab 수락과 직접 대기:** deadline300초·suspended 기본·단일 Job·`db_admin` 전용·기대 Revision 출력 판정을 계약으로 수락했다. Cloud/Recovery는 Image head와 import revision이 맞으면 `current`; lab은 D가 Schema 상태를 확인해 `current` 또는 빈 DB의 `upgrade head`1회를 정한다. Job Complete만으로 Schema PASS/DDL 권한 수락으로 쓰지 않는다. D는 lab DB Service DNS·인증서 SAN/10월26일 이후 유효기간·Schema, 새 TLS+AUTH Redis의 구성/시각·목적 자격·음성 Case5개를 공급/실행한다. 기존 PVC 없는 lab DB의 재시작/삭제 금지는 유지한다. 전체 계약 수신과 실제 CA/Secret/Endpoint·Job/Redis7.1/업무 Run은 별도다. 이미 보고된 Data bootstrap IAM Apply를 다시 대기조건으로 만들지 않는다.

**Cloud 활성화의 직접 조건:** 현재 App Pool 기본값과 Cloud3HA/surge1의 연결 예산은 아직 합의 전이다. C v2.2의 pool3+overflow2 후보도 종료1개 시나리오60이며 실제 max_connections·process/종료 예산 확인 후 B/C가 결정한다. 현0보류·승인3HA Preview를 유지한다. Pool 값을 환경변수에 적는 것만으로 현재 App이 소비하지 않으므로 B App Source·D 재빌드/Digest를 거쳐 별도 활성화한다.

**v2 시점 Redis 지원 범위 검토 이력 — 현재 선택은 v2.2 Valkey7.2:** [AWS engine versions](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/engine-versions.html)는 ElastiCache7.1을 RedisOSS7.0 호환으로 설명하고, [locked redis-py8.1.0 지원표](https://github.com/redis/redis-py/blob/v8.1.0/README.md)는6.0이상 클라이언트의 Redis7.2이상 지원 범위를 적는다. 실행 불가능이 증명된 것은 아니지만 현재 선택을 문서상 지원 조합/호환 PASS로 수락할 수 없다. B/C가 engine/client 지원 전략을 먼저 합의하고 전체 실제 시험을 수행한다. driver 임의 다운그레이드·Valkey 전환·RESP2 강제 변경은 지금 적용하지 않으며 기존8.1 RESP3/응답 동작도 시험 범위에 포함한다. 이 판단은 Cloud App 연결/업무 수락에 해당하며 첫 ROSA Plan·제한 등록·offline Image 검사와 독립이다.

**D lab 부분 공급 수신·B 판단 — 2026-10-06 KST:** [D §6 최신 답변](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6012181426)(17:17:02 KST 개정)을 읽었다. DB Service DNS `mariadb.seokpan-app.svc`, DB 서버 인증서의 같은 SAN·발급자 `seokpan-lab-ca`·서버 인증서2026-10-31 만료 보고를 수신해10/26 이후 조건을 수락한다. CA 인증서의 만료·실제 CA bytes/Hash·Runtime/Migration 목적 Secret·Schema/DB 노드 경로는 별도 공급·실행 대기다. D도 Migration300초를 수락했고 실제 `current`/`upgrade`는 아직 실행하지 않았다.

| 직접 입력/진행 | 지금 수신·결정 | 다음 담당·실제 조건 |
| --- | --- | --- |
| lab MariaDB | DNS/SAN/만료·300초 범위 수신. PVC 없는 기존 DB 재시작/삭제 금지 유지 | D: CA bytes/Hash·목적 자격·합성 데이터 출처·실제 Schema/current·노드 연결. Schema가 비었을 때만 수락한 단일 upgrade1회 |
| lab TLS+AUTH Redis | 현재 사용 가능한 새 TLS/AUTH Redis 없음. 기존 seokpan-app/redis8.10.1은 평문/noAUTH·PVC5Gi이며 demo2 보존. Argo 내부 Redis도 제외 | **D가 lab 구성/실행·공급과 일정을 맡고, B는 선언/restricted UID·읽기전용/쓰기 경로·TLS/AUTH Probe를 리뷰, C는 Data CA/AUTH 계약 확인.** 정확 DNS·CA 발급 주체/기간·ImageDigest/noeviction·Probe·공유 사용 수락은 D 실제 개정 대기 |
| db_admin Runtime 음성 Case | Migration 실제 자격을 Backend Deployment에 공급하지 않음. 승인 Image의 순수 URL 검사 함수에 가짜 db_admin URL을 주고 계정 거부만 확인 | D 기존 cp-03에서 `--network=none --pull=never`·Secret/DB/CA/Settings 없이 실행. 별도 Pod/진짜 자격 공급 없음. 실제 수행/결과는 GitOps6 Run에 기록 |
| 실제 Image Alembic head | 승인 Source head20260902_0002 확인과 Image 내부 자산 확인을 분리 | D cp-03의 승인 Digest Image에서 ScriptDirectory offline `get_heads`로 확인 가능. DB/env.py·lab Registry 연결을 기다리지 않음. 검사안 제공이며 실제 실행은 NOT RUN |

**영향/계속할 일:** D는 lab Redis 구성 주체/일정과 실제 선언·입력, B는 그 개정과 제한 등록 입력을 리뷰하고 Source를 연결한다. 지금 신규 Redis 선언·Namespace·검사 Gate를 만들지 않았으며 기존 demo2/Argo Redis·DB를 수정하지 않았다. 순수 User 거부 Case는 TLS/Ready/GRANT 시험의 PASS가 아니고 offline Image head는 실제 DB revision 확인이 아니다. 자세한 실행안은 GitOps PR15 인계 문서에서 확인한다. 이 수신은 OCP Registry 차단·실제 Secret/Data/Owner 수락을 해소한 전체 배포 완료가 아니다.

**17:27~17:30 KST 추가 수신 이력 — 현재는 위 v2.2/lab v1.1 기준 우선:** [C v2.1 후속](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6012401242)에서 lab Redis 설정 원칙을 받았다. C는 complete `redis.conf`·인증서 조건·Probe 실행 기준을 **10/7 오전 제공 예정**이며, D가 인증서 발급/Kubernetes 구성·배포·시험을 맡고 B는 소비 선언·임의 UID/쓰기 경로·TLS/AUTH Probe를 리뷰한다. C의 `port0`, server TLS+별도AUTH, noeviction·저장off/emptyDir·Key0440·AUTH 환경변수/TLS execProbe 원칙은 수신했고 완성 공급/실행은 아직 아니다. D가 Service 이름을 정해 SAN에 `.svc`/`.svc.cluster.local` 두이름을 넣고 소비 Host를 하나와 정확히 맞춘다. Redis7.x 권장은 정확 version/digest 공급이 아니며 Cloud7.1/client8.1 지원 전략·실제 호환 대기는 유지한다. 같은 Recovery 설정 원칙도 환경별 CA/Token/DNS를 섞지 않고 적용한다.

**D의17:30 읽기 보고:** [GitOps6 현재 카드](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6)에서 대상 Namespace의 기본 SA/CA 외 객체 없음, Quota/LimitRange/NetworkPolicy 없음·default Project의 넓은 허용·Applications0·Controller 정상 보고를 수신했다. D Caller system:admin과 B 권한은 별도이며 실제 적용 직전 Owner/권한/사용창·선택 범위/live Diff 수락을 유지한다. D는 CA CN seokpan-lab-ca의 만료도2026-10-31 05:54:12 GMT로 보고했다. 이는 추가 CA metadata 보고이고 CA bytes/Hash·TLS 독립검증 완료가 아니다. DB서버 인증서와 CA 만료를 같은 관측으로 합치지 않는다. 기존 demo2/DB/평문Redis/PVC·Argo 내부Redis를 변경하지 않는다.

**기록·전달·수신 구분:** Registry 판단은 [GitOps14](https://github.com/seokpan/seokpan-hybrid-gitops/issues/14)·[10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10)에 작성했다. 18:44:47 KST 전달 확인으로 Registry·Data·최신 비용 답장 3건의 전달·수신은 완료됐다. 이번 전달 확인에 따라 C·D 메시지 2건은 전달 완료, 두 메시지의 수신·응답은 미확인이다. 앞선 18:44:47 KST의 3건 전달·수신 완료와 구분한다. 4조의10/6 사용 수락 보고는 받았고 이후 사용창·연락/중단 담당·노드 재시작 수반 변경 재안내는 별도다. C 계약 B5 응답은 [Infra19](https://github.com/seokpan/seokpan-hybrid-infra/issues/19)에 기록한 부분 수락/보완이며 Runtime 수락이 아니다. [Docs43](https://github.com/seokpan/seokpan-hybrid-docs/issues/43)의 개정 원장 독립 감사 피드백은 D 수신 확인까지 완료됐으며 수식 보완·Cost Gate PASS는 남았다.

**OCP 확인 순서:** [GitOps #14](https://github.com/seokpan/seokpan-hybrid-gitops/issues/14)의 B 응답에서 Registry 후보/공유 Owner 입력을 확인 → [GitOps #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10)의 단계별 준비/수락 → [#5](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5) 등록·Sync와 [#6](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6) Pull/Data/업무 결과를 구분한다. 학습은 [§5.10](TJUNG03_WORKFLOW_AND_LEARNING_GUIDE.md#510-이번-학습--git-선언-적용과-image-pull은-서로-다른-경로다), 기록은 [05 §9.38](05_IMPLEMENTATION_AND_VALIDATION.md#b-lab-registry-path-and-sync-scope-20261006)를 본다. 이번에는 실제 공지·등록/Sync·Registry 복사·망 변경·AWS 실행을 하지 않았다.

**이전 상단 기준의 시점 이력:** 기준 2026-10-06 KST: 개정 비용 원장을 수신해 실제 계산 엔진으로 독립 재검증했다. 현재 PARTIAL과 남은 수식 보완을 원 Issue에 연결한다. 아래 #33 Draft/2a5 검토는 당시 이력이고 최신은 Ready/062a371이다. 실제 출력·가동 시각·본인 가용성은 미확인이다.

</details>

## 2026-10-08 작업 묶음 — Docs #88 이후

- [x] 정책 사본 권한·17개 파일 해시 수신, Docs #88 병합·브랜치 삭제 확인
- [x] [새 Image Source·스키마·ZIP·ROSA 준비 연결](IMAGE_MIGRATION_ROSA_PREFLIGHT_20261008.md)
- [x] [1차 쓰기 중지·복귀 준비 절차](FIRST_SERVICE_WRITE_STOP_PREPARATION.md)
- [ ] D 새 공급 Issue·Build/Scan/Digest·내부 Registry mapping·신규 Pull/교체 창 수신
- [ ] B 실제 1차 Context·Parent/HPA/쓰기 주체 확인 → 제어 경로·실행자/창 수락
- [ ] B/C 이관 당일 쓰기 중지 유지·최종 Dump/Import/비교 → ROSA current/App 검증
- [ ] B Controller clone/Lock·Operator/정책 대조 → A 보호 수신·실제 기반/권한·C/A SG2
- [ ] B/A/D 목적 Caller/Backend·지원/구독/Quota/disk·예비 비용/창 → 첫 전체 Plan

실제 수행/수신은 원 Issue/Run에서 판정. 다중 투표·WS 유지/재접속·Rolling/장애·Prune/Delete, Recovery·금고 독립 사본 및 보존 중인 개인 변경은 기존 후속 범위 유지. 멘토링/OADP는 보류.

## 2026-10-08 직접 결과 이후

- [x] 실제 Operator6개/보관정책ID대조·Core1.16.4·origin/개인변경 결과 수신
- [x] 개인App2/GitOps2수정의최신main통합·App30/GitOps33 정확HEAD Linux CI 확인
- [x] D32새공급Issue·추가진단ZIP일치·PoolSource예산 확인
- [x] Controller Source/Lock·격리 validate/교정 mock·지원후보 목록 및 A 정책 사본 수신 보고 확인
- [x] App30/34·GitOps33 승인/병합·PR 브랜치 삭제, 기본 IAM User 인증·본인 MFA 장치1개 읽기 확인
- [x] B 개인 Caller 서울 사양/Quota 부분 읽기·D32 새 Source18819963 Run5 보고 수신 및 공급 후보 수락
- [ ] 지금 가능: EC2 첫호출 오류 진단, D 보존 참조/내부 공급·mapping 준비와 Owner 사용창 조율
- [ ] 선행 입력 대기: A 실제 역할/권한/제한 기반/Backend·C/A SG2·프로젝트 계정/지원/Quota/disk·예비 비용/Owner/창 → 첫 Cloud Plan
- [ ] 실행 조건 수락 후: 새 Image 수락·OCP 최신 자원/Owner 창·실제 교체/시험

[연결](CONTROLLER_SOURCE_CATALOG_FOLLOWUP_20261008.md). 기존독립작업의잔여와멘토링보류 유지.
