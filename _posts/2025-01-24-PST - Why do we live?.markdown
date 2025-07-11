---
title: Why Do We Live? &ndash; A Wrong Question to Ask
date: Fri Jan 24 01:41:51 PST 2025
last_modified_at: Fri Jul 11 12:43:05 PDT 2025
categories:
 - blog
tags:
 - values
 - philosophy
 - life
toc: false
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
---

posted: {{ page.date| date: "%d-%b-%Y" }}
&amp;
updated: {{ page.last_modified_at| date: "%d-%b-%Y" }}
{: .notice--primary}

<blockquote>
&hellip; the right question to ask is "Do I want meaning of my life?"
</blockquote>

<blockquote>
The meaning of life isn't an inherent truth waiting to be discovered.
<br>
&hellip; it's something we actively create through our will and intention.
</blockquote>

# NotebookLM Podcasts

<h2>based on this blog</h2>

<audio id="podcast-1" controls>
	<source type="audio/wav" src="/resource/posts/2025-01-24-PST - Why do we live/NotebookLM/Creating Life's Meaning_ A Personal Journey-01.wav">
	Your browser does not support this shorter audio element.
</audio>

<audio id="podcast-2" controls>
	<source type="audio/wav" src="/resource/posts/2025-01-24-PST - Why do we live/NotebookLM/Creating Life's Meaning_ A Personal Journey-02.wav">
	Your browser does not support this shorter audio element.
</audio>


Like most people (I believe &hellip; or guess), I have often pondered why we live and, more specifically, why I live or should live.
Throughout different stages of my life, I've found various answers, including the possibility that there is no answer at all.

Before developing sufficient capacity for philosophical thinking and logical reasoning, my thoughts wandered aimlessly.
As the child of non-religious parents, I didn't rely on divine beings to find meaning.
During high school, I explored Christianity but found its answers unsatisfactory, as the Bible failed to convincingly demonstrate God's existence,
hence
for example,
making the &ldquo;Christian type&rdquo; of purpose-driven life arguments unconvincing.
&mdash;
Please don't get me wrong. I know this cannot disprove anything.

A turning point came when I read the two-volume biography
of <a href="https://en.wikipedia.org/wiki/Ludwig_Wittgenstein">Ludwig Wittgenstein</a>, subtitled "Duties of a Genius"
(<a href="https://product.kyobobook.co.kr/detail/S000001364617">this</a> and <a href="https://product.kyobobook.co.kr/detail/S000001364618">this</a>).
As soon as I saw the subtitle,
it triggered something inside me.
&mdash;
It was a turning point viewed in hindsight
meaning that I did not understand why I was struck by that subtitle
then.
&mdash;
Without clearly knowing what, how, and why it triggered,
I interpreted it like this (after reading those books): Wittgenstein recognized his exceptional intellect, acknowledging he had no equal among his contemporaries.
He knew he surpassed even his advisor Bertrand Russell in many ways, particularly in philosophy,
and this awareness of his rare gift led him to feel obligated to contribute to humanity
(because he was received the rare gift whether or not he wanted).
This line of thoughts struck me deeply (now I think), compelling me to search for my own purpose,
even though I didn't consider myself his intellectual equal that time.

This idea persisted until at least 2017, as I recall mentioning it during a phone conversation with my brother.
It happened that, since 2015, I had become deeply interested in Buddha's teachings;
not the Buddhism as a religion, but his original teachings he taught to help people overcome the (inevitable) suffering.
As I explored concepts of mercy, compassion, nirvāna, enlightenment, and Anātman,
these teachings transformed my life and eventually led me to nirvāna.
During this period, influenced by Buddha's teachings, I concluded that life had no inherent meaning.
I clearly understood and accepted the randomness of my existence.
&mdash; After all, I resulted from the chance meeting of an egg with a random sperm.
&mdash; But that was my misinterpretation. Well, misinterpretation or not,
what mattered is what I have realized now regardless of his original teachings (below).

While this element of chance is undeniable, I've recently come to understand that the meaning of life still exists.
Few people (throughout human history) could, can, and will be able to understand this argument,
but the conclusion that life has no inherent meaning is right,
but at the same time wrong.
To be more precise,
it's not not-right, nor not-wrong
for the reasons that I will lay down in my arguments in the below paragraph.
&ndash;
It transcends the binary of right and wrong for reasons that defy verbal and logical articulation - here
we encounter the limits of language to capture certain fundamental truths
(as Wittgenstein pointed out).

The fundamental error that I, and virtually everyone on the earth and throughout the human history,
have made is asking
&ldquo;What is the meaning of my life?&rdquo;,
&ldquo;Why do I live?&rdquo;,
or
&ldquo;Why should I live?&rdquo;
whereas
the right question to ask is "Do I want meaning of my life?"

The meaning of life isn't an inherent truth waiting to be discovered.
It isn't universally accessible or predetermined.
Rather, it's something we actively create through our will and intention.
The meaning of life is what we create as active and autonomous agents, not something bestowed by others,
even by some absolute being endorsed by holy scriptures.

[Sunghee](/)

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
