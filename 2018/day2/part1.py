from pathlib import Path
print("advent of code 2018 day 2")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
     file = f.read().splitlines()

number_of_double = 0
number_of_triple = 0

for box_id in file:
    double = 0
    triple = 0
    box_id = list(box_id)
    while box_id != []:
        letter = box_id[0]
        count = box_id.count(letter)
        if count == 2 : double += 1
        elif count == 3 : triple += 1
        box_id = list(filter((letter).__ne__, box_id))

    number_of_double += 1 if double > 0 else 0
    number_of_triple += 1 if triple > 0 else 0

checksum = number_of_double * number_of_triple

print("The checksum for your list of box IDs is", checksum)