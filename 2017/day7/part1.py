print("advent of code 2017 day 7")

with open('./input.txt') as f:
    file = f.read().splitlines()

list_down = []
list_above = []

for line in file:
    if "->" in line:
        line = line.split(" -> ")
        program_name = line[0].split()
        list_down += [program_name[0]]
        list_above += line[1].split(", ")

for program in list_down:
    if program not in list_above:
        bottom_program = program

print("The  name of the bottom program is", bottom_program)