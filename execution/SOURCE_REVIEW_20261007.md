> **현재 재개 기준:** [§11](#b-work-current-delta-20261007)·[work 인계](WORK_HANDOFF_20261007.md). §1–10의 수치/상태는 해당 시점의 이력이다.

### 조사 중 추가된 실행 보고·수정 PR — 2026-10-07 후속 조회

[D 등록·선택 Sync 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5#issuecomment-6034601393)는 SHA A의 Valkey 4객체 `Succeeded`·FE/BE 미생성을, [Pod 확인](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6#issuecomment-6034590906)은 검토 Digest의 amd64 하위 ImageID·허용 UID만 보고했다. 등록/Sync를 다시 미실행으로 되돌리지 않는다. 실제 TLS/AUTH/Hostname·Ready 전체 Run과 Prune/Delete 차단은 아직 근거가 없으며 공유 Owner 재확인·등록 Commit·B 공유 시각의 빈칸 및 사전 합의되지 않은 `oc patch operation.sync.resources` 경로는 원 #5에서 보완·수락한다. #21의 완료 체크만으로 이 잔여를 완료 처리하지 않는다. 이 조사자는 클러스터를 직접 재조회하지 않았다.

[GitOps #27](https://github.com/seokpan/seokpan-hybrid-gitops/pull/27)로 checker 정책이 main에 반영됐다. [#25](https://github.com/seokpan/seokpan-hybrid-gitops/pull/25)의 현재 변경은 회귀 테스트·등록 안내2파일이며 HEAD `53314d33fcc061e5de4da2f8d3570edd6d5a7273`의 [Linux CI37706970618](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37706970618)에서69PASS를 확인했다. 현재 등록 Source는 Workload SHA B=`bfee2669e62bf823969ce224e5599eccace5d024`를 참조한다. SHA B 비교는 선언 구조 PASS/Runtime NOT VERIFIED, SHA A=`244b48b885d7ac645c402e561a032ae65a8f3461` 입력은 불일치 BLOCKED다. 기존 #24 이후 checker 실패·3파일 변경·옛 HEAD 검증은 당시 이력이다. 최신 검증/범위의 PR 제목·본문과 안내를 정정해 A 재리뷰를 요청했다. Controller/Workload YAML·실제 등록/Sync·전체 release Gate·공유 충돌/Prune/Delete 보호는 유지한다.

[Infra Draft #43](https://github.com/seokpan/seokpan-hybrid-infra/pull/43)은 ROSA `workspace_key_prefix=phase2/rosa/env`와 목적 Role의 List 범위를 맞춘다. default State Key는 유지한다. 기존 harness/보존 검사 PASS, 보조 로컬 fmt/validate는 NOT RUN 이력이다. [정확 PR HEADd5aeddd의 CI37598580155](https://github.com/seokpan/seokpan-hybrid-infra/actions/runs/37598580155)는 Core1.16.4/AWS6.67.0/RHCS1.7.7의 fmt·backend=false/readonly init·validate(errors0/warnings0)·Schema13종·OIDC mock2·Source/Lock 불변 PASS다. 실제 Backend 인증·Workspace 조회·Cloud Plan/Apply는 NOT RUN이다. 누락만으로 기존 init 실패를 단정하지 않는다. 검토·병합 후 본인 clone/Workspace와 실제 Caller/Backend를 확인한다.

[GitOps #26](https://github.com/seokpan/seokpan-hybrid-gitops/issues/26)은 후속 조회에서 Stage2의 실제 추적 Issue로 확인됐다. [D의 backend-db-runtime 공급 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6#issuecomment-6034843156)는 두 URL 키·계약 Host/DB 이름과 기존 lab 계정 비밀번호 공유를 명시한다. Secret 미공급으로 되돌리지 않되 실제 새 URL 접속·C 형식/GRANT·데이터 출처 수락은 대기다. Route/Origin·새 Backend Image·Stage2 활성화/전체 Gate도 미완료다.

첫 읽기·작업 위치·실행 조건은 [실행 인계](EXECUTION_ENTRYPOINT_20261007.md)를 따른다. 원 보고와 이 Source 수정의 수신/검토·실행은 별개다.


# S1–S4 Source 검토 — 2026-10-07

> 담당: B 정태훈(tjung03)  
> 상태: S1의 두 결함 재현·수정·회귀·PR 제출 완료. S2의 새 lab 선언 및 직접 의존 대조, S3 이력 색인 보완. 전체 전수 의미 검토/Q10은 미완료.  
> 원 작업: [App #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4#issuecomment-6029248805), [Build 인계 #2](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-6029292025), [GitOps #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10#issuecomment-6029297406), [Docs #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21)

## 1. 사용 Source와 수집 범위

| 저장소 | 시작 main | 작업 중 반영할 변경 |
|---|---|---|
| App | `bdaa9dfa0a09e5d8efb1714ccf62860315b1346e` | 독립 수정 PR #17/#18. 기존 승인 Image는 그대로 |
| Infra | `0f47617816b74365f5911ba2e273013ae82d6612` | #38 병합 유지. 실제 Caller/기반 출력·Data 입력은 별도 |
| GitOps | `12d78ac547729f0e314abfb2ac6238c95b1f3bd7` | D #19가 `de130af839626c9d0a030580693a4060c41c9abd`에 병합 |
| Docs | `fff5ac222243a231e5473f4ab39f87aa6cc10f6f` | #68 병합·Project v3 등록 확인. 이 검토의 새 문서 변경은 별도 |

[수집·기준선 Run 37557035447](https://github.com/seokpan/seokpan-hybrid-docs/actions/runs/37557035447)에서 공개 refs/PR HEAD를 포함한 Git Bundle, 고정 Source, 전체 Issue/PR 목록·일반/inline 댓글·milestone·Workflow Run 목록과 페이지 연결을 확보했다. 이 수집은 01:25:40~01:25:53 UTC의 순차 관측이며 원자적 전체 Snapshot이 아니다.

수집 당시 일반 Issue47개·PR94개·일반 댓글187개·inline댓글0개·Branch11개·Workflow Run117개, 페이지응답29개·수집오류0건이다. 리뷰 제출/thread의 전면 갱신은 이 수집 Job에 포함하지 않았으며 이전 수집·이번 지정 PR 조회와 구분한다. 이후 #19 병합과 이 작업의 새 PR/Run은 별도 관측으로 연결한다.

Artifact `11455536698`, ZIP SHA256 `dd9b2ef9224239fcf7bf79286177b97a2a15c8335829fa54392ee27776d26f0f`. 저장된 SHA256 목록과 파일/Bundle을 대조했다. Branch만 복원하면 빠지는 PR HEAD refs까지 로컬 색인에 포함했다. 저장 refs별 도달 이력은 App98·Infra110·GitOps48·Docs175, 합계431개다. 각 부모·변경 경로·diff 해시와 문서/구현/통합/임시 작업 분류를 보존했다. **이는 모든 과거 diff·CI 로그의 의미 검토 완료 건수가 아니다.** 이전 시점393개와 현재431개를 동일 순간의 증감으로 단정하지 않는다.

## 2. S1 확인한 Source 연결

| 검토 축 | 직접 대조한 경로/동작 | 결론·남은 경계 |
|---|---|---|
| 접속/설정 | `connection_contract.py`, `connection_settings.py`, `settings.py`, MariaDB/Redis connection/settings, `test_hybrid_connections.py` | Runtime/Migration 목적 자격·정확 Host/Port·별도 AUTH·명시 CA/TLS·실패 경계를 유지. 실제 공급값/서버 연결은 별도 |
| DB 시간·Pool | MariaDB connection/settings·game_adapter의 시간 변환/transaction/finalization, Game persistence contract | 게임 UTC-naive·DATETIME(3)/복원UTC와 DB세션/회원 CURRENT_TIMESTAMP 구분. 두 Runtime Engine·Migration NullPool, Pool3+2/60은 미채택. 실측/설정 합의 전 크기·세션 시간대를 바꾸지 않음 |
| 생성·종료 | `production.py`, `production_app.py`, App 서비스 생성/lifespan 연결 | 첫 startup 취소 지점에서 runner 누수 재현 → F11 수정. 정상 종료·Readiness·provider 순서 회귀 |
| 영속/Runtime 최종화 | `game/application/resolution.py`, `captured_completion.py`, `persistence.py`, `game_adapter.py`, Redis turn_coordinator와 vote runtime command | DB 확정·불명 후 확인, 공유 Resolver·퇴장/재시도·DB-before-Runtime·후속 통지 실패 경계를 대조. 실제 다중 Pod/Failover 성공으로 확대하지 않음 |
| Lua 쓰기/거부 | `vote_scripts.py` apply_resolution과 Adapter/명령, 기존 실제 Lua fixture·버전 검사 | board HSET 뒤 기한 거부로 일부 상태가 남는 F12 재현·수정. 전체 Room/Session/Generation Lua 전수 검토와 별개 |

위 표는 관련 경로 검토 범위이며 App의 모든 함수와 모든 테스트가 수작업 검토됐다는 의미가 아니다. 서비스 생성 호출부 외 App 전체 라우트, Room/Session/연결 세대의 남은 Lua·WS lifecycle, Frontend 전체 경로와 과거 이력의 의미 검토는 계속 남는다. CI 통과도 그 검토를 대신하지 않는다.

## 3. F11 — startup 취소 시 runner 정리 누락

원 코드가 runner를 만든 직후 첫 `await asyncio.sleep(0)`을 정리 `try/finally` 밖에서 실행했다. 그 지점에서 startup이 취소되면 provider context는 닫히지만 runner의 취소/join 구간에 진입하지 않는다. 실제 App lifespan 함수와 대역 provider/services를 사용한 결정적 시험에서 Task가 살아 있는 상태로 provider가 종료됨을 확인했다.

[App #17](https://github.com/seokpan/seokpan-hybrid-app/pull/17), HEAD `367938f08e735fe123827b3c9362307b5d59408f`: runner 생성 직후부터 기존 try/finally가 책임지도록 이동했다. 정상 종료/취소 전파·runner-stop-before-provider-close·runtime 참조 해제·registry 종료·불필요한 SIGTERM 호출 부재를 2개 Case로 확인한다. 제품 Source와 새 테스트2파일만 변경했다.

[Run 37557811841](https://github.com/seokpan/seokpan-hybrid-app/actions/runs/37557811841): 기존 Source+새회귀는 취소1FAIL/정상1PASS, 수정2PASS. 전체 Backend1754·별도 runner47 PASS, JUnit failure/error/skip0. trigger `051766ab21bd70502dbc157a1f5c277689d1600f` 뒤 임시 workflow만 제거한 최종 HEAD와 구분한다. Artifact `11455364455`, ZIP SHA256 `0e1f7864d82af842c8e1416ec0778c0c5f23aab619842a983366f02c1764ba05`를 내려받아 CRC/로그/두 출력 바이트를 대조했다.

운영에서 이미 발생한 사고라는 보고나 여러 번 반복되는 강제 취소·프로세스 강제종료의 모든 경우를 해결했다는 주장은 아니다. 최초 자식 Task 생성 전 실패와 별도 종료 정책은 현재 시험 범위를 따른다.

## 4. F12 — Lua가 거부를 반환했는데 board는 변경되는 경로

`apply_resolution`은 board Hash에 좌표를 쓴 뒤 다음 기한을 검사했다. 동일/이전 기한이면 `INVALID_NEXT_DEADLINE`을 반환하지만 이미 작성한 좌표가 남고 game JSON은 이전 상태다. 다음 정상 재시도는 그 좌표를 이미 점유한 것으로 판단할 수 있다. 다른 명령이 끼어들지 않는 Lua 실행 특성과 애플리케이션 거부 시 이전 쓰기의 취소는 같은 보장이 아니다.

[App #18](https://github.com/seokpan/seokpan-hybrid-app/pull/18), HEAD `971c4a56590200cfa75bab8ba8f23d968d85edd3`: ACTIVE 다음 기한 검사를 board HSET 앞으로 옮겼다. Script9→10이며 Runtime Schema·외부 API·게임 규칙은 유지한다. 기존 버전 기대값2곳과 실제 Lua 시험2개를 함께 변경했다. 모두4파일이다.

[Run 37559151544](https://github.com/seokpan/seokpan-hybrid-app/actions/runs/37559151544): 기존 Lua+새실제5Case는 기존3PASS/새2FAIL, 수정5PASS. 거부 뒤 snapshot/raw game 불변 및 같은 Resolver의 정상 재시도 성공을 확인했다. 기본 Backend1752·별도 runner47도 PASS다. opt-in Lua5개와 기본suite는 별도이며, 별도 runner47은 기본suite와 중복되므로 고유 Case 총수로 더하지 않는다.

검증은 Python3.13.15·uv0.12.5·기존 Lock, 기존 fixture가 요구한 공식 Redis7.2.4 Source `d2c8a4b91e8c0e6aefd1f5bc0bf582cddbe046b7`의 소유된 빈 loopback/비영속 프로세스에서 수행했다. 종료·포트 해제를 확인했다. **Valkey를 Redis OSS로 되돌린 결정이 아니며 Valkey7.2 실제 Image/TLS/AUTH·Cloud 호환성 PASS가 아니다.** 해당 조합은 실제 환경에서 별도로 확인한다.

적용 작업 트리의 해시를 확인하고 검사했으므로 summary의 `dirty=true`와 trigger `ddf5622126c1bccd9ba7e090c43606f3e4336ddd`를 보존한다. 검사한4파일을 그대로 게시한 최종 HEAD를 trigger와 동일시하지 않는다. Artifact `11455848128`, ZIP SHA256 `df3ee46adde36b6a8c2d9f848717dec28666db2395d35a46d205f41a62314320`의 CRC/red-green/기본CI/게시SHA/네 출력 바이트를 다시 대조했다.

기본 runner의 정상 양수 기한 계산은 바꾸지 않았다. 모든 Lua 오류에 rollback을 추가한 변경이 아니고 운영 장애·외부 공격 경로를 재현했다는 주장도 아니다. [Redis 공식 scripting 경계](https://redis.io/docs/latest/develop/programmability/eval-intro/)와 [rollback 설명](https://redis.io/blog/you-dont-need-transaction-rollbacks-in-redis/)을 참고하되 결함 판정은 해당 코드와 red/green 결과에 근거한다.

## 5. S2 — lab 새 선언과 Recovery/CI의 직접 조건

[D GitOps #19](https://github.com/seokpan/seokpan-hybrid-gitops/pull/19)는 검토 HEAD `2215aff8d4e49bcde0d5e66ce6a0769870a76605`의 기존 B 변경 요청(StatefulSet Kind·롤백)을 해소하고 승인·병합됐다. 10:30:33 KST 병합 main은 `de130af839626c9d0a030580693a4060c41c9abd`. 부모#18과 PR HEAD의 3-way tree는 실제 병합 tree `c809a609d844125ec17a25d42501364a951324a2`와 같아 #18 문서 변경도 보존된다.

기존 [B 승인 리뷰](https://github.com/seokpan/seokpan-hybrid-gitops/pull/19#pullrequestreview-5436531268)는 Source40검사·8진단 Render/26객체·lab12객체와 Artifact 확인을 기록한다. 이 리뷰/검사는 해당 수행 기록으로 수신했고 새로운 승인·실제 클러스터 실행으로 반복 기록하지 않는다. 기존 ‘D 초안/선언 없음’ 대기는 해소됐다.

| 경로 | 코드·인계 대조 | 다음 직접 조건 |
|---|---|---|
| lab | Valkey7.2.14 내부 Digest·TLS/AUTH include/env·0440·임의 UID·emptyDir/noeviction·0Replica·StatefulSet Kind 허용 | 실제 AppProject 등록 개정·권한/live Diff·사용창, Image/CA/Secret 읽기와 DNS/SAN·Service/Ready·DB/Schema·목적 자격/Route 수락 |
| Recovery | `redis.yaml`·`redis.conf`·Kustomization·`render_release.py`/관련 Source 검사. 현재 redis-server/TCP Probe·Volume/Digest 보류 | 승인 Recovery Valkey Image·binary·TLS/AUTH Probe·Storage/UID를 선언/renderer/테스트와 같이 개정. lab Digest·Storage 정책을 임의 복제하지 않음 |
| Writer/Promotion | `scripts/promote_gitops.py`는 1차 repo/path, dry-run 전에도 PAT/API/clone 사용. 현재 Jenkinsfile은 해당 helper를 호출하지 않고 gitops_change=NONE | D #15의 순수 plan/mock·기본 비활성 Source는 준비 가능. 실제 Push/PR만 #14의 자격·등록·범위 검증 필요. 두 이슈 전체 완료를 서로 선행조건으로 묶지 않음 |
| 새 Backend | F11/F12는 기존 승인 Image에 들어 있지 않음. FE Source/현재 Digest 변경 없음 | C/D 리뷰·실제 병합 SHA → D Build/Scan/Digest → B의 Backend·held Migration 동반 개정·실제 동일 조합 Run |

현재 helper/Pipeline 대조는 Promotion 입력·실행 금지/보류 경계 중심이다. 전체 Jenkins 단계·실제 Job/Credential·Registry API·권한 거부·재생성 시험의 완료 판정은 아니다. Source의 보류값을 임의로 채우지 않았다.

## 6. S3–S4의 처리와 남은 조사

현재 원격 Source와 Bundle의 PR refs를 연결했고 기준선/두 수정의 전체 CI 및 red/green을 직접 내려받아 확인했다. 신규 PR은 현재 base와 변경 경로를 대조하고 임시 workflow가 최종 제품 Tree에 남지 않도록 처리했다. 새 Source 두 건은 서로 다른 파일을 수정하며 기존 Image를 자동 승격하지 않는다. 두 PR을 결합한 실제 병합본·Image의 결과는 별도로 확인한다.

| 상태 | 범위 |
|---|---|
| 완료 | F11/F12 재현→수정→동일 회귀→기존 CI→게시 바이트 확인→원 Issue/리뷰·Build 인계 |
| 완료 | #18/#19 실제 병합·기존 문서 보존·초안 대기 해소와 활성화 직접 입력 분리 |
| 계속 | Room/Session/연결 세대·WS의 남은 Source/시험 분기, 전체 Source의 파일·함수별 검토 수준 |
| 계속 | 모든 과거 PR/Commit diff의 의미 검토·누락된 최신 리뷰/thread·CI job log/artifact·외부 참조/anchor |
| 실제 입력 대기 | C의 jth 해독/해시 보고·B 수신 완료를 반영하고 독립 키 사본/복원 확인만 별도 유지. C/D Data/Schema/CA/사용창, A 기반 출력/SG·B Caller/Backend·지원/비용은 각 직접 조건 |

현재 확인한 두 수정 경로의 재검증에는 추가 실패가 없지만, 그것을 전체 저장소 Q10 수렴으로 확대하지 않는다. Q02/03/04/05/10의 미완료는 조사 대장에 유지한다. Q01/06/07/08/09/11/12와 TH81/실제 완료2는 자동 변경하지 않는다.

기록은 이 문서→원 Issue/PR/Run, WORK_TRACKER·05의 연결로 유지한다. 00–04와 Project v3의 설계는 바뀌지 않았으며 단순 실행 상태 변화 때문에 재등록하지 않는다. 실제 금고·클러스터·ROSA·Data 이관·전체 T18·Cost PASS는 이번 Source 검증에 포함하지 않는다.

## 7. 종료 전 병행 변경 수신과 문서 통합

[Docs #69](https://github.com/seokpan/seokpan-hybrid-docs/pull/69)의 기존 HEAD `fe61e5b0a68a38038685d252c12ac853a2d92d44`에서 금고 보고/B 수신·Valkey 단독 준비·ROSA/Pool 입력이 이미 정리됐다. 이 내용을 덮어쓰지 않고 본 검토의 두 App 수정과 인계를 같은 PR에 결합했다. C의 [Docs #71](https://github.com/seokpan/seokpan-hybrid-docs/pull/71) main `5b8c529e50e480ce1aa6e83a95caee8d9c877908`의 §8.14와 Tracker 행도 보존했다.

[Infra #39](https://github.com/seokpan/seokpan-hybrid-infra/pull/39)는 `ceb6fad7b8976941ad93b2b67dbecafd1e0c0959`에 병합됐다. C 기록의 A bootstrap Apply/No changes는 해당 실행 보고이며 본 검토의 직접 AWS 실행이 아니다. 10/8 foundation은 Plan만, Apply는 전체 Plan·팀 리뷰·Cost 이후이며 날짜 미확정이다. Cloud 금고 해독 보고·B 수신은 완료됐고 Controller 밖 독립 키 사본/복원 검증은 별도로 남는다. 실제 C 입력을 기존 미수신 문구로 되돌리지 않는다.

첫 문서 게시 Run37560736306은 수정된 임시 스크립트를 제거하는 단계에서 git rm이 거부해 게시 전 중단됐다. 검토한6파일의 내용 검사는 통과했고 제품 코드 실패가 아니다. 임시 스크립트만 원상 복원 후 제거하도록 고쳐 Run37561183514가 성공했으며, 산출물 Commit `ee0f3158c91af858d39b89a7cd47c2c681ff16aa`를 이번 통합의 고정 입력으로 사용했다. 이전 실패와 성공을 합치지 않는다.

통합 검사 Run37561651049는 Tracker에 김상희 행이 하나뿐이라고 잘못 가정한 검사에서 게시 전 중단됐다. 실제로는 권한·입력·작업의 세 표에 각 행이 있으므로 세 행 전체의 바이트 보존을 검사하도록 정정했다. Source/문서 손실로 판정하거나 실패를 성공에 포함하지 않는다.


<a id="b-review-followup-20261007"></a>
## 8. 승인 제안·PubSub·경로 A·Recovery 후속 — 2026-10-07

§1–7은 이전 체크포인트다. Docs69는 main078d9e에 병합됐고 기존 d7f0e619 브랜치는 보존한다. 현재 작업은 다음 원 PR과 실행 문서의 단일 현재 구획으로 연결한다.

| PR / 정확한 Source | 검증과 인계 |
|---|---|
| [App17](https://github.com/seokpan/seokpan-hybrid-app/pull/17) `367938f08e735fe123827b3c9362307b5d59408f` | 제품 Source 불변. 최종 HEAD의 Run37564888138에서1754/부분집합47 PASS·dirty=false. registry 단일/다중 참조와 Source/배포 rollback 설명을 보완하고 D 재검토 요청 |
| [App18](https://github.com/seokpan/seokpan-hybrid-app/pull/18) `5a8a8de85400687ca53ab286cbe96658935983f4` | close_turn(None)의 Lua 오류/ProviderUnavailable 오분류 수정, cjson.null·Script11·지속 Source CI. 최종 Run37566223434에서1752/부분집합47/별도회귀9 PASS·dirty=false. 최신 D 재리뷰 필요 |
| [App19](https://github.com/seokpan/seokpan-hybrid-app/pull/19) `1cc717ba4e6c7bc14d7778a6d2e2b0417d8332fc` | PubSub 소유권 이전 전 취소 정리. Lobby/Room×subscribe/버전 읽기의 기존4FAIL→수정4PASS. Run37566764240에서 최종1756/부분집합47 PASS·dirty=false. C/D 리뷰 요청 |
| [GitOps20](https://github.com/seokpan/seokpan-hybrid-gitops/pull/20) `b671871d2914b0a2bb541acbca19fd75601473d5` | 경로 A 등록 비교13개+기존40=53 PASS, Run37567731179. 진단8Render/26객체·Source 불변. 실제 Manifest/입력/등록값은 변경하지 않음. D 리뷰 |
| [Infra40](https://github.com/seokpan/seokpan-hybrid-infra/pull/40) `c1a495bc2569c745d84dbcac27dc055596e8b5b1` | C38 제안 반영: 기능14.4/목표14.5 구분·운영 차이 Metadata·오래된 설계 대기 README 정정. Run37568085720의 결과 생성기10 PASS. C/D 리뷰 |

App은 Python3.13.15·uv0.12.5·기존 Lock/format/lint/mypy/coverage 기준을 유지했다. 최종 JUnit failure/error/skip0이며 runner47은 기본 suite의 부분집합이라 합산하지 않는다. App18 회귀9 중 Apply(None)1개는 기존 Python guard,8개는 Adapter/Lua 경로다. 첫 Run37565398120은 실제8PASS/close_turn(None)1FAIL이었지만 검사 계획이2FAIL을 예상해 게시 전 중단됐다. 이 가정을 정정한 Run37565832829에서 red/green과 clean 후보를 확인했고 최종 PR CI도 통과했다. 이를 두 Lua 결함으로 기록하지 않는다.

각 Run의 Artifact를 내려받아 CRC·Source/도구·JUnit/로그·출력 해시를 확인했다. App 수정/Infra 출력은 포함된 Git Bundle의 blob과 로컬 검토 바이트도 대조했다. null 후보의 숨김.github 파일은 별도 업로드되지 않아 Bundle에서 확인했다. 정확한 Artifact ID/ZIP 해시는 원 PR에 기록했다. GitOps는 Python3.12.3/PyYAML6.0.2/Kustomize5.7.1과8개 YAML 체크섬, Infra는 Python3.12.3의 Metadata 시험이다. 회귀용 Redis7.2.4·합성 PubSub 시험은 선택 Valkey7.2 실제 Image/TLS/AUTH/Cloud 검증이 아니다. Infra도 실제 백업/복원 Run을 새로 실행하지 않았고 C_OPERATIONAL_DATA_REVIEW·RTO/RPO null·전체T18 NOT RUN을 유지한다.

### 8.1 이번 Source 대응과 남은 의미 검토

session_scripts의 create/touch/rotate/restore/revoke에서 raw CAS·절대/idle TTL·보상 시각을, room_scripts/presence_scripts와 disconnects에서 서버TIME·Generation/Lease·낡은 disconnect·입장/퇴장·owner/tombstone 후속을 대조했다. api/realtime·stream_access·snapshots·realtime_scripts/adapter에서는 session/binding/generation 재검사와 버전·통지공백·소유권을 연결했다. PubSub 이전 취소만 App19로 수정했다. 나머지 Room start_intent/start_capture/start_completion/start_closure/runtime·identity 응용 보상/경쟁·Frontend 전체와 시험 대응은 남는다. 현재 읽은 경로가 전체 App 수작업 검토 완료를 뜻하지 않는다.

S2는 Recovery 선언/renderer와 실제 Valkey Image·binary·TLS/AUTH Probe·Storage 입력, C의 합성 검토와 운영 검토, App15 Promotion/App14 Writer의 Source/mock 준비와 실제 자격/Push/PR를 구분한다. 경로 A의 등록 비교는 [#5 B 동의](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5#issuecomment-6030172661)를 따른다. D의11:53 KST4조 조건부 사용 수락은 수신했고 실제 등록 시 유효 조건을 확인한다. Workload 입력 PR→확정 전체 SHA→별도 등록값 PR로 진행하며 새 Root/Controller는 없다. Valkey 준비의 독립성을 미해결 lab 전체 Overlay Sync 허가로 읽지 않는다.

원 결과는 [App4](https://github.com/seokpan/seokpan-hybrid-app/issues/4#issuecomment-6030568884), 실제 병합 조합의 Build/Scan/Digest는 [App2](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-6030574985), 등록/실제 입력은 [GitOps10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10#issuecomment-6030599770), C 제안 수신은 [Infra38](https://github.com/seokpan/seokpan-hybrid-infra/pull/38#issuecomment-6030602922)에 기록했다. App17/18/19는 독립 HEAD 검사이며 승인 후 실제 병합 조합·Image·Runtime은 별도다.

### 8.2 S3 수집과 S4 종료 경계

수집 Run37564888138의03:02:47~03:03:48 UTC 순차 관측은144페이지·명시적 오류0, Branch16·일반Issue48·PR99·일반댓글208·inline댓글0·Review제출81·WorkflowRun129다. 목록/페이지 연결과 PR HEAD refs·42개 파일/Bundle 해시를 확인했다. Artifact11458298273 ZIP SHA256은 `551df71dd5b7048acdfcb608a70d1409400a5b6682c3c89be6061e9adac45141`이다. 이후 신규 PR/Branch/Run은 별도 조회다. 지난431개 commit 색인을 현재 완료 건수로 재사용하지 않는다. 모든 과거 diff·CI 로그/산출물·GraphQL thread 해결 상태의 의미 검토는 아직 아니다.

이번 수정의 Source→시험→원 Issue/인계→현재 문서 파급을 재검증하되 Q02/03/04/05/10 전체는 미완료다. 다음 시작점은 위 잔여 App/Frontend·Recovery/CI 시험 대응, 과거 diff/CI/참조 의미 검토와 최종 원격 변경 대조다. 본인 독립 키·Caller·Data/Route/비용 입력은 별도 직접 조건이며 이 조사 전체를 대기시키지 않는다. 00–04·그림·과거 Evidence·TH81/실제 완료2는 유지한다.


<a id="b-review-resume-20261007"></a>
## 9. 중단된 재리뷰 대응의 게시·산출물·현재 입력 확인

이 절은 §8 이후의 개정이다. 이전 Source/시험/리뷰는 고정 이력으로 보존하며 전체 S1–S4 완료를 뜻하지 않는다.

| 원 작업 | 최신 Source/상태 | 검증과 남은 조건 |
|---|---|---|
| App17 | 367938f08e735fe123827b3c9362307b5d59408f, open | 기존 APPROVED commit_id가 동일한 사실과 보완 결과에 대한 새 제출 미확인을 구분. 원 댓글6032849213의 재검토 요청 유지 |
| App18 | d624c83081f18ad81c793cfe39e81ce6075abfba, 재리뷰 대기 | Run37583252239: 전체1752/부분집합47/별도Lua9·failure/error/skip0·clean. Artifact11465476865 ZIP7430b6ee49f3d3cb96a3842115b6ac250baa51d75e3ca12450966e9a5240828f 재확인 |
| App19 | f548f921c436d614a3fe0b3969161b8d1433ab5f, 재리뷰 대기 | Run37584439948: 이전1cc717+새8Case에서4FAIL/4PASS→최종8PASS, 전체1760/부분집합47·clean. Artifact11465659044 ZIPbc51bad5ac7b6025ed4e7e5ad1cc1383c6b697825d56a8178f53e8c0bafc09f1 재확인 |
| GitOps20 | b13ae9575206a335a9e6f87efc34dd4c198884f7, A/D 재리뷰 대기 | Run37583920937 전체58PASS·8진단Render/26객체. Artifact11465856605 ZIP9e1056f9f37e6fa4fc113ff1176d0160e127c366a3ddfc856481589e50be925b, Source/8YAML hash 대조 |
| Infra40 | a0da58c345f877659e522a5b4ab5392b1d0626d3 병합, 브랜치 삭제 | C 승인5438510467·Source3파일·기존10단위검사. 삭제Run37583271261·branches 재조회 확인. 실제 Data/T18은 별도 |

App18은 D의 중복 push/PR CI·로컬 opt-in 순서 제안을 수용했고 필수검사 전환/캐시 추가는 별도 범위로 유지했다. App19는 RedisError가 취소를 가리는 경계를 실제 대역 회귀로 재현해 RedisError만 억제하고 원 취소를 전파한다. 정리 시도1회가 정리 성공을 보장하지 않는다. 첫 Run37583804408의 Ruff SIM105 실패는 정책 비활성화 없이 suppress 표현으로 정정한 뒤 재시험했다. GitOps20은 A의 metadata 지적에 annotation exact allowlist·빈 labels·추가 metadata 음성 검사를 보완했다. 기존 승인/Changes requested를 임의로 최신 승인으로 바꾸지 않았다.

세 ZIP의 실제 바이트 SHA256·CRC, App JUnit/summary·clean Source, GitOps Render hash를 재검증했다. App19의 Docs workflow trigger61874395와 검사 대상 Appf548f921은 다르다. 개별 Source CI를 결합 main/새 Image/실제 Valkey·Controller·전체 업무 PASS로 합치지 않는다.

lab의 최신 D작성/B리뷰·Stage1 전용Gate·SHA A/B 순서는 [원 #5 인계](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5#issuecomment-6032629690)로 연결한다. Stage1 PR에서는 unittest뿐 아니라 기존 Source workflow의 진단 Render에도 모든 Workload replicas0 검사라는 직접 의존이 있다. 이 검사를 삭제/우회하지 말고 승인 Stage1 경계를 반영한다. FE/BE/base/Recovery/Migration 보류를 보존하며 실제 Stage1 Gate 구현은 D의 후속 PR이다.

Cost는 [원 #43 대조](https://github.com/seokpan/seokpan-hybrid-docs/issues/43#issuecomment-6033030041)를 따른다. 파일(3) SHA2561e7186febf71e16f72d6a92c406b9d1709e8e64839a8101fb913c4f126644383, 저장 판정 PARTIAL/미완19/입력오류0/기타4다. CP3/Infra3/Worker3 유지, 필수 disk와 실제 LB/Volume/Window/Destroy·가용시간은 미확인이다. 읽기 도구의 일부 수식 해석 차이를 원본 파일 오류로 단정하거나 재저장하지 않았다. 과거 단가를 새 검증 가격으로 승격하지 않는다.

본인 금고 시도는 복원 파일 검사에서, clone 시도는 경로/필수파일 초기 검사에서 중단돼 실제 복호화/Cloud 권한 실패로 판정하지 않는다. [직접 실행 안내](TJUNG03_WORKFLOW_AND_LEARNING_GUIDE.md#b-direct-actions-20261007)에 준비·전송·정확한 파일명·누락 진단·검사·회신을 반영했다. 명령의 문법/합성 검사는 본인 Runtime 성공이 아니다. 00–04/Project v3/그림/TH81·완료2는 변경하지 않는다.


<a id="b-review-closeout-20261007"></a>
## 10. 리뷰 처리 종료와 승인된 결합 main 검증

이 절은 §8–9 이후의 실제 결과다. 중단 로그에서 App17의 새 리뷰를 확인하지 못했던 상태는 D의 5438988132(검토 HEAD367938f), App18은5438973472(HEADd624c830), App19는5438977533(HEADf548f921)의 재승인으로 해소됐다. 새 의견의 필수 제품 수정은 없었다. raw payload의 apply_resolution null 직접 Lua 시험과 정상 Provider 오류 경로에서 cleanup RedisError가 원 오류를 가리는 경계는 선택/후속 검토로 [work W10](WORK_HANDOFF_20261007.md)에 남겼다. 실제 코드 변경 없이 리뷰 수신과 후속 범위를 기록했다.

| PR | 실제 squash 병합 SHA | 결과 |
|---|---|---|
| App17 | `5e2bdc1490ebe6baf53e303db55a3aac42771976` | 기존 runner 기동 취소 정리 및 2개 Case 보존 |
| App18 | `4dd1213315edff97a3ecb4286eae058de90de157` | board 거부 순서/null·Script11·지속 CI 및 명령 순서 보존 |
| App19 | `a2afffb8605dafff1cb5b9af215aa0cf93aadcdb` | PubSub 이전 취소/cleanup RedisError 경계와 8개 Case 보존 |

정확한 결합 main **a2afffb8605dafff1cb5b9af215aa0cf93aadcdb**에서 [Run37589421928](https://github.com/seokpan/seokpan-hybrid-app/actions/runs/37589421928)의 정식 workflow를 실행했다. Backend1762 PASS·부분집합 runner47 PASS·별도 Lua9 PASS, 각 최종 JUnit failure/error/skip0, 기존 Lock/sync·format/lint·mypy·coverage PASS, Python3.13.15/uv0.12.5·dirty=false다. 이 값은 개별 PR 검사 수의 합산이 아니다.

Artifact11467549120 / ZIP SHA256 `5bca559ae4368a192d91a1ccb652ca22f58a23922df68540dd9fbb9b43d2158e`의 CRC·summary·세 JUnit·Source SHA를 다운로드 후 대조했다. [정리 Run37589531720](https://github.com/seokpan/seokpan-hybrid-app/actions/runs/37589531720)은 세 PR의 merged/head/merge SHA와 결합 main의 파일 동일성을 확인한 뒤 exact ref lease로 세 작업 브랜치를 삭제했다. 정리용 Branch도 삭제했고 main/다른 Branch/과거 Run은 보존했다.

[App2 실제 Build 인계](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-6033610765)에 결합 Source·Run·Artifact 보존 기한을 연결했다. 실제 Build/Scan/Digest·Valkey Image/TLS/AUTH·lab/Cloud 업무/T18/비용 수락은 별도다. 기존 회귀용 Redis7.2.4·대역 Provider/PubSub 시험을 실제 Valkey 배포 시험으로 확대하지 않는다.

GitOps20의 b13ae957/58PASS/A·D 재리뷰 요청은 유지한다. Infra40의 병합·브랜치 삭제는 완료다. Docs69는 main 대비 ahead0/files0이라 삭제 가능하지만 질문에 대한 판단만 했으며 보존한다. Docs72는 새 main7114e837의 C Prefix 결정/기록을 결합하고 병합 대기한다. C의 Docs74 설계 결정과 미병합 Infra42 Source/실제 백업 상태는 별도다. 03을 Infra2로 변경하지 않고 Cost PARTIAL/미정 입력을 유지한다.

이번 종료 범위는 리뷰 대응·가능한 병합/브랜치 정리·실제 결합 CI·개인 실패 절차/문서·인계다. 남은 Room start_*·identity/Frontend·Recovery/CI·과거 diff/CI/thread/참조와 실행/비용/발표/종료는 [work 인계 W01–W13](WORK_HANDOFF_20261007.md)에 담당·입력·명령/검사·종료 기준으로 남긴다. Q10 전체 수렴이나 TH/T의 실제 완료를 추가하지 않는다.


<a id="b-work-current-delta-20261007"></a>
## 11. work 재개 원격 변경 대조와 현재 실행 입력

§1–10의 Source/검사·리뷰 대기와 Runtime 관측은 해당 시점 이력으로 보존한다. 현재 검토 기준은 [실행판 상단](TJUNG03_EXECUTION_BOARD.md)과 [work W01–W13](WORK_HANDOFF_20261007.md)다. 이번에는 기존 App17/18/19 수정을 재작성하거나 1762검사를 새로 수행한 결과로 기록하지 않고, 승인된 결합 Source a2afffb8605dafff1cb5b9af215aa0cf93aadcdb와 기존 CI·D Build 인계를 재사용한다. 새 Backend Build/Scan/Digest·App/별도 held Migration의 같은 승인 Image 연결은 남는다.

GitOps20은5dc2bd546de1acbbeb47a380c85103ce2b31017f에 병합·브랜치 삭제되어 이전 재승인 대기가 해소됐다. GitOps22의 Stage-1/Gate Source는244b48b885d7ac645c402e561a032ae65a8f3461에, GitOps24의 등록 Source는a25172c7453b9d7999cb1f3cbeb1ef35774e3b63에 병합됐다. #24 targetRevision은 #22의 Workload SHA A다. Valkey1·FE/BE0·Migration suspend/current/300초·base/Recovery hold·전체 release Gate 보존을 소비하며 같은 Source를 다시 만든다는 안내를 종료한다. 실제 Controller 등록·보호 옵션·선택 Sync·Pull/Ready/TLS/AUTH/업무 Run은 원 #5/#6의 실제 결과에서 별도 판정한다.

Infra42의36dc2403aa77e2896cc4ec3c545b92e0afb49205 병합으로 periodic/·backup_periodic_retention_days Source 대기는 해소됐다. 실제 tfvars·Plan/Apply·Backup은 별도다. C Valkey 본체 해독 보고/B 수신과 B SQL 금고 jth 확인/C 세 계정 확인은 완료 보고이며 Controller 밖 독립 키/암호문 사본·복원 검사는 남는다. 정확한 원 댓글·Docs77의a9b0207b563aa25be17d4a635f6cc903fbe0e74a 병합/공급 범위는 [W06/W09](WORK_HANDOFF_20261007.md)에 연결한다. 이 환경이 실제 금고/Runtime을 재실행한 결과는 아니다.

기존 03·04 종료,DR10분/RPO30분/15분 계획 주기,CP3/Infra3/Worker3,Cost PARTIAL/$450/$500,TH81/실제 완료2를 유지한다. Source·리뷰·인계·실행·시험 판정은 계속 구분한다. Room/identity/Frontend·Recovery/CI·과거 이력의 남은 의미 검토와 실제 Runtime 검증을 전체 완료로 올리지 않으며 Q10은 미완료다.
