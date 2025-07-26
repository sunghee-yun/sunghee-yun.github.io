---
title: (WIP) Inevitabilities!
date: Sun Feb  2 14:43:34 PST 2025
last_modified_at: Sat Jul 26 02:22:37 PDT 2025
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

$$
\newcommand{\reals}{\mathbb{R}}
\newcommand{\complexes}{\mathbb{C}}
\newcommand{\integers}{\mathbb{Z}}
\newcommand{\kclosure}{\bar{K}}
\newcommand{\Prob}{\mbox{Prob}}
$$

<!--tags: {% for tag in page.tags %} <a href="/tags/#{{ tag }}">{{ tag }}</a> {% endfor %}
<br>
cats: {% for category in page.categories %} <a href="/categories/#{{ category }}">{{ category }}</a> {% endfor %}-->

posted: {{ page.date| date: "%d-%b-%Y" }}
&amp;
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

{% assign post = site.posts | where: "permalink", "/prajna/coincidence-vs-inevitability" | first %}

Unlike what I discuss in <a href="{{ post.url }}">{{ post.title }}</a>,
here I discuss the inevitabilities that I have found or rather identified,
which are true not only in our universe
but in any universe,
or rather for that matter,
it does not have to be a universe.

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

# Gaussian (distribution) indeed is normal or inevitable!

(WIP)

<div class="img-container">
<img style="max-width: 75%;" src="/resource/inevitability-vs-arbitrariness/gaussian/lots-of-gaussian-distributions-in-3d.png">
</div>

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
f_Z(z)
	=
		\frac{d}{dz} F_Z(z)
	=
		\int_{-\infty}^\infty f_X(x) \frac{d}{dz} F_Y(z-x) dx
$$



## The central limit theorem

## Taylor expansion

The second order Taylor expansion tells you that
(under some proper smoothness assumption)
a function $$f:\reals\to\reals$$
can be expressed as

$$
f(x) = f(a) + f'(a)(x-a) + \frac{1}{2} f''(a) (x-a)^2 + o((x-a)^2)
$$

for some $$a\in\reals$$


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
for $$f\in \reals$$
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


# Matrices &amp; matrix multiplications

## Extension to multiplications of arbitrary multi-dimensional arrays

<div class="img-container">
<img style="max-width: 75%;" src="/resource/inevitability-vs-arbitrariness/u1564158738_Extension_to_multiplications_of_arbitrary_multi-d_145d10c6-4efa-4e4a-b66a-2e903ab37567_3.png">
</div>
