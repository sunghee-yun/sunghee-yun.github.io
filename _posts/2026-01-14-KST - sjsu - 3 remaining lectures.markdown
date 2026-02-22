---
date: Wed Jan 14 08:46:00 PST 2026
last_modified_at: Fri Feb 20 01:35:29 PST 2026
title: "THREE remaining lectures for Kyungpook National University Students"
permalink: /ai-lecture/sjsu/3
categories:
 - blog
 - AI
 - Education
 - Reflections
tags:
 - entrepreneurship
 - teaching
 - AI education
 - San Jose State University
 - paradigm shift
 - interactive learning
toc: true
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
---

posted: {{ page.date| date: "%d-%b-%Y" }}
&
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

**Share on**
[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url={{ site.url }}{{ site.baseurl }}{{ page.url }})
| [Instagram](https://www.instagram.com/)
| [Twitter (X)](https://x.com/intent/tweet?text={{ site.url }}{{ site.baseurl }}{{ page.url }})
| [Facebook](https://www.facebook.com/sharer/sharer.php?u={{ site.url }}{{ site.baseurl }}{{ page.url }})

<!--
The original summary of feedback can be found at <a target="_blank" href="https://sungheeyun-seminars-01.github.io/resource/seminars/2025_1229 - 2026_0116 - San Jose State Univ - Special AI Lectures/Feedback on Sunghee Yun's Special AI Lectures and Request for Advanced AI Learning.pdf">Feedback and Request for Advanced Learning (PDF)</a>
{: .notice--success}
-->

# **LECTURE 6: From Theory to Production - How Silicon Valley Ships LLM Products**

## **Real Production Architecture Deep Dive**

**A. RAG in Production - Beyond the Basics**

*Start with a real problem:*
"When Notion added Notion AI, they weren't just calling OpenAI API. Let me show you what actually happens..."

**The Production RAG Stack - Layer by Layer:**

1. **Document Ingestion Pipeline**
   - **Chunking strategies that matter:** Not just "split every 512 tokens"
     - Semantic chunking (respecting paragraph/section boundaries)
     - Sliding window with overlap (128-256 token overlap to preserve context)
     - Metadata tagging (document type, date, author, department)
   - **Real challenge:** "How do you handle a 300-page PDF contract where page 47 references page 203?"
   - **Production tools:** Unstructured.io, LangChain Document Loaders, LlamaIndex
   - **Cost consideration:** "At Anthropic API pricing, re-processing 10TB of documents monthly costs..."

2. **Vector Database Selection - The Real Trade-offs**
   - **Pinecone vs. Weaviate vs. Chroma vs. Postgres+pgvector**
   - Show actual performance metrics:
     - Query latency: 10ms vs 100ms makes or breaks user experience
     - Cost at scale: "1M vectors in Pinecone costs $X/month vs self-hosted"
     - Hybrid search (vector + keyword): "Why Google still uses BM25 alongside embeddings"
   - **Real decision:** "Spotify uses custom vector DB. Why? Because at 500M users..."

3. **Embedding Model Selection**
   - **OpenAI text-embedding-3 vs. Cohere vs. open-source (BGE, E5)**
   - Dimensions trade-off: 1536-dim vs 768-dim vs 384-dim
   - **Domain-specific fine-tuning:** "For medical records, general embeddings fail because..."
   - **Multilingual considerations:** Korean+English embeddings performance gap
   - **Your Erudio Bio example:** "For cancer biomarker literature, we fine-tuned embeddings on 50K papers because..."

4. **Retrieval Strategy - Where Theory Meets Reality**
   - **K parameter tuning:** "K=5 vs K=20, how do you decide?"
   - **Re-ranking layer:** "Cross-encoder models like Cohere Rerank - why add 50ms latency?"
   - **Query transformation:**
     - HyDE (Hypothetical Document Embeddings)
     - Query decomposition for complex questions
     - Example: "What's our Q3 sales in Seoul vs Busan?" → 3 sub-queries
   - **Metadata filtering:** "Show me documents from 2024 by Engineering team"

5. **Context Window Management**
   - **The 128K token trap:** "Just because Claude has 200K context doesn't mean you should use it all"
   - **Token budgeting:** System prompt (500) + Retrieved docs (4000) + Conversation (2000) + Output (1500)
   - **Compression techniques:** LLMLingua, prompt compression
   - **Real problem:** "When your retrieved context contradicts, how does the model choose?"

**B. AI Agents - From Demo to Reliable System**

*"Remember AutoGPT? Cool demo, 90% failure rate. Here's why production agents are completely different..."*

**The Agent Architecture That Actually Works:**

1. **Agent Framework Comparison**
   - **LangGraph vs. CrewAI vs. AutoGPT vs. custom frameworks**
   - Why major companies build custom: "OpenAI has Assistants API, but Stripe built their own because..."
   - **State management:** "How do you handle 50 steps without losing context?"
   - **Error recovery:** "When tool call #7 fails, do you restart or retry?"

2. **Tool Calling - The Production Reality**
   - **Function calling vs. native tools:** OpenAI format vs. Anthropic format vs. custom parsing
   - **Tool reliability:** "Your agent calls `get_weather()` - what if the API is down?"
   - **Tool result validation:** "The API returned 404. Should your agent hallucinate or admit failure?"
   - **Cost explosion:** "Each tool call = another LLM invocation = $$$"
   - **Example from your work:** "At Amazon, recommendation agents had to call 5-7 services. Here's how we handled failure cascades..."

3. **The Planning vs. ReAct Trade-off**
   - **Planning agents:** "Think step-by-step, then execute" (like Chain-of-Thought)
     - Pros: More reliable, debuggable
     - Cons: Less adaptive, higher latency
   - **ReAct agents:** "Observe → Think → Act → Repeat"
     - Pros: Adaptive, can recover from errors
     - Cons: Unpredictable paths, token waste
   - **Real production:** "Most companies use hybrid - plan high-level, ReAct for details"

4. **Multi-Agent Systems**
   - **When to use multiple agents vs. single agent with tools?**
   - **Coordination patterns:**
     - Hierarchical (manager + worker agents)
     - Sequential (pipeline)
     - Collaborative (agents debate/vote)
   - **Real example:** "Klarna's customer service uses 3 agents: Classifier → Resolver → Validator"
   - **Communication overhead:** "Agent-to-agent communication = more LLM calls = latency + cost"

**C. Multimodal AI in Production**

1. **Vision + Language - Beyond Image Captioning**
   - **Real use cases:**
     - **Medical imaging:** "How Erudio Bio processes microscopy images for cancer detection"
     - **Visual search:** Pinterest Lens architecture
     - **Document understanding:** GPT-4V processing invoices, receipts, forms
   - **The OCR-first vs. vision-first debate:**
     - Traditional: OCR → text extraction → LLM
     - Modern: Image → Vision-Language Model → structured output
     - Cost/accuracy trade-off: "GPT-4V costs 10x more than OCR+GPT-4"

2. **Audio Integration**
   - **Whisper in production:** "Not just transcription - handling 50 languages, accents, background noise"
   - **Real-time vs. batch:** "Video conferencing notes (real-time) vs. podcast transcription (batch)"
   - **Voice cloning ethics:** "When WeStory.ai generates voiceovers, how do we prevent misuse?"

3. **The Modality Fusion Challenge**
   - **Early fusion vs. late fusion:** "Do you combine inputs before or after encoding?"
   - **Cross-modal attention:** "How does the model know to look at image region X when reading text Y?"
   - **Real bottleneck:** "Processing video = 30 fps × resolution → compute explosion"

---

## **Production Challenges Nobody Talks About**

**A. Cost Optimization**

*"I've seen startups burn $100K/month on LLM APIs without realizing it. Here's how to not be that startup..."*

1. **Token Economics**
   - **Input vs. output tokens:** "Output tokens cost 3x more in most APIs"
   - **Caching strategies:** Anthropic's prompt caching, how to structure prompts for cache hits
   - **Model selection ladder:** "Start with GPT-4 for prototyping, move to GPT-3.5 for 90% of requests, keep GPT-4 for hard cases"
   - **Example calculation:** "100K daily requests at 1K tokens each = $X/month"

2. **Latency Optimization**
   - **The 3-second rule:** "Users abandon if response takes >3 seconds"
   - **Streaming responses:** "Why ChatGPT shows tokens one-by-one (perceived performance)"
   - **Parallel calls:** "Don't wait for call #1 to finish before starting call #2"
   - **Edge deployment:** "Why Cloudflare Workers + LLM is gaining traction"

3. **Quality Monitoring**
   - **How do you know your RAG is working?**
     - Retrieval precision: "Are you getting the right documents?"
     - Faithfulness: "Is the answer grounded in retrieved context?"
     - Relevance: "Does the answer actually address the question?"
   - **Production metrics:**
     - Thumbs up/down rates
     - User abandonment rate
     - Edit distance (for coding assistants)
   - **A/B testing LLM systems:** "How Stripe tests prompt variations with 5% traffic"

**B. Safety & Reliability**

1. **Guardrails in Production**
   - **Input filtering:** "Block jailbreak attempts, PII, malicious prompts"
   - **Output filtering:** "Detect hallucinations, harmful content, off-topic responses"
   - **Tools:** LlamaGuard, Guardrails AI, NeMo Guardrails
   - **Real failure:** "Air Canada chatbot hallucinated refund policy → legal liability"

2. **The Determinism Problem**
   - **Temperature = 0 ≠ deterministic:** "Same prompt can give different outputs"
   - **Seed parameters:** OpenAI/Anthropic seed for reproducibility
   - **Why it matters:** "In legal or medical AI, reproducibility is critical"
   - **Production pattern:** "For user-facing = creative, for internal tools = deterministic"

3. **Fallback Strategies**
   - **Circuit breakers:** "When API fails, don't hang forever"
   - **Graceful degradation:** "If GPT-4 is down, fall back to GPT-3.5"
   - **Human-in-the-loop:** "Critical decisions require human approval"

---

## **Interactive Workshop**

**Case Study Exercise:**

*"You're building a AI-powered customer support system for a Korean e-commerce platform. 10M users, 100K support tickets/month. Design the architecture."*

**Students must decide:**
1. RAG or fine-tuning or both?
2. Which embedding model? (Korean-specific considerations)
3. How many vectors? (10M product descriptions × 5 customer reviews each)
4. Agent or retrieval-only?
5. Cost budget: $10K/month - how do you optimize?

**Walk through real architectural decisions:**
- "If you use GPT-4 for everything → $50K/month → bankruptcy"
- "If you use GPT-3.5 for everything → quality issues → customer complaints"
- "Solution: Classifier model (small) → routes to GPT-3.5 (80%) or GPT-4 (20%)"

**Q&A Focus Areas:**
- "How does Netflix recommendation system differ from LLM recommendation?"
- "When should you build custom models vs. use APIs?"
- "How do you handle Korean language nuances in RAG?"

---

# **LECTURE 7: The Business of AI - How Technology Becomes Value**

## **Business Model Transformation**

**A. How LLMs Are Reshaping Revenue Models**

*"Let me tell you how GitHub Copilot went from $0 to $100M ARR in 18 months..."*

**Case Study 1: GitHub Copilot ($100M ARR)**

1. **The Traditional Model (Pre-AI)**
   - GitHub: Subscription for code hosting ($4-21/user/month)
   - Revenue tied to storage, number of repos, team size
   - Competitive moat: Network effects, switching costs

2. **The AI-Native Model**
   - **Copilot Individual: $10/month** (completely new revenue stream)
   - **Copilot Business: $19/user/month** (2x the base subscription)
   - **Key insight:** "They didn't replace existing product, they augmented it"
   - **Unit economics:**
     - COGS per user: ~$3-5/month (API costs to OpenAI/Anthropic)
     - Gross margin: ~50-70% (vs 90%+ for traditional SaaS)
     - **Why acceptable:** "Volume + strategic value > margin"

3. **Customer Acquisition Changed**
   - **Traditional:** Sales-driven, free trials, feature comparison
   - **AI-era:** "Viral within teams - one dev tries it, whole team adopts"
   - **Adoption metrics:** "60-day retention is THE metric - if they keep using after 2 months, they never leave"

**Case Study 2: Jasper.ai ($125M ARR → $60M → ???)**

*"This is the cautionary tale everyone should know..."*

1. **The Rapid Rise (2021-2022)**
   - **Product:** GPT-3 wrapper for marketing copy
   - **Growth:** 0 → $125M ARR in 18 months
   - **Valuation:** $1.5B Series A
   - **Business model:** $49-599/month subscription (per seat)

2. **The Fall (2023-2024)**
   - **Competition:** ChatGPT Plus ($20/month) + plugins could do same thing
   - **Revenue drop:** $125M → ~$60M
   - **Why it happened:**
     - **No defensible moat:** "Just prompt engineering on top of OpenAI"
     - **Distribution advantage eroded:** "ChatGPT had 100M users in 2 months"
     - **Value capture problem:** "OpenAI captured the value, not the wrapper"

3. **The Lesson**
   - **Thin wrappers die:** "If your entire product is 'good prompts,' you're in trouble"
   - **What survives:**
     - Proprietary data/workflows
     - Domain-specific fine-tuning
     - Deep integration into existing software
     - Network effects or switching costs

**Case Study 3: Bloomberg GPT - Why They Built Their Own**

1. **The $300M Decision**
   - Bloomberg spent ~$300M training their own 50B parameter model
   - Could've just used GPT-4 API - why didn't they?

2. **Strategic Reasoning**
   - **Data moat:** "50 years of financial news, terminal data, proprietary feeds"
   - **Domain accuracy:** "General LLMs don't understand 'EBITDA multiple expansion' nuances"
   - **Competitive advantage:** "If we use OpenAI, so can our competitors"
   - **Customer trust:** "Bloomberg terminal users pay $24K/year for reliability - can't risk third-party hallucinations"

3. **The Build vs. Buy Framework**
   - **Build your own when:**
     - You have unique, valuable proprietary data
     - Domain accuracy is life-or-death
     - You can afford $10M-$100M investment
     - Competitive differentiation matters more than time-to-market
   - **Use APIs when:**
     - You need to ship fast
     - General-purpose models are "good enough"
     - Your moat is distribution/UX, not the model
     - You're pre-product-market fit (don't waste money on custom models)

**B. How AI Changes Competitive Dynamics**

*"Let me explain why every SaaS company is panicking right now..."*

1. **The "AI Feature Parity" Problem**
   - **Old world:** "It takes years to build feature X"
   - **AI world:** "It takes weeks to add AI-powered feature X"
   - **Result:** "Differentiation collapses - everyone has AI autocomplete, AI summarization, AI search"
   - **Example:**
     - Notion added Notion AI
     - Confluence added AI
     - Coda added AI
     - Obsidian added AI
     - "All in 6 months. All basically the same feature."

2. **New Competitive Moats**
   - **Data flywheels:** "The more users use your AI, the better it gets"
     - Grammarly: 30M users → best grammar model
     - Midjourney: 15M users → best image generation feedback loop
   - **Integration depth:** "It's not about having AI, it's about AI being embedded in every workflow"
     - Salesforce Einstein vs. standalone AI tools
   - **Trust & brand:** "In high-stakes domains (legal, medical, financial), brand matters more than technology"
   - **Proprietary data access:** "You can't replicate 50 years of Bloomberg terminal data"

3. **The Margin Compression Risk**
   - **Traditional SaaS margins:** 80-90% gross margin (hosting costs are low)
   - **AI-powered SaaS margins:** 50-70% gross margin (API costs are high)
   - **Investor concern:** "If your COGS increases 3x, your valuation multiple drops"
   - **Solutions:**
     - Self-host models (capital intensive)
     - Smart routing (cheap model for easy queries, expensive for hard)
     - Fine-tune smaller models (cheaper inference)

**C. Industry-Specific Transformations**

*"Let me walk through three industries I know well..."*

**1. Biotech / Healthcare (Your Erudio Bio Experience)**

- **Old paradigm:** Manual analysis of biomarker data, 2-4 weeks per patient
- **AI paradigm:** Erudio Bio's VSA platform + AI = same-day results
- **Business impact:**
  - **Revenue model shift:** Per-test fee → subscription for hospitals
  - **Market expansion:** "We can now serve smaller hospitals that couldn't afford manual analysis"
  - **Competitive advantage:** "Our dynamic force spectroscopy data is unique - general AI models can't replicate"
- **Key insight:** "AI doesn't replace the domain expertise (cancer biology), it amplifies it"

**2. Creative Industries (Your WeStory.ai Insight)**

- **Old model:** Hire voice actors, editors, animators ($5K-50K per project)
- **AI model:** WeStory.ai generates voiceovers, edits, animations (10% of cost)
- **Market dynamics:**
  - **Democratization:** "Small businesses can now afford professional content"
  - **Volume explosion:** "100x more content created, but paradox: harder to stand out"
  - **Value shift:** "From production to strategy/creativity - AI handles execution"
- **The controversial part:** "Voice actors are losing work - but new roles emerging (AI trainers, editors)"

**3. Semiconductor / Enterprise (Your Samsung & K-PAI Context)**

- **Old R&D process:** 6-12 months to optimize chip design
- **AI-assisted process:** Synopsys DSO.ai optimizes in weeks
- **Business transformation:**
  - **Time-to-market:** "First to market captures 70% of profit - AI acceleration is strategic"
  - **Cost reduction:** "Each wafer costs $1M+ - AI reduces failures by 30%"
  - **Talent leverage:** "One engineer with AI tools = 5 engineers without"
- **K-PAI angle:** "Korea's semiconductor lead depends on adopting AI faster than TSMC/Intel"

---

## **From Technology to Go-To-Market**

**A. The Silicon Valley Playbook**

*"Here's what actually happens inside a successful AI startup..."*

**Stage 1: The Founding Insight (Months 0-6)**

1. **How do you know you have a real problem?**
   - **Bad sign:** "AI can do X better/faster"
   - **Good sign:** "This $10B industry has a broken workflow, and AI unlocks a new solution"
   - **Your Erudio Bio story:** "Cancer diagnostics takes weeks, costs thousands, and misses early-stage patients - VSA + AI solves all three"

2. **Technical vs. Market Risk**
   - **Technical risk:** "Can we build the AI model?"
   - **Market risk:** "Will anyone pay for it?"
   - **Silicon Valley truth:** "Technical risk is easier to solve than market risk"
   - **Advice:** "If you're technically confident but market-uncertain, talk to 100 potential customers before writing code"

3. **The Founder-Market Fit Question**
   - "Why you? Why now?"
   - **Your answer:** "I spent 12 years in semiconductors, worked on optimization at Stanford, and saw how AI could transform biotech"
   - **Why it matters:** "Investors bet on founder expertise, not just ideas"

**Stage 2: Building the MVP (Months 6-18)**

1. **The 80/20 Rule for AI Products**
   - **Don't:** "Build the perfect model that handles every edge case"
   - **Do:** "Build the 80% solution that works for the most valuable use case"
   - **Example:** "GitHub Copilot v1 was terrible at certain languages, but great at Python/JavaScript - they launched anyway"

2. **Prototype vs. Production**
   - **Prototype:** "Jupyter notebook, manually labeled data, 70% accuracy"
   - **Production:** "API endpoint, automated pipeline, monitoring, 95% accuracy"
   - **The mistake:** "Spending 12 months building production before testing market demand"
   - **Better approach:** "Wizard of Oz MVP - fake the AI with humans to validate demand"

3. **Design Partner Strategy**
   - **Find 3-5 early customers willing to co-develop**
   - **What you give them:** "Early access, customization, lower pricing"
   - **What you get:** "Feedback, case studies, reference customers, revenue"
   - **Red flag:** "If you can't find 3 people willing to pay (even small $), you don't have product-market fit"

**Stage 3: Go-To-Market (Months 12-24)**

1. **Pricing AI Products - The Hard Questions**
   - **Per-user pricing:** "Works for SaaS, but AI usage varies wildly"
   - **Usage-based pricing:** "Fair, but unpredictable revenue"
   - **Hybrid:** "Base fee + usage overage" (most common)
   - **Example:** "OpenAI API is pure usage. GitHub Copilot is subscription. Which is better?"
   - **The answer:** "Depends on customer behavior - if usage is predictable, subscription; if spiky, usage-based"

2. **The AI Sales Pitch That Works**
   - **Don't lead with:** "We use GPT-4 and LangChain and vector databases..."
   - **Do lead with:** "We save you 10 hours per week and reduce errors by 40%"
   - **Story structure:**
     - Problem (current pain)
     - Solution (your AI product)
     - Proof (customer results)
     - Call to action
   - **Example pitch for Erudio Bio:** "Cancer diagnosis takes 3 weeks and costs $5K. Ours takes 1 day and costs $500. Hospital X saved $2M last year."

3. **Distribution Channels**
   - **Product-led growth (PLG):** Let users try it free, convert to paid (ChatGPT, Midjourney)
   - **Sales-led growth (SLG):** Outbound sales, demos, enterprise contracts (C3.ai, Scale AI)
   - **Which to choose?**
     - PLG if: Simple product, self-serve, low price point, broad market
     - SLG if: Complex product, requires integration, high price point, regulated industry
   - **Erudio Bio's choice:** "Healthcare = regulated + high-value = sales-led"

**B. The Money Question - Fundraising**

*"Let me tell you what investors actually care about..."*

1. **The AI Pitch Deck (15 slides)**
   - Slide 1: **Problem** (Show the pain)
   - Slide 2: **Solution** (Your AI product)
   - Slide 3: **Why now?** (Why is this possible today but not 5 years ago?)
   - Slide 4: **Market size** ($XB TAM, $YB SAM, $ZB SOM)
   - Slide 5: **Business model** (How do you make money?)
   - Slide 6: **Traction** (Revenue, users, growth rate)
   - Slide 7: **Product demo** (Show, don't tell)
   - Slide 8: **Technology moat** (Why can't someone copy you?)
   - Slide 9: **Go-to-market** (How do you acquire customers?)
   - Slide 10: **Competition** (Who else is doing this, why you win)
   - Slide 11: **Team** (Why you're the best team to solve this)
   - Slide 12: **Financials** (3-year projections)
   - Slide 13: **Use of funds** (What will you spend the money on?)
   - Slide 14: **Vision** (Where you'll be in 5-10 years)
   - Slide 15: **Ask** (How much you're raising, valuation)

2. **What VCs Actually Evaluate**
   - **Team (40% of decision):** "Can these founders execute?"
   - **Market (30%):** "Is this a big, growing market?"
   - **Product (20%):** "Is this 10x better than alternatives?"
   - **Traction (10%):** "Are customers actually paying?"
   - **The AI-specific question:** "Is this defensible against OpenAI/Google?"

3. **Valuation Mechanics**
   - **Pre-revenue:** $5-10M valuation (friends & family, angels)
   - **Post-revenue, pre-PMF:** $10-30M (pre-seed/seed)
   - **Product-market fit:** $50-150M (Series A)
   - **Scaling:** $200M-1B+ (Series B/C)
   - **AI premium:** "AI companies get 20-30% higher valuations than non-AI in 2024"
   - **But:** "If you're just a wrapper, you get 50% discount"

---

## **Interactive Case Study**

**Scenario: You're starting an AI company**

*"Break into groups of 3-4. You have 20 minutes to develop a pitch."*

**Constraints:**
- Industry: Choose one (healthcare, fintech, e-commerce, education, logistics)
- You have: Technical skills, $100K savings, 6 months runway
- You need: Idea, MVP plan, first 3 customers strategy

**Deliverable:**
- 2-minute pitch answering:
  1. What problem?
  2. Why AI solution?
  3. Who pays?
  4. How much?
  5. What's your unfair advantage?

**Debrief:**
- "Which pitches would I invest in and why?"
- "Common mistakes you all made"
- "How to strengthen your weakest point"

**Q&A:**
- "How do you know when to fundraise vs. bootstrap?"
- "Should you raise from Korean VCs or Silicon Valley VCs?"
- "How does WeStory.ai's business model work?"

---

# **LECTURE 8: Thriving in the AI Era - Career, Capabilities, and Choice**

## **Your Personal Journey - The Real Story**

**A. Decision Points & Pivots**

*"Let me tell you about the moments that actually mattered in my career..."*

**1. Samsung to Stanford (2006-ish)**
- **The context:** "I was doing well at Samsung - stable job, good salary, clear promotion path"
- **The question:** "Should I leave for a PhD at age X, with no guarantee I'll succeed?"
- **What made me decide:**
  - "I realized I was solving the same problems repeatedly"
  - "The most exciting work was being done in academia/startups, not big companies"
  - "My mentor told me: 'If you don't try, you'll always wonder'"
- **What I'd do differently:** "I'd have done it 2 years earlier - the opportunity cost of waiting is high"
- **The lesson:** "Stability is overrated when you're young and have few obligations"

**2. Stanford PhD - Choosing Convex Optimization (2006-2011)**
- **Why Stephen Boyd's group?**
  - "Optimization is the math underneath everything - ML, control systems, semiconductors"
  - "Boyd's philosophy: 'Elegant math should solve real problems'"
  - "The Erdős connection was a bonus, not the reason"
- **The hard parts:**
  - "Imposter syndrome among Stanford PhDs is real"
  - "Year 3-4: 'Is this thesis ever going to work?'"
  - "Pressure to publish vs. solve real problems"
- **What made it worth it:**
  - "Mathematical rigor I developed there still serves me today"
  - "Network: My Stanford cohort are now CTOs, professors, founders"
  - "Learned to think deeply and slowly - antidote to Silicon Valley's speed obsession"

**3. Samsung Semiconductor (12 years total) - The Optimization Pivot**
- **iOpt platform story:**
  - "I saw engineers manually tuning chip parameters for weeks"
  - "Built optimization tools that reduced 3 weeks → 3 hours"
  - "Company saved $XM, I got recognition - but also realized the limits of corporate innovation"
- **Why I stayed 12 years:**
  - "Deep domain expertise takes time - you can't rush it"
  - "I learned how chips are actually made, not just designed"
  - "Relationship capital - I still call these people for advice"
- **Why I left:**
  - "I'd done everything I could do in that role"
  - "The next level was politics, not technology"
  - "Amazon called with a very different problem"

**4. Amazon - Senior Applied Scientist (2016-2018 estimated)**
- **The opportunity:** "Build recommendation systems at scale - billions of dollars in revenue"
- **What I learned:**
  - "Scale changes everything - algorithms that work for 1M users break at 100M"
  - "A/B testing discipline: 'Show me the numbers or it doesn't matter'"
  - "Operational excellence: If your model goes down, millions in revenue are lost per hour"
- **The $200M+ impact:**
  - "Our recommendation improvements drove X% increase in conversion"
  - "That translated to hundreds of millions in revenue"
  - "But - it felt like optimizing a machine, not building something new"
- **The realization:**
  - "I'm not a 'work on someone else's vision' person"
  - "I want to build, not optimize"
  - "The only way to do that is to start something"

**5. The Startup Journey - Gauss Labs & Erudio Bio**

*"This is where it gets real..."*

**Gauss Labs (Co-founder, CTO) - Industrial AI**
- **The founding moment:**
  - "I saw manufacturers manually inspecting products - same problem as Samsung, different industry"
  - "Computer vision + optimization = automated quality control"
  - "My co-founder had manufacturing connections, I had tech - perfect combo"
- **Early challenges:**
  - "First 6 months: No revenue, living on savings, doubting every decision"
  - "Customer meetings: 'Your AI is 80% accurate.' Them: 'We need 99.9%.' Me: 'Damn.'"
  - "Learning to sell: 'I'm an engineer, not a salesperson' - had to become both"
- **The breakthrough:**
  - "One design partner gave us 6 months to prove it"
  - "We shipped 15-hour days, got to 95% accuracy"
  - "They signed a $500K contract - validation"
- **Why it didn't become huge:**
  - "Industrial AI is a hard sell - long sales cycles, pilot hell"
  - "But - it taught me everything about running a company"

**Erudio Bio (Co-founder & CTO, US / CEO, Korea) - The Current Chapter**
- **The insight:**
  - "Cancer diagnostics is broken - slow, expensive, misses early stages"
  - "Our VSA platform generates unique force spectroscopy data"
  - "Combine that with AI → better, faster, cheaper detection"
- **Why this one feels different:**
  - "Healthcare has massive markets, clear value, willingness to pay"
  - "Our tech is defensible - can't replicate our data"
  - "It's not just revenue, it's impact - we might save lives"
- **Current challenges (be honest):**
  - "IRB approvals take forever - dealing with Seoul National University Bundang Hospital right now"
  - "Regulatory path (FDA/MFDS) is 3-5 years and $10M+"
  - "Hiring is hard - need people who understand both AI and biology"
  - "Fundraising in biotech is different - need clinical data, not just traction"
- **Why I keep going:**
  - "Every time I want to quit, I remember: this could detect cancer 2 years earlier for someone"
  - "And - I'm unemployable now. Can't go back to corporate after this" (laugh)

**6. Parallel Roles - K-PAI, WeStory.ai**
- **Why I do multiple things:**
  - "One company is risky - diversifying effort and learning"
  - "K-PAI: Policy influence + network in Korea's AI ecosystem"
  - "WeStory.ai: Creative AI applications, different from biotech"
- **Time management (be real):**
  - "I don't sleep 8 hours. More like 5-6."
  - "I say no to 90% of opportunities"
  - "Each role feeds the others - K-PAI connections help Erudio, etc."

**B. What I'd Tell My 20-Year-Old Self**

1. **"Start earlier, fail faster"**
   - "I waited until my 30s to start a company - wish I'd done it at 25"
   - "Your biggest asset when young: low opportunity cost and high energy"
   - "Failure at 25 is cheap, failure at 35 is expensive"

2. **"Network is not who you know, it's who trusts you"**
   - "I spent years building relationships without asking for anything"
   - "Now when I need help, people respond"
   - "But - this takes 5-10 years, you can't shortcut it"

3. **"Depth > breadth, but breadth enables pivots"**
   - "Go deep in one domain (for me: optimization + semiconductors)"
   - "But learn enough adjacent fields to see connections (bio, AI, business)"
   - "The magic happens at intersections"

4. **"Money follows impact, not the other way around"**
   - "I never chose a job for salary"
   - "I chose for learning, impact, and people"
   - "The money came later, but more importantly - I never hated my work"

5. **"Technical skills decay, judgment compounds"**
   - "I can't code as fast as I could at 25"
   - "But I know which problems to solve and which to ignore"
   - "That judgment is worth more than any technical skill"

**C. The Hard Parts Nobody Tells You**

*"Let me be brutally honest about entrepreneurship..."*

1. **The emotional roller coaster**
   - "Monday: 'We're going to change the world!'"
   - "Friday: 'Why am I doing this? Should I get a normal job?'"
   - "This happens every week, even now"

2. **The financial stress**
   - "I've had months where I couldn't pay myself"
   - "Watching your savings drain while waiting for customers to pay"
   - "The first $1M you raise goes faster than you think"

3. **The relationship cost**
   - "I've missed family events, vacations, personal milestones"
   - "Your partners/friends need to understand this life"
   - "Or - you need to be okay being alone sometimes"

4. **The impostor syndrome**
   - "Even with a Stanford PhD and 20 years experience, I sometimes think 'Am I qualified?'"
   - "Every successful person feels this - they just hide it better"

5. **The loneliness**
   - "As a founder, you can't always be honest with your team about fears"
   - "Your investors want confidence, not doubt"
   - "You need a peer group who gets it - that's why I'm active in founder communities"

---

## **Pathways for You - Practical Career Guide**

**A. The Korean Undergrad → Silicon Valley Playbook**

*"Let me give you the actual paths, with examples..."*

**Path 1: Big Tech Engineer (Google, Meta, Amazon, etc.)**

**The Traditional Route:**
1. **Strong CS fundamentals**
   - Data structures & algorithms (LeetCode Hard level)
   - System design (design Instagram, design Uber)
   - CS degree from top university (SKY in Korea helps, but not required)

2. **Internship is critical**
   - **How to get:**
     - Apply directly (low success rate, ~1-2%)
     - Referrals (someone inside refers you - 10x better odds)
     - Company-sponsored programs (Google STEP, Meta University)
   - **Timeline:** Apply Sep-Oct for next summer internship
   - **Competition:** You're competing with Stanford/MIT students

3. **The interview process**
   - **Online assessment** (2-3 coding problems, 90 min)
   - **Phone screen** (1 hour, 2 coding problems)
   - **Onsite** (4-5 hours, coding + system design + behavioral)
   - **Pass rate:** ~5-10% of applicants
   - **Prep time:** 3-6 months of serious LeetCode practice

4. **Visa strategy**
   - **F-1 OPT:** 1 year work authorization after graduation (3 years for STEM)
   - **H-1B lottery:** 30-40% success rate, applied in March
   - **Company must sponsor you - not all will**
   - **Reality check:** "Many Koreans return home after OPT because H-1B lottery failed"

**The Alternative Route (No US Degree):**
1. **Work in Korea first (2-3 years)**
   - Naver, Kakao, Samsung, Coupang - build strong resume
   - Get promoted to senior engineer level
   - Build portfolio of impressive projects

2. **Target L4/L5 roles (not entry-level)**
   - You need 2-5 years experience to bypass junior competition
   - Senior roles have less competition from US university grads
   - Demonstrate unique skills (e.g., Korean NLP, mobile at scale)

3. **Networking is essential**
   - Attend conferences (NeurIPS, ICML, tech meetups)
   - Contribute to open source (get noticed by maintainers at FAANG)
   - LinkedIn presence (write articles, share work)

4. **The referral game**
   - "I cannot emphasize enough: referrals are 10x more valuable than blind applications"
   - "How to get referrals: Contribute to their projects, meet at conferences, leverage alumni networks"
   - "Korean network in Silicon Valley is strong - use it (K-PAI events, Korean tech groups)"

**Path 2: AI Startup Engineer**

**Why This Might Be Better:**
- Less competition (startups hire year-round)
- More responsibility earlier (wear multiple hats)
- Equity upside (if startup succeeds)
- Visa: Still need H-1B, but some startups more flexible

**How to Find Startups:**
1. **YC companies** (Y Combinator batch companies - publicly listed)
2. **AI-focused VCs portfolio** (a16z, Sequoia, Accel - check their portfolio)
3. **AngelList, Wellfound** (job platforms for startups)
4. **Networking** (K-PAI, Korean startup communities)

**What They Look For:**
- Ship fast, learn fast (not perfectionism)
- Generalist skills (can do frontend, backend, ML, DevOps)
- Self-starter (don't need hand-holding)
- Cultural fit (mission-driven, scrappy)

**Interview Difference:**
- Less LeetCode, more "build this feature"
- Work sample (take-home project)
- Founder interview (they assess culture fit heavily)

**Path 3: Research → PhD → Research Scientist**

**When to Choose This Path:**
- You love math/theory more than building products
- You want to work on long-term, unsolved problems (AGI, reasoning, etc.)
- You're willing to spend 5-6 years on PhD
- You're okay with academic-style work (papers, conferences)

**The Process:**
1. **Undergraduate research experience**
   - Work with professors at your university
   - Publish 1-2 papers (even workshops count)
   - Get strong recommendation letters

2. **Apply to US PhD programs**
   - **Target schools:** Stanford, MIT, Berkeley, CMU, UW for AI
   - **Funded PhDs:** All reputable US CS PhDs are fully funded (~$40K/year stipend)
   - **Acceptance rate:** 5-10% for top programs

3. **During PhD: Build research reputation**
   - Publish at top conferences (NeurIPS, ICML, ICLR)
   - Internships at DeepMind, OpenAI, Anthropic (pipeline to full-time)
   - Network with researchers (they hire each other)

4. **After PhD: Research Scientist roles**
   - OpenAI, Anthropic, DeepMind, Google Brain, FAIR (Meta AI)
   - Salary: $250-400K base + equity (higher than engineer track)
   - Work: Advancing state-of-the-art (not just applying existing models)

**Path 4: Entrepreneurship (The Riskiest, Highest Upside)**

**When to Consider:**
- You have a specific problem you're obsessed with solving
- You've saved 1-2 years of runway
- You have co-founder(s) with complementary skills
- You're okay with 90% chance of failure

**Silicon Valley vs. Korea:**
- **Silicon Valley pros:**
  - Access to capital ($2M seed rounds common)
  - Ecosystem support (accelerators, mentors, talent)
  - Failure is acceptable (expected, even)
- **Silicon Valley cons:**
  - High cost of living ($3K+/month rent)
  - Visa uncertainty (H-1B, O-1, or start in Korea first)
  - Intense competition
- **Korea pros:**
  - Lower burn rate (more runway per dollar)
  - Government support (K-Startup, TIPS, etc.)
  - Local market knowledge
  - Family/friend network
- **Korea cons:**
  - Smaller VC ecosystem ($500K-$1M seed typical)
  - Risk-averse culture (failure stigmatized)
  - Talent acquisition harder (top engineers go to Naver/Kakao)

**My Recommendation:**
- **Start in Korea first** (if Korean citizen)
- Validate idea, build MVP, get first customers
- Raise small round from Korean VCs
- Then expand to US if market requires it (like Erudio Bio did)

---

**B. Skills That Matter in the AI Era**

*"Let me separate the hype from reality..."*

**TIER 1: Timeless Skills (AI Won't Replace)**

1. **Critical Thinking & Problem Decomposition**
   - "AI can code, but it can't decide what to build"
   - **Example:** "Should we build feature X or Y? What's the real user problem?"
   - **How to develop:** Case competitions, consulting, startup projects

2. **Communication & Influence**
   - "The best idea without persuasion dies"
   - "Writing, speaking, storytelling - these matter more as AI handles execution"
   - **Proof:** "Why am I here giving lectures? Because communication compounds over time"

3. **Systems Thinking**
   - "Understanding second-order effects, feedback loops, unintended consequences"
   - **Example:** "If we automate customer support, what happens to our customer data quality?"
   - **Relevant to AI:** "Knowing when AI causes more problems than it solves"

4. **Judgment & Taste**
   - "AI generates 100 design options. Who decides which is best?"
   - "This is taste - developed through experience, not algorithms"
   - **In tech:** "Code that works vs. code that's maintainable vs. code that's elegant"

5. **Building Trust & Relationships**
   - "AI can network, but it can't build deep trust"
   - "Your reputation takes 10 years to build, 10 seconds to destroy"
   - **Career advice:** "The people who help you get jobs aren't on LinkedIn - they're people you helped years ago"

**TIER 2: Valuable but Evolving**

1. **Coding Ability**
   - **Current state:** Still essential for engineers
   - **Trend:** AI copilots make you 2-5x faster
   - **Future (5-10 years):** "Coding might become like Excel - everyone does it, not just experts"
   - **What to focus on:**
     - Code review (evaluating AI-generated code)
     - System architecture (AI can't design complex systems yet)
     - Debugging production issues (requires context AI doesn't have)

2. **Data Analysis**
   - **Current:** SQL, Python, visualization still needed
   - **Trend:** "ChatGPT can write SQL queries now"
   - **What remains valuable:** "Knowing which question to ask, not just how to query"

3. **Domain Expertise**
   - **Healthcare, law, finance, semiconductors** - deep knowledge still beats general AI
   - **But:** "You need to pair it with AI skills to stay relevant"
   - **Example:** "Radiologist + AI > Radiologist alone > AI alone"

**TIER 3: Rapidly Commoditizing**

1. **Boilerplate Coding**
   - CRUD apps, API integrations, basic web dev
   - "If Copilot can do it end-to-end, it's not defensible"

2. **Generic Content Creation**
   - Blog posts, marketing copy, social media - AI does 80% of this now
   - "What remains: Brand voice, strategic messaging, original research"

3. **Basic Data Entry / Admin**
   - Already automated by RPA (Robotic Process Automation) + LLMs

**What Should You Learn Right Now?**

**For Technical Students:**
1. **Fundamentals (never obsolete):**
   - Data structures & algorithms
   - System design
   - Databases (SQL + NoSQL)
   - Networking basics

2. **AI Skills (career differentiator):**
   - Train/fine-tune models (Hugging Face, PyTorch)
   - Prompt engineering (seriously - this is a skill)
   - RAG implementation (LangChain, LlamaIndex)
   - Evaluate model outputs (know when AI is hallucinating)

3. **Product Skills (multiplier):**
   - User research (talk to 100 users)
   - A/B testing & experimentation
   - Metrics & analytics (know what moves the needle)

**For Non-Technical Students:**
1. **AI Literacy (non-negotiable):**
   - Understand what LLMs can/can't do
   - Prompt engineering for your field
   - Using AI tools (ChatGPT, Claude, Midjourney, etc.)

2. **Domain Depth (your moat):**
   - Become the expert in [industry] + AI
   - Example: "Finance expert who knows how to use AI" > "AI expert with no finance knowledge"

3. **Meta-Learning (ability to learn):**
   - "In 5 years, current tools will be obsolete"
   - "Your ability to learn the next thing is your biggest asset"

---

## **The Human Questions**

**A. "What Should Humans Do That AI Cannot?"**

*"This is the question everyone's asking. Here's my honest answer..."*

**1. Define Problems Worth Solving**
- "AI optimizes for goals you give it"
- "But who decides the goal?"
- **Example:** "Should we cure cancer or should we extend human lifespan? AI can help with both, but can't choose for you"
- **In your career:** "What problem do you want to spend 10 years solving? AI can't answer that."

**2. Navigate Ambiguity & Complexity**
- "AI is trained on past data → good at known patterns"
- "But new problems have no patterns yet"
- **Example:** "How should society regulate AI? No historical precedent, AI can't help"
- **In startups:** "Should we pivot or persevere? AI can give you data, but you decide"

**3. Synthesize Across Domains**
- "The best insights come from combining unrelated fields"
- **My example:** "Convex optimization (math) + Semiconductors (engineering) + AI (CS) + Bio (medicine) = Erudio Bio"
- "AI knows each domain separately, but can't make the creative leap"

**4. Provide Empathy & Ethical Judgment**
- "AI can simulate empathy, but doesn't feel it"
- **Healthcare:** "Should we tell this patient their prognosis? AI can't make that call"
- **Business:** "Should we lay off 100 people or take pay cuts across the board? AI can't judge"

**5. Build Meaning & Purpose**
- "Humans need purpose, AI doesn't"
- "The question isn't 'What job won't AI take?' but 'What gives you meaning?'"
- **My answer:** "I don't optimize for money - I optimize for impact and learning"

**B. Interactive Exercise: Your AI Strategy**

*"Let's get practical. Take 15 minutes with your neighbor..."*

**Worksheet:**

1. **Where are you now?**
   - Major:
   - Year:
   - Career interests:

2. **In your field, what are 3 tasks AI will likely automate in 5 years?**
   - Task 1:
   - Task 2:
   - Task 3:

3. **What skills can you develop now that will remain valuable?**
   - Skill 1:
   - Skill 2:
   - Skill 3:

4. **How can you use AI as a tool (not a replacement) to amplify your work?**
   - Use case 1:
   - Use case 2:

5. **What's one action you'll take this week to adapt?**
   - Action:

**Debrief Discussion:**
- "Share your most interesting insight"
- "What surprised you when you thought about it?"
- "Who's willing to share their action item?"

---

**C. Final Q&A - No Holds Barred**

*"I've shared a lot. Now it's your turn - ask me anything..."*

**Likely Questions to Prepare For:**

1. **"Do you ever regret leaving a stable career for startups?"**
   - **Honest answer:** "Yes, sometimes. Especially when I have 0 balance in my bank account. But - if I'd stayed, I'd regret not trying more."

2. **"What if I'm not sure if I'm good enough for Silicon Valley?"**
   - "No one feels 'good enough.' Impostor syndrome is universal. But - you'll never know unless you try. Apply, fail, learn, repeat."

3. **"Should I learn AI deeply or use it as a tool?"**
   - "Depends on your goal. Want to be an AI researcher? Go deep. Want to use AI in [other field]? Learn enough to use effectively, but go deep in that field."

4. **"How do I balance learning AI vs. my major?"**
   - "Don't abandon your major. The value is AI + [your major], not AI alone. Spend 70% on major, 30% on AI skills."

5. **"What would you do if you were a CS undergrad today?"**
   - "Build stuff. Don't just take classes. Build 10 projects in 2 years. Contribute to open source. Start a YouTube channel explaining AI concepts. Ship, ship, ship."

6. **"Is it too late to start? Everyone seems ahead of me."**
   - "I started my first company at 35. You're never behind. The people who seem ahead just started earlier - but they don't have more hours in a day than you."

7. **"What if AI makes my job obsolete before I even start?"**
   - "Then you adapt. The skills I learned in semiconductors became obsolete, so I learned AI. Then I'll learn the next thing. Adaptability > any specific skill."

8. **"How do you deal with burnout?"**
   - "I don't always. Sometimes I just push through. But - I take one day a month to do nothing. Piano helps. Friends help. Admitting you're struggling helps."

9. **"Do you think AI will ever be conscious?"**
   - "Philosophically interesting, practically irrelevant. Whether AI is 'conscious' doesn't change how we should use it responsibly. Let's focus on what we can control."

10. **"What keeps you going when things are hard?"**
    - "Two things: (1) The problems I'm solving matter. (2) I'd rather fail at something meaningful than succeed at something trivial."

---

**Closing (5 minutes):**

*"I want to leave you with one final thought..."*

"AI is the most powerful tool humanity has ever created. But like all tools, it amplifies human intention.

If you use it to replace your thinking - you'll become dependent and weak.

If you use it to augment your thinking - you'll become powerful beyond what was possible before.

The AI era isn't about humans vs. machines. It's about humans WITH machines vs. the status quo.

Your generation will decide what we build with this technology. Choose wisely. Build responsibly. And never stop asking 'Just because we can, should we?'

Thank you for your attention, your curiosity, and your thoughtful questions these past weeks. I'm excited to see what you'll build.

Stay in touch. I'm here if you need advice, connections, or just someone to talk to about this crazy AI journey."

---

# Summary of 3-Lecture Arc

**Lecture 6:** Technical depth - How AI actually works in production (RAG, Agents, Multimodal)

**Lecture 7:** Business perspective - How technology becomes value (models, go-to-market, fundraising)

**Lecture 8:** Personal/career - Real stories, pathways, human capabilities in AI era

**Total estimated time:** ~3.5-4 hours per lecture (with breaks), heavily interactive, discussion-based.


