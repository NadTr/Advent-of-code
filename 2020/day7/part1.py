from pathlib import Path
import re
print("advent of code 2020 day 7")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

bags_in = {}
bag_to_find = "shiny gold"

for line in file:
    ext, int = line.split(" bags contain ")
    if int != "no other bags.":
        bags_in.update({ext:[]})
        int = int.split(", ")
        for i in int:
            numbers = re.findall(r'\d+', i)
            color = re.sub(r'\d+ ', '', i)
            color = re.sub(r' bag(s)?\.?', '', color)
            bags_in[ext] += [color]

def find_outer_bags(bag):
    outer_bags = set()
    for key, value in bags_in.items():
        if bag in value:
            outer_bags.update({key})
            for bags in find_outer_bags(key):
                outer_bags.update({bags})
    return outer_bags

number_of_outer_bags = len(find_outer_bags(bag_to_find))

print("The number of bag colors that can eventually contain at least one shiny gold bag is", number_of_outer_bags)