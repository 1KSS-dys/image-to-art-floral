# Decoder Schema

This is the operational schema for PRD / Core Rules V1.2. The PRD overrides this file if they ever conflict. Complete fields in order; do not use later-stage choices to rewrite earlier observations merely to justify a preferred bouquet. V1.2 leaves Sections 1–7 unchanged and upgrades only Material Casting.

## 1. Semantic Core

Write one short sentence, preferably about 25 Chinese characters, answering: “What truly makes this image memorable?” Describe a visual relationship, action, or feeling—not an object inventory.

```yaml
semantic_core: ""
```

## 2. Visual Priority

Keep Level 1 to roughly 3–5 indispensable mechanisms. Level 2 may be abstracted. Discard faces, logos, exact text, object counts, and small background items unless they are themselves the central visual mechanism.

```yaml
visual_priority:
  level_1: []
  level_2: []
  discard: []
```

## 3. Palette

Describe how color is organized, not just which colors appear. Area does not equal visual weight. In monochrome images, create richness through value, saturation, form, scale, and material rather than introducing unmotivated colors.

```yaml
palette:
  mode: ""
  dominant_environment: ""
  secondary: []
  accent: []
  accent_behavior: ""
  purity: 1-5
  relationship: ""
  tonal_coverage:
    highlight: ""
    midtone: ""
    shadow: ""
```

After decoding hue and accent behavior, verify that every important highlight, midtone, and shadow layer has a reasonable carrier. Do not mechanically copy area ratios, and do not require flowers to carry every layer; wrapper, backboard, or special material may do so. Never collapse a meaningful pale or mid-value environment into only its darkest color plus accents.

Allowed `mode` values:

```text
monochrome
dominant_single_accent
dominant_multi_accent
layered_gradient
organized_multicolor
opposition
radial_energy
```

## 4. Focus and Space

Preserve focus count, enclosure, scale relations, depth, and meaningful gaps. Translate environmental scale into the bouquet body: if environment outweighs subject, scene carriers must outweigh subject flowers.

```yaml
focus:
  architecture: ""
  main_focus: ""
  secondary_focus: ""
  attention_weight:
    main: 1-5
    secondary: 1-5

space:
  architecture: ""
  density: ""
  negative_space: ""
  scale_relation: ""
```

Allowed `focus.architecture` values:

```text
single_focus
dual_focus
multi_focus
distributed_focus
environment_dominant
```

Allowed `space.architecture` values:

```text
central
layered
wrapped
landscape
scattered
radial
```

## 5. Motion and Physical DNA

Strong motion changes the whole bouquet: wrapper direction, branches, flower-head posture, center of gravity, silhouette, and negative space. Never express wind, speed, or falling with one token stem or ribbon alone.

```yaml
motion:
  topology: ""
  primary_direction: ""
  secondary_direction: ""
  strength: 1-5

gravity:
  state: ""
  destination: ""

physical_dna:
  hardness: ""
  material_identity: []
```

Allowed `motion.topology` values:

```text
static
wave
flowing
floating
linear
radial_outward
centripetal
mechanical_extension
collision
```

Allowed `primary_direction` and `secondary_direction` values:

```text
up
down
left
right
upper_left
upper_right
lower_left
lower_right
center
none
```

Allowed `gravity.state` values: `weightless`, `floating`, `neutral`, `grounded`, `falling`, `sinking`, `heavy`.

Allowed `gravity.destination` values: `none`, `up`, `down`, `center`, `lower_center`, `upper_center`, `edge`.

Before Bouquet Structure, explicitly answer whether elements move out from somewhere or are drawn toward a destination. Never translate `centripetal` as `radial_outward`, `falling` as `upward_growth`, or `floating` as grounded support. Motion topology, direction, gravity state, and gravity destination must agree with the silhouette, center of gravity, flower posture, and negative space.

Motion semantics do not automatically determine the bouquet's presentation orientation. `falling`, `sinking`, and `centripetal` must not by themselves flip the whole bouquet, move the tie/cut stems above the floral body, or turn the arrangement into a suspended tassel. Keep the bound base below the floral body by default unless suspension itself is a Level 1 visual mechanism and a physically justified carrier carries it.

For a downward or centripetal reading with a normal lower base, build the motion inside the bouquet: begin from a higher or wider origin; let branches, leaves, and structural materials arc outward or upward before bending down and inward; decrease scale or density toward the destination; narrow the negative spaces toward `lower_center`; place the strongest focal weight low; and use drooping heads or cascading side lines where justified. This is an internal path toward a destination, not an instruction to invert the product.

