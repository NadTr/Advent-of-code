from pathlib import Path
print("advent of code 2018 day 2")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
     file = f.read().splitlines()

def find_One_letter_differences():
    for index in range(len(file[0])):
        for box in range(len(file)):
            new_box= file[box][0:index] + file[box][index + 1:]
            for other_box in range(box +1, len(file)):
                    other_new_box= file[other_box][0:index] + file[other_box][index + 1:]
                    if new_box == other_new_box:
                        return new_box
               
letters_in_common = find_One_letter_differences()

print("The letters are common between the two correct box IDs is", letters_in_common)