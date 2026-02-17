from pathlib import Path
print("advent of code 2017 day 17")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
     input = int(f.read())

circular_buffer = [0]
spin_number = 349
end_range = 2017
index = 0

for i in range(1, end_range + 1):
    index = (index + spin_number)%len(circular_buffer) +1
    circular_buffer.insert(index, i)

result = circular_buffer[(circular_buffer.index(2017) + 1) %len((circular_buffer))]

print("The order the programs standing after their dance is", result)