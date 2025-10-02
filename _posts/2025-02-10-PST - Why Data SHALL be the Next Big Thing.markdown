---
title: Beyond Models &ndash; Why Domain Insight and Quality Data Will Define AI's Future
date: Mon Feb 10 01:16:52 PST 2025
last_modified_at: Thu Oct  2 10:41:05 PDT 2025
permalink: /ai/data
categories:
 - blog
 - AI
tags:
 - AI
 - technology
 - data
toc: true
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
---

posted: {{ page.date| date: "%d-%b-%Y" }}
&amp;
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

<blockquote>
&hellip;
<font class="emph">the next competitive battlefield isn't in developing better base AI models,
but in effectively combining them with domain-specific data through technologies like RAG and vector databases.</font>
</blockquote>

<blockquote>
<font class="emph">This evolutionary chain
&ndash; represented by keywords from Big Data to Deep Learning, then to LLMs &amp; genAI, and now to AI agents
&ndash; represents more than just a progression of buzzwords.
Each transition signifies a fundamental leap in our ability to solve complex problems with machines,
redefining the boundaries of AI.</font>
</blockquote>

<blockquote>
<font class="emph">The future belongs not to those who can build the biggest models,
but to those who can most effectively organize and leverage their domain-specific data.</font>
</blockquote>

# NotebookLM Podcasts

<audio id="podcast-1" controls>
	<source type="audio/wav" src="https://snuee94.github.io/resource/posts/2025-02-10-PST - Why Data SHALL be the Next Big Thing/NotebookLM/Beyond Models_ Data and Domain Define AI's Future-01.wav">
	Your browser does not support this shorter audio element.
</audio>

# From Mathematical Foundations to AI Revolution

In 2004, when I completed my PhD under the supervision of one of optimization theory's most brilliant minds,
few could have predicted how optimization mathematics would become the backbone of today's AI revolution.
Yet looking back,
the threads connecting advanced mathematics to modern artificial intelligence (AI)
were already being woven in the halls of Stanford's Engineering department.

