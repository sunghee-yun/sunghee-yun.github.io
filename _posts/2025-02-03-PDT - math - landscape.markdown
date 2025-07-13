---
permalink: /math/landscape
title: Mathematical Explorer's Serendipitous Creation &ndash; A Thousand Pages of Mathematical Odyssey
date: Mon Feb  3 20:42:17 PST 2025
last_modified_at: Sun Jul 13 02:44:47 PDT 2025
categories:
 - blog
tags:
 - math
 - convex optimization
 - algebra
 - inequalities
 - abstract algebra
 - realy analysis
 - statistics
 - slides
 - document
toc: true
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
---

posted: {{ page.date| date: "%d-%b-%Y" }}
&amp;
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

<blockquote>
I aim to create a companion resource that illuminates connections between concepts
and enriches their mathematical exploration journey.
</blockquote>

# NotebookLM Podcasts

<h2>based on this blog</h2>

<audio id="podcast-1" controls>
	<source type="audio/wav" src="/resource/posts/2025-02-03-PDT - math - landscape/NotebookLM/Mathematical Beauty_ A Thousand-Page Odyssey - 01.wav">
	Your browser does not support this shorter audio element.
</audio>
<audio id="podcast-2" controls>
	<source type="audio/wav" src="/resource/posts/2025-02-03-PDT - math - landscape/NotebookLM/Sunghee's Professional Journey and Intellectual Pursuits - 01.wav">
	Your browser does not support this shorter audio element.
</audio>
<audio id="podcast-3" controls>
	<source type="audio/wav" src="/resource/posts/2025-02-03-PDT - math - landscape/NotebookLM/Sunghee's Professional Journey and Intellectual Pursuits - longer - 01.wav">
	Your browser does not support this shorter audio element.
</audio>
<audio id="podcast-4" controls>
	<source type="audio/wav" src="/resource/posts/2025-02-03-PDT - math - landscape/NotebookLM/Mathematical Beauty_ A Thousand-Page Odyssey - longer - 02.wav">
	Your browser does not support this shorter audio element.
</audio>
<audio id="podcast-5" controls>
	<source type="audio/wav" src="/resource/posts/2025-02-03-PDT - math - landscape/NotebookLM/Mathematical Beauty_ A Thousand-Page Odyssey - longer - 01.wav">
	Your browser does not support this shorter audio element.
</audio>

A Korean version

<audio id="podcast-1" controls>
	<source type="audio/wav" src="/resource/posts/2025-02-03-PDT - math - landscape/NotebookLM/Sunghee's Professional Journey and Intellectual Pursuits-kor-01.wav">
	Your browser does not support this shorter audio element.
</audio>

<h2>based on Math Codex</h2>

<audio id="podcast-5" controls>
	<source type="audio/wav" src="/resource/posts/2025-02-03-PDT - math - landscape/NotebookLM/Fundamentals of Modern Mathematics-01.wav">
	Your browser does not support this shorter audio element.
</audio>

<audio id="podcast-5" controls>
	<source type="audio/wav" src="/resource/posts/2025-02-03-PDT - math - landscape/NotebookLM/Fundamentals of Modern Mathematics-02.wav">
	Your browser does not support this shorter audio element.
</audio>

# Child blog posts

<!--span class="emph"-->
This is just the beginning of our mathematical conversation!
I'll be exploring each topic in depth through upcoming blog posts,
starting with our first deep dive into inequalities!
Stay connected for these mathematical adventures!
<!--/span-->

{% assign inequalities = site.posts | where: "permalink", "/math/inequalities" | first %}
{% assign abstract_algebra = site.posts | where: "permalink", "/math/abstract-algebra" | first %}
{% assign measure_theory = site.posts | where: "permalink", "/math/measure-theory" | first %}

- [{{ inequalities.title }}]({{ inequalities.url }})
- [{{ abstract_algebra.title }}]({{ abstract_algebra.url }})
- [{{ measure_theory.title }}]({{ measure_theory.url }})

