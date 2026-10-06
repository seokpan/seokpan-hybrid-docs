# 2차 저장소 정합성 조사·수정 대장

> 조사 시작: 2026-10-07 KST  
> 상태: IN PROGRESS — 전수조사·수정·최종 재검증 미완료  
> 담당 범위: B 정태훈(tjung03)의 구현·문서·검토·인계. A/C/D 작업은 의존성 확인과 해당 담당자 인계로 구분한다.  
> 연결: [개인 작업 #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21), [팀 실행 #8](https://github.com/seokpan/seokpan-hybrid-docs/issues/8), [진행 문서 PR #64](https://github.com/seokpan/seokpan-hybrid-docs/pull/64)

## 1. 목적과 적용 범위

네 저장소의 승인 설계, 실행 코드, 운영 안내, 협업 기록, 그림과 등록용 프로젝트 소스 사이의 불일치를 추적한다. 코드가 존재한다는 사실, 병합, 인계 제출·수신, 실제 실행, 시험 판정을 구분한다. 이 대장은 조사 범위와 미해결 사항의 정본이며, 코드·실험·측정 결과의 원본을 대체하지 않는다. 해당 결과는 원 Issue·PR·Run에 기록하고 WORK_TRACKER와 05에 연결한다.

현재 문서의 잘못된 값·모호한 지시·대화 중계식 표현은 수정한다. 반면 과거 시험의 입력·측정값·실패, 당시 유효했던 설계와 실제 수행 이력은 현재 값으로 덮어쓰지 않는다. 도구 사용에 관한 서술을 줄이는 작업을 실제 수행자나 검증 범위를 다르게 꾸미는 작업으로 확대하지 않는다.

## 2. 고정 작업 체크리스트

아래 식별자와 문구를 후속 진행 보고에서도 유지한다. 부분 조회·파일 목록 확보·수정안 작성만으로 완료 표시하지 않는다.

- [ ] Q01 — GitOps #17의 병합·브랜치 삭제를 확인하고, Docs #64의 실행판·학습 안내·WORK_TRACKER·05와 PR 기록에 반영한 뒤 변경·리뷰 상태를 검증한다.
- [ ] Q02 — 네 저장소의 전체 문서·구현 코드·설정·시험·주석·관련 파일을 목록화하고, 활성 원본·재사용 원본·과거 이력·생성물을 구분하여 내용을 조사한다.
- [ ] Q03 — 네 저장소의 열린/닫힌 Issue·PR·본문·댓글·리뷰·검사와 모든 현재 Branch·Commit·변경 파일을 추적하고, 페이지 누락·접근 제한·삭제된 이력의 확인 범위를 기록한다.
- [ ] Q04 — 상위/하위 작업·담당자·입력·산출물·원 코드·시험·인계의 직접 의존과 후속 영향을 연결하여 순환 대기·오래된 완료/대기·누락을 확인한다.
- [ ] Q05 — Valkey 전환, OCP–Harbor 연결 제약과 내부 Registry 소비, DR RTO 10분·영속 DB RPO 30분·백업 계획 주기 15분을 설계·코드·가이드·시험·비용·주석에 걸쳐 대조하고 필요한 불일치를 수정한다.
- [ ] Q06 — 그림 생성 원본·manifest·출처 기록·SVG·PNG와 이를 참조하는 문서를 대조하고, 영향을 받은 생성물만 재생성·시각 검증한다.
- [ ] Q07 — 등록된 프로젝트 소스 7개를 저장소 정본과 내용·버전·해시로 대조하고, 필요한 등록용 개정본과 교체 대상을 제공한다. 실제 프로젝트 소스 교체는 별도로 확인한다.
- [ ] Q08 — B 명의 문서·Issue·PR·댓글의 대화 의존·자기 요청 중계·불필요한 AI 작업 홍보를 목적·변경·근거·결과·한계 중심으로 정리하고, 실제 수행·승인·시험 이력은 보존한다.
- [ ] Q09 — 실제 필요한 수정만 B 범위에서 처리하고, 다른 담당자의 변경을 보존하며 해당 담당자의 검토·입력·수신이 필요한 사항을 원 작업에 인계한다.
- [ ] Q10 — 발견→직접/후속 영향→수정→재검증을 반복하고, 종료 직전 원격 변경을 다시 대조하여 확인 가능한 전체 범위에서 새로운 확인·보완 사항이 없을 때 최종 수렴을 판정한다.
- [ ] Q11 — 조사 대상·관측 SHA·근거·발견·조치·검증·미확인·다음 순서를 이 대장과 원 작업에 보존하여 다음 작업 공간에서도 연속성을 유지한다.
- [ ] Q12 — 조사 결과를 B의 기존 TH 81개·실제 완료 상태·추가 작업·직접 입력·병행 작업·실행 Gate와 연결하고, #64 병합 여부는 별도 완료 통보를 전제로 하지 않고 GitHub에서 확인한다.

## 3. 우선순위와 종료 기준

| 순서 | 묶음 | 종료 기준 |
|---|---|---|
| P0 | #17 → #64 현재 상태 및 공유 문서 충돌 방지 | 실제 병합 SHA 반영, C의 신규 main 변경 보존, 기존 체크·이력 보존, 변경 diff·리뷰 상태 확인 |
| P1 | B의 다음 실행에 영향을 주는 설계·계약·인계 | Valkey/Registry/DR·Pool·Secret·실행 보류 조건을 원 코드와 대조하고 직접 Blocker를 분리 |
| P2 | 네 저장소 전면 조사·문서 서술 및 생성물 정합성 | 전체 대상의 검토 여부·제외 이유·수정·재검증 근거 확보 |
| P3 | 등록본 제공·최종 재검증·B 후속 실행계획 | 저장소 기준 개정본·남은 실제 입력·다음 작업 순서와 최종 관측 연결 |

지금은 P0/P1 조사 중이다. #64의 기존 네 파일 보완, 전체 저장소 전수조사, 그림 시각 검증 및 등록본 교체를 완료했다고 판정하지 않는다. 조사 과정의 변경을 한 번 게시한 사실과 Q10의 최종 수렴은 별개다.

## 4. 최초 관측 저장소와 Branch

다음은 순차 조회로 확보한 관측값이며 동일 순간의 원자적 Snapshot은 아니다. 이후 쓰기 직전과 조사 종료 직전에 다시 확인한다.

| 저장소 | 관측 main 전체 SHA | 관측한 다른 Branch |
|---|---|---|
| seokpan-hybrid-app | `2003fe9d0b27a9b443da26f9fb15cd829aaf8fed` | `reference/app-migration-history-20261002` → `c837120c25c34b88bf6c6ee8e122ff50cbff062d` |
| seokpan-hybrid-infra | `2af2d61f6985ca15dbe8415c84712575f0e92aeb` | `implementation/recovery-local-fixture-20261005` → `29b4a1f01bd555edeebac946cd8ee174da4432ab`; `infra/16-hybrid-route-preparation` → `f50d802f86a84bc887c801e1c3a1f2ab856181fd` |
| seokpan-hybrid-gitops | `fa3cea313e2cb1533d9703082619b085a3de25cc` | `reference/ocp-lab-original` → `259e73b0fac1af40f7bb7b43bd1982410d1df150` |
| seokpan-hybrid-docs | `8a0a6c7f23527995929451775868f9553531ae7c` | `docs/b-registry-vault-followup` → `2c3ee24cf8520d51d4389438c7a9728aeffe3bff`; `docs/49-bootstrap-data-iam` → `8acc04be6c626888d384792027c82cfd6ab7a7e6` |

관측된 현재 Branch 목록을 과거 삭제 Branch 전체 이력까지 조사한 결과로 해석하지 않는다. Recursive Tree 응답 확보와 각 파일의 전문·동작 검토도 구분한다. App main Tree의 `truncated=false`는 확인했으며, 전체 저장소의 내용·댓글·리뷰·검사·이력 수집 완결성은 아직 미판정이다.

## 5. 발견 및 조치 대장

### F01 — GitOps #17 병합 결과와 Docs #64의 오래된 대기 표시

- 원본: [GitOps #17](https://github.com/seokpan/seokpan-hybrid-gitops/pull/17), [승인 리뷰](https://github.com/seokpan/seokpan-hybrid-gitops/pull/17#pullrequestreview-5429183276).
- 실제 결과: 2026-10-06 23:45:46 KST 병합. 검토 HEAD `adacf6fffd9d179eef4715e92a3fed721759db55`, 병합 SHA `fa3cea313e2cb1533d9703082619b085a3de25cc`. `b/lab-internal-registry-binding`은 현재 Branch 목록에 없다.
- 해소된 범위: FE/BE·별도 Migration Job의 내부 Registry 주소 소비, 기존 Digest 보존, lab Harbor Pull 참조 제거, lab Redis URL/기대 Host 연결의 Source 병합 대기.
- 유지되는 범위: FE/BE replicas 0, Migration suspend/current/300초·단일 실행·목적 자격, 기존 Secret 보존. Valkey 선언·실제 Ready·앱 활성화·업무 시험은 별도다.
- 필요한 수정: #64의 네 실행 문서와 PR 본문에서 리뷰/병합 대기를 현재 결과로 정합화한다. 과거 HEAD와 병합 SHA, Image Source와 현재 App main을 혼동하지 않는다.
- 상태: 병합·Branch 관측 완료 / 기존 네 파일 보완 및 diff 검증 대기.

### F02 — #64 작업 중 Docs main에 #66 추가

- 원본: [Docs #66](https://github.com/seokpan/seokpan-hybrid-docs/pull/66), main `8a0a6c7f23527995929451775868f9553531ae7c`.
- 내용: C의 Data Root 전환·Valkey 7.2·Token 준비 및 05 §8.13/Tracker 갱신.
- 영향: #64의 옛 base `fa94b3ded9698516af9f4ec1837cab7e5cb74c2f`만 기준으로 공유 문서를 덮어쓰면 C 변경이 누락될 수 있다.
- 확인: #64의 기존 test-merge `840ecbb89e6753bea2d802f28150e06d7b179b40`은 옛 base와 HEAD의 조합이다. 최신 main과의 정합성을 이 Commit으로 대신 판정하지 않는다.
- 상태: 신규 main·Commit diff 확인 / 공유 파일 결합·최종 충돌 재검증 대기.

### F03 — Cloud 금고 공급 보고와 B 본인 확인 범위

- 기존 B 기록: 공개키 생성·C 전달 및 암호문 공급 안내 수신. 본인 복호화·암호문 해시 대조·독립 사본은 실제 결과 확인 대기.
- #66의 C 기록: A/B 계정에서 같은 파일을 해독할 수 있음을 확인했다는 보고가 추가됐다.
- 판단: 두 기록은 확인 주체·명령·시각·본인 수신 범위를 대조해야 한다. C의 계정별 확인 보고를 곧바로 B 본인의 확인·독립 백업 완료로 바꾸거나, 근거 없이 C 보고를 오류로 삭제하지 않는다.
- 상태: 추가 보고 확인 / 원 댓글·수신·수행 범위 대조 대기. 비밀값은 수집하지 않는다.

### F04 — 등록본과 저장소의 바이트 차이

등록된 파일의 Git Blob SHA를 실제 바이트에서 계산하고, Docs main `8a0a6c7f23527995929451775868f9553531ae7c`의 design Blob SHA와 대조했다.

| 파일 | 등록본 Blob SHA | 저장소 Blob SHA | 최초 판정 |
|---|---|---|---|
| 00_PROJECT_STARTING_POINT.md | `41206700637ac915022a2ef2daaf407e37fb6346` | `41206700637ac915022a2ef2daaf407e37fb6346` | 바이트 일치. 역사적 출발점 역할 유지 |
| 01_PROJECT_CHARTER.md | `be43d9c65876f41b8faa53de37cb9f2a8ed2c551` | `be43d9c65876f41b8faa53de37cb9f2a8ed2c551` | 바이트 일치. 의미·표현 전면 검토와는 별개 |
| 02_TARGET_ARCHITECTURE.md | `63952eec5373d427b3648c5eb3d0094622c40340` | `10a25c94ac062ab8b99616ad73a9a4e63a09e6bb` | 불일치. Valkey 등 개정 차이 대조 필요 |
| 03_DETAILED_DESIGN.md | `d09d638ff754d713cbb00b3dcb911dcc0c5dfb00` | `fc54c591f727559c40d5da8452c8ce854257eeb5` | 불일치. 저장소 자체의 남은 문제도 별도 확인 |
| 04_IMPLEMENTATION_READINESS.md | `cff6f9f752917f97f514ab4c3c408e1952581ef0` | `b0f2c2eaf6d6580f49e324cbe4df3d64937e1f38` | 불일치. 개정 및 현재/과거 경계 대조 필요 |
| PROJECT_INSTRUCTIONS.md | `08840b61ffa4ccdd4a49cb4e0ab00df9395fd820` | 대응 정본 위치 확인 대기 | 10/5 개정. 활성 Valkey 계약·문서 서술·기록 방식 검토 필요 |
| TJUNG03_IMPLEMENTATION_STUDY_AND_PRESENTATION_PLAN.md | `d156f579d3c03e9f6dd343e551931643aaa6766f` | 대응 정본 위치 확인 대기 | 10/5 개정. 이후 구현·인계·Valkey와 현재 실행판 대조 필요 |

바이트 일치만으로 해당 문서가 현재 설계와 의미적으로 정합하다고 판정하지 않는다. 갱신본을 제작한 사실과 실제 Project 등록 교체 완료도 구분한다.

### F05 — 저장소 03에도 DR의 병합 전 후보 표현이 남음

- 원본: [현재 관측 03 도입부](https://github.com/seokpan/seokpan-hybrid-docs/blob/8a0a6c7f23527995929451775868f9553531ae7c/design/03_DETAILED_DESIGN.md), [DR 선택 PR #30](https://github.com/seokpan/seokpan-hybrid-docs/pull/30).
- 발견: 도입부와 현재 상태 표에 `DR 설계 변경 후보`, `main에 병합되면`, `그 전 공식 main 기준은30분/90분/1시간`이 남아 있다. 등록본만의 문제가 아니다.
- 수정 방향: 현재 승인 설계는 RTO 10분·영속 DB RPO 30분·DB 운영 중 백업 계획 주기 15분으로 설명하고, 이전 30분/90분/1시간은 당시 이력으로 명시한다. 실제 전체 T18 또는 목표 달성 완료로 승격하지 않는다.
- 후속: 04·지침·Runbook·그림 생성 원본/manifest·SVG/PNG의 같은 전제를 추적한다. 단순 전역 문자열 교체는 하지 않는다.
- 상태: 현재 03 전문 중 도입부·상태 표의 불일치 확인 / 연쇄 수정·전체 재검증 대기.

### F06 — 현재 실행 안내에 과거 대기·대화 중계식 표현 혼재

- 원본: [#64 실행판](https://github.com/seokpan/seokpan-hybrid-docs/blob/2c3ee24cf8520d51d4389438c7a9728aeffe3bff/execution/TJUNG03_EXECUTION_BOARD.md), 기존 B 명의 PR/댓글 및 등록된 개인 계획.
- 발견: 상단 최신 표와 여러 이전 기록 아래의 `지금`, `현재`, 공개키 준비 대기·Harbor 소비 안내가 함께 존재한다. `사용자 확인으로`, `사용자가 제공한`, `B/AI`, `검토·기록 지원: ChatGPT` 등의 서술은 각 기록의 성격에 따라 정리 대상이다.
- 수정 방향: 활성 안내는 현재 기술적 목적·대상·상태·근거·다음 행동으로 독립적으로 읽히게 한다. 역사적 인계 기록은 관측 시점을 분명히 하며 필요 시 원 Commit/Issue에 연결한다. 실제 실행자·조건·측정 한계는 지우지 않는다.
- 상태: 실행판 전문과 일부 인용/등록본에서 확인 / 전면 분류·수정·참조 검증 대기.

## 6. 아직 완료하지 않은 조사

현재까지 네 저장소 전체의 모든 파일 전문, Issue/PR/댓글/리뷰·검사의 페이지, 현재 Branch의 전체 변경 이력, 모든 그림의 표시 내용과 PNG 시각 검증을 완료하지 않았다. 이 문서의 생성은 Q01~Q12 완료나 최종 수렴의 증거가 아니다.

다음 반복에서는 먼저 #64의 기존 네 문서·원 PR 기록을 F01/F02와 맞추고, F03의 원 보고를 대조한다. 이어서 엔진·Registry·DR 관련 설계/코드/그림 의존성을 추적하고 조사 범위를 나머지 파일·협업 기록으로 확장한다. 새로운 확인 대상이 생기면 발견 대장에 추가한다.

## 7. B 후속 작업의 유지 경계

#17 Source 병합 대기는 해소됐다. Cloud 금고 본인 확인·독립 보관, lab Valkey 선언/권한 검토, 실제 Data/Schema/CA·Route·사용창·live Diff 수락, 단계별 활성화와 동일 조합 시험, ROSA 실제 Caller/Backend·출력/SG·지원·Plan·비용·가동창은 서로 다른 작업이다. OCP 철거를 ROSA 준비 전체의 선행조건으로 추가하지 않는다.

기존 TH 81개와 실제 완료 체크를 이 조사 대장 때문에 바꾸지 않는다. #64 병합은 담당자의 GitHub 실제 상태로 재조회하며 별도 채팅 완료 통보를 선행조건으로 요구하지 않는다. 파일/PR 정리와 유료 실행·Runtime 수락을 합치지 않는다.
