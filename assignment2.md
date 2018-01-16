---
layout: default
img: python.jpg
img_link: http://xkcd.com/353/
caption: Hello world!
title: Homework 2 "Text Classification"
active_tab: homework
release_date: 2017-01-17
due_date: 2017-01-24 11:00:00EST
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
This assignment is due on {{ page.due_date | date: "%A, %B %-d, %Y" }}. 
</div>

<div class="alert alert-info" markdown="span">
Links to tutorials and other Python resources are posted on the [resources page](resources.html).</div>


Text Classification <span class="text-muted">: Assignment 2</span> 
=============================================================
In our first class, we introduced the concept of text classification. To follow this up, we will be first review several metrics, to make sure you fully understand how text classification problems, among many other natural language processing tasks, are evaluated. From there, we will ask you to consider an example text classification problem: identifying words as simple vs. complex. With our provided dataset, you will try several baseline approaches to this problem, before using sklearn in Python to implement Naive Bayes and Logistic Regression classifiers. Finally, you will create a classifier of your own to this problem, and submit your predicted labels on a provided unlabeled test set. A leaderboard will be set up, so you can see how your final system compares to others in the class.

As with last week, you will submit your assignment via Gradescope.

## 1. Evaluation Metrics

Before we start with this text classification task, we need to first determine how we will evaluate our results. The most common metrics are precision, recall, and f-score.

For this problem, you will fill in the following functions:

- 'get_precision(y_pred, y_true)'
- 'get_recall(y_pred, y_true)'
- 'get_fscore(y_pred, y_true)'

Here, 'y_pred' is an 'nx1' list of predicted labels from a classifier, and 'y_true' is an 'nx1' list of the true labels, where 'n' is the number of datapoints.

You may not use sklearn's built-in functions for this, you must instead calculate these metrics manually. You will be using these functions to evaluate your classifiers later on in this assignment.

## 2. Complex Word Identification

Automated text simplification is a field in Natural Language Processing, where the goal is to take as input a complex text (e.g. a published journal article), and return a text that is more easily understood by a larger audience. One of the most logical first steps in text simplification, and example of text classification, is identifying which words in a text are hard to understand, i.e. 'complex', and which words are easy to understand, i.e. 'simple'.

For this problem, you will be given a dataset of words and their corresponding sentences, split into training, development, and test sets.

After taking a look at the datasets, we recommend that before you start this question, write a function 'load_file(data_file)', which takes in the file name of one of the datasets 'data_file', and reads in the words and labels from these files.

### 2.1: A very simple baseline

In the first problem, we are implementing a relatively easy baseline, to ensure you understand the process. For this baseline, fill in the function 'all_complex(data_file)'. This function takes in the file name of one of the datasets 'data_file', labels each word in the dataset as complex, and prints out the precision, recall, and fscore. 

Please report the precision, recall, and f-score using both the training data and the development data individually to be graded.

### 2.2: Word length thresholding

For our next baseline, we will use the length of each word, to determine word complexity. 

Specifically, in this problem, you should try setting various thresholds for word length. For example, you might set the threshold for 9, meaning that any words with length less than 9 will be labeled simple in this system, and any words with length at least 9 will be labeled complex. Once you find the best threshold using the training data, use this same threshold for the development data as well.

You will be filling in the function 'word_length_threshold(training_file, development_file)'. This function takes in both the training and development data files, and prints out the precision, recall, and fscore for your best threshold's performance on both the training and development data.

Please report the precision, recall, and f-score for the training and development data individually, along with the range of thresholds you tried, and the best threshold to be graded.


### 2.3: Word frequency thresholding

Our last baseline is similar to the previous baseline, but instead of thresholding on word length, you will be thresholding on word frequency. We have provided Google NGram frequencies in the text file 'ngram_counts.txt', along with the helper function 'load_ngram_counts(ngram_counts_file)' to load them into Python as a dictionary.

You will be filling in the function 'word_frequency_threshold(training_file, development_file, counts)', where 'counts' is the dictionary of word frequencies. This function again prints out the precision, recall, and fscore for your best threshold's performance on both the training and development data.

Please again report the precision, recall, and f-score on the training and development data individually, along with the range of thresholds you tried, and the best threshold to be graded.

