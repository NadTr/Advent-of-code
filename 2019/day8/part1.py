from pathlib import Path
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
        img_layers.append([[int(file[i])]])
    elif y ==0:
        img_layers[layer].append([int(file[i])])
    else:
        img_layers[layer][x].append(int(file[i]))
    y += 1

def count_elements(list, element):
    number = 0
    for line in list:
        number += line.count(element)
    return number

def find_layer_with_least_zeroes():
    min_number_zeroes= img_size[0] *img_size[1]
    number_zeroes, layer_index =0, 0
    for layer in range(len(img_layers)):
        number_zeroes = count_elements(img_layers[layer], 0)
        if number_zeroes < min_number_zeroes:
            min_number_zeroes = number_zeroes
            layer_index = layer
    return layer_index


layer_index = find_layer_with_least_zeroes()
result = count_elements(img_layers[layer_index], 1) * count_elements(img_layers[layer_index], 2)

print("The result of the layer with the least zeroes is", result)