---
layout: default
img: estimating_time.png
caption: Don't Panic
img_link: https://xkcd.com/1658/   
title: The Term Project
active_tab: homework
release_date: 2019-03-26
due_date: 2019-04-30T11:59:00EST
attribution: This assignment was developed by the CIS 530 course staff.
deliverables:
    -
      description: Milestone 1 - Form a team and submit three project ideas
      due_date: 2019-04-02T11:59:00EST
    -
      description: Milestone 2 - Collect your data, and write an evalation script and a simple baseline
      due_date: 2019-04-16T11:59:00EST
    -
      description: Milestone 3 - Implement a published baseline.  Prepare a project presentation
      due_date: 2019-04-23T11:59:00EST
    -
      description: Milestone 4 - Finish all your extensions to the public baseline, and submit your final project writeup
      due_date: 2019-04-30T11:59:00EST
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


Your term project will be a self-designed multi-week team-based effort. You are welcome to select one of the project ideas that we suggest, or to design your own. Your final project will consist of the following components:

1. A formal definition of the problem and a motivation for while it is an interesting challenge for natural language processing. 
1. A commented implementation of the simplest possible solution to the problem.  For instance, this could be a majority class baseline or a random baseline. 
1. A commented implementation of a baseline published in the literature, along with
   skeleton code obtained by removing the parts that students should implement.
1. One extension per team member that attempts to improve on the baseline, along
   with a brief (one- to three-paragraph) accompanying write-up for each extension
   describing the general approach and whether it worked.
1. A evaluation script that can be used to score
   submissions like on the class leaderboard. The output of any model
   implementations should be gradeable with this program.

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


## What will you need to turn in?


Here's a provisional list of the deliverables that you'll need to submit at the end of the project.  Each milestone will also have its own deliverables

1. `report.pdf`: The final version of your write-up, incorporating any additional changes to your revised draft (if any).
1. `readme.md`: A brief description of your task and a description of your code.
1. `data-train/`: A directory containing the training data.
1. `data-dev/`: A directory containing the development data for local evaluation.
1. `data-test/`: A directory containing the test data for leaderboard evaluation.
1. `default`: A full implementation of the default system.
1. `baseline`: An implementation of your baseline system.
1. `extension-1`, `extension-2`, ...: Full implementations of the extensions, one per group member.
1. `grade-dev`: A grading script for local evaluation. This may be a wrapper around a generic grading script `grade`.
1. `grade-test`: A grading script for leaderboard evaluation. This may be a wrapper around a generic grading script `grade`.




# Milestone 1

For Milestone 1, you'll need to form a team and come up with 3 project ideas.  For each idea you should describe:
1. A problem definition (1 to 2 paragraphs, plus an illustrative example)
1. A pointer to two or more more papers or sections textbook that describes the problem
1. What evaluation metrics could use to score system outputs 
1. What type of data you will need to evaluate, and how much data is available 


