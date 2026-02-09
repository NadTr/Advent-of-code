print("advent of code 2017 day 4")

with open('./input.txt') as f:
    file = f.read().splitlines()

def is_password_valid(passphrase):
    passphrase = passphrase.split()
    already_checked = []
    for word in passphrase:
        if already_checked == []:
            already_checked += [word]
        else:
            add_word = False
            for i in range(len(already_checked)):
                word_to_check = already_checked[i]
                if len(word) == len(word_to_check):
                    all_letters_in_word = False
                    for letter in word:
                        if letter in word_to_check:
                            word_to_check = word_to_check.replace(letter,'',1)
                            all_letters_in_word = True
                            continue
                        else :
                            add_word = True
                            all_letters_in_word = False
                            break
                    if all_letters_in_word:
                        return False
                else:
                    add_word = True
                    continue
            if add_word:
                already_checked += [word]
    # print(" the passphrase is valid: ", passphrase)
    return True


valid_passwords = 0
for line in file:
    if is_password_valid(line):
        valid_passwords += 1

print("The number of valid password is", valid_passwords)