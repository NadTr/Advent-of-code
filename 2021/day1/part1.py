from pathlib import Path
print("advent of code 2021 day 1")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()
    for ind in range(len(file)):
        file[ind] = int(file[ind])

result = 0

for i in range (1, len(file)):
    if file[i-1] < file[i]:
        result += 1

print("The number of times a depth measurement increases is", result)