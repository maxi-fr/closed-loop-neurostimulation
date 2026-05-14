---
title: Closed-loop Brain Stimulation
type: concept
tags: [neurotechnology, stimulation, feedback]
sources: [chang-et-al-2020.md, chouzouris-et-al-2021.md, froehlich-jezernik-2005.md, salfenmose-obermayer-2022.md]
created: 2026-05-14
updated: 2026-05-14
---

# Closed-loop Brain Stimulation

Closed-loop brain stimulation is an approach to neuromodulation where stimulation parameters $u(t)$ are automatically adjusted in real-time based on recorded neural activity $x(t)$ (feedback). This is often formalized as a control law $u(t) = f(x(t))$, where $f$ is the control policy.

## Key Points
- **Contrast with Open-loop:** Traditional stimulation is often "open-loop," meaning it delivers constant pulses regardless of the brain's current state. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]
- **Biophysical State Control:** Beyond simple signal modulation, closed-loop control can target the underlying biophysical states, such as the activation and inactivation of specific ion channels [[raw/Froehlich_Jezernik_2005/Froehlich_Jezernik_2005.md#2.4. Cascaded controller for control of ion channel activation/inactivation | Fröhlich & Jezernik 2005]].
- **Bistability and State Switching:** In systems with multiple stable states (e.g., "up" and "down" activity states), closed-loop strategies can be used to switch between them with high efficiency [[raw/Salfenmose_Obermayer_2022/Salfenmose_Obermayer_2022.md#Abstract | Salfenmose & Obermayer 2022]].
- **Minimal Intervention Strategy:** In noiseless systems, state switching can be achieved with a minimal control pulse that merely pushes the system across a basin of attraction boundary [[raw/Salfenmose_Obermayer_2022/Salfenmose_Obermayer_2022.md#3.2. | Salfenmose & Obermayer 2022]].
- **Advantages:** Potential for higher therapeutic efficacy, reduced side effects, and lower energy consumption by only stimulating when and how it is needed. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]
- **Components:** Requires sensors to record brain activity (e.g., EEG or intracellular voltage), a controller to decide on stimulation changes (e.g., [[concepts/model-predictive-control.md|Model Predictive Control]]), and an actuator (stimulator). [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]

## Related Concepts
- [[concepts/model-predictive-control.md|Model Predictive Control]] — An advanced control strategy for closed-loop systems.
- [[concepts/optimal-nonlinear-control.md|Optimal Nonlinear Control]] — A framework for steering nonlinear network dynamics.
- [[concepts/neural-mass-model.md|Neural Mass Model]] — Macroscopic models often used to design closed-loop controllers.

## Sources
- [[sources/chang-et-al-2020.md|Model Predictive Control for Seizure Suppression Based on Nonlinear Auto-Regressive Moving-Average Volterra Model]] — Framework for real-time control of epileptic seizures using MPC and Volterra models.
- [[sources/chouzouris-et-al-2021.md|Applications of optimal nonlinear control to a whole-brain network of FitzHugh-Nagumo oscillators]] — Framework for state-switching and synchronization in large-scale brain networks.
- [[sources/froehlich-jezernik-2005.md|Feedback control of Hodgkin–Huxley nerve cell dynamics]] — Demonstrates closed-loop control of ion channel states for AP generation and suppression.
- [[sources/salfenmose-obermayer-2022.md|Nonlinear optimal control of a mean-field model of neural population dynamics]] — Analyzes efficient switching strategies in biophysically grounded models.
