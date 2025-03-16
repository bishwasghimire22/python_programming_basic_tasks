# Create a program called strings_digit_sum that first inputs a string from the user.
# Then the program should print the sum of all digits that are included in the inputted string.
# If there are no digits in the string, the program should print 0.

user_input = input("Enter a string: ")

digit_sum = 0
for c in user_input:
    if c.isdigi():
        digit_sum += int(c)

print(f"The sum of digits is {digit_sum}")
