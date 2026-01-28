print("advent of code 2023 day 8")

global number_of_steps
number_of_steps = 0

with open('./day8.txt') as f:
    file = f.read().splitlines()

steps = list(file[0])
map = {}
for i in range(2,len(file)):
    line = file[i].split("=")
    values = line[1].split(",")
    values[0] = ''.join(filter(str.isalpha, values[0]))
    values[1] = ''.join(filter(str.isalpha, values[1]))
    map[''.join(filter(str.isalpha, line[0]))] = values


def follow_the_way(steps, map):
    global number_of_steps
    current_step = 'AAA'
    while(current_step != 'ZZZ'):
        for direction in steps:
            current_step = map[current_step][0 if direction == 'L' else 1]
            # print(direction, "  " , current_step)
            number_of_steps += 1
            if current_step == 'ZZZ':
                break

follow_the_way(steps, map)
       
print("The number of steps are required to reach ZZZ is " + str(number_of_steps))
