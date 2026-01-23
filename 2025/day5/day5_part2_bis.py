with open('./day5.txt') as f:
    file = f.read().split("\n\n")
    fresh_ranges = file[0].splitlines()
    for index in range(len(fresh_ranges)):
        splited = fresh_ranges[index].split("-") 
        fresh_ranges[index] = [int(splited[0]),int(splited[1])]
        # print(fresh_ranges)
sorted_ranges = sorted(fresh_ranges)

merged_ranges = []
for start, end in sorted_ranges:
    # print(merged)
    if merged_ranges and start <= merged_ranges[-1][1] + 1:
        # Overlapping or adjacent - merge with last range
        merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], end))
    else:
        # No overlap - add new range
        merged_ranges.append((start, end))

# Calculate total count from merged ranges
number_of_fresh_ingredients = sum(end - start + 1 for start, end in merged_ranges)
print(number_of_fresh_ingredients)
print("There are "+ str(number_of_fresh_ingredients)+" fresh ingredients in total")
