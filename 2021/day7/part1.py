from pathlib import Path
print("advent of code 2021 day 7")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().split(',')

file = list(map(int, file))
file.sort()
target_pos = file[len(file)//2]
min_fuel = sum(abs(x - target_pos) for x in file)

print("The least fuel possible to reach the same horizontal position  is ", min_fuel)