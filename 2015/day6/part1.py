from pathlib import Path
import numpy as np
import re
print("advent of code 2015 day 6")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
         file = f.read().splitlines()

lights = np.zeros((1000,1000),  dtype=int)

def change_lights(area, manner):
    for x in range(int(area[0][0]), int(area[1][0]) + 1):
        for y in range(int(area[0][1]), int(area[1][1]) + 1):
            if manner == "toggle ":
                lights[x,y] = 1 - lights[x][y]
            else:
                lights[x,y] = 1 if manner == "turn on " else 0

for line in file : 
    manner = re.findall('([a-zA-Z ]*)\d*.*', line)
    area = line[len(manner[0]):].split("through")
    for i in range(len(area)):
        area[i] = re.findall(r'-?\d*\.?\d+', area[i])
    # print (manner, " on ", area)
    change_lights(area, manner[0])

    
number_of_ligths_on = sum(sum(lights))

print("The number of ligths on is ", number_of_ligths_on)
