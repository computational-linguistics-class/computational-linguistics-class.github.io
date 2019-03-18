---
layout: default
img: bobbytables.png
caption: If word contains '); label as PER
img_link: https://xkcd.com/327/   
title: Homework 7 - Named Entity Recognition
active_tab: homework
release_date: 2018-02-21
due_date: 2018-03-03T12:00:00EST
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

Your task is to implement your own named entity recognizer. Relax, you'll find it's a lot easier than it sounds, and it should be very satisfying to accomplish this. You will implement an entity tagger using scikit learn, filling out the stub that we give you. There will be a leaderboard.

As with nearly all NLP tasks, you will find that the two big points of variability in NER are (a) the features, and (b) the learning algorithm, with the features arguably being the more important of the two. The point of this assignment is for you to think about and experiment with both of these. Are there interesting features you can use? What latent signal might be important for NER? What have you learned in the class so far that can be brought to bear?

Get a headstart on common NER features by looking at Figure 21.5 in the textbook. 

<div class="alert alert-info" markdown="1">
Here are the materials that you should download for this assignment:
* [Code stub](downloads/hw7/ner.py).
* [conlleval.py](downloads/hw7/conlleval.py): eval script
</div>


## The Data

The data we use comes from the Conference on Natural Language Learning (CoNLL) 2002 shared task of named entity recognition for Spanish and Dutch. The [introductory paper to the shared task](http://www.aclweb.org/anthology/W02-2024) will be of immense help to you, and you should definitely read it. You may also find the [original shared task page](https://www.clips.uantwerpen.be/conll2002/ner/) helpful. We will use the Spanish corpus (although you are welcome to try out Dutch too).  

The tagset is:
* *PER*: for Person
* *LOC*: for Location
* *ORG*: for Organization
* *MISC*: for miscellaneous named entities

The data uses BIO encoding (called IOB in the textbook), which means that each named entity tag is prefixed with a `B-`, which means beginning, or an `I-`, which means inside. So, for a multiword entity, like "James Earle Jones", the first token "James" would be tagged with "B-PER", and each subsequent token is "I-PER". The O tag is for non-entities.

We strongly recommend that you study the training and dev data (no one's going to stop you from examining the test data, but for the integrity of your model, it's best to not look at it). Are there idiosyncracies in the data? Are there patterns you can exploit with cool features? Are there obvious signals that identify names? For example, in some Turkish writing, there is a tradition of putting an apostrophe between a named entity and the morphology attached to it. A feature of `isApostrophePresent()` goes a long way. Of course, in English and several other languages, capitalization is a hugely important feature. In some African languages, there are certain words that always precede city names. 

The data is packaged nicely from [NLTK](http://www.nltk.org/). Get installation instructions here: [installing NLTK](http://www.nltk.org/install.html).

You will be glad to hear that the data is a mercifully small download. See the [NLTK data](http://www.nltk.org/data) page for for download options, but one way to get the conll2002 data is:

```
$ python -m nltk.downloader conll2002
```


## Evaluation

There are two common ways of evaluating NER systems: phrase-based, and token-based. In phrase-based, the more common of the two, a system must predict the entire span correctly for each name. For example, say we have text containing "James Earle Jones", and our system predicts "[PER James Earle] Jones". Phrase-based gives no credit for this because it missed "Jones", whereas token-based would give partial credit for correctly identifying "James" and "Earle" as B-PER and I-PER respectively. We will use phrase-based to report scores.

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

Here's how to get scores (assuming the above format is in a file called `results.txt`):

```
# Phrase-based score
$ python conlleval.py results.txt
```

(The python version of conlleval doesn't calculate the token-based score, but if you really want it, you can use the [original perl version](https://www.clips.uantwerpen.be/conll2000/chunking/output.html). You would use the `-r` flag.)


## Baselines

The version we have given you gets about 49% F1 right out of the box. We made some very simple modifications, and got it to 60%. This is a generous baseline that any thoughtful model should be able to beat. The state of the art on the Spanish dataset is about 85%. If you manage to beat that, then look for conference deadlines and start writing, because you can publish it.  

As always, beating the baseline alone with earn you a B on the project. In order to earn an A, demonstrate that you have thought about the problem carefully, and come up with solutions beyond what was strictly required. Extra credit for the top of the leaderboard etc.

## Report

1. Explain four features you added for NER, why you expected them to help, and how they affected your performance. Include a table detailing the change in F1-score as a result of adding each feature or set of features.
2. Explain the different types of models you experimented with, how they performed, and which you chose for your final model. Include a table comparing the scores of different models. For each model, be sure to tune your parameters and include tables recording the F1-score attained for each set of parameters. You will also need to submit your final, trained model. You can save your model to a file in the following way:

```
import pickle
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, Y_train)
filename = 'model'
pickle.dump(model, open(filename, 'wb'))
```

To load your model, you can use the following code:

```
loaded_model = pickle.load(open(filename, 'rb'))
```


## Deliverables 
<div class="alert alert-warning" markdown="1">
Here are the deliverables that you will need to submit:
* Code, as always, in Python 3.
* Saved model[model] - Your final trained model. Please put it in the same path as your code.
* Constrained results (in a file called `constrained_results.txt`)
* PDF Report (called writeup.pdf)
</div>



## Recommended readings
* Jurafsky and Martin chapter [21](https://web.stanford.edu/~jurafsky/slp3/21.pdf)
* [Design Challenges and Misconeptions in Named Entity Recognition](http://cogcomp.org/papers/RatinovRo09.pdf) a very highly cited NER paper from a Penn professor
* [Entity Extraction is a Boring Solved Problem -- or is it?](https://aclanthology.info/pdf/N/N07/N07-2046.pdf)
* [Neural Architectures for Named Entity Recognition](https://arxiv.org/abs/1603.01360), a popular recent paper on... just read the title.
* [Introductory paper to CoNLL 2002 shared task](http://www.aclweb.org/anthology/W02-2024)
