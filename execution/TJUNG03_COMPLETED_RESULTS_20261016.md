# 정태훈 완결 작업 결과 — 2026-10-16

이 문서는 이미 실행·검토·수락이 끝난 범위만 기록한다. 기준 자료는 기존 원 Issue/PR와 보호 결과물이다. 문서 작성 과정에서 설치·Plan·Sync·시험·해독을 재실행하지 않았다. 전체 작업 체크 정본은 [Docs #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21)이다.

## 확정된 완료 범위

후속 완결 범위: [10/20 새 ROSA·Cloud 앱3/3·정상 Baseline](B_RUNTIME_AND_PROJECT_CLOSEOUT_20261020.md), [10/21 HPA 반환 자료 무결성·요청 분석](HPA_ATTEMPT04_VERIFIED_RESULTS_20261021.md). HPA10/50/100 VU 구간 완료와200 VU 중단을 구분하며 전체 HPA·게임/WSS·Recovery·최종 삭제 완료를 뜻하지 않는다. 후속으로 [B ROSA 삭제 Apply·State0·원격 부재와 owned 잔존0](B_ROSA_DELETE_EXECUTED_20261021.md)을 확인했다. B Snapshot4개는 삭제 후 모두 ABSENT로 확인했으며 [확인 범위 내 B AWS 자원 정리는 완료](B_ROSA_FINAL_CLOSEOUT_20261021.md)다. 다른 담당 범위나 계정 전체 과금0을 완료 처리하지 않는다.


| 완료 범위 | 실제 결과 | 원 근거·작성/실행 범위 |
| --- | --- | --- |
| ROSA 설치·관리 접속 | 10/14 23:30:33 KST Apply 종료0. 이후 노드9/9 Ready, Control Plane3/Infra3/Compute3, Operator34 안정·보호 관리 접속/출력 인계 | [Infra #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25). B Controller 실행. 최초 Plan의 검사17개·내용22항목과 Apply·Ready를 각각 구분한다 |
| Worker 참조·Data 연결 규칙 | Compute3의 Machine 참조와 계정/VPC/클러스터에 대응한 Worker SG 확인. ROSA State의 Data Binding2개(TCP3306/6379) 적용 | [Infra #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25) · [태그 보존 #70](https://github.com/seokpan/seokpan-hybrid-infra/pull/70). A Foundation Owner와 B ROSA Binding Owner를 구분한다 |
| 승인 이미지 실행 검사·임시 참조 분리 | FE/BE × Compute3의 실행6/6·임시 객체 정리, Runtime SA와 Replica0 후보의 임시 Pull 참조 분리 | [Infra #79](https://github.com/seokpan/seokpan-hybrid-infra/pull/79). 앱 서버 기동 없이 확인한 범위이며 새 Worker·12시간 경과 Pull을 뜻하지 않는다 |
| Cloud 보호 입력·TLS/AUTH 검사 | Secret2·CA ConfigMap2 공급/내용 대응. RDS/Valkey TLS1.3·호스트 확인, Valkey AUTH/PING. 잘못된 CA/호스트 및 Valkey 인증 거부5/5 | [Infra #71](https://github.com/seokpan/seokpan-hybrid-infra/pull/71) · [Infra #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25). TLS·인증 거부 검사 범위이며 서비스 계정 SQL·업무 검증을 대신하지 않는다 |
| GitOps/Cloud 플랫폼 등록 | GitOps Operator1.21.4·CSV Succeeded/Argo Available. Cloud AppProject, Namespace Role/Binding·Ingress 정책4개 적용, 기본 Controller 권한45개와 routes/custom-host create 수락 | [Infra #72](https://github.com/seokpan/seokpan-hybrid-infra/pull/72) · [GitOps #52](https://github.com/seokpan/seokpan-hybrid-gitops/pull/52)·[#53](https://github.com/seokpan/seokpan-hybrid-gitops/pull/53). 플랫폼 구성 완료 범위이며 실제 통신·전체 최소권한 완료 판정은 아니다 |
| 정상 관리·모니터링 인계 수락 | B 정상 GitHub/OpenShift·Argo 정책7개, 모니터링 등록·Controller 권한18개 수락. D 보고의 고정16fd14cd 수동 Sync/Synced/Healthy·3객체·smoke firing/삭제·Argo 거부6개를 B 인계에서 수락 | [Infra #75](https://github.com/seokpan/seokpan-hybrid-infra/pull/75)·[#81](https://github.com/seokpan/seokpan-hybrid-infra/pull/81). D 실행을 B 직접 실행으로 기록하지 않는다. 앱 target/운영 알림의 성공 주장은 포함하지 않는다 |
| 기존 Data 작업 Pod의 제한 접속 갱신 | 같은 Pod UID를 유지한 bound 토큰 갱신·지정 범위 허용/거부·무해한 exec 확인 PASS. Workload/RBAC 변경0·Pull 변경0·SQL0 | [Infra #73](https://github.com/seokpan/seokpan-hybrid-infra/pull/73)의 제한 접속과 기존 검증 함수를 재사용한 10/16 결과. Controller 권한 축소나 최종 자격 회수 완료를 뜻하지 않는다 |
| 데스크톱 UI 수락 | 1299×864·1440×900 실제27/27 PASS·오류0, 48.418초. 원 결과 JSON과 PNG12장 시각 수락 완료·추가 수정/재시험 항목0 | [App #21](https://github.com/seokpan/seokpan-hybrid-app/issues/21). 10/15 B03 실제 실행. 기존1280×900 경기/Rating·재접속·방장 승계 결과는 재사용 |
| Cloud 보류 Application·Recovery Namespace 준비 | 고정5294e77의 Application 실제 등록·객체 목록8/8·source 정규화 차이0/오류 조건0. Recovery Namespace 생성·Active·UID 대응·기존 관리 Context 공급 권한8개 확인 | [GitOps #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10) · [Cloud 등록 #52](https://github.com/seokpan/seokpan-hybrid-gitops/pull/52). Replica0·수동 보류를 유지한 등록/준비 완료 범위. 서버 manifest 전체 독립 대조·실제 Sync·Engine 기동을 포함하지 않는다 |
| Recovery 보호 입력 최초 공급 | cp-01의 지정 Recovery Namespace에 Secret3·ConfigMap2를 create5로 최초 생성. 생성 응답의 객체 UID·내용 대조 PASS, Namespace/RBAC 변경0·SQL0 | [GitOps #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10) · [Docs #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21). 기존 보호 공급 receipt의 완료 수락. Engine·Runtime TLS/AUTH·실제 복원·오프라인 망 독립/RTO/RPO는 포함하지 않는다 |
| 비용 입력용 실물 규격 조회·전달 | 인스턴스9개, 부착 EBS13개/3070GiB(루트2850+추가220), NLB3개(외부2/내부1), CLB0. B 규격 입력 전달 완료 | [비용 입력 Docs #43](https://github.com/seokpan/seokpan-hybrid-docs/issues/43#issuecomment-6145410624). 10/15 09:27:37 KST 조회 범위이며 단가·총비용·청구 확정이 아니다 |

## UI 검증의 완결 근거

B03은 10/15 10:17:08~10:17:56 KST의 기존 실제 실행이다. 두 해상도의 대기/진행 보드 경계·스크롤/휠 안정, 상세 패널의 마우스/키보드 조작과 고정 요약, 실제8인 목록의 단일 스크롤, 채팅 입력 고정, 로그인/회원가입의 클라이언트·서버 오류 전후 카드 크기와 세션/방 WebSocket을 수락했다. 시험방 종료·임시 CA 제거도 완료했다. 48.418초는 기능 검사 소요 시간이며 성능 지연이나 RTO가 아니다.

원 묶음은 result.json과 PNG12장이다. 수락한 아카이브는 836828바이트, SHA-256 `4ed555679ced2757f76c6d9c4c06be1fdf38de79056c2471cc3dddd502391154`다. 원 결과와 이미지의 결속/개별 해시는 보호 증거 대장에 보존한다. 가림 표시 뒤의 입력 텍스트·픽셀을 확인했다고 주장하지 않는다. 이번 기록 등록에서 새 브라우저 실행이나 화면 재시험은 하지 않았다.

## 원 이슈 완료 기준의 근거 대응

### App #21 UI 기준

원 기준의 순서·의미를 유지한다. B03의27개 검사만으로8개 기준을 모두 충족했다고 판정하지 않고, 원 Source·기존 실제 기능·추가 화면 수락을 합쳐 대조한다.

| 원 기준 | 충족 근거와 수락 범위 |
| --- | --- |
| 1. 실제 서비스의 UI 반영·기존 계약 유지 | [App #22](https://github.com/seokpan/seokpan-hybrid-app/pull/22)의 Backend/API/게임 모델·배포 선언 불변, [#34](https://github.com/seokpan/seokpan-hybrid-app/pull/34)의 UI 흐름 회귀, [기존 실제 Run7](https://github.com/seokpan/seokpan-hybrid-app/issues/4#issuecomment-6145407122)의 Image/서비스 기능을 연결한다. B03은 같은 서비스의 세션·HTTP/방 WS를 확인했고 Backend/배포 변경0이다 |
| 2. 두 해상도의 보드·페이지 스크롤 | B03의 각 해상도 waiting/active board/page fits 및 기존 휠/위치 측정·PNG 수락 |
| 3. 요약 위치·마우스/키보드·긴 목록 단일 스크롤 | 각 해상도 panel keyboard/summary·roster pointer/keyboard·실제8인 long list one scroll area 및 PNG 수락 |
| 4. 채팅 목록 스크롤·입력 고정 | 각 해상도 waiting/active chat scroll/input fixed 및 PNG 수락 |
| 5. 로그인/회원가입 오류 전후 카드 크기 | 각 해상도 client-error와 자기 시험계정 server-login/duplicate-registration 오류의 실제 크기 측정·PNG 외곽 확인. 가림 뒤 입력 텍스트의 시각 확인과 구분 |
| 6. 결과/Rating·모달·대기방 복귀 | 기존10/13 실제1280×900 기능의 정상5목·9착수·Rating 방향·모달 닫기/재열기·대기방 복귀 PASS. B03에서 반복하지 않음 |
| 7. 고정 도구 Source 검사 연결 | [App #22 고정 개정의 Source Run](https://github.com/seokpan/seokpan-hybrid-docs/blob/312db8c099ba5c9f67362f12b9df27be8653e7a3/evidence/T09/source-audit-20261007-01/summary.md)과 App #34의 Node24.19.0/npm12.0.2·도구81/unit278/build·모의 UI36/Full2 결과. 실제 서비스 결과와 구분 |
| 8. 코드 검사·리뷰·병합 | App #22의 검증 개정 `abb648350084c9ebe6c63ee7668921de66f5b03f`·문구 보완 HEAD `663b52278afd020dceb46d8dab1a2ebdfe6e7557`의 [승인 리뷰](https://github.com/seokpan/seokpan-hybrid-app/pull/22#pullrequestreview-5449755134)·병합 확인, 후속 App #34 연결 |

### Infra #80 최초 모니터링 등록 기준

| 원 수락 조건 | 충족 근거와 수락 범위 |
| --- | --- |
| 원본 확인값·범위/소유·서버 dry-run | [Infra #81](https://github.com/seokpan/seokpan-hybrid-infra/pull/81)의 고정 GitOps `16fd14cd1c085a8314a5e2e18b89e2cd3b051626` 등록과 기존 실제 등록 수락. 지정 AppProject/Application·Namespace 객체의 소유/선언 차이를 덮어쓰지 않음 |
| Controller18권한·Argo 정책 반영 | 기존 Namespace LocalSubjectAccessReview18개와 정상 운영자 get/sync 수락. 계정 대행 없음. D의 Sync·한정 smoke/거부6개 보고 수락은 B 직접 실행과 구분 |
| 실패·부분 생성 기록 | #81의 보호 receipt·자동 삭제/롤백 금지·읽기 중단 후 조회만 재개 경계 구현과 오프라인 거부 사례로 확인. 실제 장애 주입·일반 부분 실패 복구 성공으로 확대하지 않음 |
| 오프라인 검사 | #81 최종 HEAD `4a0e017a80e23239c3a73eeebc5cb4b13c63cc24`의22개 PASS·[CI 성공](https://github.com/seokpan/seokpan-hybrid-infra/actions/runs/38859439817), 병합 main `1114b8108900225578aaa6c4b4f36df8fd0e4652` 연결 |

최초 등록 기준4개는 충족했다. 앱 target UP·운영 규칙 평가·알림 수신은 이 원 이슈의 종료 기준에 포함되지 않는다. 두 원 이슈의 종료로 상위 App #4·GitOps #10·Infra #25 또는 Docs #21의 미충족 복합 체크를 완료 처리하지 않는다.

## 완료된 정합 보완

- **Recovery 최초 공급:** 고정 `5294e77af873ec5318bbb7f1a1097d68208d03fa`에 대응한 암호화 Bundle 전달·확인, 별도 보호 키 권한600, SOPS3.13.3 해독1회와 Secret3/ConfigMap2 최초 생성·내용/UID 대조를 수락했다. 보호 receipt는 `RECOVERY_PROTECTED_SUPPLY_20261016` 논리 참조로 보관한다. `apply` 명령 미사용은 `create`5개 성공과 다른 필드이며 공급 미실행을 뜻하지 않는다. 별도 verify 모드나 해독/생성을 반복하지 않았다. Harbor/DB의 추가 보호 입력과 Engine·복원/업무의 전체 수락으로 확대하지 않는다.

- **ROSA 태그 보존:** 초기 Foundation 계획의 클러스터 태그 제거8개를 Apply하지 않고 중단했다. 기본 Provider는 Data 설치 제외 태그를 관리하고, ROSA 공유 자원만 클러스터 태그 접두사를 별도로 처리하도록 수정했다. A 전체 계획 종료0·자원/출력 변경0·태그 변경0과 B의78 no-op/검사14 PASS를 연결했다. 재설치는 하지 않았다. [Infra #70](https://github.com/seokpan/seokpan-hybrid-infra/pull/70)·[#78](https://github.com/seokpan/seokpan-hybrid-infra/pull/78).
- **지정 Route host 권한:** Cloud Namespace Role의 `routes/custom-host / create` 규칙1개 보완과 실제 허용 확인을 완료했다. 기존45개 검사/Ingress 적용을 반복하거나 전체 Controller 권한 축소 완료로 기록하지 않았다. [GitOps #53](https://github.com/seokpan/seokpan-hybrid-gitops/pull/53).
- **보류 Application source 비교:** 관측된 차이는 빈 `target.group` 3개의 상태 직렬화 생략뿐이었다. 그 차이만 정규화한 비교에서 잔여 차이0·오류 조건0을 확인했다. Application을 수정하거나 Sync해서 비교를 통과시킨 결과가 아니다. 고정 개정은 `5294e77af873ec5318bbb7f1a1097d68208d03fa`다.

## Recovery Valkey·CI 개정 정합 — 2026-10-16

Recovery 보호 입력 Secret3·ConfigMap2와 별도 Harbor Secret의 최초 공급·내용/UID 대조를 완료했다. [GitOps #57](https://github.com/seokpan/seokpan-hybrid-gitops/pull/57)의 병합 Source `c75a4b5e3b3b9bae4ea7d8a431962cb9ca7308d7`에서 Valkey만 수동 1개로 기동해 Ready·재시작0·UID999·파일 접근·TLS/AUTH PASS를 확인했다. Source의 전체 Replica0과 실제 Valkey1을 구분한다. TLS/AUTH는 API port-forward 경로이며 CNI 허용/거부·새 Registry 연결/노드 CA 인과·FE/BE·DB 복원·전체 업무/RTO/RPO는 미검증이다. Cloud 앱·SQL·Migration 실행은 포함하지 않는다.

[Valkey 실행 증거](../evidence/B06-VALKEY-01/b06-valkey-20261016-01/summary.md).

후속 [D의 B06-NP-01 결과](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10#issuecomment-6213554272)에서 같은 노드·다른 노드의 backend 라벨 Pod→Valkey TCP6379 허용6/6, 비허용 주체 차단6/6 및 임시 객체 정리를 확인했다. 비허용 주체의 제한 egress 정책과 허용 대조군으로 ingress 차단을 구분했으며 패킷 카운터/플로우 로그 증거는 아니다. worker-01의 Valkey 새 Pull 이벤트도 관측됐다. Backend/Frontend Pull·DB3306·DNS53·FE→BE8000·다른 비허용 주체·전체 복구는 별도다.

CI/Promotion 개정 정합은 [App #47](https://github.com/seokpan/seokpan-hybrid-app/issues/47#issuecomment-6158883408)·[GitOps #45](https://github.com/seokpan/seokpan-hybrid-gitops/issues/45#issuecomment-6160603523)의 완료 근거와 병합 Source를 연결해 확인했다. 이미지 App Source `c2dad254cc407431092691f9ea5892f8324f1520`과 이후 출처 도구 `d037a55f234a8720e6db9b01b8f31d08a3a16af9`을 구분한다. [Writer PAT 발급·등록·기존 실행/거부 결과](https://github.com/seokpan/seokpan-hybrid-app/issues/14#issuecomment-6139234475)는 완료로 유지하며 Lifecycle·추가 권한 Case·비상/독립 보관·최종 회수는 별도다.

| 역할 | 채택 개정 |
| --- | --- |
| FE/BE 이미지 App Source | `c2dad254cc407431092691f9ea5892f8324f1520` |
| 출처 기록 도구 | `d037a55f234a8720e6db9b01b8f31d08a3a16af9` |
| Cloud 보류 GitOps Source | `5294e77af873ec5318bbb7f1a1097d68208d03fa` |
| Recovery Valkey GitOps Source | `c75a4b5e3b3b9bae4ea7d8a431962cb9ca7308d7` |

TH-03.3의 개정 정합은 완료다. TH-03.4의 잔여와 Cloud/Recovery의 전체 Runtime 수락을 이 결과로 완료 처리하지 않는다.

## 기록의 경계

> **이 절과 아래 조사 기준은 2026-10-16 당시 기록이다.** 아래의 ROSA/NAT 유지·삭제 미실행과 당시 main SHA는 현재 상태가 아니다. 10/21 최종 B AWS 자원 종료는 [후속 종료 기록](B_ROSA_FINAL_CLOSEOUT_20261021.md)을 따른다. 원 기준 중 미수락 시험은 성공으로 바꾸지 않는다.

원 조건 전체가 충족되지 않은 TH는 체크하지 않는다. ROSA 실행은 완료됐지만 TH-12.2의 실제 사용 개정 리뷰 기록·TH-12.4의 비용 조건 등 복합 기준은 별도다. Cloud 업무/운영 Pool·다중 Pod/장애·독립 Recovery/RTO/RPO·비상/자격 회수·중간 재생성·최종 보존/비용/발표는 이 완료 기록으로 닫지 않는다. 그 진행 상세는 신규 완료 문서화 대상에서 제외하고 원 Issue의 미완료 체크로 유지한다.

운영 일정은 **검증 완료까지 기존 ROSA/NAT 유지**로 정정됐다. 과거10/16 금요일/주말 전 삭제 목표는 현재 삭제 지시가 아니다. 삭제 실행·예약은 없으며 기존 $450 계획/$500 한도와 실제 청구/잔여 예산 확인을 유지한다.

## 조사 기준

네 저장소는 아래 각 main을 개별 조회했다. 동시점 원자적 Snapshot이나 현재 live 재조회를 뜻하지 않는다.

| 저장소 | 조회한 main |
| --- | --- |
| app | `d037a55f234a8720e6db9b01b8f31d08a3a16af9` |
| infra | `f23b29b63a509f2e182016fc7af13386fde7f766` |
| gitops | `16fd14cd1c085a8314a5e2e18b89e2cd3b051626` |
| docs | `c46ad369e33059864719d3ff55217f73c6e98a15` |

조사 시작점의 GitHub 이슈100개·댓글408개, B 작성 PR118개의 설명과 B가 작성/참여한 PR156개의 Conversation/리뷰299건을 대조했다. 네 main의 추적 파일926개 중 UTF-8 파일911개와 이번 문서 변경본을 검색했다. 작성/배정 이슈13개·B 댓글120개 및 다른 담당 이슈의 B 기록을 대조했다. 기존 실행 진입/학습 안내와 과거 조사 문서는 현재 완료 근거로 연결했고, 당시 체크·절차·Source/측정값은 보존했다. 원 저장소 문서의 보완은 [Infra #83](https://github.com/seokpan/seokpan-hybrid-infra/pull/83)·[GitOps #58](https://github.com/seokpan/seokpan-hybrid-gitops/pull/58)에 별도로 게시해 대조한다. Infra의 새 VPN Source와 GitOps의 미병합 Recovery 후보를 B 실행/복구 완료로 올리지 않았다. 과거 Run·수치·실제 수행자·다른 담당의 체크는 보존했다. 문서 변경의 검사 결과와 게시 여부는 해당 PR에서 확인한다.
