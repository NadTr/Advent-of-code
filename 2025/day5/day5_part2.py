print("advent of code day 5")

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


# def analyze_range(fresh_range):
#     global ranges_analyzed
#     need_new_range = True
#     val = fresh_range
#     (min_range, max_range) = val.split("-")
#     (min_range, max_range) = (int(min_range), int(max_range))
#     length = (max_range - min_range) + 1
#     # print("total of fresh ingredients in range " + str(min) +" - " + str(max)+" is " + str(length))

#     if ranges_analyzed != []:
#         for index in range(len(ranges_analyzed)):
#             (i, j) = ranges_analyzed[index].split("-")
#             (i, j) = (int(i), int(j))
#             end_range_min = i
#             end_range_max = j
#             if min_range >= i and min_range <= j:
#                 length -= min_range - i + 1
#                 print (min, max, i, j, length)
#                 end_range_min = min(min_range,i)
#                 need_new_range = False

#             if max_range <= j and max_range >= i :
#                 length -= j - max_range+1
#                 # print (min, max, i, j, length)
#                 # end_range_max = max(j,max_range)
#                 end_range_max = max_range
#                 need_new_range = False
#             ranges_analyzed[index] = str(end_range_min) +"-"+str(end_range_max)
#             print(ranges_analyzed[index])
#     if need_new_range:
#         ranges_analyzed += [fresh_range]
#     print("total of fresh ingredients added " + str(length))
#     return length

# for fresh_range in fresh_ranges:
#     result = analyze_range(fresh_range)
#     number_of_fresh_ingredients += result


print("There are "+ str(number_of_fresh_ingredients)+" fresh ingredients in ranges")


    