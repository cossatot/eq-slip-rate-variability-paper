import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

np.random.seed(420)

# sampling functions
def lognormal_scale(arith_mean, arith_var):
    return np.log(arith_mean / 
                  np.sqrt(1 + arith_var / arith_mean**2))

def lognormal_shape(arith_mean, arith_var):
    return np.sqrt(np.log(1 + arith_var / arith_mean**2))


def lognormal(mean, std, n_eqs=0, return_pdf=False):
    shape = lognormal_shape(mean, std**2)
    scale = lognormal_scale(mean, std**2)
    
    _lognorm = ss.lognorm(shape,
                          scale=np.exp(scale))
    
    if return_pdf == True:
        return _lognorm
    else:
        return _lognorm.rvs(n_eqs)


def exponential(mean, std, n_eqs=0, return_pdf=False):
    if mean != std:
        raise ValueError('mean and std must be equal!')
    
    _expon = ss.expon(scale = mean)
    
    if return_pdf == True:
        return _expon
    else:
        return _expon.rvs(n_eqs)


# make some example distributions for plotting
lgn_1000_500 = lognormal(1000, 500, return_pdf=True)
lgn_1000_1000 = lognormal(1000, 1000, return_pdf=True)
lgn_1000_2000 = lognormal(1000, 2000, return_pdf=True)
exp_1000 = exponential(1000, 1000, return_pdf=True)

# plot the distributions
t = np.linspace(0,8000, 500)

f1, ax1 = plt.subplots(1,1,
                       #figsize=(10,7)
                       )
#ax1.set_title('Earthquake recurrence distributions')
ax1.plot(t, lgn_1000_500.pdf(t), label='logn, μ=1000, σ=500')
ax1.plot(t, lgn_1000_1000.pdf(t), label='logn, μ=1000, σ=1000')
ax1.plot(t, lgn_1000_2000.pdf(t), label='logn, μ=1000, σ=2000')
ax1.plot(t, exp_1000.pdf(t), label='exp, μ=σ=1000')

ax1.legend(loc='best')

ax1.set_xlabel('recurrence interval (yr)')
ax1.set_ylabel('probability')

# slip distribution
f2, ax2 = plt.subplots(1,1)
#ax2.set_title('Earthquake slip distribution')
ax2.plot(np.linspace(0, 5, num=500),
         lognormal(1, 0.5, return_pdf=True).pdf(np.linspace(0,5,num=500)))

ax2.set_xlabel('Slip (m)')
ax2.set_ylabel('Probability')



# make slip histories
def sample_eq_displacements(mean, std, n_eqs):
    return lognormal(mean, std, n_eqs)

sim_years = int(2e6)


# This function makes a cumulative slip history given a recurrence mean,
# standard deviation, recurrence interval distribution, and simulation
# length.
def make_cum_slip(rec_mean, rec_std, distribution, yrs=sim_years,
                  displacement_mean=1, displacement_std=0.5):
    n_eqs = int(yrs / rec_mean) + 100
    
    eq_rec_times = np.int_(distribution(rec_mean, rec_std, n_eqs))
    eq_dates = np.cumsum(eq_rec_times)
    eq_dates = eq_dates[eq_dates < yrs]
    n_eqs = len(eq_dates)
    eq_rec_times = eq_rec_times[:n_eqs]
    
    eq_disps = sample_eq_displacements(displacement_mean,
                                       displacement_std,
                                       n_eqs)
    
    eq_slip = np.zeros(yrs)
    
    for i, yr in enumerate(eq_dates):
        eq_slip[yr] = eq_disps[i]
    
    cum_slip = np.cumsum(eq_slip)
    
    return cum_slip


# Now the cumulative displacement histories are made.
# We make one 2-million-year history for each distribution.
cum_disp_logn_1000_500 = make_cum_slip(1000, 500, lognormal)
cum_disp_logn_1000_1000 = make_cum_slip(1000, 1000, lognormal)
cum_disp_logn_1000_2000 = make_cum_slip(1000, 2000, lognormal)
cum_disp_exp_1000 = make_cum_slip(1000, 1000, exponential)


# This block of code plots the histories.
f3, (ax30, ax31) = plt.subplots(2,1, figsize=(12,12))

# first 100,000 years
ax30.plot([0,1e5],[0,100],'k', lw=0.5)

