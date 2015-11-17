import pdb
import numpy as np
import matplotlib.pyplot as plt
import my_isochrones
from astropy.io import ascii
from astropy.io import fits

# Purpose: import isochrone module to read in data and plot a Hess
# diagram for data at an age of one Gyr and solar metallicity.


# Read in data
data=my_isochrones.read('zp00.dat',columns=['logTe','mbol','z','imf'],age=9)
# Call the 'hess' function to plot the hess diagram
my_isochrones.hess(data['logTe'],data['mbol'],data['imf'])
# Show the figure for inspection
#plt.show()
# Uncomment to save picture to file
plt.savefig('hess_diagram.png')


# Syntax: fits.writeto('out.fits',data,header)
#         fits.append('out.fits',data,header)

fits.writeto('hess.fits',data['logTe'])




