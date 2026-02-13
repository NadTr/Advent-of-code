from pathlib import Path
print("advent of code 2016 day 9")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

length_of_decompressed_file = 0

def length_of_decompress_file(line):
    letters = list(line)
    decompressed_line_length = 0
    i = 0
    while i in range(len(letters)):
        if letters[i]=="(":
            marker =""
            index = i + 1
            while letters[index] !=")":
                marker += letters[index]
                index += 1
            marker = marker.split("x")
            str_to_repeat = ""
            for j in range(index + 1, index+ 1 + int(marker[0])):
                if j < len(letters):
                    str_to_repeat += letters[j]
            substr_length = 0
            if "(" in str_to_repeat:
                substr_length += length_of_decompress_file(str_to_repeat)
            else:
                substr_length = len(str_to_repeat)
            decompressed_line_length += int(marker[1]) * substr_length
            i = index + int(marker[0]) + 1
        else:
            decompressed_line_length += 1
            i += 1
    return decompressed_line_length
        

for line in file:
    length_of_decompressed_file += length_of_decompress_file(line)

print("The length of the decompressed file is ", length_of_decompressed_file)