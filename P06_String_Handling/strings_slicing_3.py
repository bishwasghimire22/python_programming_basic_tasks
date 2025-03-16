# Create a program called strings_slicing_3 that first inputs a string.
# Then the program should print all substrings of the string,
#  which start from the first position in the string.
#  The substrings should be printed as shown in the example output.
# NB!  You should use slicing in this exercise.
# Hint: A loop is useful here.

user_input = input("Enter a string: ")
i = 0

while i < len(user_input):
    print(user_input[: i + 1])
    i += 1
