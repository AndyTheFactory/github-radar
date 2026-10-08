---
repository: "Panniantong/Agent-Reach"
github_id: 1165277268
url: "https://github.com/Panniantong/Agent-Reach"
description: "Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees."
starred_at: "2026-10-08T20:42:10Z"
language: "Python"
topics: ["agent-infrastructure", "ai-agent", "ai-search", "automation", "bilibili", "claude-code", "cli", "cursor", "free-api", "llm-tools", "mcp", "python", "reddit-scraper", "twitter-scraper", "web-scraper", "xiaohongshu", "youtube-transcript"]
homepage: ""
license: "MIT"
archived: false
---

# Panniantong/Agent-Reach

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

**GitHub:** https://github.com/Panniantong/Agent-Reach

## README excerpt

> 👁️ Agent Reach
>
> 给你的 AI Agent 一键装上互联网能力
>
>
> 当下最稳的接入方式，替你选好、装好、体检好——接入方式会换代，你不用操心
>
>
>
>
>
>
>
> ---
> ## ❤️赞助商
> > [想出现在这里？](mailto:pnt01@foxmail.com)
>
> 点击折叠
>
>
>
> BrowserAct 支持从 Amazon、LinkedIn、X、Google Maps 等复杂网站提取你需要的任意数据。你只需用自然语言描述抓取需求，Agent 就会基于真实浏览器自动探索并测试页面流程，生成可靠、可复用的数据采集 Bot，并返回结构化结果。无需手动构建爬虫，无需编写代码。BrowserAct 内置隐身浏览、验证码处理和高质量住宅代理，帮助你更稳定地完成复杂网页数据采集。新用户注册即送 1000 积分，立即免费试用。
>
>
>
> 在腾讯云 Lighthouse 秒级部署 OpenClaw 全能助手，可通过对话丝滑接入 Agent Reach，给你的 OpenClaw 一键装上互联网能力。
>
>
>
> CoreClaw | 网页抓取平台与现成数据采集工具，CoreClaw 提供 100+ 现成数据采集工具，支持 Amazon、TikTok、Google Maps、Instagram、Facebook、YouTube 等平台，无需代码，支持 JSON/CSV 导出，仅对成功结果计费。免费$3测试！
>
>
>
> 优刻得星图astraflow大模型，支持200+模型一键调用：内置 Kimi K3、DeepSeek V4/V3、Qwen 3、GLM5.2、happyhorse等全球领先开源大模型，无需自训，开箱即用
>
>
>
> ---
> ## 为什么需要 Agent Reach？
> AI Agent 已经能帮你写代码、改文档、管项目——但你让它去网上找点东西，它就抓瞎了：
> - 📺 "帮我看看这个 YouTube 教程讲了什么" → **看不了**，拿不到字幕
> - 🐦 "帮我搜一下推特上大家怎么评价这个产品" → **搜不了**，Twitter API 要付费
> - 📖 "去 Reddit 上看看有没有人遇到过同样的 bug" → **403 被封**，服务器 IP 被拒
> - 📕 "帮我看看小红书上这个品的口碑" → **打不开**，必须登录才能看
> - 📺 "B站上有个技术视频，帮我总结一下" → **拿不到**，通用下载工具被 B站风控全面拦截
> - 🔍 "帮我在网上搜一下最新的 LLM 框架对比" → **没有好用的搜索**，要么付费要么质量差
> - 🌐 "帮我看看这个网页写了啥" → **抓回来一堆 HTML 标签**，根本没法读
> - 📦 "这个 GitHub 仓库是干嘛的？Issue 里说了什么？" → 能用，但认证配置很麻烦
> - 📡 "帮我订阅这几个 RSS 源，有更新告诉我" → 要自己装库写代码
> **这些不难实现，但是需要自己折腾配置**
> 每个平台都有自己的门槛——要付费的 API、要绕过的封锁、要登录的账号、要清洗的数据。你要一个一个去踩坑、装工具、调配置，光是让 Agent 能读个推特就得折腾半天。
> **Agent Reach 把这件事变成一句话：**
> 帮我安装 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
> 复制给你的 Agent，几分钟后它就能读推特、搜 Reddit、看 YouTube、刷小红书了。
> **已经装过了？更新也是一句话：**
> 帮我更新 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
> > ⭐ **Star 这个项目**，我们会持续追踪各平台的变化、接入新的渠道。你不用自己盯——平台封了我们修，有新渠道我们加。
> ### ✅ 在你用之前，你可能想知道
> | | |
> |---|---|
> | 💰 **完全免费** | 所有工具开源、所有 API 免费。唯一可能花钱的是服务器代理（$1/月），本地电脑不需要 |
> | 🔒 **隐私安全** | Cookie 只存在你本地，不上传不外传。代码完全开源，随时可审查 |
> | 🔄 **持续换代** | 每个平台都是「首选 + 备选」多后端路由。某个接入方式失效了，我们换下一个，你无感（2026-06 实例：yt-dlp 被 B站风控封死 → 已切换 bili-cli，用户零操作） |
> | 🤖 **兼容所有 Agent** | Claude Code、OpenClaw、Cursor、Windsurf……任何能跑命令行的 Agent 都能用 |
> | 🩺 **自带诊断** | `agent-reach doctor` 一条命令告诉你哪个通、哪个不通、怎么修 |
> ---
> ## 支持的平台
> | 平台 | 装好即用 | 配置后解锁 | 怎么配 |
> |------|---------|-----------|-------|
> | 🌐 **网页** | 阅读任意网页 | — | 无需配置 |
> | 📺 **YouTube** | 字幕提取 + 视频搜索 | — | 无需配置 |
> | 📡 **RSS** | 阅读任意 RSS/Atom 源 | — | 无需配置 |
> | 🔍 **全网搜索** | — | 全网语义搜索 | 自动配置（MCP 接入，免费无需 Key） |
> | 📦 **GitHub** | 读公开仓库 + 搜索 | 私有仓库、提 Issue/PR、Fork | 告诉 Agent「帮我登录 GitHub」 |
> | 🐦 **Twitter/X** | 读单条推文 | 搜索推文、浏览时间线、读长文 | 告诉 Agent「帮我配 Twitter」 |
> | 📺 **B站** | 搜索 + 视频详情（bili-cli，无需登录） | 字幕（OpenC

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

