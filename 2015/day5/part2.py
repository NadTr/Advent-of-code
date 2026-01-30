print("advent of code 2015 day 5")

with open('./input.txt') as f:
    file = f.read().splitlines()

number_of_nice_strings = 0
pair_of_letter = []

def is_string_nice(string):
    double_strings_of_2_letters_exist = False
    double_sandwich_letters_exist = False
    for i in range(len(string)):
        if not double_sandwich_letters_exist and i < len(string) -2 and string[i] == string[i+2]:
            double_sandwich_letters_exist = True
        if not double_strings_of_2_letters_exist and i < len(string) -3:
            double_letters = string[i]+string[i+1]
            for j in range(i+2, len(string) - 1):
                if string[j]+string[j+1] ==  double_letters:
                    double_strings_of_2_letters_exist = True

    if double_sandwich_letters_exist and double_strings_of_2_letters_exist:
        return True
    else: 
        return False

for line in file : 
    if is_string_nice(line):
        number_of_nice_strings += 1

print("The number of nice strings is ", number_of_nice_strings)
