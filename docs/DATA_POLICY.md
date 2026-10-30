# Data Governance and Policy

## Core rule
Public accessibility does not itself grant permission for dataset reuse or model training. Verify source, license, terms, copyright, privacy implications, and permissions before collection or use.

## Required dataset record
Record a stable ID and version; source URL or collection method; rights holder; license and terms; explicit model-training and redistribution permissions; access date; language, dialect, script, and domain; approximate size; privacy assessment; transformations; limitations; and removal/contact procedure.

Unknown or ambiguous rights status means quarantine. Do not train on or redistribute the material until resolved.

## Privacy and consent
Do not intentionally collect private conversations, credentials, personal records, private groups, or content obtained by bypassing access controls. Minimize personal data and remove identifiers where appropriate and legally permissible.

## Separation
Keep raw, interim, approved training, validation, and held-out evaluation data separate. Evaluation data must not be used for training or iterative model selection. Record split methodology and deduplication boundaries.

## Synthetic and human-authored data
Label synthetic, human-authored, and externally sourced examples separately. Record generation method, review status, and source materials. Synthetic generation does not automatically clear underlying rights.

## Removal and release
Provide a route for rights holders and individuals to raise concerns. Freeze affected data pending review and record downstream artifacts. Do not promise model unlearning without a documented, validated process.

A dataset cannot be marked approved until provenance, license, permitted use, privacy review, and quality checks are documented. This policy is not legal advice.
