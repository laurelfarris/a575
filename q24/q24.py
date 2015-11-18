import pdb #pdb.set_trace()
import numpy as np
import matplotlib.pyplot as plt
import my_isochrones
from astropy.table import Table, Column
import matplotlib

# Top panel: Plot magnitude as a function of effective temperature
# Bottom panel: Plot surface gravity as a function of effective temperature
# Left panel: all metallicities and age = 1 Gyr
# Right panel: all ages, metallicity = solar (~0.02)
# Color code all points by age

matplotlib.rc('font',**{'family':'serif','serif':['Times']})
matplotlib.rc('text',usetex=True)

# Read data
age=[]
temp=[]
grav=[]
mag=[]
z=[]

n=21 # number of files to be read

for i in range (1,n+1):
    if i < 10:
        file = '/home/holtz/analysis/apogee/dist/isochrones/zm0'+str(i)+'.dat'
    else:
        file = '/home/holtz/analysis/apogee/dist/isochrones/zm'+str(i)+'.dat'
    #file = 'zp00.dat'
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

# Create axes objects
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
t1 = []
m1 = []
g1 = []
t2 = []
m2 = []
g2 = []
z1 = []
color_z = []
temporary_max = []
temporary_min = []
for i in range (0,n):
# Data for a single age
    t1.append(temp[i][np.where(age[i]==9)])
    m1.append(mag[i][np.where(age[i]==9)])
    g1.append(grav[i][np.where(age[i]==9)])
    z1.append(z[i][np.where(age[i]==9)])

for i in range(0,n):
    for j in range(0,len(z1[i])):
        color_z.append(z1[i][j])

vmax_z = max(color_z)
vmin_z = min(color_z)
cmap = 'winter'
ax1.scatter(t1,g1,c=color_z,cmap=cmap)
ax3.scatter(t1,m1,c=color_z,cmap=cmap)

pdb.set_trace()

ax2.scatter(t2,g2,vmin=vmin,vmax=vmax,c=color,cmap=cmap)
ax4.scatter(t2,m2,vmin=vmin,vmax=vmax,c=color,cmap=cmap)
plt.savefig('something.pdf')
#plt.show()


