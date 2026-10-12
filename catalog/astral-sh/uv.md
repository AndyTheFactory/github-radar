---
repository: "astral-sh/uv"
github_id: 699532645
url: "https://github.com/astral-sh/uv"
description: "An extremely fast Python package and project manager, written in Rust."
starred_at: "2026-10-12T14:17:32Z"
language: "Rust"
topics: ["packaging", "python", "resolver", "uv"]
homepage: "https://docs.astral.sh/uv"
license: "Apache-2.0"
archived: false
---

# astral-sh/uv

An extremely fast Python package and project manager, written in Rust.

**GitHub:** https://github.com/astral-sh/uv

## README excerpt

> # uv
> An extremely fast Python package and project manager, written in Rust.
>
>
>
>
>
>
> Installing Trio's dependencies with a warm cache.
>
> ## Highlights
> - A single tool to replace `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, `virtualenv`, and
> more.
> - [10-100x faster](https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md) than `pip`.
> - Provides [comprehensive project management](#projects), with a
> [universal lockfile](https://docs.astral.sh/uv/concepts/projects/layout#the-lockfile).
> - [Runs scripts](#scripts), with support for
> [inline dependency metadata](https://docs.astral.sh/uv/guides/scripts#declaring-script-dependencies).
> - [Installs and manages](#python-versions) Python versions.
> - [Runs and installs](#tools) tools published as Python packages.
> - Includes a [pip-compatible interface](#the-pip-interface) for a performance boost with a familiar
> CLI.
> - Supports Cargo-style [workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces) for
> scalable projects.
> - Disk-space efficient, with a [global cache](https://docs.astral.sh/uv/concepts/cache) for
> dependency deduplication.
> - Installable without Rust or Python via `curl` or `pip`.
> - Supports macOS, Linux, and Windows.
> uv is backed by [Astral](https://astral.sh), the creators of
> [Ruff](https://github.com/astral-sh/ruff) and [ty](https://github.com/astral-sh/ty).
> ## Installation
> Install uv with our standalone installers:
> # On macOS and Linux.
> curl -LsSf https://astral.sh/uv/install.sh | sh
> # On Windows.
> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
> Or, from [PyPI](https://pypi.org/project/uv/):
> # With pip.
> pip install uv
> # Or pipx.
> pipx install uv
> If installed via the standalone installer, uv can update itself to the latest version:
> uv self update
> See the [installation documentation](https://docs.astral.sh/uv/getting-started/installation/) for
> details and alternative installation methods.
> ## Documentation
> uv's documentation is available at [docs.astral.sh/uv](https://docs.astral.sh/uv).
> Additionally, the command line reference documentation can be viewed with `uv help`.
> ## Features
> ### Projects
> uv manages project dependencies and environments, with support for lockfiles, workspaces, and more,
> similar to `rye` or `poetry`:
> $ uv init example
> Initialized project `example` at `/home/user/example`
> $ cd example
> $ uv add ruff
> Creating virtual environment at: .venv
> Resolved 2 packages in 170ms
> Built example @ file:///home/user/example
> Prepared 2 packages in 627ms
> In

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

uv is a Python package and project manager written in Rust, providing dependency resolution, lockfiles, virtual environments, and Python version management. It is documented as a replacement for tools such as pip, pip-tools, pipx, poetry, pyenv, twine, and virtualenv.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "a2dd7b62cf77f7b9815e59dc942f6cfe4c9a36176aa47003f257d57531577db5"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "infrastructure"
  ],
  "repository_type": "application",
  "capabilities": [
    "automation",
    "workflow-orchestration",
    "containerization"
  ],
  "technologies": [
    "Rust",
    "Python"
  ],
  "summary": "uv is a Python package and project manager written in Rust, providing dependency resolution, lockfiles, virtual environments, and Python version management. It is documented as a replacement for tools such as pip, pip-tools, pipx, poetry, pyenv, twine, and virtualenv.",
  "use_cases": [
    "Installing and resolving Python package dependencies",
    "Managing Python projects with lockfiles and workspaces",
    "Running scripts and installing Python-published tools"
  ],
  "limitations": [
    "Only documented features are listed; performance claims are not independently verified here",
    "Scope is limited to Python packaging and project management"
  ],
  "suggested_terms": [
    "python package manager",
    "python dependency resolver",
    "uv lockfile",
    "python virtualenv tool",
    "rust python tooling"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
