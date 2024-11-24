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
</script>

<h1 id="people">People</h1>

<h2 id="people-respect">Those I utterly respect!</h2>

<a href="https://stanford.edu/~boyd/">Stephen P. Boyd</a>
/
<a href="https://www.andrewng.org/">Andrew Ng</a>

<h2 id="researchers">Researchers of my interest</h2>

<a href="https://www.doc.ic.ac.uk/~mpsha/">Murray Shanahan</a>

<h2 id="entrepreneurs">Entrepreneurs I respect</h2>

<a href="https://en.wikipedia.org/wiki/Jeff_Bezos">Jeff Bezos</a>
/
<a href="https://en.wikipedia.org/wiki/Elon_Musk">Elon Musk</a>

<h2 id="companies">Companies of my interest</h2>

<a href="https://sungheeyun-erudio.github.io/">Erudio Bio, Inc.</a>
/
<a href="https://www.figure.ai/">Figure AI</a>
/
<a href="https://www.liquid.ai/">Liquid AI</a> 
/
<a href="https://mistral.ai/">Mistrial AI</a>
/
<a href="https://dnotitia.com/">D.Notitia</a>

<a href="#all-papers-in-reverse-chronological-order">All papers in reverse chronological order</a>

<h1 id="optimization">Optimization</h1>

