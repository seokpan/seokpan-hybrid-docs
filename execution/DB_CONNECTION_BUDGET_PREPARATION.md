# DB Connection Pool 연결 예산 준비

## 실행 가능한 예산 대조 — 2026-10-11

기존 예산식을 [오프라인 검사기](../tools/b_preflight/db_connection_budget.py)로
구체화했다. 실제 RDS 조회·인증·App 설정 변경·Cloud 활성화는 수행하지 않는다.
아래 과거 Source 기준의 "Pool 입력 필드 없음"은 당시 상태이며, 이번 App 후보는
명시적 입력 경로만 준비한다. 운영값·timeout·부하 기준 채택과 실제 시험은 별도다.

### App 후보와 병합 기록

현재 후보는 App main `b8cab6caa348f2e89a7ad08594becf203ddbf67d`를 기준으로 한
`feat/runtime-pool-inputs-20261011`의 로컬 변경이며 아직 게시·병합하지 않았다.
`SEOKPAN_DATABASE_POOL_SIZE`·`SEOKPAN_DATABASE_MAX_OVERFLOW`·
`SEOKPAN_DATABASE_POOL_TIMEOUT_SECONDS`를 모두 공급하면 Identity/Game 각각에
같은 Pool 값을 적용하고, 모두 미지정이면 기존 생성 옵션을 유지한다.
최종 입력 이름과 구현은 App 리뷰 결과로 확정한다. 예산 검사기는 Engine별 값을
표현할 수 있지만 이번 App 후보가 Engine마다 다른 값을 받는다는 뜻은 아니다.

이 오프라인 검사기의 병합에 App 병합이 기술적으로 필요한 것은 아니다.
두 PR을 함께 진행할 경우 App 리뷰·Linux CI·병합 후 이 문서에 App PR 링크,
병합 Commit, 검증 결과와 실제 RDS/Cloud 시험의 미확인 범위를 기록한다.
App 리뷰로 입력 계약이 바뀌면 설명과 시험을 재대조한 뒤 Docs를 병합한다.
App 후보가 미병합 상태라면 그대로 명시하고 검사기만 독립적으로 병합할 수 있다.

값을 채우지 않은 [입력 예시](../tools/b_preflight/db-connection-budget-input.example.json)를
개인 보호 경로에 복사한 뒤 수신한 상한·예약·Process·Pod·Engine별 값을 연결한다.
Linux에서는 입력을 본인 소유의 일반 파일600으로 공급한다. Windows ACL 검증은
이 도구에 포함하지 않는다. A/C/D에게 새 양식을 요구하지 않고 B가 받은 자료를 대조한다.

```bash
python3 tools/b_preflight/db_connection_budget.py /본인/보호경로/budget.json
```

`steady`·`surge`·`terminating` 각각에 연결을 보유할 수 있는 Pod 수, Pod당 Process 수,
Identity/Game 각각의 pool_size와 max_overflow를 명시한다. 종료 중 Pod가 없다는
사실도 확인 후 0으로 넣으며 미확인을 0으로 대신하지 않는다. 그룹별 계산은
`Pod × Process × (Identity 상한 + Game 상한)`이고, 관리/백업/Migration 등 전체
추가 연결 예약을 한 번 더한다. 구/신 Pool 값이 다르면 각 그룹에 대응하는 값을 넣는다.
한 그룹에 여러 설정의 Pod가 섞이면 이 검사기의 그룹별 단일 설정으로 정확한
혼합 합계를 표현할 수 없다. 그 그룹의 최대 Process 수와 Engine별 최대 연결
상한을 전체 Pod에 적용하는 보수적 입력으로 대조한다. 구성별로 따로 계산한
각 부분의 통과를 전체 통과로 해석하거나 평균값으로 축소하지 않는다.
롤링 중에는 아직 종료되지 않은 구 버전 Pod가 `steady`에도 남을 수 있으므로,
`steady`를 모두 신 버전 값으로 넣거나 구 버전 연결을 `terminating`에만 넣어
축소하지 않는다. `steady`·`surge`·`terminating`의 Pod는 중복 없이 세되,
연결을 보유한 종료 중 Pod는 별도 합계에 포함한다.

- 미입력(null): `INPUT_INCOMPLETE`, 종료 코드2. 빈칸을 기본값으로 채우지 않는다.
- 상한 초과: `DECLARED_CAP_EXCEEDS_LIMIT`, 종료 코드2.
- 선언 상한 이내: `WITHIN_DECLARED_LIMIT_PENDING_REVIEW`, 종료 코드0.
- 잘못된 구조·bool·소수 수량·무제한 Pool/overflow·중복 JSON 필드: `BLOCKED`, 종료 코드2.

