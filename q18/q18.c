/*Instructions:

Write a program that performs the following: a variable starts with a value
of one. Construct a loop that executes until the variable is larger than 100.
In each loop execution, calculate the factorial of the variable if the
variable is less than 20, then double the value of the variable and add one
to it. Output the total number of times the loop is executed, and the sum of
all of the factorials that were calculated. Make the conditions general, so
that they can be set at the top of the program, or entered by the user.

Do this in as many as you can of Fortran, C, Python, and IDL! Use a makefile
to compile your programs (where necessary) and to execute all four.

Bonus: compute the factorial using a recursive function. */
 
#include<stdio.h>
int main(){

int x, maxvalue1, maxvalue2;
float fac, facTotal;
int i,n;
x=1;
maxvalue1=100;
maxvalue2=20;
n=0;
facTotal=0.0;
while(x <= maxvalue1){
    if(x < maxvalue2){
        fac=1.0;
        for(i=1;i<=x;i++){
            fac=fac*i;
        }
        facTotal=facTotal+fac;
    }	
    x=(2*x)+1;
    n=n+1;
}
printf("\nThis loop ran a total of %d times.",n);
printf("\nThe sum of all the calculated factorials is: %f",facTotal);
printf("\n\n");
return 0;
}
