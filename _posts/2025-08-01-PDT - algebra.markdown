---
title: Inequalities and Number Theory
date: Fri Aug  1 01:00:00 PDT 2025
last_modified_at: Tue Aug  5 01:35:45 PDT 2025
permalink: /math/rig/algebra
categories:
- blog
tags:
- math
- algebra
- inequalities
- Cauchy-Schwarz inequality
- Jensen's inequality
- AM-GM inequality
- number theory
- RSA cryptography algorithm
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

- [14:49](https://notebooklm.google.com/notebook/59cd104b-0127-47f9-a12e-26afe0bedfd9/audio)
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


<h1 id="super-title-page:algebra">Algebra</h1>



<h2 id="title-page:Inequalities">Inequalities</h2>


<h3>Jensen's inequality</h3>

<ul>
<li>
	strictly convex function: for any $x\neq y$ and $0< \alpha <1$


(<a href="#definition:convex---functions"></a>)

$$

\alpha f(x) + (1-\alpha) f(y) > f(\alpha x + (1-\alpha) y)

$$


</li>
<li>
	convex function: for any $x, y$ and $0< \alpha <1$

(<a href="#definition:convex---functions"></a>)

$$

\alpha f(x) + (1-\alpha) f(y) \geq f(\alpha x + (1-\alpha) y)

$$


</li>
</ul>
<div class="inequality" id="inequality:Jensen's---inequality-------for---finite---sequences" data-name="Jensen's inequality - for finite sequences">
	


for convex function $f$ and <i>distinct</i> $x_i$
and $0< \alpha_i <1$ with $\alpha_1 + \cdots = \alpha_n=1$




$$

\alpha_1 f(x_1) + \cdots + \alpha_n f(x_n) \geq f(\alpha_1 x_1 + \cdots + \alpha_n x_n)

$$

	<ul>
	<li>
		if $f$ is strictly convex, equality holds if and only if $x_1=\cdots=x_n$

	</li>
	</ul>

</div>

<h3>Jensen's inequality - for random variables</h3>

<ul>
<li>
	discrete random variable interpretation of Jensen's inequality in summation form - assume $\Prob(X=x_i) = \alpha_i$, then

$$

\Expect f(X)
=
\alpha_1 f(x_1) + \cdots + \alpha_n f(x_n)
\geq
f(\alpha_1 x_1 + \cdots + \alpha_n x_n)
=
f\left(\Expect X\right)

$$


</li>
<li>
	true for any random variables $X$

</li>
</ul>

<div class="inequality" id="inequality:Jensen's---inequality-------for---random---variables" data-name="Jensen's inequality - for random variables">
	


for random vector $X$ (page~<a href="#page:random-variables">here</a> for definition)

$$

\Expect f(X) \geq f(\Expect X)

$$

if probability density function (PDF) $p_X$ given,

$$

\int f(x) p_X(x) dx \geq f\left(\int x p_X(x) dx\right)

$$


</div>


<h3>Proof for $n=3$</h3>

<ul>
<li>
	for any $x,y,z$ and $\alpha,\beta,\gamma>0$ with $\alpha + \beta + \gamma = 1$

$$
\begin{eqnarray*}

\alpha f(x) + \beta f(y) + \gamma f(z)
&=&
(\alpha+\beta)\left(\frac{\alpha}{\alpha+\beta} f(x) + \frac{\beta}{\alpha + \beta} f(y)\right) + \gamma f(z)
\\
&\geq&
(\alpha+\beta)f\left(\frac{\alpha}{\alpha+\beta} x + \frac{\beta}{\alpha + \beta} y\right) + \gamma f(z)
\\
&\geq&
f\left((\alpha+\beta)\left(\frac{\alpha}{\alpha+\beta} x + \frac{\beta}{\alpha + \beta} y\right) + \gamma z \right)
\\
&=&
f(\alpha x + \beta y + \gamma z )

\end{eqnarray*}
$$


</li>
</ul>

<h3>Proof for all $n$</h3>

<ul>
<li>
	use mathematical induction
	<ul>
	<li>
		assume that Jensen's inequality holds for $1\leq n\leq m$

	</li>
	<li>
		for distinct $x_i$ and $\alpha_i>0$ ($1\leq i\leq m+1$) with $\alpha_1 + \cdots + \alpha_{m+1} = 1$

$$
\begin{eqnarray*}

\sum^{m+1}_{i=1} \alpha_i f(x_i)
&=&
\left(\sum^m_{j=1} \alpha_j\right) \sum^m_{i=1} \left(\frac{\alpha_i}{\sum^m_{j=1} \alpha_j} f(x_i)\right) + \alpha_{m+1} f(x_{m+1})
\\
&\geq&
\left(\sum^m_{j=1} \alpha_j\right) f\left(\sum^m_{i=1} \left(\frac{\alpha_i}{\sum^m_{j=1} \alpha_j} x_i\right)\right) + \alpha_{m+1} f(x_{m+1})
\\
&=&
\left(\sum^m_{j=1} \alpha_j\right) f\left(\frac{1}{\sum^m_{j=1} \alpha_j}\sum^m_{i=1} {\alpha_i}{} x_i\right) + \alpha_{m+1} f(x_{m+1})
\\
&\geq&
f\left( \sum^m_{i=1} \alpha_i x_i + \alpha_{m+1} x_{m+1}\right)
=
f\left( \sum^{m+1}_{i=1} \alpha_i x_i \right)

\end{eqnarray*}
$$


	</li>
	</ul>

</li>
</ul>

<h3>1st and 2nd order conditions for convexity</h3>

<ul>
<li>
	1st order condition (assuming differentiable $f:\reals\to\reals$)
- $f$ is strictly convex if and only if for any $x\neq y$


$$

f(y) > f(x) + f'(x)(y-x)

$$


</li>
<li>
	2nd order condition (assuming twice-differentiable $f:\reals\to\reals$)

	<ul>
	<li>
		if $f''(x)>0$, $f$ is strictly convex

	</li>
	<li>
		$f$ is convex if and only if for any $x$

$$

f''(x) \geq 0

$$


	</li>
	</ul>

</li>
</ul>


<h3>Jensen's inequality examples</h3>

<ul>
<li>
	$f(x)=x^2$ is strictly convex

$$

\frac{a^2 + b^2}{2}
\geq
\left(\frac{a+b}{2}\right)^2

$$


</li>
<li>
	$f(x)=x^4$ is strictly convex

$$

\frac{a^4 + b^4}{2}
\geq
\left(\frac{a+b}{2}\right)^4

$$


</li>
<li>
	$f(x)=\exp(x)$ is strictly convex

$$

\frac{\exp(a) + \exp(b)}{2}
\geq
\exp\left(\frac{a+b}{2}\right)

$$


</li>
<li>
	equality holds if and only if $a=b$ for all inequalities

</li>
</ul>

<h3>1st and 2nd order conditions for convexity - vector version</h3>

<ul>
<li>
	1st order condition (assuming differentiable $f:\reals^n\to\reals$)
- $f$ is strict convex if and only if for any $x,y$


$$

f(y) > f(x) + \nabla f(x)^T (y-x)

$$

where $\nabla f(x) \in\reals^{n}$ with $\nabla f(x)_{i} = \partial f(x) / \partial x_i$

</li>
<li>
	2nd order condition (assuming twice-differentiable $f:\reals^n\to\reals$)

	<ul>
	<li>
		if $\nabla^2 f(x) \succ 0$, $f$ is strictly convex

	</li>
	<li>
		$f$ is convex if and only if for any $x$

$$

\nabla^2 f(x)\succeq 0

$$


	</li>
	</ul>
where $\nabla^2 f(x) \in\reals^{n\times n}$
is Hessian matrix of $f$ evaluated at $x$,
<i>i.e.</i>,
$\nabla^2 f(x)_{i,j} = \partial^2 f(x) / \partial x_i \partial x_j$

</li>
</ul>


<h3>Jensen's inequality examples - vector version</h3>

<ul>
<li>
	assume $f:\reals^n\to\reals$

</li>
<li>
	$f(x)=\|x\|_2 = \sqrt{\sum x_i^2}$ is strictly convex

$$

(\|a\|_2 + 2\|b\|_2 )/3
\geq
\left\|(a+2b)/3\right\|_2

$$

	<ul>
	<li>
		equality holds if and only if $a=b\in\reals^n$

	</li>
	</ul>

</li>
<li>
	$f(x)=\|x\|_p = \left(\sum |x_i|^p\right)^{1/p}$ ($p>1$) is strictly convex

$$

\frac{1}{k}
\left(\sum_{i=1}^k\|x^{(i)}\|_p \right)
\geq
\left\|\frac{1}{k}\sum_{i=1}^k x^{(i)}\right\|_p

$$

	<ul>
	<li>
		equality holds if and only if $x^{(1)}=\cdots=x^{(k)}\in\reals^n$

	</li>
	</ul>

</li>
</ul>

<h3>AM $\geq$ GM</h3>

<ul>
<li>
	for all $a,b>0$

$$

\frac{a + b}{2} \geq \sqrt{ab}

$$

	<ul>
	<li>
		equality holds if and only if $a=b$

	</li>
	</ul>

</li>
<li>
	below most general form holds

</li>
</ul>
<div class="inequality" id="inequality:AM-GM---inequality" data-name="AM-GM inequality">
	
for any $n$ $a_i>0$ and $\alpha_i>0$ with $\alpha_1+\cdots+\alpha_n=1$

$$

\alpha_1 a_1 + \cdots + \alpha_n a_n
\geq
{a_1^{\alpha_1} \cdots a_n^{\alpha_n}}

$$

where equality holds if and only if $a_1=\cdots=a_n$

</div>
<ul>
<li>
	let's prove these incrementally
(for rational $\alpha_i$)

</li>
</ul>


<h3>Proof of AM $\geq$ GM - simplest case</h3>

<ul>
<li>
	use fact that $x^2\geq0$ for any $x\in\reals$

</li>
<li>
	for any $a,b>0$

$$
\begin{eqnarray*}

&&
(\sqrt{a}-\sqrt{b})^2 \geq 0
\\
&\Leftrightarrow&
a^2 - 2\sqrt{ab} + b^2 \geq 0
\\
&\Leftrightarrow&
a + b \geq 2\sqrt{ab}
\\
&\Leftrightarrow&
\frac{a + b}{2} \geq \sqrt{ab}

\end{eqnarray*}
$$

	<ul>
	<li>
		equality holds if and only if $a=b$

	</li>
	</ul>

</li>
</ul>

<h3>Proof of AM $\geq$ GM - when $n=4$ and $n=8$</h3>

<ul>
<li>
	for any $a,b,c,d>0$
$$
\begin{eqnarray*}

\frac{a+b+c+d}{4}
&\geq&
\frac{2\sqrt{ab} + 2\sqrt{cd}}{4}
=
\frac{\sqrt{ab} + \sqrt{cd}}{2}

\\
&\geq&
\sqrt{\sqrt{ab} \sqrt{cd}}
=
\sqrt[4]{abcd}

\end{eqnarray*}
$$
	<ul>
	<li>
		equality holds if and only if $a=b$ and $c=d$ and $ab=cd$
if and only if $a=b=c=d$

	</li>
	</ul>

</li>
<li>
	likewise, for $a_1,\ldots,a_8>0$

$$
\begin{eqnarray*}

\frac{a_1+\cdots+a_8}{8}
&\geq&
\frac{\sqrt{a_1a_2} + \sqrt{a_3a_4} + \sqrt{a_5a_6} + \sqrt{a_7a_8}}{4}
\\
&\geq&
\sqrt[4]{\sqrt{a_1a_2} \sqrt{a_3a_4} \sqrt{a_5a_6} \sqrt{a_7a_8}}
\\
&=&
\sqrt[8]{a_1\cdots a_8}

\end{eqnarray*}
$$

	<ul>
	<li>
		equality holds if and only if $a_1=\cdots=a_8$

	</li>
	</ul>

</li>
</ul>

<h3>Proof of AM $\geq$ GM - when $n=2^m$</h3>

<ul>
<li>
	generalized to cases $n=2^m$

$$

\left(\sum_{a=1}^{2^m} a_i\right) / 2^m\geq \left({\prod_{a=1}^{2^m} a_i}\right)^{1/2^m}

$$

	<ul>
	<li>
		equality holds if and only if $a_1=\cdots=a_{2^m}$

	</li>
	</ul>

</li>
<li>
	can be proved by <i>mathematical induction</i>

</li>
</ul>

<h3>Proof of AM $\geq$ GM - when $n=3$</h3>

<ul>
<li>
	proof for $n=3$

$$
\begin{eqnarray*}

\frac{a+b+c}{3} &=& \frac{a + b + c + (a+b+c)/3}{4}
\geq \sqrt[4]{abc(a+b+c)/3}
\\
&\Rightarrow&
\left(\frac{a+b+c}{3}\right)^4 \geq {abc(a+b+c)/3}
\\
&\Leftrightarrow&
\left(\frac{a+b+c}{3}\right)^3 \geq abc
\\
&\Leftrightarrow&
\frac{a+b+c}{3} \geq \sqrt[3]{abc}

\end{eqnarray*}
$$

	<ul>
	<li>
		equality holds if and only if $a=b=c=(a+b+c)/3$ if and only if $a=b=c$

	</li>
	</ul>

</li>
</ul>

<h3>Proof of AM $\geq$ GM - for all integers</h3>

<ul>
<li>
	for any integer $n\neq 2^m$

</li>
<li>
	for $m$ such that $2^m>n$

$$
\begin{eqnarray*}

\frac{a_1+\cdots+a_n}{n} &=& \frac{a_1 + \cdots + a_n + (2^m-n) (a_1+\cdots+a_n) /n}{2^m}
\\
&&
\geq
\sqrt[2^m]{a_1\cdots a_n \cdot ((a_1 + \cdots + a_n)/n)^{2^m-n}}
\\
&\Leftrightarrow&
\left(\frac{a_1+\cdots+a_n}{n}\right)^{2^m}
\geq
a_1\cdots a_n 
\\
&&\cdot \left(\frac{a_1 + \cdots + a_n}{n}\right)^{2^m-n}
\\
&\Leftrightarrow&
\left(\frac{a_1+\cdots+a_n}{n}\right)^{n}
\geq
{a_1\cdots a_n}
\\
&\Leftrightarrow&
\frac{a_1+\cdots+a_n}{n}
\geq
\sqrt[n]{a_1\cdots a_n}

\end{eqnarray*}
$$

	<ul>
	<li>
		equality holds if and only if $a_1=\cdots=a_n$

	</li>
	</ul>

</li>
</ul>

<h3>Proof of AM $\geq$ GM - rational $\alpha_i$</h3>

<ul>
<li>
	given $n$ positive rational $\alpha_i$,
we can find $n$ natural numbers $q_i$
such that

$$

\alpha_i = \frac{q_i}{ N}

$$

where $q_1+\cdots+q_n=N$

</li>
<li>
	for any $n$ positive $a_i\in\reals$ and positive $n$ $\alpha_i\in\rationals$ with $\alpha_1+\cdots+\alpha_n=1$
$$
\begin{eqnarray*}

\alpha_1 a_1 + \cdots + \alpha_n a_n
&=& \frac{q_1 a_1 + \cdots + q_n a_n}{N}

\\
&&\geq \sqrt[N]{a_1^{q_1}\cdots a_n^{q_n}}
= a_1^{\alpha_1}\cdots a_n^{\alpha_n}

\end{eqnarray*}
$$
	<ul>
	<li>
		equality holds if and only if $a_1=\cdots=a_n$

	</li>
	</ul>

</li>
</ul>

<h3>Proof of AM $\geq$ GM - real $\alpha_i$</h3>

<ul>
<li>
	exist $n$ rational sequences $\{ \beta_{i,1}, \beta_{i,2}, \ldots\}$ ($1\leq i\leq n$) such that

$$
\begin{eqnarray*}

&&
\beta_{1,j}+\cdots+\beta_{n,j}=1 \ \forall \ j\geq1
\\
&&
\lim_{j\to\infty} \beta_{i,j} = \alpha_i \ \forall \ 1\leq i\leq n

\end{eqnarray*}
$$


</li>
<li>
	for all $j$

$$

\beta_{1,j} a_1 + \cdots + \beta_{n,j} a_n
\geq
a_1^{\beta_{1,j}}\cdots a_n^{\beta_{n,j}}

$$

hence

$$
\begin{eqnarray*}

&&
\lim_{j\to\infty} \left(\beta_{1,j} a_1 + \cdots + \beta_{n,j} a_n \right)
\geq
\lim_{j\to\infty} a_1^{\beta_{1,j}}\cdots a_n^{\beta_{n,j}}
\\
&\Leftrightarrow&
\alpha_1 a_1 + \cdots + \alpha_n a_n
\geq
a_1^{\alpha_1}\cdots a_n^{\alpha_n}

\end{eqnarray*}
$$


</li>
<li>
	<i>cannot</i> prove equality condition from above proof method

</li>
</ul>

<h3>Proof of AM $\geq$ GM using Jensen's inequality</h3>

<ul>
<li>
	$(-\log)$ is strictly convex function because

$$

\frac{d^2}{dx^2} \left(-\log(x)\right)
= \frac{d}{dx} \left(-\frac{1}{x} \right)
= \frac{1}{x^2} > 0

$$


</li>
<li>
	Jensen's inequality implies for $a_i >0$, $\alpha_i >0$ with $\sum \alpha_i = 1$
$$
\begin{eqnarray*}

-\log\left(\prod a_i^{\alpha_i}\right)
&=& -\sum \log\left( a_i^{\alpha_i}\right)

\\
&=&
\sum \alpha_i (-\log(a_i))

\\
&\geq& -\log \left(\sum \alpha_i a_i\right)

\end{eqnarray*}
$$

</li>
<li>
	$(-\log)$ strictly monotonically decreases, hence $\prod a_i^{\alpha_i} \leq \sum \alpha_i a_i$,
having just proved

$$

\alpha_1 a_1 + \cdots + \alpha_n a_n
\geq
a_1^{\alpha_1}\cdots a_n^{\alpha_n}

$$

where equality if and only if $a_i$ are equal
(by Jensen's inequality's equality condition)

</li>
</ul>

<h3>Cauchy-Schwarz inequality</h3>

<div class="inequality" id="inequality:Cauchy-Schwarz---inequality" data-name="Cauchy-Schwarz inequality">
	
for any $a_i, b_i\in\reals$





$$

( a_1^2 + \cdots + a_n^2 )
( b_1^2 + \cdots + b_n^2 )
\geq
(a_1b_1 + \cdots + a_nb_n)^2

$$


</div>
<ul>
<li>
	middle school proof

$$
\begin{eqnarray*}

&&\sum (t a_i + b_i)^2 \geq 0 \ \forall\ t \in \reals
\\
&\Leftrightarrow&
t^2 \sum a_i^2 + 2t \sum a_ib_i + \sum b_i^2 \geq 0 \ \forall\ t \in \reals
\\
&\Leftrightarrow&
\Delta = \left(\sum a_ib_i \right)^2 - \sum a_i^2 \sum b_i^2 \leq 0

\end{eqnarray*}
$$

	<ul>
	<li>
		equality holds if and only if $\exists t\in\reals$, $t a_i + b_i=0$ for all $1\leq i\leq n$

	</li>
	</ul>

</li>
</ul>

<h3>Cauchy-Schwarz inequality - another proof</h3>

<ul>
<li>
	$x\geq0$ for any $x\in\reals$, hence

$$
\begin{eqnarray*}

&&
\sum_i \sum_j (a_ib_j - a_jb_i)^2 \geq0
\\
&\Leftrightarrow&
\sum_i \sum_j (a_i^2b_j^2 - 2a_ia_jb_ib_j + a_j^2b_i^2) \geq0
\\
&\Leftrightarrow&
\sum_i \sum_j a_i^2b_j^2 + \sum_i \sum_j a_j^2b_i^2 -2 \sum_i \sum_j a_ia_jb_ib_j \geq 0
\\
&\Leftrightarrow&
2 \sum_i a_i^2 \sum_j b_j^2 - 2 \sum_i a_ib_i \sum_j a_jb_j \geq 0
\\
&\Leftrightarrow&
\sum_i a_i^2 \sum_j b_j^2 - \left(\sum_i a_ib_i\right)^2 \geq0

\end{eqnarray*}
$$

	<ul>
	<li>
		equality holds if and only if $a_ib_j=a_jb_i$ for all $1\leq i,j\leq n$

	</li>
	</ul>

</li>
</ul>

<h3>Cauchy-Schwarz inequality - still another proof</h3>

<ul>
<li>
	for any $x,y\in\reals$ and $\alpha,\beta>0$ with $\alpha + \beta = 1$

$$
\begin{eqnarray*}

&&
(\alpha x - \beta y)^2
=
\alpha^2 x^2 + \beta^2 y^2 - 2\alpha \beta xy
\\
&&
=
\alpha(1-\beta) x^2 + (1-\alpha)\beta y^2 - 2\alpha \beta xy
\geq
0
\\
&\Leftrightarrow&
\alpha x^2 + \beta y^2
\geq
\alpha \beta x^2 + \alpha \beta y^2 + 2\alpha \beta xy
= \alpha \beta (x+y)^2
\\
&\Leftrightarrow&
x^2 / \alpha + y^2 / \beta \geq (x+y)^2

\end{eqnarray*}
$$


</li>
<li>
	plug in $x=a_i$, $y=b_i$, $\alpha = A/(A+B)$, $\beta=B/(A+B)$
where $A = \sqrt{\sum a_i^2}$, $B = \sqrt{\sum b_i^2}$

$$
\begin{eqnarray*}

&&
\sum (a_i^2 / \alpha + b_i^2 / \beta) \geq \sum (a_i+b_i)^2

\\
&\Leftrightarrow&
(A+B)^2 \geq A^2 + B^2 + 2 \sum a_i b_i
\\
&\Leftrightarrow&
AB \geq \sum a_i b_i

\\
&\Leftrightarrow&
A^2B^2 \geq \left(\sum a_i b_i\right)^2

\\
&\Leftrightarrow&
{\sum a_i^2}{\sum b_i^2} \geq \left(\sum a_i b_i \right)^2

\end{eqnarray*}
$$


</li>
</ul>

<h3>Cauchy-Schwarz inequality - proof using determinant</h3>

<ul>
<li>
	almost the same proof as first one - but using $2$-by-$2$ matrix determinant

$$
\begin{eqnarray*}

&&\sum (x a_i + y b_i )^2 \geq 0 \ \forall\ x,y \in \reals
\\
&\Leftrightarrow&
x^2 \sum a_i^2 + 2xy \sum a_ib_i + y^2\sum b_i^2 \geq 0 \ \forall \ x, y \in \reals
\\
&\Leftrightarrow&
\begin{my-matrix}{cc}
x & y
\end{my-matrix}
\begin{my-matrix}{cc}
\sum a_i^2 & \sum a_ib_i
\\
\sum a_ib_i & \sum b_i^2
\end{my-matrix}
\begin{my-matrix}{c}
x \\ y
\end{my-matrix}
\geq 0
\ \forall \ x, y \in \reals
\\
\\
&\Leftrightarrow&
\left|
\begin{array}{cc}
\sum a_i^2 & \sum a_ib_i
\\
\sum a_ib_i & \sum b_i^2
\end{array}
\right|
\geq 0

\\
&\Leftrightarrow&
\sum a_i^2 \sum b_i^2 - \left(\sum a_ib_i \right)^2 \geq0

\end{eqnarray*}
$$

	<ul>
	<li>
		equality holds if and only if

$$

\left(
\exists x,y\in\reals \mbox{ with } xy\neq0
\right)
\left(
xa_i + yb_i=0\ \
\forall 1\leq i\leq n
\right)

$$


	</li>
	</ul>

</li>
<li>
	allows <span class="eemph">beautiful generalization</span> of Cauchy-Schwarz inequality

</li>
</ul>

<h3>Cauchy-Schwarz inequality - generalization</h3>




<div id="page:Cauchy-Schwarz---inequality-------generalization"></div>
<ul>
<li>
	want to say something like $\sum_{i=1}^n (x a_i + y b_i + z c_i + w d_i + \cdots)^2$

</li>
<li>
	run out of alphabets &hellip; - use double subscripts

$$
\begin{eqnarray*}

&&
\sum_{i=1}^n (x_1 A_{1,i} + x_2 A_{2,i} + \cdots + x_m A_{m,i})^2 \geq 0 \ \forall\ x_i \in \reals
\\
&\Leftrightarrow&
\sum_{i=1}^n (x^T a_i)^2
=
\sum_{i=1}^n x^T a_ia_i^T x
=
x^T \left(\sum_{i=1}^n a_ia_i^T\right) x \geq 0 \ \forall\ x \in \reals^m
\\
&\Leftrightarrow&
\left|
\begin{array}{cccc}
\sum_{i=1}^n A_{1,i}^2 & \sum_{i=1}^n A_{1,i} A_{2,i} & \cdots & \sum_{i=1}^n A_{1,i} A_{m,i}
\\
\sum_{i=1}^n A_{1,i}A_{2,i} & \sum_{i=1}^n A_{2,i}^2 & \cdots & \sum_{i=1}^n A_{2,i} A_{m,i}
\\
\vdots & \vdots & \ddots & \vdots
\\
\sum_{i=1}^n A_{1,i}A_{m,i} & \sum_{i=1}^n A_{2,i}A_{m,i} & \cdots & \sum_{i=1}^n A_{m,i}^2
\end{array}
\right|
\geq 0

\end{eqnarray*}
$$


	<ul>
	<li>
		
where $a_i = \begin{my-matrix}{ccc} A_{1,i} &\cdots & A_{m,i}\end{my-matrix}^T \in\reals^m$

	</li>
	<li>
		equality holds if and only if $\exists x\neq0\in\reals^m$, $x^Ta_i =0$ for all $1\leq i\leq n$

	</li>
	</ul>

</li>
</ul>

<h3>Cauchy-Schwarz inequality - three series of variables</h3>

<ul>
<li>
	let $m=3$

$$
\begin{eqnarray*}

&&
\begin{my-matrix}{ccc}
\sum a_{i}^2 & \sum a_{i} b_{i} & \sum a_{i} c_{i}
\\
\sum a_{i}b_{i} & \sum b_{i}^2 & \sum b_{i} c_{i}
\\
\sum a_{i}c_{i} & \sum b_{i}c_{i} & \sum c_{i}^2
\end{my-matrix}
\succeq 0
\\
&\Rightarrow&
\sum a_i^2 \sum b_i^2 \sum c_i^2 + 2 \sum a_ib_i \sum b_ic_i \sum c_ia_i
\\
&&
\geq \sum a_i^2 \left(\sum b_i c_i\right)^2 + \sum b_i^2 \left(\sum a_i c_i\right)^2 + \sum c_i^2 \left(\sum a_i b_i\right)^2

\end{eqnarray*}
$$

	<ul>
	<li>
		equality holds if and only if $\exists x,y,z\in\reals$, $xa_i + yb_i + zc_i=0$ for all $1\leq i\leq n$

	</li>
	</ul>

</li>
<li>
	questions for you
	<ul>
	<li>
		what does this mean?

	</li>
	<li>
		any real-world applications?

	</li>
	</ul>

</li>
</ul>

<h3>Cauchy-Schwarz inequality - extensions</h3>




<div class="inequality" id="inequality:Cauchy-Schwarz---inequality-------for---complex---numbers" data-name="Cauchy-Schwarz inequality - for complex numbers">
	



for $a_i, b_i \in\complexes$

$$

\sum |a_i|^2 \sum |b_i|^2 \geq \left|\sum a_i b_i \right|^2

$$


</div>

<div class="inequality" id="inequality:Cauchy-Schwarz---inequality-------for---infinite---sequences" data-name="Cauchy-Schwarz inequality - for infinite sequences">
	



for two complex infinite sequences
$\seq{a_i}_{i=1}^\infty$
and
$\seq{b_i}_{i=1}^\infty$

$$

\sum^\infty_{i=1} |a_i|^2 \sum^\infty_{i=1} |b_i|^2 \geq \left|\sum^\infty_{i=1} a_i b_i \right|^2

$$


</div>

<div class="inequality" id="inequality:Cauchy-Schwarz---inequality-------for---complex---functions" data-name="Cauchy-Schwarz inequality - for complex functions">
	



for two complex functions $f,g:[0,1] \to \complexes$

$$

\int |f|^2 \int |g|^2 \geq \left|\int f g \right|^2

$$


</div>
<ul>
<li>
	note that <span class="eemph">all these can be further generalized
as in page~\pageref{page:Cauchy-Schwarz inequality - generalization}</span>

</li>
</ul>

<h2 id="title-page:number-theory">Number Theory - Queen of Mathematics</h2>


<h3>Integers</h3>

<ul>
<li>
	integers ($\integers$)
-
$\ldots -2, -1, 0, 1, 2, \ldots$
	<ul>
	<li>
		first defined by Bertrand Russell

	</li>
	<li>
		algebraic structure - commutative ring
		<ul>
		<li>
			
addition, multiplication defined, but divison <i>not</i> defined

		</li>
		<li>
			
addition, multiplication are associative

		</li>
		<li>
			
multiplication distributive over addition

		</li>
		<li>
			
addition, multiplication are commutative

		</li>
		</ul>

	</li>
	</ul>

</li>
<li>
	natural numbers ($\naturals$)
	<ul>
	<li>
		$1, 2, \ldots$

	</li>
	</ul>

</li>
</ul>

<h3>Division and prime numbers</h3>

<ul>
<li>
	divisors for $n\in\naturals$

$$

\set{d\in\naturals}{ d \mbox{ divides } n}

$$


</li>
<li>
	prime numbers
	<ul>
	<li>
		$p$ is primes if $1$ and $p$ are only divisors

	</li>
	</ul>

</li>
</ul>

<h3>Fundamental theorem of arithmetic</h3>

<div class="theorem" id="theorem:fundamental---theorem---of---arithmetic" data-name="fundamental theorem of arithmetic">
	


integer $n\geq2$ can be factored uniquely into products of primes,
<i>i.e.</i>,
exist distinct primes, $p_1$, &hellip;, $p_k$, and $e_1,\ldots, e_k\in\naturals$
such that

$$

n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}

