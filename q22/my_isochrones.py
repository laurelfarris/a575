import os
import numpy as np
from astropy.io import ascii
import pdb
import astropy
import math

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
