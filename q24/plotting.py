import matplotlib.pyplot as plt
import astropy.constants as cnst
import math

M_sun = cnst.M_sun.cgs.value

def hr_diagram(temp,lum,rad):
    size = rad*1000
    plt.scatter(temp,lum,c=rad,s=size, linestyle=0)
    plt.xlabel('$T_{eff}$')
    plt.ylabel('$L/L_{\odot}$',rotation='horizontal')
    plt.savefig('hr_diagram.png')
    plt.clf()

# 2. Plot showing where the internal convection and radiation
#     zones are for each star: m(r)/M* as function of M*/M_sun 
def money(solar_mass,mass_profile,num_models):
    for k in range(0,num_models):
        mass_profile[k] = mass_profile[k]/(max(mass_profile[k]))
        plt.plot(solar_mass[k],mass_profile[k],color='black') 
    plt.xlabel('log $M_*/M_{\odot}$')
    plt.ylabel('$m(r)/M_*$')#,rotation='horizontal')
    plt.savefig('money.png')
    plt.clf()

# 3. Same as (2.), but r/R* as ordinate
def money2(solar_mass,radial_profile,num_models):
    for k in range(0,num_models):
        radial_profile[k] = radial_profile[k]/(max(radial_profile[k]))
        plt.plot(solar_mass[k],radial_profile[k],color='black') 
    plt.xlabel('log $M_*/M_{\odot}$')
    plt.ylabel('$r/R_*$',rotation='horizontal')
    plt.savefig('money2.png')
    plt.clf()

# Given the temperature profile of a star, plot the true driving
# gradient, the radiation gradient, and the adiabatic gradient as
# functions of the temperature.
def gradients(grad,grad_ad,grad_rad,temp,filename): 
    #plt.subplot(2,1,1)
    plt.plot(temp, grad)
    plt.plot(temp, grad_ad)
    plt.plot(temp, grad_rad)
    plt.xlabel('log $T(r)$')
    plt.ylabel('$gradient$')
    plt.savefig(filename+'.png')
    plt.clf()

# Given the temperature profile of a star, plot the B-V frequency as
# functions of the temperature.
def BV(BVfreq,temp,filename):
    plt.plot(temp,BVfreq) 
    plt.xlabel('log $T(r)$')
    plt.ylabel('BV',rotation='horizontal')
    plt.savefig(filename+'.png')
    plt.clf()


