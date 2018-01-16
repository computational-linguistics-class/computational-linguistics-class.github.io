---
layout: default
img: up_goer_five.png
img_link: https://xkcd.com/thing-explainer/
caption: Thing Explainer - Complicated Stuff In Simple Words
title: Homework 2 "Text Classification"
active_tab: homework
release_date: 2017-01-17
due_date: 2017-01-24 11:00:00EST
attribution: Reno Kriz and Chris Callison-Burch
---

<!-- Check whether the assignment is up to date -->
{% capture this_year %}{{'now' | date: '%Y'}}{% endcapture %}
{% capture due_year %}{{page.due_date | date: '%Y'}}{% endcapture %}
{% if this_year != due_year %} 
<div class="alert alert-danger">
Warning: this assignment is out of date.  It may still need to be updated for this year's class.  Check with your instructor before you start working on this assignment.
</div>
{% endif %}
<!-- End of check whether the assignment is up to date -->


<div class="alert alert-info">
This assignment is due on {{ page.due_date | date: "%A, %B %-d, %Y" }} before {{ page.due_date | date: "%I:%M%p" }}.   This assignment may be done with a partner. 
</div>


Text Classification <span class="text-muted">: Assignment 2</span> 
=============================================================

For this assignment, we'll be building a text classifier.  The goal of our text classifer will be to distinguish between words that are simple and words that are complex.  Example simple words are *heard, sat, feet, shops, town*, and example complex words are *abdicate, detained, liaison, vintners*. Distinguishing between simple and complex words is the first step in a larger NLP task called text simplification, which aims to replace complex words with simpler synonyms.  Text simplification is potentially useful for re-writing texts so that they can be more easily understood by younger readers, people learning English as a second language, or people with learning disabilities. 

The learning goals of this assignment are:
* Understand an important class of NLP evaluation methods (precision, recall and F1), and implement them yourself.
* Employ common experimental design practices in NLP.  Split the annotated data into training/development/test sets, implement simple baselines to determine how difficult the task is, and experiment with a range of features and models.
* Get an introduction to sklearn, an excellent machine learning Python package. 

We will provide you with training and development data that has been manually labeled.  We will also give you a test set without labels.  You will build a classifier to predict the labels on our test set.  You can upload your classifier's predictions to Gradescope.  We will score its predictions and maintain a leaderboard showing whose classifier has the best performance. 

We have provided [skeleton code]() that you should implement. 

## Identifying Complex Words

Automated text simplification is an NLP task, where the goal is to take as input a complex text, and return a text that is easier to understand. One of the most logical first steps in text simplification, and example of text classification, is identifying which words in a text are hard to understand, i.e. `complex`, and which words are easy to understand, i.e. 'simple`.

We have prepared a labeled training set for this assignment.  We provide a dataset of words and their corresponding sentences that has been split into training, development, and test sets.  The training set is disjoint, so if a word appears in the training set, it will not also appear in the test set or the development set.  
You can [download the datasets here]().

Here is an example of the training data:

| WORD | LABEL | SENTENCE | SENTENCE_INDEX |
| :--- |:-----:| :------  | :------------: |
|  pizza | 0 | One would require all grain servings to be rich in whole grains -- or more than 50 percent whole-grain -- affecting such items as pastas , bread , rolls and pizza crusts . | 30 |
|  seasoned | 1 | The 4-year-old from southeast Arlington was searching for fish fossils in Mansfield with his dad , Tim , last fall when the preschooler came back with a bone that has excited even seasoned paleontologists from Southern Methodist University . | 32 |
|  watching | 0 | In the balconies , `` gamescasters `` in dark suits and bright ties are breathlessly narrating and analyzing the plays to tens of thousands of fans who are watching via a live video stream . | 28 |
|  hurling | 1 | The state news agency said about 500 young men hurling stones and Molotov cocktails set ablaze the headquarters of Morsi 's Muslim Brotherhood party in Cairo . | 9 |
|  fans | 0 | In the balconies , `` gamescasters `` in dark suits and bright ties are breathlessly narrating and analyzing the plays to tens of thousands of fans who are watching via a live video stream . | 25 |
|  attire | 1 | The panel also found problematic a uniform exemption for students who wore the attire of national youth organizations like the Boy Scouts or Girl Scouts on meeting days . | 13 |


After taking a look at the datasets, we recommend that write the `load_file(data_file)` function, which takes in the file name (`data_file`) of one of the datasets, and reads in the words and labels from these files.

## Implement The Evaluation Metrics

Before we start with this text classification task, we need to first determine how we will evaluate our results. The most common metrics are precision, recall, and f-score.

For this problem, you will fill in the following functions:

- `get_precision(y_pred, y_true)`
- `get_recall(y_pred, y_true)`
- `get_fscore(y_pred, y_true)`

Here, `y_pred` is list of predicted labels from a classifier, and `y_true` is a list of the true labels.

You may not use sklearn's built-in functions for this, you must instead write your own code to calculate these metrics. You will be using these functions to evaluate your classifiers later on in this assignment.

We recommend that you also write a function `test_predictions(y_pred, y_true)`, which prints out the precision, recall, and f-score. This function will be helpful later on!


## Implement a majority class baseline

You should start by implementing simple baselines. Your first baseline is a majority class baseline.  You should complete the function `all_complex(data_file)`, which takes in the file name of one of the datasets, labels each word in the dataset as complex, and prints out the precision, recall, and fscore. 

