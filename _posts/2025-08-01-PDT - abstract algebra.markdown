---
title: Abstract Algebra
date: Fri Aug  1 02:00:00 PDT 2025
last_modified_at: Tue Aug  5 00:32:25 PDT 2025
permalink: /math/rig/abstract-algebra
categories:
- blog
tags:
- math
- abstract algebra
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
$
e = ef = f,
$
hence, $e=f$

</div>

<div class="definition" id="definition:monoids" data-name="monoids">
	


set $M$ with composition which is associative and having unit element,
called <span class="define">monoid</span>
(so in particular, $M$ is not empty)
	<ul>
	<li>
		
monoid $M$ with
$
\left(
\forall x, y \in M
\right)
\left(
xy = yx
\right)
$,
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
denoted by <span class="notation">$\aut{G}$</span>

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
with $HK = G$, $H\cap K = \{e\}$, and $ \left( x\in H, y\in K \right) \left( xy=yx \right) $,

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
$
(xH)(yH) = (xy)H,
$
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
$
\bigcap N_\lambda
$
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
$
H \overset{j}{\to}
G \overset{\varphi}{\to}
G/H
$
is exact
where $j$ is inclusion and $\varphi$

</li>
<li>
	$
0 \overset{ }{\to}
G' \overset{f}{\to}
G \overset{g}{\to}
G'' \overset{ }{\to}
0
$
is exact
if and only if
$f$ injective, $g$ surjective, and $\Img f = \Ker g$

</li>
<li>
	if $H=\Ker g$ above,
$
0 \overset{ }{\to}
H \overset{ }{\to}
G \overset{ }{\to}
G/H \overset{ }{\to}
0
$

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
called <span class="define">symmetric group of $S$</span>, denoted by <span class="notation">$\perm{S}$</span>;
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
		$ \left( \forall x,y\in G, s\in S \right) \left( x(ys) = (xy)s \right) $

	</li>
	<li>
		$ \left( \forall s\in S \right) \left( es = s \right) $

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
$
\left(
\exists z\in G
\right)
\left(
x,y \in zG_s
\right)
\Leftrightarrow
xs = ys
$

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
$
|S| \equiv 1\Mod{p}
$

	</li>
	<li>
		if $p$ divides $|S|$,
$
|S| \equiv 0\Mod{p}
$

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
$
\sum_{x\in G} a_x x
$
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
$
(x+\ideal{a})
(y+\ideal{a})
=
xy+\ideal{a},
$
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
$
\left(
\forall x,y \in A
\right)
\left(
xy \in \ideal{p}
\Rightarrow
x \in \ideal{p}
\mbox{ or }
y \in \ideal{p}
\right)
$

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
is <i>field</i> and denoted by <span class="notation">$\primefield{p}$</span>



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
\mbox{ and }
\quad
(fg)' = f'g + fg'
\quad
\mbox{ and }
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
denoted by <span class="notation">$\dimext{E}{F}$</span>

</div>

<div class="proposition" id="proposition:dimension---of---finite---extension" data-name="dimension of finite extension">
	

for field $k$ and its extension fields $F$ and $E$
with $k\subset F\subset E$

$
\dimext{E}{k}
=
\dimext{E}{F}
\dimext{F}{k}
$


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
$
E =
\bigcup_{n\in\naturals}
\bigcup_{\alpha_1, \ldots, \alpha_n \in E}
k(\alpha_1,\ldots,\alpha_n)
$

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
$
0
= f(\alpha)^\tau
= \sum_{i=0}^n (a_i^\tau ) (\alpha^\tau)^i
= \sum_{i=0}^n a_i^\sigma (\alpha^\tau)^i
= f^\sigma(\alpha^\tau)
$

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
frequently denoted by <span class="notation">$\algclosure{k}$</span>

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
denoted by <span class="notation">$\finitefield{p}{n}$</span>,
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
denoted by <span class="notation">$\maxabext{k}$</span>

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


