# 2차 저장소 정합성 조사·수정 대장

> 조사 시작·이번 갱신: 2026-10-07 KST  
> 상태: IN PROGRESS — GitOps 병합 인계 반영·자료 수집 완료, 설계/검증기 한정 보완 PR #67 제출, 전체 의미 검토·수정·최종 수렴 미완료  
> 담당 범위: B 정태훈(tjung03)의 구현·문서·검토·인계. A/C/D 작업은 의존성 확인과 해당 담당자 인계로 구분한다.  
> 원 작업: [개인 작업 #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21), [팀 실행 #8](https://github.com/seokpan/seokpan-hybrid-docs/issues/8), [진행 문서 PR #64](https://github.com/seokpan/seokpan-hybrid-docs/pull/64), [설계·출처 보완 PR #67](https://github.com/seokpan/seokpan-hybrid-docs/pull/67)

## 1. 목적과 판정 원칙

네 저장소의 승인 설계, 실제 코드, 운영 안내, 협업 기록, 그림과 등록용 프로젝트 소스 사이의 불일치를 추적한다. 코드 존재·병합·인계 제출·수신·실제 실행·시험 판정을 구분한다. 이 대장은 조사 범위와 미해결 사항을 보존하며 코드·실험·측정의 원본을 대체하지 않는다. 해당 결과는 원 Issue·PR·Run에 기록하고 WORK_TRACKER와 05에 연결한다.

현재 안내의 잘못된 값·모호한 지시·대화 중계식 표현은 수정한다. 과거 시험의 입력·측정값·실패, 당시 유효했던 설계와 실제 수행 이력은 현재 값으로 덮어쓰지 않는다. 불필요한 도구 관련 서술을 줄이는 작업을 실제 수행자·승인·검증 범위를 다르게 꾸미는 작업으로 확대하지 않는다.

파일 목록이나 검색 결과만으로 전수조사를 완료 처리하지 않는다. 발견→원 근거→직접·후속 영향→필요한 수정→재검증을 반복한다. 접근 가능한 대상의 확인 대기와 발견 사항이 모두 처리되고, 종료 직전 원격 변경 대조에서도 새로운 확인·보완 사항이 없을 때 Q10을 완료한다. 아직 그 상태가 아니다. 한정된 수정 묶음의 검사 성공과 전체 수렴은 별도다.

## 2. 고정 작업 체크리스트

아래 식별자와 문구를 후속 진행 보고에서도 유지한다. Q01은 병합 인계 문서의 반영·검사·리뷰 상태 확인 완료이며 사람 리뷰 승인이나 #64 병합 완료를 뜻하지 않는다. Q11은 이번 조사 근거와 미완료 사항의 보존 완료이며 전체 수렴을 뜻하지 않는다.

- [x] Q01 — GitOps #17의 병합·브랜치 삭제를 확인하고, Docs #64의 실행판·학습 안내·WORK_TRACKER·05와 PR 기록에 반영한 뒤 변경·리뷰 상태를 검증한다.
- [ ] Q02 — 네 저장소의 전체 문서·구현 코드·설정·시험·주석·관련 파일을 목록화하고, 활성 원본·재사용 원본·과거 이력·생성물을 구분하여 내용을 조사한다.
- [ ] Q03 — 네 저장소의 열린/닫힌 Issue·PR·본문·댓글·리뷰·검사와 모든 현재 Branch·Commit·변경 파일을 추적하고, 페이지 누락·접근 제한·삭제된 이력의 확인 범위를 기록한다.
- [ ] Q04 — 상위/하위 작업·담당자·입력·산출물·원 코드·시험·인계의 직접 의존과 후속 영향을 연결하여 순환 대기·오래된 완료/대기·누락을 확인한다.
- [ ] Q05 — Valkey 전환, OCP–Harbor 연결 제약과 내부 Registry 소비, DR RTO 10분·영속 DB RPO 30분·백업 계획 주기 15분을 설계·코드·가이드·시험·비용·주석에 걸쳐 대조하고 필요한 불일치를 수정한다.
- [ ] Q06 — 그림 생성 원본·manifest·출처 기록·SVG·PNG와 이를 참조하는 문서를 대조하고, 영향을 받은 생성물만 재생성·시각 검증한다.
- [ ] Q07 — 등록된 프로젝트 소스 7개를 저장소 정본과 내용·버전·해시로 대조하고, 필요한 등록용 개정본과 교체 대상을 제공한다. 실제 프로젝트 소스 교체는 별도로 확인한다.
- [ ] Q08 — B 명의 문서·Issue·PR·댓글의 대화 의존·자기 요청 중계·불필요한 AI 작업 홍보를 목적·변경·근거·결과·한계 중심으로 정리하고, 실제 수행·승인·시험 이력은 보존한다.
- [ ] Q09 — 실제 필요한 수정만 B 범위에서 처리하고, 다른 담당자의 변경을 보존하며 해당 담당자의 검토·입력·수신이 필요한 사항을 원 작업에 인계한다.
- [ ] Q10 — 발견→직접/후속 영향→수정→재검증을 반복하고, 종료 직전 원격 변경을 다시 대조하여 확인 가능한 전체 범위에서 새로운 확인·보완 사항이 없을 때 최종 수렴을 판정한다.
- [x] Q11 — 조사 대상·관측 SHA·근거·발견·조치·검증·미확인·다음 순서를 이 대장과 원 작업에 보존하여 다음 작업 공간에서도 연속성을 유지한다.
- [ ] Q12 — 조사 결과를 B의 기존 TH 81개·실제 완료 상태·추가 작업·직접 입력·병행 작업·실행 Gate와 연결하고, #64 병합 여부는 별도 완료 통보를 전제로 하지 않고 GitHub에서 확인한다.

## 3. 수집 범위와 한계

[읽기 전용 수집 Run](https://github.com/seokpan/seokpan-hybrid-docs/actions/runs/37499657745)은 2026-10-07 01:56:38~01:59:32 KST에 다음 자료를 수집했다. 공개 저장소 Source와 GitHub 협업 기록만 읽었으며 이 수집 Run에서는 프로젝트 코드를 실행하지 않았다. 이후 별도 수정 검증 Run은 §5.10에 기록한다.

| 저장소 | main 파일 | 현재 Branch | 일반 Issue | PR | 일반 댓글 | 리뷰 제출 | 도달 가능한 Commit | Workflow Run 목록 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| App | 392 | 2 | 9 | 6 | 19 | 7 | 91 | 0 |
| Infra | 56 | 3 | 14 | 23 | 100 | 54 | 99 | 26 |
| GitOps | 50 | 2 | 9 | 8 | 40 | 12 | 39 | 60 |
| Docs | 70 | 3 | 15 | 51 | 21 | 0 | 141 | 2 |
| 합계 | 568 | 10 | 47 | 88 | 180 | 73 | 370 | 88 |

위 표는 최초 수집 시점의 고정 목록이다. Issue 수는 PR을 제외한다. 당시 열린 일반 Issue는 21개, 열린 PR은 Docs #64 한 개였고 Inline review comment는 0개였다. 모든 PR의 리뷰·변경 파일 목록·Commit, 모든 당시 Branch의 파일 트리, 당시 Branch/열린 PR HEAD의 Check·Status, Milestone·Tag와 Workflow Run 목록을 포함한다. 당시 Branch 전체의 파일 경로는 합산 1,215개이며 중복 제거된 Git Blob 644개를 확보했다. 이후 새 PR #67·작업 Branch·Run은 이 표에 소급 합산하지 않고 추가 관측으로 연결한다.

323개 페이지 응답의 다음 페이지 여부를 보존했고 수집 오류는 0건이다. 각 Issue/PR의 `comments` 수와 수집한 일반 댓글을 번호별로 대조하여 불일치 0건을 확인했다. 저장소별 수집 시작/종료 Branch 목록과 SHA는 일치했다. 순차 조회이므로 네 저장소 전체가 같은 순간의 원자적 Snapshot이라는 뜻은 아니다.

수집 Artifact는 `repository-audit-snapshot-8d5470649e55f32d6441a6105634cf823ce904ab`, ID `11429411389`, ZIP SHA256 `a2eeb0edf313af04f2cec35a45874c1056f13d9783f3c6aabd96550d44a86ef9`다. 이번 재개에서도 ZIP과 644개 Blob의 Git SHA를 다시 대조했다. GitHub 보존 만료는 2026-10-14 01:59:32 KST다. 조사 작업 사본에는 `snapshot-index.json`, `pagination.json`, `excluded-files.json`, 저장소별 `metadata/`, Branch별 `trees/`, `blobs/`를 보존한다. 폰트·개인키·암호화 운영 입력·고위험 자격 패턴은 수집 제외 조건으로 두었고 이번 트리에서 제외된 파일은 0개다. 실제 Secret 공급 경로나 내용은 조사하지 않았다.

**아직 확인하지 않은 범위:** 모든 함수·문장·댓글의 의미 검토, 모든 과거 Run의 job log/artifact 독립 재검증, 과거 삭제된 비도달 Commit/로컬 미커밋 자료, 보호 운영 환경과 실제 설정·자격·Runtime이다. 도달 가능한 Commit 수는 당시 refs의 이력 색인이며 전체 과거 코드 diff의 의미 검토 완료 건수가 아니다. Inline thread 해결 여부는 열린 Docs #64에서 별도 조회하여 0건을 확인했다.

### 3.1 내용 선별 검사

main 파일 568개 중 UTF-8 텍스트 556개에 대상 표기·참조 검사를 적용했다. Python 3.13.5 AST로 Python 파일 243개를 파싱했고 오류는 0건이다. 이는 구문 확인이며 의존성 설치·실제 프로젝트 조합·기능/통합 시험이 아니다. main 텍스트의 Issue/PR 참조 192개를 수집 목록과 대조했으며 번호가 없는 참조는 0개다. URL 전체·fragment·인계 의미가 모두 맞는다는 판정은 아니다.

DR 후보·이전 엔진·대화 메타·Harbor 표기의 최초 검색 후보는 각각 19·11·16·27건이다. 검색 건수를 결함 건수로 사용하지 않는다. 역사 기록·프로토콜 이름·호환 인터페이스·실행 보류 후보와 잘못된 현재 안내를 문맥별로 나눠 검토한다. 기존 파일별 경로·SHA·분류·확인 수준과 이번 검증 로그·변경 Patch를 함께 보존한다.

## 4. 관측한 Source

| 저장소 | 최초 수집 main 전체 SHA | 그 밖의 당시 Branch |
|---|---|---|
| App | `2003fe9d0b27a9b443da26f9fb15cd829aaf8fed` | `reference/app-migration-history-20261002` → `c837120c25c34b88bf6c6ee8e122ff50cbff062d` |
| Infra | `2af2d61f6985ca15dbe8415c84712575f0e92aeb` | `implementation/recovery-local-fixture-20261005` → `29b4a1f01bd555edeebac946cd8ee174da4432ab`; `infra/16-hybrid-route-preparation` → `f50d802f86a84bc887c801e1c3a1f2ab856181fd` |
| GitOps | `fa3cea313e2cb1533d9703082619b085a3de25cc` | `reference/ocp-lab-original` → `259e73b0fac1af40f7bb7b43bd1982410d1df150` |
| Docs | `8a0a6c7f23527995929451775868f9553531ae7c` | 수집 중 #64 `docs/b-registry-vault-followup` → `8d5470649e55f32d6441a6105634cf823ce904ab`; `docs/49-bootstrap-data-iam` → `8acc04be6c626888d384792027c82cfd6ab7a7e6` |

#64의 수집 후 변경은 문서 결과·조사 기록 갱신과 임시 수집 workflow 제거다. 재개 시 #64 HEAD `69e321a097cde7a30940a62b16d28d45bc161841`를 확인했고, 그 이후 이번 대장 갱신은 이 PR의 추가 Commit이다. 수집 시점 SHA를 최종 HEAD로 표현하지 않는다.

추가 Source는 #67의 `docs/b-design-consistency-20261007` / `6d43339b01db760fa5856d083c4fcf33eae2f71c`다. 이 Branch는 main `8a0a6c7...`에서 분기했으며 #64와 변경 파일이 겹치지 않는다. 실제 병합은 아직 수행하지 않았다. 작업 전·종료 전 원격 변경을 다시 확인한다.

## 5. 발견·조치·재검증

### F01 — GitOps 병합 결과와 Docs 인계: 반영 완료

[GitOps PR #17](https://github.com/seokpan/seokpan-hybrid-gitops/pull/17)은 2026-10-06 23:45:46 KST 병합됐다. 검토 HEAD는 `adacf6fffd9d179eef4715e92a3fed721759db55`, 병합 SHA는 `fa3cea313e2cb1533d9703082619b085a3de25cc`다. `b/lab-internal-registry-binding` 브랜치 삭제를 확인했다.

#64의 실행판·학습 안내·Tracker·05에 병합 결과와 실제 실행 대기를 반영했다. [문서 보존 검사 Run](https://github.com/seokpan/seokpan-hybrid-docs/actions/runs/37499302235)의 결과 Commit은 `e3da382398cd76e17cf52fb88353719750938364`다. 기존 체크박스 줄·TH 식별자 수·C의 §8.13 보존, 허용 변경 경로·diff 검사를 통과했다. 내려받은 결과 ZIP SHA256 `7c7f8ff590d02fbc5c2d2b2126b35c36ac900117b3a6d91cd093e75b9e0d6530`도 대조했다. 복사 과정에서 깨졌던 채팅의 금고 예시와 달리 저장소의 Bash 예시는 온전하며 `bash -n`을 통과했다. 실제 복호화 결과는 아니다.

[GitOps 원 작업 댓글](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10#issuecomment-6016940121), [승인 검토 댓글](https://github.com/seokpan/seokpan-hybrid-gitops/pull/17#issuecomment-6018620254), [Docs PR 댓글](https://github.com/seokpan/seokpan-hybrid-docs/pull/64#issuecomment-6018633372)과 #64 본문도 갱신했다. 재개 시 #64는 Ready/open이며 A/C/D 리뷰 요청, 제출된 사람 리뷰와 inline thread 각 0건을 확인했다. 병합은 별도이며 완료 통보를 선행조건으로 요구하지 않는다.

### F02 — C의 신규 main 변경 보존: 결합 완료

[Docs PR #66](https://github.com/seokpan/seokpan-hybrid-docs/pull/66)의 main `8a0a6c7f23527995929451775868f9553531ae7c`를 #64 작업에 결합했다. C의 Data Root·Valkey·Token 기록과 Tracker 변경을 보존했고 05 §8.13의 정확한 블록 일치를 검사했다. 이전 test-merge `840ecbb89e6753bea2d802f28150e06d7b179b40`은 옛 base 조합이므로 최신 main 결합 검증으로 사용하지 않았다. 당시 임시 두 workflow는 최종 파일 트리에서 제거했다. 이번 #67도 05·WORK_TRACKER를 변경하지 않는다.

### F03 — 금고 공급자 보고와 B 본인 확인: 실행 결과 대기

B 공개키 생성·C 전달과 암호문 공급 안내 수신은 완료다. #66에는 C의 A/B 계정별 해독 확인 보고가 추가됐다. 기존 [B 수신 기록](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6016940538)은 B 본인 확인·암호문 해시 대조를 후속으로 남겼다.

두 보고의 확인 주체와 범위를 구분해 네 문서에 연결했다. C 보고를 삭제하지 않고 B 본인 확인·수신·독립 백업을 자동 완료 처리하지 않는다. 새 수행 결과가 들어오면 원 Issue에서 시각·범위·비민감 판정만 확인한다. Cloud Token을 lab Token으로 대체하거나 평문을 수집하지 않는다.

### F04 — 등록 프로젝트 소스: 대조 완료, 개정본 일부 준비·전체 교체 대기

등록된 7개 파일의 실제 바이트에서 Git Blob SHA·SHA256을 계산했다. 다음은 Docs main `8a0a6c7f23527995929451775868f9553531ae7c`와의 최초 대조다.

| 파일 | 등록본 Blob SHA | 당시 저장소 Blob SHA | 판정 |
|---|---|---|---|
| 00_PROJECT_STARTING_POINT.md | `41206700637ac915022a2ef2daaf407e37fb6346` | 동일 | 바이트 일치. 역사적 출발점으로 보존 |
| 01_PROJECT_CHARTER.md | `be43d9c65876f41b8faa53de37cb9f2a8ed2c551` | 동일 | 바이트 일치. 전체 의미 검토 완료와는 별개 |
| 02_TARGET_ARCHITECTURE.md | `63952eec5373d427b3648c5eb3d0094622c40340` | `10a25c94ac062ab8b99616ad73a9a4e63a09e6bb` | 불일치 |
| 03_DETAILED_DESIGN.md | `d09d638ff754d713cbb00b3dcb911dcc0c5dfb00` | `fc54c591f727559c40d5da8452c8ce854257eeb5` | 불일치 |
| 04_IMPLEMENTATION_READINESS.md | `cff6f9f752917f97f514ab4c3c408e1952581ef0` | `b0f2c2eaf6d6580f49e324cbe4df3d64937e1f38` | 불일치 |
| PROJECT_INSTRUCTIONS.md | `08840b61ffa4ccdd4a49cb4e0ab00df9395fd820` | 同名 정본 없음 | Project 전용 지침. 10/5 이후 설계·기록 방식과 대조 필요 |
| TJUNG03_IMPLEMENTATION_STUDY_AND_PRESENTATION_PLAN.md | `d156f579d3c03e9f6dd343e551931643aaa6766f` | 同名 정본 없음 | Project 개인 보조 소스. 실행판·Docs #21·현재 원 작업과 대조 필요 |

현재 Branch 트리에서 마지막 두 파일의 동명 저장소 정본은 확인되지 않았다. 무관한 파일을 대신 정본으로 취급하지 않는다. 당시 저장소 자체에도 F05/F07/F08이 남아 있었으므로 기존 main을 그대로 재등록하는 것으로 해결하지 않았다.

이번에는 #67의 검증·게시 Commit에서 02/03/04 세 파일의 검토용 사본을 준비했다. `REVIEW_MANIFEST.json`에 기존 등록본과 새 사본의 SHA256, 원 Commit·PR·검증 Run을 명시한다. #67 리뷰에서 추가 변경이 생기면 최신 검증본을 사용한다. Project 실제 교체는 수행하지 않았으며 지침·개인 계획의 전면 현행화는 남아 있어 Q07은 미완료다.

### F05 — DR 현재/과거 경계: #67 수정·검증 완료, 리뷰·병합 대기

발견 당시 [03 도입부·§3-G.7·§3-I.14.5](https://github.com/seokpan/seokpan-hybrid-docs/blob/8a0a6c7f23527995929451775868f9553531ae7c/design/03_DETAILED_DESIGN.md)에 `변경 후보`, `main에 병합되면`, `그 전 공식 main 기준은30분/90분/1시간`이 현재 설명으로 남아 있었다. 04 도입부에도 같은 조건이 있었고 02는 10/3 재검토를 현재처럼 설명했다.

[PR #30](https://github.com/seokpan/seokpan-hybrid-docs/pull/30)의 실제 병합 `ab116463fd1f1a75d54e734c3c1c99cd098f639d`를 대조하고 #67에서 현재 요구를 RTO 10분·영속 DB RPO 30분·DB 운영 중 Backup 15분 계획 주기로 정합화했다. 관련 상태표·Data 예약/보관량·시험/G7/B06·Gateway MTTR와의 구분·04 인계·두 manifest를 함께 보완했다. 이전 30분/90분/1시간과 철회된 후보, 실제 부분 Run은 보존했다.

03의 명시적 anchor 4개와 02/03/04 체크박스 항목 수 14/134/48을 유지했다. 실제 #30 병합을 나타내는 기존 DR 설계 항목 3개만 완료로 정정했으며 Runtime·B TH 체크를 올리지 않았다. 이 조치는 지정한 설계 표현의 정합성 보완이며 네 저장소의 모든 관련 코드·비용·문장 검토가 끝났다는 뜻은 아니다.

### F06 — 독립적인 현재 안내와 기록 주체: 일부 수정, 전면 정리 대기

실행판·가이드·팀 안내와 B 명의 Issue/PR/댓글에 `작성 요청`, `사용자 확인으로`, `사용자가 제공한`, `B/AI`, 불필요한 도구 지원 표기와 여러 시점의 `지금/현재`가 섞여 있다. 사용자 서비스 요청을 뜻하는 정상 문장과 문서 작성 과정의 메타 문장을 구분한다.

#64의 새 인계 문구와 F01의 댓글 세 곳은 목적·결과·근거·미실행 범위로 정리했다. #67에서는 팀 안내의 작성 요청/도구 지원 헤더, 아키텍처 제작·검토 문서와 수정한 설계 도입부·상태 설명을 정리했다. 나머지 전체 본문·Issue/PR/댓글·참조는 아직 전면 정리하지 않았다.

활성 안내는 현재 행동으로 독립적으로 읽히게 하고 과거 기록은 시점·원 Commit/Issue를 명확히 한다. 실제 합성 시험의 수행자·승인자·관측 환경·실패·측정값을 지우거나 사람의 직접 수행으로 바꾸지 않는다. 이번 새 PR과 결과 기록은 기술적 목적·변경·검증·범위로 작성한다.

### F07 — Diagram manifest 메타데이터 유실: #67 수정·회귀검증 완료

기존 검증 스크립트는 result를 새로 만들며 `followup_review`, `followup_review_history`, `data_engine_followup`, `check_scope_history`, `latest_check_scope`를 보존하지 않았다. 이전 격리 재현에서 정상 종료 후 다섯 키가 사라졌다. 그 재현은 재구성 layout을 사용한 메타 유실 확인이며 원래 전체 layout의 독립 시각 검증 결과는 아니었다.

#67에서는 계산 필드와 현재 설계 메타의 정본을 구분하고, 과거 이력·확장 필드를 보존했다. 이전 latest 검사 범위는 history로 이동하며 같은 입력의 재실행은 같은 바이트를 유지한다. 원자적 쓰기로 교체 중단 시 기존 manifest를 보존한다.

새 `--integrity-only`는 기존 SVG/PNG 바이트를 manifest와 대조한 뒤 원문·XML·폰트·크기를 검사하며 layout geometry는 0/생략으로 명시한다. 기본 모드는 layout이 없으면 실패한다. 단위 회귀 13개, layout 누락·Source 변경·PNG 변경의 실패 경로 3개, 실제 12쌍 산출물·반복 실행·과거 기록 보존을 로컬과 원격 Run에서 재검증했다. 이 Source 수정은 #67에 제출됐으며 아직 main 병합 전이다.

### F08 — Data Source 상태: #67 정합화, 실제 생성·호환성 대기 유지

실제 [foundation/data_redis.tf](https://github.com/seokpan/seokpan-hybrid-infra/blob/2af2d61f6985ca15dbe8415c84712575f0e92aeb/terraform/foundation/data_redis.tf)는 `engine = "valkey"`다. 발견 당시 02 §10·03 §3-D.9.7·04 §1과 두 manifest는 Source가 Redis OSS 7.1이며 C Root PR 전환 대기라고 설명했다.

#67에서 Valkey 7.2 선택·Infra #37 Source 병합을 완료된 범위로 연결하고 실제 생성·호환성/업무·정확 Image 수락은 별도로 유지했다. `Redis` 프로토콜·계층, `SEOKPAN_REDIS_*`, `backend-redis-*`, Terraform `redis_*`와 과거 시험은 일괄 개명하지 않았다. App Pool 제안·상한/종료 중 연결 예산을 엔진 전환만으로 채택·검증된 것으로 올리지 않았다.

### F09 — 그림과 실행 보류: 보존·한정 검증 완료, 전체 의미 대조 대기

12개 SVG의 표시 문구를 추출해 대조했다. 그림 01/02/04/12는 이미 Valkey 7.2를, 그림10은 RTO 10분·영속 DB RPO 30분·DB 운영 중 15분 Backup을 표시한다. Generic Redis 계층명과 1차 자산은 남아 있다. 이번에 12장 전체 배치와 그림10 상세를 시각 확인했으며 이미 맞는 24개 SVG/PNG를 다시 만들지 않았다.

12개 builder 본문을 기존 SVG 텍스트와 정확히 대조하고 내장 subset 폰트의 측정값으로 본문 경계를 확인했다. 원본 전체 폰트 설치·전체 layout 재생성으로 표현하지 않는다. 자동 무결성 검사와 모든 그림의 의미·화살표·참조·가독성 전면 검토는 별개이며 Q06은 미완료다.

GitOps Recovery `redis.yaml`은 `redis-server`, TCP Probe, 입력 대기 Image/PVC와 replicas 0을 유지한다. 선택한 Valkey Image·실행 파일·TLS/AUTH Probe·저장 정책을 실제 수락하기 전의 보류 인터페이스다. 기존 후속 구현에 연결할 대상이지 임의 Image나 새 Storage 정책으로 채울 사유가 아니다. lab에는 별도 Valkey 서버 선언이 아직 없으며 D 작성 제안·실제 수락을 구분한다.

### F10 — #67 게시 결과와 검증 산출물

- PR: [Docs #67](https://github.com/seokpan/seokpan-hybrid-docs/pull/67), Ready. C/D 리뷰 요청. 사람 승인·병합은 아직 완료로 기록하지 않음.
- 게시 Source: `6d43339b01db760fa5856d083c4fcf33eae2f71c`. 최종 변경 13개 파일, 임시 적용 입력 2개·workflow 1개는 최종 트리에서 제거.
- [검증·게시 Run 37506177013](https://github.com/seokpan/seokpan-hybrid-docs/actions/runs/37506177013): success. trigger SHA는 `1d68f77748ff0446f2908eeee57d39de8c2a644e`, 검증한 결과를 위 Source Commit으로 게시했다. 서로 다른 SHA를 동일한 CI HEAD로 표현하지 않는다.
- 실제 검사: 검증기 회귀 13개·기존 recovery_metrics 회귀 16개 PASS, 실패 경로 3개 거부/원본 보존, SVG/XML 12·PNG decode 12·내장 글리프 12·Subnet 9·원문 식별 5, 반복 바이트 동일, builder 본문 12개 일치.
- 보존: 24개 SVG/PNG, 00/01, evidence 전체, C의 05/WORK_TRACKER. 수정 파일을 정확한 13개 경로로 제한했다.
- Artifact: `design-consistency-verification-37506177013`, ID `11432016175`, ZIP SHA256 `723837e00ee8f632862a3d461886dd36cb4e1f862296be43b0c3425120a64332`. 다운로드 후 ZIP 및 13개 출력 파일의 해시를 다시 대조했고 검토한 로컬 바이트와 일치했다.
- Artifact 보존 만료: 2026-10-21 02:47:07 KST. 로그·출력 Hash·변경 Patch·검증 파일을 작업 사본에도 보존했다. 실제 Cloud/클러스터/금고/Runtime 실행은 없음.

## 6. 조사 반복과 현재 중단점

| 반복 | 확인·조치 | 새로 연결된 확인 대상 | 판정 |
|---|---|---|---|
| 1 | #64 실제 HEAD·#17 병합·#66 main 변경 대조 | 공유 네 문서 보존 결합·현재 대기 갱신 | F01/F02 조치 및 보존 검사 완료 |
| 2 | 네 저장소 자료 수집·페이지/댓글 수·Blob 검증 | DR 현재/과거, Data Source 상태, 기록 주체, 등록본 차이 | 수집 완료, 의미 검토 진행 중 |
| 3 | 생성기·manifest·12 SVG 표시·Source 연결 대조 | 정상 종료하면서 최신 메타 5개 유실 | F07 격리 재현 |
| 4 | 등록본 해시·Python 구문·Issue/PR 참조 번호 대조 | 저장소 설계 자체 보완 뒤 등록본 준비 필요 | 전체 수렴 아님 |
| 5 | F05/F07/F08 수정·메타/검사 이력·생성기 본문/산출물·보존 재검증 | 수정된 13개 경로의 전송/게시 바이트, PR 리뷰·등록본 구분 | #67 제출 및 원격 출력 해시 확인. 한정 수정 검증 완료 |

Q01의 병합 인계와 Q11의 조사 기록 보존은 마쳤다. Q02~Q10/Q12의 전체 완료는 아직 아니다. F05/F07/F08을 #67로 수정했다고 해서 모든 문장·코드·댓글의 추가 보완이 0건이라고 선언하지 않는다. 수정 묶음의 결과·한계와 미확인 대상을 계속 이어간다.

## 7. 다음 작업 순서와 B 실행 연결

1. 작업 시작마다 #64와 #67의 실제 HEAD·리뷰·병합·Branch를 확인한다. 별도 채팅 완료 통보를 기다리지 않는다. #64 인계 문서와 #67 설계/검증기 수정은 서로 다른 파일 범위이며 전체 전수조사를 두 PR 병합의 새로운 일괄 선행조건으로 추가하지 않는다.
2. Q02~Q04/Q08의 나머지 문서·주석·Issue/PR/댓글을 문맥별로 검토한다. 실행판에 반복된 과거 `지금/현재`와 이미 공급/병합된 작업의 대기, 자기 요청 중계 문구를 우선 정리한다. 역사적 Run·실제 수행자는 보존한다.
3. Valkey/lab/Recovery의 남은 실행 선언, Pool/종료 예산·Build/Digest, Registry/Writer·Secret·ROSA 입력을 각각 원 코드·담당 인계와 대조한다. 다른 담당자의 실제 작업 완료·역할 변경을 대신 확정하지 않는다.
4. Project 지침·개인 계획을 전체 원 작업/TH와 정합화하고, #67 리뷰 결과를 반영한 등록용 사본을 완성한다. 실제 Project 교체는 별도 확인한다.
5. 수정에서 파생한 링크·상태·검사·원격 변경을 다시 추적해 전체 Q10을 판정한다. 끝내지 않은 과거 Run 재검증·접근 제한·실환경 확인은 잔여 범위로 명시한다.

B의 근본 후속은 Cloud 금고 본인 확인·독립 보관, lab Valkey 선언/권한 검토, DB/Schema/CA·Route·사용창·live Diff 수락, 단계별 활성화와 동일 조합 시험, ROSA Caller/Backend·출력/SG·지원·Plan·비용·가동창이다. 입력에 의존하지 않는 준비는 병행하고 OCP 철거를 ROSA 준비 전체의 선행조건으로 추가하지 않는다. 기존 TH 81개와 실제 완료 2개는 이번 Source/문서 조사만으로 늘리지 않는다.
