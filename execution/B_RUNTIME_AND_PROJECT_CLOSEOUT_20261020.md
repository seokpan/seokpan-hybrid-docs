# B 실행 결과와 프로젝트 종료 준비 — 2026-10-20

> **B 전수 대조 후속 — 2026-10-21:** [최종 종료](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/B_ROSA_FINAL_CLOSEOUT_20261021.md)와 [실제 시험 결과](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/HPA_ATTEMPT04_VERIFIED_RESULTS_20261021.md)를 우선한다. B ROSA·정확한 소유 범위 잔존 자원·Snapshot4개 정리는 완료다. 아래 절차·입력 대기·명령은 작성 당시 기록 또는 재사용 계약이며 현재 재실행 요청이 아니다. A 자원과 다른 담당의 종료는 판정하지 않는다. [전체 대조](TJUNG03_FULL_REPOSITORY_AUDIT_20261021.md).

이 문서는 완료된 실행, 준비, 미확인을 구분한 추가 기록이다. 기존 설계와 이전 완료 기록을 지우지 않는다. 현재 시점에 프로젝트 종료나 과금 0을 선언하지 않는다.

## 실제 완료

- ROSA 새 클러스터 생성과 Terraform State 정리, 새 플랫폼 값 보존을 완료했다. 생성 대기 중 Red Hat 토큰 만료로 Apply가 오류를 반환했지만 원격 클러스터가 ready였으므로 재생성하지 않고 기존 리소스를 대조해 State만 정리했다.
- 과거 모니터링 볼륨 복원은 기존 PV/PVC 충돌에서 중단했다. 현재 앱과 모니터링에 필요한 최소 구성으로 진행했고 과거 이력 전체 복원 성공을 주장하지 않는다.
- 새 개인 GitHub 로그인, 목적 계정과 TLS·Schema 연결, Backend/Frontend 기동을 완료했다. 이후 실제 FE3/BE3 실행과 GitOps Synced·Healthy를 확인했다. 최종 실행 당시 현재 모니터링 고정 개정은16fd14cd1c085a8314a5e2e18b89e2cd3b051626이다.
- 정상 시험:6클라이언트·2방, 준비60초와 고정 관측180초. 업무24/24 성공, 확정실패0·결과불명0. 상태조회169와 투표24는 각각 미성공0. 상태조회 재시도 분류는 미확인169이며 재시도0으로 표현하지 않는다. Room 연결 종료0은 복구시간0의 근거가 아니다.
- 롤링 시나리오는 준비 구간의 GENERATOR_OR_ADAPTER_FAILED로 중단했고 실제 롤링 trigger는 없었다. 롤링 무중단이나 성공으로 표현하지 않는다.
- 이전 Controller DB 관측90표본에서 전체 연결 수 최대12, 누락0, 표본 간격 약10.008초였다. 관측 연결을 포함한다. 당시 계정별 가시성은 미수락이었다. 다른 시점의 전체 연결 수7 표본을 비앱 기준선이나 부하 최댓값으로 사용하지 않는다.

## HPA 별도 실행

- h-infra #106 승인·병합을 조회했다. 기존 입력 결합·현재 매칭 관측 계정의 PROCESS 최소 보완·TLS·FULL DB 준비·임시 HPA 생성·config/plan/상태 게시를 완료했다. 목적 계정·Schema는 바꾸지 않았다.
- HPA 활성화21:50:08 KST, 최소3·최대6. 선언 예산은 피크 Backend Pod8, 연결32+예약15=47/전역68이다. 선언 상한과 실제 관측 최댓값은 다르다.
- D 보고상21:52:38 KST 발생기 시작 후 VU0 준비102초에서 SSH 종료와 같은 시각에 기록이 끊겼다. SIGHUP은 추정이며 실제 부하 단계 완료·정상 종료·Guest 세션 정리는 미확인이다. 원본을 보존하고 같은 제어 Run의 attempt02로 분리 재개하도록 준비했다. h-infra #107은 관측·상태 게시 재개 보완이며 #106 승인과 구분한다.
- 시험 완료·확장·축소·원복·최종 판정은 아직 미확인이다. HPA Guest 로비/랭킹 HTTP 읽기 결과를 WSS·게임 처리량이나 일반 서비스 최대 수용량으로 확대 해석하지 않는다.

## 실제 화면 증거

앱 로비 접속, FE3/BE3 Running·Ready, Argo CD Synced·Healthy, HPA 현재 복제 수3 및 CPU 지표, Backend3 대상 up=1을 실제 브라우저에서 캡처했다. 이미지는 편집하지 않았다. 현재3 화면은 확장 성공 근거가 아니다.

발표용8장 묶음 SHA256:255a118884f0997d91e75f9fa2579872ad6233be289e2f9ccb43ab241cd22f31. 원본과 파일별 저장 시각·SHA256은 로컬 증거 묶음에 있으며 공개 저장소에는 자격·보호 원문을 올리지 않는다.

## B 담당 종료 범위와 남은 실행

최신 사용자 정정에 따라 B는 B 담당 자원만 삭제한다. 대상은 ROSA, B 임시 HPA·시험 자원, ROSA 전용 IAM·바인딩, B가 만든 모니터링 Snapshot과 ROSA 소유가 확인된 잔존 자원이다. A의 Foundation·RDS·Redis·VPN·NAT·EIP·공통 S3·Bootstrap과 다른 담당의 ECR은 제외하며 A 담당 자원은 A가 정리한다.

앞선 초안의 전체 프로젝트 정리 방침은 최신 범위가 아니다. 해당 범위로 실제 삭제나 A 영역의 설정 변경을 실행하지 않았다. 자격·보호 원문은 GitHub에 게시하지 않는다.

남은 실행은 HPA 종료 결과 수집·원복·최종 수치 판정, 영상·캡처·실행 근거의 GitHub 보존, B ROSA Terraform State와 삭제 대상 대조, B 삭제와 ROSA 소유 잔존 자원 확인이다. ROSA는2026-10-21 03:00 KST 전 삭제해야 한다. 실제 삭제는 아직 시작하지 않았다. B 삭제 완료와 계정 전체 과금0은 다른 주장이다.

## 원 근거

- [h-infra #93](https://github.com/seokpan/seokpan-hybrid-infra/pull/93): 최소 현재 구성
- [h-infra #95](https://github.com/seokpan/seokpan-hybrid-infra/pull/95): Data Pod 이미지 가져오기 참조 보완
- [h-infra #97](https://github.com/seokpan/seokpan-hybrid-infra/pull/97), [#98](https://github.com/seokpan/seokpan-hybrid-infra/pull/98): 계정·Schema와 앱 Source 연결
- [h-infra #101 실제 DB 표본](https://github.com/seokpan/seokpan-hybrid-infra/pull/101#issuecomment-6289279704)
- [h-infra #105 정상 및 실패 결과](https://github.com/seokpan/seokpan-hybrid-infra/pull/105#issuecomment-6290800041)
- [h-infra #106 실제 실행](https://github.com/seokpan/seokpan-hybrid-infra/pull/106#issuecomment-6291313882)
- [h-infra #107 SSH 중단과 실제 캡처 기록](https://github.com/seokpan/seokpan-hybrid-infra/pull/107#issuecomment-6291606987)
