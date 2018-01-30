---
layout: default
img: clusters.png
caption: Did you know that matplotlib has an xkcd() function?
img_link: https://matplotlib.org/xkcd/examples/showcase/xkcd.html    
title: Homework 4 - Making Sense of Word Vectors 
active_tab: homework
release_date: 2018-01-31
due_date: 2018-02-07T11:00:00EST
attribution: Stephen Mayhew and Anne Cocos developed this homework assignment for UPenn's CIS 530 class in Spring 2018.
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

Making Sense of Word Vectors <span class="text-muted">: Assignment 4</span>
=============================================================
In this assignment we will play with different vector space representations of words to solve a synonym clustering problem. The problem is illustrated in the following image.

<img src="/assets/img/bug_clusters.jpg" alt="Bug Clusters" style="width: 50%;"/>

In this image, we have a target word "bug", and a list of all synonyms (taken from WordNet). The 4 circles are the 4 senses of "bug." The input to the problem is all the synonyms in a single list, and the task is to separate them correctly. As humans, this is pretty intuitive, but computers aren't that smart. We will use this task to explore different types of word representations.

You can read more about this task in [these](https://www.cis.upenn.edu/~ccb/publications/clustering-paraphrases-by-word-sense.pdf) [papers](https://cs.uwaterloo.ca/~cdimarco/pdf/cs886/Pantel+Lin02.pdf). 

<div class="alert alert-info" markdown="1">
Here are the materials that you should download for this assignment:
* Some python code
* Data
</div>


Clustering with Word Vectors
=================================

We expect that you have read Jurafsky and Martin, chapters [15](https://web.stanford.edu/~jurafsky/slp3/15.pdf) and [16](https://web.stanford.edu/~jurafsky/slp3/16.pdf). Word vectors, also known as word embeddings, can be thought of simply as points in some high-dimensional space. Remember in geometry class when you learned about the Euclidean plane, and 2-dimensional points in that plane? It's not hard to understand distance between those points -- you can even measure it with a ruler. Then you learned about 3-dimensional points, and how to calculate the distance between these. These 3-dimensional points can be thought of as positions in physical space. 

Now, do your best to stop thinking about physical space, and generalize this idea in your mind: you can calculate a distance between 2-dimensional and 3-dimensional points, now imagine a point with 300 dimensions. The dimensions don't necessarily have meaning in the same way as the X,Y, and Z dimensions in physical space, but we can calculate distances all the same. 

This is how we will use word vectors in this assignment: as points in some high-dimensional space, where distances between points are meaningful. The interpretation of distance between word vectors depends entirely on how they were made, but for our purposes, we will consider distance to measure semantic similarity. Word vectors that are close together should have meanings that are similar. 

With this framework, we can see how to solve our synonym clustering problem. Imagine in the image below that each point is a (2-dimensional) word vector. Using the distance between points, we can separate them into 3 clusters. This is our task. 


![kmeans](/assets/img/kmeans.svg)
(Image taken from [Wikipedia](https://en.wikipedia.org/wiki/K-means_clustering))


## Gensim

We will use the [gensim library](https://radimrehurek.com/gensim/index.html) to read and interact with word vectors. In particular, familiarize yourself with the [KeyedVectors documentation](https://radimrehurek.com/gensim/models/keyedvectors.html).


## The Data

The data to be used for this assignment consists of sets of paraphrases corresponding to one of 57 polysemous target words, e.g.

| Target | Paraphrase set |
| ----------- | --------- |
| note.v | comment mark tell observe state notice say remark mention |
| hot.a | raging spicy blistering red-hot live |

(Here the `.v` following the target `note` indicates the part of speech.)

Your objective is to automatically cluster each paraphrase set such that each cluster contains words pertaining to a single *sense*, or meaning, of the target word. Note that a single word from the paraphrase set might belong to one or more clusters.

For evaluation, we take the set of ground truth senses from [WordNet](http://wordnet.princeton.edu).

### Development data

The development data consists of two files -- a words file (the input), and a clusters file (to evaluate your output). The vocab file `dev_words.txt` is formatted such that each line contains one target, its paraphrase set, and the number of ground truth clusters *k*, separated by a `::` symbol:

```
target.pos :: k :: paraphrase1 paraphrase2 paraphrase3 ...
```

You can use *k* as input to your clustering algorithm.

The clusters file `dev_clusters.txt` contains the ground truth clusters for each target word's paraphrase set, split over *k* lines:

```
target.pos :: 1 :: paraphrase2 paraphrase6
target.pos :: 2 :: paraphrase3 paraphrase4 paraphrase5
...
target.pos :: k :: paraphrase1 paraphrase9
```

### Test data

For testing, you will receive only a vocab file containing the test target words and their paraphrase sets. Your job is to create an output file, `test_clusters.txt`, formatted in the same way as `dev_clusters.txt`, containing the clusters produced by your system.

## Evaluation

There are many possible ways to evaluate clustering solutions. For this homework we will rely on the paired F-score, which you can read more about in [this paper](https://www.cs.york.ac.uk/semeval2010_WSI/paper/semevaltask14.pdf).

The general idea behind paired F-score is to treat clustering prediction like a classification problem; given a target word and its paraphrase set, we call a *positive instance* any pair of paraphrases that appear together in a ground-truth cluster. Once we predict a clustering solution for the paraphrase set, we similarly generate the set of word pairs such that both words in the pair appear in the same predicted cluster. We can then evaluate our set of predicted pairs against the ground truth pairs using precision, recall, and F-score.

We have provided an evaluation script that you can use when developing your own system. You can run it as follows:

```
python evaluate.py <GROUND-TRUTH-FILE> <PREDICTED-CLUSTERS-FILE>
```

Your Tasks
======================
You have 3 tasks. 

### 1. Exploration

We have provided a file called `question2.txt` that lists a few initial questions to get you started working with embeddings. We've also copied the initial questions below. Write your answers to each question on the specified line of `question1.txt` to turn in.

- What is the dimensionality of these vectors?
- What are the 5 most similar words to `picnic`?
- Which of these words is not like the others: "
- Solve the following analogy: "leg" is to "jump" as X is to "throw"


### 2. Sparse Representations 

Your first task is to generate clusters for the target words in `test_vocab.txt` based on a feature-based (not dense) vector space representation. In this type of VSM, each dimension of the vector space corresponds to a specific feature, such as a context word (see, for example, the term-context matrix described in [Chapter 15.1.2 of Jurafsky & Martin](https://web.stanford.edu/~jurafsky/slp3/15.pdf)). 

Since it can take a long time to build cooccurrence vectors, we have pre-built a set. You will find them here: `/fill/this/out`. The code is also available in `makecooccurrences.py` if you want to rerun on different data or different parameters.

The corpus we used is here: `/home1/a/acocos/data/reuters.rcv1.tokenized.gz` 

Your task is to fill out: `question1.py`

Here is an example of the K-means code:

{% highlight python %}
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=k).fit(X)
print(kmeans.labels_)
{% endhighlight %}


<!--- Baseline description is a placeholder --->
The baseline system for this section represents words using a term-context matrix `M` of size `|V| x D`, where `|V|` is the size of the vocabulary and D=500. Each feature corresponds to one of the top 500 most-frequent words in the corpus. The value of matrix entry `M[i][j]` gives the number of times the context word represented by column `j` appeared within W=3 words to the left or right of the word represented by row `i` in the corpus. Using this representation, the baseline system clusters each paraphrase set using K-means.  

Implementing the baseline will score you a B, but why not try and see if you can do better? You might try experimenting with different features, for example:
- What if you reduce or increase `D` in the baseline implementation?
- Does it help to change the window `W` used to extract contexts?
- Play around with the feature weighting -- instead of raw counts, would it help to use PMI or TF-IDF?
- Try a different clustering algorithm that's included with the [scikit-learn clustering package](http://scikit-learn.org/stable/modules/clustering.html), or implement your own.
- What if you include additional types of features, like paraphrases in the [Paraphrase Database](http://www.paraphrase.org) or the part-of-speech of context words?

The only feature types that are off-limits are WordNet features.

Turn in the predicted clusters that your VSM generates. Also provide a brief description of your method in a file called `writeup.pdf`, making sure to describe the vector space model you chose, the clustering algorithm you used, and the results of any preliminary experiments you might have run on the training set.

The output file should be called: `test_clusters_features.txt`

### 3. Dense Representations
Finally, we'd like to see if dense word embeddings are better for clustering the words in our test set. Run the word clustering task again, but this time use a dense word representation. 

For this task, use files:
* `/home1/m/mayhew/data/wiki-news-300d-1M.vec.bin`: fasttext word vectors (binary format, 300 dimensions)
* `/home1/m/mayhew/data/GoogleNews-vectors-negative300.bin`: Google word2vec vectors (binary format, 300 dimensions)
* `question3.py`: to load dense vectors and cluster. (this will be similar to `question1.py`)

The baseline system for this section uses the provided word vectors to represent words, and K-means for clustering. 

As before, achieving the baseline score will get you a B, but you might try to see if you can do better. Here are some ideas:
- Train your own word vectors, either on the provided corpus or something you find online. Try experimenting with the dimensionality.
- [Retrofitting](https://www.cs.cmu.edu/~hovy/papers/15HLT-retrofitting-word-vectors.pdf) is a simple way to add additional semantic knowledge to pre-trained vectors. The retrofitting code is available [here](https://github.com/mfaruqui/retrofitting). Experiment with different lexicons, or even try [counter-fitting](http://www.aclweb.org/anthology/N16-1018).

As in question 1, turn in the predicted clusters that your dense vector representation generates. Also provide a brief description of your method in `writeup.pdf` that includes the vectors you used, and any experimental results you have from running your model on the training set. 

In addition, do an analysis of different errors made by each system -- i.e. look at instances that the word-context matrix representation gets wrong and dense gets right, and vice versa, and see if there are any interesting patterns. There is no right answer for this.


The output file should be called: `test_clusters_dense.txt`


## Deliverables 
<div class="alert alert-warning" markdown="1">
Here are the deliverables that you will need to submit:
* question1.txt file with answers to questions from part 2
* simple VSM clustering output `test_clusters_features.txt`
* dense model clustering output `test_clusters_dense.txt`
* writeup.pdf
* code (.zip). It should be written in Python 3.
</div>

## Recommended readings
* Jurafsky and Martin, chapters [15](https://web.stanford.edu/~jurafsky/slp3/15.pdf) and [16](https://web.stanford.edu/~jurafsky/slp3/16.pdf)
* [Implementing Poincaré Embeddings](https://rare-technologies.com/implementing-poincare-embeddings/)
* [Clustering paraphrases by word sense](https://www.cis.upenn.edu/~ccb/publications/clustering-paraphrases-by-word-sense.pdf)
* [Discovering Word Senses from Text](https://cs.uwaterloo.ca/~cdimarco/pdf/cs886/Pantel+Lin02.pdf)
