# 石나가는 판단 2차 프로젝트 — Project Charter

> **문서 번호:** 01  
> **문서 성격:** 2차 프로젝트의 목적, 범위, 성공조건, 일정 운영 원칙을 정의하는 공식 Charter  
> **기준일:** 2026-09-30 KST  
> **프로젝트 기간:** 2026-09-28 ~ 2026-10-26  
> **AWS Credit / 지원 한도:** $500  
> **팀:** 石판(석나가는 판단), 4명  
> **프로젝트 성격:** 1차 온프레미스 Kubernetes 플랫폼을 출발점으로 하는 AWS Hybrid Cloud 마이그레이션 및 운영 검증 프로젝트

---

# 1. 문서 목적

이 문서는 2차 프로젝트가 **무엇을 위해 진행되는지, 무엇을 성공으로 판단하는지, 어떤 범위를 포함·제외하는지, 언제 구현을 멈추고 검증·발표 준비로 전환하는지**를 정의한다.

이 문서는 특정 Target Architecture를 미리 확정하는 설계 문서가 아니다.  
Target Architecture는 본 Charter의 목적·제약·성공조건을 기준으로 후속 Architecture 비교 단계에서 선택한다.

따라서 이 문서가 답하는 질문은 다음과 같다.

1. 2차 프로젝트의 핵심 목적은 무엇인가?
2. Hybrid, ROSA/OpenShift, Terraform은 어떤 위치의 기술인가?
3. Target Architecture를 어떤 기준으로 결정할 것인가?
4. 프로젝트 성공을 어떤 관점에서 검증할 것인가?
5. 무엇을 이번 프로젝트 범위에서 제외할 것인가?
6. 구현과 검증·발표 준비의 경계를 언제 둘 것인가?

---

# 2. 프로젝트 배경

## 2.1 1차 프로젝트

1차 프로젝트는 온프레미스 환경에서 다음 요소를 통합한 Kubernetes 기반 서비스 플랫폼을 구축한 프로젝트다.

- VMware 기반 VM 인프라
- kubeadm Kubernetes
- Calico
- Gateway API
- Frontend / Backend 애플리케이션
- MariaDB / MaxScale
- Redis
- NFS
- Jenkins / Harbor / Argo CD
- Prometheus / Grafana / Loki / Grafana Alloy / Alertmanager
- Ansible 기반 자동화
- Backup / Restore / DR 및 장애 검증

1차 프로젝트의 **공식 종료 Baseline은 2026-09-23**이다.

다만 2026-09-23 이후에도 신규 주요 기능 개발이 아니라 다음 범위의 Maintenance / Validation / Hardening은 계속될 수 있다.

- Bug Fix
- Stability 개선
- Recovery 검증
- 정량 측정 보완
- 문서 현행화
- 실제 구현과 Desired State의 정합성 보완

따라서 2026-09-23은 **공식 종료 경계**이며, 2차가 반드시 해당 날짜의 코드 상태를 그대로 사용한다는 의미는 아니다.

## 2.2 2차의 실제 출발 상태

2차에서 실제로 참조·상속하는 1차 구성은 다음 원칙을 따른다.

```text
1차 공식 종료 Baseline
2026-09-23
        │
        ▼
Maintenance / Validation / Hardening
        │
        ▼
최신 검증 상태
        │
        ▼
Migration 구현 직전
2차 Seed SHA 확정
```

즉:

- **Official Baseline**: 2026-09-23의 1차 공식 종료 기준
- **Latest Validated State**: 이후 Maintenance/Validation이 반영된 최신 검증 상태
- **2차 Seed**: Migration 구현 직전에 고정하는 실제 Source Commit

2차는 최신 검증 상태를 우선 사용하며, Migration 구현 직전에 Repository별 Seed SHA를 명시적으로 기록한다.

이 방식으로 1차의 공식 포트폴리오 종료 시점은 보존하면서도 이후 발견된 결함 수정과 안정성 개선을 2차에 반영할 수 있다.

---

# 3. 프로젝트 핵심 목적

## 3.1 핵심 목적 — CONFIRMED

> **1차 온프레미스 플랫폼을 AWS Hybrid Cloud로 마이그레이션하면서 단순 이전이 아니라 서비스·데이터·네트워크·CI/CD의 배치를 재판단하고, 그 선택을 IaC·운영·장애·복구·성능·비용 Evidence로 검증하는 것이 2차 프로젝트의 핵심 목적이다.**

