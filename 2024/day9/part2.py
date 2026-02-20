from pathlib import Path
print("advent of code 2024 day 9")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:       
    file = list(f.read())

disk = []

def fill_disk(disk_map):
    global disk
    for index in range(len(disk_map)):
        if int(disk_map[index]) != 0:
            space = '.' if (index + 1)%2 ==0 else str(index//2)
            for j in range(int(disk_map[index])):
                disk.append(space)


def rearrange_disk():
    global disk
    index = len(disk) - 1
    while index >= 0:
        if disk[index] == '.':
            index -= 1
            continue
        else:
            file_size = disk.count(disk[index])
            empty_space =["."] *file_size
            for i in range(index):
                if disk[i:i+file_size] == empty_space:
                    for a in range(i,i+file_size):
                        disk[a] = disk[index]
                    for b in range(index - file_size + 1, index + 1):
                        disk[b] = "."
                    break
                else: continue

            index -= file_size
    return disk


def calculate_checksum():
    checksum = 0
    for i in range(len(disk)):
        checksum +=  0 if disk[i] == "." else i * int(disk[i])
    return checksum


fill_disk(file)

rearrange_disk()

checksum = calculate_checksum()

print("The resulting filesystem checksum is", checksum)
