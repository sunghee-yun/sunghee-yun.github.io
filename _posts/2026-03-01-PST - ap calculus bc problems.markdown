---
date: Sun Mar  1 23:13:06 PST 2026
last_modified_at: Tue Mar  3 21:52:26 PST 2026
title: "AP Calculus BC for Beth"
permalink: /math/ap/calculus/bc
categories:
 - blog
 - Math
tags:
 - math
 - calculus
toc: true
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
usemathjax: true
---

posted: {{ page.date| date: "%d-%b-%Y" }}
&
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

**Share this on**
[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url={{ site.url }}{{ site.baseurl }}{{ page.url }})
| [Instagram](https://www.instagram.com/)
| [Twitter (X)](https://x.com/intent/tweet?text={{ site.url }}{{ site.baseurl }}{{ page.url }})
| [Facebook](https://www.facebook.com/sharer/sharer.php?u={{ site.url }}{{ site.baseurl }}{{ page.url }})

# Exercise Problem Collection

- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/chapter6_test.pdf">AP Calculus (BC) Chapter 6 Test</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/707238497-Unit-6-Practice-AP-Calculus-BC.pdf">SCRIBD AP Calculus BC Unit 6 Review</a>

# Important Topics, Patterns, and Rules

## Differentiation / Derivatives

### L'H&ocirc;pital's rule

[L'H&ocirc;pital's rule](https://en.wikipedia.org/wiki/L%27H%C3%B4pital%27s_rule){:target="_blank"}
states that for functions $f$ and $g$ which are defined on
an open interval $I$ and differentiable on $$I\backslash\{c\}$$
for a (possibly infinite) accumulation point $c$ of $I$,
if

$$
	\lim_{x\to c} f(x) = \lim_{x\to c} g(x) = 0 \mbox{ or } \pm \infty
$$

and $\lim_{x\to c} \dfrac{f'(x)}{g'(x)}$ exists, then

\begin{equation}
\label{eq:lhospital-rule}
	\lim_{x\to c} \frac{f(x)}{g(x)}
	=
	\lim_{x\to c} \frac{f'(x)}{g'(x)}
\end{equation}

**Examples**

$$
\begin{eqnarray*}
\lim_{x\to 0} \frac{\sin(x)}{x}
	&=&
		\lim_{x\to 0} \frac{\cos(x)}{1} = 1
\\
\lim_{x\to \infty} \frac{\log(x)}{x}
	&=&
		\lim_{x\to \infty} \frac{1/x}{1} = 0
\\
\lim_{x\to 0} x\log x
	&=&
		\lim_{x\to 0} \frac{\log(x)}{1/x} = \lim_{x\to 0} \frac{1/x}{-1/x^2} = 0
\\
\lim_{x\to \infty} \frac{\log(a+b\, e^{cx})}{x}
	&=&
		\lim_{x\to \infty} \frac{bc\, e^{cx}/(a+b\, e^{cx})}{1} = c
		\quad
		\mbox{for any } a,b,c>0
\end{eqnarray*}
$$

**Caveat**

$$
\begin{eqnarray*}
\lim_{x\to 0} \frac{x}{5}
	&\neq&
		\lim_{x\to 0} \frac{1}{0}
\end{eqnarray*}
$$

### Chain rule

\begin{equation}
\newcommand{\reals}{\mathbb{R}}
\label{eq:chain-rule}
\frac{d}{dx} f(g(x)) = f'(g(x)) g'(x)
\end{equation}

### Derivatives of trigonometric functions

$$
\begin{eqnarray}
\label{eq:der-tri}
\begin{array}{rcl}
	\dfrac{d}{dx} \sin(x) &=& \cos(x)
\\
	\dfrac{d}{dx} \cos(x) &=& - \sin(x)
\\
	\dfrac{d}{dx} \tan(x) &=& \sec^2(x)
		= \dfrac{1}{\cos^2(x)}
\\
\dfrac{d}{dx} \dfrac{1}{\tan(x)} =
	\dfrac{d}{dx} \cot(x) &=& - \csc^2(x)
		= - \dfrac{1}{\sin^2(x)}
\\
\dfrac{d}{dx} \dfrac{1}{\cos(x)} =
	\dfrac{d}{dx} \sec(x) &=& \sec(x) \tan(x)
		= \dfrac{\sin(x)}{\cos^2(x)}
\\
\dfrac{d}{dx} \dfrac{1}{\sin(x)} =
	\dfrac{d}{dx} \csc(x) &=& - \csc(x) \cot(x)
		= - \dfrac{\cos(x)}{\sin^2(x)}
\end{array}
\end{eqnarray}
$$

### Derivatives of inverse trigonometric functions

$$
\begin{eqnarray}
\label{eq:der-inverse-tri}
\begin{array}{rcl}
\dfrac{d}{dx} \sin^{-1}(x) &=& \dfrac{1}{\sqrt{1-x^2}}
\\
\dfrac{d}{dx} \cos^{-1}(x) &=& - \dfrac{1}{\sqrt{1-x^2}}
\\
\dfrac{d}{dx} \tan^{-1}(x) &=& \dfrac{1}{1+x^2}
\end{array}
\end{eqnarray}
$$

More formula can be found [here](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Derivatives_of_inverse_trigonometric_functions){:target="_blank"}!

## Integration / Integral

### Integration by Substitution

\begin{equation}
\label{eq:int-by-sub}
	\int g'(x) f'(g(x)) dx = f(g(x)) + C
\end{equation}

- Method 1 - using directly the chain rule, *e.g.*, we just note that

\begin{equation}
\label{eq:prob-int-by-sub-01}
	\int x e^{-x^2} dx = - \frac{1}{2} e^{-x^2} + C
\end{equation}

- Method 2 - using <span class="emph">u-substitution</span> (also known as <span class="emph">integration by substitution</span> or <span class="emph">substitution rule</span>),
*i.e.*,
	by letting

$$
	u = g(x)
$$

then

$$
	du = g'(x) dx
$$

thus

$$
	\int g'(x) f'(g(x)) dx
	=
		\int f'(u) du
	=
		f(u) + C
	=
		f(g(x)) + C
$$

For example, to solve \eqref{eq:prob-int-by-sub-01}, we let $u=-x^2$, then we have $du = -2xdx$,
hence

$$
	\int x e^{-x^2} dx
	=
		-\frac{1}{2} \int e^{u} du
	=
		-\frac{1}{2} e^{u} + C
	=
		-\frac{1}{2} e^{-x^2} + C
$$

which (of course) coincides with \eqref{eq:prob-int-by-sub-01}!

### Integrals of inverse trigonometric functions

$$
\begin{eqnarray}
\label{eq:int-arcsin}
\int \sin^{-1}(x) dx &=& x \sin^{-1}(x) + \sqrt{1-x^2} + C
\\
\label{eq:int-arccos}
\int \cos^{-1}(x) dx &=& x \cos^{-1}(x) - \sqrt{1-x^2} + C
\\
\label{eq:int-arctan}
\int \tan^{-1}(x) dx &=& x \tan^{-1}(x) - \frac{1}{2} \log(x^2+1) + C
\end{eqnarray}
$$

You can easily verify these formulas, *e.g.*, using formulas in \eqref{eq:der-inverse-tri}.
More formula can be found [here](https://en.wikipedia.org/wiki/List_of_integrals_of_inverse_trigonometric_functions){:target="_blank"}!

## Ordinary Differential Equations (ODE)

### Linear ODE

\begin{equation}
\label{eq:ode-linear}
\frac{d y}{dt} = a y + b
\end{equation}

where $a\neq 0$

Let's solve this ODE as follows.

$$
\begin{eqnarray}
\label{eq:001}
\frac{d y}{y+b/a} = a\, dt
	&\Leftrightarrow&
		\log (y+b/a) = a t + C
\\
\nonumber
	&\Leftrightarrow&
		y+b/a = e^{a t + C}
\end{eqnarray}
$$

hence we have

\begin{equation}
\label{eq:ode-linear-sol-gen}
y = e^{at+C} - \frac{b}{a}
\end{equation}

Now assume the initial condition $y(0) \in \reals$. Because we can calculate $C$ from \eqref{eq:001},
*i.e.*,

\begin{equation}
\label{eq:ode-linear-c}
C = \log(y(0)+b/a)
\end{equation}

if we plug \eqref{eq:ode-linear-c} into \eqref{eq:ode-linear-sol-gen},
we have

\begin{equation}
\label{eq:ode-linear-sol}
y
=
	e^{at+\log(y(0)+b/a)} - \frac{b}{a}
=
	\left(
		y(0) + \frac{b}{a}
	\right) e^{at}
	- \frac{b}{a}
\end{equation}

### ODE for Logistic Function

\begin{equation}
\label{eq:ode-logistic-fcn}
\frac{d y}{dt} = a y(b-y)
\end{equation}

with $a>0$ and $b>0$.

Let's solve this ODE as follows.

$$
\begin{eqnarray*}
\frac{d y}{y(b-y)} = a\, dt
	&\Leftrightarrow&
		\left(\frac{1}{y} + \frac{1}{b-y}\right) dy = ab\, dt
\\
	&\Leftrightarrow&
		\log y - \log (b-y) = ab t + C
\\
	&\Leftrightarrow&
		\log \left(\frac{y}{b-y}\right) = ab t + C
\\
	&\Leftrightarrow&
		\log \left(\frac{1}{b/y-1}\right) = ab t + C
\\
	&\Leftrightarrow&
		\log (b/y-1) = -ab t - C
\\
	&\Leftrightarrow&
		\frac{b}{y}-1 = e^{-ab t - C}
\end{eqnarray*}
$$

thus we have

\begin{equation}
\label{eq:ode-sol-logistic-fcn}
y(t) = \frac{b}{1+ e^{-abt-C}}
\end{equation}

This equation \eqref{eq:ode-sol-logistic-fcn} is called <span class="define">logistic function</span> or <span class="define">logistic equation</span>
and it comes in lots and lots of fields such as
ecology,
statistics and machine learning (hence AI),
medicine,
chemistry,
physics,
material science,
linguistics,
agriculture,
economics and sociology,
*etc.*
For more information, please refer to [Logistic function Wikipedia Page](https://en.wikipedia.org/wiki/Logistic_function){:target="_blank"}.

There are several things we can observe from this function!

- as long as $0< y(0) < b$, $y(t)$ monotonically increases (because $y'(t)>0$ for $t>0$)
- $\lim_{t\to\infty} y(t) = b$
- $y(t)$ is concave up (*i.e.*, $y$ is a convex function) where $y(t) < b/2$
- $y(t)$ is concave down (*i.e.*, $y$ is a concave function) where $y(t) > b/2$
- $y(t)$ reaches its middle point at $t = - C/ab$, *i.e.*, $y(-C/ab) = b/2$
(thus, if $C>0$, $y(t)$ is always concave down)

The graph below shows $y(t)$ when $a=1$, $b=10$, and $y(0)=1$.
The calculation shows it reaches its middle point at $t \simeq 0.21972$
We can see indeed the graph is *concave up* where $t< 0.21972$
and is *concave down* where $t>0.21972$!

<div class="img-container">
<img src="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/logistic_fcn_01.png">
</div>

# Exercise Problems

## Differential Equations

<ul>
<li>
Problem 4 of <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/chapter6_test.pdf">AP Calculus (BC) Chapter 6 Test</a>
&ndash;
Given the logistic differential equation $\dfrac{dA}{dt} = A\left(20-\dfrac{A}{4}\right)$
where $A(0) = 15$, what is $\lim_{t\to\infty} A(t)$?

<p>
<strong>Daddy's Solution 1</strong>

$$
\begin{eqnarray*}
\frac{dA}{A(20-A/4)} = dt
&\Leftrightarrow&
\left( \frac{1}{A} + \frac{1}{80-A} \right) dA = 20dt
\\
&\Leftrightarrow&
\log A - \log (80 - A) = 20 t + C
\\
&\Leftrightarrow&
\log \left( \frac{A}{80 - A} \right) = 20 t + C
\\
&\Leftrightarrow&
\log \left( \frac{1}{80/A - 1} \right) = 20 t + C
\\
&\Leftrightarrow&
\log ( 80/A - 1 ) = -20 t - C
\\
&\Leftrightarrow&
80/A = e^{-20 t - C} + 1
\\
&\Leftrightarrow&
A = \frac{80}{e^{-20 t - C} + 1}
\end{eqnarray*}
$$
</p>

<p>
<strong>Daddy's Solution 2</strong>

Let's try to solve using the formula we derived above, <i>i.e.</i>, \eqref{eq:ode-sol-logistic-fcn}!

Because we can rewrite the logistic differential equation as

$$
\frac{dA}{dt} = \frac{1}{4} A(80-A)
$$

and this equation is of the form \eqref{eq:ode-logistic-fcn}
with $a=1/4$ and $b=80$,
the formula \eqref{eq:ode-sol-logistic-fcn} gives

$$
A(t) = \frac{80}{1+ e^{-20t-C}}
$$
</p>

</li>
<li>
Problem 13 of <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/chapter6_test.pdf">AP Calculus (BC) Chapter 6 Test</a>

$$
\frac{dP}{dt} = \frac{k}{656} (650- P) P, \; P(0) = 1
$$

<p>
<strong>Daddy's Solution</strong>
Note that the above equation is of the form \eqref{eq:ode-logistic-fcn}
with $a=k/650$ and $b=650$,
thus
the formula \eqref{eq:ode-sol-logistic-fcn} gives

$$
	P(t)
	= \frac{650}{1+e^{-kt-C}}
	= \frac{650}{1+C' e^{-kt}}
$$

thus of the same form as in the problem!

</p>
</li>
<li>
Problem 5 of <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/chapter6_test.pdf">AP Calculus (BC) Chapter 6 Test</a>
&ndash;
Given the differential equation $\dfrac{dT}{dt} = -\dfrac{1}{4}(T-20)$, $T(0)=100$, then $T(20)$?

<p>
<strong>Daddy's Solution 1</strong>

$$
\begin{eqnarray*}
\frac{dT}{T-20} = -\frac{1}{4} dt
&\Leftrightarrow&
	\log (T-20)  = -\frac{1}{4} t + C
\\
&\Leftrightarrow&
	T(t)  = 20 + e^{-\frac{1}{4} t + C}
\end{eqnarray*}
$$

If we use $T(0)=100$, we have

$$
\log(80) = C
$$

hence

$$
	T(t)  = 20 + e^{-\frac{1}{4} t + \log(80)} = 20 + 80 e^{-\frac{1}{4}t}
$$

</p>

<p>
<strong>Daddy's Solution 2</strong>

Let's try to solve using the formula we derived above, <i>i.e.</i>, \eqref{eq:ode-linear-sol}.

Because we can rewrite the differential equation as

$$
\frac{dT}{dt} = - \frac{1}{4} T + 5
$$

and this equation is of the form \eqref{eq:ode-linear}
with $a=-1/4$ and $b=5$,
the formula \eqref{eq:ode-linear-sol} gives

$$
T(t) = (100 - 20) e^{-\frac{1}{4}t} + 20
$$
</p>
</li>
</ul>

