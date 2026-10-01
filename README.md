# seokpan-hybrid-docs
Seokpan 2차 - 하이브리드 클라우드 기획·아키텍처·검증 문서

1차 온프레미스 프로젝트를 기반으로 AWS 하이브리드 환경으로 이전하는 2차 프로젝트의 문서 저장소입니다. 승인된 목표는 **Cloud Primary + On-Prem Restore-based Recovery**입니다. 설계 승인과 실제 구축·시험 결과를 구분합니다.

## Planning & Design

[설계문서 목차](design/README.md)에서 프로젝트 소스 00~04의 원문과 문서별 역할을 확인합니다.

| 번호 | 문서 | 역할 |
| --- | --- | --- |
| 00 | [Project Starting Point](design/00_PROJECT_STARTING_POINT.md) | 1차 종료 상태와 2차의 역사적 출발점 |
| 01 | [Project Charter](design/01_PROJECT_CHARTER.md) | 목적·범위·기간·비용·성공 기준 |
| 02 | [Target Architecture](design/02_TARGET_ARCHITECTURE.md) | Cloud Primary와 On-Prem Recovery의 목표 구조 |
| 03 | [Detailed Design](design/03_DETAILED_DESIGN.md) | Network·Data·App·IAM·IaC·GitOps·시험·WBS 상세설계 |
| 04 | [Implementation Readiness](design/04_IMPLEMENTATION_READINESS.md) | 운영 결정·담당·실제 입력·실행 Gate·구현 인계 |

03과 04는 문서 단계가 종료됐습니다. 이전 문서의 당시 미확정 표기는 후속 승인·결정과 함께 읽습니다. 실제 지원·주소·용량·비용·Plan 및 Runtime 시험 완료는 별도 증거로 확인합니다.

## Architecture

[다이어그램 제작 계획](architecture/DIAGRAM_PLAN.md)에 설계 기준 12장의 목적·내용·참조 문서·제작 순서를 정리했습니다. 장수와 표현 방식은 사용자 검토 전 제안이며, 이미지는 아직 제작하지 않았습니다.

전체 논리·물리 아키텍처는 지금 목표 설계로 제작할 수 있습니다. 실제 구축 구조와 시험 결과를 보여주는 그림은 구현·검증 기록을 확인한 뒤 작성합니다.

## Implementation & Validation

프로젝트 소스의 다음 단계는 `05_IMPLEMENTATION_AND_VALIDATION.md`입니다. 실제 입력 확인·코드·통합·Migration·시험·Evidence·정리를 기록합니다. 이번 등록에는 05 사본이 제공되지 않아 포함하지 않았습니다.

검증 Run의 기록 위치와 형식은 04의 승인 기준을 따릅니다. 실행 기록이 제공되면 설계문서 원문을 덮어쓰지 않고 해당 시점의 구현·검증 상태와 연결합니다.
