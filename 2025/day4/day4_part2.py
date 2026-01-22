print("advent of code day 4")

with open('./day4.txt') as f:
    storage_line = f.read().splitlines()

number_of_rolls_accessible = 0

def number_of_rolls_around(mat, row, col) :
    number_of_rolls_around = 9
    if mat[row][col]== "@":
        number_of_rolls_around = 0
        print("le symbole en ligne " + str(row) + " et colonne " + str(col) + " est: "+str(mat[row][col]))
        for i in range(0 if row <= 1 else (row -1), (row + 2) if row < len(mat) - 1 else row + 1):
            for j in range(0 if col <= 1 else (col -1), (col + 2) if col < len(mat[i]) - 1 else  col+ 1):
                # print("row " + str(i) +" col " + str(j))
                if (i, j) != (row, col) and mat[i][j] == "@":
                    # print(mat[i][j])
                    number_of_rolls_around += 1
                    # print("le symbole en ligne " + str(row) + " et colonne " + str(col) + " a: "+str(number_of_rolls_around) + " rolls autour")
    print("le symbole en ligne " + str(row) + " et colonne " + str(col) + " a: "+str(number_of_rolls_around) + " rolls autour")
    # print(number_of_rolls_around)
    return number_of_rolls_around


for i in range(len(storage_line)):
    storage_line[i] = list(storage_line[i])

# number_of_rolls_around(storage_line,9,9)
# number_of_rolls_around(storage_line,2,4)

for i in range(len(storage_line)):
    for j in range(len(storage_line[i])):
        if storage_line[i][j]== "@":
            result = number_of_rolls_around(storage_line,i,j)
            if result < 4:
                number_of_rolls_accessible += 1
                print("le symbole en ligne " + str(i) + " et colonne " + str(j) + " est accessible")
    


print("There are "+ str(number_of_rolls_accessible)+" rolls of paper that can be accessed by a forklift ")


    