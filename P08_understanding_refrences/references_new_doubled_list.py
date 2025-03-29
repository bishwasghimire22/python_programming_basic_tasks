# Create a program called references_new_doubled_list.
# The program should have a function named new_doubled_list that takes a list of numbers as argument.
#  The new_doubled_list function should return a copy of the list where each number in the original list are multiplied by two.
#  First, copy/paste the main function below to your program. Then write the new_doubled_list function.


def new_doubled_list(num_list):
    return [num * 2 for num in num_list]


def main():
    first_list = [1, 2, 3, 4, 5, 6]
    second_list = new_doubled_list(first_list)
    print(first_list)
    print(second_list)


main()
