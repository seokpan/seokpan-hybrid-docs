# 2차 프로젝트 다이어그램 제작 계획

> **상태:** DESIGN FIGURES CREATED — 설계 그림 제작·자체 검증 완료. 최종 그림 승인 대기
> **작성일:** 2026-10-02 KST  
> **근거:** 프로젝트 소스 00~04 및 최신 프로젝트 지침  
> **제작 범위:** 설계 기준 12장, SVG 12개와 PNG 12개. 실제 구축 결과판은 미작성

현재 진행 현황:

- [x] 03 상세설계·04 구현 준비의 문서 종료 확인
- [x] 05 구현·통합·검증과 설계 다이어그램의 선후 관계 확인
- [x] 기존 1차 문서 PNG와 개인 OpenShift SVG의 형식 확인
- [x] 장수·목적·포함 내용·근거·보류 입력 정리
- [x] 제작 계획 후속 진행 요청 확인
- [x] 전체 논리·물리 아키텍처 시안 제작·자체 시각 검증
- [x] 나머지 설계 그림 제작·교차 검증
- [ ] 사용자 그림 검토 의견 반영
- [ ] 실제 구현·검증 기록에 따른 결과 그림 작성

## 1. 지금 시작할 수 있는 범위

03은 승인된 상세설계이며 04는 후속 운영 결정과 실행 인계를 정리하고 문서 전체를 종료했습니다. **05 전체 완료를 기다리지 않고 설계 기준 다이어그램의 계획·검토·제작을 진행할 수 있습니다.** 근거는 03의 승인 상태 및 04 §1·§10.5·§11.3입니다.

05는 `05_IMPLEMENTATION_AND_VALIDATION.md`로, 실제 입력·Source·코드·통합·시험 결과를 기록합니다. 이번 첨부에는 05 본문이 없어 실제 최신 구축 상황을 확인하지 않았습니다.

이 문서의 **그림 01~12**와 **프로젝트 문서 00~05**는 별도 번호입니다. 예를 들어 그림 05는 상태 책임·재접속 그림이며 문서 05의 구현 진행 단계와 동일한 항목이 아닙니다. 이후 `그림`과 `문서`를 함께 표기해 구분합니다.

| 산출물 | 제작 시점/현재 상태 | 표시 기준 |
| --- | --- | --- |
| 전체 논리 구조·통신·배포·복구 등 설계 그림 | 제작 계획에 따른 제작 완료 | 승인된 설계 목표, 구현/시험 미확인 |
| 전체 물리 아키텍처의 목표 배치도 | 제작 계획에 따른 제작 완료 | 승인 CIDR/AZ 역할/자원 역할, 규모 후보와 실제 입력 대기 구분 |
| 실제 구축 전체 논리·물리 아키텍처 | 관련 구현 기록·Source·Runtime 증거 확보 후 | 확인 시점·배치·실제 값·검증 범위를 기록 |
| 장애시험·복구 시간선·성능 결과 | 해당 Run의 검증 가능한 증거 확보 후 | 측정값·실패/제한·실행 조합을 근거로 작성 |

전체 물리 아키텍처는 클라우드 자원과 온프레미스 장비/VM의 배치를 설명합니다. AWS 관리형 서비스의 내부 물리 서버를 추정해 그리지 않습니다. 설계 단계에서는 미확인 Host·VM 주소·용량·실제 AZ ID를 임의로 채우지 않습니다.

## 2. 설계 다이어그램 12장

12장은 미리 정한 목표 숫자가 아니라 다음 설명 목적을 분리한 결과입니다. 전체 구조 2장, 연결/런타임 3장, 운영/자동화 4장, 복구/장애/이전 3장입니다. 페이지 수를 맞추기 위해 구조를 중복하거나 시험 성공 그림을 추가하지 않습니다.

**장수의 범위:** 이번에 제작한 수는 설계판 12장입니다. 후속 전체 논리·물리의 구축 결과판 2장을 작성하면 12개 주제의 최소 14개 판본이 됩니다. SVG/PNG는 같은 그림의 파일 형식이며 장수에 중복 합산하지 않습니다. 추가 결과 그림은 증거와 설명 목적에 따라 정합니다. 12장은 최종 확정 수나 최대 장수가 아니며 시안의 가독성 때문에 분할/통합이 필요하면 이유와 변경 장수를 기록합니다.

