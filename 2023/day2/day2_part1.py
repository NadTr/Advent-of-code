import re
print("advent of code 2023 day 2")

global sum_of_ids
sum_of_ids = 0

with open('./day2.txt') as f:
    file = f.read().splitlines()

def is_game_possible(game):
    for round in game:
        round = round.split()
        # print("thers is ", round[0], "  ", round[1], " balls" )
        if round[1] == "red" and int(round[0]) > 12:
            return False
        elif round[1] == "green" and int(round[0]) > 13:
            return False
        elif round[1] == "blue" and int(round[0]) > 14:
            return False
    return True

for i in range(len(file)):
    line = file[i].split(":")
    game_number = line[0].split()
    game_result = line[1].split("; ")
    game_result_new = []
    for i in game_result:
        game_result_new += i.split(", ")
    if(is_game_possible(game_result_new)):
        sum_of_ids += int(game_number[1])


print("The sum of all of the calibration values is " + str(sum_of_ids))
