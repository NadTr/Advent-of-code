from pathlib import Path
print("advent of code 2022 day 1")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

elfs= {}
elf = 1
calories = 0

for line in file:
    if line.isdigit():
        calories += int(line)
    else:
        elfs.update({elf : calories})
        elf += 1
        calories = 0

sorted_calories = sorted(elfs.values(), reverse=True)

print("The maximum total Calories carried by one elf is", sum(sorted_calories[:3]))