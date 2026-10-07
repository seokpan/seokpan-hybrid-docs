# B 작업 인계 — 리뷰 처리 종료와 다음 실행

> 기준일: 2026-10-07 KST. 담당: B 정태훈(tjung03).
> 이번 종료 단위: App17/18/19·GitOps20·Infra40 리뷰 대응, 가능한 병합/브랜치 정리, Docs69/72 판단, 단계별 lab/Cost 기준, 개인 실행 실패 안내.
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
| GitOps20 | b13ae9575206a335a9e6f87efc34dd4c198884f7 | metadata allowlist와 음성 Case 보완,58검사 PASS. A/D 재리뷰 요청. 최신 확인의 A Changes requested는 아직 새 승인으로 해소되지 않음. 병합/브랜치 삭제하지 않음 |
| Infra40 | c1a495bc2569c745d84dbcac27dc055596e8b5b1 | C 승인 후 a0da58c345f877659e522a5b4ab5392b1d0626d3에 병합·브랜치 삭제 완료. Metadata10개 단위검사, 실제 복원은 별도 |
| Docs69 | d7f0e619bfed462985f931502b00d639ac4d34b4 | 078d9e0007e82aa45d1fe1a81a2e1ca4fbec6a6b에 병합. 현재 main 대비 앞선 commit0/변경파일0, 삭제 가능. 삭제 여부 질문이므로 실제 삭제는 하지 않음 |
| Docs72 | 이 PR의 최신 HEAD 재조회 | 기존877ce979 이후 새 main7114e837의 C 변경과 이번 종료 결과를 결합. 병합 대기 유지, 새 결과는 이 PR에서 리뷰. #69 브랜치에 후속을 쓰지 않음 |

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

### W01. 남은 PR 처리 / 담당 B·A·C·D

GitOps20의 최신 재리뷰를 확인한다. A가 지적한 skip-reconcile·미승인 annotation/label이 checker/테스트에서 차단되는지 확인하고 새 feedback만 처리한다. 이전 Changes requested를 임의 dismiss하지 않는다. Docs72는 실제 최신 main과 충돌·C 기록·새 현재 상태·정확한 인계 링크를 리뷰하고 승인된 절차로 병합한다. 두 PR의 변경 범위는 다르며 한쪽 리뷰를 다른 PR 승인으로 승계하지 않는다. 이번에 #20/#72를 자동 병합하도록 예약하지 않았다.

### W02. Backend Image / D 작성·B 소비 검토

입력은 승인·병합된 App **a2afffb8605dafff1cb5b9af215aa0cf93aadcdb**와 Run37589421928이다. D가 해당 Source의 Build·Scan·Image Digest/플랫폼·Harbor 및 lab 내부 Registry 복사/Pull 개정을 공급한다. B는 App과 별도 held Migration Job이 같은 승인 Backend Digest를 참조하는지 대조한다. 새로운 Source/Image가 생기면 이 SHA를 계속 현재값으로 쓰지 말고 새 검증/Build와 연결한다. 기존 승인 Image가 이미 새 코드를 포함한다고 하지 않는다. Frontend Source는 이번 App17–19의 변경 대상이 아니다. 최종 종료는 D 인계 제출과 B 수신 범위, 실제 사용 Image 개정까지다.

### W03. lab Stage-1 Source와 전용 Gate / D 작성·B 리뷰

실행 입력 작성은 D, App/GitOps Source·배포 경계 리뷰는 B다. 역할 재배정이 아니다. lab Overlay patch로 lab-redis만 replicas1 및 `source-reviewed-runtime-unverified`, FE/BE는0 + input-required다. lab 때문에 base/backend.yaml·frontend.yaml hold를 제거하지 않는다. base/Recovery hold·Migration 별도 경계를 유지한다.

별도 **Valkey Stage-1 Preflight Gate**를 Source에 구현한다. 승인 Digest, Render된 StatefulSet/Service/ConfigMap, TLS/AUTH Secret 참조, TLS-only·Readiness AUTH, arbitrary UID/securityContext, Resource/Persistence 조건을 검사한다. FE/BE·DB의 미완성 입력을 검사 전제로 요구하지 않아야 한다. Valkey의 필수 조건은 빼지 않는다. 불필요한 FE/BE 활성화·다른 객체·권한 확대·미승인 Image/설정은 음성 Case로 차단한다.

기존 모든 Workload0/input-required 및 lab-redis0를 직접 검사하는 unittest뿐 아니라 CI의 진단 Render 후 조건도 staged activation에 맞춰 바꾼다. 검사를 삭제하거나 기존 전체 release-manifest를 약화하지 않는다. #20 Controller 등록 checker는 이 Stage-1 Gate가 아니다. 새 Gate/시험·보호 대상·Scope가 검토·병합되고 실제 입력/실행창을 수락하기 전에는 Valkey 선택 Sync도 수행하지 않는다. W02 Backend 새 Build·Cloud 금고·Cloud Pool 전체 합의는 Valkey Source 준비의 일괄 선행조건이 아니다.

