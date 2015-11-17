import os
import numpy as np
from astropy.io import ascii
import pdb
import astropy
import math
import matplotlib.pyplot as plt

# specify 'age' to request all 18 characteristics for objects with
# certain age
# specify 'columns' to request certain characteristics at all ages.
def read(infile,columns=None,age=None):
    # Read in data
    # (ascii knows to ignore lines starting with '#' !!! )
    data=ascii.read(infile, names=
       ['z','age','m_ini','m_act','log_L/Lo','logTe','logG','mbol',
       'U','B','V','R','I','J','H','K','imf','stage'])

    # If an age is specified, pull data from just that age
    if age is not None:
        # return indices of rows where data in the 'age' column is
        # equal to the age specified in call statement.
        gd=np.where(data['age']==age)
        # Assign data in previous index to 'data'
        data = data[gd]
    # default columns
    if columns is None:
        # If no columns are specified, then return only a few of them
        # (you could say these are the 'default' return values)
        #    Could specify column number rather than name? Confusing.
        data.keep_columns(['z','age','log_L/Lo','logTe','imf','stage'])
        pass
    else:
        # 'keep' the columns that the user asked for and return them
        data.keep_columns(columns)
        pass
    return data



# Make a hess diagram, defaulting to hr diagram
def hess(x,y,z,xlabel=None,ylabel=None,binsize=None):
    print len(x)
    print len(y)
    print len(z)
    cs = plt.contour(x,y,z)
    plt.clabel(cs)
'''
    N,xedges,yedges=binned_statistic_2d(x,y,z,'count',bins=100)
    cmap.set_bad('w',1.)
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.imshow
    #np.histogram2d(x,y,bins=100)
    #ax.colorbar()
    if xlabel is None:
        ax.set_xlabel('T$_{\\rm eff}$ [K]')
        ax.set_xlim(4,3.4)
    if ylabel is None:
        ax.set_ylabel('Bolometric Magnitude')

    color = []
    for i in range(0,len(z)-1):
        color.append(z[i+1]-z[i])
    color = (np.array(color))
    x = x[:-1]
    y = y[:-1]
    x,y,z=np.mgrid[x,y,z]
    plt.imshow(z,
'''
