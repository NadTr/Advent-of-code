print("advent of code 2017 day 2")

with open('./input.txt') as f:
    file = f.read().splitlines()

def division_of_divisibles(row):
    division = 0
    for i in range(len(row)):
        row[i] = int(row[i])

    for i in range(len(row)):    
        for j in range(len(row)):
            if i != j and row[i] % row[j] == 0:
                division = row[i] // row[j]
                # print(i, j, row[i], row[j], row[i] // row[j])
    return division


checksum = 0
for line in range(len(file)):
    file[line] = file[line] .split()
    checksum += division_of_divisibles(file[line])

print("The checksum of the spreadsheet is", checksum)