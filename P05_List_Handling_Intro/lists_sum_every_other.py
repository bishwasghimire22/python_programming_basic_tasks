# Create a program called lists_sum_every_other. The program should have a function named sum_every_other that takes a list as argument.
# The function should return the sum of every other value starting from the first value in the list. If the list is empty, the function should return None.
# In Python, None is a keyword that represents null (no value at all)2.
# NB! The function should not modify the original list.


def sum_every_other(mylist):
    if not mylist:
        return None

    total_sum = 0
    for i in range(0, len(mylist), 2):
        total_sum += mylist[i]
    return total_sum


def main():
    mylist = []
    print(sum_every_other(mylist), mylist)


if __name__ == "__main__":
    main()
