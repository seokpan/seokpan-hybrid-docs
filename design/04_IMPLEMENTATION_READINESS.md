# 石나가는 판단 2차 프로젝트 04 구현 준비와 실행계획

> **현재 단계:** 03 종료 유지, 04 문서 전체 종료 — 후속 05 구현·통합·검증으로 인계  
> **기준일:** 2026-10-01 KST  
> **상태:** 역할/Root 실행 책임, 복구 DB 직접 연결, AWS Provider 6.67.0 초기 후보, GitOps Writer PAT, Secret 주·예비 보관자와 Release/Evidence 형식 확정. 새 VM 생성 가능 사용자 확인. 전용 새 복구 DB VM과 유지 비상 관리자·초기 인증 회수 모델까지 사용자 채택. 전체 연쇄 보완·재검증 수렴, 추가 보완 0건으로 04 문서 전체 종료. 실제 입력·구현·시험은 후속 Gate로 인계  
> **상위 기준:** 승인된 `01_PROJECT_CHARTER.md`, `02_TARGET_ARCHITECTURE.md`, `03_DETAILED_DESIGN.md`, `PROJECT_INSTRUCTIONS.md`와 사용자의 최신 명시적 결정  
> **기간과 AWS 한도:** 2026-09-28~2026-10-26, $500. 승인된 계획선 $450와 여유 $50 유지

