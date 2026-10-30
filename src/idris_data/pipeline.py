"""Build conservative, license-aware plain-text corpora from approved JSONL records."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from idris_data.normalize import normalize_text
from idris_data.validation import validate_jsonl

APPROVED_CONSENT = {"verified", "licensed", "synthetic"}
USABLE_SPLITS = {"train", "validation", "test"}


def prepare_corpus(
    input_path: str | Path,
    schema_path: str | Path,
    output_dir: str | Path,
) -> dict[str, Any]:
    """Validate records and export reviewed, approved text into isolated split files.

    Records with unknown/rejected rights, unreviewed status, or quarantine splits
    are excluded. Exact normalized duplicates are removed globally to prevent
    cross-split leakage. The function never changes source records.
    """
    source = Path(input_path)
    errors = validate_jsonl(source, schema_path)
    if errors:
        preview = "; ".join(errors[:10])
        raise ValueError(f"input JSONL failed schema validation: {preview}")

    buckets: dict[str, list[str]] = {split: [] for split in sorted(USABLE_SPLITS)}
    seen: set[str] = set()
    counts: dict[str, int] = {
        "records_seen": 0,
        "records_exported": 0,
        "excluded_rights": 0,
        "excluded_review": 0,
        "excluded_split": 0,
        "excluded_empty": 0,
        "duplicates_removed": 0,
    }

    with source.open("r", encoding="utf-8") as handle:
        for raw_line in handle:
            record = json.loads(raw_line)
            counts["records_seen"] += 1
            if record.get("consent_status") not in APPROVED_CONSENT:
                counts["excluded_rights"] += 1
                continue
            if record.get("review_status") != "reviewed":
                counts["excluded_review"] += 1
                continue
            split = record.get("split")
            if split not in USABLE_SPLITS:
                counts["excluded_split"] += 1
                continue

            text = normalize_text(record["text"])
            if not text:
                counts["excluded_empty"] += 1
                continue
            if text in seen:
                counts["duplicates_removed"] += 1
                continue

            seen.add(text)
            buckets[split].append(text)
            counts["records_exported"] += 1

    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    for split, texts in buckets.items():
        output_path = destination / f"{split}.txt"
        content = "\n".join(texts)
        output_path.write_text(content + ("\n" if content else ""), encoding="utf-8")

    report = {
        "input_file": source.name,
        "policy": {
            "accepted_consent_status": sorted(APPROVED_CONSENT),
            "required_review_status": "reviewed",
            "accepted_splits": sorted(USABLE_SPLITS),
            "deduplication": "global exact match after NFC and whitespace normalization",
        },
        "split_counts": {split: len(texts) for split, texts in buckets.items()},
        **counts,
    }
    (destination / "preparation-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return report
