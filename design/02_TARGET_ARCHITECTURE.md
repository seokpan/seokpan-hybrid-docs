# 石나가는 판단 2차 프로젝트 — Target Architecture

> **문서 번호:** 02  
> **문서 성격:** 2차 프로젝트의 확정 Target Architecture, 책임 배치, Failure Domain, Lifecycle 및 검증 경계를 정의하는 공식 Architecture 문서  
> **기준일:** 2026-10-01 KST  
> **프로젝트 기간:** 2026-09-28 ~ 2026-10-26  
> **AWS Credit / 지원 한도:** $500  
> **팀:** 石판(석나가는 판단), 4명  
> **Architecture 상태:** CONFIRMED — 상세 Network/IAM/Migration/Test 설계 전 단계  
> **상위 원칙:** 정상 사용자 요청은 AWS Cloud Primary 내부에서 처리하고, On-Prem은 Restore-based Recovery·CI·Recovery Artifact 역할을 수행한다.

---

# 1. 문서 목적

이 문서는 1차 온프레미스 Kubernetes 플랫폼을 출발점으로 하는 2차 AWS Hybrid Cloud 프로젝트의 **Target Architecture를 확정**한다.

이 문서 하나만으로 다음을 파악할 수 있도록 작성한다.

1. 정상 서비스가 어디에서 실행되는가?
2. AWS와 On-Prem은 각각 어떤 책임을 가지는가?
3. ROSA, Database, Redis, Registry, CI/CD, Observability를 어디에 배치하는가?
4. 어떤 Resource를 Terraform이 관리하고 어떤 Resource를 GitOps가 관리하는가?
5. High Availability와 Restore-based Recovery는 어떤 Failure Domain을 담당하는가?
6. ROSA를 반복 생성·삭제하면서도 어떤 자원은 유지해야 하는가?
7. 어떤 부분까지 이번 Architecture에서 확정됐고 무엇이 후속 상세설계로 남아 있는가?
8. 어떤 검증을 통과해야 Architecture의 주장을 Evidence로 인정할 수 있는가?

본 문서는 `01_PROJECT_CHARTER.md`에서 정의한 목적·Scope·성공조건을 구체적인 배치와 책임 구조로 내린 결과다.  
다만 본 문서를 이해하기 위해 이전 문서를 반드시 읽어야 하는 것은 아니다.

---

# 2. 프로젝트 배경과 출발점

## 2.1 1차 온프레미스 플랫폼

1차 프로젝트는 VMware 기반 온프레미스 환경에 다음 구성요소를 통합했다.

- kubeadm Kubernetes Control Plane 3대 / Worker 2대
- Calico
- Gateway API
- Frontend / Backend 애플리케이션
- MariaDB Primary/Replica + MaxScale
- Redis StatefulSet + PVC + AOF
- NFS
- Jenkins
- Harbor
- Argo CD
- Prometheus / Grafana / Loki / Grafana Alloy / Alertmanager
- Ansible
- Backup / Restore / 장애 검증

1차 프로젝트의 공식 종료 Baseline은 2026-09-23이며, 2차는 해당 날짜의 Source를 기계적으로 복제하지 않는다.

2차 Application Migration 직전에는 Bug Fix·Validation·Hardening이 반영된 **Latest Validated State**에서 Repository별 Seed SHA를 고정한다.

## 2.2 2차 Architecture의 목적

2차 프로젝트는 1차 VM을 AWS에 그대로 복제하는 Lift-and-Shift가 아니다.

각 역할을 다음 관점으로 다시 판단한다.

- Retain
- Rehost
- Replatform
- Replace
- Retire

핵심은 다음과 같다.

> **1차 온프레미스 플랫폼을 AWS Hybrid Cloud로 마이그레이션하면서 서비스·데이터·네트워크·CI/CD의 책임 배치를 재판단하고, 그 선택을 IaC·운영·장애·복구·성능·비용 Evidence로 검증한다.**

## 2.3 1차 구성요소의 최종 Migration 판정 경계

본 Target Architecture에 특정 1차 구성요소가 등장하지 않는다는 사실만으로 해당 구성요소가 자동으로 `Retire`된 것으로 해석하지 않는다.

예를 들어 다음 구성요소의 최종 `Retain / Rehost / Replatform / Replace / Retire` 판정은 후속 Migration Matrix에서 명시적으로 기록한다.

- Calico
- Gateway API
- MaxScale
- 기존 Argo CD
- 1차 Redis 구현
- 1차 Monitoring/Logging 구성요소
- 기타 Target 정상 경로에 직접 나타나지 않는 1차 역할

Target Architecture는 최종 배치 방향을 정하며, 세부 Migration Disposition은 별도 Migration Matrix의 책임이다.

---

# 3. Target Architecture 결정

## 3.1 확정 운영모델

Target Architecture는 다음으로 확정한다.

> **B1 — Cloud Primary + On-Prem Restore-based Recovery**

정상 사용자 요청은 AWS 안에서 처리한다.

```text
User
  │
  ▼
AWS
  ├─ ROSA Classic Multi-AZ
  │    ├─ Frontend
  │    ├─ Backend
  │    └─ OpenShift GitOps / Native Monitoring
  │
  ├─ Amazon RDS for MariaDB Multi-AZ
  ├─ Amazon ElastiCache for Redis OSS Multi-AZ
  ├─ Amazon ECR
  └─ Amazon S3
```

On-Prem은 정상 사용자 요청의 필수 경로가 아니라 다음 역할을 담당한다.

```text
On-Prem
  ├─ MariaDB Restore Target
  ├─ Recovery Validation용 Runtime Redis
  ├─ NFS / Recovery Backup Artifact
  ├─ Jenkins
  ├─ Harbor Recovery Registry
  ├─ 1차 On-Prem Kubernetes — Recovery Validation Runtime
  └─ 1차 On-Prem Observability
```

AWS와 On-Prem 사이의 Hybrid Link는 다음 역할을 수행한다.

- Backup / Recovery 경로
- 관리 통신
- 필요 시 복제 실험
- Recovery 검증

