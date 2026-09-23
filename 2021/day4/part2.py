from pathlib import Path
print("advent of code 2021 day 4")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

num_to_draw = list(map(int, file[0].split(',')))
number_of_boards = len(file[2:])//6
boards = {}

for i in range(1, (number_of_boards + 2)):
    start = (i - 1) * 6 + 1
    board = []
    for line in range(1, 6):
        board.append(list(map(int, file[start + line].split())))
    boards.update({i : board})

unwon_boards = list(boards.values())

def print_boards():
    for k, v in boards.items():
        print(k)
        for l in v:
            print(l)


def is_number_in_board(num):
    for i in range(1, number_of_boards + 2):
        board_to_check = boards[i]
        for line in range(len(board_to_check)):
            if num in board_to_check[line]:
                board_to_check[line][board_to_check[line].index(num)] = 'X'
        boards.update({i : board_to_check})


def check_bingo(b):
    cols = [[] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            cols[j].append(b[i][j])

    for i in range(5):
        if b[i] == ['X','X','X','X','X']:
            return True
        if cols[i] == ['X','X','X','X','X']:
            return True
        
    return False


def play():
    for num in num_to_draw:
        is_number_in_board(num)
        if num >= 5:
            for b in boards.values():
                if b not in unwon_boards: continue
                if check_bingo(b):
                    if len(unwon_boards) == 1:
                        return b, num
                    unwon_boards.remove(b)
            
                
winner, last_number = play()           
score = 0
for i in range(5):
    for j in range(5):
        score += 0 if winner[i][j] == 'X' else winner[i][j]

print("The last board's final score is", score * last_number)