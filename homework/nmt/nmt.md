---
layout: default
img: original_greek.png
caption: That's not how it works, but it is a good idea for <a href="https://arxiv.org/pdf/1907.05791">collecting bitexts</a>
img_link: https://xkcd.com/2168/   
title: HW10 - Neural Machine Translation
active_tab: homework
release_date: 2020-04-08
due_date: 2020-04-15T11:59:59EDT
submission_link:
materials:
    -
      name: data for translation
      url: https://nlp.stanford.edu/projects/jesc/data/split.tar.gz
    -
      name: skeleton iPython notebook
      url: http://computational-linguistics-class.org/homework/nmt/cis530_nmt_skeleton.ipynb
    -
      name: Japanese sentences to translate for leaderboard submission
      url: http://computational-linguistics-class.org/homework/nmt/jp_test_sentences.txt
attribution: This assignment was developed by Li "Harry" Zhang, Liam Dugan and Chris Callison-Burch for UPenn's CIS 530 class in Spring 2020 during the Coronavirus pandemic.
readings:
-
   title: Neural Machine Translation and Sequence-to-sequence Models&#58; A Tutorial
   authors: Graham Neubig
   venue: arXiv
   type: tutorial
   url: https://arxiv.org/abs/1703.01619
-
   title: Neural Machine Translation
   authors: Graham Neubig
   venue: Guest Lecture for CIS 530, Spring 2019
   type: Guest Lecture
   url: https://upenn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=bd53c6a8-0d0a-42b1-9b15-a9d6000a4d2a   
-
   title: BLEU&#58; a Method for Automatic Evaluation of Machine Translation
   authors: Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu
   type: conference
   year: 2002
   venue: ACL
   url: https://www.aclweb.org/anthology/P02-1040.pdf
-
   title: Neural Machine Translation of Rare Words with Subword Units
   authors: Rico Sennrich, Barry Haddow, and Alexandra Birch
   type: conference
   year: 2016
   venue: ACL
   url: https://arxiv.org/pdf/1508.07909.pdf
-
   title: Encoder-Decoder Models, Attention, and Contextual Embeddings
   authors: Dan Jurafsky and James H. Martin
   venue: Speech and Language Processing (3rd edition draft)
   type: textbook
   url: https://web.stanford.edu/~jurafsky/slp3/10.pdf
-
   title: JESC&#58; Japanese-English Subtitle Corpus
   authors: Reid Pryzant, Youngjoo Chung, Dan Jurafsky and Denny Britz
   type: conference
   year: 2018
   venue: LREC
   url: https://arxiv.org/pdf/1710.10639.pdf
-
   title: Controlling Japanese Honorifics in English-to-Japanese Neural Machine Translation
   authors: Weston Feely, Eva Hasler and Adria de Gispert
   type: conference
   year: 2019
   venue: WAT
   url: https://www.aclweb.org/anthology/D19-5203.pdf
-
   title: OpenNMT&#58; Open-Source Toolkit for Neural Machine Translation
   authors: Guillaume Klein, Yoon Kim, Yuntian Deng, Jean Senellart, and Alexander M. Rush
   type: conference
   year: 2017
   venue: ACL
   url: https://www.aclweb.org/anthology/P17-4012/
-
   title: SentencePiece&#58; A simple and language independent subword tokenizer and detokenizer for Neural Text Processing
   authors: Taku Kudo and John Richardson
   type: conference
   year: 2018
   venue: EMNLP
   url: https://arxiv.org/pdf/1808.06226.pdf
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

Neural Machine Translation <span class="text-muted">: Assignment 10</span>
=============================================================

In this assignment, you are to train a Japanese to English neural machine translation (NMT) system. Unlike many of your previous assignments in this class, this assignment will be almost entirely open-ended. You will write very little code and there will be very minimal instructions so you can learn to explore like a real NLP practitioner.
You will learn to use existing packages to build a complete end-to-end NMT pipeline. This will include:
- Some preprocessing libraries to prepare the data, e.g. tokenization
- An NMT library to train an NMT model, and generate translations
- Some scripts to evaluate the translations

