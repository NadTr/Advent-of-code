from pathlib import Path
print("advent of code 2019 day 1")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
     file = f.read().splitlines()

def get_fuel_requirement(mass):
    return mass//3 - 2

total_fuel = 0
for mass in file:
    fuel_mass = get_fuel_requirement(int(mass))
    total_fuel += fuel_mass
    while fuel_mass > 0:
        fuel_mass = get_fuel_requirement(fuel_mass)
        total_fuel += fuel_mass if fuel_mass > 0 else 0

print("The sum of the fuel requirements for all of the modules", total_fuel)