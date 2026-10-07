# T09 준비의 Source 구독 오류 처리 부분 Run — provider-cleanup-20261007-01

- [x] App #4 W10 후속의 결함 재현·좁은 수정·관련 검사
- [x] 정확 PR HEAD의 기존 Linux 정식 정책·별도 Lua 검사 성공 확인
- [x] Windows 실패 및 원 main 별도 사본의 같은 실패 보존
- [ ] App #20 사람 리뷰·병합, D 새 Build/Scan/Digest 및 B 소비 수락
- [ ] 실제 Valkey·lab/ROSA·WSS/전체 T09 Acceptance

배정 책임은 B 정태훈(tjung03), 실제 Source 작성·로컬 실행·기록은 Codex다. Linux 실행은 GitHub Actions ubuntu-24.04 runner이며 Codex가 원 Job/Step 로그를 읽었다. GitHub 게시 주체 tjung03과 실제 실행자를 구분한다. D/팀원의 직접 실행·리뷰·수신 완료로 기록하지 않는다.

## 문제·Source·변경

[원 App #4](https://github.com/seokpan/seokpan-hybrid-app/issues/4), [App #19의 D 비차단 의견](https://github.com/seokpan/seokpan-hybrid-app/pull/19#pullrequestreview-5438977533)을 이어 [App Draft #20](https://github.com/seokpan/seokpan-hybrid-app/pull/20)의 `e3488953b0f51b1a54dc7899a8a57c8024c54c13`를 검사했다. 부모는 main `a2afffb8605dafff1cb5b9af215aa0cf93aadcdb`다. `_subscribe`의 subscribe/버전 읽기 실패 뒤 `aclose`도 RedisError를 던지면 기존 RealtimeUnavailable 변환이 가려진다. Provider 오류 처리 분기의 정리 RedisError만 `suppress`로 감싸고 기존 `REALTIME_PROVIDER_UNAVAILABLE` 변환을 유지했다. 기존 CancelledError 전파·정상 구독·API/Schema/Pool/배포 선언/Lock은 변경하지 않았다.

승인 근거는 03 §3-E.7/12/14/15와 §3-G T09, 04 §5.4/§6이다. 이 Run은 T09 준비의 합성 Source 오류 경계 검사이며 실제 다른 Pod 재접속·Snapshot·WSS 시험이 아니다. IF-11/T09 전체 PASS를 부여하지 않는다.

## 실제 결과

| 실행 | 결과·조건 |
|---|---|
| 원 main 제품 코드 + 새 경계 검사 | 20Case 중 14PASS/6FAIL. 기존 취소8 + 새 Provider12. 실패6은 Lobby/Room × subscribe/버전/잘못된 버전 × cleanup RedisError이며 실패 Run을 보존했다 |
| 수정 후 관련 검사 | 같은20 + 기존 Adapter8 = 28PASS. cleanup 1회 시도·안전한 오류코드·예외 cause/context 억제·기존 취소 전파 확인 |
| 로컬 Windows 기존 정식 정책 | Lock/sync/format/lint/mypy PASS. 전체 수집1774, pytest 보고1768PASS/1FAIL/4SKIP/2ERROR, 180.28초. 오류2는 동일 긴 매개변수 Case의 setup/teardown이므로 서로 다른 시험2건으로 합산하지 않는다. 실패로 종료해 후속 domain coverage/runner 단계 NOT RUN |
| Windows 원 main 별도 코드 사본 | 선택7Case에서 메트릭1FAIL과 긴 이름 setup/teardown2ERROR가 동일 재현. 제품 수정 때문에 새로 발생한 것으로 분류하지 않는다. 메트릭은 process_cpu_seconds_total 미제공, 오류는 Windows 환경변수32767자 제한. TLS4 skip은 해당 로컬 PATH의 OpenSSL 미발견이며 검사/skip 정책을 변경하지 않았다 |
| 정확 HEAD Linux [CI37605414615](https://github.com/seokpan/seokpan-hybrid-app/actions/runs/37605414615) | 기존 정식 정책 PASS: Backend1774/92.91초·runner47/0.60초, 별도 소유 Redis7.2.4 Lua9/1.38초. runner47은 기본suite 부분집합으로 합산하지 않는다. JUnit/coverage 검증과 최종 git diff 불변 Step 성공을 원 Job112739564454 로그로 확인했다 |

도구는 Python3.13.15·uv0.12.5·pytest9.1.1·redis-py8.1.0·Ruff0.16.5·mypy2.3.1, 기존 uv.lock Blob=`bda7c5d967997f5e5475c211b375b1967b947704`를 유지했다. Windows 정식 정책의 `commit=a2afffb8605dafff1cb5b9af215aa0cf93aadcdb`, `dirty=true`, `source_sha256=76db368d5637688163f1ff27480fde75cc2e4e2b1ba2dec88da7ea9e6fbf265a`는 커밋 전 수정 작업 트리를 가리킨다. 이를 clean main 검사로 기록하지 않는다. 이후 제품/시험2파일만 커밋한 PR HEAD와 Linux checkout SHA가 일치한다.

CI Artifact11474896267의 서버 메타데이터는 64914bytes·digest `sha256:12b29014bb9f47acc520e44e5b8baccddc270fb8490e27d4e0ee0cbc2cd158b8`·head_sha=e3488953b0f51b1a54dc7899a8a57c8024c54c13다. 재사용 다운로드 참조의 로컬 접근은 HTTP403으로 실패해 ZIP bytes/CRC/Artifact 내부 summary·JUnit의 독립 다운로드 검증은 **NOT RUN**이다. 위 결과 근거는 원 Job/Step 로그와 기존 Workflow의 보고서 검사 성공이며 메타데이터 digest를 독립 계산값으로 주장하지 않는다. 임시 URL은 기록하지 않는다.

## 재개 delta·직접 입력·보고 수신

시작과 원격 종료 대조에서 네 main은 사용자 기준 그대로였다: App `a2afffb8605dafff1cb5b9af215aa0cf93aadcdb`, Infra `36dc2403aa77e2896cc4ec3c545b92e0afb49205`, GitOps `a25172c7453b9d7999cb1f3cbeb1ef35774e3b63`, Docs `a9b0207b563aa25be17d4a635f6cc903fbe0e74a`. 순차 조회이며 원자적 Snapshot으로 주장하지 않는다. Docs #72는 open/미병합 HEAD `b2bd48e3bf420a7d9374465a09608ee9d6f59dc6`, GitOps Draft #25는 `60643111f45a4a6cf66788551308fcf566ded4ea`, Infra Draft #43은 `d5aeddd4ca36f9c4265954d21507bd6a35264827`다. #25 CI37599479178, #43 CI37599480959의 새 success도 확인했으며 리뷰 없음·미병합 Source와 main 상태를 구분한다.

현재 Windows 작업 경로는 시작 시 비어 있어 새 clone4개를 생성했고 처음 개인 변경은 없었다. 다른 PC/Controller clone·개인 변경·State/키는 조사하지 않았다. AGENTS.md 검색은 이 네 clone에서 없음. 실제 Git2.54.0.windows.1·Node24.19.0·Bash5.3.9·PowerShell7.6.5, 번들 Python3.12.14와 이 작업용 고정 Python3.13.15/uv0.12.5를 구분한다. Terraform/AWS/ROSA/oc/kubectl/age/Docker는 현재 PATH 미발견이다. ROSA Lock Blob668098ad0f1e293982e9bcf8e931128346a00049는 main과 일치하며 AWS6.67.0/RHCS1.7.7을 읽었다. Cloud Caller/Backend/지원/Quota·A/C 보호 입력·실제 사용창은 확인하지 않았다. ZIP 지침과 별도10/7v3 지침은 텍스트가 동일했다. 외부 v4 helper의 Controller 실파일은 미확인이다.

[D 보고 수신 원 기록](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5#issuecomment-6035851057)에서 등록/Valkey4객체 Sync6034601393·ImageID/UID6034590906·DB Secret 공급6034843156을 보고 범위로 받았다. 성공한 등록/Sync를 반복하지 않았고 Runtime 재조회/전체 PASS를 하지 않았다. Stage1 Workload/등록 targetRevision=244b48b885d7ac645c402e561a032ae65a8f3461, Valkey1·FE/BE0·Migration suspend, base/Recovery hold를 유지한다. DNS/Hostname·TLS/AUTH·Ready·Prune/Delete·Owner/사용창·Gate/live Diff/수동경로 근거/수락은 남는다. Stage2는 GitOps #26이며 DB 실제접속/C 형식·GRANT·데이터 출처, Route/Origin·새 Image와 전체 Gate가 남는다.

Controller Valkey/SQL 금고 본체 해독 성공 보고는 유지하고 독립 매체/복원 Identity만 별도 미완료다. 새 키/공개키 공급·복호화를 반복하지 않았다. ROSA 실제 실행과 유료 생성, Restore/장애/삭제를 하지 않았다. DR10분/DB RPO30분/Backup15분·CP3/Infra3/Worker3·Cost PARTIAL/$450계획/$500한도·TH81/기존 완료2·Q 미완료는 그대로다.

## 원본 보관·한계·다음 입력

로컬 합성 JUnit/Windows 전체 로그는 이번 작업 Workspace에 보존했다. 공개 기록에는 값 없는 판정과 다음 논리 참조/비민감 파일 SHA256만 남긴다. 키/Token/비밀번호/kubeconfig/State/전체Output/Saved Plan은 읽거나 업로드하지 않았다.

- `local:app4-before-junit` SHA256=`0bbeaea8b2c3932c7a04711d5a717c52778b12b0d5d45ee629d8fe1e7b700c8b`
- `local:app4-focused-after-junit` SHA256=`a79088368f7ca3170f73e58f69ed8eb6a061b5c2fb1a19931b2c4e1ec5a9a0a1`
- `local:app4-windows-full-summary` SHA256=`bca62af8418f4ca71a21aeb3f8dcd613295e16d662d4c9560720790e192355c6`
- `local:app4-windows-full-junit` SHA256=`a45ebbb3002267ad12272c36d7b5448568ac6a93bb48c27daf40a876ee04fec1`
- `local:app4-windows-baseline-junit` SHA256=`bf7a63b906679bea753b7de53d7e4bcab4e40df4e49c9a38a6bcebde723f7405`
- `local:app4-windows-full-log` SHA256=`8e15aeaa4e97b1cf9653b4539e9637f81e523fd73014ca1a4dfaebb0a3500884`

다음은 D/C 사람 리뷰→App #20 실제 병합 Source 수신→D Backend Build/Scan/Digest·플랫폼·Registry/Pull 인계→B App/별도 held Migration 소비 검토다. App17/18/19의 기존 병합 조합과 이번 미병합 수정의 Image를 구분한다. 이 Source 수정은 그 공급 개정을 추가하며 기존 승인 Image를 새 Source로 승계하지 않는다. Evidence Index 담당 D에게 링크를 제출하며 D 수신/수락은 아직 확인 전이다. 전체 S1/Q10·Runtime/Cost/TH/T 완료 체크를 가산하지 않는다.
