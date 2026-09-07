<h1 align="center">Photo Style Prompts</h1>

<p align="center">Turn photos into art. Compare the results, choose a style, copy the prompt.</p>

<p align="center"><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="https://ailesson.io/prompts/types/image">AILesson</a> · <a href="LICENSE">MIT License</a></p>

Reusable AI image-editing prompts for photo-to-art transformations: watercolor, anime scenes, oil paintings, pencil sketches, pixel art, and more. Every example pairs the actual reference image with its generated result and links to the full recipe on [AILesson](https://ailesson.io).

## Quick start

1. Choose a style in the gallery and expand its prompt.
2. Upload your photo to an AI image-generation or editing tool that accepts reference images.
3. Fill in the template variables with the subject, composition, and palette you want to preserve.
4. Run the prompt, then compare the viewpoint, spatial relationships, silhouettes, and any lettering with your original.

Most templates use `{{subject}}` and `{{palette}}`. The watercolor travel print uses `{{scene}}`, `{{palette}}`, and `{{caption}}`; set `caption` to `NONE` for no lettering. Individual prompt files include variable guidance and example inputs.

Examples were generated with English prompts; Chinese templates have not been independently tested. These are recorded outputs, not guarantees of identical results on a new run.

## Before and after

Open an image at full size or select a style name to jump to its prompt. Images retain their aspect ratios. The watercolor reference is an AI-generated fictional scene; other photo credits are listed in [IMAGE_CREDITS.md](IMAGE_CREDITS.md).

| Style | Before | After |
| :--- | :---: | :---: |
| **[Watercolor Travel Print](#watercolor-travel-prints)** | <a href="https://ailesson.io/content-assets/sha256/f3/56/f35677c8ff98057e3afbcafd4339e1e882dd4cc29bf068fa079a2f8c58bbbe4b.png"><img src="https://ailesson.io/content-assets/sha256/f3/56/f35677c8ff98057e3afbcafd4339e1e882dd4cc29bf068fa079a2f8c58bbbe4b.png" alt="AI-generated fictional photograph of a lakeside boathouse, jetty and snow-capped mountain at blue hour." width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/01/5d/015dc54d62ec2fe26f45b9dc60ceeed65fbd130c0099c57542d6c38750ff8586.png"><img src="https://ailesson.io/content-assets/sha256/01/5d/015dc54d62ec2fe26f45b9dc60ceeed65fbd130c0099c57542d6c38750ff8586.png" alt="A small blue-gray watercolor lake scene with a mountain on the left and a warmly lit boathouse on the right, surrounded by wide ivory paper margins." width="320"></a> |
| **[Hand-painted anime scene](#hand-painted-anime-scenes)** | <a href="https://ailesson.io/content-assets/sha256/60/b6/60b6c57cd35766a133979b111ca77b6af62573386e88ae4b6c0e834613a1aad4.png"><img src="https://ailesson.io/content-assets/sha256/60/b6/60b6c57cd35766a133979b111ca77b6af62573386e88ae4b6c0e834613a1aad4.png" alt="A coastal bay viewed across a golden field, with wooded slopes, a small beach and hillside houses." width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/97/76/9776ea79c20a4905efae2d1428dbf0c3cf90ab94da365b5bdc8c6b295e101249.png"><img src="https://ailesson.io/content-assets/sha256/97/76/9776ea79c20a4905efae2d1428dbf0c3cf90ab94da365b5bdc8c6b295e101249.png" alt="A hand-painted coastal panorama with golden meadows, green slopes, a blue bay and small hillside houses beneath painted clouds." width="320"></a> |
| **[Impressionist oil painting](#impressionist-oil-paintings)** | <a href="https://ailesson.io/content-assets/sha256/40/30/4030559193d5c3911193c6375bda8d56b31796aaaedbd1e8c8ded0bd2b567abc.png"><img src="https://ailesson.io/content-assets/sha256/40/30/4030559193d5c3911193c6375bda8d56b31796aaaedbd1e8c8ded0bd2b567abc.png" alt="Pink tulips in a clear glass vase with a raffia bow beside a wicker basket in front of windows." width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/90/9b/909be6a851abed4a5a858956c1e2abeca519a8de1d46624ba50dd9d6d3c5da85.png"><img src="https://ailesson.io/content-assets/sha256/90/9b/909be6a851abed4a5a858956c1e2abeca519a8de1d46624ba50dd9d6d3c5da85.png" alt="An oil-painted still life of pink tulips in a glass vase beside a wicker basket, with textured strokes and warm window light." width="320"></a> |
| **[Graphite pencil sketch](#graphite-sketches)** | <a href="https://ailesson.io/content-assets/sha256/f7/74/f77456efd607639a92825d09289328963f260acd3c436972bab509d8405fc57e.png"><img src="https://ailesson.io/content-assets/sha256/f7/74/f77456efd607639a92825d09289328963f260acd3c436972bab509d8405fc57e.png" alt="A fluffy pale cat asleep on a white windowsill, with a limb and tail hanging down and a ladder on the right." width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/0a/bb/0abbc60926261aa9b2d2e98809444b5acd66899abaec117e66f5319d1bd955ab.png"><img src="https://ailesson.io/content-assets/sha256/0a/bb/0abbc60926261aa9b2d2e98809444b5acd66899abaec117e66f5319d1bd955ab.png" alt="A graphite sketch of a sleeping fluffy cat on a windowsill, with one limb hanging down and a lightly drawn ladder at right." width="320"></a> |
| **[Pop-art comic print](#pop-art-prints)** | <a href="https://ailesson.io/content-assets/sha256/f7/74/f77456efd607639a92825d09289328963f260acd3c436972bab509d8405fc57e.png"><img src="https://ailesson.io/content-assets/sha256/f7/74/f77456efd607639a92825d09289328963f260acd3c436972bab509d8405fc57e.png" alt="A fluffy pale cat asleep on a white windowsill, with a limb and tail hanging down and a ladder on the right." width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/24/40/2440784288af45ca4fc718cb5f8112de718b4a08d0e45ae48c8beaebdee377e8.png"><img src="https://ailesson.io/content-assets/sha256/24/40/2440784288af45ca4fc718cb5f8112de718b4a08d0e45ae48c8beaebdee377e8.png" alt="A cream sleeping cat rendered with dark comic contours, coral and cyan room shapes and selective halftone dots." width="320"></a> |
| **[Retro travel poster](#retro-travel-posters)** | <a href="https://ailesson.io/content-assets/sha256/60/b6/60b6c57cd35766a133979b111ca77b6af62573386e88ae4b6c0e834613a1aad4.png"><img src="https://ailesson.io/content-assets/sha256/60/b6/60b6c57cd35766a133979b111ca77b6af62573386e88ae4b6c0e834613a1aad4.png" alt="A coastal bay viewed across a golden field, with wooded slopes, a small beach and hillside houses." width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/d3/34/d334c19f4d428ae0978f2445d9a54861c645602349edaff7f2d605ab6ce48664.png"><img src="https://ailesson.io/content-assets/sha256/d3/34/d334c19f4d428ae0978f2445d9a54861c645602349edaff7f2d605ab6ce48664.png" alt="A flat-color retro illustration of a coastal village and curved bay, framed by ochre fields and deep green slopes." width="320"></a> |
| **[Pixel-art landscape](#pixel-art-scenes)** | <a href="https://ailesson.io/content-assets/sha256/ea/66/ea66fe51fe702cd080905fc1954c0dba73eab85b0489b9b2ac4a5a1ee7c2658c.png"><img src="https://ailesson.io/content-assets/sha256/ea/66/ea66fe51fe702cd080905fc1954c0dba73eab85b0489b9b2ac4a5a1ee7c2658c.png" alt="A red-roof boathouse on the left shore of a blue mountain lake, with pine forest and foreground shrubs." width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/a6/17/a6178f488396fb2297a3b440e581581b3197ac30460f2cce4941e3bb8affd20d.png"><img src="https://ailesson.io/content-assets/sha256/a6/17/a6178f488396fb2297a3b440e581581b3197ac30460f2cce4941e3bb8affd20d.png" alt="A pixel-art mountain lake with a red-roof boathouse on the left, dark pine trees and golden foreground shrubs." width="320"></a> |
| **[Layered paper scene](#layered-paper-scenes)** | <a href="https://ailesson.io/content-assets/sha256/60/b6/60b6c57cd35766a133979b111ca77b6af62573386e88ae4b6c0e834613a1aad4.png"><img src="https://ailesson.io/content-assets/sha256/60/b6/60b6c57cd35766a133979b111ca77b6af62573386e88ae4b6c0e834613a1aad4.png" alt="A coastal bay viewed across a golden field, with wooded slopes, a small beach and hillside houses." width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/bc/1e/bc1e864434ee614dfda46fffac8443c6cde578965c41d7d65434561e4a495964.png"><img src="https://ailesson.io/content-assets/sha256/bc/1e/bc1e864434ee614dfda46fffac8443c6cde578965c41d7d65434561e4a495964.png" alt="A layered paper coastal panorama with ochre fields, green tree cutouts, turquoise water and small cream houses." width="320"></a> |
| **[Two-color linocut](#two-color-linocuts)** | <a href="https://ailesson.io/content-assets/sha256/f7/74/f77456efd607639a92825d09289328963f260acd3c436972bab509d8405fc57e.png"><img src="https://ailesson.io/content-assets/sha256/f7/74/f77456efd607639a92825d09289328963f260acd3c436972bab509d8405fc57e.png" alt="A fluffy pale cat asleep on a white windowsill, with a limb and tail hanging down and a ladder on the right." width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/ef/e4/efe415278a1bf9b4eb9d23f60b8afbd2f6e4f4c921f8da5bf23f1ab0de4bf26d.png"><img src="https://ailesson.io/content-assets/sha256/ef/e4/efe415278a1bf9b4eb9d23f60b8afbd2f6e4f4c921f8da5bf23f1ab0de4bf26d.png" alt="An indigo and terracotta linocut-style print of a sleeping cream cat beside a window and ladder." width="320"></a> |
| **[Cyanotype print](#cyanotype-prints)** | <a href="https://ailesson.io/content-assets/sha256/40/30/4030559193d5c3911193c6375bda8d56b31796aaaedbd1e8c8ded0bd2b567abc.png"><img src="https://ailesson.io/content-assets/sha256/40/30/4030559193d5c3911193c6375bda8d56b31796aaaedbd1e8c8ded0bd2b567abc.png" alt="Pink tulips in a clear glass vase with a raffia bow beside a wicker basket in front of windows." width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/c0/27/c027013d73e6427621a58ecf113675664dfb43aa2f20d8ba7bf146b65a34aa87.png"><img src="https://ailesson.io/content-assets/sha256/c0/27/c027013d73e6427621a58ecf113675664dfb43aa2f20d8ba7bf146b65a34aa87.png" alt="A blue-and-white cyanotype-style still life with tulips, a glass vase and a wicker basket." width="320"></a> |
| **[Stained-glass panel](#stained-glass-panels)** | <a href="https://ailesson.io/content-assets/sha256/40/30/4030559193d5c3911193c6375bda8d56b31796aaaedbd1e8c8ded0bd2b567abc.png"><img src="https://ailesson.io/content-assets/sha256/40/30/4030559193d5c3911193c6375bda8d56b31796aaaedbd1e8c8ded0bd2b567abc.png" alt="Pink tulips in a clear glass vase with a raffia bow beside a wicker basket in front of windows." width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/93/8b/938b7791b1ae0c7ac8fc55b3c387c988fabf0a8bfdf23f476fd158a1ae1c9321.png"><img src="https://ailesson.io/content-assets/sha256/93/8b/938b7791b1ae0c7ac8fc55b3c387c988fabf0a8bfdf23f476fd158a1ae1c9321.png" alt="Pink tulips and a wicker basket reinterpreted as luminous stained glass with green leaves and amber glass sections." width="320"></a> |
| **[Neon contour artwork](#neon-contour-art)** | <a href="https://ailesson.io/content-assets/sha256/f7/74/f77456efd607639a92825d09289328963f260acd3c436972bab509d8405fc57e.png"><img src="https://ailesson.io/content-assets/sha256/f7/74/f77456efd607639a92825d09289328963f260acd3c436972bab509d8405fc57e.png" alt="A fluffy pale cat asleep on a white windowsill, with a limb and tail hanging down and a ladder on the right." width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/ad/4f/ad4f4c064e4180d2cab6164a477b4874257efb6fa0fbdb511b06a31a3fcaae33.png"><img src="https://ailesson.io/content-assets/sha256/ad/4f/ad4f4c064e4180d2cab6164a477b4874257efb6fa0fbdb511b06a31a3fcaae33.png" alt="A sleeping cat outlined in cyan light beside dim window and ladder contours on a dark navy background." width="320"></a> |
| **[Digital wireframe landscape](#digital-wireframe-landscapes)** | <a href="https://ailesson.io/content-assets/sha256/60/b6/60b6c57cd35766a133979b111ca77b6af62573386e88ae4b6c0e834613a1aad4.png"><img src="https://ailesson.io/content-assets/sha256/60/b6/60b6c57cd35766a133979b111ca77b6af62573386e88ae4b6c0e834613a1aad4.png" alt="A coastal bay viewed across a golden field, with wooded slopes, a small beach and hillside houses." width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/78/6a/786a4f97a52e44c500a5a5ccabb7ccf71e1c179cb62485fdbee47e48eb4a05a9.png"><img src="https://ailesson.io/content-assets/sha256/78/6a/786a4f97a52e44c500a5a5ccabb7ccf71e1c179cb62485fdbee47e48eb4a05a9.png" alt="A midnight-blue coastal landscape drawn as cyan triangular wireframe terrain with a small lime shoreline." width="320"></a> |
| **[Iridescent metal render](#iridescent-metal-renders)** | <a href="https://ailesson.io/content-assets/sha256/40/30/4030559193d5c3911193c6375bda8d56b31796aaaedbd1e8c8ded0bd2b567abc.png"><img src="https://ailesson.io/content-assets/sha256/40/30/4030559193d5c3911193c6375bda8d56b31796aaaedbd1e8c8ded0bd2b567abc.png" alt="Pink tulips in a clear glass vase with a raffia bow beside a wicker basket in front of windows." width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/3b/e5/3be5ddd6e64ed7809f417bd3217d8ccdeb28b9f65f734e39ea0d335759b49f5f.png"><img src="https://ailesson.io/content-assets/sha256/3b/e5/3be5ddd6e64ed7809f417bd3217d8ccdeb28b9f65f734e39ea0d335759b49f5f.png" alt="Pearlescent silver tulips with pink-blue reflections in a clear vase beside a pale woven basket." width="320"></a> |
| **[3D miniature world](#3d-miniature-worlds)** | <a href="https://ailesson.io/content-assets/sha256/ea/66/ea66fe51fe702cd080905fc1954c0dba73eab85b0489b9b2ac4a5a1ee7c2658c.png"><img src="https://ailesson.io/content-assets/sha256/ea/66/ea66fe51fe702cd080905fc1954c0dba73eab85b0489b9b2ac4a5a1ee7c2658c.png" alt="A red-roof boathouse on the left shore of a blue mountain lake, with pine forest and foreground shrubs." width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/8e/ad/8eaddfc7837080402cb0f8111802e4cb64cc4285a1310770110b939ae09a6242.png"><img src="https://ailesson.io/content-assets/sha256/8e/ad/8eaddfc7837080402cb0f8111802e4cb64cc4285a1310770110b939ae09a6242.png" alt="A compact 3D-style mountain lake model with turquoise water, ivory mountains, green trees and a terracotta-roof boathouse." width="320"></a> |

## Prompts

<a id="watercolor-travel-prints"></a>

### Watercolor Travel Print

Repaint a familiar scene as a small watercolor vignette on ivory paper while keeping its key landmarks and viewpoint.

[AILesson ↗](https://ailesson.io/prompts/recipes/turn-photos-into-watercolor-travel-prints) · [English prompt](prompts/watercolor-travel-prints.md) · [中文提示词](prompts/zh-CN/watercolor-travel-prints.md)

<details>
<summary>Copy prompt</summary>

```text
Transform the attached scene photograph into a quiet watercolor travel print.

Scene and essential landmarks: {{scene}}
Palette and mood: {{palette}}
Caption: {{caption}}

Use the uploaded photograph as the composition reference. Keep the original viewpoint, recognizable silhouettes, relative positions and depth relationships of the listed landmarks inside the painted scene. Simplify small details without inventing new objects. Repaint the scene with transparent watercolor washes, gentle pigment blooms, broken dry-brush accents and soft irregular edges on warm ivory paper with subtle visible grain. Let sky and water dissolve naturally into unpainted paper. Use restrained color and a small warm light accent; no heavy outlines, photographic textures or glossy 3D rendering.

Make a square art print at least 1024 by 1024 pixels. Center a small unified scene occupying about 50–55% of the canvas width, leaving generous unpainted paper on every side. Do not fill the page with the original photograph or create a before-and-after collage. If Caption is NONE, add no text. Otherwise place only the supplied caption below the painting in small understated handwritten lettering; do not invent dates or extra lines. No frame, watermark or additional people, vehicles or buildings.
```

Upload a scene photo and fill in the variables. The included reference is an AI-generated fictional photo, not a real location or the original author’s image. The example uses the English template with that reference. Chinese and caption variants are untested. Fixed examples do not change as you type.

</details>

<a id="hand-painted-anime-scenes"></a>

### Hand-painted anime scene

Keep a coastal view recognizable while repainting it with luminous gouache-like shapes and layered depth.

[AILesson ↗](https://ailesson.io/prompts/recipes/turn-photos-into-hand-painted-anime-scenes) · [English prompt](prompts/hand-painted-anime-scenes.md) · [中文提示词](prompts/zh-CN/hand-painted-anime-scenes.md)

<details>
<summary>Copy prompt</summary>

```text
Transform the attached photo into a hand-painted anime scene.

Essential elements: {{subject}}
Palette and mood: {{palette}}

Repaint as a hand-painted background for a 2D animated film. Use opaque gouache-like color masses, delicately drawn architectural contours, soft layered atmospheric depth and selective crisp highlights. Simplify the foreground grass into rhythmic brush shapes. Separate near, middle and far planes with value and temperature. Keep the village small within the landscape. Avoid photorealism, plastic 3D shading, heavy comic outlines and recognizable franchise motifs.

Use the attached photograph as the only visual reference. Preserve its camera viewpoint, major silhouettes, relative positions, and recognizable subject. Simplify fine details without adding objects. Produce only the finished artwork, not a comparison, mockup or framed print. Keep the original landscape aspect ratio, at least 1400 pixels wide. No text, lettering, logos, signature or watermark; omit any signage visible in the photograph.
```

Upload a photo and describe the elements to keep. Sample photo: Leticia Golubov, Unsplash License; source and license links are listed below. The example was generated from the English template. The Chinese version is untested. The displayed example does not change as you type.

</details>

<a id="impressionist-oil-paintings"></a>

### Impressionist oil painting

Turn a flower or tabletop photo into a tactile oil painting with broken color, visible strokes and soft background edges.

[AILesson ↗](https://ailesson.io/prompts/recipes/turn-photos-into-impressionist-oil-paintings) · [English prompt](prompts/impressionist-oil-paintings.md) · [中文提示词](prompts/zh-CN/impressionist-oil-paintings.md)

<details>
<summary>Copy prompt</summary>

```text
Transform the attached photo into a impressionist oil painting.

Essential elements: {{subject}}
Palette and mood: {{palette}}

Repaint as an impressionist still-life oil painting. Build petals, glass and wicker from visible short broken brushstrokes and varied paint thickness. Use warm/cool color relationships rather than black outlines. Put firmer edges and modest impasto highlights on the flowers, and softer lost edges in the background. Let individual strokes remain legible at normal viewing size. Preserve the vase's transparency using painted light patches. No photographic blur, uniform texture overlay or melted forms.

Use the attached photograph as the only visual reference. Preserve its camera viewpoint, major silhouettes, relative positions, and recognizable subject. Simplify fine details without adding objects. Produce only the finished artwork, not a comparison, mockup or framed print. Keep the original landscape aspect ratio, at least 1400 pixels wide. No text, lettering, logos, signature or watermark; omit any signage visible in the photograph.
```

Upload a photo and describe the elements to keep. Sample photo: Jez Timms, CC0 1.0; source and license links are listed below. The example was generated from the English template. The Chinese version is untested. The displayed example does not change as you type.

</details>

<a id="graphite-sketches"></a>

### Graphite pencil sketch

Render a familiar pet or object in graphite, preserving its pose with directional pencil marks and clean paper highlights.

[AILesson ↗](https://ailesson.io/prompts/recipes/turn-photos-into-graphite-sketches) · [English prompt](prompts/graphite-sketches.md) · [中文提示词](prompts/zh-CN/graphite-sketches.md)

<details>
<summary>Copy prompt</summary>

```text
Transform the attached photo into a graphite pencil sketch.

Essential elements: {{subject}}
Palette and mood: {{palette}}

Draw a finished observational graphite sketch. Describe the cat's fur with directional tapered pencil marks that follow the body, preserving its closed eyes, muzzle shape and relaxed pose. Build shadows with layered hatching and cross-hatching; reserve clean paper for highlights. Use delicate construction lines for the window and ladder, softer than the animal. Include subtle paper tooth. No ink contours, charcoal smears, gray photo filter or excessive tiny hairs.

Use the attached photograph as the only visual reference. Preserve its camera viewpoint, major silhouettes, relative positions, and recognizable subject. Simplify fine details without adding objects. Produce only the finished artwork, not a comparison, mockup or framed print. Keep the original landscape aspect ratio, at least 1400 pixels wide. No text, lettering, logos, signature or watermark; omit any signage visible in the photograph.
```

Upload a photo and describe the elements to keep. Sample photo: Bryony Elena, Unsplash License; source and license links are listed below. The example was generated from the English template. The Chinese version is untested. The displayed example does not change as you type.

</details>

<a id="pop-art-prints"></a>

### Pop-art comic print

Give a pet photo a bold printed look using flat colors, clean outlines and selective halftone shadows.

[AILesson ↗](https://ailesson.io/prompts/recipes/turn-photos-into-pop-art-prints) · [English prompt](prompts/pop-art-prints.md) · [中文提示词](prompts/zh-CN/pop-art-prints.md)

<details>
<summary>Copy prompt</summary>

```text
Transform the attached photo into a pop-art comic print.

Essential elements: {{subject}}
Palette and mood: {{palette}}

Reinterpret as a single-panel pop-art screen print. Use bold clean ink contours, large flat color areas, and regular halftone dots confined to selected shadow shapes. Reduce fur to a few expressive zigzag tufts while preserving the animal's facial proportions and sleepy expression. Simplify the room into broad geometric planes. Keep dot scale consistent and retain generous quiet areas. No speech bubbles, captions, burst shapes, arrows, repeated panels, gradients or photographic texture.

Use the attached photograph as the only visual reference. Preserve its camera viewpoint, major silhouettes, relative positions, and recognizable subject. Simplify fine details without adding objects. Produce only the finished artwork, not a comparison, mockup or framed print. Keep the original landscape aspect ratio, at least 1400 pixels wide. No text, lettering, logos, signature or watermark; omit any signage visible in the photograph.
```

Upload a photo and describe the elements to keep. Sample photo: Bryony Elena, Unsplash License; source and license links are listed below. The example was generated from the English template. The Chinese version is untested. The displayed example does not change as you type.

</details>

<a id="retro-travel-posters"></a>

### Retro travel poster

Simplify a favorite coast or landscape into an understated travel illustration with sweeping shapes and a small print palette.

[AILesson ↗](https://ailesson.io/prompts/recipes/turn-photos-into-retro-travel-posters) · [English prompt](prompts/retro-travel-posters.md) · [中文提示词](prompts/zh-CN/retro-travel-posters.md)

<details>
<summary>Copy prompt</summary>

```text
Transform the attached photo into a retro travel poster.

Essential elements: {{subject}}
Palette and mood: {{palette}}

Redesign as a mid-century illustrated travel poster without typography. Distill terrain and buildings into confident interlocking flat shapes with elegant sweeping contours. Use three clear depth layers, strong readable light/shadow masses and a subtle lithographic paper grain. Keep the coast's silhouette geographically recognizable rather than inventing dramatic peaks. Preserve the original horizontal framing and let the artwork fill the canvas. No border, labels, slogans, gradients, 3D rendering or distressed damage.

Use the attached photograph as the only visual reference. Preserve its camera viewpoint, major silhouettes, relative positions, and recognizable subject. Simplify fine details without adding objects. Produce only the finished artwork, not a comparison, mockup or framed print. Keep the original landscape aspect ratio, at least 1400 pixels wide. No text, lettering, logos, signature or watermark; omit any signage visible in the photograph.
```

Upload a photo and describe the elements to keep. Sample photo: Leticia Golubov, Unsplash License; source and license links are listed below. The example was generated from the English template. The Chinese version is untested. The displayed example does not change as you type.

</details>

<a id="pixel-art-scenes"></a>

### Pixel-art landscape

Rebuild a landscape with crisp pixel clusters, stepped silhouettes and a compact palette inspired by classic games.

[AILesson ↗](https://ailesson.io/prompts/recipes/turn-photos-into-pixel-art-scenes) · [English prompt](prompts/pixel-art-scenes.md) · [中文提示词](prompts/zh-CN/pixel-art-scenes.md)

<details>
<summary>Copy prompt</summary>

```text
Transform the attached photo into a pixel-art landscape.

Essential elements: {{subject}}
Palette and mood: {{palette}}

Rebuild as carefully composed 16-bit-era pixel art. Use a visibly coarse, consistent square pixel grid, as if drawn at approximately 320 pixels wide and enlarged with nearest-neighbor scaling. Shape trees, mountains, roofs and water with deliberate clusters, crisp stair-step diagonals and selective ordered dithering. Make the small boathouse readable with a few high-contrast pixels. Keep distant details simpler than foreground clusters. No smooth brushwork, anti-aliased edges, photo mosaic, HUD, game characters or text. This is an aesthetic target, not a claim of an exact indexed palette.

Use the attached photograph as the only visual reference. Preserve its camera viewpoint, major silhouettes, relative positions, and recognizable subject. Simplify fine details without adding objects. Produce only the finished artwork, not a comparison, mockup or framed print. Keep the original landscape aspect ratio, at least 1400 pixels wide. No text, lettering, logos, signature or watermark; omit any signage visible in the photograph.
```

Upload a photo and describe the elements to keep. Sample photo: Rafael Peier, Unsplash License; source and license links are listed below. The example was generated from the English template. The Chinese version is untested. The displayed example does not change as you type.

</details>

<a id="layered-paper-scenes"></a>

### Layered paper scene

Rebuild a landscape from matte paper shapes, shallow overlap shadows and tactile cut edges.

[AILesson ↗](https://ailesson.io/prompts/recipes/turn-photos-into-layered-paper-scenes) · [English prompt](prompts/layered-paper-scenes.md) · [中文提示词](prompts/zh-CN/layered-paper-scenes.md)

<details>
<summary>Copy prompt</summary>

```text
Transform the attached photo into artwork in this style: Layered paper scene.

Essential elements: {{subject}}
Palette and mood: {{palette}}

Rebuild the entire landscape as a handmade layered cut-paper illustration viewed straight on. Construct hills, sea and trees from broad individually cut matte paper shapes, with subtle visible fibers and slight irregularities along scissor-cut edges. Use shallow physical overlap shadows to distinguish five to seven major depth planes, not dozens of contour-map rings. Form small houses from simple paper rectangles and pitched roofs. Keep foreground shapes broad and distant shapes restrained. No drawn outlines, photographic textures, glossy plastic, text scraps, decorative objects or deep theatrical shadows.

Use the attached photograph as the only visual reference. Preserve its camera viewpoint, major silhouettes, relative positions, and recognizable subject. Simplify fine details without adding objects. Produce only the finished artwork, not a comparison, mockup or framed print. Keep the original landscape aspect ratio, at least 1400 pixels wide. No text, lettering, logos, signature or watermark; omit any signage visible in the photograph.
```

Upload a photo and describe the elements to keep. Sample photo: Leticia Golubov, Unsplash License; source and license links are listed below. The example was generated from the English template. The Chinese version is untested. The displayed example does not change as you type.

</details>

<a id="two-color-linocuts"></a>

### Two-color linocut

Turn a pet photo into an expressive relief-print illustration with two ink colors and carved paper-white marks.

[AILesson ↗](https://ailesson.io/prompts/recipes/turn-photos-into-two-color-linocuts) · [English prompt](prompts/two-color-linocuts.md) · [中文提示词](prompts/zh-CN/two-color-linocuts.md)

<details>
<summary>Copy prompt</summary>

```text
Transform the attached photo into artwork in this style: Two-color linocut.

Essential elements: {{subject}}
Palette and mood: {{palette}}

Reinterpret as a hand-pulled two-color linocut print. Use broad solid ink masses and confident carved white channels. Follow the animal's fur direction with sparse tapered gouge marks; build the room with larger geometric cuts. Reserve unprinted cream paper for the pale fur and window light. Ink edges may show slight hand-cut wobble and tiny printing imperfections, while the main silhouette stays clean. Keep the sleeping expression and body anatomy. No pencil cross-hatching, halftone dots, smooth gradients, wood-grain overlay or photographic shading. The two-color request describes an ink-print aesthetic, not guaranteed production-ready separations.

Use the attached photograph as the only visual reference. Preserve its camera viewpoint, major silhouettes, relative positions, and recognizable subject. Simplify fine details without adding objects. Produce only the finished artwork, not a comparison, mockup or framed print. Keep the original landscape aspect ratio, at least 1400 pixels wide. No text, lettering, logos, signature or watermark; omit any signage visible in the photograph.
```

Upload a photo and describe the elements to keep. Sample photo: Bryony Elena, Unsplash License; source and license links are listed below. The example was generated from the English template. The Chinese version is untested. The displayed example does not change as you type.

</details>

<a id="cyanotype-prints"></a>

### Cyanotype print

Translate a flower or still-life photo into luminous blue-and-white tones inspired by photographic cyanotypes.

[AILesson ↗](https://ailesson.io/prompts/recipes/turn-photos-into-cyanotype-prints) · [English prompt](prompts/cyanotype-prints.md) · [中文提示词](prompts/zh-CN/cyanotype-prints.md)

<details>
<summary>Copy prompt</summary>

```text
Transform the attached photo into artwork in this style: Cyanotype print.

Essential elements: {{subject}}
Palette and mood: {{palette}}

Create a digital interpretation of a photographic cyanotype made from a negative. Keep the complete still-life composition, but translate it into rich Prussian-blue shadows, nuanced pale-blue midtones and clean paper-white highlights. Make the tulip petals and leaf veins luminous and readable against darker surroundings; preserve the vase and basket rather than isolating only a plant silhouette. Add subtle absorbent paper texture and delicate exposure variation near the outer edges. No added specimen labels, botanical names, decorative frame, sepia tint or colored flowers. This is a simulated photographic cyanotype appearance, not an actual contact photogram or a chemical-process demonstration.

Use the attached photograph as the only visual reference. Preserve its camera viewpoint, major silhouettes, relative positions, and recognizable subject. Simplify fine details without adding objects. Produce only the finished artwork, not a comparison, mockup or framed print. Keep the original landscape aspect ratio, at least 1400 pixels wide. No text, lettering, logos, signature or watermark; omit any signage visible in the photograph.
```

Upload a photo and describe the elements to keep. Sample photo: Jez Timms, CC0 1.0; source and license links are listed below. The example was generated from the English template. The Chinese version is untested. The displayed example does not change as you type.

</details>

<a id="stained-glass-panels"></a>

### Stained-glass panel

Reimagine flowers and still lifes as translucent glass pieces with dark seams and gentle backlight.

[AILesson ↗](https://ailesson.io/prompts/recipes/turn-photos-into-stained-glass-panels) · [English prompt](prompts/stained-glass-panels.md) · [中文提示词](prompts/zh-CN/stained-glass-panels.md)

<details>
<summary>Copy prompt</summary>

```text
Transform the attached photo into artwork in this style: Stained-glass panel.

Essential elements: {{subject}}
Palette and mood: {{palette}}

Translate the still life into a luminous stained-glass artwork viewed straight on, filling the image without showing a wall or external frame. Build recognizable flowers, leaves, vase and basket from intentionally shaped glass pieces bounded by slender dark lead-like seams. Let seams follow major forms and avoid arbitrary cracks across petals. Keep foreground pieces larger and readable, with restrained smaller pieces in the background. Use subtly rippled translucent glass, internal color variation and soft transmitted light, never a shiny mosaic of tiny fragments. Preserve the photo's spatial arrangement. No religious symbols, lettering, extra ornaments, starbursts or dramatic lens flare. This is concept art, not a fabrication pattern.

Use the attached photograph as the only visual reference. Preserve its camera viewpoint, major silhouettes, relative positions, and recognizable subject. Simplify fine details without adding objects. Produce only the finished artwork, not a comparison, mockup or framed print. Keep the original landscape aspect ratio, at least 1400 pixels wide. No text, lettering, logos, signature or watermark; omit any signage visible in the photograph.
```

Upload a photo and describe the elements to keep. Sample photo: Jez Timms, CC0 1.0; source and license links are listed below. The example was generated from the English template. The Chinese version is untested. The displayed example does not change as you type.

</details>

<a id="neon-contour-art"></a>

### Neon contour artwork

Reduce a familiar subject to luminous cyan contours with generous dark space and a restrained halo.

[AILesson ↗](https://ailesson.io/prompts/recipes/turn-photos-into-neon-contour-art) · [English prompt](prompts/neon-contour-art.md) · [中文提示词](prompts/zh-CN/neon-contour-art.md)

<details>
<summary>Copy prompt</summary>

```text
Transform the attached photo into artwork in this style: Neon contour artwork.

Essential elements: {{subject}}
Palette and mood: {{palette}}

Redraw the photograph as refined luminous contour-line art. Use sparse continuous light filaments to describe the subject's outer silhouette and a few essential inner features. Preserve the sleeping cat's closed eyes, muzzle, hanging paw and tail. Reduce the window and ladder to a few dim architectural lines, making the subject brighter than its surroundings. Keep most areas dark and empty; do not trace every hair or fill surfaces with neon. Use a narrow bright line core and only a restrained soft halo. No visible neon-tube hardware, text, grids, particles, lens flares, cyberpunk signs, solid painted fills or rainbow gradients.

Use the attached photograph as the only visual reference. Preserve its camera viewpoint, major silhouettes, relative positions, and recognizable subject. Simplify fine details without adding objects. Produce only the finished artwork, not a comparison, mockup or framed print. Keep the original landscape aspect ratio, at least 1400 pixels wide. No text, lettering, logos, signature or watermark; omit any signage visible in the photograph.
```

Upload a photo and describe the elements to keep. Sample photo: Bryony Elena, Unsplash License; source and license links are listed below. The example was generated from the English template. The Chinese version is untested. The displayed example does not change as you type.

</details>

<a id="digital-wireframe-landscapes"></a>

### Digital wireframe landscape

Rebuild a landscape as fine architectural mesh lines, quiet dark planes and a small luminous focal accent.

[AILesson ↗](https://ailesson.io/prompts/recipes/turn-photos-into-digital-wireframe-landscapes) · [English prompt](prompts/digital-wireframe-landscapes.md) · [中文提示词](prompts/zh-CN/digital-wireframe-landscapes.md)

<details>
<summary>Copy prompt</summary>

```text
Transform the attached photo into artwork in this style: Digital wireframe landscape.

Essential elements: {{subject}}
Palette and mood: {{palette}}

Reconstruct the landscape as a clean futuristic architectural wireframe visualization. Describe hills using a moderately spaced coherent triangular terrain mesh that follows the slopes. Draw houses as simple fine-line volumes; keep the bay as a quiet dark plane with only a few long perspective lines. Make the closest mesh edges slightly brighter and thicker, and distant edges finer and dimmer. Preserve the recognizable headland, beach and hillside settlement. Avoid uniform screen-space grids, random laser scribbles, dense glowing fog, surface photo textures and invented skyscrapers. The geometry is a stylized visual interpretation, not surveyed topography or a recoverable 3D mesh. No axis markers, coordinates, labels, HUD, border or text.

Use the attached photograph as the only visual reference. Preserve its camera viewpoint, major silhouettes, relative positions, and recognizable subject. Simplify fine details without adding objects. Produce only the finished artwork, not a comparison, mockup or framed print. Keep the original landscape aspect ratio, at least 1400 pixels wide. No text, lettering, logos, signature or watermark; omit any signage visible in the photograph.
```

Upload a photo and describe the elements to keep. Sample photo: Leticia Golubov, Unsplash License; source and license links are listed below. The example was generated from the English template. The Chinese version is untested. The displayed example does not change as you type.

</details>

<a id="iridescent-metal-renders"></a>

### Iridescent metal render

Recast flowers or objects as pearlescent metal sculptures with soft studio reflections and a quiet pale setting.

[AILesson ↗](https://ailesson.io/prompts/recipes/turn-photos-into-iridescent-metal-renders) · [English prompt](prompts/iridescent-metal-renders.md) · [中文提示词](prompts/zh-CN/iridescent-metal-renders.md)

<details>
<summary>Copy prompt</summary>

```text
Transform the attached photo into artwork in this style: Iridescent metal render.

Essential elements: {{subject}}
Palette and mood: {{palette}}

Reinterpret the still life as a sophisticated sculptural 3D product render. Convert the tulip petals and leaves into smooth thin iridescent metal forms, preserving the bouquet silhouette and stems. Keep the vase clear polished glass. Simplify the wicker basket into a matte warm-white sculptural woven volume so it does not compete with the reflective flowers. Simplify the window background into soft architectural planes while preserving the original object arrangement. Use large softbox-like reflections to reveal curvature and restrained thin-film-like color shifts; keep broad quiet silver areas. No liquid melting, mirror chaos, neon glow, oil-slick saturation, faceted crystals, extra flowers or text. This is a raster image with a holographic-material aesthetic, not a hologram or an editable 3D model.

Use the attached photograph as the only visual reference. Preserve its camera viewpoint, major silhouettes, relative positions, and recognizable subject. Simplify fine details without adding objects. Produce only the finished artwork, not a comparison, mockup or framed print. Keep the original landscape aspect ratio, at least 1400 pixels wide. No text, lettering, logos, signature or watermark; omit any signage visible in the photograph.
```

Upload a photo and describe the elements to keep. Sample photo: Jez Timms, CC0 1.0; source and license links are listed below. The example was generated from the English template. The Chinese version is untested. The displayed example does not change as you type.

</details>

<a id="3d-miniature-worlds"></a>

### 3D miniature world

Turn a favorite place into a compact 3D-style landscape model with sculpted terrain, glassy water and soft studio light.

[AILesson ↗](https://ailesson.io/prompts/recipes/turn-photos-into-3d-miniature-worlds) · [English prompt](prompts/3d-miniature-worlds.md) · [中文提示词](prompts/zh-CN/3d-miniature-worlds.md)

<details>
<summary>Copy prompt</summary>

```text
Transform the attached photo into artwork in this style: 3D miniature world.

Essential elements: {{subject}}
Palette and mood: {{palette}}

Turn the photographed place into a polished miniature 3D landscape model on one thin rounded rectangular terrain base. Keep the boathouse at the left lakeshore, forest behind it and mountain ridges farther back, with the lake opening toward the right foreground. Deliberately reframe from a slightly elevated three-quarter camera so the complete miniature base is visible, while preserving these landmark relationships. Reduce distant scenery into a compact sculpted mountain backdrop on the same base. Use smooth matte ceramic-like terrain, simplified tree volumes, a glassy turquoise water slab with a visible edge and softly beveled architecture. Center the unified model with generous clean studio space around it and soft contact shadows beneath. No floating separate islands, cutaway labels, tiny people, extra buildings, toy packaging, text or excessive depth-of-field blur. Produce a landscape-format image at least 1400 pixels wide. This is a 3D-style concept illustration, not a reconstructable or printable model.

Use the attached photo as the landmark reference. Output only the finished artwork, with no comparison collage, watermark or signage.
```

Upload a photo and describe the elements to keep. Sample photo: Rafael Peier, Unsplash License; source and license links are listed below. The example was generated from the English template. The Chinese version is untested. The displayed example does not change as you type. The displayed result also received a cleanup edit to simplify forms and remove roof lettering.

</details>

## About the examples

Images load from the AILesson CDN; the repository does not store image copies and offline clones do not include them. Content-addressed URLs do not automatically follow upstream image replacements. Update the data and rebuild the READMEs when an example changes.

[data/prompts.json](data/prompts.json) preserves actual inputs, generation prompts, reference associations, revisions, postprocessing, and observed limitations. Outputs are raster examples; 3D, glass, and printmaking styles do not include editable models or fabrication plans.

## Contributing

Prompt improvements, new styles, and translation fixes are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) and our [Code of Conduct](CODE_OF_CONDUCT.md).

## License and image credits

Prompts, documentation, and scripts use the [MIT License](LICENSE). Third-party reference photos retain their Unsplash License or CC0 terms and are not relicensed under MIT. AILesson’s original contributions to generated examples are offered under MIT to the extent it holds applicable rights; applicable source-photo terms still apply. See [IMAGE_CREDITS.md](IMAGE_CREDITS.md) for per-style attribution and references.

---

[AILesson](https://ailesson.io) · [Image prompts](https://ailesson.io/prompts/types/image) · [Icon prompts](https://github.com/ailessonio/icon-prompts)
