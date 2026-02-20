from pathlib import Path
import re
print("advent of code 2015 day 19")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
      file = f.read().splitlines()

letter_replacements = {}
initial_molecule = file[-1]
end_molecule = "e"

for i in range(len(file)-2):
    line = file[i].split(" => ")
    if line[0] in letter_replacements:
        letter_replacements[line[1]] += line[0]
    else:
        letter_replacements.update({line[1]: line[0]}) 

step = 0
molecule_not_found = True
molecule = initial_molecule

while (molecule_not_found):
    new_changed_molecules = []
    for replacement in letter_replacements:
        if replacement in molecule:
            molecule = re.sub(replacement, letter_replacements[replacement], molecule, count = 1)
            step += 1
        if molecule == end_molecule:
            molecule_not_found = False
            break
        
print("The number of step to create the molecule from e is", step)
