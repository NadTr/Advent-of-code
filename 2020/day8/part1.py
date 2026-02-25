from pathlib import Path
print("advent of code 2020 day 8")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

for line in range(len(file)):
    instr, numb = file[line].split()
    file[line] = (instr , int(numb))

def execute_instr():
    index = 0
    accumulator = 0
    instr_already_done = set()
    while index not in instr_already_done:
        instr_already_done.update({index})
        if file[index][0] == "nop":
            index += 1
        elif file[index][0] == "acc":
            accumulator += file[index][1]
            index += 1
        elif file[index][0] == "jmp":
            index += file[index][1]
    return accumulator


result = execute_instr()

print("The value is in the accumulator before any instruction is executed a second time is", result)