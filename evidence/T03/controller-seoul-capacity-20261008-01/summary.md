# T03 / controller-seoul-capacity-20261008-01

## 수행·범위

- 실제 수행자: B / jth@ansible. 수신 시각: 2026-10-08 21:43:00 KST (`2026-10-08T12:43:00.281435+00:00`). 실제 실행 시각은 제공되지 않았으며 수신 시각과 구분.
- Source: `ef424da0a6bfcdd56079ab5be249f429fa0b9c36`. ROSA Lock: `668098ad0f1e293982e9bcf8e931128346a00049`.
- 서울 리전·AWS 인스턴스 사양/제공 AZ(Availability Zone, 가용 영역)·서비스 할당량 13개와 최근 CPU 사용량의 한정 읽기. 실제 AWS API 호출 17회 보고 수신.
- 전체 T03: **PARTIAL**. 프로젝트 계정·목적 Role·기존 사용량·실제 배치·ROSA 지원·비용/전체 Plan 수락과 구분.

## 수신 결과

- [x] 서울 리전 활성 YES (`opt-in-not-required`)
- [x] AWS `m5.xlarge`: 4 vCPU·16 GiB, 제공 AZ 4개
- [x] Quota(서비스 할당량) 13개 값 읽기, 원 판정 33개 보존
- [ ] EBS(Elastic Block Store, 블록 스토리지) 할당량 기준 차이 수락: 미확인
- [ ] 기존 사용량·실제 가용량·A의 3개 AZ/프로젝트 계정 대조: 미확인
- [ ] ROSA 지원·조직/구독·목적 Role/Backend·전체 Plan: 미확인/미실행

| 읽은 할당량 | 수신 값 | 조회 블록의 비교 기준 | 원 판정 |
|---|---|---|---|
| Standard On-Demand CPU | 100.0 | 100 vCPU | AT_LEAST_REFERENCE / MINIMUM_REFERENCE |
| gp2 저장공간 | 50.0 | 300 TiB | BELOW_REFERENCE / OPTIMAL_REFERENCE_ONLY |
| gp3 저장공간 | 50.0 | 300 TiB | BELOW_REFERENCE / OPTIMAL_REFERENCE_ONLY |
| io1 저장공간 | 50.0 | 300 TiB | BELOW_REFERENCE / OPTIMAL_REFERENCE_ONLY |
| Elastic IP | 5.0 | 5 count | AT_LEAST_REFERENCE / DOCUMENT_REFERENCE |
| VPC | 5.0 | 5 count | AT_LEAST_REFERENCE / DOCUMENT_REFERENCE |
| Internet Gateway | 5.0 | 5 count | AT_LEAST_REFERENCE / DOCUMENT_REFERENCE |
| Network Interface | 5000.0 | 5000 count | AT_LEAST_REFERENCE / DOCUMENT_REFERENCE |
| Network Interface당 Security Group | 5.0 | 5 count | AT_LEAST_REFERENCE / DOCUMENT_REFERENCE |
| EBS Snapshot | 100000.0 | 10000 count | AT_LEAST_REFERENCE / DOCUMENT_REFERENCE |
| io1 IOPS | 300000.0 | 300000 IOPS | AT_LEAST_REFERENCE / DOCUMENT_REFERENCE |
| Application Load Balancer | 50.0 | 50 count | AT_LEAST_REFERENCE / DOCUMENT_REFERENCE |
| Classic Load Balancer | 20.0 | 20 count | AT_LEAST_REFERENCE / DOCUMENT_REFERENCE |

## 공식 기준 대조와 판정 한계

- 원 `OPTIMAL_REFERENCE_ONLY`·`DOCUMENT_OPTIMAL_REFERENCE` 문자열은 [raw](raw.json)·[observations](observations.csv)에 그대로 보존. 현행 공식 설명을 해당 출력 문구만으로 수락하지 않음.
- [Classic 준비 문서 §5.1 Table 5.1](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html-single/prepare_your_environment/index)의 **Minimum required** 열은 gp2·gp3·io1 각각 300 TiB. 실제 읽은 50 TiB는 이 문서 값보다 작음.
- [ROSA CLI 고정 Source](https://github.com/openshift/rosa/blob/c2e552d6d0ada5a50536507f54ceaeaa198df56e/pkg/aws/quota.go)는 gp2·io1의 `DesiredValue`를 50 TiB로 검사하며 gp3 항목은 없음. 이 Source 읽기는 현재 Controller에서 해당 CLI를 설치·실행한 결과가 아님. CLI 버전은 아직 미선정·미설치.
- A/B와 계정 Owner가 적용할 현행 지원·검사 기준을 확인하거나 필요한 증설을 조율하기 전 **EBS/ROSA 준비 전체 PASS로 판정하지 않음**. 할당량은 리전의 사용 상한이며 개별 Worker disk 선택이나 실제 사용량과 다름.
- 최근 15분 CPU CloudWatch 자료 없음은 **사용량 0이 아님**. 그 외 할당량도 기존 사용량·현재 잔여량 미확인.
- AWS 제공 AZ 4개를 A의 실제 3개 AZ·Subnet 배치와 동일하다고 처리하지 않음. AWS 사양 확인은 ROSA machine 지원 판정이 아님.
- CP3/Infra3/Worker3의 총 machine·disk 소요 미확인. 9개 노드 모두 `m5.xlarge`라고 가정하지 않음.
- 프로젝트 계정 제한 출력·목적 Role 권한·Red Hat 조직/구독·STS·선택 patch/machine/disk·예비 비용·Owner/사용창·전체 Plan은 미확인. 성공한 기본 Caller/MFA 읽기·정책/Provider/mock 반복 없음.

## 연결

[현재 후속](../../../execution/MERGED_SOURCE_PLAN_READINESS_20261008.md), [원 Infra #25](https://github.com/seokpan/seokpan-hybrid-infra/issues/25), [05 §9.57](../../../execution/05_IMPLEMENTATION_AND_VALIDATION.md#merged-source-controller-auth-20261008). Index 제출과 D 수신 구분. 전체 Runtime·TH/Q·Cost/DR 완료 가산 없음.
