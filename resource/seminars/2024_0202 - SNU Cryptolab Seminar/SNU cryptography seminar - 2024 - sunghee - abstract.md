---
layout: single
title: "[SNU Math Department Cryptography Seminar] Industrial AI Technology in Manufacturing"
permalink: /seminar/2024_0202 - SNU Cryptolab Seminar/abstract
author_profile: true
last_modified_at: Fri Jul 18 20:35:25 PDT 2025
---

# Abstract

This talk covers somewhat different but related topics; distributed learning ML and industrial AI applications. The first shows how we can do the federated-learning-type of ML and prove the convergence in convex cases, but can extend it to non-convex cases in practice. The second shows how AI can be (and is being) effectively applied to manufacturing problems, but with very different variants, \eg, totally home-grown algorithms.

The ADMM is a dual-ascend optimization method with a smoothed Lagrange function, which has been known for many years in various contexts, but never recognized in one optimization framework. This can not only be applied to ML using parallelism for both data splitting and model splitting but also shows nice convergence properties. We will see how one can systematically use this theoretically firm optimization methodology for diverse ML applications such as decentralized support vector machine (SVM) ML and various consensus problems. Unlike most federated or ML using parallelism such as asynchronous stochastic gradient descent (SGD), this provides a systematic framework for decentralized ML with nice convergence properties.

The latter part of the talk turns the audience's attention to the application sides of AIs. The advent of deep learning (DL) technology was followed by the emergence of a host of new AI technologies in the fields of computer vision (CV), natural language processing (NLP), recommendation systems (RecSys), etc., and it has made a great impact in virtually all aspects of our lives. However, we have not seen much progress in applying these MLs in the industry sectors. There are numerous reasons as to why. For example, the manufacturing equipment entails data drift and shift, hence the ML methods working well for general
applications suffer from these concept drifts.
The computer vision applications in the industry very often require extremely high accuracy, hence the allowable error is extremely small to the extent that even the state-of-the-art CV ML algorithms need lots of tunings and manual work. We introduce industrial AI and discuss why this field is still a blue ocean with huge potential to deliver business values to enterprises. We will present a few success stories of applying ML techniques to some of the most difficult industrial AI problems and show how we could make the breakthroughs. Then we present time-series machine learning (ML) algorithms and techniques, and their applications in Manufacturing.
