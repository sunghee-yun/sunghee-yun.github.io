---
date: Sun Mar  1 23:13:06 PST 2026
last_modified_at: Thu Mar  5 05:27:26 PST 2026
title: "Daddy's AP Calculus BC for Beth"
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

### Definition

The [<span class="emph">derivative</span>](https://en.wikipedia.org/wiki/Derivative){:target="_blank"} is a fundamental tool that quantifies the sensitivity to change of a function's output with respect to its input.
The derivative of a function of a single variable at a chosen input value, when it exists, is <span class="emph">the slope of the tangent line</span> to the graph of the function at that point.
The tangent line is <span class="emph">the best linear approximation of the function</span> near that input value.
The derivative is often described as <span class="emph">the instantaneous rate of change</span>, the ratio of the instantaneous change in the dependent variable to that of the independent variable.
The process of finding a derivative is called <span class="emph">differentiation</span>.

A function of a real variable $\newcommand{\reals}{\mathbb{R}}f(x)$ is differentiable at a point $a$ of its domain,
if its domain contains an open interval containing $a$, and the limit in \eqref{eq:def-derivative} exists.

\begin{equation}
\label{eq:def-derivative}
	\lim_{h\to 0} \frac{f(a+h)-f(a)}{h}
\end{equation}

### Chain rule {#chain-rule}

\begin{equation}
\label{eq:chain-rule}
\frac{d}{dx} f(g(x)) = f'(g(x)) g'(x)
\end{equation}

### Mean value theorem {#mean-value-theorem}

The [mean value theorem](https://en.wikipedia.org/wiki/Mean_value_theorem){:target="_blank"} (or Lagrange's mean value theorem) states, roughly,
that for a given planar arc between two endpoints,
there is at least one point at which the tangent to the arc is parallel to the secant through its endpoints.
It is one of the most important results in real analysis.

Let $f:[a,b]\to\reals$ be a continuous function on the closed interval $[a,b]$,
and differentiable on the open interval $(a,b)$,
where $a< b$. Then there exists some $c$ in $(a,b)$ such that

\begin{equation}
	f'(c) = \frac{f(b)-f(a)}{b-a}
\end{equation}

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
\lim_{x\to 0} \frac{2x^2-3x}{3x^2+3x}
	&=&
		\lim_{x\to 0} \frac{4x-3}{6x+3} = -1
\\
\lim_{x\to \infty} \frac{2x^2+3x}{2+x^2}
	&=&
		\lim_{x\to \infty} \frac{2x+3}{2x}
		=
		\lim_{x\to \infty} \frac{2}{2} = 1
\\
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
		\lim_{x\to 0^+} \frac{\ln(x)}{1/x} = \lim_{x\to 0^+} \frac{1/x}{-1/x^2}
\\
	&=&
		\lim_{x\to 0^+} (-x) = 0
\\
\lim_{x\to \infty} \frac{\ln(a+b\, e^{cx})}{x}
	&=&
		\lim_{x\to \infty} \frac{bc\, e^{cx}/(a+b\, e^{cx})}{1}
\\
	&=&
		c \quad \mbox{for } a,b,c>0
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

### Taylor series {#taylor-series}

The [<span class="define">Taylor series</span> or <span class="define">Taylor expansion</span>](https://en.wikipedia.org/wiki/Taylor_series){:target="_blank"}
of a function is an infinite sum of terms that are expressed in terms of the function's derivatives at a single point.
For most common functions, the function and the sum of its Taylor series are equal near this point.
Taylor series are named after [Brook Taylor](https://en.wikipedia.org/wiki/Brook_Taylor){:target="_blank"},
who introduced them in 1715.
A Taylor series is also called a <span class="define">Maclaurin series</span>
when 0 is the point where the derivatives are considered,
after [Colin Maclaurin](https://en.wikipedia.org/wiki/Colin_Maclaurin){:target="_blank"},
who made extensive use of this special case of Taylor series in the 18th century.

The Taylor series of a real or complex-valued function $f(x)$,
that is infinitely differentiable at a real or complex number $a$, is the power series

\begin{equation}
\label{eq:taylor-series}
	\sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!} (x-a)^n
=
	f(a)
	+ \frac{f'(a)}{1!}(x-a)
	+ \frac{f^{\prime\prime}(a)}{2!}(x-a)^2
	+ \cdots
\end{equation}

where $n!$ denotes the factorial of $n$,
the function $f^{(n)}(a)$ denotes the $n$-th derivative of $f$ evaluated at the point $a$,
the derivative of order zero of $f$ is defined to be $f$ itself,
and
$(x − a)^0$ and $0!$ are both defined to be $1$.

With $a = 0$, the <span class="define">Maclaurin series</span> takes the form

\begin{equation}
\label{eq:maclaurin-series}
	\sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!} x^n
=
	f(0)
	+ \frac{f'(0)}{1!}x
	+ \frac{f^{\prime\prime}(0)}{2!}x^2
	+ \cdots
\end{equation}

<h4>Examples</h4>

- [**exponential function**](https://en.wikipedia.org/wiki/Taylor_series#Exponential_function){:target="_blank"}

\begin{equation}
	e^x
	=
	\sum_{n=0}^\infty \frac{x^n}{n!} = 1 + x + \frac{x^2}{2} + \frac{x^3}{3!} + \cdots
\end{equation}

- [**natural logarithm**](https://en.wikipedia.org/wiki/Taylor_series#Natural_logarithm){:target="_blank"}

\begin{equation}
	\ln(1+x)
	=
	\sum_{n=0}^\infty (-1)^{n+1} \frac{x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots
\end{equation}

hence

\begin{equation}
	\ln(1-x)
	=
	- \sum_{n=0}^\infty (-1)^{n} \frac{x^n}{n} = - x - \frac{x^2}{2} - \frac{x^3}{3} - \cdots
\end{equation}

- [**geometric series**](https://en.wikipedia.org/wiki/Taylor_series#Geometric_series){:target="_blank"}

\begin{equation}
	\frac{1}{1-x}
	=
	\sum_{n=0}^\infty x^n = 1 + x + x^2 + \cdots
\end{equation}

\begin{equation}
	\frac{1}{(1-x)^2}
	=
	\sum_{n=1}^\infty nx^{n-1} = 1 + 2x + 3x^2 + \cdots
\end{equation}

- [**trigonometric functions**](https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions){:target="_blank"}

$$
\begin{eqnarray}
	\sin(x)
	&=&
		\sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!} x^{2n+1}
	=
		x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots
\\
	\cos(x)
	&=&
		\sum_{n=0}^\infty \frac{(-1)^n}{(2n)!} x^{2n}
	=
		1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots
\end{eqnarray}
$$

More examples can be shown in [Taylor series Wikipedia Page](https://en.wikipedia.org/wiki/Taylor_series#List_of_Maclaurin_series_of_some_common_functions){:target="_blank"}!

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

- Method 1 - using directly the [chain rule](#chain-rule), *e.g.*, we just note that

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

## Fundamental theorem of calculus {#fundamental-theorem-of-calculus}

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

## Length / Distance / Velocity / Acceleration

(WIP)

## Area and Volume

The area can be calculated by the integration of the **length** $l(x)$ of a cross section perpendicular to the $x$-axis,
*i.e.*,

\begin{equation}
A = \int_a^b l(x) dx
\end{equation}

The volume can be calculated by the integration of the **area** $A(x)$ of a cross section perpendicular to the $x$-axis,
*i.e.*,

\begin{equation}
V = \int_a^b A(x) dx
\end{equation}

<h4>The area between two curves</h4>

\begin{equation}
A = \int_a^b \left|f(x) - g(x)\right| dx
\end{equation}

<h4>The area in polar coordinates</h4>

\begin{equation}
A = \frac{1}{2} \int_\alpha^\beta r(\theta)^2 d\theta
\end{equation}

**The area between two polar curves**

\begin{equation}
A = \frac{1}{2} \int_\alpha^\beta (r_\mathrm{outer}(\theta)^2 - r_\mathrm{inner}(\theta)^2) d\theta
\end{equation}

<h4>Disc method for volume calculation</h4>

\begin{equation}
	V = \pi \int_a^b R(x)^2 dx
\end{equation}

where $R(x)$ is the distance between the axis of revolution and the outside of the object

<h4>Washer method for volume calculation</h4>

\begin{equation}
	V = \pi \int_a^b \left( R(x)^2 - r(x)^2 \right)dx
\end{equation}

where $R(x)$ is the radius of the outside of the object and
$r(x)$ is the radius of the inside of the object

<h4>Shell method for volume calculation</h4>

[<span class="define">Shell integration</span>](https://en.wikipedia.org/wiki/Shell_integration){:target="_blank"}
(the <span class="define">shell method</span> in integral calculus)
is a method for calculating the volume of a solid of revolution,
when integrating along an axis perpendicular to the axis of revolution.
This is in contrast to disc integration which integrates along the axis parallel to the axis of revolution.

Consider a volume in three dimensions obtained by rotating a cross-section in the $xy$-plane around the $y$-axis.
Suppose the cross-section is defined by the graph of the positive function $f(x)$ on the interval $[a, b]$.
Then the formula for the volume will be

\begin{equation}
	V = 2 \pi \int_a^b x f(x) dx
\end{equation}

If the function is of the $y$ coordinate and the axis of rotation is the $x$-axis then the formula becomes

\begin{equation}
	V = 2 \pi \int_a^b y f(y) dy
\end{equation}

## Infinite Sequences and Series

(WIP)

## Ordinary Differential Equations (ODE)

### Linear ODE

\begin{equation}
\label{eq:ode-linear}
\frac{d}{dt} y(t) = a y + b
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
y(t) = e^{at+C} - \frac{b}{a}
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
y(t)
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
\frac{d}{dt} y(t) = a y(b-y)
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

# Exercise Problems

## Differentiation & Integration

<ul>
<li>
<strong>Varsity Tutors Problem</strong>
Evaluate $f'(1)$ when $f(x) = \int_0^x (6t^2 - 3t + 10) dt$.

<p>
<strong>Answer</strong>
$$
13
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Evaluate:

$$
	\int_0^{\infty} \frac{\cos x}{e^x} dx
$$

<p>
<strong>Answer</strong>
$$
\frac{1}{2}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Evaluate:

$$
	\int_0^{\infty} \frac{x}{e^{x^2}} dx
$$

<p>
<strong>Answer</strong>
$$
\frac{1}{2}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Evaluate:

$$
	\int_0^{\infty} \frac{\cos x}{e^{x^2}} dx
$$

<p>
<strong>Answer</strong>
$$
\frac{1}{2}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Find $\frac{dy}{dx}$ if $x^3-x\ln y=ye^x$.
<p>

<strong>Answer</strong>
$$
	\frac{dy}{dx} = \frac{3x^2y-y\ln y - y^2 e^x}{e^x y+x}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Find $dy/dx$:
$$
	y = \tan^{-1} (2x(x+1)^{10}))
$$

<p>
<strong>Answer</strong>
$$
	\frac{dy}{dx} = \frac{2(x+1)^9 (11x+1)}{1+4x^2(x+1)^{20}}
$$
</p>
</li>
<li>
<strong>Varsity Tutors Problem</strong>
What is the derivative of $r=7\sin\theta -6$?

<p>
<strong>Answer</strong>
$$
	\frac{dy}{dx}
	=
		\frac{7\sin 2\theta - 6 \cos\theta}{7\cos 2\theta + 6\sin\theta}
	=
		\frac{14\cos\theta \sin\theta - 6 \cos\theta}{7 - 14\sin^2\theta + 6\sin\theta}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Let $f(x) = \cos(4x)$ on the interval $(0,\pi/2)$.
Find a value for the number(s) that
satisfies the [mean value theorem](#mean-value-theorem)
for this function and interval.

<p>
<strong>Answer</strong>
$$
	\frac{\pi}{4}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Approximate

$$
\int_1^2 x^2 \ln x \, dx
$$

using the midpoint rule with $n=5$. Round your answer to three decimal places.

<p>
<strong>Answer</strong>
$$
	1.064
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Approximate

$$
\int_0^{\pi/4} \tan^2 x \, dx
$$

using the trapezoidal rule with $n=4$. Round your answer to three decimal places.

<p>
<strong>Answer</strong>
$$
	0.227
$$
</p>
</li>
</ul>

## Length & Distance & Velocity & Acceleration & Energy

<ul>
<li>
<strong>Varsity Tutors Problem</strong> Given the velocity function

$$
	v(t) = \int_0^{t^2+2t+1} z^d \sin(z^5)\,dz
$$

where $d$ is real number such that $d\in(0,1)$,
find the acceleration function $a(x)$

<p>
<br>
<span class="emph">Daddy's Solution</span>

We use
<!--
the [chain rule](#chain-rule),
<i>i.e.</i>,
\eqref{eq:chain-rule}
and
-->
the first part of <a href="#fundamental-theorem-of-calculus">the fundamental theorem of calculus</a>
<i>i.e.</i>,
\eqref{eq:fund-theorem-of-calculus-1}
to get

$$
\begin{eqnarray*}
	a(t)
	&=& \frac{d}{dt} v(t) = (2t+2) (t^2+2t+1)^d \sin((t^2+2t+1)^5)
\\
	&=& 2(t+1)^{2d+1} \sin((t+1)^{10})
\end{eqnarray*}
$$

by noting that $t^2+2t+1=(t+1)^2$.

</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Given $\vec{r}(t) = (5t^3, e^{11t}, e^{5t})$.
Calculate $\dfrac{d}{dt} \vec{r}(t)$.

<p>
<strong>Answer</strong>
$$
	\frac{d}{dt} \vec{r}(t) = (15t^2, 11e^{11t}, 5e^{5t})
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Find the equation for the velocity of a particle if the acceleration of the particle is given by

$$
	a(t) = 16 t^2 + 48
$$

and the velocity at time $t=0$ of the particle is $30$.

<p>
<strong>Answer</strong>
$$
	v(t)
	=
	\frac{16}{3} t^3 + 48 t + 30
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
What is the length of the curve $g(x) = x^{3/2}$ over the interval $0\leq x\leq 4$?

<p>
<span class="emph">Daddy's Solution</span>
$$
\begin{eqnarray*}
	\int_{0}^4 \sqrt{1+g'(x)^2}\, dx
	&=&
		\int_{0}^4 \sqrt{1+\frac{9}{4}x} \,dx
\\
	&=&
		\frac{4}{9} \cdot \frac{2}{3} \left.\left(1+\frac{9}{4}x\right)^{3/2}\right|_{x=0}^4
\\
	&=&
		\frac{8}{27} (10\sqrt{10}-1)
\end{eqnarray*}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong> Given $x=t+10$ and $y=2t-9$,
what is the arc length between $0\leq t\leq 4$?

<p>
<strong>Answer</strong>
$$
	4\sqrt{5}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Find the length of the following parametric curve

$$
	x = e^t \cos(t),\;
	y = e^t \sin(t),\;
	0 \leq t \leq 2\pi.
$$

	<ol>
	<li>
		$\sin(t)+\cos(t)$
	</li>
	<li>
		$e^t \cos(t)$
	</li>
	<li>
		$1$
	</li>
	<li>
		$e^{2\pi}$
	</li>
	<li>
		$\sqrt{2} (e^{2\pi} -1)$
	</li>
	</ol>

<p>
<br>
<span class="emph">Daddy's Solution</span>

Note first that the length of the curve can be calculated by

$$
	\int_0^{2\pi} |\vec{v}(t)| dt
$$

where $\vec{v}(t)$ is the velocity vector.

Now the displacement (<i>i.e.,</i> location) vector is given by

$$
\vec{d}(t) = (x(t), y(t)) = (e^t \cos t, e^t \sin t)
$$

hence the velocity vector can be calculated as

$$
\vec{v}(t)
=
	\frac{d}{dt} \vec{d}(t)
=
	\left( \frac{d}{t} x(t), \frac{d}{dt} y(t) \right)
=
	(e^t(\cos t - \sin t), e^t (\sin t + \cos t))
$$

and the size of $\vec{v}(t)$ is

$$
\begin{eqnarray*}
|\vec{v}(t)|
	&=&
		e^t \sqrt{(\cos t - \sin t)^2 + (\cos t + \sin t)^2}
\\
	&=&
		e^t \sqrt{(\cos t - \sin t)^2 + (\cos t + \sin t)^2}
\\
	&=&
		\sqrt{2}\, e^t
\end{eqnarray*}
$$

Therefore the length can be calculated as

$$
	\int_0^{2\pi} |\vec{v}(t)| dt = \sqrt{2} \int_0^{2\pi} e^t dt
	= \sqrt{2} \, \left.\left( e^t \right)\right|_{t=0}^{2\pi}
	= \sqrt{2} (e^{2\pi} -1)
$$

</p>
</li>

<!--li>
Find the work done by gravity exerting an acceleration of - 10 m/s<sup>2</sup>
for a 10kg block down 5m from its original position with no initial velocity.
Remember that
	<ul>
	<li>
		$F_\mathrm{grav} = \mathrm{mass} \times \mathrm{acceleration}$
	</li>
	<li>
		$W = \int_a^b F(x) \, dx$,
		where $F(x)$ is a force measured in Newtons,
		$W$ is work measured in Joules,
		and $a$ and $b$ are initial and final positions respectively.
	</li>
	</ul>
</li-->
</ul>

## Polar Coordinates

<ul>
<li>
<strong>Varsity Tutors Problem</strong> What is the polar form of $y=-7x^2$?
</li>

<p>
<strong>Answer</strong>
$$
	r(\theta)
	=
	- \frac{\sin\theta}{7\cos^2\theta}
	=
	- \frac{1}{7} \tan\theta \sec\theta
$$
</p>
</ul>

## Differential Equations

<ul>
<li>
Problem 4 of <a target="_blank" href="https://sungheeyun-photos-01.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/chapter6_test.pdf">AP Calculus (BC) Chapter 6 Test</a>
&ndash;
Given the logistic differential equation $\dfrac{dA}{dt} = A\left(20-\dfrac{A}{4}\right)$
where $A(0) = 15$, what is $\lim_{t\to\infty} A(t)$?

<p>
<br>
<span class="emph">Daddy's Solution 1</span>

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
<span class="emph">Daddy's Solution 2</span>

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
<br>
<span class="emph">Daddy's Solution</span>
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
<br>
<span class="emph">Daddy's Solution 1</span>

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
<span class="emph">Daddy's Solution 2</span>

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

## Infinite Sequences and Series

<ul>
<li>
<strong>Varsity Tutors Problem</strong>
Calculate the sum of a geometric series with the following values:

$$
n=10,\;
a_1 = 11,\;
r = \frac{2}{20}
$$

rounded to the nearest integer.

<p>
<strong>Answer</strong>
$$
	12
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
For the series $\sum_{n=0}^\infty (-1)^n (\frac{n^n}{8^n})$,
determine if the series converge or diverge.
If it diverges, choose the best reason.

<p>
<strong>Answer</strong>
The series diverges, since $\lim_{n\to\infty} x_n \neq0$.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Determine if the series converges or diverges. You do not need to find the sum.

$$
	\sum_{n=1}^\infty \frac{1}{n^3+2}
$$

<p>
<strong>Answer</strong>
The series converges.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Find the interval of convergence of $x$ for the series

$$
	\sum_{n=1}^\infty \frac{3^n x^n}{n!}
$$

<p>
<strong>Answer</strong>
$$
(-\infty, \infty)
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Which of the following series does not converge?

	<ol>
	<li>
		$\sum_{i=0}^\infty \frac{n!}{n^2\cos(n)}$
	</li>
	<li>
		$\sum_{i=0}^\infty \frac{n-1}{n^3+1}$
	</li>
	<li>
		$\sum_{i=0}^\infty 0.9999999999999999999^n$
	</li>
	<li>
		$\sum_{i=0}^\infty \frac{(-1)^n}{n}$
	</li>
	<li>
		$\sum_{i=0}^\infty \frac{n^2 \ln(n)}{n!}$
	</li>
	</ol>

<p>
<strong>Answer</strong>
1.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Which of following intervals of convergence cannot exist?

	<ol>
	<li>
		$[2,\infty)$
	</li>
	<li>
		For any $q$, $p$ such that $q\leq p$, the interval $[q,p]$
	</li>
	<li>
		$[2,10000)$
	</li>
	<li>
		For any $\epsilon >0$, the interval $[a-\epsilon,a+\epsilon]$ for some $a\in\reals$
	</li>
	</ol>

<p>
<strong>Answer</strong>
1.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Determine whether

$$
	\sum_{n=1}^\infty (-1)^n \sin (1/n)
$$

converges or diverges, and explain why.

<p>
<strong>Answer</strong>
The series (conditionally) converges,
which can be confirmed by the alternating series test.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Determine whether the following series converges or diverges:

$$
	\sum_{n=0}^\infty (-1)^n \left(\frac{5}{n}\right)
$$

<p>
<strong>Answer</strong>
The series (conditionally) converges,
which can be confirmed by the alternating series test.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
One of the following infinite series converges. Which is it?

	<ol>
	<li>
		$\sum_{k=1}^\infty \frac{1}{k}$
	</li>
	<li>
		$\sum_{k=1}^\infty \frac{\sin(k)}{k^2}$
	</li>
	<li>
		$\sum_{k=1}^\infty (-1)^k \sin(k)$
	</li>
	<li>
		$\sum_{k=2}^\infty \frac{k}{\ln(k)}$
	</li>
	<li>
		None of the others converge.
	</li>
	</ol>

<p>
<strong>Answer</strong>
2.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Determine the nature of convergence of the series having the general term:

$$
	\frac{8}{\sqrt{n(n+1)(n+2)}}
$$

	<ol>
	<li>
		$\frac{\pi}{7}$
	</li>
	<li>
		$\frac{\pi}{5}$
	</li>
	<li>
		The series is convergent.
	</li>
	<li>
		$\frac{1}{2}$
	</li>
	<li>
		The series is divergent.
	</li>
	</ol>

<p>
<strong>Answer</strong>
3.
</p>
</li>
</ul>

## Taylor Series and Approximation

<ul>
<li>
<strong>Varsity Tutors Problem</strong>
Write out the first three terms of the Taylor series about $a=1$ for the following function.

$$
f(x) = x^2 + e^x
$$

<p>
<strong>Answer</strong>
$$
\begin{eqnarray*}
	f(x) &\simeq& f(1) + f'(1) (x-1) + \frac{1}{2!} f^{\prime\prime}(x) (x-1)^2
\\
	&=&
		1 + e + (2+e)(x-1) + \frac{1}{2} (2+e)(x-1)^2
\end{eqnarray*}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Write the first three terms of the Taylor series for the following function about $x=1$:

$$
f(x) = x^2 + 3x + 2
$$

<p>
<strong>Answer</strong>
$$
\begin{eqnarray*}
	f(x) &\simeq& f(1) + f'(1) (x-1) + \frac{1}{2!} f^{\prime\prime}(x) (x-1)^2
\\
	&=&
		6 + 5(x-1) + (x-1)^2
\end{eqnarray*}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
For which of the following functions can the Maclaurin series representation be expressed in four or fewer non-zero terms?

	<ol>
	<li>
		$f(x) = x^5/3+2$
	</li>
	<li>
		$f(x) = x^2 + \sqrt{x} + 1$
	</li>
	<li>
		$f(x) = \ln |x + 3|$
	</li>
	<li>
		$f(x) = x + 3 \sin(x)$
	</li>
	</ol>

<p>
<strong>Answer</strong>
1.
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
