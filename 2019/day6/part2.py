from pathlib import Path
print("advent of code 2019 day 6")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

orbits = {}
for i in range(len(file)):
    object, orbit =  file[i].split(")")
    orbits.update({orbit:object})

orbit_you = orbits["YOU"]
orbit_san = orbits["SAN"]
steps_from_you = [orbit_you]
steps_from_san = [orbit_san]
link_not_found = True

while link_not_found:
    if orbit_you in orbits:
        orbit_you = orbits[orbit_you]
    if orbit_san in orbits:
        orbit_san = orbits[orbit_san]    
    if orbit_you not in steps_from_san:
        steps_from_you += [orbit_you]
    if orbit_san not in steps_from_you:
        steps_from_san += [orbit_san]
    if orbit_you in steps_from_san or orbit_san in steps_from_you:  
        link_not_found = False
        if orbit_you in steps_from_san:
            link = orbit_you
        else:
            link = orbit_san


total_transfers = 0
orbit_you = orbits["YOU"]
orbit_san = orbits["SAN"]
while orbit_you != link:
    orbit_you = orbits[orbit_you]
    total_transfers += 1

while orbit_san != link:
    orbit_san = orbits[orbit_san]
    total_transfers += 1

print("The total number of direct and indirect orbits is", total_transfers)