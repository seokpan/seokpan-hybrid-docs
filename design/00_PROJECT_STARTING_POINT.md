# 石나가는 판단 2차 프로젝트 — 시작 기준점

> **문서 성격:** 1차 온프레미스 Kubernetes 프로젝트 종료 이후, 2차 AWS/ROSA 하이브리드 클라우드 프로젝트를 시작하기 위한 공식 기준 문서  
> **현행화 기준:** 2026-09-30 KST  
> **1차 공식 종료 Baseline:** 2026-09-23  
> **2차 프로젝트 시작:** 2026-09-28  
> **2차 프로젝트 목표 종료:** 2026-10-26  
> **AWS Credit / 지원 한도:** $500 — 프로젝트 총 AWS 사용비용은 이 범위 내에서 관리  
> **문서 목적:** 1차의 실제 종료 상태를 출발점으로 고정하고, 2차에서 무엇을 유지·이전·재설계·대체할지 순차적으로 판단하기 위한 기준을 제공한다.  
> **중요:** 본 문서는 2차의 최종 아키텍처를 확정하는 문서가 아니다. 확정된 사실, 현재 제안, 미확정 의사결정을 구분하여 관리한다.

---

# 1. 문서 사용 원칙

이 문서는 다음 세 가지를 동시에 만족해야 한다.

1. **1차 프로젝트의 실제 종료 상태를 왜곡하지 않는다.**
2. **2차 프로젝트의 아직 확정되지 않은 선택지를 확정안처럼 기록하지 않는다.**
3. **2차 설계를 시작할 때마다 이 문서를 기준점으로 삼되, 최신 Runtime·GitHub·공식 서비스 제약은 필요 시 다시 현행화한다.**

본 문서의 내용은 다음 상태 중 하나로 해석한다.

- **CONFIRMED** — 프로젝트 리드·팀이 명시적으로 승인했거나 실제 Source/Evidence로 확정된 내용
- **CURRENT STATE** — 현재 저장소·문서·운영 확인 기준의 상태
- **PROPOSAL** — 현재 유력한 제안이지만 아직 확정하지 않은 내용
- **PENDING DECISION** — 프로젝트 리드·팀 논의를 거쳐 별도 확정이 필요한 내용
- **VALIDATION PENDING** — 구현은 존재하지만 추가 검증·측정이 남은 내용
- **DEFERRED** — 1차 완료조건에서 제외되고 2차 또는 후속 단계에서 재평가할 내용

---

# 2. 프로젝트 계보

## 2.1 1차 프로젝트

**「石나가는 판단」 1차 프로젝트**는 온프레미스 환경에서 Kubernetes 기반 서비스 플랫폼을 구축하고, 애플리케이션·데이터·CI/CD·Observability·DR을 통합·검증한 프로젝트다.

1차는 포트폴리오로 독립 보존한다.

### 1차의 핵심 성격

- 온프레미스 중심
- VMware 기반 VM
- kubeadm Kubernetes
- Calico VXLAN
- Gateway API 기반 애플리케이션 진입
- MariaDB + MaxScale
- Redis StatefulSet + PVC + AOF
- NFS
- Jenkins + Harbor + Argo CD
- Prometheus / Grafana / Loki / Grafana Alloy / Alertmanager
- Ansible 기반 인프라 자동화
- 실제 장애·복구·DR·CI/CD Evidence 관리

## 2.2 2차 프로젝트

2차 프로젝트는 1차 결과물을 폐기하고 처음부터 새로 만드는 프로젝트가 아니다.

**현재 정의:**

> 1차의 동작하는 온프레미스 플랫폼과 애플리케이션을 기준점으로 삼아 AWS 하이브리드 클라우드로 책임을 재배치·이전하고, **ROSA/OpenShift와 Terraform을 우선 검토 기술로 두되 실제 채택 모델·범위는 단계별 검증 후 확정**하며, GitOps·HA·DR·보안·관측성·검증 체계를 포함한 재현 가능한 플랫폼을 만드는 프로젝트다.

따라서 2차의 핵심은 단순한 “VM Lift-and-Shift”가 아니다.

```text
1차 On-Prem 실제 상태
        ↓
역할/책임 단위 분해
        ↓
Retain / Rehost / Replatform / Replace / Retire 판단
        ↓
On-Prem ↔ AWS 책임 재배치
        ↓
ROSA/OpenShift 적용 범위 판단
        ↓
Hybrid Network
        ↓
Terraform / GitOps 적용 범위 판단
        ↓
HA / DR / Security / Observability
        ↓
검증 가능한 Target Architecture
```

## 2.3 2차 프로젝트의 현재 확정 제약 — CONFIRMED

- 프로젝트 기간: **2026-09-28 ~ 2026-10-26**
- AWS Credit / 지원 한도: **$500**, 프로젝트 AWS 사용비용은 이 범위 내에서 관리
- 1차 결과물은 독립 포트폴리오로 보존
- 2차는 1차의 실제 구현을 출발점으로 사용
- ROSA / OpenShift / Terraform은 지향 기술이지만, 구체적 모델·배치·적용 범위는 단계별 검토 후 확정
- 비용이 큰 Managed Service나 Network 구성은 기능 적합성뿐 아니라 총비용·가동시간·삭제계획까지 함께 검토

## 2.4 팀 구성과 1차 책임영역 — CURRENT CONTEXT

| 팀원 | 1차 중심 책임영역 | 2차에서의 의미 |
|---|---|---|
| 이유빈 | Network / Ansible / External Infra | Network·AWS Foundation 조사에 활용 가능한 기존 역량 |
| 정태훈 | Kubernetes / Application Integration / Redis / Argo CD | ROSA·Application·GitOps 조사에 활용 가능한 기존 역량 |
| 김상희 | MariaDB / MaxScale / NFS / Backup / Recovery | Data·Storage·DR 조사에 활용 가능한 기존 역량 |
| 최유준 | Harbor / Jenkins / Observability / 장애·부하 Evidence | Delivery·Observability·Validation 조사에 활용 가능한 기존 역량 |

위 표는 **1차의 실제 담당과 기존 역량을 설명하는 참고정보**다.  
2차의 최종 역할·Workstream·Owner를 자동 확정하지 않으며, 2차 WBS 단계에서 다시 논의한다.

---

# 3. 1차 프로젝트 종료 상태

## 3.1 공식 종료와 Maintenance 경계 — CONFIRMED

1차의 공식 프로젝트 종료 Baseline은 **2026-09-23**으로 유지한다.

그 이후 발생하는 작업은 프로젝트 범위를 다시 확대하는 것이 아니라 **Closeout / Maintenance / Validation / Hardening**으로 분리한다.

```text
2026-09-23
1차 공식 종료 Baseline
        │
        ├── 버그 수정
        ├── 강화 Validation
        ├── 장애 분석
        ├── Recovery Evidence 보완
        ├── 보안 패치
        └── 문서 현행화
             ↓
      1차 Maintenance HEAD
```

