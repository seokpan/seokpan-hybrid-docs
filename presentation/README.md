# Presentation

이 폴더는 석판 2차 프로젝트의 **최종 발표 준비 기준과 후속 발표 산출물**을 관리합니다.

현재는 실제 05 결과가 충분히 나오기 전이므로 발표 슬라이드나 Demo 대본을 먼저 확정하지 않습니다. 프로젝트의 공식 Test/Acceptance와 실제 Evidence를 우선하고, 발표는 그 결과를 선별해 설명합니다.

## Start Here

1. [PRESENTATION_BASELINE.md](PRESENTATION_BASELINE.md) — 발표 Narrative, 과장 방지, 1차 비교, Troubleshooting 및 Evidence 선별 기준
2. [Tracking Issue #6](https://github.com/seokpan/seokpan-hybrid-docs/issues/6) — 05에서 발생하는 발표 후보 Evidence 진행상태 추적
3. 실제 실행 결과는 `evidence/<test-id>/<run-id>/`를 원본으로 사용

## 다른 문서와의 관계

| 영역 | 역할 |
| --- | --- |
| `design/03_DETAILED_DESIGN.md` | 공식 Test/Acceptance 및 상세설계 기준 |
| `design/04_IMPLEMENTATION_READINESS.md` | 실행 준비, Release/Evidence 형식과 Gate |
| `execution/05_IMPLEMENTATION_AND_VALIDATION.md` | 실제 구현·통합·검증 진행과 Actual |
| `evidence/` | 실제 Run·Metric·Timeline·실패/재시험 원본 |
| `presentation/` | 원본 Evidence를 발표 관점에서 선별하는 기준과 최종 발표 산출물 |

`design/`, `architecture/`, `execution/`, `evidence/`의 선행 문서 작업은 main에 병합되어 있습니다. Presentation은 해당 원본을 중복 수정하지 않고 경로·Issue로 연결하며, 실제 Run의 정본은 `evidence/`에 유지합니다.

## 원칙

- 제품 기본기능이나 일반 구축 절차를 특별한 팀 성과처럼 과장하지 않습니다.
- 설계 판단, 실제 구현, 실제 검증, Troubleshooting을 구분합니다.
- 발표용 수치를 새로 만들지 않고 실제 Evidence를 참조합니다.
- 실패·PARTIAL·N/A·NOT RUN과 한계를 숨기지 않습니다.
- 1차↔2차 비교는 조건이 맞는 항목만 수행하고 직접 비교가 부적절한 경우 운영책임·구조 차이를 설명합니다.
- 발표 때문에 공식 Test 조건이나 성공 기준을 바꾸지 않습니다.

## 향후 파일

Actual이 충분히 확보된 뒤 필요에 따라 다음 문서를 추가합니다.

- `PRESENTATION_OUTLINE.md`
- `DEMO_SCENARIO.md`
- `QNA.md`

현재는 위 문서를 빈 틀로 미리 만들지 않습니다.