## 3.2 우선순위

2차의 주목적은 신규 Application 개발이 아니라 다음에 있다.

1. Infrastructure / Platform Migration
2. 서비스·데이터·네트워크·CI/CD의 책임 재배치
3. IaC 기반 재현성
4. 장애·복구·관측·성능·비용 검증
5. 선택한 Architecture의 근거와 Trade-off 설명

Application은 1차의 실제 서비스를 Migration과 End-to-End 검증에 사용한다.

---

# 4. Target Hybrid Architecture 상태

## 4.1 현재 상태 — PENDING DECISION

2차의 최종 Hybrid 운영모델은 Charter 단계에서 미리 확정하지 않는다.

이것은 결정을 회피하는 것이 아니라, 복수 Architecture 후보를 동일한 기준으로 비교하기 위해 의도적으로 결정을 후속 단계로 유예한 것이다.

후속 Architecture 비교에서 최소 다음 질문을 검토한다.

- 어떤 역할을 AWS로 이전할 것인가?
- 어떤 역할을 On-Prem에 남길 것인가?
- 어떤 역할을 Managed Service로 대체할 것인가?
- Hybrid Link는 실시간 요청, 관리, 배포, 복제, 백업 중 무엇을 운반하는가?
- Hybrid Link 장애가 서비스 중단으로 이어지는가, 아니면 RPO 증가나 관측 공백 등으로 제한되는가?
- 선택한 구조가 기간과 $500 지원 범위에서 실제 구현·검증 가능한가?
- 1차에서 확보한 Kubernetes, DB, Backup/Restore, CI/CD 자산을 어떤 방식으로 재사용할 것인가?

가능한 운영모델에는 다음과 같은 형태가 포함될 수 있으나 이에 한정되지 않는다.

- AWS Application + On-Prem Data
- Cloud Primary + On-Prem DR
- On-Prem Primary + AWS 보조/DR
- Multi-Cluster Hybrid
- Migration 과정에서만 Hybrid를 사용하는 전환형 구조

최종 Target은 후속 Architecture 비교 및 Decision Record를 통해 확정한다.

---

# 5. Hybrid / ROSA / Terraform의 위치

교육과정에서는 Hybrid 환경, OpenShift/ROSA, Terraform을 중심 기술로 안내받았다.

다만 팀이 확인한 범위에서는 더 적합한 구조·도구·방식이 있다면 변경할 수 있으며, 절대적인 강제 기술로 취급하지 않는다.

이에 따라 현재 위치를 다음과 같이 정의한다.

| 항목 | Charter상의 위치 |
|---|---|
| Hybrid Cloud | 프로젝트의 핵심 문제영역 |
| OpenShift / ROSA | Primary Platform Candidate |
| Terraform | Primary IaC Candidate |

즉, 특별한 반대 근거가 없다면 현재 방향을 우선 검토하지만, 더 적절한 대안이 확인될 경우 다음을 기록하고 변경할 수 있다.

```text
현재 후보
→ 대안
→ 비교 기준
→ 선택 이유
→ 영향 범위
→ 최종 결정
```

기술 자체를 사용했다는 사실보다 **왜 선택했고 어떤 운영 차이를 만들었는지**를 중요하게 본다.

---

# 6. 성공조건

프로젝트 성공은 단순한 Cluster 생성, Terraform Apply 성공, 브라우저 접속 성공만으로 판단하지 않는다.

다음 12개 축은 프로젝트 종료 시 모두 답할 수 있어야 한다.

단, 현재 Charter에서는 모든 수치 Target과 구현 방법을 고정하지 않는다.  
Target Architecture 선택 후 각 축별 Metric, Acceptance Criteria, Baseline, Target을 구체화한다.

## 6.1 성공조건 12개 축

