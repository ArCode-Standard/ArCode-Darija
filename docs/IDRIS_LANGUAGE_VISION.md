# IDRIS Language Vision

**Status:** Strategic direction  
**Maintainer:** ArCode Standard  
**Project:** ArCode Darija  
**Model:** IDRIS (إدريس)

## 1. Vision

IDRIS aims to become an AI system grounded first in the language people use in everyday Moroccan life, then expanded to additional languages and accessible communication modalities.

The initial linguistic foundation is **Moroccan Darija**. The roadmap then expands to **Amazigh varieties**, **Hassaniya**, and **Moroccan Sign Language (LSM)**. Modern Standard Arabic, French, and Arabizi remain important for code-switching, literacy, and practical communication; they do not replace the project's Darija-first identity.

This is a long-term research direction, not a claim that these capabilities already exist. Each stage requires suitable data, community participation, independent evaluation, and a clear release decision.

## 2. Language roadmap

### Stage 1 — Moroccan Darija (primary foundation)

Build strong, natural understanding and generation across:

- Short and long utterances, connected discourse, and multi-turn dialogue.
- Everyday conversation, work, education, public services, and other real contexts.
- Humor, irony, sarcasm, seriousness, politeness, disagreement, uncertainty, and emotional tone.
- Arabic-script Darija, Latin-script Darija (Arabizi), and natural code-switching with French and Arabic.
- Regional, social, and speaker variation without treating one variety as the only correct Darija.

The existing Moroccan Darija lexicon is a seed resource, not a complete language dataset. It should be complemented by reviewed sentences, contextual examples, conversations, and evaluation material.

### Stage 2 — Amazigh

Expand through separately documented varieties, including:

- Tashelhit (Tachelhit / تشلحيت)
- Central Atlas Tamazight (Tamazight / تامازيغت)
- Tarifit (Tarifit / تاريفيت)

Do not collapse these varieties into one artificial standard. Record the variety, region when voluntarily and appropriately supplied, script, orthographic conventions, and reviewer expertise for each example. Support for Tifinagh and other attested writing practices should be based on documented data rather than assumptions.

### Stage 3 — Hassaniya

Develop a dedicated Hassaniya track that documents regional variation, vocabulary, morphology, syntax, oral usage, and code-switching. Record where and how each variety is used when that information is available and appropriate. Do not assume that one small corpus represents all Hassaniya speakers or communities.

### Stage 4 — Moroccan Sign Language (LSM)

Treat sign language as a full language and a distinct multimodal research track—not as a word list, signed version of spoken Darija, or universal sign system.

The work should be led and reviewed with Deaf LSM users, qualified sign-language professionals, and relevant community organizations. Establish the scope and regional variation of LSM with them before defining a dataset standard.

Potential capabilities, developed and evaluated separately, include:

- **Sign-to-text:** video input to a written-language rendering, with uncertainty handling.
- **Sign-to-voice:** sign input to optional spoken output.
- **Text-to-sign:** written text to a reviewed sign-language representation.
- **Voice-to-sign:** speech to sign-language output.

Research data may need video, frame sequences, hand shape and orientation, movement, body posture, facial grammar, spatial relations, and discourse context. A hand-shape classifier alone is not sign-language understanding. Text glosses can support annotation but are not a complete substitute for the language itself.

## 3. Shared language-data principles

Every dataset track should preserve provenance and linguistic distinctions. At minimum, records should capture, where applicable:

- Stable record ID and dataset/version identifier.
- Language and variety (for example, ary, zgh, tzm, rif, or a carefully documented Hassaniya label).
- Script and orthographic convention.
- Text, dialogue turns, or a reference to securely stored media.
- Context, communicative intent, tone, and emotion only when supported by the example.
- Source, author/contributor consent, license, permitted uses, and redistribution status.
- Human-authored, transcribed, translated, or synthetic origin.
- Review status, reviewer role, and correction history.

Do not infer a speaker's identity, location, ethnicity, emotion, or intent without evidence. Avoid collecting unnecessary personal data. Keep raw media access-controlled and do not commit sensitive recordings to the public repository.

## 4. Model and system architecture

The intended direction is a shared reasoning and dialogue core connected to specialized language and modality components:

1. **Shared core:** dialogue state, instruction following, reasoning, and context management.
2. **Language components:** Darija, Amazigh varieties, and Hassaniya data and evaluation tracks.
3. **Text processing:** script handling, normalization, transliteration where justified, and code-switching.
4. **Audio components:** speech recognition and speech generation, introduced only when supported by data and evaluation.
5. **Visual and sign components:** video perception, temporal movement modeling, and sign-language generation.
6. **Communication layer:** interfaces that connect text, audio, and visual outputs while preserving the distinctions between languages and modalities.

This is a target architecture, not a requirement to train one enormous model or implement every modality in the first release. Modular components and explicit interfaces allow the project to evolve without rebuilding the Darija foundation. Any shared representations must be tested for negative transfer and loss of linguistic detail.

## 5. Evaluation and release gates

A language or modality is not considered supported merely because examples were added to training. Each stage must have:

- A documented, rights-cleared dataset with train, validation, and held-out test separation.
- Review by fluent speakers and, where relevant, trained linguists or community experts.
- Tests for comprehension, generation quality, context retention, code-switching, and ambiguity.
- Coverage analysis across varieties, scripts, domains, and speaker groups where ethically collected.
- Error analysis, limitations, and known failure cases.
- Public claims tied to reproducible evaluation results.

For LSM, evaluation must include Deaf native or highly proficient signers and assess meaning preservation, grammaticality, intelligibility, and real-world usability. Consent, privacy, and control over recordings are mandatory.

## 6. Responsible development

- Do not describe synthetic examples as authentic community speech.
- Do not use a dataset unless its provenance, consent, license, and permitted use have been reviewed.
- Do not assume a dataset's public availability grants permission for every training or commercial use.
- Credit contributors according to their preferences and the applicable agreements.
- Provide a way to report errors and request correction or removal where applicable.
- Avoid presenting IDRIS as a replacement for qualified human interpreters, especially in medical, legal, emergency, or other high-stakes settings.
- In accessibility applications, provide uncertainty indicators and a human fallback.

## 7. Current status

This document records the project's strategic direction only. It does not assert that IDRIS currently understands Darija, Amazigh, Hassaniya, or LSM at a production level. Dataset readiness, model training, and benchmark results must be reported separately and only when verified.

## 8. Guiding principle

> A language is not a list of words. It is a living system of meaning, context, expression, and communication.

**IDRIS begins with Moroccan Darija, grows through the languages and communities of the region, and works toward more inclusive communication.**
