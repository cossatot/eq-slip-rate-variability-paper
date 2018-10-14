 oskin

> [O1] This paper presents a useful thought experiment on the impact of 
> earthquake cycle variability on measured slip rates, and concludes that the 
> convergence on the expected value is a function of the coefficient of 
> variation. Overall this is a sensible conclusion. Underpinning this analysis 
> are four assumed variants of earthquake recurrence, and a function to express 
> the variability of slip per event. 

> [O2] I would like to see the effect of COV isolated from the slip per event 
> distribution (use 1m slip for every event). 

I performed this experiment; the figure with the slip rate results is shown
below for comparison with Figure 5 in the paper, and are included in a new
document in the supplemental material. The most relevant figure is also shown
here: 

![Figure \label{fig}](../figures/nsv_slip_rate_envelopes.pdf)

The differences between the results of this experiment (fixed per-event
displacement of 1 m) and of the numerical experiment performed in the manuscript
are basically that these results are less smooth, but the total variance at any
point in time (*x-axis*) is less. This is simply due to removing the
stochasticity from one of the two variables in the system. The relative
spread in the data and convergence rates are unchanged. This is to be expected
as the variability in the per-event displacement is the same for all recurrence
distributions, so even though it is a random variable in the simulations, it is
not an experimental variable.

What I find the most interesting about this experiment is that the fluctuations
in the estimated slip rates show very clearly the mean earthquake cycles once
the noise from the per-event displacements has been removed. It is clear that
these are kind of damped or averaged out after ~7 earthquake cycles.
Nonetheless, though this is a cool pattern to see, I don't think it adds
enough insight to be worth including in the manuscript. I have added the figure
and table that show the slip rate variation through time to a new supplemental
document, accompanied by a brief discussion.

> [O3] I would also like to a see a more quantitative comparison of COV and a 
> convergence on the mean to back up the assertion that COV of the distribution 
> is more important than the distribution itself.

This comment is addressed in the response to [O18] below.


> [O4] The paper would be improved by a more quantitative, empirical basis and 
> discussion of physical processes that may drive such recurrence behavior.

This paper is written to be a quick and clean demonstration of the effects of 
recurrence (and slip) variability on slip rate estimations. I want to keep the
work as simple and as digestible as possible, for a few reasons:

1. The intended audience for the paper is not only crustal deformation
   researchers, but others in the seismic hazard community as well--this
   includes engineers, geotechnical workers, analysts in the insurance industry,
   etc. In my experience as a member of this community, many others are
   only interested in these sorts of phenomena to the degree that they are
   consequential and actionable; their intellectual interests are often oriented
   towards their fields of expertise (structural engineering, ground motions,
   human and economic exposure, etc.). I want this paper to be a straightforward
   reference for how to evaluate slip rate data in light of aleatory variability
   that is not tied down in jargon or linked to specific geological or
   geophysical models or ideas that may not stand the test of time. Because of
   how variable and poorly-understood earthquake recurrence and fault
   interaction phenomena are, an in-depth discussion without resolution may well
   be off-putting to much of the audience that I would like to read this paper.

2. I don't believe that the state of the science is such that several paragraphs
   to a page of discussion can summarize our (minimal) understanding of these
   issues with any degree of satisfaction. Understanding earthquake recurrence
   and fault interaction is a fascinating research topic, and it deserves either
   a very full treatment (a review paper, lots of data analysis and modeling) or
   simply a few references before the paper moves on. We are not at the stage
   where we have a lot of answers, so it is very easy to get bogged down.

> [O5] There is a literature of ideas to draw upon, such as post-seismic fault 
> reloading (Kenner and Simons, 2005), earthquake super cycles (Sieh et al., 
> 2008; Weldon et al., 2004), isolated versus fault-network behavior (Berryman et 
> al., 2012). Some of these ideas are discussed briefly but need more 
> explanation.

I disagree. It is clear that this stochasticity exists in nature, but I don't
think that we understand why. The modeling by Brad Hager's and Mark Simons'
research groups 


