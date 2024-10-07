---
title: MIT-Invented Liquid Neural Networks - A Game-Changer for the Future of LLMs
date: Sun Oct  6 22:27:27 PDT 2024
last_modified_at: Mon Oct  7 00:54:33 PDT 2024
categories:
 - blog
tags:
 - AI
 - LLM
 - future
 - research
 - technology
 - energy
 - compact modeling
 - domain adaption
 - data
toc: true
toc_label: "ToC"
toc_icon: "cog"
toc_sticky: true
---

<head>
	<link rel="stylesheet" href="/resource/styles.css">
</head>

posted: {{ page.date| date: "%d-%b-%Y" }}
{: .notice--primary}


The pace of AI development, particularly in Large Language Models (LLMs), has been nothing short of extraordinary. As someone who has interacted extensively with key LLM services—Anthropic’s Claude, OpenAI’s ChatGPT, Google’s Gemini, Mistral’s Mistral, X’s Grok, and Perplexity AI—I’ve been astounded not only by their rapid advancement but by their vast capabilities. Yet, after this first-hand experience, I now believe that the impact of AI’s evolution is likely to be far greater than I originally imagined.

But for this post, I want to focus on a critical aspect of LLMs: their massive energy consumption, largely driven by the Transformer architecture that powers them. &mdash; I will write more on the topic later in other blog posts.


The amount of energy consumed by entities providing LLM services is staggering. OpenAI, for instance, reportedly loses money on each inference, even with customer charges for their advanced models. This burden, I believe, will eventually fall on small businesses relying on these APIs, leading to unsustainable costs.

Figures like Sam Altman are seeking trillions in investments to build more data centers and even semiconductor manufacturing facilities. Some have even speculated that AI’s future could rely on nuclear fusion for power. However, I don’t believe that any economy can thrive on limitless energy consumption. This path seems unsustainable, and it doesn’t take an expert to recognize that.

<h1 id="energy-dilemma">Energy dilemma</h1>

I’ve had discussions with entrepreneurs in the nuclear fusion space, and while there’s excitement, the technology isn’t commercially viable yet. The most optimistic estimates suggest it could become a reality by 2035, with some projections extending to 2050. With such uncertainty around future energy solutions, it’s imperative that AI research shifts its focus toward reducing energy consumption now.

One potential solution is model compaction—streamlining models to make them more efficient without sacrificing performance. While I can’t offer specific technical solutions here in this post, many researchers are already making strides in this area. Reducing the number of neural connections that need to be activated during each inference could be key to minimizing the energy demand.

Current LLMs excel at general natural language tasks because they’ve been trained on vast amounts of data, learning virtually every grammatical and conversational structure. But do we need this full capacity for every use case?

<h1 id="llms-in-specific-applications">LLMs in specific applications</h1>

For example, during my recent business development efforts at Erudio Bio, Inc., I spoke with several leading medical professionals at South Korea’s largest hospitals. Many expressed interest in LLMs for automating tasks like charting. While LLMs are capable of handling natural language input, do they need their full linguistic capabilities to handle something as specific as medical charting? Probably not.

This observation extends beyond the medical field. For most use cases, the extensive language understanding of LLMs is neither necessary nor sufficient. This suggests a natural evolution toward lighter models, fine-tuned for specific applications, such as charting for medical professionals.

In the coming years, data may prove even more crucial than today's impressive large language models. The growing importance of data in shaping AI capabilities will be explored further in upcoming posts.

<h1 id="lnn">Enter liquid neural networks (LNN)</h1>

This brings me to a breakthrough that could address the very issues I’ve been grappling with;
I accidentally stumbled upon this article a few days ago -
<a href="https://venturebeat.com/ai/mit-spinoff-liquid-debuts-non-transformer-ai-models-and-theyre-already-state-of-the-art/">
	MIT spinoff Liquid debuts non-transformer AI models and they’re already state-of-the-art.
</a>
Their innovative architecture doesn’t require the constant toggling of GPU circuits, as Transformers do.
&ndash; This article is in <a href="/articles#ai-llm">this list</a>, too.

The energy savings are impressive, and the speed of inference is another game-changer. - Look at below figure from the article. -
Liquid AI delivers results instantly, in stark contrast to Transformer-based models, which process tokens very slowly. - You can practically read the output as it generates
if I exaggerate (quite) a bit.

<div class="img-container">
	<img src="/assets/images/ai/llm/lfm-performance-comparison.webp">
</div>

This could very well be the solution I’ve been searching for—a more energy-efficient, faster approach to AI that doesn’t sacrifice performance. Liquid Neural Networks may hold the key to a sustainable future for LLMs, and I’m excited to see where this technology leads.


<h1 id="conclusion">Conclusion</h1>

As we continue to push the boundaries of AI capabilities, it's crucial that we also focus on making these technologies more sustainable and accessible. The Liquid Neural Network and similar innovations in model efficiency could be the solution we've been looking for, paving the way for a new generation of powerful yet energy-efficient AI systems.

In the coming years, we may see a shift towards more specialized, efficient models tailored to specific tasks, with data playing an increasingly critical role in their development and deployment. This evolution could democratize AI technology, making it more accessible to businesses and developers of all sizes.

The future of AI is not just about raw power, but about intelligent, efficient systems that can deliver amazing results without breaking the bank—or the power grid.










