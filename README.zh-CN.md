<h1 align="center">Photo Style Prompts · 照片风格转换提示词</h1>

<p align="center">把照片变成艺术画。对照效果，选择风格，复制提示词。</p>

<p align="center"><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="https://ailesson.io/zh/prompts/types/image">AILesson</a> · <a href="LICENSE">MIT License</a></p>

使用可复用的 AI 图片编辑提示词，将照片转换为水彩、动画场景、油画、素描、像素画与更多风格。浏览风格效果，点击预览图进入 [AILesson](https://ailesson.io/zh) 完整配方。

## 快速开始

1. 在下方图库中选择一种风格，展开提示词。
2. 将自己的照片上传到支持参考图的 AI 图片生成或编辑工具。
3. 填写模板中的变量，说明需要保留的主体、构图与配色。
4. 运行提示词，再对照原图检查视角、位置关系、轮廓及文字。

多数模板使用 `{{subject}}` 与 `{{palette}}`。水彩旅行画使用 `{{scene}}`、`{{palette}}` 和 `{{caption}}`；不需要题字时将 `caption` 设为 `NONE`。各风格的独立提示词文件提供变量说明与示例输入。

示例由英文提示词生成；中文模板尚未单独验证。它们展示真实生成结果，但不保证每次重复运行得到同样的图像。

## 风格图库

点击效果图，在 AILesson 查看完整配方；点击风格名，跳转到本页提示词。

| | | |
| :---: | :---: | :---: |
| **[留白水彩旅行画](#watercolor-travel-prints)**<br><br><a href="https://ailesson.io/zh/prompts/recipes/turn-photos-into-watercolor-travel-prints"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/01/5d/015dc54d62ec2fe26f45b9dc60ceeed65fbd130c0099c57542d6c38750ff8586.png" alt="蓝灰色水彩湖景小画，左侧为雪山，右侧为亮着暖光的木屋，四周留有宽阔象牙色纸面。" width="240"></a> | **[手绘动画场景](#hand-painted-anime-scenes)**<br><br><a href="https://ailesson.io/zh/prompts/recipes/turn-photos-into-hand-painted-anime-scenes"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/97/76/9776ea79c20a4905efae2d1428dbf0c3cf90ab94da365b5bdc8c6b295e101249.png" alt="金色草坡、绿色山坡、蓝色海湾与山间小屋组成的手绘海岸全景，天空绘有云层。" width="240"></a> | **[印象派油画](#impressionist-oil-paintings)**<br><br><a href="https://ailesson.io/zh/prompts/recipes/turn-photos-into-impressionist-oil-paintings"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/90/9b/909be6a851abed4a5a858956c1e2abeca519a8de1d46624ba50dd9d6d3c5da85.png" alt="玻璃瓶中的粉色郁金香与藤篮静物油画，呈现厚薄笔触和温暖窗光。" width="240"></a> |
| **[石墨铅笔素描](#graphite-sketches)**<br><br><a href="https://ailesson.io/zh/prompts/recipes/turn-photos-into-graphite-sketches"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/0a/bb/0abbc60926261aa9b2d2e98809444b5acd66899abaec117e66f5319d1bd955ab.png" alt="窗台上熟睡的蓬松猫咪石墨素描，一条肢体垂下，右侧梯子以浅线绘出。" width="240"></a> | **[波普漫画印画](#pop-art-prints)**<br><br><a href="https://ailesson.io/zh/prompts/recipes/turn-photos-into-pop-art-prints"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/24/40/2440784288af45ca4fc718cb5f8112de718b4a08d0e45ae48c8beaebdee377e8.png" alt="奶油色熟睡猫咪，搭配深色漫画轮廓、珊瑚红与青蓝室内色块及局部半调网点。" width="240"></a> | **[复古旅行海报](#retro-travel-posters)**<br><br><a href="https://ailesson.io/zh/prompts/recipes/turn-photos-into-retro-travel-posters"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/d3/34/d334c19f4d428ae0978f2445d9a54861c645602349edaff7f2d605ab6ce48664.png" alt="以赭色田野和深绿山坡围绕海湾村庄的复古平涂插画，海岸呈弧形延伸。" width="240"></a> |
| **[像素艺术场景](#pixel-art-scenes)**<br><br><a href="https://ailesson.io/zh/prompts/recipes/turn-photos-into-pixel-art-scenes"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/a6/17/a6178f488396fb2297a3b440e581581b3197ac30460f2cce4941e3bb8affd20d.png" alt="左侧有红顶船屋、深色松树与金色前景灌木的像素山湖风景。" width="240"></a> | **[层叠剪纸场景](#layered-paper-scenes)**<br><br><a href="https://ailesson.io/zh/prompts/recipes/turn-photos-into-layered-paper-scenes"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/bc/1e/bc1e864434ee614dfda46fffac8443c6cde578965c41d7d65434561e4a495964.png" alt="由赭色田野、绿色剪纸树丛、青绿海面与奶油色小屋组成的层叠纸艺海岸全景。" width="240"></a> | **[双色油毡版画](#two-color-linocuts)**<br><br><a href="https://ailesson.io/zh/prompts/recipes/turn-photos-into-two-color-linocuts"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/ef/e4/efe415278a1bf9b4eb9d23f60b8afbd2f6e4f4c921f8da5bf23f1ab0de4bf26d.png" alt="靛蓝与陶土红双色油毡版画风格的熟睡奶油色猫咪，旁边为窗户与梯子。" width="240"></a> |
| **[蓝晒印相](#cyanotype-prints)**<br><br><a href="https://ailesson.io/zh/prompts/recipes/turn-photos-into-cyanotype-prints"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/c0/27/c027013d73e6427621a58ecf113675664dfb43aa2f20d8ba7bf146b65a34aa87.png" alt="蓝白影调的蓝晒风格静物，包含郁金香、玻璃花瓶与藤篮。" width="240"></a> | **[彩色玻璃画](#stained-glass-panels)**<br><br><a href="https://ailesson.io/zh/prompts/recipes/turn-photos-into-stained-glass-panels"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/93/8b/938b7791b1ae0c7ac8fc55b3c387c988fabf0a8bfdf23f476fd158a1ae1c9321.png" alt="粉色郁金香与藤篮被转译为透光彩色玻璃，搭配绿色叶片和琥珀色玻璃区域。" width="240"></a> | **[霓虹轮廓线](#neon-contour-art)**<br><br><a href="https://ailesson.io/zh/prompts/recipes/turn-photos-into-neon-contour-art"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/ad/4f/ad4f4c064e4180d2cab6164a477b4874257efb6fa0fbdb511b06a31a3fcaae33.png" alt="深海军蓝背景上的青色光线熟睡猫咪，窗户和梯子轮廓较暗。" width="240"></a> |
| **[数字线框地景](#digital-wireframe-landscapes)**<br><br><a href="https://ailesson.io/zh/prompts/recipes/turn-photos-into-digital-wireframe-landscapes"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/78/6a/786a4f97a52e44c500a5a5ccabb7ccf71e1c179cb62485fdbee47e48eb4a05a9.png" alt="午夜蓝海岸风景，以青色三角网格表现地形，局部海岸为青柠色。" width="240"></a> | **[虹彩金属渲染](#iridescent-metal-renders)**<br><br><a href="https://ailesson.io/zh/prompts/recipes/turn-photos-into-iridescent-metal-renders"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/3b/e5/3be5ddd6e64ed7809f417bd3217d8ccdeb28b9f65f734e39ea0d335759b49f5f.png" alt="带粉蓝反射的珍珠银郁金香置于透明花瓶中，旁边为浅色编织藤篮。" width="240"></a> | **[3D 微缩世界](#3d-miniature-worlds)**<br><br><a href="https://ailesson.io/zh/prompts/recipes/turn-photos-into-3d-miniature-worlds"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/8e/ad/8eaddfc7837080402cb0f8111802e4cb64cc4285a1310770110b939ae09a6242.png" alt="紧凑的三维风格山湖模型，含青绿湖水、瓷白山体、绿树和陶土红顶船屋。" width="240"></a> |

## 提示词

<a id="watercolor-travel-prints"></a>

### 留白水彩旅行画

保留照片的关键景物与视角，将熟悉的场景画成象牙色纸面上的留白水彩小景。

[AILesson ↗](https://ailesson.io/zh/prompts/recipes/turn-photos-into-watercolor-travel-prints) · [English prompt](prompts/watercolor-travel-prints.md) · [中文提示词](prompts/zh-CN/watercolor-travel-prints.md)

<details>
<summary>展开提示词</summary>

```text
将上传的场景照片转化为宁静的水彩旅行画。

场景与关键景物：{{scene}}
配色与氛围：{{palette}}
题字：{{caption}}

以上传照片为构图参考。在画中的场景内部保留原始视角、可辨认的轮廓、所列景物的相对位置与远近关系。简化细节，不凭空增添物件。使用透明水彩薄涂、轻微颜料晕染、断续干笔和柔软不规则边缘，在带有细微可见纸纹的暖象牙色纸上重新绘制。让天空与水面自然淡入未着色纸面。配色克制，只留一小处暖光；无粗重描边、摄影纹理或亮面三维效果。

输出至少 1024×1024 像素的方形艺术画。将完整的小场景居中，宽度约占画布的 50–55%，四周保留充足空白纸面。不把原照片铺满画布，不输出前后对比拼图。题字为 NONE 时不加任何文字；否则仅将提供的题字用小巧克制的手写字体放在画下，不编造日期或额外文字。不含画框、水印或新增的人物、车辆、建筑。
```

上传场景照片并填写变量。本页参考图为 AI 生成的虚构照片，并非真实地点或原作者图片。示例使用英文模板及该参考图生成；中文与题字变体尚未测试。固定示例不会随输入实时变化。

</details>

<a id="hand-painted-anime-scenes"></a>

### 手绘动画场景

保留海岸风景的辨识度，用明亮水粉色块与分层景深将照片重绘为动画背景。

[AILesson ↗](https://ailesson.io/zh/prompts/recipes/turn-photos-into-hand-painted-anime-scenes) · [English prompt](prompts/hand-painted-anime-scenes.md) · [中文提示词](prompts/zh-CN/hand-painted-anime-scenes.md)

<details>
<summary>展开提示词</summary>

```text
将上传照片转化为手绘动画场景。

必须保留的元素：{{subject}}
配色与氛围：{{palette}}

重绘为二维动画电影的手绘背景。使用类似不透明水粉的色块、细致的建筑轮廓、柔和分层的空气透视与少量清晰高光。前景草地简化为有节奏的笔触形状，通过明度与冷暖区分近中远景。村庄在景观中保持较小比例。避免摄影质感、塑料三维光影、粗重漫画描边和可辨认的影视系列元素。

以上传照片为唯一视觉参考，保留相机视角、主要轮廓、相对位置与可辨认的主体。简化细节，不添加物件。仅输出成品画作，不输出对比拼图、样机或带框印刷品。保持原图横向宽高比，宽度至少 1400 像素。不含文字、字母、标志、签名或水印；省略照片中原有的标牌文字。
```

上传照片并描述需要保留的元素。示例摄影：Leticia Golubov，采用 Unsplash License 授权；来源与许可链接见下方。示例使用英文模板生成，中文版本尚未测试。展示的示例不会随输入实时变化。

</details>

<a id="impressionist-oil-paintings"></a>

### 印象派油画

把花卉或桌面照片转成油画，以碎色、可见笔触与柔和背景边缘表现颜料质感。

[AILesson ↗](https://ailesson.io/zh/prompts/recipes/turn-photos-into-impressionist-oil-paintings) · [English prompt](prompts/impressionist-oil-paintings.md) · [中文提示词](prompts/zh-CN/impressionist-oil-paintings.md)

<details>
<summary>展开提示词</summary>

```text
将上传照片转化为印象派油画。

必须保留的元素：{{subject}}
配色与氛围：{{palette}}

重绘为印象派静物油画。以可见的短碎笔触与不同厚薄的颜料塑造花瓣、玻璃和藤编，用色彩冷暖关系代替黑色描边。花朵采用较清晰的边缘与适度厚涂高光，背景边缘柔和消隐。正常观看尺寸下仍能辨认单笔笔触，以光斑绘画表现玻璃的透明感。避免摄影虚化、统一纹理覆盖或融化般的形体。

以上传照片为唯一视觉参考，保留相机视角、主要轮廓、相对位置与可辨认的主体。简化细节，不添加物件。仅输出成品画作，不输出对比拼图、样机或带框印刷品。保持原图横向宽高比，宽度至少 1400 像素。不含文字、字母、标志、签名或水印；省略照片中原有的标牌文字。
```

上传照片并描述需要保留的元素。示例摄影：Jez Timms，采用 CC0 1.0 授权；来源与许可链接见下方。示例使用英文模板生成，中文版本尚未测试。展示的示例不会随输入实时变化。

</details>

<a id="graphite-sketches"></a>

### 石墨铅笔素描

以石墨排线重绘熟悉的宠物或物件，用有方向的铅笔线与纸面高光保留姿态。

[AILesson ↗](https://ailesson.io/zh/prompts/recipes/turn-photos-into-graphite-sketches) · [English prompt](prompts/graphite-sketches.md) · [中文提示词](prompts/zh-CN/graphite-sketches.md)

<details>
<summary>展开提示词</summary>

```text
将上传照片转化为石墨铅笔素描。

必须保留的元素：{{subject}}
配色与氛围：{{palette}}

绘制完整的观察式石墨素描。用顺着身体走向、末端收尖的铅笔线表现猫毛，保留闭合的眼睛、口鼻形状与放松姿态。以层叠排线和交叉排线构建阴影，为高光保留干净纸面。窗户与梯子使用比主体更轻的结构线，呈现细微纸纹。避免墨线轮廓、炭笔涂抹、照片灰度滤镜和过密碎毛。

以上传照片为唯一视觉参考，保留相机视角、主要轮廓、相对位置与可辨认的主体。简化细节，不添加物件。仅输出成品画作，不输出对比拼图、样机或带框印刷品。保持原图横向宽高比，宽度至少 1400 像素。不含文字、字母、标志、签名或水印；省略照片中原有的标牌文字。
```

上传照片并描述需要保留的元素。示例摄影：Bryony Elena，采用 Unsplash License 授权；来源与许可链接见下方。示例使用英文模板生成，中文版本尚未测试。展示的示例不会随输入实时变化。

</details>

<a id="pop-art-prints"></a>

### 波普漫画印画

用平涂色块、清晰描边与局部半调阴影，让宠物照片呈现鲜明的波普印刷效果。

[AILesson ↗](https://ailesson.io/zh/prompts/recipes/turn-photos-into-pop-art-prints) · [English prompt](prompts/pop-art-prints.md) · [中文提示词](prompts/zh-CN/pop-art-prints.md)

<details>
<summary>展开提示词</summary>

```text
将上传照片转化为波普漫画印画。

必须保留的元素：{{subject}}
配色与氛围：{{palette}}

转化为单幅波普丝网印画。使用干净有力的墨线轮廓、大面积平涂色块，以及仅位于部分阴影内的规则半调网点。毛发简化为少量有表现力的锯齿状毛簇，同时保留猫咪的面部比例与困倦表情。室内简化为宽阔几何平面，网点尺度一致并保留足够安静区域。无对话框、标题、爆炸形、箭头、多格拼图、渐变或摄影纹理。

以上传照片为唯一视觉参考，保留相机视角、主要轮廓、相对位置与可辨认的主体。简化细节，不添加物件。仅输出成品画作，不输出对比拼图、样机或带框印刷品。保持原图横向宽高比，宽度至少 1400 像素。不含文字、字母、标志、签名或水印；省略照片中原有的标牌文字。
```

上传照片并描述需要保留的元素。示例摄影：Bryony Elena，采用 Unsplash License 授权；来源与许可链接见下方。示例使用英文模板生成，中文版本尚未测试。展示的示例不会随输入实时变化。

</details>

<a id="retro-travel-posters"></a>

### 复古旅行海报

将喜爱的海岸或风景简化为复古旅行插画，使用流畅形状与克制的印刷配色。

[AILesson ↗](https://ailesson.io/zh/prompts/recipes/turn-photos-into-retro-travel-posters) · [English prompt](prompts/retro-travel-posters.md) · [中文提示词](prompts/zh-CN/retro-travel-posters.md)

<details>
<summary>展开提示词</summary>

```text
将上传照片转化为复古旅行海报。

必须保留的元素：{{subject}}
配色与氛围：{{palette}}

重设计为不含文字的二十世纪中期旅行海报插画。将地形与建筑归纳为相互衔接的明确平面色块，轮廓流畅优雅。使用清晰的三层景深、容易辨认的大块明暗及细微石版印刷纸纹。保留海岸轮廓的可辨认性，不虚构陡峭山峰。保持原图横向取景，画面铺满画布。无边框、地名、标语、渐变、三维渲染或破损做旧。

以上传照片为唯一视觉参考，保留相机视角、主要轮廓、相对位置与可辨认的主体。简化细节，不添加物件。仅输出成品画作，不输出对比拼图、样机或带框印刷品。保持原图横向宽高比，宽度至少 1400 像素。不含文字、字母、标志、签名或水印；省略照片中原有的标牌文字。
```

上传照片并描述需要保留的元素。示例摄影：Leticia Golubov，采用 Unsplash License 授权；来源与许可链接见下方。示例使用英文模板生成，中文版本尚未测试。展示的示例不会随输入实时变化。

</details>

<a id="pixel-art-scenes"></a>

### 像素艺术场景

用清晰像素簇、阶梯轮廓与紧凑配色重建风景，呈现经典游戏般的画面。

[AILesson ↗](https://ailesson.io/zh/prompts/recipes/turn-photos-into-pixel-art-scenes) · [English prompt](prompts/pixel-art-scenes.md) · [中文提示词](prompts/zh-CN/pixel-art-scenes.md)

<details>
<summary>展开提示词</summary>

```text
将上传照片转化为像素艺术场景。

必须保留的元素：{{subject}}
配色与氛围：{{palette}}

重绘为精心构图的十六位时代像素画。采用明显粗颗粒且一致的方形像素网格，如同以约 320 像素宽绘制后使用最近邻放大。用有意组织的像素簇、清晰阶梯状斜线与少量有序抖色塑造树木、山峰、屋顶和水面。以少量高对比像素让小船屋可辨认，远景细节比前景像素簇更简洁。无平滑笔触、抗锯齿边缘、照片马赛克、游戏界面、角色或文字。这是视觉目标，不承诺精确的索引色数量。

以上传照片为唯一视觉参考，保留相机视角、主要轮廓、相对位置与可辨认的主体。简化细节，不添加物件。仅输出成品画作，不输出对比拼图、样机或带框印刷品。保持原图横向宽高比，宽度至少 1400 像素。不含文字、字母、标志、签名或水印；省略照片中原有的标牌文字。
```

上传照片并描述需要保留的元素。示例摄影：Rafael Peier，采用 Unsplash License 授权；来源与许可链接见下方。示例使用英文模板生成，中文版本尚未测试。展示的示例不会随输入实时变化。

</details>

<a id="layered-paper-scenes"></a>

### 层叠剪纸场景

用哑光纸片、浅叠压阴影与可见剪切边缘，将风景照片重构为手工剪纸场景。

[AILesson ↗](https://ailesson.io/zh/prompts/recipes/turn-photos-into-layered-paper-scenes) · [English prompt](prompts/layered-paper-scenes.md) · [中文提示词](prompts/zh-CN/layered-paper-scenes.md)

<details>
<summary>展开提示词</summary>

```text
将上传照片转化为层叠剪纸场景。

必须保留的元素：{{subject}}
配色与氛围：{{palette}}

把整个风景重构为正面观看的手工层叠剪纸插画。山坡、海面与树木由独立裁切的宽阔哑光纸片组成，呈现细微纸纤维和略有不规则的剪切边缘。使用浅浅的叠压阴影区分五至七个主要远近层次，不画成密集等高线。小房屋由简单纸矩形与坡屋顶组成，前景形状宽阔，远景简洁。无描线、摄影纹理、亮面塑料、报纸文字碎片、装饰物或深重舞台阴影。

以上传照片为唯一视觉参考，保留相机视角、主要轮廓、相对位置与可辨认的主体。简化细节，不添加物件。仅输出成品画作，不输出对比拼图、样机或带框印刷品。保持原图横向宽高比，宽度至少 1400 像素。不含文字、字母、标志、签名或水印；省略照片中原有的标牌文字。
```

上传照片并描述需要保留的元素。示例摄影：Leticia Golubov，采用 Unsplash License 授权；来源与许可链接见下方。示例使用英文模板生成，中文版本尚未测试。展示的示例不会随输入实时变化。

</details>

<a id="two-color-linocuts"></a>

### 双色油毡版画

用两种油墨色与纸白刻痕，将宠物照片转成有表现力的凸版印刷插画。

[AILesson ↗](https://ailesson.io/zh/prompts/recipes/turn-photos-into-two-color-linocuts) · [English prompt](prompts/two-color-linocuts.md) · [中文提示词](prompts/zh-CN/two-color-linocuts.md)

<details>
<summary>展开提示词</summary>

```text
将上传照片转化为双色油毡版画。

必须保留的元素：{{subject}}
配色与氛围：{{palette}}

转化为手工压印的双色油毡版画。使用大块实色油墨和明确的留白刻槽，以少量末端收尖的刀痕顺着毛发方向排列，室内采用更宽阔的几何刻面。浅色毛发与窗光保留为未上墨的奶油色纸面。墨色边缘可有轻微手工晃动与细小压印不匀，但主要轮廓保持干净，保留熟睡表情与身体结构。无铅笔交叉排线、半调网点、平滑渐变、木纹覆盖或摄影明暗。双色要求描述油墨印刷的视觉效果，不保证可生产的分色稿。

以上传照片为唯一视觉参考，保留相机视角、主要轮廓、相对位置与可辨认的主体。简化细节，不添加物件。仅输出成品画作，不输出对比拼图、样机或带框印刷品。保持原图横向宽高比，宽度至少 1400 像素。不含文字、字母、标志、签名或水印；省略照片中原有的标牌文字。
```

上传照片并描述需要保留的元素。示例摄影：Bryony Elena，采用 Unsplash License 授权；来源与许可链接见下方。示例使用英文模板生成，中文版本尚未测试。展示的示例不会随输入实时变化。

</details>

<a id="cyanotype-prints"></a>

### 蓝晒印相

将花卉或静物照片转成明亮蓝白影调，模拟摄影蓝晒的纸面效果。

[AILesson ↗](https://ailesson.io/zh/prompts/recipes/turn-photos-into-cyanotype-prints) · [English prompt](prompts/cyanotype-prints.md) · [中文提示词](prompts/zh-CN/cyanotype-prints.md)

<details>
<summary>展开提示词</summary>

```text
将上传照片转化为蓝晒印相。

必须保留的元素：{{subject}}
配色与氛围：{{palette}}

创作以照片负片制成蓝晒印相的数字化转译。保留完整静物构图，将影调转为浓郁普鲁士蓝阴影、细腻浅蓝中间调与干净纸白高光。让郁金香花瓣与叶脉在较暗环境中明亮可辨，保留花瓶与藤篮，不只提取植物剪影。加入细微吸水纸纹和外缘轻微曝光变化。不添加标本标签、植物名称、装饰边框、棕褐色调或彩色花朵。这是模拟摄影蓝晒的视觉效果，不是真实接触式物影照片或化学工艺演示。

以上传照片为唯一视觉参考，保留相机视角、主要轮廓、相对位置与可辨认的主体。简化细节，不添加物件。仅输出成品画作，不输出对比拼图、样机或带框印刷品。保持原图横向宽高比，宽度至少 1400 像素。不含文字、字母、标志、签名或水印；省略照片中原有的标牌文字。
```

上传照片并描述需要保留的元素。示例摄影：Jez Timms，采用 CC0 1.0 授权；来源与许可链接见下方。示例使用英文模板生成，中文版本尚未测试。展示的示例不会随输入实时变化。

</details>

<a id="stained-glass-panels"></a>

### 彩色玻璃画

用透光玻璃片、深色接缝与柔和背光，将花卉静物转成彩色玻璃画。

[AILesson ↗](https://ailesson.io/zh/prompts/recipes/turn-photos-into-stained-glass-panels) · [English prompt](prompts/stained-glass-panels.md) · [中文提示词](prompts/zh-CN/stained-glass-panels.md)

<details>
<summary>展开提示词</summary>

```text
将上传照片转化为彩色玻璃画。

必须保留的元素：{{subject}}
配色与氛围：{{palette}}

将静物转成正面观看的透光彩色玻璃画，画面铺满图片，不展示墙壁或外部画框。用有意塑形的玻璃片组成可辨认的花朵、叶片、花瓶与藤篮，以细窄深色铅条般的接缝划分。接缝顺着主要形体排列，避免任意裂纹穿过花瓣。前景玻璃片较大且清楚，背景仅使用克制的小片。呈现轻微波纹半透明玻璃、内部色彩变化与柔和透射光，避免大量亮面碎片马赛克。保留原照空间关系，无宗教符号、文字、额外装饰、星芒或强烈镜头眩光。这是概念插画，不是制作图纸。

以上传照片为唯一视觉参考，保留相机视角、主要轮廓、相对位置与可辨认的主体。简化细节，不添加物件。仅输出成品画作，不输出对比拼图、样机或带框印刷品。保持原图横向宽高比，宽度至少 1400 像素。不含文字、字母、标志、签名或水印；省略照片中原有的标牌文字。
```

上传照片并描述需要保留的元素。示例摄影：Jez Timms，采用 CC0 1.0 授权；来源与许可链接见下方。示例使用英文模板生成，中文版本尚未测试。展示的示例不会随输入实时变化。

</details>

<a id="neon-contour-art"></a>

### 霓虹轮廓线

将熟悉的主体归纳为青色发光轮廓，以充足暗部留白和克制光晕呈现未来感。

[AILesson ↗](https://ailesson.io/zh/prompts/recipes/turn-photos-into-neon-contour-art) · [English prompt](prompts/neon-contour-art.md) · [中文提示词](prompts/zh-CN/neon-contour-art.md)

<details>
<summary>展开提示词</summary>

```text
将上传照片转化为霓虹轮廓线。

必须保留的元素：{{subject}}
配色与氛围：{{palette}}

将照片重绘为精致的发光轮廓线艺术。用稀疏连续光丝描述主体外轮廓及少量关键内部特征，保留猫咪闭合的眼睛、口鼻、垂下的爪子与尾巴。窗户和梯子简化为少量较暗建筑线，主体亮于环境。大部分区域保持暗色留空，不描出每根毛，也不以霓虹填满表面。线条中心细亮，仅带克制柔光。无可见灯管五金、文字、网格、粒子、镜头眩光、赛博朋克招牌、实色涂面或彩虹渐变。

以上传照片为唯一视觉参考，保留相机视角、主要轮廓、相对位置与可辨认的主体。简化细节，不添加物件。仅输出成品画作，不输出对比拼图、样机或带框印刷品。保持原图横向宽高比，宽度至少 1400 像素。不含文字、字母、标志、签名或水印；省略照片中原有的标牌文字。
```

上传照片并描述需要保留的元素。示例摄影：Bryony Elena，采用 Unsplash License 授权；来源与许可链接见下方。示例使用英文模板生成，中文版本尚未测试。展示的示例不会随输入实时变化。

</details>

<a id="digital-wireframe-landscapes"></a>

### 数字线框地景

将风景重建为精细建筑网格线、安静暗色平面和少量发光焦点。

[AILesson ↗](https://ailesson.io/zh/prompts/recipes/turn-photos-into-digital-wireframe-landscapes) · [English prompt](prompts/digital-wireframe-landscapes.md) · [中文提示词](prompts/zh-CN/digital-wireframe-landscapes.md)

<details>
<summary>展开提示词</summary>

```text
将上传照片转化为数字线框地景。

必须保留的元素：{{subject}}
配色与氛围：{{palette}}

将风景重构为干净的未来建筑线框表现。用间距适中、结构连贯的三角地形网格顺着坡度描述山坡，房屋用简单细线体块表示。海湾保留为安静暗色平面，仅有少量长透视线。近处网格边稍亮稍粗，远处更细更暗，保留可辨认的岬角、海滩与山坡聚落。避免覆盖屏幕的均匀网格、随机激光涂鸦、浓重光雾、照片表面纹理或虚构摩天楼。几何形态是视觉转译，不是测绘地形或可提取的三维网格。无坐标轴、坐标值、标签、游戏界面、边框或文字。

以上传照片为唯一视觉参考，保留相机视角、主要轮廓、相对位置与可辨认的主体。简化细节，不添加物件。仅输出成品画作，不输出对比拼图、样机或带框印刷品。保持原图横向宽高比，宽度至少 1400 像素。不含文字、字母、标志、签名或水印；省略照片中原有的标牌文字。
```

上传照片并描述需要保留的元素。示例摄影：Leticia Golubov，采用 Unsplash License 授权；来源与许可链接见下方。示例使用英文模板生成，中文版本尚未测试。展示的示例不会随输入实时变化。

</details>

<a id="iridescent-metal-renders"></a>

### 虹彩金属渲染

将花卉或物件转成珍珠虹彩金属雕塑，以柔和工作室反射和浅色环境突出材质。

[AILesson ↗](https://ailesson.io/zh/prompts/recipes/turn-photos-into-iridescent-metal-renders) · [English prompt](prompts/iridescent-metal-renders.md) · [中文提示词](prompts/zh-CN/iridescent-metal-renders.md)

<details>
<summary>展开提示词</summary>

```text
将上传照片转化为虹彩金属渲染。

必须保留的元素：{{subject}}
配色与氛围：{{palette}}

将静物转译为精致的雕塑式三维产品渲染图。花瓣与叶片变为光滑薄片状虹彩金属，保留花束轮廓与花茎；花瓶保持清透抛光玻璃。藤篮简化为暖白哑光雕塑式编织体积，使其不与反光花朵争夺注意力。窗户背景简化为柔和建筑平面，保留原物件排列。以大型柔光箱般的反射展示曲面，薄膜般色彩变化克制，保留宽阔安静银色区域。无液体融化、混乱镜像、霓虹发光、高饱和油膜、晶体切面、新增花朵或文字。结果是全息材质观感的位图，不是全息影像或可编辑三维模型。

以上传照片为唯一视觉参考，保留相机视角、主要轮廓、相对位置与可辨认的主体。简化细节，不添加物件。仅输出成品画作，不输出对比拼图、样机或带框印刷品。保持原图横向宽高比，宽度至少 1400 像素。不含文字、字母、标志、签名或水印；省略照片中原有的标牌文字。
```

上传照片并描述需要保留的元素。示例摄影：Jez Timms，采用 CC0 1.0 授权；来源与许可链接见下方。示例使用英文模板生成，中文版本尚未测试。展示的示例不会随输入实时变化。

</details>

<a id="3d-miniature-worlds"></a>

### 3D 微缩世界

将喜爱的地点转成紧凑的三维风格景观模型，搭配雕塑地形、玻璃感水体与柔和工作室光线。

[AILesson ↗](https://ailesson.io/zh/prompts/recipes/turn-photos-into-3d-miniature-worlds) · [English prompt](prompts/3d-miniature-worlds.md) · [中文提示词](prompts/zh-CN/3d-miniature-worlds.md)

<details>
<summary>展开提示词</summary>

```text
将上传照片转化为3D 微缩世界。

必须保留的元素：{{subject}}
配色与氛围：{{palette}}

将照片地点转成放在一块薄圆角矩形地形底座上的精致三维微缩景观。船屋仍在左侧湖岸，森林在其后，山脊位于更远处，湖面朝右前方展开。明确改用略高的四分之三视角，让完整微缩底座可见，同时保留上述景物关系。远景收束为同一底座上的紧凑雕塑山体，地形采用光滑哑光陶瓷感，树木归纳为简化体积，青绿湖水像带可见边缘的玻璃水体，建筑边缘轻微倒角。完整模型居中，四周保留充足干净工作室空间，下方有柔和接触阴影。无分散漂浮小岛、剖面标签、小人、额外建筑、玩具包装、文字或过强景深虚化。输出宽度至少 1400 像素的横向图片。这是三维风格概念插画，不是可复原或打印的模型。

以上传照片作为景物参考。仅输出完整作品，不含对比拼图、水印或标牌文字。
```

上传照片并描述需要保留的元素。示例摄影：Rafael Peier，采用 Unsplash License 授权；来源与许可链接见下方。示例使用英文模板生成，中文版本尚未测试。展示的示例不会随输入实时变化。 展示结果还经过一次清理编辑，以简化形体并移除屋顶文字。

</details>

## 示例与使用说明

图片通过 AILesson CDN 加载，仓库不保存图片副本，离线克隆不包含图片。固定内容链接不会自动跟随上游换图；更新数据后需重新生成 README。

[data/prompts.json](data/prompts.json) 保留实际输入、生成提示词、参考图关联、修订、后处理与已知偏差。生成图片是位图示例；三维、玻璃和版画风格也不提供可编辑模型或生产图纸。

## 参与贡献

欢迎改进提示词、补充风格和修订翻译。请阅读 [贡献指南](CONTRIBUTING.md) 与 [行为准则](CODE_OF_CONDUCT.md)。

## 许可与图片署名

提示词、文档和脚本使用 [MIT License](LICENSE)。第三方参考照片保留各自的 Unsplash License 或 CC0 条款，不被重新授权为 MIT。生成示例中的 AILesson 原创贡献按 MIT 提供，以其可授予的权利为限；原照片的适用条款仍需遵守。逐项来源与风格参考见 [IMAGE_CREDITS.md](IMAGE_CREDITS.md)。

---

[AILesson](https://ailesson.io/zh) · [Image prompts](https://ailesson.io/zh/prompts/types/image) · [Icon prompts](https://github.com/ailessonio/icon-prompts)
