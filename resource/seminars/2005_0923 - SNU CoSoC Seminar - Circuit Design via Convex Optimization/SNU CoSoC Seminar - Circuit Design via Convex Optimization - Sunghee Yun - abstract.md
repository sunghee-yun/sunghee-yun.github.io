---
layout: single
title: "[SNU CoSoC Seminar] Circuit Design via Convex Optimization"
permalink: /seminar/2005_0923 - SNU CoSoC Seminar - Circuit Design via Convex Optimization/abstract
author_profile: true
last_modified_at: Sun Jul 20 02:12:47 EDT 2025
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
This talk concerns convex optimization, which is a specific class of optimization problems,
and shows how it can be applied to a statistical digital circuit sizing problem.
This problem is formulated as a convex optimization problem
and solved by a heuristic method based on convex optimization for very large-scale problems.

The first part of the talk introduces convex optimization,
which is a specific class of nonlinear optimization problems.
The convex problem classes include many types of optimization problems,
*e.g.*, least squares (LS), linear Program (LP), quadratic program (QP),
second-order cone program (SOCP), geometric program (GP), generalized geometric program (GGP),
semi-definite program (SDP),
and they are fundamentally tractable.
Therefore there are a variety of areas for which the convex optimization can be applied.
We show that a number of problems which can be formulated as convex optimization problems
and show a simple example in digital circuit area.

The second part of the talk shows how a GGP is used for a statistical circuit sizing problem.
First it briefly reviews generalized geometric programming, which is extended from geometric programming.
Since a GP can be solved very efficiently and globally even for a very large-scale problem
and a GGP can be directly transformed to a GP,
a GGP can also be solved efficiently.
Then a stochastic activity network (SAN) problem is studied
since the statistical circuit sizing problem can be formulated as a SAN.
A heuristic method to optimize a SAN using a GGP solver is developed
and we show it works very well for most digital circuits
and handles the performance uncertainty problem very efficiently.

# Claude's abstract

The first part of this presentation introduces convex optimization as a powerful mathematical framework that bridges the gap between simple linear problems and intractable nonlinear optimization. Unlike the traditional view that separates linear from nonlinear problems, the key distinction lies between convex and nonconvex formulations - a paradigm shift that reveals why certain problems are fundamentally tractable while others remain computationally challenging. The talk demonstrates how convex optimization encompasses classical problem classes like least squares, linear programming, and quadratic programming, while extending to newer standard forms including second-order cone programs, geometric programs, and semidefinite programs that can be solved efficiently using modern interior-point methods.

The presentation showcases practical applications through statistical digital circuit optimization, specifically addressing parameter variations in deep submicron semiconductor manufacturing. Using a Ladner-Fisher 32-bit adder as a case study with 451 design variables, the work demonstrates how generalized geometric programming (GGP) can model gate delays accurately and cast circuit optimization problems into convex forms. The statistical design methodology accounts for process variations using the Pelgrom model, showing significant improvements in yield - where traditional nominal optimization results in wide delay distributions under uncertainty, the proposed statistical approach achieves much tighter performance bounds with dramatically reduced 90th percentile delays.

The broader significance lies in establishing convex optimization as an emerging technology that combines the reliability and efficiency of least squares methods with the broader applicability needed for complex engineering problems. By recognizing that convexity, rather than linearity, determines problem tractability, engineers can reformulate challenging design problems into solvable forms. This approach offers a systematic alternative to heuristic methods like simulated annealing, providing global solutions with polynomial-time guarantees while handling large-scale problems that arise in modern circuit design and manufacturing optimization.

The second part of this seminar presents a comprehensive approach to circuit design using geometric programming (GP), a special form of convex optimization that enables efficient solution of large-scale circuit sizing problems. The basic methodology involves formulating circuit design problems as geometric programs and solving them using specialized interior-point methods that exploit the problem structure. Geometric programming occupies a strategic position between restrictive methods like least-squares and general but computationally expensive approaches like simulated annealing, offering an optimal trade-off between problem generality and solution effectiveness while maintaining global optimality guarantees.

The mathematical foundation relies on monomial and posynomial functions, where monomials are products of variables raised to real powers and posynomials are sums of monomials. Standard geometric programs minimize a posynomial objective subject to posynomial inequality constraints and monomial equality constraints. Through logarithmic transformation, these highly nonlinear problems convert to convex optimization problems that can be solved efficiently using interior-point methods. For problems not naturally in GP form, generalized geometric programming extends the framework by handling positive fractional powers and maximum functions through slack variable transformations.

Digital circuit design applications demonstrate the practical power of this approach through gate scaling problems that optimize area, power, and delay trade-offs. Using RC delay models, the seminar shows how circuit delay (maximum over all path delays) and total area/power (linear combinations of gate sizes) can be formulated as generalized geometric programs. Advanced applications include statistical design under process variations, multi-corner robust design, and multiple-scenario optimization. A notable example using a 451-gate Ladner-Fisher 32-bit adder illustrates how statistical design methods achieve significantly better performance under uncertainty compared to nominal optimization approaches.

The seminar concludes with power and ground network design applications, where statistical current variations necessitate mesh topologies over tree structures. An average power formulation using convex optimization enables automatic topology selection and wire sizing while maintaining current density and voltage constraints. The key insight is that geometric programming provides a systematic framework for handling concurrent constraints and objectives in circuit design, achieving robust solutions even when perfect statistical analysis is not feasible. The approach requires careful modeling effort but delivers high payoff through reliable, globally optimal solutions to large-scale problems.
