print("advent of code day 3")

with open('./day3.txt') as f:
    battery_line = f.read().splitlines()

output_total = 0

def biggest_number_in_array(array, min_index, max_index):
    return max(array[min_index: max_index])

def biggest_voltage(battery_bank) :
    biggest_voltage = ""
    index_max_number = 0
    array_battery_bank = [int(digit) for digit in str(battery_bank)]
    for j in range(12):
        result = biggest_number_in_array(array_battery_bank, 0, len(array_battery_bank)-(11-j))
        biggest_voltage += str(result)
        index_max_number = array_battery_bank.index(result)
        array_battery_bank = array_battery_bank[(index_max_number+1):]
        print("Le plus grand chiffre est " + str(result) + " à la position " + str(index_max_number))
    print(biggest_voltage)
    return int(biggest_voltage)


for i in battery_line:
    output_total += biggest_voltage(int(i))
    


print("The total output joltage is " + str(output_total))


    