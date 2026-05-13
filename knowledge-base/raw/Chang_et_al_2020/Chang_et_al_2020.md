![](_page_0_Picture_2.jpeg)

# Model Predictive Control for Seizure Suppression Based on Nonlinear Auto-Regressive Moving-Average Volterra Model

Siyuan Chang<sup>®</sup>, *Graduate Student Member, IEEE*, Xile Wei<sup>®</sup>, *Member, IEEE*, Fei Su<sup>®</sup>, Chen Liu<sup>®</sup>, *Member, IEEE*, Guosheng Yi<sup>®</sup>, Jiang Wang<sup>®</sup>, *Member, IEEE*, Chunxiao Han, and Yanqiu Che<sup>®</sup>, *Member, IEEE*

Abstract—This article investigates a closed-loop brain stimulation method based on model predictive control strategy to suppress epileptic seizures. A neural mass model (NMM), exhibiting the normal and various epileptic seizures by changing physiologically meaningful parameters, is used as a black-box model of the brain. Based on system identification, an auto-regressive moving-average Volterra model is established to reveal the relationship between stimulation and neuronal responses. Then, the model predictive control strategy is implemented based the Volterra model, which can generate an optimal stimulation waveform to eliminate epileptiform waves. The computational simulation results indicate the proposed closed-loop control strategy can optimize the stimulation waveform without particular knowledge of the physiological properties of the system. The robustness of the proposed control strategy to system disturbances makes it more appropriate for future clinical application.

Index Terms—Seizure, closed-loop brain stimulation, system identification, Volterra model, model predictive control.

#### I. Introduction

As a serious neurological disorder with significant morbidity and mortality, epilepsy causes mental and physical damage to patients and disrupts their normal life [1]. Electroencephalography (EEG), a powerful brain activity recording technique, plays a significant role in the diagnosis and treatment of epilepsy [2], [3]. Two main characteristics of epilepsy, epileptiform spikes and high-frequency oscillations, can be reflected in the EEG signals [4]–[6].

Computational models from microscopic to macroscopic scales play a pivotal role in research of neurological disorder [7], [8]. The EEG signals used in the diagnosis and treatment of epilepsy are summation of post-synaptic membrane potentials of many neurons, therefore, macroscopic neurophysiological models are widely used in mechanism analysis of epilepsy. The neural mass model (NMM), as a macroscopic model, can produce normal EEG waves or epileptiform discharges by adjusting excitatory and inhibitory interactions between interconnected pyramidal cells and interneurons [4], [9]. Since the NMM is established originally by Lopes Da Silva *et al.* in 1970s [10], [11], and developed by Jansen *et al.* [12] and Wendling *et al.* [3], [13], [14], it has become the preferred model to simulate the dynamic patterns of epileptic EEG signals.

Due to the serious side effects and possible surgical injury, the development and application of anti-epileptic drug treatments and surgical treatments have encountered a bottleneck [15]-[17]. By utilizing electrical pulses to modulate neural activities, brain stimulation [18], such as deep brain stimulation (DBS) [19]-[21] or transcranial electrical stimulation (TES) [22], has become an effective clinical treatment option for epilepsy patients [23], [24]. However, the signals of traditional open-loop brain stimulation are constant and can't be adjusted according to patient's disease progression. It limits therapeutic effects, even induces serious side effects such as involuntary movements, compulsive gambling [25], [26]. In addition, constant stimulation waveform may consume more energy than needed [27], [28]. Therefore, it is of great importance to construct a closed-loop brain stimulation system which can automatically adjust the stimulation signals via realtime state feedback [23], [29], [30].

Because the brain contains more than 100 billion neurons, and 100 trillion connections can be created between neurons [31], it is still impossible to build the precise computation model of brain with the current knowledge of neurophysiology.

1534-4320 © 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

Furthermore, the external environment disturbances would have effects on the brain activity [32]. Therefore, there is a great challenge for closed-loop controller design due to the modelling uncertainty and disturbances. In the previous studies, many model-based closed-loop brain stimulation strategies have been proposed to address these challenges [33], such as improved proportional-integral-derivative control [34], [35], feedback linearization control [36], optimal control or fuzzy control [37], and feedback decoupling control [38], [39]. These control strategies are dependent on the states of the controlled plant models. In this study, we introduce the model predictive control (MPC) strategy to design closed-loop brain stimulation for epileptic seizure suppression [40], [41]. MPC strategy does not need the controlled plant model or its states, but uses the system input and output data to identify the predictive model for control. Because of its good performance and robustness, MPC has been extremely successful in industrial, medical, and automotive applications [42], [43], such as refining and chemical industries control [44], unmanned aerial vehicles control [45] and closed-loop modulation of Parkinson's disease [46], [47]. MPC is a mature control strategy which iteratively computes locally optimal control signals by solving an optimisation problem over a future time horizon under certain process constraints [48]. This optimisation problem uses a predictive model of the future plant behaviour. Without prior knowledge of the plant, the predictive model can be identified based on the historical input and output data by using the theory of system identification. At each sampling time step, the predictive model is used to predict the system output in prediction horizon and an optimal control signal is obtained by solving a constrained finite horizon optimal control problem [49], [50].

The MPC performance relies on the predictive model [50], [51]. In this study, we chose Volterra model as the predictive model to reflect the controlled plant dynamic character in the control loop. The Volterra model have shown good performance in modelling uncertain and complex nonlinear process, owing to its learning and adaptation capabilities [52]. In addition, compared with neural networks modeling, the Volterra model has a more compact structure and then its implementation in brain stimulator is generally less timeconsuming [53]. Since the Volterra model is introduced by Vito Volterra in 1930, it has been successfully applied to many nonlinear systems to describe dynamic relationships, especially complex nonlinear neural systems [54]–[56]. In [55], a nonlinear autoregressive Volterra model is applied to modeling the input-output relationship of the Hodgkin–Huxley (HH) model. In [47], a autoregressive Volterra based nonlinear model predictive control scheme is developed for adjustments of DBS parameters in basal ganglia-thalamic network and show good performance.

In this article, we consider the control of epileptic seizures as a tracking control problem [30], and design MPC strategy to suppress the epileptic seizures based on an identified nonlinear auto-regressive moving-average (NARMA) Volterra model of the complex neural model, regardless of its internal structures. The objectives of this article are twofold. First, a NARMA Volterra model is developed to predict the neural activity. Second, a framework for real-time control of epileptic seizures is provided.

