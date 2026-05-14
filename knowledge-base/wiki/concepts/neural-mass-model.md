---
title: Neural Mass Model
type: concept
tags: [modeling, neuroscience, eeg]
sources: [chang-et-al-2020.md]
created: 2026-05-14
updated: 2026-05-14
---

# Neural Mass Model

A Neural Mass Model (NMM) is a macroscopic neurophysiological model that simulates the collective activity of large populations of neurons. It is widely used to analyze the mechanisms of brain disorders like epilepsy and to simulate EEG signals.

## Key Points
- **Macroscopic Scale:** Instead of modeling individual neurons, NMMs represent the average behavior of neuronal populations (e.g., pyramidal cells, excitatory interneurons, inhibitory interneurons). [[raw/Chang_et_al_2020/Chang_et_al_2020.md#A. Black Box Computation Model | Chang et al. 2020]]
- **EEG Simulation:** NMMs can produce normal EEG waves or epileptiform discharges by adjusting parameters governing excitatory and inhibitory interactions. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]
- **Structure:** Typically consists of components like sigmoid functions (converting potential to firing rate) and second-order linear transfer functions (converting firing rate back to potential). [[raw/Chang_et_al_2020/Chang_et_al_2020.md#A. Black Box Computation Model | Chang et al. 2020]]
- **Evolution:** Developed by researchers such as Jansen, Wendling, and Lopes Da Silva. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]

## Related Concepts
- [[concepts/seizure-suppression.md|Seizure Suppression]] — NMMs are often used as "virtual brains" to test suppression strategies.
- [[concepts/volterra-model.md|Volterra Model]] — Can be used to identify a simplified input-output relationship from a complex NMM.

## Sources
- [[sources/chang-et-al-2020.md|Model Predictive Control for Seizure Suppression Based on Nonlinear Auto-Regressive Moving-Average Volterra Model]] — Uses an NMM as a black-box model to test [[concepts/model-predictive-control.md|Model Predictive Control]] strategies. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#A. Black Box Computation Model | Chang et al. 2020]]
