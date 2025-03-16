# Create a program called strings_subset that first inputs two strings from the user.
# The program should check if all the characters in the second string are included in the first string.
# The program should print "Subset" if this is true.
#  Otherwise, the program should print "Not subset".
# If the second string is empty, the program should print "Nothing to be checked".
# Hint:  A boolean variable (initalised to True) and a loop is useful in this exercise.

first_str = input("Enter first string: ")
second_str = input("Enter second string: ")

if second_str == "":
    print("Nothing to be checked")
else:
    is_subset = True
    for c in second_str:
        if c not in first_str:
            is_subset = False
    if is_subset:
        print("Subset")
    else:
        print("Not subset")
