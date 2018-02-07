---
layout: default
img: ios_keyboard.png
caption: Movie quotes according to autocomplete
img_link: https://www.explainxkcd.com/wiki/index.php/1427:_iOS_Keyboard
title: Homework 5 - Character-based Language Models
active_tab: homework
release_date: 2018-02-07
due_date: 2018-02-14T11:00:00EST
attribution: This assignment is based on [The Unreasonable Effectiveness of Character-level Language Models](http://nbviewer.jupyter.org/gist/yoavg/d76121dfde2618422139) by Yoav Goldberg and [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) by Andrej Karpathy. Daphne Ippolito, John Hewitt, and Chris Callison-Burch adapted their work into a homework assignment for UPenn's CIS 530 class in Spring 2018.  
readings:
-
   title: Language Modeling with N-grams
   authors: Dan Jurafsky and James H. Martin
   venue: Speech and Language Processing (3rd edition draft)
   type: textbook
   url: https://web.stanford.edu/~jurafsky/slp3/4.pdf
-
   title: The Unreasonable Effectiveness of Recurrent Neural Networks
   authors: Andrej Karpathy 
   venue: Blog post.
   type: blog
   year: 2015
   url: http://karpathy.github.io/2015/05/21/rnn-effectiveness/
-
   title: The Unreasonable Effectiveness of Character-level Language Models
   authors: Yoav Goldberg
   venue: Response to Andrej Karpathy's blog post.
   type: blog
   year: 2015	
   url: http://nbviewer.jupyter.org/gist/yoavg/d76121dfde2618422139
-
   title: Language Independent Authorship Attribution using Character Level Language Models
   authors: Fuchun Pen, Dale Schuurmans, Vlado Keselj, Shaojun Wan
   type: conference
   year: 2003
   venue: EACL
   url: http://www.aclweb.org/anthology/E/E03/E03-1053.pdf
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


Character-based Language Models <span class="text-muted">: Assignment 5</span>
=============================================================

In the textbook, language modeling was defined as the task of predicting the next word in a sequence given the previous words. In this assignment, we will focus on the related problem of predicting the next *character* in a sequence given the previous characters. 

The learning goals of this assignment are to: 
* Understand how to compute language model probabilities using maximum likelihood estimation
* Implement basic smoothing, back-off and interpolation.
* Have fun using a language model to probabilistically generate texts.
* Use a set of language models to perform text classification. 
* Try out a more advanced form of language modeling using a Recurrent Neural Network. 


<div class="alert alert-info" markdown="1">
* todo - give the students a training/dev/test split.
* todo - skeleton python code.
* todo - training/dev data for text classification task.
</div>


## Part 1: Unsmoothed Maximum Likelihood Character-Level Language Models 

We're going to be starting with some [nice, compact code for character-level language models](http://nbviewer.jupyter.org/gist/yoavg/d76121dfde2618422139). that was written by [Yoav Goldberg](http://u.cs.biu.ac.il/~yogo/).  Here's Yoav's code for training a language model:

### Train a language model

{% highlight python %}
from collections import *

def train_char_lm(fname, order=4):
    data = open(fname).read()
    lm = defaultdict(Counter)
    pad = "~" * order
    data = pad + data
    for i in range(len(data)-order):
      history, char = data[i:i+order], data[i+order]
      lm[history][char]+=1
    def normalize(counter):
      s = float(sum(counter.values()))
      return [(c,cnt/s) for c,cnt in counter.items()]
    outlm = {hist:normalize(chars) for hist, chars in lm.items()}
    return outlm
{% endhighlight %}

`fname` is a file to read the characters from. `order` is the history size to consult. Note that we pad the data with leading `~` so that we also learn how to start.


Now you can train a language model.  First grab some text like this corpus of Shakespeare:

``` bash
$ wget http://cs.stanford.edu/people/karpathy/char-rnn/shakespeare_input.txt`
```

Now train the model:
{% highlight python %}
lm = train_char_lm("shakespeare_input.txt", order=4)
{% endhighlight %}

### P(hello world) 

Ok. Now we can look-up the probability of the next letter given some history.  Here are some example queries:

{% highlight python %}
>>> lm['hell']
[('!', 0.06912442396313365), (' ', 0.22119815668202766), ("'", 0.018433179723502304), ('i', 0.03225806451612903), ('\n', 0.018433179723502304), ('-', 0.059907834101382486), (',', 0.20276497695852536), ('o', 0.15668202764976957), ('.', 0.1336405529953917), ('s', 0.009216589861751152), (';', 0.027649769585253458), (':', 0.018433179723502304), ('?', 0.03225806451612903)]
{% endhighlight %}

Actually, let's pretty print the output, and sort the letters based on their probabilities.

{% highlight python %}
import pprint
import operator

def print_probs(lm, history):
    probs = sorted(lm[history],key=lambda x:(-x[1],x[0]))
    pp = pprint.PrettyPrinter()
    pp.pprint(probs)
{% endhighlight %}

OK, print again:

{% highlight python %}
>>> print_probs(lm, "hell")
[(' ', 0.22119815668202766),
 (',', 0.20276497695852536),
 ('o', 0.15668202764976957),
 ('.', 0.1336405529953917),
 ('!', 0.06912442396313365),
 ('-', 0.059907834101382486),
 ('?', 0.03225806451612903),
 ('i', 0.03225806451612903),
 (';', 0.027649769585253458),
 ('\n', 0.018433179723502304),
 ("'", 0.018433179723502304),
 (':', 0.018433179723502304),
 ('s', 0.009216589861751152)]
{% endhighlight %}

This means that `hell` can be followed by any of these dozen characters: 

` ,o.!-?i;\n':s` 

and that the probability of `o` given `hell` is 15.7%, $$p(o \mid hell)=0.157$$.  The most probable character to see after `hell` is a space, $$p(o \mid hell)=0.221$$.

The distribution of letters that occur after `worl` is different than the distribution of letters that occur after `hell`.  Here is that distribution: 

{% highlight python %}
>>> print_probs(lm, "worl")
[('d', 1.0)]
{% endhighlight %}

What does that mean?  It means that in our corpus, the only possible continuation that we observed for `worl` was the letter `d`, and we assign 100% of probability mass to it, $$p(d \mid worl)=1.0$$.

### Let's write some Shakespeare!

Generating text with the model is simple. To generate a letter, we will look up the last `n` characters, and then sample a random letter based on the probability distribution for those letters.   Here's Yoav's code for that:

{% highlight python %}
from random import random

def generate_letter(lm, history, order):
    history = history[-order:]
    dist = lm[history]
    x = random()
    for c,v in dist:
        x = x - v
        if x <= 0: return c
{% endhighlight %}

To generate a passage of text, we just seed it with the initial history and run letter generation in a loop, updating the history at each turn.  We'll stop generating after a specified number of letters.

{% highlight python %}
def generate_text(lm, order, nletters=500):
    history = "~" * order
    out = []
    for i in range(nletters):
        c = generate_letter(lm, history, order)
        history = history[-order:] + c
        out.append(c)
    return "".join(out)
{% endhighlight %}

Now, try generating some Shakespeare with different order n-gram models.  You should try running the following commands.  

{% highlight python %}
>>> lm = train_char_lm("shakespeare_input.txt", order=2)
>>> print(generate_text(lm, 2))


>>> lm = train_char_lm("shakespeare_input.txt", order=3)
>>> print(generate_text(lm, 3))


>>> lm = train_char_lm("shakespeare_input.txt", order=4)
>>> print(generate_text(lm, 4))


>>> lm = train_char_lm("shakespeare_input.txt", order=7)
>>> print(generate_text(lm, 7))
{% endhighlight %}

What do you think?  Is it as good as [1000 monkeys working at 1000 typewriters](https://www.youtube.com/watch?v=no_elVGGgW8)?

### What the F?

Try generating a bunch of short passages:


{% highlight python %}
>>> print(generate_text(lm, 5, 40))
First, and quence
Shall we gave it. Now
>>> print(generate_text(lm, 5, 40))
First die.

KING OF FRANCE:
I prithee, 
>>> print(generate_text(lm, 5, 40))
First marriage,
And scarce it: wretches 
>>> print(generate_text(lm, 5, 40))
First, the midsummer;
We make us allia s
>>> print(generate_text(lm, 5, 40))
First choose
Which now,
Where like thee.

>>> lm = train_char_lm("shakespeare_input.txt", order=4)
>>> print(generate_text(lm, 4, 40))
First blood
assurance
To grace and leade
>>> print(generate_text(lm, 4, 40))
First, are almightly,
Am I to bedew the 
>>> print(generate_text(lm, 4, 40))
First Senato, come unexamination hast br

>>> lm = train_char_lm("shakespeare_input.txt", order=2)
>>> print(generate_text(lm, 2, 40))
Firm
Histed mor ituffe bonguis hon tract
>>> print(generate_text(lm, 2, 40))
Fir my fat,
Forromfor intre You to lor c

{% endhighlight %}

Do you notice anything?  *They all start with F!*  In fact, after we hit a certain order, the first word is always *First*?  Why is that?  Is the model trying to be clever?  First, generate the word *First*. Explain what is going on in your writeup.


## Part 2: Perplexity, smoothing, back-off and interpolation  

In this part of the assignment, you'll adapt Yoav's code in order to implement several of the  techniques described in [Section 4.2 of the Jurafsky and Martin textbook](https://web.stanford.edu/~jurafsky/slp3/4.pdf).  

### Perplexity 

How do we know whether a LM is good? There are two basic approaches:
1. Task-based evaluation (also known as extrinsic evaluation), where we use the LM as part of some other task, like automatic speech recognition, or spelling correcktion, or an OCR system that tries to covert a professor's messy handwriting into text. 
2. Intrinsic evaluation.  Intrinsic evaluation tries to directly evalute the goodness of the language model by seeing how well the probability distributions that it estimates are able to explain some previously unseen test set. 

Here's what the textbook says:

> For an intrinsic evaluation of a language model we need a test set. As with many of the statistical models in our field, the probabilities of an N-gram model come from the corpus it is trained on, the training set or training corpus. We can then measure the quality of an N-gram model by its performance on some unseen data called the test set or test corpus. We will also sometimes call test sets and other datasets that are not in our training sets held out corpora because we hold them out from the training data.

> So if we are given a corpus of text and want to compare two different N-gram models, we divide the data into training and test sets, train the parameters of both models on the training set, and then compare how well the two trained models fit the test set.

> But what does it mean to "fit the test set"? The answer is simple: whichever model assigns a higher probability to the test set is a better model.

We'll implement the most common method for intrinsic metric of language models: *perplexity*.  The perplexity of a language model on a test set is the inverse probability of the test set, normalized by the number of words. For a test set $$W = w_1 w_2 ... w_N$$:


$$Perplexity(W) = P(w_1 w_2 ... w_N)^{\frac{1}{N}}$$


$$ = \sqrt[N]{\frac{1}{P(w_1 w_2 ... w_N)}}$$


$$ = \sqrt[N]{\prod_{i=1}^{N}{\frac{1}{P(w_i \mid w_1 ... w_{i-1})}}}$$


OK - let's implement it. Here's a possible function signature for perplexity.  (We might update it during class on Wednesday).  Give it a go. 

{% highlight python %}
def perplexity(test_filename, lm, order=4)
    test = open(test_filename).read()
    pad = "~" * order
	test = pad + data
    # Your code here...
{% endhighlight %}


A couple of things to keep in mind:

1. Remember to pad the front of the file
2. Numeric underflow is going to be a problem, so consider using logs.




### Laplace Smoothing and Add-k Smoothing 

Laplace Smoothing is described in section 4.4.1.  Laplace smoothing  adds one to each count (hence its alternate name *add-one smoothing*).   Since there are *V* words in the vocabulary and each one was incremented, we also need to adjust the denominator to take into account the extra V observations.

$$P_{Laplace}(w_i) = \frac{count_i + 1}{N+V}$$

A variant of Laplace smoothing is called *Add-k smoothing* or *Add-epsilon smoothing*.  This is described in section Add-k 4.4.2.  Let's change the function definition of `train_char_lm` so that it takes a new argument, `add_k`, which specifies how much to add.  By default, we'll set it to one, so that it acts like Laplace smoothing:

{% highlight python %}
def train_char_lm(fname, order=4, add_k=1):
    # Your code here...
{% endhighlight %}

### Interpolation

Next, let's implement interpolation.  The idea here is to calculate the higher order n-gram probabilities also combining the probabilities for lower-order n-gram models.  Like smoothing, this helps us avoid the problem of zeros if we haven't observed the longer sequence in our training data.  Here's the math:

$$P_{backoff}(w_i|w_{i−2} w_{i−1}) = \lambda_1 P(w_i|w_{i−2} w_{i−1}) + \lambda_2 P(w_i|w_{i−1}) + \lambda_3 P(w_i)$$

where $\lambda_1 + \lambda_2 + \lambda_3 = 1$.


Now, write a back-off function:

{% highlight python %}
def calculate_prob_with_backoff(char, history, lms, lambdas, max_order=4)
    # Your code here...
{% endhighlight %}

You should also write a helper function to set the lambdas.  Here's a function definition that gives you access to a development set.  You can also experiment with setting them manually. 

{% highlight python %}
# returns a list of lambda values that weight the contribution of n-gram model
def set_lambdas(dev_filename, lms, max_order=4)
    # Your code here...
{% endhighlight %}

## Part 3: Text Classification using LMs

Language models can be applied to text classification. If we want to classify a text $$D$$ into a category $$c \in C={c_1, ..., c_N}$$. We can pick the category $$c$$ that has the largest posterior probability given the text. That is,

$$ c^* = arg max_{c \in C} P(c|D) $$

Using Bayes rule, this can be rewritten as:

$$ c^* = arg max_{c \in C} P(D|c) P(c)$$

If we assume that all classes are equally likely, then we can just drop the $$P(c)$$ term:

$$ = arg max_{c \in C} P(D|c)$$

Here $$P(D \mid c)$$ is the likelihood of $$D$$ under category $$c$$, which can be computed by training language models for all texts associated with category $$c$$.  This technique of text classification is drawn from [literature on authorship identification](http://www.aclweb.org/anthology/E/E03/E03-1053.pdf), where the approach is to learn a separate language model for each author, by training on a data set from that author. Then, to categorize a new text D, they use each language model to calculate the likelihood of D under that model, and pick the  category that assigns the highest probability to D.

Try it!  We'll set up a leaderboard for a text classification task.  Your job is to configure a set of language models that perform the best on the text classification task. 


## Part 4: Character-Level Recurrent Neural Networks


You will be using Pytorch for this assignment, and instead of providing you source code, we ask you to build off a couple Pytorch tutorials. Pytorch is one of the most popular deep learning frameworks in both industry and academia, and learning its use will be invaluable should you choose a career in deep learning. 

# Setup

## Using miniconda
Miniconda is a package, dependency and environment management for python (amongst other languages). It lets you install different versions of python, different versions of various packages in different environments which makes working on multiple projects (with different dependencies) easy.

There are two ways to use miniconda,

1. **Use an existing installation from another user (highly recommended)**: On ```biglab```, add the following line at the end of your ```~/.bashrc``` file.
```
export PATH="/home1/m/mayhew/miniconda3/bin:$PATH"
```
Then run the following command
```
source ~/.bashrc
```
If you run the command ```$ which conda```, the output should be ```/home1/m/mayhew/miniconda3/bin/conda```.

2. **Installing Miniconda from scratch**: On ```biglab```, run the following commands. Press Enter/Agree to all prompts during installation.
```
$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ chmod +x Miniconda3-latest-Linux-x86_64.sh
$ bash Miniconda3-latest-Linux-x86_64.sh
```
After successful installation, running the command ```$ which conda``` should output ```/home1/m/$USERNAME/miniconda3/bin/conda```.

## Installing Pytorch and Jupyter

For this assignment, you'll be using [Pytorch](http://pytorch.org/) and [Jupyter](http://jupyter.org/).

1. If you followed our recommendation and used the existing miniconda installation from 1. above, you're good to go. Stop wasting time and start working on the assignment!

2. Intrepid students who installed their own miniconda version from 2. above, need to install their own copy of Pytorch and Jupyter.
To install Pytorch, run the command
```
conda install pytorch-cpu torchvision -c pytorch
```
To check, run python and ```import torch```. This should run without giving errors.
To install jupyter, run the command (it might take a while)
```
conda install jupyter
```
Running the command ```jupyter --version``` should yield the version installed.

## How to use Jupyter notebook
For this homework, you have the option of using [jupyter notebook](https://jupyter.org/), which lets you interactively edit your code within the web browser. Jupyter reads files in the `.ipynb` format. To launch from biglab, do the following.

1. On ```biglab```, navigate to the directory with your code files and type `jupyter notebook --port 8888 --no-browser`.
2. In your local terminal, set up port forward by typing `ssh -N -f -L localhost:8888:localhost:8888 yourname@biglab.seas.upenn.edu`.
3. In your local web browser, navigate to `localhost:8888`.

# What's a char-rnn?

Good question! Andrej Karpathy, a researcher at OpenAI, has written an excellent blog post which you should read before beginning this assignment.

[http://karpathy.github.io/2015/05/21/rnn-effectiveness/](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)

Karpathy shows results for several fun domains:

Shakespeare plays

* Paul Graham essays
* LaTeX documents
* Linux source code
* Baby names

In this assignment you will follow the Pytorch tutorial code to implement your own char-rnn, and then test it on a dataset of your choice. You will also train on our provided training set, and submit to the leaderboard, where we will measure your model's complexity on our test set.

# Classification using char-rnn

## Follow the tutorial code

Read through the tutorial [here](http://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html) that builds a char-rnn that is used to classify baby names by their country of origin. While we strongly recommend you carefully read through the tutorial, you will find it useful to build off the released code [here](https://github.com/spro/practical-pytorch/tree/master/char-rnn-classification/char-rnn-classification.ipynb). Make sure you can reproduce the tutorial's results on the tutorial's provided baby-name dataset before moving on.

## Switch to city names dataset

<div class="alert alert-info" markdown="1">
Download the city names dataset.
* [training/validation sets](downloads/hw5/cities.zip)
* [test file for leaderboard](downloads/hw5/test_data.zip)
</div>

Modify the tutorial code to instead read from city names dataset. The tutorial code problematically used the same text file for both training and evaluation. We learned in class about how this is not a great idea. For the city names dataset we provide you separate train and validation sets, as well as a test file for the leaderboard.

All training should be done on the train set and all evaluation (including confusion matrices and accuracy reports) on the validation set. You will need to change the data processing code to get this working. Specifically, you'll need to modify the code in the 3rd code block to create two variables `category_lines_train` and `category_lines_val`. In addition, to handle unicode, you might need to replace calls to `open` with calls to `codecs.open(filename, "r",encoding='utf-8', errors='ignore')`.

Warning: you'll want to lower the learning rating to 0.02 or less or you might get NaNs when training.

Attribution: the city names dataset is derived from [Maxmind](http://download.maxmind.com/download/geoip/database/LICENSE_WC.txt)'s dataset.

**Experimentation and Analysis**

Complete the following analysis on the city names dataset, and include your finding in the report.

1. Write code to output accuracy on the validation set. Include your best accuracy in the report. (For a benchmark, the TAs were able to get accuracy above 50%) Discuss where your model is making mistakes. Use a confusion matrix plot to support your answer.
2. Modify the training loop to periodically compute the loss on the validation set, and create a plot with the training and validation loss as training progresses. Is your model overfitting? Include the plot in your report. TODO: Phrase better?
3. Experiment with the learning rate. You can try a few different learning rates and observe how this affects the loss. Another common practice is to drop the learning rate when the loss has plateaued. Use plots to explain your experiments and their effects on the loss.
4. Experiment with the size of the hidden layer or the model architecture How does this affect validation accuracy?

**Leaderboard**

Write code to make predictions on the provided test set. The test set has one unlabeled city name per line. You code should output a file `labels.txt` with one two-letter country code per line. Extra credit will be given to the top leaderboard submissions. Here are some ideas for improving your leaderboard performance:

* Play around with the vocabulary (the `all_letters` variable), for example modifying it to only include lowercase letters, apostrophe, and the hyphen symbol.
* Test out label smoothing
* Try a more complicated architecture, for example, swapping out the RNN for LSTM or GRU units.
* Use a different initalization for the weights, for example, small random values instead of 0s

In your report, describe your final model and training parameters.

# Text generation using char-rnn

In this section, you will be following more Pytorch tutorial code in order to reproduce Karpathy's text generation results. Read through the tutorial [here](http://pytorch.org/tutorials/intermediate/char_rnn_generation_tutorial.html), and then download [this ipython notebook](https://github.com/spro/practical-pytorch/tree/master/char-rnn-generation) to base your own code on.

You will notice that the code is quite similar to that of the classification problem. The biggest difference is in the loss function. For classification, we run the entire sequence through the RNN and then impose a loss only on the final class prediction. For the text generation task, we impose a loss at each step of the RNN on the predicted character. The classes in this second task are the possible characters to predict.

TODO: Things we could ask the students to do
1. Implement perplexity and show a plot of training time vs. perplexity
2. Play with the architecture
3. Add a <start token> to the vocabular.

## Experimenting with your own dataset

Be creative! Pick some dataset that interests you. Here are some ideas:

* [ABC music format](https://raw.githubusercontent.com/rdeese/tunearch-corpus/master/all-abcs.txt)
* [Donald Trump speeches](https://github.com/ryanmcdermott/trump-speeches)
* [Webster dictionary](http://www.gutenberg.org/cache/epub/29765/pg29765.txt)
* [Jane Austen novels](http://www.gutenberg.org/files/31100/31100.txt)

## Analysis

# Deliverables
<div class="alert alert-warning" markdown="1">
Here are the deliverables that you will need to submit:
* writeup.pdf
* code (.zip). It should be written in Python 3 and include a README.txt briefly explaining how to run it.
* `labels.txt` predictions for leaderboard.
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