import re

print("advent of code 2024 day 3")

global sum_of_multiplications
sum_of_multiplications = 0
  

with open('./day3.txt') as f:
    file = f.read()

pattern = r'mul\(\d+,\d+\)'  
result_table = re.findall(pattern, file)

for line in result_table:
    nums = line[4:-1].split(",")
    sum_of_multiplications += int(nums[0]) * int(nums[1])

print("The total sum of the multiplications is  " + str(sum_of_multiplications))