### Maintenance에서 허용하는 작업

- 버그 수정
- 기존 기능의 안정성 보완
- 검증·측정 보완
- 장애 원인 분석
- DR / Recovery Evidence 강화
- 보안 취약점 수정
- 문서·Runbook·Evidence 현행화
- 기존 구현과 Desired State의 정합성 수정

### 원칙적으로 1차에 추가하지 않는 작업

- 신규 주요 기능
- 대규모 아키텍처 변경
- 1차 범위를 확장하는 신규 플랫폼
- AWS/ROSA 전용 구현
- Terraform 기반 2차 인프라
- 2차 Target Architecture를 위한 구조적 변경

이 경계를 사용하여 **1차 포트폴리오의 완결성**과 **2차 프로젝트의 독립성**을 동시에 보존한다.

---

# 4. 1차 Source of Truth

1차 Actual State는 기억이나 초기 기획서만으로 판단하지 않는다.

## 4.1 저장소 역할

| Repository | 역할 |
|---|---|
| `seokpan-app` | Application Source, Test, Container, Jenkins CI 정의 |
| `seokpan-gitops` | Kubernetes Desired State, Argo CD, Platform/CICD/Observability Manifest |
| `seokpan-infra` | On-Prem Infra, Network, DB/Storage, Secret 공급, Ansible |
| `seokpan-docs` | Architecture, Current State, 변경 이력, Runbook, Validation, Troubleshooting |

## 4.2 문서 Source of Truth 관계

```text
01~08 기획·설계 Baseline
= 확정 당시의 계획·설계

PROJECT_CHANGES.md
= Baseline 이후 변경 이유

CURRENT_STATE.md
= 종료 이후 실제 구현·검증 상태

MVP_IMPLEMENTATION_BASELINE.md
= 실제 MVP 구현 기준

09
= 역할별 실행·통합 실시설계

10
= GitHub 협업 / Repository 운영

11
= 구축·자동화 Runbook

12
= 검증·측정 / Evidence

Troubleshooting
= 실제 장애 → 원인 → 조치 → 검증

Implementation Repositories
= 현재 코드·Manifest·자동화의 최종 Source of Truth
```

**과거 기획값을 현재 Runtime 상태처럼 해석하지 않는다.**

---

# 5. 2026-09-30 기준 저장소 현행 상태

문서 작성 시점에 확인된 각 저장소의 최신 HEAD는 다음과 같다.

| Repository | HEAD |
|---|---|
| `seokpan-app` | `1128ebcc21bc1523aea68f46659ce6beeed7b00d` |
| `seokpan-gitops` | `fbc26c4f1b0e878880e5bd92327aa88a057854e1` |
| `seokpan-infra` | `fc122001c214a4cd6c57fab4a0189cdb59ea318d` |
| `seokpan-docs` | `4d865ebc6fb9fab03223aa5db784f658fe6f1eb5` |

이 SHA들은 **2026-09-30 현행화 참고값**이다.

2차 Application Migration의 최종 Seed SHA로 자동 확정하지 않는다.

---

# 6. 1차 실제 인프라 구조

1차 핵심 인프라는 **Physical Server 4대의 VMware Workstation 기반**으로 구성했다. 초기 원 목표는 VM 18개였으나, 실제 MVP는 `lb-02`와 `maxscale-02`를 제외한 **16 VM**으로 축소하여 구현했다.

따라서 2차에서는 다음을 구분한다.

- **원 설계 규모:** Physical Server 4대 / VM 18개
- **실제 1차 MVP:** Physical Server 4대 / 핵심 서비스 VM 16개
- 외부 관리·부하 시험 등 지원 장비는 핵심 16 VM과 별도 검증 자원으로 취급하며, 2차에서 사용 가능 여부는 필요 시 다시 확인

## 6.1 실제 16 VM Inventory — CURRENT STATE

`seokpan-infra/ansible/inventory/hosts.yml` 기준:

| 영역 | VM |
|---|---|
| Virtual Router | `vrouter-01`, `vrouter-02`, `vrouter-03`, `vrouter-04` |
| Kubernetes Control Plane | `cp-01`, `cp-02`, `cp-03` |
| Kubernetes Worker | `worker-01`, `worker-02` |
| MariaDB | `mariadb-01`, `mariadb-02` |
| MaxScale | `maxscale-01` |
| Load Balancer | `lb-01` |
| Registry | `harbor` |
| Storage | `nfs` |
| Ansible Controller | `ansible` |
| **합계** | **16 VM** |

### 주요 대역

- External / 학원망 측: `10.1.93.x`
- Private Subnet: `192.168.51.0/24` ~ `192.168.54.0/24`
- 기존 VIP: `10.1.93.90`

2차 AWS VPC, Pod Network, Service Network 및 Tunnel Network 설계 시 **CIDR 중복을 금지**한다.

---

# 7. 1차 플랫폼 실제 구조

```text
                         Client
                           │
                           ▼
                         lb-01
                        HAProxy
                           │
              ┌────────────┴────────────┐
              │                         │
        Kubernetes API            Application
              │                         │
       ┌──────┴──────┐                  │
       │             │                  │
    CP × 3        Worker × 2            │
       │             │                  │
       └──────── Kubernetes ────────────┘
                     │
      ┌──────────────┼─────────────────┐
      │              │                 │
 Frontend/Backend   Redis            Jenkins
                                   Argo CD
                                   Observability

                     │
             External Infrastructure
                     │
       ┌─────────────┼──────────────┐
       │             │              │
  MariaDB ×2    MaxScale ×1        NFS

            Harbor / Ansible Controller

              Network Foundation
                   │
              vRouter ×4
```

### Kubernetes / Platform 주요 구성

- kubeadm
- Control Plane 3대
- Worker 2대
- Calico VXLAN
- Gateway API
- Frontend / Backend Deployment
- Redis StatefulSet + PVC + AOF
- Jenkins
- Argo CD App-of-Apps
- Prometheus
- Grafana
- Loki
- Grafana Alloy
- Alertmanager

### External Infrastructure

- HAProxy
- MariaDB Primary / Replica
- MaxScale
- NFS
- Harbor
- Ansible Controller

---

# 8. Application State Ownership

1차에서 확립한 상태 책임 경계는 2차에서도 기본 보존 여부를 우선 검토한다.

| 상태 | Authority / 책임 |
|---|---|
| Member / Game / Move / Result / Rating 등 영속 상태 | MariaDB |
| Session / Room / Ready / Connection Generation / Game Runtime / Turn / Vote | Redis |
| Application Source / Domain Contract | `seokpan-app` |
| Kubernetes Desired State | `seokpan-gitops` |
| Server / DB / Secret / CA / Infrastructure | `seokpan-infra` |

핵심 원칙:

- MariaDB와 Redis의 책임을 임의로 합치지 않는다.
- 일반 Backend Replica 시작 시 DB Migration을 자동 실행하지 않는다.
- Runtime Credential과 Migration Credential을 분리한다.
- 검증된 Container Image와 Runtime Desired State 변경을 분리한다.
- GitOps Repository의 변경과 실제 Runtime 변경을 구분한다.
- Secret / Password / Token / Private Key를 Git에 평문으로 저장하지 않는다.

---

# 9. 1차 구현·검증 상태

프로젝트 운영자의 최신 확인과 `CURRENT_STATE.md`를 함께 기준으로 다음 영역은 1차의 동작하는 종료 상태로 본다.

- Kubernetes Cluster
- Application Platform
- Frontend / Backend
- MariaDB / MaxScale
- Redis Runtime
- Jenkins
- Harbor
- Argo CD / GitOps
- CI/CD Delivery
- Observability
- Backup / Recovery 기본 체계

2026-09-30 기준 프로젝트 운영자는 **클러스터·서비스 플랫폼·CI/CD·DB가 현재 잘 동작하고 있음**을 직접 확인했다.  
이는 운영환경 전체를 본 문서 작성 시점에 다시 재측정했다는 뜻은 아니며, 기존 Runtime Evidence·GitHub Source와 최신 운영 확인을 함께 반영한 상태 표현이다.

## 9.1 CI/CD 정상 흐름

```text
App main
→ Jenkins Test / Build / Scan / Health
→ Harbor Final Digest
→ Component Impact 판단
→ GitOps Promotion Branch / Commit / PR
→ Human Review / Approval
→ Merge
→ Argo CD Sync
→ Kubernetes Runtime
```

다음 경계는 유지한다.

- GitOps `main` 직접 Push 금지
- 자동 Merge 금지
- 사람 Review / Approval 유지
- Image Digest 및 Source SHA 추적
- 비영향 Component의 불필요한 Rollout 최소화
- Git Revert 기반 Runtime Rollback 가능

---

# 10. 1차 Maintenance / Validation Backlog

1차의 전체 구조는 동결되었지만, 2026-09-30 기준 일부 강화 검증과 안정성 작업은 계속된다.

## 10.1 `seokpan-app #112`

**Application Runtime·Concurrency·Recovery·Measurement 잔여 검증**

주요 잔여 범위:

- Realtime / WebSocket Failure Boundary
- Redis connected / generation 수렴
- Reconnect / Safe Leave 세부 검증
- Runtime Presentation
- Room Admission / Session Concurrency
- Captured Game Lifecycle 재평가
- 정량 Measurement

이 Issue는 신규 주요 기능 Parent가 아니라 **Closeout Validation** 성격이다.

## 10.2 `seokpan-app #117`

**Background Runner 실패 후 Backend Pod 영구 NotReady 재발 방지**

- Redis Provider 오류 이후 Background Runner의 실패 정책
- Fail-closed Readiness
- 복구 후 2/2 Ready 재수렴
- Transient Provider 오류와 불변식 오류의 정책 분리

이 작업 역시 1차 Architecture를 다시 설계하는 것이 아니라 **Runtime Stability Hardening**으로 취급한다.

## 10.3 Cluster HA Validation Boundary

1차 핵심 클러스터와 서비스가 동작하는 상태와 별개로, **cp-03 / API VIP 장애 경로의 HA 검증은 Closeout에서 별도 미완료 경계로 유지**되어 있다.

이를 다음처럼 해석한다.

- 현재 클러스터 전체가 비정상이라는 의미가 아님
- Control Plane / API VIP의 특정 장애 시나리오에 대한 추가 Evidence가 남았다는 의미
- 2차에서 ROSA의 Managed Control Plane 책임과 비교할 때 참고할 1차 운영 한계·검증 항목

---

# 11. 1차에서 명시적으로 Deferred된 주요 항목

다음 항목은 1차 성과로 과장하지 않고, 2차에서 필요성을 다시 판단한다.

- Backend HPA
- Captured Game Lifecycle Production 활성화
- `lb-02`
- `maxscale-02`
- Redis Sentinel / Redis Cluster
- ANALYSIS Runtime
- 일부 Exporter / Alert Rule 강화
- Hybrid Cloud
- OpenShift / ROSA
- Terraform

---

# 12. 1차 Baseline / Maintenance / 2차 Seed 정책 — CONFIRMED

## 12.1 1차 공식 Baseline

- 공식 종료일: **2026-09-23**
- 1차 포트폴리오 기준 결과물을 보존한다.
- 이후 수정은 Maintenance / Closeout로 별도 추적한다.

## 12.2 Maintenance HEAD

1차 저장소의 최신 `main`은 검증·버그 수정으로 일부 변할 수 있다.

이 때문에 `main HEAD = 1차 공식 종료 Baseline`으로 동일시하지 않는다.

## 12.3 2차 Seed

2차의 Architecture / AWS / Network / ROSA / Terraform 설계는 즉시 진행한다.

그러나 **Application Source를 실제로 Fork/Copy/Migrate하는 시점의 Seed SHA는 Migration 구현 직전에 확정**한다.

```text
현재
→ Architecture / AWS / ROSA / Network / Terraform 조사·설계

동시에
→ 1차 #112 / #117 Maintenance

Migration 구현 직전
→ 최종 Application Seed SHA 확정
```

이 방식으로 1차 보완 때문에 2차 전체 일정이 중단되는 문제와, 2차 기준 코드가 계속 흔들리는 문제를 동시에 피한다.

---

# 13. 2차에서 반드시 먼저 정의해야 할 질문

## 13.1 Hybrid의 의미 — PENDING DECISION

“Hybrid Cloud”는 최소 두 가지 의미가 있다.

### A. Migration 과정만 Hybrid

```text
On-Prem
  ↓ 점진 이전
AWS / ROSA
```

최종적으로 AWS/ROSA 중심으로 수렴할 수 있다.

### B. 최종 Architecture도 Hybrid

```text
On-Prem 역할
      ↕
Hybrid Network
      ↕
AWS / ROSA 역할
```

일부 서비스가 장기적으로 On-Prem에 남는다.

이 결정은 다음 항목 전체에 영향을 준다.

- DB 위치
- Redis 위치
- Registry 위치
- CI/CD 위치
- VPN/Tunnel 필요성
- DR 방향
- DNS
- Latency
- 비용
- 장애 시 서비스 지속성

따라서 Target Architecture 전에 명시적으로 확정한다.

---

# 14. VM이 아니라 역할 단위로 Migration 판단

2차는 16 VM을 기계적으로 EC2로 복사하는 프로젝트가 아니다.

아래 Migration Matrix를 순차적으로 확정한다.

