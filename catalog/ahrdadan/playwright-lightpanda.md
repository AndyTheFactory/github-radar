---
repository: "ahrdadan/playwright-lightpanda"
github_id: 1108760219
url: "https://github.com/ahrdadan/playwright-lightpanda"
description: "\"Lightpanda + Playwright automation for lightweight hosts” – highlights the core stack and target environments."
starred_at: "2026-10-08T20:15:50Z"
language: "Python"
topics: []
homepage: ""
license: "MIT"
archived: false
---

# ahrdadan/playwright-lightpanda

"Lightpanda + Playwright automation for lightweight hosts” – highlights the core stack and target environments.

**GitHub:** https://github.com/ahrdadan/playwright-lightpanda

## README excerpt

> # Lightpanda + Playwright (Python)
> This project demonstrates how to use [Lightpanda](https://github.com/lightpanda-io/browser) as a lightweight browser backend for a Playwright Python client over the Chrome DevTools Protocol (CDP). The goal is a repeatable workflow that can run inside constrained hosting environments, such as cPanel, without touching the system-wide browser or requiring root privileges.
> ## Requirements
> - A Linux shell (bash) with `curl`, `chmod`, and `ps` available.
> - Python 3.13 or newer; this repository is configured via `pyproject.toml`.
> - Network access to download the Lightpanda binary and to reach the target web site.
> > Running this setup on cPanel strongly recommends doing the work inside your own project folder to avoid interfering with the shared hosting environment.
> ## Setup
> Each command assumes you are inside the folder where this repository lives (the same directory that contains `main.py` and `start_lightpanda.sh`).
> ### 1. Prepare the directory
> mkdir -p ~/mysite/automation
> cd ~/mysite/automation
> Copy this repository into that directory (via `git clone` or file upload) before continuing.
> ### 2. Create a Python virtual environment
> python3 -m venv venv
> source venv/bin/activate
> pip install --upgrade pip
> You can run `make init` from this directory to create the venv and ensure pip is up to date.
> ### 3. Install Python dependencies
> pip install -r requirements.txt
> Or run `make install`, which activates the environment created by `make init` and installs the same requirements.
> ### 4. Download Lightpanda
> curl -L -o lightpanda https://github.com/lightpanda-io/browser/releases/download/nightly/lightpanda-x86_64-linux
> chmod +x lightpanda
> The binary is a single executable and does not require additional system libraries.
> ### 5. Start the Lightpanda browser
> Use the helper script to launch Lightpanda on `127.0.0.1:9222` and keep it running in the background:
> make start
> This runs `./start_lightpanda.sh`, which stops any stale process, launches Lightpanda with `nohup`, waits a couple of seconds for it to warm up, and captures the logs in `lightpanda.log`.
> ### 6. Run the Playwright script
> With Lightpanda running, the Playwright client in `main.py` can connect over CDP. Use:
> make run
> That runs the script with the virtual environment’s Python interpreter and prints the title of `https://www.wikipedia.org/`, a sample set of links, and a screenshot saved as `bukti_sukses.png`.
> ### 7. Stop the browser
> When you are done, stop Lightpanda with:
> make sto

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Demonstrates using Lightpanda as a lightweight browser backend for a Playwright Python client over the Chrome DevTools Protocol. It provides a Makefile and helper scripts to set up, start, run, and stop the browser in constrained hosting environments such as cPanel. Example script loads wikipedia.org, prints its title and links, and saves a screenshot.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "f13eda6919c8ab781e142ad9d49eae51cde978256436ed9e3d1b7bf962175409"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "infrastructure",
    "applications"
  ],
  "repository_type": "template",
  "capabilities": [
    "web-scraping",
    "automation",
    "deployment"
  ],
  "technologies": [
    "Python",
    "Playwright",
    "Lightpanda",
    "Chrome DevTools Protocol",
    "Makefile",
    "Bash",
    "cPanel"
  ],
  "summary": "Demonstrates using Lightpanda as a lightweight browser backend for a Playwright Python client over the Chrome DevTools Protocol. It provides a Makefile and helper scripts to set up, start, run, and stop the browser in constrained hosting environments such as cPanel. Example script loads wikipedia.org, prints its title and links, and saves a screenshot.",
  "use_cases": [
    "Running browser automation on shared or constrained hosts without root access",
    "Connecting Playwright Python scripts to a lightweight CDP browser backend",
    "Capturing page titles, links, and screenshots from web pages"
  ],
  "limitations": [
    "Setup instructions target Linux x86_64 and Python 3.13 or newer",
    "Depends on a nightly Lightpanda binary download from GitHub releases",
    "README describes only a single sample script and does not document broader features"
  ],
  "suggested_terms": [
    "lightpanda",
    "playwright",
    "cdp browser automation",
    "headless browser python",
    "cpanel automation"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