> [O6a] Likewise one could examine actual earthquake slip distributions (not 
> landform offsets of historic events, which convolve landscape processes with 
> tectonic slip) to develop an empirical basis for the slip function.

Such a distribution is given by Biasi and Weldon (2009), following work done by 
Hemphill-Haley and Weldon (1999). It is a bit different than the lognormal 
distribution used in that the probability of relatively low values (zero or 
near-zero) is higher than in a lognormal distribution. The sample COV of this 
distribution is 0.67, slightly lower than the lognormal slip distribution used
in the paper, with a COV of 0.75.

As an experiment, I have re-done the simulation sampling from this 
distribution; the data are given as 1313 discrete points from earthquakes 
worldwide, normalized to the mean slip per event. I have sampled randomly from 
this finite set, with replacement, instead of interpolating the set into a 
continuous distribution and sampling from that. The results are in the new
supplemental materials (Figures S1 and S2, Table S1, and some discussion).

The results are nearly indistinguishable.


> [O6b] Some of the scatter in slip distributions is likely due to 
> underreported measurement uncertainty (Gold et al., 2013), and thus the 
> cancellation of this error over multiple earthquakes should let cumulative 
> slip converge more quickly than may be predicted from the author’s model.

Either I don't understand this comment (which is quite possible) or it is a bit 
misapplied. The only reading of this comment under which one expects faster 
convergence than I have modeled is if the reviewer believes that measurement 
error is some component of the total variability represented. But that is not 
the case in the modeling; these distributions are taken to represent only 
aleatory variability and the study is performed with assumptions of zero 
measurement error.


> [O7] Page 1, line 4. The open interval problem is well known and attempts to 
> quantify it do exist on case-by-case basis.

Yes, and some of these cases are cited in the introduction. However, the 
open-interval problem simply deals with the uncertainty in a single recurrence 
interval (the present one), and not the variability that is present throughout 
all of the closed earthquake intervals that have contributed to the measured 
offset; this larger issue is the topic of the manuscript.

*No changes.*

> [O8] Page 1, line 13. It seems odd to characterize uncertainty due to a 
> random distribution as epistemic. Isn’t this unreported aleatory uncertainty?

No, it's not unreported aleatory uncertainty. It is aleatory variability 
*transformed* into epistemic uncertainty by a condition of ignorance of the 
underlying distribution.

The issue is that, with a single measurement (such as a slip rate measurement) 
one doesn't know what the mean slip rate is, or how much this rate varies 
through time. 


A quick dice analogy:

If I have a fair, six-sided die, and I 


> [O9] Page 1, line 20: Why is marker in quotes?

> [O10] Page 2, line 5. afterslip and creep also contribute.

> [O11] Page 2, line 10-11. Awkward sentence. Break into two.

> [O12] Page 2, line 13 and other citations:  persistent use of ‘e.g’ after 
> citing only one or two articles is poor form and makes this reader think that 
> the author has not adequately explored the literature.

The use of 'e.g.' denotes that the given citations are not authoritative in the 
sense that the cited works are where the concepts given are first introduced or 
best developed, as this isn't true. The cited works are generally just modern, 
high quality studies that exemplify the topic at hand.

I don't really care what readers may think of the depth of my scholarship.

> [O13a] Page 3,  line 11.  This is not the correct definition of an 
> exponential / poisson distribution.  There is no prescribed number of events, 
> only a prescribed time-independent probability. 

The time-independent probability is the mean rate of events. The mean rate of 
events is the mean number of events that occur within some time interval.

Obviously with finite sample sets (of time, or of events) there will be some 
variation--otherwise I wouldn't have written the paper.

> [O13b] It is also worth noting that this is physically unrealistic at short 
> time intervals because it violates elastic rebound.

Elastic rebound is a theory, not a law. It is unfortunately a step removed from 
modern understanding of the mechanics of earthquakes, which are based around 
stress, not strain. These map to each other nicely in the case of elastic and 
Newtonian viscoelastic rheologies, but not as nicely with rate-dependent 
rheologies, which are often considered the best characterization of the lower 
crust and upper mantle (e.g., Hetland and Hager, xxx). It's also hard to put 
strain in a framework with friction, for example. 'Physically realistic' 
modeling has to make a lot of assumptions and use heavy duty equipment (finite 
elements, for example) to incorporate strain.

