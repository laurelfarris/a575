Instructions:
Plot some HR diagrams given a set of isochrones. Make a 2x2 panel of plots. On
the left panels plot effective temperature against surface gravity and
bolometric magnitude for isochrones of multiple metallicities, but a single age
of 1 Gyr; color code the points by metallicity. On the right panel, plot the
same but for a series of ages at a single metallicity (solar); color code the
points by age. Challenge: write an event handler that returns the mass of the
nearest point to a mouse click or a key press.

Progress:

11/01/15
Toying with the idea of making a separate module for plotting (have
one for a565), but not sure how to generalize hr diagram for things
like axis labels and scaling on third dimension, unless this could be
part of the function's input.

All four panels plotted and saved as 'hr\_diagram.png'. Should be the
right data... just need to narrow them down a single age/metallicity
and do the color-coding.

11/04/15
zp00.dat only has one metallicity, so I'm probably using the wrong
one. Color map isn't doing what I want it to either... other than
that, finished except for the event handler.

11/12/15
Need to read in proper isochrone file, but rewrote everything using axes
objects instead of plt.

