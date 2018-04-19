---
layout: default
img: python.jpg
img_link: http://xkcd.com/353/
caption: Hello world!
title: Code Switching
active_tab: homework
term_project: true
---



# Code Switching

With the Internet becoming increasingly accessible, a linguistically diverse population has come online.
It has been observed that such non-English population usually uses its own language written in Roman
script (‘Transliteration’) to generate web content like tweets, blogs, etc. Moreover, these people switch back
and forth between languages mid-sentence, a behaviour termed as ‘Code Switching’. In this homework, you will recognize named-entities in a code-switched document. This is a shared task in ACL’18 [1].

### The Data

The organizers of the shared task have chosen to annotate the following 9 categories:

1. Person
2. Location
3. Organization
4. Product
5. Group
6. Event
7. Time
8. Title
9. Other

They have released 2 datasets for this problem: English-Spanish and Egyptian-Arabic tweets. You
will work on English-Spanish tweets for the purpose of this homework. Guidelines for 9 entity types for English-Spanish tweets are also available on in ACL’18 [2]. For that, there are 50757 annotated tweets as training data and 832 tweets as development data. The data is available at the below links:

[Training data](https://code-switching.github.io/2018/files/spa-eng/train_offset.tsv)  
[Development data](https://code-switching.github.io/2018/files/spa-eng/dev_offset.tsv)

The format of these files is: `<tweet_id> <user_id> <start_offset> <end_offset> <label>`

You can use a python library like `tweeple` to download the actual tweets!

Following is an example of NER in code-switched data:

*My Facebook, Ig & Twitter is hellaa dead y’all are some Gay ass people Jk soy yo que has no
life*

This sample tweet is chosen from the training data. The text is a mix of English and Spanish. Here,
‘Facebook’, ‘Ig’ and ‘Twitter’ are identified as Named Entities (subcategory: Product).

### Evaluation

As in general NER tasks, you will use F1-score to evaluate the performance of your system. The script score.py can be used for evaluation. You can pass the file containing extracted named entities as input, as it will ouput the F-1 score. An example of the extracted named entities is as follows:

    el	O	O
    novio	O	O
    de	O	O
    sarah	B-PER	B-PER
    me	O	O
    trajo	O	O
    strawberry	O	O
    lemonade	O	O
    :o	O	O
    automatic	O	O
    boyfriend	O	O
    points	O	O
    !!	O	O

### Simple baseline

Without much effort, you should be able to get 31% F1-score on the dev-set.

### References

[1] Code switching. https://code-switching.github.io/2018/. [Online; accessed 18-April-2018].

[2] NG-SPA Guideline - NER Shared Task. https://code-switching.github.io/2018/files/spa-eng/README.html. [Online; accessed 18-April-2018].

