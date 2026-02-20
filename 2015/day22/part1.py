from pathlib import Path
print("advent of code 2015 day 22")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:    
    file = f.read().splitlines()

registers = {"a":0,"b":0}

for line in range(len(file)):
    file[line] = file[line].split()

index = 0
while index < len(file):
    line = file[index]
    if line[0]== "hlf":
        registers[line[1]] /= 2
        index += 1
    elif line[0]== "tpl":
        registers[line[1]] *= 3
        index += 1
    elif line[0]== "inc":
        registers[line[1]] += 1
        index += 1

    elif line[0]== "jmp":
        index += int(line[1])
    elif line[0]== "jie":
        if registers[line[1][0]]%2 == 0:
            index += int(line[2])
        else: index += 1
    elif line[0]== "jio":
        if registers[line[1][0]] == 1:
            index += int(line[2])
        else: index += 1

print("The the value in register b at the end is ", registers["b"])