**정상 사용자 요청의 필수 경로에는 Hybrid Link와 On-Prem Resource를 포함하지 않는다.**

이 원칙은 후속 Network 상세설계에서도 유지해야 하는 Architecture Invariant다.

---

# 4. 전체 Architecture

```text
                              ┌───────────────────────────────────────┐
                              │                 AWS                   │
                              │                                       │
          User ──────────────▶│ ROSA Classic Multi-AZ                │
                              │ ├─ Frontend                           │
                              │ ├─ Backend                            │
                              │ ├─ OpenShift GitOps                   │
                              │ └─ OpenShift Native Monitoring        │
                              │          │                            │
                              │          ├──────────────┐             │
                              │          ▼              ▼             │
                              │  RDS for MariaDB   ElastiCache        │
                              │  Multi-AZ          Redis OSS          │
                              │  Primary +         Multi-AZ           │
                              │  Sync Standby      Primary + Replica  │
                              │                                       │
                              │  ECR                    S3             │
                              │  Runtime Image          Backup         │
                              └──────────────────┬────────────────────┘
                                                 │
                                      Backup / Recovery /
                                      Management / Optional
                                          Replication
                                                 │
                                         Hybrid Tunnel
                                                 │
                              ┌──────────────────▼────────────────────┐
                              │              On-Prem                  │
                              │                                       │
                              │ MariaDB Restore Target                │
                              │ Recovery Validation용 Runtime Redis   │
                              │ NFS / Portable Backup Artifact        │
                              │ Jenkins — Build / Test / Image Scan   │
                              │ Harbor — Recovery Registry            │
                              │ 1차 On-Prem Kubernetes                │
                              │   └─ Recovery Validation Runtime      │
                              │ 1차 Prometheus/Grafana/Loki           │
                              └───────────────────────────────────────┘
```

---

# 5. Architecture 선택 근거

## 5.1 검토한 주요 Family

Architecture 비교에서는 다음 유형을 검토했다.

### A. Application Cloud + Data On-Prem

```text
User → ROSA → Hybrid Tunnel → On-Prem MariaDB
```

장점:

- 기존 DB/MaxScale 활용이 큼
- Data Migration 작업이 작음
- 초기 Integration이 상대적으로 단순함

단점:

- 모든 주요 DB 요청이 Hybrid Link에 의존
- 학원 Network·Tunnel·On-Prem DB 장애가 정상 Cloud 서비스 장애로 이어짐
- ROSA를 Multi-AZ로 구성해도 정상 Runtime의 Availability가 On-Prem Failure Domain에 묶임

### B. Cloud Primary + On-Prem Recovery

```text
User → ROSA → AWS DB → Response

AWS ↔ On-Prem
= Backup / Recovery / Management
```

장점:

- 정상 서비스와 Hybrid Failure Domain을 분리
- Application뿐 아니라 Data 책임까지 Cloud로 재배치
- Tunnel 장애와 정상 서비스 장애를 별도 Test Scenario로 검증 가능
- Recovery 및 RPO/RTO 검증 구조가 명확함

단점:

- DB Migration 필요
- Restore-based Recovery 설계 필요
- Cloud Managed Data 계층 비용 추가

### C. On-Prem Primary + AWS Pilot/DR

기존 1차 자산을 가장 많이 유지할 수 있으나, 정상 Runtime Migration의 변화폭이 작아 2차의 Cloud Migration 목적과 상대적으로 거리가 있음.

### D. Dual Platform / Multi-Cluster

검증 가능한 내용은 많지만 Network·Data·RBAC·Monitoring·Traffic Management의 운영면적이 크게 증가하며 10/16 Technical Freeze 일정에 비해 과도함.

## 5.2 최종 선택 이유

B1을 선택한 핵심 이유는 다음과 같다.

1. 정상 사용자 요청을 AWS 내부에서 종료할 수 있음
2. Hybrid Tunnel 장애가 곧바로 서비스 장애가 되는 구조를 피할 수 있음
3. 1차 Data 계층을 단순 폐기하지 않고 Recovery 자산으로 역할 변경 가능
4. Cloud Migration과 Recovery 검증을 하나의 Architecture에서 설명 가능
5. RDS / ElastiCache / ROSA 각각의 Failure Domain을 독립적으로 검증 가능
6. Terraform·GitOps 재현성 검증과 ROSA 반복 생성/삭제 운영방식이 자연스럽게 연결됨

---

# 6. Platform — ROSA Classic Multi-AZ

## 6.1 선택

AWS의 OpenShift Platform은 **ROSA Classic Multi-AZ**를 사용한다.

ROSA with HCP가 아니라 Classic을 선택한 핵심 이유는 비용이나 기능 개수보다 **Control Plane Troubleshooting Visibility를 보존하기 위해서**다.

1차에서는 kubeadm Control Plane을 직접 구축·운영했다.  
2차 Managed Platform에서도 Control Plane과 Worker의 상태·로그·Operator/API 동작을 관찰하고, Self-managed Kubernetes와 Managed OpenShift의 Troubleshooting Boundary를 비교할 수 있어야 한다.

## 6.2 관리 책임 경계

ROSA Classic의 Control Plane이 고객 AWS Account/VPC에 존재한다는 사실은 **고객이 kubeadm처럼 Control Plane Lifecycle을 직접 관리한다는 의미가 아니다.**

Architecture에서 구분한다.

### 프로젝트가 수행할 것

- Control Plane / Worker 상태 확인
- OpenShift Cluster Operator 상태 확인
- 지원되는 Control Plane / Node Log 진단
- kubelet 및 Host 수준의 지원되는 진단
- API / Operator 이상 상황 분석
- 1차 Self-managed Kubernetes와 Managed Responsibility 비교

### 프로젝트 목표가 아닌 것

- AWS Console에서 ROSA Control Plane EC2 강제 종료
- etcd 직접 수정
- Control Plane OS 수동 변경
- Static Pod 임의 변경
- Red Hat 관리 책임 범위의 Lifecycle을 직접 운영

따라서 발표나 문서에서는 **“ROSA Master를 직접 운영했다”**고 표현하지 않는다.

