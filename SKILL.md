---
name: image-to-art-floral
description: Translate one reference image's palette relationships, focus, space, motion, physical DNA, and emotion into one complete artistic floral arrangement on pure white. Use when the user provides or refers to an image and asks “生成花束”, “根据图片生成花艺”, “把这张图片变成花艺”, “继续生成花艺”, or expresses an equivalent image-to-floral intent. If no image is available, ask the user to attach one. Do not use for ordinary bouquet styling without a reference image, flower identification, or text-only floral copy.
---

# Image to Art Floral

Translate visual language into floral design. Do not decorate an image with flowers and do not reproduce its objects.

## Authority and scope

Resolve every conflict in this order:

1. PRD / Core Rules V1.2 are authoritative.
2. [Decoder Schema](references/decoder-schema.md) operationalizes the PRD.
3. The case library is optional retrieval evidence only.

The input is exactly one reference image. If none is available, ask the user to attach one. Do not ask for flower preferences, budget, use, size, or style unless the user independently adds such constraints.

Before acting, read [Decoder Schema](references/decoder-schema.md), [Floral Casting Rules V1.2](references/casting-rules.md), and [Generation Prompt and QA](references/generation-prompt-and-qa.md) completely. Archived requirements, [V1.1 regression guidance](references/regression-v1.1.md), and [V1.2 Carrier Preservation regression](references/regression-v1.2.md) are for maintenance or evaluation only; do not load them in normal runs.

## Required workflow

Inspect the input image, then run this sequence without reordering or skipping stages:

```text
Input image
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

Keep the completed decoder record internal unless the user asks to see it. Never jump from detected colors to flower names. Determine structure before casting any specific material.

After Carrier Assignment, lock every Level 1 carrier before Bouquet Structure or Material Casting. Carrier Assignment outranks Material Casting: search only the material category permitted by each lock, and never substitute foliage, flowers, or branches for a locked wrapper/backboard unless `carrier_override_allowed: true` was explicitly set by the Decoder. A locked packaging carrier may be accompanied—but not replaced—by source-justified Level 2 botanical environment support: no more than 20% of total visible botanical area, dispersed below the main focus, and never crossing in front of or obscuring it. After Bouquet Structure is fixed, derive requirements inside each locked carrier, then use the V1.2 Casting Rules and relevant files under [material-library](material-library/) to select `Carrier → Function inside that carrier → Morphology → Scale → Texture → Material / Physical DNA → Specific Material → Color Treatment`. Natural color is the default; load [Color Treatment](material-library/color-treatment.yaml) only when its gate has a source-derived reason. Do not revise upstream Decoder decisions to justify a preferred material.

### Conditional case retrieval

Complete Semantic Core through Motion / Physical DNA before considering cases. Normal runs use no cases.

Retrieval is allowed only when ambiguity in a critical field would materially change carrier assignment or bouquet structure—for example, two plausible palette modes, focus/space architectures, or physical identities remain after inspecting the image. It is not justified merely because a case shares a color or subject.

When retrieval is justified:

1. Query [the retrieval script](scripts/retrieve_cases.py) with decoded categorical fields plus mechanism-level tags or visual features.
2. Request only 1–3 results. If no result clears the relevance threshold, continue from the Decoder alone.
3. Read only the returned cards. Transfer `key_rule`, abstraction logic, carrier-role logic, and structural reasoning.
4. Do not copy a case's flower combination, material list, wrapper form, decoration, composition, or color ratio. A case-specific choice may enter the design only when the input image independently justifies it.
5. Do not pass case cards, case images, retrieval tags, or case IDs into the image-generation prompt.

Example retrieval call:

```bash
python3 scripts/retrieve_cases.py \
  --palette-mode opposition \
  --focus-architecture dual_focus \
  --space-architecture scattered \
  --motion-topology collision \
  --hardness mechanical \
  --tag 红青对抗 --tag 黑色负空间 \
  --feature 两股能量互相穿刺 \
  --top-k 2
```

The compact index and cards live under [references/case-library](references/case-library/README.md). Historical images remain outside normal runtime context.

## Generation and delivery

After Material Casting, run every pre-generation QA gate in the reference. If any gate fails, revise the earliest failing design stage and re-run all downstream stages. A design that is merely a conventional bouquet recolored from the image automatically fails.

Build one concise generation prompt from the current image's decoder and final design only. Instantiate locked wrappers/backboards before describing plant materials. Use the input image as a visual reference for analysis, but explicitly forbid the reference image, collage, border, scene, and ungrounded text from appearing in the result. Typography remains off by default and is allowed only when it is itself Level 1 or important Level 2 visual information assigned to a physical carrier.

Invoke the available image-generation tool and create exactly one result. Then perform the output-only delivery check described in the QA reference. If a hard output constraint fails, regenerate with a focused correction; do not redesign from a case.

Unless the user asked for rationale or intermediate artifacts, deliver only the final generated image. Do not expose the decoder, retrieval output, or prompt by default.
