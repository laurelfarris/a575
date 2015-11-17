Homework #10

Instructions:

Accomplish the following tasks using a single input command line, putting the
output in a separate file for each task. Put the input commands into a file so
that you could edit/rerun it, and have a record of what you did. Check in
input and output.

    Provide a sorted list of how much disk space individual users are taking
up on /home/hyades, sorted such that the bigger users are at the top of the
list. If your last name starts with an "odd-numbered" letter, do this for
users with "odd-numbered" last names (aceg...), otherwise do "even-numbered"
(bdfh...) last names. Note that you may have some trouble with permissions on
some files, so you won't be able to count those; however, note that the error
messages that the Unix commands create are directed to stderr, so if you
redirect stdout using '>', the error messages will still go to the terminal
and not to your output, so you should still be able to sort it.

    Create a list of the ten largest files (that you have permission to see),
sorted by size, on /home/hyades. Do the same for both user partitions of the
disk on your computer.

---------------------------------------------------------------------------

Results:

part 1: 
 Sorts all users (preceeded by /home/hyades) by descending
  disk-usage order. Still need to remove names that start
  every other letter... otherwise finished.

part 2:
du -aS still seems to be listing subdirectories at the end of each tree...
otherwise seems to work.
