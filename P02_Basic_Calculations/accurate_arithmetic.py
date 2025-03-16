# Create a program called accurate_arithmetic that first inputs two decimal numbers from the user.
# Then, the program should print the sum of the decimal numbers as shown in the example output. 
# You are not required to set the number of decimal places in the output.
# Note 
# • Please do not be too surprised, if your code fails a couple of times in Viope testing before
# you have finished it. 
# • Please study the course materials carefully to see how you can perform exact computations on
# decimal values.  
from decimal import Decimal
num1 = Decimal(input("Enter first number: "))
num2 = Decimal(input("Enter second number: "))

result = Decimal(num1 + num2)

print(f"\n{num1} + {num2} = {result}")
