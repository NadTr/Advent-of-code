from pathlib import Path
print("advent of code 2022 day 2")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

shape = {
    'X': 1,
    'Y' :2,
    'Z': 3 
    }
hands = {
    'A':{ 'X': 3 , 'Y': 6, 'Z': 0},
    'B':{ 'X': 0 , 'Y': 3, 'Z': 6},
    'C':{ 'X': 6 , 'Y': 0, 'Z': 3},   
    }
score = 0
for line in file:
    op, mine = line.split()
    score += hands[op][mine] + shape[mine]

print("The total score if everything goes exactly according to the strategy guide is", score)