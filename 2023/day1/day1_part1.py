print("advent of code 2023 day 1")

global sum_of_calibrations
sum_of_calibrations = 0

with open('./day1.txt') as f:
    file = f.read().splitlines()

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
    line = list(line)
    sum_of_calibrations += calculate_calibration(line)




print("The sum of all of the calibration values is " + str(sum_of_calibrations))
