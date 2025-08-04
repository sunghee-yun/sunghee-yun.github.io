---
title: Convex Optimization
date: Fri Aug  1 07:00:00 PDT 2025
last_modified_at: Mon Aug  4 04:56:11 PDT 2025
permalink: /math/rig/convex-optimization
categories:
- blog
tags:
- math
- optimization
- convex optimization
- dual problem
- duality
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
		
$
\naturals
$
 - set of natural numbers



	</li>
	<li>
		
$
\integers
$
 - set of integers



	</li>
	<li>
		
$
\integers_+
$
 - set of nonnegative integers

	</li>
	<li>
		
$
\rationals
$
 - set of rational numbers



	</li>
	<li>
		
$
\reals
$
 - set of real numbers



	</li>
	<li>
		
$
\preals
$
 - set of nonnegative real numbers

	</li>
	<li>
		
$
\ppreals
$
 - set of positive real numbers

	</li>
	<li>
		
$
\complexes
$
 - set of complex numbers



	</li>
	</ul>

</li>
<li>
	sequences 
$
\seq{x_i}
$
 and the like

	<ul>
	<li>
		finite 
$
\seq{x_i}_{i=1}^n
$
, infinite 
$
\seq{x_i}_{i=1}^\infty
$
 - use 
$
\seq{x_i}
$
 whenever unambiguously understood





	</li>
	<li>
		similarly for other operations, <i>e.g.</i>, 
$
\sum x_i
$
, 
$
\prod x_i
$
, 
$
\cup A_i
$
, 
$
\cap A_i
$
, 
$
\bigtimes A_i
$


	</li>
	<li>
		similarly for integrals, <i>e.g.</i>, 
$
\int f
$
 for 
$
\int_{-\infty}^\infty f
$


	</li>
	</ul>

</li>
<li>
	sets
	<ul>
	<li>
		
$
\compl{A}
$
 - complement of 
$
A
$




	</li>
	<li>
		
$
A\sim B
$
 - 
$
A\cap \compl{B}
$




	</li>
	<li>
		
$
A\Delta B
$
 - 
$
(A\cap \compl{B}) \cup (\compl{A} \cap B)
$


	</li>
	<li>
		
$
\powerset(A)
$
 - set of all subsets of 
$
A
$


	</li>
	</ul>

</li>
<li>
	sets in metric vector spaces
	<ul>
	<li>
		$\closure{A}$ - closure of set 
$
A
$




	</li>
	<li>
		$\interior{A}$ - interior of set 
$
A
$




	</li>
	<li>
		
$
\relint A
$
 - relative interior of set 
$
A
$




	</li>
	<li>
		
$
\boundary A
$
 - boundary of set 
$
A
$




	</li>
	</ul>

</li>
<li>
	set algebra
	<ul>
	<li>
		
$
\sigma(\subsetset{A})
$
 - 
$
\sigma
$
-algebra generated by $\subsetset{A}$,
<i>i.e.</i>, smallest 
$
\sigma
$
-algebra containing $\subsetset{A}$


	</li>
	</ul>

</li>
<li>
	norms in 
$
\reals^n
$



	<ul>
	<li>
		
$
\|x\|_p
$
 (
$
p\geq1
$
) - 
$
p
$
-norm of 
$
x\in\reals^n
$
, <i>i.e.</i>, 
$
(|x_1|^p + \cdots + |x_n|^p)^{1/p}
$


	</li>
	<li>
		<i>e.g.</i>, 
$
\|x\|_2
$
 - Euclidean norm

	</li>
	</ul>

</li>
<li>
	matrices and vectors
	<ul>
	<li>
		
$
a_{i}
$
 - 
$
i
$
-th entry of vector 
$
a
$


	</li>
	<li>
		
$
A_{ij}
$
 - entry of matrix 
$
A
$
 at position 
$
(i,j)
$
,
<i>i.e.</i>, entry in 
$
i
$
-th row and 
$
j
$
-th column

	</li>
	<li>
		
$
\Tr(A)
$
 - trace of 
$
A \in\reals^{n\times n}
$
,
<i>i.e.</i>, 
$
A_{1,1}+ \cdots + A_{n,n}
$




	</li>
	</ul>

</li>
<li>
	symmetric, positive definite, and positive semi-definite matrices
	<ul>
	<li>
		
$
\symset{n}\subset \reals^{n\times n}
$
 - set of symmetric matrices



	</li>
	<li>
		
$
\possemidefset{n}\subset \symset{n}
$
 - set of positive semi-definite matrices;

$
A\succeq0 \Leftrightarrow A \in \possemidefset{n}
$




	</li>
	<li>
		
$
\posdefset{n}\subset \symset{n}
$
 - set of positive definite matrices;

$
A\succ0 \Leftrightarrow A \in \posdefset{n}
$




	</li>
	</ul>

</li>
<li>
	sometimes,
use Python script-like notations
(with serious abuse of mathematical notations)
	<ul>
	<li>
		use 
$
f:\reals\to\reals
$
 as if it were 
$
f:\reals^n \to \reals^n
$
,
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
		use 
$
\sum x
$
 to mean 
$
\ones^T x
$
 for 
$
x\in\reals^n
$
,
<i>i.e.</i>

$$

\sum x = x_1 + \cdots + x_n

$$

which corresponds to Python code <code>x.sum()</code>
where <code>x</code> is <code>numpy</code> array

	</li>
	<li>
		use 
$
x/y
$
 for 
$
x,y\in\reals^n
$
 to mean

$$

\rowvecthree{x_1/y_1}{\cdots}{x_n/y_n}^T

$$

which corresponds to Python code <code>x / y</code>
where <code>x</code> and <code>y</code> are 
$
1
$
-d <code>numpy</code> arrays

	</li>
	<li>
		use 
$
X/Y
$
 for 
$
X,Y\in\reals^{m\times n}
$
 to mean

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
where <code>X</code> and <code>Y</code> are 
$
2
$
-d <code>numpy</code> arrays

	</li>
	</ul>

</li>
</ul>


<h3>Some definitions</h3>

<div id="page:Some---definitions"></div>
<div class="definition" id="definition:infinitely---often-------i.o." data-name="infinitely often - i.o.">
	


statement 
$
P_n
$
, said to happen <span class="define">infinitely often</span> or <span class="define">i.o.</span> if

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
	




statement 
$
P(x)
$
,
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
		
$
0\cdot \infty = \infty \cdot 0 = 0
$


	</li>
	<li>
		
$
(\forall x\in\ppreals)(x\cdot \infty = \infty \cdot x = \infty)
$


	</li>
	<li>
		
$
\infty \cdot \infty = \infty
$


	</li>
	</ul>

</li>
</ul>


<h1 id="super-title-page:Convex---Optimization">Convex Optimization</h1>






























<h2 id="title-page:Convex---Sets">Convex Sets</h2>


<h3>Lines and line segmenets</h3>

<div class="definition" id="definition:lines" data-name="lines">
	
for some 
$
x,y\in\reals^n
$


$$

\set{\theta x + (1-\theta) y}{\theta\in\reals}

$$

called <span class="define">line going through $x$ and $y$</span>

</div>
<div class="definition" id="definition:line---segmenets" data-name="line segmenets">
	
for some 
$
x,y\in\reals^n
$


$$

\set{\theta x + (1-\theta) y}{0\leq\theta\leq1\in\reals}

$$

called <span class="define">line segment connecting $x$ and $y$</span>

</div>

<h3>Affine sets</h3>

<div class="definition" id="definition:affine---sets" data-name="affine sets">
	
set, 
$
C\subset \reals^n
$
,
every line going through any two points in which
is contained in 
$
C
$
, <i>i.e.</i>

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
	
for set, 
$
C\subset\reals^n
$
,
intersection of all affine sets containing 
$
C
$
,
called <span class="define">affine hull of $C$</span>,
denoted by <span class="notation">$\affinehull C$</span>,
which is equal to
set of all affine combinations of points in 
$
C
$
, <i>i.e.</i>

$$

\bigcup_{n\in\naturals}
\set{\theta_1 x_1 + \cdots + \theta_n x_n}{x_1,\ldots,x_n\in C, \theta_1 + \cdots + \theta_n=1}

$$


</div>
<div class="definition" id="definition:affine---dimension" data-name="affine dimension">
	
for 
$
C\subset \reals^n
$
,
dimension of 
$
\affinehull C
$
,
called <span class="define">affine dimension</span>

</div>

<h3>Relative interiors and boundaries</h3>

<div class="definition" id="definition:relative---interiors---of---sets" data-name="relative interiors of sets">
	
for 
$
C\subset \reals^n
$
,

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
	
for 
$
C\subset \reals^n
$
,

$
\closure{C}\sim \relint C
$
,
called <span class="define">relative boundary of $C$</span>

</div>

<h3>Convex sets</h3>

<div class="definition" id="definition:convex---sets" data-name="convex sets">
	
set, 
$
C\subset \reals^n
$
,
every line segment connecting any two points in which
is contained in 
$
C
$
, <i>i.e.</i>

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
	
for set, 
$
C\subset \reals^n
$
,
intersection of all convex sets containing 
$
C
$
,
called <span class="define">convex hull of $C$</span>,
denoted by <span class="notation">$\cvxhull C$</span>,
which is equal to
set of all convex combinations of points in 
$
C
$
, <i>i.e.</i>

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
	
set, 
$
C\subset \reals^n
$
,
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
	
set, 
$
C\subset \reals^n
$
,
which is both convex and cone,
called <i>convex cone</i>;

$
C
$
 is convex cone if and only if

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
	

$
n-1
$
 dimensional affine set in 
$
\reals^n
$
,
called <span class="define">hyperplane</span>;
every hyperplane
can be expressed as

$$

\set{x\in\reals^n}{a^T = b}

$$

for some 
$
a\neq0 \in \reals^n
$
 and 
$
b\in \reals
$


</div>
<div class="definition" id="definition:half---spaces" data-name="half spaces">
	
one of two sets divided by hyperplane,
called <span class="define">half space</span>;
every half space
can be expressed as

$$

\set{x\in\reals^n}{a^T \leq b}

$$

for some 
$
a\neq0 \in \reals^n
$
 and 
$
b\in \reals
$


</div>
<ul>
<li>
	hyperplanes and half spaces are convex sets

</li>
</ul>

<h3>Euclidean balls and ellipsoids</h3>

<div class="definition" id="definition:Euclidean---ball" data-name="Euclidean ball">
	
set of all points distance of which from point, 
$
x\in\reals^n
$
,
is no greater than 
$
r>0
$
,
called <span class="define">(Euclidean) ball centered at $x$ with radius, $r$</span>,
denoted by <span class="notation">$\ball{x}{r}$</span>,
<i>i.e.</i>

$$

\ball{x}{r} = \set{y\in\reals^n}{\|y-x\|_2\leq r}

$$


</div>
<div class="definition" id="definition:ellipsoids" data-name="ellipsoids">
	
ball elongated along 
$
n
$
 orthogonal axes,
called <span class="define">ellipsoid</span>,
<i>i.e.</i>,

$$

\set{y\in\reals^n}{(y-x)^TP^{-1}(y-x)\leq 1}

$$

for some 
$
x\in\reals^n
$
 and 
$
P\in \posdefset{n}
$


</div>
<ul>
<li>
	Euclidean balls and ellipsoids are convex sets

</li>
</ul>

<h3>Norm balls and norm cones</h3>

<div class="definition" id="definition:norm---ball" data-name="norm ball">
	
for norm, 
$
\|\cdot\|:\reals^n\to\preals
$
,
set of all points distance of which measured in the norm from point, 
$
x\in\reals^n
$
,
is no greater than 
$
r>0
$
,
called <span class="define">norm ball centered at $x$ with radius, $r$, associated with norm, $\|\cdot\|$</span>,
<i>i.e.</i>

$$

\set{y\in\reals^n}{\|y-x\|\leq r}

$$


</div>
<div class="definition" id="definition:norm---cone" data-name="norm cone">
	
for norm, 
$
\|\cdot\|:\reals^n\to\preals
$
,

$
x\in\reals^n
$
,
and

$
r>0
$
,

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

for 
$
A\in\reals^{m\times n}
$
, 
$
b\in\reals^m
$
, 
$
C\in\reals^{p\times n}
$
, 
$
d\in\reals^p
$


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
			for convex set 
$
C
$


$$
\alpha C
$$
 is convex set for any 
$
\alpha\in\reals
$


		</li>
		</ul>

	</li>
	<li>
		sum preserves convexity
		<ul>
		<li>
			for convex sets 
$
C
$
 and 
$
D
$


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
			for convex sets 
$
C
$
 and 
$
D
$


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
			for convex set 
$
C\subset A \times B
$


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
			for affine function 
$
f:A\to B
$
 and convex sets 
$
C\subset A
$
 and 
$
D\subset B
$


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
			for convex sets 
$
C\subset \reals^n, D\subset \reals^m
$

and
linear-fractional function, 
$
g:\reals^n\to\reals^m
$
,
<i>i.e.</i>, function defined by 
$
g(x) = (Ax+b)/(c^Tx+d)
$

for 
$
A\in\reals^{m\times n}
$
, 
$
b\in\reals^m
$
, 
$
c\in\reals^n
$
, and 
$
d\in\reals
$


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
	
closed convex cone 
$
K
$
 which is

	<ul>
	<li>
		solid, <i>i.e.</i>, 
$
\interior{K}\neq \emptyset
$


	</li>
	<li>
		pointed, <i>i.e.</i>, 
$
x\in vK
$
 and 
$
-x\in K
$
 imply 
$
x=0
$


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
	
proper cone 
$
K
$

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
	
$
\preceq_K
$
 and 
$
\prec_K
$
 are partial orderings

</li>
</ul>

<h3>Convex sets induced by generalized inequalities</h3>

<ul>
<li>
	for affine function 
$
g:\reals^n\to\symset{m}
$
,
<i>i.e.</i>, 
$
f(x)=A_0 + A_1 x_1 + \cdots + A_n x_n
$

for some 
$
A_0,\ldots,A_n\in\symset{m}
$
,

$
f^{-1}(\possemidefset{n})
$
 is convex (by <a href="#proposition:convexity---preserving---set---operations"></a>),
<i>i.e.</i>,

$$

\set{x\in\reals^n}{A_0 + A_1 x_1 + \cdots + A_n x_n \succeq 0} \subset \reals^n

$$

is convex

</li>
<li>
	can negate each matrix 
$
A_i
$
 and have same results,
hence

$$

\set{x\in\reals^n}{A_0 + A_1 x_1 + \cdots + A_n x_n \preceq 0} \subset \reals^n

$$

is (also) convex

</li>
</ul>


<h3>Separating and supporting hyperplanes</h3>

<div class="theorem" id="theorem:separating---hyperplane---theorem" data-name="separating hyperplane theorem">
	
for nonempty disjoint convex sets 
$
C
$
 and 
$
D
$
,
exists hyperplane which separates 
$
C
$
 and 
$
D
$
,
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
	
for nonempty disjoint convex sets 
$
C
$
 and 
$
D
$
,
hyperplane satisfying property in <a href="#theorem:separating---hyperplane---theorem"></a>,
called <span class="define">separating hyperplane</span>,
said to <span class="define">separate $C$ and $D$</span>

</div>
<div class="theorem" id="theorem:supporting---hyperplane---theorem" data-name="supporting hyperplane theorem">
	
for nonempty convex set 
$
C
$

and 
$
x\in \boundary C
$
,
exists hyperplane passing through 
$
x
$
,
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
	
for nonempty convex set 
$
C
$

and 
$
x\in \boundary C
$
,
hyperplane satisfied property in <a href="#theorem:supporting---hyperplane---theorem"></a>,
called <span class="define">supporting hyperplane</span>

</div>

<h3>Dual cones</h3>



<div class="definition" id="definition:dual---cones" data-name="dual cones">
	
for cone 
$
K
$
,

$$

\set{x}{\forall y \in K, y^Tx\geq 0 }

$$

called <span class="define">dual cone of $K$</span>,
denoted by <span class="notation">$K^\ast$</span>

</div>
<ul>
<li>
	the figure illustrates 
$
x \in K^\ast
$
 while 
$
z\not\in K^\ast
$


</li>
</ul>



&nbsp;


<div id="fig:dual---cone"></div>



<h3>Dual norms</h3>

<div class="definition" id="definition:dual---norms" data-name="dual norms">
	
for norm 
$
\|\cdot\|
$
,
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
		dual cone of subspace 
$
V\subset \reals^n
$

is orthogonal complement of 
$
V
$
, 
$
V^\perp
$
,
where

