---
repository: "DUTANGx/TF2-albert-NER"
github_id: 225274516
url: "https://github.com/DUTANGx/TF2-albert-NER"
description: "wrapping albert via bert-for-tf2, implementing NER task"
starred_at: "2020-02-16T23:03:05Z"
language: "Python"
topics: []
homepage: ""
license: null
archived: false
---

# DUTANGx/TF2-albert-NER

wrapping albert via bert-for-tf2, implementing NER task

**GitHub:** https://github.com/DUTANGx/TF2-albert-NER

## README excerpt

> # TF2-albert-NER
> wrapping albert as tfkeras layer via [bert-for-tf2](https://github.com/kpe/bert-for-tf2), implemented NER task
> F1 on MSRA: 95-99%. F1 on Boson: 80-85%.
> Features 2019-12-20: Added Boson data(processed as BIO format).
> Features 2019-12-16: Added Bi-LSTM.
> Features 2019-12-10: Added CRF model training on multiple GPUs.
> To use:
> 1. modify the model_dir which contains the albert weight and config.json.
> 2. initialize model, if first use, please load_pretrained, otherwise you could directly use load(). The trained weights(in model_dir/training_checkpoints, which will be created automatically while training) will be loaded.
> 3. follow the script in model_crf to do NER prediction or create a dockerservice then call(in tf2service).

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Wraps ALBERT as a tf.keras layer using bert-for-tf2 and implements named entity recognition (NER) with CRF and Bi-LSTM models. The README reports F1 scores of 95-99% on MSRA and 80-85% on Boson, and mentions a Docker service for prediction.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "25c278cffa6413f4f49a346461c75c76020adf100d71d3492eb648bbb441ac45"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [],
  "repository_type": "library",
  "capabilities": [
    "information-extraction",
    "model-training",
    "inference-serving",
    "containerization"
  ],
  "technologies": [
    "Python",
    "TensorFlow",
    "Keras",
    "ALBERT",
    "bert-for-tf2",
    "Bi-LSTM",
    "CRF",
    "Docker"
  ],
  "summary": "Wraps ALBERT as a tf.keras layer using bert-for-tf2 and implements named entity recognition (NER) with CRF and Bi-LSTM models. The README reports F1 scores of 95-99% on MSRA and 80-85% on Boson, and mentions a Docker service for prediction.",
  "use_cases": [
    "Named entity recognition on the MSRA and Boson datasets",
    "Training CRF-based NER models on multiple GPUs",
    "Serving NER predictions through a Docker service"
  ],
  "limitations": [
    "Reported F1 scores come from the README and are not independently verified",
    "Requires manually setting model_dir to ALBERT weights and config.json",
    "No license, topics, or dependency versions are documented"
  ],
  "suggested_terms": [
    "named entity recognition",
    "ALBERT",
    "tf.keras NER",
    "bert-for-tf2",
    "BIO sequence labeling"
  ],
  "confidence": "medium"
}
```

<!-- github-radar:enrichment:end -->
