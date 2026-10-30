import json

from idris_data.validation import validate_jsonl


def test_valid_record_passes(tmp_path):
    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "required": ["record_id", "text"],
        "properties": {
            "record_id": {"type": "string"},
            "text": {"type": "string", "minLength": 1},
        },
        "additionalProperties": False,
    }
    schema_path = tmp_path / "schema.json"
    data_path = tmp_path / "records.jsonl"
    schema_path.write_text(json.dumps(schema), encoding="utf-8")
    data_path.write_text(
        json.dumps({"record_id": "r1", "text": "لاباس"}) + "\n",
        encoding="utf-8",
    )
    assert validate_jsonl(data_path, schema_path) == []


def test_invalid_jsonl_is_reported(tmp_path):
    schema_path = tmp_path / "schema.json"
    data_path = tmp_path / "records.jsonl"
    schema_path.write_text(json.dumps({"type": "object"}), encoding="utf-8")
    data_path.write_text("{not-json}\n", encoding="utf-8")
    errors = validate_jsonl(data_path, schema_path)
    assert len(errors) == 1
    assert "invalid JSON" in errors[0]
