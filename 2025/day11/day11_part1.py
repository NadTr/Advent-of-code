print("advent of code day 11")

global number_of_paths
number_of_paths = 0
start_key = 0
dictio = {}

with open('./day11.txt') as f:
    file = f.read().splitlines()

def find_path(path_key):
    global number_of_paths
    step = dictio[path_key]
    # print("find next step to " + str(step))
    for index in range(len(step)):
        if step[index] == "out":
            number_of_paths += 1
            # print("found one path")
            break
        else:
            find_path(step[index])
    
    
for line in range(len(file)):
    file[line] = file[line].split(":")
    dictio.update({ file[line][0]: file[line][1].split()}) 

find_path("you")


print("There are "+ str(number_of_paths) +" many different paths lead from you to out ")


    