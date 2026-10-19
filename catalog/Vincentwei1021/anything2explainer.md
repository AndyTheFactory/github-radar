---
repository: "Vincentwei1021/anything2explainer"
github_id: 1361693766
url: "https://github.com/Vincentwei1021/anything2explainer"
description: "Topic in, narrated explainer video out. A Claude Code / Codex skill that turns any topic into a black-canvas motion-graphics explainer video with TTS voiceover, subtitles and a chapter progress bar. Chinese or English; every frame drawn in code with Remotion."
starred_at: "2026-10-19T11:03:31Z"
language: "TypeScript"
topics: ["agent-skills", "ai-agents", "ai-video", "claude-code", "claude-code-skill", "codex", "edge-tts", "educational-video", "explainer-video", "kokoro", "motion-graphics", "multi-agent", "react", "remotion", "text-to-video", "tts", "typescript", "video-generation"]
homepage: ""
license: "NOASSERTION"
archived: false
---

# Vincentwei1021/anything2explainer

Topic in, narrated explainer video out. A Claude Code / Codex skill that turns any topic into a black-canvas motion-graphics explainer video with TTS voiceover, subtitles and a chapter progress bar. Chinese or English; every frame drawn in code with Remotion.

**GitHub:** https://github.com/Vincentwei1021/anything2explainer

## README excerpt

> # anything2explainer
> **English** | [简体中文](README_ZH.md)
> **Topic in, narrated explainer video out.** anything2explainer is a [Claude Code](https://claude.com/claude-code) / [Codex](https://openai.com/codex) skill that turns any topic into a black-canvas motion-graphics explainer video with TTS voiceover, subtitles and a chapter progress bar, in Chinese or English. Every frame is drawn in code with [Remotion](https://remotion.dev) (React + TypeScript). No stock footage, no generative video model, no frames lifted from anyone else's work.
> It is not a CLI. What ships here is the whole method an AI coding agent needs to finish the film: a compilable Remotion template, a primitives and lighting library, tooling for voiceover / storyboard / rendering / quantitative QC, written style and motion specs, a multi-agent division-of-labour protocol, and one complete reference film as the quality bar.
> **English cut** — *RAG & Knowledge Bases*, 5′02″, 44 lines / 785 words, voiced by kokoro-82m `am_liam` at natural speed:
> https://github.com/user-attachments/assets/e2771c68-a28c-4459-ac5a-a5b685181eeb
> **Chinese cut** — *RAG 与知识库* v2, 4′54″, 44 lines / 1490 characters, dot-field backdrop (`bg: 'dots'`), voiced through the bring-your-own-TTS path (Volcengine TTS 2.0 + forced alignment):
> https://github.com/user-attachments/assets/5c213990-cbba-439e-8371-fbb3aa348e05
> Both cuts share one storyboard and 44 shots; the English cut re-times every shot to the English voiceover. The full paper trail of the original Chinese cut (4′35″, star-field backdrop, 8 build agents in parallel for 40 minutes, two QC rounds) lives in [`examples/rag/`](examples/rag/) (research → narration → storyboard → shot source → QC reports → delivery notes); rendered frames are in [`examples/rag/frames/`](examples/rag/frames/).
> ## What it does
> - **Input**: a topic ("explain vector databases"), or an article / document you want turned into a video. You also pick the length and the language.
> - **Output**: a 1280×720 H.264 MP4 with synchronized voiceover, word-boundary-aligned subtitles, chapter cards, a top HUD and a bottom chapter progress bar, plus the full paper trail (research doc with sources, narration, storyboard, per-shot source code, QC reports).
> - **How**: the agent researches the topic with sources, writes the narration, generates the voiceover and frame-accurate timeline, storyboards every shot, then dispatches parallel build agents that write one Remotion component per shot. QC agents review the ren

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

A Claude Code / Codex skill providing a Remotion (React + TypeScript) template, primitives library, tooling and specs for producing narrated motion-graphics explainer videos from a topic. The repository is not a standalone CLI; it supplies the method and tooling an AI coding agent uses to build the video.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "c90167deea84b3090ca74bbbded63142dd56f31a6c27e9095c095517420670b4"
  },
  "primary_domain": "vision-media",
  "secondary_domains": [
    "developer-tools",
    "ai-ml"
  ],
  "repository_type": "template",
  "capabilities": [
    "media-editing",
    "video-processing",
    "content-generation",
    "workflow-orchestration"
  ],
  "technologies": [
    "TypeScript",
    "React",
    "Remotion",
    "Claude Code",
    "Codex",
    "edge-tts",
    "kokoro-82m"
  ],
  "summary": "A Claude Code / Codex skill providing a Remotion (React + TypeScript) template, primitives library, tooling and specs for producing narrated motion-graphics explainer videos from a topic. The repository is not a standalone CLI; it supplies the method and tooling an AI coding agent uses to build the video.",
  "use_cases": [
    "Producing narrated explainer videos on a topic with an AI coding agent",
    "Reusing a Remotion template and motion/style specs for educational video",
    "Studying a complete reference film and its paper trail (research, narration, storyboard, QC)"
  ],
  "limitations": [
    "Not a CLI; relies on an AI coding agent (Claude Code or Codex) to run the workflow",
    "Depends on external TTS options (kokoro-82m, or bring-your-own TTS such as Volcengine)",
    "License is listed as NOASSERTION, so licensing terms are unclear"
  ],
  "suggested_terms": [
    "remotion explainer video",
    "claude code skill video",
    "motion graphics TTS",
    "agent skill video generation",
    "kokoro tts remotion"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
