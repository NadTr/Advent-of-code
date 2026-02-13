from pathlib import Path
import hashlib
print("advent of code 2016 day 4")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    door_id = f.read()

def string_to_hex(string):
    hashed_pass = hashlib.md5(string.encode())
    return hashed_pass.hexdigest()

def next_letter(door_id, step):
    step = step
    while(True):
        result = string_to_hex(door_id + str(step))
        if result[0:5] == "00000":
            # print("The MD5 hash is ", result, step)
            return result[5], step
        step += 1

password = ""
step = 0
while len(password) < 8:
    (letter, step) = next_letter(door_id, step + 1)
    password += str(letter)




print("The password of the door", door_id,"is", password)