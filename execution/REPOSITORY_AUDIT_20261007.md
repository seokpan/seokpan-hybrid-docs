# 2차 저장소 최초 전수 조사 — 2026-10-07

* 현재 판단
- 소스·원 토론·보존 이력·자동 검사·산출물·그림을 연결해 최초 조사 기준 확보. 실제 서비스 전체 성공이나 프로젝트 종료 판정과 별도.
- 우선 보완: App Guest 이름 충돌·captured 시작의 연결 상태 차이, Infra 이관·RDS 제어의 실패 판정, GitOps 공개 설정 검사 문법.
- App 시작/구독 정리 2건·GitOps 설정 검사 2건·Docs Windows 검사 도구 2건은 소스 수정과 격리 검증 완료. 새 소스의 Linux 검사·리뷰·병합·Image 연결은 아래 원 작업에서 확인. 새 App22 UI 변경은 동일 main 위의 독립 후속으로 검토. 포커스·모바일 확대·로비 채팅 높이 회귀3건 수정 후 정확 HEAD 재검증·push 완료.
- 조회 결과는 저장소별 관측 시각과 전체 SHA로 관리. 조사 중 다른 담당자의 병합을 확인해 변경분을 다시 검토.

* 조사 기준과 변경분

| 저장소 | 조사 시작 기준 main | 마지막 검토 main | 확인한 변경 |
|---|---|---|---|
| App | a2afffb8605dafff1cb5b9af215aa0cf93aadcdb | 같은 SHA | #20 e348895·#22 abb6483 및 별도 시작/구독 수정 2개; main 병합 미완료 |
| Infra | 36dc2403aa77e2896cc4ec3c545b92e0afb49205 | 같은 SHA | #43 d5aeddd, #44 v1.3·#45 v1.1·#46 및 #16/#17/#19 최신 댓글 |
| GitOps | a25172c7453b9d7999cb1f3cbeb1ef35774e3b63 | b8cf3235dd44f74dd4ed831449cfedfa08eb34ae | #27·#28·#29·#30 병합, #25 b30e978 새 main 통합 |
| Docs | a9b0207b563aa25be17d4a635f6cc903fbe0e74a | 10dd13de78357d60b78dc5ee8e3a02aad815bd2c | #79·81 C Recovery/Runbook 보고 병합; #72 ba1b998 인계와 본 조사 후속은 main 미병합 |

- 최초 수집: Issue/PR 170개(일반 Issue55·PR115), 원격 branch20개, CI(Continuous Integration, 자동 검사) Run173개.
- 12:33–12:34 UTC 변경분: Issue/PR175개(일반 Issue57·PR118). 새 Issue Infra46·Docs78, 새 PR GitOps29/30·Docs79의 원 토론·소스·결과 연결.
- 13:31 UTC 추가 변경분: App21/22·Docs80/81로 Issue/PR179개(일반 Issue59·PR120), GitOps26 C DB 보고6038214247. 이후 변경분만 추가 검토.
- 14:19–14:20 UTC 재조회: 네 main·사람 토론/리뷰 변경 없음. App22의 승인된 소스 후속 push만 추가 확인. 열린 본인 PR5개, 전체179개 항목·25개 원격 branch 유지.
- 부가 목록: 각 저장소 Tag/Release/Deployments/Environments는 읽기 API200·0건. Label47개·Milestone4개·Workflow목록41개·Artifact111개 대조. Artifact111개 모두 보존 Run에 연결, 만료0. Workflow 목록의 active는 현재 main의 파일/실행 가능을 뜻하지 않으며 실제 main은 App/Infra/GitOps 각1개·Docs0개. GitHub Pages404는 공개 여부/접근 제한과 구분해 성공으로 처리하지 않음.
- 현재 main 추적 파일: App396·Infra57·GitOps58·Docs73. App22 HEAD는402파일·main 대비18파일 변경. 별도 열린 PR와 신규 수정·GitOps 보존 원본41파일도 검토 대상.
- 초기 도달 이력 App127·Infra119·GitOps69·Docs216에서 출발. 삭제된 CI 임시 HEAD·보존 bundle의 PR 시험용 merge·조사 중 새 commit을 별도 참조로 확보해 후속 검토.
- 같은 원문·같은 변경은 원 commit/파일/토론에 연결해 재사용. 파일 목록·구문·Hash 확인을 함수/시험/토론의 의미 검토로 대신하지 않음.

* 주요 발견과 처리

