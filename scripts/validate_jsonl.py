"""Validate a JSONL corpus against data/schema.json."""

from __future__ import annotations

import argparse
import sys

from idris_data.validation import validate_jsonl


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Path to a JSONL file")
    parser.add_argument(
        "--schema", default="data/schema.json", help="Path to the JSON Schema"
    )
    args = parser.parse_args()

    errors = validate_jsonl(args.input, args.schema)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        print(f"Validation failed: {len(errors)} issue(s).", file=sys.stderr)
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
