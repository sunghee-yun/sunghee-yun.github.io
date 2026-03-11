---
date: Sun Mar  1 23:13:06 PST 2026
last_modified_at: Wed Mar 11 00:08:43 PDT 2026
title: "Daddy's AP Calculus BC for Beth"
permalink: /math/ap/calculus/bc
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
sections:
  fundamental-theorem-of-calculus: "Fundamental theorem of calculus"
  iv-finite-diff: "Interactive visualization - finite difference approximation"
  iv-taylor-approximation: "Interactive visualization - Taylor approximation"
  iv-integral-approximation: "Interactive visualization - integral approximation"
  iv-arc-length: "Interactive visualization - arc length"
  iv-disc-method: "Interactive visualization — disc method"
  iv-washer-method: "Interactive 3D visualization — washer method"
  iv-shell-method: "Interactive 3D visualization — shell method"
  iv-volumes: "Interactive 3D visualizations - volumes"
  iv-ode: "Interactive animation — watch the solution evolve in real time"
  iv-deri-power-functions: "Power Functions"
  iv-anti-deri-power-functions: "Antiderivative of Power Functions"
---

posted: {{ page.date| date: "%d-%b-%Y" }}
&
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

<style>
table, tr, td, th {
    font-size: inherit !important;
    font-family: inherit !important;
}
</style>

{% assign inevitability = site.posts | where: "permalink", "/prajna/coincidence-vs-inevitability" | first %}

**Share this on**
[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url={{ site.url }}{{ site.baseurl }}{{ page.url }})
| [Instagram](https://www.instagram.com/)
| [Twitter (X)](https://x.com/intent/tweet?text={{ site.url }}{{ site.baseurl }}{{ page.url }})
| [Facebook](https://www.facebook.com/sharer/sharer.php?u={{ site.url }}{{ site.baseurl }}{{ page.url }})

<div class="img-container-justified">
	<div style="width: 49%; border: 1px solid #ccc; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin: 20px 0;">
		<div style="background-color: #2c3e50; color: white; padding: 10px 15px; font-size: 14px;">
			<strong>Deep Dive - An AI Pioneers Personal Calculus Blueprint</strong>
			<span style="opacity: 0.8;">(35:21)</span>
		</div>
		<div style="padding: 10px; background-color: #ecf0f1;">
			<audio id="podcast-audio-deep-dive-01" controls style="width: 100%;">
				<source type="audio/mp4" src="https://sungheeyun-podcasts-03.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/Deep Dive - An_AI_Pioneers_Personal_Calculus_Blueprint.m4a">
				Your browser does not support this audio element.
			</audio>
		</div>
	</div>
	<div style="width: 49%; border: 1px solid #ccc; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin: 20px 0;">
		<div style="background-color: #2c3e50; color: white; padding: 10px 15px; font-size: 14px;">
			<strong>Deep Dive - Engineering Logic for AP Calculus BC</strong>
			<span style="opacity: 0.8;">(43:04)</span>
		</div>
		<div style="padding: 10px; background-color: #ecf0f1;">
			<audio id="podcast-audio-deep-dive-02" controls style="width: 100%;">
				<source type="audio/mp4" src="https://sungheeyun-podcasts-03.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/Deep Dive - Engineering_Logic_for_AP_Calculus_BC.m4a">
				Your browser does not support this audio element.
			</audio>
		</div>
	</div>
</div>

<div class="img-container-justified">
	<div style="width: 49%; border: 1px solid #ccc; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin: 20px 0;">
		<div style="background-color: #2c3e50; color: white; padding: 10px 15px; font-size: 14px;">
			<strong>An AI Expert’s Calculus Guide For Beth</strong>
			<span style="opacity: 0.8;">(18:48)</span>
		</div>
		<div style="padding: 10px; background-color: #ecf0f1;">
			<audio id="podcast-audio-01" controls style="width: 100%;">
				<source type="audio/mp4" src="https://sungheeyun-podcasts-03.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/An_AI_Expert's_Calculus_Guide_For_Beth.m4a">
				Your browser does not support this audio element.
			</audio>
		</div>
	</div>
	<div style="width: 49%; border: 1px solid #ccc; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin: 20px 0;">
		<div style="background-color: #2c3e50; color: white; padding: 10px 15px; font-size: 14px;">
			<strong>An AI Expert's Calculus Blueprint for Beth</strong>
			<span style="opacity: 0.8;">(20:55)</span>
		</div>
		<div style="padding: 10px; background-color: #ecf0f1;">
			<audio id="podcast-audio-02" controls style="width: 100%;">
				<source type="audio/mp4" src="https://sungheeyun-podcasts-03.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/An_AI_Expert_s_Calculus_Blueprint_for_Beth.m4a">
				Your browser does not support this audio element.
			</audio>
		</div>
	</div>
</div>

<div class="img-container-justified">
	<div style="width: 49%; border: 1px solid #ccc; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin: 20px 0;">
		<div style="background-color: #2c3e50; color: white; padding: 10px 15px; font-size: 14px;">
			<strong>A CTO's Fatherly Guide to Calculus</strong>
			<span style="opacity: 0.8;">(35:43)</span>
		</div>
		<div style="padding: 10px; background-color: #ecf0f1;">
			<audio id="podcast-audio-long-01" controls style="width: 100%;">
				<source type="audio/mp4" src="https://sungheeyun-podcasts-03.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/A_CTO_s_fatherly_guide_to_calculus.m4a">
				Your browser does not support this audio element.
			</audio>
		</div>
	</div>
	<div style="width: 49%; border: 1px solid #ccc; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin: 20px 0;">
		<div style="background-color: #2c3e50; color: white; padding: 10px 15px; font-size: 14px;">
			<strong>A CTO's Calculus Guide for Beth</strong>
			<span style="opacity: 0.8;">(49:29)</span>
		</div>
		<div style="padding: 10px; background-color: #ecf0f1;">
			<audio id="podcast-audio-long-02" controls style="width: 100%;">
				<source type="audio/mp4" src="https://sungheeyun-podcasts-03.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/A_CTO_s_calculus_guide_for_Beth.m4a">
				Your browser does not support this audio element.
			</audio>
		</div>
	</div>
</div>

<div class="img-container-justified">
	<div style="width: 49%; border: 1px solid #ccc; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin: 20px 0;">
		<div style="background-color: #2c3e50; color: white; padding: 10px 15px; font-size: 14px;">
			<strong>An AI Expert's Calculus Guide for Beth</strong>
			<span style="opacity: 0.8;">(41:31)</span>
		</div>
		<div style="padding: 10px; background-color: #ecf0f1;">
			<audio id="podcast-audio-long-03" controls style="width: 100%;">
				<source type="audio/mp4" src="https://sungheeyun-podcasts-03.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/An_AI_Expert_s_Calculus_Guide_for_Beth.m4a">
				Your browser does not support this audio element.
			</audio>
		</div>
	</div>
	<div style="width: 49%; border: 1px solid #ccc; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin: 20px 0;">
		<div style="background-color: #2c3e50; color: white; padding: 10px 15px; font-size: 14px;">
			<strong>Debate - Applied Modeling Versus Pure Mathematical Rigor</strong>
			<span style="opacity: 0.8;">(20:11)</span>
		</div>
		<div style="padding: 10px; background-color: #ecf0f1;">
			<audio id="podcast-audio-debate-01" controls style="width: 100%;">
				<source type="audio/mp4" src="https://sungheeyun-podcasts-03.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/Debate - Applied_Modeling_Versus_Pure_Mathematical_Rigor.m4a">
				Your browser does not support this audio element.
			</audio>
		</div>
	</div>
</div>

# Daily Practice Problems 🗓️

Beth's **daily warm-up sessions** live on a separate page — short, casual, 15–20 minutes.
Each session has problems + a collapsible answer key so you can self-check.

[➡️ **Beth's Daily Calculus Practice**](/math/ap/calculus/bc/daily){:target="_blank"}

| Date | Topics |
|------|--------|
| [11-Mar-2026](/math/ap/calculus/bc/daily#mar-11-2026){:target="_blank"} | Limits (two methods) · Series · Integration by parts · Volumes around $y$-axis (shell vs. washer) |
| [10-Mar-2026](/math/ap/calculus/bc/daily#mar-10-2026){:target="_blank"} | Limits (two methods) · Series · FTC + chain rule · Volumes of revolution (disc & shell) |
| [09-Mar-2026](/math/ap/calculus/bc/daily#mar-09-2026){:target="_blank"} | Limits at 0 and $\infty$ · Series convergence · FTC Part 1 |

# Interactive Visualization Tools

- [{{ page.sections.iv-finite-diff }}](#iv-finite-diff)
- [{{ page.sections.iv-taylor-approximation }}](#iv-taylor-approximation)
- [{{ page.sections.iv-integral-approximation }}](#iv-integral-approximation)
- [{{ page.sections.iv-arc-length }}](#iv-arc-length)
- [{{ page.sections.iv-disc-method }}](#iv-disc-method)
- [{{ page.sections.iv-washer-method }}](#iv-washer-method)
- [{{ page.sections.iv-shell-method}}](#iv-shell-method)
- [{{ page.sections.iv-volumes}}](#iv-volumes)
- [{{ page.sections.iv-ode}}](#iv-ode)
- [{{ page.sections.iv-deri-power-functions }}](#iv-deri-power-functions)
- [{{ page.sections.iv-anti-deri-power-functions }}](#iv-anti-deri-power-functions)

# Important Topics, Patterns, and Rules

## Differentiation / Derivatives

### Definition

The [<span class="emph">derivative</span>](https://en.wikipedia.org/wiki/Derivative){:target="_blank"} is a fundamental tool that quantifies the sensitivity to change of a function's output with respect to its input.
The derivative of a function of a single variable at a chosen input value, when it exists, is <span class="emph">the slope of the tangent line</span> to the graph of the function at that point.
The tangent line is <span class="emph">the best linear approximation of the function</span> near that input value.
The derivative is often described as <span class="emph">the instantaneous rate of change</span>, the ratio of the instantaneous change in the dependent variable to that of the independent variable.
The process of finding a derivative is called <span class="emph">differentiation</span>.

A function of a real variable $\newcommand{\reals}{\mathbb{R}}\newcommand{\naturals}{\mathbb{N}}\newcommand{\series}{\sum_{n=1}^\infty a_n}\newcommand{\absseries}{\sum_{n=1}^\infty |a_n|}f(x)$ is differentiable at a point $a$ of its domain,
if its domain contains an open interval containing $a$, and the limit in \eqref{eq:def-derivative} exists.

\begin{equation}
\label{eq:def-derivative}
	\lim_{h\to 0} \frac{f(a+h)-f(a)}{h}
\end{equation}

<h4>Examples</h4>

$$
\begin{eqnarray}
\label{eq:der-examples}
\begin{array}{lcl}
	\dfrac{d}{dx} c
		&=&
			0
	\quad\mbox{for every } c \in \reals
\\
	\dfrac{d}{dx} x
		&=&
			1
\\
	\dfrac{d}{dx} x^2
		&=&
			2x
\\
	\dfrac{d}{dx} \left(\dfrac{1}{x}\right)
		&=&
			- \dfrac{1}{x^2}
\\
	\dfrac{d}{dx} \left(\dfrac{1}{x^2}\right)
		&=&
			- \dfrac{2}{x^3}
\\
	\dfrac{d}{dx} x^p
		&=&
			p x^{p-1}
				\quad\mbox{for every nonzero } p\in \reals
\\
	\dfrac{d}{dx} e^x
		&=&
			e^x
\\
	\dfrac{d}{dx} \ln x
		&=&
			\dfrac{1}{x}
\\
	\dfrac{d}{dx} \sin x
		&=&
			\cos x
\\
	\dfrac{d}{dx} \cos x
		&=&
			- \sin x
\end{array}
\end{eqnarray}
$$

#### Interactive visualization - finite difference approximations {#iv-finite-diff}

The derivative is defined as a limit, but in practice we approximate it with finite differences.
Watch how all three methods converge to the true tangent as $h \to 0$ — and notice how the
<span class="emph">centered difference</span> is dramatically more accurate than the other two!

<div id="deriv-viz" style="background:linear-gradient(135deg,#0f172a,#0f2027,#0f172a);border-radius:16px;padding:24px;margin:24px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:16px;">
    <div style="font-size:11px;letter-spacing:.3em;color:#a78bfa;text-transform:uppercase;margin-bottom:6px;">Finite Difference Approximations</div>
    <div style="font-size:22px;color:#f1f5f9;font-weight:normal;">Approximating the Derivative</div>
    <div style="font-size:12px;color:#94a3b8;font-style:italic;margin-top:4px;">Drag <em>h</em> toward 0 — watch all three methods converge to the true tangent</div>
  </div>
  <div style="display:flex;gap:8px;margin-bottom:12px;justify-content:center;flex-wrap:wrap;" id="deriv-fnbtns"></div>
  <canvas id="deriv-canvas" style="width:100%;display:block;border-radius:8px;background:#080d1a;"></canvas>

  <!-- Formula box -->
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin:14px 0;">
    <div style="background:rgba(239,68,68,.1);border:1px solid rgba(239,68,68,.4);border-radius:8px;padding:10px;text-align:center;">
      <div style="font-size:10px;color:#ef4444;letter-spacing:.1em;text-transform:uppercase;margin-bottom:4px;">Forward</div>
      <div style="font-size:12px;color:#fca5a5;font-style:italic;">[f(x+h)−f(x)] / h</div>
      <div style="font-size:13px;color:#ef4444;font-family:monospace;margin-top:4px;" id="deriv-fwd-val">—</div>
    </div>
    <div style="background:rgba(59,130,246,.1);border:1px solid rgba(59,130,246,.4);border-radius:8px;padding:10px;text-align:center;">
      <div style="font-size:10px;color:#3b82f6;letter-spacing:.1em;text-transform:uppercase;margin-bottom:4px;">Backward</div>
      <div style="font-size:12px;color:#93c5fd;font-style:italic;">[f(x)−f(x−h)] / h</div>
      <div style="font-size:13px;color:#3b82f6;font-family:monospace;margin-top:4px;" id="deriv-bwd-val">—</div>
    </div>
    <div style="background:rgba(34,197,94,.1);border:1px solid rgba(34,197,94,.4);border-radius:8px;padding:10px;text-align:center;">
      <div style="font-size:10px;color:#22c55e;letter-spacing:.1em;text-transform:uppercase;margin-bottom:4px;">Centered ⭐</div>
      <div style="font-size:12px;color:#86efac;font-style:italic;">[f(x+h)−f(x−h)] / 2h</div>
      <div style="font-size:13px;color:#22c55e;font-family:monospace;margin-top:4px;" id="deriv-ctr-val">—</div>
    </div>
  </div>
  <div style="background:rgba(167,139,250,.08);border:1px solid rgba(167,139,250,.3);border-radius:8px;padding:10px;text-align:center;margin-bottom:14px;">
    <span style="color:#94a3b8;font-size:12px;">True f′(x) = </span>
    <span style="color:#a78bfa;font-size:15px;font-family:monospace;" id="deriv-true-val">—</span>
    &nbsp;&nbsp;
    <span style="color:#64748b;font-size:11px;" id="deriv-error-summary"></span>
  </div>

  <!-- x slider -->
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
    <span style="color:#94a3b8;font-size:13px;min-width:72px;font-style:italic;" id="deriv-xlabel">x = 1.00</span>
    <input id="deriv-xslider" type="range" min="-200" max="200" value="100" style="flex:1;accent-color:#a78bfa;" />
    <span style="color:#64748b;font-size:11px;min-width:72px;text-align:right;">move point x</span>
  </div>
  <!-- h slider -->
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
    <span style="color:#94a3b8;font-size:13px;min-width:72px;font-style:italic;" id="deriv-hlabel">h = 1.00</span>
    <input id="deriv-hslider" type="range" min="1" max="200" value="100" style="flex:1;accent-color:#f97316;" />
    <span style="color:#64748b;font-size:11px;min-width:72px;text-align:right;">h → 0 for exact</span>
  </div>

  <div style="text-align:center;font-size:11px;color:#475569;">
    Red = forward &nbsp;|&nbsp; Blue = backward &nbsp;|&nbsp; Green = centered &nbsp;|&nbsp; White = true tangent &nbsp;|&nbsp; Orange dot = point x
  </div>
</div>

<script>
(function(){
  var DFNS = {
    "sin x": {
      f:  function(x){ return Math.sin(x); },
      df: function(x){ return Math.cos(x); },
      label: "sin(x)", xmin: -2*Math.PI, xmax: 2*Math.PI, ymin: -1.8, ymax: 1.8
    },
    "x³−3x": {
      f:  function(x){ return x*x*x - 3*x; },
      df: function(x){ return 3*x*x - 3; },
      label: "x³−3x", xmin: -2.5, xmax: 2.5, ymin: -4, ymax: 4
    },
    "eˣ": {
      f:  function(x){ return Math.exp(x); },
      df: function(x){ return Math.exp(x); },
      label: "eˣ", xmin: -2.5, xmax: 2.5, ymin: -0.5, ymax: 10
    },
    "ln x": {
      f:  function(x){ return x > 0 ? Math.log(x) : NaN; },
      df: function(x){ return x > 0 ? 1/x : NaN; },
      label: "ln(x)", xmin: 0.05, xmax: 5, ymin: -2.5, ymax: 2
    }
  };
  var DFN_KEYS = Object.keys(DFNS);
  var curDFn = "sin x";
  var curX = 1.0;
  var curH = 1.0;
  var PAD = {top:24,right:24,bottom:40,left:48};
  var DW, DH;
  var dcanvas = document.getElementById("deriv-canvas");

  function dtoC(x,y,xmin,xmax,ymin,ymax){
    var cx = PAD.left+(x-xmin)/(xmax-xmin)*(DW-PAD.left-PAD.right);
    var cy = DH-PAD.bottom-(y-ymin)/(ymax-ymin)*(DH-PAD.top-PAD.bottom);
    return [cx,cy];
  }

  function dresize(){
    var cont=document.getElementById("deriv-viz");
    DW=cont.clientWidth-48; DH=Math.round(DW*0.48);
    dcanvas.width=DW; dcanvas.height=DH;
    ddraw();
  }

  function drawLine(ctx,x1,y1,x2,y2){ ctx.beginPath(); ctx.moveTo(x1,y1); ctx.lineTo(x2,y2); ctx.stroke(); }

  function ddraw(){
    var ctx=dcanvas.getContext("2d");
    ctx.clearRect(0,0,DW,DH);
    var cfg=DFNS[curDFn];
    var xmin=cfg.xmin,xmax=cfg.xmax,ymin=cfg.ymin,ymax=cfg.ymax;
    var f=cfg.f, df=cfg.df;
    var x=curX, h=curH;

    // clamp x to visible range (no h-based clamping — let diff formulas return NaN when out of domain)
    var xc = Math.max(xmin+0.001, Math.min(xmax-0.001, x));

    // Grid
    ctx.strokeStyle="rgba(148,163,184,.1)"; ctx.lineWidth=1;
    for(var yi=Math.ceil(ymin);yi<=Math.floor(ymax);yi++){
      var gy=dtoC(0,yi,xmin,xmax,ymin,ymax)[1];
      drawLine(ctx,PAD.left,gy,DW-PAD.right,gy);
    }

    // Axes
    ctx.strokeStyle="#334155"; ctx.lineWidth=1.5;
    var ay=dtoC(0,0,xmin,xmax,ymin,ymax)[1];
    var ax=dtoC(0,0,xmin,xmax,ymin,ymax)[0];
    drawLine(ctx,PAD.left,ay,DW-PAD.right+8,ay);
    drawLine(ctx,ax,DH-PAD.bottom,ax,PAD.top-8);

    // Tick labels
    ctx.font="11px Georgia,serif"; ctx.fillStyle="#64748b";
    var xstep=(xmax-xmin)>10?2:1;
    for(var xi=Math.ceil(xmin);xi<=Math.floor(xmax);xi+=xstep){
      var tp=dtoC(xi,0,xmin,xmax,ymin,ymax);
      ctx.textAlign="center"; ctx.fillText(xi,tp[0],tp[1]+14);
    }
    var ystep=(ymax-ymin)>10?2:1;
    for(var yi2=Math.ceil(ymin);yi2<=Math.floor(ymax);yi2+=ystep){
      if(yi2===0) continue;
      var tp2=dtoC(0,yi2,xmin,xmax,ymin,ymax);
      ctx.textAlign="right"; ctx.fillText(yi2,tp2[0]-5,tp2[1]+4);
    }

    // True function
    ctx.strokeStyle="#f8fafc"; ctx.lineWidth=2.2;
    ctx.shadowColor="rgba(248,250,252,.3)"; ctx.shadowBlur=4;
    ctx.beginPath(); var fstarted=false;
    for(var i=0;i<=500;i++){
      var xv=xmin+i/500*(xmax-xmin), fv=f(xv);
      if(!isFinite(fv)||fv<ymin-5||fv>ymax+5){fstarted=false;continue;}
      var p=dtoC(xv,fv,xmin,xmax,ymin,ymax);
      fstarted?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]); fstarted=true;
    }
    ctx.stroke(); ctx.shadowBlur=0;

    // Helper: draw a secant / tangent line through (x0,y0) with slope m
    function drawTangentLine(color, lw, x0, y0, m, dashArr){
      // find endpoints within view
      var t1=(xmin-x0)/m+0, t2=(xmax-x0)/m+0; // x extent
      var xl=x0+(xmin-x0), xr=x0+(xmax-x0);
      var p1=dtoC(xmin, y0+m*(xmin-x0),xmin,xmax,ymin,ymax);
      var p2=dtoC(xmax, y0+m*(xmax-x0),xmin,xmax,ymin,ymax);
      ctx.strokeStyle=color; ctx.lineWidth=lw;
      if(dashArr) ctx.setLineDash(dashArr); else ctx.setLineDash([]);
      drawLine(ctx,p1[0],p1[1],p2[0],p2[1]);
      ctx.setLineDash([]);
    }

    var fy=f(xc), dfy=df(xc);
    var fwd=(f(xc+h)-f(xc))/h;
    var bwd=(f(xc)-f(xc-h))/h;
    var ctr=(f(xc+h)-f(xc-h))/(2*h);

    // True tangent (white dashed)
    if(isFinite(dfy)) drawTangentLine("rgba(248,250,252,.6)",1.5,xc,fy,dfy,[6,4]);

    // Forward secant (red)
    if(isFinite(fwd)) drawTangentLine("rgba(239,68,68,.8)",2,xc,fy,fwd,[]);

    // Backward secant (blue)
    if(isFinite(bwd)) drawTangentLine("rgba(59,130,246,.8)",2,xc,fy,bwd,[]);

    // Centered secant (green)
    if(isFinite(ctr)) drawTangentLine("rgba(34,197,94,.9)",2.5,xc,fy,ctr,[]);

    // Mark x, x+h, x-h on curve
    function dotOnCurve(xv,color,r){
      var yv=f(xv); if(!isFinite(yv)) return;
      var p=dtoC(xv,yv,xmin,xmax,ymin,ymax);
      ctx.fillStyle=color; ctx.shadowColor=color; ctx.shadowBlur=8;
      ctx.beginPath(); ctx.arc(p[0],p[1],r,0,Math.PI*2); ctx.fill();
      ctx.shadowBlur=0;
    }
    dotOnCurve(xc,        "#f97316",6);   // x — orange
    dotOnCurve(xc+h,      "#ef4444",4);   // x+h — red
    dotOnCurve(xc-h,      "#3b82f6",4);   // x-h — blue

    // f(x) label
    var lx=xmin+(xmax-xmin)*0.75, ly=f(lx);
    if(isFinite(ly)){
      var lp=dtoC(lx,ly,xmin,xmax,ymin,ymax);
      ctx.fillStyle="#f8fafc"; ctx.font="italic 13px Georgia,serif"; ctx.textAlign="left";
      ctx.fillText(cfg.label,lp[0]+6,lp[1]-8);
    }

    // Update value displays
    function fmt(v){ return isFinite(v)?v.toFixed(5):"—"; }
    function errFmt(approx,truth){
      if(!isFinite(approx)||!isFinite(truth)) return "";
      var e=Math.abs(approx-truth);
      return e<1e-9?"≈ 0":e.toFixed(6);
    }
    document.getElementById("deriv-fwd-val").textContent=fmt(fwd)+" (err: "+errFmt(fwd,dfy)+")";
    document.getElementById("deriv-bwd-val").textContent=fmt(bwd)+" (err: "+errFmt(bwd,dfy)+")";
    document.getElementById("deriv-ctr-val").textContent=fmt(ctr)+" (err: "+errFmt(ctr,dfy)+")";
    document.getElementById("deriv-true-val").textContent=fmt(dfy);
    // error ratio summary
    if(isFinite(fwd)&&isFinite(bwd)&&isFinite(ctr)&&isFinite(dfy)){
      var ef=Math.abs(fwd-dfy), eb=Math.abs(bwd-dfy), ec=Math.abs(ctr-dfy);
      if(ec>1e-12&&ef>1e-12){
        var ratio=ef/ec;
        document.getElementById("deriv-error-summary").textContent=
          "Centered is ~"+ratio.toFixed(0)+"× more accurate than forward!";
      } else {
        document.getElementById("deriv-error-summary").textContent="All converged to true value ✓";
      }
    }
  }

  // Function buttons
  var dbtnC=document.getElementById("deriv-fnbtns");
  DFN_KEYS.forEach(function(k){
    var btn=document.createElement("button");
    btn.id="deriv-fnbtn-"+k; btn.textContent=k;
    function styleAll(){
      DFN_KEYS.forEach(function(kk){
        var b=document.getElementById("deriv-fnbtn-"+kk); if(!b) return;
        b.style.cssText=kk===curDFn
          ?"padding:6px 14px;border-radius:8px;border:2px solid #a78bfa;background:rgba(167,139,250,.2);color:#a78bfa;font-size:13px;font-family:Georgia,serif;cursor:pointer;font-weight:bold;"
          :"padding:6px 14px;border-radius:8px;border:2px solid rgba(148,163,184,.2);background:rgba(10,15,30,.5);color:#94a3b8;font-size:13px;font-family:Georgia,serif;cursor:pointer;";
      });
    }
    btn.addEventListener("click",function(){
      curDFn=k;
      // reset x to center of range and update slider bounds to match function domain
      var cfg=DFNS[k]; curX=(cfg.xmin+cfg.xmax)/2;
      var sl=document.getElementById("deriv-xslider");
      sl.min=Math.round(cfg.xmin*100); sl.max=Math.round(cfg.xmax*100);
      sl.value=Math.round(curX*100);
      document.getElementById("deriv-xlabel").textContent="x = "+curX.toFixed(2);
      styleAll(); ddraw();
    });
    btn.style.cssText=k===curDFn
      ?"padding:6px 14px;border-radius:8px;border:2px solid #a78bfa;background:rgba(167,139,250,.2);color:#a78bfa;font-size:13px;font-family:Georgia,serif;cursor:pointer;font-weight:bold;"
      :"padding:6px 14px;border-radius:8px;border:2px solid rgba(148,163,184,.2);background:rgba(10,15,30,.5);color:#94a3b8;font-size:13px;font-family:Georgia,serif;cursor:pointer;";
    dbtnC.appendChild(btn);
  });

  document.getElementById("deriv-xslider").addEventListener("input",function(){
    curX=+this.value/100;
    document.getElementById("deriv-xlabel").textContent="x = "+curX.toFixed(2);
    ddraw();
  });
  document.getElementById("deriv-hslider").addEventListener("input",function(){
    curH=+this.value/100;
    document.getElementById("deriv-hlabel").textContent="h = "+curH.toFixed(2);
    ddraw();
  });

  // Initialize slider bounds to match the default function (sin x has xmin=-2π, xmax=2π,
  // but the HTML slider is hardcoded min="-200" max="200" — without this init block the
  // x slider is stuck at [-2, 2] on first load until the user clicks another function and back.
  (function(){
    var cfg = DFNS[curDFn];
    curX = (cfg.xmin + cfg.xmax) / 2;
    var sl = document.getElementById("deriv-xslider");
    sl.min   = Math.round(cfg.xmin * 100);
    sl.max   = Math.round(cfg.xmax * 100);
    sl.value = Math.round(curX * 100);
    document.getElementById("deriv-xlabel").textContent = "x = " + curX.toFixed(2);
  })();

  window.addEventListener("resize",dresize);
  dresize();
})();
</script>

### Chain rule {#chain-rule}

\begin{equation}
\label{eq:chain-rule}
\frac{d}{dx} f(g(x)) = f'(g(x)) g'(x)
\end{equation}

We can recursively apply this to derive,
*e.g.*, the following rules.

\begin{equation}
\label{eq:chain-rule-3}
\frac{d}{dx} f(g(h(x))) = f'(g(h(x))) g'(h(x)) h'(x)
\end{equation}

\begin{equation}
\label{eq:chain-rule-4}
\frac{d}{dx} f(g(h(p(x)))) = f'(g(h(p(x)))) g'(h(p(x))) h'(p(x)) p'(x)
\end{equation}

$$
\begin{eqnarray}
\label{eq:chain-rule-5}
\begin{array}{l}
\dfrac{d}{dx} f(g(h(p(q(x)))))
\\
= f'(g(h(p(q(x))))) g'(h(p(q(x)))) h'(p(q(x))) p'(q(x)) q'(x)
\end{array}
\end{eqnarray}
$$

And in general,
for $n$ functions $f_1, f_2, \ldots, f_n$,
the cursively applying the [chain rule](#chain-rule) $n$ times yields

$$
\begin{eqnarray}
\label{eq:chain-rule-n}
\begin{array}{rcl}
	\dfrac{d}{dx} f_1(f_2(\cdots f_n(x)\cdots))
		&=&
			f_1'(f_2(\cdots f_n(x)\cdots))
			f_2'(\cdots f_n(x)\cdots)
	\\
		&&
			\cdots
			f_{n-1}'(f_n(x)) f_n'(x)
\end{array}
\end{eqnarray}
$$

If we express this using the standard function composition notion $f \circ g$,
*i.e.*, $(f\circ g)(x)$ is defined to be $f(g(x))$,

$$
\begin{eqnarray}
\label{eq:chain-rule-n-fcn-comp}
\begin{array}{rcl}
	\dfrac{d}{dx} (f_1\circ f_2\circ f_3\circ \cdots \circ f_n)(x)
		&=&
			f_1'( (f_2\circ f_3\circ \cdots \circ f_n)(x) )
	\\
		&&
			f_2'( (f_3\circ \cdots \circ f_n)(x) )
	\\
		&&
			\qquad
			\qquad
			\vdots
	\\
		&&
			f_{n-2}'((f_{n-1}\circ f_n)(x))
	\\
		&&
			f_{n-1}'(f_n(x))
			f_n'(x)
\end{array}
\end{eqnarray}
$$

### Basic properties {#differentiation-basic-properties}

For differentiable functions $f$ and $g$, and a constant $c$, the following rules hold.

<span id="differentiation-linearity"></span>
<h4>Linearity</h4>

Differentiation is a <span class="emph">linear</span> operation!

$$
	(f + g)' = f' + g'
	\;
	\mbox{and}
	\;
	(cf)' = c f'
$$

So in one line

\begin{equation}
\label{eq:der-linearity}
	(a f + b g)' = a f' + b g'
\end{equation}

<span class="emph">This is arguably the single most useful structural fact about derivatives.</span>

<span id="differentiation-product-rule"></span>
<h4>Product rule</h4>

The derivative of a product is <span style="color: red; font-weight: bold;">not</span> just $f'g'$!

\begin{equation}
\label{eq:der-product-rule}
(fg)' = f'g + fg'
\end{equation}

A handy way to remember this
&ndash;
<span class="emph">"derivative of first times second, plus first times derivative of second."</span>

> **Why the product rule matters for integration** The product rule $(fg)' = f'g + fg'$ can be rearranged as
> $f'g = (fg)' - fg'$, and integrating both sides gives exactly
> the **integration by parts** formula — so the product rule is the *parent* of one of the most important integration techniques!
> We'll see this connection in the integration section below.

<h4>Quotient rule</h4>

It follows directly from the chain rule and the product rule!

\begin{equation}
\label{eq:der-quotient-rule}
	\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}
\end{equation}

because
<!--
the linearity of differentiation \eqref{eq:der-linearity},
-->
the chain rule \eqref{eq:chain-rule}
and
the product rule \eqref{eq:der-product-rule}
(together with basic derivative formulas in \eqref{eq:der-examples})
imply

$$
	\left(\frac{f}{g}\right)'
		=
			\left(f\cdot\frac{1}{g}\right)'
		=
			f' \left(\frac{1}{g}\right) + f \left(\frac{1}{g}\right)'
		=
			f' \cdot \frac{1}{g} - f \cdot \frac{g'}{g^2}
		=
			\frac{f'g - fg'}{g^2}
$$

A mnemonic
&ndash;
<span class="emph">"low d-high minus high d-low, over low squared."</span>

Indeed,
using
the linearity of differentiation \eqref{eq:der-linearity}
with the two rules,
*i.e.*,
the chain rule \eqref{eq:chain-rule}
and
the product rule \eqref{eq:der-product-rule}
(together with basic derivative formulas in \eqref{eq:der-examples}),
<span style="color: red;">we can derive every single formula related to differentiation in the whole universe!
Actually, even in every multiverse! &#x2605;^^&#x2605;</span><sup><a href="#footnote01" id="ref01">1</a></sup>

### Mean value theorem {#mean-value-theorem}

The [mean value theorem](https://en.wikipedia.org/wiki/Mean_value_theorem){:target="_blank"} (or Lagrange's mean value theorem) states, roughly,
that for a given planar arc between two endpoints,
there is at least one point at which the tangent to the arc is parallel to the secant through its endpoints.
It is one of the most important results in real analysis.

Let $f:[a,b]\to\reals$ be a continuous function on the closed interval $[a,b]$,
and differentiable on the open interval $(a,b)$,
where $a< b$. Then there exists some $c$ in $(a,b)$ such that

\begin{equation}
	f'(c) = \frac{f(b)-f(a)}{b-a}
\end{equation}

### L'H&ocirc;pital's rule

[L'H&ocirc;pital's rule](https://en.wikipedia.org/wiki/L%27H%C3%B4pital%27s_rule){:target="_blank"}
states that for functions $f$ and $g$ which are defined on
an open interval $I$ and differentiable on $$I\backslash\{c\}$$
for a (possibly infinite) accumulation point $c$ of $I$,
if

$$
	\lim_{x\to c} f(x) = \lim_{x\to c} g(x) = 0 \mbox{ or } \pm \infty
$$

and $\lim_{x\to c} \dfrac{f'(x)}{g'(x)}$ exists, then

\begin{equation}
\label{eq:lhospital-rule}
	\lim_{x\to c} \frac{f(x)}{g(x)}
	=
	\lim_{x\to c} \frac{f'(x)}{g'(x)}
\end{equation}

**Examples**

$$
\begin{eqnarray*}
\lim_{x\to 0} \frac{2x^2-3x}{3x^2+3x}
	&=&
		\lim_{x\to 0} \frac{4x-3}{6x+3} = -1
\\
\lim_{x\to \infty} \frac{2x^2+3x}{2+x^2}
	&=&
		\lim_{x\to \infty} \frac{2x+3}{2x}
		=
		\lim_{x\to \infty} \frac{2}{2} = 1
\\
\lim_{x\to 0} \frac{\sin(x)}{x}
	&=&
		\lim_{x\to 0} \frac{\cos(x)}{1} = 1
\\
\lim_{x\to \infty} xe^{-x}
	&=&
		\lim_{x\to \infty} \frac{x}{e^x}
		=
		\lim_{x\to \infty} \frac{1}{e^x} = 0
\\
\lim_{x\to \infty} x^2 e^{-x}
	&=&
		\lim_{x\to \infty} \frac{x^2}{e^x}
		=
		\lim_{x\to \infty} \frac{2x}{e^x}
		=
		\lim_{x\to \infty} \frac{2}{e^x} = 0
\\
\lim_{x\to \infty} \frac{\ln(x)}{x}
	&=&
		\lim_{x\to \infty} \frac{1/x}{1} = 0
\\
\lim_{x\to 0^+} x\ln x
	&=&
		\lim_{x\to 0^+} \frac{\ln(x)}{1/x} = \lim_{x\to 0^+} \frac{1/x}{-1/x^2}
\\
	&=&
		\lim_{x\to 0^+} (-x) = 0
\\
\lim_{x\to \infty} \frac{\ln(a+b\, e^{cx})}{x}
	&=&
		\lim_{x\to \infty} \frac{bc\, e^{cx}/(a+b\, e^{cx})}{1}
\\
	&=&
		c \quad \mbox{for } a,b,c>0
\\
\lim_{x\to 0} \frac{e^x-1}{x}
	&=&
		\lim_{x\to 0} \frac{e^x}{1} = 1
\\
\lim_{x\to 0} \frac{e^x-1}{x^2+x}
	&=&
		\lim_{x\to 0} \frac{e^x}{2x+1} = 1
\\
\lim_{x\to 0} \frac{2\sin x - \sin(2x)}{x-\sin x}
	&=&
		\lim_{x\to 0} \frac{2\cos x - 2\cos(2x)}{1-\cos x}
\\
	&=&
		\lim_{x\to 0} \frac{-2\sin x + 4\sin(2x)}{\sin x}
\\
	&=&
		\lim_{x\to 0} \frac{-2\cos x + 8\cos(2x)}{\cos x} = 6
\\
\lim_{h\to 0} \frac{f(x+h)+f(x-h)-2f(x)}{h^2}
	&=&
		\lim_{h\to 0} \frac{f(x+h)+f(x-h)-2f(x)}{h^2}
\\
	&=&
		\lim_{h\to 0} \frac{f'(x+h)-f'(x-h)}{2h}
\\
	&=&
		\lim_{h\to 0} \frac{f^{\prime\prime}(x+h)+f^{\prime\prime}(x-h)}{2} = f^{\prime\prime}(x)
\end{eqnarray*}
$$

**Caveat**

$$
\begin{eqnarray*}
\lim_{x\to 0} \frac{x}{5}
	&\neq&
		\lim_{x\to 0} \frac{1}{0}
\end{eqnarray*}
$$

### Taylor series {#taylor-series}

The [<span class="define">Taylor series</span> or <span class="define">Taylor expansion</span>](https://en.wikipedia.org/wiki/Taylor_series){:target="_blank"}
of a function is an infinite sum of terms that are expressed in terms of the function's derivatives at a single point.
For most common functions, the function and the sum of its Taylor series are equal near this point.
Taylor series are named after [Brook Taylor](https://en.wikipedia.org/wiki/Brook_Taylor){:target="_blank"},
who introduced them in 1715.
A Taylor series is also called a <span class="define">Maclaurin series</span>
when 0 is the point where the derivatives are considered,
after [Colin Maclaurin](https://en.wikipedia.org/wiki/Colin_Maclaurin){:target="_blank"},
who made extensive use of this special case of Taylor series in the 18th century.

The Taylor series of a real or complex-valued function $f(x)$,
that is infinitely differentiable at a real or complex number $a$, is the power series

\begin{equation}
\label{eq:taylor-series}
	\sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!} (x-a)^n
=
	f(a)
	+ \frac{f'(a)}{1!}(x-a)
	+ \frac{f^{\prime\prime}(a)}{2!}(x-a)^2
	+ \cdots
\end{equation}

where $n!$ denotes the factorial of $n$,
the function $f^{(n)}(a)$ denotes the $n$-th derivative of $f$ evaluated at the point $a$,
the derivative of order zero of $f$ is defined to be $f$ itself,
and
$(x − a)^0$ and $0!$ are both defined to be $1$.

With $a = 0$, the <span class="define">Maclaurin series</span> takes the form

\begin{equation}
\label{eq:maclaurin-series}
	\sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!} x^n
=
	f(0)
	+ \frac{f'(0)}{1!}x
	+ \frac{f^{\prime\prime}(0)}{2!}x^2
	+ \cdots
\end{equation}

#### Interactive visualization - Taylor approximation {#iv-taylor-approximation}

Watch how each successive Taylor term *sculpts* the approximation closer and closer to the true curve.
Drag the **order** slider to add terms one by one, and drag the **center** slider to move the expansion point $a$.
Try different functions — $e^x$ converges everywhere, while $\ln(1+x)$ only converges for $|x| \le 1$!

<div id="taylor-viz" style="background:linear-gradient(135deg,#0f172a,#1a1040,#0f172a);border-radius:16px;padding:24px;margin:24px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:16px;">
    <div style="font-size:11px;letter-spacing:.3em;color:#34d399;text-transform:uppercase;margin-bottom:6px;">Taylor / Maclaurin Series</div>
    <div style="font-size:22px;color:#f1f5f9;font-weight:normal;">Polynomial Approximation</div>
    <div style="font-size:12px;color:#94a3b8;font-style:italic;margin-top:4px;">Adding one term at a time — watch the polynomial curve hug the function</div>
  </div>

  <!-- Function selector -->
  <div style="display:flex;gap:8px;margin-bottom:14px;justify-content:center;flex-wrap:wrap;" id="taylor-fnbtns"></div>

  <canvas id="taylor-canvas" style="width:100%;display:block;border-radius:8px;background:#0a0f1e;"></canvas>

  <!-- Formula display -->
  <div id="taylor-formula" style="background:rgba(20,30,60,.7);border:1px solid rgba(52,211,153,.3);border-radius:10px;padding:12px 16px;margin:14px 0;text-align:center;font-size:13px;color:#f1f5f9;min-height:44px;line-height:1.7;box-shadow:0 0 16px rgba(52,211,153,.1);"></div>

  <!-- Order slider -->
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
    <span style="color:#94a3b8;font-size:13px;min-width:90px;font-style:italic;" id="taylor-orderlabel">order = 0</span>
    <input id="taylor-slider" type="range" min="0" max="30" value="0" style="flex:1;accent-color:#34d399;" />
    <span style="color:#64748b;font-size:11px;min-width:60px;text-align:right;">higher → better</span>
  </div>

  <!-- Center slider -->
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
    <span style="color:#94a3b8;font-size:13px;min-width:90px;font-style:italic;" id="taylor-centerlabel">a = 0</span>
    <input id="taylor-cslider" type="range" min="-200" max="200" value="0" style="flex:1;accent-color:#fb923c;" />
    <span style="color:#64748b;font-size:11px;min-width:60px;text-align:right;">move center</span>
  </div>

  <!-- Stats row -->
  <div style="display:flex;gap:10px;" id="taylor-stats"></div>
  <div style="text-align:center;margin-top:12px;font-size:11px;color:#475569;">
    Green = true function &nbsp;|&nbsp; Orange = Taylor approximation &nbsp;|&nbsp; Orange dot = expansion point <em>a</em>
  </div>
</div>

<script>
(function(){
  // ── function definitions ──────────────────────────────────────────────
  var FNS = {
    "sin x": {
      f: function(x){ return Math.sin(x); },
      // coefficients of Maclaurin: sin x = x - x³/3! + x⁵/5! - ...
      coeff: function(n, a){
        // General Taylor: sum f^(n)(a)/n! * (x-a)^n
        // We'll compute numerically
        return null; // use numerical differentiation
      },
      label: "sin(x)",
      xmin: -2*Math.PI, xmax: 2*Math.PI, ymin: -2.5, ymax: 2.5,
      cmin: -628, cmax: 628   // ≈ ±2π ×100
    },
    "cos x": {
      f: function(x){ return Math.cos(x); },
      label: "cos(x)",
      xmin: -2*Math.PI, xmax: 2*Math.PI, ymin: -2.5, ymax: 2.5,
      cmin: -628, cmax: 628
    },
    "eˣ": {
      f: function(x){ return Math.exp(x); },
      label: "eˣ",
      xmin: -3, xmax: 3, ymin: -1, ymax: 12,
      cmin: -300, cmax: 300
    },
    "ln(1+x)": {
      f: function(x){ return (x > -1) ? Math.log(1+x) : NaN; },
      label: "ln(1+x)",
      xmin: -1.5, xmax: 3, ymin: -3, ymax: 3,
      cmin: -80, cmax: 280    // a must stay > -1; keep comfortable margin
    },
    "x²+x−2": {
      f: function(x){ return x*x + x - 2; },
      label: "(x−1)(x+2)",
      xmin: -3.5, xmax: 3.5, ymin: -3.5, ymax: 8,
      note: "Exact at order 2!",
      cmin: -350, cmax: 350
    },
    "x⁵−5x³+4x": {
      f: function(x){ return x*x*x*x*x - 5*x*x*x + 4*x; },
      label: "x⁵−5x³+4x",
      xmin: -2.5, xmax: 2.5, ymin: -5, ymax: 5,
      note: "Exact at order 5!",
      cmin: -250, cmax: 250
    }
  };
  var FN_KEYS = Object.keys(FNS);
  var curFn = "sin x";
  var curOrder = 0;
  var curA = 0;

  var PAD = {top:28, right:28, bottom:44, left:52};
  var W, H;
  var canvas = document.getElementById("taylor-canvas");

  function factorial(n){ var r=1; for(var i=2;i<=n;i++) r*=i; return r; }

  // ── Exact analytical nth derivative at point a for each function ──────
  // Returns f^(n)(a) exactly — no numerical error.
  function exactDeriv(fn, n, a) {
    if(fn === "eˣ") {
      // d^n/dx^n e^x = e^x
      return Math.exp(a);
    }
    if(fn === "sin x") {
      // cycle: sin, cos, -sin, -cos, sin, ...
      var cycle = n % 4;
      if(cycle === 0) return  Math.sin(a);
      if(cycle === 1) return  Math.cos(a);
      if(cycle === 2) return -Math.sin(a);
                      return -Math.cos(a);
    }
    if(fn === "cos x") {
      // cycle: cos, -sin, -cos, sin, cos, ...
      var cycle = n % 4;
      if(cycle === 0) return  Math.cos(a);
      if(cycle === 1) return -Math.sin(a);
      if(cycle === 2) return -Math.cos(a);
                      return  Math.sin(a);
    }
    if(fn === "ln(1+x)") {
      // f(x)   = ln(1+x),  f^(0)(a) = ln(1+a)
      // f^(n)(x) = (-1)^(n+1) * (n-1)! / (1+x)^n  for n >= 1
      if(a <= -1) return NaN;
      if(n === 0) return Math.log(1 + a);
      var sign = (n % 2 === 1) ? 1 : -1;
      return sign * factorial(n - 1) / Math.pow(1 + a, n);
    }
    if(fn === "x²+x−2") {
      // f(x) = x² + x - 2  (degree 2 polynomial)
      // f^(0)(a) = a²+a-2,  f^(1)(a) = 2a+1,  f^(2)(a) = 2,  f^(n≥3)(a) = 0
      if(n === 0) return a*a + a - 2;
      if(n === 1) return 2*a + 1;
      if(n === 2) return 2;
      return 0;
    }
    if(fn === "x⁵−5x³+4x") {
      // f(x) = x⁵ - 5x³ + 4x  (degree 5 polynomial, roots at 0,±1,±2)
      // f^(0)(a) = a⁵-5a³+4a
      // f^(1)(a) = 5a⁴-15a²+4
      // f^(2)(a) = 20a³-30a
      // f^(3)(a) = 60a²-30
      // f^(4)(a) = 120a
      // f^(5)(a) = 120
      // f^(n≥6)(a) = 0
      if(n === 0) return a*a*a*a*a - 5*a*a*a + 4*a;
      if(n === 1) return 5*a*a*a*a - 15*a*a + 4;
      if(n === 2) return 20*a*a*a - 30*a;
      if(n === 3) return 60*a*a - 30;
      if(n === 4) return 120*a;
      if(n === 5) return 120;
      return 0;
    }
    return NaN;
  }

  // Evaluate Taylor polynomial of given order centered at a
  function taylorVal(fn, order, a, x) {
    var sum = 0;
    for(var n=0; n<=order; n++){
      var dn = exactDeriv(fn, n, a);
      if(!isFinite(dn)) return NaN;
      sum += dn / factorial(n) * Math.pow(x - a, n);
    }
    return sum;
  }

  // ── Canvas helpers ────────────────────────────────────────────────────
  function toC(x, y, xmin, xmax, ymin, ymax){
    var cx = PAD.left + (x - xmin)/(xmax - xmin)*(W - PAD.left - PAD.right);
    var cy = H - PAD.bottom - (y - ymin)/(ymax - ymin)*(H - PAD.top - PAD.bottom);
    return [cx, cy];
  }

  function resize(){
    var cont = document.getElementById("taylor-viz");
    W = cont.clientWidth - 48;
    H = Math.round(W * 0.52);
    canvas.width = W; canvas.height = H;
    draw();
  }

  // ── Build term label for formula display ─────────────────────────────
  function termStr(n, a, dn) {
    if(!isFinite(dn) || Math.abs(dn) < 1e-10) return null;
    var coef = dn / factorial(n);
    var sign = coef >= 0 ? "+" : "−";
    var absCoef = Math.abs(coef);
    var coefStr = absCoef.toFixed(3).replace(/\.?0+$/, "");
    if(coefStr === "1" && n > 0) coefStr = "";
    var xpart = n === 0 ? "" : n === 1 ? (a===0?"x":"(x−"+a.toFixed(1)+")") : (a===0?"x":"(x−"+a.toFixed(1)+")")+"<sup>"+n+"</sup>";
    return sign + " " + coefStr + xpart;
  }

  function updateFormula(){
    var terms = [];
    for(var n=0; n<=curOrder; n++){
      var dn = exactDeriv(curFn, n, curA);
      var s = termStr(n, curA, dn);
      if(s) terms.push(s);
    }
    var str = terms.join(" ").replace(/^\+\s*/,"");
    var order_names = ["0th","1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th","21st","22nd","23rd","24th","25th","26th","27th","28th","29th","30th"];
    var note = FNS[curFn].note || "";
    var exactFlag = (curFn === "x²+x−2" && curOrder >= 2) || (curFn === "x⁵−5x³+4x" && curOrder >= 5);
    var noteHtml = exactFlag ? ' &nbsp;<span style="color:#4ade80;font-size:11px;font-style:normal;">✓ EXACT FIT</span>' : (note ? ' &nbsp;<span style="color:#94a3b8;font-size:11px;">'+note+'</span>' : "");
    document.getElementById("taylor-formula").innerHTML =
      '<span style="color:#94a3b8;font-size:12px;">'+order_names[curOrder]+'-order approx:&nbsp;&nbsp;</span>'
      +'<span style="color:#fb923c;">T<sub>'+curOrder+'</sub>(x) = '+str+'</span>'+noteHtml;
  }

  // ── Max error in visible window ───────────────────────────────────────
  function maxError(){
    var cfg = FNS[curFn];
    var f = cfg.f;
    var worst = 0;
    var steps = 80;
    for(var i=0;i<=steps;i++){
      var x = cfg.xmin + i/steps*(cfg.xmax - cfg.xmin);
      var tv = taylorVal(curFn, curOrder, curA, x);
      var fv = f(x);
      if(isFinite(tv) && isFinite(fv)){
        var err = Math.abs(tv - fv);
        if(err > worst) worst = err;
      }
    }
    return worst;
  }

  // ── Main draw ─────────────────────────────────────────────────────────
  function draw(){
    var ctx = canvas.getContext("2d");
    ctx.clearRect(0,0,W,H);
    var cfg = FNS[curFn];
    var xmin=cfg.xmin, xmax=cfg.xmax, ymin=cfg.ymin, ymax=cfg.ymax;
    var f = cfg.f;
    var steps = 500;

    // Grid
    ctx.strokeStyle = "rgba(148,163,184,.12)"; ctx.lineWidth = 1;
    var yStep = (ymax-ymin) > 8 ? 2 : 1;
    for(var y=Math.ceil(ymin); y<=Math.floor(ymax); y+=yStep){
      var gy = toC(0,y,xmin,xmax,ymin,ymax)[1];
      ctx.beginPath(); ctx.moveTo(PAD.left,gy); ctx.lineTo(W-PAD.right,gy); ctx.stroke();
    }
    var xStep = (xmax-xmin) > 8 ? 2 : 1;
    for(var x=Math.ceil(xmin); x<=Math.floor(xmax); x+=xStep){
      var gx = toC(x,0,xmin,xmax,ymin,ymax)[0];
      ctx.beginPath(); ctx.moveTo(gx,PAD.top); ctx.lineTo(gx,H-PAD.bottom); ctx.stroke();
    }

    // Axes
    ctx.strokeStyle="#475569"; ctx.lineWidth=1.5;
    var ax0=toC(xmin,0,xmin,xmax,ymin,ymax), ax1=toC(xmax,0,xmin,xmax,ymin,ymax);
    var ay0=toC(0,ymin,xmin,xmax,ymin,ymax), ay1=toC(0,ymax,xmin,xmax,ymin,ymax);
    ctx.beginPath(); ctx.moveTo(ax0[0],ax0[1]); ctx.lineTo(ax1[0]+8,ax1[1]); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(ay0[0],ay0[1]); ctx.lineTo(ay1[0],ay1[1]-8); ctx.stroke();
    // arrowheads
    ctx.fillStyle="#475569";
    ctx.beginPath(); ctx.moveTo(ax1[0]+8,ax1[1]-4); ctx.lineTo(ax1[0]+15,ax1[1]); ctx.lineTo(ax1[0]+8,ax1[1]+4); ctx.fill();
    ctx.beginPath(); ctx.moveTo(ay1[0]-4,ay1[1]-8); ctx.lineTo(ay1[0],ay1[1]-15); ctx.lineTo(ay1[0]+4,ay1[1]-8); ctx.fill();

    // Tick labels
    ctx.font="11px Georgia,serif"; ctx.fillStyle="#64748b";
    for(var xi=Math.ceil(xmin); xi<=Math.floor(xmax); xi+=xStep){
      if(xi===0) continue;
      var tp=toC(xi,0,xmin,xmax,ymin,ymax);
      ctx.textAlign="center"; ctx.fillText(xi===Math.PI?"π":xi===-Math.PI?"-π":(xi===2*Math.PI?"2π":xi===-2*Math.PI?"-2π":xi), tp[0], tp[1]+14);
    }
    for(var yi=Math.ceil(ymin); yi<=Math.floor(ymax); yi+=yStep){
      if(yi===0) continue;
      var tp2=toC(0,yi,xmin,xmax,ymin,ymax);
      ctx.textAlign="right"; ctx.fillText(yi, tp2[0]-6, tp2[1]+4);
    }
    ctx.textAlign="center"; ctx.fillStyle="#64748b";
    ctx.fillText("x", ax1[0]+18, ax1[1]+4);
    ctx.textAlign="left"; ctx.fillText("y", ay1[0]+5, ay1[1]-16);

    // True function (green)
    ctx.strokeStyle="#4ade80"; ctx.lineWidth=2.5;
    ctx.shadowColor="rgba(74,222,128,.4)"; ctx.shadowBlur=5;
    ctx.beginPath();
    var started=false;
    for(var i=0;i<=steps;i++){
      var xv=xmin+i/steps*(xmax-xmin);
      var yv=f(xv);
      if(!isFinite(yv)||yv<ymin-5||yv>ymax+5){ started=false; continue; }
      var p=toC(xv,yv,xmin,xmax,ymin,ymax);
      started?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]); started=true;
    }
    ctx.stroke(); ctx.shadowBlur=0;

    // Taylor approximation (orange)
    ctx.strokeStyle="#fb923c"; ctx.lineWidth=2;
    ctx.shadowColor="rgba(251,146,60,.4)"; ctx.shadowBlur=4;
    ctx.beginPath();
    var tstarted=false;
    for(var i=0;i<=steps;i++){
      var xv=xmin+i/steps*(xmax-xmin);
      var tv=taylorVal(curFn,curOrder,curA,xv);
      if(!isFinite(tv)||tv<ymin-8||tv>ymax+8){ tstarted=false; continue; }
      var p=toC(xv,tv,xmin,xmax,ymin,ymax);
      tstarted?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]); tstarted=true;
    }
    ctx.stroke(); ctx.shadowBlur=0;

    // Expansion point dot
    var aVal = curA;
    var faVal = f(aVal);
    if(isFinite(faVal)){
      var ap=toC(aVal,faVal,xmin,xmax,ymin,ymax);
      ctx.fillStyle="#fb923c";
      ctx.shadowColor="rgba(251,146,60,.8)"; ctx.shadowBlur=10;
      ctx.beginPath(); ctx.arc(ap[0],ap[1],6,0,Math.PI*2); ctx.fill();
      ctx.shadowBlur=0;
      // label
      ctx.fillStyle="#fb923c"; ctx.font="12px Georgia,serif"; ctx.textAlign="left";
      ctx.fillText("a="+aVal.toFixed(1), ap[0]+9, ap[1]-6);
    }

    // f(x) label
    var labelX=xmin+(xmax-xmin)*0.72;
    var labelY=f(labelX);
    if(isFinite(labelY)){
      var lp=toC(labelX,labelY,xmin,xmax,ymin,ymax);
      ctx.fillStyle="#4ade80"; ctx.font="italic 13px Georgia,serif"; ctx.textAlign="left";
      ctx.fillText(cfg.label, lp[0]+6, lp[1]-8);
    }

    // Stats
    var err=maxError();
    var errCol=err<0.01?"#4ade80":err<0.5?"#fbbf24":"#f87171";
    var order_names=["0th","1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th","21st","22nd","23rd","24th","25th","26th","27th","28th","29th","30th"];
    document.getElementById("taylor-stats").innerHTML=[
      ["Function", cfg.label, "#4ade80"],
      ["Order", order_names[curOrder], "#fb923c"],
      ["Max error", err<1e-6?"≈ 0":err.toFixed(4), errCol]
    ].map(function(d){
      return '<div style="flex:1;background:rgba(10,15,30,.7);border:1px solid rgba(148,163,184,.1);border-radius:10px;padding:10px;text-align:center;">'
        +'<div style="font-size:10px;color:#64748b;letter-spacing:.1em;text-transform:uppercase;margin-bottom:3px;">'+d[0]+'</div>'
        +'<div style="font-size:16px;color:'+d[2]+';font-family:monospace;">'+d[1]+'</div></div>';
    }).join("");

    updateFormula();
  }

  // ── Helper: sync center slider bounds + value to current function ────
  function updateCenterSlider(fn, newA) {
    var cfg = FNS[fn];
    var sl = document.getElementById("taylor-cslider");
    sl.min   = cfg.cmin;
    sl.max   = cfg.cmax;
    // clamp newA to valid range, then set
    var aReal = Math.max(cfg.cmin/100, Math.min(cfg.cmax/100, (newA !== undefined ? newA : 0)));
    sl.value = Math.round(aReal * 100);
    curA = aReal;
    document.getElementById("taylor-centerlabel").textContent = "a = " + curA.toFixed(2);
  }

  // ── Function buttons ──────────────────────────────────────────────────
  var btnC = document.getElementById("taylor-fnbtns");
  FN_KEYS.forEach(function(k){
    var btn=document.createElement("button");
    btn.id="taylor-fnbtn-"+k;
    btn.textContent=k;
    function styleAll(){
      FN_KEYS.forEach(function(kk){
        var b=document.getElementById("taylor-fnbtn-"+kk);
        if(!b) return;
        if(kk===curFn){
          b.style.cssText="padding:6px 14px;border-radius:8px;border:2px solid #34d399;background:rgba(52,211,153,.2);color:#34d399;font-size:13px;font-family:Georgia,serif;cursor:pointer;font-weight:bold;";
        } else {
          b.style.cssText="padding:6px 14px;border-radius:8px;border:2px solid rgba(148,163,184,.2);background:rgba(10,15,30,.5);color:#94a3b8;font-size:13px;font-family:Georgia,serif;cursor:pointer;";
        }
      });
    }
    btn.addEventListener("click",function(){
      curFn=k;
      updateCenterSlider(k, 0);   // reset a=0 and fix slider range for new function
      styleAll(); draw();
    });
    btnC.appendChild(btn);
    // initial style
    btn.style.cssText=k===curFn
      ?"padding:6px 14px;border-radius:8px;border:2px solid #34d399;background:rgba(52,211,153,.2);color:#34d399;font-size:13px;font-family:Georgia,serif;cursor:pointer;font-weight:bold;"
      :"padding:6px 14px;border-radius:8px;border:2px solid rgba(148,163,184,.2);background:rgba(10,15,30,.5);color:#94a3b8;font-size:13px;font-family:Georgia,serif;cursor:pointer;";
  });

  // ── Sliders ───────────────────────────────────────────────────────────
  document.getElementById("taylor-slider").addEventListener("input",function(){
    curOrder=+this.value;
    var names=["0th","1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th"];
    document.getElementById("taylor-orderlabel").textContent="order = "+curOrder+" ("+names[curOrder]+")";
    draw();
  });
  document.getElementById("taylor-cslider").addEventListener("input",function(){
    curA=+this.value/100;
    document.getElementById("taylor-centerlabel").textContent="a = "+curA.toFixed(2);
    draw();
  });

  // ── Init: set correct slider range for the default function ──────────
  updateCenterSlider(curFn, 0);

  window.addEventListener("resize",resize);
  resize();
})();
</script>


<h4>Examples</h4>

- [**exponential function**](https://en.wikipedia.org/wiki/Taylor_series#Exponential_function){:target="_blank"}

\begin{equation}
	e^x
	=
	\sum_{n=0}^\infty \frac{x^n}{n!} = 1 + x + \frac{x^2}{2} + \frac{x^3}{3!} + \cdots
\end{equation}

- [**natural logarithm**](https://en.wikipedia.org/wiki/Taylor_series#Natural_logarithm){:target="_blank"}

\begin{equation}
	\ln(1+x)
	=
	\sum_{n=0}^\infty (-1)^{n+1} \frac{x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots
\end{equation}

hence

\begin{equation}
	\ln(1-x)
	=
	- \sum_{n=0}^\infty (-1)^{n} \frac{x^n}{n} = - x - \frac{x^2}{2} - \frac{x^3}{3} - \cdots
\end{equation}

- [**geometric series**](https://en.wikipedia.org/wiki/Taylor_series#Geometric_series){:target="_blank"}

\begin{equation}
	\frac{1}{1-x}
	=
	\sum_{n=0}^\infty x^n = 1 + x + x^2 + \cdots
\end{equation}

\begin{equation}
	\frac{1}{(1-x)^2}
	=
	\sum_{n=1}^\infty nx^{n-1} = 1 + 2x + 3x^2 + \cdots
\end{equation}

- [**trigonometric functions**](https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions){:target="_blank"}

$$
\begin{eqnarray}
	\sin(x)
	&=&
		\sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!} x^{2n+1}
	=
		x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots
\\
	\cos(x)
	&=&
		\sum_{n=0}^\infty \frac{(-1)^n}{(2n)!} x^{2n}
	=
		1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots
\end{eqnarray}
$$

More examples can be shown in [Taylor series Wikipedia Page](https://en.wikipedia.org/wiki/Taylor_series#List_of_Maclaurin_series_of_some_common_functions){:target="_blank"}!

### Derivatives of trigonometric functions

$$
\begin{eqnarray}
\label{eq:der-tri}
\begin{array}{rcl}
	\dfrac{d}{dx} \sin(x) &=& \cos(x)
\\
	\dfrac{d}{dx} \cos(x) &=& - \sin(x)
\\
	\dfrac{d}{dx} \tan(x) &=& \sec^2(x)
		= \dfrac{1}{\cos^2(x)}
\\
\dfrac{d}{dx} \dfrac{1}{\tan(x)} =
	\dfrac{d}{dx} \cot(x) &=& - \csc^2(x)
		= - \dfrac{1}{\sin^2(x)}
\\
\dfrac{d}{dx} \dfrac{1}{\cos(x)} =
	\dfrac{d}{dx} \sec(x) &=& \sec(x) \tan(x)
		= \dfrac{\sin(x)}{\cos^2(x)}
\\
\dfrac{d}{dx} \dfrac{1}{\sin(x)} =
	\dfrac{d}{dx} \csc(x) &=& - \csc(x) \cot(x)
		= - \dfrac{\cos(x)}{\sin^2(x)}
\end{array}
\end{eqnarray}
$$

### Derivatives of inverse trigonometric functions

$$
\begin{eqnarray}
\label{eq:der-inverse-tri}
\begin{array}{rcl}
\dfrac{d}{dx} \sin^{-1}(x) &=& \dfrac{1}{\sqrt{1-x^2}}
\\
\dfrac{d}{dx} \cos^{-1}(x) &=& - \dfrac{1}{\sqrt{1-x^2}}
\\
\dfrac{d}{dx} \tan^{-1}(x) &=& \dfrac{1}{1+x^2}
\end{array}
\end{eqnarray}
$$

More formula can be found [here](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Derivatives_of_inverse_trigonometric_functions){:target="_blank"}!

## Integration / Integral

### Riemann integral

The [<span class="define">Riemann integral</span>](https://en.wikipedia.org/wiki/Riemann_integral){:target="_blank"},
created by [Bernhard Riemann](https://en.wikipedia.org/wiki/Bernhard_Riemann){:target="_blank"},
was the first rigorous definition of the integral of a function on an interval.
It was presented to the faculty at the [University of Göttingen](https://en.wikipedia.org/wiki/University_of_G%C3%B6ttingen){:target="_blank"} in 1854,
but not published in a journal until 1868.

For many functions and practical applications,
the Riemann integral can be evaluated by
the [{{ page.sections.fundamental-theorem-of-calculus }}](#fundamental-theorem-of-calculus)
or approximated by [numerical integration](https://en.wikipedia.org/wiki/Numerical_integration){:target="_blank"},
or simulated using [Monte Carlo integration](https://en.wikipedia.org/wiki/Monte_Carlo_integration){:target="_blank"}.

<h4>The big idea - slicing areas into rectangles</h4>

Imagine you want to find the area under a curve $f(x)$ between $x = a$ and $x = b$.
The key idea is simple

> slice the interval $[a, b]$ into $n$ thin vertical strips, approximate each strip as a rectangle, and add up all the rectangle areas!

As you use more and more slices (i.e., as $n \to \infty$), the approximation gets better and better — and in the limit, it becomes exact.
That limit is precisely the <span class="define">definite integral</span>!

$$
\int_a^b f(x)\, dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i) \cdot \Delta x
$$

where $\Delta x = \dfrac{b-a}{n}$ is the width of each slice,
and $x_i$ is any chosen point inside the $i$-th slice.
The sum $\displaystyle\sum_{i=1}^{n} f(x_i) \cdot \Delta x$ is called a
[<span class="define">Riemann sum</span>](https://en.wikipedia.org/wiki/Riemann_integral#Riemann_sum){:target="_blank"}.

### Four practical approximation methods (AP exam favorites!)

Depending on *where* you pick $x_i$ inside each slice, you get different approximation methods.
The AP Calculus BC exam tests all four of these.

| Method | Where $x_i$ is chosen | Character |
|---|---|---|
| **Left Riemann sum** | Left endpoint of each slice | Underestimates if $f$ is increasing; overestimates if decreasing |
| **Right Riemann sum** | Right endpoint of each slice | Overestimates if $f$ is increasing; underestimates if decreasing |
| **Midpoint rule** | Midpoint of each slice | Generally more accurate than left or right |
| **Trapezoidal rule** | Uses trapezoids instead of rectangles | Exact for linear $f$; see formula below |

The <span class="emph">trapezoidal rule</span> replaces each rectangle with a trapezoid
whose two parallel sides are $f(x_{i-1})$ and $f(x_i)$.
This gives:

\begin{equation}
\label{eq:trapezoidal-rule}
	\frac{\Delta x}{2} \left( f(x_0) + 2f(x_1) + 2f(x_2) + \cdots + 2f(x_{n-1}) + f(x_n) \right)
\end{equation}

Note that the first and last terms have coefficient $1$, while all interior terms have coefficient $2$.
Refer to [LibreTexts - Numerical Integration - Midpoint, Trapezoid, Simpson's rule](https://math.libretexts.org/Courses/Mount_Royal_University/Calculus_for_Scientists_II/2%3A_Techniques_of_Integration/2.5%3A_Numerical_Integration_-_Midpoint%2C_Trapezoid%2C_Simpson's_rule){:target="_blank"}
for more details.

<h4>Over- or underestimate? It depends on concavity!</h4>

A key AP exam question type asks - *"Is this approximation an overestimate or underestimate?"*
The answer depends on the **concavity** of $f$ on the interval:

- If $f$ is <span class="emph">concave up</span> ($f'' > 0$): the trapezoidal rule **overestimates**, and the midpoint rule **underestimates**.
- If $f$ is <span class="emph">concave down</span> ($f'' < 0$): the trapezoidal rule **underestimates**, and the midpoint rule **overestimates**.

For left/right Riemann sums, the over/underestimate depends on whether $f$ is increasing or decreasing (as shown in the table above).

#### Interactive visualization - integral approximation {#iv-integral-approximation}

Try it yourself, Beth! Drag the slider to increase $n$ and watch how the rectangles converge to the exact area.
Toggle between methods to see Left, Right, Midpoint, and Trapezoidal approximations.

<div id="riemann-viz" style="background:linear-gradient(135deg,#0f172a,#1e1b4b,#0f172a);border-radius:16px;padding:24px;margin:24px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:16px;">
    <div style="font-size:11px;letter-spacing:.3em;color:#818cf8;text-transform:uppercase;margin-bottom:6px;">Riemann Integration</div>
    <div style="font-size:22px;color:#f1f5f9;font-weight:normal;">Area Under a Curve</div>
    <div style="font-size:12px;color:#94a3b8;font-style:italic;margin-top:4px;">Slice into rectangles → sum up → take the limit as n → ∞</div>
  </div>
  <canvas id="riemann-canvas" style="width:100%;display:block;border-radius:8px;background:#0f172a;"></canvas>
  <div id="riemann-formula" style="background:rgba(30,27,75,.6);border-radius:10px;padding:12px;margin:14px 0;text-align:center;font-size:14px;color:#f1f5f9;">
    S<sub>n</sub> = Σ f(x*<sub>i</sub>) · Δx &nbsp;→&nbsp; ∫<sub>a</sub><sup>b</sup> f(x) dx
  </div>
  <div style="display:flex;gap:8px;margin-bottom:14px;justify-content:center;flex-wrap:wrap;" id="riemann-btns"></div>
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
    <span id="riemann-nlabel" style="color:#94a3b8;font-size:13px;min-width:72px;font-style:italic;">n = 6 slices</span>
    <input id="riemann-slider" type="range" min="1" max="50" value="6" style="flex:1;accent-color:#818cf8;" />
    <span style="color:#64748b;font-size:11px;min-width:80px;text-align:right;">n → ∞ for exact</span>
  </div>
  <div style="display:flex;gap:10px;" id="riemann-stats"></div>
  <div style="text-align:center;margin-top:12px;font-size:11px;color:#475569;">Drag the slider — more slices → smaller error → exact integral</div>
</div>

<script>
(function(){
  var A=0.5, B=5.5;
  function f(x){ return 0.6*Math.sin(x-0.5)*x+1.8; }
  var METHODS=["left","right","midpoint","trapezoid"];
  var LABELS={left:"Left",right:"Right",midpoint:"Midpoint",trapezoid:"Trapezoid"};
  var COLORS={
    left:  {fill:"rgba(96,165,250,.35)", stroke:"#3b82f6"},
    right: {fill:"rgba(52,211,153,.35)", stroke:"#10b981"},
    midpoint:{fill:"rgba(251,191,36,.35)",stroke:"#f59e0b"},
    trapezoid:{fill:"rgba(232,121,249,.35)",stroke:"#d946ef"}
  };
  var PAD={top:28,right:28,bottom:44,left:48};
  var yMin=0, yMax=5.5;
  var curMethod="left", curN=6;

  // True integral via Simpson
  function trueVal(){
    var n=1000,dx=(B-A)/n,s=f(A)+f(B);
    for(var i=1;i<n;i++) s+=(i%2===0?2:4)*f(A+i*dx);
    return dx/3*s;
  }
  var TRUE=trueVal();

  function rSum(method,n){
    var dx=(B-A)/n,s=0;
    for(var i=0;i<n;i++){
      var x0=A+i*dx,x1=x0+dx;
      if(method==="left") s+=f(x0)*dx;
      else if(method==="right") s+=f(x1)*dx;
      else if(method==="midpoint") s+=f((x0+x1)/2)*dx;
      else s+=(f(x0)+f(x1))/2*dx;
    }
    return s;
  }

  var canvas=document.getElementById("riemann-canvas");
  var W,H;
  function resize(){
    var cont=document.getElementById("riemann-viz");
    W=cont.clientWidth-48; H=Math.round(W*0.52);
    canvas.width=W; canvas.height=H;
    draw();
  }

  function toC(x,y){
    var cx=PAD.left+(x-A)/(B-A)*(W-PAD.left-PAD.right);
    var cy=H-PAD.bottom-(y-yMin)/(yMax-yMin)*(H-PAD.top-PAD.bottom);
    return [cx,cy];
  }

  function draw(){
    var ctx=canvas.getContext("2d");
    ctx.clearRect(0,0,W,H);
    var n=curN, method=curMethod, col=COLORS[method];
    var dx=(B-A)/n;
    var baseY=toC(A,0)[1];

    // rectangles / trapezoids
    for(var i=0;i<n;i++){
      var x0=A+i*dx,x1=x0+dx;
      var cx0=toC(x0,0)[0],cx1=toC(x1,0)[0];
      ctx.fillStyle=col.fill; ctx.strokeStyle=col.stroke; ctx.lineWidth=1.5;
      if(method!=="trapezoid"){
        var xs=method==="left"?x0:method==="right"?x1:(x0+x1)/2;
        var cyT=toC(x0,f(xs))[1];
        ctx.beginPath(); ctx.rect(cx0,cyT,cx1-cx0,baseY-cyT); ctx.fill(); ctx.stroke();
        var cxs=toC(xs,0)[0], cys=toC(xs,f(xs))[1];
        ctx.fillStyle=col.stroke; ctx.beginPath(); ctx.arc(cxs,cys,3,0,Math.PI*2); ctx.fill();
        ctx.fillStyle=col.fill;
      } else {
        var cyL=toC(x0,f(x0))[1],cyR=toC(x1,f(x1))[1];
        ctx.beginPath(); ctx.moveTo(cx0,baseY); ctx.lineTo(cx0,cyL); ctx.lineTo(cx1,cyR); ctx.lineTo(cx1,baseY); ctx.closePath(); ctx.fill(); ctx.stroke();
      }
    }

    // grid
    ctx.strokeStyle="rgba(148,163,184,.15)"; ctx.lineWidth=1;
    for(var y=1;y<=5;y++){ var gy=toC(A,y)[1]; ctx.beginPath(); ctx.moveTo(PAD.left,gy); ctx.lineTo(W-PAD.right,gy); ctx.stroke(); }

    // axes
    ctx.strokeStyle="#94a3b8"; ctx.lineWidth=1.5;
    var cxA=toC(A,0)[0],cxB=toC(B,0)[0];
    ctx.beginPath(); ctx.moveTo(cxA,baseY); ctx.lineTo(cxB+10,baseY); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(cxA,baseY); ctx.lineTo(cxA,PAD.top-8); ctx.stroke();
    ctx.fillStyle="#94a3b8";
    ctx.beginPath(); ctx.moveTo(cxB+10,baseY-4); ctx.lineTo(cxB+17,baseY); ctx.lineTo(cxB+10,baseY+4); ctx.fill();
    ctx.beginPath(); ctx.moveTo(cxA-4,PAD.top-8); ctx.lineTo(cxA,PAD.top-15); ctx.lineTo(cxA+4,PAD.top-8); ctx.fill();
    ctx.font="12px Georgia,serif"; ctx.textAlign="center"; ctx.fillText("x",cxB+21,baseY+4);
    ctx.textAlign="left"; ctx.fillText("y",cxA+5,PAD.top-16);

    // ticks
    ctx.font="11px Georgia,serif"; ctx.fillStyle="#64748b";
    for(var xi=Math.ceil(A);xi<=Math.floor(B);xi++){
      var tc=toC(xi,0); ctx.strokeStyle="#94a3b8"; ctx.lineWidth=1;
      ctx.beginPath(); ctx.moveTo(tc[0],tc[1]); ctx.lineTo(tc[0],tc[1]+4); ctx.stroke();
      ctx.textAlign="center"; ctx.fillText(xi,tc[0],tc[1]+14);
    }
    ctx.textAlign="right";
    for(var yi=1;yi<=5;yi++){
      var tc2=toC(A,yi); ctx.strokeStyle="#94a3b8"; ctx.lineWidth=1;
      ctx.beginPath(); ctx.moveTo(tc2[0]-3,tc2[1]); ctx.lineTo(tc2[0],tc2[1]); ctx.stroke();
      ctx.fillText(yi,tc2[0]-6,tc2[1]+4);
    }

    // curve
    ctx.strokeStyle="#f8fafc"; ctx.lineWidth=2.5; ctx.shadowColor="rgba(248,250,252,.4)"; ctx.shadowBlur=5;
    ctx.beginPath();
    for(var si=0;si<=400;si++){
      var xv=A+(si/400)*(B-A), cv=toC(xv,f(xv));
      si===0?ctx.moveTo(cv[0],cv[1]):ctx.lineTo(cv[0],cv[1]);
    }
    ctx.stroke(); ctx.shadowBlur=0;

    // f(x) label
    var lp=toC(4.0,f(4.0)); ctx.fillStyle="#f8fafc"; ctx.font="italic 13px Georgia,serif"; ctx.textAlign="left"; ctx.fillText("y = f(x)",lp[0]+6,lp[1]-8);

    // update stats
    var approx=rSum(method,n);
    var err=(approx-TRUE)/TRUE*100;
    var errCol=Math.abs(err)<1?"#4ade80":Math.abs(err)<5?"#fbbf24":"#f87171";
    var stats=document.getElementById("riemann-stats");
    stats.innerHTML=[
      ["Approximation",approx.toFixed(5),COLORS[method].stroke],
      ["True Value",TRUE.toFixed(5),"#94a3b8"],
      ["Error",(err>0?"+":"")+err.toFixed(2)+"%",errCol]
    ].map(function(d){
      return '<div style="flex:1;background:rgba(15,23,42,.6);border:1px solid rgba(148,163,184,.1);border-radius:10px;padding:10px;text-align:center;">'
        +'<div style="font-size:10px;color:#64748b;letter-spacing:.1em;text-transform:uppercase;margin-bottom:3px;">'+d[0]+'</div>'
        +'<div style="font-size:16px;color:'+d[2]+';font-family:monospace;">'+d[1]+'</div></div>';
    }).join("");

    // update formula border color
    document.getElementById("riemann-formula").style.borderColor=COLORS[method].stroke+"55";
    document.getElementById("riemann-formula").style.boxShadow="0 0 16px "+COLORS[method].stroke+"22";
  }

  // Build buttons
  var btnContainer=document.getElementById("riemann-btns");
  METHODS.forEach(function(m){
    var btn=document.createElement("button");
    btn.id="riemann-btn-"+m;
    btn.textContent=LABELS[m];
    btn.style.cssText="padding:6px 14px;border-radius:8px;cursor:pointer;font-size:13px;font-family:Georgia,serif;transition:all .2s;";
    function styleBtn(){
      if(curMethod===m){
        btn.style.border="2px solid "+COLORS[m].stroke;
        btn.style.background=COLORS[m].fill;
        btn.style.color=COLORS[m].stroke;
        btn.style.fontWeight="bold";
      } else {
        btn.style.border="2px solid rgba(148,163,184,.2)";
        btn.style.background="rgba(15,23,42,.5)";
        btn.style.color="#94a3b8";
        btn.style.fontWeight="normal";
      }
    }
    btn.addEventListener("click",function(){
      curMethod=m;
      METHODS.forEach(function(mm){ document.getElementById("riemann-btn-"+mm) && (function(b2,m2){ if(curMethod===m2){b2.style.border="2px solid "+COLORS[m2].stroke;b2.style.background=COLORS[m2].fill;b2.style.color=COLORS[m2].stroke;b2.style.fontWeight="bold";}else{b2.style.border="2px solid rgba(148,163,184,.2)";b2.style.background="rgba(15,23,42,.5)";b2.style.color="#94a3b8";b2.style.fontWeight="normal";}})(document.getElementById("riemann-btn-"+mm),mm); });
      draw();
    });
    styleBtn();
    btnContainer.appendChild(btn);
  });

  // Slider
  var slider=document.getElementById("riemann-slider");
  slider.style.accentColor=COLORS[curMethod].stroke;
  slider.addEventListener("input",function(){
    curN=+this.value;
    document.getElementById("riemann-nlabel").textContent="n = "+curN+" slices";
    draw();
  });

  // Init
  window.addEventListener("resize",resize);
  resize();
})();
</script>

### Basic properties {#integration-properties}

<h4>Linearity</h4>

Just like differentiation, integration is a <span class="emph">linear</span> operation:

$$
\int \bigl(f(x) + g(x)\bigr)\, dx = \int f(x)\, dx + \int g(x)\, dx
$$

$$
\int c\, f(x)\, dx = c \int f(x)\, dx
$$

So in one line

\begin{equation}
\label{eq:int-linearity}
	\int \bigl(a f + b g\bigr)\, dx = a \int f\, dx + b \int g\, dx
\end{equation}

This lets you split up and scale integrals freely — use it constantly!

<h4>Some useful properties to know</h4>

For definite integrals, a few more properties are worth knowing!

\begin{equation}
	\int_a^b f(x)\,dx = -\int_b^a f(x)\,dx
\end{equation}

\begin{equation}
	\int_a^a f(x)\,dx = 0
\end{equation}

\begin{equation}
	\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx
\end{equation}

### Integration by parts {#integration-by-parts}

[<span class="emph">Integration by parts</span>](https://en.wikipedia.org/wiki/Integration_by_parts){:target="_blank"}
is the integration counterpart of the [product rule](#differentiation-product-rule).
Recall the product rule &ndash; $(fg)' = f'g + fg'$.
Integrating both sides and rearranging gives

\begin{equation}
\label{eq:int-by-parts}
	\int f'(x)\, g(x)\, dx = f(x)g(x) - \int f(x)\, g'(x)\, dx
\end{equation}

In the shorthand $u = g(x)$, $dv = f'(x)\,dx$ (so $v = f(x)$, $du = g'(x)\,dx$), this is the form you'll see most often:

\begin{equation}
\label{eq:int-by-parts-uv}
\int u\, dv = uv - \int v\, du
\end{equation}

<span class="emph">The art of integration by parts is choosing $u$ and $dv$ smartly.</span>
<!--
A useful mnemonic for priority of $u$: **LIATE** — Logarithm, Inverse trig, Algebraic, Trig, Exponential.
Pick $u$ from whichever category appears earliest in that list.
-->

For definite integrals, we have

<!--
\begin{equation}
	\int_a^b f'(x)\, g(x)\, dx = \Bigl.\Bigl(f(x)g(x)\Bigr)\Bigr|_{x=a}^b - \int_a^b f(x)\, g'(x)\, dx
\end{equation}
-->

\begin{equation}
\label{eq:int-by-parts-definite}
	\int_a^b f'(x)\, g(x)\, dx = \Bigl[f(x)g(x)\Bigr]_a^b - \int_a^b f(x)\, g'(x)\, dx
\end{equation}

<h4>Examples</h4>

<ol>
<li>
Find an indefinite integral $\displaystyle\int x e^x\,dx$

<p>
<strong>Solution 1</strong>
Choose $f(x) = e^x$ and $g(x) = x$. Then $f'(x) = e^x$ and $g'(x) = 1$, hence
\eqref{eq:int-by-parts} gives

\begin{equation}
\label{eq:int-by-parts-exam-01}
\int x e^x\, dx = x e^x - \int e^x\, dx = x e^x - e^x + C = (x-1)e^x + C
\end{equation}
</p>

<p>
<strong>Solution 2</strong>
Choose $u = x$ and $v = e^x$. Then $du = dx$ and $dv = e^x dx$, thus
\eqref{eq:int-by-parts-uv} gives

$$
\int x e^x\, dx = x e^x - \int e^x\, dx = x e^x - e^x + C = (x-1)e^x + C
$$
</p>
</li>

<li>
Find an indefinite integral $\displaystyle\int \ln x\,dx$

<p>
<strong>Solution 1</strong>
Choose $f(x) = x$ and $g(x) = \ln x$. Then $f'(x) = 1$ and $g'(x) = 1/x$, hence
\eqref{eq:int-by-parts} gives

$$
	\int \ln x \, dx
		=
			x \ln x - \int 1\, dx
		=
			x \ln x - x + C
$$
</p>

<p>
<strong>Solution 2</strong>
Choose $u = \ln x$ and $v = x$. Then $du = (1/x)dx$ and $dv = dx$, thus
\eqref{eq:int-by-parts-uv} gives

$$
	\int \ln x \, dx
		=
			x \ln x - \int 1\, dx
		=
			x \ln x - x + C
$$
</p>
</li>

<li>
Find an indefinite integral $\displaystyle\int x \sin x\,dx$

<p>
<strong>Solution 1</strong>
Choose $f(x) = -\cos x$ and $g(x) = x$. Then $f'(x) = \sin x$ and $g'(x) = 1$, hence
\eqref{eq:int-by-parts} gives

$$
	\int x \sin x \, dx
		=
			- x \cos x + \int \cos x\, dx
		=
			- x \cos x + \sin x + C
$$
</p>

<p>
<strong>Solution 2</strong>
Choose $u = x$ and $v = -\cos x$. Then $du = dx$ and $dv = \sin x dx$, thus
\eqref{eq:int-by-parts-uv} gives

$$
	\int x \sin x \, dx
		=
			- x \cos x + \int \cos x\, dx
		=
			- x \cos x + \sin x + C
$$
</p>
</li>

<li>
Find an indefinite integral $\displaystyle\int x^2 e^x \,dx$

<p>
<strong>Solution</strong>
Choose $f(x) = e^x$ and $g(x) = x^2$. Then $f'(x) = e^x$ and $g'(x) = 2x$, hence
\eqref{eq:int-by-parts} gives

$$
\begin{eqnarray*}
	\int x^2 e^x \, dx
		&=&
			x^2 e^x - 2 \int x e^x \, dx
		=
			x^2 e^x - 2 (x-1) e^x + C
\\
		&=&
			(x^2 -2x+2)e^x + C
\end{eqnarray*}
$$
where \eqref{eq:int-by-parts-exam-01} is used
</p>
</li>

<li>
Find an indefinite integral $\displaystyle\int e^x \sin x \,dx$

<p>
<strong>Solution</strong>
We let $\displaystyle I = \int e^x \sin x \,dx$.
Now choose $f(x) = e^x$ and $g(x) = \sin x$. Then $f'(x) = e^x$ and $g'(x) = \cos x$, hence
\eqref{eq:int-by-parts} gives

\begin{equation}
\label{eq:01}
	I = \int e^x \sin x \, dx
		=
			e^x \sin x - \int e^x \cos x \, dx
\end{equation}

Now to find $\displaystyle\int e^x \cos x \,dx$,
we let $f(x) = e^x$ and $g(x) = \cos x$. Then $f'(x) = e^x$ and $g'(x) = - \sin x$, hence

\begin{equation}
\label{eq:02}
	\int e^x \cos x \, dx
		=
			e^x \cos x + \int e^x \sin x \, dx = e^x \cos x + I
\end{equation}

Now if we combine \eqref{eq:01} and \eqref{eq:02},
we have

$$
	I = e^x \sin x - e^x \cos x - I
$$

thus,

$$
	\int e^x \sin x \, dx = I = \frac{1}{2} e^x (\sin x - \cos x) + C
$$

</p>
</li>

<li>
Find an indefinite integral $\displaystyle\int e^x \cos x \,dx$
</li>

<li>
Find an indefinite integral $\displaystyle\int x \ln x \,dx$
</li>
</ol>

### Integration by Substitution

\begin{equation}
\label{eq:int-by-sub}
	\int g'(x) f'(g(x)) dx = f(g(x)) + C
\end{equation}

- Method 1 - using directly the [chain rule](#chain-rule), *e.g.*, we just note that

\begin{equation}
\label{eq:prob-int-by-sub-01}
	\int x e^{-x^2} dx = - \frac{1}{2} e^{-x^2} + C
\end{equation}

- Method 2 - using <span class="emph">u-substitution</span> (also known as <span class="emph">integration by substitution</span> or <span class="emph">substitution rule</span>),
*i.e.*,
	by letting

$$
	u = g(x)
$$

then

$$
	du = g'(x) dx
$$

thus

$$
	\int g'(x) f'(g(x)) dx
	=
		\int f'(u) du
	=
		f(u) + C
	=
		f(g(x)) + C
$$

For example, to solve \eqref{eq:prob-int-by-sub-01}, we let $u=-x^2$, then we have $du = -2xdx$,
hence

$$
	\int x e^{-x^2} dx
	=
		-\frac{1}{2} \int e^{u} du
	=
		-\frac{1}{2} e^{u} + C
	=
		-\frac{1}{2} e^{-x^2} + C
$$

which (of course) coincides with \eqref{eq:prob-int-by-sub-01}!

### Integrals of inverse trigonometric functions

$$
\begin{eqnarray}
\label{eq:int-arcsin}
	\int \sin^{-1}(x) dx
		&=&
			x \sin^{-1}(x) + \sqrt{1-x^2} + C
\\
\label{eq:int-arccos}
	\int \cos^{-1}(x) dx
		&=&
			x \cos^{-1}(x) - \sqrt{1-x^2} + C
\\
\label{eq:int-arctan}
	\int \tan^{-1}(x) dx
		&=&
			x \tan^{-1}(x) - \frac{1}{2} \ln(x^2+1) + C
\\
\label{eq:int-arcsin-a}
	\int \sin^{-1}(ax) dx
		&=&
			x \sin^{-1}(ax) + \frac{\sqrt{1-a^2x^2}}{a} + C
\\
\nonumber
	\int \sin^{-1}(ax)^2 dx
		&=&
			-2x + x \sin^{-1}(ax)^2
\\
\label{eq:int-arcsin-squared}
		&&
			\quad
			+ \frac{2\sqrt{1-a^2x^2}\sin^{-1}(ax)}{a} + C
\\
\label{eq:int-arccos-a}
	\int \cos^{-1}(ax) dx
		&=&
			x \cos^{-1}(ax) - \frac{\sqrt{1-a^2x^2}}{a} + C
\\
\nonumber
	\int \cos^{-1}(ax)^2 dx
		&=&
			-2x + x \cos^{-1}(ax)^2
\\
\label{eq:int-arccos-squared}
		&&
			\quad
			- \frac{2\sqrt{1-a^2x^2}\cos^{-1}(ax)}{a} + C
\\
\label{eq:int-arctan-a}
	\int \tan^{-1}(ax) dx
		&=&
			x \tan^{-1}(ax) - \frac{\ln(a^2x^2+1)}{2a} + C
\end{eqnarray}
$$

You can easily verify these formulas, *e.g.*, using formulas in \eqref{eq:der-inverse-tri}.
More formula can be found [here](https://en.wikipedia.org/wiki/List_of_integrals_of_inverse_trigonometric_functions){:target="_blank"}!

## Fundamental theorem of calculus {#fundamental-theorem-of-calculus}

The [fundamental theorem of calculus (FTC)](https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus){:target="_blank"}
is
a theorem that links the concept of differentiating a function (calculating its slopes, or rate of change at every point on its domain)
with the concept of integrating a function (calculating the area under its graph, or the cumulative effect of small contributions).
Roughly speaking, the two operations can be thought of as inverses of each other.

The first part of the theorem,
[the first FTC](https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus#First_part){:target="_blank"},
states that for a continuous function $f$,
an [antiderivative](https://en.wikipedia.org/wiki/Antiderivative){:target="_blank"}
or indefinite integral $F$ can be obtained
as the integral of $f$ over an interval with a variable upper bound.

Let $f$ be a continuous real-valued function defined on a closed interval $[a, b]$.
Let $F$ be the function defined, for all $x$ in $[a, b]$, by

$$
F(x) = \int_a^x f(t) \, dt
$$

Then $F$ is uniformly continuous on $[a, b]$ and differentiable on the open interval $(a, b)$, and

$$
F'(x) = f(x)
$$

for all $x$ in $(a,b)$ so $F$ is an [antiderivative](https://en.wikipedia.org/wiki/Antiderivative){:target="_blank"} of $f$.
We can combine these two equations to write

\begin{equation}
\label{eq:fund-theorem-of-calculus-1}
\frac{d}{dx} \int_a^x f(t) \, dt = f(x)
\end{equation}

<!--
The fundamental theorem is often employed to compute the definite integral of a function $f$
for which an antiderivative $F$ is known.
Specifically, if $f$ is a real-valued continuous function on $[a, b]$ and $F$ is an antiderivative of $f$
in $[a, b]$, then

$$
\int_a^b f(t) \, dt = F(b) - F(a)
$$
-->

Conversely, [the second part of FTC](https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus#Second_part){:target="_blank"}
(sometimes referred to as **Newton–Leibniz theorem**),
states that the integral of a function $f$ over a fixed interval is equal to the change of any [antiderivative](https://en.wikipedia.org/wiki/Antiderivative){:target="_blank"} $F$
between the ends of the interval.
<!--
This greatly simplifies the calculation of a definite integral provided an antiderivative can be found by symbolic integration, thus avoiding numerical integration.
-->

Let $f$ be a real-valued function on a closed interval $[a,b]$ and $F$ a continuous function on $[a,b]$
which is an antiderivative of $f$ in $(a,b)$,
*i.e.*,

$$
F'(x) = f(x)
$$

Then if $f$ is [Riemann integrable](https://en.wikipedia.org/wiki/Riemann_integrable){:target="_blank"}
on $[a,b]$ then

\begin{equation}
\label{eq:fund-theorem-of-calculus-2}
\int_a^b f(x) \, dx = F(b) - F(a)
\end{equation}

**Examples** using \eqref{eq:fund-theorem-of-calculus-1}

<ol>
<li> &nbsp;
<p>
$$
\frac{d}{dx} \int_2^x \sqrt{1+t^2} \, dt
	=
		\sqrt{1+x^2}
$$
</p>
</li>
<li> &nbsp;
<p>
$$
\lim_{h\to 0} \frac{\int_1^{1+h} \sqrt{x^5+8} \, dx}{h}
	=
		\sqrt{1^5+8} = 3
$$
</p>
</li>
<li> &nbsp;
<p>
$$
\frac{d}{dx} \int_a^{g(x)} f(t) \, dt
	=
		f(g(x)) g'(x)
$$
</p>
</li>
<li> &nbsp;
<p>
$$
\frac{d}{dx} \int_{h(x)}^{g(x)} f(t) \, dt
	=
		f(g(x)) g'(x) - f(h(x)) h'(x)
$$
</p>
</li>
<li> &nbsp;
<p>
$$
\frac{d}{dx} \int_2^{x^2} \sqrt{1+t^2} \, dt
	=
		2x \sqrt{1+x^4}
$$
</p>
</li>
</ol>

## Distance / Velocity / Acceleration / Length

### One-dimensional case

In physics classes,
we've learned movement of objects
on a line,
*i.e.*,
in one-dimensional line.

Suppose
the location (or displacement) $d(t)\in\reals$,
the velocity $v(t)\in\reals$,
and
the acceleration $a(t)\in\reals$
of an (rigid) object (or point mass).
Then we have

$$
\begin{eqnarray}
\begin{array}{rcl}
v(t)
	&=&
		d'(t)
\\
	&=&
		\dfrac{d}{dt} d(t)
\end{array}
\end{eqnarray}
$$

$$
\begin{eqnarray}
\begin{array}{rcl}
a(t)
	&=&
		v'(t) = d^{\prime\prime}(t)
\\
	&=&
		\dfrac{d}{dt} v(t) = \dfrac{d^2}{dt^2} d(t)
\end{array}
\end{eqnarray}
$$

Therefore

\begin{equation}
\label{eq:vel-int-dis-1}
	d(t) = \int_{t_0}^t v(\tau) d\tau + d(t_0)
\end{equation}

and

\begin{equation}
	v(t) = \int_{t_0}^t a(\tau) d\tau + v(t_0)
\end{equation}

### Two-dimensional case

We can very naturally extend what we did in 1-dimensional line
to a 2-dimensional plane
with the concept of a vector
and its representation using a Cartesian coordinate system.

Let $\vec{d}(t) = (x(t), y(t))\in\reals^2$ be the location of an object in a 2-dimensional space.
Then the velocity $\vec{v}(t) = (v_x(t), v_y(t))\in\reals^2$ is

\begin{equation}
(v_x(t), v_y(t))
	=
		\dfrac{d}{dt} \vec{d}(t)
	=
		\left(
			\dfrac{d}{dt} x(t),
			\dfrac{d}{dt} y(t)
		\right)
	=
		(x'(t), y'(t))
\end{equation}

hence

\begin{equation}
	v_x(t) = x'(t),\quad
	v_y(t) = y'(t)
\end{equation}

and the acceleration $\vec{a}(t) = (a_x(t), a_y(t)) \in\reals^2$ is

\begin{equation}
(a_x(t), a_y(t))
	=
		\frac{d}{dt} \vec{v}(t)
	=
		\left(
			\frac{d}{dt} v_x(t),
			\frac{d}{dt} v_y(t)
		\right)
	=
		(v_x'(t), v_y'(t))
\end{equation}

hence

\begin{equation}
	a_x(t) = v_x'(t) = x^{\prime\prime}(t),\quad
	a_y(t) = v_y'(t) = y^{\prime\prime}(t)
\end{equation}

Therefore

\begin{equation}
	\vec{d}(t) = \int_{t_0}^t \vec{v}(\tau) d\tau + \vec{d}(t_0)
\end{equation}

or equivalently

\begin{equation}
	(x(t),y(t)) = \int_{t_0}^t (x(\tau), y(\tau)) d\tau + (x(t_0), y(t_0))
\end{equation}

hence

\begin{equation}
	x(t) = \int_{t_0}^t v_x(\tau) d\tau + x(t_0),\;
	y(t) = \int_{t_0}^t v_y(\tau) d\tau + y(t_0)
\end{equation}

Also

\begin{equation}
	\vec{v}(t) = \int_{t_0}^t \vec{a}(\tau) d\tau + \vec{v}(t_0)
\end{equation}

or equivalently

\begin{equation}
	(v_x(t),v_y(t)) = \int_{t_0}^t (a_x(\tau), a_y(\tau)) d\tau + (v_x(t_0), v_y(t_0))
\end{equation}

hence

\begin{equation}
	v_x(t) = \int_{t_0}^t a_x(\tau) d\tau + v_x(t_0),\;
	v_y(t) = \int_{t_0}^t a_y(\tau) d\tau + v_y(t_0)
\end{equation}

This can be also extended to the 3-dimensional case in a similar way.

### Parameterized curve

The length of a curve parameterized by $(x(t),y(t))$ from $t=t_1$ to $t=t_2$ is

\begin{equation}
\label{eq:vel-int-len}
	\mathrm{length}
	=
	\int_{t_1}^{t_2} \left|\vec{v}(t)\right| dt
\end{equation}

because this can be thought of an object moving along a 1-dimensional curve,
hence \eqref{eq:vel-int-dis-1} applies.

#### Interactive visualization - arc length {#iv-arc-length}

Watch how approximating the curve by $n$ straight chords converges to the true arc length $\int_{t_1}^{t_2} \lvert\vec{v}(t)\rvert\,dt$.
The lower panel shows $\lvert\vec{v}(t)\rvert = \sqrt{x'(t)^2 + y'(t)^2}$ — its integral is exactly the arc length!

<div id="arc-viz" style="background:linear-gradient(135deg,#0f172a,#1a0f2e,#0f172a);border-radius:16px;padding:24px;margin:24px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:16px;">
    <div style="font-size:11px;letter-spacing:.3em;color:#e879f9;text-transform:uppercase;margin-bottom:6px;">Arc Length</div>
    <div style="font-size:22px;color:#f1f5f9;font-weight:normal;">∫ |<span style="font-style:italic;">v</span>(t)| dt — Summing Infinitesimal Steps</div>
    <div style="font-size:12px;color:#94a3b8;font-style:italic;margin-top:4px;">Each chord approximates a tiny piece of the curve — more chords → exact length</div>
  </div>
  <div style="display:flex;gap:8px;margin-bottom:12px;justify-content:center;flex-wrap:wrap;" id="arc-fnbtns"></div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
    <div>
      <div style="font-size:11px;color:#94a3b8;text-align:center;margin-bottom:6px;letter-spacing:.05em;">PARAMETRIC CURVE (x(t), y(t))</div>
      <canvas id="arc-canvas-curve" style="width:100%;display:block;border-radius:8px;background:#080a14;"></canvas>
    </div>
    <div>
      <div style="font-size:11px;color:#94a3b8;text-align:center;margin-bottom:6px;letter-spacing:.05em;">SPEED |v(t)| — INTEGRATE FOR LENGTH</div>
      <canvas id="arc-canvas-speed" style="width:100%;display:block;border-radius:8px;background:#080a14;"></canvas>
    </div>
  </div>

  <!-- Stats -->
  <div style="display:flex;gap:10px;margin:14px 0;" id="arc-stats"></div>

  <!-- n slider -->
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
    <span style="color:#94a3b8;font-size:13px;min-width:80px;font-style:italic;" id="arc-nlabel">n = 4 chords</span>
    <input id="arc-slider" type="range" min="1" max="60" value="4" style="flex:1;accent-color:#e879f9;" />
    <span style="color:#64748b;font-size:11px;min-width:80px;text-align:right;">n → ∞ for exact</span>
  </div>
  <div style="text-align:center;font-size:11px;color:#475569;">
    Purple chords = chord approximation &nbsp;|&nbsp; White curve = true path &nbsp;|&nbsp; Shaded area = ∫|v(t)|dt ≈ arc length
  </div>
</div>

<script>
(function(){
  var ARC_CURVES = {
    "Circle": {
      x:  function(t){ return Math.cos(t); },
      y:  function(t){ return Math.sin(t); },
      dx: function(t){ return -Math.sin(t); },
      dy: function(t){ return  Math.cos(t); },
      t1: 0, t2: 2*Math.PI,
      xmin:-1.4,xmax:1.4,ymin:-1.4,ymax:1.4,
      trueLen: 2*Math.PI
    },
    "Spiral": {
      x:  function(t){ return t*Math.cos(t)/4; },
      y:  function(t){ return t*Math.sin(t)/4; },
      dx: function(t){ return (Math.cos(t)-t*Math.sin(t))/4; },
      dy: function(t){ return (Math.sin(t)+t*Math.cos(t))/4; },
      t1: 0, t2: 4*Math.PI,
      xmin:-3.5,xmax:3.5,ymin:-3.5,ymax:3.5,
      trueLen: null  // computed numerically
    },
    "Lemniscate": {
      // x=cos(t), y=sin(t)cos(t)  — figure-8 like
      x:  function(t){ return Math.cos(t); },
      y:  function(t){ return Math.sin(t)*Math.cos(t); },
      dx: function(t){ return -Math.sin(t); },
      dy: function(t){ return Math.cos(2*t); },
      t1: 0, t2: 2*Math.PI,
      xmin:-1.4,xmax:1.4,ymin:-0.8,ymax:0.8,
      trueLen: null
    },
    "Cycloid": {
      x:  function(t){ return t - Math.sin(t); },
      y:  function(t){ return 1 - Math.cos(t); },
      dx: function(t){ return 1 - Math.cos(t); },
      dy: function(t){ return Math.sin(t); },
      t1: 0, t2: 2*Math.PI,
      xmin:-0.5,xmax:7,ymin:-0.3,ymax:2.5,
      trueLen: 8  // exact: 8r = 8 for r=1
    }
  };
  var ARC_KEYS = Object.keys(ARC_CURVES);
  var curArc = "Cycloid";
  var curN = 4;
  var APADc={top:16,right:16,bottom:32,left:40};
  var APADs={top:16,right:16,bottom:32,left:40};
  var ACW,ACH;

  function speed(cfg,t){ return Math.sqrt(cfg.dx(t)*cfg.dx(t)+cfg.dy(t)*cfg.dy(t)); }

  // numerical arc length via Simpson
  function trueArcLen(cfg){
    if(cfg.trueLen!==null) return cfg.trueLen;
    var n=1000, dt=(cfg.t2-cfg.t1)/n, s=speed(cfg,cfg.t1)+speed(cfg,cfg.t2);
    for(var i=1;i<n;i++) s+=(i%2===0?2:4)*speed(cfg,cfg.t1+i*dt);
    return dt/3*s;
  }

  function chordLen(cfg,n){
    var dt=(cfg.t2-cfg.t1)/n, s=0;
    for(var i=0;i<n;i++){
      var t0=cfg.t1+i*dt, t1=cfg.t1+(i+1)*dt;
      var dx=cfg.x(t1)-cfg.x(t0), dy=cfg.y(t1)-cfg.y(t0);
      s+=Math.sqrt(dx*dx+dy*dy);
    }
    return s;
  }

  function actoC(x,y,xmin,xmax,ymin,ymax,w,h,pad){
    return [pad.left+(x-xmin)/(xmax-xmin)*(w-pad.left-pad.right),
            h-pad.bottom-(y-ymin)/(ymax-ymin)*(h-pad.top-pad.bottom)];
  }

  function arcResize(){
    var cc=document.getElementById("arc-canvas-curve");
    var cs=document.getElementById("arc-canvas-speed");
    var cont=document.getElementById("arc-viz");
    var half=(cont.clientWidth-48-12)/2;
    ACW=Math.round(half); ACH=Math.round(half*0.85);
    cc.width=ACW; cc.height=ACH;
    cs.width=ACW; cs.height=ACH;
    arcDraw();
  }

  function arcDraw(){
    var cfg=ARC_CURVES[curArc];
    var n=curN;
    var t1=cfg.t1, t2=cfg.t2;

    // ── Curve canvas ──────────────────────────────────────────────
    var cc=document.getElementById("arc-canvas-curve");
    var ctx=cc.getContext("2d");
    ctx.clearRect(0,0,ACW,ACH);
    var xmin=cfg.xmin,xmax=cfg.xmax,ymin=cfg.ymin,ymax=cfg.ymax;
    function cp(x,y){ return actoC(x,y,xmin,xmax,ymin,ymax,ACW,ACH,APADc); }

    // Grid
    ctx.strokeStyle="rgba(232,121,249,.07)"; ctx.lineWidth=1;
    for(var yi=Math.ceil(ymin);yi<=Math.floor(ymax);yi++){
      var gy=cp(0,yi)[1]; ctx.beginPath(); ctx.moveTo(APADc.left,gy); ctx.lineTo(ACW-APADc.right,gy); ctx.stroke();
    }

    // Axes
    ctx.strokeStyle="#2d1b3d"; ctx.lineWidth=1.5;
    var axy=cp(0,0)[1], axx=cp(0,0)[0];
    ctx.beginPath(); ctx.moveTo(APADc.left,axy); ctx.lineTo(ACW-APADc.right,axy); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(axx,ACH-APADc.bottom); ctx.lineTo(axx,APADc.top); ctx.stroke();
    ctx.font="10px Georgia,serif"; ctx.fillStyle="#4a2d5a"; ctx.textAlign="center";
    ctx.fillText("x",ACW-APADc.right+10,axy+4);
    ctx.textAlign="left"; ctx.fillText("y",axx+4,APADc.top+10);

    // Chords (purple)
    var dt=(t2-t1)/n;
    ctx.strokeStyle="rgba(232,121,249,.7)"; ctx.lineWidth=1.5;
    ctx.beginPath();
    for(var i=0;i<=n;i++){
      var t=t1+i*dt, p=cp(cfg.x(t),cfg.y(t));
      i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]);
    }
    ctx.stroke();

    // Chord endpoint dots
    ctx.fillStyle="#e879f9";
    for(var i=0;i<=n;i++){
      var t=t1+i*dt, p=cp(cfg.x(t),cfg.y(t));
      ctx.beginPath(); ctx.arc(p[0],p[1],3,0,Math.PI*2); ctx.fill();
    }

    // True curve (white)
    ctx.strokeStyle="#f1f5f9"; ctx.lineWidth=2;
    ctx.shadowColor="rgba(241,245,249,.3)"; ctx.shadowBlur=4;
    ctx.beginPath(); var started=false;
    for(var i=0;i<=400;i++){
      var t=t1+i/400*(t2-t1), p=cp(cfg.x(t),cfg.y(t));
      started?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]); started=true;
    }
    ctx.stroke(); ctx.shadowBlur=0;

    // Start dot (green) & end dot (orange)
    var ps=cp(cfg.x(t1),cfg.y(t1)), pe=cp(cfg.x(t2),cfg.y(t2));
    ctx.fillStyle="#4ade80"; ctx.beginPath(); ctx.arc(ps[0],ps[1],5,0,Math.PI*2); ctx.fill();
    ctx.fillStyle="#fb923c"; ctx.beginPath(); ctx.arc(pe[0],pe[1],5,0,Math.PI*2); ctx.fill();
    ctx.fillStyle="#94a3b8"; ctx.font="11px Georgia,serif"; ctx.textAlign="left";
    ctx.fillText("start",ps[0]+6,ps[1]-4);
    ctx.fillText("end",pe[0]+6,pe[1]-4);

    // ── Speed canvas ──────────────────────────────────────────────
    var cs=document.getElementById("arc-canvas-speed");
    var ctx2=cs.getContext("2d");
    ctx2.clearRect(0,0,ACW,ACH);

    // compute speed range
    var speeds=[]; for(var i=0;i<=200;i++) speeds.push(speed(cfg,t1+i/200*(t2-t1)));
    var smax=Math.max.apply(null,speeds)*1.15;
    function sp(t,s){ return actoC(t,s,t1,t2,0,smax,ACW,ACH,APADs); }

    // Shaded area under |v(t)| for chord segments (Riemann-style)
    for(var i=0;i<n;i++){
      var ta=t1+i*dt, tb=t1+(i+1)*dt;
      var smid=speed(cfg,(ta+tb)/2);
      var p0=sp(ta,0), p1=sp(ta,smid), p2=sp(tb,smid), p3=sp(tb,0);
      ctx2.fillStyle="rgba(232,121,249,.2)";
      ctx2.strokeStyle="rgba(232,121,249,.5)"; ctx2.lineWidth=1;
      ctx2.beginPath(); ctx2.moveTo(p0[0],p0[1]); ctx2.lineTo(p1[0],p1[1]);
      ctx2.lineTo(p2[0],p2[1]); ctx2.lineTo(p3[0],p3[1]); ctx2.closePath();
      ctx2.fill(); ctx2.stroke();
    }

    // True speed curve shaded
    ctx2.fillStyle="rgba(241,245,249,.06)";
    ctx2.beginPath();
    var basePt=sp(t1,0);
    ctx2.moveTo(basePt[0],basePt[1]);
    for(var i=0;i<=300;i++){
      var t=t1+i/300*(t2-t1), p=sp(t,speed(cfg,t));
      ctx2.lineTo(p[0],p[1]);
    }
    ctx2.lineTo(sp(t2,0)[0],sp(t2,0)[1]); ctx2.closePath(); ctx2.fill();

    // True speed curve (white)
    ctx2.strokeStyle="#f1f5f9"; ctx2.lineWidth=2;
    ctx2.beginPath(); var s2started=false;
    for(var i=0;i<=300;i++){
      var t=t1+i/300*(t2-t1), p=sp(t,speed(cfg,t));
      s2started?ctx2.lineTo(p[0],p[1]):ctx2.moveTo(p[0],p[1]); s2started=true;
    }
    ctx2.stroke();

    // Axes for speed plot
    ctx2.strokeStyle="#2d1b3d"; ctx2.lineWidth=1.5;
    var sax=sp(t1,0); ctx2.beginPath(); ctx2.moveTo(sax[0],sax[1]); ctx2.lineTo(sp(t2,0)[0],sp(t2,0)[1]); ctx2.stroke();
    ctx2.font="10px Georgia,serif"; ctx2.fillStyle="#4a2d5a";
    ctx2.textAlign="center";
    ctx2.fillText("t",sp(t2,0)[0]+10,sp(t2,0)[1]);
    ctx2.textAlign="left"; ctx2.fillStyle="#94a3b8";
    ctx2.fillText("|v(t)|",APADs.left+2,APADs.top+12);

    // t tick labels
    ctx2.fillStyle="#4a2d5a"; ctx2.font="10px Georgia,serif"; ctx2.textAlign="center";
    for(var i=0;i<=4;i++){
      var t=t1+i/4*(t2-t1), p=sp(t,0);
      ctx2.fillText((t/(Math.PI)).toFixed(1)+"π",p[0],p[1]+13);
    }

    // Stats
    var cl=chordLen(cfg,n), tl=trueArcLen(cfg);
    var err=Math.abs(cl-tl)/tl*100;
    var errCol=err<0.1?"#4ade80":err<2?"#fbbf24":"#f87171";
    document.getElementById("arc-stats").innerHTML=[
      ["Chord sum",cl.toFixed(5),"#e879f9"],
      ["True length",tl.toFixed(5),"#f1f5f9"],
      ["Error",err.toFixed(3)+"%",errCol]
    ].map(function(d){
      return '<div style="flex:1;background:rgba(10,5,20,.7);border:1px solid rgba(148,163,184,.1);border-radius:10px;padding:10px;text-align:center;">'
        +'<div style="font-size:10px;color:#64748b;letter-spacing:.1em;text-transform:uppercase;margin-bottom:3px;">'+d[0]+'</div>'
        +'<div style="font-size:15px;color:'+d[2]+';font-family:monospace;">'+d[1]+'</div></div>';
    }).join("");
  }

  // Buttons
  var abtnC=document.getElementById("arc-fnbtns");
  ARC_KEYS.forEach(function(k){
    var btn=document.createElement("button");
    btn.id="arc-fnbtn-"+k; btn.textContent=k;
    function styleAll(){
      ARC_KEYS.forEach(function(kk){
        var b=document.getElementById("arc-fnbtn-"+kk); if(!b) return;
        b.style.cssText=kk===curArc
          ?"padding:6px 14px;border-radius:8px;border:2px solid #e879f9;background:rgba(232,121,249,.15);color:#e879f9;font-size:13px;font-family:Georgia,serif;cursor:pointer;font-weight:bold;"
          :"padding:6px 14px;border-radius:8px;border:2px solid rgba(148,163,184,.2);background:rgba(10,5,20,.5);color:#94a3b8;font-size:13px;font-family:Georgia,serif;cursor:pointer;";
      });
    }
    btn.addEventListener("click",function(){ curArc=k; styleAll(); arcDraw(); });
    btn.style.cssText=k===curArc
      ?"padding:6px 14px;border-radius:8px;border:2px solid #e879f9;background:rgba(232,121,249,.15);color:#e879f9;font-size:13px;font-family:Georgia,serif;cursor:pointer;font-weight:bold;"
      :"padding:6px 14px;border-radius:8px;border:2px solid rgba(148,163,184,.2);background:rgba(10,5,20,.5);color:#94a3b8;font-size:13px;font-family:Georgia,serif;cursor:pointer;";
    abtnC.appendChild(btn);
  });

  document.getElementById("arc-slider").addEventListener("input",function(){
    curN=+this.value;
    document.getElementById("arc-nlabel").textContent="n = "+curN+" chord"+(curN>1?"s":"");
    arcDraw();
  });

  window.addEventListener("resize",arcResize);
  arcResize();
})();
</script>

## Area and Volume

### Area

The area can be calculated by the integration of the **length** $l(x)$ of a cross section perpendicular to the $x$-axis,
*i.e.*,

\begin{equation}
A = \int_a^b l(x) dx
\end{equation}

<h4>The area between two curves</h4>

\begin{equation}
A = \int_a^b \left|f(x) - g(x)\right| dx
\end{equation}

<h4>The area in polar coordinates</h4>

\begin{equation}
A = \frac{1}{2} \int_\alpha^\beta r(\theta)^2 d\theta
\end{equation}

<h4>The area between two polar curves</h4>

\begin{equation}
A = \frac{1}{2} \int_\alpha^\beta (r_\mathrm{outer}(\theta)^2 - r_\mathrm{inner}(\theta)^2) d\theta
\end{equation}

### Volume

The volume can be calculated by the integration of the **area** $A(x)$ of a cross section perpendicular to the $x$-axis,
*i.e.*,

\begin{equation}
V = \int_a^b A(x) dx
\end{equation}

<h4>Disc method for volume calculation</h4>

\begin{equation}
\label{eq:vol-disc-method}
	V = \pi \int_a^b R(x)^2 dx
\end{equation}

where $R(x)$ is the distance between the axis of revolution and the outside of the object

#### Interactive visualization — disc method {#iv-disc-method}


<div id="disc-viz" style="background:linear-gradient(135deg,#020814,#0a1628,#020814);border-radius:16px;padding:24px;margin:24px 0;font-family:Georgia,serif;">

  <div style="text-align:center;margin-bottom:16px;">
    <div style="font-size:11px;letter-spacing:.3em;color:#60a5fa;text-transform:uppercase;margin-bottom:4px;">Volume of Revolution</div>
    <div style="font-size:22px;color:#f1f5f9;font-weight:normal;">Disc Method — Interactive Visualization</div>
    <div style="font-size:13px;color:#94a3b8;font-style:italic;margin-top:4px;">
      V = &pi; &int;<sub>a</sub><sup>b</sup> R(x)<sup>2</sup> dx &nbsp;=&nbsp; sum of solid circular discs
    </div>
  </div>

  <div id="disc-fn-btns" style="display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-bottom:14px;"></div>

  <div style="display:flex;gap:10px;margin-bottom:12px;">
    <div style="flex:1;background:rgba(2,8,20,.8);border-radius:12px;border:1px solid rgba(148,163,184,.1);overflow:hidden;">
      <canvas id="disc-canvas-2d" width="420" height="270" style="width:100%;display:block;"></canvas>
    </div>
    <div style="flex:1;background:rgba(2,8,20,.8);border-radius:12px;border:1px solid rgba(96,165,250,.2);overflow:hidden;position:relative;">
      <canvas id="disc-canvas-3d" width="420" height="270" style="width:100%;display:block;cursor:grab;"></canvas>
      <div style="position:absolute;bottom:7px;right:9px;font-size:10px;color:rgba(96,165,250,.55);font-style:italic;background:rgba(0,0,0,.45);padding:2px 7px;border-radius:4px;pointer-events:none;">&#x1F5B1; drag to rotate</div>
    </div>
  </div>

  <div id="disc-formula" style="background:rgba(96,165,250,.08);border:1px solid rgba(96,165,250,.4);border-radius:10px;padding:11px 18px;margin-bottom:12px;text-align:center;font-size:14px;color:#f1f5f9;"></div>

  <div style="display:flex;flex-direction:column;gap:9px;margin-bottom:12px;">
    <div style="display:flex;align-items:center;gap:12px;">
      <span id="disc-n-label" style="color:#94a3b8;font-size:13px;min-width:100px;font-style:italic;">n = 6 discs</span>
      <input id="disc-n-slider" type="range" min="2" max="24" value="6" style="flex:1;accent-color:#60a5fa;">
      <span style="color:#64748b;font-size:11px;min-width:80px;text-align:right;">more &rarr; exact</span>
    </div>
    <div style="display:flex;align-items:center;gap:12px;">
      <span id="disc-hl-label" style="color:#94a3b8;font-size:13px;min-width:100px;font-style:italic;">disc #3</span>
      <input id="disc-hl-slider" type="range" min="0" max="5" value="2" style="flex:1;accent-color:#f472b6;">
      <span style="color:#64748b;font-size:11px;min-width:80px;text-align:right;">highlight</span>
    </div>
  </div>

  <div style="display:flex;gap:10px;margin-bottom:10px;">
    <div style="flex:1;background:rgba(2,8,20,.7);border:1px solid rgba(148,163,184,.1);border-radius:10px;padding:10px;text-align:center;">
      <div style="font-size:10px;color:#64748b;letter-spacing:.1em;text-transform:uppercase;margin-bottom:3px;">True Volume</div>
      <div id="disc-stat-true" style="font-size:15px;color:#4ade80;font-family:monospace;">&#x2014;</div>
    </div>
    <div style="flex:1;background:rgba(2,8,20,.7);border:1px solid rgba(148,163,184,.1);border-radius:10px;padding:10px;text-align:center;">
      <div style="font-size:10px;color:#64748b;letter-spacing:.1em;text-transform:uppercase;margin-bottom:3px;">Disc Sum</div>
      <div id="disc-stat-sum" style="font-size:15px;color:#60a5fa;font-family:monospace;">&#x2014;</div>
    </div>
    <div style="flex:1;background:rgba(2,8,20,.7);border:1px solid rgba(148,163,184,.1);border-radius:10px;padding:10px;text-align:center;">
      <div style="font-size:10px;color:#64748b;letter-spacing:.1em;text-transform:uppercase;margin-bottom:3px;">Error</div>
      <div id="disc-stat-err" style="font-size:15px;font-family:monospace;">&#x2014;</div>
    </div>
  </div>

  <div style="text-align:center;font-size:11px;color:#475569;">
    <span style="color:#60a5fa;">n slider</span>: more discs &rarr; converges &nbsp;|&nbsp;
    <span style="color:#f472b6;">highlight slider</span>: inspect each &Delta;V &nbsp;|&nbsp;
    <span style="color:rgba(96,165,250,.6);">drag 3D panel</span>: spin &amp; tilt freely &nbsp;|&nbsp;
    <span style="color:#4ade80;">&#10003;</span>: f(x)&sup2; is linear &mdash; disc sum is <em>always</em> exact (interesting edge case!)
  </div>
</div>

<script>
(function(){
  var DFUNS = {
    "x/2":           { f:function(x){return x/2;},                  label:"x/2",            xmax:3.0, ymax:1.6 },
    "x\u00b2":       { f:function(x){return x*x;},                  label:"x\u00b2",        xmax:2.0, ymax:4.2 },
    "1+x/4":         { f:function(x){return 1+x/4;},                label:"1+x/4",          xmax:3.0, ymax:2.0 },
    "\u221ax":       { f:function(x){return Math.sqrt(x);},         label:"\u221ax",        xmax:3.0, ymax:2.0, exact:true },
    "sin(\u03c0x/2)":{ f:function(x){return Math.sin(Math.PI*x/2);},label:"sin(\u03c0x/2)", xmax:2.0, ymax:1.2, exact:true }
  };
  var DFK = Object.keys(DFUNS);
  var dst = { fnKey:DFK[0], n:6, hl:2, az:Math.PI/3, el:Math.PI/7 };

  // project (xpos along axis, r=radius, theta=angle around axis)
  function dproj(xpos, r, theta, az, el) {
    var X=xpos, Y=r*Math.cos(theta), Z=r*Math.sin(theta);
    var X1=X*Math.cos(az)-Y*Math.sin(az);
    var Y1=X*Math.sin(az)+Y*Math.cos(az);
    var Y2=Y1*Math.cos(el)-Z*Math.sin(el);
    var Z2=Y1*Math.sin(el)+Z*Math.cos(el);
    return [X1,-Z2,Y2];
  }

  var dc2=document.getElementById("disc-canvas-2d");
  var dc3=document.getElementById("disc-canvas-3d");

  function drawDisc2D(){
    var ctx=dc2.getContext("2d");
    var W=dc2.width,H=dc2.height;
    var PAD={l:48,r:16,t:20,b:40};
    var fn=DFUNS[dst.fnKey],nv=dst.n,hl=dst.hl;
    var xmax=fn.xmax,ymax=fn.ymax,dx=xmax/nv;
    function toC(x,y){return[PAD.l+x/xmax*(W-PAD.l-PAD.r),H-PAD.b-y/ymax*(H-PAD.t-PAD.b)];}
    ctx.clearRect(0,0,W,H); ctx.fillStyle="#020814"; ctx.fillRect(0,0,W,H);
    // grid
    ctx.strokeStyle="rgba(148,163,184,.1)"; ctx.lineWidth=1;
    for(var g=0;g<=Math.ceil(ymax);g++){var gc=toC(0,g);ctx.beginPath();ctx.moveTo(PAD.l,gc[1]);ctx.lineTo(W-PAD.r,gc[1]);ctx.stroke();}
    // disc slices
    for(var i=0;i<nv;i++){
      var xm=(i+.5)*dx,R=fn.f(xm);
      var c0=toC(i*dx,0),c1=toC((i+1)*dx,R);
      var isHi=(i===hl);
      ctx.fillStyle=isHi?"rgba(244,114,182,.45)":i%2===0?"rgba(96,165,250,.18)":"rgba(96,165,250,.12)";
      ctx.strokeStyle=isHi?"#f472b6":"rgba(96,165,250,.55)";
      ctx.lineWidth=isHi?2:1;
      ctx.fillRect(c0[0],c1[1],c1[0]-c0[0],c0[1]-c1[1]);
      ctx.strokeRect(c0[0],c1[1],c1[0]-c0[0],c0[1]-c1[1]);
      if(isHi){
        var cR=toC((i+.5)*dx,R/2);
        ctx.fillStyle="#f472b6"; ctx.font="bold 11px Georgia,serif"; ctx.textAlign="center";
        ctx.fillText("R=f(x)",cR[0],cR[1]);
        // double-headed radius arrow
        var cb=toC((i+1)*dx-.5,0),ct=toC((i+1)*dx-.5,R);
        ctx.strokeStyle="#f472b6"; ctx.lineWidth=1.5; ctx.setLineDash([3,3]);
        ctx.beginPath();ctx.moveTo(cb[0],cb[1]);ctx.lineTo(ct[0],ct[1]);ctx.stroke();
        ctx.setLineDash([]);
      }
    }
    // curve
    ctx.strokeStyle="#60a5fa"; ctx.lineWidth=2.5;
    ctx.shadowColor="rgba(96,165,250,.5)"; ctx.shadowBlur=6;
    ctx.beginPath();
    for(var k=0;k<=400;k++){var xk=k/400*xmax,ck=toC(xk,fn.f(xk));k===0?ctx.moveTo(ck[0],ck[1]):ctx.lineTo(ck[0],ck[1]);}
    ctx.stroke(); ctx.shadowBlur=0;
    // axes
    var a0=toC(0,0),a1x=toC(xmax,0),a1y=toC(0,ymax);
    ctx.strokeStyle="#475569"; ctx.lineWidth=1.5;
    ctx.beginPath();ctx.moveTo(a0[0],a0[1]);ctx.lineTo(a1x[0]+10,a0[1]);ctx.stroke();
    ctx.beginPath();ctx.moveTo(a0[0],a0[1]);ctx.lineTo(a0[0],a1y[1]-8);ctx.stroke();
    ctx.fillStyle="#475569";
    ctx.beginPath();ctx.moveTo(a1x[0]+10,a0[1]-4);ctx.lineTo(a1x[0]+17,a0[1]);ctx.lineTo(a1x[0]+10,a0[1]+4);ctx.fill();
    ctx.beginPath();ctx.moveTo(a0[0]-4,a1y[1]-8);ctx.lineTo(a0[0],a1y[1]-15);ctx.lineTo(a0[0]+4,a1y[1]-8);ctx.fill();
    ctx.font="11px Georgia,serif"; ctx.fillStyle="#64748b"; ctx.textAlign="center";
    for(var xi=0.5;xi<=xmax+.01;xi+=0.5){var tc=toC(xi,0);ctx.fillText(xi.toFixed(1),tc[0],tc[1]+14);}
    ctx.textAlign="right";
    for(var yi=1;yi<=Math.floor(ymax);yi++){var tc2=toC(0,yi);ctx.fillText(yi,tc2[0]-6,tc2[1]+4);}
    ctx.fillStyle="#60a5fa"; ctx.font="italic 13px Georgia,serif"; ctx.textAlign="left";
    var lp=toC(xmax*.55,fn.f(xmax*.55));ctx.fillText("y = "+fn.label,lp[0]+6,lp[1]-8);
    ctx.fillStyle="#475569"; ctx.font="13px Georgia,serif";
    ctx.textAlign="center"; ctx.fillText("x",a1x[0]+21,a0[1]+4);
    ctx.textAlign="left";   ctx.fillText("R(x)",a0[0]+6,a1y[1]-16);
    ctx.fillStyle="#94a3b8"; ctx.font="12px Georgia,serif"; ctx.textAlign="center";
    ctx.fillText("2D Cross-Section (side view)",W/2,14);
  }

  function drawDisc3D(){
    var ctx=dc3.getContext("2d");
    var W=dc3.width,H=dc3.height;
    var az=dst.az,el=dst.el;
    var fn=DFUNS[dst.fnKey],nv=dst.n,hl=dst.hl,dx=fn.xmax/nv;
    ctx.clearRect(0,0,W,H); ctx.fillStyle="#020814"; ctx.fillRect(0,0,W,H);
    var ocx=W*.45,ocy=H*.55,scale=Math.min(W,H)*.21;
    var SEGS=52;

    function p3(xp,r,th){var s=dproj(xp,r,th,az,el);return[ocx+s[0]*scale,ocy+s[1]*scale];}
    function dep(xp,r,th){return dproj(xp,r,th,az,el)[2];}

    // draw a filled disc face (circle) at xpos with radius R
    function drawFace(xp,R,fill,stroke,lw){
      ctx.beginPath();
      for(var s=0;s<=SEGS;s++){var th=s/SEGS*2*Math.PI,pt=p3(xp,R,th);s===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      // fill to center
      ctx.closePath();
      ctx.fillStyle=fill; ctx.strokeStyle=stroke; ctx.lineWidth=lw;
      ctx.fill(); ctx.stroke();
    }

    // draw cylindrical outer wall (full rotation) between x0..x1 at radius R
    function drawOuterWall(x0,x1,R,tStart,tEnd,fill,stroke,lw){
      var steps=Math.max(4,Math.round(SEGS*Math.abs(tEnd-tStart)/(2*Math.PI)));
      ctx.beginPath();
      for(var s=0;s<=steps;s++){var th=tStart+s/steps*(tEnd-tStart),pt=p3(x0,R,th);s===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var s=steps;s>=0;s--){var th=tStart+s/steps*(tEnd-tStart),pt=p3(x1,R,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath();
      ctx.fillStyle=fill; ctx.strokeStyle=stroke; ctx.lineWidth=lw;
      ctx.fill(); ctx.stroke();
    }

    // sort discs: farthest x first if x-axis goes "into" scene, else closest
    var order=[];
    for(var i=0;i<nv;i++) order.push(i);
    order.sort(function(a,b){
      return dep((a+.5)*dx,0,0)-dep((b+.5)*dx,0,0);
    });

    for(var oi=0;oi<order.length;oi++){
      var i=order[oi];
      var x0=i*dx,x1=(i+1)*dx,xm=(x0+x1)/2;
      var R=fn.f(xm),isHi=(i===hl);
      var wFill  =isHi?"rgba(244,114,182,0.20)":"rgba(96,165,250,0.10)";
      var wStroke=isHi?"#f472b6":"rgba(96,165,250,0.50)";
      var fFill  =isHi?"rgba(244,114,182,0.45)":"rgba(96,165,250,0.25)";
      var lw     =isHi?1.6:0.7;
      var backS=az+Math.PI/2,backE=az+3*Math.PI/2;
      var frontS=az-Math.PI/2,frontE=az+Math.PI/2;

      // back face at x0
      var bfDepx0=dep(x0,0,0), bfDepx1=dep(x1,0,0);
      // draw back face first (whichever face is farther)
      if(bfDepx0<bfDepx1){
        drawFace(x0,R,fFill,wStroke,lw*.8);
        drawOuterWall(x0,x1,R,backS,backE,wFill,wStroke,lw);
        drawOuterWall(x0,x1,R,frontS,frontE,wFill,wStroke,lw);
        drawFace(x1,R,fFill,wStroke,lw);
      } else {
        drawFace(x1,R,fFill,wStroke,lw*.8);
        drawOuterWall(x0,x1,R,backS,backE,wFill,wStroke,lw);
        drawOuterWall(x0,x1,R,frontS,frontE,wFill,wStroke,lw);
        drawFace(x0,R,fFill,wStroke,lw);
      }
    }

    // x-axis (revolution axis)
    var ax0=p3(-0.1,0,0),ax1=p3(fn.xmax*1.12,0,0);
    ctx.strokeStyle="rgba(148,163,184,.45)"; ctx.lineWidth=1.3; ctx.setLineDash([5,4]);
    ctx.beginPath();ctx.moveTo(ax0[0],ax0[1]);ctx.lineTo(ax1[0],ax1[1]);ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle="#94a3b8"; ctx.font="11px Georgia,serif"; ctx.textAlign="left";
    ctx.fillText("x (axis)",ax1[0]+4,ax1[1]+4);

    // surface curve on top (theta=π/2 slice)
    ctx.strokeStyle="#60a5fa"; ctx.lineWidth=2;
    ctx.shadowColor="rgba(96,165,250,.5)"; ctx.shadowBlur=4;
    ctx.beginPath();
    for(var k=0;k<=120;k++){
      var xk=k/120*fn.xmax,pt=p3(xk,fn.f(xk),Math.PI/2);
      k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);
    }
    ctx.stroke(); ctx.shadowBlur=0;

    // annotations on highlighted disc
    var xmh=(hl+.5)*dx,Rh=fn.f(xmh),x0h=hl*dx,x1h=(hl+1)*dx;
    // radius arrow (vertical on front face)
    var pc=p3(xmh,0,Math.PI/2),pr=p3(xmh,Rh,Math.PI/2);
    ctx.strokeStyle="#f472b6"; ctx.lineWidth=1.8;
    ctx.beginPath();ctx.moveTo(pc[0],pc[1]);ctx.lineTo(pr[0],pr[1]);ctx.stroke();
    var angR=Math.atan2(pr[1]-pc[1],pr[0]-pc[0]);
    ctx.fillStyle="#f472b6";
    ctx.beginPath();ctx.moveTo(pr[0],pr[1]);
    ctx.lineTo(pr[0]-7*Math.cos(angR-.4),pr[1]-7*Math.sin(angR-.4));
    ctx.lineTo(pr[0]-7*Math.cos(angR+.4),pr[1]-7*Math.sin(angR+.4));
    ctx.fill();
    ctx.font="bold 12px Georgia,serif"; ctx.textAlign="right";
    ctx.fillText("R=f(x)",pr[0]-8,(pc[1]+pr[1])/2);
    // thickness arrow on outer edge
    var pe0=p3(x0h,Rh*1.08,Math.PI*.6),pe1=p3(x1h,Rh*1.08,Math.PI*.6);
    ctx.strokeStyle="#a78bfa"; ctx.lineWidth=1.5;
    ctx.beginPath();ctx.moveTo(pe0[0],pe0[1]);ctx.lineTo(pe1[0],pe1[1]);ctx.stroke();
    ctx.fillStyle="#a78bfa"; ctx.font="bold 11px Georgia,serif"; ctx.textAlign="center";
    ctx.fillText("\u0394x",(pe0[0]+pe1[0])/2,(pe0[1]+pe1[1])/2-8);

    ctx.fillStyle="#94a3b8"; ctx.font="12px Georgia,serif"; ctx.textAlign="center";
    ctx.fillText("3D Disc View  \u2014  drag to rotate",W/2,14);
  }

  function discStats(){
    var fn=DFUNS[dst.fnKey],nv=dst.n,hl=dst.hl,dx=fn.xmax/nv;
    var xm=(hl+.5)*dx,R=fn.f(xm),dv=Math.PI*R*R*dx;
    var tv=0,di=fn.xmax/1000;
    for(var i=0;i<1000;i++){var xi=(i+.5)*di,ri=fn.f(xi);tv+=Math.PI*ri*ri*di;}
    var ss=0;
    for(var i=0;i<nv;i++){var xi=(i+.5)*dx,ri=fn.f(xi);ss+=Math.PI*ri*ri*dx;}
    var err=Math.abs(ss-tv)/tv*100;
    var ec=err<1?"#4ade80":err<5?"#fbbf24":"#f87171";
    document.getElementById("disc-formula").innerHTML=
      "<span style='color:#f472b6'>Disc #"+(hl+1)+"</span>"
      +"<span style='color:#94a3b8;margin:0 10px'>|</span>"
      +"\u0394V = \u03c0 &middot; <span style='color:#f472b6'>R</span><sup>2</sup>"
      +" &middot; <span style='color:#a78bfa'>\u0394x</span>"
      +" = \u03c0 &middot; <span style='color:#f472b6'>"+R.toFixed(3)+"</span><sup>2</sup>"
      +" &middot; <span style='color:#a78bfa'>"+dx.toFixed(3)+"</span>"
      +" = <span style='color:#fbbf24;font-weight:bold'>"+dv.toFixed(4)+"</span>";
    document.getElementById("disc-stat-true").textContent=tv.toFixed(5);
    document.getElementById("disc-stat-sum").textContent=ss.toFixed(5);
    var ee=document.getElementById("disc-stat-err");
    if(fn.exact){
      ee.textContent="\u2713 Exact!"; ee.style.color="#4ade80"; ee.title="f(x)\u00b2 is linear or symmetric \u2014 midpoint rule is perfectly exact for any n";
    } else {
      ee.textContent=err.toFixed(3)+"%"; ee.style.color=ec; ee.title="";
    }
  }

  function discRedraw(){drawDisc2D();drawDisc3D();discStats();}

  // buttons
  var dbc=document.getElementById("disc-fn-btns");
  DFK.forEach(function(k){
    var b=document.createElement("button");
    b.textContent="y = "+DFUNS[k].label+(DFUNS[k].exact?" ✓":""); b.dataset.key=k;
    b.style.cssText="padding:6px 16px;border-radius:8px;cursor:pointer;font-size:13px;font-family:Georgia,serif;";
    b.addEventListener("click",function(){dst.fnKey=k;dst.hl=Math.floor(dst.n/3);updDiscBtns();discRedraw();});
    dbc.appendChild(b);
  });
  function updDiscBtns(){dbc.querySelectorAll("button").forEach(function(b){var a=(b.dataset.key===dst.fnKey);b.style.border=a?"2px solid #60a5fa":"2px solid rgba(148,163,184,.2)";b.style.background=a?"rgba(96,165,250,.2)":"rgba(2,8,20,.5)";b.style.color=a?"#60a5fa":"#94a3b8";b.style.fontWeight=a?"bold":"normal";});}
  updDiscBtns();

  var dns=document.getElementById("disc-n-slider"),dhs=document.getElementById("disc-hl-slider");
  dns.addEventListener("input",function(){dst.n=parseInt(this.value);dst.hl=Math.min(dst.hl,dst.n-1);dhs.max=dst.n-1;dhs.value=dst.hl;document.getElementById("disc-n-label").textContent="n = "+dst.n+" discs";document.getElementById("disc-hl-label").textContent="disc #"+(dst.hl+1);discRedraw();});
  dhs.addEventListener("input",function(){dst.hl=parseInt(this.value);document.getElementById("disc-hl-label").textContent="disc #"+(dst.hl+1);discRedraw();});

  var ddrag={active:false,lastX:0,lastY:0};
  function dxy(e){return e.touches?{x:e.touches[0].clientX,y:e.touches[0].clientY}:{x:e.clientX,y:e.clientY};}
  dc3.addEventListener("mousedown",function(e){e.preventDefault();var p=dxy(e);ddrag={active:true,lastX:p.x,lastY:p.y};dc3.style.cursor="grabbing";});
  dc3.addEventListener("touchstart",function(e){e.preventDefault();var p=dxy(e);ddrag={active:true,lastX:p.x,lastY:p.y};},{passive:false});
  window.addEventListener("mousemove",function(e){if(!ddrag.active)return;var p=dxy(e);dst.az+=(p.x-ddrag.lastX)*.010;dst.el=Math.max(-Math.PI/2+.05,Math.min(Math.PI/2-.05,dst.el-(p.y-ddrag.lastY)*.010));ddrag.lastX=p.x;ddrag.lastY=p.y;drawDisc3D();});
  window.addEventListener("touchmove",function(e){if(!ddrag.active)return;e.preventDefault();var p=dxy(e);dst.az+=(p.x-ddrag.lastX)*.010;dst.el=Math.max(-Math.PI/2+.05,Math.min(Math.PI/2-.05,dst.el-(p.y-ddrag.lastY)*.010));ddrag.lastX=p.x;ddrag.lastY=p.y;drawDisc3D();},{passive:false});
  window.addEventListener("mouseup",function(){ddrag.active=false;dc3.style.cursor="grab";});
  window.addEventListener("touchend",function(){ddrag.active=false;});

  discRedraw();
})();
</script>


<h4>Washer method for volume calculation</h4>

\begin{equation}
	V = \pi \int_a^b \left( R(x)^2 - r(x)^2 \right)dx
\end{equation}

where $R(x)$ is the radius of the outside of the object and
$r(x)$ is the radius of the inside of the object

#### Interactive 3D visualization — washer method {#iv-washer-method}


<div id="washer-viz" style="background:linear-gradient(135deg,#0a0014,#1a000a,#0a0014);border-radius:16px;padding:24px;margin:24px 0;font-family:Georgia,serif;">

  <div style="text-align:center;margin-bottom:16px;">
    <div style="font-size:11px;letter-spacing:.3em;color:#f87171;text-transform:uppercase;margin-bottom:4px;">Volume of Revolution</div>
    <div style="font-size:22px;color:#f1f5f9;font-weight:normal;">Washer Method — Interactive Visualization</div>
    <div style="font-size:13px;color:#94a3b8;font-style:italic;margin-top:4px;">
      V = &pi; &int;<sub>a</sub><sup>b</sup> [R(x)<sup>2</sup> &minus; r(x)<sup>2</sup>] dx &nbsp;=&nbsp; sum of hollow washers
    </div>
  </div>

  <div id="washer-fn-btns" style="display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-bottom:14px;"></div>

  <div style="display:flex;gap:10px;margin-bottom:12px;">
    <div style="flex:1;background:rgba(10,0,20,.8);border-radius:12px;border:1px solid rgba(148,163,184,.1);overflow:hidden;">
      <canvas id="washer-canvas-2d" width="420" height="270" style="width:100%;display:block;"></canvas>
    </div>
    <div style="flex:1;background:rgba(10,0,20,.8);border-radius:12px;border:1px solid rgba(248,113,113,.2);overflow:hidden;position:relative;">
      <canvas id="washer-canvas-3d" width="420" height="270" style="width:100%;display:block;cursor:grab;"></canvas>
      <div style="position:absolute;bottom:7px;right:9px;font-size:10px;color:rgba(248,113,113,.55);font-style:italic;background:rgba(0,0,0,.45);padding:2px 7px;border-radius:4px;pointer-events:none;">&#x1F5B1; drag to rotate</div>
    </div>
  </div>

  <div id="washer-formula" style="background:rgba(248,113,113,.08);border:1px solid rgba(248,113,113,.4);border-radius:10px;padding:11px 18px;margin-bottom:12px;text-align:center;font-size:14px;color:#f1f5f9;"></div>

  <div style="display:flex;flex-direction:column;gap:9px;margin-bottom:12px;">
    <div style="display:flex;align-items:center;gap:12px;">
      <span id="washer-n-label" style="color:#94a3b8;font-size:13px;min-width:110px;font-style:italic;">n = 6 washers</span>
      <input id="washer-n-slider" type="range" min="2" max="24" value="6" style="flex:1;accent-color:#f87171;">
      <span style="color:#64748b;font-size:11px;min-width:80px;text-align:right;">more &rarr; exact</span>
    </div>
    <div style="display:flex;align-items:center;gap:12px;">
      <span id="washer-hl-label" style="color:#94a3b8;font-size:13px;min-width:110px;font-style:italic;">washer #3</span>
      <input id="washer-hl-slider" type="range" min="0" max="5" value="2" style="flex:1;accent-color:#fbbf24;">
      <span style="color:#64748b;font-size:11px;min-width:80px;text-align:right;">highlight</span>
    </div>
  </div>

  <div style="display:flex;gap:10px;margin-bottom:10px;">
    <div style="flex:1;background:rgba(10,0,20,.7);border:1px solid rgba(148,163,184,.1);border-radius:10px;padding:10px;text-align:center;">
      <div style="font-size:10px;color:#64748b;letter-spacing:.1em;text-transform:uppercase;margin-bottom:3px;">True Volume</div>
      <div id="washer-stat-true" style="font-size:15px;color:#4ade80;font-family:monospace;">&#x2014;</div>
    </div>
    <div style="flex:1;background:rgba(10,0,20,.7);border:1px solid rgba(148,163,184,.1);border-radius:10px;padding:10px;text-align:center;">
      <div style="font-size:10px;color:#64748b;letter-spacing:.1em;text-transform:uppercase;margin-bottom:3px;">Washer Sum</div>
      <div id="washer-stat-sum" style="font-size:15px;color:#f87171;font-family:monospace;">&#x2014;</div>
    </div>
    <div style="flex:1;background:rgba(10,0,20,.7);border:1px solid rgba(148,163,184,.1);border-radius:10px;padding:10px;text-align:center;">
      <div style="font-size:10px;color:#64748b;letter-spacing:.1em;text-transform:uppercase;margin-bottom:3px;">Error</div>
      <div id="washer-stat-err" style="font-size:15px;font-family:monospace;">&#x2014;</div>
    </div>
  </div>

  <div style="text-align:center;font-size:11px;color:#475569;">
    <span style="color:#f87171;">outer R(x)</span> &minus; <span style="color:#fbbf24;">inner r(x)</span>: region between two curves &nbsp;|&nbsp;
    <span style="color:rgba(248,113,113,.6);">drag 3D panel</span>: spin &amp; tilt
  </div>
</div>

<script>
(function(){
  var WFUNS = {
    "\u221ax vs x":     { R:function(x){return Math.sqrt(x);},   r:function(x){return x;},              Rl:"\u221ax",         rl:"x",        xmax:1.0, ymax:1.15 },
    "2 vs x\u00b2":     { R:function(x){return 2;},              r:function(x){return x*x;},             Rl:"2",               rl:"x\u00b2",  xmax:1.4, ymax:2.2  },
    "cos+1 vs 0.4":     { R:function(x){return Math.cos(Math.PI*x/4)+1;}, r:function(x){return 0.4;},   Rl:"cos(\u03c0x/4)+1",rl:"0.4",      xmax:2.0, ymax:2.2  },
    "x+0.5 vs 0.5x":   { R:function(x){return x+0.5;},          r:function(x){return 0.5*x;},           Rl:"x+0.5",           rl:"x/2",      xmax:1.5, ymax:2.1  }
  };
  var WFK=Object.keys(WFUNS);
  var wst={fnKey:WFK[0],n:6,hl:2,az:Math.PI/3,el:Math.PI/7};

  function wproj(xpos,r,theta,az,el){
    var X=xpos,Y=r*Math.cos(theta),Z=r*Math.sin(theta);
    var X1=X*Math.cos(az)-Y*Math.sin(az);
    var Y1=X*Math.sin(az)+Y*Math.cos(az);
    var Y2=Y1*Math.cos(el)-Z*Math.sin(el);
    var Z2=Y1*Math.sin(el)+Z*Math.cos(el);
    return [X1,-Z2,Y2];
  }

  var wc2=document.getElementById("washer-canvas-2d");
  var wc3=document.getElementById("washer-canvas-3d");

  function drawWasher2D(){
    var ctx=wc2.getContext("2d");
    var W=wc2.width,H=wc2.height;
    var PAD={l:48,r:16,t:20,b:40};
    var fn=WFUNS[wst.fnKey],nv=wst.n,hl=wst.hl;
    var xmax=fn.xmax,ymax=fn.ymax,dx=xmax/nv;
    function toC(x,y){return[PAD.l+x/xmax*(W-PAD.l-PAD.r),H-PAD.b-y/ymax*(H-PAD.t-PAD.b)];}
    ctx.clearRect(0,0,W,H); ctx.fillStyle="#0a0014"; ctx.fillRect(0,0,W,H);
    // grid
    ctx.strokeStyle="rgba(148,163,184,.1)"; ctx.lineWidth=1;
    for(var g=0;g<=Math.ceil(ymax);g++){var gc=toC(0,g);ctx.beginPath();ctx.moveTo(PAD.l,gc[1]);ctx.lineTo(W-PAD.r,gc[1]);ctx.stroke();}
    // shaded region between curves (background)
    ctx.fillStyle="rgba(248,113,113,.06)";
    ctx.beginPath();
    for(var k=0;k<=200;k++){var xk=k/200*xmax,ck=toC(xk,fn.R(xk));k===0?ctx.moveTo(ck[0],ck[1]):ctx.lineTo(ck[0],ck[1]);}
    for(var k=200;k>=0;k--){var xk=k/200*xmax,ck=toC(xk,fn.r(xk));ctx.lineTo(ck[0],ck[1]);}
    ctx.closePath(); ctx.fill();
    // washer slices (rectangles from r to R)
    for(var i=0;i<nv;i++){
      var xm=(i+.5)*dx,R=fn.R(xm),ri=fn.r(xm);
      var c0=toC(i*dx,ri),c1=toC((i+1)*dx,R);
      var isHi=(i===hl);
      // outer rect
      ctx.fillStyle=isHi?"rgba(248,113,113,.40)":i%2===0?"rgba(248,113,113,.16)":"rgba(248,113,113,.10)";
      ctx.strokeStyle=isHi?"#f87171":"rgba(248,113,113,.50)";
      ctx.lineWidth=isHi?2:1;
      ctx.fillRect(c0[0],c1[1],c1[0]-c0[0],c0[1]-c1[1]);
      ctx.strokeRect(c0[0],c1[1],c1[0]-c0[0],c0[1]-c1[1]);
      // inner "hole" (erase)
      var cr0=toC(i*dx,0),cr1=toC((i+1)*dx,ri);
      ctx.fillStyle="#0a0014";
      ctx.fillRect(cr0[0]+1,cr1[1],cr1[0]-cr0[0]-2,cr0[1]-cr1[1]);
      ctx.strokeStyle=isHi?"rgba(251,191,36,.8)":"rgba(251,191,36,.3)";
      ctx.lineWidth=isHi?1.5:0.8;
      ctx.strokeRect(cr0[0],cr1[1],cr1[0]-cr0[0],cr0[1]-cr1[1]);
      if(isHi){
        // R arrow
        var ca=toC((i+1)*dx-.5,0),cb=toC((i+1)*dx-.5,R);
        ctx.strokeStyle="#f87171"; ctx.lineWidth=1.5; ctx.setLineDash([3,3]);
        ctx.beginPath();ctx.moveTo(ca[0],ca[1]);ctx.lineTo(cb[0],cb[1]);ctx.stroke();
        // r arrow
        var cc=toC(i*dx+.5,0),cd=toC(i*dx+.5,ri);
        ctx.strokeStyle="#fbbf24";
        ctx.beginPath();ctx.moveTo(cc[0],cc[1]);ctx.lineTo(cd[0],cd[1]);ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle="#f87171"; ctx.font="bold 10px Georgia,serif"; ctx.textAlign="right";
        ctx.fillText("R",cb[0]-3,(ca[1]+cb[1])/2);
        ctx.fillStyle="#fbbf24"; ctx.textAlign="left";
        ctx.fillText("r",cd[0]+3,(cc[1]+cd[1])/2);
      }
    }
    // outer curve (R)
    ctx.strokeStyle="#f87171"; ctx.lineWidth=2.5;
    ctx.shadowColor="rgba(248,113,113,.5)"; ctx.shadowBlur=6;
    ctx.beginPath();
    for(var k=0;k<=400;k++){var xk=k/400*xmax,ck=toC(xk,fn.R(xk));k===0?ctx.moveTo(ck[0],ck[1]):ctx.lineTo(ck[0],ck[1]);}
    ctx.stroke(); ctx.shadowBlur=0;
    // inner curve (r)
    ctx.strokeStyle="#fbbf24"; ctx.lineWidth=2;
    ctx.shadowColor="rgba(251,191,36,.4)"; ctx.shadowBlur=5;
    ctx.beginPath();
    for(var k=0;k<=400;k++){var xk=k/400*xmax,ck=toC(xk,fn.r(xk));k===0?ctx.moveTo(ck[0],ck[1]):ctx.lineTo(ck[0],ck[1]);}
    ctx.stroke(); ctx.shadowBlur=0;
    // legend
    ctx.fillStyle="#f87171"; ctx.font="italic 12px Georgia,serif"; ctx.textAlign="left";
    var lp=toC(xmax*.5,fn.R(xmax*.5));ctx.fillText("R(x)="+fn.Rl,lp[0]+5,lp[1]-7);
    ctx.fillStyle="#fbbf24";
    var lp2=toC(xmax*.55,fn.r(xmax*.55));ctx.fillText("r(x)="+fn.rl,lp2[0]+5,lp2[1]+14);
    // axes
    var a0=toC(0,0),a1x=toC(xmax,0),a1y=toC(0,ymax);
    ctx.strokeStyle="#475569"; ctx.lineWidth=1.5;
    ctx.beginPath();ctx.moveTo(a0[0],a0[1]);ctx.lineTo(a1x[0]+10,a0[1]);ctx.stroke();
    ctx.beginPath();ctx.moveTo(a0[0],a0[1]);ctx.lineTo(a0[0],a1y[1]-8);ctx.stroke();
    ctx.fillStyle="#475569";
    ctx.beginPath();ctx.moveTo(a1x[0]+10,a0[1]-4);ctx.lineTo(a1x[0]+17,a0[1]);ctx.lineTo(a1x[0]+10,a0[1]+4);ctx.fill();
    ctx.font="11px Georgia,serif"; ctx.fillStyle="#64748b"; ctx.textAlign="center";
    for(var xi=0.25;xi<=xmax+.01;xi+=0.25){var tc=toC(xi,0);if(xi%0.5<0.01)ctx.fillText(xi.toFixed(2),tc[0],tc[1]+14);}
    ctx.textAlign="right";
    for(var yi=0;yi<=Math.floor(ymax);yi++){var tc2=toC(0,yi);ctx.fillText(yi,tc2[0]-6,tc2[1]+4);}
    ctx.fillStyle="#475569"; ctx.font="13px Georgia,serif";
    ctx.textAlign="center"; ctx.fillText("x",a1x[0]+21,a0[1]+4);
    ctx.fillStyle="#94a3b8"; ctx.font="12px Georgia,serif"; ctx.textAlign="center";
    ctx.fillText("2D Cross-Section (side view)",W/2,14);
  }

  function drawWasher3D(){
    var ctx=wc3.getContext("2d");
    var W=wc3.width,H=wc3.height;
    var az=wst.az,el=wst.el;
    var fn=WFUNS[wst.fnKey],nv=wst.n,hl=wst.hl,dx=fn.xmax/nv;
    ctx.clearRect(0,0,W,H); ctx.fillStyle="#0a0014"; ctx.fillRect(0,0,W,H);
    var ocx=W*.45,ocy=H*.55,scale=Math.min(W,H)*.22;
    var SEGS=52;

    function p3(xp,r,th){var s=wproj(xp,r,th,az,el);return[ocx+s[0]*scale,ocy+s[1]*scale];}
    function dep(xp,r,th){return wproj(xp,r,th,az,el)[2];}

    // draw annular face at xpos, between r0..r1
    function drawAnnFace(xp,r0,r1,fill,stroke,lw){
      ctx.beginPath();
      for(var s=0;s<=SEGS;s++){var th=s/SEGS*2*Math.PI,pt=p3(xp,r1,th);s===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var s=SEGS;s>=0;s--){var th=s/SEGS*2*Math.PI,pt=p3(xp,r0,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath();
      ctx.fillStyle=fill; ctx.strokeStyle=stroke; ctx.lineWidth=lw;
      ctx.fill(); ctx.stroke();
    }

    // draw cylindrical wall arc at radius r between x0..x1
    function drawCylWall(x0,x1,r,tStart,tEnd,fill,stroke,lw){
      var steps=Math.max(4,Math.round(SEGS*Math.abs(tEnd-tStart)/(2*Math.PI)));
      ctx.beginPath();
      for(var s=0;s<=steps;s++){var th=tStart+s/steps*(tEnd-tStart),pt=p3(x0,r,th);s===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
      for(var s=steps;s>=0;s--){var th=tStart+s/steps*(tEnd-tStart),pt=p3(x1,r,th);ctx.lineTo(pt[0],pt[1]);}
      ctx.closePath();
      ctx.fillStyle=fill; ctx.strokeStyle=stroke; ctx.lineWidth=lw;
      ctx.fill(); ctx.stroke();
    }

    var order=[];
    for(var i=0;i<nv;i++) order.push(i);
    order.sort(function(a,b){return dep((a+.5)*dx,0,0)-dep((b+.5)*dx,0,0);});

    for(var oi=0;oi<order.length;oi++){
      var i=order[oi];
      var x0=i*dx,x1=(i+1)*dx,xm=(x0+x1)/2;
      var R=fn.R(xm),ri=fn.r(xm),isHi=(i===hl);

      var outerFill  =isHi?"rgba(248,113,113,0.22)":"rgba(248,113,113,0.09)";
      var outerStroke=isHi?"#f87171":"rgba(248,113,113,0.50)";
      var innerFill  =isHi?"rgba(251,191,36,0.28)":"rgba(200,150,20,0.18)";
      var innerStroke=isHi?"rgba(251,191,36,0.90)":"rgba(251,191,36,0.55)";
      var faceFill   =isHi?"rgba(248,113,113,0.42)":"rgba(248,113,113,0.20)";
      var lw         =isHi?1.5:0.7;

      var backS=az+Math.PI/2,backE=az+3*Math.PI/2;
      var frontS=az-Math.PI/2,frontE=az+Math.PI/2;

      var nearX=(dep(x0,0,0)<dep(x1,0,0))?x1:x0;
      var farX =(nearX===x0)?x1:x0;

      // painter's order: far annular face, back outer wall, full inner wall, front outer wall, near annular face
      drawAnnFace(farX,ri,R,faceFill,outerStroke,lw*.8);
      drawCylWall(x0,x1,R,backS,backE,outerFill,outerStroke,lw);
      drawCylWall(x0,x1,ri,0,2*Math.PI,innerFill,innerStroke,lw*.9);
      drawCylWall(x0,x1,R,frontS,frontE,outerFill,outerStroke,lw);
      drawAnnFace(nearX,ri,R,faceFill,outerStroke,lw);
    }

    // x-axis
    var ax0=p3(-0.05,0,0),ax1=p3(fn.xmax*1.12,0,0);
    ctx.strokeStyle="rgba(148,163,184,.45)"; ctx.lineWidth=1.3; ctx.setLineDash([5,4]);
    ctx.beginPath();ctx.moveTo(ax0[0],ax0[1]);ctx.lineTo(ax1[0],ax1[1]);ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle="#94a3b8"; ctx.font="11px Georgia,serif"; ctx.textAlign="left";
    ctx.fillText("x (axis)",ax1[0]+4,ax1[1]+4);

    // outer surface curve
    ctx.strokeStyle="#f87171"; ctx.lineWidth=2;
    ctx.shadowColor="rgba(248,113,113,.5)"; ctx.shadowBlur=4;
    ctx.beginPath();
    for(var k=0;k<=120;k++){var xk=k/120*fn.xmax,pt=p3(xk,fn.R(xk),Math.PI/2);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
    ctx.stroke();
    // inner surface curve
    ctx.strokeStyle="#fbbf24"; ctx.lineWidth=1.8;
    ctx.shadowColor="rgba(251,191,36,.4)"; ctx.shadowBlur=4;
    ctx.beginPath();
    for(var k=0;k<=120;k++){var xk=k/120*fn.xmax,pt=p3(xk,fn.r(xk),Math.PI/2);k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);}
    ctx.stroke(); ctx.shadowBlur=0;

    // annotations on highlighted washer
    var xmh=(hl+.5)*dx,Rh=fn.R(xmh),rh=fn.r(xmh),x0h=hl*dx,x1h=(hl+1)*dx;
    // R arrow (outer radius)
    var pc=p3(xmh,0,Math.PI/2),pR=p3(xmh,Rh,Math.PI/2);
    ctx.strokeStyle="#f87171"; ctx.lineWidth=1.8;
    ctx.beginPath();ctx.moveTo(pc[0],pc[1]);ctx.lineTo(pR[0],pR[1]);ctx.stroke();
    ctx.fillStyle="#f87171";
    var angR=Math.atan2(pR[1]-pc[1],pR[0]-pc[0]);
    ctx.beginPath();ctx.moveTo(pR[0],pR[1]);ctx.lineTo(pR[0]-7*Math.cos(angR-.4),pR[1]-7*Math.sin(angR-.4));ctx.lineTo(pR[0]-7*Math.cos(angR+.4),pR[1]-7*Math.sin(angR+.4));ctx.fill();
    ctx.font="bold 11px Georgia,serif"; ctx.textAlign="right"; ctx.fillText("R",(pc[0]+pR[0])/2-4,(pc[1]+pR[1])/2);
    // r arrow (inner radius)
    var pr=p3(xmh,rh,Math.PI/2);
    ctx.strokeStyle="#fbbf24"; ctx.lineWidth=1.8;
    ctx.beginPath();ctx.moveTo(pc[0],pc[1]);ctx.lineTo(pr[0],pr[1]);ctx.stroke();
    ctx.fillStyle="#fbbf24";
    var angr=Math.atan2(pr[1]-pc[1],pr[0]-pc[0]);
    ctx.beginPath();ctx.moveTo(pr[0],pr[1]);ctx.lineTo(pr[0]-7*Math.cos(angr-.4),pr[1]-7*Math.sin(angr-.4));ctx.lineTo(pr[0]-7*Math.cos(angr+.4),pr[1]-7*Math.sin(angr+.4));ctx.fill();
    ctx.font="bold 11px Georgia,serif"; ctx.textAlign="left"; ctx.fillText("r",pr[0]+5,(pc[1]+pr[1])/2+4);
    // thickness
    var pe0=p3(x0h,Rh*1.08,Math.PI*.65),pe1=p3(x1h,Rh*1.08,Math.PI*.65);
    ctx.strokeStyle="#a78bfa"; ctx.lineWidth=1.5;
    ctx.beginPath();ctx.moveTo(pe0[0],pe0[1]);ctx.lineTo(pe1[0],pe1[1]);ctx.stroke();
    ctx.fillStyle="#a78bfa"; ctx.font="bold 11px Georgia,serif"; ctx.textAlign="center";
    ctx.fillText("\u0394x",(pe0[0]+pe1[0])/2,(pe0[1]+pe1[1])/2-8);

    ctx.fillStyle="#94a3b8"; ctx.font="12px Georgia,serif"; ctx.textAlign="center";
    ctx.fillText("3D Washer View  \u2014  drag to rotate",W/2,14);
  }

  function washerStats(){
    var fn=WFUNS[wst.fnKey],nv=wst.n,hl=wst.hl,dx=fn.xmax/nv;
    var xm=(hl+.5)*dx,R=fn.R(xm),ri=fn.r(xm),dv=Math.PI*(R*R-ri*ri)*dx;
    var tv=0,di=fn.xmax/1000;
    for(var i=0;i<1000;i++){var xi=(i+.5)*di,Ri=fn.R(xi),rii=fn.r(xi);tv+=Math.PI*(Ri*Ri-rii*rii)*di;}
    var ss=0;
    for(var i=0;i<nv;i++){var xi=(i+.5)*dx,Ri=fn.R(xi),rii=fn.r(xi);ss+=Math.PI*(Ri*Ri-rii*rii)*dx;}
    var err=Math.abs(ss-tv)/tv*100;
    var ec=err<1?"#4ade80":err<5?"#fbbf24":"#f87171";
    document.getElementById("washer-formula").innerHTML=
      "<span style='color:#fbbf24'>Washer #"+(hl+1)+"</span>"
      +"<span style='color:#94a3b8;margin:0 10px'>|</span>"
      +"\u0394V = \u03c0 [<span style='color:#f87171'>R</span><sup>2</sup>"
      +" \u2212 <span style='color:#fbbf24'>r</span><sup>2</sup>]"
      +" &middot; <span style='color:#a78bfa'>\u0394x</span>"
      +" = \u03c0 [<span style='color:#f87171'>"+R.toFixed(3)+"</span><sup>2</sup>"
      +" \u2212 <span style='color:#fbbf24'>"+ri.toFixed(3)+"</span><sup>2</sup>]"
      +" &middot; <span style='color:#a78bfa'>"+dx.toFixed(3)+"</span>"
      +" = <span style='color:#fbbf24;font-weight:bold'>"+dv.toFixed(4)+"</span>";
    document.getElementById("washer-stat-true").textContent=tv.toFixed(5);
    document.getElementById("washer-stat-sum").textContent=ss.toFixed(5);
    var ee=document.getElementById("washer-stat-err");
    ee.textContent=err.toFixed(3)+"%"; ee.style.color=ec;
  }

  function washerRedraw(){drawWasher2D();drawWasher3D();washerStats();}

  // buttons
  var wbc=document.getElementById("washer-fn-btns");
  WFK.forEach(function(k){
    var b=document.createElement("button");
    b.textContent="R="+WFUNS[k].Rl+", r="+WFUNS[k].rl; b.dataset.key=k;
    b.style.cssText="padding:6px 14px;border-radius:8px;cursor:pointer;font-size:12px;font-family:Georgia,serif;";
    b.addEventListener("click",function(){wst.fnKey=k;wst.hl=Math.floor(wst.n/3);updWBtns();washerRedraw();});
    wbc.appendChild(b);
  });
  function updWBtns(){wbc.querySelectorAll("button").forEach(function(b){var a=(b.dataset.key===wst.fnKey);b.style.border=a?"2px solid #f87171":"2px solid rgba(148,163,184,.2)";b.style.background=a?"rgba(248,113,113,.18)":"rgba(10,0,20,.5)";b.style.color=a?"#f87171":"#94a3b8";b.style.fontWeight=a?"bold":"normal";});}
  updWBtns();

  var wns=document.getElementById("washer-n-slider"),whs=document.getElementById("washer-hl-slider");
  wns.addEventListener("input",function(){wst.n=parseInt(this.value);wst.hl=Math.min(wst.hl,wst.n-1);whs.max=wst.n-1;whs.value=wst.hl;document.getElementById("washer-n-label").textContent="n = "+wst.n+" washers";document.getElementById("washer-hl-label").textContent="washer #"+(wst.hl+1);washerRedraw();});
  whs.addEventListener("input",function(){wst.hl=parseInt(this.value);document.getElementById("washer-hl-label").textContent="washer #"+(wst.hl+1);washerRedraw();});

  var wdrag={active:false,lastX:0,lastY:0};
  function wxy(e){return e.touches?{x:e.touches[0].clientX,y:e.touches[0].clientY}:{x:e.clientX,y:e.clientY};}
  wc3.addEventListener("mousedown",function(e){e.preventDefault();var p=wxy(e);wdrag={active:true,lastX:p.x,lastY:p.y};wc3.style.cursor="grabbing";});
  wc3.addEventListener("touchstart",function(e){e.preventDefault();var p=wxy(e);wdrag={active:true,lastX:p.x,lastY:p.y};},{passive:false});
  window.addEventListener("mousemove",function(e){if(!wdrag.active)return;var p=wxy(e);wst.az+=(p.x-wdrag.lastX)*.010;wst.el=Math.max(-Math.PI/2+.05,Math.min(Math.PI/2-.05,wst.el-(p.y-wdrag.lastY)*.010));wdrag.lastX=p.x;wdrag.lastY=p.y;drawWasher3D();});
  window.addEventListener("touchmove",function(e){if(!wdrag.active)return;e.preventDefault();var p=wxy(e);wst.az+=(p.x-wdrag.lastX)*.010;wst.el=Math.max(-Math.PI/2+.05,Math.min(Math.PI/2-.05,wst.el-(p.y-wdrag.lastY)*.010));wdrag.lastX=p.x;wdrag.lastY=p.y;drawWasher3D();},{passive:false});
  window.addEventListener("mouseup",function(){wdrag.active=false;wc3.style.cursor="grab";});
  window.addEventListener("touchend",function(){wdrag.active=false;});

  washerRedraw();
})();
</script>


<span id="shell-method"></span>
<h4>Shell method for volume calculation</h4>

[<span class="define">Shell integration</span>](https://en.wikipedia.org/wiki/Shell_integration){:target="_blank"}
(the <span class="define">shell method</span> in integral calculus)
is a method for calculating the volume of a solid of revolution,
when integrating along an axis perpendicular to the axis of revolution.
This is in contrast to disc integration which integrates along the axis parallel to the axis of revolution.

Consider a volume in three dimensions obtained by rotating a cross-section in the $xy$-plane around the $y$-axis.
Suppose the cross-section is defined by the graph of the positive function $f(x)$ on the interval $[a, b]$.
Then the formula for the volume will be

\begin{equation}
\label{eq:vol-shell-method-rot-y}
	V = 2 \pi \int_a^b x f(x) dx
\end{equation}

If the function is of the $y$ coordinate and the axis of rotation is the $x$-axis then the formula becomes

\begin{equation}
\label{eq:vol-shell-method-rot-x}
	V = 2 \pi \int_a^b y f(y) dy
\end{equation}

#### Interactive 3D visualization — shell method {#iv-shell-method}

<div id="shell-viz" style="background:linear-gradient(135deg,#020b14,#0f1f0a,#020b14);border-radius:16px;padding:24px;margin:24px 0;font-family:Georgia,serif;">

  <!-- Title -->
  <div style="text-align:center;margin-bottom:16px;">
    <div style="font-size:11px;letter-spacing:.3em;color:#4ade80;text-transform:uppercase;margin-bottom:4px;">Volume of Revolution</div>
    <div style="font-size:22px;color:#f1f5f9;font-weight:normal;">Shell Method — Interactive Visualization</div>
    <div style="font-size:13px;color:#94a3b8;font-style:italic;margin-top:4px;">
      V = 2&pi; &int; x &middot; f(x) dx &nbsp;=&nbsp; sum of hollow cylindrical shells
    </div>
  </div>

  <!-- Function buttons -->
  <div id="shell-fn-btns" style="display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-bottom:14px;"></div>

  <!-- Two canvases side by side -->
  <div style="display:flex;gap:10px;margin-bottom:12px;">
    <div style="flex:1;background:rgba(5,10,20,.8);border-radius:12px;border:1px solid rgba(148,163,184,.1);overflow:hidden;">
      <canvas id="shell-canvas-2d" width="420" height="270" style="width:100%;display:block;"></canvas>
    </div>
    <div style="flex:1;background:rgba(5,10,20,.8);border-radius:12px;border:1px solid rgba(56,189,248,.2);overflow:hidden;position:relative;">
      <canvas id="shell-canvas-3d" width="420" height="270" style="width:100%;display:block;cursor:grab;"></canvas>
      <div style="position:absolute;bottom:7px;right:9px;font-size:10px;color:rgba(56,189,248,.55);font-style:italic;background:rgba(0,0,0,.45);padding:2px 7px;border-radius:4px;pointer-events:none;">
        🖱 drag to rotate
      </div>
    </div>
  </div>

  <!-- Highlighted shell formula -->
  <div id="shell-formula" style="background:rgba(251,146,60,.08);border:1px solid rgba(251,146,60,.4);border-radius:10px;padding:11px 18px;margin-bottom:12px;text-align:center;font-size:14px;color:#f1f5f9;"></div>

  <!-- Sliders -->
  <div style="display:flex;flex-direction:column;gap:9px;margin-bottom:12px;">
    <div style="display:flex;align-items:center;gap:12px;">
      <span id="shell-n-label" style="color:#94a3b8;font-size:13px;min-width:100px;font-style:italic;">n = 6 shells</span>
      <input id="shell-n-slider" type="range" min="2" max="24" value="6" style="flex:1;accent-color:#38bdf8;">
      <span style="color:#64748b;font-size:11px;min-width:80px;text-align:right;">more &rarr; exact</span>
    </div>
    <div style="display:flex;align-items:center;gap:12px;">
      <span id="shell-hl-label" style="color:#94a3b8;font-size:13px;min-width:100px;font-style:italic;">shell #3</span>
      <input id="shell-hl-slider" type="range" min="0" max="5" value="2" style="flex:1;accent-color:#fb923c;">
      <span style="color:#64748b;font-size:11px;min-width:80px;text-align:right;">highlight</span>
    </div>
  </div>

  <!-- Stats row -->
  <div style="display:flex;gap:10px;margin-bottom:10px;">
    <div style="flex:1;background:rgba(5,10,20,.7);border:1px solid rgba(148,163,184,.1);border-radius:10px;padding:10px;text-align:center;">
      <div style="font-size:10px;color:#64748b;letter-spacing:.1em;text-transform:uppercase;margin-bottom:3px;">True Volume</div>
      <div id="shell-stat-true" style="font-size:15px;color:#4ade80;font-family:monospace;">—</div>
    </div>
    <div style="flex:1;background:rgba(5,10,20,.7);border:1px solid rgba(148,163,184,.1);border-radius:10px;padding:10px;text-align:center;">
      <div style="font-size:10px;color:#64748b;letter-spacing:.1em;text-transform:uppercase;margin-bottom:3px;">Shell Sum</div>
      <div id="shell-stat-sum" style="font-size:15px;color:#38bdf8;font-family:monospace;">—</div>
    </div>
    <div style="flex:1;background:rgba(5,10,20,.7);border:1px solid rgba(148,163,184,.1);border-radius:10px;padding:10px;text-align:center;">
      <div style="font-size:10px;color:#64748b;letter-spacing:.1em;text-transform:uppercase;margin-bottom:3px;">Error</div>
      <div id="shell-stat-err" style="font-size:15px;font-family:monospace;">—</div>
    </div>
  </div>

  <div style="text-align:center;font-size:11px;color:#475569;">
    <span style="color:#38bdf8;">n slider</span>: more shells &rarr; converges to exact &nbsp;|&nbsp;
    <span style="color:#fb923c;">highlight slider</span>: inspect each &Delta;V &nbsp;|&nbsp;
    <span style="color:rgba(56,189,248,.6);">drag 3D panel</span>: spin &amp; tilt freely
  </div>
</div>

<script>
(function(){
  // ── Functions ──────────────────────────────────────────────────────
  var FUNS = {
    "\u221ax":     { f: function(x){ return Math.sqrt(x); },           label:"\u221ax",     xmax:2.5, ymax:2.2 },
    "x\u00b2":    { f: function(x){ return x*x; },                     label:"x\u00b2",    xmax:2.2, ymax:2.2 },
    "x(2\u2212x)":{ f: function(x){ return x*(2-x); },                 label:"x(2\u2212x)",xmax:2.0, ymax:1.2 },
    "sin(\u03c0x)":{ f: function(x){ return Math.sin(Math.PI*x); },    label:"sin(\u03c0x)",xmax:1.0, ymax:1.1 }
  };
  var FN_KEYS = Object.keys(FUNS);

  // ── State ──────────────────────────────────────────────────────────
  var state = { fnKey: FN_KEYS[0], n: 6, hl: 2, az: Math.PI/4, el: Math.PI/6 };

  // ── 3D projection ──────────────────────────────────────────────────
  function proj3(r, theta, z, az, el) {
    var X = r*Math.cos(theta), Y = r*Math.sin(theta);
    var X1 = X*Math.cos(az) - Y*Math.sin(az);
    var Y1 = X*Math.sin(az) + Y*Math.cos(az);
    var Y2 = Y1*Math.cos(el) - z*Math.sin(el);
    var Z2 = Y1*Math.sin(el) + z*Math.cos(el);
    return [X1, -Z2, Y2]; // [sx, sy, depth]
  }

  // ── Canvas elements ────────────────────────────────────────────────
  var c2d = document.getElementById("shell-canvas-2d");
  var c3d = document.getElementById("shell-canvas-3d");

  // ── 2D draw ────────────────────────────────────────────────────────
  function draw2D() {
    var ctx = c2d.getContext("2d");
    var W = c2d.width, H = c2d.height;
    var PAD = {l:48,r:16,t:20,b:40};
    var fn = FUNS[state.fnKey], nv = state.n, hl = state.hl;
    var xmax = fn.xmax, ymax = fn.ymax, dx = xmax/nv;

    function toC(x,y){ return [PAD.l+x/xmax*(W-PAD.l-PAD.r), H-PAD.b-y/ymax*(H-PAD.t-PAD.b)]; }

    ctx.clearRect(0,0,W,H);
    ctx.fillStyle="#050a14"; ctx.fillRect(0,0,W,H);

    // grid
    ctx.strokeStyle="rgba(148,163,184,.1)"; ctx.lineWidth=1;
    for(var g=0;g<=Math.ceil(ymax);g++){
      var gc=toC(0,g); ctx.beginPath(); ctx.moveTo(PAD.l,gc[1]); ctx.lineTo(W-PAD.r,gc[1]); ctx.stroke();
    }

    // shells as rectangles
    for(var i=0;i<nv;i++){
      var xm=(i+.5)*dx, h=fn.f(xm);
      var c0=toC(i*dx,0), c1=toC((i+1)*dx,h);
      var isHi=(i===hl);
      ctx.fillStyle   = isHi?"rgba(251,146,60,.45)":i%2===0?"rgba(56,189,248,.15)":"rgba(56,189,248,.10)";
      ctx.strokeStyle = isHi?"#fb923c":"rgba(56,189,248,.5)";
      ctx.lineWidth   = isHi?2:1;
      ctx.fillRect(c0[0],c1[1],c1[0]-c0[0],c0[1]-c1[1]);
      ctx.strokeRect(c0[0],c1[1],c1[0]-c0[0],c0[1]-c1[1]);
      if(isHi){
        var cm=toC(xm,0);
        ctx.strokeStyle="#fb923c"; ctx.lineWidth=1.5; ctx.setLineDash([3,3]);
        ctx.beginPath(); ctx.moveTo(PAD.l,cm[1]); ctx.lineTo(cm[0],cm[1]); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle="#fb923c"; ctx.font="bold 11px Georgia,serif"; ctx.textAlign="center";
        ctx.fillText("r = x",(PAD.l+cm[0])/2,cm[1]-5);
        var cmh=toC(xm,h/2);
        ctx.fillText("h=f(x)",cmh[0],cmh[1]);
      }
    }

    // curve
    ctx.strokeStyle="#2dd4bf"; ctx.lineWidth=2.5;
    ctx.shadowColor="rgba(45,212,191,.5)"; ctx.shadowBlur=6;
    ctx.beginPath();
    for(var k=0;k<=400;k++){
      var xk=k/400*xmax, ck=toC(xk,fn.f(xk));
      k===0?ctx.moveTo(ck[0],ck[1]):ctx.lineTo(ck[0],ck[1]);
    }
    ctx.stroke(); ctx.shadowBlur=0;

    // axes
    var a0=toC(0,0), a1x=toC(xmax,0), a1y=toC(0,ymax);
    ctx.strokeStyle="#475569"; ctx.lineWidth=1.5;
    ctx.beginPath(); ctx.moveTo(a0[0],a0[1]); ctx.lineTo(a1x[0]+10,a0[1]); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(a0[0],a0[1]); ctx.lineTo(a0[0],a1y[1]-8); ctx.stroke();
    ctx.fillStyle="#475569";
    ctx.beginPath(); ctx.moveTo(a1x[0]+10,a0[1]-4); ctx.lineTo(a1x[0]+17,a0[1]); ctx.lineTo(a1x[0]+10,a0[1]+4); ctx.fill();
    ctx.beginPath(); ctx.moveTo(a0[0]-4,a1y[1]-8); ctx.lineTo(a0[0],a1y[1]-15); ctx.lineTo(a0[0]+4,a1y[1]-8); ctx.fill();
    ctx.font="11px Georgia,serif"; ctx.fillStyle="#64748b"; ctx.textAlign="center";
    for(var xi=0.5;xi<=xmax;xi+=0.5){var tc=toC(xi,0);ctx.fillText(xi,tc[0],tc[1]+14);}
    ctx.textAlign="right";
    for(var yi=1;yi<=Math.floor(ymax);yi++){var tc2=toC(0,yi);ctx.fillText(yi,tc2[0]-6,tc2[1]+4);}
    ctx.fillStyle="#2dd4bf"; ctx.font="italic 13px Georgia,serif"; ctx.textAlign="left";
    var lp=toC(xmax*.65,fn.f(xmax*.65));
    ctx.fillText("y = "+fn.label,lp[0]+6,lp[1]-8);
    ctx.fillStyle="#475569"; ctx.font="13px Georgia,serif";
    ctx.textAlign="center"; ctx.fillText("x",a1x[0]+21,a0[1]+4);
    ctx.textAlign="left";   ctx.fillText("y",a0[0]+6,a1y[1]-16);
    ctx.fillStyle="#94a3b8"; ctx.font="12px Georgia,serif"; ctx.textAlign="center";
    ctx.fillText("2D Cross-Section",W/2,14);
  }

  // ── 3D draw ────────────────────────────────────────────────────────
  function draw3D() {
    var ctx = c3d.getContext("2d");
    var W = c3d.width, H = c3d.height;
    var az=state.az, el=state.el;
    var fn=FUNS[state.fnKey], nv=state.n, hl=state.hl, dx=fn.xmax/nv;

    ctx.clearRect(0,0,W,H);
    ctx.fillStyle="#050a14"; ctx.fillRect(0,0,W,H);

    var ocx=W*.5, ocy=H*.55, scale=Math.min(W,H)*.27;
    var SEGS=52;

    function p3(r,theta,z){
      var s=proj3(r,theta,z,az,el);
      return [ocx+s[0]*scale, ocy+s[1]*scale];
    }
    function depth3(r,theta,z){ return proj3(r,theta,z,az,el)[2]; }

    // ── Draw annulus (ring cap) ──
    function drawAnnulus(r0,r1,z,fill,stroke,lw){
      ctx.beginPath();
      for(var s=0;s<=SEGS;s++){
        var th=s/SEGS*2*Math.PI, pt=p3(r1,th,z);
        s===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);
      }
      for(var s=SEGS;s>=0;s--){
        var th=s/SEGS*2*Math.PI, pt=p3(r0,th,z);
        ctx.lineTo(pt[0],pt[1]);
      }
      ctx.closePath();
      ctx.fillStyle=fill; ctx.strokeStyle=stroke; ctx.lineWidth=lw;
      ctx.fill(); ctx.stroke();
    }

    // ── Draw cylindrical wall arc ──
    function drawWall(r,zBot,zTop,tStart,tEnd,fill,stroke,lw){
      var steps=Math.max(4,Math.round(SEGS*Math.abs(tEnd-tStart)/(2*Math.PI)));
      ctx.beginPath();
      for(var s=0;s<=steps;s++){
        var th=tStart+s/steps*(tEnd-tStart), pt=p3(r,th,zBot);
        s===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);
      }
      for(var s=steps;s>=0;s--){
        var th=tStart+s/steps*(tEnd-tStart), pt=p3(r,th,zTop);
        ctx.lineTo(pt[0],pt[1]);
      }
      ctx.closePath();
      ctx.fillStyle=fill; ctx.strokeStyle=stroke; ctx.lineWidth=lw;
      ctx.fill(); ctx.stroke();
    }

    // sort shells back-to-front
    var order=[];
    for(var i=0;i<nv;i++) order.push(i);
    order.sort(function(a,b){
      return depth3((a+.5)*dx,0,fn.f((a+.5)*dx)*.5)
           - depth3((b+.5)*dx,0,fn.f((b+.5)*dx)*.5);
    });

    for(var oi=0;oi<order.length;oi++){
      var i=order[oi];
      var r0=i*dx, r1=(i+1)*dx, rm=(r0+r1)/2;
      var h=fn.f(rm), isHi=(i===hl);

      var outerFill   = isHi?"rgba(251,146,60,0.22)":"rgba(56,189,248,0.10)";
      var outerStroke = isHi?"#fb923c":"rgba(56,189,248,0.55)";
      var innerFill   = isHi?"rgba(251,100,20,0.30)":"rgba(14,116,163,0.22)";
      var innerStroke = isHi?"rgba(251,146,60,0.80)":"rgba(56,189,248,0.70)";
      var capFill     = isHi?"rgba(251,146,60,0.50)":"rgba(56,189,248,0.28)";
      var capStroke   = isHi?"#fb923c":"rgba(56,189,248,0.80)";
      var botFill     = isHi?"rgba(251,100,20,0.18)":"rgba(14,100,140,0.15)";
      var lw          = isHi?1.5:0.7;

      var backStart=az+Math.PI/2, backEnd=az+3*Math.PI/2;
      var frontStart=az-Math.PI/2, frontEnd=az+Math.PI/2;

      // 1. bottom annulus
      drawAnnulus(r0,r1,0,botFill,innerStroke,lw*.6);
      // 2. back outer wall
      drawWall(r1,0,h,backStart,backEnd,outerFill,outerStroke,lw);
      // 3. full inner wall (shows the hollow)
      drawWall(r0,0,h,0,2*Math.PI,innerFill,innerStroke,lw);
      // 4. front outer wall (semi-transparent)
      drawWall(r1,0,h,frontStart,frontEnd,outerFill,outerStroke,lw);
      // 5. top annulus (glowing ring — shows donut cross-section)
      drawAnnulus(r0,r1,h,capFill,capStroke,lw*1.2);
    }

    // rotation axis
    var zb=p3(0,0,-0.08), zt=p3(0,0,fn.ymax*1.15);
    ctx.strokeStyle="rgba(148,163,184,.4)"; ctx.lineWidth=1.2; ctx.setLineDash([5,4]);
    ctx.beginPath(); ctx.moveTo(zb[0],zb[1]); ctx.lineTo(zt[0],zt[1]); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle="#94a3b8"; ctx.font="11px Georgia,serif"; ctx.textAlign="center";
    ctx.fillText("axis",zt[0],zt[1]-8);

    // surface curve on front face
    ctx.strokeStyle="#2dd4bf"; ctx.lineWidth=2;
    ctx.shadowColor="rgba(45,212,191,.5)"; ctx.shadowBlur=4;
    ctx.beginPath();
    for(var k=0;k<=120;k++){
      var r=k/120*fn.xmax, pt=p3(r,0,fn.f(r));
      k===0?ctx.moveTo(pt[0],pt[1]):ctx.lineTo(pt[0],pt[1]);
    }
    ctx.stroke(); ctx.shadowBlur=0;

    // ── Annotations on highlighted shell ──
    var rm=(hl+.5)*dx, hh=fn.f(rm);
    var r0h=hl*dx, r1h=(hl+1)*dx;

    // radius arrow
    var p0=p3(0,0,0), p1=p3(r1h,0,0);
    ctx.strokeStyle="#fb923c"; ctx.lineWidth=1.8;
    ctx.beginPath(); ctx.moveTo(p0[0],p0[1]); ctx.lineTo(p1[0],p1[1]); ctx.stroke();
    var angR=Math.atan2(p1[1]-p0[1],p1[0]-p0[0]);
    ctx.fillStyle="#fb923c";
    ctx.beginPath(); ctx.moveTo(p1[0],p1[1]);
    ctx.lineTo(p1[0]-8*Math.cos(angR-.4),p1[1]-8*Math.sin(angR-.4));
    ctx.lineTo(p1[0]-8*Math.cos(angR+.4),p1[1]-8*Math.sin(angR+.4));
    ctx.fill();
    ctx.font="bold 12px Georgia,serif"; ctx.textAlign="center";
    ctx.fillText("r = x",(p0[0]+p1[0])/2,(p0[1]+p1[1])/2+15);

    // height arrow
    var frontTh=-az;
    var hb=p3(r1h*1.04,frontTh,0), ht=p3(r1h*1.04,frontTh,hh);
    ctx.strokeStyle="#2dd4bf"; ctx.lineWidth=1.8;
    ctx.beginPath(); ctx.moveTo(hb[0],hb[1]); ctx.lineTo(ht[0],ht[1]); ctx.stroke();
    var angH=Math.atan2(ht[1]-hb[1],ht[0]-hb[0]);
    ctx.fillStyle="#2dd4bf";
    ctx.beginPath(); ctx.moveTo(ht[0],ht[1]);
    ctx.lineTo(ht[0]-7*Math.cos(angH-.4),ht[1]-7*Math.sin(angH-.4));
    ctx.lineTo(ht[0]-7*Math.cos(angH+.4),ht[1]-7*Math.sin(angH+.4));
    ctx.fill();
    ctx.font="bold 12px Georgia,serif"; ctx.textAlign="left";
    ctx.fillText("h=f(x)",ht[0]+6,(hb[1]+ht[1])/2+4);

    // thickness Δx
    var topTh=-az+Math.PI*.7;
    var t0=p3(r0h,topTh,hh*1.12), t1=p3(r1h,topTh,hh*1.12);
    ctx.strokeStyle="#a78bfa"; ctx.lineWidth=1.5;
    ctx.beginPath(); ctx.moveTo(t0[0],t0[1]); ctx.lineTo(t1[0],t1[1]); ctx.stroke();
    ctx.fillStyle="#a78bfa"; ctx.font="bold 11px Georgia,serif"; ctx.textAlign="center";
    ctx.fillText("\u0394x",(t0[0]+t1[0])/2,(t0[1]+t1[1])/2-8);

    ctx.fillStyle="#94a3b8"; ctx.font="12px Georgia,serif"; ctx.textAlign="center";
    ctx.fillText("3D Shell View  \u2014  drag to rotate",W/2,14);
  }

  // ── Stats update ───────────────────────────────────────────────────
  function updateStats() {
    var fn=FUNS[state.fnKey], nv=state.n, hl=state.hl;
    var dx=fn.xmax/nv;
    var xm=(hl+.5)*dx, hv=fn.f(xm);
    var shellVol=2*Math.PI*xm*hv*dx;

    // true volume
    var tv=0, di=fn.xmax/1000;
    for(var i=0;i<1000;i++){var xi=(i+.5)*di; tv+=2*Math.PI*xi*fn.f(xi)*di;}

    // shell sum
    var ss=0;
    for(var i=0;i<nv;i++){var xi=(i+.5)*dx; ss+=2*Math.PI*xi*fn.f(xi)*dx;}

    var err=Math.abs(ss-tv)/tv*100;
    var errCol=err<1?"#4ade80":err<5?"#fbbf24":"#f87171";

    document.getElementById("shell-formula").innerHTML=
      "<span style='color:#fb923c'>Shell #"+(hl+1)+"</span>"
      +"<span style='color:#94a3b8;margin:0 10px'>|</span>"
      +"\u0394V = 2\u03c0 &middot; <span style='color:#fb923c'>r</span>"
      +" &middot; <span style='color:#2dd4bf'>h</span>"
      +" &middot; <span style='color:#a78bfa'>\u0394x</span>"
      +" = 2\u03c0 &middot; <span style='color:#fb923c'>"+xm.toFixed(3)+"</span>"
      +" &middot; <span style='color:#2dd4bf'>"+hv.toFixed(3)+"</span>"
      +" &middot; <span style='color:#a78bfa'>"+dx.toFixed(3)+"</span>"
      +" = <span style='color:#fbbf24;font-weight:bold'>"+shellVol.toFixed(4)+"</span>";

    document.getElementById("shell-stat-true").textContent=tv.toFixed(5);
    document.getElementById("shell-stat-sum").textContent=ss.toFixed(5);
    var errEl=document.getElementById("shell-stat-err");
    errEl.textContent=err.toFixed(3)+"%";
    errEl.style.color=errCol;
  }

  // ── Full redraw ────────────────────────────────────────────────────
  function redraw(){ draw2D(); draw3D(); updateStats(); }

  // ── Build function buttons ─────────────────────────────────────────
  var btnContainer=document.getElementById("shell-fn-btns");
  FN_KEYS.forEach(function(k){
    var btn=document.createElement("button");
    btn.textContent="y = "+FUNS[k].label;
    btn.dataset.key=k;
    btn.style.cssText="padding:6px 16px;border-radius:8px;cursor:pointer;font-size:13px;font-family:Georgia,serif;";
    btn.addEventListener("click",function(){
      state.fnKey=k;
      state.hl=Math.floor(state.n/3);
      updateButtons();
      redraw();
    });
    btnContainer.appendChild(btn);
  });

  function updateButtons(){
    btnContainer.querySelectorAll("button").forEach(function(b){
      var active=(b.dataset.key===state.fnKey);
      b.style.border=active?"2px solid #4ade80":"2px solid rgba(148,163,184,.2)";
      b.style.background=active?"rgba(74,222,128,.2)":"rgba(5,10,20,.5)";
      b.style.color=active?"#4ade80":"#94a3b8";
      b.style.fontWeight=active?"bold":"normal";
    });
  }
  updateButtons();

  // ── Sliders ────────────────────────────────────────────────────────
  var nSlider=document.getElementById("shell-n-slider");
  var hlSlider=document.getElementById("shell-hl-slider");

  nSlider.addEventListener("input",function(){
    state.n=parseInt(this.value);
    state.hl=Math.min(state.hl,state.n-1);
    hlSlider.max=state.n-1;
    hlSlider.value=state.hl;
    document.getElementById("shell-n-label").textContent="n = "+state.n+" shells";
    document.getElementById("shell-hl-label").textContent="shell #"+(state.hl+1);
    redraw();
  });
  hlSlider.addEventListener("input",function(){
    state.hl=parseInt(this.value);
    document.getElementById("shell-hl-label").textContent="shell #"+(state.hl+1);
    redraw();
  });

  // ── Mouse/touch drag on 3D canvas ─────────────────────────────────
  var drag={active:false,lastX:0,lastY:0};

  function getXY(e){
    if(e.touches) return {x:e.touches[0].clientX,y:e.touches[0].clientY};
    return {x:e.clientX,y:e.clientY};
  }
  c3d.addEventListener("mousedown",function(e){
    e.preventDefault();
    var p=getXY(e); drag={active:true,lastX:p.x,lastY:p.y};
    c3d.style.cursor="grabbing";
  });
  c3d.addEventListener("touchstart",function(e){
    e.preventDefault();
    var p=getXY(e); drag={active:true,lastX:p.x,lastY:p.y};
  },{passive:false});
  window.addEventListener("mousemove",function(e){
    if(!drag.active) return;
    var p=getXY(e);
    state.az += (p.x-drag.lastX)*0.010;
    state.el  = Math.max(-Math.PI/2+.05,Math.min(Math.PI/2-.05,state.el-(p.y-drag.lastY)*0.010));
    drag.lastX=p.x; drag.lastY=p.y;
    draw3D();
  });
  window.addEventListener("touchmove",function(e){
    if(!drag.active) return;
    e.preventDefault();
    var p=getXY(e);
    state.az += (p.x-drag.lastX)*0.010;
    state.el  = Math.max(-Math.PI/2+.05,Math.min(Math.PI/2-.05,state.el-(p.y-drag.lastY)*0.010));
    drag.lastX=p.x; drag.lastY=p.y;
    draw3D();
  },{passive:false});
  window.addEventListener("mouseup",function(){ drag.active=false; c3d.style.cursor="grab"; });
  window.addEventListener("touchend",function(){ drag.active=false; });

  // ── Initial draw ───────────────────────────────────────────────────
  redraw();
})();
</script>

#### Interactive 3D visualizations - volumes {#iv-volumes}

<h4>Equilateral Triangle Cross-Sections</h4>

<ul>
<li>
The solid whose cross-sections
perpendicular to the $x$-axis are <i>equilateral triangles</i> with
side length $s = x^2$ for $x \in [0,2]$.

$$
	V
	=
		\frac{\sqrt{3}}{4} \int_{0}^{2} (x^2)^2 dx
	=
		\frac{\sqrt{3}}{4} \cdot \frac{1}{5} \Bigl.\Bigl(x^5\Bigr)\Bigr|_{x=0}^2
	=
		\frac{8\sqrt{3}}{5}
	\simeq
		2.7713
$$

<div style="border: 1px solid #ccc; border-radius: 8px; overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15); margin: 24px 0;">
  <div style="background-color: #2c3e50; color: white;
              padding: 10px 16px; font-size: 13px;">
    <strong>3D Solid — Equilateral Triangle Cross-Sections</strong>
    <span style="opacity:0.7; margin-left:8px; font-size:11px">
      Drag to rotate · Auto-rotating
    </span>
  </div>
  <iframe
	src="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/solid-visualization.html"
    width="100%"
    height="520"
    frameborder="0"
    loading="lazy"
    title="3D solid with equilateral triangle cross-sections, y=x², x from 0 to 2"
    style="display:block;">
  </iframe>
</div>
</li>

<li>
The volume of the solid of revolution obtained
by rotating about the $x$-axis
the area under $y = \sin(x)$ from $x = 0$ to $x = \pi/2$.

<p>
<br>
<span class="emph">Daddy's Solution 1</span>
We can use the disc method \eqref{eq:vol-disc-method}
to have

\begin{eqnarray*}
V
	&=&
		\int_{0}^{\pi/2} \pi y^2 dx
	=
		\pi \int_{0}^{\pi/2} \sin(x)^2 dx
	=
		\frac{\pi}{2} \int_{0}^{\pi/2} (1-\cos(2x)) dx
\\
	&=&
		\frac{\pi}{2} \left[x + \frac{1}{2}\sin(2x)\right]_{0}^{\pi/2}
	=
		\frac{\pi^2}{4}
	\simeq
		2.4674
\end{eqnarray*}
</p>

<p>
<span class="emph">Daddy's Solution 2</span>
We can try to use the <a href="#shell-method">shell method</a> \eqref{eq:vol-shell-method-rot-x}
to have

\begin{eqnarray*}
V
	&=&
		2\pi \int_{0}^{1} y f(y) dy
			=
				2\pi \int_{0}^{1} y \left(\frac{\pi}{2} - \sin^{-1} y \right) dy
\\
	&=&
		2\pi \left[
			\frac{\pi}{4}y^2 - \frac{y^2\sin^{-1} y}{2} + \frac{\sin^{-1} y}{4} - \frac{y\sqrt{1-y^2}}{4}
		\right]_{0}^{1}
\\
	&=&
		2\pi \left(\frac{\pi}{4} - \frac{\pi}{4} + \frac{\pi}{8}\right)
			=
				\frac{\pi^2}{4}
			\simeq
				2.4674
\end{eqnarray*}
where
the integration by parts \eqref{eq:int-by-parts} together with \eqref{eq:int-arcsin} is used!
</p>

<div style="border: 1px solid #ccc; border-radius: 8px; overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15); margin: 24px 0;">
  <div style="background-color: #2c3e50; color: white;
              padding: 10px 16px; font-size: 13px;">
    <strong>3D Solid of Revolution — y = sin(x) about the x-axis</strong>
    <span style="opacity:0.7; margin-left:8px; font-size:11px">Drag to rotate</span>
  </div>
  <iframe
	src="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/solid-revolution-sinx.html"
    width="100%" height="520" frameborder="0" loading="lazy"
    title="Solid of revolution: y=sin(x) rotated about x-axis from 0 to pi/2"
    style="display:block;">
  </iframe>
</div>
</li>

<li>
The volume of the solid of revolution obtained
by rotating about the $y$-axis ($x=0$)
the region bounded by the $y$-axis, $y=1$, and the curve $y = \sin(x)$ ($0\leq x\leq \pi/2$) from $y = 0$ to $y = 1$.

<p>
<br>
<span class="emph">Daddy's Solution 1</span>
We can use the disc method \eqref{eq:vol-disc-method}
to get

\begin{eqnarray*}
V
	&=&
		\int_{0}^{1} \pi x^2 dy
	=
		\pi \int_{0}^{1} \sin^{-1}(y)^2 dy
\\
	&=&
		\pi \left.\left(
			-2y + y \sin^{-1}(y)^2 + 2\sqrt{1-y^2}\sin^{-1}(y)
			\right)\right|_{y=0}^1
\\
	&=&
		\pi \left(-2+\frac{\pi^2}{4}\right)
	=
		\frac{\pi^3}{4} - 2\pi
	\simeq
		1.4684
\end{eqnarray*}
where \eqref{eq:int-arcsin-squared} is used.
Note that \eqref{eq:int-arcsin-squared} is a very complicated
hard-to-remember indefinite integral formula!
</p>

<p>
<span class="emph">Daddy's Solution 2</span>
We can try to use the <a href="#shell-method">shell method</a> \eqref{eq:vol-shell-method-rot-y}
to have

\begin{eqnarray*}
V
	&=&
		2\pi \int_{0}^{\pi/2} x f(x) dx
			=
				2\pi \int_{0}^{\pi/2} x (1 - \sin x) dx
\\
	&=&
		2\pi\left[
			\frac{x^2}{2} + x \cos x - \sin x
		\right]_{0}^{\pi/2}
			=
				2\pi\left(
					\frac{\pi^2}{8} - 1
				\right)
\\
	&=&
		\frac{\pi^3}{4} - 2\pi
			\simeq
				1.4684
\end{eqnarray*}
where
the integration by parts \eqref{eq:int-by-parts} is used!
Note that <i>in this case</i>, we don't need to use a complicated indefinite integral formula as above
if we use the shell method!
</p>

<div style="border: 1px solid #ccc; border-radius: 8px; overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15); margin: 24px 0;">
  <div style="background-color: #2c3e50; color: white;
              padding: 10px 16px; font-size: 13px;">
    <strong>3D Solid of Revolution — y = sin(x) rotated about the y-axis</strong>
    <span style="opacity:0.7; margin-left:8px; font-size:11px">Drag to rotate</span>
  </div>
  <iframe
	src="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/solid-revolution-sinx-yaxis.html"
    width="100%" height="520" frameborder="0" loading="lazy"
    title="Solid of revolution: region between y-axis and y=sin(x), rotated about y-axis"
    style="display:block;">
  </iframe>
</div>
</li>

<li>
The volume of the solid of revolution obtained
by rotating about the $y$-axis ($x=0$)
the region bounded by the $x=\pi/2$, the $x$-axis, and the curve $y = \sin(x)$ ($0\leq x\leq \pi/2$),
from $y = 0$ to $y = 1$.

<p>
<br>
<span class="emph">Daddy's Solution 1</span>

If we simply use the above result,

$$
	V
		=
			\pi (\pi/2)^2 \cdot 1 - \left( \frac{\pi^3}{4} - 2\pi \right)
		=
			2\pi
$$

Beautifully clean answer!
</p>

<p>
<span class="emph">Daddy's Solution 2</span>

Now let's try to use the <a href="#shell-method">shell method</a> \eqref{eq:vol-shell-method-rot-y}
$$
\begin{eqnarray*}
	V
	&=&
		2 \pi \int_{0}^{\pi/2} x f(x) \,dx
	=
		2 \pi \int_{0}^{\pi/2} x \sin(x) \,dx
\\
	&=&
		2 \pi \Bigl.\Bigl( - x \cos(x)  + \sin(x)\Bigr)\Bigr|_{x=0}^{\pi/2}
	=
		2 \pi
\end{eqnarray*}
$$

which is almost as simple as the previous one except that we don't need to depend on the solution of the previous problem!
</p>

<div style="border: 1px solid #ccc; border-radius: 8px; overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15); margin: 24px 0;">
  <div style="background-color: #2c3e50; color: white;
              padding: 10px 16px; font-size: 13px;">
    <strong>3D Solid of Revolution — washer method, y = sin(x) about the y-axis</strong>
    <span style="opacity:0.7; margin-left:8px; font-size:11px">Drag to rotate</span>
  </div>
  <iframe
    src="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/solid-revolution-washer-yaxis.html"
    width="100%" height="520" frameborder="0" loading="lazy"
    title="Solid of revolution: washer method, region under y=sin(x) rotated about y-axis"
    style="display:block;">
  </iframe>
</div>
</li>
</ul>

## Infinite Sequences and Series

### Sequences

A [sequence](https://en.wikipedia.org/wiki/Sequence){:target="_blank"}
is a collection of objects possibly with repetition, that come in a specified order.
Like a set, it contains members (also called elements, or terms).
Unlike a set, the same elements can appear multiple times at different positions in a sequence, and unlike a set, the order does matter.<sup><a href="#footnote02" id="ref02">2</a></sup>

For example, (M, A, R, Y) is a sequence of letters with the letter &ldquo;M&rdquo; first and &ldquo;Y&rdquo; last.
This sequence differs from (A, R, M, Y).
Also, the sequence (1, 1, 2, 3, 5, 8), which contains the number 1 at two different positions, is a valid sequence.
Sequences can be finite, as in these examples, or infinite, such as the sequence of even positive integers (2, 4, 6, &hellip;).

<span id="sequence-examples"></span>
<h4>Examples</h4>

<h5>Sign sequence</h5>

A
[<span class="define">sign sequence</span>
or
<span class="define">$\pm1$-sequence</span>
or
<span class="define">bipolar sequence</span>](https://en.wikipedia.org/wiki/Sign_sequence){:target="_blank"}
is a sequence of numbers,
each of which is either $1$ or $−1$. One example is the sequence $(1, −1, 1, −1, \ldots)$,
*i.e.*,

\begin{equation}
\label{eq:sign-seq}
	a_n = (-1)^n
\end{equation}

<h5>Arithmetic sequence</h5>

An
[<span class="define">arithmetic progression</span>
or
<span class="define">arithmetic sequence</span>
or
<span class="define">linear sequence</span>](https://en.wikipedia.org/wiki/Arithmetic_progression){:target="_blank"}
is
a sequence of numbers such that the difference from any succeeding term to its preceding term remains constant throughout the sequence.
The constant difference is called <span class="define">common difference</span> of that arithmetic progression.
For instance, the sequence $5, 7, 9, 11, 13, 15, \ldots$ is an arithmetic progression with a common difference of $2$.

If the initial term of an arithmetic progression is $a_{1}$ and the common difference of successive members is $d$,
then the $n$-th term of the sequence $$\{a_n\}$$ is given by

\begin{equation}
\label{eq:arith-seq}
	a_n = a_1 + (n-1)d
\end{equation}

<h5>Geometric sequence</h5>

An
[<span class="define">geometric progression</span>
or
<span class="define">geometric sequence</span>](https://en.wikipedia.org/wiki/Geometric_progression){:target="_blank"}
is a mathematical sequence of non-zero numbers where each term after the first is found by multiplying the previous one by a fixed number
called the <span class="define">common ratio</span>.

For example, the sequence $2, 6, 18, 54, \ldots$ is a geometric progression with a common ratio of $3$.
Similarly $10, 5, 2.5, 1.25, \ldots$ is a geometric sequence with a common ratio of $1/2$.

The general form of a geometric sequence is

\begin{equation}
\label{eq:geo-seq}
	a_n = a r^{n-1}
\end{equation}

where $r$ is the common ratio and $a$ is the <span class="define">initial value</span>.

<span id="constant-recursive-sequence"></span>
<h5>Constant-recursive sequence</h5>

An infinite sequence of numbers $$\{a_n\}_{n=1}^\infty$$
is called <span class="define">constant-recursive</span>
if it satisfies an equation of the form

\begin{equation}
\label{eq:recursion}
	a_n = c_1 a_{n-1} + c_2 a_{n-2} + \cdots + c_d a_{n-d}
\end{equation}

for all $n>d$ where $c_i$ are constants.
The equation is called a <span class="define">linear recurrence relation</span>.
The concept is also known as a
[<span class="define">linear recurrence sequence</span>,
<span class="define">linear-recursive sequence</span>,
<span class="define">linear-recurrent sequence</span>,
or
<span class="define">a C-finite sequence</span>](https://en.wikipedia.org/wiki/Constant-recursive_sequence){:target="_blank"}.

<h5>Fibonacci sequence</h5>

[Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence){:target="_blank"}
is a sequence in which each element is the sum of the two elements that precede it.

The Fibonacci numbers may be defined by the recurrence relation

$$
\begin{eqnarray}
&
	F_0 = 0, \; F_1 = 1
&
\\
&
	F_n = F_{n-1} + F_{n-2}
&
	\mbox{for } n \geq 2
\end{eqnarray}
$$

thus
Fibonacci sequence is a [constant-recursive sequence](#constant-recursive-sequence) with $d=2$.

The sequence is $(0, 1, 1, 2, 3, 5, 8, 13, 21, 34, \ldots)$.

<h4>Increasing and decreasing</h4>

A sequence is said to be <span class="define">monotonically increasing</span> if each term is greater than or equal to the one before it.
For example, the sequence $$\{a_n\}_{n=1}^\infty$$ is monotonically increasing if and only if
$a_{n+1}\geq a_{n}$ for all $n \in \naturals$.
If each consecutive term is strictly greater than ($>$) the previous term
then the sequence is called <span class="define">strictly monotonically increasing</span>.
A sequence is <span class="define">monotonically decreasing</span>
if each consecutive term is less than or equal to the previous one,
and is <span class="define">strictly monotonically decreasing</span> if each is strictly less than the previous.
If a sequence is either increasing or decreasing it is called a <span class="define">monotone sequence</span>.
(This is a special case of the more general notion of a monotonic function.)

The terms <span class="define">nondecreasing</span> and <span class="define">nonincreasing</span>
are often used in place of *increasing* and *decreasing*
in order to avoid any possible confusion with strictly increasing and strictly decreasing, respectively.

<h4>Bounded</h4>

If the sequence of real numbers $$\{a_n\}_{n=1}^\infty$$ is such that all the terms are less than some real number $M$,
then the sequence is said to be <span class="define">bounded from above</span>.
In other words, this means that there exists $M$ such that for all $n$, $a_n \leq M$.
Any such $M$ is called an <span class="define">upper bound</span>.
Likewise, if, for some real $m$, $a_n \geq m$ for all $n$,
then the sequence is said to be <span class="define">bounded from below</span> and any such $m$ is called a <span class="define">lower bound</span>.
If a sequence is both bounded from above and bounded from below, then the sequence is said to be <span class="define">bounded</span>.

### Limits and Convergence

An important property of a sequence is <span class="define">convergence</span>.
If a sequence converges, it converges to a particular value known as the <span class="define">limit</span>.
If a sequence converges to some limit, then it is <span class="define">convergent</span>.
A sequence that does not converge is <span class="define">divergent</span>.

Informally, a sequence has a limit if the elements of the sequence become closer and closer to some value $L$
(called the limit of the sequence),
and they become and remain *arbitrarily* close to $L$,
(meaning that given a real number $d$ greater than zero,
all but a finite number of the elements of the sequence have a distance from $L$ less than $d$).
In this case, we write

\begin{equation}
\label{eq:limit-seq}
	\lim_{n\to\infty} a_n = L
\end{equation}

<h4>Examples</h4>

$$
\begin{eqnarray*}
\begin{array}{lcl}
	\lim_{n\to\infty} \left( \dfrac{n+1}{2n^2} \right)
		&=&
			0
\\
	\lim_{n\to\infty} \left( \dfrac{n^2+3n+100}{2n^2 + 10} \right)
		&=&
			\dfrac{1}{2}
\\
	\lim_{n\to\infty} n^3
		&=&
			\infty
\\
	\lim_{n\to\infty} (-1)^n
		&\mbox{is}&
			\mbox{divergent}
\end{array}
\end{eqnarray*}
$$

<h4>Important results</h4>

If
$$\{a_n\}_{n=1}^\infty$$
and
$$\{b_n\}_{n=1}^\infty$$
are convergent sequences,
the following limits exist,
and can be computed as follows.

$$
\begin{eqnarray}
\lim_{n\to\infty} (a_n + b_n)
	&=&
		\lim_{n\to\infty} a_n + \lim_{n\to\infty} b_n
\\
\lim_{n\to\infty} (a_n - b_n)
	&=&
		\lim_{n\to\infty} a_n - \lim_{n\to\infty} b_n
\\
\lim_{n\to\infty} (ca_n)
	&=&
		c \lim_{n\to\infty} \; \mbox{for } c \in \reals
\\
\lim_{n\to\infty} (a_n b_n)
	&=&
		\left(\lim_{n\to\infty} a_n \right) \left(\lim_{n\to\infty} b_n\right)
\\
\lim_{n\to\infty} \frac{a_n}{b_n}
	&=&
		\left(\lim_{n\to\infty} a_n \right) /\left(\lim_{n\to\infty} b_n\right)
			\; \mbox{provided } \lim_{n\to\infty} b_n \neq 0
\end{eqnarray}
$$

Moreover

- If $a_n \leq b_n$ for all $n>N$ for some $N$,
then $\lim_{n\to\infty} a_n \leq \lim_{n\to\infty} b_n$.
- If $a_n \leq c_n \leq b_n$ for all $n>N$ for some $N$ and $\lim_{n\to\infty} a_n = \lim_{n\to\infty} b_n = L$,
then $$\{a_n\}_{n=1}^\infty$$ is convergent and $\lim_{n\to\infty} c_n = L$.
- If a sequence is bounded and monotonic,
then it is convergent.
- A sequence is convergent if and only if all of its subsequences are convergent.

### Series

A [<span class="define">series</span>](https://en.wikipedia.org/wiki/Sequence#Series){:target="_blank"} is, informally speaking, the sum of the terms of a sequence. That is, it is an expression of the form

\begin{equation}
\sum _{n=1}^{\infty} a_n
\end{equation}

or

\begin{equation}
a_1 + a_2 + a_3 + \cdots
\end{equation}

where $$\{a_n\}_{n=1}^\infty$$ is a sequence of real or complex numbers.

<span id="series-examples"></span>
<h4>Examples</h4>

<h5><a target="_blank" href="https://en.wikipedia.org/wiki/Geometric_series">Geometric series</a></h5>

\begin{equation}
\label{eq:geo-series}
	\sum_{n} a r^{n-1}
\end{equation}

- The finite sum

\begin{equation}
\label{eq:geo-series-finite-sum}
	\sum_{k=1}^n a r^{k-1}
		=
			a \frac{r^n-1}{r-1}
		=
			a \frac{1-r^n}{1-r}
\end{equation}

- The infinite sum ($a\neq0$)

$$
\begin{equation}
\label{eq:geo-series-infinite-sum}
	\sum_{n=1}^\infty a r^{n-1}
		= \left\{ \begin{array}{ll}
				\dfrac{a}{1-r}	&\mbox{if } |r| < 1
			\\
				\infty	&\mbox{if } r = 1,\; a >0
			\\
				-\infty	&\mbox{if } r = 1,\; a <0
			\\
				\mbox{oscillates, hence diverges}	&\mbox{if } r = -1
			\\
				\mbox{diverges}	&\mbox{if } |r|>1
		\end{array}
		\right.
\end{equation}
$$

<h5><a target="_blank" href="https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)">Harmonic series</a></h5>

\begin{equation}
\label{eq:harmonic-series}
	\sum_{n} \frac{1}{n}
\end{equation}

- The infinite sum diverges!

\begin{equation}
\label{eq:harmonic-series-infinite-sum}
	\sum_{n} \frac{1}{n} = \infty
\end{equation}

<h5><a target="_blank" href="https://en.wikipedia.org/wiki/Alternating_series">Alternating series</a></h5>

An alternating series is an infinite series of terms that alternate between positive and negative signs.

<ul>
<li>
Some examples

\begin{equation}
\label{eq:alternating-series-example-01}
	\sum_{n=1}^\infty \frac{(-1)^{n+1}}{n} = 1 - \frac{1}{2} + \frac{1}{3} - \cdots = \ln 2
\end{equation}

\begin{equation}
\label{eq:alternating-series-example-02}
	\sum_{n=1}^\infty \frac{(-1)^{n+1}}{2n-1} = 1 - \frac{1}{3} + \frac{1}{5} - \cdots = \frac{\pi}{4}
\end{equation}
</li>
</ul>

<h5><a target="_blank" href="https://en.wikipedia.org/wiki/Dirichlet_series">Dirichlet series</a></h5>

\begin{equation}
\label{eq:dirichlet-series}
	\sum_{n} \frac{1}{n^p}
\end{equation}

- The infinite sum converges if and only if $p>1$.

- when $p=2$

\begin{equation}
\label{eq:dirichlet-series-2}
	\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}
\end{equation}

### Series Convergence

The <span class="define">partial sums</span> of a series are the expressions resulting from replacing the infinity symbol with a finite number,
*i.e.*, the $N$-th partial sum of the series

\begin{equation}
	S_N = \sum_{n=1}^N a_n = a_1 + a_2 + \cdots + a_N
\end{equation}

The partial sums themselves form a sequence $$\{S_N\}_{N=1}^\infty$$,
which is called the <span class="define">sequence of partial sums</span> of the series $\sum_{n=1}^{\infty}a_{n}$.
If the sequence of partial sums converges, then we say that the series $\sum_{n=1}^{\infty}a_{n}$ is convergent,
and the limit

\begin{equation}
	\lim_{N\to\infty} S_N
\end{equation}

is called the <span class="define">value of the series</span>.
The same notation is used to denote a series and its value, *i.e.*, we write

\begin{equation}
	\sum_{n=1}^\infty = \lim_{N\to\infty} S_N
\end{equation}

<h4>Examples</h4>

<!--
$$
\begin{eqnarray}
	\sum_{n=1}^\infty \dfrac{1}{n}
		&=&
			\infty
\\
	\sum_{n=1}^\infty \dfrac{(-1)^{n+1}}{n}
		&=&
			\ln 2
\\
	\sum_{p: \text{prime number}}^\infty \dfrac{1}{p}
		&=&
			\dfrac{1}{2} + \dfrac{1}{3} + \dfrac{1}{5} + \dfrac{1}{7} + \dfrac{1}{11} + \cdots = \infty
\\
	\sum_{n=1}^\infty \dfrac{1}{n(n+1)}
		&=&
			1
\\
	\sum_{n=1}^\infty \dfrac{1}{n!}
		&=&
			e
\\
	\sum_{n=1}^\infty \dfrac{1}{n^2}
		&=&
			\dfrac{\pi^2}{6}
\\
	\sum_{n=0}^\infty r^n
		&=&
			\dfrac{1}{1-r}
			\; \mbox{assuming } |r| < 1
\end{eqnarray}
$$
-->

$$
\begin{eqnarray}
\label{eq:infinite-series-sums}
\begin{array}{lllc}
	\sum_{n=0}^\infty r^n
		&=
			\dfrac{1}{1-r}
			\qquad \mbox{assuming } |r| < 1
\\
	\sum_{n=1}^\infty \dfrac{1}{n}
		&=
			\dfrac{1}{1} + \dfrac{1}{2} + \dfrac{1}{3} + \dfrac{1}{4} + \dfrac{1}{5} + \cdots
		&=
			&\infty
\\
	\sum_{p:\;\text{prime number}}^\infty \dfrac{1}{p}
		&=
			\dfrac{1}{2} + \dfrac{1}{3} + \dfrac{1}{5} + \dfrac{1}{7} + \dfrac{1}{11} + \cdots
		&=
			&\infty
\\
	\sum_{n=1}^\infty \dfrac{(-1)^{n+1}}{n}
		&=
			\dfrac{1}{1} - \dfrac{1}{2} + \dfrac{1}{3} - \dfrac{1}{4} + \dfrac{1}{5} - \cdots
		&=
			&\ln 2
\\
	\sum_{n=1}^\infty \dfrac{(-1)^{n+1}}{2n-1}
		&=
			\dfrac{1}{1} - \dfrac{1}{3} + \dfrac{1}{5} - \dfrac{1}{7} + \dfrac{1}{9} - \cdots
		&=
			&\dfrac{\pi}{4}
\\
	\sum_{n=1}^\infty \dfrac{1}{n(n+1)}
		&=
			\dfrac{1}{1\cdot 2} + \dfrac{1}{2\cdot 3} + \dfrac{1}{3\cdot 4} + \cdots
		&=
			&1
\\
	\sum_{n=1}^\infty \dfrac{1}{n^2}
		&=
			\dfrac{1}{1^2} + \dfrac{1}{2^2} + \dfrac{1}{3^2} + \dfrac{1}{4^2} + \cdots
		&=
			&\dfrac{\pi^2}{6}
\\
	\sum_{n=1}^\infty \dfrac{1}{(2n-1)^2}
		&=
			\dfrac{1}{1^2} + \dfrac{1}{3^2} + \dfrac{1}{5^2} + \dfrac{1}{7^2} + \cdots
		&=
			&\dfrac{\pi^2}{8}
\\
	\sum_{n=1}^\infty \dfrac{1}{n^4}
		&=
			\dfrac{1}{1^4} + \dfrac{1}{2^4} + \dfrac{1}{3^4} + \dfrac{1}{4^4} + \cdots
		&=
			&\dfrac{\pi^4}{90}
\\
	\sum_{n=1}^\infty \dfrac{1}{(2n-1)^4}
		&=
			\dfrac{1}{1^4} + \dfrac{1}{3^4} + \dfrac{1}{5^4} + \dfrac{1}{7^4} + \cdots
		&=
			&\dfrac{\pi^4}{96}
\\
	\sum_{n=0}^\infty \dfrac{1}{n!}
		&=
			\dfrac{1}{0!} + \dfrac{1}{1!} + \dfrac{1}{2!} + \dfrac{1}{3!} + \cdots
		&=
			&e
\end{array}
\end{eqnarray}
$$

Please refer to [Sums of Sequences](/prajna/coincidence-vs-inevitability#sums-of-sequences){:target="_blank"}
of [{{ inevitability.title }}]({{ inevitability.url }}){:target="_blank"},
which is Daddy's Philosophical and Existential Exploratory blogs,
if you want to know more fun results for some of infinite series!

### Conditional and Absolute Convergence

If the series $\absseries$ converges, then the series $\series$ is said to be
[<span class="define">absolutely convergent</span>](https://en.wikipedia.org/wiki/Absolutely_convergent){:target="_blank"}.
<span class="emph">Every absolute convergent series (real or complex) is also convergent</span>,
but <span style="color: red; font-weight: bold;">the converse is not true.</span>
(For example, the Maclaurin series of the exponential function is absolutely convergent for every complex value of the variable.)

If the series $\series$ converges but the series $\absseries$ diverges,
then the series $\series$
is [<span class="define">conditionally convergent</span>](https://en.wikipedia.org/wiki/Conditionally_convergent){:target="_blank"}.
(For example, the Maclaurin series of the logarithm function $\ln(1+x)$ is conditionally convergent for $x = 1$.)

<h4>Examples</h4>

- Let $a_n=(-1)^n/n!$ for $n\geq 0$. Then $\series = 1 - 1/1! + 1/2! - \cdots$ converges (to $e^{-1}$),
and $\absseries$ also converges (to $e^1$),
hence $\series$ **absolutely** converges!

- Let $a_n = (-1)^{n+1}/n$ for $n\geq 1$. Then $\series =  1 - 1/2 + 1/3 - \cdots$ converges (to $\ln 2$),
but $\absseries$ diverges (to $\infty$),
hence $\series$ **conditionally** converges!

### Series Convergence Tests

<h4>$p$-series test</h4>

The series

\begin{equation}
	\sum_{n=1}^\infty \frac{1}{n^p}
\end{equation}

converges if and only if $p>1$.

<h4>Comparison test</h4>

If $|a_n| \leq b_n$ for all $n>N$ for some $N$ and $\sum_{n=1}^\infty b_n$ converges,
$\sum_{n=1}^\infty a_n$ converges.

<h5>Corollary</h5>

If $0\leq a_n \leq b_n$ for all $n$ and $\sum_{n=1}^\infty b_n$ converges,
$\sum_{n=1}^\infty a_n$ converges.

<h4>Ratio test</h4>

Assume $a_n\neq 0$ for all $n$. Suppose that

$$
	\lim_{n\to\infty} \left|\frac{a_{n+1}}{a_n}\right| = r.
$$

- If $r<1$, then the series is absolutely convergent.
- If $r > 1$, then the series diverges.
- If $r = 1$, the ratio test is **inconclusive**, and the series may converge or diverge.

<h4>Integral test</h4>

Assume $f:\reals\to\reals$.
If $a_n = f(n)$ is a positive and monotonically decreasing function and

$$
	\int_{1}^\infty f(x) dx = \lim_{t\to\infty} \int_1^t f(x) dx < \infty
$$

then the series converges.
But if the integral diverges, then the series diverges, too.

<h4>Limit comparison test</h4>

If $a_n >0$, $b_n>0$, and the limit $\lim_{n\to\infty} a_n / b_n$ exists and nonzero,
then $\series$ converges **if and only if** $\sum_{n=1}^\infty b_n$ converges.

<h4>Alternating series test</h4>

Also known as the [Leibniz criterion](https://en.wikipedia.org/wiki/Alternating_series_test){:target="_blank"},
the [<span class="define">alternating series test</span>](https://en.wikipedia.org/wiki/Alternating_series_test){:target="_blank"}
states that for an [alternating series](https://en.wikipedia.org/wiki/Alternating_series){:target="_blank"}
of the form

\begin{equation}
\label{eq:alt-series}
	\sum_{n=1}^\infty (-1)^n a_n
\end{equation}

if $$\{a_n\}_{n=1}^\infty$$ is monotonically decreasing, and has a limit of $0$ at infinity,
then the series converges.

## Ordinary Differential Equations (ODE)

### Linear ODE

\begin{equation}
\label{eq:ode-linear}
\frac{d}{dt} y(t) = a y + b
\end{equation}

where $a\neq 0$

Let's solve this ODE as follows.

$$
\begin{eqnarray}
\label{eq:001}
\frac{d y}{y+b/a} = a\, dt
	&\Leftrightarrow&
		\ln (y+b/a) = a t + C
\\
\nonumber
	&\Leftrightarrow&
		y+b/a = e^{a t + C}
\end{eqnarray}
$$

hence we have

\begin{equation}
\label{eq:ode-linear-sol-gen}
y(t) = e^{at+C} - \frac{b}{a}
\end{equation}

Now assume the initial condition $y(0) \in \reals$. Because we can calculate $C$ from \eqref{eq:001},
*i.e.*,

\begin{equation}
\label{eq:ode-linear-c}
C = \ln(y(0)+b/a)
\end{equation}

if we plug \eqref{eq:ode-linear-c} into \eqref{eq:ode-linear-sol-gen},
we have

\begin{equation}
\label{eq:ode-linear-sol}
y(t)
=
	e^{at+\ln(y(0)+b/a)} - \frac{b}{a}
=
	\left(
		y(0) + \frac{b}{a}
	\right) e^{at}
	- \frac{b}{a}
\end{equation}

### ODE for Logistic Function

\begin{equation}
\label{eq:ode-logistic-fcn}
\frac{d}{dt} y(t) = a y(b-y)
\end{equation}

with $a>0$ and $b>0$.

Let's solve this ODE as follows.

$$
\begin{eqnarray*}
\frac{d y}{y(b-y)} = a\, dt
	&\Leftrightarrow&
		\left(\frac{1}{y} + \frac{1}{b-y}\right) dy = ab\, dt
\\
	&\Leftrightarrow&
		\ln y - \ln (b-y) = ab t + C
\\
	&\Leftrightarrow&
		\ln \left(\frac{y}{b-y}\right) = ab t + C
\\
	&\Leftrightarrow&
		\ln \left(\frac{1}{b/y-1}\right) = ab t + C
\\
	&\Leftrightarrow&
		\ln (b/y-1) = -ab t - C
\\
	&\Leftrightarrow&
		\frac{b}{y}-1 = e^{-ab t - C}
\end{eqnarray*}
$$

thus we have

\begin{equation}
\label{eq:ode-sol-logistic-fcn}
y(t) = \frac{b}{1+ e^{-abt-C}}
\end{equation}

This equation \eqref{eq:ode-sol-logistic-fcn} is called <span class="define">logistic function</span> or <span class="define">logistic equation</span>
and it comes in lots and lots of fields such as
ecology,
statistics and machine learning (hence AI),
medicine,
chemistry,
physics,
material science,
linguistics,
agriculture,
economics and sociology,
*etc.*
For more information, please refer to [Logistic function Wikipedia Page](https://en.wikipedia.org/wiki/Logistic_function){:target="_blank"}.

There are several things we can observe from this function!

- as long as $0< y(0) < b$, $y(t)$ monotonically increases (because $y'(t)>0$ for $t>0$)
- $\lim_{t\to\infty} y(t) = b$
- $y(t)$ is concave up (*i.e.*, $y$ is a convex function) where $y(t) < b/2$
- $y(t)$ is concave down (*i.e.*, $y$ is a concave function) where $y(t) > b/2$
- $y(t)$ reaches its middle point at $t = - C/ab$, *i.e.*, $y(-C/ab) = b/2$
(thus, if $C>0$, $y(t)$ is always concave down)

The graph below shows $y(t)$ when $a=1$, $b=10$, and $y(0)=1$.
The calculation shows it reaches its middle point at $t \simeq 0.21972$
We can see indeed the graph is *concave up* where $t< 0.21972$
and is *concave down* where $t>0.21972$!

<div class="img-container">
<img src="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/logistic_fcn_01.png">
</div>

#### Interactive animation — watch the solution evolve in real time {#iv-ode}

<div id="ode-viz" style="background:linear-gradient(135deg,#0f172a,#001a0f,#0f172a);border-radius:16px;padding:24px;margin:24px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:16px;">
    <div style="font-size:11px;letter-spacing:.3em;color:#34d399;text-transform:uppercase;margin-bottom:6px;">Ordinary Differential Equations</div>
    <div style="font-size:22px;color:#f1f5f9;font-weight:normal;">Solution Curves in Motion</div>
    <div style="font-size:12px;color:#94a3b8;font-style:italic;margin-top:4px;">The moving dot traces the particle's position — watch how parameters change its fate</div>
  </div>

  <!-- ODE type toggle -->
  <div style="display:flex;gap:8px;margin-bottom:14px;justify-content:center;">
    <button id="ode-btn-linear" onclick="odeSwitch('linear')" style="padding:7px 20px;border-radius:8px;border:2px solid #34d399;background:rgba(52,211,153,.2);color:#34d399;font-size:13px;font-family:Georgia,serif;cursor:pointer;font-weight:bold;">Linear ODE</button>
    <button id="ode-btn-logistic" onclick="odeSwitch('logistic')" style="padding:7px 20px;border-radius:8px;border:2px solid rgba(148,163,184,.2);background:rgba(10,15,30,.5);color:#94a3b8;font-size:13px;font-family:Georgia,serif;cursor:pointer;">Logistic ODE</button>
  </div>

  <canvas id="ode-canvas" style="width:100%;display:block;border-radius:8px;background:#060e0a;"></canvas>

  <!-- Play/Pause -->
  <div style="display:flex;justify-content:center;gap:12px;margin:14px 0 10px;">
    <button id="ode-playbtn" style="padding:8px 28px;border-radius:8px;border:2px solid #34d399;background:rgba(52,211,153,.15);color:#34d399;font-size:14px;font-family:Georgia,serif;cursor:pointer;">▶ Play</button>
    <button onclick="odeReset()" style="padding:8px 20px;border-radius:8px;border:2px solid rgba(148,163,184,.2);background:rgba(10,15,30,.5);color:#94a3b8;font-size:14px;font-family:Georgia,serif;cursor:pointer;">↺ Reset</button>
  </div>

  <!-- Parameter sliders — shown/hidden by mode -->
  <div id="ode-linear-controls">
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
      <span style="color:#94a3b8;font-size:13px;min-width:80px;font-style:italic;" id="ode-lin-a-label">a = −0.50</span>
      <input id="ode-lin-a" type="range" min="-150" max="150" value="-50" style="flex:1;accent-color:#34d399;" oninput="odeLinParamChange()"/>
      <span style="color:#64748b;font-size:11px;min-width:80px;text-align:right;">growth rate a</span>
    </div>
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
      <span style="color:#94a3b8;font-size:13px;min-width:80px;font-style:italic;" id="ode-lin-b-label">b = 1.00</span>
      <input id="ode-lin-b" type="range" min="-200" max="200" value="100" style="flex:1;accent-color:#34d399;" oninput="odeLinParamChange()"/>
      <span style="color:#64748b;font-size:11px;min-width:80px;text-align:right;">constant b</span>
    </div>
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
      <span style="color:#94a3b8;font-size:13px;min-width:80px;font-style:italic;" id="ode-lin-y0-label">y₀ = 3.00</span>
      <input id="ode-lin-y0" type="range" min="-400" max="400" value="300" style="flex:1;accent-color:#fb923c;" oninput="odeLinParamChange()"/>
      <span style="color:#64748b;font-size:11px;min-width:80px;text-align:right;">initial value y₀</span>
    </div>
  </div>
  <div id="ode-logistic-controls" style="display:none;">
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
      <span style="color:#94a3b8;font-size:13px;min-width:80px;font-style:italic;" id="ode-log-a-label">a = 0.50</span>
      <input id="ode-log-a" type="range" min="10" max="200" value="50" style="flex:1;accent-color:#34d399;" oninput="odeLogParamChange()"/>
      <span style="color:#64748b;font-size:11px;min-width:80px;text-align:right;">growth rate a</span>
    </div>
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
      <span style="color:#94a3b8;font-size:13px;min-width:80px;font-style:italic;" id="ode-log-b-label">b = 10.00</span>
      <input id="ode-log-b" type="range" min="100" max="2000" value="1000" style="flex:1;accent-color:#34d399;" oninput="odeLogParamChange()"/>
      <span style="color:#64748b;font-size:11px;min-width:80px;text-align:right;">carrying capacity b</span>
    </div>
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
      <span style="color:#94a3b8;font-size:13px;min-width:80px;font-style:italic;" id="ode-log-y0-label">y₀ = 1.00</span>
      <input id="ode-log-y0" type="range" min="10" max="950" value="100" style="flex:1;accent-color:#fb923c;" oninput="odeLogParamChange()"/>
      <span style="color:#64748b;font-size:11px;min-width:80px;text-align:right;">initial value y₀</span>
    </div>
  </div>

  <div style="text-align:center;font-size:11px;color:#475569;margin-top:10px;" id="ode-formula-display"></div>
</div>

<script>
(function(){
  var odeMode="linear";
  var odeAnimId=null, odePlaying=false;
  var odeT=0, odeTMax=8;
  var OW,OH;
  var oc=document.getElementById("ode-canvas");
  var PAD={top:24,right:28,bottom:40,left:52};

  // params
  var linA=-0.5, linB=1.0, linY0=3.0;
  var logA=0.5,  logB=10.0, logY0=1.0;

  window.odeSwitch=function(mode){
    odeMode=mode; odeReset();
    document.getElementById("ode-linear-controls").style.display=mode==="linear"?"block":"none";
    document.getElementById("ode-logistic-controls").style.display=mode==="logistic"?"block":"none";
    document.getElementById("ode-btn-linear").style.cssText=mode==="linear"
      ?"padding:7px 20px;border-radius:8px;border:2px solid #34d399;background:rgba(52,211,153,.2);color:#34d399;font-size:13px;font-family:Georgia,serif;cursor:pointer;font-weight:bold;"
      :"padding:7px 20px;border-radius:8px;border:2px solid rgba(148,163,184,.2);background:rgba(10,15,30,.5);color:#94a3b8;font-size:13px;font-family:Georgia,serif;cursor:pointer;";
    document.getElementById("ode-btn-logistic").style.cssText=mode==="logistic"
      ?"padding:7px 20px;border-radius:8px;border:2px solid #34d399;background:rgba(52,211,153,.2);color:#34d399;font-size:13px;font-family:Georgia,serif;cursor:pointer;font-weight:bold;"
      :"padding:7px 20px;border-radius:8px;border:2px solid rgba(148,163,184,.2);background:rgba(10,15,30,.5);color:#94a3b8;font-size:13px;font-family:Georgia,serif;cursor:pointer;";
    odeDraw(0);
  };

  window.odeLinParamChange=function(){
    linA=+document.getElementById("ode-lin-a").value/100;
    linB=+document.getElementById("ode-lin-b").value/100;
    linY0=+document.getElementById("ode-lin-y0").value/100;
    document.getElementById("ode-lin-a-label").textContent="a = "+linA.toFixed(2);
    document.getElementById("ode-lin-b-label").textContent="b = "+linB.toFixed(2);
    document.getElementById("ode-lin-y0-label").textContent="y₀ = "+linY0.toFixed(2);
    odeReset();
  };
  window.odeLogParamChange=function(){
    logA=+document.getElementById("ode-log-a").value/100;
    logB=+document.getElementById("ode-log-b").value/100;
    logY0=+document.getElementById("ode-log-y0").value/100;
    document.getElementById("ode-log-a-label").textContent="a = "+logA.toFixed(2);
    document.getElementById("ode-log-b-label").textContent="b = "+logB.toFixed(2);
    document.getElementById("ode-log-y0-label").textContent="y₀ = "+logY0.toFixed(2);
    odeReset();
  };

  // Solution functions
  function linSol(t){ return (linY0+linB/linA)*Math.exp(linA*t) - linB/linA; }
  function logSol(t){
    // y(t) = b / (1 + (b/y0 - 1)*e^{-abt}) = b / (1 + e^{C - abt}), C = ln(b/y0 - 1)
    var C=Math.log(logB/logY0-1);
    return logB/(1+Math.exp(C-logA*logB*t));
  }
  function curSol(t){ return odeMode==="linear"?linSol(t):logSol(t); }

  function odeYRange(){
    var vals=[];
    for(var i=0;i<=100;i++) vals.push(curSol(i/100*odeTMax));
    vals=vals.filter(isFinite);
    var mn=Math.min.apply(null,vals), mx=Math.max.apply(null,vals);
    var pad=(mx-mn)*0.2+0.5;
    return [mn-pad, mx+pad];
  }

  function otoC(t,y,yr){
    var cx=PAD.left+(t/odeTMax)*(OW-PAD.left-PAD.right);
    var cy=OH-PAD.bottom-(y-yr[0])/(yr[1]-yr[0])*(OH-PAD.top-PAD.bottom);
    return [cx,cy];
  }

  window.odeReset=function(){
    odePlaying=false; odeT=0;
    if(odeAnimId){cancelAnimationFrame(odeAnimId);odeAnimId=null;}
    document.getElementById("ode-playbtn").textContent="▶ Play";
    odeDraw(0);
  };

  function odeDraw(t){
    var ctx=oc.getContext("2d");
    ctx.clearRect(0,0,OW,OH);
    var yr=odeYRange();

    // Grid
    ctx.strokeStyle="rgba(52,211,153,.08)"; ctx.lineWidth=1;
    var yStep=Math.pow(10,Math.floor(Math.log10((yr[1]-yr[0])/5)));
    for(var yg=Math.ceil(yr[0]/yStep)*yStep;yg<=yr[1];yg+=yStep){
      var gy=otoC(0,yg,yr)[1];
      ctx.beginPath(); ctx.moveTo(PAD.left,gy); ctx.lineTo(OW-PAD.right,gy); ctx.stroke();
    }
    for(var tg=0;tg<=odeTMax;tg++){
      var gx=otoC(tg,0,yr)[0];
      ctx.beginPath(); ctx.moveTo(gx,PAD.top); ctx.lineTo(gx,OH-PAD.bottom); ctx.stroke();
    }

    // Axes
    ctx.strokeStyle="#1e3a2a"; ctx.lineWidth=1.5;
    var ay=otoC(0,0,yr)[1], ax=otoC(0,yr[0],yr)[0];
    ctx.beginPath(); ctx.moveTo(PAD.left,ay); ctx.lineTo(OW-PAD.right+8,ay); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(ax,OH-PAD.bottom); ctx.lineTo(ax,PAD.top-8); ctx.stroke();

    // Axis labels
    ctx.font="11px Georgia,serif"; ctx.fillStyle="#4b7a5c"; ctx.textAlign="center";
    for(var ti=0;ti<=odeTMax;ti++) ctx.fillText(ti,otoC(ti,yr[0],yr)[0],OH-PAD.bottom+14);
    ctx.textAlign="right";
    var yStep2=Math.pow(10,Math.floor(Math.log10((yr[1]-yr[0])/5)));
    for(var yi=Math.ceil(yr[0]/yStep2)*yStep2;yi<=yr[1];yi+=yStep2){
      ctx.fillText(yi.toFixed(1),PAD.left-5,otoC(0,yi,yr)[1]+4);
    }
    ctx.fillStyle="#4b7a5c"; ctx.font="12px Georgia,serif";
    ctx.textAlign="center"; ctx.fillText("t",OW-PAD.right+16,ay+4);
    ctx.textAlign="left"; ctx.fillText("y",ax+5,PAD.top-10);

    // Equilibrium line for logistic
    if(odeMode==="logistic"){
      var ep=otoC(0,logB,yr)[1];
      ctx.strokeStyle="rgba(251,191,36,.4)"; ctx.lineWidth=1; ctx.setLineDash([5,4]);
      ctx.beginPath(); ctx.moveTo(PAD.left,ep); ctx.lineTo(OW-PAD.right,ep); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle="rgba(251,191,36,.7)"; ctx.font="11px Georgia,serif"; ctx.textAlign="left";
      ctx.fillText("y = b = "+logB.toFixed(1),PAD.left+4,ep-5);
    }

    // Full solution curve (dim trail)
    ctx.strokeStyle="rgba(52,211,153,.3)"; ctx.lineWidth=1.5;
    ctx.beginPath(); var started=false;
    for(var i=0;i<=300;i++){
      var tv=i/300*odeTMax, yv=curSol(tv);
      if(!isFinite(yv)){started=false;continue;}
      var p=otoC(tv,yv,yr);
      started?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]); started=true;
    }
    ctx.stroke();

    // Traced portion (bright)
    ctx.strokeStyle="#34d399"; ctx.lineWidth=2.5;
    ctx.shadowColor="rgba(52,211,153,.5)"; ctx.shadowBlur=6;
    ctx.beginPath(); var tstarted=false;
    for(var i=0;i<=300;i++){
      var tv=i/300*t, yv=curSol(tv);
      if(tv>t) break;
      if(!isFinite(yv)){tstarted=false;continue;}
      var p=otoC(tv,yv,yr);
      tstarted?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]); tstarted=true;
    }
    ctx.stroke(); ctx.shadowBlur=0;

    // Moving dot
    if(t>0){
      var yd=curSol(t);
      if(isFinite(yd)){
        var dp=otoC(t,yd,yr);
        ctx.fillStyle="#fb923c"; ctx.shadowColor="rgba(251,146,60,.9)"; ctx.shadowBlur=14;
        ctx.beginPath(); ctx.arc(dp[0],dp[1],7,0,Math.PI*2); ctx.fill();
        ctx.shadowBlur=0;
        ctx.fillStyle="#f1f5f9"; ctx.font="12px Georgia,serif"; ctx.textAlign="left";
        ctx.fillText("y("+t.toFixed(1)+") = "+yd.toFixed(3),dp[0]+10,dp[1]-6);
      }
    }

    // Formula display
    var fml=odeMode==="linear"
      ? "y′ = "+linA.toFixed(2)+"y + "+linB.toFixed(2)+"  →  y(t) = (y₀ + b/a)eᵃᵗ − b/a"
      : "y′ = "+logA.toFixed(2)+"·y·("+logB.toFixed(2)+"−y)  →  y(t) = b / (1 + e^{−abt−C})";
    document.getElementById("ode-formula-display").textContent=fml;
  }

  // Animation loop
  var odePrevTime=null, odeSpeed=1.2;
  function odeAnimate(ts){
    if(!odePrevTime) odePrevTime=ts;
    var dt=(ts-odePrevTime)/1000*odeSpeed;
    odePrevTime=ts;
    odeT=Math.min(odeT+dt,odeTMax);
    odeDraw(odeT);
    if(odeT<odeTMax) odeAnimId=requestAnimationFrame(odeAnimate);
    else { odePlaying=false; document.getElementById("ode-playbtn").textContent="▶ Play"; }
  }

  document.getElementById("ode-playbtn").addEventListener("click",function(){
    if(odeT>=odeTMax) odeT=0;
    if(odePlaying){
      odePlaying=false; cancelAnimationFrame(odeAnimId); odeAnimId=null;
      this.textContent="▶ Play";
    } else {
      odePlaying=true; odePrevTime=null;
      this.textContent="⏸ Pause";
      odeAnimId=requestAnimationFrame(odeAnimate);
    }
  });

  function odeResize(){
    var cont=document.getElementById("ode-viz");
    OW=cont.clientWidth-48; OH=Math.round(OW*0.45);
    oc.width=OW; oc.height=OH;
    odeDraw(odeT);
  }
  window.addEventListener("resize",odeResize);
  odeResize();
  odeDraw(0);
  document.getElementById("ode-formula-display").textContent=
    "y′ = −0.50·y + 1.00  →  y(t) = (y₀ + b/a)eᵃᵗ − b/a";
})();
</script>

# Exercise Problems

## Differentiation & Integration

<ol>
<li>
<strong>Varsity Tutors Problem</strong>
Evaluate $f'(1)$ when $f(x) = \int_0^x (6t^2 - 3t + 10) dt$.

<p>
<strong>Answer</strong>
$$
13
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Evaluate:

$$
	\int_0^{\infty} \frac{\cos x}{e^x} dx
$$

<p>
<strong>Answer</strong>
$$
\frac{1}{2}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Evaluate:

$$
	\int_0^{\infty} \frac{x}{e^{x^2}} dx
$$

<p>
<strong>Answer</strong>
$$
\frac{1}{2}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Evaluate:

$$
	\int_0^{\infty} \frac{\cos x}{e^{x^2}} dx
$$

<p>
<strong>Answer</strong>
$$
\frac{1}{2}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Find $\frac{dy}{dx}$ if $x^3-x\ln y=ye^x$.
<p>

<strong>Answer</strong>
$$
	\frac{dy}{dx} = \frac{3x^2y-y\ln y - y^2 e^x}{e^x y+x}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Find $dy/dx$:
$$
	y = \tan^{-1} (2x(x+1)^{10}))
$$

<p>
<strong>Answer</strong>
$$
	\frac{dy}{dx} = \frac{2(x+1)^9 (11x+1)}{1+4x^2(x+1)^{20}}
$$
</p>
</li>
<li>
<strong>Varsity Tutors Problem</strong>
What is the derivative of $r=7\sin\theta -6$?

<p>
<strong>Answer</strong>
$$
	\frac{dy}{dx}
	=
		\frac{7\sin 2\theta - 6 \cos\theta}{7\cos 2\theta + 6\sin\theta}
	=
		\frac{14\cos\theta \sin\theta - 6 \cos\theta}{7 - 14\sin^2\theta + 6\sin\theta}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Let $f(x) = \cos(4x)$ on the interval $(0,\pi/2)$.
Find a value for the number(s) that
satisfies the [mean value theorem](#mean-value-theorem)
for this function and interval.

<p>
<strong>Answer</strong>
$$
	\frac{\pi}{4}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Approximate

$$
\int_1^2 x^2 \ln x \, dx
$$

using the midpoint rule with $n=5$. Round your answer to three decimal places.

<p>
<strong>Answer</strong>
$$
	1.064
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Approximate

$$
\int_0^{\pi/4} \tan^2 x \, dx
$$

using the trapezoidal rule with $n=4$. Round your answer to three decimal places.

<p>
<strong>Answer</strong>
$$
	0.227
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Given

$$
	f(x) = \int_0^x \left( \frac{1}{t^2} - 2t + 3\right) dt
$$

what is $f'(6)$?

	<ol>
	<li>
		$\frac{323}{36}$
	</li>
	<li>
		$-\frac{36}{323}$
	</li>
	<li>
		$-\frac{323}{36}$
	</li>
	<li>
		$\frac{36}{323}$
	</li>
	<li>
		None of the above.
	</li>
	</ol>

<p>
<strong>Answer</strong>
3.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Evaluate

$$
	\int_1^\infty \frac{4}{x^5} dx
$$

	<ol>
	<li>
		$-\infty$
	</li>
	<li>
		$0$
	</li>
	<li>
		$1$
	</li>
	<li>
		$-1$
	</li>
	<li>
		$\infty$
	</li>
	</ol>

<p>
<strong>Answer</strong>
3.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
$$
	\int \frac{x-1}{(x-3)(x+4)} dx =
$$

	<ol>
	<li>
		$\frac{5}{7(x+4)} \ln |x| + \frac{2}{7(x-3)} \ln |x| + C$
	</li>
	<li>
		$\frac{1}{7} \ln |x-2| + \frac{1}{7} \ln |x-4| + C$
	</li>
	<li>
		$\frac{5}{7(x+4)} + \frac{2}{7(x+2)} + C$
	</li>
	<li>
		$\frac{2}{7} \ln |x-3| + \frac{5}{7} \ln |x+4| + C$
	</li>
	<li>
		$\frac{(x-3)^2}{7} + \frac{2(x+4)^2}{7} + C$
	</li>
	</ol>

<p>
<strong>Answer</strong>
4.
</p>
</li>
</ol>

## Length & Distance & Velocity & Acceleration & Energy

<ol>
<li>
<strong>Varsity Tutors Problem</strong> Given the velocity function

$$
	v(t) = \int_0^{t^2+2t+1} z^d \sin(z^5)\,dz
$$

where $d$ is real number such that $d\in(0,1)$,
find the acceleration function $a(x)$

<p>
<br>
<span class="emph">Daddy's Solution</span>

We use
<!--
the [chain rule](#chain-rule),
<i>i.e.</i>,
\eqref{eq:chain-rule}
and
-->
the first part of <a href="#fundamental-theorem-of-calculus">FTC</a>
<i>i.e.</i>,
\eqref{eq:fund-theorem-of-calculus-1}
to get

$$
\begin{eqnarray*}
	a(t)
	&=& \frac{d}{dt} v(t) = (2t+2) (t^2+2t+1)^d \sin((t^2+2t+1)^5)
\\
	&=& 2(t+1)^{2d+1} \sin((t+1)^{10})
\end{eqnarray*}
$$

by noting that $t^2+2t+1=(t+1)^2$.

</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Given $\vec{r}(t) = (5t^3, e^{11t}, e^{5t})$.
Calculate $\dfrac{d}{dt} \vec{r}(t)$.

<p>
<strong>Answer</strong>
$$
	\frac{d}{dt} \vec{r}(t) = (15t^2, 11e^{11t}, 5e^{5t})
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Find the equation for the velocity of a particle if the acceleration of the particle is given by

$$
	a(t) = 16 t^2 + 48
$$

and the velocity at time $t=0$ of the particle is $30$.

<p>
<strong>Answer</strong>
$$
	v(t)
	=
	\frac{16}{3} t^3 + 48 t + 30
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
What is the length of the curve $g(x) = x^{3/2}$ over the interval $0\leq x\leq 4$?

<p>
<span class="emph">Daddy's Solution</span>
$$
\begin{eqnarray*}
	\int_{0}^4 \sqrt{1+g'(x)^2}\, dx
	&=&
		\int_{0}^4 \sqrt{1+\frac{9}{4}x} \,dx
\\
	&=&
		\frac{4}{9} \cdot \frac{2}{3} \left.\left(1+\frac{9}{4}x\right)^{3/2}\right|_{x=0}^4
\\
	&=&
		\frac{8}{27} (10\sqrt{10}-1)
\end{eqnarray*}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong> Given $x=t+10$ and $y=2t-9$,
what is the arc length between $0\leq t\leq 4$?

<p>
<strong>Answer</strong>
$$
	4\sqrt{5}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Find the length of the following parametric curve

$$
	x = e^t \cos(t),\;
	y = e^t \sin(t),\;
	0 \leq t \leq 2\pi.
$$

	<ol>
	<li>
		$\sin(t)+\cos(t)$
	</li>
	<li>
		$e^t \cos(t)$
	</li>
	<li>
		$1$
	</li>
	<li>
		$e^{2\pi}$
	</li>
	<li>
		$\sqrt{2} (e^{2\pi} -1)$
	</li>
	</ol>

<p>
<br>
<span class="emph">Daddy's Solution</span>

Note first that the length of the curve can be calculated by

$$
	\int_0^{2\pi} |\vec{v}(t)| dt
$$

by \eqref{eq:vel-int-len}
where $\vec{v}(t)$ is the velocity vector.

Now the displacement (<i>i.e.,</i> location) vector is given by

$$
\vec{d}(t) = (x(t), y(t)) = (e^t \cos t, e^t \sin t)
$$

hence the velocity vector can be calculated as

$$
\vec{v}(t)
=
	\frac{d}{dt} \vec{d}(t)
=
	\left( \frac{d}{t} x(t), \frac{d}{dt} y(t) \right)
=
	(e^t(\cos t - \sin t), e^t (\sin t + \cos t))
$$

and the size of $\vec{v}(t)$ is

$$
\begin{eqnarray*}
|\vec{v}(t)|
	&=&
		e^t \sqrt{(\cos t - \sin t)^2 + (\cos t + \sin t)^2}
\\
	&=&
		e^t \sqrt{(\cos t - \sin t)^2 + (\cos t + \sin t)^2}
\\
	&=&
		\sqrt{2}\, e^t
\end{eqnarray*}
$$

Therefore the length can be calculated as

$$
	\int_0^{2\pi} |\vec{v}(t)| dt = \sqrt{2} \int_0^{2\pi} e^t dt
	= \sqrt{2} \, \left.\left( e^t \right)\right|_{t=0}^{2\pi}
	= \sqrt{2} (e^{2\pi} -1)
$$

</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
The temperature of an oven is increasing at a rate $r(t) = 2 e^{0.5 t}$
degrees Fahrenheit per miniute for $0\leq t\leq 10$ minutes.
The initial temperature of the oven is $T(0) = 75$ degrees Fahrenheit.

What is the temperture of the oven at $t = 5$? Round your answer to the nearest tenth.

	<ol>
	<li>
		119.7
	</li>
	<li>
		212.2
	</li>
	<li>
		239.4
	</li>
	<li>
		323.9
	</li>
	</ol>

<p>
<strong>Answer</strong>
1.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Give the arclength of the graph of the function $f(x) = \frac{1}{2} \ln(\cos 2x)$
on the interval $[0, \frac{\pi}{8}]$.

	<ol>
	<li>
		$\frac{1}{2} \ln\left(1+\sqrt{2}\right)$
	</li>
	<li>
		$1+\sqrt{2}$
	</li>
	<li>
		$\frac{1}{2} + \frac{1}{2} \sqrt{2}$
	</li>
	<li>
		$\frac{1}{2} + \frac{1}{2} \ln{2}$
	</li>
	<li>
		$\ln\left(1+\sqrt{2}\right)$
	</li>
	</ol>

<p>
<strong>Answer</strong>
1.
</p>
</li>

<!--li>
Find the work done by gravity exerting an acceleration of - 10 m/s<sup>2</sup>
for a 10kg block down 5m from its original position with no initial velocity.
Remember that
	<ul>
	<li>
		$F_\mathrm{grav} = \mathrm{mass} \times \mathrm{acceleration}$
	</li>
	<li>
		$W = \int_a^b F(x) \, dx$,
		where $F(x)$ is a force measured in Newtons,
		$W$ is work measured in Joules,
		and $a$ and $b$ are initial and final positions respectively.
	</li>
	</ul>
</li-->
</ol>

## Area & Volume

<ol>
<li>
<strong>Varsity Tutors Problem</strong>
Find the volume of the solid generated by rotating about the $y$-axis the region under the curve $y=\sqrt{x}$,
from $0$ to $4$.

	<ol>
	<li>
		$\frac{64}{3} \pi$
	</li>
	<li>
		$\frac{256}{7} \pi^2$
	</li>
	<li>
		$\frac{128}{5} \pi$
	</li>
	<li>
		$\frac{\pi}{2}$
	</li>
	<li>
		None of the other answers
	</li>
	</ol>

<p>
<strong>Answer</strong>
3.
</p>
</li>
</ol>

## Polar Coordinates

<ol>
<li>
<strong>Varsity Tutors Problem</strong> What is the polar form of $y=-7x^2$?
</li>

<p>
<strong>Answer</strong>
$$
	r(\theta)
	=
	- \frac{\sin\theta}{7\cos^2\theta}
	=
	- \frac{1}{7} \tan\theta \sec\theta
$$
</p>
</ol>

## Taylor Series and Approximation

<ol>
<li>
<strong>Varsity Tutors Problem</strong>
Write out the first three terms of the Taylor series about $a=1$ for the following function.

$$
f(x) = x^2 + e^x
$$

<p>
<strong>Answer</strong>
$$
\begin{eqnarray*}
	f(x) &\simeq& f(1) + f'(1) (x-1) + \frac{1}{2!} f^{\prime\prime}(x) (x-1)^2
\\
	&=&
		1 + e + (2+e)(x-1) + \frac{1}{2} (2+e)(x-1)^2
\end{eqnarray*}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Write the first three terms of the Taylor series for the following function about $x=1$:

$$
f(x) = x^2 + 3x + 2
$$

<p>
<strong>Answer</strong>
$$
\begin{eqnarray*}
	f(x) &\simeq& f(1) + f'(1) (x-1) + \frac{1}{2!} f^{\prime\prime}(x) (x-1)^2
\\
	&=&
		6 + 5(x-1) + (x-1)^2
\end{eqnarray*}
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
For which of the following functions can the Maclaurin series representation be expressed in four or fewer non-zero terms?

	<ol>
	<li>
		$f(x) = x^5/3+2$
	</li>
	<li>
		$f(x) = x^2 + \sqrt{x} + 1$
	</li>
	<li>
		$f(x) = \ln |x + 3|$
	</li>
	<li>
		$f(x) = x + 3 \sin(x)$
	</li>
	</ol>

<p>
<strong>Answer</strong>
1.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Write out the first three terms of the Taylor series about $a=1$ for the following function:

$$
	f(x) = 10x^2 + x
$$


	<ol>
	<li>
		$11+21x+10x^2$
	</li>
	<li>
		$11+21(x-1)+10(x-1)^2$
	</li>
	<li>
		$0 + 0 + 0$
	</li>
	<li>
		$0 + 21(x-1) + 10(x-1)^2$
	</li>
	</ol>

<p>
<strong>Answer</strong>
2.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Write out the first four terms of the Taylor series about $a=1$ for the following function:

$$
	f(x) = x^2+2x+1
$$


	<ol>
	<li>
		$0 + 0 + 0 + 0$
	</li>
	<li>
		$0 + 4 + 4(x-1) + (x-1)^2$
	</li>
	<li>
		$4 + 4(x-1) + (x-1)^2 + 0$
	</li>
	<li>
		$4 + 4(x-1)^2 + (x-1)^3 + 0$
	</li>
	</ol>

<p>
<strong>Answer</strong>
3.
</p>
</li>
</ol>

## Infinite Sequences and Series

<ol>
<li>
<strong>Varsity Tutors Problem</strong>
Calculate the sum of a geometric series with the following values:

$$
n=10,\;
a_1 = 11,\;
r = \frac{2}{20}
$$

rounded to the nearest integer.

<p>
<strong>Answer</strong>
$$
	12
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
For the series $\sum_{n=0}^\infty (-1)^n (\frac{n^n}{8^n})$,
determine if the series converge or diverge.
If it diverges, choose the best reason.

<p>
<strong>Answer</strong>
The series diverges, since $\lim_{n\to\infty} x_n \neq0$.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Determine whether the series converges or diverges:

$$
	\sum_{n=1}^\infty (-1)^{n+1} \frac{n^4}{2n^4+1}
$$

	<ol>
	<li>
		The series may be convergent, divergent, or conditionally convergent.
	</li>
	<li>
		The series is conditionally convergent.
	</li>
	<li>
		The series is (absolutely) convergent.
	</li>
	<li>
		The series is divergent.
	</li>
	</ol>

<p>
<strong>Answer</strong>
4.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Determine if the series converges or diverges. You do not need to find the sum.

$$
	\sum_{n=1}^\infty \frac{1}{n^3+2}
$$

<p>
<strong>Answer</strong>
The series converges.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Find the interval of convergence of $x$ for the series

$$
	\sum_{n=1}^\infty \frac{3^n x^n}{n!}
$$

<p>
<strong>Answer</strong>
$$
(-\infty, \infty)
$$
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Which of the following series does not converge?

	<ol>
	<li>
		$\sum_{i=0}^\infty \frac{n!}{n^2\cos(n)}$
	</li>
	<li>
		$\sum_{i=0}^\infty \frac{n-1}{n^3+1}$
	</li>
	<li>
		$\sum_{i=0}^\infty 0.9999999999999999999^n$
	</li>
	<li>
		$\sum_{i=0}^\infty \frac{(-1)^n}{n}$
	</li>
	<li>
		$\sum_{i=0}^\infty \frac{n^2 \ln(n)}{n!}$
	</li>
	</ol>

<p>
<strong>Answer</strong>
1.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Which of following intervals of convergence cannot exist?

	<ol>
	<li>
		$[2,\infty)$
	</li>
	<li>
		For any $q$, $p$ such that $q\leq p$, the interval $[q,p]$
	</li>
	<li>
		$[2,10000)$
	</li>
	<li>
		For any $\epsilon >0$, the interval $[a-\epsilon,a+\epsilon]$ for some $a\in\reals$
	</li>
	</ol>

<p>
<strong>Answer</strong>
1.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Determine whether

$$
	\sum_{n=1}^\infty (-1)^n \sin (1/n)
$$

converges or diverges, and explain why.

<p>
<strong>Answer</strong>
The series (conditionally) converges,
which can be confirmed by the alternating series test.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Determine whether the following series converges or diverges:

$$
	\sum_{n=0}^\infty (-1)^n \left(\frac{5}{n}\right)
$$

<p>
<strong>Answer</strong>
The series (conditionally) converges,
which can be confirmed by the alternating series test.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
One of the following infinite series converges. Which is it?

	<ol>
	<li>
		$\sum_{k=1}^\infty \frac{1}{k}$
	</li>
	<li>
		$\sum_{k=1}^\infty \frac{\sin(k)}{k^2}$
	</li>
	<li>
		$\sum_{k=1}^\infty (-1)^k \sin(k)$
	</li>
	<li>
		$\sum_{k=2}^\infty \frac{k}{\ln(k)}$
	</li>
	<li>
		None of the others converge.
	</li>
	</ol>

<p>
<strong>Answer</strong>
2.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Determine whether the following series converges or diverges. If it converges, what does it converge to?

$$
	\sum_{n=0}^\infty (2)^{-2n}
$$

	<ol>
	<li>
		$\dfrac{3}{4}$
	</li>
	<li>
		Diverges
	</li>
	<li>
		$1$
	</li>
	<li>
		$\dfrac{4}{3}$
	</li>
	</ol>

<p>
<strong>Answer</strong>
4.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Determine the nature of convergence of the series having the general term:

$$
	\frac{8}{\sqrt{n(n+1)(n+2)}}
$$

	<ol>
	<li>
		$\frac{\pi}{7}$
	</li>
	<li>
		$\frac{\pi}{5}$
	</li>
	<li>
		The series is convergent.
	</li>
	<li>
		$\frac{1}{2}$
	</li>
	<li>
		The series is divergent.
	</li>
	</ol>

<p>
<strong>Answer</strong>
3.
</p>
</li>

<li>
<strong>Varsity Tutors Problem</strong>
Determine if the following series is divergent, convergent or neither.

$$
	\sum_{n=1}^\infty \frac{n!}{2^{n+1}}
$$

	<ol>
	<li>
		Neither
	</li>
	<li>
		Inconclusive
	</li>
	<li>
		Both
	</li>
	<li>
		Divergent
	</li>
	<li>
		Convergent
	</li>
	</ol>

<p>
<strong>Answer</strong>
4.
</p>
</li>
</ol>

## Differential Equations

<ol>
<li>
Problem 4 of <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/chapter6_test.pdf">AP Calculus (BC) Chapter 6 Test</a>
&ndash;
Given the logistic differential equation $\dfrac{dA}{dt} = A\left(20-\dfrac{A}{4}\right)$
where $A(0) = 15$, what is $\lim_{t\to\infty} A(t)$?

<p>
<br>
<span class="emph">Daddy's Solution 1</span>

$$
\begin{eqnarray*}
\frac{dA}{A(20-A/4)} = dt
&\Leftrightarrow&
\left( \frac{1}{A} + \frac{1}{80-A} \right) dA = 20dt
\\
&\Leftrightarrow&
\ln A - \ln (80 - A) = 20 t + C
\\
&\Leftrightarrow&
\ln \left( \frac{A}{80 - A} \right) = 20 t + C
\\
&\Leftrightarrow&
\ln \left( \frac{1}{80/A - 1} \right) = 20 t + C
\\
&\Leftrightarrow&
\ln ( 80/A - 1 ) = -20 t - C
\\
&\Leftrightarrow&
80/A = e^{-20 t - C} + 1
\\
&\Leftrightarrow&
A = \frac{80}{e^{-20 t - C} + 1}
\end{eqnarray*}
$$
</p>

<p>
<span class="emph">Daddy's Solution 2</span>

Let's try to solve using the formula we derived above, <i>i.e.</i>, \eqref{eq:ode-sol-logistic-fcn}!

Because we can rewrite the logistic differential equation as

$$
\frac{dA}{dt} = \frac{1}{4} A(80-A)
$$

and this equation is of the form \eqref{eq:ode-logistic-fcn}
with $a=1/4$ and $b=80$,
the formula \eqref{eq:ode-sol-logistic-fcn} gives

$$
A(t) = \frac{80}{1+ e^{-20t-C}}
$$
</p>

</li>
<li>
Problem 13 of <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/chapter6_test.pdf">AP Calculus (BC) Chapter 6 Test</a>

$$
\frac{dP}{dt} = \frac{k}{656} (650- P) P, \; P(0) = 1
$$

<p>
<br>
<span class="emph">Daddy's Solution</span>
Note that the above equation is of the form \eqref{eq:ode-logistic-fcn}
with $a=k/650$ and $b=650$,
thus
the formula \eqref{eq:ode-sol-logistic-fcn} gives

$$
	P(t)
	= \frac{650}{1+e^{-kt-C}}
	= \frac{650}{1+C' e^{-kt}}
$$

thus of the same form as in the problem!

</p>
</li>
<li>
Problem 5 of <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/chapter6_test.pdf">AP Calculus (BC) Chapter 6 Test</a>
&ndash;
Given the differential equation $\dfrac{dT}{dt} = -\dfrac{1}{4}(T-20)$, $T(0)=100$, then $T(20)$?

<p>
<br>
<span class="emph">Daddy's Solution 1</span>

$$
\begin{eqnarray*}
\frac{dT}{T-20} = -\frac{1}{4} dt
&\Leftrightarrow&
	\ln (T-20) = -\frac{1}{4} t + C
\\
&\Leftrightarrow&
	T(t) = 20 + e^{-\frac{1}{4} t + C}
\end{eqnarray*}
$$

If we use $T(0)=100$, we have

$$
\ln(80) = C
$$

hence

$$
	T(t) = 20 + e^{-\frac{1}{4} t + \ln(80)} = 20 + 80 e^{-\frac{1}{4}t}
$$

</p>

<p>
<span class="emph">Daddy's Solution 2</span>

Let's try to solve using the formula we derived above, <i>i.e.</i>, \eqref{eq:ode-linear-sol}.

Because we can rewrite the differential equation as

$$
\frac{dT}{dt} = - \frac{1}{4} T + 5
$$

and this equation is of the form \eqref{eq:ode-linear}
with $a=-1/4$ and $b=5$,
the formula \eqref{eq:ode-linear-sol} gives

$$
T(t) = (100 - 20) e^{-\frac{1}{4}t} + 20
$$
</p>
</li>
</ol>

# Exercise Problem Collection

- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/chapter6_test.pdf">AP Calculus (BC) Chapter 6 Test</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/707238497-Unit-6-Practice-AP-Calculus-BC.pdf">SCRIBD AP Calculus BC Unit 6 Review</a>

## Area and Volume

- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.1_ca1.pdf">c_11.1_ca1.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.1_ca2.pdf">c_11.1_ca2.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.1_packet.pdf">c_11.1_packet.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.1_solutions.pdf">c_11.1_solutions.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.2_ca1.pdf">c_11.2_ca1.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.2_ca2.pdf">c_11.2_ca2.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.2_packet.pdf">c_11.2_packet.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.2_solutions.pdf">c_11.2_solutions.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.3_ca1.pdf">c_11.3_ca1.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.3_ca2.pdf">c_11.3_ca2.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.3_packet.pdf">c_11.3_packet.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.3_solutions.pdf">c_11.3_solutions.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.4_ca1.pdf">c_11.4_ca1.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.4_ca2.pdf">c_11.4_ca2.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.4_packet.pdf">c_11.4_packet.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11.4_solutions.pdf">c_11.4_solutions.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11_review_solutions.pdf">c_11_review_solutions.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/c_11_review.pdf">c_11_review.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/free_response_on_area_and_volume.pdf">free_response_on_area_and_volume.pdf</a>
- <a target="_blank" href="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/area-and-volume/free_response_answers_on_area_and_volume.pdf">free_response_answers_on_area_and_volume.pdf</a>

# Appendix

## Some trigonometric equivalences

[source](https://en.wikipedia.org/wiki/List_of_trigonometric_identities){:target="_blank"}

### Pythagorean Identities {#pythagorean-identities}

\begin{equation}
\label{eq:tri-pythagorean-identity}
	\sin^2 \theta + \cos^2 \theta = 1
\end{equation}

which implies

\begin{equation}
\label{eq:tri-pythagorean-identity-sin}
	\sin \theta = \pm \sqrt{1-\cos^2\theta}
\end{equation}

\begin{equation}
\label{eq:tri-pythagorean-identity-cos}
	\cos \theta = \pm \sqrt{1-\sin^2\theta}
\end{equation}

\begin{equation}
\label{eq:tri-pythagorean-identity-csc}
	1 + \cot^2\theta = \csc^2 \theta
\end{equation}

\begin{equation}
\label{eq:tri-pythagorean-identity-sec}
	1 + \tan^2\theta = \sec^2 \theta
\end{equation}

\begin{equation}
\label{eq:tri-pythagorean-identity-sec-csc}
	\sec^2\theta + \csc^2\theta = \sec^2 \theta \csc^2\theta
\end{equation}

### Shifts and Periodicity

<figure>
  <div class="img-container">
    <img style="max-width: 60%;" src="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/Unit_Circle_-_shifts.svg.png">
  </div>
  <figcaption>Transformation of coordinates $(a,b)$ when shifting the reflection angle $\alpha$ in increments of $\dfrac{\pi}{4}$</figcaption>
</figure>

|function|period|shift by $\dfrac{\pi}{2}$|shift by $\pi$|shift by multiples of $2\pi$|
|$\sin$|$2\pi$|$\sin\left(\theta \pm \dfrac{\pi}{2}\right) = \pm \cos\theta$|$\sin(\theta+\pi) = - \sin\theta$|$\sin(\theta + k\cdot 2\pi) = + \sin\theta$|
|$\cos$|$2\pi$|$\cos\left(\theta \pm \dfrac{\pi}{2}\right) = \mp \sin\theta$|$\cos(\theta+\pi) = - \cos\theta$|$\cos(\theta + k\cdot 2\pi) = + \cos\theta$|
|$\tan$|$\pi$|$\tan\left(\theta \pm \dfrac{\pi}{2}\right) = - \cot\theta$|$\tan(\theta+\pi) = + \tan\theta$|$\tan(\theta + k\cdot 2\pi) = + \tan\theta$|
|$\csc$|$2\pi$|$\csc\left(\theta \pm \dfrac{\pi}{2}\right) = \pm \sec\theta$|$\csc(\theta+\pi) = - \csc\theta$|$\csc(\theta + k\cdot 2\pi) = + \csc\theta$|
|$\sec$|$2\pi$|$\sec\left(\theta \pm \dfrac{\pi}{2}\right) = \mp \csc\theta$|$\sec(\theta+\pi) = - \sec\theta$|$\sec(\theta + k\cdot 2\pi) = + \sec\theta$|
|$\cot$|$\pi$|$\cot\left(\theta \pm \dfrac{\pi}{2}\right) = - \tan\theta$|$\cot(\theta+\pi) = + \cot\theta$|$\cot(\theta + k\cdot 2\pi) = + \tan\theta$|

|function|shift by $\dfrac{\pi}{4}$|shift by $\dfrac{\pi}{2}$|shift by multiples of $\pi$|
|$\tan$|$\tan\left(\theta \pm \dfrac{\pi}{4}\right) = \dfrac{\tan\theta \pm 1}{1 \mp \tan \theta}$|$\tan\left(\theta + \dfrac{\pi}{2}\right) = - \cot\theta$|$\tan(\theta + k\cdot \pi) = + \tan\theta$|
|$\cot$|$\cot\left(\theta \pm \dfrac{\pi}{4}\right) = \dfrac{\cot\theta \mp 1}{1 \pm \cot \theta}$|$\cot\left(\theta + \dfrac{\pi}{2}\right) = - \tan\theta$|$\cot(\theta + k\cdot \pi) = + \cot\theta$|

### Reflections, Shifts, and Periodicity

<figure>
  <div class="img-container">
    <img style="max-width: 60%;" src="https://sungheeyun-photos-02.github.io/resource/sungheeyun.github.io/posts/2026-03-01-PST - ap calculus bc problems/Unit_Circle_-_symmetry.svg.png">
  </div>
  <figcaption>Transformation of coordinates $(a,b)$ when shifting the reflection angle $\alpha$ in increments of $\dfrac{\pi}{4}$</figcaption>
</figure>

|$\theta$ reflected in $\alpha=0$|$\theta$ reflected in $\alpha=\dfrac{\pi}{4}$|$\theta$ reflected in $\alpha=\dfrac{\pi}{2}$|$\theta$ reflected in $\alpha=\dfrac{3\pi}{4}$|$\theta$ reflected in $\alpha=\pi$|
|$\sin(-\theta) = - \sin\theta$|$\sin\left(\dfrac{\pi}{2}-\theta\right) = + \cos\theta$|$\sin(\pi-\theta) = + \sin\theta$|$\sin\left(\dfrac{3\pi}{2}-\theta\right) = - \cos\theta$|$\sin(2\pi-\theta) = \sin(-\theta) = - \sin \theta$|
|$\cos(-\theta) = + \cos\theta$|$\cos\left(\dfrac{\pi}{2}-\theta\right) = + \sin\theta$|$\cos(\pi-\theta) = - \cos\theta$|$\cos\left(\dfrac{3\pi}{2}-\theta\right) = - \sin\theta$|$\cos(2\pi-\theta) = \cos(-\theta) = + \cos \theta$|
|$\tan(-\theta) = - \tan\theta$|$\tan\left(\dfrac{\pi}{2}-\theta\right) = + \cot\theta$|$\tan(\pi-\theta) = - \tan\theta$|$\tan\left(\dfrac{3\pi}{2}-\theta\right) = + \cot\theta$|$\tan(2\pi-\theta) = \tan(-\theta) = - \tan \theta$|
|$\csc(-\theta) = - \csc\theta$|$\csc\left(\dfrac{\pi}{2}-\theta\right) = + \sec\theta$|$\csc(\pi-\theta) = + \csc\theta$|$\csc\left(\dfrac{3\pi}{2}-\theta\right) = - \sec\theta$|$\csc(2\pi-\theta) = \csc(-\theta) = - \csc \theta$|
|$\sec(-\theta) = + \sec\theta$|$\sec\left(\dfrac{\pi}{2}-\theta\right) = + \csc\theta$|$\sec(\pi-\theta) = - \sec\theta$|$\sec\left(\dfrac{3\pi}{2}-\theta\right) = - \csc\theta$|$\sec(2\pi-\theta) = \sec(-\theta) = + \sec \theta$|
|$\cot(-\theta) = - \cot\theta$|$\cot\left(\dfrac{\pi}{2}-\theta\right) = + \tan\theta$|$\cot(\pi-\theta) = - \cot\theta$|$\cot\left(\dfrac{3\pi}{2}-\theta\right) = + \tan\theta$|$\cot(2\pi-\theta) = \cot(-\theta) = - \cot \theta$|

### Sum and Difference Identities

$$
\begin{eqnarray}
\label{eq:tri-sin-sum-identity}
	\sin(\alpha + \beta)
		&=&
			\sin\alpha \cos\beta + \cos\alpha \sin\beta
\\
\label{eq:tri-cos-sum-identity}
	\cos(\alpha + \beta)
		&=&
			\cos\alpha \cos\beta - \sin\alpha \sin\beta
\end{eqnarray}
$$

hence

$$
\begin{eqnarray}
	\sin(\alpha - \beta)
		&=&
			\sin\alpha \cos\beta - \cos\alpha \sin\beta
\\
	\cos(\alpha - \beta)
		&=&
			\cos\alpha \cos\beta + \sin\alpha \sin\beta
\end{eqnarray}
$$

which imply

$$
\begin{eqnarray}
	\tan(\alpha + \beta)
		&=&
			\frac{\tan\alpha + \tan \beta}{1 - \tan\alpha\tan\beta}
\\
	\tan(\alpha - \beta)
		&=&
			\frac{\tan\alpha - \tan \beta}{1 + \tan\alpha\tan\beta}
\end{eqnarray}
$$

### Multiple-angle Formulas

We can derive all the formula here essentially using these two formulas; \eqref{eq:tri-sin-sum-identity} and \eqref{eq:tri-cos-sum-identity}!

<ul>
<li>
\eqref{eq:tri-sin-sum-identity}
implies

\begin{equation}
\label{eq:tri-sin-2-theta}
	\sin(2\theta) = 2\sin\theta \cos\theta
\end{equation}
</li>

<li>
\eqref{eq:tri-cos-sum-identity}
(together with \eqref{eq:tri-pythagorean-identity})
implies

\begin{equation}
\label{eq:tri-cos-2-theta}
	\cos(2\theta) = \cos^2 \theta - \sin^2\theta = 1 - 2\sin^2\theta = 2\cos^2\theta - 1
\end{equation}
</li>

<li>
\eqref{eq:tri-sin-2-theta} and \eqref{eq:tri-cos-2-theta} imply

\begin{equation}
\label{eq:tri-tan-2-theta}
	\tan(2\theta) = \frac{2\tan\theta}{1 - \tan^2\theta}
\end{equation}
</li>

<li>
\eqref{eq:tri-sin-sum-identity}, \eqref{eq:tri-sin-2-theta}, and \eqref{eq:tri-cos-2-theta}
(together with \eqref{eq:tri-pythagorean-identity})
imply

\begin{equation}
\label{eq:tri-sin-3-theta}
	\sin(3\theta) = 3\sin\theta - 4\sin^3\theta
\end{equation}

because

$$
\begin{eqnarray*}
	\sin(3\theta)
		&=&
			\sin(\theta + 2\theta)
		=
			\sin\theta \cos(2\theta) + \cos\theta \sin(2\theta)
\\
		&=&
			\sin\theta (1-2\sin^2\theta) + 2\cos^2\theta \sin\theta
\\
		&=&
			\sin\theta (1-2\sin^2\theta) + 2(1-\sin^2\theta) \sin\theta
\\
		&=&
			3\sin\theta - 4\sin^3\theta
\end{eqnarray*}
$$
</li>

<li>
\eqref{eq:tri-sin-3-theta} implies

\begin{equation}
\label{eq:tri-cos-3-theta}
	\cos(3\theta) = -3\cos\theta + 4\cos^3\theta
\end{equation}

because

$$
\begin{eqnarray*}
	\cos(3\theta)
		&=&
			- \sin \left(3\theta + \frac{3\pi}{2} \right)
		=
			- \sin \left(3\left(\theta + \frac{\pi}{2}\right) \right)
\\
		&=&
			- 3\sin\left(\theta + \frac{\pi}{2}\right) + 4\sin^3\left(\theta + \frac{\pi}{2}\right)
\\
		&=&
			- 3\cos\theta + 4\cos^3\theta
\end{eqnarray*}
$$
</li>

<li>
Now
\eqref{eq:tri-sin-3-theta},
\eqref{eq:tri-cos-3-theta},
and
\eqref{eq:tri-pythagorean-identity-sec}
imply

\begin{equation}
\label{eq:tri-tan-3-theta}
	\tan(3\theta)
		=
			\frac{3\tan\theta - \tan^3\theta}{1 - 3\tan^2\theta}
\end{equation}

because

$$
\begin{eqnarray*}
	\tan(3\theta)
		&=&
			\frac{3\sin\theta - 4\sin^3\theta}{-3\cos\theta + 4\cos^3\theta}
		=
			\frac{3\tan\theta \sec^2\theta - 4\tan^3\theta}{-3\sec^2\theta + 4}
\\
		&=&
			\frac{3\tan\theta (1+\tan^2\theta) - 4\tan^3\theta}{-3(1+\tan^2\theta) + 4}
\\
		&=&
			\frac{3\tan\theta - \tan^3\theta}{1 - 3\tan^2\theta}
\end{eqnarray*}
$$
</li>
</ul>

### Half-angle formulas

Similarly, all the formulas here can be (easily) derived from what we have studied so far.

<ul>
<li>
	\eqref{eq:tri-cos-2-theta} readily implies

\begin{equation}
\label{eq:tri-sin-half-theta}
	\sin^2\frac{\theta}{2} = \frac{1-\cos\theta}{2}
\end{equation}
</li>

<li>
	Also, \eqref{eq:tri-cos-2-theta} readily implies
\begin{equation}
\label{eq:tri-cos-half-theta}
	\cos^2\frac{\theta}{2} = \frac{1+\cos\theta}{2}
\end{equation}
</li>

<li>
Now
\eqref{eq:tri-sin-2-theta},
\eqref{eq:tri-sin-half-theta},
and
\eqref{eq:tri-cos-half-theta},
imply

\begin{equation}
\label{eq:tri-tan-half-theta}
	\tan\frac{\theta}{2}
		=
			\frac{1-\cos\theta}{\sin\theta}
		=
			\frac{\sin\theta}{1+\cos\theta}
		=
			\frac{\tan\theta}{1+\sec\theta}
\end{equation}

because

$$
\begin{eqnarray*}
	\tan\frac{\theta}{2}
		&=&
			\frac{\sin(\theta/2)}{\cos(\theta/2)}
\\
		&=&
			\frac{2\sin^2(\theta/2)}{2\sin(\theta/2)\cos(\theta/2)}
				=
					\frac{1-\cos\theta}{\sin\theta}
\\
		&=&
			\frac{2\cos(\theta/2)\sin(\theta/2)}{2\cos^2(\theta/2)}
				=
					\frac{\sin\theta}{1+\cos\theta}
					=
						\frac{\tan\theta}{\sec\theta+1}
\end{eqnarray*}
$$
</li>
</ul>

### Power-reduction formulas

Once again, everything here can be deduced from what we've already studied!<sup><a href="#footnote03" id="ref03">3</a></sup>

<span class="emph">So in a sense, essentially, no addition knowledge adds up here, but it's always good to know and get accustomed to these patterns,
*e.g.*, to get good grades on AP Calculus BC tests! &#x2605;^^&#x2605;</span>

<ul>
<li>
\eqref{eq:tri-cos-2-theta}
implies

\begin{equation}
\label{eq:tri-sin-squared}
	\sin^2\theta = \frac{1 - \cos(2\theta)}{2}
\end{equation}

\begin{equation}
\label{eq:tri-cos-squared}
	\cos^2\theta = \frac{1 + \cos(2\theta)}{2}
\end{equation}
</li>

<li>
\eqref{eq:tri-sin-3-theta}
and
\eqref{eq:tri-cos-3-theta}
respectively
imply

\begin{equation}
\label{eq:tri-sin-cubed}
	\sin^3\theta = \frac{3\sin\theta - \sin(3\theta)}{4}
\end{equation}

\begin{equation}
\label{eq:tri-cos-cubed}
	\cos^3\theta = \frac{3\cos\theta + \cos(3\theta)}{4}
\end{equation}
</li>

<li>
Some (tedious) calculations also lead to

\begin{equation}
\label{eq:tri-sin-power-4}
	\sin^4\theta = \frac{3 - 4\cos(2\theta) + \cos(4\theta)}{8}
\end{equation}

\begin{equation}
\label{eq:tri-cos-power-4}
	\cos^4\theta = \frac{3 + 4\cos(2\theta) + \cos(4\theta)}{8}
\end{equation}

\begin{equation}
\label{eq:tri-sin-power-5}
	\sin^5\theta = \frac{10\sin\theta - 5\sin(3\theta) + \sin(5\theta)}{16}
\end{equation}

\begin{equation}
\label{eq:tri-cos-power-5}
	\cos^5\theta = \frac{10\cos\theta + 5\cos(3\theta) + \cos(5\theta)}{16}
\end{equation}
</li>
</ul>

## Interactive Visualization Tools

### Power Functions {#iv-deri-power-functions}

Drag the slider to sweep $p$ continuously from $-3$ to $3$.
The tool draws $f(x) = x^p$ and its derivative $f'(x) = p\,x^{p-1}$ live for $x \ge 0$,
so you can watch the geometry morph in real time — and see exactly how the derivative rule works across every case
&ndash;
integer, fractional, negative, and zero exponents!

<div id="power-viz" style="background:linear-gradient(135deg,#0f172a,#1a1200,#0f172a);border-radius:16px;padding:24px;margin:24px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:16px;">
    <div style="font-size:11px;letter-spacing:.3em;color:#fbbf24;text-transform:uppercase;margin-bottom:6px;">Power Functions</div>
    <div style="font-size:22px;color:#f1f5f9;font-weight:normal;">f(x) = x<sup>p</sup> &nbsp;and&nbsp; f'(x) = p·x<sup>p−1</sup></div>
    <div style="font-size:12px;color:#94a3b8;font-style:italic;margin-top:4px;">Drag p and watch f and f' morph continuously — notice what happens at p = 0, 1, 2 …</div>
  </div>

  <canvas id="power-canvas" style="width:100%;display:block;border-radius:8px;background:#080910;"></canvas>

  <!-- formula display -->
  <div id="power-formula" style="background:rgba(26,18,0,.8);border:1px solid rgba(251,191,36,.3);border-radius:10px;padding:12px 20px;margin:14px 0;text-align:center;font-size:15px;color:#f1f5f9;box-shadow:0 0 16px rgba(251,191,36,.1);"></div>

  <!-- p slider -->
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
    <span style="color:#fbbf24;font-size:13px;min-width:56px;font-style:italic;text-align:right;" id="power-plabel">p = 1</span>
    <input id="power-pslider" type="range" min="-300" max="300" value="100" step="1" style="flex:1;accent-color:#fbbf24;" />
    <span style="color:#64748b;font-size:11px;min-width:56px;">p ∈ [-3, 3]</span>
  </div>

  <!-- x0 hover: show tangent -->
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
    <span style="color:#94a3b8;font-size:13px;min-width:56px;font-style:italic;text-align:right;" id="power-x0label">x₀ = 1.0</span>
    <input id="power-x0slider" type="range" min="1" max="300" value="100" step="1" style="flex:1;accent-color:#a78bfa;" />
    <span style="color:#64748b;font-size:11px;min-width:56px;">move x₀</span>
  </div>

  <!-- stats row -->
  <div style="display:flex;gap:10px;" id="power-stats"></div>

  <div style="text-align:center;margin-top:12px;font-size:11px;color:#475569;">
    Gold = f(x) = x<sup>p</sup> &nbsp;|&nbsp; Teal = f'(x) = p·x<sup>p−1</sup> &nbsp;|&nbsp; Purple dot = (x₀, f(x₀)) with tangent line
  </div>
</div>

<script>
(function(){
  var curP = 1.0;
  var curX0 = 1.0;
  var PAD = {top:28, right:28, bottom:44, left:52};
  var W, H;
  var canvas = document.getElementById("power-canvas");

  // fixed window: x in [0, 3], y auto-scaled per p
  var XMIN = 0, XMAX = 3;

  function safeF(x, p){
    if(x < 0) return NaN;
    if(x === 0){
      if(p > 0) return 0;
      if(p === 0) return 1;
      return NaN; // x^negative at 0 = ±∞
    }
    return Math.pow(x, p);
  }

  function safeDf(x, p){
    if(x <= 0) return NaN;
    if(p === 0) return 0;
    return p * Math.pow(x, p - 1);
  }

  function getYBounds(p){
    // sample f and f' over [0.01, 3] and pick nice bounds
    var vals = [], steps = 300;
    for(var i=1; i<=steps; i++){
      var x = 0.01 + (i/steps)*(XMAX - 0.01);
      var fv = safeF(x, p);
      var dfv = safeDf(x, p);
      if(isFinite(fv))  vals.push(fv);
      if(isFinite(dfv)) vals.push(dfv);
    }
    if(vals.length === 0) return {ymin:-2, ymax:2};
    var lo = Math.min.apply(null, vals);
    var hi = Math.max.apply(null, vals);
    // clamp extremes
    lo = Math.max(lo, -6);
    hi = Math.min(hi,  6);
    // add margin
    var margin = (hi - lo) * 0.12 || 0.5;
    return {ymin: lo - margin, ymax: hi + margin};
  }

  function toC(x, y, ymin, ymax){
    var cx = PAD.left + (x - XMIN)/(XMAX - XMIN)*(W - PAD.left - PAD.right);
    var cy = H - PAD.bottom - (y - ymin)/(ymax - ymin)*(H - PAD.top - PAD.bottom);
    return [cx, cy];
  }

  function pLabel(p){
    // nice fraction display for common values
    var fracs = {"-3":"-3", "-2.5":"-5/2", "-2":"-2", "-1.5":"-3/2", "-1":"-1",
                 "-0.5":"-1/2", "0":"0", "0.5":"1/2", "1":"1", "1.5":"3/2",
                 "2":"2", "2.5":"5/2", "3":"3"};
    var key = p.toFixed(1);
    return fracs[key] || p.toFixed(2);
  }

  function draw(){
    var ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, W, H);
    var p = curP;
    var x0 = curX0;
    var bounds = getYBounds(p);
    var ymin = bounds.ymin, ymax = bounds.ymax;
    var steps = 600;

    // ── grid ──
    ctx.strokeStyle = "rgba(148,163,184,.1)"; ctx.lineWidth = 1;
    for(var y = Math.ceil(ymin); y <= Math.floor(ymax); y++){
      if(Math.abs(y) > 10) continue;
      var gy = toC(0, y, ymin, ymax)[1];
      ctx.beginPath(); ctx.moveTo(PAD.left, gy); ctx.lineTo(W - PAD.right, gy); ctx.stroke();
    }
    // y=0 line
    var y0line = toC(0, 0, ymin, ymax)[1];
    ctx.strokeStyle = "rgba(148,163,184,.35)"; ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(PAD.left, y0line); ctx.lineTo(W-PAD.right, y0line); ctx.stroke();

    // ── axes ──
    ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
    // x-axis at y=0 (or bottom if y=0 out of range)
    var axY = Math.max(PAD.top, Math.min(H - PAD.bottom, toC(0,0,ymin,ymax)[1]));
    ctx.beginPath(); ctx.moveTo(PAD.left, axY); ctx.lineTo(W-PAD.right+10, axY); ctx.stroke();
    // y-axis at x=0 (left edge since domain is x>=0)
    ctx.beginPath(); ctx.moveTo(PAD.left, PAD.top-8); ctx.lineTo(PAD.left, H-PAD.bottom); ctx.stroke();
    // arrowhead x
    ctx.fillStyle="#475569";
    ctx.beginPath(); ctx.moveTo(W-PAD.right+10,axY-4); ctx.lineTo(W-PAD.right+17,axY); ctx.lineTo(W-PAD.right+10,axY+4); ctx.fill();
    // arrowhead y
    ctx.beginPath(); ctx.moveTo(PAD.left-4,PAD.top-8); ctx.lineTo(PAD.left,PAD.top-15); ctx.lineTo(PAD.left+4,PAD.top-8); ctx.fill();

    // tick labels
    ctx.font = "11px Georgia,serif"; ctx.fillStyle = "#64748b";
    ctx.textAlign = "center";
    for(var xi = 0; xi <= 3; xi++){
      var tp = toC(xi, 0, ymin, ymax);
      ctx.fillText(xi, tp[0], axY + 14);
    }
    ctx.textAlign = "right";
    for(var yi = Math.ceil(ymin); yi <= Math.floor(ymax); yi++){
      if(yi === 0 || Math.abs(yi) > 6) continue;
      var tp2 = toC(0, yi, ymin, ymax);
      if(tp2[1] < PAD.top || tp2[1] > H-PAD.bottom+5) continue;
      ctx.fillText(yi, PAD.left - 6, tp2[1] + 4);
    }
    ctx.textAlign = "center";
    ctx.fillStyle="#475569"; ctx.font="12px Georgia,serif";
    ctx.fillText("x", W-PAD.right+21, axY+4);
    ctx.textAlign="left"; ctx.fillText("y", PAD.left+5, PAD.top-16);

    // ── draw f(x) = x^p (gold) ──
    ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 2.5;
    ctx.shadowColor = "rgba(251,191,36,.4)"; ctx.shadowBlur = 6;
    ctx.beginPath();
    var fStarted = false;
    for(var i = 0; i <= steps; i++){
      var xv = XMIN + (i/steps)*(XMAX - XMIN);
      if(xv < 1e-4 && p < 0){ fStarted=false; continue; } // avoid singularity
      var yv = safeF(xv, p);
      if(!isFinite(yv) || yv < ymin - 5 || yv > ymax + 5){ fStarted=false; continue; }
      var cp = toC(xv, yv, ymin, ymax);
      fStarted ? ctx.lineTo(cp[0], cp[1]) : ctx.moveTo(cp[0], cp[1]);
      fStarted = true;
    }
    ctx.stroke(); ctx.shadowBlur = 0;

    // ── draw f'(x) = p x^{p-1} (teal) ──
    ctx.strokeStyle = "#2dd4bf"; ctx.lineWidth = 2;
    ctx.shadowColor = "rgba(45,212,191,.35)"; ctx.shadowBlur = 5;
    ctx.beginPath();
    var dStarted = false;
    for(var i = 0; i <= steps; i++){
      var xv = 0.01 + (i/steps)*(XMAX - 0.01); // start slightly above 0
      var yv = safeDf(xv, p);
      if(!isFinite(yv) || yv < ymin - 5 || yv > ymax + 5){ dStarted=false; continue; }
      var cp = toC(xv, yv, ymin, ymax);
      dStarted ? ctx.lineTo(cp[0], cp[1]) : ctx.moveTo(cp[0], cp[1]);
      dStarted = true;
    }
    ctx.stroke(); ctx.shadowBlur = 0;

    // ── tangent line at x0 ──
    var fx0  = safeF(x0, p);
    var dfx0 = safeDf(x0, p);
    if(isFinite(fx0) && isFinite(dfx0)){
      // tangent: y = fx0 + dfx0*(x - x0)
      var txL = toC(XMIN, fx0 + dfx0*(XMIN - x0), ymin, ymax);
      var txR = toC(XMAX, fx0 + dfx0*(XMAX - x0), ymin, ymax);
      ctx.strokeStyle = "rgba(167,139,250,.7)"; ctx.lineWidth = 1.5;
      ctx.setLineDash([5, 4]);
      ctx.beginPath(); ctx.moveTo(txL[0], txL[1]); ctx.lineTo(txR[0], txR[1]); ctx.stroke();
      ctx.setLineDash([]);

      // dot on f at x0
      var dotP = toC(x0, fx0, ymin, ymax);
      ctx.fillStyle = "#a78bfa";
      ctx.shadowColor = "rgba(167,139,250,.8)"; ctx.shadowBlur = 12;
      ctx.beginPath(); ctx.arc(dotP[0], dotP[1], 6, 0, Math.PI*2); ctx.fill();
      ctx.shadowBlur = 0;

      // dot on f' at x0
      var dotDP = toC(x0, dfx0, ymin, ymax);
      ctx.fillStyle = "#2dd4bf";
      ctx.beginPath(); ctx.arc(dotDP[0], dotDP[1], 4, 0, Math.PI*2); ctx.fill();

      // vertical dashed line at x0
      var vtop = toC(x0, ymax, ymin, ymax);
      var vbot = toC(x0, ymin, ymin, ymax);
      ctx.strokeStyle = "rgba(167,139,250,.3)"; ctx.lineWidth = 1;
      ctx.setLineDash([3, 4]);
      ctx.beginPath(); ctx.moveTo(dotP[0], vtop[1]); ctx.lineTo(dotP[0], vbot[1]); ctx.stroke();
      ctx.setLineDash([]);
    }

    // ── curve labels ──
    var labelX = 2.2;
    var fLabel = safeF(labelX, p);
    if(isFinite(fLabel) && fLabel >= ymin && fLabel <= ymax){
      var lp = toC(labelX, fLabel, ymin, ymax);
      ctx.fillStyle = "#fbbf24"; ctx.font = "italic 13px Georgia,serif"; ctx.textAlign = "left";
      ctx.fillText("f(x)=x^"+pLabel(p), lp[0]+6, lp[1]-8);
    }
    var dfLabel = safeDf(labelX, p);
    if(isFinite(dfLabel) && dfLabel >= ymin && dfLabel <= ymax){
      var dlp = toC(labelX, dfLabel, ymin, ymax);
      ctx.fillStyle = "#2dd4bf"; ctx.font = "italic 13px Georgia,serif"; ctx.textAlign = "left";
      ctx.fillText("f'(x)="+pLabel(p)+"x^"+(p-1).toFixed(p%1===0?0:2), dlp[0]+6, dlp[1]+14);
    }

    // ── formula box ──
    var fx0v  = safeF(x0, p);
    var dfx0v = safeDf(x0, p);
    var pStr  = pLabel(p);
    var pm1Str = pLabel(p-1);
    document.getElementById("power-formula").innerHTML =
      '<span style="color:#fbbf24;">f(x) = x<sup>'+pStr+'</sup></span>'
      +'&nbsp;&nbsp;&nbsp;&nbsp;'
      +'<span style="color:#2dd4bf;">f\'(x) = '+pStr+' · x<sup>'+pm1Str+'</sup></span>'
      +(isFinite(fx0v) && isFinite(dfx0v)
        ? '&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a78bfa;">at x₀='+x0.toFixed(2)+': &nbsp;f='+fx0v.toFixed(4)+', &nbsp;f\'='+dfx0v.toFixed(4)+'</span>'
        : '');

    // ── stats ──
    document.getElementById("power-stats").innerHTML=[
      ["p", pStr, "#fbbf24"],
      ["f(x₀) = x₀^p", isFinite(fx0v)?fx0v.toFixed(4):"∞", "#fbbf24"],
      ["f'(x₀) = slope", isFinite(dfx0v)?dfx0v.toFixed(4):"∞", "#2dd4bf"]
    ].map(function(d){
      return '<div style="flex:1;background:rgba(10,8,0,.7);border:1px solid rgba(148,163,184,.1);border-radius:10px;padding:10px;text-align:center;">'
        +'<div style="font-size:10px;color:#64748b;letter-spacing:.1em;text-transform:uppercase;margin-bottom:3px;">'+d[0]+'</div>'
        +'<div style="font-size:16px;color:'+d[2]+';font-family:monospace;">'+d[1]+'</div></div>';
    }).join("");
  }

  function resize(){
    var cont = document.getElementById("power-viz");
    W = cont.clientWidth - 48;
    H = Math.round(W * 0.52);
    canvas.width = W; canvas.height = H;
    draw();
  }

  // p slider — mapped linearly from -3 to 3, step 0.01
  document.getElementById("power-pslider").addEventListener("input", function(){
    curP = +this.value / 100;
    document.getElementById("power-plabel").textContent = "p = " + pLabel(curP);
    draw();
  });

  // x0 slider — mapped from 0.05 to 3
  document.getElementById("power-x0slider").addEventListener("input", function(){
    curX0 = 0.05 + (+this.value - 1) / 299 * (3 - 0.05);
    document.getElementById("power-x0label").textContent = "x₀ = " + curX0.toFixed(2);
    draw();
  });

  window.addEventListener("resize", resize);
  resize();
})();
</script>

### Antiderivative of Power Functions {#iv-anti-deri-power-functions}

This is the *flip side* of the previous tool — now we look at $f(x) = \dfrac{x^p}{p}$ and its derivative $f'(x) = x^{p-1}$.
This is exactly the **power rule for integration**!

$$
	\int x^{p-1}\,dx = \frac{x^p}{p} + C
		\quad
			\mbox{for }p \neq 0
$$

Drag $p$ and notice the beautiful symmetry with the previous tool
&ndash;
the derivative of $\displaystyle \frac{x^p}{p}$ is always $x^{p-1}$ — watch how $f'(x) = x^{p-1}$ changes shape as $p$ sweeps,
and observe the **special cases** carefully!

- What happens at $p=1$?
- What happens at $p=0.5$?
- What happens at $p=0$ (the famous exception where $\displaystyle \int x^{-1} dx = \ln x$, not a power function!)?

<div id="antipow-viz" style="background:linear-gradient(135deg,#0f172a,#00121a,#0f172a);border-radius:16px;padding:24px;margin:24px 0;font-family:Georgia,serif;">
  <div style="text-align:center;margin-bottom:16px;">
    <div style="font-size:11px;letter-spacing:.3em;color:#38bdf8;text-transform:uppercase;margin-bottom:6px;">Antiderivative of Power Functions</div>
    <div style="font-size:22px;color:#f1f5f9;font-weight:normal;">f(x) = x<sup>p</sup>/p &nbsp;and&nbsp; f'(x) = x<sup>p−1</sup></div>
    <div style="font-size:12px;color:#94a3b8;font-style:italic;margin-top:4px;">The power rule for integration: ∫x<sup>p−1</sup>dx = x<sup>p</sup>/p + C &nbsp;(p ≠ 0)</div>
  </div>

  <canvas id="antipow-canvas" style="width:100%;display:block;border-radius:8px;background:#050a10;"></canvas>

  <!-- formula display -->
  <div id="antipow-formula" style="background:rgba(0,18,26,.8);border:1px solid rgba(56,189,248,.3);border-radius:10px;padding:12px 20px;margin:14px 0;text-align:center;font-size:15px;color:#f1f5f9;box-shadow:0 0 16px rgba(56,189,248,.1);"></div>

  <!-- p slider -->
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
    <span style="color:#38bdf8;font-size:13px;min-width:56px;font-style:italic;text-align:right;" id="antipow-plabel">p = 1</span>
    <input id="antipow-pslider" type="range" min="-500" max="500" value="100" step="1" style="flex:1;accent-color:#38bdf8;" />
    <span onclick="document.getElementById('antipow-pslider').value=0;document.getElementById('antipow-plabel').textContent='p = 0';document.getElementById('antipow-pslider').dispatchEvent(new Event('input'));" style="color:#64748b;font-size:11px;min-width:56px;cursor:pointer;user-select:none;">p ∈ [−5, 5] ↺</span>
  </div>

  <!-- x0 slider -->
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
    <span style="color:#94a3b8;font-size:13px;min-width:56px;font-style:italic;text-align:right;" id="antipow-x0label">x₀ = 1.0</span>
    <input id="antipow-x0slider" type="range" min="1" max="300" value="100" step="1" style="flex:1;accent-color:#a78bfa;" />
    <span style="color:#64748b;font-size:11px;min-width:56px;">move x₀</span>
  </div>

  <!-- stats row -->
  <div style="display:flex;gap:10px;" id="antipow-stats"></div>

  <div style="text-align:center;margin-top:12px;font-size:11px;color:#475569;">
    Sky blue = f(x) = x<sup>p</sup>/p &nbsp;|&nbsp; Teal = f'(x) = x<sup>p−1</sup> &nbsp;|&nbsp; Purple dot = (x₀, f(x₀)) with tangent
  </div>
</div>

<script>
(function(){
  var curP = 1.0;
  var curX0 = 1.0;
  var PAD = {top:28, right:28, bottom:44, left:52};
  var W, H;
  var canvas = document.getElementById("antipow-canvas");
  var XMIN = 0, XMAX = 3;

  function safeF(x, p){
    // f(x) = x^p / p  — but at p=0 the antiderivative is ln(x), not x^0/0
    if(Math.abs(p) < 0.005) return x > 0 ? Math.log(x) : NaN;
    if(x < 0) return NaN;
    if(x === 0){
      if(p > 0) return 0;
      return NaN; // singularity
    }
    return Math.pow(x, p) / p;
  }

  function safeDf(x, p){
    // f'(x) = x^{p-1}
    if(x <= 0) return NaN;
    if(p - 1 === 0) return 1; // x^0 = 1
    return Math.pow(x, p - 1);
  }

  function getYBounds(p){
    var vals = [], steps = 300;
    for(var i=1; i<=steps; i++){
      var x = 0.01 + (i/steps)*(XMAX - 0.01);
      var fv  = safeF(x, p);
      var dfv = safeDf(x, p);
      if(isFinite(fv))  vals.push(fv);
      if(isFinite(dfv)) vals.push(dfv);
    }
    if(vals.length === 0) return {ymin:-2, ymax:2};
    var lo = Math.max(Math.min.apply(null, vals), -6);
    var hi = Math.min(Math.max.apply(null, vals),  6);
    var margin = (hi - lo) * 0.12 || 0.5;
    return {ymin: lo - margin, ymax: hi + margin};
  }

  function toC(x, y, ymin, ymax){
    var cx = PAD.left + (x - XMIN)/(XMAX - XMIN)*(W - PAD.left - PAD.right);
    var cy = H - PAD.bottom - (y - ymin)/(ymax - ymin)*(H - PAD.top - PAD.bottom);
    return [cx, cy];
  }

  function pFmt(v){
    var fracs = {"-3":"-3","-2.5":"-5/2","-2":"-2","-1.5":"-3/2","-1":"-1",
                 "-0.5":"-1/2","0":"0","0.5":"1/2","1":"1","1.5":"3/2",
                 "2":"2","2.5":"5/2","3":"3"};
    return fracs[v.toFixed(1)] || v.toFixed(2);
  }

  function draw(){
    var ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, W, H);
    var p = curP, x0 = curX0;
    var b = getYBounds(p);
    var ymin = b.ymin, ymax = b.ymax;
    var steps = 600;

    // grid
    ctx.strokeStyle = "rgba(148,163,184,.1)"; ctx.lineWidth = 1;
    for(var y = Math.ceil(ymin); y <= Math.floor(ymax); y++){
      if(Math.abs(y) > 10) continue;
      var gy = toC(0, y, ymin, ymax)[1];
      ctx.beginPath(); ctx.moveTo(PAD.left, gy); ctx.lineTo(W-PAD.right, gy); ctx.stroke();
    }
    // y=0 baseline
    ctx.strokeStyle = "rgba(148,163,184,.35)"; ctx.lineWidth = 1.5;
    var y0line = toC(0, 0, ymin, ymax)[1];
    ctx.beginPath(); ctx.moveTo(PAD.left, y0line); ctx.lineTo(W-PAD.right, y0line); ctx.stroke();

    // axes
    ctx.strokeStyle = "#1e3a4a"; ctx.lineWidth = 1.5;
    var axY = Math.max(PAD.top, Math.min(H-PAD.bottom, toC(0,0,ymin,ymax)[1]));
    ctx.beginPath(); ctx.moveTo(PAD.left, axY); ctx.lineTo(W-PAD.right+10, axY); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(PAD.left, PAD.top-8); ctx.lineTo(PAD.left, H-PAD.bottom); ctx.stroke();
    ctx.fillStyle="#1e3a4a";
    ctx.beginPath(); ctx.moveTo(W-PAD.right+10,axY-4); ctx.lineTo(W-PAD.right+17,axY); ctx.lineTo(W-PAD.right+10,axY+4); ctx.fill();
    ctx.beginPath(); ctx.moveTo(PAD.left-4,PAD.top-8); ctx.lineTo(PAD.left,PAD.top-15); ctx.lineTo(PAD.left+4,PAD.top-8); ctx.fill();

    // tick labels
    ctx.font="11px Georgia,serif"; ctx.fillStyle="#64748b";
    ctx.textAlign="center";
    for(var xi=0; xi<=3; xi++){
      var tp = toC(xi, 0, ymin, ymax);
      ctx.fillText(xi, tp[0], axY+14);
    }
    ctx.textAlign="right";
    for(var yi=Math.ceil(ymin); yi<=Math.floor(ymax); yi++){
      if(yi===0 || Math.abs(yi)>6) continue;
      var tp2 = toC(0, yi, ymin, ymax);
      if(tp2[1]<PAD.top || tp2[1]>H-PAD.bottom+5) continue;
      ctx.fillText(yi, PAD.left-6, tp2[1]+4);
    }
    ctx.textAlign="center"; ctx.fillStyle="#1e3a4a"; ctx.font="12px Georgia,serif";
    ctx.fillText("x", W-PAD.right+21, axY+4);
    ctx.textAlign="left"; ctx.fillText("y", PAD.left+5, PAD.top-16);

    // p=0 note (no longer an error — we now plot ln(x) as the correct antiderivative)
    if(Math.abs(p) < 0.005){
      ctx.fillStyle="rgba(251,191,36,.10)";
      ctx.fillRect(PAD.left, PAD.top, W-PAD.left-PAD.right, H-PAD.top-PAD.bottom);
    }

    // f(x) = x^p / p  (sky blue)
    ctx.strokeStyle="#38bdf8"; ctx.lineWidth=2.5;
    ctx.shadowColor="rgba(56,189,248,.4)"; ctx.shadowBlur=6;
    ctx.beginPath();
    var fStarted=false;
    for(var i=0; i<=steps; i++){
      var xv = XMIN + (i/steps)*(XMAX-XMIN);
      if(xv < 1e-4 && p < 0){ fStarted=false; continue; }
      var yv = safeF(xv, p);
      if(!isFinite(yv)||yv<ymin-5||yv>ymax+5){ fStarted=false; continue; }
      var cp = toC(xv, yv, ymin, ymax);
      fStarted?ctx.lineTo(cp[0],cp[1]):ctx.moveTo(cp[0],cp[1]); fStarted=true;
    }
    ctx.stroke(); ctx.shadowBlur=0;

    // f'(x) = x^{p-1}  (teal)
    ctx.strokeStyle="#2dd4bf"; ctx.lineWidth=2;
    ctx.shadowColor="rgba(45,212,191,.35)"; ctx.shadowBlur=5;
    ctx.beginPath();
    var dStarted=false;
    for(var i=0; i<=steps; i++){
      var xv = 0.01 + (i/steps)*(XMAX-0.01);
      var yv = safeDf(xv, p);
      if(!isFinite(yv)||yv<ymin-5||yv>ymax+5){ dStarted=false; continue; }
      var cp = toC(xv, yv, ymin, ymax);
      dStarted?ctx.lineTo(cp[0],cp[1]):ctx.moveTo(cp[0],cp[1]); dStarted=true;
    }
    ctx.stroke(); ctx.shadowBlur=0;

    // tangent at x0
    var fx0  = safeF(x0, p);
    var dfx0 = safeDf(x0, p);
    if(isFinite(fx0) && isFinite(dfx0)){
      var txL = toC(XMIN, fx0+dfx0*(XMIN-x0), ymin, ymax);
      var txR = toC(XMAX, fx0+dfx0*(XMAX-x0), ymin, ymax);
      ctx.strokeStyle="rgba(167,139,250,.7)"; ctx.lineWidth=1.5;
      ctx.setLineDash([5,4]);
      ctx.beginPath(); ctx.moveTo(txL[0],txL[1]); ctx.lineTo(txR[0],txR[1]); ctx.stroke();
      ctx.setLineDash([]);
      // dot on f
      var dp = toC(x0, fx0, ymin, ymax);
      ctx.fillStyle="#a78bfa"; ctx.shadowColor="rgba(167,139,250,.8)"; ctx.shadowBlur=12;
      ctx.beginPath(); ctx.arc(dp[0],dp[1],6,0,Math.PI*2); ctx.fill();
      ctx.shadowBlur=0;
      // dot on f'
      var ddp = toC(x0, dfx0, ymin, ymax);
      ctx.fillStyle="#2dd4bf";
      ctx.beginPath(); ctx.arc(ddp[0],ddp[1],4,0,Math.PI*2); ctx.fill();
      // vertical dashed
      ctx.strokeStyle="rgba(167,139,250,.25)"; ctx.lineWidth=1; ctx.setLineDash([3,4]);
      var vt=toC(x0,ymax,ymin,ymax), vb=toC(x0,ymin,ymin,ymax);
      ctx.beginPath(); ctx.moveTo(dp[0],vt[1]); ctx.lineTo(dp[0],vb[1]); ctx.stroke();
      ctx.setLineDash([]);
    }

    // curve labels
    var lx = 2.1;
    var fy  = safeF(lx, p);
    var dfy = safeDf(lx, p);
    if(isFinite(fy) && fy>=ymin && fy<=ymax){
      var lp2=toC(lx,fy,ymin,ymax);
      ctx.fillStyle="#38bdf8"; ctx.font="italic 13px Georgia,serif"; ctx.textAlign="left";
      var fLabel = Math.abs(p)<0.005 ? "f(x)=ln(x)" : "f(x)=x^"+pFmt(p)+"/"+pFmt(p);
      ctx.fillText(fLabel, lp2[0]+6, lp2[1]-8);
    }
    if(isFinite(dfy) && dfy>=ymin && dfy<=ymax){
      var dlp=toC(lx,dfy,ymin,ymax);
      ctx.fillStyle="#2dd4bf"; ctx.font="italic 13px Georgia,serif"; ctx.textAlign="left";
      ctx.fillText("f'(x)=x^"+pFmt(p-1), dlp[0]+6, dlp[1]+14);
    }

    // formula box
    var pS=pFmt(p), pm1S=pFmt(p-1);
    var isP0 = Math.abs(p) < 0.005;
    var noteP1 = (Math.abs(p-1)<0.01) ? ' &nbsp;<span style="color:#fbbf24;font-size:11px;">← f(x)=x, f\'(x)=1 ✓</span>' : '';
    var noteP2 = (Math.abs(p-2)<0.01) ? ' &nbsp;<span style="color:#fbbf24;font-size:11px;">← f(x)=x²/2, f\'(x)=x ✓</span>' : '';
    var noteP0 = isP0 ? ' &nbsp;<span style="color:#fbbf24;font-size:11px;">← the famous exception: ∫x⁻¹dx = ln(x)+C ✓</span>' : '';
    document.getElementById("antipow-formula").innerHTML=
      (isP0
        ? '<span style="color:#38bdf8;">f(x) = ln(x)</span>'
          +'&nbsp;&nbsp;&nbsp;&nbsp;'
          +'<span style="color:#2dd4bf;">f\'(x) = x<sup>-1</sup> = 1/x</span>'
        : '<span style="color:#38bdf8;">f(x) = x<sup>'+pS+'</sup> / '+pS+'</span>'
          +'&nbsp;&nbsp;&nbsp;&nbsp;'
          +'<span style="color:#2dd4bf;">f\'(x) = x<sup>'+pm1S+'</sup></span>'
      )
      +noteP0+noteP1+noteP2
      +(isFinite(fx0)&&isFinite(dfx0)
        ?'&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a78bfa;">at x₀='+x0.toFixed(2)+': &nbsp;f='+fx0.toFixed(4)+', &nbsp;f\'='+dfx0.toFixed(4)+'</span>'
        :'');

    // stats
    document.getElementById("antipow-stats").innerHTML=[
      ["p", isP0 ? "0  (ln)" : pS, "#38bdf8"],
      [isP0 ? "f(x₀) = ln(x₀)" : "f(x₀) = x₀ᵖ/p", isFinite(fx0)?fx0.toFixed(4):"∞", "#38bdf8"],
      ["f'(x₀) = x₀ᵖ⁻¹", isFinite(dfx0)?dfx0.toFixed(4):"∞", "#2dd4bf"]
    ].map(function(d){
      return '<div style="flex:1;background:rgba(0,8,15,.7);border:1px solid rgba(148,163,184,.1);border-radius:10px;padding:10px;text-align:center;">'
        +'<div style="font-size:10px;color:#64748b;letter-spacing:.1em;text-transform:uppercase;margin-bottom:3px;">'+d[0]+'</div>'
        +'<div style="font-size:16px;color:'+d[2]+';font-family:monospace;">'+d[1]+'</div></div>';
    }).join("");
  }

  function resize(){
    var cont=document.getElementById("antipow-viz");
    W=cont.clientWidth-48; H=Math.round(W*0.52);
    canvas.width=W; canvas.height=H; draw();
  }

  document.getElementById("antipow-pslider").addEventListener("input",function(){
    curP=+this.value/100;
    document.getElementById("antipow-plabel").textContent="p = "+pFmt(curP);
    draw();
  });
  document.getElementById("antipow-x0slider").addEventListener("input",function(){
    curX0=0.01+(+this.value-1)/299*(3-0.01);
    document.getElementById("antipow-x0label").textContent="x₀ = "+curX0.toFixed(2);
    draw();
  });

  window.addEventListener("resize",resize);
  resize();
})();
</script>

---

<ol>
<li id="footnote01">
For example,
for every trigonometric differentiation formulas can be derived from this single formula!

$$
	\frac{d}{dx} \sin x = \cos x
$$

*i.e.*, we can even derive the derivative of the cosine function from this
by

$$
	\frac{d}{dx} \cos x
		=
			\frac{d}{dx} \sin \left(x + \frac{\pi}{2}\right)
		=
			\cos \left(x + \frac{\pi}{2}\right) \frac{d}{dx} \left(x + \frac{\pi}{2}\right)
		=
			- \sin x
$$

where the chain rule \eqref{eq:chain-rule} is used!
	&nbsp;<a href="#ref01">↩</a></li>
<li id="footnote02">
	The notion of a sequence can be generalized to an indexed family, defined as a function from an arbitrary index set.
	&nbsp;<a href="#ref02">↩</a></li>
<li id="footnote03">
	Indeed, we do <span style="color: red; font-weight: bold;">NOT</span> even need both \eqref{eq:tri-sin-sum-identity} and \eqref{eq:tri-cos-sum-identity},
	because one readily implies the other.
	For example,
	assume that we only knew \eqref{eq:tri-sin-sum-identity}.
	Then we can derive
	$$
	\begin{eqnarray*}
		\cos(\alpha + \beta)
			&=&
				\sin\left(\alpha + \beta + \frac{\pi}{2}\right)
					=
						\sin\left(\alpha + \left(\beta + \frac{\pi}{2}\right) \right)
	\\
			&=&
				\sin\alpha \cos\left(\beta + \frac{\pi}{2}\right)
				+
				\cos\alpha \sin\left(\beta + \frac{\pi}{2}\right)
	\\
			&=&
				- \sin\alpha \sin\beta
				+ \cos\alpha \cos\beta
	\end{eqnarray*}
	$$

	hence, \eqref{eq:tri-sin-sum-identity} immeidately implies \eqref{eq:tri-cos-sum-identity}!
	And (of course) vice versa!

	So in a sense, we can derive <span style="color: red; font-weight: bold;">every single trigonometric identity existing in the whole universe</span>
	from these two; the very basic <a href="#pythagorean-identities">Pythagorean identity</a> \eqref{eq:tri-pythagorean-identity}
	and the two-term summuation formula for $\sin$ \eqref{eq:tri-sin-sum-identity}!
	They are

	$$
		\sin^2\theta + \cos^2\theta = 1
	$$
	and
	$$
		\sin(\alpha + \beta)
			=
				\sin\alpha \cos\beta + \cos\alpha \cos\beta
	$$

	&nbsp;<a href="#ref03">↩</a></li>
</ol>
