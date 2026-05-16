---
title: Input-Convex Neural Network
type: concept
tags: [machine-learning, convex-optimization, neural-networks]
sources: [steffen-cannon-2025.md]
created: 2026-05-14
updated: 2026-05-14
---

# Input-Convex Neural Network

Input-Convex Neural Networks (ICNN) are a class of neural network architectures where the output is a convex function of the inputs.

## Key Points
- **Structural Constraints:** Convexity is ensured by using non-negative weights between hidden layers and using convex, non-decreasing activation functions (such as ReLU). They often include skip connections from the input to hidden layers to maintain expressiveness [[raw/Steffen_Cannon_2025/Steffen_Cannon_2025.md#III-A. Difference of Convex Functions Neural Network Model | Steffen & Cannon 2025]].
- **Application in MPC:** ICNNs are particularly useful in [[concepts/model-predictive-control.md|Model Predictive Control]] because they allow the formulation of optimization problems that can be solved efficiently using convex programming techniques [[raw/Steffen_Cannon_2025/Steffen_Cannon_2025.md#I. INTRODUCTION | Steffen & Cannon 2025]].
- **Difference of Convex (DC) Modeling:** Two ICNNs can be combined to represent any continuous twice-differentiable function as a **Difference of Convex (DC) function**: $f(x) = f_1(x) - f_2(x)$. This allows for modeling complex nonlinearities while still providing tight bounds for linearization [[raw/Steffen_Cannon_2025/Steffen_Cannon_2025.md#III-A. Difference of Convex Functions Neural Network Model | Steffen & Cannon 2025]].

## Related Concepts
- [[concepts/difference-of-convex-functions.md|Difference of Convex Functions]] — The mathematical framework using ICNNs.
- [[concepts/model-predictive-control.md|Model Predictive Control]] — Optimization framework utilizing ICNN-based models.

## Sources
- [[sources/steffen-cannon-2025.md|Deep Learning Model Predictive Control for Deep Brain Stimulation in Parkinson's Disease]] — Uses ICNNs to model the nonlinear dynamics of beta oscillations.