$$


</div>
<ul>
<li>
	hence,
integers are <i>factorial ring</i>
(<a href="#definition:factorial---ring"></a>)

</li>
</ul>


<h3>Elementary quantities</h3>

<ul>
<li>
	greatest common divisor (gcd) (of $a$ and $b$)



$$

\gcd(a,b) = \max \set{d}{d\mbox{ divides both }a \mbox{ and } b}

$$

	<ul>
	<li>
		for definition of gcd
for general entire rings,
refer to <a href="#definition:greatest---common---divisor"></a>

	</li>
	</ul>

</li>
<li>
	least common multiple (lcm) (of $a$ and $b$)



$$

\mbox{lcm}(a,b) = \min \set{m}{\mbox{both } a \mbox{ and } b \mbox{ divides }m}

$$


</li>
<li>
	$a$ and $b$ coprime, relatively prime, mutually prime $\Leftrightarrow$ $\gcd(a,b)=1$

</li>
</ul>


<h3>Are there infinite number of prime numbers?</h3>

<ul>
<li>
	yes!

</li>
<li>
	proof
	<ul>
	<li>
		assume there only exist finite number of prime numbers, <i>e.g.</i>, $p_1 < p_2 < \cdots <p_n$

	</li>
	<li>
		but then, $p_1 \cdot p_2 \cdots p_n + 1$ is prime,
