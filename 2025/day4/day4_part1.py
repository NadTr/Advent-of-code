print("advent of code day 4")

with open('./day4.txt') as f:
    storage_line = f.read().splitlines()

new_storage_line= storage_line
number_of_rolls_accessible = 0
number_of_rounds = 0
run_successful = True

def number_of_rolls_around(mat, row, col) :
    number_of_rolls_around = 9
    if mat[row][col]== "@":
        number_of_rolls_around = 0
        # print("le symbole en ligne " + str(row) + " et colonne " + str(col) + " est: "+str(mat[row][col]))
        for i in range(0 if row <= 1 else (row -1), (row + 2) if row < len(mat) - 1 else row + 1):
            for j in range(0 if col <= 1 else (col -1), (col + 2) if col < len(mat[i]) - 1 else  col+ 1):
                # print("row " + str(i) +" col " + str(j))
                if (i, j) != (row, col) and mat[i][j] == "@":
                    # print(mat[i][j])
                    number_of_rolls_around += 1
                    # print("le symbole en ligne " + str(row) + " et colonne " + str(col) + " a: "+str(number_of_rolls_around) + " rolls autour")
    # print("le symbole en ligne " + str(row) + " et colonne " + str(col) + " a: "+str(number_of_rolls_around) + " rolls autour")
    # print(number_of_rolls_around)
    return number_of_rolls_around


for i in range(len(storage_line)):
    new_storage_line[i] = list(storage_line[i])

# number_of_rolls_around(storage_line,9,9)
# number_of_rolls_around(storage_line,2,4)
def round_to_remove_rolls(new_storage_line):
    rolls_to_remove_in_run = []
    global number_of_rolls_accessible 
    for i in range(len(new_storage_line)):
        for j in range(len(new_storage_line[i])):
            if new_storage_line[i][j]== "@":
                result = number_of_rolls_around(new_storage_line,i,j)
                if result < 4:
                    number_of_rolls_accessible += 1
                    # print("le symbole en ligne " + str(i) + " et colonne " + str(j) + " est accessible")
                    rolls_to_remove_in_run += [i,j]
    # print("There are "+ str(number_of_rolls_accessible)+" rolls of paper that can be accessed by a forklift ")
    return rolls_to_remove_in_run
    
# while( another_round):
    # another_round = round_to_remove_rolls()
def another_round():
    rolls_to_remove = round_to_remove_rolls(new_storage_line)
    # print(rolls_to_remove)
    if rolls_to_remove != []:
        global number_of_rounds
        number_of_rounds += 1
        for i in range(0, len(rolls_to_remove), 2):
            # print(roll_position)
            new_storage_line[rolls_to_remove[i]][rolls_to_remove[ i + 1]] = "x"
            # print("roll in col " +str(rolls_to_remove[i])+ " and row " +str(rolls_to_remove[i + 1])+ " has been removed")
    return rolls_to_remove

while(run_successful):
    # another_round()
    number_of_rounds +=1
    run_successful = True if another_round() != [] else False


print("There are "+ str(number_of_rolls_accessible)+" rolls of paper that can be accessed by a forklift ")
print("There are "+ str(number_of_rounds)+" round successful ")


    