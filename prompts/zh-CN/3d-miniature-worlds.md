# 3D 微缩世界

将喜爱的地点转成紧凑的三维风格景观模型，搭配雕塑地形、玻璃感水体与柔和工作室光线。

## 变量

- `subject` — 必须保留的元素: 左侧湖岸的红顶船屋、松林、棱角分明的山峰、蓝色湖面倒影，以及前景低矮灌木。
- `palette` — 配色与氛围: 瓷白山峰、低饱和常绿树、半透明青绿湖水与一点陶土红屋顶，搭配暖灰白工作室背景。

## 提示词

```text
将上传照片转化为3D 微缩世界。

必须保留的元素：{{subject}}
配色与氛围：{{palette}}

将照片地点转成放在一块薄圆角矩形地形底座上的精致三维微缩景观。船屋仍在左侧湖岸，森林在其后，山脊位于更远处，湖面朝右前方展开。明确改用略高的四分之三视角，让完整微缩底座可见，同时保留上述景物关系。远景收束为同一底座上的紧凑雕塑山体，地形采用光滑哑光陶瓷感，树木归纳为简化体积，青绿湖水像带可见边缘的玻璃水体，建筑边缘轻微倒角。完整模型居中，四周保留充足干净工作室空间，下方有柔和接触阴影。无分散漂浮小岛、剖面标签、小人、额外建筑、玩具包装、文字或过强景深虚化。输出宽度至少 1400 像素的横向图片。这是三维风格概念插画，不是可复原或打印的模型。

以上传照片作为景物参考。仅输出完整作品，不含对比拼图、水印或标牌文字。
```

上传照片并描述需要保留的元素。示例摄影：Rafael Peier，采用 Unsplash License 授权；来源与许可链接见下方。示例使用英文模板生成，中文版本尚未测试。展示的示例不会随输入实时变化。 展示结果还经过一次清理编辑，以简化形体并移除屋顶文字。

## 示例

| 原图 | 效果图 |
| :---: | :---: |
| <a href="https://ailesson.io/content-assets/sha256/ea/66/ea66fe51fe702cd080905fc1954c0dba73eab85b0489b9b2ac4a5a1ee7c2658c.png"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/ea/66/ea66fe51fe702cd080905fc1954c0dba73eab85b0489b9b2ac4a5a1ee7c2658c.png" alt="蓝色山湖左岸的红顶船屋，周围有松林与前景灌木。" width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/8e/ad/8eaddfc7837080402cb0f8111802e4cb64cc4285a1310770110b939ae09a6242.png"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/8e/ad/8eaddfc7837080402cb0f8111802e4cb64cc4285a1310770110b939ae09a6242.png" alt="紧凑的三维风格山湖模型，含青绿湖水、瓷白山体、绿树和陶土红顶船屋。" width="320"></a> |

[Unsplash / Rafael Peier](https://unsplash.com/photos/mountain-lake-with-a-boathouse-and-surrounding-forest-I_XRy-z8m8k) · [Unsplash License](https://unsplash.com/license)

- `subject`: 左侧湖岸的红顶船屋、松林、棱角分明的山峰、蓝色湖面倒影，以及前景低矮灌木。
- `palette`: 瓷白山峰、低饱和常绿树、半透明青绿湖水与一点陶土红屋顶，搭配暖灰白工作室背景。

场景有意重新取景并收束到微缩底座。第二次编辑去掉屋顶文字，并简化山体与树木。船屋和森林仍可辨，但比例与远处地形被压缩。

## 检查结果

- 对照主要景物的左右关系；相机角度与比例有意改变。
- 检查景物关系、完整底座与清晰水体边缘，避免分散漂浮碎块或新增建筑。
- 分享前放大检查细节，清除意外生成的文字。

[AILesson](https://ailesson.io/zh/prompts/recipes/turn-photos-into-3d-miniature-worlds) · [Image credits](../../IMAGE_CREDITS.md) · [Gallery](../../README.zh-CN.md)
