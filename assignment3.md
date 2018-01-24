---
layout: default
img: period_speech.png
img_link: https://xkcd.com/771/
caption: Understanding Shakespeare with Math    
title: Homework 3 "Vector Space Models"
active_tab: homework
release_date: 2018-01-24
due_date: 2018-01-31T11:00:00EST
attribution: Daphne Ippolito, Anne Cocos, Stephen Mayhew, and Chris Callison-Burch developed this homework assignment for UPenn's CIS 530 class in Spring 2018.
readings:
-
   title: Vector Semantics
   authors: Dan Jurafsky and James H. Martin
   venue: Speech and Language Processing (3rd edition draft)
   type: textbook
   url: https://web.stanford.edu/~jurafsky/slp3/15.pdf
-
   title: From Frequency to Meaning&colon; Vector Space Models of Semantics
   authors: Peter D. Turney and Patrick Pantel
   venue: Journal of Artificial Intelligence Research
   year: 2010
   type: journal
   url: https://www.jair.org/media/2934/live-2934-4846-jair.pdf
   id: from-frequency-to-meaning
   abstract: Computers understand very little of the meaning of human language. This profoundly limits our ability to give instructions to computers, the ability of computers to explain their actions to us, and the ability of computers to analyse and process text. Vector space models (VSMs) of semantics are beginning to address these limits. This paper surveys the use of VSMs for semantic processing of text. We organize the literature on VSMs according to the structure of the matrix in a VSM. There are currently three broad classes of VSMs, based on term–document, word–context, and pair–pattern matrices, yielding three classes of applications. We survey a broad range of applications in these three categories and we take a detailed look at a specific open source project in each category. Our goal in this survey is to show the breadth of applications of VSMs for semantics, to provide a new perspective on VSMs for those who are already familiar with the area, and to provide pointers into the literature for those who are less familiar with the field.
   bibtex: |
      @article{turney2010frequency,
        title={From Frequency to Meaning: Vector Space Models of Semantics},
        author={Turney, Peter D and Pantel, Patrick},
        journal={Journal of Artificial Intelligence Research},
        volume={37},
        pages={141--188},
        year={2010}
      }
- 
   title: Paraphrasing for Style
   authors: Wei Xu, Alan Ritter, Bill Dolan, Ralph Grisman, and Colin Cherry 
   venue: Coling
   year: 2012
   type: conference
   url: http://www.aclweb.org/anthology/C12-1177
   id: paraphrasing-for-style
   abstract: We present initial investigation into the task of paraphrasing language while targeting a particular writing style. The plays of William Shakespeare and their modern translations are used as a testbed for evaluating paraphrase systems targeting a specific style of writing. We show that even with a relatively small amount of parallel training data, it is possible to learn paraphrase models which capture stylistic phenomena, and these models outperform baselines based on dictionaries and out-of-domain parallel text. In addition we present an initial investigation into automatic evaluation metrics for paraphrasing writing style. To the best of our knowledge this is the first work to investigate the task of paraphrasing text with the goal of targeting a specific style of writing.
   bibtex: |
      @inproceedings{xu2012paraphrasing,
        title={Paraphrasing for Style},
        author={Xu, Wei and Ritter, Alan and Dolan, Bill and Grishman, Ralph and Cherry, Colin},
        booktitle={COLING},
        pages={2899--2914},
        year={2012}
      }

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

Vector Space Models <span class="text-muted">: Assignment 3</span>
=============================================================

