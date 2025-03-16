# Create a program called strings_box that first inputs a string.
# Then the program should print the inputted string in a in a "box" as shown in the example output.
# NB! You should not write a loop in your program.Example output:

# Enter a string: Hello
### ---------
### | Hello |
### ---------

user_input = input("Enter a string: ")
inputted = "| " + user_input + " |"

print(f"{len(inputted) * "-"}")
print(f"{inputted}")
print(f"{len(inputted) * "-"}")
