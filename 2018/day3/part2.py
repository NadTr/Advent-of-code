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
    file[i] = [claim_id, [int(edges[0]), int(edges[1])],  [int(fabric[0]), int(fabric[1])]]

for claim in file:
    for x in range(claim[1][1], claim[1][1] + claim[2][1]):
        for y in range(claim[1][0], claim[1][0] + claim[2][0]):
            if area[x][y] == ".":
                area[x][y] = "#"
            else:
                area[x][y] = "X"

def is_claim_correct(claim):
    for x in range(claim[1][1], claim[1][1] + claim[2][1]):
        for y in range(claim[1][0], claim[1][0] + claim[2][0]):
            if area[x][y] == "#":
                continue
            else:
                return False
    return True

for claim in file:
    if is_claim_correct(claim):
        correct_claim = claim[0]

print("The ID of the only claim that doesn't overlap is", correct_claim)