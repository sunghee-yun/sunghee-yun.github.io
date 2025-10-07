---
layout: single
title: Welcome to My AI Learning Hub
permalink: /ai-learning
toc: true
toc_label: "ToC"
toc_icon: "cog"
toc_sticky: true
last_modified_at: Sun Oct  5 17:07:51 PDT 2025
---

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

# NotebookLM Podcasts

<audio id="podcast-1" controls>
	<source type="audio/wav" src="https://sungheeyun-podcasts.github.io/resource/pages/ai-learning/NotebookLM/Sunghee's AI Learning Hub-01.wav">
	Your browser does not support this shorter audio element.
</audio>

<audio id="podcast-2" controls>
	<source type="audio/wav" src="https://sungheeyun-podcasts.github.io/resource/pages/ai-learning/NotebookLM/Sunghee's AI Learning Hub-02.wav">
	Your browser does not support this shorter audio element.
</audio>

Korean versions

<audio id="podcast-kor-1" controls>
	<source type="audio/wav" src="https://sungheeyun-podcasts.github.io/resource/pages/ai-learning/NotebookLM/Sunghee's AI Learning Hub-kor-02.wav">
	Your browser does not support this shorter audio element.
</audio>

<audio id="podcast-kor-2" controls>
	<source type="audio/wav" src="https://sungheeyun-podcasts.github.io/resource/pages/ai-learning/NotebookLM/Sunghee's AI Learning Hub-kor-01.wav">
	Your browser does not support this shorter audio element.
</audio>

# Online courses {#online-course}

- [coursera](https://www.coursera.org)
- [DeepLearning.AI](https://www.deeplearning.ai/courses)

# Optimization {#opt}

## Books {#opt-books}

- Convex Optimization 1st Edition
	&nbsp;
	Stephen Boyd, Lieven Vandenberghe
	(<a href="https://www.amazon.com/Convex-Optimization-Corrections-2008-Stephen/dp/0521833787/">Amazon</a>,
	<a href="https://stanford.edu/~boyd/cvxbook/">Boyd's homepage</a>,
	<a href="/resource/books/opt/Convex Optimization - Stephen Boyd and Lieven Vandenberghe.pdf">PDF</a>)

# Machine learning {#ml}

## Books {#ml-books}

- Introduction to Applied Linear Algebra
	&nbsp;
	Stephen Boyd @ Stanford University,
	Lieven Vandenberghe @ UCLA
	(<a href="https://www.amazon.com/Introduction-Applied-Linear-Algebra-Matrices/dp/1316518965/">Amazon</a>,
	<a href="https://stanford.edu/~boyd/vmls/">Boyd's homepage</a>,
	<a href="/resource/books/AI/Introduction to Applied Linear Algebra - Stephen Boyd and Lieven Vandenberghe.pdf">PDF</a>)
- The Elements of Statistical Learning: Data Mining, Inference, and Prediction
	&nbsp;
	Trevor Hastie, Robert Tibshirani, Jerome Friedman
	(<a href="https://www.amazon.com/Elements-Statistical-Learning-Prediction-Statistics/dp/0387848576/">Amazon</a>)
	&nbsp;
	<div class="foldable-toggle">my comment</div>
	<div class="foldable-content">
	<p>
		The bible of traditional statistical learning.
		Very hard to read.
		I do not recommend for beginners.
	</p>
	<p>
		However,
		if you're versed with statistics
		and want to understand the core of (classical) theory and development,
		you may want to skim through it
		or/and use it as a reference
		for statistically or mathematically rigorous understanding of basic and advanced
		concepts such as overfitting, the expectation-maximization (EM) algorithm,
		and Bayesian inference.
	</p>
	</div>
- Pattern Recognition and Machine Learning (Information Science and Statistics)
	&nbsp;
	Christopher M. Bishop
	(<a href="https://www.amazon.com/Pattern-Recognition-Learning-Information-Statistics/dp/0387310738/">Amazon</a>,
	<a href="/resource/books/AI/Pattern Recognition and Machine Learning - Bishop.pdf">PDF</a>)
- Deep Learning
	&nbsp;
	Ian Goodfellow, Yoshua Bengio, Aaron Courville
	(<a href="https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618/ref=sr_1_1">Amazon</a>,
	<a href="/resource/books/AI/Deep Learning - Goodfellow, Bengio, Courville.pdf">PDF</a>)
- Reinforcement Learning: An Introduction (Adaptive Computation and Machine Learning series)
	&nbsp;
	Richard S. Sutton, Andrew G. Barto
	(<a href="https://www.amazon.com/Reinforcement-Learning-Introduction-Adaptive-Computation/dp/0262039249/">Amazon</a>,
	<a href="/resource/books/AI/Reinforcement Learning - Richard S. Sutton and Andrew G. Barto.pdf">PDF</a>)
- Machine Learning: A Probabilistic Perspective (Adaptive Computation and Machine Learning series)
	&nbsp;
	Kevin P. Murphy
	(<a href="https://www.amazon.com/Machine-Learning-Probabilistic-Perspective-Computation/dp/0262018020/">Amazon</a>)
- Probabilistic Graphical Models: Principles and Techniques (Adaptive Computation and Machine Learning series)
	&nbsp;
	Daphne Koller, Nir Friedman
	(<a href="https://www.amazon.com/Probabilistic-Graphical-Models-Principles-Computation/dp/0262013193/">Amazon</a>)
- Probabilistic Machine Learning: Advanced Topics (Adaptive Computation and Machine Learning series)
	&nbsp;
	Kevin P. Murphy
	(<a href="https://www.amazon.com/Probabilistic-Machine-Learning-Advanced-Computation/dp/0262048434/">Amazon</a>)

## Lectures {#ml-lectures}

- [/coursera/ Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction)
	&nbsp;
	Andrew Ng @ Stanford University &amp; DeepLearning.AI,
	Geoff Ladwig @ DeepLearning.AI,
	Aarti Bagul
	- Supervised Machine Learning: Regression and Classification
	- Advanced Learning Algorithms
	- Unsupervised Learning, Recommenders, Reinforcement Learning

- [/coursera/ Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)
	&nbsp;
	Andrew Ng @ Stanford University &amp; DeepLearning.AI,
	Younes Bensouda Mourri @ DeepLearning.AI,
	Kian Katanforoosh @ DeepLearning.AI
	- Neural Networks and Deep Learning
	- Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization
	- Structuring Machine Learning Projects
	- Convolutional Neural Networks
	- Sequence Models
