import pdb #pdb.set_trace()
import numpy as np
import matplotlib.pyplot as plt
import my_isochrones
from astropy.table import Table, Column

# Top panel: Plot magnitude as a function of effective temperature
# Bottom panel: Plot surface gravity as a function of effective temperature
# Left panel: all metallicities and age = 1 Gyr
# Right panel: all ages, metallicity = solar (~0.02)
# Color code all points by age

# Read data
age=[]
temp=[]
grav=[]
mag=[]
z=[]

n=21 # number of files to be read
n=1
for i in range (1,n+1):
    if i < 10:
        file = '/home/holtz/analysis/apogee/dist/isochrones/zm0'+str(i)+'.dat'
    else:
        file = '/home/holtz/analysis/apogee/dist/isochrones/zm'+str(i)+'.dat'
    file = 'zp00.dat'
    data = my_isochrones.read(file,columns=('age','logTe','logG','mbol','z'))
    age.append(data['age'])
    temp.append(data['logTe'])
    grav.append(data['logG'])
    mag.append(data['mbol'])
    z.append(data['z'])

# Note that each of these contains 19 elements, and each of those
# contains several thousand lines of data.
age=np.array(age)
temp=np.array(temp)
grav=np.array(grav)
mag=np.array(mag)
z=np.array(z)

#myTable = Table([age,temp,grav,mag,z],names=('age','logTe','logG','mbol','z'))

# Create axes objects
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)


for i in range (0,n):
# Data for a single age
    t1 = temp[np.where(age[i]==9)]
    m1 =  mag[np.where(age[i]==9)]
    g1 = grav[np.where(age[i]==9)]
    ax1.scatter(t1,g1)
    ax3.scatter(t1,m1)
'''
# Data for a single metallicity
    t2 = temp[np.where(z[i]==0.02)]
    m2 =  mag[np.where(z[i]==0.02)]
    g2 = grav[np.where(z[i]==0.02)]
    ax2.scatter(t2,g2)
    ax4.scatter(t2,m2)
'''

plt.show()

'''
Make copies in case I screw everything up
    d1 = data[np.where(data['age']==9)]
    d2 = data[np.where(data['z']==0.02)]
    c1 = d1['z']
    c2 = 10**(d2['age'])
    size = 1

ax1.scatter(d1['logTe'],d1['logG'],s=size,c=c1)
ax2.scatter(d2['logTe'],d2['logG'],s=size,c=c2)
ax3.scatter(d1['logTe'],d1['mbol'],s=size,c=c2)#cmap='winter')
ax4.scatter(d2['logTe'],d2['mbol'],s=size,c=c2)
# Set labels only for plot edges... how to do this in a nicer way?
# plot looks kind of crowded
ax1.set_ylabel('$log(g)$')
ax3.set_xlabel('$T_{eff} [K]$')
ax3.set_ylabel('$M_{bol}$')
ax4.set_xlabel('$T_{eff} [K]$')

# Save figure
plt.savefig('q24.png')

'''
