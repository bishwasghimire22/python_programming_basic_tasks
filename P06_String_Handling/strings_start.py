# Create a program called strings_start that first inputs a string from the user. Then the program should print the following:
# the string in all small letters,
#  the string in all capital letters,
#  and the length of the string.

user_input = input("Enter a string: ")
print()
print(user_input.lower())
print(user_input.upper())
print(f"{len(user_input)} characters")
