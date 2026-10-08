# T03 / controller-base-caller-mfa-20261008-01

## 수행·범위

- 실제 수행자: B / jth@ansible. 실행 시각은 별도 제공되지 않았으며 수신 시각과 구분.
- Source: ef424da0a6bfcdd56079ab5be249f429fa0b9c36. ROSA Lock: 668098ad0f1e293982e9bcf8e931128346a00049.
- 전체 T03: PARTIAL. 이번 한정 읽기 판정과 실제 목적 Role/Backend/Cloud Plan 수락 구분.

## 수신 결과

- BASE_READ_SCOPE_GUARDS: PASS
- AWS_BASE_CALLER_AUTH: PASS
- AWS_BASE_CALLER_KIND: IAM_USER
- PROJECT_ACCOUNT_LIMITED_OUTPUT_MATCH: NOT VERIFIED / A input not received
- CURRENT_SOURCE_B_TRUST_PRINCIPAL: MATCH
- AWS_OWN_MFA_READ: PASS
- AWS_OWN_MFA_DEVICE_COUNT: 1
- MFA_DEVICE_SELECTION_OTP_COMPATIBILITY: NOT VERIFIED
- MFA_AUTHENTICATED_SESSION: NOT VERIFIED / device read only
- ROSA_PURPOSE_ROLE_BACKEND_SERVICE_PERMISSIONS: NOT VERIFIED

## 판정 한계

- 로컬 Role/MFA 프로필0은 실제 IAM Role 부재·MFA 미등록 판정이 아니다. 현행 tf-session.sh는 기본 IAM User와 서버 MFA 장치를 조회한다.
- 기본 Caller 인증·Source Trust 대상 일치·MFA 장치 존재를 MFA 인증 세션·ROSA 서비스 권한으로 승계하지 않는다. 기대 Account 제한 출력과 실제 목적 Role/Backend 입력은 A 공급 후 대조.
- 자격값·계정 번호·ARN·MFA Serial·전체 API 응답·Token·State/Output/Plan은 수집/공개하지 않음.
- 첫 전체 ROSA Plan·유료 생성·전체 Runtime·TH/Q 완료 가산 없음.

## 연결

[현재 후속](../../../execution/MERGED_SOURCE_PLAN_READINESS_20261008.md), [원 Infra #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25). Index 제출과 D 수신 구분.
