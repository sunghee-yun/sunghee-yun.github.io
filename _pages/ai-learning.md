---
layout: single
title: Welcome to My AI Learning Hub
permalink: /ai-learning
toc: true
toc_label: "ToC"
toc_icon: "cog"
toc_sticky: true
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

<h1 id="ml">
	Online class sites
</h1>

<ul>
<li>
	<a href="https://www.coursera.org/">coursera</a>
</li>
<li>
	<a href="https://www.deeplearning.ai/courses/">DeepLearning.AI</a>
</li>
</ul>

<h1 id="ml">
	Machine learning (ML)
</h1>

<h2 id="ml-books">
	Books
</h2>

<ul>
<li>
	Introduction to Applied Linear Algebra
	-
	Stephen Boyd @ Stanford University,
	Lieven Vandenberghe @ UCLA
	(<a href="https://www.amazon.com/Introduction-Applied-Linear-Algebra-Matrices/dp/1316518965/">Amazon</a>,
	<a href="https://stanford.edu/~boyd/vmls/">Boyd's homepage</a>,
	<a href="/resource/books/AI/Introduction to Applied Linear Algebra - Stephen Boyd and Lieven Vandenberghe.pdf">PDF</a>)
</li>
<li>
	Deep Learning - Ian Goodfellow, Yoshua Bengio, Aaron Courville
	(<a href="https://www.facebook.com/sunghee.yun1/posts/pfbid0itijGVyiNTpxbPRK9Z4hff5BsqbEXKt8XEHzoDCxfYHks78kkuD2k2kYWDsQkQnQl">Amazon</a>,
	<a href="/resource/books/AI/Deep Learning - Goodfellow, Bengio, Courville.pdf">PDF</a>)
</li>
<li>
	Pattern Recognition and Machine Learning (Information Science and Statistics) - Christopher M. Bishop
	(<a href="https://www.amazon.com/Pattern-Recognition-Learning-Information-Statistics/dp/0387310738/">Amazon</a>,
	<a href="/resource/books/AI/Pattern Recognition and Machine Learning - Bishop.pdf">PDF</a>)
</li>
<li>
	Probabilistic Graphical Models: Principles and Techniques (Adaptive Computation and Machine Learning series)
	-
	Daphne Koller, Nir Friedman
	(<a href="https://www.amazon.com/Probabilistic-Graphical-Models-Principles-Computation/dp/0262013193/">Amazon</a>)
</li>
<li>
	Machine Learning: A Probabilistic Perspective (Adaptive Computation and Machine Learning series)
	-
	Kevin P. Murphy
	(<a href="https://www.amazon.com/Machine-Learning-Probabilistic-Perspective-Computation/dp/0262018020/">Amazon</a>)
</li>
<li>
	Probabilistic Machine Learning: Advanced Topics (Adaptive Computation and Machine Learning series)
	-
	Kevin P. Murphy
	(<a href="https://www.amazon.com/Probabilistic-Machine-Learning-Advanced-Computation/dp/0262048434/">Amazon</a>)
</li>
<li>
	Reinforcement Learning: An Introduction (Adaptive Computation and Machine Learning series)
	-
	Richard S. Sutton, Andrew G. Barto
	(<a href="https://www.amazon.com/Reinforcement-Learning-Introduction-Adaptive-Computation/dp/0262039249/">Amazon</a>,
	<a href="/resource/books/AI/Reinforcement Learning - Richard S. Sutton and Andrew G. Barto.pdf">PDF</a>)
</li>
<li>
	The Elements of Statistical Learning: Data Mining, Inference, and Prediction
	-
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
		for have statistically or mathematically rigorous understanding of basic and advanced
		concepts such as overfitting, the expectation-maximization (EM) algorithm,
		and Bayesian inference.
	</p>
	</div>
</li>
</ul>

<h2 id="ml-lectures">
	Lectures
</h2>

<ul>
<li>
	<a href="https://www.coursera.org/specializations/machine-learning-introduction">
	(coursera)
	Machine Learning Specialization</a>
	-
	Andrew Ng @ Stanford University &amp; DeepLearning.AI,
	Geoff Ladwig @ DeepLearning.AI,
	Aarti Bagul
	<ul>
	<li>
		Supervised Machine Learning: Regression and Classification
	</li>
	<li>
		Advanced Learning Algorithms
	</li>
	<li>
		Unsupervised Learning, Recommenders, Reinforcement Learning
	</li>
	</ul>
</li>
<li>
	<a href="https://www.coursera.org/specializations/deep-learning">
	(coursera)
	Deep Learning Specialization</a>
	-
	Andrew Ng @ Stanford University &amp; DeepLearning.AI,
	Younes Bensouda Mourri @ DeepLearning.AI,
	Kian Katanforoosh @ DeepLearning.AI
	<ul>
	<li>
		Neural Networks and Deep Learning
	</li>
	<li>
		Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization
	</li>
	<li>
		Structuring Machine Learning Projects
	</li>
	<li>
		Convolutional Neural Networks
	</li>
	<li>
		Sequence Models
	</li>
	</ul>
</li>
</ul>

<h1 id="ml">
	Optimization
</h1>

<h2 id="opt-books">
	Books
</h2>

<ul>
<li>
	Convex Optimization 1st Edition
	-
	Stephen Boyd, Lieven Vandenberghe
	(<a href="https://www.amazon.com/Convex-Optimization-Corrections-2008-Stephen/dp/0521833787/">Amazon</a>,
	<a href="https://stanford.edu/~boyd/cvxbook/">Boyd's homepage</a>,
	<a href="/resource/books/opt/Convex Optimization - Stephen Boyd and Lieven Vandenberghe.pdf">PDF</a>)
</li>
</ul>
