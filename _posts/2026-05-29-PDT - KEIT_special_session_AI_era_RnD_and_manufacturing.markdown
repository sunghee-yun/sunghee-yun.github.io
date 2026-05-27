---
date: Tue May 26 23:51:03 KST 2026
last_modified_at: Thu May 28 00:52:25 KST 2026
permalink: /ai/keit-special-session-rnd-manufacturing-ai-era
layout: single
title: "KEIT Special Session &ndash; The Future of Industrial Technology R&D and Manufacturing Innovation in the AI Era"
categories:
 - blog
 - AI
 - R&D
 - Manufacturing
tags:
 - AI
 - R&D
 - manufacturing
 - semiconductors
 - panel
 - KEIT
toc: true
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
---

posted: {{ page.date| date: "%d-%b-%Y" }}
&amp;
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

<!--script src="{{ '/assets/js/toc-collapse.js' | relative_url }}"></script-->

**Share on**
[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url={{ site.url }}{{ site.baseurl }}{{ page.url }})
| [Instagram](https://www.instagram.com/)
| [Twitter (X)](https://x.com/intent/tweet?text={{ site.url }}{{ site.baseurl }}{{ page.url }})
| [Facebook](https://www.facebook.com/sharer/sharer.php?u={{ site.url }}{{ site.baseurl }}{{ page.url }})

{% assign cognitive_catalysis = site.posts | where: "permalink", "/ai/new-ai-human-collaboration-model" | first %}
{% assign ai_reason = site.posts | where: "permalink", "/ai/reason" | first %}
{% assign ai_safety = site.posts | where: "permalink", "/ai/future/" | first %}
{% assign data_essay = site.posts | where: "permalink", "/ai/data" | first %}
{% assign salzburg_report = site.posts | where: "permalink", "/ai/salzburg-report-case-of-ai" | first %}
{% assign journey = site.posts | where: "permalink", "/contributions/my-entrepreneurial-journey/en" | first %}

- Prep notes for the KEIT round table — tight, spoken talking points.
- Full answers are for the questions directed to me and the **Common** ones; the rest are one-line hand-offs.
- Blog frameworks ([cognitive catalysis](https://sungheeyun.github.io/ai/new-ai-human-collaboration-model), [data-as-moat](https://sungheeyun.github.io/ai/data), [AI-isn't-safe-or-dangerous](https://sungheeyun.github.io/ai/future/), the connector's mindset) are woven in only where they sharpen the point.
- My one-line anchor across every answer: across Samsung, Amazon, Gauss Labs, and now Erudio Bio, the work has been the same — AI and convex optimization finding patterns and optimal points in complex systems; only the target changed, from silicon chips to life.
- I speak as a *connector* who has actually stood on the fab floor, not a single-domain specialist.

## 1. Special Session Configuration

- **Theme**: The Future of Industrial Technology R&D and Manufacturing Innovation in the AI Era
- **Format**: Round table
- **Time / Venue**: May 29, 2026 (Fri) 13:30–14:45 KST, Korea University (Centennial Memorial Samsung Hall — Global Conference Hall, B1)
- **Structure**: Intro (10 min, Prof. Songhee Kang, TU Korea) → Discussion (60 min) → Wrap-up (10 min)

## 2. Speaker Lineup

- **Chair**: Prof. Keun Lee (Seoul National University / Chung-Ang University)
- **UK**: Prof. Tim Minshall (University of Cambridge)
- **China**: Prof. Yuan Zhou (Tsinghua University)
- **Japan**: Prof. Kazuyuki Motohashi (University of Tokyo)
- **USA / Korea**: Sunghee Yun (Erudio Bio; former CTO of Gauss Labs, VP of SK Hynix)

## 3. Discussion Questions & Draft Answers

### [Topic 1] How is AI changing R&D planning and evaluation methodologies?

**Q1. As AI automates trend analysis and roadmapping, in which areas is human expert-based Technology Foresight still indispensable?** *(Minshall, Motohashi)*

> Defer to Minshall and Motohashi. One line if useful: AI extrapolates the consensus from existing literature well; deciding *which* problems are worth solving and sensing the non-incremental break stays human.

**Q2. How are AI-based project screening and evaluation tools being implemented in Japan and the UK, and how do they coexist with expert panels?** *(Minshall, Motohashi)*

> Defer to Minshall and Motohashi. One line: the workable pattern is "AI triages, humans decide" — the model surfaces novelty/overlap/feasibility, the panel spends judgment on the contested middle.

**Q3. To what extent does China utilize AI in national core technology planning, and is this widening the speed gap with other countries?** *(Yuan Zhou)*

> Defer to Yuan Zhou.

**Q4. How has the method of setting R&D goals and conducting interim check-ups changed in industrial fields after the introduction of AI?** *(Sunghee Yun)*

Planning moved from a periodic, document-driven ritual to a continuous, data-driven loop — the unit of planning used to be the quarter; now it's the dataset.

- **Live forecasts, not fixed gates** — the model re-estimates achievable yield/cost as evidence arrives; the human still owns whether to accept the re-baseline.
- **Continuous check-ups** — anomaly detection flags drift in near real time, so the review is "do we pivot or kill?" not "what happened?"
- **The real prize is a faster, confident *no*** — kill weak branches before they burn fab time or wet-lab cost. KPI shifts from "milestones hit" to "good decisions per unit of experimental budget."
- **Caution:** don't let the metric become the target — we kept a human "reality gate" before any big commitment. The lesson I carried from Samsung's iOpt platform still holds: a model is only good if the field engineers actually use it; an interim check-up the team doesn't trust changes nothing.

### [Topic 2] AI Integration and Industrial R&D Productivity (Manufacturing / Materials)

**Q1. To what extent is AI replacing or compressing the "wet lab" cycle in semiconductors, batteries, and bio, and how is this reshaping the workforce structure?** *(Sunghee Yun)*

Compressing, not replacing — the experiment stays the source of truth; AI just slashes how many you need to run.

- **Materials/batteries** — surrogate models + Bayesian optimization screen thousands of candidates in silico; "self-driving labs" turn the design-make-test loop from weeks to days.
- **Semiconductors** — gains are in design/process (AI-assisted EDA, virtual metrology); you still can't pattern-match your way out of a physical defect.
- **Bio is hardest** — structure prediction jumped, but noisy causal loops keep the wet lab central. At Erudio Bio we're porting semiconductor design-automation thinking straight into preclinical drug design (we call it bioTCAD) — same optimization lens, target changed from silicon to molecules.
- **Workforce migrates, not just shrinks** — routine "pair of hands" roles fall; demand jumps for *connectors / hybrids* who speak both domain science and data, plus new roles in data curation and "keeping the model honest." The scarce person is the translator between bench and model. The reskilling is the real challenge.

**Q2. Will the generalization of AI Foundation Models allow SMEs to have R&D capabilities similar to large corporations, or will the data gap widen?** *(Common)*

Both — foundation models equalize the *generic* layer and divide the *proprietary* layer.

- **Equalizer** — base models are commoditizing fast (only a few players build them); any SME can rent frontier capability by API. Model mastery is now table stakes, not an edge.
- **But the moat moved to data + domain knowledge** — raw industrial data is worthless until someone who knows the process makes it usable (RAG over curated data). Incumbents sit on decades of it.
- **Net** — models raise the floor for everyone, raise the ceiling fastest for whoever owns unique data. The real lever for SMEs is shared data infrastructure and compute access, not more models.

**Q3. What is the role of government support in how UK industries integrate AI?** *(Minshall)*

> Defer to Minshall (Catapult, Made Smarter). One line: the useful role is de-risking *adoption* for mid-size manufacturers — shared testbeds and skills — not subsidizing frontier models.

**Q4. In Japan's "Monozukuri" innovation model, how does AI address the "codification of artisan knowledge"?** *(Motohashi)*

> Defer to Motohashi. One line: sensors + ML can capture the master's "feel" as data, but it encodes the correlation, not the judgment of when the rule *doesn't* apply — that's the part worth protecting.

**Q5. What is the true source of competitiveness in industrial AI: algorithms, data, or process context knowledge?** *(Common)*

Almost the opposite of the consumer-AI headlines: **process knowledge first, data second, algorithms a distant third.**

- **Algorithms commoditized** — published and re-implemented within months; no durable moat there.
- **Data is necessary but overrated alone** — mostly noise until someone who understands the process knows what it means.
- **Process knowledge is the moat** — knowing which variables matter and which prediction is safe to act on is what makes a fab engineer trust the output. At Gauss Labs the hard part was never the algorithm. This is the throughline of my whole career: the same AI-plus-convex-optimization lens worked at Samsung (wafer yield), Amazon (recommendations), and now Erudio Bio (drug design) — what travels across domains is the optimization-and-pattern lens *plus* domain knowledge, never the model alone. One-liner: competitiveness lives at the intersection of proprietary data and the domain knowledge to use it — the algorithm is the easy 10%.

### [Topic 3] The Future of Manufacturing: What will factories look like in 2035?

**Q1. How will the job structure of the Korean industrial workforce be reorganized as AI transformation accelerates? What policies are the UK, Japan, and China testing?** *(Minshall, Motohashi, Yuan Zhou)*

> Mostly for the panelists on comparative policy. If pulled in on Korea: expect polarization — fewer mid-skill operators, more at the high-skill and flexible-services ends — so the priority is mid-career reskilling. The deeper risk is *concentration* of AI's gains — the question my Salzburg working group framed as "Technology, Growth, and Inequality" — an institutional question more than a technical one.

**Q2. As AI automates design and optimization, how should "technology accumulation" be redefined? Does AI's ability to compress/transfer experience change the "catch-up" structure for latecomer countries?** *(Common)*

Yes, but not as simple leapfrogging — AI changes what's easy to copy and what stays hard.

- **Codifiable experience now compresses into models** — accumulates faster, depreciates faster.
- **Helps catch-up in the middle of the curve** — latecomers skip some slow manual tuning.
- **But the moat deepens at the frontier** — running a leading-edge fab at high yield is tacit knowledge AI can't capture, because the data only exists inside the few firms already there.
- **Net for Korea:** defend the frontier; don't assume the lead is durable.

**Q3. What are the most persistent challenges with "autonomous factories"? Pros and cons of China's many "Dark Factories"?** *(Common, Yuan Zhou)*

The hard part isn't robotics — it's the long tail of exceptions.

- **The 5% problem** — automating the normal case is routine; the rare fault/out-of-spec part is where the cost and risk live. Every exception that needs a human breaks the lights-out promise.
- **Brittle to change** — great at high-volume stable products, slow and human-intensive to retool.
- **Skill hollowing + single-point-of-failure** — remove humans and you lose the intuition that caught subtle problems.
- **China's dark factories (defer detail to Yuan Zhou):** pros — speed, scale, consistency, lower cost via domestic volume; cons — capital lock-in, inflexibility, dependence on continuous demand.

**Q4. Why does "demonstration success" in AI factory R&D often fail to lead to "technology diffusion"? What can be learned from the UK's KTN/Catapult experience?** *(Minshall)*

> Defer to Minshall on KTN/Catapult. One line from industry: pilots succeed in curated conditions with the original team; diffusion fails because the receiving plant lacks the data infrastructure and domain-fluent people to sustain it — and because the demo was never built for the field engineer who has to live with it. A technology is only good if the people on the floor actually use it. Fund integration and skills, not more demos.

### [Topic 4] The Future of Global AI R&D Cooperation

**Q1. How should international R&D portfolios be redesigned amidst the US-China tech decoupling?** *(Common)*

Geopolitics is now a first-class design constraint, not an afterthought.

- **Segment by sensitivity** — keep pre-competitive science (climate, health, fundamental) open; handle strategic/dual-use work (advanced compute, leading-edge chips) jurisdiction-aware.
- **Design for resilience, not just efficiency** — "friend-shoring" / "+1" on critical capabilities so one rupture can't sever a whole program.
- **Korea's spot** — between largest ally and largest market; deepen trusted-partner alliances where stakes are high, keep open science alive everywhere still permitted.
- **Hedge** — assume weights, tooling, and data may face controls; don't be single-sourced on any one country's chips, cloud, or talent.

**Q2. What lessons does the UK's re-participation in Horizon Europe provide regarding "tech alliance-based R&D"?** *(Minshall)*

> Defer to Minshall. One line: collaboration networks are costly to exit and slow to rebuild — political ruptures tax research with a lag, so insulate science from short-term politics where possible.

**Q3. What efforts is China making to form a global AI ecosystem? Where are the possibilities for cooperation with Korea?** *(Yuan Zhou)*

> Defer to Yuan Zhou. If asked on Korea: realistic openings are standards, open science, and shared application domains (manufacturing, materials) — not sensitive frontier compute.

**Q4. As AI regulations tighten, regulatory arbitrage is occurring. What kind of regulatory framework do AI startups want?** *(Sunghee Yun)*

Not *no* regulation — **predictable, proportionate, portable** regulation. Uncertainty costs a startup far more than rules do.

- **Predictable** — a clear rule I can build against beats "we'll decide later." Ambiguity is the killer.
- **Proportionate** — regulate by the application's risk, not by the word "AI"; SME sandboxes and reduced compliance matter, because heavy uniform compliance is itself a moat protecting incumbents.
- **Portable** — fragmentation across EU/US-states/federal is pure deadweight cost; we want mutual recognition and common standards.
- **On arbitrage:** it's a symptom, not a strategy — adds overhead, signals fragility to investors. Regulators should compete on clarity and sandbox quality, not a race to the bottom.

### [Topic 5] The Emergence of Non-Human Innovators and R&D Governance

**Q1. How should patent attribution, research-fund settlement, and performance evaluation for AI-generated inventions be designed?** *(Minshall, Motohashi, Yuan Zhou)*

> Mostly for the panelists. One line: attribute to the human directing the AI (with disclosure of AI's role) — current law requires a human inventor, and that's also the honest description. The harder question is fair settlement when AI sharply lowers the human effort.

**Q2. How do you assess the risks open-source AI models (LLaMA, DeepSeek, etc.) pose to corporate security and national strategic technology protection?** *(Yuan Zhou, Sunghee Yun)*

Net positive for industry — but separate two risks people blur.

- **Open models can be the *safer* corporate choice** — run on-premise, keep sensitive process data inside the firewall instead of sending it to a third-party API.
- **The real inbound risk is people** — staff pasting proprietary data into external chatbots; fix with a sanctioned internal model.
- **Where I'd push the field:** privacy-preserving computation — homomorphic encryption lets firms collaborate and share model insight *without ever exposing raw proprietary data*. This is the bet behind my Silicon Valley AI Nexus work and my CryptoLab engagement; for industrial AI it reframes "open vs. closed" into "shareable computation, protected data."
- **Model-side / supply-chain risk** — poisoning, backdoors, provenance ambiguity. "Open" ≠ "vetted"; evaluate and fine-tune on trusted data before strategic use.
- **National angle (defer geopolitics to Yuan Zhou):** open weights make export controls leaky — protect the real chokepoints (leading-edge compute, fab know-how, unique data), not architectures already in the open.

**Q3. How should R&D audit systems be strengthened to combat AI-driven research misconduct (data manipulation, false results)?** *(Common)*

Shift audit from trusting outputs to verifying provenance — AI now makes fakes look perfectly plausible.

- **Provenance over inspection** — auditable trail from result back to raw instrument data; if you can't reconstruct it, treat it as unverified.
- **Fight AI with AI, carefully** — detection scales but it's an arms race; a "clean" score isn't proof.
- **Reproducibility is the real audit** — tie funding milestones to reproducible artifacts (data + code), not claimed results.
- **Fix incentives** — reward honest negative results and pre-registration, or you're treating the symptom.

**Q4. With the shift toward software/data/cloud costs in R&D, is "labor-cost-centered" budget support still valid? What should government budgets prioritize?** *(Common)*

No — labor-centric budgeting is outdated and actively distorts modern R&D.

- **Cost base moved** — compute, cloud, data, and software now dominate, not headcount.
- **Labor-only grants distort** — teams over-hire and under-invest in compute/data, and can't burst when needed.
- **Prioritize:** (1) shared compute infrastructure for SMEs/universities; (2) data as infrastructure — curated, shared domain datasets; (3) flexible cost categories so cloud/data/software are first-class fundable items.
- **Caveat:** the scarce *hybrid* talent is still the bottleneck — fund compute, data, *and* people as the three real inputs.

---

*Full answers are first-person drafts for my own questions and the "Common" ones; ">" items are quick hand-offs. (Note: source doc lists me as "Seong-hee Yoon" in Topic 5 Q2 — worth fixing.)*
