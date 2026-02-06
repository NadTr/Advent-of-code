print("advent of code 2016 day 9")

with open('./input.txt') as f:
    file = f.read().splitlines()

length_of_decompressed_file = 0

def decompress_file(line):
    letters = list(line)
    decompressed_line = ""
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
            decompressed_line += "".join(int(marker[1]) * str_to_repeat )
            i = index + int(marker[0]) + 1
        else:
            decompressed_line += "".join(letters[i])
            i += 1
    return decompressed_line
        

for line in file:
    dec_line =  decompress_file(line)
    length_of_decompressed_file += len(dec_line)

print("The length of the decompressed file is ", length_of_decompressed_file)