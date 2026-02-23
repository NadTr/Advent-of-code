from pathlib import Path
print("advent of code 2019 day 4")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().split("-")

def is_password_valid(password):
    double = False
    length_double = 1
    increase = True
    for i in range(len(password) - 1):
        if password[i] == password[i+1]:
            length_double += 1
            if i == len(password) -2 and length_double == 2:
                double = True
        else:
            if length_double == 2:
                double = True
            length_double = 1
        if int(password[i]) > int(password[i+1]):
            increase = True
            return False
    if double and increase:
        return True
    else: return False


valid_passwords = 0
for password in range(int(file[0]), int(file[1]) +1):
    if is_password_valid(str(password)):
        valid_passwords += 1

print("The number of different passwords within the range given is", valid_passwords)