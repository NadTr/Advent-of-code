from pathlib import Path
import re
print("advent of code 2020 day 4")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().split("\n\n")

# fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
valid_passports = 0

for line in file:
    line = re.findall(r"[a-z]+\:", line)
    for i in range(len(line)):
        line[i] = line[i][:3]
    if len(line) >= len(fields):
        for f in range(len(fields)):
            if fields[f] in line:
                if f >= len(fields) -1:
                    valid_passports += 1
            else:
                break

print("The number of valid passports is", valid_passports)