from pathlib import Path
import itertools
print("advent of code 2015 day 13")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:    file = f.read().splitlines()

datas = {}
best_happiness_score = 0

for i in range(len(file)):
    (name_1, result) = file[i].split(" would ")
    (happiness_level, name_2) = result. split(" happiness units by sitting next to ")
    happiness_level = happiness_level.split()
    happiness_level = int(happiness_level[1]) if happiness_level[0] == "gain" else -int(happiness_level[1])
    name_2 = name_2[:-1]
    if name_1 in datas:
        datas[name_1].update({name_2 : happiness_level})
    else:
        datas.update({name_1:{name_2 : happiness_level}})

people = list(datas.keys())
print(people)
tables = list(itertools.permutations(people))

for table in tables:
    happiness = 0
    for i in range(0, len(table)):
        start_person = table[i]
        next_person = table[(0 if i >= len(table)-1 else i+1)]
        happiness += datas[start_person][next_person]
        happiness += datas[next_person][start_person]
    if best_happiness_score < happiness:
        best_happiness_score = happiness

print("The total sum of all max happiness is ", best_happiness_score)
