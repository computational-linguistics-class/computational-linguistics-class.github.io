---
layout: default
img: python.jpg
img_link: http://xkcd.com/353/
caption: Hello world!
title: Classification of PTSD and Depression From Tweets
active_tab: homework
term_project: true
---

# Classification of PTSD and Depression From Tweets

In spirit of mental health awareness, your task for this assignment is to finish the implementation for an algorithm that helps identify Twitter users as patients of Post Traumatic Stress Disorder (PTSD), depression, or control users, based on a significant sample of tweets from each user. There are three types of tasks to accomplish: 

1. PTSD vs. control
2. depression vs. control
3. PTSD vs. depression

Our baseline trains N-gram langauge models from [Homework 5](http://computational-linguistics-class.org/assignment5.html) - one model for each condition: PTSD, depression and control. Depending on the task of interest, we use two of the three LM's to obtain a confidence score for each user. For task condition A vs. condition B: the output of our code allows for us to rank a given list of users in terms of most confident to have condition A to least confident to have condition A (most confident to have condition B). 

Here are the materials that you should download for this assignment: 

* skeleton python code
* text files for each of the conditions: control_text.txt, depression_text.txt and ptsd_text.txt
* evaluation script
* raw training / dev data for training LMs
* test file for leaderboard

## Part 1: Extract Data Into Training Files

The given training, dev and test data containing user tweets are given in the format of json objects stored in TAR Archive files. You can download the test data, dev data and train data directories. To train the LMs, you must first extract the tweets of each category - PTSD, depression and control - into separate files. We provide you with the code in ```extract_tweets.py```. 

By the end of this section, you should have three text files: ```control_text.txt```, ```depression_text.txt```, and ```ptsd_text.txt```

## Part 2: Training Smoothed Character-Level Language Models and Score Each User

As you remember from Homework 5, the language model helps us "characterize" a body of training text by recording the probability of a letter following a history. For the purposes of achieving a fast runtime, the baseline LM uses an order of 1. This performs sufficiently well, but you are also welcome to train a higher-order model. 

We provide you with the following code in the Python stub file. 

```python
def train_char_lm(fname, order=1, add_k=0.5):
	
	'''
	Trains a language model with smoothing.
	Inputs: 
		fname: Path to a text corpus. 
		order: The length of the n-grams. 
		add_k: k value for add-k smoothing.
	Returns: 
		A dictionary mapping from n-grams of length n to a list of tuples.
    	Each tuple consists of a possible net character and its probability.
	'''

	data = codecs.open(fname, 'r', encoding='utf8', errors='replace').read()
	lm = defaultdict(Counter)
	vocab = set(list(data))
	pad = "~" * order
	data = pad + data
	
	# add OOV term
	vocab.add('<UNK>')

	for i in range(len(data)-order):
		history, char = data[i:i+order], data[i+order]
		lm[history][char]+=1

	for history, chars in lm.items(): 
		lm[history] = {k: v + add_k for k, v in lm[history].items()}
		not_in_v = [v for v in vocab if v not in lm[history]]
		for v in not_in_v:
			lm[history][v] = add_k

	def normalize(counter):
		s = float(sum(counter.values()))
		return [(c,cnt/(s + ((len(vocab) * add_k)))) for c,cnt in counter.items()] 

	outlm = {hist:normalize(chars) for hist, chars in lm.items()}
	
	return outlm 
```


Using the three LMs, you will be generating a confidence value for each user for one of the three tasks. For finding the score of a user with a set of tweets C, with LMs for conditions A and B, we use the following expression from [Coppersmith et al.](http://www.aclweb.org/anthology/W/W15/W15-1204.pdf). For this task, you would need to extract the tweets belonging to a user from the raw data that we have provided. 

![Equation](http://i65.tinypic.com/20zu3w0.pngo)

NOTE: to speed up the runtime, we have chosen to calculate the score for every 10th tweet rather than each individual tweet. 

The goal is to output a file that contains the list of test / dev users sorted by highest to lowest confidence value. The format of the output file should be a list of usernames separated by newline. We have provided you with a script to get the precision for your output : score.py. There are two required parameters: the predicted list, the gold file (gold.txt), and depending on which of the three tasks you are running, you must also specify one or both of the flags ```--depress``` and ```--ptsd```

```
python3 score.py --pred ptsd_cont.txt --gold gold.txt --depress --ptsd
```
Without extensions, the baseline precision you should be able to achieve with the dev data is: 

* Depression v Control: 0.614038
* PTSD v Control: 0.556939
* Depression v PTSD: 0.785940

## Part 3: Implement Extensions

We have provided the following extension ideas, and you must implement at least one of the following, or come up with your own extension idea : 

1. Using your favourite sklearn classifier, train a classifier for each : PTSD, depression and control tweets
2. Clean the raw data further - users could be removed if their tweets were not 75% English, or the tweets could be cleaned of usernames, etc. 
3. Create age - and gender - matched controls for training the language model. 
4. Implement another smoothing method for the language model 

Please explain in the writeup why you chose to implement the extension you did, and what quantitative result you obtained with the extension. 

## Deliverables
Here are the deliverables that you will need to submit:
* Code, written in Python3
* Test data rankings, in three files, one for each task : ```ptsd_cont.txt``` , ```dep_cont.txt``` and ```ptsd_cont.txt```
* A written writeup addressing the following questions, called ```WriteUp.pdf``` 

## Recommended Readings

* [CLPsych 2015 Shared Task: Depression and PTSD on Twitter](http://www.aclweb.org/anthology/W/W15/W15-1204.pdf) -- this is where we got our published baseline!
* [From ADHD to SAD: Analyzing the Language of Mental Health on Twitter through Self-Reported Diagnoses](http://www.aclweb.org/anthology/W/W15/W15-1201.pdf)
* [Quantifying Mental Health Signals in Twitter](https://www.cs.jhu.edu/~mdredze/publications/2014_acl_mental_health.pdf) 
* [Measuring Post Traumatic Stress Disorder in Twitter](https://www.cs.jhu.edu/~mdredze/publications/2014_icwsm_ptsd.pdf)


