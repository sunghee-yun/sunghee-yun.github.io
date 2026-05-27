---
date: Tue May 26 23:51:03 KST 2026
last_modified_at: Wed May 27 23:51:03 KST 2026
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
toc: false
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

{% assign multi_agent = site.posts | where: "permalink", "/multi-agent-ai-biz-landscape" | first %}
{% assign data_essay = site.posts | where: "permalink", "/ai/data" | first %}
{% assign ai_safety = site.posts | where: "permalink", "/ai/future/" | first %}
{% assign hallucination = site.posts | where: "permalink", "/ai/halluciation-not-a-bug" | first %}

These are my preparation notes for the KEIT Special Session round table. I drafted full answers for the questions directed to me and for the ones marked **Common**; for the rest I kept brief notes so I can hand off cleanly to the relevant panelist or chime in with a single supporting point.

## 1. Special Session Configuration

- **Theme**: The Future of Industrial Technology R&D and Manufacturing Innovation in the AI Era
- **Format**: Round table
- **Time / Venue**: May 29, 2026 (Fri) 13:30–14:45, Korea University (Centennial Memorial Samsung Hall — Global Conference Hall, B1)
- **Structure**: Introduction of topics (10 min, Prof. Songhee Kang, TU Korea) → Discussion (60 min) → Comprehensive discussion & wrap-up (10 min)

## 2. Speaker Lineup

- **Chair**: Prof. Keun Lee (Seoul National University / Chung-Ang University)
- **UK**: Prof. Tim Minshall (University of Cambridge)
- **China**: Prof. Yuan Zhou (Tsinghua University)
- **Japan**: Prof. Kazuyuki Motohashi (University of Tokyo)
- **USA / Korea**: Sunghee Yun (Erudio Bio; former CTO of Gauss Labs, VP of SK Hynix)

## 3. Discussion Questions & Draft Answers

### [Topic 1] How is AI changing R&D planning and evaluation methodologies?

**Q1. As AI automates trend analysis and roadmapping, in which areas is human expert-based Technology Foresight still indispensable?** *(Minshall, Motohashi)*

> **Brief note:** Defer to Minshall and Motohashi. Short supporting point if useful: AI is strong at extrapolating from existing literature and patents, but human foresight is still indispensable where the signal is sparse — framing which problems are worth solving, judging disruptive (non-incremental) shifts, and making value-laden bets under deep uncertainty.

**Q2. How are AI-based project screening and evaluation tools being implemented in Japan and the UK, and how do they coexist with expert panels?** *(Minshall, Motohashi)*

> **Brief note:** Defer to Minshall and Motohashi. Supporting point: the emerging pattern is "AI triages, humans decide" — models pre-screen for novelty, overlap and feasibility, and panels focus their time on the contested middle tier rather than the obvious accept/reject cases.

**Q3. To what extent does China utilize AI in national core technology planning, and is this widening the speed gap with other countries?** *(Yuan Zhou)*

> **Brief note:** Defer to Yuan Zhou.

**Q4. How has the method of setting R&D goals and conducting interim check-ups changed in industrial fields after the introduction of AI?** *(Sunghee Yun)*

The biggest change I've seen, both at SK Hynix and at Gauss Labs, is that goal-setting has shifted from being a periodic, document-driven ritual to a continuous, data-driven loop. The unit of planning used to be the quarter or the milestone; now it is increasingly the dataset and the model run.

- **From fixed targets to live hypotheses:** We used to lock specs at the start of a project and review against them at fixed gates. With AI in the loop, the target itself becomes a moving estimate — a model continuously re-forecasts the achievable yield, performance, or cost given the data accumulated so far, so the "goal" is re-baselined as evidence arrives.
- **Interim check-ups become continuous, not calendar-based:** Instead of a human-prepared status review every few months, dashboards and anomaly-detection models flag when a project is drifting off its predicted trajectory in near real time. The review meeting changes character — it is less about "what happened" and more about "the model says we are diverging here, why, and do we kill or pivot."
- **Faster, cheaper kill decisions:** The most valuable effect is shortening the time to a confident "no." In semiconductor and bio R&D the expensive thing is running the full physical cycle. AI lets us simulate or predict outcomes earlier, so we stop weak branches before they consume fab time or wet-lab cost. The KPI quietly shifts from "milestones hit" to "good decisions per unit of experimental budget."
- **A caution — the metrics can fool you:** Models optimize what you measure. If interim check-ups reward only the predicted metric, teams start engineering toward the predictor rather than the real-world result. So in practice we kept a human "reality gate" — a physical confirmation before any major resource commitment — precisely to stop the planning AI from quietly drifting away from ground truth.