Use a suspended or inverted presentation only as a last-resort translation when the source's suspension mechanism is Level 1. If used, keep the hanging point subordinate, avoid a dominant crown of exposed cut stems, and prevent broom- or tassel-like silhouettes.

Allowed `hardness` values: `soft`, `flexible`, `structured`, `hard`, `mechanical`.

Allowed `material_identity` values: `watery`, `misty`, `textile`, `papery`, `matte`, `glossy`, `metallic`, `dry`, `organic`, `synthetic`, `rough`.

### Object and character decoding

For a concrete object, decompose `Object → Color / Shape / Material / Motion / Semantic Role`, retain only its highest-value properties, then map those properties to floral carriers. Use direct entities only when their color, form, semantics, and world all independently fit the source.

Classify a person image before translation as one of:

```text
atmosphere_character
action_character
lifestyle_character
structural_character
group_character
```

Translate the class's governing mechanism. Never map one person to one flower.

## 6. Carrier Assignment

Assign each Level 1 and useful Level 2 mechanism to a carrier. Empty strings are valid when a carrier has no job; do not invent a role to fill every field.

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

carrier_lock:
  level_1:
    - visual_priority_ref: ""
      carrier: ""
      priority: level_1
      locked: true
      carrier_override_allowed: false

environment_support:
  enabled: false
  primary_environment_carrier: ""
  auxiliary_botanical_carriers: []
  max_share_of_visible_botanical_area: "20%"
  distribution: dispersed
  placement: below_main_focus
  main_focus_occlusion: false
```

Default responsibilities are not templates:

| Carrier | Typical responsibility |
|---|---|
| Flower | subject, focus, living core |
| Branch | speed, trajectory, direction, skeleton |
| Leaf / grass | wind, ground, natural layer, linear motion |
| Wrapper | water, waves, cloth, enclosure, large color field |
| Backboard | sky, night, poster plane, flat environment |
| Ribbon | trail, gathering, minor color extension |
| Special material | cloud, mist, metal, transparency, non-botanical identity |
| Negative space | floating, isolation, vastness, mechanical intervals |

Flowers need not be the main carrier. Environmental information must live in the bouquet body, never in the final background.

Every Level 1 `scene_carrier` assignment must create one `carrier_lock.level_1` record. `locked` defaults to `true`. Material Casting may select a concrete material only inside the locked carrier category; it may not change the carrier. Set `carrier_override_allowed: true` only when the Decoder itself finds an explicit source-derived reason before Bouquet Structure. Casting may never create that permission for its own convenience.

| Locked carrier | Casting search scope |
|---|---|
| `wrapper` | Packaging/wrapper materials only. |
| `backboard` | Backboard, paper, cardstock, acrylic, or rigid-sheet materials only. |
| `flower` | Flower materials only. |
| `branch` | Branch or line materials only. |
| `leaf_or_grass` | Foliage or grass materials only. |
| `ribbon` | Ribbon/textile packaging materials only. |
| `special_material` | Special-material library only. |
| `negative_space` | Spatial treatment only; never replace it with a physical filler. |

Locked `wrapper` must not become foliage, flower, or branch. Locked `backboard` must not become a giant leaf or flower mass. If `focus.architecture: environment_dominant` and wrapper/backboard holds Level 1 environment information, that packaging carrier must remain visibly present and carry the assigned area/weight in the final bouquet.

When the source environment has organic texture, depth, or material continuity that packaging alone would make flat, set `environment_support.enabled: true`. The locked wrapper/backboard remains the Level 1 primary environment carrier. Assign any auxiliary plant separately as a Level 2 `leaf_or_grass`, `branch`, or `flower` carrier and cast it only inside that category. Auxiliary plants may echo the environment but must occupy no more than 20% of the total visible botanical area, appear as dispersed accents below the main focus, and never cross in front of or obscure the main-focus silhouette. This is co-carriage, not carrier substitution; do not enable it when the source does not justify botanical environment support.

For every carrier that holds Level 1 information, continue from role to physical behavior. Fill only the relevant blocks; do not invent properties for unused carriers.

```yaml
carrier_physical:
  wrapper:
    material: ""
    hardness: ""
    opacity: ""
    surface: ""
    geometry: ""
  backboard:
    material: ""
    hardness: ""
    opacity: ""
    surface: ""
    geometry: ""
  special_material:
    material: ""
    hardness: ""
    opacity: ""
    surface: ""
    geometry: ""
