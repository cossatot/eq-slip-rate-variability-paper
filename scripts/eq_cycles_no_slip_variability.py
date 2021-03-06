#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['font.sans-serif'] = 'Arial'

#import scipy.stats as ss

from slip_rate_fns import *


save_figs = True

'''Calculations'''

np.random.seed(420)

n_eqs = 15

print('Making example distributions...')
# make some example distributions for plotting
lgn_1000_500 = lognormal(1000, 500, return_pdf=True)
lgn_1000_1000 = lognormal(1000, 1000, return_pdf=True)
lgn_1000_2000 = lognormal(1000, 2000, return_pdf=True)
exp_1000 = exponential(1000, 1000, return_pdf=True)
print('Done.')

print('Making slip histories...')
# make slip histories
sim_years = int(2e6)

# Now the cumulative displacement histories are made.
# We make one 2-million-year history for each distribution.
cum_disp_logn_1000_500 = make_cum_slip(1000, 500, lognormal,
                                       displacement_mean=1.,
                                       displacement_std=0.,
                                       yrs=sim_years)
cum_disp_logn_1000_1000 = make_cum_slip(1000, 1000, lognormal,
                                       displacement_mean=1.,
                                       displacement_std=0.,
                                        yrs=sim_years)
cum_disp_logn_1000_2000 = make_cum_slip(1000, 2000, lognormal,
                                       displacement_mean=1.,
                                       displacement_std=0.,
                                        yrs=sim_years)
cum_disp_exp_1000 = make_cum_slip(1000, 1000, exponential,
                                       displacement_mean=1.,
                                       displacement_std=0.,
                                  yrs=sim_years)
print('Done.')

print('Calculating slip rate history windows...')
# calculate the windows.
windows = np.logspace(np.log10(500),
                      np.log10(100000), 50, dtype='int')

# calculate the slip rates for each series.
logn_1000_500_rates = {w : moving_average_rate(cum_disp_logn_1000_500, w)
                       for w in windows}

logn_1000_1000_rates = {w : moving_average_rate(cum_disp_logn_1000_1000, w)
                       for w in windows}

logn_1000_2000_rates = {w : moving_average_rate(cum_disp_logn_1000_2000, w)
                       for w in windows}

exp_1000_rates = {w : moving_average_rate(cum_disp_exp_1000, w)
                  for w in windows}
print('Done.')


print('Calculating statistics for each window...')
# calcualate the quartiles for each series.
pctiles = [1, 25, 50, 75, 99]

logn_1000_500_rate_quarts = {w: {p: ss.scoreatpercentile(
                                        logn_1000_500_rates[w], p)
                                 for p in pctiles}
                             for w in windows}

logn_1000_1000_rate_quarts = {w: {p: ss.scoreatpercentile(
                                        logn_1000_1000_rates[w], p)
                                 for p in pctiles}
                             for w in windows}

logn_1000_2000_rate_quarts = {w: {p: ss.scoreatpercentile(
                                        logn_1000_2000_rates[w], p)
                                 for p in pctiles}
                             for w in windows}

exp_1000_rate_quarts = {w: {p: ss.scoreatpercentile(
                                        exp_1000_rates[w], p)
                                 for p in pctiles}
                             for w in windows}


a_pctiles = [5, 25, 50, 75, 95]

def est_slip_adjust(rates, top_clip=None):
    adj = np.copy(rates)
    adj[rates > 0.] = 1 / rates[rates > 0.]
    adj[rates == 0.] = np.inf
    
    if top_clip is not None:
        adj[adj > top_clip] = top_clip
    
    return adj

tc = 5.

logn_1000_500_rq_adj = {w: {p: ss.scoreatpercentile(
                                    est_slip_adjust(logn_1000_500_rates[w],
                                                    top_clip=tc), p)
                                 for p in a_pctiles}
                             for w in windows}

logn_1000_1000_rq_adj = {w: {p: ss.scoreatpercentile(
                                    est_slip_adjust(logn_1000_1000_rates[w],
                                                    top_clip=tc), p)
                                 for p in a_pctiles}
                             for w in windows}

