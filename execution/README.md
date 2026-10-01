# Implementation and Validation

이 폴더는 석판 2차 프로젝트의 **지금 공유해서 쓰는 작업 안내와 공동 진행 기록**입니다. 05 최종 완료를 기다리지 않고 각자 준비·구현·인계를 진행합니다. 정태훈이 모든 결과를 받아 대필하는 방식으로 운영하지 않습니다.

> 공유용 PR의 진행본입니다. main 병합·팀원별 읽기/쓰기·실제 사용 확인은 별도입니다. 현재 역할별 실적은 담당자가 자기 근거와 확인 시각을 연결해야 합니다.

## Start Here

1. [05 공통 안내](05_IMPLEMENTATION_AND_VALIDATION.md#09-문서와-진행표-운영)와 아래 본인 역할을 읽습니다.
2. [공통 진행표](WORK_TRACKER.md)의 자기 작업/입력 행에 **기존 Issue·PR와 확인한 입력**을 연결합니다. 필요한 입력이 없으면 해당 실행만 대기로 남기고 독립 준비를 계속합니다.
3. 자기 Issue/PR에 진행·차단·검사 결과를 기록하고 [인계 양식](HANDOFF_TEMPLATE.md)으로 결과 수신자에게 직접 넘깁니다. 수신자는 받은 개정과 수락/보완 범위를 기록합니다.
4. 실제 실행은 [Evidence 안내](../evidence/README.md)에 따라 새 Run으로 남기고 Index와 진행표에 링크를 연결합니다. 코드 Merge와 최종 시험 PASS를 구분합니다.

## Role Entry Points

| 담당 | 먼저 읽기 | 본인이 기록할 곳 | 다음 인계 |
| --- | --- | --- | --- |
| 이유빈 | [기반/foundation 첫 작업](05_IMPLEMENTATION_AND_VALIDATION.md#이유빈) | Infra 작업 Issue/PR, 진행표 I02·기반 인계 | B ROSA, C Data, D Registry/비용 |
| 정태훈 | [App/GitOps/ROSA 첫 작업](05_IMPLEMENTATION_AND_VALIDATION.md#정태훈) | App/GitOps/ROSA Issue/PR, I01·I02·I06 | D Build/lab, C Data/Recovery, A 기반 |
| 김상희 | [Data/Recovery 첫 작업](05_IMPLEMENTATION_AND_VALIDATION.md#김상희) | Infra Data/Restore Issue/PR, I03·범위별 I05 | A foundation, B App/복구, D 증거 |
| 최유준 | [CI/lab/시험 첫 작업](05_IMPLEMENTATION_AND_VALIDATION.md#최유준) | CI/GitOps lab Issue/PR, I04·I07·Evidence Index | A Registry/CI, B Image/lab, C Recovery |

## Where to Write

| 내용 | 기록 위치 |
| --- | --- |
| 필요한 입력·제공된 개정·아직 없는 값 | [진행표의 I01~I07](WORK_TRACKER.md#input-handover)와 해당 작업 Issue의 인계 기록. 공개 표에는 비민감 값/논리 참조만 |
| 진행·Blocker·결과 제출/수신 확인 | 해당 App/Infra/GitOps 작업 Issue. 인계 양식을 댓글/본문에 사용하고 별도 최신본을 중복 작성하지 않음 |
| 코드·검사·리뷰 | 해당 Branch/PR |
| 실제 실행·수치·실패·시간선 | Docs의 evidence/&lt;test-id&gt;/&lt;run-id&gt;/ — [빈 양식](../evidence/_template/summary.md)에서 시작 |
| 전체 인계·통합 Gate | [공통 진행표](WORK_TRACKER.md), [단일05](05_IMPLEMENTATION_AND_VALIDATION.md)에는 링크와 집계 시각 |

새 Issue 번호·수행자·실제 시각·성공값을 미리 만들어 채우지 않습니다. 기존 Issue가 범위를 담으면 이어 쓰고 별도 산출물/종료 조건이 필요할 때만 나눕니다. 같은05 편집은 최신 정본과 타 담당 기록을 대조하며, 독립 작업/직접 인계는 문서 Merge를 기다리지 않습니다.

## Approved References

설계 등록 [PR #3](https://github.com/seokpan/seokpan-hybrid-docs/pull/3)는 조회 시 main 미병합입니다. 아래 고정 Commit의 원문5개는 첨부와 바이트 동일성을 확인했습니다. 이 공유 PR에서는 원문을 중복 등록하거나 다이어그램 계획을 변경하지 않습니다.

- [00 출발점](https://github.com/seokpan/seokpan-hybrid-docs/blob/5d6c917b0b39ca1d132b1ae6a9d6c9adfd428b0d/design/00_PROJECT_STARTING_POINT.md)
- [01 기획/성공 기준](https://github.com/seokpan/seokpan-hybrid-docs/blob/5d6c917b0b39ca1d132b1ae6a9d6c9adfd428b0d/design/01_PROJECT_CHARTER.md)
- [02 목표 아키텍처](https://github.com/seokpan/seokpan-hybrid-docs/blob/5d6c917b0b39ca1d132b1ae6a9d6c9adfd428b0d/design/02_TARGET_ARCHITECTURE.md)
- [03 상세설계·시험·WBS/비용](https://github.com/seokpan/seokpan-hybrid-docs/blob/5d6c917b0b39ca1d132b1ae6a9d6c9adfd428b0d/design/03_DETAILED_DESIGN.md)
- [04 배정·I01~I07·인계/Run 양식](https://github.com/seokpan/seokpan-hybrid-docs/blob/5d6c917b0b39ca1d132b1ae6a9d6c9adfd428b0d/design/04_IMPLEMENTATION_READINESS.md)

구조와 시험 목표는 승인03/04, 최신 사용자 결정과 등록 프로젝트 지침을 따릅니다. 팀원이 모든 원문을 처음부터 다시 읽어야 작업을 시작하는 조건은 아닙니다. 공통 안내·본인 작업·관련 근거/인계부터 확인합니다.
