---
layout: default
img: python.jpg
img_link: http://xkcd.com/353/
caption: Hello world!
title: Puns
active_tab: homework
term_project: true
---


# "Penn There. Done That." - Computational Localization of English Puns


## Overview:

Word sense disambiguation (WSD), the task of identifying a word's meaning in context, has long been recognized as an important task in computational linguistics. Traditional approaches to WSD rest on the assumption that there is a single, unambiguous communicative intention underlying each word in the document. However, there exists a class of language constructs known as _**puns**_, in which lexical-semantic ambiguity is a deliberate effect of the communication act. 
 
A pun is a form of wordplay in which one sign (e.g., a word or phrase) suggests two or more meanings by exploiting polysemy, homonymy, or phonological similarity to another sign, for an intended humorous or rhetorical effect. For example,Danqi Chen the first of
the following two punning jokes exploits the sound similarity between the surface sign *“propane”* and the latent target *“profane”*, while the second exploits contrasting meanings of the word *“interest”*:
 -  When the church bought gas for their annual barbecue, proceeds went from the sacred to the propane.
 -  I used to be a banker but I lost interest.

Puns where the two meanings share the same pronunciation are known as *homophonic* or *perfect*, while those relying on similar- but not identical sounding signs are known as *heterophonic* or *imperfect*. Where the signs are considered as written rather than spoken sequences, a similar distinction can be made between homographic and heterographic puns.

So this problem got featured as one of the shared tasks in the SemEval-2017 which involved 3 subtasks:
* **Pun Detection**
* **Pun Location**
* **Pun Interpretation**

Our assignment is based on subtask 2 which is **Pun Location** where our dataset would only have contexts that contained a pun. For any or all of the contexts, systems had to make a single guess as to which word is the pun. For example, given context (2) above, the system should have indicated that the tenth word, *“interest”*, is the pun.


## Data:

The data for the SemEval Task 7 subtask 2 which is **Pun Location** in the shared task : __*Detection and Interpretation of English Puns*__ is split into 2 parts as follows:  
* *Homographic Puns*: test dataset contains a total of **2250** sentences containing them
* *Heterographic Puns*: test dataset contains a total of **1780** sentences containing them

These datasets are in XML format. We will explore training our predictive model on different corpuses (of your choice) and we will use the same evaluation dataset as given to us in the shared task to compare our model's metrics against the metrics resulted from prior work on the shared task.

Here is an example of a sentence in the dataset containing a heterographic pun:
    
```
  <text id="het_1">
    <word id="het_1_1">'</word>
    <word id="het_1_2">'</word>
    <word id="het_1_3">I</word>
    <word id="het_1_4">'</word>
    <word id="het_1_5">m</word>
    <word id="het_1_6">halfway</word>
    <word id="het_1_7">up</word>
    <word id="het_1_8">a</word>
    <word id="het_1_9">mountain</word>
    <word id="het_1_10">,</word>
    <word id="het_1_11">'</word>
    <word id="het_1_12">'</word>
    <word id="het_1_13">Tom</word>
    <word id="het_1_14">alleged</word>
    <word id="het_1_15">.</word>
  </text> 
```
The results for each phase must be submitted in a delimited text file named answer.txt. Each line consists of two fields separated by horizontal whitespace (a single tab or space character). The first field is the ID of a context from the data set. The second field is the ID of the one word in that context which is a pun. For the above example, the format would be as under:

```
    het_1	het_1_14
```

The data resource for all the subtasks (2 included) can be found [here](http://alt.qcri.org/semeval2017/task7/data/uploads/semeval2017_task7.tar.xz). 


## Evaluation:
The evaluation for the task of interest is done using 4 standard metrics:

* coverage: # of guesses ÷ # of contexts
* precision: # of correct guesses ÷ # of guesses
* recall: # of correct guesses ÷ # of contexts
* F1: ( 2 × precision × recall ) ÷ ( precision + recall )

The higher the metrics, the better our results. 

 Sample data and results files are available
To run the evaluation script, run

```
python3 score.py --goldfile goldfilepath --predfile predfilepath
```

e.g.

```
python3 score.py --goldfile data/homographic.gold --predfile baseline_predictions
Namespace(goldfile='data/homographic.gold', predfile='baseline_predictions')
Performance
Coverage:  1.0  Precision: 0.4704418170504045  Recall:  0.4704418170504045  F-score:  0.4704418170504045
```


## Baselines:
By using simple ideas we can cross the first and a reasonably competitive baseline of **45%** for the homographic puns and the heterographic puns. This is a generous baseline that any thoughtful model should be able to beat. The state of the art on this dataset is about 66% for the homographic puns and close to 80% for the heterographic puns. If you manage to beat that, then look for conference deadlines and start writing, because you can publish it. 

Inspiration for example could be drawn from using language models or metrics which could emphasize the word position.
One approach we thought would be a cool avenue to explore was using PMI values. The intuition is that sentences with puns have a particular word, paired with the pun, that has a higher assoication with the pun.The word pair should have a high enough assoication that allows word play.

Other avenues could involve building your own pun dataset and turning the problem into a supervised one. However, the data would need to be annotated and also one would have to be certain of no overlap between the test dataset and the built training dataset.

## References:
[SemEval Shared Task 7: Detection and Interpretation of English Puns](http://www.aclweb.org/anthology/S17-2005)
