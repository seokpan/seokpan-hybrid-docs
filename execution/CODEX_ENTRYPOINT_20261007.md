# 구현·검증 실행 인계 — 2026-10-07

> **최신 조사 후속 — 2026-10-07:** [전수 조사](REPOSITORY_AUDIT_20261007.md)·[05§9.47](05_IMPLEMENTATION_AND_VALIDATION.md#repository-full-audit-20261007) 참조. GitOps main의 Root SHA B/FE·BE1은 소스 병합 상태이며, 마지막 수신 Runtime은 SHA A/FE·BE0이다. 성공한 등록/선택Sync·금고 본체 확인을 반복하지 않는다. C의 GitOps26/6038214247 DB 형식·GRANT·TLS 접속·합성 출처 수락 보고는 수신했고 실제 Stage2 적용·Route/업무는 원 #26에서 후속 확인한다. 아래 시점별 인계 보존.

> 목적: 승인 설계와 최신 Source를 유지하면서 구현·검증을 다음 작업 환경에서 이어간다.
조회는 저장소별 시각을 구분하고, 시작 시 아래 SHA 이후 변경분을 확인한다.
> 원 작업: [Docs #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21)·[인계 PR #72](https://github.com/seokpan/seokpan-hybrid-docs/pull/72). 상세 실행 카드는 [WORK_HANDOFF_20261007.md](WORK_HANDOFF_20261007.md).

- [x] 첨부 NextInputs ZIP 무결성 확인: CRC 정상, SHA256 항목12개 일치
- [x] 2차 저장소4개와 현재 Source·Issue/PR·댓글·리뷰·Branch·Commit·Run 대조
- [x] 첨부 이후 병합된 App·GitOps·Infra 변경과 현재/과거 지시 구분
- [ ] 이 PR 최신 변경의 팀 검토·병합과 다음 실행자의 인계 수신
- [ ] 본인 보호 환경·독립 키 사본·직접 입력·실제 실행 및 시험

## 1. 첫 작업에서 읽을 순서

1. 사용자가 제공한 `PROJECT_INSTRUCTIONS.md`와 개인 실행계획을 먼저 읽는다. 두 파일은 Project 보조 소스이며 저장소와 자동 동기화되는 파일이 아니다. 이 요청에 제공된 지침은10/7 v3다.
2. 본 문서→[실행 인계 W01–W13](WORK_HANDOFF_20261007.md)→[실행판](TJUNG03_EXECUTION_BOARD.md)→원 Issue/PR의 최신 댓글을 읽는다.
3. 해당 작업에 필요한 승인 설계03·준비04 절과 실제 코드·검사·Lock을 읽는다. 00은 역사적 출발점, 03/04 문서 종료와 Runtime 완료는 별개다.
4. `git status`와 원격 변화·개인 변경·미병합 PR을 확인한다. 기존 clone/Branch/State/키를 초기화하지 않는다. 전체 저장소의 변경 목록은 작업 묶음 전후 확인하고, 의미 검토는 영향받는 파일·입력·시험·인계로 확장한다.

프로젝트 대화·Project 파일·개인 Key·VPN·kubeconfig·실제 보호 입력이 다른 작업 환경으로 자동 전달된다고 가정하지 않는다. 이번 첨부는 원 CI Artifact/Render/Harness의 부분집합이므로 원 SHA와 Run을 참조한다. Backend1752와 중복 runner47을 합산하지 않는다.

## 2. Source 기준선과 최신 변화

| 저장소 | 조사 기준 main | 현재 의미 |
|---|---|---|
| App | `a2afffb8605dafff1cb5b9af215aa0cf93aadcdb` | #17 startup 취소 정리, #18 Lua 거부 전 쓰기 방지, #19 PubSub 구독 취소 정리 병합. 실제 배포 Image는 별도 Build/Scan/Digest 인계 필요 |
| Infra | `36dc2403aa77e2896cc4ec3c545b92e0afb49205` | #39/#42 병합. Backup 일반 경로 periodic/ 및 변수명 변경. 실제 foundation/rosa Plan·Apply와 제한 출력은 별도 |
| GitOps | `a25172c7453b9d7999cb1f3cbeb1ef35774e3b63` | #19 Valkey 선언, #20 등록 검사, #22 Stage1, #24 등록값 Source 병합. D의 등록·Valkey 선택 Sync 성공 보고 수신. TLS/AUTH/Hostname·삭제 보호 및 전체 Ready 수락은 별도 |
| Docs | `a9b0207b563aa25be17d4a635f6cc903fbe0e74a` | #63/#64/#67/#68/#69/#71/#74/#75/#77 병합. C 최신 공급 기록을 보존한 #72 인계 갱신은 검토·병합 대기 |

현재 GitOps **Valkey Stage1 SHA A는 `244b48b885d7ac645c402e561a032ae65a8f3461`**다. 실제 등록 Source의 targetRevision과 대조한다. 이동하는 main이나 등록 Manifest 자신의 SHA로 대체하지 않는다. lab Valkey1·FE/BE0·Migration suspend이며 base/Recovery의 보류는 유지한다. `source-reviewed-runtime-unverified`는 Runtime PASS가 아니다.

현재 복호화 기록: C의 jth Valkey 금고 성공 보고와 B 수신, 이어 [SQL 금고의 B 확인](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6033157659)이 있다. 완료한 공개키 전달·본체 복호화를 다시 요구하지 않는다. **Controller 밖 독립 매체·복원 Identity 검사만 별도 미완료**다. 이 인계 작업에서 비밀값이나 실제 Controller를 재조회하지 않았다.


### 조사 중 추가된 실행 보고·수정 PR — 2026-10-07 후속 조회

[D 등록·선택 Sync 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5#issuecomment-6034601393)는 SHA A의 Valkey 4객체 `Succeeded`·FE/BE 미생성을, [Pod 확인](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6#issuecomment-6034590906)은 검토 Digest의 amd64 하위 ImageID·허용 UID만 보고했다. 등록/Sync를 다시 미실행으로 되돌리지 않는다. 실제 TLS/AUTH/Hostname·Ready 전체 Run과 Prune/Delete 차단은 아직 근거가 없으며 공유 Owner 재확인·등록 Commit·B 공유 시각의 빈칸 및 사전 합의되지 않은 `oc patch operation.sync.resources` 경로는 원 #5에서 보완·수락한다. #21의 완료 체크만으로 이 잔여를 완료 처리하지 않는다. 이 조사자는 클러스터를 직접 재조회하지 않았다.

현재 GitOps main의 [CI 37595556200](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37595556200)는 #24 등록값과 이전 checker allowlist 불일치로 실패했다. [Draft #25](https://github.com/seokpan/seokpan-hybrid-gitops/pull/25)는 checker/test/안내 3파일의 정합 수정이며 동일 도구에서 69검사·8 Render/26객체·고정 SHA 비교 PASS이며 [정확 PR HEAD6064311의 CI37598576166](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37598576166)도 completed/success다. 이는 미병합 PR의 검사이고 현재 main의 기존 CI 실패는 유지된다. Controller/Workload YAML과 실제 상태는 변경하지 않았고 main에 아직 병합되지 않았다. 전체 release Gate·공유 충돌·Prune/Delete 보호는 보존한다.

[Infra Draft #43](https://github.com/seokpan/seokpan-hybrid-infra/pull/43)은 ROSA `workspace_key_prefix=phase2/rosa/env`와 목적 Role의 List 범위를 맞춘다. default State Key는 유지한다. 기존 harness/보존 검사 PASS, 보조 로컬 fmt/validate는 NOT RUN 이력이다. [정확 PR HEADd5aeddd의 CI37598580155](https://github.com/seokpan/seokpan-hybrid-infra/actions/runs/37598580155)는 Core1.16.4/AWS6.67.0/RHCS1.7.7의 fmt·backend=false/readonly init·validate(errors0/warnings0)·Schema13종·OIDC mock2·Source/Lock 불변 PASS다. 실제 Backend 인증·Workspace 조회·Cloud Plan/Apply는 NOT RUN이다. 누락만으로 기존 init 실패를 단정하지 않는다. 검토·병합 후 본인 clone/Workspace와 실제 Caller/Backend를 확인한다.

[GitOps #26](https://github.com/seokpan/seokpan-hybrid-gitops/issues/26)은 후속 조회에서 Stage2의 실제 추적 Issue로 확인됐다. [D의 backend-db-runtime 공급 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6#issuecomment-6034843156)는 두 URL 키·계약 Host/DB 이름과 기존 lab 계정 비밀번호 공유를 명시한다. Secret 미공급으로 되돌리지 않되 실제 새 URL 접속·C 형식/GRANT·데이터 출처 수락은 대기다. Route/Origin·새 Backend Image·Stage2 활성화/전체 Gate도 미완료다.

첫 읽기·작업 위치·실행 조건은 [실행 인계](CODEX_ENTRYPOINT_20261007.md)를 따른다. 원 보고와 이 Source 수정의 수신/검토·실행은 별개다.

## 3. 실행 위치 판단

소스 수정·검사는 로컬 PC 또는 격리 원격 환경에서 진행할 수 있다. 실제 금고·lab·ROSA 실행은 기존 승인 Controller·본인 보호 Workspace와 지정 계정/사용창에서 진행한다.

| 작업 | 우선 위치 | 직접 조건 |
|---|---|---|
| Source 수정·정적 검사·Render·PR 검토·합성 예행 | 로컬 PC 또는 격리 원격 환경 | 정확 Repo/SHA·도구·Lock·격리 환경. 실제 Credential 불필요한 범위부터 진행 |
| 본인 금고·키 보관·Secret 공급 | 승인 Controller의 본인 계정과 독립 보호 매체 | 값 없는 결과, 키/Token의 화면·argv·history·로그 노출 방지 |
| lab 등록·선택 Sync·실제 업무 | lab 접근 가능한 기존 승인 실행 위치 | D/공유 Owner의 실제 실행 범위·사용창·권한·live Diff. B는 Source/경계 리뷰 |
| ROSA 실제 Caller/Backend·Plan/Apply/삭제 | B의 승인 보호 Workspace/Controller 접근 흐름 | 개인 MFA/STS·목적 Role·같은 Backend/Provider Caller·RHCS 인증·A/C 입력·지원/비용/실행창 |
| 전체 Offline Recovery | 승인 On-Prem 복구 Host | 사전 Backup/Image/Manifest/Secret/Key/도구·Runbook. 외부 보조 서비스의 가용성을 복구 필수 경로로 추가하지 않음 |

근거:03 §3-F.4/5/8/15.2의 State·제한 입력·실행,04 §2의 Owner/단일 공유 실행자·§5의 보호 자산,03 §3-I.14.5의 Offline 복구다. ROSA Public API 때문에 Cloud 실행 자체가 불가능한 것은 아니다. Cloud가 실제 실행을 하려면 기존 개인 보호·네트워크·권한·비용 경계를 별도로 성립시켜야 하며 이번에 그러한 설정을 수행하지 않았다.

작업 환경 간 PC 파일·VPN·개인 Identity·DB/SSH/API 연결은 자동 공유되지 않는다. 원격 연결은 실제 환경에서 별도 확인하며 지원·권한·보호 조건을 수락해야 한다.

## 4. 사용량을 줄이는 인계 방식

작업 위치나 명령 실행 방식 변경만으로 사용량·비용 절감을 보장하지 않는다. 서비스 사용 한도와 별도 API 과금은 실제 계정 조건으로 확인한다.

작업을 기존 원 Issue 단위로 좁히고, 첫 실행에 지침·승인 경계를 읽은 뒤 정확 SHA·변경 경로·필요 입력·현재 결함·검사·다음 시작점만 이어간다. 매 명령마다 모든 설계·대화·이력을 다시 넣지 않는다. 큰 원문 로그 대신 보호 원본의 논리 참조와 필요한 판정만 기록한다. 각 작업 묶음의 시작/끝·공유 실행 직전에는 네 저장소의 변화와 직접 의존을 확인한다. 이 방식은 반복 맥락을 줄이는 제안이며 절감률 실측은 아니다.

## 5. 다음 작업 묶음

| 우선 작업 | 지금 가능한 부분 | 남은 직접 입력·완료 조건 |
|---|---|---|
| 인계 수신·로컬 준비 | 최신 Source·미병합 Docs #72/GitOps #25/Infra #43·개인 변경·정확 도구/Lock 확인 | 본인 작업 가능한 시간·Controller 접근과 목적 Caller/Backend 결과 |
| 독립 키 사본 | 기존 본인 Identity와 동일 금고의 독립 암호화 매체 보관·복원 검사 | 실제 매체 독립성·복원 Identity만으로 성공·비민감 암호문 개정 기록. 새 키 생성 없음 |
| Valkey Stage1 | 병합된 #22/#24 및 D의 등록·4객체 선택 Sync 성공 보고를 수신 | 성공한 등록/Sync 반복 없이 원 보고 빈칸·Gate/live Diff/경로 수락 보완→DNS/Hostname/TLS/AUTH/Ready·Prune/Delete 보호 Run |
| Backend 새 이미지·Stage2 | D Build/Scan/Digest 인계와 B 소비 개정 준비 | 실제 병합 App SHA의 Image, C DB/Schema/목적 Secret/CA·D/Owner Route/Origin→SHA B 등록→전체 release Gate→필요 단일 Migration→BE1→FE1→같은 조합 Run |
| ROSA 첫 실제 Plan | LOCAL_PREPARATION→INPUT_CONTRACT→REVIEW_AND_EXECUTION_GATES, 버전/Lock·권한·지원 검토 | A 제한 Network/prerequisite 출력·C SG2·B 목적 Caller/Backend·지원/Quota·사전 비용. OCP 철거나 전체 Recovery 종료를 일괄 조건으로 추가하지 않음 |
| Pool·Recovery·CI 후속 | 기존 원 Issue에서 코드/정적 준비 병행 | 두 Runtime Engine/Migration NullPool 유지. C 실제 한도·예약·종료 겹침 합의; 승인 Recovery Valkey Image/Probe/UID/Storage; D Writer/Promotion/ECR 실제 입력 |
| 비용·최종 시험·정리 | Source/사양·가용 시간·원장 입력·시험/삭제 계획 | Cost PARTIAL 유지. Full Plan·누적/가동/재시험/삭제지연/잔존 포함 $450계획/$500한도·유료 범위 수락→Window A/B·전체 T18·보존/삭제/종료 |

첨부의 `check-restored-cloud-vault.sh`는 복원 Identity와 암호문 파일의 두 절대 경로를 인자로 받는 안내다. 인계 카드에 언급한 외부 v4 검사 Script는 이번 ZIP에 없으므로 사용자의 실제 파일 유무/정본을 확인하기 전 실행하지 않는다. ROSA 준비는 저장소의 LOCAL_PREPARATION 명령으로 진행할 수 있다.

## 6. 검사와 종료 경계

실제 작업 결과는 원 Issue/PR/새 Run에 기록하고 Tracker·05에는 링크·상태·영향을 연결한다. 배정 책임자·실제 실행자·Principal·계정 관리 책임·리뷰/수신을 구분한다. Secret·전체 State/Output·Saved Plan·Private Key는 공개 인계에 넣지 않는다. 같은 State 쓰기·Restore·장애 주입·삭제는 지정 실행자와 공유 창을 따른다.

이번 최신 현황 수집을 모든 함수·과거 Commit diff·CI Artifact·외부 참조의 전면 의미 검토 완료로 확대하지 않는다. Q02/03/04/05/10, TH81·기존 실제 완료2, 공식 T/Must 판정은 기존 의미를 보존한다. 03 Backup periodic/ 정합은 이미 병합된 이름 변경이며 DR10분/DB RPO30분/Backup15분 설계는 유지한다. 출처 Manifest와 Evidence Index의 현재 표현 보완은 새 Runtime 성공이 아니다.

남은 작업:

- [ ] 최신 PR 검토/병합 및 인계 수신 범위 확인
- [ ] B 독립 키 사본·본인 clone/도구/목적 Caller/Backend·가용 시간
- [ ] D/B Stage1 보고 근거·Valkey 전체 시험·보호 동작 수락, C/D/B 새 Image/Data/Route 기반 Stage2
- [ ] A/C 제한 실제 입력·B ROSA Plan·D 전체 Cost Gate와 팀 실행창
- [ ] Pool/Recovery/CI 후속·Cloud 정상 업무·재생성/장애/부하·전체 Offline T18
- [ ] Evidence/발표·독립 자산 보존·인증 회수·승인 삭제·잔존 비용·10/26 종료 목표
