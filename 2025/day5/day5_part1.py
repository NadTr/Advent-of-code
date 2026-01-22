print("advent of code day 5")

global number_of_fresh_ingredients
number_of_fresh_ingredients = 0

with open('./day5.txt') as f:
    file = f.read().split("\n\n")
    fresh_ranges = file[0].splitlines()
    ingredients = file[1].splitlines()

def is_ingredient_fresh(ingr_id):
    fresh = False
    for ranges in fresh_ranges:
        (min, max) = ranges.split("-")
        # print("freshness range is from " + min + " to " + max)
        if ingr_id >= int(min) and ingr_id <= int(max):
            fresh = True
            # print ("the ingredient " + str(ingr_id) + " is fresh")
            return fresh
    return fresh

for ingr in ingredients:
    is_fresh = is_ingredient_fresh(int(ingr))
    if(is_fresh):
        number_of_fresh_ingredients += 1


print("There are "+ str(number_of_fresh_ingredients)+" fresh ingredients ")


    