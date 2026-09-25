from pathlib import Path
print("advent of code 2021 day 10")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

scores =  []
pairs = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}
points = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
} 
def autocomplete_score(arr):
    score = 0
    for char in arr[::-1]:
        score = score * 5  + points[pairs[char]]
    return score

def inspect_line(line):
    open = []
    for char in line:
        if char in pairs.keys():
            open.append(char)
        else:
            if char == pairs[open[-1]]:
                open.pop()
            else:
                return 0
    return autocomplete_score(open)

for line in file:
    score = inspect_line(line) 
    if score != 0:
        scores.append(score)

scores = sorted(scores)

print("The total syntax error score is ",  scores[len(scores)//2 + ( -1 if len(scores)% 2 == 0 else 0)])