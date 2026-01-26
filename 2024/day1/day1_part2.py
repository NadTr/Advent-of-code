print("advent of code 2024 day 1")

global total_similarities
total_similarities = 0
left_col=[]
right_col=[]

with open('./day1.txt') as f:
    file = f.read().splitlines()

for line in file:
    line = line.split()
    left_col += [int(line[0])]
    right_col += [int(line[1])]

left_col = sorted(left_col)
right_col = sorted(right_col)

start_index = 0

for i in range(len(left_col)):
    appearences = 0
    for j in range(start_index, len(right_col)):
        if left_col[i]==right_col[j]:
            appearences += 1
        if right_col[j] > left_col[i]:
            # print (appearences, left_col[i], " mult = ", appearences * left_col[i])
            total_similarities += appearences * left_col[i]
            break

print("The total similarities between these lists is " + str(total_similarities))
