# 명령·보호 범위

- 논리 참조: `controller-seoul-ec2-usage-20261008`, Source SHA256 `2b28a6d179e092b294aaa9359f66f18be8cba252587176478ce7a7cadcbdfb28`. 실제 수행 B / jth@ansible.
- 긴 클립보드/base64·셸 명령·원 API 응답/ID/ARN·계정/자격값·보호 로그는 공개하지 않음. 원14개 판정 줄만 저장.
- 기본 Caller/MFA·CPU Quota 이전 수신 결과를 재사용. 읽기 목록은 EC2 DescribeInstances/DescribeCapacityReservations/DescribeInstanceTypes이며 첫 호출1회 뒤 중단.
- Controller 시작 시각은 제공됐으나 종료/서버 시각과 목록 조회가 한 시점의 관측인지 미확인.
- 최소1호출 오류 분류 진단은 준비 후속이며 본 Run에서 추가 실행하지 않음. 오류 원인을 추정하여 공개하지 않음.
- STS/MFA/Token 반복·AssumeRole·증설·IAM/ROSA·State/Plan·Cloud 생성/변경 없음. 이전 Capacity Run 결과와 기존 Source/Caller Run 보존.
