print("advent of code 2016 day 2")

with open('./input.txt') as f:
    file = f.read().splitlines()

directions = {
    "L":[0, -1],
    "D":[1, 0],
    "R":[0, 1],
    "U":[-1, 0]
}

pave = [[1,2,3],[4,5,6],[7,8,9]] 

pos = [1,1]
password = ""

for line in file:
    for step in line:
        if pos[0]+ directions[step][0] >= 0 and pos[0]+ directions[step][0] <= 2:
            pos[0] += directions[step][0]
        if pos[1]+ directions[step][1] >= 0 and pos[1]+ directions[step][1] <= 2:
            pos[1] += directions[step][1]
        # print(step, pos)
    number = pave[pos[0]][pos[1]]
    password += str(number)
    # print(number, password)

print("The password is ", password)