"""JSONL validation against the repository's dataset record schema."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


def load_schema(schema_path: str | Path) -> dict[str, Any]:
    with Path(schema_path).open("r", encoding="utf-8") as handle:
        schema = json.load(handle)
    Draft202012Validator.check_schema(schema)
    return schema


def validate_jsonl(
    input_path: str | Path, schema_path: str | Path
) -> list[str]:
    """Return human-readable errors; an empty list means all records are valid."""
    validator = Draft202012Validator(load_schema(schema_path))
    errors: list[str] = []
    with Path(input_path).open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            if not raw_line.strip():
                errors.append(f"line {line_number}: blank lines are not valid records")
                continue
            try:
                record = json.loads(raw_line)
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_number}: invalid JSON: {exc.msg}")
                continue
            for error in sorted(validator.iter_errors(record), key=lambda item: list(item.path)):
                location = ".".join(str(part) for part in error.path) or "<record>"
                errors.append(f"line {line_number}, {location}: {error.message}")
    return errors