### W04. 등록 SHA A와 Valkey 선택 Sync / D 작성·B 리뷰·지정 실행자

순서: W03 병합 **SHA A** → 별도 등록 PR → 실제 Owner/사용창/RBAC·객체 충돌 확인 → Bootstrap → SHA A의 Stage-1 Gate·live Diff → Valkey 리소스 선택 수동 Sync.

기존 openshift-gitops Controller, AppProject/Application 각1개(`seokpan-ocp-lab-app`), 두 metadata.namespace=`openshift-gitops`, Application project=`seokpan-ocp-lab-app`, destination=`seokpan-argotest`, path=`apps/overlays/lab`, targetRevision=SHA A. 등록 Manifest 자신의 SHA를 넣지 않는다. 새 Root/Controller/Operator와 default Project 수정은 없다. Secret/Job/Namespace/PVC를 Project 허용목록에 추가하지 않는다.

제어 객체 최초 apply는 Git Bootstrap이며 이후도 Git→Review→지정 apply다. 이 객체들 자체가 새 Root에서 자동 Sync되는 구조는 아니다. 자동 Sync/SelfHeal/Prune/finalizer는 사용하지 않는다. D의 과거 조건부 공유 사용 수락과 이번 실제 사용창은 구분한다. #5의 등록/Sync/Health/SHA와 #6의 실제 Valkey Pull/Ready/TLS/AUTH를 분리한다. 실패 시 마지막 성공 단계·현재 리소스·실행 Owner·수동 정리/복구 범위를 남긴다. Source merge/Synced/Valkey Ready는 전체 lab PASS가 아니다.

### W05. Stage 2 / C 입력·D 작성/실행·B 리뷰

부재 보고는 `backend-db-runtime`, `backend-database-ca`다. 실제 현재 환경에서 그 둘과 `backend-redis-runtime`, `backend-redis-ca`, DB Host/Name/Schema/목적 권한, Route Host/ALLOWED_ORIGINS를 개정별로 수락한다. 보고 시점의 부재를 현재 재조회 결과로 쓰지 않는다. Secret 값은 별도 Owner 공급이다.

W02의 새 Backend Image를 포함해 FE/BE 활성화는 lab Overlay의 replica/release-state patch로 반영 → 병합 **SHA B** → 등록 Source targetRevision SHA B 변경/Review/지정 apply → 기존 전체 release-manifest 정상 통과 → 필요한 단일 Migration → 최초 FE/BE 수동 Sync와 대표 업무 Run. Schema 확인을 새 DDL 실행 성공으로 바꾸지 않는다. Valkey 선택 Sync와 전체 App 업무 결과를 별도로 기록한다.

### W06. 본인 독립 사본 검사 / B 직접

현재 로그는 `/home/jth/secrets/seokpan/restore-check.M14I3E` 폴더 생성까지만 확인된다. 필요한 복원 파일 검사에서 중단됐으므로 SOPS/키/Token 오류로 판정할 수 없다. 폴더를 만드는 것과 독립 사본 파일을 복원하는 것은 별도 작업이다.

작업 장소는 Controller의 jth SSH 세션과 Controller 밖 본인 PC의 파일전송 창을 구분한다. 기존 본인 키(통상 `~/.config/sops/age/keys.txt`, 실제 존재 확인)와 C 암호문의 독립 사본을 암호화된 별도 매체에 보관한 뒤 그 매체에서 복원 폴더로 다시 전송한다. 파일 이름은 `restored-age-key.txt`, `foundation-data.sops.yaml`. 같은 Controller의 cp는 독립 사본 시험이 아니다. 원본을 편집하거나 새 키를 만들지 않는다.

학습 안내의 `b-direct-actions-20261007` 절과 제공된 `verify-restored-vault-v4.sh`를 사용한다. 실행은 `bash ~/work/seokpan-checks/verify-restored-vault-v4.sh /home/jth/secrets/seokpan/restore-check.M14I3E`. Script는 본인 키·암호문 개정·형식과 복원 키만 사용하는 환경을 검사하고 Token을 출력하지 않는다. 단축 해시12자 비교는 완전한 SHA256 동일성 증명이 아니다. 종료는 독립 매체에서 꺼낸 사실·검사 결과·비민감 개정과 실패 단계의 B 보고 수신이다. 기존 C 본체 해독 보고/B 수신을 다시 미완료로 되돌리지 않는다.

### W07. 본인 clone·도구 → ROSA 인증·입력 / B, A/C 협업

