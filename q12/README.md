Homework #12

The SDSS/APOGEE team creates large libraries of synthetic spectra for a region
in the near-IR. To do so requires a list of all of the atomic/molecular lines
in the region: you can find a current list in
/home/apogee/speclib/linelists/linelist.20150714

    In your working directory (q12), create a symbolic link to this file
    Write a one line command to determine the number of atomic/molecular lines
in the file, remembering that you have to ignore the lines that are comments.
    Create an abbreviated version of this list by using a one-line awk command
to select only every hundredth line, but preserve all of the header lines.
    The format of this information needs to be modified for input into various
spectral synthesis programs. One such program is Turbospectrum, and the script
turboscript, along with the awk program file turbo_atoms.awk is used to do the
trick. Go through these files, trying to understand what they do, and annotate
them with comments giving your line-by-line description. Verify it by running
it on your abbreviated line list.
    Check in the input command file for the first three items, as well as the
annotated scripts.



NOTES:

The link was created and the first two tasks accomplished... still need to
figure out the third one.


