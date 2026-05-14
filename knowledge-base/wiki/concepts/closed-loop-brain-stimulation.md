---
title: Closed-loop Brain Stimulation
type: concept
tags: [neurotechnology, stimulation, feedback]
sources: [chang-et-al-2020.md]
created: 2026-05-14
updated: 2026-05-14
---

# Closed-loop Brain Stimulation

Closed-loop brain stimulation is an approach to neuromodulation where stimulation parameters are automatically adjusted in real-time based on recorded neural activity (feedback).

## Key Points
- **Contrast with Open-loop:** Traditional stimulation is often "open-loop," meaning it delivers constant pulses regardless of the brain's current state. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]
- **Advantages:** Potential for higher therapeutic efficacy, reduced side effects, and lower energy consumption by only stimulating when and how it is needed. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]
- **Components:** Requires sensors to record brain activity (e.g., EEG), a controller to decide on stimulation changes (e.g., [[concepts/model-predictive-control.md|Model Predictive Control]]), and an actuator (stimulator). [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]
- **Challenges:** Requires robust control strategies to handle modeling uncertainty and system disturbances. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]

## Related Concepts
- [[concepts/model-predictive-control.md|Model Predictive Control]] — An advanced control strategy for closed-loop systems.
- [[concepts/seizure-suppression.md|Seizure Suppression]] — A major application area for closed-loop stimulation.

## Sources
- [[sources/chang-et-al-2020.md|Model Predictive Control for Seizure Suppression Based on Nonlinear Auto-Regressive Moving-Average Volterra Model]] — Framework for real-time control of epileptic seizures using MPC and Volterra models. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]
