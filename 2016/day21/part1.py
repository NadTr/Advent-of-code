from pathlib import Path
print("advent of code 2016 day 21")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

start_string = "efghdabc"
letters_order = list(start_string)

def swap(a,b):
    letter = letters_order[a]
    letters_order[a] = letters_order[b]
    letters_order[b] = letter


def move(start_position, end_position):
    global letters_order
    letter = letters_order[start_position]
    del letters_order[start_position]
    letters_order.insert(end_position, letter)


def reverse(start, end):
    reversed_part = letters_order[start:] if end >= len(letters_order) -1 else letters_order[start : end + 1] 
    reversed_part = reversed_part [::-1]
    for i in range(0, end - start + 1):
        letters_order[start + i] = reversed_part[i]


def rotate(direction, steps):
    global letters_order
    index = len(letters_order) - steps
    if direction == "right":
        letters_order =  letters_order[index:] + letters_order[0: index]
    else:
        letters_order =  letters_order[steps:] + letters_order[0: steps]


for line in file:
    line = line.split()
    action = line[0]
    if action == "swap":
        if line[1] == "position":
            swap(int(line[2]), int(line[-1]))
        else:
            swap(letters_order.index(line[2]), letters_order.index(line[-1]))
    elif action == "move":
        move( int(line[2]),  int(line[-1]))
    elif action == "reverse":
        reverse(int(line[2]), int(line[-1])) 
    else: #"rotate"
        if line[1] == "based":
            index =  letters_order.index(line[-1]) 
            rotate("right", index + 1 if index < 4 else index + 2)
        else:
            rotate(line[1], int(line[2]))

program_str = "".join(x for x in letters_order)

print("The the result of scrambling ", start_string," is", program_str)