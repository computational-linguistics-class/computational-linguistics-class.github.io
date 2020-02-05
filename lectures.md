---
layout: default
title: Lectures
active_tab: lectures
---

<!-- Create a HTML anchor for the most recent lecture -->
{% assign anchor_created = false %}
{% capture now %}{{'now' | date: '%s'}}{% endcapture %}
<!-- End create a HTML anchor for the most recent lecture -->


<div class="alert alert-info">
You can <a href="https://upenn.hosted.panopto.com/Panopto/Pages/Sessions/List.aspx?folderID=39306b65-c02f-499b-90cb-ab3b015e2d53">watch recordings of the lecture videos online</a>.
</div>
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
      {% else if lecture.type and lecture.type == 'homework' %}
        class="primary"
      {% else if lecture.type and lecture.type == 'no_lecture' %}
        class="success"
      {% endif %}
    {% endif %}
    >

    <!-- End create a HTML anchor for the most recent lecture -->
      <td width="14%">{{ lecture.date | date: '%a, %b %-d, %Y' }}</td>
      <td width="30%">
         {{ lecture.title }} 


        {% if lecture.slides %}
          <a href="slides/{{ lecture.slides }}">[slides]</a>
        {% endif %}


        {% if lecture.recording %}
          <a href="{{ lecture.recording }}">[video] </a>
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
              {% if reading.optional %}<b>Optional:</b> {% endif %}
              {{ reading.authors }}, <a href="{{ reading.url }}">{{ reading.title }}</a> 
            <br />
          {% else %}
              {% if reading.optional %}<b>Optional</b> {% endif %}
             {{ reading.authors }}, {{ reading.title }} 
            <br />
          {% endif %}
          {% endfor %}
        {% endif %}
      </td>
    </tr>
    {% endfor %}
    
  </tbody>
</table>

