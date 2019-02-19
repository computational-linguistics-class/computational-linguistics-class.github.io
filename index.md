---
title: CIS 530 - Computational Linguistics - University of Pennsylvania
layout: default
img: head.png
img_link: http://emnxw.com/heads/
caption: Image credit&colon; Edwige and Xavier
active_tab: main_page 
---



<!-- Display an alert about upcoming homework assignments -->
{% capture now %}{{'now' | date: '%s'}}{% endcapture %}
{% for page in site.pages %}
{% if page.release_date and page.due_date %}
{% capture release_date %}{{page.release_date | date: '%s'}}{% endcapture %}
{% capture due_date %}{{page.due_date | date: '%s'}}{% endcapture %}
{% if release_date < now and due_date >= now %}
<div class="alert alert-info">
<a href="{{page.url}}">{{ page.title }}</a> has been released.  
{% if page.deliverables %}
The assignment has multiple deliverables.
<ul>
{% for deliverable in page.deliverables %}
<li>{{ deliverable.due_date | date: "%b %-d, %Y" }} - {{deliverable.description}}.</li>
{% endfor %}
</ul>
{% else %}
It is due before {{ page.due_date | date: "%I:%M%p" }} on {{ page.due_date | date: "%A, %B %-d, %Y" }}.
{% endif %}
</div>
{% endif %}
{% endif %}
{% endfor %}
<!-- End alert for upcoming homework assignments -->


Course number
: CIS 530 - Computational Linguistics 

Instructor
: [Chris Callison-Burch](http://www.cis.upenn.edu/~ccb/) - [office hours by appointment](ccb-office-hours.youcanbook.me)

Website 
: [computational-linguistics-class.org](http://computational-linguistics-class.org/)

Homework Submission
: [Gradescope](https://www.gradescope.com/courses/35473)

Discussion Forum
: [Piazza](https://piazza.com/upenn/spring2019/cis530)

Time and place
: Spring 2019, Mondays and Wednesdays 1:30-3pm (3401 Walnut room 401B)

Office hours
: Mondays 10am-noon in the Levine 5th Floor Bump Space
: Mondays 4:30pm-6:30pm in the Levine 5th Floor Bump Space
: Tuesdays 2:30pm-4:30pm in the Levine 5th Floor Bump Space
: Tuesdays 5:30pm-7:30pm in 3401 Walnut room 401B
: Thursdays 10am-11am in the GRW 5th Floor Bump Space
: Fridays 10am-noon in the Harrison Mezz


Textbook
: [Speech and Language Processing (3rd edition draft) by Dan Jurafsky and James H. Martin](https://web.stanford.edu/~jurafsky/slp3/)
: The course will have [weekly required readings](lectures.html).  

Grading
: The grading for the course will consist of:
    * 60% for weekly homework assignments 
    * 15% for quizzes about the readings
    * 25% for the final project

Collaboration Policy
: Unless otherwise noted, you are allowed to work in pairs on the homework assignment.  Both partners will receive the same grade.  The final projects will have larger groups. 

Late Day Policy
: Each student has five free "late days". Homeworks can be submitted at most two days late. If you are out of late days, then you will not be able to get credit for subsequent late assignments. One “day” is defined as anytime between 1 second and 24 hours after the homework deadline. The intent of the late day policy it to allow you to take extra time due to unforseen circumstances like illnesses or family emergencies, and for forseeable interruptions like on campus interviewing and religious holidays. You do not need to ask permission to use your late days. No additional late days are granted.
