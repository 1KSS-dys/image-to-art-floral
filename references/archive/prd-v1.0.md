# 图片 → 艺术花艺生成 Skill｜需求文档

**版本：V1.0**  
**产品形态：图片视觉解码 + 花艺设计决策 + 图像生成 Skill**

## 一、产品定义

用户上传一张任意图片，Skill 先理解图片的视觉核心，再将其中的**色彩关系、焦点、空间、动势、材质、形态与情绪**重新组织为一束新的艺术花艺，最终输出一张**纯白背景下的完整花艺成品图**。

核心原则只有一句：

> **不是把图片“配成花”，而是把图片的视觉语言“翻译成花艺”。**

因此，系统不追求复刻图片中的人物、物体或具体构图，也不能简单执行“蓝色图片→蓝色花”“海边图片→加贝壳”“音乐图片→加音符”。最终作品需要让人能够感受到它与原图属于同一个视觉世界，但花束本身必须是一件独立成立的设计作品。

---

## 二、产品目标

Skill 需要解决三个核心问题。

第一，**图片为什么会给人现在这种感觉**。系统需要识别真正决定画面气质的因素，而不是罗列“图中有什么”。

第二，**这些视觉信息应该由花艺中的谁承担**。花、枝叶、包装、背板、丝带、特殊材料和留白拥有不同职责，不能默认所有内容都交给花朵表现。

第三，**重新设计一束花，而不是复刻已有参考花束**。Case Library 只用于学习转译逻辑，不能成为模板库。

---

## 三、输入要求

V1 仅需要用户输入：

**1 张参考图片。**

支持人物摄影、穿搭、风景、绘画、插画、电影海报、专辑封面、品牌视觉、抽象图像、幻想/赛博图、群像、产品视觉等。

V1 暂不要求用户主动选择花材、预算、用途、尺寸或花艺流派。系统应根据图片自主完成基础设计。

---

## 四、输出要求

最终只输出 **1 束完整艺术花艺的成品图**。

### 强制生成规范

```yaml
output:
  background: "#FFFFFF"
  bouquet_count: 1
  full_bouquet_visible: true
  human: false
  hand: false
  environment: false
  furniture: false
  text: false
  logo: false
  reference_image: false
```

最终背景必须为**绝对纯白色 #FFFFFF**，不得出现房间、墙面、桌面、沙发、户外景观、渐变、彩色背景或参考图拼贴。

花束主体完整展示，整体居中或视觉居中，四周保留合理白色留白。允许极轻微自然接触阴影，但不能形成场景感。

特别规定：

> **原图中的天空、海洋、房间、夜色、草地等环境信息，只能被翻译进花艺本体，不得依赖最终背景表达。**

例如海洋可以变成包装的层叠波浪结构，天空可以变成背板，裙摆可以变成大面积柔性包装，但最终背景依旧保持纯白。

---

# 五、核心生成流程

整个 Skill 强制按照以下顺序运行：

```text
输入图片
↓
1. Semantic Core｜视觉核心
↓
2. Visual Priority｜信息优先级
↓
3. Palette｜颜色关系
↓
4. Focus + Space｜焦点与空间
↓
5. Motion + Physical DNA｜动势与物理气质
↓
6. Carrier Assignment｜花艺载体分配
↓
7. Bouquet Structure｜花束结构
↓
8. Material Casting｜花材选角
↓
9. QA
↓
纯白背景成品生成
```

严禁跳过前面的视觉解码，直接根据颜色选择花材。

---

# 六、图片视觉解码规则

## 6.1 Semantic Core｜视觉核心

系统首先必须用一句话回答：

> **这张图真正让人记住的是什么？**

该句应表达视觉关系或感受，原则上控制在 25 个汉字左右。

正确：

> 裙摆和草一起被风吹开。

> 冷光从深蓝夜色里缓慢浮起。

> 两股能量在黑暗中互相撕扯。

错误：

> 一个女孩穿白裙在草地奔跑，背景有蓝天。

后者只是对象描述，没有完成视觉解码。

---

## 6.2 Visual Priority｜信息优先级

系统将图片信息分成三层：

```yaml
visual_priority:
  level_1: []
  level_2: []
  discard: []
```

`Level 1` 是必须进入最终花艺的核心信息，建议控制在 3–5 项；`Level 2` 可以被抽象转译；`Discard` 原则上舍弃。

人脸细节、Logo、精确文字、对象数量、微小背景物件等通常应进入 Discard，除非它们本身就是图片的核心视觉机制。

---

## 6.3 Palette｜颜色关系

系统不能只提取主色，而必须判断颜色是**如何组织的**。

```yaml
palette:
  mode: ""
  dominant_environment: ""
  secondary: []
  accent: []
  accent_behavior: ""
  purity: 1-5
  relationship: ""
```

`mode` 限定为：

```text
monochrome
dominant_single_accent
dominant_multi_accent
layered_gradient
organized_multicolor
opposition
radial_energy
```

关键规则：

颜色面积不等于视觉权重。例如一个面积很小的橙色瞳孔，也可能比大面积黑白更重要。

