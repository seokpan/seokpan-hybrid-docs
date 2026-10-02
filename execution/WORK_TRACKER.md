# Work and Input Tracker

이 표는 작업/입력/통합의 **링크와 마지막 확인 시각**을 연결합니다. 담당자 인계와 팀의 부분 보고를 연결하며 이 표의 빈칸을 작업 부재나 실패로 해석하지 않습니다. 기존05의 Source 관측과 부분 검사 이력은 그 시점/범위로 보존합니다.

## Current Observation

최신 조회 묶음은 `2026-10-02T04:21:55Z` / `2026-10-02T13:21:55+09:00` 기준입니다. 아래 main SHA와 현재 Issue/병합 상태를 읽기로 연결했습니다. 이전 03:52:45.552 KST의 Infra `c9a3e797a436bef32a5e7d14b9d8fce58e28a574` 및 App/GitOps 관측은 이력이며, 새 세션 수정·App Issue를 아래에 반영합니다. 개인 로컬 작업·미인계 실행의 부재를 뜻하지 않습니다. 팀의 Runtime 보고와 AI의 Source 읽기는 구분하고, AI는 해당 Runtime을 재실행하지 않았습니다. 배정 담당과 실제 작성·수행자는 구분합니다.

| 저장소 | 관측 main 전체 SHA | 연결 범위 |
| --- | --- | --- |
| Infra | `18c3a275a98b0f68226d5bcfba4aa7cf2984d1d2` | 기존 Bootstrap/State 보고 + PR #14/#15 병합. 실제 foundation/rosa 서비스 Root·전원 세션 검증은 별도 |
| App | `6902f3a184b4f1f07ade782536335a88d72612fc` | [#1 환경별 DB·Redis 대상/TLS/AUTH](https://github.com/seokpan/seokpan-hybrid-app/issues/1) 열림. 실제 App 이관/구현은 main에서 미확인 |
| GitOps | `523e9206dd6398adc6776855573890063b837a85` | #1·#5·#6 열림, #2~4 및 #7 해당 lab 종료. 실제 hybrid base/ROSA 판정과 구분 |
| Docs | `c1afca0b227fc66a551c7c1856f6b3b4fc2dfd1c` | PR #10 팀 안내/README 병합. #6 발표 후보와 #8 입력 인계는 별도 목적의 열린 추적 Issue |

추가 자료의 판정과 비민감 권한 계약은 [05 §8](05_IMPLEMENTATION_AND_VALIDATION.md#supplement-20261002)에만 기록합니다. 원문/민감정보를 중복 보관하지 않습니다. 1차 App main `a75867b7b579de08b14fe93f80b1a7b05cc85890`은 읽은 Source이며 검증 Seed로 자동 수락하지 않습니다.

## Team Access

Docs는 공개 저장소입니다. 공개 읽기 경로 제공과 개인이 실제 열람·기록에 성공한 확인은 구분합니다. 후속 인계는 [Issue #8](https://github.com/seokpan/seokpan-hybrid-docs/issues/8)에서 이어갑니다.

사용자가 첨부의 위→아래 순서를 최유준·이유빈·김상희로 명시해 계정을 연결했습니다. 네 계정에 대해 네 저장소 권한 API 조회 16건이 모두 성공했습니다.

| 배정 담당 | 명시 GitHub 계정 | Docs | Infra | App | GitOps |
| --- | --- | --- | --- | --- | --- |
| 이유빈 | `ggbun2` | admin | admin | admin | admin |
| 정태훈 | `tjung03` | admin | admin | admin | admin |
| 김상희 | `kshi1313-gif` | admin | admin | admin | admin |
| 최유준 | `cyj200115-prog` | admin | admin | admin | admin |

GitHub ID·권한은 명시 매핑과 API 결과로 연결하고 Commit/Caller만으로 실제 사람을 단정하지 않습니다. 권한을 변경하거나 팀원에게 자동 메시지·초대를 보내지 않았습니다. main 보호 상세 조회는 현재 연결의 권한 제한으로 확인하지 못했으며 보호가 없다고 판정하지 않습니다. 기존 규칙을 변경하지 않고 PR 병합 시 GitHub의 검사 결과를 확인합니다.

최신 권한 API 관측 시각은 `2026-10-01T18:52:11.308Z` / `2026-10-02T03:52:11.308+09:00`입니다. 이전 B 단독 조회는 03:12:47.529 KST 이력입니다. 개인 본인 환경의 실제 열람·Issue/PR 기록은 각자가 자기 작업 기록으로 확인합니다. Repo admin 등급은 Branch 보호·CI PAT/Job 정책·AWS/Cluster 인증·Runtime 판정을 대신하지 않습니다. 계정/권한 확인에 팀원의 개인 비밀번호나 PAT 공유는 필요하지 않습니다.

## Next Handover

계정 매핑/Repo 권한 확인은 완료됐습니다. 각자는 아래 입력 정리와 독립 코드·검사 준비를 병행합니다. 다른 사람의 사용 확인이나 I01~I07 전체 제출을 모든 작업의 시작 조건으로 삼지 않습니다.

| 담당 | 지금 연결할 첫 입력/Source | 직접 수신자 |
| --- | --- | --- |
| 이유빈 | 현재 foundation 작업 Issue/Branch/전체 SHA, 병합된 세션 수정의 실제 실패/Caller 검증과 기반 Output 계약. 미구현은 미구현으로 기록 | B ROSA, C Data, D Registry/비용 |
| 정태훈 | 실제 검증 Seed의 전체 SHA·검증 근거·미반영 변경, 현재 App/base/Overlay Source. 관측 main을 검증 Seed로 자동 채택하지 않음 | D Build/lab, C Data, A 기반 |
| 김상희 | Host 용량/복구 공간, 비민감 Schema/GRANT·CA 및 Backup/복호화 수단의 보호 논리 참조. 미확인 항목과 제공 시점 | A foundation/Host, B App/Recovery, D 증거 |
| 최유준 | 원 lab Overlay/Manifest Source, CI Job/Agent·Image/Digest 인계 상태, 실제 가용시간과 비용 입력의 확인 상태 | B base/Image, A Registry/CI, C Recovery |

1. 자기 기존 작업 Issue에 [인계 양식](HANDOFF_TEMPLATE.md)으로 현재 개정·완료 범위·없는 입력·직접 Blocker·다음 수신자를 기록하고 이 표에 링크합니다. 개인 본인환경의 기록 성공도 같은 작업에서 확인합니다.
2. 수신자는 받은 개정과 사용할 범위/보완을 확인합니다. 전체 팀의 결과를 한 사람이 받아 대필할 때까지 기다리지 않습니다.
3. 공유 Apply·배포·Restore·장애/부하는 해당 작업의 입력·리뷰·Caller/Context·Plan·비용/시간 조건을 확인한 뒤 조율합니다. 독립 준비는 병행합니다.

권한 API가 실패했다면 조회 미확인으로만 남기고 공개 Source 점검·로컬 후보/검사·인계 준비를 계속합니다. 실제 쓰기/접속이 막힌 작업은 허용된 기록 경로로 결과를 제공하고 해당 대상의 접근을 해결합니다. 기록 반영자와 실제 작성/수행자는 구분합니다.

## Work Links

자기 행을 먼저 갱신하고 상세 진행은 기존 작업 Issue에서 관리합니다.

| 담당 | 대표 Issue/관련 PR | 현재 Source·산출물 | 지금 준비할 일 | 직접 Blocker·해결 담당 | 다음 인계·수신자 | 마지막 확인 |
| --- | --- | --- | --- | --- | --- | --- |
| 이유빈 | [Infra #10](https://github.com/seokpan/seokpan-hybrid-infra/issues/10)·[PR #12](https://github.com/seokpan/seokpan-hybrid-infra/pull/12)·[PR #14](https://github.com/seokpan/seokpan-hybrid-infra/pull/14)·[PR #15](https://github.com/seokpan/seokpan-hybrid-infra/pull/15). foundation 작업은 담당자가 연결 | 세션 수정/안내 main 반영 확인. 실제 foundation 산출물 인계 필요 | foundation 통합·제한 Output·최종 VPN 경로 계약 | I02의 실제 Caller/실패 차단·도구/지원/Plan, C/D 선언 인계 | B/C/D 기반 인계 | Source 13:21:55 KST / 실제 Root 결과 인계 대기 |
| 정태훈 | [App #1](https://github.com/seokpan/seokpan-hybrid-app/issues/1), 관련 [GitOps #6](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6)·[#5](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5). base/rosa Source는 담당자가 연결 | App Issue 접수, 실제 이관/Build는 별도. 앞선 로컬 초안05 §7 보존 | 검증 Seed·이력 보존 이관·대상 검사/TLS/AUTH 구현·base/Overlay·ROSA 입력 계약 | I01 검증 Seed/미반영 변경, C Client/Secret 계약, I02/I06 | D 수정 Image·base lab, C Data, A 기반 | Source 13:21:55 KST / Seed 수락·구현 결과 대기 |
| 김상희 | [Infra #17](https://github.com/seokpan/seokpan-hybrid-infra/issues/17) 1차 DB 사전 점검·이관 범위 결정. [Infra #19](https://github.com/seokpan/seokpan-hybrid-infra/issues/19) foundation Data 코드. [DB lab #7 종료](https://github.com/seokpan/seokpan-hybrid-gitops/issues/7), [실행 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/7#issuecomment-5944080811), [05 §8 권한/TLS](05_IMPLEMENTATION_AND_VALIDATION.md#supplement-20261002) | #17 점검 결과·행 수 기준값·[인계 기록](https://github.com/seokpan/seokpan-hybrid-infra/issues/17#issuecomment-5945238648). #19 Data 모듈 초안(브랜치 `infra/19-foundation-data`, validate 통과, 서울 생성 가능 조합 조회)·[foundation Role Data 권한 요청](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-5947207348). C 권한 입력·D lab 수행 보고 부분 접수 | Network merge 후 첫 plan 전 foundation Root 직접 배치로 전환·PR, 목적 GRANT/CA·Dump 계정·위치·Backup/격리 Restore 준비 | Network 리소스 이름·bootstrap Data 권한 반영 / 이유빈. I03 실제 Host/용량·CA·Dump 계정·위치·Backup/Restore 목적 계정·I05 / 김상희. 실사용자 데이터는 그대로 이관 결정(10-02, #17) | A Data 선언·권한(#19), B App 시간대·Redis 7.1 Driver 호환·Migration/Recovery, D 증거·행 수 기준값 | 2026-10-02T07:50Z (16:50 KST) / Cloud 미생성·Restore 미검증 |
| 최유준 | [GitOps #5 base sync](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5)·[#6 대상 블로커](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6)·[#7 DB lab 종료](https://github.com/seokpan/seokpan-hybrid-gitops/issues/7); 기존 #1~4 참조 유지 | #6 실행 이미지 재현·#7 권한/업무 재검증 보고 접수. 실제 CI/base 조합은 대기 | CI/Harness·원 Manifest/전체 Digest 인계, 수정 Image #6·실제 base #5 검증 | B Seed/수정 Image/base PR, I04/I07. #7 권한 교체를 반복 요구하지 않음 | A/B/C, 전원 시험/비용 | Source/보고 13:21:55 KST / base·최종 시험 대기 |

## Input Handover

04 §10.1 배정을 유지합니다. 제공된 값·개정은 담당자가 확인해 적고 수신자가 사용 범위/대상/시점을 확인합니다. 비밀값·상세 접속정보는 보호 대장 논리 참조로 연결합니다.

| ID | 확인 담당 | 필요한 입력·확인 시점 | 제공된 개정/비민감 참조 | 수신 확인·범위 | 남은 제약·다음 행동 |
| --- | --- | --- | --- | --- | --- |
| I01 | 정태훈, 최유준 lab | 실제 Seed·미반영 변경·원 Overlay·전체 Commit/Digest·실습 조건. 이관/lab 전 | 기존 #1~4 + [#6 재현](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6#issuecomment-5944604370)·[App #1](https://github.com/seokpan/seokpan-hybrid-app/issues/1). 1차 main은 Current Observation에 연결 | 보고 부분 접수, 검증 Seed·실제 base 수신 수락 미확인 | 검증 Seed 전체 SHA/근거·미반영 변경·원 Manifest/전체 Digest 인계 → App 수정/Build → #6/#5의 해당 검증 |
| I02 | 이유빈, 정태훈 rosa | Controller·Tool/Lock·Caller/Role·정본 Backend·지원/Quota. 해당 Plan 전 | [State 정리](https://github.com/seokpan/seokpan-hybrid-infra/issues/10#issuecomment-5928992867)·[Bootstrap/임시 Probe](https://github.com/seokpan/seokpan-hybrid-infra/pull/12#issuecomment-5930110859)·병합 PR #14/#15·[네 사람 세션 확인](https://github.com/seokpan/seokpan-hybrid-infra/issues/13#issuecomment-5947593250) | 네 사람의 personal·bootstrap 세션 발급과 bootstrap plan No changes 확인(2026-10-02, Infra #13). 실제 foundation/rosa 서비스 Root 세션·Plan과는 다름 | 실제 Caller/만료·오류 시 Plan/Apply 차단·Backend/Provider Principal 일치·도구/지원·실제 Plan/제한 Output |
| I03 | 김상희, 이유빈 자산; 최유준 lab 수행 | Host CPU/RAM/공간·격리 Storage·DB/CA·Dump/GRANT. 배치/Import 전 | [05 §8.2~3의 비민감 GRANT](05_IMPLEMENTATION_AND_VALIDATION.md#supplement-20261002)·[DB lab #7](https://github.com/seokpan/seokpan-hybrid-gitops/issues/7#issuecomment-5944080811)·기존 대역 DB/TLS 보고·[Infra #17](https://github.com/seokpan/seokpan-hybrid-infra/issues/17) 1차 버전 11.8.9·Schema·크기·행 수 기준값 (2026-10-02T03:12Z) | GRANT 입력과 lab 권한/대표 업무 보고, #17 점검 결과 부분 접수. 실제 DDL·RDS·Recovery 자산 수신 수락은 별도 | Engine family·실제 Host/공간·CA·Dump 계정·위치·Migration DDL·Backup/Restore 목적 계정·독립 사본·격리 Restore. 완료된 #7 권한 교체를 재요구하지 않음 |
| I04 | 최유준, 정태훈 리뷰 | PAT 정책·Repo 보호·Job/Agent/Binding·Registry/Scan. 발급/CI 변경 전 | 네 사람 Repo 권한 조회는 Team Access, 실제 CI 입력 인계 미확인 | 정책/Job/Registry 수신 수락 미확인 | 실제 PAT 정책·Build/Test/Scan·Digest Mapping·Push/PR/Pull |
| I05 | 승인된 범위별 주/예비 보관자 | 보호 원본·독립 사본·오프라인 Key/해제·증거 접근/보존. 공급/Offline 전 | 이번 조회 범위에서 완료 근거 미확인 | 범위별 수신 수락 미확인 | 범위별 공급/접근·복호화/복원·보존 책임 확인 |
| I06 | 정태훈, 이유빈 리뷰, 최유준 lab | 개인 IDP/RBAC·Argo·비상 경로·초기 인증/세션 회수. 초기 관리자 종료 전 | [Argo 예제 동작/정리](https://github.com/seokpan/seokpan-hybrid-gitops/issues/3#issuecomment-5927423295)·[UWM 원복 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/4#issuecomment-5928589042) | 해당 lab 참고 접수, 실제 관리 인계 수락 미확인 | 개인 IDP/SSO/RBAC·유지 비상·초기 인증/기존 세션 회수·잔존 확인 |
| I07 | 최유준 집계, 네 담당자 | 실제 가용시간·가격/Credit·누적/잔존·Plan·Window/재시험/정리. Full Apply 전 | 이번 조회 범위에서 Gate 충족 근거 미확인 | 실제 실행 조건 수신 수락 미확인 | $450 계획선/$500 한도·현재 Plan/가격·가용시간·실행 창 연결 |

기존 I01 lab 인계 참조: [#1 대역 DB/TLS](https://github.com/seokpan/seokpan-hybrid-gitops/issues/1#issuecomment-5926003372)·[#2 Manifest 인계 계획](https://github.com/seokpan/seokpan-hybrid-gitops/issues/2#issuecomment-5927202120)·[#3 예제](https://github.com/seokpan/seokpan-hybrid-gitops/issues/3#issuecomment-5927423295)·[#4 관측](https://github.com/seokpan/seokpan-hybrid-gitops/issues/4#issuecomment-5928589042). 새 #5/#6/#7의 결과와 구분해 보존합니다.

I02의 PR #12 보고는 Bootstrap Apply 및 foundation/rosa 접두사의 **임시 Probe Root** 시험이다. 실제 foundation/rosa 서비스 구현·생성·최종 권한 판정으로 확대하지 않는다. 당시 남은 세션 처리의 후속 Source는 PR #14(2026-10-02 10:13:35 KST 병합), 안내는 PR #15(11:39:58 KST 병합)로 연결한다. 읽은 diff에서 유효 모드 발급 전 이전 세션을 해제하고 실패 시 Caller를 표시한다. 인자 오타는 기존 세션을 유지한다. 모든 실패·만료·Caller 불일치 때 Plan/Apply가 차단되는지와 실제 Principal 일치는 실행 담당자가 확인한다. 기본 자격증명으로 남는 것을 안전한 실행 허가로 해석하지 않는다. 이 기록은 Source 읽기이며 실제 세션/Root를 실행한 결과가 아니다. Bootstrap 재구축·State 이전 반복은 요구하지 않는다.

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

