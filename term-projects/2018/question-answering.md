---
layout: default
img: python.jpg
img_link: http://xkcd.com/353/
caption: Hello world!
title: Question Answering
active_tab: homework
term_project: true
---

# Question Answering

The problem is very simple. Provide a multiple choice question, and let the machine answer it.


## What is exciting about your term project? Why did you want to work on this topic?
Motivation: Question answering is very general and sure has a lot of application.
It is one of the oldest research areas, so it is very interesting to read them
We can combine recent results (word 2 vec, dense vectors, etc) to improve results.



## Dataset

My dataset is part of the dataset available here http://data.allenai.org/arc/. Each file contains information about 8000 grade-school level science multiple choice questions, their answers, and miscellaneous related info (question source, etc). 

## Data Sample

Which factor will most likely cause a person to develop a fever?  (A) a leg muscle relaxing after exercise (B) a bacterial population in the bloodstream (C) several viral particles on the skin (D) carbohydrates being digested in the stomach

## What is the baseline performance for the simple baseline like a majority class baseline?

The baseline for this dataset is surprising low. 

## Simple baseline

The simple baseline uses word coocurrence frequency between the answers and the question as its sole feature when trainig a LogisticRegression classifier. It scores an accuracy of 0.27450980392156865. My evaluation code is in the simple_baseline.py file.

## Literature review

### Crowdsourcing for Multiple-Choice Question Answering

In the multiple-choice question answering paper, it described methods to leverage crowd wisdom for multiple-choice question answering, and employ lightweight machine learning techniques, such as block coordinate descent, to improve the aggregation accuracy of crowdsourced answers to these questions. In their evaluation, the “Confident Only Voting” (CO) slightly outperforms the “Majority Voting” and “Confidence Weighted Voting”, and is the better model during their test. In this CO method, they filter the collected data by only choosing x which has a confidence label “certain”. 

### GloVe: Global Vectors for Word Representation

GloVe is an unsupervised learning algorithm for obtaining vector representations for words. Training is performed on aggregated global word-word co-occurrence statistics from a corpus, and the resulting representations showcase interesting linear substructures of the word vector space. The GloVe model performs significantly better than the other baselines, often with smaller vector sizes and smaller corpora. The results using the word2vec tool are somewhat better than most of the previously published results.


### Question Answering Using Deep Learning

In this project, they study the application of several deep learning models to the question answering task. After describing two RNN-based baselines, they focus our attention on end-to-end memory networks, which have provided state-of-the-art results on some QA tasks while being relatively fast to train.


We decided to try the RNN as our published baseline, and also compare RNN to the usual neural network.

## Published baseline

The published baseline involves using Neural Network, one of the deep learning method. 

## Extensions

Word2Vec, RNN, Crowdsorcing algorithms could be extensions that we could use.

## Presentation
[Here are our presentation slides](https://docs.google.com/presentation/d/1mptvbylcj2GeiYL311TuBhebdL-rQ0e304fh0HGtL-Q/edit?usp=sharing)