but which is greater than $p_n$, hence contradiction

	</li>
	</ul>

</li>
</ul>


<h3>Integers modulo $n$</h3>

<div class="definition" id="definition:modulo" data-name="modulo">
	
when $n$ divides $a-b$,
$a$, said to be <span class="define">equivalent to</span> $b$ <span class="define">modulo $n$</span>,
denoted by

$$

a \equiv b \Mod{n}

$$

read as &ldquo;<span class="define">$a$ congruent to $b$ mod $n$</span>''

</div>
<ul>
<li>
	$a\equiv b\Mod{n}$ and $c\equiv d\Mod{n}$ imply
	<ul>
	<li>
		$a+c\equiv b+d \Mod{n}$

	</li>
	<li>
		$ac\equiv bd \Mod{n}$

	</li>
	</ul>

</li>
</ul>
<div class="definition" id="definition:congruence---class" data-name="congruence class">
	






classes determined by modulo relation,
called <span class="define">congruence</span> or <span class="define">residue class under modulo</span>

</div>
<div class="definition" id="definition:integers---modulo---n" data-name="integers modulo n">
	




set of equivalence classes under modulo,
denoted by <span class="notation">$\integers/n \integers$</span>,
called <span class="define">integers modulo $n$</span> or <span class="define">integers mod $n$</span>

