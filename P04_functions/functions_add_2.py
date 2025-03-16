# Create a program called functions_add_2. Copy/paste all the code from your functions_add program to the new program. Then modify the new program as follows:
# if __name__ == "__main__":
#    main()
# In addition to running the functions_add_2 program normally, we can now do some unit testing where the
# test module calls your add function without running your program.
# Please copy/paste your code to Viope.This time, when you click on the Run button,
# Viope runs the test module and Viope shows the unit test report (instead of your program's normal output) in the test execution console.
# Therefore, we do not have the example output in this exercise description.
# NB! The test module (not your program) prints the output you see below.


def add(num1: float, num2: float):
    return round(int(num1 + num2 + 0.5))


def main():
    num1 = float(input("Enter a float: "))
    num2 = float(input("Enter a float: "))

    result = add(num1, num2)
    print(result)


if __name__ == "__main__":
    main()
