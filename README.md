# Random Grid
Generates and saves a random integer ASCII grid based on a user-specified size and range. The use story is as follows:
* The user specifies the number of columns and rows for the raster to be generated (e.g., 4 cols and 5 rows).
* Then, the user specifies the range and step of values to pool from when populating the grid values (e.g., from 2 to 8 with step of 2 which results in the following set of integers: 2, 4, 6, 8; see next step).
* Based on the input, the system generates a 2-dimensional array of a given size and then populates it with values randomly (!) selected from the pool of eligible integers (as described above; see figure 2 for an illustration).
* The array is saved to a text file (similar to the ASCII grid file format, mimicking the formatting in the ASCII grid file body--but without the ASCII grid header).

View a link to the [repl.it](https://repl.it/GJun/4)
