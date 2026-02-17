from pathlib import Path
print("advent of code 2024 day 4")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:    
    file = f.read().splitlines()

number_of_XMAS = 0

def find_all_XMAS_around(x, y):
    for i in [-1,1]:
        for j in [-1,1]:
            if ((file[x + i][y + j] == "M" and  file[x - i][y - j]=="S"
                and file[x + i][y - j] == "M" and  file[x - i][y + j]=="S")
                or (file[x + i][y + j] == "S" and  file[x - i][y - j]=="M"
                and file[x + i][y - j] == "M" and  file[x - i][y + j]=="S")):
                # print( "the A in ", x, " and ", y, " form a XMAS")
                return 1
    return 0

for line in range(1, len(file) - 1):
    for col in range(1, len(file[line]) - 1):
        if file[line][col] == "A":
            number_of_XMAS +=find_all_XMAS_around(line, col)

print("The total number of XMAS is  " + str(number_of_XMAS))
