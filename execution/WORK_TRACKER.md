# Work and Input Tracker

이 표는 작업/입력/통합의 **링크와 마지막 확인 시각**을 연결합니다. 현재 실적은 담당자 인계 전이며 이 표의 빈칸을 작업 부재나 실패로 해석하지 않습니다. 기존05의 Source 관측과 부분 검사 이력은 그 시점/범위로 보존합니다.

## Current Observation

Source 조회는 `2026-10-01T18:07:38Z` / `2026-10-02 03:07:38+09:00`입니다. 아래 세 main SHA는 이전 관측과 같고 조회 가능한 Branch는 main 하나씩, 열린 PR은 없었습니다. 개인 로컬 작업·미인계 실행의 부재를 뜻하지 않습니다. 연결한 결과는 팀의 보고이며 AI가 Runtime을 재실행한 결과가 아닙니다. 배정 담당과 원본 기록의 실제 작성·수행자는 구분합니다.

| 저장소 | 관측 main 전체 SHA | 연결 범위 |
| --- | --- | --- |
| Infra | `c9a3e797a436bef32a5e7d14b9d8fce58e28a574` | Bootstrap/State 정리와 실행 보고. 실제 foundation/rosa Root는 별도 |
| App | `6902f3a184b4f1f07ade782536335a88d72612fc` | 이번 목록에서 실제 이관 구현 Issue/PR 미확인 |
| GitOps | `523e9206dd6398adc6776855573890063b837a85` | #1 열림, #2~4 해당 lab 종료 보고. 실제 hybrid base/ROSA 판정과 구분 |

## Team Access

