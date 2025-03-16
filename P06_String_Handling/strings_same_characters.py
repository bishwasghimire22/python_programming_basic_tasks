# Create a program called strings_same_characters that inputs two strings.
# The program should first remove blanks from the strings and then detect if the strings contain exactly the same set of characters.
# The program should print "Same characters" if this is true. Otherwise, the program should print "Different characters".
# The characters are not required to be in the same order in both strings.
# For example, "A1234A" and "AA2413" contain the same set of characters. "BORROW" and "BROW" do not contain the same set of characters.
#
# NB! Slicing is not needed in this exercise.
# Hint: You should not write a loop in this exercise. After inputting two strings, you can check them in a single if statement.

first_str = input("Enter first string: ")
second_str = input("Enter second string: ")

first_str = first_str.replace(" ", "")
second_str = second_str.replace(" ", "")
if sorted(first_str) == sorted(second_str):
    print("Same characters")
else:
    print("Different characters")
