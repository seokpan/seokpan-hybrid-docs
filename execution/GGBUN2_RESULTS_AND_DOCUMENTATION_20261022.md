# 이유빈 Network·Foundation·IAM·Hybrid 실행 결과와 문서 현행화

**문서 대조 기준일: 2026-10-22 KST / 실제 결과: 아래에 연결한 2026-10-06~21 기록.**

Foundation 구축·재검사·출력 인계, NAT 생성·중간 정리·재생성, VPN 경유 백업 VM의 RDS TLS 접속과 원본 출발지 보존, AWS 측 원복·Foundation 종료가 원 작업 기록에 보고돼 있다. VPN의 MTU·전체 허용/거부·재부팅·양종단 재구축, 온프렘 최종 원복·키 폐기, 전체 DR·최종 청구는 이 결과로 완료 판정하지 않는다.

이 문서는 **기존 실행 보고와 코드 병합 근거를 대조한 현재 요약**이다. 새 AWS 조회·Plan·Apply·접속·복원 시험을 수행하지 않았고 Controller 보호 로그·State·AWS 이벤트 원본을 직접 열어 독립 검증하지 않았다. 아래의 ‘실행 보고’는 원 댓글에서 확인한 결과이며, 이번 문서 작성자가 재실행한 결과를 뜻하지 않는다. 기존 Run의 정본을 대체하거나 새 시험 Run을 만들지 않는다.

## 1. 담당 범위와 근거를 읽는 방법

| 구분 | 범위와 책임 |
|---|---|
| A 이유빈(`ggbun2`) | Foundation 공통 실행 틀·Network·통합 실행, 관련 IAM 보완, Hybrid VPN 구성·실행 기록 |
| B 정태훈 | ROSA·App·GitOps의 원 담당. A의 기반 출력 소비·검토와 B 직접 실행을 구분 |
| C 김상희 | Data 코드·계약·백업/복원 절차의 원 작성·검증 담당. A의 통합 Apply·인수 후 실행과 구분 |
| D 최유준 | Registry/CI·관측·시험·비용 집계 담당. Registry/CI 코드 작성과 이유빈의 Foundation 통합·실행을 구분한다. |

원 작업 Issue/PR·결과 댓글은 상세 근거, 이 문서는 범위별 현재 요약, `WORK_TRACKER.md`는 바로가기다. 실제 수치·파일·시간선의 새 공개 증거 묶음은 기존 원본을 확보하고 민감정보를 확인한 뒤 `evidence/` 안내에 따라 별도로 등록한다.

대조한 저장소 기준은 Docs `20e21bf370e7e64b20a6b6f38c18d2c7bdb3e330`, Infra `1d4d5f68a979f5ac5ba7b361626a69b30c7595bb`다. 이 두 SHA는 **문서 조사 시점의 main**이며 아래 각 실행의 Source SHA와 다르다.

## 2. 작업별 결과와 완료 경계

