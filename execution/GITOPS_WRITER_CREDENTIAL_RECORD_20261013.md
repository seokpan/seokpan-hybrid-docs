# GitOps Writer Credential 운영 기록 (`hybrid-gitops-writer`)

> **잔여 체크 표현 정리 — 2026-10-21:** 미체크 문구는 실제 수행/미수행 사실을 바꾸지 않고 일반 기록 또는 재사용 조건으로 표시했다. [변경 전 체크 원문](https://github.com/seokpan/seokpan-hybrid-docs/blob/2de414c618a465f0d94860f4b92f4fb7ac777b7a/execution/GITOPS_WRITER_CREDENTIAL_RECORD_20261013.md)은 해당 고정 커밋에 보존한다. 현재 실행 대기나 전체 목표 달성률이 아니며 [원 계획별 변경·최종 판정·영향](https://github.com/seokpan/seokpan-hybrid-docs/pull/140)을 따른다.

> **B 전수 대조 후속 — 2026-10-21:** 이 문서의 조사·준비·현재/대기 표기는 제목 날짜의 이력이다. 이후 B 앱·정상 시험·HPA 한계·최종 종료는 [최신 종료 기록](https://github.com/seokpan/seokpan-hybrid-docs/blob/main/execution/B_ROSA_FINAL_CLOSEOUT_20261021.md)과 [전수 대조](TJUNG03_FULL_REPOSITORY_AUDIT_20261021.md)를 따른다. 성공한 실행을 다시 대기시키거나 미수행 시험을 성공으로 바꾸지 않는다.

작성: 최유준 / 작성 날짜: 2026-10-13 / 대표 Issue: [h-app #14](https://github.com/seokpan/seokpan-hybrid-app/issues/14), 사용처 [h-app #15](https://github.com/seokpan/seokpan-hybrid-app/issues/15)

이 문서는 공개 저장소용 **논리 참조 기록**이다. Token 값·접두어·일부 문자열, 발급 계정명, 계정 번호, 보호 보관 파일의 실제 경로·Key는 쓰지 않는다(§6 점검 대상). 값이 필요한 항목은 `[보호 기록: <논리 참조>]`로만 연결한다. 이 기록은 Credential 경로의 검증이며 이미지 공급·OCP/Cloud 배포·업무 수락을 뜻하지 않는다.

## 1. Credential 계약

| 항목 | 기록 | 근거 |
| --- | --- | --- |
| Credential ID | `hybrid-gitops-writer` | h-app #14 (정태훈 리뷰 확인) |
| 종류 | Jenkins Username/Password (같은 PAT로 HTTPS Git과 REST) | h-app #14 |
| 등록 위치 | Jenkins `hybrid` Folder | h-app #14 |
| 사용 범위 | `hybrid/image-pipeline`의 Promotion 단계(`Promotion (credentialed)`)만. 통제는 Jenkinsfile 리뷰(hybrid-app main 보호) | h-app #14, #15 |
| 토큰 종류 | GitHub Fine-grained PAT 1개 | 04 §5.2 `PH2-04-GITOPS-WRITER-PAT` |
| 대상 저장소 | `seokpan/seokpan-hybrid-gitops` 1개 (Resource owner `seokpan`) | h-app #14 설정 항목 기록 |
| 권한 | Contents Read/Write · Pull requests Read/Write · Metadata Read-only. Organization 권한 0, Administration·Workflows 없음 | h-app #14 |
| 조직 승인 | 2026-10-06 | h-app #14 |
| 만료 | 2027-10-03 (무기한 가능 여부는 별도 확인 대상) | h-app #14 |
| 발급 계정 | `[보호 기록: 발급 계정 논리 참조]` | |
| 원본 보관 | SOPS+age, Automation CI 범위 파일. 주 보관 최유준, 예비 정태훈 (04 §5.3). `[보호 기록: 보관 논리 참조]` | |
| 등록 방식 | UI 수동 등록 = **임시 구성**(결정 E) | h-app #14 |
| 1차 Credential과의 관계 | `seokpan-gitops` 한정 1차 Credential과 별개. 재사용·변경하지 않음 | h-app #14 |

## 2. 통제 경계 (변하지 않는 규칙)

- 토큰 권한상 Merge·직접 Push가 기술적으로 가능하다. 실제 통제는 **Pipeline 정책 + main 보호**(필수 승인 1, Bypass 없음, deletion·non_fast_forward·pull_request 규칙)에 있다.
- CI는 Promotion Branch Push와 PR 생성까지만 한다. 자동 Merge·main Push·Apply는 없다. Merge는 사람이 한다.
- Argo(OpenShift GitOps)에 이 PAT를 복사하지 않는다.
- Required status checks가 없어 PR은 리뷰만으로 Merge 가능하다(별도 결정 사항).
- 모드 기본값 `PROMOTION_MODE=OFF`. 쓰기는 `WRITE`에서만, 대상 환경은 `recovery`만.

## 3. 검증 기록

| # | 일시(KST) | 대상 | 범위·결과 | 증거 |
| --- | --- | --- | --- | --- |
| V1 | 2026-10-06 | 사전 점검(수동, Jenkins Runtime 아님) | 조직 승인 후 인증 성공. 범위 밖 저장소(hybrid-app) Branch 생성 → `HTTP=403` | h-app #14 코멘트 |
| V2 | 2026-10-07 | 임시 Job `hybrid/d2-writer-check` Build 3 (삭제됨) | PUSH_OK → PR_CREATE 201(gitops #23 Draft) → PR_DUPLICATE 422 → OPEN_PR 1건 → PR_CLOSE 200 → Branch 삭제 | h-app #14 코멘트 |
| V3 | 2026-10-12 13:18 | Image Pipeline `main` #8, `--remote-check` | Credential 주입 단계 통과, `PROMOTION_STATUS=DRY_RUN`, 쓰기 없음, `Finished: SUCCESS` | 콘솔 로그 §4 |
| V4 | 2026-10-12 16:12 | Image Pipeline `main` #9, `--write` | `PROMOTION_STATUS=PR_CREATED` → [gitops #40](https://github.com/seokpan/seokpan-hybrid-gitops/pull/40), Release ID `rel-recovery-20261012T071253Z-4840f1aef85b-fa53d1ce`, `Finished: SUCCESS`. PR은 사람 리뷰 후 병합 | 콘솔 로그 §4 |

실행 컨테이너: Promotion 단계는 `app-ci`(git 2.47.3) Pod에서 실행됐다. 이전 검증(V2)의 `ci-python`(git 없음) 한계는 이 선택으로 해소됐다. 단, `app-ci`는 1차 Harbor 이미지 의존이다.

## 4. 콘솔 로그 Token 노출 점검

점검 대상은 V3·V4의 Jenkins 콘솔 전체 텍스트(각 974줄)이다. 로그 원문은 공개 저장소에 올리지 않고 SHA-256만 둔다.

| Run | SHA-256 (콘솔 로그 사본) | `github_pat_` | 기타 Token 패턴(`gh[pous]_`, `Bearer`, `x-access-token:`) | `GH_TOKEN=` 노출 | 마스킹 표시 |
| --- | --- | --- | --- | --- | --- |
| #8 | `c37e67533d4d0a31688ebe75860db214c2b9c08d4652e9fe2bdba453ca45feb4` | 0건 | 0건 | 0건 | `Masking supported pattern matches of $GH_TOKEN` 확인 |
| #9 | `8b6419379b8488c2d49492d2d1388bc6af1cc6bfbbfbfd47940d96c5f7aedfbf` | 0건 | 0건 | 0건 | 동일 확인 |

- 점검 방법: 로그 사본에 `grep -c`로 위 패턴 검색. 점검일 2026-10-13, 점검자 `최유준`.
- 한계: 콘솔 텍스트만 점검했다. 보관된 Artifact(`image-metadata.json`, promotion 결과 파일)와 Git 이력 전체는 이 점검 범위가 아니다. Jenkins가 값을 마스킹하므로 0건은 "노출 없음"의 근거이지 마스킹 우회 가능성의 부정이 아니다.

## 5. 폐기·교체 절차와 이력

**폐기 시점:** 프로젝트 종료 정리(10/26), 토큰 노출 의심 시 즉시, 발급 계정 권한 변경 시.

1. Jenkins `hybrid` Folder에서 `hybrid-gitops-writer` 삭제(또는 비활성)
2. GitHub Settings의 Fine-grained token `hybrid-gitops-writer` Revoke
3. 임시 Job으로 Push/PR **인증 실패** 확인(해당 시)
4. SOPS+age 보관본에 폐기 일자 기록

**교체:** 같은 설정(저장소 1개, Contents/PR write, Metadata read)으로 재발급 → 조직 승인 → Jenkins Credential 값 갱신(**ID 유지**) → 검증(V2 방식) 재수행.
**책임:** 등록·회수 최유준 / 배포·PR 경계 리뷰 정태훈.

| 일시 | 구분(발급/교체/폐기) | 사유 | 수행자 | 인증 실패 확인(폐기 시) | 보호 기록 참조 |
| --- | --- | --- | --- | --- | --- |
| 2026-10-02 | 발급 | 최초 발급, 조직 승인 대기 | 최유준 | - | `[기입]` |
| 2026-10-07 | Jenkins 등록 | 수동 등록(임시 구성) | 최유준 | - | `[기입]` |
| | 폐기(예정 10/26) | 종료 정리 | | `[결과·시각]` | |

## 6. 공개 금지 점검표 (커밋 전 확인)

- Token 값·접두어(`github_pat_` 등)·일부 문자열이 없다.
- 발급 계정명, AWS 계정 번호, ECR URI가 없다.
- 보호 보관 파일의 실제 경로·age Key·Recipient가 없다.
- 로그 원문이 없다(SHA-256만).
- 보호 기록 참조는 논리 이름만 있다.

## 7. 수신 확인 (HANDOFF 양식)

| 항목 | 기록 |
| --- | --- |
| 제공자 | 최유준 / 작성 2026-10-13 |
| 완료 범위 | 발급·등록·검증(V1~V4)·폐기 절차 문서화·로그 점검 |
| 미확인·남은 범위 | 실제 회수와 인증 실패 확인(10/26), Required status checks 채택 여부 |
| 확인자(정태훈) / 확인 시각 | `[기입]` |
| 판정 | 수락 / 일부 수락 / 보완 요청 / 보류 `[선택]` |
| 보완 사유·재제출 조건 | `[기입]` |

## 8. 알려진 한계

- 이 기록은 Credential 경로 검증이다. 실제 Image 공급·OCP/Cloud 배포·업무 수락은 별도 기록이다(gitops #32, h-app #13).
- V1의 main 보호 "필수 승인 1"은 설정 화면 확인이며 실제 Merge 시도로 입증한 것이 아니다.
