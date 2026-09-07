#!/usr/bin/env python3
"""Generate the photo-to-art gallery and individual prompts from shared data."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'data/prompts.json').read_text())


def image_link(image, lang, width=320):
    thumbnail = image["src"].replace("https://ailesson.io/", "https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/", 1)
    return f'<a href="{image["src"]}"><img src="{thumbnail}" alt="{html.escape(image["alt"][lang], quote=True)}" width="{width}"></a>'


def photo_credit(r, lang):
    photo = next((c for c in r['citations'] if c['id'] == 'reference-photo'), None)
    license = next((c for c in r['citations'] if c['id'] == 'photo-license'), None)
    if photo:
        return f'[{photo["source"]["publisher"]}]({photo["source"]["url"]}) · [{license["source"]["title"]}]({license["source"]["url"]})'
    return 'AILesson · AI 生成的虚构参考照片' if lang == 'zh' else 'AILesson · AI-generated fictional reference photo'


def example_pair(r, e):
    return next(ref['image'] for ref in r['references'] if ref['id'] == e['comparisonReferenceImageId']), e['output']


def render(lang):
    zh = lang == 'zh'
    base = 'https://ailesson.io' + ('/zh' if zh else '')
    lines = ['<h1 align="center">' + ('Photo Style Prompts · 照片风格转换提示词' if zh else 'Photo Style Prompts') + '</h1>', '',
        '<p align="center">' + ('把照片变成艺术画。对照效果，选择风格，复制提示词。' if zh else 'Turn photos into art. Compare the results, choose a style, copy the prompt.') + '</p>', '',
        f'<p align="center"><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="{base}/prompts/types/image">AILesson</a> · <a href="LICENSE">MIT License</a></p>', '',
        ('使用可复用的 AI 图片编辑提示词，将照片转换为水彩、动画场景、油画、素描、像素画与更多风格。每个示例均展示实际使用的参考图与生成效果，并链接至 [AILesson](https://ailesson.io/zh) 完整配方。' if zh else
         'Reusable AI image-editing prompts for photo-to-art transformations: watercolor, anime scenes, oil paintings, pencil sketches, pixel art, and more. Every example pairs the actual reference image with its generated result and links to the full recipe on [AILesson](https://ailesson.io).'), '',
        '## 快速开始' if zh else '## Quick start', '',
        ('1. 在下方图库中选择一种风格，展开提示词。\n2. 将自己的照片上传到支持参考图的 AI 图片生成或编辑工具。\n3. 填写模板中的变量，说明需要保留的主体、构图与配色。\n4. 运行提示词，再对照原图检查视角、位置关系、轮廓及文字。' if zh else
         '1. Choose a style in the gallery and expand its prompt.\n2. Upload your photo to an AI image-generation or editing tool that accepts reference images.\n3. Fill in the template variables with the subject, composition, and palette you want to preserve.\n4. Run the prompt, then compare the viewpoint, spatial relationships, silhouettes, and any lettering with your original.'), '',
        ('多数模板使用 `{{subject}}` 与 `{{palette}}`。水彩旅行画使用 `{{scene}}`、`{{palette}}` 和 `{{caption}}`；不需要题字时将 `caption` 设为 `NONE`。各风格的独立提示词文件提供变量说明与示例输入。' if zh else
         'Most templates use `{{subject}}` and `{{palette}}`. The watercolor travel print uses `{{scene}}`, `{{palette}}`, and `{{caption}}`; set `caption` to `NONE` for no lettering. Individual prompt files include variable guidance and example inputs.'), '',
        ('示例由英文提示词生成；中文模板尚未单独验证。它们展示真实生成结果，但不保证每次重复运行得到同样的图像。' if zh else
         'Examples were generated with English prompts; Chinese templates have not been independently tested. These are recorded outputs, not guarantees of identical results on a new run.'), '',
        '## 风格图库' if zh else '## Before and after', '',
        ('点击图片查看完整尺寸，点击风格名跳转到提示词。图片保留原始比例；第一张水彩参考图是 AI 生成的虚构场景，其余照片的署名见 [图片来源](IMAGE_CREDITS.md)。' if zh else
         'Open an image at full size or select a style name to jump to its prompt. Images retain their aspect ratios. The watercolor reference is an AI-generated fictional scene; other photo credits are listed in [IMAGE_CREDITS.md](IMAGE_CREDITS.md).'), '',
        '| 风格 | 原图 | 效果图 |' if zh else '| Style | Before | After |', '| :--- | :---: | :---: |']
    for r in DATA:
        for e in r['examples']:
            before, after = example_pair(r, e)
            lines.append(f'| **[{r["name"][lang]}](#{r["id"]})** | {image_link(before,lang)} | {image_link(after,lang)} |')
    lines += ['', '## 提示词' if zh else '## Prompts', '']
    for r in DATA:
        lines += [f'<a id="{r["id"]}"></a>', '', f'### {r["name"][lang]}', '', r['summary'][lang], '',
                  f'[AILesson ↗]({base}/prompts/recipes/{r["alias"]}) · [English prompt](prompts/{r["id"]}.md) · [中文提示词](prompts/zh-CN/{r["id"]}.md)', '',
                  '<details>', '<summary>' + ('展开提示词' if zh else 'Copy prompt') + '</summary>', '', '```text', r['template'][lang], '```', '',
                  r['instructions'][lang], '', '</details>', '']
    lines += ['## 示例与使用说明' if zh else '## About the examples', '',
        ('图片通过 AILesson CDN 加载，仓库不保存图片副本，离线克隆不包含图片。固定内容链接不会自动跟随上游换图；更新数据后需重新生成 README。' if zh else
         'Images load from the AILesson CDN; the repository does not store image copies and offline clones do not include them. Content-addressed URLs do not automatically follow upstream image replacements. Update the data and rebuild the READMEs when an example changes.'), '',
        ('[data/prompts.json](data/prompts.json) 保留实际输入、生成提示词、参考图关联、修订、后处理与已知偏差。生成图片是位图示例；三维、玻璃和版画风格也不提供可编辑模型或生产图纸。' if zh else
         '[data/prompts.json](data/prompts.json) preserves actual inputs, generation prompts, reference associations, revisions, postprocessing, and observed limitations. Outputs are raster examples; 3D, glass, and printmaking styles do not include editable models or fabrication plans.'), '',
        '## 参与贡献' if zh else '## Contributing', '',
        ('欢迎改进提示词、补充风格和修订翻译。请阅读 [贡献指南](CONTRIBUTING.md) 与 [行为准则](CODE_OF_CONDUCT.md)。' if zh else
         'Prompt improvements, new styles, and translation fixes are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) and our [Code of Conduct](CODE_OF_CONDUCT.md).'), '',
        '## 许可与图片署名' if zh else '## License and image credits', '',
        ('提示词、文档和脚本使用 [MIT License](LICENSE)。第三方参考照片保留各自的 Unsplash License 或 CC0 条款，不被重新授权为 MIT。生成示例中的 AILesson 原创贡献按 MIT 提供，以其可授予的权利为限；原照片的适用条款仍需遵守。逐项来源与风格参考见 [IMAGE_CREDITS.md](IMAGE_CREDITS.md)。' if zh else
         'Prompts, documentation, and scripts use the [MIT License](LICENSE). Third-party reference photos retain their Unsplash License or CC0 terms and are not relicensed under MIT. AILesson’s original contributions to generated examples are offered under MIT to the extent it holds applicable rights; applicable source-photo terms still apply. See [IMAGE_CREDITS.md](IMAGE_CREDITS.md) for per-style attribution and references.'), '',
        '---', '', f'[AILesson]({base}) · [Image prompts]({base}/prompts/types/image) · [Icon prompts](https://github.com/ailessonio/icon-prompts)', '']
    return '\n'.join(lines)


def credits():
    lines = ['# Image credits and provenance', '',
        'Reference photographs retain their original terms; serving them through the AILesson CDN does not change their ownership or license. The repository MIT License covers our prompts, documentation, and scripts. AILesson offers its original contributions to generated images under MIT only to the extent it holds applicable rights, without replacing the terms of any underlying photograph. AILesson trademarks and third-party sites are excluded.', '',
        'The generated examples are digital transformations made for these recipes. They are not works by the reference photographers or endorsements by the linked sources. Style references informed the recipes; their images are not copied into this repository.', '']
    for r in DATA:
        lines += [f'## {r["name"]["en"]}', '', photo_credit(r, 'en'), '']
        for e in r['examples']:
            before, after = example_pair(r,e)
            lines += [f'- [Reference image]({before["src"]}) · [Generated result]({after["src"]})',
                      f'- Generated with {e["generation"]["tool"]} on {e["generation"]["date"]}; prompt language: {e["generation"]["promptLanguage"]}.',
                      f'- {e["notes"]["en"]}', '']
        for c in r['citations']:
            s=c['source']
            lines += [f'- [{s["title"]}]({s["url"]}) — {s["publisher"]}. {c["claim"]["en"]}', '']
    return '\n'.join(lines)


def outputs():
    yield ROOT / 'README.md', render('en')
    yield ROOT / 'README.zh-CN.md', render('zh')
    yield ROOT / 'IMAGE_CREDITS.md', credits()
    for r in DATA:
        for lang, directory in [('en','prompts'),('zh','prompts/zh-CN')]:
            zh=lang=='zh'
            lines=[f'# {r["name"][lang]}', '', r['summary'][lang], '',
                   '## 变量' if zh else '## Variables', '']
            for v in r['variables']:
                lines += [f'- `{v["key"]}` — {v["label"][lang]}: {v["placeholder"][lang]}']
            lines += ['', '## 提示词' if zh else '## Prompt', '', '```text', r['template'][lang], '```', '', r['instructions'][lang], '',
                      '## 示例' if zh else '## Example', '']
            for e in r['examples']:
                before,after=example_pair(r,e)
                lines += ['| 原图 | 效果图 |' if zh else '| Before | After |', '| :---: | :---: |', f'| {image_link(before,lang)} | {image_link(after,lang)} |', '', photo_credit(r,lang), '']
                lines += [f'- `{key}`: {value}' for key,value in e['input'][lang].items()]
                lines += ['', e['notes'][lang], '']
            lines += ['## 检查结果' if zh else '## Check the result', '']
            lines += ['- '+c[lang] for c in r['checks']]
            base='https://ailesson.io'+('/zh' if zh else '')
            parent='../..' if zh else '..'
            lines += ['', f'[AILesson]({base}/prompts/recipes/{r["alias"]}) · [Image credits]({parent}/IMAGE_CREDITS.md) · [Gallery]({parent}/README'+('.zh-CN' if zh else '')+'.md)', '']
            yield ROOT / directory / f'{r["id"]}.md', '\n'.join(lines)


if __name__ == '__main__':
    import sys
    for path,content in outputs():
        if '--check' in sys.argv:
            if not path.exists() or path.read_text()!=content:
                raise SystemExit(f'Outdated generated file: {path.relative_to(ROOT)}')
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(content)
    print('Catalog is up to date.' if '--check' in sys.argv else 'Built bilingual gallery, prompts, and credits.')
