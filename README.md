# Image to Art Floral V1.2

将一张参考图片的色彩关系、焦点、空间、运动、物理材质与情绪，重构为纯白背景下的一束完整艺术花艺。

本仓库是可直接作为 Codex Skill 使用的 V1.2 发布包，包含 Carrier Lock、Floral Material Library、Color Treatment、Hero Casting、QA、案例检索与回归基准。

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
PRD / Core Rules V1.2
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

校验内容包括入口文件、Schema、材料库、案例索引、Carrier Lock、Generation Prompt 顺序及核心输出约束。

## 版本

当前发布：**V1.2**，包含后续 Carrier Preservation Hotfix 与环境辅助植物上限规则。
