# Generation Prompt and QA

## Pre-generation QA

Run this gate only after Material Casting and before image generation.

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
  tonal_coverage_preserved: true
  motion_topology_preserved: true
  gravity_preserved: true
  attention_focus_preserved: true
  carrier_physical_matches_source: true
  unwanted_beautification: false
  hero_gate_respected: true
  casting_requirements_met: true
  color_treatment_gate_respected: true
  treatment_compatibility_preserved: true
  casting_function_diversity_preserved: true
  carrier_literal_image_copy: false
  carrier_preservation_passed: true
  image_complexity_classified: true
  density_strategy_matches_complexity: true
  complete_floral_layering_present: true
  object_translation_complete: true
  literal_nonfloral_object_present: false
  source_color_emotion_correspondence_passed: true
```

```yaml
carrier_preservation_qa:
  level_1_carriers_preserved: true
  wrapper_preserved: true
  backboard_preserved: true
  carrier_substitution_detected: false
  environment_replaced_by_foliage: false
  environment_replaced_by_flowers: false
  environment_primary_carrier_preserved: true
  environment_support_share_within_limit: true
  environment_support_distributed_below_main_focus: true
  environment_support_occludes_main_focus: false
```

Also enforce these derived checks:

- Every Level 1 item has a carrier or a deliberate negative-space treatment.
- Every locked Level 1 carrier appears explicitly in the final prompt with a selected material from its permitted carrier category. A locked wrapper or backboard remains visibly present and retains its assigned visual-area responsibility.
- Material Casting and Floral Identity must not replace a locked wrapper or backboard with foliage, flowers, branches, or another carrier category. The literal-image-copy guard removes recognizable imagery from the carrier surface; it never removes the carrier itself.
- When `environment_support.enabled: true`, preserve wrapper/backboard as the primary environment carrier while allowing separately cast Level 2 auxiliary plants to echo the environment. Their combined visible botanical area is at most 20%; they are dispersed below the main focus and never cross in front of or obscure its silhouette. `environment_replaced_by_foliage: false` prohibits replacement, not all botanical support.
- Important highlight, midtone, and shadow layers each have a justified carrier; a meaningful midtone is not collapsed into shadow.
- Focus count, attention weight, scale relation, density, and direction agree across Decoder, Structure, and Casting.
- Low-area, high-attention information becomes one clear Hero plus at most one or two supports, not many equal small accents.
- A Hero is present only when Focus Architecture and the Hero Gate require it. `single_focus` and `dual_focus` with `focus_attention >= 4` enter Hero Candidate Selection; `multi_focus`, `distributed_focus`, and `environment_dominant` are not collapsed into an arbitrary single large flower.
- A required Hero has the highest visual attention through justified scale, color, shape, isolation, position, material, texture, or contrast. It is not automatically the largest flower and is not fragmented into many equivalent medium flowers.
- Strong motion affects the whole bouquet rather than a single decorative element.
- The prompt states whether movement departs from an origin or is drawn toward a destination. `centripetal` never becomes `radial_outward`; `falling` never becomes upward growth; `floating` never becomes grounded.
- Gravity state and destination agree with the silhouette, center of gravity, component posture, and gaps.
- The whole bouquet is not inverted merely to express `falling`, `sinking`, or `centripetal`. Keep the base/tie below the floral body by default and carry downward or inward motion through internal arcs, cascading postures, density, scale, and converging negative space. Suspend or invert only when suspension itself is Level 1.
- Every Level 1 wrapper, backboard, or special-material carrier retains the source's relevant material, hardness, opacity, surface, and geometry.
- Every selected material satisfies its assigned function, morphology, scale, texture, hardness, and physical identity. Motion and atmosphere use line or atmosphere materials where those fit better than ordinary flower heads.
- Natural color is used when sufficient. Every non-natural treatment has a source-derived gate reason, a stated base color, treatment, secondary color when needed, distribution, and intensity.
- A treatment with tolerance below 3 is replaced by a more compatible material, reassigned to an appropriate non-floral carrier, or simplified to natural color. Treatment must not conceal required texture unless coating is itself the target physical identity.
- Safe-flower repetition is allowed only when morphology and semantic fit justify it and no clearly better candidate exists. High-impact or luxury materials are likewise rejected when they add no visual function.
- Material count increases only when a new material adds a distinct visual function; diversity means function diversity, not species count.
- `extreme_minimal` is accepted only when all strict Decoder criteria are present. A plain background, one person, or one object alone is not enough. If the evidence is mixed or uncertain, classify as `non_minimal`.
- An `extreme_minimal` source may remain one Hero Flower plus zero or one restrained supporting group. A `non_minimal` source must contain one or two floral Hero/anchor flowers, two to four functional supporting groups, purposeful filler flower and/or greenery, and perceptible front/middle/back layers. A sparse “single flower + wrapper” result for `non_minimal` fails QA.
- When the overall Hero is non-floral, required floral anchors remain subordinate; density repair must not steal attention from a locked wrapper, branch, ribbon, or special-material Hero.
- The bouquet should preserve roughly 80% of the source's important color relationship and emotional character. Treat this as a perceptual target, not literal pixel-area matching or permission to copy objects.
- Every Level 1 or important Level 2 non-floral object has a complete `object_translation` record. Its color, material, texture, form, and emotion are mapped to floral carriers in that priority order.
- No clothing, fabric item, accessory, headwear, utensil, furniture, or other everyday prop survives as a recognizable entity, miniature, silhouette, or wearable object. No direct object symbol has survived without passing the object-decomposition rule.
- Inspect every Level 1 environment or object assigned to wrapper, backboard, or special material. Fail QA if it survives as a recognizable photograph, illustration, scenic print, pasted image, decal, projection, or screened reproduction on that carrier. Translate its color, material, space, structure, and motion properties instead.
- Conditional Typography and source-justified symbolic graphics may remain as visual texture, but they must not become a loophole for reconstructing the source image or a recognizable environment/object depiction.
- Typography is absent unless it is Level 1 or important Level 2; when allowed, it stays on its assigned carrier and preserves visual character and rhythm without adding unrelated copy or logos.
- Do not upgrade childlike, awkward, rough, cheap, casual, strange, uneasy, plain, or handmade source qualities into polished, romantic, fashion, editorial, or gothic styling unless the image itself supports that style.
- The design remains legible when imagined on pure white; it does not need a colored or scenic background.
- If cases were retrieved, every specific material and form is independently justified by the source image. `case_template_copied` must be false.
- Creative deviations remain at or below 10% and do not alter a protected field.

If the result is merely a conventional bouquet in the image's colors, fail QA. Return to the earliest faulty stage, rebuild downstream decisions, and run QA again.

If any locked Level 1 carrier is missing, substituted, or demoted until it no longer carries its assigned visual information, fail `carrier_preservation_qa` and rewrite the Generation Prompt once. Preserve the Decoder, Carrier Assignment, Bouquet Structure, and Casting decisions; this repair is prompt assembly only, not permission to recast or re-decode.

## Prompt assembly

Do not use the archived PRD, raw case cards, case images, case IDs, retrieval tags, or a long analysis transcript as the image prompt. After the output identity and design anchor, compile the production instructions in this binding order:

1. **A. Locked Carrier** — instantiate every locked Level 1 wrapper, backboard, flower, branch, leaf/grass, ribbon, special material, or negative-space carrier with its assigned role and physical attributes.
2. **B. Bouquet Structure** — apply complexity class, density strategy, silhouette, focus/space architecture, motion topology, gravity, floral role plan, front/middle/back depth, and presentation orientation without changing the locked carriers.
3. **C. Selected Floral Materials** — add only the botanical materials selected within their permitted carrier categories and satisfy the role counts required by the density strategy.
4. **D. Color Treatment** — apply per-material base color, treatment, secondary color, distribution, intensity, and retained texture after carrier and material identity are fixed.
5. **E. Accent** — place small accents, conditional typography, and source-justified linear or symbolic texture on their assigned carriers.
6. **F. QA** — restate pure-white output constraints, carrier preservation, literal-copy exclusions, and other negative constraints.

Use this contract, replacing brackets with the current design:

```text
Create exactly one complete, standalone artistic floral arrangement, fully visible from topmost element to the base/tie, visually centered with clean white breathing room on all sides.

