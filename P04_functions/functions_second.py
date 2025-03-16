# Create a program called functions_second. The program should have a function called print_rectangle
# that takes the height and width of a rectangle as arguments.
# The function should print a rectangle using the character "*" as shown in the example output.
# The main function should first input the height and width of a rectangle
# and then then call the print_rectangle function with the inputted values.


def print_rectangle(height: int, width: int):
    for h in range(height):
        for w in range(width):
            print("*", end="")
        print("")


height = int(input("Enter height: "))
width = int(input("Enter width: "))


def main():
    print_rectangle(height, width)


main()
