from pathlib import Path
import numpy as np
print("advent of code 2015 day 18")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
      grid = f.read().splitlines()

for i in range(len(grid)):
    grid[i] = list(grid[i])
new_grid = np.copy(grid)
list_stay_on = ["0-0", "0-"+str(len(grid[0])-1), str(len(grid)-1) +"-0", str(len(grid[0])-1) +"-" +str(len(grid)-1)]

number_of_steps = 100

def look_around(row_number, column_number):
    light_arounds = 0 if grid[row_number][column_number] == "." else -1
    for i in range(row_number-1, row_number+2):
        for j in range(column_number-1, column_number+2):
            symbol = grid[i][j] if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) else "."
            if symbol == "#":
                light_arounds += 1
    return light_arounds


for step in range(1,number_of_steps + 1):
    number_ligths_on = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            light_arounds = look_around(i,j)
            if str(i) +"-"+ str(j) in list_stay_on:
                new_grid[i][j] = "#"
                number_ligths_on += 1                
            elif grid[i][j] == "#":
                if (light_arounds == 2 or light_arounds == 3):
                    new_grid[i][j] = "#"
                    number_ligths_on += 1
                else:
                    new_grid[i][j] = "."
            else:
                if (light_arounds == 3):
                    new_grid[i][j] = "#"
                    number_ligths_on += 1
                else:
                    new_grid[i][j] = "."
    grid = np.copy(new_grid)             

print("The number of lights on after", number_of_steps," steps is ", number_ligths_on)
