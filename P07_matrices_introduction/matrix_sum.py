# Create a program called matrix_sum. First, copy/paste the main function below to your program.
# Then write the print_matrix_sum function.
# The print_matrix_sum function should take two matrices as arguments and print the sum of the matrices.
#  You can suppose that the two matrices are always of the same size.


def main():
    m1 = [[1, 2, 0], [2, 3, 4]]
    m2 = [[3, 2, 5], [6, 4, 3]]
    m3 = [[1, 1, 1, 1], [3, 3, 2, 1], [2, 2, 2, 2]]
    m4 = [[2, 2, 2, 3], [2, 3, 1, 0], [1, 2, 3, 4]]

    print_matrix_sum(m1, m2)
    print()
    print_matrix_sum(m3, m4)


def print_matrix_sum(m1, m2):
    result = []

    for _ in range(len(m1)):
        row = [0] * len(m1[0])
        result.append(row)
    # result = [[0 for _ in range(len(m1[0]))] for _ in range(len(m1))]
    for r in range(len(m1)):
        for c in range(len(m1[r])):
            result[r][c] = m1[r][c] + m2[r][c]

    for r in result:
        print(*r, end=" ")
        print()


main()
