---
title: CIS 530 - Computational Linguistics - University of Pennsylvania
layout: default
img: head.png
img_link: http://emnxw.com/heads/
caption: Image credit&colon; Edwige and Xavier
active_tab: main_page 
---


<div class="alert alert-info" markdown="1">
To get a permit for CIS 530, you will need to sign up through the [CIS waitlist system](https://advising.cis.upenn.edu/index.php?id=waitlist), which will become available around November 19. Registration is not available for CIS 530 during early registration.    I will put a link on the course home page once the waitlist becomes available.  The course homepage is [http://computational-linguistics-class.org](http://computational-linguistics-class.org).

</div>


<div class="alert alert-success" markdown="1">
[Interested in being a TA for the class in Spring 2020?  Fill out this form.](https://docs.google.com/forms/d/e/1FAIpQLSepw5mcFtIGBlziBEaspUAMCzw2MkAjsej_rpOCRj0-ObS5wA/viewform?usp=sf_link)
</div>


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
: [Gradescope](XXX)

Discussion Forum
: [Piazza](XXX)

Time and place
: Spring 2020, Mondays and Wednesdays 1:30-3pm (location TBD)

Office hours
: TBD


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
