print("advent of code 2015 day 2")

with open('./input.txt') as f:
    file = f.read().splitlines()

result = 0

def ruban_length_needed(l, w, h):
    sorted_length = sorted([l, w, h])
    length = 2*(sorted_length[0]+sorted_length[1])
    bow = l*w*h
    # print("length ", length, "  bow ", bow)
    return length + bow

for line in file:
    line = line.split("x")
    result += ruban_length_needed(int(line[0]), int(line[1]), int(line[2]))
    
print("The number of square needed to wrap presents is ", result)