| ID | 제목 | 이 그림이 답할 질문 | 주요 포함 내용 | 형식 |
| --- | --- | --- | --- | --- |
| 01 | 전체 논리 아키텍처 | 무엇이 어떤 책임을 맡고 AWS/On-Prem에 남는가? | Cloud Primary, ROSA FE/BE·GitOps·Monitoring, RDS/Redis, ECR/S3, On-Prem Jenkins/Harbor/Data/Recovery | 영역별 구조도 |
| 02 | 전체 물리 아키텍처 | 자원은 어느 환경·AZ·Subnet·장비 계층에 배치되는가? | 서울 VPC·3 AZ·9 Subnet, ROSA Node 역할, NAT/IGW/VPN, Data 배치, On-Prem VM/Cluster/Storage 역할 | 목표 배치도 |
| 03 | Hybrid 네트워크와 경로 | 어디서 연결하며 어떤 통신이 VPN·인터넷을 사용하는가? | 전용 Gateway, Outbound WireGuard·EIP, RDS 왕복 경로, Route/AllowedIPs/SG, Public API·HTTPS/S3/ECR와의 구분 | 네트워크 경로도 |
| 04 | 사용자 트래픽과 TLS | HTTPS/WSS가 어디서 종료되고 FE/BE/Data로 어떻게 도달하는가? | Public Ingress LB, Router/Route Path 분기, ClusterIP Service, FE/BE, Edge TLS·내부 HTTP·Data TLS | 서비스 흐름도 |
| 05 | 상태 책임과 재접속·업무 확정 | Redis 연결 복구와 게임/DB 상태 복구는 어떻게 다른가? | Session/Room/Vote Runtime, DB 영속 기록, 재인증·상태 조회·연결 식별, 중복/부분 실패·재개 Gate | 상태/업무 흐름도 |
| 06 | CI/CD와 Release 전달 | 코드가 어떤 검증·승인 경로로 Cloud와 Recovery에 전달되는가? | Jenkins Test/Build/Scan, ECR/Harbor, GitOps PR·사람 Merge·Argo Sync, Digest/Release/Evidence | 전달 흐름도 |
| 07 | Terraform·Ansible·GitOps 소유권과 수명 | 누가 무엇을 만들고, 어떤 자원이 재생성/보존되는가? | bootstrap/foundation/rosa, 제한 Output 인계, GitOps 최초 설치 예외, Secret 별도 공급, Cloud/Offline Apply, Window 정리 | 책임/수명 구조도 |
| 08 | 관리 인증과 Secret 공급 | 사람·자동화·앱의 인증과 복구 재료를 어떻게 분리하는가? | 개인 IAM/MFA·TF Role, ROSA GitHub Team IDP/RBAC·비상 관리, CI/Backup, SOPS+age·범위별 Bundle·별도 Key | 인증/공급 경계도 |
| 09 | 관측과 Evidence | 장애를 무엇으로 판단하고 삭제 전 어떤 증거를 보존하는가? | Native/UWM, App Log·WS/DB/Redis/Backup 신호, AWS Metrics, 알림/담당 판단, Run/Index·보호 원본 | 관측/증거 흐름도 |
| 10 | 백업과 On-Prem 오프라인 복구 | AWS 접속 없이 어떤 준비물로 어디까지 복구하는가? | Data VM의 RDS 논리 Backup, S3·로컬 사전 동기화·무결성, Harbor/Bundle/Key, 전용 MariaDB·새 Redis·앱·사용자 안내 | 정상/복구 2구간 흐름도 |
| 11 | HA와 장애 영향 범위 | Pod/Worker/AZ/Data/VPN/On-Prem 장애의 영향과 복구 책임은 무엇인가? | Multi-AZ, RDS Primary/Standby, Redis Primary/Replica, Client 재접속, 단일 Gateway, 배포/백업/서비스 영향, 지원 시험 경계 | 장애 영역도 |
| 12 | 1차에서 2차로의 책임 이전 | 무엇을 유지·이전·대체하고, 1차를 어떻게 보존하는가? | kubeadm→ROSA, DB/MaxScale→RDS, Redis→새 Cloud Runtime, Jenkins 유지, ECR/Harbor 분담, Seed/격리 이관·전환 판단 | As-Is/To-Be 비교도 |

전체 논리 구조에는 개별 IP·모든 통신선을 넣지 않고 역할과 경계를 보여줍니다. 물리 구조에는 모든 CI 처리 단계를 넣지 않습니다. 이후 상세 그림에서 경로·순서·인증·장애를 확대합니다. 비교표가 더 명확한 세부 Grant·포트·버전·담당 명단은 문서 표로 유지합니다.

## 3. 그림별 제작 조건과 근거

아래 문서 번호는 [설계문서 목차](../design/README.md)의 번호입니다. 절 번호는 해당 원문의 근거 위치이며 생성 후 검증 체크리스트로 사용합니다.

### 01 전체 논리 아키텍처

