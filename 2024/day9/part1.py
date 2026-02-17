from pathlib import Path
print("advent of code 2024 day 9")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:       
    file = list(f.read())

disk = []
checksum = 0

def fill_disk(disk_map):
    for index in range(len(disk_map)):
        # print(index, disk_map[index])
        # index = int(index)
        for j in range(int(disk_map[index])):
            space = '.' if (index + 1)%2 ==0 else str(index//2)
            disk.append(space)


def rearrange_disk():
    while True:
        symbol = disk[-1]
        if symbol == '.':
            del disk[-1]
        elif '.' in disk:
            del disk[-1]
            disk[disk.index('.')] = symbol
        else: return


def calculate_checksum():
    global checksum
    for i in range(len(disk)):
        checksum += i * int(disk[i])

fill_disk(file)
rearrange_disk()
calculate_checksum()

print("The resulting filesystem checksum is", checksum)