$
V^\perp=\set{y}{\forall v\in V,v^Ty = 0}
$


	</li>
	<li>
		$\prealk{n}$ and $\possemidefset{n}$ are self-dual

	</li>
	<li>
		<i>dual of norm cone</i> is <i>norm cone associated with dual norm</i>,
<i>i.e.</i>,
if 
$
K=\set{(x,t)\in\reals^{n} \times \reals}{\|x\|\leq t}
$


$$

K=\set{(y,u)\in\reals^{n} \times \reals}{\|y\|_\ast\leq u}

$$


	</li>
	</ul>

</li>
</ul>

<h3>Properties of dual cones</h3>

<div class="proposition" id="proposition:properties---of---dual---cones" data-name="properties of dual cones">
	
for cones 
$
K
$
, 
$
K_1
$
, and 
$
K_2
$


	<ul>
	<li>
		
$
K^\ast
$
 is closed and convex

	</li>
	<li>
		
$
K_1\subset K_2 \Rightarrow K_2^\ast \subset K_1^\ast
$


	</li>
	<li>
		if 
$
\interior{K} \neq \emptyset
$
, 
$
K^\ast
$
 is pointed

	</li>
	<li>
		if $\closure{K}$ is pointed, 
$
\interior{(K^\ast)} \neq \emptyset
$


	</li>
	<li>
		
$
K^{\ast\ast}=(K^\ast)^\ast
$
 is closure of convex hull of 
$
K
$
,

	</li>
	<li>
		
$
K^\ast
$
 is closed and convex

	</li>
	</ul>

thus,

	<ul>
	<li>
		if 
$
K
$
 is closed and convex, 
$
K^{\ast\ast} = K
$


	</li>
	<li>
		dual of proper cone is proper cone

	</li>
	<li>
		for proper cone 
$
K
$
, 
$
K^{\ast\ast}=K
$


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
for proper cone 
$
K
$
,

	<ul>
	<li>
		
$
x\preceq_K y
$
 if and only if 
$
(\forall \lambda \succeq_{K^\ast} 0)(\lambda^T x \leq \lambda^T y)
$


	</li>
	<li>
		
$
x\prec_K y
$
 if and only if 
$
(\forall \lambda \succeq_{K^\ast} 0 \mbox{ with } \lambda\neq0)(\lambda^T x < \lambda^T y)
$


	</li>
	</ul>

$
K^{\ast\ast} = K
$
,
hence
above are equivalent to

	<ul>
	<li>
		
$
x\preceq_{K^\ast} y
$
 if and only if 
$
(\forall \lambda \succeq_{K} 0)(\lambda^T x \leq \lambda^T y)
$


	</li>
	<li>
		
$
x\prec_{K^\ast} y
$
 if and only if 
$
(\forall \lambda \succeq_{K} 0 \mbox{ with } \lambda\neq0)(\lambda^T x < \lambda^T y)
$


	</li>
	</ul>

</div>

<h3>Theorem of alternative for linear strict generalized inequalities</h3>

<div class="theorem" id="theorem:theorem---of---alternative---for---linear---strict---generalized---inequalities" data-name="theorem of alternative for linear strict generalized inequalities">
	
for
proper cone 
$
K\subset \reals^m
$
,

$
A\in\reals^{m\times n}
$
,
and

$
b\in\reals^m
$
,

$$

Ax \prec_K b

$$

is infeasible if and only if
exist nonzero 
$
\lambda\in\reals^m
$

such that

$$

\lambda \neq0,\
\lambda \succeq_{K^\ast} 0,\
A^T \lambda = 0,\
\lambda^T b \leq0

$$

Above two inequality systems are <i>alternative</i>,
<i>i.e.</i>, for any data, 
$
A
$
 and 
$
b
$
,
exactly one of them is feasible.


</div>

<h2 id="title-page:Convex---Functions">Convex Functions</h2>


<h3>Convex functions</h3>

<div class="definition" id="definition:convex---functions" data-name="convex functions">
	


	<ul>
	<li>
		function 
$
f:\reals^n\to\reals
$

the domain of which is convex
and which satisfies
$$
\begin{eqnarray*}

&&
\left(
\forall x,y\in \dom f, 0\leq \theta \leq 1
\right)

\\
&&
\left(
f(\theta x + (1-\theta) y)
\leq
\theta f(x) + (1-\theta) f(y)
\right)

\end{eqnarray*}
$$
said to be <span class="define">convex</span>

	</li>
	<li>
		function 
$
f:\reals^n\to\reals
$

the domain of which is convex
and which satisfies
$$
\begin{eqnarray*}

&&
\left(
\forall \mbox{ distinct } x,y\in \dom f, 0< \theta < 1
\right)

\\
&&
\left(
f(\theta x + (1-\theta) y)
<
\theta f(x) + (1-\theta) f(y)
\right)

\end{eqnarray*}
$$
said to be <span class="define">strictly convex</span>

	</li>
	</ul>

</div>
<div class="definition" id="definition:concave---functions" data-name="concave functions">
	


	<ul>
	<li>
		function 
$
f:\reals^n\to\reals
$

the domain of which is convex
where 
$
-f
$
 is convex,
said to be <span class="define">concave</span>

	</li>
	<li>
		function 
$
f:\reals^n\to\reals
$

the domain of which is convex
where 
$
-f
$
 is strictly convex,
said to be <span class="define">strictly concave</span>

	</li>
	</ul>

</div>

<h3>Extended real-value extensions of convex functions</h3>

<div class="definition" id="definition:extended---real-value---extension---of---convex---functions" data-name="extended real-value extension of convex functions">
	
for convex function 
$
f
$
,
function

$
\tilde{f}: \reals^n \to \reals\cup\{\infty\}
$

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
can drop &ldquo;
$
\dom f
$
'' in equations,
<i>e.g.</i>,
	<ul>
	<li>
		
$
f
$
 is convex if and only if its extended-value extension 
$
\tilde{f}
$
 satisfies
$$
\begin{eqnarray*}

&&
\left(
\forall x,y\in \dom f, 0\leq \theta \leq 1
\right)

\\
&&
\left(
f(\theta x + (1-\theta) y)
\leq
\theta f(x) + (1-\theta) f(y)
\right)

\end{eqnarray*}
$$

	</li>
	<li>
		
$
f
$
 is strictly convex if and only if its extended-value extension 
$
\tilde{f}
$
 satisfies
$$
\begin{eqnarray*}

&&
\left(
\forall \mbox{ distinct } x,y\in \dom f, 0< \theta < 1
\right)

\\
&&
\left(
f(\theta x + (1-\theta) y)
<
\theta f(x) + (1-\theta) f(y)
\right)

\end{eqnarray*}
$$

	</li>
	</ul>

</li>
</ul>

<h3>First-order condition for convexity</h3>

<div class="theorem" id="theorem:first-order---condition---for---convexity" data-name="first-order condition for convexity">
	
differentiable 
$
f
$
,
<i>i.e.</i>, 
$
\dom f
$
 is open
and gradient 
$
\nabla f
$
 exists at every point in 
$
\dom f
$
,
is

	<ul>
	<li>
		convex if and only if 
$
\dom f
$
 is convex
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
		strictly convex if and only if 
$
\dom f
$
 is convex
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
for convex function 
$
f
$

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
			<i>e.g.</i>, if 
$
\nabla f(x)=0
$
, 
$
x
$
 is global minimizer

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
	
twice-differentiable 
$
f
$
,
<i>i.e.</i>, 
$
\dom f
$
 is open
and Hessian 
$
\nabla^2 f
$
 exists at every point in 
$
\dom f
$
,
is
convex if and only if 
$
\dom f
$
 is convex
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
		if 
$
\dom f
$
 is convex and

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
	assume function 
$
f:\reals^n\to\reals
$

and 
$
\dom f =\reals^n
$

unlesss specified otherwise

</li>
<li>
	affine function, <i>i.e.</i>, 
$
f(x)=a^Tx +b 
$
 for some 
$
a\in\reals^n
$
 and 
$
b\in\reals
$
, is convex

</li>
<li>
	quadratic functions
- if 
$
f(x) = x^T Px + q^Tx
$

for some 
$
P\in\symset{n}
$
 and 
$
q\in\reals^n
$

	<ul>
	<li>
		
$
f
$
 is convex if and only if 
$
P\succeq0
$


	</li>
	<li>
		
$
f
$
 is strictly convex if and only if 
$
P\succ0
$


	</li>
	</ul>

</li>
<li>
	exponential function,
<i>i.e.</i>, 
$
f(x) = \exp(a^Tx+b)
$
 for some 
$
a\in\reals^n
$
 and 
$
b\in\reals
$
,
is convex

</li>
<li>
	power,
<i>i.e.</i>, 
$
f(x) = x^a
$
 for some 
$
a\geq1
$
,
is convex on 
$
\ppreals
$


</li>
<li>
	power of absolute value,
<i>i.e.</i>, 
$
f(x) = |x|^a
$
 for some 
$
a\geq1
$
,
is convex on 
$
\reals
$


</li>
<li>
	logarithm function,
<i>i.e.</i>, 
$
f(x) = \log x
$
,
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
<i>i.e.</i>, 
$
f(x)=\max(x_1,\ldots,x_n\}
$
,
is convex

</li>
<li>
	quadratic-over-linear function,

$
f(x,y) = x^2/y
$
,
is convex on 
$
\reals\times \ppreals
$


</li>
<li>
	log-sum-exp,

$
f(x) = \log(\exp(x_1)+\cdots+\exp(x_n))
$
,
is convex

</li>
<li>
	geometric mean,

$
f(x) = (\prod_{i=1}^n x_i )^{1/n}
$
,
is concave on $\pprealk{n}$

</li>
<li>
	log-determinant,

$
f(X) = \log \det X
$
,
is concave on $\posdefset{n}$

</li>
</ul>

<h3>Sublevel sets and superlevel sets</h3>

<div class="definition" id="definition:sublevel---sets" data-name="sublevel sets">
	
for function 
$
f
$
 and 
$
\alpha\in\reals
$
,

$$

\set{x\in\dom f}{f(x)\leq \alpha}

$$

called <span class="define">$\alpha$-sublevel set of $f$</span>

</div>
<div class="definition" id="definition:superlevel---sets" data-name="superlevel sets">
	
for function 
$
f
$
 and 
$
\alpha\in\reals
$
,

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
		<i>e.g.</i>, every sublevel set of 
$
\log
$
 is convex, but 
$
\log
$
 is concave

	</li>
	</ul>

</li>
</ul>


<h3>Epigraphs and hypographs</h3>

<div class="definition" id="definition:epigraphs" data-name="epigraphs">
	
for function 
$
f
$
,

$$

\set{(x,t)}{x\in\dom f, f(x)\leq t}

$$

called <span class="define">epigraph of $f$</span>,
denoted by <span class="notation">$\epi f$</span>

</div>
<div class="definition" id="definition:hypographs" data-name="hypographs">
	
for function 
$
f
$
,

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
			for convex functions 
$
f_1
$
, &hellip;, 
$
f_n
$
 and nonnegative weights 
$
w_1,\ldots, w_n
$


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
			for measurable set 
$
Y
$
,

$
w:Y\to\preals
$
,
and

$
f:X \times Y
$

where 
$
f(x,y)
$
 is convex in 
$
x
$
 for every 
$
y\in Y
$

and measurable in 
$
y
$
 for every 
$
x\in X
$


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
			for convex functions 
$
f_1
$
, &hellip;, 
$
f_n
$


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
			for indexed family of convex functions 
$
\indexedcol{f_\lambda}_{\lambda\in\Lambda}
$


$$

\sup_{\lambda \in \Lambda} f_\lambda

$$

is convex
(one way to see this is 
$
\epi \sup_\lambda f_\lambda = \bigcap_\lambda \epi f_\lambda
$
)

		</li>
		</ul>

	</li>
	<li>
		composition
<div id="page:convexity---preserving---operation-------composition"></div>
		<ul>
		<li>
			suppose 
$
g:\reals^n\to\reals^k
$
, 
$
h:\reals^k\to\reals
$
, and 
$
f=h\circ g
$

			<ul>
			<li>
				
$
f
$
 convex if 
$
h
$
 convex &amp; nondecreasing in each argument, and 
$
g_i
$
 convex

			</li>
			<li>
				
$
f
$
 convex if 
$
h
$
 convex &amp; nonincreasing in each argument, and 
$
g_i
$
 concave

			</li>
			<li>
				
$
f
$
 concave if 
$
h
$
 concave &amp; nondecreasing in each argument, and 
$
g_i
$
 concave

			</li>
			<li>
				
$
f
$
 concave if 
$
h
$
 concave &amp; nonincreasing in each argument, and 
$
g_i
$
 convex

			</li>
			</ul>

		</li>
		</ul>

	</li>
	<li>
		minimization
		<ul>
		<li>
			for function 
$
f(x,y)
$
 convex in 
$
(x,y)
$
 and convex set 
$
C
$


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
			for convex function 
$
f:X\to\reals
$
,
function 
$
g:X\times \reals \to \reals
$

defined by

$$

g(x,t) = tf(x/t)

$$

with 
$
\dom g = \set{(x,t)}{x/t \in \dom f, t>0}
$

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
		
$
\max\{a_1^Tx+b_1,\ldots,a_m^T x + b_m\}
$

for some 
$
a_i\in\reals^n
$
 and 
$
b_i\in\reals
$

is convex

	</li>
	</ul>

</li>
<li>
	sum of 
$
k
$
 largest components is convex, <i>i.e.</i>
	<ul>
	<li>
		
$
x_{[1]} + \cdots + x_{[k]}
$

where 
$
x_{[i]}
$
 denotes 
$
i
$
-th largest component,
is convex
(since 
$
f(x) = \max\set{x_{i_1}+\cdots+x_{i_r}}{1\leq i_1< i_2<\cdots < i_r\leq n}
$
)

	</li>
	</ul>

</li>
<li>
	support function of set, <i>i.e.</i>,
	<ul>
	<li>
		
$
\sup\set{x^Ty}{y\in A}
$

for 
$
A\subset\reals^n
$

is convex

	</li>
	</ul>

</li>
<li>
	distance (when measured by arbitrary norm) to farthest point of set
	<ul>
	<li>
		
$
\sup\set{\|x-y\|}{y\in A}
$

for 
$
A\subset\reals^n
$

is convex

	</li>
	</ul>

</li>
<li>
	least-squares cost as function of weights
	<ul>
	<li>
		
$
\inf_{x\in\reals^n} \sum^n_{i=1} w_i(a_i^Tx - b_i)^2
$
 for some 
$
a_i\in\reals^n
$
 and 
$
b_i\in\reals
$

is concave
		<ul>
		<li>
			note that above function equals to

$

\sum_{i=1}^n w_i b_i^2 - \sum_{i=1}^n w_i^2 b_i^2 a_i^T \left( \sum_{j=1}^n w_ja_ja_j^T\right)^{-1} a_i

$

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
		
$
\lambda_\mathrm{max}(F(x)) = \sup\set{y^TF(x)y}{\|y\|_2 \leq 1}
$

where 
$
F:\reals^n\to \symset{m}
$

is linear function in 
$
x
$


	</li>
	</ul>

</li>
<li>
	norm of matrix
	<ul>
	<li>
		
$
\sup\set{u^TG(x)v}{\|u\|_2 \leq 1, \|v\|_2\leq1}
$

where 
$
G:\reals^n\to \reals^{m\times n}
$

is linear function in 
$
x
$


	</li>
	</ul>

</li>
<li>
	distance (when measured by arbitrary norm) to convex set
	<ul>
	<li>
		for convex set 
$
C
$
,

$
\inf\set{\|x-y\|}{y\in C}
$


	</li>
	</ul>

</li>
<li>
	infimum of convex function
subject to linear constraint
	<ul>
	<li>
		for convex function 
$
h
$
,

$
\inf\set{h(y)}{Ay=x}
$
 is convex
(since it is 
$
\inf_y (h(y) + I_{Ay=x}(x,y))
$
)

	</li>
	</ul>

</li>
<li>
	perspective of Euclidean norm squared
	<ul>
	<li>
		map 
$
(x,t) \mapsto x^Tx /t
$

induces convex function in 
$
(x,t)
$
 for 
$
t>0
$


	</li>
	</ul>

</li>
<li>
	perspective of negative log
	<ul>
	<li>
		map 
$
(x,t) \mapsto -t \log(x/t)
$

induces convex function in 
$
(x,t) \in \pprealk{2}
$


	</li>
	</ul>

</li>
</ul>



<ul>
<li>
	perspective of convex function
	<ul>
	<li>
		for convex function 
$
f:\reals^n\to\reals
$
,
function 
$
g:\reals^n\to\reals
$

defined by

$$

g(x) = (c^T x + d) f((Ax+b)/(c^T x + d))

$$