- **목적:** 프로젝트 진입점에서 정상 Cloud Runtime, On-Prem 운영, 사전 준비된 복구 책임을 한 장으로 파악합니다.
- **경계:** AWS Account/ROSA, On-Prem, Source/배포/관측 역할. 정상 사용자 경로는 AWS 내부에서 종료합니다.
- **주의:** On-Prem Recovery를 Active-Active나 항상 실행 중인 이중 서비스로 그리지 않습니다. Cloud DB/Redis는 ROSA Pod 내부에 넣지 않습니다.
- **근거:** 02 §3~4, 03 §3-A.1~5, 04 §1·§5.5.
- **남은 입력:** 전체 설계 시안은 현재 제작 가능. 실제 운영 중/복구 전 준비 상태는 05 증거 확보 후 표시합니다.

### 02 전체 물리 아키텍처

- **목적:** AWS 목표 배치와 On-Prem 역할 배치, 관리형/직접 관리 경계를 보여줍니다.
- **확정 주소 계획:** VPC `192.168.64.0/20`. 아래 AZ-A/B/C는 설계상의 역할 이름이며 실제 AZ 이름/ID로 치환하기 전의 값입니다. ROSA Pod는 `10.128.0.0/14`, Service는 `10.240.0.0/16`의 승인된 주소 계획을 표시합니다.

| Subnet 역할 | AZ-A | AZ-B | AZ-C |
| --- | --- | --- | --- |
| Public | `192.168.64.0/24` | `192.168.65.0/24` | `192.168.66.0/24` |
| ROSA Private | `192.168.67.0/24` | `192.168.68.0/24` | `192.168.69.0/24` |
| Data Private | `192.168.70.0/24` | `192.168.71.0/24` | `192.168.72.0/24` |

- **예비 주소:** `192.168.73.0/24`~`192.168.79.0/24`의 7개 블록. 생성 Subnet 수는 9개이며 예비 블록을 더하지 않습니다.
- **네트워크 자원:** VPC/IGW, AZ별 NAT-A/B/C 3개, S3 Gateway Endpoint, 단일 VPN EC2/EIP와 사설 Data 경로를 표시합니다. Public API/Ingress의 플랫폼 관리 자원과 팀 소유 Network 자원을 구분합니다. ROSA Private는 같은 AZ의 NAT 경로, Data Private는 기본 인터넷 Route 없이 필요한 사설 왕복 경로를 갖는 승인 목표입니다.
- **규모 표현:** ROSA Classic 최소 Control Plane 3 + Infra 3 + Worker 3, Worker `m5.xlarge`·FE/BE 각 3 Replica는 초기 후보. 나머지 Node 사양을 Worker 사양으로 복제하지 않습니다.
- **Data 표현:** RDS Multi-AZ DB instance는 Primary + 동기 Standby, Redis는 Single Shard/cluster mode disabled의 Primary 1 + Replica 1. Data Subnet 3개를 각 서비스 인스턴스 3개로 세지 않습니다. 실제 서비스 배치 AZ는 구현 확인 전 임의 지정하지 않습니다.
- **On-Prem 표현:** 기존 Jenkins/Harbor/Cluster/Recovery Storage와 새 전용 VPN Gateway VM·Data 작업 VM·복구 DB VM을 역할로 구분합니다. 새 VM의 Host·이름·IP·용량·Hypervisor/Storage 장애 영역은 확인 대기입니다.
- **근거:** 03 §3-B.3~6·§3-B.8~9·§3-D.10·§3-F.18, 04 §1·§5.5.
- **남은 입력:** 실제 AZ 이름/ID, ROSA 관리 자원의 설치 결과, 자원 사양·지원 조합, On-Prem Host/VM·Storage 배치. 목표도는 지금 제작하고 실제 배치도에 후속 반영합니다.

### 03 Hybrid 네트워크와 경로

- **목적:** On-Prem Job Host→vRouter→전용 Gateway→WireGuard→AWS Gateway→RDS의 사설 왕복과 정상 Cloud 경로를 구분합니다.
- **확정 전제:** Tunnel `10.200.0.0/30`(AWS `.1`, On-Prem `.2`), AWS VPN EC2 1대+EIP, On-Prem 선제 연결. 최소 Host `/32` 허용과 원본 IP 보존을 적용 목표로 표시합니다.
- **필수 구분:** RDS Data 작업은 VPN, S3/ECR/GitHub/AWS API는 기존 Internet HTTPS. On-Prem에서 S3 Gateway Endpoint를 VPN 경유 사용하는 선은 그리지 않습니다. Public API 관리와 사용자 Ingress를 구분합니다.
- **주의:** Route·AllowedIPs·Host Forward Firewall·SG는 별도입니다. Pod/Service CIDR을 Hybrid에서 직접 광고하지 않습니다. 단일 VPN Gateway는 자동 AZ Failover가 아닙니다.
- **근거:** 03 §3-B.1·5·8~9·§3-D.9.3, 04 §1.
- **남은 입력:** 실제 Job Host/Gateway 주소·vRouter 연결·ENI·Source SG·DNS. 목적별 역할/주소 계획으로 시안을 만들고 실제 값은 별도 확인합니다.

### 04 사용자 트래픽과 TLS

