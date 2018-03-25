---
title: "The impact of earthquake cycle variability on neotectonic slip rate 
estimates"
author:
  name:
    first: Richard
    last: Styron
  affil:
    no: 1
    address: Earth Analysis, 21855 Bear Creek Road, Los Gatos CA 95033 USA
  email: richard.h.styron@gmail.com

journal_abbr: se
running-title: Impact of earthquake cycle on slip rates

abstract: "abstract"
...

# Introduction

Fault slip rates are generally estimated by dividing measurements of the offset 
of geologic 'marker' features by the time over which that offset accumulated. 
The uncertainty in the resulting slip estimate is typically treated as 
epistemic, through the propagation of the measurement uncertainties on the 
offset and time quantities (e.g., **refs**). However, for slip rate estimates 
on active faults made from offset measurements near the fault trace (i.e., 
within a horizontal distance that is a small fraction of the fault's locking 
depth), the episodic nature of surface displacement due to the earthquake cycle 
will necessarily affect the results: If the measurements are taken immediately 
before an earthquake, the measured offset and resulting slip rate estimate will 
be lower than average, while if the measurements are taken immediately after an 
earthquake, the offset and rate will be higher.

The magnitude of the perturbation to the slip rate is, of course, a function of 
the number of cumulative earthquakes that have contributed to the measured 
offset; for older Quaternary markers that have experienced several hundred 
major earthquakes, the effects will be minor, and for bedrock geologic markers 
with kilometers of displacement, the earthquake cycle is hardly worth 
accounting for. However, due to progressive erosion of geologic markers and the 
challenge of dating many late Pliocene to early Quaternary units (which are too 
old for radiocarbon and many cosmogenic nuclide systems), geologists often have 
no choice but to choose late Pleistocene to Holocene markers to date. For 
slow-moving faults, the slip either long waiting to be released, or just 
released, may represent a sizeable fraction of the measured fault offset.

Careful paleoseismologists and neotectonicists will take this into account in 
their calculations if sufficient data is available, and especially in the years 
after a major earthquake (e.g., @rizza_earthquake_2015), and many others will 
discuss the potential effects if the data is not (e.g., **lifton_2015**). These 
workers typically only consider the time since the last earthquake, making the 
assumption (stated or not) that the earthquakes are identical in slip and 
perfectly periodic. 

However, the recurrence intervals between successive earthquakes on any given 
fault segment has some natural variability (i.e. aleatoric uncertainty); 
similarly, displacement at a measured point is not identical in each earthquake 
(e.g., **paleoseis refs**). Therefore, the measured slip rate may deviate from 
the time-averaged rate based on the amount of natural variability in the 
earthquake cycle, particularly given successive events from the tails of the 
recurrence interval or displacement distributions. Though the physical 
mechanisms responsible and the statistical character of this natural 
variability remain under debate, its effects on the estimated slip rates may 
still be estimated given some common parameterizations.

In this study, the effects of the natural variability in earthquake recurrence 
intervals and per-event displacements on neotectonic slip rate estimates are 
investigated through Monte Carlo simulations. The study is geared towards 
providing useful heuristic bounds on the aleatoric uncertainty of late 
Quaternary slip rate estimates for fault geologists, probabilistic seismic 
hazard modelers, and others for whom such uncertainties are important.

# Modeling the earthquake cycle

To study the effects of the natural variability in the earthquake cycle on 
estimated slip rates, long displacement histories of a simulated fault with 
different parameterizations of the earthquake recurrence distribution will be 
created. Then, the mean slip rate over time windows of various sizes will be 
calculated from each of the simulated displacement histories, and the 
distribution in these results will be presented.

To isolate the effects of the earthquake cycle from other phenomena that may 
affect slip rate estimates, this study does not attempt to model erosion, nor 
does it consider any measurement uncertainty in the age or offset of the 
faulted geologic markers; these measurements are assumed to be perfect. 
Additionally, though natural variability in per-earthquake displacements is 
included in the model, it is the same for all distributions. 

## background to EQ recurrence distributions

There are a handful of statistical models for earthquake recurrence interval 
distributions that are in widespread consideration. 

