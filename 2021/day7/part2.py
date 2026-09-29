from pathlib import Path
print("advent of code 2021 day 7")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().split(',')

def fuel_cost(travel):
    return travel * (travel + 1) // 2

file = list(map(int, file))
file.sort()
median = round(sum(file)/len(file))
min_fuel = sum(fuel_cost(abs(x - median)) for x in file)

for target_pos in range(min(file), max(file)):
    cost = sum(fuel_cost(abs(x - target_pos)) for x in file)
    if not min_fuel or cost < min_fuel :
        min_fuel = cost

print("The least fuel possible to reach the same horizontal position  is ", min_fuel)