| 1차 역할 | 2차 후보 | 상태 |
|---|---|---|
| CP ×3 | ROSA Managed Control Plane 역할로 대체 | PENDING |
| Worker ×2 | ROSA Machine Pool | PENDING |
| vRouter ×4 | AWS Network / Hybrid Tunnel 역할로 재설계 | PENDING |
| lb-01 | AWS LB / OpenShift Ingress·Route 등 비교 | PENDING |
| MariaDB ×2 | On-Prem 유지 / EC2 / Managed DB 비교 | PENDING |
| MaxScale | 유지 / 이전 / 제거 / 대체 | PENDING |
| NFS | 유지 / AWS Storage 재검토 | PENDING |
| Harbor | 유지 / AWS Registry 계열 비교 | PENDING |
| Jenkins | On-Prem / AWS / ROSA 배치 비교 | PENDING |
| Redis | ROSA / AWS / On-Prem 비교 | PENDING |
| Argo CD | OpenShift GitOps 포함 재평가 | PENDING |
| Observability | 현행 / OpenShift / AWS 조합 검토 | PENDING |
| Ansible | 유지, Terraform과 책임 경계 재설계 | PENDING |

판정 범주는 필요에 따라 다음을 사용한다.

- Retain
- Rehost
- Replatform
- Replace
- Retire

---

# 15. ROSA 관련 현행 기준

## 15.1 ROSA with HCP vs ROSA Classic — PENDING DECISION

현재 ROSA에는 Hosted Control Plane(HCP)과 Classic 모델이 존재한다.

### ROSA with HCP

- Control Plane은 Red Hat 소유 AWS Account에서 호스팅·관리
- Worker는 고객 AWS Account에 배치
- Worker와 Control Plane은 AWS PrivateLink를 사용
- 고객 Account의 최소 EC2 footprint가 작음
- AWS 공식 비교 기준 최소 EC2: 2대

### ROSA Classic

- Control Plane과 Worker 모두 고객 AWS Account에 배치
- Dedicated Infrastructure Node 사용
- AWS 공식 비교 기준 최소 EC2:
  - Single-AZ: 7대
  - Multi-AZ: 9대

따라서 1차의 `cp-01~03`을 그대로 “ROSA CP 3대”로 이전한다고 가정하지 않는다.

HCP를 선택할 경우 기존 Control Plane 운영 책임 자체가 Managed Responsibility로 이동한다.

## 15.2 Networking

OpenShift Container Platform의 기본 네트워크 공급자는 **OVN-Kubernetes**다.

본 문서의 Red Hat 4.20 문서 참조는 **현재 OpenShift Networking의 기본 동작을 확인하기 위한 현행 자료**이며, 2차 프로젝트의 OpenShift/ROSA 버전을 4.20으로 확정한다는 의미가 아니다. 실제 ROSA 생성 시 지원 Version·Region·Upgrade Policy를 다시 확인한다.

따라서 1차 Calico VXLAN을 그대로 복제하는 것이 아니라 다음 요구사항을 다시 매핑한다.

- NetworkPolicy
- Pod / Service Network
- Egress
- Ingress
- MTU
- CIDR
- Overlay Network
- Hybrid Routing

특히 OpenShift 내부 네트워크 CIDR과 AWS VPC 및 On-Prem CIDR의 중복을 사전에 검토한다.

---

# 16. Hybrid Network — 후보만 관리하며 아직 확정하지 않음

이전 팀 논의에서 WireGuard 등 Software VPN 방식이 검토된 바 있으나, **본 문서에서는 아직 최종 방식으로 확정하지 않는다.**

Network 단계에서는 반드시 프로젝트 리드·팀의 기존 논의와 현재 유력 후보를 다시 확인한다.

## 16.1 검토 후보

- AWS Native Site-to-Site VPN
- EC2 기반 Software VPN Hub
- WireGuard
- Tailscale 계열
- Cloudflare Mesh
- 필요 시 기타 대안

## 16.2 AWS Native Site-to-Site VPN의 현행 제약

IP 기반 Customer Gateway의 외부 IP는 정적이어야 한다.

Customer Gateway가 NAT 뒤에 있는 경우 NAT 장비의 Public IP를 사용하며, NAT-T 사용 시 UDP 500/4500 등의 네트워크 조건이 필요하다.

따라서 다음 학원 환경 제약을 먼저 확인한다.

- Public IP의 고정 가능 여부
- 학원 FortiGate / L2 장비에 대한 관리 권한
- Port / Protocol 허용 가능 여부
- 자체 장비 등록 가능 여부
- 아웃바운드만 허용되는 환경인지

이 제약이 충족되지 않으면 AWS Native Site-to-Site VPN을 기본안으로 자동 선정하지 않는다.

## 16.3 Cloudflare 계열 현행 구분

단순 Cloudflare Tunnel은 특정 Application / Hostname / Route를 outbound-only Connector로 공개하는 용도와 잘 맞는다.

반면 **Cloudflare Mesh**는 양방향 Private IP 통신과 network-to-network 연결을 지원한다.

따라서 이후 비교에서는 Cloudflare Tunnel과 Cloudflare Mesh를 동일한 방식으로 취급하지 않는다.  
또한 **무료 사용 가능 여부·Plan 제한·프로젝트 규모에서의 비용은 이 단계에서 확정하지 않는다.** Network 후보 비교 시 당시의 공식 Pricing/Plan을 다시 확인한다.

---

# 17. AWS VPC 설계의 순서

다음 값을 먼저 임의로 정하지 않는다.

- VPC 몇 개
- Public Subnet 몇 개
- Private Subnet 몇 개
- NAT Gateway 몇 개
- Internet Gateway 사용 여부
- EIP 몇 개
- Security Group 구조

정확한 순서는 다음과 같다.

```text
1. On-Prem 현재 IP 확인
        ↓
2. 비중첩 IPAM
        ↓
3. ROSA HCP / Classic
        ↓
4. Public / Private API 요구사항
        ↓
5. Single-AZ / Multi-AZ
        ↓
6. Hybrid Network 방식
        ↓
7. VPC 수
        ↓
8. Subnet / Route Table
        ↓
9. IGW / NAT / VPC Endpoint
        ↓
10. EIP
        ↓
11. Security Group / NACL
```

즉 EIP와 NAT Gateway의 수량은 선행 설계의 **결과값**이다.

---

# 18. AWS Account / IAM 초기 원칙

사용 가능한 AWS Root Account가 존재한다.

그러나 Root는 일상 작업 계정으로 사용하지 않는다.

## 현행 AWS Best Practice 기준

- Root MFA 적용
- Root Access Key 생성 금지
- Root 사용 최소화
- 사람의 Access는 가능한 한 Temporary Credential 사용
- IAM Role / IAM Identity Center 등 검토
- 장기 Access Key 사용 최소화

현재 “팀원 4명 모두 IAM User AdministratorAccess”는 **확정안이 아니다.**

초기 실습 편의성을 위해 넓은 권한이 일시적으로 필요할 수 있으나, 다음을 별도로 결정한다.

- Bootstrap Admin
- 팀원별 Human Access
- Permission Set / Role
- MFA
- Terraform Execution Role
- ROSA용 Account / Operator Role
- CI/CD Credential
- Break-glass 방식

