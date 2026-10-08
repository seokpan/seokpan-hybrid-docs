# Recovery Host Source 검증·Controller 확인 — 2026-10-08

* 변경과 원 작업

- [GitOps #31](https://github.com/seokpan/seokpan-hybrid-gitops/pull/31), 원 작업 [GitOps #10](https://github.com/seokpan/seokpan-hybrid-gitops/issues/10)·[Infra #46](https://github.com/seokpan/seokpan-hybrid-infra/issues/46).
- HEAD `6c3de8d75f12754ece2cfeb9a1347de66e8cbafe`. Recovery EXPECTED_HOST를 `192.168.54.60`으로 반영하고 기존 Host 기대값 1곳 정정. 2파일·2줄 변경.
- base/lab/Cloud·Root targetRevision·Migration 및 Recovery의 다른 입력/replica 보류 유지. C/D 리뷰 요청, 승인·병합 대기.

* 검증 결과

- [정확 HEAD의 Linux CI](https://github.com/seokpan/seokpan-hybrid-gitops/actions/runs/37716571091): Job113114271158, Source 시험 69/69 PASS·Render 검사 PASS.
- 로컬 Host 시험과 base/lab/Recovery Render PASS. base/lab Render는 기존 main과 동일. Kustomize5.7.1 사용.
- Windows UTF-8 사본 전체69건은64PASS/5FAIL. 기존 CRLF 비교2건·POSIX 실행 파일 제약3건. 최초62PASS/5FAIL/2ERROR 중 cp949 오류2건은 UTF-8 실행에서 분리·해소. 실패 이력은 Linux PASS와 별도 보존.
- Recovery release Gate는 남은 입력 때문에 BLOCKED(exit2), 실행용 출력 생성 없음. Source PASS를 실제 DB 연결·복원·배포 수락으로 사용하지 않음.

* Controller 검사 결과 수신

- 수행 환경 `jth@ansible`, 실행 주체 B. 기존 SSH 세션과 CA 읽기 가능 확인 후 Python 해시 대조 결과 수신.
- C 공개 CA 원본의 전체 파일 SHA-256 `0d6b4a51439a58c722100265ac43e3f7f39b2d0f44bdb2d23f9d4bb87dfbb4ab` 일치 PASS.
- Terraform/AWS CLI/jq 존재 확인, 실제 버전 대조 대기. ROSA/OCM CLI 미설치, RHCS_TOKEN 미설정. 인증·구독·Quota·Backend/Caller·Cloud Plan은 미확인.
- 이 기록 작성 환경의 직접 Controller 접속·CA 재조회 결과가 아님. 실제 검사 시각은 수신 출력에 없어 null 유지. CA 원문·Token·State/Plan은 기록하지 않음.

* 다음 입력·한계

- Namespace 확정 후 Recovery `backend-database-ca` 공급. CA 일치만으로 ConfigMap 생성·TLS 연결 완료 처리 없음.
- RHCS 인증과 Classic 공식 정책 조회는 B, Account Role4·목적 권한/기반 실제 공급은 A의 Infra #47/#23, Data SG2는 C/A #19. Plan은 이 입력 및 비용·Owner/창 수락 후 진행.
- C의 Infra #48 Data 예행은10/9, 전체 Recovery 업무/RTO 검증은 별도10/19–21 창. Restore·장애·삭제·유료 생성 미실행.
- 03/04 종료·DR10분/DB RPO30분/운영 중Backup15분·CP3/Infra3/Worker3·Cost PARTIAL/$450 계획/$500 한도·TH81/기존 완료2·Q 미완료 유지.
