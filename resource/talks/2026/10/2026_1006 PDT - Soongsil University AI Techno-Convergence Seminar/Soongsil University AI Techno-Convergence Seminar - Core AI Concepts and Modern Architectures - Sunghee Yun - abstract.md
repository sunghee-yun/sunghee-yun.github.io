---
date: Tue Oct  6 00:13:18 PDT 2026
last_modified_at: Tue Oct  6 00:13:18 PDT 2026
layout: single
title: "[Soongsil University AI Techno-Convergence Seminar] Core AI Concepts and Modern Architectures"
permalink: /talks/2026_1006 PDT - Soongsil University AI Techno-Convergence Seminar/abstract
author_profile: true
toc: false
toc_label: "&nbsp;Table of Contents"
toc_icon: "fa-solid fa-list"
toc_sticky: true
---

# Abstract

Artificial Intelligence (AI) has moved from research curiosity to the defining technology of the decade, yet the mathematics underneath the most advanced systems is remarkably compact. This lecture builds that foundation from the ground up: vectors, matrices, and the chain rule; probability, random variables, and expectation; and the handful of ideas that turn these into machine learning, namely the optimal estimator, the bias–variance trade-off, maximum likelihood, and the equivalence of minimizing mean-square error, maximizing likelihood, and minimizing KL divergence. We then show how a deep neural network (DNN) is nothing more than a composition of affine maps and nonlinearities, and how backpropagation is simply the chain rule applied in reverse, which is why stochastic gradient descent remains the one optimization method the entire field relies on.

With that foundation in place, we turn to the architectures that define modern AI. Starting from the sequence-to-sequence models that preceded it, we examine the Transformer in detail: scaled dot-product attention, multi-head attention, self- and encoder–decoder attention, and the causal mask that distinguishes a decoder from an encoder. We then trace how the original encoder–decoder design split into three families, and why the decoder-only variant, from GPT-1 through today's frontier models, won. The reasons are structural rather than accidental: a single next-token objective, the ability to treat any prompt as a prefix, in-context learning that emerged at scale, and inference that maps efficiently onto GPUs and high-bandwidth memory. Along the way we explain why a decoder-only model can translate without an encoder, and how the 2017 block evolved into the RMSNorm, RoPE, grouped-query, mixture-of-experts block that powers current systems.

The final part looks at what sits on top of the model. Multimodal learning extends the same representation-learning machinery to images, audio, and video, and agentic AI wraps the language model in a loop of perception, planning, tool use, and memory, so that the system pursues an objective rather than answering a question. We survey the agent tooling now shipping from open-source projects and from Anthropic, OpenAI, and Google, and close with what this means for engineers and founders: the model is the engine but not the system, value is migrating from model training to system design, and the frontier moves fast enough that the durable skill is not any single tool but the ability to keep relearning it.
