# Create a program called sudoku_check_grid. The program should have a function named grid_ok that takes sudoku grid (matrix) as argument.
#  The function should use the functions from the three previous sudoku exercises to determine whether the complete sudoku grid is ok.
# The grid_ok function should check each of the nine rows, nine columns, and  nine 3x3 blocks in the sudoku grid.
# If all of them are ok, the function should return True.
#  Otherwise, the function should return False.
#  NB! First, copy/paste the functions (row_ok, column_ok, and block_ok) from your previous exercise solutions to this program.
#  Then copy/paste the code of the main function below to your program. Finally, write the grid_ok function.


def block_ok(sudoku, row_index, column_index):
    digits = set()
    if row_index % 3 != 0 or column_index % 3 != 0:
        return False
    for i in range(3):
        for j in range(3):
            num = sudoku[row_index + i][column_index + j]
            if num != 0:
                if num in digits:
                    return False
                digits.add(num)
    return True


def column_ok(sudoku, col_index):
    digits = set()
    for row in sudoku:
        if row[col_index] != 0:
            if row[col_index] in digits:
                return False
            digits.add(row[col_index])

    return True


def row_ok(sudoku, row_index):
    row = sudoku[row_index]
    digits = set()
    for num in row:
        if num != 0:
            if num in digits:
                return False
            digits.add(num)
    return True


def grid_ok(sudoku):
    for i in range(9):
        if not row_ok(sudoku, i):
            return False
        if not column_ok(sudoku, i):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not block_ok(sudoku, i, j):
                return False
    return True


def main():
    sudoku_1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
    ]
    sudoku_2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1],
    ]

    print(grid_ok(sudoku_1))  # False
    print(grid_ok(sudoku_2))  # True


if __name__ == "__main__":
    main()
