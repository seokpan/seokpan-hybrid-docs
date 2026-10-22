<!-- 작성자: 최유준 / 작성 날짜: 2026-10-14 -->
# Run Summary — T21 / Jenkins Build #13 (Promotion WRITE)

이 Run은 같은 App SHA의 기존 Final Image를 재사용하고 Promotion PR 2건을 생성한 기록이다. **Scan·Smoke의 신규 수행 근거가 아니다**(근거는 Build #11 Run). Source 반영 증거이며 Runtime·배포 수락이 아니다(0 Replica, 미확정 Namespace/DB/Valkey/Secret 보류).

## Identity and Scope

- Test / Case / Requirement / Run / Release: T21 / 세부 Case·Requirement ID 미지정 / `jenkins-promotion-write-20261014-01` / GitOps Release 2건(아래 PR). `release.json`의 `release_id`는 1건만 담을 수 없어 null로 두고 `review_refs`에 연결했다.
- 대표 Issue / PR / 이전 실패·후속 Run: 등록 Issue 129 / seokpan/seokpan-hybrid-gitops#48 Recovery `rel-recovery-20261014T034648Z-c2dad254cc40-4809c8fc`(병합 `0aec2bb`), seokpan/seokpan-hybrid-gitops#49 Cloud `rel-cloud-20261014T034654Z-c2dad254cc40-55ad5f3b`(병합 `19d3387`), 두 PR 모두 정태훈 승인. 관련 병합: seokpan/seokpan-hybrid-app#48(`0087bc1`)·#49(`c2dad25`)·#51(`d037a55`), seokpan/seokpan-hybrid-gitops#47(`707474c`) / 이전 Run `jenkins-promotion-remote-check-20261014-01`(#12). 이전 실제 경로 Run #9(WRITE, gitops PR #40)는 이번 범위와 구분한다.
- 환경·대상 / Source·Image·입력/도구 개정: Jenkins Build #13, `ENABLE_ECR=true`, `PROMOTION_MODE=WRITE`, Jenkins Run ID `a09-13-c2dad254cc40`. App `c2dad254cc407431092691f9ea5892f8324f1520`. 기존 Final(`git-c2dad254cc40`)을 재사용했다. backend `sha256:733f52a6f5a53c31e792cbe1d254221ff8ff86828e8c3afdc65d207e2e5fb18d`, frontend `sha256:7068a36f55427639b7b7bf8a9c5795689b891e7ec334bfd306d8cd03c5f049ff`. GitOps 기준 SHA(고정) `707474cde830e2a7942a2ae6d08fbe2e837fe478`. PR 병합 SHA는 짧은 형태만 확인했으며 전체 SHA [확인 후 기입].
- 배정 실행 책임자 / 실제 수행자 / Reviewer / 협업 내용: 정태훈 / 최유준 / PR 승인 정태훈, Evidence Reviewer 최유준 / D 수신 확인 대기
- 실행 조건·부하·장애 주입 / 대상외 항목과 이유: 부하·장애 주입 없음. Candidate Build·Scan·Smoke·Promote는 기존 Final 재사용으로 생략됐다. T21의 다른 Case(캐시 없는 새 Worker의 새 Pull, 12시간 이상 지속 사용 후 새 Pull, 재생성 후 Pull, No CI Token 복사 확인)는 이 Run에서 수행하지 않았다(NOT RUN).

## Results

- Render: NOT RUN
- Deployment: NOT RUN
- Acceptance: NOT RUN
- Baseline / Target / Actual / 단위·집계 조건: Baseline·Target 없음. Actual은 `metrics.csv`(Build 전체 451초 등, 단일 Run).
- 대표 업무·Data 일관성 / 실패·제한: 모든 Stage가 Success였다. Scan·Health Smoke 값은 `SKIPPED_EXISTING_FINAL`이며 신규 수행이 아니다. P1 재검증은 이 Run에서도 다시 수행되어 Success였다. Promotion은 Recovery·Cloud 각각 `--remote-check` 점검 후 `--write`를 실행했고, 그 결과로 PR #48·#49가 생성·병합됐다. 점검 단계의 Cloud release-id(`rel-cloud-20261014T034645Z-c2dad254cc40-f683cc1a`)는 PR 생성에 쓰인 id와 다르며, PR의 release-id를 정본으로 기록한다. Pipeline 마지막 메시지의 `gitops_change=NONE`은 image-metadata.json의 값이며 Promotion 결과를 뜻하지 않는다. 후보는 INCOMPLETE를 유지한다(누락 입력 `SOURCE_COMMITS,CONFIGURATION_REVISIONS,RENDER_AND_REVIEW`).
- 실제 시작/종료 UTC / 같은 시각의 KST / 시계·시점 불확실성: 시작 2026-10-14T03:39:31Z / 2026-10-14T12:39:31+09:00, 종료 2026-10-14T03:47:02Z / 2026-10-14T12:47:02+09:00. 시작은 Jenkins 표시값(UTC), 종료는 시작+소요(7분 31초) 계산값이다. 두 PR release-id 타임스탬프(03:46:48Z, 03:46:54Z)가 이 Run 구간 안에 있어 시각 표기를 교차 확인했다. PR 병합 시각은 기록하지 않았다 [확인 후 기입].

## Evidence and Recovery

- metrics.csv / timeline.csv / checksums.txt: 이 폴더의 파일
- 보호 Raw 논리 참조 / 보관자·접근·보존 책임 / 가용성·무결성: `image-metadata.json`은 Jenkins Build #13 아카이브 artifact의 사본이다. console log·Pipeline Steps·`promotion-result-*.txt`는 `http://jenkins-controller.cicd.svc.cluster.local:8080/job/hybrid/job/image-pipeline/job/main/13/`를 논리 참조로 하고 Git에 올리지 않는다. 콘솔 로그에서 `github_pat_` 문자열을 검색했으나 검출되지 않았다(0건). 로그 원본은 Git에 올리지 않는다. 보관자·보존 기간 [확인 후 기입]
- Backup ID·암호문 Hash·Data 기준 시각/확인 수준: 해당 없음
- 장애/판단·Dump·복원·업무 재개 단계 / RTO·RPO와 계산 근거: 해당 없음
- 영속 Data 손실 / 새 Redis Runtime 손실: 해당 없음

## Follow-up

- 원인·조치 / 수정 Commit·입력 개정: 실패 없음
- 현재 부분 State·자원·Lock·잔존 비용 / 정리·다음 인계: GitOps main에 Promotion 2건이 병합된 상태. 실제 배포·Sync는 수행하지 않았다.
- 영향받는 재시험·다음 Run / 담당·필요 시점: 배포 수락은 별도 Run(Namespace/DB/Valkey/Secret 확정 이후). D 수신 확인·정태훈 확인 대기.
