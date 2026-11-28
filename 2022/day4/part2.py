from pathlib import Path
print("advent of code 2022 day 4")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()


score =0
for line in file:
    elf1, elf2 = line.split(',')
    elf1 = list(map(int, elf1.split('-')))
    elf2 = list(map(int, elf2.split('-')))
    if (elf2[0] <= elf1[0] <= elf2[1] or elf1[0] <= elf2[0] <= elf1[1]):
        score += 1

print("The number of assignment pairs does the ranges overlap is", score )