# Create a program called lists_remove_successive_duplicates. The program should have a function named remove_successive_duplicates that takes a list as argument.
#  The function should remove successive duplicates from the original list.  We have a successive duplicate when two identical values exist one after each other in the list.
#  Original list:  [3, 1, 1, 2, 1, 2, 2, 2, 3]
#  After the successive duplicates have been removed: [3, 1, 2, 1, 2, 3]
# NB! This time, the function should modify the original list instead of returning a reference to a new list.


def remove_successive_duplicates(my_list):
    if not my_list:
        return None
    i = 0
    while i < len(my_list) - 1:
        if my_list[i] == my_list[i + 1]:
            my_list.pop(my_list[i])
        else:
            i += 1
