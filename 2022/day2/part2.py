from pathlib import Path
print("advent of code 2022 day 2")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()
result = {
    'X': 0,
    'Y' :3,
    'Z': 6
}
shape = {
    'A': 1,
    'B' :2,
    'C': 3 
    }
hands = {
    'A':{ 'X': 'C' , 'Y': 'A', 'Z': 'B'},
    'B':{ 'X': 'A' , 'Y': 'B', 'Z': 'C'},
    'C':{ 'X': 'B' , 'Y': 'C', 'Z': 'A'},   
    }
score = 0
for line in file:
    op, res = line.split()
    score += result[res] + shape[hands[op][res]]

print("The total score if everything goes exactly according to the strategy guide is", score)