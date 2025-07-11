---
permalink: /math/inequalities
title: Elegant Solutions, Endless Applications &ndash; The Living Art of Inequalities
date: Mon Feb  3 21:25:18 PST 2025
last_modified_at: Fri Jul 11 02:28:54 PDT 2025
categories:
 - blog
tags:
 - math
 - inequalities
 - Cauchy-Schwarz inequality
 - Jensen's inequality
 - slides
 - document
usemathjax: true
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
&hellip; inequalities aren't just tools for comparison
&ndash; they're windows into the fundamental structures of mathematical relationships.
</blockquote>

<blockquote>
Oh, I love Jensen's inequality! I've loved it ever since I met it for the first time in my life and I still love it!
</blockquote>

# NotebookLM Podcasts

<h2>based on this blog</h2>

<audio id="podcast-1" controls>
	<source type="audio/wav" src="/resource/posts/2025-02-03-PDT - math - inequalities/NotebookLM/The Living Art of Inequalities - 04.wav">
	Your browser does not support this shorter audio element.
</audio>
<audio id="podcast-2" controls>
	<source type="audio/wav" src="/resource/posts/2025-02-03-PDT - math - inequalities/NotebookLM/The Living Art of Inequalities - 03.wav">
	Your browser does not support this shorter audio element.
</audio>
<audio id="podcast-3" controls>
	<source type="audio/wav" src="/resource/posts/2025-02-03-PDT - math - inequalities/NotebookLM/The Living Art of Inequalities - 02.wav">
	Your browser does not support this shorter audio element.
</audio>
<audio id="podcast-4" controls>
	<source type="audio/wav" src="/resource/posts/2025-02-03-PDT - math - inequalities/NotebookLM/The Living Art of Inequalities - 01.wav">
	Your browser does not support this shorter audio element.
</audio>

<h2>based on Algebra Codex</h2>

<audio id="podcast-slides-1" controls>
	<source type="audio/wav" src="/resource/posts/2025-02-03-PDT - math - inequalities/NotebookLM/Universal Truths of Algebra_ Inequalities and Number Theory-02.wav">
	Your browser does not support this shorter audio element.
</audio>

<audio id="podcast-slides-2" controls>
	<source type="audio/wav" src="/resource/posts/2025-02-03-PDT - math - inequalities/NotebookLM/Universal Truths of Algebra_ Inequalities and Number Theory-01.wav">
	Your browser does not support this shorter audio element.
</audio>

# Parent blog

{% assign math_landscape = site.posts | where: "permalink", "/math/landscape" | first %}
- [{{ math_landscape.title }}]({{ math_landscape.url }})

# Algebra Codex {#algebra-codex}

- [Searching for Universal Truths - Algebra](/resource/fun math/fun_math_algebra - 2025_0709.pdf)

{% assign math_landscape = site.posts | where: "permalink", "/math/landscape" | first %}

# A Journey Through Mathematical Boundaries

Having painted the broad landscape of mathematics in my previous blog post [{{ math_landscape.title }}]({{ math_landscape.url }}),
I want to delve into the first chapter of my mathematical journey - inequalities.
While number theory has long been celebrated as the "Queen of Mathematics,"
with countless brilliant minds dedicating their lives to its exploration,
my heart was captured by a different realm – the fascinating world of inequalities.
Today, I'd like to share why this field has held such a special place in my mathematical journey.


# From Three Weeks to Three Years - A Mathematical Awakening

My romance with inequalities began around age 15,
shortly after I entered Seoul Science High School (SSHS).
I still remember that time vividly – I was among 180 students chosen from 1,400 applicants,
though unlike many of my peers who had prepared for years,
I had only spent three weeks studying for the entrance exam.<sup><a href="#footnote1" id="ref1">1</a></sup>

This unexpected success was just the beginning of my mathematical awakening.
When I first arrived at SSHS,
I was distinctly aware of the gap between myself and my classmates.
Many had already mastered advanced topics like trigonometry, calculus, algebra, and geometry,
while I was just beginning to explore these concepts.
The school had a prestigious Mathematics Olympiad (MO) circle,
but initially, I couldn't even consider joining because... I had no idea what trigonometric functions are!
However, something unexpected happened – after six months,
I was the only student personally invited by the math teacher to join the circle,
thanks to what he called "unprecedented progress" in mathematics.

