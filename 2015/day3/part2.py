from pathlib import Path
print("advent of code 2015 day 3")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read()

start_house_santa = [0,0]
start_house_robo = [0,0]
houses_visited = [start_house_santa]
directions = {
    "^": [0,1],
    ">": [1,0],
    "v": [0,-1],
    "<": [-1,0]
}

def next_house_to_visit(step, start_house):
    x = start_house[0] + directions[step][0]
    y = start_house[1] + directions[step][1]
    return [x,y]

for step in range(len(file)):
    if step %2 == 0:
        next_house = next_house_to_visit(file[step], start_house_santa)
        start_house_santa = next_house

    else:
        next_house = next_house_to_visit(file[step], start_house_robo)
        start_house_robo = next_house

    if(next_house not in houses_visited):
        houses_visited += [next_house]


print("The number houses that get presents is ", len(houses_visited))