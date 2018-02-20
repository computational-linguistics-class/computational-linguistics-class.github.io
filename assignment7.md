---
layout: default
img: bobbytables.png
caption: If word contains '); label as PER
img_link: https://xkcd.com/327/   
title: Homework 7 - Named Entity Recognition
active_tab: homework
release_date: 2018-02-21
due_date: 2018-02-28T11:00:00EST
attribution: This assignment is inspired by a similar assignment from Michael Elhadad's [NLP class](https://www.cs.bgu.ac.il/~elhadad/nlp17.html) at Ben-Gurion University of the Negev. Stephen Mayhew developed this homework assignment for UPenn's CIS 530 class in Spring 2018.
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
This assignment is due before {{ page.due_date | date: "%I:%M%p" }} on {{ page.due_date | date: "%A, %B %-d, %Y" }}.
</div>

Named Entity Recognition <span class="text-muted">: Assignment 7</span>
=============================================================


Since you have read Jurafsky and Martin chapter [21](https://web.stanford.edu/~jurafsky/slp3/21.pdf), you know that Named Entity Recognition is the task of finding and classifying named entities in text. This task is often considered a sequence tagging task, like part of speech tagging, where words form a sequence through time, and each word is given a tag. Unlike part of speech tagging however, NER usually uses a relatively small number of tags, where the vast majority of words are tagged with the 'non-entity' tag, or O tag.

Your task is to implement your own named entity recognizer. Relax, you'll find it's a lot easier than it sounds, and it should be very satisfying to accomplish this. There will be two versions of this task: the first, the constrained version, is the required entity tagger that you implement using scikit learn, filling out the stub that we give you. The second is an unconstrained optional version where you use whatever tool, technique, or feature you can get your hands to get the best possible score on the dataset. There will be a leaderboard for each version.

As with nearly all NLP tasks, you will find that the two big points of variability in NER are (a) the features, and (b) the learning algorithm, with the features arguably being the more important of the two. The point of this assignment is for you to think about and experiment with both of these. Are there interesting features you can use? What latent signal might be important for NER? What have you learned in the class so far that can be brought to bear?

Get a headstart on common NER features by looking at Figure 21.5 in the textbook. 


## The Data

The data we use comes from the Conference on Natural Language Learning (CoNLL) 2002 shared task of named entity recognition for Spanish and Dutch. The [introductory paper to the shared task](http://www.aclweb.org/anthology/W02-2024) will be of immense help to you, and you should definitely read it. You may also find the [original shared task page](https://www.clips.uantwerpen.be/conll2002/ner/) helpful. We will use the Spanish corpus (although you are welcome to try out Dutch too).  

The tagset is:
* *PER*: for Person
* *LOC*: for Location
* *ORG*: for Organization
* *MISC*: for miscellaneous named entities

We strongly recommend that you study the training and dev data (no one's going to stop you from examining the test data, but for the integrity of your model, it's best to not look at it). Are there idiosyncracies in the data? Are there patterns you can exploit with cool features? Are there obvious signals that identify names? For example, in some Turkish writing, there is a tradition of putting an apostrophe between a named entity and the morphology attached to it. A feature of `isApostrophePresent()` goes a long way. Of course, in English and several other languages, capitalization is a hugely important feature. In some African languages, there are certain words that always precede city names. 

The data is packaged nicely from [NLTK](http://www.nltk.org/). Get installation instructions here: [installing NLTK](http://www.nltk.org/install.html).

You will be glad to hear that the data is a mercifully small download. See the [NLTK data](http://www.nltk.org/data) page for for download options, but one way to get the conll2002 data is:

```
$ python -m nltk.downloader conll2002
```



## Evaluation

There are two common ways of evaluating NER systems: phrase-based, and token-based. In phrase-based, the more common of the two, a system must predict the entire span correctly for each name. For example, say we have text containing "James Earle Jones", adn our system predicts "[PER James Earle] Jones". Phrase-based gives no credit for this because it missed "Jones", whereas token-based would give partial credit for correctly identifying "James" and "Earle" as B-PER and I-PER respectively. We will se phrase-based to report scores.

The output of your code must be `word gold pred`, as in:
```
La B-LOC B-LOC
Coruña I-LOC I-LOC
, O O
23 O O
may O O
( O O
EFECOM B-ORG B-ORG
) O O
. O O
```

Here's how to get scores:

```
# Phrase-based score
$ ./conlleval.py results
```

(The python version of conlleval doesn't calculate the token-based score, but if you really want it, you can use the [original perl version](https://www.clips.uantwerpen.be/conll2000/chunking/output.html). You would use the `-r` flag.)


## Other resources

Here are some other NER frameworks which you are welcome to run in the unconstrained version:
* [CogComp NER](https://github.com/CogComp/cogcomp-nlp/tree/master/ner), one of the best taggers
* [LSTM-CRF](https://github.com/glample/tagger), recent neural network tagger
* [Stanford NER](https://nlp.stanford.edu/software/CRF-NER.shtml), Stanford's tried and true tagger
* [spaCy](https://spacy.io/usage/training)
* [Brown clustering software](https://github.com/percyliang/brown-cluster). You might find it useful.
* [Spanish text and vectors](http://crscardellino.me/SBWCE/)
* [Europarl corpora](http://www.statmt.org/europarl/), look for the English-Spanish parallel text

Note: you are not allowed to use pre-trained NER models even in the unconstrained version. Please train your own. You are allowed to use pre-trained embeddings.

## Baselines

We have implemented a bog-standard NER system in scikit learn using CERTAIN FEATURES and a CERTAIN MODEL. This is a very generous baseline that any thoughtful model should be able to beat. 

As always, beating the baseline alone with earn you a B on the project. In order to earn an A, demonstrate that you have thought about the problem carefully, and come up with solutions beyond what was strictly required. 


## Deliverables 
<div class="alert alert-warning" markdown="1">
Here are the deliverables that you will need to submit:
* Code
* Constrained results (to the leaderboard)
* Optional unconstrained results
* PDF Report
</div>

## Recommended readings
* Jurafsky and Martin chapter [21](https://web.stanford.edu/~jurafsky/slp3/21.pdf)
* [Design Challenges and Misconeptions in Named Entity Recognition](http://cogcomp.org/papers/RatinovRo09.pdf) a very highly cited NER paper from a Penn professor
* [Entity Extraction is a Boring Solved Problem -- or is it?](https://aclanthology.info/pdf/N/N07/N07-2046.pdf)
* [Neural Architectures for Named Entity Recognition](https://arxiv.org/abs/1603.01360), a popular recent paper on... just read the title.
* [Introductory paper to CoNLL 2002 shared task](http://www.aclweb.org/anthology/W02-2024)