from pathlib import Path
print("advent of code 2021 day 11")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

score =  0
pairs = {
    ')' : '(',
    ']' : '[',
    '}' : '{',
    '>' : '<'
}
points = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

def inspect_line(line):
    open = []
    for char in line:
        if char in pairs.values():
            open.append(char)
        else:
            if pairs[char] == open[-1]:
                open.pop()
            else:
                return points[char]
    return 0

for line in file:
    score += inspect_line(line)

print("The total syntax error score is ",  score)