Agent Reach is a Python CLI that equips AI agents with tools to read and search platforms such as Twitter/X, Reddit, YouTube, GitHub, Bilibili, and XiaoHongShu. It is MIT-licensed, includes a `doctor` diagnostic command, and uses multi-backend routing per platform according to its README.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "31d8ee65073ae80d2807e313ce289c425212dc6e109e767444dc99260c672b90"
  },
  "primary_domain": "developer-tools",
  "secondary_domains": [
    "research-learning",
    "productivity"
  ],
  "repository_type": "library",
  "capabilities": [
    "api-integration",
    "web-scraping",
    "search-retrieval",
    "information-extraction",
    "automation"
  ],
  "technologies": [
    "Python",
    "CLI",
    "MCP",
    "YouTube",
    "Twitter/X",
    "Reddit",
    "GitHub API",
    "Bilibili"
  ],
  "summary": "Agent Reach is a Python CLI that equips AI agents with tools to read and search platforms such as Twitter/X, Reddit, YouTube, GitHub, Bilibili, and XiaoHongShu. It is MIT-licensed, includes a `doctor` diagnostic command, and uses multi-backend routing per platform according to its README.",
  "use_cases": [
    "Extracting YouTube transcripts for AI agent summarization",
    "Searching Reddit or Twitter discussions from an agent",
    "Reading public GitHub repositories and issues through an agent"
  ],
  "limitations": [
    "Some platforms require user-provided login or cookies for full functionality",
    "Relies on third-party backends that may break when platforms change access rules",
    "README excerpt includes sponsor content; features beyond the excerpt were not verified"
  ],
  "suggested_terms": [
    "ai agent internet access",
    "twitter scraper cli",
    "youtube transcript extraction",
    "reddit scraper agent",
    "mcp web search"
  ],
  "confidence": "medium"
}
```

<!-- github-radar:enrichment:end -->
