# Data workspace

Large datasets are not committed to Git.

- raw: original source material; restricted and immutable where practical.
- interim: intermediate transformations.
- processed: validated, approved, versioned artifacts.
- external: externally managed files with separate terms.

Start with [SOURCE_INVENTORY.md](SOURCE_INVENTORY.md) for the preliminary public-source review. It is a discovery document, not training approval. Before adding any source, create a manifest entry, verify license and training permissions, assess privacy, and assign pending_review, approved, or rejected status. Validate records against [schema.json](schema.json). Keep evaluation
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


## First-party ArCode Standard asset

The [Moroccan Darija Lexicon](https://github.com/ArCode-Standard/moroccan-darija-dataset) was created specifically for the originating **ArCode-Darija / IDRIS** project. It is also published as an open resource so the wider community can benefit. It should therefore be treated as a first-party core project asset, not as an unrelated external dataset candidate.

The public repository currently states CC BY-NC 4.0 for reuse by the community. That public license should not be mischaracterized as a restriction imposed by an outside provider on the originating project. Internal project use depends on the actual ownership and contributor/third-party rights chain; maintain that provenance clearly, especially if the corpus includes contributions or material from others.

The current release contains 887 entries in 38 categories, with Arabic Darija, Latin/Arabizi, MSA and French fields. A structural spot-check found 887 records, all documented fields populated, unique IDs, no exact duplicate `darija_ar` values, and 38 observed categories matching the metadata. These checks validate structure only—not linguistic correctness, regional representativeness, naturalness, or translation quality.

Recommended IDRIS use: prioritize this resource for lexical normalization, script mapping, transliteration and seed evaluation. Add row-level provenance/reviewer metadata and manually review a sample across categories and scripts. It is a valuable foundation, but not a substitute for natural conversational data or a standalone conversational SFT corpus.
