# Foundation·Hybrid VPN 실행·검증 및 종료 기록

**기준일: 2026-10-22 KST**

기존 Issue·PR에 기록된 Foundation·Hybrid VPN의 구현, 검증, 인계 및 자원 종료 결과를 정리한다. 실제 실행 날짜와 확인 범위는 각 항목의 근거를 따른다.

이 문서는 GitHub의 코드·병합 이력과 기존 실행 보고를 대조한 기록이다. 문서 작성 과정에서 AWS 작업이나 통신 시험을 재실행하지 않았으며, Controller 보호 로그·State·AWS 이벤트 원본을 직접 대조하지 않았다.

## 1. 범위와 현재 결과

### 1.1 담당 범위

| 영역 | 담당 및 협업 |
| :--- | :--- |
| Foundation 공통 실행·Network·관련 IAM·Hybrid VPN | 이유빈 |
| ROSA·App·GitOps | 정태훈. 기반 출력 소비와 ROSA 측 실행은 해당 원 기록을 따른다. |
| Data 코드·계약·백업·복원 절차 | 김상희. Data 코드 작성·검증과 Foundation 통합 실행을 구분한다. |
| Registry/CI·관측·시험·비용 집계 | 최유준. Registry/CI 코드 작성과 Foundation 통합 실행을 구분한다. |

### 1.2 확인된 결과

기존 실행 보고에서 확인한 주요 결과는 다음과 같다.

- Foundation 최초 적용과 RDS 파라미터 적용 방식 보완 후 전체 재-Plan 변경 0.
- Data·Network 출력 인계와 수신자의 실제 자원 대조.
- NAT 생성 중 권한 오류 복구, 중간 정리 및 재생성.
- VPN 자원 생성·관리 접속·키 공급과 실제 설정 준비.
- 백업 VM에서 VPN을 경유한 RDS TLS 접속 및 원본 출발지 IP 보존.
- AWS VPN 시험 상태 원복과 Foundation·Bootstrap·원격 Backend 종료.

전체 VPN 시험, 전체 DR·RTO/RPO 달성, 온프렘 최종 원복·키 폐기 및 최종 청구액은 아래 결과만으로 완료 판정하지 않는다.

## 2. Foundation·Network·IAM

### 2.1 공통 실행 환경과 네트워크 코드

Foundation 공통 실행 설정과 네트워크 선언은 다음 PR로 반영됐다.

