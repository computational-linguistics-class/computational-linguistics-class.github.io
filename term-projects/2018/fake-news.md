---
layout: default
img: python.jpg
img_link: http://xkcd.com/353/
caption: Hello world!
title: Fake News
active_tab: homework
term_project: true
---

# Fake News Detection

## Goal
Identifying public misinformation is a difficult problem. Stance detection, determining the perspective a news source takes towards a given claim, is a key part of evaluating the truthfulness of a claim. 

News is an important source of information for people. However, with the growing shift towards news consumption through social media sites like Facebook and Twitter, most of the traditional as well as new-age media companies have started promoting their news stories by Tweeting them or posting them on Facebook. The competition for user attention in these social media mediums has led to the use of clickbait headlines - catchy sensational headlines that don't necessarily relate to the body of text in the article. This proliferation of "fake" or "hyper-partisan" news has challenged traditional journalism as well as media infrastructure. 

Facebook, in particular, has come under a lot of heat for proliferation of "fake news". Last year, Facebook made a shift in its News Feed algorithm in hopes that it would stem the spread of Fake News. In April of this year, executives at Facebook stressed that Facebook would be "expanding its fact-checking efforts", ramping up partnerships with third-party fact-checkers like AP journalists from all 50 states [1]. Nonetheless, some external analysts have noted that these efforts have had minimal impact and complained that Facebook was exploiting journalists' labor for a PR effort. Facebook is at a pivotal point in dealing with social, political, and cultural consequences due to weaknesses in its platform. Proliferation of Fake News on Facebook is an issue that will persist for the foreseeable future.

Fake news is informally defined as "made up stories with an intention to deceive" [2]. Fake news detection can take many forms:

1. determining if the facts present in the article are correct
2. analyzing the relationship between the article headline and article body
3. quantifying the bias of a written piece

In this challenge, we aim to address the second problem. 

## Challenge Description

Suppose you're a data scientist at Facebook. In the last year, the product managers for your team have suggested a 'Disputed Flags' feature [3] to deal with stance detection. That is, you have two human fact checkers that review specific articles to get a relationship between the headline and the body of text. 

However, you discover after a year of experimentation that the manual reviews were taking too long (over 3 days on average). Your data science manager wants you to build a machine learning classifier to detect the relationship between the article body and the article header. Your manager hopes that doing so will assist human fact checkers to detect inaccurate headlines as well as the relationship between text bodies and headlines. 

The primary objective is to build a classifier with the highest accuracy possible. Model complexity and runtime are additional factors to be considered in the model selection process. Furthermore, model interpretability is also a huge concern. Your data science manager emphasizes that having a model output that can be integrated with current manual labelling efforts is essential.

In the **deliverables** section, we will outline the materials you need to submit as well as the key questions we want you to address in the writeup.

The data and challenge are based on the Fake News Challenge [4].

