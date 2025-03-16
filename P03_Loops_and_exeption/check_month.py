# Create a program called check_month that inputs a month number from the user. 
# If the input is a valid month number, the program should print "OK".
# Otherwise, the program should print the entered value and "is not a valid month number"
# and prompt a month number again. The program should keep asking month numbers until 
# the user enters a valid month number.  
# NB! Please use exception handling in this exercise. 

while True:
    day_of_month = input("Enter a month number: ")
    try:
        month_num = int(day_of_month)
        if 1 <= month_num <= 12:
            print("OK")
            break
        else:
            print(f"{month_num} is not a valid month number\n")
    except ValueError:
        print(f"'{day_of_month}' is not a valid month number\n")

