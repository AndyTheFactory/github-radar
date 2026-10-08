---
repository: "jwzhanggy/Graph-Bert"
github_id: 235061629
url: "https://github.com/jwzhanggy/Graph-Bert"
description: "Source code of Graph-Bert"
starred_at: "2021-02-22T21:58:59Z"
language: "Python"
topics: []
homepage: ""
license: "MIT"
archived: false
---

# jwzhanggy/Graph-Bert

Source code of Graph-Bert

**GitHub:** https://github.com/jwzhanggy/Graph-Bert

## README excerpt

> # Graph-Bert
> - Depending on your transformer toolkit versions, the transformer import code may need to be adjusted, like as follows:
> + from transformers.modeling_bert import BertPreTrainedModel, BertPooler
> + --> from transformers.models.bert.modeling_bert import BertPreTrainedModel, BertPooler
> - (Please check your transformer toolikt, and update the import code accordingly.)
> ## Graph-Bert: Only Attention is Needed for Learning Graph Representations
> Paper URL at IFM Lab: http://www.ifmlab.org/files/paper/graph_bert.pdf
> Paper URL at arXiv: https://arxiv.org/abs/2001.05140
> ### Graph-Bert Paper List
> A list of the latest research papers on graph-bert can be found via the following link
> Page List URL: https://github.com/jwzhanggy/graph_bert_work
> ### Two other papers are helpful for readers to follow the ideas in this paper and the code
> (1) SEGEN: Sample-Ensemble Genetic Evolutional Network Model https://arxiv.org/abs/1803.08631
> (2) GResNet: Graph Residual Network for Reviving Deep GNNs from Suspended Animation https://arxiv.org/abs/1909.05729
> ### Graph Neural Networks from IFM Lab
> The latest graph neural network models proposed by IFM Lab can be found via the following link
> IFM Lab GNNs: https://github.com/jwzhanggy/IFMLab_GNN
> ### References
> @article{zhang2020graph,
> title={Graph-Bert: Only Attention is Needed for Learning Graph Representations},
> author={Zhang, Jiawei and Zhang, Haopeng and Xia, Congying and Sun, Li},
> journal={arXiv preprint arXiv:2001.05140},
> year={2020}
> }
> ************************************************************************************************
> ## How to run the code?
> ### To run a script, you can just use command line: python3 script_name.py
> After downloading the code, you can run
> python3 script_3_fine_tuning.py
> directly for node classification. It seems the random seed cannot control the randomness in parameter initialization in transformer, we suggest to run the code multiple times to get good scores.
> ### What are the scripts used for?
> (1) The Graph-Bert model takes (a) node WL code, (b) intimacy based subgraph batch, (c) node hop distance as the prior inputs. These can be computed with the script_1_preprocess.py.
> (2) Pre-training of Graph-Bert based on node attribute reconstruction and graph structure recovery is provided by script_2_pre_train.py.
> (3) Please check the script_3_fine_tuning.py as the entry point to run the model on node classification and graph clustering.
> (4) script_4_evaluation_plots.py is used for plots drawing and re

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Source code for Graph-Bert, a transformer-based model that learns graph node representations using attention alone. The repository includes scripts for preprocessing, pre-training, fine-tuning for node classification and graph clustering, and evaluation plots.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "d463cf7a58b63f19b340accf174527eec17975c0ca228143a6ce7a59761ec5a8"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "research-learning"
  ],
  "repository_type": "research",
  "capabilities": [
    "model-training",
    "data-transformation",
    "model-evaluation"
  ],
  "technologies": [
    "Python",
    "Transformers",
    "PyTorch"
  ],
  "summary": "Source code for Graph-Bert, a transformer-based model that learns graph node representations using attention alone. The repository includes scripts for preprocessing, pre-training, fine-tuning for node classification and graph clustering, and evaluation plots.",
  "use_cases": [
    "Node classification on graphs",
    "Graph clustering",
    "Research reproduction of Graph-Bert experiments"
  ],
  "limitations": [
    "Requires adjusting transformers import paths depending on toolkit version",
    "Random seed does not fully control transformer parameter initialization, so multiple runs are suggested",
    "README excerpt is truncated; full scope not verified"
  ],
  "suggested_terms": [
    "graph transformer",
    "graph neural network",
    "node classification",
    "graph representation learning",
    "Graph-Bert"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
