from pathlib import Path
import numpy as np, copy
print("advent of code 2020 day 8")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

for line in range(len(file)):
    instr, numb = file[line].split()
    file[line] = [instr , int(numb)]

def execute_instr(changed_file):
    index = 0
    accumulator = 0
    instr_already_done = set()
    while index not in instr_already_done and index < len(changed_file):
        instr_already_done.update({index})
        if changed_file[index][0] == "nop":
            index += 1
        elif changed_file[index][0] == "acc":
            accumulator += changed_file[index][1]
            index += 1
        elif changed_file[index][0] == "jmp":
            index += changed_file[index][1]
    return index not in instr_already_done, accumulator

index_nop = np.where(np.array(file) == "nop")[0]
index_jmp = np.where(np.array(file) == "jmp")[0]
index_to_change = [*index_nop , *index_jmp]

result = 0
for i in index_to_change:
    arranged_file = copy.deepcopy(file)
    arranged_file[i][0] = "nop" if arranged_file[i][0] =="jmp" else "jmp"
    to_the_end, value = execute_instr(arranged_file)
    if to_the_end:
        result = value
        break

print("The value is in the accumulator after the program terminates is", result)