정확한 표현은:

> **ROSA Classic에서 Managed Service가 허용하는 Control Plane 진단 범위를 활용하고, 1차 Self-managed Kubernetes와 운영책임 및 Troubleshooting Boundary를 비교했다.**

이다.

---

# 7. Platform HA와 Application HA의 구분

ROSA Classic을 Multi-AZ로 구성했다는 사실만으로 Application이 Multi-AZ HA가 되는 것은 아니다.

```text
Platform Multi-AZ
≠
Application HA
```

Frontend / Backend는 후속 Application 상세설계에서 다음을 별도로 결정한다.

- Replica 수
- AZ 분산 Scheduling
- Pod Anti-Affinity 또는 Topology Spread
- PodDisruptionBudget
- Resource Request / Limit
- Rollout / Rollback

최종 Availability Test에서는 최소 다음을 구분한다.

1. Pod Failure
2. Worker Failure
3. AZ 수준 영향
4. Application Replica 복구
5. User-visible Service 영향

ROSA의 기본 Self-Healing 자체를 팀이 구현한 HA 기능처럼 표현하지 않는다.

---

# 8. Primary Database — Amazon RDS for MariaDB Multi-AZ

## 8.1 확정 구성

Cloud Primary DB는 **Amazon RDS for MariaDB의 Multi-AZ DB instance deployment**를 사용한다.

기본 HA 모델:

```text
AZ-A                         AZ-B
Primary
   │
   │ synchronous replication
   ▼
Standby
```

정상 운영의 DB HA는 AWS 내부의 synchronous standby와 automatic failover가 담당한다.

## 8.2 RDS HA와 On-Prem Recovery 구분

```text
RDS Multi-AZ
= AWS 내부 DB HA

On-Prem Restore-based Recovery
= AWS 밖의 Recovery 검증
```

두 Failure Domain을 동일시하지 않는다.

RDS Multi-AZ 검증에서는 다음을 측정한다.

- Failover 시작 시각
- Application DB Error 발생 구간
- Standby 승격
- Application 재연결
- Read / Write 정상화 시각
- User-visible 영향시간

## 8.3 Lifecycle

RDS는 ROSA처럼 작업 Window마다 삭제하는 Ephemeral Resource가 아니다.

```text
RDS
= Persistent Data Layer
```

프로젝트 기간 동안 Data를 유지하며 미사용 기간에는 필요에 따라 Stop하여 Compute 비용을 줄인다.

Storage와 Backup 등 Stop 상태에서도 발생할 수 있는 비용은 별도로 산정한다.

---

# 9. Backup / Recovery Architecture

## 9.1 Cloud Recovery와 On-Prem Recovery를 분리

RDS Automated Backup/PITR와 On-Prem MariaDB Restore는 같은 Backup Path가 아니다.

### Cloud Recovery

```text
RDS Automated Backup / PITR
        ↓
RDS 내부 Recovery
```

목적:

- RDS 자체 Recovery
- Point-in-Time Recovery
- AWS 내부 운영 실수·장애 대응

### On-Prem Restore-based Recovery

```text
RDS MariaDB
     ↓
Portable Logical Backup
     ↓
S3
     ↓
장애 선언 전 On-Prem Recovery Storage / NFS로 사전 동기화
     ↓
AWS/RDS Recovery Scenario 선언
     ↓
On-Prem에 이미 존재하는 Backup Artifact 사용
     ↓
On-Prem MariaDB Restore
```

On-Prem Recovery를 위해서는 Cloud 밖에서 복원 가능한 **portable backup artifact**가 필요하다.

**AWS/RDS를 사용할 수 없는 Recovery Scenario를 주장하려면 Backup Artifact가 장애 선언 전에 On-Prem Recovery Storage까지 동기화되어 있어야 한다. S3에만 존재하는 Backup은 AWS 외부 Recovery Evidence로 간주하지 않는다.**

따라서 실제 RPO에는 Logical Backup 생성 주기뿐 아니라 On-Prem으로의 복제·전송 주기와 지연도 영향을 준다.

구체적인 Logical Backup Tool, Schedule, 전송 방식은 Data 상세설계에서 확정한다.

## 9.2 B1 Recovery의 성공 경계

B1의 Must Recovery는 다음까지다.

```text
Backup Artifact 확보
        ↓
On-Prem MariaDB Restore
        ↓
Schema 확인
        ↓
Row Count / 대표 데이터 확인
        ↓
대표 Read / Write
        ↓
Recovery Validation용 Redis Runtime 준비
        ↓
Application Backend 연결
        ↓
서비스 동작 확인
        ↓
RTO / RPO 측정
```

Application Backend가 Redis를 필수 Runtime Dependency로 사용한다면 Recovery Test에서는 **1차 On-Prem Redis 또는 신규 초기화 Redis**를 Recovery Validation Runtime으로 사용할 수 있다.

이 Redis는 Application을 실행하기 위한 새 Runtime State이며, AWS ElastiCache의 Session·Room·Game State를 On-Prem으로 복제하거나 무중단 복원한다는 의미가 아니다. ElastiCache Runtime State의 Cloud→On-Prem DR은 B1 Must 범위에 포함하지 않는다.

이 성공을 **완전한 자동 DR Site** 또는 **무중단 Failover**라고 표현하지 않는다.

다음은 B1 Must 범위가 아니다.

- Public DNS 자동 전환
- 완전 자동 Failover
- 무중단 User Traffic 전환
- Production 수준 Active-Active
- 사용자 Traffic 전체를 On-Prem으로 자동 Cutover

## 9.3 Warm DR — Should

RDS → On-Prem Continuous Replication은 Core Must가 아니다.

성공할 경우에도 Replication 자체만으로 `Warm DR 완료`라고 표현하지 않는다.

Warm DR 검증으로 승격하려면 최소 다음이 필요하다.

```text
Replication 정상
+
On-Prem Application Runtime
+
DB Endpoint 전환
+
User Access Path
+
실제 Cutover
+
대표 Read / Write PASS
```

---

# 10. Runtime State — Amazon ElastiCache for Redis OSS

## 10.1 확정 구성

