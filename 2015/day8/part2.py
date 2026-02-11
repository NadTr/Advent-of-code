print("advent of code 2015 day 8")

with open('./input.txt') as f:
    file = f.read().splitlines()

def encode_string_length(line):
    length = 2
    for char in line:
        if char.isalpha() or char.isdigit():
            length += 1
        else:
            length +=2
    return length
        
encode_total = 0
code_total = 0

for line in file : 
    encode_total += encode_string_length(line)
    code_total += len(line)
    # print(line, encode_total, code_total)

result = encode_total - code_total
print("The sum of string length is ", result)
