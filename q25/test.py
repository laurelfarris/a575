import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits


hdu_list = fits.open('hess_diagram.fits')
hdu_list.info()


