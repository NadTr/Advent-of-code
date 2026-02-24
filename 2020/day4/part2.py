from pathlib import Path
import re
print("advent of code 2020 day 4")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().split("\n\n")

field_names = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
valids_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
valid_passports = 0

for i in range(len(file)):
    items = re.findall(r"[a-z]+\:[^\s]+", file[i])
    line = {}
    for item in range(len(items)):
        field_name, field =items[item].split(":")
        line.update({field_name : field})
    file[i] = line

def is_line_valid(field_name, data):
    if field_name == "byr":
        if (int(data) >= 1920 and int(data) <= 2002):
            return True
    elif field_name == "iyr":
        if (int(data) >= 2010 and int(data) <= 2020):
            return True
    elif field_name == "eyr":
        if (int(data) >= 2020 and int(data) <= 2030):
            return True
    elif field_name == "hgt":
        if data[-2:] =="cm":
            if int(data[:-2]) >= 150 and int(data[:-2]) <= 193:
                return True
        elif data[-2:] =="in":
            if int(data[:-2]) >= 59 and int(data[:-2]) <= 76:
                return True
    elif field_name == "hcl":
        if len(data) == 7 and data[0] == "#" and data[1:].isalnum():
            return True
    elif field_name == "ecl":
        if data in valids_ecl:
            return True
    elif field_name == "pid":
        if len(data) == 9 and data.isdigit():
            return True
    return False
    

def is_passport_valid(line):
    if len(line) >= len(field_names):
        for f in range(len(field_names)):
            if field_names[f] in line and is_line_valid(field_names[f],line[field_names[f]]):
                if f >= len(field_names) -1:
                    return True
            else:
                return False
    return False

               
for line in file:
    if is_passport_valid(line):
        valid_passports += 1

print("The number of valid passports is", valid_passports)