logn_1000_2000_rq_adj = {w: {p: ss.scoreatpercentile(
                                    est_slip_adjust(logn_1000_2000_rates[w],
                                                    top_clip=tc), p)
                                 for p in a_pctiles}
                             for w in windows}

exp_1000_rq_adj = {w: {p: ss.scoreatpercentile(
                                    est_slip_adjust(exp_1000_rates[w],
                                                    top_clip=tc), p)
                                 for p in a_pctiles}
                             for w in windows}


print('Done.')

print('Doing some convenience calculations for plotting...')
# make arrays from quartiles for faster plotting
logn_1000_500_rq_arrays = {p: np.array([logn_1000_500_rate_quarts[w][p]
                                        for w in windows])
                           for p in pctiles}

logn_1000_1000_rq_arrays = {p: np.array([logn_1000_1000_rate_quarts[w][p]
                                        for w in windows])
                           for p in pctiles}

logn_1000_2000_rq_arrays = {p: np.array([logn_1000_2000_rate_quarts[w][p]
                                        for w in windows])
                           for p in pctiles}

exp_1000_rq_arrays = {p: np.array([exp_1000_rate_quarts[w][p]
                                   for w in windows])
                      for p in pctiles}


logn_1000_500_adj_arrays = {p: np.array([logn_1000_500_rq_adj[w][p]
                                        for w in windows])
                           for p in a_pctiles}

logn_1000_1000_adj_arrays = {p: np.array([logn_1000_1000_rq_adj[w][p]
                                        for w in windows])
                           for p in a_pctiles}

logn_1000_2000_adj_arrays = {p: np.array([logn_1000_2000_rq_adj[w][p]
                                        for w in windows])
                           for p in a_pctiles}

exp_1000_adj_arrays = {p: np.array([exp_1000_rq_adj[w][p]
                                   for w in windows])
                      for p in a_pctiles}

# normalize results by mean EQ cycle length
eq_cycles = windows / 1000
print('Done.')



print('Plotting results...')

'''plotting'''


SMALL_SIZE = 6
MEDIUM_SIZE = 8
BIGGER_SIZE = 10

one_col = 8.3 / 2.54 # cm to in
two_col = 12. / 2.54 # cm to in

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)    # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

# Plot recurrence distributions
t = np.linspace(0,8000, 500)

f1, ax1 = plt.subplots(1,1, figsize=(one_col, one_col))
#ax1.set_title('Earthquake recurrence distributions')
ax1.plot(t, lgn_1000_500.pdf(t), label='logn, μ=1000, σ=500', lw=0.5)
ax1.plot(t, lgn_1000_1000.pdf(t), label='logn, μ=1000, σ=1000', lw=0.5)
ax1.plot(t, lgn_1000_2000.pdf(t), label='logn, μ=1000, σ=2000', lw=0.5)
ax1.plot(t, exp_1000.pdf(t), label='exp, μ=σ=1000', lw=0.5)

ax1.legend(loc='best')

ax1.set_xlabel('Recurrence Interval (yr)')
ax1.set_ylabel('Probability')


# Plot slip distribution
f2, ax2 = plt.subplots(1,1, figsize=(one_col, one_col))
#ax2.set_title('Earthquake slip distribution')
ax2.plot(np.linspace(0, 5, num=500),
         lognormal(1, 0.000001, return_pdf=True).pdf(np.linspace(0,5,num=500)),
         'k')

ax2.set_xlabel('Slip (m)')
ax2.set_ylabel('Probability')


# Plot displacement histories
f3, (ax30, ax31) = plt.subplots(2,1, figsize=(two_col, two_col * 0.8))

# first 100,000 years
ax30.plot([0,1e5],[0,100],'k', lw=0.5)

ax30.plot(cum_disp_logn_1000_500[:int(1e5)], 
          lw=0.75, label='logn, μ=1000, σ=500 (periodic)')
ax30.plot(cum_disp_logn_1000_1000[:int(1e5)], 
          lw=0.74, label='logn, μ=1000, σ=1000 (unclustered)')
