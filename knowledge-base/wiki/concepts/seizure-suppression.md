---
title: Seizure Suppression
type: concept
tags: [epilepsy, neurology, treatment]
sources: [chang-et-al-2020.md]
created: 2026-05-14
updated: 2026-05-14
---

# Seizure Suppression

Seizure suppression refers to the methods and strategies used to eliminate or reduce the occurrence of epileptic seizures, characterized by epileptiform spikes and high-frequency oscillations in EEG signals.

## Key Points
- **Epileptiform Activity:** Characterized by abnormal discharges that can be simulated using macroscopic models like the [[concepts/neural-mass-model.md|Neural Mass Model]]. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]
- **Brain Stimulation:** Techniques like Deep Brain Stimulation (DBS) and Transcranial Electrical Stimulation (TES) are used to modulate neural activity and suppress seizures. In an optimal control framework, this involves minimizing an objective function $J = \int |y(t) - y_{ref}(t)|^2 dt$, where $y(t)$ is the observed EEG and $y_{ref}(t)$ is the desired non-seizure activity. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]
- **Closed-loop Approach:** Modern research focuses on [[concepts/closed-loop-brain-stimulation.md|Closed-loop Brain Stimulation]] which adjusts stimulation in real-time to match the patient's state, improving efficacy and reducing side effects. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]

## Related Concepts
- [[concepts/neural-mass-model.md|Neural Mass Model]] — Used to simulate epileptiform EEG signals for research.
- [[concepts/closed-loop-brain-stimulation.md|Closed-loop Brain Stimulation]] — A primary method for achieving automated seizure suppression.

## Sources
- [[sources/chang-et-al-2020.md|Model Predictive Control for Seizure Suppression Based on Nonlinear Auto-Regressive Moving-Average Volterra Model]] — Investigates using [[concepts/model-predictive-control.md|Model Predictive Control]] to optimize stimulation for suppression. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]
