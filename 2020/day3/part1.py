from pathlib import Path
print("advent of code 2020 day 3")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

slope = [1, 3]
trees_encountered = 0

for line in range(1, len(file)):
    x = line * slope[1] % len(file[0])
    if file[line][x] == "#":
        trees_encountered += 1    

print("The number of trees encountered is", trees_encountered)