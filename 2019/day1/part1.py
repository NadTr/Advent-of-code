from pathlib import Path
print("advent of code 2019 day 1")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
     file = f.read().splitlines()

def get_fuel_requirement(mass):
    return int(mass)//3 - 2

total_fuel = 0
for mass in file:
    total_fuel += get_fuel_requirement(mass)

print("The rsum of the fuel requirements for all of the modules", total_fuel)