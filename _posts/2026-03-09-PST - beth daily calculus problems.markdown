---
date: Mon Mar  9 07:04:38 PDT 2026
last_modified_at: Tue Mar 10 05:16:44 PDT 2026
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

- [10-Mar-2026](#mar-10-2026)
- [09-Mar-2026](#mar-09-2026)

# March 2026

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

- **Method A**: L'Hôpital's theorem (when you get $\frac{0}{0}$ or $\frac{\infty}{\infty}$)
- **Method B**: Recognise it as a **derivative definition** $\displaystyle f'(a) = \lim_{h\to 0}\frac{f(a+h)-f(a)}{h}$

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
</div>
</details>

{: .notice--warning}
> <strong>Big takeaway from Part 4</strong><br>
> Disc/washer is natural when rotating around the <em>axis you're integrating along</em>.<br>
> Shell is natural when rotating around the <em>axis perpendicular to your integration variable</em>.<br>
> When in doubt, set up both — the easier one will be obvious. And they <em>always</em> give the same answer! ✓

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