Design anchor: [generation_anchor derived only from the input image].

A. Locked carriers: [list every Level 1 `visual_priority_ref`, its locked carrier, the concrete material selected only from that carrier category, assigned visual role, physical attributes, visibility, and required area responsibility]. Instantiate wrapper and backboard carriers now, before any botanical material. Do not omit, substitute, or visually demote them. If `carrier_override_allowed` is not explicitly true in the upstream Decoder, no cross-category replacement is permitted.

B. Bouquet structure: [image complexity class and minimal/complete density strategy], [silhouette, height, width, density, center of gravity, asymmetry, focus count], [one or two floral Hero/anchor roles and two to four supporting groups when non-minimal], [purposeful filler/greenery], [explicit front, middle, and back layers]. Preserve [focus architecture and attention weights, space architecture, scale relation, negative-space behavior]. Keep the base/tie below the floral body by default. Express motion through the internal topology of wrappers, stems, branches, heads, density, scale, and gaps. Use a suspended or inverted presentation only when suspension itself is a Level 1 visual mechanism. Do not reduce a non-minimal source to a single flower plus wrapper.

C. Selected floral materials: [state whether the Hero Gate requires an overall Hero; name each floral Hero or subordinate anchor, role, attention relationship, morphology, scale, texture, hardness, and position], [two to four functional supporting groups when non-minimal], [purposeful filler/greenery], [ensemble], [floral accent], [structure], [atmosphere], [motion]. Supporting groups are role-based clusters, not a species quota. If `environment_support.enabled: true`, identify its separately cast Level 2 auxiliary plants, keep their combined visible botanical area at or below 20%, distribute them below the main focus, and prohibit foreground overlap that obscures the main-focus silhouette. Use each selected material only for its assigned botanical carrier and visual function—not for prestige, species variety, literal copying, or replacement of a locked non-floral carrier.

