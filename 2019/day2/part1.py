from pathlib import Path
print("advent of code 2019 day 2")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().split(",")

for i in range(len(file)):
    file[i] = int(file[i])

file[1] = 12
file[2] = 2

def add_numbers(numbers):
    return numbers[0] + numbers[1]

def multiply_numbers(numbers):
    return numbers[0] * numbers[1]

index = 0
not_ninetynine = True 
while not_ninetynine:
    step = file[index]
    if step == 99:
        not_ninetynine = False
    if step == 1:
        file[file[index + 3]] = add_numbers((file[file[index + 1]], file[file[index + 2]]))
    if step == 2:
        file[file[index + 3]] = multiply_numbers((file[file[index + 1]],file[file[index + 2]]))
    index += 4

print("The value is left at position 0 after the program halts is", file[0])