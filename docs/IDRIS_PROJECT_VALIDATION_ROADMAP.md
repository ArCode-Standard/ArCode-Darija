# IDRIS Project Viability and Validation Roadmap

**Document type:** Strategic, technical, and community validation plan  
**Status:** Proposed; not evidence of completed work or measured results  
**Organization:** ArCode Standard  
**Project:** ArCode Darija / IDRIS

## 1. The question this roadmap must answer

Is there a real problem that existing tools do not solve well? Can this project build a better or more suitable solution with realistic resources, legitimate data, and measurable quality?

IDRIS should not be judged by the number of languages in its vision or by model size. Its viability depends on a defined problem, users who need a solution, a demonstrated advantage, trustworthy data, and measurable results against alternatives on specific tasks.

## 2. Central hypothesis

**Hypothesis:** A language assistant can be built that performs better on selected Moroccan Darija understanding and generation tasks, respects speaker variation, Arabic script and Arabizi, and code-switching with French, and provides practical value to people or institutions.

This is a testable hypothesis, not an established fact. IDRIS must be compared with strong general-purpose models and available local solutions—not merely with itself before and after training.

## 3. Why the project may be worth pursuing

1. A documented performance gap in Darija for tasks people actually need.
2. Original or clearly licensed data, with community contribution and linguistic review.
3. A measurable advantage over general-purpose models, rather than a renamed or repackaged model.
4. Clear use cases: customer support, informal education, information access, content tools, or communication support.
5. A sustainable path that does not depend on unaffordable compute or data.
6. Governance that protects speaker rights, privacy, and linguistic diversity.

## 4. Why it may not be viable

- General-purpose models may already be sufficient for the target use cases.
- High-quality Darija data with clear rights may be unavailable.
- Fluent speakers and reviewers may not be available to help build data and evaluation.
- An independent model may cost more to train and operate than the value it creates.
- Scope may expand before Darija is validated.
- Performance may be inconsistent across regions and writing systems.
- A social need may exist without reachable users or partners willing to test a solution.

These outcomes justify narrowing the scope, using a hybrid product, or stopping independent model training. They are not personal failures.

## 5. Validation stages and decision gates

Durations are estimates for a solo founder with potential volunteer contributors. They assume no confirmed budget, team, or partnerships. Do not advance automatically; pass each decision gate first.

### V0 — Problem discovery (2 weeks)

**Work**
- Identify 2–3 potential user segments rather than targeting everyone.
- Conduct 15–25 short interviews with Darija speakers from varied backgrounds and regions.
- Ask which tasks current AI tools fail at, how often the problem occurs, and what impact it has.
- Collect use examples with permission and without unnecessary personal data.
- Select three initial testable use cases.

**Deliverables:** An anonymized interview report, ranked problems, and three defined use cases.

**Gate**
- **Continue:** A recurring, clearly described problem exists for a defined group.
- **Pivot:** The need exists but belongs to a narrower task or different user group.
- **Pause:** No important problem emerges or suitable users cannot be reached.

### V1 — Alternatives benchmark (2 weeks)

**Work**
- Prepare 100–200 realistic test cases, isolated from any future training data.
- Test several available general-purpose models on the same tasks under fair settings.
- Evaluate comprehension, naturalness, long-context understanding, dialogue, humor, sarcasm, seriousness, Arabizi, and French code-switching.
- Have fluent speakers judge outputs blindly without knowing model identity.
- Record cost, latency, and limitations for each alternative.

**Deliverables:** An initial benchmark, comparison report, and specific gap list.

**Gate**
- **Continue:** A material, recurring gap remains inadequately addressed by alternatives.
- **Pivot:** Alternatives cover most needs but leave a narrow, addressable gap.
- **Stop independent model training:** No meaningful advantage appears; consider an application, evaluation layer, or routing system over existing models instead.

### V2 — Data feasibility (3–6 weeks)

**Work**
- Audit ownership, contributions, and terms for the existing lexicon.
- Review each source separately for training, redistribution, and commercial-use permissions.
- Write a Darija annotation handbook.
- Build a reviewed pilot of 1,000–2,000 diverse records: short and long sentences, contexts, dialogues, intents, tones, writing variants, and regional variation.
- Distinguish human-authored, translated, and synthetic data.
- Independently review a subset and measure annotator agreement.
- Exclude sources with unclear rights from training.

**Deliverables:** A documented pilot, quality report, rights and consent register, and reproducible dataset version.

**Gate**
- **Continue:** Original or licensed data can be produced with sufficient quality and diversity at sustainable effort.
- **Pivot:** Data exists but is limited in volume or diversity; narrow the task.
- **Pause/stop:** Rights, consent, or quality cannot be resolved.

### V3 — Technical proof (2–3 weeks)

