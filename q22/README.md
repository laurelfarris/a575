Instructions:
We will be working with isochrones, as in Q11. Start an isochrone
module, with your first function a routine to read a single set of
Padova isochrones (as in the q11/zp00.dat file). Python is
preferred/recommended. Your function should take the filename as an
argument, as well as a list of requested quantities; implement a
default list of metallicity, age, effective temperature, luminosity,
IMF integral, and evolutionary stage. Optionally, request a single
age. The requested quantities should be returned in a structure. Your
code should have comments, and it should be formatted nicely! Check in
the module in an isochrones subdirectory (which you can include in
your PYTHONPATH). Use the module to retrieve an an isochrone of age 1
Gyr, and write it out using formatted output; place the output file in
the q22 subdirectory.

----------

Created 'practice.dat' using:
]$  grep -v '#' > practice.dat
to practice on. Once module is working correctly, then will work on
reading in the file in a way that ignores comments.

10/15/15
copied jon''s isochrone.py as an example. Haven''t written it myself yet.

11/04/15
Got rid of practice files.
Wrote own module, which seems to be working! Only issue right now is
creating my PYTHONPATH for the isochrones sub-directory, which isn't
working. Everything is in the current directory at the moment, and
I'll have to copy my module into all future directories until I
figure out how to set up the PYTHONPATH correctly. Used a simple write
to file; not sure how we were supposed to format this, or if this is
okay, since it looks pretty nice.

