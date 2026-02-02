import numpy as np
import re
print("advent of code 2015 day 10")

with open('./input.txt') as f:
    start_number = f.read()

def read_digits(number_to_read):
    prev_digit =  None
    read_number_array = []
    number_of_similars = 0
    for digit in number_to_read:
        if (prev_digit != None and digit != prev_digit):
            read_number_array.append([number_of_similars, prev_digit])
            number_of_similars = 0

        number_of_similars += 1
        prev_digit = digit

    read_number_array.append([number_of_similars, prev_digit])
 
    return "".join(str(count) + digit for count, digit in read_number_array)

for i in range(50) : 
    print(i)
    new_number = read_digits(start_number)
    # print(start_number, " is read as ", new_number)
    start_number = new_number


print("The length of the result is ", len(new_number))
