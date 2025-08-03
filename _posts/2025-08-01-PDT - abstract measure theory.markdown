---
title: Abstract Measure Theory
date: Fri Aug  1 05:00:00 PDT 2025
last_modified_at: Sun Aug  3 05:49:27 PDT 2025
permalink: /math/rig/abstract-measure-theory
categories:
- blog
tags:
- math
- abstract measure theory
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

# Introduction

## Preamble










<h3>Notations</h3>


<ul>
<li>
	sets of numbers
	<ul>
	<li>
		$\naturals$ - set of natural numbers



	</li>
	<li>
		$\integers$ - set of integers



	</li>
	<li>
		$\integers_+$ - set of nonnegative integers

	</li>
	<li>
		$\rationals$ - set of rational numbers



	</li>
	<li>
		$\reals$ - set of real numbers



	</li>
	<li>
		$\preals$ - set of nonnegative real numbers

	</li>
	<li>
		$\ppreals$ - set of positive real numbers

	</li>
	<li>
		$\complexes$ - set of complex numbers



	</li>
	</ul>

</li>
<li>
	sequences $\seq{x_i}$ and the like

	<ul>
	<li>
		finite $\seq{x_i}_{i=1}^n$, infinite $\seq{x_i}_{i=1}^\infty$ - use $\seq{x_i}$ whenever unambiguously understood





	</li>
	<li>
		similarly for other operations, <i>e.g.</i>, $\sum x_i$, $\prod x_i$, $\cup A_i$, $\cap A_i$, $\bigtimes A_i$

	</li>
	<li>
		similarly for integrals, <i>e.g.</i>, $\int f$ for $\int_{-\infty}^\infty f$

	</li>
	</ul>

</li>
<li>
	sets
	<ul>
	<li>
		$\compl{A}$ - complement of $A$



	</li>
	<li>
		$A\sim B$ - $A\cap \compl{B}$



	</li>
	<li>
		$A\Delta B$ - $(A\cap \compl{B}) \cup (\compl{A} \cap B)$

	</li>
	<li>
		$\powerset(A)$ - set of all subsets of $A$

	</li>
	</ul>

</li>
<li>
	sets in metric vector spaces
	<ul>
	<li>
		$\closure{A}$ - closure of set $A$



	</li>
	<li>
		$\interior{A}$ - interior of set $A$



	</li>
	<li>
		$\relint A$ - relative interior of set $A$



	</li>
	<li>
		$\boundary A$ - boundary of set $A$



	</li>
	</ul>

</li>
<li>
	set algebra
	<ul>
	<li>
		$\sigma(\subsetset{A})$ - $\sigma$-algebra generated by $\subsetset{A}$,
<i>i.e.</i>, smallest $\sigma$-algebra containing $\subsetset{A}$


	</li>
	</ul>

</li>
<li>
	norms in $\reals^n$


	<ul>
	<li>
		$\|x\|_p$ ($p\geq1$) - $p$-norm of $x\in\reals^n$, <i>i.e.</i>, $(|x_1|^p + \cdots + |x_n|^p)^{1/p}$

	</li>
	<li>
		<i>e.g.</i>, $\|x\|_2$ - Euclidean norm

	</li>
	</ul>

</li>
<li>
	matrices and vectors
	<ul>
	<li>
		$a_{i}$ - $i$-th entry of vector $a$

	</li>
	<li>
		$A_{ij}$ - entry of matrix $A$ at position $(i,j)$,
<i>i.e.</i>, entry in $i$-th row and $j$-th column

	</li>
	<li>
		$\Tr(A)$ - trace of $A \in\reals^{n\times n}$,
<i>i.e.</i>, $A_{1,1}+ \cdots + A_{n,n}$



	</li>
	</ul>

</li>
<li>
	symmetric, positive definite, and positive semi-definite matrices
	<ul>
	<li>
		$\symset{n}\subset \reals^{n\times n}$ - set of symmetric matrices



	</li>
	<li>
		$\possemidefset{n}\subset \symset{n}$ - set of positive semi-definite matrices;
$A\succeq0 \Leftrightarrow A \in \possemidefset{n}$



	</li>
	<li>
		$\posdefset{n}\subset \symset{n}$ - set of positive definite matrices;
$A\succ0 \Leftrightarrow A \in \posdefset{n}$



	</li>
	</ul>

</li>
<li>
	sometimes,
use Python script-like notations
(with serious abuse of mathematical notations)
	<ul>
	<li>
		use $f:\reals\to\reals$ as if it were $f:\reals^n \to \reals^n$,
<i>e.g.</i>,

$$
\exp(x) = (\exp(x_1), \ldots, \exp(x_n)) \quad \mbox{for } x\in\reals^n
$$

and

$$
\log(x) = (\log(x_1), \ldots, \log(x_n)) \quad \mbox{for } x\in\ppreals^n
$$

which corresponds to Python code <code>numpy.exp(x)</code> or <code>numpy.log(x)</code>
where <code>x</code> is instance of <code>numpy.ndarray</code>, <i>i.e.</i>, <code>numpy</code> array

	</li>
	<li>
		use $\sum x$ to mean $\ones^T x$ for $x\in\reals^n$,
<i>i.e.</i>

$$
\sum x = x_1 + \cdots + x_n
$$

which corresponds to Python code <code>x.sum()</code>
where <code>x</code> is <code>numpy</code> array

	</li>
	<li>
		use $x/y$ for $x,y\in\reals^n$ to mean

$$
\rowvecthree{x_1/y_1}{\cdots}{x_n/y_n}^T
$$

which corresponds to Python code <code>x / y</code>
where <code>x</code> and <code>y</code> are $1$-d <code>numpy</code> arrays

	</li>
	<li>
		use $X/Y$ for $X,Y\in\reals^{m\times n}$ to mean

$$
\begin{my-matrix}{cccc}
X_{1,1}/Y_{1,1} & X_{1,2}/Y_{1,2} & \cdots & X_{1,n}/Y_{1,n}
\\
X_{2,1}/Y_{2,1} & X_{2,2}/Y_{2,2} & \cdots & X_{2,n}/Y_{2,n}
\\
\vdots & \vdots & \ddots & \vdots
\\
X_{m,1}/Y_{m,1} & X_{m,2}/Y_{m,2} & \cdots & X_{m,n}/Y_{m,n}
\end{my-matrix}
$$

which corresponds to Python code <code>X / Y</code>
where <code>X</code> and <code>Y</code> are $2$-d <code>numpy</code> arrays

	</li>
	</ul>

</li>
</ul>


<h3>Some definitions</h3>


<div class="definition" id="definition:infinitely often - i.o." data-name="infinitely often - i.o.">
	


statement $P_n$, said to happen <span class="define">infinitely often</span> or <span class="define">i.o.</span> if

$$
\left(
\forall N\in\naturals
\right)
\left(
\exists n > N
\right)
\left(
P_n
\right)
$$


</div>

<div class="definition" id="definition:almost everywhere - a.e." data-name="almost everywhere - a.e.">
	




statement $P(x)$,
said to happen <span class="define">almost everywhere</span> or <span class="define">a.e.</span> or <span class="define">almost surely</span> or <span class="define">a.s.</span>
(depending on context)
associated with
measure space $\meas{X}{\algB}{\mu}$
if

$$
\mu \set{x}{P(x)} = 1
$$

or equivalently

$$
\mu \set{x}{\sim P(x)} = 0
$$


</div>


<h3>Some conventions</h3>


<ul>
<li>
	(for some subjects) use following conventions
	<ul>
	<li>
		$0\cdot \infty = \infty \cdot 0 = 0$

	</li>
	<li>
		$(\forall x\in\ppreals)(x\cdot \infty = \infty \cdot x = \infty)$

	</li>
	<li>
		$\infty \cdot \infty = \infty$

	</li>
	</ul>

</li>
</ul>


<h1 id="Real-Analysis">Real Analysis</h1>



<h2 id="set-theory">Set Theory</h2>


<h3>Some principles</h3>

<div class="principle" id="principle:principle of mathematical induction" data-name="principle of mathematical induction">
	

