from pathlib import Path
import re

print("advent of code 2024 day 3")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
      file = f.read()

sum_of_multiplications = 0

pattern_to_delete = r'don\'t\(\).*?do\(\)'
file = re.sub(pattern_to_delete,'', file, flags=re.DOTALL)
file2 = file.split("don\'t()")

pattern_to_find = r'mul\(\d+,\d+\)'  
result_table = re.findall(pattern_to_find, file2[0])

for line in result_table:
    nums = line[4:-1].split(",")
    sum_of_multiplications += int(nums[0]) * int(nums[1])

print("The total sum of the multiplications is", sum_of_multiplications)
