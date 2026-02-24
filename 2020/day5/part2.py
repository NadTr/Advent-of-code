from pathlib import Path
print("advent of code 2020 day 5")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

rows = range(128)
cols = range(8)

def get_seat_row(instr):
    this_row = rows[:]
    for i in instr:
        if i == "F":
            this_row = this_row[:len(this_row)//2]
        else:
            this_row = this_row[len(this_row)//2:]
    return this_row[0]


def get_seat_col(instr):
    this_col = cols[:]
    for i in instr:
        if i == "L":
            this_col = this_col[:len(this_col)//2]
        else:
            this_col = this_col[len(this_col)//2:]
    return this_col[0]


def get_seat_id(line):
    row = get_seat_row(line[:-3])
    col = get_seat_col(line[-3:])
    return 8 * row + col

seats = []

for line in file:
    seat_id = get_seat_id(line)
    seats += [seat_id]

seats = sorted(seats)
for i in range(len(seats) -1):
    if seats[i+1] != seats[i] + 1:
        print((seats[i], seats[i+1]))
        my_seat = seats[i] +1

print("The available seat ID on my boarding pass is", my_seat)