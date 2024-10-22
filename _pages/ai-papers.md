---
layout: single
title: Welcome to My AI Papers Hub
permalink: /papers
toc: true
toc_label: "ToC"
toc_icon: "cog"
toc_sticky: true
---

<head>
<link href="/resource/styles.css" rel="stylesheet"/>
</head>

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
</script><a href="#all-papers-in-reverse-chronological-order">All papers in reverse chronological order</a>

<h1 id="ai">AI</h1>


<h2 id="ai-dl-models">DL models</h2>

<ul>
<li>
	"Robust flight navigation out of distribution with liquid neural networks"
	@ 19-Apr-2023
	(<a href="https://www.science.org/doi/10.1126/scirobotics.adc8892">ScienceRobotics</a>)
</li>
</ul>

<h2 id="ai-llm">LLM</h2>

<ul>
<li>
	"To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning arxiv"
	@ 18-Sep-2024
	(<a href="https://arxiv.org/abs/2409.12183">arxiv</a>)
	&nbsp;
	<div class="foldable-toggle">abstract</div>
	<div class="foldable-content">
	<p>
	Chain-of-thought (CoT) via prompting is the de facto method
	 for eliciting reasoning capabilities from large language models (LLMs).
	 But for what kinds of tasks is this extra "thinking" really helpful?
	 To analyze this, we conducted a quantitative meta-analysis covering over 100 papers
	 using CoT and ran our own evaluations of 20 datasets across 14 models.
	 Our results show that CoT gives strong performance benefits primarily
	 on tasks involving math or logic, with much smaller gains on other types of tasks.
	 On MMLU, directly generating the answer without CoT leads
	 to almost identical accuracy as CoT unless the question or model's response
	 contains an equals sign, indicating symbolic operations and reasoning.
	 Following this finding, we analyze the behavior of CoT on these problems
	 by separating planning and execution and comparing against tool-augmented LLMs.
	 Much of CoT's gain comes from improving symbolic execution,
	 but it underperforms relative to using a symbolic solver.
	 Our results indicate that CoT can be applied selectively,
	 maintaining performance while saving inference costs.
	 Furthermore, they suggest a need to move beyond prompt-based CoT to new paradigms
	 that better leverage intermediate computation
	 across the whole range of LLM applications.
	</p>
	</div>
</li>
<li>
	"OneGen: Efficient One-Pass Unified Generation and Retrieval for LLMs arxiv"
	@ 08-Sep-2024
	(<a href="https://arxiv.org/abs/2409.05152">arxiv</a>)
</li>
<li>
	"Distilling System 2 into System 1"
	- Ping Yu, Jing Xu, Jason Weston &amp; Ilia Kulikov
	(META Fair)
	@ 24-Jul-2024
	(<a href="https://arxiv.org/abs/2407.06023">arxiv</a>)
</li>
<li>
	"Foundational Autoraters: Taming Large Language Models for Better Automatic Evaluation"
	- Tu Vu, Kalpesh Krishna, Salaheddin Alzubi, Chris Tar, Manaal Faruqui &amp; Yun-Hsuan Sung
	(Google, Google DeepMind &amp; UMass Amherst)
	@ 15-Jul-2024
	(<a href="https://arxiv.org/abs/2407.10817">arxiv</a>)
</li>
</ul>

<h2 id="ai-slm">SLM</h2>

<ul>
<li>
	"Mistral AI Released Mistral-Small-Instruct-2409: A Game-Changing Open-Source Language Model Empowering Versatile AI Applications with Unmatched Efficiency and Accessibility"
	@ 18-Sep-2024
	(<a href="https://www.marktechpost.com/2024/09/18/mistral-ai-released-mistral-small-instruct-2409-a-game-changing-open-source-language-model-empowering-versatile-ai-applications-with-unmatched-efficiency-and-accessibility/?amp">MarkTechPost</a>, <a href="https://huggingface.co/mistralai/Mistral-Small-Instruct-2409">model card</a>)
</li>
</ul>

<h2 id="ai-cv">CV</h2>

