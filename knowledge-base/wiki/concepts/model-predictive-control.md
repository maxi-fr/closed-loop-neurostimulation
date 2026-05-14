---
title: Model Predictive Control
type: concept
tags: [control-theory, mpc, optimization]
sources: [chang-et-al-2020.md, froehlich-jezernik-2005.md]
created: 2026-05-14
updated: 2026-05-14
---

# Model Predictive Control

Model Predictive Control (MPC) is an advanced method of process control that is used to control a process while satisfying a set of constraints. It has been used in the process industries in chemical plants and oil refineries since the 1980s. In recent years, it has also been applied to medical and neurological applications.

## Key Points
- **Optimization:** MPC iteratively computes locally optimal control signals by solving an optimization problem over a future time horizon $p$. The cost function $J$ to be minimized at each step $k$ is typically:
    $$ J(k) = \sum_{i=1}^p \|y(k+i) - w(k+i)\|^2_Q + \sum_{i=0}^{m-1} \|\Delta u(k+i)\|^2_R $$
    where $y$ is the predicted output, $w$ is the reference trajectory, and $\Delta u$ is the change in control effort. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]
- **Predictive Model:** It relies on a predictive model (e.g., [[concepts/volterra-model.md|Volterra Model]] or a linearized [[concepts/hodgkin-huxley-model.md|Hodgkin-Huxley Model]]) to forecast the future behavior of the plant. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]], [[raw/Froehlich_Jezernik_2005/Froehlich_Jezernik_2005.md#2.4. Cascaded controller for control of ion channel activation/inactivation | Fröhlich & Jezernik 2005]]
- **Constraint Handling:** A key advantage of MPC is its ability to explicitly handle constraints on control signals (e.g., stimulation intensity limits) and state variables (e.g., physiological safety bounds) [[raw/Froehlich_Jezernik_2005/Froehlich_Jezernik_2005.md#2.4. Cascaded controller for control of ion channel activation/inactivation | Fröhlich & Jezernik 2005]].
- **Cascaded Architecture:** MPC can be used as an outer loop to provide optimal reference trajectories for inner-loop controllers (e.g., [[concepts/feedback-linearization.md|Feedback Linearization]]) [[raw/Froehlich_Jezernik_2005/Froehlich_Jezernik_2005.md#2.4. Cascaded controller for control of ion channel activation/inactivation | Fröhlich & Jezernik 2005]].
- **Robustness:** Known for good performance and robustness in handling modeling uncertainties and external disturbances. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]

## Related Concepts
- [[concepts/volterra-model.md|Volterra Model]] — Often used as the predictive model in nonlinear MPC.
- [[concepts/hodgkin-huxley-model.md|Hodgkin-Huxley Model]] — A common biophysical model used as a plant or internal model.
- [[concepts/closed-loop-brain-stimulation.md|Closed-loop Brain Stimulation]] — MPC can be used to optimize stimulation signals in real-time.

## Sources
- [[sources/chang-et-al-2020.md|Model Predictive Control for Seizure Suppression Based on Nonlinear Auto-Regressive Moving-Average Volterra Model]] — Describes the use of MPC for seizure suppression using a black-box identified Volterra model.
- [[sources/froehlich-jezernik-2005.md|Feedback control of Hodgkin–Huxley nerve cell dynamics]] — Uses MPC to optimaly track ion channel states in HH neurons.
