---
layout: page
title: Writing &amp; press
subtitle: >-
  The argument that capability is a designable property of a system — and where
  the work has been covered.
permalink: /writing/
---

<section id="argument">
  <div class="kicker"><span class="eyebrow">Writing &amp; ideas</span></div>
  <h2>The argument</h2>
  <p class="prose">
    One claim runs across the domains: what people can do inside a system is a
    designable, measurable property of that system — and treating it that way
    changes what you build, what you measure, and who gets to do the work.
  </p>
  <div class="card-grid">
    {% for w in site.data.writing %}
      {% include writing-card.html item=w %}
    {% endfor %}
  </div>
</section>

<section id="press">
  <div class="kicker"><span class="eyebrow">In the press</span></div>
  <h2>Coverage</h2>
  <div class="card-grid">
    {% for m in site.data.media %}
      {% include media-card.html item=m %}
    {% endfor %}
  </div>
</section>
