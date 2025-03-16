# Create a program called check_weekday_number that inputs a weekday number from the user. 
# If the inputted value is not valid weekday number, the program should print 
# "Please enter an integer between 1 and 7". Otherwise, the program should print "OK".  
# NB! Please use exception handling in this exercise. 

weekday = input("Enter a weekday number: ")

try:
    weekday = int(weekday)
    if weekday >=1 and weekday <=7:
        print("OK")
    else:
        print("Please enter an integer between 1 and 7")
except:
    print("Please enter an integer between 1 and 7")