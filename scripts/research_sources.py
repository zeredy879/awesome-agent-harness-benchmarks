#!/usr/bin/env python3
"""Read public GitHub metadata/READMEs; never execute downloaded code.

Local raw documents are ignored by git. Published audit records contain only
URLs, hashes and availability metadata, not third-party document text.
"""
import argparse
import base64
import concurrent.futures
import hashlib
import json
import pathlib
import subprocess
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
CACHE = ROOT / '.cache' / 'sources'


def api(path):
    p = subprocess.run(['gh', 'api', path], capture_output=True, text=True, timeout=35)
    if p.returncode:
        raise RuntimeError(p.stderr.strip()[:300])
    return json.loads(p.stdout)


def fetch(repo):
    key = repo.replace('/', '__')
    cached = CACHE / (key + '.json')
    if cached.exists():
        return json.loads(cached.read_text())
    result = {'requested_repo': repo, 'checked_at': datetime.now(timezone.utc).isoformat()}
    try:
        meta = api('repos/' + repo)
        result.update(repo=meta['full_name'], url=meta['html_url'], archived=meta['archived'],
                      fork=meta['fork'], stars=meta['stargazers_count'],
                      default_branch=meta['default_branch'], description=meta['description'],
                      pushed_at=meta['pushed_at'], license=(meta.get('license') or {}).get('spdx_id'))
        readme = api('repos/' + meta['full_name'] + '/readme')
        raw = base64.b64decode(readme['content'])
        (CACHE / (key + '.md')).write_bytes(raw)
        result.update(status='source-accessible', readme_url=readme['html_url'],
                      readme_blob_sha=readme['sha'], readme_sha256=hashlib.sha256(raw).hexdigest())
    except Exception as exc:
        result.update(status='needs-review', error=str(exc))
    cached.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument('repos', nargs='*')
    p.add_argument('--catalog', action='store_true')
    p.add_argument('--audit', action='store_true')
    args = p.parse_args()
    CACHE.mkdir(parents=True, exist_ok=True)
    repos = args.repos
    if args.catalog:
        entries = json.loads((ROOT / 'data/catalog.json').read_text())['entries']
        repos = sorted({x['url'].removeprefix('https://github.com/').strip('/') for x in entries
                        if x['url'].startswith('https://github.com/')})
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
        records = sorted(ex.map(fetch, repos), key=lambda x: x['requested_repo'].lower())
    if args.audit:
        dest = ROOT / 'data/source-audit.json'
        dest.write_text(json.dumps({'description': 'Availability and provenance only; not independent benchmark reproduction.',
                                    'repositories': records}, ensure_ascii=False, indent=2) + '\n')
    for r in records:
        print(json.dumps(r, ensure_ascii=False))


if __name__ == '__main__':
    main()
