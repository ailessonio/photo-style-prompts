# Contributing

Use English for repository maintenance, issues, and pull requests. Reader-facing translations live in `README.zh-CN.md` and `prompts/zh-CN/`.

## Propose or improve a style

Open an issue for a new style or substantial change; small fixes can go straight to a pull request. Explain how the style differs from existing recipes.

1. Edit `data/prompts.json`, the shared source for the generated Markdown.
2. Keep English and Chinese variables, evidence boundaries, and intended outcomes aligned.
3. Include an actual before/after example, accurate alt text and dimensions, the exact generation prompt, tool/date, inputs, reference IDs, and any revisions or postprocessing. Set `comparisonReferenceImageId` to the reference actually used; the generated source image is not the original photo.
4. Record the original photographer, source page, and license. Only submit material you have permission to contribute. Third-party photographs retain their terms and must not be labeled MIT.
5. Use public AILesson CDN image URLs. Maintainers publish new assets through AILesson before merging; do not commit binary images, private URLs, credentials, or temporary files.
6. Run `python3 scripts/build.py`, `python3 scripts/validate.py`, and `python3 scripts/validate.py --online`. Preview both READMEs and check image proportions and prompt expansion.
7. Explain the change and its validation in the pull request. Clearly distinguish tested results from untested templates.

Python 3.11+ is sufficient. No external packages, API keys, or generation service are needed for maintenance. Do not edit generated Markdown directly.

## Source and updates

The initial collection was adapted from AILesson's photo transformation recipes. Public improvements are reviewed here; maintainers separately reconcile accepted changes with the AILesson content source. There is no automatic upstream sync or production publishing.

On refresh, preserve current example associations, original generation evidence, and credits. Verify content-addressed CDN URLs before regenerating. A replacement image needs a new URL; the old URL continues to identify its original image.

Prompts, documentation, and scripts are contributed under MIT. Image rights and source-photo terms are documented separately in `IMAGE_CREDITS.md`.
