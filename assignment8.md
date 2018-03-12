---
layout: default
img: hypernyms.png
caption: Birds are Aves
img_link: https://xkcd.com/867/
title: Homework 8 - Learning Hypernyms
active_tab: homework
release_date: 2018-03-14
due_date: 2018-03-21T11:00:00EST
attribution: Nitish Gupta and Chris Callison-Burch developed this homework assignment for UPenn's CIS 530 class in Spring 2018.
readings:
-
   title: Learning syntactic patterns for automatic hypernym discovery
   authors:  Rion Snow, Daniel Jurafsky, Andrew Y. Ng
   venue: NIPS
   type: conference
   year: 2003
   url: http://papers.nips.cc/paper/2659-learning-syntactic-patterns-for-automatic-hypernym-discovery.pdf
   id: snow-patterns
-
   title: Automatic acquisition of hyponyms from large text corpora
   authors:  Marti Hearst
   venue: ACL
   type: conference
   year: 1992
   url: http://www.aclweb.org/anthology/C92-2082
   id: hearst-patterns
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

Learning Hypernyms <span class="text-muted">: Assignment 8</span>
=============================================================

In linguistics, *Hypernymy* is an important lexical-semantic relationship that captures the *type-of* relation. In this relation, a **hyponym** is a word or phrase whose semantic field is included within that of another word, its **hypernym**. For example, *rock*, *blues* and *jazz* are all hyponyms of *music genre* (hypernym).

In this assignment, we will examine unsupervised and supervised techniques to automatically extract a list of word pairs that satisfy the hypernymy relation using a large corpus. Specifically, we will use
1. A rule-based technique, specifically lexico-syntactic patterns, to extract hyponym-hypernym word pairs.
2. Another rule-based technique but using dependency-paths
3. A supervised approach that uses dependency-path features to learn a classifier to predict whether a given word-pair exhibit the hypernymy relationship.
In this assignment, we will be using *nltk*, *spacy* and *scikit-learn*.

<!-- <div class="alert alert-warning" markdown="1">
In order to use the gensim package, you'll have to be using Python version 3.6 or higher.  On my Mac, I did the following:
* `brew install python3`
* `pip3 install gensim`
* Then when I ran python, I used the command `python3` instead of just `python`
</div> -->

<div class="alert alert-info" markdown="1">
Here are the materials that you should download for this assignment:
* [`question1.txt`](downloads/hw4/question1.txt) A template for answering question 1.
* [`data.zip`](downloads/hw4/data.zip) Contains all the data
* [`vectorcluster.py`](downloads/hw4/vectorcluster.py) Main code stub
* [`evaluate.py`](downloads/hw4/evaluate.py) Evaluation script
* [`writeup.tex`](downloads/hw4/writeup.tex) Report template.
* [`makecooccurrences.py`](downloads/hw4/makecooccurrences.py) Script to make cooccurrences (optional use)
* [Tokenized Reuters RCV1 Corpus](http://www.cis.upenn.edu/~cis530/18sp/data/reuters.rcv1.tokenized.gz)
* [Google's pretrained word2vec vectors](https://code.google.com/archive/p/word2vec/), under the heading "Pretrained word and phrase vectors"
</div>

# Part 1: Lexico-Syntactic Patterns aka Hearst Patterns for Hypernym Learning

Explain what Hearst Patterns are...
```
Example of a hearst pattern
```

**Dataset**: Our dataset, Bless2011 cleaned by Levy et al. Use this to prune Wikipedia to contain sentences with the word pair in train/val/test.

**Wikipedia Corpus**: Contains tokenized sentence and tokenized-lemmatized sentence in tab-separated form. Each new line is a new sentence

Use this code (python code) to run NLTK POS Tagger, hand-written chunker to first find NP chunks. Then use NLTK's regex matcher to implement Hearst Patterns to find hypernymy word-pairs.

In this function, *func* you should implement other Hearst Patterns and other patterns you might seem fit. Also try using the lemmatized

Use this code, to predict True/False for the val data. Use best performing patterns for Leaderboard submision on test data.

# Part 2: Dependency Paths for Hypernym Learning

Consider the sentence snippet, *... such green vegetables as spinach, peas and kale.* and its dependency-parse using [spaCy](https://spacy.io/)

<img src="/assets/img/deppath.png" alt="Example dependency path using spaCy" style="width: 100%;"/>

We will use the shortest dependency path between noun (noun-chunk) pairs to predict hypernymy relation. For example, in the example above the shortest dependency path between *vegetables* and *spinach* is
```
vegetables/NOUN -> Prep -> as/ADP -> pobj -> spinach/NOUN
```


For generalization, we will anonymize the start and end-points of the paths, as
```
X/NOUN -> Prep -> as/ADP -> pobj -> Y/NOUN
```
and can now predict that when a (X,Y) pair has such a dependency-path between them, it usually means that X is the hypernym of Y.


Two issues:
* **Better lexico-syntactic paths**: Satellite edges as in Snow et al. explain
* **Distributive Edges**: To bypass paths of conjunctions

In the given file, *wikipedia_deppaths.txt* we have already extracted dependency-paths between relevant word/chunk pairs upto a length of 4.
Using training data, figure out which paths are good to capture hypernymy relation and use that to predict the truth for hypernymy relation between word pairs in val and test data.
Submit to leaderboard again.

<!-- {% highlight python %}
from gensim.models import KeyedVectors
vecfile = 'GoogleNews-vectors-negative300.bin'
vecs = KeyedVectors.load_word2vec_format(vecfile, binary=True)
{% endhighlight %} -->




# Part 3: Dependency-path as features
Use the dependency path edges as features and learn a classifier using the training data provided.


### 3. The Leaderboard
Apparently, 3 leaderboards

### Extra Credit
Need to figure out what can be done for this.


## Deliverables
<div class="alert alert-warning" markdown="1">
Here are the deliverables that you will need to submit:
* Hearst Patterns analysis
* Dependency Paths analysis
* What worked better and why do you think so?
* Supervised Classifier details and performance analysis
* `writeup.pdf` (compiled from `writeup.tex`)
* your code (.zip). It should be written in Python 3.
</div>


## Recommended readings

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

<!-- ### HW4 Rubric
60 points total. Example baseline implementations are available [here](downloads/hw4/hw4_solutions.py).

## Questions (10 pts)
1. (1 pts)
2. (3 pts)
3. (3 pts)
4. (3 pts)

## Leaderboard entry (30 pts)
+ 5 top-3
+ 3 top-10
- 5 miss lower baseline
- 10 submitted results for dev set

## Writeup (20 pts)
1. Sparse vectors (8 pts)
  - -4 does not describe VSM, or description unclear
  - -3 does not describe clustering algorithm, or unclear
  - -4 does not include preliminary experimental results

2. Dense vectors (8 pts)
  - -4 does not describe VSM, or description unclear
  - -3 does not describe clustering algorithm, or unclear
  - -4 does not include preliminary experimental results

3. Error analysis (4 pts)
  - -2 reports comparison of methods, without analysis

## Extra Credit
+ 5 Submitted solution to test_nok_input.txt and description in writeup
+ 3 top-3 -->
