---
layout: default
img: up_goer_five.png
img_link: https://xkcd.com/thing-explainer/
caption: Thing Explainer - Complicated Stuff In Simple Words
title: Homework 2 "Text Classification"
active_tab: homework
release_date: 2018-01-17
due_date: 2018-01-24 11:00:00EST
attribution: Reno Kriz and Chris Callison-Burch developed this homework assignment for UPenn's CIS 530 class in Fall 2018.
readings:

-
   title: Naive Bayes Classification and Sentiment
   authors: Dan Jurafsky and James H. Martin
   venue: Speech and Language Processing (3rd edition draft)
   type: textbook
   url: https://web.stanford.edu/~jurafsky/slp3/6.pdf
-
   title: Logistic Regression
   authors: Dan Jurafsky and James H. Martin
   venue: Speech and Language Processing (3rd edition draft)
   type: textbook
   url: https://web.stanford.edu/~jurafsky/slp3/7.pdf
-
   title: Problems in Current Text Simplification Research&colon; New Data Can Help
   authors: Wei Xu, Chris Callison-Burch, and Courtney Napoles
   venue: TACL
   type: journal
   year: 2015
   url: http://www.cis.upenn.edu/~ccb/publications/new-data-for-text-simplification.pdf
   page_count: 16
   id: new-data-for-text-simplification
   abstract: Simple Wikipedia has dominated simplification research in the past 5 years. In this opinion paper, we argue that focusing on Wikipedia limits simplification research. We back up our arguments with corpus analysis and by highlighting statements that other researchers have made in the simplification literature. We introduce a new simplification dataset that is a significant improvement over Simple Wikipedia, and present a novel quantitative-comparative approach to study the quality of simplification data resources. 
   bibtex: |
      @article{Xu-EtAl:2015:TACL,
         author = {Wei Xu and Chris Callison-Burch and Courtney Napoles},
         title = {Problems in Current Text Simplification Research: New Data Can
       Help},
         journal = {Transactions of the Association for Computational Linguistics},
         volume = {3},
         year = {2015},
         url = {http://www.cis.upenn.edu/~ccb/publications/new-data-for-text-simplification.pdf},
         pages = {283--297}
       }
-
   title:  Comparison of Techniques to Automatically Identify Complex Words
   authors: Matthew Shardlow
   venue: ACL
   type: journal
   year: 2013
   url: http://aclweb.org/anthology/P/P13/P13-3015.pdf
   page_count: 7
   id: comparison-of-techniques
   abstract: Identifying complex words (CWs) is an important, yet often overlooked, task within lexical simplification (The process of automatically replacing CWs with simpler alternatives). If too many words are identified then substitutions may be made erroneously, leading to a loss of meaning. If too few words are identified then those which impede a user's understanding may be missed, resulting in a complex final text. This paper addresses the task of evaluating different methods for CW identification. A corpus of sentences with annotated CWs is mined from Simple Wikipedia edit histories, which is then used as the basis for several experiments. Firstly, the corpus design is explained and the results of the validation experiments using human judges are reported. Experiments are carried out into the CW identification techniques of&colon; simplifying everything, frequency thresholding and training a support vector machine. These are based upon previous approaches to the task and show that thresholding does not perform significantly differently to the more naive technique of simplifying everything. The support vector machine achieves a slight increase in precision over the other two methods, but at the cost of a dramatic trade off in recall.
   bibtex: |
      @InProceedings{shardlow:2013:SRW,
  author    = {Matthew Shardlow},
  title     = {A Comparison of Techniques to Automatically Identify Complex Words},
  booktitle = {51st Annual Meeting of the Association for Computational Linguistics Proceedings of the Student Research Workshop},
  year      = {2013},
  address   = {Sofia, Bulgaria},
  publisher = {Association for Computational Linguistics},
  pages     = {103--109},
}
-
   title:  SemEval 2016 Task 11&colon; Complex Word Identification
   authors: Gustavo Paetzold and Lucia Specia
   venue: ACL
   type: journal
   year: 2016
   url: https://www.researchgate.net/profile/Gustavo_Paetzold/publication/305334627_SemEval_2016_Task_11_Complex_Word_Identification/links/57bab70a08ae14f440bd9722/SemEval-2016-Task-11-Complex-Word-Identification.pdf
   page_count: 10
   id: SemEval-2016
   abstract: We report the findings of the Complex Word Identification task of SemEval 2016. To create a dataset, we conduct a user study with 400 non-native English speakers, and find that complex words tend to be rarer, less ambiguous and shorter. A total of 42 systems were submitted from 21 distinct teams, and nine baselines were provided. The results highlight the effectiveness of Decision Trees and Ensemble methods for the task, but ultimately reveal that word frequencies remain the most reliable predictor of word complexity.
   bibtex: |
      @InProceedings{paetzold-specia:2016,
  author    = {Gustavo Paetzold and Lucia Specia},
  title     = {SemEval 2016 Task 11&colon; Complex Word Identification},
  booktitle = {Proceedings of the 10th International Workshop on Semantic Evaluation (SemEval-2016)},
  year      = {2016},
  address   = {San Diego, California},
  publisher = {Association for Computational Linguistics},
  pages     = {560--569},
}
---

<!-- Check whether the assignment is up to date -->
{% capture this_year %}{{'now' | date: '%Y'}}{% endcapture %}
{% capture due_year %}{{page.due_date | date: '%Y'}}{% endcapture %}
{% if this_year != due_year %}
<div class="alert alert-danger" markdown="1">
Warning: this assignment is out of date.  It may still need to be updated for this year's class.  Check with your instructor before you start working on this assignment.
</div>
{% endif %}
<!-- End of check whether the assignment is up to date -->


<div class="alert alert-info" markdown="1">
This assignment is due on {{ page.due_date | date: "%A, %B %-d, %Y" }} before {{ page.due_date | date: "%I:%M%p" }}.   This assignment may be done with a partner.
</div>


Text Classification <span class="text-muted">: Assignment 2</span>
=============================================================

For this assignment, we'll be building a text classifier.  The goal of our text classifer will be to distinguish between words that are simple and words that are complex.  Example simple words are *heard, sat, feet, shops, town*, and example complex words are *abdicate, detained, liaison, vintners*. Distinguishing between simple and complex words is the first step in a larger NLP task called text simplification, which aims to replace complex words with simpler synonyms.  Text simplification is potentially useful for re-writing texts so that they can be more easily understood by younger readers, people learning English as a second language, or people with learning disabilities.

The learning goals of this assignment are:
* Understand an important class of NLP evaluation methods (precision, recall and F1), and implement them yourself.
* Employ common experimental design practices in NLP.  Split the annotated data into training/development/test sets, implement simple baselines to determine how difficult the task is, and experiment with a range of features and models.
* Get an introduction to sklearn, an excellent machine learning Python package.

We will provide you with training and development data that has been manually labeled. We will also give you a test set without labels. You will build a classifier to predict the labels on our test set.  You can upload your classifier's predictions to Gradescope. We will score its predictions and maintain a leaderboard showing whose classifier has the best performance.


<div class="alert alert-info" markdown="1">
Here are the materials that you should download for this assignment:
* [Skeleton code](downloads/hw2/hw2_skeleton.py) - this provides some of the functions that you should implement.
* [Data sets](downloads/hw2/data.tar.gz) - this is a tarball with the training/dev/test sets. 
* [Unigram counts](http://www.cis.upenn.edu/~cis530/18sp/data/ngram_counts.txt.gz) from the [Google N-gram corpus](https://research.googleblog.com/2006/08/all-our-n-gram-are-belong-to-you.html).
</div>


## Identifying Complex Words

Automated text simplification is an NLP task, where the goal is to take as input a complex text, and return a text that is easier to understand. One of the most logical first steps in text simplification, and example of text classification, is identifying which words in a text are hard to understand, and which words are easy to understand.

We have prepared a labeled training set for this assignment. We provide a dataset of words and their corresponding sentences that has been split into training, development, and test sets. The training set is disjoint, so if a word appears in the training set, it will not also appear in the test set or the development set.

This dataset was collected by taking the first 200 tokens in 200 complex texts, and crowdsourcing human judgements. We asked nine human annotators to identify at least 10 complex words in each text. From here, words that were identified as complex by at least 3 annotators were labeled as complex. In addition, words that were identified as complex by zero annotators were labeled as simple. One thing to note is that we kept only nouns, verbs, adjectives, and adverbs, and removed stopwords (i.e. common words like `the` or `and`) and proper nouns. After this filtering, we were left with 5,922 unique words. For this homework, we split these words up into 4,000 words for training, 1,000 words for development, and the remaining 922 words are reserved for testing.

Shown below is an example of the training data. Note that the training data and development data files have the same formatting, and the test data does not include the label column:

| WORD | LABEL |  ANNOTATORS  | SENTENCE | SENTENCE_INDEX |
| :--- |:-----:| :--------: | :------  | :------------: |
| jumping | 0 | 0 | `` Coleman with his jumping frog -- bet stranger $ 50 -- stranger had no frog &amp; C got him one -- in the meantime stranger filled C 's frog full of shot &amp; he could n't jump -- the stranger 's frog won . '' | 4 |
| paths | 0 | 0 | The Cannery project will feature drought-tolerant landscaping along its bike paths , and most of the front yards will be landscaped with low-water plants in place of grass . | 10|
| banks | 0 | 0 | Extending their protests into the workweek , Hong Kong democracy activists continued occupying major thoroughfares Monday , forcing the closure of some schools , banks and other businesses in the semi-autonomous Chinese territory . | 24 |
| fair-weather | 1 | 5 | Months ago , many warned him not to invest in a place where fair-weather tourists flee in the fall and the big lake 's waters turn cold and storm-tossed , forcing the 100 or so hardy full-time residents of Cornucopia to hibernate for the winter . | 13 |
| krill | 1 | 7 | But unlike the other whales , the 25-foot-long young adult stuck near the surface -- and it did n't dive down to feast on the blooms of krill that attract humpbacks to the bay . | 27 |
| affirmed | 1 | 8 | CHARLESTON , S.C. -- A grand jury affirmed the state of South Carolina 's murder charge on Monday against a white former North Charleston police officer who fatally shot an unarmed black man trying to run from a traffic stop . | 7 |


Here is what the different fields in the file mean:
* WORD: The word to be classified
* LABEL: 0 for simple words, 1 for complex words
* ANNOTATORS: The number of annotators who labled the word as complex
* SENTENCE: The sentence that was shown to annotators when they labeled the word as simple or complex
* SENTENCE_INDEX: The index of the word in the sentence (0 indexed, space delimited).

After taking a look at the datasets, we recommend that you write the `load_file(data_file)` function, which takes in the file name (`data_file`) of one of the datasets, and reads in the words and labels from these files.

Note: While the context from which each word was found is provided, you do not need it for the majority of the assignment. The only time you may need this is if you choose to implement any context-based features in your own classifier in Section 4.


## 1. Implement the Evaluation Metrics

Before we start with this text classification task, we need to first determine how we will evaluate our results. The most common metrics for evaluating binary classification (especially in cases of class imbalance) are precision, recall, and f-score.

For this problem, you will fill in the following functions:

* `get_precision(y_pred, y_true)`
* `get_recall(y_pred, y_true)`
* `get_fscore(y_pred, y_true)`

Here, `y_pred` is list of predicted labels from a classifier, and `y_true` is a list of the true labels.

You may **not** use sklearn's built-in functions for this, you must instead write your own code to calculate these metrics. You will be using these functions to evaluate your classifiers later on in this assignment.

We recommend that you also write a function `test_predictions(y_pred, y_true)`, which prints out the precision, recall, and f-score. This function will be helpful later on!

## 2. Baselines

### Implement a majority class baseline

You should start by implementing simple baselines as classifiers. Your first baseline is a majority class baseline which is one of the most simple classifier. You should complete the function `all_complex(data_file)`, which takes in the file name of one of the datasets, labels each word in the dataset as complex, and returns out the precision, recall, and f-score.

Please report the precision, recall, and f-score on both the training data and the development data individually to be graded.

### Word length baseline

For our next baseline, we will use a slightly complex baseline, the length of each word to predict its complexity.

For the word length baseline, you should try setting various thresholds for word length to classify them as simple or otherwise. For example, you might set a threshold of 9, meaning that any words with less than 9 characters will be labeled simple, and any words with 9 characters or more will be labeled complex. Once you find the best threshold using the training data, use this same threshold for the development data as well.

You will be filling in the function `word_length_threshold(training_file, development_file)`. This function takes in both the training and development data files, and returns out the precision, recall, and f-score for your best threshold's performance on both the training and development data.

Usually, Precision and Recall are inversely related and while building binary-classification systems we try to find a good balance between them (by maximizing f-score, for example). It is often useful to plot the Precision-Recall curve for various settings of the classifier to gauge its performance and compare it to other classifiers. For example, for this baseline, a Precision-Recall curve can be plotted by plotting the Precision (on the y-axis) and Recall (on the X-axis) for different values of word-length threshold.

In your write-up, please report the precision, recall, and f-score for the training and development data individually, along with the range of thresholds you tried. Also plot the Precision-Recall curve for the various thresholds you tried. For plotting, [matplotlib](https://matplotlib.org/) is a useful python library.

### Word frequency baseline

Our final baseline is a classifier similar to the last one, but thresholds on word frequency instead of length. We have provided Google NGram frequencies in the text file `ngram_counts.txt`, along with the helper function `load_ngram_counts(ngram_counts_file)` to load them into Python as a dictionary.

You will be filling in the function `word_frequency_threshold(training_file, development_file, counts)`, where `counts` is the dictionary of word frequencies. This function again returns the precision, recall, and fscore for your best threshold's performance on both the training and development data.

Please again report the precision, recall, and f-score on the training and development data individually, along with the range of thresholds you tried, and the best threshold to be graded. Similar to the previous baseline, plot the Precision-Recall curve for range of thresholds you tried. Also, make a third plot that contains the P-R curve for both the baseline classifier. Which classifier looks better *on average*?

Note: Due to its size, loading the ngram counts into Python takes around 20 seconds, and finding the correct threshold may take a few minutes to run.


## 3. Classifiers

### Naive Bayes classification

Now, let's move on to actual machine learning classifiers! For our first classifier, you will use the built-in Naive Bayes model from sklearn, to train a classifier. You should refer to the online [sklearn documentation](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html) when you are building your classifier. 

The first thing to note is that sklearn classifiers take in `numpy` arrays, rather than regular lists. You may use the online `numpy` documentation. To create a `numpy` list of length 5, you can use the following Python commands:

{% highlight python %}
>>> import numpy as np
>>> X = np.array([1,2,3,4,5])
{% endhighlight %}

To train a classifier, you need two `numpy` arrays: `X_train`, an `m` by `n` array, where `m` is the number of words in the dataset, and `n` is the number of features for each word; and `Y`, an array of length `m` for the labels of each of the words. Once we have these two arrays, we can fit a Naive Bayes classifier using the following commands:

{% highlight python %}
>>> from sklearn.naive_bayes import GaussianNB
>>> clf = GaussianNB()
>>> clf.fit(X_train, Y)
{% endhighlight %}

Finally, to use your model to predict the labels for a set of words, you only need one `numpy` array: `X_test`, an `m'` by `n` array, where `m'` is the number of words in the test set, and `n` is the number of features for each word. Note that the `n` used here is the same as the `n` in `X_train`. Then, we can use our classifier to predict labels using the following command:

{% highlight python %}
>>> Y_pred = clf.predict(X_test)
{% endhighlight %}

You should fill in the function `naive_bayes(training_file, development_file, counts)`. This function will train a `Naive Bayes` classifier on the training data using word length and word frequency as features, and returns your model's precision, recall, and f-score on the training data and the development data individually.

In your write-up, please report the precision, recall, and f-score on the training and development data for your Naive Bayes classifier that uses word length and word frequency.

NOTE: Before training and testing a classifier, it is generally important to normalize your features. This means that you need to find the mean and standard deviation (sd) of a feature. Then, for each row, perform the following transformation:

`X_scaled = (X_original - mean)/sd`

Be sure to always use the means and standard deviations from the `training data`.

### Logistic Regression

Next, you will use sklearn's built-in Logistic Regression classifier. Again, we will use word length and word frequency as your two features. You should refer to the online [sklearn documentation](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) when you are building your classifier. To import and use this model, use the following command:

{% highlight python %}
>>> from sklearn.linear_model import LogisticRegression
>>> clf = LogisticRegression()
{% endhighlight %}

For this problem, you will be filling in the function `logistic_regression(training_file, development_file, counts)`. This function will train a `Logistic Regression` classifier on the training data, and returns your model's precision, recall, and f-score on the training data and the development data individually.

Again, please report the precision, recall, and f-score on the training and development data.

### Comparing Naive Bayes and Logistic Regression

After implementing Naive Bayes and Logistic Regression classifiers, you will notice that their performance is not identical, even though they are given the same data. Add a paragraph to your write up that discusses which model performed better on this task.

## 4. Build your own model

Finally, the fun part! In this section, you will build your own classifier for the complex word identification task, and compare your results to that of your classmates. You will also perform an error analysis for your best performing model.

You can choose any other types of classifier, and any additional features you can think of! For classifiers, beyond Naive Bayes and Logistic Regression, you might consider trying `SVM`, `Decision Trees`, and `Random Forests`, among others. Additional word features that you might consider include number of syllables, number of WordNet synonyms, and number of WordNet senses . For counting the number of syllables, we have provided a python script [syllables.py](downloads/hw2/syllables.py) that contains the function `count_syllables(word)`, which you may use. To use WordNet in Python, refer to this [documentation](http://www.nltk.org/howto/wordnet.html). You could also include  sentence-based complexity features, such as length of the sentence, average word length, and average word frequency. 

When trying different classifiers, we recommend that you train on training data, and test on the development data, like the previous sections.

In your writeup, please include a description of all of the models and features that you tried. To receive full credit, you MUST try at least 1 type of classifier (not including Naive Bayes and Logistic Regression), and at least two features (not including length and frequency).

Note: You can also tune the parameters of your model, e.g. what type of kernel to use. This is NOT required, as some of you may not be that familiar with this.

### Analyze your model

An important part of text classification tasks is to determine what your model is getting correct, and what your model is getting wrong. For this problem, you must train your best model on the training data, and report the precision, recall, and f-score on the development data.

In addition, need to perform a detailed error analysis of your models. Give several examples of words on which your best model performs well. Also give examples of words which your best model performs poorly on, and identify at least TWO categories of words on which your model is making errors.


### Leaderboard

Finally, train your best model on both the training and development data. You will use this classifier to predict labels for the test data, and will submit these labels in a text file named `test_labels.txt` (with one label per line) to the leaderboard; be sure NOT to shuffle the order of the test examples. Instructions for how to post to the leaderboard will be posted on Piazza soon.

The performances of the baselines will be included on the leaderboard. In order to receive full credit, your model must be able to outperform all of the baselines. In addition, the top 3 teams will receive 5 bonus points!

### (Optional) Leaderboard using outside data

While the training data we have provided is sufficient for completing this assignment, it is not the only data for the task of identifying complex words. As an optional addition to this homework, you may look for and use any additional training data, and submit your predicted labels to a separate leaderboard.

As a start, we recommend looking at the [SemEval 2016 dataset](http://alt.qcri.org/semeval2016/task11/), a dataset that was used in a complex words identification competition. In addition, you can try to use data from [Newsela](https://newsela.com). Newsela's editors re-write newspaper articles to be appropriate for students at different grade levels.  The company has generously shared a dataset with us.  The Newsela data **may not** be re-distributed outside of Penn.  You can find the data on eniac at `/home1/c/ccb/data/newsela/newsela_article_corpus_with_scripts_2016-01-29.1.zip`.

Good luck, and have fun!




## 5. Deliverables 
<div class="alert alert-warning" markdown="1">
Here are the deliverables that you will need to submit:
* Your code. This should implement the skeleton files that we provide.  It should be written in Python 3.
* Your model's output for the test set using only the provided training and development data.   
* (Optional) your model's output for the test set, using any data that you want.
* Your writeup in the form of a PDF.
</div>


## 6. Recommended readings

<table>
   {% for publication in page.readings %}
    <tr>
      <td>
	{% if publication.url %}
		<a href="{{ publication.url }}">{{ publication.title }}.</a>
        {% else %}
		{{ publication.title }}.
	{% endif %}
	{{ publication.authors }}.
	{{ publication.venue }}  {{ publication.year }}.

	{% if publication.abstract %}
	<!-- abstract button -->
	<a data-toggle="modal" href="#{{publication.id}}-abstract" class="label label-success">Abstract</a>
	<!-- /.abstract button -->
	<!-- abstract content -->
	<div id="{{publication.id}}-abstract" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="{{publication.id}}">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title" id="{{publication.id}}">{{publication.title}}</h4>
        </div><!-- /.modal-header -->
        <div class="modal-body">
        {{publication.abstract}}
        </div><!-- /.modal-body -->
	</div><!-- /.modal-content -->
	</div><!-- /.modal-dialog -->
	</div><!-- /.abstract-content -->
	{% endif %}
		{% if publication.bibtex %}
	<!-- bibtex button -->
	<a data-toggle="modal" href="#{{publication.id}}-bibtex" class="label label-default">BibTex</a>
	<!-- /.bibtex button -->
	<!-- bibtex content -->
	<div id="{{publication.id}}-bibtex" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="{{publication.id}}">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title" id="{{publication.id}}">{{publication.title}}</h4>
        </div><!-- /.modal-header -->
        <div class="modal-body">
 	   <pre>{{publication.bibtex}}
           </pre>
        </div><!-- /.modal-body -->
	</div><!-- /.modal-content -->
	</div><!-- /.modal-dialog -->
	</div><!-- /.bibtex-content -->
	{% endif %}
</td></tr>
  {% endfor %}
</table>
