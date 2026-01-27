import re
print("advent of code 2023 day 1")

global sum_of_calibrations
sum_of_calibrations = 0

with open('./day1.txt') as f:
    file = f.read().splitlines()

def change_letters_to_number(line):  
    changed_line = line
    changed_line = re.sub("zero", 'ze0ro',changed_line)
    changed_line = re.sub("one", 'o1ne',changed_line)
    changed_line = re.sub("two", 't2wo',changed_line)
    changed_line = re.sub("three", 'th3ree',changed_line)
    changed_line = re.sub("four", 'fo4ur',changed_line)
    changed_line = re.sub("five", 'fi5ve',changed_line)
    changed_line = re.sub("six", 's6ix',changed_line)
    changed_line = re.sub("seven", 'se7ven',changed_line)
    changed_line = re.sub("eight", 'eig8ht',changed_line)
    changed_line = re.sub("nine", 'ni9ne',changed_line)
    # print(changed_line)
    return changed_line


def calculate_calibration(line):
    result = ""
    # print(line)
    for i in range(len(line)):
        if line[i].isdigit():
            result += line[i]
            break
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            result += line[i]
            break
    # print(result)
    return int(result)

for line in file:
    line = change_letters_to_number(line)
    line = list(line)
    sum_of_calibrations += calculate_calibration(line)




print("The sum of all of the calibration values is " + str(sum_of_calibrations))
