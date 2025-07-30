---
title: "Linear Algebra"
date: Wed Jul 30 10:40:27 PDT 2025
last_modified_at: Wed Jul 30 15:11:43 PDT 2025
permalink: /math/rig/linear-algebra
categories:
 - blog
tags:
 - math
 - linear algebra
toc: true
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
usemathjax: true  # for LaTeXing
---

<style>
table, tr, td, th {
    font-size: inherit !important;
    font-family: inherit !important;
}
th {
	text-align: center !important;
}
tr:nth-child(even) {
	background-color: inherit !important;
}
</style>

$$
\newcommand{\reals}{\mathbb{R}}
\newcommand{\complexes}{\mathbb{C}}
\newcommand{\integers}{\mathbb{Z}}
\newcommand{\Prob}{\mathop{\bf Prob}}
\newcommand{\Expect}{\mathop{\bf E{}}}
\newcommand{\sign}{\mathop{\bf sign}}
\newcommand{\innerp}[2]{\langle{#1},{#2}\rangle} % inner product
\newcommand{\lspan}[1]{\langle{#1}\rangle} % linear span
$$

<!--tags: {% for tag in page.tags %} <a href="/tags/#{{ tag }}">{{ tag }}</a> {% endfor %}
<br>
cats: {% for category in page.categories %} <a href="/categories/#{{ category }}">{{ category }}</a> {% endfor %}-->

posted: {{ page.date| date: "%d-%b-%Y" }}
&amp;
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

{% assign linalg_story = site.posts | where: "permalink", "/math/linear-algebra" | first %}

# Vector spaces

## Definition

For the definition of the vector space
and other related concepts,
refer to [this section](/math/linear-algebra#definition) in [{{ linalg_story.title }}]({{ linalg_story.url }}).

## Linear independence &amp; linear dependence

<div class="definition">
A set of vectors is said to be <span class="define">linearly dependent</span>
if there exists a non-trivial linear relation among them.
Otherwise,
the set is said to be <span class="define">linearly independent</span>.
</div>

<div class="theorem">
If $x$ is linearly dependent on $\{y_i\}$
and each $y_i$ is linearly dependent on $\{z_j\}$,
$x$ is linearly dependent on $\{z_j\}$.
</div>

<div class="definition">
For a subset $A$ of a vector space $V$,
the set of all linear combinations of vectors in $A$
is called the set <span class="define">spanned</span> by $A$,
and we denote it by <span class="notation">$\lspan{A}$</span>.
</div>

<div class="theorem" id="theorem:linear-dependence">
A set of nonzero vectors $\{x_1, x_2, \ldots\}$ is linearly dependent
if and only if
some $x_k$ is a linear combination of $x_1,\ldots,x_{k-1}$.
</div>

<div class="theorem">
A set of nonzero vectors $\{x_1,x_2,\ldots\}$ is linearly independent
if and only if
for each $k$, $x_k \notin \lspan{\{x_1,\ldots,x_{k-1}\}}$.
</div>

<div class="theorem" id="theorem:sdf">
For two subsets $A, B \subset V$ such that $A\subset \lspan{B}$,
$\lspan{A} \subset \lspan{B}$.
</div>

<div class="theorem">
For a subset $A\subset V$,
if $x\in A$ is dependent on some other vectors in $A$,
$\lspan{A} = \lspan{A-\{x\}}$.
</div>

<div class="theorem">
For any subset $A\subset V$,
$\lspan{\lspan{A}}= \lspan{A}$.
</div>

<div class="theorem">
If a finite set $\{x_1,\ldots,x_n\}$ spans $V$,
every linearly independent set contains at most $n$ elements.
</div>

## Bases of vector spaces

<div class="definition">
A linearly independent set spanning a vector space $V$
is called a <span class="define">basis</span> or <span class="define">base</span>
(the plural is <span class="define">bases</span>) of $V$.
</div>

<div class="theorem" id="theorem:bases-have-same-cardinality">
If a vector space has one basis with a finite number of elements,
then all other bases are finite and have the same number of elements.
</div>

<div class="theorem">
Any $n+1$ vectors in an $n$-dimensional vector space are linearly dependent.
</div>

<div class="theorem">
A set of $n$ vectors in an $n$-dimensional vector space is a basis if and only if it is linearly independent.
</div>

<div class="theorem">
A set of $n$ vectors in an $n$-dimensional vector space $V$ is a basis if and only if it spans $V$.
</div>

<div class="theorem">
In a finite dimensional vector space $V$,
every set spanning $V$ contains a basis.
</div>

<div class="theorem">
In a finite dimensional vector space,
any linearly independent set of vectors can be extended to a basis.
</div>

## Subspaces

<div class="definition">
A subspace $W$ of a vector space $V$
is a nonempty subset of $V$ which is itself a vector space
with respect to the operations of addition and scalar multiplication
defined in $V$.
In particular,
the subspace must be a vector space over the same field $F$
</div>

<div class="theorem">
The intersection of any collection of subspaces is a subspace.
</div>

<div class="theorem">
For a vector space and $V$ and $A\subset V$,
the smallest subspace containing $A$ is the subspace spanned by $A$,
<i>i.e</i>,

$$
\lspan{A}
=
\bigcap_{W:\;\text{subspace with } A \subset W} W.
$$
</div>

<div class="theorem">
For two subspaces $W_1$ and $W_2$ of a vector space $V$,
$W_1+W_2$ is a subspace of $V$.
</div>

<div class="theorem">
For two subspaces $W_1$ and $W_2$ of a vector space $V$,
$W_1+W_2$ is the smallest subspace containing $W_1$ and $W_2$,
<i>i.e.</i>,
$$
W_1 + W_2 = \lspan{W_1\cup W_2}.
$$
If $A_1$ spans $W_1$ and $A_2$ spans $W_2$,
then
$$
\lspan{A_1\cup A_2} = W_1 + W_2.
$$
</div>

<div class="theorem">
A subspace $W$ of an $n$-dimensional vector space $V$
is
a finite dimensional vector space of dimension $m\leq n$.
</div>

<div class="theorem">
For a subspace $W$ of dimension $m$ in an $n$-dimensional vector space $V$,
there exists a basis $\{a_1,\ldots,a_m,a_{m+1},\ldots,a_n\}$ of $V$
such that $\{a_1,\ldots,a_m\}$ is a basis of $W$.
</div>

<div class="theorem">
If two subspaces $U$ and $W$ of a vector space $V$ have the same finite dimension and $U\subset W$,
then $U=W$.
</div>

<div class="theorem">
For two subspaces $W_1$ and $W_2$ of a finite dimensional vector space $V$,
$$
\dim (W_1 + W_2) = \dim W_1 + \dim W_2 - \dim (W_1 \cap W_2).
$$
</div>

<div class="definition">
For two subspaces $W_1$ and $W_2$ of a finite dimensional vector space $V$,
if $W_1\cap W_2 = \{0\}$, the sum $W_1 + W_2$ is said to be <span class="define">direct</span>;
$W_1+W_2$ is said to be a <span class="define">direct sum</span> of $W_1$ and $W_2$.
To indicate that a sum is direct, we use the notation:
<span class="notation">
$$
W_1 \oplus W_2
$$
</span>
</div>

<div class="definition">
For two subspaces $W_1$ and $W_2$ of a finite dimensional vector space $V$,
if $W_1 \oplus W_2 = V$,
$W_1$ and $W_2$ are said to be <span class="define">complementary</span>
and
$W_2$ said to be a <span class="define">complementary subspace</span> of $W_1$,
or a <span class="define">complement</span> of $W_1$.
</div>

<div class="theorem">
For a subspace $W$ of a vector space $V$,
there exists a subspace $W'$ such that $V = W \oplus W'$.
</div>

<div class="theorem">
For a sum of several subspaces of a finite dimensional vector space
to be direct it is necessary and sufficient that
$$
\dim (W_1 + \cdots + W_k) = \dim W_1 + \cdots + \dim W_k.
$$
</div>
