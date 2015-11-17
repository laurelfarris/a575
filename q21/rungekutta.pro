;Programmer:		Laurel Farris
;Course:			ASTR 565 - Stellar Interiors
;Last Modified:		08 October 2015
;Description:       Use the fourth-order Runge-Kutta method to 
;					approximate the Lane-Emden equation for
;					polytropic index n = 4.5
;--------------------------------------------------------------------;

function rungekutta(index)

number=3500 
x=fltarr(number)    ;xi
y=fltarr(number)    ;theta
z=fltarr(number)    ;d(theta)/d(xi)
h = 0.01            ;step in x


;To find the first values for y and z, use the Lane_Emden equation
; expanded about the origin:
x[0]=h 
y[0]=1.0 
z[0]=-(1./3.)*x[0]+index*(x[0]^3.)/30.-((48.*index^2.-30*index)/15120.)*$
                                                       (x[0])^5.
;; Runge-Kutta method:                                                       
i=0
while (y[i] >= 0) do begin
	k1 = h*z[i]
	l1 = h*( (-2.*z[i]/x[i]) - (y[i])^index )
	k2 = h*(z[i]+0.5*l1)
	l2 = h*( (-2.*(z[i]+0.5*l1)/(x[i]+0.5*h)) - (y[i] + 0.5*k2)^index )
	k3 = h*(z[i]+0.5*l2)
	l3 = h*( (-2.*(z[i]+0.5*l2)/(x[i]+0.5*h)) - (y[i] + 0.5*k3)^index )
	k4 = h*(z[i]+l3)
	l4 = h*( (-2.*(z[i]+l3)/(x[i]+h)) - ((y[i]) + k3)^index )

	y[i+1] = y[i] + (1./6.)*k1 + (1./3.)*k2 + (1./3.)*k3 + (1./6.)*k4
	z[i+1] = z[i] + (1./6.)*l1 + (1./3.)*l2 + (1./3.)*l3 + (1./6.)*l4
	x[i+1] = x[i] + h 
	i=i+1
endwhile

finalArray = fltarr(3,number)
finalArray[0,*] = x
finalArray[1,*] = y
finalArray[2,*] = z
return, finalArray

end
