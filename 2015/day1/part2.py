from pathlib import Path
print("advent of code 2015 day 1")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read()

level = 0

for step in range(len(file)):
    if file[step] == "(":
        level += 1
    elif file[step] == ")":
        level -= 1
    if(level == -1):
        print("the first time in the level -1 is on step", step + 1)
        break