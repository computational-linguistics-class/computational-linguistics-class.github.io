---
layout: default
img: estimating_time.png
caption: Don't Panic
img_link: https://xkcd.com/1658/   
title: Term Project - Milestone 1
active_tab: homework
release_date: 2018-03-01
due_date: 2018-03-03T12:00:00EST
attribution: This assignment was developed by the CIS 530 course staff.
deliverables:
    -
      description: Milestone 1 - Form a team and submit three project ideas
      due_date: 2018-03-14T11:00:00EST
    -
      description: Milestone 2 - Collect your data, and write an evalation script and a simple baseline
      due_date: 2018-03-28T11:00:00EST
    -
      description: Milestone 3 - Implement a published baseline
      due_date: 2018-04-11T11:00:00EST
    -
      description: Milestone 4 - Submit your project writeup and a pitch video.  Finish one of your extensions the public baseline (no late days allowed)
      due_date: 2018-04-18T11:00:00EST
    -
      description: Vote on your favorite projects from the class
      due_date: 2018-04-18T12:00:00EST
    -
      description: Milestone 5 - Finish all your extensions to the public baseline
      due_date: 2018-04-25T12:00:00EST
    -
      description: Optional extra credt - Do one or more of the your classmates' projects
      due_date: 2018-04-25T12:00:00EST
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

Term Project <span class="text-muted">: Overview</span>
============


Your term project is to design a project similar to the homework assigments you have completed
in this class. Your final project will consist of the following components:

1. A description of the problem, in the style and format of the homework assignment descriptions.
1. Training and evaluation data.
1. A commented implementation of the simplest possible solution to the problem.  For instance, this could be a majority class baseline or a random baseline. 
1. A commented implementation of a baseline published in the literature, along with
   skeleton code obtained by removing the parts that students should implement.
1. One extension per team member that attempts to improve on the baseline, along
   with a brief (one- to three-paragraph) accompanying write-up for each extension
   describing the general approach and whether it worked.
1. A evaluation script that can be used to score
   submissions like on the class leaderboard. The output of any model
   implementations should be gradeable with this program.

We'll vote on the best projects, and the best ones will be available for ther students to complete as an optional final homework assignment.

We're going to split up the work on the term project into several deliverables, each with their own due dates.  You don't have to wait to start working on each part of the project.  We encourage you to begin work early, so that you have a polished final product.


## Milestones and Due Dates

<div class="alert alert-info">
Here are the milestones for the term project:
{% if page.deliverables %}
<ul>
{% for deliverable in page.deliverables %}
<li> {{ deliverable.due_date | date: "%b %-d, %Y" }} - {{deliverable.description}}.</li>
{% endfor %}
</ul>
{% endif %}
</div>


# Milestone 1

For Milestone 1, you'll need to form a team and come up with 3 project ideas.  For each idea you should describe:
1. A problem definition (1 to 2 paragraphs, plus an illustrative example)
1. A pointer to or more more papers or sections textbook that describes the problem
1. What evaluation metrics could use to score system outputs 
1. What type of data you will need to evaluate, and how much data is available 


