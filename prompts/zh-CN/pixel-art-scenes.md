# 像素艺术场景

用清晰像素簇、阶梯轮廓与紧凑配色重建风景，呈现经典游戏般的画面。

## 变量

- `subject` — 必须保留的元素: 左侧湖岸的红顶船屋、松林、棱角分明的山峰、蓝色湖面倒影，以及前景低矮灌木。
- `palette` — 配色与氛围: 紧凑的天蓝、深海军蓝、松绿、暖金配色，以少量陶土红屋顶点缀，傍晚前的午后。

## 提示词

```text
将上传照片转化为像素艺术场景。

必须保留的元素：{{subject}}
配色与氛围：{{palette}}

重绘为精心构图的十六位时代像素画。采用明显粗颗粒且一致的方形像素网格，如同以约 320 像素宽绘制后使用最近邻放大。用有意组织的像素簇、清晰阶梯状斜线与少量有序抖色塑造树木、山峰、屋顶和水面。以少量高对比像素让小船屋可辨认，远景细节比前景像素簇更简洁。无平滑笔触、抗锯齿边缘、照片马赛克、游戏界面、角色或文字。这是视觉目标，不承诺精确的索引色数量。

以上传照片为唯一视觉参考，保留相机视角、主要轮廓、相对位置与可辨认的主体。简化细节，不添加物件。仅输出成品画作，不输出对比拼图、样机或带框印刷品。保持原图横向宽高比，宽度至少 1400 像素。不含文字、字母、标志、签名或水印；省略照片中原有的标牌文字。
```

上传照片并描述需要保留的元素。示例摄影：Rafael Peier，采用 Unsplash License 授权；来源与许可链接见下方。示例使用英文模板生成，中文版本尚未测试。展示的示例不会随输入实时变化。

## 示例

| 原图 | 效果图 |
| :---: | :---: |
| <a href="https://ailesson.io/content-assets/sha256/ea/66/ea66fe51fe702cd080905fc1954c0dba73eab85b0489b9b2ac4a5a1ee7c2658c.png"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/ea/66/ea66fe51fe702cd080905fc1954c0dba73eab85b0489b9b2ac4a5a1ee7c2658c.png" alt="蓝色山湖左岸的红顶船屋，周围有松林与前景灌木。" width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/a6/17/a6178f488396fb2297a3b440e581581b3197ac30460f2cce4941e3bb8affd20d.png"><img src="https://ailesson.io/cdn-cgi/image/width=640,fit=scale-down,quality=82,format=auto,metadata=none/content-assets/sha256/a6/17/a6178f488396fb2297a3b440e581581b3197ac30460f2cce4941e3bb8affd20d.png" alt="左侧有红顶船屋、深色松树与金色前景灌木的像素山湖风景。" width="320"></a> |

[Unsplash / Rafael Peier](https://unsplash.com/photos/mountain-lake-with-a-boathouse-and-surrounding-forest-I_XRy-z8m8k) · [Unsplash License](https://unsplash.com/license)

- `subject`: 左侧湖岸的红顶船屋、松林、棱角分明的山峰、蓝色湖面倒影，以及前景低矮灌木。
- `palette`: 紧凑的天蓝、深海军蓝、松绿、暖金配色，以少量陶土红屋顶点缀，傍晚前的午后。

红顶、湖泊与山峰关系仍可辨认。成图具有粗颗粒像素簇和明显天空抖色，但船屋有所放大，也不是经过统一网格认证的游戏资产。

## 检查结果

- 对照上传照片，检查主要轮廓、视角与左右关系。
- 观察屋顶、山峰斜线与水面：像素簇应清晰可读，边缘保持利落。
- 分享前放大检查细节，清除意外生成的文字。

[AILesson](https://ailesson.io/zh/prompts/recipes/turn-photos-into-pixel-art-scenes) · [Image credits](../../IMAGE_CREDITS.md) · [Gallery](../../README.zh-CN.md)