# When Elegance Meets Power - The Art of Inequalities

It was during my preparation for various Mathematics Olympiad competitions – Korean MO, International MO, and South-Pacific MO – that I first encountered inequalities.
What captivated me most was their elegant simplicity.
While other mathematical approaches often required lengthy calculations or tedious differentiation, inequalities offered a more graceful path to solutions.

Let me share a concrete example that illustrates this beauty.
Consider finding the maximum value of $$x + 2y$$ where $$3x^2 + y^2 = 1$$.
That is to solve the following optimization problem

$$
\begin{align}
\mbox{maximize}\quad & x+2y
\\
\mbox{subject to}\quad & 3x^2+y^2=1
\end{align}
$$

The conventional calculus-based approach, while perfectly valid, involves several steps

<ol>
<li>
	Let $$k = x + 2y$$
</li>
<li>
	Substitute $x = k - 2y$ into the constraint equation

$$
3(k-2y)^2 + y^2=1
$$
</li>
<li>
	Solve the resulting quadratic equation

$$
13y^2 - 12ky + (3k^2-1) =0
$$
</li>
<li>
	Use the fact that the discriminant should be non-negative (because $y$ is a real number) to find the range of $x+2y$

$$
D/4 = 36k^2 - 13(3k^2-1) = 13-3k^2 \geq0
$$
</li>
</ol>

This leads to the correct answer of $$\sqrt{13/3}$$,
but there's a (way) more elegant way using so-called Cauchy-Schwarz inequality.
Recollect that the Cauchy-Schwarz inequality (in its summation form) states that

$$
(a_1^2 + ... + a_n^2)(b_1^2 + ... + b_n^2) \geq (a_1b_1 + ... + a_nb_n)^2
$$

for any $$a_i, b_i\in\mathbb{R}$$.
By cleverly choosing $$a_1 = \sqrt{3}x$$, $$a_2 = y$$, $$b_1 = 1/\sqrt{3}$$, and $$b_2 = 2$$, we get

$$
13/3 = (3x^2 + y^2)(1/3 + 4) \geq (x + 2y)^2
$$

hence the same result (as it should be)!

## Hidden beauty of this approach

What makes this solution particularly elegant isn't just its brevity
&ndash; it's how it reveals the underlying structure of the problem.
The Cauchy-Schwarz inequality isn't just a tool we happened to use;
it's telling us something fundamental about the geometry of our problem.
When we apply it, we're essentially exploiting the fact that the angle
between two vectors in a properly chosen inner product space can never exceed 90 degrees
(where, of course, here we should consider or rather imagine
angles in $$n$$-dimensional space
which simply no human (maybe few exceptions in history)
can understand properly intuitively
because we have never experience $$n$$-dimensional space where $$n$$ is greater than 3).

This geometric intuition leads us to a deeper understanding - inequalities often serve as bridges between algebra and geometry.
They're not just statements about which number is larger; they're revelations about the shape of mathematical space itself.

## Power of generalization (of the Cauchy-Schwarz inequality) {#cauchy-power-of-generalization}

Now one can argue that
&ldquo;hold on! but isn't it true that we can still solve such problem using the discriminant of the quadratic equation?&rdquo;
Unfortunately, the answer is no,
and here is where inequalities play practically useful roles
beyond its brevity and elegance.

Assume that we want to solve the following optimization problem now

$$
\begin{align}
\mbox{maximize}\quad & x+2y + z/3
\\
\mbox{subject to}\quad & 2x^2+y^2/3 + 2z^2=7
\end{align}
$$

We cannot solve this problem using the discriminant of the quadratic equation
because we will end up with a quadratic equation of *two* variables
even after the substitution.

Well, at least, we can consider geometric interpretation in 3-dimensional space
for this problem, but what about this one?

$$
\begin{align}
\mbox{maximize}\quad & x_1 +2x_2+ 3x_3 + \cdots + n x_n
\\
\mbox{subject to}\quad & n x_{1}^2+(n-1)x_{2}^2 + \cdots + 2 x_{n-1}^2 + x_n^2=n
\end{align}
$$

What if we want to solve this problem for an arbitrary $$n$$? I mean for any $$n$$?
You can't anymore have some geometric interpretation (in a laymen's sense)
because $$n$$ can be greater than 3.

