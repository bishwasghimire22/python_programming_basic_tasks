# Create a program called functions_first. The program should have a function called print_powers that prints the first 20 powers of two to the console.
# Call the print_powers function from the main function.  Please use a for loop in your program.
def print_powers():
    for i in range(20):
        i = 2**i
        print(i, end=" ")


def main():
    print_powers()


main()
