# Create a program called tuples_return.
# The program should have a function named pow_2_3 that takes an integer as argument.
# The function should compute the second power and the third power of the integer and return them in a tuple.
#  First, copy/paste the main function below to your program.
#  Then write the pow_2_3  function.
def pow_2_3(num):
    my_tuple = (num**2, num**3)
    return my_tuple


def main():
    x = int(input("Enter an integer: "))
    p2, p3 = pow_2_3(x)
    print(p2)
    print(p3)


if __name__ == "__main__":
    main()
