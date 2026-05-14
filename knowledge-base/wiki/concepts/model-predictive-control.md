---
title: Model Predictive Control
type: concept
tags: [control-theory, mpc, optimization]
sources: [chang-et-al-2020.md]
created: 2026-05-14
updated: 2026-05-14
---

# Model Predictive Control

Model Predictive Control (MPC) is an advanced method of process control that is used to control a process while satisfying a set of constraints. It has been used in the process industries in chemical plants and oil refineries since the 1980s. In recent years, it has also been applied to medical and neurological applications.

## Key Points
- **Optimization:** MPC iteratively computes locally optimal control signals by solving an optimization problem over a future time horizon. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]
- **Predictive Model:** It relies on a predictive model (e.g., [[concepts/volterra-model.md|Volterra Model]]) to forecast the future behavior of the plant. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]
- **Robustness:** Known for good performance and robustness in handling modeling uncertainties and external disturbances. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]
- **Feedback:** In each sampling time step, the model is used to predict output, and an optimal control signal is obtained by solving a constrained finite horizon optimal control problem. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]

## Related Concepts
- [[concepts/volterra-model.md|Volterra Model]] — Often used as the predictive model in nonlinear MPC.
- [[concepts/closed-loop-brain-stimulation.md|Closed-loop Brain Stimulation]] — MPC can be used to optimize stimulation signals in real-time.

## Sources
- [[sources/chang-et-al-2020.md|Model Predictive Control for Seizure Suppression Based on Nonlinear Auto-Regressive Moving-Average Volterra Model]] — Describes the use of MPC for seizure suppression using a black-box identified Volterra model. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]
