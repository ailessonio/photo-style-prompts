#!/usr/bin/env python3
"""Check catalog integrity, generated files, and optionally live AILesson URLs."""
import concurrent.futures
import re
import sys
import urllib.request
import urllib.error
from build import DATA, ROOT, outputs

ids = [r['id'] for r in DATA]
assert len(ids) == len(set(ids)), 'Duplicate style IDs'
urls = set()
for r in DATA:
    assert r['examples'], 'Missing example'
    keys = {v['key'] for v in r['variables']}
    ref_ids = {ref['id'] for ref in r['references']}
    for lang in ('en', 'zh'):
        assert set(re.findall(r'\{\{(\w+)\}\}', r['template'][lang])) == keys
        assert r['name'][lang] and r['summary'][lang] and r['instructions'][lang]
        urls.add(f'https://ailesson.io{"/zh" if lang == "zh" else ""}/prompts/recipes/{r["alias"]}')
    for e in r['examples']:
        assert set(e['generation']['referenceImageIds']) <= ref_ids
        for lang in ('en', 'zh'):
            assert set(e['input'][lang]) == keys
            assert e['output']['alt'][lang]
        assert e['comparisonReferenceImageId'] in ref_ids
        assert e['comparisonReferenceImageId'] in e['generation']['referenceImageIds']
        assert e['output']['width'] > 0 and e['output']['height'] > 0
    def images(value):
        if isinstance(value, dict):
            for key, item in value.items():
                if key == 'src':
                    assert re.fullmatch(r'https://ailesson.io/content-assets/sha256/[a-f0-9]{2}/[a-f0-9]{2}/[a-f0-9]{64}\.png', item), item
                    urls.add(item)
                else:
                    images(item)
        elif isinstance(value, list):
            for item in value:
                images(item)
    images(r)
for path, expected in outputs():
    assert path.read_text() == expected, f'Rebuild {path}'
    urls.update(re.findall(r'<img src="([^"]+)"', expected))
    for target in re.findall(r'\]\(([^)]+)\)', expected):
        if not target.startswith(('https:', '#')):
            assert (path.parent / target.split('#')[0]).exists(), (path, target)
for lang in ('', '/zh'):
    urls.update(f'https://ailesson.io{lang}{suffix}' for suffix in ('', '/prompts', '/prompts/types/image'))
if '--online' in sys.argv:
    def check(url):
        request = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'AILesson-Photo-Style-Prompts-Link-Check/1.0'})
        for attempt in range(3):
            try:
                with urllib.request.urlopen(request, timeout=25) as response:
                    assert response.status == 200, (url, response.status)
                    if url.endswith('.png'):
                        assert response.headers.get_content_type().startswith('image/'), url
                return None
            except (urllib.error.URLError, TimeoutError) as error:
                if attempt == 2:
                    return f'{url}: {error}'
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        failures = [result for result in pool.map(check, sorted(urls)) if result]
    if failures:
        raise SystemExit('Link checks failed:\n' + '\n'.join(failures))
    print(f'Checked {len(urls)} live page and image URLs.')
print(f'Validated {len(DATA)} styles, {sum(len(r["examples"]) for r in DATA)} gallery images, bilingual prompts, references, and generated links.')
