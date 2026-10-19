---
repository: "debpalash/VoiceStudio"
github_id: 1206390571
url: "https://github.com/debpalash/VoiceStudio"
description: "VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages."
starred_at: "2026-10-19T11:26:35Z"
language: "Python"
topics: ["ai", "audiobook", "cuda", "dubbing", "elevenlabs-alternative", "huggingface", "local-first", "mlx", "omnivoice-studio", "speech-to-text", "text-to-speech", "transcription", "translate", "tts", "voice-ai", "voice-cloning", "voice-generation", "voicestudio", "workflow"]
homepage: "https://voicestudio.sh"
license: "AGPL-3.0"
archived: false
---

# debpalash/VoiceStudio

VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages.

**GitHub:** https://github.com/debpalash/VoiceStudio

## README excerpt

> VoiceStudio
>
>
> Open-source voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages.
>
>
>
>
> ## Your voice. Your workflow.
> | Create | Produce | Connect |
> | :--- | :--- | :--- |
> | Clone a voice or design your own | Dub videos with timed speech | Local API & MCP for agents |
> | Dictate with a floating widget | Stories, audiobooks & batch jobs | Reusable recipes & watch folders |
> Start with **VoiceStudio** (default, powered by k2-fsa/OmniVoice), or choose another engine. [Features & engine catalog](docs/feature-catalog.md).
> Local workflows run on your hardware. Remote services are optional; usage analytics requires consent.
>
> Explore the workspaces · Clone, dub, design & models
>
>
>
>
>
> Voice cloningVideo dubbing
>
>
>
>
> Voice designLocal models
>
>
> ## Get started
> ### One-command install (macOS / Linux)
> # Latest Electron release
> curl -fsSL https://voicestudio.sh/install | sh
> # A specific published Electron release (replace X.Y.Z)
> curl -fsSL https://voicestudio.sh/install | sh -s -- --version X.Y.Z
> # Build current main and install the desktop app
> curl -fsSL https://voicestudio.sh/install | sh -s -- --main
> # Uninstall the app, keeping your data
> curl -fsSL https://voicestudio.sh/install | sh -s -- --uninstall
> On Windows, run `irm https://voicestudio.sh/install | iex` in PowerShell.
> Release downloads require curl and a SHA-256 tool. `--main` requires Git,
> Node.js 22+, Bun, Rust/Cargo, and platform build tools; see
> [installer prerequisites and behavior](docs/install/script.md).
> The installer preserves your settings, projects, and models. Older versions
> must contain Electron packages; it never falls back to archived Tauri builds.
> Or download from [Releases](https://github.com/debpalash/VoiceStudio/releases/latest) (macOS `.dmg`, Windows `.exe`, Linux `.AppImage` or `.deb`) and follow your platform guide:
> **[macOS](docs/install/macos.md) · [Windows](docs/install/windows.md) · [Linux](docs/install/linux.md) · [Docker](docs/install/docker.md)**
> | Hardware | Support |
> |---|---|
> | NVIDIA GPU (Windows / Linux) | CUDA acceleration |
> | Apple Silicon | Metal (MPS) acceleration |
> | No dedicated GPU (Intel/AMD integrated graphics, older PCs) | Fully usable on the CPU, slower; setup installs the small CPU build of PyTorch (about 5 GB free disk) |
> | Windows on ARM (Snapdragon X etc.) | **Experimental**, validation pending: native ARM64 app, x64 Python backend under emulation, CPU only |
> | Intel Mac | App UI only; connect to a remote backend ([wh

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

VoiceStudio is an open-source, local-first desktop application for voice cloning, voice design, text-to-speech, video dubbing, dictation, transcription, and audiobook creation. It provides a local API and MCP support for agents and runs on NVIDIA CUDA, Apple Metal, or CPU hardware.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "b90e0ef7258c6f9079b7e8b1be6debe19ca3cb3ebf534a151ab7f192ed8bf33b"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "vision-media",
    "productivity"
  ],
  "repository_type": "application",
  "capabilities": [
    "speech-synthesis",
    "speech-recognition",
    "audio-generation",
    "video-processing",
    "api-integration"
  ],
  "technologies": [
    "Python",
    "Electron",
    "Node.js",
    "PyTorch",
    "CUDA",
    "MLX",
    "Docker",
    "Rust"
  ],
  "summary": "VoiceStudio is an open-source, local-first desktop application for voice cloning, voice design, text-to-speech, video dubbing, dictation, transcription, and audiobook creation. It provides a local API and MCP support for agents and runs on NVIDIA CUDA, Apple Metal, or CPU hardware.",
  "use_cases": [
    "Narrating and producing audiobooks from text",
    "Dubbing videos with timed translated speech",
    "Local dictation and transcription without cloud services"
  ],
  "limitations": [
    "Windows on ARM support is experimental and CPU-only",
    "Intel Mac supports only the app UI and requires a remote backend",
    "CPU-only operation is slower and the setup needs about 5 GB of free disk space"
  ],
  "suggested_terms": [
    "voice cloning",
    "text-to-speech",
    "local TTS",
    "video dubbing",
    "ElevenLabs alternative"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
