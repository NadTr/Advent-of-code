from pathlib import Path
print("advent of code 2018 day 7")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
     file = f.read().splitlines()

step_before = {}

for line in file:
    steps = line.split(" must be finished before step ")
    steps = [steps[0][-1], steps[1][0]]
    if steps[0] in step_before:
        step_before[steps[0]] += [steps[1]]
    else:
        step_before.update({steps[0]:[steps[1]]})

def find_first_step():
    should_be_waiting =[]
    for key in step_before:
        should_be_waiting += step_before[key]

    for key in step_before:
        if key in should_be_waiting:
            continue
        else: return key

step_before = dict(sorted(step_before.items()))
number_of_steps = len(step_before)
ordered = ""

for i in range(number_of_steps):
    letter = find_first_step()
    ordered += letter
    if i < number_of_steps -1:
        step_before.pop(letter)
    else:
        ordered += step_before[letter][0]

print("The order should the steps be completed in is", ordered)