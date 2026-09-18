#!/usr/bin/env python3
"""Validate PRD-critical structure, retrieval, prompt, and QA invariants."""

from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def read(path: Path) -> str:
    require(path.is_file(), f"missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8") if path.is_file() else ""


skill = read(ROOT / "SKILL.md")
schema = read(ROOT / "references" / "decoder-schema.md")
generation = read(ROOT / "references" / "generation-prompt-and-qa.md")
casting_rules = read(ROOT / "references" / "casting-rules.md")
object_hard_cases = read(ROOT / "references" / "object-translation-hard-cases.md")
regression = read(ROOT / "references" / "regression-v1.1.md")
regression_v12 = read(ROOT / "references" / "regression-v1.2.md")
index_path = ROOT / "references" / "case-library" / "case-index.tsv"
cards_root = ROOT / "references" / "case-library" / "cards"
benchmarks_root = ROOT / "assets" / "benchmarks" / "v1.1"
carrier_regression_fixture = ROOT / "assets" / "regression" / "v1.2" / "case03-reference.jpg"
carrier_regression_output = ROOT / "assets" / "regression" / "v1.2" / "case03-hotfix-output.png"
material_root = ROOT / "material-library"
material_paths = [
    material_root / "flowers.yaml",
    material_root / "foliage.yaml",
    material_root / "branches.yaml",
    material_root / "packaging.yaml",
    material_root / "special-materials.yaml",
]
color_treatment = read(material_root / "color-treatment.yaml")
material_texts = [read(path) for path in material_paths]

priority_markers = ["PRD / Core Rules V1.3 are authoritative", "Decoder Schema", "case library"]
positions = [skill.find(marker) for marker in priority_markers]
require(all(position >= 0 for position in positions), "authority priority is incomplete")
require(positions == sorted(positions), "authority priority is out of order")

flow = [
    "Semantic Core",
    "Visual Priority",
    "Palette",
    "Focus / Space",
    "Motion / Physical DNA",
    "Carrier Assignment",
    "Bouquet Structure",
    "Material Casting",
    "QA",
    "Image Generation",
]
cursor = -1
for stage in flow:
    cursor = skill.find(f"→ {stage}", cursor + 1)
    require(cursor >= 0, f"workflow stage missing or out of order: {stage}")

schema_fields = [
    "semantic_core:",
    "visual_priority:",
    "image_complexity:",
    "class: extreme_minimal | non_minimal",
    "density_strategy: minimal | complete",
    "palette:",
    "focus:",
    "attention_weight:",
    "space:",
    "motion:",
    "topology:",
    "primary_direction:",
    "secondary_direction:",
    "gravity:",
    "state:",
    "destination:",
    "physical_dna:",
    "object_translation:",
    "literal_entity_allowed: false",
    "scene_carrier:",
    "carrier_lock:",
    "visual_priority_ref:",
    "locked: true",
    "carrier_override_allowed: false",
    "environment_support:",
    "max_share_of_visible_botanical_area: \"20%\"",
    "placement: below_main_focus",
    "main_focus_occlusion: false",
    "carrier_physical:",
    "bouquet_structure:",
    "floral_role_plan:",
    "spatial_layers:",
    "hero_or_anchor_flowers:",
    "supporting_groups:",
    "filler_or_greenery:",
    "hero_gate:",
    "color_treatment_gate:",
    "casting:",
    "requirements:",
    "density_plan:",
    "hero_or_anchor_count:",
    "support_group_count:",
    "candidate_materials:",
    "selected_materials:",
    "floral_anchors:",
    "color_design:",
    "safe_flower_repetition:",
    "unnecessary_luxury_materials: false",
    "treatment_overuse: false",
    "density_strategy_match: true",
    "front_mid_back_depth: true",
    "object_translation_complete: true",
    "literal_nonfloral_object_present: false",
    "typography:",
    "allow_when_visual_core: true",
    "creative_deviation:",
    "output_constraints:",
    "generation_anchor:",
]
for field in schema_fields:
    require(field in schema, f"decoder field missing: {field}")

hard_prompt_terms = [
    "exactly one complete",
    "pure-white #FFFFFF",
    "no person",
    "no hand",
    "no room",
    "no reference-image inset",
    "no ungrounded text",
    "Allow typography only",
    "no logo",
]
for term in hard_prompt_terms:
    require(term in generation, f"generation hard constraint missing: {term}")

