from pathlib import Path
import re
print("advent of code 2018 day 12")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
     file = f.read()

initial_state, instructions = file.split("\n\n")

generations = 20
initial_state = '...' + re.sub('initial state: ', '', initial_state) + '...'
instructions = instructions.splitlines()
spreading_instructions = {}
for i in range(len(instructions)):
    config, result = instructions[i].split(" => ")
    spreading_instructions.update({config:result})

def another_generation(line):
     new_line = list(line)
     for i in range(len(line)):
          if i > 1 and i < len(line) -2:
               spread = line[i-2:i+3]
               if spread in spreading_instructions:
                    new_line[i] = spreading_instructions[spread]
               else:
                    new_line[i] = "."
          elif i >= len(line) -2:
               spread = line[i-2:]
               spread += '.'* (5-len(spread))
               if spread in spreading_instructions:
                    new_line[i] = spreading_instructions[spread]
                    new_line.append('.')
     return "".join(new_line)

for year in range(generations):
    initial_state = another_generation(initial_state)

result = 0
for i in range(len(initial_state)):
     if initial_state[i]  == '#':
          result += i-3

print("The sum of the numbers of all pots which contain a plant is", result)