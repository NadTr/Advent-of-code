from pathlib import Path
print("advent of code 2016 day 8")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

lit_pixel_count = 0
grid = [['.' for j in range(50)] for i in range(6)]

def draw_rect(x, y):
    for i in range(y):
        for j in range(x):
            grid[i][j] = '#'

def rotate(direction, target, steps):
    if direction == 'y':
        grid[target] = grid[target][-steps:] + grid[target][:-steps]
    else:
        col = []
        for i in range(len(grid)):
            col.append(grid[i][target])
        col = col[-steps:] + col[:-steps]
        for i in range(len(grid)):
            grid[i][target] = col[i]


for instruction in file:
    inst = instruction.split()
    if inst[0] == 'rect':
        x, y = inst[1].split('x')
        draw_rect(int(x), int(y))
    else:
        dir, target = inst[2].split('=')
        rotate(dir, int(target), int(inst[-1]))

for line in grid:
    lit_pixel_count += line.count('#')

print("The number of lit pixels is ", lit_pixel_count)