qa_fields = [
    "semantic_core_preserved: true",
    "palette_relationship_preserved: true",
    "motion_preserved: true",
    "carrier_assignment_clear: true",
    "bouquet_structure_non_template: true",
    "unnecessary_objects: false",
    "unnecessary_colors: false",
    "background_is_pure_white: true",
    "full_bouquet_visible: true",
    "tonal_coverage_preserved: true",
    "motion_topology_preserved: true",
    "gravity_preserved: true",
    "attention_focus_preserved: true",
    "carrier_physical_matches_source: true",
    "unwanted_beautification: false",
    "hero_gate_respected: true",
    "casting_requirements_met: true",
    "color_treatment_gate_respected: true",
    "treatment_compatibility_preserved: true",
    "casting_function_diversity_preserved: true",
    "carrier_literal_image_copy: false",
    "carrier_preservation_passed: true",
    "image_complexity_classified: true",
    "density_strategy_matches_complexity: true",
    "complete_floral_layering_present: true",
    "object_translation_complete: true",
    "literal_nonfloral_object_present: false",
    "source_color_emotion_correspondence_passed: true",
]
for field in qa_fields:
    require(field in generation, f"QA field missing: {field}")

for rule in [
    "centripetal` never becomes `radial_outward",
    "falling` never becomes upward growth",
    "floating` never becomes grounded",
    "not inverted merely to express",
    "base/tie below the floral body by default",
    "Suspend or invert only when suspension itself is Level 1",
]:
    require(rule in generation, f"motion guard missing: {rule}")

for rule in [
    "recognizable photograph, illustration, scenic print, pasted image, decal, projection, or screened reproduction",
    "Translate its color, material, space, structure, and motion properties instead",
    "must not become a loophole for reconstructing the source image",
    "no carrier-mounted photograph or illustration",
    "no scenic printed wrapper or backboard",
]:
    require(rule in generation, f"carrier literal-copy guard missing: {rule}")

for field in [
    "carrier_preservation_qa:",
    "level_1_carriers_preserved: true",
    "wrapper_preserved: true",
    "backboard_preserved: true",
    "carrier_substitution_detected: false",
    "environment_replaced_by_foliage: false",
    "environment_replaced_by_flowers: false",
    "environment_primary_carrier_preserved: true",
    "environment_support_share_within_limit: true",
    "environment_support_distributed_below_main_focus: true",
    "environment_support_occludes_main_focus: false",
]:
    require(field in generation, f"carrier preservation QA missing: {field}")

for rule in [
    "at most 20%",
    "dispersed below the main focus",
    "never cross in front of or obscure its silhouette",
    "prohibits replacement, not all botanical support",
]:
    require(rule in generation, f"environment-support generation rule missing: {rule}")

prompt_sections = [
    "A. Locked carriers:",
    "B. Bouquet structure:",
    "C. Selected floral materials:",
    "D. Color treatment:",
    "E. Accent:",
    "F. QA and output constraints:",
]
prompt_positions = [generation.find(section) for section in prompt_sections]
require(all(position >= 0 for position in prompt_positions), "carrier-first prompt sections are incomplete")
require(prompt_positions == sorted(prompt_positions), "carrier-first prompt sections are out of order")
require("rewrite the Generation Prompt once" in generation, "missing-carrier prompt rewrite rule is absent")
require("not permission to recast or re-decode" in generation, "prompt repair must not recast or re-decode")

require("absolute no-correction benchmarks" in regression, "protected benchmark policy missing")
require("Do not generate or regenerate them" in regression, "protected benchmarks must remain frozen")
require("must not replace the saved baseline" in regression, "benchmark replacement guard missing")
for test_id in ("test-04", "test-06"):
    for filename in ("reference.jpg", "v1-baseline.png"):
        require(
            (benchmarks_root / test_id / filename).is_file(),
            f"protected benchmark fixture missing: {test_id}/{filename}",
        )

for rule in [
    "CASE03",
    "matte-black planar field",
    "pale-blue translucent layer",
    "medium-blue translucent layer",
    "deep-blue layered film",
    "no giant black foliage",
    "no mass of blue flowers",
    "no photographic or illustrated sea",
    "no disappearing or visually negligible wrapper",
]:
    require(rule in regression_v12, f"CASE03 carrier regression rule missing: {rule}")
require(carrier_regression_fixture.is_file(), "CASE03 carrier regression fixture missing")
require(carrier_regression_output.is_file(), "CASE03 validated hotfix output missing")

