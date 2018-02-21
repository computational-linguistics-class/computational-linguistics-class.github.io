---
title: CIS 530 - Computational Linguistics - University of Pennsylvania
layout: default
img: HAL.png
img_link: https://en.wikipedia.org/wiki/HAL_9000
caption: I am putting myself to the fullest possible use, which is all I think that any conscious entity can ever hope to do. 
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
{% for deliverable in page.deliverables %}
The {{deliverable.description}} is due before {{ deliverable.due_date | date: "%I:%M%p" }} on {{ deliverable.due_date | date: "%A, %B %-d, %Y" }}.  
{% endfor %}
{% else %}
It is due before {{ page.due_date | date: "%I:%M%p" }} on {{ page.due_date | date: "%A, %B %-d, %Y" }}.
{% endif %}
</div>
{% endif %}
{% endif %}
{% endfor %}
<!-- End alert for upcoming homework assignments -->


<!-- Display annoucement -->
<div class="alert alert-success" markdown="1">
We would like your feedback on how CIS 530 is going so far.  We'd like to know what is working for you, and what changes you'd like to see us make.  Please fill out [this survey](https://docs.google.com/forms/d/e/1FAIpQLSfSOUZi1Ffnp0Zvek9DvB8KP4rVLiXooNJ4pH7426FqQCcr_A/viewform?usp=sf_link).
</div>
<!-- End annoucement -->


<!-- Display annoucement -->
<div class="alert alert-info" markdown="1">
Today at 3pm there will be a [memorial service for Aravind Joshi](http://www.seas.upenn.edu/media/in-memoriam-joshi.php), who founded Penn's CIS department and who was a luminary in computational linguistcs.   There will be a [live stream of the memorial](https://www.youtube.com/watch?v=85qthqUmCp8) if you'd like to listen in to hear how he impacted so many people's careers and research.
</div>
<!-- End annoucement -->


Course number
: CIS 530 - Computational Linguistics 

Instructor
: [Chris Callison-Burch](http://www.cis.upenn.edu/~ccb/)

Discussion Forum
: [Piazza](https://piazza.com/upenn/spring2018/cis530)

Time and place
: Spring 2018, Mondays and Wednesdays 12-1:30, Towne 217

Office hours
: Mondays 3-5pm (3401 Walnut room 401B)
: Tuesdays 3-6pm (3401 Walnut room 401B)

Textbook
: [Speech and Language Processing (3rd edition draft) by Dan Jurafsky and James H. Martin](https://web.stanford.edu/~jurafsky/slp3/)
: The course will have [weekly required readings](lectures.html).  

Grading
: The grading for the course will consist of:

    * 60% for weekly homework assignments 
    * 20% for in-class quizzes about the readings
    * 20% for the final project


Collaboration Policy
: Unless otherwise noted, you are allowed to work in pairs on the homework assignment.  Both partners will receive the same grade.  The final projects will have larger groups. 

Late Day Policy
: Each student has five free "late days".  Homeworks can be submitted at most two days late.  If you are out of late days, then you will not be able to submit your homework. One "day" is defined as anytime between 1 second and 24 hours after the homework deadline. The intent of the late day policy it to allow you to take extra time due to unforseen circumstances like illnesses or family emergencies, and for forseeable interruptions like on campus interviewing and religious holidays.  You do not need to ask permission to use your late days.  No additional late days are granted. 

Missing classes on quiz days 
: To allow for absences on the days that we give an in-class quiz, all students may drop their 3 lowest scoring quizzes. 
