# 명령·보호 범위

| case | helper 논리 참조 | Source SHA256 |
|---|---|---|
| v1 | `controller-seoul-ec2-usage-diagnostic-20261008` | `ccd9409458e0dd842c34371f261e159f612e1f31cd9616ea1a51be6828515e3a` |
| v2 | `controller-seoul-ec2-usage-diagnostic-v2-20261008` | `da9708d3388fb6a1988e254a22ef79fa29e90e6441fa2afea5271244945fa1d4` |

- 실제 수행 B / jth@ansible. 두 블록은 서로 다른 실행이며 긴 클립보드/base64·원 명령은 포함하지 않음.
- 기존 Caller/MFA·CPU Quota 수신 결과 재사용. 각 DescribeInstances 첫 요청을 위한 CLI 호출1회, SDK 최대 시도1·동시1·timeout25초 설정. 실제 서비스 요청 수/오류 출처 미확인.
- v1은 고정32개 허용 목록, v2는 확장된426개 코드 목록을 사용한 분류 블록. 코드 비식별은 실제 AWS 권한/계정/쿼터 오류 원인의 증명이 아님.
- 원 오류/전체 응답·ID/ARN·계정·Credential/Token·보호 로그·State/Plan을 저장/공개하지 않음. 공개 raw에는 받은 판정만 기록.
- 후속은 자동 API 재시도 종료·B 현장/A 계정 Owner 비공개 확인. 새 API 실행·MFA/Token 반복·AssumeRole/세션 발급·IAM/ROSA·증설·State/Plan·유료 생성 없음.
- 앞선5Run/25파일과 승인 Source/설계·TH/Q/Cost/DR 범위 보존.
