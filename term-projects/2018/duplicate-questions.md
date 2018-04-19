---
layout: default
img: python.jpg
img_link: http://xkcd.com/353/
caption: Hello world!
title: Detecting Duplicate Questions
active_tab: homework
term_project: true
---


# Detecting Duplicate Questions

This assignment deals with detecting duplicate questions for community question-answering sites such as stackoverflow or Quora. In particular, the data and evaluation method for our assignment comes from [this Kaggle challenge](https://www.kaggle.com/c/quora-question-pairs) that was posted last year. Aside from removing duplicate questions on QA communities, this problem has broader applications as well, such as "recommended questions" on a customer service site and understanding how to process computational text in general.

While some duplicate questions pairs are easy to detect, majority of the duplicate question pairs have the same meaning but look different due to paraphrasing or reordering of the words. There are many ways to approach this assignment, including syntax modeling, sentence vector comparison, markov comparison, or using wordnet to process sentence pairs etc. A good solution will likely combine several of the above strategies into one. For the baseline of this project, you will implement a strategy that uses sentence-vector comparison. 

## Part 1: The Data

The data consists of over 400,000 question pairs taken from Quora, split into training, validation, and test sets in an 80:10:10 ratio (~300k, ~40k, ~40k question pairs). All questions were taken from Quora's site, though many are no longer posted. **NOTE:** some questions may be two or more sentences tied together (i.e. "Are there jobs for CFA candidates or charter holders in the US or the UK or EU ? I'm from India. What are my chances of getting one?" is all one question from the training data). **NOTE:** This dataset is quite large for this kind of task, so pay attention to memory limitations when implementing your algorithms!!

Read in the data as a CSV file. Each entry is comma-delineated and quoted. An example entry is provided here:
```
"id","qid1","qid2","question1","question2","is_duplicate"
"274226,"392826","392827","Is it hard to code a game like agar.io?","How do you program a game like agar.io?","0"
```
Before beginning, skim through the data to get an idea of the problems you may face. For example, duplicates could start with different question identifying words or use synonyms, while non-dupliactes could have the exact same words but in different order!

## Part 2: Evaluation

Evaluate your model using [log loss](http://wiki.fast.ai/index.php/Log_Loss). This evaluation metric requires the predicted output to be the proabability of the positive class (i.e. number between 0 and 1). Pay attention to which classifier/approach you use in part 4, because you will need to have all your predictions in this format. We chose to use this metric because the kaggle competition used this critiera for their evaluation. Plus, if you want to compare your implementation to the very best, you can look at the leaderboard [here](https://www.kaggle.com/c/quora-question-pairs/leaderboard).
  
## Part 3: Implementing Sentence-Vector Baseline

One way of detecting the similarity between two questions is to formulate them as sentence vectors and compare the vectors. (Sounds just like a [previous homework](http://computational-linguistics-class.org/assignment3.html) we've done in class). The beauty of this approach is that we can ignore all words that don't appear in either sentence. We use the sentence vector implementation from [this paper](https://pdfs.semanticscholar.org/96b8/ddc494ac1ff9599ae161e529ca6cc546b76d.pdf). The approach this paper takes is as follows:

1. POS tagging of the sentences
2. Form vectors for each sentence. Each entry in the vector should be the maximum similarity between that word and each word in the corresponding sentence.
3. Return the cosine similarity between the two vectors

## Part 4: Extend The Baseline

Improve on the baseline by implementing additional techniques. This could include examining question words (Who, What, When, etc), syntax trees and sentence structure, or other features. The implemented model must be coded by **yourself or group members**!! Some possible strategies are listed below:

  - Examine question words (Who, What, How...) to detect question type
  - Use a Markov model to compare n-tuples between questions
  - Parse question pairs to POS trees using nltk and compare the number of matching subtrees.
  - Use Named Entity Recognition (from [previous homework](http://computational-linguistics-class.org/assignment7.html)) to extract and compare Proper Nouns
  - Implement an LSTM model (like [Siamese LSTM](https://www.aaai.org/ocs/index.php/AAAI/AAAI16/paper/download/12195/12023) or [Tree LSTM](https://arxiv.org/pdf/1503.00075.pdf))
  - Use a Random Forest model (Quora used this model to mark duplicates before the competition!)

### Leaderboard
For friendly competition, we will have a leaderboard to see who has the best model in part 4. Write code that will print out a   `predictions.txt` file, which contains your models predicted probability for the duplicate class on separate lines. Extra credit will be giving to the top 5 on the leader board.

## Deliverables
For this homework assignment you will need to turn in the following:
  - code (.zip). Code needs to be written in **Python 3** and provide a README to explain how to run your code
  - `predictions.txt` for the leader board
