from pathlib import Path
from itertools import permutations
print("advent of code 2020 day 1")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()
    for ind in range(len(file)):
        file[ind] = int(file[ind])

possibles_results = permutations(file, 2)

for possibles_result in possibles_results:
    if possibles_result[0] + possibles_result[1] == 2020:
         result = possibles_result[0] * possibles_result[1]

print("The rsum of the fuel requirements for all of the modules", result)