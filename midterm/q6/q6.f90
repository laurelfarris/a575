!Calculate the sum of all integers from 1 to 1000 and print it out

PROGRAM q6

integer :: x = 1        !'x' is the incremental variable for the loop
integer :: answer = 0   !'answer' is the sum 

do while (x .le. 1000)
  answer = answer + x
  x=x+1
enddo

print*, 'The sum of all integers from 1 to 1000 is: ', answer

END
