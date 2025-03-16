# Create a program called functions_third. The program should have a function called compute_discount
# that takes price in euros and discount percentage as arguments.
# The function should compute and return the amount of discount in euros.
# The main function should first input price in euros and discount percentage from the user and then
# call the compute_discount function with the inputted values.
# Finally, the main function should print the discount in euros.
# NB! The compute_discount function should not print anything.


def compute_discount(price: float, discount: float):
    discount = price * discount / 100
    return discount


def main():
    price = float(input("Enter price: "))
    discount = float(input("Enter discount percentage: "))
    total_discount = compute_discount(price, discount)
    print(f"The discount is {total_discount:.2f} euros")


main()
