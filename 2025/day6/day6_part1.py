print("advent of code day 6")

global global_sum
global_sum = 0
number_of_col=0
number_of_row = 0

with open('./day6.txt') as f:
    file = f.read().splitlines()
    number_of_row = len(file)

def result_of_the_line(index):
    result = 0
    operator = file[number_of_row - 1][index]
    # print(operator)
    if(operator == "+"):
        for i in range(number_of_row -1):
            result += int(file[i][index])
    if(operator == "*"):
        result = 1
        for j in range(number_of_row - 1):
            result *= int(file[j][index])
    # print("the result of the col " + str(index) + " is equal to " + str(result))
    return result

for line in range(len(file)):
    file[line] = file[line].split()

number_of_col = len(file[0])
for index_col in range(number_of_col):
    global_sum += result_of_the_line(int(index_col))

# print("The file has : "+ str(number_of_col) +" col "+ str(number_of_row) + " rows")
print("There global sum is equal to: "+ str(global_sum))


    