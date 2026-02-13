from pathlib import Path
import hashlib
print("advent of code 2016 day 5")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    door_id = f.read()

password_length = 8
password_list = [" "] * password_length
print(password_list)
positions = []

def string_to_hex(string):
    hashed_pass = hashlib.md5(string.encode())
    return hashed_pass.hexdigest()


def next_letter(door_id, step):
    step = step
    while(True):
        result = string_to_hex(door_id + str(step))
        if result[0:5] == "00000" and result[5].isdigit():
            pos = int(result[5])
            if pos < password_length and pos not in positions:
                # print("The MD5 hash is ", result, step)
                return pos, result[6], step
        step += 1

step = 0

while len(positions) < password_length:
    (pos, letter, step) = next_letter(door_id, step + 1)
    positions += [pos]
    password_list[pos] = letter

password = "".join(password_list)

print("The password of the door", door_id,"is", password)