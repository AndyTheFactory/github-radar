---
repository: "AndyTheFactory/article-extraction-dataset"
github_id: 759533023
url: "https://github.com/AndyTheFactory/article-extraction-dataset"
description: "Article title, authors, date and body extraction dataset. "
starred_at: "2024-03-19T23:21:22Z"
language: "HTML"
topics: ["article-extractor", "corpus", "corpus-builder", "corpus-tools", "dataset", "datasets", "html-to-markdown", "html2text", "news", "news-aggregator", "news-crawler", "readability", "scraping", "scraping-websites", "text-cleaning", "text-extraction", "text-mining", "text-preprocessing", "web-scraping"]
homepage: ""
license: "Apache-2.0"
archived: false
---

# AndyTheFactory/article-extraction-dataset

Article title, authors, date and body extraction dataset. 

**GitHub:** https://github.com/AndyTheFactory/article-extraction-dataset

## README excerpt

> # Article extraction dataset from  News Websites
> ## Introduction
> We release a curated dataset of news articles from more than 200 websites. The dataset contains 424 articles cleaned from any kind of boileplate code, text and ads. Most articles are in English, and were published throughout 2023, most at the end of the year. The dataset is intended for research purposes, and can be used for evaluating text extraction algorithms and boilerplate removal.
> The article extraction task involves identifying and isolating the main content of a webpage, typically articles or significant textual content, while removing all irrelevant material such as advertisements, navigation menus, footers, headers, and any other non-essential elements. This process is important in applications, including web search, data mining, content analysis, and the creation of clean datasets for machine learning and natural language processing tasks. Additionally, the extraction process distills the web page down to its core informative content, making it more accessible for analysis or reading purposes.
> Article extraction, or boilerplate removal has to overcome several challenges, such as dealing with diverse webpage layouts, identifying the structural and semantic markup of HTML to discern content from boilerplate, and adapting to the dynamic nature of web content and design practices. Techniques for article extraction often involve a combination of heuristic rules, machine learning models, and natural language processing tools to analyze the DOM structure of web pages, evaluate the density and distribution of textual content, and apply models trained to recognize patterns typical of valuable content.
> ## Dataset Description
> The dataset consists of 424 articles from 212 different websites. Article sources were selected from [the list of popular news websites](https://github.com/AndyTheFactory/newspaper4k/blob/master/newspaper/resources/misc/popular_sources.txt), blogs, and online magazines. Html files were downloaded with python's `requests` library, or, in case of cloudflare protection, with `playwright`. The articles were then manually cleaned from any kind of boilerplate code, text and ads. Additionally, the dataset contains the following metadata for each article:
> - `link`: the original URL of the article
> - `site`: the website where the article was published
> - `title`: the title of the article
> - `date`: the publication date of the article
> - `authors`: the author(s) of the article
> - `text

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->
