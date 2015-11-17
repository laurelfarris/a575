!Instructions:
!
!Write a program that performs the following: 
! - a variable starts with a value of one. 
! - Construct a loop that executes until the variable is larger than 100.
! - In each loop execution 
!    - calculate the factorial of the variable if the variable is less than 20 
!    - double the value of the variable and add one to it.
! - Output the total number of times the loop is executed
! - Output the sum of all of the factorials that were calculated.
! - Make the conditions general, so that they can be set at the top of 
!         the program, or entered by the user.
!
!Do this in as many as you can of Fortran, C, Python, and IDL! Use a makefile
!to compile your programs (where necessary) and to execute all four.
!
!Bonus: compute the factorial using a recursive function. 


PROGRAM q18
implicit none

real :: maxvalue1 = 100  !Loop until The Variable is less than or equal to this
real :: maxvalue2 = 20   !Calculate while The Variable is less than this
real :: fac!factorial value for individual loop
real :: facTotal=0!Sum of all the factorials calculated
integer :: x = 1 !"The Variable"
integer :: n=0 !Number of times the loop is executed
integer :: i ! Counter for 'do loop'

do while (x .le. maxvalue1)
  if (x .lt. maxvalue2) then 
    fac=1 
    do i=1,x
      fac=fac*i
    enddo 
    facTotal=facTotal+fac
  endif
  x=(2*x)+1
  n=n+1
enddo

print*, 'This loop ran a total of ', n, ' times.'
print*, 'The sum of all the factorials calculated is: ', fac, '.'

END
