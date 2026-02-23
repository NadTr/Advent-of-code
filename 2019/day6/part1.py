from pathlib import Path
print("advent of code 2019 day 6")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

orbits = {}
for i in range(len(file)):
    object, orbit =  file[i].split(")")
    orbits.update({orbit:object})

def find_orbits(key):
    orbits_number = 0
    if key in orbits:
        orbits_number += 1
        orbits_number += find_orbits(orbits[key])
    return orbits_number


total_orbits = 0
for key in orbits:
    total_orbits += find_orbits(key)

print("The total number of direct and indirect orbits is", total_orbits)