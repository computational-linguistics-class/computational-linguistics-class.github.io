---
layout: default
img: clusters.png
caption: Did you know that matplotlib has an xkcd() function?
img_link: https://matplotlib.org/xkcd/examples/showcase/xkcd.html    
title: Homework 5 - Language Modelling with Neural Nets
active_tab: homework
release_date: 2018-02-07
due_date: 2018-02-14T11:00:00EST
attribution: Daphne Ippolito, John Hewitt, and Chris Callison-Burch developed this homework assignment for UPenn's CIS 530 class in Spring 2018.
readings:
---

In the textbook, language modeling was defined as the task of predicting the next word in a sequence given the previous words. In this assignment, we will focus on the more computationally-lightweight problem of predicting the next character in a sequence given the previous characters. You'll also solve a text classification problem like in Homework 2, except you'll do so with a recurrent neural net rather than handcrafted features. 

You will be using Pytorch for this assignment, and instead of providing you source code, we ask you to build off a couple Pytorch tutorials. Pytorch is one of the most popular deep learning frameworks in both industry and academia, and learning its use will be invaluable should you choose a career in deep learning. 

# Setup

## Installing Pytorch

Pytorch is not installed on biglab. To install it, you will first need to create a [Python virtual environment](https://docs.python.org/3/library/venv.html). A virtual environment allows you to install Python packages locally without having root access. (If you are running locally or you've already done this, you can skip this step.) Run the following two commands:

``` bash
python3 -m venv ~/py3env
source ~/py3env/bin/activate
```

Now to install Pytorch, follow the instructions on [http://pytorch.org/](http://pytorch.org/), specifying the options appropriately. On biglab, you will want to use 

```
Package Manager: pip
Python: 3.5
CUDA: None
```

Success!

## How to use IPython notebook

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

## Following the tutorial code

Follow the tutorial [here](http://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html) to build a char-rnn that is used to classify baby names by their country of origin. While we strongly recommend you carefully read through the tutorial, you might find it useful to build off the released code [here](https://github.com/spro/practical-pytorch/tree/master/char-rnn-classification). Make sure you can reproduce the tutorial's results on the provided baby-name dataset before moving on.

A note on the assignment. The tutorial code defines epoch differently than in the textbook. TODO: finish writing

## Using the city names dataset

<div class="alert alert-info" markdown="1">
Download the city names dataset.
* [training set](downloads/hw5/train.zip)
* [validation set](downloads/hw5/val.zip)
* [test file for leaderboard](downloads/hw5/test.txt)
</div>

Modify the tutorial code to instead read from city names dataset. In the tutorial, you used the same text file for both training and evaluation. We learned in class about how this is not a great idea. For the city names dataset we provide you separate train and validation sets, as well as a test file for the leaderboard. All training should be done on the train set and all validation on the validation set. 

You may need to change parts of [data.py](https://github.com/spro/practical-pytorch/blob/master/char-rnn-classification/data.py) to get this working. Specifically, to handle unicode, you might need to replace calls to `open` with calls to `codecs.open(filename, "r",encoding='utf-8', errors='ignore')`. 

Warning: you'll want to lower the learning rating to 0.02 or less or you might get NaNs when training. 

Attribution: the city names dataset is derived from [Maxmind](http://download.maxmind.com/download/geoip/database/LICENSE_WC.txt)'s dataset.

**Analysing your results**

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

# Text generation using char-rnn

In this section, you will be following more Pytorch tutorial code in order to reproduce Karpathy's text generation results. Follow the tutorial [here](http://pytorch.org/tutorials/intermediate/char_rnn_generation_tutorial.html).

## Experimenting with your own dataset

Be creative! Pick some dataset that interests you. Here are some ideas:

* [ABC music format](https://raw.githubusercontent.com/rdeese/tunearch-corpus/master/all-abcs.txt)
* [Donald Trump speeches](https://github.com/ryanmcdermott/trump-speeches)
* [Webster dictionary](http://www.gutenberg.org/cache/epub/29765/pg29765.txt) 
* [Jane Austen novels](http://www.gutenberg.org/files/31100/31100.txt)

## Analyze your results

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

