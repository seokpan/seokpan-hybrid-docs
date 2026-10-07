# 최초 저장소 Source 조사 Run — 2026-10-07

* 판정
- 현재 Source·원 토론·고유 이력·CI/산출물·그림·연쇄 링크 조사와 수정 조합 검증. 공식 T09/T18 Acceptance·Runtime·전체 종료 판정과 별도.
- 상세 변경·발견·우선순위·원 Issue·열린 PR·사용자 후속은 [종합 조사](../../../execution/REPOSITORY_AUDIT_20261007.md) 참조.
- Git 기록 계정 tjung03. 실제 시험 환경 Windows의 격리 Python/Bash/Node 및 GitHub Actions Linux. 사람 리뷰 미수신.

* 실제 결과
- App20 정확 Linux HEAD: 기본1774·부분집합47·소유 Redis7.2.4 Lua9PASS. Artifact11474896267 ZIP Hash/Digest/CRC·JUnit·Source 연결 후속PASS.
- App20+개발시작+Chat구독 소스 조합: 관련174PASS·Ruff223/mypy119PASS. 조합 Linux 전체CI·새Image·실제Valkey 미실행.
- GitOps25 b30e978 Linux CI37624059074:69PASS. Artifact11483631189 ZIP SHA256=d195af5782e0d61b33083146e210729f4597b82c669d08269e363f705ed162f2,CRC/Digest/내부Hash/SourceTree·LF8Render26객체 대조PASS.
- 등록+Lab+Recovery 설정 검사 조합73건:70PASS/기존WindowsPOSIX시험3FAIL. 실패 숨김/skip 정책 변경 없음. 새 조합 Linux 전체CI 미실행.
- Frontend 고정 main: generated API/도구81/unit269/buildPASS, UI18Case2회 반복36PASS. 모의API/WS·1280/390px 포함, 실제Backend/Route/nginx 검증 아님.
- Docs Windows기본cp949 환경14회귀 및 Recovery지표16시험PASS. 기존 Source5/SVG12/PNG12/font12/CIDR9무결성,PNG12·AppSVG·댓글PNG13시각검토.
- Infra의 Import·비교·RDS 제어 실패 판정은 합성반례 재현. 실제DB/AWS/SSH 실행 없음.

* 실패와 확인 불가
- 기존 App Windows 전체 실패와 baseline 재현은 [앞선Run](../provider-cleanup-20261007-01/summary.md)에 보존. 당시 ZIP403은 이력이며 이번 독립 다운로드 성공으로 후속 연결.
- 오래된/취소Job로그9개·삭제된 손상Base64입력1개는 원문 검토 불가. 비공개HarborLayer/실제Cluster/보호키·State/Output/Plan·본인실제입력은 미접근.
- GitOps main은 이미Stage2 SHA B/FE·BE1소스, 마지막수신Runtime은SHA A/FE·BE0. 소스병합으로실제등록/Sync완료를추정하지않음.

* 다음 입력
- 사용자: 본문현행화·Ready/사람리뷰·동일HEAD검사·병합·필요한브랜치정리. 공개Issue/PR쓰기 미실행.
- C/A: Infra44/45 실패차단 보완·실제Data/SG2/제한출력. D: 필요한App수정반영새Build/Scan/Digest·플랫폼/Pull.
- B/D/C: Stage2 원GitOps26의DB형식/GRANT/출처·Route/Origin·Owner/사용창/Gate/liveDiff 수락과지정실행자.
- 독립사본/복원Identity·ROSACaller/Backend/지원/Quota/비용은기존보호Workspace에서별도. 성공한키전달·본체해독·선택Sync반복없음.
- RTO/RPO=null,TH81/기존완료2,Q미완료,CostPARTIAL 보존.

* Source Run 무결성 후속
- 최초702fb88의 CSV/JSON3파일은 생성 시 CRLF Hash와 Git LF 바이트가 달라 체크섬 불일치. 데이터 값·시험 결과는 동일하며 LF 바이트로 정규화 후4파일 체크섬 재검증.
