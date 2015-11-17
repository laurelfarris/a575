import math

detectors = 62.
pixels = (2048.*4096)
bytes = 2.
images=500.

totalBytes = detectors*pixels*bytes*images
print 'This is {:5.2e} bytes of data!'.format(totalBytes)
