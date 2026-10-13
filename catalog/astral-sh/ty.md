---
repository: "astral-sh/ty"
github_id: 976731654
url: "https://github.com/astral-sh/ty"
description: "An extremely fast Python type checker and language server, written in Rust."
starred_at: "2026-10-12T14:17:24Z"
language: "Python"
topics: []
homepage: "https://docs.astral.sh/ty/"
license: "MIT"
archived: false
---

# astral-sh/ty

An extremely fast Python type checker and language server, written in Rust.

**GitHub:** https://github.com/astral-sh/ty

## README excerpt

> # ty
> An extremely fast Python type checker and language server, written in Rust.
>
>
>
>
> Type checking the home-assistant project without caching.
>
>
> ty is backed by [Astral](https://astral.sh), the creators of
> [uv](https://github.com/astral-sh/uv) and [Ruff](https://github.com/astral-sh/ruff).
> ty is currently in [beta](#version-policy).
> ## Highlights
> - 10x - 100x faster than mypy and Pyright
> - Comprehensive [diagnostics](https://docs.astral.sh/ty/features/diagnostics/) with rich contextual information
> - Configurable [rule levels](https://docs.astral.sh/ty/rules/), [per-file overrides](https://docs.astral.sh/ty/reference/configuration/#overrides), [suppression comments](https://docs.astral.sh/ty/suppression/), and first-class project support
> - Designed for adoption, with support for [redeclarations](https://docs.astral.sh/ty/features/type-system/#redeclarations) and [partially typed code](https://docs.astral.sh/ty/features/type-system/#gradual-guarantee)
> - [Language server](https://docs.astral.sh/ty/features/language-server/) with code navigation, completions, code actions, auto-import, inlay hints, on-hover help, etc.
> - Fine-grained [incremental analysis](https://docs.astral.sh/ty/features/language-server/#fine-grained-incrementality) designed for fast updates when editing files in an IDE
> - Editor integrations for [VS Code](https://docs.astral.sh/ty/editors/#vs-code), [PyCharm](https://docs.astral.sh/ty/editors/#pycharm), [Neovim](https://docs.astral.sh/ty/editors/#neovim) and more
> - Advanced typing features like first-class [intersection types](https://docs.astral.sh/ty/features/type-system/#intersection-types), advanced [type narrowing](https://docs.astral.sh/ty/features/type-system/#top-and-bottom-materializations), and
> [sophisticated reachability analysis](https://docs.astral.sh/ty/features/type-system/#reachability-based-on-types)
> ## Getting started
> Run ty with [uvx](https://docs.astral.sh/uv/guides/tools/#running-tools) to get started quickly:
> uvx ty check
> Or, check out the [ty playground](https://play.ty.dev) to try it out in your browser.
> To learn more about using ty, see the [documentation](https://docs.astral.sh/ty/).
> ## Installation
> To install ty, see the [installation](https://docs.astral.sh/ty/installation/) documentation.
> To add the ty language server to your editor, see the [editor integration](https://docs.astral.sh/ty/editors/) guide.
> ## Getting help
> If you have questions or want to report a bug, please open an
> [issue](https://github.com/astra

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

ty is a Python type checker and language server written in Rust, distributed by Astral. The README documents a CLI (`ty check`), diagnostics, and language server features such as completions, code actions, and auto-import for editor integration.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "5b7403403ffcc7b70818a018b4610d7e22eba5127417151fe484526ad751b6d7"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "applications"
  ],
  "repository_type": "application",
  "capabilities": [
    "static-analysis",
    "debugging",
    "code-generation"
  ],
  "technologies": [
    "Python",
    "Rust"
  ],
  "summary": "ty is a Python type checker and language server written in Rust, distributed by Astral. The README documents a CLI (`ty check`), diagnostics, and language server features such as completions, code actions, and auto-import for editor integration.",
  "use_cases": [
    "Type-checking Python projects from the command line or in CI",
    "Providing type-aware editing features in VS Code, PyCharm, and Neovim"
  ],
  "limitations": [
    "Described as beta in the README",
    "Performance claims (10x-100x faster than mypy and Pyright) are source-provided and not independently verified here"
  ],
  "suggested_terms": [
    "python type checker",
    "python language server",
    "rust python tooling",
    "mypy alternative",
    "pyright alternative"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