The rest of this article is organized as follows. Section II introduces the methods" including identification of the neural model, design of the MPC strategy. In Section III, the simulation results demonstrate the effectiveness of MPC-based closed-loop brain stimulation. Finally, the conclusion is given in Section IV.

## II. METHODS

In this section, we design a closed-loop control framework to suppress the epileptic seizures (Fig. 1). A NMM is built as a virtual brain to explore the impacts of stimulation on neural signal. The virtual brain is treated as a black-box model, where the internal structure is unknown and only input and output data can be measured. Thus, using the input and output data obtained from black box model, a NARMA Volterra predictive model is trained to describe the relationship between the stimulation input and model output. Based the predictive model, a MPC is designed to make the model output tracing the reference signal.

## A. Black Box Computation Model

In this work, we use a NMM as the black model to describe the normal and epileptic EEG activity. The simple and detailed structure of the model is shown in Fig. 2.

As shown in Fig. 2 (a), the NMM is composed of three neuronal populations, the pyramidal cells, the excitatory interneurons and the inhibitory interneurons [13]. The pyramidal cells receive excitatory and inhibitory inputs from the excitatory interneurons and inhibitory interneurons, respectively. Simultaneously, the pyramidal cells provide excitatory input to the excitatory and inhibitory interneurons. The model input *p*(*t*) (modelled by Gaussian white noise) represents the average pre-synaptic pulse density of afferent action potentials from neighboring or distant populations. The model output can be used to simulate EEG signals. $C_1$, $C_2$, $C_3$ and $C_4$ represent the average number of synaptic connections between pyramidal cells and interneurons.

The detailed schematic of the NMM is shown in Fig. 2(b), each cell consists of two components, a sigmoid function and a second order linear transfer function. The sigmoid function $S(v) = 2e_0/[1 + e^{r(v_0-v)}]$ could convert the post-synaptic potential values to average pre-synaptic pulse density. In the sigmoid function, $2e_0$ represents the maximum firing rate, $v_0$ is the post-synaptic potential corresponding to half maximum firing rate, and $r$ is the steepness of sigmoid function. The second order linear transfer function could transform the average presynaptic pulse density into post-synaptic membrane potentials. The excitatory and inhibitory transfer functions are described as $h_e(t) = Aae^{-at}$ and $h_i(t) = Bbe^{-bt}$, respectively. $A$ and $B$ denote the average synaptic gains, and $a$ and $b$ are the average time constants.

The second order linear transfer function *he*(*t*) and *hi*(*t*) could be transformed to a pair of first order ordinary differential equations

$$
\begin{aligned}
\dot{z}_1(t) &= z_2(t) \\
\dot{z}_2(t) &= Wwx(t) - 2wz_2(t) - w^2 z_1(t)
\end{aligned}
$$

![](_page_2_Figure_2.jpeg)

Fig. 1. Closed-loop control framework. The predictive model is trained to describe the input-output relationship of the black box model using the collected data. The model predictive controller optimize the control signal based on the predictive model.

![](_page_2_Figure_4.jpeg)

Fig. 2. Schematic diagram of neural mass model. The model is composed of three neuronal populations, the pyramidal cells, the excitatory interneurons and the inhibitory interneurons. Each cell consists of two components, sigmoid function and second order linear transfer function.

where $W = A$ or $W = B$ and $w = a$ or $w = b$, $x(t)$ and $z(t)$ denote the input and output signals of the second order linear transfer functions, respectively. Thus, the dynamics of NMM is modeled by equations as follows:

$$
\begin{aligned}
\dot{y}_0 &= y_3, \\
\dot{y}_3 &= AaS(y_1 - y_2) - 2ay_3 - a^2y_0, \\
\dot{y}_1 &= y_4, \\
\dot{y}_4 &= Aa(p + C_2S(C_1y_0)) - 2ay_4 - a^2y_1, \\
\dot{y}_2 &= y_5, \\
\dot{y}_5 &= BbC_4S(C_3y_0) - 2by_5 - b^2y_2
\end{aligned}
$$

$y(t) = y_1(t) - y_2(t)$ represents the output of the NMM.

## B. NARMA Volterra Predictive Model

The relationship between input stimulation and output EEG signals is highly nonlinear. Hence, a second order NARMA Volterra model was selected to identify the inputoutput relationship of the neural mass model. The NARMA Volterra model contains two inputs, the exogenous stimulation input components and the autoregressive input components. The NARMA Volterra model is described by the following equation:

$$
\begin{aligned}
y_{e}(n) &= k_{0,0} + \sum_{i=0}^{n_{u}} k_{1,0}(i)u(n-i) \\
&\quad + \sum_{i=1}^{n_{y}} k_{0,1}(i)y(n-i) \\
&\quad + \sum_{i=0}^{n_{u}} \sum_{j=0}^{n_{u}} k_{2,0}(i,j)u(n-i)u(n-j) \\
&\quad + \sum_{i=1}^{n_{y}} \sum_{j=1}^{n_{y}} k_{0,2}(i,j)y(n-i)y(n-j) \\
&\quad + \sum_{i=0}^{n_{u}} \sum_{j=1}^{n_{y}} k_{1,1}(i,j)u(n-i)y(n-j)
\end{aligned}
$$

where $y_e$ is the predicted output signal, $u$ is the input signal and $y$ is the output signal. $k_{0,0}$, $k_{1,0}$, $k_{2,0}$, $k_{0,1}$, $k_{0,2}$ and $k_{1,1}$ is the zero-order kernel, first and second-order feedforward kernels, first and second-order feedback kernels and second-order cross kernel, respectively. $n_u$ and $n_y$ represent the memory window lengths of input and output signals.

Although NARMA Volterra model is a powerful tool for identification of nonlinear relationship between input

TABLE I
THE STANDARD VALUE OF NMM PARAMETERS

