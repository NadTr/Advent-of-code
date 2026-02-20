from pathlib import Path
print("advent of code 2024 day 10")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:       
    file = f.read().splitlines()

total_trail_result = 0

def find_trail(start):
    trail_ends = []
    def find_next_step(step, position):
        # print(step, position)
        nonlocal trail_ends
        if step == 9:
            # print("found a nine", position, total_trail_result)
            str_position = str(position[0]) + "-" + str(position[1])
            if str_position not in trail_ends:
                trail_ends += [str_position]
            # total_trail_result += 1
            return
        else:
            next_step = step + 1
            if position[0] > 0:
                if file[position[0] -1][position[1]] == next_step:
                    find_next_step(next_step,(position[0] -1, position[1]))
            if position[0] < len(file) - 1:
                if file[position[0] + 1][position[1]] == next_step:
                    find_next_step(next_step,(position[0] + 1, position[1]))
            if position[1] > 0:
                if file[position[0]][position[1] - 1] == next_step:
                    find_next_step(next_step,(position[0], position[1] - 1))
            if position[1] < len(file[0]) - 1:
                if file[position[0]][position[1] + 1] == next_step:
                    find_next_step(next_step,(position[0], position[1] + 1))            
            return

    find_next_step(0, start)
    # print(trail_ends)
    return len(trail_ends)


for line in range(len(file)):
    file[line] = list(file[line])
    for step in range(len(file[line])):
        file[line][step] = int(file[line][step])

# print(file)

for line in range(len(file)):
    for step in range(len(file[line])):
        if file[line][step] == 0:
            local_trail_score = find_trail((line, step))
            # print("starting point", line, step, "score ", local_trail_score)
            total_trail_result += local_trail_score


# total_trail_result += 1 
        
print("The total number of full trails is ", total_trail_result)
