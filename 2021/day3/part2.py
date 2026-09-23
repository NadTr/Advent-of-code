from pathlib import Path
print("advent of code 2021 day 3")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()
    for i in range(len(file)):
        file[i] =  list(file[i])

def find_maj_bit_at(index, arr):
    number_of_zeroes = 0
    number_of_ones = 0

    for j in range(len(arr)):
        if arr[j][index] == '0':
            number_of_zeroes += 1
        else:
            number_of_ones += 1

    return number_of_ones >= number_of_zeroes


def find_rate(arr, majority):
    result = ''

    for i in range(len(file[0])):
        result += '1' if find_maj_bit_at(i, arr) == majority else '0'
        l = len(arr)
        new_list = []

        for j in range(len(arr)):
            if arr[j][:i+1] == list(result):
                new_list.append(arr[j])

        arr = new_list
        if len(new_list) == 1:
            return ''.join(new_list[0])
               
    return result


oxygene_generator_rate = find_rate(file, True)
CO2_scrubber_rate = find_rate(file, False)

print("The life support rating of the submarine is",  int(oxygene_generator_rate, 2) * int(CO2_scrubber_rate, 2))