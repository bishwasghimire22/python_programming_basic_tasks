# Create a program called check_integer that asks the user to enter an integer. 
# If the inputted value cannot be converted to an integer, the program should print the 
# inputted text enclosed in single quotes and "is not an integer". Otherwise, the program should
# print "OK".  NB! Please  use exception handling in this exercise. 
# Hint:  To be able to print an invalid value, 
# you should assign the inputted string to a separate variable before trying to convert
# it to an integer.  
num = input("Enter an integer: ")
try:
    int(num)
    print("OK")
except ValueError:
    print(f"'{num}' is not an integer")