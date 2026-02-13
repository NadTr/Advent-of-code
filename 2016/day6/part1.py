from pathlib import Path
print("advent of code 2016 day 6")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
     file = f.read().splitlines()

results = []
password = ""

for i in range(len(file[0])):
    dictio = {}
    results += [dictio]

def add_letter_to_result(col, letter):
    # print(col, letter)
    if letter in results[col]:
        results[col][letter] += 1
    else:
        results[col].update({letter: 1}) 
    

for line in file:
    letters = list(line)
    for i in range(len(letters)):
        add_letter_to_result(i, letters[i])

for result in results:
    res = max(result, key=result.get)
    password += res


print("The password is ", password)