# Create a program called functions_pyramid. The program should have a function called print_pyramid that takes the height of the pyramid as argument.
# The function should print a pyramid using the character "*" as shown in the example output.
# The main function should first input the height of the pyramid and then call the print_pyramid function with the inputted values.
# Hint: print(5 * "X") prints XXXXX
# If we take advantage of this operation, the whole loop that prints the pyramid can be written on two lines of code.


def print_pyramid(height: int):
    i = 1
    while i <= height:
        print(" " * (height - i) + "*" * (2 * i - 1))
        i += 1


def main():
    height = int(input("Enter pyramid height: "))
    print_pyramid(height)


main()
