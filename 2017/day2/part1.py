print("advent of code 2017 day 2")

with open('./input.txt') as f:
    file = f.read().splitlines()

def max_range_of_row(row):
    for i in range(len(row)):
        row[i] = int(row[i])
    # print(row)
    return max(row) - min(row)


checksum = 0
for line in range(len(file)):
    file[line] = file[line] .split()
    checksum += max_range_of_row(file[line])

print("The checksum of the spreadsheet is", checksum)