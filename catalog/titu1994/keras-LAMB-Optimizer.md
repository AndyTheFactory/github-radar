---
repository: "titu1994/keras-LAMB-Optimizer"
github_id: 179419246
url: "https://github.com/titu1994/keras-LAMB-Optimizer"
description: "Implementation of the LAMB optimizer for Keras from the paper \"Reducing BERT Pre-Training Time from 3 Days to 76 Minutes\" "
starred_at: "2019-07-09T21:11:23Z"
language: "Python"
topics: []
homepage: ""
license: "MIT"
archived: false
---

# titu1994/keras-LAMB-Optimizer

Implementation of the LAMB optimizer for Keras from the paper "Reducing BERT Pre-Training Time from 3 Days to 76 Minutes" 

**GitHub:** https://github.com/titu1994/keras-LAMB-Optimizer

## README excerpt

> # Keras LAMB Optimizer (Layer-wise Adaptive Moments optimizer for Batch training)
> -----
> Implementation of the LAMB optimizer from the paper [Reducing BERT Pre-Training Time from 3 Days to 76 Minutes](https://arxiv.org/abs/1904.00962).
> Supports large batch training of upto 64k while only using the learning rate as a hyper parameter. Also supports smaller batch sizes without any change in other hyper parameters.
> # Usage
> from keras_lamb import LAMBOptimizer
> optimizer = LAMBOptimizer(0.001, weight_decay=0.01)
> model.compile(optimizer, ...)
> # Requirements
> - Keras 2.2.4+
> - Tensorflow 1.13+

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Provides a Keras implementation of the LAMB (Layer-wise Adaptive Moments optimizer for Batch training) optimizer, based on the paper "Reducing BERT Pre-Training Time from 3 Days to 76 Minutes". The README states it supports large-batch training up to 64k using only the learning rate as a key hyperparameter.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "ae8cc1c93a28bfe259c9261511cae05056ebe0a4cfabfbe34978b3fa8fbced04"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "scientific-computing"
  ],
  "repository_type": "library",
  "capabilities": [
    "model-training",
    "fine-tuning"
  ],
  "technologies": [
    "Python",
    "Keras",
    "TensorFlow"
  ],
  "summary": "Provides a Keras implementation of the LAMB (Layer-wise Adaptive Moments optimizer for Batch training) optimizer, based on the paper \"Reducing BERT Pre-Training Time from 3 Days to 76 Minutes\". The README states it supports large-batch training up to 64k using only the learning rate as a key hyperparameter.",
  "use_cases": [
    "Large-batch neural network training with Keras",
    "Pre-training transformer models such as BERT with reduced training time"
  ],
  "limitations": [
    "Requires Keras 2.2.4+ and TensorFlow 1.13+, which are old versions",
    "No topics or homepage listed; documentation is limited to a short README excerpt"
  ],
  "suggested_terms": [
    "LAMB optimizer",
    "Keras optimizer",
    "large batch training",
    "BERT pre-training",
    "layer-wise adaptive optimizer"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