| Parameters | Interpretation                                              | Values | Unit               |
|------------|-------------------------------------------------------------|--------|--------------------|
| A          | Average excitatory synaptic gain                            | 3.25   | -                  |
| B          | Average inhibitory synaptic gain                            | 22     | -                  |
| a          | Average synaptic time constants of excitatory feedback loop | 100    | s                  |
| b          | Average synaptic time constants of inhibitory feedback loop | 50     | s                  |
| $2e_0$     | Maximum firing rate                                         | 5      | $s^{-1}$           |
| $v_0$      | Mean firing thresholds of the population                    | 6      | mV                 |
| r          | Slope of the sigmoid function                               | 0.56   | $\mathrm{mV}^{-1}$ |
| $C_1$      | Average number synaptic connectivity                        | 135    | -                  |
| $C_2$      | Average number synaptic connectivity                        | 108    | -                  |
| $C_3$      | Average number synaptic connectivity                        | 33.75  | -                  |
| $C_4$      | Average number synaptic connectivity                        | 33.75  | -                  |

and output, the high computational cost caused by the large number of estimation parameters leads to its practical limitation. To simplify calculations, the number of parameters was reduced by using Laguerre expansion method to expand the kernels on Laguerre basis functions [55]. The Laguerre basis functions could be obtained as follows:

$$
\begin{aligned}
\rho^{0}(i) &= \sqrt{\alpha}\rho^{0}(i-1) + \sqrt{1-\alpha}\delta(i) \\
\rho^{j}(i) &= \sqrt{\alpha}\rho^{j}(i-1) + \sqrt{\alpha}\rho^{j-1}(i) - \rho^{j-1}(i-1)
\end{aligned}
$$

where $j=0,1,\ldots,L_u-1$ ($L_y-1$) represents the number of Laguerre basis functions, $i=0,1,\ldots,n_u$ ($n_y$). $\delta(\cdot)$ is the delta function, and $\alpha \in (0,1)$ is the Laguerre time scale factor, which determines the rate of exponential relaxation, a smaller $\alpha$ corresponds to more rapid decay. We choose the $\alpha$ value through trial-and-error, test the $\alpha$ values from 0 to 1 with a step of 0.01. Based on the Laguerre expansion method, the NARMA Volterra model can be simplified to:

$$
\begin{aligned}
y_{e}(n) &= k_{0,0} + \sum_{i=0}^{L_{u}-1} c_{1,0}(i)\varphi_{i}^{u}(n) \\
&\quad + \sum_{i=1}^{L_{y}-1} c_{0,1}(i)\varphi_{i}^{y}(n) \\
&\quad + \sum_{i=0}^{L_{u}-1} \sum_{j=0}^{L_{u}-1} c_{2,0}(i,j)\varphi_{i}^{u}(n)\varphi_{j}^{u}(n) \\
&\quad + \sum_{i=0}^{L_{y}-1} \sum_{j=0}^{L_{y}-1} c_{0,2}(i,j)\varphi_{i}^{y}(n)\varphi_{j}^{y}(n) \\
&\quad + \sum_{i=0}^{L_{u}-1} \sum_{j=0}^{L_{y}-1} c_{1,1}(i,j)\varphi_{i}^{u}(n)\varphi_{i}^{y}(n) \\
\varphi_{i}^{u}(n) &= \sum_{k=1}^{n_{u}} \rho_{i}^{u}(k)u(n-k), \quad i = 0, \dots, L_{u} - 1 \\
\varphi_{j}^{y}(n) &= \sum_{k=1}^{n_{y}} \rho_{j}^{y}(k)y(n-k), \quad j = 0, \dots, L_{y} - 1
\end{aligned}
$$

Here, the parameters  $c_{1,0}(i)$ ,  $c_{0,1}(j)$ ,  $c_{2,0}(i,j)$ ,  $c_{0,2}(i,j)$ ,  $c_{1,1}(i,j)$ ,  $(i=0,\ldots,L_u-1;j=0,\ldots,L_y-1)$  are estimated by the recursive least square (RLS) method.

![](_page_3_Picture_9.jpeg)

Fig. 3. The block diagram of NARMA Volterra based model predictive control strategy.

### C. Model Predictive Control Framework

Based on the identified NARMA Volterra model, a model predictive control strategy is proposed to suppress epileptic seizures. As shown in Fig. 3, the main structures of MPC include controlled object (NMM), NARMA Volterra predictive model, cost function min *J* and smoothing model.

The objective of model predictive control algorithm is to minimize the cost function J chosen as:

$$
J = \sum_{l=1}^{n_p} \left[ y_e(n+l) - y_r(n+l) \right]^2
$$

where  $y_e$  and  $y_r$  are predicted output and reference trajectories, respectively. Here,  $n_p$  represents prediction horizon of the MPC algorithm.

In order to obtain a smooth control, the reference trajectory  $y_r = [y_r(n+1), y_r(n+2), \dots, y_r(n+n_n)]$  is designed as,

$$
y_r(n+l) = \alpha^l y(n) + (1-\alpha^l) y_d(n+l), \quad l = 1, \dots, n_p
$$

where  $\alpha^l \in (0, 1)$  is a smoothing factor, and  $y_d$  represents the normal EEG signal.

Derived from the NARMA Volterra model, the predictive output  $y_e = [y_e(n+1), y_e(n+2), \dots, y_e(n+n_p)]$  is given as follows:

$$
\begin{aligned}
y_{e}(n+l) &= k_{0,0} + \sum_{i=0}^{n_{u}} k_{1,0}(i)u(n+l-i) \\
&\quad + \sum_{i=1}^{n_{y}} k_{0,1}(i)y(n+l-i) \\
&\quad + \sum_{i=0}^{n_{u}} \sum_{j=0}^{n_{u}} k_{2,0}(i,j)u(n+l-i)u(n+l-j) \\
&\quad + \sum_{i=1}^{n_{y}} \sum_{j=1}^{n_{y}} k_{0,2}(i,j)y(n+l-i)y(n+l-j) \\
&\quad + \sum_{i=0}^{n_{u}} \sum_{j=1}^{n_{y}} k_{1,1}(i,j)u(n+l-i)y(n+l-j) \\
&\quad + e(n)
\end{aligned}
$$

where  $e(n) = y(n) - y_e(n)$  represents the predictive error.

Based on the predictive functional control algorithm, the control output can be designed as:

$$
u(n+i) = \mu \cdot A, \quad i \in [1, n_p]
$$