from some 
$
A\in\reals^{m\times n}
$
, 
$
b\in\reals^m
$
, 
$
c\in\reals^n
$
, and 
$
d\in\reals
$

with 
$
\dom g = \set{x}{(Ax+b)/(c^Tx + d)\in \dom f, c^T x + d >0}
$

is convex

	</li>
	</ul>

</li>
</ul>

<h3>Conjugate functions</h3>

<div class="definition" id="definition:conjugate---functions" data-name="conjugate functions">
	
for function 
$
f
$


$$

\sup_{y\in \dom f} (x^Ty - f(y))

$$

called <span class="define">conjugate function of $f$</span>,
denoted by <span class="notation">$f^\ast$</span>

</div>

<ul>
<li>
	conjugate function is convex for any function 
$
f
$

because it is supremum
of linear (hence convex) functions (in 
$
x
$
)
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
	
for convex and closed function 
$
f
$


$$

f^{\ast\ast} = f

$$

where closed function 
$
f
$
 is defined by function with closed 
$
\epi f
$


</div>

<h3>Conjugate function examples</h3>

<ul>
<li>
	strictly convex quadratic function
	<ul>
	<li>
		for 
$
f:\reals^n \to \preals
$

defined 
$
f(x) = x^TQx/2
$
 where 
$
Q\in \posdefset{n}
$
,

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
function 
$
f:\posdefset{n} \to \reals
$

defined by 
$
f(X) = \log \det X^{-1}
$


$$

f^\ast(X)
=
\sup_{Y\in\posdefset{n}} (\Tr XY + \log \det Y)
= \log\det (-X)^{-1} - n

$$

where 
$
\dom f^\ast = -\posdefset{n}
$


	</li>
	</ul>

</li>
<li>
	indicator function
	<ul>
	<li>
		for
indicator function 
$
I_A:\reals^n\to\{0,\infty\}
$
 with 
$
A\subset \reals^n
$


$$

I_A^\ast(x) = \sup_y (y^Tx - I_A(y)) = \sup \set{y^Tx}{y\in A}

$$

which is support function of 
$
A
$


	</li>
	</ul>

</li>
<li>
	log-sum-exp function
	<ul>
	<li>
		for
function 
$
f: \reals^n \to \reals
$

defined by 
$
f(x) = \log(\sum_{i=1}^n \exp(x_i))
$


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
		for norm function 
$
f:\reals^n\to\preals
$
 defined by 
$
f(x)=\|x\|
$


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
function 
$
f: \reals \to \preals
$

defined by 
$
f(x) = \|x\|^2/2
$


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
differentiable convex function 
$
f:\reals^n\to\reals
$


$$

f^\ast(x)=
(y^\ast)^T \nabla f(y^\ast) - f(y^\ast)

$$

where 
$
y^\ast = \argsup_y (x^Ty-f(y))
$


	</li>
	</ul>

</li>
<li>
	sum of independent functions
	<ul>
	<li>
		for
function 
$
f:\reals^n\times \reals^m \to \reals
$
 defined by 
$
f(x,y) = f_1(x) + f_2(y)
$

where 
$
f_1:\reals^n\to\reals
$
 and 
$
f_2:\reals^m\to\reals
$


$$

f^\ast(x,y) = f_1^\ast(x) + f_2^\ast(y)

$$


	</li>
	</ul>

</li>
</ul>

<h3>Convex functions \wrt\ generalized inequalities</h3>

<div class="definition" id="definition:$K$-convex---functions" data-name="$K$-convex functions">
	
for proper cone 
$
K
$
,

	<ul>
	<li>
		function 
$
f
$
 satisfying

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
		function 
$
f
$
 satisfying

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
	
for proper cone 
$
K
$


	<ul>
	<li>
		function 
$
f
$
 is 
$
K
$
-convex if and only if for every 
$
w\succeq_{K^\ast}0
$
, 
$
w^Tf
$
 is convex

	</li>
	<li>
		function 
$
f
$
 is strictly 
$
K
$
-convex if and only if for every nonzero 
$
w\succeq_{K^\ast}0
$
, 
$
w^Tf
$
 is strictly convex

	</li>
	</ul>

</div>

<h3>Matrix convexity</h3>

<div class="definition" id="definition:matrix---convexity" data-name="matrix convexity">
	
function of 
$
\reals^n
$
 into $\symset{m}$
which is 
$
K
$
-convex where 
$
K=\possemidefset{m}
$
,
called <span class="define">matrix convex</span>

</div>
<ul>
<li>
	examples of matrix convexity
	<ul>
	<li>
		function of 
$
\reals^{n\times m}
$
 into $\possemidefset{n}$
defined by 
$
X\mapsto XX^T
$

is matrix convex

	</li>
	<li>
		function of $\posdefset{n}$ into itself
defined by 
$
X\mapsto X^p
$

is matrix convex for 
$
1\leq p\leq 2
$
 or 
$
-1\leq p \leq0
$
,
and matrix concave for 
$
0\leq p\leq1
$


	</li>
	<li>
		function of $\symset{n}$ into $\posdefset{n}$
defined by 
$
X\mapsto \exp(X)
$

is <i>not</i> matrix convex

	</li>
	<li>
		quadratic matrix function of 
$
\reals^{m\times n}
$
 into $\symset{n}$
defined by 
$
X\mapsto X^TAX + B^TX + X^TB + C
$

for 
$
A\in\symset{m}
$
, 
$
B\in\reals^{m\times n}
$
, and 
$
C\in\symset{n}
$

is matrix convex when 
$
A\succeq0
$


	</li>
	</ul>

</li>
</ul>


<h2 id="title-page:Convex---Optimization---Problems">Convex Optimization Problems</h2>


<h3>Optimization problems</h3>

<div class="definition" id="definition:optimization---problems" data-name="optimization problems">
	
for 
$
\fobj:\xobj \to \reals
$
, 
$
\fie: \xie\to \reals^m
$
, 
$
\feq: \xeq \to \reals^p
$

where $\xobj$, $\xie$, and $\xeq$ are subsets of common set 
$
\xdomain
$


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
where 
$
x
$
 is <span class="define">optimization variable</span>

	<ul>
	<li>
		$\fobj$, $\fie$, and $\feq$ are
<span class="define">objective function</span>,
<span class="define">inequality \& equality contraint function</span>

	</li>
	<li>
		
$
\fie(x) \preceq 0
$
 and 
$
\feq(x) = 0
$

are
<span class="define">inequality contraints</span>
and
<span class="define">equality contraints</span>

	</li>
	<li>
		
$
\optdomain = \xobj \cap \xie \cap \xeq
$
 is <span class="define">domain</span> of optimization problem

	</li>
	<li>
		
$
\optfeasset =\set{x\in \optdomain}{\fie(x) \preceq0, \feq(x)=0}
$
, called <span class="define">feasible set</span>,

$
x\in\optdomain
$
, said to be <span class="define">feasible</span> if 
$
x\in\optfeasset
$
,
optimization problem, said to be <span class="define">feasible</span> if 
$
\optfeasset\neq \emptyset
$


	</li>
	<li>
		
$
p^\ast = \inf\set{\fobj(x)}{x\in\optfeasset}
$
, called <span class="define">optimal value</span> of optimization problem

	</li>
	<li>
		if optimization problem is <i>infeasible</i>, <span class="define">$p^\ast = \infty$</span>
(following convention that infimum of empty set is 
$
\infty
$
)

	</li>
	<li>
		if 
$
p^\ast=-\infty
$
,
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
		
$
x\in \optfeasset
$
 with 
$
\fobj(x) = p^\ast
$
, called <span class="define">(global) optimal point</span>

	</li>
	<li>
		
$
X_\mathrm{opt} = \set{x\in \optfeasset}{\fobj(x)=p^\ast}
$
, called <span class="define">optimal set</span>

	</li>
	<li>
		when 
$
X_\mathrm{opt} \neq \emptyset
$
, we say optimal value is <span class="define">attained</span> or <span class="define">achieved</span>
and
optimization problem is <span class="define">solvable</span>

	</li>
	</ul>

</div>

<ul>
<li>
	optimization problem is <i>not</i> solvable if 
$
p^\ast = \infty
$
 or 
$
p^\ast = -\infty
$

(converse is not true)

</li>
</ul>
<div class="definition" id="definition:local---optimality" data-name="local optimality">
	
for optimization problem
in <a href="#definition:optimization---problems"></a>
where 
$
\xdomain
$
 is metric space,

$
x\in\optfeasset
$
 satisfying

$

\inf\set{\fobj(z)}{z\in\optfeasset, \rho(z,x)\leq r}

$

where 
$
\rho:\xdomain\times \xdomain\to\preals
$
 is metric,
for some 
$
r>0
$
, said to be <span class="define">locally optimal</span>,
<i>i.e.</i>,

$
x
$
 solves

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
	
since if 
$
(x^\ast, y^\ast)
$
 solves first,

$
(u,v)=(x^\ast/2, 3y^\ast)
$
 solves second,
and if 
$
(u^\ast, v^\ast)
$
 solves second,

$
(x,y)=(2u^\ast, v^\ast/3)
$
 solves first

</li>
</ul>

<h3>Change of variables</h3>

<ul>
<li>
	given function 
$
\phi:\mathcalfont{Z} \to \xdomain
$
,
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

where 
$
z\in\mathcalfont{Z}
$
 is optimization variable

</li>
<li>
	if 
$
\phi
$
 is injective and 
$
\optdomain \subset \phi(\mathcalfont{Z})
$
,
above optimization problem
and
optimization problem in <a href="#definition:optimization---problems"></a>
are equivalent,
<i>i.e.</i>
	<ul>
	<li>
		
$
X_\mathrm{opt}
$
 is optimal set of problem in <a href="#definition:optimization---problems"></a>

$
\Rightarrow
$


$
\phi^{-1}(X_\mathrm{opt})
$
 is optimal set of above problem

	</li>
	<li>
		
$
Z_\mathrm{opt}
$
 is optimal set of above problem

$
\Rightarrow
$


$
\phi(Z_\mathrm{opt})
$
 is optimal set of problem in <a href="#definition:optimization---problems"></a>

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
		when 
$
\xdomain= \reals^n
$
, optimization problem can be formulated as

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

for some 
$
A\in\reals^{p\times n}
$
 and 
$
b\in\reals^p
$


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
(<i>i.e.</i>, 
$
\dom \fobj
$
 is open and 
$
\nabla \fobj
$
 exists everywhere in 
$
\dom \fobj
$
)

	<ul>
	<li>
		
$
x\in\optdomain
$
 is optimal if and only if 
$
x\in\optfeasset
$
 and

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
		for unconstrained problems, 
$
x\in\optdomain
$
 is optimal if and only if 
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

where 
$
\xobj=\reals^n
$
 and 
$
P\in\possemidefset{n}
$

	<ul>
	<li>
		
$
x
$
 is optimal if and only if

$$

\nabla \fobj(x) = Px + q = 0

$$

exist three cases
		<ul>
		<li>
			if 
$
P\in\posdefset{n}
$
, exists unique optimum 
$
x^\ast = -P^{-1}q
$


		</li>
		<li>
			if 
$
q\in\range(P)
$
, 
$
X_\mathrm{opt}=-P^\dagger q + \nullspace(P)
$


		</li>
		<li>
			if 
$
q\not\in\range(P)
$
, 
$
p^\ast = -\infty
$


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

where 
$
\xobj = \set{x\in\reals^n}{Ax \prec b}
$

	<ul>
	<li>
		
$
x
$
 is optimal if and only if

$$

\nabla \fobj(x) = \sum_{i=1}^m \frac{1}{b_i-a_i^Tx}a_i = 0

$$

exist three cases
		<ul>
		<li>
			exists unique optimum, which happens if and only if $\set{x}{b_i-a_i^Tx}$ is nonempty and bounded

		</li>
		<li>
			exist infinitely many optima, in which case, 
$
X_\mathrm{opt}
$
 is affine set

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

where 
$
\xdomain=\reals^n
$

	<ul>
	<li>
		
$
x
$
 is optimal if and only if

$$

\nabla \fobj(x) \perp \nullspace(A)

$$

or equivalently,
exists 
$
\nu\in\reals^p
$

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
with 
$
\xdomain=\reals^n
$
 and linear $\fobj$ &amp; $\fie$,
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

where 
$
c\in\reals^n
$
, 
$
C\in\reals^{m\times n}
$
, 
$
d\in\reals^m
$
, 
$
A\in\reals^{p\times n}
$
, 
$
b\in\reals^p
$


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
find amount of 
$
n
$
 different food to minimize purchase cost
while satisfying nutrition requirements
	<ul>
	<li>
		assume exist 
$
n
$
 food and 
$
m
$
 nutritions,

$
c_i
$
 is cost of food 
$
i
$
,

$
A_{ji}
$
 is amount of nutrition 
$
j
$
 contained in unit quantity of food 
$
i
$
,

$
b_j
$
 is amount requirement for nutrition 
$
j
$


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

where optimization variables are 
$
x\in\reals^n
$
 and 
$
r\in\reals
$


	</li>
	</ul>

</li>
<li>
	piecewise-linear minimization
- minimize maximum of affine functions
	<ul>
	<li>
		assume 
$
m
$
 affine functions 
$
a_i^Tx + b_i
$


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

$
\xdomain=\reals^n
$
 and
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

$
P\in\possemidefset{n}
$
, 
$
q\in\reals^n
$
,

$
G\in\reals^{m\times n}
$
, 
$
h\in\reals^m
$
,

$
A\in\reals^{p\times n}
$
, 
$
b\in\reals^p
$


</div>
<ul>
<li>
	when 
$
P=0
$
, QP reduces to LP,
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
with 
$
\xdomain=\reals^n
$

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

$
P_i\in\possemidefset{n}
$
, 
$
q_i\in\reals^n
$
, 
$
r_i\in\reals
$
,

$
A\in\reals^{p\times n}
$
, 
$
b\in\reals^p
$


</div>
<ul>
<li>
	when 
$
P_i=0
$
 for 
$
i=1,\ldots,m
$
, QCQP reduces to QP,
hence <i>QP is specialization of QCQP</i>

</li>
</ul>

<h3>Second-order cone programming</h3>

<div class="definition" id="definition:second-order---cone---programming" data-name="second-order cone programming">
	
convex optimization problem in <a href="#definition:convex---optimization"></a>
with 
$
\xdomain=\reals^n
$

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

$
f\in\reals^n
$
,

$
A_i\in\reals^{n_i\times n}
$
, 
$
b_i\in\reals^{n_i}
$
,

$
c_i\in\reals^{n}
$
, 
$
d_i\in\reals
$
,

$
F\in\reals^{p\times n}
$
, 
$
g\in\reals^p
$

called <span class="define">second-order cone program (SOCP)</span>

</div>
<ul>
<li>
	when 
$
b_i=0
$
, SOCP reduces to QCQP,
hence <i>QCQP is specialization of SOCP</i>

</li>
</ul>

<h3>SOCP examples</h3>

<ul>
<li>
	robust linear program
-
minimize 
$
c^T x
$

while satisfying

$
\tilde{a}_i^T x \leq b_i
$

for every 
$
\tilde{a}_i \in \set{a_i+P_iu}{\|u\|_2\leq1}
$

where 
$
P_i\in\symset{n}
$

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
minimize 
$
c^T x
$

while satisfying

$
\tilde{a}_i^T x \leq b_i
$

with probability no less than 
$
\eta
$

where 
$
\tilde{a} \sim \normal(a_i,\Sigma_i)
$

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
	
function 
$
f:\pprealk{n}\to\reals
$

defined by

$$

f(x) = cx_1^{a_1} \cdots x_n^{a_n}

$$

where 
$
c>0
$
 and 
$
a_i\in\reals
$
,
called <span class="define">monomial function</span>
or simply <span class="define">monomial</span>

</div>
<div class="definition" id="definition:posynomial---functions" data-name="posynomial functions">
	
function 
$
f:\pprealk{n}\to\reals
$

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

for posynomials 
$
\fobj:\pprealk{n} \to \reals
$
 &amp; 
$
\fie: \pprealk{n} \to \reals^m
$

and monomials 
$
\feq: \pprealk{n} \to \reals^p
$
,
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

for some 
$
a^{(i)}_k\in\reals^n
$
, 
$
b^{(i)}_k\in\reals
$
, 
$
G\in\reals^{p\times n}
$
, 
$
h\in\reals^p
$

where optimization variable is 
$
y=\log(x)\in\reals^n
$


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

$
K_i\subset R^{k_i}
$
 are proper cones
and

$
\fie_i:\xie_i\to\reals^{k_i}
$
 are 
$
K_i
$
-convex,
called <span class="define">convex optimization problem with generalized inequality constraints</span>

