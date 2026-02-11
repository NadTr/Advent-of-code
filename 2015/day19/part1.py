from pathlib import Path
print("advent of code 2015 day 19")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
      file = f.read().splitlines()

letter_replacements = {}
changed_molecules = []
initial_molecule = file[-1]
print(initial_molecule)

for i in range(len(file)-2):
    line = file[i].split(" => ")
    if line[0] in letter_replacements:
        letter_replacements[line[0]] += [line[1]]
    else:
        letter_replacements.update({line[0]: [line[1]]}) 

for i in range(len(initial_molecule)):
    if initial_molecule[i] in letter_replacements:
        replacements = letter_replacements[initial_molecule[i]]
        for r in replacements:
            new_molecule = initial_molecule[0:i] + r + initial_molecule[i+1:]
            # print(r, replacements,  i, new_molecule)
            if new_molecule not in changed_molecules:
                changed_molecules += [new_molecule]
    if i< len(initial_molecule) -1 and  initial_molecule[i:i+2] in letter_replacements:
        replacements = letter_replacements[initial_molecule[i:i+2]]
        for r in replacements:
            new_molecule = initial_molecule[0:i] + r + initial_molecule[i+2:]
            # print(r, replacements,i ,new_molecule)
            if new_molecule not in changed_molecules:
                changed_molecules += [new_molecule]
        
print("The number of distinct molecules can be created is ", len(changed_molecules))
