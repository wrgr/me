---
layout: page
title: Publications
subtitle: >-
  Peer-reviewed articles and conference proceedings, newest first. Starred
  entries are selected work; colored chips mark the domains each contribution
  serves. Invited talks and posters follow.
permalink: /publications/
---

<p class="prose">
  Also on <a href="https://scholar.google.com/citations?user={{ site.data.profiles.scholar }}">Google Scholar</a>{% if site.data.profiles.cv %}, and in the <a href="{{ site.data.profiles.cv | relative_url }}">CV (PDF)</a>{% endif %}.
</p>

<section id="papers">
  <div class="kicker"><span class="eyebrow">Articles &amp; proceedings</span></div>
  <div class="bibliography-wrap">
  {% bibliography --query @*[category=paper] %}
  </div>
</section>

<section id="talks">
  <div class="kicker"><span class="eyebrow">Invited talks</span></div>
  <div class="bibliography-wrap">
  {% bibliography --query @*[category=talk] %}
  </div>
</section>

<section id="posters">
  <div class="kicker"><span class="eyebrow">Posters</span></div>
  <div class="bibliography-wrap">
  {% bibliography --query @*[category=poster] %}
  </div>
</section>
