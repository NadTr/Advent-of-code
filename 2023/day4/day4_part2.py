import numpy as np
print("advent of code 2023 day 4")

global file
global cards_distribution
cards_distribution = np.ones(5)
global sum_of_card_points
sum_of_card_points = 0

with open('./day4.txt') as f:
    file = f.read().splitlines()
    cards_distribution = np.ones(len(file), dtype=int)


def value_of_card(card):
    result = 0
    card = card.split("|")
    card[0]= card[0].split()
    card[1]= card[1].split()
    for i in range(len(card[0])):
        for j in range(len(card[1])):
            if card[0][i] == card[1][j]:
                    result += 1
    return result
    


for line in range(len(file)):
    card = file[line].split(":")
    res = value_of_card(card[1])
    # print("card ",card[0], " has ", res, " matching numbers")
    for i in range(res):
        # print("so win ",cards_distribution[line]," copy of the card ", line + i + 1)
        cards_distribution[line + i + 1] += 1 * cards_distribution[line]
         


for i in cards_distribution:
     sum_of_card_points += i

            

print("The snumber of points on all the cards is " + str(sum_of_card_points))
