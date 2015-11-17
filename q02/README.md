# a575hw

2. timelag.pro and correlation.pro

These were used for my summer project with James. timelag.pro was already 
written and, given two pixels from a data cube as an argument, calculates 
the cross-correlation between the two at certain timesteps. It is called
by correlation.pro, a separate code that I wrote to cycle through every 
pair of pixels in the data cube (with no repeats) and use timestep.pro to 
calculate the cross-correlation for each pair. The purpose of this project
is to search for structure at the predicted meso-granulation scale.
