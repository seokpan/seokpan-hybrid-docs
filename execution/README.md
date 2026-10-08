# Implementation and Validation

이 폴더는 석판 2차 프로젝트의 **지금 공유해서 쓰는 작업 안내와 공동 진행 기록**입니다. 05 최종 완료를 기다리지 않고 각자 준비·구현·인계를 진행합니다. 각 담당자가 원 Issue·PR·Run에 결과를 기록하고 수신자가 인계를 확인합니다.

> PR #3·#5·#7의 설계·실행·발표 문서는 main에 반영됐습니다. 변경은 Branch/PR로 검토합니다. 네 사람의 계정 매핑과 네 저장소 Repo 권한 확인은 완료됐고, 개인 본인환경의 실제 사용·현재 작업·입력 인계는 [진행표](WORK_TRACKER.md)와 [Issue #8](https://github.com/seokpan/seokpan-hybrid-docs/issues/8)에서 이어갑니다. 담당자는 자기 근거와 확인 시각을 직접 연결합니다.

## Start Here

**정태훈의 지금 작업부터 확인:** [개인 실행판 — 지금할일·막힌입력·OCP/ROSA시작과종료·타임라인](TJUNG03_EXECUTION_BOARD.md). A전체를기다리지않고가능한준비를시작하며각실제실행의직접입력과팀인계를구분합니다.

[저장소·담당별 전체 실행 순서와 현행화 점검](TEAM_EXECUTION_SEQUENCE.md)에서 현재 전체 진행, A/B/C/D의 병행 준비·실제 선행조건·W01~W10/T01~T23·최종 보존/삭제/종료를 확인합니다. PR32 병합 이후의 현행 순서를 연결하며 TH 개인 범위와 팀 전체 범위를 구분합니다.

공유용 [팀 작업·환경 전환·입력 인계 안내](TEAM_WORK_AND_HANDOFF_GUIDE.md)에서 공통 안내, OCP·ROSA 전환 조건과 본인 담당을 한 번에 확인합니다. [담당별 바로가기](TEAM_WORK_AND_HANDOFF_GUIDE.md#role-navigation)로 이동한 뒤 아래 작업/인계 기록을 이어갑니다. 이 안내는 기존 역할 배정의 참조 기록이며 실제 Run Evidence와 구분합니다.

1. [05 공통 안내](05_IMPLEMENTATION_AND_VALIDATION.md#09-문서와-진행표-운영)와 아래 본인 역할을 읽습니다.
2. [공통 진행표](WORK_TRACKER.md)의 자기 작업/입력 행에 **기존 Issue·PR와 확인한 입력**을 연결합니다. 필요한 입력이 없으면 해당 실행만 대기로 남기고 독립 준비를 계속합니다.
3. 자기 Issue/PR에 진행·차단·검사 결과를 기록하고 [인계 양식](HANDOFF_TEMPLATE.md)으로 결과 수신자에게 직접 넘깁니다. 수신자는 받은 개정과 수락/보완 범위를 기록합니다.
4. 실제 실행은 [Evidence 안내](../evidence/README.md)에 따라 새 Run으로 남기고 Index와 진행표에 링크를 연결합니다. 코드 Merge와 최종 시험 PASS를 구분합니다.

지금 할 첫 인계는 [진행표의 Next Handover](WORK_TRACKER.md#next-handover)입니다. 자기 현재 Source·완료 범위·없는 입력을 작업 Issue에 연결하면서 독립 준비를 진행합니다. 팀원의 개인 비밀번호는 이 인계에 필요하지 않습니다.

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
| 발표 후보 | [05 §0.7의 별도 발표 기준 참조](05_IMPLEMENTATION_AND_VALIDATION.md#07-발표와-보고에-사용할-측정과-증거)를 읽고 [Issue #6](https://github.com/seokpan/seokpan-hybrid-docs/issues/6)에 원본 Run 링크와 후보 판정만 연결 |

새 Issue 번호·수행자·실제 시각·성공값을 미리 만들어 채우지 않습니다. 기존 Issue가 범위를 담으면 이어 쓰고 별도 산출물/종료 조건이 필요할 때만 나눕니다. 같은05 편집은 최신 정본과 타 담당 기록을 대조하며, 독립 작업/직접 인계는 문서 Merge를 기다리지 않습니다.

## Approved References

설계 등록 [PR #3](https://github.com/seokpan/seokpan-hybrid-docs/pull/3)은 2026-10-02 03:40:08 KST, 발표 등록 [PR #7](https://github.com/seokpan/seokpan-hybrid-docs/pull/7)은 03:49:30 KST에 병합됐습니다. 승인 원문5개의 첨부 동일성은 공유 검토 이력으로 유지하며, 아래는 main의 기준 경로입니다.

- [00 출발점](../design/00_PROJECT_STARTING_POINT.md)
- [01 기획/성공 기준](../design/01_PROJECT_CHARTER.md)
- [02 목표 아키텍처](../design/02_TARGET_ARCHITECTURE.md)
- [03 상세설계·시험·WBS/비용](../design/03_DETAILED_DESIGN.md)
- [04 배정·I01~I07·인계/Run 양식](../design/04_IMPLEMENTATION_READINESS.md)

구조와 시험 목표는 승인03/04, 최신 사용자 결정과 등록 프로젝트 지침을 따릅니다. 팀원이 모든 원문을 처음부터 다시 읽어야 작업을 시작하는 조건은 아닙니다. 공통 안내·본인 작업·관련 근거/인계부터 확인합니다.

