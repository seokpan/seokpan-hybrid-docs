# 2차 저장소 최초 전수 조사 — 2026-10-07

* 현재 판단
- 소스·원 토론·보존 이력·자동 검사·산출물·그림을 연결해 최초 조사 기준 확보. 실제 서비스 전체 성공이나 프로젝트 종료 판정과 별도.
- 우선 보완: App Guest 이름 충돌·captured 시작의 연결 상태 차이, Infra 이관·RDS 제어의 실패 판정, GitOps 공개 설정 검사 문법.
- App 시작/구독 정리 2건·GitOps 설정 검사 2건·Docs Windows 검사 도구 2건은 소스 수정과 격리 검증 완료. 새 소스의 Linux 검사·리뷰·병합·Image 연결은 아래 원 작업에서 확인.
- 조회 결과는 저장소별 관측 시각과 전체 SHA로 관리. 조사 중 다른 담당자의 병합을 확인해 변경분을 다시 검토.

* 조사 기준과 변경분

| 저장소 | 요청 기준 main | 마지막 검토 main | 확인한 변경 |
|---|---|---|---|
| App | a2afffb8605dafff1cb5b9af215aa0cf93aadcdb | 같은 SHA | #20 e348895 및 별도 시작/구독 수정 2개; main 병합 미완료 |
| Infra | 36dc2403aa77e2896cc4ec3c545b92e0afb49205 | 같은 SHA | #43 d5aeddd, #44 v1.3·#45 v1.1·#46 및 #16/#17/#19 최신 댓글 |
| GitOps | a25172c7453b9d7999cb1f3cbeb1ef35774e3b63 | b8cf3235dd44f74dd4ed831449cfedfa08eb34ae | #27·#28·#29·#30 병합, #25 b30e978 새 main 통합 |
| Docs | a9b0207b563aa25be17d4a635f6cc903fbe0e74a | 7e3dbd870bb10f13e8b5f1b5f3a8b401ac378910 | #79 C Recovery VM 보고 병합; #72 ba1b998 인계와 본 조사 후속은 main 미병합 |