</div>

<ul>
<li>
	problem in <a href="#definition:convex---optimization---with---generalized---inequality---constraints"></a>
reduces to convex optimization problem in <a href="#definition:convex---optimization"></a>
when 
$
q=1
$
 and 
$
K_1=\prealk{m}
$
,
hence <i>convex optimization is specialization of convex optimization with generalized inequalities</i>

</li>
<li>
	like convex optimization
	<ul>
	<li>
		feasible set is 
$
\optfeasset = \set{x\in\optdomain}{\fie_i(x)\preceq_{K_i} 0, Ax=b}
$
 is convex

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
with 
$
\xdomain=\reals^n
$
 and 
$
K=\possemidefset{n}
$


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

where 
$
F_1,\ldots,F_n,G\in\symset{k}
$
 and 
$
A\in\reals^{p\times n}
$
,
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

where 
$
\xdomain=\possemidefset{n}
$
 and 
$
C,A_1,\ldots,A_p\in\symset{n}
$
 and 
$
b_i\in\reals
$


	</li>
	</ul>

</div>

<h3>SDP examples</h3>

<ul>
<li>
	LP
	<ul>
	<li>
		if 
$
k=m
$
, 
$
F_i=\diag(C_{1,i}, \ldots, C_{m,i})
$
, 
$
G=-\diag(d_1,\ldots, d_m)
$

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
with 
$
\xdomain=\reals^n
$

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

$
c\in\reals^n
$
,

$
C_1,\ldots,C_n,D\in\symset{l}
$
,

$
F_1,\ldots,F_n,G\in\symset{k}
$
,
and

$
A\in\reals^{p\times n}
$
,
called <span class="define">determinant maximization problem</span>
or simply <span class="define">max-det problem</span>
(since it maximizes determinant of (positive definite) matrix with constraints)

</div>
<ul>
<li>
	if 
$
l=1
$
, 
$
C_1=\cdots=C_n=0
$
, 
$
D=1
$
,
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
with nonempty domain 
$
\optdomain
$
,
function 
$
L:\optdomain \times \reals^m \times \reals^p \to \reals
$

defined by

$$

L(x,\lambda, \nu) = \fobj(x) + \lambda^T \fie(x) + \nu^T \feq(x)

$$

called <span class="define">Lagrangian</span> associated with the optimization problem
where

	<ul>
	<li>
		
$
\lambda
$
, called <span class="define">Lagrange multiplier associated inequality constraints</span> 
$
\fie(x)\preceq0
$


	</li>
	<li>
		
$
\lambda_i
$
, called <span class="define">Lagrange multiplier associated $i$-th inequality constraint</span> 
$
\fie_i(x)\leq0
$


	</li>
	<li>
		
$
\nu
$
, called <span class="define">Lagrange multiplier associated equality constraints</span> 
$
\feq(x)=0
$


	</li>
	<li>
		
$
\nu_i
$
, called <span class="define">Lagrange multiplier associated $i$-th equality constraint</span> 
$
\feq_i(x)=0
$


	</li>
	<li>
		
$
\lambda
$
 and 
$
\nu
$
,
called <span class="define">dual variables</span> or <span class="define">Lagrange multiplier vectors</span> associated with the optimization problem

	</li>
	</ul>

</div>



<h3>Lagrange dual functions</h3>

<div class="definition" id="definition:Lagrange---dual---functions" data-name="Lagrange dual functions">
	
for optimization problem in <a href="#definition:optimization---problems"></a>
for which Lagrangian is defined,
function 
$
g:\reals^m \times \reals^p \to \reals\cup \{-\infty\}
$

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
	
$
g
$
 is <i>(always) concave function</i> (even when optimization problem is not convex)
	<ul>
	<li>
		since is pointwise infimum of linear (hence concave) functions is concave

	</li>
	</ul>

</li>
<li>
	
$
g(\lambda,\nu)
$
 provides
lower bound for optimal value of associated optimization problem,
<i>i.e.</i>,

$$

g(\lambda,\nu) \leq p^\ast

$$

for every 
$
\lambda\succeq0
$
 

</li>
<li>
	
$
(\lambda,\nu) \in \set{(\lambda,\nu)}{\lambda\succeq0, g(\lambda,\nu)>-\infty}
$
,
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
		Lagrangian - 
$
L(x,\nu) = x^T x + \nu^T(Ax-b)
$


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
		Lagrangian - 
$
L(x,\lambda,\nu) = c^T x - \lambda^T x + \nu^T(Ax-b)
$


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

where 
$
W\in\symset{n}
$

	<ul>
	<li>
		Lagrangian - 
$
L(x,\nu) = x^T(W+\diag(\nu))x - \ones^Tx
$


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
		Lagrangian - 
$
L(x,\nu) =f(x)+\nu^Tx
$


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
			hence, set of dual feasible points is 
$
-\dom f^\ast
$
,
and
for every 
$
f:\reals^n\to\reals
$
 and 
$
\nu\in\reals^n
$


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
		Lagrangian - 
$
L(x,\lambda, \nu) = f(x) + \lambda^T(Ax-b) + \nu^T(Cx-d)
$


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
		Lagrangian - 
$
L(x,\nu) = \|x\| + \nu^T(Ax-b)
$


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
		Lagrangian - 
$
L(x,\lambda,\nu) = \sum_{i=1}^n x_i\log x_i + \lambda^T(Ax-b) + \nu(\ones^Tx-1)
$


	</li>
	<li>
		Lagrange dual function
<div id="page:dual---function---of---entropy---maximization"></div>

$$

g(\lambda,\nu) = \entmax{dual fcn}

$$

obtained using 
$
f^\ast(y) = \sum_{i=1}^n \exp(y_i-1)
$

where 
$
a_i
$
 is 
$
i
$
-th column vector of 
$
A
$


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
		Lagrangian - 
$
L(X,\lambda) = -\log \det X + \sum_{i=1}^m \lambda_i(a_i^T X a_i - 1)
$


	</li>
	<li>
		Lagrange dual function
<div id="page:dual---function---of---minimum---volume---covering---ellipsoid"></div>

$$

g(\lambda)
= \minvolcovering{dual fcn}

$$

obtained using 
$
f^\ast(Y) = -\log\det(-Y) - n
$


	</li>
	</ul>

</li>
</ul>

<h3>Best lower bound</h3>

<ul>
<li>
	for every 
$
(\lambda,\nu)
$
 with 
$
\lambda\succeq 0
$
,
Lagrange dual function 
$
g(\lambda,\nu)
$
 (in <a href="#definition:Lagrange---dual---functions"></a>)
provides lower bound for optimal value 
$
p^\ast
$

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
		domain is 
$
\reals^m\times \reals^p
$


	</li>
	<li>
		<span class="define">dual feasibility</span> defined in page~<a href="#page:dual---feasible">here</a>,
<i>i.e.</i>, 
$
(\lambda,\nu)
$
 satisfying

$

\lambda \succeq 0 \quad g(\lambda,\nu) > -\infty

$

indeed means
feasibility for Lagrange dual problem

	</li>
	<li>
		
$
d^\ast = \sup\set{g(\lambda,\nu)}{\lambda\in\reals^m,\:\nu\in\reals^p,\:\lambda\succeq 0}
$
,
called <span class="define">dual optimal value</span>

	</li>
	<li>
		
$
(\lambda^\ast,\nu^\ast) = \argsup\set{g(\lambda,\nu)}{\lambda\in\reals^m,\:\nu\in\reals^p,\:\lambda\succeq 0}
$
,
said to be <span class="define">dual optimal</span> or called <span class="define">optimal Lagrange multipliers</span> (if exists)

	</li>
	</ul>

</div>


<ul>
<li>
	Lagrange dual problem in <a href="#definition:Lagrange---dual---problems"></a>
is convex optimization (even though original problem is not)
since 
$
g(\lambda,\nu)
$
 is always convex

</li>
</ul>


<h3>Making dual constraints explicit dual problems</h3>

<ul>
<li>
	(out specific) way we define Lagrange dual function in <a href="#definition:Lagrange---dual---functions"></a>
as function 
$
g
$
 of 
$
\reals^m \times \reals^p
$
 into 
$
\reals\cup\{-\infty\}
$
,
<i>i.e.</i>,

$
\dom g = \reals^n\times\reals^p
$


</li>
<li>
	however,
in many cases,
feasible set $\set{(\lambda,\nu)}{\lambda \succeq 0 \quad g(\lambda,\nu) > -\infty}$
is proper subset of 
$
\reals^n\times\reals^p
$


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

\\
&=&
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
\begin{eqnarray*}

{\fobj}^\ast(x)
&=& (x-q)^TP^{-1}(x-q)/4 - r

\\
&=&
x^TP^{-1}x/4
-q^TP^{-1}x/2
+ q^TP^{-1}q/4
-r

\end{eqnarray*}
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

where 
$
A\in\symset{n}
$
, 
$
A\not\in\possemidefset{n}
$
, and 
$
b\in\reals^n
$

	<ul>
	<li>
		since 
$
A\not\succeq 0
$
, not convex optimization problem

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

where 
$
(A+\lambda I)^\dagger
$
 is pseudo-inverse of 
$
A+\lambda I
$


</li>
<li>
	Lagrange dual problem
<div id="page:dual---problem---of---trust---region---nonconvex---quadratic---problems"></div>

$$

\noncvxquadprob{dual}

$$

where optimization variable is 
$
\lambda \in\reals
$

	<ul>
	<li>
		note we do not need constraint 
$
\lambda \geq0
$

since it is implied by 
$
A+\lambda I \succeq 0
$


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

where 
$
\lambda_i
$
 and 
$
q_i
$
 are eigenvalues and corresponding orthogormal eigenvectors of 
$
A
$
,
when 
$
\lambda_i + \lambda=0
$
 for some 
$
i
$
,
we interpret 
$
(q_i^Tb)^2/0
$
 as 0 if 
$
q_i^T0
$
 and 
$
\infty
$
 otherwise

	</li>
	</ul>

</li>
</ul>

<h3>Weak duality</h3>

<ul>
<li>
	since 
$
g(\lambda,\nu)\leq p^\ast
$
 for every 
$
\lambda\succeq 0
$
,
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
		
$
d^\ast
$
 is best lower bound for primal problem
that can be obtained from Lagrange dual function (by definition)

	</li>
	<li>
		weak duality holds even when 
$
d^\ast
$
 or/and 
$
p^\ast
$
 are not finite, <i>e.g.</i>
		<ul>
		<li>
			<i>if primal problem is unbounded below</i> so that 
$
p^\ast=-\infty
$
,
must have 
$
d^\ast = -\infty
$
,
<i>i.e.</i>, <i>dual problem is infeasible</i>

		</li>
		<li>
			conversely,
<i>if dual problem is unbounded above</i> so that 
$
d^\ast = \infty
$
,
must have 
$
p^\ast=\infty
$
,
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

where optimization variable is 
$
\nu\in\reals^n
$

		<ul>
		<li>
			the dual problem can be solved very efficiently using polynomial time algorithms
while primal problme <i>cannot</i> be solved unless 
$
n
$
 is very small

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
and exists feasible 
$
x\in\optdomain
$
 contained in 
$
\relint \optdomain
$

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
- if first 
$
k
$
 inequality constraint functions 
$
\fie_1
$
, &hellip;, 
$
\fie_k
$
 are affine,
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
&ldquo;primal is feasible 
$
\Rightarrow
$
 Slater's condition holds'',
thus
Slater's theorem (<a href="#theorem:Slater's---theorem"></a>)
implies,
exist only three cases
	<ul>
	<li>
		
$
(d^\ast = p^\ast \in \reals)
$

or

$
(d^\ast \in \reals\:\&\: p^\ast = \infty)
$

or

$
(d^\ast = p^\ast = \infty)
$


	</li>
	</ul>

</li>
<li>
	if primal is infeasible, though,

$
b\not\in\range(A)
$
,
thus
exists 
$
z
$
, such that 
$
A^Tz=0
$
 and 
$
b^Tz \neq0
$
,
then line $\set{tz}{t\in\reals}$ makes dual problem unbounded above,
hence 
$
d^\ast=\infty
$


</li>
<li>
	hence, <i>strong duality always holds</i>,
<i>i.e.</i>, 
$
(d^\ast= p^\ast \in \reals)
$
 or 
$
(d^\ast = p^\ast = \infty)
$


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
either 
$
(d^\ast=p^\ast= -\infty)
$
 or 
$
(d^\ast=p^\ast\in\reals)
$


	</li>
	<li>
		if dual is feaisble,
either 
$
(d^\ast=p^\ast= \infty)
$
 or 
$
(d^\ast=p^\ast\in\reals)
$


	</li>
	<li>
		only other case left is 
$
(d^\ast=-\infty\;\&\;p^\ast= \infty)
$

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
if exists 
$
x\succ 0
$
 with 
$
Ax \preceq b
$
 and 
$
\ones^T x =1
$
,
strong duality holds,
and indeed 
$
d^\ast=p^\ast\in\reals
$


</li>
<li>
	by the way,
can simplify dual problem by maximizing dual objective function over 
$
\nu
$


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

where 
$
\optdomain=\posdefset{n}
$


</li>
<li>
	dual problem

$$

\minvolcovering{dual}

$$

(refer to page~<a href="#page:dual---function---of---minimum---volume---covering---ellipsoid">here</a> for Lagrange dual function)

</li>
<li>
	
$
X=\alpha I
$
 with large enough 
$
\alpha>0
$
 satisfies primal's constraints,
hence Slater's condition <i>always</i> holds,
thus,
<i>strong duality always holds</i>,
<i>i.e.</i>, 
$
(d^\ast = p^\ast \in \reals)
$
 or 
$
(d^\ast = p^\ast = -\infty)
$


</li>
<li>
	in fact, 
$
\range(a_1,\ldots,a_m) = \reals^n
$
 if and only if 
$
d^\ast=p^\ast\in\reals^n
$


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

where 
$
A\in\symset{n}
$
, 
$
A\not\in\possemidefset{n}
$
, and 
$
b\in\reals^n
$


</li>
<li>
	Lagrange dual problem (page~<a href="#page:dual---problem---of---trust---region---nonconvex---quadratic---problems">here</a>)

$$

\noncvxquadprob{dual}

$$


</li>
<li>
	<i>strong duality always holds</i>
and 
$
d^\ast=p^\ast\in\reals
$

(since dual problem is feasible - large enough 
$
\lambda
$
 satisfies dual constraints)

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
	matrix game - consider game with two players 
$
A
$
 and 
$
B
$

	<ul>
	<li>
		player 
$
A
$
 makes choice 
$
1\leq a\leq n
$
,
player 
$
B
$
 makes choice 
$
1\leq b\leq m
$
,
then player 
$
A
$
 makes payment of 
$
P_{ab}
$
 to player 
$
B
$


	</li>
	<li>
		matrix 
$
P\in\reals^{n\times m}
$
, called <span class="define">payoff matrix</span>

	</li>
	<li>
		player 
$
A
$
 tries to pay as little as possible
&amp;
player 
$
B
$
 tries to received as much as possible

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
	expected payoff (from player 
$
A
$
 to player 
$
B
$
)

$$

\sum_i \sum_j u_iv_jP_{ij} = u^TPv

$$


</li>
<li>
	assume player 
$
A
$
's strategy is known to play 
$
B
$

	<ul>
	<li>
		player 
$
B
$
 will choose 
$
v
$
 to maximize 
$
u^TPv
$


$$

\sup\set{u^TPv}{v\succeq 0,\; \ones^Tv=1}
= \max_{1\leq j\leq m} (P^Tu)_j

$$


	</li>
	<li>
		player 
$
A
$
 (assuming that player 
$
B
$
 will employ above strategy to maximize payment)
will choose 
$
u
$
 to minimize payment

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
	assume player 
$
B
$
's strategy is known to play 
$
A
$

	<ul>
	<li>
		then player 
$
B
$
 will do same to maximize payment
(assuming that player 
$
A
$
 will employ such strategy to minimize payment)

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
player 
$
B
$
 has advantage over player 
$
A
$
 because 
$
A
$
's strategy's exposed to 
$
B
$
,
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
	eliminating 
$
\lambda_2
$
 gives
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
hence 
$
d^\ast=p^\ast\in\reals
$
,
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
	for every 
$
\lambda\succeq 0
$
 and 
$
\nu
$


$$
\begin{eqnarray*}

p^\ast &=& \inf\set{t}{(u,v,t) \in G, u\preceq 0, v = 0}

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

$

\set{(u,v,t)}{(u,v,t) \in G, u\preceq 0, v = 0} \subset G

$


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

hence if 
$
g(\lambda,\nu) > -\infty
$
,

$
(\lambda, \nu, 1)
$
 and 