- **목적:** 같은 공개 Host의 FE/HTTP API/WSS 분기와 신뢰 경계를 보여줍니다.
- **구조:** Client→Public Ingress LB→OpenShift Router/Route→FE/BE ClusterIP Service→Pod; BE→사설 RDS/Redis.
- **필수 표시:** HTTPS/WSS는 Router에서 Edge TLS 종료, Router→App은 초기 HTTP, Data 접속은 TLS·서버 이름/CA·목적별 인증. 관리 API 6443은 별도 경로입니다.
- **주의:** 실제 API/WS Path·Service Port를 `/api`·`/ws` 등의 추정값으로 채우지 않습니다. FE를 임의 API Proxy로 그리지 않습니다. 개인 도메인/DNS 변경도 포함하지 않습니다.
- **근거:** 03 §3-B.8.3·§3-E.3~7, 04 §1.
- **남은 입력:** 실제 Host·Path·Port·Route 수·Probe/Timeout·인증 형태. 최초 그림에는 의미별 Path를 사용합니다.

### 05 상태 책임과 재접속·업무 확정

- **목적:** Runtime 공유, 영속 업무 확정, 사용자 통지를 별개 책임으로 설명합니다.
- **포함:** Redis의 Session/Room/Ready/Connection Generation/Game Runtime/Turn/Vote; MariaDB의 Member/Game/Move/Result/Rating; 재인증·현재 상태 조회·오래된 연결 차단·미확인 쓰기 결과 확인.
- **필수 실패 분기:** DB 확정/Redis 갱신/통지 실패를 나누고, 전체 Runtime 소실 시 완료 기록 보존·진행 상태 중단·새 로그인/게임을 구분합니다.
- **주의:** DB+Redis 분산 Transaction, 메시지 영구 재생, 정확히 한 번 처리, 자동 게임 복구를 이미 구현했다고 그리지 않습니다. 복잡하면 한 장 안의 상태 책임/재접속 두 패널로 나눕니다.
- **근거:** 03 §3-D.5·§3-D.10.7·§3-E.10~14.
- **남은 입력:** 실제 Source의 인증/메시지/Schema/멱등·재접속 구현. 설계 계약도와 구현 결과도를 구분합니다.

### 06 CI/CD와 Release 전달

- **목적:** Source, Image, Desired State, 실제 배포·검증의 연결을 설명합니다.
- **포함:** App Source→On-Prem Jenkins Test/Build/Scan→ECR Push·Release 후보 기록→GitOps Promotion PR→사람 Review/Merge→OpenShift GitOps Sync→Cloud Runtime. 검토·승인된 Recovery Image의 Harbor 사전 보존과 ECR/Harbor Mapping·Bundle 준비를 별도 분기로 연결하고 PR 검토에서 복구 준비 상태를 확인합니다. 모든 Build가 곧 승인 Release이거나 Cloud 배포 성공만으로 Recovery 준비 완료라는 흐름은 만들지 않습니다.
- **필수 구분:** CI Push Principal, Node Runtime Pull, GitOps Writer와 Argo Reader; Release ID·Source SHA·FE/BE Digest·Schema/설정/Secret 개정·실제 Run 연결.
- **주의:** Jenkins의 Cloud 직접 Apply/자동 Merge/TF Apply 선을 추가하지 않습니다. ECR/Harbor Digest가 무조건 동일하다고 쓰지 않고 Mapping을 확인합니다. 최초 App 수동 Sync와 이후 자동 Sync·SelfHeal, 자동 Prune 보류를 구분합니다.
- **근거:** 03 §3-A.8·§3-F.16~17, 04 §5.2·§5.4.
- **남은 입력:** 실제 Job/Scan 결과·PAT/Reader·Digest·Promotion PR·Runtime Pull. 선언된 전달 절차를 먼저 그립니다.

### 07 Terraform·Ansible·GitOps 소유권과 수명

- **목적:** 재현 가능한 생성·초기화·배포와 자원 보호를 설명합니다.
- **포함:** bootstrap/foundation/rosa의 세 Root/State, 비밀값 아닌 제한 입력, ROSA Lifecycle, 최소 Ansible GitOps 설치/Root 등록, GitOps 내부 Desired State, Secret 별도 공급.
- **추가 구분:** Offline Recovery의 사전 Render/Ansible Apply는 로컬 격리 Namespace만의 예외. Cloud 앱 배포 Owner와 혼합하지 않습니다. Resource Owner와 사람 실행 책임도 별개입니다.
- **주의:** State Root와 비용 Lifecycle을 동일시하지 않습니다. rosa 삭제가 RDS/Redis/Backup/전체 foundation 삭제를 뜻하지 않습니다. NAT/EIP 정리는 의존 확인 후 수행하고, 최초 Local→Remote 이전을 현 환경에서 반복하는 것으로 그리지 않습니다.
- **근거:** 02 §15~19, 03 §3-A.7·§3-F.3~9·17.3·19, 04 §2·§8.6·§10.2.
- **남은 입력:** 실제 코드/Lock/Role/Plan·현재 State 연결·실행 조합. 소유권/인계도는 현재 제작 가능합니다.

