<!-- 작성자: 최유준 / 작성 날짜: 2026-10-14 -->
# Run Summary — T21 / Jenkins Build #11 (Build·Scan·Smoke)

이 Run은 Jenkins `hybrid/image-pipeline/main` Build #11의 실제 수행 기록이다. Source 반영의 증거이며 Runtime·배포 수락이 아니다(0 Replica, 미확정 Namespace/DB/Valkey/Secret 보류).

## Identity and Scope

- Test / Case / Requirement / Run / Release: T21 / 세부 Case·Requirement ID 미지정 / `jenkins-build-scan-smoke-20261014-01` / GitOps Release 없음(PROMOTION_MODE=OFF, `gitops_change=NONE`)
- 대표 Issue / PR / 이전 실패·후속 Run: 등록 Issue #129 / 관련 병합: seokpan/seokpan-hybrid-app#48(`0087bc1`)·#49(`c2dad25`)·#51(`d037a55`), seokpan/seokpan-hybrid-gitops#47(`707474c`) / 이전 실패 Run 없음. 후속 Run은 `jenkins-promotion-remote-check-20261014-01`(#12), `jenkins-promotion-write-20261014-01`(#13). 이전 실제 경로 Run #9(WRITE, gitops PR #40, App #15)는 이번 범위와 구분한다.
- 환경·대상 / Source·Image·입력/도구 개정: Jenkins Build #11, 파라미터 `ENABLE_ECR=true`, `PROMOTION_MODE=OFF`, Jenkins Run ID `a09-11-c2dad254cc40`. App `c2dad254cc407431092691f9ea5892f8324f1520`(main). Candidate tag `scan-c2dad254cc40-11`, Final tag `git-c2dad254cc40`. backend `sha256:733f52a6f5a53c31e792cbe1d254221ff8ff86828e8c3afdc65d207e2e5fb18d`, frontend `sha256:7068a36f55427639b7b7bf8a9c5795689b891e7ec334bfd306d8cd03c5f049ff`(Harbor=ECR, linux/amd64). Scan 도구·규칙 개정은 이번 기록에서 확인하지 못했다(미확인).
- 배정 실행 책임자 / 실제 수행자 / Reviewer / 협업 내용: 정태훈 / 최유준 / 최유준 / D(Registry) 수신 확인 대기
- 실행 조건·부하·장애 주입 / 대상외 항목과 이유: 부하·장애 주입 없음. T21의 다른 Case(캐시 없는 새 Worker의 새 Pull, 12시간 이상 지속 사용 후 새 Pull, 재생성 후 Pull, No CI Token 복사 확인)는 이 Run에서 수행하지 않았다(NOT RUN).

## Results

- Render: NOT RUN
- Deployment: NOT RUN
- Acceptance: NOT RUN
- Baseline / Target / Actual / 단위·집계 조건: Baseline·Target 없음. Actual은 `metrics.csv`(Build 전체 517초 등, 단일 Run).
- 대표 업무·Data 일관성 / 실패·제한: 모든 Stage가 Success였다. 이 Run에서 새로 수행한 항목은 P1 재검증(Backend verify·OpenAPI export·Frontend verify·Browser UI/Full), Image Build·Push(Harbor+ECR), Harbor Candidate Scan(backend·frontend 모두 `critical:0,high_fixable:0`), Candidate Health Smoke(backend·frontend `PASS_PROCESS_SMOKE`), Harbor→ECR Final Promote, Final Digest 검증(Harbor·ECR Digest 동일). Smoke는 `/health/live` HTTP 200 확인뿐이며 업무 기능 검증이 아니다. Harbor Candidate tag는 정리(`OK`)됐고 ECR Candidate tag `scan-c2dad254cc40-11`은 남아 있다(`candidate_tag_retained=true`, ECR 수명 정책은 seokpan/seokpan-hybrid-infra#18에서 별도 추적).
- 실제 시작/종료 UTC / 같은 시각의 KST / 시계·시점 불확실성: 시작 2026-10-14T02:59:20Z / 2026-10-14T11:59:20+09:00, 종료 2026-10-14T03:07:57Z / 2026-10-14T12:07:57+09:00. 시작은 Jenkins 표시값(UTC)이고 종료는 시작+소요(8분 37초)로 계산한 값이다. Stage별 절대 시각은 기록하지 않았고 소요시간만 `timeline.csv`에 남겼다.

## Evidence and Recovery

- metrics.csv / timeline.csv / checksums.txt: 이 폴더의 파일. checksums.txt에는 이 폴더의 공유 가능한 파일(image-metadata.json 포함)의 SHA-256을 기록한다.
- 보호 Raw 논리 참조 / 보관자·접근·보존 책임 / 가용성·무결성: `image-metadata.json`은 Jenkins Build #11 아카이브 artifact의 사본이다. console log·Pipeline Steps는 Jenkins 내부 `http://jenkins-controller.cicd.svc.cluster.local:8080/job/hybrid/job/image-pipeline/job/main/11/`를 논리 참조로 하고 Git에 올리지 않는다. 콘솔 로그에서 `github_pat_` 문자열을 검색했으나 검출되지 않았다(0건). 로그 원본은 Git에 올리지 않는다. 보관자·보존 기간 [확인 후 기입]
- Backup ID·암호문 Hash·Data 기준 시각/확인 수준: 해당 없음(복구 시험 아님)
- 장애/판단·Dump·복원·업무 재개 단계 / RTO·RPO와 계산 근거: 해당 없음
- 영속 Data 손실 / 새 Redis Runtime 손실: 해당 없음

## Follow-up

- 원인·조치 / 수정 Commit·입력 개정: 실패 없음. Scan 도구·규칙 개정 확인 [확인 후 기입]
- 현재 부분 State·자원·Lock·잔존 비용 / 정리·다음 인계: ECR Candidate tag 잔존(수명 정책 별도). Promotion은 후속 Run #12(점검), #13(PR 생성)에서 다룬다.
- 영향받는 재시험·다음 Run / 담당·필요 시점: 정태훈·D 확인 후 Run 분할·판정 범위 확정. 후보 상태는 INCOMPLETE 유지.
