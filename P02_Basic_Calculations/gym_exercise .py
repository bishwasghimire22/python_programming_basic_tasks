# Create a program called gym_exercise that first inputs the number of days when the user 
# visits the local gym per year, the yearly membership fee, and the price of the day pass. 
# Then, the program should determine which one is the cheaper option 
# (paying the yearly membership fee or buying separate day passes) and how much cheaper it is. 
# The program should display one of the following texts: 
# Buying day passes is 99.00 euros cheaper 
# Paying the yearly membership fee is 99.00 euros cheaper 
# There is no price difference 

num_days = int(input("Enter the number of days of gym visits per year: "))
price = float(input("Enter price for a day pass: "))
yearly_membership = float(input("Enter yearly membership fee: "))

price_without_membership = price * num_days

print()
if yearly_membership > price_without_membership:
    print(f"Buying day passes is {yearly_membership-price_without_membership:.2f} euros cheaper")
elif yearly_membership < price_without_membership:
    print(f"Paying the yearly membership fee is {price_without_membership-yearly_membership:.2f} euros cheaper")
else:
    print(f"There is no price difference")
    
