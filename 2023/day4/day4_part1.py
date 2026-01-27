print("advent of code 2023 day 4")

global file
global sum_of_card_points
sum_of_card_points = 0

with open('./day4.txt') as f:
    file = f.read().splitlines()

def value_of_card(card):
    result = 0
    card = card.split("|")
    card[0]= card[0].split()
    card[1]= card[1].split()
    for i in range(len(card[0])):
        for j in range(len(card[1])):
            if card[0][i] == card[1][j]:
                if result > 0:
                    result *=2
                else:
                    result = 1
    return result
    


for line in file:
    card = line.split(":")
    sum_of_card_points += value_of_card(card[1])

            

print("The snumber of points on all the cards is " + str(sum_of_card_points))
