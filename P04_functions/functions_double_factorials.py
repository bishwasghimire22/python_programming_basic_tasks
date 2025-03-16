# Create a program called functions_double_factorials. The program should have a function called double_factorial
#  that takes an integer as argument and returns the double factorial of the integer.
# See the previous "Double Factorial" exercise for more details.
#  The double_factorial function should not print anything.
# The main function should print double factorials of 0 – 9 as shown in the example output.
#  To determine the double factorial of each number, the main function should call the double_factorial function.
#  Please use the for loop in the main function.


def double_factorial(num):
    if num == 0:
        return 1
    result = 1
    if num % 2 == 0:
        for i in range(2, num + 1, 2):
            result *= i
    else:
        for i in range(1, num + 1, 2):
            result *= i

    return result


def main():
    for i in range(10):
        result = double_factorial(i)
        print(f"{i}!! = {result}")


main()
