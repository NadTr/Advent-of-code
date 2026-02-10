import re
print("advent of code 2017 day 9")
with open('./input.txt') as f:
    file = f.read()

file = re.sub(r'\!.{1}', '', file)
file = re.sub(r'<.*?>','', file)

bracket_scores_list = {}
depth = 0

for i in range(len(file)):
    if file[i] == "{":
        depth += 1
        bracket_scores_list.update({i: depth})
    elif file[i] == "}":
        depth -= 1 if depth > 0 else 0
    else:
        continue

score = sum(bracket_scores_list.values()) 

print("The total score for all groups is", score)