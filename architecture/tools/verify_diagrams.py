#!/usr/bin/env python3
"""Verify design assets and atomically refresh provenance without losing history.

Default mode requires the build's layout-audit.json. --integrity-only checks
unchanged published assets against the existing manifest and explicitly skips
layout geometry. Neither mode certifies Runtime acceptance or visual semantics.
"""
import argparse
import base64
from copy import deepcopy
import hashlib
import io
import json
import os
from pathlib import Path
import re
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
NS = {'s': 'http://www.w3.org/2000/svg'}
DECISION_KEYS = ('followup_review', 'data_engine_followup', 'consistency_revision')
SECRET_PATTERNS = (
    r'AKIA[A-Z0-9]{16}', r'ASIA[A-Z0-9]{16}', r'gh[pousr]_[A-Za-z0-9]{20,}',
    r'github_pat_[A-Za-z0-9_]{30,}',
    r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def identify(path):
    raw = path.read_bytes()
    return {'path': path.relative_to(REPO).as_posix(), 'bytes': len(raw),
            'sha256': hashlib.sha256(raw).hexdigest()}


def merge_history(*histories):
    result = []
    for history in histories:
        for item in history:
            if item not in result:
                result.append(deepcopy(item))
    return result


def compose_manifest(baseline, previous, assets, checks, mode):
    """Own computed fields; copy current decisions; retain extension/history fields."""
    result = deepcopy(previous)
    result.update({
        'schema_version': 1,
        'created_date': previous.get('created_date', baseline['recorded_date']),
        'design_basis_date': baseline['source_basis_date'],
        'status': 'DESIGN_TARGET',
        'runtime_validation': previous.get('runtime_validation', 'NOT_ASSESSED'),
        'source_files': [{'path': f['path'], 'sha256': f['sha256']}
                         for f in baseline['files']],
        'checks': deepcopy(checks), 'diagrams': deepcopy(assets),
    })
    if 'review' in baseline:
        result['source_review'] = deepcopy(baseline['review'])
    for key in DECISION_KEYS:
        if key in baseline:
            result[key] = deepcopy(baseline[key])
    result['followup_review_history'] = merge_history(
        previous.get('followup_review_history', []),
        baseline.get('followup_review_history', []),
    )
    scope = {
        'date': baseline['recorded_date'],
        'reference': 'architecture/tools/verify_diagrams.py',
        'mode': mode,
        'asset_checks': deepcopy(checks),
        'source_identity': 'SOURCE_IDENTITY_5_PASS',
        'declared_geometry': 'SKIPPED_NO_BUILD_LAYOUT' if mode == 'integrity_only'
                             else 'CHECKED_AGAINST_BUILD_LAYOUT',
        'visual_review': 'NOT_ASSESSED_BY_THIS_SCRIPT',
        'runtime_validation': 'NOT_ASSESSED_BY_THIS_SCRIPT',
        'note': 'Asset/source provenance verification only; no deployment, '
                'compatibility, cost or recovery target-attainment test.',
    }
    history = previous.get('check_scope_history', [])
    prior_scope = previous.get('latest_check_scope')
    if prior_scope and prior_scope != scope:
        history = merge_history(history, [prior_scope])
    result['check_scope_history'] = deepcopy(history)
    result['latest_check_scope'] = scope
    return result


def atomic_write(path, data):
    """Do not leave a partially written manifest after an interrupted update."""
    descriptor, temporary = tempfile.mkstemp(prefix=path.name + '.', dir=path.parent)
    try:
        with os.fdopen(descriptor, 'w', encoding='utf-8') as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def verify(integrity_only=False):
    from PIL import Image
    from fontTools.ttLib import TTFont

    manifest_path = ROOT / 'diagram-manifest.json'
    baseline = json.loads((REPO / 'design/source-manifest.json').read_text(encoding='utf-8'))
    previous = json.loads(manifest_path.read_text(encoding='utf-8')) if manifest_path.exists() else {}
    require(len(baseline['files']) == 5, 'Expected the five design source identities')
    for source in baseline['files']:
        actual = identify(REPO / source['path'])
        require(actual['bytes'] == source['bytes'] and actual['sha256'] == source['sha256'],
                f'Source identity mismatch: {source["path"]}')

    if integrity_only:
        require(previous.get('diagrams'), '--integrity-only requires an existing manifest')
        specs = previous['diagrams']
    else:
        layout = ROOT / 'tools/layout-audit.json'
        require(layout.exists(), 'Missing build layout-audit.json; build all layouts first '
                'or explicitly use --integrity-only for unchanged assets')
        specs = json.loads(layout.read_text(encoding='utf-8'))
    require([s['id'] for s in specs] == [f'{i:02d}' for i in range(1, 13)],
            'Expected exactly twelve ordered diagram specifications')

    assets = []
    old_assets = {d['id']: d for d in previous.get('diagrams', [])}
    for spec in specs:
        if integrity_only:
            svg = REPO / spec['svg']['path']
            png = REPO / spec['png']['path']
            height = spec['svg_size'][1]
            require(identify(svg) == spec['svg'], f'Existing SVG identity mismatch: {svg}')
            require(identify(png) == spec['png'], f'Existing PNG identity mismatch: {png}')
        else:
            svg = ROOT / 'diagrams' / f'{spec["slug"]}.svg'
            png = ROOT / 'exports' / f'{spec["slug"]}.png'
            height = spec['height']
        raw = svg.read_text(encoding='utf-8')
        xml = ET.fromstring(raw)
        require(xml.get('viewBox') == f'0 0 1800 {height}', f'Invalid viewBox: {svg}')
        require(xml.find('s:title', NS) is not None and xml.find('s:desc', NS) is not None,
                f'Missing accessible title/description: {svg}')
        texts = [''.join(t.itertext()) for t in xml.findall('s:text', NS)]
        require('설계 목표 · 구현/시험 미확인' in texts, f'Missing design boundary: {svg}')
        require(any(t.startswith('근거: ') for t in texts), f'Missing source caption: {svg}')
        require(any(t.startswith('확인 대기: ') for t in texts), f'Missing pending caption: {svg}')
        require(not xml.findall('s:script', NS) and not xml.findall('s:foreignObject', NS),
                f'Active SVG content: {svg}')
        require(not re.search(r'(?:href|src)=[\"\']https?://', raw), f'External SVG asset: {svg}')
        match = re.search(r'data:font/woff;base64,([A-Za-z0-9+/=]+)', raw)
        require(match is not None, f'Missing embedded font: {svg}')
        with TTFont(io.BytesIO(base64.b64decode(match.group(1), validate=True))) as font:
            cmap = font.getBestCmap()
            missing = {c for t in texts for c in t if ord(c) not in cmap and not c.isspace()}
        require(not missing, f'Missing font glyphs: {svg}: {missing}')
        if not integrity_only:
            require(texts == [t['text'] for t in spec['texts']], f'Build text mismatch: {svg}')
            for text in spec['texts']:
                require(0 <= text['x'] and text['x'] + text['w'] <= 1800
                        and text['size'] <= text['y'] <= height,
                        f'Text outside declared geometry: {svg}: {text}')
        with Image.open(png) as image:
            image.load()
            require(image.size == (3600, height * 2), f'Invalid PNG dimensions: {png}')
        for pattern in SECRET_PATTERNS:
            require(not any(re.search(pattern, text) for text in texts),
                    f'High-risk text pattern: {svg}')
        asset = deepcopy(old_assets.get(spec['id'], {}))
        asset.update({'id': spec['id'], 'title': spec['title'], 'status': 'DESIGN_TARGET',
                      'source_refs': spec['source_refs'], 'pending': spec['pending'],
                      'svg': identify(svg), 'png': identify(png),
                      'svg_size': [1800, height], 'png_size': [3600, height * 2],
                      'embedded_font_glyphs_checked': True})
        assets.append(asset)
    physical = (ROOT / 'diagrams/02-physical-architecture.svg').read_text(encoding='utf-8')
    for number in range(64, 73):
        require(f'192.168.{number}.0/24' in physical, f'Missing subnet .{number}')
    require(len(list((ROOT / 'diagrams').glob('*.svg'))) == 12, 'Unexpected SVG count')
    require(len(list((ROOT / 'exports').glob('*.png'))) == 12, 'Unexpected PNG count')
    checks = {'svg_xml': 12, 'png_decode': 12, 'embedded_font_glyphs': 12,
              'declared_geometry': 0 if integrity_only else 12,
              'approved_subnet_cidrs': 9, 'source_identity': 5,
              'high_risk_text_pattern_matches': 0}
    result = compose_manifest(baseline, previous, assets, checks,
                              'integrity_only' if integrity_only else 'build_layout')
    atomic_write(manifest_path, json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--integrity-only', action='store_true',
                        help='Verify unchanged published bytes; skip missing build geometry')
    args = parser.parse_args()
    print(json.dumps(verify(args.integrity_only), ensure_ascii=False))


if __name__ == '__main__':
    main()
