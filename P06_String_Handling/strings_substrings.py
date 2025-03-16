# Create a program called strings_substrings that first inputs a string and a character from the user.
#  The program should examine the inputted string and print all 4-character substrings,
# which start with the inputted character.
# If no such substring exists in the string, the program should not print anything more.

# Note: Substrings can overlap.
# Hint: Slicing is useful in this exercise.

str_input = input("Enter a string: ")
chr_input = input("Enter a character: ")

for i in range(len(str_input) - 3):
    if str_input[i] == chr_input:
        print(str_input[i : i + 4])
