from pathlib import Path
from collections import defaultdict
print("advent of code 2016 day 12")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

registers = defaultdict(int)
registers["c"] = 1

for line in range(len(file)):
    file[line] = file[line].split()

line = 0

while line < len(file):
    # print(registers)
    instructions = file[line]
    # print(instructions)
    if instructions[0] == "cpy":
        if instructions[1].isdigit():
            registers[instructions[2]] = int(instructions[1])
        else:
            registers[instructions[2]] = registers[instructions[1]]
    elif instructions[0] == "inc":
        registers[instructions[1]] += 1
    elif instructions[0] == "dec":
        registers[instructions[1]] -= 1
    elif instructions[0] == "jnz":
        if instructions[1] != "0" if instructions[1].isdigit() else registers[instructions[1]]!= 0 :
            line += int(instructions[2])
            continue
    line += 1
    # print(registers)


value_of_a = registers["a"]

print("The value in register a is ", value_of_a)