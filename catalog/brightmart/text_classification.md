---
repository: "brightmart/text_classification"
github_id: 92841276
url: "https://github.com/brightmart/text_classification"
description: "all kinds of text classification models and more with deep learning"
starred_at: "2020-02-03T22:02:25Z"
language: "Python"
topics: ["attention-mechanism", "classification", "convolutional-neural-networks", "fasttext", "memory-networks", "multi-class", "multi-label", "nlp", "sentence-classification", "tensorflow", "text-classification", "textcnn", "textrnn"]
homepage: ""
license: "MIT"
archived: false
---

# brightmart/text_classification

all kinds of text classification models and more with deep learning

**GitHub:** https://github.com/brightmart/text_classification

## README excerpt

> Text Classification
> -------------------------------------------------------------------------
> The purpose of this repository is to explore text classification methods in NLP with deep learning.
> #### Update:
> Customize an NLP API in three minutes, for free: NLP API Demo
> Language Understanding Evaluation benchmark for Chinese(CLUE benchmark): run 10 tasks & 9 baselines with one line of code, performance comparision with details.
> Releasing Pre-trained Model of ALBERT_Chinese Training with 30G+ Raw Chinese Corpus, xxlarge, xlarge and more, Target to match State of the Art performance in Chinese, 2019-Oct-7, During the National Day of China!
> Google's BERT achieved new state of art result on more than 10 tasks in NLP using pre-train in language model then
> fine-tuning. Pre-train TexCNN: idea from BERT for language understanding with running code and data set
> #### Introduction
> it has all kinds of baseline models for text classification.
> it also support for multi-label classification where multi labels associate with an sentence or document.
> although many of these models are simple, and may not get you to top level of the task. but some of these models are very
> classic, so they may be good to serve as baseline models. each model has a test function under model class. you can run
> it to performance toy task first. the model is independent from data set.
> several models here can also be used for modelling question answering (with or without context), or to do sequences generating.
> we explore two seq2seq model(seq2seq with attention,transformer-attention is all you need) to do text classification.
> and these two models can also be used for sequences generating and other tasks. if your task is a multi-label classification,
> you can cast the problem to sequences generating.
> we implement two memory network. one is dynamic memory network. previously it reached state of art in question
> answering, sentiment analysis and sequence generating tasks. it is so called one model to do several different tasks,
> and reach high performance. it has four modules. the key component is episodic memory module. it use gate mechanism to
> performance attention, and use gated-gru to update episode memory, then it has another gru( in a vertical direction) to
> performance hidden state update. it has ability to do transitive inference.
> the second memory network we implemented is recurrent entity network: tracking state of the world. it has blocks of
> key-value pairs as memory, run in parallel, which achi

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->