Note: Due to its size, loading the ngram counts into Python takes around 20 seconds, and finding the correct threshold may take a few minutes to run.

### 2.4: Naive Bayes

Now, let's move on to actual Machine Learning classifiers! For our first classifier, you will use the built-in 'Naive Bayes' model from 'sklearn', to train a classifier. You may use the online 'sklearn' documentation to build your classifier. For features, you will simply use word length and word frequency as your two features. To import this model, use the following command:

{% highlight python %}
>>> from sklearn.naive_bayes import GaussianNB
{% endhighlight %}

In this problem, you will be filling in the function 'naive_bayes(training_file, development_file, counts). This function will train a 'Naive Bayes' classifier on the training data, and print your model's precision, recall, and f-score on the training data and the development data individually.

Please report the 'precision', 'recall', and 'f-score' on the training and development data individually.

Note 1:  There are two important things to point out: sklearn classifiers take in 'numpy' arrays, rather than regular lists. You may use the online 'numpy' documentation. To import 'numpy' into Python, use the following command:

{% highlight python %}
>>> import numpy as np
{% endhighlight %}

Note 2: Before training and testing a classifier, it is generally important to normalize your features. This means that you need to find the mean and standard deviation (sd) of a feature. Then, for each row, perform the following transformation:

X_scaled = (X_original - mean)/sd

Be sure to always use the means and standard deviations from the 'training data'.

### 2.5: Logistic Regression

Next, you will use the built-in 'Logistic Regression' from 'sklearn' to train a classifier. Again, we will use word length and word frequency as your two features. To import this model, use the following command:

{% highlight python %}
>>> from sklearn.linear_model import LogisticRegression
{% endhighlight %}

For this problem, you will be filling in the function 'logistic_regression(training_file, development_file, counts). This function will train a 'Logistic Regression' classifier on the training data, and print your model's precision, recall, and f-score on the training data and the development data individually.

Like Section 2.4, please report the 'precision', 'recall', and 'f-score' on the training and development data individually.

### 2.6: Comparison of Naive Bayes vs. Logistic Regression.

After implementing the previous two sections, you will notice that even though the 'Naive Bayes' and 'Logistic Regression' classifiers are given the same data, their performance is not identical. In this section, please discuss which model performed better on this task, and why you think this was the case.

### 2.7: Your own model

Finally, the fun part! In this section, you will build your own classifier for the complex word identification task, and compare your results to that of your classmates. You will also perform an error analysis for your best performing model.

#### 2.7.1: Model details

Unlike the previous sections, for this problem, you can choose any other types of classifier, and any additional features you can think of! For classifiers, beyond 'Naive Bayes' and 'Logistic Regression', you might consider trying 'SVM', 'Decision Trees', and 'Random Forests', among others. Additional features you may consider include number of syllables, as well as sentence-based complexity features, such as length of the sentence, average word length, etc. For counting the number of syllables, we have provided a python script 'syllables.py' that contains the function 'count_syllables(word)', which you may use.

When trying different classifiers, we recommend that you train on training data, and test on the development data, like the previous sections.

In your writeup, please include a description of all of the models and features that you tried.

Note: You can also tune the parameters of your model, e.g. what type of kernel to use. This is not required, as some of you may not be that familiar with this.


#### 2.7.2: Model Analysis

An important part of text classification tasks is determing exactly what your model is getting correct, and what your model is getting wrong. For this problem, you must train your best model on the training data, and report the precision, recall, and f-score on the development data.

In addition, need to perform a detailed error analysis of your models. Give several examples of words on which your best model performs well. Also give examples of words which your best model performs poorly on, and try to identify at least two categories of words on which your model is making errors.


#### 2.7.3: Testing your best model

Finally, train your best model on both the training and development data. You will use this classifier to predict labels for the test data, and will submit these labels in a text file named 'test_labels.txt' (with one label per line) to the leaderboard; be sure NOT to shuffle the order of the test examples. Instructions for how to post to the leaderboard will be posted on Piazza soon.

The baselines' performances will be included on the leaderboard. In order to receive full credit, your model must be able to outperform all of the baselines. In addition, the top 3 teams will receive 5 bonus points!

Good luck, and have fun!
