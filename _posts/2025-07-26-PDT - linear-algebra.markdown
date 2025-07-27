---
title: (WIP) Linear Algebra
date: Sat Jul 26 18:29:58 PDT 2025
last_modified_at: Sat Jul 26 18:29:58 PDT 2025
permalink: /math/linear-algebra
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
\newcommand{\kclosure}{\bar{K}}
\newcommand{\Prob}{\mathop{\bf Prob}}
\newcommand{\Expect}{\mathop{\bf E{}}}
$$

<!--tags: {% for tag in page.tags %} <a href="/tags/#{{ tag }}">{{ tag }}</a> {% endfor %}
<br>
cats: {% for category in page.categories %} <a href="/categories/#{{ category }}">{{ category }}</a> {% endfor %}-->

posted: {{ page.date| date: "%d-%b-%Y" }}
&amp;
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

{% assign post = site.posts | where: "permalink", "/prajna/coincidence-vs-inevitability" | first %}

# Vector spaces

In mathematics and physics,
a <span class="emph">vector space</span>
is a set whose elements (called vectors)
can be added together and multiplied or *scaled* by numbers called <span class="emph">scalars</span>.
The operations of <span class="emph">vector addition</span> and <span class="emph">scalar multiplication</span>
must satisfy certain requirements,
called <span class="emph">vector axioms</span>.
Real vector spaces and complex vector spaces are kinds of vector spaces based on different kinds of scalars:
real numbers and complex numbers.
Scalars can also be, more generally, elements of any [field](/math/abstract-algebra#fields---the-realm-of-perfect-division).

<!--
Vector spaces generalize Euclidean vectors, which allow modeling of physical quantities (such as forces and velocity) that have not only a magnitude, but also a direction. The concept of vector spaces is fundamental for linear algebra, together with the concept of matrices, which allows computing in vector spaces. This provides a concise and synthetic way for manipulating and studying systems of linear equations.
-->

<!--
Vector spaces are characterized by their dimension, which, roughly speaking, specifies the number of independent directions in the space. This means that, for two vector spaces over a given field and with the same dimension, the properties that depend only on the vector-space structure are exactly the same (technically the vector spaces are isomorphic). A vector space is finite-dimensional if its dimension is a natural number. Otherwise, it is infinite-dimensional, and its dimension is an infinite cardinal. Finite-dimensional vector spaces occur naturally in geometry and related areas. Infinite-dimensional vector spaces occur in many areas of mathematics. For example, polynomial rings are countably infinite-dimensional vector spaces, and many function spaces have the cardinality of the continuum as a dimension.
-->

Many vector spaces that are considered in mathematics are also endowed with other structures.
This is the case of [algebras](/math/abstract-algebra),
which include field extensions, polynomial rings, associative algebras and Lie algebras.
This is also the case of [topological vector spaces](/math/topological-spaces), which include function spaces, inner product spaces, normed spaces, Hilbert spaces and Banach spaces.

## Definition

A vector space over a [field](/math/abstract-algebra#fields---the-realm-of-perfect-division) $$F$$,
also called $$F$$-vector space is a non-empty set $$V$$ together with a binary operation
and a binary function that satisfy the 8 axioms listed below.
The elements of $$V$$ are commonly called <span class="emph">vectors</span>,
and the elements of $$F$$ are called <span class="emph">scalars</span>.

| axiom | statement |
|:-|:-|
| additive [commutativity](https://en.wikipedia.org/wiki/Commutative_property) | $$(x,y\in V)(x+y=y+x)$$ |
| additive [associativity](https://en.wikipedia.org/wiki/Associative_property) | $$(x,y,z\in V)(x+(y+z)=(x+y)+z)$$ |
| existence of [additive identify](https://en.wikipedia.org/wiki/Additive_identity) | $$(\exists 0\in V)(\forall x\in V)(x+0=x)$$ |
| existence of [additive inverse](https://en.wikipedia.org/wiki/Additive_inverse) | $$(\forall x \in V)(\exists y \in V)(x+y=0)$$ - $$y$$, called <span class="emph">additive inverse</span> of $$x$$, denoted by $$-x$$ |
| multiplicative [associativity](https://en.wikipedia.org/wiki/Associative_property) | $$(\forall x\in V\;\&\;\forall \alpha, \beta \in F)(\alpha(\beta x)=(\alpha\beta)x)$$ |
| multiplicative [identity](https://en.wikipedia.org/wiki/Identity_element) | $$(\forall x\in V)(1x = x)$$ where $$1$$ is the multiplicative identity of $$F$$ |
| [distributivity](https://en.wikipedia.org/wiki/Distributivity) of multiplication over vector addition | $$(\forall x,y \in V \;\&\; \forall \alpha\in F)(\alpha(x+y) = \alpha x + \alpha y)$$ |
| [distributivity](https://en.wikipedia.org/wiki/Distributivity) of multiplication over field addition | $$(\forall x \in V \;\&\; \alpha, \beta \in F)((\alpha+ \beta)x = \alpha x + \beta x)$$ |

Subtraction of two vectors can be defined as

$$
x - y =  x + (-y)
$$

Some of (direct) consequences of the axioms:

- $(\forall x \in V)(0x = 0)$
- $$(\forall \alpha \in F)(\alpha 0 = 0)$$ where $$0$$ is the additive identity
- $(\forall x \in V)((-1)x = -x)$
- $(\forall \alpha \in F \;\&\; \forall x \in V)(\alpha x = 0 \implies \alpha = 0 \mbox{ or } x = 0)$

## Bases, vector coordinates, and subspaces
(WIP)

### Linear combination

For $$x_1,\ldots,x_n\in V$$ and $$\alpha_1, \ldots, \alpha_n\in F$$,

$$
\alpha_1 x_1 + \cdots + \alpha_n x_n \in V
$$

is called a <span class="emph">linear combination</span> of $$x_1, \ldots, x_n$$
where $$\alpha_1, \ldots, \alpha_n$$ are called the *coefficients* of the linear combination.

### Linear independence

The (set of) $$n$$ vectors, $$x_1,\ldots,x_n \in V$$, are said to be <span class="emph">linearly independent</span> if

$$
\alpha_1 x_1 + \cdots + \alpha_n x_n  = 0
\implies
\alpha_1 = \cdots = \alpha_n = 0.
$$

In other words,
a set of vectors is said to be linearly
no vector in the set can be expressed as a linear combination of the other vectors.

### Subspace

A <span class="emph">linear subspace</span> or <span class="emph">vector subspace</span> or just <span class="emph">subspace</span>
of a vector space $$V$$
is a non-empty subset of $$V$$ that is itself a vector space,
*i.e.*,
that is closed under vector addition and scalar multiplication.

Consequently, an intersection of subspaces is itself a subspace.

### Linear span

For a subset $$W$$ of a vector space $$V$$,
the <span class="emph">linear span</span>
or simply <span class="emph">span</span> of $$W$$
is defined by
the smallest subspace of $$V$$ that contains $$W$$.

It can be shown that the span of $$W$$ is the set of all linear combinations of elements of $$W$$.

If $$S$$ is the span of $$W$$,
$$W$$ is said to <span class="emph">span</span> or <span class="emph">generate</span> $$S$$,
and $$W$$ is called a <span class="emph">spanning set</span> or a <span class="emph">generating set</span> of $$S$$.

### Basis and dimension

A subset of a vector space is a <span class="emph">basis</span>
if its elements are linearly independent and span the vector space.
Every vector space has at least one basis
and many in general.
Moreover, all bases of a vector space have the same cardinality, which is called the <span class="emph">dimension</span> of the vector space.
*This is a fundamental property of vector spaces!*

Bases are a fundamental tool for the study of vector spaces,
especially when the dimension is finite.
In the infinite-dimensional case, the existence of infinite bases, often called [Hamel bases](https://en.wikipedia.org/wiki/Hamel_bases),
depends on [the axiom of choice](https://en.wikipedia.org/wiki/Axiom_of_choice).
It follows that, in general, no base can be explicitly described.<sup><a href="#footnote1" id="ref1">1</a></sup>

### Coordinates

Consider a basis $$v_1,\ldots,v_n$$ of a vector space $$V$$ of dimension $$n$$ over a field $$F$$.
Then for every $$x\in V$$,
there exists $$\alpha_1, \ldots, \alpha_n \in F$$ such that

$$
x = \alpha_1 v_1 + \cdots + \alpha_n v_n
$$

The scalars $$a_{1},\ldots ,a_{n}$$ are called the <span class="emph">coordinates</span>
of $$x$$ on the basis.
They are also said to be the <space class="emph">coefficients of the decomposition</space> of $$x$$
on the basis.
One also says that
the $$n$$-tuple of the coordinates is the <span class="emph">coordinate vector</span> of $$x$$
on the basis, since the set $$F^n$$ of the $$n$$-tuples of elements of $$F$$ is itself
a vector space for componentwise addition and scalar multiplication,
whose dimension is $$n$$.

The one-to-one correspondence between vectors and
their coordinate vectors maps vector addition to vector addition and scalar multiplication
to scalar multiplication.
It is thus a [vector space isomorphism](https://en.wikipedia.org/wiki/Vector_space_isomorphism),
which allows translating reasonings and computations on vectors into reasonings and computations
on their coordinates.

## Eigenvalues and eigenvectors

XXX

<hr>
<ol>
<li id="footnote1">
	For example, the real numbers form an infinite-dimensional vector space over the rational numbers,
	for which no specific basis is known.
	&nbsp;<a href="#ref1">↩</a></li>
</ol>
