# Image to Art Floral V1.3

将一张参考图片的色彩关系、焦点、空间、运动、物理材质与情绪，重构为纯白背景下的一束完整艺术花艺。

本仓库是可直接作为 Codex Skill 使用的 V1.3 发布包。V1.3 在完整保留 V1.2 Carrier Lock、Floral Material Library、Color Treatment、Hero Casting、案例检索与回归基准的基础上，只新增图片复杂度判断、花束密度策略和非花艺物件转译规则。

## 什么时候调用

当用户提供或明确指向一张图片，并表达下列或相近意图时，调用 `image-to-art-floral`：

- “生成花束”
- “根据图片生成花艺”
- “把这张图片变成花艺”
- “用这张图设计一束花”
- “继续生成花艺”
- “将参考图转译为艺术花束”

如果当前对话中没有可用图片，先请用户上传一张参考图。

以下请求不应调用本 Skill：普通花束搭配、花材识别、养护建议，以及没有参考图片的纯文字花艺文案。

自动触发依据位于 [`SKILL.md`](SKILL.md) 的 `description`。`agents/openai.yaml` 保持 `allow_implicit_invocation: true`，因此用户不需要显式输入 `$image-to-art-floral`。

## 核心流程

```text
输入图片
→ Semantic Core
→ Visual Priority
→ Palette
→ Focus / Space
→ Motion / Physical DNA
→ Carrier Assignment
→ Bouquet Structure
→ Material Casting
→ QA
→ Image Generation
```

规则优先级：

```text
PRD / Core Rules V1.3
> Decoder Schema
> Case Library
```

Material Casting 必须服从已经锁定的 Carrier：

```text
Carrier
→ Function
→ Morphology
→ Scale
→ Texture
→ Material / Physical DNA
→ Specific Material
→ Color Treatment
```

案例库只在关键判断不确定时检索最相关的 1–3 个案例，不作为花材、包装或构图模板。

## 输出硬约束

- 只生成一束完整花艺；
- 背景为纯白 `#FFFFFF`；
- 花束顶部、边缘、包装与底部绑扎全部可见；
- 无人物、手持、花瓶或环境场景；
- 不出现参考图拼贴、照片贴图、Logo、水印或无依据文字；
- 不把参考图中的人物、建筑、物件等直接复制为模型或包装印刷；
- Typography 仅在其本身属于重要视觉信息时作为纹理使用；
- 包装或背板一旦被锁定为 Level-1 Carrier，不得被花朵、叶材或枝材替换。
- 非花艺物件必须先拆解为颜色、材质、纹理、形态与情绪，再转译为花材、包装或装饰语言；不得把衣物、饰品、帽子、器物、家具或其他生活物件直接塞入花束。
- 除非参考图被严格判定为 `extreme_minimal`，花束必须包含 Hero、Supporting、Filler / Greenery 与前中后三层空间关系，避免退化为“单花 + 包装纸”。

## V1.3 更新

本次是 Casting 与生成约束的最小升级，没有重构 Decoder 主链路。

- `image_complexity`：严格区分 `extreme_minimal` 与 `non_minimal`；不确定时按 `non_minimal` 处理。
- `density_strategy`：非极简图必须形成 1–2 个 Hero、2–4 组 Supporting、Filler / Greenery 与前中后三层。
- `object_translation`：所有 Level-1 或重要 Level-2 非花艺物件在 Carrier Assignment 前完成视觉属性拆解。
- 转译优先级固定为：颜色 → 材质 / 纹理 → 形态 → 情绪；保留原物实体为最低优先级且默认禁止。
- Generation Prompt 与 QA 新增复杂度、密度、转译完整性和 Literal Prop 检查。
- 新增围巾 / 布料、头饰 / 配饰、斗笠 / 竹编物件三组跨题材 Hard Case。

V1.2 的材料库、Color Treatment、Carrier Lock、Case Library、检索逻辑与回归资产均保持不变。

## 目录结构

```text
image-to-art-floral/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── material-library/
│   ├── flowers.yaml
│   ├── foliage.yaml
│   ├── branches.yaml
│   ├── packaging.yaml
│   ├── special-materials.yaml
│   └── color-treatment.yaml
├── references/
│   ├── decoder-schema.md
│   ├── casting-rules.md
│   ├── generation-prompt-and-qa.md
│   ├── object-translation-hard-cases.md
│   ├── regression-v1.1.md
│   ├── regression-v1.2.md
│   ├── case-library/
│   └── archive/
├── scripts/
│   ├── retrieve_cases.py
│   └── validate_skill.py
└── assets/
    ├── benchmarks/
    └── regression/
```

`references/archive/` 仅用于保留历史规则，不参与正常运行上下文。

## 安装

将仓库目录放入 Codex 的 Skills 目录，并保持目录名为 `image-to-art-floral`：

```text
~/.codex/skills/image-to-art-floral/
```

也可以从 GitHub 仓库根目录安装为名为 `image-to-art-floral` 的 Skill。安装后重新打开 Codex 或刷新 Skills 列表。

## 使用示例

自然语言自动调用：

```text
根据这张图片生成花艺
```

显式调用：

```text
Use $image-to-art-floral to turn this image into one artistic floral arrangement.
```

## 验证

在仓库根目录运行：

```bash
python3 scripts/validate_skill.py .
```

校验内容包括入口文件、Schema、材料库、案例索引、Carrier Lock、Generation Prompt 顺序、图片复杂度、花束密度、物件转译及核心输出约束。

## 版本

当前发布：**V1.3**。V1.2 的 Carrier Preservation Hotfix、环境辅助植物上限、材料库与 Color Treatment 继续生效。
