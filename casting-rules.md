# Floral Casting Rules V1.3

Use this file only after Bouquet Structure is fixed. V1.3 preserves the V1.2 library, Hero, Color Treatment, and Carrier Lock logic. It adds only complexity-bound density and non-floral object translation; it must not revise Semantic Core, Palette, Focus, Space, Motion, Carrier Assignment, or Bouquet Structure to justify a preferred flower.

## Carrier Lock comes first

Carrier Assignment is authoritative over Material Casting. Before forming any candidate set, read the Level 1 `carrier_lock` records from the Decoder. A locked carrier narrows the library search; visual strength, novelty, Hero Score, Floral Identity, or color-treatment potential can rank materials only inside that permitted carrier category.

Do not search all libraries for the visually strongest material. Use this boundary:

| Locked carrier | Allowed source |
|---|---|
| `wrapper` | `packaging.yaml` wrapper variants only |
| `backboard` | `packaging.yaml` paper/backboard variants, plus explicitly backboard-capable rigid sheet or acrylic variants |
| `flower` | `flowers.yaml` only |
| `branch` | `branches.yaml`, or a line material explicitly assigned as branch by the Decoder |
| `leaf_or_grass` | `foliage.yaml` and grass entries only |
| `ribbon` | ribbon/textile variants in `packaging.yaml` only |
| `special_material` | `special-materials.yaml` only |
| `negative_space` | no material search; preserve the gap |

Never substitute foliage, flowers, or branches for a locked wrapper/backboard. Never substitute a flower mass or giant leaf for Level 1 environment assigned to packaging. Cross-category substitution is legal only when the upstream Decoder explicitly set `carrier_override_allowed: true`; Casting cannot set or infer that flag.

## Casting order

Always cast in this order:

```text
Locked Carrier
→ Function inside that carrier
→ Morphology
→ Scale
→ Texture
→ Material / Physical DNA
→ Specific Material
→ Color Treatment
```

Visual Function Diversity matters more than species count. Three to five materials are enough when they cover the required Hero, Support, Motion, Structure, Atmosphere, or carrier functions. Never add a species merely to make the result look more luxurious or varied.

## Complexity-to-density gate

Read `image_complexity.class` and `bouquet_structure.density_strategy` before forming floral candidates.

| Complexity | Required floral structure |
|---|---|
| `extreme_minimal` | One Hero Flower, with zero or one restrained supporting group. Filler is optional. Keep deliberate negative space. |
| `non_minimal` | One or two floral Hero/anchor flowers, two to four functional supporting groups, purposeful filler flower and/or greenery, and explicit front/middle/back depth. |

`extreme_minimal` is valid only when all strict Decoder criteria are met. Uncertainty defaults to `non_minimal`. A plain background or one photographed subject does not by itself justify a sparse bouquet.

Supporting groups are functional clusters—such as color transition, motion, secondary focus, atmosphere, or depth—not a species quota. One material may serve more than one group when its placement clearly separates the functions. Filler/greenery must add depth, rhythm, transition, or texture; do not create a generic filler wall. In a complete bouquet, place foreground accents or low filler in front, the main floral mass and focal anchors in the middle, and line/structure/atmosphere behind, unless the decoded source justifies a different but still explicit three-layer relation.

The density gate does not replace the Hero Gate. If the overall Hero is a locked wrapper, branch, ribbon, or special material, treat the one or two floral Hero/anchor flowers as subordinate botanical anchors. They satisfy floral completeness without stealing highest attention or changing the decoded focus architecture.

## Non-floral object translation gate

Before candidate search, read the completed `object_translation` records. Casting receives only extracted properties and mapped carrier roles—not the source entity as a candidate.

Use this priority:

```text
Color correspondence
→ Material / texture correspondence
→ Form / directional correspondence
→ Emotional correspondence
→ Literal entity preservation (prohibited for ordinary props)
```

Map color to natural or treated flowers and packaging; material and texture to wrapper, ribbon, special material, surface, or fine botanical texture; form to morphology, grouping, branches, and line direction; and emotion to overall refinement, density, rhythm, and style. Never cast clothing, a fabric item, accessory, headwear, utensil, furniture, or another everyday prop as itself, a miniature, or a recognizable silhouette. Typography and source-justified symbolic graphics may remain only under their existing conditional rules.

## Load the material library

Translate the casting requirements into visual attributes inside each locked carrier before reading candidates. Then read only the file permitted by the lock under `material-library/`:

- `flowers.yaml` for floral Hero, support, event, and botanical atmosphere candidates;
- `foliage.yaml` for planes, blades, skeletons, wind, and structural leaves;
- `branches.yaml` for trajectories, gravity, arcs, and rigid or flexible lines;
- `packaging.yaml` for wrapper/backboard materials that must match Carrier Physical Attributes;
- `special-materials.yaml` for transparent, atmospheric, industrial, reflective, mesh, or wire behavior;
- `color-treatment.yaml` only after natural-color sufficiency has been judged.

Material families list explicit `variants`. Select and name the variant whose physical attributes match the already assigned carrier; never treat a role tag such as `environment`, `structure`, or `hero_material` as permission to cross the carrier boundary. Role tags rank candidates only after carrier filtering.

## Floral Identity preservation

Floral Identity means the complete work still has an intentional botanical focus or floral organization. It does not require plants to occupy the largest area. When an environment-dominant design locks Level 1 information to wrapper, backboard, paper, film, textile, or special material, those carriers may remain the primary visual area while a small number of plants establishes the floral relationship.

Do not increase “flower feeling” by replacing locked paper, film, textile, wrapper, or backboard with foliage. Floral Identity must never override Carrier Lock.

### Environment co-carriage

