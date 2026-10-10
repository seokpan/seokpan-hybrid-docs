# 승인 요구사항부터 다시 대조한 B 준비 범위 — 2026-10-11

- [x] Charter Must/성공축, 03 T·IF·IM·Network 조건, 04 역할, 05 측정·증거 규칙에서 출발해 네 저장소를 대조
- [x] OCP의 기존 bastion 조사와 공유 환경 담당 근거를 재사용하고 자원 확보 후보를 계산
- [x] 입력 없이 가능한 자원 비교·시험별 측정/증거 준비를 보완
- [ ] 실제 Cloud/OCP/Recovery 시험, 권한/창·자원 변경, 최종 비용·시연/종료

81개 TH 목록과 준비 자료 25개는 참조 목록이다. 이 문서는 그 목록 밖의 승인 세부 조건까지 대조한다. 아래 파일은 **관련 구현/절차/부분 Source 시험의 근거**이며 행 전체의 자동 시험 Coverage나 실환경 PASS를 뜻하지 않는다. 실환경 결과가 필요한 모든 행은 부분 증거를 보존하고 최종 수락을 미완료로 둔다. 새 시험 ID·운영 구조·수치 목표를 추가하지 않는다.

기준 main: App `b8cab6caa348f2e89a7ad08594becf203ddbf67d`, Docs `a380b0f727b934548cefd34fe85bea2508d6226b`, GitOps `34b362f0ca9a3f119e55f9557548b81a6012f930`, Infra `bbd1d5793fe32e79e02aab2833852c656933b758`. App43/Docs100의 미병합 Pool 입력·예산 검사기는 후보 준비로 별도 인정하며 이 변경에 복사하지 않는다.

## 성공축과 실행·증거의 연결

| Charter 성공축 | 승인 시험 연결 | 최종 확인 범위 |
|---|---|---|
| Migration Decision | T01·T22 | 구성요소 처리 방향·이유·원본/Seed·운영 책임 |
| Hybrid Connectivity | T04·T14·NET-01~10 | 실제 왕복 경로/Source·정상/금지 통신·Gateway 복구 |
| Infrastructure Reproducibility | T02·T19·IM-01~09 | 목적 Role/State·전체 Plan·Binding 보존/해제·재생성 |
| Application Migration | T05~09·IF-01~18 | 실제 이관/Schema·업무·다중 Pod·WSS |
| Availability / Failure | T10~14 | 정상 종료와 강제 장애·부분 실패/업무 재개 |
| Recovery / DR | T17~18 | 독립 검증본·Data 시점·전체 업무 복원/RTO/RPO |
| Observability | T15 | 장애→Metric/Log/Alert→판단의 시간/ID |
| Performance | T16 | 대표 업무 Client 지연·초회 오류/정확성·병목 |
| Cost | T20 | 전체 실비·잔존/재시도·삭제/자동 재시작 |
| Security | T03·T04·T07·T21 | 실제 인증/거부/회수·TLS·Secret/Image |
| Platform Value | T22 | 같은 기능/조건과 관리 책임의 비교 |
| Documentation / Presentation | T23 | 결정→Source/Release→실측→제한/영상 추적 |

