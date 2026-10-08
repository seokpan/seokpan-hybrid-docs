# Architecture

> **상태:** 설계 기준 그림 12장 제작·자체 검증 완료, 사용자 그림 검토 대기  
> **설계 근거:** Project Source 00~04, 기본 구조 2026-10-01 KST·DR 목표 개정 2026-10-05 KST·Valkey 목표 개정 2026-10-06 KST  
> **제작일:** 최초 2026-10-02 KST·그림 10 개정 2026-10-05 KST·그림 01/02/04/12 개정 2026-10-06 KST. 실제 구축·운영·시험 결과를 보여주는 판본과 구분

현재 진행 현황:

- [x] 제작 계획과 대상 범위 확인
- [x] 전체 논리·물리 시안 2장 제작·자체 시각 검증
- [x] 상세 그림 10장 제작·원문/그림 간 교차 검증
- [x] SVG 12개·고해상도 PNG 12개·출처/해시 기록
- [x] 저장소 목차와 제작 검증 기록 연결
- [ ] 사용자 그림 검토 의견 반영
- [ ] 관련 구현 증거로 실제 구축 결과판 작성

## 전체 구조

### 전체 논리 아키텍처

정상 Cloud 사용자 경로와 On-Prem의 운영·복구 역할을 분리합니다. 공유 Runtime과 영속 업무 Data는 ROSA 밖 관리형 서비스의 책임입니다.

![전체 논리 아키텍처 — 설계 목표](exports/01-logical-architecture.png)

[SVG 편집 원본](diagrams/01-logical-architecture.svg) · [PNG 원본](exports/01-logical-architecture.png)

### 전체 물리 아키텍처

승인된 서울 VPC·3 AZ 역할·9개 Subnet과 기존/전용 On-Prem 역할을 배치합니다. 실제 AZ 이름·Host/VM 사양·주소·Data 서비스 배치 AZ는 아직 확인 대기입니다.

