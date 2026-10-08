---
repository: "alexandrerodenas/Pixo"
github_id: 1016963682
url: "https://github.com/alexandrerodenas/Pixo"
description: "Pixo is a powerful, privacy-focused web application that helps you automatically organize your local photos using artificial intelligence, right in your browser. No uploads, no servers, no data collection—your photos and your data stay on your machine."
starred_at: "2026-10-08T20:17:28Z"
language: "TypeScript"
topics: ["image", "image-classification", "object-detection", "tensorflowjs", "webapp"]
homepage: "https://pixo-omega.vercel.app"
license: "GPL-3.0"
archived: false
---

# alexandrerodenas/Pixo

Pixo is a powerful, privacy-focused web application that helps you automatically organize your local photos using artificial intelligence, right in your browser. No uploads, no servers, no data collection—your photos and your data stay on your machine.

**GitHub:** https://github.com/alexandrerodenas/Pixo

## README excerpt

> Pixo
>
> Organize your photos effortlessly.
>
>
>
> Pixo is a privacy-first web application that organizes your local photos using AI — entirely in your browser. No uploads, no servers, no data collection.
> Leveraging the File System Access API and TensorFlow.js, it runs MobileNet and COCO-SSD models locally for scene classification, object detection, blur scoring, and duplicate matching.
> ## Features
> - **100% Local & Private** — All processing stays in your browser. Your photos never leave your machine.
> - **AI Analysis** — Scene classification (MobileNet) and object detection (COCO-SSD), accelerated via WebGPU, WASM, or WebGL.
> - **Blur Detection** — Laplacian Variance analysis on GPU, scoring each photo 0–100 with visual indicators.
> - **Duplicate Detection** — Semantic embeddings to find exact duplicates, near-duplicates, and burst photos, auto-selecting the best version.
> - **Dual View Modes** — Grid View for browsing, Folder View grouped by AI classification labels.
> - **Custom Rules** — Create classification and detection rules (e.g., *"SELECT photos with 'beach' classification > 80%"*) with optional auto-apply.
> - **Uncertainty Filtering** — Configurable threshold to flag ambiguous photos as *Uncategorized* for manual review.
> - **Save & Organize** — Mark favorites, isolate selections, move saved photos to a dedicated folder, or permanently delete.
> - **Dark Mode** — Respects your system's appearance settings.
> - **Profile Import/Export** — Backup or share your rules and preferences as JSON.
> ## Quick Start
> ### Direct Browser
> Open `index.html` in a browser supporting the File System Access API (Chrome, Edge). Follow the onboarding, then select a photo directory.
> ### Docker
> docker build -t pixo .
> docker run -d -p 8080:80 pixo
> Open [http://localhost:8080](http://localhost:8080).
> > **Note**: `localhost` is treated as a secure context by browsers, satisfying the File System Access API requirement.
> ## Usage
> 1. **Onboarding** — Enter your name to create a profile with sensible default rules.
> 2. **Load Photos** — Click *Select Directory* in the sidebar.
> 3. **AI Analysis** — Models run automatically; track progress in real-time.
> 4. **Organize** — Find duplicates, isolate blurry shots, mark favorites, apply rules, move or delete.
> 5. **Customize** — Add rules, adjust uncertainty threshold, change the saved folder name, export your profile.
> ## Tech Stack
> **React 19**, **TypeScript**, **TensorFlow.js** (MobileNet, COCO-SSD), **Vite**, **Tailwind CSS**, **Docker**.
> ## Roadmap
> ##

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Pixo is a browser-based web application that organizes local photos using TensorFlow.js models (MobileNet, COCO-SSD) for scene classification and object detection. It also provides blur scoring, duplicate detection, custom rules, and profile import/export, with processing performed locally without uploads.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "571fce2d4be7d7377f7043bac851ea2e0298680a3f963b1e0b4de69020589b01"
  },
  "primary_domain": "vision-media",
  "secondary_domains": [
    "ai-ml",
    "productivity"
  ],
  "repository_type": "application",
  "capabilities": [
    "image-classification",
    "object-detection",
    "indexing",
    "media-editing",
    "classification"
  ],
  "technologies": [
    "TypeScript",
    "React",
    "TensorFlow.js",
    "Vite",
    "Tailwind CSS",
    "Docker",
    "WebGPU",
    "WebGL"
  ],
  "summary": "Pixo is a browser-based web application that organizes local photos using TensorFlow.js models (MobileNet, COCO-SSD) for scene classification and object detection. It also provides blur scoring, duplicate detection, custom rules, and profile import/export, with processing performed locally without uploads.",
  "use_cases": [
    "Organizing large local photo libraries by AI-generated labels",
    "Finding duplicate, near-duplicate, and blurry photos for cleanup",
    "Applying custom classification rules to sort photos into folders"
  ],
  "limitations": [
    "Requires a browser supporting the File System Access API (Chrome, Edge)",
    "Relies on browser-side model execution, so performance depends on the local device",
    "Classification and detection outputs are model-based and may be uncertain, as the README notes an uncertainty threshold"
  ],
  "suggested_terms": [
    "photo organizer",
    "tensorflowjs",
    "browser image classification",
    "duplicate photo finder",
    "local AI photos"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
