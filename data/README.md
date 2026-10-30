# Data workspace

Large datasets are not committed to Git.

- raw: original source material; restricted and immutable where practical.
- interim: intermediate transformations.
- processed: validated, approved, versioned artifacts.
- external: externally managed files with separate terms.

Before adding a source, create a manifest entry, verify license and training permissions, assess privacy, and assign pending_review, approved, or rejected status. Validate records against schema.json. Keep evaluation data separate from training data.

A public URL is not sufficient evidence of reuse permission.