ax30.plot(cum_disp_logn_1000_500[:int(1e5)], label='logn, μ=1000, σ=500 (periodic)')
ax30.plot(cum_disp_logn_1000_1000[:int(1e5)], label='logn, μ=1000, σ=1000 (~random)')
ax30.plot(cum_disp_logn_1000_2000[:int(1e5)], label='logn, μ=1000, σ=2000 (clustered)')
ax30.plot(cum_disp_exp_1000[:int(1e5)], label='exp, μ=1000 (random)')

ax30.legend(loc='upper left')

ax30.set_xlabel('years')
ax30.set_ylabel('cumulative displacement (m)')

# longer term
ax31.plot([0,1e6],[0,1000],'k', lw=0.5)

ax31.plot(cum_disp_logn_1000_500[:int(2e6)], label='logn, μ=1000, σ=500 (periodic)')
ax31.plot(cum_disp_logn_1000_1000[:int(2e6)], label='logn, μ=1000, σ=1000 (~random)')
ax31.plot(cum_disp_logn_1000_2000[:int(2e6)], label='logn, μ=1000, σ=2000 (clustered)')
ax31.plot(cum_disp_exp_1000[:int(2e6)], label='exp, μ=1000 (random)')

ax31.legend(loc='upper left')

ax31.set_xlabel('years')
ax31.set_ylabel('cumulative displacement (m)')



# Look at event spacing
n_eqs = 15

f4, ax4 = plt.subplots(1,1)

ax4.scatter(lognormal(1000, 500, n_eqs).cumsum(),
         np.ones(n_eqs) * 3,
         c='C0', label='logn, μ=1000, σ=n_eqs00 (periodic)')

ax4.scatter(lognormal(1000, 1000, n_eqs).cumsum(),
         np.ones(n_eqs) * 2,
         c='C1', label='logn, μ=1000, σ=1000 (~random)')

ax4.scatter(lognormal(1000, 2000, n_eqs).cumsum(),
         np.ones(n_eqs) * 1,
         c='C2', label='logn, μ=1000, σ=n_eqs00 (clustered)')

ax4.scatter(exponential(1000, 1000, n_eqs).cumsum(),
         np.ones(n_eqs) * 0,
         c='C3', label='exp, μ=σ=1000 (random)')

ax4.legend(loc='upper center')

ax4.set_ylim([-0.1,4])
ax4.set_xlabel('years')




# Calculate slip rates

# This is the function to calculate the slip
# rates over the time series.
def moving_average_rate(cum_disp, window, scale='mm/yr'):
    rates = [(cum_disp[i+window] - cum_disp[i]) / window
             for i in range(len(cum_disp) - window)]
    
    rates = np.array(rates)
    
    if scale == 'mm/yr':
        rates *= 1000
    elif scale == 'm/yr':
        pass
    
    return rates

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

# normalize results by mean EQ cycle length
eq_cycles = windows / 1000

# plot these results
f5, (ax50, ax51) = plt.subplots(2, 1, figsize=(12,12),
                             sharex=True, sharey=True)

ax50.ax5hline(1, color='k', lw=0.5)

ax50.fill_between(eq_cycles, logn_1000_500_rq_arrays[1],
                            logn_1000_500_rq_arrays[99],
                 alpha=0.15, color='C0',
                 label='1-99th pctile')
ax50.fill_between(eq_cycles, logn_1000_500_rq_arrays[25],
                            logn_1000_500_rq_arrays[75],
                 alpha=0.5, color='C0',
                 label='25-75th pctile')


ax50.plot(eq_cycles, logn_1000_500_rq_arrays[50], 'C0-', label='median')

ax50.set_ylabel('Estimated slip rate (mm/yr)')
ax50.legend(loc='upper right')
ax50.set_title('Lognormal, mean=1000yr, std=500yr')



ax51.ax5hline(1, color='k', lw=0.5)

ax51.fill_between(eq_cycles, exp_1000_rq_arrays[1],
                            exp_1000_rq_arrays[99],
                 alpha=0.15, color='C3',
                 label='1-99th pctile')

ax51.fill_between(eq_cycles, exp_1000_rq_arrays[25],
                            exp_1000_rq_arrays[75],
                 alpha=0.5, color='C3',
                 label='25-75th pctile')


ax51.plot(eq_cycles, exp_1000_rq_arrays[50], 'C3-', label='median')

ax51.legend(loc='upper right')
ax51.set_title('Exponential, mean=1000yr, std=1000yr')

ax51.set_ylabel('Estimated slip rate (mm/yr)')
ax51.set_xlabel('Mean number of earthquakes (or thousand years of window length)')
#ax50.set_xscale('log')
#plt.xlim([0, 20])
ax50.set_ylim([0,5])