<ul>
<li>
	"Compact Model Parameter Extraction via Derivative-Free Optimization"
	- Rafael Perez Martinez, Masaya Iwamoto, Kelly Woo, Zhengliang Bian, Roberto Tinti, Stephen Boyd &amp; Srabanti Chowdhury
	@ 24-Jun-2024
	(<a href="https://stanford.edu/~boyd/papers/compact_model_parameter_extraction.html">Boyd's homepage</a>, <a href="https://arxiv.org/abs/2406.16355">arxiv</a>)
</li>
</ul>

<h2 id="optimization-cvxopt">Convex optimization</h2>

<ul>
<li>
	"Optimization Algorithm Design via Electric Circuits"
	- Stephen P. Boyd, Tetiana Parshakova, Ernest K. Ryu &amp; Jaewook J. Suh
	@ 04-Nov-2024
	(<a href="https://arxiv.org/abs/2411.02573">arxiv</a>)
</li>
</ul>

<h1 id="ai">AI</h1>


<h2 id="ai-fundamentals">Fundamentals</h2>

<ul>
<li>
	"How Classification Baseline Works for Deep Metric Learning: A Perspective of Metric Space"
	- Yuanqu Mou, Zhengxue Jian, Haiyang Bai &amp; Chang Gou
	@ 05-Sep-2024
	(<a href="https://openreview.net/forum?id=DVl5GAuBXA">OpenReview.net</a>)
	&nbsp;
	<div class="foldable-toggle">abstract</div>
	<div class="foldable-content">
	<p>
	Deep Metric Learning (DML) stands as a powerful technique utilized for training models to capture semantic similarities between data points across various domains, including computer vision, natural language processing, and recommendation systems. Current approaches in DML often prioritize the development of novel network structures or loss functions while overlooking metric properties and the intricate relationship between classification and metric learning. This oversight results in significant time overhead, particularly when the number of categories increases. To address this challenge, we propose extending the loss function used in classification to function as a metric, thereby imposing constraints on the distances between training samples based on the triangle inequality. This approach is akin to proxy-based methods and aims to enhance the efficiency of DML. Drawing inspiration from metrically convex metrics, we introduce the concept of a "weak-metric" to overcome the limitations associated with certain loss functions that cannot be straightforwardly extended to full metrics. This ensures the effectiveness of DML under various circumstances. Furthermore, we extend the Cross Entropy loss function to function as a weak-metric and introduce a novel metric loss derived from Cross Entropy for experimental comparisons with other methods. The results underscore the credibility and reliability of our proposal, showcasing its superiority over state-of-the-art techniques. Notably, our approach also exhibits significantly faster training times as the number of categories increases, making it a compelling choice for large-scale datasets.
	</p>
	</div>
</li>
<li>
	"Classification is a Strong Baseline for Deep Metric Learning"
	- Andrew Zhai &amp; Hao-Yu Wu
	@ 30-Nov-2018
	(<a href="https://arxiv.org/abs/1811.12649">arxiv</a>)
</li>
</ul>

<h2 id="ai-bio">Bio</h2>

<ul>
<li>
	"Sequence modeling and design from molecular to genome scale with Evo"
	- Eric Nguyen, Michael Poli, Matthew G. Durrant, Brian Kang, Dhruva Katrekar, David B. Li, Liam J. Bartie, Armin W. Thomas, Samuel H. King, Garyk Brixi, Jeremy Sullivan, Madelena Y. Ng, Ashley Lewis, Aaron Lou, Stefano Ermon, Stephen A. Baccus, Tina Hernandez-Boussard, Christopher Ré, Patrick D. Hsu &amp; Brian L. Hie
	(Arc Institute, Department of Computer Science @ Stanford University &amp; Stanford Data Science)
	@ 15-Nov-2024
	(<a href="https://www.science.org/doi/10.1126/science.ado9336">Science</a>)
</li>
<li>
	"Geometry-Aware Generative Autoencoders for Warped Riemannian Metric Learning and Generative Modeling on Data Manifolds"
	- Xingzhi Sun, Danqi Liao, Kincaid MacDonald, Yanlei Zhang, Chen Liu, Guillaume Huguet, Guy Wolf, Ian Adelstein, Tim G. J. Rudner &amp; Smita Krishnaswamy
	@ 16-Oct-2024
	(<a href="https://arxiv.org/abs/2410.12779">arxiv</a>)
	&nbsp;
	<div class="foldable-toggle">abstract</div>
	<div class="foldable-content">
	<p>
	Rapid growth of high-dimensional datasets in fields such as single-cell RNA sequencing and spatial genomics has led to unprecedented opportunities for scientific discovery, but it also presents unique computational and statistical challenges. Traditional methods struggle with geometry-aware data generation, interpolation along meaningful trajectories, and transporting populations via feasible paths. To address these issues, we introduce Geometry-Aware Generative Autoencoder (GAGA), a novel framework that combines extensible manifold learning with generative modeling. GAGA constructs a neural network embedding space that respects the intrinsic geometries discovered by manifold learning and learns a novel warped Riemannian metric on the data space. This warped metric is derived from both the points on the data manifold and negative samples off the manifold, allowing it to characterize a meaningful geometry across the entire latent space. Using this metric, GAGA can uniformly sample points on the manifold, generate points along geodesics, and interpolate between populations across the learned manifold using geodesic-guided flows. GAGA shows competitive performance in simulated and real-world datasets, including a 30% improvement over the state-of-the-art methods in single-cell population-level trajectory inference.
	</p>
	</div>
</li>
<li>
	"Predicting Gene Ontology Annotations from CAFA Using Distance Machine Learning and Transfer Metric Learning"
	- Shilpa Choudhary, MD Khaja Shaik, Sivaneasan Bala Krishnan &amp; Sunita Gupta
	@ 30-Sep-2024
	(<a href="https://onlinelibrary.wiley.com/doi/abs/10.1002/9781394268832.ch21">Wiley</a>)
</li>
</ul>

<h2 id="ai-agent">AI agent</h2>

<ul>
<li>
	"Agent-as-a-Judge: Evaluate Agents with Agents"
	- Mingchen Zhuge, Changsheng Zhao, Dylan Ashley, Wenyi Wang, Dmitrii Khizbullin, Yunyang Xiong, Zechun Liu, Ernie Chang, Raghuraman Krishnamoorthi, Yuandong Tian, Yangyang Shi, Vikas Chandra &amp; Jürgen Schmidhuber
	(Meta AI &amp; King Abdullah University of Science and Technology (KAUST))
	@ 14-Oct-2024
	(<a href="https://arxiv.org/abs/2410.10934">arxiv</a>)
</li>
<li>
	"MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering"
	- Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng &amp; Aleksander Mądry
	(OpenAI)
	@ 09-Oct-2024
	(<a href="https://arxiv.org/abs/2410.07095">arxiv</a>)
</li>
<li>
	"MMAU: A Holistic Benchmark of Agent Capabilities Across Diverse Domains"
	- Guoli Yin, Haoping Bai, Shuang Ma, Feng Nan, Yanchao Sun, Zhaoyang Xu, Shen Ma, Jiarui Lu, Xiang Kong, Aonan Zhang, Dian Ang Yap, Yizhe zhang, Karsten Ahnert, Vik Kamath, Mathias Berglund, Dominic Walsh, Tobias Gindele, Juergen Wiest, Zhengfeng Lai, Xiaoming Wang, Jiulong Shan, Meng Cao, Ruoming Pang &amp; Zirui Wang
	(Apple Inc.)
	@ 18-Jul-2024
	(<a href="https://arxiv.org/abs/2407.18961">arxiv</a>)
</li>
</ul>

<h2 id="ai-llm">LLM</h2>

<ul>
<li>
	"HtmlRAG: HTML is Better Than Plain Text for Modeling Retrieved Knowledge in RAG Systems"
	- Jiejun Tan, Zhicheng Dou, Wen Wang, Mang Wang, Weipeng Chen &amp; Ji-Rong Wen
	(Renmin University of China &amp; Baichuan Intelligent Technology)
	@ 05-Nov-2024
	(<a href="https://arxiv.org/abs/2411.02959v1">arxiv</a>)
</li>
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
	(Google &amp; Google DeepMind &amp; UMass Amherst)
	@ 15-Jul-2024
	(<a href="https://arxiv.org/abs/2407.10817">arxiv</a>)
</li>
<li id="facts">
	"FACTS About Building Retrieval Augmented Generation-based Chatbots"
	- Rama Akkiraju, Anbang Xu, Deepak Bora, Tan Yu, Lu An, Vishal Seth, Aaditya Shukla, Pritam Gundecha, Hridhay Mehta, Ashwin Jha, Prithvi Raj, Abhinav Balasubramanian, Murali Maram, Guru Muthusamy, Shivakesh Reddy Annepally, Sidney Knowles, Min Du, Nick Burnett, Sean Javiya, Ashok Marannan, Mamta Kumari, Surbhi Jha, Ethan Dereszenski, Anupam Chakraborty, Subhash Ranjan, Amina Terfai, Anoop Surya, Tracey Mercer, Vinodh Kumar Thanigachalam, Tamar Bar, Sanjana Krishnan, Samy Kilaru, Jasmine Jaksic, Nave Algarici, Jacob Liberman, Joey Conway, Sonu Nayyar &amp; Justin Boitano
	(NVIDIA)
	@ 10-Jul-2024
	(<a href="https://arxiv.org/abs/2407.07858">arxiv</a>)
	&nbsp;
	<div class="foldable-toggle">RAG pipeline for Chatbots</div>
	<div class="foldable-content">
	<div class="fig-container">
	<figure>
	<img src="/assets/images/ai/llm/rag-pipeline-for-chatbot-nvidia.png">
	<figcaption>
	Control Points in a typical RAG pipeline when building Chatbots
	</figcaption>
	</figure>
	</div>
	</div>
</li>
<li>
	"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
	- Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press &amp; Karthik Narasimhan
	(Princeton University, Princeton Language and Intelligence &amp; University of Chicago)
	@ 10-Oct-2023
	(<a href="https://arxiv.org/abs/2310.06770">arxiv</a>)
	&nbsp;
	<div class="foldable-toggle">RAG pipeline for Chatbots</div>
	<div class="foldable-content">
	<div class="fig-container">
	<figure>
	<img src="/assets/images/ai/llm/rag-pipeline-for-chatbot-nvidia.png">
	<figcaption>
	Control Points in a typical RAG pipeline when building Chatbots
	</figcaption>
	</figure>
	</div>
	</div>
</li>
<li>
	"The Unreasonable Effectiveness of Data"
	- Alon Halevy, Peter Norvig &amp; Fernando Pereira
	(Google)
	@ 24-Mar-2009
	(<a href="https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/35179.pdf">Google Research</a>)
</li>
</ul>

<h2 id="ai-llm-intelligence">LLM &amp; intelligence</h2>

<ul>
<li>
	"Talking About Large Language Models"
	- Murray Shanahan
	@ 07-Dec-2022
	(<a href="https://arxiv.org/abs/2212.03551">arxiv</a>)
</li>
<li>
	"Simulacra as Conscious Exotica"
	- Murray Shanahan
	@ 19-Feb-2012
	(<a href="https://arxiv.org/abs/2402.12422">arxiv</a>)
</li>
<li>
	"Satori Before Singularity"
	- Murray Shanahan
	@ 01-Jan-2012
	(<a href="https://www.doc.ic.ac.uk/~mpsha/ShanahanJCS2012.pdf">PDF</a>)
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
	(<a href="https://arxiv.org/abs/2407.13517">arxiv</a>)
</li>
</ul>

<h2 id="ai-dl-models">DL models</h2>

<ul>
<li>
	"Robust flight navigation out of distribution with liquid neural networks"
	@ 19-Apr-2023
	(<a href="https://www.science.org/doi/10.1126/scirobotics.adc8892">ScienceRobotics</a>)
</li>
<li>
	"Improved Variational Autoencoders for Text Modeling using Dilated Convolutions"
	@ 27-Feb-2017
	(<a href="https://arxiv.org/abs/1702.08139">arxiv</a>)
</li>
<li>
	"Generating Sentences from a Continuous Space"
	@ 19-Nov-2015
	(<a href="https://arxiv.org/abs/1511.06349">arxiv</a>)
</li>
</ul>

<h2 id="ai-nn-models">NN models</h2>

<ul>
<li>
	"Statistical Mechanics of Neural Networks"
	- Haim Sompolinsky
	@ 01-Dec-1988
	(<a href="https://lnkd.in/gjRQWUb9">Physics Today</a>)
	(Haim Sompolinsky is a professor of physics at the Racah
Institute of Physics of the Hebrew University of Jerusalem.)
</li>
</ul>

<h2 id="ai-metric learning">Metric learning</h2>

<ul>
<li>
	"Self-Taught Metric Learning without Labels"
	- Sungyeon Kim, Dongwon Kim, Minsu Cho &amp; Suha Kwak
	(POSTECH)
	@ 04-May-2022
	(<a href="https://arxiv.org/abs/2205.01903">arxiv</a>, <a href="https://github.com/tjddus9597/STML-CVPR22">github</a>, <a href="https://www.researchgate.net/publication/363906881_Self-Taught_Metric_Learning_without_Labels">ResearchGate</a>)
</li>
<li>
	"A Robust and Efficient Doubly Regularized Metric Learning Approach"
	- Meizhu Liu &amp; Baba C. Vemuri
	@ 01-Jan-2012
	(<a href="https://www.academia.edu/77676366/A_Robust_and_Efficient_Doubly_Regularized_Metric_Learning_Approach">academia.edu</a>, <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3761969/">NIH</a>)
</li>
</ul>

<h2 id="ai-recsys">Recommender system</h2>

<ul>
<li>
	"Collaborative Filtering for Implicit Feedback Datasets"
	- Yifan Hu, Yehuda Koren &amp; Chris Volinsky
	(AT&amp;T Labs &amp; Yahoo! Research)
	@ 18-Jul-2024
	(<a href="http://yifanhu.net/PUB/cf.pdf">PDF</a>)
</li>
<li>
	"Logistic Matrix Factorization for Implicit Feedback Data"
	- Christopher C. Johnson
	(Spotify)
	@ 01-Dec-2014
	(<a href="https://stanford.edu/~rezab/nips2014workshop/submits/logmat.pdf">PDF</a>)
</li>
<li>
	"BPR: Bayesian Personalized Ranking from Implicit Feedback"
	- Steffen Rendle, Christoph Freudenthaler, Zeno Gantner &amp; Lars Schmidt-Thieme
	@ 09-May-2012
	(<a href="https://arxiv.org/abs/1205.2618">arxiv</a>)
</li>
<li>
	"Applications of the conjugate gradient method for implicit feedback collaborative filtering"
	- Gábor Takács, István Pilászy &amp; Domonkos Tikk
	@ 23-Oct-2011
	(<a href="https://dl.acm.org/doi/10.1145/2043932.2043987">ACM</a>)
</li>
</ul>

<h1 id="code repo">Code repo</h1>


<h2 id="code repo-ai">AI</h2>

<ul>
<li>
	"OpenAI's Swarm"
	- OpenAI
	@ 10-Oct-2024
	(<a href="https://github.com/openai/swarm">github</a>)
</li>
</ul>
<h1 id="all-papers-in-reverse-chronological-order">All papers in reverse chronological order</h1>
<ul>
<li>
	"Sequence modeling and design from molecular to genome scale with Evo"
	- Eric Nguyen, Michael Poli, Matthew G. Durrant, Brian Kang, Dhruva Katrekar, David B. Li, Liam J. Bartie, Armin W. Thomas, Samuel H. King, Garyk Brixi, Jeremy Sullivan, Madelena Y. Ng, Ashley Lewis, Aaron Lou, Stefano Ermon, Stephen A. Baccus, Tina Hernandez-Boussard, Christopher Ré, Patrick D. Hsu &amp; Brian L. Hie
	(Arc Institute, Department of Computer Science @ Stanford University &amp; Stanford Data Science)
	@ 15-Nov-2024
	(<a href="https://www.science.org/doi/10.1126/science.ado9336">Science</a>)
</li>
<li>
	"HtmlRAG: HTML is Better Than Plain Text for Modeling Retrieved Knowledge in RAG Systems"
	- Jiejun Tan, Zhicheng Dou, Wen Wang, Mang Wang, Weipeng Chen &amp; Ji-Rong Wen
	(Renmin University of China &amp; Baichuan Intelligent Technology)
	@ 05-Nov-2024
	(<a href="https://arxiv.org/abs/2411.02959v1">arxiv</a>)
</li>
<li>
	"Optimization Algorithm Design via Electric Circuits"
	- Stephen P. Boyd, Tetiana Parshakova, Ernest K. Ryu &amp; Jaewook J. Suh
	@ 04-Nov-2024
	(<a href="https://arxiv.org/abs/2411.02573">arxiv</a>)
</li>
<li>
	"Geometry-Aware Generative Autoencoders for Warped Riemannian Metric Learning and Generative Modeling on Data Manifolds"
	- Xingzhi Sun, Danqi Liao, Kincaid MacDonald, Yanlei Zhang, Chen Liu, Guillaume Huguet, Guy Wolf, Ian Adelstein, Tim G. J. Rudner &amp; Smita Krishnaswamy
	@ 16-Oct-2024
	(<a href="https://arxiv.org/abs/2410.12779">arxiv</a>)
	&nbsp;
	<div class="foldable-toggle">abstract</div>
	<div class="foldable-content">
	<p>
	Rapid growth of high-dimensional datasets in fields such as single-cell RNA sequencing and spatial genomics has led to unprecedented opportunities for scientific discovery, but it also presents unique computational and statistical challenges. Traditional methods struggle with geometry-aware data generation, interpolation along meaningful trajectories, and transporting populations via feasible paths. To address these issues, we introduce Geometry-Aware Generative Autoencoder (GAGA), a novel framework that combines extensible manifold learning with generative modeling. GAGA constructs a neural network embedding space that respects the intrinsic geometries discovered by manifold learning and learns a novel warped Riemannian metric on the data space. This warped metric is derived from both the points on the data manifold and negative samples off the manifold, allowing it to characterize a meaningful geometry across the entire latent space. Using this metric, GAGA can uniformly sample points on the manifold, generate points along geodesics, and interpolate between populations across the learned manifold using geodesic-guided flows. GAGA shows competitive performance in simulated and real-world datasets, including a 30% improvement over the state-of-the-art methods in single-cell population-level trajectory inference.
	</p>
	</div>
</li>
<li>
	"Agent-as-a-Judge: Evaluate Agents with Agents"
	- Mingchen Zhuge, Changsheng Zhao, Dylan Ashley, Wenyi Wang, Dmitrii Khizbullin, Yunyang Xiong, Zechun Liu, Ernie Chang, Raghuraman Krishnamoorthi, Yuandong Tian, Yangyang Shi, Vikas Chandra &amp; Jürgen Schmidhuber
	(Meta AI &amp; King Abdullah University of Science and Technology (KAUST))
	@ 14-Oct-2024
	(<a href="https://arxiv.org/abs/2410.10934">arxiv</a>)
</li>
<li>
	"OpenAI's Swarm"
	- OpenAI
	@ 10-Oct-2024
	(<a href="https://github.com/openai/swarm">github</a>)
</li>
<li>
	"MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering"
	- Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng &amp; Aleksander Mądry
	(OpenAI)
	@ 09-Oct-2024
	(<a href="https://arxiv.org/abs/2410.07095">arxiv</a>)
</li>
<li>
	"Predicting Gene Ontology Annotations from CAFA Using Distance Machine Learning and Transfer Metric Learning"
	- Shilpa Choudhary, MD Khaja Shaik, Sivaneasan Bala Krishnan &amp; Sunita Gupta
	@ 30-Sep-2024
	(<a href="https://onlinelibrary.wiley.com/doi/abs/10.1002/9781394268832.ch21">Wiley</a>)
</li>
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
	"How Classification Baseline Works for Deep Metric Learning: A Perspective of Metric Space"
	- Yuanqu Mou, Zhengxue Jian, Haiyang Bai &amp; Chang Gou
	@ 05-Sep-2024
	(<a href="https://openreview.net/forum?id=DVl5GAuBXA">OpenReview.net</a>)
	&nbsp;
	<div class="foldable-toggle">abstract</div>
	<div class="foldable-content">
	<p>
	Deep Metric Learning (DML) stands as a powerful technique utilized for training models to capture semantic similarities between data points across various domains, including computer vision, natural language processing, and recommendation systems. Current approaches in DML often prioritize the development of novel network structures or loss functions while overlooking metric properties and the intricate relationship between classification and metric learning. This oversight results in significant time overhead, particularly when the number of categories increases. To address this challenge, we propose extending the loss function used in classification to function as a metric, thereby imposing constraints on the distances between training samples based on the triangle inequality. This approach is akin to proxy-based methods and aims to enhance the efficiency of DML. Drawing inspiration from metrically convex metrics, we introduce the concept of a "weak-metric" to overcome the limitations associated with certain loss functions that cannot be straightforwardly extended to full metrics. This ensures the effectiveness of DML under various circumstances. Furthermore, we extend the Cross Entropy loss function to function as a weak-metric and introduce a novel metric loss derived from Cross Entropy for experimental comparisons with other methods. The results underscore the credibility and reliability of our proposal, showcasing its superiority over state-of-the-art techniques. Notably, our approach also exhibits significantly faster training times as the number of categories increases, making it a compelling choice for large-scale datasets.
	</p>
	</div>
</li>
<li>
	"Distilling System 2 into System 1"
	- Ping Yu, Jing Xu, Jason Weston &amp; Ilia Kulikov
	(META Fair)
	@ 24-Jul-2024
	(<a href="https://arxiv.org/abs/2407.06023">arxiv</a>)
</li>
<li>
	"MMAU: A Holistic Benchmark of Agent Capabilities Across Diverse Domains"
	- Guoli Yin, Haoping Bai, Shuang Ma, Feng Nan, Yanchao Sun, Zhaoyang Xu, Shen Ma, Jiarui Lu, Xiang Kong, Aonan Zhang, Dian Ang Yap, Yizhe zhang, Karsten Ahnert, Vik Kamath, Mathias Berglund, Dominic Walsh, Tobias Gindele, Juergen Wiest, Zhengfeng Lai, Xiaoming Wang, Jiulong Shan, Meng Cao, Ruoming Pang &amp; Zirui Wang
	(Apple Inc.)
	@ 18-Jul-2024
	(<a href="https://arxiv.org/abs/2407.18961">arxiv</a>)
</li>
<li>
	"Mask2Map: Vectorized HD Map Construction Using Bird's Eye View Segmentation Masks"
	- Sehwan Choi, Jungho Kim, Hongjae Shin &amp; Jun Won Choi
	(Hanyang University &amp; SNU)
	@ 18-Jul-2024
	(<a href="https://arxiv.org/abs/2407.13517">arxiv</a>)
</li>
<li>
	"Collaborative Filtering for Implicit Feedback Datasets"
	- Yifan Hu, Yehuda Koren &amp; Chris Volinsky
	(AT&amp;T Labs &amp; Yahoo! Research)
	@ 18-Jul-2024
	(<a href="http://yifanhu.net/PUB/cf.pdf">PDF</a>)
</li>
<li>
	"Foundational Autoraters: Taming Large Language Models for Better Automatic Evaluation"
	- Tu Vu, Kalpesh Krishna, Salaheddin Alzubi, Chris Tar, Manaal Faruqui &amp; Yun-Hsuan Sung
	(Google &amp; Google DeepMind &amp; UMass Amherst)
	@ 15-Jul-2024
	(<a href="https://arxiv.org/abs/2407.10817">arxiv</a>)
</li>
<li id="facts">
	"FACTS About Building Retrieval Augmented Generation-based Chatbots"
	- Rama Akkiraju, Anbang Xu, Deepak Bora, Tan Yu, Lu An, Vishal Seth, Aaditya Shukla, Pritam Gundecha, Hridhay Mehta, Ashwin Jha, Prithvi Raj, Abhinav Balasubramanian, Murali Maram, Guru Muthusamy, Shivakesh Reddy Annepally, Sidney Knowles, Min Du, Nick Burnett, Sean Javiya, Ashok Marannan, Mamta Kumari, Surbhi Jha, Ethan Dereszenski, Anupam Chakraborty, Subhash Ranjan, Amina Terfai, Anoop Surya, Tracey Mercer, Vinodh Kumar Thanigachalam, Tamar Bar, Sanjana Krishnan, Samy Kilaru, Jasmine Jaksic, Nave Algarici, Jacob Liberman, Joey Conway, Sonu Nayyar &amp; Justin Boitano
	(NVIDIA)
	@ 10-Jul-2024
	(<a href="https://arxiv.org/abs/2407.07858">arxiv</a>)
	&nbsp;
	<div class="foldable-toggle">RAG pipeline for Chatbots</div>
	<div class="foldable-content">
	<div class="fig-container">
	<figure>
	<img src="/assets/images/ai/llm/rag-pipeline-for-chatbot-nvidia.png">
	<figcaption>
	Control Points in a typical RAG pipeline when building Chatbots
	</figcaption>
	</figure>
	</div>
	</div>
</li>
<li>
	"Compact Model Parameter Extraction via Derivative-Free Optimization"
	- Rafael Perez Martinez, Masaya Iwamoto, Kelly Woo, Zhengliang Bian, Roberto Tinti, Stephen Boyd &amp; Srabanti Chowdhury
	@ 24-Jun-2024
	(<a href="https://stanford.edu/~boyd/papers/compact_model_parameter_extraction.html">Boyd's homepage</a>, <a href="https://arxiv.org/abs/2406.16355">arxiv</a>)
</li>
<li>
	"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
	- Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press &amp; Karthik Narasimhan
	(Princeton University, Princeton Language and Intelligence &amp; University of Chicago)
	@ 10-Oct-2023
	(<a href="https://arxiv.org/abs/2310.06770">arxiv</a>)
	&nbsp;
	<div class="foldable-toggle">RAG pipeline for Chatbots</div>
	<div class="foldable-content">
	<div class="fig-container">
	<figure>
	<img src="/assets/images/ai/llm/rag-pipeline-for-chatbot-nvidia.png">
	<figcaption>
	Control Points in a typical RAG pipeline when building Chatbots
	</figcaption>
	</figure>
	</div>
	</div>
</li>
<li>
	"Robust flight navigation out of distribution with liquid neural networks"
	@ 19-Apr-2023
	(<a href="https://www.science.org/doi/10.1126/scirobotics.adc8892">ScienceRobotics</a>)
</li>
<li>
	"Talking About Large Language Models"
	- Murray Shanahan
	@ 07-Dec-2022
	(<a href="https://arxiv.org/abs/2212.03551">arxiv</a>)
</li>
<li>
	"Self-Taught Metric Learning without Labels"
	- Sungyeon Kim, Dongwon Kim, Minsu Cho &amp; Suha Kwak
	(POSTECH)
	@ 04-May-2022
	(<a href="https://arxiv.org/abs/2205.01903">arxiv</a>, <a href="https://github.com/tjddus9597/STML-CVPR22">github</a>, <a href="https://www.researchgate.net/publication/363906881_Self-Taught_Metric_Learning_without_Labels">ResearchGate</a>)
</li>
<li>
	"Classification is a Strong Baseline for Deep Metric Learning"
	- Andrew Zhai &amp; Hao-Yu Wu
	@ 30-Nov-2018
	(<a href="https://arxiv.org/abs/1811.12649">arxiv</a>)
</li>
<li>
	"Improved Variational Autoencoders for Text Modeling using Dilated Convolutions"
	@ 27-Feb-2017
	(<a href="https://arxiv.org/abs/1702.08139">arxiv</a>)
</li>
<li>
	"Generating Sentences from a Continuous Space"
	@ 19-Nov-2015
	(<a href="https://arxiv.org/abs/1511.06349">arxiv</a>)
</li>
<li>
	"Logistic Matrix Factorization for Implicit Feedback Data"
	- Christopher C. Johnson
	(Spotify)
	@ 01-Dec-2014
	(<a href="https://stanford.edu/~rezab/nips2014workshop/submits/logmat.pdf">PDF</a>)
</li>
<li>
	"BPR: Bayesian Personalized Ranking from Implicit Feedback"
	- Steffen Rendle, Christoph Freudenthaler, Zeno Gantner &amp; Lars Schmidt-Thieme
	@ 09-May-2012
	(<a href="https://arxiv.org/abs/1205.2618">arxiv</a>)
</li>
<li>
	"Simulacra as Conscious Exotica"
	- Murray Shanahan
	@ 19-Feb-2012
	(<a href="https://arxiv.org/abs/2402.12422">arxiv</a>)
</li>
<li>
	"A Robust and Efficient Doubly Regularized Metric Learning Approach"
	- Meizhu Liu &amp; Baba C. Vemuri
	@ 01-Jan-2012
	(<a href="https://www.academia.edu/77676366/A_Robust_and_Efficient_Doubly_Regularized_Metric_Learning_Approach">academia.edu</a>, <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3761969/">NIH</a>)
</li>
<li>
	"Satori Before Singularity"
	- Murray Shanahan
	@ 01-Jan-2012
	(<a href="https://www.doc.ic.ac.uk/~mpsha/ShanahanJCS2012.pdf">PDF</a>)
</li>
<li>
	"Applications of the conjugate gradient method for implicit feedback collaborative filtering"
	- Gábor Takács, István Pilászy &amp; Domonkos Tikk
	@ 23-Oct-2011
	(<a href="https://dl.acm.org/doi/10.1145/2043932.2043987">ACM</a>)
</li>
<li>
	"The Unreasonable Effectiveness of Data"
	- Alon Halevy, Peter Norvig &amp; Fernando Pereira
	(Google)
	@ 24-Mar-2009
	(<a href="https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/35179.pdf">Google Research</a>)
</li>
<li>
	"Statistical Mechanics of Neural Networks"
	- Haim Sompolinsky
	@ 01-Dec-1988
	(<a href="https://lnkd.in/gjRQWUb9">Physics Today</a>)
	(Haim Sompolinsky is a professor of physics at the Racah
Institute of Physics of the Hebrew University of Jerusalem.)
</li>
</ul>