### [Topic 2] AI Integration and Industrial R&D Productivity (Focus on Manufacturing / Materials)

**Q1. To what extent is AI replacing or compressing the "wet lab" cycle in semiconductors, batteries, and bio, and how is this reshaping the workforce structure?** *(Sunghee Yun)*

AI is compressing the wet-lab cycle far more than it is replacing it, and the distinction matters. The physical experiment is still the source of truth; what AI removes is the number of physical experiments you need to reach it.

- **Compression, not replacement:** In materials and batteries, surrogate models plus Bayesian optimization let you screen thousands of candidate formulations in silico and then physically test only the most promising handful. "Self-driving" or autonomous labs — robotics plus an AI that chooses the next experiment — are turning the design–make–test–analyze loop from weeks into days for the right problem classes.
- **Semiconductors:** Most of the gain is in design and process — AI-assisted EDA, lithography/OPC optimization, and virtual metrology that predicts a measurement instead of taking it. That directly cuts cycle time and wafer cost. But you cannot AI your way out of a physical defect; the fab floor remains stubbornly real.
- **Bio is the hardest to compress:** Protein structure prediction collapsed one step dramatically, but biology's feedback loops are noisy and causally tangled, so the wet lab stays central. AI narrows the search; it does not yet close it.

On the workforce, the shape of the change is what people underestimate:

- The "pair of hands" roles — routine sample prep, repetitive characterization — shrink first.
- Demand rises for hybrids: people who understand both the domain physics/chemistry and the data/ML pipeline. The scarce talent is not the pure ML engineer or the pure bench scientist, but the person who can translate between them.
- New roles appear around data: experiment-data curation, ML-ops for the lab, and "model validation" — someone whose job is to keep the surrogate honest against physical reality. Net, the headcount doesn't simply fall; it migrates up the skill curve, which is a real reskilling and hiring challenge for incumbent manufacturers.

**Q2. Will the generalization of AI Foundation Models allow SMEs to have R&D capabilities similar to large corporations, or will the data gap widen?** *(Common)*

Both at once, and which one dominates depends on the layer you are competing on. Foundation models are a genuine equalizer at the generic layer and a divider at the proprietary layer.

- **The equalizing effect is real:** An SME today can rent frontier-scale capability by API for the price of a coffee per query. Off-the-shelf foundation models, open weights, and cloud compute mean a small team no longer needs to build a large in-house ML group to get strong general-purpose reasoning, code, or literature synthesis. The fixed cost of "table-stakes" AI has collapsed.
- **But the moat moved to proprietary data and process context:** The model is increasingly a commodity; the differentiator is the data you have that no one else does — your fab's process traces, your battery cycling data, your assay results. Large incumbents sit on decades of exactly this. So the gap doesn't close, it relocates from "who can build the model" to "who owns the domain data and the feedback loop."
- **My net view:** Foundation models raise the floor for everyone but raise the ceiling fastest for whoever owns unique, high-quality data. SMEs win in narrow verticals where they have a data advantage or can move faster; they lose in domains where capability scales with proprietary data volume. The policy lever that actually helps SMEs is therefore shared / pre-competitive data infrastructure and access to compute — not more generic models.

**Q3. What is the role of government support in how UK industries integrate AI?** *(Minshall)*

> **Brief note:** Defer to Minshall (Catapult network, Made Smarter, etc.). Supporting point if asked: the useful government role is de-risking adoption for the long tail of mid-size manufacturers — shared testbeds and skills — rather than subsidizing frontier model development.

**Q4. In Japan's "Monozukuri" innovation model, how does AI address the "codification of artisan knowledge"?** *(Motohashi)*

> **Brief note:** Defer to Motohashi. Supporting point: this is the tacit-to-explicit problem — sensors plus ML can capture the master's "feel" (vibration, temperature, timing) as data, but the risk is losing the judgment that knows when the rule doesn't apply.

**Q5. What is the true source of competitiveness in industrial AI: algorithms, data, or process context knowledge?** *(Common)*

If I had to rank them for industrial AI specifically: process context knowledge first, data second, algorithms a distant third. This is almost the opposite of the ranking people assume from the consumer-AI headlines.

