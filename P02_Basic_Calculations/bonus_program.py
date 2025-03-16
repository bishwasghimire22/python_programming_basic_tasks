# Create a program called bonus_program that first inputs the selling price of a car from 
# the user. Then, the program should calculate the salesperson's bonus with two decimals. 
# The sales bonus is 1 % of the selling price if the car costs less than 50000. 
# Otherwise, the bonus is 1,5 % of the selling price. The minimum bonus is 200 euros. 
# For example, if the selling price is 18000 euros, then the bonus is 200 euros. 
# If the selling price is 25000 euros, then 
# the bonus is 250 euros. If the selling price is 60000 euros, then the bonus is 900 euros.
 
selling_price = float(input("Enter the car's selling price: "))

if selling_price < 50000 and selling_price >18000:    
    sales_bonus = selling_price * 0.01
elif selling_price >=50000:
    sales_bonus = selling_price * 0.015
else:
    sales_bonus = min_bonus

print(f"The bonus is {sales_bonus:.2f} euros.")