The term project is a team exercise.  The minimum team size is 4, and the max team size is 6.  If you need help finding a team, you can post on [this Piazza thread](https://piazza.com/class/jqh5n0qv849p0?cid=5).

You should turn in a PDF with your 3 ideas and your team.  If you have a prefrence on which project you'd like to pursue, you're welcome to indicate that in your report too.


## Project Ideas

You should identify what topic you would like to work on.  Pretty much any topic in natural language processing is fair game.  The first milestone for the term project is to pick 3 topic ideas that your team might be interested in exploring.  The course staff will help assess the feasibility of your ideas and will make a recommendation of which of your 3 initial ideas is the best fit for the scope of the term project.  

* **Bias in word vectors** - Perhaps suprisingly, there is gender and racial bias in word embeddings.  For your term project, you can replicate the findings in [*Semantics derived automatically from language corpora contain human-like biases*](https://purehost.bath.ac.uk/ws/portalfiles/portal/168480066/CaliskanEtAl_authors_full.pdf) by Aylin Caliskan, Joanna Bryson, Arvind Narayanan (2017) or in [*Word embeddings quantify 100 years of gender and ethnic stereotypes*](https://www.pnas.org/content/115/16/E3635.short) by Nikhil Garg, Londa Schiebinger, Dan Jurafsky, and James Zou.  They show that word vectors trained on web data encode a spectrum of known biases, as measured by the Implicit Association Test.  This is largely due to the fact that people's biases are expressed in their writing and thus in the data we use to train our emeddings.  After you recreate these results, you can see if it is possible to remove the bias by anonymizing names and gender nouns and pronouns in the training data.  You could then retrain word embeddings (glove, word2vec and/or Fasttext) and then measure see if the bias is still present.  

* **Identifying words to anonymize** - Clinical records with protected health information (PHI) cannot be directly shared as is, due to privacy constraints, making it particularly cumbersome to carry out NLP research in the medical domain. A necessary precondition for accessing clinical records outside of hospitals is their de-identification, i.e., the exhaustive removal (or replacement) of all mentioned PHI phrases. To determine how well we are able to identify PHI phrases, a group has prepared Medical Document Anonymization Task (MedDocAn).  The MedDocAn task is run on a synthetic corpus of 1000 clinical case studies. This corpus was selected manually by a practicing physician and augmented with PHI information from discharge summaries and medical genetics clinical records.  The challenge for this project will be to perform entity recognition on the data, and detect sensitive spans. Find information at the [MedDocAn task page](http://temu.bsc.es/meddocan).

* **Identifying claims and perspectives that support or refute them** - There are many ways to respond to a claim such as "animals should have lawful rights", and these responses form a spectrum of perspectives, each with a stance relative to this claim and, ideally, with evidence supporting it. Inherently, this is a natural language understanding task.  You can address the task of *substantiated perspective discovery* where, given a *claim*, a system is expected to discover a diverse set of well-corroborated perspectives that take a stance with respect to the claim. Each perspective should be substan- tiated by evidence paragraphs which summarize pertinent results and facts. We recently created [PERSPECTRUM](https://www.cis.upenn.edu/~ccb/publications/discovering-diverse-perspectives.pdf), a dataset of claims, perspectives and evidence, making use of online debate websites to create the initial data collection, and augmenting it using search engines in order to expand and diversify our dataset.  


* **Training emeddings with different types of contexts** - word2vec and GloVe train word embeddings using local context information like a small window surrounding words.  You could implement software for training word embeddings from different types of contexts, like widening the narrow context windows to complete documents, or contexts like [*Dependency-Based Word Embeddings*](https://www.aclweb.org/anthology/P14-2050) by Omer Levy and Yoav Goldberg.  Perform a systematic analysis of how different contexts change the learned embeddings, using the evaluation methodology outlined in [*Evaluation of Word Vector Representations by Subspace Alignment*](http://www.cs.cmu.edu/~ytsvetko/papers/qvec.pdf) by Yulia Tsvetkov et al.

* **Create cross-lingual embeddings** - experiment with various methods for creating [cross-lingual word embeddings](https://www.aclweb.org/anthology/P16-1157) and evaluate how good each method is at learning missing entries in a bilingual dictionary.  Here's a set of [100 bilingual dictionaries](http://cs.brown.edu/people/epavlick/data.html) that you can use.  

* **Commonsense inference with BERT and SWAG** - [BERT](https://arxiv.org/abs/1810.04805) has shown to be very effective at many language understanding tasks.  For your project you can evaluate how well BERT solves Grounded Commonsense Inference in the new [SWAG data set](https://arxiv.org/pdf/1808.05326.pdf).  There's a github repo with [BERT as a service](https://github.com/hanxiao/bert-as-service) that should allow you to get up and running quickly.  For extensions for this project, you can try to replicated SWAG's adversarial dataset collection methodology, but with BERT as the model. 

* **Order prenominal modifiers** - In English, prenominal modifiers must come in a certain order.   It sounds fluent to say *the big beautiful white wooden house*, but not *the white wooden beautiful big house*.  Here's a NLP good paper describing a [class-based approach to ordering prenominal modifiers](http://www.aclweb.org/old_anthology/W/W09/W09-0608.pdf).
You could collect all of the pre-nominal modifiers from a large parsed corpus like the [WaCKy corpora](http://wacky.sslmit.unibo.it/doku.php?id=corpora) or the [Annotated Gigaword](https://catalog.ldc.upenn.edu/ldc2012t21), and then train a model to predict their order.   Here's a rule from a grammar book about what order adjectives are supposed to come in.  Is it true?
 <blockquote align="center" class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Things native English speakers know, but don&#39;t know we know: <a href="https://t.co/Ex0Ui9oBSL">pic.twitter.com/Ex0Ui9oBSL</a></p>&mdash; Matthew Anderson (@MattAndersonNYT) <a href="https://twitter.com/MattAndersonNYT/status/772002757222002688?ref_src=twsrc%5Etfw">September 3, 2016</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

 * **Generation text description of images** - There's been a lot of cool work that combines computer vision and natural language processing.  One thread of that research tries to generate captions for images.  A good overview is provided in these papers:
   - [Framing Image Description as a Ranking Task: Data, Models and Evaluation Metrics](https://www.jair.org/media/3994/live-3994-7274-jair.pdf)
   - [Show and Tell: Lessons learned from the 2015 MSCOCO Image Captioning Challenge](https://arxiv.org/abs/1609.06647)
   - [From Captions to Visual Concepts and Back](http://www.m-mitchell.com/papers/CVPR15_0866.pdf)
   - There are several tutorials on how to get started with caption generation:  [A Gentle Introduction to Deep Learning Caption Generation Models](https://machinelearningmastery.com/deep-learning-caption-generation-models/)
   - [How to Develop a Deep Learning Photo Caption Generator from Scratch](https://machinelearningmastery.com/develop-a-deep-learning-caption-generation-model-in-python/)
   - [Caption this, with TensorFlow. How to build and train an image caption generator using a TensorFlow notebook.](https://www.oreilly.com/learning/caption-this-with-tensorflow)

In addition to these ideas, you can check out the numerous [shared tasks](shared-tasks.html) that are run by the NLP community.  Shared tasks are a good fit for the term project, because they provide shared data, establish evaluation metrics, and  there will be several publications describing how researchers approached the tasks.


<a name="milestone-2"></a>
# Milestone 2

The course staff will review the 3 ideas that you submitted for Milestone 1, and make a recommendation on which of your ideas you ought to pursue.  For Milestone 2, your job is to get started on that idea with three steps:
1. Collect your data
2. Write an evaluation script
3. Write a simple baseline (for instance, a majority class baseline)

We have also assigned a course staff member to be your mentor.  Feel free to reach out to your mentor with any questions.

## Collect your data

Since most of the projects that we do in this course are data-driven, it's very important to have your data ready to go at the outset of a project.  You should collect all of the data that you'll need for your term project and split the data into three pieces:

* Training data
* Development data
* Test data

The training data will be used to train the model, the dev data can be used to optimize your system parameters and/or to evaluate different approaches to the problem, the test data is a "blind" test set that will be used in the final evaluation.

If you are basing your term project on a shared task, then usually the data will be collected already, and usually it will be divided into a standard training/dev/test split.  If it's already assembled and split - great!  You're ahead of the game.  If you're not doing a shared task, then you may need to assemble your own data.  A good way of creating your own training/dev/test split is to divide the data into chunks that are sized around 80%/10%/10%, where you want to use most of the data for training.  It's important to ensure that the same items don't appear in more than one of the splits.

For your M2 deliverables, we'll ask you to submit your data, plus a markdown file named data.md that describes the format of the data.  If your data is very large, then you can submit a sample of the data and give a link to a Google Drive that contains the full data set.   You data.md should describe the number of items in each of your training/dev/test splits.

## Write an evaluation script

For the next part of M2, you'll need to determine a suitable evaluation metric for your task, and implement it.  If you're basing your term project on a shared task, then there is likely an established evaluation metric for the task.  You should re-use it. If you're doing a new task, then you may have to do a literature review in order to determine what metrics are best suited for your task.

You should write an evaluation script that takes two things as input: a system's output and a corresponding set of gold standard answers.  Your script should output a number that quantifies how good the system's answers are.    

For your deliverables, you should include your script, plus an example of how to run it from the command line.  You should give a formal definition of the evaluation metric that explains how it is calculated in a markdown file called scoring.md - this file should  cite any relevant papers that introduce the metric.    You can also cite Wikipedia articles that describe your evaluation metric, and/or link to an overview paper describing the shared task that you're basing your project on if it defines the metric.

## Write a simple baseline

As the final part of M2, you should write a simple baseline.  This should be the simplest way of producing output for your task.  For example, it could be a majority class baseline (like the one that we used in HW1) that determines the majority class from the training data and guesses that class for each item in the test set.

You should write a python program that will generate the output for the baseline, and you should submit that as simple-baseline.py.  You should also include a markdown file named simple-baseline.md that describes your simple baseline, gives sample output, and reports the score of the baseline when you run it on the test set, and evaluate it with your scoring script. 


## What do you need to turn in?

* You should create a directory containing your training/dev/test data (please create a gzipped tar archive of the data).  If your data is too large to upload to gradescope, the you can submit a sample of the training data, plus your compute dev and test sets.
* Please upload a markdown file that describes your data (name it data.md).  It should give an example of the data, describe the file format of the data, give a link to the full data set (if you're uploading a sample), and give a description of where you collected the data from.
* You should describe your evaluation metric in a markdown file called scoring.md.  This should give a formal definition of your metric, and relevant citations to where it was introduced.  Your scoring.md file should also show how to run your evaluation script on the command line (with example arguments, and example output).  The scoring.md file should say whether higher scores are better, or lower scores are better.
* You should include your evaluation script (you can call then score.py if you're writing it in python).
* You should upload simple-baseline.py and describe it in simple-baseline.md.  Your simple-baseline.md should say what score your evaluation metric gives to the simple baseline for your test set.



<a name="milestone-3"></a>
# Milestone 3

The goals of Milestone 3 are to do a literature review to determine the approaches that other researchers took to solve your problem, and to implement a published system to establish as a strong baseline for your project.

For your literature review, you should read 3-5 research papers that address the problem that you are working on.  You should write a 1-2 paragraph summary of each paper, desribing the approaches that they proposed and what results they got.  You should also include an addition 1-2 paragraphs saying which of the approaches that you selected as the published baseline that you are re-implementing.  You should submit your literature review in a markdown formatted file called lit-review.md.

You should re-implement the published baseline that you selected.  It's fine to use machine learning packages like sklearn, or NLP software like Spacy or NLTK, but you should implement the main algorithms yourself.  You should not turn in existing code that implements the baseline.

You should include a baseline.md markdown file that includes step-by-step instructions on how to run your baseline code.   Your baseline.md should also report the score for your system for your test and development data, and compare that to your random baseline.

For Milestone 3, you will also prepare an in-class presentation for your project.
Your in-class presentation should be 12 minutes long.  You should create a slidedeck with [Google Slides](https://www.google.com/slides/about/).  Your presentation should convey  these main ideas:
* What is the topic of your term project?  You should clearly explain to your classmates the problem that you selected to work on.  Give an illustrative example of the problem first, and then give a more formal definition of the problem.
* What is exciting about your term project?  Why did you want to work on this topic?  
* How does the topic relate to the class? What new things did you learn? 

You may also want to cover topics like this:
* What kind of data is available for this problem?  How do you evaluate whether a solution is good or not?  If the evaluation metric is not already familiar to the class, then walk through an explanation of how it works.
* What is the baseline performance for the simple baseline like a majority class baseline?
* What approaches have people taken in the past?  How successful have they been?
* What did you implement for your published baseline?



For Milestone 4, you'll need to implement several extensions beyond this published baseline.  These should be different experiments that you run to try to improve its performance.  The number of extension that you'll implement depends on number of members of your group.  If you have 4 team members, you should implement 2 extensions.  If you have 5, then 3 extensions.  If you have 6, then 4 extensions. 



## What do you need to turn in?

* You should submit a literature review in a markdown file called lit-review.md.  This will include the citation information for each paper  (authors, title of paper, publication venue, year of publication, number of pages) in a Works Citated section. You should have a 1-2 paragraph description of each paper, plus a 1-2 paragraph explanation of which one you chose to implement as your baseline and why.
* You should submit your code for the baseline system.  This should be in a python file called a baseline.py.  You should also submit a baseline.md file explaining how to run it, and reporting its performance on your dev and test set, according to your evaluation metric. 

* A markdown file called homework.md that contains the write-up your project as if it were a homework assignment. 
* A markdown file called extensions.md that desribes the extension(s) to the published baseline that you implemented for Milestone 4.  It should explain what you tried, and whether it improved performance over the baseline (it's OK if it didn't).  You should include tables of results using your scoring function and test data.



<a name="milestone-5"></a>
# Milestone 4

For your final milestone, you'll complete your extensions to the baseline, and you'll produce a final writeup for your term project.  As a reminder, the number of extensions that you must submit depends on your group size.  If you have 4 team members, you should implement 2 extensions.  If you have 5, then 3 extensions.  If you have 6, then 4 extensions. You already produced one of those extensions for Milestone 4.

Your final report should be written in the style of a scientific paper.  It should contain the following sections:

* Title.  A descrpitive title for your term project
* Authors.  A list of team members
* Abstract.  Your abstract should give an overview of your project and your results (~100 words).
* Introduction.  Your introduction should contain the following information. (~300-500 words, plus one illustrative example).
   * An informal description of the task, and how it relates to NLP/Computational Linguistics (1-2  paragraphs)
   * A figure that illustrates the task, or an illustrative example of the type of problem you're trying to solve.  This can be a picture, or an example of an input and output.  You should include a caption or a short paragraph that describes what's happening in your illustration.
   * A formal definition of the problem.
   * A paragraph describing why you picked this task for your term project. 
* Literature Review. You can adapt your literature review from Milestone 3 for this part of your writeup.  (~300-500 words, with 3 or more ciations).
   * If you adapted a shared task for your term project, then you should describe the share task in your literature review, and cite the overview paper and give a URL to shared task homepage (if applicable).
   * For your literature review, you should also cute and summarize 3-5 research papers that address the problem that you are working on.  You should write a 1-2 paragraph summary of each paper, desribing the approaches that they proposed and what results they got.  Be sure to include a full citation of these papers in your Bibliography. 
* Experimental Design.  Your Experimental Design section should include a description of your training data, your evaluation metric, and your simple baseline model along with its performance on the test set.  You can adapt your Milestone 2 submission for this part. (~300-500 words, plus 2 figures/tables, plus 1 or more equations).
   * Data.  This subsection should describe your training/development/test data.  You should give an figure or table with examples from your data (including inputs and output labels).  You should include a table that describes the size of your data sets.  For example, it should give number of sentences or words, etc for each of the splits.  You should also characterize the data.  For instance, if there's a skewed distribtuion over the labels, you should reoprt it here.  If your training data comes from a published paper, then cite that paper and explain how they collected the data.  If you constructed your data set, then explain in detail how you collected it, and include example code in an appendix.
   * Evaluation Metric.  This subsection should describe your evaluation metric.  You should include an English description of the metric, an equation for how your metric is computed, and a citation for this metric, and some citation(s) that shows what past publication(s) used this metric for the task that you're working on. For your equation, you can use [MathJax](https://www.mathjax.org) markup.
   * Simple baseline.  You should compute the majority class baseline (or other simple baseline) for your data, and report it in this section.  This is a way of characterizing the data and showing the diffiulty of the task.  
* Experimental Results.  In this section, you should describe your implementation of a published baseline, and all of the extensions that you experimented with for your term project, and an error analysis of your system's output. (~300-500 words).
   * Published baseline.  In this subsection you should write a detailed description of the published baseline that you implemented and cite the paper that it was published in. (You can update your Milestone 4 submission for this).  You should report how well the model performs on your test set using the evaluation metric that you defined in your experimental design section.  Does your implementation of the published baseline reach the same level of accuracy as the original paper?  If not, why not?  Are your results directly comparable -- are they on the same test set?  If not, why not?
   * Extensions.  In this subsection, you should describe each of the extensions that you tried.  You should include a ~1-2 paragraph of each extension that explains what you tried, why you tried it, and how it performed compared to your baseline.  You should include a table of results, where the rows are the performance of the baseline or one of your extensions, and the columns are  the performance on the test set (and on the dev set if you measured it).  If you did any experiments where you searched over a set of different parameters, then you should include a result on how varying the parameter changed the performance on the dev or test set.  Your tables and figures should include a detailed caption that explain how to read them.
   * Error analysis.  In this subsection, you should perform an error anlaysis for your best performing system.  Show examples of the errors that it makes.  Can you cateorize the types of errors that it makes, and give an esimate of how prevelant each error type is?  If you extensions performed better than the published baseline, then show examples of the errors that the published baseline makes that your extensions get correct (and vice versa if your extension introduces some new errors).  
* Conclusions. You should write a brief summary of what you accomplished in your term project.  Did any of your implementations reach state-of-the-art performance on the task?  If not, how close did you come?  If not very close, then why not?  (~100-300 words). 
* Acknowledgements.  If you used someone else's code or you benefited from discussions with one of the TAs, then you should thank them here.  Give credit generously!   (Optional)
* Appendicies. This can include short snippets of code that were relevant to your project, along with a description of what it's doing.  It could also include more examples of your training data or your system's output. (Optional)

I really like examples and good illustrations.  If you created some nice visuals for your final presentation slides, then I encourage you to include them in your writeup too.  You can submit your images in a images/ subfolder.


## What do you need to turn in?

You should turn  the following items:
* final-report.pdf 
* data/ - a subdirectory containing the training/dev/test splits that you use.  If your data is too large to submit, then you can include a file named download.md that explains how to download your data.
* code/ - a subdirectory containing all code that you developed for your project, including the baseline and extensions, and your evaluation scripts.  This should include a README.md that gives a step by step walk thorugh of how to run your code, including an example of the command lines to run to reproduce the results that you report. 
* output/ - a subdirectory containing your model's predictions on the test set, along with the gold labels.  This should also include a README.md that shows the command line on how to run your evaluation script on the output, and example of what scores the script returns.


You've reached the end.  Great job!