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
    if (password[int(range[0]) -1] == char) ^ (password[int(range[1]) -1] == char):
        valids_passwords += 1

print("The number of valids passwords according to the new interpretation of their policies is", valids_passwords)