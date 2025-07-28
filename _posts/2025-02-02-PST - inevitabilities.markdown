---
title: (WIP) Inevitabilities!
date: Sun Feb  2 14:43:34 PST 2025
last_modified_at: Mon Jul 28 03:56:36 PDT 2025
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

{% assign post = site.posts | where: "permalink", "/prajna/coincidence-vs-inevitability" | first %}

Unlike what I discuss in <a href="{{ post.url }}">{{ post.title }}</a>,
here I discuss the inevitabilities that I have found or rather identified,
which are true not only in our universe
but in any universe,
or rather for that matter,
it does not have to be a universe.

# The Gaussian Distribution &ndash; Why "Normal" is Actually Inevitable

(WIP)

<!--div class="img-container">
<img style="max-width: 75%;" src="/resource/inevitability-vs-arbitrariness/gaussian/lots-of-gaussian-distributions-in-3d.png">
</div-->

Walk into any statistics classroom, flip open any data science textbook, or peek under the hood of most machine learning algorithms,
and you'll find the same ubiquitous bell-shaped curve staring back at you.
The Gaussian distribution—also known as the normal distribution—appears so frequently in nature and human affairs that we've literally named it "normal."
But is this dominance merely a convenient mathematical fiction, or does it reflect something deeper about the structure of reality itself?

