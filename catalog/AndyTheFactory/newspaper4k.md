---
repository: "AndyTheFactory/newspaper4k"
github_id: 708506677
url: "https://github.com/AndyTheFactory/newspaper4k"
description: "📰 Newspaper4k a fork of the beloved Newspaper3k. Extraction of articles, titles, and metadata from news websites. "
starred_at: "2023-11-20T22:12:42Z"
language: "Python"
topics: ["articles", "articles-data", "crawler", "datasets-preparation", "news", "newspaper3k", "python", "requests", "scraper", "scraping"]
homepage: "https://newspaper4k.readthedocs.io/en/latest/index.html"
license: "MIT"
archived: false
---

# AndyTheFactory/newspaper4k

📰 Newspaper4k a fork of the beloved Newspaper3k. Extraction of articles, titles, and metadata from news websites. 

**GitHub:** https://github.com/AndyTheFactory/newspaper4k

## README excerpt

> # Newspaper4k: Article Scraping & Curation, a continuation of the beloved newspaper3k by codelucas
> Newspaper4k Project grew from a fork of the well known newspaper3k  by [codelucas](https://github.com/codelucas/newspaper) which was not updated since September 2020. The initial goal of this fork was to keep the project alive and to add new features and fix bugs. As of version 0.9.3 there are many new features and improvements that make Newspaper4k a great tool for article scraping and curation. To make the migration to Newspaper4k easier, all the classes and methods from the original project were kept and the new features were added on top of them. All API calls from  the original project still work as expected, such that for users familiar with newspaper3k you will feel right at home with Newspaper4k.
> At the moment of the fork, in the original project were over 400 open issues, which I have duplicated, and as of v 0.9.3 only about 180 issues still need to be verified (many are already fixed, but it's pretty cumbersome to check - [hint hint ... anyone contributing?](https://github.com/AndyTheFactory/newspaper4k/discussions/606)). If you have any issues or feature requests please open an issue here.
> |     |     |
> |-------------|-------------|
> | **Experimental ChatGPT helper bot for Newspaper4k:**         | [![ChatGPT helper](docs/user_guide/assets/chatgpt_chat200x75.png)](https://chat.openai.com/g/g-OxSqyKAhi-newspaper-4k-gpt)|
> ## Python compatibility
> - Python 3.10+ minimum
> # Quick start
> pip install newspaper4k
> ## Using the CLI
> You can start directly from the command line, using the included CLI:
> python -m newspaper --url="https://edition.cnn.com/2023/11/17/success/job-seekers-use-ai/index.html" --language=en --output-format=json --output-file=article.json
> More information about the CLI can be found in the [CLI documentation](https://newspaper4k.readthedocs.io/en/latest/user_guide/cli_reference.html).
> ## Using the Python API
> Alternatively, you can use Newspaper4k in Python:
> ### Processing one article / url at a time
> import newspaper
> article = newspaper.article('https://edition.cnn.com/2023/10/29/sport/nfl-week-8-how-to-watch-spt-intl/index.html')
> print(article.authors)
> # ['Hannah Brewitt']
> print(article.publish_date)
> # 2023-10-29 09:00:15.717000+00:00
> print(article.text)
> # New England Patriots head coach Bill Belichick, right, embraces Buffalo Bills head coach Sean McDermott ...
> print(article.top_image)
> # https://media.cnn.com/api/v1/images/stellar/prod/2310

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->