<!-- List the materials from the header -->
{% if page.materials %}
<div class="alert alert-info">
You can download the materials for this assignment here:
<ul>
{% for item in page.materials %}
<li><a href="{{item.url}}">{{ item.name }}</a></li>
{% endfor %}
</ul>
</div>
{% endif %}

You will be working with a Notebook in Google Colab, which offers enough computing power to be sufficient for this assignment as well as for most small-scale academic NLP research. However, [Google Colab Pro](https://colab.research.google.com/signup) is a premium service that you may want to consider if you find yourself really struggling with training time.

## Part 0: Readings
To ensure that you’re able to effectively explore on your own, it is vital to at least be familiar with the terminology of NMT systems and the general landscape of the field. Since the MT chapter of Jurafsky and Martin has yet to be written, you are instead heavily encouraged to study [this tutorial](https://arxiv.org/pdf/1703.01619.pdf) on neural machine translation written by Graham Neubig from CMU which will serve as a great conceptual overview of the field.  Prof. Neubig also gave a guest lecture on NMT for CIS 530 in 2019.  You can [watch his guest lecture online](https://upenn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=bd53c6a8-0d0a-42b1-9b15-a9d6000a4d2a).

The earlier sections in the tutorial go over material that we have already covered in this class (namely NGram, log-linear, and RNN language models) so those who want to take the opportunity to quickly review are encouraged to do so. However, if you’re confident in your mastery of those topics you should be able to start with section 7 of the tutorial which goes over encoder-decoder models and section 8 of the tutorial which goes over attention. These two sections contain the most relevant information for this assignment.

Additionally, while there is no Jurafsky and Martin chapter on Machine Translation in particular, reviewing the information on encoder-decoder models and attention in [Chapter 10](https://web.stanford.edu/~jurafsky/slp3/10.pdf) will still be very useful for not only this assignment but the upcoming BERT homework.

## Part 1: Setup Google Colab
Okay, enough reading, now onto the technical sections. If you need a refresher on what Google Colab is or how it works, revisit Assignment 6. After you have a Notebook ready, make sure you set the hardware accelerator to `GPU` under `Change Runtime Type` in the `Runtime` menu.

Next, let’s talk about storage. Whenever you start up a Colab Notebook, a virtual environment is created for you that contains some local storage space, which is nice! However, the issue is that this virtual machine gets reset a lot (when you get disconnected for a while, restart browser, session time-out, etc.) and when that happens, all your files on the virtual machine get lost.

In order to prevent this, you can mount a folder from your Google Drive into this local storage space when working with Colab to ensure that your files won’t be lost even if you disconnect. To do so, **modify and run the corresponding code block in the skeleton Notebook**.

There! You now have access to all the files in your Drive, and any changes you make to files through the Notebook will also be reflected in your Drive.

Note: In Google Colab, to run a Unix command such as `cd`, `ls`, and `pwd`, add an exclamation mark `!` before the command.

## Part 2: Data Gathering and Pre-Processing
Now that we have some persistent storage, time to fill it up with data!

### Download Data
We will be using the Japanese-English Subtitle Corpus (JESC) [(Pryzant et al., 2018)](https://arxiv.org/abs/1710.10639), developed in Dan Jurafsky’s lab at Stanford, as our source of English-Japanese parallel sentences for this assignment. This massive dataset was created by scraping several large repositories of amateur fan translations of anime, manga, and other television programs which, along with a whole bunch of novel filtering metrics, has created a dataset which has much fewer misalignments (i.e. pairs where the English and the Japanese don’t actually say the same things despite being for the same timestamp) than its contemporaries. While many of the final entries are still often misaligned by maybe a word or two, this weakness is easily made up for by its size,  making JESC the de-facto dataset for training ja-en and en-ja systems.

You can download JESC for free from [here](https://nlp.stanford.edu/projects/jesc/data/split.tar.gz), by **modifying and running the corresponding code block in the skeleton Notebook**.

(Note: In Google Colab, your virtual machine is a Unix machine. To download a file from a URL, you can use `!wget`. To unzip a tar.gz file, you can use `!tar -xzf`.  The exclamation point at the beginning of the command tells the colab notebook that you want to run a Unix command instead of Python.)

You should now have three files (train, dev, test), each of which contain the English and Japanese sentences on the same line, separated by a tab. However, for each split, the libraries that we will use expect two files, one in each language, with one sentence per line. **Follow the code in the skeleton Notebook to convert the train file to `en-train.txt`, `ja-train.txt`; convert the dev file to `en-dev.txt`, `ja-dev.txt`; convert the test file to `en-test.txt`, `ja-test.txt`.**

### Byte-Pair Encoding

For our baseline preprocessing implementation, we will use a technique called Byte Pair Encoding (BPE) [(Sennrich et al. 2016)](https://www.aclweb.org/anthology/P16-1162/). This technique allows us to define tokens with much smaller granularity than just full words, which is particularly useful in languages such as Japanese where the concept of what is and isn’t a word is not particularly well defined.

The way Byte-Pair encoding works is by starting with character-level tokens, then iteratively combining the two tokens which most frequently occur together. Continuing to do this up to a specified threshold gives us surprisingly robust tokens for words, subword units, as well as multi-word units. This technique can also help with the “unseen word problem”, as it naturally parses out the prefixes and suffixes from unseen words. (Look at 2.4.3 in textbook for more information)

You can find the original BPE implementation [here](https://github.com/rsennrich/subword-nmt) along with installation instructions. **Install it by modifying and running the corresponding code block in the skeleton Notebook.**

(Hint: For many Python packages and all packages in this assignment, you can install them with one line: `!pip install [package name]`.)

Read the “USAGE INSTRUCTIONS” on the BPE Github repo first to get yourself familiar with how the `subword-nmt` library works, then:
- Learn BPE on the training data using command `subword-nmt learn-bpe`
- Apply BPE to the training, validation, and testing data using command `subword-nmt apply-bpe`
Note: The codes_file is where the BPE information is stored. You can name it anything you like. Also, set num_operations to 10000.

You should do this once for the English data (en-train.txt, en-dev.txt, en-test.txt), and once for the Japanese Data (ja-train.txt, ja-dev.txt, ja-test.txt).

Running these preprocessing steps should take around 10-15 minutes. If you take a look at the data after BPE is finished running, you will notice the sentences look quite different once the algorithm has broken them up into smaller tokens. See if you can see a pattern in which words get broken up and which words get joined together.

## Part 3: Training and Translating
Now on to the fun part!

While you can always write your own NMT system from scratch using pyTorch (as in Assignment 6), most practitioners simply use existing libraries. In this assignment, we will be using OpenNMT. OpenNMT [(Klein et al. 2017)](https://www.aclweb.org/anthology/P17-4012/) is, as the name suggests, an open source neural machine translation library. It was released by the Harvard NLP group in December of 2016 and has generally been the de-facto baseline NMT implementation ever since due to its ease of use and generally good results.

The base system consists of a simple attention-based sequence to sequence model with support for gating, stacking, input feeding, regularization, beam search, and plenty of other bells and whistles (If that sounds like greek to you, go back over sections 7 & 8 of Graham Neubig’s [tutorial](https://arxiv.org/pdf/1703.01619.pdf)). You can find the repository [here](https://github.com/OpenNMT/OpenNMT-py).

Once you’ve finished installing the OpenNMT library, follow the instructions in “Quickstart” to preprocess/binarize your data, train a model using the train and dev set, and generate translations for your test set by **modifying and running the corresponding code block in the skeleton Notebook**. In our case, the “source” is Japanese, and the “target” is English. That’s it. You have a complete translation system!

Do be warned that training on the entirety of JESC will take you **upwards of 45 minutes**, so start early on this! You may also opt to only use 10% of the training data in your experiments to speed up your analysis.

Don’t forget to un-do the BPE tokenization for your output translations so that they actually look like normal words! You can do this using this Unix command:
`!sed -r 's/(@@ )|(@@ ?$)//g' [bpe_file] > [word_file]`

## Part 4: Evaluation
Now that you have your candidate translations, how do you test their correctness without asking a native speaker?

Well, as a first naive implementation, we can start by devising a system that gives any translation that perfectly matches the gold standard reference translation a 1 and anything else a 0. Now, there are two key issues with our naive approach.

1. Sentences can have multiple correct translations (basing our score off only one is a bad idea)
2. A binary loss function is not good for gradient descent. We need a more granular metric.

To combat both of these issues, a method called BLEU “Bilingual Evaluation Understudy” was developed by [Papineni et al. (2002)](https://www.aclweb.org/anthology/P02-1040.pdf). Instead of checking for an exact match between full sentences, BLEU score evaluates translations by checking for the number of **shared n-grams** between the candidate and reference translation. More specifically, BLEU calculates the precision of each order of n-gram (unigram, bigram, trigram, etc.) then averages those precisions together with a brevity penalty to get the final score. Thus a perfect match still gets 1.0, but only a complete mismatch (not a single word in common between the reference and candidate translation) will get a 0.0.

While using BLEU is far from perfect, it has plenty of benefits.
- It is quick and inexpensive to calculate.
- It is easy to understand.
- It is language independent.
- It correlates highly with human evaluation.
- It's popular!

That being said, the shortcomings of BLEU are readily apparent (e.g. the inability to deal with synonyms) and MT experts, [such as one particular Penn professor](https://www.cis.upenn.edu/~ccb/publications/re-evaluating-the-role-of-bleu-in-mt-research.pdf), have been complaining about them for well over a  decade now. You may want to implement a different metric such as [METEOR](https://www.cs.cmu.edu/~alavie/METEOR/pdf/Banerjee-Lavie-2005-METEOR.pdf) or [hLEPOR](http://www.mt-archive.info/10/MTS-2013-Han.pdf) for one of your extensions as it may provide you valuable insight on the types of things BLEU gets wrong (you can do so in Part 5).

**Following the skeleton notebook, modify and run the code block** to download the script for calculating BLEU using [Moses](http://www.statmt.org/moses/index.php?n=Main.HomePage), and calculate the BLEU score between your translation and the English test data.

## Part 5: Research
In this section you will explore several topics of your choosing, and **include your findings in a research section in the final report**. There is no starter code in the skeleton Notebook for this section. For full credit, you should implement **three** additions/comparisons to the baseline (for example, you can try two different metrics and a different tokenizer).  If you have time, you’re welcome to do more than three!

You should compare the results from every extension you implement in this section with the results you get from the baseline BPE. This evaluation should be done through one automatic metric such as BLEU and a manual evaluation of your system's English translations vs. the gold standard English translations. **Please include comparisons for any and all extensions you make in your report.**

Below, we list several ideas that you could do for your three additions/comparisons to the baseline system.

### Evaluation Metric
So far, we have only been using BLEU as our objective function. Consider some alternatives:
- METEOR
- ROUGE
- hLEPOR
How do we know which one is good? We can manually examine the first 20 translations generated by your baseline system and rate them by [adequacy and fluency](https://www.taus.net/academy/best-practices/evaluate-best-practices/adequacy-fluency-guidelines) on an integer scale of 0-5. After that, calculate the sentence-level score for your selected metric for these 20 translations. Finally, calculate the [Spearman’s correlation](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient) of each scale with BLEU. **Please include these results in your report.**

### Tokenizers
In our baseline, we only use Byte-Pair Encoding in our preprocessing. While it is totally fine to run BPE on untokenized text for languages like Japanese and Korean, in some cases, it can be beneficial to do language-specific tokenization **before** running BPE.

English tokenization is comparatively straightforward and can be implemented through NLTK with a package named [Moses](http://www.statmt.org/moses/?n=Moses.Baseline). On the other hand, Japanese tokenization is a bit more involved, as there are no readily apparent word boundaries such as spaces to split words on.

There are generally two main methods of tokenization in Japanese that you may choose to experiment with.
- **Dictionary-based sequence-prediction**: These models make a dictionary of words with parts of speech and find the best sequence of the words in the dictionary that matches the input character sequence. The scores for the “best” sequence can be based on scores assigned by hand (JUMAN++) or through a Hidden Markov Model (MeCab).
- **Word-boundary prediction**: These models are a bit simpler and more robust to text with many unknown words. The basic idea is that for every two adjacent characters in the input string, you predict whether there is a word boundary between the two characters, and the final result gives you a full string of words. The most widely used is KyTea written by Graham Neubig.

As a general guideline, dictionary-based tokenizers tend to produce longer and more morphologically rich tokens that are more consistent with what Japanese linguists would consider words. On the other hand, word-boundary tokenizers tend to produce much smaller and more fine-grained tokens that would, for example, separate out the stem and the ending of a conjugated verb but can sometimes go a bit overboard and tokenize too much.

All of the tokenizers mentioned above (JUMAN, MeCab, KyTea) can be installed through the conveniently named [JapaneseTokenizer pip package](https://pypi.org/project/JapaneseTokenizer/).

### WordPiece and SentencePiece Encoders
You may also consider experimenting with the **wordpiece** algorithm [(Schuster and Nakajima, 2012)](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/37842.pdf) or its newer cousin, the **sentencepiece** algorithm [(Kudo and Richardson, 2018)](https://arxiv.org/abs/1808.06226) as an alternative to Byte-Pair encoding. The wordpiece algorithm was initially developed to solve a Japanese/Korean segmentation problem for Google’s speech recognition system so it could be particularly effective for our specific use case. Also, wordpiece-style tokenizers have been seeing a growth in popularity as of late, most notably being used as the tokenizer for the now ubiquitous BERT language model [(Devlin et al. 2019)](https://arxiv.org/abs/1810.04805). If you want a more detailed explanation of how wordpiece and sentencepiece differ from BPE, check out section 2.4 of Jurafsky and Martin.

### Extra Data Sources
While JESC is plenty large enough to keep your colab notebook churning away, you may choose to incorporate even more sources of Japanese-English parallel data to further improve your NMT system. You can find a breakdown of the various sources of such data on Graham Neubig’s website [here](http://www.phontron.com/japanese-translation-data.php).

One dataset that would be particularly worthwhile to look into would be [JParaCrawl](http://www.kecl.ntt.co.jp/icl/lirg/jparacrawl/) which recently took the crown away from JESC and became the largest publically available Japanese-English parallel corpus this past November.

### Extra Credit: Formality Sensitive Machine Translation (FSMT)
One really interesting idea proposed by [Feely et al. (2019)](https://www.aclweb.org/anthology/D19-5203.pdf) to improve English to Japanese translation systems is through the use of [FSMT](https://www.aclweb.org/anthology/D17-1299/). In Japanese, all sentences include a formality marker found in the verb endings. You may choose to incorporate this knowledge into your NMT system by parsing the Japanese sentences for their formality and then prepending the corresponding <formal> or <informal> token to the beginning of your english sentences before training.

This extension would also require you to incorporate a classifier that assigns an english sentence the <formal> or <informal> tag at test time in order to avoid having to look at the test data to assign labels. This can be as simple as training a logistic regression classifier on the average of the word embeddings of each token in the sentence but feel free to get creative. You can find human annotated data for training a formality classifier at http://www.seas.upenn.edu/~nlp/resources/formality-corpus.tgz.

## Leaderboard
Once you have your final model, run your system on the [leaderboard test sentences](http://computational-linguistics-class.org/homework/nmt/jp_test_sentences.txt) **and submit your final english translations to the leaderboard**.

Your submission file should be named `translations.txt` and should consist only of the raw, not Byte-Pair Encoded English translations, one sentence per line. We will evaluate your translations using BLEU, and since we all know BLEU is not perfect, this will not constitute a lot of your grade.

We will be putting the baseline system up on the leaderboard purely for your reference. **You are not required to beat it**. It is perfectly fine to submit a system that does worse than the baseline on BLEU as long as you include thoughtful analysis in your writeup. We encourage students to not only play around with things that improve their score but also to investigate the evaluation metrics themselves and analyze how they correlate with your human evaluation.

## Deliverables
Here are the deliverables that you will need to submit:
- `writeup.pdf`
- `code.ipynb`
- `translations.txt` (to leaderboard)

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
