---
repository: "mwstowe/foff-milter"
github_id: 1023357755
url: "https://github.com/mwstowe/foff-milter"
description: "Sendmail milter to help combat spam"
starred_at: "2026-05-22T22:40:16Z"
language: "Rust"
topics: []
homepage: ""
license: "MIT"
archived: false
---

# mwstowe/foff-milter

Sendmail milter to help combat spam

**GitHub:** https://github.com/mwstowe/foff-milter

## README excerpt

> # FOFF Milter v0.10.6
> A comprehensive, enterprise-grade email security platform written in Rust featuring intelligent threat detection, modular rulesets, and zero-configuration deployment.
> ## 🎯 **Production Ready - 100% Test Compliance & Zero False Positives**
> **Latest Achievement**: Production-ready v0.8.55 with hidden text (Bayesian poisoning) detection, Marriott brand impersonation, and dependency updates. Detects large blocks of conversational text hidden via CSS (display:none) — a common spam evasion technique. Fixed National Geographic and Suncadia Resort false positives. Added emsend1.com ESP. Updated 15 dependencies to latest patch versions. Maintains 466/466 tests passing with 100% accuracy.
> ## 🚀 Complete Email Security Platform
> FOFF Milter provides production-ready email security with:
> - **🛡️ Intelligent Threat Detection**: Advanced feature analysis with contextual scoring
> - **📋 Modular Rulesets**: 20+ specialized detection modules covering all threat vectors
> - **🔍 Enhanced Forensic Analysis**: Comprehensive email analysis with sender consistency checks
> - **🎯 Advanced Fraud Detection**: German inheritance scams, health misinformation, brand impersonation
> - **🔧 Zero Configuration**: Works out-of-the-box with sane platform-specific defaults
> - **🔍 Advanced Analytics**: Deep inspection of attachments, URLs, and content patterns
> - **📊 Enterprise Monitoring**: Real-time statistics and comprehensive reporting
> - **⚡ Production Performance**: Optimized for high-volume processing with parallel execution
> - **🔄 Hot Reload**: Live configuration updates without service interruption
> - **🔐 Cryptographic Integrity**: Module hashing for version tracking and consistency
> ## 🧠 Intelligent Feature Analysis System
> FOFF Milter uses advanced feature extraction and comprehensive email normalization:
> ### Enhanced Unicode Normalization Engine (v0.8.11)
> - **Mathematical Alphanumeric Symbols**: Complete support for Unicode range U+1D400-1D7FF including Mathematical Sans-Serif Bold
> - **Advanced Evasion Detection**: Suspicious decorative symbols (⟰, ⵑ) removal and normalization
> - **Multi-Layer Decoding**: Automatic detection and decoding of Base64, HTML entities, URL encoding, UUEncoding
> - **Unicode Obfuscation Resolution**: Homoglyph replacement, zero-width character removal, mathematical symbol normalization
> - **Evasion Detection**: Sophisticated scoring of encoding layers and obfuscation techniques
> - **Normalized Content Analysis**: Rules work on clean, decoded content regar

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

FOFF Milter is a Sendmail milter written in Rust for email spam and fraud detection. The README describes rule modules, Unicode and encoding normalization, forensic analysis, hot-reloadable configuration, and monitoring statistics.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "1eab9ddd4d15020c4c264c384183601f459a296f2b25363ab9c9b21f4130ff15"
  },
  "primary_domain": "security",
  "secondary_domains": [
    "productivity"
  ],
  "repository_type": "application",
  "capabilities": [
    "classification",
    "static-analysis",
    "information-extraction",
    "monitoring",
    "reporting"
  ],
  "technologies": [
    "Rust",
    "Sendmail",
    "Milter"
  ],
  "summary": "FOFF Milter is a Sendmail milter written in Rust for email spam and fraud detection. The README describes rule modules, Unicode and encoding normalization, forensic analysis, hot-reloadable configuration, and monitoring statistics.",
  "use_cases": [
    "Filtering spam and phishing email on Sendmail mail servers",
    "Detecting brand impersonation and advance-fee fraud in inbound mail",
    "Analyzing email content and attachments for evasion techniques"
  ],
  "limitations": [
    "Accuracy and false-positive claims are self-reported in the README and not independently verified",
    "Requires a Sendmail mail server deployment with milter support"
  ],
  "suggested_terms": [
    "sendmail milter",
    "spam filter",
    "email security",
    "phishing detection",
    "rust email filter"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
