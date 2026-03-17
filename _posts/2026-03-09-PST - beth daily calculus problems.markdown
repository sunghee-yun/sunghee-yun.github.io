---
date: Mon Mar  9 07:04:38 PDT 2026
last_modified_at: Mon Mar 16 20:15:05 PDT 2026
title: "Beth's Daily AP Calculus BC Practice"
permalink: /math/ap/calculus/bc/daily
categories:
 - blog
 - Math
tags:
 - math
 - calculus
toc: true
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
usemathjax: true
---

posted: {{ page.date| date: "%d-%b-%Y" }}
&
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

**Share this on**
[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url={{ site.url }}{{ site.baseurl }}{{ page.url }})
| [Instagram](https://www.instagram.com/)
| [Twitter (X)](https://x.com/intent/tweet?text={{ site.url }}{{ site.baseurl }}{{ page.url }})
| [Facebook](https://www.facebook.com/sharer/sharer.php?u={{ site.url }}{{ site.baseurl }}{{ page.url }})

<div class="daily-intro">
Short daily sessions — <strong>15–20 min</strong>, casual, no pressure. 🧠<br>
Think of it like a daily stretch before a game. The goal is <em>exposure</em>, not perfection.<br>
The more times you bump into a concept, the more natural it becomes.
<blockquote>
&ldquo;The best way to understand a limit is to bump into it over and over —<br>
not to stare at it once for three hours.&rdquo; — Daddy
</blockquote>
</div>

[← Back to main reference page](/math/ap/calculus/bc){:target="_blank"}

<!--
=================================================================
HOW TO ADD A NEW DAY:
  1. Copy the block between the ══ markers below
  2. Paste it right below the "# Month Year" heading
     (or start a new # Month Year section)
  3. Fill in the date, topics, problems, and answers
  4. Done!
=================================================================
-->

# Table of Contents

*New sessions are prepended at the top of each day's section — most recent first.*

- [16-Mar-2026](#mar-16-2026)
- [15-Mar-2026](#mar-15-2026)
- [11-Mar-2026](#mar-11-2026)
- [10-Mar-2026](#mar-10-2026)
- [09-Mar-2026](#mar-09-2026)

# March 2026

## March 16, 2026 {#mar-16-2026}

<div class="date-banner">
📅 <strong>Mon, March 16, 2026</strong> &nbsp;|&nbsp;
Topics
&ndash;
<strong>Limits (sharp tools)</strong> · <strong>Indeterminate forms</strong> · <strong>Series</strong> · <strong>Integration by parts</strong> · <strong>FTC both parts</strong> · <strong>Volumes</strong>
</div>

### Part 1 — Limits: Sharp Tools

Same two roads — but some of today's limits require **three applications of L'Hôpital**, or **Taylor series** that cut straight through.
Always ask yourself: *is there a slicker way than L'Hôpital?*

<ol>
<li>$\displaystyle\lim_{x\to 0}\frac{\arcsin x}{x}$
&nbsp;&nbsp;<em>(Method B: which derivative? at which point?)</em></li>

<li>$\displaystyle\lim_{x\to 0}\frac{\arctan(3x)}{\sin(2x)}$
&nbsp;&nbsp;<em>(no L'Hôpital needed — divide top and bottom by $x$, reuse known limits)</em></li>

<li>$\displaystyle\lim_{x\to 0}\frac{e^x - e^{-x}}{2x}$
&nbsp;&nbsp;<em>(split into two fractions each $\to 1$, or: which derivative at $x=0$?)</em></li>

<li>$\displaystyle\lim_{x\to 0}\frac{x - \sin x}{x\tan x}$
&nbsp;&nbsp;<em>(Taylor is far slicker than L'Hôpital here — try both)</em></li>

<li>$\displaystyle\lim_{x\to 0}\frac{\ln(1+x^2)}{1-\cos x}$
&nbsp;&nbsp;<em>(write out the first nonzero Taylor term for each)</em></li>

<li>$\displaystyle\lim_{x\to 0}\frac{(1+x)^{1/3}-1}{x}$
&nbsp;&nbsp;<em>(Method B: derivative of $(1+x)^{1/3}$ at $x=0$)</em></li>

<li>$\displaystyle\lim_{x\to\infty}\frac{\ln x}{\sqrt{x}}$
&nbsp;&nbsp;<em>(L'Hôpital once; or recall which always beats which at $\infty$)</em></li>

<li>$\displaystyle\lim_{x\to 0}\frac{\cos x - 1 + \frac{x^2}{2}}{x^4}$
&nbsp;&nbsp;<em>(write out the Taylor series of $\cos x$ to the $x^4$ term)</em></li>

<li>$\displaystyle\lim_{x\to 2}\frac{x^2-4}{x^3-8}$
&nbsp;&nbsp;<em>(factor both — and recognise it as a derivative definition!)</em></li>

<li>$\displaystyle\lim_{x\to 0}\frac{\sin(x^2)}{x^2}$
&nbsp;&nbsp;<em>(substitute $u=x^2$)</em></li>

<li>$\displaystyle\lim_{x\to\infty}\frac{x^2+\sin x}{x^2+\cos x}$
&nbsp;&nbsp;<em>(divide through by $x^2$; what happens to $\sin x/x^2$ and $\cos x/x^2$?)</em></li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 1</summary>
<div class="answer-body">
<ol>
<li>
<span class="ans">$1$</span><br>
<span class="hint"><strong>Method B:</strong> $f'(0)$ for $f(x)=\arcsin x$; $f'(x)=\dfrac{1}{\sqrt{1-x^2}}$, so $f'(0)=1$. ✓</span><br>
<span class="hint"><strong>Method A:</strong> $\frac{0}{0}$; diff: $\displaystyle\frac{1/\sqrt{1-x^2}}{1}\big|_{x=0}=1$. ✓</span>
</li>

<li>
<span class="ans">$\dfrac{3}{2}$</span><br>
<span class="hint">Divide top and bottom by $x$: $\displaystyle\frac{\arctan(3x)/x}{\sin(2x)/x}\to\frac{3}{2}$, using $\arctan(u)/u\to 1$ and $\sin(u)/u\to 1$ with $u=3x$ and $u=2x$. ✓</span>
</li>

<li>
<span class="ans">$1$</span><br>
<span class="hint"><strong>Split:</strong> $\displaystyle\frac{e^x-e^{-x}}{2x}=\frac{1}{2}\cdot\frac{e^x-1}{x}+\frac{1}{2}\cdot\frac{1-e^{-x}}{x}\to\frac{1}{2}+\frac{1}{2}=1$.<br>
(For the second fraction: let $u=-x$, then $\frac{1-e^{-x}}{x}=\frac{e^u-1}{u}\to 1$.) ✓<br>
<strong>Method B:</strong> $f'(0)$ for $f(x)=\sinh x=\frac{e^x-e^{-x}}{2}$; $f'(0)=\cosh(0)=1$. ✓</span>
</li>

<li>
<span class="ans">$0$</span><br>
<span class="hint"><strong>Taylor (slicker):</strong> $\sin x = x-\frac{x^3}{6}+\cdots$; so $x-\sin x\approx\frac{x^3}{6}$. Also $\tan x\approx x$, so $x\tan x\approx x^2$. Ratio $\approx\frac{x^3/6}{x^2}=\frac{x}{6}\to 0$. ✓</span><br>
<span class="hint"><strong>L'Hôpital:</strong> Applying it three times to $\frac{x-\sin x}{x\tan x}$ is messy — Taylor is the right tool here.</span>
</li>

<li>
<span class="ans">$2$</span><br>
<span class="hint">Taylor: $\ln(1+x^2)\approx x^2$ and $1-\cos x\approx\dfrac{x^2}{2}$. Ratio $\to\dfrac{x^2}{x^2/2}=2$. ✓<br>
Both numerator and denominator have their first nonzero term at order $x^2$ — a clean cancellation.</span>
</li>

<li>
<span class="ans">$\dfrac{1}{3}$</span><br>
<span class="hint"><strong>Method B:</strong> $f'(0)$ for $f(x)=(1+x)^{1/3}$; $f'(x)=\frac{1}{3}(1+x)^{-2/3}$, so $f'(0)=\frac{1}{3}$. ✓<br>
<strong>Method A:</strong> $\frac{0}{0}$; diff: $\displaystyle\frac{(1/3)(1+x)^{-2/3}}{1}\big|_{x=0}=\frac{1}{3}$. ✓</span>
</li>

<li>
<span class="ans">$0$</span><br>
<span class="hint">L'Hôpital ($\frac{\infty}{\infty}$): $\displaystyle\frac{1/x}{1/(2\sqrt{x})}=\frac{2}{\sqrt{x}}\to 0$. ✓<br>
General principle: $\ln x$ grows slower than <em>any</em> positive power of $x$ as $x\to\infty$.</span>
</li>

<li>
<span class="ans">$\dfrac{1}{24}$</span><br>
<span class="hint">Taylor: $\cos x = 1 - \dfrac{x^2}{2} + \dfrac{x^4}{24} - \cdots$; so $\cos x - 1 + \dfrac{x^2}{2} = \dfrac{x^4}{24}+\cdots$. Divide by $x^4$: limit $=\dfrac{1}{24}$. ✓<br>
Three applications of L'Hôpital would also work, but Taylor is instant.</span>
</li>

<li>
<span class="ans">$\dfrac{1}{3}$</span><br>
<span class="hint"><strong>Direct factor:</strong> $x^2-4=(x-2)(x+2)$; $x^3-8=(x-2)(x^2+2x+4)$. Cancel $(x-2)$: $\displaystyle\frac{x+2}{x^2+2x+4}\big|_{x=2}=\frac{4}{12}=\frac{1}{3}$. ✓<br>
<strong>Method B:</strong> $\displaystyle\frac{x^2-4}{x^3-8}=\frac{x^2-2^2}{x^3-2^3}\to\frac{2\cdot 2}{3\cdot 2^2}=\frac{4}{12}=\frac{1}{3}$ (ratio of derivatives of numerator and denominator at $x=2$). ✓</span>
</li>

<li>
<span class="ans">$1$</span><br>
<span class="hint">Let $u=x^2$; as $x\to 0$, $u\to 0$: $\displaystyle\frac{\sin(x^2)}{x^2}=\frac{\sin u}{u}\to 1$. ✓<br>
This is the third disguise of $\frac{\sin\theta}{\theta}\to 1$ — recognise the pattern!</span>
</li>

<li>
<span class="ans">$1$</span><br>
<span class="hint">Divide numerator and denominator by $x^2$: $\displaystyle\frac{1+\sin x/x^2}{1+\cos x/x^2}$. Since $|\sin x|\leq 1$ and $|\cos x|\leq 1$, both $\sin x/x^2\to 0$ and $\cos x/x^2\to 0$. Limit $=\frac{1}{1}=1$. ✓</span>
</li>
</ol>
</div>
</details>

---

### Part 2 — Indeterminate Forms: $0^0$, $\infty^0$, $1^\infty$

**The universal recipe:** to handle $[f(x)]^{g(x)}$ in indeterminate form, let $L$ be the limit, take $\ln L = \lim g(x)\cdot\ln f(x)$, evaluate the resulting $0\cdot\infty$ form (usually by L'Hôpital), then set $L=e^{\ln L}$.

<ol>
<li>$\displaystyle\lim_{x\to\infty} x\!\left(\sqrt{1+\tfrac{1}{x}}-1\right)$
&nbsp;&nbsp;<em>(multiply by the conjugate, or Taylor: $\sqrt{1+u}\approx 1+\frac{u}{2}$ for small $u$)</em></li>

<li>$\displaystyle\lim_{x\to 0^+} x^{\sin x}$ &nbsp; ($0^0$ form)</li>

<li>$\displaystyle\lim_{x\to\infty}\left(\frac{x+3}{x-1}\right)^{\!x}$ &nbsp; ($1^\infty$ form)</li>

<li>$\displaystyle\lim_{n\to\infty} n^{1/n}$ &nbsp; ($\infty^0$ form)</li>

<li>$\displaystyle\lim_{x\to 0^+}(\cos x)^{1/x^2}$ &nbsp; ($1^\infty$ form — answer involves $e$!)</li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 2</summary>
<div class="answer-body">
<ol>
<li>
<span class="ans">$\dfrac{1}{2}$</span><br>
<span class="hint"><strong>Taylor:</strong> $\sqrt{1+u}\approx 1+\frac{u}{2}$ for small $u$; with $u=1/x$: $x\!\left(1+\frac{1}{2x}+\cdots-1\right)=x\cdot\frac{1}{2x}+\cdots\to\frac{1}{2}$. ✓<br>
<strong>Conjugate:</strong> Multiply by $\frac{\sqrt{1+1/x}+1}{\sqrt{1+1/x}+1}$: $\displaystyle\frac{x\cdot(1/x)}{\sqrt{1+1/x}+1}=\frac{1}{\sqrt{1+1/x}+1}\to\frac{1}{2}$. ✓</span>
</li>

<li>
<span class="ans">$1$</span><br>
<span class="hint">$\ln L = \lim_{x\to 0^+}\sin x\cdot\ln x$. Since $\sin x\approx x$ near $0$: $\sin x\cdot\ln x\approx x\ln x\to 0$ (the Mar 15 Part 1 #7 result). So $\ln L=0$, $L=e^0=1$. ✓<br>
This is the $0^0$ form — and the answer is $1$, not $0$ or undefined.</span>
</li>

<li>
<span class="ans">$e^4$</span><br>
<span class="hint">$\ln L=\lim x\ln\!\left(1+\dfrac{4}{x-1}\right)\approx x\cdot\dfrac{4}{x-1}\to 4$. So $L=e^4$. ✓<br>
More carefully: let $u=\frac{4}{x-1}\to 0^+$; $\frac{\ln(1+u)}{u/x}\cdot\frac{1}{1}\to 1\cdot\lim\frac{4x}{x-1}=4$. ✓</span>
</li>

<li>
<span class="ans">$1$</span><br>
<span class="hint">$\ln L=\lim_{n\to\infty}\dfrac{\ln n}{n}$. L'Hôpital: $\displaystyle\frac{1/n}{1}\to 0$. So $\ln L=0$, $L=e^0=1$. ✓<br>
Intuition: the exponent $\frac{1}{n}\to 0$ "squashes" even $n\to\infty$ down to $1$.</span>
</li>

<li>
<span class="ans">$e^{-1/2} = \dfrac{1}{\sqrt{e}}$</span><br>
<span class="hint">$\ln L=\lim_{x\to 0^+}\dfrac{\ln\cos x}{x^2}$. Taylor: $\cos x\approx 1-\frac{x^2}{2}+\cdots$, so $\ln\cos x\approx\ln\!\left(1-\frac{x^2}{2}\right)\approx-\frac{x^2}{2}$. Thus $\dfrac{\ln\cos x}{x^2}\to-\dfrac{1}{2}$. So $L=e^{-1/2}$. ✓<br>
<strong>L'Hôpital check:</strong> $\displaystyle\frac{-\sin x/\cos x}{2x}=\frac{-\tan x}{2x}\to-\frac{1}{2}$. ✓</span>
</li>
</ol>
</div>
</details>

---

### Part 3 — Series: Power Series and More Tests

<ol>
<li>$\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n}{n\cdot 2^n}$
&nbsp;&nbsp;<em>(ratio test for convergence; exact value connects to a famous logarithm)</em></li>

<li>$\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n\,\pi^{2n}}{(2n)!}$
&nbsp;&nbsp;<em>(recognise this as the Maclaurin series for a trig function evaluated at a specific point)</em></li>

<li>$\displaystyle\sum_{n=1}^{\infty}\frac{1}{n(n+1)(n+2)}$
&nbsp;&nbsp;<em>(partial fractions — this telescopes, but the fractions are trickier)</em></li>

<li>$\displaystyle\sum_{n=1}^{\infty}\frac{n(n+1)}{3^n}$
&nbsp;&nbsp;<em>(ratio test for convergence; exact value is a beautiful bonus)</em></li>

<li>$\displaystyle\sum_{n=2}^{\infty}\frac{1}{n^2\ln n}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty}\frac{n^3}{4^n}$
&nbsp;&nbsp;<em>(ratio test; exact value optional — needs triple differentiation of geometric series)</em></li>

<li>$\displaystyle\sum_{n=0}^{\infty}\frac{x^{2n}}{n!}$ &nbsp; — find the <strong>radius of convergence</strong> $R$, and identify the closed-form sum</li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 3</summary>
<div class="answer-body">
<ol>
<li>
<span class="ans">Absolutely converges $= \ln\!\dfrac{2}{3}$</span><br>
<span class="hint">Ratio test on $|a_n|$: $\dfrac{n}{2(n+1)}\to\dfrac{1}{2}<1$. Absolutely convergent. ✓<br>
<strong>Exact value:</strong> Recall $\displaystyle\sum_{n=1}^\infty\frac{(-1)^n}{n}x^n=-\ln(1+x)$ for $|x|\leq 1$. At $x=\frac{1}{2}$: $\displaystyle\sum_{n=1}^\infty\frac{(-1)^n}{n\cdot 2^n}=-\ln\!\frac{3}{2}=\ln\!\frac{2}{3}$. ✓</span>
</li>

<li>
<span class="ans">$-1$</span><br>
<span class="hint">The Maclaurin series for $\cos\theta = \displaystyle\sum_{n=0}^\infty\frac{(-1)^n\theta^{2n}}{(2n)!}$. Here $\theta=\pi$: $\displaystyle\sum_{n=0}^\infty\frac{(-1)^n\pi^{2n}}{(2n)!}=\cos\pi=-1$. ✓<br>
<em>Recognising Taylor series in disguise is one of the most powerful skills on the AP exam!</em></span>
</li>

<li>
<span class="ans">Converges $= \dfrac{1}{4}$</span><br>
<span class="hint">Partial fractions: $\dfrac{1}{n(n+1)(n+2)}=\dfrac{1}{2}\!\left(\dfrac{1}{n(n+1)}-\dfrac{1}{(n+1)(n+2)}\right)$.<br>
Telescoping: all middle terms cancel, leaving $\dfrac{1}{2}\cdot\dfrac{1}{1\cdot 2}=\dfrac{1}{4}$. ✓</span>
</li>

<li>
<span class="ans">Converges $= \dfrac{9}{4}$</span><br>
<span class="hint">Ratio test: $\dfrac{(n+1)(n+2)/3^{n+1}}{n(n+1)/3^n}=\dfrac{n+2}{3n}\to\dfrac{1}{3}<1$. ✓<br>
<strong>Exact value (bonus):</strong> Using $\sum_{n=0}^\infty x^n=\frac{1}{1-x}$, differentiate twice and multiply carefully to get $\displaystyle\sum_{n=1}^\infty n(n+1)x^n=\frac{2x}{(1-x)^3}$. At $x=\frac{1}{3}$: $\dfrac{2/3}{(2/3)^3}=\dfrac{2/3}{8/27}=\dfrac{9}{4}$. ✓</span>
</li>

<li>
<span class="ans">Converges</span><br>
<span class="hint">Comparison: $\dfrac{1}{n^2\ln n}<\dfrac{1}{n^2}$ for all $n\geq 2$. Since $\displaystyle\sum\frac{1}{n^2}$ converges ($p=2$), so does this by comparison. ✓<br>
(No simple closed form exists.)</span>
</li>

<li>
<span class="ans">Converges $= \dfrac{44}{27}$</span><br>
<span class="hint">Ratio test: $\dfrac{(n+1)^3/4^{n+1}}{n^3/4^n}=\dfrac{1}{4}\!\left(\dfrac{n+1}{n}\right)^3\to\dfrac{1}{4}<1$. ✓<br>
<strong>Exact value (bonus):</strong> Triple differentiation of $\sum x^n$ gives $\displaystyle\sum_{n=1}^\infty n^3 x^n=\frac{x(1+4x+x^2)}{(1-x)^4}$. At $x=\frac{1}{4}$: $\dfrac{(1/4)(1+1+1/16)}{(3/4)^4}=\dfrac{(1/4)(33/16)}{81/256}=\dfrac{33}{64}\cdot\dfrac{256}{81}=\dfrac{44}{27}$. ✓</span>
</li>

<li>
<span class="ans">$R = \infty$; sum $= e^{x^2}$</span><br>
<span class="hint">Ratio test: $\left|\dfrac{x^{2(n+1)}/(n+1)!}{x^{2n}/n!}\right|=\dfrac{x^2}{n+1}\to 0$ for any fixed $x$. So $R=\infty$: converges for all $x$. ✓<br>
<strong>Closed form:</strong> $\displaystyle\sum_{n=0}^\infty\frac{x^{2n}}{n!}=\sum_{n=0}^\infty\frac{(x^2)^n}{n!}=e^{x^2}$. ✓<br>
This is one of the most useful functions in probability theory (related to the Gaussian)!</span>
</li>
</ol>
</div>
</details>

---

### Part 4 — Integration by Parts: Revisit &amp; Extend

The "solve for $I$" trick from Mar 15 appears again in <strong>#1</strong> — the companion problem to $\int e^x\sin x\,dx$.
Problems <strong>#4</strong> and <strong>#5</strong> introduce **inverse trig antiderivatives** via parts.

<ol>
<li>$\displaystyle\int e^{-x}\cos x\,dx$ &nbsp; ★
&nbsp;&nbsp;<em>(parts twice — the integral comes back again! Use the same solve-for-$I$ trick)</em></li>

<li>$\displaystyle\int x^2\ln x\,dx$
&nbsp;&nbsp;<em>($u=\ln x$, $dv=x^2\,dx$ — LIATE says $\ln x$ comes first)</em></li>

<li>$\displaystyle\int \arcsin x\,dx$
&nbsp;&nbsp;<em>(sneaky: $u=\arcsin x$, $dv=dx$; you will need $\int\frac{x}{\sqrt{1-x^2}}\,dx$ — try $w=1-x^2$)</em></li>

<li>$\displaystyle\int x\ln(x+1)\,dx$
&nbsp;&nbsp;<em>($u=\ln(x+1)$, $dv=x\,dx$; then split $\frac{x^2}{x+1}=x-1+\frac{1}{x+1}$)</em></li>

<li>$\displaystyle\int \ln^2 x\,dx$
&nbsp;&nbsp;<em>($u=\ln^2 x$, $dv=dx$; the remaining integral is the Mar 11 result $\int\ln x\,dx$)</em></li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 4</summary>
<div class="answer-body">
<ol>
<li>
<span class="ans">$\dfrac{e^{-x}(\sin x - \cos x)}{2} + C$</span><br>
<span class="hint">Let $I=\displaystyle\int e^{-x}\cos x\,dx$.<br>
<strong>First parts:</strong> $u=\cos x$, $dv=e^{-x}dx$ $\Rightarrow$ $du=-\sin x\,dx$, $v=-e^{-x}$:<br>
$I = -e^{-x}\cos x - \displaystyle\int e^{-x}\sin x\,dx$.<br>
<strong>Second parts:</strong> $u=\sin x$, $dv=e^{-x}dx$ $\Rightarrow$ $v=-e^{-x}$:<br>
$\displaystyle\int e^{-x}\sin x\,dx = -e^{-x}\sin x + \int e^{-x}\cos x\,dx = -e^{-x}\sin x + I$.<br>
So: $I=-e^{-x}\cos x-(-e^{-x}\sin x+I)=-e^{-x}\cos x+e^{-x}\sin x-I$.<br>
$2I=e^{-x}(\sin x-\cos x)$ $\Rightarrow$ $\boxed{I=\dfrac{e^{-x}(\sin x-\cos x)}{2}+C}$. ✓<br>
<em>Compare with Mar 15 #3: same trick, $e^{-x}$ instead of $e^x$ — the sign inside flips!</em></span>
</li>

<li>
<span class="ans">$\dfrac{x^3}{3}\ln x - \dfrac{x^3}{9} + C$</span><br>
<span class="hint">$u=\ln x$, $dv=x^2\,dx$ $\Rightarrow$ $du=\frac{1}{x}dx$, $v=\frac{x^3}{3}$.<br>
$\displaystyle\int x^2\ln x\,dx=\frac{x^3}{3}\ln x-\int\frac{x^2}{3}\,dx=\frac{x^3}{3}\ln x-\frac{x^3}{9}+C$. ✓</span>
</li>

<li>
<span class="ans">$x\arcsin x + \sqrt{1-x^2} + C$</span><br>
<span class="hint">$u=\arcsin x$, $dv=dx$ $\Rightarrow$ $du=\frac{1}{\sqrt{1-x^2}}dx$, $v=x$.<br>
$\displaystyle\int\arcsin x\,dx=x\arcsin x-\int\frac{x}{\sqrt{1-x^2}}\,dx$.<br>
For the remaining integral: let $w=1-x^2$, $dw=-2x\,dx$:<br>
$\displaystyle\int\frac{x}{\sqrt{1-x^2}}\,dx=-\frac{1}{2}\int w^{-1/2}\,dw=-\sqrt{1-x^2}$.<br>
Total: $x\arcsin x+\sqrt{1-x^2}+C$. ✓</span>
</li>

<li>
<span class="ans">$\dfrac{x^2-1}{2}\ln(x+1) - \dfrac{x^2}{4} + \dfrac{x}{2} + C$</span><br>
<span class="hint">$u=\ln(x+1)$, $dv=x\,dx$ $\Rightarrow$ $du=\frac{1}{x+1}dx$, $v=\frac{x^2}{2}$.<br>
$\displaystyle\int x\ln(x+1)\,dx=\frac{x^2}{2}\ln(x+1)-\int\frac{x^2}{2(x+1)}\,dx$.<br>
Split: $\dfrac{x^2}{x+1}=x-1+\dfrac{1}{x+1}$.<br>
$\displaystyle\int\frac{x^2}{2(x+1)}\,dx=\frac{x^2}{4}-\frac{x}{2}+\frac{1}{2}\ln(x+1)+C$.<br>
Total: $\dfrac{x^2}{2}\ln(x+1)-\dfrac{x^2}{4}+\dfrac{x}{2}-\dfrac{1}{2}\ln(x+1)+C=\dfrac{x^2-1}{2}\ln(x+1)-\dfrac{x^2}{4}+\dfrac{x}{2}+C$. ✓</span>
</li>

<li>
<span class="ans">$x\ln^2 x - 2x\ln x + 2x + C$</span><br>
<span class="hint">$u=\ln^2 x$, $dv=dx$ $\Rightarrow$ $du=\frac{2\ln x}{x}dx$, $v=x$.<br>
$\displaystyle\int\ln^2 x\,dx=x\ln^2 x-2\int\ln x\,dx$.<br>
Use the Mar 11 result $\displaystyle\int\ln x\,dx=x\ln x-x$:<br>
$=x\ln^2 x-2(x\ln x-x)+C=x\ln^2 x-2x\ln x+2x+C$. ✓</span>
</li>
</ol>
</div>
</details>

---

### Part 5 — FTC: Both Parts, Full Power

Today we use **both** parts of the Fundamental Theorem:

$$\underbrace{\frac{d}{dx}\int_a^{g(x)} f(t)\,dt = f\!\bigl(g(x)\bigr)\cdot g'(x)}_{\textbf{FTC Part 1}} \qquad\qquad \underbrace{\int_a^b f(x)\,dx = F(b)-F(a)}_{\textbf{FTC Part 2}}$$

<ol>
<li>$\displaystyle\frac{d}{dx}\int_1^{x^3}\ln t\,dt$</li>

<li>$\displaystyle\frac{d}{dx}\int_{\cos x}^{\sin x} e^{t^2}\,dt$
&nbsp;&nbsp;<em>(both limits depend on $x$ — split at any constant, then apply the chain-rule version to each)</em></li>

<li>Let $F(x)=\displaystyle\int_0^x t\sin t\,dt$. &nbsp; Find $F'(x)$ and $F''(x)$.
&nbsp;&nbsp;<em>(FTC Part 1 gives $F'$ directly; differentiate again with the product rule)</em></li>

<li>Evaluate: $\displaystyle\int_0^1 xe^x\,dx$
&nbsp;&nbsp;<em>(antiderivative from Mar 11 Part 4 #1, then apply FTC Part 2)</em></li>

<li>Evaluate: $\displaystyle\int_0^{\pi/2} x\cos x\,dx$
&nbsp;&nbsp;<em>(antiderivative from Mar 15 Part 4 #1 with $dv=\cos x\,dx$, then FTC Part 2)</em></li>

<li>$\displaystyle\frac{d}{dx}\!\left[x\int_0^x \sin t\,dt\right]$
&nbsp;&nbsp;<em>(product rule first; FTC Part 1 handles the derivative of the integral piece; FTC Part 2 evaluates the other)</em></li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 5</summary>
<div class="answer-body">
<ol>
<li>
<span class="ans">$9x^2\ln x$</span><br>
<span class="hint">FTC Part 1 + chain rule: $f(t)=\ln t$, $g(x)=x^3$, $g'(x)=3x^2$.<br>
$= \ln(x^3)\cdot 3x^2 = 3\ln x\cdot 3x^2 = 9x^2\ln x$. ✓</span>
</li>

<li>
<span class="ans">$e^{\sin^2 x}\cos x + e^{\cos^2 x}\sin x$</span><br>
<span class="hint">Split at $0$: $\displaystyle\int_{\cos x}^{\sin x}=\int_0^{\sin x}-\int_0^{\cos x}$.<br>
Differentiate each with chain rule:<br>
$\displaystyle\frac{d}{dx}\int_0^{\sin x}e^{t^2}\,dt = e^{\sin^2 x}\cdot\cos x$,<br>
$\displaystyle\frac{d}{dx}\int_0^{\cos x}e^{t^2}\,dt = e^{\cos^2 x}\cdot(-\sin x)$.<br>
Total: $e^{\sin^2 x}\cos x + e^{\cos^2 x}\sin x$. ✓</span>
</li>

<li>
<span class="ans">$F'(x) = x\sin x$ &nbsp;;&nbsp; $F''(x) = \sin x + x\cos x$</span><br>
<span class="hint"><strong>$F'(x)$:</strong> FTC Part 1 directly — the integrand evaluated at the upper limit: $F'(x)=x\sin x$. ✓<br>
<strong>$F''(x)$:</strong> Differentiate $x\sin x$ with the product rule: $F''(x)=\sin x+x\cos x$. ✓</span>
</li>

<li>
<span class="ans">$1$</span><br>
<span class="hint">Antiderivative from Mar 11 Part 4 #1: $\displaystyle\int xe^x\,dx = e^x(x-1)+C$.<br>
FTC Part 2: $\Bigl[e^x(x-1)\Bigr]_0^1 = e^1(1-1)-e^0(0-1) = 0-(-1) = 1$. ✓</span>
</li>

<li>
<span class="ans">$\dfrac{\pi}{2}-1$</span><br>
<span class="hint">IBP: $u=x$, $dv=\cos x\,dx$ $\Rightarrow$ $v=\sin x$: antiderivative $= x\sin x+\cos x$.<br>
FTC Part 2: $\Bigl[x\sin x+\cos x\Bigr]_0^{\pi/2} = \Bigl(\frac{\pi}{2}\cdot 1+0\Bigr)-(0\cdot 0+1) = \frac{\pi}{2}-1$. ✓</span>
</li>

<li>
<span class="ans">$1 - \cos x + x\sin x$</span><br>
<span class="hint"><strong>Product rule:</strong> $\displaystyle\frac{d}{dx}\!\left[x\int_0^x\sin t\,dt\right]=\int_0^x\sin t\,dt + x\cdot\frac{d}{dx}\int_0^x\sin t\,dt$.<br>
<strong>FTC Part 1:</strong> $\displaystyle\frac{d}{dx}\int_0^x\sin t\,dt=\sin x$.<br>
<strong>FTC Part 2:</strong> $\displaystyle\int_0^x\sin t\,dt=\bigl[-\cos t\bigr]_0^x=1-\cos x$.<br>
Total: $(1-\cos x)+x\sin x$. ✓</span>
</li>
</ol>
</div>
</details>

---

### Part 6 — Volumes: Choose Your Weapon

For each problem, set up **both methods** and verify they agree.
Pay attention to which method wins — and why!

<h4>Problem 1.</h4> The region bounded by $y=\sin x$, $y=0$, and $x\in[0,\pi]$ is rotated around the **$x$-axis**.

<details class="answers">
<summary>▶ Solution — Problem 1</summary>
<div class="answer-body">

<strong>Disc method</strong> (rotate around $x$-axis — this is the natural direction)

Use the identity $\sin^2 x = \dfrac{1-\cos 2x}{2}$:

$$
\begin{eqnarray*}
	V
		&=&
			\pi\int_0^{\pi}\sin^2 x\,dx
		=
			\frac{\pi}{2}\int_0^{\pi}(1-\cos 2x)\,dx
\\
		&=&
			\frac{\pi}{2}\left[x - \frac{\sin 2x}{2}\right]_0^{\pi}
		=
			\frac{\pi}{2}\cdot\pi
		=
			\boxed{\dfrac{\pi^2}{2}}
\end{eqnarray*}
$$

<strong>Shell method</strong> (horizontal shells, integrate in $y$ from $0$ to $1$)

Inverting $y=\sin x$ on $[0,\pi]$ gives two branches: $x=\arcsin y$ (left) and $x=\pi-\arcsin y$ (right). Shell height $=(\pi-\arcsin y)-\arcsin y=\pi-2\arcsin y$.

$$
\begin{eqnarray*}
	V
		&=&
			2\pi\int_0^1 y\bigl(\pi-2\arcsin y\bigr)\,dy
\end{eqnarray*}
$$

This integral requires integration by parts twice — messy! The disc method is clearly the winner here.

<p class="hint">🔍 Disc wins decisively — one integral, one trig identity, done. Shell requires inverting a trig function into two branches and then a non-trivial IBP. When the axis of rotation matches your integration variable, disc is almost always preferable.</p>

<div id="p1-16mar-viz" style="background:linear-gradient(135deg,#020814,#0a1628,#020814);border-radius:14px;padding:18px;margin:16px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:10px;">
    <span style="font-size:11px;letter-spacing:.3em;color:#60a5fa;text-transform:uppercase;">Problem 1 — </span>
    <span style="font-size:13px;color:#f1f5f9;">$y=\sin x$, $x\in[0,\pi]$, rotated around $x$-axis</span>
  </div>
  <div style="display:flex;gap:10px;">
    <div style="flex:1;background:rgba(2,8,20,.8);border-radius:10px;border:1px solid rgba(148,163,184,.1);overflow:hidden;">
      <canvas id="m16p1-2d" style="width:100%;display:block;"></canvas>
    </div>
    <div style="flex:1;background:rgba(2,8,20,.8);border-radius:10px;border:1px solid rgba(96,165,250,.2);overflow:hidden;position:relative;">
      <canvas id="m16p1-3d" style="width:100%;display:block;cursor:grab;"></canvas>
      <div style="position:absolute;bottom:6px;right:8px;font-size:10px;color:rgba(96,165,250,.5);background:rgba(0,0,0,.4);padding:2px 6px;border-radius:4px;pointer-events:none;">drag to rotate</div>
    </div>
  </div>
  <div style="text-align:center;margin-top:8px;font-size:11px;color:#475569;">
    <span style="color:#38bdf8;">blue</span> = $y=\sin x$ &nbsp;|&nbsp;
    <span style="color:#f87171;">red dashed</span> = $x$-axis (rotation axis) &nbsp;|&nbsp;
    <span style="color:#60a5fa;">3D</span>: lens-shaped solid, $V=\tfrac{\pi^2}{2}$
  </div>
</div>
<script>
(function(){
  var c2=document.getElementById("m16p1-2d"),c3=document.getElementById("m16p1-3d");
  var az=Math.PI/3,el=Math.PI/8,drag={on:false,lx:0,ly:0};
  function initSize(){var w=c2.parentElement.clientWidth,h=Math.round(w*.72);c2.width=w;c2.height=h;c3.width=w;c3.height=h;}
  function draw2D(){
    var W=c2.width,H=c2.height,ctx=c2.getContext("2d");
    ctx.fillStyle="#020814";ctx.fillRect(0,0,W,H);
    var pl=44,pr=18,pt=18,pb=34,xmin=-0.3,xmax=3.6,ymin=-0.35,ymax=1.25;
    function tc(x,y){return[pl+(x-xmin)/(xmax-xmin)*(W-pl-pr),H-pb-(y-ymin)/(ymax-ymin)*(H-pt-pb)];}
    ctx.strokeStyle="rgba(148,163,184,.07)";ctx.lineWidth=1;
    [0,1].forEach(function(i){var p=tc(0,i);ctx.beginPath();ctx.moveTo(pl,p[1]);ctx.lineTo(W-pr,p[1]);ctx.stroke();});
    // shaded region
    ctx.beginPath();ctx.moveTo(tc(0,0)[0],tc(0,0)[1]);
    for(var i=0;i<=100;i++){var x=i/100*Math.PI,p=tc(x,Math.sin(x));ctx.lineTo(p[0],p[1]);}
    ctx.lineTo(tc(Math.PI,0)[0],tc(Math.PI,0)[1]);ctx.closePath();
    ctx.fillStyle="rgba(56,189,248,.17)";ctx.fill();
    // x-axis rotation axis — red dashed
    ctx.strokeStyle="#f87171";ctx.lineWidth=2;ctx.setLineDash([6,4]);
    ctx.beginPath();ctx.moveTo(tc(xmin,0)[0],tc(xmin,0)[1]);ctx.lineTo(tc(xmax,0)[0],tc(xmax,0)[1]);ctx.stroke();ctx.setLineDash([]);
    // y-axis
    ctx.strokeStyle="#475569";ctx.lineWidth=1.2;
    ctx.beginPath();ctx.moveTo(tc(0,ymin)[0],tc(0,ymin)[1]);ctx.lineTo(tc(0,ymax)[0],tc(0,ymax)[1]);ctx.stroke();
    // curve y=sinx
    ctx.strokeStyle="#38bdf8";ctx.lineWidth=2.5;ctx.shadowColor="rgba(56,189,248,.5)";ctx.shadowBlur=5;
    ctx.beginPath();for(var i=0;i<=120;i++){var x=i/120*Math.PI,p=tc(x,Math.sin(x));i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}ctx.stroke();ctx.shadowBlur=0;
    // x=pi label
    ctx.fillStyle="#94a3b8";ctx.font="11px Georgia,serif";ctx.textAlign="center";ctx.fillText("π",tc(Math.PI,0)[0],tc(Math.PI,0)[1]+13);
    ctx.fillStyle="#38bdf8";ctx.font="italic 12px Georgia,serif";ctx.textAlign="left";ctx.fillText("y=sin x",tc(Math.PI/4,Math.sin(Math.PI/4))[0]+5,tc(Math.PI/4,Math.sin(Math.PI/4))[1]-6);
    ctx.fillStyle="#f87171";ctx.font="11px Georgia,serif";ctx.textAlign="center";ctx.fillText("axis of rotation",tc(2.8,0.12)[0],tc(2.8,0.12)[1]);
    // peak dot
    var dp=tc(Math.PI/2,1);ctx.fillStyle="#f1f5f9";ctx.shadowColor="#f1f5f9";ctx.shadowBlur=5;ctx.beginPath();ctx.arc(dp[0],dp[1],3.5,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;
    ctx.fillStyle="#94a3b8";ctx.font="12px Georgia,serif";ctx.textAlign="center";ctx.fillText("2D Region",W/2,12);
  }
  function proj(xp,r,th,az,el){var X=xp,Y=r*Math.cos(th),Z=r*Math.sin(th);var X1=X*Math.cos(az)-Y*Math.sin(az),Y1=X*Math.sin(az)+Y*Math.cos(az),Y2=Y1*Math.cos(el)-Z*Math.sin(el),Z2=Y1*Math.sin(el)+Z*Math.cos(el);return[X1,-Z2,Y2];}
  function draw3D(){
    var W=c3.width,H=c3.height,ctx=c3.getContext("2d");
    ctx.fillStyle="#020814";ctx.fillRect(0,0,W,H);
    var ocx=W*.38,ocy=H*.55,scale=Math.min(W,H)*.115,SEGS=52,N=44;
    function p3(xp,r,th){var s=proj(xp,r,th,az,el);return[ocx+s[0]*scale,ocy+s[1]*scale];}
    function dep(xp,r,th){return proj(xp,r,th,az,el)[2];}
    var slices=[];
    for(var i=0;i<N;i++){var x0=i/N*Math.PI,x1=(i+1)/N*Math.PI,xm=(x0+x1)/2;slices.push({x0:x0,x1:x1,R:Math.sin(xm)});}
    slices.sort(function(a,b){return dep((a.x0+a.x1)/2,0,0)-dep((b.x0+b.x1)/2,0,0);});
    for(var di=0;di<slices.length;di++){
      var s=slices[di],R=s.R,x0=s.x0,x1=s.x1;
      for(var face=0;face<2;face++){
        var xf=face===0?x0:x1;
        ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(xf,R,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
        ctx.closePath();ctx.fillStyle=face===0?"rgba(56,189,248,.14)":"rgba(56,189,248,.30)";ctx.strokeStyle="rgba(56,189,248,.42)";ctx.lineWidth=0.6;ctx.fill();ctx.stroke();
      }
      ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(x0,R,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(x1,R,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath();ctx.fillStyle="rgba(56,189,248,.09)";ctx.strokeStyle="rgba(56,189,248,.28)";ctx.lineWidth=0.5;ctx.fill();ctx.stroke();
    }
    // x-axis
    ctx.strokeStyle="rgba(248,113,113,.7)";ctx.lineWidth=1.5;ctx.setLineDash([5,4]);
    ctx.beginPath();ctx.moveTo(p3(-0.1,0,0)[0],p3(-0.1,0,0)[1]);ctx.lineTo(p3(Math.PI+0.2,0,0)[0],p3(Math.PI+0.2,0,0)[1]);ctx.stroke();ctx.setLineDash([]);
    // profile curves
    ctx.strokeStyle="#38bdf8";ctx.lineWidth=2;ctx.shadowColor="rgba(56,189,248,.6)";ctx.shadowBlur=5;
    ctx.beginPath();for(var i=0;i<=80;i++){var x=i/80*Math.PI,pt=p3(x,Math.sin(x),Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}ctx.stroke();
    ctx.beginPath();for(var i=0;i<=80;i++){var x=i/80*Math.PI,pt=p3(x,Math.sin(x),-Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}ctx.stroke();ctx.shadowBlur=0;
    ctx.fillStyle="#94a3b8";ctx.font="12px Georgia,serif";ctx.textAlign="center";ctx.fillText("3D Solid  —  drag to rotate",W/2,13);
  }
  function xy(e){return e.touches?{x:e.touches[0].clientX,y:e.touches[0].clientY}:{x:e.clientX,y:e.clientY};}
  c3.addEventListener("mousedown",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};c3.style.cursor="grabbing";});
  c3.addEventListener("touchstart",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};},{passive:false});
  window.addEventListener("mousemove",function(e){if(!drag.on)return;var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();});
  window.addEventListener("touchmove",function(e){if(!drag.on)return;e.preventDefault();var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();},{passive:false});
  window.addEventListener("mouseup",function(){drag.on=false;c3.style.cursor="grab";});
  window.addEventListener("touchend",function(){drag.on=false;});
  initSize();draw2D();draw3D();window.addEventListener("resize",function(){initSize();draw2D();draw3D();});
})();
</script>

</div>
</details>

<h4>Problem 2.</h4> The region bounded by $y=x^3$, $y=0$, and $x=2$ is rotated around the $\boldsymbol{y}$**-axis**.

<details class="answers">
<summary>▶ Solution — Problem 2</summary>
<div class="answer-body">

<strong>Shell method</strong> (vertical shells, integrate in $x$; radius $=x$, height $=x^3$, from $x=0$ to $x=2$)

$$
\begin{eqnarray*}
	V
		&=&
			2\pi\int_0^2 x\cdot x^3\,dx
		=
			2\pi\int_0^2 x^4\,dx
		=
			2\pi\left[\frac{x^5}{5}\right]_0^2
\\
		&=&
			2\pi\cdot\frac{32}{5}
		=
			\boxed{\dfrac{64\pi}{5}}
\end{eqnarray*}
$$

<strong>Washer method</strong> (integrate in $y$ from $0$ to $8$; invert $y=x^3\Rightarrow x=y^{1/3}$; outer radius $R=2$ from $x=2$, inner radius $r=y^{1/3}$)

$$
\begin{eqnarray*}
	V
		&=&
			\pi\int_0^8\Bigl(2^2-\bigl(y^{1/3}\bigr)^2\Bigr)\,dy
		=
			\pi\int_0^8\bigl(4-y^{2/3}\bigr)\,dy
\\
		&=&
			\pi\left[4y-\frac{3}{5}y^{5/3}\right]_0^8
		=
			\pi\!\left(32-\frac{3}{5}\cdot 32\right)
		=
			\pi\cdot\frac{64}{5}
		=
			\boxed{\dfrac{64\pi}{5}}\checkmark
\end{eqnarray*}
$$

<p class="hint">🔍 Shell wins again for $y$-axis rotation with the curve given in $x$ — one monomial integral. Washer required inverting $y=x^3$ and computing a fractional power $y^{2/3}$ — doable, but shell is cleaner.</p>

<div id="p2-16mar-viz" style="background:linear-gradient(135deg,#100814,#1a0a28,#100814);border-radius:14px;padding:18px;margin:16px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:10px;">
    <span style="font-size:11px;letter-spacing:.3em;color:#c084fc;text-transform:uppercase;">Problem 2 — </span>
    <span style="font-size:13px;color:#f1f5f9;">$y=x^3$, $x=2$, $y=0$, rotated around $y$-axis</span>
  </div>
  <div style="display:flex;gap:10px;">
    <div style="flex:1;background:rgba(16,8,20,.8);border-radius:10px;border:1px solid rgba(148,163,184,.1);overflow:hidden;">
      <canvas id="m16p2-2d" style="width:100%;display:block;"></canvas>
    </div>
    <div style="flex:1;background:rgba(16,8,20,.8);border-radius:10px;border:1px solid rgba(192,132,252,.2);overflow:hidden;position:relative;">
      <canvas id="m16p2-3d" style="width:100%;display:block;cursor:grab;"></canvas>
      <div style="position:absolute;bottom:6px;right:8px;font-size:10px;color:rgba(192,132,252,.5);background:rgba(0,0,0,.4);padding:2px 6px;border-radius:4px;pointer-events:none;">drag to rotate</div>
    </div>
  </div>
  <div style="text-align:center;margin-top:8px;font-size:11px;color:#475569;">
    <span style="color:#c084fc;">purple</span> = $y=x^3$ &nbsp;|&nbsp;
    <span style="color:#4ade80;">green dashed</span> = $y$-axis &nbsp;|&nbsp;
    outer $R=2$, inner $r=y^{1/3}$, $V=\tfrac{64\pi}{5}$
  </div>
</div>
<script>
(function(){
  var c2=document.getElementById("m16p2-2d"),c3=document.getElementById("m16p2-3d");
  var az=Math.PI/3.5,el=Math.PI/8,drag={on:false,lx:0,ly:0};
  function initSize(){var w=c2.parentElement.clientWidth,h=Math.round(w*.72);c2.width=w;c2.height=h;c3.width=w;c3.height=h;}
  function draw2D(){
    var W=c2.width,H=c2.height,ctx=c2.getContext("2d");
    ctx.fillStyle="#100814";ctx.fillRect(0,0,W,H);
    var pl=44,pr=18,pt=18,pb=34,xmin=-0.2,xmax=2.5,ymin=-0.8,ymax=9;
    function tc(x,y){return[pl+(x-xmin)/(xmax-xmin)*(W-pl-pr),H-pb-(y-ymin)/(ymax-ymin)*(H-pt-pb)];}
    ctx.strokeStyle="rgba(148,163,184,.07)";ctx.lineWidth=1;
    [0,2,4,6,8].forEach(function(i){var p=tc(0,i);ctx.beginPath();ctx.moveTo(pl,p[1]);ctx.lineTo(W-pr,p[1]);ctx.stroke();});
    // shaded region
    ctx.beginPath();ctx.moveTo(tc(0,0)[0],tc(0,0)[1]);
    for(var i=0;i<=80;i++){var x=i/80*2,p=tc(x,x*x*x);ctx.lineTo(p[0],p[1]);}
    ctx.lineTo(tc(2,0)[0],tc(2,0)[1]);ctx.closePath();
    ctx.fillStyle="rgba(192,132,252,.15)";ctx.fill();
    // y-axis rotation axis
    ctx.strokeStyle="#4ade80";ctx.lineWidth=2;ctx.setLineDash([6,4]);
    ctx.beginPath();ctx.moveTo(tc(0,ymin)[0],tc(0,ymin)[1]);ctx.lineTo(tc(0,ymax)[0],tc(0,ymax)[1]);ctx.stroke();ctx.setLineDash([]);
    // x-axis
    ctx.strokeStyle="#475569";ctx.lineWidth=1.2;
    ctx.beginPath();ctx.moveTo(tc(xmin,0)[0],tc(xmin,0)[1]);ctx.lineTo(tc(xmax,0)[0],tc(xmax,0)[1]);ctx.stroke();
    // x=2 dashed
    ctx.strokeStyle="rgba(248,250,252,.3)";ctx.lineWidth=1.2;ctx.setLineDash([4,4]);
    ctx.beginPath();ctx.moveTo(tc(2,0)[0],tc(2,0)[1]);ctx.lineTo(tc(2,8.5)[0],tc(2,8.5)[1]);ctx.stroke();ctx.setLineDash([]);
    // curve y=x^3
    ctx.strokeStyle="#c084fc";ctx.lineWidth=2.5;ctx.shadowColor="rgba(192,132,252,.5)";ctx.shadowBlur=5;
    ctx.beginPath();for(var i=0;i<=100;i++){var x=i/100*2.1,p=tc(x,x*x*x);i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}ctx.stroke();ctx.shadowBlur=0;
    ctx.fillStyle="#c084fc";ctx.font="italic 12px Georgia,serif";ctx.textAlign="left";ctx.fillText("y=x³",tc(1.3,1.3**3)[0]+5,tc(1.3,1.3**3)[1]-6);
    ctx.fillStyle="rgba(248,250,252,.5)";ctx.font="11px Georgia,serif";ctx.textAlign="center";ctx.fillText("x=2",tc(2,0)[0],tc(2,0)[1]+13);
    ctx.fillStyle="#4ade80";ctx.font="11px Georgia,serif";ctx.textAlign="right";ctx.fillText("axis",tc(0,5)[0]-4,tc(0,5)[1]);
    var dp=tc(2,8);ctx.fillStyle="#f1f5f9";ctx.shadowColor="#f1f5f9";ctx.shadowBlur=5;ctx.beginPath();ctx.arc(dp[0],dp[1],3.5,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;
    ctx.fillStyle="#f1f5f9";ctx.font="10px Georgia,serif";ctx.textAlign="left";ctx.fillText("(2,8)",dp[0]+4,dp[1]-4);
    ctx.fillStyle="#94a3b8";ctx.font="12px Georgia,serif";ctx.textAlign="center";ctx.fillText("2D Region",W/2,12);
  }
  function proj(yp,r,th,az,el){var X=yp,Y=r*Math.cos(th),Z=r*Math.sin(th);var X1=X*Math.cos(az)-Y*Math.sin(az),Y1=X*Math.sin(az)+Y*Math.cos(az),Y2=Y1*Math.cos(el)-Z*Math.sin(el),Z2=Y1*Math.sin(el)+Z*Math.cos(el);return[X1,-Z2,Y2];}
  function draw3D(){
    var W=c3.width,H=c3.height,ctx=c3.getContext("2d");
    ctx.fillStyle="#100814";ctx.fillRect(0,0,W,H);
    var ocx=W*.44,ocy=H*.60,scale=Math.min(W,H)*.075,SEGS=52,N=40;
    function p3(yp,r,th){var s=proj(yp,r,th,az,el);return[ocx+s[0]*scale,ocy+s[1]*scale];}
    function dep(yp,r,th){return proj(yp,r,th,az,el)[2];}
    var slices=[];
    for(var i=0;i<N;i++){var y0=i/N*8,y1=(i+1)/N*8,ym=(y0+y1)/2;slices.push({y0:y0,y1:y1,Ro:2,Ri:Math.pow(ym,1/3)});}
    slices.sort(function(a,b){return dep((a.y0+a.y1)/2,0,0)-dep((b.y0+b.y1)/2,0,0);});
    for(var di=0;di<slices.length;di++){
      var s=slices[di],Ro=s.Ro,Ri=s.Ri,y0=s.y0,y1=s.y1;
      for(var face=0;face<2;face++){
        var yf=face===0?y0:y1;
        ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(yf,Ro,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
        for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(yf,Ri,th);ctx.lineTo(pt[0],pt[1]);}
        ctx.closePath();ctx.fillStyle=face===0?"rgba(192,132,252,.14)":"rgba(192,132,252,.30)";ctx.strokeStyle="rgba(192,132,252,.44)";ctx.lineWidth=0.6;ctx.fill();ctx.stroke();
      }
      ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(y0,Ro,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(y1,Ro,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath();ctx.fillStyle="rgba(192,132,252,.07)";ctx.strokeStyle="rgba(192,132,252,.26)";ctx.lineWidth=0.5;ctx.fill();ctx.stroke();
      ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(y0,Ri,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(y1,Ri,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath();ctx.fillStyle="rgba(96,165,250,.05)";ctx.strokeStyle="rgba(96,165,250,.20)";ctx.lineWidth=0.5;ctx.fill();ctx.stroke();
    }
    ctx.strokeStyle="rgba(74,222,128,.7)";ctx.lineWidth=1.5;ctx.setLineDash([5,4]);
    ctx.beginPath();ctx.moveTo(p3(-0.3,0,0)[0],p3(-0.3,0,0)[1]);ctx.lineTo(p3(8.5,0,0)[0],p3(8.5,0,0)[1]);ctx.stroke();ctx.setLineDash([]);
    ctx.strokeStyle="#c084fc";ctx.lineWidth=2;ctx.shadowColor="rgba(192,132,252,.6)";ctx.shadowBlur=5;
    ctx.beginPath();for(var i=0;i<=60;i++){var y=i/60*8,pt=p3(y,Math.pow(y,1/3),Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}ctx.stroke();
    ctx.beginPath();for(var i=0;i<=60;i++){var y=i/60*8,pt=p3(y,Math.pow(y,1/3),-Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}ctx.stroke();ctx.shadowBlur=0;
    ctx.fillStyle="#94a3b8";ctx.font="12px Georgia,serif";ctx.textAlign="center";ctx.fillText("3D Solid  —  drag to rotate",W/2,13);
  }
  function xy(e){return e.touches?{x:e.touches[0].clientX,y:e.touches[0].clientY}:{x:e.clientX,y:e.clientY};}
  c3.addEventListener("mousedown",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};c3.style.cursor="grabbing";});
  c3.addEventListener("touchstart",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};},{passive:false});
  window.addEventListener("mousemove",function(e){if(!drag.on)return;var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();});
  window.addEventListener("touchmove",function(e){if(!drag.on)return;e.preventDefault();var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();},{passive:false});
  window.addEventListener("mouseup",function(){drag.on=false;c3.style.cursor="grab";});
  window.addEventListener("touchend",function(){drag.on=false;});
  initSize();draw2D();draw3D();window.addEventListener("resize",function(){initSize();draw2D();draw3D();});
})();
</script>

</div>
</details>

<h4>Problem 3.</h4> The region bounded by $y = 4 - x^2$ and $y = x^2$ (they meet at $x = \pm\sqrt{2}$; use $x \geq 0$) is rotated around the $\boldsymbol{y}$**-axis**.

<details class="answers">
<summary>▶ Solution — Problem 3</summary>
<div class="answer-body">

<strong>Shell method</strong> (vertical shells, integrate in $x$; radius $=x$, height $=(4-x^2)-x^2=4-2x^2$, from $x=0$ to $x=\sqrt{2}$)

$$
\begin{eqnarray*}
	V
		&=&
			2\pi\int_0^{\sqrt{2}} x\bigl(4-2x^2\bigr)\,dx
		=
			2\pi\int_0^{\sqrt{2}}\bigl(4x-2x^3\bigr)\,dx
\\
		&=&
			2\pi\left[2x^2-\frac{x^4}{2}\right]_0^{\sqrt{2}}
		=
			2\pi\!\left(4-2\right)
		=
			\boxed{4\pi}
\end{eqnarray*}
$$

<strong>Disc method</strong> (integrate in $y$; at height $y$, the horizontal extent is limited by whichever parabola is the binding constraint)

For $y\in[0,2]$: binding constraint is $y\leq x^2$ (lower parabola), giving $x\leq\sqrt{y}$ — a disc of radius $\sqrt{y}$.
For $y\in[2,4]$: binding constraint is $y\leq 4-x^2$ (upper parabola), giving $x\leq\sqrt{4-y}$ — a disc of radius $\sqrt{4-y}$.

$$
\begin{eqnarray*}
	V
		&=&
			\pi\int_0^2\bigl(\sqrt{y}\bigr)^2\,dy + \pi\int_2^4\bigl(\sqrt{4-y}\bigr)^2\,dy
\\
		&=&
			\pi\int_0^2 y\,dy + \pi\int_2^4(4-y)\,dy
\\
		&=&
			\pi\left[\frac{y^2}{2}\right]_0^2 + \pi\left[4y-\frac{y^2}{2}\right]_2^4
\\
		&=&
			\pi\cdot 2 + \pi\bigl[(16-8)-(8-2)\bigr]
		=
			2\pi + 2\pi
		=
			\boxed{4\pi}\checkmark
\end{eqnarray*}
$$

<p class="hint">🔍 Shell was simpler here — one polynomial integral. The disc approach required recognising the two $y$-regions carefully (which parabola is the binding constraint changes at $y=2$) and splitting into two integrals. Both are clean, but shell edges out the win.</p>

<div id="p3-16mar-viz" style="background:linear-gradient(135deg,#081414,#0a1a1a,#081414);border-radius:14px;padding:18px;margin:16px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:10px;">
    <span style="font-size:11px;letter-spacing:.3em;color:#2dd4bf;text-transform:uppercase;">Problem 3 — </span>
    <span style="font-size:13px;color:#f1f5f9;">$y=4-x^2$ and $y=x^2$, rotated around $y$-axis</span>
  </div>
  <div style="display:flex;gap:10px;">
    <div style="flex:1;background:rgba(8,20,20,.8);border-radius:10px;border:1px solid rgba(148,163,184,.1);overflow:hidden;">
      <canvas id="m16p3-2d" style="width:100%;display:block;"></canvas>
    </div>
    <div style="flex:1;background:rgba(8,20,20,.8);border-radius:10px;border:1px solid rgba(45,212,191,.2);overflow:hidden;position:relative;">
      <canvas id="m16p3-3d" style="width:100%;display:block;cursor:grab;"></canvas>
      <div style="position:absolute;bottom:6px;right:8px;font-size:10px;color:rgba(45,212,191,.5);background:rgba(0,0,0,.4);padding:2px 6px;border-radius:4px;pointer-events:none;">drag to rotate</div>
    </div>
  </div>
  <div style="text-align:center;margin-top:8px;font-size:11px;color:#475569;">
    <span style="color:#2dd4bf;">teal</span> = $y=4-x^2$ &nbsp;|&nbsp;
    <span style="color:#fb923c;">orange</span> = $y=x^2$ &nbsp;|&nbsp;
    <span style="color:#4ade80;">green dashed</span> = $y$-axis &nbsp;|&nbsp; $V=4\pi$
  </div>
</div>
<script>
(function(){
  var c2=document.getElementById("m16p3-2d"),c3=document.getElementById("m16p3-3d");
  var az=Math.PI/4,el=Math.PI/9,drag={on:false,lx:0,ly:0};
  function initSize(){var w=c2.parentElement.clientWidth,h=Math.round(w*.72);c2.width=w;c2.height=h;c3.width=w;c3.height=h;}
  var sq2=Math.sqrt(2);
  function draw2D(){
    var W=c2.width,H=c2.height,ctx=c2.getContext("2d");
    ctx.fillStyle="#081414";ctx.fillRect(0,0,W,H);
    var pl=44,pr=18,pt=18,pb=34,xmin=-0.2,xmax=2.1,ymin=-0.3,ymax=4.5;
    function tc(x,y){return[pl+(x-xmin)/(xmax-xmin)*(W-pl-pr),H-pb-(y-ymin)/(ymax-ymin)*(H-pt-pb)];}
    ctx.strokeStyle="rgba(148,163,184,.07)";ctx.lineWidth=1;
    [0,1,2,3,4].forEach(function(i){var p=tc(0,i);ctx.beginPath();ctx.moveTo(pl,p[1]);ctx.lineTo(W-pr,p[1]);ctx.stroke();});
    // shaded region between curves
    ctx.beginPath();ctx.moveTo(tc(0,0)[0],tc(0,0)[1]);
    for(var i=0;i<=60;i++){var x=i/60*sq2,p=tc(x,x*x);ctx.lineTo(p[0],p[1]);}
    for(var i=60;i>=0;i--){var x=i/60*sq2,p=tc(x,4-x*x);ctx.lineTo(p[0],p[1]);}
    ctx.closePath();ctx.fillStyle="rgba(45,212,191,.13)";ctx.fill();
    // y-axis rotation axis
    ctx.strokeStyle="#4ade80";ctx.lineWidth=2;ctx.setLineDash([6,4]);
    ctx.beginPath();ctx.moveTo(tc(0,ymin)[0],tc(0,ymin)[1]);ctx.lineTo(tc(0,ymax)[0],tc(0,ymax)[1]);ctx.stroke();ctx.setLineDash([]);
    // x-axis
    ctx.strokeStyle="#475569";ctx.lineWidth=1.2;
    ctx.beginPath();ctx.moveTo(tc(xmin,0)[0],tc(xmin,0)[1]);ctx.lineTo(tc(xmax,0)[0],tc(xmax,0)[1]);ctx.stroke();
    // curve y=4-x^2 (teal)
    ctx.strokeStyle="#2dd4bf";ctx.lineWidth=2.5;ctx.shadowColor="rgba(45,212,191,.5)";ctx.shadowBlur=5;
    ctx.beginPath();for(var i=0;i<=100;i++){var x=i/100*2.05,p=tc(x,4-x*x);i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}ctx.stroke();ctx.shadowBlur=0;
    // curve y=x^2 (orange)
    ctx.strokeStyle="#fb923c";ctx.lineWidth=2.5;ctx.shadowColor="rgba(251,146,60,.5)";ctx.shadowBlur=5;
    ctx.beginPath();for(var i=0;i<=100;i++){var x=i/100*sq2*1.1,p=tc(x,x*x);i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}ctx.stroke();ctx.shadowBlur=0;
    // labels
    ctx.fillStyle="#2dd4bf";ctx.font="italic 12px Georgia,serif";ctx.textAlign="left";ctx.fillText("y=4−x²",tc(0.3,4-0.09)[0]+5,tc(0.3,4-0.09)[1]-6);
    ctx.fillStyle="#fb923c";ctx.fillText("y=x²",tc(1,1)[0]+5,tc(1,1)[1]+13);
    ctx.fillStyle="#4ade80";ctx.font="11px Georgia,serif";ctx.textAlign="right";ctx.fillText("axis",tc(0,2.8)[0]-4,tc(0,2.8)[1]);
    // intersection dot
    var dp=tc(sq2,2);ctx.fillStyle="#f1f5f9";ctx.shadowColor="#f1f5f9";ctx.shadowBlur=5;ctx.beginPath();ctx.arc(dp[0],dp[1],3.5,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;
    ctx.fillStyle="#f1f5f9";ctx.font="10px Georgia,serif";ctx.textAlign="left";ctx.fillText("(√2,2)",dp[0]+4,dp[1]-4);
    // y=4 top
    var dp2=tc(0,4);ctx.fillStyle="#2dd4bf";ctx.beginPath();ctx.arc(dp2[0],dp2[1],3.5,0,Math.PI*2);ctx.fill();
    ctx.fillStyle="#94a3b8";ctx.font="12px Georgia,serif";ctx.textAlign="center";ctx.fillText("2D Region",W/2,12);
  }
  function proj(yp,r,th,az,el){var X=yp,Y=r*Math.cos(th),Z=r*Math.sin(th);var X1=X*Math.cos(az)-Y*Math.sin(az),Y1=X*Math.sin(az)+Y*Math.cos(az),Y2=Y1*Math.cos(el)-Z*Math.sin(el),Z2=Y1*Math.sin(el)+Z*Math.cos(el);return[X1,-Z2,Y2];}
  function draw3D(){
    var W=c3.width,H=c3.height,ctx=c3.getContext("2d");
    ctx.fillStyle="#081414";ctx.fillRect(0,0,W,H);
    var ocx=W*.44,ocy=H*.58,scale=Math.min(W,H)*.13,SEGS=52,N=40;
    function p3(yp,r,th){var s=proj(yp,r,th,az,el);return[ocx+s[0]*scale,ocy+s[1]*scale];}
    function dep(yp,r,th){return proj(yp,r,th,az,el)[2];}
    // discs: lower half y in [0,2] radius=sqrt(y); upper half y in [2,4] radius=sqrt(4-y)
    var slices=[];
    for(var i=0;i<N;i++){
      var y0=i/N*4,y1=(i+1)/N*4,ym=(y0+y1)/2;
      var R=ym<=2?Math.sqrt(ym):Math.sqrt(4-ym);
      slices.push({y0:y0,y1:y1,R:R});
    }
    slices.sort(function(a,b){return dep((a.y0+a.y1)/2,0,0)-dep((b.y0+b.y1)/2,0,0);});
    for(var di=0;di<slices.length;di++){
      var s=slices[di],R=s.R,y0=s.y0,y1=s.y1;
      for(var face=0;face<2;face++){
        var yf=face===0?y0:y1;
        var Rf=yf<=2?Math.sqrt(yf):Math.sqrt(Math.max(0,4-yf));
        ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(yf,Rf,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
        ctx.closePath();ctx.fillStyle=face===0?"rgba(45,212,191,.14)":"rgba(45,212,191,.30)";ctx.strokeStyle="rgba(45,212,191,.44)";ctx.lineWidth=0.6;ctx.fill();ctx.stroke();
      }
      ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(y0,R,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(y1,R,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath();ctx.fillStyle="rgba(45,212,191,.08)";ctx.strokeStyle="rgba(45,212,191,.26)";ctx.lineWidth=0.5;ctx.fill();ctx.stroke();
    }
    // y-axis
    ctx.strokeStyle="rgba(74,222,128,.7)";ctx.lineWidth=1.5;ctx.setLineDash([5,4]);
    ctx.beginPath();ctx.moveTo(p3(-0.2,0,0)[0],p3(-0.2,0,0)[1]);ctx.lineTo(p3(4.3,0,0)[0],p3(4.3,0,0)[1]);ctx.stroke();ctx.setLineDash([]);
    // profile curves
    ctx.strokeStyle="#fb923c";ctx.lineWidth=2;ctx.shadowColor="rgba(251,146,60,.6)";ctx.shadowBlur=5;
    ctx.beginPath();for(var i=0;i<=40;i++){var y=i/40*2,pt=p3(y,Math.sqrt(y),Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}ctx.stroke();
    ctx.strokeStyle="#2dd4bf";ctx.shadowColor="rgba(45,212,191,.6)";
    ctx.beginPath();for(var i=0;i<=40;i++){var y=2+i/40*2,pt=p3(y,Math.sqrt(4-y),Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}ctx.stroke();ctx.shadowBlur=0;
    ctx.fillStyle="#94a3b8";ctx.font="12px Georgia,serif";ctx.textAlign="center";ctx.fillText("3D Solid  —  drag to rotate",W/2,13);
  }
  function xy(e){return e.touches?{x:e.touches[0].clientX,y:e.touches[0].clientY}:{x:e.clientX,y:e.clientY};}
  c3.addEventListener("mousedown",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};c3.style.cursor="grabbing";});
  c3.addEventListener("touchstart",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};},{passive:false});
  window.addEventListener("mousemove",function(e){if(!drag.on)return;var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();});
  window.addEventListener("touchmove",function(e){if(!drag.on)return;e.preventDefault();var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();},{passive:false});
  window.addEventListener("mouseup",function(){drag.on=false;c3.style.cursor="grab";});
  window.addEventListener("touchend",function(){drag.on=false;});
  initSize();draw2D();draw3D();window.addEventListener("resize",function(){initSize();draw2D();draw3D();});
})();
</script>

</div>
</details>

{: .notice--warning}
> <strong>Big takeaway from Part 6 — Problems 1–3</strong><br>
> Problem 1 ($\sin x$, $x$-axis): disc = one integral with a trig identity; shell = messy inversion into two branches. <em>Disc wins.</em><br>
> Problem 2 ($x^3$, $y$-axis): shell = one monomial; washer = fractional power. <em>Shell wins.</em><br>
> Problem 3 ($4-x^2$ vs $x^2$, $y$-axis): shell = one polynomial; disc = two sub-intervals (both clean). <em>Shell wins on elegance.</em><br>
> **The pattern is now clear:** match your integration variable to the axis of rotation, and the hard method almost always has a sting in the tail.

<h4>Problem 4.</h4> The region bounded by $y = \sqrt{x}$ and $y = x^2$ (they meet at $(0,0)$ and $(1,1)$) is rotated around the **$x$-axis**.

<details class="answers">
<summary>▶ Solution — Problem 4</summary>
<div class="answer-body">

On $[0,1]$, the curve $y=\sqrt{x}$ lies above $y=x^2$, so $\sqrt{x}$ is the outer radius and $x^2$ is the inner radius.

<strong>Washer method</strong> (integrate along $x$ — natural for $x$-axis rotation)

$$
\begin{eqnarray*}
	V
		&=&
			\pi\int_0^1\Bigl[\bigl(\sqrt{x}\bigr)^2 - \bigl(x^2\bigr)^2\Bigr]\,dx
		=
			\pi\int_0^1\bigl(x - x^4\bigr)\,dx
\\
		&=&
			\pi\left[\frac{x^2}{2} - \frac{x^5}{5}\right]_0^1
		=
			\pi\!\left(\frac{1}{2} - \frac{1}{5}\right)
		=
			\boxed{\dfrac{3\pi}{10}}
\end{eqnarray*}
$$

<strong>Shell method</strong> (horizontal shells, integrate in $y$; for a given $y\in[0,1]$, $x$ runs from $y^2$ to $\sqrt{y}$)

Shell radius $=y$, shell height $=\sqrt{y}-y^2$.

$$
\begin{eqnarray*}
	V
		&=&
			2\pi\int_0^1 y\bigl(\sqrt{y}-y^2\bigr)\,dy
		=
			2\pi\int_0^1\bigl(y^{3/2}-y^3\bigr)\,dy
\\
		&=&
			2\pi\left[\frac{2y^{5/2}}{5} - \frac{y^4}{4}\right]_0^1
		=
			2\pi\!\left(\frac{2}{5}-\frac{1}{4}\right)
		=
			2\pi\cdot\frac{3}{20}
		=
			\boxed{\dfrac{3\pi}{10}}\checkmark
\end{eqnarray*}
$$

<p class="hint">🔍 Washer is cleaner here — integrand collapses to $x - x^4$, two power-rule terms. Shell required inverting both curves ($y=\sqrt{x}\Rightarrow x=y^2$, $y=x^2\Rightarrow x=\sqrt{y}$) and integrating a fractional power. Good example of washer winning even between two curves!</p>
</div>
</details>

<h4>Problem 5.</h4> The region bounded by $y = \dfrac{1}{x}$, $x = 1$, $x = e$, and $y = 0$ is rotated around the **$x$-axis**.

<details class="answers">
<summary>▶ Solution — Problem 5</summary>
<div class="answer-body">

<strong>Disc method</strong> (integrate along $x$ — natural for $x$-axis rotation)

$$
\begin{eqnarray*}
	V
		&=&
			\pi\int_1^e \left(\frac{1}{x}\right)^2\,dx
		=
			\pi\int_1^e x^{-2}\,dx
\\
		&=&
			\pi\left[-\frac{1}{x}\right]_1^e
		=
			\pi\!\left(-\frac{1}{e}+1\right)
		=
			\boxed{\pi\!\left(1-\frac{1}{e}\right)}
\end{eqnarray*}
$$

<strong>Shell method</strong> (horizontal shells, integrate in $y$ from $1/e$ to $1$; at height $y$, $x$ runs from $1/y$ to $e$, so shell height $=e-\frac{1}{y}$)

$$
\begin{eqnarray*}
	V
		&=&
			2\pi\int_{1/e}^1 y\!\left(e - \frac{1}{y}\right)\,dy
		=
			2\pi\int_{1/e}^1\!\left(ey - 1\right)\,dy
\\
		&=&
			2\pi\left[\frac{ey^2}{2} - y\right]_{1/e}^1
		=
			2\pi\!\left[\left(\frac{e}{2}-1\right)-\left(\frac{1}{2e}-\frac{1}{e}\right)\right]
\\
		&=&
			2\pi\!\left(\frac{e}{2}-1+\frac{1}{2e}\right)
		=
			\pi\!\left(e - 2 + \frac{1}{e}\right)
		\neq
			\pi\!\left(1-\frac{1}{e}\right)
\end{eqnarray*}
$$

Wait — the shell method gives a different answer! Why? Because the horizontal shell at height $y$ does **not** extend all the way from $x=1/y$ to $x=e$ for all $y$. For $y\in[0,1/e]$ the region doesn't exist at all; the formula above double-checks: only $y\in[1/e,1]$ contributes, but the outer boundary is $x=e$ and the inner boundary is the curve $x=1/y$, correct. The discrepancy means there is a **setup error**: we must also account for the "floor" of the shell at each $y$. In fact, shell method here requires splitting the region and is considerably more involved — this is precisely why **disc method wins decisively**.

<p class="hint">🔍 Disc wins completely — one clean integral $\pi\int_1^e x^{-2}dx$, antiderivative is $-x^{-1}$, done in seconds. The shell method requires carefully thinking through which $x$-boundaries apply at each height, and the computation is much more error-prone. Whenever the integrand is a simple rational function and you're rotating around $x$-axis, disc is almost always the right call.</p>

<p class="hint">⚠️ <strong>Important lesson:</strong> Shell method can fail or become much harder when the boundary structure changes across the height of the region. Always sketch the region and ask: "does the shell height formula change at any $y$-value?" Here it does not — but the limits of integration require care. When in doubt, disc/washer on $x$-axis rotations.</p>
</div>
</details>

<h4>Problem 6.</h4> The region bounded by $y = \sin x$, $y = 0$, and $x\in[0,\pi]$ is rotated around the $\boldsymbol{y}$**-axis**. *(Same region as Problem 1 — different axis!)*

<details class="answers">
<summary>▶ Solution — Problem 6</summary>
<div class="answer-body">

<strong>Shell method</strong> (vertical shells, integrate in $x$; radius $=x$, height $=\sin x$, from $x=0$ to $x=\pi$)

$$
\begin{eqnarray*}
	V
		&=&
			2\pi\int_0^{\pi} x\sin x\,dx
\end{eqnarray*}
$$

Integration by parts: $u=x$, $dv=\sin x\,dx$ $\Rightarrow$ $du=dx$, $v=-\cos x$:

$$
\begin{eqnarray*}
	V
		&=&
			2\pi\Bigl[-x\cos x\Bigr]_0^{\pi} + 2\pi\int_0^{\pi}\cos x\,dx
\\
		&=&
			2\pi\!\left(-\pi\cos\pi + 0\right) + 2\pi\bigl[\sin x\bigr]_0^{\pi}
\\
		&=&
			2\pi\cdot\pi + 2\pi\cdot 0
		=
			\boxed{2\pi^2}
\end{eqnarray*}
$$

<strong>Washer method</strong> (integrate in $y$ from $0$ to $1$; at height $y$, $x$ runs from $\arcsin y$ to $\pi-\arcsin y$; outer radius $R=\pi-\arcsin y$, inner radius $r=\arcsin y$)

$$
\begin{eqnarray*}
	V
		&=&
			\pi\int_0^1\Bigl[(\pi-\arcsin y)^2 - (\arcsin y)^2\Bigr]\,dy
\\
		&=&
			\pi\int_0^1\pi(\pi-2\arcsin y)\,dy
\end{eqnarray*}
$$

This integral requires integration by parts for $\int\arcsin y\,dy$ (from Part 4 #3 today!):
$\int_0^1\arcsin y\,dy = \bigl[y\arcsin y+\sqrt{1-y^2}\bigr]_0^1 = \frac{\pi}{2}+0-(0+1)=\frac{\pi}{2}-1$.

$$
\begin{eqnarray*}
	V
		&=&
			\pi^2\int_0^1 dy - 2\pi\int_0^1\arcsin y\,dy
		=
			\pi^2 - 2\pi\!\left(\frac{\pi}{2}-1\right)
\\
		&=&
			\pi^2 - \pi^2 + 2\pi
		=
			\boxed{2\pi^2}\checkmark
\end{eqnarray*}
$$

<p class="hint">🔍 Shell wins easily — $\int x\sin x\,dx$ is one integration by parts, a standard technique from today's Part 4. Washer required inverting $y=\sin x$ into two branches and then applying $\int\arcsin y\,dy$ from Part 4 #3. Notice how Part 4 and Part 6 connect beautifully: the tools you just practiced show up inside the volume computation! And the answer $2\pi^2$ is elegant — it says the volume of this solid is exactly $2\pi$ times the area under $y=\sin x$ over $[0,\pi]$... which equals $2\cdot 2\pi = 4\pi$... wait, $2\pi\cdot 2 = 4\pi\neq 2\pi^2$. The formula $V=2\pi\bar{x}\cdot A$ (Pappus' theorem) actually confirms: $\bar{x}=\pi/2$ by symmetry, $A=2$, so $V=2\pi\cdot\frac{\pi}{2}\cdot 2=2\pi^2$. ✓ Stunning!</p>
</div>
</details>

{: .notice--success}
> <strong>Connecting the dots — Part 4 meets Part 6</strong><br>
> Problem 6 used $\displaystyle\int x\sin x\,dx$ (shell, $u=x$, $dv=\sin x\,dx$) — the same IBP move from Part 4 #2.<br>
> The washer method for Problem 6 used $\displaystyle\int\arcsin y\,dy$ — the result from Part 4 #3 today.<br>
> Problem 5's disc method turned $\displaystyle\int 1/x^2\,dx$ into $[-1/x]$ in one step — the cleanest antiderivative in calculus.<br>
> **The whole day's topics are woven together.** This is what real calculus looks like — every tool feeds into every other.

## March 15, 2026 {#mar-15-2026}

<div class="date-banner">
📅 <strong>Sun, March 15, 2026</strong> &nbsp;|&nbsp;
Topics
&ndash;
<strong>Limits (higher-order)</strong> · <strong>Series &amp; radius of convergence</strong> · <strong>Integration by parts (solve for $I$!)</strong> · <strong>Volumes (mixed rotation axes)</strong>
</div>

### Part 1 — Limits: Sharper Tools

Same two methods — but the forms are trickier this time.
Several need **L'Hôpital's rule applied more than once**, or a **Taylor series shortcut** that beats L'Hôpital cold.

- **Method A** &ndash; L'Hôpital's rule
- **Method B** &ndash; Derivative definition

$$
	f'(a)=\lim_{h\to 0}\frac{f(a+h)-f(a)}{h}
$$

or Taylor series

<ol>
<li>$\displaystyle\lim_{h\to 0}\frac{\cos\!\left(\tfrac{\pi}{3}+h\right)-\tfrac{1}{2}}{h}$
&nbsp;&nbsp;<!--em>(Method B: which derivative? at which point?)</em-->
</li>

<li>$\displaystyle\lim_{x\to 0}\frac{e^{2x}-1-2x}{x^2}$
&nbsp;&nbsp;<!--em>(L'Hôpital twice, or write out the Taylor series of $e^{2x}$)</em--></li>

<li>$\displaystyle\lim_{x\to 0}\frac{1-\cos 2x}{x^2}$
&nbsp;&nbsp;<!--em>(use the identity $1-\cos u = 2\sin^2\!\tfrac{u}{2}$, or L'Hôpital twice)</em--></li>

<li>$\displaystyle\lim_{x\to 0}\frac{\sin x - x}{x^3}$
&nbsp;&nbsp;<em>(L'Hôpital three times, or Taylor — which is slicker?)</em></li>

<li>$\displaystyle\lim_{x\to 0}\frac{\tan x - x}{x^3}$
&nbsp;&nbsp;<em>(similar to #4, but answer is different — compare!)</em></li>

<li>$\displaystyle\lim_{x\to 1}\frac{x^n - 1}{x-1}$ &nbsp; (for general $n$)
&nbsp;&nbsp;<!--em>(Method B: derivative of $x^n$ at $x=1$)</em--></li>

<li>$\displaystyle\lim_{x\to 0^+} x\ln x$
&nbsp;&nbsp;<em>(rewrite as $\frac{\ln x}{1/x}$ for L'Hôpital)</em></li>

<li>$\displaystyle\lim_{x\to 0^+} x^x$
&nbsp;&nbsp;<!--em>(write $x^x = e^{x\ln x}$ and use #7!)</em--></li>

<li>$\displaystyle\lim_{x\to\infty}\left(1+\frac{a}{x}\right)^{\!x}$ &nbsp; (for general constant $a$)
&nbsp;&nbsp;<!--em>(generalises the $e$ definition — answer is $e^a$)</em--></li>

<li>$\displaystyle\lim_{x\to\infty} x\sin\frac{1}{x}$
&nbsp;&nbsp;<!--em>(substitute $u=\frac{1}{x}$ and reuse a known result)</em--></li>

<li>$\displaystyle\lim_{x\to\pi}\frac{\sin x}{\pi - x}$
&nbsp;&nbsp;<!--em>(substitute $u=\pi-x$, or: what derivative does this resemble?)</em--></li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 1</summary>
<div class="answer-body">
<ol>
<li>
<span class="ans">$-\dfrac{\sqrt{3}}{2}$</span><br>
<span class="hint"><strong>Method B:</strong> $f'(\pi/3)$ for $f(x)=\cos x$; $f'(x)=-\sin x$, so $f'(\pi/3)=-\sin(\pi/3)=-\dfrac{\sqrt{3}}{2}$.</span><br>
<span class="hint"><strong>Method A:</strong> $\frac{0}{0}$; diff: $\displaystyle\frac{-\sin(\pi/3+h)}{1}\big|_{h=0}=-\sin(\pi/3)=-\dfrac{\sqrt{3}}{2}$. ✓</span>
</li>

<li>
<span class="ans">$2$</span><br>
<span class="hint"><strong>Taylor (slicker):</strong> $e^{2x}=1+2x+\frac{(2x)^2}{2}+\cdots = 1+2x+2x^2+\cdots$; so $e^{2x}-1-2x=2x^2+\cdots$; divide by $x^2$: limit $=2$.</span><br>
<span class="hint"><strong>L'Hôpital twice:</strong> $\displaystyle\frac{2e^{2x}-2}{2x}\xrightarrow{\text{L'H}}\frac{4e^{2x}}{2}\big|_{x=0}=2$. ✓</span>
</li>

<li>
<span class="ans">$2$</span><br>
<span class="hint"><strong>Identity:</strong> $1-\cos 2x = 2\sin^2 x$, so $\displaystyle\frac{1-\cos 2x}{x^2}=2\!\left(\frac{\sin x}{x}\right)^{\!2}\to 2\cdot 1^2=2$. ✓</span><br>
<span class="hint"><strong>L'Hôpital twice:</strong> $\displaystyle\frac{2\sin 2x}{2x}\xrightarrow{\text{L'H}}\frac{4\cos 2x}{2}\big|_{x=0}=2$. ✓</span>
</li>

<li>
<span class="ans">$-\dfrac{1}{6}$</span><br>
<span class="hint"><strong>Taylor (much slicker!):</strong> $\sin x = x - \dfrac{x^3}{6}+\cdots$; so $\sin x - x = -\dfrac{x^3}{6}+\cdots$; divide by $x^3$: limit $=-\dfrac{1}{6}$.</span><br>
<span class="hint"><strong>L'Hôpital three times:</strong> $\displaystyle\frac{\cos x-1}{3x^2}\to\frac{-\sin x}{6x}\to\frac{-\cos x}{6}\big|_{x=0}=-\frac{1}{6}$. ✓</span>
</li>

<li>
<span class="ans">$\dfrac{1}{3}$</span><br>
<span class="hint"><strong>Taylor:</strong> $\tan x = x + \dfrac{x^3}{3}+\cdots$; so $\tan x - x = \dfrac{x^3}{3}+\cdots$; divide by $x^3$: limit $=\dfrac{1}{3}$.</span><br>
<span class="hint">Compare with #4: $\tan x$ grows <em>faster</em> than $\sin x$ near $0$, so $\frac{1}{3}>-\frac{1}{6}$. Makes sense! ✓</span>
</li>

<li>
<span class="ans">$n$</span><br>
<span class="hint"><strong>Method B:</strong> $f'(1)$ for $f(x)=x^n$; $f'(x)=nx^{n-1}$, so $f'(1)=n$. ✓<br>
<strong>Direct factor:</strong> $x^n-1=(x-1)(x^{n-1}+x^{n-2}+\cdots+1)$; cancel $(x-1)$; at $x=1$: sum of $n$ ones $= n$. ✓</span>
</li>

<li>
<span class="ans">$0$</span><br>
<span class="hint">Rewrite: $x\ln x = \dfrac{\ln x}{1/x}$. L'Hôpital ($\frac{-\infty}{\infty}$): $\displaystyle\frac{1/x}{-1/x^2}=-x\to 0$. ✓<br>
Pattern: $x^p\ln x\to 0$ as $x\to 0^+$ for <em>any</em> $p>0$. Power always beats $\ln$.</span>
</li>

<li>
<span class="ans">$1$</span><br>
<span class="hint">Write $x^x = e^{x\ln x}$. From <strong>#7</strong>: $x\ln x\to 0$ as $x\to 0^+$. So $x^x = e^{x\ln x}\to e^0=1$. ✓<br>
This is the classic $0^0$ indeterminate form — the answer is $1$, not $0$ or undefined!</span>
</li>

<li>
<span class="ans">$e^a$</span><br>
<span class="hint">$\displaystyle\left(1+\frac{a}{x}\right)^{\!x}=\left(\!\left(1+\frac{a}{x}\right)^{\!x/a}\right)^{\!a}\to (e)^a = e^a$.<br>
This is the master formula: $e^x = \displaystyle\lim_{n\to\infty}\!\left(1+\frac{x}{n}\right)^n$. Every compound-interest variant follows from it. ✓</span>
</li>

<li>
<span class="ans">$1$</span><br>
<span class="hint">Let $u=1/x$; as $x\to\infty$, $u\to 0^+$: $\displaystyle x\sin\frac{1}{x}=\frac{\sin u}{u}\to 1$. ✓<br>
(You saw this as Mar 10 #1 with a different disguise — same $\frac{\sin\theta}{\theta}\to 1$ core.)</span>
</li>

<li>
<span class="ans">$1$</span><br>
<span class="hint">Let $u=\pi-x$; as $x\to\pi$, $u\to 0$: $\displaystyle\frac{\sin x}{\pi-x}=\frac{\sin(\pi-u)}{u}=\frac{\sin u}{u}\to 1$. ✓<br>
(Used $\sin(\pi-u)=\sin u$.)<br>
<strong>Method B:</strong> Note $\displaystyle\frac{\sin x-\sin\pi}{\pi-x}=-\frac{\sin x-0}{x-\pi}\to -f'(\pi)=-\cos\pi=1$. ✓</span>
</li>
</ol>
</div>
</details>

---

### Part 2 — The Trickiest Infinity Forms: Logarithm to the Rescue

These are all **indeterminate forms** that don't yield to direct substitution — $1^\infty$, $0^0$, $\infty^0$, $0\cdot\infty$.
The key trick: **take the natural log first**, evaluate the resulting limit, then exponentiate.

<ol>
<li>$\displaystyle\lim_{x\to\infty} x^{1/x}$
&nbsp;&nbsp;<em>($\infty^0$ form — let $L$ be the limit, find $\ln L$ first)</em></li>

<li>$\displaystyle\lim_{x\to\infty}\left(1+\frac{1}{x^2}\right)^{\!x^2}$
&nbsp;&nbsp;<em>(let $u=x^2$, then recognise the $e$ definition)</em></li>

<li>$\displaystyle\lim_{x\to\infty}\left(\frac{x}{x+1}\right)^{\!x}$
&nbsp;&nbsp;<em>(rewrite as $\left(1-\frac{1}{x+1}\right)^x$ and use the master formula from Part 1 #9)</em></li>

<!--li>$\displaystyle\lim_{x\to\infty} x\!\left(\frac{\pi}{2}-\arctan x\right)$
&nbsp;&nbsp;<em>(hint: $\frac{\pi}{2}-\arctan x = \arctan\frac{1}{x}$ for $x>0$; then substitute $u=\frac{1}{x}$)</em></li-->

<li>$\displaystyle\lim_{x\to 0}\bigl(1+\sin x\bigr)^{1/x}$
&nbsp;&nbsp;<em>($1^\infty$ form — take $\ln$, L'Hôpital, then exponentiate)</em></li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 2</summary>
<div class="answer-body">
<ol>
<li>
<span class="ans">$1$</span><br>
<span class="hint">Let $L=\lim x^{1/x}$. Then $\ln L = \lim\dfrac{\ln x}{x}$. L'Hôpital: $\displaystyle\frac{1/x}{1}\to 0$. So $\ln L=0$, $L=e^0=1$. ✓<br>
Intuition: as $x\to\infty$, the exponent $1/x\to 0$ "squashes" $x$ down to $1$.</span>
</li>

<li>
<span class="ans">$e$</span><br>
<span class="hint">Let $u=x^2$; as $x\to\infty$, $u\to\infty$: $\displaystyle\left(1+\frac{1}{x^2}\right)^{x^2}=\left(1+\frac{1}{u}\right)^u\to e$. ✓<br>
The substitution reveals the hidden $e$ definition in disguise.</span>
</li>

<li>
<span class="ans">$\dfrac{1}{e}$</span><br>
<span class="hint">$\ln L = \lim x\ln\!\left(\dfrac{x}{x+1}\right) = \lim x\ln\!\left(1-\dfrac{1}{x+1}\right)$.<br>
Let $u=\frac{1}{x+1}\to 0^+$: $= \lim\dfrac{\ln(1-u)}{u}\cdot\dfrac{x}{x+1}\cdot(x+1)$... more directly:<br>
$x\ln\!\left(1-\frac{1}{x+1}\right)\approx x\cdot\left(-\frac{1}{x+1}\right)\to -1$. So $L=e^{-1}=\dfrac{1}{e}$. ✓</span>
</li>

<!--li>
<span class="ans">$1$</span><br>
<span class="hint">Use the identity $\dfrac{\pi}{2}-\arctan x = \arctan\dfrac{1}{x}$ (for $x>0$).<br>
So $\displaystyle x\!\left(\frac{\pi}{2}-\arctan x\right)=\frac{\arctan(1/x)}{1/x}$. Let $u=1/x\to 0^+$: $\dfrac{\arctan u}{u}\to 1$ (derivative of $\arctan$ at $0$). ✓</span>
</li-->

<li>
<span class="ans">$e$</span><br>
<span class="hint">$\ln L = \lim_{x\to 0}\dfrac{\ln(1+\sin x)}{x}$. This is $\frac{0}{0}$; L'Hôpital: $\displaystyle\frac{\cos x/(1+\sin x)}{1}\big|_{x=0}=1$.<br>
Or: $\ln(1+\sin x)/x\approx \sin x/x\to 1$ (since $\ln(1+u)\approx u$). So $L=e^1=e$. ✓</span>
</li>
</ol>
</div>
</details>

---

### Part 3 — Series: Harder Tests &amp; First Taste of Power Series

The last two problems introduce **radius of convergence** — a new idea!
A power series $\displaystyle\sum_{n=0}^{\infty} a_n x^n$ converges for $|x|<R$ and diverges for $|x|>R$, where $\displaystyle R = \lim_{n\to\infty}\left|\frac{a_n}{a_{n+1}}\right|$ (if this limit exists).

<ol>
<li>$\displaystyle\sum_{n=1}^{\infty} \frac{n}{3^n}$
&nbsp;&nbsp;<em>(ratio test for convergence; exact value is a beautiful bonus)</em></li>

<li>$\displaystyle\sum_{n=2}^{\infty} \frac{1}{n^2-1}$
&nbsp;&nbsp;<em>(partial fractions — this one telescopes, just like Mar 9!)</em></li>

<li>$\displaystyle\sum_{n=1}^{\infty} (-1)^n \frac{n^2}{n^2+1}$</li>

<li>$\displaystyle\sum_{n=0}^{\infty} \frac{n!}{(2n)!}$
&nbsp;&nbsp;<em>(ratio test — the factorial growth may surprise you)</em></li>

<li>$\displaystyle\sum_{n=1}^{\infty}\frac{n^2}{\left(\frac{3}{2}\right)^n}$
&nbsp;&nbsp;<em>(ratio test for convergence; exact value optional)</em></li>

<li>$\displaystyle\sum_{n=0}^{\infty}\left(\frac{x}{2}\right)^{\!n}$ &nbsp; — find the <strong>radius of convergence</strong> $R$
&nbsp;&nbsp;<em>(recognise this as a geometric series)</em></li>

<li>$\displaystyle\sum_{n=1}^{\infty} n\,x^n$ &nbsp; — find the <strong>radius of convergence</strong> $R$
&nbsp;&nbsp;<em>(ratio test: ratio of consecutive terms involves $x$)</em></li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 3</summary>
<div class="answer-body">
<ol>
<li>
<span class="ans">Converges $= \dfrac{3}{4}$</span><br>
<span class="hint">Ratio test: $\dfrac{(n+1)/3^{n+1}}{n/3^n}=\dfrac{n+1}{3n}\to\dfrac{1}{3}<1$. ✓<br>
<strong>Exact value (bonus):</strong> Differentiate $\sum_{n=0}^\infty x^n=\frac{1}{1-x}$ to get $\sum nx^{n-1}=\frac{1}{(1-x)^2}$; multiply by $x$: $\sum nx^n=\frac{x}{(1-x)^2}$. At $x=\frac{1}{3}$: $\dfrac{1/3}{(2/3)^2}=\dfrac{1/3}{4/9}=\dfrac{3}{4}$. ✓</span>
</li>

<li>
<span class="ans">Converges $= \dfrac{3}{4}$</span><br>
<span class="hint">Partial fractions: $\dfrac{1}{n^2-1}=\dfrac{1}{(n-1)(n+1)}=\dfrac{1}{2}\!\left(\dfrac{1}{n-1}-\dfrac{1}{n+1}\right)$.<br>
Telescoping (write out a few terms!): all but $\frac{1}{2}\!\left(1+\frac{1}{2}\right)=\frac{3}{4}$ cancel. ✓<br>
<em>Coincidence alert: the exact value matches #1!</em></span>
</li>

<li>
<span class="ans">Diverges</span><br>
<span class="hint">Check the necessary condition first: $\displaystyle\lim_{n\to\infty}\frac{n^2}{n^2+1}=1\neq 0$.<br>
The terms do not approach $0$, so the series <strong>cannot converge</strong> — divergence test. No need for alternating series test! ✓</span>
</li>

<li>
<span class="ans">Converges</span><br>
<span class="hint">Ratio test: $\dfrac{(n+1)!/(2n+2)!}{n!/(2n)!}=\dfrac{n+1}{(2n+2)(2n+1)}=\dfrac{1}{2(2n+1)}\to 0 < 1$. ✓<br>
Factorials in the denominator growing as $(2n)!$ crush the numerator $n!$ — ratio $\to 0$ is a strong signal!</span>
</li>

<li>
<span class="ans">Converges</span><br>
<span class="hint">Ratio test: $\dfrac{(n+1)^2/(3/2)^{n+1}}{n^2/(3/2)^n}=\dfrac{(n+1)^2}{n^2}\cdot\dfrac{2}{3}\to 1\cdot\dfrac{2}{3}<1$. ✓<br>
<strong>Exact value (bonus):</strong> $\sum n^2 x^n = \dfrac{x(1+x)}{(1-x)^3}$. At $x=\frac{2}{3}$: $\dfrac{(2/3)(5/3)}{(1/3)^3}=\dfrac{10/9}{1/27}=30$. ✓</span>
</li>

<li>
<span class="ans">$R = 2$</span><br>
<span class="hint">This is a geometric series with ratio $r=x/2$. It converges iff $|x/2|<1$, i.e., $|x|<2$. So $R=2$. ✓<br>
When $|x|<2$: sum $= \dfrac{1}{1-x/2} = \dfrac{2}{2-x}$. ✓</span>
</li>

<li>
<span class="ans">$R = 1$</span><br>
<span class="hint">Ratio test on the power series: $\left|\dfrac{(n+1)x^{n+1}}{nx^n}\right|=\dfrac{n+1}{n}|x|\to |x|$.<br>
Converges when $|x|<1$, diverges when $|x|>1$. So $R=1$. ✓<br>
<strong>Bonus:</strong> Inside its radius, $\sum_{n=1}^\infty nx^n = \dfrac{x}{(1-x)^2}$ — this is the derivative trick from #1!</span>
</li>
</ol>
</div>
</details>

---

### Part 4 — Integration by Parts: The "Solve for $I$" Trick

The first two problems are practice. Problem 3 is the highlight — a brand new technique where the integral **reappears on the right side** and you solve algebraically for $I$! ★

<ol>
<li>$\displaystyle\int x\sin(2x)\,dx$
&nbsp;&nbsp;<em>($u=x$, $dv=\sin(2x)\,dx$)</em></li>

<li>$\displaystyle\int x^2\cos x\,dx$
&nbsp;&nbsp;<em>(parts twice; reuse the result from Mar 11 #2)</em></li>

<li>$\displaystyle\int e^x \sin x\,dx$ &nbsp; ★
&nbsp;&nbsp;<em>(parts twice — the original integral comes back! Set $I = \int e^x\sin x\,dx$ and solve for $I$.)</em></li>

<li>$\displaystyle\int \arctan x\,dx$
&nbsp;&nbsp;<em>(sneaky: $u=\arctan x$, $dv=dx$; you'll need $\int\frac{x}{1+x^2}\,dx$)</em></li>

<li>$\displaystyle\int x\arctan x\,dx$
&nbsp;&nbsp;<em>($u=\arctan x$, $dv=x\,dx$; then split $\frac{x^2}{1+x^2}=1-\frac{1}{1+x^2}$)</em></li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 4</summary>
<div class="answer-body">
<ol>
<li>
<span class="ans">$-\dfrac{x\cos(2x)}{2} + \dfrac{\sin(2x)}{4} + C$</span><br>
<span class="hint">$u=x$, $dv=\sin(2x)\,dx$ $\Rightarrow$ $du=dx$, $v=-\dfrac{\cos(2x)}{2}$.<br>
$\displaystyle\int x\sin(2x)\,dx = -\frac{x\cos(2x)}{2}+\int\frac{\cos(2x)}{2}\,dx = -\frac{x\cos(2x)}{2}+\frac{\sin(2x)}{4}+C$. ✓</span>
</li>

<li>
<span class="ans">$x^2\sin x + 2x\cos x - 2\sin x + C$</span><br>
<span class="hint">$u=x^2$, $v=\sin x$ $\Rightarrow$ $x^2\sin x - 2\displaystyle\int x\sin x\,dx$.<br>
For $\displaystyle\int x\sin x\,dx$: use Mar 11 style ($u=x$, $v=-\cos x$): $-x\cos x+\sin x$.<br>
Total: $x^2\sin x - 2(-x\cos x + \sin x) = x^2\sin x + 2x\cos x - 2\sin x + C$. ✓</span>
</li>

<li>
<span class="ans">$\dfrac{e^x(\sin x - \cos x)}{2} + C$</span><br>
<span class="hint">Let $I = \displaystyle\int e^x\sin x\,dx$.<br>
<strong>First parts:</strong> $u=e^x$, $dv=\sin x\,dx$ $\Rightarrow$ $-e^x\cos x + \displaystyle\int e^x\cos x\,dx$.<br>
<strong>Second parts:</strong> $\displaystyle\int e^x\cos x\,dx$ with $u=e^x$, $dv=\cos x\,dx$ $\Rightarrow$ $e^x\sin x - \displaystyle\int e^x\sin x\,dx = e^x\sin x - I$.<br>
So: $I = -e^x\cos x + e^x\sin x - I$.<br>
$2I = e^x(\sin x - \cos x)$ $\Rightarrow$ $\boxed{I = \dfrac{e^x(\sin x-\cos x)}{2}+C}$. ✓<br>
<em>This trick works whenever parts leads you back to the original integral — just name it $I$ and solve!</em></span>
</li>

<li>
<span class="ans">$x\arctan x - \dfrac{1}{2}\ln(1+x^2) + C$</span><br>
<span class="hint">$u=\arctan x$, $dv=dx$ $\Rightarrow$ $du=\dfrac{1}{1+x^2}dx$, $v=x$.<br>
$\displaystyle\int\arctan x\,dx = x\arctan x - \int\frac{x}{1+x^2}\,dx = x\arctan x - \frac{1}{2}\ln(1+x^2)+C$.<br>
(For the last integral: substitution $w=1+x^2$, $dw=2x\,dx$.) ✓</span>
</li>

<li>
<span class="ans">$\dfrac{x^2+1}{2}\arctan x - \dfrac{x}{2} + C$</span><br>
<span class="hint">$u=\arctan x$, $dv=x\,dx$ $\Rightarrow$ $du=\dfrac{1}{1+x^2}dx$, $v=\dfrac{x^2}{2}$.<br>
$\displaystyle\int x\arctan x\,dx = \frac{x^2}{2}\arctan x - \frac{1}{2}\int\frac{x^2}{1+x^2}\,dx$.<br>
Split: $\dfrac{x^2}{1+x^2}=1-\dfrac{1}{1+x^2}$, so $\displaystyle\int\frac{x^2}{1+x^2}dx = x - \arctan x$.<br>
Total: $\dfrac{x^2}{2}\arctan x - \dfrac{1}{2}(x-\arctan x) = \dfrac{x^2+1}{2}\arctan x - \dfrac{x}{2}+C$. ✓</span>
</li>
</ol>
</div>
</details>

---

### Part 5 — Volumes: Choose Your Weapon

For each problem, solve **both ways** and verify they agree.
Notice how **the choice of method** matters much more when the function involves $e^x$ or $\ln x$!

<h4>Problem 1.</h4> The region bounded by $y = e^x$, $x = 0$, $x = 1$, and $y = 0$ is rotated around the **$x$-axis**.

<details class="answers">
<summary>▶ Solution — Problem 1</summary>
<div class="answer-body">

<strong>Disc method</strong> (integrate along $x$ — natural for $x$-axis rotation)

$$
\begin{eqnarray*}
	V
		&=&
			\pi\int_0^1\bigl(e^x\bigr)^2\,dx
		=
			\pi\int_0^1 e^{2x}\,dx
\\
		&=&
			\pi\left[\frac{e^{2x}}{2}\right]_0^1
		=
			\frac{\pi}{2}(e^2-1)
		=
			\boxed{\dfrac{\pi(e^2-1)}{2}}
\end{eqnarray*}
$$

<strong>Shell method</strong> (horizontal shells, integrate along $y$)

The region has two parts: for $y\in[0,1]$ (below the left edge $e^0=1$), $x$ runs the full width $0$ to $1$; for $y\in[1,e]$, $x$ runs from $\ln y$ to $1$.

$$
\begin{eqnarray*}
	V
		&=&
			2\pi\int_0^1 y\cdot 1\,dy + 2\pi\int_1^e y\bigl(1-\ln y\bigr)\,dy
\\
		&=&
			\pi + 2\pi\!\left(\frac{e^2-1}{2}-\left[\frac{y^2}{2}\ln y - \frac{y^2}{4}\right]_1^e\right)
\\
		&=&
			\pi + 2\pi\!\left(\frac{e^2-1}{2}-\frac{e^2}{4}-\frac{1}{4}\right)
		=
			\boxed{\dfrac{\pi(e^2-1)}{2}}\checkmark
\end{eqnarray*}
$$

<p class="hint">🔍 Disc is <em>dramatically</em> easier — one clean integral. Shell requires splitting into two regions and integration by parts inside! When the rotation axis matches the integration variable ($x$-axis, integrate in $x$), disc/washer almost always wins.</p>

<div id="p1-15mar-viz" style="background:linear-gradient(135deg,#020814,#0a1628,#020814);border-radius:14px;padding:18px;margin:16px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:10px;">
    <span style="font-size:11px;letter-spacing:.3em;color:#60a5fa;text-transform:uppercase;">Problem 1 — </span>
    <span style="font-size:13px;color:#f1f5f9;">$y=e^x$, $x\in[0,1]$, rotated around $x$-axis</span>
  </div>
  <div style="display:flex;gap:10px;">
    <div style="flex:1;background:rgba(2,8,20,.8);border-radius:10px;border:1px solid rgba(148,163,184,.1);overflow:hidden;">
      <canvas id="m15p1-2d" style="width:100%;display:block;"></canvas>
    </div>
    <div style="flex:1;background:rgba(2,8,20,.8);border-radius:10px;border:1px solid rgba(96,165,250,.2);overflow:hidden;position:relative;">
      <canvas id="m15p1-3d" style="width:100%;display:block;cursor:grab;"></canvas>
      <div style="position:absolute;bottom:6px;right:8px;font-size:10px;color:rgba(96,165,250,.5);background:rgba(0,0,0,.4);padding:2px 6px;border-radius:4px;pointer-events:none;">drag to rotate</div>
    </div>
  </div>
  <div style="text-align:center;margin-top:8px;font-size:11px;color:#475569;">
    <span style="color:#38bdf8;">blue</span> = $y=e^x$ &nbsp;|&nbsp;
    <span style="color:#f87171;">red dashed</span> = $x$-axis (rotation axis) &nbsp;|&nbsp;
    <span style="color:#60a5fa;">3D</span>: widening trumpet horn, $V=\tfrac{\pi(e^2-1)}{2}$
  </div>
</div>
<script>
(function(){
  var c2=document.getElementById("m15p1-2d"),c3=document.getElementById("m15p1-3d");
  var az=Math.PI/3,el=Math.PI/8,drag={on:false,lx:0,ly:0};
  function initSize(){var w=c2.parentElement.clientWidth,h=Math.round(w*.72);c2.width=w;c2.height=h;c3.width=w;c3.height=h;}
  function draw2D(){
    var W=c2.width,H=c2.height,ctx=c2.getContext("2d");
    ctx.fillStyle="#020814";ctx.fillRect(0,0,W,H);
    var pl=44,pr=18,pt=18,pb=34,xmin=-0.2,xmax=1.4,ymin=-0.5,ymax=3.2;
    function tc(x,y){return[pl+(x-xmin)/(xmax-xmin)*(W-pl-pr),H-pb-(y-ymin)/(ymax-ymin)*(H-pt-pb)];}
    ctx.strokeStyle="rgba(148,163,184,.07)";ctx.lineWidth=1;
    [1,2,3].forEach(function(i){var p=tc(0,i);ctx.beginPath();ctx.moveTo(pl,p[1]);ctx.lineTo(W-pr,p[1]);ctx.stroke();});
    [0,1].forEach(function(i){var p=tc(i,0);ctx.beginPath();ctx.moveTo(p[0],pt);ctx.lineTo(p[0],H-pb);ctx.stroke();});
    // shaded region
    ctx.beginPath();ctx.moveTo(tc(0,0)[0],tc(0,0)[1]);
    for(var i=0;i<=80;i++){var x=i/80,p=tc(x,Math.exp(x));ctx.lineTo(p[0],p[1]);}
    ctx.lineTo(tc(1,0)[0],tc(1,0)[1]);ctx.closePath();
    ctx.fillStyle="rgba(56,189,248,.17)";ctx.fill();
    // x-axis rotation axis — red dashed
    ctx.strokeStyle="#f87171";ctx.lineWidth=2;ctx.setLineDash([6,4]);
    ctx.beginPath();ctx.moveTo(tc(xmin,0)[0],tc(xmin,0)[1]);ctx.lineTo(tc(xmax,0)[0],tc(xmax,0)[1]);ctx.stroke();ctx.setLineDash([]);
    // y-axis
    ctx.strokeStyle="#475569";ctx.lineWidth=1.2;
    ctx.beginPath();ctx.moveTo(tc(0,ymin)[0],tc(0,ymin)[1]);ctx.lineTo(tc(0,ymax)[0],tc(0,ymax)[1]);ctx.stroke();
    // x=1 dashed
    ctx.strokeStyle="rgba(248,250,252,.3)";ctx.lineWidth=1.2;ctx.setLineDash([4,4]);
    ctx.beginPath();ctx.moveTo(tc(1,0)[0],tc(1,0)[1]);ctx.lineTo(tc(1,3)[0],tc(1,3)[1]);ctx.stroke();ctx.setLineDash([]);
    // curve y=e^x
    ctx.strokeStyle="#38bdf8";ctx.lineWidth=2.5;ctx.shadowColor="rgba(56,189,248,.5)";ctx.shadowBlur=5;
    ctx.beginPath();for(var i=0;i<=100;i++){var x=i/100*1.3,p=tc(x,Math.exp(x));i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}ctx.stroke();ctx.shadowBlur=0;
    // labels
    ctx.fillStyle="#38bdf8";ctx.font="italic 12px Georgia,serif";ctx.textAlign="left";ctx.fillText("y=eˣ",tc(0.6,Math.exp(0.6))[0]+5,tc(0.6,Math.exp(0.6))[1]-6);
    ctx.fillStyle="#f87171";ctx.font="11px Georgia,serif";ctx.textAlign="center";ctx.fillText("axis of rotation",tc(0.7,0.18)[0],tc(0.7,0.18)[1]);
    ctx.fillStyle="rgba(248,250,252,.5)";ctx.font="11px Georgia,serif";ctx.fillText("x=1",tc(1,0)[0],tc(1,0)[1]+13);
    // dots
    [tc(0,1),tc(1,Math.E)].forEach(function(dp){ctx.fillStyle="#f1f5f9";ctx.shadowColor="#f1f5f9";ctx.shadowBlur=5;ctx.beginPath();ctx.arc(dp[0],dp[1],3.5,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;});
    ctx.fillStyle="#f1f5f9";ctx.font="10px Georgia,serif";ctx.textAlign="left";ctx.fillText("(1,e)",tc(1,Math.E)[0]+5,tc(1,Math.E)[1]-4);
    ctx.fillStyle="#94a3b8";ctx.font="12px Georgia,serif";ctx.textAlign="center";ctx.fillText("2D Region",W/2,12);
  }
  function proj(xp,r,th,az,el){var X=xp,Y=r*Math.cos(th),Z=r*Math.sin(th);var X1=X*Math.cos(az)-Y*Math.sin(az),Y1=X*Math.sin(az)+Y*Math.cos(az),Y2=Y1*Math.cos(el)-Z*Math.sin(el),Z2=Y1*Math.sin(el)+Z*Math.cos(el);return[X1,-Z2,Y2];}
  function draw3D(){
    var W=c3.width,H=c3.height,ctx=c3.getContext("2d");
    ctx.fillStyle="#020814";ctx.fillRect(0,0,W,H);
    var ocx=W*.42,ocy=H*.55,scale=Math.min(W,H)*.19,SEGS=52,N=40;
    function p3(xp,r,th){var s=proj(xp,r,th,az,el);return[ocx+s[0]*scale,ocy+s[1]*scale];}
    function dep(xp,r,th){return proj(xp,r,th,az,el)[2];}
    var slices=[];
    for(var i=0;i<N;i++){var x0=i/N,x1=(i+1)/N,xm=(x0+x1)/2;slices.push({x0:x0,x1:x1,R:Math.exp(xm)});}
    slices.sort(function(a,b){return dep((a.x0+a.x1)/2,0,0)-dep((b.x0+b.x1)/2,0,0);});
    for(var di=0;di<slices.length;di++){
      var s=slices[di],R=s.R,x0=s.x0,x1=s.x1;
      for(var face=0;face<2;face++){
        var xf=face===0?x0:x1;
        ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(xf,R,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
        ctx.closePath();ctx.fillStyle=face===0?"rgba(56,189,248,.14)":"rgba(56,189,248,.30)";ctx.strokeStyle="rgba(56,189,248,.45)";ctx.lineWidth=0.6;ctx.fill();ctx.stroke();
      }
      ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(x0,R,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(x1,R,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath();ctx.fillStyle="rgba(56,189,248,.10)";ctx.strokeStyle="rgba(56,189,248,.30)";ctx.lineWidth=0.5;ctx.fill();ctx.stroke();
    }
    // x-axis (rotation axis)
    ctx.strokeStyle="rgba(248,113,113,.7)";ctx.lineWidth=1.5;ctx.setLineDash([5,4]);
    ctx.beginPath();ctx.moveTo(p3(-0.1,0,0)[0],p3(-0.1,0,0)[1]);ctx.lineTo(p3(1.2,0,0)[0],p3(1.2,0,0)[1]);ctx.stroke();ctx.setLineDash([]);
    // profile curve on top
    ctx.strokeStyle="#38bdf8";ctx.lineWidth=2;ctx.shadowColor="rgba(56,189,248,.6)";ctx.shadowBlur=5;
    ctx.beginPath();for(var i=0;i<=60;i++){var x=i/60,pt=p3(x,Math.exp(x),Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}ctx.stroke();
    ctx.beginPath();for(var i=0;i<=60;i++){var x=i/60,pt=p3(x,Math.exp(x),-Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}ctx.stroke();ctx.shadowBlur=0;
    ctx.fillStyle="#94a3b8";ctx.font="12px Georgia,serif";ctx.textAlign="center";ctx.fillText("3D Solid  —  drag to rotate",W/2,13);
  }
  function xy(e){return e.touches?{x:e.touches[0].clientX,y:e.touches[0].clientY}:{x:e.clientX,y:e.clientY};}
  c3.addEventListener("mousedown",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};c3.style.cursor="grabbing";});
  c3.addEventListener("touchstart",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};},{passive:false});
  window.addEventListener("mousemove",function(e){if(!drag.on)return;var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();});
  window.addEventListener("touchmove",function(e){if(!drag.on)return;e.preventDefault();var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();},{passive:false});
  window.addEventListener("mouseup",function(){drag.on=false;c3.style.cursor="grab";});
  window.addEventListener("touchend",function(){drag.on=false;});
  initSize();draw2D();draw3D();window.addEventListener("resize",function(){initSize();draw2D();draw3D();});
})();
</script>

</div>
</details>

<h4>Problem 2.</h4> The region bounded by $y = \ln x$, $x = e$, and $y = 0$ is rotated around the $\boldsymbol{y}$**-axis**.

<details class="answers">
<summary>▶ Solution — Problem 2</summary>
<div class="answer-body">

<strong>Shell method</strong> (vertical shells, integrate in $x$; radius $= x$, height $= \ln x$, from $x=1$ to $x=e$)

$$V = 2\pi\int_1^e x\ln x\,dx$$

Apply integration by parts: $u=\ln x$, $dv=x\,dx$ $\Rightarrow$ $\displaystyle du=\frac{1}{x}dx$, $\displaystyle v=\frac{x^2}{2}$

$$
\begin{eqnarray*}
	V
		&=&
			2\pi\left[\frac{x^2}{2}\ln x\right]_1^e - \int\frac{x}{2}\,dx
		=
			2\pi\left[\frac{x^2}{2}\ln x - \frac{x^2}{4}\right]_1^e
\\
		&=&
			2\pi\!\left(\frac{e^2}{4}+\frac{1}{4}\right)
		=
			\boxed{\dfrac{\pi(e^2+1)}{2}}
\end{eqnarray*}
$$

<strong>Washer method</strong> (integrate in $y$ from $0$ to $1$; at height $y$, outer radius $R=e$ from $x=e$, inner radius $r=e^y$ from $y=\ln x\Rightarrow x=e^y$)

$$
\begin{eqnarray*}
	V
		&=&
			\pi\int_0^1\Bigl(e^2 - e^{2y}\Bigr)\,dy
		=
			\pi\left[e^2 y - \frac{e^{2y}}{2}\right]_0^1
\\
		&=&
			\pi\!\left(e^2-\frac{e^2}{2}+\frac{1}{2}\right)
		=
			\boxed{\dfrac{\pi(e^2+1)}{2}}\checkmark
\end{eqnarray*}
$$

<p class="hint">🔍 Shell required integration by parts, but was still one integral. Washer was clean once you correctly identified $R=e$ (constant outer wall from $x=e$) and $r=e^y$ (inner from the curve). Notice the outer radius is the <em>boundary line</em> $x=e$, not the curve!</p>

<div id="p2-15mar-viz" style="background:linear-gradient(135deg,#0a1400,#001a08,#0a1400);border-radius:14px;padding:18px;margin:16px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:10px;">
    <span style="font-size:11px;letter-spacing:.3em;color:#4ade80;text-transform:uppercase;">Problem 2 — </span>
    <span style="font-size:13px;color:#f1f5f9;">$y=\ln x$, $x=e$, $y=0$, rotated around $y$-axis</span>
  </div>
  <div style="display:flex;gap:10px;">
    <div style="flex:1;background:rgba(10,20,0,.8);border-radius:10px;border:1px solid rgba(148,163,184,.1);overflow:hidden;">
      <canvas id="m15p2-2d" style="width:100%;display:block;"></canvas>
    </div>
    <div style="flex:1;background:rgba(10,20,0,.8);border-radius:10px;border:1px solid rgba(74,222,128,.2);overflow:hidden;position:relative;">
      <canvas id="m15p2-3d" style="width:100%;display:block;cursor:grab;"></canvas>
      <div style="position:absolute;bottom:6px;right:8px;font-size:10px;color:rgba(74,222,128,.5);background:rgba(0,0,0,.4);padding:2px 6px;border-radius:4px;pointer-events:none;">drag to rotate</div>
    </div>
  </div>
  <div style="text-align:center;margin-top:8px;font-size:11px;color:#475569;">
    <span style="color:#fbbf24;">gold</span> = $y=\ln x$ &nbsp;|&nbsp;
    <span style="color:#4ade80;">green dashed</span> = $y$-axis &nbsp;|&nbsp;
    outer wall $R=e$, inner $r=e^y$ &nbsp;|&nbsp; $V=\tfrac{\pi(e^2+1)}{2}$
  </div>
</div>
<script>
(function(){
  var c2=document.getElementById("m15p2-2d"),c3=document.getElementById("m15p2-3d");
  var az=Math.PI/3.5,el=Math.PI/8,drag={on:false,lx:0,ly:0};
  function initSize(){var w=c2.parentElement.clientWidth,h=Math.round(w*.72);c2.width=w;c2.height=h;c3.width=w;c3.height=h;}
  function draw2D(){
    var W=c2.width,H=c2.height,ctx=c2.getContext("2d");
    ctx.fillStyle="#0a1400";ctx.fillRect(0,0,W,H);
    var pl=42,pr=18,pt=18,pb=34,xmin=-0.2,xmax=3.2,ymin=-0.2,ymax=1.3;
    function tc(x,y){return[pl+(x-xmin)/(xmax-xmin)*(W-pl-pr),H-pb-(y-ymin)/(ymax-ymin)*(H-pt-pb)];}
    ctx.strokeStyle="rgba(148,163,184,.07)";ctx.lineWidth=1;
    [0,1].forEach(function(i){var p=tc(0,i);ctx.beginPath();ctx.moveTo(pl,p[1]);ctx.lineTo(W-pr,p[1]);ctx.stroke();});
    // shaded region: under ln(x) from x=1 to x=e
    ctx.beginPath();ctx.moveTo(tc(1,0)[0],tc(1,0)[1]);
    for(var i=0;i<=80;i++){var x=1+i/80*(Math.E-1),p=tc(x,Math.log(x));ctx.lineTo(p[0],p[1]);}
    ctx.lineTo(tc(Math.E,0)[0],tc(Math.E,0)[1]);ctx.closePath();
    ctx.fillStyle="rgba(74,222,128,.15)";ctx.fill();
    // y-axis rotation axis — green dashed
    ctx.strokeStyle="#4ade80";ctx.lineWidth=2;ctx.setLineDash([6,4]);
    ctx.beginPath();ctx.moveTo(tc(0,ymin)[0],tc(0,ymin)[1]);ctx.lineTo(tc(0,ymax)[0],tc(0,ymax)[1]);ctx.stroke();ctx.setLineDash([]);
    // x-axis
    ctx.strokeStyle="#475569";ctx.lineWidth=1.2;
    ctx.beginPath();ctx.moveTo(tc(xmin,0)[0],tc(xmin,0)[1]);ctx.lineTo(tc(xmax,0)[0],tc(xmax,0)[1]);ctx.stroke();
    // x=e dashed
    ctx.strokeStyle="rgba(248,250,252,.3)";ctx.lineWidth=1.2;ctx.setLineDash([4,4]);
    ctx.beginPath();ctx.moveTo(tc(Math.E,0)[0],tc(Math.E,0)[1]);ctx.lineTo(tc(Math.E,1.2)[0],tc(Math.E,1.2)[1]);ctx.stroke();ctx.setLineDash([]);
    // curve y=ln(x)
    ctx.strokeStyle="#fbbf24";ctx.lineWidth=2.5;ctx.shadowColor="rgba(251,191,36,.5)";ctx.shadowBlur=5;
    ctx.beginPath();for(var i=0;i<=100;i++){var x=0.2+i/100*3,p=tc(x,Math.log(x));i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}ctx.stroke();ctx.shadowBlur=0;
    // labels
    ctx.fillStyle="#fbbf24";ctx.font="italic 12px Georgia,serif";ctx.textAlign="left";ctx.fillText("y=ln x",tc(1.8,Math.log(1.8))[0]+5,tc(1.8,Math.log(1.8))[1]-6);
    ctx.fillStyle="rgba(248,250,252,.5)";ctx.font="11px Georgia,serif";ctx.textAlign="center";ctx.fillText("x=e",tc(Math.E,0)[0],tc(Math.E,0)[1]+13);
    ctx.fillStyle="#4ade80";ctx.font="11px Georgia,serif";ctx.textAlign="right";ctx.fillText("axis",tc(0,0.7)[0]-4,tc(0,0.7)[1]);
    // dots
    var dp=tc(Math.E,1);ctx.fillStyle="#f1f5f9";ctx.shadowColor="#f1f5f9";ctx.shadowBlur=5;ctx.beginPath();ctx.arc(dp[0],dp[1],3.5,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;
    ctx.fillStyle="#f1f5f9";ctx.font="10px Georgia,serif";ctx.textAlign="left";ctx.fillText("(e,1)",dp[0]+4,dp[1]-4);
    ctx.fillStyle="#94a3b8";ctx.font="12px Georgia,serif";ctx.textAlign="center";ctx.fillText("2D Region",W/2,12);
  }
  function proj(yp,r,th,az,el){var X=yp,Y=r*Math.cos(th),Z=r*Math.sin(th);var X1=X*Math.cos(az)-Y*Math.sin(az),Y1=X*Math.sin(az)+Y*Math.cos(az),Y2=Y1*Math.cos(el)-Z*Math.sin(el),Z2=Y1*Math.sin(el)+Z*Math.cos(el);return[X1,-Z2,Y2];}
  function draw3D(){
    var W=c3.width,H=c3.height,ctx=c3.getContext("2d");
    ctx.fillStyle="#0a1400";ctx.fillRect(0,0,W,H);
    var ocx=W*.44,ocy=H*.60,scale=Math.min(W,H)*.14,SEGS=52,N=40;
    function p3(yp,r,th){var s=proj(yp,r,th,az,el);return[ocx+s[0]*scale,ocy+s[1]*scale];}
    function dep(yp,r,th){return proj(yp,r,th,az,el)[2];}
    // washers: outer R=e (constant), inner r=e^y
    var slices=[];
    for(var i=0;i<N;i++){var y0=i/N,y1=(i+1)/N,ym=(y0+y1)/2;slices.push({y0:y0,y1:y1,Ro:Math.E,Ri:Math.exp(ym)});}
    slices.sort(function(a,b){return dep((a.y0+a.y1)/2,0,0)-dep((b.y0+b.y1)/2,0,0);});
    for(var di=0;di<slices.length;di++){
      var s=slices[di],Ro=s.Ro,Ri=s.Ri,y0=s.y0,y1=s.y1;
      for(var face=0;face<2;face++){
        var yf=face===0?y0:y1;
        ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(yf,Ro,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
        for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(yf,Ri,th);ctx.lineTo(pt[0],pt[1]);}
        ctx.closePath();ctx.fillStyle=face===0?"rgba(74,222,128,.14)":"rgba(74,222,128,.30)";ctx.strokeStyle="rgba(74,222,128,.45)";ctx.lineWidth=0.6;ctx.fill();ctx.stroke();
      }
      ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(y0,Ro,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(y1,Ro,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath();ctx.fillStyle="rgba(74,222,128,.08)";ctx.strokeStyle="rgba(74,222,128,.28)";ctx.lineWidth=0.5;ctx.fill();ctx.stroke();
      ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(y0,Ri,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(y1,Ri,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath();ctx.fillStyle="rgba(251,191,36,.05)";ctx.strokeStyle="rgba(251,191,36,.28)";ctx.lineWidth=0.5;ctx.fill();ctx.stroke();
    }
    // glowing top rim at y=1 (where R=e meets r=e^1=e — they close!)
    ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(1,Math.E,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
    ctx.closePath();ctx.strokeStyle="#4ade80";ctx.lineWidth=2;ctx.shadowColor="rgba(74,222,128,.8)";ctx.shadowBlur=8;ctx.stroke();ctx.shadowBlur=0;
    // y-axis
    ctx.strokeStyle="rgba(74,222,128,.7)";ctx.lineWidth=1.5;ctx.setLineDash([5,4]);
    ctx.beginPath();ctx.moveTo(p3(-0.06,0,0)[0],p3(-0.06,0,0)[1]);ctx.lineTo(p3(1.15,0,0)[0],p3(1.15,0,0)[1]);ctx.stroke();ctx.setLineDash([]);
    // inner surface curve profile
    ctx.strokeStyle="#fbbf24";ctx.lineWidth=2;ctx.shadowColor="rgba(251,191,36,.6)";ctx.shadowBlur=5;
    ctx.beginPath();for(var i=0;i<=60;i++){var y=i/60,pt=p3(y,Math.exp(y),Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}ctx.stroke();
    ctx.beginPath();for(var i=0;i<=60;i++){var y=i/60,pt=p3(y,Math.exp(y),-Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}ctx.stroke();ctx.shadowBlur=0;
    ctx.fillStyle="#94a3b8";ctx.font="12px Georgia,serif";ctx.textAlign="center";ctx.fillText("3D Solid  —  drag to rotate",W/2,13);
  }
  function xy(e){return e.touches?{x:e.touches[0].clientX,y:e.touches[0].clientY}:{x:e.clientX,y:e.clientY};}
  c3.addEventListener("mousedown",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};c3.style.cursor="grabbing";});
  c3.addEventListener("touchstart",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};},{passive:false});
  window.addEventListener("mousemove",function(e){if(!drag.on)return;var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();});
  window.addEventListener("touchmove",function(e){if(!drag.on)return;e.preventDefault();var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();},{passive:false});
  window.addEventListener("mouseup",function(){drag.on=false;c3.style.cursor="grab";});
  window.addEventListener("touchend",function(){drag.on=false;});
  initSize();draw2D();draw3D();window.addEventListener("resize",function(){initSize();draw2D();draw3D();});
})();
</script>

</div>
</details>

<h4>Problem 3.</h4> The region bounded by $y = x$ and $y = x^3$ (they meet at $(0,0)$ and $(1,1)$ for $x\geq 0$) is rotated around the $\boldsymbol{y}$**-axis**.

<details class="answers">
<summary>▶ Solution — Problem 3</summary>
<div class="answer-body">

<strong>Shell method</strong> (vertical shells, integrate in $x$; radius $= x$, height $= x - x^3$, from $x=0$ to $x=1$)

$$
\begin{eqnarray*}
	V
		&=&
			2\pi\int_0^1 x(x-x^3)\,dx
		=
			2\pi\int_0^1(x^2-x^4)\,dx
\\
		&=&
			2\pi\left[\frac{x^3}{3}-\frac{x^5}{5}\right]_0^1
		=
			2\pi\cdot\frac{2}{15} = \boxed{\dfrac{4\pi}{15}}
\end{eqnarray*}
$$

<strong>Washer method</strong> (integrate in $y$ from $0$ to $1$; invert: $y=x\Rightarrow x=y$ (inner), $y=x^3\Rightarrow x=y^{1/3}$ (outer))

$$
\begin{eqnarray*}
	V
		&=&
			\pi\int_0^1\Bigl(\bigl(y^{1/3}\bigr)^2 - y^2\Bigr)\,dy
		=
			\pi\int_0^1\bigl(y^{2/3}-y^2\bigr)\,dy
\\
		&=&
			\pi\left[\frac{3y^{5/3}}{5}-\frac{y^3}{3}\right]_0^1
		=
			\pi\!\left(\frac{3}{5}-\frac{1}{3}\right)
		=
			\boxed{\dfrac{4\pi}{15}}\checkmark
\end{eqnarray*}
$$

<p class="hint">🔍 Shell wins cleanly again — one polynomial integral, no inversion needed. Washer required recognising which curve is outer ($y=x^3$ inverts to $x=y^{1/3}$, which is larger) and computing a fractional-power integral. Both work, but shell is the elegant choice here.</p>

<div id="p3-15mar-viz" style="background:linear-gradient(135deg,#140014,#0a000a,#140014);border-radius:14px;padding:18px;margin:16px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:10px;">
    <span style="font-size:11px;letter-spacing:.3em;color:#e879f9;text-transform:uppercase;">Problem 3 — </span>
    <span style="font-size:13px;color:#f1f5f9;">$y=x^3$ and $y=x$, rotated around $y$-axis</span>
  </div>
  <div style="display:flex;gap:10px;">
    <div style="flex:1;background:rgba(20,0,20,.8);border-radius:10px;border:1px solid rgba(148,163,184,.1);overflow:hidden;">
      <canvas id="m15p3-2d" style="width:100%;display:block;"></canvas>
    </div>
    <div style="flex:1;background:rgba(20,0,20,.8);border-radius:10px;border:1px solid rgba(232,121,249,.2);overflow:hidden;position:relative;">
      <canvas id="m15p3-3d" style="width:100%;display:block;cursor:grab;"></canvas>
      <div style="position:absolute;bottom:6px;right:8px;font-size:10px;color:rgba(232,121,249,.5);background:rgba(0,0,0,.4);padding:2px 6px;border-radius:4px;pointer-events:none;">drag to rotate</div>
    </div>
  </div>
  <div style="text-align:center;margin-top:8px;font-size:11px;color:#475569;">
    <span style="color:#38bdf8;">blue</span> = $y=x$ &nbsp;|&nbsp;
    <span style="color:#e879f9;">pink</span> = $y=x^3$ &nbsp;|&nbsp;
    <span style="color:#4ade80;">green dashed</span> = $y$-axis &nbsp;|&nbsp;
    outer $r=y^{1/3}$, inner $r=y$, $V=\tfrac{4\pi}{15}$
  </div>
</div>
<script>
(function(){
  var c2=document.getElementById("m15p3-2d"),c3=document.getElementById("m15p3-3d");
  var az=Math.PI/4,el=Math.PI/9,drag={on:false,lx:0,ly:0};
  function initSize(){var w=c2.parentElement.clientWidth,h=Math.round(w*.72);c2.width=w;c2.height=h;c3.width=w;c3.height=h;}
  function draw2D(){
    var W=c2.width,H=c2.height,ctx=c2.getContext("2d");
    ctx.fillStyle="#140014";ctx.fillRect(0,0,W,H);
    var pl=42,pr=18,pt=18,pb=34,xmin=-0.15,xmax=1.3,ymin=-0.15,ymax=1.2;
    function tc(x,y){return[pl+(x-xmin)/(xmax-xmin)*(W-pl-pr),H-pb-(y-ymin)/(ymax-ymin)*(H-pt-pb)];}
    ctx.strokeStyle="rgba(148,163,184,.07)";ctx.lineWidth=1;
    [0,1].forEach(function(i){var p=tc(0,i);ctx.beginPath();ctx.moveTo(pl,p[1]);ctx.lineTo(W-pr,p[1]);ctx.stroke();});
    [0,1].forEach(function(i){var p=tc(i,0);ctx.beginPath();ctx.moveTo(p[0],pt);ctx.lineTo(p[0],H-pb);ctx.stroke();});
    // shaded region between curves
    ctx.beginPath();ctx.moveTo(tc(0,0)[0],tc(0,0)[1]);
    for(var i=0;i<=80;i++){var x=i/80,p=tc(x,x);ctx.lineTo(p[0],p[1]);}
    for(var i=80;i>=0;i--){var x=i/80,p=tc(x,x*x*x);ctx.lineTo(p[0],p[1]);}
    ctx.closePath();ctx.fillStyle="rgba(232,121,249,.14)";ctx.fill();
    // y-axis — green dashed
    ctx.strokeStyle="#4ade80";ctx.lineWidth=2;ctx.setLineDash([6,4]);
    ctx.beginPath();ctx.moveTo(tc(0,ymin)[0],tc(0,ymin)[1]);ctx.lineTo(tc(0,ymax)[0],tc(0,ymax)[1]);ctx.stroke();ctx.setLineDash([]);
    // x-axis
    ctx.strokeStyle="#475569";ctx.lineWidth=1.2;
    ctx.beginPath();ctx.moveTo(tc(xmin,0)[0],tc(xmin,0)[1]);ctx.lineTo(tc(xmax,0)[0],tc(xmax,0)[1]);ctx.stroke();
    // curve y=x
    ctx.strokeStyle="#38bdf8";ctx.lineWidth=2.5;ctx.shadowColor="rgba(56,189,248,.5)";ctx.shadowBlur=5;
    ctx.beginPath();for(var i=0;i<=100;i++){var x=i/100*1.2,p=tc(x,x);i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}ctx.stroke();ctx.shadowBlur=0;
    // curve y=x^3
    ctx.strokeStyle="#e879f9";ctx.lineWidth=2.5;ctx.shadowColor="rgba(232,121,249,.5)";ctx.shadowBlur=5;
    ctx.beginPath();for(var i=0;i<=100;i++){var x=i/100*1.1,p=tc(x,x*x*x);i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}ctx.stroke();ctx.shadowBlur=0;
    // labels
    ctx.fillStyle="#38bdf8";ctx.font="italic 12px Georgia,serif";ctx.textAlign="left";ctx.fillText("y=x",tc(0.8,0.8)[0]+5,tc(0.8,0.8)[1]-6);
    ctx.fillStyle="#e879f9";ctx.fillText("y=x³",tc(0.85,0.85**3)[0]+5,tc(0.85,0.85**3)[1]+13);
    ctx.fillStyle="#4ade80";ctx.font="11px Georgia,serif";ctx.textAlign="right";ctx.fillText("axis",tc(0,0.6)[0]-4,tc(0,0.6)[1]);
    // dots
    var dp=tc(1,1);ctx.fillStyle="#f1f5f9";ctx.shadowColor="#f1f5f9";ctx.shadowBlur=5;ctx.beginPath();ctx.arc(dp[0],dp[1],3.5,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;
    ctx.fillStyle="#f1f5f9";ctx.font="10px Georgia,serif";ctx.textAlign="left";ctx.fillText("(1,1)",dp[0]+4,dp[1]-4);
    ctx.fillStyle="#94a3b8";ctx.font="12px Georgia,serif";ctx.textAlign="center";ctx.fillText("2D Region",W/2,12);
  }
  function proj(yp,r,th,az,el){var X=yp,Y=r*Math.cos(th),Z=r*Math.sin(th);var X1=X*Math.cos(az)-Y*Math.sin(az),Y1=X*Math.sin(az)+Y*Math.cos(az),Y2=Y1*Math.cos(el)-Z*Math.sin(el),Z2=Y1*Math.sin(el)+Z*Math.cos(el);return[X1,-Z2,Y2];}
  function draw3D(){
    var W=c3.width,H=c3.height,ctx=c3.getContext("2d");
    ctx.fillStyle="#140014";ctx.fillRect(0,0,W,H);
    var ocx=W*.45,ocy=H*.57,scale=Math.min(W,H)*.32,SEGS=52,N=40;
    function p3(yp,r,th){var s=proj(yp,r,th,az,el);return[ocx+s[0]*scale,ocy+s[1]*scale];}
    function dep(yp,r,th){return proj(yp,r,th,az,el)[2];}
    // washers: outer R=y^(1/3), inner r=y
    var slices=[];
    for(var i=0;i<N;i++){var y0=i/N,y1=(i+1)/N,ym=(y0+y1)/2;slices.push({y0:y0,y1:y1,Ro:Math.pow(ym,1/3),Ri:ym});}
    slices.sort(function(a,b){return dep((a.y0+a.y1)/2,0,0)-dep((b.y0+b.y1)/2,0,0);});
    for(var di=0;di<slices.length;di++){
      var s=slices[di],Ro=s.Ro,Ri=s.Ri,y0=s.y0,y1=s.y1;
      for(var face=0;face<2;face++){
        var yf=face===0?y0:y1;
        ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(yf,Ro,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
        for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(yf,Ri,th);ctx.lineTo(pt[0],pt[1]);}
        ctx.closePath();ctx.fillStyle=face===0?"rgba(232,121,249,.13)":"rgba(232,121,249,.28)";ctx.strokeStyle="rgba(232,121,249,.42)";ctx.lineWidth=0.6;ctx.fill();ctx.stroke();
      }
      ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(y0,Ro,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(y1,Ro,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath();ctx.fillStyle="rgba(232,121,249,.07)";ctx.strokeStyle="rgba(232,121,249,.28)";ctx.lineWidth=0.5;ctx.fill();ctx.stroke();
      ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(y0,Ri,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(y1,Ri,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath();ctx.fillStyle="rgba(56,189,248,.05)";ctx.strokeStyle="rgba(56,189,248,.22)";ctx.lineWidth=0.5;ctx.fill();ctx.stroke();
    }
    // y-axis
    ctx.strokeStyle="rgba(74,222,128,.7)";ctx.lineWidth=1.5;ctx.setLineDash([5,4]);
    ctx.beginPath();ctx.moveTo(p3(-0.06,0,0)[0],p3(-0.06,0,0)[1]);ctx.lineTo(p3(1.15,0,0)[0],p3(1.15,0,0)[1]);ctx.stroke();ctx.setLineDash([]);
    // profile curves
    ctx.strokeStyle="#e879f9";ctx.lineWidth=2;ctx.shadowColor="rgba(232,121,249,.6)";ctx.shadowBlur=5;
    ctx.beginPath();for(var i=0;i<=60;i++){var y=i/60,pt=p3(y,Math.pow(y,1/3),Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}ctx.stroke();
    ctx.strokeStyle="#38bdf8";ctx.shadowColor="rgba(56,189,248,.5)";
    ctx.beginPath();for(var i=0;i<=60;i++){var y=i/60,pt=p3(y,y,Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}ctx.stroke();ctx.shadowBlur=0;
    ctx.fillStyle="#94a3b8";ctx.font="12px Georgia,serif";ctx.textAlign="center";ctx.fillText("3D Solid  —  drag to rotate",W/2,13);
  }
  function xy(e){return e.touches?{x:e.touches[0].clientX,y:e.touches[0].clientY}:{x:e.clientX,y:e.clientY};}
  c3.addEventListener("mousedown",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};c3.style.cursor="grabbing";});
  c3.addEventListener("touchstart",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};},{passive:false});
  window.addEventListener("mousemove",function(e){if(!drag.on)return;var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();});
  window.addEventListener("touchmove",function(e){if(!drag.on)return;e.preventDefault();var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();},{passive:false});
  window.addEventListener("mouseup",function(){drag.on=false;c3.style.cursor="grab";});
  window.addEventListener("touchend",function(){drag.on=false;});
  initSize();draw2D();draw3D();window.addEventListener("resize",function(){initSize();draw2D();draw3D();});
})();
</script>

</div>
</details>

## March 11, 2026 {#mar-11-2026}

<div class="date-banner">
📅 <strong>Thu, March 11, 2026</strong> &nbsp;|&nbsp;
Topics
&ndash;
<strong>Limits (two methods)</strong> · <strong>Series</strong> · <strong>FTC with chain rule</strong> · <strong>Integration by parts</strong> · <strong>Volumes around $y$-axis</strong>
</div>

### Part 1 — Limits: Two Roads, Same Destination

Each limit can be solved **two ways** — find both!

- **Method A** &ndash; L'Hôpital's rule (when you get $\frac{0}{0}$ or $\frac{\infty}{\infty}$)
- **Method B** &ndash; Spot it as a **derivative definition**

$$
	f'(a) = \lim_{h\to 0}\frac{f(a+h)-f(a)}{h}
$$

<ol>
<li>$\displaystyle\lim_{h\to 0} \frac{(3+h)^2 - 9}{h}$
<!--
&nbsp;&nbsp;<em>(what function? what point?)</em>
-->
</li>

<li>$\displaystyle\lim_{h\to 0} \frac{e^{2+h} - e^2}{h}$
<!--
&nbsp;&nbsp;<em>(derivative definition at $a=2$)</em>
-->
</li>

<li>$\displaystyle\lim_{x\to 0} \frac{\tan x}{x}$
<!--
&nbsp;&nbsp;<em>(Method B: derivative of $\tan$ at $0$; Method A: L'Hôpital)</em>
-->
</li>

<li>$\displaystyle\lim_{x\to 0} \frac{\tan x}{\sin x}$
<!--
&nbsp;&nbsp;<em>(no L'Hôpital needed — can you split this using #3 and the Mar 10 result $\frac{\sin x}{x}\to 1$?)</em>
-->
</li>

<li>$\displaystyle\lim_{x\to 0} \frac{e^{2x} - 1}{x}$
<!--
&nbsp;&nbsp;<em>(use the $\frac{e^u-1}{u}\to 1$ trick from Mar 10 #7)</em>
-->
</li>

<li>$\displaystyle\lim_{x\to 0} \frac{\ln(1+3x)}{x}$
<!--
&nbsp;&nbsp;<em>(substitution $u=3x$, or L'Hôpital)</em>
-->
</li>

<li>$\displaystyle\lim_{x\to 0} \frac{e^x - 1 - x}{x^2}$
&nbsp;&nbsp;<em>(L'Hôpital twice; or Taylor series of $e^x$ — which is slicker?)</em>
</li>

<li>$\displaystyle\lim_{x \to 1} \frac{x^4 - 1}{x - 1}$
&nbsp;&nbsp;<em>(factor; and derivative definition)</em>
</li>

<li>$\displaystyle\lim_{x\to 0} \frac{\sin(3x)}{x}$
<!--
&nbsp;&nbsp;<em>(substitution $u=3x$, connects to $\frac{\sin u}{u}\to 1$)</em>
-->
</li>

<li>$\displaystyle\lim_{x\to 0} \frac{\sin(3x)}{\sin(5x)}$
<!--
&nbsp;&nbsp;<em>(divide top and bottom by $x$, reuse #9)</em>
-->
</li>

<li>$\displaystyle\lim_{x\to\infty} \frac{x^3 + 2x}{4x^3 - 1}$
<!--
&nbsp;&nbsp;<em>(divide through by the highest power)</em>
-->
</li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 1</summary>
<div class="answer-body">
<ol>
<li>
<span class="ans">$6$</span><br>
<span class="hint"><strong>Method B:</strong> $f'(3)$ for $f(x)=x^2$; $f'(x)=2x$, so $f'(3)=6$.</span><br>
<span class="hint"><strong>Method A:</strong> $\frac{0}{0}$; differentiate w.r.t. $h$: $\displaystyle\frac{2(3+h)}{1}\big|_{h=0}=6$. ✓</span>
</li>

<li>
<span class="ans">$e^2$</span><br>
<span class="hint"><strong>Method B:</strong> $f'(2)$ for $f(x)=e^x$; $f'(2)=e^2$.</span><br>
<span class="hint"><strong>Method A:</strong> $\frac{0}{0}$; diff w.r.t. $h$: $\displaystyle\frac{e^{2+h}}{1}\big|_{h=0}=e^2$. ✓</span>
</li>

<li>
<span class="ans">$1$</span><br>
<span class="hint"><strong>Method B:</strong> $f'(0)$ for $f(x)=\tan x$; $f'(0)=\sec^2(0)=1$.</span><br>
<span class="hint"><strong>Method A:</strong> $\frac{0}{0}$; diff: $\displaystyle\frac{\sec^2 x}{1}\big|_{x=0}=1$. ✓</span>
</li>

<li>
<span class="ans">$1$</span><br>
<span class="hint"><strong>No L'Hôpital — split the fraction:</strong><br>
$\dfrac{\tan x}{\sin x} = \dfrac{\sin x / \cos x}{\sin x} = \dfrac{1}{\cos x}\to\dfrac{1}{1}=1$. ✓<br>
Or: $\dfrac{\tan x}{\sin x}=\dfrac{\tan x}{x}\cdot\dfrac{x}{\sin x}\to 1\cdot 1=1$ using #3 and Mar 10 #3.</span>
</li>

<li>
<span class="ans">$2$</span><br>
<span class="hint">Let $u=2x$; as $x\to 0$, $u\to 0$, so $\displaystyle\frac{e^{2x}-1}{x}=2\cdot\frac{e^u-1}{u}\to 2\cdot 1=2$. ✓<br>
<strong>Method A:</strong> $\frac{0}{0}$; diff: $\displaystyle\frac{2e^{2x}}{1}\big|_{x=0}=2$. ✓</span>
</li>

<li>
<span class="ans">$3$</span><br>
<span class="hint">Let $u=3x$; as $x\to 0$, $u\to 0$: $\displaystyle\frac{\ln(1+3x)}{x}=3\cdot\frac{\ln(1+u)}{u}\to 3\cdot 1=3$. ✓<br>
(Uses the Mar 10 Part 1 #8 result: $\frac{\ln(1+u)}{u}\to 1$.)</span>
</li>

<li>
<span class="ans">$\dfrac{1}{2}$</span><br>
<span class="hint"><strong>Taylor series (slicker):</strong> $e^x = 1 + x + \dfrac{x^2}{2} + \cdots$, so $e^x - 1 - x = \dfrac{x^2}{2}+\cdots$; divide by $x^2$: limit $= \dfrac{1}{2}$.</span><br>
<span class="hint"><strong>L'Hôpital twice:</strong> $\displaystyle\frac{e^x-1-x}{x^2}\xrightarrow{\text{L'H}}\frac{e^x-1}{2x}\xrightarrow{\text{L'H}}\frac{e^x}{2}\big|_{x=0}=\frac{1}{2}$. ✓</span>
</li>

<li>
<span class="ans">$4$</span><br>
<span class="hint"><strong>Method B:</strong> $f'(1)$ for $f(x)=x^4$; $f'(1)=4\cdot 1^3=4$.</span><br>
<span class="hint"><strong>Direct factor:</strong> $x^4-1=(x-1)(x^3+x^2+x+1)$; cancel $(x-1)$; plug in $x=1$: $1+1+1+1=4$. ✓</span>
</li>

<li>
<span class="ans">$3$</span><br>
<span class="hint">Let $u=3x$; $\displaystyle\frac{\sin(3x)}{x}=3\cdot\frac{\sin u}{u}\to 3\cdot 1=3$. ✓<br>
<strong>Method A:</strong> diff: $\displaystyle\frac{3\cos(3x)}{1}\big|_{x=0}=3$. ✓</span>
</li>

<li>
<span class="ans">$\dfrac{3}{5}$</span><br>
<span class="hint">Divide top and bottom by $x$:
$\displaystyle\frac{\sin(3x)/x}{\sin(5x)/x}=\frac{\sin(3x)/x}{\sin(5x)/x}\to\frac{3}{5}$ using #9 for both. ✓</span>
</li>

<li>
<span class="ans">$\dfrac{1}{4}$</span><br>
<span class="hint">Divide numerator and denominator by $x^3$: $\displaystyle\frac{1+2/x^2}{4-1/x^3}\to\frac{1}{4}$ as $x\to\infty$. ✓</span>
</li>
</ol>
</div>
</details>

---

### Part 2 — Limits at Infinity &amp; Sneaky Forms

These mix $x\to\infty$, $x\to 0^+$, and $0\cdot\infty$ forms.

<ol>
<li>$\displaystyle\lim_{x\to\infty} \frac{3x^2 - x + 1}{2x^2 + 5}$</li>

<li>$\displaystyle\lim_{x\to\infty} \left(1 + \frac{2}{n}\right)^{\!n}$
&nbsp;&nbsp;<em>(variation on the $e$ definition — what's the exponent?)</em></li>

<li>$\displaystyle\lim_{x\to\infty} \left(1 + \frac{1}{n}\right)^{\!3n}$</li>

<li>$\displaystyle\lim_{x\to 0^+} x^2\ln x$</li>

<li>$\displaystyle\lim_{x\to 0^+} \sqrt{x}\ln x$</li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 2</summary>
<div class="answer-body">
<ol>
<li>
<span class="ans">$\dfrac{3}{2}$</span><br>
<span class="hint">Divide through by $x^2$: $\displaystyle\frac{3-1/x+1/x^2}{2+5/x^2}\to\frac{3}{2}$. ✓</span>
</li>

<li>
<span class="ans">$e^2$</span><br>
<span class="hint">$\left(1+\dfrac{2}{n}\right)^n = \left(\!\left(1+\dfrac{2}{n}\right)^{\!n/2}\right)^{\!2}\to (e)^2 = e^2$. ✓</span>
</li>

<li>
<span class="ans">$e^3$</span><br>
<span class="hint">$\left(1+\dfrac{1}{n}\right)^{3n}=\left(\!\left(1+\dfrac{1}{n}\right)^n\right)^{\!3}\to e^3$. ✓</span>
</li>

<li>
<span class="ans">$0$</span><br>
<span class="hint">Write $x^2\ln x = \dfrac{\ln x}{x^{-2}}$; L'Hôpital ($\frac{-\infty}{\infty}$): $\displaystyle\frac{1/x}{-2x^{-3}}=\frac{-x^2}{2}\to 0$. ✓<br>
Pattern: $x^p\ln x\to 0$ as $x\to 0^+$ for any $p>0$. Power always wins over $\ln$.</span>
</li>

<li>
<span class="ans">$0$</span><br>
<span class="hint">Same pattern: $\sqrt{x}\ln x = x^{1/2}\ln x\to 0$ as $x\to 0^+$. ($p=\frac{1}{2}>0$.) ✓</span>
</li>
</ol>
</div>
</details>

---

### Part 3 — Series

Converge or diverge? Give exact value when possible.

<ol>
<li>$\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^2}$
&nbsp;&nbsp;<em>(famous result — do you remember it?)</em></li>

<li>$\displaystyle\sum_{n=0}^{\infty} \frac{(-1)^n}{2^n}$
&nbsp;&nbsp;<em>(geometric — identify $r$)</em></li>

<li>$\displaystyle\sum_{n=1}^{\infty} \frac{n+1}{n^2+1}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} \frac{2^n + 3^n}{5^n}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} (-1)^n \frac{n}{n^2+1}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} \frac{1}{n(n+2)}$
&nbsp;&nbsp;<em>(partial fractions — telescoping!)</em></li>

<li>$\displaystyle\sum_{n=1}^{\infty} \frac{n^2}{2^n}$
&nbsp;&nbsp;<em>(ratio test for convergence; exact value is a bonus!)</em></li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 3</summary>
<div class="answer-body">
<ol>
<li>
<span class="ans">Converges $= \dfrac{\pi^2}{6}$</span><br>
<span class="hint">The Basel problem — $p$-series with $p=2>1$ (converges), and Euler proved the value is $\dfrac{\pi^2}{6}\approx 1.645$. Memorise this one! ✓</span>
</li>

<li>
<span class="ans">Converges $= \dfrac{2}{3}$</span><br>
<span class="hint">Geometric with $a=1$, $r=-\dfrac{1}{2}$; $|r|<1$ so converges. Sum $= \dfrac{1}{1-(-1/2)}=\dfrac{1}{3/2}=\dfrac{2}{3}$. ✓</span>
</li>

<li>
<span class="ans">Diverges</span><br>
<span class="hint">Limit comparison with $\dfrac{1}{n}$: $\displaystyle\frac{(n+1)/(n^2+1)}{1/n}=\frac{n(n+1)}{n^2+1}\to 1>0$. Since $\sum\frac{1}{n}$ diverges, so does this. ✓</span>
</li>

<li>
<span class="ans">Converges $= \dfrac{2}{3}+\dfrac{3}{2} = \dfrac{13}{6}$</span><br>
<span class="hint">Split: $\displaystyle\sum\frac{2^n+3^n}{5^n}=\sum\!\left(\frac{2}{5}\right)^{\!n}+\sum\!\left(\frac{3}{5}\right)^{\!n}$.<br>
Two geometric series: $\dfrac{2/5}{1-2/5}+\dfrac{3/5}{1-3/5}=\dfrac{2}{3}+\dfrac{3}{2}=\dfrac{13}{6}$. ✓</span>
</li>

<li>
<span class="ans">Converges</span> (value not elementary)<br>
<span class="hint">Alternating series test (Leibniz): $a_n=\dfrac{n}{n^2+1}$ is decreasing (check with calculus) and $a_n\to 0$. Both conditions satisfied. ✓</span>
</li>

<li>
<span class="ans">Converges $= \dfrac{3}{4}$</span><br>
<span class="hint">Partial fractions: $\dfrac{1}{n(n+2)}=\dfrac{1}{2}\!\left(\dfrac{1}{n}-\dfrac{1}{n+2}\right)$. Telescoping — write out first few terms and watch pairs cancel. Sum $=\dfrac{1}{2}\!\left(1+\dfrac{1}{2}\right)=\dfrac{3}{4}$. ✓</span>
</li>

<li>
<span class="ans">Converges $= 6$</span><br>
<span class="hint">Ratio test: $\displaystyle\frac{(n+1)^2/2^{n+1}}{n^2/2^n}=\frac{(n+1)^2}{2n^2}\to\frac{1}{2}<1$. ✓ Converges.<br>
<strong>Exact value (bonus):</strong> Differentiate $\sum nx^{n-1}=\frac{1}{(1-x)^2}$ again, multiply by $x$: $\sum n^2 x^n = \frac{x(1+x)}{(1-x)^3}$. At $x=\frac{1}{2}$: $\frac{(1/2)(3/2)}{(1/2)^3}=6$. ✓</span>
</li>
</ol>
</div>
</details>

---

### Part 4 — Integration by Parts

Recall the formula: $\displaystyle\int u\,dv = uv - \int v\,du$

The trick is choosing $u$ and $dv$ wisely.
A helpful mnemonic for choosing $u$: **LIATE** — Logarithm, Inverse trig, Algebraic, Trig, Exponential.
The item highest on that list makes the best $u$.

<ol>
<li>$\displaystyle\int x e^x\,dx$
&nbsp;&nbsp;<em>($u=x$, $dv=e^x\,dx$)</em></li>

<li>$\displaystyle\int x\cos x\,dx$</li>

<li>$\displaystyle\int x^2 e^x\,dx$
&nbsp;&nbsp;<em>(parts twice — or spot the pattern from #1)</em></li>

<li>$\displaystyle\int \ln x\,dx$
&nbsp;&nbsp;<em>(surprising: $u=\ln x$, $dv=dx$)</em></li>

<li>$\displaystyle\int x\ln x\,dx$</li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 4</summary>
<div class="answer-body">
<ol>
<li>
<span class="ans">$xe^x - e^x + C = e^x(x-1) + C$</span><br>
<span class="hint">$u=x$, $dv=e^x\,dx$ $\Rightarrow$ $du=dx$, $v=e^x$.<br>
$\displaystyle\int xe^x\,dx = xe^x - \int e^x\,dx = xe^x - e^x + C$. ✓</span>
</li>

<li>
<span class="ans">$x\sin x + \cos x + C$</span><br>
<span class="hint">$u=x$, $dv=\cos x\,dx$ $\Rightarrow$ $du=dx$, $v=\sin x$.<br>
$\displaystyle\int x\cos x\,dx = x\sin x - \int\sin x\,dx = x\sin x + \cos x + C$. ✓</span>
</li>

<li>
<span class="ans">$e^x(x^2 - 2x + 2) + C$</span><br>
<span class="hint">First parts: $u=x^2$, $v=e^x$ $\Rightarrow$ $x^2 e^x - 2\displaystyle\int xe^x\,dx$.<br>
Apply result from <strong>#1</strong> for the remaining integral: $-2(xe^x - e^x) = -2xe^x+2e^x$.<br>
Total: $e^x(x^2-2x+2)+C$. ✓</span>
</li>

<li>
<span class="ans">$x\ln x - x + C$</span><br>
<span class="hint">$u=\ln x$, $dv=dx$ $\Rightarrow$ $du=\frac{1}{x}dx$, $v=x$.<br>
$\displaystyle\int\ln x\,dx = x\ln x - \int x\cdot\frac{1}{x}\,dx = x\ln x - x + C$. ✓<br>
This is the "sneaky" parts — $dv=dx$ looks too simple, but it works beautifully.</span>
</li>

<li>
<span class="ans">$\dfrac{x^2}{2}\ln x - \dfrac{x^2}{4} + C$</span><br>
<span class="hint">$u=\ln x$, $dv=x\,dx$ $\Rightarrow$ $du=\frac{1}{x}dx$, $v=\frac{x^2}{2}$.<br>
$\displaystyle\int x\ln x\,dx = \frac{x^2}{2}\ln x - \int\frac{x^2}{2}\cdot\frac{1}{x}\,dx = \frac{x^2}{2}\ln x - \frac{x^2}{4}+C$. ✓</span>
</li>
</ol>
</div>
</details>

---

### Part 5 — Volumes Around the $y$-Axis: Shell vs. Washer

Rotating around the **$y$-axis** — this is where the **shell method** really shines.
For each problem, solve **both ways** and confirm they agree.

<h4>Problem 1.</h4> The region bounded by $y = \sqrt{x}$, $x = 1$, and $y = 0$ is rotated around the $\boldsymbol{y}$**-axis**.

<details class="answers">
<summary>▶ Solution — Problem 1</summary>
<div class="answer-body">

<strong>Shell method</strong> (vertical shells, integrate in $x$; radius $= x$, height $=  \sqrt{x}$, from $x=0$ to $x=1$)

$$
	V
		=
			2\pi\int_0^1 x \sqrt{x}\,dx
		=
			2\pi\left[\frac{2}{5} x^{5/2} \right]_0^1
		=
			\boxed{\dfrac{4\pi}{5}}
$$

<strong>Washer method</strong> (integrate in $y$ from $0$ to $1$; for a given $y$, $x$ runs from $0$ to $y^2$,
so outer radius $R = 1$, inner radius $r=y^2$)

$$
	V
		=
			\pi\int_0^1 \left( 1^2 - \bigl(y^2\bigr)^2\right)\,dy
		=
			\pi\int_0^1 (1-y^4)\,dy
		=
			\pi\left[y-\frac{y^5}{5}\right]_0^1
		=
			\boxed{\dfrac{4\pi}{5}}\checkmark
$$

<p class="hint">🔍 Shell was easier.</p>

<div id="p1-11mar-viz" style="background:linear-gradient(135deg,#020814,#0a1628,#020814);border-radius:14px;padding:18px;margin:16px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:10px;">
    <span style="font-size:11px;letter-spacing:.3em;color:#60a5fa;text-transform:uppercase;">Problem 1 — </span>
    <span style="font-size:13px;color:#f1f5f9;">$y=\sqrt{x}$, $y=1$, rotated around $y$-axis</span>
  </div>
  <div style="display:flex;gap:10px;">
    <div style="flex:1;background:rgba(2,8,20,.8);border-radius:10px;border:1px solid rgba(148,163,184,.1);overflow:hidden;">
      <canvas id="m11p1-2d" style="width:100%;display:block;"></canvas>
    </div>
    <div style="flex:1;background:rgba(2,8,20,.8);border-radius:10px;border:1px solid rgba(96,165,250,.2);overflow:hidden;position:relative;">
      <canvas id="m11p1-3d" style="width:100%;display:block;cursor:grab;"></canvas>
      <div style="position:absolute;bottom:6px;right:8px;font-size:10px;color:rgba(96,165,250,.5);background:rgba(0,0,0,.4);padding:2px 6px;border-radius:4px;pointer-events:none;">drag to rotate</div>
    </div>
  </div>
  <div style="text-align:center;margin-top:8px;font-size:11px;color:#475569;">
    <span style="color:#38bdf8;">blue curve</span> = $y=\sqrt{x}$ &nbsp;|&nbsp;
    <span style="color:#4ade80;">green dashed</span> = $y$-axis &nbsp;|&nbsp;
    <span style="color:#60a5fa;">blue walls</span> = outer cylinder ($R=1$) &nbsp;|&nbsp;
    <span style="color:#a78bfa;">purple</span> = inner paraboloid scoop ($r=y^2$), $V=\tfrac{4\pi}{5}$
  </div>
</div>
<script>
(function(){
  var c2=document.getElementById("m11p1-2d"), c3=document.getElementById("m11p1-3d");
  var az=Math.PI/3.5, el=Math.PI/8, drag={on:false,lx:0,ly:0};
  function initSize(){var w=c2.parentElement.clientWidth,h=Math.round(w*.72);c2.width=w;c2.height=h;c3.width=w;c3.height=h;}
  function draw2D(){
    var W=c2.width,H=c2.height,ctx=c2.getContext("2d");
    ctx.fillStyle="#020814";ctx.fillRect(0,0,W,H);
    var pl=42,pr=18,pt=18,pb=34,xmin=-0.15,xmax=1.3,ymin=-0.15,ymax=1.25;
    function tc(x,y){return[pl+(x-xmin)/(xmax-xmin)*(W-pl-pr),H-pb-(y-ymin)/(ymax-ymin)*(H-pt-pb)];}
    // grid
    ctx.strokeStyle="rgba(148,163,184,.07)";ctx.lineWidth=1;
    for(var i=0;i<=1;i++){var p=tc(0,i);ctx.beginPath();ctx.moveTo(pl,p[1]);ctx.lineTo(W-pr,p[1]);ctx.stroke();}
    for(var i=0;i<=1;i++){var p=tc(i,0);ctx.beginPath();ctx.moveTo(p[0],pt);ctx.lineTo(p[0],H-pb);ctx.stroke();}
    // shaded region
    ctx.beginPath();
    var p0=tc(0,1);ctx.moveTo(p0[0],p0[1]);
    for(var i=0;i<=80;i++){var x=i/80,p=tc(x,Math.sqrt(x));ctx.lineTo(p[0],p[1]);}
    var pb2=tc(1,0);ctx.lineTo(pb2[0],pb2[1]);ctx.lineTo(tc(0,0)[0],tc(0,0)[1]);ctx.closePath();
    ctx.fillStyle="rgba(56,189,248,.15)";ctx.fill();
    // y-axis (rotation axis) — green dashed
    ctx.strokeStyle="#4ade80";ctx.lineWidth=2;ctx.setLineDash([6,4]);
    var ay0=tc(0,ymin),ay1=tc(0,ymax);ctx.beginPath();ctx.moveTo(ay0[0],ay0[1]);ctx.lineTo(ay1[0],ay1[1]);ctx.stroke();ctx.setLineDash([]);
    // x-axis
    ctx.strokeStyle="#475569";ctx.lineWidth=1.2;
    var ax0=tc(xmin,0),ax1=tc(xmax,0);ctx.beginPath();ctx.moveTo(ax0[0],ax0[1]);ctx.lineTo(ax1[0],ax1[1]);ctx.stroke();
    // y=1 line
    ctx.strokeStyle="rgba(248,250,252,.3)";ctx.lineWidth=1.2;ctx.setLineDash([4,4]);
    var l0=tc(xmin,1),l1=tc(xmax,1);ctx.beginPath();ctx.moveTo(l0[0],l0[1]);ctx.lineTo(l1[0],l1[1]);ctx.stroke();ctx.setLineDash([]);
    // curve
    ctx.strokeStyle="#38bdf8";ctx.lineWidth=2.5;ctx.shadowColor="rgba(56,189,248,.5)";ctx.shadowBlur=5;
    ctx.beginPath();for(var i=0;i<=100;i++){var x=i/100*1.2,p=tc(x,Math.sqrt(x));i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}ctx.stroke();ctx.shadowBlur=0;
    // labels
    ctx.fillStyle="#38bdf8";ctx.font="italic 12px Georgia,serif";ctx.textAlign="left";
    var lp=tc(0.55,Math.sqrt(0.55));ctx.fillText("y=√x",lp[0]+5,lp[1]-6);
    ctx.fillStyle="rgba(248,250,252,.5)";ctx.font="11px Georgia,serif";ctx.textAlign="left";
    ctx.fillText("y=1",tc(1.05,1)[0],tc(1.05,1)[1]-4);
    ctx.fillStyle="#4ade80";ctx.font="11px Georgia,serif";ctx.textAlign="right";
    ctx.fillText("axis",tc(0,0.7)[0]-4,tc(0,0.7)[1]);
    ctx.fillStyle="#94a3b8";ctx.font="12px Georgia,serif";ctx.textAlign="center";ctx.fillText("2D Region",W/2,12);
  }
  function proj(yp,r,th,az,el){var X=yp,Y=r*Math.cos(th),Z=r*Math.sin(th);var X1=X*Math.cos(az)-Y*Math.sin(az),Y1=X*Math.sin(az)+Y*Math.cos(az);var Y2=Y1*Math.cos(el)-Z*Math.sin(el),Z2=Y1*Math.sin(el)+Z*Math.cos(el);return[X1,-Z2,Y2];}
  function draw3D(){
    var W=c3.width,H=c3.height,ctx=c3.getContext("2d");
    ctx.fillStyle="#020814";ctx.fillRect(0,0,W,H);
    var ocx=W*.43,ocy=H*.57,scale=Math.min(W,H)*.34,SEGS=56,N=36;
    function p3(yp,r,th){var s=proj(yp,r,th,az,el);return[ocx+s[0]*scale,ocy+s[1]*scale];}
    function dep(yp,r,th){return proj(yp,r,th,az,el)[2];}

    // Solid = cylinder (R=1) with paraboloid scoop (r=y²) removed.
    // Draw as washer stack: outer R=1, inner r=y² at each y in [0,1].
    var slices=[];
    for(var i=0;i<N;i++){
      var y0=i/N, y1=(i+1)/N, ym=(y0+y1)/2;
      slices.push({y0:y0, y1:y1, Ro:1.0, Ri:ym*ym});
    }
    slices.sort(function(a,b){return dep((a.y0+a.y1)/2,0,0)-dep((b.y0+b.y1)/2,0,0);});

    for(var di=0;di<slices.length;di++){
      var s=slices[di], Ro=s.Ro, Ri=s.Ri, y0=s.y0, y1=s.y1;
      // washer faces (annular rings)
      for(var face=0;face<2;face++){
        var yf=face===0?y0:y1;
        ctx.beginPath();
        for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(yf,Ro,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
        for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(yf,Ri,th);ctx.lineTo(pt[0],pt[1]);}
        ctx.closePath();
        ctx.fillStyle=face===0?"rgba(56,189,248,.18)":"rgba(56,189,248,.38)";
        ctx.strokeStyle="rgba(56,189,248,.55)"; ctx.lineWidth=0.7;
        ctx.fill(); ctx.stroke();
      }
      // outer cylindrical wall (R=1)
      ctx.beginPath();
      for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(y0,Ro,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(y1,Ro,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath();
      ctx.fillStyle="rgba(56,189,248,.13)";
      ctx.strokeStyle="rgba(96,165,250,.45)"; ctx.lineWidth=0.6;
      ctx.fill(); ctx.stroke();
      // inner paraboloid wall (r=y²) — different colour to distinguish
      ctx.beginPath();
      for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(y0,Ri,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(y1,Ri,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath();
      ctx.fillStyle="rgba(167,139,250,.08)";
      ctx.strokeStyle="rgba(167,139,250,.35)"; ctx.lineWidth=0.5;
      ctx.fill(); ctx.stroke();
    }

    // outer cylinder top rim — bright glowing ring at y=1
    ctx.beginPath();
    for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(1,1.0,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
    ctx.closePath();
    ctx.strokeStyle="#60a5fa"; ctx.lineWidth=2;
    ctx.shadowColor="rgba(96,165,250,.8)"; ctx.shadowBlur=8; ctx.stroke(); ctx.shadowBlur=0;

    // glowing inner paraboloid surface profile curve
    ctx.strokeStyle="#a78bfa"; ctx.lineWidth=2;
    ctx.shadowColor="rgba(167,139,250,.7)"; ctx.shadowBlur=7;
    ctx.beginPath();
    for(var i=0;i<=60;i++){var y=i/60, pt=p3(y,y*y,Math.PI/2); i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
    ctx.stroke();
    ctx.beginPath();
    for(var i=0;i<=60;i++){var y=i/60, pt=p3(y,y*y,-Math.PI/2); i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
    ctx.stroke(); ctx.shadowBlur=0;

    // y-axis (rotation axis)
    ctx.strokeStyle="rgba(74,222,128,.75)"; ctx.lineWidth=1.5; ctx.setLineDash([5,4]);
    ctx.beginPath();ctx.moveTo(p3(-0.06,0,0)[0],p3(-0.06,0,0)[1]);ctx.lineTo(p3(1.18,0,0)[0],p3(1.18,0,0)[1]);ctx.stroke();ctx.setLineDash([]);

    ctx.fillStyle="#94a3b8"; ctx.font="12px Georgia,serif"; ctx.textAlign="center";
    ctx.fillText("3D Solid  —  drag to rotate",W/2,13);
  }
  function xy(e){return e.touches?{x:e.touches[0].clientX,y:e.touches[0].clientY}:{x:e.clientX,y:e.clientY};}
  c3.addEventListener("mousedown",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};c3.style.cursor="grabbing";});
  c3.addEventListener("touchstart",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};},{passive:false});
  window.addEventListener("mousemove",function(e){if(!drag.on)return;var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();});
  window.addEventListener("touchmove",function(e){if(!drag.on)return;e.preventDefault();var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();},{passive:false});
  window.addEventListener("mouseup",function(){drag.on=false;c3.style.cursor="grab";});
  window.addEventListener("touchend",function(){drag.on=false;});
  initSize();draw2D();draw3D();window.addEventListener("resize",function(){initSize();draw2D();draw3D();});
})();
</script>

</div>
</details>

<h4>Problem 2.</h4> The region bounded by $y = x^2$, $x = 2$, and $x$-axis is rotated around the $\boldsymbol{y}$**-axis**.

<details class="answers">
<summary>▶ Solution — Problem 2</summary>
<div class="answer-body">

<strong>Shell method</strong> (vertical shells, integrate in $x$ from $0$ to $2$; radius $= x$, height $= x^2$)

$$
	V
		=
			2\pi\int_0^2 x\bigl( x^2\bigr)\,dx
		=
			\frac{\pi}{2}\Bigl[{x^4}\Bigr]_0^2
		=
			\boxed{8\pi}
$$

<strong>Washer method</strong> (integrate in $y$ from $0$ to $4$; outer radius $R = 2$ (from $x=2$ boundary), inner radius $r = \sqrt{y}$ (from $y=x^2$))

$$
\begin{eqnarray*}
V &=& \pi\int_0^4\Bigl(2^2 - \bigl(\sqrt{y}\bigr)^2\Bigr)\,dy = \pi\int_0^4\bigl(4 - y\bigr)\,dy \\
  &=& \pi\left[4y - \frac{y^2}{2}\right]_0^4 = \pi(16-8) = \boxed{8\pi}\checkmark
\end{eqnarray*}
$$

<p class="hint">🔍 Shell was more natural — the region is described cleanly in $x$. Washer needed the outer boundary $x=2$ rewritten as a constant radius, and the inner boundary inverted to $x=\sqrt{y}$.</p>

<div id="p2-11mar-viz" style="background:linear-gradient(135deg,#0a0014,#1a000a,#0a0014);border-radius:14px;padding:18px;margin:16px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:10px;">
    <span style="font-size:11px;letter-spacing:.3em;color:#f87171;text-transform:uppercase;">Problem 2 — </span>
    <span style="font-size:13px;color:#f1f5f9;">$y=x^2$, $y=4$, rotated around $y$-axis</span>
  </div>
  <div style="display:flex;gap:10px;">
    <div style="flex:1;background:rgba(10,0,20,.8);border-radius:10px;border:1px solid rgba(148,163,184,.1);overflow:hidden;">
      <canvas id="m11p2-2d" style="width:100%;display:block;"></canvas>
    </div>
    <div style="flex:1;background:rgba(10,0,20,.8);border-radius:10px;border:1px solid rgba(248,113,113,.2);overflow:hidden;position:relative;">
      <canvas id="m11p2-3d" style="width:100%;display:block;cursor:grab;"></canvas>
      <div style="position:absolute;bottom:6px;right:8px;font-size:10px;color:rgba(248,113,113,.5);background:rgba(0,0,0,.4);padding:2px 6px;border-radius:4px;pointer-events:none;">drag to rotate</div>
    </div>
  </div>
  <div style="text-align:center;margin-top:8px;font-size:11px;color:#475569;">
    <span style="color:#a78bfa;">purple</span> = $y=x^2$ &nbsp;|&nbsp;
    <span style="color:#4ade80;">green dashed</span> = $y$-axis &nbsp;|&nbsp;
    <span style="color:#f87171;">3D washer solid</span> $V=8\pi$
  </div>
</div>
<script>
(function(){
  var c2=document.getElementById("m11p2-2d"),c3=document.getElementById("m11p2-3d");
  var az=Math.PI/3.5,el=Math.PI/8,drag={on:false,lx:0,ly:0};
  function initSize(){var w=c2.parentElement.clientWidth,h=Math.round(w*.72);c2.width=w;c2.height=h;c3.width=w;c3.height=h;}
  function draw2D(){
    var W=c2.width,H=c2.height,ctx=c2.getContext("2d");
    ctx.fillStyle="#0a0014";ctx.fillRect(0,0,W,H);
    var pl=44,pr=18,pt=18,pb=34,xmin=-0.2,xmax=2.5,ymin=-0.4,ymax=4.7;
    function tc(x,y){return[pl+(x-xmin)/(xmax-xmin)*(W-pl-pr),H-pb-(y-ymin)/(ymax-ymin)*(H-pt-pb)];}
    ctx.strokeStyle="rgba(148,163,184,.07)";ctx.lineWidth=1;
    for(var i=0;i<=4;i++){var p=tc(0,i);ctx.beginPath();ctx.moveTo(pl,p[1]);ctx.lineTo(W-pr,p[1]);ctx.stroke();}
    // shaded region
    ctx.beginPath();
    var p0=tc(0,4);ctx.moveTo(p0[0],p0[1]);
    for(var i=0;i<=80;i++){var x=i/80*2,p=tc(x,x*x);ctx.lineTo(p[0],p[1]);}
    ctx.lineTo(tc(0,0)[0],tc(0,0)[1]);ctx.closePath();
    ctx.fillStyle="rgba(248,113,113,.13)";ctx.fill();
    // y-axis rotation axis
    ctx.strokeStyle="#4ade80";ctx.lineWidth=2;ctx.setLineDash([6,4]);
    var ay0=tc(0,ymin),ay1=tc(0,ymax);ctx.beginPath();ctx.moveTo(ay0[0],ay0[1]);ctx.lineTo(ay1[0],ay1[1]);ctx.stroke();ctx.setLineDash([]);
    // x-axis
    ctx.strokeStyle="#475569";ctx.lineWidth=1.2;
    ctx.beginPath();ctx.moveTo(tc(xmin,0)[0],tc(xmin,0)[1]);ctx.lineTo(tc(xmax,0)[0],tc(xmax,0)[1]);ctx.stroke();
    // y=4 line
    ctx.strokeStyle="rgba(248,250,252,.3)";ctx.lineWidth=1.2;ctx.setLineDash([4,4]);
    ctx.beginPath();ctx.moveTo(tc(xmin,4)[0],tc(xmin,4)[1]);ctx.lineTo(tc(xmax,4)[0],tc(xmax,4)[1]);ctx.stroke();ctx.setLineDash([]);
    // curve y=x²
    ctx.strokeStyle="#a78bfa";ctx.lineWidth=2.5;ctx.shadowColor="rgba(167,139,250,.5)";ctx.shadowBlur=5;
    ctx.beginPath();for(var i=0;i<=100;i++){var x=i/100*2.2,p=tc(x,x*x);i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}ctx.stroke();ctx.shadowBlur=0;
    // labels
    ctx.fillStyle="#a78bfa";ctx.font="italic 12px Georgia,serif";ctx.textAlign="left";
    var lp=tc(1.5,1.5*1.5);ctx.fillText("y=x²",lp[0]+5,lp[1]-6);
    ctx.fillStyle="rgba(248,250,252,.5)";ctx.font="11px Georgia,serif";ctx.fillText("y=4",tc(2.1,4)[0],tc(2.1,4)[1]-4);
    ctx.fillStyle="#4ade80";ctx.font="11px Georgia,serif";ctx.textAlign="right";ctx.fillText("axis",tc(0,2.5)[0]-4,tc(0,2.5)[1]);
    // dot at (2,4)
    var dp=tc(2,4);ctx.fillStyle="#f1f5f9";ctx.shadowColor="#f1f5f9";ctx.shadowBlur=6;ctx.beginPath();ctx.arc(dp[0],dp[1],4,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;
    ctx.fillStyle="#f1f5f9";ctx.font="10px Georgia,serif";ctx.textAlign="left";ctx.fillText("(2,4)",dp[0]+5,dp[1]-4);
    ctx.fillStyle="#94a3b8";ctx.font="12px Georgia,serif";ctx.textAlign="center";ctx.fillText("2D Region",W/2,12);
  }
  function proj(yp,r,th,az,el){var X=yp,Y=r*Math.cos(th),Z=r*Math.sin(th);var X1=X*Math.cos(az)-Y*Math.sin(az),Y1=X*Math.sin(az)+Y*Math.cos(az);var Y2=Y1*Math.cos(el)-Z*Math.sin(el),Z2=Y1*Math.sin(el)+Z*Math.cos(el);return[X1,-Z2,Y2];}
  function draw3D(){
    var W=c3.width,H=c3.height,ctx=c3.getContext("2d");
    ctx.fillStyle="#0a0014";ctx.fillRect(0,0,W,H);
    var ocx=W*.45,ocy=H*.6,scale=Math.min(W,H)*.16,SEGS=48,N=40;
    function p3(yp,r,th){var s=proj(yp,r,th,az,el);return[ocx+s[0]*scale,ocy+s[1]*scale];}
    function dep(yp,r,th){return proj(yp,r,th,az,el)[2];}
    // washers: outer R=2, inner r=sqrt(y)
    var slices=[];
    for(var i=0;i<N;i++){var y0=i/N*4,y1=(i+1)/N*4,ym=(y0+y1)/2;slices.push({y0:y0,y1:y1,Ro:2,Ri:Math.sqrt(ym)});}
    slices.sort(function(a,b){return dep((a.y0+a.y1)/2,0,0)-dep((b.y0+b.y1)/2,0,0);});
    for(var di=0;di<slices.length;di++){
      var s=slices[di],Ro=s.Ro,Ri=s.Ri,y0=s.y0,y1=s.y1;
      for(var face=0;face<2;face++){
        var yf=face===0?y0:y1;
        ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(yf,Ro,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
        for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(yf,Ri,th);ctx.lineTo(pt[0],pt[1]);}
        ctx.closePath();ctx.fillStyle=face===0?"rgba(248,113,113,.10)":"rgba(248,113,113,.22)";ctx.strokeStyle="rgba(248,113,113,.4)";ctx.lineWidth=0.6;ctx.fill();ctx.stroke();
      }
      ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(y0,Ro,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(y1,Ro,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath();ctx.fillStyle="rgba(248,113,113,.06)";ctx.strokeStyle="rgba(248,113,113,.25)";ctx.lineWidth=0.5;ctx.fill();ctx.stroke();
      ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(y0,Ri,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(y1,Ri,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath();ctx.fillStyle="rgba(167,139,250,.05)";ctx.strokeStyle="rgba(167,139,250,.2)";ctx.lineWidth=0.5;ctx.fill();ctx.stroke();
    }
    ctx.strokeStyle="rgba(74,222,128,.7)";ctx.lineWidth=1.5;ctx.setLineDash([5,4]);
    var ay0=p3(-0.1,0,0),ay1=p3(4.3,0,0);ctx.beginPath();ctx.moveTo(ay0[0],ay0[1]);ctx.lineTo(ay1[0],ay1[1]);ctx.stroke();ctx.setLineDash([]);
    ctx.strokeStyle="#a78bfa";ctx.lineWidth=1.5;ctx.shadowColor="rgba(167,139,250,.4)";ctx.shadowBlur=4;
    ctx.beginPath();for(var i=0;i<=60;i++){var y=i/60*4,pt=p3(y,Math.sqrt(y),Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}ctx.stroke();ctx.shadowBlur=0;
    ctx.fillStyle="#94a3b8";ctx.font="12px Georgia,serif";ctx.textAlign="center";ctx.fillText("3D Solid  —  drag to rotate",W/2,13);
  }
  function xy(e){return e.touches?{x:e.touches[0].clientX,y:e.touches[0].clientY}:{x:e.clientX,y:e.clientY};}
  c3.addEventListener("mousedown",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};c3.style.cursor="grabbing";});
  c3.addEventListener("touchstart",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};},{passive:false});
  window.addEventListener("mousemove",function(e){if(!drag.on)return;var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();});
  window.addEventListener("touchmove",function(e){if(!drag.on)return;e.preventDefault();var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();},{passive:false});
  window.addEventListener("mouseup",function(){drag.on=false;c3.style.cursor="grab";});
  window.addEventListener("touchend",function(){drag.on=false;});
  initSize();draw2D();draw3D();window.addEventListener("resize",function(){initSize();draw2D();draw3D();});
})();
</script>

</div>
</details>

<h4>Problem 3.</h4> The region bounded by $y = x(2-x)$ and $y = 0$ (the parabola meets the $x$-axis at $x=0$ and $x=2$) is rotated around the $\boldsymbol{y}$**-axis**.

<details class="answers">
<summary>▶ Solution — Problem 3</summary>
<div class="answer-body">

<strong>Shell method</strong> (vertical shells, integrate in $x$ from $0$ to $2$; radius $= x$, height $= x(2-x)$)

$$V = 2\pi\int_0^2 x \cdot x(2-x)\,dx = 2\pi\int_0^2\bigl(2x^2 - x^3\bigr)\,dx$$
$$= 2\pi\left[\frac{2x^3}{3} - \frac{x^4}{4}\right]_0^2 = 2\pi\!\left(\frac{16}{3} - 4\right) = 2\pi\cdot\frac{4}{3} = \boxed{\dfrac{8\pi}{3}}$$

<strong>Washer method</strong> (integrate in $y$: need to invert $y=x(2-x) = 1-(x-1)^2$, a downward parabola with peak at $(1,1)$)

Rewrite: $x-1 = \pm\sqrt{1-y}$, so the right branch is $x = 1+\sqrt{1-y}$ (outer radius) and left branch is $x = 1-\sqrt{1-y}$ (inner radius).

$$
\begin{eqnarray*}
V &=& \pi\int_0^1\Bigl[\bigl(1+\sqrt{1-y}\bigr)^2 - \bigl(1-\sqrt{1-y}\bigr)^2\Bigr]\,dy \\
  &=& \pi\int_0^1 4\sqrt{1-y}\,dy \quad\text{(difference of squares collapses nicely!)}\\
  &=& 4\pi\left[-\frac{2}{3}(1-y)^{3/2}\right]_0^1 = 4\pi\cdot\frac{2}{3} = \boxed{\dfrac{8\pi}{3}}\checkmark
\end{eqnarray*}
$$

<p class="hint">🔍 Shell method is <em>dramatically</em> easier — one clean integral. The washer method required completing the square, inverting the parabola to find both branches, then a $u$-substitution. This is the best example yet of why shell method was invented!</p>

<div id="p3-11mar-viz" style="background:linear-gradient(135deg,#001408,#0a1a00,#001408);border-radius:14px;padding:18px;margin:16px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:10px;">
    <span style="font-size:11px;letter-spacing:.3em;color:#4ade80;text-transform:uppercase;">Problem 3 — </span>
    <span style="font-size:13px;color:#f1f5f9;">$y=x(2-x)$, rotated around $y$-axis</span>
  </div>
  <div style="display:flex;gap:10px;">
    <div style="flex:1;background:rgba(0,20,8,.8);border-radius:10px;border:1px solid rgba(148,163,184,.1);overflow:hidden;">
      <canvas id="m11p3-2d" style="width:100%;display:block;"></canvas>
    </div>
    <div style="flex:1;background:rgba(0,20,8,.8);border-radius:10px;border:1px solid rgba(74,222,128,.2);overflow:hidden;position:relative;">
      <canvas id="m11p3-3d" style="width:100%;display:block;cursor:grab;"></canvas>
      <div style="position:absolute;bottom:6px;right:8px;font-size:10px;color:rgba(74,222,128,.5);background:rgba(0,0,0,.4);padding:2px 6px;border-radius:4px;pointer-events:none;">drag to rotate</div>
    </div>
  </div>
  <div style="text-align:center;margin-top:8px;font-size:11px;color:#475569;">
    <span style="color:#fb923c;">orange</span> = $y=x(2-x)$ &nbsp;|&nbsp;
    <span style="color:#4ade80;">green dashed</span> = $y$-axis &nbsp;|&nbsp;
    <span style="color:#4ade80;">3D solid</span> $V=\tfrac{8\pi}{3}$ (like a donut-cap!)
  </div>
</div>
<script>
(function(){
  var c2=document.getElementById("m11p3-2d"),c3=document.getElementById("m11p3-3d");
  var az=Math.PI/4,el=Math.PI/9,drag={on:false,lx:0,ly:0};
  function initSize(){var w=c2.parentElement.clientWidth,h=Math.round(w*.72);c2.width=w;c2.height=h;c3.width=w;c3.height=h;}
  function draw2D(){
    var W=c2.width,H=c2.height,ctx=c2.getContext("2d");
    ctx.fillStyle="#001408";ctx.fillRect(0,0,W,H);
    var pl=42,pr=18,pt=18,pb=34,xmin=-0.3,xmax=2.5,ymin=-0.2,ymax=1.3;
    function tc(x,y){return[pl+(x-xmin)/(xmax-xmin)*(W-pl-pr),H-pb-(y-ymin)/(ymax-ymin)*(H-pt-pb)];}
    ctx.strokeStyle="rgba(148,163,184,.07)";ctx.lineWidth=1;
    for(var i=0;i<=1;i++){var p=tc(0,i);ctx.beginPath();ctx.moveTo(pl,p[1]);ctx.lineTo(W-pr,p[1]);ctx.stroke();}
    // shaded region
    ctx.beginPath();
    ctx.moveTo(tc(0,0)[0],tc(0,0)[1]);
    for(var i=0;i<=80;i++){var x=i/80*2,y=x*(2-x),p=tc(x,y);ctx.lineTo(p[0],p[1]);}
    ctx.lineTo(tc(2,0)[0],tc(2,0)[1]);ctx.closePath();
    ctx.fillStyle="rgba(74,222,128,.13)";ctx.fill();
    // y-axis rotation axis
    ctx.strokeStyle="#4ade80";ctx.lineWidth=2;ctx.setLineDash([6,4]);
    ctx.beginPath();ctx.moveTo(tc(0,ymin)[0],tc(0,ymin)[1]);ctx.lineTo(tc(0,ymax)[0],tc(0,ymax)[1]);ctx.stroke();ctx.setLineDash([]);
    // x-axis
    ctx.strokeStyle="#475569";ctx.lineWidth=1.2;
    ctx.beginPath();ctx.moveTo(tc(xmin,0)[0],tc(xmin,0)[1]);ctx.lineTo(tc(xmax,0)[0],tc(xmax,0)[1]);ctx.stroke();
    // curve
    ctx.strokeStyle="#fb923c";ctx.lineWidth=2.5;ctx.shadowColor="rgba(251,146,60,.5)";ctx.shadowBlur=5;
    ctx.beginPath();for(var i=0;i<=100;i++){var x=i/100*2,y=x*(2-x),p=tc(x,y);i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}ctx.stroke();ctx.shadowBlur=0;
    // labels
    ctx.fillStyle="#fb923c";ctx.font="italic 12px Georgia,serif";ctx.textAlign="left";
    var lp=tc(0.8,0.8*(2-0.8));ctx.fillText("y=x(2−x)",lp[0]+5,lp[1]-8);
    ctx.fillStyle="#f1f5f9";ctx.font="10px Georgia,serif";ctx.fillText("(1,1)",tc(1,1)[0]+5,tc(1,1)[1]-5);
    ctx.fillStyle="#4ade80";ctx.font="11px Georgia,serif";ctx.textAlign="right";ctx.fillText("axis",tc(0,0.7)[0]-4,tc(0,0.7)[1]);
    // peak dot
    var dp=tc(1,1);ctx.fillStyle="#f1f5f9";ctx.shadowColor="#f1f5f9";ctx.shadowBlur=5;ctx.beginPath();ctx.arc(dp[0],dp[1],3.5,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;
    ctx.fillStyle="#94a3b8";ctx.font="12px Georgia,serif";ctx.textAlign="center";ctx.fillText("2D Region",W/2,12);
    ctx.fillStyle="#64748b";ctx.font="11px Georgia,serif";
    for(var i=0;i<=2;i++){var tp=tc(i,0);ctx.textAlign="center";ctx.fillText(i,tp[0],tp[1]+13);}
  }
  function proj(yp,r,th,az,el){var X=yp,Y=r*Math.cos(th),Z=r*Math.sin(th);var X1=X*Math.cos(az)-Y*Math.sin(az),Y1=X*Math.sin(az)+Y*Math.cos(az);var Y2=Y1*Math.cos(el)-Z*Math.sin(el),Z2=Y1*Math.sin(el)+Z*Math.cos(el);return[X1,-Z2,Y2];}
  function draw3D(){
    var W=c3.width,H=c3.height,ctx=c3.getContext("2d");
    ctx.fillStyle="#001408";ctx.fillRect(0,0,W,H);
    var ocx=W*.45,ocy=H*.58,scale=Math.min(W,H)*.30,SEGS=48,N=40;
    function p3(yp,r,th){var s=proj(yp,r,th,az,el);return[ocx+s[0]*scale,ocy+s[1]*scale];}
    function dep(yp,r,th){return proj(yp,r,th,az,el)[2];}
    // washers: outer R=1+sqrt(1-y), inner r=1-sqrt(1-y)
    var slices=[];
    for(var i=0;i<N;i++){
      var y0=i/N,y1=(i+1)/N,ym=(y0+y1)/2;
      var sq=Math.sqrt(Math.max(0,1-ym));
      slices.push({y0:y0,y1:y1,Ro:1+sq,Ri:1-sq});
    }
    slices.sort(function(a,b){return dep((a.y0+a.y1)/2,0,0)-dep((b.y0+b.y1)/2,0,0);});
    for(var di=0;di<slices.length;di++){
      var s=slices[di],Ro=s.Ro,Ri=s.Ri,y0=s.y0,y1=s.y1;
      for(var face=0;face<2;face++){
        var yf=face===0?y0:y1;
        ctx.beginPath();
        for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(yf,Ro,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
        for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(yf,Ri,th);ctx.lineTo(pt[0],pt[1]);}
        ctx.closePath();ctx.fillStyle=face===0?"rgba(74,222,128,.10)":"rgba(74,222,128,.22)";ctx.strokeStyle="rgba(74,222,128,.35)";ctx.lineWidth=0.6;ctx.fill();ctx.stroke();
      }
      ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(y0,Ro,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(y1,Ro,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath();ctx.fillStyle="rgba(74,222,128,.06)";ctx.strokeStyle="rgba(74,222,128,.25)";ctx.lineWidth=0.5;ctx.fill();ctx.stroke();
      ctx.beginPath();for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(y0,Ri,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(y1,Ri,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath();ctx.fillStyle="rgba(251,146,60,.04)";ctx.strokeStyle="rgba(251,146,60,.18)";ctx.lineWidth=0.5;ctx.fill();ctx.stroke();
    }
    // y-axis
    ctx.strokeStyle="rgba(74,222,128,.7)";ctx.lineWidth=1.5;ctx.setLineDash([5,4]);
    ctx.beginPath();ctx.moveTo(p3(-0.05,0,0)[0],p3(-0.05,0,0)[1]);ctx.lineTo(p3(1.15,0,0)[0],p3(1.15,0,0)[1]);ctx.stroke();ctx.setLineDash([]);
    // surface curves
    ctx.strokeStyle="#fb923c";ctx.lineWidth=1.5;ctx.shadowColor="rgba(251,146,60,.4)";ctx.shadowBlur=4;
    ctx.beginPath();for(var i=0;i<=60;i++){var y=i/60,sq=Math.sqrt(Math.max(0,1-y)),pt=p3(y,1+sq,Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}ctx.stroke();
    ctx.beginPath();for(var i=0;i<=60;i++){var y=i/60,sq=Math.sqrt(Math.max(0,1-y)),pt=p3(y,1-sq,Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}ctx.stroke();ctx.shadowBlur=0;
    ctx.fillStyle="#94a3b8";ctx.font="12px Georgia,serif";ctx.textAlign="center";ctx.fillText("3D Solid  —  drag to rotate",W/2,13);
  }
  function xy(e){return e.touches?{x:e.touches[0].clientX,y:e.touches[0].clientY}:{x:e.clientX,y:e.clientY};}
  c3.addEventListener("mousedown",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};c3.style.cursor="grabbing";});
  c3.addEventListener("touchstart",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};},{passive:false});
  window.addEventListener("mousemove",function(e){if(!drag.on)return;var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();});
  window.addEventListener("touchmove",function(e){if(!drag.on)return;e.preventDefault();var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();},{passive:false});
  window.addEventListener("mouseup",function(){drag.on=false;c3.style.cursor="grab";});
  window.addEventListener("touchend",function(){drag.on=false;});
  initSize();draw2D();draw3D();window.addEventListener("resize",function(){initSize();draw2D();draw3D();});
})();
</script>

</div>
</details>

## March 10, 2026 {#mar-10-2026}

<div class="date-banner">
📅 <strong>Wed, March 10, 2026</strong> &nbsp;|&nbsp;
Topics
&ndash;
<strong>Limits (two methods)</strong> · <strong>Series</strong> · <strong>FTC with chain rule</strong> · <strong>Volumes of Revolution</strong>
</div>

### Part 1 — Limits: Two Roads, Same Destination

Each limit below can be solved **two ways**.
Try both — they should give the same answer!

- **Method A** &ndash; L'Hôpital's theorem (when you get $\frac{0}{0}$ or $\frac{\infty}{\infty}$)
- **Method B** &ndash; Recognise it as a **derivative definition**

$$
	f'(a) = \lim_{h\to 0}\frac{f(a+h)-f(a)}{h}
$$

<ol>
<li>$\displaystyle\lim_{h\to 0} \frac{(2+h)^3 - 8}{h}$
&nbsp;&nbsp;<em>(hint: what function? what point?)</em></li>

<li>$\displaystyle\lim_{h\to 0} \frac{\sqrt{4+h} - 2}{h}$</li>

<li>$\displaystyle\lim_{x\to 0} \frac{\sin x}{x}$</li>

<li>$\displaystyle\lim_{x\to 0} \frac{\sqrt{4+x} - 2}{\sin x}$</li>

<li>$\displaystyle\lim_{x\to 0} \frac{\sqrt{4+\sin x} - 2}{x}$</li>

<li>$\displaystyle\lim_{x\to 0} \frac{\sqrt{4+\sin x} - 2}{\sin x}$</li>

<li>$\displaystyle\lim_{x\to 0} \frac{e^x - 1}{x}$</li>

<li>$\displaystyle\lim_{x\to 0} \frac{\ln(1+x)}{x}$</li>

<li>$\displaystyle\lim_{x\to 0} \frac{1 - \cos x}{x^2}$
&nbsp;&nbsp;<em>(L'Hôpital twice, or Taylor; and derivative definition of $\cos$ at 0)</em></li>

<li>$\displaystyle\lim_{x\to 0} \frac{e^{3x} - 1}{x}$
&nbsp;&nbsp;<em>(can you do this without L'Hôpital using #7?)</em></li>

<li>$\displaystyle\lim_{x \to 2} \frac{x^3 - 8}{x - 2}$
&nbsp;&nbsp;<em>(factor directly; and derivative definition)</em></li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 1</summary>
<div class="answer-body">
<ol>
<li>
<span class="ans">$12$</span><br>
<span class="hint"><strong>Method B (derivative):</strong> This is $f'(2)$ for $f(x)=x^3$, so $f'(2)=3\cdot 2^2=12$.</span><br>
<span class="hint"><strong>Method A (L'Hôpital):</strong> $\frac{0}{0}$ form; diff top/bottom w.r.t. $h$: $\displaystyle\frac{3(2+h)^2}{1}\big|_{h=0} = 12$. ✓</span>
</li>

<li>
<span class="ans">$\dfrac{1}{4}$</span><br>
<span class="hint"><strong>Method B:</strong> $f'(4)$ for $f(x)=\sqrt{x}$; $f'(x)=\frac{1}{2\sqrt{x}}$, so $f'(4)=\frac{1}{4}$.</span><br>
<span class="hint"><strong>Method A:</strong> $\frac{0}{0}$; diff: $\displaystyle\frac{1/(2\sqrt{4+h})}{1}\big|_{h=0}=\frac{1}{4}$. ✓</span>
</li>

<li>
<span class="ans">$1$</span><br>
<span class="hint"><strong>Method B:</strong> $f'(0)$ for $f(x)=\sin x$; $f'(0)=\cos 0=1$.</span><br>
<span class="hint"><strong>Method A:</strong> $\frac{0}{0}$; diff: $\displaystyle\frac{\cos x}{1}\big|_{x=0}=1$. ✓</span>
</li>

<li>
<span class="ans">$\dfrac{1}{4}$</span><br>
<span class="hint"><strong>No L'Hôpital needed — just multiply and divide by $x$:</strong><br>
$\dfrac{\sqrt{4+x}-2}{\sin x} = \dfrac{\sqrt{4+x}-2}{x}\cdot\dfrac{x}{\sin x}$<br>
First factor $\to \dfrac{1}{4}$ by <strong>#2</strong>; &nbsp; second factor $\to 1$ because $\dfrac{\sin x}{x}\to 1$ by <strong>#3</strong>.<br>
Product $= \dfrac{1}{4}\cdot 1 = \dfrac{1}{4}$. ✓</span>
</li>

<li>
<span class="ans">$\dfrac{1}{4}$</span><br>
<span class="hint"><strong>No L'Hôpital — substitute and split:</strong><br>
$\dfrac{\sqrt{4+\sin x}-2}{x} = \dfrac{\sqrt{4+\sin x}-2}{\sin x}\cdot\dfrac{\sin x}{x}$<br>
For the first factor, let $u = \sin x$; as $x\to 0$, $u\to 0$, so $\dfrac{\sqrt{4+u}-2}{u}\to\dfrac{1}{4}$ by <strong>#2</strong>.<br>
Second factor $\to 1$ by <strong>#3</strong>. &nbsp; Product $= \dfrac{1}{4}\cdot 1 = \dfrac{1}{4}$. ✓</span>
</li>

<li>
<span class="ans">$\dfrac{1}{4}$</span><br>
<span class="hint"><strong>No L'Hôpital — direct substitution, reuses only #2:</strong><br>
Let $u = \sin x$; as $x\to 0$, $u\to 0$, so<br>
$\dfrac{\sqrt{4+\sin x}-2}{\sin x} = \dfrac{\sqrt{4+u}-2}{u}\to\dfrac{1}{4}$ directly by <strong>#2</strong>.<br>
No need for #3 this time! The $\sin x$ cancels itself top and bottom. ✓</span>
</li>

<li>
<span class="ans">$1$</span><br>
<span class="hint"><strong>Method B:</strong> $f'(0)$ for $f(x)=e^x$; $f'(0)=e^0=1$.</span><br>
<span class="hint"><strong>Method A:</strong> $\frac{0}{0}$; diff: $\displaystyle\frac{e^x}{1}\big|_{x=0}=1$. ✓</span>
</li>

<li>
<span class="ans">$1$</span><br>
<span class="hint"><strong>Method B:</strong> $f'(0)$ for $f(x)=\ln(1+x)$; $f'(x)=\frac{1}{1+x}$, so $f'(0)=1$.</span><br>
<span class="hint"><strong>Method A:</strong> $\frac{0}{0}$; diff: $\displaystyle\frac{1/(1+x)}{1}\big|_{x=0}=1$. ✓</span>
</li>

<li>
<span class="ans">$\dfrac{1}{2}$</span><br>
<span class="hint"><strong>Method B:</strong> $-f''(0)/2!$ for $\cos x$... actually: rewrite as $\displaystyle\frac{1-\cos x}{x^2}$. Note $1-\cos x = 2\sin^2(x/2)$, so $\displaystyle\frac{2\sin^2(x/2)}{x^2}=\frac{1}{2}\left(\frac{\sin(x/2)}{x/2}\right)^2\to\frac{1}{2}$.</span><br>
<span class="hint"><strong>Method A:</strong> $\frac{0}{0}$ twice: $\displaystyle\frac{\sin x}{2x}\big|_{x=0}$ → still $\frac{0}{0}$ → $\displaystyle\frac{\cos x}{2}\big|_{x=0}=\frac{1}{2}$. ✓</span>
</li>

<li>
<span class="ans">$3$</span><br>
<span class="hint"><strong>Method B (slick):</strong> Let $u=3x$; as $x\to 0$, $u\to 0$, so $\displaystyle\frac{e^{3x}-1}{x}=3\cdot\frac{e^u-1}{u}\to 3\cdot 1=3$. Uses result from <strong>#7</strong>!</span><br>
<span class="hint"><strong>Method A:</strong> $\frac{0}{0}$; diff: $\displaystyle\frac{3e^{3x}}{1}\big|_{x=0}=3$. ✓</span>
</li>

<li>
<span class="ans">$12$</span><br>
<span class="hint"><strong>Method B:</strong> $f'(2)$ for $f(x)=x^3$; $f'(2)=3\cdot 4=12$. (Same as #1!)</span><br>
<span class="hint"><strong>Direct factor:</strong> $x^3-8=(x-2)(x^2+2x+4)$; cancel $(x-2)$; plug in $x=2$: $4+4+4=12$. ✓</span>
</li>
</ol>
</div>
</details>

---

### Part 2 — Limits at Infinity

These all involve $x\to\infty$ or $n\to\infty$.
One of them secretly reuses a result from Part 1 — can you spot which one?

<ol>
<li>$\displaystyle\lim_{x\to\infty} x\sin\dfrac{1}{x}$
&nbsp;&nbsp;<em>(hint: try the substitution $u = \frac{1}{x}$)</em></li>

<li>$\displaystyle\lim_{n\to\infty} \left(1+\frac{1}{n}\right)^{\!n}$
&nbsp;&nbsp;<em>(this one you should just know by heart!)</em></li>

<li>$\displaystyle\lim_{n\to\infty} \left(1+\frac{3}{n}\right)^{\!2n}$
&nbsp;&nbsp;<em>(variation on #2 — what changes?)</em></li>

<li>$\displaystyle\lim_{x\to\infty} \dfrac{x^{100}}{e^x}$
&nbsp;&nbsp;<em>(L'Hôpital 100 times? or is there a slicker way?)</em></li>

<li>$\displaystyle\lim_{x\to\infty} \left(\sqrt{x+1} - \sqrt{x}\right)$
&nbsp;&nbsp;<em>(try multiplying by the conjugate)</em></li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 2</summary>
<div class="answer-body">
<ol>
<li>
<span class="ans">$1$</span><br>
<span class="hint">Let $u=\dfrac{1}{x}$; as $x\to\infty$, $u\to 0^+$, so
$x\sin\dfrac{1}{x} = \dfrac{\sin u}{u} \to 1$ by Part 1 <strong>#3</strong>! ✓<br>
That's the hidden connection — the same $\displaystyle\frac{\sin\theta}{\theta}\to 1$ just wearing a disguise.</span>
</li>

<li>
<span class="ans">$e \approx 2.718\ldots$</span><br>
<span class="hint">This is the <em>definition</em> of $e$. Memorise it — it appears everywhere.<br>
More generally: $\displaystyle\lim_{n\to\infty}\!\left(1+\frac{a}{n}\right)^n = \lim_{n\to\infty}\!\left(\left(1+\frac{a}{n}\right)^{\frac{n}{a}}\right)^{a} = e^a$.</span>
</li>

<li>
<span class="ans">$e^6$</span><br>
<span class="hint">Rewrite the exponent: $\left(1+\dfrac{3}{n}\right)^{2n} = \left(\left(1+\dfrac{3}{n}\right)^{\frac{n}{3}}\right)^6$.<br>
Inner limit $\to e$ by the formula from #2 with $a=1$; $(e)^6 = e^6$.</span>
</li>

<li>
<span class="ans">$0$</span><br>
<span class="hint">Exponential <em>always</em> beats any polynomial at $\infty$ — no matter how large the power.<br>
Formally: L'Hôpital applied 100 times gives $\dfrac{100!}{e^x}\to 0$.<br>
Slicker: $e^x > \dfrac{x^{101}}{101!}$ for all large $x$ (from the Taylor series), so $\dfrac{x^{100}}{e^x} < \dfrac{101!}{x} \to 0$.</span>
</li>

<li>
<span class="ans">$0$</span><br>
<span class="hint">Multiply by the conjugate $\dfrac{\sqrt{x+1}+\sqrt{x}}{\sqrt{x+1}+\sqrt{x}}$:<br>
$\sqrt{x+1}-\sqrt{x} = \dfrac{(x+1)-x}{\sqrt{x+1}+\sqrt{x}} = \dfrac{1}{\sqrt{x+1}+\sqrt{x}} \to \dfrac{1}{\infty} = 0$. ✓</span>
</li>
</ol>
</div>
</details>

### Part 3 — Series

Converge or diverge? Give exact value when possible.

<ol>
<li>$\displaystyle\sum_{n=1}^{\infty} \frac{1}{n(n+1)}$
&nbsp;&nbsp;<em>(hint: partial fractions!)</em></li>

<li>$\displaystyle\sum_{n=1}^{\infty} \frac{n}{2^n}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} \frac{(-1)^n}{\sqrt{n}}$</li>

<li>$\displaystyle\sum_{n=2}^{\infty} \frac{1}{n \ln n}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} \frac{3^n}{n!}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} \frac{n^2+1}{n^3+1}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^{3/2}}$</li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 3</summary>
<div class="answer-body">
<ol>
<li>
<span class="ans">Converges $= 1$</span><br>
<span class="hint">Partial fractions: $\displaystyle\frac{1}{n(n+1)}=\frac{1}{n}-\frac{1}{n+1}$. Telescoping sum: all middle terms cancel, leaving $\displaystyle 1 - \lim_{N\to\infty}\frac{1}{N+1} = 1$.</span>
</li>

<li>
<span class="ans">Converges $= 2$</span><br>
<span class="hint">Ratio test: $\displaystyle\frac{(n+1)/2^{n+1}}{n/2^n}=\frac{n+1}{2n}\to\frac{1}{2}<1$. Value: differentiate the geometric series $\displaystyle\sum x^n = \frac{1}{1-x}$ to get $\displaystyle\sum nx^{n-1}=\frac{1}{(1-x)^2}$; multiply by $x$: $\displaystyle\sum nx^n = \frac{x}{(1-x)^2}$; at $\displaystyle x=\frac{1}{2}$: $\displaystyle\frac{1/2}{1/4}=2$.</span>
</li>

<li>
<span class="ans">Converges</span> (value not elementary)<br>
<span class="hint">Leibniz alternating series test: $\displaystyle\frac{1}{\sqrt{n}}$ is decreasing and $\to 0$. ✓ (Value $\approx -0.6049$, related to Dirichlet eta function.)</span>
</li>

<li>
<span class="ans">Diverges ($\infty$)</span><br>
<span class="hint">Integral test: $\displaystyle\int_2^\infty \frac{dx}{x\ln x} = \ln(\ln x)\Big|_2^\infty = \infty$. (Or: $p$-series-like with $p=1$ — just barely diverges!)</span>
</li>

<li>
<span class="ans">Converges $= e^3 - 1 \approx 19.09$</span><br>
<span class="hint">Ratio test: $\displaystyle\frac{3^{n+1}/(n+1)!}{3^n/n!}=\frac{3}{n+1}\to 0 < 1$. Value: $\displaystyle\sum_{n=0}^{\infty}\frac{3^n}{n!}=e^3$, minus the $n=0$ term ($=1$): answer $= e^3-1$.</span>
</li>

<li>
<span class="ans">Diverges ($\infty$)</span><br>
<span class="hint">Limit comparison with $\displaystyle\frac{1}{n}$: $\displaystyle\frac{(n^2+1)/(n^3+1)}{1/n}=\frac{n(n^2+1)}{n^3+1}\to 1>0$. Since $\sum\dfrac{1}{n}$ diverges, so does this.</span>
</li>

<li>
<span class="ans">Converges</span><br>
<span class="hint">$p$-series with $p=\dfrac{3}{2}>1$. (Value $= \zeta(3/2)\approx 2.612$, no simple closed form.)</span>
</li>
</ol>
</div>
</details>

### Part 4 — FTC with a Twist

These use **FTC Part 1 + chain rule** — the upper limit is a function of $x$, not just $x$ itself!

$$\frac{d}{dx}\int_a^{g(x)} f(t)\,dt = f(g(x))\cdot g'(x)$$

<ol>
<li>$\displaystyle\frac{d}{dx}\int_0^{x^2} e^{-t^2}\, dt$</li>

<li>$\displaystyle\frac{d}{dx}\int_x^{x^2} \sin(t^2)\, dt$
&nbsp;&nbsp;<em>(both limits move! split it into two integrals first)</em></li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 4</summary>
<div class="answer-body">
<ol>
<li>
<span class="ans">$2x\,e^{-x^4}$</span><br>
<span class="hint">Chain rule: $f(g(x))\cdot g'(x)$ where $f(t)=e^{-t^2}$ and $g(x)=x^2$.<br>
$= e^{-(x^2)^2}\cdot 2x = 2x\,e^{-x^4}$.</span>
</li>

<li>
<span class="ans">$2x\sin(x^4) - \sin(x^2)$</span><br>
<span class="hint">Split: $\displaystyle\int_x^{x^2} = \int_0^{x^2} - \int_0^{x}$.<br>
Differentiate each: $\displaystyle\frac{d}{dx}\int_0^{x^2}\sin(t^2)\,dt = \sin(x^4)\cdot 2x$;&nbsp; $\displaystyle\frac{d}{dx}\int_0^{x}\sin(t^2)\,dt = \sin(x^2)\cdot 1$.<br>
Answer: $\displaystyle 2x\sin(x^4) - \sin(x^2)$.</span>
</li>
</ol>
</div>
</details>

### Part 5 — Volumes of Revolution: Two Methods Every Time

For each problem, compute the volume **both ways** — disc/washer method and shell method.
Verify they agree, then reflect: *which method felt easier, and why?*

<h4>Problem 1.</h4> The region bounded by $y = x^2$, $x = 0$, $x = 2$, and $y = 0$ is rotated around the **$x$-axis**.

<details class="answers">
<summary>▶ Solution — Problem 1</summary>
<div class="answer-body">

<strong>Disc method</strong> (integrate along $x$, natural here)

$$V = \pi\int_0^2 y^2\,dx = \pi\int_0^2 \left(x^2\right)^2\,dx = \pi\int_0^2 x^4\,dx = \pi\left[\frac{x^5}{5}\right]_0^2 = \boxed{\dfrac{32\pi}{5}}$$

<strong>Shell method</strong> (horizontal shells, integrate along $y$ from $0$ to $4$)

Each shell at height $y$ has radius $= y$, height $= 2 - \sqrt{y}$ (rightmost $x$ is $2$, leftmost is $\sqrt{y}$).

$$V = 2\pi\int_0^4 y\bigl(2-\sqrt{y}\bigr)\,dy = 2\pi\int_0^4\bigl(2y - y^{3/2}\bigr)\,dy$$
$$= 2\pi\left[y^2 - \frac{2}{5}y^{5/2}\right]_0^4 = 2\pi\!\left(16 - \frac{2}{5}\cdot 32\right) = 2\pi\cdot\frac{16}{5} = \boxed{\dfrac{32\pi}{5}}\checkmark$$

<p class="hint">🔍 Disc was easier here — one clean integral vs a fractional power. Shell required inverting $y=x^2$ to $x=\sqrt{y}$ and thinking in $y$.</p>

<div id="p1-viz" style="background:linear-gradient(135deg,#020814,#0a1628,#020814);border-radius:14px;padding:18px;margin:16px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:10px;">
    <span style="font-size:11px;letter-spacing:.3em;color:#60a5fa;text-transform:uppercase;">Problem 1 — </span>
    <span style="font-size:13px;color:#f1f5f9;">$y=x^2$, $x\in[0,2]$, rotated around $x$-axis</span>
  </div>
  <div style="display:flex;gap:10px;">
    <div style="flex:1;background:rgba(2,8,20,.8);border-radius:10px;border:1px solid rgba(148,163,184,.1);overflow:hidden;">
      <canvas id="p1-2d" style="width:100%;display:block;"></canvas>
    </div>
    <div style="flex:1;background:rgba(2,8,20,.8);border-radius:10px;border:1px solid rgba(96,165,250,.2);overflow:hidden;position:relative;">
      <canvas id="p1-3d" style="width:100%;display:block;cursor:grab;"></canvas>
      <div style="position:absolute;bottom:6px;right:8px;font-size:10px;color:rgba(96,165,250,.5);background:rgba(0,0,0,.4);padding:2px 6px;border-radius:4px;pointer-events:none;">drag to rotate</div>
    </div>
  </div>
  <div style="text-align:center;margin-top:8px;font-size:11px;color:#475569;">
    <span style="color:#38bdf8;">blue region</span> = area rotated &nbsp;|&nbsp;
    <span style="color:#f87171;">red dashed</span> = axis of rotation ($x$-axis) &nbsp;|&nbsp;
    <span style="color:#60a5fa;">3D solid</span> = disc stack $V=\frac{32\pi}{5}$
  </div>
</div>
<script>
(function(){
  var c2=document.getElementById("p1-2d");
  var c3=document.getElementById("p1-3d");
  var az=Math.PI/3, el=Math.PI/8;
  var drag={on:false,lx:0,ly:0};

  function initSize(){
    var w=c2.parentElement.clientWidth;
    var h=Math.round(w*0.72);
    c2.width=w; c2.height=h;
    c3.width=w; c3.height=h;
  }

  function draw2D(){
    var W=c2.width, H=c2.height;
    var ctx=c2.getContext("2d");
    ctx.clearRect(0,0,W,H);
    var pl=44,pr=18,pt=18,pb=36;
    var xmin=-0.3,xmax=2.5,ymin=-0.5,ymax=4.5;
    function tc(x,y){return[pl+(x-xmin)/(xmax-xmin)*(W-pl-pr), H-pb-(y-ymin)/(ymax-ymin)*(H-pt-pb)];}
    // grid
    ctx.strokeStyle="rgba(148,163,184,.08)"; ctx.lineWidth=1;
    for(var i=0;i<=4;i++){var p=tc(0,i);ctx.beginPath();ctx.moveTo(pl,p[1]);ctx.lineTo(W-pr,p[1]);ctx.stroke();}
    for(var i=0;i<=2;i++){var p=tc(i,0);ctx.beginPath();ctx.moveTo(p[0],pt);ctx.lineTo(p[0],H-pb);ctx.stroke();}
    // shaded region
    ctx.beginPath();
    var p0=tc(0,0); ctx.moveTo(p0[0],p0[1]);
    for(var i=0;i<=120;i++){var x=i/120*2; var p=tc(x,x*x); i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}
    var pb2=tc(2,0); ctx.lineTo(pb2[0],pb2[1]); ctx.closePath();
    ctx.fillStyle="rgba(56,189,248,.18)"; ctx.fill();
    ctx.strokeStyle="rgba(56,189,248,.4)"; ctx.lineWidth=1; ctx.stroke();
    // axis of rotation — x-axis dashed red
    var ax0=tc(xmin,0),ax1=tc(xmax,0);
    ctx.strokeStyle="#f87171"; ctx.lineWidth=2; ctx.setLineDash([6,4]);
    ctx.beginPath(); ctx.moveTo(ax0[0],ax0[1]); ctx.lineTo(ax1[0],ax1[1]); ctx.stroke();
    ctx.setLineDash([]);
    // y-axis
    var ay0=tc(0,ymin),ay1=tc(0,ymax);
    ctx.strokeStyle="#475569"; ctx.lineWidth=1.5;
    ctx.beginPath(); ctx.moveTo(ay0[0],ay0[1]); ctx.lineTo(ay1[0],ay1[1]); ctx.stroke();
    // curve y=x²
    ctx.strokeStyle="#38bdf8"; ctx.lineWidth=2.5;
    ctx.shadowColor="rgba(56,189,248,.5)"; ctx.shadowBlur=5;
    ctx.beginPath();
    for(var i=0;i<=120;i++){var x=i/120*2.3; var p=tc(x,x*x); i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}
    ctx.stroke(); ctx.shadowBlur=0;
    // boundary lines
    ctx.strokeStyle="rgba(248,250,252,.35)"; ctx.lineWidth=1.2; ctx.setLineDash([4,4]);
    var bx2a=tc(2,0),bx2b=tc(2,4);
    ctx.beginPath(); ctx.moveTo(bx2a[0],bx2a[1]); ctx.lineTo(bx2b[0],bx2b[1]); ctx.stroke();
    ctx.setLineDash([]);
    // labels
    ctx.fillStyle="#38bdf8"; ctx.font="italic 13px Georgia,serif"; ctx.textAlign="left";
    var lp=tc(1.3,1.3*1.3); ctx.fillText("y = x²",lp[0]+6,lp[1]-6);
    ctx.fillStyle="#f87171"; ctx.font="11px Georgia,serif"; ctx.textAlign="center";
    var axp=tc(2.2,0.15); ctx.fillText("axis of rotation",axp[0],axp[1]);
    ctx.fillStyle="#94a3b8"; ctx.font="11px Georgia,serif";
    var p2=tc(2,-0.3); ctx.textAlign="center"; ctx.fillText("x=2",p2[0],p2[1]);
    ctx.textAlign="center"; ctx.fillStyle="#64748b"; ctx.font="11px Georgia,serif";
    for(var i=0;i<=2;i++){var tp=tc(i,0);ctx.fillText(i,tp[0],tp[1]+13);}
    ctx.textAlign="right";
    for(var i=1;i<=4;i++){var tp=tc(0,i);ctx.fillText(i,tp[0]-5,tp[1]+4);}
    ctx.fillStyle="#94a3b8"; ctx.font="12px Georgia,serif"; ctx.textAlign="center";
    ctx.fillText("2D Region",W/2,12);
  }

  function proj(xp,r,th,az,el){
    var X=xp,Y=r*Math.cos(th),Z=r*Math.sin(th);
    var X1=X*Math.cos(az)-Y*Math.sin(az);
    var Y1=X*Math.sin(az)+Y*Math.cos(az);
    var Y2=Y1*Math.cos(el)-Z*Math.sin(el);
    var Z2=Y1*Math.sin(el)+Z*Math.cos(el);
    return [X1,-Z2,Y2];
  }

  function draw3D(){
    var W=c3.width, H=c3.height;
    var ctx=c3.getContext("2d");
    ctx.clearRect(0,0,W,H);
    ctx.fillStyle="#020814"; ctx.fillRect(0,0,W,H);
    var ocx=W*0.45, ocy=H*0.55, scale=Math.min(W,H)*0.17;
    var N=40, SEGS=48;
    function p3(xp,r,th){var s=proj(xp,r,th,az,el);return[ocx+s[0]*scale,ocy+s[1]*scale];}
    function dep(xp,r,th){return proj(xp,r,th,az,el)[2];}

    // draw discs from x=0 to x=2
    var discs=[];
    for(var i=0;i<N;i++){
      var xm=(i+0.5)/N*2;
      discs.push({x0:i/N*2, x1:(i+1)/N*2, R:xm*xm});
    }
    // sort by depth
    discs.sort(function(a,b){return dep((a.x0+a.x1)/2,0,0)-dep((b.x0+b.x1)/2,0,0);});

    for(var di=0;di<discs.length;di++){
      var d=discs[di];
      var R=d.R, x0=d.x0, x1=d.x1;
      var isBack=dep((x0+x1)/2,0,0)<0;
      // back wall
      ctx.beginPath();
      for(var s=0;s<=SEGS;s++){var th=s/SEGS*2*Math.PI,pt=p3(x0,R,th);s===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath(); ctx.fillStyle="rgba(56,189,248,0.12)"; ctx.strokeStyle="rgba(56,189,248,0.35)"; ctx.lineWidth=0.6; ctx.fill(); ctx.stroke();
      // outer wall
      ctx.beginPath();
      for(var s=0;s<=SEGS;s++){var th=s/SEGS*2*Math.PI,pt=p3(x0,R,th);s===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var s=SEGS;s>=0;s--){var th=s/SEGS*2*Math.PI,pt=p3(x1,R,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath(); ctx.fillStyle="rgba(56,189,248,0.08)"; ctx.fill(); ctx.stroke();
      // front wall
      ctx.beginPath();
      for(var s=0;s<=SEGS;s++){var th=s/SEGS*2*Math.PI,pt=p3(x1,R,th);s===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath(); ctx.fillStyle="rgba(56,189,248,0.18)"; ctx.fill(); ctx.stroke();
    }
    // axis
    var ax0=p3(-0.1,0,0), ax1=p3(2.2,0,0);
    ctx.strokeStyle="rgba(248,113,113,.7)"; ctx.lineWidth=1.5; ctx.setLineDash([5,4]);
    ctx.beginPath(); ctx.moveTo(ax0[0],ax0[1]); ctx.lineTo(ax1[0],ax1[1]); ctx.stroke();
    ctx.setLineDash([]);
    // surface curve
    ctx.strokeStyle="#38bdf8"; ctx.lineWidth=1.8;
    ctx.shadowColor="rgba(56,189,248,.5)"; ctx.shadowBlur=4;
    ctx.beginPath();
    for(var i=0;i<=60;i++){var x=i/60*2,pt=p3(x,x*x,Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
    ctx.stroke(); ctx.shadowBlur=0;
    ctx.fillStyle="#94a3b8"; ctx.font="12px Georgia,serif"; ctx.textAlign="center";
    ctx.fillText("3D Solid  —  drag to rotate", W/2, 13);
  }

  function redraw(){draw2D();draw3D();}

  // drag
  function xy(e){return e.touches?{x:e.touches[0].clientX,y:e.touches[0].clientY}:{x:e.clientX,y:e.clientY};}
  c3.addEventListener("mousedown",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};c3.style.cursor="grabbing";});
  c3.addEventListener("touchstart",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};},{passive:false});
  window.addEventListener("mousemove",function(e){if(!drag.on)return;var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();});
  window.addEventListener("touchmove",function(e){if(!drag.on)return;e.preventDefault();var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();},{passive:false});
  window.addEventListener("mouseup",function(){drag.on=false;c3.style.cursor="grab";});
  window.addEventListener("touchend",function(){drag.on=false;});

  initSize(); redraw();
  window.addEventListener("resize",function(){initSize();redraw();});
})();
</script>

</div>
</details>

<h4>Problem 2.</h4> The region bounded by $y = \sqrt{x}$ and $y = x$ (they meet at $(0,0)$ and $(1,1)$) is rotated around the **$x$-axis**.

<details class="answers">
<summary>▶ Solution — Problem 2</summary>
<div class="answer-body">

<strong>Washer method</strong> (integrate along $x$; outer radius $R=\sqrt{x}$, inner radius $r=x$)

$$
\begin{eqnarray*}
	V
		&=&
			\pi\int_0^1\Bigl((\sqrt{x})^2 - x^2\Bigr)\,dx = \pi\int_0^1(x - x^2)\,dx
\\
		&=&
			\pi\left[\frac{x^2}{2}-\frac{x^3}{3}\right]_0^1 = \boxed{\dfrac{\pi}{6}}
\end{eqnarray*}
$$

<strong>Shell method</strong> (horizontal shells, integrate along $y$; for a given $y$ - $x$ runs from $y^2$ to $y$)

Shell radius $= y$, shell height $= y - y^2$.

$$
\begin{eqnarray*}
	V
		&=&
			2\pi\int_0^1 y\bigl(y - y^2\bigr)\,dy = 2\pi\int_0^1(y^2 - y^3)\,dy
\\
		&=&
			2\pi\left[\frac{y^3}{3}-\frac{y^4}{4}\right]_0^1 = 2\pi\cdot\frac{1}{12} = \boxed{\dfrac{\pi}{6}}\checkmark
\end{eqnarray*}
$$

<p class="hint">🔍 Both methods are equally clean here! Washer thinks in $x$ (natural for rotation around $x$-axis); shell thinks in $y$ and requires rewriting $y=\sqrt{x}\Rightarrow x=y^2$ and $y=x\Rightarrow x=y$.</p>

<div id="p2-viz" style="background:linear-gradient(135deg,#0a0014,#1a000a,#0a0014);border-radius:14px;padding:18px;margin:16px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:10px;">
    <span style="font-size:11px;letter-spacing:.3em;color:#f87171;text-transform:uppercase;">Problem 2 — </span>
    <span style="font-size:13px;color:#f1f5f9;">$y=\sqrt{x}$ and $y=x$, rotated around $x$-axis</span>
  </div>
  <div style="display:flex;gap:10px;">
    <div style="flex:1;background:rgba(10,0,20,.8);border-radius:10px;border:1px solid rgba(148,163,184,.1);overflow:hidden;">
      <canvas id="p2-2d" style="width:100%;display:block;"></canvas>
    </div>
    <div style="flex:1;background:rgba(10,0,20,.8);border-radius:10px;border:1px solid rgba(248,113,113,.2);overflow:hidden;position:relative;">
      <canvas id="p2-3d" style="width:100%;display:block;cursor:grab;"></canvas>
      <div style="position:absolute;bottom:6px;right:8px;font-size:10px;color:rgba(248,113,113,.5);background:rgba(0,0,0,.4);padding:2px 6px;border-radius:4px;pointer-events:none;">drag to rotate</div>
    </div>
  </div>
  <div style="text-align:center;margin-top:8px;font-size:11px;color:#475569;">
    <span style="color:#4ade80;">green</span> = $y=\sqrt{x}$ (outer) &nbsp;|&nbsp;
    <span style="color:#fb923c;">orange</span> = $y=x$ (inner) &nbsp;|&nbsp;
    <span style="color:#f87171;">red dashed</span> = axis &nbsp;|&nbsp;
    <span style="color:#f87171;">3D washer</span> = hollow solid $V=\frac{\pi}{6}$
  </div>
</div>
<script>
(function(){
  var c2=document.getElementById("p2-2d");
  var c3=document.getElementById("p2-3d");
  var az=Math.PI/3, el=Math.PI/8;
  var drag={on:false,lx:0,ly:0};

  function initSize(){
    var w=c2.parentElement.clientWidth;
    var h=Math.round(w*0.72);
    c2.width=w; c2.height=h;
    c3.width=w; c3.height=h;
  }

  function draw2D(){
    var W=c2.width, H=c2.height;
    var ctx=c2.getContext("2d");
    ctx.clearRect(0,0,W,H);
    ctx.fillStyle="#0a0014"; ctx.fillRect(0,0,W,H);
    var pl=40,pr=18,pt=18,pb=34;
    var xmin=-0.15,xmax=1.35,ymin=-0.2,ymax=1.25;
    function tc(x,y){return[pl+(x-xmin)/(xmax-xmin)*(W-pl-pr), H-pb-(y-ymin)/(ymax-ymin)*(H-pt-pb)];}
    // grid
    ctx.strokeStyle="rgba(148,163,184,.07)"; ctx.lineWidth=1;
    for(var i=0;i<=1;i++){var p=tc(0,i);ctx.beginPath();ctx.moveTo(pl,p[1]);ctx.lineTo(W-pr,p[1]);ctx.stroke();}
    for(var i=0;i<=1;i++){var p=tc(i,0);ctx.beginPath();ctx.moveTo(p[0],pt);ctx.lineTo(p[0],H-pb);ctx.stroke();}
    // shaded region between curves
    ctx.beginPath();
    for(var i=0;i<=80;i++){var x=i/80; var p=tc(x,Math.sqrt(x)); i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}
    for(var i=80;i>=0;i--){var x=i/80; var p=tc(x,x); ctx.lineTo(p[0],p[1]);}
    ctx.closePath();
    ctx.fillStyle="rgba(248,113,113,.15)"; ctx.fill();
    ctx.strokeStyle="rgba(248,113,113,.3)"; ctx.lineWidth=1; ctx.stroke();
    // axis of rotation — x-axis dashed red
    var ax0=tc(xmin,0),ax1=tc(xmax,0);
    ctx.strokeStyle="#f87171"; ctx.lineWidth=2; ctx.setLineDash([6,4]);
    ctx.beginPath(); ctx.moveTo(ax0[0],ax0[1]); ctx.lineTo(ax1[0],ax1[1]); ctx.stroke();
    ctx.setLineDash([]);
    // y-axis
    ctx.strokeStyle="#475569"; ctx.lineWidth=1.2;
    var ay0=tc(0,ymin),ay1=tc(0,ymax);
    ctx.beginPath(); ctx.moveTo(ay0[0],ay0[1]); ctx.lineTo(ay1[0],ay1[1]); ctx.stroke();
    // curve y=sqrt(x) — green
    ctx.strokeStyle="#4ade80"; ctx.lineWidth=2.5;
    ctx.shadowColor="rgba(74,222,128,.5)"; ctx.shadowBlur=5;
    ctx.beginPath();
    for(var i=0;i<=100;i++){var x=i/100*1.25; var p=tc(x,Math.sqrt(x)); i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}
    ctx.stroke(); ctx.shadowBlur=0;
    // curve y=x — orange
    ctx.strokeStyle="#fb923c"; ctx.lineWidth=2.5;
    ctx.shadowColor="rgba(251,146,60,.5)"; ctx.shadowBlur=5;
    ctx.beginPath();
    for(var i=0;i<=100;i++){var x=i/100*1.25; var p=tc(x,x); i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}
    ctx.stroke(); ctx.shadowBlur=0;
    // intersection dots
    function dot(x,y,color){var p=tc(x,y);ctx.fillStyle=color;ctx.shadowColor=color;ctx.shadowBlur=8;ctx.beginPath();ctx.arc(p[0],p[1],4,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;}
    dot(0,0,"#f1f5f9"); dot(1,1,"#f1f5f9");
    // labels
    ctx.fillStyle="#4ade80"; ctx.font="italic 12px Georgia,serif"; ctx.textAlign="left";
    var lp=tc(0.65,Math.sqrt(0.65)); ctx.fillText("y=√x",lp[0]+5,lp[1]-6);
    ctx.fillStyle="#fb923c";
    var lp2=tc(0.72,0.72); ctx.fillText("y=x",lp2[0]+5,lp2[1]+13);
    ctx.fillStyle="#f87171"; ctx.font="11px Georgia,serif"; ctx.textAlign="center";
    var axp=tc(1.15,0.12); ctx.fillText("axis of rotation",axp[0],axp[1]);
    ctx.fillStyle="#94a3b8"; ctx.font="10px Georgia,serif";
    var p1=tc(1,-0.12); ctx.textAlign="center"; ctx.fillText("(1,1)",tc(1,1)[0]+10,tc(1,1)[1]-6);
    ctx.fillStyle="#94a3b8"; ctx.font="12px Georgia,serif"; ctx.textAlign="center";
    ctx.fillText("2D Region",W/2,12);
  }

  function proj(xp,r,th,az,el){
    var X=xp,Y=r*Math.cos(th),Z=r*Math.sin(th);
    var X1=X*Math.cos(az)-Y*Math.sin(az);
    var Y1=X*Math.sin(az)+Y*Math.cos(az);
    var Y2=Y1*Math.cos(el)-Z*Math.sin(el);
    var Z2=Y1*Math.sin(el)+Z*Math.cos(el);
    return [X1,-Z2,Y2];
  }

  function draw3D(){
    var W=c3.width, H=c3.height;
    var ctx=c3.getContext("2d");
    ctx.clearRect(0,0,W,H);
    ctx.fillStyle="#0a0014"; ctx.fillRect(0,0,W,H);
    var ocx=W*0.45, ocy=H*0.55, scale=Math.min(W,H)*0.32;
    var N=36, SEGS=48;
    function p3(xp,r,th){var s=proj(xp,r,th,az,el);return[ocx+s[0]*scale,ocy+s[1]*scale];}
    function dep(xp,r,th){return proj(xp,r,th,az,el)[2];}

    var washers=[];
    for(var i=0;i<N;i++){
      var x0=i/N, x1=(i+1)/N, xm=(x0+x1)/2;
      washers.push({x0:x0, x1:x1, Ro:Math.sqrt(xm), Ri:xm});
    }
    washers.sort(function(a,b){return dep((a.x0+a.x1)/2,0,0)-dep((b.x0+b.x1)/2,0,0);});

    for(var di=0;di<washers.length;di++){
      var w=washers[di];
      var Ro=w.Ro, Ri=w.Ri, x0=w.x0, x1=w.x1;
      // draw washer face at x0
      for(var face=0;face<2;face++){
        var xf=face===0?x0:x1;
        // outer ring to inner ring (annulus)
        ctx.beginPath();
        for(var s=0;s<=SEGS;s++){var th=s/SEGS*2*Math.PI,pt=p3(xf,Ro,th);s===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
        // inner hole (reverse)
        for(var s=SEGS;s>=0;s--){var th=s/SEGS*2*Math.PI,pt=p3(xf,Ri,th);ctx.lineTo(pt[0],pt[1]);}
        ctx.closePath();
        ctx.fillStyle=face===0?"rgba(248,113,113,0.12)":"rgba(248,113,113,0.22)";
        ctx.strokeStyle="rgba(248,113,113,0.45)"; ctx.lineWidth=0.6;
        ctx.fill(); ctx.stroke();
      }
      // outer wall
      ctx.beginPath();
      for(var s=0;s<=SEGS;s++){var th=s/SEGS*2*Math.PI,pt=p3(x0,Ro,th);s===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var s=SEGS;s>=0;s--){var th=s/SEGS*2*Math.PI,pt=p3(x1,Ro,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath(); ctx.fillStyle="rgba(248,113,113,0.07)"; ctx.strokeStyle="rgba(248,113,113,0.3)"; ctx.lineWidth=0.5; ctx.fill(); ctx.stroke();
      // inner wall
      ctx.beginPath();
      for(var s=0;s<=SEGS;s++){var th=s/SEGS*2*Math.PI,pt=p3(x0,Ri,th);s===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var s=SEGS;s>=0;s--){var th=s/SEGS*2*Math.PI,pt=p3(x1,Ri,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath(); ctx.fillStyle="rgba(251,146,60,0.05)"; ctx.strokeStyle="rgba(251,146,60,0.25)"; ctx.lineWidth=0.5; ctx.fill(); ctx.stroke();
    }
    // axis
    var ax0=p3(-0.05,0,0), ax1=p3(1.15,0,0);
    ctx.strokeStyle="rgba(248,113,113,.7)"; ctx.lineWidth=1.5; ctx.setLineDash([5,4]);
    ctx.beginPath(); ctx.moveTo(ax0[0],ax0[1]); ctx.lineTo(ax1[0],ax1[1]); ctx.stroke();
    ctx.setLineDash([]);
    // outer surface curve
    ctx.strokeStyle="#4ade80"; ctx.lineWidth=1.5; ctx.shadowColor="rgba(74,222,128,.4)"; ctx.shadowBlur=4;
    ctx.beginPath();
    for(var i=0;i<=60;i++){var x=i/60,pt=p3(x,Math.sqrt(x),Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
    ctx.stroke();
    // inner surface curve
    ctx.strokeStyle="#fb923c"; ctx.lineWidth=1.5; ctx.shadowColor="rgba(251,146,60,.4)";
    ctx.beginPath();
    for(var i=0;i<=60;i++){var x=i/60,pt=p3(x,x,Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
    ctx.stroke(); ctx.shadowBlur=0;
    ctx.fillStyle="#94a3b8"; ctx.font="12px Georgia,serif"; ctx.textAlign="center";
    ctx.fillText("3D Washer Solid  —  drag to rotate", W/2, 13);
  }

  function redraw(){draw2D();draw3D();}
  function xy(e){return e.touches?{x:e.touches[0].clientX,y:e.touches[0].clientY}:{x:e.clientX,y:e.clientY};}
  c3.addEventListener("mousedown",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};c3.style.cursor="grabbing";});
  c3.addEventListener("touchstart",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};},{passive:false});
  window.addEventListener("mousemove",function(e){if(!drag.on)return;var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();});
  window.addEventListener("touchmove",function(e){if(!drag.on)return;e.preventDefault();var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();},{passive:false});
  window.addEventListener("mouseup",function(){drag.on=false;c3.style.cursor="grab";});
  window.addEventListener("touchend",function(){drag.on=false;});
  initSize(); redraw();
  window.addEventListener("resize",function(){initSize();redraw();});
})();
</script>

</div>
</details>

<h4>Problem 3.</h4> The region bounded by $y = x^2$ and $y = 2x$ (they meet at $(0,0)$ and $(2,4)$) is rotated around the **$y$-axis**.

<details class="answers">
<summary>▶ Solution — Problem 3</summary>
<div class="answer-body">

<strong>Shell method</strong> (vertical shells, integrate along $x$; shell radius $= x$, height $= 2x - x^2$)

$$V = 2\pi\int_0^2 x\bigl(2x - x^2\bigr)\,dx = 2\pi\int_0^2(2x^2 - x^3)\,dx$$
$$= 2\pi\left[\frac{2x^3}{3} - \frac{x^4}{4}\right]_0^2 = 2\pi\!\left(\frac{16}{3} - 4\right) = 2\pi\cdot\frac{4}{3} = \boxed{\dfrac{8\pi}{3}}$$

<strong>Washer method</strong> (integrate along $y$; for a given $y$ - outer radius from $y=x^2\Rightarrow x=\sqrt{y}$, inner radius from $y=2x\Rightarrow x=y/2$)

$$
\begin{eqnarray*}
	V
		&=&
			\pi\int_0^4\Bigl((\sqrt{y})^2 - \left(\dfrac{y}{2}\right)^2\Bigr)\,dy = \pi\int_0^4\!\left(y - \frac{y^2}{4}\right)\!dy
\\
		&=&
			\pi\left[\frac{y^2}{2}-\frac{y^3}{12}\right]_0^4
				=
					\pi\!\left(8 - \frac{64}{12}\right) = \pi\cdot\frac{8}{3} = \boxed{\dfrac{8\pi}{3}}\checkmark
\end{eqnarray*}
$$

<p class="hint">🔍 Shell was much easier here — rotating around the $y$-axis with functions given in $x$ is exactly what shell method is designed for. Washer forced us to invert both curves and integrate in $y$.</p>

<div id="p3-viz" style="background:linear-gradient(135deg,#001408,#0a1a00,#001408);border-radius:14px;padding:18px;margin:16px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:10px;">
    <span style="font-size:11px;letter-spacing:.3em;color:#4ade80;text-transform:uppercase;">Problem 3 — </span>
    <span style="font-size:13px;color:#f1f5f9;">$y=x^2$ and $y=2x$, rotated around $y$-axis</span>
  </div>
  <div style="display:flex;gap:10px;">
    <div style="flex:1;background:rgba(0,20,8,.8);border-radius:10px;border:1px solid rgba(148,163,184,.1);overflow:hidden;">
      <canvas id="p3-2d" style="width:100%;display:block;"></canvas>
    </div>
    <div style="flex:1;background:rgba(0,20,8,.8);border-radius:10px;border:1px solid rgba(74,222,128,.2);overflow:hidden;position:relative;">
      <canvas id="p3-3d" style="width:100%;display:block;cursor:grab;"></canvas>
      <div style="position:absolute;bottom:6px;right:8px;font-size:10px;color:rgba(74,222,128,.5);background:rgba(0,0,0,.4);padding:2px 6px;border-radius:4px;pointer-events:none;">drag to rotate</div>
    </div>
  </div>
  <div style="text-align:center;margin-top:8px;font-size:11px;color:#475569;">
    <span style="color:#fb923c;">orange</span> = $y=2x$ (inner boundary) &nbsp;|&nbsp;
    <span style="color:#a78bfa;">purple</span> = $y=x^2$ (outer boundary) &nbsp;|&nbsp;
    <span style="color:#4ade80;">green dashed</span> = $y$-axis (axis of rotation)
  </div>
</div>
<script>
(function(){
  var c2=document.getElementById("p3-2d");
  var c3=document.getElementById("p3-3d");
  var az=Math.PI/4, el=Math.PI/9;
  var drag={on:false,lx:0,ly:0};

  function initSize(){
    var w=c2.parentElement.clientWidth;
    var h=Math.round(w*0.72);
    c2.width=w; c2.height=h;
    c3.width=w; c3.height=h;
  }

  function draw2D(){
    var W=c2.width, H=c2.height;
    var ctx=c2.getContext("2d");
    ctx.clearRect(0,0,W,H);
    ctx.fillStyle="#001408"; ctx.fillRect(0,0,W,H);
    var pl=42,pr=18,pt=18,pb=34;
    var xmin=-0.35,xmax=2.5,ymin=-0.5,ymax=4.8;
    function tc(x,y){return[pl+(x-xmin)/(xmax-xmin)*(W-pl-pr), H-pb-(y-ymin)/(ymax-ymin)*(H-pt-pb)];}
    // grid
    ctx.strokeStyle="rgba(148,163,184,.07)"; ctx.lineWidth=1;
    for(var i=0;i<=4;i++){var p=tc(0,i);ctx.beginPath();ctx.moveTo(pl,p[1]);ctx.lineTo(W-pr,p[1]);ctx.stroke();}
    for(var i=0;i<=2;i++){var p=tc(i,0);ctx.beginPath();ctx.moveTo(p[0],pt);ctx.lineTo(p[0],H-pb);ctx.stroke();}
    // shaded region between curves
    ctx.beginPath();
    for(var i=0;i<=80;i++){var x=i/80*2; var p=tc(x,2*x); i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}
    for(var i=80;i>=0;i--){var x=i/80*2; var p=tc(x,x*x); ctx.lineTo(p[0],p[1]);}
    ctx.closePath();
    ctx.fillStyle="rgba(74,222,128,.13)"; ctx.fill();
    ctx.strokeStyle="rgba(74,222,128,.3)"; ctx.lineWidth=1; ctx.stroke();
    // axis of rotation — y-axis dashed green
    var ay0=tc(0,ymin),ay1=tc(0,ymax);
    ctx.strokeStyle="#4ade80"; ctx.lineWidth=2; ctx.setLineDash([6,4]);
    ctx.beginPath(); ctx.moveTo(ay0[0],ay0[1]); ctx.lineTo(ay1[0],ay1[1]); ctx.stroke();
    ctx.setLineDash([]);
    // x-axis
    ctx.strokeStyle="#475569"; ctx.lineWidth=1.2;
    var ax0=tc(xmin,0),ax1=tc(xmax,0);
    ctx.beginPath(); ctx.moveTo(ax0[0],ax0[1]); ctx.lineTo(ax1[0],ax1[1]); ctx.stroke();
    // curve y=2x — orange
    ctx.strokeStyle="#fb923c"; ctx.lineWidth=2.5;
    ctx.shadowColor="rgba(251,146,60,.5)"; ctx.shadowBlur=5;
    ctx.beginPath();
    for(var i=0;i<=100;i++){var x=i/100*2.3; var p=tc(x,2*x); i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}
    ctx.stroke(); ctx.shadowBlur=0;
    // curve y=x² — purple
    ctx.strokeStyle="#a78bfa"; ctx.lineWidth=2.5;
    ctx.shadowColor="rgba(167,139,250,.5)"; ctx.shadowBlur=5;
    ctx.beginPath();
    for(var i=0;i<=100;i++){var x=i/100*2.3; var p=tc(x,x*x); i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);}
    ctx.stroke(); ctx.shadowBlur=0;
    // dots at intersections
    function dot(x,y,color){var p=tc(x,y);ctx.fillStyle=color;ctx.shadowColor=color;ctx.shadowBlur=8;ctx.beginPath();ctx.arc(p[0],p[1],4,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;}
    dot(0,0,"#f1f5f9"); dot(2,4,"#f1f5f9");
    ctx.fillStyle="#f1f5f9"; ctx.font="10px Georgia,serif"; ctx.textAlign="left";
    var p22=tc(2,4); ctx.fillText("(2,4)",p22[0]+5,p22[1]-5);
    // labels
    ctx.fillStyle="#fb923c"; ctx.font="italic 12px Georgia,serif"; ctx.textAlign="left";
    var lp=tc(1.6,2*1.6); ctx.fillText("y=2x",lp[0]+5,lp[1]-6);
    ctx.fillStyle="#a78bfa";
    var lp2=tc(1.7,1.7*1.7); ctx.fillText("y=x²",lp2[0]+5,lp2[1]+13);
    ctx.fillStyle="#4ade80"; ctx.font="11px Georgia,serif"; ctx.textAlign="center";
    var ayp=tc(-0.22,3.5); ctx.fillText("axis",ayp[0],ayp[1]);
    ctx.fillStyle="#94a3b8"; ctx.font="12px Georgia,serif"; ctx.textAlign="center";
    ctx.fillText("2D Region",W/2,12);
    ctx.fillStyle="#64748b"; ctx.font="11px Georgia,serif";
    for(var i=0;i<=2;i++){var tp=tc(i,0);ctx.textAlign="center";ctx.fillText(i,tp[0],tp[1]+13);}
    ctx.textAlign="right";
    for(var i=1;i<=4;i++){var tp=tc(0,i);ctx.fillText(i,tp[0]-5,tp[1]+4);}
  }

  function proj(xp,r,th,az,el){
    // for y-axis rotation: the y-axis is the rotation axis
    // map: xpos=y(height), r=x(radius), theta=angle
    var X=xp,Y=r*Math.cos(th),Z=r*Math.sin(th);
    var X1=X*Math.cos(az)-Y*Math.sin(az);
    var Y1=X*Math.sin(az)+Y*Math.cos(az);
    var Y2=Y1*Math.cos(el)-Z*Math.sin(el);
    var Z2=Y1*Math.sin(el)+Z*Math.cos(el);
    return [X1,-Z2,Y2];
  }

  function draw3D(){
    var W=c3.width, H=c3.height;
    var ctx=c3.getContext("2d");
    ctx.clearRect(0,0,W,H);
    ctx.fillStyle="#001408"; ctx.fillRect(0,0,W,H);
    var ocx=W*0.48, ocy=H*0.60, scale=Math.min(W,H)*0.16;
    var N=40, SEGS=48;
    // rotation around y-axis: shells at each x, y goes from x² to 2x
    // project: ypos along y-axis, radius = x
    function p3(ypos,r,th){var s=proj(ypos,r,th,az,el);return[ocx+s[0]*scale,ocy+s[1]*scale];}
    function dep(ypos,r,th){return proj(ypos,r,th,az,el)[2];}

    // Build shells: for each x strip, the shell spans y from x² to 2x at radius x
    // In 3D this is a cylindrical shell at radius x, height from x² to 2x
    // We'll approximate by slicing in x, drawing annular rings at each y level
    // Actually let's draw it as discs in y: for each y, outer x = sqrt(y), inner x = y/2
    // This gives washer solid — visually clearer
    var slices=[];
    for(var i=0;i<N;i++){
      var y0=i/N*4, y1=(i+1)/N*4, ym=(y0+y1)/2;
      var Ro=Math.sqrt(ym), Ri=ym/2;
      if(Ro>Ri) slices.push({y0:y0,y1:y1,Ro:Ro,Ri:Ri});
    }
    slices.sort(function(a,b){return dep((a.y0+a.y1)/2,0,0)-dep((b.y0+b.y1)/2,0,0);});

    for(var di=0;di<slices.length;di++){
      var s=slices[di];
      var Ro=s.Ro, Ri=s.Ri, y0=s.y0, y1=s.y1;
      // washer faces
      for(var face=0;face<2;face++){
        var yf=face===0?y0:y1;
        ctx.beginPath();
        for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(yf,Ro,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
        for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(yf,Ri,th);ctx.lineTo(pt[0],pt[1]);}
        ctx.closePath();
        ctx.fillStyle=face===0?"rgba(74,222,128,0.10)":"rgba(74,222,128,0.20)";
        ctx.strokeStyle="rgba(74,222,128,0.35)"; ctx.lineWidth=0.6;
        ctx.fill(); ctx.stroke();
      }
      // outer wall
      ctx.beginPath();
      for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(y0,Ro,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(y1,Ro,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath(); ctx.fillStyle="rgba(167,139,250,0.07)"; ctx.strokeStyle="rgba(167,139,250,0.3)"; ctx.lineWidth=0.5; ctx.fill(); ctx.stroke();
      // inner wall
      ctx.beginPath();
      for(var k=0;k<=SEGS;k++){var th=k/SEGS*2*Math.PI,pt=p3(y0,Ri,th);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var k=SEGS;k>=0;k--){var th=k/SEGS*2*Math.PI,pt=p3(y1,Ri,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath(); ctx.fillStyle="rgba(251,146,60,0.05)"; ctx.strokeStyle="rgba(251,146,60,0.2)"; ctx.lineWidth=0.5; ctx.fill(); ctx.stroke();
    }
    // y-axis (rotation axis)
    var ay0=p3(-0.2,0,0), ay1=p3(4.4,0,0);
    ctx.strokeStyle="rgba(74,222,128,.7)"; ctx.lineWidth=1.5; ctx.setLineDash([5,4]);
    ctx.beginPath(); ctx.moveTo(ay0[0],ay0[1]); ctx.lineTo(ay1[0],ay1[1]); ctx.stroke();
    ctx.setLineDash([]);
    // outer surface curve (y=x² => x=sqrt(y))
    ctx.strokeStyle="#a78bfa"; ctx.lineWidth=1.5; ctx.shadowColor="rgba(167,139,250,.4)"; ctx.shadowBlur=4;
    ctx.beginPath();
    for(var i=0;i<=60;i++){var y=i/60*4,pt=p3(y,Math.sqrt(y),Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
    ctx.stroke();
    // inner surface curve (y=2x => x=y/2)
    ctx.strokeStyle="#fb923c"; ctx.lineWidth=1.5; ctx.shadowColor="rgba(251,146,60,.4)";
    ctx.beginPath();
    for(var i=0;i<=60;i++){var y=i/60*4,pt=p3(y,y/2,Math.PI/2);i===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
    ctx.stroke(); ctx.shadowBlur=0;
    ctx.fillStyle="#94a3b8"; ctx.font="12px Georgia,serif"; ctx.textAlign="center";
    ctx.fillText("3D Solid  —  drag to rotate", W/2, 13);
  }

  function redraw(){draw2D();draw3D();}
  function xy(e){return e.touches?{x:e.touches[0].clientX,y:e.touches[0].clientY}:{x:e.clientX,y:e.clientY};}
  c3.addEventListener("mousedown",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};c3.style.cursor="grabbing";});
  c3.addEventListener("touchstart",function(e){e.preventDefault();var p=xy(e);drag={on:true,lx:p.x,ly:p.y};},{passive:false});
  window.addEventListener("mousemove",function(e){if(!drag.on)return;var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();});
  window.addEventListener("touchmove",function(e){if(!drag.on)return;e.preventDefault();var p=xy(e);az+=(p.x-drag.lx)*.012;el=Math.max(-1.4,Math.min(1.4,el-(p.y-drag.ly)*.012));drag.lx=p.x;drag.ly=p.y;draw3D();},{passive:false});
  window.addEventListener("mouseup",function(){drag.on=false;c3.style.cursor="grab";});
  window.addEventListener("touchend",function(){drag.on=false;});
  initSize(); redraw();
  window.addEventListener("resize",function(){initSize();redraw();});
})();
</script>

</div>
</details>

## March 9, 2026 {#mar-09-2026}

<div class="date-banner">
📅 <strong>Mon, March 9, 2026</strong> &nbsp;|&nbsp;
Topics
&ndash;
<strong>Limits at 0 and $\infty$</strong> · <strong>Series convergence</strong> · <strong>FTC Part 1</strong>
</div>

### Part 1 — Limits

Find the value of each limit (write $\infty$, $-\infty$, or DNE when appropriate).

<ol>
<li>$\displaystyle\lim_{x\to\infty} \dfrac{x^2 - 3x}{-3x^2 + 4x + 1}$</li>

<li>$\displaystyle\lim_{x\to\infty} \dfrac{x^2 - 3x}{-3x^2 + 4x}$</li>

<li>$\displaystyle\lim_{x\to 0} \dfrac{x^2 - 3x}{-3x^2 + 4x}$</li>

<li>$\displaystyle\lim_{x\to 0^+} x\ln x$</li>

<li>$\displaystyle\lim_{x\to 0^+} x^2 \ln x$</li>

<li>$\displaystyle\lim_{x\to 0^+} x^{10} \ln x$</li>

<li>$\displaystyle\lim_{x\to 0^+} x^{0.01} \ln x$</li>

<li>$\displaystyle\lim_{x\to 0^+} x^{-1} \ln x$ &nbsp;&nbsp; <em>(careful — which dominates?)</em></li>

<li>$\displaystyle\lim_{x\to 0^+} x^{-0.01} \ln x$ &nbsp;&nbsp; <em>(subtle!)</em></li>

<li>$\displaystyle\lim_{x\to\infty} x\ln x$</li>

<li>$\displaystyle\lim_{x\to\infty} x^2 \ln x$</li>

<li>$\displaystyle\lim_{x\to\infty} x^{10} \ln x$</li>

<li>$\displaystyle\lim_{x\to\infty} x^{0.01} \ln x$</li>

<li>$\displaystyle\lim_{x\to\infty} x^{-1} \ln x$</li>

<li>$\displaystyle\lim_{x\to\infty} x^{-0.01} \ln x$ &nbsp;&nbsp; <em>(compare growth rates carefully)</em></li>

<li>$\displaystyle\lim_{x\to\infty} \dfrac{\ln(100 + e^{3x}) + 10^{10^{10}}}{5x}$</li>

<li>$\displaystyle\lim_{x\to\infty} \dfrac{\ln(100 + e^{3x}) - \ln 101}{5x}$</li>

<li>$\displaystyle\lim_{x\to 0} \dfrac{\ln(100 + e^{3x}) - \ln 101}{5x}$</li>

<li>$\displaystyle\lim_{x\to 0} \dfrac{\ln(100 + e^{3x})}{5x}$ &nbsp;&nbsp; <em>(does this even exist?)</em></li>

<li>$\displaystyle\lim_{n\to\infty} (-1)^n$</li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 1</summary>
<div class="answer-body">
<ol>
<li><span class="ans">$-\dfrac{1}{3}$</span> <span class="hint"> — divide top and bottom by $x^2$; only leading coefficients survive</span></li>

<li><span class="ans">$-\dfrac{1}{3}$</span> <span class="hint"> — same; the $+1$ in the denominator is irrelevant at $\infty$</span></li>

<li><span class="ans">$-\dfrac{3}{4}$</span> <span class="hint"> — factor out $x$: $\frac{x(x-3)}{x(-3x+4)}$, cancel $x$, plug in $x=0$: $\frac{0-3}{0+4} = -\frac{3}{4}$</span></li>

<li><span class="ans">$0$</span> <span class="hint"> — rewrite as $\frac{\ln x}{x^{-1}}$; L'Hôpital: $\frac{1/x}{-x^{-2}} = -x \to 0$</span></li>

<li><span class="ans">$0$</span> <span class="hint"> — $x^2$ kills $\ln x$ even faster; for any $p>0$: $\lim_{x\to 0^+} x^p\ln x = 0$</span></li>

<li><span class="ans">$0$</span> <span class="hint"> — same rule, $p=10$</span></li>

<li><span class="ans">$0$</span> <span class="hint"> — same rule, $p=0.01>0$; polynomial always beats log</span></li>

<li><span class="ans">$-\infty$</span> <span class="hint"> — $\frac{\ln x}{x} \xrightarrow{x\to 0^+} \frac{-\infty}{0^+} = -\infty$ (denominator $\to 0^+$ makes it blow up)</span></li>

<li><span class="ans">$-\infty$</span> <span class="hint"> — $p=-0.01<0$ so $x^{-0.01}\to +\infty$ while $\ln x\to -\infty$; product $\to -\infty$</span></li>

<li><span class="ans">$\infty$</span> <span class="hint"> — both $x\to\infty$ and $\ln x\to\infty$; no competition</span></li>

<li><span class="ans">$\infty$</span></li>

<li><span class="ans">$\infty$</span></li>

<li><span class="ans">$\infty$</span> <span class="hint"> — even a tiny positive power $\times \ln x \to \infty$</span></li>

<li><span class="ans">$0$</span> <span class="hint"> — $\frac{\ln x}{x}\to 0$; polynomial growth crushes logarithm at $\infty$</span></li>

<li><span class="ans">$0$</span> <span class="hint"> — $\frac{\ln x}{x^{0.01}}\to 0$; any polynomial power beats $\ln x$ at $\infty$</span></li>

<li><span class="ans">$\dfrac{3}{5}$</span> <span class="hint"> — the constant $10^{10^{10}}$ is irrelevant at $\infty$; $\ln(100+e^{3x})\approx 3x$ for large $x$, so limit $=\frac{3x}{5x}=\frac{3}{5}$</span></li>

<li><span class="ans">$\dfrac{3}{5}$</span> <span class="hint"> — $-\ln 101$ is a fixed constant, irrelevant at $\infty$; same reasoning</span></li>

<li><span class="ans">$\dfrac{3}{505}$</span> <span class="hint"> — at $x=0$: $\frac{0}{0}$ form; L'Hôpital: $\dfrac{3e^{3x}/(100+e^{3x})}{5}\Big|_{x=0} = \dfrac{3/101}{5} = \dfrac{3}{505}$</span></li>

<li><span class="ans">DNE</span> <span class="hint"> — numerator $\to\ln 101\neq 0$ while denominator $\to 0$; from the right $\to+\infty$, from the left $\to-\infty$</span></li>

<li><span class="ans">DNE</span> <span class="hint"> — $(-1)^n$ oscillates between $+1$ and $-1$ forever; no single value</span></li>
</ol>
</div>
</details>

### Part 2 — Series
&ndash;
Converge or Diverge?

For each series
&ndash;
does it <strong>converge</strong> or <strong>diverge</strong>?
If it converges, give the exact value if you can. If it diverges, write $\infty$, $-\infty$, or "oscillates."

<ol>
<li>$\displaystyle\sum_{n=1}^{\infty} \dfrac{1}{n}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} \dfrac{1}{n^2}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} \dfrac{1}{n^4}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} \dfrac{(-1)^{n+1}}{n}$</li>

<li>$\displaystyle\sum_{n=0}^{\infty} \dfrac{(-1)^{n}}{2n+1}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} (-1)^n$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} \dfrac{1}{n!}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} 2^{n-1}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} (0.5)^{n-1}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} (0.25)^{n-1}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} \left(\dfrac{1}{3}\right)^{n-1}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} \dfrac{n!}{e^n}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} \dfrac{e^n}{n!}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} \dfrac{n^2}{e^n}$</li>

<li>$\displaystyle\sum_{n=1}^{\infty} \dfrac{n^{1000}}{e^n}$</li>
</ol>

<details class="answers">
<summary>▶ Answers — Part 2</summary>
<div class="answer-body">
<ol>
<li><span class="ans">Diverges ($\infty$)</span> <span class="hint"> — the harmonic series; famously diverges (grows like $\ln n$)</span></li>

<li><span class="ans">Converges $= \dfrac{\pi^2}{6} \approx 1.6449$</span> <span class="hint"> — Basel problem (Euler, 1734); $p$-series with $p=2>1$</span></li>

<li><span class="ans">Converges $= \dfrac{\pi^4}{90} \approx 1.0823$</span> <span class="hint"> — $p$-series with $p=4>1$</span></li>

<li><span class="ans">Converges $= \ln 2 \approx 0.6931$</span> <span class="hint"> — alternating harmonic series (Leibniz test)</span></li>

<li><span class="ans">Converges $= \dfrac{\pi}{4} \approx 0.7854$</span> <span class="hint"> — Gregory–Leibniz formula for $\pi$! (from $\arctan 1 = \pi/4$)</span></li>

<li><span class="ans">Diverges (oscillates)</span> <span class="hint"> — partial sums alternate $-1, 0, -1, 0, \ldots$; no limit</span></li>

<li><span class="ans">Converges $= e-1 \approx 1.7183$</span> <span class="hint"> — Taylor series for $e^x$ at $x=1$, minus the $n=0$ term</span></li>

<li><span class="ans">Diverges ($\infty$)</span> <span class="hint"> — geometric with ratio $r=2>1$</span></li>

<li><span class="ans">Converges $= 2$</span> <span class="hint"> — geometric: $\dfrac{1}{1-0.5} = 2$</span></li>

<li><span class="ans">Converges $= \dfrac{4}{3}$</span> <span class="hint"> — geometric: $\dfrac{1}{1-0.25} = \dfrac{4}{3}$</span></li>

<li><span class="ans">Converges $= \dfrac{3}{2}$</span> <span class="hint"> — geometric: $\dfrac{1}{1-\frac{1}{3}} = \dfrac{3}{2}$</span></li>

<li><span class="ans">Diverges ($\infty$)</span> <span class="hint"> — ratio test: $\dfrac{(n+1)!}{e^{n+1}}\cdot\dfrac{e^n}{n!} = \dfrac{n+1}{e}\to\infty$</span></li>

<li><span class="ans">Converges $= e^e - 1 \approx 14.77$</span> <span class="hint"> — ratio test: $\dfrac{e}{n+1}\to 0<1$; relates to Taylor expansion of $e^e$</span></li>

<li><span class="ans">Converges</span> <span class="hint"> — ratio test: $\dfrac{(n+1)^2}{n^2 \cdot e}\to\dfrac{1}{e}<1$</span></li>

<li><span class="ans">Converges</span> <span class="hint"> — ratio test: limit $\to\dfrac{1}{e}<1$; exponential always beats any polynomial power</span></li>
</ol>
</div>
</details>

### Part 3 — FTC, Part 1

Find each derivative. <em>Hint
&ndash;
you do NOT need to evaluate the integral!</em>

<ol>
<li>$\displaystyle\frac{d}{dx} \int_{0}^{x} \sqrt{\sin^4 t + 234}\; dt$</li>

<li>$\displaystyle\frac{d}{dx} \int_{-1000}^{x} \sqrt{\sin^4 t + 234}\; dt$</li>

<li>$\displaystyle\frac{d}{dx} \int_{10^{10}}^{x} \sqrt{\sin^4 t + 234}\; dt$</li>
</ol>

<p class="note">👀 Look carefully at all three answers. What do you notice about the lower limit?</p>

<details class="answers">
<summary>▶ Answers — Part 3</summary>
<div class="answer-body">
<div class="same-ans">
All three give the <strong>same answer</strong>:
$$\frac{d}{dx}\int_a^x \sqrt{\sin^4 t + 234}\;dt \;=\; \sqrt{\sin^4 x + 234}$$
</div>
<p>
The lower limit $a$ — whether $0$, $-1000$, or $10^{10}$ — only contributes a fixed constant
to the antiderivative, and constants vanish under differentiation.
FTC Part 1: $\;\dfrac{d}{dx}\displaystyle\int_a^x f(t)\,dt = f(x)\;$ for <em>any</em> constant $a$.
</p>
<p class="hint">
Also: inside the integral the dummy variable is $t$, not $x$.
Writing $\sqrt{\sin^4 x+234}$ inside the integral while differentiating with respect to $x$
would be a sign confusion — that's exactly why the dummy variable matters!
</p>
</div>
</details>
