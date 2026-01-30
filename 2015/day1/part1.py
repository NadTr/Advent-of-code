print("advent of code 2015 day 1")

with open('./input.txt') as f:
    file = f.read()

level = 0

for step in file:
    if step == "(":
        level += 1
    elif step == ")":
        level -= 1
    
print("The end level is ", level)