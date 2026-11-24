from pathlib import Path
import string
print("advent of code 2022 day 3")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

priorities = {letter: index + 1 for index, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase)}

score =0
for line in file:
    item_type = set()
    middle = len(line)//2
    for char in line[:middle]:
        if char in line[middle:]:
            item_type.add(char)

    for item in item_type:
        score += priorities[item]

print("The sum of the priorities of the item types that need rearrangement is", score )