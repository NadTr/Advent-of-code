from pathlib import Path
print("advent of code 2016 day 2")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
     file = f.read().splitlines()

directions = {
    "L":[0, -1],
    "D":[1, 0],
    "R":[0, 1],
    "U":[-1, 0]
}

pave = [["","",1,"",""],
["",2, 3, 4,""],
[5, 6, 7, 8, 9],
["","A", "B", "C",""],
["", "","D","",""]
]
limits= [0,1,2,1,0]

pos = [2,0]
password = ""

for line in file:
    for step in line:
        if directions[step][0] != 0:
            if pos[0]+ directions[step][0] >= 2 - limits[pos[1]]  and pos[0]+ directions[step][0] <= 2 + limits[pos[1]]:
                pos[0] += directions[step][0]
        if directions[step][1] != 0 :
            if pos[1]+ directions[step][1] >= 2 - limits[pos[0]] and pos[1]+ directions[step][1] <= 2 + limits[pos[0]]:
                pos[1] += directions[step][1]

        # print(step, pos)
    number = pave[pos[0]][pos[1]]
    password += str(number)
    # print(number, password)

print("The password is ", password)