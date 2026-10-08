---
repository: "storytold/photocraft"
github_id: 1398080271
url: "https://github.com/storytold/photocraft"
description: "An open-source, clean-room reimplementation of Adobe Photoshop in pure Rust"
starred_at: "2026-10-08T11:52:34Z"
language: "Rust"
topics: ["adobe", "adobe-photoshop-2026", "adobe-photoshop-2026-ai", "art", "image-editing", "image-editing-software", "image-editor", "images", "photo-editing", "photoshop", "psd", "rust"]
homepage: "https://getartcraft.com/apps/photocraft"
license: "Apache-2.0"
archived: false
---

# storytold/photocraft

An open-source, clean-room reimplementation of Adobe Photoshop in pure Rust

**GitHub:** https://github.com/storytold/photocraft

## README excerpt

> PhotoCraft
>
> Image editing; an open-source, clean-room reimplementation of Adobe Photoshop, rebuilt in pure Rust.
> Layers, masks, adjustment layers, layer styles, type, vectors, brushes and real PSD files,
> in a native app written entirely in Rust. Open source, offline, and yours.
>
>
>
>
>
>
>
>
>
>
> A caption card with a drop shadow, live type, and Vibrance and Curves adjustment layers, with the Curves editor open.
> The Great Wave off Kanagawa, Katsushika Hokusai, c. 1831
>
> > [!NOTE]
> > **ArtCraft is a community of artists from all walks of life.** Digital, generative, music,
> > games &mdash; if you make things, you're one of us. **[Come say hi on Discord](https://discord.gg/artcraft).**
>
>
>
>
>
>
> 🎛️ Familiar by design
> The menus, shortcuts, panels and tools are where your hands expect them, from ⌘J to ⇧⌘D. If you know Photoshop, you already know PhotoCraft.
>
>
> ⚡ Native and fast
> A GPU compositor on wgpu (Metal, Vulkan, DX12, WebGPU), copy-on-write tiles and multithreaded filters. No Electron, no web view, no waiting.
>
>
> 🗂️ Real PSD files
> Open, edit and save layered Photoshop documents. Re-saving keeps the render of 307 of the 309 psd-tools test files.
>
>
> 🤖 Agent-ready
> Every action is a command, so you can drive the same engine from the UI, the CLI, a JSON control channel or an MCP server.
>
>
>
>
> ## Features
> Every screenshot here is the real app at work on public-domain art, rendered offscreen through its control channel.
>
>
>
>
> Levels and Vibrance adjustment layers, with the live Histogram panel.Impression, Sunrise, Claude Monet, 1872
> Edit without regret
> Adjustment layers keep every edit live. Stack Levels, Curves, Vibrance, Hue/Saturation and a dozen more, mask them to an area, reorder them, or turn them off, and your original pixels never change.
>
> 16 adjustment layers that also apply directly to pixels, including Curves with per-channel editing, Levels with a live histogram, Black &amp; White, Channel Mixer, Gradient Map, Photo Filter, Selective Color and Color Lookup (.cube, .3dl, .look). Plus Shadows/Highlights, Replace Color, Match Color, HDR Toning, Desaturate and Equalize.
>
>
>
> Outer Glow and Stroke on a live type layer, in the Layer Style dialog.Earthrise, William Anders / NASA, 1968
> Styles that sell the shot
> Drop Shadow, Inner Shadow, Outer and Inner Glow, Bevel &amp; Emboss, Satin, Stroke, and Color, Gradient and Pattern Overlay, live on any layer, including type. Patterns come from a library (built-ins, Edit › Define Pattern, .pat import/export) and PSD Patt blocks.
>
> Copy

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

PhotoCraft is an open-source, clean-room reimplementation of Adobe Photoshop written in pure Rust. It provides layers, masks, adjustment layers, layer styles, type, vectors, brushes, and real PSD file support in a native app. Every action is exposed as a command accessible via the UI, CLI, JSON control channel, or MCP server.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "8a75ac037e149e3352764b4582b1eee34da9285f2f47307724a513cf0de1edee"
  },
  "primary_domain": "applications",
  "secondary_domains": [
    "vision-media",
    "developer-tools"
  ],
  "repository_type": "application",
  "capabilities": [
    "media-editing",
    "image-generation",
    "automation",
    "api-integration",
    "document-processing"
  ],
  "technologies": [
    "Rust",
    "wgpu",
    "PSD",
    "MCP",
    "Metal",
    "Vulkan",
    "DX12",
    "WebGPU"
  ],
  "summary": "PhotoCraft is an open-source, clean-room reimplementation of Adobe Photoshop written in pure Rust. It provides layers, masks, adjustment layers, layer styles, type, vectors, brushes, and real PSD file support in a native app. Every action is exposed as a command accessible via the UI, CLI, JSON control channel, or MCP server.",
  "use_cases": [
    "Editing layered PSD documents offline",
    "Applying non-destructive adjustment layers to photos",
    "Driving image editing operations programmatically via CLI or MCP"
  ],
  "limitations": [
    "README does not document complete feature parity with Adobe Photoshop",
    "PSD round-trip fidelity is stated only for 307 of 309 psd-tools test files",
    "Platform-specific GPU backends are listed without detail on support status"
  ],
  "suggested_terms": [
    "photoshop alternative",
    "rust image editor",
    "PSD editor",
    "open source photo editing",
    "layer adjustment rust"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