In this assignment you will implement many of the things you learned in [Chapter 15 of the textbook](https://web.stanford.edu/~jurafsky/slp3/15.pdf). If you haven't read it yet, now would be a good time to do that.  We'll wait.  Done?  Great, let's move on. 

We will provide a corpus of Shakespeare plays, which you will use to create a term-document matrix and a term-context matrix. You'll implement a selection of the weighting methods and similarity metrics defined in the textbook. Ultimately, your goal is to use the resulting vectors to measure how similar Shakespeare plays are to each other, and to find words that are used in a similar fashion. All (or almost all) of the code you write will be direct implementations of concepts and equations described in [Chapter 15](https://web.stanford.edu/~jurafsky/slp3/15.pdf).

*All difficulties are easy when they are known.*

<div class="alert alert-info" markdown="1">
Here are the materials that you should download for this assignment:
* Skeleton python code
* Data - the complete works of Shakespeare
</div>


# Term-Document Matrix

You will write code to compile a term-document matrix for Shakespeare's plays, following the description in section 15.1.1 in textbook.

> In a *term-document matrix*, each row represents a word in the vocabulary and each column represents a document from some collection. The figure below shows a small selection from a term-document matrix showing the occurrence of four words in four plays by Shakespeare. Each cell in this matrix represents the number of times a particular word (defined by the row) occurs in a particular document (defined by the column). Thus *clown* appeared 117 times in *Twelfth Night

|             | As You Like It |  Twelfth Night  | Julias Caesar | Henry V |
| :---------: |:--------------:| :-------------: | :----------:  | :-----: |
| **battle**	| 1 | 1 | 8 | 15 |
| **soldier**	| 2 | 2 | 12 | 36 |
| **fool**		| 37 | 58 | 1 | 5 |
| **crown**		| 5 | 117 | 0 | 0 |

The dimensions of your term-document matrix will be the number of documents $D$ (in this case, the number of Shakespeare's plays that we give you in the corpus by the number of unique word types $\|V\|$ in that collection.   The columns represent the documents, and the rows represent the words, and each cell represents the frequency of that word in that document. 

In your code you will write a function to `create_term_document_matrix`.  This will let you be the hit of your next dinner party by being able to answer trivia questions like *how many words did Shakespeare use?*, which may give us a hint to the answer to *[How many words did Shakespeare know?]*  The table will also tell you how many words Shakespeare used only once.  did you know that there's a technical term for that?  In corpus linguistics they are called [*hapax legomena*](https://en.wikipedia.org/wiki/Hapax_legomenon), but I prefer the term *singleton*, because I don't like snooty Greek or Latin terms. 

## Comparing plays

The term-document matrix will also let us do cool things like figure out which plays are most similar to each other, by comparing the column vectors.  We could even look for outliers to see if some plays are so dissimilar from the rest of the cannon that [maybe they weren't authored by Shakespeare afterall](https://en.wikipedia.org/wiki/Shakespeare_authorship_question).  

Let's begin by considering the column representing each play.  Each column is a $\|V\|$-dimensional vector.  Let's use some math to define the similarity of these vectors.   By far the most common similarity metric is the cosine of the angle between the vectors.  The cosine similarity metric is defined in Section 15.3 of the textbook.

> The cosine, like most measures for vector similarity used in NLP, is based on the dot product operator from linear algebra, also called the inner product:

> dot-product($\vec{v}, \vec{w}) = \vec{v} \cdot \vec{w} = \sum_{i=1}^{N}{v_iw_i} = v_1w_1 +v_2w_2 +...+v_Nw_N$

> The dot product acts as a similarity metric because it will tend to be high just when the two vectors have large values in the same dimensions. Alternatively, vectors that have zeros in different dimensions (orthogonal vectors) will have a dot product of 0, representing their strong dissimilarity. 

> This raw dot-product, however, has a problem as a similarity metric: it favors long vectors. The vector length is defined as

> $\|\vec{v}\| = \sqrt{\sum_{i=1}^{N}{v_i^2}}$

> The dot product is higher if a vector is longer, with higher values in each dimension. More frequent words have longer vectors, since they tend to co-occur with more words and have higher co-occurrence values with each of them. The raw dot product thus will be higher for frequent words. But this is a problem; we would like a similarity metric that tells us how similar two words are regardless of their frequency.

> The simplest way to modify the dot product to normalize for the vector length is to divide the dot product by the lengths of each of the two vectors. This normalized dot product turns out to be the same as the cosine of the angle between the two vectors, following from the definition of the dot product between two vectors $\vec{v}$ and $\vec{w}$ as:

> $\vec{v} \cdot \vec{w} = \|\vec{v}\|\|\vec{w}\| cos \Theta$

> $\frac{\vec{v} \cdot \vec{w}}{\|\vec{v}\|\|\vec{w}\|} =  cos \Theta$

> The cosine similarity metric between two vectors $\vec{v}$ and $\vec{w}$ thus can be computed

> $cosine(\vec{v}, \vec{w}) = \frac{\vec{v} \cdot \vec{w}}{\|\vec{v}\| \|\vec{w}\|} = \frac{\sum_{i=1}^{N}{v_iw_i}}{\sqrt{\sum_{i=1}^{N}{v_i^2}} \sqrt{\sum_{i=1}^{N}{w_i^2}}} $

The cosine value ranges from 1 for vectors pointing in the same direction, through 0 for vectors that are orthogonal, to -1 for vectors pointing in opposite directions. Since our term-document matrix contains raw frequency counts, it is non-negative, so the cosine for its vectors will range from 0 to 1.  1 means that the vectors are identical, 0 means that they are totally dissimilar.  

Please implement `compute_cosine_similarity`, and for each play in the corpus, score how similar each other play is to it.  Which plays are the closet to each other in vector space (ignoring self similarity)?  Which plays are the most distant from each other? 

## How do I know if my rankings are good?

First, read all of the plays. Then perform at least three of them. Now that you are a true thespian, you should have a good intuition for the central themes in the plays.   Alternately, take a look at [this grouping of Shakespeare’s plays into Tragedies, Comedies and Histories](https://en.wikipedia.org/wiki/Shakespeare%27s_plays#Canonical_plays). Do plays that are thematically similar to the one that you're ranking appear among its most similar plays, according to cosine similarity? Another clue that you're doing the right thing is if a play has a cosine of 1 with itself.  If that's not the case, then you've messed something up. Another good hint, is that there are a ton of pays about Henry.  They'll probably be similar to each other.

# Measuring word similarity 

Next, we're going to see how we can represent words as vectors in vector space.  This will give us a way of representing some aspects of the *meaning* of words, by measuring the similarity of their vectors. 

In our term-document matrix, the rows are word vectors.  Instead of a $\|V\|$-dimensional vector, these row vectors only have $D$ dimensions.  Do you think that's enough to represent the meaning of words?  Try it out.  In the same way that you computed the similarity of the plays, you can compute the similarity of the words in the matrix.  Pick some words and compute 10 words with the highest cosine similarity between their row vector representations.  Are those 10 words good synonyms? 

## Term-Context Matrix

Instead of using a term-document matrix, a more common way of computing word similarity is by constructing a term-context matrix (also called a word-word matrix), where columns are labeled by words rather than documents.  The dimensionality of this kind of a matrix is $\|V\|$ by $\|V\|$.  Each cell represents how often the word in the row (the target word) co-occurs with the word in the column (the context) in a training corpus.  

For this part of the assignment, you should write the `create_term_context_matrix` function.  This function specifies the size word window around the target word that you will use to gather its contexts.  For instance, if you set that variable to be 4, then you will use 4 words to the left of the target word, and 4 words to its right for the context.  In this case, the cell represents the number of times in Shakespeare's plays the column word occurs in +/-4 word window around the row word.

You can now re-compute the most similar words for your test words using the row vectors in your term-context matrix instead of your term-document matrix.  What is the dimensionality of your word vectors now?  Do the most similar words make more sense than before?

# Weighting terms

Your term-context matrix contains the raw frequency of the co-occurrence of two words in each cell.  Raw frequency turns out not to be the best way of measuring the association between words.  There are several methods for weighting words so that we get better results.  You should implement two weighting schemes:

* Positive pointwise mutual information (PPMI)
* Term frequency inverse document frequency (tf-idf)

These are defined in Section 15.2 of the textbook.

*Warning, calculating PPMI for your whole $\|V\|$-by-$\|V\|$ matrix might be slow. Our intrepid TA's implementation for PPMI takes about 10 minutes to compute all values.  She always writes perfectly optmized code on her first try.*


# Weighting terms  

There are several ways of computing the similarity between two vectors.  In addition to writing a function to compute cosine similarity, you should also write functions to `compute_jaccard_similarity` and `compute_dice_similarity`.  Check out section 15.3.1. of the textbook for the defintions of the Jaccard and Dice measures. 


 
# Your Tasks

All of the following are function stubs in the python code. You just need to fill them out.

Create matrices:
* fill out `create_term_document_matrix`
* fill out `create_term_context_matrix`
* fill out `create_PPMI_matrix`
* fill out `compute_tf_idf_matrix`

Compute similarities:
* fill out `compute_cosine_similarity`
* fill out `compute_jaccard_similarity`
* fill out `compute_dice_similarity`

Do some ranking:
* fill out `rank_plays`
* fill out `rank_words`

# Report

In the ranking tasks, play with different vector representations, and different similarity functions. Does one combination appear to work better than another? Do any interesting patterns emerge? Include this discussion in your writeup.

Some patterns you could look into:
* Shakespeare's plays are traditionally classified into [comedies, histories, and tragedies](https://en.wikipedia.org/wiki/Shakespeare%27s_plays). Can you use these vector representations to cluster the plays?
* Do the vector representations of [female characters](https://en.wikipedia.org/wiki/Category:Female_Shakespearean_characters) differ distinguishably from male ones [male ones](https://en.wikipedia.org/wiki/Category:Male_Shakespearean_characters)?

# Extra credit

Quantifying the goodness of one vector space representation over another can be very difficult to do.  It might ultimately require testing how the different vector representations change the performance when used in a downstream task like question answering. A common way of quantifying the goodness of word vectors is to use them to compare the similarity of words with human similarity judgments, and then calculate the correlation of the two rankings.

If you would like extra credit on this assignment, you can quantify the goodness of each of the different vector space models that you produced (for instance by varying the size of the context window, picking PPMI or tf-idf, and selecting among cosine, Jaccard and Dice).  You can calculate their scores on the [SimLex999 data set](https://www.cl.cam.ac.uk/~fh295/simlex.html), and compute their correlation with human judgments using [Kendall's Tau](https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient).

Add a section to your writeup explaining what experiments you ran, and which setting had the highest correlation with human judgments. 

# More Optional Fun Extra Credit options


So you've built some machinery that can measure similarity between words and documents. We gave you a Shakespeare corpus, but you can use any body of text you like. For example, check out [Project Gutenberg](https://www.gutenberg.org/) for public domain texts. The sky's the limit on what you can do, but here are some ideas:

* *Term-Character Matrix*.  Our data set 
* *Novel recommender system*. Maybe you enjoyed reading _Sense and Sensibility_ and _War and Peace_. Can you suggest some similar novels? Or maybe you need some variety in your consumption. Find novels that are really different.
* *Other languages*. Do these techniques work in other languages? Project Gutenberg has texts in a variety of languages. Maybe you could use this to measure language similarity?
* *Modernizing Shakespeare*.  When I read Shakespeare in high school, I had the dickens of a time trying to understand all the weird words in the play.  Some people have re-written Shakespeare's plays into contemporary English.  An [awesome NLP researcher](https://cocoxu.github.io) has [compiled that data](https://github.com/cocoxu/Shakespeare).  User her data and your vector space models to find contemporary words that mean similar things to the Shakespearean English.  


## Deliverables 
<div class="alert alert-warning" markdown="1">
Here are the deliverables that you will need to submit:
* writeup.pdf
* code (.zip). It should be written in Python 3.
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
