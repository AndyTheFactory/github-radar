---
repository: "storytold/wordcraft"
github_id: 1408489772
url: "https://github.com/storytold/wordcraft"
description: "An open-source, clean-room reimplementation of Microsoft Word in pure Rust"
starred_at: "2026-10-11T19:56:24Z"
language: "Rust"
topics: []
homepage: "https://getartcraft.com/apps/wordcraft"
license: "Apache-2.0"
archived: false
---

# storytold/wordcraft

An open-source, clean-room reimplementation of Microsoft Word in pure Rust

**GitHub:** https://github.com/storytold/wordcraft

## README excerpt

> WordCraft
>
> Writing and document design; an open-source, clean-room reimplementation of Microsoft Word, rebuilt in pure Rust.
>
>
> A fast, open-source word processor with the Word workflow you already know: the ribbon, styles,
> tables, track changes, references and mail merge. It reads and writes .docx, runs natively on
> macOS, Windows, Linux and BSD, and in the browser via WebAssembly.
> By the ArtCraft team.
>
>
>
>
>
>
>
>
>
> The Open Studio Handbook, WordCraft's built-in sample: the ribbon, live Styles gallery, rulers and the Navigation pane.
>
> > [!NOTE]
> > **ArtCraft is a community of artists from all walks of life.** Painters, photographers,
> > filmmakers, illustrators, designers, animators, hobbyists, and people who picked up a pencil
> > last week. If you make things, you're one of us. **[Come say hi on Discord](https://discord.gg/artcraft).**
>
>
> ## A tour
> Every screenshot below is WordCraft itself, rendered offscreen by its own UI test harness
> (`cargo run -p wordcraft-ui-egui --example ui_shot`).
>
>
> Review. Track changes, comment balloons in the margin, accept and reject, spelling and grammar as you type.
> References. Tables of contents, footnotes, citations in APA, MLA, Chicago or IEEE, index and captions.
>
>
> Design. Themes, style sets, paragraph spacing, watermarks, page colour and borders.
> Dark mode with formatting marks, and the Insert tab: tables, pictures, shapes, links, headers, footers, fields and symbols.
>
>
> Layout. Drop caps, text wrapping around pictures and shapes, automatic hyphenation, line numbers and page borders.
>
>
> File. Start from a template, open recent documents, edit properties, export to PDF and other formats.
>
>
> ## Why WordCraft
> - **Familiar.** Word's ribbon tabs, groups, shortcuts and behaviour: Enter continues a list,
> Tab demotes it, Ctrl/⌘+B bolds the word under the caret, the Styles gallery previews styles live,
> F4 repeats, F7 checks spelling, F8 extends the selection.
> - **Your files.** Opens and saves .docx (OOXML), and also .odt, .rtf, .html, .md, .tex (LaTeX), .txt; opens Word 97-2003 .doc; exports PDF
> with real, selectable text, links and bookmarks.
> - **Fast.** Paragraph layout is cached, so typing in a 188-page document re-lays it out in about
> 1.4 ms; pages render on demand.
> - **Everywhere.** One Rust codebase for macOS, Windows, Linux, BSD and the web. No Electron, no
> Tauri: native [egui](https://github.com/emilk/egui) on the GPU.
> - **Built for agents.** Every action is a command with an id. The same 422 commands drive the
> ribbon, keyboard

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

WordCraft is an open-source, clean-room reimplementation of Microsoft Word written in pure Rust, featuring a ribbon UI, styles, tables, track changes, and mail merge. It reads and writes .docx and other document formats and exports PDF, running natively on desktop platforms and in the browser via WebAssembly.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "a76fe5cf1fb90ea753ff658454661df4aa4518653cf6520c2cf3468e3cba5e71"
  },
  "primary_domain": "productivity",
  "secondary_domains": [
    "developer-tools"
  ],
  "repository_type": "application",
  "capabilities": [
    "document-processing",
    "media-editing"
  ],
  "technologies": [
    "Rust",
    "egui",
    "WebAssembly",
    "OOXML"
  ],
  "summary": "WordCraft is an open-source, clean-room reimplementation of Microsoft Word written in pure Rust, featuring a ribbon UI, styles, tables, track changes, and mail merge. It reads and writes .docx and other document formats and exports PDF, running natively on desktop platforms and in the browser via WebAssembly.",
  "use_cases": [
    "Creating and editing Word-style documents",
    "Converting documents between .docx, .odt, .rtf, .html, .md, .tex, .txt and PDF"
  ],
  "limitations": [
    "README excerpt describes features only; the full feature set and maturity are not verified from this excerpt",
    "Mail merge and track changes are listed as features but their completeness is not confirmed"
  ],
  "suggested_terms": [
    "word processor",
    "rust document editor",
    "docx",
    "egui",
    "clean-room word"
  ],
  "confidence": "medium"
}
```

<!-- github-radar:enrichment:end -->
