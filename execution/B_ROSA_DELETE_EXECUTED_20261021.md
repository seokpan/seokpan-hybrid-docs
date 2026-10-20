# B ROSA 실제 삭제 및 잔존 자원 확인 — 2026-10-21

> 최종 후속: B Snapshot4개는 삭제 후 모두 ABSENT로 확인했다. [B 담당 AWS 자원 종료 기록](B_ROSA_FINAL_CLOSEOUT_20261021.md)을 최종 판정으로 따른다. 아래의 재조회 대기는 삭제 직후 당시 상태로 보존한다.

## 실제 실행 결과

Controller에서 검토한 저장 Plan을 적용했다. 결과는 PASS_B_ROSA_DESTROY_APPLY_AND_ROOT_STATE_EMPTY이며 B ROSA Terraform 루트의 managed instance는0이다. 새 Plan·앱 Sync·부하·Schema 변경은 반복하지 않았다.

Plan SHA256:
8b94450b19973a99ed6b4eacb3425e481d0464c5dbf0858dd38ebb1e7a3a28c9

후속 읽기 결과는 COLLECTED_B_FINAL_RESIDUALS이며 원격 클러스터 부재를 확인했다. 현재 클러스터의 정확한 owned 태그 범위에서 EC2 instance0, EBS volume0, ENI0, load balancer0이고 조회 오류는 없었다.

## B Snapshot

B 모니터링 Snapshot4개는 계정 소유권·정확한 ID를 확인한 뒤 모두 DeleteSnapshot 요청에 성공했다. 삭제 실행 결과의 snapshots_deleted 수는4다.

출력의 snapshots PRESENT/completed는 삭제 전 조회 결과이며 삭제 이후 잔존을 의미하지 않는다. 다만 snapshot_absence_after_delete=PENDING_NEW_READBACK이므로 삭제 후 실제 부재까지 확인됐다고 쓰지 않는다. 남은 작업은 같은4개에 대한 읽기 전용 부재 확인이며 삭제를 재실행하지 않는다.

## 완료·미확인·과금 범위

| 항목 | 실제 상태 |
|---|---|
| B ROSA 삭제 Apply | 성공 |
| B 루트 managed instance | 0 |
| 원격 ROSA 클러스터 | 부재 확인 |
| 정확한 현행 ROSA owned 태그의 EC2/EBS/ENI/LB | 각각0, 조회 오류0 |
| B Snapshot4개 | 삭제 요청 성공, 삭제 후 부재 재조회 대기 |
| A Foundation/RDS/Redis/VPN/NAT/EIP/공통S3/Bootstrap | 이 실행에서 변경하지 않음, A 정리 범위 |
| 다른 담당 ECR | 제외 |
| 태그 없는 자원·공유 자원 | 이 조회로 부재를 증명하지 않음 |
| 실제 누적 청구액·과금0 | 조회하지 않았고 확정하지 않음 |

확인 범위 내 현행 ROSA EC2/EBS/ENI/LB의 잔존 과금 자원은 발견되지 않았다. Snapshot은 삭제 후 부재 확인 전까지 저장 과금 종료를 확정하지 않는다. A 담당 잔존 자원이나 제외한 자원은 계속 과금될 수 있고 이전 사용분 청구도 남을 수 있다. 계정 전체 과금0을 선언하지 않는다.

## 증거 보존

- 실제 요청 분석·시험 한계: [HPA attempt04](HPA_ATTEMPT04_VERIFIED_RESULTS_20261021.md)
- B/D 관측 구간 대조: [B/D 종료 증거 및 Plan](B_D_HPA_FINAL_EVIDENCE_AND_B_DELETE_PLAN_20261021.md)
- [B/D 공개 증거 ZIP](evidence/hpa-attempt04-20261020/B-D-public-evidence.zip), SHA256 46dc17c8b92a711fca8f57ad9486a070e18558067b6411e16314a36d3796d055
- [실제 앱 화면](evidence/hpa-attempt04-20261020/app-lobby-connected.png)

원래 설정 복원은 최종 폐기 경로에서 생략했다. 시험 전체 통과·원래 설정 복원 성공·시연 영상 촬영 완료는 주장하지 않는다. Controller 실제 삭제 영수증을 근거로 기록했으며 인증값·State 원문·내부 호스트는 게시하지 않는다.

Snapshot 부재 확인 결과는 이 기록을 보존한 뒤 별도 추가 기록으로 남긴다.
