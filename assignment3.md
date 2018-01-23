---
layout: default
img: period_speech.png
img_link: https://xkcd.com/771/
caption: Understanding Shakespeare with Math    
title: Homework 3 - Vector Semantics
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

Vector Semantics <span class="text-muted">: Assignment 3</span>
=============================================================

In this assignment you will implement many of the things you learned in [Chapter 15 of the textbook](https://web.stanford.edu/~jurafsky/slp3/15.pdf). If you haven't read it yet, now would be a good time to do that.  We'll wait.  Done?  Great, let's move on. 

We will provide a corpus of Shakespeare plays, which you will use to create a term-document matrix and a term-context matrix. You'll implement a selection of the weighting methods and similarity metrics defined in the textbook. Ultimately, your goal is to use the resulting vectors to measure how similar Shakespeare plays are to each other, and to find words that are used in a similar fashion. All (or almost all) of the code you write will be direct implementations of concepts and equations described in [Chapter 15](https://web.stanford.edu/~jurafsky/slp3/15.pdf).

Lo, here upon thy cheek the stain doth sit Of an old tear that is not washed off yet.
There’s still a stain on your cheek from an old tear that hasn’t been washed off yet.

<div class="alert alert-info" markdown="1">
Here are the materials that you should download for this assignment:
* Skeleton python code
* Data - the complete works of Shakespeare
</div>

Your Tasks
======================
All of the following are function stubs in the python code. You just need to fill them out.

* fill out `create_term_document_matrix`
* fill out `create_term_context_matrix`
* fill out `create_PPMI_matrix`
* fill out `compute_tf_idf_matrix`
* fill out `compute_cosine_similarity`
* fill out `compute_jaccard_similarity`
* fill out `compute_dice_similarity`
* fill out `rank_plays`
* fill out `rank_words`


# Term-Document Matrix

You will write code to compile a term-document matrix for Shakespeare's plays, following the description in section 15.1.1 in textbook.

> In a *term-document matrix*, each row represents a word in the vocabulary and each column represents a document from some collection. The figure below shows a small selection from a term-document matrix showing the occurrence of four words in four plays by Shakespeare. Each cell in this matrix represents the number of times a particular word (defined by the row) occurs in a particular document (defined by the column). Thus *clown* appeared 117 times in *Twelfth Night

|              | As You Like It |  Twelfth Night  | Julias Caesar | Henry V |
| :----------: |:--------------:| :-------------: | :----------:  | :-----: |
| **battle**	| 1 | 1 | 8 | 15 |
| **soldier**	| 2 | 2 | 12 | 36 |
| **fool**		| 37 | 58 | 1 | 5 |
| **crown**		| 5 | 117 | 0 | 0 |

The dimensions of your term-document matrix will be the number of documents $D$ (in this case, the number of Shakespeare's plays that we give you in the corpus by the number of unique word types $\|V\|$ in that collection.   The columns represent the documents, and the rows represent the words, and each cell represents the frequency of that word in that document. 

In your code you will write a function to `create_term_document_matrix`.  This will let you be the hit of your next dinner party by being able to answer triva questions like *how many words did Shakespeare use?*, which may give us a hint to the answer to *[How many words did Shakespeare know?]*  The table will also tell you how many words Shakespeare used only once.  did you know that there's a technical term for that?  In corpus linguistics they are called [*hapax legomena*](https://en.wikipedia.org/wiki/Hapax_legomenon), but I prefer the term *singleton*, because I don't like snooty Greek or Latin terms. 

## Comparing plays

The term-document matrix will also let us do cool things like figure out which plays are most similar to each other, by comparing the column vectors.  We could even look for outliers to see if some plays are so dissimilar from the rest of the cannon that [maybe they weren't authored by Shakespeare afterall](https://en.wikipedia.org/wiki/Shakespeare_authorship_question).  

Let's begin by considering the column representing each play.  Each column is a $\|V\|$-dimensional vector.  Let's use some math to define the similarity of these vectors.   By far the most common similarity metric is the cosine of the angle between the vectors.  The cosine similarity metric is defined in Section 15.3 of the textbook.

$cosine(\vec{v}, \vec{w}) = \frac{\vec{v} \cdot \vec{w}}{$\|\vec{v}\| $\|\vec{w}\|} = \frac{\sum_{i=1}^{N}{v_iw_i}}{\sqrt{\sum_{i=1}^{N}{v_i^2}} \sqrt{\sum_{i=1}^{N}{w_i^2}}} $

The cosine value ranges from 1 for vectors pointing in the same direction, through 0 for vectors that are orthogonal, to -1 for vectors pointing in opposite directions. Since our term-document matrix contains raw frequency counts, it is non-negative, so the cosine for its vectors will range from 0–1.  1 means that the vectors are identical, 0 means that they are totally dissimilar.  

Please implement `compute_cosine_similarity`, and for each play in the corpus, score how similar each other play is to it.  Which plays are the closet to each other in vector space (ignoring self similarity)?  Which plays are the most distant from each other? 

## Deliverables 
<div class="alert alert-warning" markdown="1">
Here are the deliverables that you will need to submit:
* writeup.pdf
* code (.zip). It should be written in Python 3.
</div>

## Recommended readings
* Jurafsky and Martin, chapter [15](https://web.stanford.edu/~jurafsky/slp3/15.pdf)

* (A cool data set)[https://github.com/cocoxu/Shakespeare]


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
