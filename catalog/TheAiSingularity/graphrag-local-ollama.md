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
