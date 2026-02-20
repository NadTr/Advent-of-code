from pathlib import Path
print("advent of code 2024 day 6")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:   
    file = f.read().splitlines()
    for line in range(len(file)):
        file[line] = list(file[line])
        for col in range(len(file[line])):
            if file[line][col] == "^":
                start_location = [line, col]

positions_used = 0
directions  = [[-1, 0], [0, 1], [1, 0], [0, -1]]
dir = 0
is_inside = True
location = start_location

while(is_inside):
    file[location[0]][location[1]] = "X"
    new_location = [location[0] + directions[dir][0] ,location[1] + directions[dir][1]]

    if (file[new_location[0]][new_location[1]] == "#"):
            dir = 0 if dir == 3 else dir + 1
            print("change direction ", dir)
    else:
        if(new_location[0] <= 0 or new_location[0] > len(file)-2 or new_location[1] <= 0 or new_location[1] > len(file[0])-2):
            file[new_location[0]][new_location[1]] = "X"
            is_inside = False
            print("out of bound", new_location)

        else:
            location = new_location

for line in range(len(file)):
    for col in range(len(file[line])):
        if file[line][col] == "X":
            positions_used += 1     

print("The total number of positions the guard stand in is  " + str(positions_used))