- **Algorithms have largely commoditized.** The best architectures are published, open-sourced, and re-implemented within months. Almost no durable industrial moat is built purely on a clever model.
- **Data is necessary but overrated in isolation.** Everyone says "data is the new oil," but raw industrial data is mostly noise, mislabeled, or measured under conditions you no longer remember. Data only becomes valuable once someone who understands the process knows what it means.
- **Process context knowledge is the real moat.** Knowing which variables actually matter, what a sensor reading means physically, where the data is biased, and which prediction is safe to act on — that domain understanding is what turns a model into a deployed, trusted system. At Gauss Labs the hard part was never the algorithm; it was encoding semiconductor process knowledge so the model's output was something a fab engineer would actually act on.

So my one-line answer: in industrial AI, competitiveness lives at the intersection of proprietary data and the process knowledge to use it — the algorithm is the easy 10%.

### [Topic 3] The Future of Manufacturing: What will factories look like in 2035?

**Q1. How will the job structure of the Korean industrial workforce be reorganized as AI transformation accelerates? What policies are the UK, Japan, and China testing?** *(Minshall, Motohashi, Yuan Zhou)*

> **Brief note:** Primarily for the international panelists on the comparative policy side. If invited in on Korea: expect polarization — fewer mid-skill operator roles, more demand at both the high-skill (data/automation engineering) and the flexible-services ends — so the policy priority is mid-career reskilling, not just new-graduate training.

**Q2. As AI automates design and optimization, how should the concept of "technology accumulation" be redefined? Does AI's ability to compress/transfer experience fundamentally change the "catch-up" structure for latecomer countries?** *(Common)*

Yes, AI changes the catch-up structure, but not in the simple "latecomers leapfrog everyone" way the question invites. It changes what is easy to copy and what stays hard — and it actually raises the value of the hardest-to-copy assets.

- **Redefining accumulation:** Traditionally, "technology accumulation" meant decades of embodied learning — know-how living in engineers' heads and in process recipes. AI lets some of that be compressed into models and transferred quickly, so the codifiable part of experience accumulates much faster and depreciates faster too.
- **What this helps with catch-up:** Latecomers can skip some of the slow, manual tuning by buying or training models on available data — a real compression of the early learning curve, similar to how mobile let some economies skip landlines.
- **But the moat deepens at the frontier:** The experience that matters most — running a leading-edge fab at high yield — is precisely the tacit, physically-coupled knowledge that AI cannot yet capture, because the training data only exists inside the few firms already operating at that level. So AI compresses catch-up in the middle of the curve and steepens it at the very top.
- **Net:** Catch-up gets faster for codifiable, data-rich technologies and harder for tacit, capital-and-yield-intensive ones. For a country like Korea the implication is to defend the frontier (where the data moat is) rather than assume the lead is safe.

**Q3. What are the most persistent challenges in the field regarding "autonomous factories"? What are the pros and cons of China's many "Dark Factories"?** *(Common, Yuan Zhou)*

The persistent challenge with autonomous (lights-out) factories is not the robotics — it is the long tail of exceptions. Automating the 95% normal case is now routine; the remaining 5% of edge cases is where almost all the cost and risk live.

- **The exception problem:** A fully autonomous line must handle the rare fault, the out-of-spec part, the upstream supply hiccup. Each exception that still needs a human breaks the "lights-out" promise, so true autonomy is gated by how well the system degrades and recovers, not by peak throughput.
- **Brittleness and changeover:** Dark factories are superb at high-volume, stable products and poor at flexibility. Retooling for a new product is still slow and human-intensive. They optimize for a world that doesn't change — which is risky in volatile demand.
- **Resilience and skills hollowing:** When you remove humans from the floor, you also remove the people who used to catch subtle problems by intuition. If the automation fails, the recovery capability may have atrophied. There's also a cybersecurity and single-point-of-failure exposure.
- **China's dark factories — quick take (defer detail to Yuan Zhou):** Pros are speed, scale, consistent quality and lower labor cost, enabled by huge domestic volume that justifies the capex. Cons are heavy capital lock-in, inflexibility to product change, and dependence on continuous demand to amortize. Impressive for commoditized high-volume goods; less obviously the right model for high-mix or rapidly evolving products.

**Q4. Why does "demonstration success" in AI factory R&D often fail to lead to "technology diffusion"? What can be learned from the UK's knowledge transfer (KTN / Catapult) experience?** *(Minshall)*

