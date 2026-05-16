---
title: Model Predictive Control
type: concept
tags: [control-theory, mpc, optimization, neural-networks, convex-optimization]
sources: [chang-et-al-2020.md, froehlich-jezernik-2005.md, steffen-cannon-2025.md]
created: 2026-05-14
updated: 2026-05-14
---

# Model Predictive Control

Model Predictive Control (MPC) is an advanced method of process control that iteratively computes locally optimal control signals by solving an optimization problem over a future time horizon. It explicitly handles constraints and relies on a predictive model to forecast future behavior.

## Key Points
- **Optimization:** The cost function $J$ to be minimized typically involves tracking error and control effort:
    $$ J(k) = \sum_{i=1}^p \|y(k+i) - w(k+i)\|^2_Q + \sum_{i=0}^{m-1} \|\Delta u(k+i)\|^2_R $$
    In neuromodulation, the objective may be to keep a biomarker (e.g., beta-band envelope) below a pathological threshold $\beta_0$ [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]], [[raw/Steffen_Cannon_2025/Steffen_Cannon_2025.md#II. PROBLEM FORMULATION | Steffen & Cannon 2025]].
- **Predictive Models:**
    - **Linear Models:** Often used for simplicity (e.g., ARX or state-space models), but may not capture inherent neural nonlinearities [[raw/Steffen_Cannon_2025/Steffen_Cannon_2025.md#I. INTRODUCTION | Steffen & Cannon 2025]].
    - **Nonlinear Models:** Use [[concepts/volterra-model.md|Volterra Series]] or neural networks. A recent approach uses **Difference of Convex Functions Neural Networks (DCNN)** to represent nonlinear dynamics while maintaining efficient optimization via sequential convex programming [[raw/Steffen_Cannon_2025/Steffen_Cannon_2025.md#III. CONTROL LAW | Steffen & Cannon 2025]].
- **Multi-step Predictors:** Instead of recursive application of a single-step predictor, multi-step predictors can be used to improve accuracy and simplify the construction of robust tubes for **Tube MPC** [[raw/Steffen_Cannon_2025/Steffen_Cannon_2025.md#III. CONTROL LAW | Steffen & Cannon 2025]].
- **Constraint Handling:** MPC allows for hard constraints on stimulation intensity ($u \in [0, u_{\max}]$) and rate of change ($\Delta u \in [-\Delta u_{\max}, \Delta u_{\max}]$), ensuring physiological safety [[raw/Froehlich_Jezernik_2005/Froehlich_Jezernik_2005.md#2.4. Cascaded controller for control of ion channel activation/inactivation | Fröhlich & Jezernik 2005]], [[raw/Steffen_Cannon_2025/Steffen_Cannon_2025.md#II. PROBLEM FORMULATION | Steffen & Cannon 2025]].
- **Robust Tube MPC:** Addresses modeling uncertainty by ensuring that the actual system trajectory remains within a "tube" around a nominal predicted trajectory, even in the presence of disturbances or linearization errors [[raw/Steffen_Cannon_2025/Steffen_Cannon_2025.md#III-B. DCNN Tube MPC | Steffen & Cannon 2025]].

## Related Concepts
- [[concepts/volterra-model.md|Volterra Model]] — A functional series model for nonlinear system identification.
- [[concepts/input-convex-neural-network.md|Input-Convex Neural Network]] — A neural network architecture used to build convex models for MPC.
- [[concepts/closed-loop-brain-stimulation.md|Closed-loop Brain Stimulation]] — The application domain for these control strategies.

## Sources
- [[sources/chang-et-al-2020.md|Model Predictive Control for Seizure Suppression Based on Nonlinear Auto-Regressive Moving-Average Volterra Model]] — Describes the use of MPC for seizure suppression using a black-box identified Volterra model.
- [[sources/froehlich-jezernik-2005.md|Feedback control of Hodgkin–Huxley nerve cell dynamics]] — Uses MPC to optimaly track ion channel states in HH neurons.
- [[sources/steffen-cannon-2025.md|Deep Learning Model Predictive Control for Deep Brain Stimulation in Parkinson's Disease]] — Introduces DCNN-based Tube MPC for nonlinear neuromodulation.
