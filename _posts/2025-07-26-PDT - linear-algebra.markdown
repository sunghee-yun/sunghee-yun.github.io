---
title: (WIP) Linear Algebra
date: Sat Jul 26 18:29:58 PDT 2025
last_modified_at: Sun Jul 27 18:52:51 PDT 2025
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
\newcommand{\Prob}{\mathop{\bf Prob}}
\newcommand{\Expect}{\mathop{\bf E{}}}
\newcommand{\sign}{\mathop{\bf sign}}
$$

<!--tags: {% for tag in page.tags %} <a href="/tags/#{{ tag }}">{{ tag }}</a> {% endfor %}
<br>
cats: {% for category in page.categories %} <a href="/categories/#{{ category }}">{{ category }}</a> {% endfor %}-->

posted: {{ page.date| date: "%d-%b-%Y" }}
&amp;
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

# Vector Spaces

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

## History

Vector spaces stem from [affine geometry](https://en.wikipedia.org/wiki/Affine_geometry),
via the introduction of coordinates in the plane or three-dimensional space.
Around 1636, French mathematicians [René Descartes](https://en.wikipedia.org/wiki/Ren%C3%A9_Descartes)
and [Pierre de Fermat](https://en.wikipedia.org/wiki/Pierre_de_Fermat) founded [analytic geometry](https://en.wikipedia.org/wiki/Analytic_geometry)
by identifying solutions to an equation of two variables with points on a plane curve.
To achieve geometric solutions without using coordinates, [Bernard Bolzano](https://en.wikipedia.org/wiki/Bernard_Bolzano) introduced, in 1804,
certain operations on points, lines, and planes, which are predecessors of vectors.
[August Ferdinand Möbius](https://en.wikipedia.org/wiki/August_Ferdinand_M%C3%B6bius)
[in 1827](https://en.wikipedia.org/wiki/Vector_space#CITEREFM%C3%B6bius1827)
introduced the notion of [barycentric coordinates](https://en.wikipedia.org/wiki/Barycentric_coordinates_(mathematics)).
[Giusto Bellavitis](https://en.wikipedia.org/wiki/Giusto_Bellavitis)
[in 1833](https://en.wikipedia.org/wiki/Vector_space#CITEREFBellavitis1833)
introduced an [equivalence relation](https://en.wikipedia.org/wiki/Equivalence_relation) on directed line segments
that share the same length and direction which he called [equipollence](https://en.wikipedia.org/wiki/Equipollence_(geometry)).
A [Euclidean vector](https://en.wikipedia.org/wiki/Euclidean_vector) is then an [equivalence class](https://en.wikipedia.org/wiki/Equivalence_class) of that relation.

Vectors were reconsidered with the presentation of complex numbers
by [Jean-Robert Argand](https://en.wikipedia.org/wiki/Jean-Robert_Argand) and
[William Rowan Hamilton](https://en.wikipedia.org/wiki/William_Rowan_Hamilton)
and the inception of [quaternions](https://en.wikipedia.org/wiki/Quaternion) by the latter.
They are elements in $$\reals^2$$ and $$\reals^4$$;
treating them using [linear combinations](#linear-combination)
goes back to [Edmond Laguerre](https://en.wikipedia.org/wiki/Edmond_Laguerre) in 1867,
who also defined [systems of linear equations](https://en.wikipedia.org/wiki/System_of_linear_equations).

In 1857,
[Arthur Cayley](https://en.wikipedia.org/wiki/Arthur_Cayley) introduced
the [matrix notation](https://en.wikipedia.org/wiki/Matrix_notation)
which allows for harmonization and simplification of [linear maps](https://en.wikipedia.org/wiki/Linear_map).
Around the same time, [Hermann Günther Grassmann](https://en.wikipedia.org/wiki/Hermann_Grassmann)
studied the barycentric calculus initiated by Möbius.
He envisaged sets of abstract objects endowed with operations.
In his work, the concepts of [linear independence](#linear-independence) and [dimension](#basis-and-dimension),
as well as [scalar products](https://en.wikipedia.org/wiki/Scalar_product) are present.
[Grassmann](https://en.wikipedia.org/wiki/Hermann_Grassmann)'s 1844 work exceeds
the framework of vector spaces as well since his considering multiplication led him to
what are today called [algebras](https://en.wikipedia.org/wiki/Algebra_over_a_field).
Italian mathematician [Giuseppe Peano](https://en.wikipedia.org/wiki/Giuseppe_Peano)
was the first to give the modern definition of vector spaces and linear maps in 1888,
although he called them &ldquo;linear systems.&rdquo;

[Peano](https://en.wikipedia.org/wiki/Giuseppe_Peano)'s axiomatization allowed for vector spaces with infinite dimension,
but [Peano](https://en.wikipedia.org/wiki/Giuseppe_Peano) did not develop that theory further.
In 1897, [Salvatore Pincherle](https://en.wikipedia.org/wiki/Salvatore_Pincherle)
adopted [Peano](https://en.wikipedia.org/wiki/Giuseppe_Peano)'s axioms
and made initial inroads into the theory of infinite-dimensional vector spaces.

An important development of vector spaces is due to the construction of
[function spaces](https://en.wikipedia.org/wiki/Function_space)
by [Henri Léon Lebesgue](https://en.wikipedia.org/wiki/Henri_Lebesgue).
This was later formalized by [Stefan Banach](https://en.wikipedia.org/wiki/Stefan_Banach) and [David Hilbert](https://en.wikipedia.org/wiki/David_Hilbert),
around 1920.
At that time, [algebra](https://en.wikipedia.org/wiki/Algebra)
and the new field of [functional analysis](https://en.wikipedia.org/wiki/Functional_analysis) began to interact,
notably with key concepts such as spaces of p-integrable functions,
*i.e.*, [$$L^p$$ spaces](https://en.wikipedia.org/wiki/Lp_space),
and [Hilbert spaces](https://en.wikipedia.org/wiki/Hilbert_space).

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

Consider a basis $$(v_1,\ldots,v_n)$$ of a vector space $$V$$ of dimension $$n$$ over a field $$F$$.
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

# Linear Algebra

Linear algebra is the branch of [mathematics](/math/landscape) concerning [linear equations](https://en.wikipedia.org/wiki/Linear_equation) such as

$$
a_{1}x_{1}+\cdots +a_{n}x_{n}=b
$$

[linear maps](https://en.wikipedia.org/wiki/Linear_map) such as

$$
(x_{1},\ldots ,x_{n})\mapsto a_{1}x_{1}+\cdots +a_{n}x_{n}
$$

and their representations in [vector spaces](#vector-spaces) and through [matrices](#matrices).

Linear algebra is central to almost all areas of mathematics.
For instance, linear algebra is fundamental in modern presentations of [geometry](https://en.wikipedia.org/wiki/Geometry),
including for defining basic objects such as lines, planes and [rotations](https://en.wikipedia.org/wiki/Rotation_(mathematics)).
Also, [functional analysis](https://en.wikipedia.org/wiki/Functional_analysis),
a branch of [mathematical analysis](https://en.wikipedia.org/wiki/Mathematical_analysis),
may be viewed as the application of linear algebra to [function spaces](https://en.wikipedia.org/wiki/Space_of_functions).

Linear algebra is also used in most sciences and fields of [engineering](https://en.wikipedia.org/wiki/Engineering)
because it allows [modeling](https://en.wikipedia.org/wiki/Mathematical_model) many natural phenomena,
and computing efficiently with such models.
For [nonlinear systems](https://en.wikipedia.org/wiki/Nonlinear_system),
which cannot be modeled with linear algebra,
it is often used for dealing with [first-order approximations](https://en.wikipedia.org/wiki/First-order_approximation),
using the fact that the [differential](https://en.wikipedia.org/wiki/Differential_(mathematics))
of a [multivariate function](https://en.wikipedia.org/wiki/Multivariate_function)
at a point is
the linear map that best approximates the function near that point.

In the modern era of [artificial intelligence (AI)](https://en.wikipedia.org/wiki/Artificial_intelligence)
and [machine learning (ML)](https://en.wikipedia.org/wiki/Machine_learning),
linear algebra has become even more indispensable,
serving as the mathematical foundation for optimization algorithms and data processing techniques.
In [convex optimization](/math/cvxopt),
linear algebra provides the tools for understanding gradients, Hessian matrices, and the geometric properties of feasible regions,
enabling efficient solutions to problems like [linear programming](/math/cvxopt#linear-programming-lp---the-foundation)
and [quadratic programming](/math/cvxopt#quadratic-programming-qp---adding-curvature)
that arise throughout ML.

Neural networks, the backbone of deep learning, are essentially compositions of linear transformations (matrix multiplications)
followed by nonlinear activation functions,
where operations like forward propagation, backpropagation, and gradient descent
are all expressed through matrix and vector computations.
Beyond neural networks, [linear algebra](#linear-algebra) underlies virtually every ML algorithm:
principal component analysis (PCA) uses eigenvalue decomposition for dimensionality reduction,
support vector machines (SVM) rely on inner products and kernel methods,
and least squares (LS) regression directly solves linear systems.
The efficiency of modern AI systems depends heavily on optimized linear algebra libraries
that can perform massive matrix operations on specialized hardware like GPUs,
making linear algebra not just theoretically important
but practically essential for the computational demands of contemporary AI.

## History

The procedure (using counting rods) for solving simultaneous linear equations now called
[Gaussian elimination](https://en.wikipedia.org/wiki/Gaussian_elimination)
appears in the ancient Chinese mathematical text [Chapter Eight: Rectangular Arrays](https://en.wikipedia.org/wiki/Rod_calculus#System_of_linear_equations)
of [The Nine Chapters on the Mathematical Art](https://en.wikipedia.org/wiki/The_Nine_Chapters_on_the_Mathematical_Art).
Its use is illustrated in eighteen problems, with two to five equations.

[Systems of linear equations](https://en.wikipedia.org/wiki/Systems_of_linear_equations) arose in Europe
with the introduction in 1637
by [René Descartes](https://en.wikipedia.org/wiki/Ren%C3%A9_Descartes) of [coordinates](https://en.wikipedia.org/wiki/Coordinates)
in [geometry](https://en.wikipedia.org/wiki/Geometry).
In fact, in this new geometry, now called [Cartesian geometry](https://en.wikipedia.org/wiki/Cartesian_geometry),
lines and planes are represented by linear equations, and computing their intersections amounts to solving systems of linear equations.

The first systematic methods for solving linear systems used [determinants](#determinant)
and were first considered by [Gottfried Wilhelm Leibniz](https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz) in 1693.
In 1750, [Gabriel Cramer](https://en.wikipedia.org/wiki/Gabriel_Cramer) used them
for giving explicit solutions of linear systems, now called [Cramer's rule](https://en.wikipedia.org/wiki/Cramer%27s_rule).
Later, [Johann Carl Friedrich Gauss](https://en.wikipedia.org/wiki/Gauss)
further described the method of elimination,
which was initially listed as an advancement in [geodesy](https://en.wikipedia.org/wiki/Geodesy).

In 1844,
[Hermann Günther Grassmann](https://en.wikipedia.org/wiki/Hermann_Grassmann) published
his &ldquo;Theory of Extension&rdquo; which included foundational new topics of what is today called [linear algebra](#linear-algebra).
In 1848,
[James Joseph Sylvester](https://en.wikipedia.org/wiki/James_Joseph_Sylvester) introduced the term [matrix](#matrices),
which is Latin for *womb*.

<!--
Linear algebra grew with ideas noted in the complex plane. For instance, two numbers w and z in
C
{\displaystyle \mathbb {C} } have a difference w – z, and the line segments wz and 0(w − z) are of the same length and direction. The segments are equipollent. The four-dimensional system
H
{\displaystyle \mathbb {H} } of quaternions was discovered by W.R. Hamilton in 1843. The term vector was introduced as v = xi + yj + zk representing a point in space. The quaternion difference p – q also produces a segment equipollent to pq. Other hypercomplex number systems also used the idea of a linear space with a basis.
-->

[Arthur Cayley](https://en.wikipedia.org/wiki/Arthur_Cayley)
introduced [matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication)
and the [inverse matrix](https://en.wikipedia.org/wiki/Inverse_matrix) in 1856,
making possible the [general linear group](https://en.wikipedia.org/wiki/General_linear_group).
The mechanism of [group representation](https://en.wikipedia.org/wiki/Group_representation) became available for describing complex and hypercomplex numbers. Crucially, Cayley used a single letter to denote a matrix, thus treating a matrix as an aggregate object. He also realized the connection between matrices and determinants and wrote "There would be many things to say about this theory of matrices which should, it seems to me, precede the theory of determinants".

[Benjamin Peirce](https://en.wikipedia.org/wiki/Benjamin_Peirce) published his Linear Associative Algebra in 1872,
and his son [Charles Sanders Peirce](https://en.wikipedia.org/wiki/Charles_Sanders_Peirce) extended the work later.

<!--
The [telegraph](https://en.wikipedia.org/wiki/Telegraphy) required an explanatory system, and the 1873 publication by James Clerk Maxwell of A Treatise on Electricity and Magnetism instituted a field theory of forces and required differential geometry for expression. Linear algebra is flat differential geometry and serves in tangent spaces to manifolds. Electromagnetic symmetries of spacetime are expressed by the Lorentz transformations, and much of the history of linear algebra is the history of Lorentz transformations.
-->

The first modern and more precise definition of a vector space was introduced by [Giuseppe Peano](https://en.wikipedia.org/wiki/Giuseppe_Peano) in 1888;
by 1900, a theory of linear transformations of finite-dimensional vector spaces had emerged.
Linear algebra took its modern form
in the first half of the twentieth century
when many ideas and methods of previous centuries were generalized as [abstract algebra](/math/abstract-algebra).
The development of computers led to increased research in efficient [algorithms](https://en.wikipedia.org/wiki/Algorithm)
for [Gaussian elimination](https://en.wikipedia.org/wiki/Gaussian_elimination)
and [matrix decompositions](https://en.wikipedia.org/wiki/Matrix_decomposition),
and [linear algebra](#linear-algebra) became an essential tool for modeling and simulations.

## Matrices

Matrices allow explicit manipulation of
finite-dimensional [vector spaces](#vector-spaces)
and [linear maps](https://en.wikipedia.org/wiki/Linear_map).
Their theory is thus an essential part of linear algebra.

Let $$V$$ be a finite-dimensional [vector space](#vector-spaces) over a field $$F$$,
and $$(v_1, \ldots, v_m)$$ be a basis of $$V$$ (hence the dimension of $$V$$ is $$m$$).
By definition, the map $$F^m \to V$$
defined by

$$
(a_1, \ldots, a_m) \mapsto a_1 v_1 + \cdots + a_m v_m
$$

is a [bijection](https://en.wikipedia.org/wiki/Bijection) from $$F^m$$,
the set of the [sequences](https://en.wikipedia.org/wiki/Sequence_(mathematics)) of $$m$$ elements of $$F$$,
onto $$V$$.
This is an [isomorphism](https://en.wikipedia.org/wiki/Isomorphism)
of vector spaces.

This isomorphism allows representing a vector by its [inverse image](https://en.wikipedia.org/wiki/Inverse_image)
under this isomorphism,
that is by the [coordinate vector](#coordinates) $$(a_1, \ldots, a_m)$$
or by the [column matrix](https://en.wikipedia.org/wiki/Column_matrix)

$$
\begin{bmatrix}
a_1
\\
\vdots
\\
a_m
\end{bmatrix}
\in
F^m.
$$

Now let $$W$$ is a finite dimensional vector space with a basis $$(w_1, \ldots, w_n)$$
and let $$f:W \to V$$ is a linear map.

By the definition of the basis,
each of $$f(w_1), \ldots, f(w_n)$$ has its coordinate vector on the basis $$(v_1,\ldots,v_m)$$.
Let $$A_{i,j}$$ be the $$i$$-th coordinate of $$f(w_j)$$
for $$1\leq i\leq m$$ and $$1\leq j\leq n$$,
*i.e.*,

$$
\begin{array}{rcl}
f(w_1)
	&=& A_{1,1} v_1 + A_{2,1} v_2 + \cdots + A_{m,1} v_m
\\
f(w_2)
	&=& A_{1,2} v_1 + A_{2,2} v_2 + \cdots + A_{m,2} v_m
\\
	&\vdots&
\\
f(w_n)
	&=& A_{1,n} v_1 + A_{2,n} v_2 + \cdots + A_{m,n} v_m
\end{array}
$$

Suppose $$w\in W$$. Let us examine how we can express the coordinates of $$f(w)$$ (on the basis $$(v_1,\ldots,v_m)$$
in terms of the coordinates of $$w$$ on the basis $$(w_1,\ldots,w_n)$$.
Let $$(x_1,\ldots,x_n)$$ be the coordinates of $$w$$ (on the basis $$(w_1,\ldots,w_n)$$)
and $$(y_1,\ldots,y_m)$$ be the coordinates of $$f(w)$$ (on the basis $$(v_1,\ldots,v_m)$$).
Then

$$
\begin{array}{rcl}
f(w)
	&=
		&f(x_1 w_1 + \cdots + x_n w_n)
\\
	&=
		&x_1f(w_1) + \cdots + x_n f(w_n)
\\
	&=
		&(A_{1,1} x_1 + A_{1,2} x_2 + \cdots + A_{1,n} x_n) v_1
\\
	&
		&+ (A_{2,1} x_1 + A_{2,2} x_2 + \cdots + A_{2,n} x_n) v_2
\\
	&
		&\vdots
\\
	&
		&+ (A_{m,1} x_1 + A_{m,2} x_2 + \cdots + A_{m,n} x_n) v_m
\end{array}
$$

hence

$$
\begin{eqnarray}
\nonumber
y_1
	&=& A_{1,1} x_1 + A_{1,2} x_2 + \cdots + A_{1,n} x_n
\\ \nonumber
y_2
	&=& A_{2,1} x_1 + A_{2,2} x_2 + \cdots + A_{2,n} x_n
\\
\label{eq:eqs-for-mat-vec-mul}
	&\vdots&
\\ \nonumber
y_m
	&=& A_{m,1} x_1 + A_{m,2} x_2 + \cdots + A_{m,n} x_n
\end{eqnarray}
$$

Here we define a matrix $$A$$
to be the following $$2$$-dimensional array:

$$
A = \begin{bmatrix}
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

There is a bijection between the set of all such matrices, that is, $$F^{m\times n}$$
and the set of all linear mappings from $$V$$ to $$W$$.

We want to make this bijection isomorphism somehow,
which will naturally define matrix-vector multiplication and matrix-matrix multiplication as shown below.

### Matrix-vector multiplication

We define *the* matrix-vector multiplication in such a way that

$$
y = A x
$$

means the $$m$$ equations in \eqref{eq:eqs-for-mat-vec-mul}
where $$x$$ and $$y$$ are $$n$$-dimensional and $$m$$-dimensional vectors respectively
defined by

$$
x = \begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix} \in F^n,
\quad
y = \begin{bmatrix} y_1 \\ \vdots \\ y_m \end{bmatrix} \in F^m.
$$

Note that the equations in \eqref{eq:eqs-for-mat-vec-mul} readily define the matrix-vector multiplication
as we desire.

### Matrix-matrix multiplication

We define
*the* matrix-matrix multiplication in such a way
that the product of two matrices is the matrix of the composition of the corresponding linear maps.
(Whereas the equations defining the matrix-vector multiplication had already been derived above,
the equations for the matrix-matrix multiplication has to be derived here.)

Suppose that $$W$$, $$V$$, and $$U$$ are
vector spaces over a field $$F$$
whose dimensions are $$n$$, $$m$$, and $$p$$ respectively.
Suppose also that $$f:W\to V$$ and $$g:V \to U$$
are linear maps
and $$A\in F^{m \times n}$$ and $$B\in F^{p \times m}$$ are matrices
corresponding to $$f$$ and $$g$$ respectively
assuming three bases for each vector space,
*e.g.*,
$$(w_1,\ldots,w_n)$$ for $$W$$,
$$(v_1,\ldots,v_m)$$ for $$V$$,
and
$$(u_1,\ldots,u_p)$$ for $$U$$.

Now we want to find a matrix $$C\in F^{p \times n}$$
which corresponds to $$g\circ f$$,
*i.e.*,
the composition of the two linear mappings $$f$$ and $$g$$,
and define $$C$$ as the multiplication of $$A$$ and $$B$$ in a specific order,
*i.e.*,

\begin{equation}
\label{eq:mat-mat-mul}
C = BA \in F^{p\times n}.
\end{equation}

Let $$w\in W$$ and $$(x_1,\ldots,x_n)$$ be its coordinates on the basis $$(w_1,\ldots,w_n)$$,
$$v=f(w) \in V$$ and $$(y_1,\ldots,y_m)$$ be its coordinates on the basis $$(v_1,\ldots,v_m)$$,
and
$$u=f(v) \in U$$ and $$(z_1,\ldots,z_p)$$ be its coordinates on the basis $$(u_1,\ldots,u_p)$$.
If we define three column vectors as

$$
x = \begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix} \in F^n,
\quad
y = \begin{bmatrix} y_1 \\ \vdots \\ y_m \end{bmatrix} \in F^m,
\quad
z = \begin{bmatrix} z_1 \\ \vdots \\ z_p \end{bmatrix} \in F^p,
$$

we know

\begin{equation}
\label{eq:two-mat-vec-muls}
y = Ax,
\quad
z = By
\end{equation}

where these matrix-vector multiplications are defined by the equations in \eqref{eq:eqs-for-mat-vec-mul}
or equivalently in [Matrix-vector multiplication](#matrix-vector-multiplication).
Therefore for each $$i\in\{1,\ldots,p\}$$,

$$
\begin{array}{rcl}
z_i
	&=
		&B_{i,1} y_1 + B_{i,2} y_2 + \cdots + B_{i,m} y_m
\\
	&=
		&B_{i,1} (A_{1,1} x_1 + \cdots + A_{1,n} x_n)
\\
	&
		&+ B_{i,2} (A_{2,1} x_1 + \cdots + A_{2,n} x_n)
\\
	&
		&\vdots
\\
	&
		&+ B_{i,m} (A_{m,1} x_1 + \cdots + A_{m,n} x_n)
\\
	&=
		&(B_{i,1}A_{1,1} + B_{i,2}A_{2,1} + \cdots + B_{i,m}A_{m,1})x_1
\\
	&
		&+ (B_{i,1}A_{1,2} + B_{i,2}A_{2,2} + \cdots + B_{i,m}A_{m,2})x_2
\\
	&
		&\vdots
\\
	&
		&+ (B_{i,1}A_{1,n} + B_{i,2}A_{2,n} + \cdots + B_{i,m}A_{m,n})x_n.
\end{array}
$$

Therefore for each $$i\in\{1,\ldots,p\}$$ and each $$j\in\{1,\ldots,n\}$$,

\begin{equation}
\label{eq:eq-for-mat-mat-mul}
	C_{i,j} = B_{i,1}A_{1,j} + B_{i,2}A_{2,j} + \cdots + B_{i,m}A_{m,j} = \sum_{k=1}^m B_{i,k}A_{k,j}
\end{equation}

hence, we define the matrix-matrix multiplication in a way that \eqref{eq:mat-mat-mul}
means \eqref{eq:eq-for-mat-mat-mul}
for each $$i\in\{1,\ldots,p\}$$ and each $$j\in\{1,\ldots,n\}$$.

Note that this works seamlessly with the way we define the matrix-vector multiplication,
*e.g.*,
if we substitute $$Ax$$ for $$y$$ in \eqref{eq:two-mat-vec-muls}, we have

$$
z = B(Ax) = (BA)x = Cx
$$

that is,
the way we define the matrix-matrix multiplication and matrix-vector multiplication
makes them *associative!*

Indeed, if we regard a column vector in $$F^n$$ as a matrix in $$F^{n\times 1}$$,
the matrix-vector multiplication coincides with the matrix-matrix multiplication!

### Matrix operations

There are other unary and binary operations on matrices
other than usual addition, subtraction, and [multiplication](#matrix-matrix-multiplication).

<span id="trasnpose">**Transpose**</span>

The <span id="transpose">transpose</span> of $$A\in F^{m\times n}$$ is denoted by $$A^T$$
and defined by
a $$n$$-by-$$m$$ matrix $$B\in F^{n\times m}$$
satisfying

$$
B_{i,j} = A_{j,i}
\;
\mbox{for all }
1\leq i\leq n
\;
\&
\;
1\leq j\leq m.
$$

<span id="conjugate-transpose">**Conjugate transpose or Hermitian transpose**</span>

The <span class="emph">conjugate transpose</span> or <span class="emph">Hermitian transpose</span>
of $$A \in \complexes^{m\times n}$$
is denoted by $$A^H$$ or $$A^\ast$$ (or sometimes $$A'$$ or (often in physics) $$A^\dagger$$),
and
is defined by a $$n$$-by-$$m$$ complex matrix $$B\in \complexes^{n\times m}$$
satisfying

$$
B_{i,j} = \overline{A_{j,i}}
\;
\mbox{for all }
1\leq i\leq n
\;
\&
\;
1\leq j\leq m.
$$

where $$\overline{a}$$ denotes the [complex conjugate](https://en.wikipedia.org/wiki/Complex_conjugate) of $$a\in\complexes$$,
*i.e.*,
if $$a=b+i c$$ with $$b,c\in\reals$$,
$$\overline{a} = b - i c$$.

## Types of matrices

### Square matrices

A matrix is called a [<span class="emph">square matrix</span>](https://en.wikipedia.org/wiki/Square_matrix)
if the number of rows equals to that of columns.

### Diagonal matrices

A square matrix where all the off-diagonal entries are zero is called
a [<span class="emph">diagonal matrix</span>](https://en.wikipedia.org/wiki/Diagonal_matrix).
In other words,
$$A\in F^{n\times n}$$
is a diagonal matrix
if

$$
A_{i,j} = 0
\;
\mbox{for all }
i\neq j.
$$

### Identity matrices

A diagonal matrix where all the diagonal entries are $$1$$
is called the [<span class="emph">identity matrix</span>](https://en.wikipedia.org/wiki/Identity_matrix),
which is denoted by $$I$$;
$$I_n \in F^{n\times n}$$ denotes the $$n$$-by-$$n$$ identity matrix.

Note that

$$
(\forall A\in F^{m\times n})
(AI_n = A \;\&\; I_mA = A).
$$


### Symmetric matrices

A matrix is called a [<span class="emph">symmetric matrix</span>](https://en.wikipedia.org/wiki/Symmetric_matrix)
if it equals to its transpose.
Therefore a symmetric matrix is a square matrix (by definition).
In other words, $$A\in F^{n\times n}$$ is called a [<span class="emph">symmetric matrix</span>](https://en.wikipedia.org/wiki/Symmetric_matrix)
if it satisfies

$$
A^T = A.
$$

### Skew-symmetric matrices

A matrix is called [<span class="emph">skew-symmetric matrix</span>](https://en.wikipedia.org/wiki/Skew-symmetric_matrix)
if its negation equals to its [transpose](#transpose).
A skew-symmetric matrix is sometimes called an <span class="emph">antisymmetric matrix</span>
or <span class="emph">antimetric matrix</span>.
In other words,
$$A\in F^{n\times n}$$ is skew-symmetric
if

$$
A^T = -A.
$ka$

### Real matrices

When $$F=\reals$$, we call the matrices <span class="emph">real matrices</span>.

### Complex matrices

When $$F=\complexes$$, we call the matrices <span class="emph">complex matrices</span>.

### Hermitian matrices

A complex matrix is called [<span class="emph">Hermitian matrix</span>](https://en.wikipedia.org/wiki/Hermitian_matrix)
if it equals to its [conjugate transpose](#conjugate-transpose).
A Hermitian matrix is sometimes called <span class="emph">self-adjoint matrix</span>.
In other words,
$$A\in\complexes^{n\times n}$$ is Hermitian
if

$$
A^H = A.
$$

Note that a real Hermitian matrix is a [symmetric matrix](#symmetric-matrices).

### Skew-Hermitian matrices

A complex matrix is called [<span class="emph">skew-Hermitian matrix</span>](https://en.wikipedia.org/wiki/Skew-Hermitian_matrix)
if its negation equals to its [conjugate transpose](#conjugate-transpose).
A skew-Hermitian matrix is sometimes called <span class="emph">anti-Hermitian matrix</span>.
In other words,
$$A\in\complexes^{n\times n}$$ is skew-Hermitian
if

$$
A^H = -A.
$$

Note that a real skew-Hermitian matrix is a [skew-symmetric matrix](#skew-symmetric-matrices).

## Linear systems

A finite set of linear equations in a finite set of variables
is called a <span class="emph">system of linear equations</span> or a <span class="emph">linear system</span>.

[Systems of linear equations](https://en.wikipedia.org/wiki/System_of_linear_equations)
form a fundamental part of [linear algebra](#linear-algebra).
Historically, linear algebra and matrix theory have been developed for solving such systems. In the modern presentation of linear algebra through vector spaces and matrices, many problems may be interpreted in terms of linear systems.

For example, consider the following linear system.

$$
\begin{array}{rcr}
2u+v-w&=&8
\\
-3u-v+2w&=&-11
\end{array}
$$

If we let $$A\in\reals^{2\times 3}$$ and $$b\in\reals^2$$
such that

$$
A = \begin{bmatrix}
	2 & 1 & -1
	\\
	-3&-1&2
\end{bmatrix},
\quad
b = \begin{bmatrix}8\\-11\end{bmatrix}
$$

and define $$x\in\reals^3$$ as

$$
x = \begin{bmatrix}
	u\\v\\w
\end{bmatrix}
$$

the linear system can be compactly represented by

$$
b = Ax.
$$

## Endomorphisms &amp; square matrices

A linear [endomorphism](https://en.wikipedia.org/wiki/Endomorphism)
is a linear map that maps a vector space to itself.
If the vector space has a basis of $$n$$ elements,
that is,
if the dimension of the vector space is $$n$$,
such an endomorphism is represented by a square matrix of size $$n$$.

Concerning general linear maps, linear endomorphisms, and square matrices
have some specific properties that make their study an important part of linear algebra,
which is used in many parts of mathematics,
including
[geometric transformations](https://en.wikipedia.org/wiki/Geometric_transformation),
[coordinate changes](https://en.wikipedia.org/wiki/Coordinate_change),
[quadratic forms](https://en.wikipedia.org/wiki/Quadratic_form),
and many other parts of mathematics.

### Determinant

The <span class="emph">[determinant](https://en.wikipedia.org/wiki/Determinant)</span>
of a square matrix $$A\in R^{n\times n}$$
(where $$R$$ is a [ring](/math/abstract-algebra#rings---where-addition-meets-multiplication)<sup><a href="#footnote2" id="ref2">2</a></sup>)
is denoted by $$\det(A)$$
and defined by

\begin{equation}
\label{eq:det-formula}
\det(A)
	=
		\sum_{\sigma \in S_n} \sign(\sigma) A_{1,\sigma(1)} A_{2,\sigma(2)} \cdots A_{n,\sigma(n)}
\end{equation}

where $$S_n$$ is the group of all permutations,
*i.e.*, the [symmetric group](https://en.wikipedia.org/wiki/Symmetric_group),
of $$n$$ elements
and $$\sigma(\sigma)$$ is the [parity](https://en.wikipedia.org/wiki/Parity_of_a_permutation) of the permutation $$\sigma$$.

The matrix $$A$$ is invertible if and only if the determinant is invertible
(*e.g.*, nonzero if the scalars belong to a [field](/math/abstract-algebra#fields---the-realm-of-perfect-division)).

The determinant can be evaluated recursively,
*i.e.*,
one can derive the formula for the determinant of a square matrix in $$R^{n\times n}$$
using the determinants of square matrices in $$R^{(n-1)\times(n-1)}$$ as follow.

\begin{equation}
\label{eq:det-formula-recursive}
\det(A)
	=
		\sum_{k=1}^n (-1)^{k+1}A_{1,k} M_{1,k}
\end{equation}

where
$$M_{i,j}$$ is the [$$(i,j)$$-minor](https://en.wikipedia.org/wiki/Minor_(linear_algebra)) of $$A$$
that is
defined by the [determinant](#determinant) of the $$(n-1)$$-by-$$(n-1)$$ matrix
resulting from removing the $i$-th row and $j$-th column of $$A$$.

Note that we have the following equivalences.<sup><a href="#footnote3" id="ref3">3</a></sup>

$$
\begin{array}{rcl}
\det(A)
	&=&
		\sum_{k=1}^n (-1)^{1+k}A_{1,k} M_{1,k}
\\
	&=&
		\sum_{k=1}^n (-1)^{k+1}A_{k,1} M_{k,1}
\\
	&=&
		\sum_{k=1}^n (-1)^{i+k}A_{i,k} M_{i,k}
		\quad \mbox{for any } 1\leq i\leq n
\\
	&=&
		\sum_{k=1}^n (-1)^{k+j}A_{k,j} M_{k,j}
		\quad \mbox{for any } 1\leq j\leq n
\end{array}
$$

[Cramer's rule](https://en.wikipedia.org/wiki/Cramer%27s_rule) is a closed-form expression,
in terms of determinants,
of the solution of a [linear system](https://en.wikipedia.org/wiki/System_of_linear_equations).
[Cramer's rule](https://en.wikipedia.org/wiki/Cramer%27s_rule) is useful for reasoning about the solution,
but, except for $$n = 2$$ or $$3$$,
it is rarely used for computing a solution.

<!--
The determinant of an endomorphism is the determinant of the matrix representing the endomorphism in terms of some ordered basis. This definition makes sense since this determinant is independent of the choice of the basis.
-->

### Eigenvalues, eigenvectors, and characteristic polynomial

If $$f$$ is a linear endomorphism of a vector space $$V$$ over a field $$F$$,
an eigenvector of $$f$$ is a nonzero vector $$x\in \overline{V}$$
such that $$f(x) = \lambda x$$ for some $$\lambda \in \overline{F}$$
where $$\overline{F}$$ is the algebraic closure of the field $$F$$
and $$\overline{V}$$ is the extended vector space by $$\overline{F}$$.
This scalar $$\lambda$$ is called an eigenvalue of $$f$$
(associated with the eigenvector $$x$$).

If the dimension of $$V$$ is finite,
and a basis has been chosen,
$$f$$ and $$x$$ may be represented,
respectively,
by a square matrix $$A\in F^{n\times n}$$ and a (column) vector $$v\in \overline{F}^n$$.
Then the equation defining eigenvectors and eigenvalues becomes

$$
Av = \lambda v.
$$

Note the following equivalence!

$$
Av = \lambda v \iff (A-\lambda I_n) v = 0
$$

where $$I_n\in F^{n\times n}$$ is the [identity matrix](#identity-matrix).
If $$A-\lambda I_n$$ were nonsingular, *i.e.*, invertible,
$$v$$ should be a zero vector,
which is a contradiction.
Thus $$(A- \lambda I_n)\in F^{n\times n}$$ should be singular,
*i.e.*,

$$
\det (A-\lambda I_n) = 0.
$$

Note that the left-hand-side (LHS) of the equation is
a [monic polynomial](https://en.wikipedia.org/wiki/Monic_polynomial) of degree $$n$$,
is called the <span class="emph">[characteristic polynomial](https://en.wikipedia.org/wiki/Characteristic_polynomial)</span>
of the matrix $$A$$ or of the endomorphism, and
hence
<!--
the [fundamental theorem of algebra](https://en.wikipedia.org/wiki/Fundamental_theorem_of_algebra)
implies that
-->
there are (at most) $$n$$ eigenvalues.

### Diagonalizability

If a basis exists that consists only of eigenvectors,
the matrix of f on this basis has a very simple structure: it is a diagonal matrix such that the entries on the main diagonal are eigenvalues, and the other entries are zero. In this case, the endomorphism and the matrix are said to be diagonalizable. More generally, an endomorphism and a matrix are also said diagonalizable, if they become diagonalizable after extending the field of scalars. In this extended sense, if the characteristic polynomial is square-free, then the matrix is diagonalizable.

### Symmetric real matrices

We can (easily) show that all the eigenvalues of symmetric real matrices are real.

$$
v^\ast Av = v^\ast \lambda v = \lambda \|v\|_2^2
$$

$$
v^\ast A^\ast v = v^\ast \lambda^\ast v = \lambda^\ast \|v\|_2^2
$$



## Duality

### Dual map

### Inner-product spaces

## Relationship with geometry

## Usage and applications

### Functional analysis

### Scientific computation

### Geometry of ambient space

### Study of complex systems

### Fluid mechanics, fluid dynamics, and thermal energy systems

## Extensions &amp; generalizations

### Module theory

### Multilinear algebra and tensors

### Topological vector spaces

<hr>
<ol>
<li id="footnote1">
	For example, the real numbers form an infinite-dimensional vector space over the rational numbers,
	for which no specific basis is known.
	&nbsp;<a href="#ref1">↩</a></li>
<li id="footnote2">
	Here (only) for the discussion of determinant,
	we assume a <a href="/math/abstract-algebra#rings---where-addition-meets-multiplication">ring</a>
	(not a <a href="/math/abstract-algebra#fields---the-realm-of-perfect-division">field</a>)
	for the discussion of determinant.
	For the rest,
	we will get back to the assumption of a field!
	&nbsp;<a href="#ref2">↩</a></li>
<li id="footnote3">
	The original formulation \eqref{eq:det-formula}
	as well as the recursive formula \eqref{eq:det-formula-recursive}
	takes $O(n!)$ operations,
	thus in practice this formula is *never* used for the actual calculation of determinants
	(possibly except for the exercises for students).
	&nbsp;<a href="#ref3">↩</a></li>
</ol>