$
g(\lambda,\nu)
$
 define
<i>nonvertical</i>
<i>supporting hyperplane</i> for 
$
G
$

- nonvertical because third component is nonzero

</li>
</ul>

<ul>
<li>
	the figure
shows 
$
G
$
 as area inside closed curve
contained in 
$
\reals^m\times\reals^p\times\reals
$
 where 
$
m=1
$
 and 
$
p=0
$

as primal optimal value 
$
p^\ast
$
 and supporting hyperplane

$
\lambda u + t = g(\lambda)
$


</li>
</ul>




<div id="fig:geometric---interpretation---of---duality-------1"></div>


<ul>
<li>
	the figure
shows three hyperplanes determined by three values for 
$
\lambda
$
,
one of which 
$
\lambda^\ast
$
 is optimal solution for dual problem

</li>
</ul>




<div id="fig:geometric---interpretation---of---duality-------2"></div>



<h3>Epigraph interpretation of duality</h3>

<ul>
<li>
	define extended graph over 
$
G
$
 - sort of epigraph of 
$
G
$


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
	if 
$
\lambda\succeq 0
$
, 
$
g(\lambda,\nu) = \inf\set{(\lambda,\nu,1)^T(u,v,t)}{(u,v,t) \in H}
$
, thus

$$

(\lambda,\nu,1)^T (u,v,t) \geq g(\lambda,\nu)

$$

defines nonvertical supporting hyperplane for 
$
H
$


</li>
<li>
	now 
$
p^\ast = \inf\set{t}{(0,0,t)\in H}
$
, hence 
$
(0,0,p^\ast) \in \boundary H
$
, hence

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
exists 
$
x\in\optdomain
$

such that 
$
\fie(x) \prec 0
$
 and 
$
\feq(x) = 0
$


</li>
<li>
	further assume $\optdomain$ has interior (hence, 
$
\relint \optdomain = \interior{\optdomain}
$

and 
$
\rank A=p
$


</li>
<li>
	assume 
$
p^\ast\in\reals
$
 - since exists feasible 
$
x
$
, the other possibility is 
$
p^\ast = -\infty
$
,
but then, 
$
d^\ast = -\infty
$
, hence strong duality holds

</li>
<li>
	
$
H
$
 is convex 

</li>
<li>
	now define

$$

B = \set{(0,0,s)\in\reals^m\times\reals^p\times\reals}{s<p^\ast}

$$


</li>
<li>
	then 
$
B\cap H=\emptyset
$
, hence <a href="#theorem:separating---hyperplane---theorem"></a>
implies exists separable hyperplane with 
$
(\tilde{\lambda}, \tilde{\nu}, \mu)\neq 0
$
 and 
$
\alpha
$

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
	then 
$
\tilde{\lambda} \succeq 0
$
 &amp; 
$
\mu\geq0
$
 - assume 
$
\mu>0
$

	<ul>
	<li>
		can prove when 
$
\mu=0
$
, but kind of tedius, plus,
whole purpose is provide good intuition,
so will not do it here

	</li>
	</ul>

</li>
<li>
	above second inequality implies 
$
\mu p^\ast \leq \alpha
$
 and
for some 
$
x\in\optdomain
$


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

where 
$
\lambda = \tilde{\lambda}/\mu
$
 &amp; 
$
\nu = \tilde{\nu}/\mu
$


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

$

p^\ast = \inf_{x\in\optdomain} \sup_{\lambda\succeq 0, \nu} L(x,\lambda,\nu)

$

whereas

$

d^\ast = \sup_{\lambda\succeq 0,\nu} \inf_{x\in\optdomain} L(x,\lambda,\nu)

$


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

$

\sup_{\lambda\succeq 0} \inf_{x\in\optdomain} L(x,\lambda,\nu)
\leq
\inf_{x\in\optdomain} \sup_{\lambda\succeq 0} L(x,\lambda,\nu)

$

holds for general case

</li>
</ul>
<div class="inequality" id="inequality:max-min---inequality" data-name="max-min inequality">
	
for 
$
f:{X} \times {Y} \to \reals
$


$$

\sup_{y\in{Y}} \inf_{x\in{X}} f(x,y)
\leq
\inf_{x\in{X}} \sup_{y\in{Y}} f(x,y)

$$



</div>
<div class="definition" id="definition:strong---max-min---property" data-name="strong max-min property">
	
if below equality holds, we say

$
f
$
 (and 
$
X
$
 and 
$
Y
$
) satisfies <span class="define">strong max-min property</span>
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

$
X=\optdomain
$
,

$
Y=\prealk{m} \times \reals^p
$
,

$
f
$
 is Lagrangian of
optimization problem
(in <a href="#definition:optimization---problems"></a>)
for which strong duality holds

</li>
</ul>

<h3>Saddle-points</h3>

<div class="definition" id="definition:saddle-points" data-name="saddle-points">
	
for 
$
f:X\times Y\to\reals
$
,
pair 
$
x^\ast\in X
$
 and 
$
y^\ast\in Y
$

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

$
x^\ast
$
 minimizes 
$
f(x,y^\ast)
$
 over 
$
X
$

and

$
y^\ast
$
 maximizes 
$
f(x^\ast,y)
$
 over 
$
Y
$


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
holds with 
$
f(x^\ast,y^\ast)
$
 as common value

	</li>
	</ul>

</li>
</ul>


<h3>Saddle-point interpretation of strong duality</h3>

<ul>
<li>
	for primal optimum 
$
x^\ast
$
 and dual optimum 
$
(\lambda^\ast,\nu^\ast)
$



$$

g(\lambda^\ast,\nu^\ast) \leq L(x^\ast, \lambda^\ast, \nu^\ast) \leq \fobj(x^\ast)

$$


</li>
<li>
	if strong duality holds,
for every 
$
x\in\optdomain
$
, 
$
\lambda\succeq 0
$
, and 
$
\nu
$



$$

L(x^\ast,\lambda,\nu)
\leq
\fobj(x^\ast) = L(x^\ast,\lambda^\ast,\nu^\ast) = g(\lambda^\ast,\nu^\ast)
\leq
L(x,\lambda^\ast, \nu^\ast)

$$

	<ul>
	<li>
		thus 
$
x^\ast
$
 and 
$
(\lambda^\ast,\nu^\ast)
$
 form saddle-point of Lagrangian

	</li>
	</ul>

</li>
<li>
	conversely, if 
$
\tilde{x}
$
 and 
$
(\tilde{\lambda},\tilde{\nu})
$
 are saddle-point of Lagrangian,
<i>i.e.</i>,
for every 
$
x\in\optdomain
$
, 
$
\lambda\succeq 0
$
, and 
$
\nu
$



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

$

g(\tilde{\lambda},\tilde{\nu})
= \inf_{x\in\optdomain} L(x,\tilde{\lambda},\tilde{\nu})
= L(\tilde{x}, \tilde{\lambda},\tilde{\nu})
= \sup_{\lambda\succeq 0, \nu} L(\tilde{x},{\lambda},{\nu}) = \fobj(\tilde{x})

$
,
thus

$
g(\lambda^\ast,\nu^\ast) \leq g(\tilde{\lambda}, \tilde{\nu})
$

&amp;

$
\fobj(\tilde{x}) \leq \fobj(x^\ast)
$


	</li>
	<li>
		thus 
$
\tilde{x}
$
 and 
$
(\tilde{\lambda}, \tilde{\nu})
$
 are primal and dual optimal

	</li>
	</ul>

</li>
</ul>

<h3>Game interpretation</h3>

<div id="page:Game---interpretation"></div>
<ul>
<li>
	assume
two players play zero-sum game with payment function 
$
f:X\times Y\to \reals
$

where
player 
$
A
$
 pays player 
$
B
$
 amount equal to 
$
f(x,y)
$

when player 
$
A
$
 chooses 
$
x
$
 and player 
$
B
$
 chooses 
$
y
$


</li>
<li>
	player 
$
A
$
 will try to minimize 
$
f(x,y)
$

and
player 
$
B
$
 will try to maximize 
$
f(x,y)
$


</li>
<li>
	assume player 
$
A
$
 chooses first
then player 
$
B
$
 chooses after learning opponent's choice
	<ul>
	<li>
		if player 
$
A
$
 chooses 
$
x
$
, player 
$
B
$
 will choose 
$
\argsup_{y\in Y} f(x,y)
$


	</li>
	<li>
		knowing that, player 
$
A
$
 will first choose 
$
\arginf_{x\in X} \sup_{y\in Y} f(x,y)
$


	</li>
	<li>
		hence payment will be 
$
\inf_{x\in X} \sup_{y\in Y} f(x,y)
$


	</li>
	</ul>

</li>
<li>
	if player 
$
B
$
 makes her choise first, opposite happens, <i>i.e.</i>,
payment will be 
$
\sup_{y\in Y} \inf_{x\in X} f(x,y)
$


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
	saddle-point for 
$
f
$
 (and 
$
X
$
 and 
$
Y
$
),

$
(x^\ast,y^\ast)
$
,
called <span class="define">solution of game</span>
- 
$
x^\ast
$
 is optimal choice for player 
$
A
$

and

$
x^\ast
$
 is optimal choice for player 
$
B
$


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
	assume that 
$
X=\xdomain
$
 and 
$
Y=\prealk{n} \times \reals^p
$


</li>
<li>
	if player 
$
A
$
 chooses first, knowing that player 
$
B
$
 will choose 
$
\argsup_{(\lambda,\nu)\in Y}L(x,\lambda,\nu)
$
,
she will choose 
$
x^\ast = \arginf_{x\in\xdomain} \sup_{(\lambda,\nu)\in Y}L(x,\lambda,\nu)
$


</li>
<li>
	likewise, player 
$
B
$
 will choose

$
(\lambda^\ast,\nu^\ast) = \argsup_{(\lambda,\nu)\in Y} \inf_{x\in\xdomain} L(x,\lambda,\nu)
$


</li>
<li>
	optimal dualtiy gap 
$
p^\ast - d^\ast
$
 equals to advantage player who goes second has

</li>
<li>
	if strong dualtiy holds, 
$
(x^\ast, \lambda^\ast, \nu^\ast)
$
 is solution of game,
in which case no one has advantage

</li>
</ul>


<h3>Certificate of suboptimality</h3>

<ul>
<li>
	dual feasible point 
$
(\lambda,\nu)
$

degree of suboptimality of current solution

</li>
<li>
	assume 
$
x
$
 is feasible solution,
then

$$

\fobj(x) - p^\ast \leq \fobj(x) - g(\lambda,\nu)

$$

guarantees that 
$
\fobj(x)
$
 is no further than 
$
\epsilon = \fobj(x) - g(\lambda,\nu)
$

from optimal point point 
$
x^\ast
$

(even though we do not know optimal solution)

</li>
<li>
	for this reason,

$
(\lambda,\nu)
$
, called <span class="define">certificate of suboptimality</span>

</li>
<li>
	
$
x
$
 is 
$
\epsilon
$
-suboptimal for primal problem
and

$
(\lambda,\nu)
$
 is 
$
\epsilon
$
-suboptimal for dual problem

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
and assume 
$
x^\ast
$
 is primal optimum and 
$
(\lambda^\ast,\nu^\ast)
$
 is dual optimum,
then

$$

\fobj(x^\ast)
= L(x^\ast,\lambda^\ast,\nu^\ast)
= \fobj(x^\ast) + {\lambda^\ast}^T \fie(x^\ast) + {\nu^\ast}^T \feq(x^\ast)

$$


</li>
<li>
	
$
\feq(x^\ast)=0
$
 implies 
$
{\lambda^\ast}^T \fie(x^\ast)=0
$


</li>
<li>
	then 
$
\lambda^\ast \succeq 0
$
 and 
$
\fie(x^\ast) \preceq 0
$
 imply

$$

\lambda_i^\ast \fie_i(x^\ast) = 0
\quad
i=1,\ldots,m

$$


</li>
</ul>
<div class="proposition" id="proposition:complementary---slackness" data-name="complementary slackness">
	
when strong duality holds,
for primal and dual optimal points 
$
x^\ast
$
 and 
$
(\lambda^\ast, \nu)
$


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
for 
$
{x}\in\optdomain
$
 and 
$
({\lambda}, {\nu})\in\reals^m\times\reals^p
$


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
primal and dual optimal solutions 
$
x^\ast
$
 and 
$
(\lambda^\ast, \nu)
$

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
and 
$
{x}\in\optdomain
$
 and 
$
({\lambda}, {\nu})\in\reals^m\times\reals^p
$

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
	since 
$
L(x,\lambda,\nu)
$
 is convex for 
$
\lambda\succeq 0
$
,
<i>i.e.</i>,
each of 
$
\fobj(x)
$
, 
$
\lambda^T \fie(x)
$
, and 
$
\nu^T \feq(x)
$

is convex,
vanishing gradient implies 
$
x
$
 achieves infimum for Lagrangian,
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

$
x
$
 and 
$
(\lambda,\nu)
$
 are primal and dual optimal solutions
with zero duality gap

</li>
</ul>




<div class="theorem" id="theorem:KKT---and---convexity---sufficient---for---optimality---with---strong---duality" data-name="KKT and convexity sufficient for optimality with strong duality">
	
for convex optimization problem in <a href="#definition:convex---optimization"></a>
where $\fobj$, $\fie$, and $\feq$ are all differentiable,
if 
$
{x}\in\optdomain
$
 and 
$
({\lambda}, {\nu})\in\reals^m\times\reals^p
$

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

where 
$
(\lambda^\ast, \nu^\ast)
$
 is dual optimum

</li>
<li>
	example - entropy maximization
(
$
\optdomain = \pprealk{n}
$
)
	<ul>
	<li>
		primal problem - 

	</li>
	<li>
		dual problem - 

	</li>
	<li>
		provided dual optimum 
$
(\lambda^\ast,\nu^\ast)
$
,
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
		
$
\nabla_x L(x,\lambda^\ast,\nu^\ast) = \log x + A^T \lambda^\ast + (1+\nu^\ast)\ones
$
,
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

where 
$
u\in\reals^m
$
 and 
$
v\in\reals^p
$


</li>
<li>
	define 
$
p^\ast(u,v)
$
 as optimal value of above <i>perturbed</i> problem,
<i>i.e.</i>

$$

p^\ast(u,v) = \inf\set{\fobj(x)}{x\in\optdomain, \fie(x) \preceq u, \feq(x) = v}

$$

which is convex
when problem is convex optimization problem

- note

$
p^\ast(0,0)=p^\ast
$


</li>
<li>
	assume and dual optimum 
$
(\lambda^\ast,\nu^\ast)
$
,
if strong duality holds,
for every feasible 
$
x
$
 for perturbed problem
$$
\begin{eqnarray*}

p^\ast(0,0) =g(\lambda^\ast,\nu^\ast)
&\leq& \fobj(x) + {\lambda^\ast}^T \fie(x) + {\nu^\ast}^T \feq(x)

\\
&\leq& \fobj(x) + {\lambda^\ast}^T u + {\nu^\ast}^T v

\end{eqnarray*}
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
		if 
$
\lambda^\ast_i
$
 is large, when 
$
i
$
-th inequality constraint is tightened,
optimal value increases a lot

	</li>
	<li>
		if 
$
\lambda^\ast_i
$
 is small, when 
$
i
$
-th inequality constraint is relaxed,
optimal value decreases not a lot

	</li>
	<li>
		if 
$
|\nu^\ast_i|
$
 is large,
reducing 
$
v_i
$
 when 
$
\nu^\ast_i>0
$
 or increasing 
$
v_i
$
 when 
$
\nu^\ast_i<0
$

increases optimval value a lot

	</li>
	<li>
		if 
$
|\nu^\ast_i|
$
 is small,
increasing 
$
v_i
$
 when 
$
\nu^\ast_i>0
$
 or decreasing 
$
v_i
$
 when 
$
\nu^\ast_i<0
$

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
	assume 
$
p^\ast(u,v)
$
 is differentiable with respect to 
$
u
$
 and 
$
v
$
,
<i>i.e.</i>, 
$
\nabla_{(u,v)} p^\ast(u,v)
$
 exist
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
		obtain same result for 
$
v_i
$
, hence

$$

\nabla_u\; p^\ast (0,0) = -\lambda
\quad
\nabla_v\; p^\ast (0,0) = -\nu

$$


	</li>
	</ul>

</li>
<li>
	so larger 
$
\lambda_i
$
 or 
$
|\nu_i|
$
 means larger change in optimal value of perturbed problem
when 
$
u_i
$
 or 
$
v_i
$
 change a bit and vice versa
quantitatively, - 
$
\lambda_i
$
 an 
$
\nu_i
$
 provide exact ratio and direction

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
			dual Lagrange function is 
$
g = p^\ast
$
,
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

$

L(x,y,\nu) = f(y) + \nu^T(Ax+b-y)

$


		</li>
		<li>
			Lagrange dual function
-

$

g(\nu) = -I(A^T\nu = 0) + b^T\nu - f^\ast(\nu)

$


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

where 
$
A_i\in\reals^{K_i\times n}
$

and 
$
\exp(z) := (\exp(z_1),\ldots,\exp(z_k)))\in\reals^n
$

