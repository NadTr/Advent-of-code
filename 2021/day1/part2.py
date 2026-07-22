from pathlib import Path
print("advent of code 2021 day 1")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()
    for ind in range(len(file)):
        file[ind] = int(file[ind])

result = 0

for i in range (len(file) - 3):
    sliding_window_1 = file[i] + file[i+1] + file[i+2]
    sliding_window_2 = file[i+1] + file[i+2] + file[i+3]
    if sliding_window_1 < sliding_window_2:
        result += 1

print("The number of times the sum of measurements in this sliding window increases is", result)