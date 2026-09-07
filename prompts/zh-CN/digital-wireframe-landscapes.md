# 数字线框地景

将风景重建为精细建筑网格线、安静暗色平面和少量发光焦点。

## 变量

- `subject` — 必须保留的元素: 向下延伸的金色草坡、左侧深绿树丛、中央附近的小海滩、右侧山坡村庄，以及宽阔海湾与远处岬角。
- `palette` — 配色与氛围: 深午夜蓝底上的冷白与浅青网格线，海岸线仅用少量电光青柠色点缀。

## 提示词

```text
将上传照片转化为数字线框地景。

必须保留的元素：{{subject}}
配色与氛围：{{palette}}

将风景重构为干净的未来建筑线框表现。用间距适中、结构连贯的三角地形网格顺着坡度描述山坡，房屋用简单细线体块表示。海湾保留为安静暗色平面，仅有少量长透视线。近处网格边稍亮稍粗，远处更细更暗，保留可辨认的岬角、海滩与山坡聚落。避免覆盖屏幕的均匀网格、随机激光涂鸦、浓重光雾、照片表面纹理或虚构摩天楼。几何形态是视觉转译，不是测绘地形或可提取的三维网格。无坐标轴、坐标值、标签、游戏界面、边框或文字。

以上传照片为唯一视觉参考，保留相机视角、主要轮廓、相对位置与可辨认的主体。简化细节，不添加物件。仅输出成品画作，不输出对比拼图、样机或带框印刷品。保持原图横向宽高比，宽度至少 1400 像素。不含文字、字母、标志、签名或水印；省略照片中原有的标牌文字。
```

上传照片并描述需要保留的元素。示例摄影：Leticia Golubov，采用 Unsplash License 授权；来源与许可链接见下方。示例使用英文模板生成，中文版本尚未测试。展示的示例不会随输入实时变化。

## 示例

| 原图 | 效果图 |
| :---: | :---: |
| <a href="https://ailesson.io/content-assets/sha256/60/b6/60b6c57cd35766a133979b111ca77b6af62573386e88ae4b6c0e834613a1aad4.png"><img src="https://ailesson.io/content-assets/sha256/60/b6/60b6c57cd35766a133979b111ca77b6af62573386e88ae4b6c0e834613a1aad4.png" alt="从金色田野俯瞰海湾，画面包含林木山坡、小海滩与山坡房屋。" width="320"></a> | <a href="https://ailesson.io/content-assets/sha256/78/6a/786a4f97a52e44c500a5a5ccabb7ccf71e1c179cb62485fdbee47e48eb4a05a9.png"><img src="https://ailesson.io/content-assets/sha256/78/6a/786a4f97a52e44c500a5a5ccabb7ccf71e1c179cb62485fdbee47e48eb4a05a9.png" alt="午夜蓝海岸风景，以青色三角网格表现地形，局部海岸为青柠色。" width="320"></a> |

[Unsplash / Leticia Golubov](https://unsplash.com/photos/coastal-village-nestled-in-a-valley-by-the-sea-v6mz1osBv0M) · [Unsplash License](https://unsplash.com/license)

- `subject`: 向下延伸的金色草坡、左侧深绿树丛、中央附近的小海滩、右侧山坡村庄，以及宽阔海湾与远处岬角。
- `palette`: 深午夜蓝底上的冷白与浅青网格线，海岸线仅用少量电光青柠色点缀。

海湾与聚落仍可辨，青柠色海岸点缀清楚。远处地形线较密且暗，网格只是示意，并非测绘结果。

## 检查结果

- 对照上传照片，检查主要轮廓、视角与左右关系。
- 检查海岸可辨认、坡度连贯、房屋可读，去掉任意网格或坐标文字。
- 分享前放大检查细节，清除意外生成的文字。

[AILesson](https://ailesson.io/zh/prompts/recipes/turn-photos-into-digital-wireframe-landscapes) · [Image credits](../../IMAGE_CREDITS.md) · [Gallery](../../README.zh-CN.md)
