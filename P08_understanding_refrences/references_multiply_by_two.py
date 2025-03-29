# Create a program called references_multiply_by_two.
#  The program should have a function named multiply_by_two that takes a list of numbers as argument.
# The multiply_by_two function should multiply each number in the list by two.
#  First, copy/paste the main function below to your program.
# Then write the multiply_by_two function.


def multiply_by_two(num_list):
    for i in range(len(num_list)):
        num_list[i] *= 2


def main():
    numbers = [1, 2, 3, 4, 5, 6]
    more_numbers = [10, 20, 30]

    print(numbers)
    multiply_by_two(numbers)
    print(numbers)

    print(more_numbers)
    multiply_by_two(more_numbers)
    print(more_numbers)


main()
