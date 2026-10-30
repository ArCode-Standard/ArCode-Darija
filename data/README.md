# Data workspace

Large datasets are not committed to Git.

- raw: original source material; restricted and immutable where practical.
- interim: intermediate transformations.
- processed: validated, approved, versioned artifacts.
- external: externally managed files with separate terms.

Before adding a source, create a manifest entry, verify license and training
permissions, assess privacy, and assign pending_review, approved, or rejected
status. Validate records against [schema.json](schema.json). Keep evaluation
data separate from training data.

The preparation utility is deliberately fail-closed:
- only records with consent_status `verified`, `licensed`, or `synthetic`;
- only records with review_status `reviewed`;
- only `train`, `validation`, and `test` splits;
- exact duplicates are removed globally after conservative normalization.

Run it with:

```bash
python scripts/prepare_corpus.py path/to/approved-records.jsonl
```

It writes one UTF-8 text file per split plus a JSON preparation report to
`data/processed/` by default. Inspect the report before using outputs. A public
URL is not sufficient evidence of reuse permission.
