"""Prepare approved JSONL records as isolated plain-text corpus splits."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from idris_data.pipeline import prepare_corpus


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Source JSONL file")
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path("data/schema.json"),
        help="JSON Schema path (default: data/schema.json)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/processed"),
        help="Output directory (default: data/processed)",
    )
    args = parser.parse_args()
    report = prepare_corpus(args.input, args.schema, args.output_dir)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
