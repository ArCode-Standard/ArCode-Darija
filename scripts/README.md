# Data scripts

Install the project in editable mode:

    python -m pip install -e ".[dev]"

Validate JSONL records against the repository schema:

    python scripts/validate_jsonl.py path/to/records.jsonl

Exact deduplication by normalized text:

    python scripts/deduplicate_jsonl.py input.jsonl output.jsonl

The normalizer applies Unicode NFC and whitespace cleanup only. It deliberately does not transliterate Arabizi, remove diacritics, standardize regional vocabulary, or rewrite dialect spelling. Always preserve source data and record every transformation in the dataset manifest.

Run tests with:

    python -m pytest
