# Data 영역 인수인계 (김상희 → 팀)

김상희가 2026-10-13에 프로젝트에서 하차하면서 남긴 Data · Storage · Recovery 영역 인수인계 자료입니다. 처음 보는 사람은 위에서부터 차례로 읽으면 됩니다.

| 문서 | 누가 읽나 | 내용 |
| --- | --- | --- |
| [DATA_HANDOFF_20261013.md](DATA_HANDOFF_20261013.md) | 사람 | 현재 상태 · 지금까지 한 일 · 무엇이 어디에 있나 · 남은 작업 · 하차 정리 · 규칙 |
| [DATA_CODE_WALKTHROUGH_20261014.md](DATA_CODE_WALKTHROUGH_20261014.md) | 사람 | [seokpan-hybrid-infra](https://github.com/seokpan/seokpan-hybrid-infra) main의 Terraform Data 코드와 `ansible/data` 파일 이름 · 역할 · 구조 (통화 설명용) |
| [seokpan-data-handoff-for-ai.md](seokpan-data-handoff-for-ai.md) | AI | 위 인수인계와 같은 내용을 AI가 읽기 쉬운 구조로 정리. AI 작업을 시작할 때 먼저 읽힘 |

- **기준 시각:** 인수인계 2026-10-13 22:00 KST, 코드 설명 2026-10-14(infra main `0b4497d`). 이후 바뀐 내용은 각 Issue 본문(Runbook 최신 기준본)과 infra 저장소 main이 우선입니다.
- **비밀값:** 세 문서 모두 비밀번호 · Token · 개인키 · AWS 계정 번호 · 공인 IP 값을 적지 않았습니다.