> **Brief note:** Defer to Minshall on the UK KTN/Catapult lessons. Supporting point from industry: the pilot-to-scale gap is real — demos succeed in curated conditions with the original team present; diffusion fails because the receiving plant lacks the data infrastructure, integration effort, and in-house skills to sustain it. The fix is funding integration and skills, not more demonstrators.

### [Topic 4] The Future of Global AI R&D Cooperation

**Q1. How should international R&D portfolios be redesigned amidst the US-China tech decoupling?** *(Common)*

The honest answer is that the era of treating global R&D as a single frictionless pool is over, and portfolios now have to be designed with geopolitics as a first-class constraint rather than an afterthought.

- **Segment by sensitivity:** Separate pre-competitive, openly-publishable research (climate, health, fundamental science — keep these as collaborative as possible) from strategic/dual-use work (advanced compute, leading-edge semiconductors, certain bio) that now needs jurisdiction-aware handling.
- **Design for resilience, not just efficiency:** The old logic optimized for lowest cost and best talent regardless of location. The new logic adds redundancy — a "China+1" / "friend-shoring" approach to critical capabilities so a single decoupling event can't sever a whole program.
- **Korea's specific position:** Caught between its largest customer/ally and its largest neighbor/market. The pragmatic move is to deepen trusted-partner R&D alliances where the strategic stakes are high, while keeping open scientific channels alive everywhere they are still permitted.
- **Practical hedge for companies:** Assume model weights, tooling, and data may face export controls; architect so you are not single-sourced on any one country's chips, cloud, or talent. The cost of decoupling is real — don't pretend the efficient pre-2020 structure is coming back.

**Q2. What lessons does the UK's re-participation in Horizon Europe provide regarding the politico-economic conditions of "tech alliance-based R&D"?** *(Minshall)*

> **Brief note:** Defer to Minshall. Supporting point: the lesson is that scientific collaboration networks are costly to exit and slow to rebuild — political ruptures impose a real, lagged tax on research, which argues for insulating science from short-term politics where possible.

**Q3. What efforts is China making to form a global AI ecosystem? Where are the possibilities for cooperation with Korea?** *(Yuan Zhou)*

> **Brief note:** Defer to Yuan Zhou. If asked on Korea cooperation: the realistic openings are in standards, open scientific research, and shared application domains (manufacturing, materials) rather than in the most strategically sensitive frontier compute.

**Q4. As AI regulations tighten, regulatory arbitrage is occurring. What kind of regulatory framework do AI startups want?** *(Sunghee Yun)*

Having operated on the startup side, I'd push back gently on the framing: serious startups don't actually want *no* regulation — they want *predictable, proportionate, and portable* regulation. Uncertainty is far more expensive to a small company than rules are.

- **Predictability over leniency:** A clear rule I can build against beats a vague "we'll decide later." The worst environment for a startup is regulatory ambiguity, because we can't afford to bet the company on a guess about how a law will be interpreted in two years.
- **Proportionality by risk and size:** Regulate by the actual risk of the application, not by whether the word "AI" appears. And recognize that a five-person team cannot carry the same compliance load as a large incumbent — hence the value of the EU AI Act's SME provisions, regulatory sandboxes, reduced fees, and simplified documentation. Heavy uniform compliance is itself a moat that protects incumbents and crushes startups.
- **Portability / harmonization:** Fragmentation is the real killer. Today a startup faces the EU AI Act, a patchwork of US state laws, and shifting federal direction all at once. Every extra incompatible regime is pure deadweight cost for a small company. What we want is mutual recognition and common standards so one good-faith compliance effort travels across markets.
- **On regulatory arbitrage specifically:** Yes, it happens — teams do incorporate where sandboxes and lighter regimes exist. But arbitrage is a symptom, not a strategy; it adds legal overhead and signals fragility to investors. The right response from regulators is to compete on clarity and sandbox quality, not on a race to the bottom. Sensible, stable rules actually attract startups — "regulatory readiness" has become a selling point to enterprise customers and investors, not just a cost.

### [Topic 5] The Emergence of Non-Human Innovators and R&D Governance

**Q1. How should patent attribution, research fund settlement, and performance evaluation for AI-generated inventions be designed?** *(Minshall, Motohashi, Yuan Zhou)*

> **Brief note:** Primarily for the panelists. Supporting point if asked: current law in most jurisdictions requires a human inventor, so the practical near-term answer is to attribute to the human directing the AI while disclosing AI's role — but this needs reform as AI contribution grows.

