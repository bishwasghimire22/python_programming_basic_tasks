#Create a program called price_plus_vat that first inputs the price from the user. 
# Then the program should print the price with Value Added Tax (VAT) added with two decimal places as 
# shown in the example output. Suppose that VAT is always 24 %.
#If the program fails to convert the input to a float, it should print "Invalid price".
#  NB! You should use  exception handling in this exercise.
vat = 0.24
try:
    price = float(input("Enter price: "))
    print(f"The price with VAT is {price * vat + price:.2f}")
except:
    print("Invalid price")