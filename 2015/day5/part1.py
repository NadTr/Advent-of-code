from pathlib import Path
print("advent of code 2015 day 5")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
     file = f.read().splitlines()

number_of_nice_strings = 0
vowels = ["a", "e", "i", "o", "u"]
to_exclude = ["ab", "cd", "pq", "xy"]

def is_string_nice(string):
    vowel_number = 0
    double_letters_exist = False
    for i in range(len(string)):
        if string[i] in vowels:
            vowel_number += 1
        if not double_letters_exist and i < len(string) -1 and string[i] == string[i+1]:
            double_letters_exist = True
        if i < len(string) -1 and string[i:i+2] in to_exclude:
            return False
    
    if vowel_number >= 3 and double_letters_exist:
        return True
    else: 
        return False

for line in file : 
    if is_string_nice(line):
        number_of_nice_strings += 1

print("The number of nice strings is ", number_of_nice_strings)
