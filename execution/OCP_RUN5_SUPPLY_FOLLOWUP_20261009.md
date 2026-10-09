# Run #5 OCP 공급 후속 수신·push 판단 — 2026-10-09

D에게 받은 공급 보고를 기존 공개 기록과 대조했다. B의 Harbor/bastion/Cluster 직접 실행·검증 결과가 아니다. 실제 공급 이슈는 [GitOps #32](https://github.com/seokpan/seokpan-hybrid-gitops/issues/32)이며 Infra #32는 다른 작업이다.

## 새로 수신한 범위

- D 보고: 승인 Run #5 FE/BE를 OCI layout으로 복사해 Index descriptor·blob 해시를 대조했고, bastion 반입 tar와 해제본도 일치. tar SHA-256 `4bc9887ba29ca00e8df6659a440b55a6c3ad73e276ae0a900256256ad57e2c4b`.
- Source `188199630ceb5fd67d8fe57d4d5650694e2e00e3`, 전용 태그 `git-188199630ceb`. 승인 Index는 [기존 B 수락](https://github.com/seokpan/seokpan-hybrid-gitops/issues/32#issuecomment-6060263976)에 따른다.
- D가 전달한 child/attestation은 접두어만이므로 B의 전체 Digest 대조는 미완료. 실제 내부 Index/child mapping은 push 뒤 공급 예정. tar의 B 직접 해시 검사나 OCP 공급 완료로 표시하지 않는다.
- Registry 가용190G(197G 중6.9G 사용), keepTagRevisions3, Namespace ResourceQuota/LimitRange 없음 보고 수신. Worker requests는 worker-1 6797Mi/worker-2 6539Mi(99%/95%), requests 여유14.5Mi/272.5Mi 보고다. 최신 실사용·Pressure/종료 Pod·실행창 판정은 별도다. 정확한 자원 관측 시각은 미공급.
- 09:00 Pruner와 Backend Pod 교체 동시 관측 보고 수신. 인과관계는 미확정이며 D 감사 기록 후 판단한다. 다음09:00을 피해도 자원 Gate가 자동 통과하는 것은 아니다.

## 10/06 기록과 이번 방식

[10/06 FE/BE 공급 기록](https://github.com/seokpan/seokpan-hybrid-gitops/issues/14#issuecomment-6016144794)은 `skopeo copy --all --preserve-digests`, TLS 검증 유지, 전용 임시 push 권한, 내부 Service 주소로 노드 Pull4건을 기록한다. **bastion의 당시 push endpoint는 확인되지 않았다.** 노드 Pull 주소를 그대로 bastion push 주소로 단정하지 않는다.

권고는 D가 OCI 복사에 실제 사용한 Skopeo 컨테이너의 고정 image Digest·버전을 bastion에서 재사용하고, 입력 OCI layout과 필요한 authfile/CA를 제한해 연결하는 방식이다. Worker Pod나 privileged/컨테이너 엔진 socket은 필요하지 않다. `--rm`은 실행 컨테이너를 정리하며 도구 Image까지 지웠다는 뜻이 아니다. 설치/제거에 따른 host 의존성 변경이 없는 컨테이너 방식을 우선한다. [Red Hat의 Skopeo 컨테이너·authfile 안내](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/building_running_and_managing_containers/assembly_running-skopeo-buildah-and-podman-in-a-container)를 참고한다.

`--all`로 Index가 가리키는 전체 Image와 Index를 복사하고 `--preserve-digests`로 보존 불가 시 중단한다. OCI layout을 직접 읽으며 podman storage 변환·`--format`으로 승계하지 않는다. [Skopeo copy 공식 옵션](https://github.com/containers/skopeo/blob/main/docs/skopeo-copy.1.md)을 대조했다. blob 해시 일치는 내용 전송 일관성이며 attestation 서명/Source 진위 검증의 완료를 뜻하지 않는다.

현재 bastion에서 연결·DNS·CA/TLS 검증이 되는 기존 endpoint를 선택한다. 외부 Route가 이미 있으면 실제 host를 확인하고, 내부 Service를 쓰려면 bastion에서 실제 접근이 가능해야 한다. 확인되지 않은 Route host를 만들어 안내하거나 새 Route/TLS 해제를 이번 공급 준비에 추가하지 않는다. 대상은 `<endpoint>/seokpan-argotest/backend:git-188199630ceb`와 `frontend:git-188199630ceb`다. [OpenShift Registry 접근 문서](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/registry/accessing-the-registry)의 Namespace/권한 경계도 유지한다.

## Registry push와 App 교체의 분리

기존 지정 공급 범위·Owner 사용창이 유효하고 endpoint/TLS·push 권한·현재 Pruner 상태를 확인한 뒤 공급 단계 진행 가능하다. bastion push는 Worker 신규 Pod의 requests를 추가하지 않지만 기존 Registry 자원·스토리지/네트워크 부하가 있다. [ImageStream 변경 trigger](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/images/triggering-updates-on-imagestream-changes)가 Workload/Build를 자동 시작할 수 있으므로 새 태그 구독이 없는지 현재 Namespace에서 확인한다. 고정 GitOps Source FE/BE에 trigger가 없다는 확인을 live 확인으로 승계하지 않는다.

push 뒤 실제 endpoint·도구/버전·시각, 원본/내부 Index·amd64 child·attestation 전체 Digest, ImageStream/Registry raw manifest 대조를 인계한다. 보존 실패 시 중단하며 아키텍처 하나만 추출해 승인 Index와 같다고 표시하지 않는다. 기존 태그·10/06 tar는 보존한다.

Promotion·노드 Pull은 실제 내부 mapping 대조 뒤, FE→BE 교체는 추가로 양 Worker 최신 requests/실사용·Pressure·종료 Pod·Pruner·Owner 창 확인 뒤 진행한다. Pruner/Backend 사건은 audit 주체/삭제 또는 eviction 이유·OOM/Pressure·ReplicaSet/이미지 변화를 연결해 판단한다. 원인 미확정 상태에서 Pruner/HPA/requests를 임의 변경하지 않는다.

## B 선행 도구와 A 인계의 현재 상태

PR #97 도구의 Infra5·GitOps11개 원격 파일 SHA-256, lab 렌더 및 fixture 필드 대응을 다시 대조했고 SG/Plan10·OCP계산5 시험 그룹 통과. Windows에서의 합성/Source 검증이며 실제 Linux Controller 시험은 별도다. 이 오프라인 시험은 PR 병합을 기다릴 기술적 이유가 없으므로 운영 clone을 건드리지 않는 고정 임시 사본으로 먼저 확인할 수 있다. A/C 실제 값·인증/Cloud/State 호출이나 설치는 필요하지 않으며, OCP 계산은 기존 PyYAML이 있을 때만 실행한다. 이후 기존 Controller의 Linux 파일3건·SG/Plan10·OCP계산5 시험 PASS와 임시 사본 제거 결과를 수신했다. [부분 검증 기록](../evidence/T03/controller-b-offline-tools-20261009-01/summary.md)에 연결했으며 재실행·설치는 필요하지 않다.

[Infra #54](https://github.com/seokpan/seokpan-hybrid-infra/pull/54)는 B의 최신 HEAD `d82f09a4013d40ab754f85997f358a8a1fc44a64` 승인 및 A 병합 대기를 확인했다. B의 재리뷰를 반복하거나 A 구현을 B 작업에 넣지 않는다. bootstrap 실제 Plan/실효 권한 확인 → Foundation 전체 Plan/Cost Gate·실행 조건 → 실제 적용·보호 인계는 A의 후속이며 실제 ARN·권한·SG 인계를 완료한 것으로 승계하지 않는다.

## C의 합의와 실제 결과 대기 구분

C의 같은 회신은 앞서 대화에서 이미 전달받았다. [Infra #19의 SG 인계·Pool 결정 시점 합의](https://github.com/seokpan/seokpan-hybrid-infra/issues/19#issuecomment-6059291050)와 [Infra #44의 이관 순서·절차 준비/실제 확인 대기](https://github.com/seokpan/seokpan-hybrid-infra/issues/44#issuecomment-6059308630)도 확인했다. 동일 메신저 문구를 GitHub에서 발견했다고 주장하지 않는다. SG 대조 방식·Pool 결정 시점·이관 순서의 동의를 다시 기다리지 않는다. C의 실제 SG 판정은 Foundation Apply 직후 #19 기록으로, Pool 값은 RDS 실측 뒤로, 1차 접근 계정·위치는 이관 날짜와 함께 확정하는 후속으로 유지한다.
