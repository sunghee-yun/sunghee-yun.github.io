---
layout: single
title: "[UBC Sauder School of Business AI Seminar] Reinforcement Learning and its Applications"
permalink: /seminar/2019_0426 - UBC Sauder School of Business - ML Seminar/abstract
author_profile: true
last_modified_at: Sat Jul 19 05:14:39 EDT 2025
---

# Abstract

## Introduction to Reinforcement Learning

Reinforcement learning represents a fundamentally different approach to machine learning compared to traditional supervised and unsupervised methods. While supervised learning relies on labeled data pairs to predict outcomes and unsupervised learning discovers hidden patterns in unlabeled data, reinforcement learning involves an agent that actively interacts with its environment to learn optimal behaviors. This interactive approach more closely mimics how humans learn through trial and error, making decisions based on the history of actions and rewards received from the environment.

## Core Framework and Mathematical Foundation

The reinforcement learning framework is built on the concept of Markov Decision Processes (MDPs), which consist of states, actions, transition probabilities, and reward distributions. The agent's goal is to learn an optimal policy that maximizes the expected cumulative reward over time, balanced by a discount factor that determines the trade-off between immediate and long-term rewards. Key mathematical concepts include value functions that estimate expected future rewards from given states, and Q-functions that evaluate the expected reward of taking specific actions in particular states.

## Algorithmic Approaches

Two primary algorithmic families dominate reinforcement learning: Q-learning and policy gradient methods. Q-learning, particularly deep Q-learning when combined with neural networks, learns to approximate the optimal Q-function through iterative updates based on the Bellman optimality equation. Policy gradient methods, including the REINFORCE algorithm, directly optimize parameterized policies by estimating gradients of the expected reward. While Q-learning tends to be more sample-efficient when it works, policy gradients offer greater generality but often require more training samples due to high variance.

## Practical Applications Across Industries

Reinforcement learning has found successful applications across diverse domains, from gaming achievements like DeepMind's AlphaGo to practical business problems. In technology infrastructure, it optimizes resource management in computer clusters and controls traffic light systems to reduce congestion. The approach also powers personalized recommendation systems that adapt to changing user preferences and dynamic content, addressing challenges like the rapid evolution of news and user engagement patterns.

## Implementation Considerations and Future Potential

Successfully applying reinforcement learning requires several key prerequisites: deep domain knowledge to properly formulate the problem, access to simulated environments for safe training, the ability to model the problem as an MDP, and appropriate algorithmic expertise. As noted by DeepMind's research director, the combination of reinforcement learning's sequential decision-making framework with deep learning's representation capabilities offers the most promising path toward solving challenging real-world problems that extend far beyond toy domains, making it a cornerstone technology for advancing artificial intelligence.
