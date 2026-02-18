from pathlib import Path
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


still_change = True
while still_change:
    new_polymer = reaction(polymer)
    if new_polymer == polymer:
        still_change = False
    else:
        polymer = new_polymer

print("The number of units remaining after fully reacting the polymer is", len(polymer))