---
date: Sun Mar  1 23:13:06 PST 2026
last_modified_at: Wed Mar  4 02:28:16 PST 2026
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
\lim_{x\to \infty} xe^{-x}
	&=&
		\lim_{x\to \infty} \frac{x}{e^x}
		=
		\lim_{x\to \infty} \frac{1}{e^x} = 0
\\
\lim_{x\to \infty} x^2 e^{-x}
	&=&
		\lim_{x\to \infty} \frac{x^2}{e^x}
		=
		\lim_{x\to \infty} \frac{2x}{e^x}
		=
		\lim_{x\to \infty} \frac{2}{e^x} = 0
\\
\lim_{x\to \infty} \frac{\ln(x)}{x}
	&=&
		\lim_{x\to \infty} \frac{1/x}{1} = 0
\\
\lim_{x\to 0^+} x\ln x
	&=&
		\lim_{x\to 0^+} \frac{\ln(x)}{1/x} = \lim_{x\to 0^+} \frac{1/x}{-1/x^2} = \lim_{x\to 0^+} (-x) = 0
\\
\lim_{x\to \infty} \frac{\ln(a+b\, e^{cx})}{x}
	&=&
		\lim_{x\to \infty} \frac{bc\, e^{cx}/(a+b\, e^{cx})}{1} = c
		\;
		\mbox{for } a,b,c>0
\\
\lim_{x\to 0} \frac{e^x-1}{x}
	&=&
		\lim_{x\to 0} \frac{e^x}{1} = 1
\\
\lim_{x\to 0} \frac{e^x-1}{x^2+x}
	&=&
		\lim_{x\to 0} \frac{e^x}{2x+1} = 1
\\
\lim_{x\to 0} \frac{2\sin x - \sin(2x)}{x-\sin x}
	&=&
		\lim_{x\to 0} \frac{2\cos x - 2\cos(2x)}{1-\cos x}
\\
	&=&
		\lim_{x\to 0} \frac{-2\sin x + 4\sin(2x)}{\sin x}
\\
	&=&
		\lim_{x\to 0} \frac{-2\cos x + 8\cos(2x)}{\cos x} = 6
\\
\lim_{h\to 0} \frac{f(x+h)+f(x-h)-2f(x)}{h^2}
	&=&
		\lim_{h\to 0} \frac{f(x+h)+f(x-h)-2f(x)}{h^2}
\\
	&=&
		\lim_{h\to 0} \frac{f'(x+h)-f'(x-h)}{2h}
\\
	&=&
		\lim_{h\to 0} \frac{f^{\prime\prime}(x+h)+f^{\prime\prime}(x-h)}{2} = f^{\prime\prime}(x)
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
\int \tan^{-1}(x) dx &=& x \tan^{-1}(x) - \frac{1}{2} \ln(x^2+1) + C
\end{eqnarray}
$$