ax30.plot(cum_disp_logn_1000_2000[:int(1e5)], 
          lw=0.75, label='logn, μ=1000, σ=2000 (clustered)')
ax30.plot(cum_disp_exp_1000[:int(1e5)], 
          lw=0.75, label='exp, μ=1000 (unclustered)')

ax30.legend(loc='upper left')

#ax30.set_xlabel('years')
ax30.set_ylabel('cumulative displacement (m)')

# longer term
ax31.plot([0,1e6],[0,1000],'k', lw=0.5)

ax31.plot(cum_disp_logn_1000_500[:int(2e6)], 
          lw=0.75, label='logn, μ=1000, σ=500 (periodic)')
ax31.plot(cum_disp_logn_1000_1000[:int(2e6)], 
          lw=0.75, label='logn, μ=1000, σ=1000 (unclustered)')
ax31.plot(cum_disp_logn_1000_2000[:int(2e6)], 
          lw=0.75, label='logn, μ=1000, σ=2000 (clustered)')
ax31.plot(cum_disp_exp_1000[:int(2e6)], 
          lw=0.75, label='exp, μ=1000 (unclustered)')

ax31.legend(loc='upper left')

ax31.set_xlabel('years')
ax31.set_ylabel('cumulative displacement (m)')


# Plot event spacing example
f4, ax4 = plt.subplots(1,1, figsize=(one_col, one_col))

ax4.scatter(lognormal(1000, 500, n_eqs).cumsum(),
         np.ones(n_eqs) * 1.5, marker='|',
         c='C0', s=10, label='logn, μ=1000, σ=500 (periodic)')

ax4.scatter(lognormal(1000, 1000, n_eqs).cumsum(),
         np.ones(n_eqs) * 1, marker='|',
         c='C1', s=10, label='logn, μ=1000, σ=1000 (unclustered)')

ax4.scatter(lognormal(1000, 2000, n_eqs).cumsum(),
         np.ones(n_eqs) * 0.5, marker='|',
         c='C2', s=10,  label='logn, μ=1000, σ=2000 (clustered)')

ax4.scatter(exponential(1000, 1000, n_eqs).cumsum(),
         np.ones(n_eqs) * 0, marker='|',
         c='C3', s=10, label='exp, μ=σ=1000 (unclustered)')

ax4.legend(loc='upper center')

ax4.set_ylim([-0.1,2.5])
ax4.set_xlabel('years')
ax4.set_yticks([])


# Plot slip rate envelopes
f5, (ax50, ax51, ax52, ax53) = plt.subplots(4, 1, figsize=(two_col, two_col),
                                            sharex=True, sharey=True)

ax50.axhline(1, color='k', lw=0.5)

ax50.fill_between(eq_cycles, logn_1000_500_rq_arrays[1],
                            logn_1000_500_rq_arrays[99],
                 alpha=0.15, color='C0',
                 label='1-99th pctile',
                  lw=0)
ax50.fill_between(eq_cycles, logn_1000_500_rq_arrays[25],
                            logn_1000_500_rq_arrays[75],
                 alpha=0.5, color='C0',
                 label='25-75th pctile',
                  lw=0)


ax50.plot(eq_cycles, logn_1000_500_rq_arrays[50], 'C0-', label='median', 
          lw=0.75)

#ax50.set_ylabel('Estimated slip rate (mm/yr)')
ax50.legend(loc='upper right')
#ax50.set_title('Lognormal, mean=1000yr, std=500yr')

ax51.axhline(1, color='k', lw=0.5)

ax51.fill_between(eq_cycles, logn_1000_1000_rq_arrays[1],
                            logn_1000_1000_rq_arrays[99],
                 alpha=0.15, color='C1',
                 label='1-99th pctile',
                  lw=0)
ax51.fill_between(eq_cycles, logn_1000_1000_rq_arrays[25],
                            logn_1000_1000_rq_arrays[75],
                 alpha=0.5, color='C1',
                 label='25-75th pctile',
                  lw=0)