2차 Runtime State 계층은 **Amazon ElastiCache for Redis OSS**를 사용한다.

기본 구조:

- Cluster Mode Disabled
- Single Shard
- Primary 1
- Replica 1
- Multi-AZ
- Automatic Failover

## 10.2 Data Responsibility

Redis는 MariaDB와 같은 영속 Business Data Source of Truth가 아니다.

```text
MariaDB
= Persistent Business Data Authority

Redis
= Runtime State
  ├─ Session
  ├─ Room
  ├─ Game State
  └─ Runtime Coordination
```

ElastiCache Redis OSS replication은 asynchronous이므로 장애 시 최신 일부 Runtime State가 손실될 가능성을 인정한다.

따라서 Test에서는 “Redis HA가 무손실”이라고 가정하지 않고 다음을 확인한다.

- Failover 중 Application 오류
- Redis reconnect
- Active Room / Game 영향
- 손실 또는 재생성된 Runtime State
- 서비스 정상화 시간

## 10.3 1차에서 2차로의 변경

1차:

```text
Redis StatefulSet
+ PVC
+ AOF
```

2차:

```text
ElastiCache
+ Managed Replication
+ Multi-AZ
+ Automatic Failover
+ 필요 시 Snapshot
```

즉 단순 Rehost가 아니라 **Replatform**이다.

## 10.4 Migration Cutover

진행 중 Redis Runtime State의 무중단 승계는 Must가 아니다.

필요 시 Maintenance Window에서:

```text
신규 Game/Room 진입 제한
        ↓
진행 중 Session Drain
        ↓
기존 Runtime Write 중지
        ↓
새 ElastiCache 기반 Application 시작
```

방식을 사용한다.

Redis Cluster Sharding, Sentinel 자체 운영, On-Prem Redis DR Replica는 Core 범위에서 제외한다.

---

# 11. CI/CD 및 Registry

## 11.1 Jenkins

기존 On-Prem Jenkins를 **Retain**한다.

책임:

- Build
- Test
- Image Build
- Image Scan
- ECR Push
- 승인된 Recovery Release의 Harbor 보존

On-Prem 전체 장애 시 이미 실행 중인 AWS Runtime은 정상 서비스할 수 있지만 신규 Build/Release는 일시 중단될 수 있다.

따라서:

```text
Runtime Availability
≠
Delivery Availability
```

로 구분한다.

## 11.2 Amazon ECR

Amazon ECR을 AWS Cloud Runtime의 **Primary Container Registry**로 사용한다.

ROSA/OpenShift GitOps의 Runtime Image Reference는 ECR을 기준으로 한다.

Image는 `latest`보다 다음과 같은 immutable identity를 사용한다.

- Commit SHA
- Immutable Release Identifier
- 가능하면 Image Digest

## 11.3 Harbor

기존 On-Prem Harbor를 Cloud Runtime의 필수 Registry 경로에서 제외한다.

Harbor의 2차 역할은:

> **On-Prem Restore-based Recovery에 필요한 Application Image를 보존하는 Recovery Registry**

이다.

일반 개발 Build는 ECR을 중심으로 운영한다.

실제 Recovery 대상이 되는 승인된 Release는 Harbor에도 보존하고 Registry별 Release ID / Digest Mapping을 기록한다.

AWS 전체 장애를 가정한 Recovery에서 ECR에만 의존하지 않도록 한다.

## 11.4 Jenkins → ECR 인증

Jenkins의 ECR Push에는 별도의 제한된 CI IAM Principal을 사용한다.

ECR Authorization Token은 Pipeline 실행 시 동적으로 발급한다.

Jenkins에 범용 Administrator 권한이나 장기 ECR Password를 저장하는 구조를 기본값으로 두지 않는다.

## 11.5 Cloud CI 전환

OpenShift Pipelines / Tekton 등 신규 Cloud CI 전환은 Core 범위에서 제외한다.

필요성이 확인되고 Must 범위가 안정된 경우 Stretch Goal로 검토한다.

---

# 12. GitOps

ROSA 내부 Application/Platform Desired State는 **OpenShift GitOps**가 관리한다.

GitOps가 관리할 범위의 예:

- Project / Namespace
- Deployment
- Service
- Route
- ConfigMap
- ServiceMonitor
- PrometheusRule
- ApplicationSet / Application
- 필요 시 NetworkPolicy 등 Cluster 내부 Desired State

Terraform이 같은 Resource를 중복 관리하지 않는다.

---

# 13. Observability

## 13.1 기본 원칙

2차 Observability는 ROSA/OpenShift가 기본 제공하는 Monitoring Stack을 중심으로 구성한다.

### Cluster / Platform

OpenShift 기본 Monitoring을 사용한다.

대상:

- Control Plane
- Cluster Operator
- Worker
- Node
- Pod
- Platform Component

### Application

User Workload Monitoring을 활성화하고 필요한 Metric과 Alert Rule만 추가한다.

예:

- Request
- Error
- Latency
- Application-specific Metric
- ServiceMonitor
- PrometheusRule

별도의 Prometheus/Grafana Stack을 ROSA에 중복 구축하는 것은 Core 범위에서 제외한다.

## 13.2 Threshold 결정 방식

임의 Threshold부터 설정하지 않는다.

```text
정상 Baseline 측정
        ↓
Failure / Load Test
        ↓
Metric 변화 확인
        ↓
User-visible 영향 확인
        ↓
Threshold 결정
        ↓
Alert 검증
```

방식을 사용한다.

## 13.3 Logs

Must 범위에서는 중앙 Log Platform 구축 자체보다 실제 Troubleshooting에 로그를 사용한다.

- `oc logs`
- Events
- Node Log
- ROSA Classic에서 허용되는 Control Plane 진단 로그
- Application Log
- AWS Managed Service Event / Metric

OpenShift Logging + LokiStack/S3, On-Prem remote_write, CloudWatch Container Insights 등은 장기 추세 분석이나 추가 요구가 확인될 경우 Should/Conditional 확장으로 검토한다.

## 13.4 Metric / Log Retention

