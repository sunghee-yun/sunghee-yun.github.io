---
layout: single
title: Papers
permalink: /papers
toc: true
toc_label: "ToC"
toc_icon: "cog"
toc_sticky: true
---

<head>
	<link rel="stylesheet" href="/resource/styles.css">
</head>

<h1 id="ai">AI</h1>

<h2 id="llm">LLM</h2>

<ul>
<li>
	<a href="https://arxiv.org/abs/2409.12183">
		To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning
		(18-Sep-2024)
	</a>
	&nbsp;
	<div class="foldable-toggle">abstract</div>
	<div class="foldable-content">
		<p>
		Chain-of-thought (CoT) via prompting is the de facto method for eliciting reasoning capabilities from large language models (LLMs). But for what kinds of tasks is this extra "thinking" really helpful? To analyze this, we conducted a quantitative meta-analysis covering over 100 papers using CoT and ran our own evaluations of 20 datasets across 14 models. Our results show that CoT gives strong performance benefits primarily on tasks involving math or logic, with much smaller gains on other types of tasks. On MMLU, directly generating the answer without CoT leads to almost identical accuracy as CoT unless the question or model's response contains an equals sign, indicating symbolic operations and reasoning. Following this finding, we analyze the behavior of CoT on these problems by separating planning and execution and comparing against tool-augmented LLMs. Much of CoT's gain comes from improving symbolic execution, but it underperforms relative to using a symbolic solver. Our results indicate that CoT can be applied selectively, maintaining performance while saving inference costs. Furthermore, they suggest a need to move beyond prompt-based CoT to new paradigms that better leverage intermediate computation across the whole range of LLM applications.
		</p>
	</div>
</li>
<li>
	<a href="https://arxiv.org/abs/2409.05152">
		OneGen: Efficient One-Pass Unified Generation and Retrieval for LLMs
		(08-Sep-2024)
	</a>
</li>
<li>
	<a href="https://arxiv.org/abs/2407.06023">
		"Distilling System 2 into System 1"
		- Ping Yu, Jing Xu, Jason Weston, Ilia Kulikov (META Fair)
		(24-Jul-2024)
	</a>
</li>
<li>
	<a href="https://arxiv.org/abs/2407.10817">
		"Foundational Autoraters: Taming Large Language Models for Better Automatic Evaluation"
		- Tu Vu, Kalpesh Krishna, Salaheddin Alzubi, Chris Tar, Manaal Faruqui, Yun-Hsuan Sung
		@ Google, Google DeepMind &amp; UMass Amherst
		(15-Jul-2024)
	</a></li>
</ul>

<h2 id="slm">SLM</h2>

<ul>
<li>
	<a href="https://www.marktechpost.com/2024/09/18/mistral-ai-released-mistral-small-instruct-2409-a-game-changing-open-source-language-model-empowering-versatile-ai-applications-with-unmatched-efficiency-and-accessibility/?amp">
		Mistral AI Released Mistral-Small-Instruct-2409: A Game-Changing Open-Source Language Model Empowering Versatile AI Applications with Unmatched Efficiency and Accessibility
		(18-Sep-2024)
	</a>
	&nbsp;
	(<a href="https://huggingface.co/mistralai/Mistral-Small-Instruct-2409">model card</a>)
</li>
<li>
	<a href="https://arxiv.org/abs/2409.00608">
		TinyAgent: Function Calling at the Edge
		(01-Sep-2024)
	</a>
	&nbsp;
	<div class="foldable-toggle">abstract</div>
	<div class="foldable-content">
		<p>Recent large language models (LLMs) have enabled the development of advanced agentic systems that can integrate various tools and APIs to fulfill user queries through function calling. However, the deployment of these LLMs on the edge has not been explored since they typically require cloud-based infrastructure due to their substantial model size and computational demands. To this end, we present TinyAgent, an end-to-end framework for training and deploying task-specific small language model agents capable of function calling for driving agentic systems at the edge. We first show how to enable accurate function calling for open-source models via the LLMCompiler framework. We then systematically curate a high-quality dataset for function calling, which we use to fine-tune two small language models, TinyAgent-1.1B and 7B. For efficient inference, we introduce a novel tool retrieval method to reduce the input prompt length and utilize quantization to further accelerate the inference speed. As a driving application, we demonstrate a local Siri-like system for Apple's MacBook that can execute user commands through text or voice input. Our results show that our models can achieve, and even surpass, the function-calling capabilities of larger models like GPT-4-Turbo, while being fully deployed at the edge. We open-source our dataset, models, and installable package and provide a demo video for our MacBook assistant agent.</p>
	</div>
</li>
</ul>

<h2 id="cv">computer vision</h2>

<ul>
<li>
	<a href="https://arxiv.org/abs/2407.13517">
		"Mask2Map: Vectorized HD Map Construction Using Bird's Eye View Segmentation Masks"
		-
		Sehwan Choi, Jungho Kim, Hongjae Shin, Jun Won Choi @ Hanyang Univ. & SNU
		(18-Jul-2024)
	</a>
</li>
</ul>

<script>
	document.addEventListener('DOMContentLoaded', function() {
		var toggles = document.querySelectorAll('.foldable-toggle');

		toggles.forEach(function(toggle) {
			toggle.addEventListener('click', function() {
				this.classList.toggle('active');
				var content = this.nextElementSibling;
				if (content.style.display === 'block') {
					content.style.display = 'none';
				} else {
					content.style.display = 'block';
				}
			});
		});
	});
</script>

