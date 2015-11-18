import matplotlib.pyplot as plt
import numpy as np
import math
import pdb

'''
Instructions:

For a specified total number of stars, and a specifed lower mass limit, make
several realizations of the Hess diagram, using Poisson random deviates to
populate each bin.
'''

# Total number of stars
N = 10
# Lower mass limit (in solar masses)
min_mass = 0.3

# Poisson distribution syntax: np.random.poisson(lam=1.0, size=None)

# Generate some random numbers
x = np.random.poisson(lam=1.0,size=N)
print x

# Read in data
data=my_isochrones.read('../zm01.dat',columns=['logTe','mbol','z','imf'],age=9)

# Make realizations...?

# Call the 'hess' function to plot the hess diagram
my_isochrones.hess(data['logTe'],data['mbol'],data['imf'])


