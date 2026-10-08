# T03 / controller-seoul-ec2-usage-20261008-01

## 수행·범위

- 실제 수행자: B / jth@ansible. Source `ef424da0a6bfcdd56079ab5be249f429fa0b9c36`, ROSA Lock `668098ad0f1e293982e9bcf8e931128346a00049`.
- Controller 표시 시작 시각: `2026-10-08T12:52:29.145049+00:00`. 수신 시각: `2026-10-08T12:55:34.544013+00:00`. 종료 시각 미제공, Controller/서버 시각 일치 미확인.
- 앞선 CPU 할당량100 vCPU·Caller/MFA 결과를 재사용한 EC2 실제 사용량 보충 읽기. 전체 T03는 **PARTIAL**, 이번 보충 조회는 **BLOCKED**.

## 수신 결과

- 범위 Guard PASS, 실제 AWS API 호출1회 뒤 `BLOCKED / API_OR_NETWORK_ERROR`.
- Instance·Capacity Reservation·Instance Type의 사용량 숫자 미확보. **사용량0·현재 잔여CPU100으로 처리하지 않음**.
- 오류 응답/본문 미수집으로 원인 미확정. 네트워크·AWS 권한·인증 중 하나로 단정하지 않음.
- 호출 상한12회/목록별4페이지는 블록 설정이며 실제 호출수1회와 구분.
- 앞선 서울 활성·m5.xlarge 사양·할당량13개 조회의 성공 범위를 취소하지 않음. CPU 최근 자료 없음·기존 사용량 미확인과 EBS 기준 차이는 계속 남음.

## 후속·한계

- [ ] B: 첫 API1회만 사용하는 최소 오류 분류 진단 준비. 아직 실행되지 않았으며 실제 결과로 원인 확인 후 후속 결정.
- [ ] B/A·계정 Owner: 기존 사용량/가용량·숨은 관리 자원·Capacity Reservation·서비스별 과금/할당 계산·배치 대조.
- [ ] 프로젝트 계정·목적 Role/Backend·EBS 기준·지원·비용/Owner/창·첫 전체 Plan 수락.

원14개 판정은 [raw](raw.json)·[observations](observations.csv)에 보존. 중지/미기동 Instance 제외 등 표시된 블록의 정책은 실제 목록 조회 완료 결과가 아님. 성공한 Caller/MFA·Token·정책/Provider/mock 반복 없음. 자격값/ID/ARN·전체 응답·State/Plan 미수집, Cloud Plan/Apply·생성 없음.

## 연결

[이전 서울 용량 Run](../controller-seoul-capacity-20261008-01/summary.md), [현재 후속](../../../execution/MERGED_SOURCE_PLAN_READINESS_20261008.md), [원 Infra #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25), [05 §9.57](../../../execution/05_IMPLEMENTATION_AND_VALIDATION.md#merged-source-controller-auth-20261008). 새 실패 Run을 이전 성공에 덮어쓰지 않음.