The term project is a team exercise.  The minimum team size is 4, and the max team size is 6.  If you need help finding a team, you can post on [this Piazza thread](https://piazza.com/class/jbse3zxepja7bz?cid=366).


## Project Ideas

You should identify what topic you would like to work on.  Pretty much any topic in natural language processing is fair game.  The first milestone for the term project is to pick 3 topic ideas that your team might be interested in exploring.  The course staff will help assess the feasibility of your ideas and will make a recommendation of which of your 3 initial ideas is the best fit for the scope of the term project.  


The NLP community has a great tradition of "shared tasks".  Many of these are perfect for a term-project for this class, since they give you a great starting point for a problem definition, training and test data, a standard evaluation metric, and lots of published baselines.  Here are some pointers to shared tasks that were featured at CoNLL, SemEval, WMT, and Kaggle. 

You are welcome to choose a share task topic or to develop your own topic, provided that it is related to NLP.

### CoNLL Shared Tasks

The Conference on Computational Natural Language Learning (CoNLL) hosts a shared task every year.  Here are the past [CoNLL shared tasks](http://www.conll.org/previous-tasks): 


1. Multilingual Parsing from Raw Text to Universal Dependencies
1. Universal Morphological Reinflection
1. Multilingual Shallow Discourse Parsing
1. Shallow Discourse Parsing
1. Grammatical Error Correction	English	Proceedings
1. Modelling Multilingual Unrestricted Coreference in OntoNotes
1. Modelling Unrestricted Coreference in OntoNotes	English
1. Hedge Detection	English	Proceedings
1. Syntactic and Semantic Dependencies in Multiple Languages
1. Joint Parsing of Syntactic and Semantic Dependencies
1. Dependency Parsing: Multilingual & Domain Adaptation
1. Multi-Lingual Dependency Parsing
1. Semantic Role Labeling	English	 
1. Language-Independent Named Entity Recognition
1. Clause Identification
1. Chunking
1. NP Bracketing


### SemEval

The International Workshop on Semantic Evaluation (SemEval) hosts a range of shared tasks every year.  Here are links to the SemEval tasks:

[SemEval-2017](http://alt.qcri.org/semeval2017/index.php?id=tasks)


1. Semantic Textual Similarity
2. Multi­lingual and Cross­-lingual Semantic Word Similarity
3. Community Question Answering
4. Sentiment Analysis in Twitter
5. Fine-Grained Sentiment Analysis on Financial Microblogs and News
6. #HashtagWars. Learning a Sense of Humor
7. Detection and Interpretation of English Puns
8. RumourEval. Determining rumour veracity and support for rumours
9. Abstract Meaning Representation Parsing and Generation
10. Extracting Keyphrases and Relations from Scientific Publications
11. End-User Development using Natural Language
12. Clinical TempEval


[SemEval-2016](http://alt.qcri.org/semeval2016/index.php?id=tasks)


1. Semantic Textual Similarity. A Unified Framework for Semantic Processing and Evaluation
2. Interpretable Semantic Textual Similarity
3. Community Question Answering
4. Sentiment Analysis in Twitter
5. Aspect-Based Sentiment Analysis
6. Detecting Stance in Tweets
7. Determining Sentiment Intensity of English and Arabic Phrases
8. Meaning Representation Parsing
9. Chinese Semantic Dependency Parsing
10. Detecting Minimal Semantic Units and their Meanings
11. Complex Word Identification
12. Clinical TempEval
13. TExEval-2 -- Taxonomy Extraction
14. Semantic Taxonomy Enrichment


[SemEval-2015](http://alt.qcri.org/semeval2015/index.php?id=tasks)

1. Paraphrase and Semantic Similarity in Twitter
2. Semantic Textual Similarity
3. Answer Selection in Community Question Answering
4. TimeLine. Cross-Document Event Ordering
5. QA TempEval
6. Clinical TempEval
7. Diachronic Text Evaluation
8. SpaceEval
9. CLIPEval Implicit Polarity of Events
10. Sentiment Analysis in Twitter
11. Sentiment Analysis of Figurative Language in Twitter
12. Aspect Based Sentiment Analysis
13. Multilingual All-Words Sense Disambiguation and Entity Linking
14. Analysis of Clinical Text
15. A CPA dictionary-entry-building task
17. Taxonomy Extraction Evaluation
18. Semantic Dependency Parsing


[SemEval-2014](http://alt.qcri.org/semeval2014/index.php?id=tasks)

1. Evaluation of Compositional Distributional Semantic Models on Full Sentences through  Semantic Relatedness and Entailment
1. Grammar Induction for Spoken Dialogue Systems
1. Cross-Level Semantic Similarity
1. Aspect Based Sentiment Analysis
1. L2 Writing Assistant
1. Supervised Semantic Parsing of Spatial Robot Commands
1. Analysis of Clinical Text
1. Broad-Coverage Semantic Dependency Parsing
1. Sentiment Analysis in Twitter
1. Multilingual Semantic Textual Similarity


[SemEval-2013](https://www.cs.york.ac.uk/semeval-2013/index.php%3Fid=tasks.html)

1. TempEval-3 Temporal Annotation
1. Sentiment Analysis in Twitter
1. Spatial Role Labeling
1. Free Paraphrases of Noun Compounds
1. Evaluating Phrasal Semantics
1. Semantic Textual Similarity (becomes *Sem Shared Task)
1. The Joint Student Response Analysis and 8th Recognizing Textual Entailment Challenge
1. Cross-lingual Textual Entailment for Content Synchronization
1. Extraction of Drug-Drug Interactions from BioMedical Texts
1. Cross-lingual Word Sense Disambiguation
1. Evaluating Word Sense Induction & Disambiguation within An End-User Application
1. Multilingual Word Sense Disambiguation
1. Word Sense Induction for Graded and Non-Graded Senses
1. The Coarse-Grained and Fine-Grained Chinese Lexical Sample and All-Words Task

[SemEval-2012](https://www.cs.york.ac.uk/semeval-2013/index.php%3Fid=tasks.html)

1. English Lexical Simplification
1. Measuring Degrees of Relational Similarity
1. Spatial Role Labeling
1. Evaluating Chinese Word Similarity
1. Chinese Semantic Dependency Parsing
1. Semantic Textual Similarity
1. COPA. Choice Of Plausible Alternatives An evaluation of commonsense causal reasoning
1. Cross-lingual Textual Entailment for Content Synchronization

[Previous years](https://en.wikipedia.org/wiki/SemEval#External_links)


## Kaggle 

Kaggle is a platform for machine learning competitions where people compete to produce the best models for a huge range of different datasets. Companies often offer a reward for their competitions.  There's tons of cool data and competitions that you can base your final project on.  

Here are a few relevant competitions:
* [Sentiment Analysis on Movie Reviews](https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews)
* [Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)
* [Convert English text from written expressions into spoken forms](https://www.kaggle.com/c/text-normalization-challenge-english-language)
* [Quora Question Pairs - Can you identify question pairs that have the same intent?](https://www.kaggle.com/c/quora-question-pairs)
* [The Allen AI Science Challenge - Is your model smarter than an 8th grader?](https://www.kaggle.com/c/the-allen-ai-science-challenge)
* [DonorsChoose.org Application Screening - Predict whether teachers' project proposals are accepted](https://www.kaggle.com/c/donorschoose-application-screening#evaluation)
* [TensorFlow Speech Recognition Challenge - Can you build an algorithm that understands simple speech commands?](https://www.kaggle.com/c/tensorflow-speech-recognition-challenge)
* [Spooky Author Identification - Identify horror authors from their writings](https://www.kaggle.com/c/spooky-author-identification)


You can also check out the [Linguistics tag](https://www.kaggle.com/tags/linguistics) and  the [Langauges tag](https://www.kaggle.com/tags/languages) for lots of other ideas.  Want [130,000 wine reviews](https://www.kaggle.com/zynicide/wine-reviews) with their ratings, or [55,000 song lyrics](https://www.kaggle.com/mousehead/songlyrics)?  Find them on Kaggle. 


## Course staff ideas

Here are a list of potential project ideas that were brainstormed by the course staff:
* __Rank scalar adjectives__. Adjectives like good, tasty, yummy, delicious, scrumptious all describe some property of a noun (how good something tastes), but they vary in intensity.  Can you write an algorithm to put them in the correct order by intensity?  For instance, *good < tasty < yummy < delicious < scrumptious*.  Here are some good papers about the ranking scalar adjectives:
  * [Was it good? it was provocative. learning the meaning of scalar adjectives.](https://aclanthology.info/pdf/P/P10/P10-1018.pdf)
  * [Good, great, excellent: Global inference of semantic intensities.](https://www.cs.unc.edu/~mbansal/papers/tacl_acl13_semanticIntensity.pdf)
  * [Deriving adjectival scales from continuous space word representations](http://aclweb.org/anthology//D/D13/D13-1169.pdf)
  * [Large, huge or gigantic? identifying and encoding intensity relations among adjectives in wordnet.](https://link.springer.com/content/pdf/10.1007%2Fs10579-012-9212-1.pdf)
  * [Adjscales: Differentiating between similar adjectives for language learners.](http://zzz.cl.cs.titech.ac.jp/_media/publication/639.pdf)
  * [Lexicon-Based Methods for Sentiment Analysis](https://www.mitpressjournals.org/doi/abs/10.1162/COLI_a_00049) provides [intensity rankings](https://github.com/sfu-discourse-lab/SO-CAL/blob/master/Resources/dictionaries/English/adj_dictionary1.11.txt) that might be useful as features.  
 
* __Order prenominal modifiers__. In English, prenominal modifiers must come in a certain order.   It sounds fluent to say *the big beautiful white wooden house*, but not *the white wooden beautiful big house*.  Here's a NLP good paper describing a [class-based approach to ordering prenominal modifiers](http://www.aclweb.org/old_anthology/W/W09/W09-0608.pdf).
You could collect all of the pre-nominal modifiers from a large parsed corpus like the [WaCKy corpora](http://wacky.sslmit.unibo.it/doku.php?id=corpora) or the [Annotated Gigaword](https://catalog.ldc.upenn.edu/ldc2012t21), and then train a model to predict their order.   Here's a rule from a grammar book about what order adjectives are supposed to come in.  Is it true?
 <blockquote align="center" class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Things native English speakers know, but don&#39;t know we know: <a href="https://t.co/Ex0Ui9oBSL">pic.twitter.com/Ex0Ui9oBSL</a></p>&mdash; Matthew Anderson (@MattAndersonNYT) <a href="https://twitter.com/MattAndersonNYT/status/772002757222002688?ref_src=twsrc%5Etfw">September 3, 2016</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

 * __Predict the star rating of Amazon reviews__.  Amazon released a collection of  [130 million customer reviews](https://s3.amazonaws.com/amazon-reviews-pds/readme.html) from 1995 until 2015.  How well you predict the star rating based on the text of the reviews? There are tons of papers on NLP and sentiment analysis.  [Chapter 6](https://s3.amazonaws.com/amazon-reviews-pds/readme.html) and [Chapter 18](https://web.stanford.edu/~jurafsky/slp3/18.pdf) of the textbook as a good place to start. 

 * __Help assess depression and risks of self-harm in social media__.  One way that NLP might be used for social good is to try to identify people who are at risk of suicide based on their social media posts. There's a ton of good academic work on this.
   * The annual workshop on [Computational Linguistics and Clinical Psychology](http://clpsych.org) is a good place to start looking.  It has a lot of relevant publications in its past proceedings, and has featured many shared tasks.
   * One of the EMNLP 2017 best paper awards went to [Depression and Self-Harm Risk Assessment in Online Forums](http://aclweb.org/anthology/D17-1322)
   * Vanessa Callison-Burch was involved in [Facebook's suicide prevention efforts](https://www.nytimes.com/2016/06/15/technology/facebook-offers-tools-for-those-who-fear-a-friend-may-be-suicidal.html)

* __Generation text description of images__.  There's been a lot of cool work that combines computer vision and natural language processing.  One thread of that research tries to generate captions for images.  A good overview is provided in these papers:
  * [Framing Image Description as a Ranking Task: Data, Models and Evaluation Metrics](https://www.jair.org/media/3994/live-3994-7274-jair.pdf)
  * [Show and Tell: Lessons learned from the 2015 MSCOCO Image Captioning Challenge](https://arxiv.org/abs/1609.06647)
  * [From Captions to Visual Concepts and Back](http://www.m-mitchell.com/papers/CVPR15_0866.pdf)
There are even several tutorials on how to get started with caption generation: 
  * [A Gentle Introduction to Deep Learning Caption Generation Models](https://machinelearningmastery.com/deep-learning-caption-generation-models/)
  * [How to Develop a Deep Learning Photo Caption Generator from Scratch](https://machinelearningmastery.com/develop-a-deep-learning-caption-generation-model-in-python/)
  * [Caption this, with TensorFlow. How to build and train an image caption generator using a TensorFlow notebook.](https://www.oreilly.com/learning/caption-this-with-tensorflow)

# What do you need to turn in?

For Milestone 1, you'll need to turn in writeups for your 3 project ideas.  

For the whole project, here's a provisional list of the deliverables that you'll need to submit:

1. `report.md`: The final version of your write-up, incorporating any additional changes to your revised draft (if any).
1. `readme.md`: A brief description of your task and the included code.
1. `data-train/`: A directory containing the training data.
1. `data-dev/`: A directory containing the development data for local evaluation.
1. `data-test/`: A directory containing the test data for leaderboard evaluation.
1. `default`: A full implementation of the default system.
1. `baseline`: A skeleton of the baseline system to be provided to students.
1. `baseline-solution`: A full implementation of the baseline system.
1. `extension-1`, `extension-2`, ...: Full implementations of the extensions, one per group member.
1. `extensions.md`: A brief write-up describing your extensions and their performance.
1. `grade-dev`: A grading script for local evaluation. This may be a wrapper around a generic grading script `grade`.
1. `grade-test`: A grading script for leaderboard evaluation. This may be a wrapper around a generic grading script `grade`.



