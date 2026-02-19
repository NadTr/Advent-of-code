from pathlib import Path
import re
print("advent of code 2018 day 12")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
     file = f.read()

initial_state, instructions = file.split("\n\n")
initial_state = re.sub('initial state: ', '', initial_state)
generations = 50000000000
current_state = '...' + initial_state + '...'
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

def number_of_plants(state):
     result = 0
     for i in range(len(state)):
          if current_state[i]  == '#':
               result += i-3
     return result

def number_of_plants_after_year_96(state_99, year_after_99):
     # print(year_after_99, "*", state_99 )
     result = 0
     for i in range(len(state_99)):
          if state_99[i]  == '#':
               result += i + year_after_99
     return result
 
index_99 = current_state.index("#") - 3
state_99 = []
current_plants = number_of_plants(current_state)
for year in range(generations):
     current_state = another_generation(current_state)
     if year == 99:
          index_99 = current_state.index("#")
          state_99 = current_state[ index_99: index_99 + len(initial_state) + 20]
          break

result = number_of_plants_after_year_96(state_99,  generations  + (index_99 - 100) -3 )

# other_result = number_of_plants(current_state)
print("The sum of the numbers of all pots which contain a plant is", result)