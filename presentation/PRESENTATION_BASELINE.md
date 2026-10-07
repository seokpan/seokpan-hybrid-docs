# 石나가는 판단 2차 프로젝트 — Presentation Baseline

> **목적:** 05 구현·통합·검증에서 발생하는 실제 결과를 최종 발표 관점에서 놓치지 않고 선별하기 위한 기준
> **기준일:** 2026-10-02 KST
> **상태:** USER-CONFIRMED PRESENTATION BASELINE — 05 Actual/Evidence 연동 대기
> **적용 범위:** 최종 발표 Narrative, 정량 Evidence, 1차↔2차 비교, Troubleshooting, Demo 후보 선별
> **중요:** 이 문서는 03의 Test/Acceptance 기준이나 05의 실행 결과를 대체하지 않는다.

현재 진행 현황:

- [x] 발표 기본 Narrative 정리
- [x] 과장 방지·Contribution/Evidence 기준 정리
- [x] 발표용 핵심 검증 질문 6개 정리
- [x] 1차 비교 Baseline 재측정 원칙 정리
- [x] 1차↔2차 비교 분류 기준 정리
- [x] Troubleshooting 선별 기준 정리
- [x] 05 Evidence → 발표 후보 선별 흐름 정리
- [ ] 05 실제 Run/Actual 확보
- [ ] 필요한 1차 비교 Baseline 재측정
- [ ] 실제 Troubleshooting 후보 확정
- [ ] 최종 발표 목차·슬라이드·Demo·대본·Q&A 확정

## 1. 문서의 역할과 기준

이 문서는 발표를 먼저 만들고 프로젝트 결과를 거기에 맞추기 위한 문서가 아니다.

프로젝트의 순서는 다음을 유지한다.

```text
Requirement
→ Test / Validation
→ Actual Result
→ Evidence
→ Interpretation
→ Presentation Selection
```

공식 Test와 Acceptance Criteria는 승인된 03 상세설계를 따른다. 실제 입력·실행·통합·시험 결과는 05와 `evidence/<test-id>/<run-id>/`에 기록한다. 이 문서는 그 결과 중 최종 발표에서 설명할 가치가 있는 것을 선별하는 기준만 제공한다.

현재 저장소 기준은 다음과 같다.

- 승인 00~04 원문과 설계 자료: PR #3 병합 완료
- 05 협업 실행 안내와 Evidence 양식: PR #5 병합 완료
- 발표 Baseline 등록 이력: PR #7
- 발표 Evidence 추적: Issue #6

기준 경로는 다음을 사용한다.

- `design/03_DETAILED_DESIGN.md`
- `design/04_IMPLEMENTATION_READINESS.md`
- `execution/05_IMPLEMENTATION_AND_VALIDATION.md`
- `evidence/<test-id>/<run-id>/`

## 2. 발표 기본 Narrative

최종 발표의 기본 흐름은 다음을 출발점으로 한다.

```text
1차 As-Is
→ Migration 필요
→ 무엇을 왜 유지 / 이전 / 대체했는가
→ Target Architecture
→ 실제 구축
→ 실제로 무엇이 일어났는가
→ Troubleshooting
→ 정량 검증
→ 1차↔2차 비교
→ 목표 달성 및 한계
→ Demo
→ 정리 / Q&A
```

이 흐름은 현재의 준비 기준이며 최종 슬라이드 목차나 장수를 의미하지 않는다. 05의 실제 결과에 따라 순서와 비중은 변경할 수 있다.

## 3. Contribution & Evidence Integrity

발표에서는 다음 여섯 범주를 구분한다.

1. 제품·플랫폼이 기본 제공하는 기능
2. 일반적인 구축 절차
3. 팀이 직접 비교·선택한 설계
4. 팀이 직접 구현·자동화한 부분
5. 팀이 실제로 검증한 결과
6. 팀이 직접 발견하고 해결한 문제

기본 기능이나 통상적인 절차를 대표 성과로 과장하지 않는다.

| 사례 | 표현 기준 |
| --- | --- |
| Kubernetes/OpenShift가 Replica를 다시 배치 | 플랫폼 기본 동작을 확인 |
| OpenShift Route 적용 | 기능 사용·적용 |
| Terraform으로 VPC/자원 생성 | IaC로 구성·관리 |
| 실제 환경 제약을 놓고 Network 대안을 비교·선택 | 팀의 설계 판단 |
| 장애를 주입하고 사용자 영향·RTO 등을 측정 | 팀의 검증 결과 |
| 예상과 다른 문제를 분석·수정하고 동일 조건 재시험 | Troubleshooting / 문제해결 |

다음 표현은 실제 Evidence 범위를 넘지 않을 때만 사용한다.

- 구현
- 자동화
- 고가용성
- HA
- DR
- 무중단
- 최적화
- 개선

