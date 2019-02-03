---
layout: default
img: clusters.png
caption: Did you know that matplotlib has an xkcd() function?
img_link: https://matplotlib.org/xkcd/examples/showcase/xkcd.html    
title: Homework 4 - Advanced Vector Space Models
active_tab: homework
release_date: 2018-01-31
due_date: 2018-02-07T11:00:00EST
attribution: Stephen Mayhew, Anne Cocos and Chris Callison-Burch developed this homework assignment for UPenn's CIS 530 class in Spring 2018.
readings:
-
   title: Vector Semantics
   authors: Dan Jurafsky and James H. Martin
   venue: Speech and Language Processing (3rd edition draft)
   type: textbook
   url: https://web.stanford.edu/~jurafsky/slp3/15.pdf
-
   title: Semantics with Dense Vectors
   authors: Dan Jurafsky and James H. Martin
   venue: Speech and Language Processing (3rd edition draft)
   type: textbook
   url: https://web.stanford.edu/~jurafsky/slp3/16.pdf
-
   title: Efficient Estimation of Word Representations in Vector Space
   authors:  Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean
   venue: ArXiV
   type: conference
   year: 2013
   url: https://arxiv.org/pdf/1301.3781.pdf?
   id: efficient-estimation-of-word-representations
   abstract: We propose two novel model architectures for computing continuous vector representations of words from very large data sets. The quality of these representations is measured in a word similarity task, and the results are compared to the previously best performing techniques based on different types of neural networks. We observe large improvements in accuracy at much lower computational cost, i.e. it takes less than a day to learn high quality word vectors from a 1.6 billion words data set. Furthermore, we show that these vectors provide state-of-the-art performance on our test set for measuring syntactic and semantic word similarities.
