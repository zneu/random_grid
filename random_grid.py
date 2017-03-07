# Generates and saves a random integer ASCII grid based on a user-specified size and range. The use story is as follows:
# 1. The user specifies the number of columns and rows for the raster to be generated (e.g., 4 cols and 5 rows).
# 2. Then, the user specifies the range and step of values to pool from when populating the grid values (e.g., from 2 to 8 with step of 2 which results in the following set of integers: 2, 4, 6, 8; see next step).
# 3. Based on the input, the system generates a 2-dimensional array of a given size and then populates it with values randomly (!) selected from the pool of eligible integers (as described above; see figure 2 for an illustration).
# 4. The array is saved to a text file (similar to the ASCII grid file format, mimicking the formatting in the ASCII grid file body--but without the ASCII grid header).

import random

def show_help():
    pass

def user_input():
    print("Please give number of columns and number of rows")
    try:
        columns = int(input("# columns > "))
        rows = int(input("# rows > "))
    except ValueError:
        print("Please, try again!")
        quit()

    print("Please give range of numbers to be generated (e.g. (0, 10))")
    try:
        x = int(input("First number > "))
        y = int(input("Second number> "))
    except ValueError:
        print("Please, try again!")
        quit()

    print("Please provide a step (e.g. if you provided (2, 8) with a step 2 you would get the following integers: 2, 4, 6, 8)")
    try:
        step = int(input("> "))
        if step == 0:
            step = 1
        else:
            pass
    except ValueError:
        print("Please, try again!")
        quit()

    return rows, columns, x, y, step

def grid(rows, columns, x, y, step=1):
    grid = []
    count = 0
    while rows > 0:
        grid.append([])
        column_count = columns
        while column_count > 0:
            grid[count].append(random.randrange(x, y, step))
            column_count -= 1
        count += 1
        rows -= 1
    return grid

def create_file(grid):
    f = open("grid.txt", "w+")
    for row in grid:
        for number in row:
            f.write(" " + str(number) + " ")
        f.write("\n")
    f.close()

rows, columns, x, y, step = user_input()
y += 1
grid = grid(rows, columns, x, y, step)
print("Creating your grid")
create_file(grid)
print("See grid.txt")
