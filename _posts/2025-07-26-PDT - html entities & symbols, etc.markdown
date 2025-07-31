---
title: HTML entities &amp; LaTeX symbols
date: Sat Jul 26 14:05:05 PDT 2025
last_modified_at: Thu Jul 31 01:05:36 PDT 2025
permalink: /html-entities
categories:
 - blog
tags:
 - html entities
toc: true
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
usemathjax: true  # for LaTeXing
---

posted: {{ page.date| date: "%d-%b-%Y" }}
&amp;
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

<style>
table, tr, td, th {
    font-size: inherit !important;
    font-family: inherit !important;
}
</style>

$$
\newcommand{\reals}{\mathbb{R}}
\newcommand{\preals}{\reals_{+}}
\newcommand{\ppreals}{\reals_{++}}
\newcommand{\complexes}{\mathbb{C}}
\newcommand{\integers}{\mathbb{Z}}
\newcommand{\kclosure}{\overline{K}}

\newcommand{\Prob}{\mathop{\bf Prob}}
\newcommand{\Expect}{\mathop{\bf E{}}}
\newcommand{\Var}{\mathop{\bf  Var{}}}

\newcommand{\sign}{\mathop{\bf sign}}
\newcommand{\innerp}[2]{\langle{#1},{#2}\rangle} % inner product
\newcommand{\lspan}[1]{\langle{#1}\rangle} % linear span
$$

# HTML Entities

## Some symbols

Unicode symbols:

| symbol | description | HTML entities |
|:-|:-|:-|
|&#9744; &#x2610;|ballot box|&amp;#9744; or &amp;#x2610;|
|&#9745; &#x2611;|ballot box with check|&amp;#9745; or &amp;#x2611;|
|&#9746; &#x2612;|ballot box with X|&amp;#9746; or &amp;#x2612;|
|&#10003; &#x2713;|check mark|&amp;#10003; or &amp;#x2713;|
|&#10004; &#x2714;|heavy check mark|&amp;#10004; or &amp;#x2714;|

For comparison, unchecked box:


## Faces

&#x1F600;
&#x1F601;
&#x1F602;
&#x1F603;
&#x1F604;
&#x1F605;
&#x1F606;
&#x1F607;
&#x1F608;
&#x1F609;
&#x1F60A;
&#x1F60B;
&#x1F60C;
&#x1F60D;
&#x1F60E;
&#x1F60F;

&#x2605;^^&#x2605;

# LaTeX

## Math

$$\reals$$
$$\complexes$$
$$\integers$$
$$\kclosure$$
$$\Prob$$
$$\Expect$$