전체 구조는 승인된 설계입니다. 실제 배정 확인과 Worker 등 일부 초기 규모 후보를 구분합니다. 해당 자원 배치의 구현 증거가 확보되면 05 전체 종료 전에도 구축 결과판을 작성합니다. [후보 구분과 결과판 작성 시점](DIAGRAM_PLAN.md#51-후보배정-확인실제-구축의-구분과-결과판-작성-시점)을 참고합니다.

![전체 물리 아키텍처 — 목표 배치도](exports/02-physical-architecture.png)

[SVG 편집 원본](diagrams/02-physical-architecture.svg) · [PNG 원본](exports/02-physical-architecture.png)

## 그림별 목차

| ID | 그림 | 설명 목적 | SVG | PNG |
| --- | --- | --- | --- | --- |
| 01 | 전체 논리 아키텍처 | Cloud/On-Prem 환경·책임 경계 | [원본](diagrams/01-logical-architecture.svg) | [원본](exports/01-logical-architecture.png) |
| 02 | 전체 물리 아키텍처 | AZ/Subnet·자원/VM 역할의 목표 배치 | [원본](diagrams/02-physical-architecture.svg) | [원본](exports/02-physical-architecture.png) |
| 03 | Hybrid 네트워크와 경로 | RDS 사설 왕복과 Internet HTTPS 분리 | [원본](diagrams/03-hybrid-network.svg) | [원본](exports/03-hybrid-network.png) |
| 04 | 사용자 트래픽과 TLS | FE/API/WSS 분기·TLS 종료·Data 연결 | [원본](diagrams/04-service-traffic-tls.svg) | [원본](exports/04-service-traffic-tls.png) |
| 05 | 상태 책임과 재접속·업무 확정 | Runtime/DB/통지와 부분 실패·재개 기준 | [원본](diagrams/05-state-reconnect-consistency.svg) | [원본](exports/05-state-reconnect-consistency.png) |
| 06 | CI/CD와 Release 전달 | 후보·Review/Merge·배포·Recovery 사전 보존 | [원본](diagrams/06-cicd-release-flow.svg) | [원본](exports/06-cicd-release-flow.png) |
| 07 | Terraform·Ansible·GitOps 소유권과 수명 | 세 Root/State·인계·Owner·삭제/복구 예외 | [원본](diagrams/07-iac-gitops-ownership.svg) | [원본](exports/07-iac-gitops-ownership.png) |
| 08 | 관리 인증과 Secret 공급 | 목적별 인증·주/예비 보관자·Key 분리 | [원본](diagrams/08-identity-secret-supply.svg) | [원본](exports/08-identity-secret-supply.png) |
| 09 | 관측과 Evidence | 신호·판단·Run/Index·결과/보호 원본 보존 | [원본](diagrams/09-observability-evidence.svg) | [원본](exports/09-observability-evidence.png) |
| 10 | 백업과 On-Prem 오프라인 복구 | 정상 사전 준비·로컬 Restore·시험 목표 | [원본](diagrams/10-backup-offline-recovery.svg) | [원본](exports/10-backup-offline-recovery.png) |
| 11 | HA와 장애 영향 범위 | 플랫폼 HA·상태 손실·운영/복구 장애 영역 | [원본](diagrams/11-ha-failure-domains.svg) | [원본](exports/11-ha-failure-domains.png) |
| 12 | 1차에서 2차로의 책임 이전 | 역할별 유지/이전/대체·Seed·전환·1차 보존 | [원본](diagrams/12-migration-responsibility.svg) | [원본](exports/12-migration-responsibility.png) |

위 ID는 그림 번호입니다. 프로젝트 문서 05의 구현·검증 단계 번호와 구분합니다. 12장의 SVG/PNG는 각각 다른 형식의 같은 그림이며 총 24장으로 계산하지 않습니다.

**현재 DR 설계 — 2026-10-05:** 온프레미스 오프라인 복구의 **RTO 10분·영속 DB RPO 30분·운영 중 Portable Backup 15분 주기**를 설계·시험 요구사항으로 반영했습니다. Cloud Primary + On-Prem Backup/Restore, 별도 새 DB VM·새 Redis·사전 로컬 자산을 사용하는 구조와 일반 7일 보존은 유지합니다. 생성 원본과 그림 10 SVG/PNG를 함께 갱신했고, 다른 11개 그림의 바이트는 보존했습니다. 이 수치는 달성값이나 24시간 운영 보장이 아닙니다. 실제 전체 복구 시간·로컬 백업 최신성·지연·부하의 합격 판정은 별도 Run으로 남깁니다. 판단 근거와 이전 값은 [03 §3-I.14](../design/03_DETAILED_DESIGN.md#recovery-design-review-20261003)에 연결합니다.

**2026-10-03 재검토 이력:** 당시에는 RTO 30분·RPO 90분·1시간 백업을 유지한 채 적절성/달성 여부를 재검토했습니다. 02/03/04의 별도 새 DB/Redis·전체 업무/접속 범위를 보완하고, 그림 내용·수치를 변경하지 않아 출처 Manifest만 갱신했습니다. 그때의 원문·판단 이력은 보존하며 현행 목표는 위 2026-10-05 개정을 따릅니다.

**현재 Data·Registry 경계:** Cloud·lab·Recovery의 선택 엔진은 Valkey 7.2 계열이다. 그림 01/02/04/12의 엔진 표시는 2026-10-06 개정이며, 나머지 `Redis`는 프로토콜·Runtime 논리 계층 또는 1차/과거 자산을 뜻한다. 실습 OCP는 Harbor 직접 경로 제약에 따라 승인 이미지를 내부 Registry로 보존 복사해 소비한다. 이는 그림의 정상 Cloud ECR 경로와 온프레미스 Harbor Recovery 보존 역할을 대체하지 않는다. lab 실제 경로·Source·Pull/업무 결과는 [GitOps #14](https://github.com/seokpan/seokpan-hybrid-gitops/issues/14)·[#17](https://github.com/seokpan/seokpan-hybrid-gitops/pull/17)과 05에서 추적한다.

## 제작·검증 기록

- [제작 계획](DIAGRAM_PLAN.md): 목적·포함 내용·근거·실제 확인 대기 입력
- [계획 연쇄 검토 이력](REVIEW_RECORD.md): 제작 전 원문/계획 검토와 보완
- [제작 검토 기록](PRODUCTION_REVIEW.md): 실제 산출물의 교차·시각·파일 검증과 한계
- [Diagram Manifest](diagram-manifest.json): 원문 식별·그림별 근거/대기 입력·출력 크기/해시
- [설계문서 목차](../design/README.md): 00~04 원문과 해석 순서

정확한 문자·자원·연결을 유지하도록 편집 가능한 벡터로 제작했습니다. SVG에는 한글 글꼴을 포함하고 PNG는 폭 3600px로 출력합니다. GitHub README에는 PNG 미리보기와 SVG 원본 링크를 함께 둡니다. GitHub 브라우저의 SVG 표시를 직접 확인한 상태로 기록하지 않습니다.

## 재생성

[생성 코드](tools/build_diagrams.py)와 [파일 검증 코드](tools/verify_diagrams.py)를 보존합니다. Python 3.12+, Pillow, fonttools, Inkscape 및 설치된 [원본 한글 글꼴](assets/README.md)이 필요합니다. 저장소 Root에서 실행합니다.

```bash
python3 architecture/tools/build_diagrams.py --font /path/to/NotoSansCJKkr-Regular.otf --render
python3 architecture/tools/verify_diagrams.py
```

일부 그림만 다시 만들 때는 `--only 1 2`처럼 그림 번호를 지정합니다. 전체 layout 입력이 없는 새 작업 사본에서는 먼저 필요한 전체 생성 입력을 마련합니다. 그림 바이트를 변경하지 않는 출처·설계 메타 갱신은 `python3 architecture/tools/verify_diagrams.py --integrity-only`로 기존 SVG/PNG를 manifest 해시와 대조할 수 있습니다. 이 모드는 원 생성 layout의 선언 기하 검사를 생략하며 이를 PASS로 기록하지 않습니다. 기본 검증 모드는 layout 입력이 없으면 실패합니다. 회귀 검사는 `python3 -m unittest discover -s architecture/tools -p "test_*.py"`로 수행합니다.

무결성 검사는 저장소 원문 바이트와 상대경로 표기를 대조한다. Windows에서 Git의 줄바꿈 변환이 적용된 작업 파일은 원문 해시와 다를 수 있다. 개인 clone의 설정·파일을 바꾸지 않고 검사하려면 별도 폴더에 `git -c core.autocrlf=false archive --format=zip --output=<별도 ZIP 절대경로> <검토한 전체 SHA>`로 원문 사본을 만든 뒤 그 사본에서 검사한다. 상대경로는 Windows·Linux 모두 `/` 표기를 사용한다. `--integrity-only`도 사본의 `architecture/diagram-manifest.json`을 갱신하므로 기존 clone 보존이 필요하면 반드시 별도 사본을 사용한다.

최신 DR·Data 메타는 `design/source-manifest.json`에서 읽고 과거 검토·검사 이력과 알 수 없는 확장 필드는 보존합니다. 검증 실패 시 manifest를 덮어쓰지 않으며 같은 입력의 반복 실행은 같은 결과를 내야 합니다.

자동 검사는 글자/출력 경계·폰트 글리프·파일/원문 동일성을 확인합니다. 의미와 화살표 방향, 겹침/가독성은 수정된 그림을 직접 렌더링해 다시 확인합니다. 사용자 편집으로 SVG를 변경하면 PNG와 Manifest도 같은 개정으로 갱신합니다.

## 남은 작업과 다음 단계

- [ ] 사용자 그림 검토 의견 반영
- [ ] 문서 05의 해당 입력·Source/Run 확인 후 전체 논리·물리의 구축 결과판 2장 작성
- [ ] 실제 장애/복구·성능 Run에 설명 가치가 있으면 결과 그림 추가

설계판 12장은 보존합니다. 제안된 구축 결과판 2장까지 만들면 최소 14개 판본이며, 지금 제작한 그림을 HA/DR·RTO/RPO·예산 충족의 실행 증거로 사용하지 않습니다.
