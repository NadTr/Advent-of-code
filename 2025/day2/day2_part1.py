print("advent of code day 2")

with open('./day2.txt') as f:
    ranges = f.read().split(",")
sum_of_all_invalid_ids = 0

def is_id_invalid(id):
    id_str = str(id)
    id_length = len(id_str)

    if id_length % 2 == 0:
        if (id_str[:int(id_length/2)] == id_str[int(id_length/2):]):
            print("id length " + str(id_length))
            print("id invalid: " + id_str)
            return True
    else:
        return False

def identify_invalid_id(min, max):
    tmp_sum = 0
    for id in range(min, max + 1):
        if(is_id_invalid(id)):
            tmp_sum += id
    return tmp_sum

for id_range in ranges:
    (min, max) = id_range.split("-")
    sum_of_all_invalid_ids += identify_invalid_id(int(min), int(max))


print("the sum of all invalid id is " + str(sum_of_all_invalid_ids))


    