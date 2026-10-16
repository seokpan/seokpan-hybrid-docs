# B06-VALKEY-01 — Recovery Valkey 단독 기동

- Run: `b06-valkey-20261016-01`
- 결과 기록일: 2026-10-16 KST
- 판정: `PASS_RECOVERY_VALKEY_READY_UID_TLS_AUTH`
- 대상: 기존 Kubernetes / `seokpan-recovery`
- Source: `c75a4b5e3b3b9bae4ea7d8a431962cb9ca7308d7` ([GitOps #57](https://github.com/seokpan/seokpan-hybrid-gitops/pull/57))

## 실제 결과

| 범위 | 관측 결과 |
| --- | --- |
| 객체 생성 | NetworkPolicy4·ConfigMap1·Service1·StatefulSet1, 총7개 |
| 기동 | `recovery-redis`만0→1, Pod `recovery-redis-0`, worker-02, Ready |
| 재시작 | 0 |
| 실행/파일 | UID999, 설정/TLS/AUTH 파일 읽기, 임시 쓰기 경로 확인 PASS |
| TLS/AUTH | CA/서버 이름 검증, 미인증 PING·잘못된 AUTH 거부, 정상 AUTH/PING PASS |
| 입력 공급 | 기존 보호5객체·Harbor Secret 재공급0, SOPS 재해독0 |
| 제외 실행 | Backend/Frontend·Cloud앱·SQL·Migration·DB 복원0 |

Valkey imageID는 `harbor.seokpan.soldesk.store/seokpan-hybrid/valkey@sha256:ef0f9fb533b1f06fb7aba6478d758ca1c077d49e2bcb2b4365a4ea7f50b6d42e`와 일치했다. imagePullPolicy는 `IfNotPresent`다. Source 전체 Replica0 중 Valkey만 수동1로 기동했다.

## 증거와 판정 경계

기동 실행의 구조화된 결과를 [summary.json](summary.json)에 비민감 필드로 연결한다. 실제 실행 출력에서 수락한 결과이며 문서 작성 중 재실행하지 않았다. 관측되지 않은 시작/종료 시각·소요시간을 만들지 않았다.

TLS/AUTH는 로컬 API port-forward 경로다. CNI 정책 집행의 실통신 증거가 아니며 캐시를 배제한 Registry 새 접속·워커 CA 인과도 독립 관측하지 않았다. 실제 Backend/Frontend·DB 복원·FE 진입/복원 Client·전체 업무·오프라인 망 독립·RTO10분/RPO30분은 이 Run에서 판정하지 않는다.