---

# 19. Terraform과 GitOps의 책임 경계

Terraform은 설계를 대신 정하는 도구가 아니다.

**확정된 Infrastructure Desired State를 재현 가능한 코드로 만드는 도구**로 사용한다.

잠정 책임 분리는 다음과 같다.

## Terraform 후보 책임

- AWS Account-level / IAM 관련 리소스
- VPC
- Subnet
- Route Table
- IGW / NAT / Endpoint
- Security Group
- AWS Managed Services
- ROSA prerequisite / Cluster Infrastructure
- Hybrid Network의 AWS 측 리소스

## OpenShift GitOps / Argo CD 후보 책임

- Namespace / Project
- Application Workload
- Service
- Route / Ingress
- ConfigMap
- NetworkPolicy
- Platform Workload
- Kubernetes / OpenShift Desired State

같은 리소스를 Terraform과 Argo CD가 동시에 소유하지 않는다.

2차 설계에서 **Resource Ownership Matrix**를 공식 산출물로 만든다.

---

# 20. HA와 DR의 구분

HA와 DR을 하나의 “고가용성” 항목으로 묶지 않는다.

2차에서는 Failure Domain을 먼저 정의한다.

| Failure Domain | 검토 질문 |
|---|---|
| Pod 장애 | Replica가 서비스 지속 가능한가 |
| Worker 장애 | 다른 Worker에서 재배치 가능한가 |
| AZ 장애 | Multi-AZ가 필요한가 |
| Hybrid Tunnel 장애 | On-Prem 의존 서비스는 어떻게 되는가 |
| DB Primary 장애 | 자동/수동 Failover인가 |
| AWS ↔ On-Prem 단절 | 서비스가 지속·축소·중단 중 무엇인가 |
| On-Prem 전체 장애 | AWS가 독립 운영 가능한가 |
| AWS 측 장애 | On-Prem이 어떤 역할을 하는가 |
| 데이터 손상 | Backup / Restore 기준은 무엇인가 |
| 잘못된 배포 | GitOps / Image / DB Rollback은 무엇인가 |

각 Failure Domain에 다음을 연결한다.

- RTO
- RPO
- 자동 복구 / 수동 복구
- Runbook
- Monitoring / Alert
- Evidence
- Acceptance Criteria

---

# 21. 2차에서 초기부터 누락하면 안 되는 요소

다음은 Target Architecture 이후에 뒤늦게 붙이지 않고 초기 설계 단계부터 관리한다.

## Governance / Security

- AWS Root 보호
- IAM / Identity Center / Role
- OpenShift RBAC
- Least Privilege
- Secret 관리
- Audit
- CloudTrail 등 AWS Audit 여부
- Credential Rotation

## Network

- IPAM
- CIDR 중복
- VPC
- AZ
- Public / Private Subnet
- NAT / IGW / Endpoint
- DNS
- Route53
- TLS / Certificate
- On-Prem ↔ AWS Name Resolution
- Hybrid Tunnel HA

## Cost

- 프로젝트 AWS Credit / 예산
- ROSA 비용
- EC2
- NAT Gateway
- EIP
- Load Balancer
- Storage
- Data Transfer
- Managed Service
- 삭제되지 않은 Resource 비용
- AWS Budget / Alert
- 구축 후 Destroy Plan

## Platform

- ROSA HCP / Classic
- OpenShift Version
- Worker / Machine Pool
- Autoscaling
- StorageClass
- Registry
- Ingress / Route
- NetworkPolicy

## Data

- MariaDB 위치
- Redis 위치
- Storage
- Backup
- Restore
- Replication
- Migration Cutover
- Rollback

## Delivery

- Jenkins 위치
- Registry 위치
- GitOps
- Terraform
- CI Credential
- Artifact provenance

## Operations

- Metrics
- Logs
- Alert
- SLO / Health
- 장애 탐지
- Runbook

## Validation / Portfolio

- Functional Test
- Network Test
- HA Test
- DR Test
- Load Test
- Security Test
- Restore Test
- Cost Evidence
- Architecture Diagram
- Demo Scenario
- Demo Video
- Final Presentation
- Portfolio Documentation

---

# 22. GitHub 1차 / 2차 분리 원칙

## CONFIRMED

1차는 독립 포트폴리오로 보존한다.

2차 작업 때문에 1차 저장소의 역사와 결과물이 혼합되거나 사라져서는 안 된다.

## PROPOSAL

2차 전용 저장소를 별도로 구성하는 방향이 유력하다.

예시:

```text
seokpan
├─ 1차
│  ├─ seokpan-app
│  ├─ seokpan-infra
│  ├─ seokpan-gitops
│  └─ seokpan-docs
│
└─ 2차 후보
   ├─ seokpan-hybrid-app
   ├─ seokpan-hybrid-infra
   ├─ seokpan-hybrid-gitops
   └─ seokpan-hybrid-docs
```

단, 이 Naming과 Repository 수는 아직 최종 확정하지 않는다.

다음 단계에서 먼저 확정할 것은 **“1차 포트폴리오 Repository를 보호하고 2차 작업을 별도 경계에서 진행한다”는 원칙과 초기 문서 위치**다.  
Application / Infra / GitOps / Docs를 최종적으로 몇 개 Repository로 나눌지는 Project Charter와 Migration 범위를 확인한 뒤 확정한다.

특히 Application Source를 별도 Repository로 Fork/Copy할지, 기존 Source를 재사용할지는 실제 변경 범위를 검토한 뒤 결정한다.

---

# 23. 프로젝트 의사결정 방식

2차에서 기술 선택은 다음 절차를 사용한다.

```text
① 현재 확인된 사실
        ↓
② 기존 팀 논의 / 후보 확인
        ↓
③ 추가 가능한 대안 조사
        ↓
④ 제약·장단점·비용·복잡도 비교
        ↓
⑤ 프로젝트 리드 / 팀 검토
        ↓
⑥ 필요 시 조합안 도출
        ↓
⑦ 명시적 확정
        ↓
⑧ 설계 전제로 승격
```

팀에서 제시된 아이디어는 자동 확정하지 않는다.

### 예

- “WireGuard 얘기를 했었다.” → 후보
- “WireGuard로 가는 게 어떨까?” → 검토안
- “WireGuard 방식으로 확정하자.” → 확정
- “이건 바꾸지 않는다.” → 고정 제약

분석 과정에서 새로 제안된 안도 프로젝트 리드·팀의 명시적 승인 전까지는 **PROPOSAL**이다.

---

# 24. 4인 병렬 작업의 기본 틀

초기에는 다음 네 Track을 기준으로 병렬 조사할 수 있다.

| Track | 중심 영역 |
|---|---|
| A | Network / External Infra / AWS Foundation |
| B | Kubernetes / ROSA / Application / GitOps |
| C | Data / Storage / Backup / DR |
| D | CI/CD / Registry / Observability / Test Evidence |