Can you also solve this problem for arbitrary $$c_i$$'s and positive $$d_i$$'s?

$$
\begin{align}
\mbox{maximize}\quad & c_1 x_1 + c_2 x_2 + + \cdots + c_n x_n
\\
\mbox{subject to}\quad & d_1 x_1^2+ d_2 x_2^2 + \cdots + d_n x_n^2 = 1
\end{align}
$$

You see where I am going? <font class="emph">We can handle <i>all</i> of the above cases <i>beautifully</i>,
plus infinite other such cases as beautifully and elegantly as this!
This shows the enormous power of generalization
that inequalities can powerfully provide!</font>

Here I will show how we can do this extremely easily and utmostly elegantly using the Cauchy-Schwarz inequality
letting $$a_i = \sqrt{d_i} x_i$$ and $$b_i = c_i / \sqrt{d_i}$$
and
applying the Cauchy-Schwarz inequality
yield

$$
\begin{align}
&\left(c_1^2/d_1 + c_2^2/d_2 + \cdots + c_n^2/d_n\right)
\\
&=
\left(c_1^2/d_1 + c_2^2/d_2 + \cdots + c_n^2/d_n\right)
\left(d_1 x_1^2+ d_2 x_2^2 + \cdots + d_n x_n^2 \right)
\\
&=
\left(a_1^2 + a_2^2 + \cdots + a_n^2\right)
\left(b_1^2 + b_2^2 + \cdots + b_n^2\right)
\\
&\geq
\left(a_1 b_1 + a_2 b_2 + \cdots + a_nb_n\right)^2
\\
&=
\left(c_1 x_1 + c_2 x_2 + \cdots + c_nx_n\right)^2
\end{align}
$$

Thus, we have

$$
c_1 x_1 + c_2 x_2 + \cdots + c_nx_n
\leq
\sqrt{c_1^2/d_1 + c_2^2/d_2 + \cdots + c_n^2/d_n},
$$

hence the maximum value of  $$c_1 x_1 + c_2 x_2 + \cdots + c_nx_n$$ is,
and has just been proved to be,
$$\sqrt{c_1^2/d_1 + c_2^2/d_2 + \cdots + c_n^2/d_n}$$.
By assigning proper values to $$n$$, $$a_i$$, and $d_i$$,
this readily solves all the above problems at once!<sup><a href="#footnote2" id="ref2">2</a></sup>

# Another Tale of Two Paths - The AM-GM Journey

Let us start from a bit similar, but different optimization problem

$$
\begin{align}
\mbox{maximize}\quad & xy
\\
\mbox{subject to}\quad & 3x^2 + y^2 = 1
\end{align}
$$

First, we can solve this *unelegantly* by starting with letting $$xy=k$$.

1. Substituting $$k/y$$ for $$x$$ gives $$3k^2/y^2 + y^2 = 1$$,
1. which is equivalent to $$(y^2)^2 - y^2 + 3k^2=0$$.
1. Now the discriminant being non-negative implies $$D=1-12k^2\geq0$$,
1. hence $$xy\leq 1/\sqrt{12} = 1/2\sqrt{3}$$!

Now consider the classic arithmetic mean-geometric mean (AM-GM) inequality,
a simplest version of which,
probably the first one we saw in high school,
states that

$$
\frac{a+b}{2} \geq \sqrt{ab}
$$

for any nonnegative $$a$$ and $$b$$.

Now if we let $$a=3x^2\geq 0$$ and $$b=y^2\geq0$$ and plug these in the AM-GM inequality,
we have

$$
\frac{1}{2} = \frac{3x^2+y^2}{2} \geq \sqrt{3x^2y^2} = \sqrt{3} |xy|
$$

hence

$$
xy \leq |xy| \leq 1/2\sqrt{3}
$$

obtaining the very same result once again (way) more elegantly and simply.

## Power of generalizations (of the AM-GM inequality) {#am-gm-power-of-generalization}

