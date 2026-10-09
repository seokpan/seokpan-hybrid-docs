# B 관리 인증·조회 권한·Secret 공급 수락 절차

현재 진행:

- [x] 사람 GitHub IdP와 AWS Operator OIDC의 역할 분리.
- [x] Cloud 조회 Role/수동 Argo/Ingress 후보 및 입력 거부 시험 준비.
- [x] 관리 인증 수락 양식 검사와 권한 제거 후 기존/새 Session 검사 항목 준비.
- [ ] 실제 ROSA·GitHub Team/IdP·관리자/관측 Subject 및 실효 권한 수락.

승인03 §3-C의 Team 제한·목적 권한·Bootstrap 정리 조건을 실행 단계로 연결한다. Kubernetes Role은 **권한**, GitHub Team은 로그인 허용 대상, OpenShift User/Group은 실제 RoleBinding Subject다. Team 이름을 Group에 그대로 넣거나 AWS OIDC 준비를 사람 로그인 완료로 표시하지 않는다.

| 순서 | B가 준비/대조할 내용 | 실제 공급/실행 조건 | 남길 결과 |
|---|---|---|---|
| 1 | 정확한 ROSA Context·Cluster Identity·관리 Endpoint·기본 인증서 신뢰 대조 | A 실제 Cluster·지원 Version 인계 | 보호 경로의 대상 확인 기록. Token/전체 kubeconfig는 공개하지 않음 |
| 2 | GitHub Team allowlist·정상/대체 담당·callback·mapping method 결정 대조 | 실제 Team/멤버·OAuth App Owner·ROSA 해당 Version 지원 절차 | IdP 설정 개정/Owner. OAuth Client Secret은 Git/명령 기록/PR 본문에 넣지 않음 |
| 3 | 승인된 IdP 공급 경로에서 Secret 저장 위치·Owner/노출 범위 확인 | ROSA 지원 절차 채택, Secret 보호 인계 | Provider/IaC 사용 시 State의 Client Secret 노출/보호·회수 범위도 검토. 현 시점에 Terraform IdP Resource/Client Secret 추가 없음 |
| 4 | 정상 Team 새 로그인·비팀원 새 로그인 차단, OpenShift Subject 관측 | IdP 실제 적용 후 목적별 인증 | GitHub Team와 User/Group 매핑 대조. Secret 값/Token 없이 판정·개정·근거 참조 |
| 5 | 관측 Subject의 제한 RoleBinding 리뷰, B/담당 관리 권한과 일반 조회 권한 분리 | Namespace/Owner와 실제 User/Group 공급 | RoleBinding 이름·Subject·Role·Namespace 대조. 최소 조회 Role에는 Secret/ConfigMap·exec·portforward·생성/권한 수정 없음 |
| 6 | 조회 허용·Secret get/list/watch 거부·Pod 생성/exec/portforward 거부·다른 Namespace 거부 | 해당 조회 주체의 실제 Session | 양성/음성 결과. `oc auth can-i` 판정과 실제 지원되는 조회/거부를 함께 수락 |
| 7 | Team/RBAC 대상 제거 후 새 로그인 및 기존 Session/Token 재검증 | 정상 관리 경로·복귀 수단 확보, 지정 시험 주체 | Team 제거만으로 기존 Token이 즉시 폐기됐다고 주장하지 않음. 기존 Token 처리와 제거된 권한의 실효 거부 확인 |
| 8 | 정상/대체 관리자 접근과 Bootstrap Identity·Credential 사용처 목록 대조 | 실제 정상 경로 성공, 채택한 비상 접근 경로/보호 보관 검증 | 비상 htpasswd는 자동 채택하지 않음. 채택하지 않으면 그 결정과 대체 복구 경로를 따로 확인 |
| 9 | 별도 Owner 승인으로 불필요 Bootstrap 접근 정리, 정상/비상/제거 주체 재시험 | 1~8 실행 근거 및 승인, 실제 정리 권한 | 제거·잔존 사용처·재시험 기록. Source/양식 PASS를 정리 승인으로 사용하지 않음 |

`tools/b_preflight/management_acceptance.py`는 보호된 JSON 수락 기록의 필수 항목·상태·근거 참조 누락을 검사한다. POSIX 본인 소유 파일600, 최대64KiB와 기존 엄격 JSON Reader를 사용한다. 필드는 schema_version1·namespace·전체40자리 policy_revision·timezone 있는 observed_at·context_receipt·idp_receipt·emergency_path_required·case_results다. Case 이름은 도구의 `CASES`를 따르고 각 행은 status(pass/fail/not_run)와 evidence_ref(보호 논리 `receipt:...` 또는 해당 공개 GitHub 원본)다. 비상 경로를 채택하면 emergency_path, 미채택이면 emergency_not_adopted_review가 필요하다. Token·계정 정보·Client Secret 필드는 받지 않는다.

```bash
python3 tools/b_preflight/management_acceptance.py /private/reviewed-management-receipt.json
```

결과 `FORM_COMPLETE_OWNER_REVIEW_REQUIRED`는 제출된 양식이 완성됐다는 의미다. 제출 내용 진위/시각·실효 권한은 Owner의 실제 결과 대조가 필요하며 도구는 API 호출·인증·IdP/RBAC 변경·Bootstrap 정리를 수행하거나 승인하지 않는다. 실패/미실행 Case가 하나라도 있으면 BLOCKED다.

App Secret은 사람 IdP와 별도다. 환경별 Namespace의 DB Runtime·Migration·Redis AUTH·DB/Redis CA 및 Recovery Pull/서버 TLS/AUTH를 같은 승인 개정으로 공급한다. 일반 App에 Migration 인증정보를 넣지 않는다. Argo의 Workload 생성 권한은 Secret을 직접 읽지 않아도 Pod를 통해 사용할 수 있으므로 단순 Secret API 거부만으로 Writer를 완전히 격리했다고 주장하지 않는다. 실제 Secret/CA 교체·재접속은 새 Run의 업무 검증에서 확인한다.

남은 작업:

- [ ] A의 실제 Cluster/지원·담당/Team/OAuth Owner 입력 수신.
- [ ] 정상/차단 로그인·Subject·조회/거부·기존 Token·관리/비상 경로 검증.
- [ ] 별도 승인에 따른 Bootstrap 정리와 재시험.
- [ ] 환경별 Secret/CA 개정 공급·교체/업무 재접속 검증.

근거: [Kubernetes RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/), [권한의 간접 효과](https://kubernetes.io/docs/concepts/security/rbac-good-practices/), [ROSA Classic 설치의 IdP 설정](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html-single/install_rosa_classic_clusters/).
