from solverFuncs import *

# cages = [[5, 2, 0, 5], [8, 3, 1, 2, 6], [8, 2, 3, 8], [6, 3, 4, 9, 14], [13, 3, 7, 12, 13], [5, 2, 10, 15], [14, 4, 11, 16, 20, 21], [6, 3, 17, 18, 22], [10, 3, 19, 23, 24]]
# cages = [[9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13], [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16], [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]
# cages = [[7, 3, 0, 1, 2], [12, 4, 3, 4, 8, 9], [17, 6, 5, 7, 10, 11, 12, 13], [5, 1, 6], [11, 3, 14, 19, 24], [7, 2, 15, 20], [5, 3, 16, 17, 21], [11, 3, 18, 22, 23]]
# cages = [[4, 3, 0, 1, 6], [8, 3, 2, 7, 12], [14, 3, 3, 4, 8], [15, 4, 5, 10, 11, 15], [14, 6, 9, 13, 14, 18, 19, 24], [11, 3, 16, 20, 21], [9, 3, 17, 22, 23]]

# cages = []
# with open('test2.txt', 'r') as file:
#     for word in file:
#         cage = [int(float(x)) for x in word.split() if x.isdigit()]
#         cages.append(cage)
# print(cages)

puzzle = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]

cages = get_cages()

checks = 0
backtrack = 0
col = 0
row = 0
while row < 5:
    if puzzle[row][col] == 5:       #backtrack
        puzzle[row][col] = 0
        if col == 0:
            row -= 1
            col = 4
        else:
            col -= 1
        backtrack += 1
        continue
    puzzle[row][col] += 1
    checks += 1

    if check_valid(puzzle, cages) and puzzle[row][col] <= 5:                #Move to Next Cell
        col += 1
        if col >= 5:
            col = 0
            row += 1
    elif not check_valid(puzzle, cages) and puzzle[row][col] < 5:           #Continue Incrementing
        continue
    elif not check_valid(puzzle, cages) and puzzle[row][col] >= 5:          #backtrack
        puzzle[row][col] = 0
        if col == 0:
            row -= 1
            col = 4
        else:
            col -= 1
        backtrack += 1

for i in puzzle:
    print(i)
print(f'Checks: {checks} Backtrack: {backtrack}')
