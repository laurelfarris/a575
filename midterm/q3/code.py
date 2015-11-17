# (a)
# This code was tested by using the function (after it was defined of course) 
# on a random number, and calculating it by hand to make sure the value is correct.

import numpy as np
import math
import matplotlib.pyplot as plt

def myfunction(x):
	y = x**3 + x**(2./3.)
	return y

var = myfunction(2)
print var

# (b)
#This was tested by calculating the integral by hand and comparing it 
#to the output of the function. The function from (a) was hard-coded in...
#will change this if I have time.

def integral(a,b):
	c = (a+b)/2.
	y = (  
	    ((b-a)/6.) * 
		( (a**3 + a**(2./3.)) + 
	    4.*(c**3 + c**(2./3.)) + 
		(b**3 + b**(2./3.)) )
		)
	return y

result = integral(0,1)
#print result
#print 17./20.

# (c)

result_c = integral(0,10)
print "The numerical result of part (c) is: ",result_c


# (d)
def second_integral(a,b):
	n1 = 3.
	n2 = 2./3.
	x = b
	func = x**n1 + x**n2
	x = b
	step1 = (1./(n1+1))*(x**(n1+1)) + (1./(n2+1.))*(x**(n2+1))
	x = a
	step2 = (1./(n1+1))*(x**(n1+1)) + (1./(n2+1.))*(x**(n2+1))
	y = step1-step2
	return y

result_d = second_integral(0,10)
print "The result from part (d) is: ",result_d
#print 17./20.


# (e)
array = np.array[]
def third_integral(a,b,pieces):
	increment = (b-a)/pieces
	n1 = 3.
	n2 = 2./3.
	for i in range(a,b,increment):
		x = i+increment
		func = x**n1 + x**n2
		step1 = (1./(n1+1))*(x**(n1+1)) + (1./(n2+1.))*(x**(n2+1))
		x = i
		step2 = (1./(n1+1))*(x**(n1+1)) + (1./(n2+1.))*(x**(n2+1))
		y = step1-step2
		array.append(
	return y


result = third_integral(0,10,5)

# (f)
plt.plot([1,2,4,3])
plt.show()
