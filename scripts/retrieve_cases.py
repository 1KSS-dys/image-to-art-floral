#!/usr/bin/env python3
"""Retrieve 1–3 floral translation experience cards from the compact index."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
LIBRARY_ROOT = SKILL_ROOT / "references" / "case-library"
INDEX_PATH = LIBRARY_ROOT / "case-index.tsv"
CARDS_ROOT = LIBRARY_ROOT / "cards"

CATEGORY_WEIGHTS = {
    "palette_mode": 4.0,
    "focus_architecture": 4.0,
    "space_architecture": 3.0,
    "motion_primary": 4.0,
    "hardness": 2.5,
    "gravity": 2.0,
    "density": 1.5,
}

CATEGORY_MISMATCH_PENALTIES = {
    "palette_mode": 2.0,
    "focus_architecture": 1.0,
    "space_architecture": 0.5,
    "motion_primary": 2.5,
    "hardness": 1.0,
    "gravity": 0.5,
    "density": 0.25,
}


def normalize(value: str) -> str:
    return re.sub(r"[\s_\-]+", "", value.strip().lower())


def split_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def text_units(value: str) -> set[str]:
    normalized = normalize(value)
    if not normalized:
        return set()
    ascii_words = set(re.findall(r"[a-z0-9]+", normalized))
    cjk_runs = re.findall(r"[\u3400-\u9fff]+", normalized)
    cjk_bigrams = {
        run[i : i + 2]
        for run in cjk_runs
        for i in range(max(0, len(run) - 1))
    }
    return ascii_words | cjk_bigrams


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Retrieve mechanism-level floral case cards after image decoding."
    )
    parser.add_argument("--palette-mode")
    parser.add_argument("--focus-architecture")
    parser.add_argument("--space-architecture")
    parser.add_argument("--motion-topology", "--motion-primary", dest="motion_primary")
    parser.add_argument("--hardness")
    parser.add_argument("--gravity")
    parser.add_argument("--density")
    parser.add_argument("--material", action="append", default=[])
    parser.add_argument("--silhouette", action="append", default=[])
    parser.add_argument("--tag", action="append", default=[])
    parser.add_argument("--feature", action="append", default=[])
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--min-score", type=float, default=3.0)
    args = parser.parse_args()
    if not 1 <= args.top_k <= 3:
        parser.error("--top-k must be between 1 and 3")
    return args


def load_index() -> list[dict[str, str]]:
    with INDEX_PATH.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def score_case(row: dict[str, str], args: argparse.Namespace) -> tuple[float, list[str]]:
    score = 0.0
    matches: list[str] = []

    for field, weight in CATEGORY_WEIGHTS.items():
        query_value = getattr(args, field)
        if query_value and normalize(query_value) == normalize(row[field]):
            score += weight
            matches.append(f"{field}={row[field]}")
        elif query_value:
            score -= CATEGORY_MISMATCH_PENALTIES[field]

    for field, query_values, weight in (
        ("material_identity", args.material, 1.5),
        ("silhouette", args.silhouette, 2.0),
        ("retrieval_tags", args.tag, 2.0),
    ):
        case_values = {normalize(item): item for item in split_csv(row[field])}
        for query_value in query_values:
            key = normalize(query_value)
            if key in case_values:
                score += weight
                matches.append(f"{field}:{case_values[key]}")

    searchable = " ".join(
        [row["title"], row["retrieval_tags"], row["visual_features"]]
    )
    case_units = text_units(searchable)
    for feature in args.feature:
        units = text_units(feature)
        overlap = units & case_units
        if overlap:
            contribution = min(2.5, 0.5 + 0.35 * len(overlap))
            score += contribution
            matches.append(f"visual_feature:{feature}")

    return round(score, 2), matches


def main() -> int:
    args = parse_args()
    query_present = any(
        [
            args.palette_mode,
            args.focus_architecture,
            args.space_architecture,
            args.motion_primary,
            args.hardness,
            args.gravity,
            args.density,
            args.material,
            args.silhouette,
            args.tag,
            args.feature,
        ]
    )
    if not query_present:
        print("At least one decoded mechanism field is required.", file=sys.stderr)
        return 2

    ranked = []
    for row in load_index():
        score, matches = score_case(row, args)
        if score >= args.min_score:
            ranked.append((score, row["case_id"], matches, row))

    ranked.sort(key=lambda item: (-item[0], item[1]))
    selected = ranked[: args.top_k]
    results = []
    for score, case_id, matches, row in selected:
        card_path = CARDS_ROOT / f"case-{case_id}.yaml"
        results.append(
            {
                "case_id": case_id,
                "title": row["title"],
                "score": score,
                "matched_on": matches,
                "copy_guard": (
                    "Transfer only abstraction, carrier-role, structural reasoning, key_rule, "
                    "and avoid guidance. Do not copy flowers, materials, wrapping, composition, "
                    "decorations, or color ratios unless independently justified by the input image."
                ),
                "card": card_path.read_text(encoding="utf-8"),
            }
        )

    payload = {
        "retrieval_policy": "post-decoder uncertainty only; 1–3 cases; mechanism match over subject/color",
        "result_count": len(results),
        "results": results,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
