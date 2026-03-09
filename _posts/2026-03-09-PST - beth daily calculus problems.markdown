---
date: Mon Mar  9 07:04:38 PDT 2026
last_modified_at: Mon Mar  9 07:04:38 PDT 2026
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

<!--style>
.daily-intro {
  background: linear-gradient(135deg, #0f172a, #1e1b4b);
  border-radius: 14px;
  padding: 20px 26px;
  margin: 18px 0 28px 0;
  border: 1px solid rgba(167,139,250,.3);
  color: #cbd5e1;
  font-family: Georgia, serif;
  font-size: 15px;
  line-height: 1.75;
}
.daily-intro blockquote {
  border-left: 3px solid #a78bfa;
  margin: 12px 0 0 0;
  padding-left: 16px;
  color: #a78bfa;
  font-style: italic;
}
.date-banner {
  background: linear-gradient(90deg, rgba(167,139,250,.12), rgba(56,189,248,.08));
  border: 1px solid rgba(167,139,250,.25);
  border-radius: 10px;
  padding: 9px 18px;
  margin-bottom: 18px;
  font-family: Georgia, serif;
  color: #94a3b8;
  font-size: 13px;
  letter-spacing: .02em;
}
.problem-set {
  background: linear-gradient(160deg, #0f172a 0%, #0d1f2d 100%);
  border-radius: 12px;
  padding: 20px 26px 16px 26px;
  margin: 0 0 14px 0;
  border: 1px solid rgba(56,189,248,.18);
}
.problem-set h4 {
  color: #38bdf8;
  margin: 0 0 14px 0;
  font-size: 15px;
  font-family: Georgia, serif;
  letter-spacing: .04em;
  text-transform: uppercase;
}
.problem-set ol, .problem-set ul {
  color: #e2e8f0;
  font-family: Georgia, serif;
  line-height: 1.85;
  margin: 0;
  padding-left: 22px;
}
.problem-set li { margin: 5px 0; }
.problem-set .note {
  color: #64748b;
  font-size: 12.5px;
  font-style: italic;
  margin-top: 10px;
}
details.answers {
  margin: 4px 0 22px 0;
}
details.answers summary {
  cursor: pointer;
  display: inline-block;
  background: rgba(74,222,128,.1);
  border: 1px solid rgba(74,222,128,.3);
  border-radius: 8px;
  padding: 6px 16px;
  color: #4ade80;
  font-size: 13px;
  font-family: Georgia, serif;
  font-weight: bold;
  letter-spacing: .04em;
  user-select: none;
}
details.answers .answer-body {
  background: rgba(15,23,42,.95);
  border: 1px solid rgba(74,222,128,.15);
  border-radius: 0 10px 10px 10px;
  padding: 16px 22px;
  font-family: Georgia, serif;
  font-size: 14px;
}
details.answers ol { color: #cbd5e1; padding-left: 20px; }
details.answers li { margin: 6px 0; line-height: 1.7; }
.ans { color: #fbbf24; font-weight: bold; }
.hint { color: #64748b; font-style: italic; font-size: 12.5px; }
.same-ans {
  background: rgba(167,139,250,.08);
  border-left: 3px solid #a78bfa;
  padding: 10px 16px;
  border-radius: 0 8px 8px 0;
  color: #c4b5fd;
  margin: 8px 0;
}
</style-->

<div class="daily-intro">
Short daily sessions — <strong>15–20 min</strong>, casual, no pressure. 🧠<br>
Think of it like a daily stretch before a game. The goal is <em>exposure</em>, not perfection.<br>
The more times you bump into a concept, the more natural it becomes.
<blockquote>
&ldquo;The best way to understand a limit is to bump into it over and over —<br>
not to stare at it once for three hours.&rdquo; — Daddy
</blockquote>
</div>

[← Back to main reference page](/math/ap/calculus/bc)

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

# March 2026

## March 9, 2026 {#mar-9-2026}

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

---

*New sessions are prepended at the top of each month's section — most recent first.*
