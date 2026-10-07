# 2차 저장소 정합성 조사·수정 대장

> **현재 인계:** 후속 PR 병합·Project 등록·jth 해독 보고·lab Valkey Source 및 Backend 검사의 최신 결과는 [§9](#b-runtime-input-followup-20261007)를 따른다. 아래 §1~8은 이전 조사 체크포인트이며 Q 체크 상태는 유지한다.

> 개정: 2026-10-07 KST  
> 상태: IN PROGRESS — 두 중단분의 게시·산출물 복원, PR 설명/리뷰 요청 정정, fixture 요약 후속 보완 및 등록용 소스 제공. 전체 코드/이력 의미 검토와 Q10 수렴은 미완료  
> 담당: B 정태훈(tjung03). 다른 담당자의 실제 실행·승인·수신은 해당 원 기록으로 구분한다.  
> 원 작업: [개인 #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21), [팀 #8](https://github.com/seokpan/seokpan-hybrid-docs/issues/8)

## 1. 판정 기준과 보존 이력

Source 존재·리뷰·병합·인계 제출·수신·실제 실행·시험 판정을 구분한다. 자료 수집과 검색만으로 전수 의미 검토를 완료하지 않는다. 발견→원 근거→직접/후속 영향→필요한 수정→재검증을 반복하며, 접근 가능한 전체 대상의 미검토·미해결이 남아 있으면 Q10을 완료하지 않는다.

이 문서는 현재 상태와 다음 확인 지점을 정리한다. [초기 조사 F01~F10](https://github.com/seokpan/seokpan-hybrid-docs/blob/d2371a44f4c9b35cf8082991ec9700ccea2ec524/execution/REPOSITORY_CONSISTENCY_AUDIT.md)과 [두 중단분의 이전 체크포인트 전문](https://github.com/seokpan/seokpan-hybrid-docs/blob/3354bfff616685459d1586238239095109ebf64f/execution/REPOSITORY_CONSISTENCY_AUDIT.md)은 고정 Commit에서 보존한다. 과거 Evidence·측정·실행자·승인을 최신 값으로 소급 변경하지 않는다. TH 81개와 실제 완료 2개는 이 조사 때문에 변경하지 않는다.

이번 종료 단위는 **중단 작업의 실제 게시 확인과 남은 제출/검증/전달 마무리**다. 범위 안의 새 불일치는 수정했으나, 전체 코드·과거 이력의 의미 검토가 끝났다는 판정은 아니다. 다음 작업은 §8의 미완료 단위에서 이어간다.

## 2. 고정 체크리스트

Q06은 이전에 완료한 현재 12장·생성/출처 경로의 대조와 필요한 그림04 수정·시각 검증이다. 이번 재개에서는 해시·XML/PNG·manifest를 재검증했으며 새 전체 시각 검토를 했다고 기록하지 않는다. Q07은 7개 비교와 개정본 제공이며 실제 Project 첨부 교체는 아니다. Q08은 수집한 B 명의 공개 기록과 현재 문서의 작성 과정 메타 정리 범위다. Q09는 발견한 수정의 B 범위 처리·보존·원 작업 인계이며 팀원 리뷰 수신을 대신하지 않는다. 새 발견이 생기면 영향 항목을 다시 진행 상태로 관리한다.

- [x] Q01 — GitOps #17의 병합·브랜치 삭제를 확인하고, Docs #64의 실행판·학습 안내·WORK_TRACKER·05와 PR 기록에 반영한 뒤 변경·리뷰 상태를 검증한다.
- [ ] Q02 — 네 저장소의 전체 문서·구현 코드·설정·시험·주석·관련 파일을 목록화하고, 활성 원본·재사용 원본·과거 이력·생성물을 구분하여 내용을 조사한다.
- [ ] Q03 — 네 저장소의 열린/닫힌 Issue·PR·본문·댓글·리뷰·검사와 모든 현재 Branch·Commit·변경 파일을 추적하고, 페이지 누락·접근 제한·삭제된 이력의 확인 범위를 기록한다.
- [ ] Q04 — 상위/하위 작업·담당자·입력·산출물·원 코드·시험·인계의 직접 의존과 후속 영향을 연결하여 순환 대기·오래된 완료/대기·누락을 확인한다.
- [ ] Q05 — Valkey 전환, OCP–Harbor 연결 제약과 내부 Registry 소비, DR RTO 10분·영속 DB RPO 30분·백업 계획 주기 15분을 설계·코드·가이드·시험·비용·주석에 걸쳐 대조하고 필요한 불일치를 수정한다.
- [x] Q06 — 그림 생성 원본·manifest·출처 기록·SVG·PNG와 이를 참조하는 문서를 대조하고, 영향을 받은 생성물만 재생성·시각 검증한다.
- [x] Q07 — 등록된 프로젝트 소스 7개를 저장소 정본과 내용·버전·해시로 대조하고, 필요한 등록용 개정본과 교체 대상을 제공한다. 실제 프로젝트 소스 교체는 별도로 확인한다.
- [x] Q08 — B 명의 문서·Issue·PR·댓글의 대화 의존·자기 요청 중계·불필요한 AI 작업 홍보를 목적·변경·근거·결과·한계 중심으로 정리하고, 실제 수행·승인·시험 이력은 보존한다.
- [x] Q09 — 실제 필요한 수정만 B 범위에서 처리하고, 다른 담당자의 변경을 보존하며 해당 담당자의 검토·입력·수신이 필요한 사항을 원 작업에 인계한다.
- [ ] Q10 — 발견→직접/후속 영향→수정→재검증을 반복하고, 종료 직전 원격 변경을 다시 대조하여 확인 가능한 전체 범위에서 새로운 확인·보완 사항이 없을 때 최종 수렴을 판정한다.
- [x] Q11 — 조사 대상·관측 SHA·근거·발견·조치·검증·미확인·다음 순서를 이 대장과 원 작업에 보존하여 다음 작업 공간에서도 연속성을 유지한다.
- [x] Q12 — 조사 결과를 B의 기존 TH 81개·실제 완료 상태·추가 작업·직접 입력·병행 작업·실행 Gate와 연결하고, #64 병합 여부는 별도 완료 통보를 전제로 하지 않고 GitHub에서 확인한다.

## 3. 병합·수정 PR과 Source

Docs #64는 `94d5955612f589f40343360709513568bc5f0dc0`, #67은 `d2371a44f4c9b35cf8082991ec9700ccea2ec524`에 병합됐다. 작업 브랜치 삭제 이력을 유지하며 병합 상태를 이번 재개에서 다시 조회했다. GitOps #17은 `fa3cea313e2cb1533d9703082619b085a3de25cc`에 병합됐다. 이 상태를 리뷰 대기로 되돌리지 않는다.

| 후속 PR | 현재 검토 Source 및 범위 | 이번 조치 |
|---|---|---|
| [Docs #68](https://github.com/seokpan/seokpan-hybrid-docs/pull/68) | 등록 설계 내용 `92b72b7fed298da04e1c0eef1ae60d32e50bbffe`; 재개 HEAD `3354bfff616685459d1586238239095109ebf64f`. 현재 대장 갱신은 그 이후 Commit | 기존 내용·그림 변경을 반복하지 않음. 실제 제공 ZIP v3·후속 검증·미완료 범위 연결. C/D 문서 리뷰 요청 보완 |
| [Infra #38](https://github.com/seokpan/seokpan-hybrid-infra/pull/38) | 최신 `7795028642dadb7c6d297a7404c701bcd98b6130`; 두 도구·두 README·테스트 5개 파일 | 생성 요약의 설계 재확인 요구를 채택된 범위로 정정하고 회귀 1개 추가. 총 9개 PASS. C/D 리뷰 요청 보완 |
| [App #16](https://github.com/seokpan/seokpan-hybrid-app/pull/16) | `708ea3fafec95f68319fea7b7b966ecf97e4689c`; `MIGRATION_SEED.md`·연결 안내 2개 | PR 본문의 한 파일/옛 HEAD 표시를 실제 Patch와 맞춤. 코드·Lock·Image 변경 없음, C/D 요청 유지 |
| [GitOps #18](https://github.com/seokpan/seokpan-hybrid-gitops/pull/18) | `f956346184a3eff9fb558d64324c8414a9ee8f0b`; apps 안내·인계 문서 3개 | 이전 게시 `062f17b...`와 파일 차이 0개 확인 후 본문 HEAD 정정. Manifest·renderer·기동 보류 유지, C/D 요청 유지 |

각 PR의 사람 승인·병합은 아직 완료로 기록하지 않는다. 리뷰 요청은 실제 리뷰 수락이 아니다. 다음 작업은 별도 채팅 통보를 기다리지 않고 HEAD·리뷰·검사·병합·브랜치를 재조회한다. Runtime 원 이슈는 문서 PR 병합만으로 닫지 않는다.

## 4. 자료 수집·검토 수준

[재개 Snapshot Run 37538088477](https://github.com/seokpan/seokpan-hybrid-docs/actions/runs/37538088477)은 2026-10-07 07:03:20~07:04:16 KST에 공개 Source·협업 기록을 수집했다. ZIP SHA256 `e2afd5ebcdbcefc6fed5468a2258590146bb5cfbf51d8d55557c29097a7f9665`, Artifact ID `11447536059`다. 이번에도 ZIP과 **669개 Git Blob**을 재검증했다.

수집 시점의 고정 범위는 main 파일 570개, Branch 11개, 일반 Issue 47개, PR 91개, 일반 댓글 182개, 제출 리뷰 73개, 도달 가능한 Commit 393개, Workflow Run 목록 96개다. 페이지 응답 334개, 수집 오류·제외 0건, 댓글 수 대조 불일치 0건과 저장소별 시작/종료 Branch SHA 일치는 이전 수집 검증이다. 이후 PR/Commit/Run을 이 표본에 소급 포함하지 않는다. 순차 수집을 네 저장소의 원자적 Snapshot으로 표현하지 않는다.

앞선 Run 37537826727의 metadata URL 끝 슬래시 오류는 실패 이력이며 위 성공 수집과 구분한다. 임시 수집·적용 workflow와 입력은 각 작업 완료 뒤 최종 트리에서 제거한다. 이번 실제 fixture 후속 검증의 임시 workflow도 제거됐다.

이전 확인 수준은 현재 문서의 상대 파일 경로 475개·누락 후보 0개, 수집한 B 본문/댓글 137개와 제출 리뷰 14개의 작성 과정 메타 선별·문맥 검토다. 남은 표현 중 서비스 사용자·손실 허용에 관한 정상 설명과 실제 과거 수행자 근거는 보존한다. 숫자·AST·파일/댓글 수를 모든 실행 분기와 외부 URL/fragment의 의미 검토 완료로 사용하지 않는다.

**미완료:** 현재 코드 전체의 함수/설정/시험 분기, 현재 refs에서 도달 가능한 모든 과거 Commit별 diff, 과거 CI job log/artifact 전체의 독립 의미 검증, 외부 참조·anchor의 전면 대조. 비도달 삭제 이력·개인 미커밋 자료·보호 운영 입력·실환경은 공개 조회와 별도다.

### 4.1 이번 App 연결 경계의 한정 검토

App main `2003fe9d0b27a9b443da26f9fb15cd829aaf8fed`의 다음 Source를 전문 대조했다. 이것은 현재 연결/설정 경계 검토이며 App 전체 게임 로직·시간·Lua·종료 경쟁 검토 완료가 아니다.

| 파일 | 확인 내용 | 남은 실제 확인 |
|---|---|---|
| `backend/src/seokpan/connection_contract.py` | Profile별 정확한 Host/Port·DB/Runtime 사용자, Redis URL의 별도 AUTH·CA·TLS 경계 | 실제 대상·자격·체인·서버 거부/성공 |
| `backend/src/seokpan/connection_settings.py` 및 `settings.py` | 환경변수 소비·Profile·오류/민감값 표현과 Pool 크기 변수 부재 | 승인 값 주입·Pod/프로세스 설정 |
| `backend/src/seokpan/persistence/mariadb/connection.py` 및 `settings.py` | 두 Runtime Engine, 전용 Migration의 NullPool, 명시 CA·PrePing·오류/close 경로 | 연결 상한·재접속·장시간 Pool·종료 중 연결·세션 시간대 |
| `backend/src/seokpan/persistence/redis/connection.py` | 비legacy rediss·별도 AUTH·명시 CA, Client/Pool 종료 경로 | 고정 Driver와 실제 Valkey의 TLS/AUTH·RESP/Lua·업무·Failover |

`backend/tests/persistence/test_hybrid_connections.py`는 연결 인자/음성 검사 일부만 대조했으며 전체 전문·고정 의존성의 새 Pytest 실행 완료로 기록하지 않는다. 현재 `pool_size`/`max_overflow`를 임의 환경변수로 설정하기만 해도 App이 소비한다는 근거는 없다. Pool 후보 3+2/60은 C/B 합의·Source 반영·Build/Digest·Runtime 검증 전에 채택하지 않는다.

## 5. 수정·회귀 검증 결과

### 5.1 두 중단분에서 이미 게시된 변경

현재 실행판·학습 안내·05·WORK_TRACKER의 완료/대기·과거 현재형 안내와 B 명의 작성 과정 메타를 정리했다. C의 05 §8.9~8.13과 TH·체크·기존 URL·Source SHA·실행 범위를 보존했다. GitOps 인계는 내부 Registry 소비·Valkey/CA ConfigMap·독립 작업을 구분하며 App 안내도 같은 계약을 따른다.

그림04는 GitOps Source와 FE `/`→8080, API `/api/v1`·WSS `/ws/v1`→Backend8000으로 맞췄다. builder/SVG/PNG/manifest를 함께 수정했고 다른 11쌍은 보존했다. 이전 12장 시각 검토와 전체 layout 검사는 해당 Run에 연결한다. 이번 문서 바이트 복원·무결성 재검사를 새 그림 생성·시각 검토라고 표현하지 않는다.

| 이전 Run | 범위 |
|---|---|
| Docs [37520034315](https://github.com/seokpan/seokpan-hybrid-docs/actions/runs/37520034315) | 내용/그림04·전체 layout 검증. 15개 출력 복원 근거 |
| Infra [37519877827](https://github.com/seokpan/seokpan-hybrid-infra/actions/runs/37519877827) | 실행자/Evidence-only 초기 8개 회귀·5파일 |
| App [37539590807](https://github.com/seokpan/seokpan-hybrid-app/actions/runs/37539590807), GitOps [37539797118](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37539797118) | 연결/인계 MD·B 본문 변경 전후 보존·재조회 |
| Infra [37540487457](https://github.com/seokpan/seokpan-hybrid-infra/actions/runs/37540487457), Docs [37540621286](https://github.com/seokpan/seokpan-hybrid-docs/actions/runs/37540621286) | B 본문·개인 안내 정리와 보존/검사 |
| Docs [37541229258](https://github.com/seokpan/seokpan-hybrid-docs/actions/runs/37541229258) | MD8개·manifest2개, C 구획/체크/URL/SHA 보존·회귀13+16 |
| Docs [37542628820](https://github.com/seokpan/seokpan-hybrid-docs/actions/runs/37542628820) | 마지막 승인 표현3개·출처 식별·회귀13·멱등성 |

B 본문 추가 정리의 App 37541545817, Infra 37541585311, GitOps 37541638065, Docs 37541690283은 이전 전문에 보존한다. GitOps Native 37541642040의 validate success는 trigger `1e6152a9d4beb652f5b4fe4d3fd6053a3127cfd1`의 결과이며 최종 HEAD의 새 CI로 바꾸지 않는다.

### 5.2 이번 재개에서 발견·해결한 후속 결함

Infra fixture JSON은 과거 개별 결과 HTTP 화면을 이미 알려진 한계로 분류했지만, 생성 Markdown 요약은 B의 설계 재확인을 요구했다. 동일 실행에서 두 산출물이 서로 다른 범위를 설명하는 결함이다. `tools/recovery_business_fixture/run.py`의 요약을 채택된 Docs #30·03 §3-I.14.5에 연결하고 `tools/test_fixture_evidence_identity.py`에 JSON/Markdown 범위 일치 회귀를 추가했다.

[Run 37549603515](https://github.com/seokpan/seokpan-hybrid-infra/actions/runs/37549603515)은 **9개 회귀 PASS**다. 변경 전후 파일 해시·허용 경로 두 개·기존 HEAD·게시 직전 Branch를 검증하고 기존 작업 브랜치에만 게시했다. trigger `fbc92c6a838cc12622e2092added433a0ea74b64`와 게시 `7795028642dadb7c6d297a7404c701bcd98b6130`는 구분한다. 임시 workflow는 최종 트리에서 제거했다.

Artifact `11451659295`의 ZIP SHA256은 `52d128b079b148b43ab823fef3a3d24af8ee84bb69181760ec0ed916ef66480f`다. 내려받아 CRC·해시·로그·게시 SHA와 두 출력 파일의 로컬 검토본 일치를 확인했다. 최신 run.py SHA256은 `f31844855967de5ab38156f10a1272a9b98cb94e24d5b7187da8cc182226a595`, 테스트는 `780d018bbc736eed5c372547e2a4fe8215b7bcc19c418caa77405b998dda6667`다.

새 테스트의 최초 로컬 실패는 RTO의 중첩 JSON 위치를 잘못 지정한 검사 오류였다. `recovery.rto_seconds`로 바로잡은 뒤 로컬/원격 9개가 통과했다. 실패 로그를 보존하며 이를 제품 결함이나 통과 횟수로 계산하지 않는다. 실제 DB·Backend·TLS 서버 기동·전체 T18은 실행하지 않았다.

App #16 본문의 파일 수와 HEAD, GitOps #18의 HEAD도 실제 PR Patch·Commit과 맞췄다. Docs #68·Infra #38은 실제 리뷰 요청이 비어 있었으므로 C/D에게 요청했다. 요청 본문이 있다고 실제 리뷰 요청·승인이 완료됐다고 판단하지 않는다.

### 5.3 이번 재실행한 검사

- Docs 검증기 회귀13개, 복구 수치 도구16개 PASS.
- 현재 설계5개·SVG/XML12개·PNG decode12개·글리프12개·Subnet9개 무결성 PASS. 이번 `integrity-only` geometry는 0/생략이다.
- Infra 실행자 초기8개를 복원 확인한 뒤 수정된 최종9개 PASS. 이전8개+최종9개를 별개의17개 Case로 합산하지 않는다.
- 재개 Snapshot ZIP/669Blob, Docs 안내·Source·최종 문구 Artifact의 SHA256·출력 파일 대조.
- 금고 복호화·클러스터 Sync·Valkey 호환성·전체 T18·ROSA Plan/Cost는 이번 검사에 포함하지 않는다.

## 6. Project 소스 7개 — 실제 제공본 v3

이전 대장에 적힌 v2 ZIP은 이번 전달 경로에서 파일을 확보하지 못했다. 전달 완료로 추정하지 않고 검증된 저장소 파일과 등록된 지침/개인 계획 원본으로 **실제 파일 v3**를 다시 구성했다. v2와 바이트가 같다고 주장하지 않는다.

파일명: `Seokpan_Project_Sources_7files_Resume_2026-10-07_v3.zip`  
ZIP SHA256: `d0a42dbfba483f3566d54410010fd95b14d1a2428335f9ee55a29563d546c4f5`

원래 이름의 MD7개, `REGISTRATION_MANIFEST.json`, `REPLACE_GUIDE.md`를 포함한다. ZIP CRC와 포함된 일곱 파일 해시를 검증했다. 개인키·비밀값·폰트는 포함하지 않는다.

| 대상 | 내용·교체 범위 |
|---|---|
| 00·01 | 기존 등록본과 바이트 동일. 역사·목적/상위 기준 보존, 재등록 불필요 |
| 02·03·04 | Docs #68 내용 Source `92b72b7fed298da04e1c0eef1ae60d32e50bbffe`와 같은 사본. 재개 HEAD3354의 내용과 동일하며 이번 대장 갱신은 설계 파일을 바꾸지 않음 |
| PROJECT_INSTRUCTIONS | 기존 절45개·체크 상태57개 보존, 활성 Valkey/Registry·DR 기준·독립 기록·재개/직접 의존을 정합화하고 §38 추가 |
| 개인 구현·학습·발표 계획 | 기존 절18개·체크 상태26개 보존, 현재 첫 작업과 과거 현황을 구분하고 §19에 병행·인계·새 fixture·남은 감사 연결 |

지침·개인 계획은 동명 GitHub 정본이 없는 Project 전용 보조 소스다. 저장소 자동 동기화 파일로 취급하지 않는다. 이번 생성/제공과 실제 Project 첨부 교체는 별도다. 02·03·04의 변경 PR은 아직 리뷰/병합 전이므로 리뷰에서 내용이 바뀌면 실제 병합본과 다시 대조한다. 구본과 신본을 동시에 활성 기준으로 두지 않는다.

## 7. B 작업의 직접 의존과 병행

| 경로 | B의 다음 행동 | 직접 입력·원 작업 |
|---|---|---|
| Cloud AUTH | jth 계정에서 값 출력 없는 복호화·암호문 해시 대조, C 회신·독립 키 보관/복구 확인 | [Infra #19](https://github.com/seokpan/seokpan-hybrid-infra/issues/19). 공개키 전달·공급 보고 완료. 본인 실행 결과는 미수신 |
| lab | D 선언 수락/PR → C Data·B Source/AppProject/UID/Probe·자원 검토 → 실제 Service/Ready·DB/Schema·CA/Secret·Route·권한·사용창·live Diff 수락 → 필요한 단일 Migration·BE·FE·같은 조합 Run | [GitOps #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10)·[#6](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6). 기존 DB/Redis/PVC 보호, replicas0/suspend 유지 |
| ROSA | 본인 clone·도구·Caller/Backend·지원·사양·기간·가용성·비용 입력 | [Infra #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25). 실제 Plan에는 A 제한 출력/공통 prerequisite·C Data SG2, 생성에는 전체 Plan/Cost/실행창 수락 |
| Pool/새 Image | 실제 연결 상한·종료 중 연결·예약/부하 합의 → 필요한 App 코드 → D Build/Digest | [App #1](https://github.com/seokpan/seokpan-hybrid-app/issues/1)·[#4](https://github.com/seokpan/seokpan-hybrid-app/issues/4). 3+2/60은 미채택 시나리오 |
| Recovery | Valkey 승인 Image·binary·TLS/AUTH Probe·Storage/UID를 선언/renderer/검사와 함께 개정 | GitOps #10·Infra #17. 기존 held redis-server/TCP Probe·미확정 Digest/PVC를 실제 Valkey 수락으로 사용하지 않음 |

Cloud 금고 확인은 lab 검토의 선행조건이 아니다. OCP 철거·팀원 전체 업무·전체 Recovery 종료도 ROSA 준비의 일괄 선행조건이 아니다. Cost PARTIAL·실제 가용시간 미확인, Freeze milestone10/18 vs 승인10/16의 후속은 유지한다. 이번 변경은 실제 환경에 접속하거나 값을 공급한 결과가 아니다.

## 8. 다음 작업 단위와 전체 종료 조건

새 Snapshot을 처음부터 반복 생성하기보다 보존된 Snapshot과 네 PR의 실제 변경분부터 확인한다. 이번처럼 산출물의 JSON/요약·PR 본문·테스트·코드가 서로 일치하는지도 추적한다.

| 순서 | 남은 검토 단위 | 남길 결과 |
|---|---|---|
| S1 | App `test_hybrid_connections.py` 나머지, DB 시간/Pool·서비스 생성/종료, 공유 상태/Lua·최종화 분기 | 파일/함수별 확인 수준·기존 검사 대응·결함/미확인. §4.1을 전체 App 완료로 확대하지 않음 |
| S2 | GitOps Recovery `redis.yaml`/`redis.conf`·renderer·검사, CI Writer/Promotion 입력/범위·실행 보류 | 실제 담당 인계와 코드의 직접 의존. 승인되지 않은 Image/저장/Pool 값은 입력 대기로 유지 |
| S3 | 수집한 Issue/PR/댓글·도달 가능 Commit diff·CI log/artifact·참조 anchor/외부 자료 | 조회/검토/미확인/접근 제한·유효한 과거 근거를 항목별로 기록 |
| S4 | S1~S3에서 발생한 수정·회귀·원 작업/Tracker/05·등록본 영향, 종료 직전 원격 변경 | 확인 가능한 미검토·미해결이 없어질 때만 Q02/03/04/05 및 Q10 전체 수렴 판정 |

현재 문서·기록 주체·그림·등록용 파일의 지정 수정/제공과 두 중단분의 게시 정리는 끝냈다. 전체 코드·과거 이력의 의미 검토, 팀원 리뷰/병합, 본인·팀의 실제 Runtime 입력은 남아 있다. 이 잔여 범위를 숨기거나 조사 체크를 구현·시험 완료로 전환하지 않는다.


<a id="b-runtime-input-followup-20261007"></a>

## 9. 실행 입력 수신·Backend 고정 검사·lab 선언 재검토 — 2026-10-07

### 9.1 현재 상태와 기존 체크포인트의 관계

§1~8의 중단 재개·미병합/등록 대기는 그 기록 시점의 이력이다. Docs #68=fff5ac222243a231e5473f4ab39f87aa6cc10f6f, Infra #38=0f47617816b74365f5911ba2e273013ae82d6612, App #16=bdaa9dfa0a09e5d8efb1714ccf62860315b1346e, GitOps #18=12d78ac547729f0e314abfb2ac6238c95b1f3bd7의 실제 병합과 각 작업 브랜치 삭제를 확인했다. Project7개 v3 등록·00~04 병합본 일치는 [Docs21 원 확인](https://github.com/seokpan/seokpan-hybrid-docs/issues/21#issuecomment-6028672058)을 따른다. 같은 파일을 다시 등록하지 않는다.

새 [GitOps #19](https://github.com/seokpan/seokpan-hybrid-gitops/pull/19)는 검토 HEAD2215aff8d4e49bcde0d5e66ce6a0769870a76605에 B가 [승인 리뷰5436531268](https://github.com/seokpan/seokpan-hybrid-gitops/pull/19#pullrequestreview-5436531268)를 남긴 뒤 main de130af839626c9d0a030580693a4060c41c9abd에 병합됐다. D의 초안 작성 수락·선언 공급·B 기존 변경 요청 대기는 해소됐고 C Data 수락·실제 Sync/Ready/업무는 별도다. 이 기록의 작업에서는 PR 병합이나 실제 클러스터 명령을 대신 실행하지 않았다.

### 9.2 lab 검토·검증과 활성화 분리

기존 B 변경 요청은 제한 AppProject의 apps/StatefulSet 누락과 Sync 뒤 되돌림 설명이다. 최신 Source/테스트는 Kind 하나만 추가하고 Namespace/목적지·Cluster 자원·Secret/PVC/Job 경계를 유지한다. Kind 허용은 이름 lab-redis 한 개만 허용하는 정책이 아니다. Sync 후0Replica 객체도 남으므로 Git revert만으로 자동 삭제된다고 가정하지 않는다.

TLS-only·AUTH include와 두 CLI 환경변수·0440·임의 UID·읽기전용 Root·emptyDir·noeviction·startup TCP/readiness PONG/liveness 없음·내부 Registry Digest를 대조했다. SNI/PONG을 Backend의 실제 Hostname 검증으로 확대하지 않는다.128Mi 요청/256Mi 제한/192mb는 최초 후보이며 OOM 안전의 측정값이 아니다.

[Run37556270961](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37556270961)의 정확 HEAD 로그에서40개 PASS·Source 불변·8개 진단 Render/26객체(lab12)를 확인했다. Artifact11455380463의 ZIP SHA256은 cb2335319fbb1ca644acc73b74e1f62ddd562c1d8cf2ff4d04c1dab9615250df다. 다운로드 후 CRC·8 YAML 체크섬·Source SHA·생성 ConfigMap 참조·held replica/Job·동일 Backend Digest·정확 Project Kind/목적지를 검사했다. 이는 실제 클러스터 시험이 아니다.

[GitOps10 인계](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10#issuecomment-6029054228)에 Valkey 단독 준비→Valkey Service/Ready/연결→App Data/Schema→필요한 단일 Migration→BE→FE 단계를 연결했다. Valkey 단독 준비에 Cloud 금고·Cloud Pool·DB Schema 완료를 잘못 묶지 않으며, 실제1Replica 변경은 해당 입력/권한/공유 사용창·live Diff 수락 후 별도 검토한다.

### 9.3 App 연결/생명주기 Source와 기존 전체 suite 재실행

Source bdaa9dfa0a09e5d8efb1714ccf62860315b1346e는 이전2003fe9d와 비교해 MD2개만 변경됐다. 연결 계약/환경설정, MariaDB/Redis 연결·설정, production.py·production_app.py·clock.py와 연결/자원/생명주기 테스트6개를 전문 대조했다. Runtime Engine2개·Migration NullPool, 생성 중 실패·정상/예외/취소와 Client/Pool 정리의 기존 검사 범위를 확인했다. game_adapter의 시각 변환 helper는 한정 대조했으며 전체 Adapter/게임 상태/Lua/종료 경쟁 의미 검토를 완료로 올리지 않았다.

[Run37557724369](https://github.com/seokpan/seokpan-hybrid-app/actions/runs/37557724369)에서 기존 backend/scripts/verify_ci.py를 Python3.13.15·uv0.12.5·기존 uv.lock으로 실행했다. Lock/sync·Ruff format250파일/lint·mypy119파일·1752테스트가 통과했고 JUnit failure/error/skip0이다. Room/Game/Vote domain100%와 별도 Runner47개/기존80% 커버리지 기준도 통과했다.47개는 기본 suite의 부분집합 재검사이므로 고유 Case 총수로 더하지 않는다.

Artifact11455548206의 ZIP SHA256 a881648d06ade58dd1fd13f83b94c1658febb5e79abaaae851f691b07a1582d0, CRC·source/lock·summary/JUnit/coverage를 다운로드 후 확인했다. trigger1cd72cf3510e9a5b8a3ff223366e4a4d66fbac1e와 실제 checkout bdaa를 구분한다. 임시 workflow는 제거했고 정리 Commit13076301064c03dd056b76338ed74aa7fe37e6cb의 파일 Tree는 bdaa와 같다. audit/b-backend-locked-20261007 브랜치는 검사 이력 참조로 남아 있으며 병합할 코드 변경은 없다.

첫37557295253은 job env의 runner context 오류로 실행 전 실패,37557565189는 uv 배너의 build metadata 문자열 비교로 Backend 검사 전 중단됐다. 임시 실행 정의만 정정했고 두 실패를 App 제품 결함이나 테스트 PASS로 포함하지 않는다. 새 정상 실행 결과와 과거 실행을 구분해 [App1](https://github.com/seokpan/seokpan-hybrid-app/issues/1#issuecomment-6029039957)에 기록했다.

### 9.4 작업 중 새 App 수정과 재검토 파급

작업 중 별도 [App #17](https://github.com/seokpan/seokpan-hybrid-app/pull/17)이 게시됐다. HEAD367938f08e735fe123827b3c9362307b5d59408f는 runner 생성 뒤 첫 await가 cleanup try/finally 밖에 있던 기동 취소 경로를 수정한다. 기존1752 PASS만으로 새 누락 Case를 안전하다고 결론내리지 않는다. 같은 수정을 중복 작성하지 않고 실제 Patch·86줄 회귀를 검토했다.

기존 [Run37557811841](https://github.com/seokpan/seokpan-hybrid-app/actions/runs/37557811841)의 Artifact11455364455 ZIP SHA2560e1f7864d82af842c8e1416ec0778c0c5f23aab619842a983366f02c1764ba05와 before/after JUnit·1754/47 결과를 수신 대조했다. 기존 Source+새 회귀는 취소1FAIL/정상1PASS, 수정 Source는2PASS이며 최종1754/47 각각 failure/error/skip0이다. 이 작업에서 해당 PR의 코드·Run을 새로 만든 결과가 아니다. B 명의 PR의 C/D 리뷰·병합은 별도이며 본인 승인으로 대신하지 않는다.

문서/기준선 검사만으로는 새 Build가 필요 없지만 #17 Runtime 수정을 배포하려면 병합 후 새 Backend Build/Scan/Digest가 필요하다. [추가 인계](https://github.com/seokpan/seokpan-hybrid-app/issues/1#issuecomment-6029077498)에 정정했으며 기존 승인 이미지에 수정이 들어 있다고 기록하지 않는다. Valkey만 기동하는 준비와 Backend 교체는 다른 단계다.

### 9.5 Pool·ROSA·금고의 직접 입력

Pool 크기 환경변수는 현재 App에서 소비하지 않는다. 실제 global/user 연결 한도·idle 시간·예약·종료 중 연결/연속 Rolling 겹침을 C/B가 합의한 뒤 Source/검사→D 새 Build/Digest로 연결한다. [SQLAlchemy Pool](https://docs.sqlalchemy.org/en/20/core/pooling.html)의5+10 기본을 Engine2개에 적용한30/프로세스는 구성상 후보이며 선할당30개가 아니다.3+2는10/프로세스·(활성4+종료중1)×10+예약10=60 시나리오일 뿐이다. [Deployment terminating](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)의 수와 [Engine disposal](https://docs.sqlalchemy.org/en/20/core/connections.html#engine-disposal)의 checked-out 연결은 독립 확인 대상이다. 이 후보를 실제 연결 상한 보장으로 사용하지 않는다.

기존 ROSA LOCAL_PREPARATION/INPUT_CONTRACT/REVIEW_AND_EXECUTION_GATES를 재사용했다. 보조 사본의 bash-n과 OIDC harness9파일 생성·4개 Resource/정규화·원본 Lock 보존만 확인했고 Terraform validate/test/실제 Plan·본인 Caller/Backend는 미실행이다. Lock SHA256b7034e236305de9a67786cfdcd302a589e7cb7ada92d5cbea4286c871cea7831. [Infra25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25#issuecomment-6029050081)에 A 제한 출력/공통 Role·Policy/Backend와 C SG2, B 지원/구독/Quota·사양/시간/비용·실제 가용성을 연결했다. Cost PARTIAL·$450/$500을 유지한다.

[C10/7jth 금고 보고](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6028766924)는 [B 수신](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6028919355) 완료다. Controller 밖 독립 키 사본과 복원한 identity의 해독 확인만 별도다. 이 기록 작성 환경에서 Token을 열거나 키를 보관하지 않았다. [A WireGuard A주/B예비 합의](https://github.com/seokpan/seokpan-hybrid-infra/issues/16#issuecomment-6028757705)도 실제 키 생성·독립 사본 공급과 구분해 수신했다.

### 9.6 현재 수렴 범위와 다음 시작점

이번 변경은 네 실행 문서의 오래된 직접 대기를 한 번 교체하고 이 대장에 근거를 연결하는 범위다. 다른 트랙의 audit/b-s1-s4-20261007·App #17·Infra #39는 존재/범위를 확인해 보존하며 임의로 덮어쓰거나 실제 Apply를 대신하지 않는다.01~04·그림·TH/Q체크·기존 Evidence와 C의 실행 기록은 변경하지 않는다.

이번 묶음의 PR19 재검토·main 병합 수신, App 기존 suite 재검증, 새 App17/이미지 영향 수신, 금고·ROSA·Pool의 직접 인계는 원 기록에 연결했다. 다음은 App17 C/D 리뷰·실제 Build 연결, Valkey 단독 활성화의 실제 입력, 본인 독립 키/Caller·가용성 확인과 Pool 값 합의다. 미검토 게임 상태/Lua·기타 Source/과거 Commit/CI·참조는 §8의 해당 지점에서 이어간다. Q02/03/04/05/10을 완료로 올리지 않으며 신규 Run 없이 Runtime/비용 PASS를 추가하지 않는다.