ROSA를 삭제하면 Cluster 내부 Metric/Alert History가 함께 사라질 수 있다.

그러나 장기간 Trend 분석은 현재 Core 요구사항이 아니다.

따라서 Test가 끝나면 다음을 Cluster 밖의 Project Evidence로 보존한다.

- Metric Screenshot / Query Result
- Alert 발생 시각
- Application Log
- Node / Control Plane Log
- AWS Event
- Test Start / End Timestamp
- Recovery Time
- Actual Result
- Pass / Partial / Fail

장기 Retention 요구가 실제로 생길 때만 외부 중앙 저장을 추가한다.

## 13.5 기존 On-Prem Observability

1차 Prometheus/Grafana/Loki/Alloy는 1차 및 Recovery 환경의 Observability 자산으로 유지할 수 있다.

ROSA 정상 Runtime의 필수 의존성으로 만들지는 않는다.

---

# 14. IaC / GitOps Resource Ownership

2차 Infrastructure의 Primary IaC는 **Terraform**이다.

핵심 Ownership 경계:

```text
AWS / ROSA Infrastructure
→ Terraform

ROSA 내부 Desired State
→ OpenShift GitOps

Build / Image
→ Jenkins / Registry
```

동일 Resource를 Terraform과 GitOps가 동시에 관리하지 않는다.

## 14.1 Ownership Matrix

| Resource / 영역 | Owner |
|---|---|
| VPC / Subnet / Route / NAT / SG | Terraform |
| RDS MariaDB | Terraform |
| ElastiCache | Terraform |
| ECR | Terraform |
| S3 Backup | Terraform |
| AWS-side Hybrid Resource | Terraform |
| ROSA Classic Cluster | Terraform / RHCS |
| ROSA Machine Pool | Terraform / RHCS |
| ROSA Account-wide prerequisite | Terraform |
| Cluster-specific Operator Role / OIDC | Terraform / RHCS |
| Namespace / Project | GitOps |
| Application Deployment / Service / Route | GitOps |
| ServiceMonitor / PrometheusRule | GitOps |
| Application ConfigMap | GitOps |
| 실제 Secret 값 | 별도 Secret 공급체계 |
| Image Build / Test / Scan | Jenkins |
| Cloud Runtime Image | ECR |
| Recovery Image | Harbor |

---

# 15. Terraform State Architecture

Terraform State는 최소 3개 Lifecycle 경계로 분리한다.

```text
bootstrap
foundation
rosa
```

## 15.1 bootstrap

Terraform 자체 기반을 관리한다.

- S3 Remote Backend
- Versioning
- Encryption
- Public Access Block
- State Locking
- Backend Access Policy

최초 S3 Backend 생성 전에는 Local State로 Bootstrap하고 이후 Remote Backend로 State를 이동한다.

S3 Backend State Locking은 `use_lockfile` 방식을 우선한다.

Deprecated된 DynamoDB Locking을 신규 기본 구성으로 사용하지 않는다.

## 15.2 foundation

ROSA Cluster 삭제와 분리해 관리해야 하는 Cloud Foundation을 소유한다.

예:

- VPC / Base Network
- RDS
- ElastiCache
- ECR
- S3
- Hybrid 기반 Resource
- ROSA Account-wide Role / Policy

## 15.3 rosa

반복 생성·삭제 가능한 Platform Resource를 소유한다.

- ROSA Classic Multi-AZ Cluster
- Machine Pool
- Cluster-specific Operator Role
- Cluster-specific OIDC
- Cluster Lifecycle에 종속되는 Infrastructure

정상 비용절감을 위한 `destroy` 대상은 원칙적으로 `rosa` State로 제한한다.

`foundation`과 `bootstrap` 전체 Destroy는 별도 명시적 승인 없이는 수행하지 않는다.

---

# 16. IaC State와 Runtime Cost Lifecycle은 다르다

Terraform State가 `foundation`에 있다는 사실은 Resource를 프로젝트 기간 내내 실행한다는 뜻이 아니다.

Architecture에서는 두 종류의 Lifecycle을 구분한다.

## 16.1 IaC State Lifecycle

```text
bootstrap
foundation
rosa
```

## 16.2 Runtime Cost Lifecycle

```text
Persistent
Stoppable
Re-creatable
Ephemeral
```

예시:

| Resource | Terraform State | Runtime Cost Lifecycle |
|---|---|---|
| State Backend S3 | bootstrap | Persistent |
| VPC / Base Subnet | foundation | Persistent |
| RDS | foundation | Stoppable |
| ElastiCache | foundation | 유지 또는 Terraform Re-create |
| ECR / Backup S3 | foundation | Persistent |
| NAT Gateway | foundation | Network 설계에 따라 Re-creatable 후보 |
| ROSA Classic | rosa | Ephemeral Window |

따라서 `foundation = 항상 실행`으로 해석하지 않는다.

비용이 발생하는 Foundation Resource를 제거해야 할 경우 Console에서 수동 삭제하여 Drift를 만들지 않고 Terraform Code/Module/Flag를 통해 Lifecycle을 관리한다.

---

# 17. Manual PoC와 최종 Terraform Workflow

초기 불확실성을 줄이기 위해 **Manual PoC를 허용**한다.

목적:

- AWS/ROSA Resource 관계 이해
- IAM/OIDC 생성 흐름 이해
- Service Constraint 확인
- Terraform 작성 전 실제 Architecture 검증
- 예상하지 못한 오류 조기 발견

지원도구로 다음을 사용할 수 있다.

- AWS Console
- ROSA CLI
- CloudFormation IaC Generator
- Terraform Import
- Terraform `-generate-config-out`

그러나 자동 생성 결과는 최종 IaC가 아니다.

```text
Manual PoC
    ↓
Resource Discovery
    ↓
CloudFormation IaC Generator /
Terraform Import / Generated Config
    ↓
Reference
    ↓
Team이 Terraform 재설계
    ↓
Ownership / Module / Variable /
Output / State 경계 정리
    ↓
Manual Resource Import 또는 제거
    ↓
Terraform Clean Recreate
```