# Math Codex {#math-codex}

- [Searching for Universal Truths - slides](/resource/fun math/fun_math.pdf) (updated on 12-Jul-2025)
- [Searching for Universal Truths - article version (converted from slides)](/resource/fun math/fun_math_article.pdf) (updated on 12-Jul-2025)

# A Journey Through Mathematical Beauty

Mathematics has always been a profound passion of mine, rooted in both its pure beauty and the joy of exploration.
This passion has guided me through increasingly intricate mathematical landscapes
&ndash; from the elegance of number theory to the captivating world of inequalities,
and onward into deeper territories of abstract algebra and analysis
&mdash; few people could ever imagine how thrilled I was when learning about the moment when the French mathematician, Lebesgue, won
the race of inventing (or finding) a new way to overcome the limits of Riemann integral in 1912,
which let all human race witness the birth of measure theory!
My journey expanded further into linear algebra and its numerical applications,
statistics (with particular focus on its measure-theoretic foundations),
and ultimately to convex optimization
&ndash; an advanced field with powerful practical applications that became the focus of my thesis work
at [Stanford University](https://www.stanford.edu/)
under supervision of [Prof. Stephen P. Boyd](https://stanford.edu/~boyd/).

What began as a personal project &mdash; creating LaTeX slides to preserve these insights for my future self &#x1F60A;
&mdash; evolved into something far more significant.
As the collection grew, I recognized its potential to serve
as a comprehensive resource for others who share this mathematical curiosity.
The resulting work, particularly the article version available in the [<span class="math-codex-header-title"></span>](#math-codex) section,
represents a synthesis of these extensive slides and research.

My goal throughout has been to create something that would resonate with advanced learners and professionals in the field.
Through careful attention to clarity in explanations and rigor in proofs, I've aimed to make these complex concepts not just accessible, but genuinely engaging for those ready to explore them deeply.

{% assign post1 = site.posts | where: "permalink", "/prajna/coincidence-vs-inevitability" | first %}
{% assign post2 = site.posts | where: "permalink", "/prajna/inevitabilities" | first %}

A profound realization recently dawned on me:
my lifelong urge to deeply understand mathematics wasn't fundamentally about mathematics at all &hellip;
It was an expression of something far more fundamental &mdash; my innate desire to glimpse universal truth.
This connection between mathematical exploration and the search for universal truth isn't just philosophical speculation;
I explore it thoroughly with concrete examples in my related posts on
[{{ post1.title }}]({{ post1.url }}) and [{{ post2.title }}]({{ post2.url }}).

# Genesis - From Personal Notes to Mathematical Odyssey

My journey began with a deceptively simple goal:
to create a structured approach for studying and retaining advanced mathematical concepts.
I started documenting the concepts that most challenged and captivated me &mdash;
from the elegant foundations of algebraic structures to the subtle depths of real analysis and measure theory.
[LaTeX](https://www.latex-project.org/) emerged as the natural choice for this endeavor,
offering the precision and beauty that mathematics demands.
What started as personal study slides unexpectedly blossomed into an extensive collection,
spanning across diverse mathematical territories I hadn't initially planned to explore.

Though my initial intention was just to create simple notes,
I found myself drawn to the rich feature set that [LaTeX](https://www.latex-project.org/) provides beyond its beautiful typography.
The powerful indexing and citation systems became invaluable tools,
allowing me to weave connections between related concepts
throughout what eventually grew into close to 1,000 pages of slides
&mdash; a scope that, as mentioned, I never anticipated!

# Evolution - Beyond Personal Understanding

As my collection of slides approached the thousand-page mark,
I began to see their potential beyond personal reference &mdash;
they could serve as a valuable resource for others on similar mathematical journeys.
This realization led to a meticulous process of organization and refinement,
transforming dense technical content into clear, comprehensive explanations
while preserving the mathematical rigor that advanced topics demand.
The challenge of balancing accessibility with depth became a driving force,
pushing me to develop presentations that would engage readers
while maintaining the precision essential to mathematical understanding.

# Bridging Minds - A Resource for Mathematical Explorers

This work is crafted specifically for advanced learners and professionals
who are deeply immersed in mathematical studies.
While the material's complexity places it beyond general audience territory,
it offers profound value for those venturing into the deeper waters of mathematics
&mdash; from the abstract realms of algebra and real analysis
to the practical domains of convex optimization, and numerical linear algebra.
My vision is to provide these dedicated minds with more than just another reference;
I aim to create a companion resource that illuminates connections between concepts
and enriches their mathematical exploration journey.

# Horizons Unfold - The Path Forward

While this work represents years of mathematical exploration and documentation,
I see it as just the beginning of a greater journey.
The mathematical landscape is vast, and there are still many territories to chart
&mdash; from deeper investigations into linear algebra and its numerical foundations
to the fascinating realm of combinatorial optimization.
My vision extends beyond just adding content;
I aim to forge a living mathematical library that grows and evolves,
serving as a trusted companion for students, educators, and professionals
who share this passion for mathematical discovery.

# The Continuing Quest for Universal Truth

Mathematics stands as humanity's most precise language for describing universal truths
&mdash; a bridge between abstract thought and practical revelation.
Through sharing this work, I hope to contribute not only to the mathematical community
but to all fields where mathematical rigor illuminates the path to discovery.
From theoretical breakthroughs to practical applications,
this resource aims to serve as a catalyst for advancement across disciplines.
I invite fellow travelers on this mathematical journey
&mdash; whether you're an advanced learner exploring these depths
or a professional seeking precise understanding &mdash;
to join in this ongoing exploration of mathematical beauty and truth.

# Continue the Exploration Together!

I deeply value dialogue with fellow mathematical explorers.
Your insights, questions, and perspectives can enrich this ongoing journey of discovery.
I welcome all comments and discussions &mdash; please reach out to me at
<sunghee.yun@gmail.com> with "universal truth" in the subject line.

<br>
[Sunghee
<br>
<br>
Mathematician, Thinker, Finder, and Truth-Seeker
<br>
Entrepreneur, Engineer, Scientist, Business Developer, Creator, and Connector](/)

<script>
const header = document.getElementById('math-codex');
const headerText = header.textContent;
document.querySelectorAll('.math-codex-header-title').forEach(element => {
    element.textContent = headerText;
});
</script>

<script>
// Function to get URL parameters
function getUrlParameter(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

// Function to auto-play audio based on URL parameter
function autoPlayAudio() {
    const audioParam = getUrlParameter('audio');
    if (audioParam) {
        const audioElement = document.getElementById(audioParam);
        if (audioElement) {
            // Scroll to the audio element
            audioElement.scrollIntoView({ behavior: 'smooth', block: 'center' });

            // Add a small delay to ensure the page has loaded
            setTimeout(() => {
                audioElement.play().catch(error => {
                    console.log('Auto-play was prevented by browser:', error);
                    // Highlight the audio element if auto-play fails
                    audioElement.style.border = '3px solid #ff6b6b';
                    audioElement.style.borderRadius = '5px';
                });
            }, 500);
			// Alternative: Simulate click on play button
			/*
			setTimeout(() => {
				audioElement.play().catch(error => {
					// If auto-play fails, show a prominent play button or notification
					const playButton = document.createElement('button');
					playButton.textContent = '▶ Click to Play Selected Audio';
					playButton.style.cssText = `
						position: fixed;
						top: 20px;
						right: 20px;
						z-index: 1000;
						background: #007cba;
						color: white;
						border: none;
						padding: 10px 20px;
						border-radius: 5px;
						cursor: pointer;
						font-size: 16px;
					`;
					playButton.onclick = () => {
						audioElement.play();
						document.body.removeChild(playButton);
					};
					document.body.appendChild(playButton);
				});
			}, 500);
			*/
        }
    }
}

// Run the function when the page loads
document.addEventListener('DOMContentLoaded', autoPlayAudio);
</script>
