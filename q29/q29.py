import matplotlib.pyplot as plt
import numpy as np
import pdb

# The Salpeter IMF gives a constant of proportionality of 0.53 when
# the integral from 0.5 to 100 M is set equal to one.

def IMF(y):
    return (y/0.53)**(-2.35)

def transformed(y):
    return (-1.35*y/0.53)**(-1./1.35) 


# Plot several different sample sizes (total number of stars)
samples=[10,100,1000,10000]
ynew = []
xnew = []
y = []

# Loop through a few different sample sizes
for N in range(0,len(samples)):
    y.append(np.random.random(samples[N]))
    #ynew.append(transformed(y[N]))
    ynew.append(transformed(np.random.random(samples[N])))
    xnew.append(IMF(ynew))

# Create axes objects for all four samples
fig=plt.figure()
ax1=fig.add_subplot(221)
ax2=fig.add_subplot(222)
ax3=fig.add_subplot(223)
ax4=fig.add_subplot(224)

# Plot the histograms on one figure
ax1.hist(xnew[0],bins=50)
ax2.hist(xnew[1],bins=50)
ax3.hist(xnew[2],bins=50)
ax4.hist(xnew[3],bins=50)

plt.savefig('hist.png')