where $\mu$ is coefficient and $A=1$ is the value of the base function. Here, $n_p$ represents prediction horizon. Derived from Eqs. (6)-(9), the cost function $J$ can be described by the following equation,

$$
\begin{aligned}
J(n+l) &= \sum_{l=1}^{n_p} \bigg[k_{0,0} + k_{1,0}(0)\mu A + \sum_{i=1}^{n_u} k_{1,0}(i)u(n+l-i) + \sum_{i=1}^{n_y} k_{0,1}(i)y(n+l-i) \\
&\quad + k_{2,0}(0)\mu^2 A^2 + \sum_{i=1}^{n_u} k_{2,0}(0,j)\mu Ay(n+l-i) + \sum_{i=1}^{n_u} \sum_{j=1}^{n_u} k_{2,0}(i,j)u(n+l-i)u(n+l-j) \\
&\quad + \sum_{i=1}^{n_y} \sum_{j=1}^{n_y} k_{0,2}(i,j)y(n+l-i)y(n+l-j) + \sum_{j=1}^{n_y} k_{1,1}(i,j)\mu Ay(n+l-j) \\
&\quad + \sum_{i=1}^{n_u} \sum_{j=1}^{n_y} k_{1,1}(i,j)u(n+l-i)y(n+l-j) - \alpha y_r(n+j-1) - (1-\alpha)y_s(n+1)\bigg]^2
\end{aligned}
$$

Then, the cost function J(n+l) can be transformed to:

$$
\begin{aligned}
J(n+1) &= f^{2}(\mu) \\
f(\mu) &= C_{A} \cdot \mu^{2} + C_{B} \cdot \mu + C_{C} \\
C_{A} &= \sum_{l=1}^{n_{p}} (k_{2,0}(0,0)A^{2}) \\
C_{B} &= \sum_{l=1}^{n_{p}} \bigg[k_{1,0}(0)A + \sum_{j=1}^{n_{u}} k_{2,0}(0,j)Ay(n+l-i) \\
&\quad + \sum_{j=1}^{n_{y}} k_{1,1}(i,j)Ay(n+l-j)\bigg] \\
C_{C} &= \sum_{l=1}^{n_{p}} \bigg[k_{0,0} - \alpha y_{r}(n+j-1) - (1-\alpha)y_{s}(n+1) \\
&\quad + \sum_{i=1}^{n_{u}} k_{1,0}(i)u(n+l-i) + \sum_{i=1}^{n_{y}} k_{0,1}(i)y(n+l-i) \\
&\quad + \sum_{i=1}^{n_{u}} \sum_{j=1}^{n_{u}} k_{2,0}(i,j)u(n+l-i)u(n+l-j) \\
&\quad + \sum_{i=1}^{n_{y}} \sum_{j=1}^{n_{y}} k_{0,2}(i,j)y(n+l-i)y(n+l-j) \\
&\quad + \sum_{i=1}^{n_{u}} \sum_{j=1}^{n_{y}} k_{1,1}(i,j)u(n+l-i)y(n+l-j)\bigg]
\end{aligned}
$$

The optimal value of  $\mu$  satisfying the min J could be calculated as Algorithm 1.

**Algorithm 1** Optimal Control Signal Solution Algorithm
**Input:** Stimulus value $u$; Neural mass model output $y$
**Output:** Optimal value $\mu_0$
- Calculate the smooth reference trajectory $y_r$
- Predict the neural mass model output $y_e$ according to Eq.(8)
- Derive the cost function $J$ according to Eq.(6)
- **if** $C_A = 0$ **then**
  - $f(\mu) = C_B \cdot \mu + C_C$ is a linear function $\min J = f^2(\mu_0) = 0$
  - $\mu_0 = -C_B/C_C$
- **else**
  - $f(\mu) = C_A \cdot \mu^2 + C_B \cdot \mu + C_C$ is a quadratic function $\Delta = C_B^2 - 4C_AC_C$
  - **if** $\Delta > 0$ **then**
    - $\min J = f^2(\mu_{1,2}) = 0$
    - $\mu_1 = (-C_B + \sqrt{\Delta})/2C_A$
    - $\mu_2 = (-C_B - \sqrt{\Delta})/2C_A$
  - **if** $\Delta = 0$ **then**
    - $\min J = f^2(\mu_0) = 0$
    - $\mu_0 = -C_B/2C_A$
  - **if** $\Delta < 0$ **then**
    - $\min J = f^2(\mu_0) > 0$
    - $\mu_0 = -C_B/2C_A$
- **end if**

Hence, the optimal value of  $\mu$  in each step can be calculated from the cost function, and the control signal u(n) can be applied to the controlled object.

#### III. RESULT

## A. Different Behaviors of the Neural Mass Model

In the neural mass model, the neuronal behaviour is primarily influenced by excitatory synaptic gain A and inhibitory synaptic gain B; they determine the amplitude of the post-synaptic potential. The experiments show that the ratio A/B, which can be related to the balance between excitatory and inhibitory processes, directly influences the type of signal dynamics generated by the model [13]. The NMM with standard parameter values (Table. I) can generate normal EEG signals [3], [7], [13], while varying physiologically meaningful parameters can lead to various types of epileptiform waves.

Fig. 4 shows the different output signals of the NMM in normal and epileptic states, respectively. The neural mass model is simulated with constant inhibitory synaptic gain B and different excitatory synaptic gain A (3.25, 3.59, 3.60 and 3.75). The epileptic spikes appear and increase gradually as the synaptic gain increases. It has been comprehensively analyzed in [13] that the simulated signals are extremely similar to the real depth-EEG signal recorded from a neocortical structure

![](_page_5_Figure_2.jpeg)

Fig. 4. The output signals of the neural mass model and corresponding PSD. The synaptic gains are set as 3.25, 3.59, 3.60 and 3.75. The <sup>A</sup> = 3.25 corresponds to normal state, and <sup>A</sup> = 3.59, 3.60 and 3.75 corresponds to epileptic state.

![](_page_5_Figure_4.jpeg)

Fig. 5. Identification and validation process. **(a)** The identification process. **(b)** The validation process.

