import json

from idris_data.pipeline import prepare_corpus

import pytest


SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": [
        "record_id",
        "text",
        "language",
        "script",
        "source_id",
        "split",
        "consent_status",
    ],
    "properties": {
        "record_id": {"type": "string", "minLength": 1},
        "text": {"type": "string", "minLength": 1},
        "language": {"enum": ["ary", "ar", "fr", "mixed", "unknown"]},
        "script": {"enum": ["Arab", "Latn", "mixed", "other"]},
        "source_id": {"type": "string", "minLength": 1},
        "split": {"enum": ["train", "validation", "test", "quarantine"]},
        "consent_status": {
            "enum": ["verified", "licensed", "synthetic", "unknown", "rejected"]
        },
        "review_status": {"enum": ["unreviewed", "reviewed", "rejected"]},
    },
    "additionalProperties": True,
}


def _record(record_id, text, split="train", consent="licensed", review="reviewed"):
    return {
        "record_id": record_id,
        "text": text,
        "language": "ary",
        "script": "Arab",
        "source_id": "test-source",
        "split": split,
        "consent_status": consent,
        "review_status": review,
    }


def test_prepare_corpus_filters_and_deduplicates_across_splits(tmp_path):
    schema_path = tmp_path / "schema.json"
    input_path = tmp_path / "records.jsonl"
    output_dir = tmp_path / "processed"
    schema_path.write_text(json.dumps(SCHEMA), encoding="utf-8")
    records = [
        _record("1", "  سلام   عليكم ", "train"),
        _record("2", "سلام عليكم", "test"),
        _record("3", "نص غير مرخص", consent="unknown"),
        _record("4", "نص غير مراجع", review="unreviewed"),
        _record("5", "نص صالح", "validation", consent="synthetic"),
    ]
    input_path.write_text(
        "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in records),
        encoding="utf-8",
    )

    report = prepare_corpus(input_path, schema_path, output_dir)

    assert (output_dir / "train.txt").read_text(encoding="utf-8") == "سلام عليكم\n"
    assert (output_dir / "test.txt").read_text(encoding="utf-8") == ""
    assert (output_dir / "validation.txt").read_text(encoding="utf-8") == "نص صالح\n"
    assert report["duplicates_removed"] == 1
    assert report["excluded_rights"] == 1
    assert report["excluded_review"] == 1
    assert report["records_exported"] == 2


def test_prepare_corpus_fails_closed_on_invalid_jsonl(tmp_path):
    schema_path = tmp_path / "schema.json"
    input_path = tmp_path / "records.jsonl"
    schema_path.write_text(json.dumps(SCHEMA), encoding="utf-8")
    input_path.write_text("{invalid}\n", encoding="utf-8")

    with pytest.raises(ValueError, match="failed schema validation"):
        prepare_corpus(input_path, schema_path, tmp_path / "processed")
