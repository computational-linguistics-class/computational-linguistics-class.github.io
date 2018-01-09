---
layout: default
img: python
img_link: http://xkcd.com/353/
caption: Hello world!
title: Homework 1 "Python and Bash Skills"
active_tab: homework
release_date: 2018-01-10
due_date: 2018-01-17 11:00:00EST
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
This assignment is due on {{ page.due_date | date: "%A, %B %-d, %Y" }}. 
</div>

<div class="alert alert-info" markdown="span">
Links to tutorials and other Python resources are posted on the [resources page](resources.html).</div>


Python and Bash Skills <span class="text-muted">: Assignment 1</span> 
=============================================================
This week we will start writing some code! We will be using Python for most of this course, and this assignment examines your skills writing regular expressions, control flows, and string processing in Python. Being able to process files from the command line will also be incredibly useful for your life as a computational linguiust, and we ask you to implement several operations in Bash. 

You will submit your assignment via Gradescope. We'll post instructions on Piazza. 

## 1. Bash Skills
For this class, we expect you to have access to a Unix command line. If you have a Mac, you can open up the `Terminal` app. If you are on Windows, please install [PuTTY](http://www.putty.org/) or its more modern, easier-to-use cousin, [MobaXterm](https://mobaxterm.mobatek.net/), and follow the instructions [here](https://www.seas.upenn.edu/cets/answers/remote.html).

The term `bash` refers to both the program (or shell)--run by the terminal--that you type your commands into, and the programming language you use to write those commands. There exist other shells, such as `zsh` or `fish`, but we will stick to `bash`. When you type commands into the shell, we refer to these as bash commands. When you write a file with a long sequence of these command, we call that a bash program.

In order to learn bash, we've picked 3 hopefully useful commands for you to implement. When you've finished getting your solutions working on the command line, open up `bash_questions.py` and copy them into the appriorate places for submission. *You will need to modify your commands slightly to use the Python function arguments.*

### 1.1. Creating a Vocabulary
For this question, you are allowed to use `sed`, `tr`, `sort`, `uniq`, and `awk`.

A vocabulary file contains a list of all of the words in a text document along with a count of the number of occurences of each  word.

Given a text file, output a list of the words present, tab-separated by their frequency. The words should be ordered from most frquent to least frequent. You can assume all words are space-separated.

For example, the input file:
```
Seven lazy researchers like using bash.
The researchers like, like Python too.
```

Should output
```
like		2
researchers		2
bash.		1
lazy		1
like,		1
Python		1
Seven		1
The		1
too.		1
using		1
```

### 1.2. Printing Lines with Results
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
2
Accuracy: 44.34
Accuracy: 45.34
```

### 1.3 Extracting Accuracies
Frequently, when dealing with large sets of experiments, you want
to summarize a bunch of semi-structured results text files quickly.
 
 In this exercise, you'll use bash to take results of the form found 
 in `accuracies.txt` and pull out the accuracies as well as the name
 of the experiment.

For example, the line
```
Base accuracy: 0.3267522959523133 time: .4555
```

should be transformed to the line

```
Base 0.3267522959523133
```

## 3. Python Skills

All your answers should be added to `python_questions.py`. Do not include any important statement other than the ones already there.

### 3.1 File I/O
You can open, read, and write files using the aptly-named open(), read(), and write() commands. read() returns the entire contents of the file as a string. readlines() will split on the newline character and return the lines as a list, which is generally nicer for allowing you to iterate line-by-line. I won't go through an example here, but I highly recommend playing with the [csv module](https://docs.python.org/2/library/csv.html), which is incredibly useful and we will likely use regularly throughout the semester. 

{% highlight python %}
>>> file = open('test.txt', 'w')
>>> for s in ['line1', 'line2', 'line3', 'line4'] : 
...     file.write(s+'\n')
... 
>>> file.close()
>>> contents = open('test.txt').read()
>>> contents
'line1\nline2\nline3\nline4\n'
>>> contents = open('test.txt').readlines()
>>> contents
['line1\n', 'line2\n', 'line3\n', 'line4\n']
{% endhighlight %}

No need to submit anything for this question, but you should make sure you are familiar with Python file I/O.

### 3.2 Text processing in Python

For this part, you will need to submit your code to answer the following questions. You should download the [iPython notebook](assignments/downloads/python-bootcamp/IPythonBootcamp.ipynb) file, and do all of your work there. You can submit your entire notebook at the end of the assignment.
 
We will be playing with a small but oh so wonderful data set of wine reviews! You can download the data [here](assignments/downloads/python-bootcamp/data.tgz). You can unpack it as follows, and should see two files:


{% highlight tcsh %}
$ tar -xzvf data.tgz 
x data/
x data/stopwords.txt
x data/wine.txt
$ ls data
stopwords.txt	wine.txt
{% endhighlight %}

wine.txt is in the format of one review per line, followed but a star rating between 1 and 5 (except for 3 reviews, where the review decided to go rogue and give 6 stars. Pft.) The text of the review and the star rating are separated by a single tab character. There is also a file called stopwords.txt. You will use this in question 6.

Write a python script that answers each of the following questions and prints the answer to standard output. Since this is a tutorial, there are no secrets: your script should produce [this output](assignments/downloads/python-bootcamp/bootcamp-key.txt) when you are done. I will compare the output of your script directly to this answer key, so start early and come ask for help if you get stuck! I highly recommend looking into the functions available in the [python string module](https://docs.python.org/2/library/string.html).

1. What is the distribution over star ratings?
2. What are the 10 most common words used across all of the reviews, and how many times is each used?
3. How many times does the word 'a' appear?
4. How many times does the word 'fruit' appear?
5. How many times does the word 'mineral' appear?
6. Common words (like 'a') are not as interesting as uncommon words (like 'mineral'). In natural language processing, we call these common words "stop words" and often remove them before we process text. stopwords.txt gives you a list of some very common words. Remove these stopwords from your reviews. Also, try converting all the words to lower case (since we probably don't want to count 'fruit' and 'Fruit' as two different words). Now what are the 10 most common words across all of the reviews, and how many times is each used?
7. You should continue to use the preprocessed reviews for the following questions (lower-cased, no stopwords).  What are the 10 most used words among the 5 star reviews, and how many times is each used? 
8. What are the 10 most used words among the 1 star reviews, and how many times is each used? 
9. Gather two sets of reviews: 1) Those that use the word "red" and 2) those that use the word "white". What are the 10 most frequent words in the "red" reviews which do NOT appear in the "white" reviews?
10. What are the 10 most frequent words in the "white" reviews which do NOT appear in the "red" reviews?

Thats it! Again, you can compare your answers against [our key](assignments/downloads/python-bootcamp/bootcamp-key.txt) to see if you have done things correctly. 

Your code is due <b>{{ page.due_date | date: "%A, %B %-d, %Y" }}</b>. Please submit your entire iPython notebook via [turnin](https://alliance.seas.upenn.edu/~cis520/wiki/index.php?n=Resources.HomeworkSubmission) from the eniac machines. 


<div class="panel panel-danger">
<div class="panel-heading" markdown="1">
#### Grading Rubric
</div>
<div class="panel-body" markdown="1">

This assignment is worth 1 point toward your overall grade in the course.  It counts toward the participation component of your grade. The rubric for the assignment is given below.

* 1 point - if you completed the assignment in class and submitted it by the end of the day.
</div>
</div>

### Bonus! Bash bootcamp.

Knowing more than one scripting language increases your productivity 1 zillion fold (proven fact). If you breezed through the python bootcamp and are sitting and twiddling your thumbs, try brushing up your bash programming skills by doing the following questions using the same wine.txt file. Many of them are the same or similar to what you just did in python. Think about how these operations are conceptually different when you write in bash compared to python. Check out this [cheat sheet](http://crowdsourcing-class.org/bash-commands.html) of bash commands to get you started.

1. How many lines are there in the file?
2. What is the distribution over star ratings?
3. How many reviews contain the word 'a'?
4. How many reviews contain the word 'fruit'?
5. How many reviews contain the word 'mineral'?
6. Make a new file containing the full text of all the reviews, with one word per line. (You don't have to do this in python, but I think that is the easiest way. If you want to try a new command-line tool, check out [sed](http://stackoverflow.com/questions/1853009/replace-all-whitespace-with-a-line-break-paragraph-mark-to-make-a-word-list)). 
7. How many total words appear in your list?
8. How many unique words appear in your list?
9. What are the 10 most common words used across all of the reviews, and how many times is each used?
10. How many times does the word "red" appear? (Be careful of capitalization!)