$$
P(1) \& [P(n\Rightarrow P(n+1)] \Rightarrow (\forall n \in \naturals)P(n)
$$


</div>

<div class="principle" id="principle:well ordering principle" data-name="well ordering principle">
	

each nonempty subset of $\naturals$ has a smallest element

</div>

<div class="principle" id="principle:principle of recursive definition" data-name="principle of recursive definition">
	
for $f:X\to X$ and $a\in X$,
exists unique infinite sequence $\langle x_n\rangle_{n=1}^\infty\subset X$
such that

$$
x_1=a
$$

and

$$
\left(
\forall n \in \naturals
\right)
\left(
x_{n+1} = f(x_n)
\right)
$$


</div>
<ul>
<li>
	note that
<a href="#principle:principle of mathematical induction"></a>
$\Leftrightarrow$
<a href="#principle:well-ordering principle - smallest element"></a>
$\Rightarrow$
<a href="#principle:principle of recursive definition"></a>

</li>
</ul>

<h3>Some definitions for functions</h3>

<div class="definition" id="definition:functions" data-name="functions">
	
for $f:X\to Y$
	<ul>
	<li>
		terms, <span class="define">map</span> and <span class="define">function</span>, exterchangeably used



	</li>
	<li>
		$X$ and $Y$, called <span class="define">domain of $f$</span> and <span class="define">codomain of $f$</span> respectively





	</li>
	<li>
		$\set{f(x)}{x\in X}$, called <span class="define">range of $f$</span>



	</li>
	<li>
		for $Z\subset Y$, $f^{-1}(Z) = \set{x\in X}{f(x)\in Z}\subset X$, called <span class="define">preimage</span> or <span class="define">inverse image of $Z$ under $f$</span>





	</li>
	<li>
		for $y\in Y$, $f^{-1}(\{y\})$, called <span class="define">fiber of $f$ over $y$</span>



	</li>
	<li>
		$f$, called <span class="define">injective</span> or <span class="define">injection</span> or <span class="define">one-to-one</span>
if $\left( \forall x\neq v \in X \right) \left( f(x) \neq f(v) \right)$







	</li>
	<li>
		$f$, called <span class="define">surjective</span> or <span class="define">surjection</span> or <span class="define">onto</span>
if $\left( \forall x \in X \right) \left( \exists y in Y \right) (y=f(x))$







	</li>
	<li>
		$f$, called <span class="define">bijective</span> or <span class="define">bijection</span> if $f$ is both injective and surjective,
in which case, $X$ and $Y$, said to be <span class="define">one-to-one correspondece</span> or <span class="define">bijective correspondece</span>









	</li>
	<li>
		$g:Y\to X$, called <span class="define">left inverse</span> if $g\circ f$ is identity function



	</li>
	<li>
		$h:Y\to X$, called <span class="define">right inverse</span> if $f\circ h$ is identity function



	</li>
	</ul>

</div>

<h3>Some properties of functions</h3>

<div class="lemma" id="lemma:functions" data-name="functions">
	
for $f:X\to Y$
	<ul>
	<li>
		$f$ is injective if and only if $f$ has left inverse

	</li>
	<li>
		$f$ is surjective if and only if $f$ has right inverse

	</li>
	<li>
		hence, $f$ is bijective if and only if $f$ has both left and right inverse
because if $g$ and $h$ are left and right inverses respectively,
$g = g \circ (f\circ h) = (g\circ f)\circ h = h$

	</li>
	<li>
		if $|X|=|Y|<\infty$,
$f$ is injective
if and only if
$f$ is surjective
if and only if
$f$ is bijective

	</li>
	</ul>

</div>

<h3>Countability of sets</h3>

<ul>
<li>
	set $A$ is countable if range of some function whose domain is $\naturals$

</li>
<li>
	$\naturals$, $\integers$, $\rationals$: countable

</li>
<li>
	$\reals$: <i>not</i> countable

</li>
</ul>

<h3>Limit sets</h3>

<ul>
<li>
	for sequence, $\seq{A_n}$, of subsets of $X$
	<ul>
	<li>
		<span class="define">limit superior or limsup of \seq{A_n}</span>, defined by



$$
\limsup \seq{A_n} = \bigcap_{n=1}^\infty \bigcup_{m=n}^\infty A_m
$$


	</li>
	<li>
		<span class="define">limit inferior or liminf of \seq{A_n}</span>, defined by



$$
\liminf \seq{A_n} = \bigcup_{n=1}^\infty \bigcap_{m=n}^\infty A_m
$$


	</li>
	</ul>

</li>
<li>
	always

$$
\liminf \seq{A_n} \subset
\limsup \seq{A_n}
$$


</li>
<li>
	when $\liminf \seq{A_n} = \limsup \seq{A_n}$, sequence, $\seq{A_n}$,
said to <span class="define">converge to it</span>, denote



$$
\lim \seq{A_n} = \liminf \seq{A_n} = \limsup \seq{A_n} = A
$$


</li>
</ul>

<h3>Algebras of sets</h3>

<ul>
<li>
	collection $\alg$ of subsets of $X$ called <span class="define">algebra</span> or <span class="define">Boolean algebra</span> if



$$
(\forall A, B \in \alg) (A\cup B\in\alg)
\mbox{ and }
(\forall A \in \alg) (\compl{A}\in\alg)
$$

	<ul>
	<li>
		$(\forall A_1, \ldots, A_n \in \alg)(\cup_{i=1}^n A_i \in \alg)$

	</li>
	<li>
		$(\forall A_1, \ldots, A_n \in \alg)(\cap_{i=1}^n A_i \in \alg)$

	</li>
	</ul>

</li>
<li>
	algebra $\alg$ called <span class="define">$\sigma$-algebra</span> or <span class="define">Borel field</span> if



	<ul>
	<li>
		every union of a countable collection of sets in $\alg$ is in $\alg$, <i>i.e.</i>,

$$
(\forall \seq{A_i})(\cup_{i=1}^\infty A_i \in \alg)
$$


	</li>
	</ul>

</li>
<li>
	given sequence of sets in algebra $\alg$, $\seq{A_i}$, exists disjoint sequence, $\seq{B_i}$ such that

$$
B_i \subset A_i \mbox{ and }
\bigcup_{i=1}^\infty B_i = \bigcup_{i=1}^\infty A_i
$$


</li>
</ul>

<h3>Algebras generated by subsets</h3>

<ul>
<li>
	<span class="define">algebra generated by</span> collection of subsets of $X$, $\coll$, can be found by




$$
\alg =
\bigcap \set{\algk{B}}{\algk{B} \in \collF}
$$

where $\collF$ is family of all algebras containing $\coll$
	<ul>
	<li>
		smallest algebra $\alg$ containing $\coll$, <i>i.e.</i>,



$$
(\forall \algk{B} \in \collF)(\alg \subset \algk{B})
$$


	</li>
	</ul>

</li>
<li>
	<span class="define">$\sigma$-algebra generated by</span> collection of subsets of $X$, $\coll$, can be found by



$$
\alg=
\bigcap \set{\algk{B}}{\algk{B} \in \collG}
$$

where $\collG$ is family of all $\sigma$-algebras containing $\coll$
	<ul>
	<li>
		smallest $\sigma$-algebra $\alg$ containing $\coll$, <i>i.e.</i>,



$$
(\forall \algk{B} \in \collG)(\alg \subset \algk{B})
$$


	</li>
	</ul>

</li>
</ul>

<h3>Relation</h3>

<ul>
<li>
	$x$ said to <span class="define">stand in relation</span> $\rel$ to $y$,
denoted by $\relxy{x}{y}$

</li>
<li>
	$\rel$ said to <span class="define">be relation on</span> $X$ if $\relxy{x}{y}$ $\Rightarrow$ $x\in X$ and $y\in X$


</li>
<li>
	$\rel$ is
	<ul>
	<li>
		transitive if $\relxy{x}{y}$ and $\relxy{y}{z}$ $\Rightarrow$ $\relxy{x}{z}$

	</li>
	<li>
		symmetric if $\relxy{x}{y} = \relxy{y}{x}$

	</li>
	<li>
		reflexive if $\relxy{x}{x}$

	</li>
	<li>
		antisymmetric if $\relxy{x}{y}$ and $\relxy{y}{x}$ $\Rightarrow$ $x=y$

	</li>
	</ul>

</li>
<li>
	$\rel$ is
	<ul>
	<li>
		<span class="define">equivalence relation</span> if transitive, symmetric, and reflexive, <i>e.g.</i>, modulo


	</li>
	<li>
		<span class="define">partial ordering</span> if transitive and antisymmetric, <i>e.g.</i>, &ldquo;$\subset$''



	</li>
	<li>
		<span class="define">linear (or simple) ordering</span> if transitive, antisymmetric, and $\relxy{x}{y}$ or $\relxy{y}{x}$ for all $x,y\in X$




		<ul>
		<li>
			<i>e.g.</i>, &ldquo;$\geq$'' linearly orders $\reals$ while &ldquo;$\subset$'' does not $\powerset(X)$

		</li>
		</ul>

	</li>
	</ul>

</li>
</ul>

<h3>Ordering</h3>

<ul>
<li>
	given partial order, $\prec$, $a$ is
	<ul>
	<li>
		a first/smallest/least element if $x \neq a \Rightarrow a\prec x$

	</li>
	<li>
		a last/largest/greatest element if $x \neq a \Rightarrow x\prec a$

	</li>
	<li>
		a minimal element if $x \neq a \Rightarrow x \not\prec a$

	</li>
	<li>
		a maximal element if $x \neq a \Rightarrow a \not\prec x$

	</li>
	</ul>

</li>
<li>
	partial ordering $\prec$ is
	<ul>
	<li>
		strict partial ordering if $x\not\prec x$

	</li>
	<li>
		reflexive partial ordering if $x\prec x$

	</li>
	</ul>

</li>
<li>
	strict linear ordering $<$ is
	<ul>
	<li>
		<span class="define">well ordering</span> for $X$ if every nonempty set contains a first element

	</li>
	</ul>

</li>
</ul>

<h3>Axiom of choice and equivalent principles</h3>

<div class="axiom" id="axiom:axiom of choice" data-name="axiom of choice">
	
given a collection of nonempty sets, $\coll$,
there exists $f:\coll\ \to \cup_{A\in\coll} A$ such that

$$
\left(
\forall A\in\coll\
\right)
\left(
f(A) \in A
\right)
$$


</div>
<ul>
<li>
	
also called <span class="define">multiplicative axiom</span>


- preferred to be called to axiom of choice by Bertrand Russell
for reason writte 

</li>
<li>
	
no problem when $\coll$ is finite

</li>
<li>
	
need axiom of choice when $\coll$ is not finite

</li>
</ul>

<div class="principle" id="principle:Hausdorff maximal principle" data-name="Hausdorff maximal principle">
	

for particial ordering $\prec$ on $X$,
exists a maximal linearly ordered subset $S\subset X$,
<i>i.e.</i>,
$S$ is linearity ordered by $\prec$
and if $S\subset T\subset X$ and $T$ is linearly ordered by $\prec$,
$S=T$

</div>

<div class="principle" id="principle:well-ordering principle" data-name="well-ordering principle">
	
every set $X$ can be well ordered,
<i>i.e.</i>,
there is a relation $<$ that well orders $X$

</div>
<ul>
<li>
	note that
<a href="#axiom:axiom of choice"></a>
$\Leftrightarrow$
<a href="#principle:Hausdorff maximal principle"></a>
$\Leftrightarrow$
<a href="#principle:well-ordering principle"></a>

</li>
</ul>

<h3>Infinite direct product</h3>

<div class="definition" id="definition:direct product" data-name="direct product">
	
for collection of sets, $\seq{X_\lambda}$, with index set, $\Lambda$,

$$
\bigtimes_{\lambda\in\Lambda} X_\lambda
$$

called <span class="define">direct product</span>
	<ul>
	<li>
		
for $z=\seq{x_\lambda}\in\bigtimes X_\lambda$,
$x_\lambda$ called <span class="define">$\lambda$-th coordinate of $z$</span>

	</li>
	</ul>

</div>
<ul>
<li>
	if one of $X_\lambda$ is empty, $\bigtimes X_\lambda$ is empty

</li>
<li>
	<i>axiom of choice</i> is equivalent to converse, <i>i.e.</i>,
if none of $X_\lambda$ is empty, $\bigtimes X_\lambda$ is not empty
if one of $X_\lambda$ is empty, $\bigtimes X_\lambda$ is empty

</li>
<li>
	this is why Bertrand Russell prefers <i>multiplicative axiom</i> to <i>axiom of choice</i> for name of axiom (<a href="#axiom:axiom of choice"></a>)



</li>
</ul>

<h2 id="real-number-system">Real Number System</h2>


<h3>Field axioms</h3>

<ul>
<li>
	field axioms - for every $x,y,z\in\field$
	<ul>
	<li>
		$(x+y)+z= x+(y+z)$ - additive associativity

	</li>
	<li>
		$(\exists 0\in\field)(\forall x\in\field)(x+0=x)$ - additive identity

	</li>
	<li>
		$(\forall x\in\field)(\exists w\in\field)(x+w=0)$ - additive inverse

	</li>
	<li>
		$x+y= y+x$ - additive commutativity

	</li>
	<li>
		$(xy)z= x(yz)$ - multiplicative associativity

	</li>
	<li>
		$(\exists 1\neq0\in\field)(\forall x\in\field)(x\cdot 1=x)$ - multiplicative identity

	</li>
	<li>
		$(\forall x\neq0\in\field)(\exists w\in\field)(xw=1)$ - multiplicative inverse

	</li>
	<li>
		$x(y+z) = xy + xz$ - distributivity

	</li>
	<li>
		$xy= yx$ - multiplicative commutativity

	</li>
	</ul>

</li>
<li>
	system (set with $+$ and $\cdot$) satisfying axiom of field called <span class="define">field</span>
	<ul>
	<li>
		<i>e.g.</i>, field of module $p$ where $p$ is prime, $\primefield{p}$

	</li>
	</ul>

</li>
</ul>

<h3>Axioms of order</h3>

<ul>
<li>
	axioms of order - subset, $\field_{++}\subset \field$, of positive (real) numbers satisfies
	<ul>
	<li>
		$x,y\in \field_{++} \Rightarrow x+y\in \field_{++}$

	</li>
	<li>
		$x,y\in \field_{++} \Rightarrow xy\in \field_{++}$

	</li>
	<li>
		$x\in \field_{++} \Rightarrow -x\not\in \field_{++}$

	</li>
	<li>
		$x\in \field \Rightarrow x=0\lor x\in \field_{++} \lor -x \in \field_{++}$

	</li>
	</ul>

</li>
<li>
	system satisfying field axioms &amp; axioms of order called <span class="define">ordered field</span>
	<ul>
	<li>
		<i>e.g.</i>, set of real numbers ($\reals$), set of rational numbers ($\rationals$)

	</li>
	</ul>

</li>
</ul>

<h3>Axiom of completeness</h3>

<ul>
<li>
	completeness axiom
	<ul>
	<li>
		every nonempty set $S$ of real numbers which has an upper bound has a least upper bound,
<i>i.e.</i>,

$$
\set{l}{(\forall x\in S)(l\leq x)}
$$

has least element.

	</li>
	<li>
		use $\inf S$ and $\sup S$ for least and greatest element (when exist)

	</li>
	</ul>

</li>
<li>
	ordered field that is complete is <span class="define">complete ordered field</span>

	<ul>
	<li>
		<i>e.g.</i>, $\reals$ (with $+$ and $\cdot$)

	</li>
	</ul>

</li>
<li>
	 axiom of Archimedes
	<ul>
	<li>
		given any $x\in\reals$, there is an integer $n$ such that $x<n$

	</li>
	</ul>

</li>
<li>
	 corollary
	<ul>
	<li>
		given any $x<y \in \reals$, exists $r\in\rationals$ such tat
$x < r < y$

	</li>
	</ul>

</li>
</ul>

<h3>Sequences of $\reals$</h3>

<ul>
<li>
	sequence of $\reals$ denoted by $\seq{x_i}_{i=1}^\infty$ or $\seq{x_i}$
	<ul>
	<li>
		mapping from $\naturals$ to $\reals$

	</li>
	</ul>

</li>
<li>
	limit of $\seq{x_n}$ denoted by $\lim_{n\to\infty} x_n$ or $\lim x_n$ - defined by $a\in\reals$

$$
(\forall \epsilon>0)(\exists N\in\naturals) (n \geq N \Rightarrow |x_n-a|<\epsilon)
$$

	<ul>
	<li>
		$\lim x_n$ unique if exists

	</li>
	</ul>

</li>
<li>
	$\seq{x_n}$ called Cauchy sequence if

$$
(\forall \epsilon>0)(\exists N\in\naturals) (n,m \geq N \Rightarrow |x_n-x_m|<\epsilon)
$$


</li>
<li>
	Cauchy criterion - characterizing complete metric space (including $\reals$)

	<ul>
	<li>
		sequence converges if and only if Cauchy sequence

	</li>
	</ul>

</li>
</ul>

<h3>Other limits</h3>

<ul>
<li>
	cluster point of $\seq{x_n}$ - defined by $c\in\reals$

$$
(\forall \epsilon>0, N\in\naturals)(\exists n>N)(|x_n-c|<\epsilon)
$$


</li>
<li>
	limit superior or limsup of $\seq{x_n}$

$$
\limsup x_n = \inf_n \sup_{k>n} x_k
$$


</li>
<li>
	limit inferior or liminf of $\seq{x_n}$

$$
\liminf x_n = \sup_n \inf_{k>n} x_k
$$


</li>
<li>
	$\liminf x_n \leq \limsup x_n$

</li>
<li>
	$\seq{x_n}$ converges if and only if $\liminf x_n = \limsup x_n$ (=$\lim x_n$)

</li>
</ul>

<h3>Open and closed sets</h3>

<ul>
<li>
	$O$ called <span class="define">open</span> if

$$
(\forall x\in O)(\exists \delta>0)(y\in\reals)(|y-x|<\delta\Rightarrow y\in O)
$$

	<ul>
	<li>
		intersection of finite collection of open sets is open

	</li>
	<li>
		union of any collection of open sets is open

	</li>
	</ul>

</li>
<li>
	$\closure{E}$ called <span class="define">closure</span> of $E$ if

$$
(\forall x \in \closure{E} \ \&\ \delta>0)(\exists y\in E)(|x-y|<\delta)
$$


</li>
<li>
	$F$ called <span class="define">closed</span> if

$$
F = \closure{F}
$$

	<ul>
	<li>
		union of finite collection of closed sets is closed

	</li>
	<li>
		intersection of any collection of closed sets is closed

	</li>
	</ul>

</li>
</ul>

<h3>Open and closed sets - facts</h3>


<ul>
<li>
	<span class="fact-font">every open set is union of countable collection of disjoint open intervals</span>



</li>
<li>
	(Lindelo&#776;f) any collection $\coll$ of open sets has a countable subcollection $\seq{O_i}$ such that

$$
\bigcup_{O\in\coll} O = \bigcup_{i} O_i
$$

	<ul>
	<li>
		equivalently,
any collection $\collk{F}$ of closed sets has a countable subcollection $\seq{F_i}$ such that

$$
\bigcap_{O\in\collk{F}} F = \bigcap_{i} F_i
$$


	</li>
	</ul>

</li>
</ul>

<h3>Covering and Heine-Borel theorem</h3>


<ul>
<li>
	collection $\coll$ of sets called <span class="define">covering</span> of $A$ if

$$
A \subset \bigcup_{O\in\coll} O
$$

	<ul>
	<li>
		$\coll$ said to <span class="define">cover</span> $A$

	</li>
	<li>
		$\coll$ called <span class="define">open covering</span> if every $O\in\coll$ is open

	</li>
	<li>
		$\coll$ called <span class="define">finite covering</span> if $\coll$ is finite

	</li>
	</ul>

</li>
<li>
	<span class="name-font">Heine-Borel theorem\index{Heine-Borel theorem}\index{Heine, Heinrich Eduard!Heine-Borel theorem}\index{Borel, Fe&#769;lix E&#769;douard Justin E&#769;mile!Heine-Borel theorem} -</span>
for any closed and bounded set, every open covering has finite subcovering

</li>
<li>
	corollary
	<ul>
	<li>
		any collection $\coll$ of closed sets including at least one bounded set every finite subcollection of which has nonempty intersection
has nonempty intersection.

	</li>
	</ul>

</li>
</ul>

<h3>Continuous functions</h3>

<ul>
<li>
	$f$ (with domain $D$) called <span class="define">continuous at</span> $x$ if

$$
(\forall\epsilon >0)(\exists \delta>0)(\forall y\in D)(|y-x|<\delta \Rightarrow |f(y)-f(x)|<\epsilon)
$$


</li>
<li>
	$f$ called <span class="define">continuous on</span> $A\subset D$ if $f$ is continuous at every point in $A$

</li>
<li>
	$f$ called <span class="define">uniformly continuous on</span> $A\subset D$ if

$$
(\forall\epsilon >0)(\exists \delta>0)(\forall x,y\in D)(|x-y|<\delta \Rightarrow |f(x)-f(y)|<\epsilon)
$$


</li>
</ul>

<h3>Continuous functions - facts</h3>

<ul>
<li>
	$f$ is continuous if and only if for every open set $O$ (in co-domain), $f^{-1}(O)$ is open

</li>
<li>
	$f$ continuous on closed and bounded set is uniformly continuous

</li>
<li>
	<span class="name-font">extreme value theorem -</span>
$f$ continuous on closed and bounded set, $F$, is <i>bounded on $F$ and assumes its maximum and minimum on $F$</i>

$$
(\exists x_1, x_2 \in F)(\forall x\in F)(f(x_1) \leq f(x) \leq f(x_2))
$$


</li>
<li>
	<span class="name-font">intermediate value theorem -</span>
for $f$ continuous on $[a,b]$ with $f(a) \leq f(b)$,

$$
(\forall d)(f(a) \leq d \leq f(b))(\exists c\in[a,b])(f(c) = d)
$$


</li>
</ul>

<h3>Borel sets and Borel $\sigma$-algebra</h3>


<ul>
<li>
	<span class="define">Borel set</span>

	<ul>
	<li>
		any set that can be formed from open sets (or, equivalently, from closed sets)
through the operations of countable union, countable intersection, and relative complement

	</li>
	</ul>

</li>
<li>
	<span class="define">Borel algebra</span> or <span class="define">Borel $\sigma$-algebra</span>

	<ul>
	<li>
		<i>smallest $\sigma$-algebra containing all open sets</i>

	</li>
	<li>
		also
		<ul>
		<li>
			 smallest $\sigma$-algebra containing all closed sets

		</li>
		<li>
			 smallest $\sigma$-algebra containing all open intervals
(due to statement on page~)

		</li>
		</ul>

	</li>
	</ul>

</li>
</ul>


<h3>Various Borel sets</h3>

<ul>
<li>
	countable union of closed sets (in $\reals$),
called <span class="define">an $F_\sigma$</span> ($F$ for closed &amp; $\sigma$ for sum)

	<ul>
	<li>
		thus, every countable set,
every closed set,
every open interval,
every open sets,
is an $F_\sigma$ (note $(a,b)=\bigcup_{n=1}^\infty [a+1/n,b-1/n]$)

	</li>
	<li>
		countable union of sets in $F_\sigma$ again is an $F_\sigma$

	</li>
	</ul>

</li>
<li>
	countable intersection of open sets
called <span class="define">a $G_\delta$</span> ($G$ for open &amp; $\delta$ for durchschnitt - average in German)

	<ul>
	<li>
		complement of $F_\sigma$ is a $G_\delta$ and vice versa

	</li>
	</ul>

</li>
<li>
	$F_\sigma$ and $G_\delta$ are simple types of Borel sets

</li>
<li>
	countable intersection of $F_\sigma$'s is $F_{\sigma\delta}$,
countable union of $F_{\sigma\delta}$'s is $F_{\sigma\delta\sigma}$,
countable intersection of $F_{\sigma\delta\sigma}$'s is $F_{\sigma\delta\sigma\delta}$, <i>etc.</i>,
&amp; likewise for $G_{\delta \sigma \ldots}$



</li>
<li>
	below are all classes of Borel sets, but not every Borel set belongs to one of these classes

$$
F_{\sigma},
F_{\sigma\delta},
F_{\sigma\delta\sigma},
F_{\sigma\delta\sigma\delta},
\ldots,
G_{\delta},
G_{\delta\sigma},
G_{\delta\sigma\delta},
G_{\delta\sigma\delta\sigma},
\ldots,
$$


</li>
</ul>

<h2 id="Measure-and-Integration">Measure and Integration</h2>


<h3>Purpose of integration theory</h3>

<ul>
<li>
	purpose of &ldquo;measure and integration'' slides
	<ul>
	<li>
		abstract (out) most important properties of Lebesgue measure and Lebesgue integration

	</li>
	</ul>

</li>
<li>
	provide certain <i>axioms that Lebesgue measure satisfies</i>

</li>
<li>
	base our integration theory on these axioms

</li>
<li>
	hence, our theory valid for every system satisfying the axioms

</li>
</ul>

<h3>Measurable space, measure, and measure space</h3>

<ul>
<li>
	family of subsets containing $\emptyset$
closed under countable union and completement,
called <span class="define">$\sigma$-algebra</span>

</li>
<li>
	mapping of sets to extended real numbers,
called <span class="define">set function</span>

</li>
<li>
	$\measu{X}{\algk{B}}$ with set, $X$, and $\sigma$-algebra of $X$, $\algk{B}$,
called <span class="define">measurable space</span>



	<ul>
	<li>
		$A\in\algk{B}$, said to be <span class="define">measurable (with respect to \algk{B})</span>


	</li>
	</ul>

</li>
<li>
	nonnegative set function, $\mu$, defined on $\algk{B}$ satisfying
$\mu(\emptyset)=0$ and for every disjoint, $\seq{E_n}_{n=1}^\infty\subset \algk{B}$,

$$
\mu\left(\bigcup E_n\right) = \sum \mu E_n
$$

called <span class="define">measure on</span> measurable space, $\measu{X}{\algk{B}}$




</li>
<li>
	measurable space, $\measu{X}{\algk{B}}$, equipped with measure, $\mu$,
called <span class="define">measure space</span> and denoted by $\meas{X}{\algk{B}}{\mu}$


</li>
</ul>

<h3>Measure space examples</h3>


<ul>
<li>
	$\meas{\reals}{\subsetset{M}}{\mu}$
with Lebesgue measurable sets, $\subsetset{M}$, and Lebesgue measure, $\mu$

</li>
<li>
	$\meast{[0,1]}{\set{A\in\subsetset{M}}{A\subset[0,1]}}{\mu}$
with Lebesgue measurable sets, $\subsetset{M}$, and Lebesgue measure, $\mu$

</li>
<li>
	$\meas{\reals}{\algB}{\mu}$
with class of Borel sets, $\algB$, and Lebesgue measure, $\mu$

</li>
<li>
	$\meas{\reals}{\powerset(\reals)}{\mu_C}$
with set of all subsets of $\reals$, $\powerset(\reals)$, and counting measure, $\mu_C$

</li>
<li>
	interesting (and bizarre) example

	<ul>
	<li>
		$\meas{X}{\collk{A}}{\mu_B}$
with any uncountable set, $X$,
family of either countable or complement of countable set, $\collk{A}$,
and measure, $\mu_B$, such that $\mu_B A =0$ for countable $A\subset X$
and $\mu_B B=1$ for uncountable $B\subset X$

	</li>
	</ul>

</li>
</ul>

<h3>More properties of measures</h3>

<ul>
<li>
	for $A,B\in\algB$ with $A\subset B$

$$
\mu A \leq \mu B
$$


</li>
<li>
	for $\seq{E_n}\subset \algB$ with $\mu E_1 < \infty$ and $E_{n+1} \subset E_n$

$$
\mu\left(\bigcap E_n\right) = \lim \mu E_n
$$


</li>
<li>
	for $\seq{E_n}\subset \algB$

$$
\mu\left(\bigcup E_n\right) \leq \sum \mu E_n
$$


</li>
</ul>

<h3>Finite and $\sigma$-finite measures</h3>

<ul>
<li>
	measure, $\mu$, with $\mu(X)<\infty$,
called <span class="define">finite</span>

</li>
<li>
	measure, $\mu$, with $X=\bigcup X_n$ for some $\seq{X_n}$ and $\mu(X_n)<\infty$,
called <span class="define">$\sigma$-finite</span>
	<ul>
	<li>
		always can take $\seq{X_n}$ with disjoint $X_n$

	</li>
	</ul>

</li>
<li>
	Lebesgue measure on $[0,1]$ is finite

</li>
<li>
	Lebesgue measure on $\reals$ is $\sigma$-finite

</li>
<li>
	countering measure on uncountable set is <i>not</i> $\sigma$-measure

</li>
</ul>


<h3>Sets of finite and $\sigma$-finite measure</h3>

<ul>
<li>
	set, $E\in \algB$, with $\mu E<\infty$,
said to be <span class="define">of finite measure</span>

</li>
<li>
	set that is countable union of measurable sets of finite measure,
said to be <span class="define">of $\sigma$-finite measure</span>

</li>
<li>
	measurable set contained in set of $\sigma$-finite measure,
is of $\sigma$-finite measure

</li>
<li>
	countable union of sets of $\sigma$-finite measure,
is of $\sigma$-finite measure

</li>
<li>
	when $\mu$ is $\sigma$-finite,
every measurable set is of $\sigma$-finite

</li>
</ul>


<h3>Semifinite measures</h3>

<ul>
<li>
	roughly speacking, nearly all familiar properties of Lebesgue measure and Lebesgue integration
hold for arbitrary $\sigma$-finite measure

</li>
<li>
	many treatment of abstract measure theory limit themselves to $\sigma$-finite measures



</li>
<li>
	many parts of general theory, however, do <i>not</i> required
assumption of $\sigma$-finiteness

</li>
<li>
	undesirable to have development unnecessarily restrictive



</li>
<li>
	measure, $\mu$, for which every measurable set of infinite measure
contains measurable sets of arbitrarily large finite measure,
said to be <span class="define">semifinite</span>


</li>
<li>
	every $\sigma$-finite measure is semifinite measure
while measure, $\mu_B$, on page~
is not

</li>
</ul>


<h3>Complete measure spaces</h3>

<ul>
<li>
	measure space, $\meas{X}{\algB}{\mu}$, for which $\algB$ contains all subsets of sets of measure zero,
said to be <span class="define">complete</span>,




<i>i.e.</i>,

$$
(\forall B\in\algB \mbox{ with } \mu B=0)
(A \subset B \Rightarrow A \in \algB)
$$

	<ul>
	<li>
		<i>e.g.</i>, Lebesgue measure is complete, but Lebesgue measure restricted to $\sigma$-algebra of Borel sets
is <i>not</i>

	</li>
	</ul>

</li>
<li>
	every measure space can be <i>completed</i> by addition of subsets of sets of measure zero


</li>
<li>
	for $\meas{X}{\algB}{\mu}$, can find <i>complete</i> measure space $\meas{X}{\algB_0}{\mu_0}$
such that

$$
\begin{eqnarray*}
&-&
\algB \subset \algB_0
\\
&-&
E \in\algB \Rightarrow \mu E = \mu_0 E
\\
&-&
E \in\algB_0 \Leftrightarrow E = A \cup B
\mbox{ where } B,C\in\algB, \mu C = 0, A\subset C
\end{eqnarray*}
$$

	<ul>
	<li>
		$\meas{X}{\algB_0}{\mu_0}$ called <span class="define">completion</span> of $\meas{X}{\algB}{\mu}$


	</li>
	</ul>

</li>
</ul>

<h3>Local measurability and saturatedness</h3>

<ul>
<li>
	for $\meas{X}{\algB}{\mu}$,
$E\subset X$ for which $(\forall B\in\algB \mbox{ with }\mu B < \infty)(E\cap B\in\algB)$,
said to be <span class="define">locally measurable</span>


</li>
<li>
	collection, $\algC$, of all locally measurable sets
is $\sigma$-algebra containing $\algB$

</li>
<li>
	measure for which every locally measurable set is measurable,
said to be <span class="define">saturated</span>


</li>
<li>
	every $\sigma$-finite measure is saturated

</li>
<li>
	measure can be extended to saturated measure,
but (unlike completion)
extension is not unique
	<ul>
	<li>
		can take $\algC$ as extension for locally measurable sets,
but measure can be extended on $\algC$ in more than one ways

	</li>
	</ul>

</li>
</ul>

<h3>Measurable functions</h3>


<ul>
<li>
	concept and properties of measurable functions in abstract measurable space
almost identical with those of Lebesgue measurable functions
(page~)

</li>
<li>
	theorems and facts are essentially same as those of Lebesgue measurable functions

</li>
<li>
	assume measurable space, $\measu{X}{\algB}$

</li>
<li>
	for $f:X\to\ereals$, following are equivalent
	<ul>
	<li>
		$(\forall a\in\reals) (\set{x\in X}{f(x) < a}\in\algB)$

	</li>
	<li>
		$(\forall a\in\reals) (\set{x\in X}{f(x) \leq a}\in\algB)$

	</li>
	<li>
		$(\forall a\in\reals) (\set{x\in X}{f(x) > a}\in\algB)$

	</li>
	<li>
		$(\forall a\in\reals) (\set{x\in X}{f(x) \geq a}\in\algB)$

	</li>
	</ul>

</li>
<li>
	$f:X\to\ereals$ for which any one of above four statements holds,
called <span class="define">measurable</span> or <span class="define">measurable with respect to \algB</span>



</li>
</ul>

<h3>Properties of measurable functions</h3>



<ul>
<li>
		<div class="theorem" id="theorem:measurability preserving function operations" data-name="measurability preserving function operations">
		
for measurable functions, $f$ and $g$, and $c\in\reals$
		<ul>
		<li>
			$f+c$, $cf$, $f+g$, $fg$, $f\vee g$ are measurable

		</li>
		</ul>

	</div>

</li>
<li>
		<div class="theorem" id="theorem:limits of measurable functions" data-name="limits of measurable functions">
		
for every measurable function sequence, $\seq{f_n}$
		<ul>
		<li>
			$\sup f_n$, $\limsup f_n$, $\inf f_n$, $\liminf f_n$ are measurable

		</li>
		<li>
			thus, $\lim f_n$ is measurable if exists

		</li>
		</ul>

	</div>


</li>
</ul>

<h3>Simple functions and other properties</h3>


<ul>
<li>
	$\varphi$ called <span class="define">simple function</span> if for distinct $\seq{c_i}_{i=1}^n$
and measurable sets, $\seq{E_i}_{i=1}^n$


$$
\varphi(x) = \sum_{i=1}^n c_i \chi_{E_i}(x)
$$



</li>
<li>
	for nonnegative measurable function, $f$,
exists nondecreasing sequence of simple functions, $\seq{\varphi_n}$,
<i>i.e.</i>, $\varphi_{n+1}\geq \varphi_n$
such that for every point in $X$

$$
f = \lim \varphi_n
$$

	<ul>
	<li>
		for $f$ defined on $\sigma$-finite measure space,
we may choose $\seq{\varphi_n}$ so that
every $\varphi_n$ vanishes outside set of finite measure

	</li>
	</ul>

</li>
<li>
	for complete measure, $\mu$,
$f$ measurable and $f=g$ a.e. imply
measurability of $g$

</li>
</ul>

<h3>Define measurable function by ordinate sets</h3>

<ul>
<li>
	$\set{x}{f(x)<\alpha}$ sometimes called <span class="define">ordinate sets</span>

,
which is nondecreasing in $\alpha$

</li>
<li>
	below says when given nondecreasing ordinate sets,
we can find $f$ satisfying

$$
\set{x}{f(x)<\alpha}
\subset
B_\alpha
\subset
\set{x}{f(x)\leq\alpha}
$$


</li>
<li>
	for nondecreasing function, $h:D\to\algB$, for dense set of real numbers, $D$,
<i>i.e.</i>, $B_\alpha \subset B_\beta$ for all $\alpha<\beta$ where $B_\alpha = h(\alpha)$,
exists unique measurable function, $f:X\to\ereals$
such that $f\leq \alpha$ on $B_\alpha$ and $f\geq \alpha$ on $X\sim B_\alpha$

</li>
<li>
	can relax some conditions and make it a.e. version as below

</li>
<li>
	for function, $h:D\to\algB$, for dense set of real numbers, $D$,
such that $\mu(B_\alpha\sim B_\beta)=0$ for all $\alpha < \beta$ where $B_\alpha = h(\alpha)$,
exists measurable function, $f:X\to\ereals$
such that $f\leq \alpha$ a.e. on $B_\alpha$ and $f\geq \alpha$ a.e. on $X\sim B_\alpha$

	<ul>
	<li>
		if $g$ has the same property, $f=g$ a.e.

	</li>
	</ul>

</li>
</ul>

<h3>Integration</h3>


<ul>
<li>
	many definitions and proofs of Lebesgue integral
depend only on properties of Lebesgue measure
which are also true for arbitrary measure in abstract measure space
(page~)

</li>
<li>
	integral of nonnegative simple function, $\varphi(x) = \sum_{i=1}^n c_i \chi_{E_i}(x)$,
on measurable set, $E$, defined by


$$
\int_E \varphi d\mu= \sum_{i=1}^n c_i \mu (E_i \cap E)
$$

	<ul>
	<li>
		independent of representation of $\varphi$

	</li>
	</ul>


</li>
<li>
	for $a,b\in\ppreals$ and nonnegative simple functions, $\varphi$ and $\psi$

$$
\int (a\varphi + b\psi) = a \int\varphi + b \int\psi
$$



</li>
</ul>

<h3>Integral of bounded functions</h3>

<ul>
<li>
	for bounded function, $f$, identically zero outside measurable set of finite measure



$$
\sup_{\varphi:\ \mathrm{simple},\ \varphi \leq f} \int \varphi
=
\inf_{\psi:\ \mathrm{simple},\ f \leq \psi} \int \psi
$$

if and only if
$f=g$ a.e. for measurable function, $g$


</li>
<li>
	but,
<span class="fact-font">$f=g$ a.e. for measurable function, $g$,
\iaoi\
$f$ is measurable with respect to completion of $\mu$, $\bar{\mu}$</span>

</li>
<li>
	<span class="eemph">natural class of functions to consider for integration theory are
those measurable \wrt\ completion of $\mu$</span>

</li>
<li>
	thus, shall either
assume $\mu$ is complete measure
or
define integral with respect to $\mu$ to be integral with respect to completion of $\mu$
depending on context
unless otherwise specified

</li>
</ul>

<h3>Difficulty of general integral of nonnegative functions</h3>

<ul>
<li>
	for Lebesgue integral of nonnegative functions
(page~)
	<ul>
	<li>
		first define integral for bounded measurable functions

	</li>
	<li>
		define integral of nonnegative function, $f$
as supremum of integrals of all bounded measurable functions, $h\leq f$,
vanishing outside measurable set of finite measure

	</li>
	</ul>

</li>
<li>
	unfortunately, not work in case that measure is not semifinite
	<ul>
	<li>
		<i>e.g.</i>, if $\algB=\{\emptyset,X\}$ with $\mu \emptyset = 0$ and $\mu X = \infty$,
we want $\int 1 d\mu=\infty$,
but only bounded measurable function vanishing outside measurable set of finite measure is $h\equiv0$,
hence,
$\int g d\mu = 0$

	</li>
	</ul>

</li>
<li>
	to avoid this difficulty,
we define integral of nonnegative measurable function
directly in terms of
integrals of nonnegative simple functions

</li>
</ul>

<h3>Integral of nonnegative functions</h3>

<ul>
<li>
	for measurable function, $f:X\to\reals\cup\{\infty\}$, on measure space, $\meas{X}{\algB}{\mu}$,
define <span class="define">integral of nonnegative extended real-valued measurable function</span>



$$
\int f d\mu = \sup_{\varphi:\ \mathrm{simple\ function},\ 0\leq \varphi\leq f} \int \varphi d\mu
$$



</li>
<li>
	however,
<i>definition of integral of nonnegative extended real-valued measurable function</i>
can be awkward to apply because
	<ul>
	<li>
		taking supremum over large collection of simple functions

	</li>
	<li>
		<i>not clear from definition that $\int(f+g) = \int f + \int g$</i>

	</li>
	</ul>

</li>
<li>
	thus,
first establish some convergence theorems,
and
determine value of $\int f$
as limit of $\int \varphi_n$ for increasing sequence, $\seq{\varphi_n}$, of simple functions
converging to $f$

</li>
</ul>

<h3>Fatou's lemma and monotone convergence theorem</h3>

<ul>
<li>
	<span class="name-font">Fatou's lemma -</span>
for nonnegative measurable function sequence, $\seq{f_n}$,
with $\lim f_n = f$ a.e. on measurable set, $E$





$$
\int_E f \leq \liminf \int_E f_n
$$


</li>
<li>
	<span class="name-font">monotone convergence theorem -</span>
for nonnegative measurable function sequence, $\seq{f_n}$,
with $f_n\leq f$ for all $n$ and with $\lim f_n = f$ a.e.




$$
\int_E f = \lim \int_E f_n
$$



</li>
</ul>

<h3>Integrability of nonnegative functions</h3>

<ul>
<li>
	for nonnegative measurable functions, $f$ and $g$, and $a,b\in\preals$


$$
\int (af + bg) = a\int f + b\int g
\mbox{ \& }
\int f \geq 0
$$

	<ul>
	<li>
		equality holds if and only if $f=0$ a.e.

	</li>
	</ul>


</li>
<li>
	monotone convergence theorem together with above yields,
for nonnegative measurable function sequence, $\seq{f_n}$

$$
\int \sum f_n = \sum \int f_n
$$


</li>
<li>
	measurable nonnegative function, $f$, with





$$
\int_E fd\mu <\infty
$$

said to be <span class="define">integral (over measurable set, $E$, \wrt\ $\mu$)</span>


</li>
</ul>

<h3>Integral</h3>

<ul>
<li>
	arbitrary function, $f$, for which both $f^+$ and $f^-$ are integrable,
said to be <span class="define">integrable</span>





</li>
<li>
	in this case, define <span class="define">integral</span>

$$
\int_E f = \int_E f^+ - \int_E f^-
$$



</li>
</ul>

<h3>Properties of integral</h3>

<ul>
<li>
	for $f$ and $g$ integrable on measure set, $E$, and $a,b\in\reals$


	<ul>
	<li>
		$af+bg$ is integral and

$$
\int_E (af+bg) = a \int_E f + b\int_E g
$$


	</li>
	<li>
		if $|h|\leq |f|$ and $h$ is measurable, then $h$ is integrable

	</li>
	<li>
		if $f\geq g$ a.e.

$$
\int f \geq \int g
$$


	</li>
	</ul>


</li>
</ul>

<h3>Lebesgue convergence theorem</h3>

<ul>
<li>
	<span class="name-font">Lebesgue convergence theorem -</span>
for integral, $g$, over $E$
and
sequence of measurable functions, $\seq{f_n}$, with $\lim f_n(x) = f(x)$ a.e. on $E$,
if





$$
|f_n(x)|\leq g(x)
$$

then

$$
\int_E f = \lim \int_E f_n
$$




</li>
</ul>

<h3>Setwise convergence of sequence of measures</h3>

<ul>
<li>
	preceding convergence theorems assume fixed measure, $\mu$

</li>
<li>
	can generalize by allowing measure to vary

</li>
<li>
	given measurable space, $\measu{X}{\algB}$, sequence of set functions, $\seq{\mu_n}$, defined on $\algB$, satisfying

$$
(\forall E\in\algB)
(\lim \mu_n E = \mu E)
$$

for some set function, $\mu$, defined on $\algB$,
said to <span class="define">converge setwise</span> to $\mu$


</li>
</ul>

<h3>General convergence theorems</h3>

<ul>
<li>
	<span class="name-font">generalization of Fatou's leamma -</span>



for measurable space, $\measu{X}{\algB}$,
sequence of measures, $\seq{\mu_n}$, defined on $\algB$, converging setwise to $\mu$, defined on $\algB$,
and
sequence of nonnegative functions, $\seq{f_n}$, each measurable with respect to $\mu_n$,
converging pointwise to function, $f$, measurable with respect to $\mu$
(compare with Fatou's lemma on page~)

$$
\int f d\mu \leq \liminf\int f_n d\mu_n
$$


</li>
<li>
	<span class="name-font">generalization of Lebesgue convergence theorem -</span>



for measurable space, $\measu{X}{\algB}$,
sequence of measures, $\seq{\mu_n}$, defined on $\algB$, converging setwise to $\mu$, defined on $\algB$,
and
sequences of functions, $\seq{f_n}$ and $\seq{g_n}$, each of $f_n$ and $g_n$, measurable with respect to $\mu_n$,
converging pointwise to $f$ and $g$, measurable with respect to $\mu$, respectively,
such that
(compare with Lebesgue convergence theorem on page~)

$$
\lim \int g_n d\mu_n = \int g d\mu < \infty
$$

satisfy

$$
\lim \int f_n d\mu_n = \int f\mu
$$


</li>
</ul>

<h3>$L^p$ spaces</h3>

<ul>
<li>
	for complete measure space, $\meas{X}{\algB}{\mu}$
	<ul>
	<li>
		space of measurable functions on $X$ with with $\int |f|^p < \infty$,
for which element equivalence is defined by being equal a.e.,
called <span class="define">$L^p$ spaces</span> denoted by $L^p(\mu)$


	</li>
	<li>
		space of bounded measure functions,
called <span class="define">$L^\infty$ space</span> denoted by $L^\infty(\mu)$


	</li>
	</ul>

</li>
<li>
	norms
	<ul>
	<li>
		for $p\in[1,\infty)$

$$
\|f\|_p=\left(
\int |f|^p d\mu
\right)^{1/p}
$$


	</li>
	<li>
		for $p=\infty$

$$
\|f\|_\infty = \mathrm{ess\ sup} |f|
= \inf \bigsetl{|g(x)|}{\mbox{measurable }g \mbox{ with } g=f \mbox{ a.e.}}
$$


	</li>
	</ul>

</li>
<li>
	for $p\in[1,\infty]$,
spaces, $L^p(\mu)$, are Banach spaces

</li>
</ul>

<h3>Ho&#776;lder's inequality and Littlewood's second principle</h3>


<ul>
<li>
	<span class="name-font">Ho&#776;lder's inequality -</span>



for $p,q\in[1,\infty]$ with $1/p+1/q=1$,
$f\in L^p(\mu)$ and $g\in L^q(\mu)$ satisfy
$fg \in L^1(\mu)$ and

$$
\|fg\|_1 = \int |fg| d\mu \leq \|f\|_p\|g\|_q
$$



</li>
<li>
	<span class="name-font">complete measure space version of Littlewood's second principle -</span>


for $p\in[1,\infty)$

$$
\begin{eqnarray*}
&=&
(\forall f\in L^p(\mu), \epsilon>0)

\\
&&
(\exists \mbox{ simple function } \varphi \mbox{ vanishing outside set of finite measure})
\\
&&
\ \ \ \ \ \ \
(\|f-\varphi\|_p < \epsilon)
\end{eqnarray*}
$$



</li>
</ul>

<h3>Riesz representation theorem</h3>

<ul>
<li>
	<span class="name-font">Riesz representation theorem -</span>





for $p\in[1,\infty)$ and bounded linear functional, $F$, on $L^p(\mu)$
and $\sigma$-finite measure, $\mu$,
exists <i>unique</i> $g\in L^q(\mu)$
where $1/p+1/q=1$
such that

$$
F(f) = \int fg d\mu
$$

where $\|F\| = \|g\|_q$


</li>
<li>
	if $p\in(1,\infty)$,
Riesz representation theorem holds without assumption of $\sigma$-finiteness of measure

</li>
</ul>

<h2 id="Measure and Outer Measure">Measure and Outer Measure</h2>


<h3>General measures</h3>

<ul>
<li>
	consider some ways of defining measures on $\sigma$-algebra

</li>
<li>
	recall that for Lebesgue measure
	<ul>
	<li>
		define measure for open intervals

	</li>
	<li>
		define outer measure

	</li>
	<li>
		define notion of measurable sets

	</li>
	<li>
		finally derive Lebesgue measure

	</li>
	</ul>

</li>
<li>
	one can do similar things in general, <i>e.g.</i>,
	<ul>
	<li>
		derive measure from outer measure

	</li>
	<li>
		derive outer measure from measure defined on algebra of sets

	</li>
	</ul>

</li>
</ul>

<h3>Outer measure</h3>

<ul>
<li>
	set function, $\mu^\ast:\powerset(X)\to[0,\infty]$,
for space $X$, having following properties,
called <span class="define">outer measure</span>

	<ul>
	<li>
		$\mu^\ast \emptyset = 0$

	</li>
	<li>
		$A\subset B \Rightarrow \mu^\ast A \leq \mu^\ast B$
(monotonicity)

	</li>
	<li>
		$E \subset \bigcup_{n=1}^\infty E_n \Rightarrow \mu^\ast E \leq \sum_{n=1}^\infty \mu^\ast E_n$
(countable subadditivity)

	</li>
	</ul>

</li>
<li>
	$\mu^\ast$ with $\mu^\ast X<\infty$ called <span class="define">finite</span>

</li>
<li>
	set $E\subset X$ satisfying following property,
said to be <span class="define">measurable \wrt\ $\mu^\ast$</span>


$$
(\forall A\subset X)
(\mu^\ast(A) =\mu^\ast(A\cap E) + \mu^\ast(A\cap \compl{E}))
$$


</li>
<li>
	class, $\algB$, of $\mu^\ast$-measurable sets is $\sigma$-algebra

</li>
<li>
	restriction of $\mu^\ast$ to $\algB$ is complete measure on $\algB$

</li>
</ul>

<h3>Extension to measure from measure on an algebra</h3>

<ul>
<li>
	set function, $\mu:\alg\to[0,\infty]$, defined on algebra, $\alg$,
having following properties,
called <span class="define">measure on an algebra</span>

	<ul>
	<li>
		$\mu(\emptyset) = 0$

	</li>
	<li>
		$\left(
\forall \mbox{ disjoint } \seq{A_n} \subset \alg \mbox{ with } \bigcup A_n \in \alg
\right)
\left(
\mu\left(\bigcup A_n\right) = \sum \mu A_n
\right)$

	</li>
	</ul>

</li>
<li>
	<i>measure on an algebra, \alg</i>, is measure if and only if $\alg$ is $\sigma$-algebra

</li>
<li>
	can extend measure on an algebra to measure defined on $\sigma$-algebra, $\algB$, containing $\alg$,
by
	<ul>
	<li>
		constructing outer measure $\mu^\ast$ from $\mu$

	</li>
	<li>
		deriving desired extension $\bar{\mu}$ induced by $\mu^\ast$

	</li>
	</ul>

</li>
<li>
	
process by which constructing $\mu^\ast$ from $\mu$
similar to
constructing Lebesgue outer measure from lengths of intervals

</li>
</ul>

<h3>Outer measure constructed from measure on an algebra</h3>

<ul>
<li>
	
given
measure, $\mu$, on an algebra, $\alg$

</li>
<li>
	define set function, $\mu^\ast:\powerset(X)\to[0,\infty]$, by

$$
\mu^\ast E = \inf_{\seq{A_n}\subset \alg,\ E\subset \bigcup A_n} \sum \mu A_n
$$


</li>
<li>
	$\mu^\ast$ called <span class="define">outer measure induced by $\mu$</span>


</li>
<li>
	
then

</li>
<li>
	for $A\in\alg$ and $\seq{A_n}\subset\alg$ with $A\subset \bigcup A_n$, $\mu A\leq \sum \mu A_n$

</li>
<li>
	hence, $(\forall A\in\alg)(\mu^\ast A = \mu A)$

</li>
<li>
	$\mu^\ast$ is outer measure

</li>
<li>
	every $A\in\alg$ is measurable with respect to $\mu^\ast$

</li>
</ul>

<h3>Regular outer measure</h3>

<ul>
<li>
	for algebra, $\alg$
	<ul>
	<li>
		$\alg_\sigma$ denote sets that are countable unions of sets of $\alg$

	</li>
	<li>
		$\alg_{\sigma \delta}$ denote sets that are countable intersections of sets of $\alg_\sigma$

	</li>
	</ul>

</li>
<li>
	given
measure, $\mu$, on an algebra, $\alg$
and
outer measure, $\mu^\ast$ induced by $\mu$,
for every $E\subset X$ and every $\epsilon>0$,
exists $A\in\alg_\sigma$ and $B\in\alg_{\sigma \delta}$ with $E\subset A$ and $E\subset B$

$$
\mu^\ast A \leq \mu^\ast E + \epsilon
\mbox{ and }
\mu^\ast E = \mu^\ast B
$$


</li>
<li>
	outer measure, $\mu^\ast$, with below property,
said to be <span class="define">regular</span>


$$
(\forall E\subset X, \epsilon>0)
(\exists \mbox{ $\mu^\ast$-measurable set }A \mbox{ with } E\subset A)
(\mu^\ast A \subset \mu^\ast E + \epsilon)
$$


</li>
<li>
	every outer measure induced by measure on an algebra is regular outer measure


</li>
</ul>

<h3>Carathe&#769;odory theorem</h3>

<ul>
<li>
	
given measure, $\mu$, on an algebra, $\alg$ and outer measure, $\mu^\ast$ induced by $\mu$

</li>
<li>
	$E\subset X$ is $\mu^\ast$-measurable
if and only if
exist $A\in\alg_{\sigma\delta}$ and $B\subset X$ with $\mu^\ast B=0$
such that

$$
E=A\sim B
$$

	<ul>
	<li>
		for $B\subset X$ with $\mu^\ast B=0$,
exists $C\in\alg_{\sigma\delta}$ with $\mu^\ast C=0$
such that $B\subset C$

	</li>
	</ul>

</li>
<li>
	<span class="name-font">Carathe&#769;odory theorem -</span>


restriction, $\bar{\mu}$, of $\mu^\ast$ to $\mu^\ast$-measurable sets
if extension of $\mu$ to $\sigma$-algebra containing $\alg$
	<ul>
	<li>
		if $\mu$ is finite or $\sigma$-finite,
so is $\bar{\mu}$ respectively

	</li>
	<li>
		if $\mu$ is $\sigma$-finite,
$\bar{\mu}$
is only measure
on smallest $\sigma$-algebra containing $\alg$
which is extension of $\mu$

	</li>
	</ul>

</li>
</ul>

<h3>Product measures</h3>



<ul>
<li>
	for countable disjoint collection of measurable rectangles, $\seq{(A_n \times B_n)}$,
whose union is measurable rectangle, $A\times B$

$$
\lambda(A\times B) = \sum \lambda(A_n \times B_n)
$$


</li>
<li>
	for $x\in X$ and $E\in \algk{R}_{\sigma\delta}$

$$
E_x = \set{y}{\langle x,y\rangle \in E}
$$

is measurable subset of $Y$

</li>
<li>
	for $E\subset\algk{R}_{\sigma\delta}$ with $\mu \times \nu(E)<\infty$,
function, $g$, defined by

$$
g(x) = \nu E_x
$$

is measurable function of $x$ and

$$
\int g d\mu = \mu \times \nu(E)
$$


</li>
<li>
	XXX

</li>
</ul>

<h3>Carathe&#769;odory outer measures</h3>

<ul>
<li>
	set, $X$, of points and set, $\Gamma$, of real-valued functions on $X$

</li>
<li>
	two sets for which exist $a>b$ such that function, $\varphi$, greater than $a$ on one set
and less than $b$ on the other set,
said to be <span class="define">separated by function, $\varphi$</span>


</li>
<li>
	outer measure, $\mu^\ast$, with
$(\forall A,B\subset X \mbox{ separated by } f\in\Gamma)
(\mu^\ast(A\cup B) = \mu^\ast A + \mu^\ast B)$,
called <span class="define">Carathe&#769;odory outer measure with respect to $\Gamma$</span>




</li>
<li>
	outer measure, $\mu^\ast$, on metric space, $\metrics{X}{\rho}$,
for which $\mu^\ast(A\cup B)=\mu^\ast A + \mu^\ast B$ for $A,B\subset X$ with $\rho(A,B)>0$,
called <span class="define">Carathe&#769;odory outer measure for $X$</span> or <span class="define">metric outer measure</span>





</li>
<li>
	for <i>Carathe&#769;odory outer measure, $\mu^\ast$, with respect to $\Gamma$</i>,
every function in $\Gamma$ is $\mu^\ast$-measurable

</li>
<li>
	for <i>Carathe&#769;odory outer measure, $\mu^\ast$, for metric space, \metrics{X, \rho}</i>,
every closed set (hence every Borel set) is measurable with respect to $\mu^\ast$

</li>
</ul>

