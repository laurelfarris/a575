
; 1. my mac
; 2. my desktop machine (acrux)
; 3. astronomy
; 4. hyades
; 5. praesepe
; 6. virgo

PRO q08

;number of machines
n = 7 

;number of information
m = 5

;Array for everything
machine = STRARR(n)
speed = STRARR(n)
mem = STRARR(n)
swap_space = STRARR(n)
disk_space = STRARR(n)

;Assign values to all arrays
machine(1)='mac'       & speed(1)='2.8GHz'     & mem(1)='8.0G' 
		       swap_space(1)='?'      & disk_space(1)='112.0G'
machine(2)='acrux'     & speed(2)='0.8GHz'           & mem(2)='5.4G' 
                       swap_space(2)='5.6Gby'      & disk_space(2)='9.7G'
machine(3)='astronomy' & speed(3)='2612.1GHz'    & mem(3)='16.4G' 
                       swap_space(3)='0.0Gby'      & disk_space(3)='9.5G'
machine(4)='hyades'    & speed(4)='800.0GHz'     & mem(4)='32.0G' 
                       swap_space(4)='65.5Gby'      & disk_space(4)='8.4T'
machine(5)='praesepe'  & speed(5)='800.0GHz'     & mem(5)='132.0G'
                       swap_space(5)='262.0Gby'      & disk_space(5)='2.9T'
machine(6)='virgo'     & speed(6)='1400.0GHz'    & mem(6)='64.0G' 
                       swap_space(6)='131.0Gby'      & disk_space(6)='12.0T'

;Convert speed from string to number, convert that number from
; whatever speed units it's currently in to flops, then convert
; that number back to a string.

;FOR i=0,n-l
;  temp=float(speed(i))
;  temp=math_math_math --> temp_in_flops
;  speed(i)=string(temp)
;END

;print out everything
OPENW, mylun, /get_lun, "q08_table.txt"
PRINTF, mylun,' '
PRINTF, mylun, FORMAT='(A-10,4(A15))','MACHINE','SPEED','MEMORY', $
                                'SWAP_SPACE','DISK_SPACE'
PRINTF, mylun,' '

  FOR i=1,n-1 DO BEGIN
    PRINTF, mylun,FORMAT='(A-10,4(A15))',machine(i),speed(i),mem(i), $
                      swap_space(i), disk_space(i)
  END 

PRINTF, mylun,' '
free_lun, mylun

END
