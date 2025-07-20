---
layout: single
title: "[SNU CoSoC Seminar] Circuit Design via Convex Optimization"
permalink: /seminar/2005_0923 - SNU CoSoC Seminar - Circuit Design via Convex Optimization/abstract
author_profile: true
last_modified_at: Sun Jul 20 01:07:23 EDT 2025
---

# Abstract

As digital integrated circuits continue to scale with Moore's law,
and device dimensions shrink into the nanometer regime,
billions of transistors can be built
into an embedded system, to perform operations at an unprecedented speed.
This gigascale integration involves complicated physical effects that
induce much larger performance uncertainty in digital circuits than ever before.
This performance uncertainty can be handled by many manufacturing-aware design techniques
including statistical digital circuit sizing.
This \talk\ concerns convex optimization, which is a specific class of optimization problems,
and shows how it can be applied to a statistical digital circuit sizing problem.
This problem is formulated as a convex optimization problem
and solved by a heuristic method based on convex optimization for very large-scale problems.

The first part of the \talk\ introduces convex optimization,
which is a specific class of nonlinear optimization problems.
The convex problem classes include many types of optimization problems,
\eg, least squares (LS), linear Program (LP), quadratic program (QP),
second-order cone program (SOCP), geometric program (GP), generalized geometric program (GGP),
semi-definite program (SDP),
and they are fundamentally tractable.
Therefore there are a variety of areas for which the convex optimization can be applied.
We show that a number of problems which can be formulated as convex optimization problems
and show a simple example in digital circuit area.

The second part of the \talk\ shows how a GGP is used for a statistical circuit sizing problem.
First it briefly reviews generalized geometric programming, which is extended from geometric programming.
Since a GP can be solved very efficiently and globally even for a very large-scale problem
and a GGP can be directly transformed to a GP,
a GGP can also be solved efficiently.
Then a stochastic activity network (SAN) problem is studied
since the statistical circuit sizing problem can be formulated as a SAN.
A heuristic method to optimize a SAN using a GGP solver is developed
and we show it works very well for most digital circuits
and handles the performance uncertainty problem very efficiently.
