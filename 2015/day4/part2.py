from pathlib import Path
import hashlib
print("advent of code 2015 day 4")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read()

def string_to_hex(string):
    hexa_tr = hashlib.md5(string.encode())
    return hexa_tr.hexdigest()
    
found_hash = False
step = 1
while(not found_hash):
    result = string_to_hex(file + str(step))
    if result[0:6] == "000000":
        print("The MD5 hash is ", result, step)
        found_hash = True
    step += 1

