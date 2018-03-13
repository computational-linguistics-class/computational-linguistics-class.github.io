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
   venue: COLING
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

CCB todo: Add paragraph describing the usefulness of hypernym relations for tasks like Question Answering and RTE/NLI.

In linguistics, *Hypernymy* is an important lexical-semantic relationship that captures the *type-of* relation. In this relation, a **hyponym** is a word or phrase whose semantic field is included within that of another word, its **hypernym**. For example, *rock*, *blues* and *jazz* are all hyponyms of *music genre* (hypernym).

In this assignment, we will examine unsupervised techniques to automatically extract a list of word pairs that satisfy the hypernymy relation using a large corpus. Specifically, we will use
1. A rule-based technique using lexico-syntactic patterns to extract hyponym-hypernym word pairs.
2. Another rule-based technique but using dependency-paths
3. A DIY approach where you can use any supervised/unsupervised technique extract hypernym-hyponym word pairs.


In this assignment, we will be using *nltk*.  If you are use Stephen's miniconda you should be fine. Otherwise, install nltk and the relavant tagger using.
```
pip install nltk
$ python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('averaged_perceptron_tagger')
```

<!-- <div class="alert alert-warning" markdown="1">
In order to use the gensim package, you'll have to be using Python version 3.6 or higher.  On my Mac, I did the following:
* `brew install python3`
* `pip3 install gensim`
* Then when I ran python, I used the command `python3` instead of just `python`
</div> -->

