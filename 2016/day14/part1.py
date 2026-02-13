from pathlib import Path
import hashlib, re
print("advent of code 2016 day 14")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    salt = f.read()

def string_to_hex(string):
    hashed_pass = hashlib.md5(string.encode())
    return hashed_pass.hexdigest()

def next_letter(salt, index):
    index = index
    while(True):
        result = string_to_hex(salt + str(index))
        triplets = re.search(r'(.)\1\1', result)
        if triplets != None:
            sequence = triplets.group()[0] * 5
            # print(triplets, sequence)
            # return result, index
            for i in range(1, 1001):
                find_occurence = string_to_hex(salt + str(index + i))
                if re.search(sequence, find_occurence) != None:
                    print("The MD5 hash is ", result, index, find_occurence )
                    return result, index
        index += 1

index = -1
for i in range(64):
    (hash, index) = next_letter(salt, index + 1)

print("The index that produces the 64th one-time pad key of", salt,"is", index)