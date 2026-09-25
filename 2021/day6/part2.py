from pathlib import Path
print("advent of code 2021 day 6")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().split(',')
    file = list(map(int, file))

days = 256
lanternfishes_counter = {}

for i in range (9):
    lanternfishes_counter.update({ i : file.count(i)})

for i in range(days):
    counter_to_zero = lanternfishes_counter[0]
    for k in lanternfishes_counter.keys():
        if k == 8 : continue
        lanternfishes_counter[k] = lanternfishes_counter[k+1]
    lanternfishes_counter[6] += counter_to_zero
    lanternfishes_counter[8] = counter_to_zero

# print(lanternfishes_counter)

print("The number of planternfish would there be after 80 days is ", sum(lanternfishes_counter.values()) )