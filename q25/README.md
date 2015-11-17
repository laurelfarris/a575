Instructions:

A Hess diagram is a 2-dimensional representation of a pair of stellar
parameters, with the number of stars given at each of the parameter pairs; for
example, an HR diagram with effective temperature and magnitude as the two
axes, with the number of stars at each location specified. Add a function to
your isochrone module to create a Hess diagram of an isochrone, with x and y
quantities specified as parameters (defaulting to effective temperature and
luminosity), with optional bin sizes specified. The number of stars between two
isochrone points is given by the difference between the INT IMF values for the
two points, so you could, for example, load this many stars into a rectangular
region as defined by the effective temperatures and magnitudes of the two
points. Create a Hess diagram for the 1 Gyr, solar metallicity isochrone, and
save it as a FITS file. Display it as an image.

Progress:

11/01/15
Started... At the moment, points are color coded by 'intimf', not the difference in
this value between points. Not sure what 'my' isochrone module is...
maybe the code from q24? Also having trouble using numpy arrays as
parameters in a function, which is why the hess diagram plotting is
not in its own function at the moment.

11/08/15
Been at this for a couple hours... had problems getting the third
dimension plotting option to work (array was not the correct size; had
to crop x and y for lack of a better idea). Trying to figure out how
to display as an image and save as a fits file. Found some good
documentation, but it's slow going... doing a lot of test codes and
'googling'.
