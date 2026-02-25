from pathlib import Path
import re
print("advent of code 2020 day 7")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

bags_in = {}
bag_to_find = "shiny gold"

for line in file:
    ext, inside = line.split(" bags contain ")
    if inside != "no other bags.":
        # bags_in.update({ext:[]})
        bags_in.update({ext:{}})
        inside = inside.split(", ")
        for i in inside:
            numbers = re.findall(r'\d+', i)
            numbers = int(numbers[0])
            color = re.sub(r'\d+ ', '', i)
            color = re.sub(r' bag(s)?\.?', '', color)
            bags_in[ext].update({color : numbers})


def find_inner_bags(bag):
    number_of_bags = 0
    if bag in bags_in:
        for key, value in bags_in[bag].items():
            number_of_bags += value * (1 + find_inner_bags(key))
    return number_of_bags

number_of_outer_bags = find_inner_bags(bag_to_find)

print("The number of individual bags are required inside your single shiny gold bag is", number_of_outer_bags)