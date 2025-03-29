# Create a program called matrix_count_occurrences. The program should have a function named count_occurrences,
# which takes a matrix (two-dimensional array) and an integer as its arguments.
# The function should return the count of occurrences of the integer in the matrix.
#  First, copy/paste the main function below to your program.
# Then write the count_occurrences function.
#
#


def main():
    m = [[1, 2, 3], [1, 2, 2], [1, 1, 1], [1, 2, 1]]
    print(count_occurrences(m, 1))
    print(count_occurrences(m, 2))
    print(count_occurrences(m, 5))


def count_occurrences(m, num):
    count = 0

    for row in m:
        for col in row:
            if col == num:
                count += 1

    return count


main()
