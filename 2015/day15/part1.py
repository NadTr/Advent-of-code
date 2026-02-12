from pathlib import Path
import itertools
print("advent of code 2015 day 15")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:    
    file = f.read().splitlines()

total_spoons = 100
total_score = 0
datas = {}

for i in range(len(file)):
    (ingredient, property_names) = file[i].split(": ")
    property_names = property_names. split(", ")
    datas.update({ingredient:{}})
    for property in property_names:
        (property_name, property_amount) = property. split()
        datas[ingredient].update({property_name : int(property_amount)})

ingredients = list(datas.keys())
recipes = list(itertools.combinations_with_replacement(ingredients, total_spoons))
recipe = {}
for ingredient in ingredients:
    recipe.update({ingredient: 0})
    
recipe_score = {}
property_names = list(datas[ingredients[0]].keys())
property_names.remove("calories")

for r in recipes:
    score = 1
    for property in property_names:
        recipe_score.update({property: 0})

    for ingredient in ingredients:
        ingr_count = r.count(ingredient)
        recipe[ingredient] = ingr_count

    for ingr in recipe:
        for property in property_names:
            recipe_score[property] += recipe[ingr] * datas[ingr][property]

    for property in property_names:
            score *= (recipe_score[property] if recipe_score[property] > 0 else 0)

    if total_score < score:
        total_score = score

print("The score of the highest-scoring cookie is ", total_score)