> **2026-10-03 DR 재검토 인계:** 기존 문서 종료와 운영 결정은 유지하며, 사용자 재검토 요청의 설계 판단은 [03 §3-I.14](03_DETAILED_DESIGN.md#recovery-design-review-20261003)에 연결한다. 05 전체 구현 후에만 00–04를 수정하는 순서는 아니다. 새 목표·백업 주기·DR 구조는 미확정이며 05는 기존 W04 예행의 부족한 근거를 확보하는 실행 기록이다.

이 문서는 승인된 03 상세설계를 실제 작업자, 입력, 인계, 일정과 구현 시작 조건으로 연결한다. 03의 설계 기준은 유지하고, 04에서 확정된 운영 결정과 아직 확인하지 못한 실제 값을 구분해 기록한다. 사람별 역할, 작성과 리뷰 책임, Root별 실행 책임, 복구 DB 직접 연결, AWS Provider 6.67.0 초기 후보, GitOps Writer PAT, Secret 주·예비 보관자와 Release/Evidence 운영 형식, 전용 새 복구 DB VM과 비상 관리·초기 인증 회수 모델이 확정됐다. 새 복구 VM 생성은 가능하다는 사용자 확인을 받았고 Host의 자원 여유는 아직 예상이다. AI의 코드 작성, 배포, 계정 변경, 데이터 이전, 시험과 비용 확인은 완료된 것으로 표시하지 않는다. 팀원의 선행 Bootstrap 코드와 시험 보고는 별도 출처/범위로 기록한다. 추가 demo2 보고의 최유준 A/B/C 예제·관측·정책 검증과 부분 정리도 보고 범위로 접수하며 실제 base/ROSA 시험과 구분한다.

현재 진행 현황:

- [x] 최신 등록 03의 두 피드백 수정과 첨부본 일치 확인
- [x] 사용자 확인을 근거로 03 문서 단계 종료
- [x] 00 §30.6 이후 추가 역할 변경이나 확정 없음 확인
- [x] 영역별 작성과 Root별 실행 담당안 사용자 채택
- [x] ocp-lab 후속 검증을 최유준 책임으로 연결
- [x] 역할의 직접 영향과 후속 인계 조건 기록
- [x] 격리 복구 MariaDB 직접 연결안 사용자 채택
- [x] 복구용 새 VM 생성 가능 사용자 확인
- [x] AWS 자격증명 공지와 Infra Source/Issue 결과 대조
- [x] AWS Provider 6.67.0 초기 검증 후보 사용자 채택
- [x] GitOps Writer PAT 하나와 무기한 우선/허용 최대 수명 사용자 채택
- [x] 범위별 Secret 주·예비 보관자와 Release/Evidence 운영 형식 사용자 채택
- [x] 계정 대여를 포함한 협업 설명과 실제 수행자 기록 연결
- [ ] 원래 demo2 수행자와 미커밋 Overlay 제공자 확인
- [ ] Source, 계정, 도구, 권한, 로컬 자산과 가용시간 확인
- [x] 전용 새 복구 DB VM과 유지 비상 관리자·초기 인증 회수 모델 사용자 채택
- [x] 입력 인계 대장·실행 절차·Release/Run 양식과 문서 종료 조건 정리
- [x] 추가 demo2 A/B/C 검증 보고의 결과·잔존·후속 책임 대조
- [x] PR #11 merge와 새 Root/State Key/정확 버전·입력 전달 문서의 Source 정합 확인
- [x] 두 새 구조안의 직접·후속 영향 반영
- [x] 04·지침 전체 재검증 수렴과 04 문서 전체 종료 판단
- [ ] 작업별 실제 구현 시작 조건 충족과 실행

## 1 03 종료와 04 사용 범위

2026-10-01 최신 등록 사본에서 03 §3-D.4는 `00_PROJECT_STARTING_POINT.md §5`로 정정됐고, §3-G.1은 일부 지정 Source 조회, 최종 Seed 미확인, Runtime 미검증과 ROSA 최종 시험 NOT RUN을 구분했다. 해당 사본은 수정된 첨부본과 바이트 단위로 일치했다. 사용자는 동일한 파일의 프로젝트 소스 업로드 완료를 확인했고, 이번 확인을 거쳐 03 문서 단계를 종료했다.

03의 당시 "실제 배정 확인 전" 기록은 작성 당시 상태다. 이 문서의 새 결정이 현재 사람별 배정을 제공하며, 완료된 03을 다시 작성 중으로 되돌리는 뜻은 아니다. 사용자가 03 종료 뒤 04를 진행하도록 명시했으므로, 03 §3-H.1의 당시 준비 기록 방식에 이어 이 04 문서에서 후속 준비를 관리한다. 00의 `GATE 4 — Foundation Build`와 이 문서의 04 번호는 서로 다른 식별자다.

다음 승인 기준을 유지한다.

- Cloud Primary와 On-Prem Restore-based Recovery, ROSA Classic Multi-AZ, RDS MariaDB Multi-AZ, ElastiCache Redis OSS Multi-AZ
- App, Infra, GitOps, Docs 네 저장소와 1차 독립 포트폴리오 보존
- bootstrap, foundation, rosa 세 Root와 State, 목적별 실행 Role, 제한된 비밀값 아닌 입력 전달
- ECR Cloud Runtime Pull과 Harbor Recovery 보존, GitOps와 Secret 공급의 소유권 분리
- SOPS+age와 범위별 Secret 공급, Git 밖 암호문 원본과 오프라인 예비 Key
- App 자동 Sync/SelfHeal과 자동 Prune 보류, 제한된 Offline Ansible Apply 예외
- 승인된 버전과 규모의 초기 후보, 시험 목표, $450 계획선과 $500 한도, 10/16 Technical Freeze 등 기존 일정

03 §3-B에서 서울 전용 **VPC 1개·3 AZ·Subnet 9개(Public 3/ROSA Private 3/Data Private 3)·AZ별 NAT 3개**는 이미 설계 승인됐다. VPC/Machine CIDR은 `192.168.64.0/20`, Subnet은 `.64`~`.72`의 /24이며 `.73`~`.79`는 예비 주소 블록이다. ROSA 설치 입력은 Public/ROSA Private의 6개이고 Data Subnet 3개는 DB/Redis 인스턴스 3대를 뜻하지 않는다. 실제 AZ 이름/ID·생성된 Resource ID·Host `/32`·지원/가격·Plan 결과는 구현 입력/증거로 확인한다.

다음 문서 **05는 구현·통합·검증의 진행 기록**이다. 핵심 구조 설계는 03에서, 운영 책임·남은 구조 결정·실행 인계는 04에서 끝낸다. 05는 추가 설계 승인 문서를 계속 만드는 단계가 아니며 00의 GATE 5(Migration), WBS의 W05(Cost Gate)와도 다른 번호다. 준비된 독립 영역의 입력 확보·코드/정적 확인·로컬 예행은 병행하고 공유 State·Restore·Cloud 가동은 의존 순서와 실행 Gate를 지킨다.

새로운 실제 지원, 비용, Source, 자산의 제약이 위 기준 변경을 요구하면 문제와 영향을 제시해 해당 변경을 별도로 결정한다. 역할 확정만으로 계정 권한, 코드나 시험 결과를 확인했다고 기록하지 않는다.

## 2 확정된 역할 결정

### 2.1 결정 기록

| 항목 | 기록 |
|---|---|
| Decision ID | PH2-04-ROLE-ROOT-EXECUTION |
| 결정일 | 2026-10-01 KST |
| 사용자 확인 | 00 §30.6 이후 변경하거나 확정한 역할 배정 없음. 직전의 영역별 작성과 Root별 실행 담당안 채택에 동의 |
| 기존 상태 | 03은 A~D 작업 트랙과 공유 실행 Owner 원칙을 승인했고, 사람별 실제 배정은 확인 전이었다 |
| 채택안 | 기존 담당 영역을 이어가며 작성, 통합, 리뷰, 공유 실행 책임을 구분. bootstrap/foundation 실행은 이유빈, rosa 실행은 정태훈 |
| 검토한 대안 | Terraform 전체 실행 한 사람 집중, 영역별 작성과 Root별 실행 담당, 주요 영역 재배정 |
| 근거 | 00 §30.6 초안의 연속성 유지, Network/Data/ROSA 통합 실행의 집중 완화, 실제 Root 전체 검토와 인계 책임 확보 |
| 직접 영향 | Root와 Repo별 작성, Plan 검토, 실행 인계, base/lab 검증 책임 |
| 후속 영향 | Caller/MFA/Role, 제한 입력, Source와 Secret 인계, Release, T/IF/IM 시험, W02~W08 일정과 비용 |
| 재검토 조건 | 사람별 가용시간이나 업무량 불충족, 필요한 권한/도구 확보 실패, 인계 지연, 소유권 충돌, Freeze 또는 예산을 위반하는 실행계획 |
| 미확인 | 개인별 권한/Branch 규칙, Merge 책임, 실행 Controller, 가용시간, 실제 소요/가격과 시험 결과 |
| 관련 근거 | 00 §30.6, 03 §3-H.2~4와 §3-I.13.4, GitOps Issue #1, 이번 사용자 명시적 동의 |

### 2.2 작성과 실행과 리뷰 배정

| 대상 | 작성과 통합 담당 | 공유 실행 담당 | 리뷰와 인계 |
|---|---|---|---|
| bootstrap Root | 이유빈 | 이유빈 | 정태훈이 Backend/Role과 후속 실행 연결 검토 |
| foundation Root | 이유빈 전체 통합, 김상희 Data 영역, 최유준 Registry/CI 권한 영역 작성 | 이유빈 | 정태훈 ROSA 입력 검토, 김상희와 최유준 담당 영역 Plan 검토 |
| rosa Root | 정태훈, 이유빈 기반 연결 협업 | 정태훈 | 이유빈 Network/IAM/기반 입력 검토 |
| App와 GitOps base/Overlay | 정태훈 | 정태훈 배포 변경 조율 | 최유준 Image/Pull/CI, 김상희 DB/TLS/Migration 검토 |
| Data 이전과 Backup/Restore | 김상희 | 김상희 | 정태훈 App 연결과 업무 재개 조건 검토 |
| CI와 관측과 시험과 Evidence Index | 최유준 | 최유준 시험 조율 | 각 담당자가 자기 결과를 작성하고 관련 담당자가 상호 리뷰 |

Registry/CI 코드를 작성하는 최유준과 Data 코드를 작성하는 김상희가 foundation의 별도 State를 만드는 것은 아니다. 코드 원본은 기존 Infra 경계 안에 두고 이유빈이 해당 Root 전체 변경을 통합해 실행한다. 역할 배정은 승인된 Terraform/GitOps/Secret의 Resource 소유권을 바꾸지 않는다.

정태훈은 ROSA 생성과 App/base 통합을 함께 담당하므로 실제 가용시간을 확인해 지원 작업과 인계 시점을 조정한다. 이유빈도 foundation 전체의 통합 부담을 가지므로 C/D 영역 리뷰를 Root 전체 승인 없이 단독 Apply하는 방식으로 대체하지 않는다. 사람별 예상 시간이 없는 현재 단계에서 균등 분담이나 일정 충족을 완료로 기록하지 않는다.

### 2.3 Root 실행 인계

| 실행 단위 | 시작 전에 대조할 입력 | 다음 담당에게 넘길 결과 |
|---|---|---|
| bootstrap | 개인 인증과 MFA, Account/Region, 기존 자원 충돌, Backend/Role 선언. 최초 신규 환경은 Local State 보호와 Remote 이전 조건, 현 기존 환경은 §8.6의 Remote 정본·이전 이력·Caller/Lock과 새 경로 확인 | 최초 환경은 보호된 Remote 이전 결과, 현 기존 환경은 정본 연결/점검 결과를 인계하며 이전을 반복하지 않음. 목적별 Role·비밀값 아닌 참조·Root 실행 조건 |
| foundation | 검토된 Root 코드/Plan, 개인 MFA/STS와 목적 실행 Role, Backend State Key, Data/Registry/Network 변경의 전체 영향 | Account/Region와 생성 조합, 필요한 Output만 담은 입력 개정, Data/SG/Endpoint 등 허용된 참조 |
| rosa | 최신 foundation 인계, 실제 지원/Quota, 개인 MFA/STS와 목적 실행 Role, Backend State Key, 생성/삭제 경계와 Cost 조건 | 새 Cluster ID/Context와 Node/Role/Host 참조, Bootstrap/GitOps/Secret 인계 조건 |

같은 State에 대한 쓰기 실행자는 작업 기록에 지정한 한 사람으로 유지한다. 다른 Root라도 공유 SG/Network/Data 등의 의존성이 있으면 인계를 확인한 순서대로 변경한다. 사람이 Root를 넘겨받을 때는 마지막 코드/Plan과 실행 상태, Lock, 미완료 변경, 실제 Caller와 입력 개정을 확인한다. 위 표는 실행 전 확인 절차이며 실제 실행 결과가 아니다.

### 2.4 공동 참여와 계정 사용 기록

2026-10-01 사용자는 필요하면 팀원이 서로의 계정을 물리적으로 빌려 사용할 수도 있고 실제로 전원이 참여한다고 설명했다. 동시에 설계상 역할·보관자 배정의 의미에 동의했다. 이 설명은 팀의 허용된 협업 방식과 참여에 관한 사용자 제공 정보로 기록한다. 특정 Run에서 누가 어느 계정을 사용했는지 또는 어떤 작업을 완료했는지까지 확인된 것은 아니다.

설계의 실행/보관 책임은 유지하고 실제 작업 기록은 아래처럼 구분한다. 계정 대여를 이유로 역할안을 다시 승인받거나 모든 Key의 수신자를 네 사람 전체로 확대하지 않는다.

| 기록 | 의미와 범위 |
|---|---|
| 배정된 실행 책임자 | 승인된 Root/Restore/시험 인계 책임 |
| 실제 수행자 | 해당 명령·UI를 실제 실행한 사람 |
| 관측 인증 주체 | 해당 실행의 OS 계정, AWS User/Role, GitHub/Cluster Principal 또는 보호된 Profile 참조 |
| 계정 관리 책임자 | 사용한 개인 계정/접근 수단의 관리 주체. AWS Account 소유 주체와 구분 |
| 협업 참여자와 작업 | 작성·설명·리뷰·진단·입력 제공 등 실제 참여 내용 |
| 차용/인계 참조 | 대상·범위·시각·실행 인계와 사용자 설명의 참조. Credential 값은 기록하지 않음 |

Caller/Commit 계정만으로 실제 사람의 기여를 단정하지 않는다. 권한 시험은 실제 사용한 Principal과 적용 정책으로 판정하며 Admin 사용 결과를 제한 Role의 PASS로 바꾸지 않는다. 설계상 범위 분리가 실제 운영에서도 달성됐는지는 개별 결과로 확인한다. 같은 State의 실행을 한 사람씩 인계하는 원칙과 기존 Root 책임은 유지한다.

## 3 base와 ocp-lab 인계

### 3.1 향후 실습 담당

사용자의 ocp-lab 추천안 채택은 최유준이 향후 Argo 검증을 실행하고 결과를 조율하는 책임으로 적용한다. 정태훈은 공통 base와 환경별 Overlay 통합을 담당한다. 기존 demo2 9항목 통과와 11건 발견의 원래 수행자, 미커밋 Overlay 작성자는 별도 출처 확인 상태로 남긴다. 최유준에게 과거 수행 이력을 소급해 부여하지 않는다. 추가 제공된 2026-10-01 16:04~18:30 A/B/C 보고는 최유준을 작업자로 명시한다. 그 수행 범위의 Argo 공개 예제·Native/UWM·정책/알림 검증은 팀 보고 완료로 접수한다. 실제 hybrid-gitops base 검증은 여전히 후속 작업이며 상세 영향과 정리 상태는 §8.5에 기록한다.

| 인계 | 책임 | 필요한 결과 |
|---|---|---|
| 공통 base 작성 | 정태훈 | Branch/전체 Commit, Render 결과, 공통 선언과 환경별 설정 차이, Secret 참조와 Migration 단일 실행 경계 |
| 기존 Overlay 제공 | 원래 사전검증 수행자와 작성자 확인 필요, 정태훈이 확보/통합 | 미커밋 변경 원본, Manifest 출처, 실제 Image Digest와 빌드 조건, CA/설정 차이, 원시 시험 기록 |
| 실제 base의 lab Argo 검증 | 최유준 | 추가 보고의 공개 예제 검증과 구분. 지정 Context/Namespace와 공유 Operator 사용 확인, base 전체 Commit 검증, Sync와 Secret/삭제 보호 결과 |
| DB/TLS/Migration 대조 | 김상희와 정태훈 | 1차 GRANT와 목적별 권한, 대역 DB의 조건, TLS/CA/Job 결과와 ROSA 미검증 구분 |
| 리뷰와 Merge | 해당 리뷰 담당과 실제 Repo 운영 책임 연결 | 최종 Commit과 검증 Commit의 차이, 필요한 영향 범위 재검증, Merge 권한과 Branch 규칙 확인 |

Cloud Application을 lab Branch에 연결하지 않는다. 실습 검증은 ROSA 최종 Acceptance가 아니며 검증 이후 코드/Manifest/Image가 바뀌면 영향을 받은 결과를 다시 확인한다. 앞선 demo2 결과를 PR의 최신 Commit 결과로 대체 표기하지 않는다.

2026-10-01 후속 읽기 조회에서 GitOps main은 `523e9206dd6398adc6776855573890063b837a85`였고 README와 .gitignore, main Branch 하나, 열린 PR 없음 상태였다. 이는 당시 관측이며 이번 역할/PAT 확정이 Branch 생성이나 base 작성 완료를 뜻하지 않는다. 실제 작업 시작 시 최신 Tree/Branch/PR을 다시 확인한다.

### 3.2 실습 정리 조건

기존 보고의 seokpan-app 유지 계획은 6단계 검증과 연결됐고, 추가 보고는 인계 문서 8단계에서 앱 검증 환경을 일괄 삭제한다고 기록했다. 18:27 기준 앱·예제용 빈 Project/managed-by·Operator·Redis requests 변경은 남아 있다는 보고다. UWM 시험 정리와 실습 전체 정리를 구분하며 정확한 삭제 시각은 새로 확정하지 않는다. 최유준이 검증 종료와 결과 보존을 확인하고, 정태훈이 Overlay/Release 인계를 확인하며, 기존 공유 환경 담당자의 사용 종료를 확인한 뒤 정리 시점을 계획한다. 미커밋 Overlay, Image/Digest, 시험 결과와 필요한 설정을 확보하고 테스트 Secret/CA/Key를 정리한다. 기존 1차 자원을 실습 정리 대상으로 포함하지 않는다.

## 4 실제 입력 확인 목록

아래 표는 승인한 배정을 실제 환경에 연결하기 위한 확인 목록이다. 현재 값과 증거가 없는 항목은 확인 전이며, 누락은 해당 의존 작업의 Blocker로 기록한다. 비밀번호, Token, Private Key, 전체 Credential이나 비밀값이 포함된 URL은 문서에 받거나 복제하지 않는다.

| 묶음 | 확인 책임 | 필요한 비밀값 없는 입력 또는 보호 경로 참조 | 막는 작업 |
|---|---|---|---|
| 사람과 협업 | 네 담당자, 각 영역 리뷰 담당 | 개인별 Repo 권한/Branch 규칙, Merge 실행자, 가용일/시간, 인계 연락 경로 | 해당 Repo 코드 시작과 리뷰/Merge, 세부 WBS |
| Source와 Seed | 정태훈 | 최신 검증 Commit와 근거, 미반영 Maintenance, Seed 전체 SHA, 대상 Repo 이력 충돌, 실제 Path/Client/Probe/인증 계약 | 실제 App 이관과 수정 |
| base와 lab | 정태훈과 최유준 | 기존 수행자, Branch/Commit와 미커밋 Overlay, Context/Namespace, Operator 책임, Image Digest, Secret 공급 참조 | lab Argo 검증 |
| AWS와 Controller | 이유빈, 정태훈 rosa 범위 | Account/서울 Region, Caller/MFA/STS/Role, Credit 조건, Quota/Classic 지원/구독, Red Hat/OCM 인증의 공급/만료/복원 참조, 도구/Provider/Lock, 실행 Workspace와 보호 저장소 | 실제값이 필요한 HCL 입력 확정·Plan/Apply. 비의존 선언 작성·도구/Schema·로컬 확인은 가능 |
| ROSA 개인 인증 | 정태훈, 이유빈 기반 인증 협업 | GitHub IDP/RBAC의 실제 Org/Team/사용자 매핑, 필요한 권한과 허용/거부/회수 결과, Bootstrap와 비상 접속 공급 참조 | 플랫폼 초기 설정과 개인 관리 접속 검증 |
| DB와 TLS | 김상희와 정태훈 | 1차 GRANT에서 비밀값 제거, 목적별 권한, Engine/Client/Driver/Schema, CA/Hostname 검증 경로, 데이터와 Dump 크기 | 권한 판정, 연결 수정 검증, Data 이전 |
| 로컬 Recovery | 김상희, 이유빈 기반 자산 협업 | 새 복구 VM 생성 가능 사용자 확인. 사용할 Host/Namespace와 실제 CPU/RAM/디스크 여유, 독립 DB Data Directory, Storage/NFS/독립 사본, 도구/Harbor/CA는 확인 전 | 확정된 전용 VM 모델의 실제 Host/용량 확정·배치, Offline 복구 |
| CI와 Registry | 최유준, 정태훈 App/Pull 협업 | 실제 Jenkins Job/Agent와 인증 공급 참조, Scan 도구/정책 결과, ECR/Harbor Artifact Mapping, PR 대상과 쓰기 인증 정책 | CI 변경과 Cloud Pull/Release 검증 |
| 비용과 Window | 최유준 집계, 이유빈 자원 목록, 김상희 Data 수명, 정태훈 ROSA 시간 | 서울 단가/출처, Credit 적용 범위, 누적/잔존, 실제 생성/삭제 시간, 가용일과 재시험 여유 | Window 확정과 첫 Full Apply Cost Gate |

Seed는 App 이관 직전에 고정한다. 그 전에 Source 읽기 조사나 공통 base 준비를 멈출 필요는 없으나, 실제 2차 코드 이관과 수정에는 대상 Repo/Branch/Owner와 해당 Source 기준을 확인한다. 전체 AWS 입력이나 Cost Gate 완료를 base 검토의 필수 선행으로 만들지 않는다.

## 5 결정 현황과 진행 순서

| 순서 | 결정·확인 항목 | 필요한 사실 | 현재 상태 |
|---|---|---|---|
| 1 | 로컬 복구 DB의 직접 연결 또는 격리 MaxScale 경유 | 단일 복원 목표, App Client/TLS 계약과 필요한 프록시 기능 | 직접 연결 사용자 확정 — 2026-10-01 |
| 2 | 복구 DB의 실제 배치와 사용 자산 | VM/Host/Namespace, Storage와 여유, 격리와 독립 보존 가능성 | 전용 새 VM 배치 §5.5 사용자 확정. 실제 Host/자원은 확인 전 |
| 3 | CI GitOps Writer의 실제 인증과 PR 권한 | 기존 GitHub/Jenkins 정책과 발급/만료/회수 책임 | PAT 하나 채택, 무기한 우선/제한 시 허용 최대 수명. 실제 정책/발급/등록은 확인 전 |
| 4 | 비상 관리 접속과 Bootstrap 계정 회수 | 정상 IDP/로컬 경로, 실제 지원/보관/사용/회수 책임 | §5.6 유지 비상 관리자/초기 인증 회수 모델 사용자 확정. 실제 지원/전환/회수 검증은 후속 인계 |
| 5 | Secret 주/예비 보관자와 보호 자산 | 승인된 SOPS+age 범위 분리, 독립 Key/암호문 사본과 복원 경로 | 사람별 배정 확정. 실제 Key/보호 자산/복원 결과는 확인 전 |
| 6 | Release Metadata와 대용량 Evidence 형식/경로 | CI/도구와 실제 보호 저장소, 보관 책임 | JSON/Markdown/CSV와 논리 경로/책임 확정. 대용량 보호 원본의 실제 위치는 확인 전 |
| 7 | 세부 WBS와 가동 Window와 실습 정리 시점 | 실제 Source 변경량, 가용시간/휴무, 단가/Credit/누적, 생성/삭제/재시험 시간 | 기존 목표 창을 유지하며 실제 값으로 구체화 |

각 결정은 현재 사실, 기존 팀 논의, 주요 대안, 제약/장단점/시간/비용, 권고, 사용자 검토와 명시적 확정, 영향 반영 순서로 다룬다. 이 목록은 현재 확인된 범위이며 새 제약으로 발견된 선택을 누락하지 않는다.

DB 접속 방식과 전용 VM 배치 모델은 각각 채택됐다. Endpoint, TLS 계정과 실제 용량까지 자동 확정된 것은 아니다. 반대로 자산 확인은 접속 구조의 독립 비교를 막지 않는다. 배치 모델의 채택과 실제 Host·용량의 확인을 구분한다. 해당 Host를 사용하기 전 자산을 실측하며 기존 1차 DB/MaxScale/Data Directory를 덮어쓰지 않는다.

### 5.1 확정된 로컬 복구 DB 직접 연결

**상태는 CONFIRMED DECISION이다.** 2026-10-01 사용자가 직접 연결안을 채택했다. 03 §3-D.3에서 MaxScale 재사용 여부를 별도 결정으로 남겼고, §3-D.9.8은 새 격리 2차 DB에 복원하도록 했다. §3-G.7의 RTO 30분 목표는 장애 주입/접속 불가 시작부터 탐지·복구 결정·Key/자료 준비·DB 복원·새 Redis·App 배포·Host 안내와 대표 업무/Data 확인 완료까지 포함한다. 접속 방식은 이 복구 목표와 1차 자산 보호를 기준으로 비교했다.

| 결정 기록 | 내용 |
|---|---|
| Decision ID | PH2-04-RECOVERY-DB-DIRECT |
| 결정일과 승인 | 2026-10-01 KST. 사용자 "직접 연결안을 채택" |
| 결정 | Recovery App이 새 격리 2차 MariaDB에 직접 TLS 연결. 복구 경로에 MaxScale를 추가하지 않음 |
| 근거와 대안 | 단일 DB 복원과 업무 재개 목표에 맞춰 Proxy 의존성을 줄임. 별도 MaxScale와 기존 1차 MaxScale 활용을 비교 |
| 확인된 조건 | 복구용 새 VM 생성 가능 — 사용자 확인 |
| 미확인 | 실제 Host와 CPU/RAM/디스크 여유, 채택한 VM의 용량/Endpoint/계정/CA와 Driver 호환, 수행 시간과 결과 |
| 사용자 예상 | 현재 자원이 부족하지 않을 것 같다고 했으나 실측 확인은 아님 |
| 담당과 영향 | 김상희 DB/계정/CA/Restore, 이유빈 Host 자산, 정태훈 Recovery 설정, 최유준 T04/T18과 복구 시간선. W04/W08/Bundle/Secret 연결 |
| 재검토 조건 | 필수 Proxy 기능, 직접 연결 호환성 문제, 복제/HA 요구 추가, 실제 자원 또는 시간/비용 제약 |

| 대안 | 편익 | 준비와 검증 부담 | 프로젝트 판단 |
|---|---|---|---|
| 격리 복구 MariaDB에 App 직접 연결 | 접속과 진단 경로가 짧고 별도 Proxy 기동에 의존하지 않음 | 실제 DB/Driver 호환, 목적별 계정과 CA/Hostname, Endpoint와 실패 시험 필요 | 채택. 실제 결과/소요는 미측정 |
| 별도 격리 MaxScale 경유 | 기존 Proxy 운영 경험과 Listener/Service 방식 활용 | Proxy 바이너리/설정/인증/보존, App→Proxy와 Proxy→DB TLS, Routing/Backend와 Proxy 실패 시험 추가 | 대안. 필수 Proxy 기능이 확인되면 재검토 |
| 기존 1차 MaxScale에 복구 Backend 추가 | 기존 프로세스를 활용할 수 있음 | 1차 Service/Listener/설정 변경과 경합, 기존 업무 영향, 복구 절차의 1차 Proxy 의존성 검토 필요 | 현재 비권고. 보호 범위와 변경 승인을 추가로 확인해야 함 |

MaxScale의 Listener는 Service로 연결 요청을 전달하고 Router가 Backend DB로 요청을 전달한다. 공식 문서는 들어오는 Client 연결과 나가는 DB 연결의 TLS를 각각 구성한다. [MaxScale Configuration Guide](https://mariadb.com/docs/maxscale/maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide), [Securing Your MaxScale Deployment](https://mariadb.com/docs/maxscale/maxscale-security/securing-your-maxscale-deployment)를 2026-10-01 읽어 기능 경계를 확인했다. [MariaDB Secure Connections Overview](https://mariadb.com/docs/server/security/encryption/data-in-transit-encryption/secure-connections-overview)는 Client/Server TLS와 인증서 검증을 설명한다. 실제 설치 버전과 App Driver의 지원/설정을 별도 확인한다.

직접 연결 선택은 제품 문서가 강제하는 구성이 아니라 프로젝트 조건에 따른 판단이다. 단일 복원 DB로 업무를 재개하는 현재 범위에서 복구 의존성을 줄이려는 이유다. MaxScale 한 개를 단일 DB 앞에 추가하는 것만으로 대체 DB나 복제 구성이 생기지는 않는다. 실제 App의 필수 Proxy 의존성, 직접 연결의 호환성 문제, 추가 복제/Proxy 기능 요구가 확인되면 이 선택을 재검토한다.

김상희가 격리 DB의 접속/계정/CA와 Restore 조건을 정리하고 정태훈이 Recovery App/Overlay 연결 계약을 반영한다. 최유준은 T04/T18의 TLS 실패, 오프라인 대표 업무와 전체 복구 시간선을 연결한다. W04 예행과 W08 측정, Bundle/Secret 보존, 후속 수정의 시간/비용을 같이 추적한다. 아직 30분 RTO나 90분 DB RPO를 달성했다고 기록하지 않는다.

이번 목표 재검토는 직접 TLS·전용 새 VM·새 Redis를 뒤집는 결정이 아니다. 현재 단계에서 이 구조가 필요한 사용자 범위와 감당 가능한 중단/손실을 충족하는지, 사전 준비/작은 절차 개선으로 충분한지 확인한다. Host/도구·사전 로컬 사본/Key/Image·담당자 대응·클라이언트 위치/접속 조건을 먼저 기록하고 §10.2의 t0~t1 전체 시간선과 손실·부담/비용을 측정한다. 세부 입력/기록은 [05 §9.2~9.6](../execution/05_IMPLEMENTATION_AND_VALIDATION.md#recovery-objective-review-20261002)을 사용하며 새 양식이나 모든 백업 주기/DR 구조의 비교 구현을 추가하지 않는다. 실측에 따라 운영 인계·목표·구조의 변경이 채택되면 이 문서의 해당 절을 보완한다.

신규 복구 VM 생성은 가능하다. 다음으로 이유빈과 김상희가 사용할 Host/Namespace, 실제 CPU/RAM/디스크 여유, 1차와 분리된 Data Directory, Backup/독립 사본과 Harbor/도구를 확인한다. 03 §3-D.10.5의 2 vCPU/4 GiB/40 GiB는 Data 작업 VM의 초기 검토 후보이며 복구 DB 용량을 확정한 값이 아니다. 실제 Data/Index/로그/Import 임시 공간과 여유를 대조해 채택한 전용 VM의 Host·용량과 디스크 배치를 확정한다. 이 입력이 없어도 Source 읽기, CI 인증/보관 비교, Release 형식 준비는 계속할 수 있다.

### 5.2 확정된 Jenkins GitOps Writer PAT

**상태는 CONFIRMED DECISION이다.** 2026-10-01 사용자는 PAT 하나로 Push와 PR을 처리하는 안을 채택했다. 만료는 무기한을 우선하고, 조직/제품 정책이 이를 허용하지 않으면 허용되는 최대 수명을 적용하는 기준으로 기록한다. 실제 Token 발급이나 Jenkins 등록, 조직 정책 변경을 수행한 상태는 아니다.

| 결정 기록 | 내용 |
|---|---|
| Decision ID | PH2-04-GITOPS-WRITER-PAT |
| 결정일과 승인 | 2026-10-01 KST. 사용자 PAT 하나로 Push·PR 채택, 무기한 우선/최대 만료 수명 선호 |
| 결정 | GitOps Repo 전용 Fine-grained PAT 하나로 HTTPS Git Push와 PR REST API 처리 |
| 만료 기준 | 무기한이 실제 허용되면 무기한. 제한이 있으면 제품과 조직 정책 안에서 허용되는 최대 수명. 실제 만료 설정/일자는 확인 후 기록 |
| 권한 | seokpan의 seokpan-hybrid-gitops 한 개, Contents write·Pull requests write·기본 Metadata read. Administration/Workflows/Org 권한을 추가하지 않음 |
| 실행 흐름 | CI 검증 후 Release Branch Push와 PR 생성. 사람 Review/Merge와 기존 main 보호 유지 |
| 근거 | 최소 초기 통합, 같은 Token으로 Git/PR 처리, 프로젝트 중 불필요한 만료 교체를 줄이려는 사용자 선택 |
| 관리 책임 | 최유준이 CI Credential 등록/검증/회수를 조율하고 정태훈이 배포/PR 경계를 리뷰. 실제 발급자는 Org membership·Repo 권한·정책을 확인해 연결 |
| 미확인 | 조직 PAT 허용/승인/최대 수명, 실제 발급자 권한, Token/Credential ID, Jenkins Job/Plugin, Branch Rule/Bypass |
| 기준 연결 | 03 §3-C.12.4의 제한 PAT 후보를 실제 Writer 방식으로 채택. 당시 유한 만료 후보보다 이번 사용자 결정의 무기한 우선/최대 수명 기준을 우선 적용. 완료된 03 원문은 보존 |
| 재검토 조건 | 조직 정책/발급자 제약으로 사용 불가, 실제 Push/PR 실패, 필요한 API 불충족, 인계/권한 회수로 유지 불가 |

| 비교한 주요 대안 | 편익 | 부담과 이번 판단 |
|---|---|---|
| Fine-grained PAT 하나 | 같은 Credential로 HTTPS Push·PR, 초기 설정이 작음 | 발급자/조직 정책에 의존. 사용자 채택 |
| GitHub App 하나 | 설치 Token 자동 발급, 사람과 구분되는 주체 | App/Key/Plugin 통합과 단계별 Token 공급 검증 추가. 미채택 대안으로 보존 |
| SSH Write Deploy Key + PR PAT | Git Push는 PAT 만료와 독립 | PR PAT의 만료 관리는 남고 SSH/Host Key와 PAT 두 경로 관리 |
| SSH Write Deploy Key + PR App | PR Token 자동 발급 가능 | SSH와 App 둘 다 준비. 특별한 SSH 필요가 없으면 경로가 늘어남 |
| SSH Write Deploy Key + 수동 PR | Git 인증은 만료일 없는 Key 사용 | Release마다 수동 PR. 기존 CI PR 생성 흐름을 바꾸는 별도 선택 |

[PAT 공식 문서](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)는 Fine-grained PAT의 무기한 수명을 허용하지만 조직/Enterprise 최대 수명 정책이 이를 제한할 수 있다고 설명한다. [조직 정책](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization)의 기본 최대 수명 설명을 실제 seokpan 정책으로 단정하지 않는다. 무기한은 지정 만료일이 없다는 뜻이며 사용자 권한 상실·정책 제한·회수와 무관한 영구 유효성을 보장하는 뜻은 아니다. 실제 정책을 확인해 적용값을 기록하고, 무기한 사용을 위해 조직 제한을 임의로 해제하지 않는다.

#### 5.2.1 실제 공급과 검증

| 항목 | 준비와 확인 조건 |
|---|---|
| 원본과 사용 사본 | Automation CI 목적별 암호화 원본 → 별도 Jenkins Credential. 일반 Build Job에 전체 Bundle이나 age 개인 Key를 공급하지 않음 |
| Credential | 같은 PAT를 사용하는 Username/Password Credential로 HTTPS Git와 REST Token Binding을 연결. 실제 ID/소유자/Job 범위는 보호 운영 기록에 연결 |
| Git Push | command-line HTTPS Git 인증을 Release 단계에 한정. Checkout 설정만으로 임의 Shell git push 인증까지 완료됐다고 보지 않음 |
| PR API | 같은 Token으로 PR 조회/생성/오류 판정 구현. 기존 PR이 있으면 중복 생성하지 않는 흐름과 결과 인계 확인 |
| 권한과 main | Branch Push/PR 생성, 보호 대상 직접 Push와 Review 없는 변경 차단, 미허용 쓰기와 회수 후 인증 실패 확인 |
| 수명 관리 | 실제 무기한/만료일·조직 승인·발급자와 사용 범위 기록. 유한 최대 수명인 경우 교체 책임과 시점 연결. 불필요해지면 사용 종료/회수 기록 |
| Argo Reader | 공개 GitOps Repo는 익명 HTTPS 읽기 필요 충족 여부 먼저 확인. 인증이 필요할 때만 별도 Reader 공급. Writer PAT를 Argo에 복사하지 않음 |

[PR API 공식 권한](https://docs.github.com/en/rest/pulls/pulls)에 따르면 PR 생성에는 Pull requests write, Merge에는 Contents write가 사용된다. PAT 하나로 Push와 PR을 처리해도 Token 권한만으로 CI Merge가 기술적으로 불가능해지지는 않는다. Pipeline 정책, main 보호/Ruleset와 실제 발급자의 Bypass를 함께 대조한다. 디렉터리별 쓰기 제한을 PAT 기능으로 주장하지 않으며, 다른 공개 Repo의 익명 읽기를 전체 접근 거부 시험으로 혼동하지 않는다.

2026-10-01 후속 조회에서 GitOps main은 `523e9206dd6398adc6776855573890063b837a85`였고 Tree는 README와 .gitignore, Branch는 main 하나, 열린 PR은 없었다. main의 protected 표시는 있었으나 세부 보호/Bypass는 확인하지 않았다. PAT 선택은 실제 base/Release/Pipeline 작성이나 Token 발급 완료를 뜻하지 않는다.

### 5.3 확정된 Secret 주·예비 보관 책임

**상태는 CONFIRMED DECISION이다.** 2026-10-01 사용자가 보관자 배정안 채택에 동의했다. 승인된 SOPS+age, Cloud Bootstrap/Automation/On-Prem Recovery 범위 분리와 독립 오프라인 예비본을 현재 사람 배정에 연결한다. 실제 Key/파일/보호 저장소·접근 설정과 복원 시험은 확인 전이다.

| 결정 기록 | 내용 |
|---|---|
| Decision ID | PH2-04-SECRET-CUSTODY |
| 결정일과 승인 | 2026-10-01 KST. 사용자 보관자 배정안 채택 동의 |
| 결정 | 아래 표의 범위별 주·예비 보관자, 목적별 파일/수신자 분리와 Backup 개인 Key 별도 관리 |
| 근거 | 기존 업무 책임과 부재/소실 대비, 전체 Key 집중 또는 전원 전체 복호화 대안 비교 |
| 영향 | Secret 공급/교체/회수, CI/Cloud Bootstrap, Offline Restore와 예비본 검증 |
| 미확인 | 실제 독립 저장 매체·보호 경로·Key·복호화와 서비스 동작 결과 |
| 재검토 조건 | 담당자 부재/권한/자산 제약, Key 회수나 보관/복구 실패 |

| 대안 | 편익 | 부담과 판단 |
|---|---|---|
| 한 사람이 모든 원본/Key 보관 | 초기 인계가 단순함 | 사람 부재/Host 소실 의존과 권한 집중. 기본안으로 비권고 |
| 범위별 주/예비 보관자 | 기존 업무와 연결하고 부재/소실에 대비 | 파일별 수신자·개정·예비본 검증 필요. 사용자 채택 |
| 네 사람 모두 전체 복호화 | 빠른 인계 | 불필요한 접근과 회수 범위 증가. 승인된 범위 분리의 운영 취지에 불리함 |

| 범위 | 주 보관자 | 예비 보관자 | 보관 범위 |
|---|---|---|---|
| Cloud Bootstrap | 정태훈 | 이유빈 | IDP·필요한 Reader·Cloud App 공급 항목. 실제 서비스별 발급/변경 책임은 유지 |
| Automation — CI | 최유준 | 정태훈 | GitOps Writer PAT·ECR CI·Harbor Publisher. 목적별 파일과 Job 공급 |
| Automation — Backup | 김상희 | 이유빈 | Backup SQL·제한된 S3 전송 Credential. CI 파일/수신자와 분리 |
| On-Prem Recovery | 김상희 | 최유준 | 로컬 DB/Redis/App·Harbor Pull·필요한 관리 Secret. 실제 App 저장 데이터 해독 Key는 사용 시 포함하고 Backup 파일의 age 개인 Key는 다음 행에서 별도 관리 |
| Backup 데이터 복호화 Key | 김상희 | 이유빈 | 대형 Backup 파일의 age 개인 Key. SOPS Bundle Identity와 목적 분리 |

WireGuard Peer Private Key는 승인된 별도 Host/담당자 범위로 유지하며 이유빈이 해당 보관 경로를 확인한다. 개인 AWS Admin Key/MFA와 Root Credential은 공유 Bundle에 넣지 않는다. 실제 App Signing/Data Encryption Key 필요 여부와 기존 데이터 해독 조건을 확인하고, 필요한 기존 Key를 임의로 재생성하지 않는다.

이 표의 예비 보관은 실행 책임의 자동 변경이 아니다. Apply/Restore 실행자 변경은 기존 인계 절차를 따른다. 독립 Recipient 둘은 둘 중 한 사람이 해독 가능한 구조이며 2인 동시 승인을 구현한 것으로 표현하지 않는다. 실제 Cloud App/Backup 권한과 다른 사람의 수신 범위가 다르면 논리 Bundle 안에서도 파일을 나눈다.

확인할 자산은 주 보관자의 보호 경로, 독립 암호문 사본, 별도 암호화된 오프라인 Key 매체와 해제 수단이다. 서로 다른 사용자 계정이어도 같은 Host/Disk만 사용하면 소실 대비가 충족되지 않는다. Data 생성 Job에는 Backup 공개 Recipient만 공급하며 개인 복호화 Key를 원본 생성 VM에 두지 않는다. 보호 원본 복원은 서비스 로그인/Pull/DB 연결로 검증하며 폐기된 PAT를 암호문에서 꺼내 유효하게 되살리는 절차로 취급하지 않는다.

### 5.4 확정된 Release·Evidence 운영 형식

**상태는 CONFIRMED DECISION이다.** 2026-10-01 사용자가 Release/Evidence 운영 형식 채택에 동의했다. 03 §3-A.8·§3-G.9·§3-I.7의 승인 필드와 Index 경계를 파일/인계 순서로 구체화한다. 실제 Release/Run 자료 생성과 수집/검증은 미실행이다.

| 결정 기록 | 내용 |
|---|---|
| Decision ID | PH2-04-RELEASE-EVIDENCE-FORMAT |
| 결정일과 승인 | 2026-10-01 KST. 사용자 Release/Evidence 운영 형식 채택 동의 |
| 결정 | JSON 조합/Run 기록, Markdown Summary/Index, CSV 수치/시간선과 아래 논리 경로 |
| 근거 | 자동 생성/검증과 원인 설명의 역할 분리, 기존 03 필드 유지와 중복 전사 완화 |
| 책임 | 각 실행자 자기 결과 작성, 최유준 형식/Index, 정태훈 배포 선언/Render, 김상희 Data/Backup, 이유빈 Infra/Caller 참조 |
| 미확인 | 실제 Artifact/Commit/Digest/Run과 대용량 보호 Storage 위치/권한/보존 결과 |
| 재검토 조건 | 실제 도구/수집 형식 충돌, 민감값 포함, 경로/보관 자산 제약 |

| 형식 | 편익과 부담 | 권고 용도 |
|---|---|---|
| JSON | CI 생성/필수 필드 확인에 적합, 긴 설명 작성은 불편 | Release 조합과 Run 조건/결과 식별정보 |
| YAML | Manifest와 함께 읽기 쉬움, 표현/타입 해석 관리 필요 | 기존 GitOps Manifest 유지. Release 기본 형식을 하나 더 늘리지 않음 |
| Markdown | 원인·제한·재시험을 읽기 쉬움, 집계 필드 일관성 관리 필요 | Summary와 상위 Evidence Index |
| CSV | 수치/Timeline 비교에 적합, 열·단위 정의 필요 | 비민감 Metric과 장애/재개 시간선 |

채택한 방식은 JSON + Markdown + CSV의 역할 분리다. 자동 생성된 JSON의 값을 사람이 옮겨 적는 중복을 줄이고, 원인/기여/제한은 Markdown에 작성한다.

| 논리 위치 | 내용 | 책임 |
|---|---|---|
| GitOps `releases/<release-id>.json` | 후보의 안정 Release ID, 이미 존재하는 App/Infra SHA·FE/BE Digest/플랫폼·Schema/Config/Secret 개정과 검토 근거 | 정태훈 선언 일치 확인, 최유준 CI 결과 제공 |
| Docs `evidence/<test-id>/<run-id>/release.json` | 실제 사용한 GitOps 전체 SHA까지 포함한 실행 조합·Render/Bundle 개정·Test Run | 실행자 제공, 최유준 형식/Index 연결 |
| 같은 Run의 summary.md | 기대/실제·판정·누락·제한·원인·재시험·기여 | 작업자 작성, 해당 Reviewer 검토 |
| 같은 Run의 metrics.csv/timeline.csv/checksums.txt | 비민감 수치와 단위·시간선·공유 가능한 산출물 무결성 | 각 트랙 수집, 최유준 연결 |
| 기존 보호 Storage | 대용량 원시 Log/영상과 보호 운영 자료. 공개 Index에는 논리 참조만 | 실제 Storage와 접근/보관 담당 확인 전 |
| 승인된 Backup S3/로컬 Recovery Storage | 암호화 Backup 원본과 보존 상태 | 김상희 Data/Recovery 경로 유지 |

GitOps 파일 자체를 포함한 Commit SHA를 그 파일에 넣으면 자기 참조로 Commit이 다시 바뀐다. 후보에는 Release ID와 이미 존재하는 Source/Artifact 개정을 두고, 실제 PR/검토/배포 GitOps Commit은 해당 Commit이 생긴 뒤 Docs 실행 기록에 연결한다. Config 개정은 논리 ID 또는 실제 GitOps Commit으로 연결하며 Secret은 개정 ID만 기록한다.

필드에는 schema_version·release_id·run_id·시험/하위 Case/Requirement·환경·App/Infra/GitOps 전체 SHA·Image Digest/플랫폼·Schema/Config/Secret 개정·Tool Manifest·Render/Recovery Bundle 개정·Backup ID/암호문 Hash/Data 기준 시각·실행 조건·UTC ISO/KST·실행자/Reviewer·Baseline/Target/Actual·판정/제한/후속 Run을 포함한다. Candidate, Render 후 검토, 실제 Deployed와 Acceptance 결과는 서로 구분하고 미실행 결과는 NOT RUN으로 둔다.

새 Backup마다 App Release를 변경할 필요는 없다. Backup 대장과 Recovery Bundle에서 해당 Release/Schema와의 호환을 연결하고 실제 복구 Run이 사용한 Backup ID를 고정한다. 실패 Run을 덮어쓰지 않고 후속 Run과 관계를 남긴다. State/Saved Plan·Credential·Secret 실제 값/평문 Hash·개인정보·평문 SQL/Backup 원본은 공개 파일에 넣지 않는다. 실제 보호 경로와 접근방법은 보호 운영 대장에 두고 Docs에는 공개 가능한 논리 ID만 연결한다.

### 5.5 확정된 복구 DB 전용 VM 배치

**상태는 CONFIRMED DECISION이다.** 2026-10-01 KST 사용자가 남은 두 구조 권고안에 동의해 새 전용 VM 배치 모델을 채택했다. 직접 TLS 연결·새 VM 생성 가능과 배치 모델은 각각 확인된 결정이며, 실제 Host·용량은 미확인 입력이다. 아래는 채택 전에 비교한 주요 대안이다.

| 대안 | 구현·복구 편익 | 의존성과 준비 부담 | 판단 |
|---|---|---|---|
| 새 전용 VM에 격리 MariaDB | 기존 VM/DB 운영 경험 활용, DB 기동·Import 진단을 App Cluster와 분리, 1차 DB 보호 경계를 설명하기 쉬움 | OS/DB/TLS/서비스·디스크 관리와 Host 실측 필요. 같은 Hypervisor/Storage 장애까지 독립적이라는 뜻은 아님 | 채택 |
| 로컬 Cluster의 격리 MariaDB StatefulSet | Recovery App과 함께 선언 관리 가능, 별도 DB OS 관리 축소 가능 | DB가 Cluster/CNI/Storage/PV 준비에 의존. 실제 DB Image·파일 권한·PV·재시작/복원 절차를 추가 확인 | 대안 |

**채택한 모델은 새 전용 VM의 격리 MariaDB다.** Recovery App은 직접 TLS 경로로 접속한다. 기존 1차 DB/MaxScale를 수정하지 않으며 이전·주기 Backup용 Data 작업 VM과 복구 DB VM은 서로 별도 VM으로 관리한다. 같은 물리 Host·Hypervisor·Storage를 공유하면 장애 영역이나 독립 사본의 독립성까지 보장하지 않으므로 I03/I05에서 확인한다. 실제 Host/이름/주소/DB 계정/CA/용량은 구현 입력으로 확보한다. 03 §3-D.10.5의 Data 작업 VM 초기 후보 2 vCPU·4 GiB·OS 40 GiB를 복구 DB 크기로 자동 복제하지 않는다.

| 결정 기록 | 내용 |
|---|---|
| Decision ID | PH2-04-RECOVERY-DB-DEDICATED-VM |
| 결정일과 승인 | 2026-10-01 KST. 사용자 남은 두 구조 권고안 모두 채택 |
| 근거 | 단일 DB 복원·RTO 30분 목표, 1차 보호, 새 VM 생성 가능. 현재 자원 여유는 예상이며 실측 전 |
| 책임 | 김상희 DB/Restore/용량, 이유빈 Host/Network 협업, 정태훈 Recovery 설정, 최유준 복구 시간선 |
| 확인 시점 | VM 생성/배치 전에 Host 실측과 Data Directory/디스크 확인, 예행 전에 TLS·CA·DB/Driver·Backup 검증 |
| 재검토 조건 | Host 여유 부족, 독립 보존/통신 실패, 복원 소요나 운영 부담이 목표를 위반 |
| 바뀌지 않는 기준 | Cloud RDS/Redis, 새 Recovery Redis, 직접 연결, 1차 보존, Backup 암호화와 Offline 사전 동기화 |

채택한 VM 모델 안에서 Host·용량을 조정하는 통상 구현을 매번 새 구조 선택으로 되돌리지 않는다. 격리·보존·예산·복구 목표를 바꾸는 제약이 발견될 때만 영향과 대안을 제시한다. VM 생성/Import/DB 연결 시험은 아직 실행하지 않았다.

### 5.6 확정된 비상 접속과 초기 관리자 회수

**상태는 CONFIRMED DECISION이다.** 2026-10-01 KST 사용자가 남은 두 구조 권고안에 동의해 유지 비상 관리자 하나와 초기 인증 명시 회수 모델을 채택했다. 정상 GitHub 프로젝트 Team IDP와 개인별 RBAC는 승인 기준을 유지한다. 아래는 외부 IDP 장애의 관리 경로와 초기 인증 종료를 비교한 기록이다.

| 대안 | 편익 | 의존성과 운영 부담 | 판단 |
|---|---|---|---|
| 프로젝트 정책상 htpasswd 비상 관리 계정 하나 유지 + 초기 관리자 명시 회수 | 정상 IDP 장애 중에도 Cluster API/OAuth가 살아 있으면 관리 경로를 확보할 수 있음 | 별도 비밀번호/보관·사용 사유·필요 권한·교체/회수 시험 필요 | 채택 |
| 상시 비상 계정 없이 필요할 때 ROSA 관리 경로로 관리자 생성 | 상시 Static Credential 보관 감소 | 장애 시 Red Hat/OCM 인증·권한과 ROSA 관리 API를 이용해 다시 생성해야 함. 그 경로도 불가하면 지연 | 대안 |

**채택한 모델은 유지 비상 계정 하나와 초기 Bootstrap 인증의 명시 회수 조합이다.** 초기 비밀번호를 그대로 영구 비상 값으로 넘기지 않는다. 실제 Classic/CLI 지원 방식에 맞춰 정상 개인 관리자 경로를 확인한 뒤 유지 비상 인증을 설정·검증하고 초기 인증을 회수한다. 동시에 두 htpasswd 사용자를 만들 수 있다고 전제하지 않으며 전환 순서는 실제 지원 범위에서 정한다. 마지막 유효 관리 경로를 검증 없이 제거하지 않는다.

[ROSA Classic 관리 접속](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/install_rosa_classic_clusters/rosa-sts-accessing-cluster)은 `rosa create admin`의 htpasswd 관리자 경로를 안내한다. [ROSA CLI](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/cli_tools/rosa-cli)의 `delete admin` 등 지원 회수 경로를 사용한다. 자동 만료를 전제하지 않으며 ROSA 관리자를 self-managed 설치의 kubeadmin으로 간주해 Secret 삭제 명령을 복제하지 않는다.

Classic IDP 설명의 단일 Static 관리 사용자 문구와 [공통 ROSA IDP 문서](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/authentication_and_authorization/sd-configuring-identity-providers)의 여러 htpasswd 사용자 절은 지원 표현이 다르다. 따라서 여기서 하나는 프로젝트 운영 정책이며 제품의 기술적 최대 사용자 수라는 주장이 아니다. 실제 Classic Cluster/ROSA CLI/OCM의 생성·전환·회수 지원을 구현 시 확인한다.

| 대상 | 운영 절차와 책임 | 검증 경계 |
|---|---|---|
| 정상 ROSA | 정태훈 설정, 이유빈 리뷰. 개인 GitHub 로그인·실제 Principal과 허용/금지 작업 확인 | Team Allowlist와 관리자 권한을 동일시하지 않음. OCM 관리 권한도 별도 확인 |
| 초기 ROSA 관리자 | 정태훈 초기 IDP/GitOps/RBAC 설정 후 정상 개인 관리 경로·비상 전환 확인, 초기 인증 회수. 이유빈 재검토 | 신규 로그인 거부, 높은 Binding 회수와 이미 발급된 Token/임시 kubeconfig 재접속을 구분 |
| 유지 ROSA 비상 관리 | Cloud Bootstrap 정태훈 주/이유빈 예비 보관. 사용 사유·실제 수행자·사용 Principal·범위·종료와 교체/회수 기록 | IDP/RBAC 복구에 필요한 최소 권한을 실제 확인. 일반 CI/일상 로그인에 사용하지 않음 |
| Argo 초기 admin | 정상 OpenShift SSO와 Argo의 별도 RBAC·관리자/제한 사용자 시험 뒤 Operator CR의 지원 설정으로 비활성화 | GitOps 1.21.4 실제 설치에서 설정/회수 확인. 상시 Argo 공용 비상 비밀번호를 추가하지 않고 ROSA 관리 경로의 CR 복구 가능성 시험 |
| On-Prem Offline 관리 | 김상희 주/최유준 예비 보관, 이유빈 Host 접속 협업. 필요한 로컬 SSH/Cluster 인증을 사전 보존·복원 검증 | AWS/GitHub 신규 조회 없는 관리 경로. Cloud 비상 값과 분리. 실제 접속 방식·유효기간·보호 경로는 입력 대장으로 인계 |

[GitOps 1.21 Dex/OpenShift OAuth](https://docs.redhat.com/en/documentation/red_hat_openshift_gitops/1.21/html/access_control_and_user_management/configuring-sso-for-argo-cd-using-dex)와 [Argo RBAC](https://docs.redhat.com/en/documentation/red_hat_openshift_gitops/1.21/html/access_control_and_user_management/configuring-argo-cd-rbac)는 인증과 Argo 권한 설정을 구분한다. OpenShift 개인 ClusterRoleBinding만으로 Argo 관리 권한이 자동 전달된다고 판단하지 않는다. Operator 소유 설정을 임의 ConfigMap/Secret 덮어쓰기로 계속 관리하지 않는다.

[ROSA OAuth Token 관리](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/authentication_and_authorization/managing-oauth-access-tokens)에 따르면 `oc logout`은 현재 Token을 무효화한다. 비밀번호 교체/IDP 삭제만으로 서로 다른 모든 기존 OAuth/Argo 세션이 즉시 종료된다고 기록하지 않는다. 초기 인증 정리에서는 새 로그인, 높은 권한, 관련 발급 Token과 Argo 세션을 각각 확인하고 남은 세션이나 회수 권한 부족은 미완료로 남긴다.

| 결정 기록 | 내용 |
|---|---|
| Decision ID | PH2-04-EMERGENCY-ACCESS-CLEANUP |
| 결정일과 승인 | 2026-10-01 KST. 사용자 남은 두 구조 권고안 모두 채택 |
| 결정 범위 | 정상 GitHub IDP 유지, Cloud 비상 관리 하나, 초기 ROSA/Argo 인증의 검증 후 회수, 독립 로컬 관리 경로 |
| 근거 | 외부 IDP 장애 대비와 초기 권한 종료, 이미 채택한 Cloud/Recovery 보관 책임 활용 |
| 영향 | Secret 범위와 Bootstrap/SSO/RBAC·T03·Clean Recreate·Offline Recovery 절차 |
| 미확인 | 실제 관리 권한·지원 버전·비상 인증 공급·전환·Token/세션 회수 결과 |
| 재검토 조건 | 실제 지원/권한/전환 실패, 보관·회수 부담, 정상 관리 경로 상실 또는 복구 목표 위반 |

htpasswd 경로는 Cluster API/OAuth 전체 장애나 AWS 전체 접근 불가를 해결하지 않는다. 이 관리 접속안의 적용 범위를 벗어난 장애에서는 사용자 업무 영향과 장애 범위를 판정하고, 서비스 복구가 필요한 경우 승인된 On-Prem Restore-based Recovery 절차로 연결한다. 사용자 설명의 계정 대여가 실제로 발생하면 §2.4대로 수행자/Principal을 남기며 설계 배정 변경이나 이미 허용된 협업의 재승인을 요구하지 않는다. 인증 값·Key 생성과 접속/회수 시험은 미실행이다.

## 6 작업별 구현 시작 조건

| 진입점 | 시작 전에 필요한 확인 | 이번 문서의 현재 판정 |
|---|---|---|
| 코드 작업 | 해당 Repo/Branch/권한/리뷰, 작성과 실행 Owner, Source/Seed와 Secret 경계 | 담당 확정, 실제 권한/Branch/Source 입력 확인 전 |
| 실제 base의 lab Argo | base/Overlay의 전체 Commit, 실제 Context/Namespace/Operator 책임, Secret/Registry, 단일 Owner와 삭제 보호 | 예제 Argo 동작은 추가 팀 보고 완료. 실제 base 인계/검증과 AI Runtime 확인은 미완료 |
| TF 정적/로컬 확인 | 검토할 Root 코드, 정확한 도구/Provider/Lock/Schema와 필요한 Module | 계정 전체 Preflight 완료를 선행하지 않음. 해당 코드/도구 준비 후 수행 |
| 실제 TF Plan | 해당 Root 코드/Provider/Lock, 실제 입력/Caller/Role/Backend와 보호된 Plan 저장 | Root 담당 확정, 실제 코드/계정/Backend 입력 확인 전 |
| 첫 Full Apply | 검토된 실제 Plan와 자원/삭제 범위, 계정/지원/Quota, Secret 초기화, 실제 가격/Credit/누적/Window/정리 비용 | NOT READY. 실제 Plan/비용과 실행 입력 미확인 |

실제 Plan과 일부 측정값은 코드 준비 이후에 생긴다. 04에서는 각 구현 단위의 시작 조건과 뒤 단계에서 확인할 조건을 정의하며, 아직 만들지 않은 Plan이나 시험 결과를 준비 완료의 증거로 사용하지 않는다. 진행 가능한 구현 단위만 인계하고 미해결 조건은 담당/확인 시점/막는 작업으로 유지한다.

[Terraform Validate 공식 범위](https://developer.hashicorp.com/terraform/cli/commands/validate)는 구문/내부 일관성을 확인하며 Remote State나 Provider API를 검증하지 않는다. 필요한 Provider/Module을 갖춘 별도 작업 사본의 로컬 확인을 실제 Backend/Caller 검증과 구분한다. 여기서 Controller의 기존 Backend/State 설정을 변경하거나 Terraform 명령을 실행한 것은 아니다.

## 7 확정 결정의 연쇄 영향과 검토

| 변경 | 직접 연결 | 후속 연결과 상태 |
|---|---|---|
| bootstrap/foundation 이유빈 실행 | 03 §3-F.2~5의 Root/Backend/Role와 입력 전달 | T02/T03/T19, W02/W03/W06/W08. 실행자 개인 인증과 실제 결과는 확인 전 |
| rosa 정태훈 실행 | foundation 제한 입력, ROSA Lifecycle, Bootstrap와 Secret/GitOps 인계 | T01/T02/T03/T19/T21, W03/W06/W08. 실제 지원/Plan/Cost는 확인 전 |
| foundation 영역별 작성 | Data/Registry의 원본 Owner와 Root 통합 | 김상희/최유준의 담당 영역 리뷰와 이유빈 전체 실행 연결. State 추가 없음 |
| base 정태훈, lab 최유준 | 03 §3-I.13의 11건, Image/Pull/CA/Job/Route/Probe | 기존 IF/T 대응과 W03/W06 연결. lab 결과를 ROSA PASS로 확대하지 않음 |
| Data 김상희, 시험 최유준 | Backup/Restore와 App 재개, 장애 주입 순서와 원시 결과 | T04/T05/T12/T13/T17/T18, W04/W06/W08. DB/Backup/RTO/RPO 실측 미실행 |
| Evidence 각자 작성, 최유준 Index | Code/Image/Manifest/Schema/Config/Secret 개정과 Run 연결 | JSON/Markdown/CSV·논리 경로 확정. 실제 원시 보호 자료 위치와 Run은 확인 전 |
| 격리 복구 DB 직접 연결 확정 | Recovery Endpoint/계정/CA와 App 설정, MaxScale 의존성 제외 | T04/T18/W04/W08, 전용 새 VM 모델 확정. 실제 Host/용량·배치 결과는 확인 전 |
| AWS Provider 6.67.0 초기 후보 확정 | 03 §3-F.14/B01의 AWS 후보를 최신 결정으로 연결 | 필요한 Root의 Schema/제약/Lock/도구 Manifest와 실제 TF 검증 연결. Core 등 다른 후보/Backend/State 변경과 전체 PASS는 포함하지 않음 |
| GitOps Writer PAT 확정 | 03 §3-C.12.4의 제한 후보와 3-F의 CI→PR→사람 Merge 흐름 | 무기한 우선/허용 최대 수명과 실제 Org 정책·발급자·Job 경계를 연결. Writer 인증은 Argo Reader와 분리. 실제 발급/등록/시험은 미실행 |
| Secret 주/예비 보관자 확정 | Cloud/CI/Backup/Recovery/Backup 개인 Key의 수신자·원본/예비본 | 03 §3-C.12와 T03·Offline Restore 인계. 계정 대여 설명으로 전체 Key 수신자를 확대하지 않음. 실제 보관/복원은 확인 전 |
| PR #11 Source 정합 | 새 경로/key·정확 버전·입력 전달 README, 팀의 이전/No changes 보고 | I02/Root·T02/T03/T19에 연결. TF Role/MFA·각 clone·State 이력/복원·다른 Root 구현은 후속. 기존03 보존 |
| 추가 demo2 A/B/C 보고 | 예제 Argo·Native/UWM·알림/정책과 최유준 수행 범위, 부분 정리·잔존 | T03/T04/T11/T14/T15/T19/T21·W03/W04/W05/W08. 실제 base/ROSA·원시 Log/Manifest·권한/Token 회수는 미확인. 기존 Cloud 후보/Prune/Grafana 경계 유지 |
| 두 구조 결정 사용자 확정 | §5.5 복구 DB 전용 VM, §5.6 비상 경로와 초기 인증 회수 | I03/I05/I06·Secret/Runbook/T03/T04/T18/W04/W08로 연결. 모델은 확정이며 실제 자산·지원·전환·회수·복구 결과는 각 실행 Gate에서 확인 |
| 공동 참여/계정 사용 설명 | 배정 책임·실제 수행자·관측 Principal·계정 관리 책임과 협업 내용 구분 | Run/기여 기록과 권한 시험 판정에 연결. 구체 Run의 수행/실효 분리는 아직 증거 없음 |

이번 문서 검토에서는 사용자 채택 범위, 00의 팀 초안, 03의 Root/Ownership·관리 장애와 업무 장애·RTO/RPO, 실제 수행 이력, 담당/리뷰 표, 두 구조 결정과 입력/Runbook/문서 종료 조건을 대조했다. 역할 확정이 실제 권한/도구/Branch/Seed/과거 수행자 확인으로 확대되지 않도록 구분했다. 복구 직접 연결 확정과 새 VM 생성 가능/자원 여유 예상도 서로 다른 상태로 관리한다. AI는 실제 HCL/Manifest 작성, 계정 변경, GitHub 쓰기, Apply, DB 복원이나 시험을 수행하지 않았다. 팀의 기존 코드/실행 보고는 다음 절에서 별도로 대조한다.

## 8 추가 자료와 선행 Source 대조

### 8.1 자료 분류와 조회 범위

2026-10-01 사용자가 팀의 개인 Linux/IAM 자격증명 등록과 bootstrap init/plan 공지를 제공했다. 공지는 TEAM PROVIDED 운영 안내이고 NoCredentials 사례는 팀 수행 보고다. 공지를 계정/Backend/모든 역할 검증 완료로 처리하지 않는다.

04에 포함하는 근거는 자료의 제공 시점이 아니라 실제 실행 준비에 미치는 영향이다. 개인 인증과 Backend 접근은 Terraform 시작 입력이고, 기존 Lock/State와 승인 기준의 차이는 Root 인계 조건과 보완 책임에 연결된다. 따라서 공지 전문을 수록하는 대신 실행에 필요한 확인 사실, 보고의 범위, 차이와 담당을 추출해 기록한다. 설계 기준은 승인된 03과 최신 사용자 결정으로 유지한다.

이후 [Infra README](https://github.com/seokpan/seokpan-hybrid-infra/blob/b1aeaad678a22b7339e0cdceae992a91349e8d5c/README.md), 같은 Commit의 Tree와 bootstrap main.tf/backend.tf/.terraform.lock.hcl, [Issue #5](https://github.com/seokpan/seokpan-hybrid-infra/issues/5)의 본문과 결과 코멘트 두 개를 읽었다. Source 기준 Commit은 `b1aeaad678a22b7339e0cdceae992a91349e8d5c`다. 실제 controller/AWS/State에는 접속하지 않았다. 제공 공지나 Repo의 Account ID/접속정보/Key를 문서로 복제하지 않는다.

| 자료 | 확인한 사실과 한계 |
|---|---|
| 실제 Repo Tree | bootstrap/에는 main.tf/backend.tf/Lock 파일 존재. terraform/foundation과 terraform/rosa는 README만 존재. 코드 존재가 Runtime 완료는 아님 |
| bootstrap Source | S3 Backend, Versioning, SSE-S3, Public Access Block, 비TLS 요청 거부 정책과 use_lockfile 코드 확인. 해당 Source에는 목적별 TF 실행 Role Resource가 없음. 실제 Role 존재 여부는 미조회 |
| 버전 Source | Terraform required_version는 ~>1.16.0, AWS Provider 제약은 ~>6.0, Lock은 6.67.0. Controller의 실제 Terraform Core 값은 미확인 |
| Issue #5 중간 코멘트 | 팀원 네 IAM User에 AdministratorAccess가 연결됐다고 보고. 추가 Backend 정책 불필요/remote_state 접근 가능이라는 작성자의 판단은 목적별 Role와 제한 입력 설계의 검증을 대신하지 않음 |
| Issue #5 최종 코멘트 | 작성자 외 팀원의 개인 Linux/IAM 조합에서 Caller, init, Provider 6.67.0과 No changes를 보고. 처음 NoCredentials였고 aws configure 후 성공했다고 보고. 다른 모든 팀원/Root의 실동작 결과는 아님 |

해당 Issue는 closed였으나, 04의 실효 권한/다른 Key 접근 차단/Role별 실행/전체 재현성 시험을 완료 처리하지 않는다. 공식 시험 T는 기존 NOT RUN 상태를 유지하고, 해당 bootstrap 사전 결과를 별도 팀 보고로 연결한다.

### 8.2 공지의 활용과 보완

| 공지 내용 | 적용과 보완 |
|---|---|
| 본인 Linux 계정, su -, OS root Terraform 금지 | 공유 Controller의 작업 규칙과 일치. OS 로그인과 AWS Caller/Role 확인을 별도로 수행 |
| 개인 ~/.aws와 aws configure | 개인 원천 인증 등록으로 활용. MFA→목적별 STS Role과 최초 Bootstrap의 인증 예외를 대체하지 않음 |
| IAM User ARN만 정상 예시 | 원천 개인 Profile 확인에서는 활용 가능. 정상 Role Profile은 assumed-role 신원이므로 Account/Source/목적 Role/MFA 세션을 구분 |
| GetCallerIdentity 성공 | 신원 확인이며 서비스 권한 PASS가 아님. 실제 Backend/Provider Profile, 환경변수 우선순위와 Account/Region을 각각 대조 |
| ~/.aws 경로와 chmod700 | 기본 경로 설명이며 다른 Profile/환경변수/파일 경로가 실제 선택을 바꿀 수 있음. 디렉터리 외 소유자/credentials/config 파일 접근 제한도 확인 |
| bootstrap init/plan No changes | 해당 Commit/Root/Backend/입력/인증 조합의 변경 제안 없음. 목적 Role, foundation/rosa, 모든 IAM/S3 동작, 복구/Cost 전체 PASS가 아님 |
| Apply/Destroy 금지 | 이번 공지의 확인 범위에서 유지. State 이전, Backend 변경, init-upgrade를 인증 확인에 추가하지 않음 |
| 공유 Controller 전체 dnf update 금지 | 팀의 버전 고정 규칙으로 유지. 개별 패키지도 설치 전 실제 버전과 의존 영향 확인 |
| 버전 변경이면 State를 되돌릴 수 없음 | 일반 사실로 단정하지 않음. 새 기능/State 형식을 구버전이 읽지 못할 수 있어 Downgrade가 보장되지 않는다는 의미로 정리 |
| 성공/실패만 공유 | 비밀값 노출 방지 의도는 유지. 별도 비민감 Index에는 작업자/시각/Commit/Root/도구/인증 Profile 참조/검증 범위와 결과를 연결 |

공식 확인은 [AWS Role와 MFA](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-role.html), [GetCallerIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html), [AWS CLI 인증 우선순위](https://docs.aws.amazon.com/cli/latest/topic/config-vars.html), [S3 Backend](https://developer.hashicorp.com/terraform/language/backend/s3), [Plan 범위](https://developer.hashicorp.com/terraform/cli/commands/plan), [Terraform v1.x 호환성](https://developer.hashicorp.com/terraform/language/v1-compatibility-promises)을 2026-10-01 읽어 대조했다. 수정된 공지를 팀에 전송하거나 실제 인증을 등록한 것은 아니다.

### 8.3 최초 차이와 후속 Source 정합 상태

최초 대조는 Infra `b1aeaad678a22b7339e0cdceae992a91349e8d5c` 기준이었다. 이후 PR #11의 merge와 `fbc502d3b2de7b6794d7b9d2fd5bbcd376fb9041` Source를 읽어 해소된 차이를 갱신했다. 최초 발견을 삭제하거나 여전히 전부 미해소라고 반복하지 않으며, 실제 State/Caller/개인 작업 사본 확인은 Source 정합과 구분한다. 상세 이전 보고와 현물 인계는 §8.6에 기록한다.

| 최초 발견 | 후속 Source 정합 | 남은 책임과 확인 조건 |
|---|---|---|
| 개인 인증 직접 사용과 TF Role 부재 | PR #11은 TF Role을 추가하지 않음. README/Issue #10은 MFA 등록 뒤 PR B로 별도 구현 예정 | 이유빈 작성/실행, 정태훈 리뷰. Trust/MFA/목적 Role·Backend/Provider Caller와 제한 Key/Lock 시험. Human Admin 승인 기준 유지 |
| bootstrap 경로와 짧은 State Key | `terraform/bootstrap/`와 `phase2/bootstrap/terraform.tfstate`로 Source 정합. 구 key 정리·새 key No changes는 팀 보고 | 이유빈 Root 인계. 실제 각 clone의 새 경로/key·Workspace·Caller와 보호 State 이전 기록·Lineage/Serial 차이·복원 참조 확인 |
| Core/AWS 범위 제약과 후보 차이 | bootstrap Core `1.16.4`, AWS `6.67.0` 정확 제약과 Lock `version/constraints=6.67.0` 확인. AWS 후보는 이미 사용자 채택 | 이유빈/정태훈이 다른 Root 구현 시 정확 제약/Lock/Manifest 연결. 팀의 게시된 1.16.4 실행 결과와 실제 Controller/개인 사본을 구분 |
| State 간 광역 remote_state 인계 제안 | README가 필요한 비밀값 아닌 Output만 보호 입력 파일로 전달하도록 정합 | 이유빈/정태훈이 추출/소비 검사 구현. foundation/rosa는 README만 있으며 실제 입력 추출/검사/Root HCL은 아직 없음 |
| README 기준 문서 누락 | 03을 Source of Truth에 추가하고 Root/State/Ownership/Cost 설명 갱신 | 새 04 결정과 실행 Ledger 인계. README 갱신만으로 해당 Resource 구현 완료를 판단하지 않음 |
| 리뷰 Plan 자료와 보호 규칙 | 공개 Plan 요약/보호 원본 구분은 실행 절차에서 확인 필요 | 비민감 변경 요약만 공개. Raw Saved Plan/State는 보호 경로로 유지/처리하고 공개 첨부하지 않음 |
| Backend 복구 예시의 한계 | 경로 표기는 갱신됐지만 Local 전환/버킷 재생성 예시 유지 | 이유빈 실제 State 사본/Version·Lineage/Serial·자원 검증을 포함한 복구 인계. 버킷 재생성만으로 이전 State가 돌아오지 않음 |
| Milestone 10/18과 승인 Freeze 10/16 차이 | PR #11의 구조 정렬로 일정 차이까지 해소된 것은 아님 | 승인 10/16 유지. 이유빈/최유준이 가용일/WBS 정합화. GitHub 일정 변경은 수행하지 않음 |

Source 정합 완료와 TF Role/State 복원/개인 작업 사본/실제 Plan·Apply 준비는 별도로 판정한다. 팀원이 수행했다고 보고한 변경을 이번 AI 실행으로 기록하지 않는다.

### 8.4 확정된 AWS Provider 초기 후보 조정

**상태는 CONFIRMED DECISION이다.** 2026-10-01 사용자가 AWS Provider 초기 후보 권고안을 채택했다. 현재 Source는 AWS Provider 6.67.0을 고정했고 팀원 bootstrap 성공 보고가 있다. [공식 6.67.0 Release](https://github.com/hashicorp/terraform-provider-aws/releases/tag/v6.67.0)의 공개와 변경 설명도 대조했다. 이 결정은 초기 검증 후보의 조정이며 프로젝트 전체 안정성과 모든 Resource 조합의 검증 완료를 뜻하지 않는다.

| 결정 기록 | 내용 |
|---|---|
| Decision ID | PH2-04-AWS-PROVIDER-6-67 |
| 결정일과 승인 | 2026-10-01 KST. 사용자 "AWS Provider 초기 후보는 권고안을 채택할게" |
| 결정 | hashicorp/aws 초기 검증 후보를 6.66.0에서 6.67.0으로 조정. 필요한 Root의 정확한 제약, 각각의 Lock와 도구 Manifest에 연결 |
| 근거 | 현재 bootstrap Lock와 팀의 선행 보고 조합을 보존하고 초기 구현 후보를 정합화. 신규 Release라는 이유만으로 최신값을 추종하지 않음 |
| 범위 | AWS Provider 후보만 변경. Core 1.16.4, RHCS 1.7.7, ROSA/GitOps의 승인 후보와 기존 Backend/State는 유지 |
| 책임과 영향 | 이유빈 Infra 고정 작성, 정태훈 리뷰와 rosa 조합 대조. 각 영역 담당이 관련 Schema/Plan 검토, 최유준 시험/도구 Evidence Index 연결 |
| 미확인 | Controller 실제 Core, 필요한 Root의 HCL/Schema/Lock/Plan, 통합/재생성 결과. 팀의 bootstrap 보고 외 AI Runtime 실행 없음 |
| 재검토 조건 | 실제 Schema/지원 충돌, 회귀 또는 재생성 실패, 계정/Region 제약과 시간/비용 영향 |
| 기준 연결 | 완료된 03 원문은 보존하고 이번 사용자 결정과 이 04 기록을 AWS 후보의 최신 기준으로 적용 |

| 대안 | 편익 | 부담과 한계 |
|---|---|---|
| 6.66.0 후보 유지, 기존 bootstrap의 6.67.0과 구분 | 기존 승인 후보 유지 | Root별 다른 Provider 조합 관리. 이미 작성된 State를 무조건 Downgrade하지 않고 호환/재검증 필요 |
| 6.67.0을 AWS Provider 초기 후보로 조정 | 현재 Lock와 bootstrap 보고 조합을 이어가며 초기 구현 버전을 통일하기 쉬움 | foundation/rosa 지원 Schema/Lock/실제 Plan과 통합/재생성 시험은 새로 확인 필요 |
| Root별 최종 검증까지 후보 조정 보류 | 추가 실제 조합 근거를 모을 수 있음 | 구현 팀이 어느 초기 버전으로 준비할지 혼선과 대기 발생 가능 |

위 대안을 비교한 뒤 6.67.0 후보 조정안을 채택했다. 기존 bootstrap Source와 보고 조합을 보존해 불필요한 Downgrade를 피하고, 각 필요한 Root에서 실제 조합을 검증한다. 이번 AI가 코드/도구/Lock을 변경한 것은 아니다. 후속 PR #11의 bootstrap 정확 제약/Lock 변경은 Source에서 확인됐으며, 다른 Root의 구현과 실제 실행 검증은 계속 연결해야 한다.

### 8.5 추가 demo2 관측·Argo·NetworkPolicy 검증 보고

**자료 분류는 팀원이 수행한 OBSERVED EVIDENCE의 보고다.** 2026-10-01 사용자가 참고용으로 제공한 `OCP 실습 서버(demo2) 2차 사전 검증 작업 보고 - 2026/10/01` 원문을 읽었다. 보고는 최유준을 작업자로, 16:04~18:30 KST를 작업 시각으로 명시한다. 환경은 OCP 4.20.0, master 3/worker 2, GitOps Operator 1.22.0/Argo 3.5.3으로 보고됐다. 로그 08~33과 Manifest는 별도 보관 중이라는 설명이며 AI가 해당 원시 Log/Manifest나 Runtime을 조회한 것은 아니다. 원본 보고를 수정하지 않고 현재 판단에 필요한 결과와 인계만 반영한다.

이 보고의 작업자 확인은 이번 A/B/C 범위에 적용한다. 기존 Issue #1의 9항목/11건과 원래 미커밋 Overlay 작성자까지 모두 최유준으로 소급 확정하지 않는다. 사용 계정은 Token 계정이었다가 보호 kubeconfig로 교체했다는 보고이므로 실제 Principal·Token 회수와 파일 정리는 별도 검증 항목이다. 계정 관리/공유와 실제 수행자 기록은 §2.4에 연결한다. 접속 경로나 kubeconfig 값은 공개 문서에 복제하지 않는다.

| 보고된 완료 범위 | 이번 반영 | 아직 필요한 검증 |
|---|---|---|
| A Native/UWM | backend 메트릭 수집, ServiceMonitor Target Up, 시험 Rule firing/resolved, PodNotReady/PodPending 알림 보고 | 실제 base의 선택/라벨/권한·운영 Rule/부하·ROSA에서 재확인. 콘솔 p95 0.005초는 해당 조건의 보고 수치이며 60명/30분 HTTP·WS 목표 달성 증거가 아님 |
| B Argo 공개 예제 | managed-by 전후 권한, Sync/Prune/SelfHeal/cascade 동작 보고. 예제는 short Commit과 Image 대체 조건을 기록 | 실제 hybrid-gitops base 전체 SHA/Render·Owner·Secret 공급·삭제 보호·Cloud 후보 버전 검증. 예제 통과를 실제 App/ROSA Acceptance로 확대하지 않음 |
| C 알림/NetworkPolicy/콘솔 | UWM 전용 Alertmanager·프로젝트 AlertmanagerConfig→내부 webhook, Ingress Default Deny의 05/10/20/30 허용 단계와 화면 확인 보고 | 실제 Namespace/Pod/Port 선택과 신규 연결·재시작·양 Router 경로, ROSA LoadBalancer/Route 경로. 메일/Resend는 제외된 후속 검증 |

보고의 GitOps 1.22.0/Argo 3.5.3은 실습 조합이다. 승인된 GitOps 1.21.4 초기 후보와 Cloud 규모·Argo 자동 Prune 보류를 바꾸지 않는다. 공개 예제의 Prune/cascade 결과는 삭제 위험과 권한 경계를 검증할 근거이며 운영 기능을 자동 활성화하는 승인이 아니다.

| 발견·차이 | 직접 영향과 구현 인계 | 담당·시험/WBS |
|---|---|---|
| UWM 우선순위와 Redis 선점/약 15분 Backend Not Ready | Cloud worker 산정에 UWM/플랫폼 requests와 App 3 Replica·실제 사용량을 함께 반영. 실습 master 배치는 우회 조건으로만 남김. Redis 256Mi는 lab 변경이며 Cloud ElastiCache 크기나 정상 App requests의 새 기준이 아님 | 최유준 관측/측정, 정태훈 App/ROSA, 이유빈 자원/Cost. T11/T15·W03/W05/W08 |
| requests/limits 미설정과 리소스 위험 | 실제 Admit된 Pod의 전체 Container/QoS/Priority/LimitRange 확인. Scheduler 선점과 메모리 압박 Eviction을 구분하고 App/DB/Redis 설정을 실사용/부하로 검증 | 정태훈 base, 최유준 측정, 김상희 lab Data. T11/T15/T18 |
| ServiceMonitor/Rule/AlertmanagerConfig | 서비스/수집 대상과 Selector·Namespace·Port, Rule scope와 receiver·업무 Metric의 Probe 제외 조건을 확인. PodNotReady/Pending의 사용자 관측 공백 대응을 base로 인계. 1차 관측 Manifest를 무조건 그대로 이관하지 않음 | 최유준 작성/관측, 정태훈 base 통합. T15·W03/W06 |
| Argo managed-by와 넓은 권한 | 라벨·실제 Role/Binding·Controller SA Rule를 보존/리뷰하고 대상 Namespace를 제한. Secret/exec/RoleBinding/Project 삭제 가능성은 실제 실효 권한으로 검증. App 소유권과 Secret 별도 공급 경계 연결 | 정태훈 GitOps, 최유준 lab, 이유빈 기반 리뷰. T03/T19·W03/W04 |
| Prune/SelfHeal/cascade | 임시 예제에서 삭제 동작을 확인한 보고. 운영은 자동 Prune 보류 유지, 수동 삭제/Finalizer·연쇄 삭제·비밀값 공급 전 Sync 보류 Case를 인계 | 정태훈/최유준. T03/T19·W04/W08 |
| restricted-v2 예제 실패와 Image 대체 | 실제 FE/BE/Redis/Job의 UID/파일·Port 계약/이미지를 검증. 예제 Image 교체만으로 App 전체 SCC 통과를 판단하지 않음 | 정태훈 Source/base, 최유준 Image. T01/T03/T21 |
| Ingress Default Deny와 기존/새 연결 | Ready/기존 연결만으로 판정하지 않고 신규 연결·Consumer 재시작·허용/거부를 함께 측정. 05/10/20/30 번호는 이번 시험의 식별자. 05는 내부 webhook Pod가 있을 때의 조건부 규칙이고, 10의 Namespace 전체 허용은 실제 서비스별 Pod/Port 계약과 비교. 모든 Pod/Port 허용을 정당화하지 않음. Egress/TLS/DB 접근은 별도 Case | 이유빈 Network, 정태훈 base, 최유준 시험. T03/T04/T14/T15 |
| Router의 Node별 결과 | HostNetwork/OVN의 실습 경로와 ROSA 실제 Ingress 경로를 분리. actual Router Namespace 라벨·Endpoint·Source/Port를 확인하고 정책을 최소 범위로 구성 | 이유빈/정태훈, 최유준 재현. T04/T14 |
| Service 재생성으로 ClusterIP 변경 | 기존 lab hostAliases/IP 고정의 취약성 확인. App DB/Redis Host의 환경별 설정·DNS/CA/Hostname 계약을 실제 Source와 연결 | 정태훈 App, 김상희 Data/TLS. T04/T18/T19 |
| 초기 Token/보호 kubeconfig 변경과 회수 대기 | 서버 Token 폐기 결과·실제 Principal·기존 세션·임시 파일 정리를 확인. 높은 계정 사용 결과를 제한 Role PASS로 바꾸지 않음. §5.6 회수 Runbook의 실습 사례로 연결 | 최유준 실습 결과/보호 대장, 정태훈 플랫폼, 이유빈 리뷰. T03 |
| history/실행 실패 후 진행 | 자동 Sync의 history 차이는 해당 버전/설정 보고로 남김. 실제 배포 SHA/Run을 별도 고정하고 Git revert도 Schema/Secret 호환을 검토. Bootstrap 자동화는 실패 시 후속 적용 중단·부분 상태를 기록 | 정태훈 배포/Bootstrap, 최유준 Run. T10 선택 Case/T19 |

[Kubernetes NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/)는 정책 변경이 기존 연결을 종료하는지는 구현별 동작으로 설명한다. 이 실습에서 연결이 유지됐다는 결과를 모든 CNI의 불변 규칙으로 일반화하지 않는다. [Pod QoS](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/)는 CPU/메모리 requests/limits와 실제 Pod 구성을 기준으로 하며 [Pod Priority/Preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/)과 [Node-pressure Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/)은 별도 판단이다. 모든 BestEffort Pod가 조건에 관계없이 언제나 먼저 제거된다고 단정하지 않는다. 최신 Kubernetes의 추가 기능을 OCP 4.20 지원 확인 없이 도입하지 않는다.

보고의 `managed-by=NS admin`, 사용자 Rule의 Namespace 자동 범위, `release` 라벨 제거와 UWM ConfigMap 적용 방식은 실제 Operator 버전/설치 설정에서 검증할 항목이다. 단일 라벨이 언제나 같은 Role Rule를 만든다거나 모든 ServiceMonitor가 추가 라벨을 금지한다는 일반 결론으로 옮기지 않는다. 원시 Manifest/Role/설정의 출처와 전체 Commit을 받은 뒤 base의 정확한 변경을 결정한다. `up=0`/BackendDown은 수집 경로 차단으로도 발생할 수 있어 프로세스 중지와 Scrape 불가 원인을 구분한다. 새 TCP/WS·Consumer 재시작·같은/다른 Node·수집/알림을 별도 조건으로 확인한다.

**18:27 최종 점검의 정리 상태도 팀 보고 시점으로 기록한다.** UWM 시험 설정은 비활성화/ConfigMap 삭제했다고 보고됐으나 전체 실습 자원이 사라진 상태는 아니다.

| 남은 상태의 보고 | 후속 처리와 책임 |
|---|---|
| seokpan-app App/대역 DB/Redis Ready, frontend 200/api 401 | 정태훈/최유준이 실제 base 검증과 인계 문서 8단계 정리를 조율. 단순 HTTP 응답은 대표 업무/Data 검증 전체를 뜻하지 않음 |
| Redis requests 256Mi와 Overlay 반영 | 최유준이 실제 변경본/전체 Commit 인계, 정태훈 lab Overlay 통합. PVC 유지 보고만으로 진행 게임/Redis Runtime·DB 데이터 무손실을 증명하지 않음 |
| seokpan-argotest 빈 Project와 managed-by | 최유준 실제 base 시험에서 재사용, 이후 라벨/Role/Binding/Finalizer/잔존 결과까지 확인 |
| GitOps Operator 설치 유지 | 공유 환경 담당자와 필요 범위/정리 시점 확인 후 처리. AI가 삭제/공지하지 않음 |
| Token 폐기, Issue 3건 결과 등록/Close와 공유 공지 미완료 | 최유준 후속 확인 책임. 이번 접수로 해당 외부 쓰기/전송을 대신 수행하거나 완료로 기록하지 않음 |

메일/Resend는 보고자의 후속 제안이며 이번 접수만으로 서비스 선택이나 수신 PASS가 확정되지 않는다. 최유준은 실제 알림 요구·기존 서비스 계약/비용·receiver/Secret·Egress 조건을 확보해 필요한 ROSA 수신 시험으로 인계한다. 김상희는 비민감 GRANT 제공/임시 권한 교체와 정태훈의 Backend 재검증을 연결한다. 추가 보고의 Grafana 논의는 관측 화면 요구의 참고 사항이며, 이미 승인된 Cloud Native/UWM와 1차/복구 Grafana 보존 기준을 다시 후보로 되돌리지 않는다. Cloud Grafana를 새로 추가해야 하는 실제 요구가 확인되면 범위/비용/일정 영향을 별도로 비교한다. 이것을 이번 04 문서 종료의 세 번째 구조 Blocker로 만들지 않는다.

### 8.6 PR #11 구조 정렬·State 이전 공지 대조

추가 공지는 **팀의 변경 완료/운영 조건 보고**다. [PR #11](https://github.com/seokpan/seokpan-hybrid-infra/pull/11)은 2026-10-01 18:48:40 KST merge 상태로 조회됐으며, 후속 조회 당시 main도 merge Commit `fbc502d3b2de7b6794d7b9d2fd5bbcd376fb9041`였다. 해당 Tree·README·bootstrap main/backend/Lock을 읽어 아래 정합을 확인했다. Source의 관리 대상 AWS Resource 정의 변경은 없지만 State 객체의 복사/삭제는 별도의 변경 작업으로 보고됐다. AWS Runtime에서 모든 변경 여부를 AI가 직접 확인한 것은 아니다.

| 항목 | Source/팀 보고의 확인 범위 | 남은 실행 인계 |
|---|---|---|
| Root 경로 | 실제 Tree에 `terraform/bootstrap/`, `terraform/foundation/README.md`, `terraform/rosa/README.md` 확인 | 새 경로를 기준으로 코드/인계. foundation/rosa Root HCL·계정/자원 구현은 아직 없음 |
| Backend | bootstrap의 `phase2/bootstrap/terraform.tfstate`, 서울, encrypt/use_lockfile 유지 확인 | 지정 정본/key·Workspace/Caller·Lock/복구 참조를 각 실행 사본에서 확인 |
| 정확 버전 | Core 1.16.4/AWS 6.67.0 제약, Lock의 version/constraints 6.67.0 확인 | Controller 공용 설치/개인 호출 바이너리 확인. 버전 불일치를 개인 임의 설치/전체 업데이트로 해결하지 않음 |
| 입력/기준 문서 | README의 03 기준·Root Ownership·제한된 비밀값 아닌 Output 파일 전달 정합 | 실제 추출/소비 코드·입력 개정/Account/Region/생성 시각 검사 구현은 후속 |
| 팀 Runtime 보고 | [PR 검증 댓글](https://github.com/seokpan/seokpan-hybrid-infra/pull/11#issuecomment-5928927573)의 Core/Provider/init/No changes 출력, [Issue #10 후속](https://github.com/seokpan/seokpan-hybrid-infra/issues/10#issuecomment-5928992867)의 정규화 State 비교·구 key 삭제·잔여 Lock 없음·버저닝 보존 보고 | 해당 Root/조합 보고이며 네 사람/목적 Role/다른 Root/복원·동시 실행/Cost 전체 PASS가 아님. 실제 보호 State/Version/독립 사본과 재접속 결과 확인 |
| Bootstrap apply 중지 해제 | 사용자 제공 공지는 일시 중지 해제와 지정 담당자만 apply 조건을 명시 | 기존 승인 Root 실행자 이유빈과 리뷰/Plan/Lock 인계 유지. 일반 팀원의 확인 절차는 init/plan이며 destroy 또는 Full Apply 준비 완료로 확대하지 않음 |

**State 내용 비교와 식별정보의 차이를 함께 인계한다.** Issue #10은 구 Serial 2/새 Serial 1과 서로 다른 Lineage를 보고했다. 비교한 `version/terraform_version/outputs/resources`는 동일하고 새 key의 Plan은 No changes였다는 보고다. 이는 선택된 내용과 Plan 정합의 근거이며 전체 State 바이트/모든 메타데이터/이력 보존의 동일성을 뜻하지 않는다. 구 key는 삭제됐고 버저닝으로 이전 버전을 보존했다는 설명은 실제 Version ID·읽기/독립 사본/복원 시험과 별개다.

보고가 제시한 빈 새 key에서의 Lineage 재발급/Serial 초기화 원인은 아직 확인되지 않았다. [공식 현재 State Migration Source](https://github.com/hashicorp/terraform/blob/main/internal/command/meta_backend_migrate.go)는 가능한 경우 Lineage/Serial 보존 처리를 설명한다. 정확한 1.16.4 실행 조건/원시 이전 State/Backend·Workspace·명령 순서는 아직 재현 확인하지 않았으므로 이번 차이의 원인을 일반 동작이나 특정 버전 버그로 확정하지 않는다. 이유빈은 보호 이전 기록과 식별정보 차이를 인계하고 필요한 원인 확인을 진행한다. 이 발견만으로 삭제된 구 key를 되살리거나 정본 State를 임의 편집/재이전하지 않는다.

[Terraform init 공식 범위](https://developer.hashicorp.com/terraform/cli/commands/init)에 따르면 `-migrate-state`는 기존 State의 복사를 시도하고 `-reconfigure`는 기존 설정을 재구성하며 State 이전을 하지 않는다. 따라서 팀의 이전 완료 정본에 연결하는 각 clone은 새 Root에서 init/reconfigure와 Plan을 확인하는 흐름으로 인계한다. 새 State 이전을 팀원마다 반복하지 않는다.

구 `bootstrap/` 삭제 안내는 각 사본의 내용 보존 확인을 앞에 연결한다. 미커밋 변경·Git에 무시된 입력/Local State/Backup/Plan·사용자 자료가 없는지 확인해 필요한 보호 자료를 옮기고, 확인된 잔여 캐시만 정리하거나 구 폴더를 격리한다. git status만으로 ignored 파일까지 없는 것으로 판단하지 않는다. 과거 Root에서는 Plan/Apply를 이어가지 않으며, 새 Root에서 예상과 다른 Create/Destroy/Replace가 제안되면 Apply 없이 Root/정본/Caller와 입력을 확인한다.

실제 TF Role/MFA AssumeRole은 PR B의 남은 범위다. Source 정합과 Bootstrap 성공 보고를 해당 Role 정책·Trust/MFA·Key별 거부/Lock 시험 완료로 바꾸지 않는다. 이번 공지를 팀에 재전송하거나 git pull/폴더 삭제/init/plan/apply/State 조작을 AI가 실행한 것은 아니다. 완료된03은 보존하고 최신 AWS 후보/Source 변경은 04 결정·실행 인계에서 연결한다.

## 9 실행 인계와 WBS 구체화

이 절은 승인된 W01~W10을 현재 사람 배정과 실제 입력에 연결한 준비 계획이다. W02 전체 완료를 모든 W03 작업의 일괄 선행으로 해석하지 않는다. 해당 영역의 입력과 Repo/Owner가 확보되면 독립 준비를 진행하고 공유 실행은 Root/자원 인계 순서로 조율한다. 코드 작성/실행·소요시간·가용일을 완료한 것으로 기록하지 않는다.

| 작업 | 담당과 리뷰 | 지금 진행할 준비 | 실제 다음 단계의 입력과 인계 |
|---|---|---|---|
| W01 03 종료 | 완료 | 승인 기준과 새 04 결정의 연결 유지 | 실제 미확인 입력은 W02로 인계 |
| W02-A Infra | 이유빈, 정태훈 rosa 리뷰 | Root/Role/Output·버전·Backend/State 차이와 필요한 자원 목록 | Controller 도구·Caller/Role·State 참조·지원/Quota 확인 후 해당 Root 코드/Plan 준비 |
| W02-B App/base | 정태훈, 최유준/김상희 리뷰 | Source 변경 요구·공통 base/Overlay·11건 대응과 Case 준비 | 최신 Source/Seed 근거·미반영 변경·lab Overlay/작성자/Commit/Digest를 W03에 인계 |
| W02-C Data/Recovery | 김상희, 정태훈 리뷰, 이유빈 Host 협업 | 목적별 DB 권한/TLS·직접 연결·Backup/Restore와 Bundle 절차 | 비민감 GRANT/Schema·Dump 규모·Host 실측·독립 Storage/Harbor/CA 확보 후 코드/격리 예행 |
| W02-D CI/lab/Evidence | 최유준, 정태훈 리뷰 | PAT 권한/수명 기준·ECR/Harbor·Release/시험/Index 준비 | Jenkins Job/Agent/Plugin/Scan·Org PAT 정책/Repo 보호·lab Context/Namespace와 원본 인계 |
| W03 영역별 코드 | 확정된 네 담당자 병행, Root별 실행 책임 유지 | 각 영역의 입력 충족 후 HCL/App/base/Pipeline 작성과 로컬 확인 | fmt/validate·Render·CI Build/Test/Scan·Output 전달 검토. 실제 Plan은 계정/Backend/Caller 입력 후 |
| W04 로컬 예행 | 김상희 복구, 최유준 Harness/lab, 정태훈 App | 확보된 독립 자산부터 Restore·Bundle·업무 Harness/lab 계획 실행 | 격리 VM/Storage·검증 Image/Backup·Secret 공급과 고정 Commit 필요. lab 결과와 ROSA 결과 구분 |
| W05 첫 Full Apply Cost Gate | 최유준 집계, 이유빈 자원, 김상희 Data, 정태훈 ROSA | 서울 단가/Credit/누적·자원 수명·두 Window 산식 준비 | 검토된 Plan·실제 단가/시간/정리/재시험/잔존 비용 필요. $450 계획선/$50 여유/$500 한도 유지 |
| W06/W07 통합·결함 해소 | 각 자원 실행자, 최유준 시험 조율 | 정상 Case/인계 순서·실패 후 재시험 준비 | 해당 W03~05 인계 충족→Window A→E2E/Backup/Release와 결함 조치. 10/16 Technical Freeze 유지 |
| W08 검증 | 최유준 조율, 영역별 실행자 | Clean Recreate·장애·부하·Offline Case의 순차 실행계획 | 검증 Release/Bundle·정상 Baseline·갱신 Cost와 단일 공유 실행자 확인. 10/19~21 목표 창 유지 |
| W09/W10 결과·종료 | 각자 결과, 최유준 Index/비용, 정태훈 배포 조합, 이유빈 자원, 김상희 Data | 실제 기여·제한·Runbook·시연/잔존 책임 연결 | 10/22 Demo Freeze·10/23 Presentation Ready·10/26 종료. 실제 결과와 비용·보존/정리 확인 |

지금 필요한 입력은 세 묶음으로 관리한다.

- 실제 자산: 복구 DB를 둘 Host의 CPU/RAM/디스크 여유, 독립 Data/Backup/암호문/Key 보관 위치와 도구/CA. 새 VM 생성 가능 여부는 이미 확인됐으므로 반복 확인하지 않는다.
- 원본과 실행 환경: 최신 Source/Seed·미반영 변경·lab Overlay/수행자/Commit/Image, 비민감 GRANT, Jenkins/도구 설정과 버전, 개인 권한/Role/Backend 참조, Org PAT 정책과 Repo 보호.
- 일정과 비용: 사람별 가용일/시간·휴무·실제 소요, 서울 단가/Credit/누적/잔존, 생성/삭제/재시험 시간. 실제 Plan은 코드 준비 뒤 첫 Full Apply Gate에서 확인한다.

위 입력으로 Window A/B의 실제 시작/종료와 세부 순서를 채우되 기존 Freeze 날짜를 자동 변경하지 않는다. 전체 AWS 입력을 기다리며 Source/도구/자산 조사나 로컬 선언/시험계획 준비를 중단하지 않는다. 예상/Actual·결과/Evidence·Blocker·다음 인계는 03의 기존 실행 Ledger 필드를 사용한다.

## 10 구현 인계 양식과 실행 절차

이 절의 양식과 절차는 채택된 배정·형식 및 승인03의 실행 Ledger를 구체화한 준비 산출물이다. 새 Repository 파일/Schema Validator/Pipeline이 구현됐다는 의미는 아니다. §5.5~6의 모델은 채택됐으며 자산·인증 작업은 해당 실제 입력과 실행 Gate를 확인해 진행한다. 비의존적인 Source/권한/도구 조사와 양식 준비는 병행한다.

### 10.1 미확인 입력의 담당과 확인 시점

| 인계 ID·담당 | 확보할 입력과 확인 시점 | 막는 작업과 실패 영향 | 완료 증거/인계 |
|---|---|---|---|
| I01 정태훈, 최유준 lab | App 최신 검증 Source/Seed·미반영 변경·원 Overlay/작성자·전체 Commit/Digest와 추가 보고의 관측/정책 Manifest·원시 Log 논리 참조. 이관 직전/lab 실행 전 | 실제 App 이관/lab 검증. 출처·조합 불명확하면 재현/기여 판정 불가 | Seed 선택 기록·비민감 Source 차이·Overlay PR/Commit·lab 조건→W03/W04 |
| I02 이유빈, 정태훈 rosa | PR #11 새 Root/key·State 식별정보/보호 이전 기록, 도구/Core/Provider/Lock·Caller/MFA/목적 Role·Backend/State·지원/Quota. 로컬 확인 전 해당 도구, 실제 Plan 전 계정/Backend | Root 확인/Plan/Apply. 다른 Caller/Backend로 얻은 결과는 대상 Root 증거가 아님 | Tool Manifest·Role/Caller 논리 참조·State 점검·보호 Plan 리뷰→Root 실행자 |
| I03 김상희, 이유빈 자산 | 복구 Host 실측·격리 Data Directory·Storage/독립 사본·DB/Client/CA·Dump 크기·비민감 GRANT. 배치/Import 전 | 복구 DB 배치/TLS/Restore. 1차 영향·공간 부족·복구 지연 가능 | 자원/공간 산정·격리/TLS/목적 권한·Backup 무결성/복원 결과→Recovery 인계 |
| I04 최유준, 정태훈 리뷰 | Org PAT 최대 수명/발급 권한·Repo 보호/Bypass·Job/Agent/Binding·ECR/Harbor/Scan. 발급/CI 변경 전 | 실제 Writer/Build/Push/PR. 일반 Merge 제한과 별도 Reader 경계 미검증 | 비민감 정책/Job 범위·발급/교체 책임·Push/PR/차단 결과와 Artifact Mapping→Release |
| I05 범위별 보관자 | 보호 원본/독립 암호문/오프라인 Key·해제 수단·대용량 Evidence 보호 경로와 접근/보존 책임. Secret 공급/Offline 예행 전 | Secret 초기화/회수·Offline 재현. Key/사본 소실 또는 서비스 인증 실패 | 보호 대장 논리 ID·예비본 읽기/복호화·서비스 연결/옛 인증 거부→Cloud/CI/Recovery |
| I06 정태훈, 이유빈 리뷰, 최유준 lab | 실제 IDP/OCM/SSO/RBAC·비상 전환·초기 인증과 세션 회수, demo2 Token 폐기/보호 kubeconfig·잔존 처리. 초기 관리자 종료 전 | 정상 관리 인계·비상 접속 T03. 남은 관리 경로 상실이나 높은 권한 잔존 | 정상 허용/거부·비상 접속·신규/기존 Token·Argo 회수 결과→관리 Runbook |
| I07 최유준 집계, 네 담당자 | 가용일/시간·가격 출처/Credit·누적/잔존·실제 Plan·Window/정리/재시험. 세부 일정 확정/첫 Full Apply 전 | Window/Full Apply. $450 계획선/$500 한도 또는 Freeze 위반 가능 | 시간/비용 산식·검토된 Plan·잔존/정리 목록→Cost Gate와 실행 Window |

각 담당자는 입력을 확보했을 때 상태·확인 시각·출처·Reviewer·다음 담당을 갱신한다. 확보하지 못하면 원인·해당 Blocker·다음 확인 시점·진행 가능한 독립 작업을 기록한다. 실제 날짜가 없는 인계에 임의의 가용시간이나 성공 시각을 넣지 않는다. 공개 대장은 논리 참조만 제공하고 접속정보·Credential·State/Plan 원본은 보호 경로로 관리한다.

### 10.2 실행 단위별 Runbook 골격

| 실행 단위 | 순서 | 완료 조건과 실패 시 인계 |
|---|---|---|
| Infra Root | Source/Tool/입력 개정 고정→기존 Backend/State/Lock·실제 Caller 확인→Root 전체 Plan 리뷰→§6·§10.5의 해당 Cost/실행 조건 확인→허용된 범위 실행→해당 결과 확인→제한된 비밀값 아닌 Output 인계 | 코드 정적 확인과 실제 Plan/Apply 결과를 분리. 실패 시 Lock/부분 변경/잔존 자원·마지막 Plan/Caller를 보호 기록하고 같은 State의 다음 쓰기를 인계 후 진행 |
| App/base/lab | Source/Seed·Overlay Commit 확인→Image Build/Test/Scan·Digest/플랫폼 매핑→Secret 별도 공급 확인→Render/Owner/Namespace/삭제 경계 리뷰→lab 배포/Argo Case→결과와 원본 인계 | Build/Render/lab PASS는 ROSA Acceptance와 구분. 실패 Run/조건을 보존하고 기존 실습 Overlay를 근거 없이 삭제하지 않음 |
| CI와 Release | 제한된 Job Credential Binding→ECR/Harbor Digest와 Scan 결과→Release 후보 JSON→GitOps Branch Push/PR→사람 리뷰/Merge→Commit 후 Docs Run 연결→실제 배포/업무 시험 | CI가 자동 Merge하지 않는 흐름 확인. 후보와 배포/Acceptance 별도 판정. 실패 조합을 덮어쓰지 않고 수정 PR/새 Run으로 연결 |
| Secret 공급/교체 | 목적별 암호문·Recipient/개정 확인→주/예비본 읽기·복호화→대상 서비스에 제한 공급→로그인/Pull/DB 연결→교체 후 옛 인증/Token 확인→임시 파일 정리 | SOPS 해독만으로 서비스 성공을 판정하지 않음. 폐기된 자격증명/필요한 기존 데이터 해독 Key를 구분하고 실제 인증·회수 미완료를 다음 실행자에게 알림 |
| Offline Recovery | 장애 전 Backup/Image/Render/Secret/도구·CA 확보→장애 주입/접속 불가 시작 t0 기록→탐지·복구 결정→Key/사전 자료 확인→격리 DB Import/TLS 검증→새 Redis/App 적용→Host 안내→대표 업무/영속 데이터 확인 t1→RTO/RPO 판정 | 장애 선언/주입·탐지·조치·단계 완료/실패 시각을 기록하며 RTO=t1−t0가 30분 이내인지 판정. 03 §3-C.12.7에 따라 AWS·GitHub·Cloud IDP·ECR·AWS KMS 신규 조회에 의존하지 않는 경로를 검증한다. 로컬 DNS·Harbor 접근까지 차단하는 시험으로 확대하지 않으며 1차 자산을 복원 대상으로 사용하지 않음 |
| Cloud 관리 인계 | 정상 개인 IDP/RBAC·Argo SSO/권한 시험→채택된 비상 경로/전환 시험→초기 인증·높은 Binding·관련 Token/세션 정리→재접속 거부/정상 경로 재확인 | §5.6 결정에 따라 실제 지원·입력 확인 후 적용. 접속 계정 생성만으로 완료하지 않고 신규 로그인과 기존 세션의 남은 범위를 기록 |

팀원의 개인 자격증명/새 clone 재접속 점검은 init/plan까지다. 최신 공지는 Bootstrap apply 일시 중지를 해제했지만 지정 Root 담당자와 검토된 범위 조건은 유지한다. 이 문서로 각자 State를 재이전하거나 임의 apply/destroy·전체 패키지 업데이트·지원하지 않는 ROSA Managed Resource 변경을 수행하는 것으로 해석하지 않는다. Bootstrap의 기존 Source 차이는 §8의 담당/영향에 따라 정합화하고 실제 변경은 별도 검토된 코드/실행 범위로 진행한다.

### 10.3 Release 후보 JSON 양식

다음은 `releases/<release-id>.json` 구현 시 사용할 빈 양식이다. 현재 존재하는 실제 Release 파일이 아니며, `null`과 `NOT RUN`은 입력/실행 미확인 상태다. 이름·필드 표현은 이 형식 안의 구현 세부사항으로 관리하고 새로운 기술 선택으로 취급하지 않는다.

```json
{
  "schema_version": 1,
  "record_kind": "candidate",
  "completeness": "INCOMPLETE",
  "release_id": null,
  "source": {
    "app_sha": null,
    "infra_sha": null
  },
  "images": {
    "frontend": {"ecr_digest": null, "harbor_digest": null, "platform": null},
    "backend": {"ecr_digest": null, "harbor_digest": null, "platform": null}
  },
  "revisions": {
    "schema": null,
    "config": null,
    "secret": null,
    "tool_manifest": null,
    "recovery_bundle": null
  },
  "review_refs": [],
  "verification": {
    "render": "NOT RUN",
    "deployment": "NOT RUN",
    "acceptance": "NOT RUN"
  },
  "missing_inputs": [
    "SOURCE_COMMITS",
    "ARTIFACT_DIGESTS_AND_PLATFORMS",
    "CONFIGURATION_REVISIONS",
    "RENDER_AND_REVIEW"
  ]
}
```

후보 범위 밖의 산출물은 이유를 기록해 대상외로 판정한다. 빈칸을 가짜 값으로 채우지 않고 Cloud/Recovery의 필요한 범위에 따라 필수 항목을 확인한다. 후보 안에 그 후보를 포함한 GitOps Commit SHA를 넣지 않는다. 검사 코드/Schema Validator 구현은 적절한 기존 CI 진입점을 확인해 W03에서 수행한다.

### 10.4 Docs Run의 추가 필드와 검사 규칙

Docs의 `evidence/<test-id>/<run-id>/release.json`은 후보에서 실제 사용한 조합에 다음을 추가한다. 후보와 Run은 서로 다른 기록이며 후보를 실행 성공의 기록으로 덮어쓰지 않는다.

| 추가 필드 묶음 | 기록할 내용 |
|---|---|
| Run 식별 | record_kind=run, Release/Run/Test/Case/Requirement ID, 환경과 대상 범위, 선행 실패/후속 Run |
| 실행 Source | 실제 GitOps 전체 SHA, Render/Bundle/Tool Manifest 참조, Image Digest/실행 플랫폼, 조건/부하/장애 주입 |
| 실행과 협업 | assigned_execution_owner, actual_operator, reviewer, collaborators와 작업, observed_principal_ref, account_management_owner_ref, borrowing_handover_ref |
| 시각과 판정 | UTC ISO 시각(Z 또는 명시적 오프셋)과 같은 시각을 변환한 KST 표시, Baseline/Target/Actual/단위·집계 조건, render/deployment/acceptance별 결과와 증거 |
| Recovery/Backup | 사용 Backup ID·암호문 Hash, 사고 시각과 영속 Data 기준 시각/확인 수준, Dump 시작/종료·사전 동기화/무결성·Import·업무 재개 시각. RPO=사고 시각−실제 사용 Data 기준 시각의 90분 목표와 손실 업무·Redis 새 Runtime 손실을 구분. RTO/달성·미달 이유 |
| 보호 자료 | raw_artifact_ref, custodian_ref, access_policy_ref, retention_ref, availability/integrity 결과. 실값/접속 경로는 보호 운영 대장 |

정확한 Snapshot 시각을 계측하지 못한 Backup은 Dump 시작 시각과 확인 수준을 보수적으로 기록하고 쓰기 Marker/복원 데이터로 대조한다. 파일 수정/덤프 종료 시각을 Data 기준으로 대신하지 않는다. 정확한 RPO를 판정할 수 없으면 시점 범위와 확인된 손실을 기록하며 기존 90분 목표를 자동 완화하지 않는다.

JSON/Markdown/CSV 구현 후 검사는 다음 기준으로 수행한다.

1. 필수 Source/Digest/설정 개정과 대상 조건이 미확인이면 완성 후보로 승격하지 않는다. 대상외는 이유와 범위를 기록한다.
2. 전체 SHA·Digest·타임존을 포함한 UTC 시각·결과 열과 고정한 CSV 열/단위/집계 조건을 확인하고 대상 조합과 실제 사용값의 일치를 리뷰한다. 단계 시각의 순서와 누락을 확인하며 시계/시점 불확실성은 제한으로 기록하고 임의의 0이나 추정 성공 시각으로 채우지 않는다. 형식이 맞다는 사실만으로 실행 성공을 판정하지 않는다.
3. 후보에는 자기 참조 GitOps SHA를 넣지 않고, Run은 Commit이 존재한 뒤 실제 사용 GitOps SHA를 연결한다.
4. Render·Deployment·Acceptance를 각각 NOT RUN/PASS/PARTIAL/FAIL/N/A로 기록하며 PASS에는 해당 증거가 필요하다. N/A는 이유와 제외된 시험 범위를 기록한다.
5. Secret 값/평문 Hash·Credential·State/Plan·평문 SQL/Backup·개인정보·비밀값 포함 URL을 공개하지 않는다. 원본과 실제 접속정보는 보호 운영 대장의 논리 참조에서 연결한다.
6. 같은 Run의 Summary/Metric/Timeline/공유 가능한 Checksum을 연결하고 실패 Run을 보존해 수정/재시험을 별도 Run으로 기록한다.
7. 참여자는 실제 작업을 기록하며 Commit/Caller 이름만으로 실행자나 전원의 성과를 배정하지 않는다. 담당과 다른 실행은 §2.4의 인계 정보를 남긴다.

이 단계에서 확인한 것은 문서 내 빈 JSON의 파싱과 확정/입력 대기/미실행 상태·담당/의존관계의 정합이다. 실제 수집 코드·후보 생성·인증/Runtime 시험의 PASS가 아니다.

### 10.5 Cost/Window 기록과 04 문서 종료 조건

Cost/Window는 기존 승인 목표일을 유지하며 실제 Plan/단가/Credit/시간으로 채운다.

| 기록 대상 | 계산/확인 |
|---|---|
| Window A/B 생성·검증·삭제 | 자원별 실제 단가×가동시간, 생성/삭제 대기와 재시험 시간 포함. Window 사이 유지 자원은 별도 계산 |
| Data/Storage/통신과 잔존 | RDS/Redis·EBS/S3/Backup/통신/NAT 등, Stop/Delete 후 남는 자원과 최소 과금/시간 단위를 실제 조건으로 확인 |
| Credit와 누적 | Credit 대상/기간/미적용 비용, 기발생/이번 예상/잔존을 구분. Credit 충당과 자원 비용을 이중 차감하지 않음 |
| 판정 | $450 계획선+$50 여유=$500 상한. 예상과 실적·불확정 비용을 구분하고 초과/일정 변경이 필요하면 문제/영향/대안 제시 |

03 §3-H.6에 따라 총 예상 비용은 **현재 누적＋잔여 비Window 기반/Data/Storage＋잔여 ROSA 관련 Window＋전송/요청/관측＋정리 지연/실패 예상**으로 계산한다. $450 계획선을 초과하면 신규 가동을 보류하고 조정하며 $500 전체 한도를 유지한다. 실제 단가·Credit 조건·가동/삭제/재시험 시간을 확인하기 전 Cost PASS를 기록하지 않는다.

**04 문서 종료와 구현/시험 준비 완료는 별도다.** 다음 조건이 갖춰지면 04 문서 단계의 종료를 판단할 수 있다.

- 이미 채택된 결정·책임과 03의 보존/Ownership/Cost 기준이 모순 없이 기록돼 있다.
- §5.5~6의 구조 모델이 명시적으로 채택되고 직접/후속 영향과 해당 Runbook에 반영돼 있다.
- 미확인 입력마다 담당·확인 시점·막는 작업·필요한 증거·실패 영향이 배정돼 구현 단계로 인계돼 있다.
- Root/Source/Secret/Release/Evidence/WBS와 문서 전체의 연쇄 검토가 끝났다.

Host명/실제 용량, Credential ID, Org 정책, 실제 단가/Plan이나 후속 시험 결과가 전부 갖춰질 때까지 04 문서 종료를 미루지 않는다. 해당 구현/Plan/Apply/시험의 Gate로 인계한다. §5.5~6은 사용자 채택이 완료됐으며 최종 전체 재검증 결과는 §11에 기록한다. 실제 코드 시작은 해당 입력 대기, 실제 base의 lab/Plan은 필요한 현물/환경 대기, 첫 Full Apply는 NOT READY, 최종 ROSA/Recovery 시험은 NOT RUN이다.

## 11 전체 연쇄 검토와 종료 기록

### 11.1 범위와 방법

역사적 00·승인된 01/02/03·등록 지침, 사용자 결정 전체, 현재 04 전체, 추가 팀 보고, 이미 조회한 지정 Repo/PR/Issue 및 공식 문서 범위를 대조한다. 결정→책임→입력→코드/실행 Owner→Secret/Release→시험/실패 처리→일정/비용→후속 인계를 추적하고, 수정 후 직접 영향과 후속 범위를 다시 읽는다. Runtime·보호 원본·미제공 입력은 확인 가능한 문서/Source와 구분한다. 닫힌 03과 팀 보고 원본은 수정하지 않는다.

### 11.2 보완과 재검증 기록

| 검토 회차 | 발견과 조치 | 재검증 범위/판정 |
|---|---|---|
| 1 전체 추적 | 사용자 채택으로 §5.5/6을 확정 전환하고 Header/결정표/입력/연쇄 영향/Runbook/종료 조건을 함께 정합화 | 모델 확정과 실제 입력·Runtime 대기를 분리 |
| 1 실행 해석 보완 | 최초 bootstrap과 현 Remote 정본 연결 분기, 비의존 정적 작업 허용, Data/Recovery 별도 VM과 장애 영역 구분, Offline 신규 외부 조회 의존 제거, CSV/시간선 검사, 전체 비용 산식/$450 초과 신규 가동 보류 연결 | §2/4/5/6/7/9/10·03 근거·I01~I07·T/W/Window 재대조 |
| 1 단계/지침 연결 | 승인된 Network 수량·05 구현 범위를 명시하고 지침의 과거 미확정 역할/보관/형식·현재 단계를 현행화 | 문서번호/GATE/WBS, 닫힌03·닫힐04·실행05와 Runtime Gate 구분 |
| 2 수정 후 전체 검증 | 개정 지침 §27의 Backup 개인 Key 예비 보관자 요약이 04 §5.3과 다른 점 발견, 이유빈으로 정정 | Cloud/CI/Backup/Recovery/개인 Key의 보관·공급·Offline 인계를 다시 대조 |
| 3 정정 후 전체 재검증 | 04 전체·개정 지침·승인 설계의 역할/보관·Infra/State·Recovery·Release/Evidence·시간/비용·단계 연결을 재검증, 추가 보완 0건 | 문서 정합 범위에서 수렴. JSON 파싱·Markdown 표/코드 경계·I01~I07·상태 검사 통과, 승인03/등록 지침 원본 SHA-256 불변 |

### 11.3 종료와 다음 입력

2026-10-01 KST 전체 연쇄 검토→보완→재검증→정정 후 재검증을 마쳤으며 추가 보완/변경 0건으로 수렴했다. 사용자 요청의 종료 조건이 충족돼 **04 문서 전체 종료**로 판단한다. 역할/Infra·State/Recovery/Evidence를 나눠 전체 대조하고 수정 영향을 다시 확인했으며 최종 상태 선언도 별도 확인했다. I01~I07과 W02~W10은 `05_IMPLEMENTATION_AND_VALIDATION.md`로 인계한다. 05의 새 Source 관측/실행 결과는 그 기록에 누적하며 닫힌 04의 과거 관측을 최신 Runtime으로 바꾸지 않는다. 설계 기준을 실질적으로 바꾸는 제약은 결정·영향을 별도 기록한다.

04의 문서 완결성과 실제 실행 준비를 분리한다. 실제 base/lab·Plan·Full Apply·ROSA/Recovery Acceptance는 미완료이며, 문서 검증으로 PASS를 부여하지 않는다. 추가 입력/코드/시험으로 발견되는 제약은 후속 단계의 정당한 변경 관리이며 모든 미래 사실이 알려졌다는 뜻으로 문서를 종료하지 않는다.

## 남은 작업과 다음 단계

- [x] 03 종료와 04 진입 기록
- [x] 작성, 리뷰, Root별 실행과 Data/시험 책임 확정 기록
- [x] 향후 ocp-lab 최유준 책임과 과거 수행 이력 구분
- [x] 복구 DB 직접 연결 확정과 새 VM 생성 가능 확인
- [x] AWS 공지와 실제 Source/Issue 보고의 범위 대조
- [x] AWS Provider 6.67.0 초기 검증 후보 확정
- [x] GitOps Writer PAT와 무기한 우선/최대 수명 기준 확정
- [x] Secret 보관·Release/Evidence 운영의 후속 대안 비교 정리
- [x] Secret 보관자·Release/Evidence 형식/책임 사용자 채택 반영
- [x] 공동 참여와 계정 대여 설명의 실제 수행/계정 기록 연결
- [x] 영역별 입력에 따른 WBS·인계와 병행 조건 구체화
- [ ] 기존 Overlay 제공자와 출처, 실제 Branch/Commit와 Merge 책임 확인
- [ ] 실제 Source/Seed/GRANT/권한/계정/도구/자산/가용시간 확보
- [ ] 채택한 전용 VM의 실제 Host 자원·용량과 배치 결과 확인
- [x] PR #11의 경로/State Key/정확 버전/입력 전달 문서 정합 확인
- [ ] 목적 TF Role/MFA·개인 clone·State 이전 기록/복원·실제 입력 전달 구현 확인
- [x] §5.5 전용 복구 DB VM과 §5.6 비상 접속/초기 인증 회수 모델 사용자 채택 반영
- [x] 입력별 담당/확인 시점/Blocker/증거/실패 영향과 인계 연결
- [x] 실행 단위별 Runbook, 후보 JSON/Run 필드/검사 규칙 정리
- [x] 추가 demo2 보고의 예제/실제 base 구분·잔존/Token/후속 담당 연결
- [x] WBS/Window/Cost 조건과 04 문서 종료/실제 실행 Gate 분리
- [x] 새 결정의 연쇄 검토·정정 후 재검증 수렴과 04 문서 전체 종료 판단

두 구조 결정과 최종 전체 검토·지침 정합 확인이 완료돼 04를 종료했다. 다음은 05의 실제 입력/Source 점검과 준비된 영역의 구현·통합·검증이다. 확정된 보관자·형식의 실제 자산/접근/인계와 Source·도구·계정·Host·비용 입력은 I01~I07로 구현 단계에 넘긴다. 03 종료는 유지하며 04 문서 종료, 작업별 구현 시작과 첫 Full Apply는 서로 다른 조건으로 판정한다.
