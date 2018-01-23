---
layout: default
img: 
caption: Word vectors    
title: Homework 3 - Vector Semantics
active_tab: homework
release_date: 2018-01-24
due_date: 2018-01-31T11:00:00EST
attribution: Daphne Ippolito and Anne Cocos developed this homework assignment for UPenn's CIS 530 class in Spring 2018.
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


<div class="alert alert-info" markdown="1">
Here are the materials that you should download for this assignment:
* Some python code
* Data
</div>

We expect that you have read Jurafsky and Martin, chapters [15](https://web.stanford.edu/~jurafsky/slp3/15.pdf)


Things you have to do:
* fill out `create_term_document_matrix`
* fill out `create_term_context_matrix`
* fill out `create_PPMI_matrix`
* fill out `compute_tf_idf_matrix`
* fill out `compute_cosine_similarity`
* fill out `compute_jaccard_similarity`
* fill out `compute_dice_similarity`
* fill out `rank_plays`
* fill out `rank_words`


## Deliverables 
<div class="alert alert-warning" markdown="1">
Here are the deliverables that you will need to submit:
* writeup.pdf
* code (.zip). It should be written in Python 3.
</div>

## Recommended readings
* Jurafsky and Martin, chapter [15](https://web.stanford.edu/~jurafsky/slp3/15.pdf)
