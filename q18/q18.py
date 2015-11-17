#!/usr/bin/env python
#
#Instructions:
#
#Write a program that performs the following: 
# - a variable starts with a value of one. 
# - Construct a loop that executes until the variable is larger than 100.
# - In each loop execution 
#    - calculate the factorial of the variable if the variable is less than 20 
#    - double the value of the variable and add one to it.
# - Output the total number of times the loop is executed
# - Output the sum of all of the factorials that were calculated.
# - Make the conditions general, so that they can be set at the top of 
#         the program, or entered by the user... prompt?
#
#Do this in as many as you can of Fortran, C, Python, and IDL! Use a makefile
#to compile your programs (where necessary) and to execute all four.
#
#Bonus: compute the factorial using a recursive function. 

x = 1            #"The Variable"
maxvalue1 = 100  #Loop until The Variable is less than or equal to this
maxvalue2 = 20   #Calculate while The Variable is less than this

n=0   #Number of times the loop is executed
facTotal=0L   # Sum of all factorials

while (x <= maxvalue1):
	if (x < maxvalue2):
		fac=1L
		for i in range(1,x+1):  # final value in range NOT inclusive!
			fac=fac*i
		facTotal=facTotal+fac
		print fac
	x=(2*x)+1
	n=n+1

print "This loop ran a total of ", n, "times."
print "The sum of all the factorials calculated is: ", fac

