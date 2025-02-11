---
title: The Real AI Revolution Isn't About AI &ndash; It's About Data
date: Mon Feb 10 01:16:52 PST 2025
last_modified_at: Tue Feb 11 03:38:54 PST 2025
permalink: /ai/data
categories:
 - blog
tags:
 - AI
 - technology
 - data
toc: true
toc_label: "ToC"
toc_icon: "cog"
toc_sticky: true
usemathjax: true  # Add this line
---

<!--tags: {% for tag in page.tags %} <a href="/tags/#{{ tag }}">{{ tag }}</a> {% endfor %}
<br>
cats: {% for category in page.categories %} <a href="/categories/#{{ category }}">{{ category }}</a> {% endfor %}-->

posted: {{ page.date| date: "%d-%b-%Y" }}
&amp;
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

<blockquote>
&hellip;
the next competitive battlefield isn't in developing better base AI models,
but in effectively combining them with domain-specific data through technologies like RAG and vector databases.
</blockquote>

<blockquote>
This evolutionary chain
&ndash; represented by keywords from Big Data to Deep Learning, then to LLMs &amp; genAI, and now to AI agents
&ndash; represents more than just a progression of buzzwords.
Each transition signifies a fundamental leap in our ability to solve complex problems with machines,
redefining the boundaries of AI.
</blockquote>

<blockquote>
The future belongs not to those who can build the biggest models,
but to those who can most effectively organize and leverage their domain-specific data.
</blockquote>

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

This intersection of theoretical mathematics and practical engineering would shape my entire career trajectory,
beginning with my role at Samsung Electronics in December 2004.
(I should note that this position also served as my mandatory military service, as the research center was government-designated.)
At Samsung, I developed numerous optimization tools that dramatically improved productivity across semiconductor chip design,
manufacturing processes, and testing operations.

# The Industrial Impact &ndash; Optimization at Scale

Among hundreds of projects, here I will just state the first three that came to my mind.
The first was a comprehensive circuit optimization tool that could simultaneously optimize hundreds of parameters
to optimize tens of objectives such as power consumption, delay times, circuit area, and signal duties.
While (psychologists proved) humans can optimize at most 5 or 6 parameters at the same time,
this tool could optimize hundreds of parameters to find the *true* optimum.

