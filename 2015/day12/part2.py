import re, json
print("advent of code 2015 day 12")

with open('./input.txt') as f:
    file = f.read()

json_file = json.loads(file)

def hook(dict):
  if "red" not in dict.values(): return dict
correct_file = str(json.loads(file, object_hook=hook))

numbers = re.findall('[-+]?\d+', correct_file)
numbers = list(map(int, numbers))
total_sum = sum(numbers)

print("The total sum of all numbers is ", total_sum)