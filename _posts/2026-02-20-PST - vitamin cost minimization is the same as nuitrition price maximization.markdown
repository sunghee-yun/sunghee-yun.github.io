---
title: "(WIP) Vitamin cost minimization is equivalent to nuitrition price maximization!"
date: Fri Feb 20 17:20:13 PST 2026
last_modified_at: Sun Feb 22 22:55:04 PST 2026
permalink: /math/cvxopt/duality/vitamin
categories:
 - blog
tags:
 - convex optimization
 - math
 - duality
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

{% assign strategic_ignorance = site.posts | where: "permalink", "/prajna/wisdom-of-strategic-ignorance" | first %}
{% assign ai_reason = site.posts | where: "permalink", "/ai/reason" | first %}
{% assign musical_notes = site.posts | where: "permalink", "/prajna/wonders/richness-of-musical-notes" | first %}
{% assign salzburg = site.posts | where: "permalink", "/ai/bridging-technology-and-humanity" | first %}
{% assign why_do_we_live = site.posts | where: "url", "/blog/PST-Why-do-we-live/" | first %}

# Vitamin cost minimzation problem

Assume $\newcommand{\reals}{\mathbb{R}}\newcommand{\preals}{\reals_+}m$ different nutritions and $n$ different vitamins each of which contains the nutritions.
Further assume that $A_{i,j}\in\preals$ ($1\leq i\leq m$, $1\leq j\leq n$) is
the amount the $i$th nutrition that one unit of the $j$th vitamin contains,
and the cost of one unit of $j$th vitamin is $c_j \in \preals$ ($1\leq j\leq n$).

Now we want to minimize the total cost of vitamins
while the total amount of the $i$th nutrition taken is at least $b_i \in \preals$ ($1\leq i\leq m$).
For example, $b_i$ can be the minimum recommended amount of the $i$th nutrition that should be taken daily.

We define the following matrix and vectors containing these information.

$$
\begin{eqnarray}
\label{eq:data-a}
A
=
\begin{bmatrix}
A_{1,1} & A_{1,2} & \cdots & A_{1,n}
\\
A_{2,1} & A_{2,2} & \cdots & A_{2,n}
\\
\vdots & \vdots & \ddots & \vdots
\\
A_{m,1} & A_{m,2} & \cdots & A_{m,n}
\\
\end{bmatrix}
\in \preals^{m\times n}
\end{eqnarray}
$$

$$
\begin{eqnarray}
\label{eq:data-b}
b
=
\begin{bmatrix}
b_1
\\
b_2
\\
\vdots
\\
b_m
\end{bmatrix}
\in \preals^{m}
\end{eqnarray}
$$

$$
\begin{eqnarray}
\label{eq:data-c}
c
=
\begin{bmatrix}
c_1
\\
c_2
\\
\vdots
\\
c_n
\end{bmatrix}
\in \preals^{n}
\end{eqnarray}
$$

Suppose that we take
$x_1$ units of the 1st vitamin,
$x_2$ units of the 2nd vitamin,
&hellip;,
$x_n$ units of the $n$th vitamin.
Define a vector

$$
\begin{eqnarray}
\label{eq:var-x}
x
=
\begin{bmatrix}
x_1
\\
x_2
\\
\vdots
\\
x_n
\end{bmatrix}
\in \reals^{n}
\end{eqnarray}
$$

Then the total cost is

\begin{equation}
\label{eq:cost}
c^T x = c_1 x_1 + \cdots + c_n x_n.
\end{equation}

The $i$th constraint that the total amount of the $i$th nutrition should be no less than $b_i$
can be expressed as

\begin{equation}
\label{eq:cnst-i}
A_{i,1} x_1 + \cdots + A_{i,n} x_n \geq b_i
\end{equation}

for $1\leq i\leq m$.
These $m$ inequalities can be compactly expressed using the matrix-vector multiplication as

\begin{equation}
\label{eq:cnst}
Ax \geq b.
\end{equation}

# Primal and dual problems

## Primal problem

Using \eqref{eq:cost} and \eqref{eq:cnst},
the vitamin cost minimization problem can be
expressed as

$$
\begin{eqnarray}
\label{eq:primal-prob}
\begin{array}{ll}
	\mbox{minimize} & c^Tx
	\\
	\mbox{subject to} & A x \geq b
	\\
	& x \geq 0
\end{array}
\end{eqnarray}
$$

where the optimization variable is $x\in\reals^n$.
This problem is also called the <span class="emph">primal problem</span>
(as opposed to the dual problem as will become clear momentarily).