ax51.plot(eq_cycles, logn_1000_1000_rq_arrays[50], 'C1-', label='median', 
          lw=0.75)


ax52.axhline(1, color='k', lw=0.5)

ax52.fill_between(eq_cycles, logn_1000_2000_rq_arrays[1],
                            logn_1000_2000_rq_arrays[99],
                 alpha=0.15, color='C2',
                 label='1-99th pctile',
                  lw=0)
ax52.fill_between(eq_cycles, logn_1000_2000_rq_arrays[25],
                            logn_1000_2000_rq_arrays[75],
                 alpha=0.5, color='C2',
                 label='25-75th pctile',
                  lw=0)


ax52.plot(eq_cycles, logn_1000_2000_rq_arrays[50], 'C2-', label='median', 
          lw=0.75)




ax53.axhline(1, color='k', lw=0.5)

ax53.fill_between(eq_cycles, exp_1000_rq_arrays[1],
                            exp_1000_rq_arrays[99],
                 alpha=0.15, color='C3',
                 label='1-99th pctile',
                  lw=0)

ax53.fill_between(eq_cycles, exp_1000_rq_arrays[25],
                            exp_1000_rq_arrays[75],
                 alpha=0.5, color='C3',
                 label='25-75th pctile',
                  lw=0)


ax53.plot(eq_cycles, exp_1000_rq_arrays[50], 'C3-', label='median',
          lw=0.75)

#ax51.legend(loc='upper right')
#ax51.set_title('Exponential, mean=1000yr, std=1000yr')

ax52.set_ylabel('Estimated slip rate (mm/yr)')
ax53.set_xlabel('Mean number of earthquakes (or thousand years of window length)')
#ax50.set_xscale('log')
#plt.xlim([0, 20])
ax50.set_ylim([0,4])
ax50.set_xlim([0,60])



def plot_rate_quartiles(quarts=None, median=True, xlim=None, ylim=None,
                        log_x=False, log_y=False, fill_between=False,
                        mean=1, ax=None, lw=1.):

    if mean is not False:
        ax.axhline(mean, color='k', lw=0.5)
    

    ax.plot(eq_cycles, logn_1000_500_rq_arrays[quarts[0]], color='C0', lw=lw)
    ax.plot(eq_cycles, logn_1000_500_rq_arrays[quarts[1]], color='C0', lw=lw
            #label='logn, μ=1000, σ=500'
            )

    ax.plot(eq_cycles, logn_1000_1000_rq_arrays[quarts[0]], color='C1', lw=lw)
    ax.plot(eq_cycles, logn_1000_1000_rq_arrays[quarts[1]], color='C1', lw=lw
            #label='logn, μ=1000, σ=1000',
            )

    ax.plot(eq_cycles, logn_1000_2000_rq_arrays[quarts[0]], color='C2', lw=lw)
    ax.plot(eq_cycles, logn_1000_2000_rq_arrays[quarts[1]], color='C2', lw=lw
            #label='logn, μ=1000, σ=2000',
            )

    ax.plot(eq_cycles, exp_1000_rq_arrays[quarts[0]], color='C3', lw=lw)
    ax.plot(eq_cycles, exp_1000_rq_arrays[quarts[1]], color='C3', lw=lw
            #label='exp, μ=σ=1000',
            )
    
    if median is True:
        ax.plot(eq_cycles, logn_1000_500_rq_arrays[50], 'C0--', lw=lw)
        ax.plot(eq_cycles, logn_1000_1000_rq_arrays[50], 'C1--', lw=lw)
        ax.plot(eq_cycles, logn_1000_2000_rq_arrays[50], 'C2--', lw=lw)
        ax.plot(eq_cycles, exp_1000_rq_arrays[50], 'C3--', lw=lw)
    
    if xlim is not None:
        ax.set_xlim(xlim)
    
    if ylim is not None:
        ax.set_ylim(ylim)
        
    if log_x is True:
        ax.set_xscale('log')
    
    if log_y is True:
        ax.set_yscale('log')
        
    return ax

