---
date: Mon Mar  9 07:04:38 PDT 2026
last_modified_at: Tue Mar 10 18:06:42 PDT 2026
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
