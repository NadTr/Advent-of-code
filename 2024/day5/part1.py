from pathlib import Path
print("advent of code 2024 day 5")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:    
    file = f.read()

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

for update in updates:
    correct_order = True
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                # print(update, rule)
                correct_order = False
                break
    if correct_order:
        # print("update order correct", update, len(update)// 2 )
        result += update[len(update)// 2]

print("The sum of the middle page number from those correctly-ordered updates is",result)