单色图片优先利用**明度、饱和度、花型、尺寸、材质**建立丰富度，不得为了丰富随意加入新色。

多色图片必须识别颜色关系。例如多色可能是“涂鸦跳点”“红色舞台里的群像”“中心爆发”或“红青对抗”，不能统一理解成彩虹。

---

## 6.4 Focus + Space｜焦点与空间

```yaml
focus:
  architecture: ""
  main_focus: ""
  secondary_focus: ""

space:
  architecture: ""
  density: ""
  negative_space: ""
  scale_relation: ""
```

`focus.architecture`：

```text
single_focus
dual_focus
multi_focus
distributed_focus
environment_dominant
```

`space.architecture`：

```text
central
layered
wrapped
landscape
scattered
radial
```

系统需要判断：焦点有几个、谁包围谁、主体与环境谁更大、画面是否依赖留白、前后层级如何。

原图中的空间关系必须进入花艺结构。例如：

> 海包住人物 → 包装包住花。

> 人很小、风景很大 → 场景载体面积大于代表人物的花。

> 多个物体漂浮 → 花材之间必须留下距离。

---

## 6.5 Motion + Physical DNA｜动势与物理气质

```yaml
motion:
  primary: ""
  secondary: ""
  direction: ""
  strength: 1-5

physical_dna:
  hardness: ""
  gravity: ""
  material_identity: []
```

`motion.primary`：

```text
static
upward
downward
directional
flowing
wave
floating
radial_explosion
mechanical_extension
collision
```

`hardness`：

```text
soft
flexible
structured
hard
mechanical
```

`gravity`：

```text
weightless
light
neutral
heavy
sinking
```

`material_identity` 可选择：

```text
watery
misty
textile
papery
matte
glossy
metallic
dry
organic
synthetic
rough
```

强动势必须影响**整个花束**。例如风不能只靠一根草表达，而应同时改变包装展开方向、枝材方向、花头姿态、重心、外轮廓与留白。

同样颜色也可能对应不同材质语言。例如“泳池蓝”可以是湿润、透明、流动，“梦境蓝”则可能是雾化、失重和微光，因此不得建立固定“蓝色模板”。

---

# 七、花艺载体分配

系统完成视觉解码后，需要决定“哪一种视觉信息由谁来演”。

```yaml
scene_carrier:
  flower: ""
  branch: ""
  leaf_or_grass: ""
  wrapper: ""
  backboard: ""
  ribbon: ""
  special_material: ""
  negative_space: ""
```

载体默认职责如下：

| 载体 | 主要职责 |
|---|---|
| Flower | 主体、焦点、生命核心 |
| Branch | 速度、轨迹、方向、骨架 |
| Leaf / Grass | 风、地面、自然层、线性动势 |
| Wrapper | 水体、海浪、裙摆、布料、包裹、大色块 |
| Backboard | 天空、夜色、海报、平面环境 |
| Ribbon | 尾迹、收束、小面积延伸色 |
| Special Material | 云、雾、金属、透明、非植物质感 |
| Negative Space | 漂浮、孤独、辽阔、机械结构间隔 |

**花不一定是主角。**

包装、背板、枝材甚至留白，都可能成为花艺的核心设计载体。

---

# 八、具象对象转译规则

任何具体对象出现时，先执行：

```text
Object
↓
Color
Shape
Material
Motion
Semantic Role
↓
保留最高价值属性
↓
映射到花艺载体
```

系统优先进行**视觉同构**，而不是模型复制。

例如：

> 鸟 → 翼状植物结构。

> 裙摆 → 飞扬的柔性包装。

> 眼睛 → 圆形焦点 + 放射结构。

> 云 → 棉絮、纤维、雾状材料。

> 赛车 → 速度、锐角、硬质材料和推进方向。

只有当某个实体同时高度符合原图的**颜色、形态、语义与世界观**时，才允许直接作为实体进入花艺，例如某些水果、果实或植物。

---

# 九、人物图片分类

人物图必须先判断其主要价值属于哪一类：

```text
atmosphere_character
action_character
lifestyle_character
structural_character
group_character
```

`Atmosphere Character` 优先翻译色彩、光线和气质；`Action Character` 优先翻译动作、方向、服装动态；`Lifestyle Character` 优先翻译穿搭、材质、季节与生活方式；`Structural Character` 优先翻译机械、骨架、装甲和能量结构；`Group Character` 优先翻译多人之间的关系、节奏和多焦点结构。

禁止“一人对应一朵花”。

---

# 十、花束结构生成

系统必须先建立花束骨架，再选择具体花材。

```yaml
bouquet_structure:
  silhouette: ""
  height: low / medium / high
  width: narrow / medium / wide
  density: low / medium / high
  center_of_gravity: ""
  asymmetry: 1-5
  focus_count: ""
```

`silhouette` 可以选择：

```text
central_compact
vertical_sculptural
directional
landscape
wrapped
radial
floating
group_ensemble
asymmetric_editorial
```

禁止系统无依据回退到：

> 对称圆形花束 + 中央主花 + 绿叶填满 + 外围包装。

结构必须由输入图片本身决定。

---

# 十一、花材 Casting

