from pathlib import Path
import hashlib, re
print("advent of code 2016 day 14")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    salt = f.read()

def stretched_hash(hash):
    for i in range (2017):
        hashed_pass = hashlib.md5(hash.encode())
        hash = hashed_pass.hexdigest()
    return hash


def next_letter(salt, index):
    index = index
    while(True):
        result = thousand_hashes[0]
        del thousand_hashes[0]
        thousand_hashes.append(stretched_hash(salt + str(index + 1000)))
        triplets = re.search(r'(.)\1\1', result)
        if triplets != None:
            sequence = triplets.group()[0] * 5
            for find_occurence in thousand_hashes:
                # find_occurence = stretched_hash(salt + str(index + i))
                if re.search(sequence, find_occurence) != None:
                    # print("The MD5 hash is ", result, index, find_occurence,index +thousand_hashes.index(find_occurence))
                    return result, index
        index += 1

index = 0
thousand_hashes = []
for i in range(1000):
    thousand_hashes.append(stretched_hash(salt + str(i)))

for i in range(64):
    (hash, index) = next_letter(salt, index)
    index += 1

print("The index that produces the 64th one-time pad key of", salt,"is", index - 1)