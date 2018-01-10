---
layout: default
title: Lectures
active_tab: lectures
---

<!-- Create a HTML anchor for the most recent lecture -->
{% assign anchor_created = false %}
{% capture now %}{{'now' | date: '%s'}}{% endcapture %}
<!-- End create a HTML anchor for the most recent lecture -->

The lecture schedule will be updated as the term progresses. 

<table class="table table-striped">
  <thead>
    <tr>
      <th>Date</th> 
      <th>Topic</th>
      <th>Required Readings</th>
    </tr>
  </thead>
  <tbody>
    {% for lecture in site.data.lectures %}

    <!-- Create a HTML anchor for the most recent lecture -->
    {% capture lecture_date %}{{lecture.date | date: '%s'}}{% endcapture %}
    {% assign lecture_date = lecture_date | plus: 0 %}
    {% assign now = now | minus: 14400 %}

    <tr
    {% if anchor_created != true and lecture_date >= now %}
      {% assign anchor_created = true %}
      id="now" 
    {% endif %}
    
    {% if lecture.type %}
      {% if lecture.type and lecture.type == 'exam' %}
        class="info" 
      {% else if lecture.type and lecture.type == 'deadline' %}
        class="warning"
      {% else if lecture.type and lecture.type == 'no_lecture' %}
        class="success"
      {% endif %}
    {% endif %}
    >

    <!-- End create a HTML anchor for the most recent lecture -->
      <td>{{ lecture.date | date: '%a, %b %-d, %Y' }}</td>
      <td>
        {% if lecture.slides %}
          <a href="{{ lecture.slides }}">{{ lecture.title }}</a>
        {% else %}
         {{ lecture.title }} 
        {% endif %}



	    {% if lecture.speaker %}
          {% if lecture.speaker_url %}
            by <a href="{{ lecture.speaker_url }}">{{ lecture.speaker }}</a> 
          {% else %} 
          by {{ lecture.speaker }}
          {% endif %}
	    {% endif %}

      </td>
      <td>
        {% if lecture.readings %} 
          {% for reading in lecture.readings %}
          {% if reading.url %}
             {{ reading.authors }}, <a href="{{ reading.url }}">{{ reading.title }}</a>
          {% else %}
             {{ reading.authors }}, {{ reading.title }}
          {% endif %}
          {% endfor %}
          <br />
        {% endif %}
      </td>
    </tr>
    {% endfor %}
    
  </tbody>
</table>

