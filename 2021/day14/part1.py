from pathlib import Path
from collections import Counter
print("advent of code 2021 day 14")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

result = 0
template = file[0]
insertion_rules = {}

for i in range(2, len(file)):
    line = file[i].split(' -> ')
    insertion_rules.update({ line[0]: line[1]})

def insert_chars(line):
    new_line = ''
    for i in range(len(line)-1):
        if line[i:i+2] in insertion_rules.keys():
            new_line += line[i] + insertion_rules[line[i:i+2]]
        else:
            new_line += line[i]
    
    return new_line + line[-1]

text = template

for _ in range(10):
    text = insert_chars(text)

char_count = Counter(text)

print("The quantity of the most common element and subtract the quantity of the least common element is ", max(char_count.values())- min(char_count.values()))