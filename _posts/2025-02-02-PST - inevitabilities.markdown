---
title: "Beyond Coincidence &ndash; Mathematical Truths That Transcend All Possible Universes"
date: Sun Feb  2 14:43:34 PST 2025
last_modified_at: Tue Jul 29 03:20:58 PDT 2025
permalink: /prajna/inevitabilities
categories:
 - blog
tags:
 - inevitabilities
toc: true
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
usemathjax: true  # for LaTeXing
---

<!--tags: {% for tag in page.tags %} <a href="/tags/#{{ tag }}">{{ tag }}</a> {% endfor %}
<br>
cats: {% for category in page.categories %} <a href="/categories/#{{ category }}">{{ category }}</a> {% endfor %}-->

posted: {{ page.date| date: "%d-%b-%Y" }}
&amp;
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

<blockquote>
<a href="#inevitability-of-gaussian-dist">
<span class="emph" id="quote:inevitability-of-gaussian-dist">
We see Gaussian distributions everywhere not because our universe happens to be constructed that way,
but because any universe with randomness and aggregation would necessarily exhibit the same patterns.
</span>
</a>
</blockquote>

<blockquote>
<a href="#glimpse-into-deepest-logical-structures">
<span class="emph" id="quote:glimpse-into-deepest-logical-structures">
Understanding this inevitability doesn't just help us appreciate the elegant mathematics underlying probability theory; it offers us a glimpse into the deepest logical structures that shape reality at the most fundamental level.
</span>
</a>
</blockquote>

<blockquote>
<a href="#universe-has-no-choice-but-sinusoidal">
<span class="emph" id="quote:universe-has-no-choice-but-sinusoidal">
&hellip; and as we'll see, sinusoidal functions are the only possible <i>eigenfunctions</i> of any such system. This isn't just a mathematical curiosity; it's a window into why the universe had no choice but to encode wave phenomena in the language of trigonometry.
</span>
</a>
</blockquote>

<blockquote>
<a href="#deeper-mathematical-necessity-for-sinusoidal-waves">
<span class="emph" id="quote:deeper-mathematical-necessity-for-sinusoidal-waves">
&hellip; Maxwell's equations
don't arbitrarily impose sinusoidal solutions on electromagnetic phenomena.
Rather, they emerge from a deeper mathematical necessity.
</span>
</a>
</blockquote>

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
$$

# NotebookLM Podcasts

