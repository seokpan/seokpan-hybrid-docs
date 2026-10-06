#!/usr/bin/env python3
"""Apply reviewed Markdown edits and B-owned body corrections, never Runtime changes."""
import hashlib
import json
import os
from pathlib import Path
import re
import urllib.request


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def require(value, message):
    if not value:
        raise RuntimeError(message)


def transform(before, item):
    require(digest(before) == item['before_sha256'], 'Preimage changed; do not overwrite')
    lines = before.splitlines(keepends=True)
    end = len(lines)
    for first, last, text in reversed(item['edits']):
        require(0 <= first <= last <= end, 'Invalid or overlapping edit')
        lines[first:last] = text.splitlines(keepends=True)
        end = first
    after = ''.join(lines)
    require(digest(after) == item['after_sha256'], 'Reviewed output hash mismatch')
    require(re.findall(r'\[[ xX]\]', before) == re.findall(r'\[[ xX]\]', after),
            'Completion checkbox state changed')
    return after


def main():
    plan = json.loads(Path('.github/maintenance/reviewed-input.json').read_text())
    repo = os.environ['GITHUB_REPOSITORY']
    require(repo == plan['repository'] and repo in {
        'seokpan/seokpan-hybrid-app', 'seokpan/seokpan-hybrid-gitops',
        'seokpan/seokpan-hybrid-infra', 'seokpan/seokpan-hybrid-docs'}, 'Wrong repository')
    report = Path(os.environ['RUNNER_TEMP']) / 'reviewed-resume-report'
    report.mkdir(exist_ok=True)
    outcomes = []
    def api(endpoint, body=None):
        require(re.fullmatch(r'issues/(?:comments/)?[0-9]+', endpoint), 'Unexpected API target')
        request = urllib.request.Request('https://api.github.com/repos/' + repo + '/' + endpoint,
            data=None if body is None else json.dumps({'body': body}).encode(),
            headers={'Authorization': 'Bearer ' + os.environ['GH_TOKEN'],
                     'Accept': 'application/vnd.github+json', 'Content-Type': 'application/json',
                     'User-Agent': 'seokpan-reviewed-maintenance'},
            method='GET' if body is None else 'PATCH')
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    file_outputs = {}
    for name, item in plan['files'].items():
        path = Path(name)
        require(not path.is_absolute() and '..' not in path.parts and path.suffix == '.md',
                'Only reviewed Markdown paths may change')
        before = path.read_text(encoding='utf-8')
        after = transform(before, item)
        require(after.count('```') % 2 == 0, 'Unbalanced code fences')
        require(after.count('<details>') == after.count('</details>'), 'Unbalanced details')
        file_outputs[path] = after
    metadata_outputs = []
    for item in plan['metadata']:
        row = api(item['endpoint'])
        require(row['user']['login'] == 'tjung03', 'Refuse another author body')
        before = row.get('body') or ''
        if digest(before) == item['after_sha256']:
            outcomes.append({'endpoint': item['endpoint'], 'status': 'ALREADY_MATCHES'})
            continue
        after = transform(before, item)
        for pattern in [r'https?://[^\s)>]+', r'(?<![a-f0-9])[a-f0-9]{40}(?![a-f0-9])']:
            require(re.findall(pattern, before) == re.findall(pattern, after), 'Evidence reference changed')
        metadata_outputs.append((item, before, after))
    for path, output in file_outputs.items():
        path.write_text(output, encoding='utf-8')
        destination = report / 'files' / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(output, encoding='utf-8')
    # Re-read immediately before each body-only write; stop instead of overwriting changed text.
    try:
        for item, before, after in metadata_outputs:
            current = api(item['endpoint'])
            require(current['user']['login'] == 'tjung03' and (current.get('body') or '') == before,
                    'Concurrent metadata change; remaining writes stopped')
            key = item['endpoint'].replace('/', '-')
            (report / (key + '.before.md')).write_text(before, encoding='utf-8')
            api(item['endpoint'], after)
            require((api(item['endpoint']).get('body') or '') == after, 'Metadata readback mismatch')
            (report / (key + '.after.md')).write_text(after, encoding='utf-8')
            outcomes.append({'endpoint': item['endpoint'], 'status': 'UPDATED_READBACK_MATCH',
                             'before_sha256': item['before_sha256'], 'after_sha256': item['after_sha256']})
    finally:
        (report / 'metadata-result.json').write_text(json.dumps(outcomes, indent=2) + '\n')
    (report / 'file-hashes.json').write_text(json.dumps({str(p): digest(t) for p,t in file_outputs.items()}, indent=2) + '\n')
    print(json.dumps({'files': len(file_outputs), 'metadata': len(outcomes),
                      'runtime': 'NOT_PERFORMED', 'checkboxes': 'PRESERVED'}))


if __name__ == '__main__':
    main()