`environment_replaced_by_foliage: false` does not mean “remove all foliage.” When the Decoder enables `environment_support`, keep the locked wrapper/backboard as the Level 1 primary environment carrier and cast a small Level 2 botanical echo inside each auxiliary carrier's own library category.

The combined auxiliary plants must remain at or below 20% of total visible botanical area. Distribute them as separated accents below the main focus; they may sit behind its lower edge but must not cross in front of or obscure its silhouette. They provide transition, depth, and material continuity—not a second focus, filler wall, or replacement environment. If the limit, placement, or visibility rule fails, reduce or remove auxiliary plants without changing the primary carrier.

## Focus Architecture and Hero policy

Not every bouquet needs a Hero Flower or even a floral Hero.

| Focus architecture | Hero policy |
|---|---|
| `single_focus` | Usually one unmistakable Hero material. |
| `dual_focus` | Two coordinated or opposed Hero materials are allowed. |
| `multi_focus` | Use two to four distinct focal roles; do not force one largest material. |
| `distributed_focus` | Usually omit an absolute single Hero; preserve distributed attention. |
| `environment_dominant` | Weaken or omit the Hero when the carrier field is the visual core. |

```yaml
hero_gate:
  focus_attention: 1-5
  visual_centrality: 1-5
  contrast_requirement: 1-5
  scale_requirement: 1-5
  hero_required: false
```

Set `hero_required: true` when `focus_attention >= 4` and Focus Architecture is `single_focus` or `dual_focus`. Otherwise decide from the architecture without inventing a Hero.

A Hero is the material with the highest visual attention, not automatically the physically largest flower. It may win through scale, color, shape, isolation, position, material, texture, or contrast. It may be a flower, orchid stem, anthurium plane, long structural branch, wrapper plane, or special material when that carrier performs the Main Focus.

## Hero Candidate Selection

When the Hero Gate is open:

1. State the Main Focus's visual function.
2. State required morphology.
3. State required scale.
4. State required texture, hardness, and material identity.
5. Select three to five candidates from the material category allowed by the Main Focus carrier lock.
6. Judge whether each candidate's natural palette is sufficient.
7. If not, run the Color Treatment Gate and compatibility check.
8. Score every candidate using the same evidence.
9. Select the highest score inside the locked carrier category and record why it wins. Do not default to an orchid or another prestige material because the image feels “high-end.”

```yaml
hero_score:
  morphology_fit: 0-5
  scale_fit: 0-5
  semantic_fit: 0-5
  palette_fit: 0-5
  material_identity_fit: 0-5
  color_treatment_potential: 0-5
  novelty: 0-3
  repetition_penalty: 0-3
```

Calculate:

```text
Hero Score = morphology_fit × 2
           + semantic_fit × 2
           + scale_fit
           + palette_fit
           + material_identity_fit
           + color_treatment_potential
           + novelty
           - repetition_penalty
```

Morphology and semantic fit have the highest weight. `novelty` can break a close functional tie; it must never rescue a poorly fitting material. Price, luxury status, and popularity are not score inputs.

## Color Treatment Gate

Natural color is the default. Use `material-library/color-treatment.yaml` only when the gate has a source-derived reason. For each treated material, record base color, treatment, secondary color, distribution, and intensity. Preserve natural surface and petal texture unless the assigned physical identity specifically requires coating.

Check the selected material's `treatment_tolerance`. A requested treatment below 3 must trigger this fallback order:

1. choose a morphologically similar material with stronger treatment tolerance;
2. move the color behavior to an assigned wrapper, foliage, or special-material carrier;
3. use natural color if the palette relationship still survives.

Treatment is not decoration. One coherent treatment may be stronger than several unrelated effects. Set `treatment_overuse: true` when treatment appears without a visual task, conceals required texture, or is repeated across materials only to make the bouquet look advanced.

## Safe Flower Repetition Penalty

Roses, carnations, ordinary ranunculus, hydrangea, chrysanthemums, and small daisies remain valid. They receive no penalty when their morphology and semantic role are the best match.

After provisional selection, check:

1. Is a high-frequency safe material being used again?
2. Does its morphology and semantic fit actually lead the candidate set?
3. Does the Material Library contain a clearly better functional candidate?

Set `safe_flower_repetition.detected: true` only when the choice appears habitual. Record the repeated material and set `better_candidate_available: true` only when another candidate scores higher on morphology/semantic fit. Re-cast once from the candidate stage; do not ban the safe material or substitute a luxury flower automatically.

Likewise, set `unnecessary_luxury_materials: true` when high-impact materials were selected without functional justification. A distributed childlike cluster may not need a large lily; a hard falling structure may be led by leaves, branches, or special material rather than flowers.

## Casting QA

```yaml
casting_qa:
  hero_strength: 1-5
  morphology_fit: 1-5
  color_treatment_fit: 1-5
  function_diversity: 1-5
  safe_flower_repetition:
    detected: false
  repeated_materials: []
  better_candidate_available: false
  unnecessary_material_complexity: false
  unnecessary_luxury_materials: false
  treatment_overuse: false
  density_strategy_match: true
  front_mid_back_depth: true
  object_translation_complete: true
  literal_nonfloral_object_present: false
```

Fail Casting QA when a candidate crosses a locked carrier boundary, a required Hero is fragmented into many equivalent medium flowers, a chosen material cannot perform its assigned morphology/physical role, a treatment is incompatible or unmotivated, a clearly better in-category candidate is ignored in favor of habit, or material count rises without adding a visual function. Also fail when a `non_minimal` source becomes a sparse single-flower-plus-wrapper result, any required supporting group or spatial layer is missing, an `extreme_minimal` source is needlessly crowded, an object-translation record is incomplete, or a recognizable non-floral source prop survives. Re-cast once from requirements; never revise the upstream Decoder to make a favored material fit.
