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

res = 0
for line in range(preamble_length, len(file)):
    if not is_number_valid(line):
        index, res = line, file[line]

for i in range(1, index):
    for j in range(len(file) - i):
        temp_list = file[j:j+i]
        if sum(temp_list) == res:
            result =  max(temp_list) + min(temp_list)

print("The first number that does not have this property is", result)