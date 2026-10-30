# Moroccan Darija Source Inventory — v0.1

**Review date:** 2026-10-30  
**Scope:** Publicly discoverable Moroccan Darija text resources for research and possible IDRIS data preparation.  
**Decision rule:** Discovery is not approval. No source in this inventory is approved for model training yet. A dataset card, public download, or permissive wrapper-repository license does not automatically clear the underlying records.

## Status vocabulary

- `candidate`: relevant source found; rights and content review incomplete.
- `restricted`: known terms prevent at least some intended uses.
- `hold`: material rights, provenance, privacy, or contamination questions remain.
- `approved`: only after source-level evidence is recorded in a signed-off manifest. None currently.

## Inventory

| Source | Relevance and known characteristics | Rights / access findings | IDRIS decision |
|---|---|---|---|
| [DODa — Darija Open Dataset](https://github.com/darija-open-dataset/dataset) | Moroccan Darija lexicon, morphology, spelling variants, Arabic and Latin script; repository describes human sentence material and a combined DODa-500K translation file with human and synthetic rows. | Project site states **CC BY-NC 4.0**. NonCommercial restriction is incompatible with assuming unrestricted commercial model use. The current GitHub README also distinguishes human and synthetic material; synthetic examples are not human-validated. Confirm the exact license file and row-level provenance before any use. | **restricted / hold**. Do not include in a commercial-intent training corpus without written permission or a suitable separate license. If used for non-commercial research, preserve attribution and separate human vs synthetic records. |
| [Atlaset](https://huggingface.co/datasets/atlasia/Atlaset) | Large curated Moroccan Darija text corpus; dataset card reports about 155.5M training tokens and 19.2K test tokens, with many upstream sources including news, social media, instruction data and other corpora. | Hugging Face currently requires accepting conditions and sharing contact information to access files. The card lists many constituent datasets; a single blanket license was not established in this review. Upstream rights may differ by source. | **hold**. Do not bulk-download or train from the aggregate until terms are reviewed and every constituent source has traceable rights. Keep its test split out of IDRIS evaluation until contamination and redistribution terms are resolved. |
| [LID Dataset Base](https://huggingface.co/datasets/atlasia/lid-dataset-base) | About 2.05M rows, 46 dialects/languages, 67 source corpora, 44% Latin-script rows; labels support Darija-vs-other and dialect analysis. | Dataset card displays MIT for this dataset repository, but describes a merge of 67 source corpora. The displayed wrapper license is not sufficient evidence that every upstream text may be redistributed or used for model training. Access also requires accepting conditions. Labels are derived from source tags, not necessarily human linguistic annotation. | **hold** for generative training. Candidate for a separate language-identification experiment only after upstream rights, access conditions, split integrity and label quality are audited. |
| [Moroccan Darija dataset directory](https://github.com/nainiayoub/moroccan-darija-datasets) | Research index listing 13 resources, including sentiment, dialect ID, news, speech, NER and offensive-comment datasets. Useful as a discovery map, not itself a training corpus. | It is an index, not a rights grant. Each linked dataset has its own owner, terms and conditions. | **candidate index only**. Follow each primary source and review it independently. |
| [Dvoice](https://github.com/nainiayoub/moroccan-darija-datasets) | Speech-recognition resource listed in the directory; potentially useful for a future audio track, not the initial text-only pilot. | Exact primary source, consent, speaker release, redistribution and model-training permissions were not established in this review. | **hold**. Exclude audio and transcripts until source-level consent and license evidence are obtained. |
| [DarNERcorp](https://data.mendeley.com/datasets/286sss4k9v/4) | Moroccan Darija named-entity corpus; research-oriented annotation resource. | The directory cites a Mendeley Data record (V4), but the exact license and permitted model-training/redistribution terms were not verified here. | **candidate / hold**. Inspect the primary record and its license before any use; consider only for a separate NER task. |
| [DarijaData](https://darijadata.com/) | Advertises Moroccan Darija speech and text corpora with consent and licensing documentation. | The provider describes licensed access and consent documentation; no public downloadable corpus or public license was identified. | **not a free source**. Contact only if a budget and formal data agreement become available. |

## Initial decisions

1. **No raw dataset has been downloaded, copied, or committed by this inventory update.**
2. **No source is approved for IDRIS model training at v0.1.**
3. Treat DODa as non-commercial-restricted unless its rights holder grants broader written permission.
4. Treat Atlaset and LID Dataset Base as aggregates requiring upstream provenance and rights review; do not infer blanket permission from the dataset page or wrapper license.
5. Do not use published test splits as IDRIS evaluation data until contamination and license checks are complete.
6. Prefer a small, directly contributed, consent-documented Darija corpus for the first clean pilot. Record contributor permission, scope, attribution preference, withdrawal contact, and whether model training and redistribution are allowed.
7. Keep all raw source files outside Git. Commit manifests, scripts, documentation and aggregate quality reports only.

## Minimum approval checklist for each source

- [ ] Primary source and immutable version/commit recorded.
- [ ] Exact license text and terms URL archived or hashed.
- [ ] Rights holder and attribution requirements identified.
- [ ] Model-training permission explicitly established.
- [ ] Commercial-use permission established if commercial use may occur.
- [ ] Redistribution permission recorded separately from training permission.
- [ ] Access conditions and any account/contact-information requirements recorded.
- [ ] Privacy, personal-data and sensitive-content review completed.
- [ ] Human-authored, synthetic and translated records distinguishable.
- [ ] Upstream provenance and duplicate/benchmark contamination reviewed.
- [ ] Dataset manifest completed and independently reviewed.

## Research references

- Atlaset dataset card: https://huggingface.co/datasets/atlasia/Atlaset
- LID Dataset Base card: https://huggingface.co/datasets/atlasia/lid-dataset-base
- DODa project: https://github.com/darija-open-dataset/dataset
- DODa project site and stated license: https://darija-open-dataset.github.io/
- Moroccan Darija dataset directory: https://github.com/nainiayoub/moroccan-darija-datasets
- DarijaData provider: https://darijadata.com/

This inventory is a preliminary engineering review, not legal advice or a final license opinion. Re-check terms at the time of acquisition and before each release.
