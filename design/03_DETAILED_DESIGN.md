# 石나가는 판단 2차 프로젝트 03 상세설계

> **문서 단계:** 03 상세설계 승인 완료 / 후속 05 구현·검증의 설계 기준  
> **기준일:** 최초 2026-10-01 KST / 설계 정합성 개정 2026-10-07 KST  
> **상태:** CONFIRMED DESIGN — 2026-10-01 상세설계 승인, 2026-10-05 DR 목표·주기 및 2026-10-06 Valkey 선택 반영. 실제 구현·시험 결과는 05와 원 Issue·PR·Run에서 관리  
> **상위 기준:** `01_PROJECT_CHARTER.md`, `02_TARGET_ARCHITECTURE.md`, `PROJECT_INSTRUCTIONS.md` 및 기록된 최신 승인 결정  
> **기간 / AWS 지원 한도:** 2026-09-28~2026-10-26 / $500

> **현재 DR 설계 기준:** [§3-I.14.5](#recovery-design-decision-20261005)의 **RTO 10분·영속 DB RPO 30분·DB 운영 중 Portable Backup 15분 계획 주기, 기존 Backup/Restore 구조 유지**를 적용한다. [PR #30](https://github.com/seokpan/seokpan-hybrid-docs/pull/30)은 main에 병합됐으며 30분/90분/1시간은 이전 승인 이력이다. 설계 선택과 실제 운영 달성은 별개다. 전체 T18은 미검증이며 05/ROSA 전체 완료를 설계 선택의 선행조건으로 두지 않는다.

이 문서는 프로젝트 03 상세설계 전체를 담은 단일 문서다. Repository·Network·IAM/Secret·Migration/Data·서비스 규약·Terraform/GitOps·시험/Evidence·WBS/비용과 통합 검토 결과를 포함한다. 세부 절차·비교 근거·검증 조건은 각 분야 절에 유지하고 분야 간 참조를 같은 문서의 절 번호로 연결했다.

설계 단계 진행 현황 — 실제 실행 상태는 05와 원 작업 참조:

- [x] 3-A~3-E·3-F-1 승인된 작업 전제 문서화
- [x] B01~B07 선택·대안·영향·구현 Gate 작성
- [x] 전체 연쇄 검토·보완·재귀 검증 결과 반영
- [x] 전체 상세 내용·시험 Matrix·Runbook·WBS를 단일 03 문서에 통합
- [x] B01~B07 승인 이전 단일 통합본·지침 재귀 검토 기록 — §3-I.12.1
- [x] B01~B07 작업 전제 사용자 컨펌 및 연쇄 반영 — 2026-10-01, §3-I.12.2
- [x] 승인 반영본·지침 연쇄 보완 후 추가 변경 없는 재검증 — §3-I.12.3
- [x] 승인 반영본 전체03·개정 지침 사용자 최종 컨펌 — 2026-10-01
- [x] 최종 승인 상태 반영·프로젝트 소스 등록 완료 보고 — §3-I.12.4
- [x] 추가 팀원 자료·Issue 결과의 범위 대조 및 구현 준비 인계 — §3-I.13
- [x] 두 독립 부분 Run·고정 App Source와 제약 비교에 따른 DR 목표/주기/구조 변경 후보 정리 — §3-I.14.5
- [x] DR 설계 요구 채택·PR #30 병합. 후속 문구·출처 정합성 보완과 실제 운영 경로 Acceptance는 별도
- [ ] 실제 Seed·팀 배정·계정/도구/자산 Preflight 확인
- [ ] 첫 Full Apply 전 Cost Baseline Gate 확인

## 문서의 승인 상태와 사용 범위

3-A~3-E·3-F-1·B01~B07 작업 전제 검토를 거쳐 2026-10-01 전체 상세설계와 프로젝트 지침이 승인됐다. 이후 DR 요구사항과 Data 엔진의 변경은 각 결정 기록에 연결한다. 실제 지원·입력·가격 확인 및 구현·시험 완료는 설계 승인과 구분한다. 버전·규모는 실제 지원과 Source 검증을 전제로 한 초기 후보이며, 시험 수치는 프로젝트 요구사항이다. 설계 승인을 실행·시험 성공으로 기록하지 않는다.

실제 Source/Seed SHA·Account/Quota/지원 패치·Role/IDP/Secret 공급 값·로컬 자산·가격/Credit·자원/Pool 측정값은 구현 전에 확인한다. 미확인 입력을 임의 값이나 PASS로 대체하지 않는다. 문서 최종 확정 후에도 실제 지원·비용·Source 결과가 변경을 요구하면 그 영향과 재검증을 기록한다.

3-A~3-I는 이 문서 안의 분야 식별자다. `§3-F.18.2`는 Terraform/GitOps 절의 18.2 항목을 뜻한다. IF·IM·NET·T는 시험/통신 요구 식별자이고 `[3-F-R1]` 같은 표기는 해당 분야의 공식 참고 자료다. 숫자 범위/연결은 같은 분야의 해당 하위 항목을 포함한다. 각 분야의 작업 전제 승인·결정 이력과 실제 확인/실행 대기 상태를 구분하며, 다음 표와 3-I가 현재 승인 상태의 기준이다.

| 범위 | 현재 상태 | 상세 위치 |
|---|---|---|
| Repository·Source | 3-A 승인. 개인별 권한·Branch 보호·Tree·Seed의 실제 검증은 05와 원 작업에서 추적 | 3-A·3-I.13 |
| Network·IPAM·Hybrid | 3-B 작업 전제 승인. 실제 경로·Source·권한·복구는 구현 검증 대상 | 3-B |
| IAM·IDP·Secret | 3-C 작업 전제 승인. 사람 IAM User 4+Admin, CI/Backup 각 1, TF 목적 Role 별도 | 3-C |
| Migration·Backup·Recovery Data | 3-D 기존 구조 승인 유지. 별도 새 Recovery Redis, 현재 계획 주기는 DB 운영 중15분 Backup — 이전1시간 승인 이력과 구분 | 3-D·3-I.14.5 |
| 서비스 연결·인증·업무 안전 | 3-E 작업 전제 승인. 실제 App 계약·Source·동작 검증은 05에서 추적 | 3-E |
| Root/State·제한 입력·GitOps 최초 설치 | 3-F-1 작업 전제 승인 | 3-F.2~7 |
| 버전·Backend·Runtime Pull·배포·Replica | B01~B05 작업 전제 승인. 실제 지원·Source·코드/동작은 구현 단계에서 확인 | 3-F.13~18 |
| 시험/성능·복구 수치 | B06 기존 승인 이력 유지. DR은 현재 RTO10분/RPO30분으로 변경, 전체 Recovery/ROSA 최종 시험 NOT RUN | 3-G·3-I.13·3-I.14.5 |
| 작업 트랙·Window·$450 계획선/$50 여유 | B07 작업 전제 승인. 실제 담당은 04, 가동시간·비용은 05에서 추적. $500 한도·Cost Gate 유지 | 3-H |
| 전체03 | 2026-10-01 설계 승인·03 종료 유지, 구현 진행은 05에서 관리 | 3-I |

## 상세설계 목차

| 절 | 내용 |
|---|---|
| 3-A | Repository와 Source 경계 |
| 3-B | Network IPAM과 Hybrid 연결 |
| 3-C | IAM Identity와 Secret |
| 3-D | Migration Seed와 Data |
| 3-E | 서비스 연결과 업무 규약 |
| 3-F | Terraform과 GitOps 구현 구조 |
| 3-G | 시험과 Evidence |
| 3-H | 구현 WBS와 비용 |
| 3-I | 승인 상태·통합 검토·시험 대응·Runbook·재귀 검토 결과 |

## 3-A Repository와 Source 경계

### 3-A.1. 목적과 상위 Architecture

2차 프로젝트는 1차 온프레미스 Kubernetes 결과물을 AWS 하이브리드 환경으로 마이그레이션하고 검증한다. 정상 서비스는 ROSA Classic Multi-AZ, RDS MariaDB Multi-AZ, ElastiCache Valkey 7.2 Multi-AZ를 목표로 하는 Cloud Primary에서 실행한다. On-Prem은 Jenkins, Harbor Recovery Registry, 사전 동기화 Backup 및 Restore-based Recovery를 담당한다.

이 절은 Application 코드, Infrastructure 자동화, 배포 Desired State, 설계·검증 기록의 보관 위치와 경계에 대한 소단계 승인 내용을 기록한다. Resource별 Owner는 하나로 두며, 기존 1차는 독립 포트폴리오로 보존한다.

### 3-A.2. 소단계 승인된 여섯 가지 작업 전제

1. 2차는 App / Infra / GitOps / Docs의 네 저장소로 운영한다.
2. 기존 `seokpan` Organization 안에서 `seokpan-hybrid-*` 이름을 사용하고 1차 저장소와 분리한다.
3. 2차 On-Prem Hybrid·Backup·Restore 코드도 Infra / GitOps 경계 안에 포함한다.
4. Application은 Migration 구현 직전 Latest Validated State에서 Seed를 고정하고, 새 독립 저장소에 Seed까지의 Git 이력을 보존한다.
5. Bootstrap 실행 코드와 Manifest 원본을 구분하며 Resource별 Owner를 하나로 둔다.
6. Evidence Index는 Docs에서 관리하고 Release의 Code / Image / Manifest / 검증 결과를 연결한다.

### 3-A.3. 저장소별 책임

| 저장소 | Source 원본 | 경계 |
|---|---|---|
| `seokpan-hybrid-app` | Frontend / Backend, Test, Dockerfile, Application Build용 Jenkinsfile | 실제 배포 대상·Image Digest는 GitOps에서 관리 |
| `seokpan-hybrid-infra` | Terraform, AWS/ROSA 기반 구성, Bootstrap 실행 코드, 2차 Hybrid·Backup·Restore 자동화 | Cluster 내부 Resource를 GitOps와 중복 관리하지 않음 |
| `seokpan-hybrid-gitops` | ROSA 내부 Desired State, Application/Platform Manifest, 환경별 배포 설정, 별도 On-Prem Recovery 배포 정의 | Terraform State 및 실제 Secret 값을 Git에 보관하지 않음 |
| `seokpan-hybrid-docs` | 승인 설계, ADR, Migration 기록, Runbook, Test 결과, Evidence Index, Cost, Troubleshooting | 실행 코드의 원본을 중복 관리하지 않음 |

각 구현 저장소의 README에는 해당 코드의 실행법을 둔다. 프로젝트 전체의 승인된 결정·검증 결과는 Docs에서 관리하고 링크로 연결한다.

1차 저장소의 기존 이름과 Git History는 유지한다. 1차 Bug Fix·Maintenance는 기존 Track에서 수행하며, 2차 AWS/ROSA 전용 구현은 위 저장소에 기록한다.

### 3-A.4. 주요 대안과 선택 근거

가능한 모든 조합을 열거한 것은 아니며, 의사결정에 실질적으로 영향을 주는 주요 구성을 비교했다.

| 대안 | 장점 | 부담 / 채택 여부 |
|---|---|---|
| 통합 저장소 하나 | 탐색·Issue 관리가 단순하고 연관 변경을 한 PR에 기록하기 쉬움 | CI 트리거·배포 경로·검토 범위를 구분해야 함. 미채택 |
| App / Platform / Docs 세 저장소 | 저장소 수를 줄이면서 Application을 분리 | Platform 내부의 Terraform·배포 변경을 구분해야 함. 대안으로 유지 |
| App / Infra / GitOps / Docs 네 저장소 | 코드·인프라·배포·의사결정 이력이 분명하고 1차와 비교하기 쉬움 | 여러 저장소의 Issue·PR·Release 연결 필요. 채택 |

네 저장소 분리는 기술적 필수조건이 아니다. 동일 저장소에서도 Terraform / GitOps Ownership을 구분할 수 있다. Cluster 삭제와 Git 저장소 보존 역시 별개의 Lifecycle이다.

선택 근거는 1차의 App / Infra / GitOps / Docs 역할 구분을 이어가면서, 2차의 변경·검토·기여·포트폴리오를 별도로 설명하기 쉽다는 점이다.

### 3-A.5. On-Prem Recovery Source 경계

| 대상 | 보관 위치 |
|---|---|
| On-Prem VPN 설치·설정 자동화 | `seokpan-hybrid-infra` |
| Logical Backup 생성·전송·사전 동기화 코드 | `seokpan-hybrid-infra` |
| MariaDB Restore 자동화 | `seokpan-hybrid-infra` |
| On-Prem Recovery Application / Redis 배포 Manifest | `seokpan-hybrid-gitops`의 별도 Recovery 경로 |
| 복구 절차·측정 결과·Evidence Index | `seokpan-hybrid-docs` |
| 실제 Backup 파일 | 승인된 S3 / On-Prem Recovery Storage |

1차 공통 기반과 2차 전용 Recovery 구성의 관리 대상을 나눈다. 3-D-2 작업 전제 승인에 따라 Recovery Redis는 기존 1차 Redis와 분리된 새 전용 Runtime으로 구성한다(§3-D.9). 2차 전용 Resource는 2차 Source에서 관리하며 기존 1차 Redis를 복구 대상으로 덮어쓰지 않는다. 같은 Cluster의 같은 Resource를 두 GitOps 체계가 동시에 관리하지 않는다.

실제 Recovery Namespace/로컬 주소는 구현 입력으로 확인한다. 별도 새 Redis는 3-D의 승인 전제이며 Recovery Overlay와 Offline Apply 실행 방식은 3-F B04의 승인된 작업 전제이며 실제 경로·보존본·동작은 확인 전이다.

Git의 복구 Manifest만으로 AWS 외부 복구 준비가 완료되는 것은 아니다. 승인 Image, 장애 선언 전에 On-Prem에 동기화된 Backup, 설정·Secret 복구 경로를 함께 확보해야 한다. Recovery Redis는 Application 실행을 위한 Runtime이며 AWS ElastiCache Runtime State의 무중단 복제를 뜻하지 않는다.

### 3-A.6. Application Seed 및 재사용 출처

1차 공식 종료 Baseline은 2026-09-23으로 유지한다. 실제 2차 Seed는 Migration 구현 직전, Maintenance / Validation이 반영된 Latest Validated State에서 고정한다. 현재 Seed SHA는 미확정이다.

#### 가져오는 방법 비교

| 방법 | 판단 |
|---|---|
| GitHub Fork | 원본 관계가 명시되지만 Fork 관계와 별도 프로젝트 표현을 함께 운영해야 함. 미채택 |
| 새 독립 저장소 + Seed까지 Git 이력 보존 | 원본 기여·변경 이력을 유지하고 Seed 이후 2차 변경을 비교하기 쉬움. 채택 |
| 새 독립 저장소 + 파일 Snapshot 복사 | 초기 이력은 간단하지만 이전 저자·변경 이력이 끊겨 별도 출처 기록에 의존. 미채택 |

실제 이관 시 Seed Commit과 필요한 이력을 기준으로 한다. README에서 1차 상속 이력과 2차 기여를 구분한다. Seed 이후 1차 변경을 자동 동기화하지 않으며, 영향 검토 후 Cherry-pick / Backport 여부를 기록한다.

Infra / GitOps에서 일부 1차 코드를 재사용할 때도 원본 Repository, Commit SHA, 가져온 경로, 수정 이유를 기록한다. Application의 이력 보존 결정을 Infra / GitOps 전체 이력 복제 결정으로 확대하지 않는다.

Seed 기록에는 Repository, SHA, 선택일, 선택 이유, 미반영 Maintenance, 추가 Cherry-pick / Backport 판단을 포함한다.

### 3-A.7. Bootstrap와 Resource Ownership

| 책임 | 위치 |
|---|---|
| ROSA Ready 이후 GitOps 설치·초기 연결 실행 코드 | `seokpan-hybrid-infra` |
| GitOps Operator 최초 설치의 Subscription/필요 OperatorGroup 선언 | `seokpan-hybrid-infra`의 최소 Bootstrap 예외 |
| Root Application 원본과 이후 App/Project/Desired State 선언 | `seokpan-hybrid-gitops` |
| 실행 순서와 Ownership 인계 기준 | `seokpan-hybrid-docs` |

Bootstrap 실행 코드가 동일 Manifest를 별도로 복사하여 계속 관리하지 않도록 한다. 3-F-1 승인에 따라 최소 Ansible 진입점으로 GitOps를 설치하고 Root를 최초 등록한 뒤 내부 Desired State 관리 책임을 GitOps로 넘긴다(§3-F.2·§3-F.6~7). 설치 예외인 Subscription/필요 OperatorGroup 등의 원본은 Infra Bootstrap 경로에, Root/App/Project 등 이후 원본은 GitOps 경로에 둔다. 동일 객체를 양쪽에서 소유하지 않는다.

저장소 경계와 Resource Ownership은 별개다. AWS/ROSA Infrastructure는 Terraform / RHCS가 관리하고 Cloud Cluster 내부 Desired State는 GitOps가 관리한다. B04로 승인된 로컬 Offline Recovery는 GitOps Recovery Overlay에서 사전 Render한 보존 Manifest를 Infra의 Ansible로 적용하는 제한된 실행 예외다(§3-F.17.3). 선언 원본은 GitOps에 두고 해당 로컬 Namespace의 적용 객체는 이 복구 경로 하나만 관리하며 실행 중인 Argo와 같은 객체를 중복 관리하지 않는다. Secret 값/객체는 별도 공급 체계의 책임이며 Git 평문 저장 대상이 아니다.

### 3-A.8. Release와 Evidence 연결

| 식별정보 | 목적 |
|---|---|
| Application Commit SHA | Build한 코드 식별 |
| Frontend / Backend Image Digest | 배포 Artifact 식별 |
| GitOps Commit SHA | 배포 Desired State 식별 |
| ECR / Harbor Artifact 참조 | Cloud Runtime 및 Recovery Image의 대응 확인 |
| Test Run / Evidence 참조 | 해당 Release의 실제 검증 결과 확인 |

위 정보를 연결한다는 원칙은 소단계 승인되었다. Release Metadata의 필수 식별정보는 이 절과 §3-I.7을 함께 따른다. 실제 파일 형식/저장 경로와 CI→PR Promotion 구현은 §3-F.17의 B04 승인된 작업 전제와 실제 구현 입력으로 구분한다. Desired State와 실제 배포 결과는 구분한다.

별도 Evidence 저장소는 추가하지 않는다. Docs에 Index와 정리된 결과를 둔다. 대용량 로그·영상의 실제 저장 위치는 §3-G.9의 보호/Index 기준 아래 구현 Preflight에서 입력으로 확인하며 필요한 ROSA Evidence는 Cluster 삭제 전에 외부에 보존한다.

### 3-A.9. 영향 범위 및 재검토 조건

영향 영역은 Network 자동화, IAM / CI Credential, Migration / Seed, Interface Contract, Terraform / GitOps 구현구조, Test / Evidence, WBS이다. 다른 상세설계 절은 3-A의 저장소 경계를 입력으로 사용한다.

기술적 불가능, 비용 초과, 일정상 실현 불가능, Ownership 충돌, PoC 실패 또는 사용자 재검토 요청이 발생하면 영향을 보고하고 변경안을 다시 확정한다. 기존 결정을 조용히 바꾸지 않는다.

### 3-A.10. 남은 선택과 실제 구현 입력

- Repository 공개 범위 및 실제 생성·권한 설정
- B04 승인된 Base/Overlay 구조에 맞춘 실제 디렉터리·환경명
- CI의 승인된 제한 Principal/권한 기준에 맞춘 실제 Policy·Job 설정과 B04 Promotion 구현
- Release Metadata 형식
- 대용량 Evidence 저장 위치
- Seed SHA 및 실제 이관 실행
- 실제 Recovery Namespace / 승인된 별도 새 Redis의 설정 / B04 Recovery 배포 방식
- Bootstrap 설치·Ownership 인계 구현

### 3-A.11. Source 계보 및 검증 상태

`00_PROJECT_STARTING_POINT.md`는 역사적 출발점으로 보존한다. `01_PROJECT_CHARTER.md`와 `02_TARGET_ARCHITECTURE.md`는 현재 승인된 상위 프로젝트/Architecture 기준이다. 상위 문서 작성 당시 미확정이었던 Repository topology는 이후 사용자에게 승인받은 이 문서의 3-A 작업 전제를 따른다. 지침 개정본에도 이 상태를 반영했다. 전체03의 최종 컨펌과 프로젝트 소스 등록 완료는 2026-10-01 전달 확인에 따라 반영했다(§3-I.12.4). GitOps 내부 구조는 B04 작업 전제로 승인되었으며, Release Metadata의 실제 저장 형식·대용량 Evidence 위치는 구현 입력으로 확인한다.

관련 근거는 3-A 비교 제안 및 2026-10-01 KST의 명시적 승인다. 3-A 설계 작성 당시에는 GitHub 저장소 상태를 조회하거나 생성하지 않았다. 이후 이번 구현 준비에서 수행한 읽기 전용 Repo/Issue/지정 Commit 조회는 §3-I.13에 따로 기록한다. Runtime을 직접 조회하거나 Repo를 변경한 것은 아니다.

- [x] 주요 대안 비교
- [x] 사용자 소단계 승인
- [x] 여섯 가지 승인사항 작업 문서화
- [x] 상위 Architecture / 1차 보호 / Seed / Ownership 경계 대조
- [x] 전체03 문서 연쇄 검토·보완 및 재검증
- [x] 사용자 전체03 최종 컨펌 및 상세설계 승인 상태 반영
- [x] Project Source 등록 완료 보고
- [ ] GitHub Docs 반영 여부·개인별 권한/Branch 보호 실제 확인
- [ ] 저장소 생성·코드 이관·구현·Runtime 검증

3-B~3-E와 3-F-1의 승인된 작업 전제가 이 문서의 관련 상세설계 절로 연결되었다. 3-F·3-G·3-H의 B01~B07도 작업 전제로 승인되었다. 현재는 전체03·지침 최종 컨펌과 등록 완료 확인 후 실제 구현 준비 단계이며, §3-I.13을 준비 인계의 시작점으로 사용한다.

#### 상태 정정 기록 — 2026-10-01 KST

당시 사용자는 3-B 연결 모델 승인과 함께, 3단계 전체 검토 후 문서를 최종 확정하며 당시 기록은 그대로 최종본으로 받아들이지 않는다고 명시했다. 이 지시를 3-A 기록에도 적용하여 당시 `CONFIRMED` 표현을 `WORKING DRAFT / 소단계 승인`으로 정정했다. 이후 전체03 최종 컨펌은 §3-I.12.4에 기록하며 저장소 경계의 승인 내용은 유지한다.

## 3-B Network IPAM과 Hybrid 연결

### 3-B.1. 연결 모델 — 소단계 승인

**기록 ID:** PH2-3B-CONNECTIVITY  
**승인일:** 2026-10-01 KST

1. Hybrid 연결은 AWS EC2 WireGuard + On-Prem 선제 Outbound 연결을 사용한다.
2. On-Prem 종단점은 전용 VPN Gateway VM으로 한다. 구현 전 VM·주소 확보를 확인한다.
3. AWS 종단점은 VPN EC2 1대 + EIP로 시작하며, Gateway HA는 후속 범위로 둔다.
4. Tunnel에는 필요한 사설 통신만 넣는다. 정상 사용자 요청과 ECR·S3·AWS API 통신 경로를 구분한다.

통신 가능 여부와 전송 작업의 VPN 사용 여부는 별개다. S3 Backup의 On-Prem 동기화는 HTTPS 경로도 가능하며, 생성 위치·전송 도구는 Data 상세설계에서 결정한다. 정상 Cloud Runtime을 VPN Gateway에 의존시키지 않는다.

전용 Gateway를 추가하더라도 기존 vRouter의 AWS 목적지 Route, 왕복 경로와 NAT 예외를 검토해야 한다. 단일 Gateway 장애에 대해서는 탐지, 재기동·재구축, Route 복구, 통신 재개를 검증하고 AWS 정상 서비스 영향도 확인한다. Gateway HA 완료를 주장하지 않는다.

#### 비교·근거·재검토

EC2 WireGuard, AWS 관리형 Site-to-Site VPN, Mesh 계열, 다른 Software VPN 및 HTTPS 전송을 비교했다. 이는 가능한 모든 선택지를 열거한 것은 아니다. WireGuard는 승인된 시작 문서에 강의실 환경의 성공 PoC가 기록되어 있어 현재 학원망 제약에서 구현·학습·검증 부담이 작다.

전용 On-Prem Gateway는 기존 Router 역할과 VPN 역할을 분리한다. AWS 단일 종단점은 일정·비용 제약에 맞춰 우선 수용하되, 정상 서비스와 장애 영역을 분리하고 복구 절차를 검증한다.

AWS 관리형 Site-to-Site VPN을 모든 방식에서 불가능하다고 단정하지 않는다. 일반적인 IP 등록 방식의 고정 IP 요구와 AWS Private CA 인증서를 사용하는 Public VPN 예외를 구분한다. 해당 대안의 비용·IAM·학원망 적합성까지 검증한 것은 아니다.

검토에서 Gateway 확보 불가, UDP/Route 제약, 실측 성능 부족, 정상 서비스 의존성, 비용 초과 또는 일정상 문제를 발견하면 모델 변경을 제안한다. 관련 Issue / PR / Runtime Evidence는 이번 작업에서 새로 생성하지 않았다.

### 3-B.2. 기존 Network Input 및 검증 범위

| 대상 | 대역 / 상태 | 근거와 한계 |
|---|---|---|
| 학원 LAN | `10.1.93.0/24` | 기존 자료에 기록. 다른 팀과 공유하므로 전체를 VPN 허용 대상으로 삼지 않음 |
| On-Prem Private Network | `192.168.51.0/24` ~ `192.168.54.0/24` | 승인 시작 문서 및 팀 사전 점검 기록 |
| 1차 Kubernetes Pod | `10.244.0.0/16` | 팀 사전 점검 기록. 이번에 Runtime 재조회하지 않음 |
| 1차 Kubernetes Service | `10.96.0.0/12` | 팀 사전 점검 기록. 이번에 Runtime 재조회하지 않음 |
| Harbor Docker Bridge | `172.17.0.0/16`, `172.18.0.0/16` | 팀 사전 점검 기록. 모든 Docker/VM 대역을 조사한 것은 아님 |
| WireGuard PoC | 양방향 통신·TCP 3306·원본 IP 보존·MTU 등 성공 기록 | `00_PROJECT_STARTING_POINT.md` §30.1. 전체 최종 경로·HA 검증을 뜻하지 않음 |
| Demo OCP / 기타 VM·팀원 접속망 | 미확인 | 실제 연결 대상이면 최종 IPAM에 추가 |

이전 팀 초안의 시험 예정 표기는 이후 승인 문서의 PoC 성공 기록으로 대체하여 판단한다. `192.168.50~53` 표기와 초안의 EKS/kubeadm 배치는 현재 상위 기준으로 사용하지 않는다.

### 3-B.3. Region / VPC — 작업 전제 승인

**기록 ID:** PH2-3B-IPAM  
**승인일:** 2026-10-01 KST  
**승인 범위:** §3-B.3~6의 Region·VPC·IPAM·Subnet 안. 후속 설계의 작업 전제로 승인되었으며 3단계 전체 검토에서 재검토 가능. 실제 Account·Runtime 검증은 별도.

| 항목 | 승인된 작업 전제 |
|---|---|
| AWS Region | 서울 `ap-northeast-2` |
| Project VPC | Terraform이 생성·관리하는 전용 VPC 1개 |
| AZ | 선택한 Region의 3개 AZ. 실제 AZ ID·Instance 가용성 확인 후 매핑 |
| ROSA 배치 | 위 VPC와 준비한 Subnet을 사용하는 기존 VPC 설치 방식 |
| DB / Redis | 같은 VPC의 별도 Data Private Subnet Group |

서울 권고는 국내 강의실·팀 접속 동선과 일치하는 설계 판단이다. 다른 Region 대비 RTT·가격 우위를 실제 측정하거나 계산했다는 의미는 아니다. 서울과 도쿄 등 ROSA Classic 지원 Region을 대안으로 검토할 수 있으며, Account 제약·가용성·비용에 따라 재검토한다.

VPC 1개안은 ROSA ↔ RDS/Redis 통신과 Hybrid Route를 단순하게 한다. 여러 VPC는 권한·라우팅 경계를 더 나눌 수 있지만 Peering 등 연결 설계와 검증이 추가되므로 현재 작업 전제에서는 우선 채택하지 않는다.

VPC / Subnet은 `foundation`, ROSA Cluster Lifecycle은 `rosa`에서 관리하는 상위 State 경계를 따른다. ROSA 삭제 시 RDS·Redis·VPC·Hybrid 기반을 함께 삭제하는 의존성을 만들지 않는다. 유지 State의 자원도 잔존 비용을 별도로 계산한다.

### 3-B.4. CIDR 후보 비교 — 작업 전제 승인 근거

| 후보 | 장점 | 검토 부담 |
|---|---|---|
| 팀 초안 `172.20.0.0/16` | 충분한 주소 공간 | 실제 Docker/VM 대역·주소 풀 및 vRouter NAT 예외 검토 필요 |
| 팀 통합 초안 `192.168.60.0/22` | 기존 NAT 제외 정책과 맞출 수 있음 | 초안의 2-AZ·4개 /24 배치는 현재 3-AZ 요구에 맞지 않음. /22 자체가 ROSA에서 불가능하다는 뜻은 아님 |
| **`192.168.64.0/20`** | 알려진 대역과 비중복. /24 16개 중 9개 배치 후 7개 예비 가능 | 모든 접속망 충돌 여부 및 최종 NAT 규칙 확인 필요 |
| 대체 `10.60.0.0/16` | 192.168 계열의 새 충돌이 발견될 경우 대안 | 알려지지 않은 10.x 연결망과 NAT 예외 검토 필요 |

승인된 작업 전제는 `192.168.64.0/20`이다. 기존 NAT 설정과의 호환성은 선택 근거 중 하나지만, 주소 선택만으로 원본 IP 보존을 보장하지 않는다. 전체 경로의 NAT/Forward/Route 정책과 실제 수신 IP를 확인한다.

### 3-B.5. 전체 IPAM — 작업 전제 승인

| 역할 | CIDR | 설명 |
|---|---|---|
| AWS VPC | `192.168.64.0/20` | `192.168.64.0` ~ `192.168.79.255` |
| ROSA Machine | `192.168.64.0/20` | VPC/Node 주소 범위를 포함. VPC와 동일한 값은 의도된 관계 |
| ROSA Pod | `10.128.0.0/14` | 공식 기본값을 작업 전제로 사용 |
| ROSA Service | `10.240.0.0/16` | 기존 Service·Pod 대역 및 알려진 Docker 대역과 구분 |
| WireGuard Tunnel | `10.200.0.0/30` | AWS `.1`, On-Prem `.2`를 작업 전제로 사용 |

ROSA Service 기본값 `172.30.0.0/16`도 검토했으나, 승인된 작업 전제는 기존 Docker 주소 공간과 구분하기 위해 사용자 지정 대역을 사용한다. 기본값과 현재 확인된 Docker Bridge 사이에 충돌이 발견되었다는 주장은 아니다. 실제 Docker 주소 풀·기타 OCP 대역을 확인한다.

Machine CIDR과 VPC, VPC와 소속 Subnet의 포함 관계를 충돌로 오판하지 않는다. 반면 독립 Network 역할의 주소 공간은 이 프로젝트의 상위 IPAM 원칙에 따라 중복을 피한다.

### 3-B.6. Subnet 배치 — 작업 전제 승인

AZ-A/B/C는 역할 식별자이며 실제 `ap-northeast-2a` 등의 매핑을 확정한 이름이 아니다.

| 역할 | AZ-A | AZ-B | AZ-C |
|---|---|---|---|
| Public | `192.168.64.0/24` | `192.168.65.0/24` | `192.168.66.0/24` |
| ROSA Private | `192.168.67.0/24` | `192.168.68.0/24` | `192.168.69.0/24` |
| Data Private | `192.168.70.0/24` | `192.168.71.0/24` | `192.168.72.0/24` |

`192.168.73.0/24` ~ `192.168.79.0/24`의 7개 /24 블록은 미할당 예비 주소로 남긴다.

Public 3 + ROSA Private 3은 일반 non-PrivateLink Classic Multi-AZ 구성을 고려한 안이다. Data Private 3은 ROSA 설치의 추가 필수조건이 아니라 Route·관리 경계·Lifecycle을 구분하기 위한 승인된 팀 설계 전제다. Cluster Privacy / PrivateLink 선택에서 더 적합한 구성이 나오면 배치를 함께 재검토한다.

Public Subnet이라는 이유만으로 모든 Resource에 Public IP를 할당하지 않는다. VPN EC2는 Public 종단점 역할을 수행하고, ROSA Node와 RDS/Redis는 Private에 배치하는 안이다. Public API와 기본 Public Ingress를 사용하는 작업 전제는 §3-B.8에서 승인되었다.

AWS의 일반 IPv4 Subnet 예약 주소 5개를 고려하면 /24당 사용 가능한 주소는 251개다. Node, LB, ENI, Endpoint 및 Upgrade 여유를 최종 Sizing에 반영한다.

Data Subnet Group에 3개 AZ를 제공한다는 사실이 RDS 3개 DB Instance 또는 Redis 3개 Node를 생성한다는 의미는 아니다. 상위 Architecture의 RDS Multi-AZ DB instance와 Redis Primary+Replica 모델을 유지한다. 실제 배치 AZ는 서비스 설정·가용성 확인 후 결정한다.

### 3-B.7. 라우팅 범위와 다음 설계 Input

On-Prem ↔ AWS에서는 필요한 Host / Subnet을 정해 Route·WireGuard AllowedIPs·Firewall·Security Group을 각각 검토한다. 허용 범위를 먼저 학원 LAN 전체 또는 모든 Kubernetes Pod/Service 대역으로 확대하지 않는다.

이번 IPAM 표에 Pod / Service CIDR이 있다는 사실이 해당 대역의 Hybrid 직접 Routing을 승인한 것은 아니다. ClusterIP는 일반 VM 사설 IP와 동일하게 접근 가능한 주소로 취급하지 않는다. 관리·검증 연결은 채택한 API/Route/Endpoint와 필요 Host를 기준으로 한다. NAT가 적용되는 Pod Egress는 정책 판단에 사용되는 실제 Source IP를 측정한다.

AWS Egress / DNS가 학원 Gateway를 필수 의존성으로 갖지 않도록 한다. API·User Ingress·NAT/Endpoint·DNS의 승인된 작업 전제는 §3-B.8에 기록한다. Route/SG/Firewall·Gateway 복구의 승인된 작업 전제는 §3-B.9에 기록한다.

현재 공식 AWS 문서에는 Regional NAT Gateway도 있으므로, NAT 비교를 Zonal 1개 또는 AZ별 3개에 한정하지 않는다. Region·ROSA·고정할 Terraform Provider 지원 및 AZ별 과금·운영시간을 확인한 뒤 판단한다. Regional Resource ID가 하나라는 사실을 시간당 비용이 AZ 한 개분이라는 뜻으로 해석하지 않는다.

### 3-B.8. API / User Ingress / Egress / DNS — 작업 전제 승인

**기록 ID:** PH2-3B-ACCESS-EGRESS-DNS  
**승인일:** 2026-10-01 KST  
**상태:** 아래 다섯 가지를 Route·SG·Gateway 복구 설계의 작업 전제로 사용자 승인. 3단계 전체 검토 전이며 Runtime 검증과 구분한다.

1. Public API, non-PrivateLink.
2. 기본 Public Ingress + HTTPS Route, 첫 통합 검증은 기본 도메인·인증서.
3. AZ별 Zonal Public NAT Gateway 3개, 실행시간·삭제/재생성 및 Cost Gate 검토.
4. S3 Gateway Endpoint 우선, 초기 ECR API·Registry는 NAT. 유료 Interface Endpoint는 필요 확인 후 비교.
5. AWS 기본 DNS, Hybrid 사설 DNS는 실제 필요에 따라 확장.

다음 비교표는 선택 근거를 보존한다. 미확인 입력과 후속 검토 사항까지 모두 완료되었다는 승인은 아니다.

#### 3-B.8.1 검토 전제와 기존 논의

상위 Architecture는 ROSA Classic Multi-AZ, Cloud Primary, Private Data Service 및 Cloud 정상 서비스의 On-Prem 비의존성을 정했다. API Public/Private, Ingress, NAT 수량·Lifecycle, DNS는 상세설계 대상으로 남겼다. 이전 시작 문서의 HCP Worker↔Control Plane PrivateLink 설명을 Classic의 Private API 승인으로 가져오지 않는다. 제안 검토 당시 제공된 기준 자료에서 별도의 Public/Private API 팀 합의는 확인되지 않았고, 이후 Public API 안이 작업 전제로 승인됐다. 추가 팀 합의가 제시되면 비교에 반영한다.

아래는 주요 대안 비교이며 가능한 모든 제품·조합을 열거한 것은 아니다. Account 조회, CLI Plan/Apply, 실제 Route·인증·DNS·장애 시험은 수행하지 않았다.

#### 3-B.8.2 ROSA API — Public 작업 전제

| 후보 | 장점 | 비용·운영·노출의 부담 | 판단 |
|---|---|---|---|
| Public API + Public 기본 Ingress, non-PrivateLink | 팀원 관리·사용자 접속이 WireGuard와 분리됨. 현재 Public/Private Subnet 배치와 맞음 | API와 Console/OAuth 접근점이 인터넷에 존재. 인증·최소권한·Token 관리 필수 | 우선 권고 |
| Private API + Private 기본 Ingress, PrivateLink | API 네트워크 노출 축소 | 팀원 사설 접근·DNS가 필요. 일반 사용자 공개 서비스에 별도 Ingress 구성이 필요 | 현재 우선안 아님 |
| Private API + 별도 Public Ingress 조합 | 관리 API는 사설로 제한하면서 사용자 서비스를 공개 가능 | 선택 Version·지원 절차·추가 Ingress 및 LB·DNS·비용·별도 관리 복구 경로 검증 필요 | 보안 요구가 강화되면 재검토 |

현재 STS 설치 문서는 Public 또는 AWS PrivateLink Cluster를 지원하고 일반 Private non-PrivateLink 구성을 지원하지 않는다고 명시한다. 기본 생성 화면에서 Private 선택은 API와 Application Routes를 사설로 두며 기존 VPC·PrivateLink 선택을 동반한다. 따라서 단순 Private 설정만으로 Public 사용자 서비스를 완성한다고 가정하지 않는다.

공식 STS 생성 절차는 생성 후 API Public/Private 전환 불가를 명시한다. 선택 Version·RHCS 입력을 확인하고 첫 Cluster 생성 전에 이 결정을 다시 점검한다. 나중에 비용 없이 설정 하나로 바꿀 수 있는 선택으로 취급하지 않는다.

Public은 네트워크 접근성의 뜻이다. 관리 작업은 신뢰할 TLS·IDP 인증·RBAC를 거치며, 비인증 사용자에게 보호된 자원 조회·변경을 허용하지 않는다. IDP·권한·Token 만료/회수는 3-C에서 설계한다. API Source CIDR 제한은 지원되는 관리 방법을 확인하기 전 적용 가능하다고 약속하지 않는다. 추가 SG의 허용 규칙만으로 기존 허용 범위를 축소할 수 있다고 가정하지 않는다.

ROSA Node에 Public IP를 주지 않고 직접 Public SSH를 관리 경로로 삼지 않는다. Managed Control Plane OS·etcd를 임의 변경하는 접근도 포함하지 않는다. VPN EC2의 SSM 관리 후보는 3-C에서 Instance Role·Agent·HTTPS Egress를 확인한다.

#### 3-B.8.3 사용자 Ingress / TLS — 기본 Public Route 작업 전제

사용자 요청은 HTTPS → AWS Ingress LB → OpenShift Ingress/Route → Service → Pod로 처리한다. 게임 WebSocket은 WSS를 사용하고 Route Timeout, 재접속 및 연결 유지 동작을 3-E·3-G에서 검증한다.

| 후보 | 효과 | 현재 판단 |
|---|---|---|
| ROSA 기본 Public Ingress + HTTPS Route | 기본 도메인·제공된 신뢰 인증서로 첫 통합 검증 가능 | 권고 |
| 사용자 지정 도메인 + Route | 시연 주소 유지·표현 개선. DNS와 일치하는 인증서·갱신 소유자 필요 | 후속 선택 사항 |
| 별도 ALB/WAF/CDN 또는 서비스별 LB | 특정 보안·캐시·프로토콜 요구 대응 | 요구가 확인될 때 비교. 초기 기본 구성에 추가하지 않음 |

ROSA는 기본 Route Hostname과 Console, API에 필요한 외부 TLS 인증서를 제공한다. 사용자 지정 이름으로 CNAME을 만들었다는 사실만으로 기본 Wildcard 인증서가 새 이름까지 보호하지 않는다. 실제 TLS 종료 지점과 해당 이름의 인증서·갱신 방법을 함께 정한다. 기존 개인 도메인을 자동으로 프로젝트 도메인으로 지정하거나 DNS를 변경하지 않는다.

게임 Route 공개와 관리 UI 접근 권한을 분리한다. Public 기본 Ingress로 노출되는 Console/OAuth 및 기타 관리 Route는 인증·권한 검증 대상이다. FE/BE Host·Path, Same-Origin/CORS, TLS Edge/Re-encrypt 선택 및 Service Port는 3-E에서 애플리케이션 통신과 맞춰 결정한다. 2026-10-01 사용자 동의에 따라 3-E번 서비스 연결 문서의 3-E-1 같은 Host·Path 분기·Edge TLS·환경별 설정·Pod 연결 처리를 후속 설계를 위한 작업 전제로 승인받았다. 실제 경로·Port·Route 적용·TLS 검증은 확인 전이며 3-E-2 인증·재접속·업무 상태 규약으로 연결한다.

#### 3-B.8.4 Egress — AZ별 Zonal Public NAT Gateway 3개 작업 전제

| 후보 | 장점 | 부담 / 장애 영향 | 판단 |
|---|---|---|---|
| Zonal NAT 1개 공유 | 시간당 자원 수 감소 | NAT가 있는 AZ 장애가 다른 AZ의 외부 통신·새 이미지 Pull에도 영향. Cross-AZ 비용 가능 | HA 목표의 기본안으로 권고하지 않음 |
| AZ별 Zonal NAT 3개 | 같은 AZ의 NAT를 사용해 Egress 장애 범위를 분리. Classic VPC 구성과 검증 동선이 명확함 | 3개 시간당 과금 및 Public IPv4 비용 | 우선 권고 |
| Regional NAT | 다중 AZ 운영을 관리형 Regional Resource로 구성 | AZ별 시간당 과금. 서울·ROSA 설치 경로·고정 Provider 지원 및 AZ 확장 동작 확인 필요 | 확인 후 재검토 가능한 대안 |
| NAT Instance 또는 VPN EC2 겸용 | 일부 비용 조정 가능 | 처리량·패치·HA·Route 운영 부담. 단일 VPN에 Cloud 정상 Egress를 의존시킬 위험 | 현재 기본안 아님 |

Public A/B/C에 각각 NAT-A/B/C를 두고 Public Route Table은 IGW로, ROSA Private A/B/C의 인터넷 기본 경로는 각각 같은 AZ의 NAT로 연결하는 안이다. VPC Local 경로, 필요한 Hybrid 사설 경로 및 S3 Prefix 경로는 별도로 유지한다. Data Private에는 RDS/Redis 배치만을 이유로 NAT 기본 경로를 추가하지 않는다. Data Subnet에 실제 실행 주체를 배치하면 그 요구를 다시 검토한다.

이는 승인된 Egress 작업 전제다. NAT 3개가 모든 AZ 장애에서 애플리케이션 HA를 보장하는 것은 아니며 Pod 배치, Ingress, DB/Redis Failover 및 Client 재접속을 함께 검증한다. NAT Gateway에는 SG를 붙일 수 없으므로 Node/Workload의 지원되는 정책과 Subnet/Route 경계를 사용한다.

**비용·Lifecycle:** NAT는 foundation 소유의 재생성 가능 자원 후보로 유지한다. ROSA 실행 Window와 맞춰 사용하되, Cluster 삭제만으로 무조건 NAT를 삭제하지 않는다. 남은 Backup/Export 및 다른 실행 주체의 의존성이 없음을 확인한 뒤 삭제하고 다음 설치 전에 재생성·Route 연결을 확인한다. NAT를 EC2처럼 Stop해서 과금 중단하는 것으로 설명하지 않는다. EIP 유지·반납과 재생성 시 IP 변경 영향도 별도 기록한다. 자동화 구현·정확한 Toggle/모듈 경계는 3-F에서 검토한다.

NAT Hour 비용의 비교는 1개안 `서울 단가 × H`, 3개안 `서울 단가 × 3H`를 기본으로 하고, 처리량·전송·Public IPv4를 더한다. H는 실제 생성부터 삭제까지 과금시간이며 단순 작업자의 접속시간이 아니다. 예를 들어 총 실행시간 40시간은 3개안에서 120 NAT-hours가 된다. Regional도 3개 AZ를 40시간 지원하면 120 NAT-hours이며 Resource ID 한 개를 40 NAT-hours로 계산하지 않는다.

3개 NAT의 기본 EIP + VPN EIP는 최소 4개이며, ROSA LB 등의 주소는 추가 계산 대상이다. 서울 최신 요율과 전체 ROSA·RDS·Redis·Storage 비용은 아직 산출하지 않았고, $500 한도 충족을 주장하지 않는다. 첫 Full Apply 전에 시간계획을 포함해 Cost Gate를 통과해야 한다. 초과가 확인되면 실행시간·구성 변경 후보를 제시하고 재승인한다.

#### 3-B.8.5 Endpoint — S3 Gateway만 초기 기본안

- VPC 내부의 같은 Region S3 접근은 S3 Gateway Endpoint를 사용한다. 사용 Route Table 및 Endpoint/Bucket/IAM Policy는 실제 호출 주체와 Bucket을 기준으로 설계한다. Gateway Endpoint 자체에는 시간당·처리량 추가 요금이 없다. S3 저장·요청·전송 등 서비스 비용까지 무료라는 뜻은 아니다.
- ECR API·Registry는 초기 NAT 경로를 사용하고, 같은 Region의 이미지 Layer S3 접근은 Gateway Endpoint 경로를 사용한다. Endpoint Policy가 ECR Layer Bucket 또는 ROSA가 필요로 하는 S3 접근을 막지 않도록 검증한다.
- 유료 ECR `ecr.api`·`ecr.dkr` Interface Endpoint는 초기 필수 자원으로 추가하지 않는다. 필요 시 두 Endpoint와 S3 Layer 경로·Private DNS·SG·AZ별 비용을 함께 비교한다. 이 구성만으로 Quay 등 외부 Registry, GitHub, Red Hat 및 모든 AWS API의 NAT 요구가 없어지는 것은 아니다.
- On-Prem은 VPN을 통해 S3 Gateway Endpoint를 사용할 수 없다. Backup 동기화는 별도 승인된 IAM 주체로 Public S3 Endpoint에 HTTPS 접근하는 안을 유지한다. 이는 Bucket Public 공개를 뜻하지 않는다. 무조건 VPCE만 허용하는 Bucket Policy로 정당한 On-Prem Backup 경로를 막지 않도록 3-C·Data 설계와 연결한다.
- On-Prem에서 S3에 사설 접근해야 하는 새 요구가 생기면 S3 Interface Endpoint·DNS·비용을 별도 비교한다.

#### 3-B.8.6 DNS — AWS 기본 DNS, Hybrid 사설 해석은 필요 조건에 따라 확장

| 범위 | 권고 | 확인할 조건 |
|---|---|---|
| Cloud Runtime | VPC AmazonProvidedDNS, DNS Support/Hostnames 활성화 | ROSA 설치·Private Hosted Zone·Endpoint 이름 해석 |
| Public API / Route / AWS Service | 사용 위치의 정상 DNS로 해당 FQDN 조회 | 관리·사용자·Backup 각각의 실제 Hostname/TLS |
| RDS / Redis | 서비스 제공 FQDN을 사용. Failover IP를 설정/hosts에 고정하지 않음 | On-Prem Resolver에서도 실제 Endpoint의 응답을 확인. 사설 IP 해석과 접속 Route/SG는 별도 |
| Hybrid 전용 사설 이름 | 필요 시 조건부 Forwarder + Route 53 Resolver Inbound Endpoint 검토 | 대상 Zone·최소 다중 AZ 주소·VPN Route·TCP/UDP 53·비용 |
| On-Prem Recovery | 로컬 DNS/설정·로컬 DB/Redis Endpoint로 복구 실행 가능 | AWS 장애 선언 후 AWS DNS·API 조회를 필수 단계로 두지 않음 |

기본안에서는 추가 Public Hosted Zone, 팀 소유 Private Hosted Zone, Resolver Inbound/Outbound Endpoint를 선제 생성하지 않는다. ROSA 플랫폼이 필요로 관리하는 DNS Resource의 생성을 금지한다는 의미는 아니다. 사용자 지정 Public 도메인이 필요하면 현재 권한이 있는 Authoritative DNS Provider를 확인한 뒤 DNS 소유자를 정한다.

On-Prem에서 VPC 내부 Resolver 주소(VPC +2 등)로 직접 Forward하는 방식은 채택하지 않는다. AWS 사설 Zone을 조회해야 하는 경우 공식 지원 Inbound Endpoint 경로를 사용한다. 모든 AWS Private Endpoint 이름이 외부 DNS에서 해석된다고 가정하지 않는다. 실제 RDS/Redis 이름이 기존 Resolver에서 적절히 해석되면 추가 유료 Resolver Endpoint 없이 그 경로를 검증한다.

Cloud DNS를 On-Prem DNS로 일괄 Forward하지 않는다. 필요 도메인의 조건부 전달을 검토하더라도 정상 Cloud Runtime의 DNS·User Ingress·Egress 경로는 Hybrid Tunnel과 독립시킨다.

#### 3-B.8.7 소유권과 검증 기준

| 대상 | 설계/관리 경계 |
|---|---|
| VPC / IGW / NAT / Endpoint / 팀 소유 Route·SG | Terraform foundation. RDS/Redis 등 각 서비스 경계와 연결 |
| Cluster Privacy / 기존 VPC·Subnet 입력 | Terraform/RHCS rosa의 지원 입력. 첫 생성 전 검토 |
| ROSA가 관리하는 API/Ingress LB·SG·DNS | ROSA/플랫폼 관리 경계. foundation이 임의 Import/중복 관리하지 않음 |
| Application Route / Service / NetworkPolicy | 승인된 GitOps 경계. 플랫폼 설정과의 충돌 방지 |
| 외부 Public DNS / 인증서 | 사용자 지정 도메인 채택 시 명시할 소유자. GitOps Secret 및 갱신은 3-C·3-E 연결 |

필수 검증 후보는 다음과 같다. 모두 아직 실행 전이다.

1. WireGuard 중단 상태에서도 외부 팀원 API 인증·허용된 관리 작업, 사용자 HTTPS/WSS 및 Cloud Runtime이 정상인지 확인한다. On-Prem CI 중단에 따른 신규 배포 불가와 기존 Cloud 서비스 장애를 구분한다.
2. API 비인증·권한 부족 주체는 보호된 작업에 접근하지 못하고 허용된 주체만 작업할 수 있어야 한다. Console/OAuth·Token 회수도 검증한다.
3. 각 AZ에서 새 이미지 Pull·필수 Red Hat/GitHub/AWS Egress 및 S3 접근을 확인한다. 기존 이미지 Cache 성공만으로 Egress를 PASS 처리하지 않는다.
4. HTTPS 인증서 이름·신뢰·HTTP 처리 정책, WSS 연결 유지·재접속 및 Route Timeout을 확인한다.
5. RDS/Redis Endpoint 재해석·Failover 후 연결 복구를 검증한다. On-Prem에서도 이름 해석과 사설 Route/SG를 각각 확인한다.
6. 지원되는 시험 범위에서 AZ별 Egress 의존성과 NAT 재생성·Route 복구를 확인한다. Managed Control Plane 강제 종료/OS 변경으로 시험하지 않는다.
7. On-Prem S3 HTTPS 다운로드와 VPC S3 Gateway 접근을 별도로 검증한다. AWS 장애 선언 전에 Backup·필요 이미지·설정·Secret을 로컬에 확보하고 실제 복구를 검증한다.

**영향 영역:** 3-C 인증·Secret, Data Backup/Recovery, 3-E Interface/TLS, 3-F Terraform/GitOps 및 비용 Lifecycle, 3-G Evidence, 3-H 시간계획.  
**재검토 조건:** Public API 노출을 수용하지 못하는 보안 요구, 사설 DNS/접근 장애, 지원 Version/Provider 제약, $500 초과, 일정상 구현·검증 불가 또는 상위 작업 전제와 충돌.  
**Issue / PR / Runtime Evidence:** 이번 제안에 대해 새로 생성·검증한 Runtime Evidence 없음.

### 3-B.9. Route / SG / Firewall / Gateway 복구 — 작업 전제 승인

**기록 ID:** PH2-3B-ROUTE-SG-RECOVERY  
**승인일:** 2026-10-01 KST  
**상태:** 다음 다섯 가지를 후속 설계의 작업 전제로 사용자 승인. 3단계 전체 검토 전이며 실제 적용·Runtime 검증과 구분한다.

1. 목적별 Route Table과 필요한 On-Prem Host /32부터 연결. RDS 이관·검증을 초기 Hybrid 용도 후보로 연결.
2. 사설 왕복 Route·NAT 예외·원본 IP 보존 및 Route/AllowedIPs/Port 정책의 분리.
3. RDS·Redis SG 분리, Gateway Forward 기본 차단, 초기 Default NACL 허용 동작 유지.
4. 변동 출구 IP를 고려한 UDP 51820 단일 Public 허용 예외. Keepalive 25초·MTU 1420 시작값 검증.
5. 재기동·설정 복원·IaC 재구축과 EIP/ENI/Route/Key의 각각 복원·업무 통신 검증.

실제 Host 주소·AZ·Source SG·Key 보관 방식·지원 Provider·작업 방법의 미확인 상태를 없애는 승인은 아니다. 아래 비교는 선택 근거를 보존한다.

#### 3-B.9.1 검토 전제·주요 대안

기존 PoC는 원본 사설 IP를 보존한 AWS→On-Prem TCP 3306 통신을 확인했지만, 최종 전용 Gateway·ROSA·RDS·전체 vRouter 경로와 재구축 검증은 남아 있다. 초기 실제 연결 목적은 On-Prem의 승인된 이관/검증 작업 Host→RDS를 우선 후보로 한다. 수행 주체·이관 방법·작업 시간은 3-C·3-D에서 확정하고, 결정 전에는 해당 규칙을 활성화하지 않는다.

| 비교 대상 | 권고 | 대안과 부담 |
|---|---|---|
| Hybrid 목적지/Source 범위 | 필요한 On-Prem Host /32부터 추가 | 필요한 전용 Subnet으로 확대 가능. 알려진 4개 /24 또는 학원 LAN 전체를 처음부터 광고하지 않음 |
| Routing / NAT | 사설 왕복 Routing + 원본 IP 보존 | Gateway SNAT는 왕복 설정을 단순화할 수 있지만 Host별 식별·DB 계정 조건·감사 경계를 변경하므로 기본안으로 채택하지 않음 |
| SG와 Subnet 방화벽 | 팀 소유 SG·Gateway Host Firewall 우선, 초기 NACL은 AWS 기본 허용 동작 유지 | Custom NACL은 Stateless 반환 Port·ROSA 필수 통신을 포함한 추가 검증 필요 |
| WireGuard 외부 접근 | 출구 IP 변동을 고려한 UDP 51820 단일 Public 허용 예외 | 학원 출구 IP의 완전한 관리 가능 목록이 확인되면 CIDR로 축소. 미확인 고정 /32로 묶으면 Roaming 실패 가능 |
| 단일 Gateway 복구 | 서비스 재기동 + IaC 재구축 + EIP/ENI/Route 복구 | 이중 Gateway/자동 경로 전환은 HA 추가 설계·비용·검증이 필요하며 승인된 초기 범위 밖 |

주요 대안을 비교한 것이며 모든 Network 제품·조합을 열거한 것은 아니다. 1차 Router 정책을 통째로 재작성하거나 변경 승인 없이 Source 식별 모델을 바꾸지 않는다.

#### 3-B.9.2 실제 입력 전에는 사용하지 않는 역할 변수

| 역할 | 값 / 결정 상태 |
|---|---|
| `ONPREM_JOB_HOSTS` | 이관·검증용 실제 VM 사설 IP들의 /32 목록. 미확인. 임의 VM/IP를 배정하지 않음 |
| `ONPREM_TARGETS` | Cloud→On-Prem 작업이 별도 승인될 때 추가할 대상 /32. 초기 비활성 |
| `AWS_DATA_CIDRS` | `192.168.70.0/24`, `192.168.71.0/24`, `192.168.72.0/24` |
| `AWS_EXECUTOR_CIDRS` | Cloud→On-Prem 작업이 필요할 때 실제 Cloud Source 확인 후 지정. ROSA Source가 Worker IP이면 해당 Private Subnet 범위 등을 비교 |
| AWS VPN Gateway | AZ-A Public의 `192.168.64.10` 고정 Private IP 후보 + ENI + 기존 승인된 EIP. 실제 AZ/주소 사용 가능 여부 확인 전 |
| On-Prem VPN Gateway | 실제 VM·주소·접속 Subnet·기본 Gateway 미확인. 각 vRouter에서 도달 가능해야 함 |
| RDS / Redis | 제공된 서비스 FQDN과 실제 설정 Port. DB 3306 / Redis 프로토콜 6379를 초기 설계 Port로 검토 |

이 표는 실행 가능한 Terraform 변수 파일이나 Host Inventory가 아니다. 값이 없는 역할을 전체 Subnet 또는 0.0.0.0/0으로 대체해 적용하지 않는다. `192.168.64.10`은 승인된 작업 전제의 VPC/Public Subnet 안에 둔 고정 주소 후보이며 아직 IP 할당 증거가 없다.

#### 3-B.9.3 AWS Route Table — 명시적 5개 작업 전제

| Route Table | 연결 Subnet | 기본 경로 및 추가 경로 |
|---|---|---|
| Public 공용 1개 | Public A/B/C | VPC `local`, `0.0.0.0/0 → IGW`. 외부 VPN UDP와 Public LB 경로 |
| ROSA-A | ROSA Private A | VPC `local`, `0.0.0.0/0 → NAT-A`, 같은 Region S3 Prefix → S3 Gateway Endpoint |
| ROSA-B | ROSA Private B | VPC `local`, `0.0.0.0/0 → NAT-B`, 같은 Region S3 Prefix → S3 Gateway Endpoint |
| ROSA-C | ROSA Private C | VPC `local`, `0.0.0.0/0 → NAT-C`, 같은 Region S3 Prefix → S3 Gateway Endpoint |
| Data 공용 1개 | Data Private A/B/C | VPC `local`만 기본. 승인된 On-Prem 작업 활성화 시 `ONPREM_JOB_HOSTS /32 → VPN ENI` 왕복 Route 추가. 인터넷 기본 Route 없음 |

VPC Main Route Table은 별도로 `local`만 유지하고 위 9개 Subnet을 명시적으로 연결한다. 표의 5개는 팀이 추가 관리할 Route Table 수이며 Main을 포함한 총수를 5개라고 주장하지 않는다. Public/Data는 같은 Route 정책을 공유하므로 Subnet 수와 Table 수를 기계적으로 일치시키지 않는다.

ROSA Route Table에는 초기 On-Prem Route를 넣지 않는다. Cloud 실행 주체→On-Prem 대상이 실제 Migration/진단 요구로 승인되면 필요한 `ONPREM_TARGETS /32 → VPN ENI`를 해당 실행 Subnet Table에만 추가한다. Data에는 On-Prem에서 시작한 DB 접속의 응답도 동일 Tunnel로 돌아가도록 /32 Route가 필요하다. Internet 기본 Route나 VPC `local`을 VPN ENI로 바꾸지 않는다.

S3 Endpoint는 실제 VPC S3 호출 주체의 Route Table에 연결한다. 초기 ROSA Table 3개를 우선하며, VPN Bootstrap 등이 S3에 접근할 경우 Public Table에도 연결할 필요를 검토한다. RDS/Redis만 있는 Data Table에는 실행 주체 요구 없이 Endpoint 경로를 추가하지 않는다.

Subnet 자동 LB 선택을 위한 ROSA 요구 Tag는 선택 Version의 공식 절차에 따라 Public/ROSA Private에 적용하고 설치 입력은 해당 Subnet만 전달한다. Data Subnet을 의도 없이 ROSA Node/Ingress 선택 대상으로 등록하지 않는다.

#### 3-B.9.4 On-Prem 왕복 Route / AllowedIPs

On-Prem Job Host → 해당 Host의 기존 vRouter → 전용 VPN Gateway → WireGuard → AWS VPN Gateway → RDS의 경로를 기준으로 한다. 같은 LAN에서 Job Host가 전용 VPN Gateway로 직접 Route할 수 있는 경우는 별도 경로로 기록하고 비대칭 왕복을 시험한다.

- 관련 vRouter는 `AWS_DATA_CIDRS`를 실제 전용 Gateway로 전달한다. AWS VPN Host 진단이 필요하면 해당 /32만 추가한다. Cloud 작업용 다른 사설 Source/목적지를 추가할 때 Route 범위를 함께 검토한다.
- 전용 Gateway는 AWS 범위를 `wg0`로 보내고, 실제 On-Prem Job Host에는 올바른 LAN/vRouter 경로를 가진다. 모든 On-Prem 사설망이 단일 인터페이스에서 직접 연결된다고 가정하지 않는다.
- AWS Gateway의 OS Route는 `ONPREM_JOB_HOSTS /32`를 `wg0`로 보낸다. AWS VPC 경로와 외부 EIP 통신은 ENI의 기존 VPC Gateway 경로를 유지한다.
- AWS Peer의 AllowedIPs는 `10.200.0.2/32 + ONPREM_JOB_HOSTS /32`. On-Prem Peer는 `10.200.0.1/32 + AWS_DATA_CIDRS`를 초기 범위로 한다. AWS VPN Private IP의 진단은 그 /32를 명시적으로 추가한다.
- Cloud→On-Prem 작업이 추가되면 AWS Peer에 On-Prem 대상 /32, On-Prem Peer에 실제 AWS Source 대역도 추가한다. AllowedIPs는 송신 목적지 선택뿐 아니라 복호화 후 수신 Source 검사에 사용되므로 왕복 Source가 빠지면 Handshake만 성공하고 업무 통신은 실패할 수 있다.
- `0.0.0.0/0`, 학원 LAN, Kubernetes/ROSA Pod·Service CIDR을 AllowedIPs에 기본 등록하지 않는다. Peer 설정만으로 EC2/VPC/vRouter Route와 Port 방화벽을 대신하지 않는다.

AWS VPN EC2/사용 ENI의 Source/Destination Check를 끄고, 양 Gateway에서 IPv4 Forwarding을 켠다. EC2가 자신이 아닌 주소의 Routing을 수행하기 위한 설정이다. 관련 인터페이스의 Reverse Path 검사도 실제 왕복 Route와 확인하되, 문제를 가정해 모든 장비의 검사를 일괄 해제하지 않는다.

On-Prem vRouter와 두 Gateway에서 이 사설 경로를 기존 Masquerade/SNAT 대상에서 제외한다. 기존 학원 인터넷 NAT는 유지한다. Cloud Pod의 VPC 밖 Egress Source가 Node IP로 바뀌는 OpenShift 동작과 Hybrid Gateway의 추가 SNAT를 구분한다. 수신지에 보이는 실제 Source로 Allowlist와 계정 조건을 검증하며, 예상과 다르면 Pod 대역을 즉시 확대하지 않고 지원되는 Source 경로·정책을 재검토한다.

#### 3-B.9.5 허용 통신 Matrix — 요청 시작 방향 기준

| ID | 시작 주체 → 목적지 | Protocol / Port | 경로·허용 조건 |
|---|---|---|---|
| NET-01 | Internet 사용자 → Public Ingress | TCP 443, 필요 시 80→HTTPS 처리 | 승인된 Public Route. App 인증은 별도 |
| NET-02 | 팀 관리 주체 → Public API / Console·OAuth | TCP 6443 / 443 | Public 경로 + TLS·IDP·RBAC. ROSA Managed 설정 유지 |
| NET-03 | Application Worker → RDS | TCP 3306 | VPC Local. 실제 Worker Source SG 참조 + DB 계정/TLS + Workload 정책 |
| NET-04 | Application Worker → Redis | TCP 6379, 최종 Port 확인 | VPC Local. 실제 Worker Source SG 참조 + Redis 인증/TLS + Workload 정책 |
| NET-05 | On-Prem 전용 Gateway → AWS VPN EIP | UDP 51820 | On-Prem 선제 연결, Key 인증, NAT Mapping 유지 |
| NET-06 | 승인된 On-Prem Job Host /32 → RDS | TCP 3306 | Migration/검증 작업이 정해진 경우만 활성화. 양 Route·AllowedIPs·Forward Firewall·RDS SG·DB 권한 |
| NET-07 | 승인된 Cloud 실행 주체 → On-Prem DB/작업 대상 | 예: TCP 3306 | 초기 비활성. Data 설계에서 필요할 때 Host·Source·Port·기간·왕복 경로 추가 검토 |
| NET-08 | On-Prem Backup/CI → S3·ECR·GitHub·AWS API | 주로 TCP 443 | 기존 Internet HTTPS. Tunnel 전체 경로에 넣지 않음. Git SSH 등 추가 Protocol은 실제 사용 시 별도 |
| NET-09 | ROSA → 필수 외부 Registry / Red Hat / GitHub / AWS API | 공식 Platform 요구 및 Workload 요구 | 승인된 AZ별 NAT / S3 경로. 임의 443-only Platform 제한으로 설치·운영을 방해하지 않음 |
| NET-10 | 관리 주체 → VPN EC2 | SSM API/Agent의 HTTPS | 3-C에서 IAM·Agent 확인. Public TCP 22 허용은 기본에 포함하지 않음 |

표는 신규 요청의 허용 방향이다. TCP 응답의 Ephemeral Port를 반대 방향의 신규 DB 접속 허용으로 해석하지 않는다. On-Prem→Redis, Cloud Runtime→On-Prem DB/Harbor, 임의 Host→Node SSH를 기본 허용하지 않는다. Redis 외부 관리가 실제 필요하면 담당 Host /32·작업 기간·인증·읽기/변경 권한을 추가 검토한다.

#### 3-B.9.6 SG / Host Firewall / NACL 경계

**RDS와 Redis SG는 분리한다.** 정상 Cloud Source는 실제 Worker Machine Pool의 ENI에 연결된 SG를 식별해 참조하는 안이다. Node 교체에 취약한 개별 Worker IP 고정이나 VPC 전체 CIDR 허용을 기본으로 삼지 않는다. Control Plane·Infra Node에 동일 SG가 붙는다면 Worker만 식별한 것이라고 주장하지 않고 지원되는 Worker 구분 방법을 검토한다.

SG가 Worker를 구분해도 특정 Backend Pod만 구분하지는 않는다. Workload NetworkPolicy·DB/Redis 계정으로 애플리케이션 권한을 좁힌다. OVN-Kubernetes에서 실제 외부 접속 Source와 대상 ENI SG가 예상과 맞는지 확인하고, 맞지 않으면 지원되는 Source SG 또는 필요한 Source CIDR 대안을 재검토한다. 이 검증 전 SG 참조 방식의 Runtime PASS를 주장하지 않는다.

Hybrid RDS Source는 `ONPREM_JOB_HOSTS /32`다. 원본 IP를 보존하는 VPN 경로에서 VPN EC2 SG를 Source로 참조한 규칙이 On-Prem 원본 Host까지 허용한다고 가정하지 않는다. AWS 중간 Routing Appliance를 경유하는 흐름에서는 실제 IP/CIDR 기준 정책이 필요하다는 SG 제약도 고려한다.

**VPN SG/Firewall의 외부·내부 Packet을 구분한다.** 외부는 Key로 인증되는 UDP 51820이고, 복호화 후 내부는 On-Prem Job Host→Data CIDR TCP 3306 등 작업 Matrix다. 외부 UDP 허용만으로 내부의 모든 사설 통신을 허용하지 않는다.

- AWS VPN SG Public Inbound는 UDP 51820만 `0.0.0.0/0`으로 허용하는 예외를 제안한다. 학원 출구 Public IP가 변동하는 현재 입력에 맞춘 안이며 모든 Protocol/Port Public 허용이 아니다. 출구 CIDR 관리 가능 범위가 확인되면 축소한다. 호스트의 UDP Listener도 WireGuard에 한정한다.
- SG Outbound와 Gateway Forward Firewall은 활성 작업의 Data CIDR/Port 및 운영에 필요한 HTTPS 등을 기준으로 구성한다. Cloud→On-Prem 작업은 AWS ENI에 들어오는 Plaintext Source/Port 규칙도 별도로 필요하다. UDP 응답은 추적 상태와 실제 NAT Mapping을 확인하며 학원 NAT 외부 Source Port가 항상 51820이라고 가정하지 않는다.
- 양 Gateway Host Firewall은 신규 Forward 기본 차단, 허용된 Source/Destination/Port·방향만 추가하고 Established/Related 응답을 허용하는 안이다. 실제 Nftables/Firewalld 등 사용 도구와 선언적 관리자는 3-F에서 하나로 정한다. ICMP PMTU 오류 처리를 막지 않으며 장애 진단 Echo는 필요한 Source만 허용한다.
- 초기 NACL은 AWS Default NACL의 허용 동작을 유지하고 SG·Host Firewall을 먼저 검증한다. Default NACL이 업무 접근을 세밀하게 제한한다는 의미는 아니다. Custom NACL을 채택하면 Stateless 응답 Port·NAT·LB·ROSA 요구를 포함해 재검토한다.
- ROSA Managed SG의 필수 Rule을 임의 삭제하거나 추가 SG로 기존 허용을 차단했다고 주장하지 않는다. 공식 문서는 Platform Egress를 Firewall로 제어하는 구성을 PrivateLink Cluster로 제한하므로, 현재 non-PrivateLink 안에 임의 중앙 Firewall/Domain Allowlist를 추가하지 않는다. 팀 Gateway의 내부 Forward 제한과 애플리케이션 정책은 이 Platform Egress 변경과 구분한다.
- SG/NACL로 AmazonProvidedDNS 자체를 차단할 수 있다고 가정하지 않는다. 별도 DNS Firewall은 새 요구가 확인될 때 비용·지원·정책을 비교한다.

DB/Redis Protocol Port의 실제 설정, TLS와 계정 방식은 3-C·3-D·3-E와 연결한다. 네트워크 접속 허용만으로 데이터 조회·변경 권한을 부여하지 않는다.

#### 3-B.9.7 Gateway 지속 설정과 소유권

On-Prem Peer에는 AWS EIP Endpoint와 `PersistentKeepalive = 25`를 시작값으로 권고한다. AWS Peer는 학원 주소를 고정 Endpoint로 묶지 않고 인증된 Peer의 최근 주소를 학습한다. MTU는 PoC의 `1420`을 시작값으로 사용하지만 최종 경로에서 대용량 전송·Fragment/PMTU·TCP 동작을 다시 확인한다. MSS 조정은 실제 문제 확인 후 적용한다.

| 자원/설정 | 작업 전제의 소유자 및 수명 |
|---|---|
| VPN EC2 / EIP / 팀 소유 SG / 전용 ENI / AWS Hybrid Route | Terraform foundation. ROSA 삭제와 독립 |
| VPN OS / WG / Sysctl / Host Firewall / On-Prem vRouter Route·NAT 예외 | infra의 Ansible 또는 승인된 Bootstrap 경계. 재기동 후 지속·멱등성 확인 |
| WireGuard Private Key 및 복원본 | 3-C에서 저장·주입·회수 경계 결정. Git/문서/TF Output·State에 평문을 넣지 않음 |
| RDS·Redis SG 본체와 On-Prem /32 Rule | foundation의 명시적 단일 소유자. 작업 활성화/종료 시 Rule 제어 |
| ROSA Worker SG를 참조하는 Data SG Rule | rosa Lifecycle과 함께 생성·삭제하는 Binding 후보. 팀 소유 Data SG의 Rule만 관리하며 Managed Worker SG를 변경하지 않음 |
| Application Route / NetworkPolicy | gitops의 승인된 경계. Platform과 중복 소유 금지 |

ROSA 의존 Binding은 foundation의 Data SG ID를 입력으로 받아 Cluster 생성 후 연결하고, Cluster 삭제 전에 해제하는 안이다. Worker SG 삭제를 막거나 재생성 후 낡은 SG ID를 남기지 않도록 3-F에서 실행 순서를 검증한다. 동일 Data SG Rule을 foundation과 rosa가 동시에 관리하지 않는다.

동일 Data SG의 규칙을 두 State에 나누어 소유할 때는 SG 본체의 inline ingress/egress와 별도 Rule Resource를 혼용하지 않는다. 본체는 foundation, 각 규칙은 명시적 Rule Resource의 단일 Owner로 관리하고, SG 전체 규칙 목록을 강제로 비우거나 다른 State의 규칙을 덮어쓰는 선언도 금지한다. foundation 재실행 전후 rosa Binding 유지, rosa Binding 해제 후 foundation 규칙 유지, 재생성 후 새 Worker SG 연결과 양쪽 정상 Plan을 IM-03/T19에서 확인한다. 실제 선택 Provider의 Resource Schema·삭제 의존성은 구현 Gate이며 이 문서만으로 동작을 검증한 것은 아니다. HashiCorp의 [SG 규칙 관리 주의사항](https://github.com/hashicorp/terraform-provider-aws/blob/main/website/docs/r/security_group.html.markdown)을 근거로 한다. 현재 승인된 bootstrap/foundation/rosa를 유지하며 별도 네 번째 State를 이번에 확정하지 않는다.

AWS Gateway는 AZ-A에 고정 Private IP를 가진 전용 ENI를 보존해 같은 AZ에서 재사용하는 안을 우선 비교한다. Primary ENI는 실행 중 임의 Detach할 수 없으므로 기존 Instance 제거·수명 옵션·새 Instance 연결을 Provider Plan에서 확인한다. ENI 수명과 EC2 수명을 분리했더라도 같은 AZ 제약은 남으며 AZ HA가 되지 않는다. 다른 AZ로 재구축하거나 새 ENI를 사용하면 관련 Route Target을 모두 갱신해야 한다.

실제 OS·Instance Type·Disk·SSM 가능 여부는 아직 미확인이다. 즉시 Server/Network 설정을 변경하지 않았다.

#### 3-B.9.8 단일 Gateway 복구 절차 — 수동 실행 가능한 IaC 복구

| 상황 | 초기 대응 | 복구 확인 |
|---|---|---|
| WG Service/설정 오류 | 최근 변경·로그 확인, 검증된 설정 복원 후 Service 재기동 | 양방향 업무 Probe, 원본 Source, 금지 통신 |
| AWS EC2/OS 손상 | foundation으로 Instance 재구축, ENI/EIP 재사용 또는 갱신, Key·설정 재주입 | Source/Destination Check, Forwarding, Route Target, Handshake·업무 통신 |
| On-Prem Gateway VM 손상 | 선언된 VM/OS/설정 절차로 재구축, 주소·vRouter Next Hop·Key 복원 | 관련 vRouter별 왕복 Route·NAT 예외·업무 통신 |
| 학원 출구 IP/Port 변경 | On-Prem의 새 선제 통신과 Keepalive, AWS의 인증 Peer Endpoint 학습 | 외부 UDP 허용 범위, 재접속·유휴 복귀. 항상 무중단 보장하지 않음 |
| AWS Gateway AZ 불가 | 임시 중단 수용 후 가용 AZ로 재구축할지 판단 | 새 ENI·Private IP·EIP 연결·모든 Hybrid Route·정책 갱신. 자동 AZ Failover 아님 |
| Key 유출/복원 불가 | Peer 차단·폐기, 새 Key Pair 주입·상대 Public Key 갱신 | 이전 Key 접속 거부, 새 Peer 업무 통신 |

복구 Runbook은 다음 순서로 실행하도록 구체화한다.

1. 작업 일시·장애 증상·영향 범위를 기록하고 Hybrid 사용 작업을 중지한다. 독립 경로에서 Cloud HTTPS/WSS·API·DB/Redis Runtime도 확인한다.
2. WG Service·최근 Handshake·전송 Counter, Outer UDP, OS Route·Forwarding·Firewall, ENI/SG를 순서대로 점검한다. Handshake 시간만으로 건강을 판정하지 않는다.
3. 서비스 재기동/검증 설정 복원으로 해결 가능한지 판단하고, 불가하면 한 종단점씩 재구축한다. 재구축 중 중복 IP·동일 Key 동시 운영을 피한다.
4. 안전하게 확보한 Key·OS 설정을 주입하고 부팅 후 자동 시작, Forwarding, Source/Destination Check, MTU·Keepalive를 확인한다. AWS Gateway 복구 절차는 고장난 Tunnel 자체를 필수 관리 경로로 삼지 않는다.
5. AWS EIP Association과 사설 Route Target ENI를 각각 확인한다. EIP가 같아도 ENI가 새로 생기면 Route 복구가 필요하다. On-Prem IP/Next Hop이 바뀌면 관련 vRouter도 반영한다.
6. 새 Handshake 이후 승인된 Host에서 RDS FQDN 해석·TCP/TLS·권한 범위의 실제 작업을 확인한다. 원본 Source 수신 기록과 왕복 경로를 확보한다.
7. 미승인 Host·미승인 Port의 새 접속이 차단되는지 재시험하고 독립 Cloud Runtime의 영향 유무를 기록한다. SG 변경 전 기존 연결이 남을 수 있으므로 신규 연결로도 확인한다.
8. 이관/전송 작업을 Checkpoint 기준으로 재개하고 무결성·중복 실행 영향을 확인한다. 탐지·조치 시작·재기동/재구축·업무 재개 시간을 기록한다. Gateway 탐지·조치·업무 재개 시간을 §3-G.4.1/T14에 따라 측정하고 반복/재시험 조건을 실행 Case에 기록한다. 승인된 별도 Gateway MTTR 수치는 없으며 현재 설계의 Offline RTO10분을 Gateway MTTR에 대입하지 않는다. 측정 전 달성값을 주장하지 않는다.

Gateway 손상과 AWS 전체 장애의 복구는 다르다. AWS 장애 선언 후 On-Prem 서비스 복구는 이미 로컬에 확보한 Backup/이미지/설정/Secret을 사용하며 Tunnel·S3·AWS DNS 조회 성공을 대기하지 않는다.

#### 3-B.9.9 검증 Matrix와 진행 Gate

| 시험 | 필요한 Evidence / 합격 방향 |
|---|---|
| 경로 선택 | 관련 Host/vRouter/Gateway OS Route 및 AWS Table/Association 확인. DB는 WG, Internet/API/S3 Backup은 각각 승인 경로 |
| 실제 왕복 | 승인 Job Host→RDS 신규 접속·작업, 응답 경로. 필요한 경우에만 별도 Cloud→On-Prem 시험 |
| Source 보존 | 대상 Log/안전한 Packet Capture의 실제 사설 Source. SG/Firewall Counter와 비교. Key·Token·업무 데이터는 Evidence에서 제거 |
| 부정 시험 | 별도 미승인 Host와 미승인 Port 신규 접속 차단. RDS 접속 허용이 Redis 허용으로 확대되지 않음 |
| 재기동 지속 | 두 Gateway 재기동 후 WG/Forwarding/Route·NAT 예외 유지 |
| Peer 주소 변화·유휴 | 학원 출구 변경/유휴 후 재통신, Keepalive·실제 Endpoint와 회복시간 기록 |
| 대용량 | 실제 Export/Backup 크기에 가까운 전송·Checksum, PMTU/MSS 이상 및 재시도 확인 |
| 재구축 | AWS EC2 또는 On-Prem VM 하나씩 재구축, Key 재주입, EIP/ENI/Route 복원, 승인/금지 통신 재시험 |
| Tunnel 중단 | Cloud 사용자·API·DB/Redis 및 필요 Egress 정상. Hybrid 작업 중단과 Cloud 서비스 영향 구분 |
| AWS 장애 복구 | 로컬 Backup으로 On-Prem Restore 후 DB·Redis·Backend/서비스 확인. AWS 호출 필수 단계 없음 |

Network 설계 정리는 새 제안 승인과 미확인 입력의 관리 방법·검증 기준을 갖추었을 때 다음 상세설계로 넘길 수 있다. Runtime PASS는 실제 Account·OS·ROSA 환경에서 위 시험 Evidence가 확보된 뒤 판단한다. 아직 VM/Host 주소, Peer Key 보관, SSM, 실제 Worker SG·Source, Account/Provider 조건, 비용·Runtime Window 및 데이터 작업 주체가 미확인이다.

**승인된 작업 전제 범위:** ① 목적별 Route Table + Host /32 범위 + RDS 우선 Hybrid 후보 ② 사설 왕복 Route·Source 보존·AllowedIPs 분리 ③ Data SG/Workload/Host Firewall 중심 제한 및 초기 Default NACL ④ UDP 51820 Public 단일 예외 + Keepalive/MTU 시작값 ⑤ 수동 IaC 재구축·EIP/ENI/Route·Key 복원 경계.  
**영향 영역:** 3-C 인증·Key·SSM, 3-D 이관/Backup 주체, 3-E Client/TLS, 3-F State/Ansible/Rule Lifecycle, 3-G 장애 Evidence, 3-H 담당·시간·예산.  
**재검토 조건:** 실제 Route/NAT 또는 Source가 예상과 다름, 전용 Gateway 확보 불가, UDP/출구 CIDR 제약, Worker SG 분리·지원 입력 제약, 비용/일정 초과, 업무 통신 목적 변경.  
**Issue / PR / Runtime Evidence:** 이번 새 설계에 대해 생성·조회한 Runtime Evidence 없음.

### 3-B.10. 검증 결과와 미확인 항목

#### 문서·주소 계산으로 확인한 범위

- 서울 Region의 ROSA Classic 지원은 공식 문서로 확인했다.
- 알려진 학원/On-Prem/Kubernetes/Docker CIDR과 승인된 작업 전제의 VPC/Pod/Service/Tunnel 사이의 중복은 계산상 발견되지 않았다.
- 9개 Subnet 모두 승인된 VPC 범위 내부에 있고 서로 중복하지 않는다.
- VPC 안의 /24 16개 중 9개를 사용하고 7개를 예비로 남긴다.
- VPC=Machine 및 VPC→Subnet 포함 관계는 의도된 관계로 분리했다.

#### 구현 전 확인해야 할 범위

- Demo OCP 및 기타 실제 연결 대상의 CIDR
- 팀원 접속망·추가 VMware/Docker Network와 충돌
- 실제 AWS Account의 Region 접근·Quota·3개 AZ의 필요한 Instance 가용성
- ROSA Classic 사전 요구 Quota. 공식 AWS 문서의 Standard On-Demand 100 vCPU는 Quota 요구이며 실제 100 vCPU를 배치한다는 뜻은 아님
- 전용 On-Prem Gateway의 VM 자원·주소·설치 가능 여부
- 최종 경로 NAT 예외, 왕복 Route, 실제 Source IP
- 최종 ROSA Version / RHCS / AWS Provider에서 사용할 CIDR·Subnet 입력 검증
- Node/ENI/Upgrade를 고려한 Subnet 용량
- 실제 On-Prem Job Host /32·전용 Gateway IP·각 vRouter Next Hop
- 실제 Worker Source/SG 식별 및 Data SG Binding 생성·삭제 순서
- VPN EIP/ENI 보존·재연결, Key 복원, 재기동 지속 및 부정 접속 시험
- API/Ingress/Egress/DNS 작업 전제의 선택 Version·Provider 적합성 및 첫 Full Apply 전 $500 Cost Gate

이는 Runtime PASS가 아니다. Account/서버를 재조회하거나 자원을 생성하지 않았다. 아직 확인되지 않은 Network를 포함한 전체 IPAM 비충돌을 주장하지 않는다.

#### 후속 설계 인계 — 설계 전제와 구현 Gate

| 남은 입력 / 연결 사항 | 후속 단계 | 적용·PASS 전 조건 |
|---|---|---|
| On-Prem Gateway·전용 Data VM 주소, vRouter Next Hop, 추가 CIDR | 3-D-2 작업 전제 승인 / 3-F 구현 | Data VM 사용은 선택됨. 실제 Inventory·Host `/32`·왕복 Route는 확인 전이며 빈 값으로 허용 범위 확대 금지 |
| Peer Key 보관·재주입·회수, AWS 관리 접속 | 3-C IAM/Secret | Tunnel 자체에 의존하지 않는 SSM/IAM 경로 및 로컬 복구 가능 여부 |
| RDS/Redis 계정·TLS·Source/SG | 3-C / 3-D / 3-E | 실제 Client Source와 권한·Port·Failover 후 재접속 |
| Worker SG Binding과 ENI/EIP/Route 지속·삭제 순서 | 3-F Terraform/GitOps | 지원 Version/Provider의 Plan·생성·재생성·삭제 검증 |
| ROSA/NAT Runtime Window·Quota·전체 잔존 비용 | 3-F / 3-H, 첫 Full Apply Cost Gate | $500 예산 및 실제 Account 가용성 확인 |
| 정상·금지 통신·Tunnel 중단·Gateway 재구축·AWS 장애 Restore | 3-G | §3-B.8.7·§3-B.9.9의 실제 Evidence. 과거 PoC로 대체하지 않음 |

**인계 판정:** 3-B의 기본 선택·소유권·실패 영향·검증 기준은 후속 설계의 입력으로 정리되었다. 미확인 구현 값은 명시적 Gate로 남긴다. 최종 주소·설정 및 Runtime PASS는 후속 설계·구현·시험에서 확인하고, 2026-10-01 전체03 컨펌으로 Network 설계 문서도 승인되었다.

#### 3-D-2 승인된 작업 주체의 Network 환류

2026-10-01 Data 설계 작업 전제 승인에 따라 이전·주기 Backup의 실행 위치를 **On-Prem 전용 Data VM**으로 구체화한다. 실제 VM 생성·주소 확보·Rule 적용 결과는 미확인이다.

- RDS Dump/Import는 해당 VM의 실제 `/32`와 기존 vRouter/전용 Gateway/WireGuard의 왕복 경로로 제한한다. RDS Endpoint DNS·TLS·CA/서버 이름 검증과 SQL 권한은 3-D 절에 연결한다.
- S3 Backup은 기존 Internet HTTPS와 별도 제한된 Backup IAM User Key를 사용한다. S3 업로드 후 On-Prem Recovery Storage 다운로드·무결성 확인까지 검증하며 S3 HTTPS를 Tunnel 필수 경로로 바꾸지 않는다.
- DB 작업 Host 선택만으로 Redis 직접 진단 허용을 추가하지 않는다. Redis는 승인된 Cloud Backend/시험 Workload의 실제 Source와 TLS/AUTH로 검증한다.
- Data VM·VPN 장애 시 최신 Backup 지연과 Cloud 정상 서비스 동작을 분리해 확인한다. RDS Stop·Redis 유지/계획 재생성·ROSA 삭제 순서는 3-D-3 승인된 작업 전제와 3-F/3-H로 연결한다.

이 환류는 기존 연결 모델·CIDR 선택·정상 서비스의 VPN 비의존성을 변경하는 새 Network 선택이 아니다. 실제 Data Host 주소·Source·경로 확인 전에는 Rule을 활성화하지 않는다.

### 3-B.11. 후속 검토 및 전체 최종 검토

Route / SG / Gateway Recovery까지 작업 전제 승인을 받았고 Network 검증 기준·미확인 입력·후속 Gate를 정리해 3-C IAM/Secret으로 인계한다. 실제 Network Runtime 검증은 구현 후 수행한다. 3-B는 전체03 컨펌 범위에 포함되지만 모든 실제 구현 입력이 확인된 것은 아니다.

3-C IAM/Secret, 3-D Migration, 3-E Interface, 3-F Terraform/GitOps, 3-G Test/Evidence, 3-H WBS까지 연결한 전체03 검토·최종 컨펌을 완료했다. 문서 검토에서는 Address Conflict, Ownership, Runtime/Recovery 의존성, Secret 복구, 비용, 일정, Test 가능성을 함께 검토한다.

- [x] 연결 모델 사용자 소단계 승인
- [x] 당시 승인에 따른 Working Draft 상태 기록
- [x] Region / CIDR / VPC 주요 후보 비교
- [x] 알려진 주소 범위의 계산상 검증
- [x] Region / IPAM / Subnet 작업 전제 승인
- [ ] 미확인 Address / Account / Gateway 조건 확인
- [x] API / Ingress / Egress / DNS 후보 비교 및 새 제안 작성
- [x] API / Ingress / Egress / DNS 작업 전제 승인
- [x] Route / SG / Gateway Recovery 후보 비교 및 제안 작성
- [x] Route / SG / Gateway Recovery 작업 전제 승인
- [x] Network 검증 기준·미확인 입력·후속 Gate 정리
- [x] 3-C IAM/Secret 설계로 인계
- [ ] 실제 입력 확보·구현 설정 반영
- [ ] Runtime 검증 및 Evidence
- [ ] 3단계 전체 검토·최종 상세설계 승인

### 3-B.12. 공식 참고 자료

2026-10-01 KST 조회. 제품 지원 여부와 프로젝트 설계 제안을 구분한다.

- [ROSA Region 지원 및 Quota](https://docs.aws.amazon.com/general/latest/gr/rosa.html)
- [ROSA Classic CIDR / 기존 VPC 입력](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/install_rosa_classic_clusters/rosa-sts-interactive-mode-reference)
- [ROSA Classic 설치 / VPC 요구조건](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html-single/install_rosa_classic_clusters/index)
- [AWS Subnet CIDR 및 예약 주소](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html)
- [WireGuard NAT Keepalive](https://www.wireguard.com/quickstart/)
- [AWS Site-to-Site Customer Gateway 옵션](https://docs.aws.amazon.com/vpn/latest/s2svpn/cgw-options.html)
- [AWS Regional NAT Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html)

- [ROSA STS Privacy 및 Public/Private 생성 제약](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/install_rosa_classic_clusters/rosa-sts-creating-a-cluster-with-customizations)
- [ROSA TLS / Ingress / 서비스 관리 경계](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/introduction_to_rosa/policies-and-service-definition)
- [AWS Zonal NAT AZ 장애 특성](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-basics.html)
- [AWS NAT / Public IPv4 / Regional NAT 과금](https://aws.amazon.com/vpc/pricing/)
- [S3 Gateway Endpoint 및 Hybrid 제한](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)
- [ECR Interface Endpoint / S3 Layer](https://docs.aws.amazon.com/AmazonECR/latest/userguide/vpc-endpoints.html)
- [VPC DNS 속성](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html)
- [Hybrid Inbound DNS 전달](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html)
- [ElastiCache Client DNS 재해석](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ClientConfig.DNS.html)

- [AWS Route Table 구성](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)
- [AWS Route 우선순위](https://docs.aws.amazon.com/vpc/latest/userguide/route-tables-priority.html)
- [AWS SG 참조·중간 Appliance·DNS 제약](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html)
- [AWS SG Connection Tracking](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html)
- [AWS NACL Stateful/Stateless 차이](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
- [EC2 ENI·Source/Destination Check·같은 AZ 제약](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html)
- [EIP 재연결·수명·과금](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)
- [WireGuard AllowedIPs / Cryptokey Routing / Roaming](https://www.wireguard.com/)
- [ROSA STS SG·Subnet Tag·Platform Egress 지원 경계](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/prepare_your_environment/rosa-sts-aws-prereqs)
- [RDS SG Source와 Port](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html)

## 3-C IAM Identity와 Secret

### 3-C.1. 이전 단계의 승인과 이번 범위

3-A 저장소 경계, 3-B 연결·Region/IPAM/Subnet·Public API/Ingress·AZ별 NAT/S3 Endpoint/DNS·Route/SG/Gateway 복구는 후속 설계의 작업 전제로 승인되었다. Network는 기본 선택과 검증 기준을 정리했으며 실제 Host·Account·Source·Quota·비용·Runtime Gate는 남아 있다.

2026-10-01 승인된 3-C-1 작업 전제를 다음과 같이 기록한다.

1. AWS Human 인증: Root로 초기 IAM User 4개 생성, 팀원별 하나씩 사용, 각 사용자에 AdministratorAccess 부여. 기존 연합 로그인 우선 제안을 사용자 지정 단순 운영안으로 변경. 최소 확인사항은 §3-C.3에 기록하며 실제 설정 완료와 구분.
2. Terraform 실행: bootstrap/foundation/rosa 실행 권한과 State 접근 범위 분리.
3. ROSA Human 인증: GitHub IDP, 2차 프로젝트 전용 Team으로 로그인 대상 제한.
4. ROSA 권한: 제한된 Platform 관리와 Namespace/Resource별 업무 권한, 인증과 RBAC의 분리.
5. 자동화 주체: Jenkins·GitOps·Backup·Runtime별 Principal과 Credential 목적 분리.

기존 지침 §30~31에는 IAM User ×4 + AdministratorAccess의 단순 운영 후보와 Minimum Gate가 이미 기록되어 있었다. 앞선 제안은 이 후보를 충분히 반영하지 못했으며 2026-10-01 승인으로 사람 계정의 작업 전제를 갱신했다. CI의 제한된 IAM Principal과 Secret Bootstrap Gate는 유지하며, CI 최초 인증은 3-C-2의 제한된 CI IAM User Key 안으로 작업 전제 승인되었다. Secret 저장·공급·복구는 3-C-3의 SOPS + age 및 담당자 초기 공급 절차를 작업 전제로 승인했다. 실제 구현·설정 검증은 아직 진행 전이다. 기존 팀의 별도 Security 합의나 계정 정책이 추가 제시되면 비교에 반영한다. 1차 팀 역할을 2차 AWS/ROSA 권한 배정으로 자동 승격하지 않는다. 실제 사람별 배정은 업무 확인 및 3-H WBS와 연결한다.

### 3-C.2. 상위 불변조건과 구분할 권한

- Jenkins의 ECR Push는 별도 제한된 CI Principal로 수행하고 ECR Token은 실행 시 발급한다. 범용 Administrator 또는 저장된 장기 ECR Password를 기본으로 삼지 않는다.
- ROSA Operator의 AWS STS Role, 사람의 AWS Role, 사람의 ROSA RBAC, 애플리케이션 DB/Redis 권한은 별도 계층이다.
- Terraform/RHCS는 Infrastructure, GitOps는 Cluster 내부 Desired State를 소유한다. Secret 실제 값은 별도 공급 체계이며 GitOps Manifest 저장소와 동일하지 않다.
- State의 `sensitive` 표시는 Secret을 State에서 제거한다는 뜻이 아니다. State/Plan/Log의 접근과 실제 Secret 값 저장 여부를 검토한다.
- Cloud Runtime은 Hybrid·On-Prem CI에 의존하지 않는다. AWS 전체 장애 후 On-Prem Restore는 이미 로컬에 확보한 Backup·Image·설정·Secret으로 수행한다.

| 계층 | 인증 대상 / 허용 대상 | 서로 대체하지 않는 것 |
|---|---|---|
| AWS Human IAM | AWS Console/CLI·서비스 API | ROSA Namespace RBAC, SQL SELECT 권한 |
| ROSA Operator IAM | 특정 Operator의 AWS STS 작업 | Jenkins ECR Push·팀원 Console 로그인 |
| ROSA Human IDP + RBAC | 사용자 식별 + OpenShift API 작업 | AWS Account 권한·GitHub 저장소 권한 |
| GitHub Repo 권한 | 코드/Manifest 읽기·변경·Review | GitHub IDP의 ROSA 관리 Role 자동 배정 |
| DB/Redis 인증·권한 | 애플리케이션/Backup/이관의 데이터 작업 | RDS/ElastiCache AWS Control Plane 권한 |
| WireGuard Key | Peer 인증과 사설 Source 경로 | DB 계정·Namespace·AWS IAM 권한 |

IAM·RBAC 정책을 허용했다고 Network Route/SG가 자동으로 열리는 것은 아니다. 반대로 TCP Port가 열려도 데이터 작업 권한을 얻은 것은 아니다.

### 3-C.3. AWS Human 인증 — 사용자 지정 단순 운영 작업 전제

**승인된 설계:** Root가 초기 IAM User 4개를 생성하고 팀원마다 하나씩 사용한다. 각 사용자에게 AWS 관리형 `AdministratorAccess`를 부여한다. 속도·편의성을 위한 프로젝트 선택으로 소단계 승인 후 전체03 최종 컨펌 범위에 포함되었다. 실제 사용자 생성·Policy 연결·MFA 설정을 수행하거나 확인하지 않았다.

각 사용자에 직접 Policy를 연결해도 된다. 동일한 관리형 Policy를 연결한 IAM Group 하나에 4명을 넣으면 권한 연결을 한 곳에서 관리할 수 있다. Group 이름은 아직 미정이며 어느 방식도 별도 권한 체계를 도입하는 것은 아니다. 조직 정책·SCP·학교 제공 권한 등 Account 상위 제한의 존재는 구현 전에 확인한다.

Root의 초기 사용자 생성은 이번 운영안에 포함한다. 초기 설정 후 팀원은 개인 IAM User로 작업하며 Root를 일상 Terraform·Jenkins 계정으로 쓰지 않는다. AWS Account를 네 개 만드는 안이나 네 명이 하나의 로그인 정보를 공유하는 안이 아니다.

#### 기존 지침 §31의 Minimum Gate와 간단한 설정

| 항목 | 적용 방향 | 현재 상태 |
|---|---|---|
| Root MFA / 일상 사용 금지 | Root MFA, Root Access Key 생성 금지, 초기 설정 후 개인 IAM User 사용 | 설정 미확인 |
| 팀원 MFA / 개인별 분리 | 4개 개인 IAM User에 각각 MFA. Console의 사용자 Security credentials에서 기기 등록 | 사용자 지정 운영안 반영 / 설정 미확인 |
| CLI Credential 필요 여부 | CLI/Terraform 실제 담당자에게 필요한 수단만 마련. Console 사용자 생성과 Access Key 생성은 별개 | 후속 구현 입력 |
| Access Key 보관 | Git·문서·메신저에 실제 값 기록 금지. 개인 Admin Key를 Jenkins에 복사하지 않음 | 보관 방식·발급 여부 미확인 |
| Terraform 실행 권한 | §3-C.4의 Lifecycle Role/State 분리 유지, 실행 Profile과 Caller 확인 | 설계 작업 전제 승인 / 미구현 |
| ROSA 요구 Role | 공식 Account/Operator STS Role 유지. Human Admin과 별도 | 설계 유지 / 미구현 |
| CI/CD Credential | 사람 계정 4개와 별도 제한된 자동화 Principal | 작업 전제 승인 / 최초 인증은 3-C-2 작업 전제 승인 |
| 프로젝트 종료 시 폐기 | 자원 정리와 관리 경로 확보 후 프로젝트 Key·CI Credential·사용자 접근 회수 | 종료 작업에 반영 / 미실행 |

Console MFA 등록만으로 IAM User의 장기 Access Key API 요청에 MFA가 자동 강제되지는 않는다. CLI의 MFA·STS 사용과 정책 조건은 별도다. 임시 Credential을 사용하더라도 최초 인증용 장기 Key가 존재하면 그 보관·회수 책임은 남는다. 실제 CLI 담당자와 도구가 정해질 때 적용 방법을 정하며 사람 운영안 채택을 위해 Identity Center 도입을 선행하지 않는다.

#### 기존 설계와의 관계

- Network·ROSA Classic·Data·Hybrid 복구 Architecture와 직접 충돌하지 않는다. AWS Human의 연합 로그인 우선 제안만 이번 운영안으로 변경한다.
- AdministratorAccess는 광범위한 AWS 권한이다. 네 사람이 TF Role을 사용해도 개인 Admin 권한으로 다른 작업을 수행할 수 있으므로, 이를 사람의 강제 최소권한 격리라고 주장하지 않는다.
- Terraform Role 분리는 실행 목적·State·재생성/삭제 경계와 실행 기록을 정리한다. 사람이 승인 범위 안에서 작업한다는 운영 규칙과 IAM의 기술적 차단을 구분한다. foundation/bootstrap 전체 Destroy의 별도 승인 조건은 유지한다.
- AWS Admin 권한은 ROSA cluster-admin이나 DB SQL 권한을 자동으로 부여하지 않는다. 승인된 GitHub IDP·ROSA RBAC·자동화 Principal 분리는 그대로 유지한다.
- 프로젝트 말미에 심사만을 위해 연합 로그인으로 교체하거나 사람 권한을 전면 재설계하는 것을 필수 작업으로 추가하지 않는다. 최종 검토에서는 이 선택의 실제 설정과 영향, 기존 Minimum Gate를 확인한다.

Identity Center/기존 IdP 연합은 향후 확장·조직 정책 대응 시의 대안이다. 현재 기본안이나 다음 CI 설계의 선행 Gate가 아니다.

### 3-C.4. Terraform 실행 Role / State 경계 — 작업 전제 승인

**권고:** 승인된 세 Lifecycle 경계에 맞춰 실행 Role을 분리한다. 초기에는 승인된 담당자가 개인 인증 후 실행하고 Jenkins에 Terraform 광역 권한을 함께 넣지 않는다. CI Terraform 자동화 여부는 3-F에서 검토한다.

| 논리 Role | 권한 범위 | Lifecycle·State 경계 |
|---|---|---|
| TF Bootstrap | Remote Backend·암호화·Versioning·Locking·접근 정책 구성 및 필요한 권한 초기 설정 | 최초 Local State와 승인된 Remote 이동. State Bucket/Key Policy 변경은 제한된 담당자 |
| TF Foundation | VPC/Route/팀 SG/VPN, RDS/Redis, ECR/S3, ROSA Account-wide prerequisite | foundation State 및 필요한 의존 Output. 전체 Destroy는 상위 별도 승인 조건 유지 |
| TF ROSA | Cluster·Machine Pool·Cluster-specific IAM/OIDC 및 승인된 SG Binding | rosa State, 필요한 foundation Output. 반복 Create/Delete는 해당 경계 |

서비스 Action뿐 아니라 Role Trust와 `iam:PassRole`, IAM Role/Policy 생성·연결 권한도 검토한다. PassRole은 필요한 Role ARN과 전달 대상 서비스로 제한하는 안이다. ROSA 공식 설치에 필요한 Account/Operator Role·Policy는 팀의 편의대로 줄이거나 일반 CI 권한으로 재사용하지 않는다.

원래 Source에는 foundation이 Account-wide prerequisite, rosa가 Cluster-specific IAM/OIDC를 소유한다. 3-F-1 승인에 따라 TF 실행 Role 자체는 bootstrap State에서 생성·관리하고, 최초 개인 인증→Local Bootstrap→Remote 이전→목적별 Role 실행으로 순환 의존성을 해소한다(§3-F.2·§3-F.4). Role 명칭·ARN·IAM JSON을 현재 임의 생성하지 않는다.

3-F-1 승인에 따라 State 간 값은 해당 Owner가 비밀값 아닌 필요한 Output만 추출한 보호 입력 파일로 전달한다(§3-F.5). foundation State 전체를 읽는 terraform_remote_state를 기본 경로로 두지 않는다. 실제 읽기 전용 자원 조회·입력 개정/대상 확인은 구현 전에 연결한다.

실제 CLI 인증 수단의 STS Session Duration, Role Chaining, 장시간 ROSA Apply 중 Credential 갱신은 실제 실행 방식에서 검증한다. 짧은 Credential을 쓴다는 이유만으로 Cluster 생성이 끝날 때까지 항상 인증이 유지된다고 가정하지 않는다.

### 3-C.5. ROSA Human IDP — GitHub 프로젝트 Team 작업 전제 승인

| 후보 | 장점 | 조건 / 부담 | 판단 |
|---|---|---|---|
| GitHub IDP + 프로젝트 Team 제한 | 기존 seokpan 협업 계정 활용, 신규 인증 서버 운영 불필요 | Org OAuth App 등록 권한·Team·Client Secret·Callback URL·사용자 Mapping 확인 | 우선 권고 |
| 기존 OIDC IdP | 조직 인증·MFA 정책 통합 가능 | 실제 IdP/Client 등록·Trust와 사용자 Mapping 필요 | 이미 제공되는 환경이면 대안 |
| htpasswd | 외부 IdP 장애 시 독립적인 제한 관리 접속 가능 | Static Credential 보관·재주입·회수와 MFA 한계 | Bootstrap/비상 관리 경계의 후보 |
| LDAP 등 별도 인증 인프라 | 조직 Directory 활용 | 현재 확인된 Directory가 없고 운영·복구 범위 증가 | 신규 기본안으로 권고하지 않음 |

기본 권고는 seokpan 안의 **2차 프로젝트 전용 Team**을 ROSA 로그인 Allowlist로 쓰는 것이다. Team 명칭과 실제 구성원은 아직 미확정이며, Org 전체를 허용하는 대안은 신규 가입·1차/기타 구성원 범위를 함께 검토한다. 현재 Team 생성·멤버 초대·OAuth App 등록은 수행하지 않았다.

GitHub IDP는 공식적으로 Organization 또는 Team 제한을 지원한다. 실제 Org Admin 권한·OAuth App 설정을 확인하고 생성된 Cluster의 실제 Callback URL을 사용한다. IDP 이름·Mapping Method와 `oc whoami`의 실제 식별을 RoleBinding과 연결한다. GitHub Team Allowlist가 OpenShift 관리자 Group과 자동으로 같아지지는 않는다.

팀원의 GitHub MFA 상태를 확인한다. ROSA가 GitHub 로그인을 쓴다는 사실만으로 신규 로그인마다 MFA가 강제되었다고 주장하지 않는다. Org 전체 2FA 정책 변경은 1차 및 다른 구성원에도 영향을 줄 수 있으므로 자동 변경하지 않고 별도 영향 검토를 한다.

Clean Recreate에서는 새 Cluster의 OAuth Callback·IDP 설정·RBAC를 다시 확인한다. OAuth Client Secret의 원본·공급 경계는 §3-C.12의 승인안에 따르며 실제 Provider와 초기 공급 구현은 3-F에서 확인한다. Terraform/RHCS 설정에 Client Secret을 넣으면 State에 들어갈 수 있으므로 코드/State/Bootstrap 경계를 제품·Provider에 맞춰 검토한다.

### 3-C.6. ROSA RBAC / 관리자 / 비상 관리 — 작업 전제 승인

**권고:** 제한된 Platform 관리자와 Namespace/Resource별 업무 권한. 모든 팀원에게 cluster-admin 또는 Namespace admin을 일괄 부여하지 않는다.

| 업무 | 권한 후보 | 별도 승격·제한 대상 |
|---|---|---|
| 일반 확인·Evidence | 지정 App Namespace의 필요한 get/list/watch·로그 조회 | Secret 값, exec/port-forward, Cluster-wide 자원, 다른 Namespace |
| App 운영 | GitOps 변경·Review·배포 상태 확인. 실제 필요한 좁은 운영 Role | 직접 Deployment 변경·임의 Pod 생성/exec·RoleBinding 변경은 필요 시 승인된 작업 권한 |
| Data 이관/복구 | 해당 Job·Account·Backup 경로와 데이터 권한 | Platform 전체 admin, Cloud DB Master 계정의 상시 공유 |
| Observability | 지정 Monitoring Resource·대상 Workload 조회와 필요한 설정 | 모든 Namespace Secret 및 전체 Cluster 변경 |
| Platform 운영 | 필요한 관리자에 dedicated-admin 우선 비교 | Operator/GitOps 설치·Cluster-scope 설정에 더 높은 권한이 필요하면 지정 담당자 작업 기간에 부여 |
| Bootstrap / 비상 대응 | 제한된 담당자의 최소 관리자 경로 | 일반 CI·팀 공유 kubeconfig·일상 운영으로 사용하지 않음 |

`dedicated-admin`은 프로젝트 Namespace만의 제한 Role이 아니라 넓은 고객 관리자 권한이다. 일반 팀원의 읽기 권한으로 취급하지 않는다. cluster-admin은 꼭 필요한 Bootstrap/관리 작업의 최소 인원에만 부여하고 작업 종료 후 RoleBinding·Session/Token 경계를 확인한다. ROSA의 Managed Resource 제한은 cluster-admin이 있더라도 보존한다.

RBAC는 허용 권한의 합이다. 낮은 Role을 추가한다고 기존 높은 Role이 축소되지 않는다. `admin`/`edit` 및 집계된 기본 Role의 실제 Rule도 확인한다. 특정 사용자의 명목상 view Role만 보고 모든 실효 권한이 읽기라고 판단하지 않는다.

Secret get/list를 막았더라도 Pod 생성/수정·exec·GitOps Manifest 변경 권한으로 해당 Namespace의 Secret을 사용할 수 있는지 검토한다. App 운영자와 Secret 공급자의 권한 경계가 완전히 독립적이라고 과장하지 않는다. Logs·State·Backup·SSM Shell도 Secret/데이터 접근 경로가 될 수 있다.

Bootstrap에서는 공식 관리 경로로 GitOps/IDP/RBAC의 초기 설정을 수행하고 정상 개인 IDP 로그인·허용/금지 작업을 검증한다. htpasswd 비상 경로를 보존하는 경우 담당자·보관·사용 사유·회수/교체를 기록하며 팀 공용 일상 계정으로 사용하지 않는다. 일회 Bootstrap 계정과 유지할 비상 계정을 구분하고 실사용 담당자 배정과 보관 방식은 Secret 설계에서 확정한다.

실제 사용자/Group·Namespace·ServiceAccount·RoleBinding 이름은 아직 작성하지 않았다. 기본 시스템 Group·Self-Provisioner 및 다른 Binding에 의한 권한도 조사하고, 팀 전체 외부 사용자에게 무조건 Cluster 작업 권한을 주지 않는다.

### 3-C.7. 자동화 Principal / Credential 목적 — 작업 전제 승인

| 주체 | 필요한 권한 후보 | 기본에 포함하지 않는 권한 |
|---|---|---|
| Jenkins ECR Push | 지정 Application ECR Repo의 Push/Pull 검증과 Token 발급 | TF Apply, IAM 변경, RDS 관리, Cluster 관리자 Token |
| Jenkins GitOps 변경 | 지정 Repo/환경 경로의 Release 변경·Review 흐름 | 모든 seokpan Repo 쓰기, 인적 계정의 모든 Repo Token 공유 |
| GitOps Repo Reader | 필요한 GitOps Repo 읽기 | CI Git Write Credential 재사용 |
| GitOps Controller | 승인된 Namespace·Resource Desired State 반영. Platform 관리 영역은 별도 경계 | Jenkins AWS Human 권한·무관 Namespace·IAM/Infrastructure 소유 |
| Backup Writer | 지정 Bucket/Prefix에 생성·업로드, 필요한 암호화 권한 | State Bucket·모든 Backup 삭제·전체 Secret 읽기 |
| Backup Downloader / Restore 주체 | 승인된 Backup 객체 조회·다운로드·검증, 별도 DB 복구 계정 | 모든 S3 객체 쓰기·삭제, AWS 장애 후 AWS 인증을 필수 단계로 사용 |
| Runtime Backend | App 전용 DB/Redis Credential과 실제 필요한 ServiceAccount 권한 | ECR Push·Terraform·DB Master·일반 AWS IAM 권한 |
| VPN EC2 | SSM Agent·필요 Bootstrap 등 Instance Role | On-Prem Jenkins의 IAM 인증 Broker, 모든 S3/Secret 접근 |
| ROSA Operator | 공식 설치·운영에 필요한 Operator STS Role | 위 CI/Backup/Human Role과의 Credential 공유 |

Purpose별 Role/Principal을 분리하되 실제 쓰지 않는 Role을 미리 모두 생성하지 않는다. Data 단계에서 하나의 Job이 어떤 읽기/쓰기를 하는지 정한 뒤 Policy를 작성한다. 동일 Host에서 여러 Job을 실행해도 Process·Agent·Credential Binding을 나누고 Host 관리자에게 노출되는 범위를 검토한다.

ECR Authorization Token은 발급 Principal의 권한 범위를 따르며 유효기간이 있다. Token을 매 실행 발급해도 AWS API Token 발급용 최초 Credential이 자동으로 없어지는 것은 아니다. 최초 인증용 장기 Key는 §3-C.11에서 별도의 작업 전제로 승인되었고 실제 발급·보관·회수 설정은 검증 전이다.

On-Prem Jenkins 인증은 IAM Roles Anywhere, 실제 Token을 발급하는 OIDC Federation, 제한된 IAM User Key + STS 예외를 주요 후보로 조사한다. Roles Anywhere는 X.509 Certificate/Trust Anchor·갱신·회수 관리가 필요하다. OIDC는 실제 Jenkins 실행 주체가 신뢰 가능한 Token을 얻는 경로가 있어야 한다. GitHub 저장소를 사용한다는 이유만으로 On-Prem Jenkins가 GitHub Actions OIDC Token을 받는다고 가정하지 않는다. 2026-10-01 3-C-2의 다섯 가지 작업 전제 승인으로 제한된 ECR CI IAM User Access Key 안을 작업 전제로 선택했다. Roles Anywhere/OIDC는 재검토 대안이며 실제 Key 발급·CI 적용을 수행하지 않았다. CI 위치는 On-Prem으로 유지한다.

ROSA의 Workload ServiceAccount→AWS 권한은 실제 AWS API 호출 요구가 있을 때 별도로 설계한다. DB/Redis에 일반 Protocol로 연결하는 Backend에 모든 AWS API 권한을 자동 부여하지 않는다. ECR 이미지 Pull 인증·재발급은 Node/Kubelet/ROSA 지원 경로와 별도로 검토해야 하며 CI Push Token을 장기 ImagePullSecret으로 복사해 해결하지 않는다.

### 3-C.8. 관리·회수·장애 시 접근

- AWS Human Login·GitHub OAuth·Red Hat/OCM Login·ROSA RBAC는 서로 다른 인증/권한 경계다. 계정별 관리자·회수 경로를 기록한다.
- Human SSM StartSession 권한과 VPN EC2의 SSM Agent Role은 별도다. SSM 접속은 OS 관리 권한으로 이어질 수 있으므로 일반 읽기 권한에 포함시키지 않는다. IAM·Agent·HTTPS 접속·Session 추적을 구현에서 확인한다.
- GitHub Team 제거·IDP 설정 변경만으로 기존 OpenShift OAuth Token과 기존 Session이 즉시 모두 폐기되었다고 가정하지 않는다. 신규 로그인 제한·기존 Token·RBAC 제거를 별도로 시험한다.
- IAM User의 Console 접근·Access Key·이미 발급된 STS Session은 회수 경로를 구분한다. 한 수단을 비활성화했다고 기존 Session까지 모두 즉시 무효라고 가정하지 않는다. 긴급 차단·만료·재시험 방법을 구현에서 확인한다.
- ROSA 등 제한된 계층에서 필요한 권한 승격은 목적·대상·담당자·기간·작업 결과·회수를 기록한다. AWS Human은 이번 상시 Admin 운영안이므로 모든 AWS 작업에 별도의 임시 승격이 구현된 것처럼 기록하지 않는다.
- GitHub/On-Prem CI 장애는 신규 관리 로그인·신규 배포에 영향을 줄 수 있지만 기존 Cloud 서비스의 정상 처리를 필수 의존성으로 만들지 않는다. 장애 전 발급 Token의 수명을 무제한이라고 주장하지 않는다.
- AWS 전체 장애에서 On-Prem Restore를 수행할 로컬 관리자/DB/Harbor/Runtime Secret은 AWS·GitHub 조회 성공 없이 사용 가능해야 한다. 안전한 오프라인 복원본의 도구·관리자·검증·교체는 다음 Secret 설계에서 정한다.

### 3-C.9. 검증·입력 조건 — 아직 실행 전

| 확인 대상 | 실제 Evidence / 합격 방향 |
|---|---|
| AWS Account | 독립/Member 여부·상위 정책 제한·초기 Root 설정 가능 여부·4개 IAM User/관리형 Policy 연결 확인 |
| Human 인증 | 개인 Login·MFA·실제 Caller ARN과 작업 Role 확인 |
| TF Role 경계 | 해당 Role로 AssumeRole한 Session에서 필요한 Plan/Apply·State Lock 성공 및 무관 작업 거부 확인. 개인 Admin의 직접 호출까지 거부된다고 주장하지 않음. Backend 권한·Credential 갱신 검증 |
| ROSA IDP | 승인 Team 구성원 Login 성공·미승인 사용자 신규 Login 거부, 실제 Username·Callback·Mapping 확인 |
| RBAC | 실제 Subject의 Role/Binding·`oc auth can-i`와 허용/금지 요청 결과. 높은 다른 Binding과 Secret 간접 경로도 조사 |
| CI | 지정 ECR Push 성공·무관 Repo Push/권한 변경 거부. Token 갱신과 Agent 정리 |
| Backup | 지정 Prefix·객체 작업 성공·무관 State/Backup 작업 거부, 필요한 Key/SQL 권한 |
| 비상/회수 | 정상 IdP 의존성 장애 시 제한 접속 가능성, 신규/기존 Session 회수 후 권한 재시험 |
| Clean Recreate | IDP Callback·RBAC·Credential 재주입·ECR Pull·App DB/Redis 접속 복원 |
| On-Prem Restore | AWS 조회를 막은 상태에서 로컬 관리자·Backup·Image·Secret으로 실제 서비스 복구 |

이 문서는 Policy Simulator 결과·Runtime PASS가 아니다. AWS/GitHub/ROSA 계정 설정, 사용자 초대, 역할/Token 생성·배정 또는 실제 Credential 조회를 수행하지 않았다. 현재 예산·Quota·계정 제약도 미확인이다.

### 3-C.10. 승인·변경 결정 기록

**결정 ID:** PH2-3C-IDENTITY-PRINCIPAL / PH2-3C-HUMAN-IAM-SIMPLE  
**기록일:** 2026-10-01 KST  
**상태:** 3-C-1 나머지 네 항목은 사용자 작업 전제 승인. AWS Human은 사용자 지정 IAM User ×4 + AdministratorAccess로 변경 반영. 실제 Minimum Gate 통과·구현 완료·3단계 최종 승인과 구분한다.  
**근거:** 당시 승인 결정과 기존 지침 §30~31의 구현 속도·복잡도 및 Minimum Gate.  
**변경 영향:** 기존 연합 로그인 우선·사람 목적별 제한권한 제안은 현재 기본안에서 제외. TF Role은 실행 분리이며 사람 Admin의 기술적 격리를 보장하지 않음. CI 제한 Principal·ROSA IDP/RBAC·공식 Operator Role 유지.  
**재검토 조건:** Account 상위 정책과 충돌, Credential 노출, 실제 작업·회수·복구 불가, 일정·비용 또는 3단계 통합 검토의 변경 필요.  
**Issue / PR / Runtime Evidence:** 새 생성·조회한 자료 없음.

### 3-C.11. 3-C-2 CI 최초 인증·Secret Bootstrap 경계 — 작업 전제 승인

**결정 ID:** PH2-3C-CI-AUTH  
**승인일:** 2026-10-01 KST  
**근거:** 2026-10-01 3-C-2의 다섯 가지 작업 전제에 대한 명시적 승인.  
**상태:** 다섯 가지를 다음 Secret 설계의 작업 전제로 승인. 실제 CI User/Key/Policy/Jenkins Credential 생성·Runtime 검증 또는 3단계 최종 승인을 뜻하지 않는다. 기존 On-Prem Jenkins와 프로젝트 일정을 기준으로 최소 운영 복잡도를 우선한다.

| 번호 | 제안 | 범위 / 판단 근거 |
|---|---|---|
| 1 | 사람 4명 외에 ECR 전용 CI IAM User 1개, Console 로그인 없이 제한된 Access Key로 시작 | 사람 AdministratorAccess를 자동화에 복사하지 않음. 장기 Key 사용의 명시적 프로젝트 예외 작업 전제이며 단기 Credential만 쓰는 모델로 포장하지 않음 |
| 2 | 지정 Application ECR Repo의 이미지 Push/필요 Pull 검증만 허용, ECR 로그인 Token은 Push 단계마다 발급 | Repo 생성·삭제·IAM·Terraform·RDS·ROSA 관리 제외. GetAuthorizationToken은 Resource `*`, 이미지 작업은 실제 Repo ARN에 제한 |
| 3 | Jenkins의 2차 전용 Folder/Job 범위 Credential 보관·단계 한정 주입, 인증된 Release 단계에서만 사용 | Pipeline에는 Credential ID만. 로그 마스킹은 보조책이며 Job 수정 권한·Agent·Host 관리자 경계와 임시 Docker 설정 정리가 함께 필요 |
| 4 | AWS Push / GitOps Repo 쓰기 / GitOps Repo 읽기 / Harbor 복구 접근 Credential 분리 | Jenkins에 cluster-admin kubeconfig 또는 DB Master Secret을 기본 부여하지 않음. 실제 Git Credential 종류·발급·Repository 범위는 Secret 설계에서 별도 선택 |
| 5 | 발급→보관→사용→교체/회수의 최소 절차와 실패 시험, Runtime/Offline Restore Secret은 별도 경로 | 장기 CI Key의 유효성을 관리하고 노출·담당 변경 시 교체, 종료 시 폐기. CI Push Token을 Runtime Pull Secret으로 장기 복사하지 않음 |

#### 최초 AWS 인증 후보 비교

| 후보 | 구현·학습 부담 | 권한/인증 특성 | 현재 제안 |
|---|---|---|---|
| ECR 전용 IAM User Access Key | 기존 Jenkins Credential 기능 활용, 추가 인증 서버 불필요 | 장기 Key 보관·회수 책임. 제한된 ECR API 목적만 부여 | 짧은 프로젝트의 기본안 / 사용자 작업 전제 승인 |
| IAM Roles Anywhere | CA/Trust Anchor·Certificate·Signing Helper·갱신/회수 구축 | On-Prem에서 임시 Role Credential 가능. Certificate의 보관·회수는 필요 | 이미 쓸 PKI가 없다면 이번 기본안의 부담이 큼 |
| 실제 Jenkins OIDC + STS | 신뢰할 Token Issuer·Audience/Subject·Trust·Token 공급 검증 | 임시 Credential 가능. GitHub Repo가 있다고 Jenkins에 Actions OIDC가 공급되는 것은 아님 | 기존 공급 경로가 확인되면 재비교 |

여기서 장기 Key는 AWS 권장 임시 Workload Credential보다 단순 운영을 택하는 예외다. 사람 IAM User 채택과 구분하여 이번 3-C-2 승인으로 CI 전용 제한 Key를 선택했다. 사람 Admin Key의 자동화 재사용 승인은 아니다. 무의미한 STS 중간 Role을 추가해 최초 장기 Key의 존재를 숨기지 않으며 필요 권한이 ECR뿐이면 그 범위를 직접 제한하는 후보로 비교한다. 실제 제공 환경에 인증 공급 기능이 이미 있으면 비용·학습·복구 부담을 함께 재검토한다.

#### 실행·보관 경계

- Account ID·Region·Repo ARN은 실제 입력 후 Policy를 작성한다. ECR 공식 Push Action을 기준으로 필요한 Pull 검증 Action만 추가하고 실사용 없는 API는 제외한다.
- CI 전용 User는 Admin Group에 포함하지 않는다. 자동화용 비대화형 Credential에 사람 MFA 코드 입력을 매 Build 요구하는 모델은 사용하지 않는다.
- Credential이 필요한 Publish Job은 신뢰된 Release 입력만 실행한다. 미검토 PR·임의 Jenkinsfile·비신뢰 Build와 같은 Agent/OS 사용자에서 Secret을 공유하지 않는다. Folder 접근 제한만으로 Pipeline 작성자가 Credential을 꺼낼 수 없는 것은 아니다.
- `withCredentials` 범위에서만 주입하며 Groovy 문자열에 Secret 값을 펼치지 않고 Shell Trace를 끈다. Docker 로그인은 임시 `DOCKER_CONFIG` 경로와 `--password-stdin`을 사용하며 성공·실패 종료 모두 잔여 설정을 정리한다. Workspace/Artifact에 실제 Key·Token 파일을 남기지 않는다.
- Jenkins Credential 암호화는 Controller 저장 보호다. Controller/Host 관리자와 해당 Credential을 쓸 Pipeline 작성자를 강제 격리한다고 주장하지 않는다. Controller 복구에 필요한 암호화 자료의 안전한 보관은 다음 Secret 설계 범위다.
- Cloud ROSA의 ECR Pull 지원 경로는 CI Push 인증과 별도다. On-Prem Restore는 사전 확보한 Harbor Image와 로컬 Credential을 사용하며 장애 후 AWS Token 발급을 전제하지 않는다.

#### 확인할 시험과 다음 인계

문서·코드에서 실제 Secret 값을 다루지 않는다. 실제 검증에서는 지정 Repo Push 성공, 무관 Repo Push/IAM 변경 실패, Key 비활성화 후 신규 ECR Token 발급 실패, Build 종료 후 임시 파일 정리, Release Job 범위, 재발급 후 정상 동작을 확인한다. 이미 발급된 Token/Session의 회수 효과는 별도 확인하며 Key 비활성화만으로 모두 즉시 소멸한다고 주장하지 않는다.

다음 3-C-3에서는 Jenkins·ROSA IDP·App DB/Redis·WireGuard·Backup/Restore Secret의 실제 Source, 저장 제품, 주입, 재생성, 회수 및 AWS 조회 없이 사용할 복원본을 설계한다. 3-C-2 승인 이후 3-C-3에서 공급·보관 작업 전제를 별도로 승인했으며 실제 설정 여부와는 구분한다.

### 3-C.12. 3-C-3 Secret 공급·주입·회수·복구 — 작업 전제 승인

**제안 ID:** PH2-3C-SECRET-SUPPLY  
**작성일:** 2026-10-01 KST  
**승인일:** 2026-10-01 KST  
**상태:** 3-C-3의 다섯 가지 신규 제안이 후속 설계의 작업 전제로 승인됐다. 실제 Secret 값·암호화 파일·Key를 생성하거나 조회하지 않았으며 03 전체 최종 승인과 구분한다.  
**표현 지침:** 기술 용어의 직역보다 실제 동작을 설명하는 표현을 우선한다. 비밀번호·Key 교체, 암호화 Key 변경, 초기 설정·공급 절차처럼 목적·행동이 드러나게 쓰고 정식 제품명·명령·정책 속성명은 유지한다.

#### 3-C.12.1 작업 전제 승인된 다섯 가지

| 번호 | 작업 전제 제안 | 범위 |
|---|---|---|
| 1 | SOPS + age 암호화 파일과 지정 담당자 실행의 작은 Secret Bootstrap 절차 | 추가 Secret 서버·상시 Operator를 기본 도입하지 않고 초기 설정·교체·Clean Recreate 때 필요한 값만 공급 |
| 2 | 공급·복구 원본은 Git 밖의 접근 제한된 암호화 Bundle로 관리, 복호화 Key는 별도 보관 | Cloud Bootstrap / Automation / On-Prem Recovery 범위별 파일·수신자 분리, 암호문·복원 도구·Key 해제 수단의 장애 전 확보 |
| 3 | Terraform·GitOps·Secret 공급자의 Resource Ownership 분리 | Terraform은 기반 자원, GitOps는 Workload 및 Secret 참조, Secret 공급 절차는 지정 Secret 값·Object를 단독 관리 |
| 4 | CI/Git/Registry Credential의 목적별 저장·주입 방식 고정 | Jenkins는 승인된 제한 Credential만, Argo CD는 Git 읽기용, Harbor는 프로젝트용 Push/Pull과 Recovery Pull을 분리 |
| 5 | Clean Recreate와 AWS 조회 없는 On-Prem Restore를 서로 다른 절차로 검증, 교체·회수·복원본 동기화까지 포함 | Secret Object 존재만으로 PASS 처리하지 않고 실제 로그인·Image Pull·DB/Redis·애플리케이션 동작 확인 |

#### 3-C.12.2 기술 비교와 선택 이유

| 후보 | 구현·학습·운영 부담 | 재생성 / 장애 복구 특성 | 이번 판단 |
|---|---|---|---|
| SOPS + age + 담당자 Bootstrap | 로컬 CLI·암호화 파일·Key 보관·작은 실행 코드. 추가 상시 서버나 클러스터 Operator 불필요 | 암호문·age Identity·도구가 있으면 로컬 복호화 가능. 주입·교체는 담당자 작업이며 자동 동기화 아님 | 기본 제안 |
| AWS Secrets Manager + External Secrets Operator | Secret 저장 서비스·IAM/Workload 인증·CRD/Operator·갱신·비용 검토 | Cloud 공급 자동화에 적합. AWS 전체 장애의 로컬 복구에는 별도 원본과 인증 경로가 여전히 필요 | 이미 사용 중이거나 비밀번호·Key를 주기적으로 자동 교체할 요구가 있으면 대안 |
| Sealed Secrets | Controller·암호화 및 Controller Key 백업·복원 운영 | Git 암호문 운영 가능. Cluster 삭제 전 Key를 확보하지 않으면 기존 암호문 재사용에 문제가 생김 | Cluster 외 Key 보관과 반복 재생성 부담을 함께 비교 |
| 보호 저장소 + 승인된 수동 Bootstrap | 초기 도입이 단순함 | 항목별 원본·버전·재주입·예비 보관자·복구 검증을 절차로 유지해야 함 | SOPS 운영이 일정에 맞지 않을 때 재검토 대안 |

SOPS는 값을 암호화하는 파일 도구이며 Secret 서버·권한 승인 시스템이 아니며 비밀번호·Key를 주기적으로 자동 교체하지 않는다. age를 선택해 로컬 Identity로 복호화하는 것은 AWS KMS 조회를 기본 의존성에서 제외하는 프로젝트 선택이다. 암호문과 Key를 한 곳에서 같은 권한으로 무제한 읽을 수 있으면 파일 암호화의 보호 경계가 약해진다. 담당자와 Host 관리자 접근 범위를 실제로 확인한다.

추가 AWS Secret 저장 서비스와 Operator는 기본 Runtime 공급 경로에서 제외하는 제안이다. RDS Master Credential의 AWS 관리형 보관 등 서비스 고유 기능은 3-D/3-F에서 별도 비교할 수 있다. 이를 이유로 Terraform State에 모든 Credential이 없다고 미리 주장하지 않는다. 설치 버전·ROSA/OpenShift·기존 On-Prem 도구 호환성은 구현 전에 고정·확인한다. 현재 실제 설치나 추가 서비스 비용 산정을 수행하지 않았다.

#### 3-C.12.3 공급·복구 원본과 보관 경계

암호화 Bundle은 적용할 Credential의 공급·복구 원본이다. 실제 유효성의 권위는 해당 IAM/GitHub/DB/Harbor 서비스에 있으므로 폐기된 Key를 Bundle에서 다시 꺼낸다고 유효해지지 않는다. Jenkins Credential과 Kubernetes Secret은 공급 원본으로부터 반영된 사용 사본이다. Console에서 사용 사본만 바꾸고 원본을 갱신하지 않는 이중 관리는 피한다.

| 논리 Bundle | 주요 내용 | 사용·보관 경계 |
|---|---|---|
| Cloud Bootstrap | ROSA IDP Client Secret, GitOps Repo Reader, Cloud App DB/Redis·실제 필요한 App Secret | 지정 Bootstrap 담당자만 복호화. Cloud Cluster에 필요한 항목만 공급 |
| Automation | ECR CI Key, GitOps Writer, Harbor Publisher, 필요한 Backup 전송 Credential | 목적별 파일·Jenkins Folder/Job/Host 범위. 일반 Build Job에 전체 Bundle이나 age Key를 주지 않음 |
| On-Prem Recovery | 로컬 DB/Redis·앱 Credential, Harbor Pull, 로컬 관리 경로, 데이터 해독에 실제 필요한 Key | Cloud 관리·CI Push Secret과 구분. AWS·GitHub·ROSA 조회 없이 사용할 로컬 복원본 |

Bundle은 범위별 논리 구분이며 한 파일에 모든 Secret을 몰아넣으라는 의미가 아니다. 실제 필요한 항목만 생성하고 수신자 접근이 다른 항목은 파일을 나눈다. 개인 AWS Admin Key·Root Credential은 공용 Bundle에 넣지 않는다. WireGuard의 각 Peer Private Key도 해당 Host/운영 담당자의 별도 암호화 원본으로 보관한다.

- 원본 저장 위치는 Git 밖의 권한 제한된 운영 보관 영역이다. 실제 Host·Storage 경로는 3-H 담당자·자산 확인과 연결한다. On-Prem 공용 NFS를 쓴다면 암호문 영역의 접근·삭제·백업 권한을 먼저 확인하며 개인 Key를 함께 두지 않는다.
- age Private Identity는 지정 보관자의 보호된 로컬 저장소에 두고 예비본은 별도의 암호화된 오프라인 매체에 보관한다. 암호화 매체의 해제 수단까지 AWS 로그인·같은 소실 Host·소실 Key에 순환 의존하지 않게 시험한다.
- 최소 주 보관자와 예비 보관자를 지정한다. 독립된 수신자 Key를 넣는 경우 둘 중 허용된 한 보관자만으로 복호화 가능하도록 하는 단순안이며, 2인 동시 승인이나 암호학적 분할 보관이 구현되었다고 주장하지 않는다. 사람별 배정은 아직 미정이다.
- 운영 암호문과 예비 사본을 같은 물리 Disk/Host 하나에만 두지 않는다. Recovery 사본은 장애 전에 On-Prem에 전달하고 복호화 시험 결과를 기록한다. 단순 암호문 복사만으로 준비 완료가 아니다.
- Bundle 개정 ID·적용 환경·암호문 Checksum·보관자·갱신일·검증 결과를 Index에 연결한다. 평문 Secret의 Hash, 실제 값, Private Key 또는 Credential이 포함된 명령·URL을 Evidence로 공개하지 않는다. Checksum은 암호문 전송 확인용이며 신뢰된 승인 Index와 실제 서비스 검증을 대체하지 않는다.
- SOPS YAML/JSON의 구조·필드명 등은 평문으로 남을 수 있다. 파일 전체를 아무 정보도 보이지 않는 형식으로 취급하지 않으며 민감한 접속정보는 암호화 값으로 분류하고 공개 Index에 복사하지 않는다.

이번 제안은 암호화 Secret 파일도 GitOps Repo에 넣지 않는다. 3-A의 네 저장소 경계를 유지하고 다섯 번째 Secret 저장소를 만들지 않는다. Infra에는 Secret 없는 공급 코드·Schema·예시, GitOps에는 참조·배포 설정, Docs에는 원본의 개정/검증 Index와 Runbook을 둔다. 암호화 Bundle의 원본 Storage와 백업 관리는 별도다.

#### 3-C.12.4 대상별 Source와 공급 Matrix

아래 대상은 논리 범위다. 실제 Username·Secret 이름·Namespace·Credential ID·ARN·값은 아직 작성하지 않았다. 실제 App Code/DB/IdP 요구를 확인하고 불필요한 항목은 만들지 않는다.

| 대상 | 발급·변경 책임 / 원본 | 소비 위치·공급 방법 | 재생성 / 복구 범위 |
|---|---|---|---|
| ECR CI Access Key | IAM 발급 후 Automation 암호화 원본 갱신 | 2차 Jenkins Credential, 단계 한정 Binding | Jenkins 재구축 때 공급 또는 재발급. ROSA 앱에 공급하지 않음 |
| Jenkins GitOps Writer | 만료를 둔 Fine-grained PAT, 지정 GitOps Repo Contents 쓰기만 기본. 발급자·Org 정책 확인 | 별도 Jenkins Credential, HTTPS Git 작업 | 개인 발급자와 연결됨. Repo 전체 파일에 대한 쓰기이며 환경 경로만의 기술적 제한은 아님 |
| Argo CD Git Reader | GitOps Repo 전용 Read-only Deploy Key를 우선 후보로 생성 | GitOps 설치 Namespace의 Repository Secret. SSH Host Key 확인도 함께 공급 | 새 Cluster에 재주입. Offline Restore 실행 시 GitHub Clone 성공을 필수로 두지 않음 |
| Harbor Publisher / Recovery Pull | 2차 Project 범위 Robot Credential, Push에는 필요한 Pull 포함 / 복구는 Pull만 별도 | Publisher는 전송 담당 Job, Recovery Pull은 로컬 Runtime의 Registry 인증 | 실제 Harbor 버전·Robot 만료·지원 권한 확인. 1차 사람 Admin 계정 공유하지 않음 |
| ROSA GitHub IDP Client Secret | OAuth App 관리자가 발급·교체 후 Cloud 원본 갱신 | 지원되는 IDP 설정·지정 Namespace Secret 경로 | 새 Cluster Callback·Mapping을 갱신. Cloud IDP를 로컬 복구 인증의 필수조건으로 두지 않음 |
| Cloud App DB / Backup DB | DB 관리자가 SQL 사용자·Grant와 함께 관리 | App는 Namespace Secret 참조, Backup은 해당 Job에 별도 Credential | RDS·DB 권한 유지 여부와 새 Cluster 접속을 별도 검증. DB Master와 분리 |
| Cloud Redis 인증 | 3-D-2 승인된 TLS+AUTH Token, 실제 Engine/Provider 입력 확인 | Backend의 실제 연결 형식에 맞는 Secret 참조, Primary Endpoint | Cloud Token·Runtime State를 로컬 Redis에 자동 복제하지 않음. 실제 TLS/Driver·State 영향은 확인 전 |
| App Signing / Data Encryption | 실제 Code 사용 여부 조사 후 기능별 원본·교체 규칙 작성 | App Namespace Secret | Signing 교체와 저장 데이터 해독 Key의 교체는 영향이 다름. 데이터 해독에 필요한 기존 Key는 함부로 재생성하지 않음 |
| On-Prem DB / Redis / App | 로컬 전용 사용자·권한·Credential과 Recovery 원본 | 로컬 DB 계정 재생성 및 Recovery Namespace Secret | Cloud Master·앱 계정을 그대로 복사하지 않고 실제 Restore와 연결을 검증 |
| 로컬 관리 / GitOps Bootstrap 비상 | 기존 로컬 관리 경로의 실제 담당자·회수 책임 확인 | 제한된 관리 접속용으로만 사용 | AWS·GitHub가 불가해도 접근 가능해야 함. 일반 팀 공용 일상 계정으로 확대하지 않음 |
| WireGuard 각 Peer Key | Gateway별 운영 담당자의 별도 암호화 원본 | 해당 Host의 제한된 파일 경로 | Cloud Gateway 재생성은 §Network 복구 절차와 연결. On-Prem 서비스 복구의 필수 의존성으로 두지 않음 |
| TLS Private Key / Red Hat Token 등 | 실제 TLS·OCM 인증 방식 선택 후 Inventory에 추가 | 필요한 실행 주체만 공급 | 만료 Token은 재발급, 인증서 체인은 호환성 확인. 3-E/3-F에서 실제 범위 결정 |

Fine-grained PAT는 전체 인적 계정 권한을 복사하는 범용 Token이 아니라 이번 자동화 목적의 별도 제한 Token 후보다. 그래도 발급자 계정에 연결되며 Org의 승인·만료 정책과 Branch Rule을 따른다. PR 생성 API까지 CI가 사용하면 필요한 Pull requests 권한만 추가 검토한다. 광역 classic PAT나 Ruleset 우회 권한을 조용히 추가하지 않는다. App Repo 비공개 Checkout이 필요하면 별도 읽기 Credential을 준비한다.

Deploy Key는 Repository 단위이며 자동 만료가 없는 점을 회수 계획에 포함한다. GitOps Reader에는 Write를 부여하지 않는다. 공개 Repo라서 인증 없이 읽을 수 있는 경우 읽기 Credential 자체가 필요 없는지 먼저 확인한다. Repo 공개 범위를 이번 Secret 선택으로 바꾸지 않는다.

#### 3-C.12.5 Resource Ownership과 주입 안전선

| Resource / 책임 | Owner | 다른 체계의 경계 |
|---|---|---|
| RDS/Redis/ECR/Network/State 기반 자원 | Terraform / 승인 Lifecycle | App 실제 Secret을 임의 생성해 State에 저장하지 않음 |
| Workload·Namespace·Secret 참조·환경 Endpoint | GitOps | 동일 이름의 빈 Secret/가짜 Password Manifest를 함께 관리하지 않음 |
| 프로젝트가 공급하는 Secret Object·값 | 지정 Secret 공급 절차 | Argo CD Application의 관리·Prune 대상에 중복 등록하지 않음 |
| Operator/서비스가 생성한 Secret | 해당 Operator/서비스 | 프로젝트 Bootstrap이 생성 값을 덮어쓰지 않음 |
| Jenkins Credential | 지정 CI 공급 담당자, 암호화 원본 개정과 일치 | 일반 App CI Job에 전체 원본·복호화 Key를 부여하지 않음 |

원본 해독 후 필요한 Secret만 표준입력/메모리 경로로 공급하는 구현을 우선한다. 불가피한 임시 파일은 Workspace·Git 밖의 권한 제한 영역에 두고 성공·실패 모두 정리한다. Shell Trace·Ansible 상세 출력·Plan/Log/Artifact의 Secret 노출을 막고 실제 값이 CLI 인자·History에 남지 않게 구현한다. 특정 구현 명령과 Provider 동작은 3-F에서 검증한다.

Kubernetes Secret의 base64 인코딩은 암호화가 아니다. API/RBAC·실효 권한·ROSA의 실제 저장 보호를 확인한다. Pod가 Secret을 읽는 데 일반적으로 Secret 조회 RBAC를 추가할 필요는 없으므로 App ServiceAccount에 무조건 get/list Secret 권한을 주지 않는다. Secret을 쓸 수 있는 Workload 변경/exec 권한의 영향은 §3-C.6과 연결한다.

초기 App 연결 형식은 실제 Code의 환경 변수 요구를 우선 확인한다. Secret을 환경 변수로 주입하면 변경 후 기존 Process의 값이 자동 갱신되는 것으로 취급하지 않고 승인된 Rolling Restart·재접속 검증을 수행한다. 파일 Mount 방식도 App Reload와 subPath 제약을 확인한다. Secret Bootstrap 변경은 평문 값 대신 비민감한 개정 ID로 Deployment 재시작 의도와 연결할 수 있으며 구현은 3-F에서 선택한다.

ROSA IDP Secret은 실제 지원되는 관리 경로에 적용하며 Terraform/RHCS에 Client Secret을 전달할 경우 State에 들어가는지 먼저 조사한다. RDS Master Credential·Provider State의 예외는 별도로 명시하고 State 접근/백업 보호를 검증한다. `sensitive` 표시나 SOPS 사용만으로 State-free를 선언하지 않는다.

#### 3-C.12.6 Clean Recreate 순서

1. 새 Cluster를 만들기 전에 지정 담당자가 암호화 원본·개정·복호화 Key·지원 도구·Bootstrap Code를 확보한다. 현재 Cluster의 Secret만이 유일한 원본이면 Gate 실패다.
2. 승인된 Terraform/RHCS로 Infra/Cluster를 준비하고 실제 대상 Cluster/API·Context와 관리 Caller를 확인한다. 만료된 이전 Cluster Token을 복원 원본으로 취급하지 않는다.
3. 공식 관리 경로로 최소 GitOps 설치를 수행하고 Repo Reader를 공급한다. Namespace 등의 기초 Desired State를 적용한 뒤 App Sync를 공급 완료까지 보류한다. 정확한 설치·인계는 3-F에서 구현한다.
4. IDP Client Secret·새 Callback·RBAC와 필요한 App Secret을 공급한다. 기존 Cloud DB가 유지된다면 서비스의 유효한 Credential과 원본 개정을 대조한다.
5. 승인 Release를 Sync하고 새 Pod의 ECR Pull·DB/Redis 연결·인증·App 기능을 확인한다. Node 재생성/새 Pod에서도 지원되는 ECR Pull 인증이 동작해야 하며 저장된 CI Token으로 대신하지 않는다.
6. Bootstrap 임시 평문·Credential을 정리하고 공급 개정·허용/금지 시험·동작 결과를 기록한다. 일반 Workload의 지속 Desired State는 GitOps로 관리하고 Bootstrap이 계속 직접 배포하지 않는다.

이는 AWS가 정상인 Cluster 재생성 절차다. AWS 전체 장애의 On-Prem Restore와 같은 성공 경로로 기록하지 않는다. ROSA 정상 Runtime은 주입 완료 후 On-Prem 암호문 저장소나 담당자의 age Key를 매 요청마다 조회하지 않는다. 다만 로컬 공급 주체 장애 시 새 Secret 공급·교체가 지연될 수 있고, 비밀번호·Key 교체는 담당자가 수행한다.

#### 3-C.12.7 AWS 조회 없는 On-Prem Restore 순서

1. 장애 선언 전에 승인 Image·Portable DB Backup·Recovery Manifest/Code·암호화 Recovery Bundle·age/SOPS 도구와 신뢰 설정을 로컬에 확보한다. Key의 예비 경로·해제 수단도 준비한다.
2. 시험에서 AWS 조회를 막고 GitHub·Cloud IDP·ECR·AWS KMS 조회에도 의존하지 않는 실행 경로를 확인한다. 로컬 관리 접속을 통해 보관자가 Recovery Bundle을 복호화한다.
3. Portable Backup으로 MariaDB를 복원하고 로컬 App/Restore용 사용자·Grant를 실제로 만든다. 데이터 Dump만으로 Cloud SQL 사용자·Grant가 모두 복원된다고 가정하지 않는다. 3-D-2에서 목적별 SQL 계정·논리 Dump/Import 도구를 선택했으며 실제 Version·사용자명·Grant·옵션은 확인 뒤 작성한다.
4. Recovery Redis Runtime·로컬 Secret을 공급하고 사전 보존한 Harbor Image로 App를 시작한다. Harbor·DB·Secret 공급 권한은 각각 검증한다.
5. Cloud/Recovery Endpoint·DB/Redis Credential·Signing 정책을 대조한다. 새 Signing Key를 쓰면 재로그인이 필요할 수 있으며 기존 Cloud Session/실시간 Game State 연속성을 보장하지 않는다. 저장 데이터를 해독할 Key가 필요한 App라면 호환되는 원본 Key를 별도로 확보한다.
6. Data/Application 기능·복구 시간·사용한 Backup/Release/Secret 개정과 평문 정리 결과를 기록한다. 이 경로의 완성도를 확인한 후에만 Offline Secret Gate 통과로 판단한다.

로컬 Credential을 Bundle 안에 복사한 것만으로 로컬 DB/Harbor에서 해당 Credential이 유효한 것은 아니다. 실제 계정 생성·Grant·만료·연결까지 시험한다. 장애 후 S3에서 Bundle을 받거나 AWS KMS로 해독해야 하는 경로는 이 Scenario의 합격 경로가 아니다. Backup·이미지·Secret·도구의 동기화 개정이 서로 맞지 않으면 Release/복구 준비 Gate를 통과하지 못한 것으로 기록한다.

#### 3-C.12.8 교체·회수와 검증 기준

Secret 공급 도구의 Key 교체와 서비스 Password/API Key 교체는 별개다. SOPS 수신자를 제거하고 파일 내용을 암호화하는 Key를 새 값으로 바꿔도 이미 확보된 구 암호문이나 실제 서비스 Credential이 자동 폐기되지 않는다. Key 노출 시 새 수신자/암호화 Key를 준비하고 공급 범위를 회수한 뒤 영향 받은 서비스 Credential도 교체·무효화한다. 이전 백업은 필요한 데이터 해독·보존 정책과 함께 접근 제한한다.

변경은 새 유효 Credential 준비 → 암호화 원본 개정 → 필요한 소비자 공급 → 실제 동작·로컬 예비 사본 확인 → 구 Credential 회수의 순서로 검토한다. Credential 두 개를 동시에 허용할 수 없는 서비스는 중단·복구 절차를 별도로 정한다. 서비스 중단 없는 DB 비밀번호 교체이 이미 구현되었다고 주장하지 않는다. Jenkins의 운영 백업과 `master.key`는 별도 보호·복원 경로로 관리하며 Controller 설정 복구는 서비스 Offline Restore의 필수조건으로 만들지 않는다.

| Gate | 합격 방향 / 보존할 결과 |
|---|---|
| 원본·Key 보존 | 주/예비 보관 경로에서 허용 담당자 복호화 성공, Key 없는 실행의 실패. 실제 값은 출력·Evidence 보존하지 않음 |
| 공급 범위 | Cloud/Recovery/CI별 허용 Secret만 공급, 다른 Namespace/Job·무관 Principal 범위를 확인 |
| GitOps Ownership | App Sync/Prune/Reconcile 후 프로젝트 Secret이 빈 값으로 덮이거나 중복 관리되지 않음. Namespace 삭제는 해당 Secret 소실이므로 재주입 절차 시험 |
| Clean Recreate | 기존 Cluster에만 있는 값 없이 새 Cluster를 준비하고 실제 사용자 로그인·새 Pod Image Pull·DB/Redis·App 기능 확인 |
| Offline Restore | AWS/GitHub/KMS 조회 없이 로컬 Image·Backup·Code·Bundle·Key로 실제 복구 |
| 개정 일치·교체 | 서비스 유효 Credential·암호화 원본·사용 사본·예비 사본 대조, 소비자 재시작/재접속과 구 Credential 회수 시험 |
| 노출·State | Git/Log/Artifact/History/Plan·State의 실제 보존 범위 확인. 민감한 출력은 사본 보존 없이 처리하고 예외·조치만 기록 |

Gate는 계획이며 아직 실행하지 않았다. PoC에서 SOPS/age·도구 호환성·보관 자산·초기 주입이 일정에 맞지 않으면 보호 저장소 + 승인된 수동 Bootstrap 대안을 비용·수작업·재현성 기준으로 재검토한다. 실제 PoC 실패를 현재 발생한 것으로 기록하지 않는다.

#### 3-C.12.9 후속 인계 — 승인 반영

3-C-3 승인 내용을 바탕으로 §3-C.13에서 작업 주체·Secret 목록·초기 공급 순서·권한 표·허용되지 않은 작업의 차단 시험을 정리했다. 3-C의 설계 선택과 후속 인계를 마무리하며 실제 설정·검증은 별도로 추적한다. 3-D에서는 Data 사용자·Backup/Restore·Redis 인증·데이터 해독 요구, 3-E에서는 App 인증·TLS, 3-F에서는 실제 Script/Provider/State/GitOps 구현, 3-G에서는 검증 Evidence, 3-H에서는 보관자·자산·시간·비용을 연결한다. Runtime 증거가 없으면 설계 완료와 검증 완료를 구분한다.

### 3-C.13. 3-C-4 계정·Secret 목록과 공급·검증 절차 정리

**정리 ID:** PH2-3C-HANDOFF  
**기준:** 3-C-1~3-C-3의 사용자 작업 전제 승인. 새로운 기술 선택이나 권한 확대를 이 정리만으로 승인하지 않는다.  
**결과:** 다음 설계에 넘길 목록·작업 순서·권한 기준·실행 전 입력·시험 기준을 작성했다. 실제 계정·정책·Secret 배정과 시험은 아직 진행 전이다.

#### 3-C.13.1 작업 주체와 권한 기준

| 작업 주체 | 작업 범위 | 공급할 인증정보 | 실제 설정 전 남은 입력 |
|---|---|---|---|
| 개인 AWS IAM User 4명 | 승인된 프로젝트 작업을 Admin 권한으로 수행 | 개인 Console 로그인·MFA, 필요한 담당자의 CLI 인증 | 실제 User·MFA·CLI 담당자·계정 상위 제한. 개인 Key를 공용 원본/CI에 넣지 않음 |
| Terraform 초기 기반 / 공통 기반 / ROSA 실행자 | 승인된 Lifecycle·State 범위로 실행 | 개인 인증에서 목적별 실행 Role 사용 | Trust·Action·ARN·State 경로·필요한 의존 출력 접근·인증 만료 대처 |
| ECR CI 전용 IAM User | 지정 Repo Push·필요 Pull 검증·Token 발급 | 별도 Jenkins Credential | 실제 CI User·Repo ARN·Policy·Credential ID·Job/Agent |
| Jenkins GitOps 변경 주체 | 지정 Repo의 승인된 Release 변경 | 별도 제한 PAT 후보 | 발급자·Org 정책·만료·Branch Rule·PR 권한 필요 여부. 특정 폴더만의 IAM식 제한은 아님 |
| GitOps Repo 조회 주체 | 필요한 Repo 읽기 | 읽기 전용 Deploy Key 후보, 공개 Repo면 필요 여부 재확인 | Repo 공개 범위·Key·SSH Host 신뢰 설정·GitOps 설치 Namespace |
| ROSA 사용자 / 관리 담당자 | 프로젝트 Team으로 로그인, 필요한 Namespace/Resource 권한 | GitHub IDP + 별도 RBAC | 실제 사용자 식별·Team·RoleBinding·관리 담당자. AWS Admin에서 자동 배정하지 않음 |
| Secret 공급·보관 담당자 | 허용 범위의 원본 관리·복호화·초기 공급·교체 | 범위별 age Identity와 대상 서비스 관리 경로 | 주/예비 보관자·암호문 저장소·Key 예비 보관·지원 도구 |
| Backup 전용 IAM User | 승인된 S3 Bucket/Prefix 업로드·다운로드·필요 조회 | 전용 Data VM에 별도 제한된 Access Key | 3-D-2 승인. 실제 Bucket/Prefix·Policy·Key 공급·검증은 3-F 입력 |
| Data Backup / 이전 / 로컬 복원 작업자 | 목적별 SQL 읽기·구조 변경/가져오기·복원 | 역할별 SQL Credential, 생성 Job에는 Backup age 공개 Recipient만 | 3-D-2 승인. 실제 사용자명·Grant·Client Source·Version 확인. 관리 비밀번호와 해독 개인 Key를 예약 Job에 일괄 공급하지 않음 |
| Cloud App / On-Prem Recovery App | 해당 환경의 DB·Redis·실제 필요한 App 인증 | 각 환경의 Namespace Secret 참조 | 실제 Code의 필드·접속 형식·권한·필요한 Signing/데이터 해독 Key |
| WireGuard Host / ROSA Operator | Gateway 관리 / 공식 Cluster 운영 | Host별 Key·Instance Role / 공식 STS Role | 실제 Gateway·SSM·공식 지원 정책. CI·사람 인증과 별도 |

AWS Human Admin 권한을 강제로 좁힌 구조는 아니다. Terraform 제한 시험은 해당 실행 Role Session에서, CI 제한 시험은 CI User에서 수행한다. Admin 인증으로 시험한 결과를 제한 계정의 결과로 기록하지 않는다. AWS `GetCallerIdentity`는 호출한 계정·Role 확인용이며 필요한 서비스 작업의 권한 검증을 대신하지 않는다.

2026-10-01 3-D-2 사용자 승인 후 IAM User 수를 다음과 같이 정리한다. ECR용 CI 계정은 3-C-2에서 이미 승인한 항목이며 이번에 추가로 생긴 ECR 선택이 아니다.

| IAM User 용도 | 계획 수량 | 사용 방식 / 권한 | 승인 출처 |
|---|---|---|---|
| 팀원 개인 작업 | 4개 | 개인 Console/MFA, AdministratorAccess. 필요한 담당자만 CLI 인증 준비 | 3-C-1 사용자 지정 운영안 |
| ECR CI Push | 1개 | Console 로그인 없이 제한된 Access Key를 Jenkins에 공급. 지정 Application Repo Push·필요 Pull 검증·Token 발급 | 3-C-2 |
| S3 Backup 전송 | 1개 | Console 로그인 없이 제한된 Access Key를 전용 Data VM에 공급. 지정 Bucket/Prefix Put/Get·필요 조회, 일반 Job의 삭제·Bucket 관리 제외 | 3-D-2 |
| 합계 | **6개** | 사람 4개 + 자동화 2개. AWS Account 수가 아님 | 실제 생성 여부 미확인 |

Root는 위 IAM User 수에 포함하지 않는다. ROSA Account/Operator STS Role, Terraform 실행 Role, SQL 계정, Redis AUTH Token도 IAM User 수에 더하지 않는다. ECR 전용 로그인 User를 ECR 내부에 별도로 만드는 방식이 아니라 AWS IAM User로 인증하고 ECR 로그인 Token을 발급하는 방식이다. ECR Token과 최초 IAM Access Key는 서로 다른 수명을 가지며 CI Token을 Runtime 장기 Pull Secret으로 복사하지 않는다. Runtime Pull은 ROSA에서 지원하는 별도 경로를 확인한다.

#### 3-C.13.2 Secret 목록의 필수·조건부 구분

| 구분 | 목록 | 포함·공급 조건 |
|---|---|---|
| 승인 모델상 필요 | ECR CI Key, Secret 묶음의 age 복호화 Identity와 예비 경로, ROSA GitHub IDP Client Secret | 실제 발급·초기 공급·교체·회수·복구 경로 기록 |
| 3-D-2에서 작업 전제로 선택 | Backup S3 Key, 목적별 SQL Credential, Cloud/Recovery Redis 인증, Backup 파일용 age Recipient/해독 Identity와 예비 보관 | 전용 Data VM·환경별 소비자·해독 담당자에 필요한 범위만 공급. Secret 묶음용 Key와 Backup 해독 Key를 목적별 분리. 실제 발급·Grant·Token·지원 옵션 확인 전 |
| 실제 구성 확인 후 필요 | Git Repo 읽기/쓰기 인증, Harbor 전송/Pull, Gateway Key | 공개 Repo·기존 지원 인증·실제 Job 위치에 따라 불필요한 장기 Key/계정을 추가 생성하지 않음 |
| App 조사 후 판단 | Signing Key, 저장 데이터 해독 Key, 외부 서비스 Token, 별도 Session 암호화 값 | Code·데이터 구조를 확인한 뒤 필요한 값과 복구 호환성 결정 |
| 후속 서비스 설계에서 판단 | RDS Master 관리 방식, TLS Private Key/인증서, Red Hat/OCM 실행 인증, 비상 관리 접속 | 3-D/3-E/3-F에서 지원 방식·만료·State 저장 영향을 확인. Cloud Redis는 3-D-2에서 TLS+AUTH로 선택했으며 실제 Provider/State 영향은 검토 전 |
| 공용 공급 대상에서 제외 | Root Credential, 팀원의 개인 AWS Admin Key, 만료된 이전 Cluster Token | 전 팀·CI·App가 읽는 암호화 묶음에 넣지 않음 |

계정 수와 Secret 수를 같게 세지 않는다. Role 기반 인증이나 Operator가 관리하는 항목에는 별도 장기 Access Key를 만들 필요가 없을 수 있다. 이 목록은 생성할 Credential의 확정 수량이 아니다.

3-D-2 승인된 Data Secret 공급 위치는 다음과 같다. 실제 Secret 값·경로·사용자명·Credential ID는 별도 보호된 운영 입력이며 이 표에 넣지 않는다.

| Data 항목 | 원본 / 공급 대상 | 오프라인 복구에서 필요한 것 |
|---|---|---|
| Backup S3 Key | Automation 암호화 원본 → 전용 Data VM 예약 Job의 제한된 설정 | AWS 장애 후 로컬 복원에는 이 Key로 AWS에 접속하는 단계를 요구하지 않음 |
| Cloud SQL App / 구조 변경 / Backup 읽기 | 목적별 Cloud/Automation 원본 → Backend 또는 승인된 개별 작업 | Cloud 비밀번호를 로컬 App·복원 계정에 자동 재사용하지 않음 |
| 로컬 SQL Restore / App | Recovery 암호화 원본 → 격리 복구 DB와 Backend | 실제 가져오기·App 실행에 필요한 권한과 도구, AWS 조회 없이 공급 |
| Cloud Redis AUTH Token | Cloud 원본 → 실제 Backend Secret / 서비스 설정 | Cloud Runtime을 그대로 승계하는 용도로 보관하지 않음 |
| 로컬 Redis 인증·TLS/CA | Recovery 원본/구성 → 별도 로컬 Runtime과 Backend | 새 Redis 연결에 필요한 값·신뢰 CA·호환 Client |
| Backup age 공개 Recipient / 개인 Identity | 공개 Recipient는 생성 Job, 해독 개인 Key는 주/예비 담당자와 별도 오프라인 보관 | 보관 중인 옛 Backup도 해독할 수 있는 Key·도구·Release 호환 자료 |

Secret 대장에는 다음 필드를 사용한다. 값은 대장에 쓰지 않고 별도 암호화 원본에서 공급한다.

| 필드 | 기록할 내용 |
|---|---|
| 목적·환경 | CI Push / Cloud App / 로컬 복구 등 |
| 발급·교체·회수 담당 | 실제 사람·서비스 관리 책임. 1차 담당을 자동 승계하지 않음 |
| 공급 대상·권한 | 논리 주체·허용 대상·필요 작업, 실제 접속정보는 보호된 운영 설정 |
| 원본·사용 사본 | 암호화 원본 개정과 Jenkins/Namespace/Host 적용 개정 |
| 유효기간·변경 조건 | 실제 만료, 노출·담당 변경·종료 시 교체/폐기 기준 |
| 복구 요구 | 새 Cluster에 재주입 / AWS 없는 로컬 사용 / 재발급 필요 |
| 확인 상태·결과 참조 | 미발급 / 공급됨 / 검증됨 / 폐기됨을 구분, 민감 값 없는 결과 참조 |

#### 3-C.13.3 초기 공급 순서와 확인 지점

| 순서 | 작업 | 다음으로 넘어갈 확인 기준 |
|---|---|---|
| 1 | 보관 담당자·예비 경로·암호화 원본·도구 확보 | 허용 담당자의 로컬 복호화와 Key 없는 실행 실패, 개정 일치 |
| 2 | 실제 AWS/Cluster/Host와 실행 계정 확인 | 대상 계정·환경·실행 Role이 승인 범위와 일치. 인증정보는 출력하지 않음 |
| 3 | 목적별 인증정보 발급·암호화 원본 개정 | 발급 서비스의 유효성·권한·만료 확인, 개인 Admin Key 재사용 없음 |
| 4 | Infra·Cluster 및 최소 GitOps 설치 | 공식 설치와 State 경계 확인. 기존 1차 자원을 자동 변경하지 않음 |
| 5 | GitOps Repo 읽기 인증 공급, 기초 Namespace 준비 | 승인된 Repo 조회·기초 구성 확인, App 배포는 Secret 준비까지 보류 |
| 6 | IDP·RBAC·환경별 App/Backup Secret 공급 | 대상 범위·실제 필드·관리 책임 확인, 다른 공급 방식과 중복 관리 없음 |
| 7 | 승인 Release 배포 및 실제 연결 시험 | 새 Pod Image Pull, DB/Redis·사용자 인증·서비스 기능, 허용/차단 결과 |
| 8 | 예비 원본 갱신·임시 값 정리·기록 | 사용 개정과 복구 사본 일치, 로그·파일 정리, 종료/회수 절차 확보 |

위 순서는 의존 관계를 정리한 것이다. Secret 신규 발급 시점과 기존 유효 원본 재사용을 구분하고, DB·Registry 실제 작업 순서는 3-D/3-F의 구현과 연결한다. CI 설정은 Cluster 없이도 가능한 작업이므로 이 표를 모든 작업의 강제 직렬 일정으로 취급하지 않는다.

로컬 복구는 §3-C.12.7의 별도 절차를 따른다. GitOps 자동 조회나 CI 성공이 없어도 로컬에 확보한 Code·Manifest·Image·Backup·Secret으로 수행 가능한 경로를 구성한다. 이때 Cloud 생성용 순서를 그대로 반복하지 않는다.

#### 3-C.13.4 허용·차단 시험과 결과 기록

| 대상 | 성공해야 할 작업 | 차단·실패를 확인할 작업 | 시험 조건 |
|---|---|---|---|
| ECR CI | 지정 Repo의 Push·필요 Pull 검증·Token 발급 | 무관 Repo Push, IAM 변경, Terraform 자원 변경 | 실제 CI 인증 사용. 파괴적 작업은 사전 정책 확인과 격리된 시험 자원에서만 확인 |
| TF 실행 Role | 해당 Lifecycle Plan/Apply·State 접근/잠금 | 무관 State·IAM/Infra 변경. 선언된 의존 출력 읽기는 허용 범위에 별도 기록 | 해당 Role로 실행하고 별도 승인 없는 공통 기반 전체 삭제를 시험하지 않음 |
| GitOps Reader / Writer | Reader Clone, Writer 승인된 변경 경로 | Reader Push, Writer 무관 Repo 접근 | 공개 Repo의 익명 읽기를 금지 실패로 세지 않음. Branch Rule·PR 정책 별도 확인 |
| ROSA 사용자 | 승인 Team 로그인·업무 Resource 작업 | 미승인 로그인·다른 Namespace·권한 변경·Secret 조회 | 실제 사용자 Session과 전체 RoleBinding 기준. 관리자 `--as` 시험은 별도 권한·조건 기록 |
| Secret 공급 | 지정 원본 복호화·해당 대상 공급 | Key 없는 복호화·다른 범위 접근·잘못된 대상 공급 | 자동으로 검색되는 개인 Key가 없는 격리 환경에서 시험. 값 출력 금지 |
| Backup / Restore | 승인 객체·SQL·검증 작업 | 무관 State Bucket·객체 삭제·DB 관리 범위 | 실제 작업 위치·도구 결정 후 허용 대상 작성. 유효 Dump를 보호하며 시험 |
| 환경별 App | 필요한 DB 읽기/쓰기·Redis 접속·App 기능 | 관리용 SQL·무관 Secret·다른 환경 접속 | 실제 Data/App 요구와 Network/SG 조건을 대조 |
| 회수·재공급 | 새 Credential 동작, 구 Credential의 새 요청 차단 | 만료·폐기 Key로 신규 인증·Token 발급 | 기존 Token/Session의 잔여 유효성과 구 암호문 접근은 따로 확인 |
| 새 Cluster / 로컬 복구 | §3-C.12.6 / §3-C.12.7의 실제 동작 | 원본·Key·Image·Backup 누락 또는 잘못된 개정 | 설계 문서나 Secret Object 존재만으로 성공 처리하지 않음 |

실제 IAM·RBAC Policy의 허용은 다른 정책·Binding·Trust·상위 제한의 영향도 받는다. 업무표만으로 기술적 차단이 구현된 것으로 기록하지 않는다. Network 차단으로 요청이 실패한 것과 인증·권한 거부도 구분한다. 정책 조회/모의 평가와 실제 서비스 요청은 각각의 검증 범위를 기록한다.

Evidence에는 시험 주체·대상 범위·기대한 결과·실제 결과·시각·원본/Release 개정·제약을 남긴다. Account ID·접속정보·Secret은 공개 기록에서 제거하고 실제 식별정보가 필요한 운영 대장은 보호한다. 실행하지 않은 시험은 미실행으로 남긴다.

#### 3-C.13.5 남은 입력과 후속 인계

| 인계 단계 | 필요한 입력 / 결정 |
|---|---|
| 3-D 이전 범위·Data | 실제 Source/Seed, SQL 사용자·Backup/Restore 도구·Job 위치, Redis 인증, 저장 데이터 해독 요구 |
| 3-E 서비스 연결 규약 | Endpoint·TLS·App 인증·환경 변수·Session/재접속 요구 |
| 3-F 구현구조 | 실제 공급 코드·Namespace·정책/State 경로·IDP Provider 지원·Jenkins/Argo CD 설정·Key 보관 구현 |
| 3-G 검증·결과 | 허용/차단·만료·예비 보관·새 Cluster·로컬 복구의 실제 결과 |
| 3-H 작업 분담·일정 | 사람별 담당·예비 보관자·Storage/Host·도구 설치·검증 시간·추가 비용 |

3-C의 설계 선택·정리·인계 문서 작성을 마쳤다. 아직 실제 계정 배정·정책 작성/적용·도구 설치·검증을 완료하지 않았으므로 구현 완료나 Runtime PASS로 기록하지 않는다. 03 전체 통합 검토에서는 후속 Data/App/구현 선택과의 충돌·비용·일정을 다시 확인한다. 기술적 권한 확대나 승인된 저장 방식 변경이 필요하면 변경 이유와 영향을 별도로 제안한다.

### 3-C.14. 공식 참고 자료

2026-10-01 KST 조회. 공식 기능·권장사항과 프로젝트 설계 제안을 구분한다.

- [AWS IAM Security Best Practices / Human Federation / Workload 임시 권한](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Identity Center Organization / Account Instance 차이](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-instances.html)
- [Identity Center Session 종료·기존 Role Session](https://docs.aws.amazon.com/singlesignon/latest/userguide/authconcept.html)
- [IAM PassRole 대상 Role / Service 조건](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)
- [ROSA Classic GitHub IDP / Team 제한 / htpasswd](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/install_rosa_classic_clusters/rosa-sts-config-identity-providers)
- [ROSA Classic IDP 접근 / cluster-admin / dedicated-admin](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/install_rosa_classic_clusters/rosa-sts-accessing-cluster)
- [ROSA RBAC Role·Binding·기본 Role 범위](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/authentication_and_authorization/using-rbac)
- [GitHub Org MFA 정책](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-two-factor-authentication-for-your-organization/requiring-two-factor-authentication-in-your-organization)
- [ECR 인증 Token의 Principal Scope / 12시간](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html)
- [IAM Roles Anywhere / X.509 Certificate](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html)
- [SSM Session Manager Instance 권한](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-instance-profile.html)

- [AdministratorAccess 관리형 Policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AdministratorAccess.html)
- [개인 IAM User MFA 설정](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html)
- [MFA 보호 API·장기 Key와 임시 Credential](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html)
- [ECR 지정 Repository Push Policy](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-push-iam.html)
- [Jenkins Credential 저장·범위](https://www.jenkins.io/doc/book/using/using-credentials/)
- [Jenkins Credentials Binding·Pipeline/Agent 경계](https://www.jenkins.io/doc/pipeline/steps/credentials-binding/)

- [SOPS 파일 암호화 지원](https://getsops.io/docs/)
- [SOPS age Identity / 여러 수신자](https://getsops.io/docs/usage/identities/age/)
- [SOPS 수신자 갱신·파일 암호화 Key 교체·노출 시 대응](https://getsops.io/docs/usage/key-management/)
- [Kubernetes Secret 참조·업데이트·base64·subPath](https://kubernetes.io/docs/concepts/configuration/secret/)
- [Argo CD Secret Management / Destination Cluster 공급](https://argo-cd.readthedocs.io/en/stable/operator-manual/secret-management/)
- [Argo CD Repository Secret](https://argo-cd.readthedocs.io/en/latest/operator-manual/declarative-setup/)
- [GitHub Fine-grained PAT / Repo·권한·만료·Org 정책](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- [GitHub Read-only Deploy Key·회수](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys)
- [Harbor Project Robot 범위·Secret·만료 — 실제 버전 호환성 별도 확인](https://goharbor.io/docs/2.10.0/working-with-projects/project-configuration/create-robot-accounts/)
- [Jenkins Backup / master.key 별도 보관](https://www.jenkins.io/doc/book/system-administration/backing-up/)
- [External Secrets Operator 외부 Source→Kubernetes Secret](https://external-secrets.io/latest/introduction/overview/)
- [Sealed Secrets Controller Key 복구](https://github.com/bitnami/sealed-secrets)

- [AWS 실행 계정 확인 GetCallerIdentity / 권한 시험과의 구분](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html)
- [Kubernetes RBAC 정책·권한의 합·실제 사용자 시험](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)

### 3-C 남은 입력과 실행

- [x] 3-C-2 CI 인증 다섯 가지 작업 전제 승인
- [ ] 실제 IAM User·MFA·CLI 필요·Key 보관·상위 계정 제약 확인
- [x] 3-C-3 Secret 공급·복구 다섯 가지 작업 전제 승인
- [x] 3-C-4 계정·Secret 목록·초기 공급 순서·권한·허용/차단 기준 정리
- [ ] ARN/Action/Condition, RoleBinding·실제 Subject·작업 계정 작성
- [ ] Runtime 허용/금지·회수·재생성·Restore 검증
- [x] 3-C 설계 정리·3-D 인계
- [ ] 3-D 이전 범위·Seed·Data 상세설계
- [ ] 3단계 전체 최종 검토 후 문서 확정

## 3-D Migration Seed와 Data

### 3-D.1. 기존 승인과 이번 설계 인계

현재 승인 구조는 ROSA Classic Multi-AZ, RDS MariaDB Multi-AZ, ElastiCache Valkey 7.2 Multi-AZ의 Cloud Primary다. On-Prem Jenkins를 유지하고 ECR을 Cloud 이미지 저장소로 사용하며 승인된 복구 Image·Portable Backup·설정·Secret을 장애 전에 On-Prem에 확보한다. On-Prem 복구는 DB 복원과 새 Redis Runtime을 사용한 서비스 복구이며 진행 중 Cloud Session/Room/Game의 무중단 승계를 주장하지 않는다.

3-A의 네 개 2차 저장소·1차 보존·Application 이력 보존 및 Seed 정책은 재승인 대상이 아니다. 3-C의 개인 IAM User 4개 + AdministratorAccess, 제한된 ECR CI User Key, ROSA IDP/RBAC, SOPS + age 및 담당자 공급 절차도 후속 설계의 입력으로 유지한다.

3-D-1에서 이전 시험 순서·데이터 경로·Release 조합·전환 판단을, 3-D-2에서 SQL 계정 분리·전용 Data VM·논리 복사·암호화 백업·Redis 접속을 작업 전제로 승인받았다. 3-D-3에서 실제 호환성을 확인할 버전 기준, 초기 자원 크기 후보·Storage 산정·작업 시간·서비스 재개 기준을 작업 전제로 승인받았다. 이번에는 승인 기록과 남은 입력을 정리해 3-E로 인계한다. Source Version·주소·데이터량·자원 가용성과 성능은 아직 확인 전이며 초기 제안을 측정 결과로 기록하지 않는다.

### 3-D.2. 3-D-1의 다섯 가지 승인된 작업 전제

| 번호 | 제안 | 적용 범위 |
|---|---|---|
| 1 | 격리된 2차 환경에서 이전 예행시험을 먼저 수행 | 1차 DB·Namespace·설정을 덮지 않고, 복사한 데이터와 2차 인증정보로 검증. 1차 읽기·부하·보관 영향도 실제 작업 전에 확인 |
| 2 | DB는 논리 덤프 생성 → RDS 가져오기 → 데이터·기능 검증을 우선 시험 | 데이터량·호환성·허용 작업 시간을 확인한 뒤 적합성을 판단. DMS/지속 복제를 기본 범위에 자동 추가하지 않음 |
| 3 | Redis는 새 환경의 Runtime으로 시작하고 재로그인·새 방/게임·재접속을 검증 | PVC/AOF 복사로 Cloud 진행 상태가 이어진다고 가정하지 않음. 기존 영속 데이터와 진행 중 상태의 처리 차이를 기록 |
| 4 | 코드·이미지·배포 설정·DB 구조·Secret 개정을 하나의 검증된 Release 조합으로 연결 | 같은 앱 Commit을 기반으로 Cloud/복구의 차이를 명시. Backup 시점과 구조의 호환성, Harbor 사전 보존 확인 |
| 5 | 전환 전 쓰기 제한·진행 작업 종료·최종 데이터 복사·검증과 되돌림 조건을 문서화 | 예행시험 성공과 실제 사용자 전환을 분리. Cloud에서 발생한 새 데이터를 버리거나 1차 DB에 합치는 작업을 자동 수행하지 않음 |

위 다섯 가지는 2026-10-01 사용자 동의로 후속 설계를 위한 작업 전제가 되었다. 결정 기록은 `PH2-3D-MIGRATION-FIRST`로 연결한다. 당시 작업 전제 승인은 실제 이전·전환 수행 기록이나 문서 최종 확정은 아니었다. 이후 전체03 최종 컨펌은 §3-I.12.4에 기록하며 실환경 결과에 따른 재검토 조건은 유지한다. 상위 Architecture 선택을 반복 승인받기 위한 표가 아니다.

### 3-D.3. 기능·책임별 이전 대응표

1차 열은 시작 기준점에 기록된 상태이며 이번에 실시간으로 조회한 결과가 아니다. 실제 Code·Manifest·Version·Runtime 결과를 구현 전에 대조한다.

| 대상 | 1차 기준 | 2차 대응 / 재사용 범위 | 추가 확인·검증 |
|---|---|---|---|
| Frontend / Backend | `seokpan-app`의 검증된 코드·Image·Test | 이력을 보존한 `seokpan-hybrid-app`에서 ROSA 적합성·환경별 연결 수정 | Source/의존성·Image 버전, 실행 UID·쓰기 경로·권한, DB/Redis/TLS·WebSocket 연결 |
| Kubernetes 플랫폼 | kubeadm·Calico 기반 On-Prem | ROSA Classic에 Workload를 적용, 기존 Control Plane/etcd를 그대로 이식하지 않음 | 실제 OpenShift 버전·기본 정책·Quota·Storage·운영 지원 경계 |
| 서비스 진입 | HAProxy/Common VIP·Gateway API | Cloud Public Ingress와 OpenShift Route의 확정 연결 규약을 3-E에서 작성 | 1차 VIP/인증서를 그대로 사용할 수 있다고 가정하지 않음. 도메인·TLS·WS·헬스 확인 |
| MariaDB | On-Prem MariaDB·MaxScale, 영속 데이터 기준 | RDS MariaDB Multi-AZ에 앱 DB와 필요한 사용자를 별도 준비 | Version·문자셋·Collation·시간대·Schema·Grant·지원 SQL·덤프 호환성 |
| MaxScale | 1차의 DB 연결·운영 경로 | Cloud에서는 RDS 연결 경로로 대체, 기존 On-Prem 자산은 보존 | App의 DB 주소/연결 동작을 수정. 로컬 복구의 MaxScale 재사용 여부는 별도 결정 |
| Redis | StatefulSet·PVC·AOF, Session/Room/Ready/Game/Turn/Vote | ElastiCache Valkey 7.2에 새 Runtime 구성, 로컬 복구도 별도 Valkey 7.2 계열 Redis 사용 | 인증·TLS·명령·연결·TTL·Pub/Sub 등 실제 Code 사용, 재로그인·재접속·상태 손실 영향 |
| App DB Schema 변경 | 일반 Backend Replica 시작 시 자동 수행하지 않음 | 별도 승인된 변경 작업·인증정보로 수행 | 실행 도구·시점·구조 버전·복구 가능성·중복 실행 방지 |
| Jenkins | On-Prem Build/Test/전달 | 유지, ECR Push와 Harbor 사전 보존 경로를 추가 | 실제 Jenkinsfile·Agent·제한된 인증·Image Scan·승인 Release 연결 |
| Harbor | On-Prem Registry | Cloud용 승인 Image의 로컬 복구 사본 보존 | 실제 버전·Project·Robot 권한·만료·Digest 일치·새 Pod Pull |
| Argo CD / Manifest | 1차 GitOps Desired State | 2차 전용 ROSA 구성과 별도 로컬 복구 구성을 분리 | 기존 Namespace/Role/설정 이름 자동 승계 금지. Secret 공급 책임과 충돌 확인 |
| NFS / Backup | 1차 Storage·Backup 자산 | 로컬 Portable Backup·복구 설정 보관 용도로 재사용 검토 | 1차 PVC를 Cloud에 그대로 Mount하지 않음. Storage 용량·권한·별도 사본 확인 |
| 관측·로그 | On-Prem Prometheus/Grafana/Loki/Alloy 등 | Cloud는 OpenShift 기본·User Workload Monitoring, 1차 Stack은 1차/복구 관측 자산으로 보존 | 중복 Cloud Stack이나 장기 로그 저장을 Must로 추가하지 않음. 삭제 전 결과 보존 |
| Secret | 1차의 기존 공급 체계 | 2차 환경별 암호화 원본과 공급 절차 | 1차 값 재사용을 기본으로 하지 않음. 필요한 데이터 해독 Key는 실제 요구 확인 |

### 3-D.4. Source와 Seed 확인 절차

1차 공식 종료일은 2026-09-23이다. 00_PROJECT_STARTING_POINT.md §5의 2026-09-30 Commit들은 당시 조회 참고값이며 현재 HEAD 또는 최종 Seed라고 기록하지 않는다. 구현 직전 최신 검증 상태에서 실제 Seed를 고정한다.

| Source | 사용할 정보 | 고정 시 기록 |
|---|---|---|
| `seokpan-app` | 실제 Code·Test·Container·CI 정의, 필요한 수정의 검증 상태 | 실제 Seed SHA·선택일·이유·검증 결과·미반영 수정·작성자 이력 |
| `seokpan-gitops` | 실제 Workload·환경 변수·Service·PVC·권한·배포 정의 | 참고 Commit·재사용 경로·ROSA용 변경 범위 |
| `seokpan-infra` | 실제 DB/Backup/복구·Secret·Host 자동화 | 참고 Commit·재사용 코드·외부 자원/1차 보호 조건 |
| `seokpan-docs` | CURRENT_STATE·변경 기록·실행/검증 문서·Troubleshooting | 문서 Commit·실제 검증과 계획의 구분·미해결 항목 |

Seed를 정하기 전 확인할 사항:

1. 앱 Build/Test·대표 기능과 이미지의 관계를 확인한다. 최신 날짜나 HEAD라는 이유만으로 검증된 것으로 취급하지 않는다.
2. DB 구조 변경 도구·실행 위치와 일반 Backend 시작 시 자동 변경 여부를 확인한다. App용과 구조 변경용 Credential을 분리한다.
3. Redis 재시작·Runtime 상태 손실 후 DB 영속 상태와 App 동작을 확인한다. 필요한 수정이 있으면 수정·검증 결과를 Seed에 연결한다.
4. DB/Redis 접속·TLS·Secret 필드, OpenShift 실행 정책에 맞는 Image인지 조사한다. 모든 앱을 관리자 권한으로 실행하는 우회를 기본으로 삼지 않는다.
5. 선택한 Seed를 보존하고 이후 1차 변경은 자동 동기화하지 않는다. 필요한 변경만 이유·영향·재검증 결과와 함께 반영한다.

2차 저장소를 실제로 만들거나 Seed를 고정하는 작업은 아직 수행하지 않았다. 1차 참고 SHA를 이 문서에 최종 Seed로 재기록하지 않는다.

### 3-D.5. 영속 데이터와 진행 상태의 구분

| 상태 | 원본 책임 | 이전·복구에서 확인할 범위 |
|---|---|---|
| Member / Game / Move / Result / Rating 등 | MariaDB | Schema·Row Count·대표 관계·Read/Write·앱 기능. 개인정보·실제 행 내용은 공개 결과에 노출하지 않음 |
| Session / Room / Ready / Connection Generation / 진행 중 Game / Turn / Vote | Redis | 무중단 승계를 Must로 두지 않고 재로그인·새 Runtime·재접속·진행 상태 처리 규칙 확인 |
| 앱 코드·Image·Manifest | 각 Source 저장소·Registry | Seed/Release Commit·Image Digest·배포 설정 개정·검증 결과 |
| Credential / Signing / 데이터 해독 Key | 승인된 별도 Secret 공급 체계 | 환경별 유효성·교체 영향·저장 데이터 해독에 필요한 Key 호환성 |

Redis가 새로 시작되었다고 DB에 진행 중으로 기록된 게임까지 올바르게 마무리되었다고 판단하지 않는다. 진행 중/완료/중단 상태를 어떤 규칙으로 정리할지는 실제 App Code·도메인 규약을 확인해 3-D/3-E에서 연결한다. DB에 보존된 Member·완료 Game·Move/Result가 정상 조회되는 것과 진행 중 세션 승계는 별도 시험이다.

**2026-10-05 Source 확인에 따른 복구 기능 경계:** DB에 보존된 과거 완료 Game/Move/Result/Rating의 무결성·관계 확인과, 이용자가 HTTP로 개별 과거 결과를 조회하는 기능은 구분한다. 현재 App의 `get_result`는 Redis의 현재 Room·Participation 및 `room.game_id`/`room.last_game_id`와 일치하는 Game에만 접근한다. 따라서 새 Redis에 기존 Room이 없는 복구에서 과거 개별 결과 API/화면의 재개를 기본 기능으로 보장하지 않는다. 보존 DB 기록은 SQL/데이터 비교로 확인하고, 지정 클라이언트는 재로그인·랭킹/회원 누적 기록·새 방/게임의 진행/완료 및 해당 현재 방의 결과를 검증한다. Source 근거와 추가 기능 확대 경계는 [§3-I.14.4](#recovery-app-scope-20261005)에 연결한다.

### 3-D.6. DB 논리 이전 우선안과 대안

| 방식 | 장점 | 부담 / 현재 판단 |
|---|---|---|
| 논리 덤프·가져오기 | 경로·검증·재실행을 설명하기 쉽고 Portable Backup/로컬 복구 설계와 연결 가능 | 데이터량·Version·DDL·일관성·허용 작업 시간을 측정해야 함. 우선 예행시험 제안 |
| 외부 MariaDB→RDS 복제 | 최종 데이터 차이를 줄이는 운영에 활용 가능 | 지원 Version·Binlog/GTID·Network·권한·전환/실패 처리 조사 필요. 현재 기본 범위에 넣지 않음 |
| AWS DMS | 초기 복사와 지속 변경 전달을 서비스로 운영 가능 | 추가 자원·비용·도구 학습·지원 Schema/제약·정리 작업 필요. 실제 데이터량/중단 제약이 우선안을 부적합하게 만들면 재검토 |

RDS MariaDB는 `mariadb-backup` 물리 백업을 그대로 가져오는 경로나 S3에서 직접 MariaDB 데이터를 가져오는 기능을 지원하지 않는다. 승인된 S3 보관을 RDS의 물리 복원 또는 직접 Import 기능으로 해석하지 않는다. 논리 파일은 실제 작업 Host·지원 DB Client로 전송·가져오며 경로와 권한은 다음 소단계에서 정한다.

대상은 앱 DB와 필요한 객체다. 기존 `mysql` 시스템 DB와 사용자·Grant를 통째로 덮어쓰는 방식은 사용하지 않는다. Source/Target Version·데이터량·Storage Engine·DDL 중단 여부·문자셋/시간대·Routine/Trigger/Event/DEFINER·필요 권한을 확인한 뒤 도구와 옵션을 선택한다. 정확한 덤프 옵션이나 무중단 이전 가능성을 지금 확정하지 않는다.

예행시험용 데이터 사본의 시점과 실제 사용자 전환용 최종 데이터 사본의 시점은 다르다. 복사 후 1차에서 발생한 변경이 자동 반영되는 것으로 기록하지 않는다.

### 3-D.7. 검증된 Release 조합과 전환 판단

Release 기록에는 App Commit·FE/BE Image Digest·GitOps Commit·DB 구조 버전·Secret 개정·검증 결과를 연결한다. Backup 생성 시각·대상 구조·암호문 사본·Harbor Digest와 맞는지도 확인한다. Secret 실제 값·DB 행 내용을 기록하지 않는다.

전환을 검토할 때 다음 조건을 확인한다.

1. 격리된 Cloud 환경에서 로그인·방/투표/착수/결과·대표 DB Read/Write·재접속·새 Pod 동작을 검증한다. 실제 필수 기능 목록은 3-E/3-G와 연결한다.
2. 신규 방/게임 진입을 제한하고 진행 작업을 마무리하는 방법과 시간을 정한다. 기존 Runtime 쓰기를 중지하는 실제 제어 수단이 없으면 단순히 절차에 적었다는 이유로 준비 완료로 처리하지 않는다.
3. 필요한 DB 쓰기 제한과 일관된 최종 데이터 사본 확보 후 RDS와 App를 확인한다. 전환 시간·데이터 차이·실패 시 중단 조건을 기록한다.
4. 사용자 요청을 어느 Endpoint로 보낼지는 3-E에서 정한 도메인·TLS·연결 방식과 함께 검증한다. 1차의 DNS·서비스를 이번 문서 작성만으로 변경하지 않는다.
5. 전환 실패 시 돌아갈 Code/Image/Manifest/DB 구조를 준비한다. Cloud에 새 데이터가 쓰인 후에는 DNS만 되돌리는 것으로 데이터가 일치하지 않으므로 추가 쓰기를 통제하고 보존·복원 방식을 따로 판단한다.

1차 서비스를 유지하는 것, Cloud 사용자 요청을 이전 대상으로 선택하는 것, Cloud 데이터로 On-Prem 복구를 수행하는 것은 서로 다른 작업이다. 실제 사용자 영향이 있는 중단·전환·데이터 덮어쓰기에는 당시의 구체적인 대상과 승인 범위를 확인한다. 이번 신규 작업 전제의 승인은 실행 전환을 이미 수행한 기록이 아니다.

### 3-D.8. 3-C에서 받은 입력과 다음 상세설계

| 입력 / 남은 결정 | 연결할 단계 |
|---|---|
| App DB / 구조 변경 / Backup / Restore 사용자와 Grant | 3-D-2 Data 사용자·논리 복사·복구 설계 |
| Dump 도구·작업 Host·용량·작업 시간·보관·전송 | 3-D Data 상세설계, 3-H 작업 분담·예산 |
| Redis 인증·TLS·연결·명령·Runtime 초기화 | 3-D Data, 3-E 서비스 연결 규약 |
| Signing/데이터 해독 Key·Session·진행 상태 처리 | 실제 App 조사 및 3-E 규약 |
| Secret 대상·Namespace·공급 코드·State 저장 영향 | 3-F 구현구조 |
| RPO/RTO·실패 주입·허용/차단·Release 결과 연결 | 3-G 검증 설계 |

실제 주체·Policy·사용자 수·Version·Size·Job 위치가 정해지기 전에는 3-C의 권한 표에 임의 ARN·SQL Grant·Credential을 채우지 않는다. 후속 선택이 승인된 경계를 변경하면 이유·영향과 함께 재검토한다.

### 3-D.9. 3-D-2 DB·백업·복구와 Redis 접속 승인된 작업 전제

#### 3-D.9.1 다섯 가지 승인된 작업 전제

| 번호 | 제안 | 선택 이유 / 경계 |
|---|---|---|
| 1 | App 실행·구조 변경/가져오기·백업 읽기·로컬 복원 SQL 계정을 목적별로 분리 | 일반 Backend와 주기 백업이 DB 관리자 권한으로 실행되지 않도록 함. DB 관리 계정은 초기 사용자 준비·필요한 관리 작업에만 사용 |
| 2 | On-Prem 전용 Data 작업 VM에서 이전·주기 백업을 실행하고 `systemd timer`로 예약 | ROSA 삭제와 작업 실행을 분리하고 추가 Cloud 작업 서버를 기본 구성에 넣지 않음. RDS는 VPN 사설 경로·TLS, S3는 Internet HTTPS로 연결 |
| 3 | 호환성을 확인한 `mariadb-dump` / `mariadb`로 앱 DB 논리 복사, InnoDB에는 `--single-transaction --quick` 우선 적용 | 도구·옵션은 Source/Target/복구 DB와 함께 시험 후 고정. 덤프 중 DDL을 제한하며 혼합 Storage Engine에는 동일한 일관성을 주장하지 않음 |
| 4 | 압축·age 암호화한 Portable Backup을 S3와 장애 전 On-Prem Recovery Storage에 보관, 현재 설계는 DB 운영 중15분 계획 주기·일반 사본7일 보관 — §3-I.14.5 | S3 업로드 후 복구 저장소로 다운로드·무결성 확인해 상위 경로 유지. 마지막 복원 검증 사본은 일반 정리 제외. 기존2026-10-01의1시간 승인 이력과 현재 설계/실제 달성 구분 |
| 5 | Cloud Redis는 TLS + AUTH Token + Primary Endpoint를 사용하고 로컬 복구는 별도 Redis Runtime으로 시작 | node-based Valkey 7.2·cluster mode disabled 선택에 맞춰 단순한 접속 방식을 적용. 재로그인·연결 재생성·중복 쓰기 방지 규약은 App 설계에 연결 |

위 다섯 가지는 2026-10-01 사용자 동의로 후속 설계를 위한 작업 전제가 되었다. 결정 기록은 `PH2-3D-DATA-BACKUP-CONNECTION`으로 연결한다. 실제 계정 생성·VM 구성·백업 실행·Redis 설정을 완료했다고 기록하지 않는다. 03 전체 최종 검토 전까지 변경 가능한 작업 전제로 관리한다. 이하 제안 시점 표현은 승인된 설계 선택으로 해석하며 실제 입력·구현·시험은 별도 상태로 추적한다.

이 표의 Backup 계획 주기는 §3-I.14.5의 2026-10-05 결정에 따라 15분이다. 이전 1시간은 당시 승인 이력으로 보존한다. PR #30의 병합으로 새 설계가 적용됐으며 실제 운영 주기·성공 간격·복구 최신성은 별도 시험으로 확인한다.

#### 3-D.9.2 SQL 계정과 인증의 책임

| 목적 | 사용 위치 / 수명 | 허용할 범위 | 제한 / 실행 전 확인 |
|---|---|---|---|
| App 실행 | Cloud Backend, 로컬 복구 Backend 각각 별도 Credential | 앱 DB의 필요한 `SELECT/INSERT/UPDATE/DELETE`, 실제 사용 시 추가 실행 권한 | DDL·사용자 생성·전체 서버 관리 권한 제외. 실제 쿼리·Stored Routine·ORM 동작 조사 |
| 구조 변경 / 초기 가져오기 | 승인된 Data 작업, 일반 Replica 시작과 분리 | 지정 앱 DB의 실제 변경·가져오기에 필요한 DDL/DML | `CREATE/ALTER/INDEX/DROP` 등을 도구·작업 내용에 맞춰 검토. 기존 대상 삭제가 필요한 경우 대상·백업·영향 확인 후 실행 |
| 백업 읽기 | 전용 Data 작업 VM의 주기 Job | 앱 DB 읽기와 실제 포함하는 객체·덤프 옵션에 필요한 메타데이터 권한 | 쓰기·DDL·사용자 관리 제외. View/Trigger/Routine/Event·Storage Engine에 따른 추가 권한을 실제 시험으로 확인 |
| 로컬 복원 | 별도 2차 복구 DB의 가져오기 작업 | 새 복구 DB와 필요한 객체 구성 | 1차 운영 DB·기존 사용자·Grant를 덮어쓰지 않음. 복원 후 App 실행 계정은 별도 공급 |
| DB 초기 관리 | 담당자의 제한된 초기 설정·관리 작업 | RDS가 허용하는 사용자·권한 준비 등 | Backend·주기 Job에 Master Credential을 공급하지 않음. 실제 RDS 관리 권한과 Secret 보관 방식 확인 |

Cloud와 로컬의 같은 역할도 비밀번호를 공유하는 것을 기본으로 하지 않는다. 원본 DB의 사용자·Grant는 필요한 부분을 조사해 대상에 별도로 구성하며 시스템 DB 덤프에 포함해 복원하지 않는다. 실제 사용자명·Host 조건·SQL Grant는 Version·Client Source·도구 확인 뒤 작성한다.

SQL 비밀번호와 Redis Token은 3-C의 환경별 암호화 원본과 담당자 공급 절차를 따른다. 백업 Job에는 백업 SQL Credential과 필요한 S3 Credential만 공급하고, Secret 묶음 전체의 age 개인 Key는 주지 않는다. 평문 비밀번호를 실행 인자·Shell 추적·Jenkins Console·공개 결과에 넣지 않는다. DB Client 설정 파일은 제한된 권한으로 공급하고 해당 Client의 옵션 순서·처리 방식을 검증한다.

S3에는 **백업 전용 IAM User의 제한된 Access Key**를 승인된 초기안으로 사용한다. 기존 개인 Administrator 계정·ECR CI User Key를 재사용하지 않는다. 승인된 Bucket/Prefix의 업로드·다운로드·조회에 필요한 `PutObject/GetObject` 및 제한된 `ListBucket` 범위를 검토하고, 일반 백업 Job에는 삭제·Bucket 관리 권한을 주지 않는다. IAM Policy·Bucket Policy·실제 ARN과 Key 공급 구현은 3-F에서 작성한다. Bucket을 공개하지 않으며 On-Prem HTTPS 경로를 막는 VPC Endpoint 전용 조건을 일괄 적용하지 않는다.

이 제안은 사람용 IAM User 4개의 AdministratorAccess 전제를 변경하지 않는다. 기존 CI용 IAM User와 별도로 Backup용 주체가 추가되는 설계다. AWS Instance Profile을 On-Prem VM에서 그대로 사용할 수 있다고 가정하지 않으며, 별도 인증 중계 서비스는 기본 범위에 추가하지 않는다.

#### 3-D.9.3 Data 작업 Host와 접속 경로

| 작업 위치 대안 | 장점 | 부담 / 현재 제안 |
|---|---|---|
| On-Prem 전용 Data VM | ROSA 삭제와 무관하게 Job·기록 유지, 로컬 도구·암호문 임시 보관 및 복구 준비를 한 곳에서 관리 | VPN·VM·전원·디스크의 가용성에 따라 최신 백업이 지연. VM·주소·용량 확보 조건으로 우선 제안 |
| ROSA CronJob | RDS 사설 연결이 간단하고 Workload 실행 구조 활용 가능 | Cluster 삭제 중 실행할 수 없음. ServiceAccount/AWS 인증·임시 Storage·로컬 전송 준비 필요. 현재 주기 백업의 기본 실행 위치로 선택하지 않음 |
| 별도 AWS 작업 EC2 | ROSA 삭제와 독립, IAM Role 활용 가능 | 추가 비용·패치·접속·Schedule·Lifecycle 관리 필요. On-Prem 실행안이 실제 요구를 충족하지 못하면 재검토 |

전용 Data VM은 VPN Gateway VM과 역할을 분리한다. 기존 1차 DB Host나 Jenkins Controller에 임의로 백업 Credential·높은 DB 권한을 추가하지 않는다. 같은 전용 VM에서 이전·백업 도구를 사용하되 예약 Job은 백업 읽기 권한만 사용하고 구조 변경·가져오기는 담당자가 별도 작업으로 실행한다.

접속 기준은 다음과 같다.

- RDS: 실제 Data VM Source `/32` → vRouter/전용 Gateway → WireGuard → AWS Gateway → RDS. 기존 3-B의 왕복 Route·NAT 예외·Source 보존과 일치하는지 확인한다. Data VM 확정 전 임의 주소나 전체 On-Prem CIDR을 SG에 넣지 않는다.
- RDS Client: RDS Endpoint DNS를 사용하고 TLS를 요구하며 신뢰 CA·서버 이름을 검증한다. TLS 1.2 이상을 지원하는 Client를 선택한다. 단순 TLS 옵션만으로 인증서 검증까지 된다고 가정하지 않는다.
- S3: 기존 Internet HTTPS로 승인된 Bucket/Prefix에 접근한다. RDS 데이터 경로와 S3 전송 경로를 분리한다.
- Recovery Storage: 승인된 On-Prem 경로로 접근한다. 실제 NFS/디스크·Mount 권한·용량과 Data VM 임시 디스크의 장애 영역을 확인한다.

정상 Cloud Backend는 RDS/Redis에 VPC 내부로 접속하며 Data VM·VPN을 경유하지 않는다. 따라서 VPN 장애 시험에서는 Cloud 요청이 정상 처리되는지와 최신 백업이 지연되는지를 각각 기록한다. 이 설계만으로 Gateway·Data VM·NFS의 HA가 확보되었다고 주장하지 않는다.

#### 3-D.9.4 논리 덤프와 가져오기 기준

앱 DB의 Storage Engine이 InnoDB이고 동시 DDL을 통제할 수 있을 때 `mariadb-dump --single-transaction --quick`을 우선 시험한다. InnoDB 외 테이블에는 같은 일관성을 보장하지 않으며, 덤프 중 `ALTER/CREATE/DROP/RENAME/TRUNCATE`와 구조 변경 작업을 겹치지 않게 한다. 혼합 Engine이 발견되면 제한된 쓰기 중단·별도 방식 또는 데이터 구조 조정 여부를 재검토한다.

Source MariaDB, RDS MariaDB, 로컬 복구 MariaDB, 덤프 Client와 가져오기 Client의 Version 조합을 함께 시험한다. 새 `mariadb-dump` 출력의 Sandbox 지시문을 구형 Client가 처리하지 못할 수 있으므로 최신 Client나 기존 `mysql` Client를 그대로 쓰는 것을 기본으로 하지 않는다. 검증된 Client Version·패키지/이미지 Digest와 실행 옵션을 복구 자료에도 보존한다.

| 확인 대상 | 처리 기준 |
|---|---|
| 대상 DB / 시스템 객체 | 앱 DB와 실제 필요한 객체만 포함. `mysql` 시스템 DB·전체 사용자/Grant는 가져오지 않음 |
| View / Trigger / Routine / Event / DEFINER | 실제 사용 여부·덤프 포함 여부·대상 생성 권한·실행 계정과 Event 재실행 영향을 조사. 누락이나 오류를 숨기지 않음 |
| 문자셋 / Collation / 시간 | Source·RDS·로컬 DB·Client의 조합을 맞추고 한글·시간 값·대표 결과를 검증 |
| 암호화된 앱 데이터 | 필요한 Signing/데이터 해독 Key와 호환성 확인. DB 파일만 복원해도 모든 데이터가 해독된다고 가정하지 않음 |
| 기존 대상 DB | 기본 복원은 새 격리 DB에 수행. 덤프 내부의 삭제·생성문을 실행 전에 검토하고 운영 대상에 바로 가져오지 않음 |
| 덤프 / 가져오기 오류 | 종료 코드·로그·누락 객체 확인. `--force`로 오류를 넘긴 결과를 정상 백업·정상 복원으로 처리하지 않음 |
| 구조 변경 순서 | 덤프에 포함된 구조와 App Release를 먼저 연결. 최신 Migration을 무조건 먼저 실행하거나 가져온 뒤 무조건 재실행하지 않음 |

일반 백업 파일을 새 복구 DB에 가져오는 시험과 실제 서비스 전환용 최종 복사는 구분한다. 일반 백업은 해당 덤프 Snapshot 시점의 사본이며 덤프 종료 시각까지의 새 쓰기가 모두 들어 있다고 기록하지 않는다. 전환용 최종 복사는 §3-D.7의 쓰기 제한·진행 작업 종료·최종 검증 절차와 함께 수행한다.

#### 3-D.9.5 암호화·S3 보관·로컬 사전 확보

생성 위치를 On-Prem으로 구체화하더라도 상위 Architecture의 **Portable Backup → S3 → 장애 전 On-Prem Recovery Storage** 경로를 유지한다. 다음은 실행 코드가 아니라 설계 순서다.

1. Job 중복 실행을 잠그고 대상·Credential 유효성·DB 상태·임시 공간·Recovery Storage 상태를 확인한다. 고유한 Backup ID와 작업 시작 시각을 기록한다.
2. DB TLS 연결로 논리 덤프를 생성하고 압축한 뒤 age의 Backup용 공개 Recipient로 암호화한다. 스트림 처리를 우선 검토하여 평문 SQL 파일을 장기 보관하지 않는다. 전체 단계의 종료 코드를 확인하고 중간 실패는 부분 파일로 남겨 정상 사본과 구분한다.
3. 암호문을 Data VM의 제한된 임시 경로에 완성하고 크기·SHA-256·도구 Version·DB 구조/Release·시점 정보를 기록한다. 정상 완료 전에는 최신 백업 표시를 갱신하지 않는다.
4. 승인된 S3 Backup Prefix의 고유 Object Key로 업로드한다. 기존 사본에 덮어쓰지 않고 업로드 성공 여부를 기록한다.
5. 그 S3 Object를 On-Prem Recovery Storage로 다운로드하고 암호문 SHA-256·크기를 비교한다. 부분 파일로 받다가 검증 후 최종 경로로 전환한다. 이 절차로 S3 경로와 로컬 사전 확보를 함께 검증한다.
6. S3 보관·로컬 확보 상태를 각각 기록하고, 둘 다 확인된 사본에 완료 상태를 붙인다. 실제 복원 검증은 별도 상태로 남긴다. 임시 사본 정리는 검증된 로컬 사본과 보관 규칙 확인 후 수행한다.

S3 업로드 실패 시 암호문 임시 파일은 삭제하지 않고 재전송 대상으로 보존한다. 필요하면 담당자가 로컬 Recovery Storage에 먼저 복사·무결성 확인해 임시 복구 후보로 등록할 수 있다. 이때 `로컬 확보 성공 / S3 보관 실패`를 그대로 기록하며 두 곳 보관 완료로 표시하지 않는다. 로컬 임시 파일만 있다는 이유로 이미 Recovery Storage에 안전하게 확보했다고 주장하지 않는다.

큰 Backup 파일 자체는 SOPS로 관리하지 않고 **age로 파일 암호화**한다. Secret 묶음과 Backup 데이터의 해독 Key는 목적을 분리하고, 공개 Recipient만 생성 Job에 둔다. 해독 개인 Key는 지정 담당자·예비 담당자의 보호된 보관과 별도 오프라인 사본으로 준비한다. 두 Recipient를 사용해도 두 사람이 함께 있어야만 해독되는 구조는 아니므로 그러한 통제를 주장하지 않는다.

새 Backup Key로 교체하더라도 보관 중인 옛 백업의 해독 Key는 해당 사본을 폐기할 때까지 확보한다. 개인 Key를 암호문과 같은 위치에 함께 두지 않는다. 백업 VM 관리자나 SQL 읽기 권한 보유자는 원본 데이터에 접근할 수 있으므로 공개 Recipient 사용만으로 생성 주체에게 데이터 접근이 전혀 없다고 설명하지 않는다.

Backup 기록에는 실제 Secret 값이나 행 내용을 넣지 않는다. 최소 항목은 Backup ID, Source/Target 역할, 시작·종료 시각, Snapshot 시점의 확인 수준, 구조 버전, 연결 Release, Client/압축/암호화 도구 버전, Recipient 식별자, 파일 크기·SHA-256, S3/로컬 상태, 복원 검증 결과다. 공개 제출 자료에는 실제 Bucket·계정·사설 경로·접속정보를 필요한 수준으로 가린다.

#### 3-D.9.6 초기 주기·보관과 실패 처리

| 항목 | 초기 제안 | 확인 / 재검토 조건 |
|---|---|---|
| 예약 실행 | 설계 기준: DB 운영 Window 중15분마다, `systemd timer`로 시작 — 시간당4회 계획 | 실제 덤프/전송·부하/공간을 확인. 중복 실행 금지·스케줄 jitter/생략/늦은 완료 기록.15분 Timer만으로 RPO30분 보장 아님 |
| 추가 백업 | 작업 종료·계획된 DB Stop 전, 중요 이전/구조 변경/장애 시험 전 | 마지막 쓰기와 백업 완료 순서를 확인. 해당 전환 시험은 쓰기 제한 절차와 연결 |
| 일반 사본 보관 | S3와 Recovery Storage에서 7일 | 실제 암호문 크기·시간당 건수·저장/전송 비용·로컬 용량 확인. 두 곳의 정리 상태를 각각 기록 |
| 보호 사본 | 마지막 복원 검증 사본·핵심 시험 전 사본·최종 검증 사본 별도 보존 | 일반 7일 정리와 S3 Lifecycle 적용 Prefix를 분리. 최종 검토·제출 후 팀이 정한 정리 시점까지 보관 |
| 실패 재시도 | 완성된 동일 Backup ID 암호문을 제한 재전송, 새 사본·기존 사본 혼동 방지 | 무제한 즉시 재시도 금지. 정상 성공 간격·로컬 확보 지연이 RPO30분에 맞는지 확인. 실패/지연으로 이전 사본만 있으면 실제 최신성과 미달 기록 |
| 계획된 DB Stop | 실행 Window 밖은 계획된 생략으로 기록 | 예기치 않은 DB/VPN 장애를 계획된 생략으로 숨기지 않음. Restart 후 새 정상 백업 확인 |
| 백업·로그 감시 | 사용 가능한 로컬 사본의 실제 Data 시각/나이·S3 성공·무결성/복원 검증 상태를 분리해 확인 | Data 나이와 진행 지연으로30분 목표 초과 전에 대응할 수 있도록 실제 관측/재시도 소요에 맞춰 경고.30분 초과/시점 불명확은 미달/미판정이지 알림 성공 PASS가 아님 |

일반 사본을 정리하더라도 마지막으로 실제 복원·App 확인을 통과한 사본을 새 검증 사본 없이 제거하지 않는다. 보호 사본은 주기 사본과 다른 경로에 두어 일괄 Lifecycle로 삭제되지 않도록 한다. 백업 Job의 S3 삭제 권한을 확대해 정리하지 않고 보관 정책은 별도 Infra 관리 책임으로 둔다.

S3와 On-Prem 각각의 저장 공간이 필요하며, 작업 VM 임시 디스크와 Recovery Storage가 같은 물리 디스크인지 확인한다. 적어도 마지막 복원 검증 사본은 Data VM과 다른 장애 영역의 로컬 보관 수단에도 확보하고 실제 읽기·해독 가능성을 점검한다. 실제 구성 확인 전에는 NFS Mount만으로 독립 사본·Storage HA가 확보되었다고 기록하지 않는다.

이 주기와 보관 기간은 비용 산정 전의 초기 설계값이다. 예상 암호문 크기·DB 운영 시간·7일 사본 수·보호 사본·S3 왕복 전송·RDS/Storage 잔존 비용을 3-H의 $500 Budget과 첫 Full Apply Cost Gate에 반영한다. 예산·Window·작업 시간이 맞지 않으면 주기/보관/Host를 함께 재검토한다. RDS Automated Backup/PITR는 별도 Cloud 복구 수단이며 Portable Backup으로 대체하거나 오프라인 복구 자료로 계산하지 않는다.

15분 후보는 기존1시간의4배, 철회된5분 후보의3분의1인 시간당4회 계획이다. 실제 요청/전송·암호문/임시 보관·DB 부하·실패 재전송은 그 비율로 확정되지 않으며 실제 Cost Ledger로 검증한다. 기존 S3 `hourly/` Prefix는 일반 예약 사본이라는 논리 이름으로 유지할 수 있고15분 간격과 혼동하지 않도록 대장/코드에 명시한다. Prefix 이름만 바꾸는 작업이나 추가 저장 서비스를 필수로 만들지 않는다.

#### 3-D.9.7 Redis 인증·TLS·접속과 재접속

<a id="data-engine-contract-20261006"></a>

**2026-10-06 Data 계약 v2.2:** 팀이 선택한 현재 엔진 목표는 **ElastiCache Valkey 7.2**다. 기존 node-based, cluster mode disabled, Primary 1 + Replica 1, Multi-AZ 구조는 유지한다. **TLS와 별도 AUTH Token을 생성 시부터 적용하며 App Read/Write는 Primary Endpoint DNS로 연결**한다. Reader Endpoint는 이번 실시간 Runtime의 기본 읽기 경로에 넣지 않는다.

[Infra #19](https://github.com/seokpan/seokpan-hybrid-infra/issues/19)의 Data 계약 v2.2에 따라 선택 엔진을 Valkey 7.2로 정합화했다. 이전 Redis OSS 승인 이력과 기존 Redis 7.2.4 시험 결과는 보존하되 Valkey 시험 성공으로 승계하지 않는다. **Data Root의 Valkey 전환 Source는 [Infra PR #37](https://github.com/seokpan/seokpan-hybrid-infra/pull/37)으로 병합됐고, 실제 생성·Valkey 호환성 시험은 별도다.** Cloud·lab·Recovery는 Valkey 7.2 계열을 사용한다. lab·Recovery의 정확한 Image Digest, 실행 파일·임의 UID·TLS/AUTH·명령/Lua/업무 호환은 실제 공급 개정과 B/C 검증으로 수락한다. `Redis`, `SEOKPAN_REDIS_*`, `backend-redis-*`, Terraform `redis_*` 논리 이름은 유지한다. **DB Pool 축소안은 미채택 후보이며 실측 연결 상한·종료 중 Pod 연결·부하를 확인한 뒤 B/C가 정한다.**

ElastiCache AUTH는 node-based 구성에서 사용할 수 있고 TLS가 필요하다. Serverless는 RBAC를 요구하지만 이번 선택은 Serverless가 아니다. RBAC가 더 세분화된 권한 제어를 제공하므로 여러 독립 App 주체나 명령별 제한이 실제 요구로 나타나면 재검토한다. 이번 AUTH 선택을 사용자별·명령별 최소 권한이 확보된 설계로 표현하지 않는다.

| 구분 | 접속·설정 기준 | 실제 검증 |
|---|---|---|
| Cloud Redis | Backend에 TLS·AUTH Token·Primary Endpoint·Port를 공급. 실제 Token 생성은 AWS의 길이/허용 문자 제약 준수 | 미인증·잘못된 Token·평문 연결 거부, 올바른 TLS/인증 연결 성공 |
| TLS Client | TLS 1.2 이상 지원, CA·서버 이름 검증. 검증 비활성화나 Node IP 고정을 기본으로 하지 않음 | 실제 Driver/라이브러리·Container CA·DNS·호스트 검증·새 Pod 접속 |
| Primary 변경 | Endpoint DNS를 다시 해석하고 실패한 연결 Pool을 교체, 제한된 재접속·대기 적용 | Failover 후 새 Primary로 복구하는지, 오류·공백 시간·실패 요청 확인 |
| 재시도 | 연결 재생성과 업무 쓰기의 재실행을 구분 | Vote/Move 등 결과가 불명확한 쓰기를 무조건 재실행하지 않음. 중복 방지·상태 조회·요청 식별은 3-E에서 구체화 |
| Pub/Sub / Session | 연결 단절 중 이벤트 누락과 재로그인·Room/Game 상태 확인 | 구독 재연결만으로 놓친 이벤트가 복원되었다고 판단하지 않음 |
| 로컬 복구 Redis | 2차 복구용 별도 Instance/Namespace의 새 Runtime, 자체 Credential·TLS/CA 공급 | Cloud Token을 그대로 재사용하지 않음. 기존 1차 Redis에 `FLUSHALL`하거나 데이터를 덮어쓰지 않음 |

AUTH Token은 Redis 서비스 비밀번호이며 AWS API Access Key나 SQL 계정과 다른 Credential이다. Backend에는 Redis Token만 주고 AWS 관리 Key를 Redis 접속용으로 공급하지 않는다. Token 교체는 새 Token 등록 → Consumer Secret 갱신·재연결 확인 → 이전 Token 제거 순서로 설계하고, 실제 Engine/API 지원과 소비자 교체 시험을 거쳐 실행한다.

On-Prem 작업 VM의 Redis 직접 접근은 실제 진단 목적이 정해졌을 때만 별도 허용을 검토한다. DB 백업용 `/32`를 Redis SG에 자동 추가하지 않는다. 기본 Redis 검증은 승인된 Cloud Backend/시험 Workload에서 수행한다.

TLS/AUTH가 네트워크 단절이나 비동기 복제의 데이터 손실을 없애지는 않는다. Failover와 새 로컬 Runtime에서 Session/Room/Game/Turn/Vote를 어떻게 종료·재생성할지는 실제 Code와 DB 상태를 대조해 3-E로 연결한다. Failover 후 진행 중 게임이 항상 이어진다는 보장은 하지 않는다.

Redis Token·DB Credential을 Terraform Resource에 전달하는 경우 Sensitive 표시는 State 저장 자체를 막지 않는다. 실제 Provider 필드·State 포함 범위와 3-C의 Secret 공급 예외를 3-F에서 검토한다. 이 문서에서 Token이나 SQL 비밀번호가 State에 전혀 저장되지 않는다고 확정하지 않는다.

#### 3-D.9.8 오프라인 복원과 RPO/RTO의 판정

| 단계 | 성공 조건 | 실패 시 처리 |
|---|---|---|
| 장애 전 준비 | Recovery Storage 암호문·개인 해독 Key·호환 Client·DB/Redis 도구·App/Image/설정·Secret·CA·Release 기록을 로컬에 확보 | S3 다운로드·AWS API·Cloud DB 접속을 장애 후 필수 단계로 남기지 않음 |
| 복구 사본 선택 | 로컬에서 실제 존재하는 사본의 무결성·해독 가능성·구조/Release 호환성 확인 | 최신 사본 실패 시 이전 검증 사본으로 내려가고 실제 복구 데이터 시점 변경 기록 |
| DB 복원 | 새 격리 2차 복구 DB에 가져오기 성공, 누락·오류·객체·대표 관계 확인 | 기존 1차 DB에 덮어쓰지 않음. 부분 복원은 초기화 범위 확인 후 새 격리 대상에서 재시험 |
| Data 검증 | Schema·테이블 수/행 수·대표 관계·Read/Write·시간/문자 값 확인 | Cloud 원본의 시험 종료 후 값과 Snapshot을 무조건 동일하다고 비교하지 않음 |
| 서비스 검증 | 새 로컬 Redis, Backend 연결·재로그인·랭킹/회원 누적 기록·새 게임 진행/완료와 현재 방 결과. 기존 완료 DB 기록은 SQL/데이터 비교로 별도 확인 — §3-I.14.4 | DB 가져오기 성공만으로 서비스 복구 완료 처리하지 않음. 새 Redis에서 과거 개별 결과 HTTP/화면 복구를 보장하지 않음 |
| 결과 보존 | 실제 장애/접속 불가 시작·탐지·선언/조치·클라이언트 업무 재개 시각, 사용 사본·데이터 시점·손실 범위·실패 원인 보존 | 실행 전 계획값을 달성 결과로 보고하지 않음 |

**15분 예약 주기는 영속 DB RPO30분 달성 결과가 아니다.** 실제 On-Prem 복구 데이터 시점은 장애 전에 로컬에 확보했고 실제 해독·복원에 사용한 Snapshot을 기준으로 한다. 생성·전송 지연, VPN/Job/Storage 장애, 계획된 Stop, 최신 사본의 복원 실패로 이전 사본을 선택한 시간까지 영향을 준다. 정상 성공 경로의 실제 Data 기준 시각 간 최대 간격＋Data→로컬 사용 가능 완성본 최대 지연＋시계/시점 불확실성이30분 이내인지 확인한다. Timer15분＋지연15분이라는 가정으로 보장하지 않으며 실제 사용 사본의 Data 나이가30분을 넘거나 시점을 알 수 없으면 미달/미판정으로 남긴다.

덤프 시작·종료 시각을 기록하되 종료 시각을 데이터 시점으로 쓰지 않는다. 정확한 트랜잭션 Snapshot 시각을 계측하지 못하면 덤프 시작 시각과 확인 수준을 보수적으로 기록하고, 시험용 식별 데이터·Commit 시각·복원 후 존재 여부를 함께 대조해 실제 손실 범위를 측정한다. 정확한 RPO 숫자를 얻지 못하면 시점 범위·확인한 손실을 보고한다.

RTO는 §3-G.7과 04 §10.2에 따라 **실제 장애 주입/접속 불가 시작 t0부터 Host 안내·지정 복구 클라이언트의 접속/재로그인·대표 업무/영속 Data 확인 완료 t1까지** 기록한다. 탐지·복구 선언/판단·담당자 대응 대기·Key 준비·DB 가져오기·새 Redis/App 기동을 구분하며, 늦게 선언한 시각으로 t0를 옮겨 앞의 시간을 빼지 않는다. 실제 장애 시작을 확인하지 못하면 불확실한 시점 범위를 남기고 정확한 RTO PASS를 주장하지 않는다. 자동 Public DNS 전환과 전체 사용자 트래픽 전환은 Must에서 제외하지만 지정 클라이언트의 실제 업무 검증은 필수다. 목표·시험 조건은 3-G에 연결하고 단순 Import 소요 시간과 서비스 복구 RTO를 혼동하지 않는다.

#### 3-D.9.9 승인 뒤 구현 전 확인사항

- [ ] 실제 Source/Target/로컬 MariaDB와 DB Client Version·Engine·앱 DB/객체·데이터량 확인
- [ ] SQL 권한·실제 DB 접속 Source·RDS CA·Backend TLS/Redis Driver 지원 확인
- [ ] 전용 Data VM·Source `/32`·예약 계정·디스크·Recovery Storage·독립 로컬 사본 확보
- [ ] 제한된 Backup S3 주체·Bucket/Prefix·Key 공급·Lifecycle 경로 확인
- [ ] 압축/age 도구와 Backup Recipient·개인 해독 Key의 오프라인 확보·옛 사본 해독 확인
- [ ] 덤프→S3→로컬 사본의 동일 SHA-256, 부분 실패·지연·중복 실행·보관 정리 시험
- [ ] DB 구조/Release 호환 사본의 실제 로컬 복원·새 Redis·Backend 검증
- [ ] 비용·작업 Window·백업 부하·RPO/RTO 측정계획과 최종 설계 정합성 확인

주소·Version·Size·Grant·실제 경로를 미확인 상태로 임의 채워 넣지 않는다. 신규 선택이 승인되면 3-C번의 Secret Index/목적별 주체 표와 3-B번의 실제 Job Host 입력을 갱신하되, 별도 계정·VM을 실제 생성했다는 상태로 바꾸지 않는다.

#### 3-D.9.10 다음 소단계 인계

3-D-2 승인에 따라 §3-D.10에서 **3-D-3 Version·Sizing·Storage·작업 Window와 Data 검증 입력**을 정리한다. 이번 도구/주기안이 가능한지를 판단할 실제 입력, Cloud/로컬 DB 구조 호환성, 진행 중 DB 상태 정리 요구, RDS/Redis·임시/복구 Storage 용량, 측정 전 가정과 검증 기준을 연결한다. 실시간 요청·WebSocket·재접속·중복 처리의 상세 규약은 3-E에서 설계한다.

### 3-D.10. 3-D-3 버전·초기 용량·Storage·작업 시간 승인된 작업 전제

#### 3-D.10.1 다섯 가지 승인된 작업 전제

**기록 ID:** PH2-3D-VERSION-CAPACITY-RUNTIME  
**승인일:** 2026-10-01 KST — 최신 사용자 동의

| 번호 | 제안 | 이유 / 실행 전 조건 |
|---|---|---|
| 1 | 실제 Source와 호환되는 DB/Redis/Client 조합을 먼저 시험하고 검증된 버전·구조를 Release에 고정 | 이번 이전과 불필요한 Major Upgrade를 한 번에 묶지 않음. On-Prem→RDS뿐 아니라 RDS→로컬 논리 복원도 확인 |
| 2 | RDS 초기 후보는 `db.t4g.small`, Multi-AZ DB instance, gp3 20 GiB | 작은 검증 환경의 시작 후보. 데이터·Index·로그·증가량·연결 수·덤프 부하와 Region/Version 가용성·비용 확인 후 적용 |
| 3 | Redis 초기 후보는 `cache.t4g.small` 2개, `maxmemory-policy=noeviction` | Primary 1 + Replica 1·Multi-AZ 유지. Room/Game Key가 메모리 압박으로 임의 제거되는 것을 피하고 쓰기 실패를 명시적으로 처리 |
| 4 | Data 작업 VM은 2 vCPU·RAM 4 GiB부터 검토하고 임시·보관·복원 공간을 실제 파일 크기로 산정 | OS 영역과 데이터 영역을 구분. 7일 사본·보호 사본·실패 재전송·Import 작업 공간, 독립 로컬 사본을 함께 계산 |
| 5 | ROSA와 Data의 가동 시간을 별도로 관리하고 서비스 재개 전 DB·Runtime 상태를 확인 | RDS Stop 전 최종 백업, Redis 유지/계획 재생성 조건, 소실 Runtime에 대응하는 중단 처리와 완료 기록 보존을 연결 |

이 다섯 가지는 **다음 설계를 위한 3-D-3 승인된 작업 전제**였으며 이후 전체03 최종 컨펌 범위에 포함되었다. 문서 승인은 구현·시험 완료를 뜻하지 않는다. 자원 크기는 실제 성능·최종 비용을 확인한 값이 아니며 버전 숫자·지원 조합·가용 주소·디스크 용량을 임의 확정하지 않는다. 당시3-D-2의 계정·Host·백업 경로·1시간/7일 승인은 이력으로 보존한다. 현재 후보는 §3-I.14.5의15분/7일이며 역할/Host/암호화·경로는 유지한다.

#### 3-D.10.2 버전과 구조 호환성 확인

| 대상 | 먼저 확인할 입력 | 고정할 기준 |
|---|---|---|
| 1차 MariaDB | 실제 Server Version·Storage Engine·문자셋/Collation·SQL Mode·시간대·사용 객체 | 원본 조회 결과와 참고 Commit. 기존 문서에 없는 버전을 추정하지 않음 |
| RDS MariaDB | 서울 Region에서 생성 가능한 Engine Version·Class·Multi-AZ·Storage 조합, 지원 종료·업데이트 조건 | Source와 호환되는 지원 버전 우선. Major 변경이 필요하면 이유와 양방향 논리 복원 시험을 별도 기록 |
| 로컬 복구 MariaDB | 실제 복구용 Server 패키지/이미지와 Cloud 덤프의 호환성 | RDS에 올라간 구조·SQL·데이터를 가져올 수 있는 검증 버전. 구형 1차 DB Server를 그대로 복원 대상으로 가정하지 않음 |
| Dump / Import Client | `mariadb-dump` 출력과 `mariadb` 입력 호환성, TLS·CA 지원·옵션 | 패키지 Version 또는 Image Digest·실행 옵션을 고정하고 오프라인에 확보 |
| Valkey 7.2 / Redis Driver | 실제 1차 Server·Backend Driver Version, 사용 명령·Lua·TTL·Pub/Sub·TLS/AUTH | node-based ElastiCache에서 지원되고 App 시험을 통과한 조합. 최신 태그로 매번 바뀌지 않도록 고정 |
| DB 구조 / App Release | 실제 Migration 도구·구조 버전·FE/BE Commit 및 Image Digest | Backup 구조와 실행 App 호환성 기록. 가져오기와 Migration 실행 순서를 검증 |

동일 제품명이나 동일 Major 계열만으로 호환성이 입증되었다고 판단하지 않는다. 새 RDS에서 추가한 구조·객체·SQL이 옛 로컬 DB에서 처리되지 않을 수 있으므로 **원본→RDS→로컬 복원**을 하나의 시험 묶음으로 둔다. 실제 지원 버전은 생성 직전 다시 확인한다.

Freeze 전 실제 검증 조합을 고정하고 이후 변경은 변경 이유·영향·다시 수행한 시험과 함께 기록한다. AWS/플랫폼의 필수 유지보수까지 영구 차단할 수 있다고 주장하지 않으며 Engine 업데이트·Parameter Group Family·Client 호환성에 따른 재검증을 계획한다. OpenShift/ROSA·Terraform Provider 버전은 각각 3-E/3-F와 연결하며 이 Data 문서에서 숫자를 임의 선택하지 않는다.

#### 3-D.10.3 RDS 초기 크기와 변경 조건

`db.t4g.small`은 공식 사양상 2 vCPU·RAM 2 GiB의 Burstable Class이며 MariaDB 지원 목록에 포함된다. gp3는 MariaDB에서 20 GiB부터 선택할 수 있다. 이를 **초기 검증 후보**로 제안하며 실제 서울 Region·Engine·Multi-AZ 조합의 생성 가능성과 Account Quota는 확인 전이다. Standby를 읽기 분산용 서버나 추가 App 용량으로 계산하지 않는다.

| 항목 | 초기 기준 / 판단 | 측정·재검토 조건 |
|---|---|---|
| Class | `db.t4g.small`, 기존 Multi-AZ DB instance 유지 | CPU·여유 메모리·Swap·CPU Credit·연결·응답 시간과 덤프 동시 부하. 지속 과부하 시 Medium 등 지원 Class·전체 비용 재비교 |
| Storage | gp3 20 GiB부터 검토 | 실제 Import 후 데이터·Index·DB 로그·시험 증가량·작업 여유가 들어가는지 확인. 부족하면 첫 생성 전에 산정값으로 변경 |
| Storage 확대 | 초기에는 자동 확대를 기본으로 켜지 않고 Free Storage를 관측, 필요 시 사전 용량 변경 | 늘린 RDS 할당 공간은 제자리에서 축소할 수 없으므로 크기와 비용 검토. 자동 확대 채택 시 상한·경고·부하 시험을 함께 검토 |
| DB 연결 수 | 실제 `max_connections`와 관리/백업 여유에서 App Pool을 산정 | Backend 최대 Replica × Replica당 Process × Process당 Pool/Overflow + 작업 연결이 허용 범위를 넘지 않는지 확인 |
| Backup 동시 부하 | 동일 대상에 주기 덤프 한 개, DDL과 겹치지 않음 | 대표 Read/Write 지연·덤프 시간·임시 공간·연결 종료·재시작. 예약 간격을 넘으면 부하·도구·주기 재검토 |
| 별도 Cloud 복구 시험 | PITR/복원 자원·보관·시간은 별도 계산 | Source RDS의 비용만으로 추가 복원 DB 비용까지 포함했다고 기록하지 않음 |

20 GiB를 실제 데이터량이라고 기록하지 않는다. 초기 Storage 판단은 최소한 **Import 후 Data+Index, DB 로그·여유 작업 공간, 시험 기간 증가량, 사용률 여유**를 포함한다. 압축 백업 크기로 RDS 저장 공간을 대체 계산하지 않는다. 구체적인 사용률·연결·응답 경고값은 3-G의 부하·관측 기준에 연결한다.

연결 Pool은 지금 App Process/Replica 수를 모르므로 임의 숫자로 고정하지 않는다. RDS 자동 Failover 후 DNS·기존 연결 폐기·새 연결·Transaction 재시도를 확인하며 실패한 업무 쓰기를 무조건 중복 실행하지 않는 규약은 3-E에서 정한다.

#### 3-D.10.4 Redis 용량·Key 보관과 메모리 압박

초기 후보는 `cache.t4g.small` Primary 1 + Replica 1이다. 공식 표의 노드당 메모리는 1.37 GiB이며 **두 노드의 메모리를 합쳐 2.74 GiB의 데이터 공간이라고 계산하지 않는다.** 서비스 예약 메모리·연결/버퍼·복제·객체 Overhead를 제외한 실제 사용 가능 영역을 확인하고 예상 Runtime 크기와 비교한다.

`maxmemory-policy=noeviction`을 초기 제안으로 둔다. 이번 Redis에는 Session뿐 아니라 Room/Game/Turn/Vote 상태가 있어, Key를 용량 압박 때문에 임의 제거하면 상태 일부만 사라질 수 있다. 이 판단은 프로젝트의 상태 책임에 따른 선택이며 AWS가 모든 Redis에 같은 정책을 요구하는 것은 아니다.

`noeviction`에서도 Key의 정상 TTL 만료는 발생하고 메모리 압박 시 일부 쓰기 명령이 실패할 수 있다. 이를 가용성 보장으로 설명하지 않는다. App은 Redis 쓰기 실패를 사용자 오류·요청 결과 확인·제한된 재시도·새 Room/Game 진입 통제와 연결해야 하며 해당 시험이 실패하면 그대로 통합 완료로 처리하지 않는다.

| 확인 항목 | 필요한 입력 / 시험 |
|---|---|
| 실제 Key 유형 | Session·Room·Ready·Game·Turn·Vote·Connection Generation·Lock 등 실제 Code에서 사용한 Key와 자료형 |
| TTL·정리 | 각 Key의 정상 만료·갱신 조건, 게임 종료/연결 종료/실패 시 정리. 임의 TTL로 진행 중 상태를 삭제하지 않음 |
| 최대 동시 상태 | 시험 동시 사용자·Room/Game·관전/구독·WebSocket 연결·누적 Key. 목표 수는 3-E/3-G에서 결정 |
| 실제 메모리 | Key별 대표 크기와 전체 Peak, Engine/Database 메모리, 복제·Client 버퍼·여유, Eviction과 쓰기 오류 |
| CPU·네트워크 | Engine CPU·CPU Credit·연결 증가·Pub/Sub 메시지·TLS 처리·복제 지연 |
| Class 변경 | Small로 검증 기준을 충족하지 못하면 불필요한 Key/Pool/누수부터 조사하고 Medium 등과 비용 비교 |

Micro는 더 작은 시작 후보이나 현재 상태 책임·측정 전 여유를 고려해 Small을 먼저 제안한다. Small이 필요 충분하다는 성능 결론은 아니다. 메모리 부족을 숨기기 위해 Multi-AZ/Replica를 제거하거나 정책을 임의 변경하지 않는다. 장기 Runtime 보존·Snapshot으로 진행 게임 무손실 승계를 보장하는 범위도 추가하지 않는다.

#### 3-D.10.5 로컬 작업·보관·복원 Storage 산정

전용 Data 작업 VM은 초기 2 vCPU·RAM 4 GiB, OS/도구용 디스크 40 GiB부터 검토한다. 실제 Host 여유·이미지/도구·처리 시간에 따라 조정하며 **40 GiB에 7일 백업까지 모두 보관할 수 있다고 가정하지 않는다.** 임시 백업 영역은 별도 디스크/경로로 산정하고 기존 1차 Data/CI/VPN Host와의 자원 경합을 확인한다.

| 구분 | 포함해야 할 공간 | 산정 / 분리 기준 |
|---|---|---|
| Data VM 임시 영역 | 현재 생성 사본·재전송 대기 사본·부분 파일·작업 Log/Client Cache | 정상 한 건만의 크기로 산정하지 않음. 실패 대기 건수와 재시도 상한을 포함 |
| On-Prem Recovery Storage | 7일 예약 사본·추가 사본·보호 사본·다운로드 임시 공간 | 실제 보관 개수 × 최대 측정 암호문 크기 + 작업 여유. 기존 NFS 여유/다른 업무 사용량 확인 |
| S3 | 같은 예약·추가·보호 사본, 미완성 Multipart 작업 정리 필요 여부 | Prefix별 Lifecycle·실제 도구의 Upload 동작·추가 Version 보관 여부 확인 |
| 로컬 복원 DB | 가져온 Data/Index·로그·Migration 임시 공간·시험 증가량 | 압축 백업 크기와 별도로 측정. 1차 운영 DB Data Directory와 분리 |
| 로컬 Redis/App | 별도 Runtime·Image/도구·CA·설정·관측 Log | Backend 의존성·Volume 요구를 확인하고 AWS 조회 없이 준비 가능해야 함 |
| 독립 로컬 사본 | 최소 마지막 복원 검증 사본과 필요한 호환 도구/Release | 같은 물리 디스크를 다른 Mount로 두 번 연결한 것을 독립 사본으로 세지 않음 |

15분 계획 주기의 예약 사본 수는 `N = 7 × H × 4 + E + P`로 둔다. H는 하루 최대 DB 운영 시간,4는 시간당 계획 건수, E는7일 동안 추가 생성할 사본 수, P는 일반 기간 밖 보호 사본 수다.24시간 DB 운영이면 예약 사본 계획은 최대672개이며 성공 실적이 아니다. 중복 보호 사본·실제 Window·jitter/실패/재전송/임시 파일은 실제 개수로 조정한다. 과거1시간 기준의168개 산정은 현재 계획 주기의 용량으로 재사용하지 않는다.

Recovery Storage의 초기 계획 용량은 `1.3 × (N × B + W)` 이상으로 검토한다. B는 대표 시험 중 최대 압축·암호화 사본 크기, W는 다운로드 부분 파일·검증 작업 등 실제 필요한 추가 공간이다. **1.3은 계산한 필요량에 30%를 더하는 계획 여유이며 실제 Storage 사용률·파일 크기 측정값이 아니다.** 성장·실패 대기 증가와 다른 업무 사용량을 별도 반영한다.

Data VM 임시 영역과 로컬 복원 DB도 같은 방식으로 해당 작업의 실제 Peak와 성장 여유를 계산한다. 스트림 해독/가져오기를 사용하면 불필요한 평문 SQL 사본을 줄일 수 있으나 DB Import 공간·오류 Log·작업 버퍼는 남는다. NFS를 모든 DB Data Directory의 기본 Storage로 채택하는 것은 이번 승인 범위가 아니다.

#### 3-D.10.6 작업 시간·예약·자원 수명

| 자원 / 작업 | 가동·보존 원칙 | 순서 / 확인사항 |
|---|---|---|
| ROSA | 기존 Validation Window 단위 생성·삭제 | 삭제 전 시험 결과·승인 Release·설정/Secret·복구 Image 확보, Data 자원 수명과 분리 |
| RDS | Data는 보존, 미사용 기간 Stop 후보 | App 쓰기 제한·진행 작업 확인 → 마지막 백업의 로컬 확보 → Client 종료 → Stop 완료 상태 확인. 다음 시험 전 Start·연결·Data 확인 |
| Redis | 인접 시험 사이 유지, 긴 미사용 구간은 계획 재생성 비용과 비교 | RDS처럼 Stop 비용 모델을 적용하지 않음. 재생성 선택 시 신규 진입 제한·Runtime 처리·결과 보존·Terraform 변경·Secret/Endpoint 재공급·App 재확인 |
| Data VM / VPN | RDS Dump 실행 Window에 필요 | ROSA가 없어도 Data 작업이 필요한 동안 유지. Gateway/NAT 정리와 남은 DB·S3 전송 의존성 확인 |
| 백업 예약 | 설계 기준: DB 운영 Window의15분 계획 주기·시간당4회 | RDS Stop 구간은 계획 생략 기록, Restart 후 새 성공 사본 확보. 전송/확보 실패는 계획 생략으로 처리하지 않음. 실제 성공 간격/최신성에 따라 RPO30분 별도 판정 |
| Import / Restore | 측정된 완료 시간과 검증 시간을 예약 | 생성·Upload·Download·해독·Import·App 시작·대표 검증 시간을 각각 기록.15분 예약과 전체 업무 RTO10분 목표는 서로 다른 기준 |

RDS는 연속 7일 Stop 후 자동으로 시작할 수 있으며 Stop 상태에서도 Storage·Backup 비용이 남는다. 기동·정지는 즉시 끝난다고 가정하지 않는다. 다음 작업 전에 실제 상태·유지보수·예산을 확인한다.

ElastiCache는 미사용 상태에서도 노드가 존재하면 과금되며, 노드 비용을 멈추려면 삭제가 필요하다. 따라서 Redis 사용 시간은 ROSA 시간과 자동으로 같아지지 않는다. 기존 Architecture의 `유지 또는 Terraform Re-create`를 구체화하며, Console 임의 삭제나 foundation 전체 Destroy를 비용 절감 절차로 사용하지 않는다. 재생성은 해당 자원의 계획 변경으로 관리하고 RDS·ECR·Backup S3·State를 함께 삭제하지 않는다.

첫 Full Apply 전에 RDS Multi-AZ와 Storage, Redis 2노드의 실제 유지 시간, ROSA, NAT/Gateway/IPv4, Backup 보관·전송, 필요 복원 시험 자원까지 비용을 합산한다. 정확한 가격·시간과 Budget 여유는 3-H에서 산정하며 **현재 Small 후보 두 개만으로 $500 충족을 판정하지 않는다.** 가동 계획이 예산을 넘으면 Class·Window·보관·재생성을 다시 검토하고 상위 Must를 조용히 제거하지 않는다.

#### 3-D.10.7 Data 정합성과 Runtime 소실 후 서비스 재개

서비스 재개 기준은 **완료된 DB 기록 보존 + Runtime을 잃은 진행 상태의 명시적 처리 + 새 Session/게임 검증**으로 제안한다. DB를 가져왔다고 Redis의 진행 상태까지 복구되었다고 판단하지 않는다.

| 상태 | 재개 전 확인 / 초기 제안 | 3-E·실제 Code 확인 |
|---|---|---|
| Member·완료 Game·Move/Result·Rating | Snapshot에 포함된 영속 기록을 보존하고 SQL/데이터 비교로 관계·대표 기록을 확인. App의 과거 개별 결과 접근은 새 Redis와 구분 — §3-I.14.4 | 계정 인증·완료 여부·Rating 계산 시점·멱등 조건 |
| DB에 진행 중이지만 대응 Redis Runtime 소실 | 유지보수 상태에서 해당 대상을 식별해 중단 상태로 정리하는 방향 | 실제 상태 필드·대상 판정·별도 중단 상태/기존 상태 사용 가능성 확인. 자동 정상 이어하기로 표시하지 않음 |
| 결과 / Rating | 중단 대상에 임의 승패·착수·새 Rating을 만들어 완료 처리하지 않음 | 실제 Transaction 경계·이미 반영된 결과/Rating과 중단 처리 충돌 확인 |
| Session·Room·Ready·Turn/Vote | 재로그인·새 방/게임 기준으로 Runtime 구성 | 만료·실패 메시지·재접속 안내·중복 요청·재참여 제한 규약 |
| 새 업무 | 정합성 확인과 App 대표 Read/Write·새 게임 시험 후 진입 허용 | 실제 유지보수/입장 차단 수단, 처리 순서와 허용 조건 |

진행 중 상태의 정리는 승인된 별도 작업으로 수행하고 반복 실행해도 이미 완료한 기록·결과가 바뀌지 않도록 설계한다. 실제 필드·Code·Schema를 확인하기 전에 임의 SQL이나 상태명을 실행하지 않는다. 로컬 복구를 새 Runtime으로 시작하는 시험과 Cloud Redis Failover 후 일부 Runtime이 남는 시험은 영향이 다르므로 같은 정리 절차를 무조건 적용하지 않는다.

#### 3-D.10.8 실제 입력·검증·후속 인계

| 필요한 입력 / 결과 | 연결 단계 | 다음 판단에 쓰일 내용 |
|---|---|---|
| 실제 Source·Seed 후보·DB/Redis/Client/Driver Version | 구현 전 Source 조사 | 호환 Version·검증 순서·Major 변경 필요 여부 |
| 데이터/Index 크기·압축 암호문 크기·덤프/복원 시간 | Data 예행시험·3-G | RDS/로컬 Storage·백업 부하·주기·허용 작업 시간 |
| Process/Pool·최대 Replica·동시 사용자·Room/Game·Key/TTL | 3-E 서비스 규약·3-G 부하 | DB 연결 상한·Redis Peak·App 오류 처리 |
| 실제 VM 여유·NFS/독립 Storage·주소·경로 | 3-F 구현·3-H 담당/자산 | VM 가용성과 경합, Backup 보관·복원 가능성 |
| 서울 Region/Version/Class/Quota·현재 단가·운영 시간 | 3-F 입력 검증·3-H Cost Gate | 생성 가능한 조합과 $500 내 실행계획 |
| 진행 중/완료/중단 상태와 결과·Rating 처리 | 3-E·실제 Code 조사 | Runtime 소실 후 정합성·재개·중복 처리 시험 |

현재 확보한 입력은 승인된 설계 문서와 공식 제품 사양이다. 실제 AWS Account·프로젝트 GitHub/Runtime·DB에 접속해 수집한 결과는 없으며 초기 후보를 성능 합격 또는 실제 설치값으로 보고하지 않는다.

3-D-3 승인에 따라 §3-D.11에 **3-D 설계 정리·미확인 입력 인계**를 기록하고, 3-E에서 **3-E 서비스 연결 규약**을 이어간다. 같은 선택을 반복 승인받지 않고 새로운 경계 변경이 있을 때만 이유·영향을 제안한다. 전체 최종 검토에서는 3-B Network·3-C 계정/Secret·3-D Data의 실제 실행 주체·설정·복구·비용을 함께 확인한다.

### 3-D.11. 3-D 설계 정리와 후속 인계

#### 3-D.11.1 설계 범위 대조

| 범위 | 승인·설계 위치 | 남은 실제 입력 / 검증 | 인계 대상 |
|---|---|---|---|
| 1차 보존·2차 분리·Seed·Release 조합 | §3-D.2~4·§3-D.7, 3-A 저장소 문서 | 실제 검증 Commit·Schema·Image·배포 설정·Secret 개정·백업의 조합 | 구현 전 Source 조사·3-F·3-G |
| DB 논리 이전·전환·되돌림 | §3-D.6~7·§3-D.9.4 | 실제 데이터량·Client/Engine 호환성·허용 작업 시간·Cloud 새 데이터 처리 | 이전 예행시험·3-G·3-H |
| SQL 권한·작업 VM·접속 경로 | §3-D.9.2~9.3, 3-B Network·3-C 계정 문서 | 실제 Host·SQL Grant·TLS/CA·왕복 Route·VM 여유 | 3-F 구현·접속 시험 |
| 암호화 Portable Backup·로컬 확보·복원 | §3-D.9.4~9.8·§3-D.10.5 | 생성·S3 업로드·로컬 다운로드·무결성·실제 복원 각각의 결과 | 3-F 자동화·3-G 장애/복구 시험 |
| DB/Redis 버전·초기 크기·Storage | §3-D.10.2~10.5 | 가용 Version/Class·용량·Peak·CPU Credit·Connection Pool·운영 단가 | 3-E·3-F·3-G·3-H |
| 진행 중 상태·재개·재접속 | §3-D.5·§3-D.9.7·§3-D.10.7 | App 인증·상태 필드·중단 처리·쓰기 결과 확인·중복 방지 | 3-E-2 서비스 상태 규약 |
| ROSA/Data 가동 시간·비용 | §3-D.10.6, 3-B Lifecycle | 실제 실행 Window·최종 백업 확보·Start/Stop/재생성·전체 $500 예산 | 3-F Lifecycle·3-H Cost Gate |

위 범위의 책임·초기 선택·실패 영향·검증 조건을 대조했으며, 현재 Data 설계에서 제안 수를 다섯 개로 맞추기 위해 제외된 독립 범위는 확인하지 못했다. 실제 입력과 실행 결과는 별도 확인사항으로 남아 있다. 이는 전체 시스템에 누락이 없다는 최종 판정이 아니며, 3-A 통합 검토에서 다른 설계와 다시 대조한다.

#### 3-D.11.2 인계 판정과 진행 조건

**3-D의 설계 정리와 후속 인계는 완료한다. 실제 데이터 이전·백업·복구 시험 완료는 아니다.** 승인된 전제와 확인할 입력을 분리했으므로 3-E의 사용자 진입·TLS·설정·연결 수명 설계를 이어갈 수 있다. 실제 경로·Port·인증 방식·상태 필드는 Source를 확인한 뒤 구현한다.

- 3-E는 DB 영속 기록과 Redis Runtime의 책임 구분, Runtime 소실 시 명시적 중단 처리, 결과가 불명확한 쓰기의 무조건 재실행 금지를 입력으로 받는다.
- 3-F는 전용 Data VM·SQL/IAM 목적별 계정·백업 도구·Secret 공급·별도 Data Lifecycle을 구현 구조로 연결한다.
- 3-G는 네트워크 접속 성공, 사본 생성 성공, 로컬 확보 성공, 실제 복원 성공, App 재개 성공을 서로 다른 결과로 남긴다.
- 3-H는 덤프/복원 시간·가동 시간·비용·담당자·마감 Gate를 실제 입력으로 계산한다.

기존 선택을 같은 표현으로 반복 승인받지 않는다. 신규 선택 또는 기존 경계를 바꾸는 실제 제약이 생기면 이유·영향·대안을 제시한다. 3-E-1·3-E-2는 3-D-3 이후 별도로 작업 전제 승인을 받았다. 3-D-3 승인만으로 3-E 선택을 자동 승인한 것이 아니며, 현재 서비스 규약은 3-E의 승인 상태를 따른다.

#### 3-D.11.3 제안 묶음과 문서 번호의 의미

최근 소단계에서 다섯 묶음으로 제시한 것은 검토를 위한 표현 방식이었으며 설계 요구사항의 개수 제한이 아니다. 3-A에는 여섯 승인 항목이 있다. 후속 제안은 독립적으로 선택할 결정의 수에 맞춰 묶고, 실행 세부사항·이미 승인된 입력·미확인 사실을 개수를 맞추는 새 제안으로 취급하지 않는다.

02번은 상위 Target Architecture를 통합한 문서다. 03 상세설계에서는 저장소(문서 03)·Network(04)·계정/Secret(05)·Data(06)·서비스 연결 규약(07)으로 책임과 검토 범위를 나눈다. **문서 관리번호와 프로젝트 진행 단계는 별개**이며 문서 07 작성이 프로젝트 07단계 진입을 뜻하지 않는다. 기존 파일명과 구분은 유지한다.

### 3-D.12. 참고 자료와 검증 상태

- 업로드 시작 기준점 §4~5·§8·§12: 1차 실제 Source와 당시 Commit, 상태 책임, Seed 원칙.
- 업로드 Charter §2·Target Architecture §9~10·§11~13·§19: 최신 검증 Seed, DB/Redis·복구·전달·관측·Secret 전제.
- [AWS RDS MariaDB 데이터 가져오기 방식·제약](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MariaDB.Procedural.Importing.html)
- [AWS Redis OSS 복제 방식 — Primary/Replica와 비동기 복제](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.Redis.Groups.html)
- [MariaDB mariadb-dump — 옵션·일관성·Client 호환성](https://mariadb.com/docs/server/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump)
- [AWS RDS TLS와 CA·서버 검증](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html)
- [AWS RDS MariaDB TLS 지원](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MariaDB.Concepts.SSLSupport.html)
- [AWS ElastiCache AUTH — 지원 구성·TLS 전제·Token 변경](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/auth.html)
- [AWS ElastiCache 연결 Endpoint](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Endpoints.html)
- [AWS ElastiCache TLS](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/in-transit-encryption.html)
- [age 공식 프로젝트 — Recipient 암호화와 Identity 해독](https://github.com/FiloSottile/age)
- [AWS RDS Class별 MariaDB 지원](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.Support.html)
- [AWS RDS Class별 CPU·메모리 사양](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.Summary.html)
- [AWS RDS gp3 Storage 범위](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html)
- [AWS RDS Storage 확대·축소 제약](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.Autoscaling.html)
- [AWS RDS 일시 Stop·Multi-AZ·7일 후 시작·잔존 비용](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StopInstance.html)
- [AWS ElastiCache 노드 사양·메모리·CPU Credit](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html)
- [AWS ElastiCache Parameter Group·maxmemory-policy](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ParameterGroups.Engine.html)
- [Redis 공식 Key 제거 정책·noeviction](https://redis.io/docs/latest/develop/reference/eviction/)
- [AWS ElastiCache 생성·유지 과금·삭제](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.Create.html)
- [AWS ECR 인증·IAM Principal과 Token](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html)

공식 자료는 2026-10-01 조회했다. 업로드 Source와 승인된 작업 문서, 공식 기능 제약을 대조했으며 실제 프로젝트 GitHub/Runtime/DB 결과를 새로 조회하지 않았다. 계정 분리·Host·주기/보관·Backup S3 주체·로컬 Redis 독립 선택은 3-D-2의 승인된 프로젝트 작업 전제다. 3-D-3의 초기 Class/Storage·메모리 정책·작업 시간·재개 기준은 승인된 프로젝트 작업 전제이며 공식 문서가 그대로 정한 요구사항으로 표현하지 않는다. 실제 논리 이전의 적합성·작업 시간·데이터량·가용 용량·비용·RPO/RTO는 측정 전이다.

### 3-D 남은 입력과 실행

- [x] 3-D-3 다섯 가지 작업 전제 승인
- [ ] 실제 Source·Version·데이터량·App 요구와 검증 상태 확인
- [x] 3-D 설계 정리·미확인 입력 및 후속 단계 인계
- [ ] Source별 참고 Commit 및 구현 직전 Application Seed 고정
- [ ] 3-E~3-H 후속 상세설계
- [ ] 실제 이전·재생성·복구·전환 시험
- [x] 03 전체 통합 검토·사용자 최종 컨펌 반영

## 3-E 서비스 연결과 업무 규약

### 3-E.1. 서비스 연결 설계의 범위

3-D는 이관·백업·복구·초기 크기·가동 시간의 설계 기준과 미확인 입력을 정리했다. 3-E는 이를 실제 사용자 요청과 App 동작에 연결한다. 3-E-1에서 사용자 진입 위치, TLS 구간, 환경별 설정 공급, Pod 시작·종료 시 연결 경계를 작업 전제로 승인받았다. 3-E-2에서 사용자 인증·Session 유효성, WebSocket 재접속, 쓰기 결과 확인·중복 방지, DB/Redis 부분 실패의 처리 기준을 작업 전제로 승인받았다. 이번에는 §3-E.17에서 전체 설계를 정리해 3-F로 인계한다. 실제 인증 형식·게임 메시지·DB 필드는 Source 확인 후 연결한다.

이 절은 Data 설계와 App 동작을 연결하는 상세설계다. 저장소·Network·IAM·Data·App·IaC·시험·WBS는 이 단일 문서의 3-A~3-H에서 다룬다.

제안 수는 고정하지 않는다. 3-E-1에서는 네 연결 경계를 승인받았고, 3-E-2에서도 인증·재접속·쓰기 중복·부분 실패의 네 결정 경계를 승인받았다. 이미 승인된 입력과 구현 세부사항을 새 제안으로 추가하지 않으며, 새로운 독립 결정이 드러나면 별도로 다룬다.

### 3-E.2. 기존 승인 입력과 유지할 책임

| 입력 | 이번 설계에 적용할 내용 | 승인·상세 기록 |
|---|---|---|
| Cloud Primary와 Public 기본 Ingress | ROSA Classic Multi-AZ의 사용자 접속 경로를 유지. 정상 게임 서비스는 Hybrid VPN에 의존하지 않음 | 02·3-B |
| RDS MariaDB / Valkey 7.2(Redis 프로토콜) | DB는 영속 업무 기록, Redis는 Session/Room/Game 등 Runtime. TLS·목적별 인증과 Endpoint를 구분 | 3-C·3-D |
| Secret 공급 | 환경별 비밀값은 3-C 공급 절차와 Secret 참조로 연결. FE에 DB/Redis·IAM·Signing 비밀값을 전달하지 않음 | 3-C |
| Release 조합 | 같은 검증 App/Image와 환경별 배포 설정·Schema·Secret 개정·Backup 호환성을 연결 | 3-A·3-D |
| Cloud/On-Prem 복구 차이 | 복구 시 DB를 복원하고 로컬 Redis는 새 Runtime으로 시작. Cloud 연결·진행 상태의 무중단 승계를 보장하지 않음 | 02·3-D |
| 자원 초기 후보 | 승인된 RDS/Redis 크기를 출발점으로 하되 Pool·Replica·동시 연결·Peak를 측정해 적합성을 판단 | §3-D.10 |
| 관리 인증과 App 인증 | 팀원 IAM/ROSA IDP/RBAC는 플랫폼 작업 권한. 게임 이용자 로그인과 별도 | 3-C |

공개 게임 Route 승인은 관리 UI의 공개 접근 권한이나 DB/Redis 공개 접속 승인이 아니다. DB/Redis는 승인된 사설 Source·SG·TLS·인증 경계를 유지한다. ECR CI 계정과 Image Pull 권한의 구현은 기존 3-C/3-F 인계사항이며 이 문서에서 새 계정을 추가하지 않는다.

### 3-E.3. 3-E-1 네 가지 승인된 작업 전제

**기록 ID:** PH2-3E-ENTRY-TLS-CONFIG-LIFECYCLE  
**승인일:** 2026-10-01 KST — 최신 사용자 동의  
**상태:** 후속 설계를 위한 작업 전제 승인 / 실제 구현·검증 및 03 전체 검토 전

| 번호 | 제안 | 선택 이유 / 적용 전 조건 |
|---|---|---|
| 1 | FE·HTTP API·WSS를 하나의 공개 Host에서 Path로 분기하고 FE/BE Service는 ClusterIP로 연결 | 브라우저 연결 기준을 통일. 같은 App Namespace에 Route/Service를 두며 실제 경로·SPA 동작·Route Admitted 확인 후 적용 |
| 2 | 초기 Cloud 진입은 기본 Ingress 도메인·인증서와 Edge TLS, HTTP→HTTPS Redirect | 별도 도메인·인증서 운영 부담을 줄임. Router→App은 HTTP인 경계를 명시하고 내부 암호화 요구가 있으면 Re-encrypt와 비교 |
| 3 | App Image와 환경별 연결 설정을 분리하고 비밀값은 기존 Secret 공급 절차로 연결 | Clean Recreate와 로컬 복구의 Endpoint 차이를 관리. FE 공개 설정과 BE 비밀값을 분리하고 실제 설정 주입 방식을 Source로 확인 |
| 4 | 시작·준비·생존 확인을 나누고 Pod 종료 시 신규 작업 제한·연결 정리·제한 시간 내 종료를 구현 | 외부 DB/Redis 장애를 Pod 재시작 반복으로 처리하지 않음. 기존 WSS는 새 Pod로 이동하지 않으므로 재접속·상태 확인을 3-E-2와 연결 |

이 네 가지는 승인된 프로젝트 작업 전제다. 당시 소단계 승인 자체는 최종 상세설계 확정이나 실제 구현·검증 완료를 뜻하지 않았다. 이후 전체03 최종 컨펌은 §3-I.12.4를 따르며 실제 결과는 별도 기록한다. 공식 제품 문서가 프로젝트 구성 전체를 정한 것으로 표현하지 않는다. Path·Port·Probe URI·Timeout·Replica·인증 방식·실제 환경변수 이름은 아직 고정하지 않는다.

### 3-E.4. 공개 Host와 Path 분기

#### 3-E.4.1 사용자 진입 대응표

아래 기호는 설계 입력의 이름이며 실제 주소·환경변수·Manifest 값이 아니다.

| 요청 | 브라우저 기준 | Cloud 연결 대상 | 실제 입력 / 확인 |
|---|---|---|---|
| FE 화면·정적 파일 | `https://<PUBLIC_HOST>` | FE Route → FE ClusterIP Service → FE Pod | App 기본 경로·정적 파일·SPA fallback |
| 업무 HTTP API | 같은 Host의 `<API_PATH_SET>` | BE Route → BE ClusterIP Service → BE Pod | 실제 API 경로들·Method·Body/응답·인증 |
| 게임 실시간 연결 | `wss://<PUBLIC_HOST><WS_PATH>` | BE Route → BE Service → WebSocket 처리 Pod | 실제 Handshake 경로·Upgrade·인증·메시지 처리 |
| DB / Redis | 브라우저 연결 대상 아님 | BE → 사설 RDS/Redis Endpoint | TLS·CA·인증·Client Pool·재접속 |

`<API_PATH_SET>`은 API가 하나의 Prefix 아래 있다는 가정이 아니다. 실제 Source에서 분산 경로가 확인되면 필요한 Route 수와 Path 충돌을 검토한다. `/api`, `/ws`, `/health` 등의 경로를 이번 문서만으로 실제 값이라고 확정하지 않는다.

#### 3-E.4.2 Path 처리 기준

프로젝트 제안은 FE/BE Route와 Service를 같은 App Namespace에 두고 공개 Host를 공유하는 것이다. OpenShift는 같은 Host의 Path별 Route를 지원하며 Passthrough TLS는 Path 분기와 함께 사용할 수 없다. 구현 시 실제 ROSA 버전과 관리 정책에 맞춰 각 Route의 Admitted 상태·Service Port 연결을 확인한다. [3-E-R1]

실제 경로를 우선 보존한다. Route의 Path 선택이 Prefix를 자동 제거하는 것으로 가정하지 않는다. App이 기대하는 원래 URI와 전달 URI를 대조하고 불필요한 Rewrite를 추가하지 않는다. FE의 SPA fallback이 미지정 API·실패한 WSS 요청을 HTML 200 응답으로 숨기지 않도록 정상·오류 경로를 시험한다.

브라우저는 FE와 API의 Scheme/Host/Port를 일치시키고 WSS URL은 같은 공개 Host에서 구성하는 방향이다. WebSocket의 Origin 검사는 별도로 필요하다. 같은 Host 선택이 App 인증·권한 검사·CSRF 검토를 대신하지 않으며 실제 Cookie/Token 사용에 따른 규약은 3-E-2에서 정한다. Origin만으로 사용자를 인증하지 않는다. [3-E-R4]

#### 3-E.4.3 대안과 변경 조건

| 대안 | 장점 | 추가 조건 / 이번 판단 |
|---|---|---|
| 같은 Host + Path별 Route — 제안 | 브라우저 접속 기준과 공개 주소 관리가 단순 | 실제 경로 충돌·App URI·FE fallback 확인 필요 |
| FE/BE 별도 Host | 서비스별 배포·경로 구분이 쉬움 | CORS·Cookie 범위·WS Origin·인증서 적용 범위 추가 검토. 실제 App 제약이 있으면 비교 |
| FE 서버가 API/WS Proxy까지 담당 | 단일 공개 Route로 연결 가능 | FE가 BE 트래픽·WSS 중계 책임을 가짐. 기존 FE 구현·부하를 확인하기 전 기본 구조로 추가하지 않음 |

App Source에서 같은 Host의 경로 구분이 불가능하거나 별도 Host가 필수이면 이유·영향을 확인하고 변경안을 제시한다. 지금은 실제 경로가 확인되지 않았다는 이유만으로 App API를 새로 설계하지 않는다.

### 3-E.5. TLS 적용 구간과 인증서

#### 3-E.5.1 승인된 초기 Cloud 기준

| 통신 구간 | 제안 | 책임·확인 조건 |
|---|---|---|
| 브라우저 → 기본 Ingress / Router | HTTPS·WSS, Router에서 TLS 종료 | 기본 인증서의 Host 일치·신뢰·유효 기간을 실제 접속으로 확인 |
| HTTP 공개 접속 | FE 진입은 HTTPS Redirect | API/WS 클라이언트는 처음부터 HTTPS/WSS 사용. Redirect로 비보안 POST나 WS 연결이 안전해진다고 판단하지 않음 |
| Router → FE/BE | HTTP — 초기 Edge 제안 | 내부 구간이 암호화되지 않음을 명시. Service/Pod 접근 제어는 3-B Network·3-F 정책에 연결 |
| BE → RDS / Redis | 기존 승인 TLS·서버 검증·목적별 인증 | Edge 선택으로 Data TLS를 완화하지 않음 |
| On-Prem 복구 사용자 진입 | 별도 환경 설정·접속 기준 | 기존 Gateway/TLS를 실제 확인. Cloud 기본 도메인·인증서를 그대로 승계한다고 가정하지 않음 |

Edge는 Router에서 TLS를 종료한다. 기본 Ingress 인증서를 사용하도록 구성할 수 있으며, 실제 Cloud Host가 해당 인증서 범위에 드는지 확인해야 한다. 프로젝트는 기본 도메인부터 사용하고 별도 개인 도메인을 신규 의존성으로 만들지 않는 방향을 제안한다. [3-E-R1]

HTTPS 요청이 내부 HTTP로 전달될 때 App의 공개 URL 생성·Secure Cookie·Redirect 판단을 확인한다. 전달된 Scheme/Host 정보를 사용하는 방식과 신뢰할 Proxy 범위는 실제 Framework 설정에 맞춘다. 임의 Client가 보낸 Proxy Header를 무조건 신뢰하도록 설정하지 않는다. Cookie/Token의 최종 속성은 3-E-2에서 Source와 함께 결정한다.

#### 3-E.5.2 TLS 대안

| 방식 | Router→App | 적용 판단 |
|---|---|---|
| Edge — 초기 제안 | HTTP | 초기 연결 구성이 단순. 내부 평문 구간을 허용하는 프로젝트 전제에 대한 검토 필요 |
| Re-encrypt | TLS | 내부 암호화가 필요하면 BE/FE 서버 인증서·CA 신뢰·갱신·배포와 비용/작업량을 함께 설계 |
| Passthrough | App에서 TLS 종료 | 이번 Host/Path 분기안과 맞지 않음. 채택 시 Host 분리 등 연결 모델 재검토 필요 |

실제 요구사항이 Router→App 암호화를 요구하면 Edge 제안을 그대로 적용하지 않는다. 인증서 검증을 끄는 방식을 정상 운영 기준으로 쓰지 않는다. 이번 문서는 Route 생성 YAML이나 개인 인증서 Key를 생성·등록한 기록이 아니다.

### 3-E.6. 환경별 연결 설정과 비밀값

#### 3-E.6.1 설정 항목의 의미와 소유권

| 의미별 항목 | 공개 범위 / 공급 | 기록할 내용 | 실제 확인 |
|---|---|---|---|
| 공개 FE Host·API/WS 경로 | FE가 알아도 되는 설정 | 환경별 공개 접속 기준의 정의·개정 | 상대 경로 사용 가능 여부·브라우저 URL 구성 |
| App 허용 Origin·공개 URL·로그인 Redirect | BE 비밀값과 구분한 환경 설정 | 허용 목록·변경 절차·검증 항목 | 실제 인증 Framework·Callback 필요 여부 |
| DB/Redis Endpoint·DB 이름·TLS/CA·Pool | BE 전용 환경 설정 | 항목 의미·담당·개정 및 보호된 실행 설정의 참조 | 실제 Driver 옵션·CA 공급·타임아웃 |
| DB/Redis Credential·Signing/해독 Key | 3-C Secret 공급, BE 전용 | 값이 아닌 용도·Secret 참조·개정·공급 주체 | 실제 App 사용 여부·필수 Key·복구 호환성 |
| Route/Service/Deployment 설정 | GitOps 소유 경계 | 환경별 배포 구조·Port 참조·Image Digest·설정 개정 | 3-F 렌더링·적용·Secret 별도 공급과 충돌 확인 |

비밀값이 아닌 항목이라도 실제 민감 접속정보는 공개 작업 문서·Evidence에 평문으로 옮기지 않는다. 이 표의 항목 이름은 의미 설명이며 실제 App 환경변수 키를 만든 것이 아니다. Secret 값은 Image·FE Bundle·로그·Terraform 출력·Git 평문에 포함하지 않는다.

#### 3-E.6.2 Image와 설정의 연결

같은 검증 Image를 Cloud와 로컬 복구에서 사용하는 방향을 유지하고 연결 대상·TLS·인증정보는 환경별 공급한다. FE는 가능한 범위에서 상대 API 경로와 현재 Host를 사용한다. 절대 공개 URL 설정이 필요하면 별도 공개 Runtime 설정으로 공급하는 방식을 우선 검토한다.

FE가 빌드 시 환경값을 Bundle에 고정하는 현재 구조라면 Runtime 설정으로 바꾸는 실제 작업과 검증이 필요하다. 변경 전에는 동일 Image만으로 환경을 바꿀 수 있다고 기록하지 않는다. 환경별 Image가 불가피하면 Release 조합의 차이를 명시하고 복구 Image를 장애 전에 Harbor에 보존한다. BE 비밀값을 FE Runtime 설정으로 우회 공급하지 않는다.

#### 3-E.6.3 ROSA Clean Recreate / 로컬 복구 연결

ROSA 재생성으로 기본 Ingress Host가 달라질 수 있다. 새 Route가 Admitted된 실제 Host를 확인하고 FE 공개 URL, BE 허용 Origin, 필요한 로그인 Redirect 설정을 함께 반영한다. 설정 반영·Secret 공급·배포·브라우저 로그인/HTTP/WSS 검증을 연결한 후 사용자 접속 주소를 안내한다. 담당·자동화 구현·보호된 출력 저장 위치는 3-F에서 정한다.

Clean Recreate를 기본 도메인 영구 유지로 설명하지 않는다. 고정 공개 도메인이 필요해지면 DNS·인증서·갱신·소유자·비용을 별도 결정한다. 실제 주소를 확인하지 않은 상태에서 GitOps Manifest의 Host 값을 임의 확정하지 않는다.

On-Prem 복구는 사전 확보한 Image·설정·Secret·Backup으로 시작한다. Cloud DB/Redis Endpoint가 남아 있지 않도록 로컬 대상·TLS·Credential·공개 진입 설정을 대조한다. 복구 때 AWS에서 설정이나 인증서를 새로 내려받는 것을 필수 경로로 두지 않는다. Backup 해독 Key와 App Signing/해독 Key는 용도와 필요한 개정을 따로 확인한다.

### 3-E.7. Pod 시작·준비·생존 확인과 종료

#### 3-E.7.1 상태 확인의 책임

| 확인 | 프로젝트 제안 | 피할 동작 / 실제 입력 |
|---|---|---|
| Startup — 시작 확인 | App 초기화·Listen 가능 상태를 제한 시간 내 확인 | Source·기동 시간 확인 전 URI/시간 미고정. 매번 Schema 변경을 수행하는 Probe 금지 |
| Readiness — 요청 처리 준비 | BE가 필수 업무를 처리할 수 있는 상태인지 판단 | 필수 DB/Redis 사용 불가 시 새 업무 요청을 제한. 짧은 장애에 과민하게 전체 Pod가 빠지지 않도록 시간·오류 기준 검증 |
| Liveness — Process 생존 | App Process가 응답 불능 등으로 회복이 필요한지 확인 | 외부 DB/Redis 접속 실패를 곧바로 재시작 이유로 삼지 않음 |
| FE 준비·생존 | FE 정적 응답과 자체 구동 상태 | BE/DB 장애만으로 정상 FE를 재시작하지 않음. 화면은 오류·재접속 상태 안내 |

Kubernetes의 Readiness 실패와 Liveness 실패는 서로 다른 동작을 만든다. 이 프로젝트는 외부 의존성 장애를 준비 상태와 업무 오류 처리로 다루고 생존 확인과 분리하는 방향을 제안한다. Startup·Readiness·Liveness 각각의 조건·시간·실패 수치는 App의 실제 구동 방식과 측정 결과로 정한다. [3-E-R2]

DB/Redis 확인은 읽기 전용·짧은 제한 시간·필요한 수준으로 수행한다. 모든 Probe 호출마다 무거운 Query·새 Connection 폭증을 만들지 않으며, 실제 Framework가 지원하면 주기적 확인 결과를 활용한다. Redis의 TLS/AUTH 연결 성공만으로 `noeviction` 상태에서 업무 쓰기가 가능한지 보장하지 않으므로 메모리 압박·쓰기 오류는 별도 App 규약·관측 대상이다.

Probe가 게임 생성·Vote/Move·Schema 변경·Key 삭제 등 업무 상태를 바꾸면 안 된다. Probe 경로를 별도 공개 Route로 만들지 않으며, BE Route와 겹쳐 외부에서 닿을 수 있는 경우 민감 응답·진단 상세를 제한한다. 실제 상태 URI·Port와 응답 내용은 Source 확인 후 지정한다.

#### 3-E.7.2 Pod 종료 시 연결 처리

목표 동작은 종료 신호를 받은 Pod가 신규 업무·새 WSS를 제한하고, 처리 중 요청을 정해진 시간 내 마무리하거나 결과 확인이 필요한 상태로 남긴 뒤 연결·Pool을 정리하는 것이다. 실제 Framework의 종료 처리·Signal 전달·컨테이너 Entrypoint를 확인한다. 종료 시간은 측정 후 Deployment 설정과 연결한다.

Readiness 변경·트래픽 경로 반영·App 종료는 전파 시간이 있으므로 한순간에 완료된다고 가정하지 않는다. 기존 WSS 연결은 다른 Pod로 자동 이전되지 않는다. 앱 종료 처리와 플랫폼 종료 유예 시간을 함께 확인하고, 유예 시간을 넘는 종료와 강제 종료도 별도 시험한다. [3-E-R3]

`preStop`을 사용하면 종료 유예 시간 안에서 실제 필요한 정리 동작을 수행하는지 확인한다. 고정 Sleep만 추가해 업무 정리가 완료되었다고 판단하지 않는다. 신규 연결 거부, 진행 요청 결과, WSS 종료, Client 재접속·현재 상태 조회를 3-E-2 규약과 함께 검증한다.

Route의 Cookie 기반 연결 유지가 다른 Pod에서도 Session/Game 처리를 보장하는 것으로 설명하지 않는다. Replica 수를 늘리기 전 Redis 상태 공유·Pub/Sub·Pod 메모리 의존·Connection Generation 처리 등을 Source로 확인한다. FE/BE Replica·PDB·배치·자원 제한의 실제 값은 3-F/3-G에서 연결하며 이번 승인에 임의 수치를 포함하지 않는다.

#### 3-E.7.3 WSS 시간·재접속 연결

HTTP 요청 시간과 WSS 연결 유지 시간을 구분한다. 실제 ROSA Route, AWS Ingress LB, App, Client의 관련 Timeout·연결 유지 동작을 대조하고 App의 Heartbeat 지원 여부를 확인한다. Route별 Timeout 설정 기능은 공식 문서와 실제 ROSA 버전에 맞춰 적용한다. [3-E-R1]

Heartbeat 간격·유휴 허용 시간·재접속 대기·전체 제한 시간을 현재 임의 수치로 고정하지 않는다. 정상 게임 대기, 장시간 유휴, Client 통신 단절, Pod 삭제, Router/LB 연결 종료를 구분해 측정한다. Ping/재접속 성공은 진행 게임 상태 복구나 쓰기 결과 확정을 뜻하지 않는다.

### 3-E.8. 구현 전 확인과 검증 기준

#### 3-E.8.1 Source 확인 입력

| 입력 | 후속 판단 |
|---|---|
| FE/BE Framework·실제 구동 명령·Listen Port·경로 목록 | Route/Service/Probe 연결과 종료 신호 전달 |
| SPA 기본 경로·환경값 Build/Runtime 공급 방식 | 같은 Host/Path 충돌·환경 변경 시 Image 재사용 |
| 로그인·Cookie/Token·Signing Key·Origin 처리 | 3-E-2 인증·권한·재로그인·만료·복구 호환성 |
| WS Handshake·게임 메시지·Heartbeat·서버 연결 상태 | 재접속·구독 복원·중복 방지·Pod 간 동작 |
| DB/Redis Client·Pool·TLS/CA·오류·재시도 코드 | 3-D 용량·Failover·메모리 압박과 App 처리 |
| 기존 Health/Shutdown 지원·최장 요청·동시 연결 | Probe·종료 유예 시간·부하/장애 시험 |

전체 Source 계약 조사는 확인 전이다. 이후 지정 Commit의 연결 코드·CI·Job과 팀원 사전시험을 일부 대조한 범위는 §3-I.13에 기록한다. 현재 문서의 표·경로 기호를 전체 API 명세나 실행 YAML로 그대로 적용하지 않는다.

#### 3-E.8.2 시험 대응표 — 현재 모두 미실행

| ID | 상황 | 합격 판단에 필요한 결과 | 연결 단계 |
|---|---|---|---|
| IF-01 | 같은 Host의 FE·API·WSS 정상 접속 | TLS 신뢰·정확한 Service/Path·WS Upgrade·핵심 화면/업무 성공 | 3-F 적용·3-G |
| IF-02 | 없는 API/WS 경로·FE 새로고침 | 잘못된 API가 HTML 200으로 숨지 않음. 정상 SPA 경로 유지 | 3-E 실제 경로·3-G |
| IF-03 | HTTP·Origin·Proxy Header·인증 오류 | HTTPS/WSS 사용·허용 Origin/신뢰 Proxy·업무 인증 검증. Secret 노출 없음 | 3-E-2·3-G |
| IF-04 | RDS/Redis 통신 단절·Failover | Liveness 재시작 폭증 방지·준비 상태/업무 오류·연결 회복·결과 불명확 쓰기 처리 | 3-D·3-E-2·3-G |
| IF-05 | Redis 메모리 압박·쓰기 거부 | 처리 불가 안내·쓰기 오류 관측·부분 업무 상태 정합성 | 3-D·3-E-2·3-G |
| IF-06 | Rolling Update·Pod 삭제·강제 종료 | 신규 업무 제한·진행 요청 결과·WSS 재접속·상태 확인·중복 실행 여부 | 3-E-2·3-F·3-G |
| IF-07 | WSS 유휴·긴 게임 대기·Client 단절 | Timeout/Heartbeat 측정·종료 원인·복구 가능한 상태와 중단 상태 구분 | 3-E-2·3-G |
| IF-08 | ROSA Clean Recreate / 로컬 복구 | 환경 설정·Secret 개정·Route/TLS·로그인/HTTP/WSS 검증, 로컬은 AWS 신규 조회 없이 시작 | 3-C·3-D·3-F·3-G |

아직 목표 수치·성능·RTO/RPO를 측정하지 않았다. 접속 성공 한 번으로 게임 정합성·Multi-AZ·무중단·복구를 PASS 처리하지 않는다. 실제 동시 사용자·연결 수·Latency·실패 기준은 3-G와 Cost Gate에 맞춰 정한다.

### 3-E.9. 3-E-1 승인과 3-E-2 연결

3-E-1의 네 연결 경계를 작업 전제로 승인받았다. 이 승인을 기록하고 §3-E.10~15에서 다음 규약을 실제 Source 확인 항목과 함께 설계한다.

- 게임 이용자 인증·Session·만료·Key 개정·재로그인과 플랫폼 관리 인증의 분리.
- WebSocket 재접속·권한 재확인·구독 복원·현재 상태 조회·재시도 제한.
- Vote/Move 등의 결과 불명확 상황·중복 요청·DB/Redis 부분 실패 처리.
- Redis 새 Runtime 또는 일부 상태 소실 시 진행 게임의 중단·완료 기록·결과/Rating 보존.

상태명·DB 필드·요청 식별자·클라이언트 메시지 구조는 기존 Source를 확인하기 전 임의 확정하지 않는다. 신규 기능 변경이 필요하면 기존 구현에서 충족하는 부분과 추가 작업을 구분한다.

3-F에는 Route/Service/Deployment 소유권·환경별 설정 공급·Secret 공급과 충돌 방지·ROSA 재생성 시 Host 반영·Probe/종료 설정을 인계한다. 3-G에는 §3-E.8 시험과 3-D Data 검증을 연결하고, 3-H에는 실제 추가 작업·담당·시간·가동 비용을 인계한다. 새로운 설계 전제는 사용자 검토 후 진행하고 이미 승인된 입력은 재승인받지 않는다.

### 3-E.10. 3-E-2 인증·재접속·업무 상태 승인된 작업 전제

**기록 ID:** PH2-3E-AUTH-RECONNECT-COMMAND-CONSISTENCY  
**승인일:** 2026-10-01 KST — 최신 사용자 동의  
**상태:** 후속 설계를 위한 작업 전제 승인 / 실제 구현·검증 및 03 전체 검토 전

| 번호 | 승인된 작업 전제 | 기존 승인에서 받은 입력 / 이번에 승인된 경계 |
|---|---|---|
| 1 | HTTP와 WSS에서 같은 사용자 식별·권한·Session 유효성 기준을 적용하고 만료·로그아웃·권한 변경을 연결에 반영 | 플랫폼 관리 인증과 App 인증 분리는 기존 승인. 새 제안은 장시간 연결에도 유효성·Room/Game별 업무 권한 검사를 유지하는 것 |
| 2 | WSS 재접속은 재인증·참여 권한 확인·현재 상태 조회 후 재개하고 이전 연결의 메시지·종료 처리가 새 연결을 덮지 않도록 제한 | 연결 재생성과 업무 재실행의 구분은 기존 승인. 새 제안은 상태 동기화·연결 식별·오래된 연결 차단 기준 |
| 3 | Vote/Move·게임 확정 등 쓰기는 요청 식별·현재 Turn/상태 검사·업무별 원자적 중복 방지로 처리하고 결과가 불명확하면 확인 후 재시도 | 무조건 재실행 금지는 기존 승인. 새 제안은 같은 요청의 같은 결과, 변경 요청 구분, 영속 업무 기록의 DB 제약/Transaction 연결 |
| 4 | DB/Redis/통지의 부분 실패는 업무 확정 여부와 Runtime 정합성을 따로 판단하고 확인되지 않은 게임의 새 쓰기를 제한 | 전체 Runtime 소실 시 중단 처리·완료 기록 보존은 3-D-3 승인. 새 제안은 부분 실패의 대상 범위·성공 응답·재개 조건 |

네 항목은 승인된 서로 다른 판단 경계다. 설계 작업 전제 승인과 실제 구현·검증을 구분하며 03 전체 검토 전에는 최종 문서로 확정하지 않는다. 실제 Cookie/JWT·API·Message·Schema·Redis Key 구조를 확인하지 않은 상태에서 새 제품이나 별도 인증 서버·Event Broker를 추가하지 않는다. 기존 구현에서 충족하는 부분을 먼저 확인하고 필요한 변경만 2차 App에 반영한다.

### 3-E.11. 사용자 인증·권한과 Session 수명

#### 3-E.11.1 기존 인증 방식과의 연결

현재 확인된 문서의 책임은 Member 등 영속 기록은 DB, Session/Room/Ready/Connection Generation 등 Runtime은 Redis다. 실제 인증이 Cookie Session·JWT 등 어떤 형식인지, 로그인/Guest 발급·만료·동시 접속·Signing Key가 어떻게 구현되었는지는 아직 Source 확인 전이다.

이번 제안은 기존 검증된 인증 계약을 우선 유지하면서 HTTP와 WSS의 사용자 식별 기준을 통일하는 것이다. 새로운 인증 방식을 Source 확인 없이 정하지 않는다. Cookie 방식이면 Secure/HttpOnly/SameSite·CSRF·Domain/Path를, Token 방식이면 전달·보관·서명·만료·무효화·허용 대상 검증을 실제 구현에 맞춰 대조한다. 인증 형식에 따라 필요 없는 Key나 갱신 기능을 기본 범위에 추가하지 않는다.

브라우저 WSS 연결의 허용 Origin과 로그인 검증을 분리한다. 연결 직후 인증하는 기존 방식이라면 인증 완료 전 업무 메시지를 처리하지 않고 미인증 연결의 수명·한도를 제한한다. Cookie 자동 전송이나 Origin 일치만으로 업무 권한을 부여하지 않는다. OWASP도 WebSocket 연결과 개별 메시지의 권한 검사를 구분한다. [3-E-R5]

#### 3-E.11.2 요청과 연결의 권한 기준

| 대상 | 서버가 확인할 기준 — 제안 | Source에서 확인할 내용 |
|---|---|---|
| 사용자 / Guest | 서버가 검증·발급한 신원과 유효한 인증 상태 | Member/Guest 기능 범위·식별·만료. Client가 보낸 사용자 ID만 신뢰하지 않음 |
| Room 입장·관전·구독 | 해당 대상에 대한 접근·참여 권한과 현재 Room 상태 | 비공개 입장·퇴장·강퇴·정원·관전 규칙 |
| Ready·팀 변경·Vote | 현재 참여자·팀·Ready/Turn/게임 상태의 허용 조건 | 실제 기능 제한·투표 변경 가능 여부·권한 변경 반영 |
| 착수·Turn 종료·결과 확정 | 서버의 판정·동시성 제어·현재 버전 | Client가 최종 좌표·승패·Rating을 임의 확정하는 경로 차단 |
| 종료된/오래된 연결 | 유효한 Session과 현재 연결 식별을 다시 확인 | 이전 연결의 늦은 명령·퇴장 처리로 새 연결 상태를 변경하지 않음 |

이 표는 기능 허용 범위를 새로 만드는 명세가 아니라 검증할 경계다. Guest의 투표·채팅·관전 가능 여부와 동시 접속 정책은 기존 Domain Contract를 확인한 뒤 기록한다. 추가자료나 기억상의 UI 계획을 현재 Code의 실제 권한으로 취급하지 않는다.

#### 3-E.11.3 만료·로그아웃·Key 교체와 복구

권한이 필요한 업무 명령을 처리할 때 Session·대상 권한·현재 상태를 확인하는 방향을 제안한다. 연결 유지 중 만료·로그아웃·강퇴 등이 발생하면 새 명령·구독을 제한하고 해당 연결을 종료하거나 재인증을 요구한다. Pod가 여러 개일 때 무효화 전파와 연결 종료가 가능한지, 반영 시간과 실패 시 동작을 시험한다. 숫자는 실제 구현·측정 후 정한다.

만료 또는 필수 Session 유효성을 확인할 수 없는 경우 기존 연결만을 근거로 계속 쓰기를 허용하지 않는다. Redis 장애·상태 소실과 단순 Client 네트워크 단절을 구분한다. Session이 유효하고 Runtime이 정상인 단절은 재접속을 검토할 수 있지만, 소실된 Session·참여 권한을 Client 캐시에서 복원하지 않는다.

Signing/해독 Key는 실제 App에 필요할 때만 05 Secret 목록에 연결한다. Signing Key 교체 시 기존 Token 검증·무효화·재로그인 정책을 확인하고, 저장된 데이터의 해독 Key와 혼동하지 않는다. Cloud/로컬 복구는 기존 Session 연속성을 보장하지 않으며 새 인증 후 새 Runtime을 시작하는 기존 승인 방향을 유지한다. 실제 만료 시간·토큰 형식·저장 위치·Key 개정은 미확인이다.

### 3-E.12. WebSocket 재접속과 현재 상태 동기화

#### 3-E.12.1 재접속의 진행 기준

| 순서 | 제안 동작 | 진행 조건 / 실패 시 처리 |
|---|---|---|
| 1 | 단절을 인식하고 Client의 새 업무 쓰기를 보류 | 마지막 보드·Turn 화면은 오래된 상태임을 표시. 미확인 쓰기를 자동 재전송하지 않음 |
| 2 | 제한된 대기·재접속 시도 후 인증·Session 확인 | 무작위 지연을 포함해 동시 재접속 집중을 줄임. 만료/회수는 반복 연결 대신 재로그인 안내 |
| 3 | 현재 Room/Game 접근·참여와 새 연결 식별 확인 | Client 캐시의 Room/팀/Ready를 서버 상태로 취급하지 않음 |
| 4 | 현재 상태를 조회하고 구독·상태 버전을 맞춤 | Snapshot과 그 이후 이벤트 사이의 공백·역순·중복 처리 확인 |
| 5 | 최신 상태·권한·진행 가능 여부 확인 후 업무 입력 재개 | Session/Runtime 소실 또는 DB/Runtime 불일치는 §3-E.14 기준으로 재조회·중단 안내 |

재접속 대상은 보존된 서버 상태이며 놓친 모든 메시지의 재생을 기본 전제로 두지 않는다. Redis Pub/Sub를 실제 사용한다면 구독 단절 중 메시지는 다시 전달되지 않을 수 있다. 따라서 구독 재연결만으로 현재 화면·업무 상태를 복구했다고 판단하지 않는 방향을 제안한다. [3-E-R6]

#### 3-E.12.2 Snapshot과 이벤트 사이의 공백

현재 상태 조회 중에도 다른 참여자의 투표·Turn 진행이 발생할 수 있다. 구현은 기존 상태 버전/Sequence가 있는지 먼저 확인하고, 구독을 연결한 뒤 Snapshot 기준을 맞추거나 조회 전후 변경 여부를 검증하는 등 실제 지원 가능한 방법으로 공백을 처리한다. Snapshot 다음에 무조건 구독하면 정합성이 확보된다고 가정하지 않는다.

중복·역순·버전 공백을 검출했을 때 새 쓰기를 잠시 보류하고 권한이 있는 현재 상태를 다시 조회한다. 전체 서비스에 새 Streams/Broker를 넣어 이벤트 영구 재생을 보장하는 구조는 이번 기본 제안에 포함하지 않는다. 실제 Code에 버전·현재 상태 조회가 없으면 필요한 추가 작업을 3-F/3-G와 일정에 반영한다.

#### 3-E.12.3 이전 연결·새 연결의 충돌

Source에 명시된 Connection Generation의 실제 저장·갱신·비교를 조사한다. 제안 기준은 새 연결 식별 등록과 이전 식별 비교를 서버에서 일관되게 처리하고, 늦게 도착한 이전 연결의 메시지·Disconnect/Leave가 현재 연결·참여 상태를 지우지 못하도록 하는 것이다. 기존 세대 값이나 연결 ID를 재사용해 오래된 연결이 새 연결로 인정되는지 Redis Failover·Pod 교체에서도 확인한다.

하나의 사용자에게 여러 연결을 허용할지 또는 제한할지는 기존 Session Concurrency 규칙을 확인한다. 여기서 임의로 한 연결만 허용하도록 바꾸지 않는다. 허용된 각 연결의 소유권과 업무 쓰기 권한, 종료·정리 조건을 실제 구현에 연결한다.

Pod 여러 개에서의 재접속은 Session/Room 상태 공유뿐 아니라 구독 처리·Timer·Turn 확정 주체·Pod 메모리 상태를 확인해야 한다. Route의 연결 유지 Cookie나 공유 Redis 접속만으로 모든 Pod가 동일하게 처리한다고 판단하지 않는다.

#### 3-E.12.4 Heartbeat·종료·Client 안내

Heartbeat는 연결 응답 상태를 확인하는 용도이며 업무 처리 결과를 확인하는 응답과 구분한다. RFC의 Ping/Pong과 실제 App Heartbeat 지원을 대조한다. [3-E-R4] 간격·유휴 시간·재시도 횟수·종료 유예 시간은 Route/LB/App/Client 설정과 측정으로 정한다.

Client 화면은 연결 중·동기화 중·재로그인 필요·대상 게임 처리 보류/중단을 구분해 안내한다. 게임 처리 기준을 화면에 기술 용어로 노출하지 않고 사용자가 지금 입력 가능한지와 다음 행동을 알려준다. 실제 메시지 이름·Error Code·Close Code는 기존 계약을 확인해 연결한다.

### 3-E.13. 업무 쓰기의 중복·동시성·결과 확인

#### 3-E.13.1 요청 식별과 업무별 확정 기준

멱등 처리는 같은 업무 요청을 반복해도 결과가 중복 반영되지 않도록 하는 것이다. 요청의 신원·대상·현재 상태와 함께 식별자를 검사하는 방향을 제안한다. 식별자는 Credential이 아니며 Client가 동일 ID로 다른 내용을 보내면 새 명령으로 처리하지 않고 충돌을 확인한다.

아래 항목은 필요한 의미이며 실제 API 필드명·DB 컬럼·Redis Key를 확정한 것이 아니다.

| 의미 | 처리 기준 — 제안 | 실제 확인 |
|---|---|---|
| 요청 식별 | 같은 요청의 재시도에는 같은 ID·내용 사용 | 현재 ID 발급·응답/조회 연결·보관 기간·사용자/대상 범위 |
| 대상과 현재 상태 | Room/Game·Turn·허용 버전을 서버에서 검사 | 오래된 화면·Turn·권한으로 수행되는 쓰기 차단 |
| 동일 요청 / 다른 변경 | 중복 요청과 정상적인 투표 변경 등을 구분 | 기존 투표 변경 규칙·참여자별 처리·성능 |
| 확정 결과 | 완료·거부·처리 중·결과 확인 필요를 구분 | 실제 응답 의미·DB Commit/Redis 처리의 증거 |

#### 3-E.13.2 업무별 원자적 처리

| 업무 종류 | 책임과 제안 | 실제 구현 확인 |
|---|---|---|
| Room/Ready/Connection/Vote 등 Runtime 변경 | Redis의 관련 조건 검사와 상태 변경을 원자적으로 연결 | 실제 Transaction/Script 등 지원 방식·동시 요청·부분 변경·TTL·메모리 압박 처리 |
| 착수·게임 완료·Result/Rating 등 영속 확정 | DB Transaction과 업무별 고유성·현재 상태 조건으로 중복 확정을 차단 | 실제 Schema/제약·경합·재시도·Rollback·Result와 Rating의 일관성 |
| Redis 상태와 DB 업무 확정을 함께 쓰는 흐름 | 각 저장소의 확정 여부·진행 상태를 연결하고 부분 실패를 탐지 | 하나의 공통 Transaction으로 묶인 것으로 가정하지 않음. 보류·재조회·재개 규칙은 §3-E.14 |
| 사용자 알림·Pub/Sub·WSS 응답 | 확정 상태를 전달하고 누락은 현재 상태 조회로 확인 | 통지 성공/실패가 DB 확정 자체를 취소하거나 새 업무를 만들지 않음 |

Redis의 원자적 실행은 실패 시 모든 변경이 자동 Rollback된다는 의미로 확대하지 않는다. [3-E-R12] 사용하는 명령·Script의 오류·메모리 부족 시 일부 상태가 바뀔 수 있는지 시험한다. Redis의 일시적 잠금·중복 ID 보관만으로 DB의 착수·결과가 영구 중복 방지된다고 판단하지 않는다. Redis Failover로 해당 기록이 사라진 경우에도 DB 제약·상태 조건이 영속 업무의 중복 확정을 막는지 확인한다.

Game/Turn별 고유성·서버의 판정 주체·완료된 결과의 변경 금지는 의미상의 기준이다. 실제 Unique Key·Version Column·Locking 방식은 기존 구현을 조사해 선택한다. 필요한 Schema 변경이 발견되면 3-D의 Release/Backup 호환성과 Schema 적용·되돌림 절차에 연결한다.

#### 3-E.13.3 결과가 불명확한 경우

응답 유실·Timeout·연결 종료는 업무가 실행되지 않았다는 증거가 아니다. Client는 새 요청 ID로 같은 행동을 다시 만들어 보내지 않고 기존 요청·업무 대상을 기준으로 서버 결과를 확인하는 방향을 제안한다.

- 완료 결과를 확인하면 기존 결과를 반환하거나 현재 상태를 동기화한다.
- 실행되지 않은 상태를 확인하고 현재 권한·Turn도 유효하면 같은 요청의 제한된 재시도를 검토한다.
- 아직 처리 중이거나 확정 여부를 확인할 수 없으면 결과 확인 상태를 유지하고 새로운 중복 명령을 막는다.
- 상태가 이미 바뀌었으면 과거 Turn의 쓰기를 현재 Turn에 적용하지 않는다.

실제 결과 조회 수단이 없으면 새로운 URI를 문서만으로 만들지 않고 Source 변경 필요사항으로 남긴다. DB 연결 오류를 무조건 전체 Transaction 재실행으로 처리하지 않는다. Redis만의 완료 기록이 소실되었다면 결과를 영속적으로 증명할 수 없는 Runtime 업무도 있을 수 있으며, 이 한계를 무손실·정확히 한 번 처리 보장으로 설명하지 않는다.

### 3-E.14. DB/Redis 부분 실패와 서비스 재개

#### 3-E.14.1 업무 확정·Runtime·통지의 구분

영속 업무가 확정되었는지, Redis의 현재 게임 상태가 그 결과와 맞는지, Client가 알림을 받았는지는 서로 다른 결과다. 영속 쓰기 성공은 실제 DB Commit을 기준으로 확인하고, 단순 요청 수신·Redis 연결 성공·메시지 발행만으로 완료 응답을 보내지 않는 방향을 제안한다. Runtime만의 요청은 실제 Redis 처리 결과를 기준으로 응답하며 영속 보존을 보장한 것으로 표현하지 않는다.

| 상황 | 처리 기준 — 제안 | 재개 / 확인 |
|---|---|---|
| DB 업무 확정 전 실패 | 완료를 선언하지 않음. DB Transaction 결과·남은 Runtime 변경 확인 | 현재 상태와 동일 요청 처리 여부 확인 후 제한된 재시도 |
| DB Commit 여부 불명확 | 새 ID로 재실행하지 않고 영속 기록·업무 고유성으로 확인 | 확인 전에는 결과 확인 상태로 유지 |
| DB 확정 완료, Redis 갱신 실패 | DB 결과를 보존하고 해당 Game의 추가 진행을 제한 | DB/Runtime 대조 후 검증 가능한 상태 재구성 또는 중단 처리. 이미 확정한 결과를 임의 취소하지 않음 |
| DB·Runtime 정상, Pub/Sub/WSS 통지만 실패 | 업무를 새로 수행하지 않고 Client가 현재 상태를 조회 | 통지 누락·Client 동기화 결과 기록 |
| Redis 일부 Key/Session·Turn 손실 | 영향 대상을 식별하고 유효성·정합성을 확인 | 안전하게 확인 가능한 대상만 재개. 권한·진행 기준이 불명확한 대상은 보류/중단 |
| Redis 메모리 압박·쓰기 거부 | 요청 실패·부분 변경을 확인하고 관련 상태 쓰기를 제한 | 용량/오류 원인 해결과 실제 상태 대조 후 재개 |
| Redis 전체 소실·로컬 새 Runtime | 3-D-3 승인 기준 적용 | 완료 DB 기록 보존, 진행 상태 명시적 중단 처리, 재로그인·새 게임 검증 |

여기서 대상별 제한은 구현 가능한 정합성 확인이 있을 때의 목표다. 공통 Session/Coordination 장애로 전체 업무가 안전하지 않으면 BE 준비 상태·신규 진입을 서비스 단위로 제한할 수 있다. 반대로 하나의 게임 오류를 이유로 정상 완료 기록을 지우거나 모든 게임을 무조건 중단 처리하지 않는다.

#### 3-E.14.2 Redis Failover와 새 Runtime의 차이

ElastiCache Valkey는 비동기 복제로 일부 최신 상태를 잃을 수 있다. [3-E-R7] Failover 후 연결이 복구되었더라도 Session·Room·Turn·Vote·연결 식별이 서로 맞는지 확인한다. Client 캐시나 늦게 도착한 이벤트를 근거로 삭제된 Runtime을 무조건 생성하지 않는다.

일부 Redis 상태가 남은 Failover, Pod 교체, Redis 전체 재생성, On-Prem 논리 복원은 다른 시험이다. Pod 교체에서 현재 상태가 정상인 게임은 재접속 기준을 검증한다. 일부 소실 상태는 DB/Runtime과 실제 Code의 재구성 가능성을 확인한다. 전체 Runtime 소실에서 진행 게임을 중단하는 방향은 이미 승인받았으므로 같은 선택을 재승인 대상에 추가하지 않는다.

완료 Game/Move/Result/Rating은 DB 기록을 보존한다. 진행 중 상태 정리는 실제 상태 필드·권한·대상 판정·반복 실행 시 영향을 확인한 뒤 수행하고, 임의 승패·정상 완료·Rating을 만들지 않는다. Cloud/로컬 복구의 SQL 사용자·Credential·Signing/해독 Key·Backup 호환성은 3-C·3-D 문서의 기존 기준을 유지한다.

#### 3-E.14.3 재개 Gate

서비스 또는 대상 게임의 쓰기를 다시 허용하려면 유효한 사용자/Session·참여 권한, 해당 대상의 현재 상태, 영속 확정과 Runtime의 관계, 결과가 불명확한 요청의 처리 기준이 확인되어야 한다. DB/Redis 접속 한 번 성공·Probe 정상만으로 통과하지 않는다.

실제 자동 정합성 복구가 없으면 보류·유지보수·명시적 중단 절차로 대응하고 수행 수준을 기록한다. 분산 Transaction·자동 보상·Outbox/Broker를 이미 구현한 것으로 설명하거나 기본 범위에 자동 추가하지 않는다. 현재 구조로 필수 검증을 충족하지 못하면 대안의 범위·작업량·비용·재시험을 제시한다.

### 3-E.15. 실제 확인 입력·시험·후속 인계

#### 3-E.15.1 Source 확인과 구현 변경의 구분

| 확인할 입력 | 검토 결과를 기록할 내용 | 연결 단계 |
|---|---|---|
| 로그인·Guest·Cookie/Token·Session·만료·로그아웃 | 실제 방식·권한·Key·변경 전후 동작. 기존 구현 재사용/수정/추가 구분 | 05 Secret·3-F App |
| WS 인증·구독·현재 상태 조회·Connection Generation·동시 접속 | 이전 연결 차단·Snapshot/Event 공백·다른 Pod 재접속 | 3-F 배포·3-G |
| Room/Game/Turn/Vote·DB 착수/결과 코드 | 서버 판정·DB Transaction/고유성·Redis 원자성·재시도 | 06 Schema/용량·3-G |
| 부분 실패·noeviction·Failover·새 Runtime 처리 | 안전한 재개/중단 범위·실제 제어 수단·오류 응답 | 3-D Data·3-F·3-G |
| 실제 FE/BE Replica·Process·Pool·동시 연결 | 총 DB 연결·Redis 메모리/Client·종료·타임아웃의 초기 설정과 측정 | 06 크기·3-F·3-G·3-H |

현재 확인한 것은 승인된 문서와 공식 기능 제약이다. 실제 Application 저장소·Runtime·DB를 새로 조사하지 않았다. 로그인 방식·멱등 구현·상태 조회·DB 제약이 이미 존재한다고 가정하지 않는다. 새 의존성을 만들지 않는 계약 기준을 먼저 제안하고 실제 Source를 구현 전 조사한다.

#### 3-E.15.2 추가 시험 대응표 — 현재 모두 미실행

| ID | 상황 | 합격 판단에 필요한 결과 |
|---|---|---|
| IF-09 | 미인증·잘못된 Origin·타인의 Room/Game 요청 | 연결/업무 권한 거부, 실제 허용 범위만 조회·구독·쓰기 |
| IF-10 | Session 만료·로그아웃·강퇴·권한 변경 | 기존 WSS의 새 업무/구독 제한·반영 시간·다른 Pod 처리 |
| IF-11 | 단절 중 이벤트 발생·Snapshot 중 Turn 변경 | 현재 상태 동기화·공백/역순 검출·업무 재개 조건 |
| IF-12 | 새 연결 뒤 이전 연결의 Message/Disconnect/Leave 도착 | 새 연결·참여 상태 보존, 오래된 명령 차단 |
| IF-13 | 동일 ID 재전송·다른 내용·다중 Pod 동시 Turn/결과 확정 | 업무별 중복 차단·정상 변경 구분·DB/Redis 최종 상태 |
| IF-14 | DB Commit 후 응답 유실·Commit 불명확 | 결과 확인·동일 요청 재시도·중복 Move/Result/Rating 없음 |
| IF-15 | DB 확정 뒤 Redis 실패·통지 실패 | DB 결과 보존·관련 진행 제한·조회/정합성 확인·통지 누락 구분 |
| IF-16 | Redis Failover·부분 Key 손실·전체 재생성 | 상태별 영향·접속 복구와 업무 재개 구분·새 Runtime 중단/재로그인 |
| IF-17 | Redis 메모리 압박·쓰기 중간 실패 | 불완전 Runtime 탐지·완료 오표시 방지·재개 조건 |
| IF-18 | 로컬 DB 복원·새 Redis·사전 보존 Image/Secret | 완료 기록 보존·진행 상태 처리·신규 로그인/게임, AWS 신규 조회 비의존 |

§3-E.8의 IF-01~08과 함께 기록하며 모든 시험을 같은 PASS로 합치지 않는다. 실제 경합·실패 주입은 격리된 2차 시험 환경에서 수행하고 현재 1차 게임·DB에 적용하지 않는다. 실제 오류코드·응답·확정/중단 기록·허용 대기 시간은 Source·측정·3-G 기준과 연결한다.

#### 3-E.15.3 승인 기록과 후속 진행

3-E-2 동의에 따라 승인 기록을 반영하고 §3-E.17에 3-E 설계의 전체 범위·미확인 값·구현 입력·검증 기준을 정리해 3-F로 인계했다. 같은 기본 선택을 다시 승인받는 소단계를 만들지 않는다. 실제 Source 확인에서 새 기술·권한·Schema·기능 변경이 필요한 경우에만 이유·영향과 대안을 별도로 제안한다.

3-F는 실제 Route/Service/Deployment·Probe/종료·환경값/Secret 공급·App 변경 경계·Terraform/Provider/ROSA 버전·State/실행 경계를 연결한다. 3-G는 §3-E.8·§3-E.15의 정상/오류/장애·복구·동시성 시험을 수치와 Evidence로 정의한다. 3-H는 실제 확인·수정·예행시험·재시험의 담당·시간·비용을 계획한다. 03 전체 검토·최종 컨펌은 완료했으며 실환경 확인에 따른 변경은 근거와 영향으로 개정한다.

### 3-E.16. 팀원 Terraform 자료의 참고 분류와 3-F 인계

#### 3-E.16.1 접수 범위

**자료:** `terraform-version-guide.md` — 팀원 작성 자료, 2026-10-01 접수.  
**분류:** TEAM DRAFT + PENDING DECISION. 공용 서버 설치값은 팀원 제공 현황이며 직접 확인한 OBSERVED EVIDENCE로 분류하지 않는다. 운영안이 프로젝트 공식 조건으로 지시되거나 실행 증거가 확보되면 해당 부분만 다시 분류한다.

자료 원본은 변경하지 않는다. Project Source를 자료 전체로 덮어쓰지 않고 현재 판단에 필요한 버전·고정 방법·작업 환경·실행 권한·협업 조건만 3-F의 참고 입력으로 추출한다. 이번 3-E-1 승인에는 Terraform 버전·팀원 운영안의 채택이 포함되지 않는다.

| 제공 내용 | 이번 기록 상태 | 3-F에 인계할 판단 |
|---|---|---|
| Terraform 1.16.4 공용 설치·versionlock | 팀원 보고 설치값 / 후보 | 공식 배포 존재는 확인 [3-E-R8]. 실제 Controller·담당자·자동화 실행 환경의 버전/경로/배포 방식 확인 후 선택 |
| AWS CLI 2.37.5·GitHub CLI/git/jq | 팀원 보고 도구 현황 | 실제 설치 결과·사용 작업·CLI/인증 옵션 호환성 확인. 제공 숫자를 실측으로 보고하지 않음 |
| `required_version >= 1.16.0` | 버전 하한 예시 | 동일 버전 고정이 아님 [3-E-R9]. 실행 환경 고정과 코드의 허용 범위를 함께 선택 |
| `.terraform.lock.hcl` 커밋·Provider 업그레이드 PR | 참고할 변경 통제안 / 상위 Source와 방향 일치 | Lock 파일은 Provider 선택을 기록하며 Terraform CLI·Remote Module 전체를 고정하지 않음 [3-E-R10]. Root Module별 Lock·검증 조합 선택 |
| OS 개인 계정·개인 Clone·Root 실행 금지 | 팀 운영 초안 | 파일 소유권·개인 작업 공간·AWS 인증 주체·승인된 TF 실행 Role을 구분 |
| S3 Remote Backend | 상위 Source와 방향 일치 / 실제 적용 미확인 | bootstrap/foundation/rosa State 경계·암호화·Versioning·잠금·접근·초기 이전 절차 |
| PAT·GitHub 웹 PR·승인 1명·main 보호 | 팀 협업 운영 초안 | 실제 Repo/Branch 보호·Git 인증 방식·담당. 명령 예시만으로 Repo 생성/정책 적용 완료로 처리하지 않음 |

#### 3-E.16.2 그대로 확정하지 않을 설명과 입력

1. **OS root와 AWS Root는 다르다.** OS root로 실행하면 AWS Root Key를 사용한다고 자동 결정되지 않는다. 실제 Credential 경로·환경변수·Profile·Role을 확인한다. 반대로 OS 개인 계정 전환만으로 승인된 TF Role이 사용되는 것도 아니다. 기존 개인 IAM User 4개+Admin 선택과 별도의 TF 실행 Role·State 경계는 유지한다.
2. **AWS CLI 영향을 모두 무시하지 않는다.** Terraform Provider가 자원을 다루는 경로와 CLI를 사용하는 Caller 확인·인증·Bootstrap·Data 작업을 구분한다. 자료의 `aws configure` 예시만으로 개인 Admin 인증을 일상 TF 실행 주체로 자동 채택하지 않는다. 환경변수·Profile·인증 우선순위·Role·장시간 실행 인증을 검증한다. [3-E-R11]
3. **State 호환성과 되돌림은 실제 조합을 확인한다.** 신버전으로 쓴 State를 구버전에서 무조건 읽을 수 있거나 모든 1.x 변경이 반드시 읽기 불가라고 단정하지 않는다. 버전 변경 전 State 사본·현재 Infra·Provider 호환성·Plan을 확인하고 과거 State 파일 복원만으로 Infra 변경을 되돌렸다고 판단하지 않는다.
4. **공용 설치와 Lock 파일의 범위를 구분한다.** 공유 Controller에만 고정되어 있어도 다른 CLI/자동화 환경은 달라질 수 있다. 실행 환경·Terraform CLI 허용 범위·Provider 선택·Module 버전·실제 ROSA 지원 조합을 함께 기록한다.

이번 인계는 버전 선택을 3-F에서 할 수 있도록 후보와 확인 기준을 보존한 것이다. 1.16.4의 채택·AWS CLI/Provider 버전 확정·공용 서버 접속·설치·설정 변경을 수행하지 않았다. 자료의 원격 작업 주소나 개인 Credential은 이 문서에 옮기지 않는다.

### 3-E.17. 3-E 설계 정리와 후속 인계

#### 3-E.17.1 전체 범위 대조

| 설계 범위 | 승인·상세 기록 | 남은 실제 입력 / 검증 | 후속 연결 |
|---|---|---|---|
| 사용자 Host·Path·Service 연결 | 3-E-1 / §3-E.3~4 | 실제 경로·Port·Namespace·SPA fallback·Route Admitted | 3-F 배포·3-G 접속 |
| TLS·인증서·Proxy 인식 | 3-E-1 / §3-E.5 | 실제 Host/인증서·Framework의 Proxy 신뢰·Secure Cookie/Redirect | 3-F 설정·3-G |
| 환경별 설정·Secret·재생성 Host | 3-E-1 / §3-E.6, 05 Secret | 실제 설정 키·FE Build/Runtime 주입·App Key·공급·개정·로컬 대상 | 3-F Bootstrap·Release |
| Startup/Readiness/Liveness·종료·Heartbeat | 3-E-1 / §3-E.7 | 실제 Probe·Framework 종료·시간·동시 연결·Route/LB/App의 제한 | 3-F 설정·3-G 측정 |
| 사용자 인증·Session·업무 권한 | 3-E-2 / §3-E.10~11 | 실제 Cookie/Token/Guest·만료·로그아웃·강퇴·다중 Pod 반영 | 3-F App 변경·3-G |
| WSS 재접속·현재 상태·이전 연결 | 3-E-2 / §3-E.12 | 실제 Snapshot·Sequence·Generation·구독·동시 접속 | 3-F App/배포·3-G |
| 업무 중복·영속 확정·부분 실패 | 3-E-2 / §3-E.13~14, 3-D Data | 실제 요청 식별·DB 제약/Transaction·Redis 명령·재개/중단 제어 | 06 Schema·3-F·3-G |
| 시험·수치·비용·실제 추가 작업 | §3-E.8·§3-E.15 | IF-01~18 실측·Pool/Replica·Peak·담당·작업량 | 3-G·3-H |

#### 3-E.17.2 인계 판정

**3-E의 설계 정리와 후속 인계를 완료한다. 실제 App 조사·구현·접속·장애 시험은 완료하지 않았다.** 승인된 계약 기준과 확인할 값을 분리했으므로 Terraform/GitOps의 구현 구조를 설계할 수 있다. 실제 App를 배포하기 전 Source 확인과 필수 설정·Schema·인증·오류 처리 대조를 수행한다.

3-F에서는 같은 Resource의 Owner를 하나로 두고 Namespace·Service·Route·Deployment·비밀값 공급·배포 개정을 연결한다. App 변경은 App 저장소, 배포 선언은 GitOps, 설치/공급 코드는 Infra, 실제 결과와 변경 이유는 Docs에 기록한다. Runtime 미확인 사항을 HCL/Manifest에 임의 숫자·경로로 채우지 않는다.

IF-01~18은 3-G의 시험 입력이며 현재 모두 미실행이다. 3-H는 실제 Source에서 필요한 추가 작업과 시험 시간·가동 비용을 계획한다. 팀원 Terraform 자료는 §3-E.16의 참고 상태로 3-F 절에 인계하며 이번 승인으로 버전이나 팀 운영 규칙을 자동 확정하지 않는다.

3-F-1의 State·제한 입력 전달·GitOps 최초 설치 책임은 사용자 작업 전제로 승인되었다(§3-F.2). 3-F·3-G·3-H의 B01~B07도 2026-10-01 작업 전제로 승인되었고, 관련 항목에 반영한 뒤 3-I 통합 검토 절에서 전체03을 다시 검토한다. 승인 상태를 구분하고, 03 전체 통합 검토에서 Network·Secret·Data·Interface·구현·시험·비용의 정합성을 다시 확인한다.

### 3-E.18. 참고 자료와 확인 범위

- **[3-E-R1]** [Red Hat OpenShift Route — Path·TLS·기본 인증서·Timeout·연결 유지](https://docs.redhat.com/en/documentation/openshift_container_platform/4.16/html/networking/configuring-routes)
- **[3-E-R2]** [Kubernetes Startup·Readiness·Liveness Probe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
- **[3-E-R3]** [Kubernetes Pod Lifecycle — 종료 처리](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)
- **[3-E-R4]** [RFC 6455 — WebSocket Handshake와 Origin](https://www.rfc-editor.org/rfc/rfc6455.html)

- **[3-E-R5]** [OWASP WebSocket 인증·Session·메시지 권한](https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html)
- **[3-E-R6]** [Redis Pub/Sub 전달 방식](https://redis.io/docs/latest/develop/pubsub/)
- **[3-E-R7]** [AWS ElastiCache Redis OSS 비동기 복제](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.Redis.Groups.html)
- **[3-E-R8]** [HashiCorp Terraform 1.16.4 공식 배포](https://releases.hashicorp.com/terraform/1.16.4/)
- **[3-E-R9]** [HashiCorp 버전 조건 문법](https://developer.hashicorp.com/terraform/language/expressions/version-constraints)
- **[3-E-R10]** [HashiCorp Dependency Lock File](https://developer.hashicorp.com/terraform/language/files/dependency-lock)
- **[3-E-R11]** [AWS CLI 인증·설정 우선순위](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html)
- **[3-E-R12]** [Redis Transaction의 오류·Rollback 경계](https://redis.io/docs/latest/develop/using-commands/transactions/)

2026-10-01 공식 기능 설명과 승인된 작업 문서를 대조했다. [3-E-R1]의 OpenShift 4.16은 Route 기능을 확인한 문서 버전이며 프로젝트 ROSA 버전을 4.16으로 선택한 기록이 아니다. 실제 설치 버전·지원 기능·ROSA 관리 정책을 3-F 구현 전 확인한다. Kubernetes 최신 문서의 신규 기능을 ROSA에서 지원한다고 가정하지 않는다.

사용자 접속 Host 통일·초기 Edge TLS·설정 분리·외부 장애와 Liveness 분리는 승인된 프로젝트 작업 전제다. 3-E-2의 인증·재접속·쓰기 중복·부분 실패 처리 기준도 승인된 프로젝트 작업 전제다. 팀원 Terraform 자료는 참고 후보와 확인사항만 추출했으며 프로젝트 버전으로 확정하지 않았다. 실제 App Source·Controller/AWS/ROSA 접속·배포·브라우저·부하·장애 시험은 수행하지 않았으며 지원 가능성과 구현·검증 완료를 구분한다.

### 3-E 남은 입력과 실행

- [x] 3-E-1 네 가지 작업 전제 승인 — 2026-10-01 사용자 동의
- [ ] 실제 Source의 경로·인증·환경값·Health/Shutdown·DB/Redis Client 확인
- [x] 3-E-2 인증·Session·WebSocket·중복/부분 실패·진행 상태 처리 초안 작성
- [x] 3-E-2 네 가지 작업 전제 승인 — 2026-10-01 사용자 동의
- [x] 3-E 설계 정리·3-F Terraform/GitOps 구현 구조 인계
- [x] 3-F-1 State·의존 입력·GitOps 설치 책임 작업 전제 승인
- [x] B01~B07 버전·인증/Pull·배포·자원·시험·작업/비용 작업 전제 승인 반영 — 팀원 자료는 참고용
- [x] 3-F~3-H 통합 초안·03 전체 검토 준비 — 3-F~3-I
- [ ] 사용자 전체03 재검토에서 승인된 작업 전제·미확인 실행 입력·변경 필요 여부 대조
- [ ] 실제 구성 적용·접속·부하·장애·Clean Recreate·로컬 복구 시험
- [x] 03 전체 통합 검토·사용자 최종 컨펌 반영

## 3-F Terraform과 GitOps 구현 구조

### 3-F.1. 기존 승인과 이번 선택의 구분

| 기존 승인 | 이번 설계에서 유지할 내용 | 상세 근거 |
|---|---|---|
| 네 저장소와 1차 보존 | App·Infra·GitOps·Docs 책임 분리, 2차 전용 변경은 별도 저장소 | 3-A |
| State 세 Lifecycle | bootstrap / foundation / rosa 분리 | `02_TARGET_ARCHITECTURE.md` §15 / §3-C.4 |
| 일반 비용절감 삭제 범위 | 원칙적으로 rosa State. foundation/bootstrap 전체 Destroy는 별도 명시적 승인 조건 유지 | `02_TARGET_ARCHITECTURE.md` §15~16 / 3-B Lifecycle / §3-D.10.6 |
| Backend 보호 | S3·Versioning·Encryption·Public Access Block·use_lockfile 우선 | `02_TARGET_ARCHITECTURE.md` §15 |
| 사람과 실행 Role | 개인 IAM User 4개+Admin 운영, 목적별 TF 실행 Role·State 경계 | §3-C.3~4 |
| TF / GitOps / Secret 소유권 | AWS/ROSA 기반은 TF, 내부 배포 선언은 GitOps, 실제 Secret은 별도 공급 | `02_TARGET_ARCHITECTURE.md` §14·18~19 / §3-C.12 |
| 재현성 검증 | Clean Recreate + GitOps + Secret 재주입 + 실제 기능 확인 | 02·3-C·3-E |
| Data Lifecycle·복구 | RDS/Redis·Backup은 ROSA와 독립. 로컬 복구는 사전 보존한 자료로 실행 | 3-D |

세 State 분리·S3 Lock·일반 삭제 범위를 새 결정으로 재승인받지 않는다. 3-F-1은 그 경계를 실제 디렉터리·Backend Key·초기 실행·의존 입력·설치 책임으로 구현하는 선택이다. State가 foundation에 있다는 이유로 RDS/Redis/NAT를 계속 가동하는 것으로 해석하지 않는다.

### 3-F.2. 3-F-1 세 가지 승인된 작업 전제

**기록 ID:** PH2-3F-STATE-INPUT-BOOTSTRAP-OWNERSHIP  
**상태:** 사용자 작업 전제 승인 — 2026-10-01 최신 동의. 당시 소단계 승인과 구분한 전체03 최종 컨펌은 §3-I.12.4에 반영. 실제 입력/구현은 별도

| 번호 | 승인된 작업 전제 | 이유 / 적용 전 조건 |
|---|---|---|
| 1 | Infra 저장소에 세 독립 Terraform Root Module을 두고, 하나의 전용 State Bucket에서 서로 다른 Key·Lock·실행 Role로 관리 | Lifecycle과 실행 대상을 명확히 구분. bootstrap이 Backend와 TF 실행 Role을 소유하고 최초 개인 IAM 인증→Local Bootstrap→Remote 이전→목적별 Role 실행을 연결 |
| 2 | State 사이의 입력은 담당자가 필요한 비밀값 아닌 Output만 추출한 제한된 입력 파일로 전달 | ROSA 실행자가 foundation State 전체를 읽는 기본 구조를 피함. Account/Region·생성 조합·입력 개정·실제 자원 존재를 확인해 오래된 값을 차단 |
| 3 | GitOps 최초 설치는 Infra의 작은 Ansible 진입점으로 수행하고, Root Application 초기 등록 이후 내부 배포 선언은 GitOps로 관리 | TF의 Kubernetes Resource 중복 관리와 Bootstrap의 상시 App 적용을 피함. 프로젝트 Secret은 기존 별도 공급, App Sync는 공급·연결 확인까지 보류 |

이 세 가지는 사용자에게 승인받은 프로젝트 선택이며 공식 제품 문서가 전체 구조를 강제한 것이 아니다. Bootstrap 최초 실행 방법·파일 배치·Output 전달·GitOps 설치 수단을 고르되 정확한 버전·Provider Resource·IAM 정책·기능별 Manifest는 §3-F.13~19의 후속 통합안과 실제 지원 조합으로 연결한다.

### 3-F.3. 저장소와 디렉터리 대응

아래 경로는 3-F-1에서 승인받은 작업 구조다. 실제 생성·이관 또는 현재 저장소 Tree 확인 결과가 아니다.

| 저장소 / 제안 경로 | 책임 | 보관하지 않을 내용 |
|---|---|---|
| `seokpan-hybrid-infra/terraform/bootstrap/` | Backend 기반·TF 실행 Role·초기 State 이전 | 실제 State·Credential·평문 실행값 |
| `seokpan-hybrid-infra/terraform/foundation/` | Network·Data·Registry/Backup·Hybrid AWS·ROSA 공통 전제 | GitOps 내부 App Resource |
| `seokpan-hybrid-infra/terraform/rosa/` | ROSA Cluster·Machine Pool·Cluster 종속 IAM/OIDC | 영속 DB/Redis·State/Backup Bucket |
| `seokpan-hybrid-infra/terraform/modules/` | 필요한 반복 구조의 Local Module | 세 Lifecycle을 하나의 Apply로 숨기는 통합 Root |
| `seokpan-hybrid-infra/ansible/` | On-Prem 구성·GitOps 최초 설치·기존 Secret 공급·Data Backup/Restore 실행 코드 | Cloud Runtime의 상시 외부 설정 조회 의존성 |
| `seokpan-hybrid-infra/scripts/` | 실행 주체/대상 검사·필요 값 전달·Plan/인계 도구 | App Manifest를 지속 직접 Apply하는 CD |
| `seokpan-hybrid-gitops/` | 환경별 내부 Desired State·Root/App 선언·배포 Image Digest/설정 개정 | TF State·실제 Secret 값·개인 Credential |
| `seokpan-hybrid-app/` | App 변경·Test·Image Build·Application Jenkinsfile | TF Apply·GitOps 배포 선언 원본 |
| `seokpan-hybrid-docs/` | 결정·Runbook·변경/Release·정리된 검증 결과·Cost | State·Saved Plan·평문 입력·Backup 원본 |

Terraform Root Module은 그 디렉터리의 코드·변수·Provider·Backend로 별도 Plan/Apply를 수행하는 단위다. 하위 Local Module은 Root의 State에 포함되는 코드 묶음이며 독립 State라는 뜻이 아니다. Module은 실제 Resource·팀 작업 경계에 필요한 만큼만 나누고, 모양을 맞추기 위해 Resource마다 별도 Module을 만들지 않는다.

각 Root에 Provider 요구·검증된 Lock 파일·입력/Output 정의를 둔다. 세 Root의 Provider 조합이 다를 수 있으므로 공용 Lock 하나를 복사하면 충분하다고 가정하지 않는다. Cloud/로컬 복구 GitOps 경로·Overlay·Release는 §3-F.17 B04의 승인된 작업 전제이며 실제 App·Manifest 대조 후 구현한다.

### 3-F.4. Backend·State·초기 실행

#### 3-F.4.1 논리 Key와 접근 경계

State Bucket은 Backup Bucket과 별도의 전용 Bucket으로 구성하는 방향이다. 실제 이름·ARN·IAM JSON은 미확정이다. 아래 Key는 승인받은 논리 이름이며 Backend 암호화·인증 방식은 §3-F.15의 B02 승인 전제를 따른다. 실제 이름·ARN·정책과 동작은 구현 전에 확인한다.

| Root | 전용 State Bucket 안의 Key 제안 | 기본 실행 주체 | 정상 삭제 경계 |
|---|---|---|---|
| bootstrap | `phase2/bootstrap/terraform.tfstate` | TF Bootstrap Role, 최초 생성 전에는 지정 담당자의 개인 IAM 인증 | Backend/실행 Role의 지속 관리. 전체 삭제 별도 승인 |
| foundation | `phase2/foundation/terraform.tfstate` | TF Foundation Role | Code의 개별 Lifecycle 관리. 전체 Destroy 별도 승인 |
| rosa | `phase2/rosa/terraform.tfstate` | TF ROSA Role | 승인된 ROSA 가동 Window의 반복 생성/삭제 |

세 Lifecycle을 Workspace 전환으로 구분하지 않고 Root와 Backend Key로 명시한다. 모든 Root에서 대상 Role·Account·Region·Key를 확인하고 `use_lockfile=true`를 적용한다. S3 Lock 파일과 State 객체의 권한은 다르며, Lock 삭제에 필요한 권한을 State 전체 삭제 권한으로 확대하지 않는다. [3-F-R1]

전용 Bucket 하나는 비용·관리 단위를 줄이는 프로젝트 제안이다. Role별 Key 접근·Lock·Bucket 정책을 실제 확인하며, 동일 Bucket이 세 State를 하나의 State로 합치는 것은 아니다. Bucket 장애·잘못된 공통 정책의 영향은 세 State에 공유될 수 있다. 각 Bucket으로 분리하는 대안은 요구가 생길 때 비교한다.

#### 3-F.4.2 Bootstrap 최초 인증과 Remote 이전

Bootstrap이 Backend와 TF 실행 Role을 생성하는 구조를 작업 전제로 승인받았다. 실행 Role의 생성 전에 그 Role을 필수 인증으로 요구하지 않도록 최초 생성과 정상 실행을 구분한다.

1. 지정 담당자가 OS 개인 계정·개인 Workspace에서 개인 IAM 인증으로 Account/Region·권한·기존 자원 충돌을 확인한다. AWS Root Key를 사용하지 않는다. 실제 인증·MFA/STS 방법은 3-C 기준과 다음 구현 선택으로 검증한다.
2. Backend가 없는 첫 실행은 bootstrap Root의 Local State로 Backend 보호 설정과 승인된 TF 실행 Role·Trust/접근 정책을 구성한다. Local State·Backup·Plan은 보호된 작업 영역에 두고 Git/공유 로그에 올리지 않는다.
3. Backend 가용성·Versioning·Encryption·접근·Lock을 확인하고, bootstrap State를 정확한 Remote Key로 이전한다. AWS Resource를 이 단계에서 재생성하는 것으로 처리하지 않는다.
4. Remote State의 자원 대응·Serial/Lineage·Lock·Role 접근을 확인한다. 담당자가 개인 인증 후 목적별 Role로 정상 실행하며 Backend 인증과 Provider의 실행 주체를 각각 대조한다.
5. 초기 생성용 경로와 정상 실행 경로를 Runbook에 구분한다. Local State의 잔여 사본은 확인·보호·보관 정책에 따라 정리하며 검증 전 무조건 제거하거나 과거 사본을 새 진실로 적용하지 않는다.

TF 실행 Role은 bootstrap 소유, ROSA Account-wide IAM 전제는 foundation, Cluster-specific IAM/OIDC는 rosa 소유로 제안한다. 동일 Role/Policy를 여러 State가 동시에 관리하지 않는다. 실제 RHCS 흐름이 소유권 조정을 요구하면 Resource별 이유와 삭제 영향을 확인한다.

#### 3-F.4.3 실제 적용 전 확인

Backend Encryption은 필수이며 SSE-S3는 §3-F.15의 B02 승인 전제다. 실제 Backend 요청·Bucket 정책·State/Lock 쓰기 동작은 구현 전에 검증한다. KMS를 추가하는 대안은 Key Policy·복구·추가 비용까지 함께 판단한다. 접근 정책 수정으로 실행 Role이 자신의 State에 접근하지 못하게 되는 경우와 관리 담당자 복구 경로를 시험한다.

원격 State의 Lock은 동시 Write의 안전장치다. 담당자가 여러 Apply를 동시에 수행하는 운영 모델은 채택하지 않는다. 작업/리뷰 순서·실행 담당·실제 Caller를 기록하고 실패한 Lock을 작업이 살아 있는 상태에서 강제 해제하지 않는다. 역할을 분리해도 개인 IAM Admin의 직접 실행을 기술적으로 모두 차단한 것은 아니라는 3-C의 경계를 유지한다.

### 3-F.5. State 사이의 필요한 값 전달

#### 3-F.5.1 전달 방식 제안과 비교

| 방식 | 장점 | 부담 / 판단 |
|---|---|---|
| `terraform_remote_state` 직접 조회 | Root 간 Output 연결이 간단 | Output만 사용하는 코드여도 원본 State Snapshot 읽기 권한이 필요 [3-F-R2]. 초기 기본 전달 방식으로 선택하지 않음 |
| 필요한 Output만 제한된 입력 파일로 추출 — 제안 | 전달 범위·개정·확인 시점을 명시. ROSA 실행자에게 foundation Snapshot 접근을 요구하지 않음 | 담당자의 최신화·원본/대상 확인 필요 |
| 별도 AWS 저장 위치에 필요한 값 게시 | 접근 정책과 소비자 분리를 자동화하기 쉬움 | 저장 Resource·정책·개정·정리의 추가 책임. 초기 필수 구성에 자동 추가하지 않음 |
| AWS Data Source로 재조회 | 실제 자원 존재를 조회 가능 | Tag/Name 선택 모호성·조회 권한·Account/Region 검증 필요. 필수 입력의 확인 수단으로 검토 |

HashiCorp는 외부 공유 값을 State와 다른 위치에 명시적으로 게시하는 대안을 설명한다. [3-F-R2] 이번 파일 전달 선택은 작은 팀의 초기 구현을 단순화하기 위한 프로젝트 제안이다. 사람이 반복 작성하는 임의 숫자·복붙 목록이 아니라 제한된 추출·검증 절차로 구현한다.

#### 3-F.5.2 전달할 의미와 제외할 항목

| 연결 | 전달할 의미 — 실제 필드명/값 미확정 | 제외할 값 |
|---|---|---|
| bootstrap → 각 Root 실행 | Backend 대상·논리 Key·실행 Role 참조·보호된 인증 절차 | 개인 Key·Root Credential·Session Token을 입력 파일에 기록하지 않음 |
| foundation → rosa | 필요한 VPC/Subnet·승인된 ROSA 공통 Role/OIDC 참조·필요 Network 입력 | RDS/Redis 비밀번호·Secret 전체·전체 State/전체 Output 덤프 |
| foundation/rosa → GitOps 환경 설정 | 실제 App에 필요한 연결 대상·환경 구분·공개 진입 기준·설정 개정 | 비밀값은 3-C 공급 절차로 분리. TF가 App Secret을 직접 생성하지 않음 |
| Secret 공급 → App 배포 | 준비된 Secret 참조·값 없는 개정 ID·검증 완료 상태 | 평문 Secret·age Identity·담당자 개인 Credential |

비밀값 아닌 전달 정보라도 민감 접속정보는 보호된 실행 설정에서 관리하며 공개 Docs·Evidence·로그로 옮기지 않는다. 실제 Backend Key/Role/Endpoint 값은 공개 예시로 만들어 쓰지 않는다. 필요 Output의 이름과 자료형을 명시하고 허용 목록에 없는 값을 추출하지 않는다.

#### 3-F.5.3 오래된 입력 차단과 확인 책임

추출은 해당 State 접근 권한이 있는 담당자가 수행한다. 생성한 입력은 개인 Workspace의 Git 밖 보호 영역에 두고 소비자에게 필요한 범위로 전달한다. 추출 코드가 `terraform output -json` 전체 내용을 로그/임시 공유 파일에 남기는 구조가 되지 않도록 실제 동작을 확인한다.

입력에는 의미별 Schema/개정, Account/Region 확인, 출처 Root의 Code 개정·확인 시점과 생성 조합을 연결한다. 민감 값 없는 Metadata를 기록하고, 중요한 Network·Role 값이 바뀌면 ROSA Plan 전에 새 입력으로 갱신한다. 실제 자원 존재·선택 범위·현재 기반과의 일치를 확인하고 오래된 Subnet/Role 값이면 실행을 중단한다.

입력 파일 하나를 받았다는 이유로 foundation Apply와 rosa Apply가 자동 직렬화되지는 않는다. 의존 자원 변경이 끝난 상태와 검토된 입력을 확인한 후 다음 Root를 실행한다. foundation 권한이 없는 ROSA 실행자의 확인 수단·조회 권한은 §3-F.15.2에서 연결하며, 처음부터 foundation State 전체 읽기를 임시 편의로 추가하지 않는다.

### 3-F.6. Terraform·Ansible·GitOps·Secret의 소유권

| 대상 | Owner / 제안 실행 코드 | 중복 관리 방지 |
|---|---|---|
| Backend·TF 실행 Role | Terraform bootstrap | foundation/rosa에서 다시 선언하지 않음 |
| VPC·기본 Subnet/Route/SG·VPN EC2/EIP·RDS/Redis·ECR/Backup S3·ROSA 공통 IAM | Terraform foundation | ROSA가 자동 생성/관리하는 자원과 팀 소유 자원을 구분 |
| ROSA Cluster·Machine Pool·Cluster-specific IAM/OIDC·승인된 종속 Binding | Terraform rosa / RHCS | 같은 객체를 AWS Provider와 RHCS/CLI가 동시에 관리하지 않음 |
| On-Prem Gateway·Data VM의 OS/서비스·Backup/Restore 실행 구성 | Infra의 Ansible | VM Provisioning 도구·실제 자산은 후속 선택. AWS 기반 Resource의 Owner를 가져오지 않음 |
| OpenShift GitOps 최초 설치 선언 | Infra의 최소 Ansible Bootstrap — 예외 범위 | 실제 Subscription/필요 설치 객체만 명시. App 배포 선언을 상시 적용하지 않음 |
| Operator가 생성하는 Deployment/Secret 등 | 해당 Operator / ROSA 관리 서비스 | TF/Bootstrap/일반 GitOps가 생성 결과를 덮어쓰지 않음 |
| Cloud Root Application·AppProject·Namespace·App 배포 선언 | GitOps, Root 초기 등록만 Bootstrap 예외 | Root가 등록된 뒤 GitOps 원본 개정으로 변경. 재실행 시 무조건 덮어쓰기 금지 |
| 로컬 Offline Recovery 적용 객체 | B04의 Infra Ansible 실행 예외, 선언 원본은 GitOps Recovery Overlay | 장애 전 Render/보존본만 지정 로컬 Namespace에 적용. 실행 중인 Argo와 같은 객체 중복 관리 금지, Secret 공급 Owner는 별도 |
| 프로젝트 Secret Object·값 | 3-C의 지정 공급 절차 | 빈 Secret·평문 값·같은 객체를 Argo 관리/Prune 대상으로 등록하지 않음 |
| App Image Build·Test·ECR Push | App Jenkinsfile / 기존 Jenkins | CI가 TF Apply·직접 App Manifest 배포를 수행하지 않음 |
| Image Digest·배포 설정·Release 조합 | GitOps / 승인된 변경 흐름 | Jenkins의 직접 Cluster 변경으로 Git Desired State를 우회하지 않음 |

동일 Data SG의 규칙을 두 State에 나누어 소유할 때는 SG 본체의 inline ingress/egress와 별도 Rule Resource를 혼용하지 않는다. 본체는 foundation, 각 규칙은 명시적 Rule Resource의 단일 Owner로 관리하고, SG 전체 규칙 목록을 강제로 비우거나 다른 State의 규칙을 덮어쓰는 선언도 금지한다. foundation 재실행 전후 rosa Binding 유지, rosa Binding 해제 후 foundation 규칙 유지, 재생성 후 새 Worker SG 연결과 양쪽 정상 Plan을 IM-03/T19에서 확인한다. 실제 선택 Provider의 Resource Schema·삭제 의존성은 구현 Gate이며 이 문서만으로 동작을 검증한 것은 아니다. 세 State의 승인된 경계를 유지하며 네 번째 State를 추가하지 않는다. 근거는 [3-F-R18]이다.

실제 IDP/OAuth·RBAC·Argo 권한의 Resource별 Owner와 최초 공급은 3-C 및 §3-F.17의 범위에 맞춰 구현 전에 확인한다. GitOps 설치용 최소 예외를 일반 cluster-admin 상시 작업으로 확대하지 않는다. 3-F-1에서 새 Namespace·실제 Policy·Kubernetes Provider 설정을 생성하지 않았다.

### 3-F.7. GitOps 최초 설치와 인계

#### 3-F.7.1 초기 실행 순서와 Gate

1. ROSA Ready와 실제 API·Context·관리 Caller를 확인한다. 재생성 전의 Context/Token을 새 Cluster의 인증으로 취급하지 않는다.
2. Infra의 작은 Ansible 진입점이 승인된 GitOps Operator 설치 선언만 적용하고 설치 상태·Argo CD 준비·지원 버전을 확인한다. 공식 설치는 Subscription을 사용하는 경로가 있으며 실제 Namespace/채널/권한은 선택 버전에서 확인한다. [3-F-R3]
3. 3-C의 지정 공급 절차로 필요한 GitOps Repo 읽기 인증을 공급한다. Root Application은 승인된 GitOps Repo/Revision/Path로 초기 등록하고, 이미 존재하면 대상/Owner를 확인하며 무조건 덮어쓰지 않는다.
4. GitOps에서 AppProject·Namespace 등 기초 Desired State를 적용한다. App 배포는 필요한 Secret·Image Pull 경로·연결 설정이 준비될 때까지 보류한다. Root가 Child App의 자동 배포를 먼저 시작하지 않도록 선언 구조를 확인한다.
5. 지정 공급자가 실제 App/IDP 등 필요한 Secret을 공급하고 참조·환경·개정을 대조한다. 실제 프로젝트 Secret은 GitOps 관리/Prune 대상에서 제외한다.
6. 승인 Release의 App Sync를 수행하고 FE/HTTP/WSS·DB/Redis·인증·업무 기능을 확인한다. 배포 동기화 상태와 3-E의 업무 재개 조건을 서로 다른 결과로 남긴다.
7. 정상 운영의 내부 배포 선언은 GitOps로 변경한다. Bootstrap 재실행은 설치/등록 상태 확인과 필요한 초기 복구 범위에 한정하고 App Manifest를 계속 직접 Apply하지 않는다.

App Sync 보류는 §3-F.17 B04로 승인된 명시적 Application·자동 Sync 비활성화 경계이며 선택 버전에서 실제 동작을 확인한다. ApplicationSet을 쓰면 생성된 Child Application만 직접 바꾸는 것으로 보류가 유지되는지 가정하지 않는다. Argo CD의 자동 Sync·Prune는 별도 설정으로 다룬다. [3-F-R4]

#### 3-F.7.2 Prune와 Namespace 삭제

Secret Object를 GitOps에서 제외해도 Namespace를 삭제하면 그 안의 Secret이 소실될 수 있다. Namespace/Root/Operator 설치 영역의 삭제·Prune는 App Image 변경과 구분해 검토한다. App 단위 자동 Sync·Prune·SelfHeal·수동 검토 경계는 §3-F.17 B04의 승인된 작업 전제로 연결하고, 초기 Bootstrap이 끝났다는 이유로 전 영역의 자동 삭제를 허용하지 않는다.

자동 Prune 비활성화는 Application 자체를 삭제할 때의 연쇄 삭제를 막는 설정이 아니다. Root/Child Application의 실제 finalizer·삭제 방식·관리 Resource 목록과 Namespace 포함 여부를 별도로 대조한다. Namespace 삭제는 별도 공급 Secret에도 영향을 주므로 보호 대상·삭제 범위 검토를 생략하지 않는다. 선택 Argo 버전에서 지원하는 실제 삭제 동작을 확인하고, 시험은 격리된 대상에서 수행해 기존 데이터/Secret을 보호한다 [3-F-R19].

Sync Wave/순서만으로 Git 밖 Secret 공급 완료를 확인했다고 판단하지 않는다. GitOps가 보는 Resource 상태와 별도 공급 Gate를 실제로 연결한다. 정상 Secret 교체·재주입·실패 후 재실행·Clean Recreate에서 빈 값으로 덮이거나 삭제되는지 시험한다.

#### 3-F.7.3 Runtime Image Pull과 오프라인 복구

ECR CI User는 Push 주체이며 Runtime Pull을 대신하지 않는다. ROSA Classic의 Runtime Image Pull 방식·권한·새 Node/Pod 동작은 §3-F.16 B03의 승인된 작업 전제로 연결한다. CI의 ECR 로그인 Token을 장기 Pull Secret으로 복사하는 방식으로 이 Gate를 해결하지 않는다.

로컬 복구는 사전 보존한 Harbor Image·Backup·환경 설정·Secret·도구를 사용한다. Cloud용 GitOps Repo를 장애 후 GitHub에서 새로 내려받아야만 복구되는 구조를 필수 경로로 두지 않는다. 로컬 배포·독립 Namespace·새 Redis·CA/접속 설정은 3-D·3-E 및 §3-F.17.3 B04로 승인된 Recovery 실행 예외로 연결한다.

### 3-F.8. Plan·Apply·정리 Workflow

승인된 Branch→fmt→validate→plan→Review→Approved Apply 흐름을 실제 실행 입력과 연결한다. 초기 TF 실행은 3-C 기준의 지정 담당자 개인 인증·목적별 Role을 사용한다. Jenkins에 Terraform 광역 Apply 권한을 추가하지 않는다.

| 단계 | 확인할 결과 | 기록·보호 기준 |
|---|---|---|
| 실행 전 | OS 사용자·실제 AWS Caller/Role·Account·Region·Root·Backend Key·Code/Lock·의존 입력 | 실제 Credential을 출력하지 않고 비민감 실행 Metadata만 기록 |
| 초기화·검증 | 검토된 Provider/Module·Lock·Backend 연결·fmt/validate | 임의 `init -upgrade`를 정상 초기화와 섞지 않음 |
| Plan | 생성/변경/삭제/교체·Data/Storage/권한·의존·비용 영향 | Saved Plan은 민감값을 포함할 수 있으므로 보호된 작업 영역에 보관 [3-F-R5] |
| Review | 정확한 Root·입력 개정·삭제 범위·Cost Gate·실행 담당 | Code만이 아니라 실제 Plan을 검토. 상세 Secret이 있는 Plan을 Git/공개 Evidence에 올리지 않음 |
| Apply | 검토된 동일 Code/Lock/입력 조합의 승인된 Plan | 검토 이후 기반/입력/Code 변경 시 새 Plan·Review. 실제 실행 결과와 변경 이유 기록 |
| 확인·인계 | 실제 자원·State 대응·필요 Output·접속·복구 영향 | Apply 성공을 Runtime/복구 PASS로 확대하지 않음 |

State Lock을 끄거나 전 Root를 연속 Destroy하는 명령을 일반 Wrapper에 넣지 않는다. Force-unlock·State 수동 조작·Import·Target Apply 등은 실제 필요와 영향이 확인된 예외 절차로 구분한다. 정상 비용절감의 rosa 삭제 전에도 App 쓰기 제한·진행 상태·Backup·Data/Network 잔여 의존성을 확인한다.

첫 Full Apply 전에 전체 $500 예산의 Cost Gate를 통과해야 한다. State Bucket·암호화·NAT/EIP·Data 잔존 과금·ROSA 실행 시간·Backup 전송/보관을 함께 계산한다. 문서 작성만으로 Cost Gate·Plan·승인된 실제 Apply가 완료되었다고 기록하지 않는다.

### 3-F.9. Runtime Lifecycle과 State 소유권

| 대상 | 기존 승인 기준 | 3-F 구현에서 확인할 내용 |
|---|---|---|
| ROSA | rosa State 반복 생성/삭제 | OIDC/Operator Role·Machine Pool·종속 자원 정리·재생성 입력 |
| RDS | foundation에 보존, 미사용 시간 Stop 후보 | 최종 로컬 Backup 확보·실제 Stop/Start·자동 재시작·Drift/정상 Plan |
| Redis | foundation에 유지 또는 계획 재생성 | 서비스 중단/새 Runtime 기준·전체 Foundation Destroy 없이 대상 Lifecycle 관리 |
| NAT/EIP/Hybrid | 필요한 실행/전송 동안 유지, 의존 종료 후 코드로 재생성 가능 | Backup/Export·ROSA 설치·On-Prem 경로와 삭제/주소 변경 영향 |
| State/Backup Bucket·ECR | 지속 보관 | ROSA 삭제와 별도 보관·접근·정리 정책 |

State 경계는 자원의 소유권이고 Runtime 비용절감은 자원별 가동/재생성 동작이다. RDS Stop은 일반적으로 Terraform Destroy를 뜻하지 않으며 실제 API/운영 명령·Code가 충돌 없이 동작하는지 확인한다. 서비스 고유 동작을 처리할 도구·Flag·모듈 경계는 다음 구현 설계에서 정한다.

### 3-F.10. 주요 대안과 선택 이유

| 결정 | 선택 제안 | 유지할 대안 / 재검토 조건 |
|---|---|---|
| Root/Backend | 독립 Root 3개·전용 Bucket 1개·서로 다른 Key/Lock/Role | State별 Bucket 분리는 관리/정책의 공통 장애 영향 축소가 필요할 때 비교. Workspace만으로 Lifecycle 구분하는 안은 Owner/실행 경계가 모호해 초기 선택에서 제외 |
| State 의존 값 | 제한된 비밀값 아닌 입력 파일 | 별도 게시 저장소·Data Source는 자동화/변경 빈도 증가 시 검토. Remote State는 Snapshot 접근 영향이 허용될 때만 별도 판단 |
| GitOps 최초 설치 | Infra의 작은 Ansible 진입점·Root 초기 등록·후속 GitOps | Shell Script도 가능. 기존 On-Prem 자동화와 실행/검증을 연결하기 쉬워 Ansible 우선. TF Kubernetes Provider로 상시 내부 Desired State 관리하는 안은 중복 Owner를 만들지 않도록 제외 |

다른 대안이 기술적으로 불가능하다는 뜻이 아니다. 작은 팀·별도 포트폴리오·반복 ROSA 재생성·사전 로컬 복구의 현재 범위에 맞춘 선택이다. 실제 지원 제약이 나오면 이유·영향·작업량·비용·재시험을 비교한다.

### 3-F.11. 실제 입력과 검증 Matrix

#### 3-F.11.1 구현 전 입력

| 입력 | 필요한 판단 | 상태 |
|---|---|---|
| Account/상위 정책·실제 IAM/Role·Region/Quota | Bootstrap/TF 실행·Backend 접근·ROSA 설치 가능성 | 미확인 |
| 공용 Controller·개인 작업 공간·실제 CLI 경로/버전 | 팀 자료의 보고 현황과 실제 실행 환경 일치 | 팀원 자료만 확보 |
| Terraform/AWS/RHCS Provider·ROSA/GitOps Version/Channel | 생성 가능한 Resource/인증/Lock·삭제·Bootstrap 조합 | 후보/지원 조합 확인 필요 |
| Backend 이름·Encryption·Role Trust·정책·예비 관리 경로 | State/Lock 보호·순환 의존성 해소·복구 | §3-F.15 B02 작업 전제 승인, 실제 값/동작 미확인 |
| 3-B Network의 실제 주소/Source·3-C Credential·3-D Data·3-E App 값 | HCL/Manifest/Ansible의 실제 입력·Secret State 영향 | 승인 기준은 확보, 실제 값/동작 미확인 |
| 실제 Repo·Branch 보호·담당·Plan/실행 보관 | 코드/리뷰/실행 주체·증거 경계 | 미확인 |

#### 3-F.11.2 시험 대응표 — 현재 모두 미실행

| ID | 시험 | 합격 판단에 필요한 결과 |
|---|---|---|
| IM-01 | Local Bootstrap→Remote 이전 | 실제 Infra 대응 유지·정확한 Key/Lineage·Remote 정상·보호된 잔여 사본 처리 |
| IM-02 | 세 Root별 Caller·State/Lock 접근 | 목적별 Role의 필요한 접근 성공·무관 State 접근 시험·Lock 충돌/종료 확인 |
| IM-03 | 정상 생성·비용절감 rosa 삭제 | foundation 재실행에도 rosa Data SG Binding 유지, Cluster 삭제 전 Binding 해제, 기반 Rule/Data/Network 보존, 재생성 후 새 Worker SG 연결·양쪽 정상 Plan·잔존 비용 확인 |
| IM-04 | 제한된 입력 추출·오래된 입력/다른 Account 전달 | 불필요 Output/Secret 제외·개정 대조·잘못된 입력 차단 |
| IM-05 | GitOps 최초 설치·Bootstrap 재실행 | 설치/초기 등록·정상 Owner·App 직접 재적용/덮어쓰기 없음 |
| IM-06 | Secret 공급 전 App Sync·공급/교체·삭제 보호 | 보류 Gate·필수 참조·값 유지·빈 Secret 중복 관리 없음. 자동 Prune·수동 삭제·Application finalizer/연쇄 삭제·Namespace 삭제를 구분 |
| IM-07 | ROSA Clean Recreate | 새 Host/Context·지원 Pull·GitOps/Secret·3-E 기능/업무 상태 검증 |
| IM-08 | Offline 로컬 복구 | 사전 자료·Harbor·DB 복원·새 Redis·인증/게임, AWS/GitHub 신규 조회 비의존 |
| IM-09 | Saved Plan·State·Ansible/CI 출력 검사 | 실제 Secret 노출·접근·실패 정리·평문 Artifact 경계 확인 |

설계 검토와 실제 fmt/validate/Plan·Apply·Runtime 시험은 다른 결과다. 현재 문서에 HCL이 없으므로 도구 검증이 통과했다고 주장하지 않는다. 실제 코드를 만들 때는 선택 버전의 Validate/Plan·격리된 생성/정리·재생성·Secret·App 시험을 수행한다.

### 3-F.12. 팀원 버전 자료와 다음 설계

`terraform-version-guide.md`는 §3-E.16의 TEAM DRAFT + PENDING DECISION 상태로 사용한다. Terraform 1.16.4와 AWS CLI 2.37.5는 팀원 보고 설치값이며 Controller를 직접 확인하지 않았다. 공용 설치·개인 Clone·PR·Lock 파일의 방향은 참고하지만 실제 Branch 보호·인증·배포 조합이 적용되었다고 판단하지 않는다.

앞선 3-F-1 승인에 버전 선택은 포함되지 않았다. 이후 **§3-F.13의 B01~B07 통합안**을 묶어 검토했고 2026-10-01 작업 전제로 승인받았다. 팀원 자료 자체의 참고용 상태와 실제 설치/지원 확인 대기는 유지한다. §3-F.14~19에서 CLI/Provider/ROSA/GitOps 후보·Backend 보호·인증·Pull·배포·자동화·복구를 정리하고 3-G·3-H에서 시험·작업·비용 영향을 함께 검토한다. 정확한 CLI 고정과 `required_version` 허용 범위, Root별 Provider Lock, Remote Module 버전, 설치/갱신·ROSA 삭제 호환성을 구분한다. 팀원 자료의 버전 후보를 우선 대조하되 그대로 채택하는 것은 아니다.

이어서 GitOps 환경별 구조·Release·Sync/Prune·App 배치/Pool·Data/Hybrid 자동화·로컬 복구 실행을 실제 입력과 연결한다. 3-E의 인증·Snapshot·중복/부분 실패 규약은 기존 App에서 충족하는 부분과 필요한 변경을 구분한다. 단순 구조 선택을 반복 승인받지 않고 새 경계 변경이 필요한 선택을 제시한다.

### 3-F.13. 3-F·3-G·3-H의 B01~B07 승인된 작업 전제

**기록 ID:** PH2-03-BATCH-FGH-01  
**상태:** B01~B07 작업 전제 승인 — 2026-10-01 사용자 컨펌. 앞선 3-F-1 승인과 별도로 기록. 이후 전체03 최종 컨펌은 §3-I.12.4  
**진행 방식:** 독립 설계는 함께 작성하고, 승인 후 반복 기록·참조 반영·후속 설계 정리는 일괄 수행한다. 실제 Apply·배포·장애 시험은 의존 순서와 기존 실행 승인 조건을 따른다.

| ID | 승인된 작업 전제 | 연결 절 / 실제 확인 조건 |
|---|---|---|
| B01 | Terraform 1.16.4·AWS Provider 6.66.0·RHCS 1.7.7을 초기 검증 후보로, ROSA 4.20 계열·GitOps 1.21.4를 지원 조합 후보로 사용. 실제 지원 조회·검증 후 정확한 버전과 Lock을 기록 | §3-F.14. 최신값 자동 추종 아님. 계정/Region에서 미지원 또는 실제 Provider 제약 충돌이면 적용 보류·대안 영향 검토 |
| B02 | State Backend는 명시적 SSE-S3·Versioning·TLS·Public Access Block·Key별 접근·S3 Lock. 개인 MFA 인증에서 목적별 STS Role로 TF 실행 | §3-F.15. 기존 4명 Admin 정책 유지. 새 KMS/Identity Center를 기본 작업에 추가하지 않음 |
| B03 | ROSA Classic Worker Role에 팀 ECR Repository만 Pull할 수 있는 정책을 연결. Runtime Pull용 추가 IAM User는 기본안에 추가하지 않음 | §3-F.16. 실제 Classic Role/지원 경로 확인. Worker Role을 공유하는 모든 Cluster/Node에 권한 영향이 있음 |
| B04 | Kustomize 공통 Base+Cloud/Recovery Overlay, 고정 Image Digest, CI 검증→GitOps PR 검토→Sync. 초기 준비 후 App 자동 Sync·SelfHeal, 자동 Prune는 보류 | §3-F.17. 플랫폼/초기 Root는 검토 후 수동 Sync. Secret·Namespace 삭제와 Schema Rollback 분리 |
| B05 | Cloud Worker 3개(각 AZ 1개)·FE/BE 각 3 Replica를 초기 후보로 하고 PDB·분산 배치·Rolling 설정·DB Pool·자원 여유를 함께 검증. Recovery는 초기 1 Replica씩 | §3-F.18. Worker는 m5.xlarge 후보. Classic 전체 최소 9 EC2를 비용에 반영. Source의 다중 Pod 상태 공유 확인 후 적용 |
| B06 | 기능·재현·보안·장애·복구 시험을 필수 묶음으로 수행하고, 성능/복구 수치 목표는 3-G의 승인된 프로젝트 Acceptance 기준을 사용 | §3-G.2~7. 모든 실제 결과 미측정. 목표 미달은 그대로 기록하고 원인/범위 검토 |
| B07 | 네 작업 트랙의 역할·인계·종료 조건과 두 AWS 검증 Window를 묶어 계획. $450 예상 비용 초과 시 신규 가동 보류·$50 Buffer, $500 전체 한도 유지 | §3-H.2~7. 사람 배정·실제 일수/단가·Window 시간은 미확인. Technical/Demo Freeze 유지 |

일곱 개는 독립적인 선택 묶음을 세었기 때문이며 고정 개수 규칙이 아니다. B01~B07을 작은 승인 단계로 다시 분해하지 않는다. 정확한 ARN/Host/패치·측정에 따른 Pool/Probe 튜닝은 승인된 범위의 실행 입력으로 확인한다. 새로운 계정·상시 서비스·비용/권한 확대·Architecture 변경·성공 기준 완화가 필요해지는 경우에만 그 변경과 영향을 다시 결정한다.

2026-10-01 B01~B07의 우선 승인이 기록됐으며, 반영 후 전체 문서 검토는 별도 단계로 남았다. 당시 B01~B07은 작업 전제로 먼저 승인되었고 전체03은 검토 대기였다. 이후 두 문서 전체 최종 승인과 등록 완료 보고는 §3-I.12.4에 반영했다. 조건부 후보의 실제 지원·시험 성공·비용 충족·구축 승인을 추가하지 않는다. 이번 승인 반영 기록은 §3-I.12.2에 있다.

### 3-F.14. 버전 후보와 확인 순서 — B01

| 대상 | 초기 후보 / 고정 방법 | 확인할 근거와 한계 |
|---|---|---|
| Terraform Core | `1.16.4`, 공용 Tool Manifest에 정확한 설치값 기록. 초기 Root의 `required_version`도 동일값으로 제한하는 방향 | 팀원 후보와 공식 배포 존재 확인 [3-F-R6]. 실제 Controller 설치·CLI 동작·S3 Lock은 미확인 |
| AWS Provider | `hashicorp/aws` `6.66.0` 초기 검증 후보, 세 Root 중 필요한 Root에 정확한 제약과 각각의 Lock | 공식 Release 확인 [3-F-R7]. 6.67.0이 9/30 공개됐지만 새 버전을 자동 채택하지 않음. 6.66.0의 프로젝트 안정성이 검증됐다는 뜻도 아님 |
| RHCS Provider | `terraform-redhat/rhcs` `1.7.7` 초기 후보 | 공식 Registry 공개값 [3-F-R8]. Classic Resource·IAM/OIDC·Machine Pool·삭제 순서 Schema를 실제 Validate/Plan으로 확인. HCP Module을 Classic 대체품으로 사용하지 않음 |
| ROSA Classic | `4.20` 계열의 실제 제공되는 GA 패치 후보 | 실제 계정·서울 Region의 제공/지원 조회 전 정확한 패치 미정. OCP 지원표만으로 ROSA 생성 가능성을 확정하지 않음 |
| OpenShift GitOps | `1.21.4` 후보, 실제 1.21 채널/CSV 확인·InstallPlan 수동 승인 | 공식 Release의 OCP 4.20 호환 확인 [3-F-R9]. 실제 Catalog의 가용 CSV·설치값 확인. `latest` 채널이나 무조건 자동 Operator Upgrade를 기본안으로 두지 않음 |
| AWS CLI / rosa / oc | 팀원 AWS CLI `2.37.5`는 참고 설치값. 실제 Controller에서 필요한 API/STS 지원 확인. `oc`는 선택 OpenShift 조합에 맞춤 | 실제 설치값·공식 배포 경로·Checksum·실행 결과를 Tool Manifest에 기록. 현재 임의로 확인 완료 처리하지 않음 |
| Ansible / SOPS / age / DB 도구 | 기존 도구 활용 우선, 실제 설치·Driver/DB 호환을 확인한 정확한 버전 기록 | 새 제품 도입으로 일정 확대하지 않음. MariaDB Engine/Client/Schema는 3-D의 실제 Source 확인 조건 유지 |

공식 자료의 공개 버전 존재와 전체 조합의 검증 성공을 구분한다. 실행 전 Code Revision·Root별 Provider Schema·Module 고정·플랫폼 지원·Tool 버전을 하나의 Manifest로 묶고 fmt/validate/Plan→짧은 통합 시험→Clean Recreate에 같은 조합을 사용한다. Local Module은 Infra Commit으로, 외부 Module은 정확한 버전/Commit으로 고정한다. `.terraform.lock.hcl`은 Core/Module/ROSA 버전까지 고정하지 않는다.

ROSA의 관리형 서비스 지원/필수 갱신을 영구 패치 고정으로 막을 수 있다고 가정하지 않는다. 필수 서비스 변경과 팀이 선택한 업그레이드를 구분해 Manifest·변경 이유·재검증 범위를 기록한다. 검증에 실패한 후보를 단순 설치 성공으로 채택하지 않는다.

### 3-F.15. Backend 보호·개인 인증·실행 Role — B02

#### 3-F.15.1 보호와 State 복구

State Bucket에 SSE-S3(AES256) 기본 암호화를 코드로 명시하고 Versioning·Public Access Block·TLS 전용 접근을 적용한다. SSE-S3는 저장 시 암호화이며 추가 KMS Key·Key Policy 관리 없이 구성할 수 있다 [3-F-R10]. State 안의 비밀번호가 사라지거나 접근자가 읽을 수 없게 되는 기능은 아니다. 비밀값의 State 유입은 최소화하고 실제 State/Plan 사본도 보호한다.

Backend의 암호화 요청 설정과 Bucket 정책을 맞춰 State 및 `.tflock` 쓰기를 시험한다. 일반 삭제로 Bucket/현재 State/Version을 제거하지 않는다. Versioning만으로 복구를 PASS 처리하지 않고 격리된 확인 경로에서 알려진 이전 Version을 대조한다. Serial/Lineage·AWS 실제 자원·검증된 최신 상태를 확인한 후 State 복구 작업을 수행하며 임의의 오래된 Version을 즉시 운영에 덮어쓰지 않는다.

Role별 허용은 State Key의 Get/Put와 Lock Key의 Get/Put/Delete 및 필요한 제한된 List로 구분한다. 다른 Key 접근 실패·TLS 외 접근 차단·Lock 충돌을 시험한다. 사람 Admin 권한 때문에 Role 경계가 모든 직접 접근을 강제로 차단하는 것은 아니며 3-C의 협업 모델을 유지한다.

#### 3-F.15.2 CLI 인증과 실행 입력

개인 IAM User의 MFA를 사용하는 STS AssumeRole Profile을 목적별로 설정하는 방향이다. 실제 MFA 장치/Trust Policy와 세션 수명은 적용 전에 확인한다. 최초 bootstrap은 실행 Role이 없으므로 개인 MFA 기반 STS 세션으로 시작하고, Backend/Role 생성·State 이전 후 정상 목적별 Role 실행으로 전환한다. AWS Root Access Key를 만들지 않는다.

개인 CLI Credential은 개인 OS 계정의 보호 영역에 두며 공용 저장소/Controller 공용 홈/Job Credential로 공유하지 않는다. AssumeRole Trust는 지정 사람 IAM Principal과 MFA 조건으로 제한한다. 실제 Account/Caller/Profile·Region·Backend Key·입력 개정은 Plan 전에, 동일 조합은 Apply 전에 확인한다. Backend와 Provider가 서로 다른 Profile을 우연히 쓰는 구성을 차단한다.

ROSA 실행 Role의 기반 자원 확인은 읽기 전용 AWS/OCM 조회로 수행한다. 필요한 VPC/Subnet/Route/Role 조회 권한을 명시하고 foundation State 전체 읽기 권한으로 해결하지 않는다. 현재 Account-wide Admin 사용자 4명, ECR CI User 1명, Backup User 1명이라는 기존 계획을 변경하지 않는다.

### 3-F.16. ECR Runtime Pull·Harbor 보존 — B03

#### 3-F.16.1 ROSA Classic의 정확한 경계

Red Hat 자료는 Node가 Image를 Pull하는 인증과 Pod 안의 Build/Argo 작업 인증을 구분한다 [3-F-R11]. 배포 Pod의 Image는 Node가 가져오며 Jenkins Push Credential을 전달하는 것으로 설계하지 않는다. GitOps는 고정 Digest를 Manifest에 반영하며 ECR 태그 조회용 Pod 인증을 추가하는 Image Updater는 기본안에서 제외한다.

AWS 문서는 Classic이 서비스 정의의 Customer Managed Policy를 사용한다고 구분한다 [3-F-R12]. `ROSAWorkerInstancePolicy`라는 AWS Managed Policy의 공개 JSON [3-F-R13]을 본 것만으로 **실제 Classic Worker Role에 동일 정책/권한이 있다고 판단하지 않는다**. 실제 생성된 Role ARN·Policy·지원 경로를 조회한다.

foundation에서 소유하는 프로젝트용 Pull 정책을 실제 Classic Worker Role에 연결하는 방향이다. 정책은 `ecr:GetAuthorizationToken`에 필요한 `Resource:*`와 지정 FE/BE Repository ARN의 `BatchGetImage`·`GetDownloadUrlForLayer`·`BatchCheckLayerAvailability`만 허용한다. Token API의 범위와 Repository 읽기 범위를 구분한다. 기존 ROSA 서비스 정책 원본을 직접 변경하거나 팀 Repository에 `red-hat-managed=true`를 붙여 권한 제한을 우회하지 않는다.

Worker Role을 여러 Cluster가 공유하면 추가 권한은 그 Role을 쓰는 모든 Node에 적용된다. 이는 Pod별 IAM 격리가 아니다. 프로젝트 전용 Account Role Prefix/Role을 사용하는 방향으로 실제 충돌·Owner를 확인한다. 기존 공유 Role이라면 영향받는 Cluster와 팀을 확인한 뒤 연결 범위를 결정한다. 다른 State가 같은 Role/정책 Attachment를 중복 소유하지 않도록 foundation 자원표에 기록한다.

#### 3-F.16.2 적용 전 Gate

선택된 Classic 버전에서 지원하는 Node 인증 흐름으로 새 Worker/캐시 없는 Pod의 FE/BE Digest Pull, 인증 Token 수명 경과 후 새 Pull, Clean Recreate를 확인한다. 관리형 Node를 수동 SSH 수정하거나 비지원 Credential Provider를 설치하지 않는다. 정책·Network·DNS·Region·Repository·CPU Architecture 문제를 나눠 진단한다. CI Image Push 성공을 Runtime Pull 성공으로 기록하지 않는다.

ECR Token은 12시간 유효하며 [3-F-R16], 프로젝트의 지속 인증 시험 후보는 같은 Node 인증 경로에서 최초 Pull 뒤 12시간 이상 지난 후 캐시 없는 Image를 Pull하는 조건이다. 첫 Pull 시각만으로 실제 사용 Token의 발급/만료/갱신 시각을 입증하지 않는다. 관측할 수 있으면 값 없이 발급/재인증 Metadata를 기록하고, 관측할 수 없으면 지속 사용 후 새 Pull 성공까지만 주장한다. 예정된 통합 작업 시간과 겹쳐 수행하고 시험만을 위한 대기 가동시간·비용을 숨기지 않는다. 비용/시간 때문에 수행하지 못하면 미실행/부분 검증으로 남기며 새 Cluster Pull 성공으로 수명 경과 시험을 대체하지 않는다.

이 방식이 실제 지원/검증되지 않으면 App Sync를 보류하고 원인·대안을 보고한다. CI Token 복사, 장기 공유 Pull User, 새 Secret 갱신 Operator를 자동으로 추가하지 않는다. B03 승인 전제의 기본 계정 수는 §3-C.13.1과 동일하며, 사람 4개·CI/Backup 각 1개로 총 IAM User 6개다.

Harbor에는 승인된 Recovery Release를 장애 전에 보존한다. ECR/Harbor 각 Registry에서 실제 Digest·플랫폼 Image·Release ID를 확인하고 Mapping을 기록한다. 전송 방식에 따라 Digest가 바뀔 수 있으므로 문자열 동일성을 가정하지 않는다. Recovery Pull은 로컬 Harbor 인증/CA로 수행하며 AWS/CI Credential을 재사용하지 않는다. 필요한 도구·Image·CA·Secret 복호화 재료는 복구 전부터 사용할 수 있어야 한다.

### 3-F.17. GitOps 구조·Release·Sync·Offline 배포 — B04

#### 3-F.17.1 제안 Tree와 관리 책임

| GitOps 경로 | 내용 | 적용 방식 |
|---|---|---|
| `apps/game/base/` | FE/BE Deployment·Service·공통 Probe/정상 종료·공통 정책 | 직접 배포 대상이 아니라 Overlay 입력 |
| `apps/game/overlays/cloud/` | ROSA Route·ECR Digest·Cloud ConfigMap/Secret 참조·Replica/배치 | Cloud App Application이 관리 |
| `apps/game/overlays/recovery/` | Harbor Digest·로컬 진입/DB/Redis·새 Runtime·Replica/배치 | 사전에 Render/보존 후 격리된 로컬 복구에 적용 |
| `platform/cloud/` | Project·공통 접근/NetworkPolicy·User Workload Monitoring 설정·팀 RBAC | Platform Application, 변경 검토 후 수동 Sync |
| `clusters/cloud/` | Root/Application·AppProject·Repository/Path 연결·초기 Sync 상태 | Ansible은 Root 최초 등록까지만, 이후 GitOps |
| `releases/` | 값 없는 Release ID·App Commit·Image Mapping·Schema/설정/Secret 개정·Backup 연결 | 실제 ARN/평문 Secret/Backup 원본 제외 |

초기 구현에서 ApplicationSet을 추가하지 않고 Root와 명시적 Application으로 시작한다. Argo CD 인증은 승인된 OpenShift 사용자/RBAC와 연결하고 AppProject는 Repo·대상 Namespace·Resource 종류를 제한한다. Platform이 필요한 Cluster 범위와 App의 Namespace 범위를 구분한다. 실제 Repository Credential은 기존 별도 Secret 공급 경로로 제공하며 Operator 생성 Secret을 덮어쓰지 않는다.

#### 3-F.17.2 Sync와 변경 절차

최초 Root 등록 시 App은 자동 Sync를 비활성화한다. Namespace/플랫폼→비밀값 공급→DB/Redis TLS·Runtime Pull·Route/설정 확인→App 최초 수동 Sync·핵심 기능 확인의 순서로 진행한다. 그 다음 App의 자동 Sync·SelfHeal을 선언으로 켠다. Bootstrap이 지속 Manifest를 덮어쓰지 않는다. Root/Platform Application의 자동 Sync는 초기 기본안에서 끈다.

CI는 Source/Test 성공 후 Image를 Build하고, 유지한 Jenkins에서 상위 02가 정한 Image Scan을 수행해 결과를 해당 Image/Digest·도구/규칙 개정과 연결한 뒤 ECR Push·Release 검증 결과를 기록한다. 추가 자료 대조에서 App 사전시험 Commit의 `Jenkinsfile.image-pipeline`에 Trivy Scan·승격 차단·결과 Metadata 코드가 존재함을 읽기 전용 조회로 확인했다(§3-I.13.2). 코드 존재와 실제 Jenkins 설치·실행 성공/2차 재사용 가능성은 구분한다. 실제 Scan 도구·기존 정책·실패/예외 처리는 Source Preflight에서 확인하며 임의의 취약점 수치 기준을 추가하지 않는다. Scan 미실행/실패를 성공으로 기록하거나 검증 결과 없이 승인 Release 준비 완료로 처리하지 않는다. 이는 `02_TARGET_ARCHITECTURE.md` §11.1·26.7의 기존 Build/Test/Scan 요구를 연결한 것이며 새 Scan 제품 도입이 아니다. GitOps PR에는 Image Digest와 연결된 설정/Schema/Secret 개정·검증 결과·복구 Image 준비 상태를 기록한다. 지정 리뷰어가 확인한 Commit만 배포 Branch에 Merge하고 GitOps가 반영한다. Jenkins가 Cloud App를 직접 `oc apply`하거나 TF Apply를 하지 않는다.

App 자동 Prune는 초기에는 끈다. 제거 Resource가 남으면 OutOfSync/잔존 상태를 확인하고 삭제 대상을 검토해 수동 제거한다. Namespace·프로젝트 Secret·영속 데이터는 이 경로로 무심코 삭제하지 않는다. SelfHeal이 수동 수정과 충돌하므로 긴급 App 변경은 Sync 보류·원인/변경 기록·Git 반영·재개를 함께 수행한다.

Release 되돌리기는 호환되는 GitOps Commit/정확한 Digest/설정 조합을 다시 적용한다. Argo History Rollback만으로 자동 Sync가 이전 상태를 계속 유지하거나 DB Schema/쓰기 결과까지 되돌아간다고 설명하지 않는다. 파괴적 Schema 변경은 3-D의 Data 판단과 Backup/재개 Gate를 거친다.

#### 3-F.17.3 Offline Recovery의 제한된 실행 예외

GitOps Recovery Overlay에서 검토한 Manifest를 장애 전에 Render해 Release Bundle에 보존한다. 복구 시 GitHub/Argo가 Git을 새로 읽어야만 시작되는 구조를 피하기 위해, **로컬 복구 Namespace에 한해 Ansible의 명시적 Apply 진입점**으로 이 보존본을 적용하는 안이다. 이는 B04로 승인된 로컬 복구의 Owner 예외이며 Cloud App의 상시 CD Owner를 바꾸는 승인이 아니다.

로컬 Namespace·배포 Resource는 이 경로만 관리하고 같은 Resource를 실행 중인 Argo가 동시에 관리하지 않게 한다. 사전 확인된 Secret·DB 복원·새 Redis·Harbor Image/CA 준비 후 Apply하며 신규 Cloud 접속 없이 로그인/게임을 확인한다. 새 DB를 기존 DB에 덮어쓰지 않고 장애 전 Cloud Runtime 상태가 살아났다고 표현하지 않는다. 복구 Host 안내와 Client 재접속도 실제 복구 시간에 포함한다.

### 3-F.18. Worker·Replica·배치·자원·Pool — B05

#### 3-F.18.1 초기 후보

| 항목 | Cloud 후보 | Recovery 후보 / 확인 조건 |
|---|---|---|
| Worker | 3개, 서울 Region의 선택 AZ마다 1개, `m5.xlarge` 초기 후보 | 기존 로컬 Cluster의 실제 Node/자원 확인. 같은 사양이라고 가정하지 않음 |
| FE / BE | 각 3 Replica | 초기 각 1 Replica. DB 복원·새 Redis·기본 기능 검증부터 수행 |
| Rolling Update | `maxUnavailable:0`, `maxSurge:1` | 필요한 일시 Pod·연결 여유를 실제 계산 |
| PDB | FE/BE 각각 `minAvailable:2` 후보 | 1 Replica에 Cloud 값을 복사하지 않음 |
| 분산 배치 | AZ별 `maxSkew:1`, `whenUnsatisfiable:ScheduleAnyway`; Host 분산은 Preferred 조건 | 정상 3 AZ 분산 여부를 결과로 확인. AZ/Node 상실 시 살아 있는 Node 재배치를 막는 강제 조건을 기본으로 두지 않음 |
| Autoscaling | 초기 Worker/App HPA 자동 확장 보류 | 고정 구성을 먼저 측정. 자동 확장으로 비용·Pool을 예상 밖으로 늘리지 않음 |

Classic Multi-AZ 최소 EC2 구성은 Control Plane 3+Infrastructure 3+Worker 3으로 총 9개다 [3-F-R12]. `m5.xlarge`는 Worker 후보이며 나머지 Node의 실제 서비스 지정 사양/EBS를 Worker와 동일하게 가정하지 않는다. 전체 가동비에는 9개 Node·ROSA 서비스·Load Balancer·NAT 등을 포함한다. Worker 3개의 가격만으로 $500 충족을 판단하지 않는다.

AZ 분산은 정상 상태의 배치 목표이며 PDB는 자발적 Eviction의 제한이다 [3-F-R14]·[3-F-R15]. PDB가 Node/AZ 강제 장애·Rolling Update의 모든 중단을 막거나 WebSocket 연결을 이동시키지 않는다. 강제 분산 조건을 선택하는 대안은 재배치 불가/추가 Worker 비용과 함께 판단한다.

#### 3-F.18.2 다중 Pod 준비와 설정값

BE의 실제 프로세스 수·Session·Room Runtime·Pub/Sub·Connection Generation·업무 중복 처리가 3-E 기준을 충족해야 3 Replica로 동작시킨다. Pod 메모리에만 중요한 상태가 있으면 Replica를 늘려도 완료가 아니며 수정 범위를 3-H의 App 트랙에 기록한다.

초기 Requests/Limits·Startup/Readiness/Termination 시간·DB Pool의 정확한 숫자는 기존 Source 시작 조건과 짧은 실측을 보고 입력한다. 프레임워크·프로세스 수·DB 연결 한도를 모르는 상태에서 숫자를 확정하지 않는다. Source 확인→1 Replica 기동 측정→3 Replica/Surge 합계 계산→Node/DB 여유 확인→부하 시험을 동일 작업 묶음에서 수행하고 튜닝마다 사용자 재승인을 받지 않는다. 합계를 만족할 수 없어 DB/Worker 확대나 Replica 축소가 필요하면 Cost/가용성 영향을 제안한다.

최악의 연결 수는 `동시 Pod 수 × Pod당 프로세스 수 × (프로세스별 Pool + Overflow) + Backup/Migration/관리/검증 연결`로 계산한다. Rolling Surge뿐 아니라 종료 중인 이전 Pod가 아직 보유한 프로세스/DB 연결/CPU·RAM과 FE/BE 동시 배포를 포함하고 실제 DB `max_connections` 아래에 관리/복구용 여유를 둔다. Replica 3+Surge 1을 동시 자원 사용 최대 4 Pod분으로 단정하지 않는다 [3-F-R17]. DB Connection을 Replica 수만큼 나누는 것으로 끝내지 않는다. Redis는 Primary의 사용 메모리·Client 수·noeviction 실패를 실제 측정하고 Replica 메모리를 사용 가능한 총 메모리로 더하지 않는다.

### 3-F.19. 자동화 진입점과 종료 조건

| 진입점 제안 | 전제 | 종료 조건 / 실패 처리 |
|---|---|---|
| `tf-preflight` / `tf-plan` | B01 버전·B02 Caller·Root·입력 개정 | fmt/validate·검토용 보호 Plan. 불일치 시 Apply 진입 금지 |
| `export-inputs` | Owner 권한·완료된 기반 변경 | 허용 값만 보호 파일에 추출·대상 조회 확인. 오래된 입력은 재생성 |
| `gitops-bootstrap` | 실제 Cluster Ready·Context·설치 권한 | Operator/Root 등록까지. App는 준비 전 비활성화 |
| `secret-bootstrap` | 기존 SOPS+age 보호 자료·scope별 공급 | 참조/개정/연결만 확인. 로그의 값 노출·전체 Key 공유 금지 |
| `release-recovery-bundle` | 승인 Release·성공 Backup·Harbor Mapping | Rendered Manifest·Tool/CA·암호화 설정·Backup Hash/복호화 재료 준비 확인 |
| `backup-transfer-verify` | 3-D의 DB TLS·분리된 S3 인증 | 완성본만 S3/On-Prem으로 검증·완료 시각 기록. 실패 시 이전 검증본 보호 |
| `recovery-restore-apply` | 독립 Namespace/DB·Cloud 외부 조회 차단 | DB 복원→새 Redis→Secret→보존 Manifest→기본 기능/데이터 검증. 실패 자료 보존 |
| `window-close` | Window 결과·Backup/Bundle·삭제 범위 확인 | rosa 삭제와 부속 자원 정리 검증·잔여 과금 기록. foundation 전체 Destroy 실행 안 함 |

이 이름은 구현할 실행 기능의 작업 이름이며 현재 생성된 Script/Playbook 파일이 아니다. 각 진입점은 사전 확인·명시적 대상·재실행 시 안전성·실패 시 중단 지점·민감값 없는 결과를 갖춘다. Scheduler/Job은 현재 후보의 운영 중15분 Backup을 구현하되 동시 실행을 차단하고 jitter/중복 실행 생략/실패를 기록하며 부분 파일을 최신 복구본으로 지정하지 않는다. 실제 성공 Data 간격＋로컬 확보 지연＋시점 불확실성≤30분은 별도 관측/판정한다. 현재 Fixture Source는 운영 Timer 구현 완료가 아니다.

병렬로 가능한 것은 서로 다른 Repo/영역의 코드 작성·검토·로컬 Render/Test·문서 준비다. 실제 State 쓰기, 공유 Cluster의 Root/권한 변경, Cutover, Data Restore, 삭제/정리는 대상별 단일 실행 주체와 인계 순서로 진행한다. 동시에 작성할 수 있다는 이유로 동일 자원에 여러 Owner가 Apply하지 않는다.

### 3-F.20. 변경 영향 추적·승인 후 일괄 작업

| 변경 원인 | 직접 영향 | 후속 영향 / 함께 확인할 문서 |
|---|---|---|
| B01 버전/지원 조합 | Provider Schema·Role/OIDC·Bootstrap·Argo 기능 | Network/Data Lifecycle·Clean Recreate·Tool Bundle·시험/가동 시간 — 3-B~3-H |
| B02 암호화/인증/Key | State 접근·세션·Plan·복구 | Bootstrap 최초 실행·권한 실패 시험 — 3-C·3-F·3-G |
| B03 Worker Pull Role | 추가 Pull 정책·공유 Role 영향·Node 인증 | 계정표·ECR/Harbor·새 Node/12시간 경과/재생성 시험 — 3-C·3-F~3-H |
| B04 Sync/Prune/Offline | Owner·Namespace·Secret·Release/Schema | 삭제 보호·Host/설정·Bundle·Offline 시험 — 3-C~3-H |
| B05 Replica/Process/Pool | CPU/RAM·DB 연결·Redis Client·Rolling | DB 크기·재접속·가용성·Node 비용·부하 시험 — 3-D~3-H |
| B06 수치 목표/시험 범위 | 부하·장애·복구 시간·증거 | Window 길이·도구·비용·발표 주장 — 3-E·3-G·3-H |
| B07 작업/Window/예산 | 의존 작업 인계·실행 시점·가동시간 | Seed/Backup 최신성·실패 재시험·Freeze·Cost — 3-A~3-H |

변경 기록은 `ID / 기존 값 / 변경 값 / 이유 / 승인 상태 / 직접 의존 / 영향 문서·시험 / 재검증 / 미해결`을 포함한다. 시작 시 위 표의 영향 항목을 찾고 끝나면 문서·시험·Cost에 반영됐는지 확인한다. 관련 없는 승인까지 매번 다시 받지 않는다.

3-A~3-H의 인계/상호참조·구현 입력·Runbook·시험/WBS 대조와 단일 검토 체크리스트는 3-I 통합 검토 절에 작성했다. B01~B07 작업 전제의 승인 상태와 영향받는 인계를 일괄 반영했다. 현재는 전체03·지침 최종 컨펌 후 실제 구현 준비 단계다. 해당 승인 상태와 팀원 자료의 구현 인계를 §3-I.12.4·§3-I.13에 정리했다. 새 선택이 없는데 다시 작은 승인 단계를 만들지 않는다. 전체 검토에서 수정된 선택의 연쇄 영향도 같은 표로 추적한다.

### 3-F.21. 공식 참고 자료와 검증 범위

- **[3-F-R1]** [HashiCorp S3 Backend·State/Lock·인증정보](https://developer.hashicorp.com/terraform/language/backend/s3)
- **[3-F-R2]** [HashiCorp Remote State와 값 공유 대안](https://developer.hashicorp.com/terraform/language/state/remote-state-data)
- **[3-F-R3]** [Red Hat OpenShift GitOps Operator 설치](https://docs.redhat.com/en/documentation/red_hat_openshift_gitops/1.18/pdf/installing_gitops/Red_Hat_OpenShift_GitOps-1.18-Installing_GitOps-en-US.pdf)
- **[3-F-R4]** [Argo CD 자동 Sync·Prune·ApplicationSet](https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/)
- **[3-F-R5]** [HashiCorp Plan 파일의 민감값](https://developer.hashicorp.com/terraform/cli/commands/plan)

2026-10-01 공식 기능 설명과 승인 문서를 대조했다. GitOps 1.18 문서는 설치 기능을 확인한 자료이며 프로젝트 채택 버전이 아니다. 후속 후보와 실제 ROSA 지원 버전·설치 Namespace/권한·Argo 기능을 §3-F.14~19의 적용 전 조건으로 대조한다. State Bucket 수·Root/Key·제한된 입력 파일·Ansible 설치 진입점은 승인된 작업 전제다. §3-F.13의 B01~B07은 2026-10-01 작업 전제로 승인되었고 실제 지원·구현·시험 확인 조건을 유지한다. AWS/ROSA/Controller 접속·Provider 동작·Plan·적용·비용·성능·복구는 아직 검증하지 않았다.


- **[3-F-R6]** [Terraform 1.16.4 공식 배포](https://releases.hashicorp.com/terraform/1.16.4/)
- **[3-F-R7]** [AWS Provider 공식 Release](https://github.com/hashicorp/terraform-provider-aws/releases)
- **[3-F-R8]** [RHCS 공식 Registry / Machine Pool](https://registry.terraform.io/providers/terraform-redhat/rhcs/latest/docs/guides/machine-pool)
- **[3-F-R9]** [OpenShift GitOps 1.21 지원 조합·1.21.4 Release](https://docs.redhat.com/en/documentation/red_hat_openshift_gitops/1.21/html/release_notes/gitops-release-notes)
- **[3-F-R10]** [S3 SSE-S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html)
- **[3-F-R11]** [Red Hat ROSA/ECR Node·Pod 인증 구분](https://access.redhat.com/solutions/7008603) — Unverified 표기·2024 자료, 실제 선택 Classic 조합 검증 필요
- **[3-F-R12]** [AWS ROSA Classic/HCP 구조·정책·최소 Node](https://docs.aws.amazon.com/rosa/latest/userguide/rosa-architecture-models.html)
- **[3-F-R13]** [AWS ROSAWorkerInstancePolicy 공개 정책](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ROSAWorkerInstancePolicy.html) — 실제 Classic 정책을 대신하는 근거 아님
- **[3-F-R14]** [Kubernetes Topology Spread](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/)
- **[3-F-R15]** [Kubernetes PDB](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)
- **[3-F-R16]** [AWS ECR Registry 인증·Token 수명](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html)
- **[3-F-R18]** [HashiCorp SG 본체와 별도 Rule의 혼용 주의사항](https://github.com/hashicorp/terraform-provider-aws/blob/main/website/docs/r/security_group.html.markdown) — 현재 공식 설명, 선택 Provider의 Schema/Plan/동작은 별도 확인
- **[3-F-R17]** [Kubernetes Deployment Rolling 중 종료 Pod의 자원 사용](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) — 신규 terminatingReplicas 필드 채택 아님
- **[3-F-R19]** [Argo CD Application 삭제·finalizer·연쇄 삭제](https://argo-cd.readthedocs.io/en/stable/user-guide/app_deletion/) — 자동 Prune 설정과 별개. 선택 GitOps/Argo 버전의 실제 삭제 동작은 구현 시 확인

공식 최신 문서의 기능 설명을 선택 OpenShift/Kubernetes 버전에도 그대로 지원한다고 가정하지 않는다. 버전별 Schema와 지원값을 확인한다. 문서 조사와 실제 동작 증거는 구분하며 공식 문서도 후보 전체의 검증 성공을 증명하지 않는다.

### 3-F 남은 입력과 실행

- [x] B01~B07 작업 전제 승인·관련 항목 반영
- [ ] 실제 Source·Account·Classic 지원 버전/Role·Controller·주소·Credential 참조 확인
- [x] B01~B07 승인 상태·Runbook·시험·WBS·Cost의 연결 반영
- [x] 전체03 최종 컨펌 후 최종 문서 상태·준비 인계 정리
- [x] 03 전체 통합 검토·사용자 최종 컨펌 반영
- [ ] 실제 코드·Validate/Plan·Cost Gate·실행 승인·Apply·Clean Recreate·복구·업무 시험

## 3-G 시험과 Evidence

### 3-G.1. 설계와 실제 결과의 경계

지정 Commit의 일부 Source와 Repository 정보는 읽기 전용으로 조회했다(§3-I.13). 최신 전체 Source 조사와 최종 Seed 확인은 아직 완료하지 않았으며, AI가 실제 ROSA/AWS/DB Runtime을 직접 조회하거나 구축·시험한 것은 아니다. 아래 T 시험의 프로젝트 최종 검증 결과는 모두 **NOT RUN**으로 유지한다. 팀원의 demo2 사전검증 보고는 §3-I.13에서 해당 환경·조건·증거 범위로 별도 관리하며, ROSA 최종 시험의 PASS로 확대하지 않는다. 문서 작성이나 Source 조회만으로 구현·검증·PASS가 되지 않는다. 버전 지원·권한·환경값·Schema·실제 기능·데이터·비용의 미확인 입력은 3-F·3-H의 적용 전 Gate로 연결한다.

기존 3-B~3-F 시험을 폐기하고 새 번호로 덮어쓰지 않는다. 아래 T 번호는 통합 실행 묶음이며 개별 IF/IM/Data 시험의 결과를 연결한다. 기존 승인 요구는 유지하고 수치 목표와 실행 묶음은 B06의 승인된 프로젝트 시험 기준으로 구분한다. 목표 승인과 실제 측정·시험 성공은 별개다. 시험 진행 중 중요 실패가 있으면 증거·원인·영향 범위를 남기며 기준을 나중에 조용히 낮추지 않는다.

### 3-G.2. B06 승인된 시험 기준과 판정 규칙

**승인된 작업 전제:** 기능·보안·재현·장애·Offline 복구를 Must 묶음으로, 부하/복구 수치를 프로젝트 Acceptance 목표로 정한다. 실제 수치 목표는 운영 SLA나 제품 보장이 아니다.

| 판정 | 의미 | 후속 처리 |
|---|---|---|
| NOT RUN | 아직 실행하지 않았거나 필수 전제가 없음 | 완료/PASS로 표시하지 않음 |
| PASS | 정한 조건에서 Acceptance를 만족하고 추적 가능한 Evidence가 있음 | 환경·범위·제한을 함께 기록 |
| PARTIAL | 일부만 수행/충족. 누락·목표 미달·환경 차이가 있음 | 누락과 재시험 범위를 명시. 전체 Must 완료로 대체하지 않음 |
| FAIL | 기준 미달·보안/업무 불일치·복구 실패 | 원인·영향·조치·재시험 연결 |
| N/A | 실제 Architecture에서 해당 세부 시험이 적용되지 않음 | 이유·대체 검증 기록. 성공축 자체를 조용히 제외하지 않음 |

설치·정상 접속만으로 HA/DR/재현성 PASS를 주지 않는다. 수치만 좋고 인증·중복·데이터 일관성이 실패한 결과도 PASS가 아니다. Must 누락/실패는 최종 검토에서 해결 또는 명시적 범위 재결정이 필요하다.

### 3-G.3. Charter 12개 성공축과 Evidence 대응

| 성공축 | Acceptance | 실행 묶음 / Evidence |
|---|---|---|
| Migration Decision | 실제 구성별 유지/이전/대체/종료·이유·Owner가 모순 없이 연결됨 | T01 / Migration Matrix·Seed·최종 Resource 표 |
| Hybrid Connectivity | VPN/DataVM의 필수 경로·DB/Redis TLS·S3 경로, 정상 Cloud의 On-Prem 비의존이 확인됨 | T04·T14 / Route/SG·TLS 결과·차단 전후 기능 |
| Infrastructure Reproducibility | 3 State 경계·Secret·GitOps·실제 기능을 포함한 Terraform Clean Recreate 성공 | T02·T03·T19 / Plan/실행 Metadata·재생성 결과 |
| Application Migration | 1차 대표 End-to-End 흐름·Data 이관·새 Runtime 초기화 정상 | T05·T06 / Source 기반 시나리오·데이터 비교 |
| Availability / Failure | Pod/Worker·RDS·Redis의 선택된 장애 영향·업무 안전·복구를 실제 확인 | T10~T13 / 시간선·상태·Metric/Log |
| Recovery / DR | 사전 On-Prem 자료만으로 독립 DB/새 Redis/App 복구·RTO/RPO 측정 | T17·T18 / Bundle/Backup Hash·복원 비교·시간선 |
| Observability | 장애 현상→Metric/Log/Alert→판단이 동일 시험 ID로 연결됨 | T15 / Native/UWM·RDS/Redis Metric·상관 ID |
| Performance | 의미 있는 HTTP/WS 경로의 부하·Latency·오류·자원 병목 정량 기록 | T16 / Harness·Raw 결과·Baseline/Target/Actual |
| Cost | 전체 서비스/잔존 자원 예상·실제 비용과 $500 한도 확인 | T20 / 3-H Cost Ledger·가동/삭제·청구 관측 시각 |
| Security | 사람/실행/CI/Pull 경계·TLS·Secret 노출·사용자 권한 검증 | T03·T04·T07·T08·T21 / 민감값 없는 결과 |
| Platform Value | 1차 대비 배포·책임·Probe/관측 등 실제 차이를 근거로 설명 | T22 / 동일 흐름 비교·운영책임 변화·제한 |
| Documentation / Presentation | 결정·Troubleshooting·실측·Runbook·Demo가 Release/시험 ID로 추적됨 | T23 / Evidence Index·최종 체크·시연 영상 |

### 3-G.4. 통합 시험 Matrix — 현재 전부 NOT RUN

| ID | 시나리오 / 의존 | 핵심 확인·Acceptance | 연계 |
|---|---|---|---|
| T01 | 설계·소유권·Source 대조 | 1차 원본 보존, 2차 Seed 실제 SHA, 네 Repo/Owner, 미확인값·신규 선택 구분 | 3-A·3-D·3-F |
| T02 | 최초 Bootstrap→Remote 이전→Role 재실행 | 자원 재생성 없이 State 이전, 정확한 Key/Caller, 오래된 입력·다른 Account/Region 입력 차단, 정상 Role 재실행·Lock 충돌/실패 해제 절차 | 3-F IM-01~04 |
| T03 | 계정/Secret·State·Plan·플랫폼 접근 보호 | MFA/Caller·목적별 Role/Key 접근·무관 작업 거부, 개인 Admin의 경계 설명, IDP 신규/기존 Session·RBAC·Argo 권한, CI/Backup 권한·SOPS+age 공급/교체·출력 노출 검사. 세부 Case는 아래 대응표 | §3-C.9·13 / 3-F IM-06·09 |
| T04 | Network·TLS·접근 실패 | 허용 Source 성공·미허용 차단, DB/Redis CA/Hostname 검증, 잘못된 CA/암호 실패, S3 HTTPS 경로 분리 | 3-B·3-D |
| T05 | Seed 이관·기본 Data 검증 | 격리 DB import, 핵심 Row 수/관계/대표 업무 비교, Schema/권한, 새 Redis, 기존 DB 보존 | 3-D |
| T06 | 대표 E2E | Source 확인 후 로그인/Guest 해당 방식, 입장·관전·투표·턴/게임 종료·전적 등 실제 제공 기능, SPA 새로고침, 없는 API/WS 경로가 HTML 200으로 숨지 않는지 검증 | 3-E IF-01~02 |
| T07 | 사용자 인증/권한/만료 | 다른 Room·다른 User 접근, 만료·로그아웃·권한 제거 후 HTTP/WSS 차단. 실제 Cookie/Token 방식, HTTP→HTTPS·허용 Origin·신뢰 Proxy Header 기준 확인 | 3-E IF-03·09~10 |
| T08 | 중복·동시 쓰기·결과 불명 | 같은 요청 재전송·다른 Pod 경쟁·DB 응답 직전 단절. 업무 효과 중복 0건, 확정 결과 조회·무조건 재쓰기 방지 | 3-E IF-13~15 |
| T09 | WS 재접속·Generation·Snapshot | 다른 Pod 재접속·역순/누락 이벤트·이전 연결 종료. 현재 상태 수렴·오래된 Callback의 새 연결 삭제 방지, 유휴/긴 게임 대기·Heartbeat/Timeout·종료 원인 확인 | 3-E IF-07·11~12 |
| T10 | Rolling·Pod 종료/강제 삭제 | 신규 업무 차단·진행 요청 결과·Graceful 종료와 강제 종료 차이, 재접속·중복 방지, 정확한 Digest/개정 | 3-E IF-06 / §3-F.18 |
| T11 | Worker 1대 장애 | 정상 AZ 분산·Pod 재배치·수용 자원·업무 영향 측정. PDB에 의한 자발적 Eviction과 강제 장애 구분 | 3-F B05 |
| T12 | RDS Multi-AZ DB Instance Failover | 별도 Reader가 아닌 Endpoint 재연결, Pool/Timeout, DB 확정/불명 결과 구분, 핵심 데이터 일관성 | 3-D·3-E IF-04·14~15 |
| T13 | Redis Failover·메모리/접근 오류 | Primary Endpoint 재연결·유실 가능 Runtime 검증·noeviction 오류·게임 중단/재개 범위. DB 확정 결과 보존 | 3-D·3-E IF-04~05·15~17 |
| T14 | WireGuard/On-Prem Jenkins 단절·Gateway 복구 | Cloud 사용자 기능·캐시 없는 신규 Pull 유지, 실패한 Backup/CI 분리. Gateway 서비스/종단점 재구축·Source 보존·금지 통신·지속 설정은 아래 세부 Case | §3-B.9.8~9.9 / 3-D / 3-F B03 |
| T15 | 관측·알림·판단 | 실제 장애와 Cloud Native/UWM·DB/Redis Metric/Log의 시각·ID 대응. 알림 조건·확인 지연, 지원되는 Control Plane/Worker 상태·Cluster Operator/API·Log 진단 결과와 관리책임 경계 기록 | 02·3-E·3-H |
| T16 | 정상 부하·추가 부하 | §3-G.6의 HTTP/WS 목표·업무 정확성·자원/Pool/Redis/수집기 병목·비용을 함께 기록 | 3-D~3-H |
| T17 | Backup 생성·S3/On-Prem 검증·실패 | 완성본 Hash·복호화·실제 import, 부분 파일/전송 실패 시 이전 검증본 보존, 최신 검증 시각·수명 | 3-D·§3-F.19 |
| T18 | Offline Restore-based Recovery | AWS/GitHub 신규 조회 없이 Harbor/보존 도구·Bundle·DB/새 Redis/App 복구·업무/Data 확인, §3-G.7 측정 | 3-C~3-F / 3-E IF-08·18 / 3-F IM-08 |
| T19 | rosa 삭제→Terraform Clean Recreate | foundation 재실행 시 Binding 유지, Cluster 삭제 전 rosa Binding 해제, 기반 Rule/Data/Network·Backend 보존, 새 Worker SG 재연결·양쪽 정상 Plan, Cluster별 Role/OIDC·새 Host/Secret·GitOps·Pull·E2E | §3-B.9.7 / 3-F IM-03·05~07 / 3-E IF-08 |
| T20 | Window 종료·잔존 자원·Cost | ROSA 부속 자원/과금 종료 확인, Data/NAT/IPv4/EBS/Backup 잔존·RDS 자동 재시작까지 Ledger에 반영 | 3-B·3-D·3-H |
| T21 | CI Build/Test/Scan·Push vs Runtime Pull·Release 보존 | Source/Test·Image Scan과 Image/Digest·도구/규칙 개정·실패/예외 결과 연결, 제한된 Repo Push/Pull 구분, 캐시 없는 새 Worker·12시간 이상 지속 사용 후 새 Pull·재생성 후 Pull, Harbor Digest/CA·No CI Token 복사 | 3-C·3-F B03 |
| T22 | 1차/2차 운영책임·Platform 비교 | 같은 대표 기능에서 배포/복구/관측·담당 책임·운영 부담·비용 차이. 1차 Self-managed와 ROSA의 지원되는 Control Plane/Worker 진단·관리책임 차이 포함. 조건 다르면 직접 성능 개선 주장 안 함 | 01·02·3-A |
| T23 | 재현 문서·시연·Evidence 완결 | 결정→Code/Release→Test→실측→해석·제한→영상 추적. Credential/개인정보 제거·실패 결과 포함 | 3-A~3-H |

각 묶음은 필요한 세부 Case를 Source 확인 후 생성한다. Case 수를 목표로 늘리거나 제외하지 않는다. IF-01~18 및 IM-01~09 각각의 완료 여부를 실행 Ledger에서 연결하고 T 묶음 PASS만으로 하위 실패를 숨기지 않는다.

#### 3-G.4.1 기존 계정·Network 요구의 세부 대응

아래 항목은 3-B·3-C의 기존 요구를 T 묶음에 연결한다. 구현 입력과 실제 지원을 확인한 뒤 개별 Case 결과를 기록하며, 묶음 이름 하나로 생략하지 않는다.

| T 묶음 / 원본 요구 | 반드시 구분할 확인 |
|---|---|
| T03 / §3-C.9 Human·TF·CI·Backup | 개인 MFA/Caller, 세 목적 Role의 필요 작업/무관 State 거부, CI 지정 Repo Push/무관 Repo·권한 변경 거부, Backup 지정 Prefix/무관 State 거부. 개인 Admin 직접 호출까지 격리된다는 주장은 하지 않음 |
| T03 / §3-C.9 IDP·RBAC·회수 / §3-F.17 Argo | 승인 구성원 신규 Login·미승인 사용자 거부, 실제 Subject/Binding 및 허용·금지 요청, 다른 높은 권한·Secret 간접 경로, 구성원/권한 제거 후 신규 Login과 기존 Session/Token 각각 재시험. GitHub Team 제외만으로 기존 Session 즉시 폐기를 가정하지 않음. App T07과 구분 |
| T03 / §3-C.9 비상·Secret / 3-F IM-06·09 | 정상 IDP 장애 시 승인된 제한 관리 경로, scope별 Key/교체·옛 인증 거부, 필요한 Secret 공급 전 Sync 보류·자동 Prune/수동 삭제·Application finalizer/연쇄 삭제·Namespace 경계, State/Plan/CI/Ansible 출력 보호. SSM 관리는 NET-10의 실제 지원 확인과 연결 |
| T04 / NET-01~04·06·08~10 | Public 사용자/API·Console/OAuth, 실제 Worker의 DB/Redis, 지정 On-Prem Job /32, Backup/CI와 ROSA Egress, SSM 관리 경로를 구분. Source·왕복 Route·SG·TLS/권한의 허용/거부를 기록. NET-07은 초기 비활성·미허용 상태 확인, 추가 활성화는 승인 범위 확인 후 시험 |
| T14 / NET-05 및 §3-B.9.8~9.9 | WG Service/설정 복원, AWS Gateway 재구축의 EIP Association·ENI Route Target·Source/Destination Check·Forwarding·재부팅 지속, On-Prem Gateway 재구축의 vRouter 왕복 Route/NAT 예외를 한 종단점씩 확인. 복구 후 Handshake와 실제 업무 Probe·원본 Source·미허용 Source/Port 차단을 함께 검사 |
| T14 / §3-B.9.8 조건별 복구 | 출구 IP/Port 변경·유휴 재연결, 통제된 Peer Key 교체 후 이전 Key 거부, 다른 AZ/새 ENI 복구를 수행한 경우 모든 관련 Route/정책 갱신. 미재현 시 미실행/제한으로 남기며 자동 AZ Failover나 AZ 장애 검증 성공으로 확대하지 않음 |
| T19 / §3-B.9.7·3-F IM-03 | foundation/rosa를 순서대로 재실행하여 Rule 덮어쓰기/영구 Diff가 없는지 확인. Cluster 삭제 전에 rosa Binding을 제거하고 기반 Rule/Data를 보존. 새 Cluster Worker SG로 다시 연결한 뒤 이전 SG 참조가 남지 않는지 확인 |

Gateway 복구 시간은 장애 인지·조치·업무 Probe 완료의 실제 시간선으로 남긴다. 현재 설계의 Offline 서비스 RTO10분을 Gateway MTTR 목표로 자동 대입하지 않는다. 위 장애/재구축을 W08에 추가로 숨겨 넣지 않고 소요·재시험·재생성·가동 비용을 사전에 3-H의 Window/Cost Ledger에 반영한다.

#### 3-G.4.2 플랫폼·CI 검증 경계와 기존 Should 처리

Charter의 Rollback 검증은 Should로 유지한다. T10의 선택 세부 Case에서 호환 GitOps Commit·정확한 Digest·설정 조합으로 되돌리기, 긴급 수정 시 Sync 보류→Git 반영→재개, 정상 업무/관측을 확인한다. DB Schema와 이미 확정된 쓰기 결과는 자동 복구된다고 주장하지 않는다. Must를 침해해 생략하면 이유·제한을 기록하며 T10의 필수 Rolling/종료 판정을 이 Should 수행 여부와 혼동하지 않는다.

T21의 12시간 이상 지속 사용 후 Pull은 §3-F.16.2의 동일 Node 인증 경로/캐시 없는 Image 조건을 따른다. 실제 발급/갱신 관측이 없으면 Token 만료/갱신 자체를 입증한 결과로 확대하지 않는다. 실제 Window 비용에 포함하며 미실행이면 별도로 남긴다.

`02_TARGET_ARCHITECTURE.md` §6.2·26.2의 Control Plane 진단 Evidence는 T15의 실제 상태/Operator/API/Log 수집과 T22의 1차/2차 책임 비교에 연결한다. 지원 범위·지정 관리 주체의 실제 권한·수집 시각/환경·판단과 제한을 기록하며, 민감 Raw 진단 자료는 §3-G.9에 따라 보호한다. Managed Control Plane EC2 강제 종료·etcd/OS 직접 변경을 이 요구의 기본 시험으로 추가하지 않는다. 실제 진단 경로를 실행하지 못하면 해당 세부 Case를 NOT RUN/PARTIAL로 남기며 App 관측 성공으로 대신하지 않는다.

T21은 `02_TARGET_ARCHITECTURE.md` §26.7의 기존 Jenkins Build/Test/Scan 수행 결과도 개별 Case로 확인한다. Scan 도구/정책·Image/Digest 연결·미실행/실패/예외 결과·Release 검토 기록을 구분하고, Push/Pull 성공만으로 Scan까지 PASS 처리하지 않는다. Charter §7.2의 추가 Image Vulnerability 확인은 Should로 유지한다. 기존 CI Scan의 수행/결과 추적과 추가 취약점 분석·새로운 차단 기준 도입을 구분하며, 특정 Severity의 0건 기준이나 새 Scan 제품을 자동으로 Must에 추가하지 않는다.

`02_TARGET_ARCHITECTURE.md` §9.3의 Warm DR과 Charter의 추가 Scaling/관측·Rollback 등 Should/Could는 Must와 구분한다. 기본 Offline Restore를 Warm DR/Continuous Replication 성공으로 확대하지 않으며 선택 수행/미수행 이유·제한을 기록한다. 추가 구현/시험은 남은 일정·예산·의존성이 허용하는 승인 범위에서만 수행한다.

T11은 Worker 1대 장애이지 Region/전체 AZ 장애 검증이 아니다. AZ 장애를 실제로 재현하지 않았다면 “Multi-AZ 구성과 Worker 장애 확인”까지만 주장한다. T12/T13도 실제 제품별 Failover 방식·강도·범위를 기록한다.

### 3-G.5. 시험 실행 순서와 병렬 범위

| 실행 묶음 | 선행 조건 | 함께 수행 가능한 준비 / 순차 실행 |
|---|---|---|
| 준비 | 전체03·지침 최종 컨펌 완료, 실제 입력·지원/가격·실행 조건 확인 대기 | Source/Case 작성, Overlay Render, Backup Restore 연습, 측정 Harness, Evidence Index 준비는 독립 병행 |
| Window A / 통합 | Cost Gate·버전/권한·생성·Data/Secret/Pull | T02~09·T15·T17·T21의 정상 경로. 통합 중 공유 자원의 장애 주입은 보류 |
| Window B / 검증 | 검증된 Release·사전 복구 자료·공유 자원 단일 실행자 | T19 재생성→정상 Baseline→T10~14의 필요한 세부 장애/복구 Case를 서로 분리해 순차 수행→T16 부하. Gateway 재구축·재시험 소요는 Window/Cost에 포함. T18은 격리된 로컬 복구 환경에서 진행 |
| 종료 / 증거 | 결과·Hash·측정·삭제 범위·복구본 보존 | T20·T22·T23. 누락/실패만 영향 범위에 맞춰 재시험 |

독립된 로컬 Restore와 시험 도구 검증은 병렬로 할 수 있다. 실제 DB/Redis 장애·Worker 삭제·Rolling·부하를 동시에 주입하지 않는다. 독립된 실험을 설계한 경우에만 복합 장애를 추가하고 그 결과를 단일 원인 시험과 구분한다.

재시험은 변경 영향 표를 따른다. 예를 들어 Pool 변경은 T08/T10/T12/T16, Pull Role 변경은 T14/T19/T21, Secret 공급 변경은 T03/T04/T06/T18/T19를 대조한다. 그대로인 영역의 모든 시험을 무조건 반복하지 않는다.

### 3-G.6. 승인된 Performance·재접속 수치 목표

#### 3-G.6.1 의미 있는 초기 부하

| 단계 | 승인된 사용자/연결 목표 | 승인된 측정 시간 | 목적 |
|---|---|---|---|
| Smoke | 동시 사용자 10명·실제 게임 참여자/관전자 구분 | Warm-up 후 5분 | Harness·인증·업무 상태·분산 Pod 기능 확인 |
| Baseline | 동시 사용자 30명·HTTP/WS 실제 비율 기록 | Warm-up 후 15분 | Target과 비교할 안정 상태 측정 |
| Target | 동시 사용자 60명·서버/Client의 실제 연결 수 기록 | Warm-up 후 30분 | 프로젝트 목표 부하와 병목 확인 |

규칙상 한 Room에 60명이 투표/참여할 수 있다고 가정하지 않는다. 실제 Room/게임 인원 제한에 맞춰 방을 나누고 사용자당 행동·Think Time·관전자 비율·메시지 크기·HTTP Request 수를 기록한다. Load Generator는 로컬/별도 실행 환경을 사용하고 CPU/네트워크 병목을 확인한다. Socket 개설만 반복하는 부하는 실제 게임 처리 성능으로 보고하지 않는다.

Source에 맞는 기존 HTTP/WS 시험 도구·Harness를 활용하고 정확한 도구 버전·Script Commit·난수 Seed·시작/종료를 보존한다. 특정 도구를 설치한 것 자체가 Performance 완료 조건은 아니다.

#### 3-G.6.2 승인된 프로젝트 Acceptance 목표

| Metric | 정상 Target 부하에서의 승인된 기준 | 측정 경계 |
|---|---|---|
| 대표 HTTP 업무 응답 p95 | 1초 이하 | 해당 Route/업무별, 성공 요청 Latency와 실패율 함께 기록. 전체 평균으로 느린 API를 가리지 않음 |
| WS 업무 결과 확인 p95 | 1초 이하 | 요청 ID의 권한/업무 확정 결과를 Client가 확인한 시점. 단순 Send 완료/Socket Ack와 구분 |
| 예기치 않은 업무 오류율 | 1% 미만 | 원래 정상 업무 시도 수를 분모로 첫 시도 오류율을 계산하고 재시도·최종 실패율을 별도 기록. 의도한 부정 권한 Case 제외. 재시도 성공이 최초 Timeout/실패를 감추지 않음 |
| 업무 정확성 | 시험에서 중복 업무 효과·권한 없는 성공·확정 데이터 불일치 0건 | 시도 수·경쟁·단절 위치를 함께 기록. 모든 상황의 영구 보장이 아님 |
| WS 재접속 후 상태 수렴 | 정상 의존 서비스가 가용해진 뒤 30초 이내 | 재인증·Room 권한·현재 상태 확인·Generation. 장애 시작 이후 시간도 별도 기록 |

장애 주입 구간의 오류·복구 시간을 정상 성능 결과에 섞거나 삭제하지 않고 별도 표시한다. Requests/Limits·Replica/Process·DB Pool·DB max_connections·Redis Client/메모리·Node CPU/Memory·수집 부하를 같이 기록한다. 목표 미달이면 Raw 결과·원인·튜닝 전후를 남기고 자원/비용 확대가 필요하면 B05/B07 영향으로 검토한다.

1차 환경과 버전·부하·데이터·네트워크가 다르면 조건 차이를 명시한다. Baseline이 실제로 없으면 미측정으로 두고 “몇 % 개선”을 만들어 내지 않는다.

### 3-G.7. 승인된 Recovery·Backup 정량 목표

**현재 설계 요구사항:** [§3-I.14.5](#recovery-design-decision-20261005)의 RTO 10분·영속 DB RPO 30분·DB 운영 중 Portable Backup 15분 계획 주기는 PR #30으로 채택·병합됐다. 이전 30분/90분/1시간과 철회된 10분/15분/5분 우선 권고는 결정 이력으로 보존한다. 아래 목표의 실제 전체 Recovery 달성·Acceptance는 미검증이다.

| 항목 | 현재 프로젝트 요구사항 / 정의 | 미달·제한 처리 |
|---|---|---|
| Offline Recovery RTO | **10분 이내**. 장애 주입/접속 불가 시작→탐지/복구 결정·DB 복원·새 Redis·App 배포·Host 안내·대표 업무/Data 확인 완료까지 | 부분 Fixture/Restore 명령 시간만 계산하지 않음. 자동 장애 전환이나 동일 접속 주소 유지로 표현하지 않음 |
| Offline Recovery RPO | **30분 이내**. 사고 시각과 실제 사용한 On-Prem 검증 Backup의 일관된 Data 기준 시각 간 차이 | 정상 성공 간격＋로컬 확보 지연＋시계/시점 불확실성≤30분의 실제 근거 필요. 신규 회원·완료 Game/Result/Rating 손실을 별도 기록 |
| Backup | DB 운영 중15분 계획 주기·7일 및 최종/마지막 검증본 보호는3-D 유지 | Timer 간격만으로 RPO30분 보장하지 않음. jitter/중복 실행 생략·Data 시각·S3/로컬 완료·실패/재전송·이전 사본 선택 기록 |
| 정상 Data 비교 | Schema·핵심 Row/관계·대표 결과·권한 정상 | 단순 import Exit Code·파일 Hash만으로 업무/Data 검증 완료 아님 |

일관된 Snapshot/Data 시각을 모르면 파일 수정 시각을 Data 기준으로 대신하지 않는다. 시험에는 확인 가능한 쓰기 Marker/업무 기록을 사용해 Backup과 복원 데이터의 경계를 확인한다. 후보 적용 후 실제 사용 사본의 RPO가30분을 넘어가면 차이/손실을 미달로 보고한다. 시점 불명확은 null/미판정으로 남기며 검증 Backup이 오래됐다고 목표를 자동 완화하거나 같은 Run의 기준을 낮춰 PASS로 바꾸지 않는다.

Local Bundle과 Harbor Image·도구·복호화 Key가 존재하는지 장애 전에 확인한다. 복구 시 AWS/GitHub 외부 조회를 차단/관찰하여 사전 보존본만 사용했음을 확인하되 로컬 DNS/Harbor/기존 플랫폼까지 끊어 다른 실험으로 만들지 않는다. Restore는 격리 DB/Namespace에서 수행한다. 기존 Cloud DB/로컬 원본을 덮어쓰지 않는다.

위 RPO는 Backup으로 복원되는 영속 DB 데이터의 시점 경계다. 진행 게임/Redis Runtime의 중단·손실은 별도 항목으로 기록한다. 새 Redis Runtime은 미완료 게임 상태의 완전 복구를 뜻하지 않는다. 3-D/3-E의 승인 기준에 따라 영향을 받는 게임을 중단/검증하고 DB에 확정된 전적/결과를 보존한다. RDS의 동기 Standby와 Redis의 비동기 Replica도 같은 RPO 보장으로 설명하지 않는다.

### 3-G.8. Observability와 장애 판단

기본 관측은 OpenShift Native Monitoring+User Workload Monitoring, 기존 App 구조화 Log, RDS/ElastiCache의 AWS Metric을 사용한다. 새로운 중앙 Log 제품/외부 APM은 기본안에 추가하지 않는다. 실제 필요한 Metric 이름/Exporter·Driver·대시보드는 Source와 선택 버전을 확인해 연결한다.

| 신호 | 필요한 관찰 | 이어지는 판단 |
|---|---|---|
| App 오류/지연 | Route/업무별 Count·Latency·요청 ID·Replica/Restart·Readiness | 코드/인증/의존 실패와 과부하 구분 |
| WS | 연결/재접속·비정상 종료·Snapshot 실패·Generation | 연결만 살아 있고 업무 결과가 안 오는 경우 식별 |
| DB | Connection·CPU/Memory·지연·Failover·Timeout/확정 불명 | Pool 여유·Endpoint 재연결·결과 조회·쓰기 중단 범위 |
| Redis | Used Memory·Client·Eviction/쓰기 오류·Primary/Failover | noeviction 보호·Runtime 불일치·게임 재개 Gate |
| Backup/복구 | 사용 가능한 마지막 로컬 Backup의 Data 기준 시각/나이·성공 사본 간격·전송/검증 지연·jitter/실패·Bundle 준비 | RPO30분 후보 초과 전 실제 대응 여유를 둔 경고·재시도, 초과/시점 미확인은 미달/미판정 기록. 알림 수신을 목표 달성으로 대체하지 않음 |
| Node/배포 | CPU/Memory·Pending·AZ 배치·Rolling/Surge·ImagePullBackOff | 자원 여유·배치 제약·권한/네트워크 원인 |

알림의 조건·발생/확인 시각·담당의 조치를 기록한다. 단순 Alert Rule 존재가 아니라 시험에서 실제 판단에 도움이 됐는지 확인한다. Request/Session/Secret 값을 그대로 Metric Label이나 공개 Log에 넣지 않는다.

### 3-G.9. Evidence 형식과 보관 경계

Docs에는 정리된 결과와 재현 가능한 Script/Query·비밀값 없는 Index를 둔다. Raw State/Saved Plan·Credential·Backup 원본·개인정보·실제 Token은 공개 Evidence나 Git에 넣지 않는다. 민감 Raw 자료의 보호 경로를 값 없는 참조로 연결하고 공유본은 필요한 범위로 정리한다.

| 필드 | 기록할 내용 |
|---|---|
| 식별 | 시험 ID/하위 Case·Requirement·관련 승인 ID·실행/리뷰 담당 역할 |
| 조합 | App/Infra/GitOps Commit·Release ID·Image/Schema/설정/Secret 개정·버전 Manifest·Backup ID |
| 조건 | Cloud/Recovery·Resource/Replica/Pool·데이터 규모·부하·장애 방식·전제·비용 Window |
| 시간 | UTC ISO 시각+KST 표기·시작/종료·관측 지연·주요 장애/재개 시점 |
| 결과 | Baseline·Target·Actual·PASS/PARTIAL/FAIL/N/A·누락·제한 |
| 증거 | 정리한 Log/Metric/Query/영상·Raw 참조·Hash·실행 명령의 민감값 제거본 |
| 해석 | 원인·팀이 한 작업·제품이 처리한 동작·Troubleshooting·변경/재시험 연결 |

제안 경로는 `evidence/<test-id>/<run-id>/summary.md`, 비밀값 없는 `metrics.csv`, `timeline.csv`, `release.json`, `checksums.txt`다. 현재 이 시험 Evidence가 생성됐다는 뜻은 아니다. 실패 실행도 삭제하지 않고 후속 성공과 연결한다. 팀원별 기여는 실제 Commit/시험/문서/문제 해결로 기록하며 제품 기본 동작을 팀 구현으로 표시하지 않는다.

### 3-G.10. 3-F·3-H 연결과 일괄 후속 작업

B01~B05의 코드·권한·배포 조합이 바뀌면 §3-F.20의 표에서 영향을 받는 시험을 고른다. B06 목표/강도가 바뀌면 가동시간·복구 Bundle 크기·역할/재시험·Cost를 3-H와 함께 고친다. 사람이 바뀌어도 동일한 완료 조건과 인계 자료를 유지한다.

기존 IF/IM/Data·계정/Network 시험의 문서 대응과 실행 기록 필드는 3-G 및 3-I에 작성했다. 전체03 최종 컨펌 후 실제 Source를 기준으로 개별 실행 Case·Evidence Index·Demo 시나리오를 일괄 구체화한다. 실제 Source 확인이 필요한 HTTP Path/WS 메시지/인증 형식/Schema는 구현 직전 Seed와 연결하며 설계 전체를 그때까지 중단하지 않는다. 실제 환경과 시험 없이 Acceptance PASS를 미리 기록하지 않는다.

### 3-G 남은 입력과 실행

- [x] B06 시험 기준·정량 목표 작업 전제 승인 반영
- [ ] 실제 Seed·기능·인증·Data 기준·부하 Harness·Resource/Pool 확인
- [ ] 전체03 최종 컨펌 후 실제 Source 기반 하위 시험/실행 Ledger·Evidence Index·Demo 초안 일괄 구체화
- [x] 03 전체 통합 검토·사용자 최종 컨펌 반영
- [ ] 실제 시험·실측·실패 조치·영향 재시험·최종 Must 판정

## 3-H 구현 WBS와 비용

### 3-H.1. 이번 문서의 범위

이 절은 B07로 승인된 설계 이후의 구현 순서·병렬 준비·완료 조건·비용 통제를 기록한다. 03 상세설계 전체와 지침은 최종 컨펌되었고 지금은 **실제 구현 준비** 단계다. 준비 기록은 단일 03에 이어 관리하며 임의로 새 단계 번호를 부여하지 않는다. 설계 문서 작성·사용자 작업 전제 승인·실제 구축/검증을 구분한다.

사용자는 3-F-1 세 가지와 묶음 진행 방식에 이어 2026-10-01 B01~B07도 작업 전제로 승인했다. 전체03 문서와 지침은 이후 사용자에게 최종 컨펌되었고 프로젝트 소스 등록 완료를 확인했다. 설계 확정 전 실제 AWS 생성·IAM 변경·DB Restore·Git Merge/배포·Destroy를 수행하지 않았다. 기존 실제 실행 승인 조건은 유지한다.

### 3-H.2. B07 작업 방식·인계·일괄 검토

B01~B07 작업 전제 승인에 따라 버전/인증/Pull/배포/Replica 선택과 시험·일정·Cost 영향을 연결했다. 결정 기록·문서 상호참조·미확인 입력표·Runbook·시험/WBS의 승인 상태를 일괄 반영했고, 후속 작업은 실제 Source/환경 Preflight와 구현 인계다. 새 선택이 없으면 소단계별 재승인을 요청하지 않는다.

실제 작업은 독립 Repo/로컬 준비를 병행하고 공유 자원 실행은 순차로 한다. 각 트랙은 입력·Owner·결과·인계 조건을 갖는다. 사람 이름은 현재 자료만으로 새로 확정하지 않으며 아래 A~D는 **작업 트랙**, 실제 팀 배정은 확인할 실행 입력이다. 기존 팀 역할 자료가 있으면 최신 유효 상태를 대조해 연결한다.

| 트랙 | 범위 / 승인된 역할 경계 | 상대 트랙에 넘길 결과 | 공유 자원 경계 |
|---|---|---|---|
| A Network/Infra/Hybrid | 세 Root·Backend/Role·Network/ROSA·WireGuard·출력 전달·비용 자원표 | 실제 Caller/Context·준비된 기반 값·Plan/Resource 목록·권한/네트워크 결과 | State/ROSA/Network 실행 단일 Owner |
| B App/GitOps | Seed·Interface 수정·Kustomize·Probe/정상 종료·Release/Sync·다중 Pod 기능 | 검증된 App/Image·Manifest·설정/Secret 참조·대표 기능·Pool/프로세스 값 | App 배포/Root 설정 변경 단일 Owner |
| C Data/Recovery | DB 이관·TLS·Backup/전송/검증·로컬 DB/새 Redis·복구 Bundle의 Data 부분 | 검증 Backup·Hash/기준 시각·Schema/권한·Restore 결과·Data 재개 조건 | Cutover/DB Restore/Failover 순서 단일 Owner |
| D CI/Registry/Observability/Evidence | CI ECR Push·Harbor 보존·Native/UWM 연결·Harness·Cost Ledger/Index | Digest/Release Mapping·관측·시험 준비·비용/실행 Ledger·증거 묶음 | 시험 지휘/장애 주입·Metric 수집 조율 |

Evidence는 D 혼자 만드는 산출물이 아니다. 각 트랙이 자기 작업/실패/시험 결과를 남기고 D가 Index/형식을 연결한다. Reviewer는 실행자와 구분해 정하되 네 명의 실제 시간·역량·과거 역할을 확인해 배정한다. 리뷰가 끝나기 전에 공유 자원에 서로 다른 변경을 적용하지 않는다.

한 트랙의 전체 작업이 끝나야 다른 트랙을 시작하는 방식은 피한다. 예를 들어 A가 기반 설계를 구현하는 동안 B는 Source/Overlay/Case, C는 로컬 Restore, D는 CI/Harbor/Harness를 준비할 수 있다. 실제 Cluster 통합은 A의 기반·C의 Data·D의 Pull/Image·B의 Manifest/Secret 준비가 인계된 뒤 시작한다.

### 3-H.3. WBS와 완료 조건

| ID | 작업 묶음 | 선행 / 병렬 가능 | 종료 조건·인계 |
|---|---|---|---|
| W01 | 03 최종 검토·결정/미확인 입력 정리 | 전체03·지침 최종 컨펌 완료, 미확인 실제 입력은 W02로 인계 | Architecture/Owner/Lifecycle·시험·Cost 충돌 해결, 최종 확정과 구현 입력 미확인 구분 |
| W02 | Source/실행 입력 Preflight·팀 배정 | W01의 승인 범위. Source/Tool/가격 조사 병행 | 구현 직전 Seed SHA·Controller/도구·Account/Region·지원·로컬 자원·역할·가용시간 확인 |
| W03 | Repo/코드·Backend/Role·Pipeline 준비 | W02. A/B/C/D의 독립 작업 병행 | Root별 fmt/validate·PR/Secret/Plan 보호·Output 전달·CI Build/Test/Scan의 기존 도구/정책·Digest 연결·Overlay Render 검증 |
| W04 | 로컬 Data/Recovery/Harness 예행 | W02~03, Cloud 생성 전 병행 | 격리 Restore·Harbor/Bundle·WS/업무 Harness·Evidence 형식 준비. §3-I.14.5의10분/30분/15분 후보에 전체 시간·최신성/손실·부하/공간·추가 작업 부담 연결 |
| W05 | 첫 Full Apply Cost Baseline Gate | 실제 자원수/사양/서비스/단가·Credit 조건 | §3-H.5~7의 전체 예상·Window·정리 비용·Buffer 확인. 불충족이면 Apply 보류 |
| W06 | Window A: Foundation/ROSA·Data/Secret/Pull·GitOps/E2E 통합 | W03~05; Bootstrap→foundation→rosa 의존 순서 | T02~09 정상 경로·T15 정상 플랫폼 진단·T21 Build/Test/Scan/Pull·Backup/Harbor 사전 자료·Resource/Pool/지연 Baseline. 미완료 인계 숨기지 않음 |
| W07 | 통합 결함·Interface/Pool·Manifest 수정 | W06 결과. 공유 변경은 조율 | 원인·영향·수정 PR·필요 시험 통과. Technical Freeze 전 핵심 Must 연결 |
| W08 | Window B: Clean Recreate·장애·부하·Offline 복구 | 검증 Release/Bundle·W07·새 Cost 확인. Gateway/Binding 세부 Case의 소요·재구축/재시험 비용도 반영 | T10~21 세부 Case의 실측·실패/재시험·제한·데이터/업무 일관성·Budget 정리. 미재현 Gateway/AZ 시나리오는 성공으로 기록하지 않음 |
| W09 | 결과 정리·비교·문서·시연 | W06부터 각 트랙 병행, 핵심은 W08 후 | T22~23·실측/영상·기여·Runbook·Cost·실패 설명·Demo Freeze |
| W10 | Final Review·잔존 비용·발표 준비 | W08~09 | Must 최종 판정·한도/잔존/보관 책임·Presentation Ready·최종 Buffer |

각 작업의 `담당/Reviewer·예상/실제 소요·선행 ID·입력 개정·Blocker·결과·영향·증거·다음 작업`을 실행 Ledger에 기록한다. 지금 실제 일정 완료/시간 실측이 없으므로 담당자 이름이나 완료 날짜를 만들어 넣지 않는다.

### 3-H.4. 기존 기간·Freeze와 작업 묶음 연결

| 기존 Charter 창 | 이번 작업 연결 | 진행/완료 조건 |
|---|---|---|
| 10/1~10/2 설계/Architecture 목표 창 | W01~02·Source/버전/가격·Case 준비 | 전체03 검토와 구현 입력 구분, 독립 준비 병행 |
| 10/5~10/8 Foundation/핵심 PoC 창 | W03~06·Window A 후보 | 위험한 Pull·다중 Pod·TLS·Backend·Restore를 먼저 확인 |
| 10/12~10/15 Migration/Integration 창 | W06~07·E2E/Bundle·결함 해소 | 실제 Seed/Schema·핵심 기능·복구 자료까지 연결 |
| **10/16 Technical Freeze** | 핵심 구조/주요 기능 종료 | 구조 확대 대신 Must 결함 조치·시험 준비. 변경 예외는 Charter 기준 |
| 10/19~10/21 Validation 창 | W08·Window B 후보·W09 | Clean Recreate·장애·복구·부하·실측/Cost·재시험 |
| **10/22 Demo Freeze** | W09 | 검증된 Release/설정·실제 증거/영상 고정 |
| **10/23 Presentation Ready** | W10 | 발표 흐름·제한·질의 근거·비용/기여 정리 |
| **10/26 Final Buffer/발표** | 잔여 최종 점검 | 새 핵심 구조를 이때 추가하는 계획을 기본으로 두지 않음 |

날짜 창은 기존 Charter의 목표다. 토·일 필수 작업을 전제로 하지 않으며 실제 학원/팀 휴무·가용일을 확인해 상세 배정을 정한다. 공휴일/휴무를 일반 평일 가용시간으로 자동 계산하지 않는다. 두 Window는 목적상 묶음이며 기간 전체를 Cloud 상시 가동하는 뜻이 아니다.

ECR 수명 경과 Pull 시험의 12시간 이상 경과 조건은 Window A의 필요한 통합 작업과 겹쳐 계획하되 실제 가동시간에 포함한다. 시간/비용이 확보되지 않으면 미실행/부분 검증으로 표시하고 필수 시험 누락 처리로 연결한다. 재생성 직후 Pull만으로 대체 PASS를 기록하지 않는다.

첫 통합 Window에서 핵심 위험이 드러나면 10/19까지 방치하지 않고 같은 입력의 로컬/짧은 추가 검증으로 줄인다. 추가 Cloud Window가 필요하면 남은 비용·재생성 시간·재시험 시간을 Ledger로 대조한다. 예상 일정이 Freeze를 넘으면 Should/Could를 먼저 줄이고 Must/Architecture 변경은 명시적 재검토로 다룬다.

### 3-H.5. 전체 $500 한도와 비용 입력

**기존 승인:** 총 AWS 사용/지원 한도 $500, 첫 Full Apply 전에 Cost Baseline Gate.  
**B07 승인된 작업 전제:** 계획에 사용할 상한을 $450로 두고 $50를 실패/재시험·청구 지연 Buffer로 남긴다. 예상 누적+잔여 실행+잔존 자원 비용이 $450를 넘으면 신규 가동을 보류하고 조정한다. $50는 무조건 추가 지출 승인이 아니다.

현재 실제 서울 Region 단가·Credit 적용 대상·이미 사용한 비용·CloudWatch 집계·사용 Account를 확인하지 않았다. 따라서 **아직 Cost Gate 통과가 아니고 $500 안에 들어간다는 판단도 하지 않는다**. 지역 외 공식 예시 가격을 서울/프로젝트 가격으로 대신하지 않는다.

| 비용 입력 | 반드시 포함할 내용 | 입력 상태 |
|---|---|---|
| ROSA Classic EC2 | Control Plane 3+Infra 3+Worker 3 최소 9개. 실제 서비스 지정 사양·Worker m5.xlarge 후보·생성/삭제 시간 | 수량 구조 확인, 사양/서울 단가/실제 시간 미확인 |
| ROSA 서비스 | 실제 Worker vCPU/가동시간에 따른 요금·과금/구독 시작/종료·Credit 적용 조건 | 미확인 |
| EBS | CP/Infra/Worker/Data/Gateway Volume·크기/유형·Snapshot·삭제 후 잔존 | 미확인 |
| NAT | 승인된 AZ별 3개 Hour·처리 GB·가동 Window 밖 잔존 | 사양 승인, 시간/단가/트래픽 미확인 |
| LB/IPv4/Gateway | API/Ingress Load Balancer·Capacity/전송·사용 Public IPv4·EC2 Gateway/EIP | 실제 생성 목록/가동시간 미확인 |
| RDS | db.t4g.small Multi-AZ DB Instance 후보·gp3 20GiB 후보·Backup/Snapshot·I/O·정지/자동 재시작 | 후보 승인, 실제 단가/시간/Storage 옵션 미확인 |
| ElastiCache | cache.t4g.small Primary+Replica 2개·가동시간·전송/잔존 | 후보 승인, 실제 단가/시간 미확인 |
| S3/ECR | State/Backup/Lock·Version/보관·요청·ECR/Harbor 전송·Image/Backup 크기 | 실제 크기/단가 미확인 |
| Data Transfer/관측 | AZ 간·Internet/On-Prem 전송·Metric/Log·AWS 모니터링 옵션 | 실제 구성/GB/단가 미확인 |
| 잔존/오류 | 실패 생성·삭제 지연·Orphan LB/EBS/EIP·재시험·RDS 7일 이후 재시작 | Ledger/일별 확인 필요 |

RDS Multi-AZ의 과금/Storage는 실제 AWS Calculator 항목대로 계산하고 Primary 1대의 가격만 넣거나 중복으로 두 번 곱하지 않는다. ElastiCache는 2 Node를 계산한다. ROSA 요금도 모든 9 Node를 서비스 Worker vCPU로 곱하는 것으로 단순화하지 않는다. Credit이 서비스/Marketplace 요금에 적용되는지 확인한다. 기존 CI Scan·지원되는 플랫폼 진단·격리된 삭제 보호 시험의 실제 준비/수행/재시험 시간과 수집/보관 비용도 각 실행 Ledger에 포함한다. 이 문서 보완으로 고정 Window 시간·새 요금·시험 성공을 임의로 추가하지 않는다.

### 3-H.6. Cost Gate·가동 Window 계산

단가를 확인한 뒤 다음 구분으로 계산한다. 금액은 추정·관측·확정 청구를 나눠 기록한다.

`예상 전체 비용 = 현재 누적 비용 + 잔여 foundation/Data/Storage 비용 + 잔여 ROSA/관련 자원 Window 비용 + 전송/요청/관측 예상 + 정리 지연/실패 예상`

공통 시간당비를 산출한 경우, 두 Window의 합계 가동 가능시간은 `($450 - 현재 누적 - 잔여 비Window 비용 - 기타 예상 비용) / Window 추가 시간당비` 이하에서 계획한다. Window마다 사양/비용이 다르면 이 식 하나로 합치지 않고 따로 계산한다. 분자가 0 이하이면 가동을 시작하지 않는다. 실제 AWS 생성/초기화/실패/삭제 완료까지의 과금 시간을 포함하고 App 시험 시간만 세지 않는다.

| Gate | 확인 | 진행 조건 |
|---|---|---|
| C0 입력 | 서울 Region 단가·Credit 대상·누적/잔존·실제 Node/Volume·필수 서비스 | 누락 항목과 확인 책임을 해결 |
| C1 첫 Full Apply | 사양/Plan·두 Window·Data 유지/정리·실패 Buffer·한도 | 승인된 계획선인 전체 계획 비용≤$450와 $500 한도 충족, 기존 실행 승인 확인 |
| C2 Window 진입/추가 | 현재 비용·남은 Window·복구 자료·재생성 지연 | 남은 예산 안에서 Must 시험·정리까지 가능 |
| C3 매일/종료 | Resource 실제 목록·가동/삭제 완료 시각·잔존·청구 지연 | 비용 증가 원인 확인·추가 가동 보류/조정·증거 보존 |

AWS Budget/알림은 감지 도구이고 정확한 시점에 자원을 자동 정지시켜 한도를 보장하는 장치가 아니다. Billing 지연 때문에 실시간 수치만 보지 않고 Resource 시간 추정과 같이 판단한다. 이미 끝난 Window라도 청구가 모두 반영됐다고 가정하지 않는다.

Ledger 제안 필드: `Resource/State Owner·Region/AZ·Service/사양·수량·단가 출처/확인일·Credit 조건·생성/중지/삭제 완료·예상 가동시간·관측 누적·예상 잔여·Buffer·잔존 책임·증거`.

### 3-H.7. 정리·가동 중단·Data 보호

기본 비용절감 Destroy는 기존 승인대로 **rosa State**이며 foundation/bootstrap 전체 Destroy는 별도 명시적 승인 조건을 유지한다. Window 종료 전에 검증 Backup·Harbor Image·Release Bundle·결과·Cloud Data 재개 조건을 확인한다. 삭제 완료 뒤 Cluster-specific 자원·LB/EBS/EIP·서비스 과금 종료와 foundation의 실제 잔존 비용을 점검한다.

NAT Gateway에는 일반 EC2처럼 Stop 기능이 없으므로 가동 중단은 3-B의 foundation 코드/Lifecycle 변경·Route 영향 검토로 처리한다. ROSA/백업/관리의 필수 경로가 살아 있는 동안 NAT를 무심코 제거하지 않는다. RDS 정지 중 Storage/Backup 비용·최대 정지 후 자동 재시작을 반영한다. ElastiCache는 Stop을 가정하지 않고 유지 비용 또는 승인된 새 Runtime 재생성 계획을 선택한다.

일별 잔존 확인은 자동 Destroy 예약이 아니다. 새 파괴적 작업을 단순 예산 알림으로 실행하지 않는다. 한도 위험이 있으면 신규 생성/Window를 먼저 보류하고 현재 허용된 Lifecycle 안에서 정리하며 Data/Backup/State 보호를 유지한다.

### 3-H.8. 위험을 앞당겨 확인할 항목

| 위험 | 먼저 확인할 작업 | 실패했을 때의 영향/조치 |
|---|---|---|
| 실제 Classic 지원/구독/권한/비용 | W02·W05, 최초 Full Apply 전 | B01~03·가동시간·Cost 수정. HCP/Single-AZ로 조용히 전환 안 함 |
| Backend/Role·입력 전달 | W03·T02~03 | 세 Root 전체 진행 영향, 최초 Local/Remote 복구·Caller 수정 |
| ECR 새 Node Pull | W06 초기·T21 | App 전체 배포 차단, Classic Role/정책/Network·추가 대안 영향 검토 |
| 다중 BE Pod의 메모리 상태/중복 | W02 Source·W06 T08~09 | B05·App 수정·DB/Redis·부하/일정 영향, Replica만 늘려 완료 처리 안 함 |
| RDS/Redis TLS·Driver/Pool | 로컬 Driver/CA 확인·W06 T04 | Data/App/복구 통합 차단, Source에 맞게 연결/타임아웃 수정 |
| 실제 Dump 크기·복구 도구·로컬 자원 | W04·T17~18 예행 | DataVM 공간·RTO/RPO·Bundle/가동시간 조정 |
| Secret/Host/Schema/Release 불일치 | W06·W08 T19 | 재현성/기능/복구 실패, 조합 Metadata와 새 환경 입력 일괄 갱신 |
| 예산/일정 부족 | W05와 C2·매일 Ledger | Should/Could 우선 축소, Must/Architecture 변경은 별도 재검토 |

구체적으로 막힌 입력만 Blocker로 표시한다. 예를 들어 실제 DB Engine을 아직 확인하지 못했어도 GitOps 구조·Case·Recovery Bundle 형식 설계는 계속할 수 있다. DB 호환 import/Driver 실행은 확인 뒤 수행한다.

### 3-H.9. 연쇄 영향 기록과 03 전체 최종 검토

§3-F.20이 통합 영향표의 기준이며 3-H는 작업/비용 결과를 덧붙인다. 변경 시 `직접 변경→의존 입력/Owner→실행 순서→시험→Cost/일정→문서`를 대조한다. 한 부분의 승인만 바뀐 것처럼 기록하고 관련 시험/Pool/권한/복구가 남는 일이 없게 한다.

Runbook/시험/WBS와 연쇄 영향은 **3-I의 전체 통합 검토**에 일괄 작성했다. B01~B07 작업 전제의 승인 상태와 연결을 반영했으며 전체03·지침의 최종 컨펌과 등록 완료 확인을 반영했고 실제 Source 기반 구현 인계는 §3-I.13으로 이어간다. 사용자에게 새 선택이 없는 작은 승인 묶음을 다시 연속 제시하지 않는다. 실제 새로운 의사결정이 발견되면 원인·선택지·영향받는 기존 승인만 묶어 제시한다.

| 최종 검토 항목 | 대조 문서 | 완료 정의 |
|---|---|---|
| Source/문서 단계/상태 | 03·전체 Header | 최신 승인 우선·파일 번호/프로젝트 단계 구분·참고 자료/실제 확인 구분 |
| Architecture Invariant | 02·3-B~3-H | Cloud의 On-Prem 비의존·Classic Multi-AZ·RDS/Redis·복구/Data·$500 유지 |
| Owner/Lifecycle | 3-B~3-F | 자원별 단일 Owner·삭제 경계·State/Role/Secret·Offline 예외 모순 해소 |
| Release/업무/Data | 3-D~3-G | Seed/Image/Schema/설정/Secret/Backup 조합·다중 Pod/중복/불명 결과·복구 손실 범위 연결 |
| 시험/Evidence | 3-G·기존 IF/IM/Data | Must/수치/판정·누락/제한·관측·Demo 주장 근거 연결 |
| 실행/비용/일정 | 3-H | 역할·인계·실제 입력 Gate·Window·단가/누적·Freeze·잔존 책임 연결 |
| 미확인 실행 입력 | 전체 | 값/책임/확인 시점/막는 작업을 명시. 문서 승인으로 검증 성공 처리 안 함 |

03 전체 검토는 설계 문서 최종 확정이며 실제 구현·시험의 성공까지 미리 확정하는 단계가 아니다. 나중에 실제 Source/지원/측정 결과 때문에 변경할 경우 최종 문서를 근거·영향·재검증과 함께 개정한다.

### 3-H 남은 입력과 실행

- [x] B07 작업 트랙·Window·계획선/여유 작업 전제 승인 반영
- [x] B01~B07 승인 기록·상호참조·Runbook·시험/WBS/Cost 연결 반영
- [x] 전체03 최종 컨펌 후 최종 문서 상태·준비 인계 정리
- [x] 03 전체 통합 검토·사용자 최종 컨펌
- [ ] 실제 Seed/환경/팀/휴무/단가·Credit 조건·Cost Gate 확인
- [ ] 실제 코드·실행 승인·통합/재생성/장애/복구/부하·Evidence·잔존 비용 정리

## 3-I 통합 검토와 구현 인계

### 3-I.1. 무엇이 승인되었고 무엇이 남았는가

| 범위 | 현재 상태 | 유지할 내용 / 확인할 내용 |
|---|---|---|
| Charter / Target | 기존 승인 기준 | Cloud Primary·Classic Multi-AZ·RDS/Redis·On-Prem Restore·기간/Freeze·$500 한도 유지 |
| 3-A | 작업 전제 승인 | 네 Repo·1차 보존·구현 직전 Seed·Owner·Release/Evidence 경계 |
| 3-B | 작업 전제 승인 | 서울 Region·IPAM/Subnet·API/Ingress·AZ별 NAT·Route/SG·WireGuard/Gateway·Lifecycle |
| 3-C | 작업 전제 승인 | 사람 IAM User 4개+Admin·목적별 실행 Role·ROSA IDP/RBAC·제한된 CI/Backup·SOPS+age 공급/복구 |
| 3-D | 기존 구조 유지/현재 주기와 이전 이력 구분 | 논리 이전·격리 Restore·새 Redis·TLS 유지, 현재15분 Backup 계획/7일 보존·초기 Data 크기·업무 재개/중단 — §3-I.14.5 |
| 3-E | 작업 전제 승인 | 같은 Host의 FE/API/WSS·Edge TLS·설정/Secret·Probe/종료·인증·재접속·중복/불명 결과·부분 실패 |
| 3-F-1 | 작업 전제 승인 | 세 Root/State Key·bootstrap 실행 Role 소유·제한 Output 전달·Ansible 최초 GitOps 설치/인계 |
| 3-F·3-G·3-H | B01~B07 작업 전제 승인 — 2026-10-01 | 버전·Backend 인증·Runtime Pull·배포/Offline·Replica·시험 수치·작업/비용 운영 |
| 전체03 문서·지침 | 두 문서 전체 최종 컨펌·소스 등록 완료 보고 — 2026-10-01 | 승인된 설계 기준. 실제 입력/지원·가격/구현·시험은 별도 |
| 실제 구축/시험 | ROSA 최종 시험 NOT RUN | 읽기 전용 GitHub Repo/Issue/지정 Source 조회 완료, demo2는 팀원 보고 Evidence. AWS/ROSA/DB/Controller 직접 조회·생성/변경·시험 수행은 미실행 |

소단계 승인과 최종 설계 확정을 구분한다. 최종 설계 확정도 실제 Runtime PASS를 미리 확정하지 않는다. 이후 실제 지원·Source·측정 결과가 변경을 요구하면 이유·의존 문서·시험·비용과 함께 개정한다.

### 3-I.2. 단일 상세설계의 검토 순서

프로젝트 소스의 상세설계는 `03_DETAILED_DESIGN.md` 하나로 관리한다. 이 문서에 3-A~3-H 전체 상세 내용과 3-I의 통합 검토·시험 대응·미확인 입력·Runbook을 함께 담았다. 이 절의 요약만으로 세부 설계를 대체하지 않는다.

사용자는 3-I의 승인 상태 표와 검토 결과→3-F의 B01~B05→3-G·3-H의 시험/실행 영향→관련 3-A~3-E 상세 근거 순서로 대조할 수 있다. IF-01~18·IM-01~09와 통합 T01~23의 상세 요구/대응도 같은 문서에 포함한다. 별도 작업 파일 없이 같은 문서 안에서 확인한다. 현재는 승인된 설계 기준이며 실제 구현 준비의 최신 상태는 §3-I.13을 따른다.

### 3-I.3. Architecture와 소유권 대조 결과

아래 결과는 문서의 설계 정합성 검토다. 자원/기능/장애 시험의 PASS가 아니다.

| 확인 항목 | 문서 대조 결과 | 실제 적용 전 확인 |
|---|---|---|
| Cloud 정상 Runtime의 On-Prem 비의존 | ECR·Cloud DB/Redis·Route 정상 경로에 Jenkins/VPN/Harbor 상시 의존을 넣지 않음 | VPN/CI 경로 차단 후 사용자 업무와 새 Pull 시험 |
| ROSA Classic Multi-AZ | 모델/최소 Node 구조·비용 항목 유지. HCP/Single-AZ 대체 승인 없음 | 계정/Region 지원·실제 Node/사양·설치·총비용 |
| Data HA와 Offline Recovery | RDS 동기 Standby·Redis 비동기 Replica·사전 Backup Restore를 구분 | 제품별 장애·영속 Data 손실·진행 게임 중단·RTO/RPO |
| 세 State Lifecycle | 실행 Role은 bootstrap, 공통 자원은 foundation, Cluster별 자원은 rosa | 실제 Provider Resource·IAM/OIDC·부속 자원 삭제 순서 |
| 일반 비용절감 삭제 | rosa 반복 생성/삭제. foundation/bootstrap 전체 Destroy는 기존 별도 승인 조건 | 실제 Plan·잔여 DB/Redis/NAT/LB/EBS/IPv4 비용 |
| 사람과 자동화 계정 | 사람 4+ECR CI 1+Backup 1 IAM User 계획 유지. TF Role은 별도 | 실제 MFA·Key·Trust·Policy·STS 갱신·공유 Role 범위 |
| Secret과 GitOps | 값/프로젝트 Secret은 별도 공급, Operator 생성 객체는 Operator 소유 | 자동 Prune/수동 삭제·Application finalizer/연쇄 삭제·Namespace 삭제·State/Plan 유입·실패 출력 보호 |
| TF/Bootstrap/GitOps Owner | AWS/ROSA는 TF, 설치 예외는 최소 Ansible, 이후 Cloud Desired State는 GitOps | 같은 객체를 Provider/CLI/Argo/Bootstrap이 중복 관리하지 않는지 |
| Offline 배포 | 별도 새 DB/Redis·Harbor/보존 자료 사용. Ansible Apply는 B04로 승인된 로컬 복구 Owner 예외로 표시 | Cloud/GitHub 신규 조회 없이 로컬 Namespace에서 실제 복구 |
| 비용/일정 | $500 한도·Technical/Demo Freeze 유지. $450 계획선은 B07 승인된 작업 전제 | 실제 단가/Credit·누적/잔존·팀/휴무·Window 시간 |

### 3-I.4. 분야별 작업 문서 검토에서 보강한 항목

이 절은 B01~B07 승인 이전 검토 당시의 기록이다. 당시의 제안/미승인 표기는 역사적 상태이며 현재 승인 상태는 §3-I.1·5·12.2를 따른다.

| 항목 | 반영 문서 | 보강 내용 / 승인 영향 |
|---|---|---|
| 이전 Redis 미정 문구 | §3-A.5 | 기존 Redis 재사용 대안에서 별도 새 Recovery Redis의 승인된 현재 선택으로 최신화 |
| TF 실행 Role/Output 인계 | §3-C.4 | bootstrap Owner·제한된 입력 파일 전달의 3-F-1 승인 참조 반영 |
| 3-F-1 신규 제안 표시 | §3-E.17·체크리스트 | F1 승인과 B01~B07 미승인을 분리 |
| 설치 Manifest의 원본 | §3-A.7 ↔ §3-F.6 | Subscription/필요 설치 객체의 Infra 예외와 Root/이후 GitOps 원본 구분 |
| Rolling 중 자원/DB 연결 | §3-F.18.2 | 종료 중인 이전 Pod의 프로세스·DB 연결·자원 포함. Replica+Surge만으로 최대 사용량을 단정하지 않음 |
| 정상/오류 HTTP·WSS 시험 | 3-G T06/T07/T09 | SPA/없는 API·HTTPS/Origin/Proxy·유휴/긴 게임·Heartbeat/Timeout의 기존 IF 요구 명시 |
| 입력/Offline 시험 참조 | 3-G T02/T18/T19 | 오래된/다른 Account 입력 차단과 Offline IM-08 연결, 모호한 교차참조 정리 |
| ECR 지속 인증 시험 | §3-F.16.2·3-G T21 | 12시간 뒤 Pull 성공과 실제 Token 발급/갱신 관측 범위를 구분. 대기 비용은 가동시간에 포함 |
| 오류율·RPO 해석 | §3-G.6~7 | 첫 업무 시도 오류와 재시도/최종 실패를 나눔. 영속 DB의 RPO와 진행 게임 Runtime 손실을 구분 |
| 통합 검토 경로 | 3-A~3-H | 현재 문서의 동일한 검토 시작점으로 연결. 기존 승인 상태를 승격하지 않음 |

이 보강은 기존 승인 요구를 구현/시험으로 정확히 연결하는 작업이다. 새 계정·제품·상시 서비스·Architecture 변경·성공 목표 완화를 추가하지 않았다. 이 검토 당시 B01~B07은 제안 상태였으며, 이후 작업 전제 승인을 §3-I.12.2에 반영했다.

### 3-I.5. B01~B07 승인된 작업 전제와 재검토 대안

승인된 B01~B07의 자세한 비교·실제 확인 조건은 §3-F.13~20, §3-G.2~7, §3-H.2~7에 있다. 아래 표는 이번 작업 전제 승인 내용을 전체03에서 대조하는 표다. 대안을 자동 채택하지 않으며 전체 검토 또는 실제 지원/Source/측정 결과로 변경이 필요하면 영향을 함께 검토한다.

| ID | 승인된 작업 전제 | 재검토 대안 / 차이 | 영향 |
|---|---|---|---|
| B01 | Core 1.16.4·AWS 6.66.0·RHCS 1.7.7·ROSA 4.20 계열·GitOps 1.21.4 후보, 실제 지원/검증 후 정확한 조합 고정 | 실제 지원되는 다른 GA 조합. 최신값 자동 추종은 재현/지원 대조 부담 | Provider Schema·IAM/OIDC·Bootstrap·시험·Tool Bundle |
| B02 | SSE-S3 보호 Backend·개인 MFA→목적별 STS Role | SSE-KMS는 별도 Key/Policy/복구/비용 관리. 사람 권한 체계 확대는 현재 기본안에 없음 | State/Plan·최초 인증·장시간 Apply·복구·권한 시험 |
| B03 | Classic Worker Role에 지정 ECR Repo Pull 권한·추가 Pull IAM User 기본 제외 | 지원되는 Pull Secret 경로는 발급/갱신·원본 Key·추가 Owner 필요. 실제 지원 제약이 나오면 비교 | 공유 Role/Cluster·새 Node/지속 인증·Network·계정표 |
| B04 | Base+Overlay·Digest·CI→PR→GitOps·App 자동 Sync/SelfHeal·자동 Prune 보류. 로컬 복구는 보존 Manifest를 Ansible Apply | App 수동 Sync는 배포 단계 증가. 자동 Prune는 삭제 범위 보호 필요. Offline GitOps는 로컬 Git/Controller 가용성 준비 필요 | Namespace/Secret·Release/Schema·Offline Owner 예외·복구 시간 |
| B05 | Worker 3개·FE/BE 각 3 Replica 후보·PDB/배치/Rolling/Pool 함께 검증, Recovery 초기 각 1 | Replica/Worker 감소는 시험/가용성 목표에 영향. 확대는 Node/DB/비용 영향. Source 확인 없이 선택하지 않음 | 다중 Pod 상태·DB 연결/Redis·자원 여유·부하/장애·비용 |
| B06 | 정상60명/30분·HTTP/WS p95 1초·오류율1% 미만·Must 묶음 유지. Offline 기존30분/90분 승인 이력은 보존하고 현재 DR 설계는 RTO10분/RPO30분 — §3-I.14.5 | PR #30으로 채택·병합된 요구사항을 적용. 부하/정상 성능은 변경하지 않으며 실제 복구 달성은 미검증 | Harness·Data 규모·부하·실패/재시험·주장 범위 |
| B07 | 네 트랙·목적별 가동 Window 두 묶음·$450 계획+$50 여유·기존 Freeze 유지 | 가동 구간 재배치/추가는 남은 예산·재생성·시험 시간을 다시 계산 | 담당/인계·가동시간·잔존/실패 비용·일정 |

공식 공개 버전 존재는 전체 조합의 검증 성공이 아니다. Worker Role Pull도 Pod별 IAM 격리를 제공한다는 뜻이 아니다. 60명·RTO/RPO는 측정 전 프로젝트 목표이며 제품 SLA로 표현하지 않는다.

### 3-I.6. 미확인 입력과 막는 작업

아래 입력이 없다고 문서 대조·Case·Index·Runbook 준비 전체를 중단하지 않는다. 각 입력에 의존하는 실제 작업만 그 확인 뒤 수행한다.

| 입력 | 확인 책임 트랙 | 확인할 내용 | 직접 의존 작업 |
|---|---|---|---|
| 실제 Seed/Source | B·C | Repo Metadata·보고 Commit의 지정 Source 조회는 §3-I.13. 실제 Seed/SHA·Maintenance·전체 인증/Path/메시지·Schema·Process/상태 공유는 확인 전 | App 수정·이관·다중 Pod·업무/부하 시험 |
| Account/Region/Classic 지원 | A | 계정/구독·Quota·서울 제공 버전/사양·현재 Resource 충돌 | Full Apply·ROSA 생성/삭제 |
| Tool/인증 | A·D | 실제 Controller/CLI·Checksum/Lock·MFA/STS Profile·장시간 Apply 갱신·OCM 인증의 공급/만료 | Validate/Plan/Apply·Bootstrap |
| 객체별 IAM/IDP/Secret | A·B·C | 실제 Worker Role/공유 범위·IDP/OAuth 객체 Owner·Master/App/Backup 자격 공급·Provider의 State/Plan 저장 | 권한/IDP/Data/Secret 실제 구성 |
| Network 실제 값 | A·C | On-Prem/DataVM Source·주소/CIDR·DNS/CA·경로·SG/TLS | VPN·DB/Redis·Backup 통신 |
| 로컬 자산 | A·C·D | VM Provisioning 경로·Storage/공간·독립 DB/새 Redis·Namespace·Harbor/CA·보존 도구 | Offline Restore/배포 |
| Release/Backup 조합 | B·C·D | ECR/Harbor Digest/플랫폼·Schema/설정/Secret 개정·Backup ID/Hash/Data 기준 시각 | 배포·Rollback·Recovery·재현 |
| 실제 측정 | B·C·D | Requests/Limits·Process/Pool·DB max_connections·종료 중 Pod·Dump 크기·Harness | 크기/부하·RTO/RPO·Window 산정 |
| 일정/가격/Credit | 전체·D 취합 | 팀원별 가용일/휴무·서울 단가·Credit 범위·누적/잔존·최대 가동시간 | 담당/Window 상세 확정·Cost Gate·신규 가동 |

현재 Master/OCM 인증의 실제 공급 형식·IDP Resource별 State 유입 등은 확인 전이다. 기본 Secret 경계/Owner 안에서 지원 형식을 확인한다. 새 Secret 서비스·계정·권한 확대·Owner 변경이 필요해지면 관련 B 묶음의 영향으로 제시하며 단순 값 확인을 새 승인 단계로 만들지 않는다.

### 3-I.7. 구현 인계 Runbook

이는 실행할 순서와 종료 조건이며 현재 생성된 Script/Playbook·실행 성공 기록이 아니다. 실제 명령은 확인한 Repo/Tool/Account 입력을 사용하며 평문 Secret/가짜 ARN을 채워 실행하지 않는다.

| 순서 | 진입 조건 | 수행할 작업 | 종료 조건 / 중단 조건 |
|---|---|---|---|
| R01 Preflight | 승인 설계 범위·실제 Seed/환경 담당 | 버전 Manifest·Source/Root·Caller/Region·입력 개정·로컬 자산·Cost 입력 대조 | 누락은 직접 의존 작업에 Blocker로 기록. 다른 준비는 진행 |
| R02 최초 Backend/Role | Role 없는 최초 개인 MFA 인증·충돌/권한 확인 | bootstrap Local 생성→Backend/Role 확인→Remote 이전→정상 목적별 Role 재실행 | Key/Serial/Lineage·Lock·Caller 검증. 이전 실패 시 사본 보호·재적용 보류 |
| R03 foundation | 승인된 입력·읽기 전용 조회·Cost/실행 조건 | 기반 Network/Data/Registry/공통 IAM Plan·Review·Apply·필요 Output 제한 추출 | Owner/실제 자원/접속 경계·보호 입력 파일. rosa 소비 전 최신값 확인 |
| R04 rosa | 실제 Classic 지원·기반 값·Cost/실행 조건 | Cluster/Machine Pool·Cluster별 IAM/OIDC 생성·Ready/Context 확인 | 실제 Node/Role/Host·기반 Data 보존. 오래된 Context 재사용 차단 |
| R05 플랫폼/Secret | Ready·정확한 Context·최소 설치 권한 | Operator/Root 최초 등록·Platform 검토 Sync·Namespace·scope별 Secret 공급 | App 자동 Sync 보류, Operator 객체 덮어쓰기 없음, 필수 참조/개정 준비 |
| R06 App 통합 | Source/Test·Image Scan 결과가 연결된 검증 Image/Digest·Pull·TLS·Config/Secret·Schema | 최초 App 수동 Sync·E2E·다중 Pod/Pool 확인. 승인 범위의 자동 Sync 전환 | 핵심 업무·권한·결과/상태 일관성. 연결만 성공했다고 완료 처리 안 함 |
| R07 복구 사전 준비 | 검증 Release·완성 Backup·로컬 도구/Harbor | Recovery Overlay Render·Registry Mapping·암호화 설정·Backup Hash/복호화/실제 Restore 예행 | AWS/GitHub 신규 조회 없이 시작할 Bundle·도구·Key/CA 확보 |
| R08 검증 Window | 검증 Release/Bundle·현재 Cost·단일 시험 지휘 | Clean Recreate→Baseline→장애 순차→부하·격리 Offline Restore | T/IF/IM 결과·Actual·실패/제한·필요 재시험. Control Plane/Worker 진단·CI Scan·삭제 보호의 하위 Case도 개별 기록. 공유 자원 복합 변경 조율 |
| R09 종료/비용 | 결과/복구본 보존·정확한 삭제 범위 | rosa 종료/삭제·부속/잔존 자원·과금 종료/지연·Data/NAT/Storage Ledger | foundation/bootstrap 전체 Destroy 기본 실행 안 함. 잔존 책임·예상비용 기록 |
| R10 최종 Evidence | 실제 결과·변경/재시험·Release/Cost | 성공축별 Index·기여·실패 원인·비교·Demo/발표·제한 | Must 최종 판정·Freeze·발표 근거·잔존/보관 책임 |

병렬 작성은 A Infra, B App/GitOps, C Data/Recovery, D CI/Registry/관측/Harness에서 가능하다. 동일 State 쓰기·권한/Root 변경·Cutover·DB Restore·장애 주입·삭제는 대상별 실행 Owner와 인계 순서를 지킨다. 담당 이름은 트랙에 실제 배정한 후 기록한다.

Release 인계에는 `App/Infra/GitOps Commit`, `FE/BE ECR·Harbor Digest 및 플랫폼`, `Schema/Config/Secret 개정`, `Backup ID·Hash·Data 시각·로컬 검증 시각`, `Tool Manifest`, `Evidence Index`를 포함한다. 비밀번호/Key/Token/Backup 원본/State/Plan은 이 공개 Metadata에 넣지 않는다.

### 3-I.8. IF와 IM 하위 시험 대응

각 하위 시험은 별도 결과를 남긴다. 통합 T 시험의 PASS 하나가 모든 하위 요구의 PASS를 대신하지 않는다. 현재 전부 미실행이다.

| 하위 ID | 필수 확인 범위 | 통합 시험 |
|---|---|---|
| IF-01 | 같은 Host FE/API/WSS·TLS·정확한 Path/Service·핵심 업무 | T06 |
| IF-02 | 없는 API/WS 경로·SPA 새로고침·오류의 HTML 200 은폐 방지 | T06 |
| IF-03 | HTTP→HTTPS·Origin·신뢰 Proxy Header·인증/노출 | T07 |
| IF-04 | DB/Redis 단절/Failover·Liveness 재시작 폭증·연결/결과 불명 | T12·T13 |
| IF-05 | Redis 메모리 압박·쓰기 거부·부분 상태 | T13 |
| IF-06 | Rolling·Pod 종료/강제 삭제·진행 요청·재접속/중복 | T10 |
| IF-07 | WSS 유휴/긴 게임 대기·Heartbeat/Timeout·단절·종료 원인 | T09 |
| IF-08 | 재생성/로컬 복구의 설정·Secret·TLS·로그인/HTTP/WSS | T18·T19 |
| IF-09 | 미인증·Origin·타인 Room/Game 접근/쓰기 거부 | T07 |
| IF-10 | 만료/로그아웃/권한 변경 후 기존 WSS 새 업무 차단 | T07 |
| IF-11 | 단절 중 이벤트·Snapshot/Turn 변경·공백/역순·현재 상태 | T09 |
| IF-12 | 새 연결 뒤 이전 Message/Disconnect/Leave 차단 | T09 |
| IF-13 | 같은 ID/다른 내용·다중 Pod 동시 Turn/결과·중복 방지 | T08 |
| IF-14 | Commit 후 응답 유실/불명·결과 조회·동일 요청 처리 | T08·T12 |
| IF-15 | DB 확정 뒤 Redis/통지 실패·DB 보존·제한/정합성 | T08·T12·T13 |
| IF-16 | Redis Failover/Key 손실/새 Runtime·재접속과 업무 재개 구분 | T13·T18 |
| IF-17 | noeviction/쓰기 중간 실패·불완전 상태·완료 오표시 방지 | T13 |
| IF-18 | 로컬 DB/새 Redis·Image/Secret 사전 보존·완료 기록/새 게임 | T18 |
| IM-01 | 최초 Local Bootstrap→Remote 이전·목적별 Role | T02 |
| IM-02 | Caller·Key 접근·무관 Key 실패·Lock | T02·T03 |
| IM-03 | foundation 재실행의 Binding 유지·Cluster 삭제 전 해제·기반 Rule/Data 보존·새 Worker SG 연결·양쪽 정상 Plan·잔존 비용 | T19·T20 |
| IM-04 | 제한 Output·오래된/다른 Account 입력 차단 | T02 |
| IM-05 | GitOps 최초 설치·재실행·Owner·상시 덮어쓰기 방지 | T19의 Bootstrap 및 최초 통합 단계 |
| IM-06 | Secret 공급 전 Sync·교체·자동 Prune/수동 삭제·Application finalizer/연쇄 삭제·Namespace 경계 | T03·T19 |
| IM-07 | Clean Recreate·새 Host·Pull·Secret·업무 | T19 |
| IM-08 | 사전 보존 자료만으로 Offline Data/Redis/App 복구 | T18 |
| IM-09 | State/Plan·Ansible/CI 출력·실패 정리·노출 경계 | T03 |

3-D의 Data 시험은 T05/T12/T13/T17/T18에 연결한다. 실제 Dump/Schema/Row·TLS·완성본/Hash·복호화/import·업무 비교·실패 전송/보관은 개별 Case로 결과를 남긴다. 3-B NET-01~10의 허용 Source/Route/SG/Gateway는 §3-G.4.1의 T03/T04/T14에 연결하고, Data SG Binding Lifecycle은 T19/IM-03에 연결한다. 3-C의 IDP/RBAC·신규/기존 Session 회수·CI/Backup 경계는 T03에 연결한다. Rollback은 Charter의 Should이며 §3-G.4.2/T10의 선택 Case로 유지한다. 새로운 번호를 만들었다는 이유로 기존 요구를 삭제하지 않는다.

### 3-I.9. 변경 영향과 실행 기록

| 변경 | 함께 대조할 항목 | 관련 시험 |
|---|---|---|
| 버전/Provider/플랫폼 | Role/OIDC·Root/Lock·설치·Tool/Bundle·삭제 순서 | T02·T03·T19·T21 및 바뀐 기능 |
| Role/Backend/Secret | Caller·Key 접근·만료/갱신·State/Plan·Namespace/공급 | T02~04·T06·T18·T19·T21 중 영향 범위 |
| Replica/Process/Pool/종료 | 종료 중 Pod 포함 최대 연결·Node CPU/RAM·재접속·Redis·비용 | T08~13·T16 |
| Route/Host/CA/Config | 공개 URL·Origin·IDP Callback·Proxy·TLS·Secret 개정 | T04·T06·T07·T09·T18·T19 |
| Schema/Backup/Release | Data 호환·Cutover·업무 확정·Harbor Mapping·RTO/RPO | T05·T08·T12·T17~19 |
| Window/수치 목표/예산 | 부하·사전 Backup 시각·필수 시험·재생성/정리·Freeze | T16~20·T23 |

변경 Ledger는 `기존 값 / 새 값 / 이유 / 승인 상태 / 직접 의존 / 영향 문서·시험 / Cost·일정 / 재검증 결과 / 남은 입력`을 기록한다. Case/실행 Ledger는 `Requirement / 조건·Release / Baseline / Target / Actual / Evidence / 판정 / 제한 / 재시험`을 기록한다. 미실행을 Actual=0이나 PASS로 채우지 않는다.

재시험은 변경 영향이 있는 범위로 수행한다. 별도 이유 없이 전체 시험을 반복하거나, 영향받는 시험을 수정 내용과 함께 추적하지 않은 채 생략하지 않는다.

### 3-I.10. 전체03 검토와 이후 처리

B01~B07 우선 작업 전제 승인 이후, 두 문서 전체 최종 승인과 프로젝트 소스 등록 완료가 보고됐다. 전체03과 지침의 승인 상태·구현 인계에 이를 반영했다(§3-I.12.4). 문서 승인과 실제 지원/구현/시험 결과는 별도로 유지한다.

전체 검토 체크리스트:

- [x] 소단계와 B01~B07의 작업 전제 승인·전체03 최종 확정·실제 검증 상태 구분
- [x] Repo·Owner·State/Lifecycle·계정·Secret·Cloud/Offline 경계 문서 대조
- [x] Interface 요구와 IF/IM·통합 T 시험 연결
- [x] Replica/종료/Pool·복구/Data·가동시간/비용의 연쇄 영향 정리
- [x] 미확인 입력의 담당·확인 시점·직접 막는 작업 구분
- [x] B01~B07 사용자 작업 전제 컨펌·관련 상태 반영
- [x] 승인 반영본 두 문서에 대한 사용자 최종 컨펌 확인 — 실제 지원/비용 미검증 조건 유지
- [x] 전체03·지침 전체 최종 컨펌 범위 반영, 별도 변경/보류 지시 없음

이후 승인 반영·상호참조·Runbook·시험/WBS/Cost 인계는 일괄 처리한다. 정확한 Source/패치/ARN/Host·측정 기반 Pool/Probe는 승인 범위의 구현 입력으로 확인하며 값을 하나 확인할 때마다 새 승인 소단계를 만들지 않는다. Architecture·계정·권한·상시 서비스·비용/일정·성공 기준에 실질적 변경이 필요한 경우에만 그 영향을 묶어 다시 결정한다.

### 3-I.11. 통합 이전 분야별 작업 문서의 재귀 검토 기록

**이후 상태:** 이 절과 §3-I.12.1~3은 당시 검토 이력이다. 과거의 컨펌 대기·미조회·미실행 표현을 현재 상태로 읽지 않는다. 최신 전체03 승인/등록 상태는 §3-I.12.4, 추가 Evidence·구현 준비는 §3-I.13을 따른다.

#### 3-I.11.1 범위와 종료 조건

이 절은 단일 문서 통합 이전에 수행한 분야별 작업 문서 검토 기록이다. 당시 검토 대상은 통합 검토 결과, 분야별 작업 문서, 제공받은 기준 원본 네 문서와 확인 가능한 공식 기술 근거다. 단일 03 문서와 지침을 함께 재검토한 최신 결과는 §3-I.12에 기록한다. 승인 상태→Repo/Owner→Network/계정/Secret→Data/App→IaC/Lifecycle→하위 시험→WBS/Cost/Freeze→통합 결과의 연결을 따라 대조했다. 수정이 있으면 직접 의존 문서뿐 아니라 삭제·재생성·복구·시험 시간/비용의 후속 영향도 다시 확인했다.

종료 조건은 같은 검토 범위를 수정 반영 후 다시 대조했을 때 추가 문서 보완/변경이 발견되지 않는 것이다. 모든 미래 결함이 없다는 보증이나 실제 환경 시험 성공을 뜻하지 않는다. 미확인 입력은 §3-I.6에 확인 책임·직접 의존 작업을 연결했고, 확인되지 않은 지원/가격/권한을 임의 값이나 PASS로 채우지 않았다.

#### 3-I.11.2 발견사항과 연쇄 반영

| 발견사항 | 원인·보완 | 연쇄 반영 / 재확인 |
|---|---|---|
| Data SG 본체/Rule 간 충돌 방지 조건 부족 | State별 Rule Owner만으로 inline Rule과 별도 Resource 혼용을 막지 못함. 혼용/전체 목록 덮어쓰기 금지 명시 | §3-B.9.7→§3-F.6/IM-03→3-G T19→본 문서 IM-03. foundation 재실행·Binding 해제·기반 Rule 보존·새 Worker SG 연결을 실제 구현 시험에 연결 |
| Gateway 복구 시험이 단절 확인으로 축약됨 | 3-B의 서비스/종단점 재구축·EIP/ENI/Route·vRouter/NAT·Source/거부·Key 교체가 통합 시험에서 불명확 | 3-G T14 / §3-G.4.1→3-H W08/Cost→통합 Runbook. 미재현 AZ/복구 시나리오는 미실행/제한, Gateway MTTR와 Offline RTO 후보를 구분 |
| 플랫폼 인증과 App 인증 시험의 경계 불명확 | IDP 신규 Login·기존 Session/Token·RBAC·Argo 권한, CI/Backup 제한을 T03의 세부 Case로 명시 | §3-C.9/13→§3-F.17→3-G T03 / §3-G.4.1→3-I 대응. IAM 사람 Admin 직접 호출 격리나 Team 제외만으로 기존 Session 즉시 폐기를 가정하지 않음 |
| Release 되돌리기 요구의 통합 연결 부족 | 3-F의 호환 Commit/Digest/설정·Sync 보류/재개를 Charter의 Rollback Should에 연결 | §3-G.4.2/T10 선택 Case→3-I 대응. Must Rolling/종료와 Should 수행을 구분하며 DB 자동 Rollback 주장 없음 |
| 이미 완료한 검토 준비의 미래형 표현 | 3-F~3-H에서 통합 검토본/시험 대응을 승인 후 작성할 것처럼 남김 | §3-F.20·§3-G.10·§3-H.9→현재 3-I 검토 결과/컨펌 대기로 정리. B01~B07 미승인과 실제 실행 조건 유지 |
| 보완 후 실행 순서의 재축약 | 여러 Gateway 세부 Case를 연결한 뒤에도 3-G Window B가 장애를 '한 번씩' 시험하는 표현을 유지 | §3-G.5를 필요한 세부 Case의 분리·순차 실행으로 수정. 3-H W08의 시간/재구축/재시험 비용 및 기존 두 Window의 목적 구분 재확인 |

SG 규칙 혼용의 주의사항은 [HashiCorp 공식 문서](https://github.com/hashicorp/terraform-provider-aws/blob/main/website/docs/r/security_group.html.markdown)에서 확인했다. 선택 Provider의 Schema/Plan/실제 Rule 동작까지 확인한 결과는 아니며 구현 Gate를 유지한다.

#### 3-I.11.3 반복 결과

| 회차 | 확인 범위 | 결과 / 후속 |
|---|---|---|
| R1 전체 대조 | 직전 검토와 3-A~3-H, 기준 원본, Owner/Lifecycle·계정·복구·시험·기간/비용 | 위 SG/삭제 시험·Gateway·플랫폼 권한·Should·상태 문구 보완 발견. 3-B·3-F·3-G·3-H에 반영 |
| R2 변경 영향 재검토 | R1 수정의 직접 의존→시험 세부 Case→Window/Cost→3-I 요약/상호참조 | '한 번씩' 실행 표현의 재축약과 3-I의 이전 상태/시험 요약을 보완. 새로운 Architecture/계정/성공 목표 변경은 없음 |
| R3 전체 재검증 | 수정본 전체의 승인 상태·Owner·삭제/재생성·Cloud/Offline·IF/IM/NET/Charter 대응·수치/Freeze/비용·문서 구조/원본 보존 | 추가 보완/변경 발견 없음. 정의한 문서 검토 범위에서 재귀 종료. 실제 환경 시험은 여전히 NOT RUN |

최종 대조에서 IF 18개·IM 9개·T 23개·Charter 성공축 12개의 문서 대응, Network NET-01~10의 조건별 연결, 문서 파일 참조/섹션 번호·표 열 구조·상하단 진행 체크를 확인했다. 제공 원본 네 문서는 검토 전후 SHA-256이 같아 변경되지 않았다. 당시 B01~B07과 전체03은 사용자 컨펌 전 상태였다. **당시 판정: 분야별 초안 문서화 및 문서 재귀 검토 완료, 당시 검토 범위의 추가 보완 없음, 사용자 최종 검토/컨펌 대기. 이후 단일 문서 통합 검토에서 발견한 보완은 §3-I.12에 별도로 반영했다.**

#### 3-I.11.4 당시 검토의 컨펌 범위

당시 사용자 검토 대상은 기존 작업 전제를 포함한 03 상세설계의 통합 결과, B01~B07의 제안·대안·조건, 당시 보완과 구현 Gate였다. 현재 승인 상태는 §3-I.12.2를 따른다. 일부 선택을 변경/보류하거나 B01~B07 승인과 전체03 최종 확정을 나누어 명시할 수 있다. 최종 설계 확정 후에는 해당 상태·인계를 일괄 정리한다.

문서 검토와 실제 검증은 구분한다. Source/계정/OCM 지원·Role/IDP·로컬 자산·가격/Credit·측정값은 여전히 확인 전이며 실제 HCL/Manifest 생성·validate/Plan/Apply·DB 이전·Cloud/로컬 시험·Cost Gate 통과를 이번 결과로 주장하지 않는다. 02까지의 조사→비교/초안→재검토→사용자 컨펌 흐름을 유지하고, 03 상세설계의 3-A~3-H 세부 절을 이 통합 결과에서 함께 검토한다.

### 3-I 남은 입력과 실행

- [x] B01~B07 작업 전제 승인·관련 상태 반영
- [ ] 사용자 전체03 재검토·통합 검토 결과 최종 확정
- [ ] 전체03 최종 컨펌 범위의 문서 상태·Runbook·구현/시험 인계 일괄 마무리
- [ ] 실제 Source/계정/도구/자산/가격 입력·Cost Gate 확인
- [ ] 실제 코드·실행 승인·생성/이관/배포·재생성/장애/복구/부하·Evidence
- [ ] 최종 Must 판정·잔존 비용/자료 보관 책임·Freeze/발표 준비

### 3-I.12. 단일 프로젝트 소스 통합 확인

Repository/Source부터 WBS/비용까지 3-A~3-H의 세부 설계와 3-I의 통합 검토를 한 문서에 옮겼다. 분야별 주요 절 118개의 내용을 대응시켰으며, 개별 파일 번호 안내/중복 탐색 문구는 현재 단일 문서 목차로 정리했다. 기술 비교·승인/제안 조건·Owner·검증 기준·수치·공식 근거를 요약 과정에서 생략하지 않았다.

통합 후에는 내부 절 번호와 다른 분야 참조, 상위 00/01/02/지침의 외부 절 참조, 공식 참고 자료 식별자, IF/IM/NET/T·WBS/Cost 대응을 재대조했다. 통합 과정에서 발견한 Redis 재사용 잔여 문구를 승인된 별도 새 Recovery Redis로 맞추고, Bootstrap 참조의 분야와 외부 Source 절 번호를 정리했다. 통합 당시에는 B01~B07 및 전체03 컨펌 전 상태를 유지했다. 이후 B01~B07 작업 전제 승인은 §3-I.12.2에 반영했다. 당시 전체03 컨펌 대기 상태와 구분한 최신 최종 컨펌은 §3-I.12.4, 팀원 사전시험과 실제 ROSA 시험의 경계는 §3-I.13을 따른다. $500/Freeze 조건은 유지한다.

문서 작성/통합과 원본 파일의 보존을 확인했으며 Project Source 등록을 직접 수행하거나 확인한 상태는 아니었다. 제공 원본과 기존 작업 기록은 변경하지 않았다. 이 문서는 전체03 컨펌 범위를 반영한 뒤 최종 등록본으로 사용할 수 있다.

#### 3-I.12.1 단일 통합본과 지침의 재귀 검토 결과

이 절은 B01~B07 작업 전제 승인 전의 검토 기록이다. 현재 승인 상태는 §3-I.12.2, 승인 반영본의 후속 재귀 검토 결과는 §3-I.12.3을 따른다.

**검토일:** 2026-10-01 KST  
**대상:** 직전 단일 통합본과 지침 개정본, 현재 제공된 00/01/02/지침 원본, 통합 전 분야별 작업 기록  
**검토 당시 판정:** 초안 문서화 및 문서 재귀 검토 완료. 수정 반영 후 동일한 문서/확인 가능한 근거 범위를 다시 대조해 추가 보완·변경이 발견되지 않아 검토를 종료했다. 전체03 최종 컨펌과 실제 환경 검증은 완료 전이다.

| 발견사항 | 수정과 연쇄 반영 |
|---|---|
| 옛 파일 번호가 남은 시험/통신/인계 참조 | T/IF/IM/NET 대응의 파일 번호를 같은 문서의 3-A~3-I 절로 정리. 기술 ID와 범위는 유지하고 관련 시험 Matrix·검토 요약·변경 기록을 다시 대조 |
| 상위 Target 절을 내부 절로 잘못 변환 | 3-F의 State/Backend/Owner 근거에서 `02_TARGET_ARCHITECTURE.md`의 §14~16·18~19를 외부 참조로 복원. 단순히 내부 대상이 존재하는지뿐 아니라 원래 참조 의미와 상위 원본 제목/내용을 확인 |
| 전체03과 3-A의 범위 혼동 | 전체 문서의 승인 상태·세부 분야 통합을 3-A 범위로 표현한 곳을 전체03으로 정정. 통합 승인표와 최종 컨펌 범위 재확인 |
| Bootstrap 표/본문의 원본 위치 불일치 | Subscription/필요 OperatorGroup의 Infra 설치 예외, GitOps의 Root/이후 Desired State, Operator 생성 객체의 Owner를 표·본문·3-F·지침 §14에 일치시킴 |
| Source 계보와 현재 상태 문구 | 00은 역사적 출발점, 승인된 01/02는 현재 상위 기준으로 정정. 작업 전제 승인·문서 검토 완료·사용자 컨펌·등록·실제 실행 상태를 3-A와 지침에서 분리 |
| 과거 인계/검토 결과가 최신 상태처럼 남음 | 3-E의 이후 별도 승인을 반영하고 '다음 문서'를 내부 절로 정리. 3-I.11의 통합 이전 검토 기록과 이 절의 최신 단일 문서 검토를 구분. Metadata/Evidence의 남은 실제 입력은 현재 Gate에 연결 |
| 지침 연결의 누락 | Bootstrap 설치 예외와 별도 Secret/Operator Owner를 지침에 연결하고 기존 10/22 Demo Freeze를 일정 요약에 추가. 새 설계 선택·계정·성공 목표를 추가하지 않음 |

| 회차 | 수행한 대조 | 결과 |
|---|---|---|
| P1 단일 통합본 전체 대조 | 내용 보존·내외부 참조·Owner 표/본문·Source 계보·승인/실행 상태→지침 | 참조 변환/범위·Owner·현재 상태의 보완 발견 및 두 파일에 반영 |
| P2 변경 영향 재검토 | 보완 항목→분야별 세부 요구/시험/인계→지침·일정→통합 판정 | 과거 3-E 인계와 문서/절 표현을 최신 승인 상태로 보완. Bootstrap 지침과 기존 Freeze 대응 반영 |
| P3 전체 재검증 | 수정 후 두 파일 전체의 상태·참조 의미/대상·Owner·수치/범위·상위 기준·원본 보존 | 추가 문서 보완/변경 발견 없음. 정의한 문서 검토 범위에서 재귀 종료 |

최종 대조에서 9개 분야 절, IF 18개·IM 9개·NET 10개·T 23개·WBS 10개·Charter 성공축 12개의 문서 대응과 코드 예시/공식 근거 링크 보존을 확인했다. 내부 절 대상·외부 상위 절·표 구조·상하단 진행 체크도 확인했다. 제공 원본 네 문서와 기존 분야별 작업 기록은 검토 전후 내용이 같으며 수정하지 않았다.

**프로젝트 소스 구성 결론:** 기존 00/01/02를 유지한 상태에서 상세설계는 이 단일 `03_DETAILED_DESIGN.md`, 진행 지침은 개정 `PROJECT_INSTRUCTIONS.md`를 사용하면 된다. 기존 분야별 작업 파일을 모두 등록해야 읽을 수 있는 의존성은 없다. 최종 승인 범위를 반영한 뒤 최종 등록본으로 정리하며, 현재 등록 완료를 주장하지 않는다.

실제 Source/Seed·계정/지원·권한·가격/Credit·로컬 자산·측정값과 코드/Plan/Apply·이관/복구/부하 시험은 확인/실행 전이다. 이 재귀 검토 당시 B01~B07은 제안 상태였다. 이후 작업 전제 승인 반영은 §3-I.12.2에 기록한다. 문서 검토 종료를 실제 적용 가능성·예산 충족·Runtime PASS의 보증으로 확대하지 않는다.

#### 3-I.12.2 B01~B07 작업 전제 승인 반영 기록

**승인일 / 근거:** 2026-10-01 KST, B01~B07 우선 승인과 반영 후 전체 재검토의 구분.  
**반영 범위:** 단일 `03_DETAILED_DESIGN.md`와 개정 `PROJECT_INSTRUCTIONS.md`. 기존 00/01/02·제공 지침 원본과 통합 이전 작업 기록은 수정하지 않음.  
**현재 상태:** B01~B07 작업 전제 승인·문서 반영 완료. 전체03 사용자 재검토·최종 컨펌 대기, WORKING DRAFT 유지.

| ID | 승인된 전제 / 상세 근거 | 직접 의존·연쇄 반영 | 남은 실제 확인 |
|---|---|---|---|
| B01 | 초기 버전·지원 조합 후보 및 고정/검증 방법 — §3-F.14 | Source/Tool Manifest·Provider/Bootstrap·Lock·Clean Recreate·가동시간 | 실제 계정/Region GA 패치·Catalog/CSV·Schema·CLI/도구·조합 검증 |
| B02 | SSE-S3 보호 Backend·개인 MFA→목적별 STS Role — §3-F.15 | IAM·State/Lock/Plan 보호·Bootstrap/복구·권한 시험 | 실제 Caller/Trust/Policy·Key·세션/Lock/복구 동작 |
| B03 | Classic Worker Role의 지정 ECR Pull·추가 Pull User 기본 제외 — §3-F.16 | IAM 계정표·공유 Role 영향·새 Node/지속 Pull·Harbor·시험/가동 비용 | 실제 Classic 지원/Role·Policy/ARN·캐시 없는 Pull·재생성 |
| B04 | Base/Overlay·Digest·CI→PR→Sync·App Sync 경계·Offline 예외 — §3-F.17 | Repo/Owner·Secret/Namespace·Release/Schema·보존 Bundle·Offline 시험 | 실제 Source/경로·Render·Digest/설정/Secret·Owner 인계·복구 동작 |
| B05 | 초기 Worker/Replica·PDB/분산/Rolling·Pool·Recovery 규모 — §3-F.18 | 다중 Pod 상태·종료 Pod 연결/자원·DB/Redis·부하·장애·비용 | 실제 Source의 상태 공유·측정 기반 Requests/Limits/Pool/Probe·수용량 |
| B06 | Must 시험 묶음·성능/재접속·Offline RTO/RPO 프로젝트 목표 — §3-G.2~7 | IF/IM/NET/T 대응·Harness/Data·Evidence·재시험·Window/Cost | 실제 Baseline/부하·업무 정확성·지연/오류·복구/Backup 실측. 모든 시험 NOT RUN |
| B07 | 네 트랙·목적별 두 Window·계획선/여유·Freeze — §3-H.2~7 | Owner/인계·WBS·재생성/실패 재시험·잔존 비용·일정 | 실제 사람 배정/가용일·Window 길이·가격/Credit/누적 비용·Cost Gate |

버전·규모 후보를 승인했다고 지원/구현 검증이 끝난 것은 아니다. B06 수치는 승인된 프로젝트 목표이며 운영 SLA·제품 보장이나 실제 달성 결과가 아니다. B07 계획선/여유 승인도 실제 비용 충족이나 추가 지출 승인을 뜻하지 않는다. 승인된 값·요구·시험 범위를 이번 상태 반영으로 완화하거나 새 선택을 추가하지 않았다.

**승인 반영 당시 문서 검증:** 승인 상태→분야별 본문/체크리스트→Owner·Release/복구→시험 목표/판정→WBS/비용→지침/전체03 상태의 연결을 대조했다. 이전 검토의 제안/미승인 표기는 당시 기록으로 명시하고 현재 승인 기록과 분리했다. 시험 식별자·코드 예시·공식 참고 링크·주요 버전/수치·상위 제공 원본 보존을 확인했다. 이 검증은 당시 승인 반영의 정합성 확인이며 당시 예정된 전체03 검토를 대신하지 않는다. 이후 연쇄 재검토와 보완은 §3-I.12.3에 기록한다.

당시 다음 단계는 승인 반영본 전체 검토 후 전체03의 최종 확정·변경·보류 범위를 기록하는 것이었다. B01~B07을 다시 작은 승인 단계로 나누어 묻지 않는다. 실제 구현·가격/지원 확인·Cost Gate·시험은 별도의 실제 상태로 기록한다.

#### 3-I.12.3 B01~B07 승인 반영본의 연쇄·재귀 검토

**검토일 / 범위:** 2026-10-01 KST, 승인 반영 결과에서 관련 근거·영향을 추적하고 새 보완/변경이 발견되지 않을 때까지 재검증.  
**범위:** 승인 반영본 전체의 상태/참조/시험 대응·코드 예시·수치·원본 보존, 변경 항목의 설계→Owner→구현→시험→WBS/Runbook/비용→지침 연결, 제공 00/01/02/지침 원본과 관련 공식 자료.  
**판정:** 아래 보완을 반영한 뒤 같은 문서 검토 범위를 다시 대조해 추가 보완/변경이 발견되지 않아 이번 재귀 검토를 종료했다. B01~B07 작업 전제 승인·전체03 사용자 최종 컨펌 대기·실제 시험 NOT RUN을 유지한다.

| 발견사항 | 보완 | 연쇄 반영 / 확인 |
|---|---|---|
| 단일 문서 안의 옛 파일 번호·범위 없는 참고 ID 잔여 | 계정/Secret·DB/App·Backup/Cost 참조를 3-C/3-D/3-H로 정리하고 PDB/배치 참고 ID를 해당 분야 ID로 연결 | 3-E IF 대응→3-F 입력/계정→3-G T/성공축→현재 승인표/지침. 코드/기술 ID·내용 보존 |
| 승인 전 제안 표현과 과거 검토/현재 상태의 경계 | B02 Backend·B04 Sync/Offline·3-H 인계 설명에 현재 작업 전제 승인을 반영. 이전 재귀 검토·승인 반영 확인은 당시 기록으로 명시 | Header/체크리스트→3-F/3-H→3-I.12.1~3. B 승인과 전체03 최종 확정/실제 실행을 분리 |
| Offline Owner 예외의 앞쪽 표/지침 연결 부족 | Cloud GitOps 최초 설치와 로컬 Offline Ansible 적용의 대상/목적을 구분. Recovery 선언 원본은 GitOps, 적용 객체는 복구 경로 하나로 관리 | §3-A.7→§3-F.6·17.3→T18/IM-08→지침 §14·27. Secret Owner와 기존 1차 자원 보존 |
| Prune 보류만으로 삭제 보호가 끝난 것으로 읽힐 여지 | 자동 Prune·수동 삭제·Application finalizer/연쇄 삭제·Namespace 삭제를 구분하고 선택 Argo 버전의 실제 동작을 구현 Gate에 연결 [3-F-R19] | §3-F.7/IM-06→3-G T03→3-I IM-06/Runbook→지침/격리 시험·시간/비용 |
| 상위 02의 CI Scan·Control Plane 진단이 통합 시험/인계에서 축약 | 기존 요구의 Scan 결과/정확한 Image·Digest 연결, 지원되는 플랫폼 상태·Operator/API/Log 진단과 관리책임 비교를 개별 Case로 연결 | §3-F.17→3-G T15/T21/T22→W03/W06/W08→Runbook/Cost→지침. 실제 도구/지원/권한/수행 여부는 확인 전 |
| 보완에 따른 범위·측정·비용 해석 | 기존 CI Scan 수행/결과 추적과 Charter의 추가 취약점 분석 Should를 분리. Warm DR·추가 실험의 미수행 사유를 기록하고 Gateway 실측과 Offline RTO를 구분 | 3-B T14 인계→§3-G.4.2→3-H 비용/실행 Ledger. 새 제품·수치 기준·고정 Window 시간·성공 판정 추가 없음 |

| 회차 | 수행한 검토 | 결과 |
|---|---|---|
| C1 승인 반영본 대조 | 직전 답변의 완료 주장→현재 B 승인/전체03 상태→상위 요구→Owner/삭제→시험/인계·지침 | 잔여 참조/제안 표현·Offline 예외 연결·삭제 보호·Scan/진단 대응 보완 발견 및 반영 |
| C2 변경 영향 재검토 | 보완된 Owner/시험→하위 IM 대응→Runbook/WBS/Cost→Charter Must/Should·실제 확인 경계 | IM-06 요약/통합 표 연결, Scan 수행과 추가 취약점 분석의 우선순위, 실제 도구/설정 미확인 구분, 시험 시간/비용 인계 보완 |
| C3 전체 재검증 | 수정본 두 문서의 승인 상태·내부 참조/공식 ID·표·하위 시험/상위 요구·채택 값·Freeze/예산·코드 예시·원본/작업 기록 보존 | 추가 문서 보완/변경 발견 없음. 같은 검토 범위에서 재귀 종료 |

주요 절 119개(기존 분야별 내용 118개+통합 확인 절)를 유지하고 IF 18개·IM 9개·NET 10개·T 23개·WBS 10개·B 선택 7개의 식별자를 보존했다. 승인된 버전/규모 후보·부하/성능·재접속·Offline RTO/RPO·IPAM·기간/Freeze·$450 계획선+$50 여유/$500 한도는 변경하지 않았다. 기존 코드 예시·공식 참고 URL은 유지하고 삭제 동작의 공식 참고 [3-F-R19]를 추가했다. 제공 원본 네 문서와 기존 분야별 작업 기록은 SHA-256 대조에서 변경이 없었다.

공식 자료의 공개 버전·Classic/HCP 정책 구분·S3 Lock 권한·Argo 삭제 동작을 재대조했으며, 이것을 실제 계정/Region의 지원 조합·Controller 설치·Role/Policy·가격/Credit·실행/시험 성공으로 확대하지 않는다. 남은 입력은 §3-I.6의 확인 책임/시점/직접 막는 작업과 연결한다. 검토 종료는 정의한 문서/확인 가능한 근거의 범위에서 추가 보완을 찾지 못했다는 뜻이며 미래 결함이나 모든 실환경 조건의 부재를 보증하지 않는다.

사용자 전체03 재검토·최종 컨펌은 여전히 남아 있다. 이번 결과로 새 B 선택이나 구축/삭제 실행 승인을 만들지 않으며, 상세설계는 단일 03와 개정 지침으로 계속 관리한다.

#### 3-I.12.4 두 문서 전체 최종 컨펌·등록 완료 반영

**기록 ID / 일자:** PH2-03-FINAL-CONFIRM-01 / 2026-10-01 KST.  
**근거:** 2026-10-01 두 문서 전체 최종 승인과 프로젝트 소스 등록 완료 보고.  
**범위:** 직전 제공한 `03_DETAILED_DESIGN.md` 전체와 개정 `PROJECT_INSTRUCTIONS.md` 전체. 별도 변경/보류 범위는 제시되지 않음. 승인 직전 03 SHA-256은 `dfae209fd0fc16e462fa59caa377a8cef0c96e51c11757b46895a2edfcd3f2f2`, 지침은 `b8c8eba1952e52759700f9b900681a54ee5964a1654dd278c69424252624368f`.

최종 컨펌 범위 반영은 WORKING DRAFT/최종 검토 대기였던 현재 상태를 승인된 설계 기준으로 변경하고, 분야별 승인 상태·W01·진행표·지침·구현 인계를 일치시키는 작업이다. 실제 값/지원/가격 검증·코드/Plan/Apply·Runtime 시험의 미확인 상태는 유지한다. 당시 소단계 승인과 과거 재귀 검토 이력은 당시 기록으로 보존한다. 기존 설계 선택·버전/규모 후보·시험 목표·$500 한도·Freeze를 이번 상태 반영으로 바꾸지 않았다.

프로젝트 소스 등록 완료는 등록 담당자의 직접 확인 보고를 근거로 기록한다. 별도 목록 조회·수정 또는 자동 동기화를 수행한 것으로 기록하지 않는다. 이번 승인 상태 정리와 추가 자료의 준비 기록을 작성했다고 이미 등록한 사본에 자동 동기화되었다고 주장하지 않는다. 상세설계는 계속 단일 03이며 추가 팀원 자료 전문을 새 필수 Project Source로 등록할 필요는 없다. `00/01/02`·제공 지침/가이드 원본과 통합 전 작업 파일은 수정하지 않았다.

최종 컨펌과 함께 후속 작업을 계속하라는 지시를 반영해 구현 준비를 진행한다. 새 실질적 선택이 없으면 재승인을 반복 요청하지 않는다. 실제 지원/Source/가격이 승인 기준과 충돌하면 해당 의존 작업을 보류하고 원인·대안·시험/비용 영향을 연결한다.

### 3-I.13. 추가 자료 대조와 실제 구현 직전 준비

#### 3-I.13.1 자료 분류와 확인 범위

현재 진행 현황:

- [x] 03·개정 지침 전체 최종 컨펌·프로젝트 소스 등록 완료 보고 반영
- [x] 추가 가이드 세 개와 Issue #1 본문/코멘트 대조
- [x] 보고 Commit의 DB/Redis 연결 코드·CI/Job 템플릿 읽기 전용 확인
- [x] 승인 설계 충돌·발견사항 11건의 후속 영향·시험·인계 정리
- [x] 네 hybrid Repo 존재·현재 공개 상태·기본 Branch Metadata 확인
- [ ] 실제 Seed·개인별 권한/팀 배정·base Branch/Overlay·GRANT·계정/도구/자산 Preflight
- [ ] 의존 작업별 코드 시작 조건과 첫 Full Apply 전 Cost Gate 확인

| 자료 | 분류 | 확인한 범위 / 사용 방법 |
|---|---|---|
| `1차 APP ROSA 이관 가이드.md` | TEAM DRAFT + SOURCE CONFLICT | 제공 전문 읽음. 실제 Source 경로·TLS/설정·Promotion 재사용 지점 참고. Jenkins 변경 없음·DB 위치 재선택·권한 그대로 복제·Ruleset 일시 해제는 자동 채택하지 않음 |
| `1차 YAML ROSA 이관 가이드.md` | TEAM DRAFT + SOURCE CONFLICT | 제공 전문 읽음. SCC·Route·Base/Overlay 수정 참고. TF 플랫폼/Secret 소유·Cloud Harbor Pull·Cloud Redis StatefulSet·Prune/Finalizer·Replica 예시는 승인03으로 대조 |
| `OCP 사전테스트 가이드.md` | TEAM DRAFT + PROVIDED CONDITION + SOURCE CONFLICT | 제공 전문 읽음. 공유 실습 환경의 사전검증 순서 참고. 실습 통과=ROSA 통과·대역 DB=RDS·Pod 재생성=GitOps SelfHeal·Prune 시험 필수로 해석하지 않음 |
| [hybrid-gitops Issue #1](https://github.com/seokpan/seokpan-hybrid-gitops/issues/1) 본문·결과 코멘트 | OBSERVED EVIDENCE — 팀원 수행 결과 보고 | API로 본문과 코멘트 두 개 읽음. 초기 본문은 진행 중, [결과 코멘트](https://github.com/seokpan/seokpan-hybrid-gitops/issues/1#issuecomment-5926003372)는 9개 통과/11건 발견/제약 보고. demo2 Runtime·원시 로그를 직접 재검증한 것은 아님 |
| 보고 Commit의 지정 Source·Repo Metadata | Source 조회 결과 | DB/Redis 코드와 CI/Job 템플릿·Commit·Repo Metadata만 읽기 전용 조회. 최신 전체 Source/개인별 권한/Ruleset·Seed·실행 결과 확인과 구분 |

이번 첨부의 `PROJECT_INSTRUCTIONS.md`는 전달 실패로 새 첨부를 읽지 못했다. 기존 제공/승인본이 작업 공간에 남아 있어 그 파일을 기준으로 개정했다. 새 첨부에 별도 수정이 있었다면 재전달된 파일을 대조한다. 접속정보·비밀번호/Key·DB URL 값을 가이드에서 추출해 Source/Evidence로 복제하지 않는다.

#### 3-I.13.2 출처·보고 결과·현재 Source 사실

사전시험의 App 출처는 [6fb8b75fed633769936ea206e8a88351eb062b9a](https://github.com/seokpan/seokpan-app/commit/6fb8b75fed633769936ea206e8a88351eb062b9a), Manifest 출처는 [d5e815992c69bf26a22fb72b29589fbb8cd8abc3](https://github.com/seokpan/seokpan-gitops/commit/d5e815992c69bf26a22fb72b29589fbb8cd8abc3)임을 Commit 조회로 확인했다. Manifest는 로컬 복사·변경한 ocp-lab Overlay이며 아직 Repo에 커밋하지 않았다는 보고다. 이 두 Commit은 사전시험 출처이고 2차 최종 Seed가 아니다. 실습 서버에서 별도로 빌드한 Image를 사용했으므로 기존 Harbor·미래 ECR·Recovery Image와 동일 Digest라고 추정하지 않는다. 인계 시 전체 Digest·Build/Overlay 개정·실행 시각·원시 결과를 연결한다.

| 사전시험 항목 | 팀원 결과 코멘트가 보고한 내용 | 승인03 후속 대응 / 한계 |
|---|---|---|
| SCC | backend/frontend/redis/Migration Job restricted-v2, 고정 runAsUser 대조군 거부 | T01·T03 및 실제 ROSA SCC/권한 재확인. 전체 Security PASS 아님 |
| 기동 | 전체 Running, 재시작 0 | T06·T10 정상 기동 준비. Cloud 3 Replica·다중 Pod 검증은 미실행 |
| Migration | current→upgrade-head, 2 revision/8 table, 실습 빈 DB 승인 코멘트 | T05. 운영 Data 이전·RDS 지원 권한·Rollback/Backup 검증과 구분 |
| DB TLS/ready | Pod 내부 ready 200, DB/Redis 연결 포함 | T04·T06. TLS 결과는 대역 DB/테스트 CA 조건이며 실제 RDS/ElastiCache는 미실행 |
| Redis AOF | appendonly yes, 실습 NFS PVC에 AOF 기록 | 실습 Redis 저장 확인. ElastiCache HA·진행 게임 보존·Offline RPO 결과로 사용하지 않음 |
| Redirect | HTTP→HTTPS 302 | T07의 HTTPS 전환·목적지/보안 확인. 기존 301과 차이를 기록 |
| 경로/게임 | FE/API 라우팅·게임 한 판 완주 | T06의 참고 Case. 없는 API/WS·SPA 오류·동시 업무는 별도 |
| WebSocket | rooms/chat/lobby/presence 101, 1.6분 유지 | T09 사전 관측. 유휴·긴 게임·Heartbeat·단절/재접속·부하 목표 미검증 |
| 자동 복구 | backend Pod 삭제 후 재생성/Ready | Deployment 기본 동작 확인. Argo SelfHeal·Worker/AZ/DB/Redis 장애·무중단 증거로 확대하지 않음 |

실습 DB 계정 권한은 1차보다 넓은 임시 권한이고 대역 MariaDB에는 PVC가 없어 재시작 시 데이터 유실 가능하다는 보고다. DB 권한 시험/복구 증거로 재사용하려면 제한된 목적별 GRANT와 Storage/데이터 조건을 맞춰 다시 검증한다. 실습 GitOps Operator 1.22.0 설치 보고는 lab 조건이며 ROSA GitOps 1.21.4 후보를 교체하지 않는다. 5단계의 대체 DB 호스트 시나리오와 6단계의 Argo는 보류/미실행 보고다. 실제 RDS/ElastiCache·ECR·ROSA 최종 T 시험은 NOT RUN이다.

지정 App Commit의 `backend/src/seokpan/persistence/mariadb/connection.py`는 허용 Host/Port/DB를 상수와 비교하고 TLS 기본 검증을 사용한다. 같은 Commit의 `backend/src/seokpan/persistence/redis/connection.py`는 고정 Service Host/Port/DB·redis 스킴만 허용하며 URL 인증정보를 거부한다. 이 Source 범위에서 RDS/ElastiCache 이관의 연결 설정 변경이 필요함을 확인했다. 아직 새 설정 코드를 작성하거나 실제 서비스에 연결하지 않았다. 설정 외부화 시 URL의 임의 대상/옵션을 무제한 허용하거나 TLS 검증을 끄는 방식으로 해결하지 않는다.

같은 Commit의 `Jenkinsfile.image-pipeline`에는 Harbor 후보 Build·Trivy Scan·Health Smoke·Digest 검증·Metadata 기록·GitOps PR 코드가 있다. Source 코드의 기존 정책은 CRITICAL 또는 수정 가능한 HIGH가 있으면 승격 차단하는 방식이다. 이는 발견한 기존 코드 조건이며 이번에 새로운 취약점 목표/Should→Must 승격을 결정한 것이 아니다. 실제 Jenkins/Trivy 설치·인증·실행 결과·스캐너 DB 개정은 미확인이다. ECR Push/Cloud Pull·Harbor Recovery 보존·2차 경로/권한의 변경이 필요하므로 가이드의 “Jenkins 변경 없음”을 채택하지 않는다.

네 Repo Metadata는 2026-10-01 조회에서 모두 존재·public·기본 Branch main·archived=false였다. 조회 연결 주체에는 pull/push/admin이 표시되지만 팀원 네 사람의 권한을 확인한 것은 아니다. Repo size만으로 빈 저장소 또는 Base 완료를 판정하지 않는다. Branch 보호·Tree·열린 PR·실제 Code·Docs 반영 상태는 미확인이다. Project 소스 등록 완료 보고와 GitHub Docs 반영 완료는 별개다.

#### 3-I.13.3 발견사항 11건의 연쇄 영향과 처리 조건

아래 번호는 결과 코멘트의 1~11을 그대로 연결한다. 보고 내용은 해당 실습 조건의 관측이며 Renderer/버전·정책의 보편적 사실로 확대하지 않는다. 담당은 승인된 A~D 트랙이며 새 사람 배정은 하지 않았다.

| 번호 / 발견 | 처리·인계 조건 | 직접 의존 → 후속 시험·WBS |
|---|---|---|
| 1 Redis 고정 Host/Port/DB/스킴·인증 거부 | B가 설정/검증·Redis Client 계약을, C가 승인된 TLS+AUTH/Primary Endpoint·CA/Secret 참조를 대조. Cloud/Recovery/lab 설정을 분리하고 잘못된 대상/CA/인증·출력 노출 실패 Case 준비 | 3-C·3-D·3-E→B04 Release/Secret·T03/T04/T06/T13/T18·W02/W03/W06. Host 외부화만으로 완료 아님 |
| 2 DB Host 고정·수정 Branch 없어 대체 Host 시험 보류 | B·C가 Runtime/Migration 모두 같은 승인 대상/CA 규약을 사용하도록 변경 범위 준비. DB명/목적별 User 검증·1차 기본 동작·TLS Hostname 보호 유지 | 3-D Seed/Schema/권한→T04/T05/T06/T12/T18·W02/W03/W06. 실습 다른 Host 성공도 실제 RDS PASS 아님 |
| 3 runAsUser 삭제 후 SCC 통과, runAsGroup 유지 가능 보고 | B가 실제 FE/BE/Job의 UID/GID·파일/쓰기 경로·SCC를 확인. 가이드의 두 필드 일괄 삭제·GID 항상 0을 일반 규칙으로 확정하지 않음. 불필요한 SCC 권한 확대 없이 최소 수정 | Base/이미지→D 재빌드/Scan·T01/T03/T06/T21·W03. 선택 Dockerfile 수정은 필요 근거가 있을 때만 |
| 4 Base의 Harbor Pull Secret과 lab/ECR 인증 경로 문제 | B·D가 환경별 Pull 참조를 대조. Cloud ECR는 B03 Worker Role, Recovery는 Harbor, lab는 실제 사용 Registry로 분리. 잘못된 Secret의 Event/매칭/캐시를 확인하며 모든 Pull Secret이 항상 ECR 인증을 막는다고 단정하지 않음 | B03/B04/Secret 공급→캐시 없는 새 Worker/지속 Pull/재생성 T21·T14/T19·W03/W06 |
| 5 테스트 CA의 keyUsage 누락과 엄격 검증 실패 | lab 인증서 확장/SAN·Python/OpenSSL 실제 버전·검증 결과 인계. B·C는 Runtime/Migration의 실패 원인을 보호된 진단으로 확인. 테스트 CA 예시를 RDS CA로 사용하거나 TLS 검증을 완화하지 않음 | CA Bundle/Artifact→T04/T05/T18·W03/W04/W06. 특정 확장 한 개만 추가하면 모든 인증서가 유효하다고 주장하지 않음 |
| 6 CA subPath 마운트의 교체 반영 | B·C가 Config/CA 개정→계획된 Pod 교체→새 TLS 연결까지 확인. [ConfigMap 공식 설명](https://kubernetes.io/docs/concepts/configuration/configmap/)의 subPath 업데이트 미반영과 연결. 변경 실패 시 기존 유효 CA/Release 보호 | B04 Release/B05 Rolling·Secret 교체/Job 새 실행→T03/T04/T10/T18/T19·W03/W06. ConfigMap 수정만으로 적용 완료 아님 |
| 7 FE Prefix /로 없는 경로도 FE 응답 | B가 실제 App Path/Route를 확인하고 SPA 경로·없는 API/WS·잘못된 Prefix·오류 응답을 분리한 Case 준비. 정상 FE HTML로 API/WS 오류를 숨기지 않는 기존 IF-02 요구 유지 | 3-E IF-01/02·Route→T06/T07·W03/W06. 없는 모든 FE 경로의 1차와 동일 응답을 새 요구로 추가하지 않음 |
| 8 Redirect 301→302 관측 | B가 상태 코드 차이와 HTTPS Location/Host·Origin·Proxy·인증 Cookie를 함께 확인. 가이드의 301 고정 기대를 단순 성공 기준으로 복제하지 않음 | 3-E IF-03→T07·T22 비교·W03/W06 |
| 9 lab 1 Replica+PDB minAvailable1의 drain 제약 | lab Overlay에서 필요한 PDB 조정을 확인. [PDB 공식 설명](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)의 자발적 Eviction 한계와 연결. Cloud B05 3 Replica/PDB minAvailable2 후보를 lab 이유로 제거하지 않음 | B05 배치/Rolling·Recovery1 Replica 차이→T10/T11/T18·W03/W06/W08 |
| 10 외부 /health/ready가 FE로 라우팅 | B가 backend Pod 내부/Service 대상에서 Ready·DB/Redis 조건을 확인하고 실제 Kubelet Probe와 공개 Route 업무 Probe를 구분. FE200을 backend 준비 성공으로 사용하지 않음 | 3-E Probe·Route/IF-04→T04/T06/T10/T15·W03/W06 |
| 11 generateName Migration Job의 기존 적용 경로 | 지정 Manifest Commit 템플릿은 one-shot 실행 대상이라고 명시됨을 확인. B·C가 Render→대상/Action/Schema/Image/승인 Ref 확인→단일 실행→결과 인계를 준비. 상시 App 자동 Sync나 SelfHeal로 Schema 변경을 반복하지 않음. “Kustomize에서 언제나 불가”는 일반 결론으로 채택하지 않고 실제 선택 Renderer 동작을 확인 | 3-D Schema·Release·DB 권한/Backup→T03/T05/T19·W03/W06. 빈 값 아닌 승인 Ref도 실제 승인/대상 근거를 사람이 대조 |

공통으로 D는 해당 결과/수정 Commit/Image/Manifest·설정 개정·실패/제한을 Evidence Index에 연결한다. 아직 Image Scan 재실행·Render/서버 검증·GRANT 시험·ROSA 시험을 수행한 것으로 표시하지 않는다. WebSocket 1.6분은 관측된 길이일 뿐 장시간 설정 검증이 아니다. 가이드의 `timeout: 1h` 한 줄을 그대로 고정하지 않고 선택 Router의 연결/터널 Timeout·Heartbeat·유휴/긴 게임·재접속을 기존 T09에서 확인한다.

#### 3-I.13.4 담당 트랙·인계 묶음·구현 시작 조건

Base와 lab Overlay 인계는 Cloud 생성보다 먼저 준비할 수 있다. B App/GitOps 트랙이 Base의 실행 Owner를 확인하고, 팀원의 로컬 Overlay를 Commit 가능한 선언으로 받을 책임을 갖는다. 현재 실제 작성자/Reviewer·PR Branch는 확인 전이며 사람을 임의로 지정하지 않는다. 팀원이 Branch만 push되면 Merge 전 Argo 검증이 가능하다고 요청한 것은 실습 검증 제안이다. 실제 Branch/Commit을 받은 후 lab Application만 해당 개정으로 고정하고 공유 환경 책임·Secret·Namespace·Sync/삭제 경계를 확인한다. Cloud Application을 실습 Branch에 연결하거나 PR Merge를 자동 승인하지 않는다.

| 트랙 / 준비 묶음 | 필요한 입력·준비 결과 | 막는 작업 / 다음 인계 |
|---|---|---|
| A Infra/Hybrid | 실제 계정/서울 Region·Quota/ROSA Classic·Caller/MFA·Controller/Tool·IPAM 충돌·DataVM/로컬 자산·세 Root Owner와 제한 Output | 계정/지원·정책 입력은 해당 TF 구현/Plan/Apply를 막음. Base/Case·App 변경 범위 준비는 계속 가능 |
| B App/GitOps | 실제 Seed 전 Source 조사·Base 담당/Reviewer·PR Branch/Commit·ocp-lab Overlay·Path/Health/설정·SCC/Pull/Route/Job 수정 범위 | Source를 수정하기 전에 실제 Seed·이력/대상 Repo 충돌 처리 확인. Base 공통 부분과 Cloud/lab/Recovery 값을 분리해 A/C/D에 참조/인계 |
| C Data/Recovery | 1차 GRANT(비밀번호 제외)·목적별 Runtime/Migration/Backup 권한·RDS 제약 대조·CA·Schema/Data/Backup·로컬 Storage/독립 DB/새 Redis | 임시 넓은 권한을 실제 RDS 권한으로 복제하지 않음. GRANT 확인/제한 시험은 DB 권한 판정·실제 이전을 막지만 Secret 참조/Case 준비는 가능 |
| D CI/Registry/Evidence | 실제 Jenkins Job/Agent·Trivy 실행/기존 정책·ECR/Harbor 인증·Artifact/Digest Mapping·PR 대상·Release/Evidence 형식·Cost 입력 | 1차 Pipeline의 Harbor 고정 경로를 보존용과 Cloud Push로 나눌 변경 범위 인계. 코드 존재만으로 CI/Cloud Pull 성공 처리 안 함 |

실행 기록의 기본 필드는 기존 WBS Ledger의 `작업 ID / 담당·Reviewer / 선행 / 입력·Code 개정 / 상태·Blocker / 결과·Evidence / 직접·후속 영향 / 예상·실제 시간·비용 / 다음 인계`를 사용한다. Release는 §3-A.8·§3-I.7의 App/Infra/GitOps SHA·Image Digest/플랫폼·Schema/Config/Secret 개정·Backup/Tool/Evidence를 연결한다. Evidence 저장 형식/대용량 위치는 실제 도구·보관 책임을 확인해 이 기존 필드를 채우며 새 서비스나 Repo를 임의로 추가하지 않는다.

| 진입점 | 시작 전에 필요한 확인 | 현재 상태 / 경계 |
|---|---|---|
| 코드 작업 시작 | 해당 대상 Repo/Branch·개인별 권한/리뷰·입력 Source/Seed·Owner·참조/Secret 경계. App Seed는 실제 이관 직전 Latest Validated State의 전체 SHA/미반영 Maintenance 확인 | Repo Metadata·보고 Source 일부 확인, 실제 팀 배정/Branch/Seed 확인 전. AWS 모든 입력이나 Cost Gate 완료를 Base 준비의 필수 선행으로 만들지 않음 |
| lab Argo 검증 | Base/Overlay Branch·전체 Commit·실습 Context/Namespace·공유 Operator 사용 책임·필수 Secret·단일 관리 Owner·Prune/삭제 보호 | Base 인계와 실제 lab 상태/권한 확인 전. 1차 GRANT로 제한한 DB 재시험은 별도 미완료로 기록. Cloud Acceptance 아님 |
| TF Validate/Plan | Root별 코드·정확한 Provider/Lock·입력/Caller/Backend 보호·실제 지원 Schema·읽기 권한·민감 Plan 보관 | 코드/Controller/인증 미확인. Plan 검토와 자원 생성/변경을 구분 |
| 첫 Full Apply / 유료 가동 | 승인 Scope·검토된 실제 Plan/삭제 경계·계정/Quota/지원·팀 실행 Owner·Secret 초기화·실제 가격/Credit·누적/잔존·Window 길이·실패/재시험·정리 비용으로 Cost Baseline Gate | 실제 입력·계산·Plan 미확인. $450 계획선/$50 여유/$500 한도 유지. 단가/고정 시간/Cost PASS를 만들지 않음 |

실습 `seokpan-app`는 팀원이 6단계까지 유지할 계획이라고 보고했다. AI가 유지 기간/삭제일을 새로 확정하거나 Project를 삭제하지 않는다. 정리 전 미커밋 Overlay·Image/Source/Digest·원시 결과·필요한 인계 보존, 공유 사용 종료 확인, 대상 확인과 Secret/테스트 CA·Key 정리를 담당자가 수행한다. 실습 결과를 보존했다고 기존 1차 자원을 정리 대상으로 포함하지 않는다.

기존 $450 계획선·$500 한도·Technical Freeze 10/16·Validation 10/19~21·Demo Freeze 10/22·Presentation Ready 10/23·최종 10/26은 유지한다. 이번 자료로 드러난 App/CA/Pull/Job/GRANT·Base/Argo 인계·재시험 소요를 W02/W03/W06~08·기존 실행/Cost Ledger에 반영한다. 실습 준비를 AWS 비용 없이 한다는 보고만으로 팀 시간·보관 비용 또는 후속 ROSA 가동 비용을 0으로 처리하지 않는다. 실제 남은 소요/가용일이 기존 계획과 충돌하면 그 작업과 영향만 다시 산정한다.

#### 3-I.13.5 연쇄 검증과 구현 직전 남은 작업

최종 컨펌→Header/분야별 상태/W01/지침→보고 Commit/실습 조건→11건 발견→Owner/Secret/Release/Job→T/IF/IM→WBS/Cost/정리 인계→현재/과거 기록을 연쇄 대조했다. 1차 Source SHA와 실습 Image/Overlay·2차 Seed를 구분했고, 9개 통과 보고와 ROSA NOT RUN을 분리했다. 실제 GitHub Source/Repo 읽기 조회를 미조회로 남기지 않도록 현재 상태를 갱신했다. 가이드 전문·민감값·제공 원본과 기존 공식 URL/코드 예시는 복제/수정하지 않았다.

재검토에서 Issue 본문의 진행 중 결과와 후속 코멘트, Job의 단발 실행 경계, 실습 PDB와 Cloud B05, Trivy 코드 존재와 실제 실행, 현재 public Repo와 개인별 권한을 다시 대조했다. 첫 대조에서 남은 IAM/Data/시험 준비표의 과거 컨펌 상태와 일부 Source 미조회 표현을 보완했고, 두 번째 대조에서 두 문서의 현재/이력·표·내부 참조·기존 URL/코드 예시·승인 값·원본 보존을 검증했다. 수정본 기준으로 추가 문서 보완/변경을 발견하지 못해 이번 문서 검토 범위의 재검증을 종료했다. 기존 119개 주요 절은 보존하고 준비 절 하나를 추가했으며 IF18·IM9·NET10·T23·W10·B7 식별자와 버전/규모·성능/복구·IPAM·Freeze/예산 표를 보존했다. 제공/참고 원본과 통합 전 기록 17개 파일의 SHA-256이 변경되지 않았다. 문서 확인을 실제 Render/Validate/Apply·Runtime PASS로 확대하지 않는다.

남은 작업 — 실제 구현 단계 직전:

- [x] 전체03·지침 최종 컨펌·승인 상태·등록 완료 보고 반영
- [x] 추가 자료와 Issue 11건의 영향·재검증·담당 트랙·인계 조건 정리
- [ ] 실제 작업자/Reviewer·개인별 Repo 권한/Branch 보호·Base PR Branch/Commit 및 ocp-lab Overlay 확보
- [ ] App 이관 직전 최신 검증 Source·전체 Seed SHA·미반영 Maintenance·대상 Repo 이력 충돌 확인
- [ ] 1차 GRANT·실제 CI/도구·계정/지원·주소/자산의 필요한 입력 확인
- [ ] 준비된 작업부터 코드 시작 조건 확인, 첫 Full Apply 전 실제 Cost Baseline Gate 확인

현재 끝난 것은 설계 최종 승인 반영과 확인 가능한 추가 자료의 준비 인계다. 실제 입력이 없는 의존 작업은 미완료로 유지하며 그 밖의 독립 준비를 중단시키지 않는다. 새 선택이 없는 완료/입력 확인을 작은 재승인 단계로 만들지 않는다.

<a id="recovery-design-review-20261003"></a>
### 3-I.14. 복구 목표 피드백에 따른 설계 재검토 — 2026-10-03

**2026-10-03 검토 이력:** 아래 §3-I.14.1~3의 새 목표 미확정은 당시 상태다. 현재2026-10-05의 설계 결정·근거/판정은 [§3-I.14.5](#recovery-design-decision-20261005)를 우선한다. 당시 상태는 설계 정합 보완·선택 근거 정리 / 새 목표·주기·구조 변경 미확정이었다. 시작점은 `architecture/exports/10-backup-offline-recovery.png`의 RTO 30분·RPO 90분에 대한 강사의 사용자 관점 피드백이다. RTO 5~10분은 검토 의견이며 RPO 숫자나 전체 인터넷 사용자 전환은 새 Must로 채택되지 않았다. 사용자는 특정 숫자를 먼저 정해 구현을 맞추지 않고, 가능한 품질·편의성·네 사람의 구현/학습/운영 부담·일정·비용·설계 정합성·발표 준비를 함께 비교하도록 요청했다. 최초 AI의 10분/15분/5분 우선 권고와 근거 없는 2+3+3+2분 시간 예산은 철회된 후보로 취급한다.

#### 3-I.14.1 현재 확인한 설계와 필요한 보완

| 대상 | 현재 판단 / 지금 반영할 내용 | 아직 확인하지 못한 내용 |
|---|---|---|
| 정상 Cloud DB·Redis HA | RDS MariaDB Multi-AZ와 ElastiCache Multi-AZ 유지. Cloud 내 장애 회복과 온프레미스 백업 복원 목표는 별개 | 해당 조합의 실제 사용자 업무 회복·미확정 쓰기 영향 |
| Portable Backup | Data VM→RDS 논리 덤프/암호화→S3→로컬 완성본, 독립 보호 사본 유지. 주기만으로 RPO를 보장하지 않음 | 실제 Data 시각·완성본 확보 지연·실패 후 사용 사본·부하/공간/전송 |
| 온프레미스 복원 | 후속 04의 새 전용 MariaDB VM 직접 TLS·별도 새 Redis·로컬 보존 Image/Manifest/Secret/도구 유지. 02의 기존 1차 Redis 재사용 구문은 이 승인 기준에 정합화 | Host 여유·독립 사본/Key 가용성·실제 Import/App 기동·예비 담당자 실행 |
| RTO 성공 경계 | §3-D.9.8을 §3-G.7/04 §10.2의 장애 시작→탐지/판단→접속 안내/지정 클라이언트 업무·Data 완료에 정합화 | 전체 시간선, 시계/시점 불확실성, 반복·경계 조건의 여유 |
| 사용자 범위 | 지정 클라이언트의 접속/재로그인·랭킹/회원 누적 기록·새 게임 진행/완료와 현재 방 결과, 기존 완료 DB 기록의 SQL/데이터 확인 필수 — §3-I.14.4. Public 자동 DNS/전체 트래픽 자동 전환 제외와 구분 | 실제 위치·주소·HTTPS/WSS·도달성·처리 규모와 허용 중단/손실. 새 Redis에서 과거 개별 결과 HTTP/화면은 기존 기능으로 보장하지 않음 |

Infra [#17 사전 점검](https://github.com/seokpan/seokpan-hybrid-infra/issues/17)은 데이터 규모·객체·행 수의 입력이고 [#19](https://github.com/seokpan/seokpan-hybrid-infra/issues/19)는 Data 인프라 코드/권한 준비다. 2026-10-03 읽기 재확인에서도 이 보고를 전체 Dump/Restore·업무 재개 실측으로 사용하지 않는다. 현재 `evidence/`에는 안내와 빈 양식만 연결돼 있으며, 이 저장소에서 이번 판단에 사용할 실제 Run은 확인되지 않았다. 팀원의 외부 시험까지 없다고 단정하지 않는다. App/Manifest 검사 통과도 실제 복구·팀 부담의 증거를 대신하지 않는다.

#### 3-I.14.2 대안 비교와 구조 변경 조건

| 대안 | 효과와 필요한 근거 | 현재 선택 상태 |
|---|---|---|
| 기존 30분·90분·1시간 유지, 범위 설명 보완 | 추가 변경이 작음. 실제 중단/회원·완료 게임·Rating 유실이 허용 범위에 맞고 실행 조건이 현실적인지 필요 | 유지 중인 기준이며 적절성 결론은 대기. 기존 값이라는 이유만으로 방어하지 않음 |
| 현 복원 구조의 사전 준비·필수 스크립트·인계 개선 | 실제 병목의 수작업/준비 대기를 줄일 수 있음. 기존 W04 작업에서 소요·사용 편의·예비 담당 실행과 오류/재시험 부담 확인 | 먼저 조사할 최소 변경. 전 과정의 새 자동화 사업이나 추가 Cloud 서버를 선행하지 않음 |
| 백업 간격/전송·최신성 관리 조정 | 영속 Data 손실 구간을 줄일 가능성. 실제 성공 사본 간격·로컬 확보 지연·부하·보관·실패 처리를 대조 | 주기 숫자는 미확정. 모든 후보를 구현해 비교할 필요 없음 |
| 사전 복원 갱신·지속 복제/Warm Standby·실제 서비스 전환 | 현재 경로로 필요한 중단/손실/접속 범위를 충족하지 못할 때 검토. 동기화·승격·양쪽 쓰기 방지·복귀·접속·추가 운영/시험 책임 필요 | 필수 요구와 현재 경로의 부족이 확인될 때만 비교. 기본 범위에 추가하지 않음 |

RTO는 전체 시간선을, RPO는 실제 사용 사본의 Data 시각을 별도로 판단한다. 정상적으로 성공이 이어지는 경우에도 **성공 사본 Data 시각 사이의 최대 간격 + 그 시각부터 로컬 사용 가능한 완성본까지의 최대 지연**을 확인해야 한다. 누락/중복 실행 생략·VPN/Data VM/Storage 중단·최신 사본 복원 실패에는 이 정상 경로 계산으로 RPO 상한을 보장하지 않는다. 경고와 재시도가 미달 자체를 없애지는 않는다. Cloud가 정상인데 VPN만 끊긴 경우 로컬을 쓰기 서비스로 전환하지 않으며 격리 예행과 실제 전환을 구분한다.

비용은 실제 암호문 크기·운영 시간·주기별 건수·7일/보호/버전 사본·임시/복원 공간·S3 요청/전송·DB 부하·추가 Cloud 가동/재시험·정리 지연을 기존 I07/§3-H 산식에 연결한다. 팀 부담은 구현뿐 아니라 학습·사용/유지·실패 처리·인계·재시험·문서/SVG/PNG·발표 준비를 네 사람의 실제 가용시간에 대조한다. 가용시간과 가격이 없으므로 추가 비용 0·며칠 내 완료처럼 임의 수치를 넣지 않는다. $450 계획선/$500 한도·10/16 Technical Freeze·10/22 Demo Freeze·10/23 Presentation Ready는 유지한다.

이 판단 방식의 공식 근거는 [AWS REL13-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.html)과 [DR 전략 비교](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)다(2026-10-03 확인). 업무 영향과 기술·자원 제약을 함께 조정한다는 원칙을 참고하며, AWS의 Cloud 전략별 예시 수치를 이 온프레미스 경로의 보장으로 옮기지 않는다.

#### 3-I.14.3 최소 실행과 설계 변경의 순서

1. **설계 보완은 지금 수행:** 위 Redis·RTO/사용자 범위를 02/03/04와 대조한다. 00의 역사적 출발점과 01의 목적·예산·Freeze는 유지하고, 프로젝트 Scope/성공 기준까지 실제로 바뀔 때만 해당 상위 문서를 개정한다. 기존 문서 종료는 재검토 금지가 아니다.
2. **부족한 근거만 기존 W04 예행으로 확보:** C의 Backup/도구·격리 DB, B의 App/새 Redis·클라이언트 계약, A의 Host/로컬 자산, D의 시간선/비용·부담을 연결한다. 필요한 입력은 [05 §9.2~9.6](../execution/05_IMPLEMENTATION_AND_VALIDATION.md#recovery-objective-review-20261002)에 이미 정리돼 있다. 가용한 격리 로컬/OCP·대역 DB 예행은 먼저 할 수 있으며 전체 Cloud/ROSA 구현·05 최종 종료를 선행조건으로 묶지 않는다. 실제 RDS Backup/승인 Release를 사용하는 최종 T18과 조건 차이는 남긴다.
3. **측정과 필요성을 함께 비교해 선택:** 전체 시간선·Backup 로컬 확보/손실·지정 클라이언트 업무·편의/팀 부담·비용/Freeze를 대조한다. 실측은 가능성의 근거이며 가장 빠른 결과에 목표를 맞추지 않는다. 목표 미달 뒤 같은 Run의 기준을 낮춰 PASS로 바꾸지 않는다.
4. **채택된 변경만 함께 반영:** 새 목표/주기/구조가 결정되면 02 상위 경계, 03 Data/시험/WBS·Cost/결정, 04 준비/Runbook, 05 실제 Source/Run·Tracker, 코드·그림 생성 원본/영향 SVG/PNG·발표 참조를 동일 변경으로 갱신한다. 기존 승인/Run은 보존한다.

현재 그림10은 별도 새 DB/Redis와 전체 업무·접속 확인 및 미달성 목표를 이미 표현한다. 이번 정합 보완으로 경로·숫자가 바뀌지 않으므로 SVG/PNG 내용을 불필요하게 재생성하지 않는다. 출처 Manifest만 현재 문서 개정과 연결하고, 새 값은 채택 후 반영한다. Cloud·ROSA/App 품질 구현과 전달 이력은 유효한 별도 프로젝트 작업으로 보존하되 이번 설계 판단보다 우선하는 안내를 05/Tracker에서 바로잡는다.

- [x] 원문 두 요청·승인 설계·후속 Source의 범위 대조, 즉시 정합 보완과 구조/수치 결정 구분
- [ ] 실제 예행/최신성·손실·접속·팀 부담/비용 근거 확보
- [ ] 사용자 영향과 제약을 대조한 목표·변경 범위 선택 및 채택 내용 반영

<a id="recovery-app-scope-20261005"></a>
#### 3-I.14.4 새 Redis 복구의 완료 기록·사용자 기능 경계 — 2026-10-05

공개된 h-app main `c12b3d15a4dd2c806fac4326a9eb30ed6e8a81b3`의 [GameApplicationService.get_result](https://github.com/seokpan/seokpan-hybrid-app/blob/c12b3d15a4dd2c806fac4326a9eb30ed6e8a81b3/backend/src/seokpan/game/application/service.py), [MariaDB Game Adapter](https://github.com/seokpan/seokpan-hybrid-app/blob/c12b3d15a4dd2c806fac4326a9eb30ed6e8a81b3/backend/src/seokpan/persistence/mariadb/game_adapter.py), [Frontend GamePanel](https://github.com/seokpan/seokpan-hybrid-app/blob/c12b3d15a4dd2c806fac4326a9eb30ed6e8a81b3/frontend/src/game/GamePanel.tsx)와 [Frontend Routes](https://github.com/seokpan/seokpan-hybrid-app/blob/c12b3d15a4dd2c806fac4326a9eb30ed6e8a81b3/frontend/src/App.tsx)를 대조했다. 개별 결과 조회는 DB의 저장 Game/Result를 읽지만 먼저 현재 Redis Participation/Room을 확인하고 요청 Game이 현재 방의 현재/마지막 Game인지 제한한다. 현재 화면 경로에도 별도의 과거 개별 게임 이력 조회 UI가 확인되지 않았다. 이 확인은 Source의 기능·권한 계약이며 실제 Recovery 배포 PASS가 아니다.

| 복구 검증 대상 | 기존 Source와 정합한 완료 기준 |
| --- | --- |
| 백업에 포함된 과거 완료 Game/Move/Result/Rating | 복원 DB의 Schema·행/관계·대표 기록/비민감 비교로 보존 확인. 오래된 Game의 개별 결과 API/화면이 새 Redis에서 복구됐다는 주장과 구분 |
| 지정 클라이언트의 업무 재개 | 새 Redis에서 재로그인하고 기존 랭킹/회원 누적 기록 확인, 새 방/게임의 진행·완료와 현재 방의 결과 조회를 해당 실행 조합에서 확인 |
| 기존 세션·진행 게임 | Redis Runtime 손실/중단을 별도로 기록. 완료 결과·승패/Rating을 임의 생성하거나 기존 Room 상태를 DB만으로 재구성했다고 기록하지 않음 |
| 추가 과거 이력 기능 | 요구가 채택되면 인증/권한·API/화면·시험·운영/기간 부담을 별도로 검토. 이번 해석 정정이 새 기능/DB 구조 변경의 자동 채택은 아님 |

기존 “완료 기록 조회”를 새 Redis에서도 모든 과거 개별 결과를 화면으로 조회할 수 있다는 뜻으로 확대하지 않도록 §3-D.5·§3-D.9.8·§3-D.10.7, 이 절의 사용자 범위, 04 §5.1/§10.2와 05 §9.2~9.3을 정합화했다. 이 기능 경계 보완 시점에는 기존 Backup/Restore·전용 새 DB·새 Redis·로컬 보존 자산과30분/90분/1시간 기준을 유지했다. 이후 목표/주기의 현재 결정은 §3-I.14.5를 따른다. 구조/수치 선택 전에 수행한 실제 00–04 설계 명확화이며 05 기록만 추가한 작업이 아니다. 당시 기능 해석 보완은 그림의 경로/업무 확인을 유지했고, 이후 §3-I.14.5의 새 수치는 그림10의 SVG/PNG·생성 원본과 함께 변경하며 출처 Manifest를 개정 문서에 연결한다.

새 독립 합성 Data 부분 예행은 [05 §9.20](../execution/05_IMPLEMENTATION_AND_VALIDATION.md#recovery-fixture-measurement-20261005)·[Run](../evidence/T18/fixture-20261005-01/summary.md)에 연결했다. 앞선 §3-I.14.1의 “실제 Run 미확인”은 2026-10-03 관측 이력이다. 이번 부분 결과는 실제 RDS 경로·App/Redis/클라이언트 전체 업무·운영 목표 달성이나 새 목표 선택 완료를 대신하지 않는다. C Data 리뷰·D Index 검토/수신과 환경 차이는 실행 기록으로 인계한다.

위 문단과 아래 체크는2026-10-05 기능 경계 보완 시점의 남은 상태다. 이후 두 부분 Run과 제약 비교를 바탕으로 목표/주기를 선택한 현재 설계 상태는 [§3-I.14.5](#recovery-design-decision-20261005)를 우선한다. 이력의 미완료 체크가 현재 설계 선택의 재대기 조건은 아니며 실제 전체 운영 달성 미검증은 그대로 유지한다.

- [x] 고정 App Source의 현재 방 결과 계약과 새 Redis 복구 기능 경계 대조
- [x] 과거 DB 기록 보존과 클라이언트 업무 검증의 구분을 관련03/04/05에 명확화
- [ ] 전체 업무 예행·손실/접속/부담/비용 근거와 새 목표·주기·구조 선택, 채택 내용의 정합 반영/재검증

<a id="recovery-design-decision-20261005"></a>
#### 3-I.14.5 DR 목표·주기·구조의 설계 결정 — 2026-10-05

**기록 ID: PH2-DR-DESIGN-20261005. 상태: SPEC_COMPLETE — 설계 선택 완료·[PR #30](https://github.com/seokpan/seokpan-hybrid-docs/pull/30) main 병합 / 실제 운영 달성 미검증.** 복원 가능성·추가 부담·손실 기준·일정·비용을 비교해 RTO 10분·영속 DB RPO 30분·DB 운영 중 Backup 15분 계획 주기를 선택했다. 이 결정은 2026-10-01의 이전 30분/90분/1시간 승인 기록을 소급 변경하거나 상용 서비스의 데이터 손실 허용을 승인한 기록이 아니다. 이후 설계 문구·출처 정합성 보완은 별도 변경으로 검증하되, 그 작업을 이 설계 결정의 채택 대기로 되돌리지 않는다.

| 항목 | 이전 승인 기준 | 현재 설계와 유지하는 범위 |
| --- | --- | --- |
| 서비스 복구 RTO |30분 이내 | **10분 이내**. 실제 사고 시작→탐지/판단/대응 대기→보존 사본/Key 확인·DB 복원→새 Redis/App 기동→Host 안내/지정 클라이언트 업무·Data 확인까지 |
| 영속 DB RPO |90분 이내 | **30분 이내**. 사고와 실제 사용한 복원 가능한 로컬 사본의 일관된 Data 시각 차이. 신규 회원·완료 Game/Result/Rating의 해당 손실 범위를 명시 |
| Portable Backup | DB 운영 중1시간 | **DB 운영 중15분 계획 간격**. 실제 성공 간격/로컬 확보/시점 불확실성을 별도 관측.7일 일반 사본·마지막 검증본/독립 보호 사본 유지 |
| 구조 | Cloud Primary + On-Prem Backup/Restore | **유지**. Data VM→RDS 논리 Dump/gzip/age→S3→사전 On-Prem 사본, 새 전용 MariaDB에 직접 TLS·별도 새 Redis·로컬 보존 Image/Manifest/Secret/도구 |
| 이용/손실 범위 | 지정 클라이언트의 격리 복구 검증 | §3-I.14.4의 DB 과거 기록 보존＋새 로그인/랭킹/새 게임/현재 방 결과. 세션·진행 게임 손실 별도. Public 자동 전환·과거 이력 새 기능·Warm Standby/지속 복제 추가 없음 |

**왜 이 조합인가:** [Data Run](../evidence/T18/fixture-20261005-01/summary.md)은 작은 합성 데이터3회와 확장1회의 Dump/복원을 실제 수행했고, [Backend Run](../evidence/T18/business-fixture-20261005-01/summary.md)은 새 TLS/AUTH Redis·Production Backend HTTPS의 재로그인/랭킹·새 게임 FORFEIT/현재 결과·SQL 정합을 연결했다. Backend의 스크립트 복원/기동/업무 부분은 [Metric 정본](../evidence/T18/business-fixture-20261005-01/metrics.csv)에서 약5.814초였지만, 사람 탐지/판단/대기·Host/OCP/Image 기동·안내·FE/browser/WSS가 빠진 한 번의 Fixture 측정이므로 서비스 RTO나10분 달성 근거로 확대하지 않는다. 이 결과는 DB 복원 때문에 즉시 상시 복제 구조를 도입해야 한다는 근거가 없다는 제한된 판단과 기존 구조의 구현/연결 가능성에 사용한다.

RTO는 강사 의견의5~10분 중 상단10분을 설계 시험 목표로 선택한다. 사람/Host/클라이언트의 미측정 구간을 고려해5분 목표·새 상시 복제·별도 Cloud 자원을 추가하지 않는다.10분도 보장이나 실측 여유 계산이 아니며 전체 Run에서 실패하면 병목/조건·부담을 먼저 개선/재검토한다. 고정2/3/3/2분 예산을 다시 적용하지 않는다.

RPO30분과15분 계획 간격은 기존90분/1시간보다 손실 기준을 강화하면서 운영 중 시간당4회로 제한하는 선택이다. 최초5분 후보의12회/시간보다 생성/전송/보관·실패 처리 부담을 낮추고,15분 RPO를 위해 모든 지연을 촘촘히 보장해야 하는 조건을 추가하지 않는다.30분은 이 교육 프로젝트의 시험·설계 요구사항이며 사업 사용자가30분의 신규 회원·완료 결과·Rating 손실을 승인했다는 의미나 상용 SLA가 아니다. 실제 사용자 전환/상용 운영 범위를 확대하면 업무별 손실 허용·접속·쓰기 통제/복귀를 별도로 결정한다.

**최신성 판정:** 정상 성공 경로에서 `G + D + U ≤ 30분`을 근거로 확인한다. G는 실제 사용 가능한 성공 사본들의 Data 기준 시각 최대 간격, D는 해당 Data→로컬 사용 가능한 완성본 최대 확보 지연, U는 Snapshot 시점/시계 불확실성의 보수적 여유다.15분은 nominal Timer 간격이며 `G≤15분` 또는 `D≤15분`이 자동 확정되지 않는다. jitter·겹친 실행 생략·전송/VM/Storage 장애·계획 Stop·최신 사본 실패/이전 사본 선택은 실제 값으로 기록한다. 각 최대값을 더하는 정상 경로 확인이 실제 사고마다 복원 가능성을 보장하지도 않는다. 실제 복구는 사용 사본의 Data 나이와 손실을 별도 판정하며30분 초과는 미달, 시점 미확인은 null/미판정이다. 경고·재시도 또는 같은 Run의 목표 완화로 PASS를 만들지 않는다.

| 실행 인계 | 해당 실제 실행 전에 확보할 근거 — 설계 선택의 일괄 선행조건은 아님 |
| --- | --- |
| C Data/새 Redis | 실제 지원 버전/Client·Snapshot/권한·TLS/CA/Key·Timer/중복 잠금·S3/로컬 완료·최신성/경고·보관/실패 재전송 구현.15분 부하/성공 간격·확보 지연·실제 복원/데이터 검증을 새 Run에 기록 |
| B App/클라이언트 | 승인 Image/Manifest/Secret·현재 기능/권한/Transient 처리·새 Redis/DB 계약과 지정 클라이언트 HTTPS/WSS/FE 업무 확인. 과거 DB 기록 보존을 과거 결과 화면 복구로 확대하지 않음 |
| A Host/자산 | 사전 준비된 새 전용 DB VM/플랫폼·CPU/RAM/Storage·독립 사본·Harbor/로컬 도구/CA·관리/접속 경로·예비 담당자의 가용성 확인 |
| D Image/Index/시간선 | Build/Test/Scan·Registry별 Digest/Platform/보존·실제 Index 수신/리뷰, 사고 t0부터 업무/Data 완료 t1까지 및 신규/실패 Run의 증거 연결 |
| 실제 Cost/기간 | 이전1시간 대비15분 계획 주기의4배 계획 건수·672개/24시간×7일 계획 상한·실제 암호문/임시 공간/전송/DB 부하·재시험/인계/문서/발표 시간을 Cost Ledger에 반영. $450 계획선/$500 한도·10/16 Freeze·10/22 Demo·10/23 Ready 유지. 추가 유료 실행은 구체화된 범위/동의 전 하지 않음 |

책임 배정과 실제 수행자는 구분한다. 승인된 실행자가 C의 기술 측정을 수행할 수 있으며 C의 직접 인계·실행만을 독점 조건으로 두지 않는다. 두 합성 부분 Run의 환경·수행자·측정·검토/수신 범위는 해당 Run 원본에서 확인한다. 실제 보호 입력·공유 실행에는 대상·권한·단일 실행자·충돌 조율을 확인한다. C 전체 작업·D Image·ROSA 전체·05 최종 종료를 설계 선택의 일괄 Gate로 확대하지 않으며, 실제 Runtime/T18은 해당 준비와 실행 증거 없이 완료 처리하지 않는다.

Data 주기·최신성/실패 처리·Storage/비용·시험/G7/B06·W04, 04 준비/Runbook, 05/Tracker·Index와 그림10에 현재 설계 요구를 적용한다. 00의 역사, 01의 목적/예산/Freeze와 02의 Cloud Primary/BackupRestore·지정 검증 범위는 유지한다. 이전 승인·철회된 10/15/5 제안·기존 Run과 과거 관측은 보존한다. 이후 발견한 문서·Source·그림 출처의 불일치는 해당 변경에서 검증하며, 설계 선택 완료와 전체 정합성 조사·실제 목표 달성·T18/프로젝트 종료를 각각 판정한다.

**원본/최신 기준의 우선순위:** DR 수치·간격에는 PR #30으로 병합된 본 결정의 10분/30분/15분을 적용한다. Project 등록본과 개인 계획에 남은 이전 30분/90분/1시간은 당시 이력이며 현재 실행 기준으로 사용하지 않는다. 담당·보호·Ownership·기록·Freeze/기간·예산 등 비수치 경계는 유지한다. 등록용 개정본 제작과 실제 Project 소스 교체는 별도이며, 교체가 확인되기 전 자동 동기화를 주장하지 않는다.

- [x] 부분 실측/고정 Source와 사용자 영향·복원 구조·주기/부담 대안 비교,10분/30분/15분 후보 선택
- [x] 기존 구조·역할/예산/Freeze 유지와 실제 실행 Gate·손실/최신성 미판정 처리 인계
- [x] 관련 Source·문서·SVG/PNG/출처 정합 최종 검증·필수 추가 보완0건 — 상세 검증과 리뷰/병합 상태는 변경 PR에 연결
- [ ] 실제 Timer/전송/독립 사본과 전체 사용자 업무 t0~t1·최종 운영 T18 달성 검증 — 설계 후보 완료와 구분

## 남은 작업과 다음 단계

- [x] B01~B07 작업 전제 승인 및 전체03·개정 지침 최종 컨펌 반영
- [x] 프로젝트 소스 등록 완료 보고
- [x] 추가 자료·Issue·지정 Source의 근거/충돌·시험/인계 정리
- [x] 현재 DR10분/30분/15분·Backup/Restore 유지 설계 변경안과 근거/실행 Gate 기록 — §3-I.14.5
- [x] DR 설계 요구 채택·PR #30 병합. 후속 정합성 보완과 실제 운영 목표 달성은 별도
- [ ] 실제 팀 배정/Branch·Seed·GRANT·CI/계정/도구/자산 입력 확인
- [ ] 의존 작업별 구현 시작 조건·첫 Full Apply 전 Cost Gate 확인

실제 구현·Cloud/로컬 검증·Evidence·Must 최종 판정·잔존 비용/Freeze·발표 작업은 이 준비 이후의 실행 단계다. 상단 진행 현황과 하단 남은 준비 체크는 실제 구현에 진입하기 전까지 계속 표시한다.
