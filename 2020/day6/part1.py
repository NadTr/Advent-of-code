from pathlib import Path
import re
print("advent of code 2020 day 6")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().split("\n\n")

total_positive_answers = 0

for line in file:
    line = set(re.findall(r"[a-z]", line))
    total_positive_answers += len(line)

print("The number of positive answers is", total_positive_answers)