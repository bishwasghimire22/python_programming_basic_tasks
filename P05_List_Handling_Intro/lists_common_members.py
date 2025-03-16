# Create a program called lists_common_members. The program should have a function named common_members that takes two lists as arguments.
# The function should return True if the lists have at least one common member. Otherwise, the function should return False.
#  NB! The function should not modify the original lists.
# Hint:  In this exercise, you can solve the problem by writing a loop.


def common_members(list1, list2):
    for i in list1:
        if i in list2:
            return True

    return False


def main():
    pass


if __name__ == "__main__":
    main()
