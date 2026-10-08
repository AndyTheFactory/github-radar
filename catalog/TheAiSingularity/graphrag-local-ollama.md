---
repository: "TheAiSingularity/graphrag-local-ollama"
github_id: 825951497
url: "https://github.com/TheAiSingularity/graphrag-local-ollama"
description: "Local models support for Microsoft's graphrag using ollama (llama3, mistral, gemma2 phi3)- LLM & Embedding extraction"
starred_at: "2024-11-17T22:51:07Z"
language: "Python"
topics: []
homepage: ""
license: "MIT"
archived: false
---

# TheAiSingularity/graphrag-local-ollama

Local models support for Microsoft's graphrag using ollama (llama3, mistral, gemma2 phi3)- LLM & Embedding extraction

**GitHub:** https://github.com/TheAiSingularity/graphrag-local-ollama

## README excerpt

> ## 🤝 Contributing
> **We welcome contributions from the community to help enhance GraphRAG Local Ollama! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more details on how to get involved.**
> Need support for llama integration.
> # 🚀 GraphRAG Local Ollama - Knowledge Graph
> Welcome to **GraphRAG Local Ollama**! This repository is an exciting adaptation of Microsoft's [GraphRAG](https://github.com/microsoft/graphrag), tailored to support local models downloaded using Ollama. Say goodbye to costly OpenAPI models and hello to efficient, cost-effective local inference using Ollama!
> ## 📄 Research Paper
> For more details on the GraphRAG implementation, please refer to the [GraphRAG paper](https://arxiv.org/pdf/2404.16130).
> **Paper Abstract**
> The use of retrieval-augmented generation (RAG) to retrieve relevant information from an external knowledge source enables large language models (LLMs)to answer questions over private and/or previously unseen document collections.However, RAG fails on global questions directed at an entire text corpus, suchas “What are the main themes in the dataset?”, since this is inherently a queryfocused summarization (QFS) task, rather than an explicit retrieval task. PriorQFS methods, meanwhile, fail to scale to the quantities of text indexed by typicalRAG systems. To combine the strengths of these contrasting methods, we proposea Graph RAG approach to question answering over private text corpora that scaleswith both the generality of user questions and the quantity of source text to be indexed. Our approach uses an LLM to build a graph-based text index in two stages:first to derive an entity knowledge graph from the source documents, then to pregenerate community summaries for all groups of closely-related entities. Given aquestion, each community summary is used to generate a partial response, beforeall partial responses are again summarized in a final response to the user. For aclass of global sensemaking questions over datasets in the 1 million token range,we show that Graph RAG leads to substantial improvements over a na¨ıve RAGbaseline for both the comprehensiveness and diversity of generated answers.
> ## 🌟 Features
> - **Local Model Support:** Leverage local models with Ollama for LLM and embeddings.
> - **Cost-Effective:** Eliminate dependency on costly OpenAPI models.
> - **Easy Setup:** Simple and straightforward setup process.
> - **Web UI:** Browser-based interface for indexing, querying, and graph visualization.
> - **5 Query

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

A local-model adaptation of Microsoft's GraphRAG that uses Ollama for LLM and embedding extraction to build knowledge-graph-based indexes and answer questions over document collections. It includes a browser-based web UI for indexing, querying, and graph visualization.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "dca4336a59932e8923c2b6e3d3182d3c72307af3814dd58b40693b985bf2d387"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "research-learning",
    "data-engineering"
  ],
  "repository_type": "library",
  "capabilities": [
    "question-answering",
    "indexing",
    "inference-serving",
    "information-extraction",
    "search-retrieval"
  ],
  "technologies": [
    "Python",
    "Ollama",
    "Microsoft GraphRAG",
    "llama3",
    "mistral",
    "gemma2",
    "phi3"
  ],
  "summary": "A local-model adaptation of Microsoft's GraphRAG that uses Ollama for LLM and embedding extraction to build knowledge-graph-based indexes and answer questions over document collections. It includes a browser-based web UI for indexing, querying, and graph visualization.",
  "use_cases": [
    "Running GraphRAG pipelines without paid OpenAI API access",
    "Querying private document corpora with global sensemaking questions",
    "Visualizing entity knowledge graphs built from source documents"
  ],
  "limitations": [
    "Relies on a local Ollama installation and locally hosted models",
    "README excerpt is incomplete; full feature list and setup details are not verified here"
  ],
  "suggested_terms": [
    "GraphRAG local",
    "Ollama RAG",
    "knowledge graph LLM",
    "local LLM embeddings",
    "graph-based retrieval"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
