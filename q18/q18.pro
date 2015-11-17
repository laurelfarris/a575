; Instructions:

;Write a program that performs the following:
; - a variable starts with a value of one.
; - Construct a loop that executes until the variable is larger than 100.
; - In each loop execution
;    - calculate the factorial of the variable if the variable is less than 20
;    - double the value of the variable and add one to it.
; - Output the total number of times the loop is executed
; - Output the sum of all of the factorials that were calculated.
; - Make the conditions general, so that they can be set at the top of
;         the program, or entered by the user... prompt?
;
;Do this in as many as you can of Fortran, C, Python, and IDL! Use a makefile
;to compile your programs (where necessary) and to execute all four.
;
;Bonus: compute the factorial using a recursive function.

x=1            ;"The Variable"
maxvalue1=100  ;Loop until The Variable is less than or equal to this
maxvalue2=20   ;Calculate while The Variable is less than this

n=0 ;Number of times the loop is executed
facTotal=0 ;Sum of all factorials

while (x le maxvalue1) do begin
  if (x lt maxvalue2) then begin
    fac=1
    for i=1,x do begin
      fac=fac*i
    endfor
    facTotal=facTotal+fac
  endif
  x =(2*x)+1
  n=n+1
endwhile

print, format='("This loop ran a total of ", I2, " times.")', n
print, format='("The sum of all the factorials calculated is: ", E0.2)', fac

END
