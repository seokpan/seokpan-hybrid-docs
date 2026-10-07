from pathlib import Path
import hashlib, json, re, subprocess, sys

BASE = '04285b1e19a470f182ccf0902af38da1018910fc'
NAMES = ['TJUNG03_EXECUTION_BOARD.md','TJUNG03_WORKFLOW_AND_LEARNING_GUIDE.md','WORK_TRACKER.md','05_IMPLEMENTATION_AND_VALIDATION.md','SOURCE_REVIEW_20261007.md','REPOSITORY_CONSISTENCY_AUDIT.md']
root = Path(sys.argv[1]).resolve()
original = {}
for name in NAMES:
    rel = 'execution/' + name
    original[name] = (root / rel).read_text()
    expected = subprocess.check_output(['git','show',BASE+':'+rel],cwd=root).decode()
    assert original[name] == expected, 'Source moved: '+name

CURRENT = '''## 현재 실행 기준 — 2026-10-07 재리뷰 대응·단계별 lab 활성화

| 경로 | 확인한 상태 | 직접 다음 조건 |
|---|---|---|
| App #17 | Source367938f 불변·전체1754/부분집합47 PASS. 조회된 승인은 기존 D 리뷰1건, 보완 결과의 새 제출은 미확인 | 기존 재검토 요청에 대한 제출 확인. 새 승인으로 꾸미지 않으며 병합·브랜치 삭제 보류 |
| App #18/#19 | #18 d624c830의 CI 중복/명령 순서 보완·1752/47/별도Lua9 PASS. #19 f548f921의 cleanup RedisError/취소 전파 보완·1760/47/부분집합8 PASS | 최신 HEAD 재리뷰. 실제 승인·병합 조합 전체 검사 → D Build/Scan/Digest → B App·별도 Migration 소비 |
| GitOps #20 | b13ae957 metadata allowlist·음성 회귀 보완, 전체58 PASS. A Changes requested 대응 후 A/D 재리뷰 요청 | Controller 등록 비교와 Valkey Stage-1 Gate는 별도. 아래 단계와 원 #5 인계 적용 |
| Infra #40 | C 승인 HEAD c1a495bc → main a0da58c3 병합·작업 브랜치 삭제 확인 | Source/Metadata 수정 완료. 실제 운영 Data·Valkey·Backup/Recovery·전체 T18은 미검증 |
| Cloud 금고 | 기존 본체 해독 보고/B 수신 완료. 독립 복원 시도는 파일 검사에서 BLOCKED | 독립 매체의 키/암호문을 복원 폴더에 실제 복사한 뒤 본인 jth로 재검사. 새 키 생성/Token 노출 금지 |
| ROSA·비용 | clone 확인 시 경로/필수 파일 단계에서 진단 없이 중단. 원장(3)은 PARTIAL·미완19·기타미확인4 | clone 준비/진단 → Caller/Backend·지원·예비 비용. 실제 Plan에 A 제한 출력/prerequisite와 C SG2. CP/Infra/Worker3 유지, 실제 사양·기간 임의 입력 금지 |

D가 lab Stage-1 실행 입력 PR과 Controller 등록 PR을 작성하고 B가 Source·배포 경계를 리뷰할 수 있다. Stage1은 **lab Valkey만 replicas1/source-reviewed-runtime-unverified**, FE/BE는0/input-required다. base/Recovery hold와 기존 전체 release-manifest는 보존한다. 별도의 Valkey Stage-1 Preflight Gate를 Source에 구현·검증한 뒤 해당 Valkey 리소스만 선택 수동 Sync한다. #20 등록 checker가 Stage-1 Gate를 대신하지 않는다.

Workload PR 병합 SHA A → 등록 PR targetRevision SHA A → 실제 공유 사용창/등록·Stage1 Gate/live Diff·Valkey 선택 Sync → DB/Secret/CA/Route 수락 → FE/BE 활성화 SHA B → 등록 Source targetRevision 갱신 → 전체 release-manifest 정상 통과 → 최초 FE/BE 수동 Sync다. 등록 PR 자기 SHA 참조, 자동 Sync/Prune/finalizer, 전체 Runtime PASS 승격은 하지 않는다.

원본: [GitOps #5 최신 인계](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5#issuecomment-6032629690)·[Cost #43 대조](https://github.com/seokpan/seokpan-hybrid-docs/issues/43#issuecomment-6033030041)·[Source §9](SOURCE_REVIEW_20261007.md#b-review-resume-20261007)·[본인 직접 실행](TJUNG03_WORKFLOW_AND_LEARNING_GUIDE.md#b-direct-actions-20261007). Docs #69는 병합됐고 보존 브랜치가 main보다 앞선 Commit0·변경파일0이므로 삭제 가능하다. 실제 삭제는 별도이며 이번에는 보존한다. Docs #72는 관련 PR 상태를 반영하되 병합 대기한다. TH81/실제 완료2와 기존 Q 체크를 유지하며 Q02/03/04/05/10 전체 수렴은 아직 미완료다.

'''

