---
layout: page
title: Research
subtitle: >-
  Sponsored programs at APL, and the tools and data they produced.
permalink: /research/
---

<section id="programs">
  <div class="kicker"><span class="eyebrow">Sponsored programs</span></div>
  <h2>Led or co-led at APL</h2>
  <p class="prose">
    Funded by NIH, DARPA, IARPA, and DoD.
  </p>
  {% include research-programs.html %}
</section>

<section id="software">
  <div class="kicker"><span class="eyebrow">Software &amp; datasets</span></div>
  <h2>Tools and data</h2>
  <p class="prose">
    Infrastructure, tools, and teaching artifacts — most open source, all built
    to be used by someone other than their author.
  </p>
  <div class="card-grid">
    {% for item in site.data.software %}
      {% include software-card.html item=item %}
    {% endfor %}
  </div>
</section>

<section id="recognition">
  <div class="kicker"><span class="eyebrow">Recognition &amp; service</span></div>
  <h2>Selected awards and service</h2>
  <div class="two-col">
    <div>
      <h3>Awards</h3>
      <ul class="tight">
        {% for group in site.data.cv.awards %}
          {% for a in group.items %}
            {% if a.featured %}
        <li>{{ a.title | texclean }}, {{ a.org | texclean }}{% if a.detail %} — {{ a.detail | texclean }}{% endif %} ({{ a.year | texclean }})</li>
            {% endif %}
          {% endfor %}
        {% endfor %}
      </ul>
    </div>
    <div>
      <h3>Service</h3>
      <ul class="tight">
        {% for e in site.data.cv.service %}
          {% if e.featured %}
        <li>{{ e.role | texclean }}, {{ e.title | texclean }}{% if e.org %}, {{ e.org | texclean }}{% endif %} ({{ e.year | texclean }})</li>
          {% endif %}
        {% endfor %}
      </ul>
    </div>
  </div>
</section>

<section id="collaborate">
  <div class="kicker"><span class="eyebrow">Working together</span></div>
  <h2>Collaboration</h2>
  <p class="prose">
    Open to sponsored research, consortium roles, and co-investigator work
    across connectomics, large-scale data infrastructure, and the measurement of
    human performance. Reach him at
    <a href="mailto:{{ site.email }}">{{ site.email }}</a>.
  </p>
</section>
