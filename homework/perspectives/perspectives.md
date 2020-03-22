---
layout: default
img: for_the_sake_of_argument.png
caption: Identifying supporting and opposing arguments is a great way to annoy your friends.
img_link: https://xkcd.com/1432/
title: HW12 - Perspective Detection
active_tab: homework
release_date: 2020-04-22
due_date: 2020-04-29T11:59:59EDT
submission_link: 
attribution: This assignment was developed by Sihao Chen and Chris Callison-Burch for UPenn's CIS 530 class in Spring 2020 during the Coronavirus pandemic.
materials:
    - 
      name: XXX
      url: https://xxx
readings:
-
   title: Seeing Things from a Different Angle&colon; Discovering Diverse Perspectives about Claims
   authors: Sihao Chen, Daniel Khashabi, Wenpeng Yin, Chris Callison-Burch and Dan Roth
   venue: NAACL
   type: conference
   year: 2019
   url: https://www.cis.upenn.edu/~ccb/publications/discovering-diverse-perspectives.pdf
   page_count: 16
   id: discovering-diverse-perspectives
   abstract: One key consequence of the information revolution is a significant increase and a contamination of our information supply. The practice of fact checking won’t suffice to eliminate the biases in text data we observe, as the degree of factuality alone does not determine whether biases exist in the spectrum of opinions visible to us. To better understand controversial issues, one needs to view them from a diverse yet comprehensive set of perspectives. For example, there are many ways to respond to a claim such as “animals should have lawful rights”, and these responses form a spectrum of perspectives, each with a stance relative to this claim and, ideally, with evidence supporting it. Inherently, this is a natural language understanding task, and we propose to address it as such. Specifically, we propose the task of substantiated perspective discovery where, given a claim, a system is expected to discover a diverse set of well-corroborated perspectives that take a stance with respect to the claim. Each perspective should be substantiated by evidence paragraphs which summarize pertinent results and facts. We construct PERSPECTRUM, a dataset of claims, perspectives and evidence, making use of online debate websites to create the initial data collection, and augmenting it using search engines in order to expand and diversify our dataset. We use crowdsourcing to filter out the noise and ensure high-quality data. Our dataset contains 1k claims, accompanied with pools of 10k and 8k perspective sentences and evidence paragraphs, respectively. We provide a thorough analysis of the dataset to highlight key underlying language understanding challenges, and show that human baselines across multiple subtasks far outperform machine baselines built upon state-of-the-art NLP techniques. This poses a challenge and opportunity for the NLP community to address.
   bibtex: |
      @inproceedings{Chen-et-al:2019:NAACL,
       author = {Sihao Chen and Daniel Khashabi and Wenpeng Yin and Chris Callison-Burch and Dan Roth},
       title = {Seeing Things from a Different Angle&colon; Discovering Diverse Perspectives about Claims},
       booktitle = {The 2019 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL 2019)},
       month = {June},
       year = {2019},
       address = {Minneapolis, Minnesota},
       url = {http://www.cis.upenn.edu/~ccb/publications/discovering-diverse-perspectives.pdf}
       } 
-
   title: PerspectroScope&colon; A Window to the World of Diverse Perspectives
   authors: Sihao Chen, Daniel Khashabi, Chris Callison-Burch and Dan Roth
   venue: ACL
   type: demo
   year: 2019
   url: https://www.cis.upenn.edu/~ccb/publications/perspectroscope-demo.pdf
   page_count: 6
   id: perspectroscope-demo
   abstract: This work presents PERSPECTROSCOPE, a web-based system which lets users query a discussion-worthy natural language claim, and extract and visualize various perspectives in support or against the claim, along with evidence supporting each perspective. The system thus lets users explore various perspectives that could touch upon aspects of the issue at hand. The system is built as a combination of retrieval engines and learned textualentailment-like classifiers built using a few recent developments in natural language understanding. To make the system more adaptive, expand its coverage, and improve its decisions over time, our platform employs various mechanisms to get corrections from the users. PERSPECTROSCOPE is available at github.com/CogComp/perspectroscope.  A brief video of the system is available at youtube.com/watch?v=MXBTR1Sp3Bs.
   bibtex: |
      @inproceedings{Chen-Khashabi-et-al:2019,
       author = {Sihao Chen and Daniel Khashabi and Chris Callison-Burch and Dan Roth},
       title = {PerspectroScope&colon; A Window to the World of Diverse Perspectives},
       booktitle = {Proceedings of The 57th Annual Meeting of the Association for Computational Linguistics (ACL) demo session},
       year = {2019},
       address = {Florence, Italy},
       url = {http://www.cis.upenn.edu/~ccb/publications/comparison-of-diverse-decoding-methods-from-conditional-language-models.pdf}
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

Perspective Detection <span class="text-muted">: Assignment 12</span>
=============================================================


<div class="alert alert-danger">
Warning: this assignment is not ready yet.  It may still have updates before it is released.  Check with your instructor before you start working on this assignment.
</div>

Description goes here. 




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


