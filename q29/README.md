Instructions:
A historical functional form of the initial mass function (IMF, the
number of stars formed as a function of stellar mass) is the Salpeter
IMF, which has dN/dM ~ M^(-2.35). Considering such a relation
with a minimum mass 0.5 solar masses and a maximum
mass 100 solar masses, write a routine that generates
random deviates to populate such a distribution. Use your routine to
general some plots of IMFs for several different sample sizes, which
you should plot in histogram form. Overlay the Salpeter function on
your plots.

11/12/15
Started... Not sure how to generate random numbers based on a specific
distribution (random.power only takes a positive number, so this
probably is not the right one to use, but I was just experimenting).
Cannot find the constant of proportionality for the Salpeter IMF
(obviously the number of stars in each bin will depend on the total
sample).

11/15/15
Getting there, but need to set x min and max to cover the proper range
in masses.

11/18/15
Plots look correct (I think). Need to plot the Salpeter trend correctly,
and figure out how to manage axis labels (ie keep them from overlapping).
