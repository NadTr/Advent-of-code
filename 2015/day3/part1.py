print("advent of code 2015 day 3")

with open('./input.txt') as f:
    file = f.read()

start_house = [0,0]
houses_visited = [start_house]
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
for step in file:
    next_house = next_house_to_visit(step, start_house)
    if(next_house not in houses_visited):
        houses_visited += [next_house]
    start_house = next_house


print("The number houses that get presents is ", len(houses_visited))