def replace_current(text):
    start = text.index('## 현재 실행 기준 — ')
    end = text.index('\n## ',start+3)+1
    return text[:start]+CURRENT+text[end:]

for name in NAMES[:4]:
    (root/'execution'/name).write_text(replace_current(original[name]))

guide = root/'execution/TJUNG03_WORKFLOW_AND_LEARNING_GUIDE.md'
text = guide.read_text()
marker = '<a id="b-direct-actions-20261007"></a>'
start = text.index(marker)
old_direct = text[start:]
blocks = re.findall(r'```bash\n(.*?)\n```',old_direct,re.S)
assert len(blocks) == 3
restore = blocks[1]
restore = restore.replace('read -r -p \'독립 매체에서 복원한 폴더의 절대경로: \' DIR', 'DIR=${1:-}\nif [[ -z $DIR ]]; then\n  read -r -p \'파일 2개를 복원한 폴더의 절대경로: \' DIR || { echo \'BLOCKED: 입력 없음\'; exit 1; }\nfi')
restore = restore.replace('[[ $DIR == /* && -d $DIR && ! -L $DIR && -O $DIR ]] || exit 1', '[[ $DIR == /* && -d $DIR && ! -L $DIR && -O $DIR ]] || { echo \'BLOCKED: 폴더 절대경로·존재·jth 소유자를 확인하세요.\'; exit 1; }\nchmod 700 -- "$DIR"')
restore = restore.replace("echo 'BLOCKED: 복원 파일·소유자를 확인하세요.'", 'printf \'BLOCKED: 파일 없음/일반파일 아님/링크/소유자 불일치: %s\\n\' "$file"')
restore = restore.replace('PUBLIC=$(age-keygen -y "$KEY" 2>/dev/null)', 'PUBLIC=$(age-keygen -y "$KEY" 2>/dev/null) || { echo \'BLOCKED: 복원 개인키 형식 확인 실패\'; exit 1; }')
restore = restore.replace('[[ $SOPS_BIN == /* && -x $SOPS_BIN ]] || exit 1', '[[ $SOPS_BIN == /* && -x $SOPS_BIN ]] || { echo \'BLOCKED: sops 실행파일 경로 확인 필요\'; exit 1; }')
restore = restore.replace('env -i PATH=', 'if ! env -i PATH=')
restore = restore.replace('SOPS_AGE_KEY_FILE="$KEY" "$SOPS_BIN" decrypt', 'GNUPGHOME="$ISOLATED/.gnupg" AWS_EC2_METADATA_DISABLED=true \\\n  SOPS_AGE_KEY_FILE="$KEY" "$SOPS_BIN" decrypt')
needle = "raise SystemExit(0 if re.fullmatch(r\"[0-9a-f]{64}\\n?\", v) else 1)'"
assert needle in restore
restore = restore.replace(needle, needle+"; then\n  echo 'BLOCKED: 복원 키 복호화 또는 Token 형식 검사 실패. 값은 보내지 마세요.'\n  exit 1\nfi")

