from pathlib import Path
print("advent of code 2015 day 8")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

def string_length(line):
    index = 0
    length = 0
    escape = False
    while index <len(line):
        char = line[index]
        if escape:
            if char == "x":
                index += 3
            else:
                index += 1
            length += 1
            escape = False
        else:
            if char.isalpha():
                length += 1
                index += 1
            elif char == "\\":
                escape = True
                index += 1
    return length
        
code_total = 0
char_total = 0

for line in file : 
    code_total += len(line)
    char_total += string_length(line[1:-1])

result = code_total - char_total
print("The sum of string length is ", result)
