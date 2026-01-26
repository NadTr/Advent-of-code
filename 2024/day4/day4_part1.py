print("advent of code 2024 day 4")

global number_of_XMAS
number_of_XMAS = 0

with open('./day4.txt') as f:
    file = f.read().splitlines()

def find_XMAS(location, direction):
    letters = ['M', "A", "S"]
    if(location[0] == 0 and location[1]==0):
        return 0
    elif(location [0]+len(letters*direction[0]) > len(file) or location [0]+len(letters*direction[0]) < 0):
        return 0    
    elif(location [1]+len(letters*direction[1]) > len(file[0]) or location [1]+len(letters*direction[1]) < 0):
        return 0
    else:
        for index in range(1, len(letters) + 1):
            (x, y) = (location[0]+ index * direction[0], location[1]+ index * direction[1] )
            if(x >= len(file) or x < 0):
                return 0    
            elif(y >= len(file[0]) or y < 0):
                return 0
            elif(file[x][y] == letters[index -1]):
                continue
            else: return 0
    return 1

def find_all_XMAS_around(x, y):
    tmp_number_of_christmas = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            tmp_number_of_christmas += find_XMAS([x,y], [i,j])
    return tmp_number_of_christmas

for line in range(len(file)):
    for col in range(len(file[line])):
        if file[line][col] == "X":
            number_of_XMAS +=find_all_XMAS_around(line, col)

print("The total snumber of XMAS is  " + str(number_of_XMAS))