- [PR #32](https://github.com/seokpan/seokpan-hybrid-infra/pull/32): Backend·Provider·버전 및 공통 실행 안내.
- [PR #33](https://github.com/seokpan/seokpan-hybrid-infra/pull/33): VPC·Subnet·라우팅·S3 Gateway Endpoint 구성.
- [PR #36](https://github.com/seokpan/seokpan-hybrid-infra/pull/36): Foundation Network 관리형 정책과 역할 연결.

PR #36 적용 중 `iam:CreatePolicy` 권한 거부가 발생했다. 부분 적용 상태를 반영한 새 Plan으로 정책 생성·역할 연결을 완료하고, bootstrap 전체 재-Plan에서 `No changes`를 확인했다.

이 결과는 Network IAM 적용 범위이며, 모든 Network API의 허용·거부 시험을 완료했다는 의미는 아니다.

근거: [PR #36 적용 결과](https://github.com/seokpan/seokpan-hybrid-infra/pull/36#issuecomment-6013414243)

### 2.2 Foundation 최초 적용과 재검사

10/13 NAT 제외 Foundation 저장 Plan을 적용했다.

| 항목 | 실행 기록 |
| :--- | :--- |
| 적용 범위 | 추가 69개·수정 0개·삭제 0개·교체 0개 |
| 실행 시각 | 2026-10-13 16:12:14~16:26:42 KST |
| 소요 시간 | 14분 28초 |
| 종료값 | 0 |
| 실행 Source | `ab9be0250df009535553f1f28a1200b63aa0496d` |

이번 적용에는 NAT·NAT 전용 EIP·ROSA 인터넷 기본 경로, VPN 서버 및 ROSA 설치가 포함되지 않았다.

초기 재-Plan에서는 RDS `require_secure_transport`의 적용 방식 차이 1개가 남았다. 값은 양쪽 모두 `1`이었으나, AWS 기록은 `pending-reboot`, 당시 코드 요구는 `immediate`였다.

Data 담당의 PR #63 반영 후 다음 조건으로 전체 재-Plan을 수행했다.

- Source: `778974874d872524a9148df1c9627f426a73ddd2`
- 동일 보호 입력과 인증값 원본 사용.
- Foundation 실행 역할과 `default` Workspace 확인.
- 추가·수정·삭제·교체·조회·출력 변경 모두 0.
- 종료값 0.

추가 Apply나 DB 재시작 없이 적용 방식 차이를 해소했다. 14분 28초는 해당 Foundation Apply의 소요 시간이며, 성능 개선이나 복구 RTO 측정값은 아니다.

근거: [Foundation Apply·재검사 결과](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-6140919574)

### 2.3 출력 인계

김상희는 인계받은 Data 출력 9개와 Network 출력 2개에 대해 다음을 확인했다.

- 읽기 가능·쓰기 불가 및 JSON 형식.
- 파일과 manifest의 확인값 일치.
- RDS·Valkey 주소와 포트, 관련 보안 그룹 및 백업 자원 대응.
- Data 서브넷과 RDS 서브넷 그룹의 일치.

이 확인은 출력값과 실제 자원·계약의 일치 범위다. 당시 VPN 경유 DB 접속·TLS·출발지 IP 시험과는 구분한다.

근거: [Data 출력 수신 확인](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-6142071240)

정태훈 계정에는 기존 Data 인계 파일과 manifest의 읽기 접근을 연결하고, 읽기 가능·쓰기 불가·JSON 읽기를 확인했다.

[Docs PR #128](https://github.com/seokpan/seokpan-hybrid-docs/pull/128)은 인계 파일 접근 확인과 수신자의 manifest·해시 대조를 구분한다. 수신자의 원 회신 근거를 직접 대조하지 못한 항목은 완료로 확정하지 않으며, 실제 미수행으로 단정하지 않는다.

근거: [Data 자료 접근 연결](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-6159843548)

### 2.4 ROSA 관련 IAM

관련 코드와 실행 결과는 다음 범위로 구분한다.

- [PR #54](https://github.com/seokpan/seokpan-hybrid-infra/pull/54): ROSA 공통 IAM 자원과 Foundation 실행 권한.
- [PR #58](https://github.com/seokpan/seokpan-hybrid-infra/pull/58): ROSA 첫 Plan용 기반 조회 권한.
- PR #67: ROSA 설치용 Operator Role·OIDC 실행 권한.
- [PR #68](https://github.com/seokpan/seokpan-hybrid-infra/pull/68): DB·Valkey 연결 규칙 관리 권한.

PR #67 기반 설치용 정책은 10/14 12:27:46~12:27:52 KST에 추가 1개로 적용됐으며, 실제 역할 연결·승인 문서 일치와 bootstrap 전체 재-Plan 변경 0이 보고됐다.

이 결과는 설치 권한 적용 범위다. 실제 Operator Role·OIDC 생성과 ROSA 설치는 ROSA 담당자의 실행 기록을 따른다. PR #68의 Plan 제출만으로 해당 정책의 실제 적용 완료를 추가 판정하지 않는다.

근거: [ROSA 설치 IAM 적용 결과](https://github.com/seokpan/seokpan-hybrid-infra/issues/47#issuecomment-6160283654)

## 3. NAT 운영과 장애 복구

### 3.1 생성 중 권한 오류와 복구

10/14 NAT 적용 중 Foundation 역할의 `ec2:DescribeAddressesAttribute` 권한 누락으로 실행이 중단됐다.

당시 EIP 3개는 생성됐지만 NAT·관련 기본 경로는 생성되지 않았다. [PR #69](https://github.com/seokpan/seokpan-hybrid-infra/pull/69)로 조회 권한을 보완하고 다음 순서로 복구했다.

1. 실제 EIP와 State의 AZ별 대응 확인.
2. 해당 EIP 3개의 실패 표시 해제 및 기존 EIP 재사용.
3. 새 Foundation 전체 Plan에서 NAT 3개·기본 경로 3개 생성 범위 확인.
4. Apply 종료값 0 확인.
5. NAT 3개 `Available`, 같은 AZ 기본 경로 3개 활성 확인.
6. NAT 활성 입력을 유지한 전체 재-Plan 변경 0 확인.

복구 Apply는 추가 6개·수정 0개·삭제 0개였다. 기존 실패 Plan은 재사용하지 않았고, EIP 삭제·재생성·Import도 수행하지 않았다.

근거: [NAT 복구 결과](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-6165773506)

### 3.2 중간 정리와 재생성

| 시점 | 작업과 문제 | 확인 결과 |
| :--- | :--- | :--- |
| 10/18 | 기본 경로 3개·NAT 3개 삭제 후 EIP 처리 권한 거부 발생. 미연결 EIP 3개만 남은 새 Plan으로 반납 | 대상 NAT·EIP·기본 경로 잔존 0. NAT 비활성 입력의 전체 재-Plan 변경 0 |
| 10/20 | NAT 관련 9개 생성 Plan 준비. 첫 Apply에서 일회성 인증값 재공급 누락으로 중단 | 같은 인증값을 메모리로 공급해 10:56:44~10:58:32 KST 적용 성공. 추가 9개·수정 0개·삭제 0개 |
| 10/20 11:02:11 KST | 실제 연결 상태 조회 | NAT 3개 `available`, EIP 연결과 같은 AZ 기본 경로 활성 확인 |
| 10/21 | Foundation 최종 종료 | 종료 경과와 확인 범위는 5절 참조 |

10/18 정리는 새 Plan으로 남은 EIP를 반납한 결과이며, 기존 권한 부족 자체를 보완한 것은 아니다.

10/20의 인증값은 `ephemeral = true` 입력으로 저장 Plan에 값이 보관되지 않았다. 기존 SOPS 암호문에서 같은 값을 메모리로 복호화해 하위 프로세스에 공급했으며, 확인한 같은 저장 Plan으로 수정 적용했다.

10/20 재생성 기록에서는 적용 후 동일 입력의 전체 재-Plan이 미실행으로 남아 있다. 실제 자원 조회 성공과 재-Plan 변경 0을 혼동하지 않는다.

**9 → 0 → 9**는 NAT 3개·전용 EIP 3개·관련 기본 경로 3개를 합한 시점별 개수다. NAT Gateway 자체가 9개였다는 뜻이나 비용 절감액의 근거로 사용하지 않는다.

근거:

- [10/18 NAT·EIP 정리](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-6237410012)
- [10/20 NAT·EIP·기본 경로 재생성](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-6281612432)

## 4. Hybrid VPN 구성과 검증

### 4.1 자원·키·설정 준비

VPN 구성과 후속 보완은 다음 PR로 연결된다.

- [PR #86](https://github.com/seokpan/seokpan-hybrid-infra/pull/86): WireGuard 개인키 주입 시점을 `PreUp`에서 `PostUp`으로 변경.
- [PR #87](https://github.com/seokpan/seokpan-hybrid-infra/pull/87): 기존 온프렘 키 복원·공급.
- [PR #88](https://github.com/seokpan/seokpan-hybrid-infra/pull/88): AWS 전용 키 생성·암호화 보관.
- [PR #94](https://github.com/seokpan/seokpan-hybrid-infra/pull/94): AWS 키 공급·SSM 실행·임시 수신키 정리.

10/20 승인된 저장 Plan으로 VPN EC2·기존 EIP 연결·백업 VM 반환 Route 등 3개 자원을 생성했다. 이후 personal MFA 세션의 실제 SSM 접속, 양쪽 키 공급 및 실제 입력으로 설정 파일 생성을 확인했다.

코드 병합·키 공급·설정 파일 생성과 실제 터널·업무 통신은 서로 다른 단계로 기록한다.

근거: [VPN 자원·키 공급·설정 준비 기록](https://github.com/seokpan/seokpan-hybrid-infra/issues/16#issuecomment-6282056755)

### 4.2 AWS 키 수신 승인 정보 전달 오류

키 공급 과정에서 수신 승인 정보의 JSON 해석이 실패했다. Controller 진단에서 기존 전달 방식의 실패와 JSON 문자열 변환 후 성공을 비교했다.

[PR #110](https://github.com/seokpan/seokpan-hybrid-infra/pull/110)에서 전달 표현을 다음과 같이 변경했다.

```yaml
stdin: "{{ lookup('file', vpn_approved_target_file) | from_json | to_json }}"
```

Ansible의 자료형 변환 이후에도 수신 프로그램에 JSON 문자열을 전달하도록 마지막에 `to_json`을 적용했다. `no_log: true`는 유지했다.

병합 커밋은 `1161a81d6c5a6fb7be56a130717c659ae65c5c5e`다. 후속 실제 공급은 기존 검증·수신·설치 단계를 재사용한 별도 운영 지시서로 진행됐으며, 병합된 전체 Playbook을 처음부터 동일하게 실행한 결과와 구분한다.

### 4.3 온프렘 방화벽 보존 검사 보완

온프렘 설정 적용 중 firewalld 실행·영구 설정 비교에서 중단됐다.

NetworkManager가 관리하는 `ens160`의 구역 연결은 실행 설정에 표시됐지만, firewalld 영구 설정의 인터페이스 목록은 비어 있었다. [PR #111](https://github.com/seokpan/seokpan-hybrid-infra/pull/111)에서 실제 적용 구역이 `public`이고 차이가 해당 인터페이스 연결 한 건뿐인 경우만 허용하도록 보완했다.

서비스·포트·다른 인터페이스 등의 추가 차이는 계속 차단한다. 방화벽 설정을 일괄 영구 저장하거나 보존 검사를 제거한 변경은 아니다.

원 PR의 회귀 검사 6개·문법·공백 검사와 후속 실제 통신 결과는 각각 구분한다. 병합 커밋은 `cac4c4ecc89ff7b4a92179231d63fcc132d67895`다.

### 4.4 실제 RDS TLS 접속과 원본 IP 확인

10/21 후속 실행 보고에서 WireGuard 활성·피어 handshake·송수신 누적 카운터와 백업 VM 방향 경로를 확인했다.

백업 VM의 RDS 접속 결과는 다음과 같이 기록됐다.

```text
DB_LOGIN=PASS
TLS_CIPHER_PRESENT=YES
TLS_CERT_VERIFICATION=ENFORCED
RDS_OBSERVED_SOURCE=192.168.52.50
SOURCE_IP_PRESERVED=PASS
RESULT=RDS_TLS_AND_SOURCE_IP_PASS
TEST_EXIT=0
```

위 내용은 원 실행 보고의 발췌다. 확인 범위는 다음과 같다.

- 백업 VM의 실제 DB 로그인과 TLS 암호화 연결.
- 서버 인증서 검증 옵션을 적용한 상태의 로그인 성공.
- RDS가 관측한 출발지와 백업 VM 사설 주소의 일치.
- 임시 검사 파일 제거와 검사 종료값 0.

handshake 값 `1792516407`은 2026-10-21 02:13:27 KST에 해당한다. 이는 handshake 시점이며, 최초 기동이나 TLS 시험 전체 완료 시각은 아니다.

송수신 누적 카운터는 처리량·지연·성능 시험의 근거로 사용하지 않는다. MTU·전체 허용/거부 조합·재부팅·양종단 재구축 복구도 이번 접속 성공으로 완료 처리하지 않는다.

근거: [VPN 실제 통신·RDS TLS·출발지 IP 결과](https://github.com/seokpan/seokpan-hybrid-infra/issues/16#issuecomment-6309539081)

### 4.5 AWS 시험 상태 원복

동일 후속 기록에서 다음 결과를 확인했다.

```text
WG=INACTIVE
AUTOSTART=DISABLED
NFT=ABSENT
FORWARD=RESTORED
RESULT=AWS_VPN_RUNTIME_ROLLBACK_VERIFIED
```

확인 범위는 AWS 측 서비스 중지·자동 시작 해제·시험 nft 규칙 제거·Forwarding 복원이다. 온프렘 최종 서비스 종료·정책 원복·키 폐기까지 완료한 결과는 아니다.

## 5. 자원 종료와 잔존 확인

### 5.1 Destroy 부분 실패와 후속 처리

최초 Foundation 저장 Destroy Plan 대상은 101개였다. 첫 적용은 일부 자원을 삭제한 뒤 다음 문제로 전체 성공하지 못했다.

| 대상 | 실패 원인 | 후속 처리 |
| :--- | :--- | :--- |
| EIP | `ec2:DisassociateAddress` 권한 부족 | 미연결 상태 확인 후 EIP 4개 반납 |
| ECR | 이미지 잔존으로 Repository 삭제 거부 | Repository 2개를 이미지 포함 삭제 |
| RDS | `rds:CreateDBSnapshot` 권한 부족 | 개인 IAM 사용자로 최종 수동 Snapshot 생성 후 DB 삭제 |

부분 실패 뒤 Foundation State 잔여 14개를 확인했다. NAT Gateway 3개는 `deleted`, VPN EC2는 후속 조회에서 `terminated` 상태가 보고됐다.

변경된 AWS·State를 반영한 새 Plan으로 다음 잔여 7개를 삭제했다.

- RDS Parameter Group.
- RDS DB Subnet Group.
- RDS Security Group.
- Data Subnet 3개.
- VPC.

Plan 검토용 jq 식 오류로 한 차례 검토 단계에서 중단됐으며, 검사식을 보완한 후 확인한 Plan을 적용했다.

최종 실행 보고는 다음과 같다.

```text
Apply complete! Resources: 0 added, 0 changed, 7 destroyed.
STATE_REMAINING=0
RESULT=FOUNDATION_STATE_EMPTY
```

101·14·7은 서로 다른 시점의 계획·잔여 값이므로 합산해 총 삭제 수로 사용하지 않는다.

### 5.2 Bootstrap·Snapshot·Backend 정리

후속 종료 보고에는 다음 결과가 기록돼 있다.

- Bootstrap IAM 관련 자원 24개와 State 버킷 정책 1개, 합계 25개 삭제.
- RDS 인스턴스 삭제 waiter 성공.
- 최종 수동 RDS Snapshot 삭제 waiter 성공.
- State S3 객체 버전 220개·삭제 마커 158개, 합계 378개 제거.
- 잔여 버전·삭제 마커 0개 확인 후 State 버킷 삭제.
- 후속 버킷 목록에서 대상 부재 확인.

378개는 S3 객체 버전·삭제 마커의 합계이며, 인프라 자원 378개를 뜻하지 않는다.

ROSA State 0 조회는 ROSA 담당자의 기존 종료 결과와 연결한 확인이다. 이를 Foundation 담당자가 ROSA 종료를 직접 수행한 성과로 중복 계산하지 않는다.

### 5.3 최종 조회 범위

| 조회 범위 | 실행 보고의 결과 |
| :--- | :--- |
| 서울 EC2 `pending/running/stopping/stopped` | 대상 없음 |
| 서울 EBS·자체 EBS Snapshot·EIP | 대상 없음 |
| 서울 NAT 활성·진행·실패 상태 | 대상 없음 |
| 서울 RDS·수동 RDS Snapshot | 대상 없음 |
| 서울 ElastiCache Replication Group | 대상 없음 |
| 계정 S3 버킷 목록 | 대상 없음 |
| 서울 CloudWatch Log Group | 대상 없음 |

이 결과는 명시한 조회 범위의 잔존 확인이다. 다른 리전·미점검 서비스·RDS 자동 백업/PITR·Secrets Manager·최종 청구까지 모두 0으로 확인한 결과는 아니다.

원격 Backend는 폐기됐다고 보고돼 있다. 과거 안내에서 해당 Backend를 사용하는 Terraform 명령은 현재 운영 지시로 실행하지 않는다. GitHub Source는 보존한다.

근거: [Foundation 최종 종료·부분 실패 복구·잔존 조회](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-6309535510)

## 6. 인계·미확인 사항·관련 근거

### 6.1 과거 기록과 후속 결과

Infra #16 본문과 일부 인수인계 문서에는 작성 당시의 터널·TLS 미완료 표시가 남아 있다. 해당 기록은 당시 이력으로 보존하며, 선택한 VPN 경로의 접속 결과는 10/21 후속 댓글을 함께 읽는다.

Data 자료의 접근 확인, 수신자의 내용 검증, 실제 DB 접속은 서로 다른 확인 단계다. Docs PR #128의 미병합 상태를 실제 수신 미완료와 동일하게 해석하지 않는다.

실제 수치·파일·시간선의 원본은 관련 작업 기록과 기존 Evidence를 따른다. 이 문서는 새로운 시험 Run이나 전체 시험 수락을 추가하지 않는다.

### 6.2 미확인 범위

다음 항목은 현재 연결한 근거만으로 완료 판정하지 않는다.

- VPN MTU·전체 허용/거부 조합·재부팅·양종단 재구축 복구.
- 온프렘 최종 서비스 종료·방화벽 정책 원복·키 폐기.
- 긴급 수동 IAM 변경의 Terraform 정합성.
- 전체 DB 이관·Recovery App 연결·전체 DR·RTO/RPO 달성.
- 미점검 AWS 서비스와 최종 청구액.
- TLS 시험·원복·삭제의 정확한 일부 절대 시각.

보존된 Controller 자료·승인 기록·AWS 이벤트를 확보하면 해당 항목의 시각과 확인값을 보완한다. 자료 접근 없이 원본 검증 완료로 표시하지 않는다.

### 6.3 대조 기준과 관련 문서

문서 조사 시점의 저장소 기준은 다음과 같다. 각 실제 실행의 Source SHA는 해당 작업 기록을 따른다.

- Docs: `20e21bf370e7e64b20a6b6f38c18d2c7bdb3e330`
- Infra: `1d4d5f68a979f5ac5ba7b361626a69b30c7595bb`

관련 문서:

- [05 구현·통합·검증 기록](05_IMPLEMENTATION_AND_VALIDATION.md)
- [공통 진행표](WORK_TRACKER.md)
- [실행 안내](README.md)
- [Evidence 작성 안내](../evidence/README.md)
- [발표 준비 기준](../presentation/PRESENTATION_BASELINE.md)
- [발표 Evidence 추적 Issue #6](https://github.com/seokpan/seokpan-hybrid-docs/issues/6)
