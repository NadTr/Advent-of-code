from pathlib import Path
print("advent of code 2021 day 8")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()
unique_num_count = 0

for line in file:
    signal, output = line.split('|')
    output = output.split()
    for o in output:
        if len(o) in [2, 3, 4, 7]:
            unique_num_count  += 1


print("The number of times do digits 1, 4, 7, or 8 appears is ", unique_num_count)