Now consider general cases for which the *generalness* or the level of generalization
seems way more severe than those shown
in [<span class="cauchy-power-of-generalization-header-title"></span>](#cauchy-power-of-generalization)!

$$
\begin{align}
\mbox{maximize}\quad & xyz
\\
\mbox{subject to}\quad & 3x^5 + y^2 + 2z^3= 1
\\
& x,y, z\geq0
\end{align}
$$

Not only do we have more than 2 variables,
but also the exponents on the shoulders of variables vary.

So probably AM-GM inequality dealing with more than 2 variables would not suffice to solve this problem,
which is

$$
\frac{a_1+a_2+\cdots+a_n}{n} \geq (a_1a_2\cdots a_n)^{1/n}
$$

And yes, we cannot solve the problem using this extension only.
But we can further generalize our AM-GM inequality into

$$
w_1a_1 + w_2a_2 + \cdots + w_na_n \geq a_1^{w_1} a_2^{w_2} \cdots a_n^{w_n}
$$

which holds for any $$a_i\geq0$$ and $$w_i>0$$ with $$w_1+w_2+\cdots+w_n=1$$.<sup><a href="#footnote3" id="ref3">3</a></sup>

Now we have some very powerful tool which not only can solve the above problem,
but also infinite other variations!

First let us tackle the above one.
Let $$n=3$$, $$a_1=5\cdot 3x^5$$, $$a_2 = 2 \cdot y^2$$, $$a_3 = 3\cdot 2z^3$$,
$$w_1 = (1/5)/(1/5+1/2+1/3)$$,
$$w_2 = (1/2)/(1/5+1/2+1/3)$$,
and
$$w_3 = (1/3)/(1/5+1/2+1/3)$$.
Then $$w_1+w_2+w_3=1$$,
hence we have

$$
\begin{align}
30/31
&= (3x^5+y^2+2z^3)/(1/5+1/2+1/3)
= w_1a_1 + w_2a_2 + w_3a_3
\\
&\geq w_1^{a_1} \cdot w_2^{a_2} \cdot w_3^{a_3}
= (15^{1/5} \cdot 2^{1/2} \cdot 3^{1/3} \cdot xyz)^{30/31}
\end{align}
$$

thus

$$
xyz \leq
(30/31)^{31/30} / (15^{1/5} \cdot 2^{1/2} \cdot 3^{1/3})
$$

that is,
the maximum value of $$xyz$$ is (30/31)<sup>31/30</sup> / (15<sup>1/5</sup> &sdot; 2<sup>1/2</sup> &sdot; 3<sup>1/3</sup>).
Another way of saying this is that,
with all the combinations of the nonnegative triplets $$(x,y,z)$$
that satisfy $$3x^5 + y^2 + 2z^3 =1$$,
the maximum possible value of $$xyz$$
is (30/31)<sup>31/30</sup> / (15<sup>1/5</sup> &sdot; 2<sup>1/2</sup> &sdot; 3<sup>1/3</sup>).

<!--Isn't it amazing that we can do this calculation this easily?
It's a rule of thumb that
to obtain an answer of this complication,
one may well have to go through very complicated process of calculations,
but in this case, it's not true.
Why? I don't know. But AM-GM inequality just did the magic!-->

The elegance of this solution is striking. Conventional wisdom suggests that a problem of this complexity should require intricate calculations and multiple steps. Yet here, the AM-GM inequality cuts through the complexity like a beam of light through fog, revealing the answer with remarkable simplicity. While we can prove why this works, there's something almost magical about how a single inequality can distill pages of calculus into one elegant step. This is mathematics at its utmost beauty &ndash; where complexity yields to simplicity, and where a deeper understanding reveals shorter paths to truth.

Another way of saying this is &hellip;
There's something remarkable about this solution's simplicity. One might expect that finding this maximum value would demand pages of calculus and careful computations. Instead, the AM-GM inequality offers us a direct path to the answer, elegant in its brevity and powerful in its insight. This is one of those beautiful moments in mathematics where a deeper understanding doesn't add complexity – it strips it away, revealing the essential truth beneath.

Now one *could* readily see that we can solve the following problem now<sup><a href="#footnote4" id="ref4">4</a></sup>

$$
\begin{align}
\mbox{maximize}\quad & x_1^{e_1} x_2^{e_2} \cdots x_n^{e_n}
\\
\mbox{subject to}\quad & g_1x_1^{f_1} + g_2x_2^{f_2} + \cdots + g_nx_n^{f_n}=1
\\
& x_1,x_2, \ldots, x_n \geq0
\end{align}
$$

for any $$e_i,f_i,g_i>0$$ *very elegantly* as below!

Letting $$a_i = (g_i f_i / e_i)\: x_i^{f_i}$$ and $$w_i = (e_i/f_i)/\sum_{j=1}^n (e_j/f_j)$$ gives

$$
\begin{align}
\left( \sum_{i=1}^n g_ix_i^{f_i} \right) &/ \left( \sum_{i=1}^n e_i/f_i \right)
= \sum_{i=1}^n w_ia_i
\\
&\geq \prod_{i=1}^n a_i^{w_i}
= \left( \prod_{i=1}^n (g_if_i/e_i)^{(e_i/f_i)} x_i^{e_i} \right)^{1/\sum_{i=1}^n (e_i/f_i)}
\end{align}
$$

hence

$$
\left( \sum_{i=1}^n g_ix_i^{f_i} \right)^{\sum_{i=1}^n (e_i/f_i)}
\geq
\left( \sum_{i=1}^n e_i/f_i \right)^{\sum_{i=1}^n (e_i/f_i)}
\prod_{i=1}^n (g_if_i/e_i)^{(e_i/f_i)}
\prod_{i=1}^n x_i^{e_i}
$$

thus

$$
\prod_{i=1}^n x_i^{e_i}
\leq
\left(
\left(\sum_{i=1}^n e_i/f_i\right)^{\sum_{i=1}^n (e_i/f_i)}
\prod_{i=1}^n (g_if_i/e_i)^{(e_i/f_i)}
\right)^{-1}!
$$

<font class="emph">Can you not see the beauty as well as ultimate power of inequalities,
and for that matter, the power of mathematics?</font>

# The Art of Mathematical Extension

What truly fascinates me about inequalities is how they naturally lead us to powerful generalizations,
the different types of generalizations that I mentioned above
([here](#cauchy-power-of-generalization) and [here](#am-gm-power-of-generalization)).

Let's return to our friend, the Cauchy-Schwarz inequality. What begins as a simple relationship between two vectors extends beautifully into infinite-dimensional spaces, becoming a cornerstone of functional analysis and quantum mechanics.

Consider how the inequality evolves

<ol>
<li>
	For finite vectors

	$$
		\left(\sum_{i=1}^n a_i^2\right) \left(\sum_{i=1}^n b_i^2\right)
		\geq \left(\sum_{i=1}^n a_i b_i \right)^2
	$$
</li>
<li>
	For complex finite vectors
	$$
		\left(\sum_{i=1}^n |a_i|^2\right) \left(\sum_{i=1}^n |b_i|^2\right)
		\geq \left|\sum_{i=1}^n a_i b_i^\ast \right|^2
	$$
</li>
<li>
	For functions $f,g: \mathbb{R} \to \mathbb{C}$

	$$
		\left(\int_{-\infty}^\infty |f(t)|^2 dt\right) \left(\int_{-\infty}^\infty |g(t)|^2 dt\right)
		\geq \left|\int_{-\infty}^\infty f(t) g^\ast(t) \right|^2
	$$
</li>
<li>
	For <i>abstract</i> (possibly) infinite dimensional inner product spaces

	$$
		\langle u, u\rangle
		\langle v, v\rangle
		\geq
		\left|\langle u, v\rangle\right|^2
	$$
</li>
</ol>

Each step in this progression reveals new insights while preserving the essential geometric intuition about angles and projections.
This is mathematical beauty at its finest – the same fundamental truth manifesting itself at different levels of abstraction.

<!--(Note that each item subsumes its predecessor (if exists),
that is, 2. subsumes 1., 3. subsumes 2., and 4. subsumes 3.
In other words,
1., 2., and 3. are special cases of 2., 3., and 4. respectively.)-->
By the way,
this progression isn't just a collection of related formulas
&ndash; it reveals a beautiful hierarchy where each level subsumes its predecessors.
The finite-dimensional vector form (1) emerges as a special case of the complex vector form (2)
when we restrict ourselves to real numbers.
Similarly, the complex vector form (2) is encompassed by the function space version (3)
when we view vectors as functions taking values at discrete points.
Finally, the abstract inner product space formulation (4) provides the most general framework,
from which all previous forms can be derived by choosing specific inner product spaces.
This nested structure showcases the deep unity underlying these seemingly different mathematical contexts,
revealing how the same fundamental principle manifests at increasingly abstract levels.

## The First Level - Multiple Variables

The beauty of inequalities becomes even more apparent
when we see how naturally they extend to higher dimensions.
What started with our simple optimization problem involving two variables
reveals its true elegance as we extend to 3, 4, or even $$n$$ variables.
Each step upward in dimensionality maintains the same fundamental principles
while uncovering new layers of mathematical structure.

## The Second Level - Arbitrary Exponents

As we venture beyond simple squares and cubes into the realm of arbitrary powers,
most traditional calculus-based approaches become increasingly cumbersome.
Yet inequalities maintain their grace and power,
continuing to provide elegant solutions that reveal deeper patterns in the mathematical structure.

## The Ultimate Generalization - Abstract Spaces

Here we reach perhaps the most beautiful aspect of inequalities
&ndash; their extension into abstract mathematical spaces.
The Cauchy-Schwarz inequality takes on its most powerful form,
maintaining its geometric intuition
while providing insights into the fundamental nature of mathematical structures themselves.


# Jensen's inequality

The journey through inequalities wouldn't be complete
without exploring one of the most powerful and versatile inequalities in mathematics
&ndash; Jensen's inequality!

The journey through inequalities wouldn't be complete without exploring one of the most profound and far-reaching results in mathematics – Jensen's inequality. My first encounter with it remains etched in my memory, a moment of mathematical epiphany that occurred during a special summer camp for Korean Mathematics Olympiad awardees. There, as a high school student with the rare privilege of learning from university professors, I experienced one of those transformative moments that every mathematician *may* cherishes.
&mdash; How would I know it, though? I'm not them.

<p>
<font class="emph">Oh, I love Jensen's inequality!
I've loved it ever since I met it for the first time in my life and I still love it!</font>
</p>

<!--I vividly remember the first moment I met it. &#x1F60D;
It was when I was being taught
by math professors of universities in Korea
at the so-called math summer camp
where the Korean Mathematics Olympiad awardees
were invited to join.
Yes, I had priviliges to be taught
by university math professors when I was a mere high schooler!
&ndash; I was truly lucky.-->

I can still vividly recall the wave of excitement that washed over me as the true significance of Jensen's inequality began to crystallize in my mind. "This subsumes everything! This is so profound!" I remember thinking. "It's not just another inequality – it's the master key that unlocks them all! We don't need separate proofs for AM-GM inequality or Cauchy-Schwarz inequality
&ndash; they're all special cases of this beautiful result!"<sup><a href="#footnote5" id="ref5">5</a></sup>

While Cauchy-Schwarz illuminates the geometry of inner product spaces and AM-GM reveals the interplay between arithmetic and geometric means, Jensen's inequality ventures deeper. It unveils something truly fundamental about the nature of convexity itself – a property that lies at the heart of optimization theory and manifests throughout mathematics in surprisingly diverse ways.

## The Fundamental Insight

At its core, Jensen's inequality tells us something remarkably intuitive yet profound -
the average value of convex function values is always greater than or equal to the function value of the average value.
More precisely, for convex function $$f:X\to \mathbb{R}$$

$$
f(w_1x_1 + w_2x_2 + \cdots + w_nx_n) \leq w_1f(x_1) + w_2f(x_2) + \cdots + w_nf(x_n)
$$

<i>i.e.</i>,

$$
f\left(\sum_{i=1}^n w_ix_i\right) \leq \sum_{i=1}^n w_i f(x_i)
$$

where $$w_i\geq0$$ and $$\sum_{i=1}^n w_i=1$$.

The beauty of this inequality lies not just in its mathematical form, but in its geometric interpretation. Imagine drawing any chord on a convex function's graph – the function values will always lie below or on the chord. This simple geometric truth leads to surprisingly powerful mathematical results.

<div class="img-container">
<img width="80%" src="/resource/posts/2025-02-03-PDT - math - inequalities/jensen-3-768x342.png">
</div>
<figcaption>
$f$ is convex,
$\lambda_1, \lambda_2 \geq0$,
and
$\lambda_1 + \lambda_2 = 1$.
</figcaption>

## Jensen's inequality implies AM-GM inequality

One of the most elegant aspects of Jensen's inequality is how it provides a more general framework that includes AM-GM as a special case.
Consider $$f:\mathbb{R}_{++} \to \mathbb{R}$$ defined by $$f(x) = -\log(x)$$.
This function is convex, hence,
for any $$a_i>0$$ and $$w_i\geq0$$ with $$\sum_{i=1}^n w_i = 1$$,
we have

$$
-\log(w_1a_1 + \cdots + w_na_n) \leq -w_1\log(a_1) - \cdots - w_n\log(a_n)
$$

hence

$$
w_1a_1 + w_2a_2 + \cdots + w_na_n \geq a_1^{w_1}a_2^{w_2}\cdots a_n^{w_n}.
$$

And there it is – our weighted AM-GM inequality emerges effortlessly!
This isn't just a mathematical coincidence; it reveals a deeper truth about how these inequalities are connected through the fundamental concept of convexity.

## Jensen's inequality implies Cauchy-Schwarz inequality, too!

It turns out that the Jensen's inequality subsumes not only the AM-GM inequality,
but the Cauchy-Schwarz inequality, too!

For any $$a_i,b_i\in\mathbb{R}$$,
define $$x_i = a_i/b_i$$ and $$w_i = b_i^2/\sum_{j=1}^n b_j^2$$.
Then because $$w_i\geq0$$, $$\sum_{i=1}^n w_i=1$$,
and $$f(x)=x^2$$ is convex,
the Jensen's inequality implies

$$
\left(\frac{\sum_{i=1}^n a_ib_i}{\sum_{i=1}^n b_i^2} \right)^2
=\left(\sum_{i=1}^n w_ix_i \right)^2
\leq
\sum_{i=1}^n w_ix_i^2
=
\left(\frac{\sum_{i=1}^n a_i^2}{\sum_{i=1}^n b_i^2}\right)
$$

hence

$$
\left(\sum_{i=1}^n a_ib_i \right)^2
\leq
\left(
\sum_{i=1}^n a_i^2
\right)
\left(
\sum_{i=1}^n b_i^2
\right).
$$

This elegant derivation once again reveals the deep interconnection between these seemingly different mathematical tools.
What I find particularly fascinating is how Jensen's inequality serves as a unifying principle - a mathematical "master key" that unlocks multiple fundamental inequalities through different applications.
This hierarchical structure, where one powerful principle generates many specific results, exemplifies the beautiful economy of mathematics - the most profound truths often lead to the widest array of consequences.

# From Theory to Practice - Inequalities in Action

What makes inequalities particularly compelling is their ubiquity in real-world applications. They appear naturally in

- Optimization problems in economics
- Error bounds in statistics
- Uncertainty principles in physics
- Information theory and coding
- Algorithm analysis in computer science

In each case, inequalities don't just give us numerical bounds – they provide insight into the fundamental limitations and trade-offs inherent in these systems.

<div class="img-container">
<img src="/assets/images/math/algebra/cauchy-schwarz-ineq-01.png">
</div>

# Unreasonable effectiveness of mathematics

What I find most captivating about inequalities is how they often provide
the shortest path between seemingly unrelated mathematical concepts.
They're like mathematical shortcuts that, when properly understood, reveal the hidden connections in mathematics.
This reminds me of what Eugene Wigner called "the unreasonable effectiveness of mathematics"
&ndash; these elegant relationships seem to hint at some deeper truth about the structure of mathematical reasoning itself.

It is quite coincidental that
I recently posted
the paper "[The Unreasonable Effectiveness of Data](/papers#unreasonable-effectiveness-of-data)" written by Google Research guys
in the context of AI

# A Personal Reflection

Looking back at my mathematical journey, I realize that inequalities taught me something beyond mathematics. They taught me that sometimes the most powerful approach isn't to solve for an exact answer, but to understand the boundaries of what's possible. They showed me that constraints, rather than limiting us, often guide us toward deeper understanding.

<div class="img-container">
<img src="/assets/images/math/algebra/math-girl-01.png">
</div>

# Your Turn - An Invitation to Mathematical Discovery

Mathematics is often seen as a solitary pursuit,
but I've found that the most profound insights come from sharing and discussing ideas with others.
I invite you to explore these mathematical landscapes yourself.
Whether you're a student encountering these concepts for the first time,
an educator looking for fresh perspectives,
or a fellow enthusiast seeking mathematical beauty,
there's always more to discover in the world of inequalities.

Your questions and insights might lead us to new ways of understanding these fundamental mathematical relationships.
What hidden connections will you uncover?
What elegant proofs might you discover?
Let's continue this mathematical journey together.

I encourage you to share your thoughts, questions, and feedback.
Together, we can continue to learn, grow, and appreciate the beauty and utility of mathematics.
Please email me to <sunghee.yun@gmail.com> with any types of comments with subject starting with <span class="emph">**universal truth**!</span>

[Sunghee
<br>
<br>
Mathematician, Beauty-Enjoyer, and Fun-Seeker
<br>
Entrepreneur, Engineer, Scientist, Business Developer, Creator, and Connector](/)

---

*This blog post explores one territory from my
[{{ math_landscape.title }}]({{ math_landscape.url }})
— a serendipitous creation that began as personal LaTeX slides and evolved
into a comprehensive exploration of mathematical beauty and universal truth.
Inequalities represents just one of many interconnected mathematical landscapes
including abstract algebra, measure theory, convex optimization, and topology.*

<hr>
<ol>
<li id="footnote1">
	Well, I had heard about these so-called Science High Schools, but had thought they had nothing to do with me
	because they were for <i>smart</i> dudes whereas I was <i>NOT</i>.
	But just three weeks before the SSHS entrance exam in 1990,
	my mom brought home an application form for SSHS which she received from her friend
	whose son went to Gyunggi Science High School, Gyunggi-do, South Korea, a few years ago and now a student of
	Korea Advanced Institute of Science &amp; Technology (KAIST), Daedeok Innopolis, Daejeon, South Korea,
	so I solved problem books designed for preparing students for Science High Schools
	for the three weeks while being 100% sure that there was no way for me to get into that.
	Thus, it was myself if no others who was shockingly surprised to learn that I passed the entrance exam!
	Looking back, I believe this period marked the awakening of my mathematical potential,
	triggered perhaps by the intensive mental stimulation during those three weeks of preparation.
	Or maybe not. Who knows?
	&nbsp;<a href="#ref1">↩</a></li>
<li id="footnote2">
	By the way,
	mathematically strictly speaking,
	or even not-that-strictly speaking &#x2605;^^&#x2605;,
	to claim that the value on the right-hand-side is achievable,
	we should show the equality is achievable,
	which we can (easily).
	Hence, we should keep stating the conditions for the equality being held
	wherever necessary.
	However, for the terseness of this blog post,
	I'll omit it throughout this document.
	Just trust me on that! :)
	&nbsp;<a href="#ref2">↩</a></li>
<li id="footnote3">
	You can see how we can derive this general AM-GM inequality
	from a very simple case of $(a+b)/2 \geq \sqrt{ab}$
	in the slides in <a href="#algebra-codex"><span class="algebra-codex-header-title"></span></a>.
	You can also see Jensen's inequality <i>elegantly</i>
	implies this most general form of AM-GM inequality,
	which is another layer of the beauty we can observe in the line of our arguments here.
	&nbsp;<a href="#ref3">↩</a></li>
<li id="footnote4">
	Mathematically (in this case),
	solving the maximization problem
	is equivalent to solving the following minimization problem:
	&nbsp;<a href="#ref4">↩</a></li>

	$$
	\begin{align}
	\mbox{minimize}\quad & g_1x_1^{f_1} + g_2x_2^{f_2} + \cdots + g_nx_n^{f_n}
	\\
	\mbox{subject to}\quad & x_1^{e_1} x_2^{e_2} \cdots x_n^{e_n} = 1
	\\
	& x_1,x_2, \ldots, x_n \geq0
	\end{align}
	$$
<li id="footnote5">
	This initial insight was later reinforced and deepened during my studies with Prof. Stephen Boyd at Stanford University seven years later, where I gained an even deeper appreciation for the role of convexity in optimization theory, hence AI,
	and everything else!
	&nbsp;<a href="#ref5">↩</a></li>
</ol>

<script>
const algebra_header = document.getElementById('algebra-codex');
const algebra_headerText = algebra_header.textContent;
document.querySelectorAll('.algebra-codex-header-title').forEach(element => {
    element.textContent = algebra_headerText;
});
const cauchy_header = document.getElementById('cauchy-power-of-generalization');
const cauchy_headerText = cauchy_header.textContent;
document.querySelectorAll('.cauchy-power-of-generalization-header-title').forEach(element => {
    element.textContent = cauchy_headerText;
});
</script>

