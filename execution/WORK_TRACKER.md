# Work and Input Tracker

이 표는 작업/입력/통합의 **링크와 마지막 확인 시각**을 연결합니다. 담당자 인계와 팀의 부분 보고를 연결하며 이 표의 빈칸을 작업 부재나 실패로 해석하지 않습니다. 기존05의 Source 관측과 부분 검사 이력은 그 시점/범위로 보존합니다.

**2026-10-03 이번 DR 피드백의 우선순위:** [03 §3-I.14 설계 재검토](../design/03_DETAILED_DESIGN.md#recovery-design-review-20261003) → 필요한 02/04 정합 보완 → 기존 최소 예행에서 부족한 시간·최신성/손실·접속·팀 부담/비용 확보 → 목표/변경 범위 선택 → 채택 내용의 설계·코드·SVG/PNG 반영입니다. [05 §9](05_IMPLEMENTATION_AND_VALIDATION.md#recovery-objective-review-20261002)는 실행 근거를 지원합니다. [Cloud·ROSA·App 후속](#cloud-rosa-app-progress-20261002)과 [05 §9.13](05_IMPLEMENTATION_AND_VALIDATION.md#cloud-rosa-app-followup-20261002)은 별도 프로젝트 구현 이력이며 전체 완료를 이번 판단의 선행조건으로 묶지 않습니다. 과거 관측과 다른 담당자의 기록은 보존합니다.

## Current Observation

최신 조회 묶음은 `2026-10-02T04:21:55Z` / `2026-10-02T13:21:55+09:00` 기준입니다. 아래 main SHA와 현재 Issue/병합 상태를 읽기로 연결했습니다. 이전 03:52:45.552 KST의 Infra `c9a3e797a436bef32a5e7d14b9d8fce58e28a574` 및 App/GitOps 관측은 이력이며, 새 세션 수정·App Issue를 아래에 반영합니다. 개인 로컬 작업·미인계 실행의 부재를 뜻하지 않습니다. 팀의 Runtime 보고와 AI의 Source 읽기는 구분하고, AI는 해당 Runtime을 재실행하지 않았습니다. 배정 담당과 실제 작성·수행자는 구분합니다.

| 저장소 | 관측 main 전체 SHA | 연결 범위 |
| --- | --- | --- |
| Infra | `18c3a275a98b0f68226d5bcfba4aa7cf2984d1d2` | 기존 Bootstrap/State 보고 + PR #14/#15 병합. 실제 foundation/rosa 서비스 Root·전원 세션 검증은 별도 |
| App | `6902f3a184b4f1f07ade782536335a88d72612fc` | [#1 환경별 DB·Redis 대상/TLS/AUTH](https://github.com/seokpan/seokpan-hybrid-app/issues/1) 열림. 실제 App 이관/구현은 main에서 미확인 |
| GitOps | `523e9206dd6398adc6776855573890063b837a85` | #1·#5·#6 열림, #2~4 및 #7 해당 lab 종료. 실제 hybrid base/ROSA 판정과 구분 |
| Docs | `c1afca0b227fc66a551c7c1856f6b3b4fc2dfd1c` | PR #10 팀 안내/README 병합. #6 발표 후보와 #8 입력 인계는 별도 목적의 열린 추적 Issue |

추가 자료의 판정과 비민감 권한 계약은 [05 §8](05_IMPLEMENTATION_AND_VALIDATION.md#supplement-20261002)에만 기록합니다. 원문/민감정보를 중복 보관하지 않습니다. 1차 App main `a75867b7b579de08b14fe93f80b1a7b05cc85890`은 읽은 Source이며 검증 Seed로 자동 수락하지 않습니다.

복구 목표 피드백의 후속 준비는 [05 §9](05_IMPLEMENTATION_AND_VALIDATION.md#recovery-objective-review-20261002)와 아래 [Recovery Review Preparation](#recovery-review-preparation)에 연결합니다. 후속 읽기 기준은 `2026-10-02T09:29:49Z` / `2026-10-02T18:29:49+09:00`이며 Docs main `a2bfa4e299602ba00e481830b7109acb1f1ee930`의 05/Tracker·Evidence 양식과 관련 Infra Issue 목록·#19 댓글·#23을 대조했습니다. 이전 표의 관측 시각과 별개이며 네 저장소 전체 Runtime을 새로 확인했다는 의미가 아닙니다. 공식 수치는 아직 RTO 30분·영속 DB RPO 90분·운영 중 1시간 백업입니다.


<a id="follow-up-observation-20261002"></a>
### Follow-up Observation — PR #18 병합 후

읽기 조회 묶음의 기록 시각은 `2026-10-02T10:30:39.878Z` / `2026-10-02T19:30:39.878+09:00`이다. 아래는 최신 main·Branch/Tree·PR/Issue의 변경 관측이며 위의 13:21:55 KST 표는 과거 관측으로 보존한다. 실제 개인 작업·Runtime·수신 수락은 새로 확인한 것으로 표시하지 않는다.

| 저장소 | 관측 main 전체 SHA | 변경 원문 / 현재 경계 |
| --- | --- | --- |
| Docs | `516ccf5d6eed465f3cbf552d7389a88ec410af1b` | [PR #18](https://github.com/seokpan/seokpan-hybrid-docs/pull/18) 병합·해당 Branch 삭제 확인. 공식 목표 유지, 실제 Run 디렉터리/Index 연결 없음 |
| Infra | `44470359c4e6de366db428adcb7831bac38a690e` | [PR #21](https://github.com/seokpan/seokpan-hybrid-infra/pull/21) ECR/CI 권한·[#22](https://github.com/seokpan/seokpan-hybrid-infra/pull/22) 안내 병합. [#20 보고](https://github.com/seokpan/seokpan-hybrid-infra/issues/20#issuecomment-5949198590)는 Apply 완료, 실제 foundation Plan 권한 확인은 대기. [#23 Data 통합 질문](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-5949221314)·[#19](https://github.com/seokpan/seokpan-hybrid-infra/issues/19) 기존 Branch 작업을 유지 |
| App | `cef46c4e7b0cbd0cf6ebab487ee92c32d800ccdc` | [PR #3](https://github.com/seokpan/seokpan-hybrid-app/pull/3) README 병합. main의 실제 App 이관 코드는 미확인; [#1](https://github.com/seokpan/seokpan-hybrid-app/issues/1)·[#2](https://github.com/seokpan/seokpan-hybrid-app/issues/2) 계속 |
| GitOps | `888833312384496eac1c04876ce0183496e15053` | [PR #8](https://github.com/seokpan/seokpan-hybrid-gitops/pull/8) README 병합. [원 lab 인계](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5#issuecomment-5950121508)의 참고 Branch `reference/ocp-lab-original`, SHA `259e73b0fac1af40f7bb7b43bd1982410d1df150` Tree 확인. main 병합·ROSA base 수락/검증과 구분 |

I01 원 Manifest 제공은 위 [#5 인계 원문](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5#issuecomment-5950121508)에 부분 연결한다. 최유준의 제공 기록과 정태훈의 수신/사용 확인은 다르며, 기존 Next Handover·Work Links·I01의 원 Manifest 대기는 이 제공 범위만 갱신된다. lab CA/Route/hostAliases·Redis StatefulSet·NetworkPolicy를 Cloud 설정으로 자동 채택하지 않는다. 검증 Seed/Image·base 작성/수신·Recovery Manifest는 계속 확인해야 한다.

I07에는 [#16 Network/Hybrid 비용 입력](https://github.com/seokpan/seokpan-hybrid-infra/issues/16#issuecomment-5947011620)과 [추가 계약/기간 대기](https://github.com/seokpan/seokpan-hybrid-infra/issues/16#issuecomment-5947189192)가 부분 제공됐다. 이전 표의 미확인은 이 범위에서 갱신되며 실제 시간·전체 가격/Plan/Credit·Cost Gate는 대기한다. 입력 원문을 복사하거나 후보를 확정값으로 승격하지 않는다.

[05 §9.8](05_IMPLEMENTATION_AND_VALIDATION.md#recovery-time-helper-20261002)의 계산 도구·[사용 안내](../evidence/README.md#recovery-time-calculation)는 로컬 합성 입력 검사 완료·PR 리뷰 대상이다. 담당자의 실제 사용/수신·Run·목표 결정은 별도다.


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
| 정태훈 | 이번 요청은 [03 §3-I.14](../design/03_DETAILED_DESIGN.md#recovery-design-review-20261003)의 설계 대조와 Recovery App/새 Redis·클라이언트 범위부터 확인. 기존 App `c837120`·78개 이력 묶음과 GitOps #9의 Source/Image·C/D 입력을 최소 예행에 연결. App 게임 시각의 UTC Source 계약은 [05 §9.14](05_IMPLEMENTATION_AND_VALIDATION.md#recovery-timezone-handoff-20261003)에서 확인; 실제 과거 행·Backup Data 근거는 C/D 수신 대기. [Docs #21 전체 실행](https://github.com/seokpan/seokpan-hybrid-docs/issues/21)·Cloud #11/ROSA #28의 전달·Controller/Plan 준비는 별도 프로젝트 후속으로 보존. 개인 미반영 변경·인증 Push·새 Image/Runtime 입력은 대기 | C Data, D Build/계측, A 로컬 자산 |
| 김상희 | Host 용량/복구 공간, 비민감 Schema/GRANT·CA 및 Backup/복호화 수단의 보호 논리 참조. 미확인 항목과 제공 시점 | A foundation/Host, B App/Recovery, D 증거 |
| 최유준 | 원 lab Overlay/Manifest Source, CI Job/Agent·Image/Digest 인계 상태, 실제 가용시간과 비용 입력의 확인 상태 | B base/Image, A Registry/CI, C Recovery |

1. 자기 기존 작업 Issue에 [인계 양식](HANDOFF_TEMPLATE.md)으로 현재 개정·완료 범위·없는 입력·직접 Blocker·다음 수신자를 기록하고 이 표에 링크합니다. 개인 본인환경의 기록 성공도 같은 작업에서 확인합니다.
2. 수신자는 받은 개정과 사용할 범위/보완을 확인합니다. 전체 팀의 결과를 한 사람이 받아 대필할 때까지 기다리지 않습니다.
3. 공유 Apply·배포·Restore·장애/부하는 해당 작업의 입력·리뷰·Caller/Context·Plan·비용/시간 조건을 확인한 뒤 조율합니다. 독립 준비는 병행합니다.

권한 API가 실패했다면 조회 미확인으로만 남기고 공개 Source 점검·로컬 후보/검사·인계 준비를 계속합니다. 실제 쓰기/접속이 막힌 작업은 허용된 기록 경로로 결과를 제공하고 해당 대상의 접근을 해결합니다. 기록 반영자와 실제 작성/수행자는 구분합니다.

## Work Links

자기 행을 먼저 갱신하고 상세 진행은 기존 작업 Issue에서 관리합니다.

정태훈의 이번 DR 판단은 [03 §3-I.14](../design/03_DETAILED_DESIGN.md#recovery-design-review-20261003)와 아래 [Recovery Review Preparation](#recovery-review-preparation)을 먼저 확인한다. [Cloud·ROSA·App 후속](#cloud-rosa-app-progress-20261002)·[05 §9.13](05_IMPLEMENTATION_AND_VALIDATION.md#cloud-rosa-app-followup-20261002)의 최신 Source·검사·직접 입력은 별도 구현 상태이며, [§9.12](#tjung03-latest-source-20261002)·[등록 후속](#tjung03-registered-work-20261002)의 기록과 함께 보존한다.

| 담당 | 대표 Issue/관련 PR | 현재 Source·산출물 | 지금 준비할 일 | 직접 Blocker·해결 담당 | 다음 인계·수신자 | 마지막 확인 |
| --- | --- | --- | --- | --- | --- | --- |
| 이유빈 | [Infra #10](https://github.com/seokpan/seokpan-hybrid-infra/issues/10)·[PR #12](https://github.com/seokpan/seokpan-hybrid-infra/pull/12)·[PR #14](https://github.com/seokpan/seokpan-hybrid-infra/pull/14)·[PR #15](https://github.com/seokpan/seokpan-hybrid-infra/pull/15)·[Infra #13 bootstrap 인계](https://github.com/seokpan/seokpan-hybrid-infra/issues/13#issuecomment-5947624416)(작성 김상희, 이유빈 확인 대기). foundation 작업은 담당자가 연결 | 세션 수정/안내 main 반영 확인. 실제 foundation 산출물 인계 필요 | foundation 통합·제한 Output·최종 VPN 경로 계약 | I02의 실제 Caller/실패 차단·도구/지원/Plan, C/D 선언 인계 | B/C/D 기반 인계 | Source 13:21:55 KST / 실제 Root 결과 인계 대기 |
| 정태훈 | [Docs #21 상위](https://github.com/seokpan/seokpan-hybrid-docs/issues/21) → [App #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4)·[GitOps #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10)·[Infra #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25). 기존 [App #1](https://github.com/seokpan/seokpan-hybrid-app/issues/1)·[#2 CI](https://github.com/seokpan/seokpan-hybrid-app/issues/2)·[GitOps #5](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5)·[#6](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6)·[Draft PR #9](https://github.com/seokpan/seokpan-hybrid-gitops/pull/9) 유지 | App `c837120c25c34b88bf6c6ee8e122ff50cbff062d`·78개 이력/39 수정·390 이관파일 새 묶음. Turn/퇴장 경쟁 보완·기본 전체 1,752 PASS/JUnit·strict report PASS, 독립 193/실제 Lua 3 PASS. [GitOps PR #11](https://github.com/seokpan/seokpan-hybrid-gitops/pull/11) `ce0ce5af9866428d7734db0bb8cce1d425ec20a2` 기본 각 0/별도 각 3 Preview·19 Source 검사. [Infra Draft #28](https://github.com/seokpan/seokpan-hybrid-infra/pull/28) `9a8410ab92e8a3283a41b90f913773d85ef30963`·14파일/PR #27 최신 계약 이력 소비 | 이번 DR 우선은 [03 §3-I.14](../design/03_DETAILED_DESIGN.md#recovery-design-review-20261003)의 설계 판단과 최소 Recovery 입력/근거 확인. 개인 미반영 변경·인증된 App 전체 이력 Push/PR·D 새 Build/Scan/Digest. #9/#11·#27/#28 리뷰·수신/retarget, Controller 동일 Source/Lock 검증 및 반복 종료 판별·A 실제 제한 출력/Role·Plan 준비. Source 경쟁 보완은 완료, 실제 다중 Pod/DB 시험은 다음 환경 입력 후 이 중 Cloud/ROSA 리뷰·Controller/Plan 준비는 별도 프로젝트 후속으로 보존. | I01 실제 Image/TLS DB·Redis/CA/Secret·D/C 수신/lab. I02 validate/schema socket BLOCKED·제한 Output/지원/권한/Plan 준비. I04 [PR #24](https://github.com/seokpan/seokpan-hybrid-infra/pull/24) A 승인·병합 완료, 실제 Boundary/통합 Plan/Cost·Preview/E2E·Worker Pull 미완료. I05/I06/I07 실제 공급/관리/Cost | D App/Image·base/lab, C Client/Recovery, A 실제 제한 출력·Worker Role/SG Binding 리뷰 | Source/검사 최신 [05 §9.13](05_IMPLEMENTATION_AND_VALIDATION.md#cloud-rosa-app-followup-20261002). PR/리뷰 관측 `2026-10-02T12:24:34.213Z`; PR #24 승인/병합·Infra main `b3e6572ff3ddf7e068258102c2a7fa079acb4a7e`. 각 과거 관측/검사는 이력이며 Cloud/Runtime 재실행 없음 |
| 김상희 | [Infra #17](https://github.com/seokpan/seokpan-hybrid-infra/issues/17) 1차 DB 사전 점검·이관 범위 결정. [Infra #19](https://github.com/seokpan/seokpan-hybrid-infra/issues/19) foundation Data 코드. [DB lab #7 종료](https://github.com/seokpan/seokpan-hybrid-gitops/issues/7), [실행 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/7#issuecomment-5944080811), [05 §8 권한/TLS](05_IMPLEMENTATION_AND_VALIDATION.md#supplement-20261002) | #17 점검 결과·행 수 기준값·[인계 기록](https://github.com/seokpan/seokpan-hybrid-infra/issues/17#issuecomment-5945238648). #19 Data 모듈 초안(브랜치 `infra/19-foundation-data`, validate 통과, 서울 생성 가능 조합 조회)·[foundation Role Data 권한 요청](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-5947207348). C 권한 입력·D lab 수행 보고 부분 접수 | Network merge 후 첫 plan 전 foundation Root 직접 배치로 전환·PR, 목적 GRANT/CA·Dump 계정·위치·Backup/격리 Restore 준비 | Network 리소스 이름·bootstrap Data 권한 반영 / 이유빈. I03 실제 Host/용량·CA·Dump 계정·위치·Backup/Restore 목적 계정·I05 / 김상희. 실사용자 데이터는 그대로 이관 결정(10-02, #17) | A Data 선언·권한(#19), B App 시간대·Redis 7.1 Driver 호환·Migration/Recovery, D 증거·행 수 기준값 | 2026-10-02T07:50Z (16:50 KST) / Cloud 미생성·Restore 미검증 |
| 최유준 | [GitOps #5 base sync](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5)·[#6 대상 블로커](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6)·[#7 DB lab 종료](https://github.com/seokpan/seokpan-hybrid-gitops/issues/7); 기존 #1~4 참조 유지 | #6 실행 이미지 재현·#7 권한/업무 재검증 보고 접수. 실제 CI/base 조합은 대기 | CI/Harness·원 Manifest/전체 Digest 인계, 수정 Image #6·실제 base #5 검증 | B Seed/수정 Image/base PR, I04/I07. #7 권한 교체를 반복 요구하지 않음 | A/B/C, 전원 시험/비용 | Source/보고 13:21:55 KST / base·최종 시험 대기 |

## Input Handover

04 §10.1 배정을 유지합니다. 제공된 값·개정은 담당자가 확인해 적고 수신자가 사용 범위/대상/시점을 확인합니다. 비밀값·상세 접속정보는 보호 대장 논리 참조로 연결합니다.

| ID | 확인 담당 | 필요한 입력·확인 시점 | 제공된 개정/비민감 참조 | 수신 확인·범위 | 남은 제약·다음 행동 |
| --- | --- | --- | --- | --- | --- |
| I01 | 정태훈, 최유준 lab | 실제 Seed·미반영 변경·원 Overlay·전체 Commit/Digest·실습 조건. 이관/lab 전 | 기존 #1~4·[#6 재현](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6#issuecomment-5944604370)·[App #1 인계](https://github.com/seokpan/seokpan-hybrid-app/issues/1#issuecomment-5950971722)·[B 원 lab 수신/인계](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5#issuecomment-5950971514)·[05 §9.10](05_IMPLEMENTATION_AND_VALIDATION.md#recursive-source-review-20261002), 실행 [App #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4)·[GitOps #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10)·[Cloud Source PR #11](https://github.com/seokpan/seokpan-hybrid-gitops/pull/11) | 고정 Seed/이력 보존 묶음·원 lab SHA 범위와 PR #9 선언 준비는 유지. #11 HEAD `ce0ce5af9866428d7734db0bb8cce1d425ec20a2` 기본0/각3·PDB2/soft AZ Preview·19 Source 검사 작성자/독립 보고 접수. D/C 새 개정 수신·실제 Image/base/lab·완성 Bundle/Cloud Sync·1/3 Pod 검증은 미완료 | 개인 미반영 변경·인증된 App Push/PR, D Build/Scan/Digest, 실제 대상·TLS Redis/DB/CA/Secret·자원/UID, lab #6/#5·Recovery 수신/시험. #9 직접 Draft 조건과 #11 Source Review를 구분하며 Cloud 전체/최종 Offline 완료를 #9의 추가 조건으로 묶지 않음 |
| I02 | 이유빈, 정태훈 rosa | Controller·Tool/Lock·Caller/Role·정본 Backend·지원/Quota. 해당 Plan 전 | [State 정리](https://github.com/seokpan/seokpan-hybrid-infra/issues/10#issuecomment-5928992867)·[Bootstrap/임시 Probe](https://github.com/seokpan/seokpan-hybrid-infra/pull/12#issuecomment-5930110859)·병합 PR #14/#15·[네 사람 세션 확인](https://github.com/seokpan/seokpan-hybrid-infra/issues/13#issuecomment-5947593250)·[A #23 최신 인계](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-5951505800)·[Infra #25 후속](https://github.com/seokpan/seokpan-hybrid-infra/issues/25#issuecomment-5952123857)·[계약 PR #27](https://github.com/seokpan/seokpan-hybrid-infra/pull/27)·[Draft HCL PR #28](https://github.com/seokpan/seokpan-hybrid-infra/pull/28) | personal·bootstrap 세션/No changes 보고와 A foundation 공통/통합 Owner 유지. #28 HEAD `9a8410ab92e8a3283a41b90f913773d85ef30963`의 14파일·Core1.16.4/AWS6.67.0/RHCS1.7.7 정확 제약/설치 Lock·fmt/정적 공식 Source Schema 보고 접수. validate/providers schema는 RPC socket 생성 operation not permitted로 BLOCKED. #27 최신 `5eaef969723e29becbb1e0611d04660ddcbdb28d` 이력 소비; 과거 AWS6.66.0 표기는 이력. 실제 제한 Output/Role·지원·Plan 수신 합의는 미확인 | Controller 동일 Source/Lock fmt/validate/Provider Schema 재검증, A/C/D 실제 제한 출력·Account/Region·Role/지원 조합·Caller/정본 Backend·첫 Plan 준비 리뷰가 #28 Source Review 진입의 직접 조건. 실제 전체 Plan/Cost·Worker Role/Pull·SG/ENI·전파/T19는 별도. 전체 업무/Offline 완료를 Draft 조건으로 붙이지 않음. Bootstrap/State 이전 반복 없음 |
| I03 | 김상희, 이유빈 자산; 최유준 lab 수행 | Host CPU/RAM/공간·격리 Storage·DB/CA·Dump/GRANT. 배치/Import 전 | [05 §8.2~3의 비민감 GRANT](05_IMPLEMENTATION_AND_VALIDATION.md#supplement-20261002)·[DB lab #7](https://github.com/seokpan/seokpan-hybrid-gitops/issues/7#issuecomment-5944080811)·기존 대역 DB/TLS 보고·[Infra #17](https://github.com/seokpan/seokpan-hybrid-infra/issues/17) 1차 버전 11.8.9·Schema·크기·행 수 기준값 (2026-10-02T03:12Z) | GRANT 입력과 lab 권한/대표 업무 보고, #17 점검 결과 부분 접수. B의 [App 시각 Source 확인](05_IMPLEMENTATION_AND_VALIDATION.md#recovery-timezone-handoff-20261003)은 완료; 기존 행 전부 KST/UTC 판정·실제 DDL·RDS·Recovery 자산 수신 수락은 별도 | Engine family·실제 Host/공간·CA·Dump 계정·위치·Migration DDL·Backup/Restore 목적 계정·독립 사본·격리 Restore. 완료된 #7 권한 교체를 재요구하지 않음 |
| I04 | 최유준, 정태훈 리뷰 | PAT 정책·Repo 보호·Job/Agent/Binding·Registry/Scan. 발급/CI 변경 전 | [App #2 B 리뷰](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-5950294428)·[D 방향 수신](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-5950470901)·[B 후속 정합](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-5951015819). 옛 PR #24 HEAD `33432eecc6cae81f7725c9d39f8a7730ca9ce815` 지적은 당시 이력. [PR #24](https://github.com/seokpan/seokpan-hybrid-infra/pull/24) 최신 `4fcbab4acc3e851f9a20a9affc4e4f4c29526add`·[D 갱신](https://github.com/seokpan/seokpan-hybrid-infra/pull/24#issuecomment-5951983854)·[A APPROVED](https://github.com/seokpan/seokpan-hybrid-infra/pull/24#pullrequestreview-5391630107) | A~F B 리뷰·D 방향 수신 유지. 최신 4파일/본문의 untagged 규칙/변수·GetDownloadUrlForLayer Action 제외, N 임시·Harbor A1 정합 및 같은 HEAD fmt/validate D 보고 접수. A 사람 승인·closed/merged와 Infra main `b3e6572ff3ddf7e068258102c2a7fa079acb4a7e` 확인. 실제 권한/Plan/CI/Pull 완료와는 별도 | A 공통 Provider/Lock·실제 Boundary/통합 Plan/Cost·Lifecycle Preview/E2E/최종 N, PAT 정책·Job 등록/회수·새 Build/Scan·Registry별 Digest/플랫폼·거부 Case·Worker Pull 후속. 완료한 A 승인/Merge와 옛 수정 지적은 재요구하지 않음 |
| I05 | 승인된 범위별 주/예비 보관자 | 보호 원본·독립 사본·오프라인 Key/해제·증거 접근/보존. 공급/Offline 전 | 이번 조회 범위에서 완료 근거 미확인 | 범위별 수신 수락 미확인 | 범위별 공급/접근·복호화/복원·보존 책임 확인 |
| I06 | 정태훈, 이유빈 리뷰, 최유준 lab | 개인 IDP/RBAC·Argo·비상 경로·초기 인증/세션 회수. 초기 관리자 종료 전 | [Argo 예제 동작/정리](https://github.com/seokpan/seokpan-hybrid-gitops/issues/3#issuecomment-5927423295)·[UWM 원복 보고](https://github.com/seokpan/seokpan-hybrid-gitops/issues/4#issuecomment-5928589042) | 해당 lab 참고 접수, 실제 관리 인계 수락 미확인 | 개인 IDP/SSO/RBAC·유지 비상·초기 인증/기존 세션 회수·잔존 확인 |
| I07 | 최유준 집계, 네 담당자 | 실제 가용시간·가격/Credit·누적/잔존·Plan·Window/재시험/정리. Full Apply 전 | 이번 조회 범위에서 Gate 충족 근거 미확인 | 실제 실행 조건 수신 수락 미확인 | $450 계획선/$500 한도·현재 Plan/가격·가용시간·실행 창 연결 |

기존 I01 lab 인계 참조: [#1 대역 DB/TLS](https://github.com/seokpan/seokpan-hybrid-gitops/issues/1#issuecomment-5926003372)·[#2 Manifest 인계 계획](https://github.com/seokpan/seokpan-hybrid-gitops/issues/2#issuecomment-5927202120)·[#3 예제](https://github.com/seokpan/seokpan-hybrid-gitops/issues/3#issuecomment-5927423295)·[#4 관측](https://github.com/seokpan/seokpan-hybrid-gitops/issues/4#issuecomment-5928589042). 새 #5/#6/#7의 결과와 구분해 보존합니다.

I02의 PR #12 보고는 Bootstrap Apply 및 foundation/rosa 접두사의 **임시 Probe Root** 시험이다. 실제 foundation/rosa 서비스 구현·생성·최종 권한 판정으로 확대하지 않는다. 당시 남은 세션 처리의 후속 Source는 PR #14(2026-10-02 10:13:35 KST 병합), 안내는 PR #15(11:39:58 KST 병합)로 연결한다. 읽은 diff에서 유효 모드 발급 전 이전 세션을 해제하고 실패 시 Caller를 표시한다. 인자 오타는 기존 세션을 유지한다. 모든 실패·만료·Caller 불일치 때 Plan/Apply가 차단되는지와 실제 Principal 일치는 실행 담당자가 확인한다. 기본 자격증명으로 남는 것을 안전한 실행 허가로 해석하지 않는다. 이 기록은 Source 읽기이며 실제 세션/Root를 실행한 결과가 아니다. Bootstrap 재구축·State 이전 반복은 요구하지 않는다.

인계가 일부 수락이면 사용 가능한 범위와 막히는 후속 실행을 적습니다. 값이 없으면 해당 작업만 대기하고 독립 준비는 계속합니다.

## Recovery Review Preparation

강사 피드백과 사용자의 일정·비용·팀 부담 고려 요청을 기존 W04/T17/T18 준비에 연결합니다. 새 목표나 지속 복제·Warm Standby 도입을 확정한 기록이 아닙니다. 현재 실제 RTO/RPO Run·담당자 수신 확인·실행 창은 이 후속 조회 범위에서 미확인입니다.

| 담당 / 기존 작업 | 다음 확인·인계 | 현재 범위 / 남은 실행 |
| --- | --- | --- |
| 김상희 — Infra #17/#19, I03/I05 | Dump/Import·Backup Data 시각/로컬 확보 지연·격리 DB/공간·목적 계정·CA/Key → B App, D 시간선, A 자산 | 사전 점검·Data 초안 보고와 실제 Backup/Restore를 구분. 예행 입력·Run 연결 필요 |
| 정태훈 — App #1·GitOps #5/#6, I01/I05 | Recovery Image/Manifest·새 Redis/Secret·상태 정리·로그인/대표 업무·클라이언트 접속 범위 → C/D | 기존 Seed/Image/base 인계를 우선 진행. App 기동부터 업무 재개까지 실측 필요 |
| 이유빈 — [Infra #23 foundation 공통 틀](https://github.com/seokpan/seokpan-hybrid-infra/issues/23)·[#16 Hybrid VPN](https://github.com/seokpan/seokpan-hybrid-infra/issues/16), I03 자산 협업 | Host/플랫폼·Storage 여유·로컬 DNS/Harbor/도구 가용 조건 → C/B/D | #23의 공통/Network·Data/Registry/VPN 통합 준비 Issue 접수. VPN 전용 VM 준비와 복구 DB/독립 Storage 확보를 구분; 실제 복구 자산은 별도 확인 |
| 최유준 — 기존 CI/lab/시험, I04/I07 | 기존 Run 양식의 전체 시간선·백업 경계/실패 조건, 네 사람의 추가 작업/학습/재시험·가용시간·비용 → 각 담당/변경 검토 | 계측·비용 준비 병행. 모든 주기/DR 구조를 구현하는 비교 시험을 추가하지 않음 |

설계 판단·변경 근거는 03 §3-I.14에, 최소 예행의 상세 측정/판정·부담 입력은 05 §9에 둡니다. 코드/입력/Blocker는 기존 작업 Issue·PR, 실제 값은 `evidence/<test-id>/<run-id>/`, 이 표에는 원문 링크와 수신 범위만 남깁니다. Docs Issue #8은 Source/입력 인계, Issue #6은 실제 Run의 발표 후보에 사용합니다. 담당자에게 전달·수락됐다고 미리 표시하거나 빈 Run을 만들지 않습니다.

공유 예행 시간은 실제 입력·리뷰·담당자 가용시간을 확인한 뒤 아래 Shared Execution에 연결합니다. 목표 변경은 업무 영향·실측·팀 부담·$450 계획선/$500 한도·Freeze를 함께 대조하고 새 Acceptance 적용 전에 결정합니다. 실측을 통과시키기 위한 사후 목표 완화나 전체 독립 작업의 대기를 요구하지 않습니다.


## 2026-10-02 후속 — App/Manifest Source 구현과 인계

PR #19 병합·브랜치 삭제를 확인했다. 직전 구현·인계 전체의 [재귀 검토 §9.10](05_IMPLEMENTATION_AND_VALIDATION.md#recursive-source-review-20261002)에서 App Fragment/인증서 문구·이관 명령/보호 규칙·GitOps 설정 반영·계측 경계/누락 순서를 보완했다. 계산 도구 최종16 검사이며 PR #20의 Source/기록 후보로 제공한다. 실제 실행 성공은 아니다. 이번 목적은 계측 도구 준비 뒤 실제 예행을 막는 App/Image/Manifest 입력을 해소해 시간·손실·접속·팀 부담의 근거를 얻는 것이다. [05 §9.9](05_IMPLEMENTATION_AND_VALIDATION.md#recovery-app-source-20261002)에 코드·검사/제한을 연결한다.

| 결과 / 원본 기록 | 현재 범위 | 다음 실행 / 수신 |
| --- | --- | --- |
| [App #1 인계](https://github.com/seokpan/seokpan-hybrid-app/issues/1#issuecomment-5950971722) | 정확한 DB/Redis 대상·TLS/별도 AUTH·Runtime/Migration 계약 코드. 최종 Python3.13.15/frozen lock 전체1728·신규58·관련155 검사. Seed `7fce757f963ba59cc81c03028c043be5b45719b2` + hybrid main `cef46c4e7b0cbd0cf6ebab487ee92c32d800ccdc` 초기 두 부모 Commit `c7a452d514742f77abd2c49c5836566df7386550` 뒤 최종 `8828ed22295c27c6f3b419e762b865d17eb50b8c`, 77개 이력 수정 Bundle 준비 | 인증된 개인 환경의 Branch Push/PR·기존 미커밋 코드 대조, D 새 Build/Scan/Digest와 C/D 대상/CA/Secret. 원격 main·팀 수신 미완료 |
| [GitOps Draft PR #9](https://github.com/seokpan/seokpan-hybrid-gitops/pull/9)·[#5 수신/인계](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5#issuecomment-5950971514) | HEAD `f1e959d2f3ec5207cc42f0523cbd391930b247d7`, 실제 Kustomize base/lab/Recovery Build·선언/출력 보존/ConfigMap Hash 11검사. D 원 lab SHA `259e73b0fac1af40f7bb7b43bd1982410d1df150`의 참고 범위 수락. replicas0/미해결 입력 후보이며 Apply/Sync 보류 | Source 리뷰·새 Image, lab TLS Redis/DB/CA/Secret·자원/UID, Recovery 플랫폼/Namespace·새 Redis·직접 DB·진입 입력. D 실제 #5/#6·C Bundle 수신/예행 필요 |
| [CI A~F B 리뷰](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-5950294428)·[D 수락](https://github.com/seokpan/seokpan-hybrid-app/issues/2#issuecomment-5950470901) | 승인/조건부 구현 경계 접수. A~F 재승인 질문 없음. F 수명은 승인04 무기한 허용 시 우선/제한 시 최대 허용 기준 유지 | D 실제 CI/보존/Preview·PAT/등록 재현, A foundation Worker Pull Owner. Source 후보와 실제 자격 발급/Push 성공을 구분 |

Owner 정태훈, 작성·로컬 검사 지원 Codex이며 실제 서버/Image·Restore 수행은 별도다. App Git Push 인증이 없어 승인된 전체 이력 이관은 사용자 전달용 묶음으로 준비하고 Snapshot 전송으로 바꾸지 않았다. 기존 팀원 기록과 Source 개별 관측 시각을 보존한다. Shared Execution/Cost Gate·Cloud Apply·Restore·장애 주입을 실행하지 않았고 실제 Run Index도 추가하지 않았다.

남은 흐름: 인증된 App 원격 Source → 새 Image/정확한 환경 입력 → lab·Recovery Bundle/자산 수신 → 실제 Run의 탐지부터 업무 재개 및 Backup Data 최신성/손실·팀 부담 → 필요 변경 판단/채택 후 설계·코드·그림·발표 반영. 공식 목표·복원 구조·1차 경계·예산/Freeze는 유지한다.


<a id="tjung03-registered-work-20261002"></a>

## 2026-10-02 후속 — 정태훈 전체 작업 등록과 ROSA 입력 준비

등록 결과 기록 시각은 `2026-10-02T11:53:47.771Z` / `2026-10-02T20:53:47.771+09:00`이다. [Docs #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21)와 [App #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4)·[GitOps #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10)·[Infra #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25)를 실제 번호로 연결했다. **TH-01~19·81개 세부 식별자는 유지**하며 새 분류나 19개 신규 Issue로 늘리지 않는다. 기존 App #1 Client·#2 CI, D의 GitOps #5/#6 및 Draft PR #9의 원래 결과/역할도 유지한다.

근거는 `2026-10-02T11:39:14.141Z`의 네 Repo Source 조회 묶음, 이후 새 Infra PR #24 HEAD 및 등록 객체다. Docs는 [PR #20](https://github.com/seokpan/seokpan-hybrid-docs/pull/20) HEAD `006d374b08d8c19fa1f047c8658a9c479dfe64f4`의 기록을 기반으로 후속 연결하며 main 병합으로 표기하지 않는다. 모든 객체의 동일 순간 Snapshot이나 실제 Runtime 재확인은 아니다. 앞선 §9.9/9.10·계측/검사 보고·다른 담당 행·과거 Source 관측은 보존했다.

ROSA는 [문서 준비 PR #27](https://github.com/seokpan/seokpan-hybrid-infra/pull/27), Commit `cfcf10d8c64a1eac6bdd4ade335569c2d7d00a55`의 `terraform/rosa/README.md`·`INPUT_CONTRACT.md`에 승인 모델·정본 Key·필요한 필드 의미/오류 차단·A 리뷰·실제 Gate·SG/Worker Pull Owner·T19·삭제/보존/잔존 비용을 연결한다. **후속 HCL 수신계약 준비**이며 A/B의 실제 필드·공급 형태·수신 개정 합의, HCL/Lock·Plan·Apply 또는 Cloud/Secret/권한 변경은 아직 완료로 기록하지 않는다.

[Infra PR #24](https://github.com/seokpan/seokpan-hybrid-infra/pull/24)의 옛 HEAD `33432eecc6cae81f7725c9d39f8a7730ca9ce815`에서는 N50·untagged7일과 Preview 전 untagged 제외·N 보류 조건의 정합을 요구했다. [B의 당시 후속 리뷰](https://github.com/seokpan/seokpan-hybrid-infra/pull/24#issuecomment-5951869578)에 부분 Source 수신과 최종 Preview/E2E Gate를 분리해 연결했다. A1의 Harbor 사본 Scan/Smoke와 PR 본문의 ECR Pull 설명·`GetDownloadUrlForLayer` 필요 범위도 당시 코드/설명 정합과 실제 E2E로 대조할 조건이었다. Source 정합 개정의 준비 범위는 부분 수신 가능하며, 최종 N·Lifecycle/CI 권한·Worker Pull의 확정/PASS는 실제 Preview/E2E·Role 후속 검증에 연결한다. Worker Pull은 [A #23 답변](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-5951505800)과 PR #24 모두 미완료다. 이 조건 때문에 독립 ROSA 입력계약·Source 준비를 중단하지 않는다.

후속 단일 조회의 관측 종료는 `2026-10-02T12:12:44.366Z` / `2026-10-02T21:12:44.366+09:00`다. [Infra PR #24](https://github.com/seokpan/seokpan-hybrid-infra/pull/24)는 HEAD `4fcbab4acc3e851f9a20a9affc4e4f4c29526add`, open·미병합이며 담당 4파일과 최신 본문에서 untagged 만료 규칙/변수 및 `GetDownloadUrlForLayer` 실제 Action 제외, N=50 임시 후보·Preview 후 최종 확정, Harbor A1 Scan/Smoke 경계를 확인했다. [D의 최신 본문·검사 갱신](https://github.com/seokpan/seokpan-hybrid-infra/pull/24#issuecomment-5951983854)의 같은 HEAD init/fmt/validate 성공은 담당자 보고로 접수하며 이번에 재실행한 결과가 아니다. 옛 HEAD의 수정 지적을 현재 코드에 다시 요구하지 않는다. A의 사람 재리뷰/Merge·공통 Provider/Lock·실제 Boundary/통합 Plan/Cost·Lifecycle Preview/E2E·Worker Pull은 별도 Gate로 남긴다. 최종 N과 제외 Action의 실제 필요 여부도 실행 근거로 판단한다.

[Infra #25 Source 준비 기록](https://github.com/seokpan/seokpan-hybrid-infra/issues/25#issuecomment-5951857787)는 HCL·Schema의 정적 준비 착수를 보고한다. [Infra #26](https://github.com/seokpan/seokpan-hybrid-infra/issues/26)는 중복으로 닫혔으며 rosa 코드/입력·Plan/Cost·Runtime 정본은 [Infra #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25)다. 이 보고가 HCL 게시·정적 검사 완료·Cloud 호출/Plan/Apply를 입증하지 않는다. 보고의 AWS 6.66.0 표기는 해당 시점 기록으로 보존하고, 실제 소비 Schema·Root Lock은 승인 04와 현재 채택 AWS 6.67.0에 대조한다.

등록·문서 준비·Source/팀 검사 보고·수신·실행/시험은 분리한다. 상위 Issue는 원본 링크·현재/다음/Blocker를 관리하고, 실제 결과는 해당 Issue·PR·새 Run에서 작성한다. 공유 충돌 실행은 아래 Shared Execution에서 조율하되 **이번 등록/문서 작업으로 실제 실행 행·빈 Run·Run Index를 추가하지 않았다.** 상세 조건과 다음 순서는 [05 §9.11](05_IMPLEMENTATION_AND_VALIDATION.md#tjung03-registration-rosa-input-20261002)에 연결한다.

<a id="tjung03-latest-source-20261002"></a>

## 2026-10-02 최신 후속 — Source 승인/병합과 Cloud·ROSA 후보

Repo 목록은 `2026-10-02T12:23:42.653Z` / `2026-10-02T21:23:42.653+09:00`, 특정 PR/리뷰/댓글의 관측 종료는 `2026-10-02T12:24:34.213Z` / `2026-10-02T21:24:34.213+09:00`다. **현재 상태는 이 후속과 [05 §9.12](05_IMPLEMENTATION_AND_VALIDATION.md#tjung03-latest-source-20261002)을 우선**한다. 위 등록 후속의 11:39·12:12 당시 A 재리뷰/병합 대기·Cloud/HCL 미게시 상태와 다른 담당자의 행은 과거 관측으로 보존한다. 이 관측은 동일 순간 Snapshot·Cloud/Runtime 재실행이 아니다.

| 최신 원본 | 현재 범위와 다음 조건 |
| --- | --- |
| [Infra PR #24](https://github.com/seokpan/seokpan-hybrid-infra/pull/24) `4fcbab4acc3e851f9a20a9affc4e4f4c29526add` | [A APPROVED 리뷰](https://github.com/seokpan/seokpan-hybrid-infra/pull/24#pullrequestreview-5391630107)·closed/merged 확인, Infra main `b3e6572ff3ddf7e068258102c2a7fa079acb4a7e` 연결. 당시 Source 정합/A 재리뷰 요구는 해소. 실제 Boundary/전체 foundation Plan/Cost·Lifecycle Preview/E2E·최종 N·CI/Pull은 남음 |
| [GitOps PR #11](https://github.com/seokpan/seokpan-hybrid-gitops/pull/11) `ce0ce5af9866428d7734db0bb8cce1d425ec20a2`·[#10 후속](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10#issuecomment-5952044630) | open/non-draft·13파일. Cloud 기본 FE/BE0, 각3/PDB2/soft AZ·Host preferred는 별도 Preview. 19 Source 검사 작성자/독립 보고 접수. base는 PR #9 branch이며 #9 사람 Merge 뒤 main으로 retarget. Cloud Apply/Sync·실제 Pull/TLS·1/3 Pod/업무 PASS 아님 |
| [Infra Draft PR #28](https://github.com/seokpan/seokpan-hybrid-infra/pull/28) `9a8410ab92e8a3283a41b90f913773d85ef30963`·[#25 후속](https://github.com/seokpan/seokpan-hybrid-infra/issues/25#issuecomment-5952123857) | 14파일 ROSA HCL·정확 Tool/Provider 제약·Lock/fmt/정적 Source 보고. PR #27 최신 `5eaef969723e29becbb1e0611d04660ddcbdb28d` 이력 소비; base는 #27 branch, 사람 Merge 뒤 main으로 retarget. 실행 validate/schema socket BLOCKED이며 Controller 동일 Source/Lock 재검증·실제 제한 Output/Role/지원 조합·첫 Plan 준비 리뷰 뒤 Source Review 진입. 전체 업무/Offline 완료는 직접 Draft 조건 아님 |

Data SG 본체/기반 Rule·Account-wide Role/정책·Worker Pull IAM/Attachment는 foundation, Cluster 종속 OIDC/Operator Role와 Worker→Data Binding은 rosa Owner/State다. 실제 제한 입력 수신·Worker Role/SG/ENI 적합성·서비스 권한/지원/Quota·IAM 전파·전체 Plan/Cost/Window·실제 Pull/관리/기동/업무·재생성/최종 정리는 여전히 해당 실행 Gate로 확인한다.

PR #28 삭제 Source 후보는 Binding 해제 → `cluster_enabled=false`로 Cluster만 삭제하고 IAM/OIDC 유지 → 실제 서비스 삭제 확인 → 별도 rosa cleanup이다. Provider timeout 뒤 State 제거 가능성 때문에 State 부재만으로 실제 삭제/안전 PASS를 판정하지 않는다. 기존 삭제 전 foundation 재실행/Binding 유지, App 쓰기/진행·최신 로컬 Backup 보호, 기반 Rule/Data/Network 및 bootstrap Backend 보존, 새 SG/Host/Context·이전 참조 제거·양쪽 Plan/T19와 최종 보호/Key·독립 사본/보관 책임·잔존 비용 조건은 유지한다.

TH-01~19·81개 식별자·팀 Must/상위 종료 조건을 변경하지 않았다. 새 Cloud API 조회/Plan/Apply·유료 작업·Runtime Run·체크 완료를 기록하지 않으며 Shared Execution/Run Index/계측 파일은 그대로 보존한다. 입력 대기는 해당 실행에 적용하고 독립 Source 검토·App 변경·Image/계약 인계를 병행한다.

<a id="cloud-rosa-app-progress-20261002"></a>

## 2026-10-02 후속 — Cloud·ROSA 코드와 App 경쟁 보완

최신 Source·검사 범위와 직접 입력 대기는 [05 §9.13](05_IMPLEMENTATION_AND_VALIDATION.md#cloud-rosa-app-followup-20261002), 원본 [GitOps #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10#issuecomment-5952044630)·[Infra #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25#issuecomment-5952123857)·[App #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4#issuecomment-5952269420)·[Docs #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21#issuecomment-5952326634)에 연결한다. 앞선 등록·PR 승인/병합 관측은 이력으로 유지하며 Source/Runtime 전체의 동일 순간 Snapshot으로 사용하지 않는다.

Cloud PR #11 HEAD `ce0ce5af9866428d7734db0bb8cce1d425ec20a2`는 #9 위의 별도 Stack이고 기본 각 0/별도 각 3 목표 Preview·19 Source 검사 결과다. ROSA Draft PR #28 HEAD `9a8410ab92e8a3283a41b90f913773d85ef30963`는 PR #27 최신 `5eaef969723e29becbb1e0611d04660ddcbdb28d`의 계약·이력을 소비한 14파일 HCL/Lock 후속이며 fmt·정적 검토와 validate/schema RPC socket BLOCKED를 구분한다. 각각 부모 PR 사람 Merge 뒤 main으로 retarget한다. Registry #24 최신 `4fcbab4`의 Source 정합·A 승인·사람 Merge와 main `b3e6572` 연결은 완료됐으며 통합 실행·Preview/E2E·Worker Pull이 남는다. 완료한 A 승인/Merge를 재요구하지 않는다.

App 최신 전달 Source는 `c837120c25c34b88bf6c6ee8e122ff50cbff062d`이며 고정 Seed 대비 39 수정파일·초기 hybrid main 대비 390 전체 이관파일·78개 이력을 보존한 새 `seokpan-hybrid-app-source-final-20261002.zip`을 준비했다. 최종 기본 전체 1,752 PASS·JUnit fail/error/skip 0·strict report PASS, 독립 관련 193·신규 순수 21/SQL Guard 3·별도 실제 Lua 3 PASS, Ruff 250·mypy 119 PASS다. opt-in 전체의 과거 1,754 PASS/기존 timeout 1 FAIL과 Controller 반복 종료 판별 제한은 05 §9.13의 검사 범위에 보존했다. 원격 전체 이력 Push 인증·개인 미반영 변경 대조·새 Image·실제 대상/CA/AUTH·1/3 Pod/DB·부분 실패와 실제 Bundle 수신은 남는다. GitOps #9 Draft의 직접 조건은 이 PR의 App/Image·lab/Recovery 조합·#5/#6 검증이며 Cloud 전체·최종 T18 완료까지 넓히지 않는다. Source Review/Ready/Merge와 실제 운영·Recovery Acceptance는 구분한다.

현재 Source 범위의 재귀 검토는 필수 추가 보완 0건에서 멈췄다. TH-01~19·81개 식별자·공식 시험·RTO 30분/RPO 90분/운영 중 1시간 백업·$450/$500·Freeze/Owner는 유지한다. Source 검사만으로 새 실제 Run/Run Index·Shared Execution 행·팀 수신/전체 TH 완료를 만들지 않았다.

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




<a id="recovery-minimum-handoff-20261003"></a>
## 2026-10-03 최소 Recovery 예행의 시각 근거·후속 준비

관측 `2026-10-03T08:39:33.333Z`: h-docs main `9017bcffa3ced2763382c5d1f112780d159ba15b`과 관련 원본을 읽었다. 사용자가 h-docs PR #20/#22·#7의 병합 후 언급된 브랜치를 직접 삭제했다고 알렸고, 원격 Branch 목록에서 해당 두 Branch 부재를 확인했다. h-infra PR #27은 필수 리뷰 0건으로 승인 대기, h-gitops PR #9/#11·h-infra PR #28의 직접 Draft 조건은 유지한다.

원래 목표 선택을 지원하는 이번 독립 준비는 [05 §9.14](05_IMPLEMENTATION_AND_VALIDATION.md#recovery-timezone-handoff-20261003)의 App 시각 요청 확인이다. B의 작성/로컬 보조 확인을 제출하며 C/D가 실제 행·Data 시점까지 수락했다고 기록하지 않는다. 기존 c837 Bundle/검사·Cloud/ROSA 전달 이력과 다른 담당자의 관측 시각·Shared Execution은 유지한다.

| 완료한 준비 | 직접 남은 입력 / 막는 작업 |
| --- | --- |
| B 정상 Source의 게임 UTC 저장/읽기·Pod TZ 영향 없음 확인; 05 §8.7의 기존 행 KST 단정 정정 | C/D의 실제 작성 Image·컬럼별 작성/세션 시각·보호 근거 → 과거 행 해석과 Backup Data 기준 확인 |
| 기존 Run CSV의 Data/로컬 완성 시각·지연/사본 간격 및 HANDOFF·I07 연결 안내 | C Backup·계정/CA/Key·격리 DB/공간, A Host/로컬 자산, B/D Image·Manifest/Secret·접속 → 최소 Dump/Restore·업무 예행 |
| 기존 30분/90분/1시간·현재 복원 구조 유지, 추가 Schema·Data/HCL·상시 서비스 변경 없음 | 실제 전체 시간·손실·접속·편의/부담/비용 → 03 §3-I.14 목표·주기·구조 선택 |

새 실제 Run·실측 수치·Index·공유 장애/Restore 실행은 만들지 않았다. 현재 준비는 전체 Cloud/ROSA·최종 05 종료 대기가 아니며, 최소 예행에 직접 필요한 입력만 해당 기존 원본에서 확인한다.
