from pathlib import Path
print("advent of code 2021 day 2")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

position = [0, 0]
aim = 0

for i in range(len(file)):
    step = file[i].split()

    if step[0] =="forward":
        position[0] += int(step[1])
        position[1] += int(step[1])*aim
    else:
        if step[0] == "up":
            aim -= int(step[1])
        else:
            aim += int(step[1])

print("The multiplication of your final horizontal position by your final depth is",  position[0]* position[1])