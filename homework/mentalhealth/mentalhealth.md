---
layout: default
img: depression.png
caption: Positive Attitdue 
img_link: https://xkcd.com/828/
title: Homework 9 (Optional) - Classification of Depression
active_tab: homework
release_date: 2019-04-24
due_date: 2019-05-01T11:59:00EST
attribution: This assignment was designed by students in Penn's CIS 530 in the Spring of 2018 with help from with help from Anne Cocos and Reno Kriz.  It is based on the [CLPsych shared task from 2015](https://www.cs.jhu.edu/~mdredze/publications/clpsych15_shared_task.pdf) by Glen Coppersmith, Mark Dredze, Craig Harman, Kristy Hollingshead and Meg Mitchell.
readings:
-
   title: Proceedings of the Fourth Workshop on Computaitonal Linguistics and Clinical Psychology (CLPsych) -- From Linguistic Signal to Clinical Reality
   venue: CLPsych
   type: workshop
   year: 2015
   url: http://www.aclweb.org/anthology/W/W17/W17-31.pdf
   id: clpsych-proceedings
-
   title: CLPsych 2015 Shared Task&colon; Depression and PTSD on Twitter
   authors:  Glen Coppersmith, Mark Dredze, Craig Harman, Kristy Hollingshead, Margaret Mitchell
   venue: CLPsych
   type: workshop
   year: 2015
   url: http://www.aclweb.org/anthology/W/W15/W15-1204.pdf
   id: clspych-shared-task
-
   title: From ADHD to SAD&colon; Analyzing the Language of Mental Health on Twitter through Self-Reported Diagnoses
   authors:  Glen Coppersmith, Mark Dredze, Craig Harman, Kristy Hollingshead
   venue: CLPsych
   type: workshop
   year: 2015
   url: http://www.aclweb.org/anthology/W/W15/W15-1201.pdf
   id: adhd-to-sad
-
   title: Quantifying Mental Health Signals in Twitter
   authors: Glen Coppersmith, Mark Dredze, Craig Harman
   venue: CLPsych
   type: workshop
   year: 2014
   url: https://www.cs.jhu.edu/~mdredze/publications/2014_acl_mental_health.pdf
   id: quantifying-mental-health-on-twitter
-
   title: Measuring Post Traumatic Stress Disorder in Twitter
   authors: Glen Coppersmith, Craig Harman, Mark Dredze
   venue: ICWSM
   type: workshop
   year: 2014
   url: https://www.cs.jhu.edu/~mdredze/publications/2014_icwsm_ptsd.pdf
   id: measuring-ptsd-on-twitter
---


# Classification of PTSD and Depression From Tweets

The costs of mental and neurological health problems in the United States are staggering, estimated at over $760 billion per year. One in five people in the U.S. experience a mental health problem in a given year, and mental health and substance abuse disorders are some of the leasing causes of disability worldwide [1]. 

Language plays an important role in diagnosing many mental and neurological health problems. This is where we come in. Our aim is to find out whether we can reliably identify people with mental health issues (clinical depression and Post-Traumantic Stress Disorder (PTSD)) based on their Twitter activity. If so, this technology could lead to inexpensive screening measures to be employed by healthcare professionals.


<div class="alert alert-info" markdown="1">
Here are the materials that you should download for this assignment:

 - [Skeleton code and directory structure](clpsych.zip)
</div>

<div class="alert alert-danger" markdown="1">
**Important Note about Data** 

This homework assignment involves sensitive mental health data. Therefore in order to obtain the dataset, you will need to complete CITI Human Subjects Training (~30 mins) and sign a release form. To do so, please following the following steps:

1. Complete [CITI Training for Human Research](https://irb.upenn.edu/mission-institutional-review-board-irb/guidance/citi-training) with the Learner Group set as "Students -- Class Projects." This should take roughly 30 minutes.
2. Read and sign this [Data Use and Confidentiality Agreement](CLPsych_data_privacy_agreement.pdf)
3. Put your CITI Completion Report and a PDF of your signed data agreement [into this Google folder](https://drive.google.com/drive/folders/1AGasGuY_401pwgY2DrIlD39wbNFH33T6?usp=sharing).
4. [Fill out this form](https://docs.google.com/forms/d/e/1FAIpQLSdRhkoY-gkspJNweeu7c-w-jJqoEgEADqOEZsr0n2s3rgyMfA/viewform?usp=sf_link) when you are done.

If you're working in pairs, both partners need to follow the above steps.

The instructor will then send you the data.
</div>

## The Task

### Task Basics

Our goal is this: Given a set of a person's tweets (and their associated metadata), predict whether that person suffers from `depression`, `PTSD`, or neither of these (`control`). Specifically, we will create three models -- one for each pairwise distinction:

1. `PTSD` vs. `control`
2. `depression` vs. `control`
3. `PTSD` vs. `depression`

### Evaluation

Each model takes as input a pair of conditions to distinguish between (we'll refer to them as `conditionPOS` and `conditionNEG`), and a list of people actually having either `conditionPOS` or `conditionNEG`. The model should re-rank the list of people such that those most likely to have `conditionPOS` are at the top, and those most likely to have `conditionNEG` are at the bottom. 

The evaluation metric we will use is called *average precision*:

$$AP = \frac{1}{|R|} \cdot \sum_{i=1}^n prec(i) \cdot relevance(i)$$

where $$R$$ is the set of relevant people (i.e. people belonging to `conditionPOS`), $$n$$ is the total number of people being ranked, $$prec(i)$$ gives the precision at the $$i$$-th person, and $$relevance(i)$$ is an indicator variable denoting whether the person ranked at position $$i$$ belongs to `conditionPOS`. For example, imagine there are 5 ranked people with conditions as follows:

```
conditionPOS
conditionNEG
conditionPOS
conditionNEG
conditionPOS
```
i.e. the `conditionPOS` people have been ranked at positions 1, 3, and 5. The average precision, then, would be:

$$(1/3) \cdot ((1 \cdot 1) + (\frac{1}{2} \cdot 0) + (\frac{2}{3} \cdot 1) + (\frac{2}{4} \cdot 0) + (\frac{3}{5} \cdot 1)) = 0.756$$


## The Data 

The dataset consists of a meta file and train and test directories. The meta file is a `.csv` with information about each user, including an (anonymized) twitter handle, age, gender, tweet count, and experimental condition (`ptsd`, `depression`, or `control`). Each user also has an assigned chunk index, which refers to the location of that user's data in the train or test directory.

The tweets themselves are contained in the train and test directories. Each directory contains numbered chunks of tweets, with each chunk having tweets from a list of users. Within the test directory, we have partitioned the test data into a dev and test set, with the dev set consisting of chunks 60-65 and test data in chunks 66-89.

We have provided a simple interface for you to access the data in `util.py`:

{% highlight python %}
>>> import util
>>> traindata = util.load_data('train')
>>> devdata = util.load_data('dev')
>>> testdata = util.load_data('test')
{% endhighlight %}

The above function returns a list with a tuple pertaining to each user, consisting of the user's anonymized handle, metadata, and bytestring of tweets in JSON format. Here's an example for a user with just a single tweet:

{% highlight python %}
>>> print(traindata[26])
('b2WSKSO_G', 
 {'age': '23.25827563', 'num_tweets': '1', 'gender': 'F', 'condition': 'depression'}, 
  b'{"truncated": false, "text": "RT @nk3emnE_v: http://t.co/MAPN5ZWNUO #AustinMahoneTour #TheSecret http://t.co/VDOnovhEVw", "in_reply_to_status_id": null, "id": 5274362989788256320, "favorite_count": 0, "retweeted": false, "entities": {"symbols": [], "user_mentions": [{"indices": [3, 13], "screen_name": "nk3emnE_v", "id": 1826430017237194737, "name": "", "id_str": "1826430017237194737"}], "hashtags": [{"indices": [38, 55], "text": "AustinMahoneTour"}, {"indices": [56, 66], "text": "TheSecret"}], "urls": [{"url": "http://t.co/MAPN5ZWNUO", "indices": [15, 37], "expanded_url": "http://austinmahone.com/cUrp4uO6ffZn2X1QcKYoK78W2hl", "display_url": "austinmahone.com/cUrp4uO6ffZn2X1QcKYoK78W2hl"}, {"url": "http://t.co/VDOnovhEVw", "indices": [67, 89], "expanded_url": "http://sot.ag/v:Xal", "display_url": "sot.ag/v:Xal"}]}, "in_reply_to_screen_name": null, "id_str": "5274362989788256320", "retweet_count": 2046, "in_reply_to_user_id": null, "retweeted_status": {"truncated": false, "text": "http://t.co/MAPN5ZWNUO #AustinMahoneTour #TheSecret http://t.co/VDOnovhEVw", "in_reply_to_status_id": null, "id": 7633155867008109733, "favorite_count": 7, "retweeted": false, "entities": {"symbols": [], "user_mentions": [], "hashtags": [{"indices": [23, 40], "text": "AustinMahoneTour"}, {"indices": [41, 51], "text": "TheSecret"}], "urls": [{"url": "http://t.co/MAPN5ZWNUO", "indices": [0, 22], "expanded_url": "http://austinmahone.com/cUrp4uO6ffZn2X1QcKYoK78W2hl", "display_url": "austinmahone.com/cUrp4uO6ffZn2X1QcKYoK78W2hl"}, {"url": "http://t.co/VDOnovhEVw", "indices": [52, 74], "expanded_url": "http://sot.ag/v:Xal", "display_url": "sot.ag/v:Xal"}]}, "in_reply_to_screen_name": null, "id_str": "7633155867008109733", "retweet_count": 2046, "in_reply_to_user_id": null, "user": {"verified": false, "geo_enabled": false, "followers_count": 33417, "lang": "en", "utc_offset": 3600, "statuses_count": 93608, "friends_count": 17658, "screen_name": "nk3emnE_v", "favourites_count": 12840, "url": null, "created_at": "Fri Jul 06 13:04:22 +0000 2012", "time_zone": "Sarajevo", "listed_count": 209}, "geo": null, "in_reply_to_user_id_str": null, "possibly_sensitive": true, "lang": "und", "created_at": "Sun Apr 13 08:54:28 +0000 2014", "in_reply_to_status_id_str": null, "place": null}, "screen_name_statistics": {"has_underscore": false, "contains_swear": false, "has_digits": false, "contains_mental_health_condition": false, "has_chars": true}, "user": {"verified": false, "geo_enabled": false, "followers_count": 0, "lang": "fr", "utc_offset": null, "statuses_count": 1, "friends_count": 19, "screen_name": "b2WSKSO_G", "favourites_count": 0, "url": null, "created_at": "Sun Mar 30 21:53:58 +0000 2014", "time_zone": null, "listed_count": 0}, "geo": null, "in_reply_to_user_id_str": null, "possibly_sensitive": false, "lang": "und", "created_at": "Sun Apr 13 09:20:14 +0000 2014", "in_reply_to_status_id_str": null, "place": null}\n'
)
{% endhighlight %}
You can access a particular element of tweets for a given user using the helper function `util.get_tweets_element`. For example, to extract the text of each tweet from the same user, run:

{% highlight python %}
>>> tweettext = util.get_tweets_element(train[26][-1], elem='text')
>>> print(tweettext[0])
RT @nk3emnE_v: http://t.co/MAPN5ZWNUO #AustinMahoneTour #TheSecret http://t.co/VDOnovhEVw
{% endhighlight %}

## Part 0: Evaluation Script

For this homework, we'd like you to write your own evaluation script. We've provided starter code in `eval.py`. Your task is to implement the Average Precision metric described above.

In order to validate that your implementation is correct, we provide a sample output file (`output/random/dev_ptsd_control.txt`) with `PTSD` and `control` users from the dev set in random order. Running the following command: 

```
python3 eval.py ptsd control ../output/random/dev_ptsd_control.txt
```
should get you a score of 0.3758. 

## Part 1: The Baseline

Our baseline follows the approach proposed by Coppersmith et al. [2]. We will utilize an character-level language model like those we implemented in [Homework 5](http://computational-linguistics-class.org/assignment5.html). We will build one language model for each condition: `PTSD`, `depression`, and `control`. Depending on the distinction we are trying to model (e.g. `conditionPOS` vs `conditionNEG`), we use two of the three language models to obtain a confidence score for each user. 

For task `conditionPOS` vs `conditionNEG`: the output of the code will rank a given list of users in terms of most confident to have `conditionPOS` to least confident to have `conditionPOS` (i.e. most confident to have `conditionNEG`). 

### Part 1A: Extract Data Into Training Files

Once you have downloaded the data, the first step is to create a training corpus corresponding to each condition. Each corpus should contain all tweets from persons in the training set having the indicated condition. 

We have provided a script to do enable you to do this:

```
python3 generate_lm_training_text.py
```

By the end of this section, you should have three text files: ```control_text.txt```, ```depression_text.txt```, and ```ptsd_text.txt``` located in `data/lm-training-text`.

### Part 1B: Train Smoothed Character-Level Language Models

As you probably remember from Homework 5, the language model helps us "characterize" a body of training text by recording the probability of a letter following a history. For the purposes of achieving a fast runtime, the baseline LM uses an order of 1. This performs sufficiently well, but you are also welcome to train a higher-order model. 

Since you've already built a smoothed character-level language model in the past, we're providing you with the code in `train_lm.py`.

Your task is to use the language model script `train_lm.py` to generate language models for each of the three target conditions. Write the three models to a location where you can access them later.

### Part 1C: Predict Subjects' Condition using Language Models

Given language models for `conditionPOS` and `conditionNEG`, along with a set of a person's tweets, our goal is now to score that person based on how much more their tweet text aligns with the LM for `conditionPOS` as opposed to the LM for `conditionNEG`. To do this we will use a method proposed from [Coppersmith et al.](http://www.aclweb.org/anthology/W/W15/W15-1204.pdf):

$$\frac{\sum_C \text{log}p(c_{POS}) - \text{log}p(c_{NEG})}{|C|}$$

where $$C$$ is the list of characters in a tweet, and $$\text{log}p(c_{X})$$ gives the log probability of the tweet under language model $$X$$.

NOTE: to speed up the runtime, our baseline implementation calculates each user's score based on every 10th tweet and takes the median. 

Your task is to complete the code skeleton for the function `score_subjects` provided in `predict_lm.py`. Once you're finished, you will have a script that you can call in the following manner to produce a ranked list of users in the selected dataset, given language model files produced by `train_lm.py`:

```
python3 predict_lm.py <SPLIT> <CONDITION_POS_MODEL> <CONDITION_NEG_MODEL> <OUTFILE>
```

Use this script to create outputs for the dev and test sets for the following expriments:

(`conditionPOS` vs `conditionNEG`)

1. `ptsd` vs. `control`
2. `depression` vs. `control`
3. `ptsd` vs. `depression`

Without extensions, the baseline average precision you should be able to achieve with the dev data is: 

* Depression v Control: 0.581
* PTSD v Control: 0.569
* Depression v PTSD: 0.767

## Implement Extensions 

Now that you have met the baseline scores, it's time to build a better model. Use the skeleton provided in `predict_ext.py` to implement your extended model. 

Some ideas for how you might improve on the existing language model implementation include:

1. Using your favourite sklearn classifier, train a classifier for each : PTSD, depression and control tweets
2. Clean the raw data further - users could be removed if their tweets were not 75% English, or the tweets could be cleaned of usernames, etc. 
3. Implement another smoothing method for the language model 

Please explain in the writeup why you chose to implement the extension you did, and what quantitative result you obtained with the extension. 

## Deliverables 

Here are the deliverables that you will need to submit:

* Code, written in Python3
* Test data rankings, in three files, one for each task : `ptsd` vs. `control`, `depression` vs. `control`, and `ptsd` vs. `depression`. These should be produced using your best extended model.
* A `README.md` file that explains how to run your extended model
* A writeup called `writeup.pdf` that details:
  * A description of your extended model
  * Your extended model's scores on the dev and test sets
  * Any other experiments you tried



## Recommended readings

<table>
   {% for publication in page.readings %}
    <tr>
      <td>
	{% if publication.url %}
		<a href="{{ publication.url }}">{{ publication.title }}</a>
        {% else %}
		{{ publication.title }}
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
