from pathlib import Path
import re
print("advent of code 2015 day 12")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read()
 
numbers = re.findall(r'[-+]?\d+', file)
numbers = list(map(int, numbers))
total_sum = sum(numbers)

print("The total sum of all numbers is ", total_sum)
