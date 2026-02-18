from pathlib import Path
print("advent of code 2018 day 1")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
     file = f.read().splitlines()

def find_frequency_that_appear_twice(frequency):
    frequencies = {frequency}
    while True:
        for digit in file:
            frequency += int(digit)
            if frequency in frequencies:
                return frequency
            else:
                frequencies.add(frequency)

frequency = find_frequency_that_appear_twice(0)

print("The first frequency that appear twice is", frequency)   
 