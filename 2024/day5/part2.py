from pathlib import Path
print("advent of code 2024 day 5")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:    
    file = f.read()

unorganised_updates = []
result = 0

(rules, updates) = file.split("\n\n")

rules = rules.splitlines()
for r in range(len(rules)):
    (n1, n2) = rules[r].split("|")
    rules[r] = [int(n1), int(n2)]

updates = updates.splitlines()
for r in range(len(updates)):
    pages = updates[r].split(",")
    updates[r] = list(map(int, pages))


def is_update_organised(update):
    correct_order = True
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                correct_order = False               
    return correct_order


def organise_update(update):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            index_page1 = update.index(rule[0])
            index_page2 = update.index(rule[1])
            if index_page1 > index_page2:
                update[index_page1] = rule[1]
                update[index_page2] = rule[0]
    return update


for update in updates:
    if not is_update_organised(update):
        unorganised_updates += [update]

for unorganised_update in unorganised_updates:
    reorganised_updates = organise_update(unorganised_update)
    while not is_update_organised(reorganised_updates):
        reorganised_updates = organise_update(reorganised_updates)
    if is_update_organised(reorganised_updates):
        result += reorganised_updates[len(reorganised_updates)// 2]
 
print("The sum of the middle page number from those correctly-reordered updates is",result)
