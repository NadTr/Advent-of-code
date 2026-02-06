print("advent of code 2016 day 18")

with open('./input.txt') as f:
    line = f.read()

def find_number_of_safe_tiles(line):
    result = 0
    for char in line:
        if char == ".":
            result += 1
    return result


def execute_instructions(line):
    new_line = ""
    for i in range(len(line)):
        previous_trio = ""
        if i == 0:
            previous_trio = "." + line[:2]
        elif i == len(line)-1:
            previous_trio = line[-2:] + "."
        else:
            previous_trio =  line[i-1 : i+2]
        # print(previous_trio)
        if previous_trio == "^^." or previous_trio == ".^^" or previous_trio == "^.." or previous_trio == "..^"  :
            new_line += "^"
        else:
            new_line += "."
        # print(new_line)
    return new_line


number_of_rows =400000
number_of_safe_tiles = find_number_of_safe_tiles(line)

for _ in range(number_of_rows -1):
    line = execute_instructions(line)
    number_of_safe_tiles += find_number_of_safe_tiles(line)

print("The value in register a is ", number_of_safe_tiles)