The second project revolutionized
the next-generation DRAM cell scheme design by replacing intuition-based approaches with mathematically proven optimal solutions.
Instead of relying solely on the experience of seasoned engineers with decades of expertise,
&mdash;which, by the way, was amazing beyond my pure imagination&mdash;
we could now computationally determine the optimal cell scheme for next-generation DRAM products
&ndash; a crucial capability that could make or break years of global business strategy,
hence translated into tremendous amount of monetary value.
The impact of this work resonated years later when I was being vetted for the role of founder
and CTO of [Gauss Labs, Inc.](https://www.gausslabs.ai/), SK Hynix's industrial AI spin-off,
so I head from the Vice Chair of SK Group,
which is one of the largest conglomerates of South Korea.

The third project was perhaps the most forward-looking: a general-purpose machine learning (ML)
and optimization software platform dubbed *iOpt*
&ndash;
yes, I was so into Apple products at that time,
no other principal engineers or managers use iPhones at work,
others showed their loyalty by using Galaxy phones,
but I rebelliously used iPhones *AND* named
my proud ML and optimization software platform iOpt!
&ndash;
that compressed months-long projects
into weeks by automatically modeling problems mathematically and finding optimal solutions.
This work, though we didn't realize it at the time, was already laying the groundwork for what would become modern AI applications.

# The Rise of Machine Learning, hence AI

Around 2010, terms like "big data" and "ML" began emerging in technical discussions.
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

# The Acceleration &ndash; From Transformers to AI Agents

The pace of innovation continued to accelerate.
Shortly after I joined Amazon,
a bunch of Googlers published their landmark paper "Attention is All You Need," introducing the Transformer architecture.
The paper's ambitious title proved prophetic - Transformers began outperforming previous sequence models almost immediately,
long before ChatGPT would bring this technology into the mainstream in 2022.
Then the era of LLMs and genAI began
where LLM stands for a large language model and genAI for generative AI.
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

This evolutionary chain
&ndash; represented by keywords from Big Data to Deep Learning, then to LLMs &amp; genAI, and now to AI agents
&ndash; represents more than just a progression of buzzwords.
Each transition marked a fundamental shift in how we approach problem-solving with machines as well as the progress of AI technology.
While the technical details of each breakthrough could fill volumes (and perhaps will in future posts),
what's crucial for today's business leaders is understanding the practical implications of this rapid technological acceleration.
As someone who has straddled both the theoretical foundations and practical applications of these technologies,
I want to offer a strategic perspective for business owners navigating the AI landscape
&ndash; especially those looking to integrate or build upon these transformative technologies.
The insights I'll share next come from witnessing firsthand how mathematical theories transform into market-moving innovations.

This evolutionary chain
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

# The Commoditization of AI Technology

What we're witnessing now in the AI landscape might seem like an endless frontier of innovation, but a crucial pattern is emerging. The core AI technologies - from LLMs to generative AI models to AI agents - are rapidly becoming commoditized. This isn't to diminish their revolutionary impact, but rather to highlight an important reality:
<!--these technologies are increasingly becoming table stakes rather than differentiators.-->
mastery of these AI technologies is no longer a differentiator but a baseline requirement for competition.
<!--what was once cutting-edge AI technology is now becoming as fundamental as electricity - necessary but no longer sufficient for success.-->

Consider the current state of LLMs. While OpenAI, Anthropic, and Google made headlines with their initial releases, we're now seeing capable models emerge from smaller players like Mistral AI &amp; DeepSeek and even open-source initiatives. The barrier to entry isn't necessarily technical knowledge anymore - it's computational resources and, more importantly, <font class="emph">data!
&ndash; together with differentiated insight and experience
with domain knowledge or subject matter expertises!</font>

# The Real Competitive Advantage &ndash; RAG and Domain Knowledge

This brings us to a crucial insight that many businesses are overlooking:
the next competitive battlefield isn't in developing better base AI models,
but in effectively combining them with domain-specific data through technologies like RAG and vector databases.
Only a handful of companies have the resources to compete in developing fundamental AI technologies
(for obvious reasons &hellip; money! No, enormous amount of money, that is, investment!).
For everyone else, the real opportunity lies in how they structure, store, and leverage their proprietary data.

RAG has emerged as a perfect example of this shift. By combining the general capabilities of LLMs with domain-specific knowledge stored in vector databases, organizations can create AI applications that are both powerful and uniquely tailored to their needs. This approach doesn't require building new foundation models - instead, it focuses on what organizations already have or <font class="emph">even better, startup companies can collect or generate! &ndash; their proprietary data and domain expertise.</font>

The true value will come from companies that can:

- Transform their domain expertise into well-structured vector databases
- Implement effective RAG systems that combine this proprietary data with existing LLMs
- Continuously refine and update their knowledge bases with fresh, relevant data
- Build domain-specific applications that leverage these enhanced capabilities

# Looking Ahead &ndash; The Data-First Future

Think about healthcare providers using RAG systems to augment LLMs with their extensive medical databases,
or manufacturing companies vectorizing decades of engineering documentation and process data.
The winners won't be those who build their own LLMs from scratch,
but those who can effectively organize and leverage their unique data assets through technologies like vector databases and RAG.

As someone who has witnessed the evolution from basic optimization problems to today's AI landscape,
I can say with confidence that we're approaching an inflection point.
Just as my work at Samsung showed how domain-specific optimization could transform semiconductor design,
the next wave of innovation will come from those
who can effectively combine general-purpose AI with their specialized knowledge bases.

For business leaders, this means shifting focus from trying to compete on AI model development to investing in:

- Robust data infrastructure, including vector database implementations
- Effective RAG architectures that can leverage existing LLMs
- Tools and processes for maintaining and updating knowledge bases
- Expertise in combining domain knowledge with AI capabilities

The future belongs not to those who can build the biggest models,
but to those who can most effectively organize and leverage their domain-specific data.
In this new landscape,
having a well-structured vector database of proprietary knowledge
combined with effective RAG implementations will be more valuable than having the latest AI model.

<!--Now lastly! This really leads to the opening of the era of Private AI!,
but again more on this in one of my future blogs!-->

<br>
[Sunghee Yun](/)
<br>
<br>
Mathematician, Statistician, Theorist, Futurologist, and Digital Philosopher

