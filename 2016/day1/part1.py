from pathlib import Path
print("advent of code 2016 day 1")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
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
    

positon = [0, 0]
dir = "up"

for step in file:
    dir = change_direction(dir,step[0])
    positon[0] += int(step[1:]) * directions[dir][0]
    positon[1] += int(step[1:]) * directions[dir][1]
    print(positon)

    
print("The end position is ", positon, "at a distance of ", sum(positon))