require("material-library" in skill, "material library is not routed from SKILL.md")
require("Floral Casting Rules V1.3" in skill, "casting rules are not routed from SKILL.md")
require("Object Translation Hard Cases" in skill, "object-translation hard cases are not routed from SKILL.md")
require(
    "Carrier → Function inside that carrier → Morphology → Scale → Texture → Material / Physical DNA → Specific Material → Color Treatment" in skill,
    "carrier-first V1.2 casting order missing from SKILL.md",
)

material_blocks: list[str] = []
for content in material_texts:
    material_blocks.extend(re.split(r"(?m)^  - material_id: ", content)[1:])
require(40 <= len(material_blocks) <= 60, f"material library must contain about 40–60 entries, found {len(material_blocks)}")
material_ids = [block.splitlines()[0].strip() for block in material_blocks]
require(len(material_ids) == len(set(material_ids)), "material IDs must be unique")

for material_id, block in zip(material_ids, material_blocks):
    for field in ("name_cn:", "category:", "visual_profile:", "roles:", "treatment_tolerance:", "physical_dna:"):
        require(field in block, f"material {material_id} missing field: {field}")
    for treatment in (
        "absorption_dye:",
        "spray_dye:",
        "gradient_dye:",
        "edge_dye:",
        "center_dye:",
        "bleach:",
        "metallic_spray:",
    ):
        require(treatment in block, f"material {material_id} missing tolerance: {treatment}")

all_material_text = "\n".join(material_texts)
required_material_names = [
    "重瓣百合", "东方百合", "百合", "芍药", "大丽花", "重瓣郁金香", "大型郁金香", "蝴蝶兰",
    "大花红掌", "马蹄莲", "帝王花", "大型绣球", "鸡冠花", "大型石斛兰", "大型兰花类",
    "洋牡丹", "毛茛", "银莲花", "铁线莲", "香豌豆", "小苍兰", "石斛兰", "文心兰", "蕙兰",
    "贝母", "鸢尾", "针垫花", "姜荷花", "火炬姜", "蜘蛛菊", "飞燕草", "剑兰", "金鱼草",
    "狐尾百合", "落新妇", "蒲苇", "芒草", "垂柳枝", "雪柳", "龙柳", "枯枝", "染色枝",
    "藤蔓", "钢草", "长线型草叶", "蕾丝花", "满天星", "染色干花", "蒲葵", "龟背叶",
    "散尾葵", "剑叶", "鸢尾叶", "银叶", "尤加利", "染色叶", "骨架叶", "枯叶", "大型硬质热带叶",
    "cardstock", "art_paper", "handmade_paper", "kraft_paper", "printed_paper", "torn_edge_paper",
    "organza", "translucent_film", "clear_plastic", "mesh", "acrylic_sheet", "metal_mesh", "metal_wire",
    "mirror_material", "silver_film", "black_rigid_sheet", "ribbon", "cotton_fabric", "mesh_fabric", "velvet", "tulle",
]
for name in required_material_names:
    require(name in all_material_text, f"required material or variant missing: {name}")

required_treatments = [
    "natural:", "absorption_dye:", "spray_dye:", "gradient_dye:", "edge_dye:", "center_dye:",
    "dip_dye:", "two_tone:", "bleach:", "metallic_spray:", "matte_coating:",
]
for treatment in required_treatments:
    require(treatment in color_treatment, f"color treatment missing: {treatment}")
for distribution in (
    "uniform", "center_to_edge", "edge_to_center", "top_to_bottom", "bottom_to_top",
    "one_side", "random_cloud", "vein_following", "spot", "layered",
):
    require(distribution in color_treatment, f"color distribution missing: {distribution}")

for rule in (
    "Not every bouquet needs a Hero Flower",
    "focus_attention >= 4",
    "Select three to five candidates",
    "morphology_fit × 2",
    "semantic_fit × 2",
    "novelty",
    "repetition_penalty",
    "Safe Flower Repetition Penalty",
    "unnecessary_luxury_materials: false",
    "treatment_overuse: false",
    "Complexity-to-density gate",
    "Non-floral object translation gate",
    "one or two floral Hero/anchor flowers",
    "two to four functional supporting groups",
    "front/middle/back depth",
    "Literal entity preservation (prohibited for ordinary props)",
):
    require(rule in casting_rules, f"casting rule missing: {rule}")

