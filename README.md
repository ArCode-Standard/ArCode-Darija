# IDRIS — ArCode Darija

<p align="center">
  <strong>A Moroccan Darija–focused language model initiative</strong><br/>
  <em>مشروع نموذج لغوي متخصص في الدارجة المغربية</em>
</p>

---

## About

**IDRIS** is the language-model initiative of **ArCode Darija**, developed by **ArCode Standard**. Its goal is to build an AI model that understands and generates Moroccan Darija naturally while supporting Modern Standard Arabic, French, and Arabizi.

The name **IDRIS** is inspired by Idris I (مولاي إدريس الأول), a historical figure associated with the beginnings of the Idrisid state in Morocco. This is a historical naming inspiration only: the model does not claim to be Idris I or to possess his memories or experiences.

## Project identity

| Item | Description |
|---|---|
| Organization | ArCode Standard |
| Founder of ArCode Standard | Ismail Benali (إسماعيل بنعلي) |
| Project | ArCode Darija |
| Model name | IDRIS (إدريس) |
| Initial target | IDRIS 4B v0.1 |
| Primary language | Moroccan Darija |

## Independent research identity

IDRIS is presented publicly as an **independent Moroccan research initiative** led within ArCode Standard. It is not a university, accredited research institution, registered company, or government programme. The initiative welcomes community participation and future academic collaboration, but does not claim partnerships without confirmation. See the [IDRIS Research Charter](docs/IDRIS_RESEARCH_CHARTER.md) and the [public research portal](website/index.html).

## Language goals

See [IDRIS Language Vision](docs/IDRIS_LANGUAGE_VISION.md) for the long-term Darija-first roadmap, Amazigh and Hassaniya expansion, and the Moroccan Sign Language accessibility track.

- Natural Moroccan Darija understanding and generation.
- Support for Arabic-script Darija and Latin-script Darija (Arabizi).
- Robust handling of regional vocabulary and variation.
- Code-switching between Darija, Arabic, and French.
- Useful general capabilities such as explanation, summarization, translation, and question answering.

## Development principles

- **Accuracy and transparency:** do not fabricate facts, sources, or capabilities.
- **Dialect diversity:** recognize that Darija varies by region and speaker.
- **Responsible data use:** document dataset provenance, licensing, and permitted uses.
- **Evaluation before claims:** publish measured results and limitations; do not claim capabilities that have not been tested.
- **Clear identity:** IDRIS is an AI model, not a human or historical figure.

## Technical direction

The initial research direction is fine-tuning an existing open-weight base model rather than training a foundation model from scratch. Candidate architectures, checkpoints, licenses, tokenizers, and chat templates must be verified before use.

Planned experimentation may include:

1. Dataset inspection, deduplication, normalization, and provenance tracking.
2. Continued pretraining on appropriately licensed raw text, where justified.
3. Supervised fine-tuning (SFT) on reviewed instruction and conversation examples.
4. Evaluation on held-out Moroccan Darija benchmarks.
5. Model-card publication with limitations and reproducibility details.

No training run or benchmark result is claimed by this repository at this stage.

## Repository status

The repository includes project governance, identity specifications, a data manifest template and JSON Schema, JSONL validation and deduplication, and an approved-corpus preparation pipeline that filters by rights and review status and exports isolated splits. It also includes a QLoRA pilot configuration template and reproducibility requirements. These are engineering tools and templates: no approved corpus, training run, benchmark score, or model checkpoint is claimed. See the [roadmap](docs/ROADMAP.md) for evidence-based milestones.

## Developer quick start

Requirements: Python 3.10 or newer.

```bash
python -m pip install -e ".[dev]"
python -m pytest
python scripts/validate_jsonl.py path/to/records.jsonl
python scripts/deduplicate_jsonl.py input.jsonl output.jsonl
```

The initial text normalizer applies Unicode NFC and whitespace cleanup only. It does not transliterate Arabizi, remove diacritics, or rewrite dialect spelling. Review [data policy](docs/DATA_POLICY.md) before using any corpus.

## Data and licensing

Dataset inclusion is conditional on reviewing its license, terms of use, provenance, and redistribution permissions. Synthetic and human-authored data should be identified separately. Evaluation data must remain isolated from training data to reduce contamination.

Until a repository-level license is added, all rights are reserved by their respective owners. Do not assume that this project grants permission to reuse repository contents or third-party datasets.

## Contributing

Contributions related to Moroccan Darija linguistics, dataset documentation, evaluation design, data quality, and model engineering are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution requirements.

## Maintainers

**ArCode Standard**  
Founder: **Ismail Benali (إسماعيل بنعلي)**

---

<p align="center">
  <strong>ArCode Standard</strong><br/>
  Building an Arabic technology ecosystem.
</p>
