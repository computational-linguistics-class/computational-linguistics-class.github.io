---
layout: default
img: Alexa.png
caption: Hello Alexa    
title: Homework 3 - Word Vectors and Clustering
active_tab: homework
release_date: 2017-01-24
due_date: 2017-01-31T14:00:00EST
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



Introduction
=======================
Intro!

Word Vectors
=======================
Also known as embeddings, or dense representations. 

One of the key problems in NLP is understanding how to represent words and meaning. We all carry around representations of words in our minds, so that if I say "orange" and "tangerine" you can sense a relationship (that is, fruit, or citrus), but if I say "orange" and "state", you might think of Florida. Similarly, you know that "hilarious" and "funny" mean basically the same thing, even though they are different words. How can we get a computer to "know" this?

This is where word vectors come in.


Codenames
=====================
[Codenames](https://boardgamegeek.com/boardgame/178900/codenames) is a popular board game where a clue-giver ("spymaster") gives one-word clues to guide the clue-guessers ("teammates") into selecting the right subset of words out of the 25 word options on the table. The catch is that the spymaster's clue can only be a single word (to hint at intended cards), and a single number (to define how many cards are intended).  For example, there are 25 word cards on the table, and the spymaster wants the teammates to select only the words "WHALE," "PLATYPUS", and "KANGAROO." A good clue would be "MAMMAL 3."


Clustering
======================


