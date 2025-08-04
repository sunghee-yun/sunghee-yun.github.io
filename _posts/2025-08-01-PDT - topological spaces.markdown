---
title: Topological Spaces
date: Fri Aug  1 04:00:00 PDT 2025
last_modified_at: Mon Aug  4 16:01:19 PDT 2025
permalink: /math/rig/topological-spaces
categories:
- blog
tags:
- math
- topology
- topological spaces
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

<div id="page:Notations"></div>
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

<div id="page:Some---definitions"></div>
<div class="definition" id="definition:infinitely---often-------i.o." data-name="infinitely often - i.o.">
	


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

<div class="definition" id="definition:almost---everywhere-------a.e." data-name="almost everywhere - a.e.">
	




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

<div id="page:Some---conventions"></div>
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


<h1 id="super-title-page:Real-Analysis">Real Analysis</h1>



<h2 id="title-page:set-theory">Set Theory</h2>


<h3>Some principles</h3>

<div class="principle" id="principle:principle---of---mathematical---induction" data-name="principle of mathematical induction">
	

$$

P(1) \& [P(n\Rightarrow P(n+1)] \Rightarrow (\forall n \in \naturals)P(n)

$$


</div>

<div class="principle" id="principle:well---ordering---principle" data-name="well ordering principle">
	
each nonempty subset of $\naturals$ has a smallest element

</div>

<div class="principle" id="principle:principle---of---recursive---definition" data-name="principle of recursive definition">
	
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
<a href="#principle:principle---of---mathematical---induction"></a>
$\Leftrightarrow$
<a href="#principle:well---ordering---principle"></a>
$\Rightarrow$
<a href="#principle:principle---of---recursive---definition"></a>

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
denoted by <span class="notation">$\relxy{x}{y}$</span>

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

<div class="axiom" id="axiom:axiom---of---choice" data-name="axiom of choice">
	
given a collection of nonempty sets, $\coll$,
there exists $f:\coll\ \to \cup_{A\in\coll} A $ such that

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

<div class="principle" id="principle:Hausdorff---maximal---principle" data-name="Hausdorff maximal principle">
	

for particial ordering $\prec$ on $X$,
exists a maximal linearly ordered subset $S\subset X$,
<i>i.e.</i>,
$S$ is linearity ordered by $\prec$
and if $S\subset T\subset X$ and $T$ is linearly ordered by $\prec$,
$S=T$

</div>

<div class="principle" id="principle:well-ordering---principle" data-name="well-ordering principle">
	
every set $X$ can be well ordered,
<i>i.e.</i>,
there is a relation $<$ that well orders $X$

</div>
<ul>
<li>
	note that
<a href="#axiom:axiom---of---choice"></a>
$\Leftrightarrow$
<a href="#principle:Hausdorff---maximal---principle"></a>
$\Leftrightarrow$
<a href="#principle:well-ordering---principle"></a>

</li>
</ul>

<h3>Infinite direct product</h3>

<div class="definition" id="definition:direct---product" data-name="direct product">
	
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
	this is why Bertrand Russell prefers <i>multiplicative axiom</i> to <i>axiom of choice</i> for name of axiom (<a href="#axiom:axiom---of---choice"></a>)



</li>
</ul>

<h2 id="title-page:real-number-system">Real Number System</h2>


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
$
x < r < y
$

	</li>
	</ul>

</li>
</ul>

<h3>Sequences of $\reals$</h3>

<ul>
<li>
	sequence of $\reals$ denoted by <span class="notation">$\seq{x_i}_{i=1}^\infty$</span> or <span class="notation">$\seq{x_i}$</span>
	<ul>
	<li>
		mapping from $\naturals$ to $\reals$

	</li>
	</ul>

</li>
<li>
	limit of $\seq{x_n}$ denoted by <span class="notation">$\lim_{n\to\infty} x_n$</span> or <span class="notation">$\lim x_n$</span> - defined by $a\in\reals$
such that

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

<div id="page:open-closed-fact"></div>
<ul>
<li>
	<span class="fact-font">every open set is union of countable collection of disjoint open intervals</span>

<div id="page:open-set-in-reals-is-union-of-countable-collection-of-disjoint-open-intervals"></div>

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

<div id="page:heine-borel-theorem"></div>
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
	<span class="name-font">Heine-Borel theorem</span> -
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

<div id="page:borel-algebra"></div>
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
(due to statement on page~<a href="#page:open-set-in-reals-is-union-of-countable-collection-of-disjoint-open-intervals">here</a>)

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

<h2 id="title-page:Space---Overview">Space Overview</h2>


<h3>Diagrams for relations among various spaces</h3>

<div id="page:diagrams-for-relations-among-spaces"></div>
<ul>
<li>
	note from the figure
	<ul>
	<li>
		metric should be defined to utter completeness

	</li>
	<li>
		metric spaces can be induced from normed spaces

	</li>
	</ul>

</li>
</ul>











<div id="fig:diagrams---for---relations---among---various---spaces"></div>




<h2 id="title-page:classical-banach-spaces">Classical Banach Spaces</h2>


<h3>Normed linear space</h3>

<ul>
<li>
	$X$ called <span class="define">linear space</span> if

$$

(\forall x, y \in X, a, b \in \reals)(ax + by \in X)

$$


</li>
<li>
	linear space, $X$, called <span class="define">normed space</span> with associated norm $\|\cdot\|: X \to \preals$ if


	<ul>
	<li>
		
$$

(\forall x\in X)(\|x\|=0 \Rightarrow x \equiv 0)

$$


	</li>
	<li>
		
$$

(\forall x \in X, a \in \reals)(\|ax\| = |a|\|x\|)

$$


	</li>
	<li>
		subadditivity

$$

(\forall x,y\in X)(\|x+y\| \leq \|x\| + \|y\|)

$$


	</li>
	</ul>

</li>
</ul>

<h3>$L^p$ spaces</h3>

<ul>
<li>
	$L^p = L^p[0,1]$ denotes space of (Lebesgue) measurable functions such that


$$

\int_{[0,1]} |f|^p < \infty

$$


</li>
<li>
	define $\|\cdot\|:L^p\to\preals$

$$

\|f\| = \|f\|_p = \left(\int_{[0,1]} |f|^p\right)^{1/p}

$$


</li>
<li>
	$L^p$ are <i>linear normed spaces</i> with norm $\|\cdot\|_p$ when $p\geq 1$ because
	<ul>
	<li>
		$|f(x)|^p + |g(x)|^p \leq 2^p(|f(x)|^p + |g(x)|^p)$ implies $(\forall f, g\in L^p)(f+g \in L^p)$

	</li>
	<li>
		$|\alpha f(x)|^p = |a|^p|f(x)|^p$ implies $(\forall f\in L^p, a \in \reals)(af \in L^p)$

	</li>
	<li>
		$\|f\|=0\Rightarrow f=0\mbox{ a.e.}$

	</li>
	<li>
		$\|a f\| = |a|\|f\|$

	</li>
	<li>
		$\|f+g\|\geq \|f\|+\|g\|$ (Minkowski inequality)

	</li>
	</ul>

</li>
</ul>

<h3>$L^\infty$ space</h3>

<ul>
<li>
	$L^\infty = L^\infty[0,1]$ denotes space of measurable functions bounded a.e.


</li>
<li>
	$L^\infty$ is linear normed space with norm

$$

\|f\| = \|f\|_\infty = \mathrm{ess\ sup} |f|
= \inf_{g: g=f \ \mathrm{a.e}} \sup_{x\in[0,1]} |g(x)|

$$

	<ul>
	<li>
		thus

$$

\|f\|_\infty = \inf\set{M}{\mu\set{x}{f(x)>M}=0}

$$


	</li>
	</ul>

</li>
</ul>

<h3>Inequalities in $L^\infty$</h3>

<ul>
<li>
	<span class="name-font">Minkowski inequality -</span> for $p\in[1,\infty]$



$$

(\forall f,g\in L^p)(\|f+g\|_p \leq \|f\|_p + \|g\|_p)

$$

	<ul>
	<li>
		if $p\in(1,\infty)$, equality holds if and only if
$(\exists a,b\geq 0 \mbox{ with } ab\neq0)(af = bg \mbox{ a.e.})$

	</li>
	</ul>

</li>
<li>
	Minkowski inequality for $0<p<1$:



$$

(\forall f,g\in L^p)(f,g\geq0 \mbox{ a.e.} \Rightarrow \|f+g\|_p \geq \|f\|_p + \|g\|_p)

$$


</li>
<li>
	<span class="name-font">Ho&#776;lder's inequality -</span> for $p,q\in[1,\infty]$ with $1/p+1/q=1$


<div id="Holder---inequality!linear---normed---spaces"></div>

$$

(\forall f\in L^p, g\in L^q)
\left(fg \in L^1 \mbox{ and } \int_{[0,1]} |fg| \leq \int_{[0,1]} |f|^p \int_{[0,1]} |g|^q\right)

$$

	<ul>
	<li>
		equality holds if and only if
$(\exists a,b\geq 0 \mbox{ with } ab\neq0)(a|f|^p = b|g|^q \mbox{ a.e.})$

	</li>
	</ul>


</li>
</ul>

<h3>Convergence and completeness in normed linear spaces</h3>

<ul>
<li>
	$\seq{f_n}$ in normed linear space
	<ul>
	<li>
		said to <span class="define">converge</span> to $f$, <i>i.e.</i>, $\lim f_n =f$ or $f_n \to f$, if

$$

(\forall \epsilon>0)(\exists N\in\naturals)(\forall n> N)(\|f_n-f\|<\epsilon)

$$


	</li>
	<li>
		called <span class="define">Cauchy sequence</span> if

$$

(\forall \epsilon>0)(\exists N\in\naturals)(\forall n,m> N)(\|f_n-f_m\|<\epsilon)

$$


	</li>
	<li>
		called <span class="define">summable</span> if $\sum^n_{i=1} f_i$ converges

	</li>
	<li>
		called <span class="define">absolutely summable</span> if $\sum^n_{i=1} |f_i|$ converges

	</li>
	</ul>

</li>
<li>
	normed linear space called <span class="define">complete</span> if every Cauchy sequence converges


</li>
<li>
	normed linear space is <i>complete</i> if and only if every absolutely summable series is summable

</li>
</ul>

<h3>Banach space</h3>

<div id="page:Banach-space"></div>
<ul>
<li>
	<i>complete normed linear space</i> called <span class="define">Banach space</span>





</li>
<li>
	(Riesz-Fischer) $L^p$ spaces are compact, hence Banach spaces

</li>
<li>
	convergence in $L^p$ called <span class="define">convergence in mean of order $p$</span>

</li>
<li>
	convergence in $L^\infty$ implies nearly uniformly converges

</li>
</ul>

<h3>Approximation in $L^p$</h3>

<ul>
<li>
	$\Delta=\seq{d_i}_{i=0}^n$ with $0=d_1<d_2<\cdots<d_n=1$ called <span class="define">subdivision</span> of $[0,1]$
(with $\Delta_i = [d_{i-1},d_{i}]$)

</li>
<li>
	$\varphi_{f,\Delta}$ for $f\in L^p$ called <span class="define">step function</span> if

$$

\varphi_{f,\Delta}(x) = \frac{1}{d_i-d_{i+1}}\int_{d_{i-1}}^{d_i} f(t)dt \mbox{ for } x\in[d_{i-1},d_i)

$$


</li>
<li>
	for $f\in L^p$ ($1<p\leq \infty$), exist $\varphi_{f,\Delta}$ and continuous function, $\psi$ such that

$$

\|\varphi_{f,\Delta_i}-f\|<\epsilon
\mbox{ and }
\|\psi-f\|<\epsilon

$$

	<ul>
	<li>
		$L^p$ version of Littlewood's second principle (page~<a href="#page:littlewood:three:principles">here</a>)
<div id="page:normed---space---version---of---Littlewood's---second---principle"></div>



	</li>
	</ul>

</li>
<li>
	for $f\in L^p$, $\varphi_{f,\Delta}\to f$ as $\max \Delta_i\to0$, <i>i.e.</i>,

$$

(\forall \epsilon>0)(\exists \delta>0)(\max \Delta_i < \delta \Rightarrow \|\varphi_{f,\Delta}-f\|_p < \epsilon)

$$


</li>
</ul>

<h3>Bounded linear functionals on $L^p$</h3>

<ul>
<li>
	$F:X\in\reals$ for normed linear space $X$ called <span class="define">linear functional</span> if

$$

(\forall f, g \in F, a,b \in\reals)(F(af+bg)=aF(f)+bF(g))

$$


</li>
<li>
	linear functional, $F$, said to be <span class="define">bounded</span> if

$$

(\exists M)(\forall f\in X)(|F(f)|\leq M\|f\|)

$$


</li>
<li>
	smallest such constant called <span class="define">norm of $F$</span>, <i>i.e.</i>,

$$

\|F\| = \sup_{f\in X, f\neq0} {|F(f)|}/{\|f\|}

$$


</li>
</ul>

<h3>Riesz representation theorem</h3>

<ul>
<li>
	for every $g\in L^q$ ($1\leq p\leq \infty$), following defines a bounded linear functional in $L^p$

$$

F(f) = \int fg

$$

where $\|F\|=\|g\|_q$

</li>
<li>
	<span class="name-font">Riesz representation theorem -</span>
for every bounded linear functional in $L^p$, $F$, ($1\leq p<\infty$),
there exists $g\in L^q$ such that





<div id="page:Riesz-representation-theorem"></div>

$$

F(f) = \int fg

$$

where $\|F\|=\|g\|_q$


</li>
<li>
	for each case, $L^q$ is dual of $L^p$
(refer to page <a href="#page:Dual-of-normed-spaces">here</a> for definition of dual)

</li>
</ul>

<h2 id="title-page:metric-spaces">Metric Spaces</h2>


<h3>Metric spaces</h3>

<ul>
<li>
	$\metrics{X}{\rho}$ with nonempty set, $X$, and <span class="define">metric</span> $\rho: X\times X\to\preals$ called <span class="define">metric space</span>
if for every $x,y,z \in X$
	<ul>
	<li>
		$\rho(x,y)=0 \Leftrightarrow x=y$

	</li>
	<li>
		$\rho(x,y)=\rho(y,x)$

	</li>
	<li>
		$\rho(x,y) \leq \rho(x,z) + \rho(z,y)$ (triangle inequality)

	</li>
	</ul>

</li>
<li>
	examples of metric spaces
	<ul>
	<li>
		$\metrics{\reals}{|\cdot|}$, $\metrics{\reals^n}{\|\cdot\|_p}$ with $1\leq p\leq \infty$

	</li>
	</ul>

</li>
<li>
	for $f\subset X$, $S_{x,r} = \set{y}{\rho(y,x)<r}$ called <span class="define">ball</span>

</li>
<li>
	for $E\subset X$, $\sup\set{\rho(x,y)}{x,y \in E}$ called diameter of $E$ defined by

</li>
<li>
	$\rho$ called <span class="define">pseudometric</span> if 1st requirement removed

</li>
<li>
	$\rho$ called <span class="define">extended metric</span> if $\rho: X\times X \to\preals\cup\{\infty\}$

</li>
</ul>

<h3>Cartesian product</h3>

<ul>
<li>
	for two metric spaces $\metrics{X}{\rho}$ and $\metrics{Y}{\sigma}$,
metric space $\metrics{X\times Y}{\tau}$ with $\tau:X\times Y\to\preals$ such that

$$

\tau((x_1,y_1),(x_2,y_2)) = (\rho(x_1,x_2)^2 + \sigma(y_1,y_2)^2)^{1/2}

$$

called <span class="define">Cartesian product metric space</span>

</li>
<li>
	$\tau$ satisfies all properties required by metric
	<ul>
	<li>
		<i>e.g.</i>, $\reals^{n} \times \reals^{m} = \reals^{n+m}$

	</li>
	</ul>

</li>
</ul>

<h3>Open sets - metric spaces</h3>

<ul>
<li>
	$O \subset X$ said to be open <span class="define">open</span> if

$$

(\forall x\in O)(\exists \delta>0)(\forall y\in X)(\rho(y,x)<\delta \Rightarrow y\in O)

$$

	<ul>
	<li>
		$X$ and $\emptyset$ are open

	</li>
	<li>
		intersection of <i>finite</i> collection of open sets is open

	</li>
	<li>
		union of <i>any</i> collection of open sets is open

	</li>
	</ul>

</li>
</ul>

<h3>Closed sets - metric spaces</h3>

<ul>
<li>
	$x\in X$ called <span class="define">point of closure of $E\subset X$</span> if

$$

(\forall \epsilon>0)(\exists y\in E)(\rho(y,x) < \epsilon)

$$

	<ul>
	<li>
		$\closure{E}$ denotes set of points of closure of $E$; called <span class="define">closure</span> of $E$

	</li>
	<li>
		$E\subset \closure{E}$

	</li>
	</ul>

</li>
<li>
	$F \subset X$ said to be <span class="define">closed</span> if

$$

F = \closure{F}

$$

	<ul>
	<li>
		$X$ and $\emptyset$ are closed

	</li>
	<li>
		union of <i>finite</i> collection of closed sets is closed

	</li>
	<li>
		intersection of <i>any</i> collection of closed sets is closed

	</li>
	</ul>

</li>
<li>
	complement of closed set is open

</li>
<li>
	complement of open set is closed

</li>
</ul>

<h3>Dense sets and separability - metric spaces</h3>

<div id="page:dense-sets-and-separability-metric-spaces"></div>
<ul>
<li>
	$D\subset X$ said to be dense if

$$

\closure{D} = X

$$


</li>
<li>
	$X$ is said to be separable if exists finite dense subset, <i>i.e.</i>,



$$

(\exists D\subset X)(|D| < \infty \ \& \ \closure{D}=X)

$$


</li>
<li>
	$X$ is separable if and only if exists countable collection of open sets $\seq{O_i}$ such that
for all open $O\subset X$

$$

O = \bigcup_{O_i\subset O} O_i

$$


</li>
</ul>

<h3>Continuous functions - metric spaces</h3>

<ul>
<li>
	$f:X\to Y$ for metric spaces $\metrics{X}{\rho}$ and $\metrics{Y}{\sigma}$ called <span class="define">mapping</span> or <span class="define">function</span>
from $X$ into $Y$

</li>
<li>
	$f$ said to be <span class="define">onto</span> if 
$$
f(X)=Y
$$


</li>
<li>
	$f$ said to be <span class="define">continuous</span> at $x\in X$ if

$$

(\forall \epsilon>0)(\exists \delta>0)(\forall y\in X)(\rho(y,x)<\delta \Rightarrow \sigma(f(y),f(x))<\epsilon)

$$


</li>
<li>
	$f$ said to be <span class="define">continuous</span> if $f$ is continuous at every $x\in X$

</li>
<li>
	$f$ is continuous if and only if for every open $O\subset Y$, $f^{-1}(O)$ is open

</li>
<li>
	if $f:X\to Y$ and $g:Y\to Z$ are continuous, $g\circ f:X\to Z$ is continuous

</li>
</ul>

<h3>Homeomorphism</h3>

<ul>
<li>
	one-to-one mapping of $X$ onto $Y$ (or equivalently, one-to-one correspondece between $X$ and $Y$), $f$,
said to be <span class="define">homeomorphism</span> if
	<ul>
	<li>
		both $f$ and $f^{-1}$ are continuous

	</li>
	</ul>

</li>
<li>
	$X$ and $Y$ said to be <span class="define">homeomorphic</span> if exists homeomorphism

</li>
<li>
	<span class="define">topology</span> is study of properties unaltered by homeomorphisms and
such properties called <span class="define">topological</span>

</li>
<li>
	one-to-one correspondece $X$ and $Y$ is homeomorphism if and only if
it maps open sets in $X$ to open sets in $Y$ and vice versa

</li>
<li>
	every property defined by means of <i>open sets</i> (or equivalently, <i>closed sets</i>)
or/and being <i>continuous functions</i>
is <i>topological one</i>
	<ul>
	<li>
		<i>e.g.</i>, $f$ is continuous on $X$ is homeomorphism, then $f\circ h^{-1}$ is continuous function on $Y$

	</li>
	</ul>

</li>
</ul>

<h3>Isometry</h3>

<ul>
<li>
	homeomorphism preserving distance called <span class="define">isometry</span>, <i>i.e.</i>,

$$

(\forall x,y \in X)(\sigma(h(x),h(y)) = \rho(x,y))

$$


</li>
<li>
	$X$ and $Y$ said to be <span class="define">isometric</span> if exists isometry

</li>
<li>
	(from abstract point of view)
two isometric spaces are exactly <i>same</i>;
it's nothing but relabeling of points

</li>
<li>
	two metrics, $\rho$ and $\sigma$ on $X$, said to be <span class="define">equivalent</span>
if identity mapping of $\metrics{X}{\rho}$ onto $\metrics{X}{\sigma}$
is homeomorphism
	<ul>
	<li>
		hence, two metrics are equivalent if and only if set in one metric is open whenever open in the other metric

	</li>
	</ul>

</li>
</ul>

<h3>Convergence - metric spaces</h3>

<ul>
<li>
	$\seq{x_n}$ defined for metric space, $X$
	<ul>
	<li>
		said to <span class="define">converge</span> to $x$, <i>i.e.</i>, $\lim x_n =x$ or $x_n \to x$, if

$$

(\forall \epsilon>0)(\exists N\in\naturals)(\forall n> N)(\rho(x_n,x)<\epsilon)

$$

		<ul>
		<li>
			 equivalently, every ball about $x$ contains all but finitely many points of $\seq{x_n}$

		</li>
		</ul>

	</li>
	<li>
		said to have cluster point, $x$, if

$$

(\forall \epsilon>0, N\in\naturals)(\exists n> N)(\rho(x_n,x)<\epsilon)

$$

		<ul>
		<li>
			 equivalently, every ball about $x$ contains infinitely many points of $\seq{x_n}$

		</li>
		<li>
			 equivalently, every ball about $x$ contains at least one point of $\seq{x_n}$

		</li>
		</ul>

	</li>
	</ul>

</li>
<li>
	every convergent point is cluster point
	<ul>
	<li>
		converse not true

	</li>
	</ul>

</li>
</ul>

<h3>Completeness - metric spaces</h3>

<div id="page:Completeness---metric-spaces"></div>
<ul>
<li>
	$\seq{x_n}$ of metric space, $X$, called <span class="define">Cauchy sequence</span> if

$$

(\forall \epsilon>0)(\exists N\in\naturals)(\forall n,m> N)(\rho(x_n,x_m)<\epsilon)

$$


</li>
<li>
	convergence sequence is Cauchy sequence

</li>
<li>
	$X$ said to be <span class="define">complete</span> if every Cauchy sequence converges

	<ul>
	<li>
		<i>e.g.</i>, $\metrics{\reals}{\rho}$ with $\rho(x,y)=|x-y|$

	</li>
	</ul>

</li>
<li>
	for incomplete $\metrics{X}{\rho}$, exists complete $X^\ast$
where $X$ is isometrically embedded in $X^\ast$ as dense set

</li>
<li>
	if $X$ contained in complete $Y$,
$X^\ast$ is isometric with $\closure{X}$ in $Y$

</li>
</ul>

<h3>Uniform continuity - metric spaces</h3>

<div id="page:uniform-continuity-metric-spaces"></div>
<ul>
<li>
	$f:X\to Y$ for metric spaces $\metrics{X}{\rho}$ and $\metrics{Y}{\sigma}$
said to be <span class="define">uniformly continuous</span> if

$$

(\forall \epsilon>0)(\exists \delta)(\forall x,y \in X)(\rho(x,y) < \delta \Rightarrow \sigma(f(x),f(y))<\epsilon)

$$

	<ul>
	<li>
		example of continuous, but not uniformly continuous function
		<ul>
		<li>
			 $h:[0,1)\to\preals$ with $h(x)=x/(1-x)$

		</li>
		<li>
			 $h$ maps Cauchy sequence $\seq{1-1/n}_{n=1}^\infty$ in $[0,1)$
to $\seq{n-1}_{n=1}^\infty$ in $\preals$, which is <i>not</i> Cauchy sequence

		</li>
		</ul>

	</li>
	</ul>

</li>
<li>
	homeomorphism $f$ between $\metrics{X}{\rho}$ and $\metrics{Y}{\sigma}$ with both $f$ and $f^{-1}$
uniformly continuous called <span class="define">uniform homeomorphism</span>

</li>
</ul>

<h3>Uniform homeomorphism</h3>

<ul>
<li>
	uniform homeomorphism $f$ between $\metrics{X}{\rho}$ and $\metrics{Y}{\sigma}$
maps every Cauchy sequence $\seq{x_n}$ in $X$ mapped to $\seq{f(x_n)}$ in $Y$ which is Cauchy
	<ul>
	<li>
		being Cauchy sequence, hence, being complete preserved by uniform homeomorphism

	</li>
	<li>
		being uniformly continuous also preserved by uniform homeomorphism

	</li>
	</ul>

</li>
<li>
	each of three properties (being Cauchy sequence, being complete, being uniformly continuous)
called <span class="define">uniform property</span>

</li>
<li>
	uniform properties are <i>not</i> topological properties, <i>e.g.</i>, $h$ on page~<a href="#page:uniform-continuity-metric-spaces">here</a>
	<ul>
	<li>
		is <span class="define">homeomorphism</span> between incomplete space $[0,1)$ and complete space $\preals$

	</li>
	<li>
		maps Cauchy sequence $\seq{1-1/n}_{n=1}^\infty$ in $[0,1)$
to $\seq{n-1}_{n=1}^\infty$ in $\preals$, which is not Cauchy sequence

	</li>
	<li>
		its inverse maps uniformly continuous function $\sin$ back to non-uniformly continuity function on $[0,1)$

	</li>
	</ul>

</li>
</ul>

<h3>Uniform equivalence</h3>

<ul>
<li>
	two metrics, $\rho$ and $\sigma$ on $X$, said to be <span class="define">uniformly equivalent</span>
if identity mapping of $\metrics{X}{\rho}$ onto $\metrics{X}{\sigma}$
is uniform homeomorphism, <i>i.e.</i>,

$$

(\forall \epsilon, \delta>0, x,y \in X)
(\rho(x,y)<\delta \Rightarrow \sigma(x,y)<\epsilon
\ \&\
\sigma(x,y)<\delta \Rightarrow \rho(x,y)<\epsilon)

$$


</li>
<li>
	example of uniform equivalence on $X\times Y$
	<ul>
	<li>
		any two of below metrics are uniformly equivalent on $X\times Y$

$$
\begin{eqnarray*}

&&\tau((x_1,y_1),(x_2,y_2)) = (\rho(x_1,x_2)^2 + \sigma(y_1,y_2)^2)^{1/2}
\\
&&\rho_1((x_1,y_1),(x_2,y_2)) = \rho(x_1,x_2) + \sigma(y_1,y_2)
\\
&&\rho_\infty((x_1,y_1),(x_2,y_2)) = \max\{\rho(x_1,x_2), \sigma(y_1,y_2)\}

\end{eqnarray*}
$$


	</li>
	</ul>

</li>
<li>
	for $\metrics{X}{\rho}$ and complete $\metrics{Y}{\sigma}$ and $f:X\to Y$ uniformly continuous on $E\subset X$ into $Y$,
exists unique continuous extension $g$ of $f$ on $\closure{E}$, which is uniformly continuous

</li>
</ul>

<h3>Subspaces</h3>

<div id="page:subspaces"></div>
<ul>
<li>
	for metric space, $\metrics{X}{\rho}$,
metric space $\metrics{S}{\rho_S}$ with $S\subset X$ and $\rho_S$ being restriction of $\rho$ to S,
called <span class="define">subspace</span> of $\metrics{X}{\rho}$
	<ul>
	<li>
		<i>e.g.</i> (with standard Euclidean distance)
		<ul>
		<li>
			$\rationals$ is subspace of $\reals$

		</li>
		<li>
			$\bigsetl{(x,y)\in\reals^2}{y=0}$ is subspace of $\reals^2$, which is isometric to $\reals$

		</li>
		</ul>

	</li>
	</ul>

</li>
<li>
	for metric space, $X$, and its subspace, $S$,
	<ul>
	<li>
		$\closure{E}\subset S$ is closure of $E$ relative to $S$.

	</li>
	<li>
		$A\subset S$ is closure relative to $S$ if and only if $(\exists \closure{F}\subset A)(A = \closure{F}\cap S)$

	</li>
	<li>
		$A\subset O$ is open relative to $S$ if and only if $(\exists \mbox{ open }{O}\subset A)(A = {O}\cap S)$

	</li>
	</ul>

</li>
<li>
	also
	<ul>
	<li>
		every subspace of separable metric space is separable



	</li>
	<li>
		every complete subset of metric space is closed

	</li>
	<li>
		every closed subset of complete metric space is complete

	</li>
	</ul>

</li>
</ul>

<h3>Compact metric spaces</h3>

<div id="page:Compact-metric-spaces"></div>

<ul>
<li>
	motivation - want metric spaces where
	<ul>
	<li>
		conclusion of Heine-Borel theorem (page~<a href="#page:heine-borel-theorem">here</a>) are valid

	</li>
	<li>
		many properties of $[0,1]$ are true, <i>e.g.</i>,
Bolzano-Weierstrass property
(page~<a href="#page:bolzano-weierstrass-property-and-sequential-compactness">here</a>)

	</li>
	</ul>

</li>
<li>
	<i>e.g.</i>,
	<ul>
	<li>
		bounded closed set in $\reals$ has <i>finite open covering property</i>

	</li>
	</ul>

</li>
<li>
	metric space $X$ called <span class="define">compact metric space</span> if
every open covering of $X$, $\collk{U}$,
contains finite open covering of $X$,
<i>e.g.</i>,

$$

(\forall \mbox{ open covering of $X$}, \collk{U})(\exists \{O_1,\ldots,O_n\} \subset \collk{U})
(X\in\cup O_i)

$$


</li>
<li>
	$A\subset X$ called <span class="define">compact</span> if
compact as subspace of $X$
	<ul>
	<li>
		<i>i.e.</i>, every open covering of $A$ contains finite open covering of $A$

	</li>
	</ul>

</li>
</ul>

<h3>Compact metric spaces - alternative definition</h3>

<ul>
<li>
	collection, $\collk{F}$, of sets in $X$ said to have
<span class="define">finite intersection property</span>
if every finite subcollection of $\collk{F}$ has nonempty intersection

</li>
<li>
	if rephrase definition of compact metric spaces in terms of <i>closed</i> instead of <i>open</i>
	<ul>
	<li>
		$X$ is called <i>compact metric space</i>
if every collection of closed sets with empty intersection
contains finite subcollection with empty intersection

	</li>
	</ul>

</li>
<li>
	thus, $X$ is compact if and only if
every collection of closed sets with <i>finite intersection property</i>
has nonempty intersection

</li>
</ul>

<h3>Bolzano-Weierstrass property and sequential compactness</h3>

<div id="page:bolzano-weierstrass-property-and-sequential-compactness"></div>
<ul>
<li>
	metric space said to
	<ul>
	<li>
		have <span class="define">Bolzano-Weierstrass property</span>
if every sequence has cluster point

	</li>
	<li>
		$X$ said to be <span class="define">sequentially compact</span>
if every sequence has convergent subsequence

	</li>
	</ul>

</li>
<li>
	<span class="fact-font">$X$ has Bolzano-Weierstrass property
\iaoi\
sequentially compact</span>


</li>
</ul>

<h3>Compact metric spaces - properties</h3>

<ul>
<li>
	following three statements about metric space are equivalent
<span class="fact-font">(not true for general topological sets)</span>
	<ul>
	<li>
		being compact

	</li>
	<li>
		having Bolzano-Weierstrass property

	</li>
	<li>
		being sequentially compact

	</li>
	</ul>

</li>
<li>
	compact metric spaces have corresponding to some of those of complete metric spaces
(compare with statements on page~<a href="#page:subspaces">here</a>)
	<ul>
	<li>
		every compact subset of metric space is closed <i>and bounded</i>

	</li>
	<li>
		every closed subset of compact metric space is compact

	</li>
	</ul>

</li>
<li>
	(will show above in following slides)

</li>
</ul>

<h3>Necessary condition for compactness</h3>

<div id="page:Necessary-condition-for-compactness"></div>
<ul>
<li>
	compact metric space is sequentially compact 

</li>
<li>
	equivalently, compact metric space has Bolzano-Weierstrass property
(page~<a href="#page:bolzano-weierstrass-property-and-sequential-compactness">here</a>)

</li>
</ul>

<h3>Necessary conditions for sequentially compactness</h3>

<div id="page:sequentially-compact-metric-spaces-facts"></div>
<ul>
<li>
	every continuity real-valued function on sequentially compact space
is <i>bounded and assumes its maximum and minimum</i>

</li>
<li>
	sequentially compact space is <i>totally bounded</i>

</li>
<li>
	every open covering of sequentially compact space
has <i>Lebesgue number</i>

</li>
</ul>

<h3>Sufficient conditions for compactness</h3>

<div id="page:Sufficient-conditions-for-compactness"></div>
<ul>
<li>
	metric space that is totally bounded and has Lebesgue number for every covering
is compact

</li>
</ul>

<h3>Borel-Lebesgue theorem</h3>

<div id="page:Borel-Lebesgue-theorem"></div>
<ul>
<li>
	conditions on
pages <a href="#page:Necessary-condition-for-compactness">here</a>,
<a href="#page:sequentially-compact-metric-spaces-facts">here</a>,
and
<a href="#page:Sufficient-conditions-for-compactness">here</a>
imply the following equivalent statements
	<ul>
	<li>
		$X$ is <i>compact</i>

	</li>
	<li>
		$X$ has <i>Bolzano-Weierstrass property</i>

	</li>
	<li>
		$X$ is <i>sequentially compact</i>

	</li>
	</ul>

</li>
<li>
	above called <span class="name-font">Borel-Lebesgue theorem</span>




</li>
<li>
	hence, can drop <i>sequentially</i> in every statement on page~<a href="#page:sequentially-compact-metric-spaces-facts">here</a>,
<i>i.e.</i>,
	<ul>
	<li>
		every continuity real-valued function on <span style="color: rgb(60,60,60);"><s>sequentially</s></span> compact space is <i>bounded and assumes its maximum and minimum</i>

	</li>
	<li>
		<span style="color: rgb(60,60,60);"><s>sequentially</s></span> compact space is <i>totally bounded</i>

	</li>
	<li>
		every open covering of <span style="color: rgb(60,60,60);"><s>sequentially</s></span> compact space
has <i>Lebesgue number</i>

	</li>
	</ul>

</li>
</ul>

<h3>Compact metric spaces - other facts</h3>

<div id="page:Compact-metric-spaces---other-facts"></div>
<ul>
<li>
	closed subset of compact space is compact

</li>
<li>
	compact subset of metric space is <i>closed and bounded</i>
	<ul>
	<li>
		hence, Heine-Borel theorem (page~<a href="#page:heine-borel-theorem">here</a>) implies

	</li>
	<li>
		 <span class="fact-font">set of $\reals$ is compact \iaoi\ closed and bounded</span>

	</li>
	</ul>

</li>
<li>
	metric space is compact if and only if it is complete and totally bounded
<div id="page:compac-complete-and-totally-bounded"></div>

</li>
<li>
	thus, <span class="eemph">compactness can be viewed as absolute type of closedness</span>
	<ul>
	<li>
		 refer to page~<a href="#page:Compact-spaces---facts">here</a> for exactly same comments for general topological spaces

	</li>
	</ul>

</li>
<li>
	continuous image of compact set is compact

</li>
<li>
	continuous mapping of compact metric space into metric space
is uniformly continuous

</li>
</ul>

<h3>Diagrams for relations among metric spaces</h3>


<div id="page:Necessary-and-sufficient-conditions-for-compactness"></div>
<ul>
<li>
	the figure
shows relations among metric spaces stated on pages
<a href="#page:sequentially-compact-metric-spaces-facts">here</a>,
<a href="#page:Sufficient-conditions-for-compactness">here</a>,
<a href="#page:Borel-Lebesgue-theorem">here</a>,
and
<a href="#page:compac-complete-and-totally-bounded">here</a>

</li>
</ul>










<div id="fig:diagrams---for---relations---among---metric---spaces"></div>



<h3>Baire category</h3>

<ul>
<li>
	do (more) deeply into certain aspects of complete metric spaces,

namely, <span class="define">Baire theory of category</span>




</li>
<li>
	subset $E$ in metric space where $\sim (\closure{E})$ is dense,
said to be <span class="define">nowhere dense</span>

	<ul>
	<li>
		equivalently, $\closure{E}$ contains no nonempty open set

	</li>
	</ul>

</li>
<li>
	union of countable collection of <i>nowhere open sets</i>,
said to be <span class="define">of first category or meager</span>



</li>
<li>
	set not of first category, said to be <span class="define">of second category or nonmeager</span>



</li>
<li>
	complement of set of first category, called <span class="define">residual or co-meager</span>



</li>
</ul>

<h3>Baire category theorem</h3>

<ul>
<li>
	<span class="name-font">Baire theorem -</span>


<div id="page:Baire-theorem"></div>
for complete metric space, $X$,
and countable collection of dense open subsets, $\seq{O_k}\subset X$,
the intersection of the collection

$$

\bigcap O_k

$$

is dense
	<ul>
	<li>
		 refer to page~<a href="#page:locally-compact-space-version-of-Baire-theorem">here</a>
for locally compact space version of Baire theorem

	</li>
	</ul>

</li>
<li>
	<span class="name-font">Baire category theorem -</span>



no nonempty open subset of complete metric space
is of first category,
<i>i.e.</i>,
union of countable collection of nowhere dense subsets

</li>
<li>
	Baire category theorem is <i>unusual</i> in that
<i>uniform property, \ie, completeness of metric spaces,
implies purely topological nature</i>&nbsp;(footnote &ndash; 
&ldquo;no nonempty open subset of complete metric space is of first category&rdquo;
is purely topological nature
because if two spaces are (topologically) homeomorphic,
and no nonempty open subsets of one space is of first category,
then neither is any nonempty open subset of the other space
)

</li>
</ul>

<h3>Second category everywhere</h3>


<ul>
<li>
	metric or topological spaces with property that
&ldquo;no nonempty open subset of complete metric space is of first category'',
said to be <span class="define">of second category everywhere</span>
(with respect to themselves)


</li>
<li>
	Baire category theorem says <i>complete metric space</i> is of second category everywhere


</li>
<li>
	locally compact Hausdorff spaces are of second category everywhere, too
(refer to page~<a href="#page:Locally-compact-Hausdorff-spaces">here</a> for definition of locally compact Hausdorff spaces)

	<ul>
	<li>
		for these spaces, though, many of results of category theory
follow directly from <i>local compactness</i>

	</li>
	</ul>

</li>
</ul>

<h3>Sets of first category</h3>


<ul>
<li>
	collection of sets with following properties, called <span class="define">a $\sigma$-ideal of sets</span>


	<ul>
	<li>
		countable union of sets in the collection is, again, in the collection

	</li>
	<li>
		subset of any in the collection is, again, in the collection

	</li>
	</ul>

</li>
<li>
	both of below collections are $\sigma$-ideal of sets
	<ul>
	<li>
		sets of first category in topological space

	</li>
	<li>
		measure zero sets in complete measure space

	</li>
	</ul>

</li>
<li>
	sets of first category regards as &ldquo;small'' sets

	<ul>
	<li>
		such sets in complete metric spaces no interior points

	</li>
	</ul>

</li>
<li>
	interestingly!
set of first category in $[0,1]$
can have Lebesgue measure $1$,
hence complement of which is residual set of measure zero

</li>
</ul>

<h3>Some facts of category theory</h3>

<ul>
<li>
	for open set, $O$, and closed set, $F$,
$\closure{O}\sim O$ and $F\sim \interior{F}$ are nowhere dense

</li>
<li>
	closed set of first category in complete metric space is nowhere dense

</li>
<li>
	subset of complete metric space is residual if and only if contains dense $G_\delta$,
hence
subset of complete metric space is of first category if and only if contained in $F_\sigma$
whose complement is dense

</li>
<li>
	for countable collection of closed sets, $\seq{F_n}$,
$\bigcup \interior{F_n}$ is residual open set;
if $\bigcup F_n$ is complete metric space,
$O$ is dense

</li>
<li>
	some applications of category theory to analysis
seem almost too good to be belived;
here's one:

</li>
<li>
	<span class="name-font">uniform boundedness principle -</span>
for family, $\collF$, of real-valued continuous functions on complete metric space, $X$,
with property that $(\forall x\in X)(\exists M_x\in\reals)(\forall f\in\collF)(|f(x)|\leq M_x)$

$$

(\exists \mbox{ open }O, M\in\reals)(\forall x\in O, f\in\collF)(|f(x)|\leq M)

$$


</li>
</ul>

<h2 id="title-page:topological-spaces">Topological Spaces</h2>



<h3>Motivation for topological spaces</h3>



<ul>
<li>
	want to have something like
	<ul>
	<li>
		notion of open set is fundamental

	</li>
	<li>
		other notions defined in terms of open sets

	</li>
	<li>
		more general than metric spaces

	</li>
	</ul>

</li>
<li>
	why not stick to metric spaces?
	<ul>
	<li>
		certain notions have natural meaning
<i>not</i> consistent with topological concepts
derived from metric spaces
		<ul>
		<li>
			 <i>e.g.</i>. weak topologies in Banach spaces

		</li>
		</ul>

	</li>
	</ul>

</li>
</ul>

<h3>Topological spaces</h3>


<ul>
<li>
	$\topos{X}{J}$ with nonempty set $X$ of points and family $\tJ$ of subsets,
which we call open, having the following properties
called
<span class="define">topological spaces</span>

	<ul>
	<li>
		$\emptyset, X\in\tJ$

	</li>
	<li>
		$O_1, O_2 \in\tJ \Rightarrow O_1 \cap O_2 \in\tJ$

	</li>
	<li>
		$O_\alpha \Rightarrow \cup_\alpha O_\alpha \in \tJ$

	</li>
	</ul>

</li>
<li>
	family, $\tJ$, is called <span class="define">topology</span>



</li>
<li>
	for $X$, <i>always exist two topologies</i> defined on $X$
	<ul>
	<li>
		<span class="define">trivial topology</span> having only $\emptyset$ and $X$




	</li>
	<li>
		<span class="define">discrete topology</span> for which every subset of $X$ is an open set




	</li>
	</ul>

</li>
</ul>

<h3>Topological spaces associated with metric spaces</h3>

<ul>
<li>
	can associate topological space, $\topos{X}{J}$, to any metric space $\metrics{X}{\rho}$
where $\tJ$ is family of open sets in $\metrics{X}{\rho}$
	<ul>
	<li>
		because properties in definition of topological space
satisfied by open sets in metric space

	</li>
	</ul>

</li>
<li>
	$\topos{X}{J}$ assiaciated with metric space, $\metrics{X}{\rho}$ said to be <span class="define">metrizable</span>
	<ul>
	<li>
		$\rho$ called <span class="define">metric for</span> $\tXJ$

	</li>
	</ul>

</li>
<li>
	distinction between metric space and associated topological space is <i>essential</i>
	<ul>
	<li>
		because different metric spaces associate same topological space

	</li>
	<li>
		in this case, these metric spaces are equivalent

	</li>
	</ul>

</li>
<li>
	metric and topological spaces are couples

</li>
</ul>

<h3>Some definitions for topological spaces</h3>

<ul>
<li>
	subset $F\subset X$ with $\compl{F}$ is open called <span class="define">closed</span>

</li>
<li>
	intersection of all closed sets containing $E\subset X$ called <span class="define">closure</span> of $E$ denoted by $\closure{E}$
	<ul>
	<li>
		 $\closure{E}$ is smallest closed set containing $E$

	</li>
	</ul>

</li>
<li>
	$x\in X$ called <span class="define">point of closure</span> of $E\subset X$
if every open set containing $x$ meets $E$,
<i>i.e.</i>, has nonempty intersection with $E$

</li>
<li>
	union of all open sets contained in $E\subset X$ is called <span class="define">interior</span> of $E$ denoted by $\interior{E}$

</li>
<li>
	$x\in X$ called <i>interior point</i> of $E$ if exists open set, $E$, with $x\in O\subset E$

</li>
</ul>

<h3>Some properties of topological spaces</h3>

<ul>
<li>
	$\emptyset$, $X$ are closed

</li>
<li>
	union of closed sets is closed

</li>
<li>
	intersection of any collection of closed sets is closed

</li>
<li>
	$E\subset \closure{E}$, $\closure{\closure{E}} = \closure{E}$, $\closure{A\cup B} = \closure{A} \cup \closure{B}$

</li>
<li>
	$F$ closed if and only if $\closure{F}=F$

</li>
<li>
	$\closure{E}$ is set of <i>points of closure</i> of $E$

</li>
<li>
	$\interior{E}\subset E$, $\interior{(\interior{E})} = \interior{E}$, $\interior{(A\cup B)} = \interior{A} \cup \interior{B}$

</li>
<li>
	$\interior{E}$ is set of <i>interior points</i> of $E$

</li>
<li>
	$\interior{(\compl{E})} = \sim \closure{E}$

</li>
</ul>

<h3>Subspace and convergence of topological spaces</h3>

<ul>
<li>
	for subset of $\topos{X}{J}$, $A$,
define <span class="define">topology \tS\ for</span> $A$
with $\tS = \set{A\cap O}{O \in \tJ}$
	<ul>
	<li>
		$\tS$ called <span class="define">topology inherited from \tJ</span>

	</li>
	<li>
		$\topos{A}{S}$ called <span class="define">subspace</span> of $\topos{X}{J}$

	</li>
	</ul>

</li>
<li>
	$\seq{x_n}$ said to <span class="define">converge</span> to $x\in X$ if

$$

(\forall O \in \tJ \mbox{ containing } x)(\exists N\in\naturals)(\forall n>N)(x_n \in O)

$$

	<ul>
	<li>
		denoted by

$$

\lim x_n = x

$$


	</li>
	</ul>

</li>
<li>
	$\seq{x_n}$ said to have $x\in X$ as <span class="define">cluster point</span> if

$$

(\forall O \in\tJ\mbox{ containing } x, N\in\naturals)(\exists n>N)(x_n \in O)

$$


</li>
<li>
	$\seq{x_n}$ has converging subsequence to $x\in X$, then $x$ is cluster point of $\seq{x_n}$
	<ul>
	<li>
		converse is <i>not</i> true for arbitrary topological space

	</li>
	</ul>

</li>
</ul>

<h3>Continuity in topological spaces</h3>

<ul>
<li>
	mapping $f:X\to Y$ with $\topos{X}{J}$, $\topos{Y}{S}$ said to be <span class="define">continuous</span> if

$$

(\forall O\in \tS)(f^{-1}(O) \in \tJ)

$$


</li>
<li>
	$f:X \to Y$ said to be <span class="define">continuous at</span> $x\in X$ if

$$

(\forall O\in\tS\mbox{ containing } f(x))(\exists U\in\tJ\mbox{ containing } x)(f(U)\subset O)

$$


</li>
<li>
	$f$ is continuous if and only if $f$ is continuous at every $x\in X$

</li>
<li>
	for continuous $f$ on $\topos{X}{J}$, restriction $g$ on $A\subset X$ is continuous


</li>
<li>
	for $A$ with $A=A_1 \cup A_2$ where both $A_1$ and $A_2$ are either open or closed,
$f:A\to Y$ with each of both restrictions, $\restrict{f}{A_1}$ and $\restrict{f}{A_2}$, continuous,
is continuous

</li>
</ul>

<h3>Homeomorphism for topological spaces</h3>

<ul>
<li>
	one-to-one continuous function of $X$ onto $Y$, $f$, with continuous inverse function, $f^{-1}$,
called <span class="define">homeomorphism</span> between $\topos{X}{J}$ and $\topos{Y}{S}$

</li>
<li>
	$\topos{X}{J}$ and $\topos{Y}{S}$ said to be <span class="define">homeomorphic</span> if exists homeomorphism between them

</li>
<li>
	homeomorphic spaces are indistinguishable where homeomorphism amounting to relabeling of points
(from abstract pointp of view)

</li>
<li>
	thus, below roles are same
	<ul>
	<li>
		role that <i>homeomorphism plays for topological spaces</i>

	</li>
	<li>
		role that <i>isometry plays for metric spaces</i>

	</li>
	<li>
		role that <i>isomorphism plays for algebraic systems</i>

	</li>
	</ul>

</li>
</ul>

<h3>Stronger and weaker topologies</h3>

<div id="page:topological-spaces-stronger-and-weaker-topologies"></div>
<ul>
<li>
	for two topologies, $\tJ$ and $\tS$ for same $X$ with $\tS\supset\tJ$
	<ul>
	<li>
		$\tS$ said to be <span class="define">stronger or finer</span> than $\tJ$

	</li>
	<li>
		$\tJ$ said to be <span class="define">weaker or coarser</span> than $\tS$

	</li>
	</ul>

</li>
<li>
	$\tS$ is stronger than $\tJ$ if and only if identity mapping of $\topos{X}{S}$ to $\topos{Y}{J}$ is continuous

</li>
<li>
	for two topologies, $\tJ$ and $\tS$ for same $X$, $\tJ\cap\tS$ also topology

</li>
<li>
	for any collection of topologies, $\{\tJ_\alpha\}$ for same $X$,
$\cap_\alpha \tJ_\alpha$ is topology

</li>
<li>
	for nonempty set, $X$, and any collection of subsets of $X$, $\coll$
	<ul>
	<li>
		<span class="fact-font">exists weakest topology containing \coll,</span> <i>i.e.</i>, weakest topology where all subsets in $\coll$ are open

	</li>
	<li>
		it is intersection of all topologies containing $\coll$

	</li>
	</ul>

</li>
</ul>

<h3>Bases for topological spaces</h3>

<ul>
<li>
	collection $\collB$ of open sets of $\tXJ$
called <span class="define">a base for topology,</span> $\tJ$, of $X$
if

$$

(\forall O\in \tJ, x\in O)(\exists B\in\collB)(x\in B\subset O)

$$


</li>
<li>
	collection $\collB_x$ of open sets of $\tXJ$ containing $x$ called <span class="define">a base at</span> $x$
if

$$

(\forall O\in\tJ \mbox{ containing }x)(\exists B\in\collB_x)(x\in B\subset O)

$$

	<ul>
	<li>
		elements of $\collB_x$ often called <span class="define">neighborhoods of</span> $x$

	</li>
	<li>
		when no base given, <span class="define">neighborhood of</span> $x$ is an open set containing $x$

	</li>
	</ul>

</li>
<li>
	thus, $\collB$ of open sets is a base if and only if contains a base for every $x\in X$

</li>
<li>
	for topological space that is also metric space
	<ul>
	<li>
		all balls from a base

	</li>
	<li>
		balls centered at $x$ form a base at $x$

	</li>
	</ul>

</li>
</ul>

<h3>Characterization of topological spaces in terms of bases</h3>

<ul>
<li>
	<i>definition of open sets in terms of base</i> - when $\collB$ is base of $\tXJ$

$$

(O\in\tJ) \Leftrightarrow (\forall x\in O)(\exists B\in\collB)(x\in B\subset O)

$$


</li>
<li>
	often, convenient to specify topology for $X$ by
	<ul>
	<li>
		specifying a base of open sets, $\collB$, and

	</li>
	<li>
		using above criterion to define open sets

	</li>
	</ul>

</li>
<li>
	collection of subsets of $X$, $\collB$, is base for some topology if and only if

$$
\begin{eqnarray*}

&(\forall x\in X)(\exists B\in\collB)(x\in B)&
\\
&\mbox{and}&
\\
&(\forall x\in X, B_1, B_2 \in \collB \mbox{ with } x\in B_1\cap B_2)
(\exists B_3\in \collB)(x\in B_3 \subset B_1\cap B_2)&

\end{eqnarray*}
$$

	<ul>
	<li>
		<i>condition of collection to be basis for some topology</i>

	</li>
	</ul>

</li>
</ul>

<h3>Subbases for topological spaces</h3>

<ul>
<li>
	for $\tXJ$, collection of open sets, $\coll$, called <span class="define">a subbase</span> for topology $\tJ$
if

$$

(\forall O\in \tJ, x\in O)(\exists \seq{C_i}_{i=1}^n\subset\coll)(x\in \cap C_i \subset O)

$$

	<ul>
	<li>
		sometimes convenient to define topology in terms of subbase

	</li>
	</ul>

</li>
<li>
	for subbase for $\tJ$, $\coll$, collection of finite intersections of sets from $\coll$
forms base for $\tJ$

</li>
<li>
	any collection of subsets of $X$ is subbase for weakest topology
where sets of the collection are open

</li>
</ul>

<h3>Axioms of countability</h3>


<div id="page:topological-spaces-axioms-of-countability"></div>
<ul>
<li>
	topological space said to satisfy <span class="define">first axiom of countability</span>

if
exists countable base at every point
	<ul>
	<li>
		every metric space satisfies first axiom of countability
because for every $x\in X$, set of balls centered at $x$ with rational radii
forms base for $x$

	</li>
	</ul>

</li>
<li>
	topological space said to satisfy <span class="define">second axiom of countability</span>

if
exists countable base for the space
	<ul>
	<li>
		every metric space satisfies second axiom of countability
if and only if separable (refer to page~<a href="#page:dense-sets-and-separability-metric-spaces">here</a> for definition of separability)



	</li>
	</ul>

</li>
</ul>

<h3>Topological spaces - facts</h3>

<ul>
<li>
	given base, $\collB$, for $\tXJ$
	<ul>
	<li>
		$x \in \closure{E}$ if and only if $(\exists B\in\collB)(x\in B \ \&\ B\cap E \neq \emptyset)$

	</li>
	</ul>

</li>
<li>
	given base at $x$ for $\tXJ$, $\collB_x$, and base at $y$ for $\topos{Y}{S}$, $\topol{C}_y$
	<ul>
	<li>
		$f:X\to Y$ continuous at $x$ if and only if
$
(\forall C\in\topol{C}_y)(\exists B\in\collB_x)(B\subset f^{-1}(C))
$

	</li>
	</ul>

</li>
<li>
	if $\tXJ$ satisfies <i>first axiom of countability</i>

	<ul>
	<li>
		$x \in \closure{E}$ if and only if $(\exists \seq{x_n} \mbox{ from } E)(\lim x_n = x)$

	</li>
	<li>
		$x$ cluster point of $\seq{x_n}$ if and only if exists its subsequence converging to $x$

	</li>
	</ul>

</li>
<li>
	$\tXJ$ said to be <span class="define">Lindelo&#776;f space</span>
or have <span class="define">Lindelo&#776;f property</span>
if
every open covering of $X$ has countable subcover

</li>
<li>
	second axiom of countability implies <span class="define">Lindelo&#776;f property</span>


</li>
</ul>

<h3>Separation axioms</h3>

<ul>
<li>
	why separation axioms
	<ul>
	<li>
		properties of topological spaces are (in general) quite different from those of metric spaces

	</li>
	<li>
		often convenient assume additional conditions true in metric spaces

	</li>
	</ul>

</li>
<li>
	separation axioms

	<ul>
	<li>
		<span class="define">$T_1$ - Tychonoff spaces</span>
		<ul>
		<li>
			 $$
\begin{eqnarray*}
 &&(\forall x \neq y \in X) 
\\
&&(\exists \mbox{ open }O\subset X) 
\\
&&(y \in O, x \not\in O)
\end{eqnarray*}
$$

		</li>
		</ul>

	</li>
	<li>
		<span class="define">$T_2$ - Hausdorff spaces</span>
		<ul>
		<li>
			 $$
\begin{eqnarray*}
 &&(\forall x \neq y \in X) 
\\
&&(\exists \mbox{ open }O_1, O_2\subset X \mbox{ with } O_1\cap O_2=\emptyset) 
\\
&&(x \in O_1, y \in O_2) 
\end{eqnarray*}
$$

		</li>
		</ul>

	</li>
	<li>
		<span class="define">$T_3$ - regular spaces</span>
		<ul>
		<li>
			 $T_1$ &amp;
$$
\begin{eqnarray*}
 &&(\forall \mbox{ closed } F \subset X, x \not\in F)

\\
&&(\exists \mbox{ open }O_1, O_2\subset X \mbox{ with } O_1\cap O_2=\emptyset)

\\
&&(x \in O_1, F \subset O_2)
\end{eqnarray*}
$$

		</li>
		</ul>

	</li>
	<li>
		<span class="define">$T_4$ - normal spaces</span>
		<ul>
		<li>
			 $T_1$ &amp;
$$
\begin{eqnarray*}
 &&(\forall \mbox{ closed } F_1, F_2 \subset X)

\\
&&(\exists \mbox{ open }O_1, O_2\subset X \mbox{ with } O_1\cap O_2=\emptyset)

\\
&&(F_1 \subset O_1, F_2 \subset O_2)
\end{eqnarray*}
$$

		</li>
		</ul>

	</li>
	</ul>

</li>
</ul>

<h3>Separation axioms - facts</h3>

<ul>
<li>
	necessary and sufficient condition for $T_1$
	<ul>
	<li>
		topological space satisfies $T_1$ if and only if every singletone, $\{x\}$, is closed

	</li>
	</ul>

</li>
<li>
	important consequences of normality, $T_4$
	<ul>
	<li>
		<span class="name-font">Urysohn's lemma -</span> for normal topological space, $X$
$$
\begin{eqnarray*}

&&(\forall \mbox{ disjoint closed } A, B \subset X)

\\
&&(\exists f\in C(X,[0,1]))

\\
&&(f(A) = \{0\}, f(B) = \{1\})

\end{eqnarray*}
$$

	</li>
	<li>
		<span class="name-font">Tietze's extension theorem -</span> for normal topological space, $X$
$$
\begin{eqnarray*}

&&(\forall \mbox{ closed } A \subset X, f\in C(A,\reals))

\\
&&(\exists g \in C(X,\reals))

\\
&&(\forall x \in A)
(g(x) = f(x))

\end{eqnarray*}
$$

	</li>
	<li>
		<span class="name-font">Urysohn metrization theorem -</span>
<i>normal</i> topological space satisfying <i>second axiom of countability</i>
is <i>metrizable</i>

	</li>
	</ul>

</li>
</ul>

<h3>Weak topology generated by functions</h3>

<ul>
<li>
	given any set of points, $X$ &amp; any collection of functions of $X$ into $\reals$, $\collk{F}$,
exists weakest totally on $X$ such that
all functions in $\collk{F}$ is continuous
	<ul>
	<li>
		it is weakest topology containing
- refer to page~<a href="#page:topological-spaces-stronger-and-weaker-topologies">here</a>

$$

\coll\ = \bigcup_{f\in\collk{F}} \bigcup_{O\subset \reals} f^{-1}(O)

$$


	</li>
	<li>
		called <span class="define">weak topology generated by</span> $\collk{F}$

	</li>
	</ul>

</li>
</ul>





<h3>Complete regularity</h3>

<ul>
<li>
	for $\tXJ$ and continuous function collection $\collk{F}$,
<i>weak topology</i> generated by $\collk{F}$ is weaker than $\tJ$
	<ul>
	<li>
		however, if

$$

(\forall \mbox{ closed } F\subset X, x \not\in F)(\exists f\in\collk{F})(f(A)=\{0\}, f(x)=1)

$$

then, <i>weak topology generated by</i> $\collk{F}$ coincides with $\tJ$

	</li>
	<li>
		if condition satisfied by $\collk{F} = C(X,\reals)$,
$X$ said to be <span class="define">completely regular</span>
provided $X$ satisfied $T_1$ (Tychonoff space)

	</li>
	</ul>

</li>
<li>
	every normal topological ($T_4$) space is completely regular (Urysohn's lemma)

</li>
<li>
	every completely regular space is regular space ($T_3$)

</li>
<li>
	complete regularity sometimes called <span class="define">$T_{3\frac{1}{2}}$</span>

</li>
</ul>

<h3>Diagrams for separation axioms for topological spaces</h3>


<div id="page:Diagram-for-separation-axioms"></div>
<ul>
<li>
	the figure
shows $T_4 \Rightarrow T_{3\frac{1}{2}} \Rightarrow T_3 \Rightarrow T_2 \Rightarrow T_1$

</li>
<li>
	every metric spaces is normal space

</li>
</ul>











<div id="fig:diagrams---for---separation---axioms---for---topological---spaces"></div>




<h3>Topological spaces of interest</h3>

<ul>
<li>
	very general topological spaces quite bizarre
	<ul>
	<li>
		do <span class="eemph">not</span> seem to be much needed in analysis

	</li>
	</ul>

</li>
<li>
	only topological spaces (Royden) found useful for analysis are
	<ul>
	<li>
		metrizable topological spaces

	</li>
	<li>
		locally compact Hausdorff spaces




	</li>
	<li>
		topological vector spaces

	</li>
	</ul>

</li>
<li>
	all above are <i>completely regular</i>


</li>
<li>
	algebraic geometry, however, uses Zariski topology on affine or projective space,
topology giving us compact $T_1$ space which is not Hausdorff

</li>
</ul>

<h3>Connectedness</h3>

<ul>
<li>
	topological space, $X$,said to be <span class="define">connected</span> if <i>not</i> exist two nonempty disjoint open sets, $O_1$ and $O_2$,
such that $O_1\cup O_2 = X$
	<ul>
	<li>
		such pair, $(O_1, O_2)$, if exist, called <span class="define">separation of</span> $X$

	</li>
	<li>
		pair of disjoint nonempty closed sets, $(F_1,F_2)$, with $F_1\cup F_2=X$
is also <span class="define">separation of</span> $X$ - because they are also open

	</li>
	</ul>

</li>
<li>
	$X$ is connected if and only if only subsets that are both closed and open are $\emptyset$ and $X$

</li>
<li>
	subset $E\subset X$ said to be <span class="define">connected</span>
if connected in topology inherited from $\tXJ$
	<ul>
	<li>
		thus, $E$ is connected if not exist two nonempty open sets, $O_1$ and $O_2$,
such that $E\subset O_1\cup O_2$ and $E\cap O_1\cap O_2 = \emptyset$

	</li>
	</ul>

</li>
</ul>

<h3>Properties of connected space, component, and local connectedness</h3>

<ul>
<li>
	if exists continuous mapping of connected space to topological space, $Y$, $Y$ is connected

</li>
<li>
	<span class="name-font">(generalized version of) intermediate value theorem -</span> for $f:X\to\reals$ where $X$ is connected

$$

(\forall x, y \in X, c\in \reals \mbox{ with } f(x) < c < f(y))(\exists z \in X)(z=f(z))

$$


</li>
<li>
	subset of $\reals$ is connected if and only if is either interval or singletone

</li>
<li>
	for $x\in X$, union of all connected sets containing $x$ is called <span class="define">component</span>
	<ul>
	<li>
		component is <i>connected and closed</i>

	</li>
	<li>
		two components containing same point coincide

	</li>
	<li>
		thus, <span class="fact-font">$X$ is disjoint union of components</span>

	</li>
	</ul>

</li>
<li>
	$X$ said to be <span class="define">locally connected</span> if exists base for $X$ consisting of connected sets
	<ul>
	<li>
		components of locally connected space are <i>open</i>

	</li>
	<li>
		space <i>can be connected, but not locally connected</i>

	</li>
	</ul>

</li>
</ul>

<h3>Product topological spaces</h3>


<ul>
<li>
	for $\tXJ$ and $\topos{Y}{S}$, topology on $X\times Y$ taking as <i>a base</i> the following

$$

\set{O_1 \times O_2}{O_1 \in \tJ, O_2 \in \topol{S}}

$$


</li>
<li>
	 called <span class="define">product topology</span> for $X\times Y$

	<ul>
	<li>
		for metric spaces, $X$ and $Y$, <i>product topology is product metric</i>

	</li>
	</ul>

</li>
<li>
	for indexed family with index set, $\collk{A}$,
$\topos{X_\alpha}{\tJ_\alpha}$, product topology on $\bigtimes_{\alpha\in\collk{A}} X_{\alpha}$
defined as taking as <i>a base</i> the following

$\bigsetl{\bigtimes X_\alpha}{O_\alpha\in \tJ_\alpha, O_\alpha = X_\alpha \mbox{ except finite number of }\alpha}$


</li>
<li>
	$\pi_\alpha: \bigtimes X_{\alpha} \to X_\alpha$ with $\pi_\alpha(y) = x_\alpha$,
<i>i.e.</i>, $\alpha$-th coordinate, called <span class="define">projection</span>

	<ul>
	<li>
		every $\pi_\alpha$ continuous

	</li>
	<li>
		$\bigtimes X_\alpha$ <i>weakest topology</i> with continuous $\pi_\alpha$'s

	</li>
	</ul>

</li>
<li>
	if $(\forall \alpha\in\collk{A})(X_\alpha=X)$, $\bigtimes X_{\alpha}$ denoted by <span class="notation">$X^\collk{A}$</span>

</li>
</ul>

<h3>Product topology with countable index set</h3>

<div id="page:product-topology-with-countable-index-set"></div>
<ul>
<li>
	for countable $\collk{A}$

	<ul>
	<li>
		$\bigtimes X_\alpha$ <i>denoted by</i> <span class="notation">$X^\omega$</span> or <span class="notation">$X^\naturals$</span>
$\because$ only # elements of $\collk{A}$ important
		<ul>
		<li>
			 <i>e.g.</i>, $\textbf{2}^\omega$ is <i>Cantor set</i> if denoting discrete topology with two elements by $\textbf{2}$

		</li>
		</ul>

	</li>
	</ul>

</li>
<li>
	if $X$ is metrizable, $X^\omega$ is metrizable


</li>
<li>
	<span class="fact-font">$\naturals^\omega = \naturals^\naturals$ is topology space homeomorphic to $\reals\sim\rationals$</span>
when denoting discrete topology with countable set also by $\naturals$


</li>
</ul>

<h3>Product topologies induced by set and continuous functions</h3>

<ul>
<li>
	for $I=[0,1]$, $I^\collk{A}$ called <span class="define">cube</span>

</li>
<li>
	$I^\omega$ is metrizable, and called <span class="define">Hilbert cube</span>

</li>
<li>
	for any set $X$ and any collection of $f:X\to[0,1]$, $\collk{F}$
with $(\forall x\neq y\in X)(\exists f\in\collk{F})(f(x)\neq f(y))$
	<ul>
	<li>
		can define <i>one-to-one mapping of \collk{F}\ into $I^X$</i>
with $f(x)$ as $x$-th coordinate of $f$
		<ul>
		<li>
			 $\pi_x: \collk{F} \to I$ (mapping of $\collk{F}$ into $I$) with $\pi_x(f) = f(x)$

		</li>
		<li>
			 topology that $\collk{F}$ inherits as subspace of $I^X$ called
<span class="define">topology of pointwise convergence</span>
(because $\pi_x$ is project, hence continuous)

		</li>
		</ul>

	</li>
	<li>
		can define <i>one-to-one mapping of $X$ into $I^\collk{F}$</i>
with $f(x)$ as $f$-th coordinate of $x$
		<ul>
		<li>
			 topology of $X$ as subspace of $I^\collk{F}$ is <i>weak topology generated by \collk{F}</i>

		</li>
		<li>
			 if every $f\in\collk{F}$ is continuous,
			<ul>
			<li>
				 topology of $X$ into $I^\collk{F}$ is continuous

			</li>
			<li>
				 if for every closed $F\subset X$ and for each $x\not\in F$,
exists $f\in\collk{F}$ such that $f(x)=1$ and $f(F)=\{0\}$,
then <i>$X$ is homeomorphic to image of $I^\collk{F}$</i>

			</li>
			</ul>

		</li>
		</ul>

	</li>
	</ul>

</li>
</ul>

<h2 id="title-page:Compact-and-Locally-Compact-Spaces">Compact and Locally Compact Spaces</h2>


<h3>Compact spaces</h3>

<ul>
<li>
	compactness for metric spaces (page~<a href="#page:Compact-metric-spaces">here</a>)
can be generalized to topological spaces
	<ul>
	<li>
		things are very much similar to those of metrics spaces

	</li>
	</ul>

</li>
<li>
	for subset $K\subset X$, collection of open sets, $\openconv$, the union of which $K$ is contained in
called <span class="define">open covering</span> of $K$

</li>
<li>
	topological space, $X$, said to be <span class="define">compact</span> if every open convering of contains finite subcovering

</li>
<li>
	$K\subset X$ said to be <span class="define">compact</span> if compact as subspace of $X$
	<ul>
	<li>
		or equivalently, $K$ is compact if every covering of $K$ <i>by open sets of $X$</i>
has finite subcovering

	</li>
	<li>
		thus, Heine-Borel (page~<a href="#page:heine-borel-theorem">here</a>) says every closed and bounded subset of $\reals$
is compact

	</li>
	</ul>

</li>
<li>
	for $\collk{F}\subset\powerset(X)$ any finite subcollection of which has nonempty intersection
called <span class="define">finite intersection property</span>

</li>
<li>
	thus, topological space compact if and only if every collection with <i>finite intersection property</i>
has nonempty intersection

</li>
</ul>

<h3>Compact spaces - facts</h3>

<div id="page:Compact-spaces---facts"></div>
<ul>
<li>
	<span class="eemph">compactness can be viewed as absolute type of closedness</span> because
	<ul>
	<li>
		closed subset of compact space is compact

	</li>
	<li>
		compact subset of Hausdorff space is closed


	</li>
	</ul>

</li>
<li>
	 refer to page~<a href="#page:Compact-metric-spaces---other-facts">here</a> for exactly the same comments for metric spaces

</li>
<li>
	thus, every compact set of $\reals$ is closed and bounded

</li>
<li>
	continuous image of compact set is compact

</li>
<li>
	one-to-one continuous mapping of compact space into Hausdorff space is homeomorphism


</li>
</ul>

<h3>Refinement of open covering</h3>

<ul>
<li>
	for open covering of $X$, $\openconv$, open covering of $X$ every element of which is subset of element of $\openconv$,
called <span class="define">refinement</span> of $\openconv$ or said to <span class="define">refine</span> $\openconv$

</li>
<li>
	$X$ is cmopact if and only if every open covering has finite refinement

</li>
<li>
	any two open covers, $\openconv$ and $\collk{V}$, have common refinement, <i>i.e.</i>,

$$

\set{U\cap V}{U\in\openconv, V\in\collk{V}}

$$


</li>
</ul>

<h3>Countable compactness and Lindelo&#776;f</h3>

<div id="page:Countable-compactness-and-Lindelof"></div>
<ul>
<li>
	topological space for which every open covering has countable subcovering
said to be <span class="define">Lindelo&#776;f</span>

</li>
<li>
	topological space for which every countable open covering has finite subcovering
said to be <span class="define">countably compact</span> space

</li>
<li>
	thus, topological space is compact if and only if both Lindelo&#776;f and countably compact

</li>
<li>
	every second countable space is Lindelo&#776;f

</li>
<li>
	thus, countable compactness coincides with compactness if second countable
(<i>i.e.</i>, satisfying second axiom of countability)


</li>
<li>
	continuous image of compact countably compact space is countably compact

</li>
</ul>

<h3>Bolzano-Weierstrass property and sequential compactness</h3>

<div id="page:Bolzano-Weierstrass-property-and-sequential-compactness"></div>
<ul>
<li>
	topological space, $X$, said to have <span class="define">Bolzano-Weierstrass property</span>
if every sequence, $\seq{x_n}$, in $X$ has at least one cluster point,
<i>i.e.</i>,

$$

(\forall \seq{x_n})
(\exists x\in X)
(\forall \epsilon>0, N\in\naturals)
(\exists n>N, O\subset X)
(x\in O, O \mbox{ is open}, x_n \in O)

$$


</li>
<li>
	topological space has <i>Bolzano-Weierstrass properties</i> if and only if countably compact

</li>
<li>
	topological space said to be <span class="define">sequentially compact</span>
if every sequence has converging subsequence

</li>
<li>
	sequentially compact space is countably compact

</li>
<li>
	thus, Lindelo&#776;f coincides with compactness if sequentially compact

</li>
<li>
	countably compact and first countable (<i>i.e.</i>, satisfying first axiom of countability) space
is sequentially compact


</li>
</ul>

<h3>Diagrams for relations among topological spaces</h3>


<div id="page:Diagrams-for-relations-among-topological-spaces"></div>
<ul>
<li>
	the figure
shows relations among topological spaces stated on pages
<a href="#page:Countable-compactness-and-Lindelof">here</a>
and
<a href="#page:Bolzano-Weierstrass-property-and-sequential-compactness">here</a>

</li>
</ul>










<div id="fig:diagrams---for---relations---among---topological---spaces"></div>



<h3>Real-valued functions on topological spaces</h3>

<ul>
<li>
	continuous real-valued function on countably compact space
is bounded and assumes maximum and minimum

</li>
<li>
	$f:X\to\reals$ with topological space, $X$,
called <span class="define">upper semicontinuous</span>
if $\set{x\in X}{f(x)<\alpha}$ is open for every $\alpha \in \reals$

</li>
<li>
	stronger statement -
upper semicontinuous real-valued function on countably compact space
is bounded (from above) and assumes maximum

</li>
<li>
	<span class="name-font">Dini -</span>
for sequence of upper semicontinuous real-valued functions on countably compact space, $\seq{f_n}$,
with property that $\seq{f_n(x)}$ decreases monotonically to zero for every $x\in X$,
$\seq{f_n}$ converges to zero uniformly

</li>
</ul>

<h3>Products of compact spaces</h3>


<ul>
<li>
	<span class="fact-font">Tychonoff theorem - (probably) most important theorem in general topology</span>


</li>
<li>
	most applications in analysis need only special case of product of (closed) intervals,
but this special case does not seem to be easire to prove than general case, <i>i.e.</i>, Tychonoff theorem

</li>
<li>
	lemmas needed to prove Tychonoff theorem
	<ul>
	<li>
		for collection of subsets of $X$ with finite intersection property, $\collk{A}$,
exists collection $\collk{B}\supset\collk{A}$ with finite intersection property
that is maximal with respect to this property,
<i>i.e.</i>,
no collection with finite intersection property properly contains $\collk{B}$

	</li>
	<li>
		for collection, $\collk{B}$, of subsets of $X$
that is maximal with respect to finite intersection property,
each intersection of finite number of sets in $\collk{B}$ is again in $\collk{B}$
and
each set that meets each set in $\collk{B}$ is itself in $\collk{B}$

	</li>
	</ul>

</li>
<li>
	<span class="name-font">Tychonoff theorem -</span>


product space $\bigtimes X_\alpha$ is compact
for indexed family of compact topological spaces, $\seq{X_\alpha}$

</li>
</ul>

<h3>Locally compact spaces</h3>



<ul>
<li>
	topological space, $X$, with

$$

(\forall x\in X)(\exists \mbox{ open }O\subset X)(x\in O, \closure{O} \mbox{ is compact})

$$

called <span class="define">locally compact</span>



</li>
<li>
	topological space is locally compact
if and only if
set of all open sets with compact closures
forms base for the topological space


</li>
<li>
	every compact space is locally compact
	<ul>
	<li>
		but converse it <i>not</i> true
		<ul>
		<li>
			 <i>e.g.</i>, Euclidean spaces $\reals^n$ are locally compact,
but not compact

		</li>
		</ul>

	</li>
	</ul>

</li>
</ul>

<h3>Locally compact Hausdorff spaces</h3>



<div id="page:Locally-compact-Hausdorff-spaces"></div>
<ul>
<li>
	<i>locally compact Hausdorff spaces</i>


constitute one of most important classes of topological spaces

</li>
<li>
	so useful is combination of Hausdorff separation axioms in connection with compactness
that French usage (following Bourbaki) reserves term &lsquo;compact space'
for those compact and Hausdorff,
using term &lsquo;pseudocompact' for those not Hausdorff!

</li>
<li>
	following slides devote to establishing some of their basic properties


</li>
</ul>

<h3>Support and subordinateness</h3>

<ul>
<li>
	for function, $f$, on topological spaces,
closure of $\set{x}{f(x)\neq0}$,
called <span class="define">support</span> of $f$,
<i>i.e.</i>,

$$

\support f = \closure{\set{x}{f(x)\neq0}}

$$


</li>
<li>
	given covering $\indexedcol{O_\lambda}$ of $X$,
collection $\indexedcol{\varphi_\alpha}$ with $\varphi_\alpha:X\to\reals$
satisfying

$$

(\forall \varphi_\alpha)(\exists O_\lambda)(\support \varphi_\alpha \subset O_\lambda)

$$

said to be <span class="define">subordinate to</span> $\indexedcol{O_\lambda}$

</li>
</ul>

<h3>Some properties of locally compact Hausdorff spaces</h3>



<ul>
<li>
	for compact subset, $K$, of locally compact Hausdorff space, $X$
	<ul>
	<li>
		exists open subset with compact closure, $O\subset X$, containing $K$

	</li>
	<li>
		exists continuous nonnegative function, $f$, on $X$,
with

$$

(\forall x\in K)(f(x)=1) \mbox{ and } (\forall x\not\in O)(f(x)=0)

$$

if $K$ is $G_\delta$, may take $f<1$ in $\compl{K}$

	</li>
	</ul>

</li>
<li>
	for open covering, $\indexedcol{O_\lambda}$, for compact subset, $K$, of locally compact Hausdorff space,
exists $\seq{\varphi_i}_{i=1}^n \subset C(X,\preals)$ subordinate to $\indexedcol{O_\lambda}$
such that

$$

(\forall x \in K)(\varphi_1(x)+\cdots+\varphi_n(x) =1)

$$


</li>
</ul>

<h3>Local compactness and second Baire category</h3>


<ul>
<li>
	for locally compact space, $X$,
and countable collection of dense open subsets, $\seq{O_k}\subset X$,
the intersection of the collection

$$

\bigcap O_k

$$

is dense
<div id="page:locally-compact-space-version-of-Baire-theorem"></div>
	<ul>
	<li>
		analogue of Baire theorem for complete metric spaces
(refer to page~<a href="#page:Baire-theorem">here</a> for Baire theorem)

	</li>
	</ul>

</li>
<li>
	thus, <i>every locally compact space is locally of second Baire category with respect to itself</i>

</li>
</ul>

<h3>Local compactness, Hausdorffness, and denseness</h3>


<ul>
<li>
	for countable union, $\bigcup F_n$, of closed sets containing open subset, $O$, in locally compact space,
union of interiors, $\bigcup \interior{F_n}$, is
open set dense in $O$

</li>
<li>
	dense subset of Hausdorff space, $X$, which is locally compact in its subspace topology,
is open subset of $X$

</li>
<li>
	subset, $Y$, of locally compact Hausdorff space is locally compact in its subspace topology
if and only if
$Y$ is relatively open subset of $\closure{Y}$

</li>
</ul>

<h3>Alexandroff one-point compactification</h3>

<ul>
<li>
	for locally compact Hausdorff space, $X$,
can form $X^\ast$ by adding single point $\omega\not\in X$ to $X$
and take set in $X^\ast$ to be open
if it is either open in $X$ or complement of compact subset in $X$,
then
	<ul>
	<li>
		$X^\ast$ is compact Hausdorff spaces

	</li>
	<li>
		identity mapping of $X$ into $X^\ast$ is homeomorphism of $X$ and $X^\ast\sim\{\omega\}$

	</li>
	<li>
		$X^\ast$ called <span class="define">Alexandroff one-point compactification of $X$</span>




	</li>
	<li>
		$\omega$ often referred to as <span class="define">infinity in $X^\ast$</span>


	</li>
	</ul>

</li>
<li>
	continuous mapping, $f$, from topological space to topological space
inversely mapping compact set to compact set,
said to be <span class="define">proper</span>

</li>
<li>
	proper maps from locally compact Hausdorff space into locally compact Hausdorff space
are precisely those continuous maps of $X$ into $Y$
tha can be extended to continuous maps $f^\ast$ of $X^\ast$ into $Y^\ast$
by taking point at infinity in $X^\ast$ to point at infinity in $Y^\ast$


</li>
</ul>

<h3>Manifolds</h3>

<ul>
<li>
	connected Hausdorff space with each point having neighborhood homeomorphic to ball in $\reals^n$
called $n$-dimensional <span class="define">manifold</span>


</li>
<li>
	sometimes say manifold is connected Hausdorff space that is <i>locally Euclidean</i>

</li>
<li>
	thus, manifold has all local properties of Euclidean space;
particularly <i>locally compact and locally connected</i>

</li>
<li>
	neighborhood homeomorphic to ball called
<span class="define">coordinate neighborhood</span> or <span class="define">coordinate ball</span>

</li>
<li>
	pair $\pair{U}{\varphi}$ with coordinate ball, $U$, with homeomorphism from $U$ onto ball in $\reals^n$, $\varphi$,
called <span class="define">coodinate chart</span>;
$\varphi$ called <span class="define">coordinate map</span>

</li>
<li>
	coordinate (in $\reals^n$) of point, $x\in U$, under $\varphi$
said to be <span class="define">coordinate of $x$</span> in the chart

</li>
</ul>

<h3>Equivalent properties for manifolds</h3>

<ul>
<li>
	for manifold, $M$, the following are equivalent
	<ul>
	<li>
		$M$ is paracompact

	</li>
	<li>
		$M$ is $\sigma$-compact

	</li>
	<li>
		$M$ is Lindelo&#776;f

	</li>
	<li>
		every open cover of $M$ has star-finite open refinement

	</li>
	<li>
		exist sequence of open subsets of $M$, $\seq{O_n}$,
with $\closure{O_n}$ compact,
$\closure{O_n}\subset O_{n+1}$,
and
$M=\bigcup O_n$

	</li>
	<li>
		exists proper continuous map, $\varphi:M\to [0,\infty)$

	</li>
	<li>
		$M$ is second countable

	</li>
	</ul>

</li>
</ul>


<h2 id="title-page:Banach-Spaces">Banach Spaces</h2>


<h3>Vector spaces</h3>


<ul>
<li>
	set $X$ with $+:X\times X\to X$, $\cdot: \reals \times X\to X$
satisfying the following properties
called <span class="define">vector space</span> or <span class="define">linear space</span> or <span class="define">linear vector space</span> over $\reals$

$$
\begin{eqnarray*}

\mbox{- for all } x,y,z\in X \mbox{ and } \lambda, \mu \in \reals
\\
x+y= y+x	&& \mbox{- additive commutativity}
\\
(x+y)+z= x+(y+z)	&& \mbox{- additive associativity}
\\
(\exists 0\in X)\ x+0=x	&& \mbox{- additive identity}
\\
\lambda(x+y) = \lambda x + \lambda y	&& \mbox{- distributivity of multiplication over addition}
\\
(\lambda+\mu)x = \lambda x + \mu x	&& \mbox{- distributivity of multiplication over addition}
\\
\lambda(\mu x)= (\lambda \mu)x	&& \mbox{- multiplicative associativity}
\\
0\cdot x = 0\in X&&
\\
1\cdot x = x&&

\end{eqnarray*}
$$


</li>
</ul>

<h3>Norm and Banach spaces</h3>

<ul>
<li>
	$\|\cdot\|:X\to\preals$ with vector space, $X$, called <span class="define">norm</span> if


$$
\begin{eqnarray*}

\mbox{for all } x,y\in X \mbox{ and } \alpha \in \reals&
\\
\|x\| = 0 \Leftrightarrow x=0	&& \mbox{- positive definiteness / positiveness /point-separating}
\\
\|x+y\|\geq \|x\| + \|y\|	&& \mbox{- triangle inequality / subadditivity}
\\
\|\alpha x\| = |\alpha| \|x\|	&& \mbox{- Absolute homogeneity}

\end{eqnarray*}
$$



</li>
<li>
	<i>normed vector space</i> that is <i>complete metric space</i> with metric induced by norm,
<i>i.e.</i>, $\rho:X\times X \to \preals$ with $\rho(x,y)=\|x-y\|$,
called <span class="define">Banach space</span>




<div id="page:Banach---spaces"></div>
	<ul>
	<li>
		can be said to be class of spaces endowed with
both topological and algebraic structure

	</li>
	</ul>

</li>
<li>
	examples include
	<ul>
	<li>
		$L^p$ with $1\leq p\leq \infty$ (page~<a href="#page:Banach-space">here</a>),

	</li>
	<li>
		$C(X)=C(X,\reals)$, <i>i.e.</i>, space of all continuous real-valued functions on <i>compact</i> space, $X$

	</li>
	</ul>

</li>
</ul>

<h3>Properties of vector spaces</h3>

<ul>
<li>
	normed vector space is complete if and only if every absolutely summable sequence is summable

</li>
</ul>

<h3>Subspaces of vector spaces</h3>

<ul>
<li>
	nonempty subset, $S$, of vector space, $X$,
with $x,y\in S\Rightarrow \lambda x + \mu y\in S$,
called <span class="define">subspace</span> or <span class="define">linear manifold</span>

</li>
<li>
	intersection of any family of linear manifolds is linear manifold

</li>
<li>
	hence, for $A\subset X$,
exists smallest linear manifold containing $A$,
often denoted by <span class="notation">$\{A\}$</span>

</li>
<li>
	if $S$ is closed as subset of $X$, called <span class="define">closed linear manifold</span>

</li>
<li>
	some definitions
	<ul>
	<li>
		$A+x$ defined by $\set{y+x}{y\in A}$, called <span class="define">translate</span> of $A$ by $x$

	</li>
	<li>
		$\lambda A$ defined by $\set{\lambda x}{x \in A}$

	</li>
	<li>
		$A+B$ defined by $\set{x+y}{x \in A, y\in B}$

	</li>
	</ul>

</li>
</ul>

<h3>Linear operators on vector spaces</h3>

<ul>
<li>
	mapping of vector space, $X$, to another (possibly same) vector space
called
<span class="define">linear mapping</span>,
or
<span class="define">linear operator</span>,
or
<span class="define">linear transformation</span>
if

$$

(\forall x,y \in X, \alpha, \beta \in \reals)
(A(\alpha x + \beta y y) = \alpha (Ax) + \beta (Ay))

$$


</li>
<li>
	linear operator called <span class="define">bounded</span>
if

$$

(\exists M)
(\forall x \in X)
(\|Ax\|\leq M \|x\|)

$$


</li>
<li>
	least such bound called <span class="define">norm</span> of linear operator, <i>i.e.</i>,

$$

M
= \sup_{x\in X, x\neq 0} \|Ax\|/\|x\|

$$

	<ul>
	<li>
		linearity implies

$$

M = \sup_{x\in X, \|x\|= 1} \|Ax\| = \sup_{x\in X, \|x\|\leq 1} \|Ax\|

$$


	</li>
	</ul>

</li>
</ul>

<h3>Isomorphism and isometrical isomorphism</h3>

<ul>
<li>
	bounded linear operator from $X$ to $Y$ called <span class="define">isomorphism</span>
if exists bounded inverse linear operator,
<i>i.e.</i>,

$$

(\exists A:X\to Y, B:Y\to X)(AB \mbox{ and } BA \mbox{ are identity})

$$


</li>
<li>
	isomorphism between two normed vector spaces that preserve norms
called <span class="define">isometrical isomorphism</span>

</li>
<li>
	from abstract point of view,
isometrically isomorphic spaces are <i>identical</i>,
<i>i.e.</i>,
isometrical isomorphism merely amounts to <i>element renaming</i>

</li>
</ul>

<h3>Properties of linear operators on vector spaces</h3>

<div id="page:Properties-of-linear-operators"></div>
<ul>
<li>
	for linear operators, point continuity $\Rightarrow$ boundedness $\Rightarrow$ uniform continuity,
<i>i.e.</i>,
	<ul>
	<li>
		bounded linear operator is uniformly continuous

	</li>
	<li>
		linear operator continuous at one point is bounded

	</li>
	</ul>

</li>
<li>
	<span class="fact-font">space of all bounded linear operators from {normed vector space} to {Banach space}
is {Banach space}</span>


</li>
</ul>

<h3>Linear functionals on vector spaces</h3>

<ul>
<li>
	linear operator from vector space, $X$, to $\reals$
called <span class="define">linear functional</span>,
<i>i.e.</i>, $f:X\to\reals$ such that
for all $x,y\in X$ and $\alpha, \beta \in \reals$

$$

f(\alpha x + \beta y) = \alpha f(x) + \beta f(y)

$$


</li>
<li>
	want to extend linear functional from subspace to whole vector space
while preserving properties of functional

</li>
</ul>

<h3>Hahn-Banach theorem</h3>

<div id="page:Hahn-Banach-theorem"></div>
<ul>
<li>
	<span class="name-font">Hahn-Banach theorem -</span>
for <i>vector space</i>, $X$, and linear functional, $p:X \to \reals$ with

$$

(\forall x,y\in X, \alpha \geq0)
(p(x+y)\leq p(x) + p(y) \mbox{ and } p(\alpha x) = \alpha p(x))

$$

and for subspace of $X$, $S$, and linear functional, $f:S\to\reals$, with

$$

(\forall s \in S)
(f(s) \leq p(s))

$$

exists linear functional, $F:X\to\reals$, such that

$$

(\forall s \in S) ( F(s) = f(s))
\mbox{ and }
(\forall x \in X) (F(x) \leq p(x))

$$


</li>
<li>
	corollary - for normed vector space, $X$,
exists bounded linear functional, $f:X\to\reals$

$$

f(x) = \|f\|\|x\|

$$


</li>
</ul>

<h3>Dual spaces of normed spaces</h3>

<div id="page:Dual-of-normed-spaces"></div>
<ul>
<li>
	space of <i>bounded linear functionals</i> on <i>normed space</i>, $X$,
called <span class="define">dual</span> or <span class="define">conjugate</span> of $X$,
denoted by <span class="notation">$X^\ast$</span>





</li>
<li>
	every dual is Banach space (refer to page~<a href="#page:Properties-of-linear-operators">here</a>)

</li>
<li>
	dual of $L^p$ is (isometrically isomorphic to) $L^q$ for $1\leq p<\infty$
	<ul>
	<li>
		exists natural representation of bounded linear functional on $L^p$ by $L^q$
(by Riesz representation theorem on page~<a href="#page:Riesz-representation-theorem">here</a>)

	</li>
	</ul>

</li>
<li>
	<i>not</i> every bounded linear functionals on $L^\infty$ has natural representation


</li>
</ul>

<h3>Natural isomorphism</h3>

<div id="page:Natural-isomorphism"></div>
<ul>
<li>
	define linear mapping of normed space, $X$, to $X^{\ast\ast}$ (<i>i.e.</i>, dual of dual of $X$),
$\varphi:X\to X^{\ast\ast}$ such that for $x\in X$,
$
(
\forall f\in X^{\ast}
)
(
(\varphi (x))(f) = f(x)
)
$
	<ul>
	<li>
		then,
$
\|\varphi(x)\|
= \sup_{\|g\|=1, g\in X^\ast} g(x)
\leq \sup_{\|g\|=1, g\in X^\ast} \|g\|\|x\|
= \|x\|
$

	</li>
	<li>
		by corollary on page~<a href="#page:Hahn-Banach-theorem">here</a>, there exists
$f\in X^\ast$ such that $f(x)=\|x\|$,
then $\|f\|=1$, and $f(x)=\|x\|$, thus $\|\varphi(x)\| = \sup_{\|g\|=1, g\in X^\ast} g(x) \geq f(x) = \|x\|$

	</li>
	<li>
		thus, $\|\varphi(x)\| = \|x\|$,
hence $\varphi$ is isometrically isomorphic linear mapping of $X$ onto $\varphi(X)\subset X^{\ast\ast}$,
which is subspace of $X^{\ast\ast}$

	</li>
	<li>
		$\varphi$ called <span class="define">natural isomorphism</span> of $X$ into $X^{\ast\ast}$

	</li>
	<li>
		$X$ said to be <span class="define">reflexive</span> if $\varphi(X)=X^{\ast\ast}$

	</li>
	</ul>

</li>
<li>
	thus, $L^p$ with $1< p<\infty$ is reflexive, but $L^1$ and $L^\infty$ are not

</li>
<li>
	note $X$ may be isometric with $X^{\ast\ast}$ without reflexive

</li>
</ul>

<h3>Completeness of natural isomorphism</h3>


<div id="page:Completeness-of-natural-isomorphism"></div>
<ul>
<li>
	for natural isomorphism, $\varphi$

</li>
<li>
	$X^{\ast\ast}$ is complete, hence Banach space
	<ul>
	<li>
		because bounded linear functional to $\reals$ (refer to page~<a href="#page:Properties-of-linear-operators">here</a>)

	</li>
	</ul>

</li>
<li>
	thus, closure of $\varphi(X)$ in $X^{\ast\ast}$, $\closure{\varphi(X)}$, complete
(refer to page~<a href="#page:subspaces">here</a>)

</li>
<li>
	therefore, <span class="fact-font">every normed vector space ($X$)
is isometrically isomorphic to dense subset of Banach spaces ($X^{\ast\ast}$)</span>

</li>
</ul>

<h3>Hahn-Banach theorem - complex version</h3>

<ul>
<li>
	<span class="name-font">Bohnenblust and Sobczyk -</span>
for <i>complex</i> vector space, $X$, and linear functional, $p:X \to \reals$ with

$$

(
\forall x,y\in X, \alpha \in\complexes
)
(
p(x+y)\leq p(x) + p(y) \mbox{ and } p(\alpha x) = |\alpha| p(x)
)

$$

and for subspace of $X$, $S$, and (complex) linear functional, $f:S\to\complexes$, with

$$

(
\forall s \in S
)
(
|f(s)| \leq p(s)
)

$$

exists linear functional, $F:X\to\reals$, such that

$$

(
\forall s \in S
)
(
F(s) = f(s)
)

$$

and

$$

(
\forall x \in X
)
(
|F(x)| \leq p(x)
)

$$


</li>
</ul>

<h3>Open mapping on topological spaces</h3>

<ul>
<li>
	mapping from topological space to another topological space
the image of each open set by which is open
called <span class="define">open mapping</span>

</li>
<li>
	hence, one-to-one continuous open mapping is <i>homeomorphism</i>

</li>
<li>
	(will show)
continuous linear transformation of Banach space onto another Banach space
is
always open mapping

</li>
<li>
	(will)
use above to provide criteria
for continuity of linear transformation

</li>
</ul>

<h3>Closed graph theorem (on Banach spaces)</h3>

<ul>
<li>
	every continuous linear transformation of Banach space onto Banach space is open mapping
	<ul>
	<li>
		in particular, if the mapping is one-to-one, it is isomorphism



	</li>
	</ul>

</li>
<li>
	for linear vector space, $X$, complete in two norms, $\|\cdot\|_A$ and $\|\cdot\|_B$,
with $C\in\reals$ such that
$
(\forall x\in X)(\|x\|_A \leq C \|x\|_B)
$,
two norms are equivalent, <i>i.e.</i>,
$
(\exists C'\in\reals)(\forall x\in X)(\|x\|_B \leq C' \|x\|_A)
$

</li>
<li>
	<span class="name-font">closed graph theorem -</span> linear transformation, $A$, from Banach space, $A$, to Banach space, $B$,
with property that
&ldquo;if $\seq{x_n}$ converges in $X$ to $x\in X$ and $\seq{Ax_n}$ converges in $Y$ to $y\in Y$,
then $y=Ax$''
is continuous
	<ul>
	<li>
		equivalent to say, if graph $\set{(x,Ax)}{x\in X}\subset X\times Y$ is closed,
$A$ is continuous

	</li>
	</ul>

</li>
</ul>

<h3>Principle of uniform boundedness (on Banach spaces)</h3>

<ul>
<li>
	<span class="name-font">principle of uniform boundedness - </span>
for family of bounded linear operators, $\collk{F}$ from Banach space, $X$, to normed space, $Y$,
with

$$

(
\forall x \in X
)
(
\exists M_x
)
(
\forall T \in \collk{F}
)
(
\|Tx\| \leq M_x
)

$$


then operators in $\collk{F}$ is uniformly bounded,
<i>i.e.</i>,

$$

(
\exists M
)
(
\forall T \in \collk{F}
)
(
\|T\| \leq M
)

$$


</li>
</ul>




<h3>Topological vector spaces</h3>


<ul>
<li>
	just as notion of metric spaces generalized to notion of topological spaces

</li>
<li>
	<i>notion of normed linear space generalized to notion of topological vector spaces</i>

</li>
<li>
	linear vector space, $X$, with topology, $\tJ$, equipped with
continuous addition, $+:X\times X\to X$
and
continuous multiplication by scalars, $+:\reals\times X\to X$,
called <span class="define">topological vector space</span>

</li>
</ul>

<h3>Translation invariance of topological vector spaces</h3>

<ul>
<li>
	for topological vector space,
translation by $x\in X$ is homeomorphism (due to continuity of addition)
	<ul>
	<li>
		hence, $x+O$ of open set $O$ is open

	</li>
	<li>
		every topology with this property said to be <span class="define">translation invariant</span>

	</li>
	</ul>

</li>
<li>
	for translation invariant topology, $\tJ$, on $X$,
and
base, $\collB$, for $\tJ$ at $0$,
set

$$

\set{x+U}{U\in \collB}

$$

forms <i>a base</i> for $\tJ$ at $x$

</li>
<li>
	hence, sufficient to give a base at $0$
to determine <i>translation invariance of topology</i>

</li>
<li>
	base at $0$ often called <span class="define">local base</span>

</li>
</ul>

<h3>Sufficient and necessarily condition for topological vector spaces</h3>

<div id="page:Sufficient-and-necessarily-condition-for-topological-vector-spaces"></div>

<ul>
<li>
	for topological vector space, $X$,
can find base, $\collB$, satisfying following properties

$$
\begin{eqnarray*}

&&
(\forall U, V \in \collB)(\exists W\in \collB)(W\subset U\cap V)
\\
&&
(\forall U \in \collB, x\in U)(\exists V\in \collB)(x+V\subset U)
\\
&&
(\forall U \in \collB)(\exists V\in \collB)(V + V \subset U)
\\
&&
(\forall U \in \collB, x\in X)(\exists \alpha\in \reals)(x\in \alpha U)
\\
&&
(\forall U \in \collB, 0<|\alpha|\leq 1\in \reals)(\alpha U\subset U, \alpha U\subset \collB)

\end{eqnarray*}
$$


</li>
<li>
	conversely, for collection, $\collB$, of subsets containing $0$
satisfying above properties,
exists topology for $X$ making $X$ <i>topological vector space</i>
with $\collB$ as base at $0$
	<ul>
	<li>
		this topology is Hausdorff if and only if

$$

\bigcap\{U\in \collB\} = \{0\}

$$


	</li>
	</ul>

</li>
<li>
	for normed linear space,
can take $\collB$ to be set of spheres centered at $0$,
then $\collB$ satisfies above properties,
hence can form <i>topological vector space</i>

</li>
</ul>

<h3>Topological isomorphism</h3>

<div id="page:Topological-isomorphism"></div>
<ul>
<li>
	in topological vector space,
can compare neighborhoods at one point
with neighborhoods of another point
by translation

</li>
<li>
	for mapping, $f$,
from topological vector space, $X$,
to topological vector space, $Y$,
such that

$$
\begin{eqnarray*}

&&
(\forall \mbox{ open } O\subset Y \mbox{ with }0\in O)
(\exists \mbox{ open } U\subset X \mbox{ with }0\in U)
\\
&&
(\forall x\in X)
(f(x+U) \subset f(x) + O)

\end{eqnarray*}
$$

said to be <span class="define">uniformly continuous</span>

</li>
<li>
	linear transformation, $f$, is uniformly continuous
if continuous at one point

</li>
<li>
	continuous one-to-one mapping, $\varphi$, from $X$ onto $Y$ with continuous $\varphi^{-1}$
called <span class="define">(topological) isomorphism</span>
	<ul>
	<li>
		in abstract point of view, isomorphic spaces are <i>same</i>

	</li>
	</ul>

</li>
<li>
	<span class="name-font">Tychonoff -</span>
finite-dimensional Hausdorff topological vector space
is topologically isomorphic
to $\reals^n$ for some $n$


</li>
</ul>

<h3>Weak topologies</h3>




<ul>
<li>
	for vector space, $X$, and collection of linear functionals, $\collF$,
weakest topology generated by $\collF$,
<i>i.e.</i>, in way that each functional in $\collF$ is continuous in that topology,
called <span class="define">weak topology generated by</span> $\collF$
	<ul>
	<li>
		translation invariant

	</li>
	<li>
		base at $0$ given by sets

$$

\set{x\in X}{\forall f \in\collk{G}, |f(x)|<\epsilon}

$$

for all finite $\collk{G}\subset\collF$ and $\epsilon>0$

	</li>
	<li>
		basis satisfies properties on page~<a href="#page:Sufficient-and-necessarily-condition-for-topological-vector-spaces">here</a>,
hence, (above) weak topology makes <i>topological vector space</i>

	</li>
	</ul>

</li>
<li>
	for <i>normed</i> vector space, $X$, and collection of continuous functionals, $\collF$,
<i>i.e.</i>, $\collF\subset X^\ast$,
weak topology generated by $\collF$
<i>weaker than</i> (fewer open sets) norm topology of $X$

</li>
<li>
	metric topology generated by norm called <span class="define">strong topology of $X$</span>

</li>
<li>
	weak topology generated by $X^\ast$ called <span class="define">weak topology of $X$</span>

</li>
</ul>

<h3>Strongly and weakly open and closed sets</h3>


<ul>
<li>
	open and closed sets of strong topology called <span class="define">strongly open</span> and <span class="define">strongly closed</span>

</li>
<li>
	open and closed sets of weak topology called <span class="define">weakly open</span> and <span class="define">weakly closed</span>

</li>
<li>
	wealy closed set is strongly closed, but converse not true

</li>
<li>
	however, these coincides for linear manifold,
<i>i.e.</i>, linear manifold is weakly closed if and only if strongly closed

</li>
<li>
	every strongly converent sequence (or net) is weakly convergent

</li>
</ul>

<h3>Weak$^\ast$ topologies</h3>


<ul>
<li>
	for normed space,
<span class="define">weak topology of $X^\ast$</span>
is weakest topology for which
all functionals in $X^{\ast\ast}$ are continuous

</li>
<li>
	turns out that weak topology of $X^\ast$
is less useful than weak topology generated by $X$,
<i>i.e.</i>, that generated by $\varphi(X)$
where $\varphi$ is the natural embedding of $X$ into $X^{\ast\ast}$
(refer to page~<a href="#page:Natural-isomorphism">here</a>)

</li>
<li>
	(above) weak topology generated by $\varphi(X)$
called <span class="define">weak$^\ast$ topology for $X^\ast$</span>
	<ul>
	<li>
		even <i>weaker than</i> weak topology of $X^\ast$

	</li>
	<li>
		thus, weak$^\ast$ closed subset of is weakly closed,
and weak convergence implies weak$^\ast$ convergence

	</li>
	</ul>

</li>
<li>
	base at $0$ for weak$^\ast$ topology given by sets

$$

\set{f}{\forall x\in A, |f(x)|<\epsilon}

$$

for all finite $A\subset X$ and $\epsilon>0$

</li>
<li>
	<i>when $X$ is reflexive, weak and weak$^\ast$ topologies coincide</i>

</li>
<li>
	<span class="name-font">Alaoglu -</span> unit ball $S^\ast = \set{f\in X^\ast}{\|f\|\geq1}$
is compact in weak$^\ast$ topology

</li>
</ul>

<h3>Convex sets</h3>

<div id="page:Convex---sets"></div>
<ul>
<li>
	for vector space, $X$ and $x,y\in X$

$$

\set{\lambda x + (1-\lambda)y}{\lambda \in [0,1]} \subset X

$$

called <span class="define">segmenet joining $x$ and $y$</span>

</li>
<li>
	set $K\subset X$ said to be <span class="define">convex</span> or <span class="define">convex set</span>
if every segment joining any two points in $K$ is in $K$, <i>i.e.</i>,
$
(\forall x,y\in K)(\mbox{segment joining }x,y\subset X)
$

</li>
<li>
	every $\lambda x + (1-\lambda)y$ for $0<\lambda<1$ called <span class="define">interior point of segment</span>

</li>
<li>
	point in $K\subset X$ where intersection with $K$
of every line going through $x$
contains open interval about $x$,
said to be <span class="define">internal point</span>,
<i>i.e.</i>,

$$

(\exists \epsilon>0)(\forall y\in K, |\lambda|<\epsilon)(x+y x\in K)

$$


</li>
<li>
	convex set examples -
linear manifold  &amp; ball, ellipsoid in normed space

</li>
</ul>

<h3>Properties of convex sets</h3>

<ul>
<li>
	for convex sets, $K_1$ and $K_2$, following are also convex sets

$$

K_1 \cap K_2,\ \lambda K_1,\ K_1 + K_2

$$


</li>
<li>
	for linear operators from vector space, $X$, and vector space, $Y$,
	<ul>
	<li>
		image of convex set (or linear manifold) in $X$
is convex set (or linear manifold) in $Y$,

	</li>
	<li>
		inverse image of convex set (or linear manifold) in $Y$
is convex set (or linear manifold) in $X$

	</li>
	</ul>

</li>
<li>
	closure of convex set in topological vector space is convex set

</li>
</ul>

<h3>Support functions of and separated convex sets</h3>

<ul>
<li>
	for subset $K$ of vector space $X$,
$p:K\to \preals$ with $p(x) = \inf{\lambda|\lambda^{-1}x \in K, \lambda>0}$
called <span class="define">support functions</span>

</li>
<li>
	for convex set $K\subset X$ containing $0$ as internal point
	<ul>
	<li>
		$(\forall x\in X,\lambda\geq0)(p(\lambda x) = \lambda p(x))$

	</li>
	<li>
		$(\forall x,y\in X)(p(x+y)\leq p(x)+p(y))$

	</li>
	<li>
		$\set{x\in X}{p(x) < 1} \subset K \subset \set{x\in X}{p(x)\leq 1}$

	</li>
	</ul>

</li>
<li>
	two convex sets, $K_1$ and $K_2$
such that exists linear functional, $f$, and $\alpha\in\reals$
with
$(\forall x\in K_1)(f(x) \leq \alpha)$
and
$(\forall x\in K_2)(f(x) \geq \alpha)$,
said to be <span class="define">separated</span>

</li>
<li>
	for two disjoint convex sets in vector space
with at least one of them having internal point,
exists <i>nonzero linear functional</i> that separates two sets

</li>
</ul>

<h3>Local convexity</h3>

<ul>
<li>
	topological vector space with base for topology consisting of convest sets,
said to be <span class="define">locally convex</span>

</li>
<li>
	for family of convex sets, $\collk{N}$, in vector space,
following conditions are sufficient
for being able to translate sets in $\collk{N}$
to form base for topology
to make topological space into locally convex topological vector space

$$
\begin{eqnarray*}

&
(\forall N\in\collk{N})(x\in N \Rightarrow x \mbox{ is internal})
&
\\
&
(\forall N_1, N_2\in\collk{N})(\exists N_3\in\collk{N})(N_3 \subset N_1 \cap N_2)
&
\\
&
(\forall N \in\collk{N}, \alpha\in\reals \mbox{ with } 0<|\alpha|<1)(\alpha N \in \collk{N})
&

\end{eqnarray*}
$$


</li>
<li>
	conversely, for every locally convex topological vector space,
exists base at $0$ satisfying above conditions

</li>
<li>
	follows that
	<ul>
	<li>
		weak topology on vector space generated by linear functionals
is locally convex

	</li>
	<li>
		normed vector space is locally convex topological vector space

	</li>
	</ul>

</li>
</ul>

<h3>Facts regarding local convexity</h3>

<ul>
<li>
	for locally convex topological vector space
closed convex subset, $F$,
with point, $x$, not in $F$,
exists continuous linear functional, $f$,
such that

$$

f(x) < \inf_{y\in F} f(y)

$$


</li>
<li>
	corollaries
	<ul>
	<li>
		convex set in locally convex topological vector space
is strongly closed if and only if weakly closed

	</li>
	<li>
		for distinct points, $x$ and $y$,
in locally convex Hausdorff vector space,
exists continuous linear functional, $f$,
such that $f(x)\neq f(y)$

	</li>
	</ul>

</li>
</ul>

<h3>Extreme points and supporting sets of convex sets</h3>

<ul>
<li>
	point in convex set in vector space
that is not interior point of any line segment lying in the set,
called <span class="define">extreme point</span>

</li>
<li>
	thus,
$x$ is extreme point of convex set, $K$, if and only if
$x=\lambda y + (1-\lambda) z$ with $0<\lambda<1$ implies $y\not\in K$ or $z\not\in K$

</li>
<li>
	closed and convex subset, $S$, of convex set, $K$,
with property that
for every interior point of line segment in $K$ belonging to $S$,
entire line segment belongs to $S$,
called <span class="define">supporting set of $K$</span>

</li>
<li>
	for closed and convex set, $K$,
set of points <i>a</i> continuous linear functional assumes maximum on $K$,
is <i>supporting set of $K$</i>

</li>
</ul>

<h3>Convex hull and convex convex hull</h3>

<ul>
<li>
	for set $E$ in vector space,
intersection of all convex sets containing set, $E$,
called <span class="define">convex hull of $E$</span>,
which is convex set

</li>
<li>
	for set $E$ in vector space,
intersection of all closed convex sets containing set, $E$,
called <span class="define">closed convex hull of $E$</span>,
which is closed convex set

</li>
<li>
	<span class="name-font">Krein-Milman theorem -</span>



compact convex set
in
locally convex topologically vector space
is <i>closed convex hull of its extreme points</i>

</li>
</ul>

<h3>Hilbert spaces</h3>



<ul>
<li>
	Banach space, $H$, with function $\innerp{\cdot}{\cdot}:H\times H\to\reals$ satisfying following properties,
called <span class="define">Hilbert space</span>


$$
\begin{eqnarray*}

&&(\forall x,y,z\in H, \alpha, \beta \in \reals)(\innerp{\alpha x + \beta y}{z}=\alpha\innerp{x}{z} + \beta\innerp{y}{z})
\\
&&(\forall x,y\in H)(\innerp{x}{y} = \innerp{y}{z})
\\
&&(\forall x\in H)(\innerp{x}{x} = \|x\|^2)

\end{eqnarray*}
$$


</li>
<li>
	$\innerp{x}{y}$ called <span class="define">inner product</span>



for $x,y\in H$
	<ul>
	<li>
		examples -
$\innerp{x}{y} = x^T y = \sum x_i y_i$ for $\reals^n$,
$\innerp{x}{y} = \int x(t)y(t) dt$ for $L^2$

	</li>
	</ul>

</li>
<li>
	<span class="name-font">Schwarz or Cauchy-Schwarz or Cauchy-Buniakowsky-Schwarz inequality -</span>














$$

\|x\|\|y\| \geq \innerp{x}{y}

$$

	<ul>
	<li>
		hence,
		<ul>
		<li>
			 linear functional defined by $f(x)=\innerp{x}{y}$ bounded by $\|y\|$

		</li>
		<li>
			 $\innerp{x}{y}$ is continuous function from $H\times H$ to $\reals$

		</li>
		</ul>

	</li>
	</ul>

</li>
</ul>

<h3>Inner product in Hilbert spaces</h3>




<ul>
<li>
	$x$ and $y$ in $H$ with $\innerp{x}{y}=0$ said to be <span class="define">orthogonal</span>



denoted by <span class="notation">$x\perp y$</span>

</li>
<li>
	set $S$ of which any two elements orthogonal
called <span class="define">orthogonal system</span>



</li>
<li>
	orthogonal system called <span class="define">orthonormal</span> if every element has unit norm




</li>
<li>
	any two elements are $\sqrt{2}$ apart,
hence <i>if $H$ separable,
every orthonormal system in $H$
must be countable</i>




</li>
<li>
	shall deal only with <i>separable Hilbert spaces</i>

</li>
</ul>

<h3>Fourier coefficients</h3>

<ul>
<li>
	assume orthonormal system expressed as sequence, $\seq{\varphi_n}$ - may be finite or infinite

</li>
<li>
	for $x\in H$ 
$$
a_n = \innerp{x}{\varphi_n}
$$

called <span class="define">Fourier coefficients</span>





</li>
<li>
	for $n\in\naturals$, we have

$$

\|x\|^2 \geq \sum^n_{i=1} a_i^2

$$

	<div class="proof">
		

$$
\begin{eqnarray*}

\left\| x-\sum_{i=1}^n a_i \varphi_i \right\|^2
&=&
\innerpt{x-\sum a_i \varphi_i}{x-\sum a_i \varphi_i}{}

\\
&=&
\innerpt{x}{x}
- 2 \innerpt{x}{\sum a_i \varphi_i}{}
+ \innerpt{\sum a_i \varphi_i}{\sum a_i \varphi_i}{}
\\
&=&
\|x\|^2
- 2 \sum a_i \innerpt{x}{\varphi_i}
+ \sum a_i^2 \|\varphi_i\|^2

\\
&=&
\|x\|^2 - \sum a_i^2
\geq 0

\end{eqnarray*}
$$


	</div>

</li>
</ul>

<h3>Fourier coefficients of limit of $x$</h3>

<ul>
<li>
	<span class="define">Bessel's inequality -</span>


for $x\in H$, its Fourier coefficients, $\seq{a_n}$

$$

\sum_{n=1}^\infty a_n^2 \leq \|x\|^2

$$


</li>
<li>
	then, $\seq{z_n}$ defined by following is <i>Cauchy sequence</i>
$
z_n = \sum_{i=1}^n a_i \varphi_i
$

</li>
<li>
	completeness (of Hilbert space) implies $\seq{z_n}$ converges
- let $y=\lim z_n$

$$

y=\lim z_n = \sum_{i=1}^\infty a_i \varphi_i

$$


</li>
<li>
	continuity of inner product implies $\innerp{y}{\varphi_n} = \lim (z_n,\varphi_n) = a_n$,
<i>i.e.</i>, Fourier coefficients of $y\in H$ are $a_n$, <i>i.e.</i>,

</li>
<li>
	<i>$y$ has same Fourier coefficients as $x$</i>

</li>
</ul>

<h3>Complete orthonormal system</h3>





<ul>
<li>
	orthonormal system, $\seq{\varphi_n}_{n=1}^\infty$, of Hilbert spaces, $H$, is said to be <span class="define">complete</span>

if

$$

(\forall x\in H, n\in\naturals)(\innerp{x}{\varphi_n}=0)
\Rightarrow
x=0

$$


</li>
<li>
	orthonormal system is complete if and only if maximal, <i>i.e.</i>,




$$
\begin{eqnarray*}

\seq{\varphi_n} \mbox{ is complete}
&\Leftrightarrow&
(
(\exists \mbox{ orthonormal }R\subset H)(\forall n\in\naturals)(\varphi_n \in R)

\\
&\Rightarrow&
R = \seq{\varphi_n}
)

\end{eqnarray*}
$$

</li>
<li>
	 

</li>
<li>
	Hausdorff maximal principle (<a href="#principle:Hausdorff---maximal---principle"></a>)
implies existence of maximal orthonormal system,
hence following statement

</li>
<li>
	for separable Hilbert space, $H$,
every orthonormal system is separable
and exists <i>a</i> complete orthonormal system.
any such system, $\seq{\varphi_n}$, and $x\in H$

$$

x = \sum a_n \varphi_n

$$

with $a_n = \innerp{x}{\varphi_n}$,
and $\|x\| = \sum a_n^2$

</li>
</ul>

<h3>Dimensions of Hilbert spaces</h3>



<ul>
<li>
	every complete orthonormal system of separable Hilbert space
has same number of elements, <i>i.e.</i>, has same cardinality

</li>
<li>
	hence, every complete orthonormal system
has
either finite or countably infinite complete orthonormal system

</li>
<li>
	this number called <span class="define">dimension of separable Hilbert space</span>


	<ul>
	<li>
		for Hilbert space with countably infinite complete orthonormal system,
we say, $\dim H = \aleph_0$

	</li>
	</ul>

</li>
</ul>

<h3>Isomorphism and isometry between Hilbert spaces</h3>





<ul>
<li>
	<span class="define">isomorphism, $\Phi$, of Hilbert space onto another Hilbert space</span>
is linear mapping with property, $\innerp{\Phi x}{\Phi y} = \innerp{x}{y}$

</li>
<li>
	hence, every <i>isomorphism between Hilbert spaces is isometry</i>

</li>
<li>
	every $n$-dimensional Hilbert space is isomorphic to $\reals^n$

</li>
<li>
	every $\aleph_0$-dimensional Hilbert space is isomorphic to $l^2$,
which again is isomorphic to $L^2$

</li>
<li>
	$L^2[0,1]$ is separable and $\seq{\cos (n\pi t)}$ is infinite orthogonal system

</li>
<li>
	every bounded linear functional, $f$, on Hilbert space, $H$,
has unique $y$ such that

$$

(\forall x\in H)(f(x)=\innerp{x}{y})

$$

and $\|f\|=\|y\|$

</li>
</ul>

