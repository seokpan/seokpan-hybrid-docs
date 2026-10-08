# Red Hat 정책 조회 부분 검증 — 2026-10-08

- 판정: API 인증·Classic 필수 정책 5/5 조회·보호 사본 생성 성공. 전체 T03·ROSA 준비·Plan 완료 아님.
- 실제 실행자: tjung03, 기존 Controller의 jth@ansible. Windows → vroute-01 → SSH Controller → jth 경로.
- 원본: [Infra25 실행 결과](https://github.com/seokpan/seokpan-hybrid-infra/issues/25#issuecomment-6053637165). 실제 Controller 출력 수신 기록이며 이 문서 작성 환경에서 Runtime를 재조회한 결과 아님.

## 수행·결과

| 항목 | 실제 결과 | 아직 확인하지 않은 부분 |
|---|---|---|
| Red Hat API 인증·현재 계정 읽기 | PASS | 프로젝트 Red Hat 조직 선정·AWS 연결·구독/지원 권한 |
| Classic Account 정책 | 권한 정책 4개 + Support Trust, 총 5/5 확보 | 실제 Role/Trust·Policy ARN·기존 자원/State 관리 주체 |
| Operator 정책 | 제공 7/8 | 누락 ID 확인·실제 Classic Role 목록과 A의 Policy Map 대조 |
| OCM 참조 정책 | 제공 4/4 | OCM Role 생성·조직/AWS 연결·유효 권한 |
| 보호 사본 생성 | 폴더700/파일600 생성 결과 | 현재 소유자/권한·파일 해시 재대조·A 보호 인계/수신 |

논리 참조는 `rosa-policy-20261008T061153Z-6caf4295`. Token·계정 프로필·정책 원문·전체 State/Output/Plan·실제 보호 경로는 공개 파일 제외. Controller의 조회 기록은 2026-10-08T06:11:53Z(15:11:53 KST)이며 시계 동기화와 전체 호출 시작/종료 시각은 미검증.

처음 Token 미등록 시도는 `BLOCKED: RHCS_TOKEN_MISSING`, 정책 조회·사본 생성 미실행. 같은 jth 세션에 값을 화면 표시 없이 재등록한 뒤 성공. Token은 해당 셸 환경변수로 공급했으며 코드·argv·보호 정책 사본에 값을 저장하지 않음. Token 권한이 읽기 전용이라는 판정은 아님.

## 후속 검사·한계

저장 사본만 읽는 checker의 Python3.9 문법 검사와 합성 사본 7개 검사 통과. 정상 사본·변조·경로 이탈·필수 파일 누락·미등록 파일·잘못된 해시·Operator 목록 불일치 처리 확인. Windows 검사이므로 Controller 실제 소유자/권한·사본 무결성 결과로 사용하지 않음. manifest와 파일이 함께 바뀐 경우의 외부 원본 진위 증명이나 독립 서명 검사는 아님. 실제 누락 정책 ID는 아직 null.

## 다음 입력·실행 경계

1. B: 저장 사본의 현재 권한/해시·누락 정책 ID 확인 후 A #47 보호 인계.
2. A: 공식 정책 소비·기존 실제 IAM 자원과 State 주체 확인·공통 Role4/Policy/목적 권한 구현·리뷰·승인된 실행·제한 출력 공급.
3. C/A: 서로 다른 실제 Data SG2 공급, B 수신 대조.
4. B: Controller clone/원격/Lock·목적 Caller/Backend·지원 stable4.20 GA patch/구독/Quota·Worker disk·예비 비용/Owner/사용창 수락 후 첫 전체 Plan.

정책 조회를 반복하지 않음. 이번 Run에서 AWS/IAM 변경·Terraform·ROSA 생성·OCP Sync·DB 접속/복원 미실행. T03 전체·TH81/기존 완료2·Q 미완료·Cost PARTIAL/$450 계획/$500 한도·CP3/Infra3/Worker3·DR10/30/15 유지. D의 Index 수신은 별도 대기.
