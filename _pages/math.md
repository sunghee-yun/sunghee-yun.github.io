---
layout: single
title: Mathematics
permalink: /math
toc: true
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
date: Wed Jul 30 10:32:17 PDT 2025
last_modified_at: Wed Jul 30 10:32:17 PDT 2025
---

{% assign math_landscape = site.posts | where: "permalink", "/math/landscape" | first %}

{% assign inequalities = site.posts | where: "permalink", "/math/inequalities" | first %}
{% assign abstract_algebra = site.posts | where: "permalink", "/math/abstract-algebra" | first %}
{% assign measure_theory = site.posts | where: "permalink", "/math/measure-theory" | first %}
{% assign topological_spaces = site.posts | where: "permalink", "/math/topological-spaces" | first %}
{% assign absmeas = site.posts | where: "permalink", "/math/abstract-measure-theory" | first %}
{% assign measstat = site.posts | where: "permalink", "/math/measure-theoretic-statistics" | first %}
{% assign cvxopt = site.posts | where: "permalink", "/math/cvxopt" | first %}

{% assign linalg = site.posts | where: "permalink", "/math/rig/linear-algebra" | first %}

# My Math Journey

- [{{ math_landscape.title }}]({{ math_landscape.url }})
	- [{{ inequalities.title }}]({{ inequalities.url }})
	- [{{ abstract_algebra.title }}]({{ abstract_algebra.url }})
	- [{{ measure_theory.title }}]({{ measure_theory.url }})
	- [{{ topological_spaces.title }}]({{ topological_spaces.url }})
	- [{{ absmeas.title }}]({{ absmeas.url }})
	- [{{ measstat.title }}]({{ measstat.url }})
	- [{{ cvxopt.title }}]({{ cvxopt.url }})

# Rigorously

- [{{ linalg.title }}]({{ linalg.url }})
