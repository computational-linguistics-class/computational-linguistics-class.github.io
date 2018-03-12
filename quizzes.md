---
layout: default
title: Quizzes
active_tab: quizzes
---

<!-- Create a HTML anchor for the most recent lecture -->
{% assign anchor_created = false %}
{% capture now %}{{'now' | date: '%s'}}{% endcapture %}
<!-- End create a HTML anchor for the most recent lecture -->

Every Wednesday we will have short in-class quiz to test your understanding of the readings.  Below is a schedule of quizzes, and what readings will be covered in them.

<table class="table table-striped">
  <thead>
    <tr>
      <th>Quiz</th>
      <th>Date</th> 
      <th>Readings Covered By the Quiz</th>
    </tr>
  </thead>
  <tbody>
    {% for lecture in site.data.lectures %}

    {% if lecture.type and lecture.type == 'exam' %}
    <tr class="info" >
      <td>{{ lecture.title }} </td>

      <td>{{ lecture.date | date: '%a, %b %-d, %Y' }}</td>

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
    {% endif %}
    {% endfor %}
    
  </tbody>
</table>

