## Maik first project E-mail

* We need a preferably simple model for the brain dynamics. In general, neual mass models such as Cowan-Wilson or Jansen-Rit may be used to model population dynamics on a high level. You could start to look into suitable models for brain dynamics. May be Keivan can also point to some other approaches than neural mass models that might be used.

* Besides the dynamics model, we need a measurable output. This may be an EEG signal. So it might be good to look already into EEG forward models, i.e., models that simulate an EEG response from the states of a neural mass model.

* Related to the first two points, you may also check which Python simulators for brain dynamics, neurostimulation, and EEG signals are available.

* Most likely, we will have to use state and parameter estimation. It might be good to refresh your knowledge on these topics as well (don't go too deep into detail; I suggest to keep this part as simple as positive since it will be necessary but it is, at least in my opinion, not the most interesting aspect of the project).

* Besides researching useful cost function and constraint formulations, the most interesting part is the MPC. The problem is that we will most likely need an MPC for impulsive control, i.e., the applied currents aren't continuous variables but we need to time them as pulses of certain amplitudes (both timing and amplitude may be determined by the MPC). That is, we need to move beyond the classical MPC formulations and develop ideas on how to solve the problem. Possible directions include:

    1) Formulation as a continuous optimal control problem where pulse times and amplitudes are free and optimized over along the horizon.

    2) Continuous relaxations where sparsity/pulsing is achieved via regularization terms in the cost function (similar to what some of the attached papers do), or other relaxation strategies.

    3) Formulation as a mixed-integer problem with a fixed timing, where at each time point a discrete variable (0 - no pulse, 1 - pulse) and the continuous amplitude are optimized.

This is in general a field that hasn't been extensively explored yet. But related works may be found in the fields of closed-loop neurostimulation, MPC for impulse or hybrid or switched systems, and event-triggered MPC. This is, in my opinion, the interesting part, where we need to come up with some ideas and test several approaches. Therefore, trying to get an intuition about existing solution approaches might also be a good first step.

In the first meeting, it would make sense to briefly talk about possible MPC formulations for impulsive systems and a bit about modeling and implementation frameworks for brain dynamics, so that we have a first direction for the project.

---
