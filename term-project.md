---
layout: default
img: estimating_time.png
caption: Don't Panic
img_link: https://xkcd.com/1658/   
title: The CIS 530 Term Project
active_tab: homework
release_date: 2018-03-01
due_date: 2018-03-03T12:00:00EST
attribution: This assignment was developed by the CIS 530 course staff.
deliverables:
    -
      description: Milestone 1
      due_date: 2018-03-14T11:00:00EST
    -
      description: Milestone 2 
      due_date: 2018-03-28T11:00:00EST
    -
      description: Milestone 3 
      due_date: 2018-04-11T11:00:00EST
    -
      description: The Full Project and Writeup
      due_date: 2018-04-18T11:00:00EST
    -
      description: The Project Presentation 
      due_date: 2018-04-18T12:00:00EST
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
{% if page.deliverables %}
The assignment has multiple deliverables.
<ul>
{% for deliverable in page.deliverables %}
<li>{{deliverable.description}} is due before {{ deliverable.due_date | date: "%I:%M%p" }} on {{ deliverable.due_date | date: "%A, %B %-d, %Y" }}.</li>
{% endfor %}
</ul>
{% else %}
This assignment is due before {{ page.due_date | date: "%I:%M%p" }} on {{ page.due_date | date: "%A, %B %-d, %Y" }}.
{% endif %}
</div>
