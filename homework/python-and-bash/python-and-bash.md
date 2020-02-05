---
layout: default
img: python.jpg
img_link: http://xkcd.com/353/
caption: Hello world!
title: Homework 1 "Python and Bash Skills"
active_tab: homework
release_date: 2020-01-15
due_date: 2020-01-22 23:59:00EST
attribution: This assignment was developed by the CIS 521 staff at the University of Pennsylvania 
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
This assignment is due on {{ page.due_date | date: "%A, %B %-d, %Y" }} before {{ page.due_date | date: "%I:%M%p" }}. 
</div>


<div class="alert alert-danger">
Most homework assignments in this class can be done with a partner, but this one should be done on your own. 
</div>



<div class="alert alert-info" markdown="span">
Links to tutorials and other Python resources are posted on the [resources page](resources.html).</div>


Python and Bash Skills <span class="text-muted">: Assignment 1</span> 
=============================================================
This week we will start writing some code! We will be using Python for most of this course, and this assignment examines your skills 
writing regular expressions, control flows, and string processing in Python. Being able to process files from the command line will
also be incredibly useful for your life as a computational linguist, and we ask you to implement several operations in Bash. 

You will submit your assignment via Gradescope. We'll post instructions on Piazza. 

## 1. Bash Skills
For this class, we expect you to have access to a Unix command line. If you have a Mac, you can open up the `Terminal` app. If you are 
on Windows, please install [PuTTY](http://www.putty.org/) or its more modern, easier-to-use cousin, [MobaXterm](https://mobaxterm.mobatek.net/),
and follow the instructions [here](https://www.seas.upenn.edu/cets/answers/remote.html).

The term `bash` refers to both the program (or shell)--run by the terminal--that you type your commands into, and the programming 
language you use to write those commands. There exist other shells, such as `zsh` or `fish`, but we will stick to `bash`. When you type 
commands into the shell, we refer to these as bash commands. When you write a file with a long sequence of these command, we call that a bash program.

In order to learn bash, we've picked 3 commands for you to implement, each of which we've found useful in our research.
These questions might be tricky; you should take advantage of Piazza and TA office hours for guidance.
Our [basic](tutorials/2017-03-06-bash-for-nlp-tutorial-basic.md), and [advanced](tutorials/2017-03-07-bash-for-nlp-tutorial-topics.md) bash tutorials may be of particular use.

When you've finished getting your solutions
working on the command line, use the template files `bash_q1.sh`, `bash_q2.sh`, and `bash_q3.sh` which can be downloaded [here](bash.zip), 
and write your solution in the file.

In each bash template, you'll notice the variable `$1`.
This refers to the index-1 argument in the command used to invoke the bash script.
For example, to test `bash_q1.sh`, you may run

        ./bash_q1.sh PATH_TO_FILE

Within `bash_q1.sh`, the variable `$1` refers to `PATH_TO_FILE`.

### 1.1. Creating a Vocabulary
This question corresponds to `bash_q1.sh`.
For this question, you are allowed to use `sed`, `tr`, `sort`, `uniq`, and `awk`.

A vocabulary file contains a list of all of the words in a text document along with a count of the number of occurences of each word.

Given a text file, output a list of the words present, tab-separated by their frequency. The words should be ordered from least
frquent to most frequent. You can assume all words are space-separated.

For example, the input file:
```
Seven lazy researchers like using bash.
The researchers like, like Python too.
```

Should output
```
bash.  1
lazy 1
like,  1
Python 1
Seven  1
The  1
too. 1
using  1
like 2
researchers  2
```

### 1.2. Printing Lines with Results
This question corresponds to `bash_q2.sh`.
For this question, you're allowed to use `ls`, if statements, for statements, `grep`, and `echo`.

Check for a file named `results.txt` in each directory within a specified directory.
For each existing `results.txt`, print the directory name and then
only all lines from the corresponding `results.txt` that contain
the following substring:
```
Accuracy:
```

For example, the directory structure
```
root_directory/
    1/
        results.txt
    2/
    3/
        results.txt
```

may output:

```
1
Accuracy: 54.44
Accuracy: 52.23
3
Accuracy: 44.34
Accuracy: 45.34
```

### 1.3 Extracting Accuracies
This question corresponds to `bash_q3.sh`.
Frequently, when dealing with large sets of experiments, you want
to summarize a bunch of semi-structured results text files quickly.
 
 In this exercise, you'll use bash to take results of the form below
 in the file at path `$1` and pull out the accuracies as well as the name
 of the experiment.

For example, the lines
```
Base accuracy: 0.3267522959523133 time: .4555
Augment accuracy: 0.34124123125 time: .785 steps 5
```

should be transformed to the lines

```
Base 0.3267522959523133
Augment 0.34124123125 
```

_Note: The bash template you downloaded may ask you to average the lines. Don't do that; follow the example above._

## 2. Python Skills

All your answers should be added to `python_questions.py`, which can be downloaded [here](python_questions.py).
If you'd like to include any import statements other than the ones already provided, post on Piazza for permission first.

### 2.1. File I/O
You can open, read, and write files using the aptly-named open(), read(), and write() commands. read() returns the entire contents of
the file as a string. readlines() will split on the newline character and return the lines as a list, which is generally nicer for 
allowing you to iterate line-by-line. I won't go through an example here, but I highly recommend playing with the
[csv module](https://docs.python.org/3/library/csv.html), which is incredibly useful and we will likely use regularly throughout
the semester. 

Writing a file:
{% highlight python %}
>>> file = open('test.txt', 'w')
>>> for s in ['line1', 'line2', 'line3', 'line4'] : 
>>>     file.write(s+'\n')
>>> file.close()
{% endhighlight %}

Reading an entire file (if a file is too large to fit easily into memory, you should avoid this);
``` python
>>> with open('test.txt') as f:
>>>    contents = f.read()
>>> contents
'line1\nline2\nline3\nline4\n'
```

Or alternately:
{% highlight python %}
>>> with open('test.txt') as f:
>>>     contents = f.readlines()
>>> contents
['line1\n', 'line2\n', 'line3\n', 'line4\n']
{% endhighlight %}

Reading a file line-by-line without loading it entirely into memory:
``` python
>>> contents = ''
>>> with open('test.txt') as f:
>>>     for line in f:
>>>         contents += line
>>> contents
'line1\nline2\nline3\nline4\n'
```
No need to submit anything for this question, but you should make sure you are familiar with Python file I/O.

### 2.2. Regular Expressions
Regular expressions are a powerful way to process text by describing text patterns. If you are new to regular expressions,
[Chapter 2](https://web.stanford.edu/~jurafsky/slp3/2.pdf) in the course textbook has a good introduction.

In `python_questions.py`, fill in the functions `check_for_foo_or_bar` and  `replace_rgb`
according to their function docstrings. Use the builtin Python regular expressions library, whose documentation is found
[here](https://docs.python.org/3.4/library/re.html).

You may want to write yourself test cases to make sure you're covering all edgecases.
See the [unittest](https://docs.python.org/3.4/library/unittest.html) documentation.

I also highly recommend testing out your expressions using [this](https://regex101.com/) fancy GUI tool.

### 2.3 Edit Distance
To compute the similarity between two strings of text, linguists often use a metric called edit distance. Edit distance measures how 
similar two strings are based on the number of insertions, deletions, and substitutions necessary to turn one of the strings into the 
other.

Use dynamic programming to implement edit distance. [Chapter 2](https://web.stanford.edu/~jurafsky/slp3/2.pdf) in the textbook provides 
pseudocode that you can follow.

Write your solution in the `edit_distance` function in `python_questions.py`.

### 2.4. Text processing in Python

For this part, you will need to submit your code to answer the following questions. 
 
We will be playing with a small but oh so wonderful data set of wine reviews! You can download the data [here](data.tgz). You can down it and unpack it as follows, and should see two files:

{% highlight tcsh %}
$ wget http://computational-linguistics-class.org/homework/python-and-bash/data.tgz
$ tar -xzvf data.tgz 
x data/
x data/stopwords.txt
x data/wine.txt
$ ls data
stopwords.txt	wine.txt
{% endhighlight %}

`wine.txt` is in the format of one review per line, followed but a star rating between 1 and 5 (except for 3 reviews, where the review 
decided to go rogue and give 6 stars. Pft.) The text of the review and the star rating are separated by a single tab character. There is also a file called `stopwords.txt`, which you will use for question 6.

In the `wine_text_processing` function in `python_questions.py`, write code that answers each of the following questions and prints the
answer to standard output, followed by a newline. Since this question is meant as a tutorial, there are no secrets: your script should produce
[this output](key.txt) when you are done. If you get this output it's very likely your code works correctly, but we will ultimately be running your code on a different input file,
so start early and come ask for help if you get stuck!
For questions where there are ties, please break the tie alphabetically (e.g. apple would come before banana).
I highly recommend looking into the functions available in the
[python string module](https://docs.python.org/3/library/string.html).

1. What is the distribution over star ratings?
2. What are the 10 most common words used across all of the reviews, and how many times is each used?
3. How many times does the word 'a' appear?
4. How many times does the word 'fruit' appear?
5. How many times does the word 'mineral' appear?
6. Common words (like 'a') are not as interesting as uncommon words (like 'mineral'). In natural language processing, we call these 
common words "stop words" and often remove them before we process text. stopwords.txt gives you a list of some very common words. Remove 
these stopwords from your reviews. Also, try converting all the words to lower case (since we probably don't want to count 'fruit' and 
'Fruit' as two different words). Now what are the 10 most common words across all of the reviews, and how many times is each used?
7. You should continue to use the preprocessed reviews for the following questions (lower-cased, no stopwords).  What are the 10 most used words among the 5 star reviews, and how many times is each used? 
8. What are the 10 most used words among the 1 star reviews, and how many times is each used? 
9. Gather two sets of reviews: 1) Those that use the word "red" and 2) those that use the word "white". What are the 10 most frequent words in the "red" reviews which do NOT appear in the "white" reviews?
10. What are the 10 most frequent words in the "white" reviews which do NOT appear in the "red" reviews?

Thats it! Again, you can compare your answers against [our key](key.txt) to see if you have done things correctly. 

Your code is due <b>{{ page.due_date | date: "%A, %B %-d, %Y" }}</b>. Please submit the 3 bash files and the 1 Python file using Gradescope.


