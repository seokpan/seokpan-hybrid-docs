# 2차 저장소 정합성 조사·수정 대장

> 조사 시작·이번 갱신: 2026-10-07 KST  
> 상태: IN PROGRESS — GitOps 병합 인계 반영 완료, 자료 수집 완료, 전체 의미 검토·수정·최종 수렴 미완료  
> 담당 범위: B 정태훈(tjung03)의 구현·문서·검토·인계. A/C/D 작업은 의존성 확인과 해당 담당자 인계로 구분한다.  
> 원 작업: [개인 작업 #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21), [팀 실행 #8](https://github.com/seokpan/seokpan-hybrid-docs/issues/8), [진행 문서 PR #64](https://github.com/seokpan/seokpan-hybrid-docs/pull/64)

## 1. 목적과 판정 원칙

네 저장소의 승인 설계, 실제 코드, 운영 안내, 협업 기록, 그림과 등록용 프로젝트 소스 사이의 불일치를 추적한다. 코드 존재·병합·인계 제출·수신·실제 실행·시험 판정을 구분한다. 이 대장은 조사 범위와 미해결 사항을 보존하며 코드·실험·측정의 원본을 대체하지 않는다. 해당 결과는 원 Issue·PR·Run에 기록하고 WORK_TRACKER와 05에 연결한다.

현재 안내의 잘못된 값·모호한 지시·대화 중계식 표현은 수정한다. 과거 시험의 입력·측정값·실패, 당시 유효했던 설계와 실제 수행 이력은 현재 값으로 덮어쓰지 않는다. 불필요한 도구 관련 서술을 줄이는 작업을 실제 수행자·승인·검증 범위를 다르게 꾸미는 작업으로 확대하지 않는다.

파일 목록이나 검색 결과만으로 전수조사를 완료 처리하지 않는다. 발견→원 근거→직접·후속 영향→필요한 수정→재검증을 반복한다. 접근 가능한 대상의 확인 대기와 발견 사항이 모두 처리되고, 종료 직전 원격 변경 대조에서도 새로운 확인·보완 사항이 없을 때 Q10을 완료한다. 아직 그 상태가 아니다.

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

## 3. 이번 수집 범위와 한계

[읽기 전용 수집 Run](https://github.com/seokpan/seokpan-hybrid-docs/actions/runs/37499657745)은 2026-10-07 01:56:38~01:59:32 KST에 다음 자료를 수집했다. 공개 저장소 Source와 GitHub 협업 기록만 읽었으며 프로젝트 코드를 실행하지 않았다.

| 저장소 | main 파일 | 현재 Branch | 일반 Issue | PR | 일반 댓글 | 리뷰 제출 | 도달 가능한 Commit | Workflow Run 목록 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| App | 392 | 2 | 9 | 6 | 19 | 7 | 91 | 0 |
| Infra | 56 | 3 | 14 | 23 | 100 | 54 | 99 | 26 |
| GitOps | 50 | 2 | 9 | 8 | 40 | 12 | 39 | 60 |
| Docs | 70 | 3 | 15 | 51 | 21 | 0 | 141 | 2 |
| 합계 | 568 | 10 | 47 | 88 | 180 | 73 | 370 | 88 |

Issue 수는 PR을 제외한다. 열린 일반 Issue는 21개, 열린 PR은 Docs #64 한 개다. Inline review comment는 수집 결과 0개다. 모든 PR의 리뷰·변경 파일 목록·Commit, 모든 현재 Branch의 파일 트리, 현재 Branch/열린 PR HEAD의 Check·Status, Milestone·Tag와 Workflow Run 목록을 포함한다. 현재 Branch 전체의 파일 경로는 합산 1,215개이며 중복 제거된 실제 Git Blob 644개를 확보했다.

323개 페이지 응답의 다음 페이지 여부를 보존했고 수집 오류는 0건이다. 각 Issue/PR의 `comments` 수와 수집한 일반 댓글을 번호별로 대조하여 불일치 0건을 확인했다. 저장소별 수집 시작/종료 Branch 목록과 SHA는 일치했다. 순차 조회이므로 네 저장소 전체가 같은 순간의 원자적 Snapshot이라는 뜻은 아니다.

수집 Artifact는 `repository-audit-snapshot-8d5470649e55f32d6441a6105634cf823ce904ab`, ID `11429411389`, ZIP SHA256 `a2eeb0edf313af04f2cec35a45874c1056f13d9783f3c6aabd96550d44a86ef9`다. 다운로드한 ZIP의 해시와 각 Blob의 Git SHA를 다시 대조했다. GitHub 보존 만료는 2026-10-14 01:59:32 KST다. 조사 작업 사본에는 `snapshot-index.json`, `pagination.json`, `excluded-files.json`, 저장소별 `metadata/`, Branch별 `trees/`, `blobs/`를 보존한다. 폰트·개인키·암호화 운영 입력·고위험 자격 패턴은 수집 제외 조건으로 두었고 이번 트리에서 제외된 파일은 0개다. 실제 Secret 공급 경로나 내용은 조사하지 않았다.

**아직 확인하지 않은 범위:** 모든 함수·문장·댓글의 의미 검토, 모든 과거 Run의 job log/artifact 독립 재검증, 과거 삭제된 비도달 Commit/로컬 미커밋 자료, 보호 운영 환경과 실제 설정·자격·Runtime이다. 도달 가능한 Commit 수는 현재 refs의 이력 색인이며 전체 과거 코드 diff의 의미 검토 완료 건수가 아니다. Inline thread 해결 여부는 열린 Docs #64에서 별도 조회하여 0건을 확인했다.

### 3.1 내용 선별 검사

main 파일 568개 중 UTF-8 텍스트 556개에 대상 표기·참조 검사를 적용했다. Python 3.13.5 AST로 Python 파일 243개를 파싱했고 오류는 0건이다. 이는 구문 확인이며 의존성 설치·실제 프로젝트 조합·기능/통합 시험이 아니다. main 텍스트의 Issue/PR 참조 192개를 수집 목록과 대조했으며 번호가 없는 참조는 0개다. URL 전체·fragment·인계 의미가 모두 맞는다는 판정은 아니다.

DR 후보·이전 엔진·대화 메타·Harbor 표기의 검색 후보는 각각 19·11·16·27건이다. 검색 건수를 결함 건수로 사용하지 않는다. 역사 기록·프로토콜 이름·호환 인터페이스·실행 보류 후보와 잘못된 현재 안내를 문맥별로 나눠 검토한다. 파일별 경로·SHA·분류·확인 수준은 작업 사본의 `reports/main-file-inventory.csv`에 보존한다.

## 4. 관측한 Source

| 저장소 | main 전체 SHA | 그 밖의 현재 Branch |
|---|---|---|
| App | `2003fe9d0b27a9b443da26f9fb15cd829aaf8fed` | `reference/app-migration-history-20261002` → `c837120c25c34b88bf6c6ee8e122ff50cbff062d` |
| Infra | `2af2d61f6985ca15dbe8415c84712575f0e92aeb` | `implementation/recovery-local-fixture-20261005` → `29b4a1f01bd555edeebac946cd8ee174da4432ab`; `infra/16-hybrid-route-preparation` → `f50d802f86a84bc887c801e1c3a1f2ab856181fd` |
| GitOps | `fa3cea313e2cb1533d9703082619b085a3de25cc` | `reference/ocp-lab-original` → `259e73b0fac1af40f7bb7b43bd1982410d1df150` |
| Docs | `8a0a6c7f23527995929451775868f9553531ae7c` | 수집 중 #64 `docs/b-registry-vault-followup` → `8d5470649e55f32d6441a6105634cf823ce904ab`; `docs/49-bootstrap-data-iam` → `8acc04be6c626888d384792027c82cfd6ab7a7e6` |

#64의 수집 후 변경은 문서 결과·조사 기록 갱신과 임시 수집 workflow 제거다. 수집 시점 SHA를 이후 최종 HEAD로 표현하지 않는다. 작업 전·종료 전 원격 변경을 다시 확인한다.

## 5. 발견·조치·재검증

### F01 — GitOps 병합 결과와 Docs 인계: 이번 범위 해결

[GitOps PR #17](https://github.com/seokpan/seokpan-hybrid-gitops/pull/17)은 2026-10-06 23:45:46 KST 병합됐다. 검토 HEAD는 `adacf6fffd9d179eef4715e92a3fed721759db55`, 병합 SHA는 `fa3cea313e2cb1533d9703082619b085a3de25cc`다. `b/lab-internal-registry-binding` 브랜치 삭제를 확인했다.

#64의 실행판·학습 안내·Tracker·05에 병합 결과와 실제 실행 대기를 반영했다. [문서 보존 검사 Run](https://github.com/seokpan/seokpan-hybrid-docs/actions/runs/37499302235)의 결과 Commit은 `e3da382398cd76e17cf52fb88353719750938364`다. 기존 체크박스 줄·TH 식별자 수·C의 §8.13 보존, 허용 변경 경로·diff 검사를 통과했다. 내려받은 결과 ZIP SHA256 `7c7f8ff590d02fbc5c2d2b2126b35c36ac900117b3a6d91cd093e75b9e0d6530`도 대조했다. 복사 과정에서 깨졌던 채팅의 금고 예시와 달리 저장소의 Bash 예시는 온전하며 `bash -n`을 통과했다. 실제 복호화 결과는 아니다.

[GitOps 원 작업 댓글](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10#issuecomment-6016940121), [승인 검토 댓글](https://github.com/seokpan/seokpan-hybrid-gitops/pull/17#issuecomment-6018620254), [Docs PR 댓글](https://github.com/seokpan/seokpan-hybrid-docs/pull/64#issuecomment-6018633372)과 #64 본문도 갱신했다. 현재 #64는 Ready/open이며 기존 A/C/D 리뷰 요청을 유지한다. 제출된 사람 리뷰와 inline thread는 각 0건이다. 병합은 별도이며 이 대장에서 완료로 올리지 않는다.

### F02 — C의 신규 main 변경 보존: 이번 결합 해결

[Docs PR #66](https://github.com/seokpan/seokpan-hybrid-docs/pull/66)의 main `8a0a6c7f23527995929451775868f9553531ae7c`를 #64 작업에 결합했다. C의 Data Root·Valkey·Token 기록과 Tracker 변경을 보존했고 05 §8.13의 정확한 블록 일치를 검사했다. 이전 test-merge `840ecbb89e6753bea2d802f28150e06d7b179b40`은 옛 base 조합이므로 최신 main 결합 검증으로 사용하지 않았다. 임시 두 workflow는 최종 파일 트리에서 제거했다.

### F03 — 금고 공급자 보고와 B 본인 확인: 실행 결과 대기 유지

B 공개키 생성·C 전달과 암호문 공급 안내 수신은 완료다. #66에는 C의 A/B 계정별 해독 확인 보고가 추가됐다. 기존 [B 수신 기록](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6016940538)은 B 본인 확인·암호문 해시 대조를 후속으로 남겼다.

두 보고의 확인 주체와 범위를 구분해 네 문서에 연결했다. C 보고를 삭제하지 않고 B 본인 확인·수신·독립 백업을 자동 완료 처리하지 않는다. 새 수행 결과가 들어오면 원 Issue에서 시각·범위·비민감 판정만 확인한다. Cloud Token을 lab Token으로 대체하거나 평문을 수집하지 않는다.

### F04 — 등록 프로젝트 소스: 실제 바이트 대조 완료, 개정·교체 대기

등록된 7개 파일의 실제 바이트에서 Git Blob SHA·SHA256을 계산했다. 다음은 Docs main `8a0a6c7f23527995929451775868f9553531ae7c`와의 대조다.

| 파일 | 등록본 Blob SHA | 저장소 Blob SHA | 판정 |
|---|---|---|---|
| 00_PROJECT_STARTING_POINT.md | `41206700637ac915022a2ef2daaf407e37fb6346` | 동일 | 바이트 일치. 역사적 출발점으로 보존 |
| 01_PROJECT_CHARTER.md | `be43d9c65876f41b8faa53de37cb9f2a8ed2c551` | 동일 | 바이트 일치. 전체 의미 검토 완료와는 별개 |
| 02_TARGET_ARCHITECTURE.md | `63952eec5373d427b3648c5eb3d0094622c40340` | `10a25c94ac062ab8b99616ad73a9a4e63a09e6bb` | 불일치 |
| 03_DETAILED_DESIGN.md | `d09d638ff754d713cbb00b3dcb911dcc0c5dfb00` | `fc54c591f727559c40d5da8452c8ce854257eeb5` | 불일치 |
| 04_IMPLEMENTATION_READINESS.md | `cff6f9f752917f97f514ab4c3c408e1952581ef0` | `b0f2c2eaf6d6580f49e324cbe4df3d64937e1f38` | 불일치 |
| PROJECT_INSTRUCTIONS.md | `08840b61ffa4ccdd4a49cb4e0ab00df9395fd820` | 同名 정본 없음 | Project 전용 지침. 10/5 이후 설계·기록 방식과 대조 필요 |
| TJUNG03_IMPLEMENTATION_STUDY_AND_PRESENTATION_PLAN.md | `d156f579d3c03e9f6dd343e551931643aaa6766f` | 同名 정본 없음 | Project 개인 보조 소스. 실행판·Docs #21·현재 원 작업과 대조 필요 |

현재 Branch 트리에서 마지막 두 파일의 동명 저장소 정본은 확인되지 않았다. 무관한 파일을 대신 정본으로 취급하지 않는다. 저장소 자체에도 F05/F07/F08이 남아 있으므로 현재 파일을 그대로 재등록하면 충분하다고 판단하지 않는다. 필요한 수정·검증 후 등록용 사본과 교체 목록을 제공하며 실제 Project 교체는 별도 확인한다.

### F05 — 저장소의 DR 현재/과거 경계: 수정 대기

[03 도입부와 §3-G.7·§3-I.14.5](https://github.com/seokpan/seokpan-hybrid-docs/blob/8a0a6c7f23527995929451775868f9553531ae7c/design/03_DETAILED_DESIGN.md)에 `변경 후보`, `main에 병합되면`, `그 전 공식 main 기준은30분/90분/1시간`이 현재 설명으로 남아 있다. 04 도입부에도 같은 조건이 있고 02 도입부는 10/3 재검토를 현재처럼 설명한다. [DR PR #30](https://github.com/seokpan/seokpan-hybrid-docs/pull/30)의 병합 상태·현재 요구와 대조하는 대상이다.

현재 설계 요구는 RTO 10분·영속 DB RPO 30분·DB 운영 중 백업 계획 주기 15분이다. 이전 30분/90분/1시간과 철회된 후보는 당시 이력으로 보존한다. 주기와 실제 RPO 보장, 부분 예행과 전체 T18 달성을 합치지 않는다. 설계 도입부·본문·상태표·Runbook·주기/비용 설명·manifest·등록본까지 수정 영향을 연결한다. #64의 병합 인계 보완만으로 이 항목을 해결 처리하지 않는다.

### F06 — 독립적인 현재 안내와 기록 주체: 일부 조치, 전면 검토 대기

실행판·가이드·팀 안내와 B 명의 Issue/PR/댓글에 `작성 요청`, `사용자 확인으로`, `사용자가 제공한`, `B/AI`, 불필요한 도구 지원 표기와 여러 시점의 `지금/현재`가 섞여 있다. 사용자 서비스 요청을 뜻하는 정상 문장과 문서 작성 과정의 메타 문장을 구분한다.

이번 #64의 새 인계 문구와 위 F01의 댓글 세 곳은 목적·결과·근거·미실행 범위로 정리했다. 나머지 본문·역사 기록·참조는 아직 전면 정리하지 않았다. 활성 안내는 현재 행동으로 독립적으로 읽히게 하고 과거 기록은 시점·원 Commit/Issue를 명확히 한다. 실제 합성 시험의 수행자, 승인자, 관측 환경, 실패·측정값을 지우거나 사람의 직접 수행으로 바꾸지 않는다.

### F07 — Diagram manifest 재생성의 메타데이터 유실: 격리 재현 완료, 수정 대기

[검증 스크립트](https://github.com/seokpan/seokpan-hybrid-docs/blob/8a0a6c7f23527995929451775868f9553531ae7c/architecture/tools/verify_diagrams.py)는 새 result를 만들면서 기존 `followup_review`, `followup_review_history`, `data_engine_followup`, `check_scope_history`, `latest_check_scope`를 저장하지 않는다. DR·Valkey 정합 내용을 수작업으로 다시 넣었어도 다음 재생성에서 사라질 수 있다.

원문 작업 사본을 별도 디렉터리에 복사하고, 기존 SVG와 내장 폰트로 layout 입력을 재구성해 스크립트를 실행했다. 종료 코드 0과 SVG/XML 12·PNG decode 12·폰트 글리프 12·declared geometry 12·Subnet 9·원문 식별 5의 검사 출력이 나온 뒤 위 다섯 키가 실제 출력에서 사라졌다. 저장소 원본은 이 재현으로 변경하지 않았다.

이 재현은 manifest 보존 회귀를 확인한 것이다. 재구성한 layout을 썼으므로 원래 생성기 layout의 독립 시각 검증이나 전체 그림 의미 검토를 완료한 결과로 사용하지 않는다. 다음 수정은 정본의 최신 설계 메타와 과거 검토/검사 기록을 구분해 보존하고 누락 재발을 막는 회귀 검사를 포함해야 한다.

### F08 — 설계와 manifest의 Data Source 상태: 수정 대기

실제 [foundation/data_redis.tf](https://github.com/seokpan/seokpan-hybrid-infra/blob/2af2d61f6985ca15dbe8415c84712575f0e92aeb/terraform/foundation/data_redis.tf)는 `engine = "valkey"`다. 그러나 02 §10, 03 §3-D.9.7, 04 §1과 두 manifest의 `data_engine_followup`에는 현재 Source가 Redis OSS 7.1이며 C Root PR 전환 대기라고 남아 있다. 설계 선택과 Source 병합은 완료된 범위로 연결하고 실제 생성·호환성 시험은 별도로 남겨야 한다.

`Redis`라는 단어를 전부 교체하지 않는다. `SEOKPAN_REDIS_*`, `backend-redis-*`, Terraform `redis_*`, 기존 API/프로토콜 이름과 과거 Redis 시험은 각자의 의미를 유지한다. App Pool 후보·상한/종료 중 연결 예산도 엔진 전환만으로 채택·검증된 것으로 올리지 않는다.

### F09 — 그림과 실제 실행 보류: 구분하여 추가 검토

12개 SVG의 표시 문구를 추출해 대조했다. 그림 01/02/04/12는 이미 Valkey 7.2를 표시하고 그림 10은 RTO 10분·영속 DB RPO 30분·운영 중 15분 Backup을 표시한다. Generic Redis 계층명과 1차 자산은 남아 있다. 표시가 맞는 SVG/PNG를 일괄 다시 만드는 것이 기본 조치는 아니다. F07의 생성·출처 경로와 README/계획/검토 기록의 날짜·현재성, 그림별 화살표·가독성·실제 배치 여부는 별도 확인한다.

GitOps의 Recovery `redis.yaml`은 `redis-server`, TCP Probe, 입력 대기 Image/PVC와 replicas 0을 유지한다. 선택된 Valkey Image·실행 파일·TLS/AUTH Probe·저장 정책을 실제 수락하기 전의 보류 인터페이스이며 Runtime 완료가 아니다. 기존 후속 구현에 연결할 대상이지 임의 Image나 새 Storage 정책으로 즉시 채워 넣을 사유가 아니다. lab에는 별도 Valkey 서버 선언이 아직 없고 작성 제안·수락을 구분한다.

## 6. 조사 반복과 현재 중단점

| 반복 | 확인·조치 | 새로 연결된 확인 대상 | 판정 |
|---|---|---|---|
| 1 | #64 실제 HEAD·#17 병합·#66 main 변경 대조 | 공유 네 문서 보존 결합·현재 대기 갱신 | F01/F02 조치 및 보존 검사 완료 |
| 2 | 네 저장소 전체 자료 수집·페이지/댓글 수·Blob 검증 | DR 현재/과거, Data Source 상태, 기록 주체, 등록본 차이 | 수집 완료, 의미 검토는 진행 중 |
| 3 | 생성기·manifest·12 SVG 표시·Source 연결 대조 | 정상 종료하면서 최신 메타 5개 유실 | F07 격리 재현. 수정·재발 검사 필요 |
| 4 | 등록본 실제 해시·Python 구문·Issue/PR 참조 번호 대조 | 현재 main의 설계 자체 보완 후 등록본을 만들어야 함 | 전체 수렴 아님. Q02~Q10/Q12 미완료 유지 |

Q01의 반영과 현재 조사 기록 보존은 마쳤다. 전체 재귀 검토는 끝내지 않았다. 새로운 확인·수정 대상이 있으므로 추가 보완 0건 또는 전체 정합성 PASS라고 선언하지 않는다.

## 7. 다음 작업 순서와 B 실행 연결

먼저 다음 작업 시작 시 #64의 실제 병합·브랜치 상태를 조회한다. 별도 채팅 완료 통보를 기다리지 않는다. 그다음 F05/F08의 현재 설계 설명과 F07의 생성기 보존 결함을 한정된 변경으로 처리하고, source-manifest·diagram-manifest·그림/원문 동일성·회귀 검사를 대조한다. 이때 이미 맞는 PNG/SVG와 역사적 Run은 보존한다.

이어 Q02~Q04/Q08의 파일·주석·Issue/PR/댓글·인계 의존을 전면 검토하고, 필요한 수정만 B 영역에 적용한다. 다른 담당자의 열린 작업·실제 공급·실행 결과는 해당 원 작업에 인계한다. 등록용 02~04·지침·개인 계획은 정본 보완 뒤 제공한다. 마지막에는 수정에서 파생한 링크·상태·검사·원격 변경을 다시 추적해 Q10을 판정한다.

B의 근본 후속은 Cloud 금고 본인 확인·독립 보관, lab Valkey 선언/권한 검토, DB/Schema/CA·Route·사용창·live Diff 수락, 단계별 활성화와 동일 조합 시험, ROSA Caller/Backend·출력/SG·지원·Plan·비용·가동창이다. 입력에 의존하지 않는 준비는 병행하고 OCP 철거를 ROSA 준비 전체의 선행조건으로 추가하지 않는다. 기존 TH 81개와 실제 완료 2개는 이번 Source/문서 조사만으로 늘리지 않는다.
