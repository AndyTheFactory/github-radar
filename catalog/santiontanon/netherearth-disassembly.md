---
repository: "santiontanon/netherearth-disassembly"
github_id: 478552652
url: "https://github.com/santiontanon/netherearth-disassembly"
description: "Disassembly of the original 1986 Nether Earth ZX Spectrum game"
starred_at: "2026-10-08T20:38:15Z"
language: "HTML"
topics: []
homepage: ""
license: "Apache-2.0"
archived: false
---

# santiontanon/netherearth-disassembly

Disassembly of the original 1986 Nether Earth ZX Spectrum game

**GitHub:** https://github.com/santiontanon/netherearth-disassembly

## README excerpt

> # netherearth-disassembly
> Disassembly of the original 1986 Nether Earth ZX Spectrum game
> Disassembled by Santiago Ontañón
> Files:
> - The main disassembler file is called "netherearth-annotated.asm".
> - The file "netherearth-annotated-data.asm" contains the graphic data of the game.
> - You can assembler the game back to a binary using the build.sh file included in the repo. You do not need any additional assembler, as I include mdl.jar in the repo, that allows you to assemble the game. MDL ( https://github.com/santiontanon/mdlz80optimizer ) is my own assembler optimizer, which also has assembly/disassembly capabilities. However, if you happen to plan to use the Nether Earth code-base and edit it, I would recommend you using another assembler. MDL is much slower at assembling than other assemblers like Glass or sjasmplus, since it does many other things, and hence it might not be ideal for heavy development.
> - I also include an html rendered version of the source code ( netherearth-annotated.html ), that might be easier to see than the raw .asm file. The html file also has .png files to illustrate al the graphic data (scroll all the way to the bottom once you open it).
> All the symbol names and comments in this file are my own interpretation of the original source code, they could be wrong. So, take them all with a grain of salt! And if you see any errors, please report!

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Provides an annotated disassembly of the 1986 Nether Earth ZX Spectrum game, including source files, graphic data, and an HTML-rendered version. The repository includes a build script and bundled MDL assembler to reassemble the game binary.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "6b0b5dc7743f565afd064654124a2babf42e22f85fe972cdf3667644cab46032"
  },
  "primary_domain": "games",
  "secondary_domains": [
    "research-learning"
  ],
  "repository_type": "resource",
  "capabilities": [
    "game-development"
  ],
  "technologies": [
    "Z80 Assembly",
    "ZX Spectrum",
    "MDL Z80 Optimizer",
    "HTML",
    "Shell"
  ],
  "summary": "Provides an annotated disassembly of the 1986 Nether Earth ZX Spectrum game, including source files, graphic data, and an HTML-rendered version. The repository includes a build script and bundled MDL assembler to reassemble the game binary.",
  "use_cases": [
    "Studying the original Nether Earth ZX Spectrum game code",
    "Reassembling the game binary from the annotated source",
    "Reviewing graphic data of the game via the rendered HTML documentation"
  ],
  "limitations": [
    "Symbol names and comments are the author's interpretation and may be inaccurate",
    "MDL assembler is slow and not ideal for heavy development",
    "Topics list is empty and no homepage is provided"
  ],
  "suggested_terms": [
    "ZX Spectrum disassembly",
    "Nether Earth",
    "Z80 assembly",
    "retro game source",
    "annotated assembly"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