## Lagrangian

The <span class="emph">Lagrangian</span> $L: \reals^n \times \reals^m \times \reals^n \to \reals$ is defined by

\begin{equation}
\label{eq:lagrangian}
L(x,\tilde{\lambda}, {\bar{\lambda}})
	= c^T x + {\tilde{\lambda}}^T(b-Ax) - {\bar{\lambda}}^T x
	= (c - A^T {\tilde{\lambda}} - {\bar{\lambda}})^T x + {\tilde{\lambda}}^T b.
\end{equation}

Here the two variables
$\tilde{\lambda}\in\reals^m$
and
$\bar{\lambda}\in\reals^n$
are called
<span class="emph">Lagrange dual variables</span>
or
<span class="emph">Lagrange multipliers</span>.

## Lagrange dual function

The <span class="emph">Lagrange dual function</span> $g: \reals^m \times \reals^n \to \reals$ is defined to be
the infimum of the Lagrangian over $x$,
*i.e.*,

$$
\begin{eqnarray}
g({\tilde{\lambda}}, {\bar{\lambda}})
	=
	\inf_{x\in\reals^n} L(x,\tilde{\lambda}, {\bar{\lambda}})
	=
	\left\{\begin{array}{ll}
		b^T {\tilde{\lambda}} & \mbox{if } A^T{\tilde{\lambda}} + {\bar{\lambda}} = c,
		\\
		- \infty & \mbox{otherwise.}
	\end{array}\right.
\end{eqnarray}
$$

## Dual problem

The dual problem is defined by
the maximization problem of the Lagrange dual function
over the positive orthants of Lagrange dual variables,
*i.e.*,

$$
\begin{eqnarray}
\label{eq:dual-prob-01}
\begin{array}{ll}
	\mbox{maximize} & b^T {\tilde{\lambda}}
	\\
	\mbox{subject to} & A^T {\tilde{\lambda}} + {\bar{\lambda}} = c
	\\
	& {\tilde{\lambda}} \geq 0
	\\
	& {\bar{\lambda}} \geq 0
\end{array}
\end{eqnarray}
$$

where the optimization variables are $\tilde{\lambda}\in\reals^m$ and $\bar{\lambda}\in\reals^n$,
which is equivalent to

$$
\begin{eqnarray}
\label{eq:dual-prob}
\begin{array}{ll}
	\mbox{maximize} & b^T \lambda
	\\
	\mbox{subject to} & A^T \lambda \leq c
	\\
	& \lambda \geq 0
\end{array}
\end{eqnarray}
$$

where the optimization variables are ${\lambda}\in\reals^m$.

The problem \eqref{eq:dual-prob-01} (hence, \eqref{eq:dual-prob}, too) is called <span class="emph">the dual problem</span> of the (primal) problem \eqref{eq:primal-prob}.

## The problem the dual problem solves!

To examine this,
let's examine the unit of the Lagrange dual variables, $\tilde{\lambda}$ and $\bar{\lambda}$,
using the equation of the Lagrangian \eqref{eq:lagrangian}.

Suppose that the unit of $x_j$ is &ldquo;vitamin-unit&rdquo;,
the unit of $c_j$ is &ldquo;USD / vitamin-unit&rdquo;,
and
the unit of $b_i$ is &ldquo;nutrition-unit&rdquo;.
Then the unit $A_{i,j}$ should be &ldquo;nutrition-unit / vitamin-unit&rdquo;.
(For example, the nuitrition-unit can be milligram and the vitamin-unit can be gram.)

Now in \eqref{eq:lagrangian},
because the unit of $c^Tx$ is USD,
the units of the other terms should also be USD,
which implies

- the unit of $\tilde{\lambda}$ (and $\lambda$) is &ldquo;USD / nutrition-unit&rdquo;
- the unit of $\bar{\lambda}$ is &ldquo;USD / vitamin-unit&rdquo;

Now to simplify things, let us focus only on the dual problem of the second form,
*i.e.*, \eqref{eq:dual-prob}
and the associated Lagrange dual variable $\lambda\in\reals^m$.

Then
the unit of (the components of) $A^T\lambda$ becomes &ldquo;USD / vitamin-unit&rdquo;,
hence the unit of $A^T\lambda$ is the same as that of $c$,
thus the LHS and RHS of the 1st constraint of \eqref{eq:dual-prob} are comparable, *i.e.*, they are compatible.

Also the unit of the objective function of \eqref{eq:dual-prob} becomes USD.<sup><a href="#footnote1" id="ref1">1</a></sup>

Now observe that we've derived the formula for the dual problem
by deriving equations using the definitions of the Lagrangian and the Lagrange dual function
without intentionally providing any meaning to any of the mathematical terms derived during these processes.

However, consequently, by observing the units of the Lagrange dual variables,
we can interpret the dual problem as follows.

The dual problem is <span class="emph">the total nutrition price maximization problem</span>
with constraints that the cost required to make one unit of the $j$th vitamin should never exceed $c_j$ for $1\leq j\leq n$
because the $j$th component of the 1st constraint of \eqref{eq:dual-prob} is

$$
A_{1,j} \lambda_1 + A_{2,j} \lambda_2 + \cdots + A_{m,j} \lambda_m \leq c_j.
$$

So we can give these interpretation.

1. The primal problem is what vitamin consumers want to solve to minimize the cost to buy vitamins
while taking minimum recommended required amount of nutritions.
1. The dual problem is what nutrition providers (those who sell nutritions to vitamin manufacturers)
want to solve to maximize their profits while preventing the cost of vitamin manufacturing from exceeding
the vitamin price.

Three things are amazing and beautiful!

1. We never intended to give this meaning to the dual problem, but just followed the definition of the Lagrangian and the Lagrange dual function
to derive the formula of the dual problem.
1. As we will see momentarily, the optimal values for the problems are <strong style="color: red;">*always*</strong>
the same! Also, solving one problem readily solves the other. This is like magic,
but can be mathematically rigorously proved!
1. The primal and dual optimal solutions have very interesting and beautiful properties.
Refer to [Interpretation of KKT conditions](#interpretation-of-kkt-conditions) for detailed explanation.

# What Strong Duality implies

Suppose that $x^\ast$ is the optimal solution of the primal problem \eqref{eq:primal-prob}
and $\lambda^\ast$ is that of the dual problem \eqref{eq:dual-prob}.

Then the [weak duality](/math/rig/convex-optimization#definition:weak---duality){:target="_blanK"}
implies that

$$
	b^T \lambda^\ast \leq c^T x^\ast.
$$

The [Slater's theorem](/math/rig/convex-optimization#theorem:Slater's---theorem){:target="_blanK"}
implies that the [strong duality](/math/rig/convex-optimization#definition:strong---duality){:target="_blanK"}
holds for our case, hence
the optimal values of \eqref{eq:primal-prob} and \eqref{eq:dual-prob} are the same,
*i.e.*,

$$
	b^T \lambda^\ast = c^T x^\ast.
$$

This means the vitamin cost minimization problem and the nutrition price maximization problem
is essentially the same!


# KKT conditions

The KKT conditions imply that
$x^\ast$, ${\tilde{\lambda}}^\ast$, and ${\bar{\lambda}}^\ast$
are the primal and dual optimal solutions with zero duality gap
if and only if

- the primal feasibility

$$
Ax^\ast \geq b
$$

$$
x^\ast \geq 0
$$

- the dual feasibility

$$
{\tilde{\lambda}}^\ast \geq 0
$$

$$
{\bar{\lambda}}^\ast \geq 0
$$

- the complementary slackness

$$
\begin{array}{ll}
	\tilde{\lambda}^\ast_i (Ax^\ast - b)_i = 0
		&\mbox{for } 1 \leq i \leq m
\\
	\bar{\lambda}^\ast_j x_j^\ast = 0
		&\mbox{for } 1 \leq j \leq n
\end{array}
$$

- the vanishing gradient of Lagrangian

$$
A^T \tilde{\lambda}^\ast + \bar{\lambda}^\ast = c
$$

Or equivalently,
$x^\ast$ and $\lambda^\ast$
are the primal and dual optimal solutions with zero duality gap
if and only if

- the primal feasibility

$$
Ax^\ast \geq b
$$

$$
x^\ast \geq 0
$$

- the dual feasibility

$$
{\lambda}^\ast \geq 0
$$

- the complementary slackness

$$
\begin{array}{ll}
	{\lambda}^\ast_i (Ax^\ast - b)_i = 0
		&\mbox{for } 1 \leq i \leq m
\\
	(c - A^T{\lambda}^\ast)_j x_j^\ast = 0
		&\mbox{for } 1 \leq j \leq n
\end{array}
$$

# Interpretation of KKT conditions {#interpretation-of-kkt-conditions}

---

<ol>
<li id="footnote1">
	This should be true by design, that is, by the definition of Lagrangian,
	the unit of the objective function of the dual problem
	and that of the primal problem should be the same.
	&nbsp;<a href="#ref1">↩</a></li>
</ol>
