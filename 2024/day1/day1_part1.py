print("advent of code 2024 day 1")

global total_distance
total_distance = 0
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

for i in range(len(left_col)):
    total_distance += abs(right_col[i] - left_col[i])


# print(left_col, right_col)
print("The total distance between these numbers is " + str(total_distance))
