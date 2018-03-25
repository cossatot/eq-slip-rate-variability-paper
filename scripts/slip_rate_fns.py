import numpy as np
import scipy.stats as ss

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


def sample_eq_displacements(mean, std, n_eqs):
    return lognormal(mean, std, n_eqs)


# This function makes a cumulative slip history given a recurrence mean,
# standard deviation, recurrence interval distribution, and simulation
# length.
def make_cum_slip(rec_mean, rec_std, distribution, yrs=10000,
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


def moving_average_rate(cum_disp, window, scale='mm/yr'):
    rates = [(cum_disp[i+window] - cum_disp[i]) / window
             for i in range(len(cum_disp) - window)]
    
    rates = np.array(rates)
    
    if scale == 'mm/yr':
        rates *= 1000
    elif scale == 'm/yr':
        pass
    
    return rates