-
   title: Linguistic Regularities in Continuous Space Word Representations
   authors:  Tomas Mikolov, Wen-tau Yih, Geoffrey Zweig
   venue: NAACL
   type: conference
   year: 2013
   url: https://www.aclweb.org/anthology/N13-1090
   id: linguistic-regularities-in-continous-space-word-representations
   abstract: Continuous space language models have recently demonstrated outstanding results across a variety of tasks. In this paper, we examine the vector-space word representations that are implicitly learned by the input-layer weights. We find that these representations are surprisingly good at capturing syntactic and semantic regularities in language, and that each relationship is characterized by a relation-specific vector offset. This allows vector-oriented reasoning based on the offsets between words. For example, the male/female relationship is automatically learned, and with the induced vector representations, “King Man + Woman” results in a vector very close to “Queen.” We demonstrate that the word vectors capture syntactic regularities by means of syntactic analogy questions (provided with this paper), and are able to correctly answer almost 40% of the questions. We demonstrate that the word vectors capture semantic regularities by using the vector offset method to answer SemEval-2012 Task 2 questions. Remarkably, this method outperforms the best previous systems.
   bibtex: |  
      @InProceedings{mikolov-yih-zweig:2013:NAACL-HLT,
        author    = {Mikolov, Tomas  and  Yih, Wen-tau  and  Zweig, Geoffrey},
        title     = {Linguistic Regularities in Continuous Space Word Representations},
        booktitle = {Proceedings of the 2013 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
        month     = {June},
        year      = {2013},
        address   = {Atlanta, Georgia},
        publisher = {Association for Computational Linguistics},
        pages     = {746--751},
        url       = {http://www.aclweb.org/anthology/N13-1090}
      }
-
   title: Discovering Word Senses from Text
   authors: Patrick Pangel and Dekang Ling
   venue: KDD
   type: conference
   year: 2002
   url: https://www.semanticscholar.org/paper/Discovering-word-senses-from-text-Pantel-Lin/
   id: discovering-word-senses-from-text
   abstract: Inventories of manually compiled dictionaries usually serve as a source for word senses. However, they often include many rare senses while missing corpus/domain-specific senses. We present a clustering algorithm called CBC (Clustering By Committee) that automatically discovers word senses from text. It initially discovers a set of tight clusters called committees that are well scattered in the similarity space. The centroid of the members of a committee is used as the feature vector of the cluster. We proceed by assigning words to their most similar clusters. After assigning an element to a cluster, we remove their overlapping features from the element. This allows CBC to discover the less frequent senses of a word and to avoid discovering duplicate senses. Each cluster that a word belongs to represents one of its senses. We also present an evaluation methodology for automatically measuring the precision and recall of discovered senses. 
   bibtex: |  
      @inproceedings{Pantel2002DiscoveringWS,
        title={Discovering word senses from text},
        author={Patrick Pantel and Dekang Lin},
        booktitle={KDD},
        year={2002}
      }
-
   title: Clustering Paraphrases by Word Sense
   authors: Anne Cocos and Chris Callison-Burch
   venue: NAACL
   type: conference
   year: 2016
   url: https://www.cis.upenn.edu/~ccb/publications.html
   page_count: 10
   id: clustering-paraphrases-by-word-sense
   abstract: Automatically generated databases of English paraphrases have the drawback that they return a single list of paraphrases for an input word or phrase. This means that all senses of polysemous words are grouped together, unlike WordNet which partitions different senses into separate synsets. We present a new method for clustering paraphrases by word sense, and apply it to the Paraphrase Database (PPDB). We investigate the performance of hierarchical and spectral clustering algorithms, and systematically explore different ways of defining the similarity matrix that they use as input. Our method produces sense clusters that are qualitatively and quantitatively good, and that represent a substantial improvement to the PPDB resource.
   bibtex: |
      @inproceedings{Cocos-Callison-Burch:2016:NAACL,
       author = {Anne Cocos and Chris Callison-Burch},
       title = {Clustering Paraphrases by Word Sense},
       booktitle = {The 2016 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL 2016)},
       month = {June},
       year = {2016},
       address = {San Diego, California},
       url = {http://www.cis.upenn.edu/~ccb/publications/clustering-paraphrases-by-word-sense.pdf}
       } 
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

Advanced Vector Space Models <span class="text-muted">: Assignment 4</span>
=============================================================

In this assignment, we will examine some advanced uses of vector representations of words. We are going to look at two different problems: 
1. Solving word relation problems like analogies using word embeddings. 
2. Discovering the different senses of a "polysemous" word by clustering together its synonyms. 
You will use an open source Python package for creating and manipulating word vectors called Magnitude. Magnitude lets you easily train word embedding models like word2vec.


<div class="alert alert-warning" markdown="1">
In order to use the Magnitude package, please follow the [installation guidelines](https://github.com/plasticityai/magnitude#installation) 
</div>

<div class="alert alert-info" markdown="1">
Here are the materials that you should download for this assignment:
* [`question1.txt`](downloads/hw4/question1.txt) A template for answering question 1.
* [`data.zip`](downloads/hw4/data.zip) Contains all the data
* [`vectorcluster.py`](downloads/hw4/vectorcluster.py) Main code stub
* [`evaluate.py`](downloads/hw4/evaluate.py) Evaluation script
* [`writeup.tex`](downloads/hw4/writeup.tex) Report template.
* [`makecooccurrences.py`](downloads/hw4/makecooccurrences.py) Script to make cooccurrences (optional use) 
* [Tokenized Reuters RCV1 Corpus](http://www.cis.upenn.edu/~cis530/18sp/data/reuters.rcv1.tokenized.gz)
* [Google's pretrained word2vec vectors](https://code.google.com/archive/p/word2vec/), under the heading "Pretrained word and phrase vectors"
</div>



# Part 1: Exploring Analogies and Other Word Pair Relationships

Word2vec is a very cool word embedding method that was developed by Thomas Mikolov and his collaborators.  One of the noteworthy things about the method is that it can be used to solve word analogy problems like: man is to king as woman is to [blank]. The way that it they take the vectors representing *king*, *man* and *woman* and perform some vector arithmetic to produce a vector that is close to the expected answer: $king−man+woman \approx queen$. 
We can find the nearest vector in the vocabulary by looking for $argmax \ cos(x, king-man+woman)$.  Omar Levy has a nice explanation of the method in [this Quora post](https://www.quora.com/How-does-Mikolovs-word-analogy-for-word-embedding-work-How-can-I-code-such-a-function) and in his paper [Linguistic Regularities in Sparse and Explicit Word Representations](http://www.aclweb.org/anthology/W14-1618).

In addition to solving this sort of analogy problem, the same sort of vector arithmetic was used with word2vec embeddings to find relationships between pairs of words like the following: 

 <p align="center">
<img src="/assets/img/word2vec_word_pair_relationships.jpg" alt="Examples of five types of semantic and nine types of syntactic questions in the Semantic- Syntactic Word Relationship test set" style="width: 50%;"/>
</p>

In the first part of this homework, you will play around with the [Magnitude](https://github.com/plasticityai/magnitude)  library.  You will use Magnitude to load a dense vector model trained using word2vec, and use it to manipulate and analyze the vectors.  We recommend reading [Using the Library](https://github.com/plasticityai/magnitude#using-the-library) section to answer the homework questions. The questions below are designed to familiarize you with the Magnitude word2vec package, and get you thinking about what type of semantic information word embeddings can encode.  You'll submit your answers to these questions when you submit your other homework materials. 

First, download the Medium Google-word2vec embedding model available using the following [link](http://magnitude.plasticity.ai/word2vec/light/GoogleNews-vectors-negative300.magnitude).  The file to be downloaded is called `GoogleNews-vectors-negative300.magnitude` and is a Medium Pre-converted Magnitude Formats of word2vec. (Note that it can take a while to download) Once the file is downloaded use the following Python commands:

 ```python
>>> from pymagnitude import *
>>> file_path = "GoogleNews-vectors-negative300.magnitude"
>>> vectors = Magnitude(file_path)
```

Now you can use `vectors` to perform queries. For instance, you can query the distance of `cat` and `dog` in the following way: 
 ```python
>>> vectors.distance("cat", "dog")
0.69145405
```

1. What is the dimensionality of these word embeddings? Provide an integer answer.
2. What are the top-5 most similar words to `picnic` (not including `picnic` itself)? (Use the function `most_similar_to_given`)
3. According to the word embeddings, which of these words is not like the others?
`['tissue', 'papyrus', 'manila', 'newsprint', 'parchment', 'gazette']`
(Use the function `doesnt_match`)
4. Solve the following analogy: `leg` is to `jump` as *X* is to `throw`.
(Use the function `most_similar` with `positive` and `negative` arguments)

We have provided a file called `question1.txt` for you to submit answers to the questions above.

# Part 2: Creating Word Sense Clusters


Many natural language processing (NLP) tasks require knowing the sense of polysemous words, which are words with multiple meanings. For example, the word *bug* can mean:
1. a creepy crawly thing
2. an error in your computer code
3. a virus or bacteria that makes you sick
4. a listening device planted by the FBI

In past research my PhD students and I have looked into automatically deriving the different meaning of polysemous words like bug by clustering their paraphrases.  We have developed a resource called [the paraphrase database (PPDB)](http://paraphrase.org/) that contains of paraphrases for  tens of millions words and phrases.  For the target word *bug*, we have an unordered list of paraphrases including: *insect, glitch, beetle, error, microbe, wire, cockroach, malfunction, microphone, mosquito, virus, tracker, pest, informer, snitch, parasite, bacterium, fault, mistake, failure* and many others.  We used automatic clustering group those into sets like:

 <p align="center">
<img src="/assets/img/bug_clusters.jpg" alt="Bug Clusters" style="width: 50%;"/>
</p>

These clusters approximate the different word senses of *bug*.  You will explore the main idea underlying our word sense clustering method: which measure the similarity between each pair of paraphrases for a target word and then group together the paraphrases that are most similar to each other.   This affinity matrix gives an example of one of the methods for measuring similarity that we tried in [our paper](https://www.cis.upenn.edu/~ccb/publications/clustering-paraphrases-by-word-sense.pdf):

 <p align="center">
<img src="/assets/img/affinity_matrix.jpg" alt="Similarity of paraphrses" style="width: 50%;"/>
</p>

Here the darkness values give an indication of how similar paraprhases are to each other.  For instance *sim(insect, pest) > sim(insect, error)*.  

In this assignment, we will use vector representations in order to measure their similarities of pairs of paraprhases.  You will play with different vector space representations of words to create clusters of word senses.


In this image, we have a target word *bug*, and a list of all synonyms (taken from WordNet). The 4 circles are the 4 senses of *bug*. The input to the problem is all the synonyms in a single list, and the task is to separate them correctly. As humans, this is pretty intuitive, but computers aren't that smart. We will use this task to explore different types of word representations.

You can read more about this task in [these](https://www.cis.upenn.edu/~ccb/publications/clustering-paraphrases-by-word-sense.pdf) [papers](https://cs.uwaterloo.ca/~cdimarco/pdf/cs886/Pantel+Lin02.pdf). 



Clustering with Word Vectors
=================================

We expect that you have read Jurafsky and Martin, chapters [15](https://web.stanford.edu/~jurafsky/slp3/15.pdf) and [16](https://web.stanford.edu/~jurafsky/slp3/16.pdf). Word vectors, also known as word embeddings, can be thought of simply as points in some high-dimensional space. Remember in geometry class when you learned about the Euclidean plane, and 2-dimensional points in that plane? It's not hard to understand distance between those points -- you can even measure it with a ruler. Then you learned about 3-dimensional points, and how to calculate the distance between these. These 3-dimensional points can be thought of as positions in physical space. 

Now, do your best to stop thinking about physical space, and generalize this idea in your mind: you can calculate a distance between 2-dimensional and 3-dimensional points, now imagine a point with 300 dimensions. The dimensions don't necessarily have meaning in the same way as the X,Y, and Z dimensions in physical space, but we can calculate distances all the same. 

This is how we will use word vectors in this assignment: as points in some high-dimensional space, where distances between points are meaningful. The interpretation of distance between word vectors depends entirely on how they were made, but for our purposes, we will consider distance to measure semantic similarity. Word vectors that are close together should have meanings that are similar. 

With this framework, we can see how to solve our synonym clustering problem. Imagine in the image below that each point is a (2-dimensional) word vector. Using the distance between points, we can separate them into 3 clusters. This is our task. 

 
![kmeans](/assets/img/kmeans.svg)
(Image taken from [Wikipedia](https://en.wikipedia.org/wiki/K-means_clustering))


## The Data

The data to be used for this assignment consists of sets of paraphrases corresponding to one of 56 polysemous target words, e.g.

<table class="table">
  <thead>
    <tr>
      <th scope="col">Target</th>
      <th scope="col">Paraphrase set</th>
    </tr>
  </thead>
  <tbody>
    <tr>      
      <td>note.v</td>
      <td>comment mark tell observe state notice say remark mention</td>
    </tr>
    <tr>
      <td>hot.a</td>
      <td>raging spicy blistering red-hot live</td>
    </tr>
  </tbody>
</table>


(Here the `.v` following the target `note` indicates the part of speech.)

Your objective is to automatically cluster each paraphrase set such that each cluster contains words pertaining to a single *sense*, or meaning, of the target word. Note that a single word from the paraphrase set might belong to one or more clusters.

For evaluation, we take the set of ground truth senses from [WordNet](http://wordnet.princeton.edu).

### Development data

The development data consists of two files -- a words file (the input), and a clusters file (to evaluate your output). The words file `dev_input.txt` is formatted such that each line contains one target, its paraphrase set, and the number of ground truth clusters *k*, separated by a `::` symbol:

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

For testing, you will receive only words file `test_input.txt` containing the test target words and their paraphrase sets. Your job is to create an output file, formatted in the same way as `dev_output.txt`, containing the clusters produced by your system. Neither order of senses, nor order of words in a cluster matter.

## Evaluation

There are many possible ways to evaluate clustering solutions. For this homework we will rely on the paired F-score, which you can read more about in [this paper](https://www.cs.york.ac.uk/semeval2010_WSI/paper/semevaltask14.pdf).

The general idea behind paired F-score is to treat clustering prediction like a classification problem; given a target word and its paraphrase set, we call a *positive instance* any pair of paraphrases that appear together in a ground-truth cluster. Once we predict a clustering solution for the paraphrase set, we similarly generate the set of word pairs such that both words in the pair appear in the same predicted cluster. We can then evaluate our set of predicted pairs against the ground truth pairs using precision, recall, and F-score.

We have provided an evaluation script that you can use when developing your own system. You can run it as follows:

```
python evaluate.py <GROUND-TRUTH-FILE> <PREDICTED-CLUSTERS-FILE>
```

## Baselines

On the dev data, a random baseline gets about 20%, the word cooccurrence matrix gets about 36%, and the word2vec vectors get about 30%.  



### 1. Sparse Representations 

Your next task is to generate clusters for the target words in `test_input.txt` based on a feature-based (not dense) vector space representation. In this type of VSM, each dimension of the vector space corresponds to a specific feature, such as a context word (see, for example, the term-context matrix described in [Chapter 15.1.2 of Jurafsky & Martin](https://web.stanford.edu/~jurafsky/slp3/15.pdf)). 

You will calculate cooccurrence vectors on the Reuters RCV1 corpus. Download a [tokenized and cleaned version here](http://www.cis.upenn.edu/~cis530/18sp/data/reuters.rcv1.tokenized.gz). The original is [here](https://archive.ics.uci.edu/ml/datasets/Reuters+RCV1+RCV2+Multilingual,+Multiview+Text+Categorization+Test+collection). Use the provided script, `makecooccurrences.py`, to build these vectors. Be sure to set D and W to what you want. 

It can take a long time to build cooccurrence vectors, so we have pre-built a set, included in the data.zip, called `coocvec-500mostfreq-window-3.vec.filter`. To save on space, these include only the words used in the given files.

You will add K-means clustering to `vectorcluster.py`. Here is an example of the K-means code:

{% highlight python %}
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=k).fit(X)
print(kmeans.labels_)
{% endhighlight %}

<!--- Baseline description is a placeholder --->
The baseline system for this section represents words using a term-context matrix `M` of size `|V| x D`, where `|V|` is the size of the vocabulary and D=500. Each feature corresponds to one of the top 500 most-frequent words in the corpus. The value of matrix entry `M[i][j]` gives the number of times the context word represented by column `j` appeared within W=3 words to the left or right of the word represented by row `i` in the corpus. Using this representation, the baseline system clusters each paraphrase set using K-means.  

While experimenting, write out clusters for the dev input to `dev_output_features.txt` and use the `evaluate.py` script to compare against the provided `dev_output.txt`.

Implementing the baseline will score you a B, but why not try and see if you can do better? You might try experimenting with different features, for example:

* What if you reduce or increase `D` in the baseline implementation?
* Does it help to change the window `W` used to extract contexts?
* Play around with the feature weighting -- instead of raw counts, would it help to use PPMI?
* Try a different clustering algorithm that's included with the [scikit-learn clustering package](http://scikit-learn.org/stable/modules/clustering.html), or implement your own.
* What if you include additional types of features, like paraphrases in the [Paraphrase Database](http://www.paraphrase.org) or the part-of-speech of context words?

The only feature types that are off-limits are WordNet features.

Turn in the predicted clusters that your VSM generates in the file `test_output_features.txt`. Also provide a brief description of your method in `writeup.pdf`, making sure to describe the vector space model you chose, the clustering algorithm you used, and the results of any preliminary experiments you might have run on the dev set. We have provided a LaTeX file shell, `writeup.tex`, which you can use to guide your writeup.

### 2. Dense Representations
Finally, we'd like to see if dense word embeddings are better for clustering the words in our test set. Run the word clustering task again, but this time use a dense word representation. 

For this task, use files:

* [Google's pretrained word2vec vectors](https://code.google.com/archive/p/word2vec/), under the heading "Pretrained word and phrase vectors"
* The Google file is very large (~3.4GB), so we have also included in the data.zip a file called `GoogleNews-vectors-negative300.filter`, which is filtered to contain only the words in the dev/test splits.
* Modify `vectorcluster.py` to load dense vectors.

The baseline system for this section uses the provided word vectors to represent words, and K-means for clustering. 

As before, achieving the baseline score will get you a B, but you might try to see if you can do better. Here are some ideas:

* Try downloading a different dense vector space model from the web, like [Paragram](http://www.cs.cmu.edu/~jwieting/) or [fastText](https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md).
* Train your own word vectors, either on the provided corpus or something you find online. You can use the `gensim.models.Word2Vec` package for the skip-gram or CBOW models, or [GLOVE](https://nlp.stanford.edu/projects/glove/). Try experimenting with the dimensionality.
* [Retrofitting](https://www.cs.cmu.edu/~hovy/papers/15HLT-retrofitting-word-vectors.pdf) is a simple way to add additional semantic knowledge to pre-trained vectors. The retrofitting code is available [here](https://github.com/mfaruqui/retrofitting). Experiment with different lexicons, or even try [counter-fitting](http://www.aclweb.org/anthology/N16-1018).

As in question 2, turn in the predicted clusters that your dense vector representation generates in the file `test_output_dense.txt`. Also provide a brief description of your method in `writeup.pdf` that includes the vectors you used, and any experimental results you have from running your model on the dev set. 

In addition, do an analysis of different errors made by each system -- i.e. look at instances that the word-context matrix representation gets wrong and dense gets right, and vice versa, and see if there are any interesting patterns. There is no right answer for this.

### 3. The Leaderboard
In order to stir up some friendly competition, we would also like you to submit the clustering from your best model to a leaderboard. Copy the output file from your best model to a file called `test_output_leaderboard.txt`, and include it with your submission.

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
* (optional) the output of your model that automatically chooses the number of clusters, `test_nok_output_leaderboard.txt` (submit this to the Gradescope assignment 'Homework 4 EXTRA CREDIT')
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