| 성공축 | Charter 수준 완료 정의 |
|---|---|
| **Migration Decision** | 주요 구성요소를 Retain / Rehost / Replatform / Replace / Retire 중 어떻게 처리할지와 이유가 명확함 |
| **Hybrid Connectivity** | Target Architecture가 실제로 필요로 하는 On-Prem ↔ AWS 서비스·관리·복제·백업 경로가 검증됨 |
| **Infrastructure Reproducibility** | 선택한 IaC 방식으로 핵심 Cloud / Platform 자원의 재현 범위가 확인됨 |
| **Application Migration** | 1차 서비스의 대표적인 End-to-End 사용자 흐름이 Target 환경에서 정상 동작함 |
| **Availability / Failure** | Architecture상 중요한 Failure Domain에 실제 장애를 주입하고 영향과 복구 동작을 확인함 |
| **Recovery / DR** | Backup / Restore / Failover 등 채택한 복구 전략을 실제로 검증하고 필요한 경우 RTO/RPO를 측정함 |
| **Observability** | 장애 또는 비정상 상태와 Metric / Log / Alert / 판단의 연결을 Evidence로 확인함 |
| **Performance** | Target에서 의미 있는 경로에 대해 Latency / Throughput / Load / Resource Bottleneck 중 적절한 항목을 정량 측정함 |
| **Cost** | AWS 총 사용비용을 $500 지원 범위 내에서 관리하고 주요 자원의 비용 근거와 실제 사용 결과를 남김 |
| **Security** | Secret / Credential / Public Exposure / IAM / Image 등 프로젝트 규모에 필요한 기본 보안 경계를 검증함 |
| **Platform Value** | 선택한 Platform의 기본 기능 나열이 아니라 1차 환경과 비교해 운영책임·배포·보안·관측 등에서 어떤 차이가 있었는지 설명 가능함 |
| **Documentation / Presentation** | Decision, Troubleshooting, 정량 결과, Demo, 재현 가능한 문서를 근거 기반으로 완성함 |

## 6.2 정량화 방식

후속 Test / Evidence 설계에서는 가능한 항목을 다음 순서로 관리한다.

```text
Requirement
→ Measurement Method
→ Baseline
→ Target
→ Actual
→ Evidence
→ Pass / Partial / Fail / N/A
```

해당 Architecture에서 적용되지 않는 성공축은 조용히 제외하지 않고 `N/A`와 이유를 기록한다.

## 6.3 구현과 검증의 구분

다음 상태를 동일하게 보지 않는다.

```text
구현됨
≠
동작 확인됨
≠
장애/조건 변화에서 검증됨
≠
정량 Evidence가 확보됨
```

프로젝트의 중요한 항목은 가능한 한 마지막 단계까지 확인한다.

---

# 7. Scope

범위는 Must / Should / Could / Won't의 네 단계로 관리한다.

Should 또는 Could가 Must 일정과 품질을 침해하는 경우 우선순위를 낮추거나 제거한다.

## 7.1 Must — 프로젝트 성공에 필요한 범위

- Target Architecture 선택과 근거
- Hybrid Connectivity
- IaC 기반 재현성
- 핵심 Application Migration
- 서비스·데이터·State 배치
- CI/CD 경계
- 대표 End-to-End 동작
- 의미 있는 Failure Test
- Backup / Restore 또는 채택한 Recovery 전략
- Observability
- Performance 정량 측정
- AWS 비용 관리 및 Evidence
- Decision / Troubleshooting / Test / Demo 문서

## 7.2 Should — 프로젝트 품질을 높이는 범위

- OpenShift 고유 가치 1~2개를 실제 운영 관점에서 검증
- Migration 및 시연에 필요한 UX/UI 보완
- Rollback 검증
- Image Vulnerability 확인
- PDB / Deprecated API / Upgrade 고려사항 검토
- 추가 Load / Recovery Scenario

UX/UI 보완은 기존 서비스의 안정적인 Migration, 오류 표현, 시연, 사용성을 위한 범위로 제한하며 새로운 게임 규칙이나 대규모 기능 개발로 확대하지 않는다.

## 7.3 Could — Stretch Goal

Core Migration / Integration이 일정상 안정적인 경우에만 수행한다.

### OpenShift Lightspeed PoC

OpenShift Platform Operations와 AI 기반 Troubleshooting을 연결할 수 있는 Stretch Goal이다.

실제 검토 시 다음 정도의 안전한 흐름을 우선한다.

```text
Cluster 상태 조회
→ AI 기반 Diagnosis
→ Remediation 제안
→ Human Approval
→ 조치
→ Recovery Evidence
```

