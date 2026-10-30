# Training configuration

This directory contains versioned experiment configuration examples. No model
checkpoint, dataset, or training run is implied by a configuration file.

Before a training run, record:
- the exact base model ID and immutable revision;
- the model license and permitted training/redistribution uses;
- dataset manifest IDs and content hashes;
- tokenizer and chat-template revision;
- seed, sequence length, batch size, optimizer, learning rate, and adapter settings;
- hardware, software versions, run logs, and evaluation results.

Do not put credentials, private datasets, or personal data in Git.