- [11:51](https://notebooklm.google.com/notebook/16049e9c-6cee-4a8b-b8b5-d805bb6ecd0f/audio)
- [12:04](https://notebooklm.google.com/notebook/0074c597-e262-465c-88c3-197ee48b5652/audio)
- [13:26](https://notebooklm.google.com/notebook/58bc83a2-542e-4938-9d8e-d678bc541f11/audio)

{% assign post = site.posts | where: "permalink", "/prajna/coincidence-vs-inevitability" | first %}

Unlike what I discuss in <a href="{{ post.url }}">{{ post.title }}</a>,
here I discuss the inevitabilities that I have found or rather identified,
which are true not only in our universe
but in any universe,
or rather for that matter,
it does not have to be a universe.

# The Gaussian Distribution &ndash; Why "Normal" is Actually Inevitable

<!--div class="img-container">
<img style="max-width: 75%;" src="/resource/inevitability-vs-arbitrariness/gaussian/lots-of-gaussian-distributions-in-3d.png">
</div-->

Walk into any statistics classroom, flip open any data science textbook, or peek under the hood of most machine learning algorithms,
and you'll find the same ubiquitous bell-shaped curve staring back at you.
The Gaussian distribution—also known as the normal distribution—appears so frequently in nature and human affairs that we've literally named it "normal."
But is this dominance merely a convenient mathematical fiction, or does it reflect something deeper about the structure of reality itself?

The answer lies in one of the most remarkable theorems in all of mathematics: the [Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem). Far from being an arbitrary choice or a quirk of our mathematical toolkit, the [Gaussian distribution](https://en.wikipedia.org/wiki/Normal_distribution) emerges as an inevitable consequence of how randomness behaves when it accumulates. This isn't just mathematical elegance—it's a fundamental truth that transcends our universe.

Unlike the physical constants I explored in my previous post on [Arbitrariness vs Inevitability]({{ post.url }})&mdash;where
Newton's gravitational constant $G$ or the specific exponent in inverse square laws might be contingent features of our particular universe—the normal distribution represents pure mathematical inevitability. The Gaussian curve would emerge in *any* possible universe where randomness exists, even in alternate realities with completely different physical laws. In fact, we don't need universes at all for this truth to hold; it flows directly from the logical structure of probability itself, as universal and inevitable as prime numbers.

## The Central Limit Theorem &ndash; Where Chaos Becomes Order

In probability theory, the [Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem) states that, under appropriate conditions, the distribution of a normalized version of the sample mean converges to a [standard normal distribution](https://en.wikipedia.org/wiki/Normal_distribution#Standard_normal_distribution). This holds even if the original variables themselves are not [normally distributed](https://en.wikipedia.org/wiki/Normal_distribution).

The Central Limit Theorem states the following:
<blockquote>
Let $\{X_i\}_{i=1}^\infty$ be <a href="https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables">independent, identically distributed (i.i.d.)</a> random variables
with $\Expect X_i  = \mu$ and $\Var X_i =\sigma^2$. Then

\begin{equation}
\label{eq:clt}
Z_n = \sum_{i=1}^n \frac{X_i-\mu}{\sqrt{n}\sigma}
\end{equation}

converges in distribution to $\mathcal{N}(0,1)$ as $n$ goes to $\infty$.
</blockquote>

Let that sink in for a moment. You can start with *any* collection of random variables—whether they follow uniform distributions, exponential distributions, or even bizarre custom distributions with multiple peaks and valleys. Add enough of them together, and their sum will inexorably march toward the familiar bell curve. It's as if mathematics itself has a built-in organizing principle that transforms chaos into predictable patterns.

This is profoundly different from the physical laws we encounter in nature. While we might ask whether Newton's law of universal gravitation could have an exponent of 3 instead of 2 (and I argued that the exponent 2 might itself have geometric inevitability), or whether Einstein's $$E=mc^2$$ could have a different proportionality constant, no such questions arise for the Central Limit Theorem. The bell curve doesn't depend on the specific physical constants of our universe, the peculiarities of biological evolution, or the accidents of cosmic history.

The theorem serves as a cornerstone of probability theory because it implies that probabilistic and statistical methods designed for normal distributions can be applied to countless problems involving other types of distributions. But beyond its practical utility lies something more profound: the [Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem) reveals that the Gaussian distribution isn't just mathematically convenient—it's mathematically *inevitable*.

Sometimes the theorem feels almost too good to be true, like discovering that the messy complexity of the real world secretly follows elegant mathematical laws. However, unlike the curious coincidences between geometry and physics that I explored in my discussion of inverse square laws in <a href="{{ post.url }}">{{ post.title }}</a>,
the [Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)
represents unqualified inevitability. It emerges from the fundamental logic of probability itself, requiring no physical substrate whatsoever.

As fantastic as this mathematical inevitability appears, it raises an even deeper question: *why* should adding random variables together produce such orderly results? The answer reveals something profound about the nature of information, entropy, and the hidden mathematical structures that govern randomness itself—structures as universal as the geometric facts that make π appear in the area of circles, yet somehow even more fundamental.

## Proof of Central Limit Theorem boils down to three simple facts

Here
we will first clearly see
why the Central Limit Theorem *has to* hold;
it really boils down to surprisingly simple facts!<sup><a href="#footnote1" id="ref1">1</a></sup>

- A smooth function can be well approximated by the quadratic polynomial (backed by [Taylor's theorem](https://en.wikipedia.org/wiki/Taylor%27s_theorem#Taylor's_theorem_in_one_real_variable)), *i.e.*, if $f:\reals\to\reals$ is twice-differentiable at $a\in\reals$,
there exists $h:\reals\to\reals$ such that

$$
	f(x) = f(a) + f^\prime(a)(x-a) + \frac{1}{2} f^{\prime\prime}(a) (x-a)^2 + h(x)(x-a)^2
$$

and

$$
	\lim_{x\to a} h(x) = 0.
$$

- The definition of $e$, *i.e.*,

\begin{equation}
\label{eq:def-napier-constant}
	e = \lim_{n\to\infty} \left(1+\frac{1}{n}\right)^n
\end{equation}

- The characteristic function of Gaussian $\mathcal{N}(\mu,\sigma)$
is

\begin{equation}
\label{eq:char-fcn-gaussian}
	e^{it\mu - \frac{1}{2}\sigma^2t^2}.
\end{equation}

(Refer to [the list of characteristic functions of some distributions](https://en.wikipedia.org/wiki/Characteristic_function_(probability_theory)#Examples)).

Now let's see why this is the case!

### Characteristic function

The [characteristic function](https://en.wikipedia.org/wiki/Characteristic_function_(probability_theory))
of a random variable $X\in\reals$
is denoted by $\varphi_X:\reals\to\complexes$
and defined by

$$
\varphi_X(t) = \Expect e^{itX}.
$$

Note that

$$
\varphi_X'(t) = i\Expect X e^{itX}
\;
\&
\;
\varphi_X''(t) = -\Expect X^2 e^{itX}
$$

<!--
$$
\varphi_X'(t) = i\Expect (X e^{itX})
\;
\&
\;
\varphi_X''(t) = -\Expect (X^2 e^{itX})
$$

$$
\varphi_X'(t) = i\Expect \left(X e^{itX}\right)
\;
\&
\;
\varphi_X''(t) = -\Expect \left(X^2 e^{itX}\right)
$$
-->

thus

$$
\Expect X = -i \varphi_X'(0)
\;
\&
\;
\Expect X^2 = - \varphi_X''(0).
$$

Now let $X,Y\in\reals$ be two (statistically) independent random variables.
Then the [characteristic function](https://en.wikipedia.org/wiki/Characteristic_function_(probability_theory))
of $X+Y$ is

$$
\begin{eqnarray*}
\varphi_{X+Y}(t)
	&=&
		\Expect e^{it(X+Y)}
\\
	&=&
		\int_{-\infty}^\infty
		\int_{-\infty}^\infty
		f_{X,Y}(x,y) e^{it(x+y)} dx dy
\\
	&=&
		\int_{-\infty}^\infty
		\int_{-\infty}^\infty
		f_X(x) f_Y(y) e^{it(x+y)} dx dy
\\
	&=&
		\left(
			\int_{-\infty}^\infty f_X(x) e^{itx} dx
		\right)
		\left(
			\int_{-\infty}^\infty f_Y(y) e^{ity} dy
		\right)
\\
	&=&
		\varphi_X(t) \varphi_Y(t)
\end{eqnarray*}
$$

that is,
the characteristic function of $X+Y$
is the product of the two individual characteristic functions of $X$ and $Y$ respectively.
Repeatedly applying this,
we can easily reach the conclusion that
for $n$ independent random variables $X_1,\ldots,X_n$,
the characteristic function of $Z = \sum_{i=1}^n X_i$
is

$$
\varphi_Z(t)
	=
		\prod_{i=1}^n \varphi_{X_i}(t).
$$

Now let $Y_i^{(n)} = (X_i-\mu)/\sqrt{n}\sigma$ in \eqref{eq:clt}.
Then

$$
Z_n = Y_1^{(n)} + \cdots + Y_n^{(n)}.
$$

Since $Y_i^{(n)}$ for $1\leq i\leq n$ are i.i.d.,
$\varphi_{Y_i^{(n)}}:\reals\to\complexes$ are the same for all $1\leq i\leq n$.
If we let $\varphi_{n}:\reals\to\complexes$ denote this quantity,
the characteristic function of $Z_n$ is

\begin{equation}
\label{eq:char-fcn-zn}
\varphi_{Z_n}(t)
	=
		\prod_{i=1}^n \varphi_{Y_i^{(n)}}(t) = \left(\varphi_{n}(t)\right)^n.
\end{equation}

### Taylor's theorem

Let $\tilde{Y_i} = (X_i-\mu)/\sigma$.
Then
[Taylor's theorem](https://en.wikipedia.org/wiki/Taylor%27s_theorem#Taylor's_theorem_in_one_real_variable)
implies

$$
\varphi_\tilde{Y_i}(t)
	=
		\varphi_\tilde{Y_i}(0)
		+ \varphi_\tilde{Y_i}'(0)t
		+ \frac{1}{2} \varphi_\tilde{Y_i}^{\prime\prime}(0) t^2
		+ o(t^2)
	=
		1 - t^2/2 + o(t^2)
$$

since $\Expect \tilde{Y_i} = 0$ and $\Expect \tilde{Y_i}^2 = 1$
where $o(\cdot)$ denotes the [little-o notation](https://en.wikipedia.org/wiki/Big_O_notation#Little-o_notation).
Thus

\begin{equation}
\label{eq:taylor-polynomial-char-fcn}
\varphi_n(t)
	=
		\Expect e^{it(X_i-\mu)/\sqrt{n}\sigma}
<!--
	=
		\Expect e^{i(t/\sqrt{n}) \tilde{Y_i}}
-->
	=
		\varphi_\tilde{Y_i}(t/\sqrt{n})
	=
		1 - t^2/2n + o(t^2/n^2)
\end{equation}

### Definition of $e$

The [definition of $e$](https://en.wikipedia.org/wiki/E_(mathematical_constant)#Definitions)
\eqref{eq:def-napier-constant},
\eqref{eq:char-fcn-zn},
and
\eqref{eq:taylor-polynomial-char-fcn}
imply that

$$
\lim_{n\to\infty} \varphi_{Z_n}(t)
	=
		\lim_{n\to\infty}
		\left(
			1 - t^2/2n + o(t^2/n^2)
		\right)^n
	=
		e^{-t^2/2}
$$

Thus [Lévy's continuity theorem](https://en.wikipedia.org/wiki/L%C3%A9vy_continuity_theorem)
and \eqref{eq:char-fcn-gaussian}
imply that

$$
Z_n \Rightarrow \mathcal{N}(0,1)
$$

*i.e.*,
$Z_n$ [converges in distribution](/math/measure-theoretic-statistics#the-hierarchy-of-convergence)
to $\mathcal{N}(0,1)$,
hence the proof!

## The profound implications of mathematical inevitability

What makes this result so philosophically striking is its universality. The Central Limit Theorem doesn't depend on the specific physical constants of our universe, the particular chemical composition of our planet, or even the existence of matter itself. It emerges purely from the logical structure of probability and addition—operations so fundamental that any conceivable intelligence capable of counting would eventually discover them.

Consider this thought experiment: imagine a civilization of pure information beings existing in a digital realm with no physical substrate whatsoever. Even these entities, if they developed concepts of randomness and aggregation, would inevitably arrive at the same bell-shaped curve. The Gaussian distribution transcends not just our universe but the very concept of physical reality itself.

This inevitability reveals something profound about the relationship between mathematics and existence. While the physical laws I explored in my previous post on [Arbitrariness vs Inevitability]({{ post.url }}) might be contingent features of our particular cosmic circumstances, the Central Limit Theorem represents a deeper tier of truth—one that exists in the realm of pure logical necessity.

Hence in a sense, this mathematical truth doesn't even require any universe to exist, or any intelligent beings to discover it. The Central Limit Theorem represents a timeless logical necessity—it would have been true even before the [Big Bang](https://en.wikipedia.org/wiki/Big_Bang) (if such a concept as "before" has meaning), and it remains true independent of whether time, space, or physical reality exist at all. Unlike physical constants that might depend on the specific configuration of our cosmos, this theorem exists in the realm of pure logical structure, as inevitable as the fact that 2+2=4 or that prime numbers have no divisors other than 1 and themselves.

This places the Gaussian distribution in a remarkable category: truths that are not just universal across all possible universes, but truths that transcend the very concept of universe entirely. They exist in what we might call the space of logical necessity—a realm where mathematical relationships hold not because of any physical substrate, but because their denial would lead to logical contradiction.

The mathematical proof we've just examined demonstrates why this inevitability holds with such iron-clad certainty. The emergence of the Gaussian distribution from the Central Limit Theorem isn't a happy accident or a convenient approximation—it's the inevitable consequence of three fundamental mathematical facts: the nature of smooth functions (Taylor's theorem), the definition of the mathematical constant $e$, and the characteristic function of Gaussian random variables.<sup><a href="#footnote2" id="ref2">2</a></sup> These building blocks are so basic to mathematics that any mathematical framework sophisticated enough to handle probability would necessarily contain them.

## From chaos to cosmos - the universal organizing principle

Perhaps most remarkably, the Central Limit Theorem reveals that randomness itself contains a hidden organizing principle. No matter how chaotic, unpredictable, or wildly distributed your initial random variables might be, their collective behavior inexorably marches toward the same elegant bell curve. It's as if mathematics itself has a built-in tendency toward order—a cosmic preference for the Gaussian distribution that transcends any particular physical implementation.

This stands in fascinating contrast to the apparent arbitrariness of many physical phenomena. While we might wonder why Newton's gravitational constant has the specific value it does, or why electromagnetic forces follow inverse square laws rather than inverse cube laws, no such questions arise for the Central Limit Theorem. There's no "Gaussian constant" that could have been different, no alternative bell-shaped curve that some alternate universe might have discovered instead.

The ubiquity of the normal distribution in nature—from the heights of human populations to the thermal motion of gas molecules, from measurement errors in scientific instruments to the fluctuations of financial markets—now reveals itself not as a series of coincidences, but as manifestations of this deeper mathematical truth.
<a href="#quote:inevitability-of-gaussian-dist">
<span id="inevitability-of-gaussian-dist">
We see Gaussian distributions everywhere not because our universe happens to be constructed that way, but because any universe with randomness and aggregation would necessarily exhibit the same patterns.
</span>
</a>

## The bridge between mathematical and physical reality

This inevitability of the Gaussian distribution also illuminates [the mysterious effectiveness of mathematics in describing the natural world](https://en.wikipedia.org/wiki/The_Unreasonable_Effectiveness_of_Mathematics_in_the_Natural_Sciences). When physicists model complex systems using normal distributions, they're not imposing an arbitrary mathematical framework onto reluctant physical phenomena. Instead, they're recognizing that physical processes involving the aggregation of many random effects *must* conform to this mathematical truth, regardless of the underlying physical details.

The Central Limit Theorem thus serves as a bridge between the realm of pure mathematical necessity and the contingent world of physical reality. It shows us that some aspects of our universe's behavior are inevitable not because of the specific physical laws that govern matter and energy, but because of deeper logical structures that would constrain any possible universe where counting, adding, and randomness exist.

In this sense, the normal distribution represents perhaps the purest example of what I call mathematical inevitability—truths so fundamental that they transcend not just the specific features of our universe, but the very concept of physical existence itself.
<!--Or rather even beyond existence whether or not it's physical!-->
<a href="#quote:glimpse-into-deepest-logical-structures">
<span id="glimpse-into-deepest-logical-structures">
Understanding this inevitability doesn't just help us appreciate the elegant mathematics underlying probability theory; it offers us a glimpse into the deepest logical structures that shape reality at the most fundamental level.
</span>
</a>

# Sine Waves - The Mathematical Language of Linear Reality

(Hence, you really should study hard trigonometric functions in high school! &#x2605;^^&#x2605;)

Turn on a radio, observe light propagating through space, or watch ripples spread across a pond—in each case, you're witnessing the same fundamental mathematical truth &ndash; nature speaks in sine waves. But why? Why should the universe choose this particular mathematical function to carry energy, information, and disturbances across space and time?

The answer reveals another profound inevitability, one that emerges not from the specific equations of electromagnetism or acoustics, but from something far more fundamental &ndash; the mathematical structure of reality itself. Just as the Gaussian distribution emerges inevitably from the logic of probability and aggregation, sinusoidal waves emerge inevitably from the most basic properties we could expect any uniform space to possess.

The key insight lies in recognizing that space-time itself acts as what mathematicians call a <span class="emph">Linear Time-Invariant (LTI) system</span>&mdash;<a href="#quote:universe-has-no-choice-but-sinusoidal"><span id="universe-has-no-choice-but-sinusoidal">and
as we'll see, sinusoidal functions are the only possible <i>eigenfunctions</i> of any such system. This isn't just a mathematical curiosity; it's a window into why the universe had no choice but to encode wave phenomena in the language of trigonometry.
</span>
</a>

## Linear time-invariant systems - the mathematical framework of uniform space

A linear time-invariant (LTI) system is any system $$H$$ that satisfies two fundamental properties that we might naturally expect from uniform, homogeneous space.

- **Linearity** &ndash; If you combine two inputs linearly, you get the linear combination of their outputs.

$$
	H(af + bg) = aH(f) + bH(g)
$$

- **Translation Invariance** &ndash; The laws remain the same everywhere—if you delay an input by some time $$\tau$$, the output is delayed by exactly the same amount.

$$
	(Hf)(t-\tau) = H(f(t-\tau))
$$

These properties might seem abstract, but they encode something profound about the nature of space itself. Linearity captures the principle of superposition—that disturbances can be added together without interfering with each other's individual behavior. Translation invariance captures the homogeneity of space—that the laws of physics work the same way here as they do there, now as they did then.

Any medium that possesses these properties—whether it's electromagnetic fields propagating through the vacuum, sound waves traveling through air, or quantum probability amplitudes evolving through space-time—must necessarily behave as an LTI system.

<!--
The linear time-invariant (LTI) systems $$L$$ is a system satisfying the following two properties:

\begin{equation}
\label{eq:linearity}
H(a f + b g) = a H(f) + b H(g)
\end{equation}

\begin{equation}
\label{eq:time-invariance}
(Hf)(t-\tau) = H (f(t-\tau))
\end{equation}

Here $$f$$ and $$g$$ are functions of time
and
$$a$$ and $$b$$ are scalars, *e.g.*, real or complex numbers.

- The equation \eqref{eq:linearity} says the output of the system of the sum of two inputs
is the sum of the two outputs
and when an input is multiplied by a scalar,
the output is the same quantity multiplied by that scalar.
In other words, it implies the <span class="emph">linearity</span> of the system.
- The equation \eqref{eq:time-invariance} says if the input is delayed by some amount $$\tau$$,
the output is exactly the same, but delayed by exactly the same amount,
*i.e.*, it implies the <span class="emph">time-invariance</span> of the system.
-->

### Discrete-time LTI systems

First suppose that the system being considered is a discrete-time system,
that is,
we assume that $$f:\integers \to K$$
where $$K$$ is some [field](/math/abstract-algebra#fields---the-realm-of-perfect-division)
(*e.g.*, $$\reals$$ or $$\complexes$$).
Then any such $$f$$ can be expressed as

$$
f(t) = \sum_{k=-\infty}^\infty f(k) \delta(t-k)
$$

where $$\delta: \integers \to \{0,1\}$$ is
[the Kronecker delta function](https://en.wikipedia.org/wiki/Kronecker_delta),
*i.e.*,

$$
\delta(t)
=
\left\{\begin{array}{ll}
	1 &\mbox{if } t=1
	\\
	0 &\mbox{otherwise}
\end{array}\right.
$$

Then the time-invariance and linearity imply that
for a LTI system $$H$$

\begin{equation}
\label{eq:lti-op}
H(f(t))
= \sum_{k=-\infty}^\infty f(k) H(\delta(t-k))
= \sum_{k=-\infty}^\infty f(k) h(t-k)
\end{equation}

where $$h = H(\delta)$$
is the output of the system $$H$$ when the input is the Kronecker delta function $$\delta$$,
which is called <span class="emph">impulse response<span> of $$H$$.

This means for any (discrete-time) LTI system,
you can fully characterize the output of any input to the system
if you know the impulse response,
that is,
the output of the system when the input is the Kronecker delta function!

The operation on the right-hand-side (RHS) of \eqref{eq:lti-op} is called
(as a binary operation of two functions) <span class="emph">convolution</span> (of $$f$$ and $$h$$)
and typically the symbol $$\star$$ is used,
*i.e.*,
for two functions $$f,g:\integers \to K$$,
the convolution of $$f$$ and $$g$$ is denoted by
$$f\star g: \integers \to K$$ and defined by<sup><a href="#footnote3" id="ref3">3</a></sup>

\begin{equation}
\label{eq:conv}
(f\star g)(t) = \sum_{k=-\infty}^\infty f(k) g(t-k).
\end{equation}

Therefore we can write the output of a discrete-time LTI system when the input is $$f$$
as

$$
H(f) = f \star h.
$$

### Continuous-time LTI systems

Now suppose that the system being considered is a continuous-time system,
that is,
we assume that $$f:\reals \to K$$
where $$K$$ is some [field](/math/abstract-algebra#fields---the-realm-of-perfect-division).

(Here I choose the most intuitive way to explain concepts
sacrificing a bit of mathematical rigor, but not much (at all).)
Note that for some small $\Delta>0$,
we can approximate $$f:\reals \to K$$
by

$$
\begin{align}
\nonumber
f(t)
	&\approx
		\sum_{k=-\infty}^\infty f(k\Delta) I_{[k\Delta-\Delta/2, k\Delta+\Delta/2]}(t)
\\ \label{eq:fcn-approx}
	&=
		\sum_{k=-\infty}^\infty f(k\Delta) I_{[-\Delta/2, \Delta/2]}(t-k\Delta)
\end{align}
$$

where $$I_A:\reals\to K$$ for $$A\subset \reals$$ is the indicator function defined by

$$
I_A(t) = \left\{\begin{array}{ll}
	1 &\mbox{if } t \in A
	\\
	0 &\mbox{otherwise}
\end{array}\right.
$$

As $$\Delta$$ goes to $$0$$,
(with proper smoothness assumption)
the RHS of \eqref{eq:fcn-approx} converges to $$f$$.

As before, the linearity of the system implies

$$
H(f(t))
	\approx
	\sum_{k=-\infty}^\infty f(k\Delta) H\left(I_{[-\Delta/2, \Delta/2]}(t-k\Delta)\right)
$$

Now we really should note the critical difference between continuous-time system and discrete-time system here.
That is, as $$\Delta$$ goes to zero, the indicator function $$I_{[-\Delta/2, \Delta/2]}(t-k\Delta)$$ vanishes.
So we need some way to preserve the *energy* or equivalently the *area* of the function,
hence we use the following trick!

$$
H(f(t))
	\approx
	\sum_{k=-\infty}^\infty \Delta f(k\Delta) H\left(\frac{1}{\Delta} I_{[-\Delta/2, \Delta/2]}(t-k\Delta)\right)
$$

Here the *energy*, *i.e.*, the area of (or rather under) the function
$$\frac{1}{\Delta} I_{[-\Delta/2, \Delta/2]}(t-k\Delta)$$
is preserved to be 1
as shown in [Figure 1](#fig:delta-function)!

<div style="text-align: center;">
<svg width="200" height="220" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <!--rect width="400" height="250" fill="white" stroke="none"/-->

  <!-- X-axis -->
  <line x1="50" y1="200" x2="150" y2="200" stroke="black" stroke-width="2"/>
  <polygon points="150,200 140,195 140,205" fill="black"/>

  <!-- Y-axis (centered at x=0, middle of rectangle) -->
  <line x1="100" y1="200" x2="100" y2="30" stroke="black" stroke-width="2"/>
  <polygon points="100,30 095,40 105,40" fill="black"/>

  <!-- Uniform distribution rectangle -->
  <rect x="95" y="050" width="10" height="150" fill="none" stroke="blue" stroke-width="2" opacity="0.7"/>

  <!-- Labels -->
  <text x="85" y="215" font-family="Arial" font-size="14" text-anchor="middle">-&Delta;/2</text>
  <text x="115" y="215" font-family="Arial" font-size="14" text-anchor="middle">&Delta;/2</text>
  <text x="125" y="55" font-family="Arial" font-size="12" text-anchor="middle">1/&Delta;</text>
  <!--text x="190" y="215" font-family="Arial" font-size="14" text-anchor="middle">0</text-->

  <!-- Axis labels -->
  <!--text x="200" y="235" font-family="Arial" font-size="16" text-anchor="middle">x</text-->
  <!--text x="25" y="30" font-family="Arial" font-size="16" text-anchor="middle">f(x)</text-->

  <!--text x="200" y="25" font-family="Arial" font-size="18" text-anchor="middle" font-weight="bold">Uniform Distribution PDF</text-->
</svg>
<p id="fig:delta-function">
Figure 1: The graph of $\frac{1}{\Delta} I_{[-\Delta/2, \Delta/2]}(t)$ for small $\Delta>0$.
</p>
</div>

Now let

$$
	h_\Delta(t) = H\left(\frac{1}{\Delta} I_{[-\Delta/2, \Delta/2]}(t)\right).
$$

Then the time-invariance of the system implies

$$
H(f(t))
	\approx
	\sum_{k=-\infty}^\infty \Delta f(k\Delta) h_\Delta(t-k\Delta)
$$

Now we note that the RHS is nothing but a [Riemann sum](https://en.wikipedia.org/wiki/Riemann_sum),
hence under proper smoothness assumption,
we have

$$
H(f(t))
	=
	\lim_{\Delta\to0}
	\sum_{k=-\infty}^\infty \Delta f(k\Delta) h_\Delta(t-k\Delta)
	=
	\int_{-\infty}^\infty
	f(\tau) h(t-\tau) d \tau
$$

where $$h = \lim_{\Delta\to0} h_\Delta$$.

As in the discrete-time case,
$$h$$ is called the <span class="emph">impulse response</span>
of the (continuous-time) LTI system,
and the output of continuous-time LTI system
can also be fully characterized by this impulse function!

Also, similarly as for the discrete-time case,
the RHS of the equation is called the <span class="emph">convolution</span> of $$f$$ and $$h$$,
and the same symbol $$\star$$ as for the discrete-time case is used,
*i.e.*,
for any two functions $f,g: \reals \to K$, we define $f\star g:\reals \to K$
by

$$
(f \star g)(t) = \int_{-\infty}^\infty f(\tau) g(t-\tau) d\tau.
$$

<!--
and this operation (of course) is also commutative, *i.e.*,

$$
f \star g = g \star f.
$$
-->

Again, using this notation, we can express the output of continue-time LTI system as

$$
H(f) = f \star h.
$$


## The inevitable eigenfunctions

Here's where the mathematical inevitability becomes crystal clear. For any LTI system, we can ask: what functions pass through the system unchanged except for scaling? These are the system's <span class="emph">eigenfunctions</span>—inputs that emerge as perfect copies of themselves, multiplied only by some complex number.

In a very similar way that [the eigenvalues and the associated eigenvectors](/math/linear-algebra#eigenvalues-eigenvectors-and-characteristic-polynomial) are defined in [linear algebra](/math/linear-algebra),
that is,
for a matrix $$A\in K^{n\times n}$$ (for a [field](/math/abstract-algebra#fields---the-realm-of-perfect-division) $$K$$),
if there exist $$\lambda \in \kclosure$$ and $$v\in \kclosure^n$$
(where $$\kclosure$$ is the algebraic closure of $$K$$)
satisfying

\begin{equation}
\label{eq:la-eigen}
	A v = \lambda v
\end{equation}

$$\lambda$$ is called the eigenvalue of $$A$$ and $$v$$ the associated eigenvector,
we can define <span class="emph">eigenfunctions</span> (and the associated eigenvalues)
similarly for LTI systems,
*i.e.*,
for a LTI system $$H$$, <!--whose impulse response is $$h:T \to K$$-->
if there exist $$v:T \to \kclosure$$ and $$\lambda\in\kclosure$$
such that

\begin{equation}
\label{eq:lti-eigen}
H(v) = \lambda v
\end{equation}

$$v$$ is called the eigenfunction of $$H$$
and $$\lambda$$ the associated eigenvalue
where $$T=\integers$$ in discuss-time case
and $$T=\reals$$ in continuous-time case.

Note the similarity or resemblance between \eqref{eq:la-eigen} and \eqref{eq:lti-eigen}.
We can simply remove the parentheses in \eqref{eq:lti-eigen} to make it look just like \eqref{eq:la-eigen}!
So essentially they mean exactly the same thing,
hence the names.

For both discrete-time and continuous-time LTI systems,
the eigenfunctions are always of the following form.

$$
	v_f(t) = e^{i 2\pi f t} = \cos(2\pi ft) + i\sin(2\pi ft)
$$

This is a pure sinusoidal wave with frequency $$f$$.

Below we will show this.

### Discrete-time LTI systems

For discrete-time LTI systems,
we assume $f$ is in $[0,1)$
since $v_f(t)$ is a periodic function of $f$
with period 1.

<!--
Define functions $$v_f:\integers \to K$$
for $$f\in [0,1)$$
by

\begin{equation}
\label{eq:eig-fcn-discrete}
	v_f(t) = e^{i 2\pi f t }
\end{equation}

where $$e^{i 2\pi f t}$$ is defined to be $$\cos(2\pi ft) + i \sin(2\pi ft)$$.
-->

<!--Now we will show these are the eigenfunctions
for *any* (discrete-time) LTI system.
-->
Note

$$
\begin{align}
\nonumber
H(v_f)(t)
	=
		\sum_{k=-\infty}^\infty h(k) v_f(t-k)
	&=
		\sum_{k=-\infty}^\infty h(k) e^{-i 2\pi f k } e^{i2\pi f t}
	\\ \nonumber
	&=
		\left( \sum_{k=-\infty}^\infty h(k) e^{-i 2\pi f k } \right) v_f(t)
\end{align}
$$

thus, $$v_f$$ is the eigenfunction of $$H$$ with $$\lambda_f = \sum_{k=-\infty}^\infty h(k) e^{-i 2\pi f k }$$
as the associated eigenvalue
where (it turns out that) it
is the [Fourier Transform](https://en.wikipedia.org/wiki/Fourier_transform)
of the (discrete-time) impulse response $$h:\integers \to K$$.<sup><a href="#footnote4" id="ref4">4</a></sup>

### Continuous-time LTI systems

<!--
Similarly, define functions $$v_f:\reals \to K$$
for $$f\in \reals$$
by

\begin{equation}
\label{eq:eig-fcn-continuous}
	v_f(t) = e^{i 2\pi f t }.
\end{equation}

Note the difference between \eqref{eq:eig-fcn-discrete} and \eqref{eq:eig-fcn-continuous}.
Though they look exactly the same,
the domain of the functions are different;
that of the former is $$\integers$$ whereas that of the latter is $$\reals$$.
-->

Here we assume $f\in\reals$.
We will show $v_f(t)$ are the eigenfunctions
for *any* (continuous-time) LTI system.
Note

$$
\begin{align}
\nonumber
H(v_f)(t)
	=
		\int_{-\infty}^\infty h(\tau) v_f(t-\tau) d\tau
	&=
		\int_{-\infty}^\infty h(\tau) e^{-i 2\pi f \tau } e^{i 2\pi f t} d\tau
	\\ \nonumber
	&=
		\left(\int_{-\infty}^\infty h(\tau) e^{-i 2\pi f \tau } d\tau \right) v_f(t)
\end{align}
$$

thus, $$v_f$$ is the eigenfunction of $$H$$ with $$\lambda_f = \int_{-\infty}^\infty h(\tau) e^{-i 2\pi f \tau} d\tau$$
as the associated eigenvalue,
which is the [Fourier Transform](https://en.wikipedia.org/wiki/Fourier_transform)
of the (continuous-time) impulse response $$h:\reals\to K$$.<sup><a href="#footnote5" id="ref5">5</a></sup>

The proof is startlingly simple for both cases!
For both cases, we have

$$
H(v_f) = \lambda_f v_f
$$

*i.e.*,
the sinusoidal function emerges from the system as a perfect copy of itself, scaled by the eigenvalue $\lambda_f$.

<span class="emph">This holds for any LTI system whatsoever.</span>
The mathematics gives us no other choice.

## From abstract mathematics to physical reality

Now comes the profound connection
&ndash; <span class="emph">electromagnetic wave propagation through free space is necessarily an LTI process.</span>

The <span class="emph">linearity</span> is built into the very fabric of electromagnetism through Maxwell's equations—electric and magnetic fields superpose linearly. If you have two electromagnetic disturbances, the total field is simply their sum.

The <span class="emph">(time-)translation invariance</span> emerges from the homogeneity of free space itself. The laws of electromagnetism work the same way in every region of empty space, at every moment in time. There are no preferred locations or special directions in the vacuum (or favorite time).

Therefore, when electromagnetic energy propagates through space, it must behave as an LTI system—and this means its natural modes of propagation must be the eigenfunctions of this system: sinusoidal waves.

## The deep mathematical truth

This reveals something remarkable
&ndash;
<a href="#quote:deeper-mathematical-necessity-for-sinusoidal-waves">
<span id="deeper-mathematical-necessity-for-sinusoidal-waves">
Maxwell's equations don't arbitrarily impose sinusoidal solutions on electromagnetic phenomena.
Rather, they emerge from a deeper mathematical necessity.</span>
</a>

The [wave equation](https://en.wikipedia.org/wiki/Wave_equation)
that follows from [Maxwell's equations](https://en.wikipedia.org/wiki/Maxwell%27s_equations),
*i.e.*,

$$
	\frac{\partial^2 \psi}{\partial t^2} = c^2 \nabla^2 \psi
$$

which both the electric field $E$ and the magnetic field $B$ should satisfy,
isn't the source of sinusoidal behavior; it's the mathematical expression of the fact that electromagnetic propagation through homogeneous space must be an LTI process.

The sinusoidal solutions aren't just *a* solution to this equation; they're the <span class="emph">inevitable</span> solutions because they're the only functions that can propagate through any linear, translation-invariant medium without changing their fundamental character.

## Beyond electromagnetism &ndash; a universal principle

This mathematical inevitability extends far beyond electromagnetic waves. Any phenomenon that propagates through a linear, homogeneous medium—sound waves in uniform air, water waves on a calm surface, quantum probability amplitudes in free space, even vibrations through crystalline solids—must necessarily decompose into sinusoidal components.

This is why [Fourier analysis](https://en.wikipedia.org/wiki/Fourier_analysis) works so universally across physics. It's not that we've chosen a convenient mathematical tool; we've discovered that sinusoidal decomposition is the natural language that linear, translation-invariant reality uses to encode information.

Just as any statistical phenomenon involving aggregation must eventually yield Gaussian distributions, any wave phenomenon in uniform space must eventually express itself through sinusoidal functions. The mathematics offers no alternatives.

## The inevitability of trigonometry

So when your high school math teacher insisted you learn trigonometric functions, they were introducing you to something far more profound than arbitrary mathematical machinery. They were teaching you the fundamental language that any universe with linear, homogeneous space would necessarily discover.

Sine and cosine aren't just useful mathematical tools—they're the inevitable mathematical expressions of how disturbances propagate through uniform reality. In any conceivable universe where space is homogeneous and physical processes are linear, intelligent beings would eventually discover these same trigonometric relationships, not because of the specific physics of their world, but because of the deeper mathematical structures that govern any possible world with these basic properties.

The ubiquity of sinusoidal waves in nature now reveals itself not as a curious coincidence, but as a manifestation of mathematical inevitability as fundamental as the appearance of $\pi$ in geometry or the emergence of Gaussian distributions in probability. We see sine waves everywhere because any linear, translation-invariant reality must speak in this mathematical language—and remarkably, that appears to include our own.

<!--
## Why Sinusoidal Functions are Inevitable for EM Waves

### The Wave Equation - The Mathematical Heart

Maxwell's equations, when combined, lead inevitably to the **wave equation**. For electromagnetic fields propagating in free space, both the electric field E and magnetic field B satisfy:

$$\frac{\partial^2 \psi}{\partial t^2} = c^2 \nabla^2 \psi$$

where ψ represents either E or B, and c is the speed of light.

This is a **linear partial differential equation** - and here's the crucial point: the most general solution to this equation is a superposition of sinusoidal waves!

### Why Sinusoids are the Natural Solutions

Consider the simplest case - a one-dimensional wave equation:

$$\frac{\partial^2 \psi}{\partial t^2} = c^2 \frac{\partial^2 \psi}{\partial x^2}$$

If we assume a solution of the form ψ(x,t) = f(x)g(t), then separation of variables gives us:

$$\frac{g''(t)}{c^2 g(t)} = \frac{f''(x)}{f(x)} = -k^2$$

This yields:
- **Temporal part**: $g(t) = A \cos(\omega t) + B \sin(\omega t)$ where $\omega  = ck$
- **Spatial part**: $f(x) = C \cos(kx) + D \sin(kx)$

The solution is inherently sinusoidal! Any other functional form would violate the linearity and homogeneity of the wave equation.

### The Inevitability Argument

1. **Maxwell's equations are inevitable** - they emerge from the most basic principles of electromagnetism (Gauss's law, Faraday's law, etc.)

2. **The wave equation is inevitable** - it's the mathematical consequence of Maxwell's equations

3. **Sinusoidal solutions are inevitable** - they're the only functions that satisfy the linear, homogeneous, second-order differential equation

4. **Superposition principle** - any complex wave is built from these sinusoidal components (Fourier analysis)

### Connection to Your LTI Analysis

Your brilliant analysis of LTI systems actually **proves** this inevitability! You showed that:

- Sinusoidal functions $e^{i2\pi ft}$ are eigenfunctions of **any** LTI system
- Electromagnetic wave propagation through space is fundamentally an LTI process
- Therefore, sinusoids are the "natural" functions that propagate unchanged (except for amplitude/phase)

### The Deep Mathematical Truth

The appearance of trigonometric functions isn't arbitrary - it reflects the fundamental mathematical structure of:
- **Rotational symmetry** in the complex plane
- **Oscillatory solutions** to second-order linear differential equations
- **Eigenfunction decomposition** of linear operators

Just as π appears "everywhere" because it's connected to the geometry of circles and spheres, sinusoidal functions appear in wave phenomena because they're the mathematical embodiment of oscillation and periodicity.

### Conclusion for This Section

Therefore, when you ask "why trigonometric functions?" for EM waves, the answer is: **mathematical inevitability**. Any universe with linear electromagnetic laws and wave propagation would necessarily discover the same trigonometric solutions. The math doesn't give us any other choice!

This connects beautifully to your broader theme - some aspects of physics that seem arbitrary are actually rooted in deeper mathematical necessities that transcend any particular universe.
-->

<!--
# Matrices &amp; matrix multiplications

## Extension to multiplications of arbitrary multi-dimensional arrays

<div class="img-container">
<img style="max-width: 75%;" src="/resource/inevitability-vs-arbitrariness/u1564158738_Extension_to_multiplications_of_arbitrary_multi-d_145d10c6-4efa-4e4a-b66a-2e903ab37567_3.png">
</div>
-->

<hr>
<ol>
<li id="footnote1">
	Well, actually, they are two simple facts and one definition!
	&nbsp;<a href="#ref1">↩</a></li>
<li id="footnote2">
	The second and the third obviously very closely relate to each other.
	&nbsp;<a href="#ref2">↩</a></li>
<li id="footnote3">
	Note that the convolution is a <i>commutative</i> binary operator,
	<i>i.e.</i>,

	$$
	(f\star g)(t)
	= \sum_{k=-\infty}^\infty f(k) g(t-k)
	= \sum_{k'=-\infty}^\infty f(t-k') g(k')
	= (g\star f)(t).
	$$
	&nbsp;<a href="#ref3">↩</a></li>
<li id="footnote4">
	This holds for any LTI system.
	The converse is not true, though, that is, for specific LTI systems,
	there can exist eigenfunctions not of the form $e^{i 2\pi f t }$.
	&nbsp;<a href="#ref4">↩</a></li>
<li id="footnote5">
	Again, note that this holds for any LTI system.
	The converse is not true, though, that is, for specific LTI systems,
	there can exist eigenfunctions not of the form $e^{i 2\pi f t }$.
	&nbsp;<a href="#ref5">↩</a></li>
</ol>

<!--
## The PDF of sum of independent random variables

$$
\Prob(X+Y \leq z)
= \int_{-\infty}^\infty \int_{-\infty}^{z-x} f_{X,Y}(x,y)  dy dx
$$

where $$f_{X,Y}$$ is the joint PDF of $$X$$ and $$Y$$.
If $X$ and $Y$ are independent,

$$
\begin{align}
\nonumber
F_Z(z)
=
\Prob(X+Y \leq z)
	&=
		\int_{-\infty}^\infty \int_{-\infty}^{z-x} f_X(x) f_Y(y)  dy dx
\\
\nonumber
	&=
		\int_{-\infty}^\infty f_X(x) \int_{-\infty}^{z-x} f_Y(y)  dy dx
\\
\nonumber
	&=
		\int_{-\infty}^\infty f_X(x) F_Y(z-x) dx
\end{align}
$$

Then

$$
\begin{align}
\nonumber
f_Z(z)
	=
		\frac{d}{dz} F_Z(z)
	&=
		\int_{-\infty}^\infty f_X(x) \frac{d}{dz} F_Y(z-x) dx
	\\ \nonumber
	&=
		\int_{-\infty}^\infty f_X(x) f_Y(z-x) dx
\end{align}
$$

hence

$$
f_{X+Y} = f_X \star f_Y
$$

that is, the PDF of the sum of (statistically) independent random variables
is the convolution of the PDFs of the random variables.
-->
