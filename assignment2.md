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

Please again report the precision, recall, and f-score, along with the range of thresholds you tried, and the best threshold to be graded.


### 2.3: Word frequency thresholding

- You will use word frequencies to determine word complexity.
- We will provide Google NGram frequencies.
- You need to find the frequency for each word, and calculate the precision, recall, and f-score using various frequency thresholds.
- Report the range of thresholds attempted.
- Report the highest-performing frequency threshold you found on the training data (using f-score), as well as the precision, recall, and f-score of this threshold.
- Also report the precision, recall, and f-score of your best threshold on the development set.

### 2.4: Naive Bayes

- Next, you will use the built-in Naive Bayes model from sklearn, to train a classifier.
- Use word length and word frequency as your two features.
- Train your model on your training classifier.
- You will use 5-fold cross validation on the training data to calculate the precision, recall, and f-score.
- Also train your model on the full training data, and test your model on the development data. Report the precision, recall, and f-score.

### 2.5: Logistic Regression

- Next, you will use the built-in Logistic Regression model from sklearn, to train a classifier.
- Use word length and word frequency as your two features.
- Train your model on your training classifier.
- Like Section 2.4, use 5-fold cross validation on the training data to calculate the precision, recall, and f-score.
- Train your model on the full training data, test your model on the development data, again reporting the precision, recall, and f-score.

### 2.6: Comparison of Naive Bayes vs. Logistic Regression.

- In this section, explain which model performed better on this task, and why you think this is the case.

### 2.7: Your own model

- In this section, you need to come up with your own classifier.

#### 2.7.1: Model details

- You may use any additional features, as long as you explain why these features are important for identifying complex words.
- You may also use other types of classifiers (e.g. SVM, Decision Tree, etc.)
- To test different classifiers, train on the training data, and test on the development data.
- In your writeup, be sure to include a description of what you tried, as well as an in-depth analysis of your final model.

#### 2.7.2: Error Analysis.

- An important part of text classification tasks is determing exactly what your model is getting correct, and what your model is getting wrong.
- For this section, you will train your best model on the training data, and report the precision, recall, and f-score on the development data.
- You need to perform a detailed error analysis of your models.
- Give several examples of words on which your best model performs well, and that the length threshold and frequency threshold baselines do not.
- Also give examples of words which your best model performs poorly on, and try to identify at least two categories of words on which your model is making errors.

#### 2.7.3: Testing your best model

- Finally, train your best model on both the training and development data.
- You will use this classifier to predict labels for the test data, and will submit these labels (one label per line) to the leaderboard; this way you will be able to compare your model to others from the course.
- The baselines' performances will be included on the leaderboard; your model must be able to outperform all of them.
