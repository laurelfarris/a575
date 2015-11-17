import numpy as np
import math
import my_isochrones

filename = "zp00.dat"
data = my_isochrones.read(filename, age=9)

fout = open('output.dat','w')
print >> fout, data

# Example for writing to file:
# print >> fout, 'Filename:', filename  # or f.write('...\n')

fout.close()
