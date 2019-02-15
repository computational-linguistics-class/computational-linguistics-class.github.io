---
layout: default
title: Quizzes
active_tab: quizzes
---

<!-- Create a HTML anchor for the most recent quiz -->
{% assign anchor_created = false %}
{% capture now %}{{'now' | date: '%s'}}{% endcapture %}
<!-- End create a HTML anchor for the most recent quiz -->

Every week we will have short take-home quizzes to test your understanding of the readings.  
<!-- 
Below is a schedule of quizzes, and what readings will be covered in them.
-->

<table class="table table-striped">
  <thead>
    <tr>
      <th>Quiz</th>
      <th>Due Date</th> 
      <th>Readings Covered By the Quiz</th>
    </tr>
  </thead>
  <tbody>
    {% for quiz in site.data.quizzes %}

    <tr class="info" >
      <td>{{ quiz.title }} </td>

      <td>{{ quiz.due_date | date: '%a, %b %-d, %Y' }}</td>

      <td>
        {% if quiz.readings %} 
          {% for reading in quiz.readings %}
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