무제한 `cluster-admin` 권한을 부여해 자율적으로 Cluster를 변경하도록 만드는 것은 목표로 하지 않는다.

### 오목 판세 분석 AI

착수마다 판세 또는 승률 변화를 분석하는 Application AI 기능은 추가 Stretch Goal이다.

구현할 경우 단순 기능 추가보다 다음과 같이 Platform 관점으로 연결할 수 있을 때 우선 검토한다.

- 별도 AI Workload
- CPU / Memory Resource
- Latency
- Scaling
- Failure Handling
- Observability

AI 기능 때문에 Core Migration / Validation 일정이 밀리는 경우 구현하지 않는다.

### 기타 Could

- OpenShift Pipelines / Tekton
- 추가 Autoscaling 실험
- 추가 DR Scenario
- 고급 Observability

## 7.4 Won't — 이번 프로젝트에서 제외

- 새로운 게임 Rule / Game Mechanic
- 대규모 신규 UI
- Multi-Cloud 확장
- AWS / OpenShift 제품군의 전면 도입
- 목적이 불명확한 RHACM / Service Mesh / ODF 등의 추가
- 모든 계층의 Active-Active
- 완전 자동·무중단 DR
- Enterprise SIEM / Zero Trust 전면 구축
- 대규모 Kernel / DB Performance Tuning
- 실제 Major Kubernetes / OpenShift Upgrade
- 무제한 권한을 가진 자율 AI Cluster Agent
- 사용 기술 수를 늘리기 위한 기능 추가

---

# 8. 일정 및 Freeze 정책

## 8.1 일정 원칙 — CONFIRMED

> **프로젝트 일정은 평일 작업을 기준으로 수립하며 토·일 작업을 전제로 하지 않는다. 핵심 Architecture와 Foundation을 초기에 확정·구축하고, 10월 16일을 Technical Freeze 목표로 하여 이후에는 신규 구조·주요 기능 추가보다 Validation, 장애·복구, 정량 Evidence, 문서, 시연 영상 및 발표 준비를 우선한다. 주말 작업은 일정 보장을 위한 필수조건이 아닌 추가 Buffer로만 취급한다.**

공휴일 역시 가능한 한 Critical Path의 필수 작업일로 계산하지 않는다.

## 8.2 Milestone

| 시점 | 목표 |
|---|---|
| **9/30 ~ 10/1** | Project Charter 확정 및 Architecture 비교 준비 |
| **10/2 목표** | Target Architecture Decision |
| **10/5 ~ 10/8** | Foundation 구축 및 일정 위험이 큰 핵심 PoC |
| **10/12 ~ 10/15** | Migration / Integration / End-to-End 연결 |
| **10/16** | **Technical Freeze** |
| **10/19 ~ 10/21** | Validation / Failure / Recovery / Performance / Cost / Evidence |
| **10/22** | **Demo Freeze** |
| **10/23** | **Presentation Ready** |
| **10/26** | Final Buffer / 최종 발표 |

## 8.3 Technical Freeze 정의

2026-10-16 이후에는 원칙적으로 다음을 추가하지 않는다.

- 새로운 Target Architecture
- 신규 주요 Feature
- 새로운 핵심 Platform / Managed Service
- 일정에 없던 기술 확장

Freeze 이후 허용하는 변경은 다음에 한정한다.

- 서비스/발표를 막는 P0/P1 Blocker
- Validation에서 확인된 필수 Correction
- Recovery / Security / Data Integrity 문제 수정
- Demo 및 발표를 불가능하게 만드는 결함 수정

Should / Could 항목 제거는 실패로 간주하지 않는다.  
Must Scope를 안정적으로 연결하고 이후 검증 시간을 확보하는 것을 우선한다.

---

# 9. Contribution & Evidence Integrity

프로젝트 결과는 **실제로 수행한 범위와 기여 수준에 맞게 표현한다.**

플랫폼이 기본 제공하는 기능이나 일반적인 구축 절차를 팀이 특별한 기술을 개발한 것처럼 표현하지 않는다.

다음을 구분한다.

