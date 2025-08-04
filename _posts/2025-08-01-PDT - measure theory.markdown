---
title: Measure Theory
date: Fri Aug  1 03:00:00 PDT 2025
last_modified_at: Mon Aug  4 04:56:10 PDT 2025
permalink: /math/rig/measure-theory
categories:
- blog
tags:
- math
- measure theory
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


<h1 id="super-title-page:Real-Analysis">Real Analysis</h1>



<h2 id="title-page:set-theory">Set Theory</h2>


<h3>Some principles</h3>

<div class="principle" id="principle:principle---of---mathematical---induction" data-name="principle of mathematical induction">
	

$$

P(1) \& [P(n\Rightarrow P(n+1)] \Rightarrow (\forall n \in \naturals)P(n)

$$


</div>

<div class="principle" id="principle:well---ordering---principle" data-name="well ordering principle">
	
each nonempty subset of 
$
\naturals
$
 has a smallest element

</div>

<div class="principle" id="principle:principle---of---recursive---definition" data-name="principle of recursive definition">
	
for 
$
f:X\to X
$
 and 
$
a\in X
$
,
exists unique infinite sequence 
$
\langle x_n\rangle_{n=1}^\infty\subset X
$

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

$
\Leftrightarrow
$

<a href="#principle:well---ordering---principle"></a>

$
\Rightarrow
$

<a href="#principle:principle---of---recursive---definition"></a>

</li>
</ul>

<h3>Some definitions for functions</h3>

<div class="definition" id="definition:functions" data-name="functions">
	
for 
$
f:X\to Y
$

	<ul>
	<li>
		terms, <span class="define">map</span> and <span class="define">function</span>, exterchangeably used



	</li>
	<li>
		
$
X
$
 and 
$
Y
$
, called <span class="define">domain of $f$</span> and <span class="define">codomain of $f$</span> respectively





	</li>
	<li>
		
$
\set{f(x)}{x\in X}
$
, called <span class="define">range of $f$</span>



	</li>
	<li>
		for 
$
Z\subset Y
$
, 
$
f^{-1}(Z) = \set{x\in X}{f(x)\in Z}\subset X
$
, called <span class="define">preimage</span> or <span class="define">inverse image of $Z$ under $f$</span>





	</li>
	<li>
		for 
$
y\in Y
$
, 
$
f^{-1}(\{y\})
$
, called <span class="define">fiber of $f$ over $y$</span>



	</li>
	<li>
		
$
f
$
, called <span class="define">injective</span> or <span class="define">injection</span> or <span class="define">one-to-one</span>
if 
$
\left( \forall x\neq v \in X \right) \left( f(x) \neq f(v) \right)
$








	</li>
	<li>
		
$
f
$
, called <span class="define">surjective</span> or <span class="define">surjection</span> or <span class="define">onto</span>
if 
$
\left( \forall x \in X \right) \left( \exists y in Y \right) (y=f(x))
$








	</li>
	<li>
		
$
f
$
, called <span class="define">bijective</span> or <span class="define">bijection</span> if 
$
f
$
 is both injective and surjective,
in which case, 
$
X
$
 and 
$
Y
$
, said to be <span class="define">one-to-one correspondece</span> or <span class="define">bijective correspondece</span>









	</li>
	<li>
		
$
g:Y\to X
$
, called <span class="define">left inverse</span> if 
$
g\circ f
$
 is identity function



	</li>
	<li>
		
$
h:Y\to X
$
, called <span class="define">right inverse</span> if 
$
f\circ h
$
 is identity function



	</li>
	</ul>

</div>

<h3>Some properties of functions</h3>

<div class="lemma" id="lemma:functions" data-name="functions">
	
for 
$
f:X\to Y
$

	<ul>
	<li>
		
$
f
$
 is injective if and only if 
$
f
$
 has left inverse

	</li>
	<li>
		
$
f
$
 is surjective if and only if 
$
f
$
 has right inverse

	</li>
	<li>
		hence, 
$
f
$
 is bijective if and only if 
$
f
$
 has both left and right inverse
because if 
$
g
$
 and 
$
h
$
 are left and right inverses respectively,

$
g = g \circ (f\circ h) = (g\circ f)\circ h = h
$


	</li>
	<li>
		if 
$
|X|=|Y|<\infty
$
,

$
f
$
 is injective
if and only if

$
f
$
 is surjective
if and only if

$
f
$
 is bijective

	</li>
	</ul>

</div>

<h3>Countability of sets</h3>

<ul>
<li>
	set 
$
A
$
 is countable if range of some function whose domain is 
$
\naturals
$


</li>
<li>
	
$
\naturals
$
, 
$
\integers
$
, 
$
\rationals
$
: countable

</li>
<li>
	
$
\reals
$
: <i>not</i> countable

</li>
</ul>

<h3>Limit sets</h3>

<ul>
<li>
	for sequence, $\seq{A_n}$, of subsets of 
$
X
$

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
	when 
$
\liminf \seq{A_n} = \limsup \seq{A_n}
$
, sequence, $\seq{A_n}$,
said to <span class="define">converge to it</span>, denote



$$

\lim \seq{A_n} = \liminf \seq{A_n} = \limsup \seq{A_n} = A

$$


</li>
</ul>

<h3>Algebras of sets</h3>

<ul>
<li>
	collection 
$
\alg
$
 of subsets of 
$
X
$
 called <span class="define">algebra</span> or <span class="define">Boolean algebra</span> if



$$

(\forall A, B \in \alg) (A\cup B\in\alg)
\mbox{ and }
(\forall A \in \alg) (\compl{A}\in\alg)

$$

	<ul>
	<li>
		
$
(\forall A_1, \ldots, A_n \in \alg)(\cup_{i=1}^n A_i \in \alg)
$


	</li>
	<li>
		
$
(\forall A_1, \ldots, A_n \in \alg)(\cap_{i=1}^n A_i \in \alg)
$


	</li>
	</ul>

</li>
<li>
	algebra 
$
\alg
$
 called <span class="define">$\sigma$-algebra</span> or <span class="define">Borel field</span> if



	<ul>
	<li>
		every union of a countable collection of sets in 
$
\alg
$
 is in 
$
\alg
$
, <i>i.e.</i>,

$$

(\forall \seq{A_i})(\cup_{i=1}^\infty A_i \in \alg)

$$


	</li>
	</ul>

</li>
<li>
	given sequence of sets in algebra 
$
\alg
$
, 
$
\seq{A_i}
$
, exists disjoint sequence, 
$
\seq{B_i}
$
 such that

$$

B_i \subset A_i \mbox{ and }
\bigcup_{i=1}^\infty B_i = \bigcup_{i=1}^\infty A_i

$$


</li>
</ul>

<h3>Algebras generated by subsets</h3>

<ul>
<li>
	<span class="define">algebra generated by</span> collection of subsets of 
$
X
$
, 
$
\coll
$
, can be found by




$$

\alg =
\bigcap \set{\algk{B}}{\algk{B} \in \collF}

$$

where $\collF$ is family of all algebras containing 
$
\coll
$

	<ul>
	<li>
		smallest algebra 
$
\alg
$
 containing 
$
\coll
$
, <i>i.e.</i>,



$$

(\forall \algk{B} \in \collF)(\alg \subset \algk{B})

$$


	</li>
	</ul>

</li>
<li>
	<span class="define">$\sigma$-algebra generated by</span> collection of subsets of 
$
X
$
, 
$
\coll
$
, can be found by



$$

\alg=
\bigcap \set{\algk{B}}{\algk{B} \in \collG}

$$

where 
$
\collG
$
 is family of all 
$
\sigma
$
-algebras containing 
$
\coll
$

	<ul>
	<li>
		smallest 
$
\sigma
$
-algebra 
$
\alg
$
 containing 
$
\coll
$
, <i>i.e.</i>,



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
	
$
x
$
 said to <span class="define">stand in relation</span> 
$
\rel
$
 to 
$
y
$
,
denoted by <span class="notation">$\relxy{x}{y}$</span>

</li>
<li>
	
$
\rel
$
 said to <span class="define">be relation on</span> 
$
X
$
 if 
$
\relxy{x}{y}
$
 
$
\Rightarrow
$
 
$
x\in X
$
 and 
$
y\in X
$



</li>
<li>
	
$
\rel
$
 is
	<ul>
	<li>
		transitive if 
$
\relxy{x}{y}
$
 and 
$
\relxy{y}{z}
$
 
$
\Rightarrow
$
 
$
\relxy{x}{z}
$


	</li>
	<li>
		symmetric if 
$
\relxy{x}{y} = \relxy{y}{x}
$


	</li>
	<li>
		reflexive if 
$
\relxy{x}{x}
$


	</li>
	<li>
		antisymmetric if 
$
\relxy{x}{y}
$
 and 
$
\relxy{y}{x}
$
 
$
\Rightarrow
$
 
$
x=y
$


	</li>
	</ul>

</li>
<li>
	
$
\rel
$
 is
	<ul>
	<li>
		<span class="define">equivalence relation</span> if transitive, symmetric, and reflexive, <i>e.g.</i>, modulo


	</li>
	<li>
		<span class="define">partial ordering</span> if transitive and antisymmetric, <i>e.g.</i>, &ldquo;
$
\subset
$
''



	</li>
	<li>
		<span class="define">linear (or simple) ordering</span> if transitive, antisymmetric, and 
$
\relxy{x}{y}
$
 or 
$
\relxy{y}{x}
$
 for all 
$
x,y\in X
$





		<ul>
		<li>
			<i>e.g.</i>, &ldquo;
$
\geq
$
'' linearly orders 
$
\reals
$
 while &ldquo;
$
\subset
$
'' does not 
$
\powerset(X)
$


		</li>
		</ul>

	</li>
	</ul>

</li>
</ul>

<h3>Ordering</h3>

<ul>
<li>
	given partial order, 
$
\prec
$
, 
$
a
$
 is
	<ul>
	<li>
		a first/smallest/least element if 
$
x \neq a \Rightarrow a\prec x
$


	</li>
	<li>
		a last/largest/greatest element if 
$
x \neq a \Rightarrow x\prec a
$


	</li>
	<li>
		a minimal element if 
$
x \neq a \Rightarrow x \not\prec a
$


	</li>
	<li>
		a maximal element if 
$
x \neq a \Rightarrow a \not\prec x
$


	</li>
	</ul>

</li>
<li>
	partial ordering 
$
\prec
$
 is
	<ul>
	<li>
		strict partial ordering if 
$
x\not\prec x
$


	</li>
	<li>
		reflexive partial ordering if 
$
x\prec x
$


	</li>
	</ul>

</li>
<li>
	strict linear ordering 
$
<
$
 is
	<ul>
	<li>
		<span class="define">well ordering</span> for 
$
X
$
 if every nonempty set contains a first element

	</li>
	</ul>

</li>
</ul>

<h3>Axiom of choice and equivalent principles</h3>

<div class="axiom" id="axiom:axiom---of---choice" data-name="axiom of choice">
	
given a collection of nonempty sets, 
$
\coll
$
,
there exists 
$
f:\coll\ \to \cup_{A\in\coll} A 
$
 such that

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
	

for particial ordering 
$
\prec
$
 on 
$
X
$
,
exists a maximal linearly ordered subset 
$
S\subset X
$
,
<i>i.e.</i>,

$
S
$
 is linearity ordered by 
$
\prec
$

and if 
$
S\subset T\subset X
$
 and 
$
T
$
 is linearly ordered by 
$
\prec
$
,

$
S=T
$


</div>

<div class="principle" id="principle:well-ordering---principle" data-name="well-ordering principle">
	
every set 
$
X
$
 can be well ordered,
<i>i.e.</i>,
there is a relation 
$
<
$
 that well orders 
$
X
$


</div>
<ul>
<li>
	note that
<a href="#axiom:axiom---of---choice"></a>

$
\Leftrightarrow
$

<a href="#principle:Hausdorff---maximal---principle"></a>

$
\Leftrightarrow
$

<a href="#principle:well-ordering---principle"></a>

</li>
</ul>

<h3>Infinite direct product</h3>

<div class="definition" id="definition:direct---product" data-name="direct product">
	
for collection of sets, $\seq{X_\lambda}$, with index set, 
$
\Lambda
$
,

$$

\bigtimes_{\lambda\in\Lambda} X_\lambda

$$

called <span class="define">direct product</span>
	<ul>
	<li>
		
for 
$
z=\seq{x_\lambda}\in\bigtimes X_\lambda
$
,

$
x_\lambda
$
 called <span class="define">$\lambda$-th coordinate of $z$</span>

	</li>
	</ul>

</div>
<ul>
<li>
	if one of 
$
X_\lambda
$
 is empty, 
$
\bigtimes X_\lambda
$
 is empty

</li>
<li>
	<i>axiom of choice</i> is equivalent to converse, <i>i.e.</i>,
if none of 
$
X_\lambda
$
 is empty, 
$
\bigtimes X_\lambda
$
 is not empty
if one of 
$
X_\lambda
$
 is empty, 
$
\bigtimes X_\lambda
$
 is empty

</li>
<li>
	this is why Bertrand Russell prefers <i>multiplicative axiom</i> to <i>axiom of choice</i> for name of axiom (<a href="#axiom:axiom---of---choice"></a>)



</li>
</ul>

<h2 id="title-page:real-number-system">Real Number System</h2>


<h3>Field axioms</h3>

<ul>
<li>
	field axioms - for every 
$
x,y,z\in\field
$

	<ul>
	<li>
		
$
(x+y)+z= x+(y+z)
$
 - additive associativity

	</li>
	<li>
		
$
(\exists 0\in\field)(\forall x\in\field)(x+0=x)
$
 - additive identity

	</li>
	<li>
		
$
(\forall x\in\field)(\exists w\in\field)(x+w=0)
$
 - additive inverse

	</li>
	<li>
		
$
x+y= y+x
$
 - additive commutativity

	</li>
	<li>
		
$
(xy)z= x(yz)
$
 - multiplicative associativity

	</li>
	<li>
		
$
(\exists 1\neq0\in\field)(\forall x\in\field)(x\cdot 1=x)
$
 - multiplicative identity

	</li>
	<li>
		
$
(\forall x\neq0\in\field)(\exists w\in\field)(xw=1)
$
 - multiplicative inverse

	</li>
	<li>
		
$
x(y+z) = xy + xz
$
 - distributivity

	</li>
	<li>
		
$
xy= yx
$
 - multiplicative commutativity

	</li>
	</ul>

</li>
<li>
	system (set with 
$
+
$
 and 
$
\cdot
$
) satisfying axiom of field called <span class="define">field</span>
	<ul>
	<li>
		<i>e.g.</i>, field of module 
$
p
$
 where 
$
p
$
 is prime, $\primefield{p}$

	</li>
	</ul>

</li>
</ul>

<h3>Axioms of order</h3>

<ul>
<li>
	axioms of order - subset, 
$
\field_{++}\subset \field
$
, of positive (real) numbers satisfies
	<ul>
	<li>
		
$
x,y\in \field_{++} \Rightarrow x+y\in \field_{++}
$


	</li>
	<li>
		
$
x,y\in \field_{++} \Rightarrow xy\in \field_{++}
$


	</li>
	<li>
		
$
x\in \field_{++} \Rightarrow -x\not\in \field_{++}
$


	</li>
	<li>
		
$
x\in \field \Rightarrow x=0\lor x\in \field_{++} \lor -x \in \field_{++}
$


	</li>
	</ul>

</li>
<li>
	system satisfying field axioms &amp; axioms of order called <span class="define">ordered field</span>
	<ul>
	<li>
		<i>e.g.</i>, set of real numbers (
$
\reals
$
), set of rational numbers (
$
\rationals
$
)

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
		every nonempty set 
$
S
$
 of real numbers which has an upper bound has a least upper bound,
<i>i.e.</i>,

$$

\set{l}{(\forall x\in S)(l\leq x)}

$$

has least element.

	</li>
	<li>
		use 
$
\inf S
$
 and 
$
\sup S
$
 for least and greatest element (when exist)

	</li>
	</ul>

</li>
<li>
	ordered field that is complete is <span class="define">complete ordered field</span>

	<ul>
	<li>
		<i>e.g.</i>, 
$
\reals
$
 (with 
$
+
$
 and 
$
\cdot
$
)

	</li>
	</ul>

</li>
<li>
	 axiom of Archimedes
	<ul>
	<li>
		given any 
$
x\in\reals
$
, there is an integer 
$
n
$
 such that 
$
x<n
$


	</li>
	</ul>

</li>
<li>
	 corollary
	<ul>
	<li>
		given any 
$
x<y \in \reals
$
, exists 
$
r\in\rationals
$
 such tat

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
	sequence of 
$
\reals
$
 denoted by <span class="notation">$\seq{x_i}_{i=1}^\infty$</span> or <span class="notation">$\seq{x_i}$</span>
	<ul>
	<li>
		mapping from 
$
\naturals
$
 to 
$
\reals
$


	</li>
	</ul>

</li>
<li>
	limit of 
$
\seq{x_n}
$
 denoted by <span class="notation">$\lim_{n\to\infty} x_n$</span> or <span class="notation">$\lim x_n$</span> - defined by 
$
a\in\reals
$

such that

$$

(\forall \epsilon>0)(\exists N\in\naturals) (n \geq N \Rightarrow |x_n-a|<\epsilon)

$$

	<ul>
	<li>
		
$
\lim x_n
$
 unique if exists

	</li>
	</ul>

</li>
<li>
	
$
\seq{x_n}
$
 called Cauchy sequence if

$$

(\forall \epsilon>0)(\exists N\in\naturals) (n,m \geq N \Rightarrow |x_n-x_m|<\epsilon)

$$


</li>
<li>
	Cauchy criterion - characterizing complete metric space (including 
$
\reals
$
)

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
	cluster point of 
$
\seq{x_n}
$
 - defined by 
$
c\in\reals
$


$$

(\forall \epsilon>0, N\in\naturals)(\exists n>N)(|x_n-c|<\epsilon)

$$


</li>
<li>
	limit superior or limsup of 
$
\seq{x_n}
$


$$

\limsup x_n = \inf_n \sup_{k>n} x_k

$$


</li>
<li>
	limit inferior or liminf of 
$
\seq{x_n}
$


$$

\liminf x_n = \sup_n \inf_{k>n} x_k

$$


</li>
<li>
	
$
\liminf x_n \leq \limsup x_n
$


</li>
<li>
	
$
\seq{x_n}
$
 converges if and only if 
$
\liminf x_n = \limsup x_n
$
 (=
$
\lim x_n
$
)

</li>
</ul>

<h3>Open and closed sets</h3>

<ul>
<li>
	
$
O
$
 called <span class="define">open</span> if

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
	
$
\closure{E}
$
 called <span class="define">closure</span> of 
$
E
$
 if

$$

(\forall x \in \closure{E} \ \&\ \delta>0)(\exists y\in E)(|x-y|<\delta)

$$


</li>
<li>
	
$
F
$
 called <span class="define">closed</span> if

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
	(Lindelo&#776;f) any collection $\coll$ of open sets has a countable subcollection 
$
\seq{O_i}
$
 such that

$$

\bigcup_{O\in\coll} O = \bigcup_{i} O_i

$$

	<ul>
	<li>
		equivalently,
any collection $\collk{F}$ of closed sets has a countable subcollection 
$
\seq{F_i}
$
 such that

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
	collection 
$
\coll
$
 of sets called <span class="define">covering</span> of 
$
A
$
 if

$$

A \subset \bigcup_{O\in\coll} O

$$

	<ul>
	<li>
		
$
\coll
$
 said to <span class="define">cover</span> 
$
A
$


	</li>
	<li>
		
$
\coll
$
 called <span class="define">open covering</span> if every 
$
O\in\coll
$
 is open

	</li>
	<li>
		
$
\coll
$
 called <span class="define">finite covering</span> if 
$
\coll
$
 is finite

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
		any collection 
$
\coll
$
 of closed sets including at least one bounded set every finite subcollection of which has nonempty intersection
has nonempty intersection.

	</li>
	</ul>

</li>
</ul>

<h3>Continuous functions</h3>

<ul>
<li>
	
$
f
$
 (with domain 
$
D
$
) called <span class="define">continuous at</span> 
$
x
$
 if

$$

(\forall\epsilon >0)(\exists \delta>0)(\forall y\in D)(|y-x|<\delta \Rightarrow |f(y)-f(x)|<\epsilon)

$$


</li>
<li>
	
$
f
$
 called <span class="define">continuous on</span> 
$
A\subset D
$
 if 
$
f
$
 is continuous at every point in 
$
A
$


</li>
<li>
	
$
f
$
 called <span class="define">uniformly continuous on</span> 
$
A\subset D
$
 if

$$

(\forall\epsilon >0)(\exists \delta>0)(\forall x,y\in D)(|x-y|<\delta \Rightarrow |f(x)-f(y)|<\epsilon)

$$


</li>
</ul>

<h3>Continuous functions - facts</h3>

<ul>
<li>
	
$
f
$
 is continuous if and only if for every open set 
$
O
$
 (in co-domain), 
$
f^{-1}(O)
$
 is open

</li>
<li>
	
$
f
$
 continuous on closed and bounded set is uniformly continuous

</li>
<li>
	<span class="name-font">extreme value theorem -</span>

$
f
$
 continuous on closed and bounded set, 
$
F
$
, is <i>bounded on $F$ and assumes its maximum and minimum on $F$</i>

$$

(\exists x_1, x_2 \in F)(\forall x\in F)(f(x_1) \leq f(x) \leq f(x_2))

$$


</li>
<li>
	<span class="name-font">intermediate value theorem -</span>
for 
$
f
$
 continuous on 
$
[a,b]
$
 with 
$
f(a) \leq f(b)
$
,

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
			 smallest 
$
\sigma
$
-algebra containing all closed sets

		</li>
		<li>
			 smallest 
$
\sigma
$
-algebra containing all open intervals
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
	countable union of closed sets (in 
$
\reals
$
),
called <span class="define">an $F_\sigma$</span> (
$
F
$
 for closed &amp; 
$
\sigma
$
 for sum)

	<ul>
	<li>
		thus, every countable set,
every closed set,
every open interval,
every open sets,
is an 
$
F_\sigma
$
 (note 
$
(a,b)=\bigcup_{n=1}^\infty [a+1/n,b-1/n]
$
)

	</li>
	<li>
		countable union of sets in 
$
F_\sigma
$
 again is an 
$
F_\sigma
$


	</li>
	</ul>

</li>
<li>
	countable intersection of open sets
called <span class="define">a $G_\delta$</span> (
$
G
$
 for open &amp; 
$
\delta
$
 for durchschnitt - average in German)

	<ul>
	<li>
		complement of 
$
F_\sigma
$
 is a 
$
G_\delta
$
 and vice versa

	</li>
	</ul>

</li>
<li>
	
$
F_\sigma
$
 and 
$
G_\delta
$
 are simple types of Borel sets

</li>
<li>
	countable intersection of 
$
F_\sigma
$
's is 
$
F_{\sigma\delta}
$
,
countable union of 
$
F_{\sigma\delta}
$
's is 
$
F_{\sigma\delta\sigma}
$
,
countable intersection of 
$
F_{\sigma\delta\sigma}
$
's is 
$
F_{\sigma\delta\sigma\delta}
$
, <i>etc.</i>,
&amp; likewise for 
$
G_{\delta \sigma \ldots}
$




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
		partition induced by sequence 
$
\seq{x_i}_{i=1}^n
$
 with 
$
a=x_1<\cdots<x_n=b
$


	</li>
	<li>
		lower and upper sums
		<ul>
		<li>
			
$
L(f,\seq{x_i}) = \sum_{i=1}^{n-1} \inf_{x\in[x_i,x_{i+1}]} f(x) (x_{i+1}-x_{i})
$


		</li>
		<li>
			
$
U(f,\seq{x_i}) = \sum_{i=1}^{n-1} \sup_{x\in[x_i,x_{i+1}]} f(x) (x_{i+1}-x_{i})
$


		</li>
		</ul>

	</li>
	<li>
		always holds: 
$
L(f,\seq{x_i}) \leq U(f,\seq{y_i})
$
, hence

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
	consider indicator (or characteristic) function 
$
\chi_\rationals:[0,1] \to [0,1]
$


$$

\chi_\rationals(x) = \left\{\begin{array}{ll}
1 &\mbox{if } x \in \rationals
\\
0 &\mbox{if } x \not\in \rationals
\end{array}\right.

$$


</li>
<li>
	<i>not</i> Riemann integrable: 
$
\sup_{\seq{x_i}} L(f,\seq{x_i}) = 0 \neq 1 = \inf_{\seq{x_i}} U(f,\seq{x_i})
$


</li>
<li>
	however, irrational numbers infinitely more than rational numbers, hence
	<ul>
	<li>
		<i>want to</i> have some integral 
$
\int
$
 such that, <i>e.g.</i>,

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
	want some measure 
$
\mu:\subsetset{M}\to\preals=\set{x\in\reals}{x\geq0}
$

	<ul>
	<li>
		defined for every subset of 
$
\reals
$
, <i>i.e.</i>, 
$
\subsetset{M} = \powerset(\reals)
$


	</li>
	<li>
		equals to length for open interval

$$

\mu[b,a] = b-a

$$


	</li>
	<li>
		countable additivity: for disjoint 
$
\seq{E_i}_{i=1}^\infty
$

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
		indeed, 
$
\chi_\rationals
$
 is Lebesgue integrable

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
	for 
$
E\subset\reals
$
, define outer measure 
$
\mu^\ast:\powerset(\reals)\to\preals
$


$$

\mu^\ast E = \inf_{\seq{I_i}} \left\{\left.\sum l(I_i) \right| E\subset \cup I_i\right\}

$$

where 
$
I_i=(a_i,b_i)
$
 and 
$
l(I_i) = b_i-a_i
$


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
		
$
\mu^\ast E = 0
$
 if 
$
E
$
 is countable

	</li>
	<li>
		
$
[0,1]
$
 not countable

	</li>
	</ul>

</li>
</ul>

<h3>Measurable sets</h3>



<div id="page:measurable-sets"></div>
<ul>
<li>
	
$
E\subset\reals
$
 called measurable if for every 
$
A\subset\reals
$


$$

\mu^\ast A = \mu^\ast (E\cup A) + \mu^\ast (\compl{E}\cup {A})

$$


</li>
<li>
	
$
\mu^\ast E =0
$
, then 
$
E
$
 measurable

</li>
<li>
	every open interval 
$
(a,b)
$
 with 
$
a\geq -\infty
$
 and 
$
b\leq \infty
$
 is measurable

</li>
<li>
	disjoint countable union of measurable sets is measurable, <i>i.e.</i>, 
$
\cup E_i
$
 is measurable

</li>
<li>
	collection of measurable sets is 
$
\sigma
$
-algebra



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
		collection of measurable sets is 
$
\sigma
$
-algebra (page~<a href="#page:measurable-sets">here</a>)

	</li>
	<li>
		every open set is Borel set and Borel sets are 
$
\sigma
$
-algebra (page~<a href="#page:borel-algebra">here</a>)

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
	restriction of 
$
\mu^\ast
$
 in collection 
$
\subsetset{M}
$
 of measurable sets called <span class="define">Lebesgue measure</span>



$$

\mu:\subsetset{M}\to\preals

$$


</li>
<li>
	countable subadditivity - for 
$
\seq{E_n}
$



$$

\mu (\cup E_n) \leq \sum \mu E_n

$$


</li>
<li>
	<span class="define">countable additivity</span> - for disjoint 
$
\seq{E_n}
$



$$

\mu (\cup E_n) = \sum \mu E_n

$$


</li>
<li>
	for dcreasing sequence of measurable sets, $\seq{E_n}$,
<i>i.e.</i>, 
$
(\forall n\in\naturals)(E_{n+1} \subset E_n)
$


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
	if 
$
\mu^\ast E
$
 is finite, above statements are equivalent to

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
	
$
\mu^\ast E_1=0
$
 because 
$
E_1
$
 is countable, hence measurable and

$$

\mu E_1 = \mu^\ast E_1 = 0

$$


</li>
<li>
	algebra implies 
$
E_2 = [0, 1] \cap \compl{E_1}
$
 is measurable

</li>
<li>
	countable additivity implies 
$
\mu E_1 + \mu E_2 = \mu[0,1] = 1
$
, hence

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
	for 
$
f:X\to\reals\cup\{-\infty, \infty\}
$
,
<i>i.e.</i>, extended real-valued function, the followings are equivalent
	<ul>
	<li>
		for every 
$
a\in\reals
$
, 
$
\set{x\in{X}}{f(x) < a}
$
 is measurable

	</li>
	<li>
		for every 
$
a\in\reals
$
, 
$
\set{x\in{X}}{f(x) \leq a}
$
 is measurable

	</li>
	<li>
		for every 
$
a\in\reals
$
, 
$
\set{x\in{X}}{f(x) > a}
$
 is measurable

	</li>
	<li>
		for every 
$
a\in\reals
$
, 
$
\set{x\in{X}}{f(x) \geq a}
$
 is measurable

	</li>
	</ul>

</li>
<li>
	if so,
	<ul>
	<li>
		for every 
$
a\in\reals\cup\{-\infty, \infty\}
$
, 
$
\set{x\in{X}}{f(x) = a}
$
 is measurable

	</li>
	</ul>

</li>
<li>
	extended real-valued function, 
$
f
$
, called <span class="define">(Lebesgue) measurable function</span> if

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
	for real-valued measurable functions, 
$
f
$
 and 
$
g
$
, and 
$
c\in\reals
$

	<ul>
	<li>
		
$
f+c
$
, 
$
cf
$
, 
$
f+g
$
, 
$
fg
$
 are measurable

	</li>
	</ul>

</li>
<li>
	for every extended real-valued measurable function sequence, 
$
\seq{f_n}
$

	<ul>
	<li>
		
$
\sup f_n
$
, 
$
\limsup f_n
$
 are measurable

	</li>
	<li>
		hence, 
$
\inf f_n
$
, 
$
\liminf f_n
$
 are measurable

	</li>
	<li>
		thus, if 
$
\lim f_n
$
 exists, it is measurable

	</li>
	</ul>


</li>
</ul>

<h3>Almost everywhere - a.e.</h3>

<div id="page:almost:everywhere"></div>
<ul>
<li>
	statement, 
$
P(x)
$
, called <span class="define">almost everywhere</span> or <span class="define">a.e.</span> if



$$

\mu \set{x}{\sim P(x)} = 0

$$

	<ul>
	<li>
		<i>e.g.</i>, 
$
f
$
 said to be equal to 
$
g
$
 a.e. if 
$
\mu\set{x}{f(x)\neq g(x)}=0
$


	</li>
	<li>
		<i>e.g.</i>, 
$
\seq{f_n}
$
 said to converge to 
$
f
$
 a.e. if

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
		if 
$
f
$
 is measurable and 
$
f=g
$
 i.e., then 
$
g
$
 is measurable

	</li>
	<li>
		if measurable extended real-valued 
$
f
$
 defined on 
$
[a,b]
$
 with 
$
f(x) \in\reals
$
 a.e.,
then for every 
$
\epsilon>0
$
, exist step function 
$
g
$
 and continuous function 
$
h
$
 such that

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
	for any 
$
A\subset\reals
$
, 
$
\chi_A
$
 called <span class="define">characteristic function</span> if


$$

\chi_A(x) = \left\{\begin{array}{ll}
1 & x\in A\\
0 & x\not\in A\\
\end{array}\right.

$$

	<ul>
	<li>
		
$
\chi_A
$
 is measurable if and only if 
$
A
$
 is measurable

	</li>
	</ul>

</li>
<li>
	measurable 
$
\varphi
$
 called <span class="define">simple</span> if for some distinct 
$
\seq{a_i}_{i=1}^n
$



$$

\varphi(x) = \sum_{i=1}^n a_i \chi_{A_i}(x)

$$

where 
$
A_i = \set{x}{x= a_i}
$



</li>
</ul>

<h3>Littlewood's three principles</h3>



<div id="page:littlewood:three:principles"></div>
<ul>
<li>
	 let 
$
M(E)
$
 with measurable set, 
$
E
$
, denote set of measurable functions defined on 
$
E
$


</li>
<li>
	<span class="fact-font">every (measurable) set is nearly finite union of intervals</span>, <i>e.g.</i>,
	<ul>
	<li>
		
$
E
$
 is measurable if and only if

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

where 
$
a_i
$
 are <i>distinct</i> 
$
A_i=\{x|\varphi(x)=a_i\}
$
 - note 
$
A_i
$
 are <i>disjoint</i>

</li>
<li>
	when 
$
\mu\set{x}{\varphi(x)\neq0}< \infty
$
 and 
$
\varphi = \sum_{i=1}^n a_i \chi_{A_i}
$
 is canonical representation,
define <span class="define">integral of $\varphi$</span> by


$$

\int \varphi = \int \varphi (x) dx= \sum_{i=1}^n a_i \mu A_i

$$


</li>
<li>
	when 
$
E
$
 is measurable, define

$$

\int_E \varphi = \int \varphi \chi_E

$$



</li>
</ul>

<h3>Properties of integral of simple functions</h3>

<ul>
<li>
	for simple functions 
$
\varphi
$
 and 
$
\psi
$

that vanish out of finite measure set,
<i>i.e.</i>,

$
\mu\set{x}{\varphi(x)\neq0}<\infty
$
, 
$
\mu\set{x}{\psi(x)\neq0}<\infty
$
,
and for every 
$
a,b\in\reals
$

<div id="page:linearity---of---Lebesgue---integral---of---simple---functions"></div>

$$

\int (a\varphi + b\psi) = a \int\varphi + b \int\psi

$$



</li>
<li>
	thus, even for simple function, 
$
\varphi = \sum_{i=1}^n a_i \chi_{A_i}
$

that vanishes out of finite measure set,
not necessarily in canonical representation,

$$

\int \varphi = \sum_{i=1}^n a_i \mu A_i

$$


</li>
<li>
	if 
$
\varphi \geq \psi
$
 a.e.

$$

\int \varphi \geq \int \psi

$$


</li>
</ul>

<h3>Lebesgue integral of bounded functions</h3>

<div id="page:Lebesgue---integral---of---bounded---functions"></div>
<ul>
<li>
	for bounded function, 
$
f
$
, and finite measurable set, 
$
E
$
,

$$

\sup_{\varphi:\ \mathrm{simple},\ \varphi \leq f} \int_E \varphi
\leq
\inf_{\psi:\ \mathrm{simple},\ f \leq \psi} \int_E \psi

$$

	<ul>
	<li>
		if 
$
f
$
 is defined on 
$
E
$
, 
$
f
$
 is measurable function if and only if

$$

\sup_{\varphi:\ \mathrm{simple},\ \varphi \leq f} \int_E \varphi
=
\inf_{\psi:\ \mathrm{simple},\ f \leq \psi} \int_E \psi

$$


	</li>
	</ul>

</li>
<li>
	for bounded measurable function, 
$
f
$
, defined on measurable set, 
$
E
$
, with 
$
\mu E < \infty
$
,
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
	for bounded measurable functions, 
$
f
$
 and 
$
g
$
, defined on 
$
E
$
 with finite measure
<div id="page:linearity---of---nonnegative---integral-------Lebesgue"></div>
	<ul>
	<li>
		for every 
$
a,b\in\reals
$


$$

\int_E (af+bg) = a \int_E f + b\int_E g

$$


	</li>
	<li>
		if 
$
f\leq g
$
 a.e.

$$

\int_E f \leq \int_E g

$$


	</li>
	<li>
		for disjoint measurable sets, 
$
A,B\subset E
$
,

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
	if bounded function, 
$
f
$
, defined on 
$
[a,b]
$
 is Riemann integrable,
then 
$
f
$
 is measurable and

$$

\int_{[a,b]} f
=
R \int_a^b f(x) dx

$$

where 
$
R\int
$
 denotes Riemann integral

</li>
<li>
	bounded function, 
$
f
$
, defined on 
$
[a,b]
$
 is Riemann integrable
if and only if set of points where 
$
f
$
 is discontinuous has measure zero

</li>
<li>
	for sequence of measurable functions, 
$
\seq{f_n}
$
, defined on measurable 
$
E
$
 with finite measure, and 
$
M>0
$
,
if 
$
|f_n|<M
$
 for every 
$
n
$
 and 
$
f(x) = \lim f_n(x)
$
 for every 
$
x\in E
$


$$

\int_E f = \lim \int_E f_n

$$


</li>
</ul>

<h3>Lebesgue integral of nonnegative functions</h3>

<div id="page:Lebesgue---integral---of---nonnegative---functions"></div>
<ul>
<li>
	for nonnegative measurable function, 
$
f
$
, defined on measurable set, 
$
E
$
, define

<div id="page:Lebesgue---integral---of---nonnegative---measurable---function"></div>

$$

\int_E f = \sup_{h:\ \mathrm{bounded\ measurable\ function},\ \mu\set{x}{h(x)\neq0}<\infty,\ h\leq f} \int_E h

$$



</li>
<li>
	for nonnegative measurable functions, 
$
f
$
 and 
$
g
$

	<ul>
	<li>
		for every 
$
a,b\geq0
$


$$

\int_E (af + bg) = a\int_E f + b\int_E g

$$


	</li>
	<li>
		if 
$
f\geq g
$
 a.e.

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
		for every 
$
c>0
$


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
for nonnegative measurable function sequence, 
$
\seq{f_n}
$
,
with 
$
\lim f_n = f
$
 a.e. on measurable set, 
$
E
$





$$

\int_E f \leq \liminf \int_E f_n

$$

	<ul>
	<li>
		note 
$
\lim f_n
$
 is measurable (page~<a href="#page:measurable:function:facts">here</a>),
hence 
$
f
$
 is measurable (page~<a href="#page:almost:everywhere">here</a>)

	</li>
	</ul>

</li>
<li>
	<span class="name-font">monotone convergence theorem -</span>
for nonnegative increasing measurable function sequence, 
$
\seq{f_n}
$
,
with 
$
\lim f_n = f
$
 a.e. on measurable set, 
$
E
$



<div id="page:Lebesgue-------monotone---convergence---theorem"></div>

$$

\int_E f = \lim \int_E f_n

$$



</li>
<li>
	for nonnegative measure function, 
$
f
$
, and sequence of disjoint measurable sets, 
$
\seq{E_i}
$
,

$$

\int_{\cup E_i} f = \sum \int_{E_i} f

$$


</li>
</ul>

<h3>Lebesgue integrability of nonnegative functions</h3>

<div id="integrable:nonnegative:function"></div>
<ul>
<li>
	nonnegative measurable function, 
$
f
$
, said to be <span class="define">integrable</span> over measurable set, 
$
E
$
, if



<div id="page:Lebesgue---integrability---of---nonnegative---functions"></div>

$$

\int_E f < \infty

$$



</li>
<li>
	for nonnegative measurable functions, 
$
f
$
 and 
$
g
$
, if 
$
f
$
 is integrable on measurable set, 
$
E
$
,
and 
$
g\leq f
$
 a.e. on 
$
E
$
, then 
$
g
$
 is integrable and

$$

\int_E (f-g) = \int_E f - \int_E g

$$


</li>
<li>
	for nonnegative integrable function, 
$
f
$
, defined on measurable set, 
$
E
$
, and every 
$
\epsilon
$
,
exists 
$
\delta >0
$
 such that for every measurable set 
$
A\subset E
$
 with 
$
\mu A< \epsilon
$

(then 
$
f
$
 is integrable on 
$
A
$
, of course),

$$

\int_A f < \epsilon

$$


</li>
</ul>

<h3>Lebesgue integral</h3>

<ul>
<li>
	for (any) function, 
$
f
$
, define 
$
f^+
$
 and 
$
f^-
$
 such that for every 
$
x
$


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

$
f = f^+ - f^-,\ |f| = f^+ + f^-,\ f^- = (-f)^+
$


</li>
<li>
	measurable function, 
$
f
$
, said to be <span class="define">(Lebesgue) integrable</span> over measurable set, 
$
E
$
,
if (nonnegative measurable) functions, 
$
f^+
$
 and 
$
f^-
$
, are integrable




<div id="page:Lebesgue---integral"></div>

$$

\int_E f = \int_E f^+ - \int_E f^-

$$



</li>
</ul>

<h3>Properties of Lebesgue integral</h3>


<ul>
<li>
	for 
$
f
$
 and 
$
g
$
 integrable on measure set, 
$
E
$
, and 
$
a,b\in\reals
$

<div id="page:properties---of---Lebesgue---integral"></div>
	<ul>
	<li>
		
$
af+bg
$
 is integral and

$$

\int_E (af+bg) = a \int_E f + b\int_E g

$$


	</li>
	<li>
		if 
$
f\geq g
$
 a.e. on 
$
E
$
,

$$

\int_E f \geq \int_E g

$$


	</li>
	<li>
		for disjoint measurable sets, 
$
A,B\subset E
$


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
for measurable 
$
g
$
 integrable on measurable set, 
$
E
$
,
and measurable sequence 
$
\seq{f_n}
$
 converging to 
$
f
$
 with 
$
|f_n|<g
$
 a.e. on 
$
E
$
,
(
$
f
$
 is measurable (page~<a href="#page:measurable:function:facts">here</a>),
every 
$
f_n
$
 is integrable (page~<a href="#integrable:nonnegative:function">here</a>))
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
for sequence of functions, 
$
\seq{g_n}
$
, integrable on measurable set, 
$
E
$
,
converging to integrable 
$
g
$
 a.e. on 
$
E
$
,
and sequence of measurable functions, 
$
\seq{f_n}
$
,
converging to 
$
f
$
 a.e. on 
$
E
$

with 
$
|f_n|<g_n
$
 a.e. on 
$
E
$
,
if

$$

\int_E g = \lim \int_E g_n

$$

then
(
$
f
$
 is measurable (page~<a href="#page:measurable:function:facts">here</a>),
every 
$
f_n
$
 is integrable (page~<a href="#integrable:nonnegative:function">here</a>))
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
		advantage - applicable even when 
$
f
$
 not integrable

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
	
$
\seq{f_n}
$
 of measurable functions said to <span class="define">converge $f$ in measure</span> if

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
exists 
$
\seq{f_n}
$
 converging in measure to 
$
f
$
 that does not converge to 
$
f
$
 a.e.
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
	
for sequence 
$
\seq{f_n}
$
 measurable on 
$
E
$
 with 
$
\mu E<\infty
$


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

