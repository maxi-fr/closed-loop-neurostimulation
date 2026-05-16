---
title: Neural Mass Model
type: concept
tags: [modeling, neuroscience, eeg]
sources: [chang-et-al-2020.md, salfenmose-obermayer-2022.md]
created: 2026-05-14
updated: 2026-05-14
---

# Neural Mass Model

A Neural Mass Model (NMM) is a macroscopic neurophysiological model that simulates the collective activity of large populations of neurons. It is widely used to analyze the mechanisms of brain disorders like epilepsy and to simulate EEG signals.

## Key Points
- **Macroscopic Scale:** Instead of modeling individual neurons, NMMs represent the average behavior of neuronal populations (e.g., pyramidal cells, excitatory interneurons, inhibitory interneurons). [[raw/Chang_et_al_2020/Chang_et_al_2020.md#A. Black Box Computation Model | Chang et al. 2020]]
- **EEG Simulation:** NMMs can produce normal EEG waves or epileptiform discharges by adjusting parameters governing excitatory and inhibitory interactions. [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]]
- **Biophysically Realistic Variants:** Newer models, such as the **EI EIF model**, are derived from mean-field approximations of exponential integrate-and-fire (EIF) neurons, ensuring all parameters and variables are biophysically grounded. These models are often described by sets of first-order ordinary differential equations (ODEs) for each population $i$:
    $$ \tau_i \dot{r}_i = -r_i + \Phi_i(I_{ext,i} + \sum_j W_{ij} r_j) $$
    where $r_i$ is the population firing rate, $\tau_i$ is the time constant, and $\Phi_i$ is the nonlinear transfer function. [[raw/Salfenmose_Obermayer_2022/Salfenmose_Obermayer_2022.md#2.1. | Salfenmose & Obermayer 2022]].
- **Dynamics:** These models can exhibit complex behaviors including bistability (coexistence of "up" and "down" states), oscillations, and limit cycles [[raw/Salfenmose_Obermayer_2022/Salfenmose_Obermayer_2022.md#Abstract | Salfenmose & Obermayer 2022]].
- **Evolution:** Developed by researchers such as Jansen, Wendling, Lopes Da Silva, and more recently by Cakan and Obermayer [[raw/Chang_et_al_2020/Chang_et_al_2020.md#I. Introduction | Chang et al. 2020]], [[raw/Salfenmose_Obermayer_2022/Salfenmose_Obermayer_2022.md#2.1. | Salfenmose & Obermayer 2022]].

## Related Concepts
- [[concepts/seizure-suppression.md|Seizure Suppression]] — NMMs are often used as "virtual brains" to test suppression strategies.
- [[concepts/optimal-nonlinear-control.md|Optimal Nonlinear Control]] — Used to find efficient ways to steer NMMs between different activity states.
- [[concepts/closed-loop-brain-stimulation.md|Closed-loop Brain Stimulation]] — NMMs serve as the "virtual brain" plant in closed-loop control studies.
- [[concepts/volterra-model.md|Volterra Model]] — System identification framework for building black-box models of NMM dynamics.

## Sources
- [[sources/chang-et-al-2020.md|Model Predictive Control for Seizure Suppression Based on Nonlinear Auto-Regressive Moving-Average Volterra Model]] — Uses an NMM as a black-box model to test [[concepts/model-predictive-control.md|Model Predictive Control]] strategies.
- [[sources/salfenmose-obermayer-2022.md|Nonlinear optimal control of a mean-field model of neural population dynamics]] — Applies optimal control to a biophysically grounded EI EIF neural mass model.