**Q2. How do you assess the risks that open-source AI models (LLaMA, DeepSeek, etc.) pose to corporate security and national strategic technology protection?** *(Yuan Zhou, Sunghee Yun)*

Open-weight models are, on balance, a net positive for industry — but the security conversation needs to separate two very different risks that often get blurred together: data leakage on the inbound side, and supply-chain/trust risk on the model side.

- **The understated upside:** Open models are actually the safer choice for a lot of corporate use, because you can run them on-premise. For a semiconductor or bio company, the biggest day-to-day risk is sending sensitive process data to a third-party API. A local open-weight model keeps the data inside the firewall — that's a security win, not a loss.
- **The real inbound risk is people, not the model:** The leakage problem is employees pasting proprietary data into external chatbots. That's a governance and tooling issue — provide a sanctioned internal model so staff don't route around policy.
- **Model-side / supply-chain risk:** An open model is still code and weights from somewhere. Risks include data-poisoning or backdoors in the training, hidden biases, and license/provenance ambiguity. For anything strategic you need provenance, evaluation, and ideally fine-tuning on trusted data before you deploy — "open" doesn't mean "vetted."
- **National-strategic angle (defer geopolitics to Yuan Zhou):** Open weights diffuse frontier capability globally, which erodes any single country's lead and complicates export controls — you can't easily control what's already downloadable. My view: protection should focus on the genuinely scarce chokepoints — leading-edge compute, fab process know-how, and unique datasets — rather than trying to bottle up model architectures that are already in the open.

**Q3. How should R&D audit systems be strengthened to combat AI-driven research misconduct (data manipulation, false results)?** *(Common)*

AI cuts both ways here: it lowers the cost of fabricating convincing fake data and images, but it also gives auditors powerful new detection tools. The governance answer is to shift audit from trusting outputs to verifying provenance.

- **Provenance over inspection:** The durable fix is an auditable trail — capture raw instrument data, timestamps, and processing steps so a result can be traced back to a physical measurement. If you can't reconstruct where a number came from, treat it as unverified. This matters more than ever because AI-generated results look perfectly plausible.
- **Fight AI with AI, carefully:** Detection models can flag manipulated images, statistically improbable data, and duplicated figures at a scale human reviewers can't match. But detection is an arms race — don't treat a "clean" detector score as proof of integrity.
- **Reproducibility as the real audit:** The strongest defense is independent replication of high-stakes results. AI lowers the cost of re-running analyses and simulations, so we can afford to verify more. Tie funding milestones to reproducible artifacts (data + code), not just to claimed results.
- **Incentives, not just policing:** Most misconduct is driven by pressure to show positive results. Audit systems should be paired with incentives that reward honest negative results and pre-registration, or you're treating the symptom.

**Q4. With the shift toward software/data/cloud costs in R&D, is "labor-cost-centered" budget support still valid? What should government budgets prioritize?** *(Common)*

No — labor-cost-centered budgeting is increasingly outdated, and clinging to it actively distorts modern R&D. The cost structure of research has moved, and funding rules haven't caught up.

- **The cost base has shifted:** In AI-heavy R&D, the dominant expenses are now compute, cloud, data acquisition/labeling, and software/licenses — not headcount. A small team with a large compute and data budget can outproduce a large team without them.
- **Why labor-centric rules distort behavior:** When grants mainly reimburse salaries and treat cloud/data as suspect overhead, teams over-hire and under-invest in the very inputs (compute, data) that drive results. They also can't flexibly burst compute when they need it. The funding instrument shapes the science — badly, in this case.
- **What government budgets should prioritize:** (1) **Shared compute infrastructure** — national/regional GPU access, especially for SMEs and universities priced out of frontier compute; (2) **Data as infrastructure** — funding the creation, curation, and shared access of high-quality domain datasets, which is pre-competitive and exactly where markets under-invest; (3) **Flexible cost categories** so cloud, data, and software are first-class fundable items, not grudging overhead.
- **One caveat — people still matter:** The scarce hybrid talent I mentioned earlier is the real bottleneck. So the answer isn't "fund machines instead of people," it's "stop forcing everything through a salary-shaped budget line" and fund compute, data, and people as the three genuine inputs they are.

---

*Note: full answers above are first-person drafts for my own questions and for the "Common" questions; "brief note" items are short reminders so I can hand off cleanly to the relevant panelist or chime in with one supporting point.*
