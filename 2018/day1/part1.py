from pathlib import Path
print("advent of code 2018 day 1")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
     file = f.read().splitlines()

frequency = 0
for digit in file:
    frequency += int(digit)

print("The the resulting frequency is", frequency)