for rule in (
    "Carrier Assignment is authoritative over Material Casting",
    "read only the file permitted by the lock",
    "Do not search all libraries for the visually strongest material",
    "Floral Identity must never override Carrier Lock",
    "crosses a locked carrier boundary",
):
    require(rule in casting_rules, f"carrier-lock casting rule missing: {rule}")

for rule in (
    "Every Level 1 `scene_carrier` assignment must create one `carrier_lock.level_1` record",
    "Locked `wrapper` must not become foliage, flower, or branch",
    "Locked `backboard` must not become a giant leaf or flower mass",
    "This is co-carriage, not carrier substitution",
):
    require(rule in schema, f"carrier-lock decoder rule missing: {rule}")

for rule in (
    "Environment co-carriage",
    "does not mean “remove all foliage.”",
    "at or below 20% of total visible botanical area",
    "must not cross in front of or obscure its silhouette",
):
    require(rule in casting_rules, f"environment-support casting rule missing: {rule}")

require("transparent_wrapper_family" in all_material_text, "transparent wrapper packaging family missing")

for rule in (
    "Case 1 — Scarf or fabric item",
    "Case 2 — Headwear or accessory",
    "Case 3 — Conical hat or woven bamboo object",
    "fibrous, textile-like",
    "metallic, pearlescent",
    "woven-texture paper",
    "Prohibit a real scarf",
    "Prohibit copied headwear",
    "Prohibit a recognizable conical hat",
):
    require(rule in object_hard_cases, f"object-translation hard case missing: {rule}")

for rule in (
    "A plain background or one photographed subject does not by itself justify a sparse bouquet",
    "`non_minimal` source becomes a sparse single-flower-plus-wrapper result",
    "Casting receives only extracted properties and mapped carrier roles",
):
    require(rule in casting_rules, f"V1.3 casting upgrade missing: {rule}")

for rule in (
    "roughly 80% of the source's important color relationship and emotional character",
    "A sparse “single flower + wrapper” result for `non_minimal` fails QA",
    "no recognizable clothing, scarf, fabric object, accessory, headwear, hat, utensil, furniture",
):
    require(rule in generation, f"V1.3 generation/QA upgrade missing: {rule}")

rows: list[dict[str, str]] = []
if index_path.is_file():
    with index_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
require(len(rows) == 21, f"case index must contain 21 cases, found {len(rows)}")
expected_ids = {f"{index:03d}" for index in range(1, 22)}
actual_ids = {row.get("case_id", "") for row in rows}
require(actual_ids == expected_ids, "case index IDs must be exactly 001–021")

index_fields = {
    "retrieval_tags",
    "visual_features",
    "palette_mode",
    "motion_primary",
    "hardness",
    "gravity",
    "material_identity",
    "focus_architecture",
    "space_architecture",
    "silhouette",
    "density",
}
if rows:
    require(index_fields <= set(rows[0]), "index lacks visual/tag/structural retrieval fields")

card_fields = [
    "case_id:",
    "semantic_core:",
    "key_features:",
    "mapping:",
    "structure:",
    "palette:",
    "motion:",
    "physical_dna:",
    "key_rule:",
    "avoid:",
    "retrieval_tags:",
]
for case_id in sorted(expected_ids):
    card = read(cards_root / f"case-{case_id}.yaml")
    for field in card_fields:
        require(field in card, f"case-{case_id} missing field: {field}")

runtime_images = list((ROOT / "references" / "case-library").rglob("*.jpg"))
require(not runtime_images, "historical case images must not enter runtime references")

retriever = ROOT / "scripts" / "retrieve_cases.py"
if retriever.is_file():
    result = subprocess.run(
        [
            sys.executable,
            str(retriever),
            "--palette-mode",
            "opposition",
            "--focus-architecture",
            "dual_focus",
            "--motion-topology",
            "collision",
            "--tag",
            "红青对抗",
            "--top-k",
            "2",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    require(result.returncode == 0, f"retriever smoke test failed: {result.stderr.strip()}")
    require('"result_count": 1' in result.stdout, "retriever did not isolate the expected case")

if ERRORS:
    for error in ERRORS:
        print(f"FAIL: {error}")
    raise SystemExit(1)

print(f"PASS: V1.3 complexity/density + object-translation upgrade, V1.2 Carrier Lock/Casting protections, fixed decoder flow, {len(material_blocks)} materials, color treatment, carrier-first prompt, QA, CASE03 fixture, three hard cases, and 21-card retrieval are aligned")
