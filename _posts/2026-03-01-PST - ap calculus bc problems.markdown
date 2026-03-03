---
date: Mon Mar  2 23:13:06 PST 2026
last_modified_at: Tue Mar  3 03:04:16 PST 2026
title: "AP Calculus BC for the person I love (most)!"
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

# Pattern Analysis

## Differentiation / Derivatives

### Chain rule

\begin{equation}
\label{eq:chain-rule}
\frac{d}{dx} f(g(x)) = f'(g(x)) g'(x)
\end{equation}

### Derivatives of inverse trigonometric functions

$$
\begin{eqnarray}
\label{eq:der-inverse-tri}
\begin{array}{rcl}
\dfrac{d}{dx} \arcsin(x) &=& \dfrac{1}{\sqrt{1-x^2}}
\\
\dfrac{d}{dx} \arccos(x) &=& - \dfrac{1}{\sqrt{1-x^2}}
\\
\dfrac{d}{dx} \arctan(x) &=& \dfrac{1}{1+x^2}
\end{array}
\end{eqnarray}
$$

More formula can be found [here](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Derivatives_of_inverse_trigonometric_functions){:target="_black"}!

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
\label{eq:int-inverse-tri}
\begin{array}{rcl}
\int \arcsin(x) dx &=& x \arcsin(x) + \sqrt{1-x^2} + C
\\
\int \arccos(x) dx &=& x \arccos(x) - \sqrt{1-x^2} + C
\\
\int \arctan(x) dx &=& x \arctan(x) - \frac{1}{2} \log(x^2+1) + C
\end{array}
\end{eqnarray}
$$

You can easily verify these formulas, *e.g.*, using formulas in \eqref{eq:der-inverse-tri}.
More formula can be found [here](https://en.wikipedia.org/wiki/List_of_integrals_of_inverse_trigonometric_functions){:target="_black"}!

## Ordinary Differential Equations (ODE)

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
For more information, please refer to [Logistic function Wikipedia Page](https://en.wikipedia.org/wiki/Logistic_function){:target="_black"}.

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


## Unit 6

<ul>
<li>
Given the logistic differential equation $\dfrac{dA}{dt} = A\left(20-\dfrac{A}{4}\right)$
where $A(0) = 15$, what is $\lim_{t\to\infty} A(t)$?

<p>
<strong>Solution 1</strong>

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
<strong>Solution 2</strong>

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
</ul>