다만 각 Track이 독립적으로 서로 다른 전제를 확정해서는 안 된다.

```text
공동 As-Is / Requirement
        ↓
병렬 Discovery
A   B   C   D
        ↓
공동 Architecture Review
        ↓
Target Architecture
        ↓
구현 분리
```

최종 팀원 배정과 세부 WBS는 별도 단계에서 프로젝트 리드·팀 검토 후 확정한다.

---

# 25. 2차 진행 Gate

현재 권장 순서는 다음과 같다.

## GATE 0 — 1차 Baseline / Handoff
- [x] 1차 Actual State 확인
- [x] 공식 종료 Baseline 정의
- [x] Maintenance 경계 정의
- [x] 2차 Seed 정책 정의
- [ ] 2차 시작 기준 문서 등록
- [ ] 1차/2차 GitHub 경계 및 2차 초기 Workspace 결정

## GATE 1 — Project Charter
- [ ] 최종 Hybrid인지 Migration 중 Hybrid인지
- [ ] 프로젝트 목적
- [ ] 성공조건
- [ ] 비대상
- [x] 전체 기간 기준: 2026-09-28 ~ 2026-10-26
- [x] AWS Credit / 지원 한도: $500
- [ ] 세부 단계별 일정 / Freeze 날짜
- [ ] 서비스별 비용 배분
- [ ] Region
- [ ] 주요 제약

## GATE 2 — Discovery / Target Architecture
- [ ] Migration Matrix
- [ ] ROSA 모델
- [ ] Network 방식
- [ ] Data / Storage
- [ ] CI/CD / Registry
- [ ] Observability
- [ ] Security / IAM
- [ ] Target Architecture Review

## GATE 3 — PoC
- [ ] AWS Access
- [ ] Terraform Bootstrap
- [ ] ROSA
- [~] Hybrid Network — EC2 WireGuard ↔ vrouter-02 기술 타당성 PoC 완료, Target Topology 검증 대기
- [~] On-Prem ↔ AWS 실제 통신 — PoC 범위 양방향 통신·DB 3306 확인, 프로젝트 전체 경로 검증 대기
- [ ] 최소 Application 연결
- [ ] 비용 확인

## GATE 4 — Foundation Build
- [ ] Network
- [ ] IAM
- [ ] ROSA
- [ ] Terraform
- [ ] GitOps
- [ ] Shared Services

## GATE 5 — Migration
- [ ] Application
- [ ] Data
- [ ] Storage
- [ ] Delivery
- [ ] Observability

## GATE 6 — Validation
- [ ] Functional
- [ ] Network
- [ ] HA
- [ ] DR
- [ ] Backup / Restore
- [ ] Load
- [ ] Security
- [ ] Cost
- [ ] Rollback

## GATE 7 — Closeout
- [ ] Freeze
- [ ] Demo
- [ ] Video
- [ ] Final Evidence
- [ ] Presentation
- [ ] Portfolio

---

# 26. 일정의 기본 비율

전체 프로젝트 기간은 **2026-09-28 ~ 2026-10-26**으로 확정되어 있다. 아래 비율은 그 기간 안에서 세부 WBS·Freeze 날짜를 정하기 위한 초기 배분 기준이며, 세부 날짜는 WBS 단계에서 조정한다.

| 구간 | 권장 비율 |
|---|---:|
| Baseline / Charter / IAM / 비용 / 조사 | 10~15% |
| 병렬 Discovery / Target Architecture | 15~30% |
| ROSA / Hybrid / Terraform 핵심 PoC | 30~40% 시점까지 |
| Foundation + Migration | 40~70% |
| HA / DR / Load / Security 검증 | 70~85% |
| 통합 / Freeze / Evidence | 85~95% |
| Demo / 영상 / 발표 / Portfolio | 95~100% |

Freeze 이후에는 원칙적으로 신규 기능을 추가하지 않는다.

---

# 27. 현 시점 진행 상태

- [x] 1차 Actual State 현행화
- [x] 2차 프로젝트 시작점 정의
- [x] 1차 공식 종료 Baseline 확정
- [x] 1차 Maintenance 경계 확정
- [x] 2차 Seed 정책 확정
- [x] 프로젝트 의사결정 원칙 정의
- [x] WireGuard Hybrid Network 기술 타당성 PoC Evidence 확보
- [x] 팀 역할·Architecture·WBS Draft 참고자료 확보
- [ ] 본 문서를 2차 Project Source에 등록
- [ ] 1차/2차 GitHub 경계 및 초기 Workspace 확정
- [ ] Project Charter
- [ ] AWS IAM / Governance
- [ ] Migration Matrix
- [ ] ROSA / Hybrid Network
- [ ] AWS VPC 상세설계
- [ ] Terraform / GitOps Ownership
- [ ] HA / DR
- [ ] WBS / Test / Evidence
- [ ] 구현

---

# 28. 다음 작업

다음 단계는 **0-B-2 / 0-C**다.

1. 본 문서를 2차 프로젝트 Source로 등록한다.
2. **1차 Repository와 2차 작업의 분리 경계**를 먼저 확정한다.
3. 기존 팀 논의가 있다면 먼저 반영 후보로 제시한다.
4. 2차 문서·초기 작업을 둘 독립 Workspace/Repository 원칙을 정한다.
5. Project Charter에서 최종 Hybrid 범위와 주요 Workstream을 확정한다.
6. 그 결과를 반영해 Application / Infra / GitOps / Docs의 **최종 Repository topology와 Naming을 확정**한다.

즉 다음 단계에서 “1차와 2차를 분리한다/어디에 2차 기준 문서를 둘 것인가”는 결정할 수 있지만, 2차 저장소를 몇 개로 나눌지까지 Project Charter보다 앞서 고정하지 않는다.

**다음 단계에서도 구현을 먼저 시작하지 않는다.**

---

# 29. 공식 참고 자료

본 문서의 AWS / ROSA / OpenShift / Hybrid Network 관련 현행 정보는 2026-09-30 기준으로 다음 공식 문서를 참고했다.

- AWS IAM Root User Best Practices  
  https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html

- AWS IAM Security Best Practices  
  https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html

- ROSA Architecture — HCP vs Classic  
  https://docs.aws.amazon.com/rosa/latest/userguide/rosa-architecture-models.html

- ROSA with HCP Getting Started  
  https://docs.aws.amazon.com/rosa/latest/userguide/getting-started-hcp.html

- ROSA Shared Responsibilities  
  https://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html

- OpenShift OVN-Kubernetes Network Plugin  
  https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/ovn-kubernetes_network_plugin/index

- AWS Site-to-Site VPN Customer Gateway Options  
  https://docs.aws.amazon.com/vpn/latest/s2svpn/cgw-options.html

- Cloudflare Mesh  
  https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/

- Cloudflare Network-to-Network  
  https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/network-to-network/