Docs는 공개 저장소입니다. 공개 읽기 경로 제공과 개인이 실제 열람·기록에 성공한 확인은 구분합니다. 후속 인계는 [Issue #8](https://github.com/seokpan/seokpan-hybrid-docs/issues/8)에서 이어갑니다.

| 배정 담당 | 명시 GitHub 계정 | Docs 권한 API 확인 | 실제 열람·기록 확인 / 다음 입력 |
| --- | --- | --- | --- |
| 이유빈 | 미확인 | 계정 매핑 전 미조회 | 본인 ID·현재 작업/입력 인계 |
| 정태훈 | `tjung03` | admin — Repo 권한 등급 | AI 연결로 Docs 쓰기 확인. 본인 환경의 열람·기록 경로는 확인 필요 |
| 김상희 | 미확인 | 계정 매핑 전 미조회 | 본인 ID·현재 Data/Recovery 입력 인계 |
| 최유준 | 미확인 | 계정 매핑 전 미조회 | 본인 ID·현재 lab/CI/시간·비용 입력 인계 |

GitHub ID·권한은 명시 매핑과 API 결과로 연결하고 Commit/Caller만으로 실제 사람을 단정하지 않습니다. 권한을 변경하거나 팀원에게 자동 메시지·초대를 보내지 않았습니다. main 보호 상세 조회는 현재 연결의 권한 제한으로 확인하지 못했으며 보호가 없다고 판정하지 않습니다. 기존 규칙을 변경하지 않고 PR 병합 시 GitHub의 검사 결과를 확인합니다.

위 B 권한 API 관측 시각은 `2026-10-01T18:12:47.529Z` / `2026-10-02T03:12:47.529+09:00`입니다. 공개 읽기·Repo 권한 등급·본인 환경의 실제 사용 확인은 서로 다른 상태입니다.

## Work Links

자기 행을 먼저 갱신하고 상세 진행은 기존 작업 Issue에서 관리합니다.

| 담당 | 대표 Issue/관련 PR | 현재 Source·산출물 | 지금 준비할 일 | 직접 Blocker·해결 담당 | 다음 인계·수신자 | 마지막 확인 |
| --- | --- | --- | --- | --- | --- | --- |
| 이유빈 | 기존 Bootstrap [Infra #10](https://github.com/seokpan/seokpan-hybrid-infra/issues/10)·[PR #11](https://github.com/seokpan/seokpan-hybrid-infra/pull/11)·[PR #12](https://github.com/seokpan/seokpan-hybrid-infra/pull/12). foundation 작업은 담당자가 연결 | 기존 Bootstrap main/팀 보고 연결, foundation 실제 산출물 인계 필요 | foundation 통합·제한 Output | I02와 세션 실패 후속 확인 | B/C/D 기반 인계 | Source 03:07:38 KST / 담당자 인계 미확인 |
| 정태훈 | 실제 App/base/rosa 대표 작업은 이번 목록에서 미확인. [GitOps #1](https://github.com/seokpan/seokpan-hybrid-gitops/issues/1)은 lab 참고 | 앞선 B 로컬 초안은05 §7, 실제 이관/Build는 별도 | App/base·ROSA 입력 계약 | I01/I02/I06 등 확인 | D Build/lab, C Data, A 기반 | Source 03:07:38 KST / 실제 Seed 인계 미확인 |
| 김상희 | 실제 Data/Backup/Recovery 대표 작업은 이번 목록에서 미확인. [대역 DB lab 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/1#issuecomment-5926003372)는 참고 | 현재 Data/복구 입력 인계 필요 | Data/TLS·Backup·격리 Restore 준비 | I03/범위별 I05 확인 | A/B/D Data 인계 | Source 03:07:38 KST / 담당자 인계 미확인 |
| 최유준 | 기존 [GitOps #1](https://github.com/seokpan/seokpan-hybrid-gitops/issues/1)·[#2](https://github.com/seokpan/seokpan-hybrid-gitops/issues/2)·[#3](https://github.com/seokpan/seokpan-hybrid-gitops/issues/3)·[#4](https://github.com/seokpan/seokpan-hybrid-gitops/issues/4). 실제 CI/시험 작업은 담당자가 연결 | 기존 lab 보고는 그 범위, 현재 조합 인계 필요 | CI·실제 base lab·Harness·Index | I04/I07 등 확인 | A/B/C, 전원 시험/비용 | Source 03:07:38 KST / 실제 조합 인계 미확인 |

## Input Handover

04 §10.1 배정을 유지합니다. 제공된 값·개정은 담당자가 확인해 적고 수신자가 사용 범위/대상/시점을 확인합니다. 비밀값·상세 접속정보는 보호 대장 논리 참조로 연결합니다.

| ID | 확인 담당 | 필요한 입력·확인 시점 | 제공된 개정/비민감 참조 | 수신 확인·범위 | 남은 제약·다음 행동 |
| --- | --- | --- | --- | --- | --- |
| I01 | 정태훈, 최유준 lab | 실제 Seed·미반영 변경·원 Overlay·전체 Commit/Digest·실습 조건. 이관/lab 전 | [lab #1](https://github.com/seokpan/seokpan-hybrid-gitops/issues/1#issuecomment-5926003372)·[#2 Manifest 인계 계획](https://github.com/seokpan/seokpan-hybrid-gitops/issues/2#issuecomment-5927202120)·[#3 예제](https://github.com/seokpan/seokpan-hybrid-gitops/issues/3#issuecomment-5927423295)·[#4 관측](https://github.com/seokpan/seokpan-hybrid-gitops/issues/4#issuecomment-5928589042) | 과거 lab 참고 접수, 실제 base 수신 수락 미확인 | 검증 Seed 전체 SHA·미반영 변경·원 Overlay/Manifest/Raw 인계 |
| I02 | 이유빈, 정태훈 rosa | Controller·Tool/Lock·Caller/Role·정본 Backend·지원/Quota. 해당 Plan 전 | [State 정리 보고](https://github.com/seokpan/seokpan-hybrid-infra/issues/10#issuecomment-5928992867)·[Bootstrap Apply/임시 Probe 결과](https://github.com/seokpan/seokpan-hybrid-infra/pull/12#issuecomment-5930110859) | 팀 보고 부분 접수. 실제 foundation/rosa 서비스 Root 완료와 다름 | 개인 MFA/Caller·세션 실패 차단·Root 도구/지원·실제 Plan/제한 Output |
| I03 | 김상희, 이유빈 자산 | Host CPU/RAM/공간·격리 Storage·DB/CA·Dump/GRANT. 배치/Import 전 | [대역 DB/TLS lab](https://github.com/seokpan/seokpan-hybrid-gitops/issues/1#issuecomment-5926003372) 참고 | 실제 Recovery 자산/입력 수신 수락 미확인 | Host/공간·목적 GRANT/CA/Schema·Dump·독립 사본·격리 Restore |
| I04 | 최유준, 정태훈 리뷰 | PAT 정책·Repo 보호·Job/Agent/Binding·Registry/Scan. 발급/CI 변경 전 | Docs B 권한 조회는 Team Access, 실제 CI 입력 인계 미확인 | 정책/Job/Registry 수신 수락 미확인 | 실제 PAT 정책·Build/Test/Scan·Digest Mapping·Push/PR/Pull |
| I05 | 승인된 범위별 주/예비 보관자 | 보호 원본·독립 사본·오프라인 Key/해제·증거 접근/보존. 공급/Offline 전 | 이번 조회 범위에서 완료 근거 미확인 | 범위별 수신 수락 미확인 | 범위별 공급/접근·복호화/복원·보존 책임 확인 |
| I06 | 정태훈, 이유빈 리뷰, 최유준 lab | 개인 IDP/RBAC·Argo·비상 경로·초기 인증/세션 회수. 초기 관리자 종료 전 | [Argo 예제 동작/정리](https://github.com/seokpan/seokpan-hybrid-gitops/issues/3#issuecomment-5927423295)·[UWM 원복 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/4#issuecomment-5928589042) | 해당 lab 참고 접수, 실제 관리 인계 수락 미확인 | 개인 IDP/SSO/RBAC·유지 비상·초기 인증/기존 세션 회수·잔존 확인 |
| I07 | 최유준 집계, 네 담당자 | 실제 가용시간·가격/Credit·누적/잔존·Plan·Window/재시험/정리. Full Apply 전 | 이번 조회 범위에서 Gate 충족 근거 미확인 | 실제 실행 조건 수신 수락 미확인 | $450 계획선/$500 한도·현재 Plan/가격·가용시간·실행 창 연결 |

I02의 PR #12 보고는 Bootstrap Apply 및 foundation/rosa 접두사의 **임시 Probe Root** 시험이다. 실제 foundation/rosa 서비스 구현·생성·최종 권한 판정으로 확대하지 않는다. 같은 보고의 세션 발급 실패 때 이전 Role 환경변수 유지 문제는 후속 수정과 실패 차단 결과 인계가 필요하다. 새 인증 실패 뒤의 공유 실행 전에 현재 Caller/세션을 확인한다. 이 기록은 보고의 남은 확인을 연결한 것이며 PR diff 재심사·세션 수정·실제 Root 실행이 아니다.

인계가 일부 수락이면 사용 가능한 범위와 막히는 후속 실행을 적습니다. 값이 없으면 해당 작업만 대기하고 독립 준비는 계속합니다.

## Shared Execution

같은 State/공유 Context/Restore/장애·부하의 충돌 실행을 조율할 때 새 행을 추가합니다. 이 표에 연결·확인된 실제 실행은 아직 없습니다. 팀의 별도 일정이나 미인계 실행이 없다는 뜻은 아닙니다.

| 작업 링크·대상 | 실행 책임/실제 수행자 | Source·입력 개정 | 실제 예정/시작·종료 | 리뷰·Cost·중단 조건 | 현재/실패·잔존 상태 | 정리·다음 인계 |
| --- | --- | --- | --- | --- | --- | --- |

## Update Rules

- 시작/차단/검토/인계/실행 종료와 입력 변경 때 담당자가 갱신하고 UTC ISO와 필요 시 같은 시각의 KST를 연결합니다.
- 코드 반영·인계 수락·실행 종료·시험 판정을 구분합니다. 시험 판정은 NOT RUN/PASS/PARTIAL/FAIL/N/A이고 차단 사유는 별도입니다.
- Source/입력/환경이 바뀌면 과거 Run을 보존하고 영향 시험을 다시 확인합니다.
- 최신 정본과 다른 담당 기록을 보존합니다. Issue·Run 원문을 이 표에 다시 복사하지 않습니다.
- [인계 양식](HANDOFF_TEMPLATE.md)과 [Evidence 안내](../evidence/README.md)를 사용합니다.
