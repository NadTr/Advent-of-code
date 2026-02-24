from pathlib import Path
import numpy as np
print("advent of code 2019 day 8")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read()

img_size =[25,6]
img_layers = []
x, y, layer = 0, 0, 0

for i in range(len(file)):
    if y >= img_size[0]:
        y =0
        x += 1    
    if x >= img_size[1]:
        x, y = 0, 0
        layer += 1

    if x == 0 and y == 0:
        img_layers.append([[file[i]]])
    elif y ==0:
        img_layers[layer].append([file[i]])
    else:
        img_layers[layer][x].append(file[i])
    y += 1


def print_img(img):
    for line in img:
        print("".join(line))
        

last_layer = img_layers[0][:]

for x in range(len(last_layer)):
    for y in range(len(last_layer[0])):
        for layer in range(len(img_layers)):
            if img_layers[layer][x][y] != "2":
                last_layer[x][y] = chr(9608) if img_layers[layer][x][y] != "0" else " "
                break

print_img(last_layer)