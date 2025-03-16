# Create a program called lists_positive_sum. The program should have a function named positive_sum that takes a list as argument.
# The function should return the sum of positive values in the list. If there are no positive values in the list, the function should return zero.
# NB! The function should not modify the original list.
# The main function should first input five integers from the user and save them to a list.
# Then the main function should call the positive_sum function and finally print the return value of the positive_sum function.


def positive_sum(my_list):
    total_sum = 0
    for i in my_list:
        if i > 0:
            total_sum += i
    return total_sum


def main():
    my_list = []
    for i in range(5):
        num = int(input("Enter an integer: "))
        my_list.append(num)

    result = positive_sum(my_list)
    print()
    print(result)


main()
