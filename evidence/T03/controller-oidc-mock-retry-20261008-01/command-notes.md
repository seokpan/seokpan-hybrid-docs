# 교정 실행
terraform test -var-file=tests/oidc_mock.tfvars.json -filter=tests/oidc_issuer.tftest.hcl -no-color
기존 보호 harness·Core1.16.4/AWS6.67/RHCS1.7.7·합성 입력/두 mock_provider·plan2개·Backend 없음 대조 후1회 실행.
policy/version API/init/download 반복 없음. AWS/RHCS/TF 입력·debug 제거, 기존 로그 보존·새600로그/receipt.
Windows 별도 시험 사본 재현은 플랫폼 Lock 추가·단일파일 검색의 한계를 가진 로컬 근거이며 이 Linux 실제 결과와 구분.
