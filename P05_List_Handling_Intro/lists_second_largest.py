# Create a program called lists_second_largest. The program should have a function named second_largest that takes a list as argument.
#  The function should return a copy of the second largest value in the list.
# If the list has no values, or if it has only one distinct value, the function should return None.
#   NB! The function should not modify the original list.


def second_largest(mylist):
    unique_values = sorted(set(mylist))
    if len(unique_values) < 2:
        return None

    return unique_values[-2]


def main():
    pass


if __name__ == "__main__":
    main()
