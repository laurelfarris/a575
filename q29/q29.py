import matplotlib.pyplot as plt
import numpy as np
import pdb
import matplotlib
matplotlib.rc('font',**{'family':'serif','serif':['Times']})
matplotlib.rc('text',usetex=True)

# The Salpeter IMF gives a constant of proportionality of 0.53 when
# the integral from 0.5 to 100 M is set equal to one.

# IMF distribution:
def IMF(mass):
    #return 0.53*mass**(-2.35)
    return (0.53*(10**mass)**(-2.35))
    #return np.log10(0.53*(10**mass)**(-2.35))

# Transformation method
def trans(y):
    return (y/0.53)**(-1./2.35)

# Plot several different sample sizes (total number of stars)
N=[100,1000,10000,100000]

# Create arrays of random values between 0 and 1 ('dN/dM')
y1 = np.random.random(N[0])
y2 = np.random.random(N[1])
y3 = np.random.random(N[2])
y4 = np.random.random(N[3])

# Get arrays of masses back, between 0.5 and 100 (M_sun)
x1 = (trans(y1))
x2 = (trans(y2))
x3 = (trans(y3))
x4 = (trans(y4))

# Convert x arrays to log (separate because this might not work).
x1 = np.log10(x1)
x2 = np.log10(x2)
x3 = np.log10(x3)
x4 = np.log10(x4)

# Create axes objects for all four samples
fig=plt.figure()
ax1=fig.add_subplot(221)
ax2=fig.add_subplot(222)
ax3=fig.add_subplot(223)
ax4=fig.add_subplot(224)

# Plot the histograms on one figure, with the Salpter IMF plotted over each one.
ax1.hist((x1),bins=50)
ax2.hist((x2),bins=50)
ax3.hist((x3),bins=50)
ax4.hist((x4),bins=50)

'''
# Plot the Salpeter IMF on top of each histogram
ax1.plot(x1,IMF(x1))
ax2.plot(x2,IMF(x2))
ax3.plot(x3,IMF(x3))
ax4.plot(x4,IMF(x4))
'''

# Make plots presentable
ax1.set_xlim(min(x1),max(x1))
ax2.set_xlim(min(x2),max(x2))
ax3.set_xlim(min(x3),max(x3))
ax4.set_xlim(min(x4),max(x4))

ax1.set_xlabel('mass (M$_{\odot}$)')
ax1.set_ylabel('counts')
ax1.set_title('Sample of 100')
ax2.set_xlabel('mass (M$_{\odot}$)')
ax2.set_ylabel('counts')
ax2.set_title('Sample of 1,000')
ax3.set_xlabel('mass (M$_{\odot}$)')
ax3.set_ylabel('counts')
ax3.set_title('Sample of 10,000')
ax4.set_xlabel('mass (M$_{\odot}$)')
ax4.set_ylabel('counts')
ax4.set_title('Sample of 100,000')
# Save the figure
plt.savefig('hist.png')



