from pathlib import Path
print("advent of code 2024 day 1")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
     file = f.read().splitlines()

total_distance = 0
left_col=[]
right_col=[]

for line in file:
    line = line.split()
    left_col += [int(line[0])]
    right_col += [int(line[1])]

left_col = sorted(left_col)
right_col = sorted(right_col)

for i in range(len(left_col)):
    total_distance += abs(right_col[i] - left_col[i])

print("The total distance between these numbers is " + str(total_distance))
