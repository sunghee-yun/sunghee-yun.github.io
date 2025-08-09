---
title: Math Stories
date: Fri Aug  1 00:00:00 PDT 2025
last_modified_at: Sun Aug 10 02:36:29 KST 2025
permalink: /math/rig/math-stories
categories:
- blog
tags:
- math
- stories
- duality
- fundamental theorems
toc: true
toc_label: '&nbsp;Table of Contents'
toc_icon: fa-solid fa-list
toc_sticky: true
usemathjax: true
---

posted: {{page.date | date: "%d-%b-%Y"}}
&amp;
updated: {{page.last_modified_at | date: "%d-%b-%Y"}}
{:.notice - -primary}

# NotebookLM Podcast

- [14:34](https://notebooklm.google.com/notebook/7dae4e46-7c95-42b0-80f0-ff513147341e/audio)
$$
	%
	\newcommand{\algA}{\algk{A}}
	\newcommand{\algC}{\algk{C}}
	\newcommand{\bigtimes}{\times}
	\newcommand{\compl}[1]{\tilde{#1}}
	\newcommand{\complexes}{\mathbb{C}}
	\newcommand{\dom}{\mathop{\bf dom {}}}
	\newcommand{\ereals}{\reals\cup\{-\infty,\infty\}}
	\newcommand{\field}{\mathbb{F}}
	\newcommand{\integers}{\mathbb{Z}}
	\newcommand{\lbdseqk}[1]{\seqk{\lambda}{#1}}
	\newcommand{\meas}[3]{({#1}, {#2}, {#3})}
	\newcommand{\measu}[2]{({#1}, {#2})}
	\newcommand{\meast}[3]{\left({#1}, {#2}, {#3}\right)}
	\newcommand{\naturals}{\mathbb{N}}
	\newcommand{\nuseqk}[1]{\seqk{\nu}{#1}}
	\newcommand{\pair}[2]{\langle {#1}, {#2}\rangle}
	\newcommand{\rationals}{\mathbb{Q}}
	\newcommand{\reals}{\mathbb{R}}
	\newcommand{\seq}[1]{\left\langle{#1}\right\rangle}
	\newcommand{\powerset}{\mathcal{P}}
	\newcommand{\pprealk}[1]{\reals_{++}^{#1}}
	\newcommand{\ppreals}{\mathbb{R}_{++}}
	\newcommand{\prealk}[1]{\reals_{+}^{#1}}
	\newcommand{\preals}{\mathbb{R}_+}
	\newcommand{\tXJ}{\topos{X}{J}}
	%
	\newcommand{\relint}{\mathop{\bf relint {}}}
	\newcommand{\boundary}{\mathop{\bf bd {}}}
	\newcommand{\subsetset}[1]{\mathcal{#1}}
	\newcommand{\Tr}{\mathcal{\bf Tr}}
	\newcommand{\symset}[1]{\mathbf{S}^{#1}}
	\newcommand{\possemidefset}[1]{\mathbf{S}_+^{#1}}
	\newcommand{\posdefset}[1]{\mathbf{S}_{++}^{#1}}
	\newcommand{\ones}{\mathbf{1}}
	\newcommand{\Prob}{\mathop{\bf Prob {}}}
	\newcommand{\prob}[1]{\Prob\left\{#1\right\}}
	\newcommand{\Expect}{\mathop{\bf E {}}}
	\newcommand{\Var}{\mathop{\bf  Var{}}}
	\newcommand{\Mod}[1]{\;(\text{mod}\;#1)}
	\newcommand{\ball}[2]{B(#1,#2)}
	\newcommand{\generates}[1]{\langle {#1} \rangle}
	\newcommand{\isomorph}{\approx}
	\newcommand{\isomorph}{\approx}
	\newcommand{\nullspace}{\mathcalfont{N}}
	\newcommand{\range}{\mathcalfont{R}}
	\newcommand{\diag}{\mathop{\bf diag {}}}
	\newcommand{\rank}{\mathop{\bf rank {}}}
	\newcommand{\Ker}{\mathop{\mathrm{Ker} {}}}
	\newcommand{\Map}{\mathop{\mathrm{Map} {}}}
	\newcommand{\End}{\mathop{\mathrm{End} {}}}
	\newcommand{\Img}{\mathop{\mathrm{Im} {}}}
	\newcommand{\Aut}{\mathop{\mathrm{Aut} {}}}
	\newcommand{\Gal}{\mathop{\mathrm{Gal} {}}}
	\newcommand{\Irr}{\mathop{\mathrm{Irr} {}}}
	\newcommand{\arginf}{\mathop{\mathrm{arginf}}}
	\newcommand{\argsup}{\mathop{\mathrm{argsup}}}
	\newcommand{\argmin}{\mathop{\mathrm{argmin}}}
	\newcommand{\ev}{\mathop{\mathrm{ev} {}}}
	\newcommand{\affinehull}{\mathop{\bf aff {}}}
	\newcommand{\cvxhull}{\mathop{\bf Conv {}}}
	\newcommand{\epi}{\mathop{\bf epi {}}}
	\newcommand{\injhomeo}{\hookrightarrow}
	\newcommand{\perm}[1]{\text{Perm}(#1)}
	\newcommand{\aut}[1]{\text{Aut}(#1)}
	\newcommand{\ideal}[1]{\mathfrak{#1}}
	\newcommand{\bigset}[2]{\left\{#1\left|{#2}\right.\right\}}
	\newcommand{\bigsetl}[2]{\left\{\left.{#1}\right|{#2}\right\}}
	\newcommand{\primefield}[1]{\field_{#1}}
	\newcommand{\dimext}[2]{[#1:{#2}]}
	\newcommand{\restrict}[2]{#1|{#2}}
	\newcommand{\algclosure}[1]{#1^\mathrm{a}}
	\newcommand{\finitefield}[2]{\field_{#1^{#2}}}
	\newcommand{\frobmap}[2]{\varphi_{#1,{#2}}}
	%
	%\newcommand{\algfontmode}{}
	%
	%\ifdefined\algfontmode
	%\newcommand\mathalgfont[1]{\mathcal{#1}}
	%\newcommand\mathcalfont[1]{\mathscr{#1}}
	%\else
	\newcommand\mathalgfont[1]{\mathscr{#1}}
	\newcommand\mathcalfont[1]{\mathcal{#1}}
	%\fi
	%
	%\def\DeltaSirDir{yes}
	%\newcommand\sdirletter[2]{\ifthenelse{\equal{\DeltaSirDir}{yes}}{\ensuremath{\Delta #1}}{\ensuremath{#2}}}
	\newcommand{\sdirletter}[2]{\Delta #1}
	\newcommand{\sdirlbd}{\sdirletter{\lambda}{\Delta \lambda}}
	\newcommand{\sdir}{\sdirletter{x}{v}}
	\newcommand{\seqk}[2]{#1^{(#2)}}
	\newcommand{\seqscr}[3]{\seq{#1}_{#2}^{#3}}
	\newcommand{\xseqk}[1]{\seqk{x}{#1}}
	\newcommand{\sdirk}[1]{\seqk{\sdir}{#1}}
	\newcommand{\sdiry}{\sdirletter{y}{\Delta y}}
	\newcommand{\slen}{t}
	\newcommand{\slenk}[1]{\seqk{\slen}{#1}}
	\newcommand{\ntsdir}{\sdir_\mathrm{nt}}
	\newcommand{\pdsdir}{\sdir_\mathrm{pd}}
	\newcommand{\sdirnu}{\sdirletter{\nu}{w}}
	\newcommand{\pdsdirnu}{\sdirnu_\mathrm{pd}}
	\newcommand{\pdsdiry}{\sdiry_\mathrm{pd}}
	\newcommand\pdsdirlbd{\sdirlbd_\mathrm{pd}}
	%
	\newcommand{\normal}{\mathcalfont{N}}
	%
	\newcommand{\algk}[1]{\mathalgfont{#1}}
	\newcommand{\collk}[1]{\mathcalfont{#1}}
	\newcommand{\classk}[1]{\collk{#1}}
	\newcommand{\indexedcol}[1]{\{#1\}}
	\newcommand{\rel}{\mathbf{R}}
	\newcommand{\relxy}[2]{#1\;\rel\;{#2}}
	\newcommand{\innerp}[2]{\langle{#1},{#2}\rangle}
	\newcommand{\innerpt}[2]{\left\langle{#1},{#2}\right\rangle}
	\newcommand{\closure}[1]{\overline{#1}}
	\newcommand{\support}{\mathbf{support}}
	\newcommand{\set}[2]{\{#1|#2\}}
	\newcommand{\metrics}[2]{\langle {#1}, {#2}\rangle}
	\newcommand{\interior}[1]{#1^\circ}
	\newcommand{\topol}[1]{\mathfrak{#1}}
	\newcommand{\topos}[2]{\langle {#1}, \topol{#2}\rangle} % topological space
	%
	\newcommand{\alg}{\algk{A}}
	\newcommand{\algB}{\algk{B}}
	\newcommand{\algF}{\algk{F}}
	\newcommand{\algR}{\algk{R}}
	\newcommand{\algX}{\algk{X}}
	\newcommand{\algY}{\algk{Y}}
	%
	\newcommand\coll{\collk{C}}
	\newcommand\collB{\collk{B}}
	\newcommand\collF{\collk{F}}
	\newcommand\collG{\collk{G}}
	\newcommand{\tJ}{\topol{J}}
	\newcommand{\tS}{\topol{S}}
	\newcommand\openconv{\collk{U}}
	%
	\newenvironment{my-matrix}[1]{\begin{bmatrix}}{\end{bmatrix}}
	\newcommand{\colvectwo}[2]{\begin{my-matrix}{c}{#1}\\{#2}\end{my-matrix}}
	\newcommand{\colvecthree}[3]{\begin{my-matrix}{c}{#1}\\{#2}\\{#3}\end{my-matrix}}
	\newcommand{\rowvecthree}[3]{\begin{bmatrix}{#1}&{#2}&{#3}\end{bmatrix}}
	\newcommand{\mattwotwo}[4]{\begin{bmatrix}{#1}&{#2}\\{#3}&{#4}\end{bmatrix}}
	%
	\newcommand\optfdk[2]{#1^\mathrm{#2}}
	\newcommand\tildeoptfdk[2]{\tilde{#1}^\mathrm{#2}}
	\newcommand\fobj{\optfdk{f}{obj}}
	\newcommand\fie{\optfdk{f}{ie}}
	\newcommand\feq{\optfdk{f}{eq}}
	\newcommand\tildefobj{\tildeoptfdk{f}{obj}}
	\newcommand\tildefie{\tildeoptfdk{f}{ie}}
	\newcommand\tildefeq{\tildeoptfdk{f}{eq}}
	\newcommand\xdomain{\mathcalfont{X}}
	\newcommand\xobj{\optfdk{\xdomain}{obj}}
	\newcommand\xie{\optfdk{\xdomain}{ie}}
	\newcommand\xeq{\optfdk{\xdomain}{eq}}
	\newcommand\optdomain{\mathcalfont{D}}
	\newcommand\optfeasset{\mathcalfont{F}}
	%
	\newcommand{\bigpropercone}{\mathcalfont{K}}
	%
	\newcommand{\prescript}[3]{\;^{#1}{#3}}
	%
	%
$$










<h1 id="super-title-page:Stories">Math Stories</h1>


<h2 id="title-page:Fundamental---Theorems">Fundamental Theorems</h2>


<h3 id="my-foilhead-2">Fundamental theorem of arithmetic</h3>

<div class="theorem" id="theorem:Fundamental---theorem---of---arithmetic" data-name="Fundamental theorem of arithmetic">
	
integer $n\geq2$ can be factored uniquely into products of primes,
<i>i.e.</i>,
exist distinct primes, $p_1$, &hellip;, $p_k$, and $e_1,\ldots, e_k\in\naturals$
such that

$$

n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}

$$


</div>

<h3 id="my-foilhead-3">Fundamental theorem of algebra</h3>

<div class="theorem" id="theorem:Fundamental---theorem---of---algebra" data-name="Fundamental theorem of algebra">
	
every non-constant single-variable polynomial with complex coefficients
has at least one complex root,
or equivalently,
(the field of complex numbers) is algebraically closed,
or equivalently,
every non-zero, single-variable, degree $n$ polynomial with complex coefficients has,
counted with multiplicity, exactly $n$ complex roots.

</div>
<ul>
<li>
	the <span class="name-font">fundamental theorem of algebra</span>, also called <span class="name-font">d'Alembert's theorem</span> or the <span class="name-font">d'Alembert–Gauss theorem</span>

</li>
<li>
	despite its name,
not fundamental for modern algebra;
named when algebra was synonymous with the theory of equations

</li>
</ul>

<h3 id="my-foilhead-4">Fundamental theorem of calculus</h3>

<div class="theorem" id="theorem:Fundamental---theorem---of---calculus" data-name="Fundamental theorem of calculus">
	


	<ul>
	<li>
		<span class="define">first fundamental theorem of calculus</span>
-
for continuous real-valued function $f:[a,b]\to\reals$,
function $F:[a,b]\to\reals$
defined by
$
F(x) = \int_a^x f(t) dt
$
is uniformly continuous on $[a,b]$
and
differentiable on open interval $(a,b)$
and

$$

F'(x) = f(x)

$$

for all $x\in(a,b)$,
hence
$F$ is antiderivative of $f$

	</li>
	<li>
		<span class="define">second fundamental theorem of calculus</span>
or
<span class="define">Newton-Leibniz theorem</span>
-
for real-valued function $f:[a,b]\to\reals$
and
continuous function $F:[a,b]\to\reals$
which is antiderivative of $f$ in $(a,b)$,
<i>i.e.</i>
$
F'(x) = f(x)
$,
if $f$ is Riemann integrable on $[a,b]$,
then

$$

\int_a^b f(x) dx = F(b) - F(a)

$$


	</li>
	</ul>

</div>


<h3 id="my-foilhead-5">Fundamental theorem of calculus for line integrals</h3>

<div class="theorem" id="theorem:gradient---theorem" data-name="gradient theorem">
	
line integral through a gradient field can be evaluated by evaluating the original scalar field at the endpoints of the curve,
<i>i.e.</i>,
if $\varphi: X \to \reals$ is differentiable function and $\gamma$ is curve in $X\subset \reals$
which
starts at point $p\in\reals^n$
and
ends at point $q\in\reals^n$,
then

$$

\int_\gamma \nabla \varphi(x)^T dx = \varphi(q) - \varphi(p)

$$


</div>
<ul>
<li>
	generalization of the second fundamental theorem of calculus
of <a href="#theorem:Fundamental---theorem---of---calculus">Fundamental theorem of calculus</a>

</li>
</ul>

<h3 id="my-foilhead-6">Fundamental theorem of cyclic groups</h3>

<div class="theorem" id="theorem:Fundamental---theomre---of---cyclic---groups" data-name="Fundamental theomre of cyclic groups">
	
every subgroup of a cyclic group is cyclic;
moreover,
for finite cyclic group of order $n$,
every subgroup's order is a divisor of $n$,
and exists exactly one subgroup for each divisor.

</div>

<h3 id="my-foilhead-7">Fundamental theorem of equivalence relations</h3>

<div class="theorem" id="theorem:Fundamental---theorem---of---equivalence---relations" data-name="Fundamental theorem of equivalence relations">
	
equivalence relation $\sim$ on set $X$ partitions $X$;
conversely,
corresponding to any partition of $X$,
exists equivalence relation $\sim$ on $X$

</div>

<h3 id="my-foilhead-8">Fundamental theorem of finite abelian groups</h3>

<div class="theorem" id="theorem:Fundamental---theorem---of---finite---abelian---groups" data-name="Fundamental theorem of finite abelian groups">
	
every finite abelian group
can be expressed as direct sum of cyclic subgroups of prime-power order,
<i>i.e.</i>,
any finite abelian group $G$ is
isomorphic to direct sum of form

$$

\bigoplus_{i=1}^u \left(\integers/{k_i}\integers\right)

$$

in either of the following canonical ways
	<ul>
	<li>
		numbers $k_1$, &hellip;, $k_u$ are powers of (not necessarily distinct) primes

	</li>
	<li>
		$k_1$ divides $k_2$, which divides $k_3$, and so on up to $k_u$

	</li>
	</ul>

</div>
<ul>
<li>
	also known as
<span class="name-font">basis theorem for finite abelian groups</span>

</li>
</ul>

<h3 id="my-foilhead-9">Fundamental theorem of finitely generated abelian groups</h3>

<ul>
<li>
	<a href="#theorem:Fundamental---theorem---of---finitely---generated---abelian---groups">Fundamental theorem of finitely generated abelian groups</a>
generalizes
<a href="#theorem:Fundamental---theorem---of---finite---abelian---groups">Fundamental theorem of finite abelian groups</a>
in two ways

</li>
</ul>
<div class="theorem" id="theorem:Fundamental---theorem---of---finitely---generated---abelian---groups" data-name="Fundamental theorem of finitely generated abelian groups">
	

	<ul>
	<li>
		primary decomposition
-
every finitely generated abelian group is isomorphic to a direct sum of primary cyclic groups and infinite cyclic groups,
<i>i.e.</i>,
every finitely generated abelian group $G$ is isomorphic to group of form

$$

G
=
\integers^n
\oplus
\left(\integers/q_1 \integers\right)
\oplus
\cdots
\oplus
\left(\integers/q_t \integers\right)

$$

where $n\geq0$ is rank,
and
numbers $q_1, \ldots, q_t$
are powers of (not necessarily distinct) prime numbers;
in particular,
$G$ is finite if and only if $n=0$,
values of $n, q_1, \ldots, q_t$
are (up to rearranging indices) uniquely determined by $G$,
<i>i.e.</i>,
exists one and only one way to represent $G$ as such decomposition

	</li>
	<li>
		invariant factor decomposition
-
can also write any finitely generated abelian group $G$ as direct sum of form

$$

G
=
\integers^{n}
\oplus
\left(\integers /{k_{1}}\integers\right)
\oplus
\cdots
\oplus
\left(\integers /{k_{u}}\integers\right)

$$

where $k_1$ divides $k_2$,
which divides $k_3$ and so on up to $k_u$;
again, rank $n$ and invariant factors $k_1, \ldots, k_u$
are uniquely determined by $G$ (here with a unique order);
rank and sequence of invariant factors determine group up to isomorphism

	</li>
	</ul>

</div>

<h3 id="my-foilhead-10">Fundamental theorem for Galois theory</h3>

<div class="theorem" id="theorem:Fundamental---theorem---for---Galois---theory" data-name="Fundamental theorem for Galois theory">
	
for finite Galois extension, $K/k$

	<ul>
	<li>
		map $H \mapsto K^H$
induces isomorphism between
set of subgroups of $G(K/k)$ &amp; set of intermediate fields

	</li>
	<li>
		subgroup, $H$, of $G(K/k)$,
is normal
if and only if
$K^H/k$ is Galois

	</li>
	<li>
		for normal subgroup, $H$,
$\sigma\mapsto \restrict{\sigma}{K^H}$
induces isomorphism between $G(K/k)/H$ and
$G(K^H/k)$

	</li>
	</ul>

</div>

<h3 id="my-foilhead-11">Fundamental theorem on homeomorphisms</h3>

<div class="theorem" id="theorem:Fundamental---theorem---on---homeomorphisms" data-name="Fundamental theorem on homeomorphisms">
	
for two groups $G$ and $H$ and
group homeomorphism $f:G\to H$,
normal subgroup $N\subset G$,
natural surjective homeomorphism $\varphi:G\to G/N$
if $N$ is subset of $\Ker{f}$,
exists unique homeomorphism $h:G/N\to H$
such that

$$

f = h \circ \varphi

$$


</div>

<h3 id="my-foilhead-12">Fundamental theorem of ideal theory in number fields</h3>

<div class="theorem" id="theorem:Fundamental---theorem---of---ideal---theory---in---number---fields" data-name="Fundamental theorem of ideal theory in number fields">
	
every nonzero proper ideal in ring of integers
of number field admits unique factorization into
product of nonzero prime ideals;
in other words, every ring of integers of number field is Dedekind domain

</div>

<h3 id="my-foilhead-13">Fundamental theorem of linear algebra</h3>

<div class="theorem" id="theorem:rank-nullity---theorem" data-name="rank-nullity theorem">
	
number of columns of matrix $M$ is
sum of rank of $M$ and nullity of $M$,
or equivalently,
dimension of domain of linear transformation $f$
is sum of rank of $f$ (dimension of image of $f$)
and
nullity of $f$ (dimension of kernel of $f$)

</div>

<h3 id="my-foilhead-14">Fundamental theorem of linear programming</h3>

<div class="theorem" id="theorem:Fundamental---theorem---of---linear---programming" data-name="Fundamental theorem of linear programming">
	
for linear program

$$

\begin{array}{ll}
\mbox{minimal} & c^Tx
\\
\mbox{subject to} & Ax \leq b
\end{array}

$$

if $P=\set{x\in\reals^n}{Ax \leq b}$
is bounded polyhedron (hence polytope)
and $x^\ast$ is optimal solution,
then $x^\ast$ is either extreme point (<i>i.e.</i>, vertex) of $P$
or lies on some face of $P$

</div>

<h3 id="my-foilhead-15">Fundamental theorem of symmetric polynomials</h3>

<div class="theorem" id="theorem:Fundamental---theorem---of---symmetric---polynomials" data-name="Fundamental theorem of symmetric polynomials">
	
for every commutative ring $A$,
denote ring of symmetric polynomials in variables $X_1$, &hellip;, $X_n$
with coefficients in $A$
by $A[X_1,\ldots,X_n]^{S_n}$,
which is polynomial ringt in $n$ elementary symmetric polynomials $e_k(X_1,\ldots,X_n)$
for $k=1,\ldots,n$,
then
every symmetric polynomial $P(X_1,\ldots,X_n) \in A[X_1,\ldots,X_n]^{S_n}$
has unique representation

$$

P(X_1, \ldots, X_n) = Q(e_1(X_1,\ldots,X_n), \ldots, e_n(X_1,\ldots,X_n))

$$

for some polynomials $Q\in A[Y_1,\ldots,Y_n]$,
or equivalently,
ring homeomorphism
that sends $Y_k$ to $e_k(X_1,\ldots,X_n)$
for $k=1,\ldots,n$
defines
an isomorphism between
$A[Y_1,\ldots,Y_n]$
and
$A[X_1,\ldots,X_n]^{S_n}$

</div>

<h2 id="title-page:Duality">Duality</h2>


<h3 id="my-foilhead-16">Dualities</h3>

<ul>
<li>
	duality
	<ul>
	<li>
		&ldquo;very pervasive and important concept in (modern) mathematics''

	</li>
	<li>
		&ldquo;important general theme having manifestations in almost every area of mathematics''

	</li>
	</ul>

</li>
<li>
	dualities appear in many places in mathematics, <i>e.g.</i>
	<ul>
	<li>
		<i>dual</i> of normed space
is space of bounded linear functionals on the space
(page~<a href="#page:Dual-of-normed-spaces">here</a>)

	</li>
	<li>
		<i>dual</i> cones and <i>dual</i> norms are defined
(<a href="#definition:dual---cones"></a> &amp; <a href="#definition:dual---norms"></a>)

	</li>
	<li>
		can define <i>dual</i> generalized inequalities using dual cones
(<a href="#proposition:generalized---inequalities---and---dual---generalized---inequalities"></a>)

	</li>
	<li>
		can find necessary and sufficient conditions for $K$-convexity
using <i>dual</i> generalized inequalities
(<a href="#proposition:dual---characterization---of---$K$-convexity"></a>)

	</li>
	<li>
		duality can be observed even in fundamental theorem for Galois theory,
<i>i.e.</i>, $G(K/E) \leftrightarrow E$ &amp; $H \leftrightarrow K^H$
(<a href="#theorem:fundamental---theorem---for---Galois---theory"></a>)

	</li>
	<li>
		exist <i>dualities</i> in continuous / discrete functions in time domain
and continuous / discrete functions in frequency domain,
<i>i.e.</i>,
as in Fourier Transformation

	</li>
	</ul>

</li>
</ul>



<ul>
<li>
	However,
never fascinated more
than <a href="#title-page:Duality">duality appearing in optimization</a>,
<i>e.g.</i>,
	<ul>
	<li>
		properties such as weak duality (<a href="#definition:weak---duality"></a>)
and strong duality (<a href="#definition:strong---duality"></a>)

	</li>
	<li>
		dual problem provides some bound for the optimal value of the original problem,
hence certificate of suboptimality!

	</li>
	<li>
		constraint qualifications such as Slater's condition (<a href="#theorem:Slater's---theorem"></a>)
guarantee strong duality!

	</li>
	</ul>

</li>
</ul>