### 08 관리 인증과 Secret 공급

- **목적:** AWS·ROSA·Argo·SQL/Redis·Registry 인증을 같은 권한으로 오해하지 않게 합니다.
- **포함:** 개인 IAM 4개+MFA·목적별 TF Role, ROSA GitHub Team IDP/RBAC·Argo SSO/RBAC, 제한 CI/Backup 주체, 목적별 서비스 인증, SOPS+age 공급 Bundle와 별도 보호 Key/예비본.
- **필수 구분:** 개인 AWS Admin은 사람의 강제 최소권한 격리가 아닙니다. 정상 GitHub 인증, 유지 비상 htpasswd 관리자, 검증 후 회수할 초기 ROSA/Argo 인증을 구분합니다.
- **주의:** 실제 Secret/Private Key/ARN/Account ID/접속 URL은 넣지 않습니다. Backup 파일의 age 해독 Key와 SOPS Identity는 별개이고, 암호문/Key를 같은 저장소 한 곳에 놓는 구조로 그리지 않습니다. Secret 자동 동기화 서버를 추가하지 않습니다.
- **근거:** 03 §3-C·§3-F.6, 04 §5.2~3·§5.6.
- **남은 입력:** 실제 Principal/Policy/Team·공급/회수/복원 결과. 역할 및 원본/사용 사본/예비본 경계로 표현합니다.

### 09 관측과 Evidence

- **목적:** 플랫폼/업무/Data/Backup 장애를 어떤 신호로 판단하는지, 실행 결과를 어떻게 보존하는지 보여줍니다.
- **포함:** OpenShift Native Monitoring·UWM, 기존 App 구조화 Log, RDS/ElastiCache AWS Metric, 연결/게임/Backup 상태, 알림→담당 판단→Run/Evidence Index.
- **보존 경계:** Release/Run JSON, Summary/Index Markdown, Metric/Timeline CSV와 보호된 대용량 원본. ROSA 삭제 전에 필요한 결과를 외부에 보존합니다.
- **주의:** 기존 On-Prem Stack 보존과 Cloud Stack을 구분합니다. 새 Cloud Grafana/Loki/외부 APM·알림 제품을 기본 구성에 추가하지 않습니다. AWS Metric을 UWM이 직접 모두 수집한다고 단정하지 않습니다.
- **근거:** 02 §13, 03 §3-G.8~9, 04 §5.4·§8.5.
- **남은 입력:** 실제 Metric/Exporter/수집 경로·receiver·알림/Log·보존 위치와 Run. 처음에는 승인된 관측 역할을 표시합니다.

### 10 백업과 On-Prem 오프라인 복구

- **목적:** 정상 시 사전 준비와 AWS 접속 불가 시 복구 실행을 분리합니다.
- **정상 준비:** Data VM→VPN/TLS→RDS 논리 덤프→압축/age 암호화→S3 HTTPS 업로드→로컬 다운로드/무결성·완성본 확인. Image는 Harbor, Manifest/도구/CA·암호화 설정은 Recovery Bundle로 확보합니다.
- **복구 실행:** 로컬 검증 Backup 선택/해독→새 전용 VM의 격리 MariaDB 복원→직접 TLS 접속→새 Recovery Redis→별도 Secret·보존 Manifest Apply→사용자 Host 안내→대표 업무/영속 데이터 검증.
- **필수 표시:** Data 작업 VM과 복구 DB VM은 별도. 기존 1차 DB/MaxScale/Redis를 덮어쓰지 않음. 2026-10-05 개정 요구사항은 운영 중 Portable Backup 15분 주기·일반 7일 보존, RTO 10분/영속 DB RPO 30분이며 달성값이 아니라 설계·시험 목표입니다. 최초 제작 당시의 1시간·30분/90분 기준은 03 §3-I.14의 이력에 보존합니다.
- **주의:** 장애 후 AWS/S3/GitHub/Cloud IDP/ECR/KMS 신규 조회가 복구 필수 단계인 선은 그리지 않습니다. 로컬 DNS/Harbor/기존 플랫폼까지 차단하는 시험으로 확대하지 않습니다. RDS PITR와 Portable Backup은 다른 경로입니다.
- **근거:** 03 §3-C.12.7·§3-D.9.3~9.8·§3-F.17.3·§3-G.7, 04 §5.1·5.5·§10.2.
- **남은 입력:** 실제 독립 Storage/Key/호환 도구·Backup·Bundle·Restore 결과. 계획된 사전 준비와 복구 순서를 제작합니다.

