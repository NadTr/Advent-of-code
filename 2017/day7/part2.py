print("advent of code 2017 day 7")

with open('./input.txt') as f:
    file = f.read().splitlines()

program_weigths = {}
branch_weigths = {}
tower = {}

for i in range(len(file)):
    line = file[i]
    if "->" in line:
        line = line.split(" -> ")
        program_key = line[0].split()
        tower.update({program_key[0] : line[1].split(", ")})

    else: 
        program_key = line.split()
    program_weigths.update({program_key[0] : int(program_key[1][1:-1])})

def branch_weigth(branch):
    weigth =  program_weigths[branch] 
    if branch in tower:
        for key in tower[branch]:
            weigth += branch_weigth(key)
    branch_weigths[branch] = weigth
    return weigth

def find_unbalanced(program):
    weigth = 0
    index_weigth = 0
    other_weigth = weigth
    index_other_weigth = 0

    for key in tower[program]:
        if weigth == 0:
            weigth = branch_weigths[key]
            index_weigth = key
            other_weigth = weigth
        elif branch_weigths[key] == weigth:
            if other_weigth != weigth:
                return index_other_weigth, abs(weigth - other_weigth)

        elif branch_weigths[key] == other_weigth:
            return index_weigth, abs(weigth - other_weigth)
        else:
            other_weigth = branch_weigths[key]
            index_other_weigth = key
    if abs(weigth - other_weigth) == 0:
        return program, abs(weigth - other_weigth)
    else:
        return index_other_weigth, abs(weigth - other_weigth)


bottom_program = "qibuqqg" #result part 1
# bottom_program = "tknk" #result example
branch_weigth(bottom_program)
old_balance = 1
is_balanced = False

while(not is_balanced):
    (new_program, balance) = find_unbalanced(bottom_program)
    is_balanced = balance == 0
    if is_balanced:
        balanced_weigth = program_weigths[bottom_program]- old_balance

    else: 
        bottom_program = new_program
        old_balance = balance

print("The weigth of the unbalanced program should be", balanced_weigth)
