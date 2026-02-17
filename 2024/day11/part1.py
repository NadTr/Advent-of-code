from pathlib import Path
print("advent of code 2024 day 11")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:       
    file = f.read()
# stones = list(map(int, file.split()))
stones = file.split()
stones_copy = stones[:]
blinks = 25
print( stones_copy)

for i in range(1, blinks +1):
    index_copy = 0
    for index in range(len(stones_copy)):
        stone = stones[index]
        # print(stone)
        if stone == "0":
            stones_copy[index_copy] = "1"
            index_copy += 1
        elif len(stone) != 0 and  len(stone)%2 == 0:
            new_stones = [str(int(stone[:len(stone)//2])), str(int(stone[len(stone)//2:]))]
            # print(new_stones)
            stones_copy[index_copy] = new_stones[0]
            stones_copy.insert(index_copy+1, new_stones[1])
            index_copy += 2
        else: 
            stones_copy[index_copy] = str(2024 * int(stone))
            index_copy += 1
    # print(i, stones_copy)
    stones = stones_copy[:]


# print(stones_copy)
print("The number of stones will you have after blinking 25 times is", len(stones_copy))
