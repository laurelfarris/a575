#Programmer:		Laurel Farris
#Course:			ASTR 565 - Stellar Interiors
#Last Modified:		15 October 2015

## Part 1: Solve the Lane-Emden Equation numerically for n = 4.5

#"The RK4 function uses the fourth-order Runge-Kutta method to advance
#a solution to a system of ordinary differential equations one
#time-step h, given values for the variables Y and their derivatives
#dydx known at X. To calculate the fourth-order R-K, evaluate four 
#times per timestep: 

import math
import numpy as np
import matplotlib.pyplot as plt
import pdb
import astropy.constants as const
#pdb.set_trace()

#-----------------------------------------------------------------------#

## Polytropic index, n
index = 4.5

#To find the first values for y and z, use the Lane_Emden equation
# expanded about the origin:
h=0.001
xo=h 
yo=( 1. - (xo**2/6.) + (index*xo**4./120.) -
       index*(8.*index-5)*xo**6./15120. ) 
zo=( -xo/3. + index*xo**3./30. -
       (8.*index**2.-5.*index)*xo**5./2520 )

from maths import runge_kutta
dic = runge_kutta(index,xo,yo,zo)
x = np.array(dic['xi'])
y = np.array(dic['theta'])
z = np.array(dic['d_theta'])

# 2(b) Plot theta, theta**n, theta**(n+1), and q vs. xi

E1 = max(x) 
q = ((x**2)*z)*((E1**2.)*z[-1])**(-1.)
plt.plot(x,y, color="purple")
plt.plot(x,y**index)
plt.plot(x,y**(index+1))
plt.plot(x,q)
plt.show()

## Constants
pi = math.pi
G = const.G.cgs.value
Mass = const.M_sun.cgs.value
Radius = const.R_sun.cgs.value
k_B = const.k_B.cgs.value
m_u = const.u.cgs.value
# mass fractions of hydrogen(X), helium(Y), and metals(Z)
H_mass_frac = 0.7
Z_mass_frac = 0.02
He_mass_frac = 1. - (H_mass_frac + Z_mass_frac) 
# mean molecular weight
mu = ( (2.*H_mass_frac)+(0.75*He_mass_frac)+(0.5*Z_mass_frac) )**(-1.)

## Part 2: Show results
## 2(a) Calculate 8 quantities

N = (	(((4.*pi)**(1./index))/(index+1.)) *           
    (  ((-E1**((index+1.)/(index-1.))) * z[-1]  )** 
	                        ((1.-index)/index)  )  )
W = ( 4.*pi*(index+1.)*(z[-1]**2. ))**(-1.)
bigTheta= ( -(index+1)*E1*z[-1] )**(-1.)
rho_c = (  (-E1/3.)*(z[-1]**(-1))*(3.*Mass/(4.*pi*Radius**3.))   )
P_c = W*G*((1.99**2.)/(6.96**4.))*(1.e26) 
T_c = bigTheta*G*Mass*mu*m_u/(k_B*Radius)
rho_ratio = rho_c/( 3.*Mass/(4.*pi*Radius**3.)  )

#Output values in nice tabular format
print 'n =     {:10.3f}'.format(index)
print 'E1 =    {:10.3f}'.format(E1)
print 'p/p_c = {:10.3f}'.format(rho_ratio)
print 'N =     {:10.3f}'.format(N)
print 'W =     {:10.3f}'.format(W)
print 'Theta = {:10.3f}'.format(bigTheta)
print 'p_c =   {:10.3f}'.format(rho_c)
print 'P_c =   {:10.3e}'.format(P_c)
print 'T_c =   {:10.3e}'.format(T_c)