before and during a seizure. The power spectral density of the EEG signals is calculated using the Chronux neural signal analysis package (www.chronux.org) and MATLAB R2017b, the sliding window length was 1 s, the step size was 0.1 s size. The spectral power under the epileptic state is quite different from that of the normal state. As shown in the spectrograms (Fig. 4, bottom), the spectral power of low-frequency band in the epileptic state is significantly higher than that in the normal state. Thus, the synaptic gain between pyramidal cells and interneurons plays an important role in the emergence of the epileptic behaviors.

#### B. Identification of NARMA Volterra Model

In NARMA Volterra model identification, we use a Gaussian white noise with the mean value 0 Hz and the variance 200 Hz<sup>2</sup> as an input signal to stimulate the NMM, collect the input-output data at 40 hz sampling frequency, and use this data to fit the NARMA Volterra model parameters. The input and output data are divided into a training set and a test set. The training set is used to identify the parameters of NARMA Volterra model, and the test set is used to validate the prediction performance of the identified NARMA Volterra model.

![](_page_6_Figure_2.jpeg)

Fig. 6. The control results. *case* 1: the desired EEG tracing is generated by a neural mass model with standard parameters. (a) Without system disturbances, (b) system disturbances is sinusoidal signal with 20 peak-to-peak value, (c) system disturbances is square signal with 20 peak-to-peak value, (d) system disturbances is Gaussian white noise with the mean value 0 and the variance 100. The system output, reference tracing signal, control signal, tracing error and system disturbances are shown clearly. The controller is switched on at t = 5s.

![](_page_6_Figure_4.jpeg)

Fig. 7. The control results. case 2: the desired EEG tracing is a channel clinical scalp EEG waveforms. (a) Without system disturbances, (b) system disturbances is sinusoidal signal with 20 peak-to-peak value, (c) system disturbances is square signal with 20 peak-to-peak value, (d) system disturbances is Gaussian white noise with the mean value 0 and the variance 100. The system output, reference tracing signal, control signal, tracing error and system disturbances are shown clearly. The controller is switched on at t = 5s.

In the entire identification process, the cost function converges before halting training. Fig. 5 (a) and (b) show the stage of training completion and validation process, the variable 'error' represents the difference between the training (test) data and the estimated (predicted) data. It's shown that the predictive error doesn't increase significantly compared to the identification error, and both of them maintain smaller values, which represent a good predictive performance.

In order to quantify the performance of NARMA Volterra in identification, the normalized mean square error (NMSE) is calculated in both identified and validated results. The NMSE is expressed as

$$
\text{NMSE} = \frac{\sum_{n=1}^{N} [y(n) - y_e(n)]^2}{\sum_{n=1}^{N} y(n)^2}
$$

where y(n) is the actual output of the NMM and  $y_e(n)$  is the estimated value. N is the total length of the data set. The NMSE in identification process and validation process are 0.0307 and 0.0717, respectively, which denotes good identification quality.

![](_page_7_Figure_2.jpeg)

Fig. 8. Control performance. **(a)** The power of each band in case 1. **(b)** The power of each band in case 2.

![](_page_7_Figure_4.jpeg)

Fig. 9. Open-loop control and MPC performance. **(a)** The simulation results of open-loop control. **(b)** The simulation results of MPC. **(c)** The control error in each stage. **(d)** The energy consumption in each stage.

## C. Performance of Model Predictive Control Strategy

In this section, we conduct numerical experiments to illustrate the effectiveness of the proposed MPC strategy on the suppression of epileptic seizures. Here, the synaptic gain A is set to 3.75 in the NMM to simulate the epileptic seizures. The MPC strategy is applied on the NMM in two cases. In *case* 1, the reference EEG is generated by a NMM with standard parameters. In order to simulate more realistic clinical application, we chose a channel clinical scalp EEG waveforms from CHB-MIT database as the reference trajectory in *case* 2 [30], [57]. In each experiment, the simulation duration is 10s and the control signal is switched on at t = 5s.

Fig. 6 and Fig. 7 show the control effects, including control signals, tracking error and system disturbances under the proposed control algorithms in *case* 1 and *case* 2. The disturbances signals are generated to simulate the unknow disturbance such as measurement noises in actual application environment. Fig. 6 (a) and Fig. 7 (a) are simulated without system disturbances. Meanwhile, the system disturbances in Fig. 6 (b)-(d) and Fig. 7 (b)-(d) are sinusoidal signal with 20 peak-to-peak value, square signal with 20 peak-to-peak value and Gaussian white noise with the mean value 0 and the variance 100, respectively. As shown in the Fig. 6 and Fig. 7 without control, the output of NMM exhibits high amplitude spikes that is assumed to be epileptic state. The epileptic seizures is effectively suppressed with the controller switching on at 5s. Despite various system distractions, all of the outputs of the NMM effectively track the reference trajectory, and the tracking error is around 0. It demonstrates effectiveness and robustness of the MPC strategy in suppression of epileptic seizures.

Clinically, EEG spectral analysis is a powerful method for the diagnosis of epilepsy due to differences between normal and epileptic EEG signals. Some studies have shown that there is a significant association between temporal epilepsies and rhythmic the δ and β activity, besides, the δ and θ frequency activity is regarded as the hallmark of generalized epilepsies [58]. In order to further show the control performances of MPC strategy, the power of δ, θ, α and β bands before and after control is comprehensive analysed in *case* 1 and *case* 2. As shown in Fig. 8, the power of these four bands in the epileptic state (without control) is much higher than that in the normal state. With the MPC controller on, the power is effectively reduced and close to the normal level, even under system disturbances.

The performance of traditional open-loop stimulator and MPC-based closed-loop stimulator is compared and analyzed in the Fig. 9. In order to simulate the changes of clinical conditions, the synaptic gain A is adjusted from 3.75 to 3.58, 3.70 and 3.55. Under the open-loop control, the control error increases significantly as the synaptic gain A changes (Fig. 9 (a)); on the contrary, the MPC controller shows good performance in the whole process (Fig. 9 (b)). We use rootmean-square-error (RMSE) and energy consumption to quantify the control effect. The RMSE is defined as

$$
\text{RMSE} = \sqrt{\frac{1}{N} \sum_{n=1}^{N} [y(n) - y_d(n)]^2}
$$

where *y* is the actual output and *yd* is the tracking trajectory. *N* is the total length of output signals. The energy consumption is defined as

