import re
print("advent of code 2015 day 12")

with open('./input.txt') as f:
    file = f.read()
 
numbers = re.findall('[-+]?\d+', file)
numbers = list(map(int, numbers))
total_sum = sum(numbers)

print("The total sum of all numbers is ", total_sum)
