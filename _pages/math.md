---
layout: single
title: Mathematics
permalink: /math
toc: true
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
date: Wed Jul 30 10:32:17 PDT 2025
last_modified_at: Sun Aug  3 19:40:58 PDT 2025
---

{% assign math_landscape = site.posts | where: "permalink", "/math/landscape" | first %}

{% assign algebra = site.posts | where: "permalink", "/math/inequalities" | first %}
{% assign aalgebra = site.posts | where: "permalink", "/math/abstract-algebra" | first %}
{% assign mtheory = site.posts | where: "permalink", "/math/measure-theory" | first %}
{% assign topspaces = site.posts | where: "permalink", "/math/topological-spaces" | first %}
{% assign absmeas = site.posts | where: "permalink", "/math/abstract-measure-theory" | first %}
{% assign measprob = site.posts | where: "permalink", "/math/measure-theoretic-statistics" | first %}
{% assign cvxopt = site.posts | where: "permalink", "/math/cvxopt" | first %}

{% assign rig_linalg = site.posts | where: "permalink", "/math/rig/linear-algebra" | first %}
{% assign rig_aalgebra = site.posts | where: "permalink", "/math/rig/abstract-algebra" | first %}
{% assign rig_mtheory = site.posts | where: "permalink", "/math/rig/measure-theory" | first %}
{% assign rig_topspaces = site.posts | where: "permalink", "/math/rig/topological-spaces" | first %}
{% assign rig_absmeas = site.posts | where: "permalink", "/math/rig/abstract-measure-theory" | first %}
{% assign rig_measprob = site.posts | where: "permalink", "/math/rig/measure-theoretic-treatment-of-statistics" | first %}
{% assign rig_cvxopt = site.posts | where: "permalink", "/math/rig/convex-optimization" | first %}
{% assign rig_all_math = site.posts | where: "permalink", "/math/rig/everything" | first %}

# My Math Journey

- [{{ math_landscape.title }}]({{ math_landscape.url }})
	- [{{ algebra.title }}]({{ algebra.url }})
	- [{{ aalgebra.title }}]({{ aalgebra.url }})
	- [{{ mtheory.title }}]({{ mtheory.url }})
	- [{{ topspaces.title }}]({{ topspaces.url }})
	- [{{ absmeas.title }}]({{ absmeas.url }})
	- [{{ measprob.title }}]({{ measprob.url }})
	- [{{ cvxopt.title }}]({{ cvxopt.url }})

# Rigorously

- [{{ rig_all_math.title }}]({{ rig_all_math.url }})
- [{{ rig_linalg.title }}]({{ rig_linalg.url }})
- [{{ rig_aalgebra.title }}]({{ rig_aalgebra.url }})
- [{{ rig_mtheory.title }}]({{ rig_mtheory.url }})
- [{{ rig_topspaces.title }}]({{ rig_topspaces.url }})
- [{{ rig_absmeas.title }}]({{ rig_absmeas.url }})
- [{{ rig_measprob.title }}]({{ rig_measprob.url }})
- [{{ rig_cvxopt.title }}]({{ rig_cvxopt.url }})
