# Evidence Index and Run Guide

실제 실행 결과는 승인04 §5.4·§10.4에 따라 `evidence/<test-id>/<run-id>/`에 남깁니다. 각 실행 담당자가 자기 결과를 작성하고 최유준이 Index/형식을 연결합니다. **현재 Index에는 아래의 독립 합성 Data 부분 예행과 Backend 업무 연결 부분 예행의 실제 Run 2개가 연결돼 있습니다.** 격리 로컬 환경에서 실행·기록한 Run의 Index를 임시 연결했으며, C/B 영역 리뷰와 D Index 검토·수신은 대기합니다. 기존 lab 보고와05의 부분 검사 이력을 여기 새 Run으로 수행했다고 표시하지 않습니다.

## Create a Run

1. [_template/](./_template/summary.md)의 다섯 파일을 실제 test-id/run-id 폴더로 복사합니다. 새 실행·재시험은 별도 Run입니다.
2. release.json에 실제 Source·Image·환경·입력 개정·실행자·시각·조건을 연결합니다. 빈 값은 null로 유지하고 PASS는 해당 증거가 있어야 합니다.
3. summary.md에는 범위·결과·원인·제한·다음 행동, metrics.csv에는 실제 수치/단위/집계, timeline.csv에는 단계 시각을 남깁니다. 헤더만 있는 CSV는 미측정이며 0건/0초 결과가 아닙니다.
4. checksums.txt에는 공유 가능한 실제 파일의 SHA-256을 생성해 넣습니다. 보호 Raw·SQL/Backup·State/Plan·Credential은 Git에 올리지 않고 논리 참조/보관·접근 책임으로 연결합니다.
5. 아래 Index와 관련 작업 Issue·[공통 진행표](../execution/WORK_TRACKER.md)에 링크를 연결합니다. 실패 Run을 보존하고 수정/재시험과 연결합니다.

