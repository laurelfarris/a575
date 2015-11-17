Instructions:
Rewrite your Lane Emden program, attempting to use better computing practices
as mentioned in class: fully commented, no built-in numbers (e.g., nsteps),
separate integrating routine, modular implementation of integration, constant
calculation, and plotting. Make sure to validate your results! Use your
modified routine to systematically investigate the choice of step size on your
results.

10/14/2015
In the interest of getting this finished on time, I''m going to continue using
IDL, then rewrite it in python if I have time.

10/15/2015
Scratch that... attempting a python version now.
Working on figuring out the best way to return the arrays I need from
runge-kutta. 

Returning values, dictionary style. Having issues raising a negative number to
a fractional index (mine is 4.5).

10/17/2015
Put an if statement in runge-kutta module, followed by a break.
Program seems to be working now: ouput values are slightly different
than they were for the homework assignment; hopefully more accurate. 
Ouput also formatted, python-style. 
