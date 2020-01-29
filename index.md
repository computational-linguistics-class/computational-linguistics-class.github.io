---
title: CIS 530 - Computational Linguistics - University of Pennsylvania
layout: default
img: head.png
img_link: http://emnxw.com/heads/
caption: Image credit&colon; Edwige and Xavier
active_tab: main_page 
---

<!--

<div class="alert alert-danger" markdown="1">
The course is now full. Prof. Callison-Burch emailed students on the waitlist who completed HW1 on time informing them that they would get a permit.  No other permits will be available.  
</div>
	
If you didn't get a permit for the course, but you're still hoping to get in, then you should follow these steps:
1. [Join the class Piazza](https://piazza.com/upenn/spring2020/cis530).
2. [Add yourself to Gradescope](https://www.gradescope.com/courses/80035) with the entry code __MGZXK3__.
3. [Complete Homework 1](http://computational-linguistics-class.org/assignment1.html) by Wednesday (Jan 22nd) before midnight.

If you don't turn in HW1 on time, then you won't be considered for enrollment if any additional permits become available. 
</div>
-->


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
: [Chris Callison-Burch](http://www.cis.upenn.edu/~ccb/) 

Website 
: [computational-linguistics-class.org](http://computational-linguistics-class.org/)

Homework Submission
: [Gradescope](https://www.gradescope.com/courses/80035)

Discussion Forum
: [Piazza](https://piazza.com/upenn/spring2020/cis530)

Time and place
: Spring 2020, Mondays and Wednesdays 1:30-3pm in __Annenberg 110__.
: First day of class is January 15, 2020
: Last day of class is April 29, 2020

Office hours
: Mondays 10:30am-12:30pm in the Levine 5th floor next to elevators
: Tuesdays 1:30-5 in the Levine 5th floor next to elevators
: Wednesdays 10am-12:30pm in the GRW 5th floor bump space
: Wednesdays 3-6pm in the Levine 5th floor next to elevators (multiple TAs)
: Thursdays 3-5pm GRW 5th floor bump space
: Friday 4-5pm in 3401 Walnut room 463C


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
