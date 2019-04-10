---
layout: default
img: google-search.jpg
caption: Resources just for you! Easier than Googling!
title: Resources
active_tab: resources
---

References 
=============================================================

* [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) by Dan Jurafsky and Jim Martin. The authors have a public draft of the next edition of their textbook online.
* [Linguistic Fundamentals for Natural Language Processing: 100 Essentials from Morphology and Syntax](http://www.morganclaypool.com/doi/pdf/10.2200/S00493ED1V01Y201303HLT020) by Emily Bender
* [Neural Network Methods for Natural Language Processing](http://www.morganclaypool.com/doi/abs/10.2200/S00762ED1V01Y201703HLT037) by Yoav Goldberg
* [Michael Collins' notes on statistical NLP](http://www.cs.columbia.edu/~mcollins/)
* [Neural Machine Translation](https://arxiv.org/abs/1709.07809) by Philipp Koehn


Tutorials 
=============================================================
* [Practical Deep Learning For Coders, Part 1](http://course.fast.ai)
* [Cutting Edge Deep Learning For Coders, Part 2](http://course.fast.ai/part2.html)
* [Word2Vec Tutorial](http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/)
* [Christopher Olah's blog](http://colah.github.io/)

NLP courses at other universities
=============================================================

* [Yoav Artzi's Natural Language Processing class at Cornell](http://yoavartzi.com/cs5740-sp18-temp/)
* [Jason Eisner's NLP class at Johns Hopkins University](https://www.cs.jhu.edu/~jason/465/)
* [Chris Manning and Richard Socher's course at Stanford](https://web.stanford.edu/class/cs224n/)
* [Graham Neubig's Machine Translation and Sequence to Sequence Models at CMU](http://www.phontron.com/class/mtandseq2seq2017/)


Python resources
=============================================================

- Python itself has good documentation and a decent getting started page [here](https://docs.python.org/2/tutorial/introduction.html).
- Python gives a list of good tutorials [here](https://wiki.python.org/moin/BeginnersGuide/Programmers). Many are focused on people with no programming background, but two that seem a bit less introductory are the [Python in 10 minutes](http://www.stavros.io/tutorials/python/) tutorial, and [Google's Python class](https://developers.google.com/edu/python/).
- There is a [Coursera course on Python](https://www.coursera.org/course/interactivepython) running now.
- [Scikit-learn](http://scikit-learn.org/stable/) is an amazingly easy library for doing machine learning in Python. It is also wonderfully verbosely documented with tons of examples.
- [Kaggle has some tutorials on sklearn](https://www.kaggle.com/c/data-science-london-scikit-learn/visualization)
- [spaCy](https://spacy.io) is excellent Python NLP library.  It also has a cleverly named visualization tool, [displaCy](https://spacy.io/usage/visualizers).
- AllenNLP[https://github.com/allenai/allennlp] is an open-source NLP research library from [AI2](http://www.allenai.org), built on PyTorch

Using python 3.5+ on biglab
====================================
Biglab has python3.4 installed, which is a little out of date, so if you want to use a more modern python, follow these steps. First, to get to biglab:

{% highlight bash %}
$ ssh USERNAME@biglab.seas.upenn.edu
{% endhighlight %}

(where USERNAME is your Penn username)

You can either use an existing miniconda installation, or you can download your own.

### 1. Use existing miniconda installation

For this, open up `~/.bashrc` and add this line to the end:

{% highlight bash %}
export PATH="/home1/m/mayhew/miniconda3/bin:$PATH"
{% endhighlight %}

Restart your terminal (exit and ssh in again), and python should be version 3.6 from anaconda.

### 2. Install miniconda in your home directory

This is more involved, but may give you more freedom. Anaconda is a collection of scientific packages for python, and also a virtual environment manager. I suggest miniconda, which is a stripped down version. To install go here: [https://conda.io/miniconda.html](https://conda.io/miniconda.html). Alternatively, run this:

{% highlight bash %}
$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ chmod +x Miniconda3-latest-Linux-x86_64.sh
$ . Miniconda3-latest-Linux-x86_64.sh
{% endhighlight %}

Then restart your terminal (exit and ssh in again), and run this:

{% highlight bash %}
$ conda install gensim
{% endhighlight %}

Bash resources
==============

- [John](https://seas.upenn.edu/~johnhew/) has a basic introduction to bash for NLP [here](tutorials/2017-03-06-bash-for-nlp-tutorial-basic.html), and a discussion of advanced topics in bash [here](tutorials/2017-03-07-bash-for-nlp-tutorial-topics.html).
- Kevin Knight of the University of Southern California has a nice unix skills for NLP tutorial [here](http://www.isi.edu/natural-language/mt/unix.txt).


Screen / byobu / tmux
========================

Since you will be running code remotely, we strongly recommend that you use some sort of session manager. I (Stephen) use [screen](https://kb.iu.edu/d/acuy), but other options are [byobu](https://help.ubuntu.com/community/Byobu), or [tmux](https://github.com/tmux/tmux/wiki). These allow you to ssh to a remote machine, start a terminal session, disconnect from it, and reconnect at a later time. This is especially useful when you want to run long jobs. Here's a [sample screenrc file](https://github.com/mayhewsw/dotfiles/blob/master/screenrc).
