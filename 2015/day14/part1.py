from pathlib import Path
print("advent of code 2015 day 14")


script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:    file = f.read().splitlines()

run_time = 2503
datas = {}
biggest_distance = 0
all_distances = []

def run(reindeer, time):
    timer = 0
    distance = 0
    # while(timer <= time):
    for i in range(time):
        if timer < reindeer["run_time"]:
            distance += reindeer["speed"]
            # print(i, timer, distance)
            timer +=1
        elif timer >= reindeer["run_time"] and timer < reindeer["run_time"] +reindeer["rest_time"]:
            timer += 1
        else:
            timer = 1
            distance += reindeer["speed"]
    return distance


for i in range(len(file)):
    line = file[i].split() 
    datas[line[0]]={ "speed": int(line[3]), "run_time": int(line[6]), "rest_time": int(line[13])}

for key in datas:
    distance = run(datas[key], run_time)
    all_distances += [distance]

# print(all_distances)
biggest_distance = max(all_distances)

print("The winning reinder has run a total of ", biggest_distance)
