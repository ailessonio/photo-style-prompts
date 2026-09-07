# Pixel-art landscape

Rebuild a landscape with crisp pixel clusters, stepped silhouettes and a compact palette inspired by classic games.

## Variables

- `subject` — Essential elements: The red-roof boathouse at the left lakeshore, pine forest, angular mountain peaks, blue lake reflections and low shrubs across the foreground.
- `palette` — Palette and mood: A compact palette of sky blue, deep navy, pine green, warm gold and a small terracotta roof accent; late afternoon.

## Prompt

```text
Transform the attached photo into a pixel-art landscape.

Essential elements: {{subject}}
Palette and mood: {{palette}}

Rebuild as carefully composed 16-bit-era pixel art. Use a visibly coarse, consistent square pixel grid, as if drawn at approximately 320 pixels wide and enlarged with nearest-neighbor scaling. Shape trees, mountains, roofs and water with deliberate clusters, crisp stair-step diagonals and selective ordered dithering. Make the small boathouse readable with a few high-contrast pixels. Keep distant details simpler than foreground clusters. No smooth brushwork, anti-aliased edges, photo mosaic, HUD, game characters or text. This is an aesthetic target, not a claim of an exact indexed palette.

Use the attached photograph as the only visual reference. Preserve its camera viewpoint, major silhouettes, relative positions, and recognizable subject. Simplify fine details without adding objects. Produce only the finished artwork, not a comparison, mockup or framed print. Keep the original landscape aspect ratio, at least 1400 pixels wide. No text, lettering, logos, signature or watermark; omit any signage visible in the photograph.
```

Upload a photo and describe the elements to keep. Sample photo: Rafael Peier, Unsplash License; source and license links are listed below. The example was generated from the English template. The Chinese version is untested. The displayed example does not change as you type.

## Example

| Before | After |
| :---: | :---: |
| <a href="https://ailesson.io/content-assets/sha256/ea/66/ea66fe51fe702cd080905fc1954c0dba73eab85b0489b9b2ac4a5a1ee7c2658c.png"><img src="https://ailesson.io/content-assets/sha256/ea/66/ea66fe51fe702cd080905fc1954c0dba73eab85b0489b9b2ac4a5a1ee7c2658c.png" alt="A red-roof boathouse on the left shore of a blue mountain lake, with pine forest and foreground shrubs." width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/a6/17/a6178f488396fb2297a3b440e581581b3197ac30460f2cce4941e3bb8affd20d.png"><img src="https://ailesson.io/content-assets/sha256/a6/17/a6178f488396fb2297a3b440e581581b3197ac30460f2cce4941e3bb8affd20d.png" alt="A pixel-art mountain lake with a red-roof boathouse on the left, dark pine trees and golden foreground shrubs." width="320"></a> |

[Unsplash / Rafael Peier](https://unsplash.com/photos/mountain-lake-with-a-boathouse-and-surrounding-forest-I_XRy-z8m8k) · [Unsplash License](https://unsplash.com/license)

- `subject`: The red-roof boathouse at the left lakeshore, pine forest, angular mountain peaks, blue lake reflections and low shrubs across the foreground.
- `palette`: A compact palette of sky blue, deep navy, pine green, warm gold and a small terracotta roof accent; late afternoon.

The red roof, lake and mountain arrangement remain recognizable. The output has coarse pixel clusters and strong sky dithering, but the house is enlarged and the image is not a certified uniform-grid game asset.

## Check the result

- Compare the main silhouette, viewpoint and left/right relationships with the uploaded photo.
- Inspect the roof, mountain diagonals and water: pixel clusters should be readable and edges should stay crisp.
- Inspect small features at full size and remove accidental lettering before sharing.

[AILesson](https://ailesson.io/prompts/recipes/turn-photos-into-pixel-art-scenes) · [Image credits](../IMAGE_CREDITS.md) · [Gallery](../README.md)
