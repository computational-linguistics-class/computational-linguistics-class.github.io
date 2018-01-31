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

In this image, we have a target word "bug", and a list of some synonyms. The 4 circles are the 4 senses of "bug." The input to the problem is all the synonyms in a single list, and the task is to separate them correctly. As humans, this is pretty intuitive, but computers aren't that smart. We will use this task to explore different types of word representations.

You can read more about this task in [these](https://www.cis.upenn.edu/~ccb/publications/clustering-paraphrases-by-word-sense.pdf) [papers](https://cs.uwaterloo.ca/~cdimarco/pdf/cs886/Pantel+Lin02.pdf). 

<div class="alert alert-info" markdown="1">
Here are the materials that you should download for this assignment:
* [`data.zip`](downloads/hw4/data.zip) Contains all the data
* [`vectorcluster.py`](downloads/hw4/vectorcluster.py) Main code stub
* [`evaluate.py`](downloads/hw4/evaluate.py) Evaluation script
* [`makecooccurrences.py`](downloads/hw4/makecooccurrences.py) Script to make cooccurrences (optional use) 
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

The data to be used for this assignment consists of sets of paraphrases corresponding to one of 56 polysemous target words, e.g.

| Target | Paraphrase set |
| ----------- | --------- |
| note.v | comment mark tell observe state notice say remark mention |
| hot.a | raging spicy blistering red-hot live |

(Here the `.v` following the target `note` indicates the part of speech.)

Your objective is to automatically cluster each paraphrase set such that each cluster contains words pertaining to a single *sense*, or meaning, of the target word. Note that a single word from the paraphrase set might belong to one or more clusters.

For evaluation, we take the set of ground truth senses from [WordNet](http://wordnet.princeton.edu).

### Development data

The development data consists of two files -- a words file (the input), and a clusters file (to evaluate your output). The vocab file `dev_input.txt` is formatted such that each line contains one target, its paraphrase set, and the number of ground truth clusters *k*, separated by a `::` symbol:

```
target.pos :: k :: paraphrase1 paraphrase2 paraphrase3 ...
```

You can use *k* as input to your clustering algorithm.

The clusters file `dev_output.txt` contains the ground truth clusters for each target word's paraphrase set, split over *k* lines:

```
target.pos :: 1 :: paraphrase2 paraphrase6
target.pos :: 2 :: paraphrase3 paraphrase4 paraphrase5
...
target.pos :: k :: paraphrase1 paraphrase9
```

### Test data

For testing, you will receive only words file `test_input.txt` containing the test target words and their paraphrase sets. Your job is to create an output file, formatted in the same way as `dev_output.txt`, containing the clusters produced by your system.

## Evaluation

There are many possible ways to evaluate clustering solutions. For this homework we will rely on the paired F-score, which you can read more about in [this paper](https://www.cs.york.ac.uk/semeval2010_WSI/paper/semevaltask14.pdf).

The general idea behind paired F-score is to treat clustering prediction like a classification problem; given a target word and its paraphrase set, we call a *positive instance* any pair of paraphrases that appear together in a ground-truth cluster. Once we predict a clustering solution for the paraphrase set, we similarly generate the set of word pairs such that both words in the pair appear in the same predicted cluster. We can then evaluate our set of predicted pairs against the ground truth pairs using precision, recall, and F-score.

We have provided an evaluation script that you can use when developing your own system. You can run it as follows:

```
python evaluate.py <GROUND-TRUTH-FILE> <PREDICTED-CLUSTERS-FILE>
```

## Baselines

On the dev data, a random baseline gets about 10%, the word cooccurrence matrix gets about 17%, and the word2vec vectors get about 15%.  



Your Tasks
======================
You have 3 tasks. 

### 1. Exploration

The first part of this homework will lead you through loading a dense vector model (trained using `word2vec`), and playing around with the `gensim` library to manipulate and analyze the vectors. The questions are designed to familiarize you with the `gensim.models.KeyedVectors` package, and get you thinking about what type of semantic information word embeddings can encode.

Load the word vectors using the following Python commands:

{% highlight python %}
from gensim.models import KeyedVectors
vecfile = 'GoogleNews-vectors-negative300.filter'
vecs = KeyedVectors.load_word2vec_format(vecfile)
{% endhighlight %}

* What is the dimensionality of these word embeddings? Provide an integer answer.
* What are the top-5 most similar words to `picnic` (not including `picnic` itself)? (Use the function `gensim.models.KeyedVectors.wv.most_similar`)
* According to the word embeddings, which of these words is not like the others?
`['tissue', 'papyrus', 'manila', 'newsprint', 'parchment', 'gazette']`
(Use the function `gensim.models.KeyedVectors.wv.doesnt_match`)
* Solve the following analogy: "leg" is to "jump" as X is to "throw".
(Use the function `gensim.models.KeyedVectors.wv.most_similar` with `positive` and `negative` arguments.)

We have provided a file called `question1.txt` for you to submit answers to the questions above.

### 2. Sparse Representations 

Your next task is to generate clusters for the target words in `test_input.txt` based on a feature-based (not dense) vector space representation. In this type of VSM, each dimension of the vector space corresponds to a specific feature, such as a context word (see, for example, the term-context matrix described in [Chapter 15.1.2 of Jurafsky & Martin](https://web.stanford.edu/~jurafsky/slp3/15.pdf)). 

Since it can take a long time to build cooccurrence vectors, we have pre-built a set, included in the data.zip, called `coocvec-500mostfreq-window-3.vec.filter`. To save on space, these include only the words used in the given files. The code is also available in `makecooccurrences.py` if you want to rerun on different data or different parameters.

The corpus we used is here: `/home1/a/acocos/data/reuters.rcv1.tokenized.gz` (in case you want to access it directly to generate additional vector space models)

Your task is to modify: `vectorcluster.py`

Here is an example of the K-means code:

{% highlight python %}
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=k).fit(X)
print(kmeans.labels_)
{% endhighlight %}

<!--- Baseline description is a placeholder --->
The baseline system for this section represents words using a term-context matrix `M` of size `|V| x D`, where `|V|` is the size of the vocabulary and D=500. Each feature corresponds to one of the top 500 most-frequent words in the corpus. The value of matrix entry `M[i][j]` gives the number of times the context word represented by column `j` appeared within W=3 words to the left or right of the word represented by row `i` in the corpus. Using this representation, the baseline system clusters each paraphrase set using K-means.  

Implementing the baseline will score you a B, but why not try and see if you can do better? You might try experimenting with different features, for example:

* What if you reduce or increase `D` in the baseline implementation?
* Does it help to change the window `W` used to extract contexts?
* Play around with the feature weighting -- instead of raw counts, would it help to use PPMI?
* Try a different clustering algorithm that's included with the [scikit-learn clustering package](http://scikit-learn.org/stable/modules/clustering.html), or implement your own.
* What if you include additional types of features, like paraphrases in the [Paraphrase Database](http://www.paraphrase.org) or the part-of-speech of context words?

The only feature types that are off-limits are WordNet features.

Turn in the predicted clusters that your VSM generates in the file `test_output_features.txt`. Also provide a brief description of your method in `writeup.pdf`, making sure to describe the vector space model you chose, the clustering algorithm you used, and the results of any preliminary experiments you might have run on the dev set. We have provided a LaTeX file shell, `writeup.tex`, which you can use to guide your writeup.

### 3. Dense Representations
Finally, we'd like to see if dense word embeddings are better for clustering the words in our test set. Run the word clustering task again, but this time use a dense word representation. 

For this task, use files:

* `GoogleNews-vectors-negative300.filter`: Google word2vec vectors (300 dimensions, filtered to contain only the words in the dev/test splits)
* Modify `vectorcluster.py` to load dense vectors.

The baseline system for this section uses the provided word vectors to represent words, and K-means for clustering. 

As before, achieving the baseline score will get you a B, but you might try to see if you can do better. Here are some ideas:

* Try downloading a different dense vector space model from the web, like [Paragram](http://www.cs.cmu.edu/~jwieting/) or [fastText](https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md).
* Train your own word vectors, either on the provided corpus or something you find online. You can use the `gensim.models.Word2Vec` package for the skip-gram or CBOW models, or [GLOVE](https://nlp.stanford.edu/projects/glove/). Try experimenting with the dimensionality.
* [Retrofitting](https://www.cs.cmu.edu/~hovy/papers/15HLT-retrofitting-word-vectors.pdf) is a simple way to add additional semantic knowledge to pre-trained vectors. The retrofitting code is available [here](https://github.com/mfaruqui/retrofitting). Experiment with different lexicons, or even try [counter-fitting](http://www.aclweb.org/anthology/N16-1018).

As in question 2, turn in the predicted clusters that your dense vector representation generates in the file `test_output_dense.txt`. Also provide a brief description of your method in `writeup.pdf` that includes the vectors you used, and any experimental results you have from running your model on the dev set. 

In addition, do an analysis of different errors made by each system -- i.e. look at instances that the word-context matrix representation gets wrong and dense gets right, and vice versa, and see if there are any interesting patterns. There is no right answer for this.

### 4. The Leaderboard
In order to stir up some friendly competition, we would also like you to submit the clustering from your best model to  leaderboard. Copy the output file from your best model to a file called `test_output_leaderboard.txt`, and include it with your submission.

### Extra Credit
We made the clustering problem deliberately easier by providing you with `k`, the number of clusters, as an input. But in most clustering situations the best `k` isn't obvious.
To take this assignment one step further, see if you can come up with a way to automatically choose `k`. We have provided an additional test set, `test_nok_input.txt`, where the `k` field has been zeroed out. See if you can come up with a method that clusters words by sense, and chooses the best `k` on its own. (Don't look at the number of WordNet synsets for this, as that would ruin all the fun.) The baseline system for this portion always chooses `k=5`.
You can submit your output to this part in a file called `test_nok_output_leaderboard.txt`. Be sure to describe your method in `writeup.pdf`.


## Deliverables 
<div class="alert alert-warning" markdown="1">
Here are the deliverables that you will need to submit:
* `question1.txt` file with answers to questions from Exploration
* simple VSM clustering output `test_output_features.txt`
* dense model clustering output `test_output_dense.txt`
* your favorite clustering output for the leaderboard, `test_output_leaderboard.txt` (this will probably be a copy of either `test_output_features.txt` or `test_output_dense.txt`)
* `writeup.pdf` (compiled from `writeup.tex`)
* your code (.zip). It should be written in Python 3.
* (optional) the output of your model that automatically chooses the number of clusters, `test_nok_output_leaderboard.txt`
</div>

## Recommended readings
* Jurafsky and Martin, chapters [15](https://web.stanford.edu/~jurafsky/slp3/15.pdf) and [16](https://web.stanford.edu/~jurafsky/slp3/16.pdf)
* [Implementing Poincaré Embeddings](https://rare-technologies.com/implementing-poincare-embeddings/)
* [Clustering paraphrases by word sense](https://www.cis.upenn.edu/~ccb/publications/clustering-paraphrases-by-word-sense.pdf)
* [Discovering Word Senses from Text](https://cs.uwaterloo.ca/~cdimarco/pdf/cs886/Pantel+Lin02.pdf)
