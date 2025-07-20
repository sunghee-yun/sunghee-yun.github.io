---
layout: single
title: "[Amazon ML Brown Bag Seminar] Convex Optimization for Artificial Intelligence (AI)"
permalink: /seminar/2018_0202 - amazon - ml brown bag - cvxml/abstract
author_profile: true
last_modified_at: Sat Jul 19 16:50:22 EDT 2025
---

# Abstract

## The Power and Ubiquity of Convex Optimization in Machine Learning

Your presentation effectively demonstrates why convex optimization serves as a cornerstone of machine learning algorithms. As you highlight in the slides, convex optimization represents "one of few optimization classes that can be actually solved" globally and efficiently. Many fundamental ML algorithms inherently depend on convex optimization, from simple linear regression (which reduces to least squares problems) to support vector machines with kernel transformations. The beauty lies in the fact that while general optimization problems are "extremely difficult to solve" and often require heuristic approaches for suboptimal solutions, convex problems can be solved reliably using well-established algorithms like interior-point methods, even for large-scale applications with thousands of variables and constraints.

## Bridging Theory and Practice Through Multiple Perspectives

Your slides masterfully connect the mathematical foundations with practical implementation by presenting machine learning through three complementary lenses: statistical, computer science, and numerical algorithmic perspectives. The statistical view elegantly shows how Maximum Likelihood Estimation connects to KL divergence minimization and how Gaussian assumptions lead directly to mean squared error objectives. From the algorithmic perspective, you demonstrate how techniques like regularization (Ridge regression with L2 penalties, Lasso with L1 penalties) can be reformulated as convex optimization problems, enabling the use of sophisticated optimization machinery while maintaining global optimality guarantees.

## Duality as a Unifying Framework

Perhaps most importantly, your presentation emphasizes how Lagrangian duality provides both theoretical insights and practical computational advantages. The dual problem formulation not only offers optimality certificates that allow algorithms to verify solution quality during iterations, but also reveals deep structural properties of machine learning problems. Through examples like linear programming and quadratic programming duals, you show how solving the dual often provides equivalent or complementary information to the primal problem. This duality framework, combined with KKT conditions, creates a unified theoretical foundation that explains why convex optimization has been so successful in machine learning applications, from classical SVMs to modern regularized regression techniques.
