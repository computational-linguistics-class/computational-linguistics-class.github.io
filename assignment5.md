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
* [training set](downloads/hw5/train.zip)
* [validation set](downloads/hw5/val.zip)
* [test file for leaderboard](downloads/hw5/test.txt)
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
