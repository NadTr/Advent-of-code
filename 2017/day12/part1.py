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
    # print(connected)
    connections = connection_list[index]
    for c in connections:
        if c not in connected:
            add_connection_to_list(c)

# print(connection_list)

add_connection_to_list('0')

print("The number programs are in the group that contains program ID 0 is", len(connected))