具体花材是整个流程的最后一步。

```yaml
casting:
  hero: []
  support: []
  ensemble: []
  accent: []
  structure: []
  atmosphere: []
  motion: []
```

花材选择固定遵循：

> **功能 → 形态 → 材质 → 颜色 → 具体花材**

而不是：

> 蓝色图片 → 找蓝色花。

其中：

`Hero` 是主要视觉角色；`Support` 负责连接主体；`Ensemble` 负责数量与场域；`Accent` 是异常点或特殊角色；`Structure` 负责骨架；`Atmosphere` 负责雾、光、环境感；`Motion` 负责风、速度、垂坠和爆发。

系统应把花材理解成“演员”，而不仅是颜色素材。

---

# 十二、有限再创作

Skill 允许进行少量审美优化，但不得改变原图核心视觉逻辑。

```yaml
creative_deviation:
  allowed: true
  max_weight: "10%"
```

允许增加少量过渡色、必要结构材料或低权重辅助花材。

不得改变：

- Semantic Core；
- Palette Mode；
- Focus Architecture；
- Motion；
- Spatial Architecture；
- 核心情绪。

---

# 十三、全局禁止规则

系统必须遵守以下禁止项：

1. **禁止对象硬复制。** 不得看到音乐就加音符、看到海就加贝壳、看到赛车就放赛车模型、看到鸟就塞鸟模型。
2. **禁止只按颜色配花。** 颜色必须与空间、焦点、动势、材质、形态共同决定设计。
3. **禁止默认传统花束模板。** 输入需要景观、漂浮、风、机械、爆发时，必须真正改变结构。
4. **禁止无依据增加元素。** 不得为了“丰富”随机添加珍珠、蝴蝶结、卡通、羽毛、金属、新颜色或装饰。
5. **禁止依赖背景表达主题。** 最终始终为纯白背景，所有原图视觉信息都必须进入花艺本体。
6. **禁止复刻 Case Library。** 案例只能帮助理解规则，不得直接复制其中花材、包装或构图。

---

# 十四、QA 自检

生成前必须完成一次内部检查。

重点检查以下内容：

```yaml
qa:
  semantic_core_preserved: true
  palette_relationship_preserved: true
  motion_preserved: true
  carrier_assignment_clear: true
  bouquet_structure_non_template: true
  unnecessary_objects: false
  unnecessary_colors: false
  background_is_pure_white: true
  full_bouquet_visible: true
```

如果生成方案只是“换了图片配色的普通花束”，视为失败，需要重新设计一次。

如果方案严重依赖最终背景才能看出原图主题，也视为失败。

---

# 十五、Case Library 使用方式

现有 CASE-001～CASE-021 作为**经验库**保存，不直接进入主规则。

正常输入优先使用本 Skill 的 Decoder。

仅当遇到难以判断的图片时，允许检索 1–3 个相似 CASE，用来参考：

> 视觉关系如何抽象、场景如何分配给载体、动势如何进入结构。

禁止复制案例中的具体花材组合、包装样式和配色比例。

---

# 十六、Skill 核心 Schema

```yaml
semantic_core: ""

visual_priority:
  level_1: []
  level_2: []
  discard: []

palette:
  mode: ""
  dominant_environment: ""
  secondary: []
  accent: []
  accent_behavior: ""
  purity: 1-5
  relationship: ""

focus:
  architecture: ""
  main_focus: ""
  secondary_focus: ""

space:
  architecture: ""
  density: ""
  negative_space: ""
  scale_relation: ""

motion:
  primary: ""
  secondary: ""
  direction: ""
  strength: 1-5

physical_dna:
  hardness: ""
  gravity: ""
  material_identity: []

scene_carrier:
  flower: ""
  branch: ""
  leaf_or_grass: ""
  wrapper: ""
  backboard: ""
  ribbon: ""
  special_material: ""
  negative_space: ""

bouquet_structure:
  silhouette: ""
  height: ""
  width: ""
  density: ""
  center_of_gravity: ""
  asymmetry: 1-5
  focus_count: ""

casting:
  hero: []
  support: []
  ensemble: []
  accent: []
  structure: []
  atmosphere: []
  motion: []

creative_deviation:
  allowed: true
  max_weight: "10%"

output_constraints:
  background: "#FFFFFF"
  bouquet_count: 1
  full_bouquet_visible: true
  environment: false
  human: false
  hand: false
  text: false
  reference_image: false

generation_anchor: ""
```

---

# 十七、最终成功标准

一张合格的最终生成图应达到：

> **看得出它“来自这张图”，但找不到它在机械复制这张图里的什么东西。**

用户应该感受到相同的色彩逻辑、情绪、方向、空间与材质气质，而不是看到一堆从原图直接搬来的符号。

最终所有视觉判断，都要被浓缩进：

> **一束完整、独立、有艺术性的花艺 + 纯白背景。**

**Skill 总纲：**

> **先理解图片为什么成立，再把它的颜色关系、空间、焦点、动势、材质和情绪重新分配给花、枝、包装、背板、特殊材料与留白，最后生成一束在纯白背景下独立成立的艺术花艺。**