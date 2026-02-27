from pathlib import Path
import copy
print("advent of code 2020 day 11")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()
    for i in range(len(file)):
        file[i] = list(file[i])

def occupied_seats_around(row_number, column_number):
    occupied_seats = -1 if file[row_number][column_number] == "#" else 0
    for i in range(row_number-1, row_number+2):
        for j in range(column_number-1, column_number+2):
            symbol = file[i][j] if i >= 0 and i < len(file) and j >= 0 and j < len(file[0]) else "L"
            if symbol == "#":
                occupied_seats += 1
    return occupied_seats

def occupy_seat(room):
    modified_room = copy.deepcopy(room)
    for i in range(len(room)):
        for j in range(len(room[i])):
            if room[i][j] == "L": 
                if occupied_seats_around(i,j) == 0:
                    modified_room[i][j] = "#"
            if room[i][j] == "#":
                if occupied_seats_around(i,j) >= 4:
                    modified_room[i][j] = "L"
    return modified_room


is_room_stabilized = False

while not is_room_stabilized:
    new_file = occupy_seat(file)
    if new_file == file:
        is_room_stabilized = True
    file = new_file

result = 0
for line in file:
    result += line.count("#")

print("The number of seats that end up occupied is", result)