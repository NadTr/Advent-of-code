from pathlib import Path
print("advent of code 2020 day 2")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

valids_passwords = 0
for line in file:
    instructs, password = line.split(": ")
    range, char = instructs.split()
    range = range.split("-")
    nb_char =  password.count(char) 
    if nb_char >= int(range[0]) and nb_char <= int(range[1]):
        valids_passwords += 1

print("The number of valids passwords according to their policies is", valids_passwords)