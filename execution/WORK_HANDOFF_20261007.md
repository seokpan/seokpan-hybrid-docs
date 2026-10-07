# B 작업 인계 — 리뷰 처리 종료와 다음 실행

> **최신 조사 후속 — 2026-10-07:** [전수 조사](REPOSITORY_AUDIT_20261007.md)·[05§9.47](05_IMPLEMENTATION_AND_VALIDATION.md#repository-full-audit-20261007) 참조. GitOps main의 Root SHA B/FE·BE1은 소스 병합 상태이며, 마지막 수신 Runtime은 SHA A/FE·BE0이다. 성공한 등록/선택Sync·금고 본체 확인을 반복하지 않는다. C의 GitOps26/6038214247 DB 형식·GRANT·TLS 접속·합성 출처 수락 보고는 수신했고 실제 Stage2 적용·Route/업무는 원 #26에서 후속 확인한다. 아래 시점별 인계 보존.

### 조사 중 추가된 실행 보고·수정 PR — 2026-10-07 후속 조회

[D 등록·선택 Sync 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5#issuecomment-6034601393)는 SHA A의 Valkey 4객체 `Succeeded`·FE/BE 미생성을, [Pod 확인](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6#issuecomment-6034590906)은 검토 Digest의 amd64 하위 ImageID·허용 UID만 보고했다. 등록/Sync를 다시 미실행으로 되돌리지 않는다. 실제 TLS/AUTH/Hostname·Ready 전체 Run과 Prune/Delete 차단은 아직 근거가 없으며 공유 Owner 재확인·등록 Commit·B 공유 시각의 빈칸 및 사전 합의되지 않은 `oc patch operation.sync.resources` 경로는 원 #5에서 보완·수락한다. #21의 완료 체크만으로 이 잔여를 완료 처리하지 않는다. 이 조사자는 클러스터를 직접 재조회하지 않았다.

현재 GitOps main의 [CI 37595556200](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37595556200)는 #24 등록값과 이전 checker allowlist 불일치로 실패했다. [Draft #25](https://github.com/seokpan/seokpan-hybrid-gitops/pull/25)는 checker/test/안내 3파일의 정합 수정이며 동일 도구에서 69검사·8 Render/26객체·고정 SHA 비교 PASS이며 [정확 PR HEAD6064311의 CI37598576166](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37598576166)도 completed/success다. 이는 미병합 PR의 검사이고 현재 main의 기존 CI 실패는 유지된다. Controller/Workload YAML과 실제 상태는 변경하지 않았고 main에 아직 병합되지 않았다. 전체 release Gate·공유 충돌·Prune/Delete 보호는 보존한다.

[Infra Draft #43](https://github.com/seokpan/seokpan-hybrid-infra/pull/43)은 ROSA `workspace_key_prefix=phase2/rosa/env`와 목적 Role의 List 범위를 맞춘다. default State Key는 유지한다. 기존 harness/보존 검사 PASS, 보조 로컬 fmt/validate는 NOT RUN 이력이다. [정확 PR HEADd5aeddd의 CI37598580155](https://github.com/seokpan/seokpan-hybrid-infra/actions/runs/37598580155)는 Core1.16.4/AWS6.67.0/RHCS1.7.7의 fmt·backend=false/readonly init·validate(errors0/warnings0)·Schema13종·OIDC mock2·Source/Lock 불변 PASS다. 실제 Backend 인증·Workspace 조회·Cloud Plan/Apply는 NOT RUN이다. 누락만으로 기존 init 실패를 단정하지 않는다. 검토·병합 후 본인 clone/Workspace와 실제 Caller/Backend를 확인한다.

[GitOps #26](https://github.com/seokpan/seokpan-hybrid-gitops/issues/26)은 후속 조회에서 Stage2의 실제 추적 Issue로 확인됐다. [D의 backend-db-runtime 공급 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6#issuecomment-6034843156)는 두 URL 키·계약 Host/DB 이름과 기존 lab 계정 비밀번호 공유를 명시한다. Secret 미공급으로 되돌리지 않되 실제 새 URL 접속·C 형식/GRANT·데이터 출처 수락은 대기다. Route/Origin·새 Backend Image·Stage2 활성화/전체 Gate도 미완료다.

Codex의 첫 읽기·작업 위치·사용량·다음 직접 조건은 [CODEX_ENTRYPOINT_20261007.md](CODEX_ENTRYPOINT_20261007.md)를 따른다. 원 보고와 이 Source 수정의 수신/검토·실행은 별개다.


> 기준일: 2026-10-07 KST. 담당: B 정태훈(tjung03).
> 현재 인계 단위: App17/18/19 병합·새 Image 대기, GitOps20/22/24와 Infra40/42 병합 후 실행 입력, Docs72 최신화·Docs77 공급 보고, lab Stage1/2·금고 독립 사본·ROSA/Cost. 이전 리뷰/실패/검사 결과는 이력으로 보존한다.
> 구분: 이번 처리 묶음의 종료와 전체 S1–S4/Q10 수렴·실환경 완료는 다르다. 이 문서는 다음 `work` 작업 공간에서 사용할 인계 자료이며, 별도 공간에 자동 전송/등록됐다는 의미는 아니다.

## 1. 재개 시 먼저 할 일

PROJECT_INSTRUCTIONS와 최신 승인 설계를 읽고 Docs21 원 기록 → 이 문서 → 실행판 → GitOps5/10/14/6 및 Infra25를 확인한다. 새로 전체 저장소를 처음부터 수집하기 전에 아래 고정 SHA와 현재 원격 차이를 조회한다. PR의 본문뿐 아니라 최신 리뷰의 commit_id, 미해결 thread, 검사 대상 SHA, 실제 merged 값과 Branch를 확인한다. 새 팀 변경은 그 담당자의 원본에 연결하고 과거 승인/시험을 소급 변경하지 않는다.

이번 종료 단위에서 이미 끝낸 수정·시험을 새 작업으로 반복 생성하지 않는다. 임시 검사 코드나 진단 Render를 Runtime에 Apply하지 않는다. 인증 정보·Token·개인키·State/Plan 전체는 이 자료에 없으며 요청하지 않는다.

## 2. 완료한 Source와 아직 기다리는 리뷰

| 대상 | 검토 HEAD | 결과 / 직접 다음 행동 |
|---|---|---|
| App17 | 367938f08e735fe123827b3c9362307b5d59408f | D 재승인5438988132 후 squash 병합5e2bdc1490ebe6baf53e303db55a3aac42771976. 작업 브랜치 삭제 |
| App18 | d624c83081f18ad81c793cfe39e81ce6075abfba | D 재승인5438973472 후 squash 병합4dd1213315edff97a3ecb4286eae058de90de157. 작업 브랜치 삭제. Script11·CI 중복/opt-in 순서 보완 포함 |
| App19 | f548f921c436d614a3fe0b3969161b8d1433ab5f | D 재승인5438977533 후 squash 병합a2afffb8605dafff1cb5b9af215aa0cf93aadcdb. 작업 브랜치 삭제. PubSub 취소/cleanup RedisError 처리 포함 |
| GitOps20 | b13ae9575206a335a9e6f87efc34dd4c198884f7 | metadata allowlist·58PASS 후 재승인 수신,5dc2bd546de1acbbeb47a380c85103ce2b31017f 병합·작업 브랜치 삭제. 완료한 재리뷰/병합 반복 없음 |
| GitOps22 | d6a070284535dc5016dcdb8c2159604e8dcd46cd | Stage-1 lab Valkey 활성화·전용 Gate Source 병합. Workload SHA A=244b48b885d7ac645c402e561a032ae65a8f3461. D 선택 Sync 성공 보고 수신. 전체 Ready/TLS/AUTH 판정은 별도 |
| GitOps24 | 774975881ad2cac13c927ef457f7644a9ccbe34d | a25172c7453b9d7999cb1f3cbeb1ef35774e3b63 병합. 기존 Controller·제한 Project/Application, targetRevision=SHA A. Source 등록값과 실제 Bootstrap/Controller 동작 구분 |
| Infra42 | ae01b78c866fbca88389c4316b6c3a813576b907 | 36dc2403aa77e2896cc4ec3c545b92e0afb49205 병합. periodic/·backup_periodic_retention_days. 실제 입력/Plan/백업은 별도 |
| Infra40 | c1a495bc2569c745d84dbcac27dc055596e8b5b1 | C 승인 후 a0da58c345f877659e522a5b4ab5392b1d0626d3에 병합·브랜치 삭제 완료. Metadata10개 단위검사, 실제 복원은 별도 |
| Docs69 | d7f0e619bfed462985f931502b00d639ac4d34b4 | 078d9e0007e82aa45d1fe1a81a2e1ca4fbec6a6b에 병합. 현재 main 대비 앞선 commit0/변경파일0, 삭제 가능. 삭제 여부 질문이므로 실제 삭제는 하지 않음 |
| Docs72 | 기존 게시 HEAD376afcb03849e2325c5a10e80a363081bb0cd2de 이후 최신 HEAD 재조회 | 최신 main의 C Docs74/75/77 기록·이번 원격 변경을 정상 결합하고 리뷰한다. 병합 대기 유지. #69 브랜치에 후속을 쓰지 않음 |
| Docs77 | a9b0207b563aa25be17d4a635f6cc903fbe0e74a 병합 | C의 Data 공급·확인 보고가 main의05 §8.15/Tracker에 반영됨. 해당 C 원문 보존. 문서 PR 병합과 실제 Foundation/SQL/Runtime 수락 구분 |

App의 실제 결합 Source는 **a2afffb8605dafff1cb5b9af215aa0cf93aadcdb**다. [결합 main Run37589421928](https://github.com/seokpan/seokpan-hybrid-app/actions/runs/37589421928)에서 Backend **1762 PASS**, 별도 runner47 PASS(부분집합), 별도 Lua9 PASS를 확인했다. 모든 최종 JUnit failure/error/skip0, 기존 Lock/sync·format/lint·mypy·coverage 통과, Python3.13.15/uv0.12.5·dirty=false다. 이 결합 검증은 개별1754/1752/1760 결과의 산술 합산이 아니다.

Artifact11467549120 / ZIP SHA256 `5bca559ae4368a192d91a1ccb652ca22f58a23922df68540dd9fbb9b43d2158e`. 내려받은 ZIP CRC·summary commit·JUnit을 확인했다. 보존 만료2026-11-06에 앞서 필요한 증거를 보존한다. 실제 Image Build/Scan/Pull·Valkey TLS/운영 연결·다중 Pod·Cloud/T18/성능은 이 검사에 포함하지 않는다.

[브랜치 정리 Run37589531720](https://github.com/seokpan/seokpan-hybrid-app/actions/runs/37589531720)은 PR별 merged/리뷰 HEAD/병합 SHA와 결합 main의 변경 파일 동일성을 대조한 뒤 지정한 세 브랜치를 정확한 ref lease로 삭제했다. main·타인의 작업 Branch·과거 Run은 보존했다. 정리용 임시 Branch도 삭제했다.

## 3. 원본 기록 위치

| 내용 | 원본 |
|---|---|
| App 리뷰·변경·원 검증 | App PR17/18/19, App4 |
| 실제 결합 Source·검사 → Image Build/Scan/Digest | App2 |
| Controller 등록·Sync/Health·등록/Workload SHA | GitOps5 |
| 공유 Owner·사용창·Registry·실제 환경 입력 | GitOps14 |
| Pull·Ready·TLS/AUTH·대표 업무와 Run | GitOps6 |
| Source/Overlay·release 검사·Migration/Recovery 선언 | GitOps10 |
| 본인 ROSA Source/Caller/Backend/Plan·Window/Destroy | Infra25 |
| 금고 원 공급·개정·수신·독립 사본 | Infra19 |
| 비용 원장·실제 사양/가동/잔존 비용 | Docs43, D Cost Ledger |
| 전체 집계 | WORK_TRACKER·05: 원본 링크/상태/영향만. B 출발점 Docs21 |

## 4. 다음 작업 카드 — 실행 순서와 병행

### W01. 현재 PR 처리 / 담당 B·A·C·D

GitOps20의 재승인·병합·브랜치 삭제는 완료다. GitOps22 Stage-1과 GitOps24 등록값 Source도 병합됐으므로 같은 Source 작성/리뷰를 반복하지 않는다. 실제 등록/보호 시험·선택 Sync는 W03–W04의 정확한 Workload SHA/실환경 조건에서 수행한다. Docs72는 최신 main과 정상 결합해 C Docs74/75/77·기존 기록과 이 현재 인계를 보존하고 문서 재리뷰/병합을 진행한다. Docs77의 C 공급 보고는a9b0207b563aa25be17d4a635f6cc903fbe0e74a에 병합됐다. 같은 C 문서 PR을 다시 생성하지 않으며 실제 공급/Runtime 수락은 원 결과의 범위로 확인한다. 자동 병합/실행을 예약한 상태로 기록하지 않는다.

### W02. Backend Image / D 작성·B 소비 검토

입력은 승인·병합된 App **a2afffb8605dafff1cb5b9af215aa0cf93aadcdb**와 Run37589421928이다. D가 해당 Source의 Build·Scan·Image Digest/플랫폼·Harbor 및 lab 내부 Registry 복사/Pull 개정을 공급한다. B는 App과 별도 held Migration Job이 같은 승인 Backend Digest를 참조하는지 대조한다. 새로운 Source/Image가 생기면 이 SHA를 계속 현재값으로 쓰지 말고 새 검증/Build와 연결한다. 기존 승인 Image가 이미 새 코드를 포함한다고 하지 않는다. Frontend Source는 이번 App17–19의 변경 대상이 아니다. 최종 종료는 D 인계 제출과 B 수신 범위, 실제 사용 Image 개정까지다.

### W03. 병합된 lab Stage-1 Source와 전용 Gate / D 공급·B 소비 검토

[GitOps22](https://github.com/seokpan/seokpan-hybrid-gitops/pull/22)의 Stage-1 Source는 **SHA A=`244b48b885d7ac645c402e561a032ae65a8f3461`**에 병합됐다. D 작성/B 리뷰 경계와 기존 승인 결과를 재사용한다. lab Overlay에서 lab-redis만 replicas1 및 `source-reviewed-runtime-unverified`, FE/BE는0+`input-required`다. base/backend.yaml·frontend.yaml/Recovery hold, 별도 Migration의 suspend/current/300초·단일 실행을 유지한다.

병합된 Valkey Stage-1 Preflight Gate는 승인 Digest, Render된 StatefulSet/Service/ConfigMap, TLS/AUTH Secret 참조, TLS-only·Readiness AUTH, arbitrary UID/securityContext, Resource/Persistence 및 선택 실행 범위를 확인하는 진입점이다. FE/BE·DB의 미완성 입력을 Valkey 단독 준비의 일괄 조건으로 추가하지 않는다. 기존 전체 release-manifest를 약화하거나 #20 Controller 등록 checker를 이 Gate로 대신하지 않는다. 현재 실행할 정확한 SHA A/도구·검토 범위·실제 Secret/Image·사용창을 대조하고 해당 Gate와 live Diff를 통과한 Valkey 리소스만 선택 Sync한다.

Source 병합은 실제 Controller 적용·Image Pull/Ready·TLS/AUTH 성공이 아니다. 새로운 Source 변화가 있으면 해당 diff와 검사를 원 PR에 연결한다. W02의 새 Backend Build·Cloud 금고 독립 사본·Cloud Pool 전체 합의는 Valkey 단독 실행 준비의 일괄 선행조건이 아니다.

### W04. 병합된 등록 Source와 Valkey 선택 Sync / D 공급·B 리뷰·지정 실행자

[GitOps24](https://github.com/seokpan/seokpan-hybrid-gitops/pull/24)의 등록 Source는 **`a25172c7453b9d7999cb1f3cbeb1ef35774e3b63`**에 병합됐다. 등록 Manifest의 `targetRevision`은 W03의 **Workload SHA A=`244b48b885d7ac645c402e561a032ae65a8f3461`**다. 등록 PR 자신의 SHA나 이동하는 main을 Sync 대상으로 대신하지 않는다.

기존 openshift-gitops Controller와 제한 AppProject/Application 각1개(`seokpan-ocp-lab-app`), metadata.namespace=`openshift-gitops`, project=`seokpan-ocp-lab-app`, destination=`seokpan-argotest`, path=`apps/overlays/lab`을 사용한다. 새 Root/Controller/Operator·default Project 수정이나 Secret/Job/Namespace/PVC 허용 확대를 추가하지 않는다. Source의 수동 Sync·삭제 보호 옵션은 실제 Controller 동작 시험과 구분한다.

D의 실제 Bootstrap·SHA A Valkey 4객체 선택 Sync 성공 보고는 수신했다. 다음은 상단 추가 보고의 빈칸·사용창/Gate/live Diff/수동 경로 근거 수락과 #6의 전체 Ready/TLS/AUTH/Hostname·보호 시험이다. 성공한 등록/Sync를 무조건 반복하지 않는다. 제어 객체 최초 apply는 Git Bootstrap이고 이후도 Git→Review→지정 apply이며 새 Root가 두 객체 자체를 자동 관리하는 흐름이 아니다. 자동 Sync/SelfHeal/Prune/finalizer는 사용하지 않는다. D의 과거 조건부 공유 사용 수락과 이번 실제 사용창은 구분한다.

이 문서 변경에서 실제 등록/Sync를 수행하거나 Runtime을 재조회하지 않았다. 다른 실행자의 새 보고는 정확한 시각/Caller/Source/대상과 함께 원 #5/#6에서 수신하며, Source 병합·등록·Synced·Valkey Ready를 전체 lab/ROSA PASS로 올리지 않는다. 실패 시 마지막 성공 단계·현재 리소스·실행 Owner·수동 정리/복구 범위를 남긴다.

### W05. Stage 2 / C 입력·D 작성/실행·B 리뷰

이전 부재 보고 대상은 `backend-db-runtime`, `backend-database-ca`였다. 최신 공급 보고는 Docs77/원 Infra19에서 범위·개정·수신을 확인하고, 이번 원격 문서 조회를 Cluster Secret 존재/현재 연결의 직접 재조회로 사용하지 않는다. 실제 환경에서 그 둘과 `backend-redis-runtime`, `backend-redis-ca`, DB Host/Name/Schema/목적 권한, Route Host/ALLOWED_ORIGINS를 개정별로 수락한다. Secret 값은 별도 Owner 공급이며 본체 금고 해독 성공은 실제 SQL 계정 생성·Grant/TLS·App Secret 주입의 PASS가 아니다.

W02의 새 Backend Image를 포함해 FE/BE 활성화는 lab Overlay의 replica/release-state patch로 반영 → 병합 **SHA B** → 등록 Source targetRevision SHA B 변경/Review/지정 apply → 기존 전체 release-manifest 정상 통과 → 필요한 단일 Migration → 최초 FE/BE 수동 Sync와 대표 업무 Run. Schema 확인을 새 DDL 실행 성공으로 바꾸지 않는다. Valkey 선택 Sync와 전체 App 업무 결과를 별도로 기록한다.

### W06. 본인 독립 사본 검사 / B 직접

[C Valkey 금고 확인 보고](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6028766924)·[B 수신](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6028919355), [B의 SQL 금고 jth 확인](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6033157659)·[C의 세 계정 확인](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6033174437)은 본체 해독/형식·암호문 해시 확인 완료 범위다. 새 Key 생성이나 그 성공을 다시 미완료로 되돌리지 않는다. Controller 밖 독립 Key/암호문 사본과 복원한 Identity의 검사는 별도로 남는다. 아래 `/home/jth/secrets/seokpan/restore-check.M14I3E` 생성 뒤 복원 파일 검사 중단 로그는 과거 독립 사본 시도이며 본체 SOPS/Token 오류를 뜻하지 않는다.

작업 장소는 Controller의 jth SSH 세션과 Controller 밖 본인 PC의 파일전송 창을 구분한다. 기존 본인 키(통상 `~/.config/sops/age/keys.txt`, 실제 존재 확인)와 C 암호문의 독립 사본을 암호화된 별도 매체에 보관한 뒤 그 매체에서 복원 폴더로 다시 전송한다. 기존 Valkey 검사 파일 이름은 `restored-age-key.txt`, `foundation-data.sops.yaml`다. SQL 암호문 `data-sql-accounts.sops.yaml`도 목적별 승인 개정으로 독립 보관하고 해당 Schema의 값 없는 해독/형식 확인을 별도로 기록한다. Valkey 전용 helper가 SQL 필드를 검사한다고 가정하지 않는다. 같은 Controller의 cp는 독립 사본 시험이 아니다. 원본을 편집하거나 새 키를 만들지 않는다.

현재 첨부 도구는 `check-restored-cloud-vault.sh`이며 SHA256=`a2bca07f132c15e6545c5783264423ae96c16eb88bbac602a2c27a0214dfc7f9`다. 독립 보호 매체에서 복원한 Identity/Valkey 암호문의 읽을 수 있는 **절대경로 두 개**를 받는다. `bash /absolute/check-restored-cloud-vault.sh /absolute/restored/keys.txt /absolute/restored/foundation-data.sops.yaml` 형식으로 본인 계정에서 실행하며 내용 값은 인자로 넣지 않는다. 기존 `verify-restored-vault-v4.sh`는 이번 첨부에 없으므로 본인 실제 파일/내용 일치를 확인한 경우만 학습 안내의 과거 v4 경로를 사용한다. 두 도구를 이름만 바꿔 같은 것으로 취급하지 않는다. 단축 해시12자 비교는 완전한 SHA256 동일성 증명이 아니다. 종료는 독립 매체에서 꺼낸 사실·검사 결과·비민감 개정과 실패 단계의 B 보고 수신이다. 기존 C/B 본체 해독 완료를 되돌리지 않는다.

### W07. 본인 clone·도구 → ROSA 인증·입력 / B, A/C 협업

현재 clone 실패 로그는 경로/필수 파일 검사에서 진단 없이 종료됐으므로 `/home/jth/work/seokpan-hybrid-infra` 부재 또는 필수 파일 부재를 구분해야 한다. 이번 첨부에 `rosa-local-check-v4.sh`는 없으므로 본인 실제 파일/내용을 확인한 경우만 과거 helper 절차를 사용한다. 별도 helper가 없어도 [Infra 정본 LOCAL_PREPARATION.md](https://github.com/seokpan/seokpan-hybrid-infra/blob/main/terraform/rosa/LOCAL_PREPARATION.md)의 본인 clone 상태/차이·Lock·도구 확인부터 진행한다. 기존 폴더·개인 변경·Branch/Lock은 덮어쓰지 않는다. 필요한 정본 파일은 terraform/rosa/LOCAL_PREPARATION.md·scripts/tf-session.sh·rosa Lock이다.

Source HEAD/origin-main·개인 변경·Lock 차이·도구 버전을 보고한다. MISSING은 기록하고 공유 Controller의 패키지를 일괄 설치/업그레이드하지 않는다. 이어서 원 Infra25 안내에 따라 개인 MFA→목적 rosa Caller/Backend·지원/구독/Quota를 확인한다. bootstrap 성공을 rosa 권한 성공으로 사용하지 않는다. 실제 Plan에는 A 제한 출력/공통 prerequisite·C Data SG2와 올바른 Root/State/보호 입력이 필요하다. Source/도구 확인을 Caller/Backend/Plan/Apply 수행으로 승계하지 않는다.

### W08. Cost Gate / D 원장·B ROSA 입력·A/C 자원 입력

원장 실물은 `Cost_Gate_Ledger_I07(3).xlsx`, SHA256 `1e7186febf71e16f72d6a92c406b9d1709e8e64839a8101fb913c4f126644383`다. 전달 설명의 (2)와 구분한다. [Docs43 원 기록](https://github.com/seokpan/seokpan-hybrid-docs/issues/43#issuecomment-6033030041)의 저장 판정은 PARTIAL, 미완19·입력오류0·기타미확인4, Window A/B 적용 미확인이다. 원본을 수정/재저장하거나 미정값을0으로 채우지 않았다. 이는 실제 최신 AWS Billing을 재조회한 결과가 아니다.

승인 ROSA Classic Multi-AZ 수량 **CP3/Infrastructure3/Worker3** 유지. Infra3→2 정정 제안은 철회됐고 그 변경 PR을 만들지 않는다. Worker Source의 replicas3/m5.xlarge/autoscaling=false와 실제 생성값은 구분한다. `worker_disk_size_gib`는 필수 입력이며 300GiB를 임의로 채우지 않는다.

다음은 모두 입력 미정: CP·Infra 실제 Instance Type/Volume, Worker disk, API LB 유형/수량, Ingress LB 유형/수량, Window A/B 실제 시작/종료/재시험, 중간/최종 Destroy 시각, 정태훈10/12–26 가용시간/휴무. 전송·Buffer·누적/잔존 비용도 확인한다. 공식 일반 Default·예시는 참고일 뿐 프로젝트 확정 입력이 아니다. 서비스가 전체 Plan에 모두 드러나지 않으면 지원조회/생성 직후 자원 목록과 과금 시작시각으로 보완하되 생성 전 비용검토/실행 승인을 생략하지 않는다. $450 계획선/$500 한도·Cost PARTIAL을 유지하고 실제 유료 생성은 별도 Gate다.

### W09. periodic/ 변경과 최신 C 공급 보고 / A/C 주 작업·B 소비

[Docs74](https://github.com/seokpan/seokpan-hybrid-docs/pull/74)의 03/05 periodic/ 결정과 Docs75의 과거 hourly/ 설명은 최신 main과 결합할 때 그대로 보존한다. [Infra42](https://github.com/seokpan/seokpan-hybrid-infra/pull/42)는 **`36dc2403aa77e2896cc4ec3c545b92e0afb49205`**에 병합됐다. 운영 코드 리뷰/병합 대기는 해소됐으며 일반 사본 Prefix=`periodic/`, 변수=`backup_periodic_retention_days`, 보호 사본=`protected/`다.

A는 기존 tfvars의 `backup_hourly_retention_days` 사용 여부와 새 변수 소비를 확인한다. C의 Job·Lifecycle·Policy·대장 경로를 같은 개정으로 수락하고 실제 Root Plan/승인된 Apply·Backup의 결과를 별도로 기록한다. 기존 객체가 없다는 내용은 첫 실제 Backup 전 C 보고 범위다. Source 병합을 기존 운영 객체 변경/실제 백업 성공으로 해석하지 않는다.

[Docs77](https://github.com/seokpan/seokpan-hybrid-docs/pull/77)의 C 10/7 Data 공급·확인 보고는 **`a9b0207b563aa25be17d4a635f6cc903fbe0e74a`**에 병합됐다. 원 공급 댓글과 C/B의 SQL·Valkey 본체 금고 확인 범위를 수신하고, 독립 Key 사본/복원과 실제 SQL 계정 생성·App Secret/CA 공급·연결 수락을 각각 확인한다. C의 최신 05 §8.14/8.15·Tracker 후속과 기존 A/D 비용·Run은 정상 main 결합에서 그대로 보존하며 같은 C 결과를 B의 새 실행으로 대필하지 않는다.

등록 Project03·그림 출처 manifest는 periodic/ 한 줄 이후 Source 식별 차이가 있을 수 있다. 03/04 종료·승인 수량/DR 요구는 유지하고 필요한 사본/출처 정합만 확인한다. 자동 Project 교체나 직접 Runtime 재조회 완료를 주장하지 않는다.

### W10. S1 잔여 / B

시작 파일군: Room start_intent/start_capture/start_completion/start_closure/runtime, identity 보상·경쟁과 시험 대응, Frontend 전체 경로. 현재 App17/18/19 수정은 병합·검증됐으므로 새 PR로 반복하지 않는다.

리뷰 후속 두 건도 여기에 둔다. (1) apply_resolution의 Lua null 방어 분기는 기존 Apply(None) Python guard 때문에 실제 Lua 직접 실행 사례가 아니다. raw payload 직접 시험이 필요한지 판단한다. (2) 정상 Provider 오류 경로에서 aclose RedisError가 원 RealtimeUnavailable 변환을 가릴 수 있다는 D 의견은 취소 경로와 별도다. 합성 재현·영향 확인 뒤 필요하면 좁은 수정/회귀 PR을 만든다. 두 항목은 이번 승인 PR의 미해결 차단 사항이 아니다. 정리 시도와 실환경 연결 회수 성공도 구분한다.

파일·함수·규칙·시험·관측·미검토 범위를 기록한다. 전체 단위검사 통과만으로 모든 코드의 수작업 의미 검토를 완료 처리하지 않는다. 실제 Valkey/Driver/TLS/AUTH/RESP/Lua·시간대·Pool·종료 겹침 검증은 정확한 조합에서 별도 수행한다. Pool3+2/60은 미채택 시나리오다.

### W11. S2 잔여 / B·C·D·A

Recovery redis.yaml/redis.conf·renderer·검사의 held redis-server/TCP probe·Image/Volume 입력을 실제 승인 Valkey의 binary/UID/Probe/TLS/AUTH/Persistence와 함께 개정한다. lab emptyDir·기존1차 PVC를 Recovery에 그대로 복사하지 않는다. C Backup/Key/Host·D 보존 Image·B App 선언의 인계 수락 뒤 Offline 본 시험으로 연결한다.

App14 Writer와 App15 Promotion은 Source/mock 준비와 실제 자격/Push/PR를 나눈다. 현재1차 경로 기반 helper를 인증 없는2차 dry-run으로 가정하지 않는다. Release 형식·Digest/플랫폼·App/별도Migration 대응·정리 보호를 검사한다. Writer 자격 완료를 전체 순수 Source 준비의 선행조건으로 만들지 않으며 사람 승인/병합·Argo Reader 경계는 유지한다.

### W12. S3–S4 / B

기존 Snapshot/Bundle/원 Run을 재사용하고 새로운 Branch/PR/Commit/댓글·리뷰/검사 변화부터 추적한다. 도달 가능한 모든 과거 diff·CI로그/산출물·thread 상태·외부 링크/anchor의 의미 검토는 아직 남아 있다. 431commit 또는144페이지/PR99/Review81 등의 과거 수집 숫자는 완료 검토 수가 아니다. 접근불가/삭제된 비도달 이력·개인 미커밋·보호 Runtime은 그 한계를 적는다.

발견→원 코드/원 Issue→직접/후속 영향→필요 수정→회귀→기록/등록본 영향→종료 직전 원격 delta를 반복한다. 확인 가능한 미검토·미해결이 남으면 Q10은 완료하지 않는다. 새 조사 전체를 Source 리뷰/팀원 독립 준비/비용 입력의 일괄 선행조건으로 묶지 않는다.

### W13. 최종 실제 검증·종료 / B 중심 각 담당

Window A 통합은 실제 Plan·Cost·사용창 수락 후 생성/Pull/Data/Migration/정상 업무/Backup·Release로 연결한다. 승인 목표는10/12–15, Technical Freeze10/16이다. 실제 가동시간은 아직 미확정이다. 전체 Recovery/T18은 사전 보존한 Backup/Key/Image/도구·격리 Host와 지정 클라이언트의 업무/영속 Data로 RTO10분·DB RPO30분을 판정한다. 15분 예약 자체를 목표 달성으로 보지 않는다.

Window B10/19–21은 정상 Baseline·재생성→장애/부하/재시험의 목표 창이다. 삭제 전 증거·검증 Bundle·보관/회수 구분과 잔존 비용을 확인한다. 기본 비용절감 Destroy는 rosa이며 foundation/bootstrap 전체 Destroy는 별도 승인이다. Demo Freeze10/22·준비10/23·종료10/26은 기존 목표이며 주말/휴무 가용성을 임의 전제하지 않는다. OCP 공유 실습 정리는 별도 Owner/사용 종료·보존 조건이다. 개인 설명·Troubleshooting·발표는 원 Run에 연결한다.

## 5. 인계 운영과 완료 판정

이 문서의 작성/게시와 다음 work 수신·실제 수행은 별개다. 수신 작업은 사용할 Source/개정·범위·미확인/의존·완료조건을 원 Issue에서 확인한다. 한 작업 카드가 완료될 때 다른 카드의 Runtime/비용까지 자동 완료하지 않는다. 특히 Q는 조사, TH81은 개인 구현·검증/발표·종료, T01–T23은 실제 시험이다. 기존 실제 완료2는 그대로다.

Docs72 최종 HEAD/검사·병합과 사용할 GitOps Workload·등록 Source/새 실행 보고는 실행 전 GitHub에서 재조회한다. GitOps20의 재승인·병합은 완료 이력이며 현재 대기로 되돌리지 않는다. 본 인계 파일의 정확 SHA는 포함 PR의 파일 이력으로 식별하며 자기 Commit SHA를 본문에 넣어 자기참조하지 않는다.

## 6. 전체 고정 체크리스트

- [x] Q01 — GitOps #17의 병합·브랜치 삭제를 확인하고, Docs #64의 실행판·학습 안내·WORK_TRACKER·05와 PR 기록에 반영한 뒤 변경·리뷰 상태를 검증한다.
- [ ] Q02 — 네 저장소의 전체 문서·구현 코드·설정·시험·주석·관련 파일을 목록화하고, 활성 원본·재사용 원본·과거 이력·생성물을 구분하여 내용을 조사한다.
- [ ] Q03 — 네 저장소의 열린/닫힌 Issue·PR·본문·댓글·리뷰·검사와 모든 현재 Branch·Commit·변경 파일을 추적하고, 페이지 누락·접근 제한·삭제된 이력의 확인 범위를 기록한다.
- [ ] Q04 — 상위/하위 작업·담당자·입력·산출물·원 코드·시험·인계의 직접 의존과 후속 영향을 연결하여 순환 대기·오래된 완료/대기·누락을 확인한다.
- [ ] Q05 — Valkey 전환, OCP–Harbor 연결 제약과 내부 Registry 소비, DR RTO 10분·영속 DB RPO 30분·백업 계획 주기 15분을 설계·코드·가이드·시험·비용·주석에 걸쳐 대조하고 필요한 불일치를 수정한다.
- [x] Q06 — 그림 생성 원본·manifest·출처 기록·SVG·PNG와 이를 참조하는 문서를 대조하고, 영향을 받은 생성물만 재생성·시각 검증한다.
- [x] Q07 — 등록된 프로젝트 소스 7개를 저장소 정본과 내용·버전·해시로 대조하고, 필요한 등록용 개정본과 교체 대상을 제공한다. 실제 프로젝트 소스 교체는 별도로 확인한다.
- [x] Q08 — B 명의 문서·Issue·PR·댓글의 대화 의존·자기 요청 중계·불필요한 AI 작업 홍보를 목적·변경·근거·결과·한계 중심으로 정리하고, 실제 수행·승인·시험 이력은 보존한다.
- [x] Q09 — 실제 필요한 수정만 B 범위에서 처리하고, 다른 담당자의 변경을 보존하며 해당 담당자의 검토·입력·수신이 필요한 사항을 원 작업에 인계한다.
- [ ] Q10 — 발견→직접/후속 영향→수정→재검증을 반복하고, 종료 직전 원격 변경을 다시 대조하여 확인 가능한 전체 범위에서 새로운 확인·보완 사항이 없을 때 최종 수렴을 판정한다.
- [x] Q11 — 조사 대상·관측 SHA·근거·발견·조치·검증·미확인·다음 순서를 이 대장과 원 작업에 보존하여 다음 작업 공간에서도 연속성을 유지한다.
- [x] Q12 — 조사 결과를 B의 기존 TH 81개·실제 완료 상태·추가 작업·직접 입력·병행 작업·실행 Gate와 연결하고, #64 병합 여부는 별도 완료 통보를 전제로 하지 않고 GitHub에서 확인한다.
