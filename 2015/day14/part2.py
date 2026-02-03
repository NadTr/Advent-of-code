print("advent of code 2015 day 14")

run_time = 2503
datas = {}
named_distances = {}
scores = {}

with open('./input.txt') as f:
    file = f.read().splitlines()

def run(reindeer, time):
    timer = 0
    distance = 0
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
    scores[line[0]]= 0

for i in range(1,run_time):
    all_distances = []
    for key in datas:
        distance = run(datas[key], i)
        all_distances += [distance]
        named_distances[key]= distance

    
    max_distance = max(all_distances)
    for key in named_distances:
        if named_distances[key] == max_distance:
            scores[key] += 1
    # print(named_distances, max_distance, scores)

big_winner = max(scores, key=scores.get)

print("The winning reinder is ", big_winner, " with a score of ", scores[big_winner])
