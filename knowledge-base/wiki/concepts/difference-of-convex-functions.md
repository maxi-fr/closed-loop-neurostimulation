---
title: Difference of Convex Functions
type: concept
tags: [mathematics, optimization, modeling]
sources: [steffen-cannon-2025.md]
created: 2026-05-14
updated: 2026-05-14
---

# Difference of Convex Functions

A Difference of Convex (DC) function is a function that can be expressed as the difference of two convex functions. Mathematically, $f(x) = g(x) - h(x)$, where both $g$ and $h$ are convex.

## Key Points
- **Universal Approximation:** Any continuous twice-differentiable function can be represented with arbitrary accuracy as a difference of convex functions [[raw/Steffen_Cannon_2025/Steffen_Cannon_2025.md#II. PROBLEM FORMULATION | Steffen & Cannon 2025]].
- **Optimization:** DC functions allow for efficient optimization via **Sequential Convex Programming**. By linearizing the concave part ($-h(x)$), the problem becomes a sequence of convex optimization problems [[raw/Steffen_Cannon_2025/Steffen_Cannon_2025.md#I. INTRODUCTION | Steffen & Cannon 2025]].
- **Tight Linearization Bounds:** The DC property provides tight bounds on linearization errors, which is critical for robust control strategies like **Tube MPC** [[raw/Steffen_Cannon_2025/Steffen_Cannon_2025.md#I. INTRODUCTION | Steffen & Cannon 2025]].
- **DCNN Implementation:** In data-driven control, DC functions can be implemented using two **Input-Convex Neural Networks (ICNN)** [[raw/Steffen_Cannon_2025/Steffen_Cannon_2025.md#III-A. Difference of Convex Functions Neural Network Model | Steffen & Cannon 2025]].

## Related Concepts
- [[concepts/input-convex-neural-network.md|Input-Convex Neural Network]] — Implementation of DC components.
- [[concepts/model-predictive-control.md|Model Predictive Control]] — Optimization framework using DC models.

## Sources
- [[sources/steffen-cannon-2025.md|Deep Learning Model Predictive Control for Deep Brain Stimulation in Parkinson's Disease]] — Employs DC functions for nonlinear MPC in neurostimulation.
