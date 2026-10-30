# Roadmap

Milestones are complete only when evidence is committed to the repository.

## M0 — Foundation
- [x] Publish bilingual project viability roadmap with evidence-based GO / PIVOT / HOLD / STOP gates (plan published; validation not yet performed).
- [x] Publish bilingual IDRIS language vision and engineering execution plan (strategic and proposed; not implementation completion).
- [x] Public project identity and initial README.
- [x] Initial visual assets and repository positioning.
- [x] Initial governance, contribution, and security documents.
- [ ] Select an explicit repository license after ownership and dependency review.

## M1 — Data readiness
- [x] Versioned record schema and manifest template.
- [x] JSONL validation and exact-deduplication utilities.
- [x] Conservative Unicode normalization.
- [x] Initial corpus preparation pipeline with rights/review filtering and split isolation.
- [x] Preliminary public-source inventory with explicit hold/restricted decisions (see [data/SOURCE_INVENTORY.md](../data/SOURCE_INVENTORY.md)).
- [ ] Source-level rights review and approved per-source manifests.
- [ ] Leakage-resistant source/group-level split assignment and audit.
- [ ] Human-reviewed Darija evaluation set.

## M2 — Baseline
- [ ] Approve base checkpoint, license, and immutable revision.
- [ ] Freeze evaluation protocol and benchmark dataset.
- [ ] Record baseline results and error analysis.

## M3 — First adaptation
- [x] QLoRA pilot configuration template (not an executable training run).
- [x] Reproducibility requirements.
- [ ] Implement and validate the training runner against an approved checkpoint.
- [ ] Pilot run and memory/throughput validation.
- [ ] Compare SFT and optional continued-pretraining experiments.
- [ ] Evaluate dialect, script, code-switching, and regressions.

## M4 — Release candidate
- [ ] Complete model card and dataset statements.
- [ ] Publish reproducibility metadata and evaluation.
- [ ] Complete privacy and security review.
- [ ] Release only after licensing and quality gates pass.
