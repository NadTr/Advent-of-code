from pathlib import Path
import numpy as np, re
print("advent of code 2018 day 3")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
     file = f.read().splitlines()

length = 1000
area = np.full(shape=(length, length),fill_value=".")
more_than_one = 0

for i in range(len(file)):
    claim_id, infos = file[i].split(" @ ")
    edges, fabric = infos.split(":")
    edges = re.findall(r'\d+', edges)
    fabric = re.findall(r'\d+', fabric)
    for x in range(int(edges[1]), int(edges[1])+ int(fabric[1])):
        for y in range(int(edges[0]), int(edges[0]) + int(fabric[0])):
            if area[x][y] == ".":
                area[x][y] = "#"
            else:
                area[x][y] = "X"

for x in range(len(area)):
    for y in range(len(area[0])):
        if area[x][y] == "X":
            more_than_one += 1

print("The number of square inches of fabric are within two or more claims is", more_than_one)