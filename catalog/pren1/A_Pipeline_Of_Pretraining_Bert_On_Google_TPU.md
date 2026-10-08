---
repository: "pren1/A_Pipeline_Of_Pretraining_Bert_On_Google_TPU"
github_id: 190471181
url: "https://github.com/pren1/A_Pipeline_Of_Pretraining_Bert_On_Google_TPU"
description: "A tutorial of pertaining Bert on your own dataset using google TPU"
starred_at: "2019-12-28T13:49:01Z"
language: "Jupyter Notebook"
topics: []
homepage: ""
license: null
archived: false
---

# pren1/A_Pipeline_Of_Pretraining_Bert_On_Google_TPU

A tutorial of pertaining Bert on your own dataset using google TPU

**GitHub:** https://github.com/pren1/A_Pipeline_Of_Pretraining_Bert_On_Google_TPU

## README excerpt

> # A Pipeline Of Pretraining Bert On Google TPU
> A tutorial of pertaining Bert on your own dataset using google TPU
> ## Introduction
> Bert, which is also known as the Bidirectional Encoder Representations from Transformers, is a powerful neural network model presented by Google in 2018. There exist a bunch of pre-trained models that can be fine-tuned for the downstream tasks to achieve good performances. Though the pre-trained model is good enough, you may still want to tune the pre-trained model offered by Google on your own domain-specific corpus for several additional epochs. That is, give your Bert model a chance to be familiar with your jargons. Then we can expect better performance in the end.
> Nevertheless, as I observed, such a tuning (pretraining) process is time-consuming even on a 1080Ti GPU. The batch size is limited, and the loss decreases slowly. One promising way to solve this problem is to use TPU, which is provided by Google. From my personal experience, a V_3.8 TPU is 35 times faster than a 1080Ti GPU (no joking!). So, in this tutorial, We will go over the pipeline of pretraining the Bert on TPU.
> ## Pre-request
> 1. A Google account
> 2. A bank card (No worry! Google won't charge you any fees! At least this time :P)
> 3. Your data
> ## Data preparation
> Prepare your data as you are told at [the Bert repo](https://github.com/google-research/bert#pre-training-with-bert). After this process, you should get a .txt file. This time, let's simply use the sample_text.txt, which can be downloaded from [the Bert repo](https://github.com/google-research/bert.git).
> Download the pre-trained Bert model at [here](https://storage.googleapis.com/bert_models/2018_11_23/multi_cased_L-12_H-768_A-12.zip), make sure you unzip it. Now you get a folder named "multi_cased_L-12_H-768_A-12".
> ## Data upload
> First, go to the [Google cloud platform](https://cloud.google.com) and sign in. Create your project, and you should see this interface:
>
>
> Then, click the storage button on the left bar:
>
>
> Click Create bucket, then give it a name. For example, the "sample_bucket_test". Make sure that this name is not used by any other people.
>
>
>
>
> Ok! Now it's time to upload the data (sample_text.txt) and the pre-trained model from Google (multi_cased_L-12_H-768_A-12) to the bucket!
>
>
> Click the Upload folder button, and select the folder "multi_cased_L-12_H-768_A-12" to upload the pre-trained model. Click the Upload files button, and select the file "sample_text.txt" to upload your data. Then yo

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->
