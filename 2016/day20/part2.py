from pathlib import Path
print("advent of code 2016 day 20")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

for i in range(len(file)):
    range = file[i].split("-")
    file[i] = [int(range[0]), int(range[1])]

sorted_ranges = sorted(file)

merged_ranges = []
for start, end in sorted_ranges:
    if merged_ranges and start <= merged_ranges[-1][1] + 1:
        merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], end))
    else:
        merged_ranges.append((start, end))

number_of_ip = 4294967295 - sum(end - start + 1 for start, end in merged_ranges) + 1


print("The number of authorised ip is ", number_of_ip)