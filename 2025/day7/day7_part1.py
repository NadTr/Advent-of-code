print("advent of code day 7")

global number_of_splits
number_of_splits = 0

with open('./day7.txt') as f:
    file = f.read().splitlines()

length = len(file)

for line in range(len(file)):
    file[line] = list(file[line]) 

start_point = [0, file[0].index("S")]

def follow_line(start_point):
    global number_of_splits
    for ind in range(start_point[0], length):
        if file[ind][start_point[1]] == "^":
            if file[ind][start_point[1]-1] == "." or file[ind][start_point[1]+1] == ".":
                number_of_splits += 1

            if file[ind][start_point[1]-1] == ".":
                # number_of_splits += 1
                follow_line([ind, start_point[1] - 1])
            if file[ind][start_point[1]+1] == ".":
                # number_of_splits += 1
                follow_line([ind, start_point[1] + 1])
            break
        else:
            file[ind][start_point[1]] = "|"

        # print(file[ind][start_point[1]])


follow_line(start_point)
# for line in file:
    # print(line)
print("The tachyon beam is split a total of "+ str(number_of_splits) + " times.")


    