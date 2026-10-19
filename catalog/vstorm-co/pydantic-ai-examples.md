---
repository: "vstorm-co/pydantic-ai-examples"
github_id: 1125477819
url: "https://github.com/vstorm-co/pydantic-ai-examples"
description: "A community-maintained collection of Pydantic AI examples."
starred_at: "2026-10-19T11:42:42Z"
language: "Python"
topics: ["ai-agents", "anthropic", "llm", "openai", "pydantic", "pydantic-ai", "vstorm"]
homepage: "https://vstorm-co.github.io/pydantic-ai-examples/"
license: "MIT"
archived: false
---

# vstorm-co/pydantic-ai-examples

A community-maintained collection of Pydantic AI examples.

**GitHub:** https://github.com/vstorm-co/pydantic-ai-examples

## README excerpt

> # PydanticAI Examples
> A comprehensive collection of examples demonstrating PydanticAI framework capabilities, from basic model requests to advanced document processing with schema validation.
> ## Prerequisites
> ### System Requirements
> - Python 3.13+
> - `uv` package manager
> ### Environment Setup
> # Install dependencies
> uv sync
> # Create .env file with your API key
> echo "OPENAI_API_KEY=your-key-here" > .env
> **Note**: Most examples use OpenAI's GPT-5.1. Ensure your API key has appropriate permissions and sufficient quota.
> ## Learning Path
> **Recommended order for learning PydanticAI**:
> 1. **[Direct Model Requests](direct_model_request/)** - Understand basic LLM API calls
> 2. **[Temperature](temperature/)** - Understand model parameters
> 3. **[Reasoning Effort](reasoning_effort/)** - Uncover how the reasoning effort may change the model's output
> 4. **[Basic Sentiment](basic_sentiment/)** - Learn structured outputs with Pydantic
> 5. **[Dynamic Classification](dynamic_classification/)** - Runtime schema generation
> 6. **[Bielik](bielik_example/)** - Local models and tools
> 7. **[History Processor](history_processor/)** - Multi-turn conversations
> 8. **[OCR Parsing](ocr_parsing_demo/)** - Complex real-world document processing
> ## Examples Overview
> ### 1. Direct Model Requests
> **Location**: `direct_model_request/`
> Demonstrates direct model API calls without using Agents.
> - Basic synchronous model requests using gpt-5.2
> - When to use direct API vs Agents
> - Simple text prompt handling
> [View Example →](direct_model_request/)
> ### 2. Model Parameters
> **Location**: `temperature/`
> Control model behavior using temperature.
> - Temperature effects on creativity vs consistency
> - Practical configuration examples
> - Use case recommendations
> [View Example →](temperature/)
> ### 3. Reasoning Effort
> **Location**: `reasoning_effort/`
> Demonstrates reasoning_effort parameter for gpt-5.2.
> - Control depth of internal reasoning
> - Complex problem-solving examples
> - Trade-off between accuracy and latency
> [View Example →](reasoning_effort/)
> ### 4. Basic Sentiment Classification
> **Location**: `basic_sentiment/`
> Fixed 3-class sentiment analysis (positive/negative/neutral) with structured outputs.
> - Fixed Literal types defined at design time
> - Simple accuracy evaluation
> - Type-safe results with Pydantic validation
> [View Example →](basic_sentiment/)
> ### 5. Dynamic Classification
> **Location**: `dynamic_classification/`
> Runtime-adaptable classification that handles any number of classes dynamically.
> - Dynamic

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->
