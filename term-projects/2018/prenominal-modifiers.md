---
layout: default
img: python.jpg
img_link: http://xkcd.com/353/
caption: Hello world!
title: Prenominal Modifiers
active_tab: homework
term_project: true
---

# Prenominal Modifiers 

## Background
Consider the English phrase, “the three tall gray U.S. government buildings.” From a computational perspective, it is not obvious why the technically-grammatically-sound variation, “the tall U.S. government gray three buildings,” is incorrect, yet all native English speakers have an intuition that most orderings other than the one below are wrong.
![](https://lh4.googleusercontent.com/h0QFd7WHjsVE41dfjhdImbRX8trb6uSZ5Mq8sj9kS8pzOV9H43-kVPecabR1VlU7BjGhBtef6jbanCYL34rm28TwPlWUDr-6bULa_vIN9H4PUJXl-TY4HWD6pNcU_W_p7RHBpqUg)

In this assignment, you will implement one of the cutting-edge NLP approaches to solving the problem of ordering these prenominal modifiers in English.

## Outline of Your Tasks
-   Generate the data from the Brown and Penn TreeBank corpora.
-   Train different models to learn and predict the best ordering of modifiers.
-   Random baseline model
-   Published baseline model using Liu and Haghighi’s “Maximum Entropy Reranking Approach”
-   Choose one extension to implement that improves upon this published baseline.
-   Evaluate the performance of these predictions using precision, recall, and F-score.
  
## Generating the Data
To generate the train/dev/test data, run: ```python3 extract-data.py```

First this script will extract all adjective sequences from the Brown and Penn TreeBank corpora, automatically downloading these corpora from nltk if they haven’t been downloaded already. Then, for each adjective sequence, it generates a line of training/dev/test data. Each line of train, dev, and test consists of a pair of space-separated adjectives, a tab, a noun, a tab, and a True/False value which is True if the first modifier correctly occurs before the second and False otherwise.

For example, the noun phrase "big brown bear" would generate:
```big brown bear  True``` 
```brown big  bear  False```

And the adjective list "big brown fluffy bear" would generate
```big brown  bear  True ``` 
```big fluffy  bear  True ``` 
```brown big  bear  False  ```
```fluffy big  bear  False  ```
```brown fluffy  bear  True  ```
```fluffy brown  bear  False```

Stats about the data you will be working with:
-   Brown Corpus (21,251 multi-adjective sequences)
-   Penn Treebank (2,833 multi-adjective sequences)

Train/Dev/Test Breakdown from extract-data.py
-   data/train.txt: 42,497 items (80%)
-   data/dev/txt: 5,312 lines (10%)

## Evaluation
Our evaluation metric is based on the number of correctly ordered adjective pairs in the predicted file, where a pair of predicted adjectives is 'correctly ordered' if it appears in the same order as it does in the gold file.

For example, consider the gold-standard noun phrase "big brown fluffy ", where cat is the noun, and "big", "brown", and "fluffy" are the adjectives. Let's say the predicted phrase is "fluffy big brown."

The predicted labels would look like this:
```big brown True```  
```big fluffy False  ```
```brown big False  ```
```fluffy big True```  
```brown fluffy False  ```
```fluffy brown True```

The gold labels would look like this:
```big brown True  ```
```big fluffy True  ```
```brown big False```  
```fluffy big False ``` 
```brown fluffy True  ```
```fluffy brown False```

In this example, the true positives are: ```big brown```. The false negatives are: ```big fluffy``` and ```brown fluffy```. The false positives are: ```fluffy big``` and ```fluffy brown```. The true negatives are: ```brown big```. The precision, recall, and f-score can then be computed from these intermediate values. The higher the f-score, the better.

To compute precision, recall, and F-score on the predicted data, run:
```python3 evaluate.py --goldfile <goldfilename> --predfile <predfilename>```

## Simple Baseline
Please create a simple baseline that predicts if a tuple is in the correct order. Create a dictionary mapping tuples ```(adjective1, adjective2)``` to their total number of occurrences. To predict the label for ```(adj1, adj2)```, return the value that the tuple maps to in the dictionary or randomly generate a label if the pair was never seen before.

This method achieved precision, recall, and F-score of between 50-51%. The state-of-the-art methods get around 90% accuracy, so the 50% random baseline should not be difficult to beat.

## Published Baseline: Prenominal Modifier Ordering Using Liu and Haghighi’s “Maximum Entropy Reranking Approach”

### Background
Your task is to, given a set B of prenominal modifiers, a noun phrase head H which B denoted 𝝅(B), design an algorithm that determines the “correct” natural-sounding ordering   of the modifiers in .

An example of input that the algorithm would receive is: 

B = {black, furry, tall}

H = cat

𝝅(B) = {(black, furry, tall), (black, tall, furry), (furry, tall, black), (furry, black, tall), (tall, black, furry), (tall, furry, black)}

With this information, your algorithm should output:
x* = (tall, black, furry)	

For each x in 𝝅(B), you will create a feature vector for *x* that will be used to calculate the probability that each ordering in 𝝅(B) is indeed the correct ordering. Then you will will find the permutation that has the highest probability of occuring with the noun.

## Your Task
Each line of your extracted data file contains a particular ordering of modifiers, the noun that the modifiers modify, and a boolean label denoting whether or not that modifier permutation is correct. Thus, you will apply the maximum entropy reranking algorithm to each line.

*Step 1*
Write a method ```kernel(x)``` that returns a feature vector based on the word tuple x. You might try experimenting with different features, for example:
-   Does the modifier in position *i*  contain a hyphen?
-   Was the modifier in position *i* seen in the training data?
-   Perhaps the majority of words that end with -ly are adverbs and should usually be positioned farthest from the head noun. Can you check whether the modifier in position *i* ends with a typical adverb suffix, such as “-al”, “-ble”, “-er”, or “-ly”?
-   Is the modifier in position *i* a number? Does it just start with a number?
-   Is the modifier in position *i* a color?
-   How long is the modifier in position *i*?
    
*Step 2*
Write a method ```prob(x, W)``` that finds the probability word tuple x occurring according to model W. The distribution over orderings x ∈ π(B) is given by
**![](https://lh6.googleusercontent.com/g5xKUnyVJLv-nB_QIfIUnZi_STdF8dwmvtkMmAYkZog_kmK_w-GUsgTPoUB0J5-gBaWsrJ6dI3gY4AJ1C5_ucCZc1IqTbytZrSCzfSs2kqc4dP2ELGjODwcW0gqdRytQyx5pdan-)**
where a 𝜙(B,H,x) is a feature vector over a particular ordering of the features B, and W is a learned weight vector over features.

*Step 3*
Write a method ```predict(x, W)``` that decides among all permutations of the words in tuple x which ordering is the most probable. In this method, you should be calling the ```prob(x,W)``` method.

*Step 4*
We need to, at training time, select W to maximize
**![](https://lh4.googleusercontent.com/xFxAoEK90ybu_dJH9hKRH5a1Czc9BrqzaqoGVfbgmKYcsBUfoTuLLHhJcXkacq1y9bIDbfB5LOOQUseLlu7-jLN78I22_OllMLSDok5W0YkseYgzPGYsbaP0le4Z0lVzantcW2KN)**
To do this, you can do this by writing a method called ```loss(W)``` that returns the negated value of aforementioned formula. The value is negated because you will then minimize the loss function with *scipy.optimize.minimize()*.

*Step 5*
Call the *scipy.optimize.minimize()* function in your main method. This optimization method will return optimal weights W* with which you can use to predict the labels of your development and validation sets. Do this by calling ```predict(x,W*)``` on each line.

*Step 6*
Evaluate your predicted labels against the gold labels by using score.py. Compare the performance of your model against the simple baseline.

*Helpful hints*
-   To prevent rewriting of the same code, try writing a separate method to parse a line into the form ```(<tuple-of-modifiers>, <noun-head>, <label>)```
-   Keep in mind that the vector W whose length is equal to the number of of distinct combinations of modifiers. This means the length of W will be equal to the number of lines in the file that have the *True* label. Before optimizing, initialize the initial W vector to random values.


### Extension 1: Google N-gram feature
Google published a [dataset of n-grams](https://research.googleblog.com/2006/08/all-our-n-gram-are-belong-to-you.html) and their frequency counts drawn from public webpages with a total of over one trillion tokens (about 1 billion unique 3-grams, 4-grams, and 5-grams and 300,000 bigrams). With all of this data, it is possible to compute the n-gram count for each permutation and add a feature that marks whether a permutation is the permutation of a set of modifiers with the highest count.

Implement this feature. How does it compare to the model without this feature? Discuss this in your writeup.

### Extension 2: Word2vec Similarity
This extension leverages word-embeddings to build more features into the model. In this extension, we want to use pre-trained Word2Vec vectors to predict class-based orderings of the premodifiers. In English, we can generalize the ordering of premodifiers types as number, opinion, size, age, shape, color, origin, material, purpose. Now, using Word2Vec vectors for this each of these classes, predict whether the ordering a set of premodifiers is correct. To do this, you can predict classes for each word in a certain ordering of premodifiers, and check whether it matches the general ordering mentioned above. Implement this extension, and in your writeup, discuss how your model performs.

You can download Google News Word2Vec here: [https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing)


## Writeup
Please report the performance of your different models.

Discuss how you implemented your extension to the published baseline. What features did you try in your model? Does one combination appear to work better than another? Do any interesting patterns emerge? Include this discussion in your writeup.

## Deliverables
Here are the deliverables you will need to submit:
-   writeup.pdf
-   code (.zip). It should It should be written in Python 3 and include a README.txt briefly explaining how to run it.
-   predictions.txt predictions for leaderboard.
    
## Recommended Readings
[“Ordering Prenominal Modifiers with a Reranking Approach”](https://aclanthology.info/pdf/P/P11/P11-1111.pdf) by Jenny Liui, Aria Haghighi of MIT, published in Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics, June 2011
[“Class-Based Ordering of Prenominal Modifiers”](http://www.m-mitchell.com/papers/Mitchell-10-prenominal_mods.pdf) by Margaret Mitchell at the Center for Spoken Language Understanding, published in Proceedings of the 12th European Workshop on Natural Language Generation, March 2009