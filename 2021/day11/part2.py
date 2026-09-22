from pathlib import Path
import numpy
print("advent of code 2021 day 11")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    grid = f.read().splitlines()
    for i in range(len(grid)):
            grid[i] = list(grid[i])
            for j in range(len(grid[i])):
                grid[i][j] = int(grid[i][j])

def show_grid():
     print("-------------------------")
     for line in grid:
          print(line)

def add_step():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += 1

def flash(x,y):
    neighbors_x = range(max(0, x - 1), min(x + 2, len(grid)))
    neighbors_y = range(max(0, y - 1), min(y + 2, len(grid[0])))
    for nx in neighbors_x:
        for ny in neighbors_y:
            if grid[nx][ny] not in [0, 10]:
                grid[nx][ny] += 1
    grid[x][y] = 0
           

# show_grid()
step = synchro_step = 0
while synchro_step == 0:
    step += 1
    add_step()
    while any(10 in line for line in grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 10:
                    flash(i, j)
    # show_grid()
    # print(numpy.flatnonzero(grid))
    # print(len(numpy.flatnonzero(grid)))
    if len(numpy.flatnonzero(grid)) == 0:
        synchro_step = step


print("The first step during which all octopuses flash is ",  synchro_step)