The most commonly used is the *exponential* distribution. This is associated 
with a Poisson process, and is the distribution that results from a prescribed 
number of earthquakes being distributed uniformly randomly within some time 
interval. Consequently, the probability of an earthquake (or other event) 
occurring at any time does not change with time since the previous event (i.e. 
the hazard function is time-invariant); this leads to the characterization of 
the exponential recurrence distribution as 'random', 'memoryless' or 
'time-independent'. The exponential distribution is also the simplest to 
describe statistically, as it requires only one parameter (the mean rate 
parameter), which is a statistical scale parameter. The standard deviation of 
samples generated from an exponential distribution is equal to the mean.

The other distributions that are in common usage are time-dependent 
distributions, meaning that the probability of an event occurring at any time 
since the previous event changes with the elapsed time since that event. This 
class of distributions includes the lognormal, Weibull, gamma, and Brownian 
Passage Time (@matthews_brownian_2002) distributions. Though these 
distributions differ in notable ways, particularly in the properties of the 
right tails at several times the mean (e.g., @davis_longer_1989, 
@matthews_brownian_2002), they share a broadly general shape, and given 
suitable parameters, generated sample sets may not be substantively different. 
In fact, the distributions are similar enough that it is difficult if not 
impossible to discriminate between them given realistic seismologic and 
paleoseismologic datasets (e.g., **Ogata, 1999**; @matthews_brownian_2002). 
These distributions are described by both the scale and shape parameters.

[the behavior of these distributions and of empirical datasets] may be 
characterized by the regularity of the spacing between events (i.e. the 
recurrence intervals): these may be periodic, unclustered (i.e., 'random'), or 
clustered. Assignment into these categories is typically done with a parameter 
known as the coefficient of variation, or $COV = \sigma / \mu$, where $\sigma$ 
is the standard deviation of the recurrence intervals, and $\mu$ is the mean 
recurrence interval.

Periodic earthquakes are those that occur more regularly than random, and have 
a $COV < 1$ (i.e. $\sigma < \mu$). These may be generated by any of the 
time-dependent distributions described above with suitable scale and shape 
parameters.

Unclustered earthquakes occur as regularly as random, and have a $COV=1$. 



### Earthquake recurrence interval distributions


\begin{figure}[t]
\includegraphics[width=8.3cm]{./figures/recurrence_dists.pdf}
\caption{Earthquake recurrence distributions. \label{eq-rec-dists}}
\end{figure}

### Earthquake slip distributions

\begin{figure}[t]
\includegraphics[width=8.3cm]{./figures/slip_dist.pdf}
\caption{Earthquake recurrence distributions. \label{slip-dist}}
\end{figure}


## Stochastic displacement histories

\begin{figure*}[t]
  \includegraphics[width=12cm]{./figures/disp_histories.pdf}
  \caption{Simulated displacement histories for each of the recurrence 
  distributions, and the 'true' mean line at 1 mm/yr in black. \emph{A}: The 
  first hundred thousand years. \emph{B}: The entire 2 million years. The 
  histories are the same in both plots. \label{disp-histories}}
\end{figure*}

\begin{figure}[t]
  \includegraphics[width=8.3cm]{./figures/event_spacing.pdf}
  \caption{Spacing of 15 simulated successive earthquakes from each recurrence 
  distribution. Note that the gap between the last displayed earthquake and the 
  right side of the plot does not represent a long recurrence interval. 
  \label{eq-spacing}}
\end{figure}


## Slip rate calculations

\begin{figure*}[t]
  \includegraphics[width=12cm]{./figures/slip_rate_envelopes.pdf}
  \caption{Caption. \label{slip-rate-envelopes}}
\end{figure*}


\begin{figure*}[t]
  \includegraphics[width=12cm]{./figures/slip_rate_estimates.pdf}
  \caption{Caption. \label{slip-rate-estimates}}
\end{figure*}


# Discussion

# Conclusions


\codeavailability{All code is licensed with a very permissive (MIT) license and 
can be found at https://github.com/cossatot/eq-slip-rate-variability/ .}

\competinginterests{The authors declare no competing interests.}

\begin{acknowledgements}
Fuck all y'all.
\end{acknowledgements}


\begin{thebibliography}{}

\end{thebibliography}
