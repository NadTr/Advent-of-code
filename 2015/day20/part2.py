from pathlib import Path
import math
print("advent of code 2015 day 20")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    target = int(f.read())

house_number = 0
house_target = None

while not house_target:
    house_number += 1
    
    small_divisors = [i for i in range(1, int(math.sqrt(house_number)) + 1) if house_number % i == 0]
    large_divisors = [house_number / d for d in small_divisors if house_number != d * d]   

    first_50_divisors = (div for div in (small_divisors + large_divisors) if house_number/ div <= 50)

    if sum(first_50_divisors) * 11 >= target:
        house_target = house_number

print("The lowest house number that obtain", target," presents is ", house_target)