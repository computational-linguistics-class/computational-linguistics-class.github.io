---
layout: default
img: python.jpg
img_link: http://xkcd.com/353/
caption: Hello world!
title: Semantic Textual Similarity
active_tab: homework
term_project: true
---

# Semantic Textual Similarity

## Problem Definition

Your goal in this project is to measure semantic textual similarity between a given pair of sentences (what they mean rather than whether they look similar syntactically). 

Semantic Textual Similarity (STS) measures the degree of equivalence in the underlying semantics of paired
snippets of text. While making such an assessment is trivial for humans, constructing algorithms and
computational models that mimic human level performance represents a difficult and deep natural language
understanding (NLU) problem.


#### Example 1:

English: Birdie is washing itself in the water basin.

English Paraphrase: The bird is bathing in the sink.

Similarity Score: 5 ( The two sentences are completely equivalent, as they mean the same thing.)

#### Example 2:

English: The young lady enjoys listening to the guitar.

English Paraphrase: The woman is playing the violin.

Similarity Score: 1 ( The two sentences are not equivalent, but are on the same topic. )

You are free to use any unsupervised or supervised approach for the above mentioned problem. A very simple baseline to start with would be using binary bag-of-words model with the entire vocabulary as features to create embeddings and measuring the cosine similarity between the produced embeddings to generate a final prediction score. 

## Evaluation Metric
Given two sentences, participating systems are asked to return a continuous valued similarity score on a scale from
0 to 5, with 0 indicating that the semantics of the sentences are completely independent and 5 signifying semantic
equivalence. Performance is assessed by computing the Pearson correlation between machine assigned semantic
similarity scores and human judgements.

For more details of different levels of similarity, see table in [Models submitted to shared task - STS 2017](http://www.aclweb.org/anthology/S17-2001).

## Dataset
Training data [`en-train.txt`](../data/en-train-complete.txt) contains 9472 pairs while each of [`en-val.txt`](../data/en-val.txt) and [`en-test.txt`](../data/en-test.txt) contains 1500 pairs. 

Speaking of sources of data, there are a lot of available data from shared tasks in STS from at least the last 5 years. We just use the evaluation data from [2017 shared task](http://alt.qcri.org/semeval2017/task1/) as the test set.


## Resources

[STS Shared Task 2017](http://alt.qcri.org/semeval2017/task1/)

[Models submitted to shared task - STS 2017](http://www.aclweb.org/anthology/S17-2001)


## A simple baseline

Suggested by [Models submitted to shared task - STS 2017](http://www.aclweb.org/anthology/S17-2001), a simple baseline can be the cosine of binary sentence vectors with each dimension representing whether an individual word appears in a sentence. You should reach a Pearson correlation about 0.35.

## Improving performance

Broadly speaking, there are following three aspects towards improvements:

1. whether or not the method utilizes gold-standard similarities (supervised or unsupervised; simple baseline is obviously unsupervised);
2. choice of sentence embeddings;
3. the way of utilizing sentence embeddings.

Enumerous attempts have been made and following is just a selected list:

1. ECNU - **[Junfeng Tian, Zhiheng Zhou, Man Lan, and Yuanbin Wu. 2017. ECNU at SemEval-2017 Task 1: Leverage kernel- based traditional nlp features and neural networks to build a universal model for multilingual and cross-lingual seman- tic textual similarity. In Proceedings of SemEval-2017.](http://www.aclweb.org/anthology/S17-2028)**
2. BIT - **[Wu, Hao, et al. "BIT at SemEval-2017 Task 1: Using semantic information space to evaluate semantic textual similarity." Proceedings of the 11th International Workshop on Semantic Evaluation (SemEval-2017). 2017.](http://www.aclweb.org/anthology/S17-2007)**
3. MITRE  - **[John Henderson, Elizabeth Merkhofer, Laura Strickhart, and
Guido Zarrella. 2017. MITRE at SemEval-2017 Task 1:
Simple semantic similarity. In Proceedings of SemEval2017.](http://www.aclweb.org/anthology/S17-2027)**
4. FCICU  -  **[Basma Hassan, Samir AbdelRahman, Reem Bahgat, and Ibrahim Farag. 2017. FCICU at SemEval-2017 Task 1: Sense-based language independent semantic textual
similarity approach. In Proceedings of SemEval-2017.](http://www.aclweb.org/anthology/S17-2015)**
5. Compi_LIG  -  **[Ferrero, Jérémy, et al. "CompiLIG at SemEval-2017 Task 1: Cross-language plagiarism detection methods for semantic textual similarity." arXiv preprint arXiv:1704.01346 (2017).](https://arxiv.org/pdf/1704.01346.pdf)**
6. LIM_LIG  -  **[Ferrero, Jérémy, and Didier Schwab. "LIM-LIG at SemEval-2017 Task1: Enhancing the Semantic Similarity for Arabic Sentences with Vectors Weighting." International Workshop on Semantic Evaluations (SemEval-2017). 2017.](https://hal.archives-ouvertes.fr/hal-01531255/)**
7. DT_Team -  **[Maharjan, Nabin, et al. "DT_Team at SemEval-2017 Task 1: Semantic Similarity Using Alignments, Sentence-Level Embeddings and Gaussian Mixture Model Output." Proceedings of the 11th International Workshop on Semantic Evaluation (SemEval-2017). 2017.](http://www.aclweb.org/anthology/S17-2014)**  
8. sent2vec  -  **[Pagliardini, Matteo, Prakhar Gupta, and Martin Jaggi. "Unsupervised learning of sentence embeddings using compositional n-gram features." arXiv preprint arXiv:1703.02507 (2017).](https://arxiv.org/abs/1703.02507)**
 
DT_Team might be a good start since it turns the problem into feature engineering and selection of classifiers. You will receive full credits by having over 0.60 Pearson correlation.
