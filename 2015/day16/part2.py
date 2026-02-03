import re
print("advent of code 2015 day 16")

datas = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}
aunts = {}

with open('./input.txt') as f:
    file = f.read().splitlines()

for i in range(len(file)):
    line = re.sub(r'Sue (\d+): ', r'\1 \\ ', file[i])
    line = line.split("\\ ")
    items = line[1]. split(", ")
    aunts[line[0]]={}
    for item in items:
        item = item.split(": ")
        aunts[line[0]].update({item[0]:item[1]})

def is_aunt_corresponding(aunt,datas):
    for item in aunt:
        if item in datas:
            if item == "cats" or item == "trees":
                if int(aunt[item]) < datas[item]:
                    return False  
            elif item == "pomeranians" or item == "goldfish":
                if int(aunt[item]) > datas[item]:
                    return False  
            elif aunt[item] == str(datas[item]):
                # print("This aunt has the right number of ", item, datas[item])
                continue
            else:
                return False
    return True
            
for aunt in aunts:
    # print("Aunt number ", aunt)
    if is_aunt_corresponding(aunts[aunt],datas):
        aunt_number = aunt

print("The number of the aunt Sue that gave you the gift is ", aunt_number)
