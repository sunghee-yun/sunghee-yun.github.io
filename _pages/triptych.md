---
date: Thu May  7 16:34:36 PDT 2026
last_modified_at: Thu May  7 16:56:00 PDT 2026
layout: single
title: Triptych
permalink: /triptych
toc: true
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
---

{: .notice--primary}
posted: {{ page.date| date: "%d-%b-%Y" }}
&amp;
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}

{% assign inevitabilities_trilogy = site.posts | where: "permalink", "/prajna/inevitabilities-trilogy/podcasts" | first %}
{% assign epistemic = site.posts | where: "permalink", "/prajna/epistemic-gap/podcasts" | first %}
{% assign existential = site.posts | where: "permalink", "/prajna/existential-trilogy/podcasts" | first %}

{% assign arbitrariness = site.posts | where: "permalink", "/prajna/coincidence-vs-inevitability" | first %}
{% assign inevitabilities = site.posts | where: "permalink", "/prajna/inevitabilities" | first %}
{% assign shadow_prices = site.posts | where: "permalink", "/prajna/glimpse-of-universal-truths-via-shadow-prices" | first %}

{% assign partial_info = site.posts | where: "permalink", "/prajna/wisdom-of-strategic-ignorance" | first %}
{% assign full_info = site.posts | where: "permalink", "/prajna/impossibility-of-full-knowledge" | first %}
{% assign shadow_price = site.posts | where: "permalink", "/prajna/glimpse-of-universal-truths-via-shadow-prices" | first %}

{% assign why_do_we_live = site.posts | where: "permalink", "/blog/PST-Why-do-we-live/" | first %}
{% assign coming_back = site.posts | where: "permalink", "/prajna/coming-back-to-the-human" | first %}
{% assign ubi = site.posts | where: "permalink", "/ai/future/ubi" | first %}

# Three Trilogy Articles

- [{{ inevitabilities_trilogy.title }}]({{ inevitabilities_trilogy.url }}){:target="_blank"} @ {{ inevitabilities_trilogy.date | date: "%d-%b-%Y" }}
	- [{{ arbitrariness.title }}]({{ arbitrariness.url }}){:target="_blank"} @ {{ arbitrariness.date | date: "%d-%b-%Y" }}
	- [{{ inevitabilities.title }}]({{ inevitabilities.url }}){:target="_blank"} @ {{ inevitabilities.date | date: "%d-%b-%Y" }}
	- [{{ shadow_prices.title }}]({{ shadow_prices.url }}){:target="_blank"} @ {{ shadow_prices.date | date: "%d-%b-%Y" }}
- [{{ epistemic.title }}]({{ epistemic.url }}){:target="_blank"} @ {{ epistemic.date | date: "%d-%b-%Y" }}
	- [{{ partial_info.title }}]({{ partial_info.url }}){:target="_blank"} @ {{ partial_info.date | date: "%d-%b-%Y" }}
	- [{{ full_info.title }}]({{ full_info.url }}){:target="_blank"} @ {{ full_info.date | date: "%d-%b-%Y" }}
	- [{{ shadow_price.title }}]({{ shadow_price.url }}){:target="_blank"} @ {{ shadow_price.date | date: "%d-%b-%Y" }}
- [{{ existential.title }}]({{ existential.url }}){:target="_blank"} @ {{ existential.date | date: "%d-%b-%Y" }}
	- [{{ why_do_we_live.title }}]({{ why_do_we_live.url }}){:target="_blank"} @ {{ why_do_we_live.date | date: "%d-%b-%Y" }}
	- [{{ coming_back.title }}]({{ coming_back.url }}){:target="_blank"} @ {{ coming_back.date | date: "%d-%b-%Y" }}
	- [{{ ubi.title }}]({{ ubi.url }}){:target="_blank"} @ {{ ubi.date | date: "%d-%b-%Y" }}