rosa = blocks[2]
old_input = rosa[rosa.index("read -r -p '본인 seokpan-hybrid-infra clone의 절대경로: '"):rosa.index('git status --short --branch')].rstrip()
new_input = '''command -v git >/dev/null || { echo 'BLOCKED: git 도구 없음'; exit 1; }
CREATE=no
if [[ ${1:-} == --create-if-missing ]]; then CREATE=yes; shift; fi
REPO=${1:-"$HOME/work/seokpan-hybrid-infra"}
[[ $REPO == /* ]] || { echo 'BLOCKED: clone의 절대경로를 지정하세요.'; exit 1; }
if [[ ! -e $REPO ]]; then
  [[ $CREATE == yes ]] || { printf 'BLOCKED: 폴더 없음: %s. 최초 clone은 --create-if-missing 옵션 사용\\n' "$REPO"; exit 1; }
  mkdir -p -- "$(dirname -- "$REPO")"
  git clone https://github.com/seokpan/seokpan-hybrid-infra.git "$REPO" || { echo 'BLOCKED: clone 실패·네트워크 확인'; exit 1; }
fi
[[ -d $REPO && ! -L $REPO && -O $REPO ]] || { echo 'BLOCKED: clone 폴더·jth 소유자·심볼릭 링크 확인'; exit 1; }
cd -- "$REPO"
TOP=$(git rev-parse --show-toplevel 2>/dev/null) || { echo 'BLOCKED: Git clone이 아닌 폴더'; exit 1; }
[[ $TOP == "$(pwd -P)" ]] || { echo 'BLOCKED: clone 최상위 경로를 지정하세요.'; exit 1; }
REMOTE=$(git remote get-url origin 2>/dev/null) || { echo 'BLOCKED: origin 없음'; exit 1; }
case "$REMOTE" in
  https://github.com/seokpan/seokpan-hybrid-infra|https://github.com/seokpan/seokpan-hybrid-infra.git|git@github.com:seokpan/seokpan-hybrid-infra.git) ;;
  *) echo 'BLOCKED: origin이 예상 Infra 저장소와 다름. URL의 인증정보는 공유하지 마세요.'; exit 1 ;;
esac
for file in terraform/rosa/LOCAL_PREPARATION.md scripts/tf-session.sh terraform/rosa/.terraform.lock.hcl; do
  [[ -f $file ]] || { printf 'BLOCKED: 필수 파일 없음: %s. 오래된 checkout/경로 확인. 개인 변경을 버리지 마세요.\\n' "$file"; exit 1; }
done'''
assert old_input in rosa
rosa = rosa.replace(old_input,new_input)
rosa = rosa.replace('git fetch origin main', "git fetch origin main || { echo 'BLOCKED: fetch 실패·네트워크/접근 확인'; exit 1; }")