| 항목 | 근거·영향 | 처리·원 작업 |
|---|---|---|
| App Guest 표시이름 충돌 | 서로 다른 정상 Guest가 같은 Guest-NNNN을 받으면 기본 legacy 시작이 Room만 PLAYING으로 바뀐 뒤 실패. 합성 Memory에서 동일 입력 재현 | [App4](https://github.com/seokpan/seokpan-hybrid-app/issues/4): 표시값 유일성 규칙과 시작 전 검증 결정·회귀 필요. #20의 다른 변경으로 해결됐다고 간주 금지 |
| captured 연결 상태 차이 | Domain/legacy는 ready AND connected, captured Lua는 ready만 반영. 연결 끊김 뒤 Ready 유예10초에 의미 차이 | App4: Memory/실제 소유 Lua 동등성 시험 필요. 기본모드 legacy이며 실제 Valkey 재현·활성화는 미실행 |
| 개발 시작 취소 누수 | 첫 await가 정리 try 밖에 있어 취소 때 runner 종료 누락 | fix/4-development-startup-cancel @9e42d286620175be2896b91ccf6a73ed01e6feab. 관련50PASS·Ruff/mypyPASS, 새 PR/정확 Linux 검사 필요 |
| Chat 구독 정리 | 취소 때 aclose 누락, cleanup RedisError가 CHAT_DELIVERY_UNAVAILABLE 변환을 가림 | fix/4-chat-subscribe-cleanup @666dad6260746f7ed570808f0f4d93c760dfec2c. 관련112PASS·Ruff/mypyPASS, 새 PR/정확 Linux 검사 필요 |
| Infra Import/비교 실패 판정 | 원격 gunzip 파이프 오류·SQL 조회 오류가 성공 코드/빈 동일 해시로 남음 | [Infra44](https://github.com/seokpan/seokpan-hybrid-infra/issues/44): 원격 pipefail·각 SQL 단계 실패 차단·예상8테이블/값 확인. 실제 이관 전 C 보완·B 검토 |
| RDS Stop/Start 실패 판정 | 예상 밖 상태의 break·waiter 실패 후 완료 기록, 사본 해시 명령 공백 누락 | [Infra45](https://github.com/seokpan/seokpan-hybrid-infra/issues/45): 요청/조회/waiter 오류 차단·최종 상태 일치·sha256sum 명령 정정. 실제 Stop/Start 미실행 |
| DB TLS 거부 시험 | 잘못된 CA 시험에서 서버 검증 옵션을 제거해 실제 Client 조건과 다름 | Infra44: 이름 검증 유지한 CA/이름 음성 시험 분리 |
| 옛 보관기간 변수 | 옛 tfvars retention 값은 Plan 중단 대신 경고 후 무시되고 새 기본7 적용 가능 | [Infra42](https://github.com/seokpan/seokpan-hybrid-infra/pull/42)·[Infra19](https://github.com/seokpan/seokpan-hybrid-infra/issues/19): A 보호 입력의 필드 이름·Plan 경고/실제 보관기간 확인. Core1.16.4 합성 Root 재현 |
| Valkey Lab 설정 검사 | 대소문자·후순위 덮어쓰기·지원하지 않는 inline 댓글/escape를 잘못 승인 | fix/valkey-stage1-config-validation-20261007 @bcb7bd18bf7d7c55a0c59bc45a7ae6c7783dbbaf(원 수정2c22e0ac·새 main 통합). 보수적 literal 문법·정확 값/횟수/순서 검사. [GitOps21](https://github.com/seokpan/seokpan-hybrid-gitops/issues/21)·[GitOps6](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6) 연결 |
| Recovery 설정 검사 | 같은 셸 문법 오해가 Recovery 검사에도 남음 | fix/recovery-config-validation-20261007 @fc3d95031945c1bbd3819c541409c7621dd7cd62. Lab parser 재사용·회귀2건, Lab 수정 선행 병합 필요 |
| Docs Windows 도구 | Windows 경로 구분자 및 기본 cp949 인코딩으로 검사 실패 | portable path0efe597·명시 UTF-8 17b9e203. 현재 브랜치에 포함, 기본 인코딩 환경14회귀PASS |
| App22 UI 회귀 | 강퇴 취소 후 포커스 복귀 실패·모바일600px 확대 제거·390px 로비 채팅 높이 변동 | feat/desktop-ui-polish @abb648350084c9ebe6c63ee7668921de66f5b03f. 후속6파일 수정·기존 입력/DOM/쓰기/모바일 확대 단언 보존. 단계별 남는 공간 자동맞춤 검사 |
| 현행 안내 지연 | 승인 완료 DR 기준의 병합 대기 표현·Provider 후속9.43 중복 | 발표 기준·팀 인계 안내·05 현행 목표 정정, Provider 후속9.46으로 변경. 기존 Run·03/04 원문 보존 |
| 원 Issue의 현재 카드 지연 | App2/4·GitOps10/21·Infra25·Docs21이 이후 보고/병합보다 뒤처짐 | 최신 댓글과 완료 범위만 갱신할 복사안 준비. 특히 GitOps21 Closed/전체 체크가 실제 TLS/AUTH/Ready/삭제 보호 근거를 대신하지 않음 |
| 보존 참조 Hash | GitOps 원본 SHA256SUMS의 자기 파일 행 불일치 | 원본 그대로 보존. 인덱스 자기 행을 제외한 payload40개와 고정 commit 대조 |
| 운영 안내·일정 | App Harbor-only Pipeline 상태, Infra RDS 제어 안내, Milestone10/18이 실제 소스/승인10/16과 차이 | 현재 README·원 결정 링크·Milestone 수정 제안. 과거 기준과 책임/실제 수행 기록 유지 |

- Infra17 identity_svc 운영 CRUD 유지 결론은 최신 댓글6037754777·Infra44 v1.3에 반영돼 해소. 실제 GRANT/TLS/접속 확인은 별도.
- App15의 D 질문4개는 응답 필요: release-source.yaml annotation PR 분리, release_id 형식, Cloud tag→Digest/public ECR name 범위, lab 실제 mapping 전 fixture 범위.

* 실제 검증과 한계

| 검증 | 결과 | 적용 범위 |
|---|---|---|
| App20 e348895 Linux CI37605414615 | Backend1774·부분집합47·소유 Redis7.2.4 Lua9 PASS | 해당 HEAD 소스. 새 G03/G04·Valkey·Image/실제 업무로 승계 금지 |
| App20 CI Artifact11474896267 | ZIP SHA256·metadata Digest·CRC·Source/JUnit 대조 PASS | 이전 Run의 다운로드403 이력은 보존하고 이번 후속 성공을 별도 연결 |
| App20+개발/Chat 수정 격리 조합 | 관련174PASS·Ruff223/mypy119PASS | Windows Python3.13.15; 조합의 정확 Linux 전체 CI 미실행 |
| GitOps25 b30e978 CI37624059074 | Linux69PASS, 진단8Render/26객체 | Artifact11483631189 ZIP Digest/CRC·내부 Hash·Source/Tree·정확 LF 로컬 바이트 일치 |
| GitOps 등록+Lab+Recovery 수정 조합 | 73건 중70PASS·기존 Windows POSIX fixture3FAIL | Kustomize5.7.1/Python3.13.15/PyYAML6.0.2; 같은 기존3실패를 포함한 Windows 제한. 새 조합 Linux 전체 CI 미실행 |
| Frontend main a2 격리 verify | generated API·정적 검사·도구81·unit269·build PASS | Node24.19.0/npm12.0.2, Lock 고정; 실제 Backend·nginx·Route 접속과 별도 |
| Frontend main a2 UI 모의 시험 | 18Case를2회 반복=36PASS | 1280/390px 포함, 모의 API/WS. 실제 WSS·다중 Pod 시험 아님 |
| App22 abb6483 격리 verify/UI | API·format/lint/type·도구81·unit278/21파일·build67 모듈·정확 HEAD UI36PASS | Node24.19.0/npm12.0.2 fresh 설치, 모의 API/WS. 1299×864/1440×900의 대기/진행/결과6화면·1280/390px 시험. clean Source SHA256 98a50c5500f2aa232652e3c497eecfdcf8a01e00a9ea0b27b244956e66bbcc10. Backend·CI·Lock·schema·nginx/Dockerfile 변경0 |
| Infra 제어 흐름 반례 | 오류를 성공으로 기록하는 경로 재현 | 합성 셸/빈 Terraform Root. DB/AWS/SSH·실제 Plan 미접근 |
| Docs 그림·검사 | Source5·SVG12·PNG12·font12·CIDR9 무결성 PASS, PNG12·App SVG 및 댓글 PNG13 시각검토 | 기존 Git LF 사본. 새 Inkscape Render·실제 구축 결과판·Runtime PASS 없음 |
| CI 보존 자료 | 전체181Run·111ZIP의 Hash/CRC·JUnit·Source 연결, bundle16·tar4 내부 대조 | tar571파일 모두 Git blob 연결. 제공하지 않는 로그와 삭제된 손상 payload는 아래 제한 |

- App22 실패 이력: ui01 6PASS/1FAIL/29미실행(숨은 상세 패널 진입 흐름), ui02·03 8/1/27(모달 포커스, ui03은 로컬 패치 경로 오류로 같은 소스 반복), ui04 13/1/22(모바일 확대), ui05 13/1/22(옛 단계 간 고정 픽셀 비교), chat01 2/1/5(로비 높이). 남는 공간 자동맞춤을 확인하는 새 단언·수정 뒤 chat02 8PASS, ui06 36PASS, 확정 commit ui07 36PASS. 중간 타입 검사 실패도 보존 후 Node용 브라우저 평가 방식 보완·전체 verify 재통과. skip/쓰기·DOM 단언 축소 없음.
- Windows clone의 CRLF 변환은 Kustomize ConfigMap Hash와 source_sha256을 바꿀 수 있음. 고정 revision 선택 목록은 정확 Git Blob LF 또는 해당 Linux 산출물 기준. 기존 clone의 줄바꿈/개인 변경을 초기화하지 않음.
- GitOps Source 진단 산출물은 실행용 승인 YAML이 아님. 실제 실행 전 Gate/live Diff·현재 대상·선택 리소스·Owner/사용창 수락 필요.
- Windows 로그인 계정 soldesk·Git 기록 계정 tjung03, 격리 실행 Python/Bash/Node 및 GitHub Actions Linux. 실제 lab/금고/ROSA 실행은 본 조사에서 수행하지 않음.

* Stage1 보고와 현재 Stage2 소스

| 구분 | 마지막 수신 보고 | 현재 GitOps main 소스 |
|---|---|---|
| Workload/등록 | SHA A244b48b885d7ac645c402e561a032ae65a8f3461 | Root targetRevision=SHA B bfee2669e62bf823969ce224e5599eccace5d024 |
| App replicas | Valkey1·FE/BE0 | Valkey1·FE/BE1 |
| Migration·보호 | suspend/current, base/Recovery hold | suspend/current/300초·base/Recovery0·Prune/Delete=false 유지 |
| 근거 | GitOps5/6034601393 등록·선택Sync, GitOps6/6034590906 ImageID/UID,6034843156 DB Secret 공급 | #28/29/30 리뷰·소스 병합. B 등록 재apply/Stage2 실제 Sync·업무 성공 근거 미수신 |

- [GitOps26](https://github.com/seokpan/seokpan-hybrid-gitops/issues/26)에서 [C DB 보고6038214247](https://github.com/seokpan/seokpan-hybrid-gitops/issues/26#issuecomment-6038214247)의 형식/GRANT·TLS1.3/이름 검증 접속·합성 데이터 출처 수락 수신(D 조회 실행/C 판정). 직접 재조회는 미수행. 남은 입력: B 등록 개정 적용·선택 Sync, 실제 Route/Origin/TLS/WSS·Owner/사용창·Gate/live Diff와 지정 실행 경로 수락.
- 기존 승인 FE/BE Image는 App46e21 기반. App17/18/19와 새20/후속 수정의 Build/Scan/Digest·플랫폼/Pull·App 및 held Migration 동일 Image 연결 필요.
- Controller SQL/Valkey 금고 본체 해독 성공 보고 유지. 남은 것은 Controller 밖 독립 사본·복원 Identity 검사이며 새 키/공개키 전달 반복 없음.
- C Infra46/Docs79·81의 Recovery VM 생성·TLS/격리 준비·Recovery CA 오프라인 사본 보고 수신. Recovery CA 사본과 B의 SOPS 복원 Identity 검사는 서로 다른 범위. Server04의 Controller/복구VM 공통 Host 한계·실제 사본/15분 운영·복원계정/Data/업무·전체 RTO는 별도.
- ROSA 첫 실제 Plan은 B 목적 Caller/Backend·지원/Quota, A 제한 출력/prerequisite, C SG2, 예비 비용·현재 사용창 수락 후 지정 실행자1명으로 진행.

* 열린 본인 PR과 직접 순서

| PR | 검토 상태 | 다음 행동·순서 |
|---|---|---|
| [App20](https://github.com/seokpan/seokpan-hybrid-app/pull/20) | Ready/e348895, A 승인5449718861·동일 HEAD CI 성공 | Source 보완 없음. 병합 후 새 Backend Build/Scan/Digest·App/held Migration 수락 별도 |
| [Infra43](https://github.com/seokpan/seokpan-hybrid-infra/pull/43) | Ready/7d89def, A 승인5449687427·CI 성공 | Source 보완 없음. 병합 후 기존 Workspace/State 위치 확인·Backend 재초기화 조건·실제 Caller/Plan 별도 |
| [GitOps25](https://github.com/seokpan/seokpan-hybrid-gitops/pull/25) | Ready/53314d3, 변경요청5449781239 후 정정·A 재리뷰 요청 | 최신2파일 diff·SHA B 선언검사 PASS/A BLOCKED·Linux69PASS. 재승인 전 병합 대기 |
| [App22](https://github.com/seokpan/seokpan-hybrid-app/pull/22) | Ready/663b522, A 승인5449755134·제품검사/Lock 동일 | Source 보완 없음. App20과 변경 경로 독립. 새 Frontend Image·실제 Backend/Route/UI 검증 별도 |
| [Docs72](https://github.com/seokpan/seokpan-hybrid-docs/pull/72) | Ready, main10dd 통합·현재 리뷰 후속 연결 | 관련 PR의 새 HEAD·승인·병합/브랜치 정리 결과를 확인해 기록하며 열린 상태 유지 |

- App/Infra/GitOps main은 승인 최소1·새 push 뒤 이전 승인 무효화·squash만 허용하는 Ruleset 적용. App20/22·Infra43은 현재 HEAD 승인 완료. GitOps25는 정정 후 재리뷰 대기. Docs72는 현재 승인 없음.
- Docs는 활성 main Ruleset 없음. 프로젝트의 사람 검토와 실제 수신을 생략하는 근거로 사용하지 않음.
- CI 성공과 review request 존재는 승인 아님. Ready 전환 뒤 발생한 새 Run도 같은 HEAD와 conclusion 확인.
- main/reference 및 열린 PR·후속 base 의존 branch 보존. squash 뒤 `--merged` 결과만으로 변경 미반영/삭제 가능 판정 금지. 필요한 patch/Run·고정 참조·개인 미push·실제 배포 revision 확인 뒤 브랜치 소유자가 삭제.

* 재검토 종료 범위와 다음 입력
- 현재 소스/시험→승인03/04→원 토론→과거 고유 변경→CI/산출물/보존 bundle→저장소 간 링크→새 원격 변경→수정 조합 재시험 순으로 재대조.
- 접근 가능한 자료에서 새 고유 자료 검토·수정·재시험을 반복하고, 마지막 변경분 대조와 후속6파일 독립 검토에서 추가 미검토 변경/새 결함0을 확인해 해당 관측 범위의 최초 조사 종료. 미해결 항목이 모두 해결됐거나 프로젝트가 완료됐다는 뜻은 아님. 다음부터 이 기준 이후 변경분을 우선 검토. 고유 원문별 검토 근거와 정확 중복 연결은 로컬 coverage 기록으로 보존.
- 확인 불가: 초기 오래된/취소 Job 로그9건, Docs의 삭제된 손상 Base64 입력1건, App21의 비공개 과거 Sites 디자인 참조, 비공개 Harbor Layer/Runtime·보호 State/전체Output/SavedPlan·실제 개인 입력/금고/Cloud. 부재·권한 없음·성공으로 추정하지 않음.
- 연쇄 링크 검사: GitHub 링크800개(외부 연결126개 포함), 상대 경로918건·문서 anchor750건 대조. 옛 삭제 branch1개는 원 commit으로 연결하고 현재 대상의 누락0 확인. 인계 첨부13PNG·저장소12PNG·App SVG 시각검토는 과거/소스 자료이며 현장 상태 수락과 별도.
- 1차 외부 저장소·공식 기술자료는 연결된 관련 범위만 대조. 4개 2차 저장소 밖 모든 인터넷 자료의 전수 검토를 주장하지 않음.
- 승인03/04 종료, DR10분·DB RPO30분·운영 Backup15분, CP3/Infra3/Worker3, Cost PARTIAL/$450계획/$500한도, TH81·기존 완료2, Q02/03/04/05/10 미완료 보존.
- 공개 Issue/PR·댓글·리뷰·병합·branch 정리 상태는 원 작업에 기록한다. 소스 변경·검사 개정과 실제 실행·수신 범위를 구분해 인계.
- 증거: [Source 조사 Run](../evidence/T09/source-audit-20261007-01/summary.md)·[05 추가 기록](05_IMPLEMENTATION_AND_VALIDATION.md#repository-full-audit-20261007)·[Tracker](WORK_TRACKER.md#repository-full-audit-20261007).


* 2026-10-08 리뷰 후속

[검증 Run](../evidence/T09/registration-review-followup-20261008-01/summary.md)에 SHA B/A 비교·Windows66/3FAIL·정확 새 HEAD Linux69PASS와 원 리뷰 연결. 승인된 세 PR은 Source 보완 없이 병합 가능하며 새 Image/실환경 수락은 별도. GitOps25는 새53314d3의 재승인을 기다린다. 멘토링 후보의 설계·도구 도입은 이 리뷰 후속에 포함하지 않는다.
