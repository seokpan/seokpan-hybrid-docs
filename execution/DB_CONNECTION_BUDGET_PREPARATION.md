# DB Connection Pool 연결 예산 준비

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
