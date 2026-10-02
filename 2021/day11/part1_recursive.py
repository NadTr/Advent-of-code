from pathlib import Path
print("advent of code 2021 day 11")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    grid = f.read().splitlines()
    for i in range(len(grid)):
            grid[i] = list(list(map(int, grid[i])))

flash_count = 0
flashed_this_step = set()

def show_grid():
     print("-------------------------")
     for line in grid:
          print(' '.join(str(x) for x in line))


def increase_energy(i, j):
    global flashed_this_step
    if (i, j) not in flashed_this_step:
        grid[i][j] += 1
        if grid[i][j] == 10:
            flash(i,j)


def flash(y,x):
    global flash_count
    global flashed_this_step
    flashed_this_step.add((y,x))
    flash_count += 1
    grid[y][x] = 0

    neighbors_y = range(max(0, y - 1), min(y + 2, len(grid)))
    neighbors_x = range(max(0, x - 1), min(x + 2, len(grid[0])))
    for ny in neighbors_y:
        for nx in neighbors_x:
            if (ny,nx) != (y, x):
                increase_energy(ny, nx)


# show_grid()
for step in range(100):
    flashed_this_step = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            increase_energy(i,j)

print("The number of flashes after 100 steps is ",  flash_count)