숫자나 플랫폼 기능이 좋게 보인다는 이유만으로 팀의 독자 성과로 승격하지 않는다.

## 4. 발표 가치 Filter

실제 Run이나 사건이 발생했을 때 다음 순서로 판정한다.

| 질문 | 판정 기준 |
| --- | --- |
| 실제로 무엇이 관측됐는가? | Log/Metric/Timeline/Run으로 사실 확인 |
| 제품 기본기능 또는 일반 절차인가? | 그 자체만으로 Highlight로 승격하지 않음 |
| 팀의 판단·구현·검증·Troubleshooting은 무엇인가? | 팀 기여 범위를 구체적으로 분리 |
| 사용자 또는 운영에 어떤 차이가 있었는가? | 실제 영향과 조건을 기록 |
| 정량 Evidence가 있는가? | 있으면 단위·집계·시험조건과 함께 사용 |
| 실패·Partial·N/A·제한을 그대로 설명할 수 있는가? | 숨기지 않고 발표 후보 판단 |
| 과장된 수식어 없이도 의미가 있는가? | 그렇지 않으면 메인 발표 후보에서 제외 |

발표 후보는 Evidence가 있다는 이유만으로 자동 승격하지 않는다.

## 5. 발표에서 답할 여섯 검증 질문

| ID | 질문 | 현재 확보된 입력 | 05에서 필요한 결과 |
| --- | --- | --- | --- |
| Q1 | 왜 이 Architecture를 선택했는가? | 01~04의 설계·Trade-off | 실제 구현 제약과 구현 후 평가 |
| Q2 | Migration 후 서비스 특성은 어떻게 달라졌는가? | Performance/Test 설계 | 2차 Actual과 필요한 1차 비교 Baseline |
| Q3 | 장애 시 사용자에게 실제 어떤 영향이 있었는가? | T10~T14 등 Failure Scenario | 오류·영향·복구의 실제 시간선과 업무 결과 |
| Q4 | 장애 후 실제 복구 가능한가? | Offline Recovery 설계·RTO/RPO 목표 | T18 Actual과 데이터/업무 확인 |
| Q5 | 환경을 다시 만들 수 있는가? | T19 Clean Recreate 설계 | Cluster→Secret→GitOps→App→E2E 실제 결과 |
| Q6 | 설계 예상과 실제는 어디서 달랐는가? | 설계 예상·제약 | Troubleshooting, 실패, 비용, 제한, 수정 전후 |

이 질문은 발표 선별을 위한 내부 프레임이며 03의 공식 T01~T23을 대체하지 않는다.

## 6. 공식 정량 목표와 발표 사용 원칙

공식 수치와 Acceptance는 03 §3-G.6~7을 기준으로 한다.

### Performance / Reconnect

| 단계·Metric | 승인 기준 |
| --- | --- |
| Smoke | 동시 사용자 10명, Warm-up 후 5분 |
| Baseline | 동시 사용자 30명, Warm-up 후 15분 |
| Target | 동시 사용자 60명, Warm-up 후 30분 |
| 대표 HTTP 업무 응답 p95 | 1초 이하 |
| WS 업무 결과 확인 p95 | 1초 이하 |
| 예기치 않은 업무 오류율 | 1% 미만 |
| 중복 업무 효과·권한 없는 성공·확정 데이터 불일치 | 0건 |
| WS 재접속 후 상태 수렴 | 정상 의존 서비스 가용 후 30초 이내 |

### Recovery

