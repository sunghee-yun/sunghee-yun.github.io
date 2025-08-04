---
title: All Math Topics in All the Multiverses
date: Fri Aug  2 00:00:00 PDT 2025
last_modified_at: Sun Aug  3 23:56:28 PDT 2025
permalink: /math/rig/everything
categories:
- blog
tags:
- math
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


<h1 id="super-title-page:Stories">Math Stories</h1>


<h3>Some fundamental theorems in math!</h3>


<h3>Dualities</h3>

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
\frac{a+b+c+d}{4}
\geq
\frac{2\sqrt{ab} + 2\sqrt{cd}}{4}
=
\frac{\sqrt{ab} + \sqrt{cd}}{2}
\geq
\sqrt{\sqrt{ab} \sqrt{cd}}
=
\sqrt[4]{abcd}
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
&&
\frac{a+b+c}{3} = \frac{a + b + c + (a+b+c)/3}{4}
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
&&
\frac{a_1+\cdots+a_n}{n} = \frac{a_1 + \cdots + a_n + (2^m-n) (a_1+\cdots+a_n) /n}{2^m}
\\
&&
\geq
\sqrt[2^m]{a_1\cdots a_n \cdot ((a_1 + \cdots + a_n)/n)^{2^m-n}}
\\
&\Leftrightarrow&
\left(\frac{a_1+\cdots+a_n}{n}\right)^{2^m}
\geq
{a_1\cdots a_n \cdot \left(\frac{a_1 + \cdots + a_n}{n}\right)^{2^m-n}}
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
\alpha_1 a_1 + \cdots + \alpha_n a_n
= \frac{q_1 a_1 + \cdots + q_n a_n}{N}
\geq \sqrt[N]{a_1^{q_1}\cdots a_n^{q_n}}
= a_1^{\alpha_1}\cdots a_n^{\alpha_n}
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
= -\sum \log\left( a_i^{\alpha_i}\right)
=
\sum \alpha_i (-\log(a_i)) \geq -\log \left(\sum \alpha_i a_i\right)
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
\Leftrightarrow
(A+B)^2 \geq A^2 + B^2 + 2 \sum a_i b_i
\\
&\Leftrightarrow&
AB \geq \sum a_i b_i
\Leftrightarrow
A^2B^2 \geq \left(\sum a_i b_i\right)^2
\Leftrightarrow
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
\Leftrightarrow
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

<h1 id="super-title-page:Abstract---Algebra">Abstract Algebra</h1>
















<h2 id="title-page:Why---Abstract---Algebra?">Why Abstract Algebra?</h2>


<h3>Why abstract algebra?</h3>



<ul>
<li>
	it's fun!

</li>
<li>
	can understand <i>instrict structures</i> of algebraic objects

</li>
<li>
	allow us to solve <i>extremely practical problems</i>
(depending on your definition of practicality)
	<ul>
	<li>
		<i>e.g.</i>, can prove why root formulas for polynomials of order $n\geq 5$ do not exist

	</li>
	</ul>

</li>
<li>
	prepare us for pursuing further math topics such as
	<ul>
	<li>
		differential geometry

	</li>
	<li>
		algebraic geometry

	</li>
	<li>
		analysis

	</li>
	<li>
		representation theory

	</li>
	<li>
		algebraic number theory

	</li>
	</ul>

</li>
</ul>


<h3>Some history</h3>


<ul>
<li>
	by the way, historically, often the case that application of an idea presented
before extracting and presenting the idea on its own right

</li>
<li>
	<i>e.g.</i>,
Galois used &ldquo;quotient group'' only implicitly in his 1830's investigation,
and it had to wait until 1889 to be explicitly presented as &ldquo;abstract quotient group''
by Ho&#776;lder

</li>
</ul>


<h2 id="title-page:Groups">Groups</h2>


<h3>Monoids</h3>

<div class="definition" id="definition:law---of---composition" data-name="law of composition">
	
mapping $S\times S \to S$ for set $S$,
called <span class="define">law of composition (of $S$ to itself)</span>


	<ul>
	<li>
		
when $(\forall x, y, z \in S)((xy)z = x(yz))$,
composition is said to be <span class="define">associative</span>



	</li>
	<li>
		
$e\in S$ such that $(\forall x\in S)(ex = xe = x)$,
called <span class="define">unit element</span> - always unique



	</li>
	</ul>

</div>
<div class="proof">
	
for any two unit elements $e$ and $f$,
$e = ef = f,$
hence, $e=f$

</div>

<div class="definition" id="definition:monoids" data-name="monoids">
	


set $M$ with composition which is associative and having unit element,
called <span class="define">monoid</span>
(so in particular, $M$ is not empty)
	<ul>
	<li>
		
monoid $M$ with
$\left(
\forall x, y \in M
\right)
\left(
xy = yx
\right)$,
called <span class="define">commutative or abelian</span> monoid






	</li>
	<li>
		
subset $H\subset M$ which has <i>the</i> unit element $e$ and is itself monoid,
called <span class="define">submonoid</span>



	</li>
	</ul>

</div>

<h3>Groups</h3>

<div class="definition" id="definition:group" data-name="group">
	
monoid $G$ with

$$
\left(
\forall x \in G
\right)
\left(
\exists y \in G
\right)
\left(
xy = yx = e
\right)
$$

called <span class="define">group</span>
	<ul>
	<li>
		
for $x\in G$, $y\in G$ with $xy=yx=e$,
called <span class="define">inverse of $x$</span>


	</li>
	<li>
		
group derived from commutative monoid,
called <span class="define">abelian group</span> or <span class="define">commutative group</span>






	</li>
	<li>
		
group $G$ with $|G|<\infty$,
called <span class="define">finite group</span>



	</li>
	<li>
		
(similarly as submonoid)
$H\subset G$ that has unit element and is itself group,
called <span class="define">subgroup</span>



	</li>
	<li>
		
subgroup consisting only of unit element, called <span class="define">trivial</span>



	</li>
	</ul>

</div>

<h3>Cyclic groups, generators, and direct products</h3>

<div class="definition" id="definition:cyclic---groups" data-name="cyclic groups">
	

group $G$ with

$$
\left(
\exists a\in G
\right)
\left(
\forall x \in G
\right)
\left(
\exists n\in \naturals
\right)
\left(
x = a^n
\right)
$$

called <span class="define">cyclic group</span>
,
such $a\in G$ called <span class="define">cyclic generator</span>



</div>
<div class="definition" id="definition:generators" data-name="generators">
	
for group $G$, $S\subset G$
with

$$
\left(
\forall x \in G
\right)
\left(
x \mbox{ is arbitrary product of elements or inverse elements of } S
\right)
$$

called <span class="define">set of generators for $G$</span>,
said to <span class="define">generate $G$</span>,
denoted by <span class="notation">$G=\generates{S}$</span>



</div>
<div class="definition" id="definition:direct---products" data-name="direct products">
	
for two groups $G_1$ and $G_2$,
group $G_1\times G_2$
with

$$
\left(
\forall (x_1,x_2), (y_1,y_2) \in G_1 \times G_2
\right)
\left(
(x_1,x_2)(y_1,y_2)
= (x_1y_1, x_2,y_2) \in G_1 \times G_2
\right)
$$

whose unit element defined by $(e_1,e_2)$
where $e_1$ and $e_2$ are unit elements of $G_1$ and $G_2$ respectively,
called <span class="define">direct product of $G_1$ and $G_2$</span>



</div>

<h3>Homeomorphism and isomorphism</h3>

<div class="definition" id="definition:homeomorphism" data-name="homeomorphism">
	
for monoids $M$ and $M'$,
mapping $f:M\to M'$ with $f(e)=e'$

$$
\left(
x,y \in M
\right)
\left(
f(xy) = f(x)f(y)
\right)
$$

where $e$ and $e'$ are unit elements of $M$ and $M'$ respectively,
called <span class="define">monoid-homeomorphism</span> or simple <span class="define">homeomorphism</span>




	<ul>
	<li>
		<span class="define">group homeomorphism</span> $f:G\to G'$ is similarly monoid-homeomorphism



	</li>
	<li>
		homeomorphism $f:G\to G'$ where exists $g:G\to G'$ such that $f\circ g:G'\to G'$ and $g\circ f:G\to G$
are identity mappings,
called <span class="define">isomorphism</span>,




sometimes denoted by <span class="notation">$G\isomorph G'$</span>

	</li>
	<li>
		homeomorphism of $G$ into itself, called <span class="define">endomorphism</span>





	</li>
	<li>
		isomorphism of $G$ onto itself, called <span class="define">automorphism</span>





	</li>
	</ul>

</div>
<ul>
<li>
	set of all automorphisms of $G$ is itself group,
denoted by <span class="notation">\aut{G}</span>

</li>
</ul>

<h3>Kernel, image, and embedding of homeomorphism</h3>

<div class="definition" id="definition:kernel---of---homeomorphism" data-name="kernel of homeomorphism">
	


for group-homeomorphism $f:G\to G'$ where $e'$ is unit element of $G'$,
$f^{-1}(\{e'\})$, which is subgroup of $G$,
called <span class="define">kernel of $f$</span>,
denoted by <span class="notation">$\Ker{f}$</span>

</div>
<div class="definition" id="definition:embedding---of---homeomorphism" data-name="embedding of homeomorphism">
	


homeomorphism $f:G\to G'$ establishing isomorphism between $G$ and $f(G)\subset G'$,
called <span class="define">embedding</span>

</div>
<div class="proposition" id="proposition:group---homeomorphism---and---isomorphism" data-name="group homeomorphism and isomorphism">
	 
	<ul>
	<li>
		for group-homeomorphism $f:G\to G'$, $f(G)\subset G'$ is subgroup of $G'$

	</li>
	<li>
		homeomorphism whose kernel is trivial is injective,



often denoted by special arrow

$$
f:G \injhomeo G'
$$


	</li>
	<li>
		surjective homeomorphism whose kernel is trivial is <i>isomorphism</i>

	</li>
	<li>
		for group $G$, its generators $S$, and another group $G'$,
map $f:S\to G'$ has at most one extension to homeomorphism of $G$ into $G'$

	</li>
	</ul>

</div>

<h3>Orthogonal subgroups</h3>

<div class="proposition" id="proposition:orthogonal---subgroups" data-name="orthogonal subgroups">
	


for group $G$ and two subgroups $H$ and $K\subset G$
with $HK = G$, $H\cap K = \{e\}$, and $\left( x\in H, y\in K \right) \left( xy=yx \right)$,

$$
f: H\times K \to G
$$

with $(x,y)\mapsto xy$
is <i>isomorphism</i>
can generalize to finite number of subgroups, $H_1$, &hellip;, $H_n$ such that

$$
H_1 \cdots H_n = G
$$

and

$$
H_{k+1} \cap (H_1\cdots H_k) = \{e\}
$$

in which case, $G$ is isomorphic to $H_1\cdots H_n$

</div>

<h3>Cosets of groups</h3>

<div class="definition" id="definition:cosets---of---groups" data-name="cosets of groups">
	


for group $G$ and subgroup $H\subset G$,
$aH$ for some $a\in G$,
called <span class="define">left coset of $H$ in $G$</span>,


and element in $aH$, called
<span class="define">coset representation of $aH$</span>


- can define <span class="define">right cosets</span> similarly



</div>
<div class="proposition" id="proposition:cosets---of---groups" data-name="cosets of groups">
	
for group $G$ and subgroup $H\subset G$,
	<ul>
	<li>
		for $a\in G$,
$x\mapsto ax$ induces bijection of $H$ onto $aH$,
hence all left cosets have same cardinality

	</li>
	<li>
		$aH \cap bH \neq \emptyset$ for $a,b\in G$ implies $aH=bH$

	</li>
	<li>
		hence, $G$ is disjoint union of left cosets of $H$

	</li>
	<li>
		same statements can be made for right cosets

	</li>
	</ul>

</div>
<div class="definition" id="definition:index---and---order---of---group" data-name="index and order of group">
	




number of left cosets of $H$ in $G$,
called <span class="define">index of $H$ in $G$</span>,
denoted by <span class="notation">$(G:H)$</span>
- index of trivial subgroups,
called <span class="define">order of $G$</span>,
denoted by <span class="notation">$(G:1)$</span>

</div>

<h3>Indices and orders of groups</h3>

<div class="proposition" id="proposition:indices---and---orders" data-name="indices and orders">
	
for group $G$ and two subgroups $H$ and $K\subset G$ with $K\subset H$,

$$
(G:H) (H:K) = (G:K)
$$

when $K$ is trivial, we have

$$
(G:H) (H:1) = (G:1)
$$



</div>
hence, if $(G:1)<\infty$, both $(G:H)$ and $(H:1)$ divide $(G:1)$

<h3>Normal subgroup</h3>

<div class="definition" id="definition:normal---subgroups" data-name="normal subgroups">
	


subgroup $H\subset G$ of group $G$ with

$$
\left(
\forall x \in G
\right)
\left(
x H = H x
\right)
\Leftrightarrow
\left(
\forall x \in G
\right)
\left(
xHx^{-1}= H
\right)
$$

called <span class="define">normal subgroup of $G$</span>,
in which case

	<ul>
	<li>
		set of cosets $\set{xH}{x\in G}$ with law of composition defined by
$(xH)(yH) = (xy)H,$
forms group with unit element $H$,
denoted by <span class="notation">$G/H$</span>,
called <span class="define">factor group of $G$ by $H$</span>,


read <span class="define">$G$ modulo $H$</span>
or <span class="define">$G$ mod $H$</span>

	</li>
	<li>
		$x \mapsto xH$ induces homeomorphism of $X$ onto $\set{xH}{x\in G}$,
called <span class="define">canonical map</span>

,
kernel of which is $H$

	</li>
	</ul>

</div>
<div class="proposition" id="proposition:normal---subgroups---and---factor---groups" data-name="normal subgroups and factor groups">
	
 

	<ul>
	<li>
		kernel of (every) homeomorphism of $G$ is normal subgroups of $G$

	</li>
	<li>
		for family of normal subgroups of $G$, $\seq{N_\lambda}$,
$\bigcap N_\lambda$
is also normal subgroup

	</li>
	<li>
		every subgroup of abelian group is normal

	</li>
	<li>
		factor group of abelian group is abelian

	</li>
	<li>
		factor group of cyclic group is cyclic

	</li>
	</ul>

</div>

<h3>Normalizers and centralizers</h3>

<div class="definition" id="definition:normalizers---and---centralizers" data-name="normalizers and centralizers">
	
for subset $S\subset G$ of group $G$,

$$
\set{x\in G}{xSx^{-1} = S}
$$

is subgroup, called <span class="define">normalizer of $S$,</span>


and also called <span class="define">centralizer of $a$</span> when $S=\{a\}$ is singletone;

$$
\set{x\in G}{(\forall y\in S)(xyx^{-1} = y)}
$$

called <span class="define">centralizer of $S$,</span>


and centralizer of $G$ itself, called <span class="define">center of $G$</span>



</div>
<ul>
<li>
	<i>e.g.</i>,
$A \mapsto \det A$ of multiplicative group of square matrices in $\reals^{n\times n}$
into $\reals\sim\{0\}$
is homeomorphism,
kernel of which called <span class="define">special linear group,</span>


and (of course) is normal

</li>
</ul>


<h3>Normalizers and congruence</h3>

<div class="proposition" id="proposition:normalizers---of---groups" data-name="normalizers of groups">
	
subgroup $H\subset G$ of group $G$
is normal subgroup of its normalizer $N_H$
	<ul>
	<li>
		subgroup $H\subset G$ of group $G$
is normal subgroup of its normalizer $N_H$

	</li>
	<li>
		subgroup $K\subset G$ with $H\subset K$ where $H$ is normal in $K$
is contained in $N_H$

	</li>
	<li>
		for subgroup $K\subset N_H$,
$KH$ is group
and $H$ is normal in $KH$

	</li>
	<li>
		normalizer of $H$ is largest subgroup of $G$ in which $H$ is normal

	</li>
	</ul>

</div>

<div class="definition" id="definition:congruence---with---respect---to---normal---subgroup" data-name="congruence with respect to normal subgroup">
	


for normal subgroup $H\subset G$ of group $G$,
we write

$$
x \equiv y \Mod{H}
$$

if $xH=yH$,
read <span class="define">$x$ and $y$ are congruent modulo $H$</span>
- this notation used mostly for additive groups

</div>


<h3>Exact sequences of homeomorphisms</h3>

<div class="definition" id="definition:exact---sequences---of---homeomorphisms" data-name="exact sequences of homeomorphisms">
	


below sequence of homeomorphisms with $\Img f = \Ker g$

$$
G' \overset{f}{\longrightarrow}
G \overset{g}{\longrightarrow}
G''
$$

said to be <span class="define">exact</span>
below sequence of homeomorphisms
with $\Img f_i = \Ker f_{i+1}$

$$
G_1 \overset{f_1}{\longrightarrow}
G_2 \overset{f_2}{\longrightarrow}
G_3 \longrightarrow
\cdots
\overset{f_{n-1}}{\longrightarrow}
G_n
$$

said to be <span class="define">exact</span>

</div>
<ul>
<li>
	for normal subgroup $H\subset G$ of group $G$,
sequence
$H \overset{j}{\to}
G \overset{\varphi}{\to}
G/H$
is exact
where $j$ is inclusion and $\varphi$

</li>
<li>
	$0 \overset{}{\to}
G' \overset{f}{\to}
G \overset{g}{\to}
G'' \overset{}{\to}
0$
is exact
if and only if
$f$ injective, $g$ surjective, and $\Img f = \Ker g$

</li>
<li>
	if $H=\Ker g$ above,
$0 \overset{}{\to}
H \overset{}{\to}
G \overset{}{\to}
G/H \overset{}{\to}
0$

</li>
<li>
	more precisely, exists commutative diagram as in the figure,
in which vertical mappings are isomorphisms and rows are <i>exact</i>




<div id="fig:commutative---diagram---for---canonical---map"></div>



</li>
</ul>

<h3>Canonical homeomorphism examples</h3>

all homeomorphisms described below called <span class="define">canonical</span>
<ul>
<li>
	for two groups $G$ &amp; $G'$ and homeomorphism $f:G\to G'$ whose kernel is $H$,
exists unique homeomorphism $f_*: G/H \to G'$ with 
$$
f=f_*\circ \varphi
$$

where $\varphi:G\to G/H$ is canonical map,
and $f_*$ is injective
	<ul>
	<li>
		$f_*$ can be defined by $xH\mapsto f(x)$

	</li>
	<li>
		<span class="define">$f_*$ said to be induced by $f$</span>

	</li>
	<li>
		$f_*$ induces isomorphism $\lambda: G/H \to \Img f$

	</li>
	<li>
		below sequence summarizes above statements

$$
G \overset{\varphi}{\to}
G/H \overset{\lambda}{\to}
\Img f \overset{j}{\to}
G
$$

where $j$ is inclusion

	</li>
	</ul>

</li>
<li>
	for group $G$,
subgroup $H\subset G$,
and
homeomorphism $f:G\to G'$ whose kernel contains $H$,
intersection of all normal subgroups containing $H$, $N$,
which is the smallest normal subgroup containing $H$,
is contained in $\Ker f$,
<i>i.e.</i>,
$N\subset \Ker f$,
and exists unique homeomorphism, $f_*:G/N\to G'$
such that 
$$
f = f_* \circ \varphi
$$

where $\varphi:G\to G/H$ is canonical map
	<ul>
	<li>
		$f_*$ can be defined by $xN\mapsto f(x)$

	</li>
	<li>
		<span class="define">$f_*$ said to be induced by $f$</span>

	</li>
	</ul>

</li>
<li>
	for subgroups of $G$, $H$ and $K$ with $K\subset H$,
$xK \mapsto xH$ induces homeomorphism of $G/K$ into $G/H$,
whose kernel is $\set{xK}{x\in H}$,
thus <span class="eemph">canonical isomorphism</span>



$$
(G/K)/(H/K) \isomorph (G/K)
$$

this can be shown in the figure
where rows are exact




<div id="fig:commutative---diagram---for---canonical---isomorphism"></div>



</li>
<li>
	for subgroup $H\subset G$ and $K\subset G$ with $H$ contained in normalizer of $K$,
$H\cap K$ is normal subgroup of $H$,
$HK=KH$ is subgroup of $G$,
exists surjective homeomorphism

$$
H \to HK / K
$$

with $x \mapsto xK$,
whose kernel is $H\cap K$,
hence <span class="eemph">canonical isomorphism</span>



$$
H/(H\cap K) \isomorph HK/K
$$


</li>
<li>
	for group homeomorphism $f:G\to G'$, normal subgroup of $G'$, $H'$,

$$
H=f^{-1}(H')\subset G
$$

as shown in the figure,




<div id="fig:commutative---diagram---1"></div>


$H$ is normal in $G$
and kernel of homeomorphism

$$
G \overset{f}{\to} G'\overset{\varphi}{\to} G'/H'
$$

is $H$ where $\varphi$ is canonical map,
hence we have injective homeomorphism

$$
\bar{f}:G/H \to G'/H'
$$

again called <span class="eemph">canonical homeomorphism</span>,
giving commutative diagram
in the figure;
if $f$ is surjective, $\bar{f}$ is isomorphism




<div id="fig:commutative---diagram---for---canonical---homeomorphism"></div>



</li>
</ul>

<h3>Towers</h3>

<div class="definition" id="definition:towers---of---groups" data-name="towers of groups">
	


for group $G$,
sequence of subgroups

$$
G = G_0
\supset G_1
\supset G_2
\supset \cdots
\supset G_m
$$

called <span class="define">tower of subgroups</span>
	<ul>
	<li>
		said to be <span class="define">normal</span> if every $G_{i+1}$ is normal in $G_i$

	</li>
	<li>
		said to be <span class="define">abelian</span> if normal and every factor group $G_i/G_{i+1}$ is abelian

	</li>
	<li>
		said to be <span class="define">cyclic</span> if normal and every factor group $G_i/G_{i+1}$ is cyclic

	</li>
	</ul>










</div>
<div class="proposition" id="proposition:towers---inded---by---homeomorphism" data-name="towers inded by homeomorphism">
	

for group homeomorphism $f:G\to G'$ and normal tower

$$
G' = G'_0
\supset G'_1
\supset G'_2
\supset \cdots
\supset G'_m
$$

tower

$$
f^{-1}(G') = f^{-1}(G'_0)
\supset f^{-1}(G'_1)
\supset f^{-1}(G'_2)
\supset \cdots
\supset f^{-1}(G'_m)
$$

is
	<ul>
	<li>
		normal if $G'_i$ form normal tower

	</li>
	<li>
		abelian if $G'_i$ form abelian tower

	</li>
	<li>
		cyclic if $G'_i$ form cyclic tower

	</li>
	</ul>
because every homeomorphism

$$
G_i / G_{i+1}
\to
G'_i / G'_{i+1}
$$

is injective

</div>

<h3>Refinement of towers and solvability of groups</h3>

<div class="definition" id="definition:refinement---of---towers" data-name="refinement of towers">
	



for tower of subgroups,
tower obtained by inserting finite number of subgroups,
called <span class="define">refinement of tower</span>

</div>

<div class="definition" id="definition:solvable---groups" data-name="solvable groups">
	


group having an abelian tower whose last element is trivial subgroup,
said to be <span class="define">solvable</span>


</div>

<div class="proposition" id="proposition:finite---solvable---groups" data-name="finite solvable groups">
	 

	<ul>
	<li>
		abelian tower of finite group admits cyclic refinement

	</li>
	<li>
		finite solvable group admits cyclic tower, whose last element is trivial subgroup

	</li>
	</ul>

</div>

<div class="theorem" id="theorem:Feit-Thompson---theorem" data-name="Feit-Thompson theorem">
	


group whose order is prime power is solvable

</div>

<div class="theorem" id="theorem:solvability---condition---in---terms---of---normal---subgroups" data-name="solvability condition in terms of normal subgroups">
	
for group $G$ and its normal subgroup $H$,
$G$ is solvable if and only if
both $H$ and $G/H$ are solvable

</div>


<h3>Commutators and commutator subgroups</h3>

<div class="definition" id="definition:commutator" data-name="commutator">
	


for group $G$,
$xyx^{-1}y^{-1}$ for $x,y\in G$,
called <span class="define">commutator</span>

</div>
<div class="definition" id="definition:commutator---subgroups" data-name="commutator subgroups">
	


subgroup generated by commutators of group $G$,
called <span class="define">commutator subgroup</span>,
denoted by <span class="notation">$G^C$</span>,
<i>i.e.</i>

$$
G^C = \generates{\set{xyx^{-1}y^{-1}}{x,y\in G}}
$$


</div>
<ul>
<li>
	$G^C$ is normal in $G$

</li>
<li>
	$G/G^C$ is commutative

</li>
<li>
	$G^C$ is contained in kernel of every homeomorphism of $G$ into commutative group

</li>
<li>
	
 of above statements

</li>
</ul>
<ul>
<li>
	<span class="eemph">commutator group is at the heart of solvability and non-solvability problems!</span>

</li>
</ul>


<h3>Simple groups</h3>

<div class="definition" id="definition:simple---groups" data-name="simple groups">
	

non-trivial group having no normal subgroup other than itself and trivial subgroup,
said to be <span class="define">simple</span>

</div>

<div class="proposition" id="proposition:simple---groups" data-name="simple groups">
	
abelian group is simple
if and only if
cycle of prime order

</div>


<h3>Butterfly lemma</h3>

<div class="lemma" id="lemma:butterfly---lemma-------Zassenhaus" data-name="butterfly lemma - Zassenhaus">
	



for subgroups $U$ and $V$ of a group
and normal subgroups $u$ and $v$ of $U$ and $V$ respectively,

$$
u(U\cap v) \mbox{ is normal in } u(U\cap V)
$$


$$
(u\cap V)v \mbox{ is normal in } (U\cap V)v
$$

and factor groups are isomorphic,
<i>i.e.</i>,

$$
u(U\cap V) / u(U\cap v)
\isomorph\
(U\cap V)v / (u\cap V)v
$$

these shown in the figure

</div>
<ul>
<li>
	indeed

$$
(U\cap V)/((u\cap V)(U\cap v))
\isomorph\
u(U\cap V) / u(U\cap v)
\isomorph\
(U\cap V)v / (u\cap V)v
$$


</li>
</ul>




<div id="fig:butterfly---lemma"></div>



<h3>Equivalent towers</h3>

<div class="definition" id="definition:equivalent---towers" data-name="equivalent towers">
	




for two normal towers
of same height
starting from same group
ending with trivial subgroup

$$
G = G_1
\supset G_2
\supset G_3
\supset \cdots
\supset G_{n+1} = \{e\}
$$


$$
G = H_1
\supset H_2
\supset H_3
\supset \cdots
\supset H_{n+1} = \{e\}
$$

with

$$
G_i/G_{i+1}\isomorph H_{\pi(i)+1}/H_{\pi(i)}
$$

for some permutation $\pi\in\perm{\{1,\ldots,n\}}$,
<i>i.e.</i>,
sequences of factor groups are same
up to isomorphisms and permutation of indices,
said to be <span class="define">equivalent</span>

</div>

<h3>Schreier and Jordan-Ho&#776;lder theorems</h3>

<div class="theorem" id="theorem:Schreier---theorem" data-name="Schreier theorem">
	



two normal towers starting from same group and ending with trivial subgroup
have equivalent refinement

</div>

<div class="theorem" id="theorem:Jordan-Holder---theorem" data-name="Jordan-Holder theorem">
	




all normal towers starting from same group and ending with trivial subgroup
where each factor group is non-trivial and simple
are equivalent

</div>


<h3>Cyclic groups</h3>

<div class="definition" id="definition:exponent---of---groups---and---group---elements" data-name="exponent of groups and group elements">
	


for group $G$,
$n\in\naturals$ with $a^n=e$ for $a\in G$,
called <span class="define">exponent of $a$</span>;
$n\in\naturals$ with $x^n=e$ for every $x\in G$,
called <span class="define">exponent of $G$</span>

</div>

<div class="definition" id="definition:period---of---group---elements" data-name="period of group elements">
	


for group $G$ and $a\in G$,
smallest $n\in\naturals$ with $a^n=e$,
called <span class="define">period of $a$</span>

</div>

<div class="proposition" id="proposition:period---of---elements---of---finite---groups" data-name="period of elements of finite groups">
	
for finite group $G$ of order $n>1$,
period of every non-unit element $a$ ($\neq e$) devided $n$;
if $n$ is prime number,
$G$ is cyclic and period of every generator is $n$

</div>

<div class="proposition" id="proposition:subgroups---of---cyclic---groups" data-name="subgroups of cyclic groups">
	
every subgroup of cyclic group is cyclic
and image of every homeomorphism of cyclic group is cyclic

</div>


<h3>Properties of cyclic groups</h3>

<div class="proposition" id="proposition:properties---of---cyclic---groups" data-name="properties of cyclic groups">
	 
	<ul>
	<li>
		infinity cyclic group has exactly two generators; if $a$ is one, $a^{-1}$ is the other

	</li>
	<li>
		for cyclic group $G$ of order $n$ and generator $x$,
set of generators of $G$ is

$$
\set{x^m}{m \mbox{ is relatively prime to }n}
$$


	</li>
	<li>
		for cyclic group $G$ and two generators $a$ and $b$,
exists automorphism of $G$ mapping $a$ onto $b$;
conversely, every automorphism maps $a$ to some generator

	</li>
	<li>
		for cyclic group $G$ of order $n$ and $d\in\naturals$ dividing $n$,
exists unique subgroup of order $d$

	</li>
	<li>
		for cyclic groups $G_1$ and $G_2$ of orders $n$ and $m$ respectively
with $n$ and $m$ relatively prime,
$G_1\times G_2$ is cyclic group

	</li>
	<li>
		for non-cyclic finite abelian group $G$,
exists subgroup isomorphic to $C\times C$
with $C$ cyclic with prime order

	</li>
	</ul>

</div>

<h3>Symmetric groups and permutations</h3>

<div class="definition" id="definition:symmetric---groups---and---permutations" data-name="symmetric groups and permutations">
	




for nonempty set $S$, group $G$ of bijective functions of $S$ onto itself
with law of composition being function composition,
called <span class="define">symmetric group of $S$</span>, denoted by <span class="notation">\perm{S}</span>;
elements in $\perm{S}$ called <span class="define">permutations of $S$</span>;
element swapping two disjoint elements in $S$ leaving every others left,
called <span class="define">transposition</span>





</div>
<div class="proposition" id="proposition:sign---homeomorphism---of---finite---symmetric---groups" data-name="sign homeomorphism of finite symmetric groups">
	
for finite symmetric group $S_n$,
exits unique homeomorphism $\epsilon: S_n \to\{-1,1\}$
mapping every transposition, $\tau$, to $-1$,
<i>i.e.</i>, $\epsilon(\tau)=-1$

</div>


<div class="definition" id="definition:alternating---groups" data-name="alternating groups">
	
element of finite symmetric group $\sigma$ with $\epsilon(\sigma)=1$,
called <span class="define">even</span>,
element $\sigma$ with $\epsilon(\sigma)=-1$,
called <span class="define">odd</span>;




kernel of $\epsilon$, called <span class="define">alternating group</span>, denoted by <span class="notation">$A_n$</span>



</div>
<div class="theorem" id="theorem:solvability---of---finite---symmetric---groups" data-name="solvability of finite symmetric groups">
	
symmetric group $S_n$ with $n\geq 5$
is <i>not</i> solvable

</div>
<div class="theorem" id="theorem:simplicity---of---alternating---groups" data-name="simplicity of alternating groups">
	
alternating group $A_n$ with $n\geq 5$ is simple

</div>

<h3>Operations of group on set</h3>

<div class="definition" id="definition:operations---of---group---on---set" data-name="operations of group on set">
	


for group $G$ and set $S$,
homeomorphism

$$
\pi:G \to \perm{S}
$$

called <span class="define">operation of $G$ on $S$</span> or <span class="define">action of $G$ on $S$</span>



	<ul>
	<li>
		$S$, called <span class="define">$G$-set</span>



	</li>
	<li>
		denote $\pi(x)$ for $x\in G$
by <span class="define">$\pi_x$</span>,
hence homeomorphism denoted by <span class="notation">$x\mapsto \pi_x$</span>

	</li>
	</ul>

</div>
<ul>
<li>
	obtain mapping from such operation, $G\times S \to S$, with $(x,s)\mapsto \pi_x(s)$

</li>
<li>
	often abbreviate $\pi_x(s)$ by $xs$, with which the following two properties satisfied
	<ul>
	<li>
		$\left( \forall x,y\in G, s\in S \right) \left( x(ys) = (xy)s \right)$

	</li>
	<li>
		$\left( \forall s\in S \right) \left( es = s \right)$

	</li>
	</ul>

</li>
<li>
	conversely, for mapping $G\times S\to S$ with $(x,s)\mapsto xs$ satisfying above two properties,
$s\mapsto xs$ is permutation for $x\in G$,
hence $\pi_x$ is homeomorphism of $G$ into $\perm{S}$

</li>
<li>
	thus, operation of $G$ on $S$ can be defined as mapping $S\times G\to S$ satisfying above two properties

</li>
</ul>

<h3>Conjugation</h3>

<div class="definition" id="definition:conjugation---of---groups" data-name="conjugation of groups">
	


for group $G$ and map $\gamma_x:G\to G$ with $\gamma_x(y) = xyx^{-1}$,
homeomorphism

$$
G \to \aut{G} \mbox{ defined by } x\mapsto \gamma_x
$$

called <span class="define">conjugation</span>,
which is operation of $G$ on itself

</div>
<ul>
<li>
	$\gamma_x$, called <span class="define">inner</span>



</li>
<li>
	kernel of conjugation is <i>center of $G$</i>

</li>
<li>
	to avoid confusion, instead of writing $xy$ for $\gamma_x(y)$, write

$$
\gamma_x(y) = xyx^{-1} = \prescript{x}{}{y}
\mbox{ and }
\gamma_{x^{-1}}(y) = x^{-1}yx = {y}^x
$$


</li>
<li>
	for subset $A\subset G$,
map $(x,A) \mapsto xAx^{-1}$
is operation of $G$ on set of subsets of $G$

</li>
<li>
	similarly for subgroups of $G$

</li>
<li>
	two subsets of $G$, $A$ and $B$ with $B= x A x^{-1}$ for some $x\in G$,
said to be <span class="define">conjugate</span>



</li>
</ul>

<h3>Translation</h3>

<div class="definition" id="definition:translation" data-name="translation">
	


operation of $G$ on itself defined by map

$$
(x,y) \mapsto xy
$$

called <span class="define">translation</span>,
denoted by <span class="notation">$T_x:G \to G$</span>
with $T_x(y) = xy$

</div>
<ul>
<li>
	for subgroup $H\subset G$,
$T_x(H) = xH$ is left coset
	<ul>
	<li>
		denote set of left cosets also by $G/H$ even if $H$ is not normal

	</li>
	<li>
		denote set of right cosets also by $H\backslash G$

	</li>
	</ul>

</li>
<li>
	examples of translation
	<ul>
	<li>
		$G=GL(V)$, group of linear automorphism of vector space with field $F$,
for which, map $(A,v)\mapsto Av$ for $A\in G$ and $v\in V$
defines operation of $G$ on $V$
		<ul>
		<li>
			$G$ is subgroup of group of permutations, $\perm{V}$

		</li>
		</ul>

	</li>
	<li>
		for $V=F^n$, $G$ is group of nonsingular $n$-by-$n$ matrices

	</li>
	</ul>

</li>
</ul>


<h3>Isotropy</h3>

<div class="definition" id="definition:isotropy" data-name="isotropy">
	


for operation of group $G$ on set $S$

$$
\set{x\in G}{xs = s}
$$

called <span class="define">isotropy of $G$</span>,
denoted by <span class="notation">$G_s$</span>,
which is subgroup of $G$

</div>
<ul>
<li>
	for conjugation operation of group $G$,
$G_s$ is normalizer of $s\in G$

</li>
<li>
	isotropy groups are conjugate,
<i>e.g.</i>, for $s,s'\in S$ and $y\in G$ with $ys=s'$,

$$
G_{s'} = yG_s y^{-1}
$$


</li>
<li>
	by definition, kernel of operation of $G$ on $S$ is

$$
K = \bigcap_{s\in S} G_s \subset G
$$


</li>
<li>
	operation with trivial kernel, said to be <span class="define">faithful</span>



</li>
<li>
	$s\in G$ with $G_s = G$, called <span class="define">fixed point</span>




</li>
</ul>

<h3>Orbits of operation</h3>

<div class="definition" id="definition:orbits---of---operation" data-name="orbits of operation">
	



for operation of group $G$ on set $S$,
$\set{xs}{x\in G}$,
called <span class="define">orbit of $s$ under $G$</span>,
denoted by <span class="notation">$Gs$</span>

</div>
<ul>
<li>
	for $x,y\in G$ in same coset of $G_s$, $xs = ys$, <i>i.e.</i>
$\left(
\exists z\in G
\right)
\left(
x,y \in zG_s
\right)
\Leftrightarrow
xs = ys$

</li>
<li>
	hence, mapping $G/G_s \to S$ with $x \mapsto x G_s$
is morphism of $G$-sets, thus

</li>
</ul>
<div class="proposition" id="proposition:">
	
for group $G$, operating on set $S$ and $s\in S$,
order of orbit $Gs$ is equal to index $(G:G_s)$

</div>

<div class="proposition" id="proposition:">
	
for subgroup $H$ of group $G$,
number of conjugate subgroups to $H$
is index of normalizer of $H$ in $G$

</div>

<div class="definition" id="definition:transitive---operation" data-name="transitive operation">
	



operation with one orbit, said to be <span class="define">transitive</span>

</div>


<h3>Orbit decomposition and class formula</h3>

<ul>
<li>
	orbits are disjoint

$$
S = \coprod_{\lambda \in \Lambda} Gs_\lambda
$$

where $s_\lambda$ are elements of distinct orbits

</li>
</ul>
<div class="formula" id="formula:orbit---decomposition---formula" data-name="orbit decomposition formula">
	


for group $G$ operating on set $S$,
index set $\Lambda$ whose elements represent distinct orbits

$$
|S| = \sum_{\lambda \in \Lambda} (G:G_\lambda)
$$


</div>
<div class="formula" id="formula:class---formula" data-name="class formula">
	


for group $G$ and set $C\subset G$ whose elements represent distinct conjugacy classes

$$
(G:1) = \sum_{x\in C} (G:G_x)
$$


</div>

<h3>Sylow subgroups</h3>

<div class="definition" id="definition:sylow---subgroups" data-name="sylow subgroups">
	


for prime number $p$,
finite group with order $p^n$ for some $n\geq0$, called <span class="define">$p$-group</span>;
subgroup $H\subset G$ of finite group $G$ with order $p^n$ for some $n\geq0$, called <span class="define">$p$-subgroup</span>;
subgroup of order $p^n$ where $p^n$ is highest power of $p$ dividing order of $G$,
called <span class="define">$p$-Sylow subgroup</span>





</div>
<div class="lemma" id="lemma:">
	
finite abelian group of order divided by prime number $p$
has subgroup of order $p$

</div>
<div class="theorem" id="theorem:$p$-Sylow---subgroups---of---finite---groups" data-name="$p$-Sylow subgroups of finite groups">
	
finite group of order divided by prime number $p$
has $p$-Sylow subgroup

</div>
<div class="lemma" id="lemma:number---of---fixed---points---of---group---operations" data-name="number of fixed points of group operations">
	
for $p$-group $H$, operating on finite set $S$

	<ul>
	<li>
		number of fixed points of $H$ is congruent to size of $S$ modulo $p$,
<i>i.e.</i>

$$
\mbox{\# fixed points of }H \equiv |S| \Mod{p}
$$


	</li>
	<li>
		if $H$ has exaxctly one fixed point,
$|S| \equiv 1\Mod{p}$

	</li>
	<li>
		if $p$ divides $|S|$,
$|S| \equiv 0\Mod{p}$

	</li>
	</ul>

</div>

<h3>Sylow subgroups and solvability</h3>

<div class="theorem" id="theorem:solvability---of---finite---$p$-groups" data-name="solvability of finite $p$-groups">
	
finite $p$-group is solvable;
if it is non-trivial,
it has non-trivial center

</div>
<div class="corollary" id="corollary:">
	
for non-trivial $p$-group,
exists sequence of subgroups

$$
\{e\} = G_0
\subset G_1
\subset G_2
\subset \cdots
\subset G_n
=G
$$

where $G_i$ is normal in $G$
and $G_{i+1}/G_i$ is cyclic group of order $p$

</div>
<div class="lemma" id="lemma:normality---of---subgroups---of---order---$p$" data-name="normality of subgroups of order $p$">
	
for finite group $G$ and smallest prime number dividing order of $G$ $p$,
every subgroup of index $p$ is normal

</div>
<div class="proposition" id="proposition:solvability---of---groups---of---order---$pq$" data-name="solvability of groups of order $pq$">
	
group of order $pq$ with $p$ and $q$ being distinct prime numbers,
is solvable

</div>
<ul>
<li>
	now can prove following
	<ul>
	<li>
		group of order, $35$, is solvable
- implied by <a href="#proposition:finite---solvable---groups"></a>
and <a href="#proposition:properties---of---cyclic---groups"></a>

	</li>
	<li>
		group of order less than $60$ is solvable

	</li>
	</ul>

</li>
</ul>

<h2 id="title-page:Rings">Rings</h2>


<h3>Rings</h3>

<div class="definition" id="definition:ring" data-name="ring">
	
set $A$ together with two laws of composition called multiplication and addition
which are written as product and sum respectively, satisfying following conditions,
called <span class="define">ring</span>





	<ul>
	<li>
		$A$ is commutative group with respect to addition
- unit element denoted by <span class="notation">$0$</span>

	</li>
	<li>
		$A$ is monoid with respect to multiplication
- unit element denoted by <span class="notation">$1$</span>

	</li>
	<li>
		multiplication is distributive
over addition,
<i>i.e.</i>

$$
\left(
\forall x, y, z \in A
\right)
\left(
(x+y)z = xz + yz
\mbox{ \& }
z(x+y) = zx + zy
\right)
$$


	</li>
	<li>
		
do not assume $1\neq 0$

	</li>
	</ul>

</div>

<ul>
<li>
	can prove, <i>e.g.</i>,
	<ul>
	<li>
		$\left( \forall x \in A \right) \left( 0x = 0 \right)$
because
$0x + x = 0x + 1x = (0+1)x = 1x = x$

	</li>
	<li>
		if $1=0$, $A=\{0\}$
because
$x = 1x = 0x = 0$

	</li>
	<li>
		$\left( \forall x,y\in A \right) \left( (-x)y = -(xy) \right)$
because
$xy + (-x)y = (x+ -x)y = 0y = 0$

	</li>
	</ul>

</li>
</ul>
<div class="definition" id="definition:subring" data-name="subring">
	


subset of ring which itself is ring with same additive and multiplicative laws of composition,
called <span class="define">subring</span>

</div>

<h3>More on ring</h3>

<div class="definition" id="definition:multiplicative---group---of---invertible---elements---of---ring" data-name="multiplicative group of invertible elements of ring">
	








subset $U$ of ring $A$
such that every element of $U$ has both left and right inverses,
called <span class="define">group of units of $A$</span> or <span class="define">group of invertible elements of $A$</span>,
sometimes denoted by <span class="notation">$A^\ast$</span>

</div>
<div class="definition" id="definition:division---ring" data-name="division ring">
	

ring with $1\neq0$ and every nonzero element being invertible,
called <span class="define">division ring</span>

</div>
<div class="definition" id="definition:commutative---ring" data-name="commutative ring">
	

ring $A$ with $\left( \forall x,y \in A \right) \left( xy= yx \right)$,
called <span class="define">commutative ring</span>

</div>

<div class="definition" id="definition:center---of---ring" data-name="center of ring">
	


subset $C\subset A$ of ring $A$ such that

$$
C= \set{a\in A}{\forall x \in A, xa = ax}
$$

is <i>subring</i>,
and
is called <span class="define">center of ring $A$</span>

</div>

<h3>Fields</h3>

<div class="definition" id="definition:field" data-name="field">
	
commutative division ring, called <span class="define">field</span>

</div>

<h3>General distributivity</h3>

<ul>
<li>
	general distributivity
- for ring $A$, $\seq{x_i}_{i=1}^n\subset A$ and $\seq{y_i}_{i=1}^n\subset A$

$$
\left(
\sum x_i
\right)
\left(
\sum y_j
\right)
=
\sum_i \sum_j x_iy_j
$$


</li>
</ul>

<h3>Ring examples</h3>

<ul>
<li>
	for set $S$ and ring $A$,
<span class="emph">set of all mappings of $S$ into $A$ $\Map(S,A)$</span>
whose addition and multiplication are defined as below,
is <i>ring</i>


$$
\begin{eqnarray*}
&
\left(
\forall f,g\in \Map(S,A)
\right)
\left(
\forall x\in S
\right)
\left(
(f+g)(x) = f(x)+g(x)
\right)
&
\\
&
\left(
\forall f,g\in \Map(S,A)
\right)
\left(
\forall x\in S
\right)
\left(
(fg)(x) = f(x)g(x)
\right)
&
\end{eqnarray*}
$$

	<ul>
	<li>
		additive and multiplicative unit elements of $\Map(S,A)$
are constant maps whose values are
additive and multiplicative unit elements of $A$
respectively

	</li>
	</ul>
	<ul>
	<li>
		$\Map(S,A)$ is commutative if and only if $A$ is commutative

	</li>
	<li>
		for set $S$, $\Map(S,\reals)$
(page~<a href="#page:Notations">here</a>)
is a commutative ring

	</li>
	</ul>

</li>
<li>
	for abelian group $M$,
<span class="emph">set $\End(M)$ of group homeomorphisms of $M$ into itself</span>
is <i>ring</i> with normal addition and mapping composition as multiplication

	<ul>
	<li>
		additive and multiplicative unit elements of $\End(M)$
are constant map whose value is the unit element of $M$
and identity mapping
respectively

	</li>
	</ul>
	<ul>
	<li>
		not commutative in general

	</li>
	</ul>

</li>
<li>
	for ring $A$,
<span class="emph">set $A[X]$ of polynomials over $A$</span>
is <i>ring</i>,
(<a href="#definition:polynomial"></a>)

</li>
<li>
	for field $K$,
$K^{n\times n}$,
<i>i.e.</i>,
set of $n$-by-$n$ matrices with components in $K$,
is <i>ring</i>
	<ul>
	<li>
		$\left(K^{n\times n}\right)^\ast$,
<i>i.e.</i>,
multiplicative group of units of $K^{n\times n}$,
consists
of non-singular matrices,
<i>i.e.</i>,
those whose determinants are nonzero

	</li>
	</ul>

</li>
</ul>


<h3>Group ring</h3>

<div class="definition" id="definition:group---ring" data-name="group ring">
	


for group $G$ and field $K$,
set of all formal linear combinations
$\sum_{x\in G} a_x x$
with $a_x\in K$ where $a_x$ are zero except finite number of them
where addition is defined normally
and multiplication is defined as

$$
\left(
\sum_{x\in G} a_x x
\right)
\left(
\sum_{y\in G} b_y y
\right)
=
\sum_{z\in G}
\left(
\sum_{xy=z} a_xb_y xy
\right)
$$

called <span class="define">group ring</span>,
denoted by <span class="notation">$K[G]$</span>

	<ul>
	<li>
		$\sum_{xy=z} a_xb_y$ above
defines what is called <span class="define">convolution product</span>

	</li>
	</ul>

</div>

<h3>Convolution product</h3>

<div class="definition" id="definition:convolution---product" data-name="convolution product">
	


for two functions $f,g$ on group $G$,
<span class="define">convolution (product)</span>,
denoted by <span class="notation">$f\ast g$</span>,
defined by

$$
(f\ast g)(z) =
\sum_{xy=z} f(x)f(y)
$$

as function on group $G$

	<ul>
	<li>
		one may restrict this definition to functions which are $0$ except at finite number of elements

	</li>
	</ul>

</div>
<ul>
<li>
	for $f,g\in L^1(\reals)$, can define <i>convolution product</i> $f\ast g$ by

$$
(f\ast g) (x) = \int_{\reals} f(x-y)g(y)dy
$$

	<ul>
	<li>
		satisfies all axioms of ring except that there is not unit element

	</li>
	<li>
		commutative (essentially because $\reals$ is commutative)

	</li>
	</ul>

</li>
<li>
	more generally,
for locally compact group $G$ wiht Haar measure $\mu$,
can define <i>convolution product</i>
by

$$
(f\ast g) (x) = \int_{G} f(xy^{-1})g(y)d\mu(y)
$$


</li>
</ul>

<h3>Ideals of ring</h3>

<div class="definition" id="definition:ideal" data-name="ideal">
	
subset $\ideal{a}$ of ring $A$ which is subgroup of additive group of $A$
with $A\ideal{a}\subset \ideal{a}$,
called <span class="define">left ideal</span>;



indeed, $A\ideal{a} = \ideal{a}$ because $A$ has $1$;
<span class="define">right ideal</span> can be similarly defined, <i>i.e.</i>, $\ideal{a} A = \ideal{a}$;



subset which is both left and right ideal, called <span class="define">two-sided ideal</span>
or simply <span class="define">ideal</span>






</div>
<ul>
<li>
	for ring $A$,
$(0)$ are $A$ itself area ideals

</li>
</ul>
<div class="definition" id="definition:principal---ideal" data-name="principal ideal">
	


for ring $A$ and $a\in A$, left ideal $Aa$, called <span class="define">principal left ideal</span>

	<ul>
	<li>
		$a$, said to be generator of $\ideal{a}=Aa$ (over $A$)

	</li>
	</ul>

</div>
<div class="definition" id="definition:principal---two-sided---ideal" data-name="principal two-sided ideal">
	


$AaA$, called <span class="define">principal two-sided ideal</span>
where

$$
AaA
=
\bigcup_{i=1}^\infty \bigsetl{\sum_{i=1}^n x_i a y_i}{x_i,y_i\in A}
$$


</div>
<div class="lemma" id="lemma:ideals---of---field" data-name="ideals of field">
	

only ideals of field
are the field itself and zero ideal

</div>

<h3>Principal rings</h3>

<div class="definition" id="definition:principal---ring" data-name="principal ring">
	

commutative ring of which every ideal is principal and $1\neq0$,
called <span class="define">principal ring</span>

</div>
<ul>
<li>
	$\integers$ (set of integers)
is <i>principal</i> ring

<div id="page:nonzero---ideals---of---integers---are---principal"></div>

</li>
<li>
	$k[X]$ (ring of polynomials) for field $k$
is <i>principal</i> ring

</li>
<li>
	ring of algebraic integers in number field $K$
is <i>not</i> necessarily principal
	<ul>
	<li>
		let $\ideal{p}$ be prime ideal,
let $R_\ideal{p}$
be ring of all elements $a/b$
with $a,b\in R$ and $b\not\in\ideal{p}$,
then
$R_\ideal{p}$ is principal,
with one prime ideal $\ideal{m}_\ideal{p}$
consisting of all elements $a/b$ as above
but with $a\in\ideal{p}$

	</li>
	</ul>

</li>
<li>
	let $A$
be set of entire functions on complex plane,
then $A$ is commutative ring,
and every finitely generated ideal is <i>principal</i>
	<ul>
	<li>
		given discrete set of complex numbers $\{z_i\}$
and nonnegative integers $\{m_i\}$,
exists entire function $f$
having zeros at $z_i$ of multiplicity $m_i$
and <i>no</i> other zeros

	</li>
	<li>
		every principal ideal is of form $Af$ for some such $f$

	</li>
	<li>
		group of units $A^\ast$ in $A$
consists of functions having no zeros

	</li>
	</ul>

</li>
</ul>

<h3>Ideals as both additive and multiplicative monoids</h3>

<ul>
<li>
	ideals form additive monoid
	<ul>
	<li>
		for left ideals $\ideal{a}$, $\ideal{b}$, $\ideal{c}$ of ring $A$,
$\ideal{a}+\ideal{b}$ is left ideal,
$(\ideal{a}+\ideal{b})+\ideal{c} =\ideal{a}+(\ideal{b}+\ideal{c})$,
hence form additive monoid with $(0)$ as the unit elemenet

	</li>
	<li>
		similarly
for right ideals &amp; two-sided ideals

	</li>
	</ul>

</li>
<li>
	ideals form multiplicative monoid
	<ul>
	<li>
		for left ideals $\ideal{a}$, $\ideal{b}$, $\ideal{c}$ of ring $A$,
define $\ideal{a}\ideal{b}$ as

$$
\ideal{a}\ideal{b}
=
\bigcup_{i=1}^\infty \bigsetl{\sum_{i=1}^n x_i y_i}{x_i \in \ideal{a},y_i\in \ideal{b}}
$$

then $\ideal{a}\ideal{b}$ is also left ideal,
$(\ideal{a}\ideal{b})\ideal{c} =\ideal{a}(\ideal{b}\ideal{c})$,
hence form multiplicative monoid with $A$ itself as the unit elemenet;
for this reason,
this unit element $A$, <i>i.e.</i>, the ring itself, often written as $(1)$

	</li>
	<li>
		similarly
for right ideals &amp; two-sided ideals

	</li>
	</ul>

</li>
<li>
	ideal multiplication is also distributive over addition

</li>
<li>
	however, set of ideals does <span class="emph">not</span> form ring
(because the additive monoid is <i>not</i> group)

</li>
</ul>

<h3>Generators of ideal</h3>

<div class="definition" id="definition:generators---of---ideal" data-name="generators of ideal">
	



for ring $A$ and $a_1,\ldots,a_n\subset A$, set of elements of $A$ of form

$$
\sum_{i=1}^n x_i a_i
$$

with $x_i \in A$, is left ideal,
denoted by <span class="notation">$(a_1,\ldots,a_n)$</span>,
called <span class="define">generators</span> of the left ideal;


similarly for right ideals

</div>
<ul>
<li>
	above equal to smallest ideals containing $a_i$, <i>i.e.</i>,
intersection of all ideals containing $a_i$

$$
\cap_{a_1,\ldots, a_n\in\ideal{a}} \ideal{a}
$$


-
just like set ($\sigma$-)algebras in set theory 

</li>
</ul>

<h3>Entire rings</h3>

<div class="definition" id="definition:zero---divisor" data-name="zero divisor">
	


for ring $A$,
$x,y\in A$ with $x\neq0$, $y\neq0$, and $xy=0$,
said to be <span class="define">zero divisors</span>

</div>

<div class="definition" id="definition:entire---ring" data-name="entire ring">
	


commutative ring with no zero divisors for which $1\neq0$,
said to be <span class="define">entire</span>;
entire ring, sometimes called <span class="define">integral domain</span>



</div>

<div class="lemma" id="lemma:every---field---is---entire---ring" data-name="every field is entire ring">
	
every field is entire ring

</div>


<h3>Ring-homeomorphism</h3>

<div class="definition" id="definition:ring-homeomorphism" data-name="ring-homeomorphism">
	



mapping of ring into ring $f:A\to B$
such that
$f$ is monoid-homeomorphism for both additive and multiplicative structure on $A$ and $B$,
<i>i.e.</i>,

$$
\left(
\forall
a, b \in A
\right)
\left(
f(a+b) = f(a) + f(b) \mbox{ \& } f(ab) = f(a)f(b)
\right)
$$

and

$$
f(1)=1 \mbox{ \& } f(0)=0
$$

called <span class="define">ring-homeomorphism</span>;
<span class="define">kernel</span>, defined to be kernel of $f$
viewed as additive homeomorphism




</div>
<ul>
<li>
	<i>kernel of ring-homeomorphism</i> $f:A\to B$
is ideal of $A$


</li>
<li>
	conversely, for ideal $\ideal{a}$, can construct factor ring $A/\ideal{a}$

</li>
<li>
	simply say &ldquo;homeomorphism'' if reference to ring is clear

</li>
</ul>
<div class="proposition" id="proposition:injectivity---of---field---homeomorphism" data-name="injectivity of field homeomorphism">
	



ring-homeomorphism from field into field
is injective
(due to <a href="#lemma:ideals---of---field"></a>)

</div>


<h3>Factor ring and canonical map</h3>

<div class="definition" id="definition:factor---ring---and---residue---class" data-name="factor ring and residue class">
	




for ring $A$ and an ideal $\ideal{a} \subset A$,
set of cosets $x+\ideal{a}$ for $x\in A$
combined with <i>addition</i> defined by viewing $A$ and $\ideal{a}$ as additive groups,
<i>multiplication</i> defined by
$(x+\ideal{a})
(y+\ideal{a})
=
xy+\ideal{a},$
which satisfy all requirements for ring,
called <span class="define">factor ring</span> or <span class="define">residue class ring</span>,
denoted by <span class="notation">$A/\ideal{a}$</span>;
cosets in $A/\ideal{a}$,
called <span class="define">residue classes modulo \ideal{a}</span>,
and each coset $x+\ideal{a}$
called <span class="define">residue class of $x$ modulo \ideal{a}</span>

</div>
<ul>
<li>
	for ring $A$ and ideal $\ideal{a}$
	<ul>
	<li>
		for subset $S\subset \ideal{a}$, write $S \equiv 0 \Mod{\ideal{a}}$

	</li>
	<li>
		for $x,y\in A$, if $x-y\in\ideal{a}$, write $x \equiv y \Mod{\ideal{a}}$

	</li>
	<li>
		if $\ideal{a} = (a)$ for $a\in A$,
for $x,y\in A$, if $x-y\in\ideal{a}$, write $x \equiv y \Mod{a}$

	</li>
	</ul>

</li>
</ul>
<div class="definition" id="definition:canonical---map---of---ring" data-name="canonical map of ring">
	


ring-homeomorphism of ring $A$ into factor ring $A/\ideal{a}$

$$
A \to A/\ideal{a}
$$

called <span class="define">canonical map of $A$ into $A/\ideal{a}$</span>

</div>

<h3>Factor ring induced ring-homeomorphism</h3>

<div class="proposition" id="proposition:factor---ring---induced---ring-homeomorphism" data-name="factor ring induced ring-homeomorphism">
	

for ring-homeomorphism $g:A\to A'$
whose kernel contains ideal $\ideal{a}$,
exists unique ring-homeomorphism $g_\ast:A/\ideal{a} \to A'$
making diagram in the figure
commutative,
<i>i.e.</i>,
$g^\ast \circ f = g$
where $f$ is the ring canonical map
$f:A\to A/\ideal{a}$

</div>






<div id="fig:factor-ring-induced-ring-homeomorphism"></div>

<ul>
<li>
	the
ring canonical map $f:A\to A/\ideal{a}$
is universal in category of homeomorphisms
whose kernel contains $\ideal{a}$

</li>
</ul>


<h3>Prime ideal and maximal ideal</h3>

<div class="definition" id="definition:prime---ideal" data-name="prime ideal">
	



for commutative ring $A$,
ideal $\ideal{p}\neq A$ with $A/\ideal{p}$ entire,
called <span class="define">prime ideal</span> or just <span class="define">prime</span>;

</div>
<ul>
<li>
	equivalently,
ideal $\ideal{p}\neq A$ is <span class="define">prime</span>
if and only if
$\left(
\forall x,y \in A
\right)
\left(
xy \in \ideal{p}
\Rightarrow
x \in \ideal{p}
\mbox{ or }
y \in \ideal{p}
\right)$

</li>
</ul>
<div class="definition" id="definition:maximal---ideal" data-name="maximal ideal">
	



for commutative ring $A$,
ideal $\ideal{m}\neq A$ such that

$$
\left(
\forall \mbox{ ideal } \ideal{a} \subset A
\right)
\left(
\ideal{m} \subset \ideal{a} \Rightarrow \ideal{a} = A
\right)
$$

called <span class="define">maximal ideal</span>

</div>
<div class="lemma" id="lemma:properties---of---prime---and---maximal---ideals" data-name="properties of prime and maximal ideals">
	
for commutative ring $A$







	<ul>
	<li>
		every maximal ideal is prime

	</li>
	<li>
		every ideal is contained in some maximal ideal

	</li>
	<li>
		ideal $\{0\}$ is prime if and only if $A$ is entire

	</li>
	<li>
		ideal $\ideal{m}$ is maximal if and only if $A/\ideal{m}$ is field

	</li>
	<li>
		inverse image of prime ideal of commutative ring homeomorphism
is prime

	</li>
	</ul>

</div>

<h3>Embedding of ring</h3>

<div class="definition" id="definition:ring-isomorphism" data-name="ring-isomorphism">
	
bijective ring-homeomorphism (<a href="#definition:ring-homeomorphism"></a>) is isomorphism

</div>

<ul>
<li>
	indeed,
for bijective ring-isomorphism $f:A\to B$,
exists set-theoretic inverse $g:B\to A$ of $f$,
which is ring-homeomorphism

</li>
</ul>
<div class="lemma" id="lemma:image---of---ring-homeomorphism---is---subring" data-name="image of ring-homeomorphism is subring">
	
image $f(A)$ of ring-homeomorphism $f:A\to B$
is subring of $B$


</div>
<div class="definition" id="definition:embedding---of---ring" data-name="embedding of ring">
	


ring-isomorphism between $A$ and its image,
established by injective ring-homeomorphism $f:A\to B$,
called <span class="define">embedding of ring</span>

</div>
<div class="definition" id="definition:induced---injective---ring-homeomorphism" data-name="induced injective ring-homeomorphism">
	

for ring-homeomorphism $f:A\to A'$
and ideal $\ideal{a}'$ of $A'$,
injective ring-homeomorphism

$$
A/f^{-1}(\ideal{a}') \to A'/\ideal{a}'
$$

called <span class="define">induced injective ring-homeomorphism</span>

</div>

<h3>Characteristic of ring</h3>

<ul>
<li>
	for ring $A$,
consider ring-homeomorphism

$$
\lambda:\integers \to A
$$

such that

$$
\lambda(n) = ne
$$

where $e$ is multiplicative unit element of $A$
	<ul>
	<li>
		kernel of $\lambda$ is ideal $(n)$
for some $n\geq0$,
<i>i.e.</i>,
ideal generated by some nonnegative integer $n$

	</li>
	<li>
		hence, canonical injective ring-homeomorphism $\integers/n\integers \to A$,
which is ring-isomorphism between $\integers/n\integers$ and subring of $A$

	</li>
	<li>
		when $n\integers$ is prime ideal,
exist two cases; either $n=0$ or $n=p$ for prime number $p$

	</li>
	</ul>

</li>
</ul>
<div class="definition" id="definition:characteristic---of---ring" data-name="characteristic of ring">
	


ring $A$ with $\{0\}$ as prime ideal kernel above,
said to have <span class="define">characteristic $0$</span>;
if prime ideal kernel is $p\integers$ for prime number $p$,
$A$,
said to have <span class="define">characteristic $p$</span>,
in which case,
$A$ contains (isomorphic image of) $\integers/p\integers$ as subring,
abbreviated by <span class="define">\primefield{p}</span>

</div>

<h3>Prime fields and prime rings</h3>

<ul>
<li>
	field $K$ has characteristic $0$ or $p$ for prime number $p$



</li>
<li>
	$K$ contains as subfield (isomorphic image of)

	<ul>
	<li>
		$\rationals$ if characteristic is $0$

	</li>
	<li>
		$\primefield{p}$ if characteristic is $p$

	</li>
	</ul>

</li>
</ul>

<div class="definition" id="definition:prime---field" data-name="prime field">
	


in above cases,
both $\rationals$ and $\primefield{p}$,
called <span class="define">prime field (contained in $K$)</span>;
since prime field is smallest subfield of $K$
containing $1$ having no automorphism other than identity,
identify it with $\rationals$ or $\primefield{p}$
for each case

</div>
<div class="definition" id="definition:prime---ring" data-name="prime ring">
	


in above cases,
<span class="define">prime ring (contained in $K$)</span>
means either integers $\integers$ if $K$ has characteristic $0$
or $\primefield{p}$ if $K$ has characteristic $p$

</div>


<h3>$\integers/n\integers$</h3>


<ul>
<li>
	$\integers$ is ring


</li>
<li>
	every ideal of $\integers$ is principal,
<i>i.e.</i>, either $\{0\}$ or $n\integers$ for some $n\in\naturals$
(refer to page~<a href="#page:nonzero---ideals---of---integers---are---principal">here</a>)

</li>
<li>
	ideal of $\integers$ is prime if and only if is $p\integers$ for some prime number $p\in\naturals$


	<ul>
	<li>
		$p\integers$ is maximal ideal

	</li>
	</ul>

</li>
</ul>

<div class="definition" id="definition:ring---of---integers---modulo---$n$" data-name="ring of integers modulo $n$">
	


$\integers/n\integers$, called <span class="define">ring of integers modulo $n$</span>;
abbreviated as <span class="define">$\mbox{mod }n$</span>

</div>
<ul>
<li>
	$\integers/p\integers$ for prime $p$
is <i>field</i> and denoted by <span class="notation">\primefield{p}</span>



</li>
</ul>


<h3>Euler phi-function</h3>

<div class="definition" id="definition:Euler---phi-function" data-name="Euler phi-function">
	






for $n>1$,
order of <a href="#definition:divison---rings">divison ring</a> of $\integers/n\integers$,
called <span class="define">Euler phi-function</span>,
denoted by <span class="notation">$\varphi(n)$</span>;
if prime factorization of $n$ is

$$
n = p_1^{e_1} \cdots p_r^{e_r}
$$

with distinct $p_i$ and $e_i\geq1$

$$
\varphi(n)
= p_1^{e_1-1} (p_1 - 1)
\cdots
p_r^{e_r-1} (p_r - 1)
$$


</div>

<div class="theorem" id="theorem:Euler's---theorem" data-name="Euler's theorem">
	


for $x$ prime to $n$

$$
x^{\varphi(n)} \equiv 1 \Mod{n}
$$


</div>


<h3>Chinese remainder theorem</h3>

<div class="theorem" id="theorem:Chinese---remainder---theorem" data-name="Chinese remainder theorem">
	

for ring $A$
and
$n$ ideals $\ideal{a}_1$, &hellip; $\ideal{a}_n$ ($n\geq2$)
with $\ideal{a}_i + \ideal{a}_j=A$ for all $i \neq j$

$$
\left(
\forall
x_1,\ldots, x_n \in A
\right)
\left(
\exists x \in A
\right)
\left(
\forall 1\leq i\leq n
\right)
\left(
x \equiv x_i
\Mod{\ideal{a}_i}
\right)
$$


</div>
<div class="corollary" id="corollary:isomorphism---induced---by---Chinese---remainder---theorem" data-name="isomorphism induced by Chinese remainder theorem">
	


for ring $A$,
$n$ ideals $\ideal{a}_1$, &hellip; $\ideal{a}_n$ ($n\geq2$)
with $\ideal{a}_i + \ideal{a}_j=A$ for all $i \neq j$,
and
map of $A$ into product induced by canonical maps of $A$ onto $A/\ideal{a}_i$
for each factor,
<i>i.e.</i>,

$$
f: A
\to
\prod A/\ideal{a}_i
$$

$f$ is surjective
and
$\Ker f = \bigcap \ideal{a}_i$,
hence, exists isomorphism

$$
A/\cap \ideal{a}_i \isomorph \prod A/\ideal{a}_i
$$


</div>

<h3>Isomorphism of endomorphisms of cyclic groups</h3>

<div class="theorem" id="theorem:isomorphism---of---endomorphisms---of---cyclic---groups" data-name="isomorphism of endomorphisms of cyclic groups">
	

for cyclic group $A$ of order $n$,
endomorphisms of $A$ into $A$
with $x\mapsto kx$ for $k\in\integers$
induce

	<ul>
	<li>
		ring isomorphism

$$
\integers/n\integers \isomorph \End(A)
$$


	</li>
	<li>
		group isomorphism

$$
(\integers/n\integers)^\ast \isomorph \Aut(A)
$$


	</li>
	</ul>
where
$(\integers/n\integers)^\ast$
denotes group of units of
$\integers/n\integers$
(<a href="#definition:multiplicative---group---of---invertible---elements---of---ring"></a>)

</div>
<ul>
<li>
	<i>e.g.</i>,
for group of $n$-th roots of unity in $\complexes$,
all automorphisms are given by

$$
\xi \mapsto \xi^k
$$

for $k\in(\integers/n\integers)^\ast$

</li>
</ul>

<h3>Irreducibility and factorial rings</h3>

<div class="definition" id="definition:irreducible---ring---element" data-name="irreducible ring element">
	


for entire ring $A$,
non-unit non-zero element $a\in A$ with

$$
\left(
\forall b, c\in A
\right)
\left(
a = bc \Rightarrow b \mbox{ or } c \mbox{ is unit}
\right)
$$

said to be <span class="define">irreducible</span>

</div>

<div class="definition" id="definition:unique---factorization---into---irreducible---elements" data-name="unique factorization into irreducible elements">
	


for entire ring $A$,
element $a\in A$
for which,
exists unit $u$ and irreducible elements, $p_1$, &hellip;, $p_r$ in $A$ such that

$$
a = u \prod p_i
$$

and this expression is unique up to permutation and multiplications by units,
said to have <span class="define">unique factorization into irreducible elements</span>

</div>

<div class="definition" id="definition:factorial---ring" data-name="factorial ring">
	


entire ring with every non-zero element has unique factorial into irreducible elements,
called <span class="define">factorial ring</span> or <span class="define">unique factorization ring</span>

</div>

<h3>Greatest common divisor</h3>

<div class="definition" id="definition:devision---of---entire---ring---elements" data-name="devision of entire ring elements">
	


for entire ring $A$ and nonzero elements $a,b\in A$,
<span class="define">$a$ said to divide $b$</span>
if exists $c\in A$ such that $ac=b$,
denoted by <span class="notation">$a|b$</span>

</div>
<div class="definition" id="definition:greatest---common---divisor" data-name="greatest common divisor">
	


for entire ring $A$ and $a,b\in A$,
$d\in A$ which divides $a$ and $b$ and satisfies

$$
\left(
\forall c \in A
\right)
\left(
c|a \mbox{ \& } c|b
\Rightarrow
c | d
\right)
$$

called <span class="define">greatest common divisor (g.c.d.) of $a$ and $b$</span>

</div>
<div class="proposition" id="proposition:existence---of---greatest---common---divisor---of---principal---entire---rings" data-name="existence of greatest common divisor of principal entire rings">
	


for principal entire ring $A$
and nonzero $a,b\in A$,
$c\in A$ with $(a,b) = (c)$
is g.c.d. of $a$ and $b$

</div>
<div class="theorem" id="theorem:principal---entire---ring---is---factorial" data-name="principal entire ring is factorial">
	
principal entire ring is factorial

</div>

<h2 id="title-page:Polynomials">Polynomials</h2>



<h3>Why (ring of) polynomials?</h3>





<ul>
<li>
	lays ground work for polynomials in general

</li>
<li>
	needs polynomials over arbitrary rings for diverse purposes
	<ul>
	<li>
		polynomials over finite field
which cannot be identified with polynomial functions in that field


	</li>
	<li>
		polynomials with integer coefficients;

reduce them mod $p$ for prime $p$

	</li>
	<li>
		polynomials over arbitrary commutative rings


	</li>
	<li>
		rings of polynomial differential operators

for
algebraic geometry &amp; analysis

	</li>
	</ul>

</li>
<li>
	<i>e.g.</i>, ring learning with errors (RLWE)
for cryptographic algorithms

</li>
</ul>


<h3>Ring of polynomials</h3>

<ul>
<li>
	exist many ways to define polynomials over commutative ring;
here's one

</li>
</ul>
<div class="definition" id="definition:polynomial" data-name="polynomial">
	



for ring $A$,
set of functions from monoid $S = \set{X^r}{r\in\integers, r\geq0}$
into $A$
which are equal to $0$
except finite number of elements of $S$,
called <span class="define">polynomials over $A$</span>,
denoted by <span class="notation">$A[X]$</span>

</div>
<ul>
<li>
	for every $a\in A$,
define function which has value $a$ on $X^n$, and value $0$ for every other element of $S$,
by <span class="define">$aX^r$</span>

</li>
<li>
	then, <i>a</i> polynomial can be uniquely written as

$$
f(X) = a_0X^0 + \cdots + a_nX^n
$$

for some $n\in\integers_+$,
$a_i\in A$

</li>
<li>
	$a_i$, called <span class="define">coefficients of $f$</span>

</li>
</ul>


<h3>Polynomial functions</h3>

<div class="definition" id="definition:polynomial---function" data-name="polynomial function">
	

for two rings $A$ and $B$ with $A\subset B$
and $f\in A[X]$ with $f(X) = a_0 + a_1 X + \cdots + a_nX^n$,
map $f_B: B\to B$ defined by

$$
f_B(x) = a_0 + a_1 x + \cdots + a_n x^n
$$

called <span class="define">polynomial function associated with $f(X)$</span>

</div>
<div class="definition" id="definition:evaluation---homeomorphism" data-name="evaluation homeomorphism">
	


for two rings $A$ and $B$ with $A\subset B$ and $b\in B$,
ring homeomorphism from $A[X]$ into $B$
with association, $\ev_b:f\mapsto f(b)$,
called <span class="define">evaluation homeomorphism</span>,
said to be obtained by <span class="define">substituting $b$ for $X$ in $f$</span>

</div>
<ul>
<li>
	hence, for $x\in B$, subring <span class="define">$A[x]$</span> of $B$
generated by $x$ over $A$ is
ring of all polynomial values $f(x)$ for $f\in A[X]$

</li>
</ul>
<div class="definition" id="definition:variables---and---transcendentality" data-name="variables and transcendentality">
	


for two rings $A$ and $B$ with $A\subset B$,
if $x\in B$ makes evaluation homeomorphism $\ev_x:f\mapsto f(x)$ isomorphic,
$x$, said to be <span class="define">transcendental over $A$</span>
or <span class="define">variable over $A$</span>

</div>
<ul>
<li>
	in particular, <i>$X$ is variable over $A$</i>

</li>
</ul>

<h3>Polynomial examples</h3>

<ul>
<li>
	consider $\alpha=\sqrt{2}$ and $\bigset{a+b\alpha}{a,b\in\integers}$,
subring of $\integers[\alpha]\subset \reals$
generated by $\alpha$.
	<ul>
	<li>
		$\alpha$ is <i>not</i> transcendental
because $f(\alpha)=0$ for $f(X)=X^2-1$

	</li>
	<li>
		hence kernel of evaluation map of $\integers[X]$ into $\integers[\alpha]$
is not injective,
hence not isomorphism

	</li>
	<li>
		indeed

$$
\integers[\alpha] = \bigset{a+b\alpha}{a,b\in\integers}
$$


	</li>
	</ul>

</li>
<li>
	consider $\primefield{p}$ for prime number $p$
	<ul>
	<li>
		$f(X) = X^p - X\in \primefield{p}[X]$ is not zero polynomial,
but because $x^{p-1} \equiv 1$ for every nonzero $x\in\primefield{p}$
by <a href="#theorem:Euler's---theorem"></a> (Euler's theorem),
$x^p\equiv x$ for every $x\in\primefield{p}$,
thus for polynomial function, $f_{\primefield{p}}$,
$f_{\primefield{p}}(x)=0$ for every $x$ in $\primefield{p}$

	</li>
	<li>
		<i>i.e.</i>, <span class="emph">non-zero polynomial induces zero polynomial function</span>

	</li>
	</ul>

</li>
</ul>

<h3>Reduction map</h3>



<ul>
<li>
	for homeomorphism $\varphi:A\to B$ of commutative rings,
exists associated homeomorphisms
of polynomial rings $A[X]\to B[X]$
such that

$$
f(X) = \sum a_i X^i
\mapsto
\sum \varphi(a_i) X^i
= (\varphi f)(X)
$$


</li>
</ul>
<div class="definition" id="definition:reduction---map" data-name="reduction map">
	


above ring homeomorphism $f\mapsto \varphi f$,
called <span class="define">reduction map</span>

</div>
<ul>
<li>
	<i>e.g.</i>, for complex conjugate $\varphi: \complexes \to \complexes$,
homeomorphism of $\complexes[X]$ into itself
can be obtained by reduction map $f \mapsto \varphi f$,
which is complex conjugate of polynomials with complex coefficients

</li>
</ul>
<div class="definition" id="definition:reduction---of---$f$---modulo---$p$" data-name="reduction of $f$ modulo $p$">
	


for prime ideal $\ideal{p}$ of ring $A$
and
surjective canonical map $\varphi: A \to A/\ideal{p}$,
reduction map $\varphi f$ for $f\in A[X]$,
sometimes called <span class="define">reduction of $f$ modulo \ideal{p}</span>

</div>

<h3>Basic properties of polynomials in one variable</h3>

<div class="theorem" id="theorem:Euclidean---algorithm" data-name="Euclidean algorithm">
	


for set of all polynomials in one variable of nonnegative degrees $A[X]$
with commutative ring $A$

$$
\begin{eqnarray*}
&&
\left(
\forall f,g \in A[X]
\mbox{ with leading coefficients of } g \mbox{ unit in }A
\right)

\\
&&
\left(
\exists q, r \in A[X]
\mbox{ with } \deg r < \deg g
\right)
\left(
f = qg + r
\right)
\end{eqnarray*}
$$


</div>

<div class="theorem" id="theorem:principality---of---polynomial---ring" data-name="principality of polynomial ring">
	

polynomial ring in one variable $k[X]$ with field $k$
is principal

</div>

<div class="corollary" id="corollary:factoriality---of---polynomial---ring" data-name="factoriality of polynomial ring">
	

polynomial ring in one variable $k[X]$ with field $k$
is factorial

</div>


<h3>Constant, monic, and irreducible polynomials</h3>

<div class="definition" id="definition:constant---and---monic---polynomials" data-name="constant and monic polynomials">
	




$k \in k[X]$ with field $k$,
called <span class="define">constant polynomial</span>;
$f(x) \in k[X]$ with leading coefficient $1$,
called <span class="define">monic polynomial</span>

</div>

<div class="definition" id="definition:irreducible---polynomials" data-name="irreducible polynomials">
	



polynomial $f(x)\in k[X]$ such that

$$
\left(
\forall g(X), h(X) \in k[X]
\right)
\left(
f(X) = g(X)h(X) \Rightarrow g(X) \in k \mbox{ or } h(X) \in k
\right)
$$

said to be <span class="define">irreducible</span>

</div>


<h3>Roots or zeros of polynomials</h3>

<div class="definition" id="definition:root---of---polynomial" data-name="root of polynomial">
	




for commutative ring $B$, its subring $A\subset B$,
and $f(x)\in A[X]$ in one variable,
$b\in B$ satisfying

$$
f(b) = 0
$$

called <span class="define">root</span> or <span class="define">zero</span> of $f$

</div>

<div class="theorem" id="theorem:number---of---roots---of---polynomial" data-name="number of roots of polynomial">
	

for field $k$,
polynomial $f\in k[X]$ in one variable of degree $n\geq 0$
has at most $n$ roots in $k$;
if $a$ is root of $f$ in $k$,
$X-a$ divides $f(X)$

</div>


<h3>Induction of zero functions</h3>

<div class="corollary" id="corollary:induction---of---zero---function---in---one---variable" data-name="induction of zero function in one variable">
	

for field $k$ and infinite subset $T\subset k$,
if polynomial $f\in k[X]$ in one variable over $k$
satisfies

$$
\left(
\forall a \in k
\right)
\left(
f(a) =0
\right)
$$

then $f(0)=0$,
<i>i.e.</i>,
$f$ induces zero function

</div>
<div class="corollary" id="corollary:induction---of---zero---function---in---multiple---variables" data-name="induction of zero function in multiple variables">
	

for field $k$ and $n$ infinite subsets of $k$, $\seq{S_i}_{i=1}^n$,
if polynomial in $n$ variables over field $k$
satisfies

$$
\left(
\forall a_i\in S_i \mbox{ for } 1\leq i \leq n
\right)
\left(
f(a_1,\ldots,a_n)=0
\right)
$$

then
$f=0$,
<i>i.e.</i>,
$f$ induces zero function

</div>
<div class="corollary" id="corollary:induction---of---zero---functions---in---multiple---variables-------infinite---fields" data-name="induction of zero functions in multiple variables - infinite fields">
	

if polynomial in $n$ variables over infinite field $k$
induces zero function in $k^{(n)}$,
$f=0$

</div>
<div class="corollary" id="corollary:induction---of---zero---functions---in---multiple---variables-------finite---fields" data-name="induction of zero functions in multiple variables - finite fields">
	

if polynomial in $n$ variables over finite field $k$ of order $q$,
degree of which in each variable is less than $q$,
induces zero function in $k^{(n)}$,
$f=0$

</div>

<h3>Reduced polynomials and uniqueness</h3>

<ul>
<li>
	for field $k$ with $q$ elements,
polynomial in $n$ variables over $k$
can be expressed as

$$
f(X_1,\ldots,X_n) = \sum a_i X_1^{\nu_{i,1}} \cdots X_n^{\nu_{i,n}}
$$

for finite sequence, $\seqscr{a_i}{i=1}{m}$, and
$\seqscr{\nu_{i,1}}{i=1}{m}$,
&hellip;,
$\seqscr{\nu_{i,n}}{i=1}{m}$
where $a_i\in k$ and $\nu_{i,j} \geq 0$

</li>
<li>
	because $X_i^q=X_i$ for any $X_i$,
any $\nu_{i,j}\geq q$ can be (repeatedly) replaced by $\nu_{i,j}-(q-1)$,
hence
$f$ can be rewritten as

$$
f(X_1,\ldots,X_n) = \sum a_i X_1^{\mu_{i,1}} \cdots X_n^{\mu_{i,n}}
$$

where $0\leq \mu_{i,j} < q$ for all $i,j$

</li>
</ul>
<div class="definition" id="definition:reduced---polynomials" data-name="reduced polynomials">
	

above polynomial, called <span class="define">reduced polynomial</span>,
denoted by <span class="notation">$f^\ast$</span>

</div>
<div class="corollary" id="corollary:uniqueness---of---reduced---polynomials" data-name="uniqueness of reduced polynomials">
	

for field $k$ with $q$ elements,
reduced polynomial is unique
(by <a href="#corollary:induction---of---zero---functions---in---multiple---variables-------finite---fields"></a>)

</div>


<h3>Multiplicative subgroups and $n$-th roots of unity</h3>

<div class="definition" id="definition:multiplicative---subgroup---of---field" data-name="multiplicative subgroup of field">
	


for field $k$,
subgroup of group $k^\ast=k\sim \{0\}$,
called <span class="define">multiplicative subgroup of $k$</span>

</div>

<div class="theorem" id="theorem:finite---multiplicative---subgroup---of---field---is---cyclic" data-name="finite multiplicative subgroup of field is cyclic">
	
finite multiplicative subgroup of field is cyclic

</div>

<div class="corollary" id="corollary:multiplicative---subgroup---of---finite---field---is---cyclic" data-name="multiplicative subgroup of finite field is cyclic">
	
multiplicative subgroup of finite field is cyclic

</div>

<div class="definition" id="definition:primitive---$n$-th---root---of---unity" data-name="primitive $n$-th root of unity">
	



generator for group of $n$-th roots of unity,
called <span class="define">primitive $n$-th root of unity</span>;
group of roots of unity, denoted by <span class="notation">$\mu$</span>;
group of roots of unity in field $k$, denoted by <span class="notation">$\mu(k)$</span>

</div>


<h3>Algebraic closedness</h3>

<div class="definition" id="definition:algebraically---closed" data-name="algebraically closed">
	





field $k$, for which every polynomial in $k[X]$ of positive degree has root in $k$,
said to be <span class="define">algebraically closed</span>

</div>
<ul>
<li>
	<i>e.g.</i>, complex numbers are algebraically closed

</li>
<li>
	every field is contained in some algebraically closed field
(<a href="#theorem:existence---of---algebraically---closed---field---extensions"></a>)

</li>
<li>
	for algebraically closed field $k$
	<ul>
	<li>
		(of course) every irreducible polynomial in $k[X]$ is of degree $1$

	</li>
	<li>
		unique factorization of polynomial of nonnegative degree can be written in form

$$
f(X) = c \prod_{i=1}^{r} (X-\alpha_i)^{m_i}
$$

with nonzero $c\in k$, distinct roots, $\alpha_1,\ldots,\alpha_r \in k$,
and
$m_1,\ldots,m_r \in \naturals$

	</li>
	</ul>

</li>
</ul>

<h3>Derivatives of polynomials</h3>

<div class="definition" id="definition:derivative---of---polynomial---over---commutative---ring" data-name="derivative of polynomial over commutative ring">
	


for polynomial $f(X) = a_nX^n + \cdots + a_1 X + a_0 \in A[X]$ with commutative ring $A$,
map $D:A[X] \to A[X]$
defined by

$$
Df(X) = na_n X^{n-1} + \cdots + a_1
$$

called <span class="define">derivative of polynomial</span>,
denoted by <span class="notation">$f'(X)$</span>;

</div>
<ul>
<li>
	for $f,g\in A[X]$ with commutative ring $A$, and $a\in A$

$$
(f+g)' = f' + g'
\quad
\mbox{\&}
\quad
(fg)' = f'g + fg'
\quad
\mbox{\&}
\quad
(af)' = af'
$$


</li>
</ul>


<h3>Multiple roots and multiplicity</h3>

<ul>
<li>
	nonzero polynomial $f(X)\in k[X]$ in one variable over field $k$
having $a\in k$ as root
can be written of form

$$
f(X) = (X-a)^m g(X)
$$

with some polynomial $g(X)\in A[X]$
relatively prime to $(X-a)$ (hence, $g(a)\neq0$)

</li>
</ul>
<div class="definition" id="definition:multiplicity---and---multiple---roots" data-name="multiplicity and multiple roots">
	




above, $m$, called <span class="define">multiplicity of $a$ in $f$</span>;
$a$, said to be <span class="define">multiple root of $f$</span>
if $m>1$

</div>

<div class="proposition" id="proposition:necessary---and---sufficient---condition---for---multiple---roots" data-name="necessary and sufficient condition for multiple roots">
	



for polynomial $f$ of one variable over field $k$,
$a\in k$ is multiple root of $f$
if and only if
$f(a)=0$ and $f'(a)=0$

</div>

<div class="proposition" id="proposition:derivative---of---polynomial" data-name="derivative of polynomial">
	


for polynomial $f\in K[X]$ over field $K$ of positive degree,
$f'\neq0$ if $K$ has characteristic $0$;
if $K$ has characteristic $p>0$,
$f'=0$
if and only if

$$
f(X) = \sum_{\nu=1}^n a_\nu X^\nu
$$

where $p$ divides each integer $\nu$ whenever $a_\nu\neq0$

</div>


<h3>Frobenius endomorphism</h3>


<ul>
<li>
	homeomorphism of $K$ into itself $x\mapsto x^p$
has trivial kernel, hence injective

</li>
<li>
	hence,
iterating $r\geq 1$ times yields endomorphism, $x\mapsto x^{p^r}$

</li>
</ul>

<div class="definition" id="definition:Frobenius---endomorphism" data-name="Frobenius endomorphism">
	



for field $K$, prime number $p$, and $r\geq1$,
endomorphism of $K$ into itself, $x\mapsto x^{p^r}$,
called <span class="define">Frobenius endomorphism</span>

</div>


<h3>Roots with multiplicity $p^r$ in fields having characteristic $p$</h3>


<ul>
<li>
	for field $K$ having characteristic $p$
	<ul>
	<li>
		$p | {p \choose \nu}$ for all $0< \nu < p$ because $p$ is prime,
hence,
for every $a,b\in K$

$$
(a+b)^p = a^p + b^p
$$


	</li>
	<li>
		applying this resurvely $r$ times yields

$$
(a+b)^{p^r}
= (a^p + b^p)^{p^{r-1}}
= (a^{p^2} + b^{p^2})^{p^{r-2}}
= \cdots
= a^{p^r} + b^{p^r}
$$

hence

$$
(X-a)^{p^r} = X^{p^r} - a^{p^r}
$$


	</li>
	<li>
		if $a,c\in K$ satisfy $a^{p^r} = c$

$$
X^{p^r} - c
= X^{p^r} - a^{p^r}
= (X-a)^{p^r}
$$

hence, polynomial $X^{p^r}-c$ has precisely one root $a$ of multiplicity $p^r$!

	</li>
	</ul>

</li>
</ul>

<h2 id="title-page:Algebraic---Extension">Algebraic Extension</h2>




<h3>Algebraic extension</h3>


<ul>
<li>
	will show
	<ul>
	<li>
		for polynomial over field,
always exists some extension of <i>that</i> field
where the polynomial has root

	</li>
	<li>
		existence of algebraic closure
for every field

	</li>
	</ul>

</li>
</ul>


<h3>Extension of field</h3>

<div class="definition" id="definition:extension---of---field" data-name="extension of field">
	

for field $E$ and its subfield $F\subset E$,
$E$
said to be <span class="define">extension field of $F$</span>,
(sometimes) denoted by <span class="notation">$E/F$</span>
(which should <i>not</i> confused with <i>factor group</i>)

	<ul>
	<li>
		can view $E$ as <span class="define">vector space</span> over $F$


	</li>
	<li>
		if dimension of the vector space is finite,
extension called <span class="define">finite extension of $F$</span>





	</li>
	<li>
		if infinite,
called <span class="define">infinite extension of $F$</span>





	</li>
	</ul>

</div>

<h3>Algebraic over field</h3>

<div class="definition" id="definition:algebraic---over---field" data-name="algebraic over field">
	


for field $E$ and its subfield $F\subset E$,
$\alpha\in E$ satisfying

$$
\left(
\exists a_0,\ldots, a_n
\mbox{ with not all } a_i \mbox{ zero}
\right)
\left(
a_0 + a_1\alpha + \cdots + a_n \alpha^n=0
\right)
$$

said to be <span class="define">algebraic over $F$</span>

	<ul>
	<li>
		for algebraic $\alpha\neq0$,
can always find such equation like above that $a_0\neq0$

	</li>
	</ul>

</div>
<ul>
<li>
	equivalent statements to <a href="#definition:algebraic---over---field"></a>
	<ul>
	<li>
		exists homeomorphism $\varphi: F[X] \to E$ such that


$$
\left(\forall x\in F\right) \left(\varphi(x) = x\right)
\mbox{ \& }
\varphi(X) = \alpha
\mbox{ \& }
\Ker \varphi \neq \{0\}
$$


	</li>
	<li>
		exists evaluation homeomorphism $\ev_\alpha: F[X] \to E$
with nonzero kernel
(refer to <a href="#definition:evaluation---homeomorphism"></a> for definition of evaluation homeomorphism)

	</li>
	</ul>

</li>
<li>
	in which case,
$\Ker \varphi$ is principal ideal
(by <a href="#theorem:principality---of---polynomial---ring"></a>),
hence generated by single element,
thus exists nonzero $p(X) \in F[X]$ (with normalized leading coefficient being $1$)
so that

$$
F[X] / (p(X)) \isomorph F[\alpha]
$$


</li>
<li>
	$F[\alpha]$ <i>entire</i> (<a href="#lemma:every---field---is---entire---ring"></a>),
hence $p(X)$ irreducible (refer to <a href="#definition:prime---ideal"></a>)

</li>
</ul>

<div class="definition" id="definition:THE---irreducible---polynomial" data-name="THE irreducible polynomial">
	



normalized $p(X)$ (<i>i.e.</i>, with leading coefficient being $1$)
uniquely determined by $\alpha$,
called <span class="define">THE irreducible polynomial of $\alpha$ over $F$</span>,
denoted by <span class="notation">$\Irr(\alpha, F, X)$</span>

</div>


<h3>Algebraic extensions</h3>

<div class="definition" id="definition:algebraic---extension" data-name="algebraic extension">
	




for field $F$,
its extension field every element of which is algebraic over $F$,
said to be <span class="define">algebraic extension of $F$</span>

</div>

<div class="proposition" id="proposition:algebraicness---of---finite---field---extensions" data-name="algebraicness of finite field extensions">
	




for field $F$,
every finite extension field of $F$
is algebraic over $F$

</div>
<ul>
<li>
	converse is <i>not</i> true,
<i>e.g.</i>,
subfield of complex numbers
consisting of algebraic numbers over $\rationals$
is infinite extension of $\rationals$

</li>
</ul>


<h3>Dimension of extensions</h3>



<div class="definition" id="definition:dimension---of---extension" data-name="dimension of extension">
	


for field $F$ and its extension field $E$,
dimension of $E$ as vector space over $F$,
called <span class="define">dimension of $E$ over $F$</span>,
denoted by <span class="notation">\dimext{E}{F}</span>

</div>

<div class="proposition" id="proposition:dimension---of---finite---extension" data-name="dimension of finite extension">
	

for field $k$ and its extension fields $F$ and $E$
with $k\subset F\subset E$

$\dimext{E}{k}
=
\dimext{E}{F}
\dimext{F}{k}$


	<ul>
	<li>
		if $\seqscr{x_i}{i\in I}{}$ is basis for $F$ over $k$,
and $\seqscr{y_j}{j\in J}{}$ is basis for $E$ over $F$,
$\seqscr{x_iy_j}{(i,j)\in I\times J}{}$
is basis for $E$ over $k$

	</li>
	</ul>

</div>

<div class="corollary" id="corollary:finite---dimension---of---extension" data-name="finite dimension of extension">
	

for field $k$ and its extension fields $F$ &amp; $E$
with $k\subset F\subset E$,
$E/k$ is finite
if and only if
both
$F/k$
and
$E/F$
are finite

</div>


<h3>Generation of field extensions</h3>

<div class="definition" id="definition:generation---of---field---extensions" data-name="generation of field extensions">
	



for field $k$, its extension field $E$, and $\alpha_1,\ldots, \alpha_n \in E$,
smallest subfield containing $k$ and $\alpha_1$, &hellip;, $\alpha_n$,
said to be <span class="define">finitely generated over $k$ by $\alpha_1$, \ldots, $\alpha_n$</span>,
denoted by <span class="notation">$k(\alpha_1,\ldots, \alpha_n)$</span>

</div>
<ul>
<li>
	$k(\alpha_1,\ldots, \alpha_n)$ consists of all quotients
$f(\alpha_1,\ldots,\alpha_n)/g(\alpha_1,\ldots, \alpha_n)$
where $f,g\in k[X]$ and $g(\alpha_1,\ldots, \alpha_n)\neq0$,
<i>i.e.</i>

$$
\begin{eqnarray*}
&&
k(\alpha_1,\ldots,\alpha_n)

\\
&=& \bigset{f(\alpha_1,\ldots, \alpha_n)/g(\alpha_1,\ldots,\alpha_n)}{f,g\in f[X], g(\alpha_1,\ldots,\alpha_n)\neq0}
\end{eqnarray*}
$$


</li>
<li>
	<i>any</i> field extension $E$ over $k$
is union of smallest subfields containing $\alpha_1,\ldots, \alpha_n$
where $\alpha_1,\ldots, \alpha_n$ range over finite set of elements of $E$,
<i>i.e.</i>

$$
E =
\bigcup_{n\in\naturals}
\bigcup_{\alpha_1, \ldots, \alpha_n \in E}
k(\alpha_1,\ldots,\alpha_n)
$$


</li>
</ul>
<div class="proposition" id="proposition:finite---extension---is---finitely---generated" data-name="finite extension is finitely generated">
	

every finite extension of field is finitely generated

</div>

<h3>Tower of fields</h3>

<div class="definition" id="definition:tower---of---fields" data-name="tower of fields">
	

sequence of extension fields

$$
F_1
\subset
F_2
\subset
\cdots
\subset
F_n
$$

called <span class="define">tower of fields</span>

</div>

<div class="definition" id="definition:finite---tower---of---fields" data-name="finite tower of fields">
	


tower of fields,
said to be <span class="define">finite</span>
if and only if
each step of extensions is finite

</div>


<h3>Algebraicness of finitely generated subfields</h3>

<div class="proposition" id="proposition:algebraicness---of---finitely---generated---subfield---by---single---element" data-name="algebraicness of finitely generated subfield by single element">
	

for field $k$, its extension field $E$, and $\alpha\in E$ being algebraic over $k$

$$
k(\alpha) = k[\alpha]
$$

and

$$
[k(\alpha):k] = \deg \Irr(\alpha, k, X)
$$

hence $k(\alpha)$ is finite extension of $k$,
thus <i>algebraic extension over $k$</i>
(by <a href="#proposition:algebraicness---of---finite---field---extensions"></a>)

</div>

<div class="lemma" id="lemma:a---fortiori---algebraicness" data-name="a fortiori algebraicness">
	



for field $k$,
its extension field $F$,
and $\alpha\in E$ being algebraic over $k$
where $k(\alpha)$ and $F$ are subfields of common field,
$\alpha$ is algebraic over $F$

	<ul>
	<li>
		indeed, $\Irr(\alpha,k,X)$
has <i>a fortiori</i>
coefficients in $F$

	</li>
	</ul>

</div>



<ul>
<li>
	assume tower of fields

$$
k \subset k(\alpha_1) \subset k(\alpha_1, \alpha_2) \subset \cdots \subset k(\alpha_1,\ldots, \alpha_n)
$$

where $\alpha_i$ is algebraic over $k$

</li>
<li>
	then, $\alpha_{i+1}$ is algebraic over $k(\alpha_1,\ldots,\alpha_i)$ (by <a href="#lemma:a---fortiori---algebraicness"></a>)

</li>
</ul>

<div class="proposition" id="proposition:algebraicness---of---finitely---generated---subfields---by---multiple---elements" data-name="algebraicness of finitely generated subfields by multiple elements">
	

for field $k$
and
$\alpha_1$, &hellip;, $\alpha_n$ being algebraic over $k$,
$E=k(\alpha_1,\ldots,\alpha_n)$
is finitely algebraic over $k$
(due to <a href="#proposition:algebraicness---of---finitely---generated---subfield---by---single---element"></a>,
<a href="#proposition:dimension---of---finite---extension"></a>,
and
<a href="#proposition:algebraicness---of---finite---field---extensions"></a>).
Indeed, $E = k[\alpha_1, \ldots, \alpha_n]$ and

$$
\begin{eqnarray*}
[k(\alpha_1,\ldots,\alpha_n):k] &=& \deg \Irr(\alpha_1,k,X) \deg \Irr(\alpha_2,k(\alpha_1),X)
\\
&&
\cdots \deg \Irr(\alpha_n, k(\alpha_1,\ldots,\alpha_{n-1}), X),
\end{eqnarray*}
$$



</div>

<h3>Compositum of subfields and lifting</h3>

<div class="definition" id="definition:compositum---of---subfields" data-name="compositum of subfields">
	


for field $k$ and its extension fields $E$ and $F$, which are subfields of common field $L$,
smallest subfield of $L$ containing both $E$ and $F$,
called <span class="define">compositum of $E$ and $F$ in $L$</span>,
denoted by <span class="notation">$EF$</span>

	<ul>
	<li>
		
cannot define compositum if $E$ and $F$ are not embedded in common field $L$

	</li>
	</ul>

</div>
<ul>
<li>
	could define <span class="define">compositum of set of subfields of $L$</span>
as smallest subfield containing subfields in the set

</li>
</ul>

<div class="lemma" id="lemma:">
	
extension $E$ of $k$ is
compositum of all its finitely generated subfields over $k$,
<i>i.e.</i>,
$E =
\bigcup_{n\in\naturals}
\bigcup_{\alpha_1, \ldots, \alpha_n \in E}
k(\alpha_1,\ldots,\alpha_n)$

</div>


<h3>Lifting</h3>

<div class="definition" id="definition:lifting" data-name="lifting">
	




extension $EF$ of $F$,
called <span class="define">translation of $E$ to $F$</span> or <span class="define">lifting of $E$ to $F$</span>

	<ul>
	<li>
		often draw diagram as in the figure

	</li>
	</ul>

</div>





<div id="fig:translation---or---lifting---of---fields"></div>


<h3>Finite generation of compositum</h3>

<div class="lemma" id="lemma:finite---generation---of---compositum" data-name="finite generation of compositum">
	


for field $k$,
its extension field $F$,
and
$E = k(\alpha_1,\ldots,\alpha_n)$
where both $E$ and $F$ are contained in common field $L$,

$$
EF = F(\alpha_1, \ldots, \alpha_n)
$$

<i>i.e.</i>,
compositum $EF$ is finitely generated over $F$ 

	<ul>
	<li>
		refer to diagra in the figure

	</li>
	</ul>

</div>





<div id="fig:lifting---of---smallest---fields"></div>


<h3>Distinguished classes</h3>

<div class="definition" id="definition:distinguished---class---of---field---extensions" data-name="distinguished class of field extensions">
	


for field $k$,
class $\classk{C}$ of extension fields satisfying

	<ul>
	<li>
		for tower of fields $k\subset F\subset E$,
extension $k\subset E$ is in $\classk{C}$
if and only if
both $k\subset F$ and $F\subset E$ are in $\classk{C}$

	</li>
	<li>
		if $k\subset E$ is in $\classk{C}$, $F$ is any extension of $k$,
and both $E$ and $F$ are subfields of common field,
then $F\subset EF$ is in $\classk{C}$

	</li>
	</ul>


said to be <span class="define">distinguished</span>;
the figure illustrates these two properties,
which imply the following property

	<ul>
	<li>
		if $k\subset F$ and $k\subset E$ are in $\classk{C}$
and both $E$ and $F$ are subfields of common field,
$k\subset EF$ is in $\classk{C}$

	</li>
	</ul>

</div>



&nbsp;


<div id="fig:lattice---diagram---of---fields"></div>



<h3>Both algebraic and finite extensions are distinguished</h3>

<div class="proposition" id="proposition:algebraic---and---finite---extensions---are---distinguished" data-name="algebraic and finite extensions are distinguished">
	


class of algebraic extensions is distinguished,
so is class of finite extensions

</div>
<ul>
<li>
	true that finitely generated extensions form distinguished class (not necessarily algebraic extensions or finite extensions)

</li>
</ul>

<h3>Field embedding and embedding extension</h3>

<div class="definition" id="definition:field---embedding" data-name="field embedding">
	


for two fields $F$ and $L$,
injective homeomorphism $\sigma:F\to L$,
called <span class="define">embedding of $F$ into $L$</span>;
then (of course) $\sigma$ induces isomorphism of $F$ with its image $\sigma F$&nbsp;(footnote &ndash; 
Here $\sigma F$ is sometimes written as $F^\sigma$.)

</div>
<div class="definition" id="definition:field---embedding---extension" data-name="field embedding extension">
	


for field embedding $\sigma:F\to L$,
field extension $F\subset E$,
and
embedding $\tau:E\to L$
whose restriction to $F$ being equal to $\sigma$,
said to <span class="define">be over $\sigma$</span> or <span class="define">extend $\sigma$;</span>
if $\sigma$ is identity,
embedding $\tau$, called <span class="define">embedding of $E$ over $F$</span>;
diagrams in the figure show these embedding extensions

</div>




&nbsp;



<div id="fig:field---embedding---extensions"></div>


<ul>
<li>
	assuming $F$, $E$, $\sigma$, and $\tau$ same as in <a href="#definition:field---embedding---extension"></a>,
if $\alpha\in E$ is root of $f\in F[X]$, then $\alpha^\tau$ is root of $f^\sigma$
for
if $f(X) = \sum_{i=0}^n a_i X^i$, then $f(\alpha) = \sum_{i=0}^n a_i \alpha^i = 0$,
and
$0
= f(\alpha)^\tau
= \sum_{i=0}^n (a_i^\tau ) (\alpha^\tau)^i
= \sum_{i=0}^n a_i^\sigma (\alpha^\tau)^i
= f^\sigma(\alpha^\tau)$

</li>
</ul>

<h3>Embedding of field extensions</h3>

<div class="lemma" id="lemma:field---embedding---of---algebraic---extension" data-name="field embedding of algebraic extension">
	


for field $k$ and its algebraic extension $E$,
embedding of $E$ into itself over $k$
is isomorphism


</div>

<div class="lemma" id="lemma:compositums---of---fields" data-name="compositums of fields">
	


for field $k$ and its field extensions $E$ and $F$ contained in common field,

$$
E[F] = F[E] = \bigcup_{n=1}^\infty \bigset{e_1f_1 + \cdots + e_nf_n}{e_i\in E, f_i\in F}
$$

and
$EF$ is field of quotients of these elements

</div>

<div class="lemma" id="lemma:embeddings---of---compositum---of---fields" data-name="embeddings of compositum of fields">
	


for
field $k$,
its field extensions $E_1$ and $E_2$ contained in commen field $E$,
and
embedding $\sigma:E\to L$ for field $L$,

$$
\sigma(E_1 E_2) = \sigma(E_1) \sigma(E_2)
$$


</div>


<h3>Existence of roots of irreducible polynomial</h3>


<ul>
<li>
	assume $p(X) \in k[X]$ irreducible polynomial and consider canonical map, which is ring homeomorphism

$$
\sigma: k[X] \to k[X] / ((p(X))
$$


</li>
<li>
	consider $\Ker \restrict{\sigma}{k}$
	<ul>
	<li>
		every kernel of ring homeomorphism is ideal,
hence if nonzero $a \in \Ker \restrict{\sigma}{k}$, $1\in \Ker \restrict{\sigma}{k}$
because $a^{-1} \in \Ker \restrict{\sigma}{k}$,
but $1\not\in (p(X))$

	</li>
	<li>
		thus, $\Ker \restrict{\sigma}{k} = \{0\}$,
hence $p^\sigma\neq0$

	</li>
	</ul>

</li>
<li>
	now for $\alpha = X^\sigma$

$$
p^\sigma(\alpha)
= p^\sigma(X^\sigma) = (p(X))^\sigma = 0
$$


</li>
<li>
	thus, $\alpha$ is algebraic in $k^\sigma$,
<i>i.e.</i>,
$\alpha \in k[X]^\sigma$ is root of $p^\sigma$ in $k^\sigma(\alpha)$

</li>
</ul>
<div class="lemma" id="lemma:existence---of---roots---of---irreducible---polynomial" data-name="existence of roots of irreducible polynomial">
	

for field $k$ and irreducible $p(X)\in k[X]$ with $\deg p \geq 1$,
exist field $L$ and homeomorphism $\sigma:k \to L$
such that $p^\sigma$ with $\deg p^\sigma \geq 1$ has root
in field extension of $k^\sigma$

</div>


<h3>Existence of algebraically closed algebraic field extensions</h3>



<div class="proposition" id="proposition:existence---of---extension---fields---containing---roots" data-name="existence of extension fields containing roots">
	

for field $k$ and $f\in k[X]$ with $\deg f \geq 1$,
exists extension of $k$ in which $f$ has root

</div>

<div class="corollary" id="corollary:existence---of---extension---fields---containing---roots" data-name="existence of extension fields containing roots">
	

for field $k$ and $f_1$, &hellip;, $f_n$ $\in$ $k[X]$ with $\deg f_i \geq 1$,
exists extension of $k$ in which every $f_i$ has root

</div>

<div class="theorem" id="theorem:existence---of---algebraically---closed---field---extensions" data-name="existence of algebraically closed field extensions">
	

for every field $k$,
exists algebraically closed extension of $k$

</div>

<div class="corollary" id="corollary:existence---of---algebraically---closed---algebraic---field---extensions" data-name="existence of algebraically closed algebraic field extensions">
	


for every field $k$,
exists algebraically closed algebraic extension of $k$


</div>

<h3>Isomorphism between algebraically closed algebraic extensions</h3>

<div class="proposition" id="proposition:number---of---algebraic---embedding---extensions" data-name="number of algebraic embedding extensions">
	


for field, $k$,
$\alpha$ being algebraic over $k$,
algebraically closed field, $L$,
and
embedding, $\sigma:k\to L$,
# possible embedding extensions of $\sigma$ to $k(\alpha)$ in $L$
is
equal to # distinct roots of $\Irr(\alpha,k,X)$,
hence
no greater than # roots of $\Irr(\alpha,k,X)$

</div>
<div class="theorem" id="theorem:algebraic---embedding---extensions" data-name="algebraic embedding extensions">
	


for field, $k$,
its algebraic extensions, $E$,
algebraically closed field, $L$,
and
embedding, $\sigma:k\to L$,
exists embedding extension of $\sigma$ to $E$ in $L$;
if $E$ is algebraically closed and $L$ is algebraic over $k^\sigma$,
every such embedding extension is isomorphism of $E$ onto $L$

</div>
<div class="corollary" id="corollary:isomorphism---between---algebraically---closed---algebraic---extensions" data-name="isomorphism between algebraically closed algebraic extensions">
	


for field, $k$,
and
its algebraically closed algebraic extensions, $E$ and $E'$,
exists isomorphism bewteen $E$ and $E'$ which induces identity on $k$,
<i>i.e.</i>

$$
\tau: E \to E'
$$



where $\restrict{\tau}{k}$ is identity

</div>
<ul>
<li>
	thus, <span class="eemph">algebraically closed algebraic extension is determined up to isomorphism</span>


</li>
</ul>

<h3>Algebraic closure</h3>

<div class="definition" id="definition:algebraic---closure" data-name="algebraic closure">
	


for field, $k$,
algebraically closed algebraic extension of $k$, which is determined up to isomorphism,
called <span class="define">algebraic closure of $k$</span>,
frequently denoted by <span class="notation">\algclosure{k}</span>

</div>
<ul>
<li>
	examples
	<ul>
	<li>
		complex conjugation is automorphism of $\complexes$
(which is the only continuous automorphism of $\complexes$)

	</li>
	<li>
		subfield of $\complexes$ consisting of all numbers which are algebraic over $\rationals$
is algebraic closure of $\rationals$, <i>i.e.</i>, $\algclosure{\rationals}$

	</li>
	<li>
		$\algclosure{\rationals} \neq \complexes$

	</li>
	<li>
		$\algclosure{\reals} = \complexes$

	</li>
	<li>
		<i>\algclosure{\rationals}\ is countable</i>

	</li>
	</ul>

</li>
</ul>

<div class="theorem" id="theorem:countability---of---algebraic---closure---of---finite---fields" data-name="countability of algebraic closure of finite fields">
	


algebraic closure of finite field is countable

</div>

<div class="theorem" id="theorem:cardinality---of---algebraic---extensions---of---infinite---fields" data-name="cardinality of algebraic extensions of infinite fields">
	


for infinite field, $k$,
every algebraic extension of $k$
has same cardinality as $k$

</div>

<h3>Splitting fields</h3>



<div class="definition" id="definition:splitting---fields" data-name="splitting fields">
	
for field, $k$, and $f\in k[X]$ with $\deg f \geq 1$,
field extension, $K$, of $k$,
$f$ splits into linear factors in which,
<i>i.e.</i>,

$$
f(X) = c (X-\alpha_1) \cdots (X-\alpha_n)
$$

and which is finitely generated over $k$ by $\alpha_1$, &hellip;, $\alpha_n$
(hence $K=k(\alpha_1, \ldots, \alpha_n)$),
called <span class="define">splitting field of $f$</span>

</div>
<ul>
<li>
	for field, $k$,
every $f\in k[X]$
has splitting field
in $\algclosure{k}$

</li>
</ul>
<div class="theorem" id="theorem:isomorphism---between---splitting---fields" data-name="isomorphism between splitting fields">
	


for field, $k$, $f\in k[X]$ with $\deg f \geq1$,
and two splitting fields of $f$, $K$ and $E$,
exists isomorphism between $K$ and $E$;
if $k\subset K\subset \algclosure{k}$,
every embedding of $E$ into $\algclosure{k}$
over $k$
is isomorphism of $E$ onto $K$

</div>

<h3>Splitting fields for family of polynomials</h3>

<div class="definition" id="definition:splitting---fields---for---family---of---polynomials" data-name="splitting fields for family of polynomials">
	
for field, $k$,
index set, $\Lambda$,
and indexed family of polynomials,
$\set{f_\lambda\in k[X]}{\lambda \in \Lambda, \deg f_\lambda \geq1}$,
extension field of $k$,
every $f_\lambda$ splits into linear factors in which
and
which is generated by all roots of all polynomials, $f_\lambda$,
called <span class="define">splitting field for family of polynomials</span>

</div>
<ul>
<li>
	in most applications, deal with finite $\Lambda$

</li>
<li>
	becoming increasingly important to consider infinite algebraic extensions

</li>
<li>
	various proofs would not be simpler if restricted ourselves to finite cases

</li>
</ul>
<div class="corollary" id="corollary:isomorphism---between---splitting---fields---for---family---of---polynomials" data-name="isomorphism between splitting fields for family of polynomials">
	
for field, $k$,
index set, $\Lambda$,
and two splitting fields, $K$ and $E$, for family of polynomials,
$\set{f_\lambda\in k[X]}{\lambda \in \Lambda, \deg f_\lambda \geq1}$,
every embedding of $E$ into $\algclosure{K}$
over $k$
is isomorphism of $E$ onto $K$

</div>

<h3>Normal extensions</h3>

<div class="theorem" id="theorem:normal---extensions" data-name="normal extensions">
	
for field, $k$,
and its algebraic extension, $K$,
with $k\subset K\subset \algclosure{k}$,
following statements are equivalent

	<ul>
	<li>
		every embedding of $K$ into $\algclosure{k}$ over $k$ induces automorphism

	</li>
	<li>
		$K$ is splitting field of family of polynomials in $k[X]$

	</li>
	<li>
		every irreducible polynomial of $k[X]$ which has root in $K$
splits into linear factors in $K$

	</li>
	</ul>

</div>
<div class="definition" id="definition:normal---extensions" data-name="normal extensions">
	
for field, $k$,
and its algebraic extension, $K$,
with $k\subset K\subset \algclosure{k}$,
satisfying properties in <a href="#theorem:normal---extensions"></a>,
said to be <span class="define">normal</span>

</div>
<ul>
<li>
	<i>not</i> true that class of normal extensions is <i>distinguished</i>
	<ul>
	<li>
		<i>e.g.</i>, below tower of fields is tower of normal extensions

$$
\rationals
\subset
\rationals(\sqrt{2})
\subset
\rationals(\sqrt[4]{2})
$$


	</li>
	<li>
		but, extension $\rationals \subset \rationals(\sqrt[4]{2})$ is not normal
because complex roots of $X^4-2$ are not in $\rationals(\sqrt[4]{2})$

	</li>
	</ul>

</li>
</ul>

<h3>Retention of normality of extensions</h3>

<div class="theorem" id="theorem:retention---of---normality---of---extensions" data-name="retention of normality of extensions">
	
normal extensions remain normal under lifting;
if $k\subset E\subset K$ and $K$ is normal over $k$,
$K$ is normal over $E$;
if $K_1$ and $K_2$ are normal over $k$ and are contained in common field,
$K_1K_2$ is normal over $k$,
and so is $K_1\cap K_2$

</div>

<h3>Separable degree of field extensions</h3>

<ul>
<li>
	for field, $F$, and its algebraic extension, $E$
	<ul>
	<li>
		let $L$ be algebraically closed field and assume embedding, $\sigma:F\to L$
		<ul>
		<li>
			exists embedding extension of $\sigma$ to $E$ in $L$
by <a href="#theorem:algebraic---embedding---extensions"></a>

		</li>
		<li>
			such $\sigma$ maps $E$ on subfield of $L$ which is algebraic over $F^\sigma$

		</li>
		<li>
			hence, $E^\sigma$ is contained in algebraic closure of $F^\sigma$ which is contained in $L$

		</li>
		<li>
			will <i>assume</i> that $L$ is the algebraic closure of $F^\sigma$

		</li>
		</ul>

	</li>
	<li>
		let $L'$ be another algebraically closed field and assume another embedding, $\tau:F\to L'$
- assume as before that $L'$ is algebraic closure of $F^\tau$

	</li>
	<li>
		then <a href="#theorem:algebraic---embedding---extensions"></a>
implies, exists isomorphism, $\lambda:L\to L'$
extending $\tau\circ \sigma^{-1}$ applied to $F^\sigma$

	</li>
	<li>
		let
$S_\sigma$ &amp; $S_\tau$ be sets of embedding extensions of $\sigma$ to $E$ in $L$ and $L'$
respectively

	</li>
	<li>
		then $\lambda$ induces map from $S_\sigma$ into $S_\tau$ with $\tilde{\sigma} \mapsto \lambda \circ \tilde{\sigma}$
and $\lambda^{-1}$ induces inverse map from $S_\tau$ into $S_\sigma$,
hence exists bijection between $S_\sigma$ and $S_\tau$, hence have same cardinality

	</li>
	</ul>

</li>
</ul>
<div class="definition" id="definition:separable---degree---of---field---extensions" data-name="separable degree of field extensions">
	
above cardinality only depends on extension $E/F$,
called <span class="define">separable degree of $E$ over $F$</span>,
denoted by <span class="notation">$[E:F]_s$</span>

</div>

<h3>Multiplicativity of and upper bound on separable degree of field extensions</h3>

<div class="theorem" id="theorem:multiplicativity---of---separable---degree---of---field---extensions" data-name="multiplicativity of separable degree of field extensions">
	
for tower of algebraic field extensions, $k\subset F\subset E$,

$$
[E:k]_s
=
[E:F]_s
[F:k]_s
$$


</div>
<div class="theorem" id="theorem:upper---limit---on---separable---degree---of---field---extensions" data-name="upper limit on separable degree of field extensions">
	
for finite algebraic field extension, $k\subset E$

$$
[E:k]_s \leq [E:k]
$$


</div>
<ul>
<li>
	<i>i.e.</i>, separable degree is at most equal to degree (<i>i.e.</i>, dimension) of field extension

</li>
</ul>
<div class="corollary" id="corollary:">
	
for tower of algebraic field extensions, $k\subset F\subset E$,
with $[E:k]<\infty$

$$
[E:k]_s = [E:k]
$$

holds
if and only if
corresponding equality holds in every step of tower,
<i>i.e.</i>, for $E/F$ and $F/k$

</div>

<h3>Finite separable field extensions</h3>

<div class="definition" id="definition:finite---separable---field---extensions" data-name="finite separable field extensions">
	
for finite algebraic field extension, $E/k$,
with $[E:k]_s=[E:k]$,
$E$,
said to be <span class="define">separable over $k$</span>

</div>
<div class="definition" id="definition:separable---algebraic---elements" data-name="separable algebraic elements">
	
for field, $k$,
$\alpha$, which is algebraic over $k$
with $k(\alpha)$ being separable over $k$,
said to be <span class="define">separable over $k$</span>

</div>
<div class="proposition" id="proposition:separability---and---multiple---roots" data-name="separability and multiple roots">
	
for field, $k$,
$\alpha$, which is algebraic over $k$,
is separable over $k$
if and only if
$\Irr(\alpha,k,X)$
has no multiple roots

</div>
<div class="definition" id="definition:separable---polynomials" data-name="separable polynomials">
	
for field, $k$,
$f\in k[X]$ with no multiple roots,
said to be <span class="define">separable</span>

</div>
<div class="lemma" id="lemma:">
	
for tower of algebraic field extensions,
$k\subset F\subset K$,
if $\alpha \in K$ is separable over $k$,
then $\alpha$ is separable over $F$

</div>
<div class="theorem" id="theorem:finite---separable---field---extensions" data-name="finite separable field extensions">
	
for finite field extension, $E/k$,
$E$ is separable over $k$
if and only if
every element of $E$ is separable over $k$

</div>

<h3>Arbitrary separable field extensions</h3>

<div class="definition" id="definition:arbitrary---separable---field---extensions" data-name="arbitrary separable field extensions">
	
for (not necessarily finite) field extension, $E/k$,
$E$,
of which
every finitely generated subextension
is separable over $k$,
<i>i.e.</i>,

$$
\left(
\forall n\in\naturals\ \& \ \alpha_1,\ldots, \alpha_n \in E
\right)
\left(
k(\alpha_1, \ldots, \alpha_n)
\mbox{ is separable over }
k
\right)
$$

said to be <span class="define">separable over $k$</span>

</div>
<div class="theorem" id="theorem:separable---field---extensions" data-name="separable field extensions">
	
for algebraic extension, $E/k$,
$E$, which is generated by family of elements, $\{\alpha_\lambda\}_{\lambda\in\Lambda}$,
with every $\alpha_\lambda$ is separable over $k$,
is separable over $k$

</div>
<div class="theorem" id="theorem:separable---extensions---are---distinguished" data-name="separable extensions are distinguished">
	
separable extensions form distinguished class of extensions

</div>

<h3>Separable closure and conjugates</h3>

<div class="definition" id="definition:separable---closure" data-name="separable closure">
	
for field, $k$,
compositum of all separable extensions of $k$ in given algebraic closure $\algclosure{k}$,
called <span class="define">separable closure of $k$</span>,
denoted by <span class="notation">$k^\mathrm{s}$ or \sepclosure{k}</span>

</div>
<div class="definition" id="definition:conjugates---of---fields" data-name="conjugates of fields">
	
for algebraic field extension, $E/k$,
and embedding of $E$, $\sigma$, in $\algclosure{k}$ over $k$,
$E^\sigma$,
called <span class="define">conjugate of $E$ in \algclosure{k}</span>

</div>
<ul>
<li>
	smallest normal extension of $k$ containing $E$
is compositum of all conjugates of $E$ in $\algclosure{E}$

</li>
</ul>
<div class="definition" id="definition:conjugates---of---elements---of---fields" data-name="conjugates of elements of fields">
	
for field, $k$,
$\alpha$ being algebraic over $k$,
and
distinct embeddings, $\sigma_1$, &hellip;, $\sigma_r$ of $k(\alpha)$ into $\algclosure{k}$ over $k$,
$\alpha^{\sigma_1}$,
&hellip;,
$\alpha^{\sigma_r}$,
called <span class="define">conjugates of $\alpha$ in \algclosure{k}</span>

</div>
<ul>
<li>
	$\alpha^{\sigma_1}$,
&hellip;,
$\alpha^{\sigma_r}$
are simply
distinct roots of $\Irr(\alpha, k, X)$

</li>
<li>
	smallest normal extension of $k$
containing one of these conjugates
is simply
$k(\alpha^{\sigma_1}, \ldots, \alpha^{\sigma_r})$

</li>
</ul>

<h3>Prime element theorem</h3>

<div class="theorem" id="theorem:prime---element---theorem" data-name="prime element theorem">
	
for finite algebraic field extension, $E/k$,
exists $\alpha\in E$ such that $E=k(\alpha)$
if and only if
exists only finite # fields, $F$, such that $k\subset F\subset E$;
if $E$ is separable over $k$,
exists such element, $\alpha$

</div>
<div class="definition" id="definition:primitive---element---of---fields" data-name="primitive element of fields">
	
for finite algebraic field extension, $E/k$,
$\alpha\in E$ with $E=k(\alpha)$,
called <span class="define">primitive element of $E$ over $k$</span>

</div>

<h3>Finite fields</h3>

<div class="definition" id="definition:finite---fields" data-name="finite fields">
	
for every prime number, $p$, and integer, $n\geq1$,
exists finite field of order $p^n$,
denoted by <span class="notation">\finitefield{p}{n}</span>,
uniquely determined as subfield of algebraic closure, $\algclosure{\primefield{p}}$,
which is splitting field of polynomial

$$
f_{p,n}(X) = X^{p^n} - X
$$

and whose elements are roots of $f_{p,n}$

</div>
<div class="theorem" id="theorem:finite---fields" data-name="finite fields">
	
for every finite field, $F$,
exist prime number, $p$, and integer, $n\geq1$,
such that $F=\finitefield{p}{n}$

</div>
<div class="corollary" id="corollary:finite---field---extensions" data-name="finite field extensions">
	
for finite field, , and integer, $m\geq1$,
exists one and only one extension of degree, $m$,
which is 

</div>
<div class="theorem" id="theorem:multiplicative---group---of---finite---field" data-name="multiplicative group of finite field">
	
multiplicative group of finite field is cyclic

</div>

<h3>Automorphisms of finite fields</h3>

<div class="definition" id="definition:Frobenius---mapping" data-name="Frobenius mapping">
	
mapping

$$
\frobmap{p}{n}: \finitefield{p}{n} \to \finitefield{p}{n}
$$

defined by $x\mapsto x^p$,
called <span class="define">Frobenius mapping</span>

</div>
<ul>
<li>
	 is (ring) homeomorphism
with $\Ker \frobmap{p}{n} = \{0\}$ since  is field,
thus is injective (<a href="#proposition:injectivity---of---field---homeomorphism"></a>),
and surjective because  is finite,

</li>
<li>
	thus,  is <i>isomorphism
leaving \primefield{p}\ fixed</i>

</li>
</ul>
<div class="theorem" id="theorem:group---of---automorphisms---of---finite---fields" data-name="group of automorphisms of finite fields">
	
group of automorphisms of 
is cyclic of degree $n$,
generated by 

</div>
<div class="theorem" id="theorem:group---of---automorphisms---of---finite---fields---over---another---finite---field" data-name="group of automorphisms of finite fields over another finite field">
	
for prime number, $p$, and integers, $m,n\geq1$,
in any $\algclosure{\primefield{p}}$,
 is contained in 
if and only if
$n$ divides $m$,
<i>i.e.</i>, exists $d\in\integers$ such that $m=dn$,
in which case,
 is <i>normal and separable</i> over 
group of automorphisms of  over 
is cyclic of order, $d$,
generated by $\frobmap{p}{m}^n$

</div>

<h2 id="title-page:Galois---Theory">Galois Theory</h2>



<h3>What we will do to appreciate Galois theory</h3>



<ul>
<li>
	study
	<ul>
	<li>
		group of automorphisms of finite (and infinite) Galois extension (at length)

	</li>
	<li>
		give examples, <i>e.g.</i>, cyclotomic extensions, abelian extensions, (even) non-abelian ones

	</li>
	<li>
		leading into study of matrix representation of Galois group &amp; classifications

	</li>
	</ul>

</li>
<li>
	have
tools to prove
	<ul>
	<li>
		fundamental theorem of algebra

	</li>
	<li>
		insolvability of quintic polynomials

	</li>
	</ul>

</li>
<li>
	mention unsolved problems
	<ul>
	<li>
		given finite group, exists Galois extension of $\rationals$ having this group as Galois group?

	</li>
	</ul>

</li>
</ul>

<h3>Fixed fields</h3>

<div class="definition" id="definition:fixed---field" data-name="fixed field">
	

for field, $K$, and group of automorphisms, $G$, of $K$,

$$
\set{x\in K}{\forall \sigma\in G, x^\sigma = x}\subset K
$$

is subfield of $K$, and
called <span class="define">fixed field of $G$</span>,
denoted by <span class="notation">$K^G$</span>

</div>
<ul>
<li>
	$K^G$ is subfield of $K$ because for every $x,y\in K^G$
	<ul>
	<li>
		$0^\sigma = 0 \Rightarrow 0\in K^G$

	</li>
	<li>
		$(x+y)^\sigma = x^\sigma + y^\sigma = x + y \Rightarrow x+y \in K^G$

	</li>
	<li>
		$(-x)^\sigma = - x^\sigma = - x \Rightarrow -x \in K^G$

	</li>
	<li>
		$1^\sigma = 1 \Rightarrow 1\in K^G$

	</li>
	<li>
		$(xy)^\sigma = x^\sigma y^\sigma = xy \Rightarrow xy\in K^G$

	</li>
	<li>
		$(x^{-1})^\sigma = (x^\sigma)^{-1} = x^{-1} \Rightarrow x^{-1} \in K^G$

	</li>
	</ul>
hence, $K^G$ closed under addition &amp; multiplication,
and is commutative division ring,
thus field

</li>
<li>
	$0,1\in K^G$, hence <i>$K^G$ contains prime field</i>

</li>
</ul>

<h3>Galois extensions and Galois groups</h3>

<div class="definition" id="definition:Galois---extensions" data-name="Galois extensions">
	



algebraic extension, $K$, of field, $k$,
which is normal and separable,
said to be <span class="define">Galois (extension of $k$)</span>
or <span class="define">Galois over $k$</span>
considering $K$ as embedded in $\algclosure{k}$;
for convenience,
sometimes say <span class="define">$K/k$ is Galois</span>

</div>
<div class="definition" id="definition:Galois---groups" data-name="Galois groups">
	


for field, $k$ and its Galois extension, $K$,
group of automorphisms of $K$ over $k$,
called <span class="define">Galois group of $K$ over $k$</span>,
denoted by <span class="notation">$G(K/k)$, $G_{K/k}$, $\Gal(K/k)$, or (simply) $G$</span>





</div>
<div class="definition" id="definition:Galois---group---of---polynomials" data-name="Galois group of polynomials">
	
for field, $k$, separable $f\in k[X]$ with $\deg f \geq 1$,
and
its splitting field, $K/k$,
Galois group of $K$ over $k$ (<i>i.e.</i>, $G(K/k)$),
called <span class="define">Galois group of $f$ over $k$</span>

</div>
<div class="proposition" id="proposition:Galois---group---of---polynomials---and---symmetric---group" data-name="Galois group of polynomials and symmetric group">
	
for field, $k$, separable $f\in k[X]$ with $\deg f \geq 1$,
and
its splitting field, $K/k$,

$$
f(X) = (X-\alpha_1) \cdots (X-\alpha_n)
$$

elements of Galois group of $f$ over $k$, $G$,
permute roots of $f$,
hence, exists injective homeomorphism
of $G$ into $S_n$, <i>i.e.</i>, symmetric group on $n$ elements

</div>

<h3>Fundamental theorem for Galois theory</h3>

<div class="theorem" id="theorem:fundamental---theorem---for---Galois---theory" data-name="fundamental theorem for Galois theory">
	




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

(illustrated in the figure)

</div>

<ul>
<li>
	shall prove step by step

</li>
</ul>










<div id="fig:diagrams---for---Galois---main---result"></div>




<h3>Galois subgroups association with intermediate fields</h3>

<div class="theorem" id="theorem:Galois---subgroups---associated---with---intermediate---fields-------1" data-name="Galois subgroups associated with intermediate fields - 1">
	
for Galois extension, $K/k$,
and intermediate field, $F$

	<ul>
	<li>
		$K/F$ is Galois &amp; $K^{G(K/F)} = F$, hence, $K^G = k$

	</li>
	<li>
		map

$$
F \mapsto G(K/F)
$$

induces <i>injective</i> homeomorphism
from set of intermediate fields
to subgroups of $G$

	</li>
	</ul>



</div>
<div class="definition" id="definition:Galois---subgroups---associated---with---intermediate---fields" data-name="Galois subgroups associated with intermediate fields">
	
for Galois extension, $K/k$, and intermediate field, $F$,
subgroup, $G(K/F)\subset G(K/k)$,
called <span class="define">group associated with $F$</span>,
said to <span class="define">belong to $F$</span>

</div>
<div class="corollary" id="corollary:Galois---subgroups---associated---with---intermediate---fields-------1" data-name="Galois subgroups associated with intermediate fields - 1">
	
for Galois extension, $K/k$,
and
two intermediate fields, $F_1$ and $F_2$,
$G(K/F_1) \cap G(K/F_2)$ belongs to $F_1F_2$,
<i>i.e.</i>,

$$
G(K/F_1) \cap G(K/F_2)
= G(K/F_1F_2)
$$



</div>
<div class="corollary" id="corollary:Galois---subgroups---associated---with---intermediate---fields-------2" data-name="Galois subgroups associated with intermediate fields - 2">
	
for Galois extension, $K/k$,
and
two intermediate fields, $F_1$ and $F_2$,
smallest subgroup of $G$ containing $G(K/F_1)$ and $G(K/F_2)$
belongs to
$F_1\cap F_2$,
<i>i.e.</i>

$$
\bigcap_{G(K/F_1)\subset H, G(K/F_2)\subset H} \set{H}{H\subset G(K/k)}
=
G(K/(F_1\cap F_2))
$$


</div>
<div class="corollary" id="corollary:Galois---subgroups---associated---with---intermediate---fields-------3" data-name="Galois subgroups associated with intermediate fields - 3">
	
for Galois extension, $K/k$,
and
two intermediate fields, $F_1$ and $F_2$,

$$
F_1\subset F_2
\mbox{ \iaoi\ }
G(K/F_2)\subset G(K/F_1)
$$



</div>
<div class="corollary" id="corollary:">
	
for finite separable field extension, $E/k$,
the smallest normal extension of $k$ containing $E$, $K$,
$K/k$ is finite Galois
and exist only finite number of intermediate fields

</div>
<div class="lemma" id="lemma:">
	
for algebraic separable extension, $E/k$,
if every element of $E$ has degree no greater than $n$ over $k$
for some $n\geq1$,
$E$ is finite over $k$ and $[E:k]\leq n$

</div>
<div class="theorem" id="theorem:Artin's---theorem" data-name="Artin's theorem">
	
<div id="theorem:Artins---theorem"></div>
(Artin)
for field, $K$,
finite $\Aut(K)$ of order, $n$,
and $k = K^{\Aut(K)}$,
$K/k$ is Galois,
$G(K/k)= \Aut(K)$,
and $[K:k] = n$

</div>
<div class="corollary" id="corollary:Galois---subgroups---associated---with---intermediate---fields-------4" data-name="Galois subgroups associated with intermediate fields - 4">
	
for finite Galois extension, $K/k$,
every subgroup of $G(K/k)$ belongs to intermediate field

</div>
<div class="theorem" id="theorem:Galois---subgroups---associated---with---intermediate---fields-------2" data-name="Galois subgroups associated with intermediate fields - 2">
	
for Galois extension, $K/k$,
and intermediate field, $F$,

	<ul>
	<li>
		$F/k$ is normal extension
if and only if
$G(K/F)$ is normal subgroup of $G(K/k)$

	</li>
	<li>
		if $F/k$ is normal extension,
map, $\sigma \mapsto \restrict{\sigma}{F}$,
induces
homeomorphism
of $G(K/k)$ onto $G(F/k)$
of which $G(K/F)$ is kernel,
thus

$$
G(F/k) \isomorph G(K/k)/G(K/F)
$$


	</li>
	</ul>

</div>

<h3>Proof for fundamental theorem for Galois theory</h3>

<ul>
<li>
	finally, we prove <i>fundamental theorem for Galois theory</i>
(<a href="#theorem:fundamental---theorem---for---Galois---theory"></a>)

</li>
<li>
	assume $K/k$ is finite Galois extension
and $H$ is subgroup of $G(K/k)$
	<ul>
	<li>
		<a href="#corollary:Galois---subgroups---associated---with---intermediate---fields-------4"></a>
implies $K^H$ is intermediate field,
hence
<a href="#theorem:Galois---subgroups---associated---with---intermediate---fields-------1"></a>
implies
$K/K^H$ is Galois,
<a href="#theorem:Artins---theorem"></a>
implies
$G(K/K^H) = H$,
thus,
every $H$ is Galois

	</li>
	<li>
		map, $H\mapsto K^H$,
induces homeomorphism, $\sigma$, of set of all subgroups of $G(K/k)$
into set of intermediate fields

	</li>
	<li>
		$\sigma$ is <i>injective</i>
since
for any two subgroups, $H$ and $H'$, of $G(K/k)$,
if $K^H=K^{H'}$,
then $H=G(K/K^H)=G(K/K^{H'})=H'$

	</li>
	<li>
		$\sigma$ is <i>surjective</i>
since
for every intermediate field, $F$,
<a href="#theorem:Galois---subgroups---associated---with---intermediate---fields-------1"></a>
implies
$K/F$ is Galois, $G(K/F)$ is subgroup of $G(K/k)$, and $K^{G(K/F)}=F$,
thus,
$\sigma(G(K/F)) = K^{G(K/F)}= F$

	</li>
	<li>
		<i>therefore, $\sigma$ is isomorphism
between
set of all subgroups of $G(K/k)$
and
set of intermediate fields
</i>

	</li>
	<li>
		since <a href="#theorem:separable---extensions---are---distinguished"></a>
implies
separable extensions are distinguished,
$H^K/k$ is separable,
thus
<a href="#theorem:Galois---subgroups---associated---with---intermediate---fields-------2"></a>
implies that $K^H/k$ is Galois if and only if $G(K/K^H)$ is normal

	</li>
	<li>
		lastly,
<a href="#theorem:Galois---subgroups---associated---with---intermediate---fields-------2"></a>
implies that if $K^H/k$ is Galois,
$G(H^K/k) \isomorph G(K/k) / H$

	</li>
	</ul>

</li>
</ul>

<h3>Abelian and cyclic Galois extensions and groups</h3>

<div class="definition" id="definition:abelian---Galois---extensions" data-name="abelian Galois extensions">
	
Galois extension with abelian Galois group,
said to be <span class="define">abelian</span>

</div>
<div class="definition" id="definition:cyclic---Galois---extensions" data-name="cyclic Galois extensions">
	
Galois extension with cyclic Galois group,
said to be <span class="define">cyclic</span>

</div>
<div class="corollary" id="corollary:">
	
for Galois extension, $K/k$,
and
intermediate field, $F$,

	<ul>
	<li>
		if $K/k$ is abelian, $F/k$ is Galois and abelian

	</li>
	<li>
		if $K/k$ is cyclic, $F/k$ is Galois and cyclic

	</li>
	</ul>

</div>
<div class="definition" id="definition:maximum---abelian---extension" data-name="maximum abelian extension">
	
for field, $k$,
compositum of all abelian Galois extensions of $k$
in given $\algclosure{k}$,
called <span class="define">maximum abelian extension of $k$</span>,
denoted by <span class="notation">\maxabext{k}</span>

</div>

<h3>Theorems and corollaries about Galois extensions</h3>

<div class="theorem" id="theorem:">
	
for Galois extension, $K/k$,
and arbitrary extension, $F/k$,
where $K$ and $F$ are subfields of common field,

	<ul>
	<li>
		$KF / F$ and $K/(K\cap F)$ are Galois extensions

	</li>
	<li>
		map 
$$
\sigma \mapsto \sigma|K
$$

induces
isomorphism
between
$G(KF / F)$ and $G(K/(K\cap F))$

	</li>
	</ul>

theorem illustrated in the figure

</div>




<div id="fig:diagram---for---Galois---lifting"></div>


<div class="corollary" id="corollary:">
	
for finite Galois extension, $K/k$,
and arbitrary extension, $F/k$,
where $K$ and $F$ are subfields of common field,

$$
[KF:F] \mbox{ divides } [F:k]
$$


</div>
<div class="theorem" id="theorem:">
	
for Galois extensions, $K_1/k$ and $K_2/k$,
where $K_1$ and $K_2$ are subfields of common field,

	<ul>
	<li>
		$K_1K_2/k$ is Galois extension

	</li>
	<li>
		map

$$
\sigma \mapsto (\restrict{\sigma}{K_1}, \restrict{\sigma}{K_2})
$$

of $G(K_1K_2/k)$ into $G(K_1/k) \times G(K_2/k)$
is injective;
if $K_1\cap K_2=k$,
map is isomorphism

	</li>
	</ul>
theorem illustrated in the figure

</div>




<div id="fig:diagram---for---Galois---two-side---lifting"></div>


<div class="corollary" id="corollary:">
	
for $n$ Galois extensions, $K_i/k$,
where $K_1$, &hellip;, $K_n$ are subfields of common field
and
$K_{i+1}\cap(K_1\cdots K_i) = k$ for $i=1,\ldots,n-1$,

	<ul>
	<li>
		$K_1\cdots K_n/k$ is Galois extension

	</li>
	<li>
		map

$$
\sigma \mapsto (\restrict{\sigma}{K_1}, \ldots, \restrict{\sigma}{K_n})
$$

induces
isomorphism
of $G(K_1\cdots K_n/k)$ onto $G(K_1/k) \times \cdots \times G(K_n/k)$

	</li>
	</ul>

</div>
<div class="corollary" id="corollary:">
	
for Galois extension, $K/k$,
where $G(K/k)$ can be written as $G_1\times \cdots \times G_n$,
and
$K_1$, &hellip;, $K_n$,
each of which is
fixed field of

$$
G_1 \times \cdots \times \underbrace{\{e\}}_{i\mathrm{th\ position}} \times \cdots \times G_n
$$


	<ul>
	<li>
		$K_1/k$, &hellip;, $K_n/k$ are Galois extensions

	</li>
	<li>
		$G(K_i/k)=G_i$ for $i=1,\ldots,n$

	</li>
	<li>
		$K_{i+1}\cap(K_1\cdots K_i) = k$ for $i=1,\ldots,n-1$

	</li>
	<li>
		$K=K_1\cdots K_n$

	</li>
	</ul>

</div>
<div class="theorem" id="theorem:">
	
assume all fields are subfields of common field

	<ul>
	<li>
		for two abelian Galois extensions, $K/k$ and $L/k$,
$KL/k$ is abelian Galois extension

	</li>
	<li>
		for abelian Galois extension, $K/k$,
and any extension, $E/k$,
$KE/E$ is abelian Galois extension

	</li>
	<li>
		for abelian Galois extension, $K/k$, and intermediate field, $E$,
both $K/E$ and $E/k$ are abelian Galois extensions

	</li>
	</ul>

</div>

<h3>Solvable and radical extensions</h3>

<div class="definition" id="definition:sovable---extensions" data-name="sovable extensions">
	
finite separable extension, $E/k$,
such that
Galois group
of
smallest Galois extension, $K/k$,
containing $E$
is solvable,
said to be <span class="define">solvable</span>

</div>
<div class="theorem" id="theorem:solvable---extensions---are---distinguished" data-name="solvable extensions are distinguished">
	
solvable extensions form distinguished class of extensions

</div>
<div class="definition" id="definition:solvable---by---radicals" data-name="solvable by radicals">
	
finite extension, $F/k$,
such that it is separable
and exists finite extension, $E/k$, containing $F$
admitting tower decomposition

$$
k = E_0 \subset E_1 \subset \cdots \subset E_m = E
$$

with $E_{i+1}/E_i$ is obtained by adjoining root of

	<ul>
	<li>
		unity, or

	</li>
	<li>
		$X^n=a$ with $a\in E_i$, and $n$ prime to characteristic, or

	</li>
	<li>
		$X_p-X-a$ with $a\in E_i$ if $p$ is positive characteristic

	</li>
	</ul>

said to be <span class="define">solvable by radicals</span>

</div>
<div class="theorem" id="theorem:extensions---solvable---by---radicals" data-name="extensions solvable by radicals">
	
separable extension, $E/k$,
is solvable by radicals
if and only if
it is solvable

</div>

<h3>Applications of Galois theory</h3>

<div class="theorem" id="theorem:insolvability---of---quintic---polynomials" data-name="insolvability of quintic polynomials">
	
general equation of degree, $n$,
cannot be solved by radicals
for $n\geq5$
(implied by
<a href="#definition:Galois---group---of---polynomials"></a>,
<a href="#proposition:Galois---group---of---polynomials---and---symmetric---group"></a>,
<a href="#theorem:extensions---solvable---by---radicals"></a>,
and
<a href="#theorem:solvability---of---finite---symmetric---groups"></a>)

</div>

<div class="theorem" id="theorem:fundamental---theorem---of---algebra" data-name="fundamental theorem of algebra">
	


$f\in \complexes[X]$ of degree, $n$,
has precisely $n$ roots in $\complexes$
(when counted with multiplicity),
hence
$\complexes$ is algebraically closed

</div>


<h1 id="super-title-page:Real-Analysis">Real Analysis</h1>



<h2 id="title-page:set-theory">Set Theory</h2>


<h3>Some principles</h3>

<div class="principle" id="principle:principle---of---mathematical---induction" data-name="principle of mathematical induction">
	

$$
P(1) \& [P(n\Rightarrow P(n+1)] \Rightarrow (\forall n \in \naturals)P(n)
$$


</div>

<div class="principle" id="principle:well---ordering---principle" data-name="well ordering principle">
	
<div id="principle:well-ordering---principle-------smallest---element"></div>
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
<a href="#principle:well-ordering---principle-------smallest---element"></a>
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
$x < r < y$

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

<h2 id="title-page:lebesgue-measure">Lebesgue Measure</h2>



<h3>Riemann integral</h3>

<ul>
<li>
	Riemann integral


	<ul>
	<li>
		partition induced by sequence $\seq{x_i}_{i=1}^n$ with $a=x_1<\cdots<x_n=b$

	</li>
	<li>
		lower and upper sums
		<ul>
		<li>
			$L(f,\seq{x_i}) = \sum_{i=1}^{n-1} \inf_{x\in[x_i,x_{i+1}]} f(x) (x_{i+1}-x_{i})$

		</li>
		<li>
			$U(f,\seq{x_i}) = \sum_{i=1}^{n-1} \sup_{x\in[x_i,x_{i+1}]} f(x) (x_{i+1}-x_{i})$

		</li>
		</ul>

	</li>
	<li>
		always holds: $L(f,\seq{x_i}) \leq U(f,\seq{y_i})$, hence

$$
\sup_{\seq{x_i}} L(f,\seq{x_i}) \leq \inf_{\seq{x_i}} U(f,\seq{x_i})
$$


	</li>
	<li>
		Riemann integrable if

$$
\sup_{\seq{x_i}} L(f,\seq{x_i}) = \inf_{\seq{x_i}} U(f,\seq{x_i})
$$


	</li>
	</ul>

</li>
<li>
	every continuous function is Riemann integrable

</li>
</ul>

<h3>Motivation - want measure better than Riemann integrable</h3>


<ul>
<li>
	consider indicator (or characteristic) function $\chi_\rationals:[0,1] \to [0,1]$

$$
\chi_\rationals(x) = \left\{\begin{array}{ll}
1 &\mbox{if } x \in \rationals
\\
0 &\mbox{if } x \not\in \rationals
\end{array}\right.
$$


</li>
<li>
	<i>not</i> Riemann integrable: $\sup_{\seq{x_i}} L(f,\seq{x_i}) = 0 \neq 1 = \inf_{\seq{x_i}} U(f,\seq{x_i})$

</li>
<li>
	however, irrational numbers infinitely more than rational numbers, hence
	<ul>
	<li>
		<i>want to</i> have some integral $\int$ such that, <i>e.g.</i>,

$$
\int_{[0,1]} \chi_\rationals(x) dx = 0
\mbox{ and }
\int_{[0,1]} (1-\chi_\rationals(x)) dx = 1
$$


	</li>
	</ul>

</li>
</ul>

<h3>Properties of desirable measure</h3>


<ul>
<li>
	want some measure $\mu:\subsetset{M}\to\preals=\set{x\in\reals}{x\geq0}$
	<ul>
	<li>
		defined for every subset of $\reals$, <i>i.e.</i>, $\subsetset{M} = \powerset(\reals)$

	</li>
	<li>
		equals to length for open interval

$$
\mu[b,a] = b-a
$$


	</li>
	<li>
		countable additivity: for disjoint $\seq{E_i}_{i=1}^\infty$
$$
\mu(\cup E_i) = \sum \mu(E_i)
$$


	</li>
	<li>
		translation invariant 
$$
\mu(E+x) = \mu(E) \mbox{ for } x\in\reals
$$


	</li>
	</ul>

</li>
<li>
	<i>no</i> such measure exists

</li>
<li>
	<i>not</i> known whether measure with first three properties exists

</li>
<li>
	want to find translation invariant <i>countably additive measure</i>
	<ul>
	<li>
		hence, <i>give up on first property</i>

	</li>
	</ul>

</li>
</ul>

<h3>Race won by Henri Lebesgue in 1902!</h3>

<ul>
<li>
	mathematicians in 19th century struggle to solve this problem

</li>
<li>
	race won by French mathematician, <span class="eemph">Henri Le&#769;on Lebesgue in 1902!</span>


</li>
<li>
	Lebesgue integral covers much wider range of functions
	<ul>
	<li>
		indeed, $\chi_\rationals$ is Lebesgue integrable

$$
\int_{[0,1]} \chi_\rationals(x) dx = 0
\mbox{ and }
\int_{[0,1]} (1-\chi_\rationals(x)) dx = 1
$$


	</li>
	</ul>

</li>
</ul>

<h3>Outer measure</h3>



<ul>
<li>
	for $E\subset\reals$, define outer measure $\mu^\ast:\powerset(\reals)\to\preals$

$$
\mu^\ast E = \inf_{\seq{I_i}} \left\{\left.\sum l(I_i) \right| E\subset \cup I_i\right\}
$$

where $I_i=(a_i,b_i)$ and $l(I_i) = b_i-a_i$

</li>
<li>
	outer measure of open interval is length

$$
\mu^\ast(a_i,b_i) = b_i-a_i
$$


</li>
<li>
	countable subadditivity

$$
\mu^\ast\left(\cup E_i\right) \leq \sum \mu^\ast E_i
$$


</li>
<li>
	corollaries
	<ul>
	<li>
		$\mu^\ast E = 0$ if $E$ is countable

	</li>
	<li>
		$[0,1]$ not countable

	</li>
	</ul>

</li>
</ul>

<h3>Measurable sets</h3>



<div id="page:measurable-sets"></div>
<ul>
<li>
	$E\subset\reals$ called measurable if for every $A\subset\reals$

$$
\mu^\ast A = \mu^\ast (E\cup A) + \mu^\ast (\compl{E}\cup {A})
$$


</li>
<li>
	$\mu^\ast E =0$, then $E$ measurable

</li>
<li>
	every open interval $(a,b)$ with $a\geq -\infty$ and $b\leq \infty$ is measurable

</li>
<li>
	disjoint countable union of measurable sets is measurable, <i>i.e.</i>, $\cup E_i$ is measurable

</li>
<li>
	collection of measurable sets is $\sigma$-algebra



</li>
</ul>

<h3>Borel algebra is measurable</h3>

<ul>
<li>
	note
	<ul>
	<li>
		every open set is disjoint countable union of open intervals (page~<a href="#page:open-closed-fact">here</a>)

	</li>
	<li>
		disjoint countable union of measurable sets is measurable (page~<a href="#page:measurable-sets">here</a>)

	</li>
	<li>
		open intervals are measurable (page~<a href="#page:measurable-sets">here</a>)

	</li>
	</ul>

</li>
<li>
	hence, every open set is measurable

</li>
<li>
	also
	<ul>
	<li>
		collection of measurable sets is $\sigma$-algebra (page~<a href="#page:measurable-sets">here</a>)

	</li>
	<li>
		every open set is Borel set and Borel sets are $\sigma$-algebra (page~<a href="#page:borel-algebra">here</a>)

	</li>
	</ul>

</li>
<li>
	hence, <span class="fact-font">Borel sets are measurable</span>


</li>
<li>
	specifically, <span class="fact-font">Borel algebra (smallest $\sigma$-algebra containing all open sets) is measurable</span>


</li>
</ul>

<h3>Lebesgue measure</h3>

<ul>
<li>
	restriction of $\mu^\ast$ in collection $\subsetset{M}$ of measurable sets called <span class="define">Lebesgue measure</span>



$$
\mu:\subsetset{M}\to\preals
$$


</li>
<li>
	countable subadditivity - for $\seq{E_n}$


$$
\mu (\cup E_n) \leq \sum \mu E_n
$$


</li>
<li>
	<span class="define">countable additivity</span> - for disjoint $\seq{E_n}$


$$
\mu (\cup E_n) = \sum \mu E_n
$$


</li>
<li>
	for dcreasing sequence of measurable sets, $\seq{E_n}$,
<i>i.e.</i>, $(\forall n\in\naturals)(E_{n+1} \subset E_n)$

$$
\mu\left(
\bigcap E_n
\right)
=
\lim
\mu E_n
$$


</li>
</ul>

<h3>(Lebesgue) measurable sets are nice ones!</h3>



<ul>
<li>
	following statements are equivalent

$$
\begin{eqnarray*}
&-&
E \mbox{ is measurable}
\\
&-&
(\forall \epsilon >0)
(\exists \mbox{ open } O\supset E)
(\mu^\ast(O\sim E)<\epsilon)
\\
&-&
(\forall \epsilon >0)
(\exists \mbox{ closed } F\subset E)
(\mu^\ast(E\sim F)<\epsilon)
\\
&-&
(\exists G_\delta)
(G_\delta \supset E)
(\mu^\ast(G_\delta\sim E)<\epsilon)
\\
&-&
(\exists F_\sigma)
(F_\sigma \subset E)
(\mu^\ast(E\sim F_\sigma)<\epsilon)
\end{eqnarray*}
$$


</li>
<li>
	if $\mu^\ast E$ is finite, above statements are equivalent to

$$
(\forall \epsilon>0)
\left(\exists U = \bigcup_{i=1}^n (a_i,b_i) \right)
(\mu^\ast (U\Delta E) < \epsilon)
$$


</li>
</ul>

<h3>Lebesgue measure resolves problem in movitation</h3>


<ul>
<li>
	let

$$
E_1 = \set{x\in[0,1]}{x\in\rationals},\
E_2 = \set{x\in[0,1]}{x\not\in\rationals}
$$


</li>
<li>
	$\mu^\ast E_1=0$ because $E_1$ is countable, hence measurable and

$$
\mu E_1 = \mu^\ast E_1 = 0
$$


</li>
<li>
	algebra implies $E_2 = [0, 1] \cap \compl{E_1}$ is measurable

</li>
<li>
	countable additivity implies $\mu E_1 + \mu E_2 = \mu[0,1] = 1$, hence

$$
\mu E_1 = 1
$$


</li>
</ul>

<h2 id="title-page:measurable-functions">Lebesgue Measurable Functions</h2>


<h3>Lebesgue measurable functions</h3>




<div id="page:Lebesgue-measurable-functions"></div>
<ul>
<li>
	for $f:X\to\reals\cup\{-\infty, \infty\}$,
<i>i.e.</i>, extended real-valued function, the followings are equivalent
	<ul>
	<li>
		for every $a\in\reals$, $\set{x\in{X}}{f(x) < a}$ is measurable

	</li>
	<li>
		for every $a\in\reals$, $\set{x\in{X}}{f(x) \leq a}$ is measurable

	</li>
	<li>
		for every $a\in\reals$, $\set{x\in{X}}{f(x) > a}$ is measurable

	</li>
	<li>
		for every $a\in\reals$, $\set{x\in{X}}{f(x) \geq a}$ is measurable

	</li>
	</ul>

</li>
<li>
	if so,
	<ul>
	<li>
		for every $a\in\reals\cup\{-\infty, \infty\}$, $\set{x\in{X}}{f(x) = a}$ is measurable

	</li>
	</ul>

</li>
<li>
	extended real-valued function, $f$, called <span class="define">(Lebesgue) measurable function</span> if

	<ul>
	<li>
		domain is measurable

	</li>
	<li>
		any one of above four statements holds

	</li>
	</ul>


</li>
</ul>

<h3>Properties of Lebesgue measurable functions</h3>


<div id="page:measurable:function:facts"></div>
<ul>
<li>
	for real-valued measurable functions, $f$ and $g$, and $c\in\reals$
	<ul>
	<li>
		$f+c$, $cf$, $f+g$, $fg$ are measurable

	</li>
	</ul>

</li>
<li>
	for every extended real-valued measurable function sequence, $\seq{f_n}$
	<ul>
	<li>
		$\sup f_n$, $\limsup f_n$ are measurable

	</li>
	<li>
		hence, $\inf f_n$, $\liminf f_n$ are measurable

	</li>
	<li>
		thus, if $\lim f_n$ exists, it is measurable

	</li>
	</ul>


</li>
</ul>

<h3>Almost everywhere - a.e.</h3>

<div id="page:almost:everywhere"></div>
<ul>
<li>
	statement, $P(x)$, called <span class="define">almost everywhere</span> or <span class="define">a.e.</span> if



$$
\mu \set{x}{\sim P(x)} = 0
$$

	<ul>
	<li>
		<i>e.g.</i>, $f$ said to be equal to $g$ a.e. if $\mu\set{x}{f(x)\neq g(x)}=0$

	</li>
	<li>
		<i>e.g.</i>, $\seq{f_n}$ said to converge to $f$ a.e. if

$$
(\exists E \mbox{ with } \mu E=0)(\forall x \not\in E)(\lim f_n (x) = f(x))
$$


	</li>
	</ul>

</li>
<li>
	facts
	<ul>
	<li>
		if $f$ is measurable and $f=g$ i.e., then $g$ is measurable

	</li>
	<li>
		if measurable extended real-valued $f$ defined on $[a,b]$ with $f(x) \in\reals$ a.e.,
then for every $\epsilon>0$, exist step function $g$ and continuous function $h$ such that

$$
\mu\set{x}{|f-g| \geq \epsilon} < \epsilon,\
\mu\set{x}{|f-h| \geq \epsilon} < \epsilon
$$


	</li>
	</ul>

</li>
</ul>

<h3>Characteristic \& simple functions</h3>

<div id="page:Characteristic---and---simple---functions"></div>
<ul>
<li>
	for any $A\subset\reals$, $\chi_A$ called <span class="define">characteristic function</span> if


$$
\chi_A(x) = \left\{\begin{array}{ll}
1 & x\in A\\
0 & x\not\in A\\
\end{array}\right.
$$

	<ul>
	<li>
		$\chi_A$ is measurable if and only if $A$ is measurable

	</li>
	</ul>

</li>
<li>
	measurable $\varphi$ called <span class="define">simple</span> if for some distinct $\seq{a_i}_{i=1}^n$


$$
\varphi(x) = \sum_{i=1}^n a_i \chi_{A_i}(x)
$$

where $A_i = \set{x}{x= a_i}$


</li>
</ul>

<h3>Littlewood's three principles</h3>



<div id="page:littlewood:three:principles"></div>
<ul>
<li>
	 let $M(E)$ with measurable set, $E$, denote set of measurable functions defined on $E$

</li>
<li>
	<span class="fact-font">every (measurable) set is nearly finite union of intervals</span>, <i>e.g.</i>,
	<ul>
	<li>
		$E$ is measurable if and only if

$$
(\forall \epsilon>0)
(\exists \{I_i: \mbox{open\ interval}\}_{i=1}^n)
(\mu^\ast(E \Delta (\cup I_n)) < \epsilon)
$$


	</li>
	</ul>

</li>
<li>
	<span class="fact-font">every (measurable) function is nearly continuous</span>, <i>e.g.</i>,
	<ul>
	<li>
		(Lusin's theorem)

$$
(\forall f \in M[a,b])(\forall \epsilon >0)(\exists g \in C[a,b]) (\mu\set{x}{f(x)\neq g(x)}< \epsilon)
$$


	</li>
	</ul>

</li>
<li>
	<span class="fact-font">every convergent (measurable) function sequence is nearly uniformly convergent</span>, <i>e.g.</i>,

$$
\begin{eqnarray*}
&&
(\forall \mbox{ measurable }\seq{f_n} \mbox{ converging to } f \mbox { a.e. on } E \mbox{ with } \mu E<\infty)

\\
&&
(\forall \epsilon>0 \mbox{ and } \delta>0)
(\exists A\subset E \mbox{ with } \mu(A)<\delta \mbox{ and } N\in\naturals)
\\
&&
(\forall n > N, x\in E\sim A)(|f_n(x)-f(x)|<\epsilon)
\end{eqnarray*}
$$


</li>
</ul>

<h3>Egoroff's theorem</h3>




<ul>
<li>
	<span class="name-font">Egoroff theorem -</span> provides stronger version of third statement
on page~<a href="#page:littlewood:three:principles">here</a>

$$
\begin{eqnarray*}
&&
(\forall \mbox{ measurable }\seq{f_n} \mbox{ converging to } f \mbox { a.e. on } E \mbox{ with } \mu E<\infty)

\\
&&
(\exists A\subset E \mbox{ with } \mu(A)<\epsilon)
(f_n \mbox{ uniformly converges to } f \mbox{ on } E\sim A )
\end{eqnarray*}
$$


</li>
</ul>

<h2 id="title-page:lebesgue-integral">Lebesgue Integral</h2>



<h3>Integral of simple functions</h3>

<div id="page:Integral---of---simple---functions"></div>
<ul>
<li>
	<span class="define">canonical representation</span> of simple function


$$
\varphi(x) = \sum_{i=1}^n a_i \chi_{A_i}(x)
$$

where $a_i$ are <i>distinct</i> $A_i=\{x|\varphi(x)=a_i\}$ - note $A_i$ are <i>disjoint</i>

</li>
<li>
	when $\mu\set{x}{\varphi(x)\neq0}< \infty$ and $\varphi = \sum_{i=1}^n a_i \chi_{A_i}$ is canonical representation,
define <span class="define">integral of $\varphi$</span> by


$$
\int \varphi = \int \varphi (x) dx= \sum_{i=1}^n a_i \mu A_i
$$


</li>
<li>
	when $E$ is measurable, define

$$
\int_E \varphi = \int \varphi \chi_E
$$



</li>
</ul>

<h3>Properties of integral of simple functions</h3>

<ul>
<li>
	for simple functions $\varphi$ and $\psi$
that vanish out of finite measure set,
<i>i.e.</i>,
$\mu\set{x}{\varphi(x)\neq0}<\infty$, $\mu\set{x}{\psi(x)\neq0}<\infty$,
and for every $a,b\in\reals$
<div id="page:linearity---of---Lebesgue---integral---of---simple---functions"></div>

$$
\int (a\varphi + b\psi) = a \int\varphi + b \int\psi
$$



</li>
<li>
	thus, even for simple function, $\varphi = \sum_{i=1}^n a_i \chi_{A_i}$
that vanishes out of finite measure set,
not necessarily in canonical representation,

$$
\int \varphi = \sum_{i=1}^n a_i \mu A_i
$$


</li>
<li>
	if $\varphi \geq \psi$ a.e.

$$
\int \varphi \geq \int \psi
$$


</li>
</ul>

<h3>Lebesgue integral of bounded functions</h3>

<div id="page:Lebesgue---integral---of---bounded---functions"></div>
<ul>
<li>
	for bounded function, $f$, and finite measurable set, $E$,

$$
\sup_{\varphi:\ \mathrm{simple},\ \varphi \leq f} \int_E \varphi
\leq
\inf_{\psi:\ \mathrm{simple},\ f \leq \psi} \int_E \psi
$$

	<ul>
	<li>
		if $f$ is defined on $E$, $f$ is measurable function if and only if

$$
\sup_{\varphi:\ \mathrm{simple},\ \varphi \leq f} \int_E \varphi
=
\inf_{\psi:\ \mathrm{simple},\ f \leq \psi} \int_E \psi
$$


	</li>
	</ul>

</li>
<li>
	for bounded measurable function, $f$, defined on measurable set, $E$, with $\mu E < \infty$,
define <span class="define">(Lebesgue) integral of $f$ over $E$</span>

<div id="page:Lebesgue---integral---of---simple---functions"></div>

$$
\int_E f(x) dx =
\sup_{\varphi:\ \mathrm{simple},\ \varphi \leq f} \int_E \varphi
=
\inf_{\psi:\ \mathrm{simple},\ f \leq \psi} \int_E \psi
$$



</li>
</ul>

<h3>Properties of Lebesgue integral of bounded functions</h3>


<ul>
<li>
	for bounded measurable functions, $f$ and $g$, defined on $E$ with finite measure
<div id="page:linearity---of---nonnegative---integral-------Lebesgue"></div>
	<ul>
	<li>
		for every $a,b\in\reals$

$$
\int_E (af+bg) = a \int_E f + b\int_E g
$$


	</li>
	<li>
		if $f\leq g$ a.e.

$$
\int_E f \leq \int_E g
$$


	</li>
	<li>
		for disjoint measurable sets, $A,B\subset E$,

$$
\int_{A\cup B} f = \int_A f + \int_B f
$$


	</li>
	</ul>


</li>
<li>
	hence,

$$
\left|\int_E f \right| \leq \int_E |f|
\mbox{  \&  }
f=g \mbox{ a.e. } \Rightarrow \int_E f = \int_E g
$$


</li>
</ul>

<h3>Lebesgue integral of bounded functions over finite interval</h3>

<ul>
<li>
	if bounded function, $f$, defined on $[a,b]$ is Riemann integrable,
then $f$ is measurable and

$$
\int_{[a,b]} f
=
R \int_a^b f(x) dx
$$

where $R\int$ denotes Riemann integral

</li>
<li>
	bounded function, $f$, defined on $[a,b]$ is Riemann integrable
if and only if set of points where $f$ is discontinuous has measure zero

</li>
<li>
	for sequence of measurable functions, $\seq{f_n}$, defined on measurable $E$ with finite measure, and $M>0$,
if $|f_n|<M$ for every $n$ and $f(x) = \lim f_n(x)$ for every $x\in E$

$$
\int_E f = \lim \int_E f_n
$$


</li>
</ul>

<h3>Lebesgue integral of nonnegative functions</h3>

<div id="page:Lebesgue---integral---of---nonnegative---functions"></div>
<ul>
<li>
	for nonnegative measurable function, $f$, defined on measurable set, $E$, define

<div id="page:Lebesgue---integral---of---nonnegative---measurable---function"></div>

$$
\int_E f = \sup_{h:\ \mathrm{bounded\ measurable\ function},\ \mu\set{x}{h(x)\neq0}<\infty,\ h\leq f} \int_E h
$$



</li>
<li>
	for nonnegative measurable functions, $f$ and $g$
	<ul>
	<li>
		for every $a,b\geq0$

$$
\int_E (af + bg) = a\int_E f + b\int_E g
$$


	</li>
	<li>
		if $f\geq g$ a.e.

$$
\int_E f \leq \int_E g
$$


	</li>
	</ul>

</li>
<li>
	thus,
	<ul>
	<li>
		for every $c>0$

$$
\int_E cf = a\int_E f
$$


	</li>
	</ul>

</li>
</ul>

<h3>Fatou's lemma and monotone convergence theorem for Lebesgue integral</h3>

<div id="page:integral:nonneg:facts"></div>
<ul>
<li>
	<span class="name-font">Fatou's lemma -</span>
for nonnegative measurable function sequence, $\seq{f_n}$,
with $\lim f_n = f$ a.e. on measurable set, $E$




$$
\int_E f \leq \liminf \int_E f_n
$$

	<ul>
	<li>
		note $\lim f_n$ is measurable (page~<a href="#page:measurable:function:facts">here</a>),
hence $f$ is measurable (page~<a href="#page:almost:everywhere">here</a>)

	</li>
	</ul>

</li>
<li>
	<span class="name-font">monotone convergence theorem -</span>
for nonnegative increasing measurable function sequence, $\seq{f_n}$,
with $\lim f_n = f$ a.e. on measurable set, $E$


<div id="page:Lebesgue-------monotone---convergence---theorem"></div>

$$
\int_E f = \lim \int_E f_n
$$



</li>
<li>
	for nonnegative measure function, $f$, and sequence of disjoint measurable sets, $\seq{E_i}$,

$$
\int_{\cup E_i} f = \sum \int_{E_i} f
$$


</li>
</ul>

<h3>Lebesgue integrability of nonnegative functions</h3>

<div id="integrable:nonnegative:function"></div>
<ul>
<li>
	nonnegative measurable function, $f$, said to be <span class="define">integrable</span> over measurable set, $E$, if



<div id="page:Lebesgue---integrability---of---nonnegative---functions"></div>

$$
\int_E f < \infty
$$



</li>
<li>
	for nonnegative measurable functions, $f$ and $g$, if $f$ is integrable on measurable set, $E$,
and $g\leq f$ a.e. on $E$, then $g$ is integrable and

$$
\int_E (f-g) = \int_E f - \int_E g
$$


</li>
<li>
	for nonnegative integrable function, $f$, defined on measurable set, $E$, and every $\epsilon$,
exists $\delta >0$ such that for every measurable set $A\subset E$ with $\mu A< \epsilon$
(then $f$ is integrable on $A$, of course),

$$
\int_A f < \epsilon
$$


</li>
</ul>

<h3>Lebesgue integral</h3>

<ul>
<li>
	for (any) function, $f$, define $f^+$ and $f^-$ such that for every $x$

$$
\begin{eqnarray*}
f^+(x) &=& \max\{f(x), 0\}
\\
f^-(x) &=& \max\{-f(x), 0\}
\end{eqnarray*}
$$


</li>
<li>
	note
$f = f^+ - f^-,\ |f| = f^+ + f^-,\ f^- = (-f)^+$

</li>
<li>
	measurable function, $f$, said to be <span class="define">(Lebesgue) integrable</span> over measurable set, $E$,
if (nonnegative measurable) functions, $f^+$ and $f^-$, are integrable




<div id="page:Lebesgue---integral"></div>

$$
\int_E f = \int_E f^+ - \int_E f^-
$$



</li>
</ul>

<h3>Properties of Lebesgue integral</h3>


<ul>
<li>
	for $f$ and $g$ integrable on measure set, $E$, and $a,b\in\reals$
<div id="page:properties---of---Lebesgue---integral"></div>
	<ul>
	<li>
		$af+bg$ is integral and

$$
\int_E (af+bg) = a \int_E f + b\int_E g
$$


	</li>
	<li>
		if $f\geq g$ a.e. on $E$,

$$
\int_E f \geq \int_E g
$$


	</li>
	<li>
		for disjoint measurable sets, $A,B\subset E$

$$
\int_{A\cup B} f = \int_A f + \int_B g
$$


	</li>
	</ul>


</li>
</ul>

<h3>Lebesgue convergence theorem (for Lebesgue integral)</h3>

<ul>
<li>
	<span class="name-font">Lebesgue convergence theorem -</span>
for measurable $g$ integrable on measurable set, $E$,
and measurable sequence $\seq{f_n}$ converging to $f$ with $|f_n|<g$ a.e. on $E$,
($f$ is measurable (page~<a href="#page:measurable:function:facts">here</a>),
every $f_n$ is integrable (page~<a href="#integrable:nonnegative:function">here</a>))
and



<div id="page:lebesgue-integral-facts-2"></div>

$$
\int_E f = \lim \int_E f_n
$$

<div id="page:Lebesgue---convergence---theorem---for---Lebesgue---integral"></div>


</li>
</ul>

<h3>Generalization of Lebesgue convergence theorem (for Lebesgue integral)</h3>

<ul>
<li>
	<span class="name-font">generalization of Lebesgue convergence theorem -</span>
for sequence of functions, $\seq{g_n}$, integrable on measurable set, $E$,
converging to integrable $g$ a.e. on $E$,
and sequence of measurable functions, $\seq{f_n}$,
converging to $f$ a.e. on $E$
with $|f_n|<g_n$ a.e. on $E$,
if

$$
\int_E g = \lim \int_E g_n
$$

then
($f$ is measurable (page~<a href="#page:measurable:function:facts">here</a>),
every $f_n$ is integrable (page~<a href="#integrable:nonnegative:function">here</a>))
and

$$
\int_E f = \lim \int_E f_n
$$


</li>
</ul>

<h3>Comments on convergence theorems</h3>


<ul>
<li>
	Fatou's lemma (page~<a href="#page:integral:nonneg:facts">here</a>),
monotone convergence theorem (page~<a href="#page:integral:nonneg:facts">here</a>),
Lebesgue convergence theorem (page~<a href="#page:lebesgue-integral-facts-2">here</a>),
<i>all</i>
state that under suitable conditions, we say something about

$$
\int \lim f_n
$$

in terms of

$$
\lim \int f_n
$$


</li>
<li>
	Fatou's lemma requires weaker condition than Lebesgue convergence theorem, <i>i.e.</i>,
only requires &ldquo;bounded below'' whereas Lebesgue converges theorem also requires &ldquo;bounded above''

$$
\int \lim f_n \leq \liminf \int f_n
$$


</li>
<li>
	monotone convergence theorem is somewhat between the two;
	<ul>
	<li>
		advantage - applicable even when $f$ not integrable

	</li>
	<li>
		Fatou's lemma and monotone converges theorem very clsoe in sense that
can be derived from each other using only facts of positivity and linearity of integral

	</li>
	</ul>

</li>
</ul>

<h3>Convergence in measure</h3>


<ul>
<li>
	$\seq{f_n}$ of measurable functions said to <span class="define">converge $f$ in measure</span> if

$$
(\forall \epsilon>0)
(\exists N\in\naturals)
(\forall n > N)
(\mu\set{x}{|f_n-f|>\epsilon} < \epsilon)
$$


</li>
<li>
	thus, third statement on page~<a href="#page:littlewood:three:principles">here</a> implies

$$
(\forall \seq{f_n} \mbox{ converging to } f \mbox { a.e. on } E \mbox{ with } \mu E<\infty)
(f_n \mbox{ converge in measure to }f)
$$


</li>
<li>
	however, the converse is <i>not</i> true, <i>i.e.</i>,
exists $\seq{f_n}$ converging in measure to $f$ that does not converge to $f$ a.e.
	<ul>
	<li>
		<i>e.g.</i>, XXX

	</li>
	</ul>

</li>
<li>
	Fatou's lemma (page~<a href="#page:integral:nonneg:facts">here</a>),
monotone convergence theorem (page~<a href="#page:integral:nonneg:facts">here</a>),
Lebesgue convergence theorem (page~<a href="#page:lebesgue-integral-facts-2">here</a>)
<span class="eemph">remain valid!</span>
even when &ldquo;convergence a.e.'' replaced by &ldquo;convergence in measure''

</li>
</ul>

<h3>Conditions for convergence in measure</h3>

<div class="proposition" id="proposition:necessary---condition---for---converging---in---measure" data-name="necessary condition for converging in measure">
	

$$
\left(
\forall \seq{f_n} \mbox{ converging in measure to } f
\right)
\left(
\exists \mbox{ subsequence }\seq{f_{n_k}} \mbox{ converging a.e. to } f
\right)
$$


</div>
<div class="corollary" id="corollary:necessary---and---sufficient---condition---for---converging---in---measure" data-name="necessary and sufficient condition for converging in measure">
	
for sequence $\seq{f_n}$ measurable on $E$ with $\mu E<\infty$

$$
\begin{eqnarray*}
&&\seq{f_n} \mbox{ converging in measure to } f
\\
&\Leftrightarrow&
\left(
\forall \mbox{ subsequence }\seq{f_{n_k}}
\right)
\left(
\exists \mbox{ its subsequence }\seq{f_{n_{k_l}}} \mbox{ converging a.e. to } f
\right)
\end{eqnarray*}
$$


</div>

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
$(\forall C\in\topol{C}_y)(\exists B\in\collB_x)(B\subset f^{-1}(C))$

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
			 $(\forall x \neq y \in X)(\exists \mbox{ open }O\subset X)(y \in O, x \not\in O)$

		</li>
		</ul>

	</li>
	<li>
		<span class="define">$T_2$ - Hausdorff spaces</span>
		<ul>
		<li>
			 $(\forall x \neq y \in X)(\exists \mbox{ open }O_1, O_2\subset X \mbox{ with } O_1\cap O_2=\emptyset)(x \in O_1, y \in O_2)$

		</li>
		</ul>

	</li>
	<li>
		<span class="define">$T_3$ - regular spaces</span>
		<ul>
		<li>
			 $T_1$ &amp;
$(\forall \mbox{ closed } F \subset X, x \not\in F)
(\exists \mbox{ open }O_1, O_2\subset X \mbox{ with } O_1\cap O_2=\emptyset)
(x \in O_1, F \subset O_2)$

		</li>
		</ul>

	</li>
	<li>
		<span class="define">$T_4$ - normal spaces</span>
		<ul>
		<li>
			 $T_1$ &amp;
$(\forall \mbox{ closed } F_1, F_2 \subset X)
(\exists \mbox{ open }O_1, O_2\subset X \mbox{ with } O_1\cap O_2=\emptyset)
(F_1 \subset O_1, F_2 \subset O_2)$

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
(\forall \mbox{ disjoint closed } A, B \subset X) (\exists f\in C(X,[0,1])) (f(A) = \{0\}, f(B) = \{1\})
$$


	</li>
	<li>
		<span class="name-font">Tietze's extension theorem -</span> for normal topological space, $X$

$$
(\forall \mbox{ closed } A \subset X, f\in C(A,\reals))
(\exists g \in C(X,\reals))
(\forall x \in A)
(g(x) = f(x))
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
\lambda(x+y) = \lambda x + \lambda y	&& \mbox{- distributivity of multiplicative over addition}
\\
(\lambda+\mu)x = \lambda x + \mu x	&& \mbox{- distributivity of multiplicative over addition}
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
$(
\forall f\in X^{\ast}
)
(
(\varphi (x))(f) = f(x)
)$
	<ul>
	<li>
		then,
$\|\varphi(x)\|
= \sup_{\|g\|=1, g\in X^\ast} g(x)
\leq \sup_{\|g\|=1, g\in X^\ast} \|g\|\|x\|
= \|x\|$

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
$(\forall x\in X)(\|x\|_A \leq C \|x\|_B)$,
two norms are equivalent, <i>i.e.</i>,
$(\exists C'\in\reals)(\forall x\in X)(\|x\|_B \leq C' \|x\|_A)$

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
$(\forall x,y\in K)(\mbox{segment joining }x,y\subset X)$

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
=
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
$z_n = \sum_{i=1}^n a_i \varphi_i$

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
\seq{\varphi_n} \mbox{ is complete}
\Leftrightarrow
(
(\exists \mbox{ orthonormal }R\subset H)(\forall n\in\naturals)(\varphi_n \in R)
\Rightarrow
R = \seq{\varphi_n}
)
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

<h2 id="title-page:Measure-and-Integration">Measure and Integration</h2>


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


<div id="page:measure!measurable---spaces"></div>
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
<div id="page:interesting-(and-bizarre)-example"></div>
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
while measure, $\mu_B$, on page~<a href="#page:interesting-(and-bizarre)-example">here</a>
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

<div id="page:Measurable---functions"></div>
<ul>
<li>
	concept and properties of measurable functions in abstract measurable space
almost identical with those of Lebesgue measurable functions
(page~<a href="#title-page:measurable-functions">here</a>)

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


<div id="page:Properties---of---measurable---functions"></div>
<ul>
<li>
		<div class="theorem" id="theorem:measurability---preserving---function---operations" data-name="measurability preserving function operations">
		
for measurable functions, $f$ and $g$, and $c\in\reals$
		<ul>
		<li>
			$f+c$, $cf$, $f+g$, $fg$, $f\vee g$ are measurable

		</li>
		</ul>

	</div>

</li>
<li>
		<div class="theorem" id="theorem:limits---of---measurable---functions" data-name="limits of measurable functions">
		
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

<div id="page:Simple---functions"></div>
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

<div id="page:Integration"></div>
<ul>
<li>
	many definitions and proofs of Lebesgue integral
depend only on properties of Lebesgue measure
which are also true for arbitrary measure in abstract measure space
(page~<a href="#title-page:lebesgue-integral">here</a>)

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

<div id="page:integral---of---simple---functions"></div>

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
(page~<a href="#page:Lebesgue---integral---of---nonnegative---functions">here</a>)
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

<div id="page:integral---of---nonnegative---extended---real-valued---measurable---function"></div>

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



<div id="page:Fatou's---lemma!integral"></div>

$$
\int_E f \leq \liminf \int_E f_n
$$


</li>
<li>
	<span class="name-font">monotone convergence theorem -</span>
for nonnegative measurable function sequence, $\seq{f_n}$,
with $f_n\leq f$ for all $n$ and with $\lim f_n = f$ a.e.


<div id="page:abstract-------monotone---convergence---theorem"></div>

$$
\int_E f = \lim \int_E f_n
$$



</li>
</ul>

<h3>Integrability of nonnegative functions</h3>

<ul>
<li>
	for nonnegative measurable functions, $f$ and $g$, and $a,b\in\preals$
<div id="page:linearity---of---nonnegative---integral-------abstract"></div>

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



<div id="page:integrability---of---nonnegative---functions"></div>

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



<div id="page:integral"></div>

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

<div id="page:properties---of---integral"></div>
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



<div id="page:Lebesgue!convergence---theorem"></div>

$$
|f_n(x)|\leq g(x)
$$

then

$$
\int_E f = \lim \int_E f_n
$$

<div id="page:Lebesgue---convergence---theorem"></div>


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
(compare with Fatou's lemma on page~<a href="#page:Fatou's---lemma!integral">here</a>)

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
(compare with Lebesgue convergence theorem on page~<a href="#page:Lebesgue!convergence---theorem">here</a>)

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
called <span class="define">$L^p$ spaces</span> denoted by <span class="notation">$L^p(\mu)$</span>


	</li>
	<li>
		space of bounded measure functions,
called <span class="define">$L^\infty$ space</span> denoted by <span class="notation">$L^\infty(\mu)$</span>


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

<div id="page:Holder---inequality-complete---measure---spaces"></div>
<ul>
<li>
	<span class="name-font">Ho&#776;lder's inequality -</span>


<div id="page:Holder's---inequality!complete---measure---spaces"></div>
for $p,q\in[1,\infty]$ with $1/p+1/q=1$,
$f\in L^p(\mu)$ and $g\in L^q(\mu)$ satisfy
$fg \in L^1(\mu)$ and

$$
\|fg\|_1 = \int |fg| d\mu \leq \|f\|_p\|g\|_q
$$



</li>
<li>
	<span class="name-font">complete measure space version of Littlewood's second principle -</span>
<div id="page:complete---measure---space---version---of---Littlewood's---second---principle"></div>

for $p\in[1,\infty)$

$$
\begin{eqnarray*}
&&
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




<div id="page:Riesz---representation---theorem!complete---measure---spaces"></div>
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

<h2 id="title-page:Measure---and---Outer---Measure">Measure and Outer Measure</h2>


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

<h1 id="super-title-page:Measure---Theoretic---Treatment---of---Probabilities">Measure-theoretic Treatment of Probabilities</h1>



<h2 id="title-page:Probability---Measure">Probability Measure</h2>


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

(thus, measurable functions defined on page~<a href="#page:Lebesgue-measurable-functions">here</a>
and page~<a href="#page:Measurable---functions">here</a>
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

(refer to page~<a href="#page:measure!measurable---spaces">here</a> for resumblance with measurable spaces)
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
<div id="page:probability-measures-agreeing-on-P-agree-on-sigma-P"></div>

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



<div id="probability---spaces!independence!of---collection---of---classes---of---events"></div>

</li>
<li>
	<span class="fact-font">
for independent indexed collection, \seq{\subsetset{A}_\lambda}, with every $\subsetset{A}_\lambda$ being $\pi$-sytem,
\seq{\sigma(\subsetset{A}_\lambda)} are independent
</span>
<div id="page:pi-system-induces-independent-sigma-algebras"></div>

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
		<div class="lemma" id="lemma:first---Borel-Cantelli" data-name="first Borel-Cantelli">
		

for sequence of events, $\seq{A_n}$, with $\sum P(A_n)$ converging

$$
P(\limsup A_n) = 0
$$


	</div>

</li>
<li>
		<div class="lemma" id="lemma:second---Borel-Cantelli" data-name="second Borel-Cantelli">
		

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
	
(use conventions in page~<a href="#page:Some---conventions">here</a> for extended real values)

</li>
<li>
	indeed, $\pi'(E)=\pi''(E)$ for every $E\in\algX\times\algY$; let $\pi=\pi'=\pi''$

</li>
<li>
	$\pi$ is
	<ul>
	<li>
		called <span class="define">product measure</span>


and denoted by <span class="notation">$\mu\times \nu$</span>

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

<h2 id="title-page:Random---Variables">Random Variables</h2>


<h3>Random variables</h3>

<div id="page:random-variables"></div>
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



and denoted by <span class="notation">$\sigma(X)$</span>
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
	
(refer to statement on page~<a href="#page:probability-measures-agreeing-on-P-agree-on-sigma-P">here</a>)
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
	random variables, $X_1$, &hellip;, $X_n$,
with independent $\sigma$-algebras generated by them,
said to be <span class="define">independent</span>



</li>
<li>
	
(refer to page~<a href="#probability---spaces!independence!of---collection---of---classes---of---events">here</a> for
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
	for random variables, $X_1$, &hellip;, $X_n$,
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
	random variables, $X_1$, &hellip;, $X_n$,
each of which is measurable with respect to each of $n$ independent $\sigma$-algebras,
$\algk{G}_1\subset \algF$, &hellip;, $\algk{G}_n\subset \algF$
respectively,
are independent



</li>
</ul>

<h3>Independence of random vectors</h3>

<ul>
<li>
	for random vectors, $X_1:\Omega\to\reals^{d_1}$, &hellip;, $X_n:\Omega\to\reals^{d_n}$,
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

<div class="theorem" id="theorem:Probability---evaluation---for---two---independent---random---vectors" data-name="Probability evaluation for two independent random vectors">
	
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

<div class="theorem" id="theorem:squence---of---random---variables" data-name="squence of random variables">
	
for sequence of probability measures on $\algR$, $\seq{\mu_n}$,
exists probability space, $\meas{X}{\Omega}{P}$,
and sequence of independent random variables in $\reals$, $\seq{X_n}$,
such that each $X_n$ has $\mu_n$ as distribution

</div>

<h3>Expected values</h3>

<div class="definition" id="definition:expected---values" data-name="expected values">
	


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

<div class="inequality" id="inequality:Markov---inequality" data-name="Markov inequality">
	



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
<div class="inequality" id="inequality:Chebyshev's---inequality" data-name="Chebyshev's inequality">
	



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

<div class="inequality" id="inequality:Jensen's---inequality" data-name="Jensen's inequality">
	



for random variable, $X$, on $\meas{\Omega}{\algF}{P}$,
and convex function, $\varphi$

$$
\varphi\left(\Expect X\right)
\prob{X\geq \alpha} \leq \frac{1}{\alpha} \int_{X\geq \alpha} X d P \leq \frac{1}{\alpha} \Expect X
$$


</div>
<div class="inequality" id="inequality:Holder's---inequality" data-name="Holder's inequality">
	



for two random variables, $X$ and $Y$, on $\meas{\Omega}{\algF}{P}$,
and $p,q\in(1,\infty)$ with $1/p+1/q=1$

$$
\Expect |XY| \leq
\left(\Expect |X|^p\right)^{1/p}
\left(\Expect |X|^q\right)^{1/q}
$$


</div>


<div class="inequality" id="inequality:Lyapunov's---inequality" data-name="Lyapunov's inequality">
	



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


<div class="theorem" id="theorem:Kolmogorov's---zero-one---law" data-name="Kolmogorov's zero-one law">
	


if $A\in\algF=\bigcap_{n=1}^\infty \sigma(X_n, X_{n+1},\ldots)$ for independent $\seq{X_n}$,

$$
\prob{A} = 0 \vee \prob{A} = 1
$$


</div>
-- define $S_n = \sum X_i$
<div class="inequality" id="inequality:Kolmogorov's---maximal---inequality" data-name="Kolmogorov's maximal inequality">
	


for independent $\seq{X_i}_{i=1}^n$ with $\Expect X_i =0$ and $\Var X_i<\infty$
and $\alpha>0$

$$
\prob{\max S_i \geq \alpha} \leq \frac{1}{\alpha}\Var S_n
$$


</div>
<div class="inequality" id="inequality:Etemadi's---maximal---inequality" data-name="Etemadi's maximal inequality">
	


for independent $\seq{X_i}_{i=1}^n$
and $\alpha>0$

$$
\prob{\max |S_i| \geq 3\alpha} \leq 3 \max \prob{|S_i|\geq\alpha}
$$


</div>

<h3>Moments</h3>

<div class="definition" id="definition:moments---and---absolute---moments" data-name="moments and absolute moments">
	




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

<div class="definition" id="definition:moment---generating---function" data-name="moment generating function">
	


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

<h2 id="title-page:Convergence---of---Random---Variables">Convergence of Random Variables</h2>


<h3>Convergences of random variables</h3>



<div class="definition" id="definition:convergence---with---probability---$1$" data-name="convergence with probability $1$">
	



random variables, $\seq{X_n}$,
with

$$
\prob{\lim X_n = X}
= P(\set{\omega \in \Omega}{\lim X_n(\omega) = X(\omega)})
= 1
$$

said to <span class="define">converge to $X$ with probability $1$</span>
and denoted by <span class="notation">$X_n\to X$ a.s.</span>

</div>
<div class="definition" id="definition:convergence---in---probability" data-name="convergence in probability">
	



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
<div class="definition" id="definition:weak---convergence" data-name="weak convergence">
	



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
and denoted by <span class="notation">$F_n \Rightarrow F$</span>

</div>
<div class="definition" id="definition:converge---in---distribution" data-name="converge in distribution">
	



When $F_n\Rightarrow F$,
associated random variables, $\seq{X_n}$,
said to <span class="define">converge in distribution</span> to $X$, associated with $F$,
and denoted by <span class="notation">$X_n \Rightarrow X$</span>

</div>
<div class="definition" id="definition:weak---convergence---of---measures" data-name="weak convergence of measures">
	


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




<div class="proposition" id="proposition:relations---of---convergence---of---random---variables" data-name="relations of convergence of random variables">
	
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
<div class="theorem" id="theorem:strong---law---of---large---numbers" data-name="strong law of large numbers">
	


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
<div class="corollary" id="corollary:strong---law---of---large---numbers" data-name="strong law of large numbers">
	
for sequence of independent and identically distributed (i.i.d.) random variables
with $\Expect X_1^- < \infty$ and $\Expect X_1^+ = \infty$ (hence, $\Expect X = \infty$)

$$
\frac{1}{n} S_n \to \infty
$$

with probability $1$

</div>

<h3>Weak law of large numbers</h3>

-- define $S_n = \sum_{i=1}^n X_i$
<div class="theorem" id="theorem:weak---law---of---large---numbers" data-name="weak law of large numbers">
	


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
(<a href="#proposition:relations---of---convergence---of---random---variables"></a>),
strong law of large numbers
implies
weak law of large numbers

</li>
</ul>

<h3>Normal distributions</h3>



-- assume probability space, $\meas{\Omega}{\algF}{P}$
<div class="definition" id="definition:normal---distributions" data-name="normal distributions">
	


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
and denoted by <span class="notation">$X \sim \normal(c,\sigma^2)$</span>

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
<div class="definition" id="definition:multivariate---normal---distributions" data-name="multivariate normal distributions">
	


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
and denoted by <span class="notation">$X \sim \normal(c,\Sigma)$</span>

</div>
<ul>
<li>
	
note that $\Expect X=c$ and covariance matrix is $\Sigma$

</li>
</ul>

<h3>Lindeberg-Le&#769;vy theorem</h3>





-- define $S_n = \sum^n X_i$
<div class="theorem" id="theorem:Lindeberg-Levy---theorem" data-name="Lindeberg-Levy theorem">
	




for independent random variables, $\seq{X_n}$, having same distribution with expected value, $c$, and same variance, $\sigma^2<\infty$,
${(S_n - nc)}/{\sigma\sqrt{n}}$ converges to standard normal distribution in distribution, <i>i.e.</i>,

$$
\frac{S_n - nc}{\sigma\sqrt{n}} \Rightarrow N
$$

where $N$ is standard normal distribution

</div>
<ul>
<li>
	
<a href="#theorem:Lindeberg-Levy---theorem"></a> implies

$$
S_n / n \Rightarrow c
$$


</li>
</ul>

<h3>Limit theorems in $\reals^n$</h3>



<div class="theorem" id="theorem:equivalent---statements---to---weak---convergence" data-name="equivalent statements to weak convergence">
	
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
<div class="theorem" id="theorem:convergence---in---distribution---of---random---vector" data-name="convergence in distribution of random vector">
	
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
<div class="theorem" id="theorem:central---limit---theorem" data-name="central limit theorem">
	
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
<div class="theorem" id="theorem:convergence---with---probability---1---for---random---series" data-name="convergence with probability 1 for random series">
	
for independent $\seq{X_n}$ with $\Expect X_n=0$ and $\Var X_n < \infty$

$$
\sum X_n \mbox{ converges with probability $1$}
$$


</div>
<div class="theorem" id="theorem:convergence---conditions---for---random---series" data-name="convergence conditions for random series">
	
for independent $\seq{X_n}$,
$\sum X_n$ converges with probability $1$
if and only if
they converges in probability

</div>

-- define trucated version of $X_n$ by $X_n^{(c)}$, <i>i.e.</i>, $X_n I_{|X_n|\leq c}$
<div class="theorem" id="theorem:convergence---conditions---for---truncated---random---series" data-name="convergence conditions for truncated random series">
	
for independent $\seq{X_n}$,

$$
\begin{eqnarray*}
&&
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

<h1 id="super-title-page:Convex---Optimization">Convex Optimization</h1>






























<h2 id="title-page:Convex---Sets">Convex Sets</h2>


<h3>Lines and line segmenets</h3>

<div class="definition" id="definition:lines" data-name="lines">
	
for some $x,y\in\reals^n$

$$
\set{\theta x + (1-\theta) y}{\theta\in\reals}
$$

called <span class="define">line going through $x$ and $y$</span>

</div>
<div class="definition" id="definition:line---segmenets" data-name="line segmenets">
	
for some $x,y\in\reals^n$

$$
\set{\theta x + (1-\theta) y}{0\leq\theta\leq1\in\reals}
$$

called <span class="define">line segment connecting $x$ and $y$</span>

</div>

<h3>Affine sets</h3>

<div class="definition" id="definition:affine---sets" data-name="affine sets">
	
set, $C\subset \reals^n$,
every line going through any two points in which
is contained in $C$, <i>i.e.</i>

$$
\left(
\forall x,y \in C
\right)
\left(
\set{\theta x + (1-\theta) y}{\theta \in \reals} \subset C
\right)
$$

called
<span class="define">affine set</span>

</div>
<div class="definition" id="definition:affine---hulls" data-name="affine hulls">
	
for set, $C\subset\reals^n$,
intersection of all affine sets containing $C$,
called <span class="define">affine hull of $C$</span>,
denoted by <span class="notation">$\affinehull C$</span>,
which is equal to
set of all affine combinations of points in $C$, <i>i.e.</i>

$$
\bigcup_{n\in\naturals}
\set{\theta_1 x_1 + \cdots + \theta_n x_n}{x_1,\ldots,x_n\in C, \theta_1 + \cdots + \theta_n=1}
$$


</div>
<div class="definition" id="definition:affine---dimension" data-name="affine dimension">
	
for $C\subset \reals^n$,
dimension of $\affinehull C$,
called <span class="define">affine dimension</span>

</div>

<h3>Relative interiors and boundaries</h3>

<div class="definition" id="definition:relative---interiors---of---sets" data-name="relative interiors of sets">
	
for $C\subset \reals^n$,

$$
\bigcup_{O:\mathrm{open}, O\cap \affinehull C\subset C} O \cap \affinehull C
$$

or equivalently

$$
\set{x}{(\exists \epsilon >0)(\forall y\in \affinehull{C}, \|y-x\|<\epsilon)(y\in C)}
$$

is called <span class="define">relative interior of $C$</span> or <span class="define">interior relative to $C$</span>,
denoted by <span class="notation">$\relint C$</span>

</div>
<div class="definition" id="definition:relative---boundaries---of---sets" data-name="relative boundaries of sets">
	
for $C\subset \reals^n$,
$\closure{C}\sim \relint C$,
called <span class="define">relative boundary of $C$</span>

</div>

<h3>Convex sets</h3>

<div class="definition" id="definition:convex---sets" data-name="convex sets">
	
set, $C\subset \reals^n$,
every line segment connecting any two points in which
is contained in $C$, <i>i.e.</i>

$$
\left(
\forall x,y\in C
\right)
\left(
\forall 0\leq \theta\leq1
\right)
\left(
\theta x + (1-\theta) y \in C
\right)
$$

called <span class="define">convex set</span>

</div>
<div class="definition" id="definition:convex---hulls" data-name="convex hulls">
	
for set, $C\subset \reals^n$,
intersection of all convex sets containing $C$,
called <span class="define">convex hull of $C$</span>,
denoted by <span class="notation">$\cvxhull C$</span>,
which is equal to
set of all convex combinations of points in $C$, <i>i.e.</i>

$$
\bigcup_{n\in\naturals}
\set{\theta_1 x_1 + \cdots + \theta_n x_n}{x_1,\ldots,x_n\in C, \theta_1 + \cdots + \theta_n=1, \theta_1, \ldots, \theta_n >0}
$$


</div>
<ul>
<li>
	convex hull (of course) is convex set

</li>
</ul>

<h3>Cones</h3>

<div class="definition" id="definition:cones" data-name="cones">
	
set, $C\subset \reals^n$,
for which

$$
\left(
\forall x\in C, \theta \geq 0
\right)
\left(
\theta x \in C
\right)
$$

called <span class="define">cone</span> or <span class="define">nonnegative homogeneous</span>

</div>
<div class="definition" id="definition:convex---cone" data-name="convex cone">
	
set, $C\subset \reals^n$,
which is both convex and cone,
called <i>convex cone</i>;
$C$ is convex cone if and only if

$$
\left(
\forall x, y\in C, \theta, \xi \geq0
\right)
\left(
\theta x + \xi y \in C
\right)
$$


</div>
<ul>
<li>
	convex cone (of course) is convex set

</li>
<li>
	examples of convex cones:
$\prealk{n}$, $\pprealk{n}$, $\possemidefset{n}$, and $\posdefset{n}$

</li>
</ul>

<h3>Hyperplanes and half spaces</h3>

<div class="definition" id="definition:hyperplanes" data-name="hyperplanes">
	
$n-1$ dimensional affine set in $\reals^n$,
called <span class="define">hyperplane</span>;
every hyperplane
can be expressed as

$$
\set{x\in\reals^n}{a^T = b}
$$

for some $a\neq0 \in \reals^n$ and $b\in \reals$

</div>
<div class="definition" id="definition:half---spaces" data-name="half spaces">
	
one of two sets divided by hyperplane,
called <span class="define">half space</span>;
every half space
can be expressed as

$$
\set{x\in\reals^n}{a^T \leq b}
$$

for some $a\neq0 \in \reals^n$ and $b\in \reals$

</div>
<ul>
<li>
	hyperplanes and half spaces are convex sets

</li>
</ul>

<h3>Euclidean balls and ellipsoids</h3>

<div class="definition" id="definition:Euclidean---ball" data-name="Euclidean ball">
	
set of all points distance of which from point, $x\in\reals^n$,
is no greater than $r>0$,
called <span class="define">(Euclidean) ball centered at $x$ with radius, $r$</span>,
denoted by <span class="notation">$\ball{x}{r}$</span>,
<i>i.e.</i>

$$
\ball{x}{r} = \set{y\in\reals^n}{\|y-x\|_2\leq r}
$$


</div>
<div class="definition" id="definition:ellipsoids" data-name="ellipsoids">
	
ball elongated along $n$ orthogonal axes,
called <span class="define">ellipsoid</span>,
<i>i.e.</i>,

$$
\set{y\in\reals^n}{(y-x)^TP^{-1}(y-x)\leq 1}
$$

for some $x\in\reals^n$ and $P\in \posdefset{n}$

</div>
<ul>
<li>
	Euclidean balls and ellipsoids are convex sets

</li>
</ul>

<h3>Norm balls and norm cones</h3>

<div class="definition" id="definition:norm---ball" data-name="norm ball">
	
for norm, $\|\cdot\|:\reals^n\to\preals$,
set of all points distance of which measured in the norm from point, $x\in\reals^n$,
is no greater than $r>0$,
called <span class="define">norm ball centered at $x$ with radius, $r$, associated with norm, $\|\cdot\|$</span>,
<i>i.e.</i>

$$
\set{y\in\reals^n}{\|y-x\|\leq r}
$$


</div>
<div class="definition" id="definition:norm---cone" data-name="norm cone">
	
for norm, $\|\cdot\|:\reals^n\to\preals$,
$x\in\reals^n$,
and
$r>0$,

$$
\set{(x,y)\in\reals^n \times \reals}{ \|x\|\leq r} \subset \reals^{n+1}
$$

called <span class="define">cone associated with norm, $\|\cdot\|$</span>

</div>
<div class="definition" id="definition:second-order---cone" data-name="second-order cone">
	
norm cone associated with Euclidean norm,
called <span class="define">second-order cone</span>

</div>
<ul>
<li>
	norm balls and norm cones are convex sets

</li>
</ul>

<h3>Polyhedra</h3>

<div class="definition" id="definition:polyhedra" data-name="polyhedra">
	
intersection of finite number of hyperplanes and half spaces,
called <span class="define">polyhedron</span>;
every polyhedron can be expressed as

$$
\set{x\in\reals^n}{Ax \preceq b, Cx = d}
$$

for $A\in\reals^{m\times n}$, $b\in\reals^m$, $C\in\reals^{p\times n}$, $d\in\reals^p$

</div>
<ul>
<li>
	polyhedron is convex set (by <a href="#proposition:convexity---preserving---set---operations"></a>)

</li>
</ul>

<h3>Convexity preserving set operations</h3>

<div class="proposition" id="proposition:convexity---preserving---set---operations" data-name="convexity preserving set operations">
	


	<ul>
	<li>
		intersection preserves convexity
		<ul>
		<li>
			for (any) collection of convex sets, $\coll$,

$$
\bigcap_{C\in\coll} C
$$
 is convex set


		</li>
		</ul>

	</li>
	<li>
		scalar scaling preserves convexity
		<ul>
		<li>
			for convex set $C$

$$
\alpha C
$$
 is convex set for any $\alpha\in\reals$

		</li>
		</ul>

	</li>
	<li>
		sum preserves convexity
		<ul>
		<li>
			for convex sets $C$ and $D$

$$
C+D
$$
 is convex set

		</li>
		</ul>

	</li>
	<li>
		direct product preserves convexity
		<ul>
		<li>
			for convex sets $C$ and $D$

$$
C\times D
$$
 is convex set

		</li>
		</ul>

	</li>
	<li>
		projection preserves convexity
		<ul>
		<li>
			for convex set $C\subset A \times B$

$$
\set{x\in A}{(\exists y)((x,y)\in C)}
$$

is convex

		</li>
		</ul>

	</li>
	<li>
		image and inverse image by affine function preserve convexity
		<ul>
		<li>
			for affine function $f:A\to B$ and convex sets $C\subset A$ and $D\subset B$

$$
f(C) \;\& \; f^{-1}(D)
$$

are convex

		</li>
		</ul>

	</li>
	<li>
		image and inverse image by linear-fractional function preserve convexity
		<ul>
		<li>
			for convex sets $C\subset \reals^n, D\subset \reals^m$
and
linear-fractional function, $g:\reals^n\to\reals^m$,
<i>i.e.</i>, function defined by $g(x) = (Ax+b)/(c^Tx+d)$
for $A\in\reals^{m\times n}$, $b\in\reals^m$, $c\in\reals^n$, and $d\in\reals$

$$
g(C) \ \& \ g^{-1}(D)
$$

are convex

		</li>
		</ul>

	</li>
	</ul>

</div>


<h3>Proper cones and generalized inequalities</h3>

<div class="definition" id="definition:proper---cones" data-name="proper cones">
	
closed convex cone $K$ which is

	<ul>
	<li>
		solid, <i>i.e.</i>, $\interior{K}\neq \emptyset$

	</li>
	<li>
		pointed, <i>i.e.</i>, $x\in vK$ and $-x\in K$ imply $x=0$

	</li>
	</ul>

called <span class="define">proper cone</span>

</div>
<ul>
<li>
	examples of proper cones:
$\prealk{n}$ and $\possemidefset{n}$

</li>
</ul>
<div class="definition" id="definition:generalized---inequalities" data-name="generalized inequalities">
	
proper cone $K$
defines <span class="define">generalized inequalities</span>


	<ul>
	<li>
		(nonstrict) generalized inequality

$$
x \preceq_K y
\Leftrightarrow
y - x\in K
$$


	</li>
	<li>
		strict generalized inequality

$$
x \prec_K y
\Leftrightarrow
y - x\in \interior{K}
$$


	</li>
	</ul>

</div>
<ul>
<li>
	$\preceq_K$ and $\prec_K$ are partial orderings

</li>
</ul>

<h3>Convex sets induced by generalized inequalities</h3>

<ul>
<li>
	for affine function $g:\reals^n\to\symset{m}$,
<i>i.e.</i>, $f(x)=A_0 + A_1 x_1 + \cdots + A_n x_n$
for some $A_0,\ldots,A_n\in\symset{m}$,
$f^{-1}(\possemidefset{n})$ is convex (by <a href="#proposition:convexity---preserving---set---operations"></a>),
<i>i.e.</i>,

$$
\set{x\in\reals^n}{A_0 + A_1 x_1 + \cdots + A_n x_n \succeq 0} \subset \reals^n
$$

is convex

</li>
<li>
	can negate each matrix $A_i$ and have same results,
hence

$$
\set{x\in\reals^n}{A_0 + A_1 x_1 + \cdots + A_n x_n \preceq 0} \subset \reals^n
$$

is (also) convex

</li>
</ul>


<h3>Separating and supporting hyperplanes</h3>

<div class="theorem" id="theorem:separating---hyperplane---theorem" data-name="separating hyperplane theorem">
	
for nonempty disjoint convex sets $C$ and $D$,
exists hyperplane which separates $C$ and $D$,
<i>i.e.</i>

$$
\left(
\exists a\neq0\in\reals^n, b\in\reals
\right)
\left(
\forall x\in C, y\in D
\right)
\left(
a^T x + b \geq 0
\ \& \
a^T y + b \leq 0
\right)
$$


</div>
<div class="definition" id="definition:separating---hyperplanes" data-name="separating hyperplanes">
	
for nonempty disjoint convex sets $C$ and $D$,
hyperplane satisfying property in <a href="#theorem:separating---hyperplane---theorem"></a>,
called <span class="define">separating hyperplane</span>,
said to <span class="define">separate $C$ and $D$</span>

</div>
<div class="theorem" id="theorem:supporting---hyperplane---theorem" data-name="supporting hyperplane theorem">
	
for nonempty convex set $C$
and $x\in \boundary C$,
exists hyperplane passing through $x$,
<i>i.e.</i>,

$$
\left(
\exists a\neq0\in\reals^n
\right)
\left(
\forall y\in C
\right)
\left(
a^T(y-x) \leq 0
\right)
$$


</div>
<div class="definition" id="definition:supporting---hyperplanes" data-name="supporting hyperplanes">
	
for nonempty convex set $C$
and $x\in \boundary C$,
hyperplane satisfied property in <a href="#theorem:supporting---hyperplane---theorem"></a>,
called <span class="define">supporting hyperplane</span>

</div>

<h3>Dual cones</h3>



<div class="definition" id="definition:dual---cones" data-name="dual cones">
	
for cone $K$,

$$
\set{x}{\forall y \in K, y^Tx\geq 0 }
$$

called <span class="define">dual cone of $K$</span>,
denoted by <span class="notation">$K^\ast$</span>

</div>
<ul>
<li>
	the figure illustrates $x \in K^\ast$ while $z\not\in K^\ast$

</li>
</ul>



&nbsp;


<div id="fig:dual---cone"></div>



<h3>Dual norms</h3>

<div class="definition" id="definition:dual---norms" data-name="dual norms">
	
for norm $\|\cdot\|$,
fudnction defined by

$$
y \mapsto \sup \set{y^Tx}{\|x\|\leq 1}
$$

called <span class="define">dual norm of $\|\cdot\|$</span>,
denoted by <span class="notation">$\|\cdot\|_\ast$</span>

</div>
<ul>
<li>
	examples
	<ul>
	<li>
		dual cone of subspace $V\subset \reals^n$
is orthogonal complement of $V$, $V^\perp$,
where
$V^\perp=\set{y}{\forall v\in V,v^Ty = 0}$

	</li>
	<li>
		$\prealk{n}$ and $\possemidefset{n}$ are self-dual

	</li>
	<li>
		<i>dual of norm cone</i> is <i>norm cone associated with dual norm</i>,
<i>i.e.</i>,
if $K=\set{(x,t)\in\reals^{n} \times \reals}{\|x\|\leq t}$

$$
K=\set{(y,u)\in\reals^{n} \times \reals}{\|y\|_\ast\leq u}
$$


	</li>
	</ul>

</li>
</ul>

<h3>Properties of dual cones</h3>

<div class="proposition" id="proposition:properties---of---dual---cones" data-name="properties of dual cones">
	
for cones $K$, $K_1$, and $K_2$

	<ul>
	<li>
		$K^\ast$ is closed and convex

	</li>
	<li>
		$K_1\subset K_2 \Rightarrow K_2^\ast \subset K_1^\ast$

	</li>
	<li>
		if $\interior{K} \neq \emptyset$, $K^\ast$ is pointed

	</li>
	<li>
		if $\closure{K}$ is pointed, $\interior{(K^\ast)} \neq \emptyset$

	</li>
	<li>
		$K^{\ast\ast}=(K^\ast)^\ast$ is closure of convex hull of $K$,

	</li>
	<li>
		$K^\ast$ is closed and convex

	</li>
	</ul>

thus,

	<ul>
	<li>
		if $K$ is closed and convex, $K^{\ast\ast} = K$

	</li>
	<li>
		dual of proper cone is proper cone

	</li>
	<li>
		for proper cone $K$, $K^{\ast\ast}=K$

	</li>
	</ul>

</div>

<h3>Dual generalized inequalities</h3>

<ul>
<li>
	dual of proper cone is proper (<a href="#proposition:properties---of---dual---cones"></a>),
hence the dual also induces generalized inequalities

</li>
</ul>
<div class="proposition" id="proposition:">
	
<div id="proposition:generalized---inequalities---and---dual---generalized---inequalities"></div>
for proper cone $K$,

	<ul>
	<li>
		$x\preceq_K y$ if and only if $(\forall \lambda \succeq_{K^\ast} 0)(\lambda^T x \leq \lambda^T y)$

	</li>
	<li>
		$x\prec_K y$ if and only if $(\forall \lambda \succeq_{K^\ast} 0 \mbox{ with } \lambda\neq0)(\lambda^T x < \lambda^T y)$

	</li>
	</ul>
$K^{\ast\ast} = K$,
hence
above are equivalent to

	<ul>
	<li>
		$x\preceq_{K^\ast} y$ if and only if $(\forall \lambda \succeq_{K} 0)(\lambda^T x \leq \lambda^T y)$

	</li>
	<li>
		$x\prec_{K^\ast} y$ if and only if $(\forall \lambda \succeq_{K} 0 \mbox{ with } \lambda\neq0)(\lambda^T x < \lambda^T y)$

	</li>
	</ul>

</div>

<h3>Theorem of alternative for linear strict generalized inequalities</h3>

<div class="theorem" id="theorem:theorem---of---alternative---for---linear---strict---generalized---inequalities" data-name="theorem of alternative for linear strict generalized inequalities">
	
for
proper cone $K\subset \reals^m$,
$A\in\reals^{m\times n}$,
and
$b\in\reals^m$,

$$
Ax \prec_K b
$$

is infeasible if and only if
exist nonzero $\lambda\in\reals^m$
such that

$$
\lambda \neq0,\
\lambda \succeq_{K^\ast} 0,\
A^T \lambda = 0,\
\lambda^T b \leq0
$$

Above two inequality systems are <i>alternative</i>,
<i>i.e.</i>, for any data, $A$ and $b$,
exactly one of them is feasible.


</div>

<h2 id="title-page:Convex---Functions">Convex Functions</h2>


<h3>Convex functions</h3>

<div class="definition" id="definition:convex---functions" data-name="convex functions">
	


	<ul>
	<li>
		function $f:\reals^n\to\reals$
the domain of which is convex
and which satisfies

$$
\left(
\forall x,y\in \dom f, 0\leq \theta \leq 1
\right)
\left(
f(\theta x + (1-\theta) y)
\leq
\theta f(x) + (1-\theta) f(y)
\right)
$$

said to be <span class="define">convex</span>

	</li>
	<li>
		function $f:\reals^n\to\reals$
the domain of which is convex
and which satisfies

$$
\left(
\forall \mbox{ distinct } x,y\in \dom f, 0< \theta < 1
\right)
\left(
f(\theta x + (1-\theta) y)
<
\theta f(x) + (1-\theta) f(y)
\right)
$$

said to be <span class="define">strictly convex</span>

	</li>
	</ul>

</div>
<div class="definition" id="definition:concave---functions" data-name="concave functions">
	


	<ul>
	<li>
		function $f:\reals^n\to\reals$
the domain of which is convex
where $-f$ is convex,
said to be <span class="define">concave</span>

	</li>
	<li>
		function $f:\reals^n\to\reals$
the domain of which is convex
where $-f$ is strictly convex,
said to be <span class="define">strictly concave</span>

	</li>
	</ul>

</div>

<h3>Extended real-value extensions of convex functions</h3>

<div class="definition" id="definition:extended---real-value---extension---of---convex---functions" data-name="extended real-value extension of convex functions">
	
for convex function $f$,
function
$\tilde{f}: \reals^n \to \reals\cup\{\infty\}$
defined by

$$
\tilde{f}(x)
=
\left\{\begin{array}{ll}
f(x) &\mbox{if } x \in \dom f
\\
\infty &\mbox{if } x \not\in \dom f
\end{array}\right.
$$

called <span class="define">extended real-value extension of $f$</span>

</div>
<ul>
<li>
	using extended real-value extensions of convex functions,
can drop &ldquo;$\dom f$'' in equations,
<i>e.g.</i>,
	<ul>
	<li>
		$f$ is convex if and only if its extended-value extension $\tilde{f}$ satisfies

$$
\left(
\forall x,y\in \dom f, 0\leq \theta \leq 1
\right)
\left(
f(\theta x + (1-\theta) y)
\leq
\theta f(x) + (1-\theta) f(y)
\right)
$$


	</li>
	<li>
		$f$ is strictly convex if and only if its extended-value extension $\tilde{f}$ satisfies

$$
\left(
\forall \mbox{ distinct } x,y\in \dom f, 0< \theta < 1
\right)
\left(
f(\theta x + (1-\theta) y)
<
\theta f(x) + (1-\theta) f(y)
\right)
$$


	</li>
	</ul>

</li>
</ul>

<h3>First-order condition for convexity</h3>

<div class="theorem" id="theorem:first-order---condition---for---convexity" data-name="first-order condition for convexity">
	
differentiable $f$,
<i>i.e.</i>, $\dom f$ is open
and gradient $\nabla f$ exists at every point in $\dom f$,
is

	<ul>
	<li>
		convex if and only if $\dom f$ is convex
and

$$
\left(
\forall x,y\in \dom f
\right)
\left(
f(y) \geq f(x) + \nabla f(x) ^T (y-x)
\right)
$$


	</li>
	<li>
		strictly convex if and only if $\dom f$ is convex
and

$$
\left(
\forall \mbox{ distinct } x,y\in \dom f
\right)
\left(
f(y) > f(x) + \nabla f(x) ^T (y-x)
\right)
$$


	</li>
	</ul>

</div>
<ul>
<li>
	<a href="#theorem:first-order---condition---for---convexity"></a>
implies
that
for convex function $f$
	<ul>
	<li>
		first-order Taylor approximation is <i>global underestimator</i>

	</li>
	<li>
		can derive
global information
from
local information
		<ul>
		<li>
			<i>e.g.</i>, if $\nabla f(x)=0$, $x$ is global minimizer

		</li>
		<li>
			<span class="eemph">explains remarkable properties of convex functions and convex optimization problems</span>

		</li>
		</ul>

	</li>
	</ul>

</li>
</ul>

<h3>Second-order condition for convexity</h3>

<div class="theorem" id="theorem:second-order---condition---for---convexity" data-name="second-order condition for convexity">
	
twice-differentiable $f$,
<i>i.e.</i>, $\dom f$ is open
and Hessian $\nabla^2 f$ exists at every point in $\dom f$,
is
convex if and only if $\dom f$ is convex
and

$$
\left(
\forall x\in \dom f
\right)
\left(
\nabla^2 f(x) \succeq 0
\right)
$$

	<ul>
	<li>
		if $\dom f$ is convex and

$$
\left(
\forall x\in \dom f
\right)
\left(
\nabla^2 f(x) \succ 0
\right)
$$

it is strictly convex

	</li>
	</ul>

</div>

<h3>Convex function examples</h3>

<ul>
<li>
	assume function $f:\reals^n\to\reals$
and $\dom f =\reals^n$
unlesss specified otherwise

</li>
<li>
	affine function, <i>i.e.</i>, $f(x)=a^Tx +b$ for some $a\in\reals^n$ and $b\in\reals$, is convex

</li>
<li>
	quadratic functions
- if $f(x) = x^T Px + q^Tx$
for some $P\in\symset{n}$ and $q\in\reals^n$
	<ul>
	<li>
		$f$ is convex if and only if $P\succeq0$

	</li>
	<li>
		$f$ is strictly convex if and only if $P\succ0$

	</li>
	</ul>

</li>
<li>
	exponential function,
<i>i.e.</i>, $f(x) = \exp(a^Tx+b)$ for some $a\in\reals^n$ and $b\in\reals$,
is convex

</li>
<li>
	power,
<i>i.e.</i>, $f(x) = x^a$ for some $a\geq1$,
is convex on $\ppreals$

</li>
<li>
	power of absolute value,
<i>i.e.</i>, $f(x) = |x|^a$ for some $a\geq1$,
is convex on $\reals$

</li>
<li>
	logarithm function,
<i>i.e.</i>, $f(x) = \log x$,
is concave on $\ppreals$

</li>
<li>
	negative entropy,
<i>i.e.</i>,

$$
f(x) = \left\{\begin{array}{ll}
x\log x & \mbox{if } x >0
\\
0 &\mbox{if } x=0
\end{array}\right.
$$

is convex on $\preals$

</li>
<li>
	norm as function is convex
(by definition of norms,
<i>i.e.</i>, triangle inequality &amp; absolute homogeneity)

</li>
<li>
	max function,
<i>i.e.</i>, $f(x)=\max(x_1,\ldots,x_n\}$,
is convex

</li>
<li>
	quadratic-over-linear function,
$f(x,y) = x^2/y$,
is convex on $\reals\times \ppreals$

</li>
<li>
	log-sum-exp,
$f(x) = \log(\exp(x_1)+\cdots+\exp(x_n))$,
is convex

</li>
<li>
	geometric mean,
$f(x) = (\prod_{i=1}^n x_i )^{1/n}$,
is concave on $\pprealk{n}$

</li>
<li>
	log-determinant,
$f(X) = \log \det X$,
is concave on $\posdefset{n}$

</li>
</ul>

<h3>Sublevel sets and superlevel sets</h3>

<div class="definition" id="definition:sublevel---sets" data-name="sublevel sets">
	
for function $f$ and $\alpha\in\reals$,

$$
\set{x\in\dom f}{f(x)\leq \alpha}
$$

called <span class="define">$\alpha$-sublevel set of $f$</span>

</div>
<div class="definition" id="definition:superlevel---sets" data-name="superlevel sets">
	
for function $f$ and $\alpha\in\reals$,

$$
\set{x\in\dom f}{f(x)\geq \alpha}
$$

called <span class="define">$\alpha$-superlevel set of $f$</span>

</div>
<div class="proposition" id="proposition:convexity---of---level---sets" data-name="convexity of level sets">
	


	<ul>
	<li>
		every sublevel set of convex function is convex

	</li>
	<li>
		and every superlevel set of concave function is convex

	</li>
	</ul>

</div>
<ul>
<li>
	note, however, converse is not true
	<ul>
	<li>
		<i>e.g.</i>, every sublevel set of $\log$ is convex, but $\log$ is concave

	</li>
	</ul>

</li>
</ul>


<h3>Epigraphs and hypographs</h3>

<div class="definition" id="definition:epigraphs" data-name="epigraphs">
	
for function $f$,

$$
\set{(x,t)}{x\in\dom f, f(x)\leq t}
$$

called <span class="define">epigraph of $f$</span>,
denoted by <span class="notation">$\epi f$</span>

</div>
<div class="definition" id="definition:hypographs" data-name="hypographs">
	
for function $f$,

$$
\set{(x,t)}{x\in\dom f, f(x)\geq t}
$$

called <span class="define">hypograph of $f$</span>,
denoted by <span class="notation">$\hypo f$</span>

</div>
<div class="proposition" id="proposition:graphs---and---convexity" data-name="graphs and convexity">
	


	<ul>
	<li>
		function is convex if and only if its epigraph is convex

	</li>
	<li>
		function is concave if and only if its hypograph is convex

	</li>
	</ul>

</div>

<h3>Convexity preserving function operations</h3>

<div class="proposition" id="proposition:convexity---preserving---function---operations" data-name="convexity preserving function operations">
	


	<ul>
	<li>
		nonnegative weighted sum preserves convexity
		<ul>
		<li>
			for convex functions $f_1$, &hellip;, $f_n$ and nonnegative weights $w_1,\ldots, w_n$

$$
w_1 f_1 + \cdots w_n f_n
$$

is convex

		</li>
		</ul>

	</li>
	<li>
		nonnegative weighted integration preserves convexity
		<ul>
		<li>
			for measurable set $Y$,
$w:Y\to\preals$,
and
$f:X \times Y$
where $f(x,y)$ is convex in $x$ for every $y\in Y$
and measurable in $y$ for every $x\in X$

$$
\int_Y w(y) f(x,y) dy
$$

is convex

		</li>
		</ul>

	</li>
	<li>
		pointwise maximum preserves convexity
		<ul>
		<li>
			for convex functions $f_1$, &hellip;, $f_n$

$$
\max\{f_1, \ldots, f_n\}
$$

is convex

		</li>
		</ul>

	</li>
	<li>
		pointwise supremum preserves convexity
		<ul>
		<li>
			for indexed family of convex functions $\indexedcol{f_\lambda}_{\lambda\in\Lambda}$

$$
\sup_{\lambda \in \Lambda} f_\lambda
$$

is convex
(one way to see this is $\epi \sup_\lambda f_\lambda = \bigcap_\lambda \epi f_\lambda$)

		</li>
		</ul>

	</li>
	<li>
		composition
<div id="page:convexity---preserving---operation-------composition"></div>
		<ul>
		<li>
			suppose $g:\reals^n\to\reals^k$, $h:\reals^k\to\reals$, and $f=h\circ g$
			<ul>
			<li>
				$f$ convex if $h$ convex &amp; nondecreasing in each argument, and $g_i$ convex

			</li>
			<li>
				$f$ convex if $h$ convex &amp; nonincreasing in each argument, and $g_i$ concave

			</li>
			<li>
				$f$ concave if $h$ concave &amp; nondecreasing in each argument, and $g_i$ concave

			</li>
			<li>
				$f$ concave if $h$ concave &amp; nonincreasing in each argument, and $g_i$ convex

			</li>
			</ul>

		</li>
		</ul>

	</li>
	<li>
		minimization
		<ul>
		<li>
			for function $f(x,y)$ convex in $(x,y)$ and convex set $C$

$$
\inf_{y\in C} f(x,y)
$$

is convex provided it is bounded below where domain is $\set{x}{(\exists y\in C)((x,y) \in \dom f)}$


		</li>
		</ul>

	</li>
	<li>
		perspective of convex function preserves convexity
		<ul>
		<li>
			for convex function $f:X\to\reals$,
function $g:X\times \reals \to \reals$
defined by

$$
g(x,t) = tf(x/t)
$$

with $\dom g = \set{(x,t)}{x/t \in \dom f, t>0}$
is convex

		</li>
		</ul>

	</li>
	</ul>

</div>

<h3>Convex functions examples</h3>

<a href="#proposition:convexity---preserving---function---operations"></a>
implies

<ul>
<li>
	piecewise-linear function is convex, <i>i.e.</i>
	<ul>
	<li>
		$\max\{a_1^Tx+b_1,\ldots,a_m^T x + b_m\}$
for some $a_i\in\reals^n$ and $b_i\in\reals$
is convex

	</li>
	</ul>

</li>
<li>
	sum of $k$ largest components is convex, <i>i.e.</i>
	<ul>
	<li>
		$x_{[1]} + \cdots + x_{[k]}$
where $x_{[i]}$ denotes $i$-th largest component,
is convex
(since $f(x) = \max\set{x_{i_1}+\cdots+x_{i_r}}{1\leq i_1< i_2<\cdots < i_r\leq n}$)

	</li>
	</ul>

</li>
<li>
	support function of set, <i>i.e.</i>,
	<ul>
	<li>
		$\sup\set{x^Ty}{y\in A}$
for $A\subset\reals^n$
is convex

	</li>
	</ul>

</li>
<li>
	distance (when measured by arbitrary norm) to farthest point of set
	<ul>
	<li>
		$\sup\set{\|x-y\|}{y\in A}$
for $A\subset\reals^n$
is convex

	</li>
	</ul>

</li>
<li>
	least-squares cost as function of weights
	<ul>
	<li>
		$\inf_{x\in\reals^n} \sum^n_{i=1} w_i(a_i^Tx - b_i)^2$ for some $a_i\in\reals^n$ and $b_i\in\reals$
is concave
		<ul>
		<li>
			note that above function equals to
$\sum_{i=1}^n w_i b_i^2 - \sum_{i=1}^n w_i^2 b_i^2 a_i^T \left( \sum_{j=1}^n w_ja_ja_j^T\right)^{-1} a_i$
but not clear whether it is concave

		</li>
		</ul>

	</li>
	</ul>

</li>
</ul>



<ul>
<li>
	maximum eigenvalue of symmetric matrix
	<ul>
	<li>
		$\lambda_\mathrm{max}(F(x)) = \sup\set{y^TF(x)y}{\|y\|_2 \leq 1}$
where $F:\reals^n\to \symset{m}$
is linear function in $x$

	</li>
	</ul>

</li>
<li>
	norm of matrix
	<ul>
	<li>
		$\sup\set{u^TG(x)v}{\|u\|_2 \leq 1, \|v\|_2\leq1}$
where $G:\reals^n\to \reals^{m\times n}$
is linear function in $x$

	</li>
	</ul>

</li>
<li>
	distance (when measured by arbitrary norm) to convex set
	<ul>
	<li>
		for convex set $C$,
$\inf\set{\|x-y\|}{y\in C}$

	</li>
	</ul>

</li>
<li>
	infimum of convex function
subject to linear constraint
	<ul>
	<li>
		for convex function $h$,
$\inf\set{h(y)}{Ay=x}$ is convex
(since it is $\inf_y (h(y) + I_{Ay=x}(x,y))$)

	</li>
	</ul>

</li>
<li>
	perspective of Euclidean norm squared
	<ul>
	<li>
		map $(x,t) \mapsto x^Tx /t$
induces convex function in $(x,t)$ for $t>0$

	</li>
	</ul>

</li>
<li>
	perspective of negative log
	<ul>
	<li>
		map $(x,t) \mapsto -t \log(x/t)$
induces convex function in $(x,t) \in \pprealk{2}$

	</li>
	</ul>

</li>
</ul>



<ul>
<li>
	perspective of convex function
	<ul>
	<li>
		for convex function $f:\reals^n\to\reals$,
function $g:\reals^n\to\reals$
defined by

$$
g(x) = (c^T x + d) f((Ax+b)/(c^T x + d))
$$

from some $A\in\reals^{m\times n}$, $b\in\reals^m$, $c\in\reals^n$, and $d\in\reals$
with $\dom g = \set{x}{(Ax+b)/(c^Tx + d)\in \dom f, c^T x + d >0}$
is convex

	</li>
	</ul>

</li>
</ul>

<h3>Conjugate functions</h3>

<div class="definition" id="definition:conjugate---functions" data-name="conjugate functions">
	
for function $f$

$$
\sup_{y\in \dom f} (x^Ty - f(y))
$$

called <span class="define">conjugate function of $f$</span>,
denoted by <span class="notation">$f^\ast$</span>

</div>

<ul>
<li>
	conjugate function is convex for any function $f$
because it is supremum
of linear (hence convex) functions (in $x$)
(<a href="#proposition:convexity---preserving---function---operations"></a>)

</li>
</ul>
<div class="inequality" id="inequality:Fenchel's---inequality" data-name="Fenchel's inequality">
	
definition of conjugate function implies

$$
f(x) + f^\ast(y) \geq x^Ty
$$

sometimes called <i>Young's inequality</i>

</div>

<div class="proposition" id="proposition:conjugate---of---conjugate" data-name="conjugate of conjugate">
	
for convex and closed function $f$

$$
f^{\ast\ast} = f
$$

where closed function $f$ is defined by function with closed $\epi f$

</div>

<h3>Conjugate function examples</h3>

<ul>
<li>
	strictly convex quadratic function
	<ul>
	<li>
		for $f:\reals^n \to \preals$
defined $f(x) = x^TQx/2$ where $Q\in \posdefset{n}$,

$$
f^\ast(x)= \sup_y(y^Tx - y^TQy/2)
= (y^Tx - y^TQy/2)|_{y=Q^{-1}x}
= x^TQ^{-1}x/2
$$

which is also strictly convex quadratic function

	</li>
	</ul>

</li>
<li>
	log-determinant
	<ul>
	<li>
		for
function $f:\posdefset{n} \to \reals$
defined by $f(X) = \log \det X^{-1}$

$$
f^\ast(X)
=
\sup_{Y\in\posdefset{n}} (\Tr XY + \log \det Y)
= \log\det (-X)^{-1} - n
$$

where $\dom f^\ast = -\posdefset{n}$

	</li>
	</ul>

</li>
<li>
	indicator function
	<ul>
	<li>
		for
indicator function $I_A:\reals^n\to\{0,\infty\}$ with $A\subset \reals^n$

$$
I_A^\ast(x) = \sup_y (y^Tx - I_A(y)) = \sup \set{y^Tx}{y\in A}
$$

which is support function of $A$

	</li>
	</ul>

</li>
<li>
	log-sum-exp function
	<ul>
	<li>
		for
function $f: \reals^n \to \reals$
defined by $f(x) = \log(\sum_{i=1}^n \exp(x_i))$

$$
f^\ast(x) =
\sum_{i=1}^n x_i \log x_i + I_{x\succeq 0, \ones^T x = 1}(x)
$$


	</li>
	</ul>

</li>
<li>
	norm
	<ul>
	<li>
		for norm function $f:\reals^n\to\preals$ defined by $f(x)=\|x\|$

$$
f^\ast(x)
=
\sup_y( {y^Tx - \|y\|})
= I_{\|x\|_\ast\leq1}(x)
$$


	</li>
	</ul>

</li>
<li>
	norm squared
	<ul>
	<li>
		for
function $f: \reals \to \preals$
defined by $f(x) = \|x\|^2/2$

$$
f^\ast(x) = \|x\|_\ast^2/2
$$


	</li>
	</ul>

</li>
<li>
	differentiable convex function
	<ul>
	<li>
		for
differentiable convex function $f:\reals^n\to\reals$

$$
f^\ast(x)=
(y^\ast)^T \nabla f(y^\ast) - f(y^\ast)
$$

where $y^\ast = \argsup_y (x^Ty-f(y))$

	</li>
	</ul>

</li>
<li>
	sum of independent functions
	<ul>
	<li>
		for
function $f:\reals^n\times \reals^m \to \reals$ defined by $f(x,y) = f_1(x) + f_2(y)$
where $f_1:\reals^n\to\reals$ and $f_2:\reals^m\to\reals$

$$
f^\ast(x,y) = f_1^\ast(x) + f_2^\ast(y)
$$


	</li>
	</ul>

</li>
</ul>

<h3>Convex functions \wrt\ generalized inequalities</h3>

<div class="definition" id="definition:$K$-convex---functions" data-name="$K$-convex functions">
	
for proper cone $K$,

	<ul>
	<li>
		function $f$ satisfying

$$
\left(
\forall x,y \in \dom f, 0\leq \theta\leq 1
\right)
\left(
f(\theta x + (1-\theta) y)
\preceq_K
\theta f(x) + (1-\theta) f(y)
\right)
$$

called <span class="define">$K$-convex</span>

	</li>
	<li>
		function $f$ satisfying

$$
\left(
\forall x\neq y \in \dom f, 0< \theta< 1
\right)
\left(
f(\theta x + (1-\theta) y)
\prec_K
\theta f(x) + (1-\theta) f(y)
\right)
$$

called <span class="define">strictly $K$-convex</span>

	</li>
	</ul>

</div>
<div class="proposition" id="proposition:dual---characterization---of---$K$-convexity" data-name="dual characterization of $K$-convexity">
	
for proper cone $K$

	<ul>
	<li>
		function $f$ is $K$-convex if and only if for every $w\succeq_{K^\ast}0$, $w^Tf$ is convex

	</li>
	<li>
		function $f$ is strictly $K$-convex if and only if for every nonzero $w\succeq_{K^\ast}0$, $w^Tf$ is strictly convex

	</li>
	</ul>

</div>

<h3>Matrix convexity</h3>

<div class="definition" id="definition:matrix---convexity" data-name="matrix convexity">
	
function of $\reals^n$ into $\symset{m}$
which is $K$-convex where $K=\possemidefset{m}$,
called <span class="define">matrix convex</span>

</div>
<ul>
<li>
	examples of matrix convexity
	<ul>
	<li>
		function of $\reals^{n\times m}$ into $\possemidefset{n}$
defined by $X\mapsto XX^T$
is matrix convex

	</li>
	<li>
		function of $\posdefset{n}$ into itself
defined by $X\mapsto X^p$
is matrix convex for $1\leq p\leq 2$ or $-1\leq p \leq0$,
and matrix concave for $0\leq p\leq1$

	</li>
	<li>
		function of $\symset{n}$ into $\posdefset{n}$
defined by $X\mapsto \exp(X)$
is <i>not</i> matrix convex

	</li>
	<li>
		quadratic matrix function of $\reals^{m\times n}$ into $\symset{n}$
defined by $X\mapsto X^TAX + B^TX + X^TB + C$
for $A\in\symset{m}$, $B\in\reals^{m\times n}$, and $C\in\symset{n}$
is matrix convex when $A\succeq0$

	</li>
	</ul>

</li>
</ul>


<h2 id="title-page:Convex---Optimization---Problems">Convex Optimization Problems</h2>


<h3>Optimization problems</h3>

<div class="definition" id="definition:optimization---problems" data-name="optimization problems">
	
for $\fobj:\xobj \to \reals$, $\fie: \xie\to \reals^m$, $\feq: \xeq \to \reals^p$
where $\xobj$, $\xie$, and $\xeq$ are subsets of common set $\xdomain$

$$
\begin{array}{ll}
\mbox{minimize}
& \fobj(x)
\\
\mbox{subject to}
& \fie(x) \preceq 0
\\
& \feq(x) =0
\end{array}
$$

called <span class="define">optimization problem</span>
where $x$ is <span class="define">optimization variable</span>

	<ul>
	<li>
		$\fobj$, $\fie$, and $\feq$ are
<span class="define">objective function</span>,
<span class="define">inequality \& equality contraint function</span>

	</li>
	<li>
		$\fie(x) \preceq 0$ and $\feq(x) = 0$
are
<span class="define">inequality contraints</span>
and
<span class="define">equality contraints</span>

	</li>
	<li>
		$\optdomain = \xobj \cap \xie \cap \xeq$ is <span class="define">domain</span> of optimization problem

	</li>
	<li>
		$\optfeasset =\set{x\in \optdomain}{\fie(x) \preceq0, \feq(x)=0}$, called <span class="define">feasible set</span>,
$x\in\optdomain$, said to be <span class="define">feasible</span> if $x\in\optfeasset$,
optimization problem, said to be <span class="define">feasible</span> if $\optfeasset\neq \emptyset$

	</li>
	<li>
		$p^\ast = \inf\set{\fobj(x)}{x\in\optfeasset}$, called <span class="define">optimal value</span> of optimization problem

	</li>
	<li>
		if optimization problem is <i>infeasible</i>, <span class="define">$p^\ast = \infty$</span>
(following convention that infimum of empty set is $\infty$)

	</li>
	<li>
		if $p^\ast=-\infty$,
optimization problem
said to be <span class="define">unbounded</span>

	</li>
	</ul>

</div>

<h3>Global and local optimalities</h3>

<div class="definition" id="definition:global---optimality" data-name="global optimality">
	
for optimization problem
in <a href="#definition:optimization---problems"></a>

	<ul>
	<li>
		$x\in \optfeasset$ with $\fobj(x) = p^\ast$, called <span class="define">(global) optimal point</span>

	</li>
	<li>
		$X_\mathrm{opt} = \set{x\in \optfeasset}{\fobj(x)=p^\ast}$, called <span class="define">optimal set</span>

	</li>
	<li>
		when $X_\mathrm{opt} \neq \emptyset$, we say optimal value is <span class="define">attained</span> or <span class="define">achieved</span>
and
optimization problem is <span class="define">solvable</span>

	</li>
	</ul>

</div>

<ul>
<li>
	optimization problem is <i>not</i> solvable if $p^\ast = \infty$ or $p^\ast = -\infty$
(converse is not true)

</li>
</ul>
<div class="definition" id="definition:local---optimality" data-name="local optimality">
	
for optimization problem
in <a href="#definition:optimization---problems"></a>
where $\xdomain$ is metric space,
$x\in\optfeasset$ satisfying
$\inf\set{\fobj(z)}{z\in\optfeasset, \rho(z,x)\leq r}$
where $\rho:\xdomain\times \xdomain\to\preals$ is metric,
for some $r>0$, said to be <span class="define">locally optimal</span>,
<i>i.e.</i>,
$x$ solves

$$
\begin{array}{ll}
\mbox{minimize}
& \fobj(z)
\\\mbox{subject to}&
\fie(z) \preceq 0
\\&
\feq(z) =0
\\&
\rho(z,x) \leq r
\end{array}
$$


</div>

<h3>Equivalent optimization problems</h3>

<div class="definition" id="definition:equivalent---optimization---problems" data-name="equivalent optimization problems">
	
two optimization problems
where solving one readily solve the other,
said to be <span class="define">equivalent</span>

</div>
<ul>
<li>
	below two optimization problems are equivalent
	<ul>
	<li>
		
$$
\begin{array}{ll}
\mbox{minimize}
& -x-y
\\
\mbox{subject to}
& 2x+y \leq1
\\
& x+2y \leq1
\end{array}
$$


	</li>
	<li>
		
$$
\begin{array}{ll}
\mbox{minimize}
& -2u-v/3
\\
\mbox{subject to}
& 4u+v/3 \leq1
\\
& 2u+2v/3 \leq1
\end{array}
$$


	</li>
	</ul>

</li>
<li>
	
since if $(x^\ast, y^\ast)$ solves first,
$(u,v)=(x^\ast/2, 3y^\ast)$ solves second,
and if $(u^\ast, v^\ast)$ solves second,
$(x,y)=(2u^\ast, v^\ast/3)$ solves first

</li>
</ul>

<h3>Change of variables</h3>

<ul>
<li>
	given function $\phi:\mathcalfont{Z} \to \xdomain$,
optimization problem in <a href="#definition:optimization---problems"></a>
can be rewritten as

$$
\begin{array}{ll}
\mbox{minimize}
& \fobj(\phi(z))
\\
\mbox{subject to}
& \fie(\phi(z)) \preceq 0
\\
& \feq(\phi(z)) =0
\end{array}
$$

where $z\in\mathcalfont{Z}$ is optimization variable

</li>
<li>
	if $\phi$ is injective and $\optdomain \subset \phi(\mathcalfont{Z})$,
above optimization problem
and
optimization problem in <a href="#definition:optimization---problems"></a>
are equivalent,
<i>i.e.</i>
	<ul>
	<li>
		$X_\mathrm{opt}$ is optimal set of problem in <a href="#definition:optimization---problems"></a>
$\Rightarrow$
$\phi^{-1}(X_\mathrm{opt})$ is optimal set of above problem

	</li>
	<li>
		$Z_\mathrm{opt}$ is optimal set of above problem
$\Rightarrow$
$\phi(Z_\mathrm{opt})$ is optimal set of problem in <a href="#definition:optimization---problems"></a>

	</li>
	</ul>

</li>
<li>
	two optimization problems said to be related by
<span class="define">
change of variable or substitution of variable $x=\phi(z)$
</span>

</li>
</ul>

<h3>Convex optimization</h3>

<div class="definition" id="definition:convex---optimization" data-name="convex optimization">
	
optimization problem in <a href="#definition:optimization---problems"></a>
where $\xdomain$ is Banach space,
<i>i.e.</i>,
complete linear normed vector space,
$\fobj$ &amp; $\fie$ are convex functions,
and
$\feq$ is affine function,
called <span class="define">convex optimization problem</span>

	<ul>
	<li>
		when $\xdomain= \reals^n$, optimization problem can be formulated as

$$
\begin{array}{ll}
\mbox{minimize}
& \fobj(x)
\\
\mbox{subject to}
& \fie(x) \preceq 0
\\
& Ax = b
\end{array}
$$

for some $A\in\reals^{p\times n}$ and $b\in\reals^p$

	</li>
	</ul>

</div>
<ul>
<li>
	domain of convex optimization problem is <i>convex</i>
	<ul>
	<li>
		since
domains of $\fobj$, $\fie$, and $\feq$ are convex (by definition of convex functions)
and intersection of convex sets is convex

	</li>
	</ul>

</li>
<li>
	feasible set of convex optimization problem
is <i>convex</i>
	<ul>
	<li>
		since
sublevel sets of convex functions are convex,
feasible sets for affine function is either empty set, singleton, or affine sets, all of which are convex sets

	</li>
	</ul>

</li>
</ul>

<h3>Optimality conditions for convex optimization problems</h3>

<div class="theorem" id="theorem:local---optimality---implies---global---optimality" data-name="local optimality implies global optimality">
	
for convex optimization problem
(in <a href="#definition:convex---optimization"></a>),
every local optimal point is global optimal point

</div>

<div class="theorem" id="theorem:optimality---conditions---for---convex---optimality---problems" data-name="optimality conditions for convex optimality problems">
	
for convex optimization problem
(in <a href="#definition:convex---optimization"></a>),
when $\fobj$ is differentiable
(<i>i.e.</i>, $\dom \fobj$ is open and $\nabla \fobj$ exists everywhere in $\dom \fobj$)

	<ul>
	<li>
		$x\in\optdomain$ is optimal if and only if $x\in\optfeasset$ and

$$
\left(
\forall y \in \optfeasset
\right)
\left(
\nabla \fobj(x)^T(y-x) \geq0
\right)
$$


	</li>
	<li>
		for unconstrained problems, $x\in\optdomain$ is optimal if and only if 
$$
\nabla \fobj(x)=0
$$


	</li>
	</ul>

</div>


<h3>Optimality conditions for some convex optimization problems</h3>

<ul>
<li>
	unconstrained convex quadratic optimization

$$
\begin{array}{ll}
\mbox{minimize}
& \fobj(x) = (1/2)x^TPx + q^Tx
\end{array}
$$

where $\xobj=\reals^n$ and $P\in\possemidefset{n}$
	<ul>
	<li>
		$x$ is optimal if and only if

$$
\nabla \fobj(x) = Px + q = 0
$$

exist three cases
		<ul>
		<li>
			if $P\in\posdefset{n}$, exists unique optimum $x^\ast = -P^{-1}q$

		</li>
		<li>
			if $q\in\range(P)$, $X_\mathrm{opt}=-P^\dagger q + \nullspace(P)$

		</li>
		<li>
			if $q\not\in\range(P)$, $p^\ast = -\infty$

		</li>
		</ul>

	</li>
	</ul>

</li>
<li>
	analytic centering

$$
\begin{array}{ll}
\mbox{minimize}
& \fobj(x) = - \sum_{i=1}^m \log (b_i-a_i^Tx)
\end{array}
$$

where $\xobj = \set{x\in\reals^n}{Ax \prec b}$
	<ul>
	<li>
		$x$ is optimal if and only if

$$
\nabla \fobj(x) = \sum_{i=1}^m \frac{1}{b_i-a_i^Tx}a_i = 0
$$

exist three cases
		<ul>
		<li>
			exists unique optimum, which happens if and only if $\set{x}{b_i-a_i^Tx}$ is nonempty and bounded

		</li>
		<li>
			exist infinitely many optima, in which case, $X_\mathrm{opt}$ is affine set

		</li>
		<li>
			exists no optimum, which happens if and only if $\fobj$ is unbounded below

		</li>
		</ul>

	</li>
	</ul>

</li>
<li>
	convex optimization problem with equality constraints only

$$
\begin{array}{ll}
\mbox{minimize}
& \fobj(x)
\\
\mbox{subject to}
& Ax =b
\end{array}
$$

where $\xdomain=\reals^n$
	<ul>
	<li>
		$x$ is optimal if and only if

$$
\nabla \fobj(x) \perp \nullspace(A)
$$

or equivalently,
exists $\nu\in\reals^p$
such that

$$
\nabla \fobj(x) = A^T\nu
$$


	</li>
	</ul>

</li>
</ul>

<h3>Linear programming</h3>

<div class="definition" id="definition:linear---programming" data-name="linear programming">
	
convex optimization problem in <a href="#definition:convex---optimization"></a>
with $\xdomain=\reals^n$ and linear $\fobj$ &amp; $\fie$,
called <span class="define">linear program (LP)</span>,
which can be formulated as

$$
\begin{array}{ll}
\mbox{minimize}
& c^Tx
\\
\mbox{subject to}
& Cx \preceq d
\\
& A x =b
\end{array}
$$

where $c\in\reals^n$, $C\in\reals^{m\times n}$, $d\in\reals^m$, $A\in\reals^{p\times n}$, $b\in\reals^p$

	<ul>
	<li>
		can transform above LP into <span class="define">standard form LP</span>

$$
\begin{array}{ll}
\mbox{minimize}
& \tilde{c}^T\tilde{x}
\\
\mbox{subject to}
& \tilde{A}\tilde{x} = \tilde{b}
\\
& \tilde{x} \succeq0
\end{array}
$$


	</li>
	</ul>

</div>

<h3>LP examples</h3>

<ul>
<li>
	diet problem
-
find amount of $n$ different food to minimize purchase cost
while satisfying nutrition requirements
	<ul>
	<li>
		assume exist $n$ food and $m$ nutritions,
$c_i$ is cost of food $i$,
$A_{ji}$ is amount of nutrition $j$ contained in unit quantity of food $i$,
$b_j$ is amount requirement for nutrition $j$

	</li>
	<li>
		diet problem can be formulated as LP

$$
\begin{array}{ll}
\mbox{minimize}
& c^Tx
\\
\mbox{subject to}
& Ax \succeq b
\\
& x\succeq0
\end{array}
$$


	</li>
	</ul>

</li>
<li>
	Chebyshev center of polyhedron
- find largest Euclidean ball contained in polyhedron
	<ul>
	<li>
		assume polyhedron is $\set{x\in\reals^n}{a_i^Tx \leq b_i, i=1,\ldots, m}$

	</li>
	<li>
		problem of finding Chebyshev center of polyhedron can be formulated as LP

$$
\begin{array}{ll}
\mbox{maximize}
& r
\\
\mbox{subject to}
& a_i^T x + r\|a_i\|_2 \leq b_i
\end{array}
$$

where optimization variables are $x\in\reals^n$ and $r\in\reals$

	</li>
	</ul>

</li>
<li>
	piecewise-linear minimization
- minimize maximum of affine functions
	<ul>
	<li>
		assume $m$ affine functions $a_i^Tx + b_i$

	</li>
	<li>
		piecewise-linear minimization problem
can be formulated as LP

$$
\begin{array}{ll}
\mbox{minimize}
& t
\\
\mbox{subject to}
& a_i^Tx + b_ i \leq t,\quad i=1,\ldots,m
\end{array}
$$


	</li>
	</ul>

</li>
<li>
	linear-fractional program

$$
\begin{array}{ll}
\mbox{minimize} &
(
c^T x + d
)
/
(
e^T x + f
)
\\
\mbox{subject to} &
Gx \preceq h
\\ &
Ax = b
\end{array}
$$

	<ul>
	<li>
		if feasible set is nonempty,
can be formulated as LP

$$
\begin{array}{ll}
\mbox{minimize} &
c^T y + dz
\\
\mbox{subject to} &
Gy - hz \preceq0
\\ &
Ay-bz = 0
\\ &
e^Ty + fz = 1
\\ &
z\geq0
\end{array}
$$


	</li>
	</ul>

</li>
</ul>

<h3>Quadratic programming</h3>

<div class="definition" id="definition:quadratic---programming" data-name="quadratic programming">
	
convex optimization problem in <a href="#definition:convex---optimization"></a>
with
$\xdomain=\reals^n$ and
convex quadratic $\fobj$ and linear $\fie$,
called <span class="define">quadratic program (QP)</span>,
which can be formulated as

$$
\begin{array}{ll}
\mbox{minimize}
& (1/2) x^TPx + q^Tx
\\
\mbox{subject to}
& Gx \preceq h
\\
& A x =b
\end{array}
$$

where
$P\in\possemidefset{n}$, $q\in\reals^n$,
$G\in\reals^{m\times n}$, $h\in\reals^m$,
$A\in\reals^{p\times n}$, $b\in\reals^p$

</div>
<ul>
<li>
	when $P=0$, QP reduces to LP,
hence <i>LP is specialization of QP</i>

</li>
</ul>

<h3>QP examples</h3>

<ul>
<li>
	least-squares (LS) problems
	<ul>
	<li>
		LS can be formulated as QP

$$
\begin{array}{ll}
\mbox{minimize} &
\|Ax-b\|_2^2
\end{array}
$$


	</li>
	</ul>

</li>
<li>
	distance between two polyhedra
	<ul>
	<li>
		assume two polyhedra
$\set{x\in\reals^n}{Ax\preceq b, Cx =d}$
and
$\set{x\in\reals^n}{\tilde{A}x\preceq \tilde{b}, \tilde{C}x =\tilde{d}}$

	</li>
	<li>
		problem of finding distance between two polyhedra
can be formulated as QP

$$
\begin{array}{ll}
\mbox{minimize} &
\|x-y\|_2^2
\\
\mbox{subject to} &
Ax\preceq b, \quad Cx =d
\\ &
\tilde{A}y\preceq \tilde{b}, \quad \tilde{C}y =\tilde{d}
\end{array}
$$


	</li>
	</ul>

</li>
</ul>

<h3>Quadratically constrained quadratic programming</h3>

<div class="definition" id="definition:quadratically---constrained---quadratic---programming" data-name="quadratically constrained quadratic programming">
	
convex optimization problem in <a href="#definition:convex---optimization"></a>
with $\xdomain=\reals^n$
and
convex quadratic $\fobj$ &amp; $\fie$,
called <span class="define">quadratically constrained quadratic program (QCQP)</span>,
which can be formulated as

$$
\begin{array}{ll}
\mbox{minimize}
& (1/2) x^TP_0x + q_0^Tx
\\
\mbox{subject to}
& (1/2) x^TP_ix + q_i^Tx + r_i \leq0,\quad i=1,\ldots,m
\\
& A x =b
\end{array}
$$

where
$P_i\in\possemidefset{n}$, $q_i\in\reals^n$, $r_i\in\reals$,
$A\in\reals^{p\times n}$, $b\in\reals^p$

</div>
<ul>
<li>
	when $P_i=0$ for $i=1,\ldots,m$, QCQP reduces to QP,
hence <i>QP is specialization of QCQP</i>

</li>
</ul>

<h3>Second-order cone programming</h3>

<div class="definition" id="definition:second-order---cone---programming" data-name="second-order cone programming">
	
convex optimization problem in <a href="#definition:convex---optimization"></a>
with $\xdomain=\reals^n$
and
linear $\fobj$ and convex $\fie$
of form

$$
\begin{array}{ll}
\mbox{minimize}
& f^T x
\\
\mbox{subject to}
& \|A_ix + b_i\|_2 \leq c_i^T x + d_i,\quad i=1,\ldots,m
\\
& F x =g
\end{array}
$$

where
$f\in\reals^n$,
$A_i\in\reals^{n_i\times n}$, $b_i\in\reals^{n_i}$,
$c_i\in\reals^{n}$, $d_i\in\reals$,
$F\in\reals^{p\times n}$, $g\in\reals^p$
called <span class="define">second-order cone program (SOCP)</span>

</div>
<ul>
<li>
	when $b_i=0$, SOCP reduces to QCQP,
hence <i>QCQP is specialization of SOCP</i>

</li>
</ul>

<h3>SOCP examples</h3>

<ul>
<li>
	robust linear program
-
minimize $c^T x$
while satisfying
$\tilde{a}_i^T x \leq b_i$
for every $\tilde{a}_i \in \set{a_i+P_iu}{\|u\|_2\leq1}$
where $P_i\in\symset{n}$
	<ul>
	<li>
		can be formulated as SOCP

$$
\begin{array}{ll}
\mbox{minimize} &
c^T x
\\
\mbox{subject to} &
a_i^T x + \|P_i^T x\|_2 \leq b_i
\end{array}
$$


	</li>
	</ul>

</li>
<li>
	linear program with random constraints
-
minimize $c^T x$
while satisfying
$\tilde{a}_i^T x \leq b_i$
with probability no less than $\eta$
where $\tilde{a} \sim \normal(a_i,\Sigma_i)$
	<ul>
	<li>
		can be formulated as SOCP

$$
\begin{array}{ll}
\mbox{minimize} &
c^T x
\\
\mbox{subject to} &
a_i^T x + \Phi^{-1}(\eta)\|\Sigma_i^{1/2} x\|_2 \leq b_i
\end{array}
$$


	</li>
	</ul>

</li>
</ul>


<h3>Geometric programming</h3>

<div class="definition" id="definition:monomial---functions" data-name="monomial functions">
	
function $f:\pprealk{n}\to\reals$
defined by

$$
f(x) = cx_1^{a_1} \cdots x_n^{a_n}
$$

where $c>0$ and $a_i\in\reals$,
called <span class="define">monomial function</span>
or simply <span class="define">monomial</span>

</div>
<div class="definition" id="definition:posynomial---functions" data-name="posynomial functions">
	
function $f:\pprealk{n}\to\reals$
which is finite sum of monomial functions,
called <span class="define">posynomial function</span>
or simply <span class="define">posynomial</span>

</div>
<div class="definition" id="definition:geometric---programming" data-name="geometric programming">
	
optimization problem

$$
\begin{array}{ll}
\mbox{minimize} &
\fobj(x)
\\
\mbox{subject to} &
\fie(x) \preceq 1
\\ &
\feq(x) =1
\end{array}
$$

for posynomials $\fobj:\pprealk{n} \to \reals$ &amp; $\fie: \pprealk{n} \to \reals^m$
and monomials $\feq: \pprealk{n} \to \reals^p$,
called <span class="define">geometric program (GP)</span>

</div>

<h3>Geometric programming in convex form</h3>

<ul>
<li>
	geometric program in
<a href="#definition:geometric---programming"></a>
is not convex optimization problem (as it is)

</li>
<li>
	however, can be transformed to equivalent convex optimization problem
by change of variables and transformation of functions

</li>
</ul>
<div class="proposition" id="proposition:geometric---programming---in---convex---form" data-name="geometric programming in convex form">
	
geometric program (in <a href="#definition:geometric---programming"></a>)
can be transformed to equivalent convex optimization problem

$$
\begin{array}{ll}
\mbox{minimize} &
\log\left(
\sum_{k=1}^{K_0} \exp((a^{(0)}_k)^T y + b^{(0)}_k)
\right)
\\
\mbox{subject to} &
\log\left(
\sum_{k=1}^{K_i} \exp((a^{(i)}_k)^T y + b^{(i)}_k)
\right)
\leq0
\quad
i=1,\ldots,m
\\ &
Gy = h
\end{array}
$$

for some $a^{(i)}_k\in\reals^n$, $b^{(i)}_k\in\reals$, $G\in\reals^{p\times n}$, $h\in\reals^p$
where optimization variable is $y=\log(x)\in\reals^n$

</div>

<h3>Convex optimization with generalized inequalities</h3>

<div class="definition" id="definition:convex---optimization---with---generalized---inequality---constraints" data-name="convex optimization with generalized inequality constraints">
	
convex optimization problem in <a href="#definition:convex---optimization"></a>
with inequality constraints replaced by generalized inequality constraints,
<i>i.e.</i>

$$
\begin{array}{ll}
\mbox{minimize}
& \fobj(x)
\\
\mbox{subject to}
& \fie_i(x) \preceq_{K_i} 0\quad i=1,\ldots,q
\\
& \feq(x) = 0
\end{array}
$$

where
$K_i\subset R^{k_i}$ are proper cones
and
$\fie_i:\xie_i\to\reals^{k_i}$ are $K_i$-convex,
called <span class="define">convex optimization problem with generalized inequality constraints</span>

</div>

<ul>
<li>
	problem in <a href="#definition:convex---optimization---with---generalized---inequality---constraints"></a>
reduces to convex optimization problem in <a href="#definition:convex---optimization"></a>
when $q=1$ and $K_1=\prealk{m}$,
hence <i>convex optimization is specialization of convex optimization with generalized inequalities</i>

</li>
<li>
	like convex optimization
	<ul>
	<li>
		feasible set is $\optfeasset = \set{x\in\optdomain}{\fie_i(x)\preceq_{K_i} 0, Ax=b}$ is convex

	</li>
	<li>
		local optimality implies global optimality

	</li>
	<li>
		optimality conditions in
<a href="#theorem:optimality---conditions---for---convex---optimality---problems"></a>
applies without modification

	</li>
	</ul>

</li>
</ul>


<h3>Conic programming</h3>

<div class="definition" id="definition:conic---programming" data-name="conic programming">
	
convex optimization problem with generalized inequality constraints
in <a href="#definition:convex---optimization---with---generalized---inequality---constraints"></a>
with linear $\fobj$ and one affine $\fie$

$$
\begin{array}{ll}
\mbox{minimize}
& \fobj(x)
\\
\mbox{subject to}
& \fie(x) \preceq_{K} 0
\\
& \feq(x) = 0
\end{array}
$$

called <span class="define">conic program (CP)</span>

	<ul>
	<li>
		can transform above CP to <span class="define">standard form CP</span>

$$
\begin{array}{ll}
\mbox{minimize}
& \tildefobj(X)
\\
\mbox{subject to}
& \tildefeq (X) = 0
\\
& X \succeq_{K} 0
\end{array}
$$


	</li>
	</ul>

</div>
<ul>
<li>
	cone program is one of simplest convex optimization problems
with generalized inequalities

</li>
</ul>

<h3>Semidefinite programming</h3>

<div class="definition" id="definition:semidefinite---programming" data-name="semidefinite programming">
	
conic program in <a href="#definition:conic---programming"></a>
with $\xdomain=\reals^n$ and $K=\possemidefset{n}$

$$
\begin{array}{ll}
\mbox{minimize} &
c^Tx
\\
\mbox{subject to} &
x_1F_1 + \cdots + x_nF_n + G \preceq 0
\\ &
Ax = b
\end{array}
$$

where $F_1,\ldots,F_n,G\in\symset{k}$ and $A\in\reals^{p\times n}$,
called <span class="define">semidefinite program (SDP)</span>

	<ul>
	<li>
		above inequality, called <span class="define">linear matrix inequality (LMI)</span>

	</li>
	<li>
		can transform SDP to standard form SDP

$$
\begin{array}{ll}
\mbox{minimize} &
\Tr (CX)
\\
\mbox{subject to} &
\Tr (A_iX) = b_i\quad i=1,\ldots,p
\\ &
X \succeq 0
\end{array}
$$

where $\xdomain=\possemidefset{n}$ and $C,A_1,\ldots,A_p\in\symset{n}$ and $b_i\in\reals$

	</li>
	</ul>

</div>

<h3>SDP examples</h3>

<ul>
<li>
	LP
	<ul>
	<li>
		if $k=m$, $F_i=\diag(C_{1,i}, \ldots, C_{m,i})$, $G=-\diag(d_1,\ldots, d_m)$
in <a href="#definition:semidefinite---programming"></a>,
SDP reduces to LP in <a href="#definition:linear---programming"></a>

	</li>
	<li>
		hence, LP is specialization of SDP

	</li>
	</ul>

</li>
<li>
	SOCP
	<ul>
	<li>
		SOCP in <a href="#definition:second-order---cone---programming"></a>
is equivalent to

$$
\begin{array}{ll}
\mbox{minimize} &
f^T x
\\
\mbox{subject to} &
Fx = g
\\ &
\begin{my-matrix}{cc}
c_i^Tx + d_i & x^TA_i^T + b_i^T
\\
A_ix + b_i & (c_i^Tx + d_i)I_{n_i}
\end{my-matrix}
\succeq 0
\quad
i=1,\ldots,m
\end{array}
$$

which can be transformed to SDP in <a href="#definition:semidefinite---programming"></a>,
thus, SDP reduces to SOCP

	</li>
	<li>
		hence, SOCP is specialization of SDP

	</li>
	</ul>

</li>
</ul>

<h3>Determinant maximization problems</h3>

<div class="definition" id="definition:determinant---maximization---problems" data-name="determinant maximization problems">
	
convex optimization problem with generalized inequality constraints
in <a href="#definition:convex---optimization---with---generalized---inequality---constraints"></a>
with $\xdomain=\reals^n$
of form

$$
\begin{array}{ll}
\mbox{minimize} &
-\log \det (x_1C_1 + \cdots + x_n C_n + D)
+c^Tx
\\
\mbox{subject to} &
x_1F_1 + \cdots + x_nF_n + G \preceq 0
\\ &
-x_1C_1 - \cdots - x_nC_n - D \prec 0
\\ &
Ax = b
\end{array}
$$

where
$c\in\reals^n$,
$C_1,\ldots,C_n,D\in\symset{l}$,
$F_1,\ldots,F_n,G\in\symset{k}$,
and
$A\in\reals^{p\times n}$,
called <span class="define">determinant maximization problem</span>
or simply <span class="define">max-det problem</span>
(since it maximizes determinant of (positive definite) matrix with constraints)

</div>
<ul>
<li>
	if $l=1$, $C_1=\cdots=C_n=0$, $D=1$,
max-det problem reduces to SDP,
hence <i>SDP is specialization of max-det problem</i>

</li>
</ul>

<h3>Diagrams for containment of convex optimization problems</h3>

<ul>
<li>
	the figure
shows
containment relations among convex optimization problems

</li>
<li>
	vertical lines ending with filled circles indicate existence of direct reductions,
<i>i.e.</i>, optimization problem transformations to special cases

</li>
</ul>










<div id="fig:diagrams---for---containment---of---convex---optimization---problems"></div>



<h2 id="title-page:Duality">Duality</h2>


<h3>Lagrangian</h3>

<div class="definition" id="definition:Lagrangian" data-name="Lagrangian">
	
for optimization problem in <a href="#definition:optimization---problems"></a>
with nonempty domain $\optdomain$,
function $L:\optdomain \times \reals^m \times \reals^p \to \reals$
defined by

$$
L(x,\lambda, \nu) = \fobj(x) + \lambda^T \fie(x) + \nu^T \feq(x)
$$

called <span class="define">Lagrangian</span> associated with the optimization problem
where

	<ul>
	<li>
		$\lambda$, called <span class="define">Lagrange multiplier associated inequality constraints</span> $\fie(x)\preceq0$

	</li>
	<li>
		$\lambda_i$, called <span class="define">Lagrange multiplier associated $i$-th inequality constraint</span> $\fie_i(x)\leq0$

	</li>
	<li>
		$\nu$, called <span class="define">Lagrange multiplier associated equality constraints</span> $\feq(x)=0$

	</li>
	<li>
		$\nu_i$, called <span class="define">Lagrange multiplier associated $i$-th equality constraint</span> $\feq_i(x)=0$

	</li>
	<li>
		$\lambda$ and $\nu$,
called <span class="define">dual variables</span> or <span class="define">Lagrange multiplier vectors</span> associated with the optimization problem

	</li>
	</ul>

</div>



<h3>Lagrange dual functions</h3>

<div class="definition" id="definition:Lagrange---dual---functions" data-name="Lagrange dual functions">
	
for optimization problem in <a href="#definition:optimization---problems"></a>
for which Lagrangian is defined,
function $g:\reals^m \times \reals^p \to \reals\cup \{-\infty\}$
defined by

$$
g(\lambda,\nu)
=
\inf_{x\in\optdomain} L(x,\lambda,\nu)
=
\inf_{x\in\optdomain} \left(\fobj(x) + \lambda^T \fie(x) + \nu^T \feq(x)\right)
$$

called
<span class="define">Lagrange dual function</span>
or just
<span class="define">dual function</span>
associated with the optimization problem

</div>


<ul>
<li>
	$g$ is <i>(always) concave function</i> (even when optimization problem is not convex)
	<ul>
	<li>
		since is pointwise infimum of linear (hence concave) functions is concave

	</li>
	</ul>

</li>
<li>
	$g(\lambda,\nu)$ provides
lower bound for optimal value of associated optimization problem,
<i>i.e.</i>,

$$
g(\lambda,\nu) \leq p^\ast
$$

for every $\lambda\succeq0$ 

</li>
<li>
	$(\lambda,\nu) \in \set{(\lambda,\nu)}{\lambda\succeq0, g(\lambda,\nu)>-\infty}$,
said to be <span class="define">dual feasible</span>
<div id="page:dual---feasible"></div>

</li>
</ul>


<h3>Dual function examples</h3>

<ul>
<li>
	LS solution of linear equations

$$
\lssollineqs{primal}
$$

	<ul>
	<li>
		Lagrangian - $L(x,\nu) = x^T x + \nu^T(Ax-b)$

	</li>
	<li>
		Lagrange dual function
<div id="page:dual---function---of---LS---solution---of---lines---equations"></div>

$$
\lssollineqs{dual fcn}
$$


	</li>
	</ul>

</li>
<li>
	standard form LP

$$
\begin{array}{ll}
\mbox{minimize} &
c^Tx
\\
\mbox{subject to} &
Ax = b
\\ &
x\succeq 0
\end{array}
$$

	<ul>
	<li>
		Lagrangian - $L(x,\lambda,\nu) = c^T x - \lambda^T x + \nu^T(Ax-b)$

	</li>
	<li>
		Lagrange dual function
<div id="page:dual---function---of---standard---form---LP"></div>

$$
g(\lambda,\nu) = \left\{\begin{array}{ll}
-b^T\nu & A^T\nu - \lambda + c = 0
\\
-\infty & \mbox{otherwise}
\end{array}\right.
$$

		<ul>
		<li>
			hence, set of dual feasible points is $\set{(A^T\nu + c,\nu)}{A^T\nu +c \succeq0}$

		</li>
		</ul>

	</li>
	</ul>

</li>
<li>
	<i>maximum cut</i>, sometimes called <i>max-cut</i>, problem, which is NP-hard
<div id="page:max-cut---problem"></div>

$$
\begin{array}{ll}
\mbox{minimize} &
x^T W x
\\
\mbox{subject to} &
x_i^2 = 1
\end{array}
$$

where $W\in\symset{n}$
	<ul>
	<li>
		Lagrangian - $L(x,\nu) = x^T(W+\diag(\nu))x - \ones^Tx$

	</li>
	<li>
		Lagrange dual function

$$
g(\nu) = \left\{\begin{array}{ll}
-\ones^T\nu
& W + \diag(\nu) \succeq 0
\\
-\infty & \mbox{otherwise}
\end{array}\right.
$$

		<ul>
		<li>
			hence, set of dual feasible points is $\set{\nu}{W+\diag(\nu)\succeq0}$

		</li>
		</ul>

	</li>
	</ul>

</li>
<li>
	some trivial problem

$$
\begin{array}{ll}
\mbox{minimize} &
f(x)
\\
\mbox{subject to} &
x=0
\end{array}
$$

	<ul>
	<li>
		Lagrangian - $L(x,\nu) =f(x)+\nu^Tx$

	</li>
	<li>
		Lagrange dual function

$$
g(\nu) = \inf_{x\in\reals^n} (f(x)+\nu^Tx)
= -\sup_{x\in\reals^n} ((-\nu)^Tx-f(x))
= - f^\ast(-\nu)
$$

		<ul>
		<li>
			hence, set of dual feasible points is $-\dom f^\ast$,
and
for every $f:\reals^n\to\reals$ and $\nu\in\reals^n$

$$
-f^\ast(-\nu) \leq f(0)
$$


		</li>
		</ul>

	</li>
	</ul>

</li>
<li>
	minimization with linear inequality and equality constraints

$$
\begin{array}{ll}
\mbox{minimize} &
f(x)
\\
\mbox{subject to} &
Ax\preceq b
\\ &
Cx= d
\end{array}
$$

	<ul>
	<li>
		Lagrangian - $L(x,\lambda, \nu) = f(x) + \lambda^T(Ax-b) + \nu^T(Cx-d)$

	</li>
	<li>
		Lagrange dual function

$$
g(\nu) = -b^T\lambda - d^T\nu - f^\ast(-A^T \lambda - C^T\nu)
$$

		<ul>
		<li>
			hence, set of dual feasible points
is $\set{(\lambda,\nu)}{-A^T\lambda - C^T\nu \in \dom f^\ast, \lambda\succeq 0}$

		</li>
		</ul>

	</li>
	</ul>

</li>
<li>
	equality constrained norm minimization

$$
\begin{array}{ll}
\mbox{minimize} &
\|x\|
\\
\mbox{subject to} &
Ax = b
\end{array}
$$

	<ul>
	<li>
		Lagrangian - $L(x,\nu) = \|x\| + \nu^T(Ax-b)$

	</li>
	<li>
		Lagrange dual function

$$
g(\nu) = -b^T\nu -\sup_{x\in\reals^n} ((-A^T\nu)^Tx - \|x\|)
= \left\{\begin{array}{ll}
-b^T \nu&\|A^T\nu\|_\ast\leq1
\\
- \infty & \mbox{otherwise}
\end{array}\right.
$$

		<ul>
		<li>
			hence, set of dual feasible points
is $\set{\nu}{\|A^T\nu\|_\ast \leq1}$

		</li>
		</ul>

	</li>
	</ul>

</li>
<li>
	entropy maximization

$$
\entmax{primal}
$$

where domain of objective function is $\pprealk{n}$
	<ul>
	<li>
		Lagrangian - $L(x,\lambda,\nu) = \sum_{i=1}^n x_i\log x_i + \lambda^T(Ax-b) + \nu(\ones^Tx-1)$

	</li>
	<li>
		Lagrange dual function
<div id="page:dual---function---of---entropy---maximization"></div>

$$
g(\lambda,\nu) = \entmax{dual fcn}
$$

obtained using $f^\ast(y) = \sum_{i=1}^n \exp(y_i-1)$
where $a_i$ is $i$-th column vector of $A$

	</li>
	</ul>

</li>
<li>
	minimum volume covering ellipsoid

$$
\minvolcovering{primal}
$$

where domain of objective function is $\posdefset{n}$
	<ul>
	<li>
		Lagrangian - $L(X,\lambda) = -\log \det X + \sum_{i=1}^m \lambda_i(a_i^T X a_i - 1)$

	</li>
	<li>
		Lagrange dual function
<div id="page:dual---function---of---minimum---volume---covering---ellipsoid"></div>

$$
g(\lambda)
= \minvolcovering{dual fcn}
$$

obtained using $f^\ast(Y) = -\log\det(-Y) - n$

	</li>
	</ul>

</li>
</ul>

<h3>Best lower bound</h3>

<ul>
<li>
	for every $(\lambda,\nu)$ with $\lambda\succeq 0$,
Lagrange dual function $g(\lambda,\nu)$ (in <a href="#definition:Lagrange---dual---functions"></a>)
provides lower bound for optimal value $p^\ast$
for optimization problem in <a href="#definition:optimization---problems"></a>

</li>
<li>
	natural question to ask is
	<ul>
	<li>
		how good is the lower bound?

	</li>
	<li>
		what is best lower bound we can achieve?

	</li>
	</ul>

</li>
<li>
	these questions lead to definition of <i>Lagrange dual problem</i>

</li>
</ul>


<h3>Lagrange dual problems</h3>

<div class="definition" id="definition:Lagrange---dual---problems" data-name="Lagrange dual problems">
	
for optimization problem in <a href="#definition:optimization---problems"></a>,
optimization problem

$$
\begin{array}{ll}
\mbox{maximize} &
g(\lambda,\nu)
\\
\mbox{subject to} &
\lambda \succeq 0
\end{array}
$$

called <span class="define">Lagrange dual problem</span>
associated with problem in <a href="#definition:optimization---problems"></a>

	<ul>
	<li>
		original problem in <a href="#definition:optimization---problems"></a>,
(somestime) called <span class="define">primal problem</span>

	</li>
	<li>
		domain is $\reals^m\times \reals^p$

	</li>
	<li>
		<span class="define">dual feasibility</span> defined in page~<a href="#page:dual---feasible">here</a>,
<i>i.e.</i>, $(\lambda,\nu)$ satisfying
$\lambda \succeq 0 \quad g(\lambda,\nu) > -\infty$
indeed means
feasibility for Lagrange dual problem

	</li>
	<li>
		$d^\ast = \sup\set{g(\lambda,\nu)}{\lambda\in\reals^m,\:\nu\in\reals^p,\:\lambda\succeq 0}$,
called <span class="define">dual optimal value</span>

	</li>
	<li>
		$(\lambda^\ast,\nu^\ast) = \argsup\set{g(\lambda,\nu)}{\lambda\in\reals^m,\:\nu\in\reals^p,\:\lambda\succeq 0}$,
said to be <span class="define">dual optimal</span> or called <span class="define">optimal Lagrange multipliers</span> (if exists)

	</li>
	</ul>

</div>


<ul>
<li>
	Lagrange dual problem in <a href="#definition:Lagrange---dual---problems"></a>
is convex optimization (even though original problem is not)
since $g(\lambda,\nu)$ is always convex

</li>
</ul>


<h3>Making dual constraints explicit dual problems</h3>

<ul>
<li>
	(out specific) way we define Lagrange dual function in <a href="#definition:Lagrange---dual---functions"></a>
as function $g$ of $\reals^m \times \reals^p$ into $\reals\cup\{-\infty\}$,
<i>i.e.</i>,
$\dom g = \reals^n\times\reals^p$

</li>
<li>
	however,
in many cases,
feasible set $\set{(\lambda,\nu)}{\lambda \succeq 0 \quad g(\lambda,\nu) > -\infty}$
is proper subset of $\reals^n\times\reals^p$

</li>
<li>
	can make this implicit feasibility condition
explicit by adding it as constraint
(as shown in following examples)
<div id="page:make---implicit---dual---feasibility---explicit"></div>

</li>
</ul>

<h3>Lagrange dual problems associated with LPs</h3>

<ul>
<li>
	standard form LP
	<ul>
	<li>
		primal problem

$$
\begin{array}{ll}
\mbox{minimize} &
c^Tx
\\
\mbox{subject to} &
Ax = b
\\ &
x\succeq 0
\end{array}
$$


	</li>
	<li>
		Lagrange dual problem

$$
\begin{array}{ll}
\mbox{maximize} &
g(\lambda,\nu) = \left\{\begin{array}{ll}
-b^T\nu & A^T\nu - \lambda + c = 0
\\
-\infty & \mbox{otherwise}
\end{array}\right.
\\
\mbox{subject to} &
\lambda \succeq 0
\end{array}
$$

(refer to page~<a href="#page:dual---function---of---standard---form---LP">here</a>
for Lagrange dual function)
		<ul>
		<li>
			can make dual feasibility explicit by adding it to constraints
as mentioned on page~<a href="#page:make---implicit---dual---feasibility---explicit">here</a>

$$
\begin{array}{ll}
\mbox{maximize} &
-b^T\nu
\\
\mbox{subject to} &
\lambda \succeq 0
\\ &
A^T\nu - \lambda + c = 0
\end{array}
$$


		</li>
		<li>
			can further simplify problem

$$
\begin{array}{ll}
\mbox{maximize} &
-b^T\nu
\\
\mbox{subject to} &
A^T\nu + c \succeq 0
\end{array}
$$


		</li>
		</ul>

	</li>
	<li>
		last problem is <i>inequality form LP</i>

	</li>
	<li>
		all three problems are equivalent,
but <i>not</i> same problems

	</li>
	<li>
		will, however, with abuse of terminology,
refer to all three problems
as Lagrange dual problem

	</li>
	</ul>

</li>
<li>
	inequality form LP
	<ul>
	<li>
		primal problem

$$
\begin{array}{ll}
\mbox{minimize} &
c^Tx
\\
\mbox{subject to} &
Ax \preceq b
\end{array}
$$


	</li>
	<li>
		Lagrangian

$$
L(x,\lambda) = c^Tx + \lambda^T(Ax-b)
$$


	</li>
	<li>
		Lagrange dual function

$$
g(\lambda)
=
-b^T\lambda + \inf_{x\in\reals^n} (c+A^T\lambda)^T x
=
\left\{\begin{array}{ll}
-b^T\lambda & A^T\lambda + c =0
\\
-\infty & \mbox{otherwise}
\end{array}\right.
$$


	</li>
	<li>
		Lagrange dual problem

$$
\begin{array}{ll}
\mbox{maximize} &
g(\lambda)
= \left\{\begin{array}{ll}
-b^T\lambda & A^T\lambda + c =0
\\
-\infty & \mbox{otherwise}
\end{array}\right.
\\
\mbox{subject to} &
\lambda \succeq 0
\end{array}
$$

		<ul>
		<li>
			can make dual feasibility explicit by adding it to constraints
as mentioned on page~<a href="#page:make---implicit---dual---feasibility---explicit">here</a>

$$
\begin{array}{ll}
\mbox{maximize} &
-b^T\nu
\\
\mbox{subject to} &
A^T\lambda + c = 0
\\ &
\lambda \succeq 0
\end{array}
$$


		</li>
		</ul>

	</li>
	<li>
		dual problem is <i>standard form LP</i>

	</li>
	</ul>

</li>
<li>
	thus,
dual of standard form LP is inequality form LP
and vice versa

</li>
<li>
	also, for both cases, dual of dual is same as primal problem

</li>
</ul>

<h3>Lagrange dual problem of equality constrained optimization problem</h3>

<ul>
<li>
	equality constrained optimization problem

$$
\begin{array}{ll}
\mbox{minimize} &
\fobj(x)
\\
\mbox{subject to} &
Ax = b
\end{array}
$$


</li>
<li>
	dual function

$$
\begin{eqnarray*}
g(\nu)
&
=
&
\inf_{x\in\dom \fobj} (\fobj(x) + \nu^T(Ax-b))
=
-b^T\nu
- \sup_{x\in\dom \fobj}(-\nu^TAx -\fobj(x))
\\
&
=
&
-b^T\nu - {\fobj}^\ast(-A^T\nu)
\end{eqnarray*}
$$


</li>
<li>
	dual problem

$$
\begin{array}{ll}
\mbox{maximize} &
-b^T\nu - {\fobj}^\ast(-A^T\nu)
\end{array}
$$


</li>
</ul>


<h3>Lagrange dual problem associated with equality constrained quadratic program</h3>

<ul>
<li>
	strictly convex quadratic problem

$$
\begin{array}{ll}
\mbox{minimize} &
\fobj(x) = x^TPx + q^T x + r
\\
\mbox{subject to} &
Ax=b
\end{array}
$$

	<ul>
	<li>
		conjugate function of objective function

$$
{\fobj}^\ast(x)
= (x-q)^TP^{-1}(x-q)/4 - r
=
x^TP^{-1}x/4
-q^TP^{-1}x/2
+ q^TP^{-1}q/4
-r
$$


	</li>
	<li>
		dual problem

$$
\begin{array}{ll}
\mbox{maximize} &
-\nu^T (AP^{-1}A^T)\nu /4 -(b + A P^{-1} q/2)^T\nu - q^TP^{-1}q/4 +r
\end{array}
$$


	</li>
	</ul>

</li>
</ul>


<h3>Lagrange dual problems associated with nonconvex quadratic problems</h3>

<ul>
<li>
	primal problem

$$
\noncvxquadprob{primal}
$$

where $A\in\symset{n}$, $A\not\in\possemidefset{n}$, and $b\in\reals^n$
	<ul>
	<li>
		since $A\not\succeq 0$, not convex optimization problem

	</li>
	<li>
		sometimes called <span class="define">trust region problem</span>
arising minimizing second-order approximation of function
over bounded region

	</li>
	</ul>

</li>
<li>
	Lagrange dual function

$$
g(\lambda)
=
\noncvxquadprob{dual fcn}
$$

where $(A+\lambda I)^\dagger$ is pseudo-inverse of $A+\lambda I$

</li>
<li>
	Lagrange dual problem
<div id="page:dual---problem---of---trust---region---nonconvex---quadratic---problems"></div>

$$
\noncvxquadprob{dual}
$$

where optimization variable is $\lambda \in\reals$
	<ul>
	<li>
		note we do not need constraint $\lambda \geq0$
since it is implied by $A+\lambda I \succeq 0$

	</li>
	<li>
		though not obvious from what it appears to be,
it is (of course) convex optimization problem
(by definition of Lagrange dual function, <i>i.e.</i>, <a href="#definition:Lagrange---dual---functions"></a>)

	</li>
	<li>
		can be expressed ar

$$
\begin{array}{ll}
\mbox{maximize} &
-\sum_{i=1}^n (q_i^Tb)^2/(\lambda_i + \lambda) - \lambda
\\
\mbox{subject to} &
\lambda \geq - \lambda_\mathrm{min}(A)
\end{array}
$$

where $\lambda_i$ and $q_i$ are eigenvalues and corresponding orthogormal eigenvectors of $A$,
when $\lambda_i + \lambda=0$ for some $i$,
we interpret $(q_i^Tb)^2/0$ as 0 if $q_i^T0$ and $\infty$ otherwise

	</li>
	</ul>

</li>
</ul>

<h3>Weak duality</h3>

<ul>
<li>
	since $g(\lambda,\nu)\leq p^\ast$ for every $\lambda\succeq 0$,
we have

$$
d^\ast = \sup\set{g(\lambda,\nu)}{\lambda\in\reals^m,\:\nu\in\reals^p,\:\lambda\succeq 0}
\leq
p^\ast
$$


</li>
</ul>
<div class="definition" id="definition:weak---duality" data-name="weak duality">
	
property that
that
optimal value of optimization problem (in <a href="#definition:optimization---problems"></a>)
is always no less than
optimal value of Lagrange daul problem (in <a href="#definition:Lagrange---dual---problems"></a>)

$$
d^\ast \leq p^\ast
$$

called <span class="define">weak duality</span>

	<ul>
	<li>
		$d^\ast$ is best lower bound for primal problem
that can be obtained from Lagrange dual function (by definition)

	</li>
	<li>
		weak duality holds even when $d^\ast$ or/and $p^\ast$ are not finite, <i>e.g.</i>
		<ul>
		<li>
			<i>if primal problem is unbounded below</i> so that $p^\ast=-\infty$,
must have $d^\ast = -\infty$,
<i>i.e.</i>, <i>dual problem is infeasible</i>

		</li>
		<li>
			conversely,
<i>if dual problem is unbounded above</i> so that $d^\ast = \infty$,
must have $p^\ast=\infty$,
<i>i.e.</i>, <i>primal problem is infeasible</i>

		</li>
		</ul>

	</li>
	</ul>

</div>

<h3>Optimal duality gap</h3>

<div class="definition" id="definition:optimal---duality---gap" data-name="optimal duality gap">
	
difference between
optimal value of optimization problem (in <a href="#definition:optimization---problems"></a>)
and
optimal value of Lagrange daul problem (in <a href="#definition:Lagrange---dual---problems"></a>),
<i>i.e.</i>

$$
p^\ast - d^\ast
$$

called <span class="define">optimal duality gap</span>

</div>
<ul>
<li>
	sometimes used for lower bound of optimal value of problem which is difficult to solve
	<ul>
	<li>
		for example,
dual problem
of max-cut problem (on page~<a href="#page:max-cut---problem">here</a>),
which is NP-hard,
is

$$
\begin{array}{ll}
\mbox{minimize} &
-\ones^T \nu
\\
\mbox{subject to} &
W + \diag(\nu) \succeq 0
\end{array}
$$

where optimization variable is $\nu\in\reals^n$
		<ul>
		<li>
			the dual problem can be solved very efficiently using polynomial time algorithms
while primal problme <i>cannot</i> be solved unless $n$ is very small

		</li>
		</ul>

	</li>
	</ul>

</li>
</ul>

<h3>Strong duality</h3>

<div class="definition" id="definition:strong---duality" data-name="strong duality">
	
if
optimal value of optimization problem (in <a href="#definition:optimization---problems"></a>)
equals to
optimal value of Lagrange daul problem (in <a href="#definition:Lagrange---dual---problems"></a>),
<i>i.e.</i>

$$
p^\ast = d^\ast
$$

<span class="define">strong duality</span> said to hold

</div>
<ul>
<li>
	strong duality does <i>not</i> hold in general
	<ul>
	<li>
		if it held always, max-cut problem, which is NP-hard, can be solved in polynomial time,
which would be one of biggest breakthrough in field of theoretical computer science

	</li>
	<li>
		may mean some of strongest cryptography methods, <i>e.g.</i>, homeomorphic cryptography,
can be broken

	</li>
	</ul>

</li>
</ul>

<h3>Slater's theorem</h3>

<ul>
<li>
	exist many conditions
which guarantee strong duality,
which are called <i>constraint qualifications</i>
- one of them is Slater's condition

</li>
</ul>
<div class="theorem" id="theorem:Slater's---theorem" data-name="Slater's theorem">
	
if
optimization problem is convex (<a href="#definition:convex---optimization"></a>),
and exists feasible $x\in\optdomain$ contained in $\relint \optdomain$
such that

$$
\fie(x) \prec 0\quad \feq(x) = 0
$$

<i>strong duality</i> holds
(and <i>dual optimum is attained when $d^\ast>-\infty$</i>)

	<ul>
	<li>
		such condition, called <span class="define">Slater's condition</span>

	</li>
	<li>
		such point, (sometimes) said to be <span class="define">strictly feasible</span>

	</li>
	</ul>

when there are affine inequality constraints,
can refine Slater's condition
- if first $k$ inequality constraint functions $\fie_1$, &hellip;, $\fie_k$ are affine,
Slater's condition can be relaxed to

$$
\fie_i(x)\leq 0\;\;i=1,\ldots,k
\quad
\fie_i(x) < 0\;\;i=k+1,\ldots,m
\quad
\feq(x) = 0
$$


</div>

<h3>Strong duality for LS solution of linear equations</h3>

<ul>
<li>
	primal problem

$$
\lssollineqs{primal}
$$


</li>
<li>
	dual problem

$$
\lssollineqs{dual}
$$

(refer to page~<a href="#page:dual---function---of---LS---solution---of---lines---equations">here</a> for Lagrange dual function)

</li>
<li>
	&ldquo;dual is always feasible''
and
&ldquo;primal is feasible $\Rightarrow$ Slater's condition holds'',
thus
Slater's theorem (<a href="#theorem:Slater's---theorem"></a>)
implies,
exist only three cases
	<ul>
	<li>
		$(d^\ast = p^\ast \in \reals)$
or
$(d^\ast \in \reals\:\&\: p^\ast = \infty)$
or
$(d^\ast = p^\ast = \infty)$

	</li>
	</ul>

</li>
<li>
	if primal is infeasible, though,
$b\not\in\range(A)$,
thus
exists $z$, such that $A^Tz=0$ and $b^Tz \neq0$,
then line $\set{tz}{t\in\reals}$ makes dual problem unbounded above,
hence $d^\ast=\infty$

</li>
<li>
	hence, <i>strong duality always holds</i>,
<i>i.e.</i>, $(d^\ast= p^\ast \in \reals)$ or $(d^\ast = p^\ast = \infty)$

</li>
</ul>

<h3>Strong duality for LP</h3>

<ul>
<li>
	every LP either is infeasible or satisfies Slater's condition

</li>
<li>
	dual of LP is LP,
hence, Slater's theorem (<a href="#theorem:Slater's---theorem"></a>)
implies
	<ul>
	<li>
		if primal is feaisble,
either $(d^\ast=p^\ast= -\infty)$ or $(d^\ast=p^\ast\in\reals)$

	</li>
	<li>
		if dual is feaisble,
either $(d^\ast=p^\ast= \infty)$ or $(d^\ast=p^\ast\in\reals)$

	</li>
	<li>
		only other case left is $(d^\ast=-\infty\;\&\;p^\ast= \infty)$
		<ul>
		<li>
			indeed, this pathological case can happen

		</li>
		</ul>

	</li>
	</ul>

</li>
</ul>

<h3>Strong duality for entropy maximization</h3>

<ul>
<li>
	primal problem

$$
\entmax{primal}
$$


</li>
<li>
	dual problem
(refer to page~<a href="#page:dual---function---of---entropy---maximization">here</a> for Lagrange dual function)

$$
\entmax{dual}
$$


</li>
<li>
	dual problem is feasible,
hence, Slater's theorem (<a href="#theorem:Slater's---theorem"></a>)
implies,
if exists $x\succ 0$ with $Ax \preceq b$ and $\ones^T x =1$,
strong duality holds,
and indeed $d^\ast=p^\ast\in\reals$

</li>
<li>
	by the way,
can simplify dual problem by maximizing dual objective function over $\nu$

$$
\entmax{simplied dual}
$$

which is geometry program in convex form
(<a href="#proposition:geometric---programming---in---convex---form"></a>)
with nonnegativity contraint

</li>
</ul>


<h3>Strong duality for minimum volume covering ellipsoid</h3>

<ul>
<li>
	primal problem

$$
\minvolcovering{primal}
$$

where $\optdomain=\posdefset{n}$

</li>
<li>
	dual problem

$$
\minvolcovering{dual}
$$

(refer to page~<a href="#page:dual---function---of---minimum---volume---covering---ellipsoid">here</a> for Lagrange dual function)

</li>
<li>
	$X=\alpha I$ with large enough $\alpha>0$ satisfies primal's constraints,
hence Slater's condition <i>always</i> holds,
thus,
<i>strong duality always holds</i>,
<i>i.e.</i>, $(d^\ast = p^\ast \in \reals)$ or $(d^\ast = p^\ast = -\infty)$

</li>
<li>
	in fact, $\range(a_1,\ldots,a_m) = \reals^n$ if and only if $d^\ast=p^\ast\in\reals^n$

</li>
</ul>

<h3>Strong duality for trust region nonconvex quadratic problems</h3>

<ul>
<li>
	one of rare occasions
in which
<i>strong duality obtains for nonconvex problems</i>

</li>
<li>
	primal problem

$$
\noncvxquadprob{primal}
$$

where $A\in\symset{n}$, $A\not\in\possemidefset{n}$, and $b\in\reals^n$

</li>
<li>
	Lagrange dual problem (page~<a href="#page:dual---problem---of---trust---region---nonconvex---quadratic---problems">here</a>)

$$
\noncvxquadprob{dual}
$$


</li>
<li>
	<i>strong duality always holds</i>
and $d^\ast=p^\ast\in\reals$
(since dual problem is feasible - large enough $\lambda$ satisfies dual constraints)

</li>
<li>
	in fact, exists stronger result
- <i>strong dual holds</i> for optimization problem with quadratic objective
and <i>one</i> quadratic inequality constraint,
provided Slater's condition holds

</li>
</ul>

<h3>Matrix games using mixed strategies</h3>

<div id="page:Matrix---games---using---mixed---strategies"></div>
<ul>
<li>
	matrix game - consider game with two players $A$ and $B$
	<ul>
	<li>
		player $A$ makes choice $1\leq a\leq n$,
player $B$ makes choice $1\leq b\leq m$,
then player $A$ makes payment of $P_{ab}$ to player $B$

	</li>
	<li>
		matrix $P\in\reals^{n\times m}$, called <span class="define">payoff matrix</span>

	</li>
	<li>
		player $A$ tries to pay as little as possible
&amp;
player $B$ tries to received as much as possible

	</li>
	<li>
		players use <span class="define">randomized or mixed strategies</span>,
<i>i.e.</i>, each player makes choice randomly and independently of other player's choice
according to probability distributions

$$
\Prob(a=i) = u_i\; i=1\leq i\leq n
\quad
\Prob(b=j) = v_j\; i=1\leq j\leq m
$$


	</li>
	</ul>

</li>
<li>
	expected payoff (from player $A$ to player $B$)

$$
\sum_i \sum_j u_iv_jP_{ij} = u^TPv
$$


</li>
<li>
	assume player $A$'s strategy is known to play $B$
	<ul>
	<li>
		player $B$ will choose $v$ to maximize $u^TPv$

$$
\sup\set{u^TPv}{v\succeq 0,\; \ones^Tv=1}
= \max_{1\leq j\leq m} (P^Tu)_j
$$


	</li>
	<li>
		player $A$ (assuming that player $B$ will employ above strategy to maximize payment)
will choose $u$ to minimize payment

$$
\begin{array}{ll}
\mbox{minimize} & \max_{1\leq j\leq m} (P^Tu)_j
\\
\mbox{subject to} &
u\succeq 0\quad \ones^Tu=1
\end{array}
$$


	</li>
	</ul>

</li>
<li>
	assume player $B$'s strategy is known to play $A$
	<ul>
	<li>
		then player $B$ will do same to maximize payment
(assuming that player $A$ will employ such strategy to minimize payment)

$$
\begin{array}{ll}
\mbox{maximize} & \min_{1\leq i\leq n} (Pv)_i
\\
\mbox{subject to} &
v\succeq 0\quad \ones^Tv=1
\end{array}
$$


	</li>
	</ul>

</li>
</ul>

<h3>Strong duality for matrix games using mixed strategies</h3>

<ul>
<li>
	in matrix game,
can guess
in frist came,
player $B$ has advantage over player $A$ because $A$'s strategy's exposed to $B$,
and vice versa,
hence
optimal value of first problem is greater than that of second problem

</li>
<li>
	surprising,
no one has advantage over the other,
<i>i.e.</i>, optimal values of two problems are <i>same</i>
-
will show this

</li>
<li>
	first observe both problems are (convex) piecewise-linear optimization problems

</li>
<li>
	formulate first problem as LP

$$
\begin{array}{ll}
\mbox{minimize} &
t
\\
\mbox{subject to} &
u\succeq 0 \quad \ones^T u =1 \quad P^T u \preceq t\ones
\end{array}
$$

	<ul>
	<li>
		Lagrangian

$$
L(u,t,\lambda_1, \lambda_2,\nu) = \nu + (1-\ones^T\lambda_1)t + (P\lambda_1 - \nu \ones - \lambda_2)^Tu
$$


	</li>
	<li>
		Lagrange dual function

$$
g(\lambda_1, \lambda_2,\nu) = \left\{\begin{array}{ll}
\nu & \ones^T\lambda_1 = 1 \;\&\; P\lambda_1 - \nu \ones = \lambda_2
\\
-\infty & \mbox{otherwise}
\end{array}\right.
$$


	</li>
	</ul>

</li>
<li>
	Lagrange dual problem

$$
\begin{array}{ll}
\mbox{maximize} &
\nu
\\
\mbox{subject to} &
\ones^T\lambda_1 = 1 \quad P\lambda_1 - \nu \ones = \lambda_2
\\ &
\lambda_1 \succeq 0 \quad \lambda_2 \succeq 0
\end{array}
$$


</li>
<li>
	eliminating $\lambda_2$ gives
below Lagrange dual problem

$$
\begin{array}{ll}
\mbox{maximize} &
\nu
\\
\mbox{subject to} &
\lambda_1 \succeq 0 \quad \ones^T\lambda_1 = 1 \quad P\lambda_1 \succeq \nu \ones
\end{array}
$$

which is equivalent to second problem in matrix game

</li>
<li>
	weak duality confirms &ldquo;player who knows other player's strategy has advantage or on par''

</li>
<li>
	moreoever,
primal problem satisfies Slater's condition, hence <i>strong duality {always} holds</i>,
and dual is feasible,
hence $d^\ast=p^\ast\in\reals$,
<i>i.e.</i>, regardless of who knows other player's strategy,
no player has advantage

</li>
</ul>

<h3>Geometric interpretation of duality</h3>

<ul>
<li>
	assume (not necessarily convex) optimization problem
in <a href="#definition:optimization---problems"></a>

</li>
<li>
	define graph

$$
G = \set{(\fie(x), \feq(x), \fobj(x))}{x\in\optdomain}
\subset \reals^m \times \reals^p \times \reals
$$


</li>
<li>
	for every $\lambda\succeq 0$ and $\nu$

$$
\begin{eqnarray*}

p^\ast &=& \inf\set{t}{(u,v,t) \in G, u\preceq 0, v &=& 0}

\\
&
\geq
&
\inf\set{t+\lambda^Tu + \nu^T v}{(u,v,t) \in G, u\preceq 0, v = 0}
\\
&
\geq
&
\inf\set{t+\lambda^Tu + \nu^T v}{(u,v,t) \in G}
=
g(\lambda,\nu)
\end{eqnarray*}
$$

where second inequality comes from
$\set{(u,v,t)}{(u,v,t) \in G, u\preceq 0, v = 0} \subset G$

</li>
<li>
	above establishes <i>weak duality</i>
<i>using graph</i>

</li>
<li>
	last equality implies that

$$
(\lambda, \nu, 1)^T (u,v,t) \geq g(\lambda,\nu)
$$

hence if $g(\lambda,\nu) > -\infty$,
$(\lambda, \nu, 1)$ and $g(\lambda,\nu)$ define
<i>nonvertical</i>
<i>supporting hyperplane</i> for $G$
- nonvertical because third component is nonzero

</li>
</ul>

<ul>
<li>
	the figure
shows $G$ as area inside closed curve
contained in $\reals^m\times\reals^p\times\reals$ where $m=1$ and $p=0$
as primal optimal value $p^\ast$ and supporting hyperplane
$\lambda u + t = g(\lambda)$

</li>
</ul>




<div id="fig:geometric---interpretation---of---duality-------1"></div>


<ul>
<li>
	the figure
shows three hyperplanes determined by three values for $\lambda$,
one of which $\lambda^\ast$ is optimal solution for dual problem

</li>
</ul>




<div id="fig:geometric---interpretation---of---duality-------2"></div>



<h3>Epigraph interpretation of duality</h3>

<ul>
<li>
	define extended graph over $G$ - sort of epigraph of $G$

$$
\begin{eqnarray*}

H &=& G + \preals^m \times \{0\} \times \preals

\\
&
=
&
\set{(u, v, t)}{x\in\optdomain, \fie(x) \preceq u, \feq(x) = v, \fobj(x)\leq t }
\end{eqnarray*}
$$


</li>
<li>
	if $\lambda\succeq 0$, $g(\lambda,\nu) = \inf\set{(\lambda,\nu,1)^T(u,v,t)}{(u,v,t) \in H}$, thus

$$
(\lambda,\nu,1)^T (u,v,t) \geq g(\lambda,\nu)
$$

defines nonvertical supporting hyperplane for $H$

</li>
<li>
	now $p^\ast = \inf\set{t}{(0,0,t)\in H}$, hence $(0,0,p^\ast) \in \boundary H$, hence

$$
p^\ast =(\lambda,\nu,1)^T (0,0,p^\ast) \geq g(\lambda,\nu)
$$


</li>
<li>
	once again establishes <i>weak duality</i>

</li>
<li>
	the figure
shows epigraph interpretation

</li>
</ul>




<div id="fig:geometric---interpretation---of---duality-------3"></div>



<h3>Proof of strong duality under constraint qualification</h3>

<ul>
<li>
	now we show proof of strong duality
- this is one of rare cases where proof is shown in main slides
instead of &ldquo;selected proofs'' section like Galois theory
since - (I hope) it will give you some good intuition about
why strong duality holds for (most) convex optimization problems

</li>
<li>
	assume Slater's condition holds,
<i>i.e.</i>,
$\fobj$ and $\fie$ are convex, $\feq$ is affine,
and
exists $x\in\optdomain$
such that $\fie(x) \prec 0$ and $\feq(x) = 0$

</li>
<li>
	further assume $\optdomain$ has interior (hence, $\relint \optdomain = \interior{\optdomain}$
and $\rank A=p$

</li>
<li>
	assume $p^\ast\in\reals$ - since exists feasible $x$, the other possibility is $p^\ast = -\infty$,
but then, $d^\ast = -\infty$, hence strong duality holds

</li>
<li>
	$H$ is convex 

</li>
<li>
	now define

$$
B = \set{(0,0,s)\in\reals^m\times\reals^p\times\reals}{s<p^\ast}
$$


</li>
<li>
	then $B\cap H=\emptyset$, hence <a href="#theorem:separating---hyperplane---theorem"></a>
implies exists separable hyperplane with $(\tilde{\lambda}, \tilde{\nu}, \mu)\neq 0$ and $\alpha$
such that

$$
\begin{eqnarray*}
(u,v,t) \in H
&\Rightarrow&
\tilde{\lambda}^T u + \tilde{\nu}^T v + \mu t \geq \alpha
\\
(u,v,t) \in B
&\Rightarrow&
\tilde{\lambda}^T u + \tilde{\nu}^T v + \mu t \leq \alpha
\end{eqnarray*}
$$


</li>
<li>
	then $\tilde{\lambda} \succeq 0$ &amp; $\mu\geq0$ - assume $\mu>0$
	<ul>
	<li>
		can prove when $\mu=0$, but kind of tedius, plus,
whole purpose is provide good intuition,
so will not do it here

	</li>
	</ul>

</li>
<li>
	above second inequality implies $\mu p^\ast \leq \alpha$ and
for some $x\in\optdomain$

$$
\mu L(x,\tilde{\lambda}/\mu, \tilde{\nu}/\mu)
=
\tilde{\lambda}^T \fie(x) + \tilde{\nu}^T \feq(x) + \mu \fobj(x) \geq \alpha \geq \mu p^\ast
$$

thus,

$$
g(\tilde{\lambda}/\mu, \tilde{\nu}/\mu) \geq p^\ast
$$


</li>
<li>
	finally, weak duality implies

$$
g(\lambda,\nu) = p^\ast
$$

where $\lambda = \tilde{\lambda}/\mu$ &amp; $\nu = \tilde{\nu}/\mu$

</li>
</ul>




<div id="fig:geometric---interpretation---of---duality-------4"></div>



<h3>Max-min characterization of weak and strong dualities</h3>

<ul>
<li>
	note


$$
\begin{eqnarray*}
\sup_{\lambda\geq 0, \nu} L(x,\lambda,\nu)
&=&
\sup_{\lambda\geq 0, \nu} \left(
\fobj(x) + \lambda^T \fie(x) + \nu^T \feq(x)
\right)
\\
&
=
&
\left\{\begin{array}{ll}
\fobj(x) & x\in\optfeasset
\\
\infty & \mbox{otherwise}
\end{array}\right.
\end{eqnarray*}
$$


</li>
<li>
	thus
$p^\ast = \inf_{x\in\optdomain} \sup_{\lambda\succeq 0, \nu} L(x,\lambda,\nu)$
whereas
$d^\ast = \sup_{\lambda\succeq 0,\nu} \inf_{x\in\optdomain} L(x,\lambda,\nu)$

</li>
<li>
	weak duality means

$$
\sup_{\lambda\succeq 0, \nu} \inf_{x\in\optdomain} L(x,\lambda,\nu)
\leq
\inf_{x\in\optdomain} \sup_{\lambda\succeq 0, \nu} L(x,\lambda,\nu)
$$


</li>
<li>
	strong duality means

$$
\sup_{\lambda\succeq 0, \nu} \inf_{x\in\optdomain} L(x,\lambda,\nu)
=
\inf_{x\in\optdomain} \sup_{\lambda\succeq 0, \nu} L(x,\lambda,\nu)
$$


</li>
</ul>

<h3>Max-min inequality</h3>

<ul>
<li>
	indeed, inequality
$\sup_{\lambda\succeq 0} \inf_{x\in\optdomain} L(x,\lambda,\nu)
\leq
\inf_{x\in\optdomain} \sup_{\lambda\succeq 0} L(x,\lambda,\nu)$
holds for general case

</li>
</ul>
<div class="inequality" id="inequality:max-min---inequality" data-name="max-min inequality">
	
for $f:{X} \times {Y} \to \reals$

$$
\sup_{y\in{Y}} \inf_{x\in{X}} f(x,y)
\leq
\inf_{x\in{X}} \sup_{y\in{Y}} f(x,y)
$$



</div>
<div class="definition" id="definition:strong---max-min---property" data-name="strong max-min property">
	
if below equality holds, we say
$f$ (and $X$ and $Y$) satisfies <span class="define">strong max-min property</span>
or <span class="define">saddle point property</span>

$$
\sup_{y\in{Y}} \inf_{x\in{X}} f(x,y)
=
\inf_{x\in{X}} \sup_{y\in{Y}} f(x,y)
$$


</div>
<ul>
<li>
	this happens,
<i>e.g.</i>,
$X=\optdomain$,
$Y=\prealk{m} \times \reals^p$,
$f$ is Lagrangian of
optimization problem
(in <a href="#definition:optimization---problems"></a>)
for which strong duality holds

</li>
</ul>

<h3>Saddle-points</h3>

<div class="definition" id="definition:saddle-points" data-name="saddle-points">
	
for $f:X\times Y\to\reals$,
pair $x^\ast\in X$ and $y^\ast\in Y$
such that

$$
\left(
\forall x \in X, y\in Y
\right)
\left(
f(x^\ast,y) \leq f(x^\ast,y^\ast) \leq f(x,y^\ast)
\right)
$$

called <span class="define">saddle-point for $f$ (and $X$ and $Y$)</span>

</div>
<ul>
<li>
	if assumption in <a href="#definition:saddle-points"></a> holds,
$x^\ast$ minimizes $f(x,y^\ast)$ over $X$
and
$y^\ast$ maximizes $f(x^\ast,y)$ over $Y$

$$
\sup_{y\in Y} f(x^\ast,y)
=
f(x^\ast,y^\ast)
=
\inf_{x\in X} f(x,y^\ast)
$$

	<ul>
	<li>
		strong max-min property (in <a href="#definition:strong---max-min---property"></a>)
holds with $f(x^\ast,y^\ast)$ as common value

	</li>
	</ul>

</li>
</ul>


<h3>Saddle-point interpretation of strong duality</h3>

<ul>
<li>
	for primal optimum $x^\ast$ and dual optimum $(\lambda^\ast,\nu^\ast)$


$$
g(\lambda^\ast,\nu^\ast) \leq L(x^\ast, \lambda^\ast, \nu^\ast) \leq \fobj(x^\ast)
$$


</li>
<li>
	if strong duality holds,
for every $x\in\optdomain$, $\lambda\succeq 0$, and $\nu$


$$
L(x^\ast,\lambda,\nu)
\leq
\fobj(x^\ast) = L(x^\ast,\lambda^\ast,\nu^\ast) = g(\lambda^\ast,\nu^\ast)
\leq
L(x,\lambda^\ast, \nu^\ast)
$$

	<ul>
	<li>
		thus $x^\ast$ and $(\lambda^\ast,\nu^\ast)$ form saddle-point of Lagrangian

	</li>
	</ul>

</li>
<li>
	conversely, if $\tilde{x}$ and $(\tilde{\lambda},\tilde{\nu})$ are saddle-point of Lagrangian,
<i>i.e.</i>,
for every $x\in\optdomain$, $\lambda\succeq 0$, and $\nu$


$$
L(\tilde{x}, {\lambda},{\nu})
\leq
L(\tilde{x}, \tilde{\lambda},\tilde{\nu})
\leq
L({x}, \tilde{\lambda},\tilde{\nu})
$$

	<ul>
	<li>
		hence
$g(\tilde{\lambda},\tilde{\nu})
= \inf_{x\in\optdomain} L(x,\tilde{\lambda},\tilde{\nu})
= L(\tilde{x}, \tilde{\lambda},\tilde{\nu})
= \sup_{\lambda\succeq 0, \nu} L(\tilde{x},{\lambda},{\nu}) = \fobj(\tilde{x})$,
thus
$g(\lambda^\ast,\nu^\ast) \leq g(\tilde{\lambda}, \tilde{\nu})$
&amp;
$\fobj(\tilde{x}) \leq \fobj(x^\ast)$

	</li>
	<li>
		thus $\tilde{x}$ and $(\tilde{\lambda}, \tilde{\nu})$ are primal and dual optimal

	</li>
	</ul>

</li>
</ul>

<h3>Game interpretation</h3>

<div id="page:Game---interpretation"></div>
<ul>
<li>
	assume
two players play zero-sum game with payment function $f:X\times Y\to \reals$
where
player $A$ pays player $B$ amount equal to $f(x,y)$
when player $A$ chooses $x$ and player $B$ chooses $y$

</li>
<li>
	player $A$ will try to minimize $f(x,y)$
and
player $B$ will try to maximize $f(x,y)$

</li>
<li>
	assume player $A$ chooses first
then player $B$ chooses after learning opponent's choice
	<ul>
	<li>
		if player $A$ chooses $x$, player $B$ will choose $\argsup_{y\in Y} f(x,y)$

	</li>
	<li>
		knowing that, player $A$ will first choose $\arginf_{x\in X} \sup_{y\in Y} f(x,y)$

	</li>
	<li>
		hence payment will be $\inf_{x\in X} \sup_{y\in Y} f(x,y)$

	</li>
	</ul>

</li>
<li>
	if player $B$ makes her choise first, opposite happens, <i>i.e.</i>,
payment will be $\sup_{y\in Y} \inf_{x\in X} f(x,y)$

</li>
<li>
	max-min inequality of <a href="#inequality:max-min---inequality"></a> says

$$
\sup_{y\in Y} \inf_{x\in X} f(x,y)
\leq
\inf_{x\in X} \sup_{y\in Y} f(x,y)
$$

<i>i.e.</i>, whowever chooses later has advantage,
which is similar or rather same as
matrix games using mixed strategies on page~<a href="#page:Matrix---games---using---mixed---strategies">here</a>

</li>
<li>
	saddle-point for $f$ (and $X$ and $Y$),
$(x^\ast,y^\ast)$,
called <span class="define">solution of game</span>
- $x^\ast$ is optimal choice for player $A$
and
$x^\ast$ is optimal choice for player $B$

</li>
</ul>

<h3>Game interpretation for weak and strong dualities</h3>

<ul>
<li>
	assume payment function in zero-sum game on page~<a href="#page:Game---interpretation">here</a>
is Lagrangian of optimization problem
in <a href="#definition:optimization---problems"></a>

</li>
<li>
	assume that $X=\xdomain$ and $Y=\prealk{n} \times \reals^p$

</li>
<li>
	if player $A$ chooses first, knowing that player $B$ will choose $\argsup_{(\lambda,\nu)\in Y}L(x,\lambda,\nu)$,
she will choose $x^\ast = \arginf_{x\in\xdomain} \sup_{(\lambda,\nu)\in Y}L(x,\lambda,\nu)$

</li>
<li>
	likewise, player $B$ will choose
$(\lambda^\ast,\nu^\ast) = \argsup_{(\lambda,\nu)\in Y} \inf_{x\in\xdomain} L(x,\lambda,\nu)$

</li>
<li>
	optimal dualtiy gap $p^\ast - d^\ast$ equals to advantage player who goes second has

</li>
<li>
	if strong dualtiy holds, $(x^\ast, \lambda^\ast, \nu^\ast)$ is solution of game,
in which case no one has advantage

</li>
</ul>


<h3>Certificate of suboptimality</h3>

<ul>
<li>
	dual feasible point $(\lambda,\nu)$
degree of suboptimality of current solution

</li>
<li>
	assume $x$ is feasible solution,
then

$$
\fobj(x) - p^\ast \leq \fobj(x) - g(\lambda,\nu)
$$

guarantees that $\fobj(x)$ is no further than $\epsilon = \fobj(x) - g(\lambda,\nu)$
from optimal point point $x^\ast$
(even though we do not know optimal solution)

</li>
<li>
	for this reason,
$(\lambda,\nu)$, called <span class="define">certificate of suboptimality</span>

</li>
<li>
	$x$ is $\epsilon$-suboptimal for primal problem
and
$(\lambda,\nu)$ is $\epsilon$-suboptimal for dual problem

</li>
<li>
	strong duality means we <i>could</i>
find arbitrarily small certificate of suboptimality

</li>
</ul>


<h3>Complementary slackness</h3>

<ul>
<li>
	assume strong duality holds for optimization problem
in <a href="#definition:optimization---problems"></a>
and assume $x^\ast$ is primal optimum and $(\lambda^\ast,\nu^\ast)$ is dual optimum,
then

$$
\fobj(x^\ast)
= L(x^\ast,\lambda^\ast,\nu^\ast)
= \fobj(x^\ast) + {\lambda^\ast}^T \fie(x^\ast) + {\nu^\ast}^T \feq(x^\ast)
$$


</li>
<li>
	$\feq(x^\ast)=0$ implies ${\lambda^\ast}^T \fie(x^\ast)=0$

</li>
<li>
	then $\lambda^\ast \succeq 0$ and $\fie(x^\ast) \preceq 0$ imply

$$
\lambda_i^\ast \fie_i(x^\ast) = 0
\quad
i=1,\ldots,m
$$


</li>
</ul>
<div class="proposition" id="proposition:complementary---slackness" data-name="complementary slackness">
	
when strong duality holds,
for primal and dual optimal points $x^\ast$ and $(\lambda^\ast, \nu)$

$$
\lambda_i^\ast \fie_i(x^\ast) = 0
\quad
i=1,\ldots,m
$$

this property, called <span class="define">complementary slackness</span>

</div>


<h3>KKT optimality conditions</h3>

<div class="definition" id="definition:KKT---optimality---conditions" data-name="KKT optimality conditions">
	
for optimization problem in <a href="#definition:optimization---problems"></a>
where $\fobj$, $\fie$, and $\feq$ are all differentiable,
below conditions
for ${x}\in\optdomain$ and $({\lambda}, {\nu})\in\reals^m\times\reals^p$

$$
\begin{eqnarray*}
\fie({x})
&\preceq&
0
\quad
\mbox{- primal feasibility}
\\
\feq(x)
&=&
0
\quad
\mbox{- primal feasibility}
\\
\lambda
&\succeq&
0
\quad
\mbox{- dual feasibility}
\\
{\lambda}^T \fie({x})
&=&
0
\quad
\mbox{- complementary slackness}
\\
\nabla_x L(x,\lambda,\nu)
&=&
0
\quad
\mbox{- vanishing gradient of Lagrangian}
\end{eqnarray*}
$$

called <span class="define">Karush-Kuhn-Tucker (KKT) optimality conditions</span>

</div>

<h3>KKT necessary for optimality with strong duality</h3>

<div class="theorem" id="theorem:KKT---necessary---for---optimality---with---strong---duality" data-name="KKT necessary for optimality with strong duality">
	
for optimization problem in <a href="#definition:optimization---problems"></a>
where $\fobj$, $\fie$, and $\feq$ are all differentiable,
if strong duality holds,
primal and dual optimal solutions $x^\ast$ and $(\lambda^\ast, \nu)$
satisfy KKT optimality conditions (in <a href="#definition:KKT---optimality---conditions"></a>),
<i>i.e.</i>,
for every optimization problem

	<ul>
	<li>
		when strong duality holds,
KKT optimality conditions are necessary for primal and dual optimality

	</li>
	<li>
		
or equivalently

	</li>
	<li>
		primal and dual optimality with strong duality imply KKT optimality conditions

	</li>
	</ul>

</div>

<h3>KKT and convexity sufficient for optimality with strong duality</h3>

<ul>
<li>
	assume convex optimization problem where $\fobj$, $\fie$, and $\feq$ are all differentiable
and ${x}\in\optdomain$ and $({\lambda}, {\nu})\in\reals^m\times\reals^p$
satisfying KKT conditions,
<i>i.e.</i>

$$
\fie({x}) \preceq 0, \; \feq({x}) = 0
, \;
{\lambda} \succeq 0
, \;
{\lambda}^T \fie({x}) = 0
, \;
\nabla_x L({x}, {\lambda},{\nu}) = 0
$$


</li>
<li>
	since $L(x,\lambda,\nu)$ is convex for $\lambda\succeq 0$,
<i>i.e.</i>,
each of $\fobj(x)$, $\lambda^T \fie(x)$, and $\nu^T \feq(x)$
is convex,
vanishing gradient implies $x$ achieves infimum for Lagrangian,
hence

$$
g(\lambda,\nu) = L(x,\lambda,\nu)
= \fobj(x) + \lambda^T \fie(x) + \nu^T \feq(x)
= f(x)
$$


</li>
<li>
	thus, strong duality holds,
<i>i.e.</i>,
$x$ and $(\lambda,\nu)$ are primal and dual optimal solutions
with zero duality gap

</li>
</ul>




<div class="theorem" id="theorem:KKT---and---convexity---sufficient---for---optimality---with---strong---duality" data-name="KKT and convexity sufficient for optimality with strong duality">
	
for convex optimization problem in <a href="#definition:convex---optimization"></a>
where $\fobj$, $\fie$, and $\feq$ are all differentiable,
if ${x}\in\optdomain$ and $({\lambda}, {\nu})\in\reals^m\times\reals^p$
satisfy KKT optimality conditions (in <a href="#definition:KKT---optimality---conditions"></a>),
they are primal and dual optimal solutions having zero duality gap
<i>i.e.</i>

	<ul>
	<li>
		for convex optimization problem,
KKT optimality conditions are sufficient for primal and dual optimality with strong duality

	</li>
	<li>
		
or equivalently

	</li>
	<li>
		KKT optimality conditions and convexity
imply primal and dual optimality and strong duality

	</li>
	</ul>

</div>
<ul>
<li>
	<a href="#theorem:KKT---necessary---for---optimality---with---strong---duality"></a>
together with
<a href="#theorem:KKT---and---convexity---sufficient---for---optimality---with---strong---duality"></a>
implies
that
for convex optimization problem
	<ul>
	<li>
		<i>
KKT optimality conditions are necessary and sufficient
for primal and dual optimality with strong duality
</i>

	</li>
	</ul>

</li>
</ul>

<h3>Solving primal problems via dual problems</h3>

<div id="page:Solving---primal---problems---via---dual---problems"></div>
<ul>
<li>
	when strong duality holds,
can retrieve primal optimum from dual optimum
since
primal optimal solution is minimize of

$$
L(x,\lambda^\ast,\nu^\ast)
$$

where $(\lambda^\ast, \nu^\ast)$ is dual optimum

</li>
<li>
	example - entropy maximization
($\optdomain = \pprealk{n}$)
	<ul>
	<li>
		primal problem - 

	</li>
	<li>
		dual problem - 

	</li>
	<li>
		provided dual optimum $(\lambda^\ast,\nu^\ast)$,
primal optimum is

$$
x^\ast
= \argmin_{x\in\optdomain}
\left(
\sum x_i \log x_i + {\lambda^\ast}^T (Ax-b) + \nu^\ast(\ones^Tx -1)
\right)
$$


	</li>
	<li>
		$\nabla_x L(x,\lambda^\ast,\nu^\ast) = \log x + A^T \lambda^\ast + (1+\nu^\ast)\ones$,
hence

$$
x^\ast = \exp(-(A^T \lambda^\ast + (1+\nu^\ast)\ones))
$$


	</li>
	</ul>

</li>
</ul>


<h3>Perturbed optimization problems</h3>

<div id="page:Perturbed---optimization---problems"></div>
<ul>
<li>
	original problem in <a href="#definition:optimization---problems"></a>
with perturbed constraints

$$
\begin{array}{ll}
\mbox{minimize} &
\fobj(x)
\\
\mbox{subject to} &
\fie(x) \preceq u
\\ &
\feq(x) =v
\end{array}
$$

where $u\in\reals^m$ and $v\in\reals^p$

</li>
<li>
	define $p^\ast(u,v)$ as optimal value of above <i>perturbed</i> problem,
<i>i.e.</i>

$$
p^\ast(u,v) = \inf\set{\fobj(x)}{x\in\optdomain, \fie(x) \preceq u, \feq(x) = v}
$$

which is convex
when problem is convex optimization problem

- note
$p^\ast(0,0)=p^\ast$

</li>
<li>
	assume and dual optimum $(\lambda^\ast,\nu^\ast)$,
if strong duality holds,
for every feasible $x$ for perturbed problem

$$
p^\ast(0,0)=g(\lambda^\ast,\nu^\ast)
\leq \fobj(x) + {\lambda^\ast}^T \fie(x) + {\nu^\ast}^T \feq(x)
\leq \fobj(x) + {\lambda^\ast}^T u + {\nu^\ast}^T v
$$

thus

$$
p^\ast(0,0)\leq p^\ast(u,v) + {\lambda^\ast}^T u + {\nu^\ast}^T v
$$

hence

$$
p^\ast(u,v)\geq p^\ast(0,0) - {\lambda^\ast}^T u - {\nu^\ast}^T v
$$


</li>
<li>
	the figure
shows this for optimization problem
with one inequality constraint and no equality constraint

</li>
</ul>




<div id="fig:sensitivity---analysis---of---optimal---value"></div>




<h3>Global sensitivity analysis via perturbed problems</h3>

<ul>
<li>
	recall

$$
p^\ast(u,v)\geq p^\ast(0,0) - {\lambda^\ast}^T u - {\nu^\ast}^T v
$$


</li>
<li>
	interpretations
	<ul>
	<li>
		if $\lambda^\ast_i$ is large, when $i$-th inequality constraint is tightened,
optimal value increases a lot

	</li>
	<li>
		if $\lambda^\ast_i$ is small, when $i$-th inequality constraint is relaxed,
optimal value decreases not a lot

	</li>
	<li>
		if $|\nu^\ast_i|$ is large,
reducing $v_i$ when $\nu^\ast_i>0$ or increasing $v_i$ when $\nu^\ast_i<0$
increases optimval value a lot

	</li>
	<li>
		if $|\nu^\ast_i|$ is small,
increasing $v_i$ when $\nu^\ast_i>0$ or decreasing $v_i$ when $\nu^\ast_i<0$
decreases optimval value not a lot

	</li>
	</ul>

</li>
<li>
	it only gives lower bounds - will explore local behavior

</li>
</ul>


<h3>Local sensitivity analysis via perturbed problems</h3>

<ul>
<li>
	assume $p^\ast(u,v)$ is differentiable with respect to $u$ and $v$,
<i>i.e.</i>, $\nabla_{(u,v)} p^\ast(u,v)$ exist
	<ul>
	<li>
		then

$$
\frac{\partial}{\partial u_i} p^\ast (0,0)
=
\lim_{h\to 0^+} \frac{p^\ast(he_i,0) - p^\ast(0,0)}{h}
\geq
\lim_{h\to 0^+} \frac{-{\lambda^\ast}^T (he_i) }{h}
=
-\lambda_i
$$

and

$$
\frac{\partial}{\partial u_i} p^\ast (0,0)
=
\lim_{h\to 0^-} \frac{p^\ast(he_i,0) - p^\ast(0,0)}{h}
\leq
\lim_{h\to 0^-} \frac{-{\lambda^\ast}^T (he_i) }{h}
=
-\lambda_i
$$


	</li>
	<li>
		obtain same result for $v_i$, hence

$$
\nabla_u\; p^\ast (0,0) = -\lambda
\quad
\nabla_v\; p^\ast (0,0) = -\nu
$$


	</li>
	</ul>

</li>
<li>
	so larger $\lambda_i$ or $|\nu_i|$ means larger change in optimal value of perturbed problem
when $u_i$ or $v_i$ change a bit and vice versa
quantitatively, - $\lambda_i$ an $\nu_i$ provide exact ratio and direction

</li>
</ul>

<h3>Different dual problems for equivalent optimization problems - 1</h3>

<ul>
<li>
	introducing new variables and equality constraints
for unconstrained problems
	<ul>
	<li>
		unconstrained optimization problem

$$
\begin{array}{ll}
\mbox{minimize} &
f(Ax+b)
\end{array}
$$

		<ul>
		<li>
			dual Lagrange function is $g = p^\ast$,
hence strong duality holds,
which, however, does not provide useful information

		</li>
		</ul>

	</li>
	<li>
		reformulate as equivalent optimization problem

$$
\begin{array}{ll}
\mbox{minimize} &
f(y)
\\
\mbox{subject to} &
Ax+b = y
\end{array}
$$

		<ul>
		<li>
			Lagrangian
-
$L(x,y,\nu) = f(y) + \nu^T(Ax+b-y)$

		</li>
		<li>
			Lagrange dual function
-
$g(\nu) = -I(A^T\nu = 0) + b^T\nu - f^\ast(\nu)$

		</li>
		<li>
			dual optimization problem

$$
\begin{array}{ll}
\mbox{maximize} &
b^T\nu - f^\ast(\nu)
\\
\mbox{subject to} &
A^T \nu = 0
\end{array}
$$


		</li>
		</ul>

	</li>
	</ul>

</li>
</ul>




<ul>
<li>
	examples
	<ul>
	<li>
		unconstrained geometric problem

$$
\begin{array}{ll}
\mbox{minimize} &
\log\left(
\sum_{i=1}^m \exp(a_i^Tx + b_i)
\right)
\end{array}
$$

		<ul>
		<li>
			reformulation

$$
\begin{array}{ll}
\mbox{minimize} &
\log\left(
\sum_{i=1}^m \exp(y_i)
\right)
\\
\mbox{subject to} &
Ax + b =y
\end{array}
$$


		</li>
		<li>
			dual optimization problem

$$
\begin{array}{ll}
\mbox{maximize} &
b^T \nu - \sum_{i=1}^m \nu_i \log \nu_i
\\
\mbox{subject to} &
\ones^T \nu = 1
\\ &
A^T \nu = 0
\\ &
\nu \succeq 0
\end{array}
$$

which is
entropy maximization problem

		</li>
		</ul>

	</li>
	<li>
		norm minimization problem

$$
\begin{array}{ll}
\mbox{minimize} &
\|Ax-b\|
\end{array}
$$

		<ul>
		<li>
			reformulation

$$
\begin{array}{ll}
\mbox{minimize} &
\|y\|
\\
\mbox{subject to} &
Ax - b = y
\end{array}
$$


		</li>
		<li>
			dual optimization problem

$$
\begin{array}{ll}
\mbox{maximize} &
b^T \nu
\\
\mbox{subject to} &
\|\nu\|_\ast \leq 1
\\ &
A^T \nu =0
\end{array}
$$


		</li>
		</ul>

	</li>
	</ul>

</li>
</ul>


<h3>Different dual problems for equivalent optimization problems - 2</h3>

<ul>
<li>
	introducing new variables and equality constraints
for constrained problems
	<ul>
	<li>
		inequality constrained optimization problem

$$
\begin{array}{ll}
\mbox{minimize} &
f_0(A_0x+b_0)
\\
\mbox{subject to} &
f_i(A_ix+b_i) \leq 0\quad i=1,\ldots,m
\end{array}
$$


	</li>
	<li>
		reformulation

$$
\begin{array}{ll}
\mbox{minimize} &
f_0(y_0)
\\
\mbox{subject to} &
f_i(y_i) \leq 0\quad i=1,\ldots,m
\\ &
A_i x + b_i = y_i\quad i=0,\ldots,m
\end{array}
$$


	</li>
	<li>
		dual optimization problem

$$
\begin{array}{ll}
\mbox{maximize} &
\sum_{i=0}^m \nu_i^T b_i - f_0^\ast(\nu_0)
- \sum_{i=1}^m \lambda_i f_i^\ast(\nu_i/\lambda_i)
\\
\mbox{subject to} &
\sum_{i=0}^m A_i^T \nu_i = 0
\\ &
\lambda \succeq 0
\end{array}
$$


	</li>
	</ul>

</li>
</ul>




<ul>
<li>
	examples
	<ul>
	<li>
		inequality constrained geometric program

$$
\begin{array}{ll}
\mbox{minimize} &
\log\left(\sum \exp(A_0x + b_0)\right)
\\
\mbox{subject to} &
\log\left(\sum \exp(A_ix + b_i)\right)\leq 0\quad i=1,\ldots,m
\end{array}
$$

where $A_i\in\reals^{K_i\times n}$
and $\exp(z) := (\exp(z_1),\ldots,\exp(z_k)))\in\reals^n$
and $\sum z := \sum_{i=1}^k z_i\in\reals$
for $z\in\reals^k$
		<ul>
		<li>
			reformulation

$$
\begin{array}{ll}
\mbox{minimize} &
\log\left(\sum \exp(y_0)\right)
\\
\mbox{subject to} &
\log\left(\sum \exp(y_i)\right)\leq 0\quad i=1,\ldots,m
\\ &
A_i x + b_i = y_i \quad i=0,\ldots,m
\end{array}
$$



		</li>
		<li>
			dual optimization problem

$$
\begin{array}{ll}
\mbox{maximize} &
\sum_{i=0}^m b_i^T \nu_i
- \nu_0^T\log(\nu_0)
- \sum_{i=1}^m \nu_i^T\log(\nu_i/\lambda_i)
\\
\mbox{subject to} &
\nu_i \succeq 0\quad i=0,\ldots,m
\\ &
\ones^T \nu_0 = 1,\; \ones^T\nu_i=\lambda_i\quad i=1,\ldots,m
\\ &
\lambda_i\geq 0 \quad i=1,\ldots,m
\\ &
\sum_{i=0}^m A_i^T\nu_i = 0
\end{array}
$$

where
and $\log(z) := (\log(z_1),\ldots,\log(z_k)))\in\reals^n$
for $z\in\pprealk{k}$


		</li>
		<li>
			simplified dual optimization problem

$$
\begin{array}{ll}
\mbox{maximize} &
\sum_{i=0}^m b_i^T \nu_i
- \nu_0^T\log(\nu_0)
- \sum_{i=1}^m \nu_i^T\log(\nu_i/\ones^T\nu_i)
\\
\mbox{subject to} &
\nu_i \succeq 0\quad i=0,\ldots,m
\\ &
\ones^T \nu_0 = 1
\\ &
\sum_{i=0}^m A_i^T\nu_i = 0
\end{array}
$$


		</li>
		</ul>

	</li>
	</ul>

</li>
</ul>


<h3>Different dual problems for equivalent optimization problems - 3</h3>

<ul>
<li>
	transforming objectives
	<ul>
	<li>
		norm minimization problem

$$
\begin{array}{ll}
\mbox{minimize} &
\|Ax - b\|
\end{array}
$$


	</li>
	<li>
		reformulation

$$
\begin{array}{ll}
\mbox{minimize} &
(1/2)\|y\|^2
\\
\mbox{subject to} &
Ax - b = y
\end{array}
$$


	</li>
	<li>
		dual optimization problem

$$
\begin{array}{ll}
\mbox{maximize} &
-(1/2)\|\nu\|_\ast^2 + b^T\nu
\\
\mbox{subject to} &
A^T\nu = 0
\end{array}
$$


	</li>
	</ul>

</li>
</ul>


<h3>Different dual problems for equivalent optimization problems - 4</h3>

<ul>
<li>
	making contraints implicit
	<ul>
	<li>
		LP with box constraints

$$
\begin{array}{ll}
\mbox{minimize} &
c^T x
\\
\mbox{subject to} &
Ax = b,\;
l \preceq x \preceq u
\end{array}
$$


	</li>
	<li>
		dual optimization problem

$$
\begin{array}{ll}
\mbox{maximize} &
-b^T\nu - \lambda_1^Tu + \lambda_2^Tl
\\
\mbox{subject to} &
A^T\nu + \lambda_1 - \lambda_2 + c = 0,\;
\lambda_1 \succeq 0,\; \lambda_2 \succeq 0
\end{array}
$$


	</li>
	<li>
		reformulation

$$
\begin{array}{ll}
\mbox{minimize} &
c^T x
+ I ( l\preceq x \preceq u)
\\
\mbox{subject to} &
Ax = b
\end{array}
$$


	</li>
	<li>
		dual optimization problem for reformulated primal problem

$$
\begin{array}{ll}
\mbox{maximize} &
-b^T \nu
- u^T(A^T\nu + c)^-
+ l^T(A^T\nu + c)^+
\end{array}
$$


	</li>
	</ul>

</li>
</ul>


<h2 id="title-page:Theorems---of---Alternatives">Theorems of Alternatives</h2>


<h3>Weak alternatives</h3>

<div class="theorem" id="theorem:weak---alternatives---of---two---systems" data-name="weak alternatives of two systems">
	
for $\fie: \xie\to\reals^m$ &amp; $\feq: \xeq\to\reals^p$
where $\xie$ and $\xeq$ are subsets of common set $\xdomain$,
which is subset of Banach space,
assuming $\optdomain = \xie \cap \xeq \neq \emptyset$,
and
$\lambda\in\reals^m$ &amp; $\nu\in\reals^p$,
below two systems of inequalities and equalities are weak alternatives,
<i>i.e.</i>, at most one of them is feasible

$$
\fie(x) \preceq 0
\quad
\feq(x) =0
$$

and

$$
\lambda \succeq 0
\quad
\inf_{x\in\optdomain}
\left(
\lambda^T \fie(x) + \nu^T \feq(x)
\right)
>0
$$


</div>
<ul>
<li>
	can prove <a href="#theorem:weak---alternatives---of---two---systems"></a>
using duality of optimization problems

</li>
<li>
	consider primal and dual problems
	<ul>
	<li>
		primal problem

$$
\begin{array}{ll}
\mbox{minimize} &
0
\\
\mbox{subject to} &
\fie(x) \preceq 0
\\ &
\feq(x) =0
\end{array}
$$


	</li>
	<li>
		dual problem

$$
\begin{array}{ll}
\mbox{maximize} &
g(\lambda,\nu)
\\
\mbox{subject to} &
\lambda \succeq 0
\end{array}
$$

where

$$
g(\lambda,\nu)
=
\inf_{x\in\optdomain}
\left(
\lambda^T \fie(x) + \nu^T \feq(x)
\right)
$$


	</li>
	</ul>

</li>
<li>
	then
$p^\ast,\; d^\ast \in \{0,\infty\}$

</li>
<li>
	now assume <i>first system of \theoremname~\ref{theorem:weak alternatives of two systems}\
is feasible,</i> then $p^\ast = 0$, hence
weak duality applies $d^\ast=0$,
thus there exist no $\lambda$ and $\nu$ such that $\lambda\succeq 0$
and $g(\lambda,\nu) > 0$
<i>i.e.</i>, <i>second system is infeasible,</i>
since otherwise there exist $\lambda$ and $\nu$
making $g(\lambda,\nu)$ arbitrarily large;
if $\tilde{\lambda}\succeq 0$ and $\tilde{\nu}$
satisfy $g({\lambda},{\nu})>0$,
$g(\alpha\tilde{\lambda}, \alpha\tilde{\nu}) = \alpha g(\tilde{\lambda}, \tilde{\nu})$
goes to $\infty$ when $\alpha\to\infty$

</li>
<li>
	assume <i>second system is feasible,</i>
then
$g(\lambda,\nu)$ can be arbitrarily large
for above reasons,
thus $d^\ast = \infty$,
hence weak duality implies $p^\ast = \infty$,
which implies
<i>first system is infeasible</i>

</li>
<li>
	therefore two systems are weak alternatives;
at most one of them is feasible

</li>
<li>
	
(actually, not hard to prove it without using weak duality)

</li>
</ul>

<h3>Weak alternatives with strict inequalities</h3>

<div class="theorem" id="theorem:weak---alternatives---of---two---systems---with---strict---inequalities" data-name="weak alternatives of two systems with strict inequalities">
	
for $\fie: \xie\to\reals^m$ &amp; $\feq: \xeq\to\reals^p$
where $\xie$ and $\xeq$ are subsets of common set $\xdomain$,
which is subset of Banach space,
assuming $\optdomain = \xie \cap \xeq \neq \emptyset$,
and
$\lambda\in\reals^m$ &amp; $\nu\in\reals^p$,
below two systems of inequalities and equalities are weak alternatives,
<i>i.e.</i>, at most one of them is feasible

$$
\fie(x) \prec 0
\quad
\feq(x) =0
$$

and

$$
\lambda \succeq 0
\quad
\lambda\neq 0
\quad
\inf_{x\in\optdomain}
\left(
\lambda^T \fie(x) + \nu^T \feq(x)
\right)
\geq
0
$$


</div>

<h3>Strong alternatives</h3>

<div class="theorem" id="theorem:strong---alternatives---of---two---systems" data-name="strong alternatives of two systems">
	
for convex $\fie: \xie\to\reals^m$ &amp; affine $\feq:\xeq\to\reals^p$
where $\xie$ and $\xeq$ are subsets $\reals^n$
assuming $\optdomain = \xie \cap \xeq \neq \emptyset$
and
$\lambda\in\reals^m$ &amp; $\nu\in\reals^p$,
if exists $x \in \relint \optdomain$ with $\feq(x)=0$,
below two systems of inequalities and equalities are strong alternatives,
<i>i.e.</i>, exactly one of them is feasible

$$
\fie(x) \preceq 0
\quad
\feq(x) =0
$$

and

$$
\lambda \succeq 0
\quad
\inf_{x\in\optdomain}
\left(
\lambda^T \fie(x) + \nu^T \feq(x)
\right)
>0
$$


</div>

<h3>Strong alternatives with strict inequalities</h3>

<div class="theorem" id="theorem:strong---alternatives---of---two---systems---with---strict---inequalities" data-name="strong alternatives of two systems with strict inequalities">
	
for convex $\fie: \xie\to\reals^m$ &amp; affine $\feq:\xeq\to\reals^p$
where $\xie$ and $\xeq$ are subsets $\reals^n$
assuming $\optdomain = \xie \cap \xeq \neq \emptyset$
and
$\lambda\in\reals^m$ &amp; $\nu\in\reals^p$,
if exists $x \in \relint \optdomain$ with $\feq(x)=0$,
below two systems of inequalities and equalities are strong alternatives,
<i>i.e.</i>, exactly one of them is feasible

$$
\fie(x) \prec 0
\quad
\feq(x) =0
$$

and

$$
\lambda \succeq 0
\quad
\lambda \neq 0
\quad
\inf_{x\in\optdomain}
\left(
\lambda^T \fie(x) + \nu^T \feq(x)
\right)
\geq
0
$$


</div>
<ul>
<li>
	proof -
consider convex optimization problem and its dual
	<ul>
	<li>
		primal problem

$$
\begin{array}{ll}
\mbox{minimize} &
s
\\
\mbox{subject to} &
\fie(x) - s \ones \preceq 0
\\ &
\feq(x) =0
\end{array}
$$


	</li>
	<li>
		dual problem

$$
\begin{array}{ll}
\mbox{maximize} &
g(\lambda,\nu)
\\
\mbox{subject to} &
\lambda \succeq 0
\quad
\ones^T \lambda = 1
\end{array}
$$

where
$g(\lambda,\nu)
=
\inf_{x\in\optdomain}
\left(
\lambda^T \fie(x) + \nu^T \feq(x)
\right)$

	</li>
	</ul>

</li>
<li>
	first observe Slater's condition
holds for primal problem
since by hypothesis of <a href="#theorem:strong---alternatives---of---two---systems---with---strict---inequalities"></a>,
exists $y\in\relint \optdomain$ with $\feq(y)=0$,
hence $(y,\fie(y))\in\xie\times \reals$
is primal feasible satisifying Slater's condition

</li>
<li>
	hence Slater's theorem (<a href="#theorem:Slater's---theorem"></a>)
implies
$d^\ast=p^\ast$

</li>
<li>
	assume first system
is feasible,
then primal problem is strictly feasible and $d^\ast = p^\ast<0$,
hence second system infeasible
since otherwise
feasible point for second system
is feasible point of dual problem,
hence $d^\ast\geq0$

</li>
<li>
	assume first system
is infeasible,
then $d^\ast = p^\ast\geq0$,
hence
Slater's theorem (<a href="#theorem:Slater's---theorem"></a>)
implies exists dual optimal $(\lambda^\ast,\nu^\ast)$ (whether or not $d^\ast=\infty$),
hence $(\lambda^\ast,\nu^\ast)$ is feasible point for second system
of <a href="#theorem:strong---alternatives---of---two---systems---with---strict---inequalities"></a>

</li>
<li>
	therefore
two systems are strong alternatives;
each is feasible if and only if the other is infeasible

</li>
</ul>

<h3>Strong alternatives for linear inequalities</h3>

<ul>
<li>
	dual function of feasibility problem for $Ax\preceq b$
is

$$
g(\lambda) = \inf_{x\in\reals^n} \lambda^T(Ax-b)
=
\left\{
\begin{array}{ll}
-b^T \lambda & A^T\lambda = 0
\\
-\infty & \mbox{otherwise}
\end{array}
\right.
$$


</li>
<li>
	hence
alternative system is $\lambda\succeq0,\;b^T\lambda <0,\; A^T\lambda=0$

</li>
<li>
	thus <a href="#theorem:strong---alternatives---of---two---systems"></a>
implies below systems are strong alternatives

$$
Ax \preceq b
\quad\&\quad
\lambda\succeq0 \quad b^T\lambda <0 \quad A^T\lambda=0
$$


</li>
<li>
	similarly
alternative system is $\lambda\succeq0,\;b^T\lambda <0,\; A^T\lambda=0$
and <a href="#theorem:strong---alternatives---of---two---systems"></a>
implies below systems are strong alternatives

$$
Ax \prec b
\quad\&\quad
\lambda\succeq0 \quad \lambda \neq 0 \quad b^T\lambda \leq 0 \quad A^T\lambda=0
$$


</li>
</ul>


<h3>Farkas' lemma</h3>

<div class="theorem" id="theorem:Farkas'---lemma" data-name="Farkas' lemma">
	
below systems of inequalities and equalities are strong alternatives

$$
Ax\preceq 0 \quad c^T x < 0
\quad \& \quad
A^T y + c = 0
\quad
y \succeq 0
$$


</div>

<ul>
<li>
	will prove <a href="#theorem:Farkas'---lemma"></a>
using LP and its dual

</li>
<li>
	consider LP
$\left(\mbox{minimize}\; c^T x \quad \mbox{subject to}\; Ax \preceq 0\right)$

</li>
<li>
	dual function is
$g(y)
=
\inf_{x\in\reals^n} \left(c^Tx + y^TAx \right)
=
\left\{
\begin{array}{ll}
0 & A^Ty + c= 0
\\
-\infty & \mbox{otherwise}
\end{array}
\right.$

</li>
<li>
	hence dual problem is
$\left(
\mbox{maximize}
\;
0
\quad
\mbox{subject to}
\;
A^T y + c = 0
,
\;
y \succeq 0
\right)$

</li>
<li>
	assume first system is feasible,
then homogeneity of primal problem implies $p^\ast = -\infty$,
thus $d^\ast$, <i>i.e.</i>, dual is infeasible,
hence second system is infeasible

</li>
<li>
	assume first system is infeasible,
since primal is always feasible,
$p^\ast=0$,
hence strong duality implies $d^\ast =0$,
thus second system is feasible

</li>
</ul>


<h2 id="title-page:Convex---Optimization---with---Generalized---Inequalities">Convex Optimization with Generalized Inequalities</h2>



<h3>Optimization problems with generalized inequalities</h3>

<div class="definition" id="definition:optimization---problems---with---generalized---inequalities" data-name="optimization problems with generalized inequalities">
	
for $\fobj:\xobj \to \reals$, $\fie: \xie\to \bigtimes_{i=1}^m \reals^{k_i}$, $\feq: \xeq \to \reals^p$
where $\xobj$, $\xie$, and $\xeq$ are subsets of common set $\xdomain$

$$
\begin{array}{ll}
\mbox{minimize}
& \fobj(x)
\\
\mbox{subject to}
& \fie(x) \preceq_\bigpropercone 0
\\
& \feq(x) =0
\end{array}
$$

called <span class="define">optimization problem with generalized inequalities</span>
where
$\bigpropercone = \bigtimes K_i$ is proper cone
with
$m$ proper cones
$K_1\subset \reals^{k_1},\ldots, K_n\subset \reals^{k_m}$

	<ul>
	<li>
		every terminology and associated notation is same
as of optimization problem in <a href="#definition:optimization---problems"></a>
such as
objective &amp; inequality &amp; equality contraint functions,
domain of optimization problem $\optdomain$,
feasible set $\optfeasset$,
optimal value $p^\ast$

	</li>
	<li>
		note that
when $K_i=\preals$ (hence $\bigpropercone=\prealk{m}$),
above optimization problem coincides with that in <a href="#definition:optimization---problems"></a>,
<i>i.e.</i>,
optimization problems with generalized inequalities
subsume
(normal) optimization problems

	</li>
	</ul>

</div>

<h3>Lagrangian for generalized inequalities</h3>

<div class="definition" id="definition:Lagrangian---for---generalized---inequalities" data-name="Lagrangian for generalized inequalities">
	
for optimization problem in
<a href="#definition:optimization---problems---with---generalized---inequalities"></a>
with nonempty domain $\optdomain$,
function $L:\optdomain \times \bigtimes_{i=1}^m \reals^{k_i} \times \reals^p \to \reals$
defined by

$$
L(x,\lambda, \nu) = \fobj(x) + \lambda^T \fie(x) + \nu^T \feq(x)
$$

called <span class="define">Lagrangian</span> associated with the optimization problem
where

	<ul>
	<li>
		every terminology and associated notation is same
as of optimization problem in <a href="#definition:Lagrangian"></a>
such as
dual variables or Lagrange multipliers $\lambda$ and $\nu$.

	</li>
	<li>
		Lagrangian for generalized inequalities
subsumes
(normal) Lagrangian (<a href="#definition:Lagrangian"></a>)

	</li>
	</ul>

</div>




<h3>Lagrange dual functions for generalized inequalities</h3>

<div class="definition" id="definition:Lagrange---dual---functions---for---generalized---inequalities" data-name="Lagrange dual functions for generalized inequalities">
	
for optimization problem in <a href="#definition:optimization---problems---with---generalized---inequalities"></a>
for which Lagrangian is defined,
function $g:\bigtimes \reals^{k_i} \times \reals^p \to \reals\cup \{-\infty\}$
defined by

$$
g(\lambda,\nu)
=
\inf_{x\in\optdomain} L(x,\lambda,\nu)
=
\inf_{x\in\optdomain} \left(\fobj(x) + \lambda^T \fie(x) + \nu^T \feq(x)\right)
$$

called
<span class="define">Lagrange dual function</span>
or just
<span class="define">dual function</span>
associated with optimization problem

	<ul>
	<li>
		Lagrange dual functions for generalized inequalities
subsume
(normal) Lagrange dual functions (<a href="#definition:Lagrange---dual---functions"></a>)

	</li>
	</ul>

</div>



<ul>
<li>
	$g$ is <i>concave function</i>

</li>
<li>
	$g(\lambda,\nu)$
is
lower bound for optimal value of associated optimization problem
<i>i.e.</i>,

$$
g(\lambda,\nu) \leq p^\ast
$$

for every $\lambda\succeq_\bigpropercone^\ast0$
where $\bigpropercone^\ast$ denotes dual cone of $\bigpropercone$,
<i>i.e.</i>,
$\bigpropercone^\ast = \bigtimes K_i^\ast$
where $K_i^\ast\subset\reals^{k_i}$ is dual cone of $K_i\subset\reals^{k_i}$

</li>
<li>
	$(\lambda,\nu)$
with $\lambda\succeq_\bigpropercone 0$ and $g(\lambda,\nu)>-\infty$
said to be <span class="define">dual feasible</span>

</li>
</ul>

<h3>Lagrange dual problems for generalized inequalities</h3>

<div class="definition" id="definition:Lagrange---dual---problems---for---generalized---inequalities" data-name="Lagrange dual problems for generalized inequalities">
	
for optimization problem in <a href="#definition:optimization---problems---with---generalized---inequalities"></a>,
optimization problem

$$
\begin{array}{ll}
\mbox{maximize} &
g(\lambda,\nu)
\\
\mbox{subject to} &
\lambda \succeq_{\bigpropercone^\ast} 0
\end{array}
$$

where $\bigpropercone^\ast$ denotes dual cone of $\bigpropercone$,
<i>i.e.</i>,
$\bigpropercone^\ast = \bigtimes K_i^\ast$
where $K_i^\ast\subset\reals^{k_i}$ is dual cone of $K_i\subset\reals^{k_i}$,
called <span class="define">Lagrange dual problem</span>
associated with problem in <a href="#definition:optimization---problems---with---generalized---inequalities"></a>

	<ul>
	<li>
		every terminology and related notation
is same as that in <a href="#definition:Lagrange---dual---problems"></a>
such as
dual feasibility,
dual optimal value $d^\ast$,
optimal Lagrange multipliers $(\lambda^\ast,\nu^\ast)$

	</li>
	<li>
		Lagrange dual problems for generalized inequalities
subsume
(normal) Lagrange dual problems (<a href="#definition:Lagrange---dual---problems"></a>)

	</li>
	</ul>

</div>


<ul>
<li>
	Lagrange dual problem in <a href="#definition:Lagrange---dual---problems---for---generalized---inequalities"></a>
is convex optimization
since $g(\lambda,\nu)$ is convex

</li>
</ul>


<h3>Slater's theorem for generalized inequalities</h3>

<div class="theorem" id="theorem:Slater's---theorem---for---generalized---inequalities" data-name="Slater's theorem for generalized inequalities">
	
if optimization problem
in <a href="#definition:optimization---problems---with---generalized---inequalities"></a>
is convex,
<i>i.e.</i>,
$\fobj$ is convex,
$\fie$ is $\bigpropercone$-convex
(<i>i.e.</i>, every $\fie_i$ is $K_i$-convex)
(<a href="#definition:$K$-convex---functions"></a>),
and exists feasible $x\in\optdomain$ contained in $\relint \optdomain$
such that

$$
\fie(x) \prec_\bigpropercone\ 0\quad \feq(x) = 0
$$

<i>strong duality</i> holds
(and <i>dual optimal value is attained when $d^\ast>-\infty$</i>)

	<ul>
	<li>
		such condition, called <span class="define">Slater's condition</span>

	</li>
	<li>
		such point, (sometimes) said to be <span class="define">strictly feasible</span>

	</li>
	<li>
		note resemblance with Slater's theorem in <a href="#theorem:Slater's---theorem"></a>

	</li>
	</ul>

</div>

<h3>Duality for SDP</h3>

<ul>
<li>
	(inequality form) SDP
<div id="page:(inequality---form)---SDP"></div>

$$
\begin{array}{ll}
\mbox{minimize} &
c^Tx
\\
\mbox{subject to} &
x_1F_1 + \cdots + x_nF_n + G \preceq 0
\end{array}
$$

where $F_1,\ldots,F_n,G\in\symset{k}$
and $\bigpropercone = \possemidefset{k}$

</li>
<li>
	Lagrangian

$$
L(x,Z)
= c^Tx + (x_1F_1 + \cdots + x_nF_n + G) \bullet Z
= \sum x_i(F_i\bullet Z + c_i) + G \bullet Z
$$

where $X\bullet Y = \Tr XY$ for $X,Y\in\symset{k}$

</li>
<li>
	Lagrange dual function

$$
g(Z) = \inf_{x\in\reals^n} L(x,Z)
=
\left\{
\begin{array}{ll}
G \bullet Z & F_i\bullet Z + c_i= 0\quad i=1,\ldots,n
\\
-\infty & \mbox{otherwise}
\end{array}
\right.
$$


</li>
<li>
	Lagrange dual problem
<div id="page:dual---of---SDP"></div>

$$
\begin{array}{ll}
\mbox{maximize} &
G\bullet Z
\\
\mbox{subject to} &
F_i \bullet Z + c_i = 0\quad i=1,\ldots,n
\\ &
Z \succeq 0
\end{array}
$$

where fact that $\possemidefset{k}$ is self-dual,
<i>i.e.</i>,
$\bigpropercone^\ast = \bigpropercone$

</li>
<li>
	Slater's theorem (<a href="#theorem:Slater's---theorem---for---generalized---inequalities"></a>)
implies if primal problem is strictly feasible,
<i>i.e.</i>,
exists $x\in\reals^n$ such that $\sum x_iF_i + G\prec 0$,
strong duality holds

</li>
</ul>

<h3>KKT optimality conditions for generalized inequalities</h3>

<div class="definition" id="definition:KKT---optimality---conditions---for---generalized---inequalities" data-name="KKT optimality conditions for generalized inequalities">
	
for optimization problem in <a href="#definition:optimization---problems---with---generalized---inequalities"></a>
where $\fobj$, $\fie$, and $\feq$ are all differentiable,
below conditions
for ${x}\in\optdomain$ and $({\lambda}, {\nu})\in\bigtimes \reals^{k_i} \times\reals^p$

$$
\begin{eqnarray*}
\fie({x})
&\preceq_\bigpropercone&
0
\quad
\mbox{- primal feasibility}
\\
\feq(x)
&=&
0
\quad
\mbox{- primal feasibility}
\\
\lambda
&\succeq_{\bigpropercone^\ast}&
0
\quad
\mbox{- dual feasibility}
\\
{\lambda}^T \fie({x})
&=&
0
\quad
\mbox{- complementary slackness}
\\
\nabla_x L(x,\lambda,\nu)
&=&
0
\quad
\mbox{- vanishing gradient of Lagrangian}
\end{eqnarray*}
$$

called <span class="define">Karush-Kuhn-Tucker (KKT) optimality conditions</span>

	<ul>
	<li>
		note KKT optimality conditions for generalized inequalities
subsume
(normal) KKT optimality conditions
(<a href="#definition:KKT---optimality---conditions"></a>)

	</li>
	</ul>

</div>

<h3>KKT conditions and optimalities for generalized inequalities</h3>

<ul>
<li>
	for every optimization problem with generalized inequalities
(<a href="#definition:optimization---problems---with---generalized---inequalities"></a>),
every statement for normal optimization problem
(<a href="#definition:optimization---problems"></a>),
regarding relations among
KKT conditions,
optimality,
primal and dual optimality,
and
strong duality,
is <i>exactly the same</i>
	<ul>
	<li>
		for every optimization problem with generalized inequalities
(<a href="#definition:optimization---problems---with---generalized---inequalities"></a>)
		<ul>
		<li>
			if strong duality holds,
primal and dual optimal points satisfy KKT optimality conditions
in <a href="#definition:KKT---optimality---conditions---for---generalized---inequalities"></a>
(same as <a href="#theorem:KKT---necessary---for---optimality---with---strong---duality"></a>)

		</li>
		<li>
			if optimization problem is convex and
primal and dual solutions satisfy KKT optimality conditions
in <a href="#definition:KKT---optimality---conditions---for---generalized---inequalities"></a>,
the solutions are optimal with strong duality
(same as <a href="#theorem:KKT---and---convexity---sufficient---for---optimality---with---strong---duality"></a>)

		</li>
		<li>
			therefore,
for convex optimization problem,
<i>KKT optimality conditions are necessary and sufficient
for primal and dual optimality with strong duality</i>

		</li>
		</ul>

	</li>
	</ul>

</li>
</ul>


<h3>Perturbation and sensitivity analysis for generalized inequalities</h3>

<ul>
<li>
	original problem in <a href="#definition:optimization---problems---with---generalized---inequalities"></a>
with perturbed constraints

$$
\begin{array}{ll}
\mbox{minimize} &
\fobj(x)
\\
\mbox{subject to} &
\fie(x) \preceq_\bigpropercone u
\\ &
\feq(x) =v
\end{array}
$$

where $u\in\reals^m$ and $v\in\reals^p$

</li>
<li>
	define $p^\ast(u,v) = p^\ast(u,v) = \inf\set{\fobj(x)}{x\in\optdomain, \fie(x) \preceq u, \feq(x) = v}$,
which is convex when problem is convex optimization problem
- note
$p^\ast(0,0)=p^\ast$

</li>
<li>
	as for normal optimization problem case (page~<a href="#page:Perturbed---optimization---problems">here</a>),
if and dual optimum $(\lambda^\ast,\nu^\ast)$,
if strong duality holds,

$$
p^\ast(u,v)\geq p^\ast(0,0) - {\lambda^\ast}^T u - {\nu^\ast}^T v
$$

and

$$
\nabla_u\; p^\ast (0,0) = -\lambda
\quad
\nabla_v\; p^\ast (0,0) = -\nu
$$


</li>
</ul>

<h3>Sensitivity analysis for SDP</h3>

<ul>
<li>
	assume inequality form SDP and its dual problem
on page~<a href="#page:(inequality---form)---SDP">here</a> and page~<a href="#page:dual---of---SDP">here</a>

</li>
<li>
	consider perturbed SDP

$$
\begin{array}{ll}
\mbox{minimize} &
c^Tx
\\
\mbox{subject to} &
x_1F_1 + \cdots + x_nF_n + G \preceq U
\end{array}
$$

for some $U\in\symset{k}$
	<ul>
	<li>
		define $p^\ast:\symset{k} \to \reals$
such that
$p^\ast(U)$ is optimal value of above problem

	</li>
	</ul>

</li>
<li>
	assume $x^\ast\in\reals^n$ and $Z^\ast\in\possemidefset{k}$
are primal and dual optimum with zero dualty gap

</li>
<li>
	then

$$
p^\ast(U) \geq p^\ast - Z^\ast \bullet U
$$


</li>
<li>
	if $\nabla_U p^\ast$ exists at $U=0$

$$
\nabla_U p^\ast(0) = - Z^\ast
$$


</li>
</ul>


<h3>Weak alternatives for generalized inequalities</h3>

<div class="theorem" id="theorem:weak---alternatives---for---generalized---inequalities" data-name="weak alternatives for generalized inequalities">
	
for $\fie:\xie \to \bigtimes \reals^{k_i}$ &amp; $\feq:\xeq \to \reals^p$
where $\xie$ and $\xeq$ are subsets of common Banach space
assuming $\optdomain = \xie \cap \xeq \neq \emptyset$,
and $\lambda \in \bigtimes \reals^{k_i}$ &amp; $\nu \in \reals^p$,
below pairs of systems are strong alternatives

$$
\begin{eqnarray*}
\fie(x) \preceq_\bigpropercone 0
\quad
\feq(x) = 0
\quad
&
\&
&
\quad
\lambda\succeq_{\bigpropercone^\ast} 0
\quad
g(\lambda,\nu) > 0
\\
\fie(x) \prec_\bigpropercone 0
\quad
\feq(x) = 0
\quad
&
\&
&
\quad
\lambda\succeq_{\bigpropercone^\ast} 0
\quad
\lambda \neq 0
\quad
g(\lambda,\nu) \geq 0
\end{eqnarray*}
$$

where $\bigpropercone = \bigtimes K_i$ with proper cones $K_i\subset\reals^{k_i}$
and function $g:\bigtimes \reals^{k_i} \times \reals^p \to \reals$ defined by

$$
g(\lambda,\nu) = \inf_{x\in\optdomain} \left( \lambda^T \fie(x) + \nu^T \feq(x) \right)
$$

note this theorem subsumes
<a href="#theorem:weak---alternatives---of---two---systems"></a>
and
<a href="#theorem:weak---alternatives---of---two---systems---with---strict---inequalities"></a>

</div>

<h3>Strong alternatives for generalized inequalities</h3>

<div class="theorem" id="theorem:strong---alternatives---for---generalized---inequalities" data-name="strong alternatives for generalized inequalities">
	
for $\bigpropercone$-convex $\fie:\xie \to \bigtimes \reals^{k_i}$ &amp; affine $\feq:\xeq \to \reals^p$
where $\xie$ and $\xeq$ are subsets of $\reals^n$
assuming $\optdomain = \xie \cap \xeq \neq \emptyset$,
and $\lambda \in \bigtimes \reals^{k_i}$ &amp; $\nu \in \reals^p$,
if exists $x\in\relint \optdomain$ with $\feq(x)=0$,
below pairs of systems are strong alternatives

$$
\begin{eqnarray*}
\fie(x) \preceq_\bigpropercone 0
\quad
\feq(x) = 0
\quad
&
\&
&
\quad
\lambda\succeq_{\bigpropercone^\ast} 0
\quad
g(\lambda,\nu) > 0
\\
\fie(x) \prec_\bigpropercone 0
\quad
\feq(x) = 0
\quad
&
\&
&
\quad
\lambda\succeq_{\bigpropercone^\ast} 0
\quad
\lambda \neq 0
\quad
g(\lambda,\nu) \geq 0
\end{eqnarray*}
$$

where $\bigpropercone = \bigtimes K_i$ with proper cones $K_i\subset\reals^{k_i}$
and function $g:\bigtimes \reals^{k_i} \times \reals^p \to \reals$ defined by

$$
g(\lambda,\nu) = \inf_{x\in\optdomain} \left( \lambda^T \fie(x) + \nu^T \feq(x) \right)
$$

note this theorem subsumes
<a href="#theorem:strong---alternatives---of---two---systems"></a>
and
<a href="#theorem:strong---alternatives---of---two---systems---with---strict---inequalities"></a>

</div>

<h3>Strong alternatives for SDP</h3>

<ul>
<li>
	for $F_1,\ldots,F_n,G\in\symset{k}$, $x\in\reals^n$, and $Z\in\symset{k}$
	<ul>
	<li>
		below systems are strong alternatives

$$
x_1F_1 + \cdots + x_nF_n + G \prec 0
$$

and

$$
Z \succeq 0 \quad Z\neq 0 \quad G\bullet Z \geq 0
\quad F_i \bullet Z = 0\;i=1,\ldots,n
$$


	</li>
	<li>
		if $\sum v_i F_i \succeq 0 \Rightarrow \sum v_i F_i = 0$,
below systems are strong alternatives

$$
x_1F_1 + \cdots + x_nF_n + G \preceq 0
$$

and

$$
Z \succeq 0 \quad G\bullet Z > 0
\quad F_i \bullet Z = 0\;i=1,\ldots,n
$$


	</li>
	</ul>

</li>
</ul>


<h2 id="title-page:Unconstrained---Minimization">Unconstrained Minimization</h2>


<h3>Unconstrained minimization</h3>

<ul>
<li>
	consider
unconstrained convex optimization problem,
<i>i.e.</i>, $m=p=0$ in <a href="#definition:convex---optimization"></a>

$$
\begin{array}{ll}
\mbox{minimize} &
\fobj(x)
\end{array}
$$

where
domain of optimization problem is $\optdomain\ = \xobj \subset \reals^n$

</li>
<li>
	assume
	<ul>
	<li>
		$\fobj$ is twice-differentiable (hence by definition $\xobj$ is open)

	</li>
	<li>
		optimal solution $x^\ast$ exists, <i>i.e.</i>, $p^\ast = \inf_{x\in\optdomain} \fobj(x) = \fobj(x^\ast)$

	</li>
	</ul>

</li>
<li>
	<a href="#theorem:first-order---condition---for---convexity"></a>
implies
$x^\ast$ is optimal solution
if and only if

$$
\nabla \fobj(x^\ast) = 0
$$


</li>
<li>
	can solve above equation directly for few cases,
but usually
depend on iterative method,
<i>i.e.</i>,
find sequence of points $\xseqk{0}, \xseqk{1}, \ldots \in \xobj$
such that
$\lim_{k\to\infty} \fobj(\xseqk{k}) = p^\ast$

</li>
</ul>


<h3>Requirements for iterative methods</h3>

<ul>
<li>
	requirements for iterative methods
	<ul>
	<li>
		initial point $\xseqk{0}$ should be in domain of optimization problem,
<i>i.e.</i>

$$
\xseqk{0} \in \xobj\
$$


	</li>
	<li>
		sublevel set of $\fobj(\xseqk{0})$

$$
S = \bigset{x\in\xobj}{\fobj(x) \leq \fobj(\xseqk{0})}
$$

should be closed

	</li>
	</ul>

</li>
<li>
	<i>e.g.</i>
	<ul>
	<li>
		sublevel set of $\fobj(\xseqk{0})$
is closed for all $\xseqk{0}\in\xobj$
if $\fobj$ is closed, <i>i.e.</i>, all its sublevel sets are closed

	</li>
	<li>
		$\fobj$ is closed
if $\xobj = \reals^n$ and $\fobj$ is continuous

	</li>
	<li>
		$\fobj$ is closed
if $\fobj$ is continuous,
$\xobj$ is open,
and $\fobj(x) \to \infty$ as $x \to \boundary \xobj$

	</li>
	</ul>

</li>
</ul>


<h3>Unconstrained minimization examples</h3>

<ul>
<li>
	convex quadratic problem

$$
\begin{array}{ll}
\mbox{minimize} &
\fobj(x) =
(1/2) x^TP x +q^Tx
\end{array}
$$

where $P\in\possemidefset{n}$ and $q\in\reals^n$
	<ul>
	<li>
		solution obtained by solving

$$
\nabla \fobj(x^\ast) = P x^\ast + q = 0
$$

		<ul>
		<li>
			if solution exists, $x^\ast = - P^\dagger q$ (thus $p^\ast>-\infty$)

		</li>
		<li>
			otherwise, problem is unbounded below, <i>i.e.</i>, $p^\ast = -\infty$

		</li>
		</ul>

	</li>
	<li>
		<span class="eemph">
ability to analytically solve quadratic minimization problem
is basis for Newton's method,
power method for unconstrained minimization
</span>

	</li>
	<li>
		least-squares (LS) is special case of convex quadratic problem

$$
\begin{array}{ll}
\mbox{minimize} &
(1/2) \|Ax-b\|_2^2
= (1/2) x^T (A^TA) x - b^TAx + (1/2)\|b\|_2^2
\end{array}
$$

		<ul>
		<li>
			optimal always exists, can be obtained via normal equations

$$
A^T Ax^\ast = b
$$


		</li>
		</ul>

	</li>
	</ul>

</li>
<li>
	unconstrained GP

$$
\begin{array}{ll}
\mbox{minimize} &
\fobj(x) =
\log\left(
\sum \exp (Ax+b)
\right)
\end{array}
$$

for $A\in\reals^{m\times n}$ and $b\in\reals^m$
	<ul>
	<li>
		solution obtained by solving

$$
\nabla \fobj(x^\ast) = \frac{\sum A^T \exp(Ax^\ast+b)}{\sum \exp(Ax^\ast+b)} = 0
$$


	</li>
	<li>
		need to resort to iterative method -
since $\xobj = \reals^n$ and $\fobj$ is continuous,
$\fobj$ is closed,
hence
every point in $\reals^n$ can be initial point

	</li>
	</ul>

</li>
<li>
	analytic center of linear inequalities

$$
\begin{array}{ll}
\mbox{minimize} &
\fobj(x) = - \sum\log(b-Ax)
\end{array}
$$

where $\xobj = \set{x\in\reals^n}{b-Ax \succ 0}$
	<ul>
	<li>
		need to resort to iterative method -
since $\xobj$ is open, $\fobj$ is continuous,
and $\fobj(x) \to \infty$ as $x\to\boundary \xobj$,
$\fobj$ is closed,
hence
every point in $\xobj$ can be initial point

	</li>
	<li>
		$\fobj$, called <span class="define">logarithmic barrier</span> for inequalities $Ax\preceq b$

	</li>
	</ul>

</li>
<li>
	analytic center of LMI

$$
\begin{array}{ll}
\mbox{minimize} &
\fobj(x) = - \log\det F(x) = \log\det F(x)^{-1}
\end{array}
$$

where $F:\reals^n\to \symset{k}$ is defined by

$$
F(x) = x_1F_1 + \cdots + x_nF_n
$$

where $F_i\in \symset{k}$
and $\xobj = \set{x\in\reals^n}{F(x)\succ 0}$
	<ul>
	<li>
		need to resort to iterative method -
since $\xobj$ is open, $\fobj$ is continuous,
and $\fobj(x) \to \infty$ as $x\to\boundary \xobj$,
$\fobj$ is closed,
hence
every point in $\xobj$ can be initial point

	</li>
	<li>
		$\fobj$, called <span class="define">logarithmic barrier</span> for LMI

	</li>
	</ul>

</li>
</ul>


<h3>Strong convexity and implications</h3>

<ul>
<li>
	function $\fobj$ is strongly convex on $S$

$$
\left(
\exists m >0
\right)
\left(
\forall x \in S
\right)
\left(
\nabla^2 \fobj(x) \succeq mI
\right)
$$


</li>
<li>
	strong convexity implies for every $x,y\in S$

$$
\fobj(y) \geq \fobj(x) + \nabla \fobj(x)^T (y-x) + ({m}/{2}) \|y-x\|_2^2
$$

	<ul>
	<li>
		which implies
gradient provides optimality certificate
and tells us how far current point is from optimum,
<i>i.e.</i>

$$
\fobj(x) - p^\ast \leq ({1}/{2m}) \|\nabla \fobj(x)\|_2^2
\quad
\|x-x^\ast\|_2 \leq ({2}/{m}) \|\nabla \fobj(x)\|_2
$$


	</li>
	</ul>

</li>
<li>
	first equation implies sublevel sets contained in $S$ is bounded,
hence continuous function $\nabla^2 \fobj(x)$ is also bounded,
<i>i.e.</i>,
$\left( \exists M >0 \right) \left( \nabla^2 \fobj(x) \preceq M I \right)$,
then

$$
\fobj(x) - p^\ast \geq \frac{1}{2M} \|\nabla \fobj(x)\|_2^2
$$


</li>
</ul>


<h3>Iterative methods</h3>

<div class="definition" id="definition:iterative---meethods" data-name="iterative meethods">
	
numerical method generating sequence of points $\xseqk{0}, \xseqk{1}, \ldots \in S\subset \reals^n$
to make $\fobj(\xseqk{k})$ approaches to some desired value from some $f:S\to\reals$,
called <span class="define">iterative method</span>

</div>
<div class="definition" id="definition:iterative---meethods---with---search---directions" data-name="iterative meethods with search directions">
	
iterative method generating
search direction $\sdirk{k}\in\reals^n$ and
step length $\slenk{k}>0$ at each step $k$
such that

$$
\xseqk{k+1} = \xseqk{k} + \slenk{k} \sdirk{k}
$$

called <span class="define">iterative method with search direction</span>
where $\sdirk{k}$, called <span class="define">search direction</span>,
$\slenk{k}$, called <span class="define">step length</span> (which actually is not length)

</div>
<div class="definition" id="definition:descent---methods" data-name="descent methods">
	
for function $f:S\to\reals$,
iterative method reducing function value,
<i>i.e.</i>

$$
\fobj(\xseqk{k+1}) \leq \fobj(\xseqk{k})
$$

for $k=0,1,\ldots$,
called <span class="define">descent method</span>

</div>


<h3>Line search methods</h3>

<div class="definition" id="definition:line---search---method" data-name="line search method">
	
for iterating method with search directions,
determining
search direction $\sdirk{k}$
and
step length $\slenk{k}$
for each step,
called <span class="define">line search method</span>

</div>
<div class="algorithm" id="algorithm:exact---line---search" data-name="exact line search">
	
for descent iterating method with search directions,
determine $\slen$ by

$$
\slen = \argmin_{s>0} \fobj(x +s\sdir)
$$


</div>
<div class="algorithm" id="algorithm:backtracking---line---search" data-name="backtracking line search">
	
for descent iterating method with search directions,
determine $\slen$ by
<ul>
<li>
	<strong>Require:</strong>	$\fobj$, \sdirk{k}, $\alpha\in(0,0.5)$, $\beta\in(0,1)$ <strong></strong>
</li>

<li>
	<strong></strong>	$\slen:=1$ <strong></strong>
</li>

<li>
	<strong>while</strong>	$\fobj(\xseqk{k} + \slen \sdirk{k}) > \fobj(\xseqk{k}) + \alpha \slen \nabla \fobj(\xseqk{k})^T \sdirk{k}$ <strong>do</strong>
</li>

<li>
	<strong></strong>	$\slen := \beta \slen$ <strong></strong>
</li>

<li>
	<strong>end while</strong>
</li>
</ul>

</div>


<h3>Gradient descent method</h3>

<div class="algorithm" id="algorithm:gradient---descent---method" data-name="gradient descent method">
	
<ul>
<li>
	<strong>Require:</strong>	$\fobj$, initial point $x\in \dom \fobj$ <strong></strong>
</li>

<li>
	<strong>repeat</strong>
</li>
<li>
	<strong></strong>	search direction - $\sdir := - \nabla \fobj(x)$ <strong></strong>
</li>

<li>
	<strong></strong>	do line search to choose $\slen>0$ <strong></strong>
</li>

<li>
	<strong></strong>	update - $x := x + \slen \sdir$ <strong></strong>
</li>

<li>
	<strong>until</strong>	stopping criterion satisfied <strong></strong>
</li>

</ul>

</div>

<h3>Summary of gradient descent method</h3>

<ul>
<li>
	gradient method often exhibits approximately linear convergence,
<i>i.e.</i>,
error $\fobj(\xseqk{k})-p^\ast$ converges to zero approximately as geometric series

</li>
<li>
	choice of backtracking parameters $\alpha$ and $\beta$
has noticeable but not dramatic effect on convergence

</li>
<li>
	exact line search sometimes improves convergence of gradient method,
but not by large,
hence mostly not worth implementation

</li>
<li>
	converge rate depends greatly on condition number of Hessian
or sublevel sets
- when condition number if large, gradient method can be useless

</li>
</ul>


<h3>Newton's method - motivation</h3>

<ul>
<li>
	second-order Taylor expansion of $\fobj$
-
$\hat{\fobj}(\sdir) =
\fobj(x + \sdir) = \fobj(x) + \nabla \fobj(x)^T \sdir + \frac{1}{2} \sdir^T \nabla^2 \fobj(x) \sdir$

</li>
<li>
	minimum of Taylor expansion achieved when
$\nabla \hat{\fobj}(\sdir) = \nabla \fobj(x) + \nabla^2 \fobj(x) v = 0$

</li>
<li>
	solution called <span class="define">Newton step</span>

$$
\sdir_\mathrm{nt}(x) = - \nabla^2 \fobj(x)^{-1} \nabla \fobj(x)
$$

assuming $\nabla^2\fobj(x)\succ0$

</li>
<li>
	thus Newton step minimizes local quadratic approximation of function

</li>
<li>
	difference of current and quadratic approximation minimum

$$
\fobj(x) - \hat{\fobj}(\sdir_\mathrm{tn}(x))
=
\frac{1}{2} \sdir_\mathrm{nt}^T \nabla^2 \fobj(x) \sdir_\mathrm{nt}
=
\frac{1}{2} \lambda(x)^2
$$


</li>
<li>
	<span class="define">Newton decrement</span>


<div id="page:Newton---decrement---in---quadratic---approximation"></div>

$$
\lambda(x)
=
\sqrt{\sdir_\mathrm{nt}(x)^T \nabla^2 \fobj(x) \sdir_\mathrm{nt}(x)}
=
\sqrt{\nabla \fobj(x)^T \nabla^2 \fobj(x)^{-1} \nabla \fobj(x)}
$$


</li>
</ul>

<h3>Newton's method</h3>

<div class="algorithm" id="algorithm:Newton's---method" data-name="Newton's method">
	
damped descent method using Newton step
<ul>
<li>
	<strong>Require:</strong>	\fobj, initial point $x\in \dom \fobj$, tolerance $\epsilon>0$ <strong></strong>
</li>

<li>
	<strong>loop</strong>
</li>
<li>
	<strong></strong>	computer Newton step and descrement
$$
\sdir_\mathrm{nt}(x) := -\nabla^2 \fobj(x)^{-1} \nabla \fobj(x)
\quad
\lambda(x)^2 := \nabla \fobj(x)^T \nabla^2 \fobj(x)^{-1} \nabla \fobj(x)
$$
 <strong></strong>
</li>

<li>
	<strong></strong>	stopping criterion - quit if $\lambda(x)^2/2 < \epsilon$ <strong></strong>
</li>

<li>
	<strong></strong>	do line search to choose $t>0$ <strong></strong>
</li>

<li>
	<strong></strong>	update - $x := x + \slen \sdir_\mathrm{nt}$ <strong></strong>
</li>

<li>
	<strong>end loop</strong>
</li>
</ul>

</div>


<ul>
<li>
	Newton step is descent direction since

$$
\left.
\left(
\frac{d}{dx}\fobj(x+t\sdir_\mathrm{nt})
\right)
\right|_{t=0}
=
\nabla \fobj(x) ^T \sdir_\mathrm{nt}
=
- \lambda(x)^2
<0
$$


</li>
</ul>


<h3>Assumptions for convergence analysis of Newton's method</h3>

<ul>
<li>
	assumptions
	<ul>
	<li>
		strong convexity and boundedness of Hessian on sublevel set

$$
\left(
\exists\; m, M > 0
\right)
\left(
\forall x \in S
\right)
\left(
mI \preceq \nabla^2 \fobj(x) \preceq MI
\right)
$$


	</li>
	<li>
		Lipschitz continuity of Hessian on sublevel set

$$
\left(
\exists L > 0
\right)
\left(
\forall x,y\in S
\right)
\left(
\|\nabla^2 \fobj(x)- \nabla^2\fobj(y)\|_2 \leq L \|x-y\|_2
\right)
$$


	</li>
	</ul>

</li>
<li>
	Lipschitz continuity constant $L$ plays critical role
in performance of Newton's method
	<ul>
	<li>
		intuition says
Newton's method
works well for functions
whose quadratic approximations
do not change fast,
<i>i.e.</i>,
when $L$ is small

	</li>
	</ul>

</li>
</ul>


<h3>Convergence analysis of Newton's method</h3>

<div class="theorem" id="theorem:convergence---analysis---of---Newton's---method" data-name="convergence analysis of Newton's method">
	
for function $\fobj$ satisfying strong convexity, Hessian continuity &amp; Lipschitz continuity
with $m, M, L>0$,
exist $0<\eta<m^2/L$ and $\gamma > 0$
such that
for each step $k$

	<ul>
	<li>
		damped Newton phase
-
if $\|\nabla \fobj(\xseqk{k})\|_2 \geq \eta$,

$$
\fobj(\xseqk{k+1}) - \fobj(\xseqk{k}) \leq - \gamma
$$


	</li>
	<li>
		quadratic convergence phase
-
if $\|\nabla \fobj(\xseqk{k})\|_2 < \eta$,
backtracking line search selects step length $\slenk{k}=1$

$$
\frac{L}{2m^2} \|\nabla \fobj(\xseqk{k+1})\|_2
\leq
\left(
\frac{L}{2m^2} \|\nabla \fobj(\xseqk{k})\|_2
\right)^2
$$


	</li>
	</ul>
# iterations of Newton's method required to satisfy stopping criterion
$\fobj(\xseqk{k})-p^\ast\leq\epsilon$ is

$$
\frac{\fobj(\xseqk{0}) - p^\ast}{\gamma}
+ \log_2 \log_2 (\epsilon_0 / \epsilon)
\quad
\mbox{where }
\epsilon_0 = 2 m^3/L^2
$$


</div>

<h3>Summary of Newton's method</h3>

<ul>
<li>
	Newton's method is <i>affine invariant</i>,
hence <i>performance is independent of condition number unlike gradient method</i>

</li>
<li>
	once entering quadratic convergence phase,
Newton's method converges extremely fast

</li>
<li>
	performance not much dependent on choice of algorithm parameters

</li>
<li>
	big disadvantage is
computational cost for evaluating search direction,
<i>i.e.</i>, solving linear system

</li>
</ul>


<h3>Self-concordance</h3>

<div class="definition" id="definition:self-concordance" data-name="self-concordance">
	
convex function $f:X\to \reals$
with $X\subset \reals^n$
such that
for all $x\in X, v\in\reals^n$,
$g(t) = f(x+tv)$
with $\dom g = \set{t\in\reals}{x+tv\in X}$
satisfies

$$
\left(
\forall t\in\dom g
\right)
\left(
|g'''(t)| \leq 2 g''(t)^{3/2}
\right)
$$


</div>

<div class="proposition" id="proposition:self-concordance---for---logarithms" data-name="self-concordance for logarithms">
	
if convex function $g:X\to\reals$ with $X\subset \ppreals$
satisfies

$$
|g'''(x)| \leq 3 g''(x) / x
$$

function $f$ with $\dom f = \set{x\in\ppreals}{g(x)<0}$
defined by

$$
f(x) = -\log(-g(x)) - \log x
$$

and
function $h$ with $\dom h = \set{x\in\ppreals}{g(x)+ax^2+bx + c<0}$
with $a\geq0$
defined by

$$
h(x) = -\log(-g(x)-ax^2-bx-c) - \log x
$$

are self-concordant

</div>


<h3>Why self-concordance?</h3>

<ul>
<li>
	convergence analysis of Newton's method depends on
assumptions about function characteristics,
<i>e.g.</i>,
$m,M, L > 0$
for strong convexity, continuity of Hessian,
<i>i.e.</i>

$$
m I \preceq \nabla^2 f(x) \preceq M I
\quad
\|\nabla^2 f(x)- \nabla^2f(y)\| \leq L \|x-y\|
$$


</li>
<li>
	<span class="define">self-concordance</span>
discovered by Nesterov and Nemirovski
(who gave name self-concordance)
plays important role
for reasons
such as
	<ul>
	<li>
		convergence analysis does not depend any function characterizing paramters

	</li>
	<li>
		many barrier functions which are used for interior-point methods,
which are important class of optimization algorithms
are self-concordance

	</li>
	<li>
		property of self-concordance is affine invariant

	</li>
	</ul>

</li>
</ul>

<h3>Self-concordance preserving operations</h3>

<div class="proposition" id="proposition:self-concordance---preserving---operations" data-name="self-concordance preserving operations">
	
self-concordance is preserved by <i>positive scaling, addition, and affine transformation,</i>
<i>i.e.</i>,
if $f, g:X\to\reals$ are self-concordant functions with $X\subset\reals^n$,
$h:H\to\reals^n$ with $H\subset \reals^m$ are affine functions,
and $a>0$

$$
af,
\quad
f+g,
\quad
f\circ h
$$

are self-concordant
where
$\dom f\circ h = \set{x\in H}{h(x) \in X}$

</div>

<h3>Self-concordant function examples</h3>

<ul>
<li>
	negative logarithm
-
$f:\ppreals \to \reals$ with

$$
f(x)=-\log x
$$

is self-concordant since

$$
|f'''(x)| / f''(x)^{3/2} = \left(2/x^3\right) / \left((1/x^2)^{3/2}\right) = 2
$$


</li>
<li>
	negative entropy plus negative logarithm
-
$f:\ppreals \to \reals$ with 
$$
f(x)=x\log x-\log x
$$

is self-concordant since

$$
|f'''(x)| / f''(x)^{3/2} = (x+2)/{(x+1)^{3/2}}
\leq 2
$$


</li>
<li>
	log barrier for linear inequalities
-
for $A\in\reals^{m\times n}$ and $b\in\reals^m$

$$
f(x) = - \sum \log(b-Ax)
$$

with $\dom f = \set{x\in\reals^n}{b-Ax \succ 0}$
is self-concordant
by
<a href="#proposition:self-concordance---preserving---operations"></a>,
<i>i.e.</i>, $f$ is affine transformation of sum of self-concordant functions

</li>
<li>
	log-determinant
-
$f:\posdefset{n}\to\reals$
with

$$
f(X) = \log\det X^{-1} = - \log\det X
$$

is self-concordant since
for every $X\in \posdefset{n}$ and $V\in\symset{n}$
function $g:\reals\to\reals$ defined by $g(t) = - \log\det(X+tV)$
where $\dom f = \set{t\in\reals}{X+tV\succeq 0}$
is self-concordant
since

$$
\begin{eqnarray*}

g(t) &=& - \log \det (X^{1/2} (I + tX^{-1/2} V X^{-1/2})X^{1/2})

\\
&=&
-\log\det X - \log\det(I+tX^{-1/2}VX^{-1/2})
\\
&=&
-\log\det X - \sum \log (1+t\lambda_i(X,V))
\end{eqnarray*}
$$

where
$\lambda_i(X,V)$ is $i$-th eigenvalue of $X^{-1/2}VX^{1/2}$
is self-concordant
by
<a href="#proposition:self-concordance---preserving---operations"></a>,
<i>i.e.</i>, $g$ is affine transformation of sum of self-concordant functions

</li>
<li>
	log of concave quadratic
-
$f:X\to\reals$
with

$$
f(x) = -\log(-x^TPx - q^Tx - r)
$$

where
$P\in\possemidefset{n}$
and
$X=\set{x\in\reals^n}{x^TPx + q^Tx + r<0}$

</li>
<li>
	function $f:X\to\reals$
with

$$
f(x) = -\log(-g(x)) - \log x
$$

where $\dom f = \set{x\in\dom g \cap \ppreals}{g(x)<0}$
and
function $h:H\to\reals$

$$
h(x) = -\log(-g(x)-ax^2-bx-c) - \log x
$$

where $a\geq0$ and $\dom h = \set{x\in\dom g \cap \ppreals}{g(x)+ax^2+bx+c<0}$
are self-concordant
if $g$ is one of below
	<ul>
	<li>
		$g(x) = -x^p$ for $0<p\leq 1$

	</li>
	<li>
		$g(x) = -\log x$

	</li>
	<li>
		$g(x) = x \log x$

	</li>
	<li>
		$g(x) = x^p$ for $-1\leq p\leq 0$

	</li>
	<li>
		$g(x) = (ax+b)^2/x$ for $a,b\in\reals$

	</li>
	</ul>
since above $g$ satisfy
$|g'''(x)| \leq 3 g''(x)/x$
for every $x\in\dom g$
(<a href="#proposition:self-concordance---for---logarithms"></a>)

</li>
<li>
	function $f:X\to\reals$
with $X = \set{(x,y)}{\|x\|_2 < y}\subset \reals^n \times \ppreals$
defined by

$$
f(x,y) = -\log(y^2-x^Tx)
$$

is self-concordant - can be proved using <a href="#proposition:self-concordance---for---logarithms"></a>

</li>
<li>
	function $f:X\to\reals$
with $X = \set{(x,y)}{|x|^p < y}\subset \reals \times \ppreals$
defined by

$$
f(x,y) = -2\log y - \log(y^{2/p}- x^2)
$$

where $p\geq1$
is self-concordant - can be proved using <a href="#proposition:self-concordance---for---logarithms"></a>

</li>
<li>
	function $f:X\to\reals$
with $X = \set{(x,y)}{\exp(x) < y}\subset \reals \times \ppreals$
defined by

$$
f(x,y) = -\log y - \log(\log y - x)
$$

is self-concordant - can be proved using <a href="#proposition:self-concordance---for---logarithms"></a>

</li>
</ul>

<h3>Properties of self-concordant functions</h3>

<div class="definition" id="definition:Newton---decrement" data-name="Newton decrement">
	
for convex function $f:X\to\reals$ with $X\subset \reals^n$,
function $\lambda:\tilde{X}\to\preals$
with $\tilde{X} = \set{x\in X}{\nabla^2 \fobj(x) \succ 0}$
defined by

$$
\lambda(x) = (\nabla \fobj(x)^T \nabla^2 \fobj(x)^{-1} \nabla \fobj(x))^{1/2}
$$

called <span class="define">Newton decrement</span>

	<ul>
	<li>
		note

$$
\lambda(x)
=
\sup_{v\neq 0}
\left(v^T \nabla \fobj(x) / \left( v^T \nabla^2 \fobj(x) v \right)^{1/2} \right)
$$


	</li>
	</ul>

</div>


<div class="theorem" id="theorem:optimality---certificate---for---self-concordant---functions" data-name="optimality certificate for self-concordant functions">
	
for strictly convex self-concordant function $f:X\to\reals^n$ with $X\subset \reals^n$,
Hessian is positive definition everywhere (hence Newton decrement is defined everywhere)
and for every $x\in X$

$$
p^\ast \geq \fobj(x) - \lambda(x)^2
\quad
\Leftrightarrow
\quad
\fobj(x) - p^\ast \leq \lambda(x)^2
$$

if $\lambda(x) \leq 0.68$

</div>


<h3>Stopping criteria for self-concordant objective functions</h3>

<ul>
<li>
	recall $\lambda(x)^2$ provides <i>approximate</i> optimality certificate,
(page~<a href="#page:Newton---decrement---in---quadratic---approximation">here</a>)
<i>i.e.</i>,
assuming $\fobj$ is well approximated by quadratic function around $x$

$$
\fobj(x) - p^\ast \lessapprox \lambda(x)^2/2
$$


</li>
<li>
	however, strict convexity together with self-concordance
provides proven bound
(by <a href="#theorem:optimality---certificate---for---self-concordant---functions"></a>)

$$
\fobj(x) - p^\ast \leq \lambda(x)^2
$$

for $\lambda(x) \leq 0.68$

</li>
<li>
	hence can use following stopping criterion for guaranteed bound

$$
\lambda(x)^2 \leq \epsilon
\quad
\Rightarrow
\quad
\fobj(x) - p^\ast \leq \epsilon
$$

for $\epsilon \leq 0.68^2$

</li>
</ul>


<h3>Convergence analysis of Newton's method for self-concordant functions</h3>

<div class="theorem" id="theorem:convergence---analysis---of---Newton's---method---for---self-concordant---functions" data-name="convergence analysis of Newton's method for self-concordant functions">
	
for strictly convex self-concordant function $\fobj$,
exist $0<\eta\leq 1/4$ and $\gamma>0$ (which depend only on line search parameters)
such that

	<ul>
	<li>
		damped Newton phase
-
if $\lambda(\xseqk{k})>\eta$

$$
\fobj(\xseqk{k+1}) - \fobj(\xseqk{k}) \leq - \gamma
$$


	</li>
	<li>
		quadratic convergence phase
-
if $\lambda(\xseqk{k})\leq\eta$
backtracking line search selects step length $\slenk{k}=1$

$$
2\lambda(\xseqk{k+1})
\leq
\left(2\lambda(\xseqk{k})\right)^2
$$


	</li>
	</ul>
# iterations required to satisfy stopping criterion
$\fobj(\xseqk{k})-p^\ast\leq\epsilon$ is

$$
\left(\fobj(\xseqk{0}) - p^\ast\right)/{\gamma}
+ \log_2 \log_2 (1 / \epsilon)
$$

where $\gamma = \alpha \beta (1-2\alpha)^2 / (20-8\alpha)$

</div>


<h2 id="title-page:Equality---Constrained---Minimization">Equality Constrained Minimization</h2>


<h3>Equality constrained minimization</h3>

<ul>
<li>
	consider
equality constrained convex optimization problem,
<i>i.e.</i>, $m=0$ in <a href="#definition:convex---optimization"></a>

$$
\begin{array}{ll}
\mbox{minimize} &
\fobj(x)
\\
\mbox{subject to} &
Ax = b
\end{array}
$$

where
$A\in\reals^{p\times n}$
and
domain of optimization problem is $\optdomain\ = \xobj \subset \reals^n$

</li>
<li>
	assume
	<ul>
	<li>
		$\rank A = p<n$,
<i>i.e.</i>, rows of $A$ are linearly independent

	</li>
	<li>
		$\fobj$ is twice-differentiable (hence by definition $\xobj$ is open)

	</li>
	<li>
		optimal solution $x^\ast$ exists, <i>i.e.</i>, $p^\ast = \inf_{x\in\optfeasset} \fobj(x) = \fobj(x^\ast)$
and $Ax^\ast = b$

	</li>
	</ul>

</li>
</ul>


<h3>Solving KKT for equality constrained minimization</h3>

<ul>
<li>
	<a href="#theorem:KKT---and---convexity---sufficient---for---optimality---with---strong---duality"></a>
implies
$x^\ast\in\xobj$ is optimal solution if and only if
exists $\nu^\ast\in\reals^p$
satisfy KKT optimality conditions,
<div id="page:KKT---conditions---for---equality---constrained---minimization"></div>
<i>i.e.</i>,

$$
\begin{eqnarray*}
Ax^\ast = b
&&\mbox{\define{primal feasibility equations}}
\\
\nabla \fobj(x^\ast) + A^T\nu^\ast = 0
&&\mbox{\define{dual feasibility equations}}
\end{eqnarray*}
$$


</li>
<li>
	solving equality constrained problem
is equivalent to
solving KKT equations
	<ul>
	<li>
		handful types of problems can be solved analytically

	</li>
	</ul>

</li>
<li>
	using unconstrained minimization methods
	<ul>
	<li>
		can eliminate equality constraints and apply unconstrained minimization methods

	</li>
	<li>
		solving dual problem using unconstrained minimization methods
and retrieve primal solution (refer to page~<a href="#page:Solving---primal---problems---via---dual---problems">here</a>)

	</li>
	</ul>

</li>
<li>
	will discuss Newton's method directly handling equality constraints
	<ul>
	<li>
		preserving problem structure such as sparsity

	</li>
	</ul>

</li>
</ul>


<h3>Equality constrained convex quadratic minimization</h3>

<ul>
<li>
	equality constrained convex quadratic minimization problem

$$
\begin{array}{ll}
\mbox{minimize} &
\fobj(x) = (1/2)x^T P x + q^Tx
\\
\mbox{subject to} &
Ax = b
\end{array}
$$

where $P\in\possemidefset{n}$ and $A\in\reals^{p\times n}$

</li>
<li>
	important since basis for extension of Newton's method to equality constrained problems

</li>
<li>
	<span class="define">KKT system</span>

$$
Ax^\ast = b \; \& \; Px^\ast + q + A^T\nu^\ast = 0
\;
\Leftrightarrow
\;
\underbrace{
\mattwotwo{P}{A^T}{A}{0}
}_{\mbox{\define{KKT matrix}}}
\colvectwo{x^\ast}{\nu^\ast}
=
\colvectwo{-q}{b}
$$


</li>
<li>
	exist primal and dual optimum $(x^\ast,\nu^\ast)$ if and only if KKT system has solution;
otherwise, problem is unbounded below

</li>
</ul>


<h3>Eliminating equality constraints</h3>

<ul>
<li>
	can solve equality constrained convex optimization
by
	<ul>
	<li>
		eliminating equality constraints and

	</li>
	<li>
		using optimization method for solving unconstrained optimization

	</li>
	</ul>

</li>
<li>
	note

$$
\optfeasset
=
\set{x}{Ax=b}
=
\set{Fz + x_0}{z\in\reals^{n-p}}
$$

for some $F\in\reals^{n\times(n-p)}$
where $\range(F) = \nullspace(A)$

</li>
<li>
	thus original problem equivalent to

$$
\begin{array}{ll}
\mbox{minimize} &
\fobj(Fz + x_0)
\end{array}
$$


</li>
<li>
	if $z^\ast$ is optimal solution, $x^\ast = Fz^\ast + x_0$

</li>
<li>
	optimal dual can be retrieved by

$$
\nu^\ast = - (AA^T)^{-1} A\nabla \fobj(x^\ast)
$$


</li>
</ul>

<h3>Solving dual problems</h3>

<ul>
<li>
	Lagrange dual function of equality constrained problem

$$
\begin{eqnarray*}
g(\nu)
&
=
&
\inf_{x\in\optdomain}
\left(
\fobj(x) + \nu^T(Ax-b)
\right)
=
-b^T\nu - \sup_{x\in\optdomain} \left((-A^T\nu)^Tx -\fobj(x)\right)
\\
&
=
&
-b^T \nu - {\fobj}^\ast(-A^T\nu)
\end{eqnarray*}
$$


</li>
<li>
	dual problem

$$
\begin{array}{ll}
\mbox{maximize} &
-b^T \nu - {\fobj}^\ast(-A^T\nu)
\end{array}
$$


</li>
<li>
	by assumption, strong duality holds, hence
if $\nu^\ast$ is dual optimum

$$
g(\nu^\ast) = p^\ast
$$


</li>
<li>
	if dual objective is twice-differentiable,
can solve dual problem using unconstrained minimization methods

</li>
<li>
	primal optimum can be retrieved using method on page~<a href="#page:Solving---primal---problems---via---dual---problems">here</a>)

</li>
</ul>


<h3>Newton's method with equality constraints</h3>

<ul>
<li>
	finally discuss Newton's method which directly handles equality constraints
	<ul>
	<li>
		similar to Newton's method for unconstrained minimization

	</li>
	<li>
		initial point, however, should be feasible, <i>i.e.</i>, $\xseqk{0}\in\xobj$ and $A\xseqk{0} = b$

	</li>
	<li>
		Newton step tailored for equality constrained problem

	</li>
	</ul>

</li>
</ul>


<h3>Newton step via second-order approximation</h3>

<ul>
<li>
	solve original problem approximately by solving

$$
\begin{array}{ll}
\mbox{minimize} &
\hat{\fobj}(x+\sdir) = \fobj(x) + \nabla \fobj(x)^T \sdir + (1/2) \sdir^T \nabla^2 \fobj(x) \sdir
\\
\mbox{subject to} &
A(x+\sdir) = b
\end{array}
$$

where $x\in\optfeasset$

</li>
<li>
	<i>Newton step for equality constrained minimization problem</i>,
defined by
solution of
KKT system
for above convex quadratic minimization problem

$$
\mattwotwo{\nabla^2 \fobj(x)}{A^T}{A}{0}
\colvectwo{\sdir_\mathrm{nt}}{w}
=
\colvectwo{-\nabla \fobj(x)}{0}
$$

<i>only when KKT system is nonsingular</i>

</li>
</ul>


<h3>Newton step via solving linearized KKT optimality conditions</h3>

<ul>
<li>
	recall KKT optimality conditions for equality constrained convex optimization problem

$$
Ax^\ast = b
\quad
\&
\quad
\nabla \fobj(x^\ast) + A^T\nu^\ast = 0
$$


</li>
<li>
	linearize KKT conditions

$$
\begin{eqnarray*}
&&
A(x+\sdir) = b
\quad
\&
\quad
\nabla \fobj(x) + \nabla^2 \fobj(x) \sdir + A^Tw = 0
\\
&\Leftrightarrow&
A\sdir = 0
\quad
\&
\quad
\nabla^2 \fobj(x) \sdir + A^Tw
=
- \nabla \fobj(x)
\end{eqnarray*}
$$

where $x\in\optfeasset$

</li>
<li>
	Newton step defined by above equations
is equivalent
to
that obtained by second-order approximation

</li>
</ul>


<h3>Newton decrement for equality constrained minimization</h3>

<ul>
<li>
	<span class="define">Newton descrement for equality constrained problem</span>
is defined by

$$
\lambda(x)
=
\left(\sdir_\mathrm{nt} \nabla^2 \fobj(x) \sdir_\mathrm{nt}\right)^{1/2}
$$




</li>
<li>
	same expression as that for unconstrained minimization,
but is <i>different</i>
since Newton step $\sdir_\mathrm{nt}$ is different from that for unconstrained minimization,
<i>i.e.</i>, $\sdir_\mathrm{nt} \neq -\nabla^2 \fobj(x)^{-1} \nabla \fobj(x)$
(refer to <a href="#definition:Newton---decrement"></a>)

</li>
<li>
	however, as before,

$$
\fobj(x) - \inf_{\sdir\in\reals^n}\set{\hat{\fobj}(x+\sdir)}{A(x+\sdir)=b}
= \lambda(x)^2/2
$$

and

$$
\left.
\left(
\frac{d}{dt}\fobj(x+t\sdir_\mathrm{nt})
\right)
\right|_{t=0}
=
\nabla \fobj(x) ^T \sdir_\mathrm{nt}
=
- \lambda(x)^2
<0
$$


</li>
</ul>


<h3>Feasible Newton's method for equality constrained minimization</h3>

<div class="algorithm" id="algorithm:feasible---Newton's---method---for---equality---constrained---minimization" data-name="feasible Newton's method for equality constrained minimization">
	 
<ul>
<li>
	<strong>Require:</strong>	$\fobj$, initial point $x\in \dom \fobj$ with $Ax=b$, tolerance $\epsilon>0$ <strong></strong>
</li>

<li>
	<strong>loop</strong>
</li>
<li>
	<strong></strong>	computer Newton step and descrement $\ntsdir(x)$ \& $\lambda(x)$
 <strong></strong>
</li>

<li>
	<strong></strong>	stopping criterion - quit if $\lambda(x)^2/2 < \epsilon$ <strong></strong>
</li>

<li>
	<strong></strong>	do line search on \fobj\ to choose $t>0$ <strong></strong>
</li>

<li>
	<strong></strong>	update - $x := x + \slen \ntsdir$ <strong></strong>
</li>

<li>
	<strong>end loop</strong>
</li>
</ul>

</div>
<ul>
<li>
	<a href="#algorithm:feasible---Newton's---method---for---equality---constrained---minimization"></a>
	<ul>
	<li>
		assumes
KKT matrix is nonsingular for every step

	</li>
	<li>
		is <i>feasible descent method</i>
since all iterates are feasible with $\fobj(\xseqk{k+1}) <\fobj(\xseqk{k})$

	</li>
	</ul>

</li>
</ul>


<h3>Assumptions for convergence analysis of feasible Newton's method for equality constrained minimization</h3>

<div id="page:conv-analysis-assumptions-feasible-equality-Newton-method"></div>
<ul>
<li>
	feasibility of initial point - $\xseqk{0}\in\dom \fobj \;\&\; A\xseqk{0}=b$

</li>
<li>
	sublevel set $S = \set{x\in \dom \fobj}{\fobj(x) \leq \fobj(\xseqk{0}),\; Ax=b}$
is closed

</li>
<li>
	boundedness of Hessian on $S$

$$
\left(
\exists M > 0
\right)
\left(
\forall x\in S
\right)
\left(
\nabla^2 \fobj(x) \preceq M I
\right)
$$


</li>
<li>
	boundedness of KKT matrix on $S$
- corresponds to strong convexity assumption in unconstrained minimization

$$
\left(
\exists K >0
\right)
\left(
\forall x \in S
\right)
\left(
\left\|
\mattwotwo{\nabla^2 \fobj(x)}{A^T}{A}{0}^{-1}
\right\|_2
\leq K
\right)
$$


</li>
<li>
	Lipschitz continuity of Hessian on $S$

$$
\left(
\exists L > 0
\right)
\left(
\forall x,y\in S
\right)
\left(
\left\|\nabla^2 \fobj(x) - \nabla^2 \fobj(y)\right\|_2
\leq
L
\|x-y\|_2
\right)
$$


</li>
</ul>


<h3>Convergence analysis of feasible Newton's method for equality constrained minimization</h3>

<div id="page:Convergence---analysis---of---feasible---Newton's---method---for---equality---constrained---minimization"></div>
<ul>
<li>
	convergence analysis of Newton's method for equality constrained minimization
can be done by analyzing
unconstrained minimization after eliminating equality constraints

</li>
<li>
	thus, yield <i>exactly same</i> results as
for unconstrained minimization
(<a href="#theorem:convergence---analysis---of---Newton's---method"></a>)
(with different parameter values),
<i>i.e.</i>,
	<ul>
	<li>
		consists of damped Newton phase and quadratic convergence phase

	</li>
	<li>
		# iterations required to achieve $\fobj(\xseqk{k})-p^\ast \leq \epsilon$
is

$$
\left(\fobj(\xseqk{0})-p^\ast\right)/\gamma + \log_2 \log_2 (\epsilon_0/\epsilon)
$$


	</li>
	</ul>

</li>
<li>
	for # iterations required to achieve $\fobj(\xseqk{k})-p^\ast \leq \epsilon$
for self-concordant functions
is also same as
for unconstrained minimization
(<a href="#theorem:convergence---analysis---of---Newton's---method---for---self-concordant---functions"></a>)

$$
\left(\fobj(\xseqk{0}) - p^\ast\right)/{\gamma}
+ \log_2 \log_2 (1 / \epsilon)
$$

where $\gamma = \alpha \beta (1-2\alpha)^2 / (20-8\alpha)$

</li>
</ul>


<h3>Newton step at infeasible points</h3>

<ul>
<li>
	only assume that $x\in\dom \fobj$ (hence, can be infeasible)

</li>
<li>
	(as before) linearize KKT conditions

$$
\begin{eqnarray*}
&&
A(x+\ntsdir) = b
\quad
\&
\quad
\nabla \fobj(x) + \nabla^2 \fobj(x) \ntsdir + A^Tw = 0
\\
&\Leftrightarrow&
A\ntsdir = b - Ax
\quad
\&
\quad
\nabla^2 \fobj(x) \ntsdir + A^Tw
=
- \nabla \fobj(x)
\\
&\Leftrightarrow&
\mattwotwo{\nabla^2 \fobj(x)}{A^T}{A}{0}
\colvectwo{\ntsdir}{w}
=
-
\colvectwo{\nabla \fobj(x)}{Ax-b}
\end{eqnarray*}
$$


</li>
<li>
	same as feasible Newton step <i>except second component on RHS of KKT system</i>

</li>
</ul>


<h3>Interpretation as primal-dual Newton step</h3>

<ul>
<li>
	update both primal and dual variables $x$ and $\nu$

</li>
<li>
	define $r:\reals^n\to\reals^p\to\reals^n\times\reals^p$
by

$$
r(x,\nu) = (r_\mathrm{dual}(x,\nu),r_\mathrm{pri}(x,\nu))
$$

where

$$
\begin{eqnarray*}
\mbox{\define{dual residual}}
&
-
&
r_\mathrm{dual}(x,\nu)
= \nabla \fobj(x) + A^T\nu
\\
\mbox{\define{primal residual}}
&
-
&
r_\mathrm{pri}(x,\nu)
= Ax-b
\end{eqnarray*}
$$


</li>
</ul>


<h3>Equivalence of infeasible Newton step to primal-dual Newton step</h3>

<ul>
<li>
	linearize $r$ to obtain primal-dual Newton step, <i>i.e.</i>

$$
\begin{eqnarray*}
&&
r(x,\nu) + D_{x,\nu} r(x,\nu) \colvectwo{\pdsdir}{\pdsdirnu} = 0
\\
&\Leftrightarrow&
\mattwotwo{\nabla^2f(x)}{A^T}{A}{0}
\colvectwo{\pdsdir}{\pdsdirnu}
=
- \colvectwo{\nabla f(x) + A^T\nu}{Ax-b}
\end{eqnarray*}
$$


</li>
<li>
	letting $\nu^+= \nu + \pdsdirnu$ gives

$$
\mattwotwo{\nabla^2f(x)}{A^T}{A}{0}
\colvectwo{\pdsdir}{\nu^+}
=
- \colvectwo{\nabla f(x)}{Ax-b}
$$

	<ul>
	<li>
		equivalent to infeasible Newton step

	</li>
	<li>
		reveals that current value of dual variable not needed

	</li>
	</ul>

</li>
</ul>


<h3>Residual norm reduction property</h3>

<ul>
<li>
	infeasible Newton step is <i>not</i> descent direction (unlike feasible Newton step)
since

$$
\begin{eqnarray*}

\left. \left(
\frac{d}{dt}\fobj(x+t\pdsdir)
\right) \right|_{t=0}
&=&
\nabla \fobj(x) ^T \pdsdir

\\
&=&
- \pdsdir^T \left(\nabla^2 \fobj(x) \pdsdir + A^Tw \right)

\\
&=& 
- \pdsdir^T \nabla^2 \fobj(x) \pdsdir + (Ax-b)^Tw
\end{eqnarray*}
$$

which is not necessarily negative

</li>
<li>
	however, norm of residual decreases in infeasible Newton direction

$$
\begin{eqnarray*}
\left.
\left(
\frac{d}{dx}
\|r(y+t\pdsdiry)\|_2^2
\right)
\right|_{t=0}
&
=
&
- 2 r(y)^T r(y) = - 2 \|r(y)\|_2^2
\\
\Leftrightarrow
\quad
\left.
\left(
\frac{d}{dx}
\|r(y+t\pdsdiry)\|_2
\right)
\right|_{t=0}
&
=
&
\frac{-2\|r(y)\|_2^2}{2\|r(y)\|_2}
= - \|r(y)\|_2
\end{eqnarray*}
$$

where $y=(x,\nu)$ and $\pdsdiry = (\pdsdir, \pdsdirnu)$

</li>
<li>
	can use $r(\xseqk{k},\nuseqk{k})$ to measure optimization progress for infeasible Newton's method

</li>
</ul>


<h3>Full and damped step feasibility property</h3>

<ul>
<li>
	assume step length is $t$ at some iteration,
then

$$
r_\mathrm{pri}(x^+,\nu^+) = Ax^+-b
= A(x + t \pdsdir) - b
= (1-t) r_\mathrm{pri}(x,\nu)
$$


</li>
<li>
	hence
$l>k$

$$
\seqk{r}{l}
=
\left(
\prod_{i=k}^{l-1}
(1-\seqk{t}{i})
\right)
\seqk{r}{k}
$$

	<ul>
	<li>
		primal residual reduced by $1-\seqk{t}{k}$ at step $k$

	</li>
	<li>
		Newton step becomes feasible step once full step length ($t=1$) taken

	</li>
	</ul>

</li>
</ul>


<h3>Infeasible Newton's method for equality constrained minimization</h3>

<div class="algorithm" id="algorithm:infeasible---Newton's---method---for---equality---constrained---minimization" data-name="infeasible Newton's method for equality constrained minimization">
	 
<ul>
<li>
	<strong>Require:</strong>	$\fobj$, initial point $x\in \dom \fobj$ \& $\nu$, tolerance $\epsilon_\mathrm{pri}>0$ \& $\epsilon_\mathrm{dual}>0$ <strong></strong>
</li>

<li>
	<strong>repeat</strong>
</li>
<li>
	<strong></strong>	computer Newton step and descrement
$\pdsdir(x)$
\&
$\pdsdirnu(x)$,
\
 <strong></strong>
</li>

<li>
	<strong></strong>	do line search on $r(x,\nu)$ to choose $\slen>0$ <strong></strong>
</li>

<li>
	<strong></strong>	update
-
$x := x + \slen \pdsdir$
\&
$\nu := \nu + \slen \pdsdirnu$
 <strong></strong>
</li>

<li>
	<strong>until</strong>	$\|r_\mathrm{dual}(x,\nu)\| \leq \epsilon_\mathrm{dual}$ \& $\|Ax-b\| \leq \epsilon_\mathrm{pri}$ <strong></strong>
</li>

</ul>

</div>
<ul>
<li>
	note similarity and difference of
<a href="#algorithm:infeasible---Newton's---method---for---equality---constrained---minimization"></a>
&amp;
<a href="#algorithm:feasible---Newton's---method---for---equality---constrained---minimization"></a>
	<ul>
	<li>
		line search done not on $\fobj$, but on primal-dual residuals $r(x,\nu)$

	</li>
	<li>
		stopping criteria depends on $r(x,\nu)$, not on Newton decrementa $\lambda(x)^2$

	</li>
	<li>
		primal and dual feasibility checked separately
- here norm in $\|Ax-b\|$ can be any norm,
<i>e.g.</i>,
$\|\cdot\|_0$,
$\|\cdot\|_1$,
$\|\cdot\|_2$,
$\|\cdot\|_\infty$,
depending on specific application

	</li>
	</ul>

</li>
</ul>


<h3>Line search methods for infeasible Newton's method</h3>

<div id="page:Line---search---methods---for---infeasible---Newton's---method"></div>
<ul>
<li>
	line search methods for infeasible Newton's method,
<i>i.e.</i>,
<a href="#algorithm:exact---line---search"></a>
&amp;
<a href="#algorithm:backtracking---line---search"></a>
same with $\fobj$ replaced by $\|r(x,\nu)\|_2$,

</li>
<li>
	but they have special forms (of course)
- refer to below special case descriptions

</li>
</ul>
<div class="algorithm" id="algorithm:exact---line---search---for---infeasible---Newton's---method" data-name="exact line search for infeasible Newton's method">
	 

$$
\slen = \argmin_{s>0} \|r(x +s\pdsdir, \nu + s\pdsdirnu)\|_2
$$


</div>
<div class="algorithm" id="algorithm:backtracking---line---search---for---infeasible---Newton's---method" data-name="backtracking line search for infeasible Newton's method">
	 
<ul>
<li>
	<strong>Require:</strong>	\sdir, \sdirnu, $\alpha\in(0,0.5)$, $\beta\in(0,1)$ <strong></strong>
</li>

<li>
	<strong></strong>	$\slen:=1$ <strong></strong>
</li>

<li>
	<strong>while</strong>	$\|r(x +\slen\pdsdir, \nu + \slen\pdsdirnu)\|_2 > (1-\alpha \slen)\|r(x,\nu)\|_2$
 <strong>do</strong>
</li>

<li>
	<strong></strong>	$\slen := \beta \slen$ <strong></strong>
</li>

<li>
	<strong>end while</strong>
</li>
</ul>

</div>


<h3>Pros and cons of infeasible Newton's method</h3>

<ul>
<li>
	pros
	<ul>
	<li>
		do not need to find feasible point separately,
<i>e.g.</i>
		<ul>
		<li>
			&ldquo;''

		</li>
		</ul>
can be solved by converting to
		<ul>
		<li>
			&ldquo;''

		</li>
		</ul>
and solved by infeasible Newton's method

	</li>
	<li>
		if step length is one at any iteration,
following steps coincides with feasible Newton's method
- could switch to feasible Newton's method

	</li>
	</ul>

</li>
<li>
	cons
	<ul>
	<li>
		exists no clear way to detect feasibility - primal residual decreases slowly
(phase I method in interior point method resolves this problem)

	</li>
	<li>
		convergence of infeasible Newton's method can be very slow
(until feasibility is achieved0

	</li>
	</ul>

</li>
</ul>


<h3>Assumptions for convergence analysis of infeasible Newton's method for equality constrained minimization</h3>

<div id="page:conv-analysis-assumptions-infeasible-equality-Newton-method"></div>
<ul>
<li>
	sublevel set $S = \bigset{(x,\nu)\in \dom \fobj\times \reals^m}{
\|r(x,\nu)\|_2
\leq
\|r(\xseqk{0},\nuseqk{0})\|_2
}$
is closed,
which always holds because $\|r\|_2$ is closed

</li>
<li>
	boundedness of KKT matrix on $S$

$$
\left(
\exists K >0
\right)
\left(
\forall x \in S
\right)
\left(
\left\|
Dr(x,\nu)^{-1}
\right\|_2
=
\left\|
\mattwotwo{\nabla^2 \fobj(x)}{A^T}{A}{0}^{-1}
\right\|_2
\leq K
\right)
$$


</li>
<li>
	Lipschitz continuity of Hessian on $S$

$$
\left(
\exists L > 0
\right)
\left(
\forall (x,\nu), (y,\mu)\in S
\right)
\left(
\left\|Dr(x,\nu) - Dr(y,\mu)\right\|_2
\leq
L
\|(x,\nu) - (y,\mu)\|_2
\right)
$$


</li>
<li>
	above assumptions imply $\set{x\in\dom \fobj}{Ax=b}\neq\emptyset$
and exist optimal point $(x^\ast,\nu^\ast)$

</li>
</ul>


<h3>Convergence analysis of infeasible Newton's method for equality constrained minimization</h3>

<ul>
<li>
	very simliar to that for Newton's method for unconstrained minimization

</li>
<li>
	consist of two phases - like unconstrained minimization or infeasible Newton's method (refer to
<a href="#theorem:convergence---analysis---of---Newton's---method"></a>
or page~<a href="#page:Convergence---analysis---of---feasible---Newton's---method---for---equality---constrained---minimization">here</a>)
	<ul>
	<li>
		damped Newton phase
-
if $\|r(\xseqk{k},\nuseqk{k})\|_2> 1/(K^2L)$

$$
\|r(\xseqk{k+1},\nuseqk{k+1})\|_2
\leq
\|r(\xseqk{k},\nuseqk{k})\|_2
- \alpha \beta / K^2L
$$


	</li>
	<li>
		quadratic convergence
damped Newton phase
-
if $\|r(\xseqk{k},\nuseqk{k})\|_2 \leq 1/(K^2L)$

$$
\left( K^2L \|r(\xseqk{k},\nuseqk{k})\|_2 / 2 \right)
\leq
\left( K^2L \|r(\xseqk{k-1},\nuseqk{k-1})\|_2 / 2 \right)^2
\leq
\cdots
\leq (1/2)^{2^k}
$$


	</li>
	</ul>

</li>
<li>
	# iterations of infeasible Newton's method required to satisfy $\|r(\xseqk{k},\nuseqk{k})\|_2\leq\epsilon$

$$
\|r(\xseqk{0},\nuseqk{0})\| /(\alpha \beta / K^2L)
+ \log_2 \log_2 (\epsilon_0/\epsilon) \quad \mbox{where}\; \epsilon_0 = 2/(K^2L)
$$


</li>
<li>
	$(\xseqk{k},\nuseqk{k})$ converges to $(x^\ast,\nu^\ast)$

</li>
</ul>


<h2 id="title-page:Barrier---Interior-point---Methods">Barrier Interior-point Methods</h2>


<h3>Interior-point methods</h3>

<ul>
<li>
	want to solve inequality constrained minimization problem

</li>
<li>
	interior-point methods solve convex optimization problem (<a href="#definition:convex---optimization"></a>)
or KKT optimality conditions (<a href="#definition:KKT---optimality---conditions"></a>)
by
	<ul>
	<li>
		applying Newton's method to sequence of
		<ul>
		<li>
			equality constrained problems or

		</li>
		<li>
			modified versions of KKT optimality conditions

		</li>
		</ul>

	</li>
	</ul>

</li>
<li>
	discuss interior-point <span class="define">barrier method</span> &amp; interior-point <span class="define">primal-dual method</span>

</li>
<li>
	hierarchy of convex optimization algorithms
	<ul>
	<li>
		simplest - linear equality constrained quadratic program - can solve analytically

	</li>
	<li>
		Newton's method - solve linear equality constrained convex optimization problem
by solving sequence of linear equality constrained quadratic programs

	</li>
	<li>
		interior-point methods
- solve linear equality &amp; convex inequality constrained problem
by solving sequence of lienar equality constrained convex optimization problem

	</li>
	</ul>

</li>
</ul>


<h3>Indicator function barriers</h3>

<ul>
<li>
	approxmiate general convex inequality constrained problem as linear equality constrained problem

</li>
<li>
	make inequality constraints implicit in objective function

$$
\begin{array}{ll}
\mbox{minimize} &
\fobj(x) + \sum I_-(\fie(x))
\\
\mbox{subject to} &
Ax=b
\end{array}
$$

where $I_-:\reals\to \reals$ is indicator function for nonpositive real numbers, <i>i.e.</i>

$$
I_{-}(u) = \left\{\begin{array}{ll}
0	 & u\leq 0
\\
\infty	 & u> 0
\end{array}\right.
$$


</li>
</ul>


<h3>Logarithmic barriers</h3>

<ul>
<li>
	approximate indicator function by logarithmic function

$$
\hat{I}_- = -(1/t) \log(-u)
\quad
\dom \hat{I}_- = -\ppreals
$$

for $t>0$ to obtain

$$
\begin{array}{ll}
\mbox{minimize} &
\fobj(x) + \sum -(1/t) \log(-\fie(x))
\\
\mbox{subject to} &
Ax=b
\end{array}
$$


</li>
<li>
	objective function is convex due to composition rule for convexity preservation
(page~<a href="#page:convexity---preserving---operation-------composition">here</a>),
and differentiable

</li>
<li>
	hence, can use Newton's method to solve it

</li>
<li>
	function $\phi$ defined by

$$
\phi(x) = - \sum \log(-\fie(x))
$$

with $\dom \phi \set{x\in\xdomain}{\fie(x) \prec 0}$
called <span class="define">logarithmic barrier</span> or <span class="define">log barrier</span>

</li>
<li>
	solve sequence of log barrier problems as we increase $t$

</li>
</ul>


<h3>Central path</h3>

<div id="page:Central---path"></div>
<ul>
<li>
	optimization problem

$$
\begin{array}{ll}
\mbox{minimize} &
t \fobj(x) + \phi(x)
\\
\mbox{subject to} &
Ax = b
\end{array}
$$

with $t>0$
where

$$
\phi(x) = - \sum \log(-\fie(x))
$$


</li>
<li>
	solution of above problem, called <span class="define">central point</span>, denoted by <span class="notation">$x^\ast(t)$</span>,
set of central points, called <span class="define">central path</span>

</li>
<li>
	intuition says $x^\ast(t)$ will converge to $x^\ast$
as $t\to\infty$

</li>
<li>
	KKT conditions imply

$$
Ax^\ast(t) = b \quad \fie(x^\ast(t)) \prec 0
$$

and exists $\nu^\ast(t)$ such that

$$
\begin{eqnarray*}
0
&=&
t \nabla \fobj(x^\ast(t)) + \nabla \phi(x^\ast(t)) + t A^T \nu^\ast(t)
\\
&=&
t\nabla \fobj(x^\ast(t))
- \sum \frac{1}{\fie_i(x^\ast(t))} \nabla\fie_i(x^\ast(t))
+ t A^T \nu^\ast(t)
\end{eqnarray*}
$$


</li>
<li>
	thus if we let $\lambda^\ast(t) = -1/t\fie_i(x^\ast(t))$,
$x^\ast(t)$ minimizes

$$
L(x,\lambda^\ast(t),\nu^\ast(t))
= \fobj(x) + {\lambda^\ast(t)}^T \fie(x) + {\nu^\ast(t)}^T (Ax-b)
$$

where $L$ is Lagrangian of original problem in <a href="#definition:convex---optimization"></a>

</li>
<li>
	hence, dual function $g(\lambda^\ast(t),\nu^\ast(t))$ is finite
and

$$
\begin{eqnarray*}

g(\lambda^\ast(t), \nu^\ast(t))
&=&
\inf_{x\in\xdomain} L(x,\lambda^\ast(t),\nu^\ast(t))
&=&
L(x^\ast(t),\lambda^\ast(t),\nu^\ast(t))

\\
&
=
&
\fobj(x^\ast(t)) + {\lambda^\ast(t)}^T \fie(x^\ast(t)) + {\nu^\ast(t)}^T (Ax^\ast(t)-b)
= \fobj(x^\ast(t)) - m/t
\end{eqnarray*}
$$

and

$$
\fobj(x^\ast(t)) - p^\ast \leq \fobj(x^\ast(t)) - g(\lambda^\ast(t), \nu^\ast(t))
= m/t
$$


</li>
<li>
	
that is,


<span class="eemph">
$x^\ast(t)$ is no more than $m/t$-suboptimal
</span>



</li>
<li>
	
which
confirms out intuition that $x^\ast(t)\to x^\ast$ as $t\to\infty$

</li>
</ul>


<h3>Central path interpretation via KKT conditions</h3>

<ul>
<li>
	previous arguments imply that $x$ is central point,
<i>i.e.</i>, $x=x^\ast(t)$ for some $t>0$
if and only if
exist $\lambda$ and $\nu$ such that

$$
\begin{eqnarray*}
Ax=b
\quad
\fie({x})
&\preceq&
0
\quad
\mbox{- primal feasibility}
\\
\lambda
&\succeq&
0
\quad
\mbox{- dual feasibility}
\\
- {\lambda_i}^T \fie_i({x})
&=&
1/t
\quad
\mbox{- complementary $1/t$-slackness}
\\
\nabla_x L(x,\lambda,\nu)
&=&
0
\quad
\mbox{- vanishing gradient of Lagrangian}
\end{eqnarray*}
$$

called <span class="define">centrality conditions</span>

</li>
<li>
	only difference between centrality conditions and KKT conditions in <a href="#definition:KKT---optimality---conditions"></a>
is <i>complementary $1/t$-slackness</i>
	<ul>
	<li>
		note that I've just made up term &ldquo;complementary $1/t$-slackness''
- you won't be able to find terminology in any literature

	</li>
	</ul>

</li>
<li>
	for large $t$, $\lambda^\ast(t)$ &amp; $\nu^\ast(t)$ <i>very closely</i> satisfy (true) complementary slackness

</li>
</ul>


<h3>Central path interpretation via force field</h3>

<ul>
<li>
	assume exist no equality constraints

</li>
<li>
	interpret $\phi$ as potential energy by some force field, <i>e.g.</i>, electrical field
and $t\fobj$ as potential energy by some other force field, <i>e.g.</i>, gravity

</li>
<li>
	then
	<ul>
	<li>
		force by first force field (in $n$-dimensional space), which we call <i>barrier force</i>, is

$$
- \nabla \phi(x) = \sum \frac{1}{\fie_i(x)} \nabla \fie_i(x)
$$


	</li>
	<li>
		force by second force field, which we call <i>objective force</i>, is

$$
- \nabla (t\fobj(x)) = -t \nabla \fobj(x)
$$


	</li>
	</ul>

</li>
<li>
	$x^\ast(t)$ is point where two forces exactly balance each other
	<ul>
	<li>
		as $x$ approach boundary, barrier force pushes $x$ harder from barriers,

	</li>
	<li>
		as $t$ increases, objective force pushes $x$ harder to point where objective potential energy is minimized

	</li>
	</ul>

</li>
</ul>


<h3>Equality constrained problem using log barrier</h3>

<ul>
<li>
	central point $x^\ast(t)$ is $m/t$-suboptimal point
guaranteed by optimality certificate $g(\lambda^\ast(t),\nu^\ast(t))$

</li>
<li>
	hence solving below problem provides solution with $\epsilon$-suboptimality

$$
\begin{array}{ll}
\mbox{minimize} &
(m/\epsilon) \fobj(x) + \phi(x)
\\
\mbox{subject to} &
Ax=b
\end{array}
$$


</li>
<li>
	but works only for small problems
since for large $m/\epsilon$,
objective function ill behaves

</li>
</ul>


<h3>Barrier methods</h3>

<div class="algorithm" id="algorithm:barrier---method" data-name="barrier method">
	 
<ul>
<li>
	<strong>Require:</strong>	strictly feasible $x$, $t>0$, $\mu>1$, tolerance $\epsilon>0$ <strong></strong>
</li>

<li>
	<strong>repeat</strong>
</li>
<li>
	<strong></strong>	centering step -
find $x^\ast(t)$
by minimizing $t\fobj + \phi$ subject to $Ax=b$
starting at $x$
 <strong></strong>
</li>

<li>
	<strong></strong>	(optionally)
compute $\lambda^\ast(t)$ \& $\nu^\ast(t)$
 <strong></strong>
</li>

<li>
	<strong></strong>	stopping criterion - quit if $m/t<\epsilon$
 <strong></strong>
</li>

<li>
	<strong></strong>	increase $t$ - $t := \mu t$
 <strong></strong>
</li>

<li>
	<strong></strong>	update $x$ - $x := x^\ast(t)$
 <strong></strong>
</li>

\Until
</ul>

</div>
<ul>
<li>
	<span class="define">barrier method</span>, also called <span class="define">path-following method</span>,
solves sequence of equality constrained optimization problem with log barrier
	<ul>
	<li>
		when first proposed by Fiacco and McCormick in 1960s,
it was called <span class="define">sequential unconstrained minimization technique (SUMT)</span>

	</li>
	</ul>

</li>
<li>
	<span class="define">centering step</span> also called <span class="define">outer iteration</span>

</li>
<li>
	each iteration of algorithm used for equality constrained problem,
called <span class="define">inner iteration</span>

</li>
</ul>

<h3>Accuracy in centering in barrier method</h3>

<ul>
<li>
	accuracy of centering
	<ul>
	<li>
		only goal of centering is getting close to $x^\ast$,
hence exact calculation of $x^\ast(t)$ not critical
as long as approximates of $x^\ast(t)$ go to $x^\ast$

	</li>
	<li>
		while cannot calculate $g(\lambda,\nu)$ for this case,
below provides dual feasible point
when
Newton step $\ntsdir$ for optimization problem on page~<a href="#page:Central---path">here</a> is small,
<i>i.e.</i>, for nearly centered

$$
\tilde{\lambda}_i
= -\frac{1}{t\fie_i(x)}
\left(
1 - \frac{\nabla \fie_i(x)^T \ntsdir}{\fie_i(x)}
\right)
$$


	</li>
	</ul>

</li>
</ul>

<h3>Choices of parameters of barrier method</h3>

<ul>
<li>
	choice of $\mu$
	<ul>
	<li>
		$\mu$ determines aggressiveness of $t$-update
		<ul>
		<li>
			larger $\mu$, less outer iterations, but more inner iterations

		</li>
		<li>
			smaller $\mu$, less outer iterations, but more inner iterations

		</li>
		</ul>

	</li>
	<li>
		values from $10$ to $20$ for $\mu$
seem to work well

	</li>
	</ul>

</li>
<li>
	candidates for choice of initial $t$
- choose $\seqk{t}{0}$ such that
	<ul>
	<li>
		

$$
m / \seqk{t}{0} \approx \fobj(\xseqk{0}) - p^\ast
$$


	</li>
	<li>
		
make central path condition on page~<a href="#page:Central---path">here</a> maximally satisfied

$$
\seqk{t}{0}
= \arginf_{t}
\inf_{\tilde{\nu}}
\left\|
t \nabla \fobj(\xseqk{0}) + \nabla \phi(\xseqk{0}) + A^T \tilde{\nu}
\right\|
$$


	</li>
	</ul>

</li>
</ul>


<h3>Convergence analysis of barrier method</h3>

<ul>
<li>
	assuming $t\fobj + \phi$
can be minimized by Newton's method
for
$\seqk{t}{0}$,
$\mu\seqk{t}{0}$,
$\mu^2\seqk{t}{0}$,
&hellip;

</li>
<li>
	at $k$'th step, duality gap achieved is $m/\mu^k\seqk{t}{0}$

</li>
<li>
	# centering steps required to achieve accuracy of $\epsilon$ is

$$
\left\lceil
\frac{\log \left(m/\epsilon \seqk{t}{0}\right)}{\log \mu}
\right\rceil
$$

plus one (initial centering step)

</li>
<li>
	for convergence of centering
	<ul>
	<li>
		for feasible centering problem,
$t\fobj + \phi$ should satisfy conditions on page~<a href="#page:conv-analysis-assumptions-feasible-equality-Newton-method">here</a>,
<i>i.e.</i>,
initial sublevel set is closed,
associated inverse KKT matrix is bounded
&amp; Hessian satisfies Lipschitz condition

	</li>
	<li>
		for infeasible centering problem,
$t\fobj + \phi$ should satisfy conditions on page~<a href="#page:conv-analysis-assumptions-infeasible-equality-Newton-method">here</a>

	</li>
	</ul>

</li>
</ul>

<h2 id="title-page:Primal-dual---Interior-point---Methods">Primal-dual Interior-point Methods</h2>


<h3>Primal-dual \& barrier interior-point methods</h3>

<ul>
<li>
	in primal-dual interior-point methods
	<ul>
	<li>
		both primal and dual variables are updated at each iteration

	</li>
	<li>
		search directions are obtained from Newton's method,
applied to modified KKT equations,
<i>i.e.</i>,
optimality conditions for logarithmic barrier centering problem

	</li>
	<li>
		primal-dual search directions are similar to, but not quite the same as,
search directions arising in barrier methods

	</li>
	<li>
		primal and dual iterates are not necessarily feasible

	</li>
	</ul>

</li>
<li>
	primal-dual interior-point methods
	<ul>
	<li>
		often more efficient than barrier methods
especially when high accuracy is required
- can exhibit better than linear convergence

	</li>
	<li>
		(customized versions) outperform barrier method
for several basic problems, such as, LP, QP, SOCP, GP, SDP

	</li>
	<li>
		can work for feasible, but <i>not</i> strictly feasible problems

	</li>
	<li>
		still active research topic, but show great promise

	</li>
	</ul>

</li>
</ul>


<h3>Modified KKT conditions and central points</h3>

<ul>
<li>
	modified KKT conditions (for convex optimization in <a href="#definition:convex---optimization"></a>) expressed as

$$
r_t(x,\lambda,\nu)
=
\colvecthree
{\nabla \fobj(x) + D\fie(x)^T\lambda + A^T\nu}
{-\diag(\lambda)\fobj(x) - (1/t) \ones}
{Ax-b}
$$

where

$$
\begin{eqnarray*}
\mbox{dual residual}
&-&
r_\mathrm{dual}(x,\lambda,\nu)
= {\nabla \fobj(x) + D\fie(x)^T\lambda + A^T\nu}
\\
\mbox{centrality residual}
&-&
r_\mathrm{cent}(x,\lambda,\nu)
= {-\diag(\lambda)\fobj(x) - (1/t) \ones}
\\
\mbox{primal residual}
&-&
r_\mathrm{pri}(x,\lambda,\nu)
= {Ax-b}
\end{eqnarray*}
$$


</li>
<li>
	if $x$, $\lambda$, $\nu$ satisfy $r_t(x,\lambda,\nu)=0$ (and $\fie(x) \prec 0$),
then
	<ul>
	<li>
		$x=x^\ast(t)$, $\lambda=\lambda^\ast(t)$, $\nu=\nu^\ast(t)$

	</li>
	<li>
		$x$ is primal feasible and $\lambda$ &amp; $\nu$ are dual feasible
with duality gap $m/t$

	</li>
	</ul>

</li>
</ul>


<h3>Primal-dual search direction</h3>

<ul>
<li>
	assume current (primal-dual) point $y=(x,\lambda,\nu)$
and Newton step $\sdiry =( \sdir, \sdirnu, \sdirlbd)$

</li>
<li>
	as before, linearize equation to obtain Newton step,
<i>i.e.</i>,

$$
r_t(y+\sdiry) \approx r_t(y) + Dr_t(y) \sdiry = 0
\quad
\Leftrightarrow
\quad
\sdiry = -Dr_t(y)^{-1} r_t(y)
$$

hence

$$
\begin{my-matrix}{ccc}
\nabla^2 f(x) + \sum \lambda_i \nabla^2 \fie_i(x)
&
D\fie(x)^T
&
A^T
\\
-\diag(\lambda) D\fobj(x)
&
-\diag(\fobj(x))
&
0
\\
A
&
0
&
0
\end{my-matrix}
\colvecthree{\sdir}{\sdirlbd}{\sdirnu}
=
- \colvecthree
{r_\mathrm{dual}}
{r_\mathrm{cent}}
{r_\mathrm{pri}}
$$


</li>
<li>
	above equation determines
<span class="define">primal-dual search direction</span> $\pdsdiry = (\pdsdir, \pdsdirlbd, \pdsdirnu)$

</li>
</ul>


<h3>Surrogate duality gap</h3>

<ul>
<li>
	iterates $\xseqk{k}$, $\lbdseqk{k}$, and $\nuseqk{k}$ of primal-dual interior-point method
are <i>not</i> necessarily feasible

</li>
<li>
	hence, cannot easily evaluate duality gap $\seqk{\eta}{k}$
as for barrier method

</li>
<li>
	define <span class="define">surrogate duality gap</span>
for $\fie(x) \prec 0$ and $\lambda\succeq0$
as

$$
\hat{\eta}(x,\lambda) = - \fie(x)^T \lambda
$$


</li>
<li>
	$\hat{\eta}$ would be duality gap if $x$ were primal feasible and $\lambda$ &amp; $\nu$ were dual feasible

</li>
<li>
	value $t$ corresponding to surrogate duality gap $\hat{\eta}$ is $m/\hat{\eta}$

</li>
</ul>


<h3>Primal-dual interior-point method</h3>

<div class="algorithm" id="algorithm:primal-dual---interior-point---method" data-name="primal-dual interior-point method">
	 
<ul>
<li>
	<strong>Require:</strong>	initial point $x$ with $\fie(x)\prec0$, $\lambda \succ 0$, $\mu > 1$,
$\epsilon_\mathrm{pri}>0$, $\epsilon_\mathrm{dual}>0$, $\epsilon>0$ <strong></strong>
</li>

<li>
	<strong>repeat</strong>
</li>
<li>
	<strong></strong>	set $t := \mu m /\hat{\eta}$
 <strong></strong>
</li>

<li>
	<strong></strong>	computer primal-dual search direction $\pdsdiry = (\pdsdir, \pdsdirlbd, \pdsdirnu)$
 <strong></strong>
</li>

<li>
	<strong></strong>	do line search to choose $s>0$ <strong></strong>
</li>

<li>
	<strong></strong>	update
-
$x := x + s \pdsdir$,
$\lambda := \lambda + s \pdsdirnu$,
$\nu := \nu + s \pdsdirnu$
 <strong></strong>
</li>

<li>
	<strong>until</strong>	$\|r_\mathrm{pri}(x,\lambda,\nu)\|_2\leq \epsilon_\mathrm{pri}$,
$\|r_\mathrm{dual}(x,\lambda,\nu)\|_2\leq \epsilon_\mathrm{dual}$,
$\hat{\eta} \leq \epsilon$
 <strong></strong>
</li>

</ul>

</div>
<ul>
<li>
	common to choose small
$\epsilon_\mathrm{pri}$, $\epsilon_\mathrm{dual}$, &amp; $\epsilon$
since primal-dual method often shows faster than linear convergence

</li>
</ul>


<h3>Line search for primal-dual interior-point method</h3>

<ul>
<li>
	liner search is standard backtracking line search on $r(x,\lambda,\nu)$
similar to that in <a href="#algorithm:exact---line---search---for---infeasible---Newton's---method"></a>
except making sure that $\fie(x) \prec 0$ and $\lambda\succ0$

</li>
<li>
	note initial $s$
in <a href="#algorithm:backtracking---line---search---for---primal-dual---interior-point---method"></a>
is largest $s$ that makes $\lambda + s\pdsdirlbd$ positive

</li>
</ul>
<div class="algorithm" id="algorithm:backtracking---line---search---for---primal-dual---interior-point---method" data-name="backtracking line search for primal-dual interior-point method">
	 
<ul>
<li>
	<strong>Require:</strong>	\pdsdir, \pdsdirlbd, \pdsdirnu, $\alpha\in(0.01,0.1)$, $\beta\in(0.3,0.8)$ <strong></strong>
</li>

<li>
	<strong></strong>	$s:= 0.99\sup\set{s\in[0,1]}{\lambda + s \sdirlbd \succeq 0} = 0.99\min\{1,\min\set{-\lambda_i/\sdirlbd_i}{\sdirlbd_i < 0}\}$ <strong></strong>
</li>

<li>
	<strong>while</strong>	$\fie (x +s\pdsdir) \not \prec 0$
 <strong>do</strong>
</li>

<li>
	<strong></strong>	$t := \beta t$ <strong></strong>
</li>

<li>
	<strong>end while</strong>
</li>
<li>
	<strong>while</strong>	$\|r(x +s\pdsdir, \lambda + s\pdsdirlbd, \nu + s\pdsdirnu)\|_2 > (1-\alpha s)\|r(x,\lambda,\nu)\|_2$
 <strong>do</strong>
</li>

<li>
	<strong></strong>	$t := \beta t$ <strong></strong>
</li>

<li>
	<strong>end while</strong>
</li>
</ul>

</div>


