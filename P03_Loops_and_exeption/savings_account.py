# Create a program called savings_account to compute compound interest for the initial deposit
# in a savings account.  Assume that  • The interest rate does not change after the initial
# deposit • The capital income tax is subtracted from the interest before it is added to the
# balance. First, the program inputs interest rate (%), capital income tax rate (%), the initial
# deposit, and the number of years. Then, the program should print the balance of the account at
# the end of each year. Instruction • You should compute the result in a simple for loop where
# you keep adding the yearly interest to the balance. If you try to use some pre-defined compound
# interest formula, it might give you slightly different results.  • If the last decimal on some
# line in your program's output differs from the example output, then please change your
# calculation order. Then retry.
# In the example above, 35 is added to the balance at the end of
# the first year.
# 5 %  of  1000  is 50
# 30 %  of  50  is  15
# 50 - 15 = 35
# Note:  You are not required to validate any input in this exercise.

interest_rate = float(input("Enter interest rate: "))
income_tax = float(input("Enter capital income tax rate: "))
initial_deposit = float(input("Enter initial deposit: "))
num_years = int(input("Enter number of years: "))

total_balance = initial_deposit

print()

for i in range(num_years):

    interest_earn = interest_rate * total_balance / 100
    tax_paid = income_tax * interest_earn / 100
    net_interest = interest_earn - tax_paid
    total_balance = total_balance + net_interest
    print(f"Year {i+1}: {total_balance:.2f}")
