---
repository: "gusye1234/nano-graphrag"
github_id: 833512367
url: "https://github.com/gusye1234/nano-graphrag"
description: "A simple, easy-to-hack GraphRAG implementation"
starred_at: "2024-11-20T06:39:58Z"
language: "Python"
topics: ["gpt", "gpt-4o", "graphrag", "learning-by-doing", "llm", "rag"]
homepage: ""
license: "MIT"
archived: false
---

# gusye1234/nano-graphrag

A simple, easy-to-hack GraphRAG implementation

**GitHub:** https://github.com/gusye1234/nano-graphrag

## README excerpt

> A simple, easy-to-hack GraphRAG implementation
>
>
>
>
> 😭 [GraphRAG](https://arxiv.org/pdf/2404.16130) is good and powerful, but the official [implementation](https://github.com/microsoft/graphrag/tree/main) is difficult/painful to **read or hack**.
> 😊 This project provides a **smaller, faster, cleaner GraphRAG**, while remaining the core functionality(see [benchmark](#benchmark) and [issues](#Issues) ).
> 🎁 Excluding `tests` and prompts,  `nano-graphrag` is about **1100 lines of code**.
> 👌 Small yet [**portable**](#Components)(faiss, neo4j, ollama...), [**asynchronous**](#Async) and fully typed.
> > If you're looking for a multi-user RAG solution for long-term user memory, have a look at this project: [memobase](https://github.com/memodb-io/memobase) :)
> ## Install
> **Install from source** (recommend)
> # clone this repo first
> cd nano-graphrag
> pip install -e .
> **Install from PyPi**
> pip install nano-graphrag
> ## Quick Start
> > [!TIP]
> >
> > **Please set OpenAI API key in environment: `export OPENAI_API_KEY="sk-..."`.**
> > [!TIP]
> > If you're using Azure OpenAI API, refer to the [.env.example](./.env.example.azure) to set your azure openai. Then pass `GraphRAG(...,using_azure_openai=True,...)` to enable.
> > [!TIP]
> > If you're using Amazon Bedrock API, please ensure your credentials are properly set through commands like `aws configure`. Then enable it by configuring like this: `GraphRAG(...,using_amazon_bedrock=True, best_model_id="us.anthropic.claude-3-sonnet-20240229-v1:0", cheap_model_id="us.anthropic.claude-3-haiku-20240307-v1:0",...)`. Refer to an [example script](./examples/using_amazon_bedrock.py).
> > [!TIP]
> >
> > If you don't have any key, check out this [example](./examples/no_openai_key_at_all.py) that using `transformers` and `ollama` . If you like to use another LLM or Embedding Model, check [Advances](#Advances).
> download a copy of A Christmas Carol by Charles Dickens:
> curl https://raw.githubusercontent.com/gusye1234/nano-graphrag/main/tests/mock_data.txt > ./book.txt
> Use the below python snippet:
> from nano_graphrag import GraphRAG, QueryParam
> graph_func = GraphRAG(working_dir="./dickens")
> with open("./book.txt") as f:
> graph_func.insert(f.read())
> # Perform global graphrag search
> print(graph_func.query("What are the top themes in this story?"))
> # Perform local graphrag search (I think is better and more scalable one)
> print(graph_func.query("What are the top themes in this story?", param=QueryParam(mode="local")))
> Next time you initialize a `GraphRAG` from the same `wor

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->
