from pathlib import Path
import itertools
print("advent of code 2015 day 17")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
      file = f.read().splitlines()

working_combinations = 0
number_to_reach = 150
            
for i in range(len(file)):
    file[i] = int(file[i])

for i in range(len(file)):
    combinaisons = itertools.combinations(file,i)
    for combi in combinaisons:
         if sum(combi) == number_to_reach:
              working_combinations += 1
    if working_combinations > 0:
         break

print("The number combinations with the least recipients is ", working_combinations)