#f6, ((ax61, ax62), (ax63, ax64)) = plt.subplots(2,2, figsize=(two_col, two_col))
#
#ax61 = plot_rate_quartiles(quarts=(1,99), ax=ax61, median=False, 
#                          ylim=(0,4), lw=0.75)
#
##ax61.legend(loc='upper right')
##ax61.set_title('Estimated slip rates,\n1-99th percentiles')
#ax61.set_ylabel('Estimated slip rates (mm/yr)')
##ax61.set_xlabel('N Earthquakes (or thousand years)')
#
#
#ax62 = plot_rate_quartiles(quarts=(25,75), ax=ax62, median=True, 
#                          ylim=(0,2), lw=0.75)
#
##ax62.legend(loc='upper right')
##ax62.set_title('Estimated slip rates,\n25-75th percentiles and median')
##ax62.set_ylabel('Estimated slip rates (mm/yr)')
##ax62.set_xlabel('N Earthquakes (or thousand years)')
#
#
#ax63 = plot_rate_quartiles(quarts=(1,99), ax=ax63, median=False, 
#                          ylim=(0,4), xlim=(0,30), lw=0.75)
#
##ax63.legend(loc='upper right')
#ax63.set_ylabel('Estimated slip rates (mm/yr)')
#ax63.set_xlabel('N Earthquakes (or thousand years)')
#
#
#ax64 = plot_rate_quartiles(quarts=(25,75), ax=ax64, median=True, 
#                          ylim=(0.5,1.5), xlim=(0,30), lw=0.75)
#
##ax64.legend(loc='upper right')
##ax64.set_ylabel('Estimated slip rates (mm/yr)')
#ax64.set_xlabel('N Earthquakes (or thousand years)')





f7, (ax70, ax71, ax72, ax73) = plt.subplots(4, 1, figsize=(two_col, two_col),
                                            sharex=True, sharey=True)

ax70.axhline(1, color='k', lw=0.5)

ax70.fill_between(eq_cycles, logn_1000_500_adj_arrays[5],
                             logn_1000_500_adj_arrays[95],
                  alpha=0.15, color='C0',
                 label='5-95th pctile',
                 lw=0)

ax70.fill_between(eq_cycles, logn_1000_500_adj_arrays[25],
                             logn_1000_500_adj_arrays[75],
                  alpha=0.5, color='C0',
                 label='25-75th pctile',
                 lw=0)

ax70.plot(eq_cycles, logn_1000_500_adj_arrays[50], 'C0-', lw=0.75, 
          label='median')


ax71.axhline(1, color='k', lw=0.5)
ax71.fill_between(eq_cycles, logn_1000_1000_adj_arrays[5],
                             logn_1000_1000_adj_arrays[95],
                  alpha=0.15, color='C1',
                 lw=0)

ax71.fill_between(eq_cycles, logn_1000_1000_adj_arrays[25],
                             logn_1000_1000_adj_arrays[75],
                  alpha=0.5, color='C1',
                 lw=0)

ax71.plot(eq_cycles, logn_1000_1000_adj_arrays[50], 'C1-', lw=0.75)


ax72.axhline(1, color='k', lw=0.5)
ax72.fill_between(eq_cycles, logn_1000_2000_adj_arrays[5],
                             logn_1000_2000_adj_arrays[95],
                  alpha=0.15, color='C2',
                 lw=0)

ax72.fill_between(eq_cycles, logn_1000_2000_adj_arrays[25],
                             logn_1000_2000_adj_arrays[75],
                  alpha=0.5, color='C2',
                 lw=0)

ax72.plot(eq_cycles, logn_1000_2000_adj_arrays[50], 'C2-', lw=0.75)


ax73.axhline(1, color='k', lw=0.5)
ax73.fill_between(eq_cycles, exp_1000_adj_arrays[5],
                             exp_1000_adj_arrays[95],
                  alpha=0.15, color='C3',
                 lw=0)

