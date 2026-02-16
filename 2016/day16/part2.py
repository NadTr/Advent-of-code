from pathlib import Path
print("advent of code 2016 day 16")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read()

disk_input = file
disk_space = 35651584
correct_checksum = 0

def inverse(bin_str):
    result = ""
    for b in bin_str:
        result += "1" if b == "0" else "0"
    return result

def fill_disk(disk_input, disk_space):
    while len(disk_input) < disk_space:
        a= disk_input
        b = disk_input[::-1]
        b = inverse(b)
        disk_input = str(a) + "0" + b
    return disk_input[:disk_space]


def get_checksum(str):
    checksum = ""
    for i in range(0,len(str), 2):
        checksum += "1" if str[i] == str[i+1] else "0"
    return checksum


def get_correct_checksum(disk):
    input = disk
    checksum = ""
    while len(checksum)%2 == 0:
        checksum = get_checksum(input)
        input = checksum
        # print("checksum" ,checksum)
    return checksum


full_disk = fill_disk(disk_input, disk_space)
# print(full_disk)
correct_checksum = get_correct_checksum(full_disk)

print("The correct checksum is", correct_checksum)