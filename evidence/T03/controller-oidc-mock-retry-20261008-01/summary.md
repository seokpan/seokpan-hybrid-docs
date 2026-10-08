# Controller OIDC mock 입력 교정
- 최초 준비 명령의 -var-file=tests/oidc_mock.tfvars.json 누락 확인. 저장 로그의 필수 입력 오류7개로 실제 원인 대조.
- 실제 B/jth@ansible에서 같은 초기화된 harness·합성 입력으로 mock 시험만 재실행. exit0·issuer_without_scheme/issuer_with_https_scheme 각각PASS·2passed/0failed, 오류없음.
- 원 Source/harness/Lock/최초 로그 보존 PASS. 새 보호 로그·receipt의 논리 참조와 SHA256만 기록.
- 고정 c5d8 Source의 격리 정적·모의 준비 차단 해소. 실제 목적 Caller/Backend·공통 IAM/ARN·지원/Quota/Cloud Plan 성공을 뜻하지 않음.
