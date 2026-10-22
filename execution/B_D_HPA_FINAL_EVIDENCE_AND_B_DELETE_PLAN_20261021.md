# B/D HPA 종료 증거 결합과 B 삭제 준비 — 2026-10-21

D 원본 인수와 B Controller 기록 결합을 완료했다. 이 Plan 검토 기록 당시 실제 삭제는 미시작이었다. 후속 [B 실제 삭제 결과](B_ROSA_DELETE_EXECUTED_20261021.md)는 Apply·State0·원격 부재·현행 owned 잔존0과 Snapshot4개 삭제 요청까지 완료했으며 [Snapshot4개 삭제 후 ABSENT](B_ROSA_FINAL_CLOSEOUT_20261021.md)도 후속 확인됐다. 기존 HPA·앱·DB·부하 시험은 재실행하지 않았다.

## 보존과 관측 결과

- D 요청 47,138건 분석 및 제한: [HPA attempt04 결과](HPA_ATTEMPT04_VERIFIED_RESULTS_20261021.md).
- B 전체 관측 425표본, 잘못된 JSON 행 0, 최대 표본 간격 17.892초. 전체 구간 복제 수 최대 6, DB 전체 연결 수 최대 24, 마지막 복제 수 3.
- D 실제 실행 구간에 해당하는 B 표본은 70개. 구간 내 복제 수 최대 6, DB 전체 연결 수 최대 23. 실제 표본 간격 중앙값 12.820초·최대 16.321초.
- VU0 구간 B 표본10·DB최대12·복제수최대3. VU10 구간14·14·3, VU50 구간23·23·6, VU100 구간23·23·6.
- VU200 구간은 약2.197초이며 B 표본이 없다. 표본 간격 사이의 순간 DB 최대나 중단 원인은 확정하지 않는다.
- 복제 수6 최초 관측은23:34:51.997 KST, 이후3 최초 관측은23:54:27.549 KST다. 실제 API 요청 또는 제어 결정 시각과 같다고 가정하지 않으며 정확한 확장·축소 지연을 계산하지 않는다.
- 전체/부하 구간의 모든 기록된 B guard 표본은 PASS였다. 이는 표본 사이 이상 부재나 전체 HPA 시나리오 통과를 증명하지 않는다.
- DB 연결 수는 관측 연결을 포함하며 예약15를 측정치에서 차감하지 않는다.

## 실제 종료 수집

B 관측·게시 종료를 확인하고 D 원본을 제한된 입력 경로로 받아 동일 Run·설정·외부/내부 해시를 검증했다. D의 기존 반환 폴더·ACL은 재사용하지 않았다.

Controller 결과: PASS_FINAL_TEARDOWN_EVIDENCE_PRESERVED_NOT_TEST_VERDICT.
generator_stopped=true, B_readers_stopped=true, restoration_verified=false.
원래 설정 복원은 최종 폐기 선택으로 생략했다. 복원 성공으로 표현하지 않는다.

결합 공개 증거 ZIP SHA256:
46dc17c8b92a711fca8f57ad9486a070e18558067b6411e16314a36d3796d055

B 단독 공개 관측 ZIP SHA256:
271ea53a81d0a488c8eed843cdc0ad050f2a19b9fadaa874300537fc1debfcaf

원본/상세 시계열과 결합 공개·비공개 ZIP은 로컬 및 Controller 보호 경로에 보존했다. 공개 본문에는 클러스터·호스트·계정 식별자와 자격을 포함하지 않는다.

## B 삭제 Plan 검토

새 저장 Plan의 해시·변경 목록을 직접 읽었다. Plan 재생성·Apply는 하지 않았다.
변경18개 모두 delete이며 구성은 클러스터1, OIDC설정1, IAM OIDC provider1, 전용 Operator 역할6·정책 연결6, Worker→Data 전용 규칙2, 입력 계약 표식1이다.

Plan SHA256:
8b94450b19973a99ed6b4eacb3425e481d0464c5dbf0858dd38ebb1e7a3a28c9

A Foundation/RDS/Redis/VPN/NAT/EIP/공통S3/Bootstrap과 다른 담당 ECR은 제외한다. B Snapshot4개는 이 Terraform Plan 밖이며 별도 대조·확인 후 삭제한다.

저장 Plan 검토 당시 남은 실행은 같은 Plan Apply, 원격 ROSA 부재 및 정확한 ROSA 소유 EC2/LB/EBS/ENI 확인, B Snapshot 정리와 최종 결과 기록이었다. 위 후속 실제 결과를 적용하며 완료한 삭제/조회를 반복하지 않는다. B 삭제와 계정 전체 과금0은 구분한다.

실제 앱·웹콘솔 캡처는 확보했으나 시연 영상 촬영 완료는 확인되지 않았다. 부하 재실행이나 영상 때문에 삭제를 자동 지연하지 않는다.