and 
$
\sum z := \sum_{i=1}^k z_i\in\reals
$

for 
$
z\in\reals^k
$

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
and 
$
\log(z) := (\log(z_1),\ldots,\log(z_k)))\in\reals^n
$

for 
$
z\in\pprealk{k}
$



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
	
for 
$
\fie: \xie\to\reals^m
$
 &amp; 
$
\feq: \xeq\to\reals^p
$

where $\xie$ and $\xeq$ are subsets of common set 
$
\xdomain
$
,
which is subset of Banach space,
assuming 
$
\optdomain = \xie \cap \xeq \neq \emptyset
$
,
and

$
\lambda\in\reals^m
$
 &amp; 
$
\nu\in\reals^p
$
,
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

$
p^\ast,\; d^\ast \in \{0,\infty\}
$


</li>
<li>
	now assume <i>first system of \theoremname~\ref{theorem:weak alternatives of two systems}\
is feasible,</i> then 
$
p^\ast = 0
$
, hence
weak duality applies 
$
d^\ast=0
$
,
thus there exist no 
$
\lambda
$
 and 
$
\nu
$
 such that 
$
\lambda\succeq 0
$

and 
$
g(\lambda,\nu) > 0
$

<i>i.e.</i>, <i>second system is infeasible,</i>
since otherwise there exist 
$
\lambda
$
 and 
$
\nu
$

making 
$
g(\lambda,\nu)
$
 arbitrarily large;
if 
$
\tilde{\lambda}\succeq 0
$
 and 
$
\tilde{\nu}
$

satisfy 
$
g({\lambda},{\nu})>0
$
,

$
g(\alpha\tilde{\lambda}, \alpha\tilde{\nu}) = \alpha g(\tilde{\lambda}, \tilde{\nu})
$

goes to 
$
\infty
$
 when 
$
\alpha\to\infty
$


</li>
<li>
	assume <i>second system is feasible,</i>
then

$
g(\lambda,\nu)
$
 can be arbitrarily large
for above reasons,
thus 
$
d^\ast = \infty
$
,
hence weak duality implies 
$
p^\ast = \infty
$
,
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
	
for 
$
\fie: \xie\to\reals^m
$
 &amp; 
$
\feq: \xeq\to\reals^p
$

where $\xie$ and $\xeq$ are subsets of common set 
$
\xdomain
$
,
which is subset of Banach space,
assuming 
$
\optdomain = \xie \cap \xeq \neq \emptyset
$
,
and

$
\lambda\in\reals^m
$
 &amp; 
$
\nu\in\reals^p
$
,
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
	
for convex 
$
\fie: \xie\to\reals^m
$
 &amp; affine 
$
\feq:\xeq\to\reals^p
$

where $\xie$ and $\xeq$ are subsets 
$
\reals^n
$

assuming 
$
\optdomain = \xie \cap \xeq \neq \emptyset
$

and

$
\lambda\in\reals^m
$
 &amp; 
$
\nu\in\reals^p
$
,
if exists 
$
x \in \relint \optdomain
$
 with 
$
\feq(x)=0
$
,
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
	
for convex 
$
\fie: \xie\to\reals^m
$
 &amp; affine 
$
\feq:\xeq\to\reals^p
$

where $\xie$ and $\xeq$ are subsets 
$
\reals^n
$

assuming 
$
\optdomain = \xie \cap \xeq \neq \emptyset
$

and

$
\lambda\in\reals^m
$
 &amp; 
$
\nu\in\reals^p
$
,
if exists 
$
x \in \relint \optdomain
$
 with 
$
\feq(x)=0
$
,
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

$

g(\lambda,\nu)
=
\inf_{x\in\optdomain}
\left(
\lambda^T \fie(x) + \nu^T \feq(x)
\right)

$


	</li>
	</ul>

</li>
<li>
	first observe Slater's condition
holds for primal problem
since by hypothesis of <a href="#theorem:strong---alternatives---of---two---systems---with---strict---inequalities"></a>,
exists 
$
y\in\relint \optdomain
$
 with 
$
\feq(y)=0
$
,
hence 
$
(y,\fie(y))\in\xie\times \reals
$

is primal feasible satisifying Slater's condition

</li>
<li>
	hence Slater's theorem (<a href="#theorem:Slater's---theorem"></a>)
implies

$
d^\ast=p^\ast
$


</li>
<li>
	assume first system
is feasible,
then primal problem is strictly feasible and 
$
d^\ast = p^\ast<0
$
,
hence second system infeasible
since otherwise
feasible point for second system
is feasible point of dual problem,
hence 
$
d^\ast\geq0
$


</li>
<li>
	assume first system
is infeasible,
then 
$
d^\ast = p^\ast\geq0
$
,
hence
Slater's theorem (<a href="#theorem:Slater's---theorem"></a>)
implies exists dual optimal 
$
(\lambda^\ast,\nu^\ast)
$
 (whether or not 
$
d^\ast=\infty
$
),
hence 
$
(\lambda^\ast,\nu^\ast)
$
 is feasible point for second system
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
	dual function of feasibility problem for 
$
Ax\preceq b
$

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
alternative system is 
$
\lambda\succeq0,\;b^T\lambda <0,\; A^T\lambda=0
$


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
alternative system is 
$
\lambda\succeq0,\;b^T\lambda <0,\; A^T\lambda=0
$

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

$
\left(\mbox{minimize}\; c^T x \quad \mbox{subject to}\; Ax \preceq 0\right)
$


</li>
<li>
	dual function is

$