Infrastructure Reproducibility PASS는 Manual PoC 성공이 아니라 **Terraform 기반 Clean Recreate 성공**을 기준으로 한다.

---

# 18. GitOps Bootstrap

ROSA가 처음 생성된 시점에는 OpenShift GitOps가 아직 존재하지 않을 수 있다.

따라서 다음 최소 Bootstrap 단계만 별도로 허용한다.

```text
Terraform
   ↓
ROSA Ready
   ↓
GitOps Bootstrap
   ↓
OpenShift GitOps Operator
   ↓
Root Application / ApplicationSet
   ↓
나머지 Desired State는 GitOps
```

Bootstrap 구현은 작은 Script / Ansible / 적절한 자동화 수단으로 구성할 수 있다.

단 Bootstrap이 Application Manifest를 계속 직접 관리해서는 안 된다.

---

# 19. Secret Bootstrap은 Reproducibility의 필수 전제다

ROSA Clean Recreate는 Cluster와 Manifest만 다시 만들어졌다고 완료되지 않는다.

Application 동작에는 다음과 같은 Credential / Secret이 필요할 수 있다.

- Database Credential
- Redis Connection Secret
- GitOps Repository Credential
- CI/CD Credential
- Application Secret
- 기타 AWS / External Service Credential

따라서 다음 원칙을 적용한다.

> **Secret 값의 Source of Truth와 ROSA Clean Recreate 시 재주입 절차가 정의되기 전에는 Infrastructure Reproducibility를 PASS로 판단하지 않는다.**

실제 Secret Management 기술은 IAM/Security 상세설계에서 확정한다.

후보 예:

- AWS Secrets Manager
- External Secrets 계열
- Sealed Secrets 계열
- 승인된 수동 Bootstrap 절차

Secret 평문을 다음에 의도적으로 저장하지 않는다.

- Git
- Terraform Code
- `.tfvars`
- CI Log
- 발표자료

Terraform의 `sensitive` 표시만으로 Secret이 State에서 제거되는 것은 아니므로 실제 값의 Terraform State 저장을 최소화한다.

---

# 20. Terraform 변경·실행 정책

Terraform 변경은 다음 흐름을 기본으로 한다.

```text
Branch
  ↓
terraform fmt
  ↓
terraform validate
  ↓
terraform plan
  ↓
Review
  ↓
Approved Apply
```

Apply / Destroy는 지정된 실행 주체만 수행한다.

State Locking은 동시 Write 충돌을 방지하는 안전장치이며 여러 사용자가 동시에 Apply하는 운영모델을 권장한다는 의미가 아니다.

Provider / Module Version은 실제 검증한 버전으로 고정한다.

`.terraform.lock.hcl`은 Source에 포함한다.

---

# 21. OCP Demo와 ROSA의 역할 분리

교육기관에서 제공한 OCP Demo는 실제 2차 Target ROSA Environment가 아니다.

## OCP Demo — Pre-validation

용도:

- OpenShift 기본 학습
- Application Manifest 검증
- Route / Service
- GitOps
- RBAC
- Operator
- 가벼운 Integration
- 비파괴 Troubleshooting

Demo Cluster는 다른 조와 공유되는 교육환경이므로 다음에 주의한다.

- 무거운 장기 Load Test
- 파괴적인 Control Plane Test
- Cluster Scope 설정의 임의 변경
- 장기 Metric/Log 저장
- 실제 Performance Acceptance

## ROSA — Final Target / Acceptance

ROSA에서 최종적으로 검증할 것:

- AWS Integration
- Multi-AZ Platform
- RDS / ElastiCache
- ECR
- Hybrid
- Terraform Recreate
- Managed Boundary
- Control Plane Troubleshooting
- Failure / Recovery
- Performance
- Cost
- 최종 Evidence
- Demo

OCP 결과를 ROSA Target Evidence로 확대해석하지 않는다.

---

# 22. ROSA Runtime Window 운영

ROSA Classic Multi-AZ는 상시 유지하지 않는다.

비용 절감을 위해 **필요한 Integration / Validation Window에 생성하고, Evidence를 확보한 뒤 삭제 가능**하도록 운영한다.

예시:

## Window A — 최초 통합

```text
Foundation Ready
        ↓
ROSA Create
        ↓
GitOps Bootstrap
        ↓
Application
        ↓
RDS / Redis / ECR
        ↓
Hybrid
        ↓
E2E
        ↓
Evidence
        ↓
ROSA Destroy
```

## Window B — Acceptance / Failure

```text
Clean Recreate
        ↓
Failure / Recovery Test
        ↓
Performance
        ↓
Observability
        ↓
Evidence
        ↓
ROSA Destroy
```

## Window C — Final Demo 필요 시

```text
Clean Recreate
        ↓
최종 검증
        ↓
Demo / 영상 / Screenshot
        ↓
Evidence
        ↓
ROSA Destroy
```

매일 기계적으로 삭제·재생성하는 것을 목표로 하지 않는다.

Clean Recreate는 재현성을 증명할 만큼 의도적으로 수행한다.

---

# 23. Cost Gate

본 프로젝트 AWS Credit / 지원 한도는 총 $500이다.

현재 Architecture는 다음과 같은 주요 비용 Resource를 포함한다.

- ROSA Classic Multi-AZ
- Control Plane / Infrastructure / Worker EC2
- EBS
- Load Balancer
- RDS MariaDB Multi-AZ
- ElastiCache Primary + Replica
- NAT / Public IPv4
- Hybrid EC2 또는 관련 Resource
- ECR / S3
- Data Transfer
- 기타 Managed Service

따라서 **첫 Full Terraform Apply 전에 Cost Baseline Gate를 통과해야 한다.**

Cost Gate에서 최소 다음을 계산한다.

- AWS Region
- ROSA Node / Instance 구성
- 예상 ROSA Runtime Hour
- RDS Instance Class / Storage
- ElastiCache Node Type
- NAT 수량 및 실행시간
- Load Balancer 수
- Public IPv4
- VPN Resource
- EBS
- S3 / ECR
- 예상 Data Transfer

결과:

```text
Hourly Baseline
Daily Baseline
예상 Integration Window 비용
최대 허용 ROSA Runtime
예산 잔여분
```

을 산출한다.

현재 Architecture는 비용 계산 전에도 성립하지만, Cost Gate가 $500 한도를 만족하지 못하면 Resource Sizing 또는 Runtime Window를 재검토한다.

---

# 24. Network Architecture에 넘기는 불변조건

VPC / CIDR / Subnet / NAT / Ingress / API / WireGuard 등은 후속 Network 상세설계에서 확정한다.

다만 다음은 Target Architecture의 불변조건이다.

## N1. 정상 Runtime은 On-Prem에 의존하지 않는다

```text
User → ROSA → RDS / Redis
```

경로에 Hybrid Tunnel을 넣지 않는다.

## N2. Data Service는 Public Internet에 직접 노출하지 않는다

- RDS
- ElastiCache

의 Public Exposure를 기본값으로 두지 않는다.

## N3. Control Plane 접근요구를 유지한다

ROSA Classic의 Control Plane 진단 요구, Security, 비용을 함께 고려해 Public / Private API 및 접근방식을 상세설계한다.

## N4. CIDR 충돌을 사전에 제거한다

최소 다음을 함께 비교한다.

- On-Prem Private Network
- 1차 On-Prem Kubernetes Pod / Service CIDR
- AWS VPC CIDR
- ROSA Machine CIDR
- ROSA Service CIDR
- ROSA Pod CIDR
- Hybrid Tunnel CIDR
- 기타 Docker/VM Network

---

# 25. Failure Domain

Architecture의 핵심 Failure Domain은 다음과 같다.

| Failure Domain | 기본 대응 | 검증 방향 |
|---|---|---|
| Application Pod | Kubernetes/OpenShift Replica | Pod Failure / Recovery |
| Worker | ROSA Multi-AZ + App Replica | Worker 장애 영향 |
| ROSA AZ | Multi-AZ Platform | 다른 AZ에서 서비스 가능 여부 |
| Control Plane 이상 | Managed ROSA + 지원 진단 | Operator/API/Log 분석 |
| RDS Primary / DB AZ | RDS Multi-AZ | Forced Failover / App reconnect |
| Redis Primary | ElastiCache Multi-AZ | TestFailover / Runtime State 영향 |
| Hybrid Tunnel | Runtime 경로와 분리 | Tunnel Down 중 AWS Service PASS |
| On-Prem 전체 | Cloud Primary | Runtime 유지 / Delivery·Recovery 영향 |
| AWS/RDS Recovery Scenario | On-Prem Restore | Backup→Restore→App 연결 |
| 잘못된 배포 | GitOps / Rollback | Rollout / Rollback |
| Secret Bootstrap 실패 | Reproducibility FAIL | Clean Recreate 시 Secret 재주입 |

---

# 26. Minimum Validation Matrix

Target Architecture를 실제로 주장하려면 최소 다음 Evidence가 필요하다.

## 26.1 Runtime

- User → Frontend → Backend
- Backend → RDS
- Backend → ElastiCache
- 정상 기능 PASS

## 26.2 ROSA

- Classic Multi-AZ 정상 생성
- Control Plane / Worker 상태
- GitOps Bootstrap
- Clean Recreate
- Control Plane 진단 Evidence
- Application HA 별도 검증

## 26.3 RDS

- MariaDB Migration
- Multi-AZ 정상
- Forced Failover
- Application reconnect
- Read / Write 정상화 시간

## 26.4 Redis

- Application Runtime State 정상
- Multi-AZ / Automatic Failover
- TestFailover
- Runtime State 영향
- Recovery Time

## 26.5 Hybrid

- AWS ↔ On-Prem 통신
- Backup / Recovery 경로
- Tunnel Down
- Tunnel Down 상태에서 AWS 정상 서비스 PASS

## 26.6 Recovery

- Portable Backup Artifact 생성
- 장애 선언 전 On-Prem Recovery Storage까지 사전 동기화
- On-Prem MariaDB Restore
- Schema / Row Count / Data 검증
- Read / Write
- Recovery Validation용 Redis Runtime 준비
- Application Backend 연결
- 서비스 동작 확인
- RTO / RPO

## 26.7 CI/CD

- Jenkins Build / Test / Scan
- ECR Push
- ECR Image 기반 ROSA 배포
- 승인 Release의 Harbor Recovery Copy
- GitOps Deployment

## 26.8 Observability

- 정상 Baseline
- 장애 주입
- Metric / Event / Log 변화
- Alert
- 원인 판단
- Recovery
- 정상화
- 외부 Evidence 저장

## 26.9 IaC

- Remote State 정상
- Foundation Apply
- ROSA Apply
- GitOps Bootstrap
- Application Ready
- Secret Bootstrap
- ROSA Destroy
- Clean Recreate
- Foundation Data 유지

## 26.10 Cost

- Actual AWS Cost 기록
- 예상값과 Actual 비교
- 차이 원인 기록
- $500 범위 확인

---

# 27. Architecture의 명시적 Validation Boundary

다음 표현은 실제 Evidence가 없으면 사용하지 않는다.

- 완전한 3-AZ Active-Active 서비스
- 무중단
- 완전한 DR Site
- 자동 DR
- Redis 무손실 HA
- ROSA Control Plane 직접 운영
- IaC 완전 자동화
- Production 수준 HA
- Production 수준 Security
- 장기 SLO Platform

실제 수행 수준에 맞게 다음처럼 표현한다.

- ROSA Classic Multi-AZ를 구성하고 Application Availability를 별도 검증
- RDS Multi-AZ failover에서 Application 영향과 복구시간 측정
- ElastiCache failover에서 Runtime State 영향 측정
- On-Prem Restore-based Recovery 검증
- Hybrid Tunnel을 정상 Runtime에서 분리하고 Tunnel Down 영향 확인
- Terraform Clean Recreate + GitOps Desired State 복원
- Managed OpenShift의 Control Plane 진단·책임 경계 비교

---

# 28. Confirmed Architecture Decision Summary

