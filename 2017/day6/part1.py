print("advent of code 2017 day 6")

with open('./input.txt') as f:
    file = f.read().split()

for i in range(len(file)):
    file[i] = int(file[i])

def reallocation_routine(combination):
    new_combination = combination
    value_to_distribute = max(combination)
    index = combination.index(value_to_distribute)
    new_combination[index] = 0
    index = index + 1 if index < len(combination) else 0
    for i in range(index, value_to_distribute + index):
        new_combination[i%len(combination)] += 1
    return new_combination

cycle_length = 0
combinations = []
combination = file

while str(combination) not in combinations:
    combinations += [str(combination)]
    new_combination = reallocation_routine(combination)
    cycle_length += 1
    combination = new_combination

print("The length of a redistribution cycle is", cycle_length)