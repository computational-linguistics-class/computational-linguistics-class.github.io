---
layout: default
img: HAL.png
img_link: https://en.wikipedia.org/wiki/HAL_9000
caption: I am putting myself to the fullest possible use, which is all I think that any conscious entity can ever hope to do.
title: Readings
active_tab: readings
---



<!-- Create a HTML anchor for the most recent lecture -->
{% assign anchor_created = false %}
{% capture now %}{{'now' | date: '%s'}}{% endcapture %}
<!-- End create a HTML anchor for the most recent lecture -->


The lecture schedule is subject to change as the term progresses.

<table class="table table-striped"> 
  <tbody>
    <tr>
      <th>Date</th>
      <th>Topic</th>
      <th>Readings</th>
    </tr>
{% for lecture in site.data.readings %}
<!-- Create a HTML anchor for the most recent lecture -->
{% capture lecture_date %}{{lecture.date | date: '%s'}}{% endcapture %}
{% assign lecture_date = lecture_date | plus: 0 %}
{% assign now = now | minus: 14400 %}
{% if anchor_created != true and lecture_date >= now %}
   {% assign anchor_created = true %}
<tr id="now">
   {% else %}
<tr>
{% endif %}
<!-- End create a HTML anchor for the most recent lecture -->
<td>{{ lecture.date | date: "%A, %B %-d, %Y" }}</td>
<td>
	{% if lecture.profile %}
	Company Profile:  
        {% endif %}
        {% if lecture.slides %}<a href="{{ lecture.slides }}">{{ lecture.title }}</a>
        {% else %}{{ lecture.title }}{% endif %}

	{% if lecture.speaker %}
        {% if lecture.speaker_url %} by <a href="{{ lecture.speaker_url }}">{{ lecture.speaker }}</a>
        {% else %} by {{ lecture.speaker }}{% endif %}
	{% endif %}

	{% if lecture.highlights %}
	  <ul>
	   {% for highlight in lecture.highlights %}	
	   <span class="text-muted"><li>
	   {{ highlight }}
	   </li></span>
          {% endfor %}
        {% endif %}
<td>
        {% if lecture.reading %}
          <ul class="fa-ul">
          {% for reading in lecture.reading %}
            <li>
            {% if reading.optional %}<i class="fa-li fa fa-star"> </i>
            {% else %}<i class="fa-li fa"> </i> {% endif %}
            {% if reading.url %}
            <a href="{{ reading.url }}">{{ reading.title }}</a>
            {% else %}
            {{ reading.title }} 
            {% endif %}
	    {% if reading.author %}
            by {{ reading.author }}
            {% endif %}
            </li>
          {% endfor %}
          </ul>
        {% endif %}
{% endfor %}

