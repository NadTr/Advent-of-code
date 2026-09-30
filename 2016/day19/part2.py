from pathlib import Path
print("advent of code 2016 day 19")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    number = int(f.read())

i = 1
while i * 3 < number:
    i *= 3

print("The last elf is ", number - i)