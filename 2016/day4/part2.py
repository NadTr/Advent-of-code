import re, string
print("advent of code 2016 day 4")

with open('./input.txt') as f:
    file = f.read().splitlines()

alphabet =  string.ascii_lowercase

def increment_letter(letter):
    if letter == "z":
        # print("passage de z à a")
        return "a"
    else : 
        return alphabet[ alphabet.index(letter) + 1]
 
 
def decrypt_room_name(name, turns):
    name = re.sub("-", " ", name)
    decrypted_name = ""
    for letter in name:
        if letter != " ":
            for i in range(turns):
                letter = increment_letter(letter)
        decrypted_name += letter
    return decrypted_name


for line in file:
    room = line.split("[")
    mod = int(room[0][-3:])%26
    decrypted_name =decrypt_room_name(room[0][:-4],mod)
    if "north" in decrypted_name:
        print(decrypted_name, room[0][-3:])
