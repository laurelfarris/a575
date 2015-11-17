import numpy as np
def runge_kutta(index,xo,yo,zo):
	h=0.001
	x=[xo]
	y=[yo]
	z=[zo]
	i=0
	while y[i] >= 0: 
		k1 = h*z[i]
		l1 = h*( (-2.*z[i]/x[i]) - ((y[i])**index) )
		k2 = h*(z[i]+0.5*l1)
		if (y[i] + 0.5*k2)<0:
			dic = { 'xi':x, 'theta':y, 'd_theta':z }
			return dic
			break
		l2 = h*( (-2.*(z[i]+0.5*l1)/(x[i]+0.5*h)) - ((y[i] + 0.5*k2)**index) )
		k3 = h*(z[i]+0.5*l2)
		l3 = h*( (-2.*(z[i]+0.5*l2)/(x[i]+0.5*h)) - ((y[i] + 0.5*k3)**index) )
		k4 = h*(z[i]+l3)
		l4 = h*( (-2.*(z[i]+l3)/(x[i]+h)) - ((y[i] + k3)**index) )

		x.append(x[i] + h) 
		y.append(y[i] + (1./6.)*k1 + (1./3.)*k2 + (1./3.)*k3 + (1./6.)*k4)
		z.append(z[i] + (1./6.)*l1 + (1./3.)*l2 + (1./3.)*l3 + (1./6.)*l4)
		i=i+1