Charter Must의 서비스/Data/State 배치는 T01·T05·T18·T19, CI/CD 경계는 T03·T21에 함께 연결한다. Should의 플랫폼 가치·UX·Rollback·Image 취약점·PDB/Deprecated API/Upgrade·추가 부하는 T06·T10~11·T16·T19·T21~22에서 검토하며 Must보다 앞선 새 기능으로 확대하지 않는다. [03 §3-G.4.2](../design/03_DETAILED_DESIGN.md#3-g42-플랫폼ci-검증-경계와-기존-should-처리)의 기준처럼 버전/업그레이드 지원과 Deprecated API/PDB 확인은 실제 대상 버전으로 남긴다. Could/Won't를 이 조사에서 실행 작업으로 추가하지 않는다.

## T01~T23 대조

| 승인 조건 | 기존 관련 구현·준비/부분 시험 | 실행·통합 담당 | 아직 필요한 실제 확인 |
|---|---|---|---|
| T01 설계·소유권·Source 대조 | [source](https://github.com/seokpan/seokpan-hybrid-docs/blob/a380b0f727b934548cefd34fe85bea2508d6226b/execution/REPOSITORY_AUDIT_20261007.md) | B/A/C/D | 실제 Seed·최신 Source·담당 및 인계 개정 대조 |
| T02 최초 Bootstrap→Remote 이전→Role 재실행 | [state](https://github.com/seokpan/seokpan-hybrid-infra/blob/bbd1d5793fe32e79e02aab2833852c656933b758/terraform/rosa/REVIEW_AND_EXECUTION_GATES.md) | A→B | B 목적 인증·State/Lock와 실패 해제. A bootstrap 성공을 B 결과로 승계하지 않음 |
| T03 계정/Secret·State·Plan·플랫폼 접근 보호 | [auth](https://github.com/seokpan/seokpan-hybrid-docs/blob/a380b0f727b934548cefd34fe85bea2508d6226b/tools/b_preflight/management_acceptance.py) | A/B/D | 실제 권한 주체·거부·신규/기존 Session 회수·Secret/Plan 노출 검사 |
| T04 Network·TLS·접근 실패 | [tls](https://github.com/seokpan/seokpan-hybrid-app/blob/b8cab6caa348f2e89a7ad08594becf203ddbf67d/backend/tests/persistence/test_hybrid_connections.py) | A/C→B | 실제 경로/SG와 정상·잘못된 CA/Hostname/AUTH의 성공·거부 |
| T05 Seed 이관·기본 Data 검증 | [migration](https://github.com/seokpan/seokpan-hybrid-docs/blob/a380b0f727b934548cefd34fe85bea2508d6226b/execution/FIRST_SERVICE_WRITE_STOP_PREPARATION.md) | C→B | 대상·접근·이관일→최종 덤프/행·관계 비교→App 확인 |
| T06 대표 E2E | [e2e](https://github.com/seokpan/seokpan-hybrid-app/blob/b8cab6caa348f2e89a7ad08594becf203ddbf67d/frontend/e2e/first-success.spec.ts) | B/D | 새 Image·실제 입력·사용창→대표 업무/SPA·잘못된 API 경로 |
| T07 사용자 인증/권한/만료 | [ws](https://github.com/seokpan/seokpan-hybrid-app/blob/b8cab6caa348f2e89a7ad08594becf203ddbf67d/backend/tests/websocket/test_stream_access.py) | B | 실제 다중 Pod의 타인/다른 Room·만료/로그아웃·Origin/Proxy |
| T08 중복·동시 쓰기·결과 불명 | [coord](https://github.com/seokpan/seokpan-hybrid-app/blob/b8cab6caa348f2e89a7ad08594becf203ddbf67d/backend/tests/persistence/test_redis_production_coordination.py) | B/C | 실제 다중 Pod 경쟁·응답 유실·DB 확정/불명과 중복 효과 |
| T09 WS 재접속·Generation·Snapshot | [race](https://github.com/seokpan/seokpan-hybrid-app/blob/b8cab6caa348f2e89a7ad08594becf203ddbf67d/backend/tests/application/test_kick_session_race.py) | B/D | 실제 WSS 단절/다른 Pod/세대·Snapshot·유휴/긴 대기/Heartbeat |
| T10 Rolling·Pod 종료/강제 삭제 | [rollout](https://github.com/seokpan/seokpan-hybrid-gitops/blob/34b362f0ca9a3f119e55f9557548b81a6012f930/tools/test_release_safety_manifests.py) | B/D | 자원/사용창→FE 이전 Pod 소멸→BE·정상/강제 종료 별도 시험 |
| T11 Worker 1대 장애 | [cloud](https://github.com/seokpan/seokpan-hybrid-gitops/blob/34b362f0ca9a3f119e55f9557548b81a6012f930/tools/test_cloud_platform_contract_manifests.py) | B/D | ROSA 실제 AZ 분산·Worker 장애/재배치. OCP 시험으로 대신하지 않음 |
| T12 RDS Multi-AZ DB Instance Failover | [runtime](https://github.com/seokpan/seokpan-hybrid-app/blob/b8cab6caa348f2e89a7ad08594becf203ddbf67d/backend/docs/production-runtime.md) | C/B/D | 실제 RDS Failover·Pool/대기·확정/불명 결과 |
| T13 Redis Failover·메모리/접근 오류 | [coord](https://github.com/seokpan/seokpan-hybrid-app/blob/b8cab6caa348f2e89a7ad08594becf203ddbf67d/backend/tests/persistence/test_redis_production_coordination.py) | C/B/D | 실제 Redis Failover/Key 손실/noeviction·DB 확정 결과 보존 |
| T14 WireGuard/On-Prem Jenkins 단절·Gateway 복구 | [state](https://github.com/seokpan/seokpan-hybrid-infra/blob/bbd1d5793fe32e79e02aab2833852c656933b758/terraform/rosa/REVIEW_AND_EXECUTION_GATES.md) | A/B/D | WG 한 종단점씩·Jenkins 단절·신규 Pull·경로/Source/Key 회수 |
| T15 관측·알림·판단 | [metric](https://github.com/seokpan/seokpan-hybrid-app/blob/b8cab6caa348f2e89a7ad08594becf203ddbf67d/backend/src/seokpan/metrics.py) | D/B/C | 실제 장애와 시각/ID·Metric/Log/Alert/판단 연결 |
| T16 정상 부하·추가 부하 | [metric](https://github.com/seokpan/seokpan-hybrid-app/blob/b8cab6caa348f2e89a7ad08594becf203ddbf67d/backend/src/seokpan/metrics.py) | D/B/C | Client HTTP/업무 WS·초회 오류/정확성·자원/Pool 실측 |
| T17 Backup 생성·S3/On-Prem 검증·실패 | [backup](https://github.com/seokpan/seokpan-hybrid-infra/blob/bbd1d5793fe32e79e02aab2833852c656933b758/tools/recovery_fixture/README.md) | C/D/B | 완성/Hash/복호화/import·실패 시 이전 검증본 보존 |
| T18 Offline Restore-based Recovery | [recovery](https://github.com/seokpan/seokpan-hybrid-gitops/blob/34b362f0ca9a3f119e55f9557548b81a6012f930/tools/check_recovery_bundle.py) | C/B/D | 대상·독립 사본·복원 계정→AWS/GitHub 없는 FE/WSS/업무/Data·RTO/RPO |
| T19 rosa 삭제→Terraform Clean Recreate | [state](https://github.com/seokpan/seokpan-hybrid-infra/blob/bbd1d5793fe32e79e02aab2833852c656933b758/terraform/rosa/REVIEW_AND_EXECUTION_GATES.md) | A/B/C/D | Binding 해제/기반 보존·재생성 후 새 SG/Host/Secret/Pull/정상 Plan |
| T20 Window 종료·잔존 자원·Cost | [cost](https://github.com/seokpan/seokpan-hybrid-docs/blob/a380b0f727b934548cefd34fe85bea2508d6226b/execution/05_IMPLEMENTATION_AND_VALIDATION.md) | A/B/C/D | 삭제 대상/잔존 NAT·IPv4·EBS·DB·Backup·과금/재시작 확인 |
| T21 CI Build/Test/Scan·Push vs Runtime Pull·Release 보존 | [release](https://github.com/seokpan/seokpan-hybrid-app/blob/b8cab6caa348f2e89a7ad08594becf203ddbf67d/scripts/test_release_candidate.py) | D/A→B | 실제 Build/Scan/Push·새 Worker/12시간 후/재생성 후 Pull |
| T22 1차/2차 운영책임·Platform 비교 | [presentation](https://github.com/seokpan/seokpan-hybrid-docs/blob/a380b0f727b934548cefd34fe85bea2508d6226b/presentation/PRESENTATION_BASELINE.md) | B/D | 같은 기능의 실측·관리 책임·서로 다른 조건/미측정 구분 |
| T23 재현 문서·시연·Evidence 완결 | [evidence](https://github.com/seokpan/seokpan-hybrid-docs/blob/a380b0f727b934548cefd34fe85bea2508d6226b/evidence/README.md) | 全員→B/D | 같은 Release/개정의 원본·실패·영상·Hash·비밀정보 제외 |

## 세부 조건을 생략하지 않는 대응

IF·IM·NET은 위 T 행의 세부 조건이다. 위 T의 일부 성공을 아래 모든 세부 조건 성공으로 확대하지 않는다. 제목 옆의 승인 원문에 허용/거부·실패 조건이 있다. 특히 NET-07은 초기 비활성/미허용 확인이며 활성화 요청이 아니다.

| 세부 조건 | 승인 원문의 대상 | 준비/검토에 연결할 T | 실환경 증거에 남길 구분 |
|---|---|---|---|
| NET-01 | Internet 사용자 → Public Ingress | T04 | 요청 Source/목적/왕복 경로·허용/거부·TLS/권한; 공개 IP/자격 원문 제외 |
| NET-02 | 팀 관리 주체 → Public API / Console·OAuth | T04 | 요청 Source/목적/왕복 경로·허용/거부·TLS/권한; 공개 IP/자격 원문 제외 |
| NET-03 | Application Worker → RDS | T04 | 요청 Source/목적/왕복 경로·허용/거부·TLS/권한; 공개 IP/자격 원문 제외 |
| NET-04 | Application Worker → Redis | T04 | 요청 Source/목적/왕복 경로·허용/거부·TLS/권한; 공개 IP/자격 원문 제외 |
| NET-05 | On-Prem 전용 Gateway → AWS VPN EIP | T14 | 요청 Source/목적/왕복 경로·허용/거부·TLS/권한; 공개 IP/자격 원문 제외 |
| NET-06 | 승인된 On-Prem Job Host /32 → RDS | T04 | 요청 Source/목적/왕복 경로·허용/거부·TLS/권한; 공개 IP/자격 원문 제외 |
| NET-07 | 승인된 Cloud 실행 주체 → On-Prem DB/작업 대상 | T04 | 요청 Source/목적/왕복 경로·허용/거부·TLS/권한; 공개 IP/자격 원문 제외 |
| NET-08 | On-Prem Backup/CI → S3·ECR·GitHub·AWS API | T04 | 요청 Source/목적/왕복 경로·허용/거부·TLS/권한; 공개 IP/자격 원문 제외 |
| NET-09 | ROSA → 필수 외부 Registry / Red Hat / GitHub / AWS API | T04 | 요청 Source/목적/왕복 경로·허용/거부·TLS/권한; 공개 IP/자격 원문 제외 |
| NET-10 | 관리 주체 → VPN EC2 | T04 | 요청 Source/목적/왕복 경로·허용/거부·TLS/권한; 공개 IP/자격 원문 제외 |
| IF-01 | 같은 Host의 FE·API·WSS 정상 접속 | T06 | 실제 환경·동일 Release·조건/원본 결과, 부분 Source 시험과 구분 |
| IF-02 | 없는 API/WS 경로·FE 새로고침 | T06 | 실제 환경·동일 Release·조건/원본 결과, 부분 Source 시험과 구분 |
| IF-03 | HTTP·Origin·Proxy Header·인증 오류 | T07 | 실제 환경·동일 Release·조건/원본 결과, 부분 Source 시험과 구분 |
| IF-04 | RDS/Redis 통신 단절·Failover | T12·T13 | 실제 환경·동일 Release·조건/원본 결과, 부분 Source 시험과 구분 |
| IF-05 | Redis 메모리 압박·쓰기 거부 | T13 | 실제 환경·동일 Release·조건/원본 결과, 부분 Source 시험과 구분 |
| IF-06 | Rolling Update·Pod 삭제·강제 종료 | T10 | 실제 환경·동일 Release·조건/원본 결과, 부분 Source 시험과 구분 |
| IF-07 | WSS 유휴·긴 게임 대기·Client 단절 | T09 | 실제 환경·동일 Release·조건/원본 결과, 부분 Source 시험과 구분 |
| IF-08 | ROSA Clean Recreate / 로컬 복구 | T18·T19 | 실제 환경·동일 Release·조건/원본 결과, 부분 Source 시험과 구분 |
| IF-09 | 미인증·잘못된 Origin·타인의 Room/Game 요청 | T07 | 실제 환경·동일 Release·조건/원본 결과, 부분 Source 시험과 구분 |
| IF-10 | Session 만료·로그아웃·강퇴·권한 변경 | T07 | 실제 환경·동일 Release·조건/원본 결과, 부분 Source 시험과 구분 |
| IF-11 | 단절 중 이벤트 발생·Snapshot 중 Turn 변경 | T09 | 실제 환경·동일 Release·조건/원본 결과, 부분 Source 시험과 구분 |
| IF-12 | 새 연결 뒤 이전 연결의 Message/Disconnect/Leave 도착 | T09 | 실제 환경·동일 Release·조건/원본 결과, 부분 Source 시험과 구분 |
| IF-13 | 동일 ID 재전송·다른 내용·다중 Pod 동시 Turn/결과 확정 | T08 | 실제 환경·동일 Release·조건/원본 결과, 부분 Source 시험과 구분 |
| IF-14 | DB Commit 후 응답 유실·Commit 불명확 | T08·T12 | 실제 환경·동일 Release·조건/원본 결과, 부분 Source 시험과 구분 |
| IF-15 | DB 확정 뒤 Redis 실패·통지 실패 | T08·T12·T13 | 실제 환경·동일 Release·조건/원본 결과, 부분 Source 시험과 구분 |
| IF-16 | Redis Failover·부분 Key 손실·전체 재생성 | T13·T18 | 실제 환경·동일 Release·조건/원본 결과, 부분 Source 시험과 구분 |
| IF-17 | Redis 메모리 압박·쓰기 중간 실패 | T13 | 실제 환경·동일 Release·조건/원본 결과, 부분 Source 시험과 구분 |
| IF-18 | 로컬 DB 복원·새 Redis·사전 보존 Image/Secret | T18 | 실제 환경·동일 Release·조건/원본 결과, 부분 Source 시험과 구분 |
| IM-01 | Local Bootstrap→Remote 이전 | T02 | 실제 Caller/대상 Root·입력 개정·전후 상태/실패 정리 |
| IM-02 | 세 Root별 Caller·State/Lock 접근 | T02·T03 | 실제 Caller/대상 Root·입력 개정·전후 상태/실패 정리 |
| IM-03 | 정상 생성·비용절감 rosa 삭제 | T19·T20 | 실제 Caller/대상 Root·입력 개정·전후 상태/실패 정리 |
| IM-04 | 제한된 입력 추출·오래된 입력/다른 Account 전달 | T02 | 실제 Caller/대상 Root·입력 개정·전후 상태/실패 정리 |
| IM-05 | GitOps 최초 설치·Bootstrap 재실행 | T19의 Bootstrap 및 최초 통합 단계 | 실제 Caller/대상 Root·입력 개정·전후 상태/실패 정리 |
| IM-06 | Secret 공급 전 App Sync·공급/교체·삭제 보호 | T03·T19 | 실제 Caller/대상 Root·입력 개정·전후 상태/실패 정리 |
| IM-07 | ROSA Clean Recreate | T19 | 실제 Caller/대상 Root·입력 개정·전후 상태/실패 정리 |
| IM-08 | Offline 로컬 복구 | T18 | 실제 Caller/대상 Root·입력 개정·전후 상태/실패 정리 |
| IM-09 | Saved Plan·State·Ansible/CI 출력 검사 | T03 | 실제 Caller/대상 Root·입력 개정·전후 상태/실패 정리 |

## 발견한 준비 누락과 이번 보완

구현 쪽도 선언/시험 내용을 대조했다. App의 `first-success.spec.ts`에는 투표·결과/Rating·새로고침 재접속·Guest 동작이 있고, `test_room_connection_lifecycle.py`에는 불명확한 연결 뒤 새 Generation 수렴과 이전 Disconnect 차단이 있다. Redis coordination 시험의 mock/합성 범위를 실제 다중 Pod 결과로 승격하지 않는다. Cloud 기본 렌더는 replicas0 보류, `activation-target`은 FE/BE3개와 zone `ScheduleAnyway`/preferred anti-affinity의 **정적 후보**다. 이것은 실제 AZ 분산 보장이 아니므로 T11은 현장 배치·장애/재배치를 따로 확인한다. ROSA Source는 공통4 Role과 Operator Policy Map을 입력으로 받고 실제6 Operator 대조 postcondition·B 목적 Caller·S3 lockfile과 별도 SG Binding을 선언한다. 선언·mock 성공과 실제 권한/State/전체 Plan은 구분한다. Ansible 상위 README의 Gateway/Bootstrap 초안만으로 실제 Gateway 복구 자동화가 구현·검증됐다고 취급하지 않는다.

| 발견 사항 | 이번에 미리 처리한 부분 | 실제 입력/실행 뒤 남는 부분 |
|---|---|---|
| 파일 25개가 있다는 것만으로 승인 세부 조건의 준비 완료를 주장할 수 없음 | 12축과 T23개·IF18개·IM9개·NET10개를 승인 원문에서 추출해 대응 | 각 Case의 실제 허용·거부/실패 결과와 조건별 Coverage |
| FE/BE 소계만으로는 자원 확보 후보의 반대편 Worker 영향을 계산할 수 없음 | [노드별 메모리 비교](OCP_CAPACITY_ALTERNATIVES_20261011.md)·검사기/음수·미확인 경계 시험 | CPU/슬롯/배치·실사용/Peak·변경 과정 surge/종료 Pod·사용창 |
| Backend HTTP Histogram을 Client 업무 WS 지연으로 대신하면 T16이 빠짐 | 아래 Client 기준·초회 시도 분모·실패/불명 결과 포함 방식 고정 | D의 부하 도구/원본 측정과 B의 대표 업무·결과 일치 확인. 실제 계측 구현 완료로 기록하지 않음 |
| 정상 연결/인증 Source 시험이 실제 회수·금지 통신·부분 장애 증거를 대신할 위험 | 세부 IF/IM/NET 대응과 아래 증거 입력 확인표 | 실제 권한 주체/경로·장애 주입/복귀·오류/예외 수신 |
| 기존 Pull 성공이 새 Worker·12시간 이후·재생성 Pull까지 입증하지 않음 | 아래 세 시점·캐시 확인·소비 자격의 별도 기록 | D/A 환경 공급 뒤 각각 실제 Pull. 승인 Image/캐시 상태/시간 기록 |

## 값이 없어도 준비할 수 있는 측정·증거 절차

기존 [다섯 파일](../evidence/README.md)과 [빈 양식](../evidence/_template/summary.md)을 사용한다. 신규 실행 결과/Run/시간/대상은 미리 만들지 않는다. 미측정은 빈 값 또는 null로 유지한다.

1. **T06~09·T16 대표 업무:** 실제 App가 제공하는 로그인·Room 입장/관전·다중 투표·게임 종료/결과 중 선택한 동작을 먼저 적는다. 동일 Release/Digest·Client 위치·Room별 인원/행동·HTTP/WS 비율·Pod/Process/Pool 구성을 조건에 기록한다. Smoke10명/5분→Baseline30명/15분→Target60명/30분은 Warm-up 제외 기준이며 실제 조합/지속시간은 원본에서 확인한다.

   한 Room에 모든 사용자가 들어간다고 가정하지 않는다. 실제 인원 제한에 맞춰 방을 나누고 참여자/관전자·Think Time·메시지 크기·HTTP 요청 수·서버/Client 연결 수를 기록한다. 부하 도구/스크립트 버전·난수 Seed·시작/종료·Load Generator CPU/네트워크 병목도 조건에 포함한다. Socket 개설만 반복한 결과는 업무 부하 결과로 쓰지 않는다.
2. **지연/정확성:** HTTP는 Client 요청부터 결과 확인까지, 업무 WS는 해당 행동을 보낸 Client의 단조 시계 시작부터 연결된 업무 결과 확인까지 측정한다. Message/업무 ID 연결은 보호 원본으로 남긴다. 서버 HTTP Histogram·WS Ping·브로커 발행 시간은 보조 지표이며 Client 업무 WS p95≤1초의 대체값이 아니다. 업무/Route별 성공 요청 지연과 초회 실패율을 별도로 집계한다. p95 집계 대상/방법·표본 수를 기록하고 timeout/응답 유실/불명 결과는 실패·불명 결과로 남긴다. 초회 업무 시도 분모와 예상 거부/예상하지 않은 오류 구분을 남겨 오류<1% 및 중복 효과·금지 성공·DB 확정 불일치0건을 각각 대조한다. 수치가 없는 부분을 PASS로 채우지 않는다.
3. **T09~15 장애/재접속:** 주입 시작·관측/첫 알림·담당 확인·의존성 복구·Client 상태 수렴·업무/Data 확인을 timeline에 따로 적는다. 의존성 사용 가능 뒤 수렴≤30초와 전체 장애 시간을 혼동하지 않는다. 시계 출처/동기화/오차·Metric/Log/Alert ID·확정/불명 결과·재시도/중복 여부를 함께 보존한다. 정상 종료·강제 종료·DB/Redis·Gateway 장애는 각 Case로 분리한다.
4. **T03·IM-02/06/09·NET:** 보호된 실제 Principal/대상/입력 참조를 확정한 뒤 정상 요청과 무관 범위·옛 인증의 거부를 한 쌍으로 기록한다. 신규 Login과 기존 Session/Token 회수는 따로 시험한다. 자동 Prune·수동 삭제·finalizer/연쇄 삭제·Namespace 삭제를 별도 결과로 연결한다. 개인 Admin까지 격리된다는 주장을 하지 않는다.
5. **T21 실제 Pull:** 첫 새 Worker·12시간 이상 사용 후 새 Pull·재생성 후 새 Worker를 구분한다. 각 시점의 Worker/Digest·사전 이미지 캐시 확인·사용된 Pull 경로/권한·Ready/업무 결과를 보호 원본과 연결한다. imagePullPolicy나 기존 Ready만으로 캐시 없는 Pull을 입증하지 않는다. CI Key를 Worker에 복사하지 않는다.
6. **T17~20 복원/재생성/정리:** 선택한 검증본의 Data 기준 시각·무결성/복호화/import와 Controller 외 사본의 접근/복원 계정을 확인한다. RTO는 사고→지정 Client의 전체 업무/Data 확인, RPO는 선택 사본의 Data 기준과 사고 시각으로 기록한다. DB 명령2초를 전체 RTO로 사용하지 않는다. 재생성 전 Binding 해제와 기반/Backend/Data 보존, 이후 새 Worker SG/Host/Secret·양쪽 전체 Plan을 연결한다. 최종 삭제는 실제 대상/보존 목록을 확정한 뒤 잔존 과금·RDS 재시작·자격 회수를 확인한다.

**준비와 구현의 남은 경계:** 현재 Source 대조에서 Backend는 HTTP Histogram을 제공하지만 Client WS 업무 지연·전체 부하/장애 증거 수집의 실제 실행 구현은 확인되지 않았다. D가 맡은 Harness/관측 작업을 B가 중복 제작하지 않는다. D가 준비한 계측/도구 개정과 출력 예시를 받으면 위 지표를 소비할 수 있는지 B가 검토하고 필요한 부분만 보완한다. 대상/Identity/운영 구조·공유 사용창/장애 범위는 빈 값 교체만으로 끝나는 항목이 아니므로 명령을 미리 확정하지 않는다.

## 다음 처리와 남은 범위

- [ ] App43 리뷰·병합 → Docs100 최종 App Commit 반영 → 새 Image/실제 Pool·Cloud 검증
- [ ] GitOps38 리뷰·병합; GitOps37의 Source 승인과 Draft 해제/교체 조건을 구분
- [ ] OCP 공유 환경 관리 담당/실제 소비자·변경 범위/창 → 안전한 자원 확보 → 재측정 → worker-1 FE/BE Pull → FE/BE 순차 교체/업무·보호 시험
- [ ] A의 실행 입력·B 서비스 권한·지원/기반 인계 → B 목적 인증/Backend·전체 ROSA Plan/수량/삭제/비용 검토 → 검토된 단계별 생성
- [ ] C SG/실제 RDS 연결 상한·예약 → B/C Process·롤링·Pool 예산 → Cloud App 검증
- [ ] C와 이관일/1차 관리·접근 경로 → 1차 서비스의 DB 변경 요청 차단 확인 → 최종 덤프/이관/비교 → Migration current·App 검증
- [ ] Recovery Namespace/Engine/Storage·독립 사본/복원 계정 → 새 Redis·App/Client까지 전체 오프라인 복구
- [ ] 정상 Baseline → 승인 장애/재생성·부하·관측·장시간 Pull → 실비·동일 조건 비교·영상/기여 → 보존/삭제/잔존 비용·회수 → 종료

각 단계의 부분 인계는 먼저 확인한다. 이 대조가 모든 미래 환경/분기/제약을 완전히 검증했다는 의미는 아니다. 실제 개정·운영 입력·시험 결과가 오면 영향받는 조건만 다시 검토한다.