현재 clone 실패 로그는 경로/필수 파일 검사에서 진단 없이 종료됐으므로 `/home/jth/work/seokpan-hybrid-infra` 부재 또는 필수 파일 부재를 구분해야 한다。 제공 `rosa-local-check-v4.sh`를 jth로 실행한다. 명시적 `--create-if-missing`에서만 최초 clone을 만들고 기존 폴더·개인 변경·Branch/Lock은 덮어쓰지 않는다. 필요한 파일은 terraform/rosa/LOCAL_PREPARATION.md·scripts/tf-session.sh·rosa Lock이다.

Source HEAD/origin-main·개인 변경·Lock 차이·도구 버전을 보고한다. MISSING은 기록하고 공유 Controller의 패키지를 일괄 설치/업그레이드하지 않는다. 이어서 원 Infra25 안내에 따라 개인 MFA→목적 rosa Caller/Backend·지원/구독/Quota를 확인한다. bootstrap 성공을 rosa 권한 성공으로 사용하지 않는다. 실제 Plan에는 A 제한 출력/공통 prerequisite·C Data SG2와 올바른 Root/State/보호 입력이 필요하다. 이 helper는 Caller/Backend/Plan/Apply를 실행하지 않는다.

### W08. Cost Gate / D 원장·B ROSA 입력·A/C 자원 입력

원장 실물은 `Cost_Gate_Ledger_I07(3).xlsx`, SHA256 `1e7186febf71e16f72d6a92c406b9d1709e8e64839a8101fb913c4f126644383`다. 전달 설명의 (2)와 구분한다. [Docs43 원 기록](https://github.com/seokpan/seokpan-hybrid-docs/issues/43#issuecomment-6033030041)의 저장 판정은 PARTIAL, 미완19·입력오류0·기타미확인4, Window A/B 적용 미확인이다. 원본을 수정/재저장하거나 미정값을0으로 채우지 않았다. 이는 실제 최신 AWS Billing을 재조회한 결과가 아니다.

승인 ROSA Classic Multi-AZ 수량 **CP3/Infrastructure3/Worker3** 유지. Infra3→2 정정 제안은 철회됐고 그 변경 PR을 만들지 않는다. Worker Source의 replicas3/m5.xlarge/autoscaling=false와 실제 생성값은 구분한다. `worker_disk_size_gib`는 필수 입력이며 300GiB를 임의로 채우지 않는다.

다음은 모두 입력 미정: CP·Infra 실제 Instance Type/Volume, Worker disk, API LB 유형/수량, Ingress LB 유형/수량, Window A/B 실제 시작/종료/재시험, 중간/최종 Destroy 시각, 정태훈10/12–26 가용시간/휴무. 전송·Buffer·누적/잔존 비용도 확인한다. 공식 일반 Default·예시는 참고일 뿐 프로젝트 확정 입력이 아니다. 서비스가 전체 Plan에 모두 드러나지 않으면 지원조회/생성 직후 자원 목록과 과금 시작시각으로 보완하되 생성 전 비용검토/실행 승인을 생략하지 않는다. $450 계획선/$500 한도·Cost PARTIAL을 유지하고 실제 유료 생성은 별도 Gate다.

### W09. 새 C 변경과 설계 사본 / A/C 주 작업·B 소비

[Docs74](https://github.com/seokpan/seokpan-hybrid-docs/pull/74)가 main7114e8376b41812e86fbec14321d5b5f2224b332에 병합됐다. 일반 Backup Prefix를 periodic/으로 정하고 과거 hourly/를 이력으로 남긴 03·05 한 줄씩의 변경이다. Docs72 충돌 정리에서 이를 보존한다.

[Infra42](https://github.com/seokpan/seokpan-hybrid-infra/pull/42) HEAD ae01b78c866fbca88389c4316b6c3a813576b907은 확인 시 open이다. 운영 코드는 아직 그 PR의 리뷰/병합·실제 입력 확인이 남으므로 Docs74만으로 실제 적용 완료를 기록하지 않는다. A는 기존 tfvars의 backup_hourly_retention_days 사용 여부와 개명 입력을 확인한다. 첫 실제 백업 전 C의 Job·Lifecycle·Policy·대장 경로를 같은 개정으로 맞춘다. 기존 객체 없다는 내용은 C 보고 범위다.

등록된 Project03·그림 출처 manifest는 Docs74 이후 source hash 차이가 생길 수 있다. 승인 수량/DR 목표를 다시 설계하지 말고 periodic/ 한 줄 영향·참조/manifest 원문 식별을 대조한 뒤 필요한 사본/출처만 갱신한다. 이 후속은 work에서 처리하고 자동 Project 교체를 주장하지 않는다.

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

Docs72 최종 HEAD/검사·병합과 GitOps20 재리뷰 상태는 실행 전 GitHub에서 재조회한다. 본 인계 파일의 정확 SHA는 포함 PR의 파일 이력으로 식별하며 자기 Commit SHA를 본문에 넣어 자기참조하지 않는다.

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