</div>

<h3>Euler's theorem</h3>

<div class="definition" id="definition:Euler's---totient---function" data-name="Euler's totient function">
	




for $n\in\naturals$,

$$

\varphi(n)
= (p_1-1)p_1^{e_1-1} \cdots (p_k-1)p_k^{e_k-1}
= n \prod_{\mathrm{prime}\ p\ \mathrm{dividing}\ n} (1-1/p)

$$

called <span class="define">Euler's totient function</span>,
also called <span class="define">Euler $\varphi$-function</span>



</div>
<ul>
<li>
	<i>e.g.</i>, $\varphi(12) = \varphi(2^2\cdot 3^1) = 1\cdot2^1\cdot 2\cdot3^0 = 4$,
$\varphi(10) = \varphi(2^1\cdot5^1) = 1\cdot2^0\cdot 4\cdot 5^0 =4$

</li>
</ul>
<div class="theorem" id="theorem:Euler's---theorem-------number---theory" data-name="Euler's theorem - number theory">
	


for coprime $n$ and $a$

$$

a^{\varphi(n)} \equiv 1 \Mod{n}

$$


</div>
<ul>
<li>
	<i>e.g.</i>, $5^4 \equiv 1 \Mod{12}$ whereas $4^4 \equiv 4 \neq 1 \Mod{12}$

</li>
</ul>
<ul>
<li>
	<span class="eemph">Euler's theorem underlies RSA cryptosystem, which is pervasively used in internet communication</span>

</li>
</ul>

