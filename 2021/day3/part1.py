from pathlib import Path
print("advent of code 2021 day 3")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()
    for i in range(len(file)):
        file[i] =  list(file[i])

gamma_rate = ''
epsilon_rate = ''
for i in range(len(file[0])):
    number_of_zeroes = 0
    number_of_ones = 0
    for j in range(len(file)):
        if file[j][i] == '0':
            number_of_zeroes += 1
        else:
            number_of_ones += 1
    gamma_rate += '1' if number_of_ones > number_of_zeroes else '0'
    epsilon_rate += '1' if number_of_ones <= number_of_zeroes else '0'


print("The power consumption of the submarine is",  int(gamma_rate, 2) * int(epsilon_rate, 2))