| 영역 | 확정 내용 |
|---|---|
| Target Model | **Cloud Primary + On-Prem Restore-based Recovery** |
| OpenShift | **ROSA Classic Multi-AZ** |
| OCP Demo | **Pre-validation 환경** |
| Application Runtime | **ROSA** |
| Primary DB | **Amazon RDS for MariaDB Multi-AZ DB instance deployment** |
| Recovery DB | **On-Prem MariaDB Restore Target** |
| Redis | **ElastiCache for Redis OSS / Single Shard / Primary+Replica / Multi-AZ / Auto Failover** |
| CI | **On-Prem Jenkins Retain** |
| Cloud Registry | **Amazon ECR** |
| Recovery Registry | **On-Prem Harbor** |
| GitOps | **OpenShift GitOps** |
| Observability | **OpenShift Native Monitoring + User Workload Monitoring** |
| Long-term Observability | **필수 아님 / 필요 시 확장** |
| IaC | **Terraform** |
| Terraform State | **bootstrap / foundation / rosa** |
| Manual PoC | **허용, 최종 IaC는 Terraform Clean Recreate로 검증** |
| On-Prem Recovery | **장애 전 사전 동기화된 Portable Backup → MariaDB Restore → Recovery Redis Runtime → Data/App 검증** |
| Warm DR | **Should / 별도 승격 조건** |
| Hybrid Runtime Dependency | **정상 사용자 경로에서는 제외** |
| ROSA Lifecycle | **필요한 Validation Window에 생성·삭제 가능** |
| RDS Lifecycle | **Persistent / 필요 시 Stop** |
| Secret Bootstrap | **Reproducibility 필수 Dependency** |
| Cost Gate | **첫 Full Apply 이전 필수** |

---

# 29. 현재 미확정 사항

다음은 Target Architecture를 변경하지 않고 후속 상세설계에서 결정한다.

## Network / Access

- AWS Region
- VPC 수
- VPC CIDR
- Public / Private Subnet
- ROSA Machine / Service / Pod CIDR
- ROSA API Public / Private
- User Ingress 구조
- OpenShift Route / AWS Load Balancer 관계
- NAT Gateway 수 및 Lifecycle
- EIP / Public IPv4
- DNS
- Hybrid Network 최종 방식
- WireGuard 최종 채택 여부 및 Gateway 위치
- Hybrid HA

## IAM / Security / Secret

- 팀 Human IAM 모델
- Terraform 실행 Role
- ROSA Account / Operator Role 세부정책
- Jenkins ECR IAM Principal
- Secret Management 기술
- Secret Bootstrap 구현
- Certificate / TLS 경계

## Sizing / Application

- ROSA Instance Type / Worker Count
- Frontend / Backend Replica
- PDB / Topology 정책
- RDS Instance Class / Storage
- ElastiCache Node Type
- Backup Schedule / Retention

## Migration / Recovery

- 실제 Migration Seed SHA
- MariaDB Migration 절차
- Portable Logical Backup 도구
- Cutover Window
- Redis Drain 절차
- Warm DR 실행 여부

## Delivery / Repository

- 2차 최종 Repository Topology
- GitOps Repository 구조
- Release Promotion 절차
- Recovery Release Metadata 형식
- Evidence 저장 위치

## Test

- 수치 Baseline
- Target SLO가 아닌 프로젝트용 Acceptance Threshold
- Performance Scenario
- 최종 Failure Test Matrix
- Demo Scenario

---

# 30. 다음 단계 Input

Target Architecture가 확정되었으므로 다음 단계는 이 Architecture를 바꾸지 않는 범위에서 상세설계를 수행한다.

권장 의존순서는 다음과 같다.

```text
Target Architecture
        ↓
Repository / Source Boundary
        ↓
Network / IPAM / Hybrid
        ↓
IAM / Secret Bootstrap
        ↓
Migration Matrix / Seed
        ↓
Interface Contract
        ↓
Terraform / GitOps 구현구조
        ↓
Test / Evidence Matrix
        ↓
Implementation
```

실제 진행순서는 일정과 팀 병렬작업을 고려해 조정할 수 있다.

단, 후속 설계가 다음 Architecture Invariant를 깨는 경우에는 본 문서를 다시 검토한다.

1. 정상 Runtime이 On-Prem/Hybrid에 의존하지 않음
2. ROSA Classic Multi-AZ 유지
3. RDS Multi-AZ / ElastiCache Multi-AZ 유지
4. AWS HA와 On-Prem Restore-based Recovery를 구분
5. Terraform과 GitOps Ownership 충돌 금지
6. ROSA만 반복 생성·삭제할 수 있는 Lifecycle 경계 유지
7. Secret Bootstrap 없는 Clean Recreate를 PASS로 인정하지 않음
8. $500 Cost Gate 유지
9. Platform 기본기능과 팀의 실제 기여를 과장 없이 구분

---

# 31. Architecture 완료 판정

본 Architecture는 다음 조건을 충족하여 Target Architecture 단계 완료 기준으로 사용한다.

> **이 절의 `[x]`는 Architecture/설계 결정이 확정되었음을 의미한다. 실제 AWS Resource 구축, Runtime 동작 검증 또는 Evidence 확보가 완료되었다는 의미가 아니다. 구현·검증 완료 상태는 후속 Current State / Test Evidence에서 별도로 관리한다.**

- [x] Cloud Primary / On-Prem 역할 확정
- [x] 정상 서비스 경로 확정
- [x] Hybrid Link의 책임 확정
- [x] ROSA Platform 모델 확정
- [x] RDS 배치 및 HA 모델 확정
- [x] Redis 배치 및 HA 모델 확정
- [x] CI/CD 및 Registry 역할 확정
- [x] Observability 기본 모델 확정
- [x] Terraform / GitOps Ownership 확정
- [x] Terraform Lifecycle 경계 확정
- [x] Restore-based Recovery의 Validation Boundary 확정
- [x] Cost 및 Secret Bootstrap Gate 추가
- [x] Architecture 전체 연쇄·재귀 검토 완료
- [x] 사용자 최종 승인 완료

후속 상세설계는 본 문서를 Source of Truth로 사용한다.
