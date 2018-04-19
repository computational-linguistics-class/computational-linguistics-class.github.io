---
layout: default
img: python.jpg
img_link: http://xkcd.com/353/
caption: Hello world!
title: Text Summarization
active_tab: homework
term_project: true
---

# Text Summarization
Text summarization is the task of getting the most important ideas from a document or text. There are two types of text summarization: extractive and abstractive. Extractive text summarization involves taking sections of text directly from the document as the summary, while abstractive summarization rewrites or paraphrases the document/its main ideas. In this assignment, we will focus on extractive text summarization. You will implement:

* A simple, rule-based summarizer
* An atomic-event based summarizer
* Modifications to the event-based summarizer

An atomic event consists of two named entities in the same sentence (a relation) with a connector (a verb or action noun) between them. We define action nouns as WordNet hyponyms of "activity" or "event". For example, in the sentence "John hits Bob with his car." the named entities are John and Bob, the relation is John--Bob, and the connector is "hits". This model works with the hypothesis that important ideas in an article are likely those that appear frequently and are about one named entity acting upon another.

### Files to Download:
[data.tgz](https://drive.google.com/file/d/1I00XpcAUCbEgqpmR13Sp8_UcnOXzlQjP/view?usp=sharing): contains the data sets

[evaluation script](https://github.com/kashgupta/textsummarization/blob/master/score.py): reports precision, recall, and f-score using ROUGE

You may use packages from [spaCy](https://spacy.io/) to tokenize data, and do POS or named entity tagging.

# The Data:
The data for this assignment consists of approximately 300k articles from CNN and the Daily Mail, and comes from the the [DeepMind Q&A Dataset](https://cs.nyu.edu/~kcho/DMQA/). The 300k articles are divided into training, development, and test sets.  For the training and development sets, each line of the article file (bothtrain.txt and bothdev.txt) contains a cleaned, tab-separated article and its summary. The test set contains only article texts. The summary files will be used with the eval script. If you wish, you may use the original files from DeepMind to support some part of your implementation.

# Part 1: Basic Extractive Summarization
For part 1, you should implement a basic summarizer that takes in article text and outputs the first sentence of the article as the summary. Please make sure the summary output file is the same format as the sumonly files provided, as the evaluation script may not work otherwise. Report your precision, recall, and f-score with ROUGE-1 and ROUGE-2 in your writeup.

# Part 2: Event-Based Extractive Summarization
In this part of the assignment, instead of selecting the first sentence of the article, you will instead select the most "important" sentences. Importance is described by the number and weighting of the atomic events the sentence contains.

For this part of the assignment, you will need to implement the following functionalies:

1. Find all the atomic events in the article.
2. Get all sentences from the article
3. Count the frequency with which each relation (from those atomic events) appears in the article, ignoring differences in the connector
4. Count the frequency with which each connector appears within a specific relation (i.e. how many times "hits" is a connector for John--Mary in the article)
5. Calculate the weight of each atomic event. 
    * Let: (normalized relation weight of [RELATION1]) = (count of RELATION1 in article) / (total relation count)
    * Let: (normalized connector weight of [CONNECTOR1 in RELATION1]) = (# of times CONNECTOR1 is the connector for RELATION1) / (# of times RELATION1 appears in the aritle) 
    * Weight of ATOMIC_EVENT1 = (normalized CONNECTOR1 weight) * (normalized relation weight)
6. Create a matrix of atomic events by sentences. If an atomic event appears in the sentence, then (index_of_atomic_event, index_of_sentence) = the weight of the atomic event. Otherwise, 0.
7. Select the 3 sentences that have the highest total atomic event weights to extract to the summary

You can also try extracting more or fewer sentences, allowing for different kinds of words to be part of relations or connectors, or other methods to improve performance.


Report the results of any modifications you made, your ROUGE-1 and ROUGE-2 precision, recall, and f-score, and any interesting observasions about the model

Files containing the hyponyms can be found [here](https://github.com/kashgupta/textsummarization/blob/master/Milestone3_Submission/activity_hyponyms.txt) and [here](https://github.com/kashgupta/textsummarization/blob/master/Milestone3_Submission/event_hyponyms.txt).

# Part 3: DIY
Try at least two additional methods of summarizing the articles. These can build off your existing code in some way or use a different implementation altoghether. Explain what methods you attempted, whether they were effective, and why they may have been effective or ineffective in the writeup. Upload your best model's output to the leaderboard in a file called results.txt

Our model, the atomic event summarizer with very few modifications, produced ROUGE-1 precision: 0.253, recall: 0.561, and f-score 0.349. On ROUGE-2, precision: 0.126, recall: 0.038, f-score: 0.079. Your implementation should beat both f-scores for full credit.

Ideas for potential techniques include:
* Using features other than atomic events to rank sentences
* Using WordNet senses to identify important events
* Implementing a supervised extraction method using the training data

# Evaluation:
The evaluation script, score.py, generates the precision, recall, and f-score base on ROUGE. ROUGE is a metric that compares n-grams that appear in the predicted summary with those that appear in the gold summary. In this assignment, we consider the ROUGE-1 and ROUGE-2 score (unigrams and bigrams). [This](http://rxnlp.com/how-rouge-works-for-evaluation-of-summarization-tasks/) explains how the ROUGE precision, recall, and f-score is calculated for a single summary. The eval script calculates the ROUGE score over every summary in the test set and outputs the average. You can run the eval script with the following command line code:

```sh
$ python3 score.py --goldfile GOLDFILE --predfile PREDFILE --ngram N
```
For example, if you wanted to calculate the ROUGE-2 score:

```sh
$ python3 score.py --goldfile sumdata/bothtestsumonly.txt --predfile base_test_pred.txt --ngram 2
```

# Files to Submit
* Your code for Part 1, 2, and 3 in separate .py files
* Your predicted summaries for each part
* Your best model's predicted summaries in results.txt
* A README file explaining how to run your code
* A writeup.pdf explaining what you tried in each part, whether it worked, and why or why not that may be