```

Recommended values:

- `material`: `paper`, `cardstock`, `fabric`, `organza`, `film`, `plastic`, `metallic`, `natural_fiber`, `mesh`, `other`
- `hardness`: `soft`, `flexible`, `structured`, `hard`, `mechanical`
- `opacity`: `transparent`, `translucent`, `semi_opaque`, `opaque`
- `surface`: `matte`, `glossy`, `rough`, `smooth`, `textured`, `printed`, `handmade`
- `geometry`: `flowing`, `folded`, `planar`, `layered`, `wrinkled`, `angular`, `curved`, `fragmented`

Carrier assignment is incomplete when a Level 1 role is named but its source-defining hardness, opacity, surface, or geometry is omitted. A flat matte cardstock field must not drift into soft flowing organza merely because both can act as wrapper.

## 7. Bouquet Structure

Build the skeleton before naming materials.

```yaml
bouquet_structure:
  silhouette: ""
  height: low | medium | high
  width: narrow | medium | wide
  density: low | medium | high
  center_of_gravity: ""
  asymmetry: 1-5
  focus_count: ""
```

Allowed `silhouette` values:

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

Do not default to a symmetric round bouquet with one central hero, green filler, and outer wrapping. Every structural choice must trace back to the source decoder.

## 8. Material Casting

Cast by `Function → Morphology → Scale → Texture → Material / Physical DNA → Color Treatment → Specific Material`. Bouquet Structure is already fixed; casting must not rewrite any upstream Decoder field.

```yaml
hero_gate:
  focus_attention: 1-5
  visual_centrality: 1-5
  contrast_requirement: 1-5
  scale_requirement: 1-5
  hero_required: false

color_treatment_gate:
  required: false
  reason: ""

casting:
  requirements:
    hero:
      required: false
      function: ""
      morphology:
        scale: ""
        openness: ""
        petal_density: ""
        silhouette: ""
      texture: ""
      hardness: ""
      attention_weight: 1-5
    support:
      function: ""
      morphology: []
    structure:
      line_character: ""
      hardness: ""
    atmosphere:
      density: ""
      texture: ""

  candidate_materials:
    hero: []
    support: []
    structure: []
    atmosphere: []

  selected_materials:
    hero:
      material_id: ""
      reason: ""
      color_design:
        base_color: ""
        treatment: natural
        secondary_color: ""
        distribution: uniform
        intensity: low
    support: []
    ensemble: []
    accent: []
    structure: []
    atmosphere: []
    motion: []

  qa:
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
```

Follow [Floral Casting Rules V1.2](casting-rules.md). Form three to five Hero candidates only when the Hero Gate requires one, and select from the relevant files in `material-library/`. Non-floral carriers are first-class candidates. Visual Function Diversity matters more than Species Count Diversity; three to five total materials may be enough.

Judge area weight separately from attention weight. For `single_focus` or `dual_focus`, low-area/high-attention information normally needs one unmistakable Hero role plus at most one or two supports. Hero means highest visual attention and may win through scale, color, shape, isolation, position, material, texture, or contrast; it is not automatically the physically largest flower. Preserve `multi_focus`, `distributed_focus`, and `environment_dominant` architectures instead of forcing a single Hero.

Treat materials as performers with roles. Avoid random pearls, bows, feathers, cartoons, metal, new colors, luxury flowers, or ornaments added only for richness. Roses, carnations, ordinary ranunculus, hydrangea, chrysanthemums, and small daisies remain valid only when their morphology and semantics win the candidate comparison; never replace them merely for novelty.

## Conditional typography

```yaml
typography:
  default: false
  allow_when_visual_core: true
```

Keep typography off by default. Allow it only when handwriting, calligraphy, graffiti, poster type, or printed type is Level 1 or important Level 2 visual information. Assign it to wrapper, backboard, printed material, or handwritten texture and preserve character, stroke weight, density, direction, and layout rhythm rather than complete wording. Never introduce unrelated copy, random English, decorative fake text, brands, or logos. Typography is a narrow exception and does not authorize literal objects.

## Controlled creative deviation

```yaml
creative_deviation:
  allowed: true
  max_weight: "10%"
```

Minor transition colors or supporting materials are allowed only when structurally necessary. Never alter the Semantic Core, Palette Mode, Focus Architecture, Motion, Spatial Architecture, or core emotion.

## Output contract carried into generation

```yaml
output_constraints:
  background: "#FFFFFF"
  bouquet_count: 1
  full_bouquet_visible: true
  environment: false
  furniture: false
  human: false
  hand: false
  logo: false
  reference_image: false

generation_anchor: ""
```

Write `generation_anchor` as one compact sentence binding Semantic Core, color relationship, focus/space, motion, physical DNA, carrier hierarchy, and structure. It is a design summary, not a raw image prompt.
