# 병합 소스의 ROSA·OCP 준비 검사

- 대상: Infra `6849c32d5b24a0e4994b7fbe849a1032211dc9a3`·GitOps `61edd0fd60e1004260c0b5082dc792fce847616b`. [실행 순서·직접 입력](../../../execution/ROSA_OCP_NEXT_ACTIONS_20261008.md).
- 환경: Windows 격리 사본, Core1.16.4/Git Bash5.3.9/Python3.12.14/Kustomize5.7.1. 개인 Controller·Cloud 인증·State/비밀값 미사용.
- PASS: ROSA fmt/helper 문법·기존 OIDC harness의 4개 Resource/정규화/versions/providers/variables/Lock 보존, Root 등록 SHA B 대조, 전체 lab release Gate. harness는 scoped source이며 전체 Root mock/실제 Operator 조회 성공이 아님.
- Lock SHA256: `72ab1002dca9b1de7df233e5af5c197e789186949cb53eb1273a73d68ef81f0b`. Git 저장소 LF 사본 기준, 과거 CRLF 작업 사본의 해시와 구분.
- Controller: 1차 인벤토리 대상 TCP22 연결 실패, SSH 로그인 미시도. 실패만으로 실제 VM 가동·인증·ROSA 권한 부재를 판정하지 않음.
- 한계: Controller live preflight/Backend·지원·실제 보호 입력/Cloud Plan·Apply·등록/Sync·전체 Runtime·공식 T01 및 RTO/RPO NOT RUN. 실제 배포/업무 보고 수신은 원 #26과 별도.
- 후속: B Controller·Caller/Backend/지원, A 기반/공통 prerequisite·목적 서비스 권한, C SG2, B/D 예비 비용/창 → 실제 첫 전체 Plan. OCP 후속과 병행.
