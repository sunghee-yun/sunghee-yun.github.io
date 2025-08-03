---
title: Measure-theoretic Treatment of Statistics
date: Fri Aug  1 06:00:00 PDT 2025
last_modified_at: Sun Aug  3 05:49:27 PDT 2025
permalink: /math/rig/measure-theoretic-treatment-of-statistics
categories:
- blog
tags:
- math
- measure theory
- statistics
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


<h1 id="Measure Theoretic Treatment of Probabilities">Measure-theoretic Treatment of Probabilities</h1>



<h2 id="Probability Measure">Probability Measure</h2>


<h3>Measurable functions</h3>


<ul>
<li>
	
denote <span class="define">$n$-dimensional Borel sets</span> by $\algR^n$


</li>
<li>
	for two measurable spaces, $\measu{\Omega}{\algF}$ and $\measu{\Omega'}{\algF'}$,
function, $f:\Omega \to \Omega'$ with

$$
\left(
\forall A' \in \algF'
\right)
\left(
f^{-1}(A') \in \algF
\right)
$$

said to be <span class="define">measurable with respect to $\algF/\algF'$</span>

(thus, measurable functions defined on page~
and page~
can be said to be measurable with respect to $\collk{B}/\algR$)

</li>
<li>
	when $\Omega=\reals^n$ in $\measu{\Omega}{\algF}$,
$\algF$ is assumed to be $\algR^n$,
and sometimes drop $\algR^n$
	<ul>
	<li>
		thus, <i>e.g.</i>, we say $f:\Omega\to\reals^n$ is measurable with respect to $\algF$ (instead of $\algF/\algR^n$)

	</li>
	</ul>

</li>
<li>
	measurable function, $f:\reals^n\to\reals^m$ (<i>i.e.</i>, measurable with respect to $\algR^n/\algR^m$),
called <span class="define">Borel functions</span>



</li>
<li>
	$f:\Omega\to\reals^n$ is measurable with respect to $\algF/\algR^n$
if and only if
every component, $f_i:\Omega\to\reals$, is measurable with respect to $\algF/\algR$

</li>
</ul>

<h3>Probability (measure) spaces</h3>



<ul>
<li>
	set function, $P:\algk{F}\to[0,1]$, defined on algebra, $\algk{F}$, of set $\Omega$,
satisfying following properties,
called <span class="define">probability measure</span>

(refer to page~ for resumblance with measurable spaces)
	<ul>
	<li>
		$(\forall A\in\algk{F})(0\leq P(A)\leq 1)$

	</li>
	<li>
		$P(\emptyset) = 0,\ P(\Omega) = 1$

	</li>
	<li>
		$(\forall \mbox{ disjoint } \seq{A_n} \subset \algk{F} )(P\left(\bigcup A_n\right) = \sum P(A_n))$

	</li>
	</ul>

</li>
<li>
	for $\sigma$-algebra, $\algk{F}$, $\meas{\Omega}{\algk{F}}{P}$,
called <span class="define">probability measure space</span> or <span class="define">probability space</span>



</li>
<li>
	set $A\in\algk{F}$ with $P(A)=1$,
called <span class="define">a support of $P$</span>


</li>
</ul>

<h3>Dynkin's $\pi$-$\lambda$ theorem</h3>




<ul>
<li>
	class, $\subsetset{P}$, of subsets of $\Omega$ closed under finite intersection,
called <span class="define">$\pi$-system</span>, <i>i.e.</i>,

	<ul>
	<li>
		$(\forall A,B\in \subsetset{P})(A\cap B\in\subsetset{P})$

	</li>
	</ul>

</li>
<li>
	class, $\subsetset{L}$, of subsets of $\Omega$ containing $\Omega$
closed under complements and countable disjoint unions
called <span class="define">$\lambda$-system</span>

	<ul>
	<li>
		$\Omega \in \subsetset{L}$

	</li>
	<li>
		$(\forall A\in \subsetset{L})(\compl{A}\in\subsetset{L})$

	</li>
	<li>
		$(\forall \mbox{ disjoint }\seq{A_n})(\bigcup A_n \in \subsetset{L})$

	</li>
	</ul>

</li>
<li>
	<i>class that is both $\pi$-system and $\lambda$-system is $\sigma$-algebra</i>


</li>
<li>
	<span class="name-font">Dynkin's $\pi$-$\lambda$ theorem -</span>
for $\pi$-system, $\subsetset{P}$, and $\lambda$-system, $\subsetset{L}$,
with $\subsetset{P} \subset \subsetset{L}$,




$$
\sigma(\subsetset{P}) \subset \subsetset{L}
$$


</li>
<li>
	for $\pi$-system, $\algk{P}$,
two probability measures, $P_1$ and $P_2$, on $\sigma(\algk{P})$,
agreeing $\algk{P}$,
agree on $\sigma(\algk{P})$


</li>
</ul>

<h3>Limits of Events</h3>

<div class="theorem" id="theorem:convergence-of-events" data-name="convergence-of-events">
	no


for sequence of subsets, $\seq{A_n}$,

$$
P(\liminf A_n) \leq \liminf P(A_n) \leq \limsup P(A_n) \leq P(\limsup A_n)
$$

	<ul>
	<li>
		
for $\seq{A_n}$ converging to $A$

$$
\lim P(A_n) = P(A)
$$


	</li>
	</ul>

</div>
<div class="theorem" id="theorem:independence-of-smallest-sig-alg" data-name="independence-of-smallest-sig-alg">
	no
for sequence of $\pi$-systems, $\seq{\algA_n}$, $\seq{\sigma(\algA_n)}$ is independent

</div>

<h3>Probabilistic independence</h3>

<ul>
<li>
	 given probability space, $\meas{\Omega}{\algk{F}}{P}$

</li>
<li>
	$A,B\in\algk{F}$ with

$$
P(A\cap B) = P(A) P(B)
$$

said to be <span class="define">independent</span>




</li>
<li>
	indexed collection, $\seq{A_\lambda}$, with

$$
\left(
\forall n\in\naturals, \mbox{ distinct } \lambda_1, \ldots, \lambda_n \in \Lambda
\right)
\left(
P\left(\bigcap_{i=1}^n A_{\lambda_i}\right) = \prod_{i=1}^n P(A_{\lambda_i})
\right)
$$

said to be <span class="define">independent</span>




</li>
</ul>

<h3>Independence of classes of events</h3>

<ul>
<li>
	indexed collection, $\seq{\subsetset{A}_\lambda}$, of classes of events (<i>i.e.</i>, subsets) with

$$
\left(
\forall A_\lambda \in \subsetset{A}_\lambda
\right)
\left(
\seq{A_\lambda} \mbox{ are independent}
\right)
$$

said to be <span class="define">independent</span>





</li>
<li>
	<span class="fact-font">
for independent indexed collection, \seq{\subsetset{A}_\lambda}, with every $\subsetset{A}_\lambda$ being $\pi$-sytem,
\seq{\sigma(\subsetset{A}_\lambda)} are independent
</span>


</li>
<li>
	for independent (countable) collection of events, $\seq{\seq{A_{ni}}_{i=1}^\infty}_{n=1}^\infty$,
$\seq{\algk{F}_n}_{n=1}^\infty$ with $\algk{F}_n = \sigma(\seq{A_{ni}}_{i=1}^\infty)$
are independent

</li>
</ul>

<h3>Borel-Cantelli lemmas</h3>




<ul>
<li>
		<div class="lemma" id="lemma:first Borel-Cantelli" data-name="first Borel-Cantelli">
		

for sequence of events, $\seq{A_n}$, with $\sum P(A_n)$ converging

$$
P(\limsup A_n) = 0
$$


	</div>

</li>
<li>
		<div class="lemma" id="lemma:second Borel-Cantelli" data-name="second Borel-Cantelli">
		

for independent sequence of events, $\seq{A_n}$, with $\sum P(A_n)$ diverging

$$
P(\limsup A_n)=1
$$


	</div>

</li>
</ul>

<h3>Tail events and Kolmogorov's zero-one law</h3>






<ul>
<li>
	for sequence of events, $\seq{A_n}$

$$
\algk{T} = \bigcap_{n=1}^\infty \sigma\left(\seq{A_i}_{i=n}^\infty\right)
$$

called <span class="define">tail $\sigma$-algebra associated with \seq{A_n}</span>;
its lements are called <span class="define">tail events</span>





</li>
<li>
	<span class="name-font">Kolmogorov's zero-one law -</span>


for independent sequence of events, $\seq{A_n}$
every event in tail $\sigma$-algebra
has probability measure either $0$ or $1$

</li>
</ul>

<h3>Product probability spaces</h3>



<ul>
<li>
	for two measure spaces, $\meas{X}{\algX}{\mu}$ and $\meas{Y}{\algY}{\nu}$,
want to find product measure, $\pi$,
such that

$$
\left(
\forall A\in \algX, B\in\algY
\right)
\left(
\pi(A\times B) = \mu(A)\nu(B)
\right)
$$

	<ul>
	<li>
		<i>e.g.</i>, if both $\mu$ and $\nu$ are Lebesgue measure on $\reals$,
$\pi$ will be Lebesgue measure on $\reals^2$

	</li>
	</ul>

</li>
<li>
	$A\times B$ for $A\in\algX$ and $B\in\algY$ is <i>measurable rectangle</i>


</li>
<li>
	<span class="define">$\sigma$-algebra generated by measurable rectangles</span>


denoted by

$$
\algX \times \algY
$$

	<ul>
	<li>
		thus, <span class="eemph">not</span> Cartesian product in usual sense

	</li>
	<li>
		generally <i>much larger</i> than class of measurable rectangles

	</li>
	</ul>

</li>
</ul>

<h3>Sections of measurable subsets and functions</h3>

<ul>
<li>
	
for two measure spaces, $\meas{X}{\algX}{\mu}$ and $\meas{Y}{\algY}{\nu}$

</li>
<li>
	sections of measurable subsets

	<ul>
	<li>
		$\set{y\in Y}{(x,y)\in E}$ is <span class="define">section of $E$ determined by $x$</span>

	</li>
	<li>
		$\set{x\in X}{(x,y)\in E}$ is <span class="define">section of $E$ determined by $y$</span>

	</li>
	</ul>

</li>
<li>
	sections of measurable functions
- for measurable function, $f$, with respect to $\algX\times \algY$

	<ul>
	<li>
		$f(x,\cdot)$ is <span class="define">section of $f$ determined by $x$</span>

	</li>
	<li>
		$f(\cdot,y)$ is <span class="define">section of $f$ determined by $y$</span>

	</li>
	</ul>

</li>
<li>
	sections of measurable subsets are measurable
	<ul>
	<li>
		$\left( \forall x\in X, E\in \algX \times \algY \right) \left( \set{y\in Y}{(x,y)\in E} \in \algY \right)$

	</li>
	<li>
		$\left( \forall y\in Y, E\in \algX \times \algY \right) \left( \set{x\in X}{(x,y)\in E} \in \algX \right)$

	</li>
	</ul>

</li>
<li>
	sections of measurable functions are measurable
	<ul>
	<li>
		$f(x,\cdot)$ is measurable with respect to $\algY$ for every $x\in X$

	</li>
	<li>
		$f(\cdot,y)$ is measurable with respect to $\algX$ for every $y\in Y$

	</li>
	</ul>

</li>
</ul>

<h3>Product measure</h3>



<ul>
<li>
	
for two $\sigma$-finite measure spaces, $\meas{X}{\algX}{\mu}$ and $\meas{Y}{\algY}{\nu}$

</li>
<li>
	two functions defined below for every $E\in\algX\times\algY$ are $\sigma$-finite measures
	<ul>
	<li>
		$\pi'(E) = \int_X \nu\set{y\in Y}{(x,y)\in E} d\mu$

	</li>
	<li>
		$\pi''(E) = \int_Y \mu\set{x\in X}{(x,y)\in E} d\nu$

	</li>
	</ul>

</li>
<li>
	for every measurable rectangle, $A\times B$, with $A\in\algX$ and $B\in\algY$

$$
\pi'(A\times B)
=
\pi''(A\times B)
=
\mu(A) \nu(B)
$$


</li>
<li>
	
(use conventions in page~ for extended real values)

</li>
<li>
	indeed, $\pi'(E)=\pi''(E)$ for every $E\in\algX\times\algY$; let $\pi=\pi'=\pi''$

</li>
<li>
	$\pi$ is
	<ul>
	<li>
		called <span class="define">product measure</span>


and denoted by <span class="define">$\mu\times \nu$</span>

	</li>
	<li>
		$\sigma$-finite measure

	</li>
	<li>
		<i>only</i> measure such that $\pi(A\times B) =\mu(A) \nu(B)$ for every measurable rectangle

	</li>
	</ul>

</li>
</ul>

<h3>Fubini's theorem</h3>




<ul>
<li>
	suppose two $\sigma$-finite measure spaces, $\meas{X}{\algX}{\mu}$ and $\meas{Y}{\algY}{\nu}$
- define
	<ul>
	<li>
		$X_0 = \set{x\in X}{\int_Y |f(x,y)|d\nu < \infty}\subset X$

	</li>
	<li>
		$Y_0 = \set{y\in Y}{\int_X |f(x,y)|d\nu < \infty}\subset Y$

	</li>
	</ul>

</li>
<li>
	<span class="name-font">Fubini's theorem -</span>



for nonnegative measurable function, $f$,
following are measurable
with respect to $\algX$ and $\algY$ respectively

$$
g(x) = \int_Y f(x,y)d\nu,\ \
h(y) = \int_X f(x,y)d\mu
$$

and following holds

$$
\int_{X\times Y} f(x,y) d\pi
=
\int_X \left(\int_Y f(x,y) d\nu\right)d\mu
=
\int_Y \left(\int_X f(x,y) d\mu\right)d\nu
$$


</li>
<li>
	
for $f$, (not necessarily nonnegative) integrable function with respect to $\pi$
	<ul>
	<li>
		$\mu(X\sim X_0) = 0$, $\nu(Y\sim Y_0)=0$

	</li>
	<li>
		$g$ and $h$ are finite measurable on $X_0$ and $Y_0$ respectively

	</li>
	<li>
		(above) equalities of <i>double integral</i> holds

	</li>
	</ul>

</li>
</ul>

<h2 id="Random Variables">Random Variables</h2>


<h3>Random variables</h3>


<ul>
<li>
	
for probability space, $\meas{\Omega}{\algk{F}}{P}$,

</li>
<li>
	measurable function (with respect to $\algF/\algR$), $X:\Omega \to \reals$,
called <span class="define">random variable</span>


</li>
<li>
	measurable function (with respect to $\algF/\algR^n$), $X:\Omega \to \reals^n$,
called <span class="define">random vector</span>


	<ul>
	<li>
		when expressing $X(\omega)=(X_1(\omega), \ldots, X_n(\omega))$,
$X$ is measurable if and only if every $X_i$ is measurable

	</li>
	<li>
		thus, $n$-dimensional random vaector is simply
$n$-tuple of random variables

	</li>
	</ul>

</li>
<li>
	smallest $\sigma$-algebra with respect to which $X$ is measurable,
called <span class="define">$\sigma$-algebra generated by $X$</span>



and denoted by <span class="define">$\sigma(X)$</span>
	<ul>
	<li>
		$\sigma(X)$ consists exactly of sets, $\set{\omega\in \Omega}{X(\omega)\in H}$, for $H\in\algR^n$

	</li>
	<li>
		random variable, $Y$, is measurable with respect to $\sigma(X)$
if and only if
exists measurable function, $f:\reals^n\to\reals$
such that
$Y(\omega) = f(X(\omega))$ for all $\omega$,
<i>i.e.</i>,
$Y=f\circ X$

	</li>
	</ul>

</li>
</ul>

<h3>Probability distributions for random variables</h3>

<ul>
<li>
	probability measure on $\reals$, $\mu = PX^{-1}$, <i>i.e.</i>,

$$
\mu(A) = P(X\in A) \mbox{ for } A \in \algR
$$

called <span class="define">distribution</span> or <span class="define">law</span> of random variable, $X$




</li>
<li>
	function, $F:\reals\to[0,1]$, defined by

$$
F(x) = \mu(-\infty, x] = P(X\leq x)
$$

called <span class="define">distribution function</span> or <span class="define">cumulative distribution function (CDF)</span> of $X$








</li>
<li>
	Borel set, $S$, with $P(S)=1$, called <span class="define">support</span>


</li>
<li>
	random variable, its distribution, its distribution function,
said to be <span class="define">discrete</span>

when has <i>countable</i> support

</li>
</ul>

<h3>Probability distribution of mappings of random variables</h3>

<ul>
<li>
	for measurable $g:\reals\to\reals$,

$$
\left(
\forall A\in\algR
\right)
\left(
\prob{g(X)\in A} = \prob{X \in g^{-1}(A)} = \mu (g^{-1}(A))
\right)
$$

hence, $g(X)$ has distribution of $\mu g^{-1}$


</li>
</ul>

<h3>Probability density for random variables</h3>

<ul>
<li>
	Borel function, $f: \reals\to\preals$, satisfying

$$
\left(
\forall A \in \algR
\right)
\left(
\mu(A) = P(X\in A) = \int_A f(x) dx
\right)
$$

called <span class="define">density</span> or <span class="define">probability density function (PDF)</span>
of random variable







</li>
<li>
	above is equivalent to

$$
\left(
\forall a < b \in \reals
\right)
\left(
\int_a^b f(x) dx = P(a<X\leq b) = F(b) - F(a)
\right)
$$


</li>
<li>
	
(refer to statement on page~)
	<ul>
	<li>
		note, though, $F$ does not need to differentiate to $f$ everywhere;
only $f$ required to integrate properly

	</li>
	<li>
		if $F$ does differentiate to $f$ and $f$ is continuous,
<i>fundamental theorem of calculus</i> implies
$f$ indeed is density for $F$

	</li>
	</ul>

</li>
</ul>

<h3>Probability distribution for random vectors</h3>

<ul>
<li>
	(similarly to random variables) probability measure on $\reals^n$, $\mu = PX^{-1}$,
<i>i.e.</i>,

$$
\mu(A) = P(X\in A) \mbox{ for } A \in \algk{B}^k
$$

called <span class="define">distribution</span> or <span class="define">law</span> of random vector, $X$





</li>
<li>
	function, $F:\reals^k\to[0,1]$, defined by

$$
F(x) = \mu S_x = P(X\preceq x)
$$

where

$$
S_x = \set{\omega\in \Omega}{X(\omega)\preceq x}
= \set{\omega\in \Omega}{X_i(\omega)\leq x_i}
$$

called <span class="define">distribution function</span> or <span class="define">cumulative distribution function (CDF)</span> of $X$








</li>
<li>
	(similarly to random variables) random vector, its distribution, its distribution function,
said to be <span class="define">discrete</span>

when has <i>countable</i> support

</li>
</ul>

<h3>Marginal distribution for random vectors</h3>

<ul>
<li>
	(similarly to random variables) for measurable $g:\reals^n\to\reals^m$

$$
\left(
\forall A\in\algR^{m}
\right)
\left(
\prob{g(X)\in A}
=
\prob{X \in g^{-1}(A)}
=
\mu(g^{-1}(A))
\right)
$$

hence, $g(X)$ has distribution of $\mu g^{-1}$

</li>
<li>
	for $g_i:\reals^n\to\reals$ with $g_i(x) = x_i$

$$
\left(
\forall A\in\algR
\right)
\left(
\prob{g(X)\in A}
=
\prob{X_i \in A}
\right)
$$


</li>
<li>
	measure, $\mu_i$, defined by $\mu_i(A) = \prob{X_i\in A}$,
called <span class="define">($i$-th) marginal distribution of $X$</span>



</li>
<li>
	for $\mu$ having density function, $f:\reals^n\to\preals$,
density function of marginal distribution is

$$
f_i(x) = \int_{\algR^{n-1}}
f(x_{-i}) d \mu_{-i}
$$

where $x_{-i} = (x_1,\ldots,x_{i-1}, x_{i+1}, \ldots, x_n)$
and similarly for $d\mu_{-i}$

</li>
</ul>

<h3>Independence of random variables</h3>



<ul>
<li>
	random variables, $X_1$, , $X_n$,
with independent $\sigma$-algebras generated by them,
said to be <span class="define">independent</span>



</li>
<li>
	
(refer to page~ for
independence of collections of subsets)
	<ul>
	<li>
		because $\sigma(X_i) = X_i^{-1}(\algR)=\set{X_i^{-1}(H)}{H\in\algR}$,
independent if and only if

$$
\left(
\forall H_1, \ldots, H_n\in \algR
\right)
\left(
P\left(X_1\in H_1,\ldots, X_n\in H_n\right)
= \prod P\left(X_i\in H_i\right)
\right)
$$

<i>i.e.</i>,

$$
\left(
\forall H_1, \ldots, H_n\in \algR
\right)
\left(
P\left(\bigcap X_i^{-1}(H_i)\right)
= \prod P\left(X_i^{-1}(H_i)\right)
\right)
$$


	</li>
	</ul>

</li>
</ul>

<h3>Equivalent statements of independence of random variables</h3>

<ul>
<li>
	for random variables, $X_1$, , $X_n$,
having $\mu$ and $F:\reals^n\to[0,1]$ as their distribution and CDF,
with each $X_i$ having $\mu_i$ and $F_i:\reals\to[0,1]$ as its distribution and CDF,
following statements are <i>equivalent</i>



	<ul>
	<li>
		$X_1,\ldots,X_n \mbox{ are independent}$

	</li>
	<li>
		$\left( \forall H_1, \ldots, H_n\in \algR \right) \left( P\left(\bigcap X_i^{-1}(H_i)\right) = \prod P\left(X_i^{-1}(H_i)\right) \right)$

	</li>
	<li>
		$\left( \forall H_1,\ldots,H_n \in \algR \right) \left( P(X_1\in H_1,\ldots, X_n\in H_n) = \prod P(X_i \in H_i) \right)$

	</li>
	<li>
		$\left( \forall x\in \reals^n \right) \left( P(X_1\leq x_1,\ldots, X_n\leq x_n) = \prod P(X_i \leq x_i) \right)$

	</li>
	<li>
		$\left( \forall x \in \reals^n \right) \left( F(x) = \prod F_i(x_i) \right)$

	</li>
	<li>
		$\mu = \mu_1 \times \cdots \times \mu_n$

	</li>
	<li>
		$\left( \forall x \in \reals^n \right) \left( f(x) = \prod f_i(x_i) \right)$

	</li>
	</ul>

</li>
</ul>

<h3>Independence of random variables with separate $\sigma$-algebra</h3>

<ul>
<li>
	 given probability space, $\meas{\Omega}{\algk{F}}{P}$

</li>
<li>
	random variables, $X_1$, , $X_n$,
each of which is measurable with respect to each of $n$ independent $\sigma$-algebras,
$\algk{G}_1\subset \algF$, , $\algk{G}_n\subset \algF$
respectively,
are independent



</li>
</ul>

<h3>Independence of random vectors</h3>

<ul>
<li>
	for random vectors, $X_1:\Omega\to\reals^{d_1}$, , $X_n:\Omega\to\reals^{d_n}$,
having $\mu$ and $F:\reals^{d_1}\times\cdots\times\reals^{d_n}\to[0,1]$ as their distribution and CDF,
with each $X_i$ having $\mu_i$ and $F_i:\reals^{d_i}\to[0,1]$ as its distribution and CDF,
following statements are <i>equivalent</i>



	<ul>
	<li>
		$X_1,\ldots,X_n \mbox{ are independent}$

	</li>
	<li>
		$\left( \forall H_1\in\algR^{d_1}, \ldots, H_n\in \algR^{d_n} \right)
\left( P\left(\bigcap X_i^{-1}(H_i)\right) = \prod P\left(X_i^{-1}(H_i)\right) \right)$

	</li>
	<li>
		$\left( \forall H_1\in\algR^{d_1}, \ldots, H_n\in \algR^{d_n} \right)
\left( P(X_1\in H_1,\ldots, X_n\in H_n) = \prod P(X_i \in H_i) \right)$

	</li>
	<li>
		$\left( \forall x_1\in \reals^{d_1},\ldots,x_n\in\reals^{d_n} \right)
\left( P(X_1\preceq x_1,\ldots, X_n\preceq x_n) = \prod P(X_i \preceq x_i) \right)$

	</li>
	<li>
		$\left( \forall x_1\in \reals^{d_1},\ldots,x_n\in\reals^{d_n} \right)
\left( F(x_1,\ldots,x_n) = \prod F_i(x_i) \right)$

	</li>
	<li>
		$\mu = \mu_1 \times \cdots \times \mu_n$

	</li>
	<li>
		$\left( \forall x_1\in \reals^{d_1},\ldots,x_n\in\reals^{d_n} \right)
\left( f(x_1,\ldots,x_n) = \prod f_i(x_i) \right)$

	</li>
	</ul>

</li>
</ul>

<h3>Independence of infinite collection of random vectors</h3>

<ul>
<li>
	infinite collection of random vectors
for which every finite subcollection is independent,
said to be <span class="define">independent</span>





</li>
<li>
	for independent (countable) collection of random vectors, $\seq{\seq{X_{ni}}_{i=1}^\infty}_{n=1}^\infty$,
$\seq{\algk{F}_n}_{n=1}^\infty$ with $\algk{F}_n = \sigma(\seq{X_{ni}}_{i=1}^\infty)$
are independent

</li>
</ul>

<h3>Probability evaluation for two independent random vectors</h3>

<div class="theorem" id="theorem:Probability evaluation for two independent random vectors" data-name="Probability evaluation for two independent random vectors">
	
for independent random vectors, $X$ and $Y$,
with distributions, $\mu$ and $\nu$, in $\reals^n$ and $\reals^m$ respectively

$$
\left(
\forall B\in\algR^{n+m}
\right)
\left(
\prob{(X,Y)\in B} = \int_{\reals^n} \prob{(x,Y)\in B} d\mu_X
\right)
$$

and

$$
\left(
\forall A\in\algR^{n}, B\in\algR^{n+m}
\right)
\left(
\prob{X\in A, (X,Y)\in B} = \int_{A} \prob{(x,Y)\in B} d\mu_X
\right)
$$


</div>

<h3>Sequence of random variables</h3>

<div class="theorem" id="theorem:squence of random variables" data-name="squence of random variables">
	
for sequence of probability measures on $\algR$, $\seq{\mu_n}$,
exists probability space, $\meas{X}{\Omega}{P}$,
and sequence of independent random variables in $\reals$, $\seq{X_n}$,
such that each $X_n$ has $\mu_n$ as distribution

</div>

<h3>Expected values</h3>

<div class="definition" id="definition:expected values" data-name="expected values">
	


for random variable, $X$, on $\meas{\Omega}{\algF}{P}$,
integral of $X$ with respect to measure, $P$

$$
\Expect X
=
\int X dP
=
\int_\Omega X(\omega) dP
$$

called <span class="define">expected value of $X$</span>

</div>

<ul>
<li>
	$\Expect X$ is
	<ul>
	<li>
		always defined for nonnegative $X$

	</li>
	<li>
		for general case
		<ul>
		<li>
			
defined, or

		</li>
		<li>
			
$X$ has an expected value if either $\Expect X^+<\infty$ or $\Expect X^-<\infty$ or both,
in which case, $\Expect X =\Expect X^+ - \Expect X^-$

		</li>
		</ul>

	</li>
	</ul>

</li>
<li>
	$X$ is integrable if and only if $\Expect |X| <\infty$

</li>
<li>
	limits
	<ul>
	<li>
		if $\seq{X_n}$ is dominated by integral random variable
or
they are uniformly integrable,
$\Expect X_n$ converges to $\Expect X$
if $X_n$ converges to $X$ in probability

	</li>
	</ul>

</li>
</ul>

<h3>Markov and Chebyshev's inequalities</h3>

<div class="inequality" id="inequality:Markov inequality" data-name="Markov inequality">
	



for random variable, $X$, on $\meas{\Omega}{\algF}{P}$,

$$
\prob{X\geq \alpha} \leq \frac{1}{\alpha} \int_{X\geq \alpha} X d P \leq \frac{1}{\alpha} \Expect X
$$

for nonnegative $X$, hence

$$
\prob{|X|\geq \alpha} \leq \frac{1}{\alpha^n} \int_{|X|\geq \alpha} |X|^n d P \leq \frac{1}{\alpha^n} \Expect |X|^n
$$

for general $X$

</div>
<div class="inequality" id="inequality:Chebyshev's inequality" data-name="Chebyshev's inequality">
	



as special case of Markov inequality,

$$
\prob{|X-\Expect X|\geq \alpha}
\leq
\frac{1}{\alpha^2} \int_{|X-\Expect X|\geq \alpha} (X-\Expect X)^2 d P
\leq
\frac{1}{\alpha^2} \Var X
$$

for general $X$

</div>

<h3>Jensen's, Ho&#776;lder's, and Lyapunov's inequalities</h3>

<div class="inequality" id="inequality:Jensen's inequality" data-name="Jensen's inequality">
	



for random variable, $X$, on $\meas{\Omega}{\algF}{P}$,
and convex function, $\varphi$

$$
\varphi\left(\Expect X\right)
\prob{X\geq \alpha} \leq \frac{1}{\alpha} \int_{X\geq \alpha} X d P \leq \frac{1}{\alpha} \Expect X
$$


</div>
<div class="inequality" id="inequality:Holder's inequality" data-name="Holder's inequality">
	



for two random variables, $X$ and $Y$, on $\meas{\Omega}{\algF}{P}$,
and $p,q\in(1,\infty)$ with $1/p+1/q=1$

$$
\Expect |XY| \leq
\left(\Expect |X|^p\right)^{1/p}
\left(\Expect |X|^q\right)^{1/q}
$$


</div>


<div class="inequality" id="inequality:Lyapunov's inequality" data-name="Lyapunov's inequality">
	



for random variable, $X$, on $\meas{\Omega}{\algF}{P}$,
and $0<\alpha<\beta$

$$
\left(\Expect |X|^\alpha\right)^{1/\alpha}
\leq
\left(\Expect |X|^\beta\right)^{1/\beta}
$$


</div>
<ul>
<li>
	note Ho&#776;lder's inequality implies Lyapunov's inequality

</li>
</ul>

<h3>Maximal inequalities</h3>


<div class="theorem" id="theorem:Kolmogorov's zero-one law" data-name="Kolmogorov's zero-one law">
	


if $A\in\algF=\bigcap_{n=1}^\infty \sigma(X_n, X_{n+1},\ldots)$ for independent $\seq{X_n}$,

$$
\prob{A} = 0 \vee \prob{A} = 1
$$


</div>
-- define $S_n = \sum X_i$
<div class="inequality" id="inequality:Kolmogorov's maximal inequality" data-name="Kolmogorov's maximal inequality">
	


for independent $\seq{X_i}_{i=1}^n$ with $\Expect X_i =0$ and $\Var X_i<\infty$
and $\alpha>0$

$$
\prob{\max S_i \geq \alpha} \leq \frac{1}{\alpha}\Var S_n
$$


</div>
<div class="inequality" id="inequality:Etemadi's maximal inequality" data-name="Etemadi's maximal inequality">
	


for independent $\seq{X_i}_{i=1}^n$
and $\alpha>0$

$$
\prob{\max |S_i| \geq 3\alpha} \leq 3 \max \prob{|S_i|\geq\alpha}
$$


</div>

<h3>Moments</h3>

<div class="definition" id="definition:moments and absolute moments" data-name="moments and absolute moments">
	




for random variable, $X$, on $\meas{\Omega}{\algF}{P}$,
integral of $X$ with respect to measure, $P$

$$
\Expect X^n
=
\int x^k d\mu
=
\int x^k dF(x)
$$

called <span class="define">$k$-th moment</span> of $X$ or $\mu$ or $F$,
and

$$
\Expect |X|^n
=
\int |x|^k d\mu
=
\int |x|^k dF(x)
$$

called <span class="define">$k$-th absolute moment</span> of $X$ or $\mu$ or $F$

</div>
<ul>
<li>
	if $\Expect |X|^n<\infty$, $\Expect |X|^k<\infty$ for $k<n$

</li>
<li>
	$\Expect X^n$ defined only when $\Expect|X|^n<\infty$

</li>
</ul>


<h3>Moment generating functions</h3>

<div class="definition" id="definition:moment generating function" data-name="moment generating function">
	


for random variable, $X$, on $\meas{\Omega}{\algF}{P}$,
$M:\complexes \to \complexes$ defined by

$$
M(s)
=
\Expect \left( e^{sX} \right)
=
\int e^{sx} d\mu
=
\int e^{sx} dF(x)
$$

called <span class="define">moment generating function of $X$</span>

</div>
<ul>
<li>
	$n$-th derivative of $M$ with respect to $s$ is
$M^{(n)}(s) = \frac{d^n}{ds^n} F(s) = \Expect \left(X^ne^{sX}\right) = \int xe^{sx} d\mu$

</li>
<li>
	thus,
$n$-th derivative of $M$ with respect to $s$ at $s=0$ is $n$-th moment of $X$

$$
M^{(n)}(0) = \Expect X^n
$$


</li>
<li>
	for independent random variables, $\seq{X_i}_{i=1}^n$, moment generating function of $\sum X_i$

$$
\prod M_i(s)
$$


</li>
</ul>

<h2 id="Convergence of Random Variables">Convergence of Random Variables</h2>


<h3>Convergences of random variables</h3>



<div class="definition" id="definition:convergence with probability $1$" data-name="convergence with probability $1$">
	



random variables, $\seq{X_n}$,
with

$$
\prob{\lim X_n = X}
= P(\set{\omega \in \Omega}{\lim X_n(\omega) = X(\omega)})
= 1
$$

said to <span class="define">converge to $X$ with probability $1$</span>
and denoted by <span class="define">$X_n\to X$ a.s.</span>

</div>
<div class="definition" id="definition:convergence in probability" data-name="convergence in probability">
	



random variables, $\seq{X_n}$,
with

$$
\left(
\forall \epsilon>0
\right)
\left(
\lim \prob{|X_n-X|>\epsilon} = 0
\right)
$$

said to <span class="define">converge to $X$ in probability</span>

</div>
<div class="definition" id="definition:weak convergence" data-name="weak convergence">
	



distribution functions, $\seq{F_n}$, with

$$
\left(
\forall x \mbox{ in domain of }F
\right)
\left(
\lim F_n(x) = F(x)
\right)
$$

said to <span class="define">converge weakly to distribution function, $F$,</span>
and denoted by <span class="define">$F_n \Rightarrow F$</span>

</div>
<div class="definition" id="definition:converge in distribution" data-name="converge in distribution">
	



When $F_n\Rightarrow F$,
associated random variables, $\seq{X_n}$,
said to <span class="define">converge in distribution</span> to $X$, associated with $F$,
and denoted by <span class="define">$X_n \Rightarrow X$</span>

</div>
<div class="definition" id="definition:weak convergence of measures" data-name="weak convergence of measures">
	


for measures on $\measu{\reals}{\algR}$, $\seq{\mu_n}$, associated with distribution functions, $\seq{F_n}$, respectively,
and measure on $\measu{\reals}{\algR}$, $\mu$, associated with distribution function, $F$,
we denote

$$
\mu_n \Rightarrow \mu
$$

if

$$
\left(
\forall A = (-\infty, x] \mbox{ with } x\in\reals
\right)
\left(
\lim \mu_n(A) = \mu(A)
\right)
$$


</div>
<ul>
<li>
	indeed, if above equation holds for $A=(-\infty, x)$,
it holds for many other subsets

</li>
</ul>

<h3>Relations of different types of convergences of random variables</h3>




<div class="proposition" id="proposition:relations of convergence of random variables" data-name="relations of convergence of random variables">
	
convergence with probability $1$ implies convergence in probability,
which implies $X_n\Rightarrow X$, <i>i.e.</i>

$$
\begin{eqnarray*}
&&
X_n \to X \mbox{ a.s., \ie, } X_n \mbox{ converge to } X \mbox{ with probability $1$}
\\
&\Rightarrow&
X_n \mbox{ converge to } X \mbox{ in probability}
\\
&\Rightarrow&
X_n \Rightarrow X \mbox{, \ie, } X_n \mbox{ converge to } X \mbox{ in distribution},
\end{eqnarray*}
$$


</div>

<h3>Necessary and sufficient conditions for convergence of probability</h3>





$$
{X_n}\ \mbox{ converge in probability}
$$

if and only if

$$
\left(
\forall \epsilon>0
\right)
\left(
\prob{|X_n-X|>\epsilon\mbox{ i.o}}
=
\prob{\limsup |X_n-X| > \epsilon } = 0
\right)
$$

if and only if

$$
\left(
\forall \mbox{ subsequence }\seq{X_{n_k}}
\right)
\left(
\exists \mbox{ its subsequence }\seq{X_{n_{k_l}}} \mbox{ converging to } f \mbox{ with probability } 1
\right)
$$


<h3>Necessary and sufficient conditions for convergence in distribution</h3>





$$
X_n\Rightarrow X, \mbox{\ie, $X_n$ converge in distribution}
$$

if and only if

$$
F_n\Rightarrow F, \mbox{\ie, $F_n$ converge weakly}
$$

if and only if

$$
\left(
\forall A = (-\infty, x] \mbox{ with } x\in\reals
\right)
\left(
\lim \mu_n(A) = \mu(A)
\right)
$$

if and only if

$$
\left(
\forall x \mbox{ with } \prob{X=x} = 0
\right)
\left(
\lim \prob{X_n\leq x} = \prob{X\leq x}
\right)
$$


<h3>Strong law of large numbers</h3>

-- define $S_n = \sum_{i=1}^n X_i$
<div class="theorem" id="theorem:strong law of large numbers" data-name="strong law of large numbers">
	


for sequence of independent and identically distributed (i.i.d.) random variables
with finite mean, $\seq{X_n}$

$$
\frac{1}{n} S_n \to \Expect X_1
$$

with probability $1$

</div>
<ul>
<li>
	strong law of large numbers also called <span class="define">Kolmogorov's law</span>




</li>
</ul>
<div class="corollary" id="corollary:strong law of large numbers" data-name="strong law of large numbers">
	
for sequence of independent and identically distributed (i.i.d.) random variables
with $\Expect X_1^- < \infty$ and $\Expect X_1^+ = \infty$ (hence, $\Expect X = \infty$)

$$
\frac{1}{n} S_n \to \infty
$$

with probability $1$

</div>

<h3>Weak law of large numbers</h3>

-- define $S_n = \sum_{i=1}^n X_i$
<div class="theorem" id="theorem:weak law of large numbers" data-name="weak law of large numbers">
	


for sequence of independent and identically distributed (i.i.d.) random variables
with finite mean, $\seq{X_n}$

$$
\frac{1}{n} S_n \to \Expect X_1
$$

in probability

</div>
<ul>
<li>
	because convergence with probability $1$ implies convergence in probability
(<a href="#proposition:relations of convergence of random variables"></a>),
strong law of large numbers
implies
weak law of large numbers

</li>
</ul>

<h3>Normal distributions</h3>



-- assume probability space, $\meas{\Omega}{\algF}{P}$
<div class="definition" id="definition:normal distributions" data-name="normal distributions">
	


Random variable, $X:\Omega\to\reals$, with

$$
\left(
A\in\algR
\right)
\left(
\prob{X\in A} = \frac{1}{\sqrt{2\pi}\sigma} \int_A e^{-(x-c)^2/2} d\mu
\right)
$$

where $\mu=PX^{-1}$
for some $\sigma>0$ and $c\in\reals$,
called <span class="define">normal distribution</span>
and denoted by <span class="define">$X \sim \normal(c,\sigma^2)$</span>

</div>
<ul>
<li>
	
note $\Expect X=c$ and $\Var X=\sigma^2$

</li>
<li>
	
called <span class="define">standard normal distribution</span>
when $c=0$ and $\sigma=1$



</li>
</ul>

<h3>Multivariate normal distributions</h3>



-- assume probability space, $\meas{\Omega}{\algF}{P}$
<div class="definition" id="definition:multivariate normal distributions" data-name="multivariate normal distributions">
	


Random variable, $X:\Omega\to\reals^n$, with

$$
\left(
A\in\algR^n
\right)
\left(
\prob{X\in A} = \frac{1}{\sqrt{(2\pi)^n}\sqrt{\det \Sigma}} \int_A e^{-(x-c)^T\Sigma^{-1}(x-c)/2} d\mu
\right)
$$

where $\mu=PX^{-1}$
for some $\Sigma\succ0\in\posdefset{n}$ and $c\in\reals^n$,
called <span class="define">($n$-dimensional) normal distribution</span>,
and denoted by <span class="define">$X \sim \normal(c,\Sigma)$</span>

</div>
<ul>
<li>
	
note that $\Expect X=c$ and covariance matrix is $\Sigma$

</li>
</ul>

<h3>Lindeberg-Le&#769;vy theorem</h3>





-- define $S_n = \sum^n X_i$
<div class="theorem" id="theorem:Lindeberg-Levy theorem" data-name="Lindeberg-Levy theorem">
	




for independent random variables, $\seq{X_n}$, having same distribution with expected value, $c$, and same variance, $\sigma^2<\infty$,
${(S_n - nc)}/{\sigma\sqrt{n}}$ converges to standard normal distribution in distribution, <i>i.e.</i>,

$$
\frac{S_n - nc}{\sigma\sqrt{n}} \Rightarrow N
$$

where $N$ is standard normal distribution

</div>
<ul>
<li>
	
<a href="#theorem:Lindeberg-Levy theorem"></a> implies

$$
S_n / n \Rightarrow c
$$


</li>
</ul>

<h3>Limit theorems in $\reals^n$</h3>



<div class="theorem" id="theorem:equivalent statements to weak convergence" data-name="equivalent statements to weak convergence">
	
each of following statements are equivalent to
weak convergence of measures, $\seq{\mu_n}$, to $\mu$,
on measurable space, $\measu{\reals^k}{\algR^k}$
	<ul>
	<li>
		$\lim \int f d\mu_n = \int f d\mu$ for every bounded continuous $f$

	</li>
	<li>
		$\limsup \mu_n(C) \leq \mu(C)$ for every closed $C$

	</li>
	<li>
		$\liminf \mu_n(G) \geq \mu(G)$ for every open $G$

	</li>
	<li>
		$\lim \mu_n(A) = \mu(A)$ for every $\mu$-continuity $A$

	</li>
	</ul>

</div>
<div class="theorem" id="theorem:convergence in distribution of random vector" data-name="convergence in distribution of random vector">
	
for random vectors, $\seq{X_n}$, and random vector, $Y$, of $k$-dimension,
$X_n\Rightarrow Y$, <i>i.e.</i>, $X_n$ converge to $Y$ in distribution
if and only if

$$
\left(
\forall z\in \reals^k
\right)
\left(
z^T X_n \Rightarrow z^T Y
\right)
$$


</div>

<h3>Central limit theorem</h3>




-- assume probability space, $\meas{\Omega}{\algF}{P}$ and define $\sum^n X_i = S_n$
<div class="theorem" id="theorem:central limit theorem" data-name="central limit theorem">
	
for random variables, $\seq{X_n}$, having same distributions with $\Expect X_n = c\in\reals^k$
and positive definite covariance matrix, $\Sigma\succ0\in\mathcalfont{S}_k$,
<i>i.e.</i>, $\Expect(X_n-c)(X_n-c)^T = \Sigma$,
where $\Sigma_{ii} < \infty$ (hence $\Sigma \prec M I_n$ for some $M\in\ppreals$ due to Cauchy-Schwarz inequality),

$$
(S_n -nc)/\sqrt{n} \mbox{ converges in distribution to } Y
$$

where $Y \sim \normal(0,\Sigma)$

</div>


<h3>Convergence of random series</h3>


<ul>
<li>
	for independent $\seq{X_n}$, probability of $\sum X_n$ converging is either $0$ or $1$

</li>
<li>
	below characterize two cases in terms of distributions of individual $X_n$
-- XXX: diagram


</li>
</ul>
<div class="theorem" id="theorem:convergence with probability 1 for random series" data-name="convergence with probability 1 for random series">
	
for independent $\seq{X_n}$ with $\Expect X_n=0$ and $\Var X_n < \infty$

$$
\sum X_n \mbox{ converges with probability $1$}
$$


</div>
<div class="theorem" id="theorem:convergence conditions for random series" data-name="convergence conditions for random series">
	
for independent $\seq{X_n}$,
$\sum X_n$ converges with probability $1$
if and only if
they converges in probability

</div>

-- define trucated version of $X_n$ by $X_n^{(c)}$, <i>i.e.</i>, $X_n I_{|X_n|\leq c}$
<div class="theorem" id="theorem:convergence conditions for truncated random series" data-name="convergence conditions for truncated random series">
	
for independent $\seq{X_n}$,

$$
\begin{eqnarray*}
&=&
\sum X_n
\mbox{ converge with probability $1$}

\\
&&
\mbox{if all of }
\sum \prob{|X_n|>c},
\sum \Expect(X_n^{(c)}),
\sum \Var(X_n^{(c)})
\mbox{ converge for some }c>0
\end{eqnarray*}
$$


</div>

