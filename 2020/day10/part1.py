from pathlib import Path
# from itertools import permutations 
print("advent of code 2020 day 10")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

file = sorted(list(map(int, file)))

start = 0
numbers_of_one = 0
numbers_of_three = 1

line = 0
while line < len(file):
    if file[line] == start + 1:
        numbers_of_one += 1
    elif file[line] == start + 3:
        numbers_of_three += 1
    elif file[line] == start + 2 and line < len(file) -1 and  file[line] == start + 3:
        numbers_of_one += 1
        numbers_of_three += 1
        line += 1
    start = file[line]
    line += 1

result = numbers_of_one * numbers_of_three

print("The number of 1-jolt differences multiplied by the number of 3-jolt differences is", result)