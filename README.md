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

## Language scope and roadmap

**Current research scope: Moroccan Darija only.** The first research and data track focuses on Darija written in Arabic script and Latin script (Arabizi), including natural code-switching with French and Modern Standard Arabic (MSA), and regional and contextual variation within Moroccan Darija.

French and MSA are included as languages that may appear in mixed-language examples or serve as translation/context targets. Their inclusion does not mean that IDRIS is currently a general-purpose French or Arabic model.

**Future strategic directions — not active project scope:** Amazigh varieties (including Tashelhit, Central Atlas Tamazight and Tarifit), Hassaniya, and Moroccan Sign Language (LSM) are described in the language vision as possible independent future research tracks. They are not part of the current dataset, model-development scope, or available capabilities. Each would require its own community-led scoping, data rights, specialist review, and evaluation before work begins.

- Study and document Moroccan Darija as used by speakers.
- Preserve Arabic-script and Latin-script (Arabizi) writing without imposing one spelling standard.
- Examine code-switching with French and MSA in Darija contexts.
- Represent regional, social, and contextual variation within Moroccan Darija.
- Treat any additional language or modality as a separately approved future track.

See [IDRIS Language Vision](docs/IDRIS_LANGUAGE_VISION.md) for the long-term roadmap and its stage gates.

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

## Licensing, copyright, and reuse

### Current repository-wide status

**This repository does not currently have a single repository-wide license.** Until a license is explicitly selected, approved, and added for a particular category of material, copyright and other applicable rights remain with their respective authors or rights holders. Making a file publicly accessible on GitHub does not, by itself, grant permission to copy, modify, redistribute, commercially use, or include it in model training.

Do not interpret the absence of a license as an open-source or public-domain dedication. A license added to one category or directory must not be assumed to cover the rest of the repository.

### Decisions by content category

| Category | Current status | Required decision / handling |
|---|---|---|
| **Source code** | No repository-wide code license has been adopted. | Select and approve a software license (for example, MIT or Apache-2.0), then add its license text and clearly define which files it covers. Until then, all rights remain with the relevant code authors or rights holders. |
| **Documentation and website content** | No documentation license has been adopted. | Select a separate documentation license (for example, CC BY 4.0) and state its scope. Do not assume a future code license also covers prose, diagrams, images, or website assets. |
| **Project-owned datasets** | No blanket data license applies to all data in this repository. | License each dataset/version explicitly, after confirming that the project has the rights needed to do so. Keep dataset licensing separate from code and documentation licensing. |
| **Community contributions** | No Contributor License Agreement (CLA), Developer Certificate of Origin (DCO), or other inbound contribution license has been adopted. | Contributors retain their copyright. A pull request does not transfer ownership or automatically grant the project permission to redistribute or relicense the contribution. Before merging copyrightable code, prose, or data, maintainers must establish that the contributor has authority to submit it and obtain the permissions required under the applicable contribution terms. |
| **External resources** | Governed by their original rights holders, licenses, and terms. | Record the source, author/rightsholder, exact license or permission, applicable version, attribution requirements, and permitted uses. Do not copy, redistribute, adapt, or use material for training unless those actions are permitted. If rights are unclear, quarantine the material and do not use it. |

### Existing Moroccan Darija dataset

The separate [moroccan-darija-dataset](https://github.com/ArCode-Standard/moroccan-darija-dataset) repository currently identifies its lexical dataset as **CC BY-NC 4.0**. That license applies to the material expressly covered by that dataset repository's license and notices; it does **not** automatically license this repository's source code, documentation, website, or other datasets. Non-commercial restrictions also mean it must not be treated as permission for commercial reuse.

Before distributing or using any dataset, verify that every included item is eligible for the stated license. A project license cannot grant rights that the project does not own or control.

### Interim rules pending formal adoption

1. Keep code, documentation, datasets, website assets, and third-party resources distinguishable; do not apply one blanket license by implication.
2. Preserve copyright notices, attribution, source references, and license files supplied with imported material.
3. Record dataset provenance and permitted uses in the data manifest and source inventory. Training permission and redistribution permission must be checked separately.
4. Do not merge community material when the contributor's authority or the required inbound permission is unresolved.
5. When a category-specific license is adopted, add the full license text, identify its scope, and update this table and the relevant contribution/data policies.

These statements describe the project's current handling policy; they are not legal advice. License selection and contribution terms should be reviewed for compatibility with the project's intended research and future distribution model.

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
