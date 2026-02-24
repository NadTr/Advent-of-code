from pathlib import Path
print("advent of code 2020 day 3")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
all_trees_encountered = []
for slope in slopes:
    trees_encountered = 0
    for line in range(1, len(file), slope[0]):
        x = line * slope[1] % len(file[0])
        if file[line][x] == "#":
            trees_encountered += 1   
    all_trees_encountered += [trees_encountered]

result = 1
for number_of_trees in all_trees_encountered:
    result *= number_of_trees

print("The multiplication of trees encountered in each slope is", result)