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
	</a>
	<div class="foldable-toggle">abstract</div>
	<div class="foldable-content">
		<p>
		Chain-of-thought (CoT) via prompting is the de facto method for eliciting reasoning capabilities from large language models (LLMs). But for what kinds of tasks is this extra "thinking" really helpful? To analyze this, we conducted a quantitative meta-analysis covering over 100 papers using CoT and ran our own evaluations of 20 datasets across 14 models. Our results show that CoT gives strong performance benefits primarily on tasks involving math or logic, with much smaller gains on other types of tasks. On MMLU, directly generating the answer without CoT leads to almost identical accuracy as CoT unless the question or model's response contains an equals sign, indicating symbolic operations and reasoning. Following this finding, we analyze the behavior of CoT on these problems by separating planning and execution and comparing against tool-augmented LLMs. Much of CoT's gain comes from improving symbolic execution, but it underperforms relative to using a symbolic solver. Our results indicate that CoT can be applied selectively, maintaining performance while saving inference costs. Furthermore, they suggest a need to move beyond prompt-based CoT to new paradigms that better leverage intermediate computation across the whole range of LLM applications.
		</p>
    </div>
</li>
<li>
	"Distilling System 2 into System 1"
	-
	Ping Yu, Jing Xu, Jason Weston, Ilia Kulikov
	(META Fair)
	<a href="https://arxiv.org/abs/2407.06023">
	arXiv
	</a>
</li>
<li>
	"Foundational Autoraters: Taming Large Language Models for Better Automatic Evaluation"
	-
	Tu Vu, Kalpesh Krishna, Salaheddin Alzubi, Chris Tar, Manaal Faruqui, Yun-Hsuan Sung
	@ Google, Google DeepMind &amp; UMass Amherst
	<a href="https://arxiv.org/abs/2407.10817">
	arXiv
	</a></li>
</ul>

<h2 id="cv">computer vision</h2>

<ul>
<li>
	"Mask2Map: Vectorized HD Map Construction Using Bird's Eye View Segmentation Masks"
	-
	Sehwan Choi, Jungho Kim, Hongjae Shin, Jun Won Choi
	@ Hanyang Univ. & SNU
	<a href="https://arxiv.org/abs/2407.13517">
	arXiv
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

