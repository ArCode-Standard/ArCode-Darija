# IDRIS — Project Overview

## Mission
IDRIS is a Moroccan Darija-focused language-model initiative by ArCode Standard. It aims to improve natural understanding and generation of Moroccan Darija while supporting Arabic, French, and Arabizi.

## Initial target
IDRIS 4B v0.1 is the initial target class, not evidence that a trained checkpoint exists. The base checkpoint must be selected only after reviewing its license, model card, tokenizer, chat template, architecture, and hardware compatibility.

## Scope
- Moroccan Darija comprehension and generation.
- Arabic-script Darija and Latin-script Darija (Arabizi).
- Regional lexical and grammatical variation.
- Code-switching with French and Modern Standard Arabic.
- Explanation, summarization, translation, and question answering.

The initial project does not claim universal dialect coverage, guaranteed factuality, autonomous agency, or professional reliability.

## Development stages
1. Governance: data, licensing, privacy, security, and contribution rules.
2. Data discovery: review provenance and rights before processing.
3. Data engineering: validate, normalize conservatively, deduplicate, and split to prevent leakage.
4. Baseline: evaluate a documented base model.
5. Adaptation: optional continued pretraining, then supervised fine-tuning.
6. Evaluation: held-out tests for dialect, scripts, code-switching, factuality, and safety.
7. Release: publish a model card, dataset statements, configurations, results, and limitations.

## Current status
This repository contains project identity and planning documentation. No training run, benchmark result, or released IDRIS checkpoint is claimed. Candidate models and datasets remain subject to license and compatibility review.

## Release gates
A release candidate requires documented base-model and data licenses, traceable provenance, reproducible preprocessing and training, leakage-controlled evaluation, a complete model card, and no unresolved critical privacy or security issue.
