import matplotlib.pyplot as plt
import numpy as np
import math

# Numbers given for problem
pixels = 8192
sigma = 5

# Create delta function(s): f(x)
f = np.zeros(pixels)
for i in range(0,pixels,10):
    f[i] = 1

# Create gaussian: h(x)
#h = (math.sqrt(2.*math.pi*sigma**2) * 
 #   math.exp( (-(x-a)**2)/(2.*sigma**2)))
h = np.zeros(sigma)
# ...?

## Convolve pixel array with a gaussian in physical space: g(i) = f(x) * h(x)
#   '*' here denotes a convolution, not multiplication

total = 0
for i in range(0,pixels):
    for j in range(0,pixels):
        total = total + f[i] * h[i-j] 
    
## Do the convolution in Fourier space by:

#taking the FT of f and h:
FT_f = np.fft.fft(f) 
FT_h = np.fft.fft(h)

# multiplying them, and FT-ing them back:
FT_g = np.fft.fft(FT_f * FT_h)

# ... should be the same result either way? Maybe without FT-ing them
# back...

# Plot the convolution and the final result:
fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

ax1.plot(x,g)
ax2.plot(x,FT_g)

plt.show()
#plt.savefig('q32.png')
