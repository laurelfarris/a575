;Programmer(s):		Laurel Farris
;Course:		N/A
;File Name:		correlation2.pro
;Function(s)		timelag.pro
;			correlation.pro?
;			  for 3 codes total... faster this way?
;Last modified:		21 July 2015
;Description:		Do a cross-correlation of each pixel with every
;			 other pixel (no repeats)
  

PRO correlation2, cube, output

PRINT, "Start:	", SYSTIME() ; Display time that code started running
pixels = (SIZE(cube))[1]     ; 1D dim of 'cube' (pixels) 
t = (SIZE(cube))[3] 	     ; Single value: Number of images
tau = [0:t:5]-(t/2)	     ; "Array of possible timelags"
output = [] 		     ; Append maxcor for every loop



;; Loop through every pair of pixels

; First pixel (ts1)
FOR x1=0, pixels-1 DO BEGIN
FOR y1=0, pixels-1 DO BEGIN
;--------------------------------------------------------------;

; Second pixel (ts2)

  y_test=y1+1 ;; start one pixel above ts1 

  FOR x2=x1,pixels-1 DO BEGIN
   FOR y2=y_test,pixels-1 DO BEGIN
 
     timelag, cube[x,y,*], cube[x2,y2,*], tau, maxcor ;Run timelag on 2 pixels
     output = [[output],[maxcor]] ;Append output array with the maximum correlation
                                  ; value and its corresponding timelag

   ENDFOR

  y_test=0 ;; loop back around to first value of y as ts2 increases in x

  ENDFOR

;--------------------------------------------------------------;
ENDFOR
ENDFOR

PRINT, "End:	", SYSTIME()
;PRINT, "Total run time:	", 
END


