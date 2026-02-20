from pathlib import Path
print("advent of code 2024 day 10")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:       
    file = f.read().splitlines()

total_trail_result = 0

def find_next_step(step, position):
    global total_trail_result
    if step == 9:
        total_trail_result += 1
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


for line in range(len(file)):
    file[line] = list(file[line])
    for step in range(len(file[line])):
        file[line][step] = int(file[line][step])

for line in range(len(file)):
    for step in range(len(file[line])):
        if file[line][step] == 0:
            find_next_step(0, (line, step))
        
print("The total number of full trails is ", total_trail_result)