ax73.fill_between(eq_cycles, exp_1000_adj_arrays[25],
                             exp_1000_adj_arrays[75],
                  alpha=0.5, color='C3',
                 lw=0)

ax73.plot(eq_cycles, exp_1000_adj_arrays[50], 'C3-', lw=0.75)


ax70.legend(loc='upper right')

ax72.set_ylabel('Epistemic uncertainty in rate measurement')
ax73.set_xlabel('Mean number of earthquakes (or thousand years)')

plt.xlim([0,40])
plt.ylim([0,5])



print('Done.')


print('Re-calculating values for epistemic uncertainty table...')
tc = None

a_windows = [2531, 4843, 10323, 42103]

logn_1000_500_rq_adj = {w: {p: ss.scoreatpercentile(
                                    est_slip_adjust(logn_1000_500_rates[w],
                                                    top_clip=tc), p)
                                 for p in a_pctiles}
                             for w in a_windows}

logn_1000_1000_rq_adj = {w: {p: ss.scoreatpercentile(
                                    est_slip_adjust(logn_1000_1000_rates[w],
                                                    top_clip=tc), p)
                                 for p in a_pctiles}
                             for w in a_windows}

logn_1000_2000_rq_adj = {w: {p: ss.scoreatpercentile(
                                    est_slip_adjust(logn_1000_2000_rates[w],
                                                    top_clip=tc), p)
                                 for p in a_pctiles}
                             for w in a_windows}

exp_1000_rq_adj = {w: {p: ss.scoreatpercentile(
                                    est_slip_adjust(exp_1000_rates[w],
                                                    top_clip=tc), p)
                                 for p in a_pctiles}
                             for w in a_windows}

logn_1000_500_adj_arrays = {p: np.array([logn_1000_500_rq_adj[w][p]
                                        for w in a_windows])
                           for p in a_pctiles}

logn_1000_1000_adj_arrays = {p: np.array([logn_1000_1000_rq_adj[w][p]
                                        for w in a_windows])
                           for p in a_pctiles}

logn_1000_2000_adj_arrays = {p: np.array([logn_1000_2000_rq_adj[w][p]
                                        for w in a_windows])
                           for p in a_pctiles}

exp_1000_adj_arrays = {p: np.array([exp_1000_rq_adj[w][p]
                                   for w in a_windows])
                      for p in a_pctiles}

print('done.')
print('making table...')
def make_perc_df(name, rates, winds=[2500, 5000,10000,40000], 
                 pctiles=[5,25,50,75,95]):
    ts = [windows[np.argmin(np.abs(windows-w))]
          for w in winds]
    cols = ['dist','t'] + pctiles
    df = pd.DataFrame(columns=cols, index=ts)
    df['dist'] = name
    df['t'] = ts
    
    for t in ts:
        for p in pctiles:
            df.loc[t, p] = np.round(rates[t][p], decimals=2)
    df = df.set_index(['dist', 't'])
    
    return df

print(
pd.concat((make_perc_df('logn_0.5', logn_1000_500_rq_adj),
           make_perc_df('logn_1', logn_1000_1000_rq_adj),
           make_perc_df('logn_2', logn_1000_2000_rq_adj),
           make_perc_df('exp_1', exp_1000_rq_adj))).to_latex()
)


if save_figs:
    print('Saving figures...')
    f1.savefig('../manuscript/figures/nsv_recurrence_dists.pdf', bbox_inches="tight")
    f2.savefig('../manuscript/figures/nsv_slip_dist.pdf', bbox_inches="tight")
    f3.savefig('../manuscript/figures/nsv_disp_histories.pdf', bbox_inches="tight")
    f4.savefig('../manuscript/figures/nsv_event_spacing.pdf', bbox_inches="tight")
    f5.savefig('../manuscript/figures/nsv_slip_rate_envelopes.pdf', bbox_inches="tight")
    #f6.savefig('../manuscript/figures/slip_rate_estimates.pdf', bbox_inches="tight")
    f7.savefig('../manuscript/figures/nsv_epist_unc.pdf', bbox_inches="tight")

plt.show()