PROCEDURE = '''<a id="b-direct-actions-20261007"></a>
## 본인 직접 실행 — 복원 파일 준비와 clone 진단 (재개 개정)

### A. 금고 오류가 의미하는 것

제공된 로그는 `restore-check.M14I3E` 폴더 생성 뒤 필요한 두 파일을 검사하다 중단됐다. 아직 SOPS 복호화 단계에 도달하지 않았으므로 키 불량·Token 불량으로 판정하지 않는다. 파일 부재/이름/소유자 중 어느 조건인지는 그 로그만으로 확정할 수 없다. `mktemp -d`는 빈 폴더만 만들며 독립 매체의 파일을 복원하지 않는다. 복붙 로그의 `)rintf`도 정상 코드는 아니므로 중간에 잘린 명령을 재사용하지 않는다.

**작업 장소 1 — Controller, jth SSH 세션.** 이미 만든 폴더를 사용한다. 없으면 새 임시 폴더를 만들고 그때 출력된 경로를 사용한다. 아래는 새 키를 만들거나 기존 키를 덮어쓰는 명령이 아니다.

```bash
id -un
ls -ld "$HOME/secrets/seokpan/restore-check.M14I3E"
ls -l "$HOME/secrets/seokpan/restore-check.M14I3E/restored-age-key.txt" \\
  "$HOME/secrets/seokpan/restore-check.M14I3E/foundation-data.sops.yaml"
```

**작업 장소 2 — Controller 밖의 본인 PC/독립 매체.** 기존 개인키의 독립 사본과 해당 암호문이 먼저 있어야 한다. 없는 경우 본인 SSH/SFTP 경로로 Controller의 기존 `~/.config/sops/age/keys.txt`와 `~/secrets/seokpan/foundation-data.sops.yaml`을 본인이 통제하는 암호화된 별도 디스크/매체에 보관한다. 기존 키를 `age-keygen`으로 새로 생성하지 않는다. 다른 사람의 키/계정을 받지 않으며 채팅·메일·Git·공용/동기화 폴더로 보내지 않는다. 같은 Controller의 다른 폴더는 독립 사본이 아니다.

그 **독립 매체에 보관한 사본에서** Controller로 다시 전송한다. SFTP를 쓰면 원격 폴더는 위 `restore-check.M14I3E`, 파일 이름은 아래와 정확히 맞춘다. 원본 개인키를 화면에서 열거나 복사/붙여넣기할 필요가 없다.

| 독립 매체에서 읽을 파일 | Controller 복원 폴더 안 이름 |
|---|---|
| 기존 본인 age 개인키 사본(예: keys.txt) | restored-age-key.txt |
| C가 공급한 암호문 사본 | foundation-data.sops.yaml |

Windows PowerShell의 SCP를 사용한다면 아래 입력에 **현재 실제 SSH 주소/포트와 독립 매체의 파일 경로**를 지정한다. 터미널 프롬프트의 `ansible` 이름을 Windows에서 해석 가능한 주소라고 가정하지 않는다. 전송은 본인 PC와 본인 Controller 사이에 한정한다.

```powershell
$Controller = Read-Host '현재 SSH 접속에 쓰는 Controller 주소'
$Port = Read-Host 'SSH 포트 (기본이면 22)'
$KeyCopy = Read-Host '독립 매체의 기존 개인키 파일 절대경로'
$CipherCopy = Read-Host '독립 매체의 foundation-data.sops.yaml 절대경로'
if (!(Test-Path -LiteralPath $KeyCopy -PathType Leaf) -or !(Test-Path -LiteralPath $CipherCopy -PathType Leaf)) { throw '독립 사본 파일부터 확인하세요.' }
$Restore = '/home/jth/secrets/seokpan/restore-check.M14I3E'
scp -P $Port $KeyCopy "jth@${Controller}:$Restore/restored-age-key.txt"
if ($LASTEXITCODE -ne 0) { throw '개인키 사본 전송 실패' }
scp -P $Port $CipherCopy "jth@${Controller}:$Restore/foundation-data.sops.yaml"
if ($LASTEXITCODE -ne 0) { throw '암호문 사본 전송 실패' }
```

새 폴더를 만들었다면 `$Restore`만 실제 출력 경로로 바꾼다. SSH 서버 신원 경고가 나오면 기존 접속 정보와 확인하고 무시하는 옵션을 추가하지 않는다. 전송 후 다시 Controller jth 세션에서 위 `ls -l`로 두 파일·소유자를 확인한 뒤 다음 검사를 실행한다.

### A.1 Controller에서 복원 키만 사용해 검사

전체 블록을 실행하거나 동일 내용의 `verify-restored-vault-v4.sh`를 Controller의 `~/work/seokpan-checks/`에 저장해 `bash ~/work/seokpan-checks/verify-restored-vault-v4.sh /home/jth/secrets/seokpan/restore-check.M14I3E`로 실행한다. 기존 기본 키로 우연히 성공하지 않도록 빈 HOME·격리 환경과 지정 복원 키만 사용한다. Token은 파이프로 형식 검사하고 출력/평문 파일/명령 인자로 남기지 않는다.

```bash
RESTORE_CODE
```

성공 회신은 `본인 복원 키·해독·형식: OK`, `암호문 확인값: 9a86f90e6ba6`, 그리고 본인이 확인한 `Controller 밖 독립 매체에서 복원함`이다. 12자리 확인값은 기존 암호문 개정 비교용 단축값이며 완전한 SHA256 일치 증명이 아니다. 실패하면 BLOCKED 단계만 보내고 개인키/Token은 보내지 않는다. 검사기는 파일의 독립 매체 출처 자체를 증명하지 못한다. 성공 뒤 검사용 복원 사본은 필요한 사용을 마치고 두 지정 파일/빈 폴더만 정리하되 원본 키·독립 보관본은 보존한다.

### B. ROSA clone — 같은 Controller의 jth에서 실행

제공된 로그만으로 `/home/jth/work/seokpan-hybrid-infra`가 없었는지, 내부 필수 파일이 없었는지 확정할 수 없다. 이전 명령은 이 검사 실패에 메시지가 없었다. 아래 개정은 해당 원인을 출력하고, **최초 clone이 없을 때만 명시적 옵션으로 새 clone**을 만든다. 이미 있는 디렉터리/개인 변경은 덮어쓰지 않는다.

아래 블록을 `rosa-local-check-v4.sh`에 저장한 뒤 처음에는 `bash ~/work/seokpan-checks/rosa-local-check-v4.sh --create-if-missing /home/jth/work/seokpan-hybrid-infra`로 실행한다. 기존 clone이 다른 곳에 있으면 마지막 경로만 실제 최상위로 바꾼다. 현재 셸에 긴 코드를 붙여 넣는 대신 파일로 저장해 실행하면 코드 중간 잘림을 피할 수 있다.

```bash
ROSA_CODE
```

코드·Lock 차이가 있어도 reset/stash/upgrade/자동 pull을 하지 않는다. 도구 PRESENT는 지원/버전/권한 검증이 아니며 MISSING은 해당 준비의 남은 입력이다. 필요한 설치는 기존 고정 버전과 공유 Controller 영향을 확인한 뒤 별도 처리한다. 기준은 Infra `terraform/rosa/LOCAL_PREPARATION.md`의 Core1.16.4·AWS6.67.0·RHCS1.7.7이다. 본인 실제 clone·도구·Caller·Backend가 확인되기 전 ROSA Plan 준비 완료로 표시하지 않는다.

**회신:** HEAD/origin-main, 개인 변경 유무, Local/Origin Lock 식별값, 도구 MISSING 목록과 TF/AWS 버전, 작업 가능한 일시. 자격증명·환경변수 전체·State·tfvars 내용은 보내지 않는다. 이 단계에는 tf-session source/init/plan/apply·oc apply·AWS/RHCS 서비스 호출을 추가하지 않는다.
'''
PROCEDURE=PROCEDURE.replace('RESTORE_CODE',restore).replace('ROSA_CODE',rosa)
guide.write_text(text[:start]+PROCEDURE)