## Data 
Data from the past year of manual article labels are included (collected using the Disputed Flags feature). The data can be downloaded [**here**](https://drive.google.com/drive/folders/1H_X3gWf9VyoPvZ_Y-qzuJKvcgK9TOOrV?usp=sharing). For the purposes of this challenge, your data has already been split into training/dev/test. 

The two types of tables are:

**stances** - has the stances associated with each headline

Columns:
- Headline
    - The text of the headline
- Body ID
    - The unique identifier associated with the body of text matched with the headline
- Stance
    - This is our **target metric**- what we are trying to predict. The stance label to be assigned could be one of the 4 categories: ‘agree’, ‘disagree’, ‘discuss’, or ‘unrelated’. Hence, our problem is a **multi-class classification problem** and this will be later discussed in our evaluation section.
        - **Agrees** - The body text agrees with the headline.
        - **Disagrees**: The body text disagrees with the headline.
        - **Discusses**: The body text discuss the same topic as the headline, but does not take a position
        - **Unrelated**: The body text discusses a different topic than the headline

**bodies** - has the text associated with the article body

Columns:
- Body ID
    - Matches with the Body ID in **stances**
- articleBody
    - The full text for the article body.
****

Note that the distribution of the headline-body relationship is not the same across training/dev/test- **in your writeup, please explore how the distribution of the target metric varies across the training/dev/test sets**. 

We will assume also that the text for the article body and the article headline has not been cleaned/preprocessed. **In your data preprocessing stage, please do some additional data cleaning. Additionally, in your feature engineering, play around with the different features you can do with bodies of text**. As your data science manager likes to remind you, good data beats good models. So, take this step seriously!

## Files Provided
We have provided you with four files [**here**](https://drive.google.com/drive/folders/1H_X3gWf9VyoPvZ_Y-qzuJKvcgK9TOOrV?usp=sharing):

-  mlp.py
    -  skeleton code for setting up a simple neural network
-  setup.py
    -  skeleton code for importing the data as well as feature engineering
-  supervisedClassifier.py
    -  skeleton code for setting up a simple multi-class classification learner
-  evaluate.py
    -  skeleton code for evaluating the classifier as described below

## Evaluation
After meeting with the product manager on your team, you decide to come up with a sensible evaluation metric for this problem. 

Your product manager feels that the related/unrelated classification task should be much easier and less relevant for detecting fake news on Facebook, so it should be given less weight in the evaluation metric. Furthermore, your product manager feels that the stance detection task (classifying agrees, disagrees, or discusses) is much more difficult, nuanced, and relevant to fake news detection. Thus, you decide to give it more weight in the evaluation metric.

Hence, our evaluation metric is designed as a 2-level scoring system:

**Level 1**: Correctly classify headline and body text as related or unrelated and receive 25% score weighting
**Level 2**: Correctly classify related pairs as agrees, disagrees, or discusses and receive 75% score weighting

A visual representation of this evaluation metric is shown below.

![](http://www.fakenewschallenge.org/assets/img/fnc-eval.png)

## Machine Learning
### Feature Engineering
Extract TF-IDF embeddings of each article and headline (using a Bag of Words method), and remove stopwords, which you can get from the NLTK.corpus package or create on your own from observed data. Using the sklearn Vectorizer library,  extract TFIDF features of size 5000 from the data, creating word embeddings for the headline and body, and then combine the word embeddings into one vector for each sample. Also include a feature that measures the cosine similarity between the headline and article TF-IDF vectors.
### Baseline
* *Majority Class Baseline*: Label all samples with most frequent class label in the training data. (See sci-kit's Majority Class classifier)
* *Neural Net Baseline* Using the features extracted from the previous section, construct a Neural network to classify the document embeddings. Use Tensorflow to implement the neural net. A suggested neural net structure contains 1 hidden layer and a linear layer, and then applies the Softmax function to classify the documents. The hidden layer should be of dimension 100, and the batch size should be 500. ![](https://i.imgur.com/TCw75ei.png)

## Deliverables
In **Readme.md**, please describe how to run your feature engineering/data manipulation/data cleaning/classifier files. 

In your **writeup**, please address these key motivating questions and structure it as the following (some questions mentioned above are relisted here):

- Data Cleaning/Manipulation 
    - Outline your steps in cleaning up the text data (headlines and bodies). Try different manipulations with the text data (lemmatization, stemming, lower casing, punctuation removal, stop word removal, etc.)
- Exploratory Data Analysis (pick 2 bullet points in addition to bullet point #1)
    - **Required**: Check the distribution of unrelated/discusses/agrees/disagrees across the train/dev/test sets. Show a histogram and discuss if these distributions are roughly the same.
    - Find the 20 most common words in the headlines. Do these words make sense? Create a word cloud for these top 20 words.
    - Find the 50 most common words in the bodies. Do these words make sense? Create a word cloud for these top 50 words.
    - Discuss the general distribution of the target metric. Is the target metric balanced or unbalanced? What are the implications of this with respect to our classifier? What are some steps we can take with regards to addressing this unbalanced dataset?
    - Check the distribution of characters per headline. Then, check the distribution of characters per body. What is the median for each of these two metrics? Does this distribution resemble any statistical distribution?
    -  Repeat the previous bullet point but now use the number of words in the headline/body as the metric of interest.

- Machine Learning
    - Feature Engineering and Model Complexity
        - What features did you try? What was the intuitive reason why you picked those features?
        - What features were most predictive of the target metric? Which features didn't work well?
        - How big was your feature space? What were the steps you took to address overfitting? 
    - Model 1 (Baseline): Majority Class
        - Dicuss what your first baseline algorithm does. Does it perform well? Discuss the disparity between the unweighted accuracy and the evaluation score and why this shows that the majority class classifier is inappropriate here.
        - Give a confusion matrix
    - Model 2: Multilayer Perceptron
        - Discuss what your Multilayer Perceptron algorithm does. 
        - Parameter tune your MLP classifier. What was the optimal hidden layer size, dropout, regularization parameter, learning rate, batch size, number of epochs? Discuss any additional parameters you tuned.
        - Give a confusion matrix
    - Extension 1 (Extra credit)
        - Explain why you chose the model as your extension. How does it contrast to the MLP? What are your expectations for the classifier's performance prior to running the classifier? How does it contrast to the actual classifier's performance?
        - Parameter tune your model and discuss what parameters you tuned.
        - Give a confusion matrix
    - Extension 2 (Extra credit)
        - Repeat the process for Extension 1. For any of the extensions you can consider the following approaches:
            - other neural net models
            - logistic regression
            - random forest
            - support vector machines
            - gradient boosting trees
            - an ensemble of any of the above
            - performing a PCA to reduce dimensionality
    - Give a table comparing key performance metrics across all the models you tried (unweighted accuracy, the evaluation metric, etc.).
- Conclusions (all bullet points required)
    - If you had to pick one of the models that you tried, which one would you pick? Why? What criteria do you think are most important for model selection in this case (speed, parsimony, interpretability, accuracy, etc.)? Compare the different models you tried on these key model performance indicators.
    - If you had more time with this project, what areas would you like to explore further? 
    - What are the business implications of such a project to Facebook as well as other tech/media companies (i.e. Twitter, Google, Reddit, etc)?  
    - Your product manager asks you if you think human manual stance labelling is even necessary after this classifier you've built. What would you say? Many of the supervised learning algorithms appropriate for this problem (like logistic regression and random forest) are probabilistic in nature- how would you use this model output to make human labelling more efficient?

Things to turn in:
1. code (setup.py, mlp.py, evaluate.py, other classifier files)
2. Readme.md
3. writeup.pdf

## Recommended Readings
1. [Stop Clickbait: Detecting and Preventing Clickbaits in Online News Media](https://arxiv.org/pdf/1610.09786.pdf)
2. [From Clickbait to Fake News Detection: An Approach based on Detecting the Stance of Headlines to Articles](http://aclweb.org/anthology/W17-4215)
3. [Team Athene on the Fake News Challenge](https://medium.com/@andre134679/team-athene-on-the-fake-news-challenge-28a5cf5e017b
)
4. [Talos Targets Disinformation with Fake News Challenge Victory](http://blog.talosintelligence.com/2017/06/talos-fake-news-challenge.html)

## Appendix
1.https://www.theguardian.com/technology/2018/mar/29/facebook-fake-news-political-ad-security-us-midterms-2018
2.https://www.nytimes.com/2016/12/06/us/fake-news-partisan-republican-democrat.html
3.https://www.theverge.com/2017/12/21/16804912/facebook-disputed-flags-misinformation-newsfeed-fake-news
4.http://www.fakenewschallenge.org/