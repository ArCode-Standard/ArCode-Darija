# Training Methodology — Proposed

This is an experimental plan, not a claim that training has occurred.

## Base checkpoint
Qwen3-4B-Base is a candidate for investigation, not an approved dependency. Verify the exact immutable revision, model and tokenizer licenses, architecture, supported library versions, Arabic/Darija/Arabizi tokenization, chat template, and GPU memory requirements before selection.

## Data preparation
Validate records against the project schema; preserve provenance; normalize Unicode conservatively; detect exact and near duplicates; remove disallowed personal data; split by source or conversation before augmentation; and isolate evaluation data.

## Adaptation
A. Baseline: evaluate the untouched base checkpoint on a frozen test suite.
B. Optional continued pretraining: use only approved, high-quality raw text; compare to baseline and monitor regressions.
C. Supervised fine-tuning: use reviewed instruction-response examples with explicit language, script, and dialect metadata.

LoRA or QLoRA may be suitable for constrained hardware. Record quantization, rank, target modules, sequence length, effective batch size, optimizer, scheduler, seed, precision, package versions, and hardware. Choose hyperparameters only after the actual GPU budget is known.

## Evaluation
Measure Arabic-script Darija, Arabizi, regional variation, French/Arabic code-switching, instruction following, factuality, calibration, privacy leakage, safety, and regression in Arabic and French. Human review by competent Moroccan Darija speakers is required; automated metrics alone are insufficient.

## Reproducibility
Record dataset manifest versions, code commit, base and tokenizer revisions, configuration, seed, hardware, runtime versions, package lock, logs, evaluation protocol, and checkpoint hashes.

Do not publish performance claims without a reproducible evaluation report.