SOURCE_ADD='''

<a id="b-review-resume-20261007"></a>
## 9. 중단된 재리뷰 대응의 게시·산출물·현재 입력 확인

이 절은 §8 이후의 개정이다. 이전 Source/시험/리뷰는 고정 이력으로 보존하며 전체 S1–S4 완료를 뜻하지 않는다.

| 원 작업 | 최신 Source/상태 | 검증과 남은 조건 |
|---|---|---|
| App17 | 367938f08e735fe123827b3c9362307b5d59408f, open | 기존 APPROVED commit_id가 동일한 사실과 보완 결과에 대한 새 제출 미확인을 구분. 원 댓글6032849213의 재검토 요청 유지 |
| App18 | d624c83081f18ad81c793cfe39e81ce6075abfba, 재리뷰 대기 | Run37583252239: 전체1752/부분집합47/별도Lua9·failure/error/skip0·clean. Artifact11465476865 ZIP7430b6ee49f3d3cb96a3842115b6ac250baa51d75e3ca12450966e9a5240828f 재확인 |
| App19 | f548f921c436d614a3fe0b3969161b8d1433ab5f, 재리뷰 대기 | Run37584439948: 이전1cc717+새8Case에서4FAIL/4PASS→최종8PASS, 전체1760/부분집합47·clean. Artifact11465659044 ZIPbc51bad5ac7b6025ed4e7e5ad1cc1383c6b697825d56a8178f53e8c0bafc09f1 재확인 |
| GitOps20 | b13ae9575206a335a9e6f87efc34dd4c198884f7, A/D 재리뷰 대기 | Run37583920937 전체58PASS·8진단Render/26객체. Artifact11465856605 ZIP9e1056f9f37e6fa4fc113ff1176d0160e127c366a3ddfc856481589e50be925b, Source/8YAML hash 대조 |
| Infra40 | a0da58c345f877659e522a5b4ab5392b1d0626d3 병합, 브랜치 삭제 | C 승인5438510467·Source3파일·기존10단위검사. 삭제Run37583271261·branches 재조회 확인. 실제 Data/T18은 별도 |

App18은 D의 중복 push/PR CI·로컬 opt-in 순서 제안을 수용했고 필수검사 전환/캐시 추가는 별도 범위로 유지했다. App19는 RedisError가 취소를 가리는 경계를 실제 대역 회귀로 재현해 RedisError만 억제하고 원 취소를 전파한다. 정리 시도1회가 정리 성공을 보장하지 않는다. 첫 Run37583804408의 Ruff SIM105 실패는 정책 비활성화 없이 suppress 표현으로 정정한 뒤 재시험했다. GitOps20은 A의 metadata 지적에 annotation exact allowlist·빈 labels·추가 metadata 음성 검사를 보완했다. 기존 승인/Changes requested를 임의로 최신 승인으로 바꾸지 않았다.

세 ZIP의 실제 바이트 SHA256·CRC, App JUnit/summary·clean Source, GitOps Render hash를 재검증했다. App19의 Docs workflow trigger61874395와 검사 대상 Appf548f921은 다르다. 개별 Source CI를 결합 main/새 Image/실제 Valkey·Controller·전체 업무 PASS로 합치지 않는다.

lab의 최신 D작성/B리뷰·Stage1 전용Gate·SHA A/B 순서는 [원 #5 인계](https://github.com/seokpan/seokpan-hybrid-gitops/issues/5#issuecomment-6032629690)로 연결한다. Stage1 PR에서는 unittest뿐 아니라 기존 Source workflow의 진단 Render에도 모든 Workload replicas0 검사라는 직접 의존이 있다. 이 검사를 삭제/우회하지 말고 승인 Stage1 경계를 반영한다. FE/BE/base/Recovery/Migration 보류를 보존하며 실제 Stage1 Gate 구현은 D의 후속 PR이다.

Cost는 [원 #43 대조](https://github.com/seokpan/seokpan-hybrid-docs/issues/43#issuecomment-6033030041)를 따른다. 파일(3) SHA2561e7186febf71e16f72d6a92c406b9d1709e8e64839a8101fb913c4f126644383, 저장 판정 PARTIAL/미완19/입력오류0/기타4다. CP3/Infra3/Worker3 유지, 필수 disk와 실제 LB/Volume/Window/Destroy·가용시간은 미확인이다. 읽기 도구의 일부 수식 해석 차이를 원본 파일 오류로 단정하거나 재저장하지 않았다. 과거 단가를 새 검증 가격으로 승격하지 않는다.

본인 금고 시도는 복원 파일 검사에서, clone 시도는 경로/필수파일 초기 검사에서 중단돼 실제 복호화/Cloud 권한 실패로 판정하지 않는다. [직접 실행 안내](TJUNG03_WORKFLOW_AND_LEARNING_GUIDE.md#b-direct-actions-20261007)에 준비·전송·정확한 파일명·누락 진단·검사·회신을 반영했다. 명령의 문법/합성 검사는 본인 Runtime 성공이 아니다. 00–04/Project v3/그림/TH81·완료2는 변경하지 않는다.
'''
p=root/'execution/SOURCE_REVIEW_20261007.md'
p.write_text('> **현재 재개 기준:** [§9](#b-review-resume-20261007). §1–8의 수치/상태는 해당 시점의 이력이다.\n\n'+original[p.name]+SOURCE_ADD)
p=root/'execution/REPOSITORY_CONSISTENCY_AUDIT.md'
s=original[p.name].replace('최신 리뷰·경로 A·Source 후속은 [§11](#b-review-followup-audit-20261007)', '최신 재리뷰·lab/비용·본인 진단은 [§12](#b-review-resume-audit-20261007), 이전 리뷰·경로 A·Source 후속은 [§11](#b-review-followup-audit-20261007)',1)
s+='''

<a id="b-review-resume-audit-20261007"></a>
## 12. 재리뷰 대응 재개·Docs72 반영·본인 실행 안내

[Source §9](SOURCE_REVIEW_20261007.md#b-review-resume-20261007)에 최신5개PR·리뷰 원문·3개ZIP/시험·Infra40 병합/삭제·lab Stage1/2·Cost 원장(3)·금고/clone 실패 단계를 대조했다. 이미 게시된 App18/19/GitOps20 수정을 중복 생성하지 않았다. Docs69 보존 브랜치는 main 대비 ahead0/files0라 삭제 가능하지만 이번에는 실제 삭제하지 않는다. Docs72는 관련 PR 상태 변동을 반영한 뒤 병합 대기를 유지한다.

문서4개의 단일 현재 구획을 갱신하고 학습 안내의 직접 실행 구획을 보완했다. 나머지 원본문·C의05 §8.9–8.14·Tracker 원행·Shared Execution·기존TH/Q 체크·설계/그림·Evidence는 보존한다. 새 Runtime 결과가 없으므로 TH81/실제 완료2를 바꾸지 않는다. D의 Stage1 후속에는 테스트뿐 아니라 CI 진단의 replicas0 조건도 함께 인계한다.

이번 요청의 미처리 상태/안내 보완과 전체 전수 의미 검토는 구분한다. Q02/Q03/Q04/Q05/Q10은 미완료다. 다음 출발점은 S1 Room/Session/연결세대·Frontend의 남은 Source/시험 → S2 Recovery/Writer/Promotion 직접 연결 → S3 도달 diff/CI/참조 의미 검토 → S4 최종 원격 변화 대조다. 금고 독립 복원·ROSA 본인 도구/Caller·lab 입력과 비용 준비는 직접 조건에 따라 병행한다.
'''
p.write_text(s)
for name, heading in [('05_IMPLEMENTATION_AND_VALIDATION.md','### 9.44 재리뷰 대응 재개와 단계별 lab·비용·본인 진단'),('WORK_TRACKER.md','## B 재개 인계 — 재리뷰·lab 단계·Cost·직접 실행')]:
    p=root/'execution'/name
    with p.open('a') as f:
        f.write('\n\n'+heading+'\n\n[Source §9](SOURCE_REVIEW_20261007.md#b-review-resume-20261007)·[대장 §12](REPOSITORY_CONSISTENCY_AUDIT.md#b-review-resume-audit-20261007)와 상단 현재 구획을 따른다. Infra40 병합/삭제, App18/19/GitOps20 재리뷰, App17 새 제출 확인, D Stage1 Gate/등록 입력과 B 리뷰, Cost PARTIAL 및 본인 복원/clone 진단을 원 작업에 연결한다. 실제 사용창·본인 키/Caller·배포·T18·비용 수락은 별도다. C 기록·과거 결과/체크/Shared Execution은 보존한다.\n')

for name in NAMES:
    s=(root/'execution'/name).read_text()
    assert re.findall(r'(?m)^.*\[[ x~]\].*$',s) == re.findall(r'(?m)^.*\[[ x~]\].*$',original[name]), 'Checkbox changed: '+name
for name in NAMES[:4]:
    before=original[name]
    end=before.index('\n## ',before.index('## 현재 실행 기준 — ')+3)+1
    tail=before[end:]
    if 'WORKFLOW_AND_LEARNING' in name: tail=tail.split(marker)[0]
    assert tail in (root/'execution'/name).read_text(), 'Historic/C section changed: '+name
for label, code in [('restore',restore),('rosa',rosa)]:
    check=subprocess.run(['bash','-n'],input=code,text=True,capture_output=True)
    assert check.returncode==0,(label,check.stderr)
print(json.dumps({'files':6,'current_sections':4,'checkboxes':'preserved','historic_and_C_sections':'preserved','bash_syntax_only':2,'user_runtime':'NOT RUN','global_Q10':'INCOMPLETE'},ensure_ascii=False))
print(json.dumps({n:hashlib.sha256((root/'execution'/n).read_bytes()).hexdigest() for n in NAMES},indent=2))