$$
\text{Energy} = \sqrt{\frac{1}{T} \int_{T} u^2 dt}
$$

where *u* is the control signals and *T* denotes the total time of control signals. As shown in Fig. 9 (a), the control error of open-loop control and MPC is close to each other in the 1st stage. Nevertheless, the open-loop control error becomes obviously higher as the synaptic gain A changes, especially in the 2nd and 4th stages. By contrast, the MPC control error is relatively small in the whole process. The energy consumption is also a key performance indicator for implantable stimulator. The energy consumption of MPC-based stimulator is lower than open-loop stimulator in each stage.

# IV. CONCLUSION

In this article, a closed-loop model predictive control strategy is designed to eliminate the epileptic seizures. Due to the limitation of ethics, it's hard to testify the control strategy directly on biological experiment. Hence, computational model can be used as an effective alternative test platform. In this article, a NMM which could reproduce the different types of real EEG signals recorded in human hippocampus is used to testify the effectiveness of the proposed strategy [13]. We assume the NMM as a black box model, and collect stimulation input data and output EEG data from it. Then a NARMA Volterra model is used to identified the input-output relationship of black box model. Hence, a model predictive controller based on the NARMA Volterra model is designed to make the model output signal to track the reference signal. It has been illustrated by simulations that the epileptic seizures can be suppressed using closed-loop model predictive control, even if there are various system disturbances. The model predictive control strategy combined with system identification techniques can guarantee the tracking of desired EEG signal without knowledge of the physiological properties of the system.

The NMM used in this article consisting of three components is a single-input, single-output system. However, the brain networks in reality may different from the NMM model, the stimulation may only influence a subpopulation of neurons. Hence, the beforehand controllability (observability) analysis of corresponding brain networks is deemed to be necessary for the control system design. In our previous study [59], we have made a comprehensive analysis about the controllability and observability of three-node network, which could play an important role in suitable control framework design.

In the present simulation study, the normal EEG signal is used as the desired trajectory to design and evaluate the proposed algorithm. In practical applications, it may be appropriate to record EEG signals in a patient's health condition as his own desired targets. Furthermore, many studies demonstrate that the seizures can be predicted using characteristics of neuronal activity, such as synchronization or PSD [60], [61]. The further research on the closed-loop control based on such characteristics of neuronal activity is interesting and necessary. The effectiveness and robustness of the NARMA based GPC algorithm is proved on the NMM model, at the same time, the GPC consumes more computational resources for clinical applications compare to the high efficiency control strategy, such as feedback decoupling control strategy [62]– [64]. However, this disadvantage can be solved with the improvement of processor power.

# REFERENCES

- [1] P. N. Banerjee, D. Filippi, and W. Allen Hauser, "The descriptive epidemiology of epilepsy—A review," *Epilepsy Res.*, vol. 85, no. 1, pp. 31–45, Jul. 2009.
- [2] C.-X. Han, J. Wang, G.-S. Yi, and Y.-Q. Che, "Investigation of EEG abnormalities in the early stage of Parkinson's disease," *Cognit. Neurodyn.*, vol. 7, no. 4, pp. 351–359, Aug. 2013.
- [3] F. Wendling, F. Bartolomei, J. J. Bellanger, J. Bourien, and P. Chauvel, "Epileptic fast intracerebral EEG activity: Evidence for spatial decorrelation at seizure onset," *Brain*, vol. 126, no. 6, pp. 1449–1459, Jun. 2003.