Please report the precision, recall, and f-score using both the training data and the development data individually to be graded.

## Word length baseline

For our next baseline, we will use the length of each word to predict its complexity. 

For the word length baseline, you should try setting various thresholds for word length. For example, you might set a threshold of 9, meaning that any words with less than 9 characters will be labeled simple, and any words with 9 characters or more will be labeled complex. Once you find the best threshold using the training data, use this same threshold for the development data as well.

You will be filling in the function `word_length_threshold(training_file, development_file)`. This function takes in both the training and development data files, and prints out the precision, recall, and f-score for your best threshold's performance on both the training and development data.

In your write-up, please report the precision, recall, and f-score for the training and development data individually, along with the range of thresholds you tried.


## Word frequency baseline

Our final baseline thresholds on word frequency instead of length. We have provided Google NGram frequencies in the text file `ngram_counts.txt`, along with the helper function `load_ngram_counts(ngram_counts_file)` to load them into Python as a dictionary.

You will be filling in the function `word_frequency_threshold(training_file, development_file, counts)`, where `counts` is the dictionary of word frequencies. This function again prints out the precision, recall, and fscore for your best threshold's performance on both the training and development data.

Please again report the precision, recall, and f-score on the training and development data individually, along with the range of thresholds you tried, and the best threshold to be graded.

Note: Due to its size, loading the ngram counts into Python takes around 20 seconds, and finding the correct threshold may take a few minutes to run.

## Naive Bayes classification 

Now, let's move on to actual machine learning classifiers! For our first classifier, you will use the built-in Naive Bayes model from sklearn, to train a classifier. You should refer to the online sklearn documentation when you are building your classifier. For features, you will start by use word length and word frequency as your two features. To import this model, use the following command:

{% highlight python %}
>>> from sklearn.naive_bayes import GaussianNB
{% endhighlight %}

You should fill in the function `naive_bayes(training_file, development_file, counts). This function will train a `Naive Bayes` classifier on the training data, and print your model's precision, recall, and f-score on the training data and the development data individually.

In your write-up, please report the precision, recall, and f-score on the training and development data for your Naive Bayes classifier that uses word length and word frequency.

Note 1:  There are two important things to point out: sklearn classifiers take in `numpy` arrays, rather than regular lists. You may use the online `numpy` documentation. To import `numpy` into Python, use the following command:

{% highlight python %}
>>> import numpy as np
{% endhighlight %}

Note 2: Before training and testing a classifier, it is generally important to normalize your features. This means that you need to find the mean and standard deviation (sd) of a feature. Then, for each row, perform the following transformation:

X_scaled = (X_original - mean)/sd

Be sure to always use the means and standard deviations from the `training data`.

## Logistic Regression

Next, you will use sklearn;s built-in Logistic Regression classifier. Again, we will use word length and word frequency as your two features. To import this model, use the following command:

{% highlight python %}
>>> from sklearn.linear_model import LogisticRegression
{% endhighlight %}

For this problem, you will be filling in the function `logistic_regression(training_file, development_file, counts)`. This function will train a `Logistic Regression` classifier on the training data, and print your model's precision, recall, and f-score on the training data and the development data individually.

Again, please report the precision, recall, and f-score on the training and development data.

## Comparing of Naive Bayes vs. Logistic Regression.

After implementing the previous two sections, you will notice that even though the Naive Bayes and Logistic Regression classifiers are given the same data, their performance is not identical. Add a paragraph to your write up that discusses which model performed better on this task, and why you think this was the case.

## Build your own model

Finally, the fun part! In this section, you will build your own classifier for the complex word identification task, and compare your results to that of your classmates. You will also perform an error analysis for your best performing model.

## Try different models

You can choose any other types of classifier, and any additional features you can think of! For classifiers, beyond Naive Bayes and Logistic Regression, you might consider trying `SVM`, `Decision Trees`, and `Random Forests`, among others. Additional features you may consider include number of syllables, as well as sentence-based complexity features, such as length of the sentence, average word length, etc. For counting the number of syllables, we have provided a python script `syllables.py` that contains the function `count_syllables(word)`, which you may use.

When trying different classifiers, we recommend that you train on training data, and test on the development data, like the previous sections.

In your writeup, please include a description of all of the models and features that you tried.

Note: You can also tune the parameters of your model, e.g. what type of kernel to use. This is not required, as some of you may not be that familiar with this.


## Analyze your model

An important part of text classification tasks is to determine what your model is getting correct, and what your model is getting wrong. For this problem, you must train your best model on the training data, and report the precision, recall, and f-score on the development data.

In addition, need to perform a detailed error analysis of your models. Give several examples of words on which your best model performs well. Also give examples of words which your best model performs poorly on, and try to identify at least two categories of words on which your model is making errors.


## Comparing your best model to your classmates

Finally, train your best model on both the training and development data. You will use this classifier to predict labels for the test data, and will submit these labels in a text file named `test_labels.txt` (with one label per line) to the leaderboard; be sure NOT to shuffle the order of the test examples. Instructions for how to post to the leaderboard will be posted on Piazza soon.

The baselines` performances will be included on the leaderboard. In order to receive full credit, your model must be able to outperform all of the baselines. In addition, the top 3 teams will receive 5 bonus points!

Good luck, and have fun!
