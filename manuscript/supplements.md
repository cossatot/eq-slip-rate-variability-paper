---
title: "The impact of earthquake cycle variability on neotectonic and paleoseismic slip rate estimates: Supplemental Discussion"
author: 
    name: Richard Styron
header-includes: |
  \usepackage{booktabs}
  \renewcommand{\thefigure}{S\arabic{figure}}
  \renewcommand{\thetable}{S\arabic{table}}
---

This document contains the relevant results of two numerical experiments that
are identical to those in the manuscript, except with somewhat different slip
distributions. The first experiment uses an empirical slip distribution from
*Biasi and Weldon* (*2006*) concatenated from 13 continental earthquakes and
normalized to have a mean of 1 m. This is perhaps a more realistic slip
distribution than the lognormal distribution used in the experiment in the
manuscript, but as an empirical distribution it is limited to values that have
been observed. The second experiment uses an invariant slip of 1 m for each
earthquake, to highlight the effects of the variation in earthquake timing on
the results. 

Here, the figures showing the slip rate estimates are included; the setup
(order, axes, symbology, etc.) of these figures are identical to Figure 5 in the
manuscript to allow for easy comparison of these results, which are the most
important in the manuscript. Tables similar to Table 1 in the manuscript are
also included, so that comparison of the 'numbers' can be done as well.


## Simulations with empirical offset distribution

This experiment uses an empirical slip distribution (Figure \ref{bw_slip_dist})
from *Biasi and Weldon* (*2006*). The distribution is finite, and is composed of
~1400 total values representing field measurements and values interpolated by
those authors from between irregularly-spaced measurements from a set of 13
earthquakes, which have been normalized to the mean offset for each earthquake.
The final distribution has a mean of 1 (taken as 1 m in this experiment) and a
CV of 0.67, very slightly below the CV of 0.75 for the lognormal slip
distribution used in the experiment in the manuscript, which also has a mean of
1 m.

![Histogram of per-event fault offsets from *Biasi and Weldon* (*2006*); 
compare this to Figure 3 in the manuscript. 
\label{bw_slip_dist}](./figures/bw_slip_dist.pdf)

The empirical distribution used here is qualitatively dissimilar to the
lognormal distribution used in the manuscript. The mode of the distribution is
zero, and the central part of the distribution (values between ~0.1 m and 1.75
m) all share a broadly similar relative probability (0.4-0.55). Values greater
than 1.75 m have a much lower, and decreasing probability, until the maximum
value of about 3 m; the distribution has compact support and values above this
are strictly impossible, unlike the lognormal slip distribution used in the
manuscript which allows values to approach infinity, though at extremely low
probabilities. 

In this experiment, slip values are sampled randomly from the finite set of
values in this distribution with replacement.

![Variability in measured slip rates through time, using per-event fault 
displacements from *Biasi and Weldon* (*2006*) and all other parameters from 
the manuscript; compare this figure to Figure 5 in the
manuscript.\label{bw_slip_rate_envelopes}](./figures/bw_slip_rate_envelopes.pdf)

The results (Figure \ref{bw_slip_rate_envelopes}, Table \ref{bw_ep_unc_table})
are nearly indistinguishable from those from the experiment in the manuscript.
The sole observable difference is that the 5th percentile in the estimated slip
rates for the clusted lognormal recurrence interval is above zero following
about 20 mean earthquake cycles (20,000 years) in the experiment with the
empirical slip distribution. All other metrics are near-identical.


\begin{table}[h!]
\begin{tabular}{lllllll}
\toprule
distribution & $t$ &   5    &    25   &   50    &   75    &    95    \\
\midrule
lognormal, CV=0.5 & 2531  &  0.51 &  0.74 &  1.05 &  1.64 &  5.62 \\
      & 4843  &   0.6 &  0.79 &  1.02 &  1.38 &  2.46 \\
      & 10323 &   0.7 &  0.85 &     1 &  1.21 &  1.68 \\
      & 42103 &  0.83 &  0.93 &     1 &  1.08 &  1.23 \\
lognormal, CV=1 & 2531  &  0.45 &  0.71 &  1.13 &  2.26 &   $\infty$ \\
      & 4843  &  0.53 &  0.77 &  1.09 &  1.65 &  4.94 \\
      & 10323 &  0.64 &  0.84 &  1.06 &  1.39 &  2.32 \\
      & 42103 &   0.8 &  0.93 &  1.04 &  1.17 &  1.48 \\
lognormal, CV=2 & 2531  &  0.35 &  0.59 &  1.16 &  8.44 &   $\infty$ \\
      & 4843  &  0.43 &  0.66 &  1.02 &  2.14 &   $\infty$ \\
      & 10323 &  0.52 &  0.72 &  0.96 &  1.55 &  6.04 \\
      & 42103 &  0.71 &  0.81 &  0.94 &  1.15 &  1.85 \\
