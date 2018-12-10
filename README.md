#The impact of earthquake cycle variability on neotectonic and paleoseismic
slip rate estimates

This repository contains the code and the manuscript for a recent paper 
entitled [*The impact of earthquake cycle variability on neotectonic and 
paleoseismic slip rate estimates*][se_man] by myself (Richard Styron), accepted 
at *Solid Earth*.

The script used in the main experiment in the paper is called 
'eq_cycle_slip_rates_plotlast.py', and calls functions in 'slip_rate_fns.py'.  
There are two very similar scripts that use different slip distributions that 
are used in the experiments described in the supplemental materials in the 
paper.

The scripts are called from Python (or IPython) with no arguments. The scripts 
use the standard Python 'data science' modules of Python in 2018:
- `Python`: v. 3.6.4 from Anaconda
- `IPython`: v. 6.2.1
- `numpy`: v. 1.14.0
- `scipy`: v. 1.0.0
- `pandas`: v. 0.22.0
- `matplotlib`: v. 2.1.2


The manuscript and products are copyright 2018, Richard Styron, and released 
under a [Creative Commons Attribution 4.0 
License](https://creativecommons.org/licenses/by/4.0/legalcode.txt).

The code is copyright 2018, Richard Styron, licensed under the [MIT 
License](https://opensource.org/licenses/MIT).

[se_man]: https://www.solid-earth-discuss.net/se-2018-40/se-2018-40.pdf