**Work**
- Select a base model after checking license, tokenizer, chat template, and memory requirements.
- Measure the unadapted model on the frozen benchmark.
- Run a very small SFT/QLoRA experiment on approved data.
- Compare with the base model and the strongest general-purpose alternative.
- Measure memory, latency, cost, and stability.
- Check regressions in Arabic, French, and general tasks.
- Have Darija speakers analyze errors.

**Deliverables:** A reproducible experiment report with results, limitations, and costs.

**Gate**
- **Continue:** A practically meaningful improvement appears on target tasks without unacceptable regressions.
- **Pivot:** Gains are limited to one task; turn the project into a specialized model, adapter, or assistive tool.
- **Stop model training:** No repeatable improvement follows reasonable experiments; do not increase spend or model size.

### V4 — User value test (3–4 weeks)

**Work**
- Build a narrow prototype, not a full platform.
- Test it with 20–30 users from the target segment.
- Measure task completion, comprehension quality, rephrasing effort, errors, trust, and return intent.
- Determine whether users prefer IDRIS to available alternatives and why.
- For institutional use cases, run at least one partner pilot before claiming a market.

**Deliverables:** A user study report, error log, and product recommendations.

**Gate**
- **Continue:** Users complete a real task better and return to use the solution.
- **Pivot:** Value is clear for a narrower group or function.
- **Stop/redesign:** No meaningful improvement or repeat use.

### V5 — Investment and expansion decision (1 week)

Write a decision memo answering:
- Which problem has been validated?
- Which users demonstrably need the solution?
- Where does IDRIS outperform alternatives, and by what measure?
- Which data rights have been verified?
- What does operation and maintenance cost?
- What people and skills are required?
- What risks and limitations remain?
- What is the smallest useful release?

**Deliverable:** A clear GO / PIVOT / HOLD / STOP decision.

## 6. Evidence and metrics

| Dimension | Measure | Required evidence |
|---|---|---|
| Need | Frequency and severity | Documented, anonymized interviews |
| Language | Darija comprehension and generation | Blind human evaluation and defined tasks |
| Context | References, long dialogue, tone | Held-out test set |
| Differentiation | Gap versus alternatives | Same-task comparison |
| Data | Rights, quality, diversity | Manifest, review, record-level provenance |
| Technology | Cost, latency, memory | Reproducible runtime logs |
| Adoption | Task completion and return use | Real user pilot |
| Sustainability | Maintenance and resource burden | Realistic resource estimate |

Stars, likes, or lexicon size alone are not evidence of model success. Synthetic examples are not proof of real-world language competence.

## 7. Suggested initial thresholds

These are provisional pilot thresholds to revisit after the first stage, not universal scientific standards:
- 15–25 interviews with potential users.
- 100–200 realistic, isolated test cases.
- 1,000–2,000 approved and reviewed pilot training records, if rights permit.
- Independent human review of results, with disagreements documented.
- Clear, repeatable improvement on target tasks versus baseline; set a numeric threshold after measuring evaluator variance and test difficulty.
- 20–30 users in a limited pilot before scaling.
- No unresolved critical rights or privacy issue.

Meeting a record count is not enough. Quality, diversity, and rights matter more than volume.

## 8. Resource strategy

- Start with free tools and small experiments.
- Do not buy a GPU or server before proving the need.
- Use hosted models for comparison only, while recording privacy terms and costs.
- Use free GPU resources when available, but do not make the plan dependent on them.
- Keep experiments small and stop when time or resource limits are exceeded.
- Do not build a public API or production infrastructure before validating use.

## 9. Decision on later languages

Expansion must not happen merely because it appears in the vision:

- **Amazigh:** Begin feasibility research only after Darija gates pass, with speakers of Tashelhit, Central Atlas Tamazight, and Tarifit involved.
- **Hassaniya:** Run a separate needs, data, reviewer, and partner assessment.
- **Moroccan Sign Language (LSM):** Treat it as a separate multimodal track. Do not start without active leadership and participation from the Deaf community and LSM specialists, and explicit consent for video and data. Its potential social impact is significant, but its cost and complexity differ from a text model.

## 10. Final decision rules

**GO — Continue:** Clear need, measured advantage, legitimate data, successful user testing, and sustainable resources.

**PIVOT — Change direction:** The problem is real, but independent model training is not the best solution. Pivot to Darija evaluation, an application over existing models, a specialized adapter, or open datasets and tools.

**HOLD — Pause:** An opportunity exists, but rights, data, partners, or resources are missing. Define an explicit condition for restarting.

**STOP — Stop:** No validated need, technical advantage, or sustainable lawful data path remains after fair testing.

## 11. Conclusion

We do not need to prove today that IDRIS will become a large multilingual model. We need to prove something smaller and more important: there is a real problem in Darija understanding, IDRIS can solve part of it better than available alternatives, and we can build it with legitimate data and realistic resources.

**Success is not completing the roadmap; success is making the right decision based on evidence.**
