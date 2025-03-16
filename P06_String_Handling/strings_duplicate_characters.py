# Create a program called strings_duplicate_characters that first inputs a string from the user.
# The program should check if any character occurs more than once in the string. If there are no duplicate characters in the string,
# the program should print "No duplicates". Otherwise, the program should print "Contains duplicate(s)".

# NB! You should not write a loop is here. We can solve this problem using a set.

user_input = input("Enter a string: ")

if sorted(user_input) == sorted(set(user_input)):
    print("No duplicates")

else:
    print("Contains duplicate(s)")
