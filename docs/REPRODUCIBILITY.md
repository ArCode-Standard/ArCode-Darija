# Reproducibility

Every experiment must be reproducible from a recorded configuration and
immutable inputs.

## Required record

- experiment ID and UTC start/end timestamps;
- base model identifier and immutable revision;
- model license review and permitted use;
- tokenizer and chat-template revision;
- dataset manifest version, split counts, and SHA-256 hashes;
- preprocessing command and repository commit;
- random seed and complete training configuration;
- Python, PyTorch, Transformers, PEFT, CUDA, and driver versions as applicable;
- hardware model, accelerator memory, peak memory, runtime, and throughput;
- training/validation curves, evaluation protocol, and known limitations.

## Release gate

Do not publish a checkpoint as an IDRIS release until its provenance, license,
dataset rights, evaluation results, limitations, and reproducibility record
have been reviewed. Configuration templates are not evidence that training ran.