발표 후보로 선별한 실제 Run은 [05 §0.7](../execution/05_IMPLEMENTATION_AND_VALIDATION.md#07-발표와-보고에-사용할-측정과-증거)의 별도 기준에 따라 [Issue #6](https://github.com/seokpan/seokpan-hybrid-docs/issues/6)에 원본 Run 링크와 간략한 후보 판정을 연결합니다. 실제 수치·로그·시간선의 정본은 이 Run이며 Issue에 복사하지 않습니다.

GitOps의 `releases/<release-id>.json`은 후보/선언이며 Docs의 Run과 구분합니다. 후보 안에 후보 자신을 포함한 GitOps SHA를 넣지 않습니다. 실제 Run은 Commit 후 실제 사용 GitOps SHA를 기록합니다. `_template/release.json`은 승인 필드의 빈 Run 양식이며 새 Validator/파이프라인 구현이나 최종 검증을 의미하지 않습니다.

## Recovery time calculation

복구 예행 후 기존 Run의 시각 계산에는 Python 3.9 이상과 표준 라이브러리만 사용하는 [계산 보조 도구](../tools/recovery_metrics.py)를 선택해서 쓸 수 있습니다. 저장소 루트에서 실행합니다.

```bash
python3 tools/recovery_metrics.py evidence/<test-id>/<run-id>/release.json
```

도구는 파일을 읽고 JSON 결과를 표준 출력에 표시합니다. 원본 다섯 파일·판정·checksum을 수정하거나 새 Run을 만들지 않습니다. 종료 코드 0은 계산 처리 완료(미측정 포함), 2는 입력/읽기 오류이며 시험 PASS/FAIL이 아닙니다. 빈 양식은 `UNMEASURED`와 null을 출력합니다.

| 출력 | 의미 / 사용 조건 |
| --- | --- |
| `rto_seconds` | 사고부터 `business_resumed_at_utc`까지의 시간 차이. 실제 업무/Data 확인 완료를 시간선·Raw 근거로 확인해야 함. Import 시간과 구분 |
| `data_time_difference_seconds` | 입력된 Data 기준 시각과 사고 시각의 차이. 확인 전에는 정확한 RPO나 보장 상한으로 사용하지 않음 |
| `rpo_seconds` | 기본 null. 선택한 Backup의 실제 Data 시각과 `data_reference_level`·Marker/복원 근거를 Reviewer가 확인했을 때만 아래 옵션으로 계산. 보수적 경계/시계 불확실성이 남으면 옵션을 쓰지 않고 summary에 범위·제한 기록 |
| `dump_seconds`, `import_seconds` | 입력된 단계 시작/종료 간 차이. 전체 RTO와 합산하지 않음 |

```bash
# 실제 Data 시각의 정확성을 근거로 확인한 경우에만 사용
python3 tools/recovery_metrics.py evidence/<test-id>/<run-id>/release.json --confirmed-data-time
```

옵션은 Reviewer의 확인을 명시하며 도구 자체의 증명이나 새 `data_reference_level` Enum이 아닙니다. Backup ID·확인 수준·관련 시각이 없으면 거부합니다. ISO 시각의 시간대가 없거나 시각이 역전되거나 기존 `rto_seconds`/`rpo_seconds`와 계산이 다르면 오류를 표시합니다. 오프셋 있는 시각은 UTC로 정규화해 계산하지만 Run의 UTC/KST 기록 규칙은 유지합니다. UTC 표현 범위를 벗어난 시각도 입력 오류(exit 2)로 거부합니다. 선택 Backup의 Data 기준·Dump 시작/종료가 존재하는 Import·업무 복귀 시각보다 뒤인 경우는 중간 시각이 누락돼도 거부합니다. 사전에 만든 Backup을 허용하며 사고 이후에 Dump가 시작돼야 한다거나 Data 기준이 Dump 시작 이전이어야 한다는 새 제약은 두지 않습니다. 도구는 timeline.csv·metrics.csv·Raw·Backup 무결성·시계 동기화·데이터 손실을 검사하지 않으며 전체 Run Validator가 아닙니다.

검토한 수치만 기존 metrics.csv의 적절한 `metric_id`/`actual`/`unit`/`condition_ref`/`raw_artifact_ref`에 기록하고, 계산 근거·불확실성·미달은 summary.md에 남깁니다. 파일을 바꿨으면 기존 지침대로 checksums.txt를 갱신합니다. 목표 비교·Acceptance는 승인 기준과 실제 증거로 별도 검토하며, 한 Run의 차이로 운영 RPO 상한이나 전체 서비스 복구를 보장하지 않습니다.

도구 자체의 검사는 `python3 -m unittest discover -s tools -p 'test_recovery_metrics.py' -v`로 실행합니다. 합성 시각으로 수행한 코드 검사이며 실제 T17/T18 실행이나 발표용 실측 근거가 아닙니다.

<a id="recovery-design-review-inputs"></a>
## Recovery design review inputs

현재 승인된 목표/주기 설계는 [03 §3-I.14.5](../design/03_DETAILED_DESIGN.md#recovery-design-decision-20261005)의 **RTO10분·영속 DB RPO30분·DB 운영 중 Portable Backup15분·기존 Backup/Restore 유지**다. 이 개정은 [Docs #30](https://github.com/seokpan/seokpan-hybrid-docs/pull/30)으로 main에 병합됐으며 이전30분/90분/1시간 승인 이력과 구분한다. 이미 수행한 아래 두 부분 Run의10파일·빈 Target/null·NOT RUN 판정은 소급 수정하지 않는다. 실제 운영 Timer/Backup 경로·사고 시작부터 지정 클라이언트 업무/Data 완료의 전체 Run이 있어야 새 목표 달성을 판정한다.

정상 성공 경로에서는 실제 성공 Data 최대 간격G＋Data→로컬 사용 가능한 완성본 지연D＋시점/시계 불확실성U≤30분을 관측한다. nominal15분을 G≤15분 또는 D≤15분 보장으로 대체하지 않는다. jitter/생략·전송/Storage/VM 장애·이전 사본 선택은 실제 사용 Data 나이와 손실로 기록하고 초과는 미달, 시점 미확인은 null/미판정으로 남긴다.30분은 채택된 프로젝트 시험 요구사항이며 실제 사업 사용자의 손실 허용 승인이나 상용 SLA가 아니다.

복구 목표의 설계 판단은 [03 §3-I.14](../design/03_DETAILED_DESIGN.md#recovery-design-review-20261003), 최소 예행의 입력·측정은 [05 §9.2~9.6](../execution/05_IMPLEMENTATION_AND_VALIDATION.md#recovery-objective-review-20261002)를 따른다. 기존 Run 다섯 파일과 [HANDOFF](../execution/HANDOFF_TEMPLATE.md)를 사용하며 새 스키마·시험 ID·상시 자동화를 추가하지 않는다.

현재 새 Redis에서의 사용자 기능 범위는 [03 §3-I.14.4](../design/03_DETAILED_DESIGN.md#recovery-app-scope-20261005)를 따른다. 고정 [h-app Source c12b3d15](https://github.com/seokpan/seokpan-hybrid-app/tree/c12b3d15a4dd2c806fac4326a9eb30ed6e8a81b3)의 [Game 결과 계약](https://github.com/seokpan/seokpan-hybrid-app/blob/c12b3d15a4dd2c806fac4326a9eb30ed6e8a81b3/backend/src/seokpan/game/application/service.py)과 [현재 결과 화면](https://github.com/seokpan/seokpan-hybrid-app/blob/c12b3d15a4dd2c806fac4326a9eb30ed6e8a81b3/frontend/src/game/GamePanel.tsx)을 근거로 기존 완료 DB 기록 보존과 현재 방 결과 조회를 구분한다. 아래 Fixture DDL의 출처는 같은 개정의 [20260901 Migration](https://github.com/seokpan/seokpan-hybrid-app/blob/c12b3d15a4dd2c806fac4326a9eb30ed6e8a81b3/backend/migrations/versions/20260901_0001_stone_game_v1.py)·[20260902 Migration](https://github.com/seokpan/seokpan-hybrid-app/blob/c12b3d15a4dd2c806fac4326a9eb30ed6e8a81b3/backend/migrations/versions/20260902_0002_game_participant_identity_expand.py)이며, 실제 Migration CLI/운영 Schema/데이터 검증과 구분한다. Source는 [h-infra Draft PR #29](https://github.com/seokpan/seokpan-hybrid-infra/pull/29)와 Run의 정확한 Infra SHA를 연결한다.

기존 CSV의 식별자는 다음처럼 사용할 수 있다. 아래는 기입 안내이며 실제 이벤트·측정값이 아니다. 시각/Actual을 측정하지 못했으면 빈 값을 유지하고 summary에 이유·범위·불확실성을 남긴다.

| 기존 파일 / 기입 예 | 입력할 실제 근거와 조건 |
| --- | --- |
| timeline.csv: `backup_data_reference:<backup-id>` | 사본별 Data 시각/경계·확인 수준과 보호 원본 참조. 게임/회원 naive 시각의 최댓값이나 Dump 종료로 대체하지 않음 |
| timeline.csv: `backup_local_complete:<backup-id>` | 로컬 사용 가능한 완성본 확보 시각과 무결성/가용성 근거. S3 업로드 완료와 구분 |
| metrics.csv: `backup_local_delay_seconds` | 같은 사본의 Data 시각→로컬 완성 차이, 단위 seconds. Data 시점이 불확실하면 정확한 값으로 취급하지 않고 범위/제한을 기록 |
| metrics.csv: `successful_backup_data_gap_seconds` | 인접한 사용 가능한 성공 사본들의 Data 시각 차이. 보호 로그 참조·관측 기간·표본 수·누락/실패·집계 조건을 함께 기록 |

선택 사본 한 개의 RPO와 정상 경로의 성공 사본 간격/확보 지연은 별개다. 관측 최대값을 운영 보장으로 확대하지 않으며 중단·이전 사본 선택·복원 실패는 실제 사용 Data 시각으로 별도 판단한다. App 작성/DB 기본값 시각의 Source 해석과 실제 행 미확인은 [05 §9.14](../execution/05_IMPLEMENTATION_AND_VALIDATION.md#recovery-timezone-handoff-20261003)에 연결한다.

지정 클라이언트 위치·접속·로그인/업무·처리 범위는 summary의 조건에 기록한다. 네 사람의 추가 구현/학습/운영/인계/재시험·문서/발표와 실제 가용시간, 암호문 크기/보관/전송·DB 부하/추가 가동 비용은 기존 HANDOFF·I07과 담당 Issue 원본을 연결하고 예상/실측/미측정을 구분한다. 숫자를 모르는데 0 또는 완료로 채우지 않는다.

## Run Index

| Test/Case·Requirement | Run·환경 | 실행자·Reviewer | 실제 Source/Release | Render/Deployment/Acceptance | 증거 링크 | 실패/후속 Run·제한 |
| --- | --- | --- | --- | --- | --- | --- |
| T18의 Data 부분 예행 / 최종 T17·T18 미실행 | `fixture-20261005-01` / 새 임시 MariaDB의 로컬 TCP 합성 Fixture | 배정 책임 C 김상희. 격리 로컬 합성 시험. C 리뷰·D Index 검토/수신 대기 | App `c12b3d15a4dd2c806fac4326a9eb30ed6e8a81b3`, Infra `4a4ee1b6762502be1e2ddf12d451e45205fdca03`; 실제 Image/Release 없음 | 모두 NOT RUN; 합성 Data 부분 실행만 PASS | [Summary](T18/fixture-20261005-01/summary.md)·[Release](T18/fixture-20261005-01/release.json)·[Metric](T18/fixture-20261005-01/metrics.csv)·[Timeline](T18/fixture-20261005-01/timeline.csv)·[Checksum](T18/fixture-20261005-01/checksums.txt), Source [h-infra Draft PR #29](https://github.com/seokpan/seokpan-hybrid-infra/pull/29) | MariaDB 10.11.14이며 실제 기준 11.8.9와 다름. 동시 쓰기 없는 합성 데이터·동일 Host 복사, 실제 RDS/S3/VPN·TLS/목적 계정·App/Redis/접속·전체 RTO/RPO 미측정. 운영 Backup 자동화/최종 Acceptance 아님 |
| T18의 합성 Backend 업무 연결 부분 예행 / 최종 T18 미실행 | `business-fixture-20261005-01` / 새 임시 DB·TLS/AUTH Redis·HTTPS Backend, loopback | 배정 책임 C Data/B App/D 증거, 실제 Host A. 격리 로컬 합성 시험. C/B 영역 리뷰·D Index 검토/수신 대기 | App `c12b3d15a4dd2c806fac4326a9eb30ed6e8a81b3`, Infra `29b4a1f01bd555edeebac946cd8ee174da4432ab`; 실제 Image/Release 없음 | 모두 NOT RUN; 합성 Backend 부분 실행만 PASS | [Summary](T18/business-fixture-20261005-01/summary.md)·[Release](T18/business-fixture-20261005-01/release.json)·[Metric](T18/business-fixture-20261005-01/metrics.csv)·[Timeline](T18/business-fixture-20261005-01/timeline.csv)·[Checksum](T18/business-fixture-20261005-01/checksums.txt), Source [h-infra Draft PR #29](https://github.com/seokpan/seokpan-hybrid-infra/pull/29) | Fixture MariaDB/Redis 버전·새 목적 SSL 계정/TLS의 부분 조건. age 복원→새 Redis→Backend HTTPS 로그인/랭킹→새 게임 FORFEIT 완료/현재 결과·SQL Rating 검증. FE/browser/WSS·Image/OCP/Host·RDS/S3/VPN·사고 탐지/판단/안내·과거 개별 결과 HTTP 미검증; 전체 RTO/RPO null |

## Required Boundaries

- UTC ISO 시각과 KST가 같은 시각인지 확인하고 불확실한 시점은 제한으로 남깁니다.
- RTO는 장애 시작부터 대표 업무/Data 확인까지, RPO는 사고와 실제 사용 Backup의 Data 기준 시각 차이입니다. Dump 종료/파일 수정 시각으로 대체하지 않습니다.
- DB 영속 Data와 Redis Runtime 손실을 구분합니다. 복구 명령 성공만으로 업무 복구 PASS가 아닙니다.
- 모든 Run에 적용되지 않는 항목은 summary의 제외 범위에 이유를 남깁니다. N/A는 전체 성공축을 생략하는 수단으로 쓰지 않습니다.
- JSON은 조합/실행 정보, CSV는 수치/시간선, Markdown은 해석을 맡습니다. 실제 값은 원본에서 연결하고 중복 기록이 충돌하면 원본·대상·개정·시점을 확인합니다.


## Source 부분 검사 Run — 전체 Runtime Acceptance와 구분

| Test 준비 | Run/환경·실제 수행자 | Source/원 결과 | 판정·제한·다음 입력 |
|---|---|---|---|
| T09 준비의 구독 오류 경계 | [provider-cleanup-20261007-01](T09/provider-cleanup-20261007-01/summary.md), Windows·GitHub Actions Linux. 배정 B; D Index 리뷰/수신 대기 | [App Draft #20](https://github.com/seokpan/seokpan-hybrid-app/pull/20) `e3488953b0f51b1a54dc7899a8a57c8024c54c13`, [CI37605414615](https://github.com/seokpan/seokpan-hybrid-app/actions/runs/37605414615) | Source 부분28PASS·Linux 기본1774/부분집합47/별도Lua9 PASS. Windows 정식FAIL과 baseline 재현 보존. 실제 Valkey/WSS/T09 Acceptance NOT RUN. 사람 리뷰/병합·새 Image·B 소비 수락 필요 |
| 저장소 전수 Source 조사·T09/T18 최종판정 제외 | [source-audit-20261007-01](T09/source-audit-20261007-01/summary.md), Windows격리도구/GitHubActionsLinux, Git계정tjung03·사람리뷰미수신 | [종합조사](../execution/REPOSITORY_AUDIT_20261007.md)·[GitOps25 CI37624059074](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37624059074) | App174·Frontendunit269/UI36·GitOps25Linux69·Docs14+16PASS. GitOps조합Windows70PASS/3기존FAIL. 실제Runtime/새Image/전체T09/T18·Cost 미판정 |


### 공개 기록·문서 출처 검사

- [T09/public-record-integrity-20261008-01](T09/public-record-integrity-20261008-01/summary.md): 문구·환경 메타데이터·출처 해시·체크섬 및 기존 문서/지표 검사. 소스 검사 범위이며 실제 Runtime·배포·전체 T09/T18 미수행. [Docs72](https://github.com/seokpan/seokpan-hybrid-docs/pull/72) 리뷰·Index 수신은 별도 확인.


<a id="registration-review-followup-20261008"></a>
### 등록 리뷰 후속 Source 검사 — 2026-10-08

[T09/registration-review-followup-20261008-01](T09/registration-review-followup-20261008-01/summary.md)에 GitOps25의 SHA B 비교 PASS/A 불일치 BLOCKED·Windows66PASS/3FAIL·정확53314d3 Linux69PASS와 재리뷰 요청을 연결한다. App20/22·Infra43은 현재 HEAD 승인·Source 추가 수정 없음, 병합 후 새 Image/실환경 수락은 별도다. Controller/State/Cloud/DB 실행·새 TH/Q 완료 없음. 병합·브랜치 삭제 결과와 새 승인 수신은 원 PR에서 후속 확인한다.

- [병합 Source ROSA/OCP 준비 검사](T01/plan-source-readiness-20261008-01/summary.md): fmt/helper/harness 보존·등록 비교/전체lab Gate PASS, Controller TCP22 연결 실패·실제 Plan NOT RUN. 공식 T01/Runtime 완료와 별도.

- [Recovery Host Source·Controller CA 확인 결과 수신](T09/recovery-host-20261008-01/summary.md): GitOps31 정확 HEAD Linux69PASS, Windows64PASS/5FAIL, Recovery Gate BLOCKED. B의 jth@ansible CA 해시 일치 결과 수신; ConfigMap/DB 연결·복원/실제 ROSA Plan 미실행. 새 Index 연결 제출, D 수신 대기.

## Controller 인증·정책 조회 부분 검증

- [T03/redhat-policy-read-20261008-01](T03/redhat-policy-read-20261008-01/summary.md): 실제 실행 B/jth@ansible. API 인증·Classic 필수5/5·보호 사본 생성 성공, Operator7/8·OCM 참조4/4. 현재 파일 권한/해시·누락 ID·A 수신 대기. AWS/IAM 변경·Plan/Apply·전체 T03/ROSA 수락 미수행. [원 Infra25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25#issuecomment-6053637165) 연결, D Index 검토/수신 대기.

- [T03/policy-bundle-readback-20261008-01](T03/policy-bundle-readback-20261008-01/summary.md): B/jth@ansible의 저장 사본 현재 권한·17파일 해시 일치 PASS, AWS VPCE 정책 누락 ID 확인. 앞선 조회 Run의 당시 미확인 기록 보존. 실제 Operator/ARN Map·A 전달/수신·외부 원본 진위·API/AWS/IAM/Terraform·전체 T03은 미확인/미실행. D Index 수신 대기.

## 2026-10-08 Controller 목록·독립 Source Run 연결

- [T03 controller-source-catalog-20261008-01](T03/controller-source-catalog-20261008-01/summary.md): B/jth@ansible의목록/보관ID대조·Source지연/Lock/Core 보고수신,PARTIAL. A실제IAM/지원/CloudPlan 미완료.
- [App30 Linux Run37752274074](https://github.com/seokpan/seokpan-hybrid-app/actions/runs/37752274074),HEAD3c924927·Artifact11537878750·전체1786/부분집합47/Lua9 failure/error/skip0·Source만PASS.
- [GitOps33 Linux Run37752286969](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37752286969),HEAD78ad1393·Artifact11537863510·발견=실행73/진단렌더8체크섬PASS·Source만PASS.
- 공개RunIndex 연결과D수신확인 구분. 기존진단Source6ea2d9a의추가ZIP은같은PC경로이며Runtime/금고독립사본 대체 아님.

### 동일 PR 리뷰 제안 보완의 새 Source 검사

- [App30 Run37759276727](https://github.com/seokpan/seokpan-hybrid-app/actions/runs/37759276727): HEAD cf8ef2cae927bfc6d13da8e0c7a7f918e09974ca·Artifact11541900559·전체1798/부분집합47/Lua9 failure/error/skip0. ZIP SHA256 c9988031df9fb263cf9b24fd25f5c3e3dbcacde139159a2fba3ac3ecd547e890, 만료2026-11-07T09:51:03Z.
- [GitOps33 Run37759280003](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37759280003): HEAD275cc640cad34532502beba453f109d5697f898c·Artifact11541945097·발견=실행76 PASS/진단렌더8체크섬PASS. ZIP SHA2561b27c8f0d0b7ad578cc52f704c24897d7abd199495adfb1a5a9379b9115cfb26, 만료2026-10-15T09:49:30Z.
- 최초 두 Run과 승인은 당시 HEAD 이력. 새 커밋 D 재리뷰 요청 완료·승인/병합 대기. Controller T03 부분 Run의 실제 수신 기록을 재작성하지 않으며 Cloud/Runtime PASS 가산 없음.

## Full·Controller 실제 후속 — 2026-10-08

- [T09/full-e2e-ui-followup-20261008-01](T09/full-e2e-ui-followup-20261008-01/summary.md): B 로컬 Windows·Memory Backend. clean3126 Full2/UI36·unit278/tooling81 PASS, 실제 Image/OCP/SQL/Valkey 미검증.
- [T03/controller-source-provider-20261008-01](T03/controller-source-provider-20261008-01/summary.md): B/jth@ansible c5 Source/Lock·격리 Root validate PASS, 최초 mock BLOCKED·버전39후보/STS UNKNOWN. 실제 Cloud Plan 미실행.
- [T03/controller-oidc-mock-retry-20261008-01](T03/controller-oidc-mock-retry-20261008-01/summary.md): 최초 필수 입력 오류7개 → 합성 var-file 교정 후 실제 exit0·named2/summary2 PASS, Source/Lock/원 로그 보존. AWS/RHCS·운영 Backend/State 미실행.
- D Index 수신 대기. Source 정적/모의 시험을 전체 T03/TH/Q/DR/Cloud/Cost 수락으로 가산하지 않음.