- Terraform ROSA HCP Module  
  https://registry.terraform.io/modules/terraform-redhat/rosa-hcp/rhcs/latest

---

---

# 30. 추가 제공자료 반영 — 2026-09-30

본 절은 2026-09-30에 추가 제공된 팀 자료와 프로젝트 리드의 운영·발표 방향을 반영한다.

추가 자료:

1. `vpn-test-report.pdf`
   - 강의실(온프렘) ↔ AWS WireGuard 터널 PoC
   - 작성자: 김상희
   - 작성일: 2026-09-29
2. `석판_2차_프로젝트_역할_분담표.pdf`
   - 2차 역할·Architecture·Terraform·일정 초안
   - 팀 회의용 Draft이며 확정 문서가 아님

이 자료들은 기존 Gate와 진행 순서를 바꾸는 문서가 아니다. 향후 해당 단계의 의사결정에서 **Observed Evidence / Team Draft / User Preference**로 다시 검토한다.

## 30.1 WireGuard PoC — OBSERVED EVIDENCE

강의실 환경에서 다음 형태의 실제 PoC가 완료되었다.

```text
On-Prem vrouter-02
        │
        │ 강의실에서 먼저 연결
        ▼
교육장 NAT / Internet
        │
        ▼
AWS EC2 VPN Server
WireGuard + Public IP
        │
        ▼
AWS Test Resource
```

실측된 범위:

- WireGuard Handshake 성공
- UDP 51820 통과
- 터널 양방향 통신 성공
- AWS → On-Prem MariaDB TCP 3306 연결 성공
- AWS가 온프렘 서버의 원본 사설 IP를 확인
- MTU 1420 시험 통과
- 터널 처리량 약 Upload 443 Mbps / Download 389 Mbps
- RTT 약 3 ms 수준
- 약 1시간 50분 연속 통신에서 Packet Loss 미관측
- 50분 이상 유휴 상태였던 TCP 연결이 이후 정상 통신
- 교육장 출구 Public IP가 실제로 한 번 전환된 상황에서 Packet Loss 미관측
- PoC 종료 후 AWS 시험 리소스 삭제

### 검증 범위의 한계

이 결과를 다음으로 확대하지 않는다.

- 석판 전체 Hybrid Network 검증 완료
- vrouter-01~04 전체 경로 검증 완료
- ROSA ↔ On-Prem 전체 통신 검증 완료
- Harbor / 모든 DB / 모든 서비스 검증 완료
- WireGuard HA 검증 완료
- 출구 IP 변경 시 항상 무중단 보장

현재 판정:

> **EC2 기반 WireGuard 방식이 현재 강의실 네트워크에서 기술적으로 동작할 수 있다는 사실은 실제 PoC로 확인되었다.**

따라서 WireGuard는 단순 아이디어가 아니라 **Observed Evidence가 있는 유력 Hybrid Network 후보**다. 최종 채택 여부는 Hybrid Network 단계에서 다시 결정한다.

## 30.2 강의실 Network PoC에서 확인된 설계 Input

PoC 보고서에 따르면 강의실 Network는 다음 특성을 가진다.

- vRouter 외부 인터페이스는 `10.1.93.x` 사설망
- 교육장 NAT를 통해 Internet에 나감
- 외부에서 보이는 출구 Public IP가 복수이며 연결 시 달라질 수 있음
- 교육장 공유기 / Gateway에 대한 직접 관리권한이 제한됨
- 외부에서 강의실로 임의의 신규 Inbound 연결을 받기 어려움
- On-Prem이 먼저 Outbound 연결을 생성하는 방식은 가능

이 조건은 향후 AWS Native Site-to-Site VPN, EC2 Software VPN, WireGuard, Tailscale 계열, Cloudflare Mesh 등 후보 비교의 중요한 제약으로 사용한다.

## 30.3 WireGuard 실제 구축안에서 재검토할 항목

PoC 문서에는 두 가지 On-Prem Gateway 구성이 제안되어 있다.

### 방법 A — 기존 vRouter 겸용

```text
vrouter-02
+ WireGuard
```

장점:
- 신규 VM 불필요
- PoC와 동일 구조라 빠르게 시작 가능

위험:
- vrouter-02 장애 또는 변경이 내부망과 VPN에 동시에 영향

### 방법 B — 전용 VPN Gateway VM

```text
vpn-gw-01
+ WireGuard
```

장점:
- 기존 Router와 VPN 역할 분리
- 장애 영향 범위 분리

비용:
- VM 1대 추가
- 별도 Routing 설정 필요

PoC 작성자는 방법 B를 권장하지만, 이는 **팀 초안/기술 제안**이며 프로젝트 확정안은 아니다.

향후 Hybrid Network 단계에서는 최소 다음을 다시 결정한다.

- vRouter 겸용 vs Dedicated VPN Gateway
- AWS VPN EC2 1대의 SPOF 수용 여부
- VPN Gateway HA 필요 여부
- Route 설계
- NAT 예외
- Security Group
- EIP
- WireGuard Key 관리
- Persistent Keepalive
- MTU / MSS
- Terraform / Ansible 소유권

## 30.4 NAT / Original Source IP 경계

1차 vRouter의 기존 Masquerade 정책은 AWS 목적지 Traffic까지 NAT할 수 있다.

이 경우 AWS 측에서 원래 On-Prem Source IP 대신 Router IP가 보일 수 있으며 MariaDB Account Host Condition, Security Policy, Logging / Audit, Network Allowlist 등에 영향을 줄 수 있다.

PoC에서는 AWS 목적지 대역을 NAT 대상에서 제외하는 방식으로 원본 IP 보존을 확인했다.

따라서 Hybrid Network 최종 설계에서 **NAT Exemption / Source IP Preservation**을 별도 Acceptance 항목으로 둔다.

## 30.5 VPC CIDR 후보와 Source Conflict

WireGuard 보고서에는 AWS VPC 후보로 `172.20.0.0/16`이 제안되어 있다. 그러나 해당 값은 **실제 PoC의 최종 VPC로 검증된 값이 아니라 실제 프로젝트용 후보**다.

최종 CIDR은 다음을 동시에 놓고 다시 검토한다.

- `10.1.93.0/24`
- `192.168.51.0/24`
- `192.168.52.0/24`
- `192.168.53.0/24`
- `192.168.54.0/24`
- ROSA / OpenShift Pod Network
- ROSA / OpenShift Service Network
- VPC
- VPN Tunnel Address
- 추가 실습 OpenShift Network

팀 역할분담 Draft 일부에는 On-Prem 대역이 `192.168.50~53.0/24`로 기재되어 있으나, 1차 실제 Inventory와 WireGuard 실측 자료에서는 `192.168.51~54.0/24`가 사용된다.

현재 프로젝트 Actual State 기준은 `192.168.51.0/24` ~ `192.168.54.0/24`이며, 역할분담 Draft의 `50~53` 표기는 IPAM 단계에서 다시 검증한다.