<div class="alert alert-info" markdown="1">
Here is the required code you should download for this assignment [form here](https://drive.google.com/drive/folders/1EBZs5L2rbF0immOetBTC3AZbgf4XYtMG?usp=sharing):
* `lexicalinference/` Contains all the relevant code. The description for individual files is given below
</div>


<div class="alert alert-info" markdown="1">
Here are the materials that you should download for this assignment [form here](https://drive.google.com/drive/folders/1EBZs5L2rbF0immOetBTC3AZbgf4XYtMG?usp=sharing):
* `bless2011/` Contains the train, validation and test (without labels) data
* `wikipedia_sentences.txt` Contains tokenized relevant wikipedia sentences. A lemmatized version also exists.
* `wikipedia_deppaths.txt` Contains word pairs and the shortest dependency path between them as extracted using spaCy
</div>

# Part 1: Hearst Patterns for Hypernym Learning

Marti Hearst, in her classic 1992 COLING paper [Automatic Aquisition of Hyponyms from Large Text Cororpa](http://www.aclweb.org/anthology/C92-2082), described how lexico-syntactic patterns can be used for hyponym acquisition.

Consider the sentence,
```
How do I distinguish among different musical genres such as blues, rock, and jazz, etc., and is there a good listeners’ trick to discern such extinctions?
```
Upon reading, we can easily infer that *blues*, *rock* and *jazz* are types of *musical genres*.
Consider another sentence that contains a similar lexico-syntactic construction and expresses a hypernymy relation between *green vegetables* and *spinach*, *peas*, and *kale*.
```
I am going to get green vegetables such as spinach, peas and kale.
```
We can generalize this construction to
```
NP_0 such as NP_1, NP_2, ... (and | or) NP_n
```
where *NP_0* is the hypernym of *NP_1*, *NP_2*, ..., *NP_n*.
Here, *NP_x* refers to a [noun phrase or noun chunk](https://en.wikipedia.org/wiki/Noun_phrase).


Hearst identified many such patterns, hence forth referred to as Hearst Patterns. Since these patterns are already constructed manually, we can use these patterns on a large corpus for hyponym acquisition.
In this section of the assignment, we will use these patterns to extract hyper-hyponym word pairs from Wikipedia.

## Dataset

To evaluate the quality of our extraction, we will use a post-processed version of [BLESS2011 dataset](http://www.aclweb.org/anthology/W11-2501).
[Levy et al. '15](http://www.aclweb.org/anthology/N15-1098) post-processed to clean the dataset for reasons mentioned in the paper. We provide you with the dataset. The files contain tab-separated text where the first (second) column contains the possible hyponym (hypernym) and the third column contains True/False indicating whether the relationship holds.

## Wikipedia Corpus

As our large corpus to extract hyper-hyponyms, we will use Wikipedia text. Since Wikipedia is too large for efficient processing, we provide you with a pruned version. This only contains sentences that contain a word pair from train/val/test set.
Each line in the file contains 2 tab-separated columns. The first column contains the tokenized text, and the second contains the lemmatized version of the same sentence.

## How to Get Started

As you must have noticed, implementing Hearst Patterns requires noun-phrase chunking and then regex pattern matching where these patterns are relevant Hearst pattern.

In the file ```hearst/hearstPatterns.py``` we use NLTK to implement a nltk-regex based [noun-phrase chunker](http://www.nltk.org/book/ch07.html) and Hearst pattern matching.
The list ```self.__hearst_patterns``` already contains one pattern implemented. Your job is to implement more Hearst Patterns as described in the original paper, or come up with your own patterns.

Carefully read through the code to figure out how it is implemented. On a high-level, the code first finds noun phrases and represents them as
```
I like to listen to NP_music from NP_musical_genres such as NP_blues , NP_rock and NP_jazz .
```
then applies the regex Heart Pattern matcher to extract hyper-hyponym pairs. For this particular example, it extracts
`('blues', 'musical genres')`, `('rock', 'musical genres')`, and `('jazz', 'musical genres')`


To use the method above to perform large-scale extraction on Wikipedia, and evaluation against the provided dataset, we provide the following functions:
* `hearst/extractHearstHyponyms.py` - Implements a method to apply the Hearst Patterns from all Wikipedia sentences and place them in a file.

* `extractDatasetPredictions.py` - Labels the train/val/test pairs as True/False based on their existence in the extracted hyper-hyponym pairs.

* `computePRF.py` - Takes the gold-truth and prediction file to compute the Precision, Recall and F1 score.


You should implement different Hearst Patterns, and/or come up with your own patterns by eyeballing Wikipedia data. Use the train and validation data to estimate the performance of different pattern combinations and submit the predictions from the best model on the test data to the leaderboard as the file `hearst.txt`. The format of this file will the same as the train and validation data.
```
hyponym \t hypernym \t True/False
```

## Hint for post-processing extractions

As you might notice in the dataset, the (hypernym, hyponym) pair contains single, usually lemmatized, tokens. On the other hand, the extractions from our code extracts a lot of multi-word noun phrases. This could negatively affect our performance on the provided dataset. Our performance should drastically improve if we post-process our extractions to output only single token extractions.

You should be able to use your knowledge about noun-phrases and lemmatization to figure out a post-processing methodology that might improve your performance. In the final report, make clear distinction between change in performance when the extractions were post-processed, compared to when they were not.


# Part 2: Dependency Paths for Hypernym Learning

Consider the sentence snippet, *... such green vegetables as spinach, peas and kale.* and its dependency-parse using [spaCy](https://spacy.io/)

<img src="/assets/img/deppath.png" alt="Example dependency path using spaCy" style="width: 100%;"/>

We (again) observe that there are dependency paths between *vegetables* and *spinach*, *peas*, and *kale* that can be typical in expressing hyper-hyponymy relation between words. This observation was made in [Snow et al.'s](https://web.stanford.edu/~jurafsky/paper887.pdf) seminal paper.

We can use the shortest dependency path between noun (noun-chunk) pairs to predict hypernymy relation. For example, in the example above the shortest dependency path between *vegetables* and *spinach* is
```
vegetables/NOUN -> Prep -> as/ADP -> pobj -> spinach/NOUN
```

For generalization, we will anonymize the start and end-points of the paths, as
```
X/NOUN -> Prep -> as/ADP -> pobj -> Y/NOUN
```
and can now predict that when a (X,Y) pair has such a dependency-path between them, it usually means that X is the hypernym of Y.


Simply using the shortest dependency paths as two major issues that can be tackled in the following manner:
* **Better lexico-syntactic paths**: Two words containing *as* in between is not a good indicator of the hypernymy relation being expressed and the word *such* outside the shortest path plays an important role.
Snow et al. hence proposed *Satellite edges*, i.e. single edges to the left (right) of the leftmost (rightmost) token.
In the example above, in addition to the shortest-path, the paths we extract will also contain satellite edges from *vegetable -> green*, *vegetable -> such*, and *spinach -> peas*.

* **Distributive Edges**: The shortest path from *vegetables* from *peas* contains *spinach/NOUN* node connected via the *conj* edge. The presence of specific words in the path that do not inform of the hypernymy relation (*spinach* in this case) can be deterimental to our performance, and also increase the path length significantly.
Snow et al. proposed to add additional edges bypassing *conj* edges to mitigate this issue. Therefore, we can add edges of type *pobj* from *vegetables* to *peas* and *kale*.

**Good News**: You don't need to extract such paths.  We've extracted them for you.  You're welcome! To keep the number of extracted paths tractable, the file `wikipedia_deppaths.txt` contains dependency paths extracted from Wikipedia between all train/val/test word pairs.
Similar to Snow et al., we only keep dependency paths of length 4 or shorter.
The file contain three tab-separated columns, the first containing **X**, second **Y** and the third the dependency path.
An example path extraction is:
```
mammal  fox     such/ADJ/amod<_X/NOUN/dobj_<as/ADP/prep_<Y/NOUN/pobj
```
The path edges are delimited by the underscore ( *_* ). Hence the edges in the path are:
1. `such/ADJ/amod<`:  An edge of type *amod* from the right side (*X*) to the word *such*
2. `X/NOUN/dobj`: An edge of type *dobj* from outside the shortest path span (since no direction marker ('<' or '>')) to the token *X*
3. `<as/ADP/prep`: An edge of type *prep* from *as* to the left of it (*X*).
4. `<Y/NOUN/pobj`: An edge of type *pobj* from *Y* to the left of it (*as*)

### How to proceed
Since it is difficult to come up with your own dependency path patterns, we suggest you use the the training data to come up with a list of dependency-paths that are positive examples of paths between actual hyper-hyponym pairs.

* `depPath/extractRelevantDepPaths.py`: Fill this python script, to extract positive dependency paths from `wikipedia_deppaths.txt` using the training and the validation data and store them to a file
* `depPath/extractDepPathHyponyms.py`: Complete this python script to generate hyper-hyponym extractions for the wikipedia corpus (`wikipedia_deppaths.txt`) (similar to Hearst Patterns)
* `extractDatasetPredictions.py`: Use this function (similar to Hearst Patterns) to label the train/val/test pairs as True/False based on their existence in the extracted hyper-hyponym pairs.
* `computePRF.py`: Similar to Hearst Patterns, use this script to evaluate the performance on the given dataset

For the best performing dependency paths, submit the test predictions on the relevant leaderboard with the filename `deppath.txt`.

# Part 3: DIY

*<center>Cause I'm as free as a bird now, And this bird you can not change. - Lynyrd Skynyrd</center>*


In the previous two sections we saw how we can use manually specified rule-based techniques to extract word-pairs satisfying hypernymy relations.
In this section, you have to implement **at least two** additional methods to extract such word pairs. A few example ideas are:
* Combine the extractions from Hearst patterns and Dependency-path patterns
* Use the dependency paths to extract features and learn a supervised classifier
* Combine the above two ...


### 3. The Leaderboard
We will have three leaderboards for this assignment, namely
1. Hearst Patterns - `hearst.txt`
2. DepdencyPath Patterns - `deppath.txt`
3. DIY Model - `diy.txt`

### Extra Credit
* Extra credit to the top-5 teams on each leaderboard.
* Extra credit to teams that perform significantly better on Part 3 then Part 1/2.


## Deliverables
<div class="alert alert-warning" markdown="1">
Here are the deliverables that you will need to submit. The writeup needs to be submit as `writeup.pdf`:
* The three prediction files
* Written analysis on which Hearst Patterns worked the best
* Written analysis commenting on the Precision/Recall values when using Hearst Patterns
* Written analysis on few Dependency Paths that worked the best
* Written analysis commenting on the Precision/Recall values when using Dependency Paths
* Implementation details of the DIY model
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