### 11 HA와 장애 영향 범위

- **목적:** 플랫폼 기본 HA, 애플리케이션 복구, On-Prem Restore-based Recovery의 차이를 보여줍니다.
- **포함:** Pod/Worker/AZ, RDS Primary/동기 Standby, Redis Primary/비동기 Replica, VPN Gateway, CI·Data VM·Harbor/Storage·On-Prem 전체, 잘못된 배포/데이터 손상의 영향과 대응.
- **핵심 판단:** VPN/On-Prem 장애는 기존 Cloud 서비스와 신규 배포/백업에 다른 영향을 줍니다. Redis Failover와 Runtime 전체 소실·DB 복원은 같은 복구가 아닙니다.
- **주의:** RDS Standby를 읽기 Replica로, Multi-AZ/PDB를 전체 무중단 보장으로 그리지 않습니다. 단일 Gateway의 수동 재구축과 Cloud 장애의 로컬 복원을 구분합니다. Managed CP EC2 강제종료/etcd 수정은 기본 시험에 넣지 않습니다.
- **근거:** 02 §25~27, 03 §3-B.9.8·§3-E.14·§3-F.18·§3-G, 04 §10.2.
- **남은 입력:** 실제 장애 주입·탐지·서비스 영향·MTTR/RTO/RPO·재시험. 지금은 장애 영역/목표 대응도이며 PASS·달성 수치를 붙이지 않습니다.

### 12 1차에서 2차로의 책임 이전

- **목적:** 이전의 기술 목록보다 역할을 유지·재배치·대체한 이유와 1차 보존 경계를 설명합니다.
- **포함:** 1차 실제 구현을 기준으로 kubeadm/Calico·Gateway·MariaDB/MaxScale·Redis·Jenkins/Harbor·Argo·Storage/관측과 2차 대응 역할을 연결합니다.
- **이전 흐름:** 최신 검증 Seed 선택→격리된 2차 환경의 논리 DB 이전 예행→새 Redis/Release 기능 검증→쓰기 제한/진행 작업 종료·최종 복사→전환/되돌림 판단. 수행 완료가 아니라 승인된 절차입니다.
- **주의:** 1차 계획 PNG의 18 VM·ANALYSIS·추가 LB/MaxScale를 실제 MVP로 가져오지 않습니다. 00의 실제 기준을 사용합니다. 아직 최종 판정되지 않은 개별 자원은 Retire/완료로 단정하지 않습니다. Cloud 쓰기 이후 DNS만 되돌려 데이터까지 복구된다고 표현하지 않습니다.
- **근거:** 00 §6·8·12, 02 §2.3, 03 §3-A.6·§3-D.2~7.
- **남은 입력:** 실제 Seed/재사용 경로·Migration/전환·최종 역할별 판정. 목표 역할 대응으로 먼저 제작합니다.

## 4. 표현과 파일 형식 제안

참고로 확인한 자료:

