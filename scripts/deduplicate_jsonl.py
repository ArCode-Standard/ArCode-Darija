#!/usr/bin/env python3
"""Exact deduplication of JSONL records using conservative normalized text."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from idris_data.normalize import normalize_text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Input JSONL path")
    parser.add_argument("output", help="Output JSONL path")
    parser.add_argument(
        "--text-field", default="text", help="Field used for duplicate detection"
    )
    args = parser.parse_args()

    seen: set[str] = set()
    kept = 0
    removed = 0
    with Path(args.input).open("r", encoding="utf-8") as source, Path(
        args.output
    ).open("w", encoding="utf-8") as target:
        for line_number, raw_line in enumerate(source, start=1):
            if not raw_line.strip():
                continue
            record = json.loads(raw_line)
            if not isinstance(record, dict):
                raise ValueError(f"line {line_number}: expected a JSON object")
            text = record.get(args.text_field)
            if not isinstance(text, str):
                raise ValueError(
                    f"line {line_number}: field {args.text_field!r} must be a string"
                )
            canonical = normalize_text(text)
            digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
            if digest in seen:
                removed += 1
                continue
            seen.add(digest)
            target.write(json.dumps(record, ensure_ascii=False) + "\n")
            kept += 1

    print(f"Kept {kept} record(s); removed {removed} exact duplicate(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
