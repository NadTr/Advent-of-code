print("advent of code 2017 day 4")

with open('./input.txt') as f:
    file = f.read().splitlines()

def is_password_valid(passphrase):
    passphrase = passphrase.split()
    already_checked = []
    for word in passphrase:
        if word in already_checked:
            return False
        else:
            already_checked += [word]
        # print(already_checked)
    return True


valid_passwords = 0
for line in file:
    if is_password_valid(line):
        valid_passwords += 1

print("The number of valid password is", valid_passwords)