from pathlib import Path
from itertools import permutations 
print("advent of code 2020 day 9")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

file = list(map(int, file))
preamble_length = 25

def is_number_valid(index):
    preamble = file[index - preamble_length : index]
    possibles_results = permutations(preamble, 2)
    for result in possibles_results:
        if sum(result) == file[index]:
            return True
    return False

result = 0
for line in range(preamble_length, len(file)):
    if not is_number_valid(line):
        result = file[line]

print("The first number that does not have this property is", result)