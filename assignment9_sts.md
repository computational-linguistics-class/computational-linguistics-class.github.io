---
layout: default
img: similarities.png
img_link: http://xkcd.com/353/
caption: Similarities
title: Homework 9 (Optional) - Semantic Textual Similarity
active_tab: homework
term_project: true
release_date: 2018-05-02
due_date: 2018-05-14T11:00:00EST
attribution: This assignment was designed by students in Penn's CIS 530 in the Spring of 2018 with help from Nikesh Garera.  It is based on [SemEval-2017 Task 1 "Semantic Textual Similarity Multilingual and Cross-lingual Focused Evaluation"](http://www.aclweb.org/anthology/S17-2001) by Dan Cer, Mona Diab, Eneko Agirre, Iñigo Loez-Gazpio and Lucia Specia.
---

# Semantic Textual Similarity

The ability to automatically infer the semantic similarity between two pieces of text is of utmost importance in natural language processing. While the semantic similarity at a lexical level, i.e. between words has been widely studied (Eg. word-net, word-vectors), inferring semantic similarity for longer pieces of text is still fairly under-researched.  

In this assignment, we will try to design a machine learning model for measuring semantic similarity between two given sentences in English. Along with understanding lexical-level similarity, this also requires modeling how syntactic composition affects the semantics of a sentence, even though at the lexical level the sentences might be very similar. Consider the following examples,

<!-- Semantic Textual Similarity (STS) measures the degree of equivalence in the underlying semantics of paired
snippets of text. While making such an assessment is trivial for humans, constructing algorithms and
computational models that mimic human level performance represents a difficult and deep natural language
understanding (NLU) problem. -->

#### Example 1:

Sentence 1: Birdie is washing itself in the water basin.

Sentence 2: The bird is bathing in the sink.

*The two sentences have very high semantic similarity, even though the lexical match is very low*

#### Example 2:

English: The young lady enjoys listening to the guitar.

English Paraphrase: The young lady enjoys playing the guitar.

*The two sentences have very low semantic similarity, even though the lexical match is very high*

<div class="alert alert-info" markdown="1">
Here are the materials that you should download for this assignment:
* [`data.zip`](/downloads/sts/data.zip): Contains the data for STS-2017.
* [`evaluate.py`](/downloads/sts/evaluate.py): Contains the evaluation script for the assignment
</div>


### Semantic Text Similarity Shared Task
In this assignment, we will make use of the data provided in the [Semantic Textual Similarity (STS) - 2017](http://www.aclweb.org/anthology/S17-2001) shared task.

1. Similarity Measure: The semantic similarity in this dataset is measured on a scale of 0-5 where 0 indicates that the semantics of the sentences are completely independent and 5 signifies semantic equivalence.

2. Data: We provide training/validation/test splits for the data containing 13365/1500/250 samples, respectively.

3. Evaluation Metric: Performance is assessed by computing the Pearson correlation between machine assigned semantic similarity scores and human judgements.

In addition to the provided data, you are free to use any supervised or unsupervised data. One possible resource is the plethora of available data from [shared tasks in STS](http://ixa2.si.ehu.es/stswiki/index.php/Main_Page) from at least the last 5 years.


## A simple unsupervised baseline

Suggested by [models submitted to shared task - STS 2017](http://www.aclweb.org/anthology/S17-2001), a simple unsupervised baseline can be the cosine similarity between the bag-of-words representation  sentence. You need to implement this simple baseline as a sanity check. This should reach a Pearson correlation of about 0.35 on the test set.


## Improving performance

For the next part of the assignment, you need to develop two models for predicting STS. The team that did this as a course project implemented the [model from DT_Team](http://www.aclweb.org/anthology/S17-2014) and report a Pearson correlation score of ~0.65.

You can implement the same model, or come up with new ideas to improve the performance.

## Submission

You need to submit two things:
1. A `writeup.pdf` explaining in detail the models implemented
2. `code.zip` containing the code with a comprehensible README

## References

Here is a list of numerous submissions to the STS task. Feel free to borrow ideas from here.

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