종료 코드0도 `runtime_approval=false`다. 입력의 출처·최신성, 실제 Process/Pod 수,
종료 연결 유지 시간, 예약의 모든 소비자 포함 여부, timeout/recycle·부하·재접속,
사용창·배포 승인은 확인하지 않는다. 예시 3+2/60은 시험 Fixture의 수학 대조이며
운영값으로 채택하지 않았다. 기존 역할별 Engine2·Migration NullPool·Cloud0/hold·
첫 ROSA Plan과 Cloud App 활성화 조건의 분리는 유지한다.

## Source 기준과 실제 미확인

App main5df2ce280188a7e3874fa370ec8116d50ca34af3·GitOps main9d108349146f7a4734b2da1ea0fa9d56dae971ee 기준. Runtime Engine은 Process마다 Identity/Game2개, Migration은 NullPool. Pool 설정 필드/환경변수는 아직 없음. Cloud 기본은0/hold, 별도 승인 목표 Preview는Backend 3개·maxSurge 1개/maxUnavailable0. 3이 현재 실제 가동수라는 뜻 아님.

고정 SQLAlchemy 2.0.52의 AsyncAdaptedQueuePool 기본 5+overflow 10을 설치된 라이브러리에서 확인. 생성자만 준비하고 DB연결 호출0. Uvicorn Source 명령에 --workers 미지정, 기본Process 1개이지만 WEB_CONCURRENCY·실제 Image 명령/Process를 확인해야 함. [SQLAlchemy 공식 pooling](https://docs.sqlalchemy.org/en/20/core/pooling.html#sqlalchemy.pool.AsyncAdaptedQueuePool)과 대조. Pool은 필요할 때 연결을 열므로 다음 수치를 실제 열린 연결 수로 표시하지 않음.

## 예산식

동시 DB 연결을 보유할 수 있는 Pod수 × Pod당Process 수 × 각Engine의(pool_size+max_overflow) 합계 + 관리/백업/Migration/여유 예약 ≤ 실제 @@max_connections. 종료 중 연결이 남는 Pod도 포함하고 실제 Process/Replica/Engine·Rolling 조건이 바뀌면 재계산.

| 조건 | Process 1개·Engine2·각5+10 가정의 Pool 상한 | 실제 판정 |
|---|---:|---|
| Backend 1개 | 30 | 실제Process·부하·RDS상한 미확인 |
| 목표Backend 3개 | 90 | Source 예산, 현재 연결수 아님 |
| 목표3+Surge 1개 | 120 | 종료 중 Pod 제외한 계산 |
| 연결이 남은 종료 중 Pod T 포함 | 120+30×T | T와 종료/재접속 실측 필요 |

C의 예약 10개을 함께 쓰면 네 번째 행은130+30×T와 실제 상한을 대조. 예약 10개의 구성은 db_admin 관리·backup_dump 최대 2·Migration 1개·여유이며 실제 사용/추가 예약 기준을 C가 확인. maxSurge 1개을 실제 전체Pod/연결 상한으로 쓰지 않음. 반복 배포/종료 지연에 따른 T도 관찰.

## 다음 입력·구현

1. B/D: 실제 승인 Image 명령·WEB_CONCURRENCY/Process·Replica/Rolling·종료 중 Pod/연결 확인.
2. C: RDS 생성 뒤 실제 @@max_connections·예약 구성/여유·계정별 연결 기준 공급.
3. B/C: 상한과 timeout/정리/재접속·부하 기준 합의. 기존3+2/합계60은 미채택 후보 유지, 이 식의 확정값으로 사용하지 않음.
4. B: 합의 후 App 설정 필드/환경변수·범위/거부 검사/회귀 구현, D새Build/Scan/Digest→GitOps소비 연결. 현재 임의값/미구현 환경변수 추가 없음.
5. 실제 시험: Max_used_connections·계정/전체동시연결·대기/연결오류·Rolling/종료·재접속·예약여유 확인. Source계산을 RDS/성능 PASS로 사용하지 않음.

원 [C v2.3 개정 예정](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6051212790)·[App4](https://github.com/seokpan/seokpan-hybrid-app/issues/4). 이 준비는 ROSA Root 첫 Plan의 전체 선행조건이 아니며 Cloud App 활성화 전에 실제 입력을 대조. 설계 수치·DB사양·Pool 값 채택/DDL/실제 접속 변경 없음.

## C 수신·Cloud App 활성화 조건 — 2026-10-08

C는 Data 수치기준 v2.2§2.6과 예산의 정합, 3+2/60 미채택, 실제 RDS 상한 뒤 B/C 결정, ROSA Plan과 분리에 동의했다. C의 기본식 예상은 max_connections85미만이며 실제 조회값이 아니다. 그 범위라면 정상3Pod의 기본 Pool 상한90만으로도 예산을 넘는다.

Cloud Backend 활성화 전 실제 상한·예약10·Process/Engine·Rolling/종료 중 Pod 예산을 수락하고 필요한 Pool 구현/설정·새 Image·GitOps 소비를 완료한다. 현재 Cloud0/hold 유지, 임의3+2·60 확정/환경변수 추가 없음. 첫 ROSA Plan의 직접 입력과 Cloud App 활성화 입력을 구분한다.