- [4] H. E. Scharfman, "The neurobiology of epilepsy," *Current Neurol. Neurosci. Rep.*, vol. 7, no. 4, pp. 348–354, Jul. 2007.
- [5] F. Wendling, F. Bartolomei, F. Mina, C. Huneau, and P. Benquet, "Interictal spikes, fast ripples and seizures in partial epilepsies–combining multi-level computational models with experimental data: Computational and experimental models of epilepsy," *Eur. J. Neurosci.*, vol. 36, no. 2, pp. 2164–2177, Jul. 2012.
- [6] C. Rummel, E. Abela, M. Hauf, R. Wiest, and K. Schindler, "Ordinal patterns in epileptic brains: Analysis of intracranial EEG and simultaneous EEG-fMRI," *Eur. Phys. J. Special Topics*, vol. 222, no. 2, pp. 569–585, Jun. 2013.
- [7] F. Wendling, P. Benquet, F. Bartolomei, and V. Jirsa, "Computational models of epileptiform activity," *J. Neurosci. Methods*, vol. 260, pp. 233–251, Feb. 2016.
- [8] W. W. Lytton, "Computer modelling of epilepsy," *Nature Rev. Neurosci.*, vol. 9, no. 8, pp. 626–637, Aug. 2008.
- [9] J. G. R. Jefferys, "Models and mechanisms of experimental epilepsies," *Epilepsia*, vol. 44, no. s12, pp. 44–50, Dec. 2003.
- [10] F. H. Lopes da Silva, A. van Rotterdam, P. Barts, E. van Heusden, and W. Burr, "Models of neuronal populations: The basic mechanisms of rhythmicity," *Prog Brain Res*, vol. 45, pp. 281–308, Jan. 1976.
- [11] F. H. Lopes da Silva, A. Hoeks, H. Smits, and L. H. Zetterberg, "Model of brain rhythmic activity: The alpha-rhythm of the thalamus," *Kybernetik*, vol. 15, no. 1, pp. 27–37, 1974.
- [12] B. H. Jansen, G. Zouridakis, and M. E. Brandt, "A neurophysiologicallybased mathematical model of flash visual evoked potentials," *Biol. Cybern.*, vol. 68, no. 3, pp. 275–283, Jan. 1993.
- [13] F. Wendling, J. J. Bellanger, F. Bartolomei, and P. Chauvel, "Relevance of nonlinear lumped-parameter models in the analysis of depth-EEG epileptic signals," *Biol. Cybern.*, vol. 83, no. 4, pp. 367–378, Sep. 2000.
- [14] F. Wendling, F. Bartolomei, J. J. Bellanger, and P. Chauvel, "Epileptic fast activity can be explained by a model of impaired GABAergic dendritic inhibition: Epileptic activity explained by dendritic dis-inhibition," *Eur. J. Neurosci.*, vol. 15, no. 9, pp. 1499–1508, May 2002.
- [15] P. Rajna and C. Lona, "Sensory stimulation for inhibition of epileptic seizures," *Epilepsia*, vol. 30, no. 2, pp. 168–174, Apr. 1989.
- [16] I. Osorio and M. G. Frei, "Seizure abatement with single dc pulses: Is phase resetting at play?" *Int J Neural Syst.*, vol. 19, no. 3, pp. 149–156, 2009.
- [17] S. Saillet *et al.*, "Neural adaptation to responsive stimulation: A comparison of auditory and deep brain stimulation in a rat model of absence epilepsy," *Brain Stimulation*, vol. 6, no. 3, pp. 241–247, May 2013.
- [18] J. Parvizi, "Electrical brain stimulation," *Brain Stimulation*, vol. 8, no. 2, p. 437, Mar. 2015.
- [19] D. Tarsy, "Deep brain stimulation and movement disorders," *Epilepsy Behav.*, vol. 2, no. 3, pp. S45–S54, Jun. 2001.
- [20] M. Sprengers, K. Vonck, E. Carrette, A. G. Marson, and P. Boon, "Deep brain and cortical stimulation for epilepsy," in *Cochrane Database of Systematic Reviews*, The Cochrane Collaboration, ed. Chichester, U.K.: Wiley, Jun. 2014, Art. no. CD008497.
- [21] C. H. Halpern, U. Samadani, B. Litt, J. L. Jaggi, and G. H. Baltuch, "Deep brain stimulation for epilepsy," *Neurotherapeutics*, vol. 5, no. 1, pp. 59–67, 2008.
- [22] C. E. Santana-Gomez *et al.*, "Transcranial focal electrical stimulation reduces seizure activity and hippocampal glutamate release during status epilepticus," in *Proc. 37th Annu. Int. Conf. IEEE Eng. Med. Biol. Soc. (EMBC)*, Milan, Italy, Aug. 2015, pp. 6586–6589.
- [23] A. Berényi, M. Belluscio, D. Mao, and G. Buzsáki, "Closed-loop control of epilepsy by transcranial electrical stimulation," *Science*, vol. 337, no. 6095, pp. 735–737, 2012.
- [24] R. A. Sandler *et al.*, "Designing patient-specific optimal neurostimulation patterns for seizure suppression," *Neural Comput.*, vol. 30, no. 5, pp. 1180–1208, May 2018.
- [25] S. Järvenpää, J. Peltola, S. Rainesalo, E. Leinonen, K. Lehtimäki, and K. Järventausta, "Reversible psychiatric adverse effects related to deep brain stimulation of the anterior thalamus in patients with refractory epilepsy," *Epilepsy Behav.*, vol. 88, pp. 373–379, Nov. 2018.
- [26] E. Moro, Y.-Y. W. Poon, A. M. Lozano, J. A. Saint-Cyr, and A. E. Lang, "Subthalamic nucleus stimulation: Improvements in outcome with reprogramming," *JAMA Neurol.*, vol. 63, no. 9, p. 1266, 2006.
- [27] P. Ghasemi, T. Sahraee, and A. Mohammadi, "Closed- and open-loop deep brain stimulation: Methods, challenges, current and future aspects," *J. Biomed. Phys. Eng.*, vol. 8, no. 2, pp. 209–216, Jul. 2018.
- [28] S.-F. Liang, Y.-C. Liao, F.-Z. Shaw, D.-W. Chang, C.-P. Young, and H. Chiueh, "Closed-loop seizure control on epileptic rat models," *J. Neural Eng.*, vol. 8, no. 4, Aug. 2011, Art. no. 045001.