- [1차 전체 논리 아키텍처 PNG](https://github.com/seokpan/seokpan-docs/blob/main/logical-architecture/01_SeokPan_%EC%A0%84%EC%B2%B4%20%EB%85%BC%EB%A6%AC%20%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98.png): 영역별 박스·계층·제품 아이콘 중심의 상세 구조. 실제 이미지 확인.
- [1차 문서 README](https://github.com/seokpan/seokpan-docs/blob/main/README.md): 기획 PNG와 실제 MVP 현황을 구분해 안내. 현재 1차 문서의 이미지 목록도 확인.
- [개인 OpenShift 운영 점검 SVG](https://github.com/tjung03/OpenShift/blob/main/docs/images/operations-flow.svg): 간결한 흐름·일관된 색상·큰 글자. SVG 원본 구조 확인.

**권고는 영역별 배치의 명확함과 SVG의 선명한 글자/편집성을 함께 사용하는 방식입니다.** 특정 이미지의 배치나 당시 구성요소를 그대로 복사하지 않습니다. 논리/물리 전체도는 역할·환경 구분 중심, 흐름도는 목적이 있는 연결선 중심으로 만듭니다.

| 요소 | 제작 방향 제안 |
| --- | --- |
| 언어 | 제목·역할·설명은 한국어, AWS/ROSA 제품명·Protocol·명령은 공식 영문 유지. 디렉터리/파일명은 영어 |
| 기본 화면 | 문서/발표에서 읽기 쉬운 밝은 배경·큰 글자·AWS/On-Prem/관리형/직접 관리 경계 |
| 색상/아이콘 | 소수의 일관된 색상, 식별에 도움이 되는 정확한 제품 아이콘. 아이콘을 모두 채우기 위한 추가 자원 금지 |
| 연결선 | 전체도에는 핵심 관계만, 상세도에는 방향·Protocol/목적을 표시. 외부/사설/복구 경로를 문구로도 구분 |
| 분량 | 한 장당 하나의 주된 설명 목적. 복잡하면 같은 장의 패널을 나누고 글자를 작게 줄이지 않음 |
| 상태 | 그림 제목 또는 본문 캡션에 설계 목표/실제 구축·기준일·근거·초기 후보/확인 대기 표시 |
| 편집 원본 | 정확한 자원·문자·주소·연결을 관리할 수 있는 SVG 중심. 필요 시 draw.io 원본도 함께 보존 |
| 배포용 | GitHub README는 PNG 미리보기와 SVG 원본 링크, 발표/문서 삽입은 고해상도 PNG. 같은 그림의 다른 형식은 장수에 추가하지 않음 |
| 생성 방식 | 정확한 도형·글자·연결은 편집 가능한 벡터로 제작. 장식 이미지 생성만으로 아키텍처 정확성을 판정하지 않음 |

다음 경로에 설계 그림 12장의 SVG 원본을 생성했습니다. [그림 목차](README.md)에서 각 SVG/PNG를 확인합니다.

| ID | SVG 원본 경로 |
| --- | --- |
| 01 | `architecture/diagrams/01-logical-architecture.svg` |
| 02 | `architecture/diagrams/02-physical-architecture.svg` |
| 03 | `architecture/diagrams/03-hybrid-network.svg` |
| 04 | `architecture/diagrams/04-service-traffic-tls.svg` |
| 05 | `architecture/diagrams/05-state-reconnect-consistency.svg` |
| 06 | `architecture/diagrams/06-cicd-release-flow.svg` |
| 07 | `architecture/diagrams/07-iac-gitops-ownership.svg` |
| 08 | `architecture/diagrams/08-identity-secret-supply.svg` |
| 09 | `architecture/diagrams/09-observability-evidence.svg` |
| 10 | `architecture/diagrams/10-backup-offline-recovery.svg` |
| 11 | `architecture/diagrams/11-ha-failure-domains.svg` |
| 12 | `architecture/diagrams/12-migration-responsibility.svg` |

PNG는 같은 이름의 `architecture/exports/*.png`로 폭 3600px로 출력했습니다. README에는 전체 구조 등 소수의 그림을 우선 배치하고, 상세 그림은 목적별 목차로 연결합니다. 긴 설명은 이 Markdown에서 관리합니다.

## 5. 제작 순서

1. **계획 확인 — 완료:** 제작 계획의 범위를 확인하고 제작을 진행했습니다.
2. **01/02 시안 제작 — 완료:** 전체 논리·물리 2장으로 글자 크기·정보량·배치를 자체 확인했습니다.
3. **03/04/06/10 제작 — 완료:** Hybrid·사용자 통신·CI/CD·백업/복구 경로를 전체 그림과 대조했습니다.
4. **05/07/08/09/11/12 제작 — 완료:** 상태·Owner·인증/Secret·관측·장애·Migration을 제작했습니다.
5. **전체 12장 자체 검증 — 완료:** 문서/그림·그림끼리·SVG/PNG의 내용과 가독성을 확인하고 목차를 연결했습니다. 사용자 최종 그림 검토는 별도입니다.
6. **구축 결과판 작성 — 대기:** 문서 05의 관련 증거를 확인해 실제 전체 논리·물리 아키텍처를 별도 파일로 작성합니다. 설계 목표판은 보존합니다.

그림 02의 실제 Host/VM 배치판은 실제 입력을 기다립니다. 문서 05 전체 종료까지 기다릴 필요는 없으며 해당 그림의 입력·증거가 확보된 시점에 작성합니다. 장애/복구 시간선·측정 그래프·Troubleshooting 그림은 해당 Run에 설명 가치가 있을 때 추가합니다. 지금 가상의 측정 그림이나 추가 장수를 정하지 않습니다.

### 5.1 후보·배정 확인·실제 구축의 구분과 결과판 작성 시점

‘실제 AZ·Host·VM 배치와 규모 후보를 구분한다’는 표현은 전체 아키텍처가 계속 후보라는 뜻이 아닙니다. 지침 §13·§27~28, 03 §3-B 및 04 §1·§4·§5.5에 따라 다음 상태를 구분합니다.

| 항목 | 현재 문서상 상태 | 후보/대기 상태를 벗어나는 근거 | 그림 반영 시점 |
| --- | --- | --- | --- |
| Cloud Primary/On-Prem Recovery, ROSA Classic Multi-AZ, VPC·Subnet·NAT 구조 | 승인된 설계 | 이미 승인됨. 같은 결정을 다시 승인받지 않음 | 현재 설계판에 확정 구조로 표시 |
| AZ-A/B/C와 실제 AZ 이름/ID의 대응 | 승인된 3 AZ 구조의 실제 배정 확인 대기 | 담당자가 확인한 계정/Region의 AZ와 코드 입력. 생성 후 자원 조회로 실제 대응 확인 | 확인된 입력은 목표 배치도 개정에, 생성 확인값은 구축 결과판에 반영 |
| Worker 사양·앱 Replica·버전 등 초기 검증 후보 | 승인된 초기 검증 후보 | 담당자의 실제 지원·Quota·부하 요구·가격/Window 대조와 구현 입력 채택. 첫 Full Apply 전 Cost Gate 준수 | 채택값은 구현 목표로 표시. 생성/배포 조회로 실제 적용 확인 후 구축 결과판에 반영 |
| 새 전용 복구 DB VM | 전용 VM 모델 승인, Host·CPU/RAM/디스크·주소 확인 대기 | 이유빈·김상희가 Host 여유와 1차 격리를 확인해 실제 배치/사양을 기록. 생성·설정 조회로 실제 자원 확인 | 실제 배치가 확인된 영역부터 결과판에 반영 |
| 복구·HA·성능 성과 | 시험 목표, 실제 결과 미확인 | 해당 Run의 실행 조건·Actual Result·Evidence·판정 | 배치도 완성 후에도 시험 전에는 미검증으로 유지. 결과 그림은 해당 Run 확인 후 작성 |

구축 결과판은 **05의 해당 영역에서 자원 배치가 실제 확인된 시점**에 작성할 수 있습니다. 일부만 확인됐으면 확인 시점을 붙인 중간 결과판으로 만들고 미구축/미확인 영역을 명시합니다. Terraform Plan이나 GitOps 선언만으로 Runtime 구축 완료를 표시하지 않습니다. 전체 결과판은 Cloud·On-Prem 배치와 적용 Release를 대조한 뒤 작성하고, 10/16 Technical Freeze 전후 실제 구조가 안정되는 시점에 발표용 판본을 정리하는 것을 권고합니다. 이 시점은 새 강제 일정이나 구축 성공 보장이 아닙니다.

설계판만으로 설계 의도는 설명할 수 있습니다. 다만 최종 보고·포트폴리오의 ‘실제 구축’ 설명에는 확인 시점과 증거가 연결된 결과판이 적합하므로, 관련 입력이 확보되면 전체 논리·물리 결과판 2장을 후속 작업으로 작성합니다. 지금은 이번 첨부에 05/Runtime 증거가 없어 실제 구축 상태를 채울 수 없습니다.

## 6. 검증과 변경 처리

- [x] 각 그림의 요소·연결선·상태를 근거 문서와 대조
- [x] 정상 Cloud Runtime의 On-Prem/VPN 비의존, HA/DR, Data/Secret/Owner 경계를 모든 그림에 일관되게 적용
- [x] RDS/Redis 수와 역할, 9 Subnet과 예비 블록, Node/Replica 후보 상태를 대조
- [x] 04의 새 복구 DB VM·직접 TLS·담당·인증·보관·Release 결정을 반영
- [x] 실제 Host/IP/Path/Version/측정값을 추정하지 않고 남은 입력·반영 대상을 기록
- [x] 로컬 SVG 렌더와 PNG의 글자 겹침·잘림·잘못된 연결·출력 가독성 확인
- [ ] GitHub 브라우저에서 SVG 표시 확인
- [x] Credential/State/Plan/개인정보/평문 Backup/보호 원본 경로의 공개 여부 확인
- [x] Source·결정 변경 시 의존 그림 재검증과 원본/출력 갱신 절차 기록
- [x] 제작과 검증, 설계 승인과 Runtime/시험 PASS를 구분

설계 목표 그림의 완성을 실제 환경의 HA/무중단/DR 달성이나 예산 충족의 증거로 사용하지 않습니다. 문서 05에서 실질적인 설계 변경이 필요하면 결정·영향을 기록하고 그림을 개정해 이전 목표와 실제 결과를 추적할 수 있게 합니다.

원문·설계 판단·계획 보완의 연쇄 재검증은 [검토 기록](REVIEW_RECORD.md)에서 확인합니다. 이 기록은 제작 전 계획 검토의 이력입니다. 제작한 그림의 시각/파일 검증은 [제작 검토 기록](PRODUCTION_REVIEW.md)에 별도로 남겼으며 Runtime 시험과 구분합니다.

## 남은 작업과 다음 단계

- [x] 후속 진행 요청 확인·전체 12장 제작·자체 검증·목차 연결
- [ ] 그림 검토·표시 확인 의견 반영
- [ ] 실제 입력/Run 확인 후 구축 결과판·추가 결과 그림 작성

[제작 검토 기록](PRODUCTION_REVIEW.md)에 제작 중 보완과 시각/파일 검증 결과를 기록했습니다. 문서 05의 입력을 기다리는 부분은 실제 환경값·검증 결과를 사용하는 곳입니다. 설계판 12장은 제작했으며 실제 구축 결과판은 별도로 작성합니다.