I earned my PhD in Electrical Engineering under [Professor Stephen P. Boyd](https://stanford.edu/~boyd/),
arguably the most influential figure in the field of convex optimization
&ndash; the mathematical discipline that would later provide the foundational framework for all modern AI algorithms.
While many of my EE colleagues focused on semiconductor design, I was drawn to the pure mathematical beauty of optimization theory.
Finding [Prof. Boyd](https://stanford.edu/~boyd/) at Stanford rather than MIT or Caltech
was one of the most fortuitous accidents of my academic career.
Though my passion was mathematics, I still needed to ground my work in electrical engineering,
which led me to focus my thesis on "power and delay optimization of digital logic circuits using convex optimization."

<div class="img-container">
<img style="max-width: 80%;" src="/resource/posts/2025-02-10-PST - Why Data SHALL be the Next Big Thing/u1564158738_From_Mathematical_Foundations_to_AI_RevolutionPer_ea6dd357-674a-4505-9db5-996265e8b093_2.png">
</div>

This intersection of theoretical mathematics and practical engineering would shape my entire career trajectory, beginning with my role at Samsung Electronics in December 2004. This position also served as my mandatory military service, as the research center was government-designated. At Samsung, I developed numerous optimization tools that dramatically improved productivity across semiconductor chip design, manufacturing processes, and testing operations.

# The Industrial Impact &ndash; Optimization at Scale

Among hundreds of projects, here I will just state the first three that came to my mind now.
The first was a comprehensive circuit optimization tool that could simultaneously optimize hundreds of parameters
to optimize tens of objectives such as power consumption, delay times, circuit area, and signal duties.
While (psychologists proved) humans can optimize at most 5 or 6 parameters at the same time,
this tool could optimize hundreds of parameters to find the *true* optimum.

The second project revolutionized the next-generation DRAM cell scheme design by replacing intuition-based approaches with mathematically proven optimal solutions. Instead of relying solely on the experience of seasoned engineers with decades of expertise—which was amazing beyond my pure imagination—we could now computationally determine the optimal cell scheme for next-generation DRAM products. This capability could make or break years of global business strategy, translating into tremendous monetary value. The impact of this work resonated years later when I was being vetted for the role of founder and CTO of [Gauss Labs, Inc.](https://www.gausslabs.ai/), SK Hynix's industrial AI spin-off, as I heard from the Vice Chair of SK Group, one of the largest conglomerates of South Korea.

<div class="img-container">
<!--img style="max-width: 80%;" src="/resource/posts/2025-02-10-PST - Why Data SHALL be the Next Big Thing/u1564158738_The_Industrial_Impact__Optimization_at_ScalePerma_24d8c32b-7495-482b-b72a-fd79a13cf5ab_1.png"-->
<img style="max-width: 80%;" src="/resource/posts/2025-02-10-PST - Why Data SHALL be the Next Big Thing/u1564158738_The_first_was_a_comprehensive_circuit_optimizatio_ead44627-e1f0-4125-b295-89fd6629b429_0.png">
</div>

The third project was perhaps the most forward-looking: a general-purpose machine learning (ML)
and optimization software platform dubbed *iOpt*
&ndash;
yes, I was so into Apple products at that time,
no other principal engineers or managers dared to use iPhones at work;
they showed their loyalty by using Galaxy phones,
but I rebelliously used iPhones *AND* named
my proud ML and optimization software platform iOpt!
&ndash;
This platform compressed months-long projects into weeks by automatically modeling problems mathematically and finding optimal solutions.
This work, though we didn't realize it at the time, was already laying the groundwork for what would become modern AI applications.

# The Rise of Machine Learning, hence the Rise of AI

<!--Around 2010, terms like "big data" and "ML" began emerging in technical discussions.
I distinctly remember [Prof. Boyd](https://stanford.edu/~boyd/) advising me to explore the potential of machine learning
&ndash; advice that initially puzzled me but now seems prescient.
While most of us were still focused on traditional optimization problems,
he had already recognized that ML would transform the technology landscape;
probably anyone in Silicon Valley would've done it.
The transformation accelerated in 2012 with the rise of deep learning,
marked by AlexNet's revolutionary performance at the ImageNet Large-Scale Visual Recognition Challenges (ILSVRC).
AlexNet demonstrated that deep neural networks could finally outperform human-engineered features
in computer vision, opening the floodgates
for applications in image generation, recognition, classification, and recommendation systems.
It was Hinton's life-long master piece,
which was the product of his life-long patience even under
people's mockings that neural network does NOT work!
-->

<!--Around 2010, terms like "big data" and "ML" began emerging in technical discussions. I distinctly remember Prof. Boyd advising me to explore the potential of machine learning – advice that initially puzzled me but now seems prescient. While most of us were still focused on traditional optimization problems, he had already recognized that ML would transform the technology landscape. The transformation accelerated in 2012 with the rise of deep learning, marked by AlexNet's revolutionary performance at the ImageNet Large-Scale Visual Recognition Challenges (ILSVRC). AlexNet demonstrated that deep neural networks could finally outperform human-engineered features in computer vision, opening the floodgates for applications in image generation, recognition, classification, and recommendation systems. It was Hinton's life-long masterpiece, which was the product of his life-long patience even under people's mockings that neural networks do NOT work!-->

Around 2010, terms like "big data" and "ML" began emerging in technical discussions.
I distinctly remember Prof. Boyd advising me to explore the potential of machine learning
&ndash; advice that initially puzzled me but now seems prescient.
While most of us were still focused on traditional optimization and engineering problems,
he had already recognized that ML would transform the technology landscape.
The transformation accelerated in 2012 with the rise of deep learning,
marked by AlexNet's revolutionary performance at the ImageNet Large-Scale Visual Recognition Challenge (ILSVRC).
This breakthrough represented the culmination of Geoffrey Hinton's decades-long work on neural networks,
validating his unwavering belief in their potential despite widespread skepticism.
AlexNet demonstrated that deep neural networks could finally outperform human-engineered features in computer vision,
opening the floodgates for applications in image generation, recognition, classification, and recommendation systems.
What we didn't realize then was that this breakthrough was merely a glimpse of the transformative capabilities
that would emerge in the following years.

# The Acceleration &ndash; From Transformers to AI Agents

The pace of innovation continued to accelerate.
Shortly after I joined Amazon in July, 2017,
a bunch of Googlers published their landmark paper "[Attention is All You Need](/papers#attention-is-all-you-need),"
introducing the *transformative* Transformer architecture.
The paper's ambitious title proved prophetic - Transformers began outperforming previous sequence models almost immediately,
long before ChatGPT would bring this technology into the mainstream in 2022.
Then the era of LLMs and genAI began.<sup><a href="#footnote1" id="ref1">1</a></sup>
Ever since,
there have been unprecedentedly fast development and progress
in these areas
marked by the names of new versions of products or new products
such as
AlphaFold 2,
DALL-E, DALL-E 2,
DALL-E 3,
Mistral AI,
Optimus,
GPT-4o,
Figure AI,
Claude Sonnet,
and
AlphaFold 3.
Literrally,
you would see new things coming
beating the performance of the predecessors
every week (without any bit of exeggerations).
And just months ago, I started seeing "AI agents" as new buzzwords everywhere,
marking yet another paradigm shift in how we think about artificial intelligence.

<div class="img-container">
<img src="/resource/posts/2025-02-10-PST - Why Data SHALL be the Next Big Thing/ai-history.png">
</div>

This evolutionary chain
&ndash; represented by keywords from Big Data to Deep Learning, then to LLMs &amp; genAI, and now to AI agents
&ndash; represents more than just a progression of buzzwords.
Each transition marked a fundamental shift in how we approach problem-solving with machines
as well as the progress of AI technology.
While the technical details of each breakthrough could fill volumes (and perhaps will in future posts), <font class="emph">what's
crucial for today's business leaders is understanding the practical implications of this rapid technological acceleration.</font>
As someone who has straddled both the theoretical foundations and practical applications of these technologies,
I want to offer a strategic perspective for business owners navigating the AI landscape
&ndash; especially those looking to integrate or build upon these transformative technologies.
The insights I'll share next come from witnessing firsthand how mathematical theories transform into market-moving innovations.

<!--This evolutionary chain
&ndash; from Big Data to Deep Learning, through LLMs and generative AI (genAI), and now to AI agents
&ndash; embodies more than a mere progression of industry buzzwords.
Each transition signifies a fundamental leap in our ability to solve complex problems with machines,
redefining the boundaries of AI.
While each breakthrough deserves its own technical deep-dive (which I'll explore in future posts),
what's most critical now is understanding how this accelerating technological wave is reshaping business landscapes.
Having spent my career bridging the gap between theoretical mathematics and real-world applications,
I've gained unique insights into how these technologies transform from academic concepts into market-moving innovations.
Let me share a perspective that's particularly relevant for business leaders looking to navigate
&ndash; and capitalize on &ndash; this rapidly evolving AI landscape.
-->

# The Commoditization of AI Technology

What we're witnessing now in the AI landscape might seem like an endless frontier of innovation, but a crucial pattern is emerging. The core AI technologies - from LLMs to generative AI models to AI agents - are rapidly becoming commoditized. This isn't to diminish their revolutionary impact, but rather to highlight an important reality:
<!--these technologies are increasingly becoming table stakes rather than differentiators.-->
mastery of these AI technologies is no longer a differentiator but a baseline requirement for competition.
<!--what was once cutting-edge AI technology is now becoming as fundamental as electricity - necessary but no longer sufficient for success.-->

<div class="img-container-justified">
&nbsp;
<img style="max-width: 45%;" src="/resource/posts/2025-02-10-PST - Why Data SHALL be the Next Big Thing/Gemini_Generated_Image_wpgma2wpgma2wpgm.jpeg">
<img style="max-width: 45%;" src="/resource/posts/2025-02-10-PST - Why Data SHALL be the Next Big Thing/Gemini_Generated_Image_hv95vehv95vehv95.jpeg">
&nbsp;
</div>

Consider the current state of LLMs.
While OpenAI, Anthropic, and Google made headlines with their initial releases,
we're now seeing capable models emerge from smaller players like Mistral AI &amp; DeepSeek and even open-source initiatives.
The barrier to entry isn't necessarily technical knowledge anymore, but <font class="emph">data!
&ndash; together with differentiated insight and experience
with domain knowledge or subject matter expertises!</font>

# The Real Competitive Advantage &ndash; RAG and Domain Knowledge

As someone who has witnessed firsthand the evolution from basic optimization problems to today's sophisticated AI landscape, I see a clear parallel between my early work and the current state of AI. Just as my optimization tools at Samsung gained their true value by incorporating deep domain knowledge of semiconductor design, today's most powerful AI applications will emerge from the fusion of general AI capabilities with specialized expertise.

Retrieval-Augmented Generation (RAG) represents this perfect synthesis. By combining the general capabilities of Large Language Models with domain-specific knowledge stored in vector databases, organizations can create AI applications that are both powerful and uniquely tailored to their needs. Vector databases serve as the modern equivalent of the specialized optimization constraints we used to define in my early career – they provide the crucial domain-specific boundaries that transform general-purpose tools into precision instruments.

# Looking Ahead &ndash; The Data-First Future

As I reflect on my journey from optimizing circuit parameters to witnessing the rise of autonomous AI systems, one truth becomes increasingly clear: the future belongs to those who can effectively bridge the gap between general-purpose AI and specialized domain knowledge. Just as my work at Samsung showed how domain-specific optimization could transform semiconductor design, the next wave of innovation will come from those who can effectively combine general-purpose AI with their specialized knowledge bases.

The parallels between my early career and today's AI landscape are striking. Twenty years ago, I was working to optimize hundreds of parameters simultaneously in circuit design – today, we're using similar mathematical principles to optimize billions of parameters in neural networks. The key difference is scale, not fundamental approach. This perspective gives me unique insight into where the field is heading.

For business leaders, this means shifting focus from trying to compete on AI model development to investing in:

- Robust data infrastructure, including vector database implementations
- Effective RAG architectures, both software and hardware, that can leverage existing LLMs
- Tools and processes for maintaining and updating knowledge bases
- <font class="emph">Expertise in combining domain knowledge with AI capabilities</font>

Just as my optimization work gained its true value through deep integration with semiconductor expertise, tomorrow's AI solutions will derive their power not from raw computational capability, but from their ability to meaningfully incorporate domain-specific knowledge and expertise. This is where I see the field heading – not toward bigger models, but toward smarter integration of specialized knowledge with general AI capabilities.

As I look back on my journey from pure mathematics to the frontiers of AI, I'm reminded that the most powerful innovations often come not from revolutionary new technologies, but from finding novel ways to combine existing tools with deep domain expertise. This was true in my optimization work two decades ago, and it remains true in today's AI landscape. The future belongs not to those who can build the biggest models, but to those who can most effectively bridge the gap between general AI capabilities and specialized domain knowledge.

<br>
[Sunghee Yun](/)
<br>
<br>
Mathematician, Statistician, Theorist, Futurologist, and Digital Philosopher

<hr>
<ol>
<li id="footnote1">
	LLM stands for a large language model and genAI for generative AI.
	&nbsp;<a href="#ref1">↩</a></li>
</ol>
