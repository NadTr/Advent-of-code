from pathlib import Path
import re
print("advent of code 2016 day 4")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

sum_of_valid_rooms = 0

def return_name_to_dict(name):
    results = {}
    letters=list(name)
    for letter in letters:
        if letter in results:
            results[letter] += 1
        else:
            results.update({letter: 1}) 
    return results


def is_room_valid(name, checksum):
    name = re.sub("-", "", name)
    name_letters = return_name_to_dict(name)
    sorted_letters = dict(sorted(name_letters.items(), key=lambda item:item[1], reverse=True))
    keys_found = {}

    for key, value in sorted_letters.items():
        if value in keys_found:
            keys_found[value] += key
        else:
            keys_found.update({value:key}) 

    result =""
    for k, v in keys_found.items():
        result += ''.join(sorted(v))

    if result[:5] == checksum:
        return True
    else: 
        return False


for line in file:
    room = line.split("[")
    if is_room_valid(room[0][:-4],room[1][:-1]):
        # print(int(room[0][-3:]))
        sum_of_valid_rooms += int(room[0][-3:])

print("The number of valid rooms is ", sum_of_valid_rooms)