There is also a separate issue with elastic rebound theory: It's not very easy 
to tell whether all the accumulated shear strain was released in an earthquake 
or not. What kind of measurements would tell us this?

I strongly suspect that we are fundamentally underestimating the frequency of 
very short recurrence intervals on faults. They're close to invisible to 
paleoseismology, which is our main source of data for recurrence interval 
statistics, because very closely-spaced events may not each produce 
differentiable colluvial wedges or other signs of surface deformation. This 
could plausibly result in a strong sample bias in the statistics. Nonetheless, 
we have clear observations of short recurrence intervals in the past few years. 
For example, some parts of the Monte Vettore fault slipped about 20 cm in the 
Amatrice earthquake and then ~2 m in the Norcia earthquake a few months later 
(Gruppo di Lavoro INGV sul Terremoto di Amatrice-Visso. (2016, October 29). 
PRIMO RAPPORTO DI SINTESI SUL TERREMOTO DI VISSO ML 5.9 DEL 26 OTTOBRE 2016 
(ITALIA CENTRALE). Zenodo. http://doi.org/10.5281/zenodo.163818).  


From a fault mechanics perspective, some researchers (for example Mark Zoback 
and his students, primarily Townend, as well as myself) believe that the shear 
stress on a fault required to initiate failure is much greater than the stress 
drop during the event, i.e. shear stress does not go to zero. Failure is 
decently described by Mohr-Coulomb models, and at, say, 10 km depth, the 
confining pressure is almost 300 MPa. With reasonable static friction 
coefficients (say 0.3 to 0.6) and typical pore fluid pressure, 



> [O14] Page 3, line 24. It would be useful to briefly discuss how shape and 
> scale affect distributions generally. Shape governs the how tailed and is 
> dimensionless; scale determines the spread of the distribution and is 
> dimensioned (in years for this case).

Isn't this implicit in the


> [O15] Page 4, line 6.  Pareto distribution is another, simpler distribution 
> needing only shape and scale to describe COV > 1

The Pareto distribution isn't used to describe earthquake recurrence, as far as 
I know. I believe that its only use in seismology is the tapered Pareto 
distribution for magnitude-frequency distributions by Yan Kagan (and perhaps 
others); this is similar in concept but not close enough to use here.

(Moderately) interestingly, I gather that Pareto/power-law distributions often 
form in environments characterized by exponential growth and aggregation 
(population, money, etc.), while the somewhat similar and discussed 
hyperexponential distribution can result from the sum of possibly-independent 
random Poisson processes, though both give rise to final distributions with 
similar tails.

*No changes.*

> [O16] Page 4, line 15. Akciz et al (2012) revised Grant and Sieh (1994) and 
> found much more periodic behavior.

The referenced sentence simply states "However, one can find examples of 
studies indicating the opposite conclusions", to reinforce the paragraph's 
opening statement that "No consensus exists among earthquake scientists as to 
the most appropriate recurrence interval distribution."  That a study revised a 
previous study and found different results further reinforces this point, but I 
don't think there is additional benefit to citing it.

*No changes.*

> [O17] Page 4, line 28.  The author should consider non-dimensionalizing the 
> results of this study to facilitate more general use of its results. Instead 
> of mean slip of 1m, one would refer to non-dimensional slip of 1 and multiply 
> by average slip per event to scale the results.  This is effectively what the 
> author describes already, though without formal non-dimensionalization.

I considered formal nondimensionalization but decided against it.

In the end, I decided to present the results dimensionally because most 
geologists think dimensionally (myself included). 

Dimensional thinking allows for different heuristics to be used when analyzing 
methods and results, than non-dimensional thinking. Basically, 
non-dimensionalizing parameters forces parameters to only be defined in terms 
of their relationship with each other, and to only exist within the context of 
this specific problem. 

If I say a fault has a mean slip of 1, and a mean recurrence interval of 1, and 
a mean slip rate of 1, it's hard to picture such a fault. Are those reasonable 
values for these parameters, individually? Can't say. Furthermore, the slip 
rate isn't even 1, it's 1/1, because it's a rate and the non-dimensional units 
are still not arithmetically compatible units--multiplication and division are 
possible (kind of, but not reducible) but addition and subtraction are not at 
all defined. (Please forgive me for not knowing enough measure theory to 
rigorously state this...).

Non-dimensionalization in many geological problems reduces the clarity of the 
analysis or solution because it strips it of context. At the same time it can 
facilitate the manipulation of the equations within the study, or during 
programming, etc. Physicists like it because it makes their work easier, I 
would say, and they're all pretty used to it.

Compare this to the dimensionalized problem in the paper. Can you imagine a 
fault with a mean per-event slip of 1 m, a recurrence interval of 1000 years, 
and a slip rate of 1 mm/yr?  I can, and I can place it--it's a small but pretty 
active intraplate fault, or a splay in a plate boundary. It's the kind of fault 
one might actually go and trench.

However, all the numbers are 1 (or 1000) so that it is easy to scale to other 
faults by multiplying by non-dimensional scaling factors (i.e., for a Mongolian 
fault with a slip rate of 3 mm/yr and a per-event slip of 10 m, you scale the 
slip by 10 and the slip rate by 3). It's not accidental.

*No changes.*

> [O18] Page 5, line 15. The statement ‘appears to be related to COV’ is 
> disappointing. Given that this paper is entirely simulation, the author 
> should be able to make a quantitative comparison of slip-rate variance to 
> COV.




> [O19] Page 5, line 29. This problem has been studied (Weldon et al., 2004; 
> Sieh et al., 2008). The Sumatran subduction zone work is particularly 
> relevant and completely overlooked here.

The work by Weldon et al. (2004) is referenced on Page 6, Line 3. Neither of
these papers deal with the topic of autocorrelated recurrence intervals in any
quantitative or otherwise explicit manner, and I don't read anything that I can
interpret as a qualitative discussion either. One can read both papers and not
get a sense of whether a short recurrence interval implies the next recurrence
interval will be short or long, much less any quantification. Both papers deal
with the concept of 'earthquake supercycles' or groups of earthquakes that are
relatively tightly-spaced and separated from other groups by long recurrence
intervals. This may share a conceptual link, but from a technical perspective
this likely has more to do with periodicity than autocorrelation, and these are
mathematically separate such that a periodic sequence may have positive or
negative autocorrelation. Goh and Barabasi (2008, Europhysics Letters) is a
useful discussion on the topic of autocorrelation vs. periodicity in regards to
quantifying clustering behavior (though one may safely ignore the references to
seismicity in that paper).

[Note: I've analyzed Weldon's data (from K. Scharer's refined OxCal earthquake 
dates) and found that earthquake recurrence interval duration at the Wrightwood 
and Pallett Creek sites has a negative autocorrelation, i.e. a short recurrence 
interval is likely to be followed by a long recurrence interval, and vice 
versa. This is quite unlike the autocorrelation in the Puget Lowlands of
Washington State, which is more like a network of generally similar faults
instead of an isolated or dominant plate boundary fault like the SAF or the
Alpine Fault as referenced in another comment on Kelvin Berryman's work, where a
long recurrence interval will more likely be followed by another long recurrence
interval. I don't know what this means, or whether it's all noise, but it's
intriguing to me and I put this bit in the paper in hopes of catching the
attention of others who may be looking for a project.]


> [O20] Page 6, line 1. Zero friction at rupture arrest is very unrealistic, 
> and not a prerequisite for characteristic behavior.

It is not a necessary condition but it is a sufficient one, when coupled with 
fairly regular reloading and failure conditions. I personally think it's 
unlikely as well (see Styron and Hetland 2015 for example), but zero (or very
near zero) friction is part and parcel with complete stress drop in major
earthquakes, which is supported by many studies [REFS]. Furthermore, there are a
host of laboratory experiments which suggest that friction during slip decreases
to very low values [MORE REFS].