You can easily verify these formulas, *e.g.*, using formulas in \eqref{eq:der-inverse-tri}.
More formula can be found [here](https://en.wikipedia.org/wiki/List_of_integrals_of_inverse_trigonometric_functions){:target="_blank"}!

## Fundamental theorem of calculus

The [fundamental theorem of calculus](https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus){:target="_blank"}
is
a theorem that links the concept of differentiating a function (calculating its slopes, or rate of change at every point on its domain)
with the concept of integrating a function (calculating the area under its graph, or the cumulative effect of small contributions).
Roughly speaking, the two operations can be thought of as inverses of each other.

The first part of the theorem,
[the first fundamental theorem of calculus](https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus#First_part){:target="_blank"},
states that for a continuous function $f$,
an [antiderivative](https://en.wikipedia.org/wiki/Antiderivative){:target="_blank"}
or indefinite integral $F$ can be obtained
as the integral of $f$ over an interval with a variable upper bound.

Let $f$ be a continuous real-valued function defined on a closed interval $[a, b]$.
Let $F$ be the function defined, for all $x$ in $[a, b]$, by

$$
F(x) = \int_a^x f(t) \, dt
$$

Then $F$ is uniformly continuous on $[a, b]$ and differentiable on the open interval $(a, b)$, and

$$
F'(x) = f(x)
$$

for all $x$ in $(a,b)$ so $F$ is an [antiderivative](https://en.wikipedia.org/wiki/Antiderivative){:target="_blank"} of $f$.
We can combine these two equations to write

\begin{equation}
\label{eq:fund-theorem-of-calculus-1}
\frac{d}{dx} \int_a^x f(t) \, dt = f(x)
\end{equation}

<!--
The fundamental theorem is often employed to compute the definite integral of a function  $f$
for which an antiderivative $F$ is known.
Specifically, if $f$ is a real-valued continuous function on $[a, b]$ and $F$ is an antiderivative of $f$
in $[a, b]$, then

$$
\int_a^b f(t) \, dt = F(b) - F(a)
$$
-->

Conversely, [the second part of the theorem of calculus](https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus#Second_part){:target="_blank"}
(sometimes referred to as **Newton–Leibniz theorem**),
states that the integral of a function $f$ over a fixed interval is equal to the change of any [antiderivative](https://en.wikipedia.org/wiki/Antiderivative){:target="_blank"} $F$
between the ends of the interval.
<!--
This greatly simplifies the calculation of a definite integral provided an antiderivative can be found by symbolic integration, thus avoiding numerical integration.
-->

Let $f$ be a real-valued function on a closed interval $[a,b]$ and $F$ a continuous function on $[a,b]$
which is an antiderivative of $f$ in $(a,b)$,
*i.e.*,

$$
F'(x) = f(x)
$$

Then if $f$ is [Riemann integrable](https://en.wikipedia.org/wiki/Riemann_integrable){:target="_blank"}
on $[a,b]$ then

\begin{equation}
\label{eq:fund-theorem-of-calculus-2}
\int_a^b f(x) \, dx = F(b) - F(a)
\end{equation}

**Examples** using \eqref{eq:fund-theorem-of-calculus-1}

$$
\begin{eqnarray*}
\frac{d}{dx} \int_2^x \sqrt{1+t^2} \, dt
	&=&
		\sqrt{1+x^2}
\\
\lim_{h\to 0} \frac{\int_1^{1+h} \sqrt{x^5+8} \, dx}{h}
	&=&
		\sqrt{1^5+8} = 3
\\
\frac{d}{dx} \int_a^{g(x)} f(t) \, dt
	&=&
		f(g(x)) g'(x)
\\
\frac{d}{dx} \int_{h(x)}^{g(x)} f(t) \, dt
	&=&
		f(g(x)) g'(x) - f(h(x)) h'(x)
\\
\frac{d}{dx} \int_2^{x^2} \sqrt{1+t^2} \, dt
	&=&
		2x \sqrt{1+x^4}
\end{eqnarray*}
$$

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
		\ln (y+b/a) = a t + C
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
C = \ln(y(0)+b/a)
\end{equation}

if we plug \eqref{eq:ode-linear-c} into \eqref{eq:ode-linear-sol-gen},
we have

\begin{equation}
\label{eq:ode-linear-sol}
y
=
	e^{at+\ln(y(0)+b/a)} - \frac{b}{a}
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
		\ln y - \ln (b-y) = ab t + C
\\
	&\Leftrightarrow&
		\ln \left(\frac{y}{b-y}\right) = ab t + C
\\
	&\Leftrightarrow&
		\ln \left(\frac{1}{b/y-1}\right) = ab t + C
\\
	&\Leftrightarrow&
		\ln (b/y-1) = -ab t - C
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

## Area and Volume

The area can be calculated by the integration of the **length** $l(x)$ of a cross section perpendicular to the $x$-axis,
*i.e.*,

$$
A = \int_a^b l(x) dx
$$

The volume can be calculated by the integration of the **area** $A(x)$ of a cross section perpendicular to the $x$-axis,
*i.e.*,

$$
V = \int_a^b A(x) dx
$$

<h4>The area between two curves</h4>

$$
A = \int_a^b \left|f(x) - g(x)\right| dx
$$

<h4>The area in polar coordinates</h4>

$$
A = \frac{1}{2} \int_\alpha^\beta r(\theta)^2 d\theta
$$

**The area between two polar curves**

$$
A = \frac{1}{2} \int_\alpha^\beta (r_\mathrm{outer}(\theta)^2 - r_\mathrm{inner}(\theta)^2) d\theta
$$

<h4>Volume - disc method</h4>

$$
	V = \pi \int_a^b R(x)^2 dx
$$

where $R(x)$ is the distance between the axis of revolution and the outside of the object

$$
	V = \pi \int_a^b \left( R(x)^2 - r(x)^2 \right)dx
$$

where $R(x)$ is the radius of the outside of the object and
$r(x)$ is the radius of the inside of the object

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
\ln A - \ln (80 - A) = 20 t + C
\\
&\Leftrightarrow&
\ln \left( \frac{A}{80 - A} \right) = 20 t + C
\\
&\Leftrightarrow&
\ln \left( \frac{1}{80/A - 1} \right) = 20 t + C
\\
&\Leftrightarrow&
\ln ( 80/A - 1 ) = -20 t - C
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
	\ln (T-20)  = -\frac{1}{4} t + C
\\
&\Leftrightarrow&
	T(t)  = 20 + e^{-\frac{1}{4} t + C}
\end{eqnarray*}
$$

If we use $T(0)=100$, we have

$$
\ln(80) = C
$$

hence

$$
	T(t)  = 20 + e^{-\frac{1}{4} t + \ln(80)} = 20 + 80 e^{-\frac{1}{4}t}
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

# Exercise Problem Collection

- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/chapter6_test.pdf">AP Calculus (BC) Chapter 6 Test</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/707238497-Unit-6-Practice-AP-Calculus-BC.pdf">SCRIBD AP Calculus BC Unit 6 Review</a>

## Area and Volume

- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.1_ca1.pdf">c_11.1_ca1.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.1_ca2.pdf">c_11.1_ca2.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.1_packet.pdf">c_11.1_packet.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.1_solutions.pdf">c_11.1_solutions.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.2_ca1.pdf">c_11.2_ca1.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.2_ca2.pdf">c_11.2_ca2.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.2_packet.pdf">c_11.2_packet.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.2_solutions.pdf">c_11.2_solutions.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.3_ca1.pdf">c_11.3_ca1.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.3_ca2.pdf">c_11.3_ca2.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.3_packet.pdf">c_11.3_packet.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.3_solutions.pdf">c_11.3_solutions.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.4_ca1.pdf">c_11.4_ca1.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.4_ca2.pdf">c_11.4_ca2.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.4_packet.pdf">c_11.4_packet.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.4_solutions.pdf">c_11.4_solutions.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11_review_solutions.pdf">c_11_review_solutions.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11_review.pdf">c_11_review.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/free_response_on_area_and_volume.pdf">free_response_on_area_and_volume.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/free_response_answers_on_area_and_volume.pdf">free_response_answers_on_area_and_volume.pdf</a>
