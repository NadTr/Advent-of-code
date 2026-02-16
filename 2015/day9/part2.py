from pathlib import Path
import itertools
print("advent of code 2015 day 9")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
      file = f.read().splitlines()

longest_distance = 0
roads = {}
            
for i in range(len(file)):
    line = file[i].split(" = ")
    cities = line[0].split(" to ")
    distance = int(line[1])
    if cities[0] in roads:
        roads[cities[0]].update({cities[1] : distance})
    else:
        roads.update({cities[0]:{cities[1] : distance}})

    if cities[1] in roads:
        roads[cities[1]].update({cities[0] : distance})
    else:
         roads.update({cities[1]:{cities[0] : distance}})

cities = list(roads.keys())
routes = list(itertools.permutations(cities))

for combi in routes:
    distance = 0
    for i in range(0, len(combi)-1):
        start_point = combi[i]
        dest = combi[0 if i >= len(combi) else i+1]
        distance += roads[start_point][dest]
    if longest_distance < distance:
         longest_distance = distance

print("The distance of the longest route is ", longest_distance)