| 영역 | 원 기록에서 확인한 결과 | 판정 범위·한계 | 원 근거 |
|---|---|---|---|
| Foundation 공통 틀·Network | Backend/Provider/버전 공통 설정과 VPC·Subnet·라우팅·S3 Endpoint 코드 병합 | Source 반영. 실제 실행은 아래 Apply 기록으로 따로 확인 | [PR32](https://github.com/seokpan/seokpan-hybrid-infra/pull/32), [PR33](https://github.com/seokpan/seokpan-hybrid-infra/pull/33) |
| Network IAM | 최초 `iam:CreatePolicy` 거부 뒤 새 Plan으로 정책 생성·역할 연결, bootstrap 재-Plan `No changes` | 해당 IAM 적용 완료 보고. 모든 API 허용/거부 시험 완료는 아님 | [PR36 적용 결과](https://github.com/seokpan/seokpan-hybrid-infra/pull/36#issuecomment-6013414243) |
| Foundation 최초 실행 | NAT 제외 69개 생성 범위의 Apply 종료값 0. RDS 파라미터 적용 방식 차이 보완 뒤 전체 재-Plan 변경 0 | NAT·VPN 서버·ROSA 설치를 포함한 결과가 아님 | [#23 최초 Apply·재검사](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-6140919574) |
| Data 출력 인계 | C가 Data 9개·Network 2개 출력의 읽기 전용 접근·manifest·실제 AWS 자원 대응을 확인 | 값과 계약 수신 확인. 당시 VPN 접속·TLS 시험과 별개 | [C 수신 확인](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-6142071240) |
| B의 Data 자료 접근 | `c-data-outputs.json`·manifest 읽기 가능/쓰기 불가·JSON 읽기 확인 | A 접근 확인과 B의 내용 수신·실제 접속을 구분. 후속 정정 PR128은 미병합 | [접근 연결 결과](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-6159843548), [Docs PR128](https://github.com/seokpan/seokpan-hybrid-docs/pull/128) |
| ROSA 설치 IAM | PR67 기반 정책 추가 1개 적용, 실제 연결·문서 일치, bootstrap 전체 재-Plan 변경 0 | A의 설치 권한 적용 결과. B의 Operator/OIDC 생성·ROSA 설치와 구분 | [#47 IAM 적용](https://github.com/seokpan/seokpan-hybrid-infra/issues/47#issuecomment-6160283654) |
| NAT 수명 관리 | 10/14 복구 → 10/18 관련 9개 정리 → 10/20 관련 9개 재생성 | 각 날짜의 생성·정리 결과. 10/20 같은 입력의 재-Plan은 해당 기록에서 미실행 | [복구](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-6165773506), [중간 정리](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-6237410012), [재생성](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-6281612432) |
| VPN 자원·키·설정 준비 | EC2·EIP 연결·반환 Route 생성 3개, personal MFA SSM 접속, 양쪽 키 공급·설정 파일 생성 | 당시 준비 범위. 이후 실제 통신은 다음 행의 최신 기록을 적용 | [#16 준비·실행 경과](https://github.com/seokpan/seokpan-hybrid-infra/issues/16#issuecomment-6282056755) |
| VPN 실제 통신 | WireGuard active·handshake·송수신 관측. 백업 VM RDS 로그인·TLS·서버 인증서 검증 옵션 적용·출발지 `192.168.52.50` 일치, 검사 종료값 0 | 선택한 실제 경로의 TLS·원본 IP 보존 성공 보고. 전체 네트워크 시험이나 성능 시험은 아님 | [#16 최신 통신 결과](https://github.com/seokpan/seokpan-hybrid-infra/issues/16#issuecomment-6309539081) |
| VPN AWS 측 원복·종료 | WG 중지·자동 시작 해제·시험 nft 규칙 제거·Forwarding 복원. 후속 VPN EC2 종료·EIP 반납 보고 | AWS 시험 상태·자원 종료. 온프렘 최종 원복·키 폐기는 미확인 | [#16 최신 종료 결과](https://github.com/seokpan/seokpan-hybrid-infra/issues/16#issuecomment-6309539081) |
| Foundation·Bootstrap·Backend 종료 | 부분 실패 복구 뒤 Foundation State 0, Bootstrap 관련 25개 삭제, State 버킷 버전/마커 378개 제거·버킷 부재 보고 | 명시한 조회 범위의 종료 보고. 다른 리전·미점검 서비스·최종 청구까지 0이라는 뜻은 아님 | [#23 최종 종료](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-6309535510) |

PR54의 공통 IAM 생성 코드, PR58의 기반 조회 권한, PR68의 Data 연결 권한은 각각의 [Source](https://github.com/seokpan/seokpan-hybrid-infra/pull/54)·[Source](https://github.com/seokpan/seokpan-hybrid-infra/pull/58)·[Source](https://github.com/seokpan/seokpan-hybrid-infra/pull/68) 범위를 유지한다. PR68의 Plan 제출만으로 실제 정책 적용 완료를 추가 판정하지 않는다. 관련 전체 IAM 시험과 긴급 수동 권한 변경의 Terraform 정합성도 이 문서에서 일괄 완료하지 않는다.

## 3. 주요 실행 흐름과 측정값

### 3.1 Foundation: 생성 → 차이 발견 → 코드 보완 → 변경 없음

10/13 최초 NAT 제외 Foundation Apply는 16:12:14~16:26:42 KST, **14분 28초**, 종료값 0으로 보고됐다. 실행 Source는 `ab9be0250df009535553f1f28a1200b63aa0496d`다.

초기 재-Plan에는 RDS `require_secure_transport`의 값 자체가 아닌 적용 방식(`immediate`/`pending-reboot`) 차이 1개가 남았다. Data 담당의 PR63 반영 후 Source `778974874d872524a9148df1c9627f426a73ddd2`에서 추가·수정·삭제·교체·조회·출력 변경 모두 0, 종료값 0을 확인했다고 기록돼 있다. 이 시간은 해당 Foundation Apply 소요이며 ROSA 설치 시간·통신 지연·복구 RTO가 아니다.

### 3.2 NAT: 생성·정리·재생성을 서로 다른 실행으로 보존

| 시점 | 실제 경과 | 확인 결과·주의 |
|---|---|---|
| 10/14 | EIP 3개 부분 생성 뒤 조회 권한 거부 → PR69 권한 보완 → 같은 EIP 재사용 → 새 전체 Plan으로 NAT3·기본 경로3 생성 | NAT3 `Available`, 같은 AZ 기본 경로3 활성, 전체 재검사 변경 0. 기존 실패 Plan을 복구 Plan으로 재사용하지 않음 |
| 10/18 | 기본 경로3·NAT3 삭제 후 EIP 처리 권한 거부 → 미연결 EIP3만 남은 새 Plan 적용 | NAT/EIP/기본 경로 대상 잔존 0, 같은 비활성 입력의 전체 재검사 변경 0. 권한 부족 자체를 수정한 결과는 아님 |
| 10/20 | NAT 활성 입력으로 관련 9개 생성 Plan → Apply의 ephemeral 인증값 재공급 누락으로 중단 → 같은 인증값을 메모리로 공급해 적용 | 10:56:44~10:58:32 KST, 추가9·수정0·삭제0. 11:02:11 KST 실제 NAT/EIP/같은 AZ 경로 확인. 이후 동일 입력 재-Plan은 이 기록에서 미실행 |
| 10/21 | Foundation 최종 종료 | 이전 재생성 상태가 현재 가동 상태라는 뜻은 아님. 상세는 §5 |

NAT 관련 묶음의 **9 → 0 → 9**는 시점별 NAT3·전용 EIP3·관련 기본 경로3을 합한 개수다. NAT Gateway 자체가 9개였다는 뜻이 아니다. 현재 가동 자원 수나 비용 절감액으로 사용하지 않는다.

### 3.3 VPN: 준비와 실제 접속의 최신 결과 구분

10/20~21 준비 기록에는 EC2 생성·키 공급·설정 생성까지만 완료돼 있었다. 이후 [10/21 최신 댓글](https://github.com/seokpan/seokpan-hybrid-infra/issues/16#issuecomment-6309539081)에 실제 경로의 다음 결과가 추가됐다.

```text
DB_LOGIN=PASS
TLS_CIPHER_PRESENT=YES
TLS_CERT_VERIFICATION=ENFORCED
RDS_OBSERVED_SOURCE=192.168.52.50
SOURCE_IP_PRESERVED=PASS
RESULT=RDS_TLS_AND_SOURCE_IP_PASS
TEST_EXIT=0
```

위는 **원 실행 보고의 발췌**다. 출발지 주소는 이미 공개된 사설 백업 VM 주소이며 실제 RDS Endpoint·공인 IP·인증값은 포함하지 않는다.

handshake 값 `1792516407`은 2026-10-21 02:13:27 KST에 해당한다. 이는 handshake 시점이며 최초 기동·TLS 시험 종료·원복 완료 시각이 아니다. TLS 시험·원복·삭제의 정확한 절대 시각은 미확정으로 유지한다. MTU·거부 조합·재부팅·재구축을 이 접속 성공으로 완료 처리하지 않는다.

## 4. 트러블슈팅과 코드 근거

| 문제 | 판단·수정 | 확인 근거와 주장 제한 |
|---|---|---|
| NAT EIP 속성 조회 `AccessDenied` | `ec2:DescribeAddressesAttribute`를 보완하고 부분 생성 EIP를 대조해 재사용 | [PR69](https://github.com/seokpan/seokpan-hybrid-infra/pull/69), §2의 실제 조회·NAT 복구 보고. IAM 무제한 확대나 EIP 전량 재생성으로 기록하지 않음 |
| AWS 키 수신 승인 정보 JSON 해석 실패 | Ansible의 자료형 변환 뒤 Python 표현 문자열 전달 문제를 재현. 마지막 `to_json`으로 JSON 문자열 전달 | [PR110](https://github.com/seokpan/seokpan-hybrid-infra/pull/110), 병합 `1161a81d6c5a6fb7be56a130717c659ae65c5c5e`, 준비·재개 실제 결과는 #16 원 기록 |
| 온프렘 방화벽 실행/영구 설정 보존 검사 중단 | NetworkManager가 관리하는 `ens160`의 public 구역 연결 표현만 조건부 허용. 서비스·포트·다른 인터페이스 차이는 계속 거부 | [PR111](https://github.com/seokpan/seokpan-hybrid-infra/pull/111), 병합 `cac4c4ecc89ff7b4a92179231d63fcc132d67895`. 원 PR의 회귀 검사6개와 후속 실제 통신 보고를 구분 |

PR110의 핵심 변경은 다음 한 줄이다. 전체 수신·검사·정리 절차를 대체하는 실행 예제가 아니며, `no_log: true`는 유지됐다.

```yaml
stdin: "{{ lookup('file', vpn_approved_target_file) | from_json | to_json }}"
```

기존 `PreUp`→`PostUp` 보완과 키 보관·복원·SSM 공급 코드는 [PR86](https://github.com/seokpan/seokpan-hybrid-infra/pull/86)·[PR87](https://github.com/seokpan/seokpan-hybrid-infra/pull/87)·[PR88](https://github.com/seokpan/seokpan-hybrid-infra/pull/88)·[PR94](https://github.com/seokpan/seokpan-hybrid-infra/pull/94)에 있다. Source 병합과 실제 공급은 §2의 #16 실행 근거를 따로 연결한다.

## 5. 종료 결과와 보존·미확인 범위

[최종 종료 보고](https://github.com/seokpan/seokpan-hybrid-infra/issues/23#issuecomment-6309535510)의 최초 Destroy Plan 대상은 101개였다. 부분 실패 뒤 State 잔여14개를 확인했고, EIP 반납·이미지가 남은 ECR 삭제·수동 RDS Snapshot 후 DB 삭제를 처리한 다음 새 Plan의 잔여7개를 삭제해 Foundation State0을 확인했다고 기록했다.

**101·14·7은 서로 다른 시점의 계획/잔여 값이다. 합산해 총 삭제 수로 사용하지 않는다.** Bootstrap IAM 관련24개와 State 버킷 정책1개를 합한25개도 별도 범위다. State S3의 버전220개·삭제 마커158개는 객체 이력378개이며 인프라 자원378개가 아니다.

| 보고된 최종 조회 범위 | 결과와 한계 |
|---|---|
| 서울 EC2의 pending/running/stopping/stopped, EBS·자체 EBS Snapshot·EIP, NAT의 활성/진행/실패 상태 | 대상 없음 보고. EC2 종료 이력이 전혀 없다는 뜻은 아님 |
| 서울 RDS·수동 RDS Snapshot·ElastiCache Replication Group | 대상 없음 보고. RDS 자동 백업/PITR·Secrets Manager까지 확인한 결과는 아님 |
| 계정 S3 버킷 목록·서울 CloudWatch Log Group | 대상 없음 보고. 다른 리전·미점검 서비스·최종 청구까지 0이라는 뜻은 아님 |
| 온프렘 VM·데이터·서비스·방화벽·키 | 최종 정리 상태 별도 미확인 |

ROSA State0 조회는 B의 기존 종료와 연결한 확인이며 A가 ROSA 종료를 직접 수행한 성과로 중복 계산하지 않는다. GitHub Source는 보존돼 있다. **원격 Backend는 폐기됐다고 보고돼 있으므로 과거 안내의 Terraform 명령을 현재 운영 지시로 실행하지 않는다.** 원본 로그·AWS 이벤트 확보가 필요하면 보존 사본으로 확인하고, 새 가동·재생성·유료 시험을 문서화의 선행조건으로 추가하지 않는다.

## 6. 문서 사이의 차이와 이번 반영

| 대조 대상 | 발견한 차이 | 이번 처리·후속 |
|---|---|---|
| Work Links 이유빈 행 | 초기 세션/인계 대기 위주. 뒤의 Apply·출력 수신·최신 통신·종료 보고를 반영하지 못함 | A 행을 현재 결과와 근거 링크 중심으로 현행화. B/C/D 행은 보존 |
| 05·실행 안내 | 날짜별 기록과 B 최신 요약 중심으로 A 최신 결과 진입점이 부족 | 이 문서의 날짜·범위·링크를 연결. 과거 실행 기록·체크는 보존 |
| Infra #16 본문과 최신 댓글 | 본문은 터널/RDS TLS 미완료, 최신 댓글은 실제 TLS·원본 IP 보존 및 AWS 종료 성공 | 최신 댓글을 해당 확인 범위에 적용. 원 Issue 본문·체크는 이번 Docs 변경에서 수정하지 않음 |
| Infra #23 본문과 최신 댓글 | 본문의 초기 통합 대기와 이후 Apply·최종 종료 보고가 함께 존재 | 각 단계의 원 댓글을 연결. #23 원 완료 기준 전체 충족/Close는 별도 검토 |
| Docs PR128 | Data JSON 조회 형식·B 수신 상태 정정안이 Open·미병합 | 병합된 사실로 작성하지 않음. 해당 PR의 최신 상태·원 회신 대조는 별도 후속 |
| Data 인수인계 | 기준일 10/13~14의 당시 상태. 이후 10/21 접속 성공·자원 종료와 시점이 다름 | 역사적 원본을 일괄 현재화하지 않음. 인수 후 실행은 실행자·원 근거를 구분해 후속 대조 |

이번 변경은 신규 요약, A 진행표, 05 진입 안내, 실행 README 연결이다. 원 Issue의 체크·상태·담당자 변경, PR128 대체, 다른 담당의 현재 완료 판정은 포함하지 않는다.

## 7. 남은 문서화와 발표 사용 경계

1. 보존된 Controller 결과·승인 기록·확인값을 확보하면 원 댓글의 수치·실행 개정·시각을 대조한다. 접근하지 못한 원본을 검증 완료로 쓰지 않는다.
2. 기존 원본과 `evidence/` 등록 상태를 대조해 필요한 공개 증거만 등록한다. 과거 실행의 등록일을 실제 실행일로 바꾸거나 빈 CSV를 0초/0건으로 채우지 않는다.
3. Docs PR128과 Data 인수 후 실행 범위를 별도로 대조한다. 독립 DB 복원 예행을 전체 DB 이관·전체 DR·전체 RTO/RPO 달성으로 표현하지 않는다.
4. Infra #16/#23/#47의 본문·체크와 최신 결과를 대조해 현행화 후보를 정리한다. 미검증·미수행·종료 범위 제외를 구분한 뒤 원 이슈 종료 여부를 판단한다.
5. 온프렘 최종 원복·키 폐기, IAM 긴급 변경 정합성·미점검 AWS 서비스·최종 청구의 확인 여부를 기록한다. 확인 자료가 없으면 미확인으로 유지한다.

발표 후보는 Foundation의 **Apply → 차이 보완 → 재-Plan 변경0**, NAT의 **부분 실패 원인·최소 수정·복구**, VPN의 **실제 RDS TLS·원본 IP 보존**, 종료의 **부분 실패·잔여 재계획·조회 범위 내 부재**다. 14분28초를 성능 개선 수치로, handshake 시각을 시험 소요로, 잔존 조회 결과를 최종 비용0으로, 선택 경로 접속 성공을 전체 VPN/DR 성공으로 쓰지 않는다. 발표 후보 확정은 [Issue6](https://github.com/seokpan/seokpan-hybrid-docs/issues/6)과 기존 발표 기준을 따른다.