[Docs #30](https://github.com/seokpan/seokpan-hybrid-docs/pull/30)으로 병합된 [03 §3-I.14.5](../design/03_DETAILED_DESIGN.md#recovery-design-decision-20261005)의 승인 기준을 적용한다. 현재 목표는 RTO 10분·영속 DB RPO 30분·DB 운영 중 Portable Backup 15분 계획 주기다. 이전 30분·90분·1시간과 실제 Run의 목표/판정은 당시 기록으로 보존한다. 실제 전체 목표 달성은 해당 운영 Run에서 별도 확인한다.

| Metric | 설계 개정안의 목표 — 리뷰·병합 후 적용 |
| --- | --- |
| Offline Recovery RTO | 10분 이내 |
| 영속 DB Offline Recovery RPO | 30분 이내 |
| 운영 중 Portable Backup | 15분 주기 |
| 일반 Backup 보관 | 7일, 최종/마지막 검증 사본 별도 보호 |

위 값은 **Target**이며 실제 달성값이 아니다. 기존 Backup/Restore 구조를 유지하고, 부분 합성 예행과 운영 경로·클라이언트 전체 업무 재개·최종 T18 Acceptance를 구분한다. 조건이 맞는 실제 Run의 증거 전에는 Actual이나 PASS로 표현하지 않는다.

p50, 세부 자원 사용량, 단계별 소요시간 등 추가 관측값을 수집할 수 있으나 공식 Acceptance Metric과 구분한다.

## 7. 1차 비교 Baseline 재측정 원칙

1차 비교는 2차가 더 우월하다는 결론을 만들기 위한 작업이 아니다. Architecture 변경 후 실제 특성이 어떻게 달라졌는지를 확인하기 위한 것이다.

### 실행 시점

1차 재측정은 05에서 2차 Harness·측정 정의가 충분히 고정된 뒤 필요한 항목만 수행한다.

```text
2차 Harness / 측정 정의 고정
→ 1차에서 재현 가능성 판정
→ 발표 비교 가치 판정
→ 필요한 1차 Baseline만 재측정
→ 2차 Actual과 비교
```

### 표현

재측정 값은 다음처럼 표현한다.

> 2차 비교를 위해 1차 최신 검증 환경에서 동일 또는 대응 Harness로 재측정한 Baseline

다음처럼 표현하지 않는다.

> 1차 프로젝트 당시의 측정값

실제 1차 당시 기록이 존재하고 동일 결과라는 근거가 있는 경우만 역사적 당시 값으로 구분한다.

### 재측정 시 최소 조건

- 1차 Source Commit / Image
- 시험일
- 부하·사용자 행동 조건
- Harness / Script Commit
- Dataset 또는 Data 상태
- Network / Resource 조건
- Metric 정의와 단위
- 실제 제한사항

1차 공식 종료 Baseline과 이후 Maintenance/Validation 상태를 구분하며, 비교를 위해 1차 Architecture를 2차 방식으로 변경하지 않는다.

## 8. 1차↔2차 비교 분류

이 분류는 발표 편집을 위한 내부 기준이다.

| 분류 | 의미 | 예 |
| --- | --- | --- |
| DIRECT | 조건을 충분히 맞춘 동일/유사 시험 | 동일 App/Harness/사용자 수의 HTTP·WS 성능 |
| CONDITIONAL | 동일 Requirement지만 Architecture·Failure Mechanism이 다름 | MariaDB/MaxScale 장애 vs RDS Failover |
| DESCRIPTIVE | 숫자 우열보다 책임·구조·운영경계 비교가 중요 | kubeadm Control Plane vs ROSA Managed Boundary |
| N/A | 직접 비교 자체가 의미 없음 | 2차 Hybrid Tunnel Down |

DIRECT가 아니면 단순한 퍼센트 개선을 기본 표현으로 사용하지 않는다.

조건이 다른 수치 비교는 “동일한 사용자 관점의 Outcome에서 관측된 차이”처럼 범위를 명확히 한다.

## 9. 우선 비교 검토 대상

### 1차 재측정 우선 검토

- 대표 E2E
- HTTP 업무 p95
- WS 업무 결과 p95
- 오류율
- 업무 정확성
- WS 재접속 / 상태수렴

### 조건부 비교

- Worker 장애
- DB 장애 / Failover
- Redis 장애 / Failover
- Backup / Restore
- CI/CD 소요 및 운영방식

### 2차 독자 평가 우선

- Hybrid Tunnel Down에서 Cloud Runtime 비의존성
- Terraform/ROSA Clean Recreate
- AWS Cost / Validation Window
- Managed Responsibility / Troubleshooting Boundary

실제 비교 수행 여부는 05의 결과와 시험조건을 보고 결정한다.

## 10. 장애·복구 결과 기록 관점

발표에서는 “Failover가 됐다”보다 실제 사용자·업무 영향과 시간선을 우선한다.

가능하면 실제 발생한 주요 상태전이를 Timestamp로 남긴다.

예시 Template:

```text
장애 주입
→ 탐지
→ 사용자 영향
→ 플랫폼/서비스 복구 동작
→ Application 정상화
→ 대표 업무 정상 확인
```

모든 시험에 동일한 단계 수를 강제하지 않는다. 실제 사건에 존재하는 상태전이만 기록한다.

### 대표 후보

- Worker 장애: 재배치 자체보다 사용자 오류·업무 정상화
- RDS Failover: Failover 자체보다 App Pool/재연결·불명확한 쓰기·데이터 정합성
- Redis Failover: Failover 자체보다 Session/Room/Game Runtime 영향과 DB 확정 결과
- Hybrid Down: Tunnel 장애가 Cloud 정상 사용자 경로에 전파되는지 여부
- Offline Recovery: 단순 Import 완료가 아니라 대표 업무/Data 확인까지의 RTO/RPO
- Clean Recreate: Terraform Apply 자체보다 Secret/GitOps/App/E2E까지의 재현 여부

## 11. Troubleshooting 선별 기준

발표 우선순위를 높게 보는 사례:

- 설계 예상과 실제 Failure Mode가 달랐음
- 여러 계층을 추적해야 원인이 드러남
- 사용자 또는 데이터 정합성에 실제 영향이 있었음
- Architecture나 설정 판단을 수정하게 됨
- Root Cause가 확인됨
- 수정 후 같은 조건으로 재시험함
- 수정 전/후의 실제 차이를 보여줄 수 있음

일반적으로 우선순위가 낮은 사례:

- 단순 Typo
- YAML 들여쓰기
- 단순 Port/환경변수 오입력
- 일반 문서 절차만 따라 바로 해결되는 설치 실수

단, 작은 설정 문제라도 예상 밖 원인·영향·분석 가치가 크면 별도로 판단한다.

권장 기록 구조:

```text
Expected
→ Observed
→ Impact
→ Evidence
→ Root Cause
→ Correction
→ Retest
→ Result / Limitation
```

## 12. Project Evidence와 발표 자료의 관계

발표를 위해 실제 Evidence를 중복 생성하지 않는다.

```text
05 실행
→ evidence/<test-id>/<run-id>/ 원본 기록
→ Presentation Filter
→ Tracking Issue #6에서 후보 상태 추적
→ 최종 발표에서 필요한 Evidence만 참조
```

실제 Metric/Timeline/Log를 `presentation/`에 복사해 별도 정본으로 만들지 않는다.

04에서 정한 Run 구조를 그대로 사용한다.

- `release.json`: 실제 Source/Artifact/환경/실행 조합
- `summary.md`: 기대·실제·원인·제한·재시험
- `metrics.csv`: 실제 비민감 수치와 단위·집계
- `timeline.csv`: 실제 단계별 시각
- `checksums.txt`: 공유 가능한 산출물 무결성

실패 Run은 삭제하거나 성공 Run으로 덮어쓰지 않는다.

## 13. 05와의 통합 원칙

05에는 이 문서 전체를 복사하지 않는다.

05에서 필요한 것은 다음 Cross-reference다.

1. 공식 Test/Acceptance는 03을 따른다.
2. Actual Evidence는 05와 `evidence/`에 기록한다.
3. 발표 후보 선별·1차 비교·과장 방지 기준은 이 문서를 따른다.
4. 이 문서는 Test 성공조건을 변경하거나 발표에 유리하도록 결과를 재해석하는 근거가 아니다.

05 담당자는 실제 Run이 생성될 때 기존 Evidence 체계를 유지하고, 발표 가치가 있는 결과는 Issue #6에 원본 Evidence 링크만 연결한다.

## 14. 목표 달성 표현

최종 결과는 우선 다음 상태로 판정한다.

- PASS
- PARTIAL
- FAIL
- N/A
- NOT RUN

단일 “목표 달성률 %”를 먼저 만들지 않는다.

필요한 경우 최종 발표에서 Must 완료 수 등 계산 근거가 명확한 보조 수치를 추가할 수 있으나, 성공축마다 중요도가 다른 사실을 숨기지 않는다.

FAIL/PARTIAL/N/A/NOT RUN을 제거하기 위해 시험조건이나 기준을 사후 변경하지 않는다.

## 15. 지금 확정하지 않는 것

Actual 확보 전 다음은 확정하지 않는다.

- 최종 발표 슬라이드 수
- 최종 목차와 각 장의 비중
- 최종 그래프 종류
- 대표 Troubleshooting 사례
- 최종 Demo Script
- 1차↔2차 개선 Percentage
- 프로젝트 전체 달성 Percentage
- 최종 결론 문구
- 발표 대본과 예상 Q&A

## 16. 갱신 조건

이 Baseline은 발표 형식을 자주 바꾸기 위한 작업문서가 아니다.

다음 경우에만 실질 변경을 검토한다.

- 05에서 공식 Test/Acceptance 변경이 승인됨
- 실제 구현 제약으로 비교 가능성이 크게 바뀜
- 새로운 주요 Failure Domain 또는 Recovery 경계가 확정됨
- Demo/발표 요구사항이 외부에서 새로 주어짐
- 실제 Evidence가 기존 선별 기준의 오류를 드러냄

Actual 값 자체는 이 문서에 누적하지 않고 Evidence Run과 Tracking Issue에 연결한다.

## 17. Tracking

발표 Evidence 후보의 진행상태는 GitHub Issue #6에서 추적한다.

Issue에는 원본 수치·로그를 복사하지 않고 다음만 관리한다.

- 어떤 Test/Run에서 후보가 나왔는가
- 발표 가치 Filter를 통과했는가
- 1차 비교 분류는 무엇인가
- 주장 가능한 범위와 한계는 무엇인가
- 최종 발표 후보로 유지할 것인가

최종 Outline, Demo Scenario, Q&A 문서는 Actual이 충분히 확보된 뒤 `presentation/` 아래에 별도로 추가한다.

