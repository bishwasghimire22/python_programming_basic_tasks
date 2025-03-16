# Create a program called strings_slicing_2 that first inputs a string.
# Then the program should print the next to last character in the string.
#  If the string has less than two characters, the program should print "Too short string".
# NB! You should use slicing in this exercise.

user_input = input("Enter a string: ")

if len(user_input) < 2:
    print("Too short string")
else:
    print(user_input[-2])
