print("advent of code 2017 day 12")

with open('./input.txt') as f:
    file = f.read().splitlines()

connection_list = {}
connected = []

for line in file:
    line = line.split(" <-> ")
    connections = line[1].split(", ")
    connection_list.update({line[0] : connections})


def add_connection_to_list(index):
    global connected
    global connection_list
    connected += [index]
    connections = connection_list[index]
    for c in connections:
        if c not in connected:
            add_connection_to_list(c)

groups = 0

for index in connection_list:
    if index not in connected:
        # print("nouveau groupe ", index)
        add_connection_to_list(index)
        groups += 1

print("The number of groups in the list is", groups)