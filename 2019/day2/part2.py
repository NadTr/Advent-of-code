from pathlib import Path
import numpy as np
print("advent of code 2019 day 2")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    initial_file = f.read().split(",")

for i in range(len(initial_file)):
    initial_file[i] = int(initial_file[i])

def add_numbers(numbers):
    return numbers[0] + numbers[1]

def multiply_numbers(numbers):
    return numbers[0] * numbers[1]

def execute_program(file):
    index = 0
    while True:
        step = file[index]
        if step == 99:
            return file[0]
        if step == 1:
            file[file[index + 3]] = add_numbers((file[file[index + 1]], file[file[index + 2]]))
        if step == 2:
            file[file[index + 3]] = multiply_numbers((file[file[index + 1]],file[file[index + 2]]))
        index += 4


def try_inputs():
    for noun in range(99):
        for verb in range(99):
            file = initial_file[:]
            file[1] = noun
            file[2] = verb
            output = execute_program(file)
            if output == 19690720:
                return noun*100 + verb
        
result = try_inputs()

print("The value is left at position 0 after the program halts is", result)