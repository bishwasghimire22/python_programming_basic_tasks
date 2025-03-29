# Create a program called sudoku_check_column. The program should have a function named column_ok that takes sudoku grid (matrix) and column index (int) as arguments.
#  The column_ok function should return True if the row is ok. Otherwise, it should return False.
#  NB! The function should not modify the sudoku grid.
#  A column is ok if each of the digits between 1 and 9 appears zero or one times in the column.
# The column is not ok if any of the digits between 1 and 9 appears more than once in the column.
#   In the sudoku grid below, the first column is not ok because the digit 2 appears twice in the column.
#  All the other columns are ok. NB! Please copy/paste the code of the main function below to your program.


def main():
    sudoku = [
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
    print(column_ok(sudoku, column_index=0))
    print(column_ok(sudoku, column_index=1))
    print(column_ok(sudoku, column_index=8))


if __name__ == "__main__":
    main()


def column_ok(sudoku, col_index):
    digits = set()
    for row in sudoku:
        if row[col_index] != 0:
            if row[col_index] in digits:
                return False
            digits.add(row[col_index])

    return True