The answer lies in one of the most remarkable theorems in all of mathematics: the [Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem). Far from being an arbitrary choice or a quirk of our mathematical toolkit, the [Gaussian distribution](https://en.wikipedia.org/wiki/Normal_distribution) emerges as an inevitable consequence of how randomness behaves when it accumulates. This isn't just mathematical elegance—it's a fundamental truth that transcends our universe.

Unlike the physical constants I explored in my previous post on [coincidence versus inevitability](https://sungheeyun.github.io/prajna/coincidence-vs-inevitability)—where Newton's gravitational constant G or the specific exponent in inverse square laws might be contingent features of our particular universe—the normal distribution represents pure mathematical inevitability. The Gaussian curve would emerge in *any* possible universe where randomness exists, even in alternate realities with completely different physical laws. In fact, we don't need universes at all for this truth to hold; it flows directly from the logical structure of probability itself, as universal and inevitable as prime numbers.

## The Central Limit Theorem &ndash; Where Chaos Becomes Order

In probability theory, the [Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem) states that, under appropriate conditions, the distribution of a normalized version of the sample mean converges to a [standard normal distribution](https://en.wikipedia.org/wiki/Normal_distribution#Standard_normal_distribution). This holds even if the original variables themselves are not [normally distributed](https://en.wikipedia.org/wiki/Normal_distribution).

The Central Limit Theorem states the following:
<blockquote>
Let $\{X_i\}_{i=1}^\infty$ be independent, identically distributed random variables
with $\Expect X_i  = \mu$ and $\Var X_i =\sigma^2$. Then

$$
Z_n = \sum_{i=1}^n \frac{X_i-\mu}{\sqrt{n}\sigma}
$$

converges in distribution to $\mathcal{N}(0,1)$ as $n$ goes to $\infty$.
</blockquote>

Let that sink in for a moment. You can start with *any* collection of random variables—whether they follow uniform distributions, exponential distributions, or even bizarre custom distributions with multiple peaks and valleys. Add enough of them together, and their sum will inexorably march toward the familiar bell curve. It's as if mathematics itself has a built-in organizing principle that transforms chaos into predictable patterns.

This is profoundly different from the physical laws we encounter in nature. While we might ask whether Newton's law of universal gravitation could have an exponent of 3 instead of 2 (and I argued that the exponent 2 might itself have geometric inevitability), or whether Einstein's $$E=mc^2$$ could have a different proportionality constant, no such questions arise for the Central Limit Theorem. The bell curve doesn't depend on the specific physical constants of our universe, the peculiarities of biological evolution, or the accidents of cosmic history.

The theorem serves as a cornerstone of probability theory because it implies that probabilistic and statistical methods designed for normal distributions can be applied to countless problems involving other types of distributions. But beyond its practical utility lies something more profound: the [Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem) reveals that the Gaussian distribution isn't just mathematically convenient—it's mathematically *inevitable*.

Sometimes the theorem feels almost too good to be true, like discovering that the messy complexity of the real world secretly follows elegant mathematical laws. However, unlike the curious coincidences between geometry and physics that I explored in my discussion of inverse square laws in <a href="{{ post.url }}">{{ post.title }}</a>,
the [Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)
represents unqualified inevitability. It emerges from the fundamental logic of probability itself, requiring no physical substrate whatsoever.

As fantastic as this mathematical inevitability appears, it raises an even deeper question: *why* should adding random variables together produce such orderly results? The answer reveals something profound about the nature of information, entropy, and the hidden mathematical structures that govern randomness itself—structures as universal as the geometric facts that make π appear in the area of circles, yet somehow even more fundamental.

## Proof of Central Limit Theorem boils down to two simple facts

Here
we will first clearly see
why the Central Limit Theorem *has to* hold;
it really boils down to surprisingly simple facts!

- A smooth function can be well approximated by the quadratic polynomial (backed by [Taylor's theorem](https://en.wikipedia.org/wiki/Taylor%27s_theorem#Taylor's_theorem_in_one_real_variable)), *i.e.*, if $f:\reals\to\reals$ is twice-differentiable at $a\in\reals$,
there exists $h:\reals\to\reals$ such that
\begin{equation}
	f(x) = f(a) + f^\prime(a)(x-a) + \frac{1}{2} f^{\prime\prime}(a) (x-a)^2 + h(x)(x-a)^2
\end{equation}
and
\begin{equation}
	\lim_{x\to a} h(x) = 0.
\end{equation}

- The definition of $e$, *i.e.*,

\begin{equation}
\label{eq:def-napier-constant}
	e = \lim_{n\to\infty} \left(1+\frac{1}{n}\right)^n
\end{equation}

Now let's see why this is the case!

### Characteristic function of a random variable

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

# The most natural function for electromagnetic waves to use for propagating energy is sinusoidal waves

(Hence, you really should study hard trigonometric functions in high school! &#x2605;^^&#x2605;)

<!--
&#42;^^&#42;
-->

(WIP)

<div class="img-container">
<img style="max-width: 75%;" src="/resource/inevitability-vs-arbitrariness/sinusoidal/electromagnetic-waves-propagate-in-space.png">
</div>

## Linear time-invariant (LTI) system

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
$$f\star g: \integers \to K$$ and defined by

\begin{equation}
\label{eq:conv}
(f\star g)(t) = \sum_{k=-\infty}^\infty f(k) g(t-k)
\end{equation}

Note that the convolution is a *commutative* binary operator,
*i.e.*,

$$
(f\star g)(t)
= \sum_{k=-\infty}^\infty f(k) g(t-k)
= \sum_{k'=-\infty}^\infty f(t-k') g(k')
= (g\star f)(t).
$$

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

Here I choose the most intuitive way to explain concepts
sacrificing a bit of mathematical strictness.
We can approximate $$f:\reals \to K$$
by

\begin{equation}
\label{eq:fcn-approx}
f(t)
	\approx
	\sum_{k=-\infty}^\infty f(k\Delta) I_{[k\Delta-\Delta/2, k\Delta+\Delta/2]}(t)
	=
	\sum_{k=-\infty}^\infty f(k\Delta) I_{[-\Delta/2, \Delta/2]}(t-k\Delta)
\end{equation}

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
hence the following trick!

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

Also, similarly as in the discrete-time case,
the RHS of the equation is called the <span class="emph">convolution</span> of $$f$$ and $$h$$,
and the same symbol $$\star$$ as in the discrete-time case is used,
*i.e.*,
for any two functions $$f,g: \reals \to K$$, we define

$$
(f \star g)(t) = \int_{-\infty}^\infty f(\tau) g(t-\tau) d\tau
$$

and this operation (of course) is also commutative, *i.e.*,

$$
f \star g = g \star f.
$$

Again, using this notation, we can express the output of continue-time LTI system as

$$
H(f) = f \star h.
$$

## Eigenfunctions of LTIs

As the eigenvalues and the associated eigenvectors are defined in linear algebra as below,
that is,
for a matrix $$A\in K^{n\times n}$$ (for a field $$K$$),
if there exist $$\lambda \in \kclosure$$ and $$v\in \kclosure^n$$
(where $$\kclosure$$ is the algebraic closure of $$K$$)
satisfying

\begin{equation}
\label{eq:la-eigen}
	A v = \lambda v
\end{equation}

$$\lambda$$ is called the eigenvalue of $$A$$ and $$v$$ the associated eigenvector,
we can define <span class="emph">eigenfunctions</span> (and the associated eigenvalues)
similarly for LTI systems.

For a LTI system $$H$$ whose impulse response is $$h:T \to K$$
(where $$T=\integers$$ in discuss-time case
and $$T=\reals$$ in continuous-time case),
if there exist $$v:T \to \kclosure$$ and $$\lambda\in\kclosure$$
such that

\begin{equation}
\label{eq:lti-eigen}
H(v) = \lambda v
\end{equation}

$$v$$ is called the eigenfunction of $$H$$
and $$\lambda$$ the associated eigenvalue.

Note the similarity or resemblance between \eqref{eq:la-eigen} and \eqref{eq:lti-eigen}.
We can simply remove the parentheses in \eqref{eq:lti-eigen} to make it look just like \eqref{eq:la-eigen}!
So essentially they mean exactly the same thing,
hence the names.

Now let us show that sinusoidal waves are the eigenvalues of *any* LTI systems.
Here once again,
we show this for both discrete-time and continuous-time cases separately.

### Discrete-time LTI systems

Define functions $$v_f:\integers \to K$$
for $$f\in [0,1)$$
by

\begin{equation}
\label{eq:eig-fcn-discrete}
	v_n(t) = e^{i 2\pi f t }
\end{equation}

where $$e^{i 2\pi f t}$$ is defined to be $$\cos(2\pi ft) + i \sin(2\pi ft)$$.

Now we will show these are the eigenfunctions
for *any* (discrete-time) LTI system.
Note

$$
\begin{align}
\nonumber
H(v_n)(t)
	=
		\sum_{k=-\infty}^\infty h(k) v_n(t-k)
	&=
		\sum_{k=-\infty}^\infty h(k) e^{-i 2\pi f k } e^{i2\pi f t}
	\\ \nonumber
	&=
		\left( \sum_{k=-\infty}^\infty h(k) e^{-i 2\pi f k } \right) e^{i2\pi f t}
\end{align}
$$

thus, $$v_f$$ is the eigenfunction of $$H$$ with $$\sum_{k=-\infty}^\infty h(k) e^{-i 2\pi f k }$$
as the associated eigenvalue
where (it turns out that) the associated eigenvalue
is the [Fourier Transform](https://en.wikipedia.org/wiki/Fourier_transform)
of the (discrete-time) impulse response $$h:\integers \to K$$.

Note that this holds for any LTI system.
The converse is not true, though, that is, for specific LTI systems,
there can exist eigenfunctions not of the form $$e^{i 2\pi f t }$$.

### Continuous-time LTI systems

Similarly, define functions $$v_f:\reals \to K$$
for $$f\in \reals$$
by

\begin{equation}
\label{eq:eig-fcn-continuous}
	v_n(t) = e^{i 2\pi f t }.
\end{equation}

Note the difference between \eqref{eq:eig-fcn-discrete} and \eqref{eq:eig-fcn-continuous}.
Though they look exactly the same,
the domain of the functions are different;
that of the former is $$\integers$$ whereas that of the latter is $$\reals$$.

Once again, we will show these are the eigenfunctions
for *any* (continuous-time) LTI system.
Note

$$
\begin{align}
\nonumber
H(v_n)(t)
	=
		\int_{-\infty}^\infty h(\tau) v_n(t-\tau) d\tau
	&=
		\int_{-\infty}^\infty h(\tau) e^{-i 2\pi f \tau } e^{i 2\pi f t} d\tau
	\\ \nonumber
	&=
		\left(\int_{-\infty}^\infty h(\tau) e^{-i 2\pi f \tau } d\tau \right) e^{i2\pi f t}
\end{align}
$$

thus, $$v_f$$ is the eigenfunction of $$H$$ with $$\int_{-\infty}^\infty h(\tau) e^{-i 2\pi f \tau} d\tau$$
as the associated eigenvalue
where the associated eigenvalue is the [Fourier Transform](https://en.wikipedia.org/wiki/Fourier_transform)
of the (continuous-time) impulse response $$h:\reals\to K$$.

Again, note that this holds for any LTI system.
The converse is not true, though, that is, for specific LTI systems,
there can exist eigenfunctions not of the form $$e^{i 2\pi f t }$$.

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
- **Temporal part**: g(t) = A cos(ωt) + B sin(ωt) where ω = ck
- **Spatial part**: f(x) = C cos(kx) + D sin(kx)

The solution is inherently sinusoidal! Any other functional form would violate the linearity and homogeneity of the wave equation.

### The Inevitability Argument

1. **Maxwell's equations are inevitable** - they emerge from the most basic principles of electromagnetism (Gauss's law, Faraday's law, etc.)

2. **The wave equation is inevitable** - it's the mathematical consequence of Maxwell's equations

3. **Sinusoidal solutions are inevitable** - they're the only functions that satisfy the linear, homogeneous, second-order differential equation

4. **Superposition principle** - any complex wave is built from these sinusoidal components (Fourier analysis)

### Connection to Your LTI Analysis

Your brilliant analysis of LTI systems actually **proves** this inevitability! You showed that:

- Sinusoidal functions e^{i2πft} are eigenfunctions of **any** LTI system
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

# Matrices &amp; matrix multiplications

## Extension to multiplications of arbitrary multi-dimensional arrays

<div class="img-container">
<img style="max-width: 75%;" src="/resource/inevitability-vs-arbitrariness/u1564158738_Extension_to_multiplications_of_arbitrary_multi-d_145d10c6-4efa-4e4a-b66a-2e903ab37567_3.png">
</div>

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
