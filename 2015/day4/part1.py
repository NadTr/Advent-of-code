import hashlib
print("advent of code 2015 day 4")

with open('./input.txt') as f:
    file = f.read()

def string_to_hex(string):
    hexa_tr = hashlib.md5(string.encode())
    return hexa_tr.hexdigest()
    
found_hash = False
step = 1
while(not found_hash):
    result = string_to_hex(file + str(step))
    # print("result of hash ", file, step, " is = ", result )
    if result[0:5] == "00000":
        print("The MD5 hash is ", result, step)
        found_hash = True
    step += 1

