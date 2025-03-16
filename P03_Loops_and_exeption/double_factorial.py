#The double factorial of n is the product of all the integers from 1 up to n that have the same 
# parity (odd or even) as n. You can use an arithmetic operator to determine the parity of an 
# integer. 0!! is 1        5!! = 1 x 3 x 5 = 15       6!! = 1 x 2 x 4 x 6 = 48 Create a program 
# called double_factorial that inputs a non-negative integer from the user. 
# The program should display the double factorial of the inputted integer.
#  If the input value is negative, 
# the program should display "Please enter a non-negative integer". 

user_input = int(input("Enter a non-negative integer: "))

if user_input < 0:
    print("Please enter a non-negative integer")
else:
    if user_input == 0:
        print(f"{user_input}!! = {1}")
    else:
        result = 1
        if user_input % 2 == 0:
            for i in range(2, user_input + 1, 2):
                result *= i
            
        else:
            for i in range(1, user_input + 1, 2):
                result *= i
                
        print(f"{user_input}!! = {result}")