<ul>
<li>
	"Mask2Map: Vectorized HD Map Construction Using Bird's Eye View Segmentation Masks"
	- Sehwan Choi, Jungho Kim, Hongjae Shin &amp; Jun Won Choi
	(Hanyang University &amp; SNU)
	@ 18-Jul-2024
</li>
</ul>
<h1 id="all-papers-in-reverse-chronological-order">All papers in reverse chronological order</h1>
<ul>
<li>
	"To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning arxiv"
	@ 18-Sep-2024
	(<a href="https://arxiv.org/abs/2409.12183">arxiv</a>)
	&nbsp;
	<div class="foldable-toggle">abstract</div>
	<div class="foldable-content">
	<p>
	Chain-of-thought (CoT) via prompting is the de facto method
	 for eliciting reasoning capabilities from large language models (LLMs).
	 But for what kinds of tasks is this extra "thinking" really helpful?
	 To analyze this, we conducted a quantitative meta-analysis covering over 100 papers
	 using CoT and ran our own evaluations of 20 datasets across 14 models.
	 Our results show that CoT gives strong performance benefits primarily
	 on tasks involving math or logic, with much smaller gains on other types of tasks.
	 On MMLU, directly generating the answer without CoT leads
	 to almost identical accuracy as CoT unless the question or model's response
	 contains an equals sign, indicating symbolic operations and reasoning.
	 Following this finding, we analyze the behavior of CoT on these problems
	 by separating planning and execution and comparing against tool-augmented LLMs.
	 Much of CoT's gain comes from improving symbolic execution,
	 but it underperforms relative to using a symbolic solver.
	 Our results indicate that CoT can be applied selectively,
	 maintaining performance while saving inference costs.
	 Furthermore, they suggest a need to move beyond prompt-based CoT to new paradigms
	 that better leverage intermediate computation
	 across the whole range of LLM applications.
	</p>
	</div>
</li>
<li>
	"Mistral AI Released Mistral-Small-Instruct-2409: A Game-Changing Open-Source Language Model Empowering Versatile AI Applications with Unmatched Efficiency and Accessibility"
	@ 18-Sep-2024
	(<a href="https://www.marktechpost.com/2024/09/18/mistral-ai-released-mistral-small-instruct-2409-a-game-changing-open-source-language-model-empowering-versatile-ai-applications-with-unmatched-efficiency-and-accessibility/?amp">MarkTechPost</a>, <a href="https://huggingface.co/mistralai/Mistral-Small-Instruct-2409">model card</a>)
</li>
<li>
	"OneGen: Efficient One-Pass Unified Generation and Retrieval for LLMs arxiv"
	@ 08-Sep-2024
	(<a href="https://arxiv.org/abs/2409.05152">arxiv</a>)
</li>
<li>
	"Distilling System 2 into System 1"
	- Ping Yu, Jing Xu, Jason Weston &amp; Ilia Kulikov
	(META Fair)
	@ 24-Jul-2024
	(<a href="https://arxiv.org/abs/2407.06023">arxiv</a>)
</li>
<li>
	"Mask2Map: Vectorized HD Map Construction Using Bird's Eye View Segmentation Masks"
	- Sehwan Choi, Jungho Kim, Hongjae Shin &amp; Jun Won Choi
	(Hanyang University &amp; SNU)
	@ 18-Jul-2024
</li>
<li>
	"Foundational Autoraters: Taming Large Language Models for Better Automatic Evaluation"
	- Tu Vu, Kalpesh Krishna, Salaheddin Alzubi, Chris Tar, Manaal Faruqui &amp; Yun-Hsuan Sung
	(Google, Google DeepMind &amp; UMass Amherst)
	@ 15-Jul-2024
	(<a href="https://arxiv.org/abs/2407.10817">arxiv</a>)
</li>
<li>
	"Robust flight navigation out of distribution with liquid neural networks"
	@ 19-Apr-2023
	(<a href="https://www.science.org/doi/10.1126/scirobotics.adc8892">ScienceRobotics</a>)
</li>
</ul>
