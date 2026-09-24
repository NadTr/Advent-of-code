from pathlib import Path
print("advent of code 2021 day 5")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

for i in range(len(file)):
    line = []
    for l in file[i].split(' -> '):
        line.append([int(x) for x in l.split(',')])
    file[i] = line

def draw_line(x1, y1, x2, y2):
    if x1 == x2:
        (y1, y2) = (y1, y2) if y1 < y2 else (y2, y1)
        for i in range(y1, y2 + 1):
            diagram[i][x1] += 1
    else:
        (x1, x2) = (x1, x2) if x1 < x2 else (x2, x1)
        for j in range(x1, x2 + 1):
            diagram[y1][j] += 1

size = 1000
diagram = [[ 0 for _ in range(size) ] for _ in range(size)]

for line in file:
    [[x1,y1], [x2,y2]] = line
    if x1 == x2 or y1 == y2:
        draw_line(x1, y1, x2, y2)

score = 0

for i in diagram:
    for j in i:
        score += 0 if j <= 1 else 1

print("The number of points where at least two lines overlap is ", score )