g(y)
=
\inf_{x\in\reals^n} \left(c^Tx + y^TAx \right)
=
\left\{
\begin{array}{ll}
0 & A^Ty + c= 0
\\
-\infty & \mbox{otherwise}
\end{array}
\right.

$


</li>
<li>
	hence dual problem is

$

\left(
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
\right)

$


</li>
<li>
	assume first system is feasible,
then homogeneity of primal problem implies 
$
p^\ast = -\infty
$
,
thus 
$
d^\ast
$
, <i>i.e.</i>, dual is infeasible,
hence second system is infeasible

</li>
<li>
	assume first system is infeasible,
since primal is always feasible,

$
p^\ast=0
$
,
hence strong duality implies 
$
d^\ast =0
$
,
thus second system is feasible

</li>
</ul>


<h2 id="title-page:Convex---Optimization---with---Generalized---Inequalities">Convex Optimization with Generalized Inequalities</h2>



<h3>Optimization problems with generalized inequalities</h3>

<div class="definition" id="definition:optimization---problems---with---generalized---inequalities" data-name="optimization problems with generalized inequalities">
	
for 
$
\fobj:\xobj \to \reals
$
, 
$
\fie: \xie\to \bigtimes_{i=1}^m \reals^{k_i} 
$
, 
$
\feq: \xeq \to \reals^p
$

where $\xobj$, $\xie$, and $\xeq$ are subsets of common set 
$
\xdomain
$


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

$
\bigpropercone = \bigtimes K_i
$
 is proper cone
with

$
m
$
 proper cones

$
K_1\subset \reals^{k_1},\ldots, K_n\subset \reals^{k_m}
$


	<ul>
	<li>
		every terminology and associated notation is same
as of optimization problem in <a href="#definition:optimization---problems"></a>
such as
objective &amp; inequality &amp; equality contraint functions,
domain of optimization problem $\optdomain$,
feasible set $\optfeasset$,
optimal value 
$
p^\ast
$


	</li>
	<li>
		note that
when 
$
K_i=\preals
$
 (hence 
$
\bigpropercone=\prealk{m}
$
),
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
with nonempty domain 
$
\optdomain
$
,
function 
$
L:\optdomain \times \bigtimes_{i=1}^m \reals^{k_i} \times \reals^p \to \reals
$

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
dual variables or Lagrange multipliers 
$
\lambda
$
 and 
$
\nu
$
.

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
function 
$
g:\bigtimes \reals^{k_i} \times \reals^p \to \reals\cup \{-\infty\}
$

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
	
$
g
$
 is <i>concave function</i>

</li>
<li>
	
$
g(\lambda,\nu)
$

is
lower bound for optimal value of associated optimization problem
<i>i.e.</i>,

$$

g(\lambda,\nu) \leq p^\ast

$$

for every 
$
\lambda\succeq_\bigpropercone^\ast0
$

where 
$
\bigpropercone^\ast
$
 denotes dual cone of $\bigpropercone$,
<i>i.e.</i>,

$
\bigpropercone^\ast = \bigtimes K_i^\ast
$

where 
$
K_i^\ast\subset\reals^{k_i}
$
 is dual cone of 
$
K_i\subset\reals^{k_i}
$


</li>
<li>
	
$
(\lambda,\nu)
$

with 
$
\lambda\succeq_\bigpropercone 0
$
 and 
$
g(\lambda,\nu)>-\infty
$

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

where 
$
\bigpropercone^\ast
$
 denotes dual cone of $\bigpropercone$,
<i>i.e.</i>,

$
\bigpropercone^\ast = \bigtimes K_i^\ast
$

where 
$
K_i^\ast\subset\reals^{k_i}
$
 is dual cone of 
$
K_i\subset\reals^{k_i}
$
,
called <span class="define">Lagrange dual problem</span>
associated with problem in <a href="#definition:optimization---problems---with---generalized---inequalities"></a>

	<ul>
	<li>
		every terminology and related notation
is same as that in <a href="#definition:Lagrange---dual---problems"></a>
such as
dual feasibility,
dual optimal value 
$
d^\ast
$
,
optimal Lagrange multipliers 
$
(\lambda^\ast,\nu^\ast)
$


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
since 
$
g(\lambda,\nu)
$
 is convex

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
(<i>i.e.</i>, every 
$
\fie_i
$
 is 
$
K_i
$
-convex)
(<a href="#definition:$K$-convex---functions"></a>),
and exists feasible 
$
x\in\optdomain
$
 contained in 
$
\relint \optdomain
$

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

where 
$
F_1,\ldots,F_n,G\in\symset{k}
$

and 
$
\bigpropercone = \possemidefset{k}
$


</li>
<li>
	Lagrangian
$$
\begin{eqnarray*}

L(x,Z)
&=& c^Tx + (x_1F_1 + \cdots + x_nF_n + G) \bullet Z

\\
&=& \sum x_i(F_i\bullet Z + c_i) + G \bullet Z

\end{eqnarray*}
$$
where 
$
X\bullet Y = \Tr XY
$
 for 
$
X,Y\in\symset{k}
$


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

$
\bigpropercone^\ast = \bigpropercone
$


</li>
<li>
	Slater's theorem (<a href="#theorem:Slater's---theorem---for---generalized---inequalities"></a>)
implies if primal problem is strictly feasible,
<i>i.e.</i>,
exists 
$
x\in\reals^n
$
 such that 
$
\sum x_iF_i + G\prec 0
$
,
strong duality holds

</li>
</ul>

<h3>KKT optimality conditions for generalized inequalities</h3>

<div class="definition" id="definition:KKT---optimality---conditions---for---generalized---inequalities" data-name="KKT optimality conditions for generalized inequalities">
	
for optimization problem in <a href="#definition:optimization---problems---with---generalized---inequalities"></a>
where $\fobj$, $\fie$, and $\feq$ are all differentiable,
below conditions
for 
$
{x}\in\optdomain
$
 and 
$
({\lambda}, {\nu})\in\bigtimes \reals^{k_i} \times\reals^p
$


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

where 
$
u\in\reals^m
$
 and 
$
v\in\reals^p
$


</li>
<li>
	define 
$
p^\ast(u,v) = p^\ast(u,v) = \inf\set{\fobj(x)}{x\in\optdomain, \fie(x) \preceq u, \feq(x) = v}
$
,
which is convex when problem is convex optimization problem
- note

$
p^\ast(0,0)=p^\ast
$


</li>
<li>
	as for normal optimization problem case (page~<a href="#page:Perturbed---optimization---problems">here</a>),
if and dual optimum 
$
(\lambda^\ast,\nu^\ast)
$
,
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

for some 
$
U\in\symset{k}
$

	<ul>
	<li>
		define 
$
p^\ast:\symset{k} \to \reals
$

such that

$
p^\ast(U)
$
 is optimal value of above problem

	</li>
	</ul>

</li>
<li>
	assume 
$
x^\ast\in\reals^n
$
 and 
$
Z^\ast\in\possemidefset{k}
$

are primal and dual optimum with zero dualty gap

</li>
<li>
	then

$$

p^\ast(U) \geq p^\ast - Z^\ast \bullet U

$$


</li>
<li>
	if 
$
\nabla_U p^\ast
$
 exists at 
$
U=0
$


$$

\nabla_U p^\ast(0) = - Z^\ast

$$


</li>
</ul>


<h3>Weak alternatives for generalized inequalities</h3>

<div class="theorem" id="theorem:weak---alternatives---for---generalized---inequalities" data-name="weak alternatives for generalized inequalities">
	
for 
$
\fie:\xie \to \bigtimes \reals^{k_i}
$
 &amp; 
$
\feq:\xeq \to \reals^p
$

where $\xie$ and $\xeq$ are subsets of common Banach space
assuming 
$
\optdomain = \xie \cap \xeq \neq \emptyset
$
,
and 
$
\lambda \in \bigtimes \reals^{k_i}
$
 &amp; 
$
\nu \in \reals^p
$
,
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

where 
$
\bigpropercone = \bigtimes K_i
$
 with proper cones 
$
K_i\subset\reals^{k_i}
$

and function 
$
g:\bigtimes \reals^{k_i} \times \reals^p \to \reals
$
 defined by

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
	
for $\bigpropercone$-convex 
$
\fie:\xie \to \bigtimes \reals^{k_i}
$
 &amp; affine 
$
\feq:\xeq \to \reals^p
$

where $\xie$ and $\xeq$ are subsets of 
$
\reals^n
$

assuming 
$
\optdomain = \xie \cap \xeq \neq \emptyset
$
,
and 
$
\lambda \in \bigtimes \reals^{k_i}
$
 &amp; 
$
\nu \in \reals^p
$
,
if exists 
$
x\in\relint \optdomain
$
 with 
$
\feq(x)=0
$
,
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

where 
$
\bigpropercone = \bigtimes K_i
$
 with proper cones 
$
K_i\subset\reals^{k_i}
$

and function 
$
g:\bigtimes \reals^{k_i} \times \reals^p \to \reals
$
 defined by

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
	for 
$
F_1,\ldots,F_n,G\in\symset{k}
$
, 
$
x\in\reals^n
$
, and 
$
Z\in\symset{k}
$

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
		if 
$
\sum v_i F_i \succeq 0 \Rightarrow \sum v_i F_i = 0
$
,
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
<i>i.e.</i>, 
$
m=p=0
$
 in <a href="#definition:convex---optimization"></a>

$$

\begin{array}{ll}
\mbox{minimize} &
\fobj(x)
\end{array}

$$

where
domain of optimization problem is 
$
\optdomain\ = \xobj \subset \reals^n
$


</li>
<li>
	assume
	<ul>
	<li>
		$\fobj$ is twice-differentiable (hence by definition $\xobj$ is open)

	</li>
	<li>
		optimal solution 
$
x^\ast
$
 exists, <i>i.e.</i>, 
$
p^\ast = \inf_{x\in\optdomain} \fobj(x) = \fobj(x^\ast)
$


	</li>
	</ul>

</li>
<li>
	<a href="#theorem:first-order---condition---for---convexity"></a>
implies

$
x^\ast
$
 is optimal solution
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
find sequence of points 
$
\xseqk{0}, \xseqk{1}, \ldots \in \xobj
$

such that

$

\lim_{k\to\infty} \fobj(\xseqk{k}) = p^\ast

$


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
		sublevel set of 
$
\fobj(\xseqk{0})
$


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
		sublevel set of 
$
\fobj(\xseqk{0})
$

is closed for all 
$
\xseqk{0}\in\xobj
$

if $\fobj$ is closed, <i>i.e.</i>, all its sublevel sets are closed

	</li>
	<li>
		$\fobj$ is closed
if 
$
\xobj = \reals^n
$
 and $\fobj$ is continuous

	</li>
	<li>
		$\fobj$ is closed
if $\fobj$ is continuous,
$\xobj$ is open,
and 
$
\fobj(x) \to \infty
$
 as 
$
x \to \boundary \xobj
$


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

where 
$
P\in\possemidefset{n}
$
 and 
$
q\in\reals^n
$

	<ul>
	<li>
		solution obtained by solving

$$

\nabla \fobj(x^\ast) = P x^\ast + q = 0

$$

		<ul>
		<li>
			if solution exists, 
$
x^\ast = - P^\dagger q
$
 (thus 
$
p^\ast>-\infty
$
)

		</li>
		<li>
			otherwise, problem is unbounded below, <i>i.e.</i>, 
$
p^\ast = -\infty
$


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

for 
$
A\in\reals^{m\times n}
$
 and 
$
b\in\reals^m
$

	<ul>
	<li>
		solution obtained by solving

$$

\nabla \fobj(x^\ast) = \frac{\sum A^T \exp(Ax^\ast+b)}{\sum \exp(Ax^\ast+b)} = 0

$$


	</li>
	<li>
		need to resort to iterative method -
since 
$
\xobj = \reals^n
$
 and $\fobj$ is continuous,
$\fobj$ is closed,
hence
every point in 
$
\reals^n
$
 can be initial point

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

where 
$
\xobj = \set{x\in\reals^n}{b-Ax \succ 0}
$

	<ul>
	<li>
		need to resort to iterative method -
since $\xobj$ is open, $\fobj$ is continuous,
and 
$
\fobj(x) \to \infty
$
 as 
$
x\to\boundary \xobj
$
,
$\fobj$ is closed,
hence
every point in $\xobj$ can be initial point

	</li>
	<li>
		$\fobj$, called <span class="define">logarithmic barrier</span> for inequalities 
$
Ax\preceq b
$


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

where 
$
F:\reals^n\to \symset{k}
$
 is defined by

$$

F(x) = x_1F_1 + \cdots + x_nF_n

$$

where 
$
F_i\in \symset{k}
$

and 
$
\xobj = \set{x\in\reals^n}{F(x)\succ 0}
$

	<ul>
	<li>
		need to resort to iterative method -
since $\xobj$ is open, $\fobj$ is continuous,
and 
$
\fobj(x) \to \infty
$
 as 
$
x\to\boundary \xobj
$
,
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
	function 
$
\fobj
$
 is strongly convex on 
$
S
$


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
	strong convexity implies for every 
$
x,y\in S
$


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
	first equation implies sublevel sets contained in 
$
S
$
 is bounded,
hence continuous function 
$
\nabla^2 \fobj(x)
$
 is also bounded,
<i>i.e.</i>,

$
\left( \exists M >0 \right) \left( \nabla^2 \fobj(x) \preceq M I \right)
$
,
then

$$

\fobj(x) - p^\ast \geq \frac{1}{2M} \|\nabla \fobj(x)\|_2^2

$$


</li>
</ul>


<h3>Iterative methods</h3>

<div class="definition" id="definition:iterative---meethods" data-name="iterative meethods">
	
numerical method generating sequence of points 
$
\xseqk{0}, \xseqk{1}, \ldots \in S\subset \reals^n
$

to make 
$
\fobj(\xseqk{k})
$
 approaches to some desired value from some 
$
f:S\to\reals
$
,
called <span class="define">iterative method</span>

</div>
<div class="definition" id="definition:iterative---meethods---with---search---directions" data-name="iterative meethods with search directions">
	
iterative method generating
search direction 
$
\sdirk{k}\in\reals^n
$
 and
step length 
$
\slenk{k}>0
$
 at each step 
$
k
$

such that

$$

\xseqk{k+1} = \xseqk{k} + \slenk{k} \sdirk{k}

$$

called <span class="define">iterative method with search direction</span>
where $\sdirk{k}$, called <span class="define">search direction</span>,
$\slenk{k}$, called <span class="define">step length</span> (which actually is not length)

</div>
<div class="definition" id="definition:descent---methods" data-name="descent methods">
	
for function 
$
f:S\to\reals
$
,
iterative method reducing function value,
<i>i.e.</i>

$$

\fobj(\xseqk{k+1}) \leq \fobj(\xseqk{k})

$$

for 
$
k=0,1,\ldots
$
,
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
error 
$
\fobj(\xseqk{k})-p^\ast
$
 converges to zero approximately as geometric series

</li>
<li>
	choice of backtracking parameters 
$
\alpha
$
 and 
$
\beta
$

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
	second-order Taylor expansion of 
$
\fobj
$

-
$$
\begin{eqnarray*}

\hat{\fobj}(\sdir) &=&
\fobj(x + \sdir) 
\\
&=& \fobj(x) + \nabla \fobj(x)^T \sdir + \frac{1}{2} \sdir^T \nabla^2 \fobj(x) \sdir

\end{eqnarray*}
$$

</li>
<li>
	minimum of Taylor expansion achieved when
$$
\begin{eqnarray*}

\nabla \hat{\fobj}(\sdir) &=& \nabla \fobj(x) + \nabla^2 \fobj(x) v = 0

\end{eqnarray*}
$$

</li>
<li>
	solution called <span class="define">Newton step</span>

$$

\sdir_\mathrm{nt}(x) = - \nabla^2 \fobj(x)^{-1} \nabla \fobj(x)

$$

assuming 
$
\nabla^2\fobj(x)\succ0
$


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
\begin{eqnarray*}

\lambda(x)
&=&
\sqrt{\sdir_\mathrm{nt}(x)^T \nabla^2 \fobj(x) \sdir_\mathrm{nt}(x)}

\\
&=&
\sqrt{\nabla \fobj(x)^T \nabla^2 \fobj(x)^{-1} \nabla \fobj(x)}

\end{eqnarray*}
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
\[
\sdir_\mathrm{nt}(x) := -\nabla^2 \fobj(x)^{-1} \nabla \fobj(x)
\]
\[
\lambda(x)^2 := \nabla \fobj(x)^T \nabla^2 \fobj(x)^{-1} \nabla \fobj(x)
\]
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
	Lipschitz continuity constant 
$
L
$
 plays critical role
in performance of Newton's method
	<ul>
	<li>
		intuition says
Newton's method
works well for functions
whose quadratic approximations
do not change fast,
<i>i.e.</i>,
when 
$
L
$
 is small

	</li>
	</ul>

</li>
</ul>


<h3>Convergence analysis of Newton's method</h3>

<div class="theorem" id="theorem:convergence---analysis---of---Newton's---method" data-name="convergence analysis of Newton's method">
	
for function 
$
\fobj
$
 satisfying strong convexity, Hessian continuity &amp; Lipschitz continuity
with 
$
m, M, L>0
$
,
exist 
$
0<\eta<m^2/L
$
 and 
$
\gamma > 0
$

such that
for each step 
$
k
$


	<ul>
	<li>
		damped Newton phase
-
if 
$
\|\nabla \fobj(\xseqk{k})\|_2 \geq \eta
$
,

$$

\fobj(\xseqk{k+1}) - \fobj(\xseqk{k}) \leq - \gamma

$$


	</li>
	<li>
		quadratic convergence phase
-
if 
$
\|\nabla \fobj(\xseqk{k})\|_2 < \eta
$
,
backtracking line search selects step length 
$
\slenk{k}=1
$


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

$
\fobj(\xseqk{k})-p^\ast\leq\epsilon
$
 is

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
	
convex function 
$
f:X\to \reals
$

with 
$
X\subset \reals^n
$

such that
for all 
$
x\in X, v\in\reals^n
$
,

$
g(t) = f(x+tv)
$

with 
$
\dom g = \set{t\in\reals}{x+tv\in X}
$

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
	
if convex function 
$
g:X\to\reals
$
 with 
$
X\subset \ppreals
$

satisfies

$$

|g'''(x)| \leq 3 g''(x) / x

$$

function 
$
f
$
 with 
$
\dom f = \set{x\in\ppreals}{g(x)<0}
$

defined by

$$

f(x) = -\log(-g(x)) - \log x

$$

and
function 
$
h
$
 with 
$
\dom h = \set{x\in\ppreals}{g(x)+ax^2+bx + c<0}
$

with 
$
a\geq0
$

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

$
m,M, L > 0
$

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
if 
$
f, g:X\to\reals
$
 are self-concordant functions with 
$
X\subset\reals^n
$
,

$
h:H\to\reals^n
$
 with 
$
H\subset \reals^m
$
 are affine functions,
and 
$
a>0
$


$$

af,
\quad
f+g,
\quad
f\circ h

$$

are self-concordant
where

$
\dom f\circ h = \set{x\in H}{h(x) \in X}
$


</div>

<h3>Self-concordant function examples</h3>

<ul>
<li>
	negative logarithm
-

$
f:\ppreals \to \reals
$
 with

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

$
f:\ppreals \to \reals
$
 with 
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
for 
$
A\in\reals^{m\times n}
$
 and 
$
b\in\reals^m
$


$$

f(x) = - \sum \log(b-Ax)

$$

with 
$
\dom f = \set{x\in\reals^n}{b-Ax \succ 0}
$

is self-concordant
by
<a href="#proposition:self-concordance---preserving---operations"></a>,
<i>i.e.</i>, 
$
f
$
 is affine transformation of sum of self-concordant functions

</li>
<li>
	log-determinant
-

$
f:\posdefset{n}\to\reals
$

with

$$

f(X) = \log\det X^{-1} = - \log\det X

$$

is self-concordant since
for every 
$
X\in \posdefset{n}
$
 and 
$
V\in\symset{n}
$

function 
$
g:\reals\to\reals
$
 defined by 
$
g(t) = - \log\det(X+tV)
$

where 
$
\dom f = \set{t\in\reals}{X+tV\succeq 0}
$

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

$
\lambda_i(X,V)
$
 is 
$
i
$
-th eigenvalue of 
$
X^{-1/2}VX^{1/2}
$

is self-concordant
by
<a href="#proposition:self-concordance---preserving---operations"></a>,
<i>i.e.</i>, 
$
g
$
 is affine transformation of sum of self-concordant functions

</li>
<li>
	log of concave quadratic
-

$
f:X\to\reals
$

with

$$

f(x) = -\log(-x^TPx - q^Tx - r)

$$

where

$
P\in\possemidefset{n}
$

and

$
X=\set{x\in\reals^n}{x^TPx + q^Tx + r<0}
$


</li>
<li>
	function 
$
f:X\to\reals
$

with

$$

f(x) = -\log(-g(x)) - \log x

$$

where 
$
\dom f = \set{x\in\dom g \cap \ppreals}{g(x)<0}
$

and
function 
$
h:H\to\reals
$


$$

h(x) = -\log(-g(x)-ax^2-bx-c) - \log x

$$

where 
$
a\geq0
$
 and 
$
\dom h = \set{x\in\dom g \cap \ppreals}{g(x)+ax^2+bx+c<0}
$

are self-concordant
if 
$
g
$
 is one of below
	<ul>
	<li>
		
$
g(x) = -x^p
$
 for 
$
0<p\leq 1
$


	</li>
	<li>
		
$
g(x) = -\log x
$


	</li>
	<li>
		
$
g(x) = x \log x
$


	</li>
	<li>
		
$
g(x) = x^p
$
 for 
$
-1\leq p\leq 0
$


	</li>
	<li>
		
$
g(x) = (ax+b)^2/x
$
 for 
$
a,b\in\reals
$


	</li>
	</ul>
since above 
$
g
$
 satisfy

$
|g'''(x)| \leq 3 g''(x)/x
$

for every 
$
x\in\dom g
$

(<a href="#proposition:self-concordance---for---logarithms"></a>)

</li>
<li>
	function 
$
f:X\to\reals
$

with 
$
X = \set{(x,y)}{\|x\|_2 < y}\subset \reals^n \times \ppreals
$

defined by

$$

f(x,y) = -\log(y^2-x^Tx)

$$

is self-concordant - can be proved using <a href="#proposition:self-concordance---for---logarithms"></a>

</li>
<li>
	function 
$
f:X\to\reals
$

with 
$
X = \set{(x,y)}{|x|^p < y}\subset \reals \times \ppreals
$

defined by

$$

f(x,y) = -2\log y - \log(y^{2/p}- x^2)

$$

where 
$
p\geq1
$

is self-concordant - can be proved using <a href="#proposition:self-concordance---for---logarithms"></a>

</li>
<li>
	function 
$
f:X\to\reals
$

with 
$
X = \set{(x,y)}{\exp(x) < y}\subset \reals \times \ppreals
$

defined by

$$

f(x,y) = -\log y - \log(\log y - x)

$$

is self-concordant - can be proved using <a href="#proposition:self-concordance---for---logarithms"></a>

</li>
</ul>

<h3>Properties of self-concordant functions</h3>

<div class="definition" id="definition:Newton---decrement" data-name="Newton decrement">
	
for convex function 
$
f:X\to\reals
$
 with 
$
X\subset \reals^n
$
,
function 
$
\lambda:\tilde{X}\to\preals
$

with 
$
\tilde{X} = \set{x\in X}{\nabla^2 \fobj(x) \succ 0}
$

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
	
for strictly convex self-concordant function 
$
f:X\to\reals^n
$
 with 
$
X\subset \reals^n
$
,
Hessian is positive definition everywhere (hence Newton decrement is defined everywhere)
and for every 
$
x\in X
$


$$

p^\ast \geq \fobj(x) - \lambda(x)^2
\quad
\Leftrightarrow
\quad
\fobj(x) - p^\ast \leq \lambda(x)^2

$$

if 
$
\lambda(x) \leq 0.68
$


</div>


<h3>Stopping criteria for self-concordant objective functions</h3>

<ul>
<li>
	recall 
$
\lambda(x)^2
$
 provides <i>approximate</i> optimality certificate,
(page~<a href="#page:Newton---decrement---in---quadratic---approximation">here</a>)
<i>i.e.</i>,
assuming 
$
\fobj
$
 is well approximated by quadratic function around 
$
x
$


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

for 
$
\lambda(x) \leq 0.68
$


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

for 
$
\epsilon \leq 0.68^2
$


</li>
</ul>


<h3>Convergence analysis of Newton's method for self-concordant functions</h3>

<div class="theorem" id="theorem:convergence---analysis---of---Newton's---method---for---self-concordant---functions" data-name="convergence analysis of Newton's method for self-concordant functions">
	
for strictly convex self-concordant function $\fobj$,
exist 
$
0<\eta\leq 1/4
$
 and 
$
\gamma>0
$
 (which depend only on line search parameters)
such that

	<ul>
	<li>
		damped Newton phase
-
if 
$
\lambda(\xseqk{k})>\eta
$


$$

\fobj(\xseqk{k+1}) - \fobj(\xseqk{k}) \leq - \gamma

$$


	</li>
	<li>
		quadratic convergence phase
-
if 
$
\lambda(\xseqk{k})\leq\eta
$

backtracking line search selects step length 
$
\slenk{k}=1
$


$$

2\lambda(\xseqk{k+1})
\leq
\left(2\lambda(\xseqk{k})\right)^2

$$


	</li>
	</ul>
# iterations required to satisfy stopping criterion

$
\fobj(\xseqk{k})-p^\ast\leq\epsilon
$
 is

$$

\left(\fobj(\xseqk{0}) - p^\ast\right)/{\gamma}
+ \log_2 \log_2 (1 / \epsilon)

$$

where 
$
\gamma = \alpha \beta (1-2\alpha)^2 / (20-8\alpha)
$


</div>


<h2 id="title-page:Equality---Constrained---Minimization">Equality Constrained Minimization</h2>


<h3>Equality constrained minimization</h3>

<ul>
<li>
	consider
equality constrained convex optimization problem,
<i>i.e.</i>, 
$
m=0
$
 in <a href="#definition:convex---optimization"></a>

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

$
A\in\reals^{p\times n}
$

and
domain of optimization problem is 
$
\optdomain\ = \xobj \subset \reals^n
$


</li>
<li>
	assume
	<ul>
	<li>
		
$
\rank A = p<n
$
,
<i>i.e.</i>, rows of 
$
A
$
 are linearly independent

	</li>
	<li>
		$\fobj$ is twice-differentiable (hence by definition $\xobj$ is open)

	</li>
	<li>
		optimal solution 
$
x^\ast
$
 exists, <i>i.e.</i>, 
$
p^\ast = \inf_{x\in\optfeasset} \fobj(x) = \fobj(x^\ast)
$

and 
$
Ax^\ast = b
$


	</li>
	</ul>

</li>
</ul>


<h3>Solving KKT for equality constrained minimization</h3>

<ul>
<li>
	<a href="#theorem:KKT---and---convexity---sufficient---for---optimality---with---strong---duality"></a>
implies

$
x^\ast\in\xobj
$
 is optimal solution if and only if
exists 
$
\nu^\ast\in\reals^p
$

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

where 
$
P\in\possemidefset{n}
$
 and 
$
A\in\reals^{p\times n}
$


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
}_{\mbox{KKT matrix}}
\colvectwo{x^\ast}{\nu^\ast}
=
\colvectwo{-q}{b}