## 30.6 역할분담표 — TEAM DRAFT

추가 제공된 역할분담표는 팀 회의용 초안이다.

Draft의 주요 가설:

```text
AWS / ROSA
- Application

        ↕ VPN

On-Prem
- MariaDB / MaxScale
- Harbor
- NFS 여부 재검토
```

역할 초안:

| 담당 | Draft 영역 |
|---|---|
| 이유빈 | Network / Hybrid Connection / AWS VPC |
| 정태훈 | OpenShift / ROSA / Application |
| 김상희 | Data / Storage / Backup / Recovery |
| 최유준 | CI/CD / Registry / Monitoring / Test |

이 구조는 1차 담당영역과 연속성이 높다는 장점이 있지만 최종 역할 배정, 부담당, Terraform Module 구조, DB/Harbor/NFS 잔존, ROSA Application 배치, 4주 WBS 상세는 자동 확정하지 않는다.

## 30.7 ROSA / Terraform 필수 여부 — 확인 필요

역할분담 Draft에는 Hybrid Environment, OpenShift / ROSA, Terraform이 “꼭 써야 하는 기술”로 기재되어 있다.

그러나 이 문구가 다음 중 무엇을 의미하는지는 아직 공식 확정하지 않았다.

1. 교육과정 / 프로젝트 외부 요구사항
2. 팀 내부 기술 선택 Draft

따라서 Project Charter 단계에서 반드시 확인한다.

## 30.8 추가 OpenShift 실습환경 — PROVIDED RESOURCE / PENDING USE

팀 Draft에는 Demo01 / Demo02라는 별도 OpenShift 실습환경이 기재되어 있다. 각 환경의 실제 2차 Architecture 포함 여부, ROSA Migration 사전 학습용 여부, On-Prem Hybrid 역할 여부, 강의실 Network / VPN 연결 가능 여부는 미확정이다.

사용 목적은 ROSA / OpenShift 단계에서 확인한다.

## 30.9 AWS Account / 비용 운영 방향 — PROVIDED CONDITION + USER PREFERENCE

현재 제공된 외부조건:

- AWS Root Account 지원
- AWS 사용 Credit / 지원 한도: **$500**

현재 프로젝트 리드의 운영 선호:

- IAM 자체에 과도한 설계 시간을 쓰지 않음
- 팀원 4명이 빠르게 독립 작업할 수 있는 Access를 선호
- `IAM User ×4 + AdministratorAccess`를 초기 단순 운영 후보로 고려
- 필요하다면 Terraform / ROSA / CI용 역할은 별도로 분리
- 필요한 안전선을 지키되 과도한 보안 설계 복잡도로 전체 일정을 지연시키지 않음

따라서 `AdministratorAccess ×4`는 현재 **확정사항이 아닌 유력 단순화 후보**다.

## 30.10 일정 운영 방향 — USER PREFERENCE

공식 프로젝트 기간은 `2026-09-28 ~ 2026-10-26`이다.

목표는 10/26에 구현을 끝내는 것이 아니라, **핵심 구축·Migration·통합을 가능한 한 일찍 완료하고 공식 종료일 이전에 충분한 Validation / Troubleshooting 정리 / 문서 / 시연영상 / 발표 준비 시간을 확보하는 것**이다.

최종 WBS에서는 공식 종료일과 별도로 다음 내부 Milestone을 설정한다.

- Foundation Complete
- Migration Complete
- Integration Complete
- Technical Freeze
- Validation Complete
- Demo Freeze
- Presentation Ready

실제 날짜는 WBS 단계에서 확정한다.

## 30.11 발표 Narrative — USER DIRECTION

현재 예상 발표 흐름은 다음과 같다.

```text
1차 프로젝트 소개
        ↓
1차 Architecture / Actual State
        ↓
2차 Migration 요구사항
        ↓
무엇을 남기고 / 옮기고 / 대체했는가
        ↓
선택 근거
        ↓
Target Hybrid Architecture
        ↓
실제 구축 / Migration 과정
        ↓
Troubleshooting 사례
        ↓
정량적 결과
        ↓
목표 달성률
        ↓
시연 영상
```

이는 확정된 Slide 목차는 아니지만 Project Charter와 Test Plan에서 필요한 Evidence를 역산하는 Input으로 사용한다.

## 30.12 정량 Evidence 원칙

발표 직전에 임의의 숫자를 만들지 않는다.

가능한 항목은 다음 순서로 관리한다.

```text
Requirement
→ Measurement Method
→ 1차 Baseline
→ 2차 Target
→ 2차 Actual
→ Evidence
→ Achievement Rate / Pass-Fail
```

후보 Metric:

- Hybrid Network Connectivity
- RTT / Packet Loss
- VPN Throughput
- Application Availability
- Pod / Worker Recovery
- DB RTO / RPO
- Backup / Restore
- Terraform Provision / Rebuild
- Rollback
- Test Pass Rate
- Cost
- Migration Completion

Target 값은 Test / Acceptance 단계에서 별도 확정한다.

## 30.13 추가자료의 현재 분류

| 구분 | 내용 |
|---|---|
| **OBSERVED EVIDENCE** | WireGuard PoC 실측 결과 |
| **PROVIDED CONDITION** | AWS Root, $500 Credit, 프로젝트 기간, 실습 자원 |
| **TEAM DRAFT** | 역할분담, ROSA App + On-Prem Data 구조, Terraform Module, 초기 WBS |
| **USER PREFERENCE** | 빠른 구축, 단순 IAM 선호 가능, 후반 검증·발표 시간 확보 |
| **PRESENTATION DIRECTION** | As-Is → 판단 → Migration → Troubleshooting → 정량결과 → Demo |
| **PENDING DECISION** | 최종 Target Architecture 전반 |
| **SOURCE CONFLICT** | 역할 Draft의 `192.168.50~53` vs 실제 `192.168.51~54` |

---

# 31. 변경 관리

본 문서는 2차 프로젝트의 “시작점”이므로 모든 세부 변경을 누적 기록하는 운영 문서로 사용하지 않는다.

이 문서 이후에 확정되는 사항은 별도 문서로 분리한다.

예시:

```text
00_PROJECT_STARTING_POINT.md
01_PROJECT_CHARTER.md
02_AS_IS_BASELINE.md
03_MIGRATION_MATRIX.md
04_TARGET_ARCHITECTURE.md
05_HYBRID_NETWORK.md
06_AWS_FOUNDATION.md
07_ROSA_PLATFORM.md
08_TERRAFORM_GITOPS_OWNERSHIP.md
09_HA_DR_BACKUP.md
10_SECURITY_IAM.md
11_TEST_EVIDENCE_PLAN.md
12_WBS_AND_CLOSEOUT.md
```

본 문서는 후속 결정이 발생하더라도 “왜 2차를 이렇게 시작했는가”를 설명하는 **역사적 기준점**으로 유지한다.

---
