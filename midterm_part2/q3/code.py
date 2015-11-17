# This program includes all parts from q3 for the midterm.
# 
import numpy as np
import math
import matplotlib.pyplot as plt

# (a) Simple function
def myfunction(x):
	n1 = 3				# n's --> exponents (specific to this function,
	n2 = (2./3.)		#                           not general).
	y = x**n1 + x**n2   # y = f(x)
	return y

result_a = myfunction(2)
print "part (a)"
print 'The value of f(x) for x = 2 is: ',result_a
print 'This was tested using a calculater.'
print ""

# (b) Simpson's algorithm
def integral(a,b):
	c = (a+b)/2.
	return(  
	    ((b-a)/6.) * 
		( (a**3 + a**(2./3.)) + 
	    4.*(c**3 + c**(2./3.)) + 
		(b**3 + b**(2./3.)) )
		)
result_b = integral(0,1)
print "part (b)"
print 'The integral of this function from 0 to 1 using Simpson\'s algorithm is: ',result_b
print 'The integral as calculated by hand is: ',17./20.
print ""

# (c)
result_c = integral(0,10)
print "part (c)"
print 'Setting the definite integral from 0 to 10 and \
using Simpson\'s algorithm gives: ',result_c
print ""

## Pass a function as an actual python function

# (d) Correct answer; use this to determine fractional accuracy
#      of Simpson's algorithm
def second_integral(a,b):
	n1 = 3.
	n2 = 2./3.
	x = b
	func = x**n1 + x**n2
	upper_limit = (1./(n1+1))*(x**(n1+1)) + (1./(n2+1.))*(x**(n2+1))
	x = a
	lower_limit = (1./(n1+1))*(x**(n1+1)) + (1./(n2+1.))*(x**(n2+1))
	y = upper_limit-lower_limit
	return y

result_d = second_integral(0,10)
print "part (d)"
print "The analytical result from 0 to 10 is: ",result_d
accuracy = math.fabs(result_d - result_c)/result_d
print "The fractional accuracy between the two answers is: ", accuracy
print ""

# (e)
'''
The function 'third_integral' takes the number of pieces and does a 
separate integral for each one, adding them all at the end. 
This function is then called 10 times, each time dividing the integral
into smaller and smaller pieces, increasing the accuracy.
'''
def third_integral(a,b,pieces,result_d):
	inc = (b-a)/pieces # increment
	n1 = 3.
	n2 = 2./3.
	final = 0
	for i in range(a,b,inc):
		x = i+inc
		upper_limit = (1./(n1+1))*(x**(n1+1)) + (1./(n2+1.))*(x**(n2+1))
		x = i
		lower_limit = (1./(n1+1))*(x**(n1+1)) + (1./(n2+1.))*(x**(n2+1))
		final = final + (upper_limit - lower_limit)
	accuracy = math.fabs(result_d - result_c)/result_d
	return accuracy

a = 0	# lower limit
b = 10	# upper limit 
xx = np.array([1,2,3,4,5,6,7,8,9,10]) # 'x-axis': number of pieces
yy = np.array([]) # 'y-axis': fractional accuracy

for j in range(1,11):
	result_e = third_integral(a,b,j,result_d)
	yy=np.append(yy,result_e*100.)
print "part (e)"
print ""

# (f)
plt.plot(xx,yy)
plt.xlabel('Number of Pieces')
plt.ylabel('Percent Accuracy')
plt.savefig('figure_1.png')
#plt.show()