$$


</li>
<li>
	exist primal and dual optimum 
$
(x^\ast,\nu^\ast)
$
 if and only if KKT system has solution;
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

for some 
$
F\in\reals^{n\times(n-p)}
$

where 
$
\range(F) = \nullspace(A)
$


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
	if 
$
z^\ast
$
 is optimal solution, 
$
x^\ast = Fz^\ast + x_0
$


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

\\
&=&
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
if 
$
\nu^\ast
$
 is dual optimum

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
		initial point, however, should be feasible, <i>i.e.</i>, 
$
\xseqk{0}\in\xobj
$
 and 
$
A\xseqk{0} = b
$


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
\hat{\fobj}(x+\sdir) \\&= \fobj(x) + \nabla \fobj(x)^T \sdir + (1/2) \sdir^T \nabla^2 \fobj(x) \sdir
\\
\mbox{subject to} &
A(x+\sdir) = b
\end{array}

$$

where 
$
x\in\optfeasset
$


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

where 
$
x\in\optfeasset
$


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
since Newton step 
$
\sdir_\mathrm{nt}
$
 is different from that for unconstrained minimization,
<i>i.e.</i>, 
$
\sdir_\mathrm{nt} \neq -\nabla^2 \fobj(x)^{-1} \nabla \fobj(x)
$

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
since all iterates are feasible with 
$
\fobj(\xseqk{k+1}) <\fobj(\xseqk{k})
$


	</li>
	</ul>

</li>
</ul>


<h3>Assumptions for convergence analysis of feasible Newton's method for equality constrained minimization</h3>

<div id="page:conv-analysis-assumptions-feasible-equality-Newton-method"></div>
<ul>
<li>
	feasibility of initial point - 
$
\xseqk{0}\in\dom \fobj \;\&\; A\xseqk{0}=b
$


</li>
<li>
	sublevel set 
$
S = \set{x\in \dom \fobj}{\fobj(x) \leq \fobj(\xseqk{0}),\; Ax=b}
$

is closed

</li>
<li>
	boundedness of Hessian on 
$
S
$


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
	boundedness of KKT matrix on 
$
S
$

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
	Lipschitz continuity of Hessian on 
$
S
$


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
		# iterations required to achieve 
$
\fobj(\xseqk{k})-p^\ast \leq \epsilon
$

is

$$

\left(\fobj(\xseqk{0})-p^\ast\right)/\gamma + \log_2 \log_2 (\epsilon_0/\epsilon)

$$


	</li>
	</ul>

</li>
<li>
	for # iterations required to achieve 
$
\fobj(\xseqk{k})-p^\ast \leq \epsilon
$

for self-concordant functions
is also same as
for unconstrained minimization
(<a href="#theorem:convergence---analysis---of---Newton's---method---for---self-concordant---functions"></a>)

$$

\left(\fobj(\xseqk{0}) - p^\ast\right)/{\gamma}
+ \log_2 \log_2 (1 / \epsilon)

$$

where 
$
\gamma = \alpha \beta (1-2\alpha)^2 / (20-8\alpha)
$


</li>
</ul>


<h3>Newton step at infeasible points</h3>

<ul>
<li>
	only assume that 
$
x\in\dom \fobj
$
 (hence, can be infeasible)

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
	update both primal and dual variables 
$
x
$
 and 
$
\nu
$


</li>
<li>
	define 
$
r:\reals^n\to\reals^p\to\reals^n\times\reals^p
$

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
	linearize 
$
r
$
 to obtain primal-dual Newton step, <i>i.e.</i>

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
	letting 
$
\nu^+= \nu + \pdsdirnu
$
 gives

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

where 
$
y=(x,\nu)
$
 and 
$
\pdsdiry = (\pdsdir, \pdsdirnu)
$


</li>
<li>
	can use 
$
r(\xseqk{k},\nuseqk{k})
$
 to measure optimization progress for infeasible Newton's method

</li>
</ul>


<h3>Full and damped step feasibility property</h3>

<ul>
<li>
	assume step length is 
$
t
$
 at some iteration,
then

$$

r_\mathrm{pri}(x^+,\nu^+) = Ax^+-b
= A(x + t \pdsdir) - b
= (1-t) r_\mathrm{pri}(x,\nu)

$$


</li>
<li>
	hence

$
l>k
$


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
		primal residual reduced by 
$
1-\seqk{t}{k}
$
 at step 
$
k
$


	</li>
	<li>
		Newton step becomes feasible step once full step length (
$
t=1
$
) taken

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
		line search done not on $\fobj$, but on primal-dual residuals 
$
r(x,\nu)
$


	</li>
	<li>
		stopping criteria depends on 
$
r(x,\nu)
$
, not on Newton decrementa 
$
\lambda(x)^2
$


	</li>
	<li>
		primal and dual feasibility checked separately
- here norm in 
$
\|Ax-b\|
$
 can be any norm,
<i>e.g.</i>,

$
\|\cdot\|_0
$
,

$
\|\cdot\|_1
$
,

$
\|\cdot\|_2
$
,

$
\|\cdot\|_\infty
$
,
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
same with $\fobj$ replaced by 
$
\|r(x,\nu)\|_2
$
,

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
	sublevel set 
$
S = \bigset{(x,\nu)\in \dom \fobj\times \reals^m}{
\|r(x,\nu)\|_2
\leq
\|r(\xseqk{0},\nuseqk{0})\|_2
}
$

is closed,
which always holds because 
$
\|r\|_2
$
 is closed

</li>
<li>
	boundedness of KKT matrix on 
$
S
$


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
	Lipschitz continuity of Hessian on 
$
S
$

$$
\begin{eqnarray*}

\left(
\exists L > 0
\right)
&&
\left(
\forall (x,\nu), (y,\mu)\in S
\right)

\\
&&
\left(
\left\|Dr(x,\nu) - Dr(y,\mu)\right\|_2
\leq
L
\|(x,\nu) - (y,\mu)\|_2
\right)

\end{eqnarray*}
$$

</li>
<li>
	above assumptions imply 
$
\set{x\in\dom \fobj}{Ax=b}\neq\emptyset
$

and exist optimal point 
$
(x^\ast,\nu^\ast)
$


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
if 
$
\|r(\xseqk{k},\nuseqk{k})\|_2> 1/(K^2L)
$


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
if 
$
\|r(\xseqk{k},\nuseqk{k})\|_2 \leq 1/(K^2L)
$

$$
\begin{eqnarray*}

\left( K^2L \|r(\xseqk{k},\nuseqk{k})\|_2 / 2 \right)
&\leq&
\left( K^2L \|r(\xseqk{k-1},\nuseqk{k-1})\|_2 / 2 \right)^2

\\
&\leq&
\cdots
\leq (1/2)^{2^k}

\end{eqnarray*}
$$

	</li>
	</ul>

</li>
<li>
	# iterations of infeasible Newton's method required to satisfy 
$
\|r(\xseqk{k},\nuseqk{k})\|_2\leq\epsilon
$


$$

\|r(\xseqk{0},\nuseqk{0})\| /(\alpha \beta / K^2L)
+ \log_2 \log_2 (\epsilon_0/\epsilon) \quad \mbox{where}\; \epsilon_0 = 2/(K^2L)

$$


</li>
<li>
	
$
(\xseqk{k},\nuseqk{k})
$
 converges to 
$
(x^\ast,\nu^\ast)
$


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

where 
$
I_-:\reals\to \reals
$
 is indicator function for nonpositive real numbers, <i>i.e.</i>

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

for 
$
t>0
$
 to obtain

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
	function 
$
\phi
$
 defined by

$$

\phi(x) = - \sum \log(-\fie(x))

$$

with 
$
\dom \phi \set{x\in\xdomain}{\fie(x) \prec 0}
$

called <span class="define">logarithmic barrier</span> or <span class="define">log barrier</span>

</li>
<li>
	solve sequence of log barrier problems as we increase 
$
t
$


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

with 
$
t>0
$

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
	intuition says 
$
x^\ast(t)
$
 will converge to 
$
x^\ast
$

as 
$
t\to\infty
$


</li>
<li>
	KKT conditions imply

$$

Ax^\ast(t) = b \quad \fie(x^\ast(t)) \prec 0

$$

and exists 
$
\nu^\ast(t)
$
 such that

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
	thus if we let 
$
\lambda^\ast(t) = -1/t\fie_i(x^\ast(t))
$
,

$
x^\ast(t)
$
 minimizes

$$

L(x,\lambda^\ast(t),\nu^\ast(t))
= \fobj(x) + {\lambda^\ast(t)}^T \fie(x) + {\nu^\ast(t)}^T (Ax-b)

$$

where 
$
L
$
 is Lagrangian of original problem in <a href="#definition:convex---optimization"></a>

</li>
<li>
	hence, dual function 
$
g(\lambda^\ast(t),\nu^\ast(t))
$
 is finite
and

$$
\begin{eqnarray*}

g(\lambda^\ast(t), \nu^\ast(t))
&=&
\inf_{x\in\xdomain} L(x,\lambda^\ast(t),\nu^\ast(t))
=
L(x^\ast(t),\lambda^\ast(t),\nu^\ast(t))

\\
&
=
&
\fobj(x^\ast(t)) + {\lambda^\ast(t)}^T \fie(x^\ast(t)) + {\nu^\ast(t)}^T (Ax^\ast(t)-b)

\\
&=&
\fobj(x^\ast(t)) - m/t

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
confirms out intuition that 
$
x^\ast(t)\to x^\ast
$
 as 
$
t\to\infty
$


</li>
</ul>


<h3>Central path interpretation via KKT conditions</h3>

<ul>
<li>
	previous arguments imply that 
$
x
$
 is central point,
<i>i.e.</i>, 
$
x=x^\ast(t)
$
 for some 
$
t>0
$

if and only if
exist 
$
\lambda
$
 and 
$
\nu
$
 such that

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
		note that I've just made up term &ldquo;complementary 
$
1/t
$
-slackness''
- you won't be able to find terminology in any literature

	</li>
	</ul>

</li>
<li>
	for large 
$
t
$
, 
$
\lambda^\ast(t)
$
 &amp; 
$
\nu^\ast(t)
$
 <i>very closely</i> satisfy (true) complementary slackness

</li>
</ul>


<h3>Central path interpretation via force field</h3>

<ul>
<li>
	assume exist no equality constraints

</li>
<li>
	interpret 
$
\phi
$
 as potential energy by some force field, <i>e.g.</i>, electrical field
and 
$
t\fobj
$
 as potential energy by some other force field, <i>e.g.</i>, gravity

</li>
<li>
	then
	<ul>
	<li>
		force by first force field (in 
$
n
$
-dimensional space), which we call <i>barrier force</i>, is

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
	
$
x^\ast(t)
$
 is point where two forces exactly balance each other
	<ul>
	<li>
		as 
$
x
$
 approach boundary, barrier force pushes 
$
x
$
 harder from barriers,

	</li>
	<li>
		as 
$
t
$
 increases, objective force pushes 
$
x
$
 harder to point where objective potential energy is minimized

	</li>
	</ul>

</li>
</ul>


<h3>Equality constrained problem using log barrier</h3>

<ul>
<li>
	central point 
$
x^\ast(t)
$
 is 
$
m/t
$
-suboptimal point
guaranteed by optimality certificate 
$
g(\lambda^\ast(t),\nu^\ast(t))
$


</li>
<li>
	hence solving below problem provides solution with 
$
\epsilon
$
-suboptimality

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
since for large 
$
m/\epsilon
$
,
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
		only goal of centering is getting close to 
$
x^\ast
$
,
hence exact calculation of 
$
x^\ast(t)
$
 not critical
as long as approximates of 
$
x^\ast(t)
$
 go to 
$
x^\ast
$


	</li>
	<li>
		while cannot calculate 
$
g(\lambda,\nu)
$
 for this case,
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
	choice of 
$
\mu
$

	<ul>
	<li>
		
$
\mu
$
 determines aggressiveness of 
$
t
$
-update
		<ul>
		<li>
			larger 
$
\mu
$
, less outer iterations, but more inner iterations

		</li>
		<li>
			smaller 
$
\mu
$
, less outer iterations, but more inner iterations

		</li>
		</ul>

	</li>
	<li>
		values from 
$
10
$
 to 
$
20
$
 for 
$
\mu
$

seem to work well

	</li>
	</ul>

</li>
<li>
	candidates for choice of initial 
$
t
$

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
	assuming 
$
t\fobj + \phi
$

can be minimized by Newton's method
for
$\seqk{t}{0}$,

$
\mu\seqk{t}{0}
$
,

$
\mu^2\seqk{t}{0}
$
,
&hellip;

</li>
<li>
	at 
$
k
$
'th step, duality gap achieved is 
$
m/\mu^k\seqk{t}{0}
$


</li>
<li>
	# centering steps required to achieve accuracy of 
$
\epsilon
$
 is

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

$
t\fobj + \phi
$
 should satisfy conditions on page~<a href="#page:conv-analysis-assumptions-feasible-equality-Newton-method">here</a>,
<i>i.e.</i>,
initial sublevel set is closed,
associated inverse KKT matrix is bounded
&amp; Hessian satisfies Lipschitz condition

	</li>
	<li>
		for infeasible centering problem,

$
t\fobj + \phi
$
 should satisfy conditions on page~<a href="#page:conv-analysis-assumptions-infeasible-equality-Newton-method">here</a>

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
	if 
$
x
$
, 
$
\lambda
$
, 
$
\nu
$
 satisfy 
$
r_t(x,\lambda,\nu)=0
$
 (and 
$
\fie(x) \prec 0
$
),
then
	<ul>
	<li>
		
$
x=x^\ast(t)
$
, 
$
\lambda=\lambda^\ast(t)
$
, 
$
\nu=\nu^\ast(t)
$


	</li>
	<li>
		
$
x
$
 is primal feasible and 
$
\lambda
$
 &amp; 
$
\nu
$
 are dual feasible
with duality gap 
$
m/t
$


	</li>
	</ul>

</li>
</ul>


<h3>Primal-dual search direction</h3>

<ul>
<li>
	assume current (primal-dual) point 
$
y=(x,\lambda,\nu)
$

and Newton step 
$
\sdiry =( \sdir, \sdirnu, \sdirlbd)
$


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
<span class="define">primal-dual search direction</span> 
$
\pdsdiry = (\pdsdir, \pdsdirlbd, \pdsdirnu)
$


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
for 
$
\fie(x) \prec 0
$
 and 
$
\lambda\succeq0
$

as

$$

\hat{\eta}(x,\lambda) = - \fie(x)^T \lambda

$$


</li>
<li>
	
$
\hat{\eta}
$
 would be duality gap if 
$
x
$
 were primal feasible and 
$
\lambda
$
 &amp; 
$
\nu
$
 were dual feasible

</li>
<li>
	value 
$
t
$
 corresponding to surrogate duality gap 
$
\hat{\eta}
$
 is 
$
m/\hat{\eta}
$


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

$
\epsilon_\mathrm{pri}
$
, 
$
\epsilon_\mathrm{dual}
$
, &amp; 
$
\epsilon
$

since primal-dual method often shows faster than linear convergence

</li>
</ul>


<h3>Line search for primal-dual interior-point method</h3>

<ul>
<li>
	liner search is standard backtracking line search on 
$
r(x,\lambda,\nu)
$

similar to that in <a href="#algorithm:exact---line---search---for---infeasible---Newton's---method"></a>
except making sure that 
$
\fie(x) \prec 0
$
 and 
$
\lambda\succ0
$


</li>
<li>
	note initial 
$
s
$

in <a href="#algorithm:backtracking---line---search---for---primal-dual---interior-point---method"></a>
is largest 
$
s
$
 that makes 
$
\lambda + s\pdsdirlbd
$
 positive

</li>
</ul>
<div class="algorithm" id="algorithm:backtracking---line---search---for---primal-dual---interior-point---method" data-name="backtracking line search for primal-dual interior-point method">
	 
<ul>
<li>
	<strong>Require:</strong>	\pdsdir, \pdsdirlbd, \pdsdirnu, $\alpha\in(0.01,0.1)$, $\beta\in(0.3,0.8)$ <strong></strong>
</li>

<li>
	<strong></strong>	$s$ $:=$ $0.99\sup\set{s\in[0,1]}{\lambda + s \sdirlbd \succeq 0}$ $=$ $0.99\min\{1,\min\set{-\lambda_i/\sdirlbd_i}{\sdirlbd_i < 0}\}$ <strong></strong>
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


