---
repository: "NationalSecurityAgency/ghidra"
github_id: 173228436
url: "https://github.com/NationalSecurityAgency/ghidra"
description: "Ghidra is a software reverse engineering (SRE) framework"
starred_at: "2026-10-25T19:39:12Z"
language: "Java"
topics: ["disassembler", "reverse-engineering", "software-analysis"]
homepage: ""
license: "Apache-2.0"
archived: false
---

# NationalSecurityAgency/ghidra

Ghidra is a software reverse engineering (SRE) framework

**GitHub:** https://github.com/NationalSecurityAgency/ghidra

## README excerpt

> # Ghidra Software Reverse Engineering Framework
> Ghidra is a software reverse engineering (SRE) framework created and maintained by the
> [National Security Agency][nsa] Research Directorate. This framework includes a suite of
> full-featured, high-end software analysis tools that enable users to analyze compiled code on a
> variety of platforms including Windows, macOS, and Linux. Capabilities include disassembly,
> assembly, decompilation, graphing, and scripting, along with hundreds of other features. Ghidra
> supports a wide variety of processor instruction sets and executable formats and can be run in both
> user-interactive and automated modes. Users may also develop their own Ghidra extension components
> and/or scripts using Java or Python.
> In support of NSA's Cybersecurity mission, Ghidra was built to solve scaling and teaming problems
> on complex SRE efforts, and to provide a customizable and extensible SRE research platform. NSA has
> applied Ghidra SRE capabilities to a variety of problems that involve analyzing malicious code and
> generating deep insights for SRE analysts who seek a better understanding of potential
> vulnerabilities in networks and systems.
> If you are a U.S. citizen interested in projects like this, to develop Ghidra and other
> cybersecurity tools for NSA to help protect our nation and its allies, consider applying for a
> [career with us][career].
> ## Security Warning
> **WARNING:** There are known security vulnerabilities within certain versions of Ghidra.  Before
> proceeding, please read through Ghidra's [Security Advisories][security] for a better understanding
> of how you might be impacted.
> ## Install
> To install an official pre-built multi-platform Ghidra release:
> * Install [JDK 25 64-bit][jdk]
> * Download a Ghidra [release file][releases]
> - **NOTE:** The official multi-platform release file is named
> `ghidra___.zip` which can be found under the "Assets" drop-down.
> Downloading either of the files named "Source Code" is not correct for this step.
> * Extract the Ghidra release file
> - **NOTE:** Do not extract on top of an existing installation
> * Launch Ghidra: `./ghidraRun` (`ghidraRun.bat` for Windows)
> - or launch [PyGhidra][pyghidra]: `./support/pyghidraRun` (`support\pyghidraRun.bat` for Windows)
> For additional information and troubleshooting tips about installing and running a Ghidra release,
> please refer to the [Getting Started][gettingstarted] document which can be found at the root of a
> Ghidra installation directory.
> ## Build
> To create the latest d

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Ghidra is a software reverse engineering framework from the NSA Research Directorate for analyzing compiled code on Windows, macOS, and Linux. It provides disassembly, decompilation, graphing, and scripting, and can run interactively or in automated modes. Users can extend it with Java or Python scripts and components.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "aa61e00d856d049665df247a45ba8d2568e01a5c006a98d9b90c6dd322cdab83"
  },
  "primary_domain": "security",
  "secondary_domains": [
    "developer-tools"
  ],
  "repository_type": "application",
  "capabilities": [
    "static-analysis",
    "automation"
  ],
  "technologies": [
    "Java",
    "Python",
    "PyGhidra",
    "JDK 25"
  ],
  "summary": "Ghidra is a software reverse engineering framework from the NSA Research Directorate for analyzing compiled code on Windows, macOS, and Linux. It provides disassembly, decompilation, graphing, and scripting, and can run interactively or in automated modes. Users can extend it with Java or Python scripts and components.",
  "use_cases": [
    "Analyzing compiled binaries and malicious code",
    "Reverse engineering software to understand potential vulnerabilities",
    "Automating binary analysis with Java or Python scripts"
  ],
  "limitations": [
    "Requires JDK 25 64-bit to run",
    "Known security vulnerabilities exist in certain versions, per its advisories",
    "The excerpt does not document vulnerability scanning or debugging features"
  ],
  "suggested_terms": [
    "reverse engineering",
    "disassembler",
    "decompiler",
    "binary analysis",
    "software reverse engineering"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