D. Color treatment: [for every materially important selection, state base color, treatment, secondary color if used, distribution, intensity, and how natural petal/leaf/material texture remains visible]. When the Color Treatment Gate is false, explicitly retain natural color. When true, describe the treatment's spatial behavior rather than reducing it to a generic color adjective. Apply treatment only after carrier and material selection; treatment cannot change carrier category.

E. Accent: [small color accent, conditional typography, source-justified symbolic graphics, and thin linear materials]. For every important non-floral source object, state its extracted color/material/texture/form/emotion and the floral carrier that receives each property; never name or instantiate the original entity. Keep each accent on its assigned carrier. Typography is off by default; if and only if it is Level 1 or important Level 2, preserve stroke character, density, direction, and layout rhythm without reproducing full wording. Otherwise require no text.

F. QA and output constraints: confirm that every locked Level 1 carrier remains visible and performs its assigned role; wrapper and backboard have not been replaced by foliage or flowers; any enabled environment-support plants stay within the 20% cap, remain dispersed below the main focus, and do not obscure it; density strategy and front/middle/back layering match image complexity; important color relationships and emotional character remain about 80% perceptually aligned; palette tonal coverage, focus, motion, gravity, physical DNA, and style fidelity remain intact. Carrier abstraction: translate every Level 1 environment or object into color, material, texture, form, emotion, space, structure, and motion properties. Do not print, paste, illustrate, project, screen, reproduce, miniaturize, or rebuild a recognizable source scene or object on any carrier. Conditional typography and source-justified symbolic graphics may appear only as abstract visual texture, never as a reconstruction of the source image. Preserve the source's actual refinement level; do not beautify it without visual evidence.

Present it as a clean isolated studio product image on an absolute uniform pure-white #FFFFFF background. No gradient and no off-white, gray, colored, transparent, or scenic background. At most a very faint natural contact shadow directly beneath the bouquet, with no floor or scene impression.

Hard exclusions: exactly one bouquet; no second arrangement; no cropped tip, edge, stem, base, or wrapping; no person; no face; no body; no hand; no hand-held bouquet; no vase or furniture; no room, wall, floor, table, outdoor setting, landscape, sky, sea, grassland, or environmental scene; no literal prop copied from the source; no recognizable clothing, scarf, fabric object, accessory, headwear, hat, utensil, furniture, or other everyday object; no miniature or silhouette reconstruction of a source prop; no carrier-mounted photograph or illustration; no scenic printed wrapper or backboard; no pasted image, decal, projection, or screen reproduction; no reference-image inset, collage, split screen, border, frame, moodboard, or before/after layout; no ungrounded text, random wording, caption, label, watermark, or signature; no brand; no logo. Allow typography only under the conditional rule above and only on its assigned bouquet carrier.
```

The source image may be supplied to the image-generation tool as a reference input. `reference_image: false` means the source must not appear inside the generated output.

## Output-only delivery check

After generation, inspect only the candidate output against these hard constraints:

- exactly one complete bouquet;
- all extremities and the base/tie are visible;
- background pixels read as uniform pure white `#FFFFFF`, apart from an optional extremely faint contact shadow;
- no human, hand, vase, furniture, environment, scene, reference inset, collage, ungrounded text, or logo;
- no Level 1 environment or object appears as a recognizable photograph, illustration, scenic print, pasted image, decal, projection, or screened reproduction on a wrapper, backboard, or special material;
- every locked Level 1 carrier is visibly present in its assigned category and still carries its intended visual information; wrapper and backboard have not been replaced by foliage or flowers;
- if environment support is enabled, wrapper/backboard remains primary and auxiliary plants occupy no more than 20% of visible botanical area, read as dispersed accents below the main focus, and never obscure it;
- complexity and density agree: non-minimal work has one or two floral Hero/anchor roles, two to four functional supporting groups, purposeful filler/greenery, and readable front/middle/back depth; extreme-minimal work remains deliberately sparse;
- no clothing, fabric item, accessory, headwear, utensil, furniture, or everyday prop appears literally; each important source object is perceptible only through its translated color, material, texture, form, or emotional effect;
- allowed typography, if any, is confined to its assigned carrier and carries visual rhythm rather than unrelated content;
- the source-derived palette relationship and tonal coverage, focus/space and attention hierarchy, motion topology and gravity, carrier physical attributes, Casting function hierarchy, material morphology, per-material color treatment, and style fidelity remain perceptible in the bouquet itself;
- a required Hero is visually unmistakable without becoming a pile of equivalent medium flowers; when no Hero is required, the original distributed or environment-dominant attention remains intact;
- no unmotivated luxury material, habitual safe-flower choice, incompatible treatment, or treatment overuse is visible.

This is a delivery gate, not a new design stage. If a locked Level 1 carrier is missing or substituted, rewrite the Generation Prompt once with the missing carrier named first, keeping Decoder, Carrier Assignment, Bouquet Structure, and Casting unchanged. For any other hard-constraint failure, regenerate once with a focused correction naming the failure. If the underlying design translation fails, return to the relevant Decoder stage and rebuild; never repair it by copying a case.
