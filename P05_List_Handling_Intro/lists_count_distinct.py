# Create a program called lists_count_distinct. The program should have a function named count_distinct that takes a list as argument.
# The function should return the count of distinct values in the list.  NB! The function should not modify the original list.
#  Hint:  There is no need to write any loop in this exercise.
# See also the 'Lists Surnames' exercise where you have already printed distinct surnames.


def count_distinct(mylist):
    return len(set(mylist))


def main():
    pass


if __name__ == "__main__":
    main()
