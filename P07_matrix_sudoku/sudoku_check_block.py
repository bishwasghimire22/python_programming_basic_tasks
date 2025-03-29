# Create a program called sudoku_check_block. The program should have a function named block_ok that takes sudoku grid (matrix), row index (int), and column index (int) as arguments.
# The block_ok function should return True if the 3x3 block is ok. Otherwise, it should return False.
#  NB! The function should not modify the sudoku grid.
#  A 3x3 block is ok if each of the digits between 1 and 9 appears zero or one times in the block.
#  The block is not ok if any of the digits between 1 and 9 appears more than once in the block.
#  In a sudoku grid, the 3x3 blocks begin at the indexes (row_index, column_index)
# (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)

# NB!  If the block_ok function is called with any other combination of row and column, it should return False.
#  NB! Please copy/paste the code of the main function below to your program.


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


def main():
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 6],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
    ]
    print(block_ok(sudoku, row_index=0, column_index=0))
    print(block_ok(sudoku, row_index=3, column_index=6))
    print(block_ok(sudoku, row_index=6, column_index=3))


if __name__ == "__main__":
    main()
