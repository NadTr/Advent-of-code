import string 
print("advent of code 2017 day 16")

with open('./input.txt') as f:
    file = f.read().split(",")

def one_dance(programs_order):
    programs_order = list(programs_order)
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
    return "".join(x for x in programs_order)

programs_order = string.ascii_lowercase[:16]
end_orders =[programs_order]

for i in range(1000000000):
    programs_order = one_dance(programs_order)
    if programs_order in end_orders:
        break
    else:
        end_orders += [programs_order]

index = 1000000000 % len(end_orders)

program_billion =end_orders[index]

print("The order the programs standing after their billion dance is", program_billion)