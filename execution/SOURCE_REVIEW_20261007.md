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
| 실제 입력 대기 | B 금고 본인 확인·독립 사본, C/D Data/Schema/CA/사용창, A 기반 출력/SG·B Caller/Backend·지원/비용 |

현재 확인한 두 수정 경로의 재검증에는 추가 실패가 없지만, 그것을 전체 저장소 Q10 수렴으로 확대하지 않는다. Q02/03/04/05/10의 미완료는 조사 대장에 유지한다. Q01/06/07/08/09/11/12와 TH81/실제 완료2는 자동 변경하지 않는다.

기록은 이 문서→원 Issue/PR/Run, WORK_TRACKER·05의 연결로 유지한다. 00–04와 Project v3의 설계는 바뀌지 않았으며 단순 실행 상태 변화 때문에 재등록하지 않는다. 실제 금고·클러스터·ROSA·Data 이관·전체 T18·Cost PASS는 이번 Source 검증에 포함하지 않는다.
