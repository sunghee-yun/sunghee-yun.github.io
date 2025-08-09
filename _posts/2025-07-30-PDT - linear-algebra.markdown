---
title: "Linear Algebra"
date: Wed Jul 30 10:40:27 PDT 2025
last_modified_at: Sun Aug 10 02:50:56 KST 2025
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

posted: {{ page.date| date: "%d-%b-%Y" }}
&amp;
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

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

{% assign linalg_story = site.posts | where: "permalink", "/math/linear-algebra" | first %}

# NotebookLM Podcasts

- [16:43](https://notebooklm.google.com/notebook/7b158ba3-7c7c-4906-812d-0c5fc1ad0c59/audio)
- [21:46](https://notebooklm.google.com/notebook/38079fa6-3355-400d-b311-17ba76b6e6a5/audio)

# Vector Spaces

## Definition

<div class="definition">
A nonempty set of elements with two laws of combination,
which we call addition and multiplication,
satisfying the following conditions is called a <span class="define">field</span>
and is denoted by <span class="notation">$F$</span>.

<ol>
<li>
	<span class="define">addition</span>
	-
	to every pair of elements $a,b\in F$,
	there is associated a unique element,
	called their <span class="define">sum</span>, which we denote by
	<span class="notation">
	$$
\newcommand{\reals}{\mathbb{R}}
\newcommand{\complexes}{\mathbb{C}}
\newcommand{\integers}{\mathbb{Z}}
\newcommand{\Prob}{\mathop{\bf Prob}}
\newcommand{\Expect}{\mathop{\bf E{}}}
\newcommand{\sign}{\mathop{\bf sign}}
\newcommand{\innerp}[2]{\langle{#1},{#2}\rangle} % inner product
\newcommand{\lspan}[1]{\langle{#1}\rangle} % linear span
\newcommand{\image}{\text{Im}}
		a+b
	$$
	</span>
</li>
<li>
	<span class="mproperty">additive associativity</span>
	-
	addition is associative;
	$$
		(\forall a, b, c \in F)((a+b)+c = a+(b+c)).
	$$
</li>
<li>
	<span class="mproperty">existence of <span class="define">additive identity</span></span>
	-
	there exists an element, which we denote by
	<span class="notation">
	$$
		0
	$$
	</span>
	such that
	$$
		(\forall a\in F)(a+0=a).
	$$
</li>
<li>
	<span class="mproperty">existence of <span class="define">additive inverse</span></span>
	-
	for each $a\in F$, there exists an element, which we denote by
	<span class="notation">
	$$
		-a
	$$
	</span>
	such that
	$$
		a+(-a)=0.
	$$
	Following the usual practice, we write $b+(-a)=b-a$.
</li>
<li>
	<span class="mproperty">additive commutativity</span>
	-
	addition is commutative;
	$$
		(\forall a, b \in F)
		(a+b=b+a).
	$$
</li>
<li>
	<span class="define">multiplication</span>
	-
	to every pair of elements $a,b\in F$,
	there is associated a unique element,
	called their <span class="define">product</span>, which we denote by
	<span class="notation">
	$$
		ab
	$$
	</span>
	or
	<span class="notation">
	$$
		a\cdot b
	$$
	</span>
</li>
<li>
	<span class="mproperty">multiplicative associativity</span>
	-
	multiplication is associative;
	$$
		(\forall a, b, c \in F)
		((ab)c = a(bc)).
	$$
</li>
<li>
	<span class="mproperty">existence of <span class="define">multiplicative identity</span></span>
	-
	there exists an element different from $0$,
	which we denote by
	<span class="notation">
	$$
		1
	$$
	</span>
	such that
	$$
		(\forall a\in F)(a\cdot 1=a)
	$$
</li>
<li>
	<span class="mproperty">existence of <span class="define">additive inverse</span></span>
	-
	for each $a\in F$ with $a\neq0$,
	there exists an element, which we denote by
	<span class="notation">
	$$
		a^{-1}
	$$
	</span>
	such that
	$$
		a\cdot a^{-1}=1.
	$$
</li>
<li>
	<span class="mproperty">multiplicative commutativity</span>
	-
	multiplication is commutative;
	$$
		(\forall a,b \in F)
		(ab=ba).
	$$
</li>
<li>
	<span class="mproperty">multiplicative distributivity over addition</span>
	-
	multiplication is distributive with respect to addition:
	$$
		(\forall a,b,c \in F)
		((a+b)c = ac + bc).
	$$
</li>
</ol>
</div>

<div class="definition">
The elements of a field are called <span class="define">scalars</span>.
</div>

<div class="definition" id="definition:vector-space">
A <span class="define">vector space</span> $V$ over a field $F$
is a nonempty set of elements,
called <span class="define">vectors</span>,
with two laws of combination,
called <span class="define">vector addition</span> (or just <span class="define">addition</span>)
and
<span class="define">scalar multiplication</span>,
satisfying the following conditions.

<ol>
<li>
	<span class="define">vector addition</span>
	-
	to every pair of vectors $x,y\in V$,
	there is associated a unique vector in $V$ called their <span class="define">sum</span>,
	which we denote by
	<span class="notation">
	$$
		x+y.
	$$
	</span>
</li>
<li>
	<span class="mproperty">additive associativity</span>
	-
	vector addition is associative;
	$$
		(\forall x, y, z \in F)((x+y)+z = x+(y+z)).
	$$
</li>
<li>
	<span class="mproperty">existence of <span class="define">additive identity</span></span>
	-
	there exists a vector, which we denote by
	<span class="notation">
	$$
		0
	$$
	</span>
	such that
	$$
		(\forall a\in F)(a+0=a).
	$$
</li>
<li>
	<span class="mproperty">existence of <span class="define">additive inverse</span></span>
	-
	for each $x\in V$, there exists an element, which we denote by
	<span class="notation">
	$$
		-x
	$$
	</span>
	such that
	$$
		x+(-x)=0.
	$$
</li>
<li>
	<span class="mproperty">additive commutativity</span>
	-
	addition is commutative;
	$$
		(\forall x, y \in F)
		(x+y=y+x).
	$$
</li>
<li>
	<span class="define">scalar multiplication</span>
	-
	to every scalar $\alpha\in F$ and vector $x\in V$,
	there is associated a unique vector,
	called the <span class="define">product</span> of $\alpha$ and $x$, which we denote by
	<span class="notation">
	$$
		\alpha x.
	$$
	</span>
</li>
<li>
	<span class="mproperty">multiplicative associativity</span>
	-
	scalar multiplication is associative;
	$$
		(\forall \alpha, \beta \in F \;\&\; \forall x\in V)
		(\alpha(\beta x) = (\alpha\beta)x).
	$$
</li>
<li>
	<span class="mproperty">multiplicative distributivity over vector addition</span>
	-
	scalar multiplication is distributive with respect to vector addition;
	$$
		(\forall \alpha \in F \;\&\; \forall x,y\in V)
		(\alpha(x+y) = \alpha x + \alpha y).
	$$
</li>
<li>
	<span class="mproperty">multiplicative distributivity over scalar addition</span>
	-
	scalar multiplication is distributive with respect to scalar addition;
	$$
		(\forall \alpha, \beta \in F \;\&\; \forall x\in V)
		((\alpha+\beta)x = \alpha x + \beta x).
	$$
</li>
<li>
	For $1\in F$
	$$
		(\forall x \in V)
		(1\cdot x = x).
	$$
</li>
</ol>
</div>

Note that the identical definition of vector space
is given in [this section](/math/linear-algebra#definition) in [{{ linalg_story.title }}]({{ linalg_story.url }}).

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
A <span class="define">subspace</span> $W$ of a vector space $V$
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

<div class="theorem" id="theorem:dimension-of-sum-of-subspaces">
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

# Linear Transformation &amp; Matrices

## Linear transformations

<div class="definition">
Let $U$ and $V$ be vector spaces over a field $F$.
A <span class="define">linear transformation</span> <span class="notation">$\sigma$</span> of $U$ into $V$
is
a single-valued mapping of $U$ into $V$
which associates to each element $x\in U$ a unique element $\sigma(x)\in V$
such that
for all $x,y\in U$ and all $\alpha,\beta \in F$,
$$
	\sigma(\alpha x + \beta y) = \alpha \sigma(x) + \beta \sigma(y).
$$
</div>

<div class="definition">
To describe the special role of the elements of $F$
in the condition $\sigma(\alpha x) = \alpha\sigma(x)$,
we say that
a linear transformation is a <span class="define">homomorphism over $F$</span>
or an <span class="define">$F$-homomorphism</span>.
</div>

<div class="definition">
When a homomorphism is <i>one-to-one</i>,
it is called <span class="define">monomorphism</span>.
</div>

<div class="definition">
When a homomorphism is <i>onto</i>, <i>i.e.</i>, $\sigma(U) = V$,
it is called <span class="define">epimorphism</span>.
</div>

<div class="definition">
A homomorphism that is both an epimorphism and a monomorphism is called an <span class="define">isomorphism</span>.
</div>

<div class="theorem">
The inverse of an isomorphism is also an isomorphism.
</div>

<div class="definition">
If a homomorphism or isomorphism can be defined uniquely by intrinsic properties
independent of a choice of basis,
the mapping is said to be <span class="define">natural</span> or <span class="define">canonical</span>.
</div>

<div class="lemma">
Any two vector spaces of dimension $n$ over a field $F$ are isomorphic.
Such an isomorphism can be established by setting up an isomorphism between each one and $F^n$.
Such an isomorphism, dependent upon the arbitrary choice of bases, is not canonical.
</div>

<div class="theorem">
For a linear transformation $\sigma: U\to V$,
$\sigma(U)=\{\sigma(u)|u \in U\}\subset V$ is a subspace of $V$.
</div>

<div class="definition">
For a linear transformation $\sigma: U\to V$,
the subspace $\sigma(U)$ is called the <span class="define">image</span> of $\sigma$,
and denoted by <span class="notation">$\image(\sigma)$</span>.
</div>

<div class="corollary">
For a linear transformation $\sigma: U\to V$,
if $W$ is a subspace of $U$,
$\sigma(W)$ is a subspace of $V$.
</div>

<div class="definition">
The <span class="define">rank</span>
of a linear transformation $\sigma: U\to V$
is defined by the dimension of the image of $\sigma$,
<i>i.e.</i>,
$\dim \image(\sigma)$,
denoted by <span class="notation">$\rho(\sigma)$</span>.
</div>

<div class="theorem">
For a linear transformation $\sigma: U\to V$,
$$
\rho(\sigma) \leq \min\{\dim U, \dim V\}.
$$
</div>

<div class="theorem">
For a linear transformation $\sigma: U\to V$,
if $W$ is a subspace of $V$,
the set $\sigma^{-1}(W)$ is a subspace of $U$.
</div>

<div class="definition">
For a linear transformation $\sigma: U\to V$,
the subspace $\sigma^{-1}(0)$ is called the <span class="define">kernel</span> of $\sigma$,
and denoted by <span class="notation">$K(\sigma)$</span>.
</div>

<div class="definition">
For a linear transformation $\sigma: U\to V$,
the dimension of $K(\sigma)$ is called the <span class="define">nullity</span> of $\sigma$,
and denoted by <span class="notation">$\nu(\sigma)$</span>.
</div>

<div class="theorem">
For a linear transformation $\sigma: U\to V$,
$$
	\rho(\sigma) + \nu(\sigma) = \dim U.
$$
</div>

<div class="theorem">
A linear transformation $\sigma: U\to V$
is a monomorphism
if and only if
$$
	\nu(\sigma)=0.
$$
</div>

<div class="theorem">
A linear transformation $\sigma: U\to V$
is an epimorphism
if and only if
$$
	\rho(\sigma)=\dim V.
$$
</div>

<div class="theorem" id="theorem:isomorphism-of-vector-spaces-with-same-finite-dimension">
For two vector spaces $U$ and $V$ with $\dim U = \dim V < \infty$,
a linear transformation $\sigma: U\to V$
is isomorphism if and only if it is epimorphism if and only if it is monomorphism.
</div>

<div class="corollary" id="sdf">
<a href="#theorem:isomorphism-of-vector-spaces-with-same-finite-dimension"></a>
implies
a linear transformation $\sigma$ of $U$ into $V$
is an isomorphism if two of the following are satisfied.
<ul>
<li>
$\dim U = \dim V$
</li>
<li>
$\sigma$ is an epimorphism
</li>
<li>
$\sigma$ is a monomorphism
</li>
</ul>
</div>

<div class="theorem" id="theorem:dimension-of-composite">
For three vector spaces $U$, $V$, and $W$ over a field $F$,
and linear transformations $\sigma: U\to V$ and $\tau: V \to W$,
$$
\rho(\sigma) = \rho(\tau\sigma) + \dim \{\image(\sigma)\cap K(\tau)\}.
$$
</div>

<div class="corollary">
For three vector spaces $U$, $V$, and $W$ over a field $F$,
and linear transformations $\sigma: U\to V$ and $\tau: V \to W$,
$$
\rho(\tau\sigma) = \dim \{\image(\sigma) + K(\tau)\} - \nu(\tau).
$$
</div>

<div class="proof">
<a href="#theorem:dimension-of-sum-of-subspaces"></a>
and
<a href="#theorem:dimension-of-composite"></a>
imply
$$
\begin{eqnarray*}
\dim \{\image(\sigma) + K(\tau)\}
	&=&
		\dim \image(\sigma)
		+
		\dim K(\tau)
		-
		\dim \{\image(\sigma) \cap K(\tau)\}
\\
	&=&
		\rho(\sigma) + \nu(\tau) - (\rho(\sigma) - \rho(\tau \sigma))
	=
		\nu(\tau) + \rho(\tau \sigma),
\end{eqnarray*}
$$
hence the proof!
</div>

<div class="corollary">
If $K(\tau) \subset \image(\sigma)$, $\rho(\sigma) = \rho(\tau\sigma) + \nu(\tau)$.
</div>

<div class="theorem">
The rank of a product (<i>i.e.</i>, composition) of two linear transformations
is less than  or equal to the rank of either factor:
$$
\rho(\tau\sigma) \leq \min\{\rho(\tau), \rho(\sigma)\}
$$
</div>

<div class="theorem">
If $\sigma$ is an epimorphism, $\rho(\tau\sigma) = \rho(\tau)$.
If $\tau$ is a monomorphism, $\rho(\tau\sigma) = \rho(\sigma)$.
</div>

<div class="corollary">
The rank of a linear transformation is not changed by
multiplication by an isomorphism (on either side).
</div>

<div class="theorem">
$\sigma$ is an epimorphism if and only if $\tau\sigma = 0$ implies $\tau=0$.
$\tau$ is a monomorphism if and only if $\tau\sigma = 0$ implies $\sigma=0$.
</div>

<div class="corollary">
$\sigma$ is an epimorphism if and only if $\tau_1\sigma = \tau_2\sigma$ implies $\tau_1=\tau_2$.
$\tau$ is a monomorphism if and only if $\tau\sigma_1 = \tau\sigma_2$ implies $\sigma_1=\sigma_2$.
</div>

<div class="theorem">
For any basis of $U$, $\{a_1,\ldots,a_n\}$
and
for any $n$ vectors $b_1, \ldots, b_n\in V$ (not necessarily linearly independent),
there exists a uniquely determined linear transformations $\sigma: U \to V$
such that $\sigma(a_i)=b_i$ for all $1\leq i\leq n$.
</div>

<div class="theorem">
For any $r$ linearly independent vectors in a finite dimensional vector space $U$, $\{u_1,\ldots,u_r\}$
and
for any $r$ vectors $v_1, \ldots, v_r\in V$ (not necessarily linearly independent),
any
of $U$, $\{a_1,\ldots,a_n\}$,
there exists a (not necessarily unique) linear transformation of $\sigma:U \to V$
such that $\sigma(u_i)=v_i$ for all $1\leq i\leq r$.
</div>

<div class="theorem">
A linear transformation $\pi$ of a vector space into itself with the property that $\pi^2 = \pi$ is called
<span class="define">projection</span>.
</div>

<div class="theorem">
If $\pi$ is a projection of $V$ into itself,
then
$$
V = \image(\pi) \oplus K(\pi)
$$
and $\pi$ acts like the identity on $\image(\pi)$.
</div>

<div class="proof">
For any $v\in V$,
let $v_1 = \pi(v)\in V$.
Let $v_2 = v-v_1$,
then $\pi(v_2) = \pi(v) - \pi(v_1) = v_1 - v_1 = 0$,
hence $v_2\in K(\pi)$.
Therefore $v_2 \in K(\pi)$,
hence $v \in \image(\pi) + K(\pi)$,
thus $V\subset \image(\pi) + K(\pi)$.
Hence, we conclude that $V=\image(\pi) + K(\pi)$.

Now let $x\in \image(\pi) \cap K(\pi)$.
Then there exists $y\in V$ such that $x=\pi(y)$,
thus $0=\pi(x) = \pi^2(y) = \pi(y) = x$.
Therefore $\image(\pi) \cap K(\pi) = \{0\}$.

Therefore $V$ is a direct sum of $\image(\pi)$ and $K(\pi)$.
</div>

## Matrices

<div class="definition" data-name="matrices">
A <span class="define">matrix</span> over a field $F$
is
a rectangular array of scalrs.
The array will be written in the form
$$
A=
\begin{bmatrix}
A_{1,1} & A_{1,2} & \cdots & A_{1,n}
\\
A_{2,1} & A_{2,2} & \cdots & A_{2,n}
\\
\vdots & \vdots & \ddots & \vdots
\\
A_{m,1} & A_{m,2} & \cdots & A_{m,n}
\end{bmatrix}
\in
F^{m\times n}
$$
A matrix with $m$ rows and $n$ columns is called an <span class="define">$m$ $\times$ $n$ matrix</span>
or <span class="define">$m$-by-$n$ matrix</span>.
$A_{i,j}$ are called
<span class="define">elements</span>
or
<span class="define">entries</span>.
</div>

<div class="definition" data-name="main diagonal">
The <span div="define">main diagonal</span> of the matrix $A\in F^{m\times n}$
is the list of elements $(A_{1,1}, A_{1,2}, \ldots, A_{t,t})$ where $t=\min\{m,n\}$.
</div>

<div class="definition" data-name="diagonal matrices">
A <span div="define">diagonal matrix</span> is a square matrix in which
the elements not in the main diagonal are zero.
</div>

<div class="definition" data-name="matrix multiplication">
A matrix-matrix multiplication is defined as a (non-commutative) binary operation
on
two matrices $A\in F^{r\times m}$ and $B\in F^{m\times n}$
defined in such a way that
the result of $AB$ is a $r$-by-$n$ matrix where
$$
(AB)_{i,j} = \sum_{k=1}^m A_{i,k} B_{k,j}
$$
for all $1\leq i\leq r$ and $1\leq j\leq n$.
</div>

{% assign linalg_post = site.posts | where: "permalink", "/math/linear-algebra" | first %}

The motivation for this specific way of defining matrix-matrix multiplication
is well explained in
[Matrix-matrix multiplication](/math/linear-algebra#matrix-matrix-multiplication)
of my another blog post about linear algebra, [{{ linalg_post.title }}]({{ linalg_post.url }}).

<div class="theorem" data-name="rank-nullity theorem">
For an $A\in F^{m\times n}$,
the rank of $A$ plus the nullity of $A$ is equal to $n$.
The rank of a product $BA$ is less than or equal to the rank of either factor.
</div>


<!--
## Nonsingular matrices

## Change of basis

## Hermite normal form

## Elementary operations &amp; elementary matrices

## Linear problems &amp; linear equations

## Other applications of the Hermite normal form

## Normal forms

## Quotient sets, quotient spaces

## $\text{Hom}(U,V)$

## $\mbox{Hom}(U,V)$
-->