- [29] X. Liu, Q. Gao, and X.-L. Li, "Control of epileptiform spikes based on nonlinear unscented Kalman filter," *Chin. Phys. B*, vol. 23, no. 1, Jan. 2014, Art. no. 010202.
- [30] Y. Ge *et al.*, "Robust closed-loop control of spike-and-wave discharges in a thalamocortical computational model of absence epilepsy," *Sci. Rep.*, vol. 9, no. 1, p. 9093, Dec. 2019.
- [31] M. D'Amelio and P. M. Rossini, "Brain excitability and connectivity of neuronal assemblies in Alzheimer's disease: From animal models to human findings," *Prog. Neurobiol.*, vol. 99, no. 1, pp. 42–60, Oct. 2012.
- [32] Y. Zhu, J. Wang, H. Li, B. Deng, and C. Liu, "Modulation of parkinsonian state with uncertain disturbance based on sliding mode control," *IEEE Trans. Neural Syst. Rehabil. Eng.*, vol. 25, no. 11, pp. 2026–2034, Nov. 2017.
- [33] R. A. Sandler, D. Song, R. E. Hampson, S. A. Deadwyler, T. W. Berger, and V. Z. Marmarelis, "Hippocampal closed-loop modeling and implications for seizure stimulation design," *J. Neural Eng.*, vol. 12, no. 5, 2015, Art. no. 056017.
- [34] J. Wang, E. Niebur, J. Hu, and X. Li, "Suppressing epileptic activity in a neural mass model using a closed-loop proportional-integral controller," *Sci. Rep.*, vol. 6, no. 1, p. 27344, Jul. 2016.
- [35] X. Liu, Q. Gao, B. Ma, J. Du, and W. Ren, "Analysis and control of epileptiform spikes in a class of neural mass models," *J. Appl. Math.*, vol. 2013, pp. 1–11, May 2013.
- [36] Y. Cao, K. Ren, F. Su, B. Deng, X. Wei, and J. Wang, "Suppression of seizures based on the multi-coupled neural mass model," *Chaos Interdiscipl. J. Nonlinear Sci.*, vol. 25, no. 10, Oct. 2015, Art. no. 103120.
- [37] X. Liu, H. Liu, Y. Tang, and Q. Gao, "Fuzzy PID control of epileptiform spikes in a neural mass model," *Nonlinear Dyn.*, vol. 71, nos. 1–2, pp. 13–23, Jan. 2013.
- [38] N. Chakravarthy, S. Sabesan, K. Tsakalis, and L. Iasemidis, "Controlling epileptic seizures in a neural mass model," *J. Combinat. Optim.*, vol. 17, no. 1, pp. 98–116, Jan. 2009.
- [39] K. Tsakalis, N. Chakravarthy, S. Sabesan, L. D. Iasemidis, and P. M. Pardalos, "A feedback control systems view of epileptic seizures," *Cybern. Syst. Anal.*, vol. 42, no. 4, pp. 483–495, Jul. 2006.
- [40] H. Peng, Z.-J. Yang, W. Gui, M. Wu, H. Shioya, and K. Nakano, "Nonlinear system modeling and robust predictive control based on RBF-ARX model," *Eng. Appl. Artif. Intell.*, vol. 20, no. 1, pp. 1–9, Feb. 2007.
- [41] S. Richter, C. N. Jones, and M. Morari, "Computational complexity certification for real-time MPC with input constraints based on the fast gradient method," *IEEE Trans. Autom. Control*, vol. 57, no. 6, pp. 1391–1403, Jun. 2012.
- [42] H. Peng, H. Shioya, X. Peng, and K. Sato, "Nonlinear MPC based on the state-space form of RBF-ARX model," in *Proc. IEEE Int. Conf. Control Appl.*, vol. 2, Taipei, Taiwan, Sep. 2004, pp. 1679–1684.
- [43] M. Ławry ´nczuk, *Computationally Efficient Model Predictive Control Algorithms* (Studies in Systems, Decision and Control), vol. 3. Cham, Switzerland: Springer, 2014.
- [44] M. L. Darby, *Industrial MPC of Continuous Processes*. 2014.
- [45] M. Kamel, T. Stastny, K. Alexis, and R. Siegwart, *Model Predictive Control for Trajectory Tracking of Unmanned Aerial Vehicles Using Robot Operating System*. Cham, Switzerland: Springer, 2017.
- [46] C. Liu *et al.*, "Closed-loop modulation of the pathological disorders of the basal ganglia network," *IEEE Trans. Neural Netw. Learn. Syst.*, vol. 28, no. 2, pp. 371–382, Feb. 2017.
- [47] F. Su *et al.*, "Nonlinear predictive control for adaptive adjustments of deep brain stimulation parameters in basal ganglia–thalamic network," *Neural Netw.*, vol. 98, pp. 283–295, Feb. 2018.
- [48] E. F. Camacho and C. Bordons, *Model Predictive Control*. London, U.K.: Springer, 2004.
- [49] D. Q. Mayne, J. B. Rawlings, C. V. Rao, and P. O. M. Scokaert, "Constrained model predictive control: Stability and optimality," *Automatica*, vol. 36, no. 6, pp. 789–814, Jun. 2000.
- [50] H.-G. Han, L. Zhang, Y. Hou, and J.-F. Qiao, "Nonlinear model predictive control based on a self-organizing recurrent neural network," *IEEE Trans. Neural Netw. Learn. Syst.*, vol. 27, no. 2, pp. 402–415, Feb. 2016.
- [51] Y. Yang, O. G. Sani, E. F. Chang, and M. M. Shanechi, "Dynamic network modeling and dimensionality reduction for human ECoG activity," *J. Neural Eng.*, vol. 16, no. 5, Aug. 2019, Art. no. 056014.
- [52] F. J. Doyle, III, B. A. Ogunnaike, and R. K. Pearson, "Nonlinear modelbased control using second-order Volterra models," *Automatica*, vol. 31, no. 5, pp. 697–714, 1995.

- [53] F. Giannini *et al.*, "Neural networks and volterra series for time-domain power amplifier behavioral models," *Int. J. RF Microw. Comput.-Aided Eng.*, vol. 17, no. 2, pp. 160–168, Mar. 2007.
- [54] M.-C. Hsiao, D. Song, and T. W. Berger, "Nonlinear dynamical model based control of *in vitro* hippocampal output," *Frontiers Neural Circuits*, vol. 7, p. 20, Feb. 2013.
- [55] S. E. Eikenberry and V. Z. Marmarelis, "A nonlinear autoregressive volterra model of the Hodgkin–Huxley equations," *J. Comput. Neurosci.*, vol. 34, no. 1, pp. 163–183, Feb. 2013.
- [56] T. W. Berger *et al.*, "A hippocampal cognitive prosthesis: Multiinput, multi-output nonlinear modeling and VLSI implementation," *IEEE Trans. Neural Syst. Rehabil. Eng.*, vol. 20, no. 2, pp. 198–211, Mar. 2012.
- [57] A. L. Goldberger *et al.*, "PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals," *Circulation*, vol. 101, no. 23, p. E215, Jun. 2000.
- [58] F. Rosenow, K. M. Klein, and H. M. Hamer, "Non-invasive EEG evaluation in epilepsy diagnosis," *Expert Rev. Neurotherapeutics*, vol. 15, no. 4, pp. 425–444, Apr. 2015.

- [59] F. Su, J. Wang, H. Li, B. Deng, H. Yu, and C. Liu, "Analysis and application of neuronal network controllability and observability," *Chaos: Interdiscipl. J. Nonlinear Sci.*, vol. 27, no. 2, Feb. 2017, Art. no. 023103.
- [60] I. Osorio, M. G. Frei, and S. B. Wilkinson, "Real-time automated detection and quantitative analysis of seizures and short-term prediction of clinical onset," *Epilepsia*, vol. 39, no. 6, pp. 615–627, Jun. 1998.
- [61] K. Lehnertz *et al.*, "Seizure prediction by nonlinear EEG analysis," *IEEE Eng. Med. Biol. Mag.*, vol. 22, no. 1, pp. 57–63, Jan. 2003.
- [62] K. Tsakalis and L. Iasemidis, "Control aspects of a theoretical model for epileptic seizures," *Int. J. Bifurcation Chaos*, vol. 16, no. 07, pp. 2013–2027, Jul. 2006.
- [63] N. Chakravarthy, S. Sabesan, L. Iasemidis, and K. Tsakalis, "Controlling synchronization in a neuron-level population model," *Int. J. Neural Syst.*, vol. 17, no. 2, pp. 123–138, Apr. 2007.
- [64] N. Chakravarthy, K. Tsakalis, S. Sabesan, and L. Iasemidis, "Homeostasis of brain dynamics in epilepsy: A feedback control systems perspective of seizures," *Ann. Biomed. Eng.*, vol. 37, no. 3, pp. 565–585, Mar. 2009.
