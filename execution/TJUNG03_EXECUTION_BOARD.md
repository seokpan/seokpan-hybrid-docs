# 정태훈 실행판 — 지금 할 일·입력 대기·OCP와 ROSA 수명

> 기준 2026-10-06 KST: Docs47·C50의 최신 기록과 App8 기존 B 승인/병합·D 첫 Run 실패/비용 수신·단계별 ROSA 권한 준비를 현재 입력/행동에 연결한다. 승인 설계/역할/목표 창은 유지한다. 본인 환경·Cloud 실제 Run/지원·권한 확인 완료가 아니다.

**마지막 팀 변경:** **B Network 소비 검토:** A [Infra #33](https://github.com/seokpan/seokpan-hybrid-infra/pull/33) HEAD `2a5b05bb4b8e8903cfd359f1133c0d7df993d3f4`와 병합 rosa 소비 Source를 대조해 B 범위의 추가 필수 Source 수정 요청0을 [원 답변](https://github.com/seokpan/seokpan-hybrid-infra/pull/33#issuecomment-6008053282)에 남겼다. A의 [수신 답변](https://github.com/seokpan/seokpan-hybrid-infra/pull/33#issuecomment-6008091169)에서 제한 Public3/ROSA Private3·Account/Region·Code SHA/시각을 실제 공급에 반영하겠다는 범위 수신을 확인했다. 이 수신은 실제 값 공급/수락이 아니다. Public3/ROSA Private3 슬롯·CIDR·AZ 쌍과 출력 표현은 현재 계약으로 소비할 수 있다. PR은 A 소유 **Draft**이며 B 답변은 전체 승인/Ready 전환·실제 Output/Plan/Apply가 아니다. C/A의 공통 `onprem_job_host_cidrs` 선언 합의와 VPN ENI/반환 Route 후속은 해당 Data 접근/이전의 조건으로 유지한다. VPN·전체 Data 이전·Backup/OCP 정리를 B 첫 ROSA Plan의 일괄 조건으로 추가하지 않는다.

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

이번 이슈 탐색 감사와 직전 안내 검토는 [05 §9.24](05_IMPLEMENTATION_AND_VALIDATION.md#b-issue-navigation-audit-20261005)에 기록합니다. 기존 범위에서 B의 마지막 정리까지 연결되어 있어 새 중복 이슈는 만들지 않았습니다.


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

**B는 지금 착수할 수 있다. A 전체 업무 완료를 기다리지 않는다.** D Run3 Image 제공과 B 개정 수락은 확인됐다. Lab/Recovery Source 리뷰·실제 Namespace Secret/Data/Owner 준비와 활성화 뒤 OCP Workload Pull/Ready/업무, A/C 실제 제한 Output/SG2·B 목적 Caller/Backend/비용·ROSA 실행은 후속이다. OCP 정리를 ROSA 시작의 일괄 조건으로 추가하지 않는다.

**현재 B 작업 묶음:** [D Run#3](https://github.com/seokpan/seokpan-hybrid-app/pull/10#issuecomment-6009053898) SUCCESS·Harbor-only·`linux/amd64` 보고와 FE/BE Final Index Digest를 [B 수락 답변](https://github.com/seokpan/seokpan-hybrid-app/pull/10#issuecomment-6009213599)에서 제공 개정으로 수락했다. App Source는 `46e21a74dd608b41f2c12a0a57d76bddfcf25949`, Final tag는 `git-46e21a74dd60`다. 초기 frontend Alpine 경고는 최신 D 스캔 정정으로 공급 대기에서 해소했다. Private Harbor 원본 metadata/bytes를 B/AI가 독립 조회한 것은 아니며 cp-03 Podman Pull/Smoke 보고도 OCP Workload Pull/Ready 판정과 구분한다. [GitOps PR #13](https://github.com/seokpan/seokpan-hybrid-gitops/pull/13)은 D의 [e757 비차단 승인 이력](https://github.com/seokpan/seokpan-hybrid-gitops/pull/13#pullrequestreview-5424225335) 뒤 README/인계 카드 2문서만 같은 PR에서 보완했다. 구승인은 현재 `DISMISSED`다. 현재 HEAD `c798ed28d516533d5ffb984ad58332e3a5e5829d`·[Source CI #40](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37420661610) SUCCESS·39개 검사 통과(skip0). [보완 답변](https://github.com/seokpan/seokpan-hybrid-gitops/pull/13#issuecomment-6010256873)에 대해 D 재검토 요청 완료·A/C 요청 유지다. 최신 PR은 `mergeable=true`/`blocked`이므로 새 HEAD 재승인·병합 가능 상태 확인이 남았다. 보호규칙 세부는 조회되지 않아 승인 해제/차단의 설정 원인을 단정하지 않는다. 제안은 명시적 비차단이며 실환경 Pull 완료를 Source 병합 선행 조건으로 추가하지 않는다. Lab/Recovery FE·BE 및 held Migration에 제공된 Final Index Digest를 연결하고 Lab `lab-harbor-pull` 참조를 추가한다. Recovery `recovery-harbor-pull`은 유지한다. App replicas0·Migration suspend/current·기타 INPUT_REQUIRED·Cloud ECR 보류는 그대로다. Image 제공·개정 수락 대기는 해소됐다. B는 Source PR 리뷰/병합 뒤 D와 대상 Namespace의 실제 Pull Secret 공급·Context·권한·단일 Owner, C/D Data·CA/TLS/AUTH·Schema/필요 Migration 준비를 수락한다. 그 뒤 별도 활성화 개정·필요 단일 Migration·수동 Sync를 수행하며 해당 Job/Pod의 Workload Pull·Ready/FE/API/WSS/대표 업무 Case를 같은 조합으로 확인한다. 선언의 Digest/Secret 이름만으로 실제 실행을 완료 처리하지 않는다. ROSA 준비는 Infra25에서 병행한다. [05 §9.36](05_IMPLEMENTATION_AND_VALIDATION.md#b-image-receipt-held-source-pullsecret-20261006)·학습 안내 §5.8을 본다.

| 실제 위치/원본 | 이번 결과 | 직접 막힌 실행·다음 행동 |
| --- | --- | --- |
| App2/PR10 → GitOps10/5/6 | D Run3 SUCCESS·Final Digest·최신 Scan 보고 수신/B 개정 수락. Lab/Recovery held Source 연결 | Source PR 리뷰/병합 → D Namespace Secret/Owner + C/D Data·Schema 준비 → B 활성화/수동 Sync → Workload Pull·Ready/Case |
| rosa 목적 Role 수요·Infra20/25 | PR35 A 재승인·병합, 정상 Get/조건부 Update 수요 확정 | 첫 Plan용 조회·State 정책/Caller·Backend·필수 Output/SG2/지원 수락 → 첫 Plan. 생성/Update/삭제 검증·조건부 ListTags 호출/미발생 기록은 해당 단계 |
| B Infra25 ↔ D Docs43 | D 수신·기간/Credit 수정 보고 확인. 새 xlsx 검증아님 | CP/Infra서비스구성·Worker disk·LB예상목록·예상/실제시간/삭제 입력. 가용성 별도실행창TBD |

**지금 확인할 결과:** Docs52 병합·브랜치 삭제, D Run3/Image·최종 스캔 정정 보고와 B 개정 수락을 확인했다. [GitOps PR #13](https://github.com/seokpan/seokpan-hybrid-gitops/pull/13)은 D의 [e757 비차단 승인 이력](https://github.com/seokpan/seokpan-hybrid-gitops/pull/13#pullrequestreview-5424225335) 뒤 README/인계 카드 2문서만 같은 PR에서 보완했다. 구승인은 현재 `DISMISSED`다. 현재 HEAD `c798ed28d516533d5ffb984ad58332e3a5e5829d`·[Source CI #40](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37420661610) SUCCESS·39개 검사 통과(skip0). [보완 답변](https://github.com/seokpan/seokpan-hybrid-gitops/pull/13#issuecomment-6010256873)에 대해 D 재검토 요청 완료·A/C 요청 유지다. 최신 PR은 `mergeable=true`/`blocked`이므로 새 HEAD 재승인·병합 가능 상태 확인이 남았다. 보호규칙 세부는 조회되지 않아 승인 해제/차단의 설정 원인을 단정하지 않는다. 제안은 명시적 비차단이며 실환경 Pull 완료를 Source 병합 선행 조건으로 추가하지 않는다. 실제 OCP Workload Pull/Ready·Data/Migration/업무, Recovery Redis TLS/AUTH/Storage/임의 UID/T18, ROSA ECR·본인 Caller/Backend/Plan/Cost는 별도다. 기존 진단 자료/체크·C 기록은 유지한다.

**보고 형식 유지:** 목적·저장소/파일·이번 결과/한계·관련자/연계·막힌 직접 입력·핵심 동작·B 다음 행동을 짧은 카드/표로 함께 설명한다. 상단 전체 현황·하단 전체 남은 작업을 유지하며 첫 회 전체 개요는 반복하지 않는다.

**최신 수신 자료:** [병합 main Native Run 37330480298](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37330480298)의 정확 main39 PASS·Source clean과 artifact11353184732의 11파일/YAML8 Hash·main/Tree·보류·Secret0 검증을 완료했다. `ocp-source-handoff-6ea2d9a90ab7c58803767220abf956d3c1b54a5f`를 **10/13 00:09:31 KST** 만료 전 별도 보존·수신하며 원 제출/요청은 [원 댓글](https://github.com/seokpan/seokpan-hybrid-gitops/pull/12#issuecomment-5998279839)이다. 이전60bda/10/12 안내는 당시 이력이다.

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

## 2 다음 작업 구간에서 B가 할 순서

| 우선 | B의 구체적인 행동 | 남길 결과/관련 담당 | 기다리는 범위 | 원본·TH |
| --- | --- | --- | --- | --- |
| 1 | 본인 clone의 HEAD·개인 변경을 보존하고 App/GitOps/Infra 병합 SHA·도구를 읽기 확인 | 본인 환경에서 확인한 전체 SHA·변경/도구·확인 시각. 에이전트 복원 공간 결과와 구분 | A/C/D 전체 완료 대기 없음. 본인 PC 접근 확인만 본인 수행 | Docs21, TH01/02 |
| 2 | 병합 #12의 최신 main artifact를 별도 승인 경로에 보존하고 ZIP/Hash·Source 개정 수신 기록 | 만료10/13 00:09:31 KST 전 보존 위치/개정·수신/보완. GitOps10↔D GitOps5/6 | Source PR 리뷰/병합 대기 해소. ZIP 직접 수신/보존은 아직 기록 미확인 | GitOps10/5/6, TH08 |
| 3 | D의 AppSHA→Build/Scan/Digest/Pull·lab Owner/권한, C의 DB/Redis/TLS/CA/Secret/Schema·Migration 보호 공급 개정 대조 | 제출·수신/보완·실입력 수락 범위. 값/Token/Key 원문은 공개하지 않음 | 실제 공급 개정을 쓰는 시험만 대기. 필요한 입력/Case 대조는 지금 가능 | App1/2·GitOps5/6/10, TH03~08/14.1 |
| 4 | 최소 입력 수락 후 별도 lab 활성화 PR에서 Replica/Digest·Renderer/보류 검사 함께 검토 | 같은 BE Digest/Config·필요 Schema/단일 Migration 수락 → D/B/C 수동 Sync·동일 조합 새 Run | 현재 보류 artifact는 실행용이 아님. 실제 Image/Context/Data/Migration 수락 필요 | GitOps5/6/10·App1/4, TH08.4 |
| 병행 A | OCP 결과와 Cloud/Recovery 차이·Secret/관리/Bundle·다중 Pod/업무 Case 준비 | Owner/보호 공급/환경 차이·수락/재시험 범위 | 실제 적용만 해당 입력 대기. OCP/ROSA 전체 종료 대기 없음 | GitOps10·App4, TH09/11/15 |
| 병행 B | ROSA 로컬 안내로 본인 clone/Lock·도구·Caller/Backend·서비스 권한/지원·A/C 출력 대응 확인 | Infra25↔A Infra23/20·C Infra19·D Infra18의 실제 입력/준비 수락표 | 안내 문서 검토와 실제 Plan은 별도. 실제 보호 출력/목적 권한·지원/예비 비용 수락 후 첫 Plan | Infra25, TH10~12 |

전체 Cloud Root/NP/UWM/완성 Recovery Bundle를 모두 끝내야 첫 OCP Sync를 할 수 있다는 일괄 조건은 만들지 않는다. 기존 OCP의 승인 Project/Application을 쓸 수 있으면 그 시험의 직접 Source·Owner·권한·입력을 확인해 최소 조합부터 검증한다. 공통/Cloud 전체 선언의 남은 범위는 병행해 완료한다. 공유 환경 소유/권한 가능 여부는 실제 Owner 확인이 필요하다.

## 3 B를 막는 입력은 실행별로 다르다

| 보류 중인 실행 | 최소 직접 입력 / 공급 책임 | 입력을 기다리는 동안 계속할 B 작업 | 완료 확인 위치 |
| --- | --- | --- | --- |
| **OCP 최초 App Sync** | D: 새 App Source의 사전검증용 Harbor Image·Scan/Digest/Platform/Pull·Context/Namespace/공유 Operator/실효 권한. C/D: lab DB·Schema·직접TLS/CA·Redis TLS/별도AUTH. B: 해당 선언/Secret 공급·Migration·초기 활성화 | 선언·Render·Case·인계와 Cloud/Recovery/ROSA Source 준비 | GitOps5/6의 동일 조합 새 Run·D 결과/B 수신 |
| **실제 rosa Plan** | A: 실제 필수 기반 출력/개정·Backend/목적 실행 Role. C: Data SG 의미 검토. B: Controller/정확 Caller·서비스 권한·지원/Quota·입력 대조. D/B: 사전 비용/창 리뷰 | PR28 Source/Schema/리뷰·Controller 준비, OCP·Secret·Bundle Source | Infra25와 원 보호 Plan/리뷰 참조 |
| **유료 ROSA 생성** | 최신 Source/실입력의 보호 전체 Plan·리뷰, 실제 지원/권한/Quota, D 전체 비용($450 계획/$500 한도)·기간/삭제/재시험/잔존·단일 실행자·구체적 실행 동의 | lab 실패 수정·Cloud 승격 조합 준비·관리/Secret Case | Infra25·Cost/Shared Execution·실제 생성 Run |
| **ROSA 최초 App 배포/E2E** | 실제 Cluster/Worker SG→Data Binding, 실제 C RDS/Redis Endpoint·목적 계정/CA/TLS/AUTH/Schema, D ECR Image/Worker Pull, B Root/Cloud Secret·Migration/Host/Route | App/선언 결함 수정·E2E/관측·복구 자산 구성 | 해당 원 Issue와 Run/Index·인계 수신 |
| **격리 로컬 전체 T18** | A: 승인 격리 Host/공간/Storage. C: 실제 검증 Backup·로컬 완성본/Hash·독립 Key/CA·복원. D: 보존 Harbor Image/Scan/Mapping·시간선. B: 복구 Render/도구/FE/API/WSS/업무 계약 | Bundle 목록/Render/Case·부분 예행 검토·코드 준비 | Infra17/App4·T18 새 Run·C 검토/D Index 수신 |
| **초기 관리자 회수** | 정상 개인 관리·Argo 권한과 유지 비상 경로 실제 성공, 신규/기존 Token·Session 회수 Case | IDP/RBAC/공급 선언과 Case | 실제 환경별 Run·B/A 리뷰 |
| **중간/최종 rosa 삭제** | App 쓰기/진행상태 보호·Backup 로컬완성·Release/Bundle/Key/영상 접근·Binding 해제·범위/비용/인계 | 삭제/보존 목록·Runbook·발표·증거 정리 | Infra25·T19/T20·실제 삭제/잔존 기록 |

OCP용 Harbor 사전검증을 ECR+Harbor CI E2E나 최종 Cloud Release 완료로 표시하지 않는다. ECR이 아직 없어도 해당 lab Image/보호/승인 경로로 OCP 사전검증을 준비할 수 있으며, ECR/Worker Pull과 양쪽 Registry 실제 검증은 별도로 남긴다. 현재 기록에 새 Image/입력이 없다는 것은 공급 완료 미확인 상태이며 서버에 없다고 직접 관측한 뜻이 아니다.

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
| TH-07.4 | 입력대기: D 새Image/RegistryDigest·Platform·Scan수신 | D 실제Build/Registry입력, GitOps6결과 | [h-app Issue #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4) Image 수신 |
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
| TH-17.4 | 후속실측: B실제Run→Index/D집계 | D 수신확인·팀전체PASS대필금지 | [h-docs Issue #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21) B 수행 집계 |
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
- [ ] **D Image/OCP:** 새Harbor사전Image/Scan/Digest/Platform·labContext/권한/Owner·같은조합Sync/Client/업무/삭제보호·Run/수신·실습정리
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
