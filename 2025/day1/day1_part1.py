print("advent of code day 1")
#lines = pathlib.Path('C:/path/numbers.txt').read_text().splitlines()

def turn_handle(old_number, rotation, number_to_add):
    new_number = old_number
    new_number += (number_to_add, -number_to_add)[rotation == "L"]
    while (new_number > 99 or new_number < 0):
        if new_number > 99:
            new_number -= 100
        elif new_number < 0:
            new_number += 100
    return new_number

with open('./day1.txt') as f:
    lines = f.read().splitlines()

print("The dial starts by pointing at 50.")

number = 50
number_of_zeroes = 0

for i in range(len(lines)):
    number = turn_handle(number, lines[i][0], int(lines[i][1:]))
    print("The dial is rotated " + lines[i] + " to point at " + str(number))
    if number == 0:
        number_of_zeroes +=1

print("the number of zeroes is " + str(number_of_zeroes))
print(number_of_zeroes)


    