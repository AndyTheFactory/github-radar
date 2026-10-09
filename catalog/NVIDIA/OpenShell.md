---
repository: "NVIDIA/OpenShell"
github_id: 1166129534
url: "https://github.com/NVIDIA/OpenShell"
description: "OpenShell is the safe, private runtime for autonomous AI agents."
starred_at: "2026-10-09T14:09:51Z"
language: "Rust"
topics: []
homepage: "https://docs.nvidia.com/openshell/latest/"
license: "Apache-2.0"
archived: false
---

# NVIDIA/OpenShell

OpenShell is the safe, private runtime for autonomous AI agents.

**GitHub:** https://github.com/NVIDIA/OpenShell

## README excerpt

> > [!IMPORTANT]
> > **New in OpenShell 0.1.x:** a stable release cadence, new isolation primitives, an expanded extension surface, and new APIs. [Read the 0.1.0 upgrade guide](https://docs.nvidia.com/openshell/latest/upgrade/0-1-0).
> OpenShell is the safe, private runtime for fleets of autonomous AI agents. Agents are most useful when they can read files, install packages, call APIs, and use credentials. OpenShell gives them that capability without giving them unrestricted access to your data, secrets, or network. You declare what each agent can touch in a policy, and OpenShell enforces it.
> ## How It Works
> OpenShell governs what agents can do in two ways: it instruments the kernel to enforce policy on every file access, system call, and network connection at runtime, and it uses formal verification to check what a policy change would allow before it is applied.
> - **Kernel-level enforcement.** Each agent runs in an isolated sandbox. Kernel controls confine which files it can access and which system calls it can make, and every network connection passes through a policy check before it leaves the sandbox. Agents never see real credentials; OpenShell adds them only to requests bound for approved endpoints.
> - **Formally verified policy changes.** Before a policy change is approved, OpenShell uses formal verification to flag risky new access it would grant, such as reaching a new host with credentials or calling a new API method, so those changes wait for human review.
> See [Architecture](https://docs.nvidia.com/openshell/latest/about/architecture) for how the gateway, supervisor, and sandbox fit together.
> ## Quickstart
> You need Linux, macOS on Apple Silicon, or Windows with WSL 2 (experimental), plus Docker, Podman, or host virtualization. See the [Support Matrix](https://docs.nvidia.com/openshell/latest/about/support-matrix) for details.
> curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh
> openshell sandbox create --name demo
> The installer sets up the CLI and a local gateway. The default sandbox image is minimal Ubuntu with no agent installed. To run a real agent, follow [Run Your First Agent](https://docs.nvidia.com/openshell/latest/about/run-your-first-agent): it runs OpenCode against a free OpenRouter model and shows how to approve new access as the agent needs it.
> ## Explore Further
> - [Sandboxes](https://docs.nvidia.com/openshell/latest/how-it-works/sandboxes/overview): images, runtimes, GPUs, and lifecycle.
> - [Policies](https:

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

OpenShell is a runtime that runs autonomous AI agents in isolated sandboxes, enforcing policies on file access, system calls, and network connections. It also uses formal verification to flag risky policy changes before approval. The README describes a CLI installer that sets up a local gateway.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "ff165285104261720e747ec3903351bf3fc1f9c5a90082507e19f9e104f1e60e"
  },
  "primary_domain": "security",
  "secondary_domains": [
    "infrastructure",
    "developer-tools"
  ],
  "repository_type": "application",
  "capabilities": [
    "authorization",
    "virtualization",
    "containerization",
    "monitoring",
    "networking"
  ],
  "technologies": [
    "Rust",
    "Docker",
    "Podman",
    "Linux kernel controls",
    "WSL 2",
    "OpenCode",
    "OpenRouter"
  ],
  "summary": "OpenShell is a runtime that runs autonomous AI agents in isolated sandboxes, enforcing policies on file access, system calls, and network connections. It also uses formal verification to flag risky policy changes before approval. The README describes a CLI installer that sets up a local gateway.",
  "use_cases": [
    "Confining AI agents' file, system call, and network access with declarative policies",
    "Injecting credentials only into requests bound for approved endpoints",
    "Reviewing risky policy changes before they are applied"
  ],
  "limitations": [
    "Requires Linux, macOS on Apple Silicon, or Windows with WSL 2 (experimental), plus Docker, Podman, or host virtualization",
    "Default sandbox image is minimal Ubuntu with no agent installed",
    "README excerpt is truncated, so full feature set is not verified"
  ],
  "suggested_terms": [
    "AI agent sandbox",
    "agent policy enforcement",
    "kernel-level sandboxing",
    "autonomous agent runtime",
    "OpenShell"
  ],
  "confidence": "medium"
}
```

<!-- github-radar:enrichment:end -->