- 최초 수집: Issue/PR 170개(일반 Issue55·PR115), 원격 branch20개, CI(Continuous Integration, 자동 검사) Run173개.
- 12:33–12:34 UTC 변경분: Issue/PR175개(일반 Issue57·PR118). 새 Issue Infra46·Docs78, 새 PR GitOps29/30·Docs79의 원 토론·소스·결과 연결.
- 현재 main 추적 파일: App396·Infra57·GitOps58·Docs73. 별도 열린 PR와 신규 수정·GitOps 보존 원본41파일도 검토 대상.
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
| Valkey Lab 설정 검사 | 대소문자·후순위 덮어쓰기·지원하지 않는 inline 댓글/escape를 잘못 승인 | fix/valkey-stage1-config-validation-20261007 @2c22e0acfc14568a971a3992128d027c0ce3911a. 보수적 literal 문법·정확 값/횟수/순서 검사. [GitOps21](https://github.com/seokpan/seokpan-hybrid-gitops/issues/21)·[GitOps6](https://github.com/seokpan/seokpan-hybrid-gitops/issues/6) 연결 |
| Recovery 설정 검사 | 같은 셸 문법 오해가 Recovery 검사에도 남음 | fix/recovery-config-validation-20261007 @fc3d95031945c1bbd3819c541409c7621dd7cd62. Lab parser 재사용·회귀2건, Lab 수정 선행 병합 필요 |
| Docs Windows 도구 | Windows 경로 구분자 및 기본 cp949 인코딩으로 검사 실패 | portable path0efe597·명시 UTF-8 17b9e203. 현재 브랜치에 포함, 기본 인코딩 환경14회귀PASS |
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
| Frontend UI 모의 시험 | 18Case를2회 반복=36PASS | 1280/390px 포함, 모의 API/WS. 실제 WSS·다중 Pod 시험 아님 |
| Infra 제어 흐름 반례 | 오류를 성공으로 기록하는 경로 재현 | 합성 셸/빈 Terraform Root. DB/AWS/SSH·실제 Plan 미접근 |
| Docs 그림·검사 | Source5·SVG12·PNG12·font12·CIDR9 무결성 PASS, PNG12·App SVG 및 댓글 PNG13 시각검토 | 기존 Git LF 사본. 새 Inkscape Render·실제 구축 결과판·Runtime PASS 없음 |
| CI 보존 자료 | 초기103ZIP+변경분 ZIP Hash/CRC·JUnit·Source 연결, bundle16·tar4 내부 대조 | tar571파일 모두 Git blob 연결. 제공하지 않는 로그와 삭제된 손상 payload는 아래 제한 |

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

- [GitOps26](https://github.com/seokpan/seokpan-hybrid-gitops/issues/26)에서 B 등록 개정 적용 조건, C 형식/GRANT·실제 접속·데이터 출처 수락, 실제 Route/Origin/TLS/WSS·Owner/사용창·Gate/live Diff와 지정 실행 경로 확인.
- 기존 승인 FE/BE Image는 App46e21 기반. App17/18/19와 새20/후속 수정의 Build/Scan/Digest·플랫폼/Pull·App 및 held Migration 동일 Image 연결 필요.
- Controller SQL/Valkey 금고 본체 해독 성공 보고 유지. 남은 것은 Controller 밖 독립 사본·복원 Identity 검사이며 새 키/공개키 전달 반복 없음.
- C Infra46/Docs79의 Recovery VM 생성·TLS/격리 준비 보고 수신. Server04의 Controller/복구VM 공통 Host 한계·실제 사본/15분 운영·복원계정/Data/업무·전체 RTO는 별도.
- ROSA 첫 실제 Plan은 B 목적 Caller/Backend·지원/Quota, A 제한 출력/prerequisite, C SG2, 예비 비용·현재 사용창 수락 후 지정 실행자1명으로 진행.

* 열린 본인 PR과 직접 순서

| PR | 검토 상태 | 다음 행동·순서 |
|---|---|---|
| [App20](https://github.com/seokpan/seokpan-hybrid-app/pull/20) | Draft/e348895, 승인0·같은 HEAD Linux 성공 | 본문에 이번 Artifact 검증 후속 반영→Ready→D/C 등 첫 리뷰→정확 HEAD/검사/승인 확인→squash. 새 시작/Chat PR은 독립 변경으로 뒤이어 통합 검사 |
| [Infra43](https://github.com/seokpan/seokpan-hybrid-infra/pull/43) | Draft/d5aeddd, 승인0·Source CI 성공 | Source 한정 Ready/첫 리뷰 가능. A Backend/List 권한·C Source 소비 관점 리뷰. 실제 Caller/Workspace는 병합 뒤 별도 |
| [GitOps25](https://github.com/seokpan/seokpan-hybrid-gitops/pull/25) | Draft/b30e978, 승인0·새 main CI 성공 | 이전 checker 실패/A 표기의 PR 본문 정정→Ready/첫 리뷰→squash. Lab 설정 수정 PR→Recovery 수정 PR 순서 |
| [Docs72](https://github.com/seokpan/seokpan-hybrid-docs/pull/72) | Ready, 승인0; 기존 ba1 인계에서 본 조사 소스 후속 | 최신 main/C 기록 포함 상태와 전체 diff 확인→현재 HEAD 첫 리뷰. 코드 PR들과 독립 Source 기록이며 main 병합 상태를 앞서 기록하지 않음 |

- App/Infra/GitOps main은 승인 최소1·새 push 뒤 이전 승인 무효화·squash만 허용하는 Ruleset 적용. 현재 네 PR 모두 제출된 승인0이므로 재승인보다 첫 리뷰 단계.
- Docs는 활성 main Ruleset 없음. 프로젝트의 사람 검토와 실제 수신을 생략하는 근거로 사용하지 않음.
- CI 성공과 review request 존재는 승인 아님. Ready 전환 뒤 발생한 새 Run도 같은 HEAD와 conclusion 확인.
- main/reference 및 열린 PR·후속 base 의존 branch 보존. squash 뒤 `--merged` 결과만으로 변경 미반영/삭제 가능 판정 금지. 필요한 patch/Run·고정 참조·개인 미push·실제 배포 revision 확인 뒤 사용자 삭제.

* 재검토 종료 범위와 다음 입력
- 현재 소스/시험→승인03/04→원 토론→과거 고유 변경→CI/산출물/보존 bundle→저장소 간 링크→새 원격 변경→수정 조합 재시험 순으로 재대조.
- 조회 가능한 자료의 마지막 추가 검토에서 새 미검토 변경과 새 결함이 없을 때 해당 관측 범위의 최초 조사를 종료. 고유 원문별 검토 근거와 정확 중복 연결은 로컬 coverage 기록으로 보존.
- 확인 불가: 초기 오래된/취소 Job 로그9건, Docs의 삭제된 손상 Base64 입력1건, 비공개 Harbor Layer/Runtime·보호 State/전체Output/SavedPlan·실제 개인 입력/금고/Cloud. 부재·권한 없음·성공으로 추정하지 않음.
- 1차 외부 저장소·공식 기술자료는 연결된 관련 범위만 대조. 4개 2차 저장소 밖 모든 인터넷 자료의 전수 검토를 주장하지 않음.
- 승인03/04 종료, DR10분·DB RPO30분·운영 Backup15분, CP3/Infra3/Worker3, Cost PARTIAL/$450계획/$500한도, TH81·기존 완료2, Q02/03/04/05/10 미완료 보존.
- 공개 Issue/PR 작성·댓글·리뷰 요청·Ready 전환·병합·branch 삭제는 사용자 작업. 소스 변경·검사·commit/push와 원 작업용 복사안을 구분해 인계.
- 증거: [Source 조사 Run](../evidence/T09/source-audit-20261007-01/summary.md)·[05 추가 기록](05_IMPLEMENTATION_AND_VALIDATION.md#repository-full-audit-20261007)·[Tracker](WORK_TRACKER.md#repository-full-audit-20261007).
