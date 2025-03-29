# Create a program called lists_remove_min_max.
# The program should have a function named remove_min_max that takes a list as argument.
#  The function should remove the smallest and the largest value in the list.
#  Note: The function should be able to handle an empty list and a list that has only one element.
#   First, copy/paste the main function below to your program. Then write the remove_min_max   function.


def remove_min_max(my_list: list):
    if len(my_list) <= 1:
        my_list.clear()
        return
    small = min(my_list)
    big = max(my_list)

    my_list.remove(small)
    my_list.remove(big)

    return my_list.sort()


def main():
    a = [3, 1, 4, 1, 5]
    remove_min_max(a)
    print(a)


if __name__ == "__main__":
    main()
