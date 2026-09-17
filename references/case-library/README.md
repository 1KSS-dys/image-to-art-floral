# Case Library Runtime Guide

This is a compact experience library derived from the standard CASE-001–CASE-021 package. It is subordinate to PRD / Core Rules V1.2 and the Decoder Schema.

## Default behavior

- Do not load this directory in normal runs.
- Decode Semantic Core, Visual Priority, Palette, Focus/Space, and Motion/Physical DNA first.
- Retrieve only when unresolved ambiguity would change carrier assignment or bouquet structure.
- Return 1–3 cards at most.
- Reuse transferable rules and carrier-role reasoning only. Never reuse a specific flower combination, wrapper form, decoration, composition, or color ratio as a template.

## Retrieval surfaces

`case-index.tsv` exposes three independent evidence surfaces:

1. `retrieval_tags`: mechanism-level labels, not single-color similarity.
2. Visual features: `palette_mode`, the legacy index field `motion_primary` (queried through the current `--motion-topology` alias), `hardness`, `gravity`, `material_identity`, and `visual_features`.
3. Structural features: `focus_architecture`, `space_architecture`, `silhouette`, `density`, and scale/spacing cues embedded in the card.

Index values are normalized to the Decoder Schema enums for retrieval. The selected source card remains unchanged and retains its original descriptive vocabulary.

Use `scripts/retrieve_cases.py` to score the compact index and load only the selected YAML cards. The script's output is reasoning evidence; it must never be copied into the generation prompt.

## Contents

- `case-index.tsv`: lightweight searchable index.
- `cards/case-NNN.yaml`: the 21 concise experience cards.
- Historical `source.jpg` and `bouquet.jpg` files are intentionally excluded from the Skill runtime. Some are low-resolution crops or composite images containing reference thumbnails or text; they are unsuitable as generation templates.

The complete standard source package remains the provenance source. The archived PRD and this library's source files are maintenance references only, not default prompt material.
