print("advent of code day 2")

with open('./day2.txt') as f:
    ranges = f.read().split(",")
sum_of_all_invalid_ids = 0

def is_repetitive(id_str, number_of_repetitions):
    start = 0
    sample_size = len(id_str)//number_of_repetitions
    # print("id: " + str(id_str) + " repet: "+ str(number_of_repetitions ) + " size: "+ str(sample_size))
    if sample_size == 1:
        for ind in range(number_of_repetitions - 1):
            i = ind * sample_size
            j = (ind + 1) * sample_size
            # print(id_str[i] )
            if id_str[i] != id_str[j]:
                return False
    else:
        for ind in range(number_of_repetitions - 1):
            i = ind * sample_size
            j = (ind + 1) * sample_size
            # print(id_str[j : j + sample_size] )
            if id_str[i :j] != id_str[j:j + sample_size]:
                return False
    return True


def is_id_invalid(id):
    id_str = str(id)
    id_length = len(id_str)

    for i in range(2,  id_length+1):
        if id_length % i == 0:
            if (is_repetitive(id_str, i)):
                # print("id length " + str(id_length) + " i: " + str(i))
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


    