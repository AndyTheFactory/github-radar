---
repository: "CamouChat-Team/camouchat-whatsapp"
github_id: 1208731872
url: "https://github.com/CamouChat-Team/camouchat-whatsapp"
description: "WhatsApp plugin for camouchat."
starred_at: "2026-07-28T14:40:00Z"
language: "Python"
topics: ["pytest", "sqlalchemy-python", "whatsapp-automation"]
homepage: ""
license: "MIT"
archived: false
---

# CamouChat-Team/camouchat-whatsapp

WhatsApp plugin for camouchat.

**GitHub:** https://github.com/CamouChat-Team/camouchat-whatsapp

## README excerpt

> # CamouChat WhatsApp 🟢
> > [!IMPORTANT]
> > 🦊 **This is the CamouChat WhatsApp Plugin Repository.**
> > If you are looking for the main CamouChat project or full ecosystem documentation, please visit our **[Central Repository](https://github.com/CamouChat-Team/CamouChat)**.
> High-stealth WhatsApp automation plugin for the CamouChat ecosystem. Built on top of `camouchat-browser` and `WA-JS`, providing a structured, API-driven pipeline for multi-account automation with end-to-end encrypted message storage.
>
>
> > [!WARNING]
> > This package requires a **one-time binary fetch** for the underlying Camoufox browser engine after installation. See [Setup](#setup) below.
> ## Key Features
> - **WA-JS Integration**: Uses the internal WhatsApp Web API via `wa-js` — not fragile DOM selectors.
> - **Multi-Account Isolation**: Each account runs in a sandboxed profile with isolated cookies, storage, and fingerprints.
> - **E2E Encryption**: All stored messages are encrypted at rest using AES-256-GCM.
> - **Async-First**: Fully `asyncio`-native for high-throughput multi-session workloads.
> - **Humanized Behavior**: Mouse movements, typing cadence, and delays mimic organic user behavior.
> ## Installation
> ### Using `uv` (Recommended)
> uv add camouchat-whatsapp "camoufox[geoip]"
> ### Using `pip`
> pip install camouchat-whatsapp "camoufox[geoip]"
> ## Setup
> > [!WARNING]
> > `uv sync` / `pip install` alone are **not enough**. You must fetch the Camoufox browser binary separately.
> ### With `uv`
> uv run python -m camoufox fetch
> ### With `pip`
> python -m camoufox fetch
> This downloads the latest hardened Firefox binary used internally by [Camoufox](https://camoufox.com/).
> ## Quick Start
> import asyncio
> import base64
> import os
> from camouchat_browser import BrowserConfig, CamoufoxBrowser, ProfileManager
> from camouchat_core import Platform, KeyManager, MessageDecryptor, MediaType
> from camouchat_whatsapp import (
> Login,
> WapiSession,
> InteractionController,
> MediaController,
> MessageModelAPI,
> FileTyped,
> RegistryConfig,
> on_newMsg,
> )
> async def main():
> # 1. Profile
> pm = ProfileManager()
> profile = pm.create_profile(platform=Platform.WHATSAPP, profile_id="work")
> # 2. Browser
> config = BrowserConfig.from_dict({"platform": Platform.WHATSAPP, "headless": False})
> browser = CamoufoxBrowser(config=config, profile=profile)
> page = await browser.get_page()
> # 3. Login (reuses saved session automatically)
> login = Login(page=page, profile=profile)
> await login.login(method=0)
> # 4. API Controllers
> wapi = WapiSession(page=page)
> interaction =

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

A Python plugin for the CamouChat ecosystem that automates WhatsApp Web via the wa-js internal API, running multiple isolated browser profiles. It stores messages encrypted at rest with AES-256-GCM and requires a separate Camoufox binary fetch after installation.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "19812f0c6770fcb3c9a1ace82ab6d67012208b911933528e7b22e939cf08765f"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "security"
  ],
  "repository_type": "library",
  "capabilities": [
    "automation",
    "api-integration",
    "authentication",
    "storage"
  ],
  "technologies": [
    "Python",
    "asyncio",
    "Camoufox",
    "WA-JS",
    "SQLAlchemy",
    "pytest",
    "AES-256-GCM",
    "uv"
  ],
  "summary": "A Python plugin for the CamouChat ecosystem that automates WhatsApp Web via the wa-js internal API, running multiple isolated browser profiles. It stores messages encrypted at rest with AES-256-GCM and requires a separate Camoufox binary fetch after installation.",
  "use_cases": [
    "Automating multi-account WhatsApp Web workflows in isolated browser profiles",
    "Storing WhatsApp messages with encryption at rest",
    "Building asyncio-based WhatsApp automation pipelines"
  ],
  "limitations": [
    "Requires a separate one-time Camoufox browser binary fetch after installation",
    "Depends on the underlying camouchat-browser and WA-JS components and the main CamouChat ecosystem",
    "Relies on WhatsApp Web's internal API, which may change without notice"
  ],
  "suggested_terms": [
    "whatsapp automation python",
    "camoufox whatsapp",
    "wa-js python",
    "multi-account browser automation",
    "encrypted message storage"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
