print("advent of code day 3")

with open('./day3.txt') as f:
    battery_line = f.read().splitlines()

output_total = 0

def biggest_voltage(battery_bank) :
    array_battery_bank = [int(digit) for digit in str(battery_bank)]
    first_digit = max(array_battery_bank[0: len(array_battery_bank)-1])
    index_max_number = array_battery_bank.index(first_digit)
    # print("Le plus grand chiffre est " + str(first_digit) + " à la position " + str(index_max_number))
    second_digit = max(array_battery_bank[index_max_number + 1: len(array_battery_bank)])
    biggest_voltage = int(str(first_digit)+str(second_digit))
    return biggest_voltage


for i in battery_line:
    output_total += biggest_voltage(int(i))
    


print("The total output joltage is " + str(output_total))


    