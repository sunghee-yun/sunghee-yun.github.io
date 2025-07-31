---
title: "From Ancient Equations to Artificial Intelligence &ndash; Linear Algebra"
date: Sat Jul 26 18:29:58 PDT 2025
last_modified_at: Thu Jul 31 01:07:12 PDT 2025
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

**A Tribute 獻呈 to My Samsung Colleagues**
<br>
<br>
This blog post has its origins in the lectures I delivered from 2008 to 2013 while working with the Computer-Aided Engineering (CAE) Team at Samsung Semiconductor.
During those years, I had the privilege of presenting on diverse mathematical topics—statistics, linear algebra, numerical linear algebra, and even Convex Optimization!
<br>
<br>
One day, a curious mind (and cherished colleague of mine ⭐^^⭐) posed two fundamental questions that would spark this entire intellectual journey - "Why linear algebra? Why matrices?" Those simple yet profound questions became the catalyst for everything you'll read here.
<br>
<br>
This work is dedicated to those brilliant team members who illuminated my days at Samsung.
Their curiosity and engagement transformed routine lectures into explorations of mathematical beauty, and their questions continue to inspire my thinking **even more than 10** years later.
{: .notice--success}

# NotebookLM Podcasts

- [27:26](https://notebooklm.google.com/notebook/9bc4fc2c-7de5-4f56-8d74-2dd09fb48fc6/audio)
- [33:11](https://notebooklm.google.com/notebook/90b5a5f3-f848-482a-9a9d-95d18c6d9bc4/audio)

# Vector Spaces

In mathematics and physics,
a <span class="emph">vector space</span>
is a set whose elements (called vectors)
can be added together and multiplied or *scaled* by numbers called <span class="emph">scalars</span>.
The operations of <span class="emph">vector addition</span> and <span class="emph">scalar multiplication</span>
must satisfy certain requirements,
called <span class="emph">vector axioms</span>.

Before diving into the formal definition, let's build intuition with a familiar example. Consider the set of all arrows in a plane, where each arrow represents a force or velocity. You can add two forces by placing them head-to-tail (vector addition), and you can double a force by making the arrow twice as long (scalar multiplication). This intuitive picture captures the essence of what vector spaces formalize mathematically.

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
| additive [commutativity](https://en.wikipedia.org/wiki/Commutative_property) | $$(\forall x,y\in V)(x+y=y+x)$$ |
| additive [associativity](https://en.wikipedia.org/wiki/Associative_property) | $$(\forall x,y,z\in V)(x+(y+z)=(x+y)+z)$$ |
| existence of [additive identify](https://en.wikipedia.org/wiki/Additive_identity) | $$(\exists 0\in V)(\forall x\in V)(x+0=x)$$ |
| existence of [additive inverse](https://en.wikipedia.org/wiki/Additive_inverse) | $$(\forall x \in V)(\exists y \in V)(x+y=0)$$ - $$y$$, called <span class="emph">additive inverse</span> of $$x$$, denoted by $$-x$$ |
| multiplicative [associativity](https://en.wikipedia.org/wiki/Associative_property) | $$(\forall x\in V\;\&\;\forall \alpha, \beta \in F)(\alpha(\beta x)=(\alpha\beta)x)$$ |
| multiplicative [identity](https://en.wikipedia.org/wiki/Identity_element) | $$(\forall x\in V)(1x = x)$$ where $$1$$ is the multiplicative identity of $$F$$ |
| [distributivity](https://en.wikipedia.org/wiki/Distributivity) of multiplication over vector addition | $$(\forall x,y \in V \;\&\; \forall \alpha\in F)(\alpha(x+y) = \alpha x + \alpha y)$$ |
| [distributivity](https://en.wikipedia.org/wiki/Distributivity) of multiplication over field addition | $$(\forall x \in V \;\&\; \alpha, \beta \in F)((\alpha+ \beta)x = \alpha x + \beta x)$$ |

**Example**
The most familiar vector space is $$\reals^3$$,
the set of all ordered triples $$(x,y,z)$$ of real numbers.
Vector addition is componentwise:
$$(x_1,y_1,z_1) + (x_2,y_2,z_2) = (x_1+x_2,y_1+y_2,z_1+z_2)$$,
and scalar multiplication is $$c(x,y,z) = (cx,cy,cz)$$.
(You can verify that all eight axioms hold for this familiar setting.)

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

### Linear span

For a subset $$W$$ of a vector space $$V$$,
the <span class="emph">linear span</span>
or simply <span class="emph">span</span> of $$W$$
is defined by
the smallest subspace of $$V$$ that contains $$W$$.

It can be shown that the span of $$W$$ is the set of all linear combinations of elements of $$W$$.

If $$S$$ is the span of $$W$$,
$$W$$ is said to <span class="emph">span</span> or <span class="emph">generate</span> $$S$$,
and $$W$$ is called a <span class="emph">spanning set</span> or a <span class="emph">generating set</span> of $$S$$,
and denoted by

$$
S = \lspan{W}.
$$

### Basis and dimension

A subset of a vector space is a <span class="emph">basis</span>
if its elements are linearly independent and span the vector space.
Every vector space has at least one basis
and many in general.

[This theorem](/math/rig/linear-algebra#theorem:bases-have-same-cardinality)
implies all bases of a vector space have the same cardinality.
This cardinality is called the <span class="emph">dimension</span> of the vector space.
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

---

# Linear Algebra

Having established the foundation of vector spaces, we now turn to
<span class="emph">linear algebra</span> itself
&ndash;
the study of linear relationships and transformations between these spaces. Where vector spaces give us the "stage," linear algebra provides the "action" through linear maps, systems of equations, and their matrix representations.

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

## The Modern AI Connection

In the modern era of [artificial intelligence (AI)](https://en.wikipedia.org/wiki/Artificial_intelligence)
and [machine learning (ML)](https://en.wikipedia.org/wiki/Machine_learning),
linear algebra has become even more indispensable,
serving as the mathematical foundation for optimization algorithms and data processing techniques.

**Think of it this way**
&ndash; Every time you interact with AI - whether it's asking ChatGPT a question, getting photo recommendations, or using voice recognition - massive matrix computations are happening behind the scenes. A single forward pass through a modern neural network like GPT-4 involves billions of matrix multiplications.

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

The bridge between abstract vector spaces and concrete computation is provided
by <span class="emph">matrices</span>
&ndash; rectangular arrays of numbers that allow us to represent and manipulate linear transformations explicitly.

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

We want to make this bijection an isomorphism,
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

Note that for any two matrices $$A$$ and $$B$$ for which the multiplication $$AB$$ can be defined,
*i.e.*, when the number of columns of $$A$$ equals to the number of rows of $$B$$,

$$
(AB)^T = B^T A^T.
$$

Recursively applying this yields

$$
(A_1A_2 \cdots A_n)^T
=
A_n^T
\cdots
A_2^T
A_1^T.
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

As for transpose operator,
for any two matrices $$A$$ and $$B$$ for which the multiplication $$AB$$ can be defined

$$
(AB)^H = B^H A^H.
$$

Recursively applying this yields

$$
(A_1A_2 \cdots A_n)^H
=
A_n^H
\cdots
A_2^H
A_1^H.
$$

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
$$

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

Now that we understand matrices, we can tackle one of the most fundamental problems in linear algebra: solving systems of linear equations. This is where theory meets computation most directly.

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

### Geometric Interpretation

Each equation represents a hyperplane (in this case, a plane in 3D space), and we're looking for points that lie on the intersection of all these hyperplanes.

### Computational Methods

In practice, we rarely use
[Cramer's rule](https://en.wikipedia.org/wiki/Cramer%27s_rule)
or matrix inversion to solve linear systems. Instead, we use

- [Gaussian elimination](https://en.wikipedia.org/wiki/Gaussian_elimination) with partial pivoting for general systems
- [LU decomposition](https://en.wikipedia.org/wiki/LU_decomposition) when solving multiple systems with the same matrix
- [Cholesky decomposition](https://en.wikipedia.org/wiki/Cholesky_decomposition) for positive definite symmetric systems
- [QR decomposition](https://en.wikipedia.org/wiki/QR_decomposition) for over-determined systems (least squares)
- [Iterative methods](https://en.wikipedia.org/wiki/Iterative_method#Linear_systems) like [conjugate gradient](https://en.wikipedia.org/wiki/Conjugate_gradient_method) for very large sparse systems

The choice of method depends on the structure of $A$ (sparse, symmetric, positive definite, etc.),
the size of $A$,
and the computational resources available.

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

The matrix $$A$$ is invertible if and only if the determinant is invertible,
*i.e.*,
has [multiplicative inverse](https://en.wikipedia.org/wiki/Multiplicative_inverse)
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

### Eigenvalues and eigenvectors of Hermitian and skew-Hermitian matrices

**The eigenvalues of a Hermitian matrix are real.**

Let $$A=A^H\in\complexes^{n\times n}$$ be a [Hermitian matrix](#hermitian-matrices).
Suppose $$\lambda\in\complexes$$ is an eigenvalue of $$A$$
and $$v\in\complexes^n$$ be the associated eigenvector.
Then

$$
\begin{array}{rcl}
\lambda \|v\|_2^2
	=
		\lambda v^H v
	=
		v^H \lambda v
	&=&
		v^H A v
\\
	&=&
		v^H A^H v
\\
	&=&
		(Av)^H v
	=
		(\lambda v)^H v
	=
		v^H \overline{\lambda} v
	=
		\overline{\lambda} \|v\|_2^2
\end{array}
$$

where $$\|\cdot\|_2$$ denotes the [standard Euclidean norm for complex vectors](https://en.wikipedia.org/wiki/Norm_(mathematics)#Finite-dimensional_complex_normed_spaces).
Since $$v$$ is a nonzero vector (by definition),

$$
\lambda = \overline{\lambda}
\iff
\Im(\lambda) = 0
\iff
\lambda \in \reals
$$

hence the proof!

Since a *real* [symmetric matrix](#symmetric-matrices) is a Hermitian matrix,
the eigenvalues of a real symmetric matrix are (of course) (also) real.

**The eigenvalues of a Hermitian matrix are purely imaginary.**

Let $$A=-A^H\in\complexes^{n\times n}$$ be a [skew-Hermitian matrix](#skew-hermitian-matrices).
Suppose $$\lambda\in\complexes$$ is an eigenvalue of $$A$$
and $$v\in\complexes^n$$ be the associated eigenvector.
Then

$$
\begin{array}{rcl}
\lambda \|v\|_2^2
	=
		\lambda v^H v
	=
		v^H \lambda v
	&=&
		v^H A v
\\
	&=&
		-v^H A^H v
\\
	&=&
		-(Av)^H v
	=
		-(\lambda v)^H v
	=
		-v^H \overline{\lambda} v
	=
		-\overline{\lambda} \|v\|_2^2,
\end{array}
$$

thus

$$
\lambda = -\overline{\lambda}
\iff
\Re (\lambda) = 0
$$

hence the proof!

Since a *real* [skew-symmetric matrix](#skew-symmetric-matrices) is a skew-Hermitian matrix,
the eigenvalues of a real skew-symmetric matrix are (of course) (also) purely imaginary.

**The eigenvectors of a Hermitian matrix with distinct eigenvalues are orthogonal.**

Let $$A=A^H\in\complexes^{n\times n}$$ be a [Hermitian matrix](#hermitian-matrices).
Suppose $$\lambda_1, \lambda_2\in\reals$$ are distinct eigenvalues of $$A$$
and $$v_1, v_2\in\complexes^n$$ are the associated eigenvectors respectively.
Note that eigenvalues of a Hermitian matrix are real.
Then

$$
\begin{array}{rcl}
\lambda_1 v_2^H v_1
=
	v_2^H \lambda_1 v_1
	&=& v_2^H Av_1
\\
	&=& v_2^H A^H v_1
=
	(Av_2)^H v_1
=
	(\lambda_2 v_2)^H v_1
=
	\lambda_2 v_2^H v_1
\end{array}
$$

thus

$$
(\lambda_1 - \lambda_2) v_2^H v_1 = 0
\iff
v_2^H v_1 = 0
$$

hence the proof!

Indeed for a Hermitian matrix,
we can *choose* $$n$$ [orthogonal](https://en.wikipedia.org/wiki/Orthogonality) eigenvectors!
Since we can normalize each (nonzero) eigenvector,
we can even choose $$n$$ [*orthonormal*](https://en.wikipedia.org/wiki/Orthonormality) eigenvectors!

Thus, every Hermitian matrix is [diagonalizable](#diagonalizability)!

**The eigenvectors of a skew-Hermitian matrix with distinct eigenvalues are orthogonal.**

Let $$A=-A^H\in\complexes^{n\times n}$$ be a [skew-Hermitian matrix](#skew-hermitian-matrices).
Suppose $$\lambda_1, \lambda_2\in\complexes$$ are distinct eigenvalues of $$A$$
and $$v_1, v_2\in\complexes^n$$ are the associated eigenvectors respectively.
Note that eigenvalues of a skew-Hermitian matrix are purely imaginary.
Then

$$
\begin{array}{rcl}
\lambda_1 v_2^H v_1
=
	v_2^H \lambda_1 v_1
	&=& v_2^H Av_1
\\
	&=& -v_2^H A^H v_1
=
	-(Av_2)^H v_1
=
	-(\lambda_2 v_2)^H v_1
=
	\lambda_2 v_2^H v_1
\end{array}
$$

thus

$$
(\lambda_1 - \lambda_2) v_2^H v_1 = 0
\iff
v_2^H v_1 = 0
$$

hence the proof!
(Note very subtle and interesting difference bewtween the above two proofs (to reach the same conclusion)!)

As for a Hermitian matrix,
for a skew-Hermitian matrix,
we can *choose* $$n$$ [orthogonal](https://en.wikipedia.org/wiki/Orthogonality) eigenvectors,
and even $$n$$ [*orthonormal*](https://en.wikipedia.org/wiki/Orthonormality) eigenvectors!

Thus, once again, every skew-Hermitian matrix is [diagonalizable](#diagonalizability)!

### Diagonalizability

If a basis exists that consists only of eigenvectors,
the matrix of $$f$$ on this basis has a very simple structure;
it is a [diagonal matrix](#diagonal-matrices) such that the entries on the main diagonal are eigenvalues,
and the other entries are zero.
In this case, the endomorphism and the matrix are said to be [diagonalizable](https://en.wikipedia.org/wiki/Diagonalizable_matrix).
More generally, an endomorphism and a matrix are also said diagonalizable,
if they become diagonalizable after [extending](/math/abstract-algebra#field-extensions---building-new-worlds) the field of scalars.
In this extended sense, if the characteristic polynomial is [square-free](https://en.wikipedia.org/wiki/Square-free_polynomial),
then the matrix is diagonalizable.

There are non-diagonalizable matrices, the simplest being

$$
{\begin{bmatrix}0&1\\0&0\end{bmatrix}} \in F^{2\times 2}.
$$

It cannot be diagonalizable since its square is the [zero matrix](https://en.wikipedia.org/wiki/Zero_matrix),
and the square of a nonzero diagonal matrix is never zero.

When an endomorphism is not diagonalizable,
there are bases on which it has a simple form, although not as simple as the diagonal form.
- The [Frobenius normal form](https://en.wikipedia.org/wiki/Frobenius_normal_form) does not need to extend the field of scalars and makes the characteristic polynomial immediately readable on the matrix.
- The [Jordan normal form](https://en.wikipedia.org/wiki/Jordan_normal_form) requires to extension of the field of scalar for containing all eigenvalues and differs from the diagonal form only by some entries that are just above the main diagonal and are equal to 1.

## Duality


A [<span class="emph">linear form</span>](https://en.wikipedia.org/wiki/Linear_form)
(also known as a <span class="emph">linear functional</span>, a <span class="emph">one-form</span>, or a <span class="emph">covector</span>)
is a [linear map](https://en.wikipedia.org/wiki/Linear_map)
from a vector space $$V$$ over a field $$F$$
to the field of scalars $$F$$,
viewed as a vector space over itself.
Equipped by [pointwise](https://en.wikipedia.org/wiki/Pointwise)
addition and multiplication by a scalar, the linear forms form a vector space,
called the [<span class="emph">dual space</span>](https://en.wikipedia.org/wiki/Dual_space) of $$V$$,
and usually denoted $$V^\ast$$ or $$V'$$.

If $$(v_1, \ldots, v_n)$$
is a basis of $$V$$
(which implies that $$V$$ is finite-dimensional),
then one can define,
for each $$1\leq i\leq n$$,
a linear map $$\nu_i^\ast$$
such that $$\nu_i^\ast(v_i) = 1$$
and $$\nu_i^\ast(v_j) = 0$$ if $$j \neq i$$.
These linear maps form a basis of $$V^\ast$$,
called the [dual basis](https://en.wikipedia.org/wiki/Dual_basis)
of $$v_1, \ldots, v_n$$.<sup><a href="#footnote4" id="ref4">4</a></sup>

For any $$v \in V$$, the map

$$
{f\to f({v} )}
$$

is a linear form on $$V^\ast$$.
This defines the [canonical linear map](https://en.wikipedia.org/wiki/Canonical_map)
from $$V$$ into $$(V^\ast)^\ast$$, the dual of $$V^\ast$$,
called the [double dual](https://en.wikipedia.org/wiki/Double_dual)
or [bidual](https://en.wikipedia.org/wiki/Bidual) of $$V$$.
This canonical map is an [isomorphism](https://en.wikipedia.org/wiki/Isomorphism) if $$V$$ is finite-dimensional,
and this allows identifying $$V$$ with its [bidual](https://en.wikipedia.org/wiki/Bidual).<sup><a href="#footnote5" id="ref5">5</a></sup>

There is thus a complete symmetry between a finite-dimensional vector space and its dual.
This motivates the frequent use, in this context, of the [bra–ket notation](https://en.wikipedia.org/wiki/Bra%E2%80%93ket_notation)

$$
\langle f,{x} \rangle
$$

for denoting $$f(x)$$.

### Dual map

Let

$$
f: V\to W
$$

be a linear map.
For every [<span class="emph">linear form</span>](https://en.wikipedia.org/wiki/Linear_form)
$$h$$ on $$W$$,
the [composite function](https://en.wikipedia.org/wiki/Composite_function) $$h \circ f$$
is a linear form on $$V$$.
This defines a linear map

$$
f^\ast: W^\ast\to V^\ast
$$

between the dual spaces,
which is called the <span class="emph">dual</span> or the <span class="emph">transpose</span> of $$f$$.

If $$V$$ and $$W$$ are finite-dimensional,
and $$M$$ is the matrix representing $$f$$ based on some ordered bases,
then the matrix of $$f^\ast$$ over the dual bases is $$M^T$$,
*i.e.*,
the [transpose](#transpose) of $$M$$
(obtained by exchanging rows and columns).

If elements of vector spaces and their duals are represented by column vectors,
this duality may be expressed in [bra–ket notation](https://en.wikipedia.org/wiki/Bra%E2%80%93ket_notation) by

$$
\langle h^T, M v\rangle = \langle h^TM, v \rangle.
$$

To highlight this symmetry, the two members of this equality are sometimes written

$$
\langle h^{T} \mid M \mid v \rangle.
$$

### Inner-product spaces

Besides these basic concepts, linear algebra also studies vector spaces with additional structure,
such as an [inner product](https://en.wikipedia.org/wiki/Inner_product).
The inner product is an example of a [bilinear form](https://en.wikipedia.org/wiki/Bilinear_form),
and it gives the vector space a geometric structure by allowing for the definition of length and angles.
Formally, an [inner product](https://en.wikipedia.org/wiki/Inner_product) is a map

$$
\innerp{\cdot}{\cdot}:
V \times V \to F
$$

that satisfies the following three axioms:

| axiom | statement |
|:-|:-|
| [conjugate](https://en.wikipedia.org/wiki/Complex_conjugate) symmetry | $$(\forall u,v\in V)(\innerp{u}{v}=\overline{\innerp{v}{u}})$$ |
| [linearity](https://en.wikipedia.org/wiki/Linear) (in the first argument) | $$(\forall u,v,w\in V\;\&\; \alpha, \beta\in F)(\innerp{\alpha u+\beta v}{w}=\alpha\innerp{u}{w} + \beta \innerp{v}{w}$$ |
| [positive-definiteness](https://en.wikipedia.org/wiki/Definite_bilinear_form) | $$(\forall v\in V)(\innerp{v}{v} \geq 0)$$ and $$(\forall v\in V)(\innerp{v}{v}=0 \iff v=0)$$ |

We can define the length of a vector v in V by

$$
\|v\|^{2}=\innerp{v}{v}
$$

and we can prove the
[Cauchy–Schwarz inequality](/math/inequalities#when-elegance-meets-power---the-art-of-inequalities):<sup><a href="#footnote6" id="ref6">6</a></sup>

$$
|\innerp{u}{v}| \leq \|u\| \|v\|.
$$

In particular,
when both $$u$$ and $$v$$ are nonzero,
we have

$$
-1 \leq \frac{\innerp{u}{v}}{\|u\| \|v\|} \leq  1
$$

hence we can call this quantity the cosine of the angle between the two vectors.


Two vectors are [orthogonal](https://en.wikipedia.org/wiki/Orthogonality) if $$\innerp{u}{v} = 0$$.
An
[orthonormal basis](https://en.wikipedia.org/wiki/Orthonormal_basis)
is a basis where all basis vectors have length 1 and are orthogonal to each other.
Given any finite-dimensional vector space,
an orthonormal basis could be found by the
[Gram–Schmidt procedure](https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt).<sup><a href="#footnote7" id="ref7">7</a></sup>

## Relationship with geometry

There is a strong relationship between [linear algebra](#linear-algebra) and [geometry](https://en.wikipedia.org/wiki/Geometry),
which started with the introduction by [René Descartes](https://en.wikipedia.org/wiki/Ren%C3%A9_Descartes)
of [Cartesian coordinates](https://en.wikipedia.org/wiki/Cartesian_coordinates) in 1637.
In this new (at that time) geometry, now called [Cartesian geometry](https://en.wikipedia.org/wiki/Cartesian_geometry),
points are represented by Cartesian coordinates,
which are sequences of three real numbers (in the case of the usual three-dimensional space).
The basic objects of geometry, which are [lines](https://en.wikipedia.org/wiki/Line_(geometry))
and [planes](https://en.wikipedia.org/wiki/Plane_(geometry)) are represented by linear equations.
Thus, computing intersections of lines and planes amounts to solving systems of linear equations. This was one of the main motivations for developing linear algebra.

Most geometric transformation, such as
translations,
rotations,
reflections,
[rigid motions](https://en.wikipedia.org/wiki/Rigid_motion),
[isometries](https://en.wikipedia.org/wiki/Isometry),
and
[projections](https://en.wikipedia.org/wiki/Projection_(mathematics)) transform lines into lines.
It follows that they can be defined, specified, and studied in terms of linear maps.
This is also the case of [homographies](https://en.wikipedia.org/wiki/Homography)
and
[Möbius transformations](https://en.wikipedia.org/wiki/M%C3%B6bius_transformation)
when considered as transformations of a [projective space](https://en.wikipedia.org/wiki/Projective_space).

Until the end of the 19th century,
geometric spaces were defined by axioms relating points, lines, and planes,
*i.e.*, [synthetic geometry](https://en.wikipedia.org/wiki/Synthetic_geometry).
Around this date, it appeared that one may also define geometric spaces by constructions involving vector spaces,
*e.g.*, [projective space](https://en.wikipedia.org/wiki/Projective_space) and [affine space](https://en.wikipedia.org/wiki/Affine_space).
It has been shown that the two approaches are essentially equivalent.
In classical geometry, the involved vector spaces are vector spaces over the reals, but the constructions may be extended to vector spaces over any field, allowing considering geometry over arbitrary fields,
including [finite fields](/math/abstract-algebra#field-examples).<sup><a href="#footnote8" id="ref8">8</a></sup>

## Usage and applications

### Functional analysis

[Functional analysis](https://en.wikipedia.org/wiki/Functional_analysis)
studies [function spaces](https://en.wikipedia.org/wiki/Function_space).
These are vector spaces with additional structure, such as [Hilbert spaces](https://en.wikipedia.org/wiki/Hilbert_space).
Linear algebra is thus a fundamental part of functional analysis and its applications, which include,
in particular, [quantum mechanics](https://en.wikipedia.org/wiki/Quantum_mechanics),
*e.g.*, [wave functions](https://en.wikipedia.org/wiki/Wave_function)
and [Fourier analysis](https://en.wikipedia.org/wiki/Fourier_analysis),
*e.g.*, [orthogonal basis](https://en.wikipedia.org/wiki/Orthogonal_basis).

### Scientific computation

Nearly all [scientific computations](https://en.wikipedia.org/wiki/Scientific_computation)
involve linear algebra.
Consequently, linear algebra algorithms have been highly optimized.
[BLAS](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms) and [LAPACK](https://en.wikipedia.org/wiki/LAPACK)
are the best known implementations.
For improving efficiency, some of them configure the algorithms automatically,
at run time, to adapt them to the specificities of the computer,
*e.g.*,
[cache](https://en.wikipedia.org/wiki/Cache_(computing)) size
and the number of available [cores](https://en.wikipedia.org/wiki/Multi-core_processor).

Since the 1960s there have been processors with specialized instructions for optimizing the operations of linear algebra, optional array processors under the control of a conventional processor, supercomputers designed for array processing and conventional processors augmented with vector registers.

Some contemporary [processors](https://en.wikipedia.org/wiki/Processor_(computing)),
typically [graphics processing units (GPU)](https://en.wikipedia.org/wiki/Graphics_processing_units),
are designed with a matrix structure, for optimizing the operations of linear algebra.

### Geometry of ambient space

The [modeling](https://en.wikipedia.org/wiki/Mathematical_model) of [ambient space](https://en.wikipedia.org/wiki/Ambient_space)
is based on [geometry](https://en.wikipedia.org/wiki/Geometry).
Sciences concerned with this space use geometry widely.
This is the case with [mechanics](https://en.wikipedia.org/wiki/Mechanics) and [robotics](https://en.wikipedia.org/wiki/Robotics),
for describing [rigid body dynamics](https://en.wikipedia.org/wiki/Rigid_body_dynamics);
[geodesy](https://en.wikipedia.org/wiki/Geodesy) for describing [Earth shape](https://en.wikipedia.org/wiki/Earth_shape);
[perspectivity](https://en.wikipedia.org/wiki/Perspectivity), [computer vision](https://en.wikipedia.org/wiki/Computer_vision),
and [computer graphics](https://en.wikipedia.org/wiki/Computer_graphics),
for describing the relationship between a scene and its plane representation; and many other scientific domains.

In all these applications, [synthetic geometry](https://en.wikipedia.org/wiki/Synthetic_geometry)
is often used for general descriptions and a qualitative approach,
but for the study of explicit situations, one must compute with [coordinates](#coordinates).
This requires the heavy use of [linear algebra](#linear-algebra).

### Study of complex systems

Most physical phenomena are modeled by [partial differential equations (PDEs)](https://en.wikipedia.org/wiki/Partial_differential_equation).
To solve them, one usually [decomposes the space](https://en.wikipedia.org/wiki/Discretization)
in which the solutions are searched into small, mutually interacting cells.
For [linear systems](https://en.wikipedia.org/wiki/Linear_system) this interaction involves linear functions.
For [nonlinear systems](https://en.wikipedia.org/wiki/Nonlinear_systems),
this interaction is often approximated by linear functions.
This is called a linear model or first-order approximation.

Linear models are frequently used for complex nonlinear real-world systems
because they make [parametrization](https://en.wikipedia.org/wiki/Parametrization_(geometry)) more manageable.
In both cases, very large matrices are generally involved.

[Weather forecasting](https://en.wikipedia.org/wiki/Weather_forecasting)
(or more specifically, [parametrization for atmospheric modeling](https://en.wikipedia.org/wiki/Parametrization_(atmospheric_modeling)))
is a typical example of a real-world application, where the whole Earth atmosphere is divided into cells of, say,
100 km of width and 100 km of height.

### Fluid mechanics, fluid dynamics, and thermal energy systems

Linear algebra, a branch of mathematics dealing with vector spaces and linear mappings between these spaces, plays a critical role in various engineering disciplines, including fluid mechanics, fluid dynamics, and thermal energy systems. Its application in these fields is multifaceted and indispensable for solving complex problems.

In fluid mechanics, linear algebra is integral to understanding and solving problems related to the behavior of fluids. It assists in the modeling and simulation of fluid flow, providing essential tools for the analysis of fluid dynamics problems. For instance, linear algebraic techniques are used to solve systems of differential equations that describe fluid motion. These equations, often complex and non-linear, can be linearized using linear algebra methods, allowing for simpler solutions and analyses.

In the field of fluid dynamics, linear algebra finds its application in computational fluid dynamics (CFD), a branch that uses numerical analysis and data structures to solve and analyze problems involving fluid flows. CFD relies heavily on linear algebra for the computation of fluid flow and heat transfer in various applications. For example, the Navier–Stokes equations, fundamental in fluid dynamics, are often solved using techniques derived from linear algebra. This includes the use of matrices and vectors to represent and manipulate fluid flow fields.

Furthermore, linear algebra plays a crucial role in thermal energy systems, particularly in power systems analysis. It is used to model and optimize the generation, transmission, and distribution of electric power. Linear algebraic concepts such as matrix operations and eigenvalue problems are employed to enhance the efficiency, reliability, and economic performance of power systems. The application of linear algebra in this context is vital for the design and operation of modern power systems, including renewable energy sources and smart grids.

Overall, the application of linear algebra in fluid mechanics, fluid dynamics, and thermal energy systems is an example of the profound interconnection between mathematics and engineering. It provides engineers with the necessary tools to model, analyze, and solve complex problems in these domains, leading to advancements in technology and industry.

## Extensions &amp; generalizations

### Module theory

The existence of multiplicative inverses in fields is not involved in the axioms defining a vector space.
One may thus replace the field of scalars by a [ring](/math/abstract-algebra#rings---where-addition-meets-multiplication) $$R$$,
and this gives the structure called a <span class="emph">module</span> over $$R$$, or $$R$$-module.

The concepts of linear independence, span, basis, and linear maps,
which are also called [module homomorphisms](https://en.wikipedia.org/wiki/Module_homomorphism),
are defined for modules exactly as for vector spaces, with the essential difference that
<!--if R is not a field,-->
there are modules that do not have any basis.
The modules that have a basis are the [free modules](https://en.wikipedia.org/wiki/Free_module),
and those that are spanned by a finite set are
the [finitely generated modules](https://en.wikipedia.org/wiki/Finitely_generated_module).
Module homomorphisms between finitely generated free modules may be represented by matrices.
The theory of matrices over a [ring](/math/abstract-algebra#rings---where-addition-meets-multiplication)
is similar to that of matrices over a [field](/math/abstract-algebra#fields---the-realm-of-perfect-division),
except that [determinants](#determinant) exist only if the ring is [commutative](https://en.wikipedia.org/wiki/Commutative_ring),
and that a square matrix over a [commutative ring]((https://en.wikipedia.org/wiki/Commutative_ring))
is [invertible](https://en.wikipedia.org/wiki/Invertible_matrix)
only if its determinant has a [multiplicative inverse](https://en.wikipedia.org/wiki/Multiplicative_inverse)
in the ring.

Vector spaces are completely characterized by their dimension (up to an isomorphism).
In general, there is not such a complete classification for modules,
even if one restricts oneself to finitely generated modules.
However, every module is a [cokernel](https://en.wikipedia.org/wiki/Cokernel) of a homomorphism of free modules.

Modules over the integers can be identified with [abelian groups](https://en.wikipedia.org/wiki/Abelian_group),
since the multiplication by an integer may be identified as a repeated addition.
Most of the theory of abelian groups may be extended to modules over a [principal ideal domain](https://en.wikipedia.org/wiki/Principal_ideal_domain).
In particular, over a principal ideal domain, every submodule of a free module is free,
and the [fundamental theorem of finitely generated abelian groups](https://en.wikipedia.org/wiki/Fundamental_theorem_of_finitely_generated_abelian_groups)
may be extended straightforwardly to finitely generated modules over a principal ring.

There are many rings for which there are algorithms for solving linear equations and systems of linear equations.
However, these algorithms have generally a [computational complexity](https://en.wikipedia.org/wiki/Computational_complexity)
that is much higher than similar algorithms over a field.
For more details, see [linear equation over a ring](https://en.wikipedia.org/wiki/Linear_equation_over_a_ring).

### Multilinear algebra and tensors

In [multilinear algebra](https://en.wikipedia.org/wiki/Multilinear_algebra),
one considers multivariable linear transformations,
that is,
mappings that are linear in each of several different variables.
This line of inquiry naturally leads to the idea of the [dual space](https://en.wikipedia.org/wiki/Dual_space),
the vector space $$V^\ast$$
consisting of linear maps $$f : V \to F$$ where $$F$$ is the field of scalars.
Multilinear maps $$T: V^n \to F$$ can be described via [tensor products](https://en.wikipedia.org/wiki/Tensor_product) of elements of V*.

If, in addition to vector addition and scalar multiplication,
there is a bilinear vector product $$V\times V \to V$$,
the vector space is called an [algebra](https://en.wikipedia.org/wiki/Algebra_over_a_field);
for instance, associative algebras are algebras with an associate vector product (like the algebra of square matrices, or the algebra of polynomials).

### Topological vector spaces

Vector spaces that are not finite-dimensional often require additional structure to be tractable.
A [normed vector space](/math/topological-spaces#banach-spaces---the-realm-of-completeness)
is a vector space along with a function called a [norm](https://en.wikipedia.org/wiki/Norm_(mathematics)).
The norm induces a [metric](https://en.wikipedia.org/wiki/Metric_(mathematics)),
which measures the distance between elements, and induces a [topology](/math/topological-space),
which allows for a definition of continuous maps.
The metric also allows for a definition of [limits](https://en.wikipedia.org/wiki/Limit_(mathematics))
and [completeness](https://en.wikipedia.org/wiki/Complete_metric_space)
&ndash;
a normed vector space that is complete is known as a [Banach space](/math/topological-spaces#banach-space).

A complete metric space along with the additional structure of an [inner product](/math/linear-algebra#inner-product-spaces)
(a conjugate symmetric [sesquilinear form](https://en.wikipedia.org/wiki/Sesquilinear_form))
is known as a [Hilbert space](/math/topological-spaces#hilbert-space),
which is in some sense a particularly well-behaved Banach space.

[Functional analysis](https://en.wikipedia.org/wiki/Functional_analysis) applies the methods of linear algebra
alongside those of [mathematical analysis](https://en.wikipedia.org/wiki/Mathematical_analysis)
to study various function spaces; the central objects of study in functional analysis are
[$$L^p$$ spaces](/math/topological-spaces#lp-space),
which are [Banach spaces](/math/topological-spaces#banach-space),
and especially the $$L^2$$ space of square-integrable functions,
which is the only [Hilbert space](/math/topological-spaces#hilbert-space) among them.

Functional analysis is of particular importance to [quantum mechanics](https://en.wikipedia.org/wiki/Quantum_mechanics),
the theory of [partial differential equations](https://en.wikipedia.org/wiki/Partial_differential_equation),
[digital signal processing](https://en.wikipedia.org/wiki/Digital_signal_processing),
and
[electrical engineering](https://en.wikipedia.org/wiki/Electrical_engineering).
It also provides the foundation and theoretical framework
that underlies the [Fourier transform](https://en.wikipedia.org/wiki/Fourier_transform) and related methods.

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
<li id="footnote4">
	If $V$ is not finite-dimensional,
	the $\nu_i^\ast$ may be defined similarly;
	they are linearly independent, but do not form a basis.
	&nbsp;<a href="#ref4">↩</a></li>
<li id="footnote5">
	In the infinite-dimensional case, the canonical map is injective, but not surjective.
	&nbsp;<a href="#ref5">↩</a></li>
<li id="footnote6">
	Note that the [Cauchy–Schwarz inequality](/math/inequalities#when-elegance-meets-power---the-art-of-inequalities)
	can be really simply written as
	an equivalent inequality:

	$$
		\innerp{u}{v} \leq \|u\|\|v\|
	$$

	that is, we do not need the absolute value operator $|\cdot|$.
	(Carefully think about it, and you'll realize it's true!)
	&nbsp;<a href="#ref6">↩</a></li>
<li id="footnote7">
	The <a href="https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt">Gram–Schmidt procedure</a>
	is and should be never used in practice
	due to its numerical instability.
	Instead,
	<a href="https://en.wikipedia.org/wiki/QR_decomposition">QR decomposition</a>
	or
	<a href="https://en.wikipedia.org/wiki/Singular_value_decomposition">singular value decomposition (SVD)</a>
	should be used!
	&nbsp;<a href="#ref7">↩</a></li>
<li id="footnote8">
	Presently, most textbooks introduce geometric spaces from linear algebra, and geometry is often presented, at the elementary level, as a subfield of linear algebra.
	&nbsp;<a href="#ref8">↩</a></li>
</ol>
