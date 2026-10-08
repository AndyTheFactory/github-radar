---
repository: "AndyTheFactory/py-homebox"
github_id: 933346861
url: "https://github.com/AndyTheFactory/py-homebox"
description: "Typed Python client library for Homebox — a self-hosted home inventory manager. Full API coverage with Pydantic v2 validation."
starred_at: "2026-04-27T19:42:59Z"
language: "Python"
topics: ["api-wrapper", "homebox", "inventory-management", "inventory-management-system", "python", "python3"]
homepage: "https://py-homebox.readthedocs.io/en/latest/"
license: "MIT"
archived: false
---

# AndyTheFactory/py-homebox

Typed Python client library for Homebox — a self-hosted home inventory manager. Full API coverage with Pydantic v2 validation.

**GitHub:** https://github.com/AndyTheFactory/py-homebox

## README excerpt

> # py-homebox
> A Python client library for the [Homebox](https://github.com/sysadminsmedia/homebox) REST API.
> Homebox is a self-hosted home inventory management system that lets you track, manage, and organise your belongings.
> **py-homebox** wraps every Homebox v1 endpoint in a clean, typed Python interface backed by [Pydantic](https://docs.pydantic.dev/) models, so you get auto-completion, validation, and inline documentation out of the box.
> ---
> ## Features
> - Full coverage of the Homebox v1 API (entities, entity types, tags, maintenance, imports/exports, notifiers, groups, users, reporting, label-maker, products/barcodes)
> - Pydantic v2 models for all request and response payloads
> - Automatic Bearer-token injection after `login()`
> - Environment-variable based configuration (no hard-coded credentials)
> ---
> ## Installation
> Install from PyPI:
> pip install homebox
> Or with [uv](https://docs.astral.sh/uv/):
> uv add homebox
> ---
> ## Compatibility
> version 0.6.0 is compatible with Homebox v0.26.0 API.
> version 0.5.0 is compatible with Homebox v0.25.0 API.
> version 0.4.0 is compatible with Homebox v0.24.0 API.
> version 0.3.0 is compatible with Homebox v0.23.0 API.
> version 0.2.0 is compatible with Homebox v0.22.0 API.
> version 0.1.0 is compatible with Homebox v0.21.0 API.
> For newer additions to the Homebox API, we will release updates to this client library.
> ---
> ## Environment variables
> The client reads two optional environment variables so that credentials are never hard-coded in your scripts:
> | Variable        | Required | Description                                                          |
> |-----------------|----------|----------------------------------------------------------------------|
> | `HOMEBOX_URL`   | **Yes**  | Base URL of the Homebox API (e.g. `https://demo.homebox.software/api`) |
> | `HOMEBOX_TOKEN` | No       | Pre-obtained Bearer token. Omit this and call `client.login()` instead. |
> Set them in your shell before running your script:
> export HOMEBOX_URL="https://demo.homebox.software/api"
> export HOMEBOX_TOKEN="your-bearer-token"   # optional
> Or store them in a `.env` file and load it with a tool such as [python-dotenv](https://pypi.org/project/python-dotenv/):
> from dotenv import load_dotenv
> load_dotenv()   # reads .env into os.environ
> from homebox import HomeboxClient
> client = HomeboxClient()   # picks up HOMEBOX_URL and HOMEBOX_TOKEN automatically
> ---
> ## Quick start
> ### Authenticate with environment variables
> import os
> from homebox import HomeboxClient
> os.enviro

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->
