print("advent of code 2017 day 5")

with open('./input.txt') as f:
    file = f.read().splitlines()

def new_index_line(index):
    line = file[index]
    file[index] = str(int(line) + 1 if int(line) < 3 else int(line) - 1)
    return (index + int(line))


number_of_steps = 0
line = 0
while line < len(file):
    line = new_index_line(line)
    number_of_steps += 1

print("The number of steps to reach the exit is", number_of_steps)