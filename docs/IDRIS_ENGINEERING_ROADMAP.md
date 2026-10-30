# IDRIS Engineering Roadmap

**Status:** Proposed execution plan; not evidence of completed work  
**Scope:** Darija data, evaluation, baseline, and first adaptation

## Objective

Turn the existing lexicon and repository tooling into a rights-cleared, reviewed, context-rich Darija corpus and a reproducible first model experiment. Darija remains the first priority. Amazigh, Hassaniya, and Moroccan Sign Language are later research tracks; design compatible interfaces now, but do not claim support before dedicated data and evaluation exist.

## Workstream 1 — Data rights and governance

- Verify ownership and contributor rights for first-party assets, including the Moroccan Darija Lexicon.
- Review license, consent, source terms, redistribution, and model-training permission separately for every source.
- Maintain a source manifest and preserve provenance through every transformation.
- Keep raw and restricted data out of Git; use access-controlled storage.
- Label human-authored, transcribed, translated, and synthetic data distinctly.

**Gate:** No record enters training without approved use, traceable provenance, and required review.

## Workstream 2 — Expand beyond the lexicon

Create versioned collections for:

1. Lexicon: words, variants, meanings, script mappings, and examples.
2. Short and long sentences from everyday domains.
3. Multi-sentence contexts that require reference resolution and implied-meaning comprehension.
4. Multi-turn dialogues with speaker turns and coherent conversation state.
5. Pragmatics: humor, irony, sarcasm, seriousness, politeness, disagreement, uncertainty, indirect requests.
6. Code-switching between Darija, French, and Arabic.
7. Documented regional and community variants.
8. Later: consented audio with transcripts and alignment metadata.

Preserve the original text. Store normalization and transliteration as separate derived fields; never overwrite a speaker's spelling. Allow unknown or ambiguous labels when intent and emotion cannot be established.

**Pilot target:** 1,000–2,000 reviewed examples across the collections, with meaningful diversity rather than near-duplicates. This is a pilot target, not proof of broad language competence.

## Workstream 3 — Annotation and quality

- Publish an annotation handbook with definitions and positive/negative examples.
- Independently review a representative subset twice and adjudicate disagreements.
- Track reviewer role and consent without collecting unnecessary personal details.
- Measure agreement for intent and tone labels.
- Audit balance by region, script, topic, length, and source.
- Detect exact and near duplicates; group related examples before dataset splitting to prevent leakage.
- Keep correction logs and dataset changelogs.

**Gate:** The corpus can be rebuilt from approved sources and every record has a known origin and review state.

## Workstream 4 — Held-out evaluation

Create and freeze an evaluation set before training. Keep it isolated from training and prompt-tuning.

Test lexical meaning, long-context comprehension, multi-turn memory, reference resolution, humor and sarcasm, seriousness and politeness, Arabic script, Arabizi, spelling variation, code-switching, natural response generation, instruction following, uncertainty, and hallucination resistance.

Use fluent Darija speakers for human evaluation. Report results by task, representative errors, and limitations. Do not reduce language quality to one aggregate score.

## Workstream 5 — Baseline and first adaptation

1. Compare candidate base models for language coverage, tokenizer behavior, context length, license, hardware needs, and immutable revision.
2. Measure an unadapted baseline on the frozen benchmark.
3. Create a reproducible environment and smoke test.
4. Run a small supervised fine-tuning experiment on reviewed instructions and dialogues.
5. Consider continued pretraining only if the approved raw-text corpus is sufficiently large and clean and the experiment has a clear hypothesis.
6. Compare all runs on the same held-out benchmark; inspect regressions in Arabic, French, and general instruction following.
7. Record code, dataset and model revisions, hyperparameters, hardware, seeds, logs, and output checksums.

QLoRA may be appropriate for a constrained pilot if the selected model and hardware support it. Do not assume a model or GPU is approved before checking licensing and runtime compatibility.

## Workstream 6 — Release gates

A release candidate requires a model card, dataset statements, source/license and privacy review, reproducible training/evaluation, known limitations, intended-use guidance, and safety testing. Distinguish research experiments from previews and production-ready systems.

Do not announce public weights or an API until the actual artifact or endpoint, license, evaluation, and operational limits are published.

## Indicative sequence

Durations are planning estimates for a solo maintainer or small team, not commitments or proof of progress.

| Phase | Estimate | Deliverable |
|---|---:|---|
| P0 — Audit | 1–2 weeks | Source and rights matrix; data inventory |
| P1 — Data design | 1 week | Annotation handbook; schemas and templates |
| P2 — Pilot corpus | 3–6 weeks | 1,000–2,000 reviewed examples; quality report |
| P3 — Benchmark | 2–3 weeks | Frozen held-out evaluation set |
| P4 — Baseline | 1–2 weeks | Base-model comparison and baseline report |
| P5 — First adaptation | 1–3 weeks | Reproducible SFT/QLoRA pilot and error analysis |
| P6 — Iteration | Ongoing | Dataset/model revisions and release review |

Benchmark design must precede training, and the test set must remain isolated.

## Immediate actions

1. Audit the current lexicon and preserve it as a versioned first-party asset.
2. Extend the schema for sentences, contexts, dialogues, intent, tone, and provenance without breaking existing records.
3. Add collection templates and validation tests.
4. Write the Darija annotation handbook.
5. Build a small consented and reviewed pilot.
6. Freeze and isolate the first evaluation set.
7. Only then select and benchmark a base model.

## Later language and modality tracks

- **Amazigh:** separate tracks for Tashelhit, Central Atlas Tamazight, and Tarifit, with variety and script metadata and community review.
- **Hassaniya:** its own corpus and evaluation track; do not assume a small sample represents all communities.
- **Moroccan Sign Language (LSM):** a multimodal project led with Deaf LSM users and qualified practitioners. Plan for video, temporal movement, facial grammar, spatial relations, consent, secure media storage, and human evaluation. It is not a text-only extension or a universal sign-language feature.

## Success criteria

The Darija foundation is ready for a first research experiment when every training record has approved, traceable provenance; annotation and review are explicit; the corpus includes long contexts and dialogue; the held-out benchmark is frozen and leakage-audited; a baseline has been measured; and the first experiment is reproducible with honest reporting of gains and regressions.

**Principle:** Build evidence before scale. Build language competence from real, reviewed communication—not from a larger word list alone.
