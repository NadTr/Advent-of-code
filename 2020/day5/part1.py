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

highest_seat_id = 0
for line in file:
    seat_id = get_seat_id(line)
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id

print("The highest seat ID on a boarding pass is", highest_seat_id)