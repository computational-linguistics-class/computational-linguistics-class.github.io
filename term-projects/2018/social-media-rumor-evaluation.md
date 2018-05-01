---
layout: default
img: python.jpg
img_link: http://xkcd.com/353/
caption: Hello world!
title: Social Media Rumor Evaluation 
active_tab: homework
term_project: true
---


# Social Medial Rumor Evaluation 


For this assignment, we will be creating a text classisification system for Twitter messages to determine the veracity of rumors, based on several linguistic and contextual features. Each rumor is in the form of a tweet that reports an updated associated with a newsworthy event. The labels describe whether the rumor is true or false, as well as a confidence percentage between 0 and 1.

This project is modeled after SemEval 2017 Task 8. There are two variants to this task. In subtask A, the veracity of a rumour will have to be predicted solely from the tweet itself (closed variant). In subtask B, predicting veracity is dependent on the provided additional context. This context consists of relevant snapshots, including a snapshot of an associated Wikipedia article, a Wikipedia dump, news articles from digital news outlets retrieved from NewsDiffs, as well as preceding tweets from the same event.

More information of the task can be found here: https://competitions.codalab.org/competitions/16172#learn_the_details


## Data Structure 

All of the code and data for this project can be downloaded here: **link**

The training and development labels for tasks A and B can be found in **/data/semeval2017-task8-dataset/traindev**.
The test labels can be found in **/data/semeval2017-task8-dataset/goldtest**.
These directories contain JSON files which map tweet IDs to the label "true", "false", or "unverified".

The raw data for the tweets, including the message content, and a large cache of metadata, is stored in **/data/semeval2017-task8-dataset/rumoureval-data**. Each rumor topic has a subdirectory, and each tweet has a directory within the topic directory, labeled by tweet ID. The tweet directory contains **/source-tweet/[ID].json, which contains the literal message and metadata. **structure.json** details the structure of the tweet and any replying tweets, and **/replies/** contains the JSON data for those replies. Additionally, **urls.dat** contains a tab-separated list of URLs linked by each tweet (labeled by ID).


## Evaluation Metric

With a multi-class prediction problem, the simplest evaluation metric is accuracy, or (TP + TN) / |N|. In other words, the number of correct predictions over the total number of test values.


## Baseline

The first baseline to implement is a majority class baseline, which labels all of the test tweets by the label that appears with greatest frequency in the training data. This should achieve a decently high accuracy score of around 0.48.


## Getting Started 

In order to get started on the actual classification task, you need first need to set up a ML classifier. Although there are several available packages for classifiers, we recommend using the scikit-learn package for SVM, NaiveBayes, and Decision Tree classifiers.

If you do not already have scikit-learn installed, first be sure install NumPy 1.8.2+ and SciPy 0.13.3+. You can install sklearn classifiers using pip:
	$ pip3 install -U scikit-learn

NOTE: A more advanced option might be constructing an RNN, for which we recommend the Pytorch package. Pytorch can be installed using pip as well:
	$ pip3 install pytorch

We recommend that you load all of the JSON data, including text and metadata content into a Pandas dataframe, which can be converted to NumPy for feeding into a classifier. This will make handling the multiple data sources and features simpler, and collect data into a central location.



## Features

There are a number of other features which we recommend you try appyling to this problem. Please pick a few of these features to add to your model, and report on the success of each feature:

* GloVe 200-D word embeddings (with dimemsionality reduction)
* Word count
* Number of "vulgar" words
* Number of adjectives
* Word embeddings
* MPQA subjectivity lexicon
* POS tags
* Tweet metadata (Number of followers, account creation date, contains images)
* Context features (Replies, Wikipedia articles)

For some of these features in particular we have included a package for parsing Twitter data, ported into Python from the CMU Tweet NLP (Noah's ARK) [Twitter Parser](http://www.cs.cmu.edu/~ark/TweetNLP/). The script TwitterParser.py is a wrapper for the original Java tagger, and provides methods for tokenizing and POS-tagging tweets, with specialized labels for URLs, emojis, retweets, user-mentions, and other twitter-specific tags.

