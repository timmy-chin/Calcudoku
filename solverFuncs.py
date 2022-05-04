def get_cages():
    cage_list = []
    n = int(input('Number of Cages: '))
    for i in range(n):
        cage_elements = input(f'Cage Number {i}: ')
        cage_num = [int(float(x)) for x in cage_elements.split() if x.isdigit()]
        cage_list.append(cage_num)
    return cage_list


def check_rows_valid(puzzle):
    valid = [check_one_row(i, puzzle) for i in range(5)]
    return False not in valid


def check_one_row(row, puzzle):
    valid = [puzzle[row].count(i) < 2 for i in range(1, 6)]
    return False not in valid


def check_columns_valid(puzzle):
    valid = [check_one_column(i, puzzle) for i in range(5)]
    return False not in valid


def check_one_column(col, puzzle):
    column_list = [puzzle[i][col] for i in range(5)]
    valid = [column_list.count(i) < 2 for i in range(1, 6)]
    return False not in valid


def check_cages_valid(puzzle, cages):
    valid = [check_one_cage(cages[i], puzzle) for i in range(len(cages))]
    return False not in valid


def check_one_cage(cage_info, puzzle):
    cage = []
    target = cage_info[0]
    cell_num = cage_info[1]
    sum = 0
    for i in range(2, cell_num+2):
        cell = cage_info[i]
        row = cell//5
        col = cell - (5*row)
        sum += puzzle[row][col]
        cage.append(puzzle[row][col])
    full = 0 not in cage

    if full and sum != target:
        return False
    elif not full and sum >= target:
        return False
    else:
        return True

def check_valid(puzzle, cages):
    return check_rows_valid(puzzle) and check_columns_valid(puzzle) and check_cages_valid(puzzle, cages)




