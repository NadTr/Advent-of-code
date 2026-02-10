import string 
print("advent of code 2017 day 16")

with open('./input.txt') as f:
    file = f.read().split(",")

programs_order = list(string.ascii_lowercase[:16])

for line in file:
    action = line[0]
    if action == "s":
        index = len(programs_order) - int(line[1:])
        programs_order =  programs_order[index:] + programs_order[0: index]
    elif action == "x":
        programs_to_move = line[1:].split("/")
        prog_a = programs_order[int(programs_to_move[0])]
        prog_b = programs_order[int(programs_to_move[1])]
        programs_order[int(programs_to_move[0])] = prog_b
        programs_order[int(programs_to_move[1])] = prog_a
    else: #"p"
        programs_to_move = line[1:].split("/")
        index_a = programs_order.index(programs_to_move[0])
        index_b = programs_order.index(programs_to_move[1])
        programs_order[index_a] = programs_to_move[1]
        programs_order[index_b] = programs_to_move[0]
    # print(programs_order)

program_str = "".join(x for x in programs_order)

print("The order the programs standing after their dance is", program_str)