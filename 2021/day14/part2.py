from pathlib import Path
from collections import Counter, defaultdict
print("advent of code 2021 day 14")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

result = 0
template = file[0]
insertion_rules = {}
counter = defaultdict(int)
char_count = defaultdict(int, Counter(template))

for i in range(2, len(file)):
    pair, to_insert = file[i].split(' -> ')
    insertion_rules.update({ pair: to_insert})

for i in range(len(template)-1):
    counter[template[i:i+2]] += 1

def insert_chars():
    new_counter = {}
    for k, v in counter.items():
        char_count[insertion_rules[k]] += v
        for key in [k[0] + insertion_rules[k],insertion_rules[k] + k[1]]:
            if key in new_counter.keys():
                new_counter[key] += v
            else:
                new_counter.update({key : v})
    return new_counter
           
for i in range(40):
    counter = insert_chars()

print("The quantity of the most common element and subtract the quantity of the least common element is ", max(char_count.values())- min(char_count.values()))