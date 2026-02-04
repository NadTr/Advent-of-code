print("advent of code 2016 day 1")

with open('./input.txt') as f:
    file = f.read().split(", ")

directions = {
    "up":[0, -1],
    "right":[1, 0],
    "down":[0, 1],
    "left":[-1, 0]
}

def change_direction(dir, turn):
    if dir == "up":
        return "right" if turn == "R" else "left"
    elif dir == "right":
        return "down" if turn == "R" else "up"
    elif dir == "down":
        return "left" if turn == "R" else "right"
    elif dir == "left":
        return "up" if turn == "R" else "down"
    


def find_position_visited_twice(file):
    dir = "up"
    positions_visited = []
    position = [0, 0]
    for step in file:
        dir = change_direction(dir,step[0])
        for i in range(int(step[1:])):
            position[0] += directions[dir][0]
            position[1] += directions[dir][1]
            # print(position)
            if position in positions_visited:
                # print("The first position visited twice is ", position, "at a distance of ", abs(position[0])+abs(position[1]))            
                return position
            else:
                positions_visited += [[position[0], position[1]]]


position = find_position_visited_twice(file)
print("The first position visited twice is ", position, "at a distance of ", abs(position[0])+abs(position[1]))            
