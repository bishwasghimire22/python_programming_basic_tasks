# Create a program called sudoku_check_row. The program should have a function named row_ok that takes sudoku grid (matrix) and row index (int) as arguments.
#  You can suppose that each item on a row in the matrix is a digit between 0 and 9. Zero represents an empty square in a sudoku grid.
#  That is, there can be several zeros on a row until the sudoku is solved.
#  The row_ok function should return True if the row is ok.
# Otherwise, it should return False. NB! The function should not modify the sudoku grid.
# A row is ok if each of the digits between 1 and 9 appears zero or one times on the row.
#  The row is not ok if any of the digits between 1 and 9 appears more than once on the row.
#   In the sudoku grid below, the second row is not ok because the digit 2 appears twice on the row.
#  All the other rows are ok. NB! Please copy/paste the code of the main function below to your program.


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

    print(row_ok(sudoku, row_index=0))
    print(row_ok(sudoku, row_index=1))
    print(row_ok(sudoku, row_index=8))


if __name__ == "__main__":
    main()


def row_ok(sudoku, row_index):
    row = sudoku[row_index]
    digits = set()
    for num in row:
        if num != 0:
            if num in digits:
                return False
            digits.add(num)
    return True
