# Create a program called print_descending that first inputs an integer from the user. 
# Then, the program should print all integers between one and the inputted integer in descending
# order. The integers should be printed on a single line. 
# You should use the for loop in this exercise. 
# If there are no integers to be printed, then the program should print "Nothing to be printed". 
# Otherwise, the program should also print the sum of the integers as below.

num = int(input("Enter an integer: "))
sum = 0
if num <= 0:
    print("Nothing to be printed")
else:
    for i in range(num, 0, -1):
        print(i, end = " ")
        sum += i
    print(f"\nThe sum is {sum}")
