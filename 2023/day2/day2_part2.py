import re
print("advent of code 2023 day 2")

global sum_of_ids
sum_of_ids = 0

with open('./day2.txt') as f:
    file = f.read().splitlines()

def game_power(game):
    reds = 1
    greens = 1
    blues = 1
    for round in game:
        round = round.split()
        if round[1] == "red" and int(round[0]) > reds:
            reds= int(round[0])
        elif round[1] == "green" and int(round[0]) > greens:
            greens= int(round[0])
        elif round[1] == "blue" and int(round[0]) > blues:
            blues= int(round[0])
    # print("there is at least ", reds, " red,  ",greens, "greens",blues, " blues ", " balls" )
    return reds * greens * blues

for i in range(len(file)):
    line = file[i].split(":")
    game_number = line[0].split()
    game_result = line[1].split("; ")
    game_result_new = []
    for i in game_result:
        game_result_new += i.split(", ")
    sum_of_ids += game_power(game_result_new)


print("The sum of all of the calibration values is " + str(sum_of_ids))
