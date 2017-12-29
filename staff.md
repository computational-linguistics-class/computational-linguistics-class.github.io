---
layout: default
title: CIS 121 Staff
active_tab: staff
---

<div class="container-fluid">
  <div class="row">
  {% for staff in site.data.staff %}
      <div class="col-lg-4 col-md-6 col-xs-12" style="margin-bottom: 20px; height: 350px;">
        <ul class="list-unstyled">
          <li>
            {% if staff.pic %}
              <img src="assets/img/staff/{{ staff.pic }}" class="img-circle" style="height: 100%; width: 100%; max-height: 250px; max-width: 250px">
            {% else %}
              <img src="assets/img/kermit.png" class="img-circle" style="height: 100%; width: 100%; max-height: 250px; max-width: 250px">
            {% endif %}
          </li>
          {% if staff.url %}
            <li><b><a href="{{ staff.url }}">{{ staff.name }}</a></b></li>
          {% else %}
            <li><b>{{ staff.name }}</b></li>
          {% endif %}
          {% if staff.extra_title %}<li><em>{{ staff.extra_title }}</em></li>{% endif %}
          <li><b>Email:</b> <code>{{ staff.email }}</code></li>
       	  {% if staff.office_hours %}<li><b>Office Hours:</b> {{ staff.office_hours | inline_markdownify }}</li>{% endif %}
          {% if staff.location %}<li><b>Location:</b> {{ staff.location | inline_markdownify }}</li>{% endif %}
        </ul>
      </div>
    {% endfor %}
  </div>
</div>
