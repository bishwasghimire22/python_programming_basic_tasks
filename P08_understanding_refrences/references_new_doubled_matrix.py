# Create a program called references_new_doubled_matrix.
# The program should have a function named new_doubled_matrix that takes a matrix as argument.
#  The matrix contains numbers.
# The new_doubled_matrix function should return a copy of the matrix where each number in the original matrix are multiplied by two.
#  First, copy/paste the main function below to your program. Then write the new_doubled_matrix function.


def new_doubled_matrix(matrix):
    new_matrix = []

    for row in matrix:
        new_row = []
        for col in row:
            col *= 2
            new_row.append(col)

        new_matrix.append(new_row)
    return new_matrix


def main():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = new_doubled_matrix(m1)
    print(m1)
    print(m2)


main()
