import string, re
print("advent of code 2015 day 11")
alphabet =  string.ascii_lowercase
isNotValid = True
with open('./input.txt') as f:
    password = f.read()


def increment_letter(letter):
    if letter == "z":
        # print("passage de z à a")
        return "a", True
    elif letter == "h" or letter == "k" or letter == "n":
        return alphabet[ alphabet.index(letter) + 2], False

    else : 
        return alphabet[ alphabet.index(letter) + 1], False
 
def increment_password(password):
    new_password = list(password)
    index = len(password)-1
    change_index = True

    while (index > 0 and change_index):
        (new_password[index], change_index) = increment_letter(new_password[index])
        if change_index:
            index -= 1
    # print(new_password)
    # return new_password
    return "". join( letter for letter in new_password)

def is_password_valid(password):
    contain_3_straight_letters = False
    contain_double_letters = 0
    if "i" in password or "l" in password or "o" in password:
        # print("The password ", password, " contains one of these letters :  i, l, o")
        return True
    
    for i in range(len(alphabet)) :
        letter = alphabet[i]
        if letter + letter in password:
            contain_double_letters += 1
            # print(password, " contains two times the letters ", alphabet[i])
        if i < 24 and alphabet[i:i+3] in password:
            contain_3_straight_letters = True
            # print(password, " contains 3 straight letters ", alphabet[i:i+3])
    if contain_3_straight_letters and contain_double_letters >= 2:
        return False
    else:
        return True
    
print(password)
if "i" in password or "l" in password or "o" in password:
    for i in range(len(password)):
        if password[i] == "i" or password[i] == "l" or password[i] == "o":
            (new_letter, bool) =increment_letter(password[i])
            # password_end = ("a" for _ in range(i, len(password)))
            password = password[0:i] + new_letter + "a" * (len(password)-i)
            break
print(password)
new_password = list(password)

while(isNotValid):
    new_password = increment_password(password)
    isNotValid = is_password_valid(new_password)
    password = new_password


print("The new valid password is ", new_password)