| 구분 | 표현 원칙 |
|---|---|
| 제품/플랫폼의 기본 기능 | 사용·확인·활용한 사실로 표현 |
| 일반적인 구축 절차 | 구현 내역으로 기록하되 대표 성과로 과장하지 않음 |
| 팀이 비교·선택한 설계 | 선택 기준과 Trade-off를 근거와 함께 설명 |
| 팀이 직접 구현·자동화한 부분 | 실제 구현 범위와 책임을 명시 |
| 팀이 직접 검증한 부분 | Test 조건, 측정값, Evidence를 제시 |
| 실제 Troubleshooting | 문제 → 원인 → 조치 → 재검증을 구체적으로 기록 |

예를 들어 Kubernetes가 삭제된 Pod를 다시 생성하는 기본 Self-Healing 동작을 확인했다면 이를 “Self-Healing 기능을 개발했다”고 표현하지 않는다.

반대로 다음과 같은 내용은 프로젝트의 의미 있는 결과가 될 수 있다.

- 여러 Architecture 후보 중 하나를 선택한 근거
- Failure Domain과 비용을 고려한 배치 변경
- 실제 환경 제약으로 인해 Network 방식을 수정한 과정
- 예상과 다른 장애 원인을 찾아 해결한 사례
- RTO/RPO, Latency, Cost 등 실제 측정 결과
- IaC Resource Ownership 또는 State 경계를 재설계한 이유

발표와 포트폴리오의 강조점은 **기술 자체의 존재가 아니라 실제 판단·구현·검증·문제해결에서 발생한 의미 있는 차이**에 둔다.

---

# 10. 의사결정 및 변경 관리

중요한 Project Decision은 후속 문서 또는 Decision Record로 남긴다.

최소 기록 항목:

- 결정 내용
- 결정일
- 검토한 후보
- 주요 제약
- 선택 근거
- 영향을 받는 영역
- 재검토 조건
- 관련 Evidence

본 Charter의 핵심 목적·Scope·Freeze 정책을 변경하려면 프로젝트 리드·팀의 명시적인 재검토를 거친다.

Target Architecture, AWS 세부 Network, Data 배치, ROSA 모델, Terraform 구조 등은 본 Charter를 기준으로 후속 단계에서 결정한다.

---

# 11. Project Source 및 Repository 경계

현재 GitHub 운영 기준은 다음과 같다.

- 기존 `seokpan` Organization을 유지한다.
- 1차 Repository는 독립 포트폴리오로 보존한다.
- 2차 초기 문서 Workspace는 `seokpan-hybrid-docs`를 사용한다.
- Application / Infra / GitOps의 최종 2차 Repository topology는 Target Architecture와 Migration 범위를 확인한 뒤 결정한다.
- 1차 Application Source의 2차 Seed는 Migration 구현 직전에 최신 검증 Commit으로 고정한다.

이 Charter는 `seokpan-hybrid-docs`의 공식 Project Source로 보관하는 것을 전제로 한다.

---

# 12. 현재 미확정 사항

본 Charter 승인 시점에도 다음은 의도적으로 미확정 상태다.

- 최종 Hybrid Architecture
- 서비스별 AWS / On-Prem 배치
- ROSA HCP / Classic 등 구체적인 Platform 모델
- AWS Region
- VPC / Subnet / CIDR
- Hybrid Network 최종 방식
- DB / Redis / Registry / Jenkins / Observability 위치
- 최종 Terraform Module / State 구조
- HA / DR의 구체적 Target
- 성공조건별 정량 Target 값
- 최종 2차 Repository topology
- AI Stretch Goal 실행 여부

이 항목들은 후속 Architecture 및 상세설계 단계에서 결정한다.

---

# 13. Charter 완료 조건

본 Charter는 다음 조건을 충족하므로 1단계 완료 기준으로 사용한다.

- [x] 프로젝트 목적 정의
- [x] Target Architecture 결정 시점과 원칙 정의
- [x] 주요 기술의 위치 정의
- [x] 성공조건 정의
- [x] Must / Should / Could / Won't Scope 정의
- [x] AI 기능의 우선순위와 안전 경계 정의
- [x] 일정 및 Technical Freeze 정의
- [x] 주말 비전제 원칙 정의
- [x] 1차 Baseline / Latest Validated State / 2차 Seed 관계 정의
- [x] 과장 없는 기여·Evidence 표현 원칙 정의
- [x] 후속 단계의 미확정 항목 명시

다음 단계는 **Architecture 후보 비교 및 Target 선택**이며, 별도의 승인 후 진행한다.
