from pathlib import Path
print("advent of code 2016 day 19")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    number = int(f.read())


elfs = {}
for i in range (1,number +1):
    elfs.update({i: 1})

# print(elfs)
presents_taken = False
while len(elfs) > 1:
    for elf in elfs:
        if elfs[elf] != 0:
            if not presents_taken :
                elfs[elf] += 1
            else:
                elfs[elf] = 0

            presents_taken = not presents_taken
        # print(elfs, elf, presents_taken)

    active_elfs =  dict(filter(lambda kv: kv[1] != 0, elfs.items()))
    # print(active_elfs)
    elfs = active_elfs



print("The last elf is ", next(iter(elfs)))