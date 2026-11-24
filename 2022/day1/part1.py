from pathlib import Path
print("advent of code 2022 day 1")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

elfs= {}
elf = 1
calories = 0
for i in file:
    if i.isdigit():
        calories += int(i)
    else:
        elfs.update({elf : calories})
        elf += 1
        calories = 0

print("The maximum total Calories carried by one elf is", max(elfs.values()))