import matplotlib.pyplot as plt
import numpy as np
import pdb

# The Salpeter IMF gives a constant of proportionality of 0.53 when
# the integral from 0.5 to 100 M is set equal to one.
def transformed(y):
    return (y/0.53)**(-1./2.35) 

#pdb.set_trace()

# Plot several different sample sizes (total number of stars)
samples=[10,100,1000,10000]
x = []
y = []

# Loop through a few different sample sizes
for N in range(0,len(samples)):
    y.append(np.random.random(samples[N]))
    x.append(transformed(y[N]))

# Create axes objects for all four samples
fig=plt.figure()
ax1=fig.add_subplot(221)
ax2=fig.add_subplot(222)
ax3=fig.add_subplot(223)
ax4=fig.add_subplot(224)

# Plot the histograms on one figure
ax1.hist(y[0],bins=50)
ax2.hist(y[1],bins=50)
ax3.hist(y[2],bins=50)
ax4.hist(y[3],bins=50)

plt.savefig('hist.png')