exponential, CV=1 & 2531  &  0.42 &  0.71 &  1.19 &  2.56 &   $\infty$ \\
      & 4843  &  0.51 &  0.77 &   1.1 &  1.77 &  7.02 \\
      & 10323 &  0.61 &  0.84 &  1.07 &  1.41 &  2.35 \\
      & 42103 &  0.81 &  0.95 &  1.04 &  1.15 &  1.39 \\
\bottomrule
\end{tabular}
\caption{Epistemic uncertainty table for Biasi and Weldon (2006) slip 
distribution \label{bw_ep_unc_table}}
  \end{table}


## Simulations with invariant 1 m offsets

The results from the simulation without slip variability (Figure 
\ref{nsv_slip_rate_envelopes}, Table \ref{nsv_ep_unc_table}) are broadly similar
to the results from the simulation in the manuscript. The differences are that
*a*) the effects of the position in the earthquake cycle on the measured slip
rate cycle are much more clear for up to about 7 events, and *b*) that the
variation in slip measurements at any time $t$, and the convergence of the slip
estimates, is a bit different. These are both the expected results of removing a
source of stochasticity or 'noise' from the system. With regards to *a*, the
'noise' from slip variability in the main experiment, which is uncorrelated with
the variability in the earthquake recurrence time series, serves to smooth out
the effects of the position within each early earthquake cycle. With regards to
*b*, the variations in the slip rate estimates in this experiment at some time
$t$ are a bit different than in the experiment in the manuscript: The total
variability (as approximated by the 5th and 95th percentiles) is greater when
slip variability is included (because there is more total stochasticity in the
system) but these longer tails are thinner, and the central portion of the
distributions (represented by the 25th, 50th, and 75th percentiles) are smoother
and tighter, because of the smoothing effect of the slip variability.

With increasing time and cumulative earthquakes, the slip rate estimates in this
experiment smooth out, and the variation is less at all percentiles than the
experiment in the manuscript; this is consistent with less stochasticity in the
system.

![Variability in measured slip rate through time with invariant per-event 
offsets of 1 m, and all other parameters from the manuscript; compare this to 
Figure 5 in the manuscript. 
\label{nsv_slip_rate_envelopes}](./figures/nsv_slip_rate_envelopes.pdf)


\begin{table}[h!]
\begin{tabular}{lllllll}
\toprule
distribution & $t$ &   5    &    25   &   50    &   75    &    95    \\
\midrule
lognormal, CV=0.5 & 2531  &  0.63 &  0.84 &  0.84 &  1.27 &   2.53 \\
      & 4843  &  0.69 &  0.81 &  0.97 &  1.21 &   1.61 \\
      & 10323 &  0.79 &  0.94 &  1.03 &  1.15 &   1.29 \\
      & 42103 &   0.9 &  0.96 &     1 &  1.05 &   1.14 \\
lognormal, CV=1 & 2531  &  0.51 &  0.63 &  0.84 &  1.27 &    $\infty$ \\
      & 4843  &  0.61 &  0.81 &  0.97 &  1.21 &   2.42 \\
      & 10323 &  0.69 &  0.79 &  0.94 &  1.15 &   2.06 \\
      & 42103 &  0.81 &  0.88 &  0.96 &  1.05 &   1.32 \\
lognormal, CV=2 & 2531  &  0.36 &  0.63 &  1.27 &   $\infty$ &    $\infty$ \\
      & 4843  &  0.44 &  0.69 &  0.97 &  2.42 &    $\infty$ \\
      & 10323 &  0.52 &  0.74 &  1.03 &  1.72 &  10.32 \\
      & 42103 &  0.66 &  0.83 &     1 &  1.28 &   2.11 \\
exponential, CV=1 & 2531  &  0.51 &  0.63 &  1.27 &  2.53 &    $\infty$ \\
      & 4843  &  0.54 &  0.81 &  0.97 &  1.61 &   2.42 \\
      & 10323 &  0.65 &  0.79 &  1.03 &  1.15 &   1.72 \\
      & 42103 &  0.77 &   0.9 &  0.98 &  1.08 &   1.24 \\
\bottomrule
\end{tabular}
\caption{Epistemic uncertainty table for invariant 1 m slip distribution
\label{nsv_ep_unc_table}}
  \end{table}

However, it is important to note that the differences between the results from
this experiment and the experiment in the manuscript are minor. Perhaps most
importantly, the relative differences between the recurrence distributions are
maintained here, and the number of earthquakes required for the measured slip
rates to stabilize are about the same.
