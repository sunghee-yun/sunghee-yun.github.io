---
title: AI seminar series in Seoul - Jun &#12316; Jul in 2024
date: Tue Jul 23 14:37:06 PDT 2024
last_modified_at: Fri Jul 11 12:00:55 PDT 2025
categories:
 - blog
tags:
 - business
 - trip
 - seoul
 - AI
 - seminar
toc: true
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
---

posted: {{ page.date| date: "%d-%b-%Y" }}
&amp;
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

# NotebookLM Podcasts

<audio id="podcast-1" controls>
	<source type="audio/wav" src="/resource/posts/2024-07-23-PDT - AI seminar series in Seoul/NotebookLM/Seoul AI Seminar Series_ LLM and Generative AI Insights-03.wav">
	Your browser does not support this shorter audio element.
</audio>

<audio id="podcast-2" controls>
	<source type="audio/wav" src="/resource/posts/2024-07-23-PDT - AI seminar series in Seoul/NotebookLM/Seoul AI Seminar Series_ LLM and Generative AI Insights-02.wav">
	Your browser does not support this shorter audio element.
</audio>

<audio id="podcast-3" controls>
	<source type="audio/wav" src="/resource/posts/2024-07-23-PDT - AI seminar series in Seoul/NotebookLM/Seoul AI Seminar Series_ LLM and Generative AI Insights-01.wav">
	Your browser does not support this shorter audio element.
</audio>

# Reflections

Last month, I had the privilege of doing AI seminar series at Samsung Electronics, Seoul National University (SNU),
Pohang University of Science and Technology (POSTECH), Sogang University,
and Yonsei University during Seoul biz & family trip.
I was utterly honored to have such opportunities
where I could share my insight and learn a lot from Q&As with talented AI researchers and practitioners in academia and industry.
<!--a href="https://www.facebook.com/share/p/ezrvBHN4TALTzUir/">Facebook post</a-->

<!--figure style="width: 40ch; display:block; margin:auto;"-->
<!--figure style="width: 40ch; display:table; margin:0 auto;"-->
<!--figure style="display:table; margin:0 auto;"-->
<div class="fig-container">
<figure>
	<img src="/resource/seminars/2024_0627 - Samsung Flash Memroy Team AI Seminar/photos/KakaoTalk_Photo_2024-06-27-21-46-51 003.jpeg">
	<figcaption>
		Myself giving a talk in Future Hall at Samsung Semiconductor
	</figcaption>
</figure>
</div>

The seminar, titled "LLM & genAI - Technology, Industry, Market, and Some Important Questions," covered a wide range of topics in the rapidly evolving field of artificial intelligence. As someone with extensive experience in both academia and industry, including roles at Stanford University, Samsung, Amazon, and as a co-founder of AI-focused companies, I aimed to provide a comprehensive overview of the current state and future prospects of AI.

I began by exploring the history and recent advances in language models, from early bag-of-words approaches to the transformative impact of attention mechanisms and transformer architectures. I highlighted how these developments have led to the creation of powerful large language models (LLMs) like GPTs, BERT, and their successors, which are reshaping natural language processing (NLP) and numerous other fields.

A significant portion of the seminar focused on the technical aspects of LLMs and generative AI. I delved into the architecture of transformers, examining concepts like multi-head attention and self-attention, which have proven crucial to the success of these models. I also discussed newer developments like joint-embedding predictive architecture (JEPA) and its variants, which aim to improve semantic representation learning.
Beyond the technical details, I explored the broader implications of AI advancements. This included discussions on:

* The AI market and industry trends, including the rapid growth of investment in AI startups and the dominance of major tech companies in developing foundation models.
* Ethical considerations and potential biases in AI systems, emphasizing the need for responsible development and deployment.
* Legal and regulatory challenges arising from AI technologies, such as copyright issues with training data and liability in autonomous systems.
* Philosophical questions about AI consciousness, knowledge, and reasoning capabilities.
* The future of AI, including predictions about the development of artificial general intelligence (AGI) and its potential impacts on society and the economy.

One of the most engaging parts of the seminar was my exploration of "important questions" surrounding AI. I grappled with issues like why we often use human-level performance as a benchmark for AI, what factors contribute to the success of deep learning, and how we should approach the development of AI to ensure it benefits humanity.

The Q&A sessions were particularly enlightening, with attendees raising thought-provoking questions about the practical applications of AI in various industries, the challenges of implementing AI systems in real-world settings, and the potential societal impacts of widespread AI adoption.

<div class="fig-container">
<figure style="width:50ch;">
	<img src="/resource/seminars/2024_0619 - Postech Seminar/photos/postech seminar.jpeg">
	<figcaption>
		Myself giving a talk at Pohang University of Science and Technology (POSTECH)
	</figcaption>
</figure>
</div>

Reflecting on the seminars, I'm struck by the incredible pace of innovation in AI and the enthusiasm of researchers and practitioners in South Korea. The questions and discussions highlighted the global nature of AI research and development, with similar challenges and opportunities being tackled around the world.

As we move forward, it's clear that collaboration between academia, industry, and policymakers will be crucial in shaping the future of AI. The ethical considerations and potential societal impacts I discussed must remain at the forefront of our minds as we continue to push the boundaries of what's possible with AI technology.

I'm grateful for the opportunity to have shared my insights and learned from the brilliant minds I encountered during this seminar series. As the field of AI continues to evolve at a breakneck pace, these kinds of exchanges become ever more valuable, helping us to navigate the complex landscape of technology, ethics, and societal impact that AI presents.

<script>
// Function to get URL parameters
function getUrlParameter(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

// Function to auto-play audio based on URL parameter
function autoPlayAudio() {
    const audioParam = getUrlParameter('audio');
    if (audioParam) {
        const audioElement = document.getElementById(audioParam);
        if (audioElement) {
            // Scroll to the audio element
            audioElement.scrollIntoView({ behavior: 'smooth', block: 'center' });

            // Add a small delay to ensure the page has loaded
            setTimeout(() => {
                audioElement.play().catch(error => {
                    console.log('Auto-play was prevented by browser:', error);
                    // Highlight the audio element if auto-play fails
                    audioElement.style.border = '3px solid #ff6b6b';
                    audioElement.style.borderRadius = '5px';
                });
            }, 500);
			// Alternative: Simulate click on play button
			/*
			setTimeout(() => {
				audioElement.play().catch(error => {
					// If auto-play fails, show a prominent play button or notification
					const playButton = document.createElement('button');
					playButton.textContent = '▶ Click to Play Selected Audio';
					playButton.style.cssText = `
						position: fixed;
						top: 20px;
						right: 20px;
						z-index: 1000;
						background: #007cba;
						color: white;
						border: none;
						padding: 10px 20px;
						border-radius: 5px;
						cursor: pointer;
						font-size: 16px;
					`;
					playButton.onclick = () => {
						audioElement.play();
						document.body.removeChild(playButton);
					};
					document.body.appendChild(playButton);
				});
			}, 500);
			*/
        }
    }
}

// Run the function when the page loads
document.addEventListener('DOMContentLoaded', autoPlayAudio);
</script>
