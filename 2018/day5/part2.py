from pathlib import Path
import string, re
print("advent of code 2018 day 5")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
     polymer = f.read()


def reaction(polymer):
    polymer = list(polymer)
    for i in range(len(polymer)):
        if i >= len(polymer) -1:
            return "".join(polymer)
        else:
            letter1,letter2 = polymer[i], polymer[i+1]
            if letter1.isupper() and letter2.islower() and letter1 == letter2.upper():
                polymer.pop(i)
                polymer.pop(i)
            elif letter1.islower() and letter2.isupper() and letter1 == letter2.lower():
                polymer.pop(i)
                polymer.pop(i)
            else: continue

def try_another_polymer(polymer):
    while True:
        new_polymer = reaction(polymer)
        if new_polymer == polymer:
            return len(polymer)
        else:
            polymer = new_polymer

minimum_length = len(polymer)
for letter in string.ascii_lowercase:
    changed_polymer = re.sub(letter, '', polymer)
    changed_polymer = re.sub(letter.upper(), '', changed_polymer)
    length = try_another_polymer(changed_polymer)
    if length < minimum_length:
        minimum_length = length


print("The length of the shortest polymer you can produce is", minimum_length)