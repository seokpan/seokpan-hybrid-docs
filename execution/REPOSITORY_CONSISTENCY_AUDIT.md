# 2차 저장소 정합성 조사·수정 대장

> 개정: 2026-10-07 KST  
> 상태: IN PROGRESS — 현재 안내·기록 주체·그림·등록용 소스 보완과 지정 회귀검증 완료, 전체 코드/이력 의미 검토와 Q10 수렴 미완료  
> 담당: B 정태훈(tjung03). 다른 담당자의 실제 실행·승인·수신은 해당 원 기록으로 구분한다.  
> 원 작업: [개인 #21](https://github.com/seokpan/seokpan-hybrid-docs/issues/21), [팀 #8](https://github.com/seokpan/seokpan-hybrid-docs/issues/8)

## 1. 판정 기준과 이전 조사

Source 존재·리뷰·병합·인계 제출·수신·실제 실행·시험 판정을 구분한다. 자료 수집과 검색만으로 전수 의미 검토를 완료하지 않는다. 발견→원 근거→직접/후속 영향→필요한 수정→재검증을 반복하며, 접근 가능한 전체 대상의 미검토·미해결이 남아 있으면 Q10을 완료하지 않는다.

이 문서는 현재 상태와 다음 확인 지점을 정리한다. [이전 조사 전문과 F01~F10](https://github.com/seokpan/seokpan-hybrid-docs/blob/d2371a44f4c9b35cf8082991ec9700ccea2ec524/execution/REPOSITORY_CONSISTENCY_AUDIT.md)은 고정 Commit에서 보존한다. 과거 Evidence·측정·실행자·승인을 최신 값으로 소급 변경하지 않는다. 기존 TH 81개와 실제 완료 2개는 이 조사 때문에 변경하지 않는다.

## 2. 고정 체크리스트

Q06은 현재 12장과 생성/출처 경로의 대조·필요 수정·시각 검증 완료다. Q07은 7개 비교와 개정본 제공 완료이며 실제 Project 등록 교체는 아니다. Q08은 수집한 B 명의 공개 기록과 현재 문서의 작성 과정 메타 정리 범위다. Q09는 발견한 수정의 B 범위 처리·보존·원 작업 인계이며 팀원 리뷰 수신 완료를 대신하지 않는다. Q10은 전체 코드·이력 의미 검토가 남아 미완료다.

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

## 3. 병합·수정 PR과 정확한 Source

Docs #64는 `94d5955612f589f40343360709513568bc5f0dc0`, #67은 `d2371a44f4c9b35cf8082991ec9700ccea2ec524`에 병합됐고 작업 브랜치는 삭제됐다. GitOps #17은 `fa3cea313e2cb1533d9703082619b085a3de25cc`에 병합됐다. 이 완료 상태를 다시 리뷰 대기로 되돌리지 않는다.

| 현재 수정 PR | 검증한 Source 및 범위 | 실제 실행과의 경계 |
|---|---|---|
| [Docs #68](https://github.com/seokpan/seokpan-hybrid-docs/pull/68) | 내용 검증 개정 `92b72b7fed298da04e1c0eef1ae60d32e50bbffe`. 현재 안내·설계 승인 표현·출처·그림04 및 본 조사 대장 | 본 대장 이후 HEAD 이동은 PR에서 확인. 실제 Host/접속·금고·Cloud 실행을 추가하지 않음 |
| [Infra #38](https://github.com/seokpan/seokpan-hybrid-infra/pull/38) | `1d7076785bb4c91613308409e5215e50d06c3ebf`. 두 fixture·README·회귀검사 5개. 실행 코드 Tree는 검증된 `27b796a4c2efc17cda3581e201c9a86e484a8f56`과 동일 | 새 버전은 실제 실행자 `--operator` 필수. 과거 Run 실행자를 바꾸지 않고 실제 DB/Valkey 재시험으로 표시하지 않음 |
| [App #16](https://github.com/seokpan/seokpan-hybrid-app/pull/16) | `708ea3fafec95f68319fea7b7b966ecf97e4689c`. 연결 계약·이관 근거 문서 2개 | App 실행 코드·Dependency/Lock·Schema·Image 변경 없음 |
| [GitOps #18](https://github.com/seokpan/seokpan-hybrid-gitops/pull/18) | `f956346184a3eff9fb558d64324c8414a9ee8f0b`. apps 안내와 두 인계 문서 3개 | Manifest·Digest·Replica·Migration·renderer의 실행 동작 변경 없음 |

위 네 PR은 이 기록 시점 미병합이며 C/D 검토 대상으로 연결한다. 승인과 병합을 대신 수행하지 않는다. 다음 작업은 별도 채팅 통보를 기다리지 않고 실제 HEAD·리뷰·병합·브랜치를 재조회한다. 원 Runtime 이슈는 문서 PR 병합만으로 닫지 않는다.

## 4. 수집 범위·누락 검사·확인 한계

[재개 Snapshot Run 37538088477](https://github.com/seokpan/seokpan-hybrid-docs/actions/runs/37538088477)은 2026-10-07 07:03:20~07:04:16 KST에 공개 Source·협업 기록을 다시 수집했다. ZIP SHA256은 `e2afd5ebcdbcefc6fed5468a2258590146bb5cfbf51d8d55557c29097a7f9665`이며 Artifact ID는 `11447536059`다.

수집 시점의 고정 범위는 main 파일 570개, Branch 11개, 일반 Issue 47개, PR 91개, 일반 댓글 182개, 제출 리뷰 73개, 도달 가능한 Commit 393개, Workflow Run 목록 96개다. 이후 생성한 PR·Commit·Run을 이 고정 표본에 소급 포함하지 않는다. 페이지 응답 334개를 추적했고 수집 오류·제외 0건, Issue/PR의 댓글 수와 수집 결과 불일치 0건을 확인했다. 저장소별 시작/종료 Branch SHA도 같았다. 669개 Blob과 ZIP 해시를 다시 검증했다. 순차 수집이지 네 저장소가 동일 순간의 원자적 Snapshot이라는 뜻은 아니다.

앞선 Run 37537826727은 저장소 metadata URL의 불필요한 끝 슬래시로 실패했다. 주소를 고친 위 Run의 성공 결과를 사용한다. 실패를 성공 수집으로 계산하지 않는다. 임시 수집·수정 workflow와 입력 파일은 각 작업 완료 후 최종 Source 트리에서 제거한다.

**아직 미완료인 전수 범위:** 모든 현재 함수/설정/시험의 의미와 실행 분기, 현재 refs에 도달 가능한 과거 Commit별 코드 diff, 모든 과거 CI job log/artifact의 독립 재검증, 전체 연결의 fragment/외부 참조 의미. 비도달 삭제 이력·개인 미커밋 자료·비공개 운영 입력·실환경은 조회 가능한 공개 범위와 별도다. 검색·AST·파일/댓글 개수와 위 Snapshot만으로 이 범위를 완료 처리하지 않는다.

현재 문서의 상대 파일 경로 475개는 확인했고 누락 경로 후보는 0개다. 이는 모든 anchor·외부 URL의 의미 검증 완료가 아니다. B 명의 수집 본문/댓글 137개 및 제출 리뷰 14개에서 작성 과정 메타를 선별하고 후보의 문맥을 검토했다. 수정 후 남은 선별 문구는 서비스 사용자·손실 허용에 관한 정상 설명 또는 실제 과거 Run의 수행자 근거이며 무조건 삭제하지 않았다.

## 5. 이번에 끝낸 수정과 재검증

### 5.1 현재 안내와 실제 의존

실행판·학습 안내·05·WORK_TRACKER의 현재 안내에서 완료된 공개키 전달·Registry 공급·Source 병합을 다시 기다리게 하던 표현을 정리했다. 여러 시점의 `지금/현재`는 과거 관측으로 분리한다. TH 번호·완료 체크·기존 Source/Run URL은 보존했다.

GitOps 인계의 lab Harbor Pull Secret 신규 공급·Registry 재선택 대기를 없애고 #17의 내부 Registry 주소와 동일 Digest를 연결했다. cp-03에 이미 보존된 Harbor 원본의 offline 검사는 lab 직접 Harbor Pull과 다른 작업이므로 유지했다. Data CA는 ConfigMap, 자격은 목적별 Secret으로 구분한다. 공급물·선언·Service/Ready·최종 업무는 각각 별도다.

App 연결 안내는 Valkey 7.2 선택과 과거 Redis OSS/합성 TLS 시험을 구분한다. Pool 축소 후보를 채택하지 않고 실제 연결 상한·종료 중 연결·예약·부하를 확인한 후 필요한 App Source→새 Build/Digest→활성화로 연결한다.

### 5.2 문서의 독립성과 기록 주체

설계·팀/개인 안내·이관 근거와 B 명의 Issue/PR/댓글을 목적·대상·승인 범위·변경·근거·결과·한계로 정리했다. `정태훈 요청`·작성 지원 홍보·대화 인용을 기술적 원인처럼 적은 문구를 제거하되 실제 과거 Run의 Codex 실행·C/D의 수행/검토·측정·한계는 보존한다.

이번 재개에서 B 명의 기존 본문/댓글은 중복 제외 22곳을 변경했다. 변경 직전 원문 해시·작성자 `tjung03`·URL·전체 SHA·체크 상태를 확인하고 body만 수정한 뒤 정확한 재조회 일치를 검사했다. 다른 작성자의 본문·리뷰·완료 상태는 변경하지 않았다. 이전 중단 작업의 변경 건수를 여기에 중복 합산하지 않는다. 전후 본문은 해당 Run 산출물에 보존한다.

03의 남은 세 승인 표현까지 다시 확인해 정리했다. Evidence 안내의 RPO30분 `후보` 표기도 채택된 시험 요구사항으로 수정했다. 실제 사업 사용자의 손실 허용·상용 SLA나 Runtime 성공을 추가한 것이 아니다. C의 05 §8.9~8.13은 원문 그대로 보존했다.

### 5.3 그림04와 전체 12장

그림04의 Path/Port 미정 문구를 현재 GitOps Source와 대조해 FE `/`→8080, API `/api/v1`·WSS `/ws/v1`→Backend8000으로 수정했다. builder·SVG·PNG·manifest를 함께 변경했으며 나머지 11쌍의 바이트는 보존했다. 실제 Route Host·클러스터 적용·HTTP/WSS 성공은 별도다.

12장 전체의 문구·주요 연결 방향·환경 경계·배치/가독성을 확인했다. Valkey 표기, DR10/30/15, Cloud ECR/온프레미스 Harbor 역할, 사용자 정상 경로와 VPN 비의존, Secret/Bundle 보관의 범위를 대조했다. 해당 그림들은 승인 설계의 설명이지 현장 배포 완료 그림이 아니다.

최초 그림04 개정 Run은 생성기의 전체 layout 기준 기하 12건을 검사했다. 이후 문서 표현만 바꾼 최신 manifest 갱신은 `--integrity-only`로 기존 산출물 바이트와 원문 식별을 확인하며 geometry 0/생략으로 기록한다. 이전 실제 기하 검사는 history에 남는다. 두 범위를 동일한 검사로 표현하지 않는다.

### 5.4 복구 예행 도구

Infra #38은 새 Run에서 특정 도구명을 실행자로 고정하지 않고 명시적 `--operator`를 요구한다. 누락·잘못된 값은 준비/실행 전에 거부하고 기존 출력은 덮어쓰지 않는다. 실행자 문자열은 인증·리뷰·인계 수신의 증거가 아니다.

새 기능으로 채택되지 않은 과거 개별 게임 결과 HTTP 화면은 필수 `missing_inputs` 대신 `known_limitations`로 구분했다. 기존 두 부분 fixture의 고정 App/Redis 버전·실제 과거 Evidence와 전체 T18 미검증 경계는 유지한다. 운영 복구 코드/시험의 전체 완료로 표시하지 않는다.

### 5.5 검증 원본

| Run | 확인 결과와 Source 범위 |
|---|---|
| [Docs 37520034315](https://github.com/seokpan/seokpan-hybrid-docs/actions/runs/37520034315) | 중단 전 게시한 #68 내용·그림04·전체 layout 검증. Artifact15파일을 복원/해시 대조 |
| [Infra 37519877827](https://github.com/seokpan/seokpan-hybrid-infra/actions/runs/37519877827) | 실행자/Evidence-only 회귀8개, 5개 출력 파일 대조. 실제 DB/Cloud fixture 재실행 아님 |
| [App 37539590807](https://github.com/seokpan/seokpan-hybrid-app/actions/runs/37539590807) | 연결 MD·B 본문4곳의 pre/post 해시·보존·readback. MD 내려받아 바이트 일치 확인 |
| [GitOps 37539797118](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37539797118) | 인계 MD3개·B 본문3곳 보존/readback. 내려받은 MD3개 바이트 일치 |
| [Infra 37540487457](https://github.com/seokpan/seokpan-hybrid-infra/actions/runs/37540487457) | B 본문6곳 정리·readback. 기존 #38 코드 Tree 보존 |
| [Docs 37540621286](https://github.com/seokpan/seokpan-hybrid-docs/actions/runs/37540621286) | 개인 안내2개·B 본문8곳, 회귀13+16. MD2개 내려받아 바이트 일치 |
| [Docs 37541229258](https://github.com/seokpan/seokpan-hybrid-docs/actions/runs/37541229258) | MD8개·manifest2개, C 구획/체크/URL/SHA 보존, 회귀13+16·무결성12쌍·멱등성. 출력10파일 내려받아 바이트 일치 |
| [Docs 37542628820](https://github.com/seokpan/seokpan-hybrid-docs/actions/runs/37542628820) | 남은 승인 표현3개·manifest 식별 갱신. 회귀13·기존 이미지 무결성·멱등성·출력 해시 검사 |
| [GitOps Native 37541642040](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37541642040) | trigger `1e6152a9d4beb652f5b4fe4d3fd6053a3127cfd1`의 validate success. 최종 HEAD는 임시 workflow 제거 후이며 동일 HEAD CI라고 표시하지 않음 |

마지막 중복 본문의 추가 정리와 재조회는 App 37541545817, Infra 37541585311, GitOps 37541638065, Docs 37541690283에 보존한다. 최종 로컬 반복에서 검증기13·복구 수치16·실행자8, 설계5개/그림24파일 식별·XML/PNG12개, lab FE/BE/Job 주소·Digest·replicas0/suspend300·CA ConfigMap·Infra Valkey Source를 다시 확인했다. 새 Runtime·유료 실행·Token 복호화는 수행하지 않았다.

## 6. Project 소스 7개 제공

`Seokpan_Project_Sources_7files_AuditResume_2026-10-07_v2.zip`에 원래 이름의 MD7개와 `REGISTRATION_MANIFEST.json`, 교체 안내를 넣었다. ZIP SHA256은 `cdc9377db3e2550ca8ca9fb95a2c68ffe20f39376f841df29111b0daedaa11a6`이다. CRC와 모든 포함 파일 해시를 검사했다.

- 00/01: 기존 등록본과 동일. 역사적 출발점·목적/상위 경계를 유지한다.
- 02/03/04: Docs #68의 검증 Source `92b72b7fed298da04e1c0eef1ae60d32e50bbffe`와 동일한 사본. #68 리뷰에서 내용이 바뀌면 최종 병합본으로 다시 대조한다.
- PROJECT_INSTRUCTIONS: 기존 절·체크 상태를 보존하면서 DR·Valkey·Registry·독립적인 기록 주체·Q/TH 구분·직접 의존/병행 원칙을 정합화했다.
- 개인 구현·학습·발표 계획: TH와 과거 관측을 보존하고 현재 출발점·실제 입력 대기·병렬 준비·새 도구 버전 확인·원 작업 링크를 연결했다.

마지막 두 파일은 동명 GitHub 정본이 없는 Project 전용 보조 소스다. 명세/실행 문서와 대조해 제공한 것이며 저장소와 자동 동기화되는 파일이 아니다. 실제 Project 첨부 교체는 수행하지 않았고, 기존 버전과 새 버전을 동시에 활성 기준으로 두지 않는다. 비밀값·개인키·폰트는 묶음에 포함하지 않는다.

## 7. B 후속 작업의 직접 의존

| 경로 | B가 계속할 일 | 원 작업과 선행 입력 |
|---|---|---|
| Cloud AUTH | 본인 jth 계정에서 값 출력 없이 복호화·암호문 해시 확인, C 회신·개인키 독립 보관/복구 확인 | [Infra #19](https://github.com/seokpan/seokpan-hybrid-infra/issues/19). 공개키 전달/공급 보고는 완료. C의 계정별 확인을 B 본인 실행·독립 백업으로 승계하지 않음 |
| lab | D 작성 수락/Valkey 선언 PR → C Data/B Source·AppProject 검토 → Service/Ready·DB/Schema·CA/목적 Secret·Route·권한·사용창·live Diff 수락 → 필요한 단일 Migration·BE·FE·동일 조합 Run | [GitOps #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10)·[#6](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6). Cloud 금고 확인과 병행. 기존 DB/Redis/PVC 보호 |
| ROSA | 본인 clone·도구·Caller/Backend·지원·사양/시간/가용성·비용 입력 | [Infra #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25). 실제 Plan은 A 제한 출력/공통 prerequisite·C Data SG2. 생성은 전체 Plan/Cost/실행창 수락 뒤 |
| Pool/새 Image | 실제 연결 상한·종료 중 연결·예약·부하를 C와 합의하고 필요 App Source→D Build/Digest | [App #1](https://github.com/seokpan/seokpan-hybrid-app/issues/1)·[#4](https://github.com/seokpan/seokpan-hybrid-app/issues/4). 3+2/60은 미채택 시나리오 |
| Recovery | 승인 Image·실행 파일·TLS/AUTH Probe·Storage/UID를 선언·renderer·검사와 함께 정합화 | GitOps #10·Infra #17. 기존 held redis-server/TCP Probe를 Valkey 수락으로 사용하지 않음. 임의 Digest/Volume·guard 우회 금지 |

Cloud 금고 확인을 lab 검토의 선행조건으로, OCP 철거·팀원 전체 업무·전체 Recovery 종료를 ROSA 준비의 선행조건으로 묶지 않는다. 기록·Source의 완료와 실제 공급/업무/Cost PASS는 별도다. Cost PARTIAL·실제 가용시간 미확인과 Freeze milestone10/18 vs 승인10/16의 메타데이터 후속도 유지한다.

## 8. 다음 미완료 묶음과 종료 조건

다음에는 새 Snapshot을 처음부터 반복 생성하기보다 위 Snapshot과 최종 PR의 변경분부터 재조회한다. 다음 미완료 묶음을 구분해 파일/함수/원 이슈/시험/인계 단위로 검토 결과를 남긴다.

| 미완료 묶음 | 추가로 끝낼 내용 |
|---|---|
| Q02/Q05 — 실행 코드 의미 | App DB/Redis 연결·Pool·시간·공유 상태/Lua·최종화 분기, GitOps Recovery 선언/renderer/검사, CI Writer/Promotion과 해당 Source/시험 대응의 남은 전면 검토 |
| Q03 — 협업·변경 이력 | 수집한 모든 과거 Commit 변경과 CI log/artifact의 의미 검증, 참조 anchor/외부 자료·접근 불가/보존 예외를 명시 |
| Q04/Q09 — 인계와 파급 | 위 코드 검토에서 새로 확인되는 직접 입력·순환 대기·작성/수신 범위를 원 Issue에 연결. 필요한 추가 수정이 생기면 해당 Q를 다시 진행 상태로 관리 |
| Q10 — 전체 수렴 | 미검토 대상과 확인 가능한 미해결이 없고, 최종 원격 변경·PR 결과 대조에서도 새 보완이 없을 때 판정. 이번 지정 수정 묶음의 검증 성공만으로 완료하지 않음 |

이번 결과는 현재 안내/작성 과정 메타·그림·등록 소스의 보완과 지정 회귀검증을 마친 체크포인트다. 모든 코드·과거 이력의 전수 의미 검토와 프로젝트 구현 완료는 아직 아니다. 검토 범위를 숨기지 않고 다음 단계는 이 표의 남은 대상부터 이어간다.
